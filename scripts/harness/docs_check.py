#!/usr/bin/env python3
"""second-brain（OKF 文書群）の決まりのうち、機械的に判定できるものを確かめる。

使い方:
    python3 scripts/harness/docs_check.py              # second-brain 全体（unreviewed/ 等を除く）
    python3 scripts/harness/docs_check.py <ディレクトリ>  # 指定したディレクトリの下だけ

決まりの正は references/documentation/open-knowledge-format-spec.md と knowledge/documentation/document-structure.md である。
問題があれば終了コード 1 を返す。期限切れ（stale_after）は警告だけで、終了コードには含めない。
"""

import re
import sys
from datetime import datetime, timezone
from pathlib import Path

KEYS = ["type", "title", "description", "tags", "status", "verified", "stale_after"]
TYPES = {"spec", "guideline", "architecture", "database-schema", "decision", "reference"}
STATUSES = {"draft", "stable", "deprecated"}
RESERVED = {"index.md", "log.md"}
LINK = re.compile(r"\]\(([^)\s]+)\)")
INDEX_ITEM = re.compile(r"^[-*] \[[^\]]*\]\(([^)\s]+)\) - (.+)$")

BUNDLE_ROOTS = ("second-brain", "docs")
NON_DOC_DIRS = {"scripts", ".git", ".claude", ".agents", ".local", "__pycache__"}


def bundle_parts(path: Path) -> tuple[str, ...]:
    """second-brain/（または docs/）からの相対パスの各部分。unreviewed/ の下なら、移動先の場所として返す。"""
    parts = path.resolve().parts
    for root_name in BUNDLE_ROOTS:
        if root_name in parts:
            rest = parts[len(parts) - parts[::-1].index(root_name) :]
            return rest[1:] if rest[:1] == ("unreviewed",) else rest
    return ()


def unreviewed_root(directory: Path) -> Path | None:
    """directory が second-brain/unreviewed/（または docs/unreviewed/）の下にあれば、その unreviewed/ を返す。"""
    for candidate in [directory, *directory.parents]:
        if candidate.name == "unreviewed" and candidate.parent.resolve().name in BUNDLE_ROOTS:
            return candidate
    return None


def is_ignored_dir(directory: Path, root: Path) -> bool:
    """OKF 文書ではないディレクトリ（scripts/ や隠しディレクトリ等）かを判定する。"""
    try:
        rel_parts = directory.resolve().relative_to(root.resolve()).parts
    except ValueError:
        rel_parts = ()
    return any(part in NON_DOC_DIRS or part.startswith(".") for part in rel_parts)


def frontmatter(text: str) -> dict[str, str] | None:
    """先頭の --- で囲まれた部分を、トップレベルの key: value として読む。無ければ None。"""
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 4)
    if end == -1:
        return None
    fields = {}
    for line in text[4:end].splitlines():
        key, sep, value = line.partition(":")
        if sep and not line.startswith(" "):
            fields[key.strip()] = value.strip().strip("'\"")
    return fields


