#!/usr/bin/env python3
"""Technology Radar の要約 (象限ごとの Markdown) から、対話型のレーダーページを生成する。

使い方:
    python3 scripts/radar/build_radar.py references/ai/thoughtworks-technology-radar-vol-35 -o radar.html

入力のディレクトリにある *-techniques.md / *-platforms.md / *-tools.md / *-languages-and-frameworks.md を読む。
各ファイルの "## Adopt" などの見出しがリング、"### 1. 名前" の見出しが 1 項目になる。
要約ファイルは読むだけで書き換えない。
"""

import argparse
import json
import math
import re
import sys
from pathlib import Path

QUADRANTS = [
    # (id, 表示名, ファイル名の末尾, 角度の開始 (度、y 軸は上向き))
    ("techniques", "Techniques", "techniques", 90),
    ("platforms", "Platforms", "platforms", 0),
    ("tools", "Tools", "tools", 180),
    ("languages-and-frameworks", "Languages & frameworks", "languages-and-frameworks", 270),
]
RINGS = ["adopt", "trial", "assess", "caution"]
# 各リングの内側と外側の半径 (最外周を 1 とする)
RING_EDGES = [0.0, 0.34, 0.6, 0.83, 1.0]
RADIUS = 470  # SVG の座標系での最外周
DOT_SPACING = 25  # 点どうしの最小間隔 (SVG の単位)
ANGLE_MARGIN = 4  # 象限の境界線からあける角度 (度)

BLIP_HEADING = re.compile(r"^### (\d+)\. (.+)$")
RING_HEADING = re.compile(r"^## (Adopt|Trial|Assess|Caution)\s*$")


def parse_quadrant(path: Path, quadrant: str) -> list[dict]:
    """1 つの象限の要約を読み、項目の一覧を返す。"""
    blips: list[dict] = []
    ring = None
    current = None
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            match = RING_HEADING.match(line)
            ring = match.group(1).lower() if match else None
            current = None
            continue
        match = BLIP_HEADING.match(line)
        if match and ring:
            current = {
                "number": int(match.group(1)),
                "name": match.group(2).strip(),
                "quadrant": quadrant,
                "ring": ring,
                "bullets": [],
            }
            blips.append(current)
            continue
        if current is None:
            continue
        if line.startswith("- "):
            current["bullets"].append(line[2:].strip())
        elif line.startswith("  ") and line.strip() and current["bullets"]:
            current["bullets"][-1] += line.strip()
    return blips


def aliases(name: str) -> list[str]:
    """項目名と、括弧内の略称 (例: "Agent Client Protocol (ACP)" → ACP) を返す。"""
    match = re.match(r"^(.+?)\s*\((.+)\)$", name)
    if match:
        return [name, match.group(1), match.group(2)]
    return [name]


def mention_pattern(blips: list[dict]) -> tuple[re.Pattern, dict[str, int]]:
    """本文中の項目名を見つける正規表現と、見つけた文字列から番号への対応を作る。"""
    lookup: dict[str, int] = {}
    for blip in blips:
        for alias in aliases(blip["name"]):
            lookup[alias.lower()] = blip["number"]
    # 長い名前を先に試し、"Agent Plugins" と "Agent Plugins を…" のような重なりを防ぐ。
    names = sorted(lookup, key=len, reverse=True)
    body = "|".join(re.escape(n) for n in names)
    pattern = re.compile(rf"(?<![A-Za-z0-9/])({body})(?![A-Za-z0-9])", re.IGNORECASE)
    return pattern, lookup


def segments(text: str, own: int, pattern: re.Pattern, lookup: dict[str, int]) -> list:
    """1 つの箇条書きを、文字列・コード・他の項目へのリンクの並びに分ける。"""
    result: list = []
    for i, part in enumerate(text.split("`")):
        if i % 2 == 1:
            result.append({"code": part})
            continue
        pos = 0
        for match in pattern.finditer(part):
            word = match.group(1)
            number = lookup[word.lower()]
            # 4 文字以下の名前 (Act、Pi、GLM など) は、大文字小文字まで一致したときだけリンクにする。
            exact = word in aliases(BLIPS_BY_NUMBER[number]["name"])
            if number == own or (len(word) <= 4 and not exact):
                continue
            if match.start() > pos:
                result.append(part[pos:match.start()])
            result.append({"n": number, "t": word})
            pos = match.end()
        if pos < len(part):
            result.append(part[pos:])
    return result