def check_doc(path: Path, text: str, errors: list[str], warnings: list[str]) -> None:
    fields = frontmatter(text)
    if fields is None:
        errors.append(f"{path}: Frontmatter がない")
        return
    present = [k for k in fields if k in KEYS]
    missing = [k for k in KEYS if k not in fields]
    if missing:
        errors.append(f"{path}: Frontmatter に {', '.join(missing)} がない")
    elif present != KEYS:
        errors.append(f"{path}: Frontmatter のキーの順番が決まりと違う")
    if fields.get("type") and fields["type"] not in TYPES:
        errors.append(f"{path}: type '{fields['type']}' は決まりの 6 種に無い")
    if fields.get("status") and fields["status"] not in STATUSES:
        errors.append(f"{path}: status '{fields['status']}' は draft / stable / deprecated に無い")

    h1 = re.search(r"^# (.+)$", text, re.M)
    if h1 and fields.get("title") and h1.group(1).strip() != fields["title"]:
        errors.append(f"{path}: H1 と title が違う")

    try:
        if datetime.fromisoformat(fields.get("stale_after", "")) < datetime.now(timezone.utc):
            warnings.append(f"{path}: stale_after を過ぎている。内容を確かめ直す")
    except ValueError:
        errors.append(f"{path}: stale_after が日時として読めない")

    body = re.sub(r"```.*?```", "", text, flags=re.S)
    for target in LINK.findall(body):
        if target.startswith(("/", "http", "#", "mailto:", "../")):
            continue
        if target.split("#")[0].endswith(".md"):
            errors.append(f"{path}: docs 内へのリンク '{target}' は / 始まりで書く")

    # knowledge/ と references/ は、プロジェクト固有の文書に依存しない。
    if bundle_parts(path)[:1] in (("knowledge",), ("references",)):
        for target in LINK.findall(body):
            if target.startswith("/") and not target.startswith(("/knowledge/", "/references/")):
                errors.append(f"{path}: プロジェクト固有の文書 '{target}' へリンクしている")


def check_index(index: Path, errors: list[str]) -> None:
    """目次の各項目の説明文が、リンク先の description と同じかを確かめる。"""
    for line in index.read_text(encoding="utf-8").splitlines():
        item = INDEX_ITEM.match(line)
        if not item or not item.group(1).endswith(".md"):
            continue
        target = index.parent / item.group(1)
        fields = frontmatter(target.read_text(encoding="utf-8")) if target.exists() else None
        if fields and fields.get("description") and item.group(2).strip() != fields["description"]:
            errors.append(f"{index}: '{item.group(1)}' の説明文が description と違う")


def check_tree(root: Path, errors: list[str], warnings: list[str]) -> None:
    resolved_root = root.resolve()
    skip = resolved_root / "unreviewed" if resolved_root.name in BUNDLE_ROOTS else None
    for directory in [root, *sorted(p for p in root.rglob("*") if p.is_dir())]:
        resolved_dir = directory.resolve()
        if is_ignored_dir(directory, root):
            continue
        if skip and (resolved_dir == skip or skip in resolved_dir.parents):
            continue
        docs = sorted(p for p in directory.glob("*.md") if p.name not in RESERVED)
        index = directory / "index.md"
        if not index.exists():
            unreviewed = unreviewed_root(directory)
            if unreviewed is None:
                has_doc_subdirs = any(
                    p.is_dir() and not is_ignored_dir(p, root) for p in directory.iterdir()
                )
                if docs or has_doc_subdirs:
                    errors.append(f"{directory}: index.md がない")
                continue
            # unreviewed/ の下は、目次を unreviewed/index.md の 1 か所にまとめる運用である。
            index = unreviewed / "index.md"
        else:
            check_index(index, errors)
        listed = {
            (index.parent / target).resolve()
            for target in LINK.findall(index.read_text(encoding="utf-8"))
        }
        for doc in docs:
            check_doc(doc, doc.read_text(encoding="utf-8"), errors, warnings)
            if doc.resolve() not in listed:
                errors.append(f"{doc}: {index} から辿れない")


def default_bundle_root() -> Path:
    """引数省略時の既定ディレクトリを返す（スクリプト自身の親である second-brain、またはカレント基準）。"""
    script_repo = Path(__file__).resolve().parents[2]
    if (script_repo / "index.md").exists():
        return script_repo
    if Path("second-brain").exists():
        return Path("second-brain")
    return Path("docs")


def main() -> int:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else default_bundle_root()
    errors: list[str] = []
    warnings: list[str] = []
    check_tree(root, errors, warnings)
    for message in warnings:
        print(f"警告: {message}")
    for message in errors:
        print(f"問題: {message}")
    print(f"\n問題 {len(errors)} 件、警告 {len(warnings)} 件")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