def place_blips(blips: list[dict]) -> None:
    """象限とリングごとに、点が重ならないよう角度と半径を決める。同じ入力なら同じ位置になる。"""
    for q_id, _, _, start in QUADRANTS:
        for ring_index, ring in enumerate(RINGS):
            group = sorted(
                (b for b in blips if b["quadrant"] == q_id and b["ring"] == ring),
                key=lambda b: b["number"],
            )
            if not group:
                continue
            inner = RING_EDGES[ring_index] * RADIUS + DOT_SPACING * 0.7
            outer = RING_EDGES[ring_index + 1] * RADIUS - DOT_SPACING * 0.7
            if ring_index == 0:
                inner = max(inner, DOT_SPACING * 2.2)
            span = math.radians(90 - 2 * ANGLE_MARGIN)
            # 1 行に並べきれなければ、リングの中で行 (同心円) を増やす。
            rows = 1
            while True:
                radii = [inner + (outer - inner) * (k + 0.5) / rows for k in range(rows)]
                capacity = [max(1, int(r * span / DOT_SPACING)) for r in radii]
                if sum(capacity) >= len(group) or rows >= 4:
                    break
                rows += 1
            total = sum(capacity)
            counts = [round(len(group) * c / total) for c in capacity]
            counts[-1] = len(group) - sum(counts[:-1])
            index = 0
            for row, (r, count) in enumerate(zip(radii, counts)):
                for k in range(count):
                    # 行ごとに半ステップずらし、隣の行の点と並ばないようにする。
                    offset = 0.5 if row % 2 == 0 else 0.25
                    fraction = (k + offset) / count if count else 0.5
                    angle = math.radians(start + ANGLE_MARGIN) + span * fraction
                    blip = group[index]
                    blip["x"] = round(r * math.cos(angle), 1)
                    blip["y"] = round(-r * math.sin(angle), 1)
                    index += 1


def find_quadrant_file(directory: Path, suffix: str) -> Path:
    matches = sorted(directory.glob(f"*-{suffix}.md"))
    matches = [m for m in matches if not (suffix == "tools" and m.name.endswith("-languages-and-frameworks.md"))]
    if len(matches) != 1:
        sys.exit(f"{directory} に *-{suffix}.md が 1 つだけあるはずが、{len(matches)} 個ある")
    return matches[0]


BLIPS_BY_NUMBER: list = []


def main() -> int:
    global BLIPS_BY_NUMBER
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("directory", type=Path, help="象限ごとの要約があるディレクトリ")
    parser.add_argument("-o", "--output", type=Path, default=Path("radar.html"))
    parser.add_argument("--volume", default="35")
    parser.add_argument("--date", default="2026-11")
    args = parser.parse_args()

    blips: list[dict] = []
    for q_id, _, suffix, _ in QUADRANTS:
        blips += parse_quadrant(find_quadrant_file(args.directory, suffix), q_id)
    blips.sort(key=lambda b: b["number"])
    numbers = [b["number"] for b in blips]
    if numbers != list(range(1, len(blips) + 1)):
        sys.exit("項目の番号が 1 から連続していない")
    BLIPS_BY_NUMBER = [None] + blips

    pattern, lookup = mention_pattern(blips)
    for blip in blips:
        blip["text"] = [segments(t, blip["number"], pattern, lookup) for t in blip.pop("bullets")]
        mentions: list[int] = []
        for bullet in blip["text"]:
            for seg in bullet:
                if isinstance(seg, dict) and "n" in seg and seg["n"] not in mentions:
                    mentions.append(seg["n"])
        blip["mentions"] = mentions
    place_blips(blips)

    data = {
        "volume": args.volume,
        "date": args.date,
        "radius": RADIUS,
        "ringEdges": RING_EDGES,
        "quadrants": [{"id": q, "label": label, "start": start} for q, label, _, start in QUADRANTS],
        "blips": blips,
    }
    payload = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("<", "\\u003c")
    template = (Path(__file__).parent / "radar_template.html").read_text(encoding="utf-8")
    if "/*__RADAR_DATA__*/null" not in template:
        sys.exit("テンプレートにデータの差し込み位置が無い")
    html = template.replace("/*__RADAR_DATA__*/null", payload).replace("__VOLUME__", args.volume)
    args.output.write_text(html, encoding="utf-8")
    print(f"{args.output}: {len(blips)} 項目、{len(html.encode('utf-8')) // 1024} KB")
    return 0


if __name__ == "__main__":
    sys.exit(main())
