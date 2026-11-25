---
type: guideline
title: 'Orca の worktree を Dev Container のマウントの中に置く'
description: 'Orca が Dev Container の中に作る git worktree を、シンボリックリンクでマウントの中（リポジトリの兄弟ディレクトリ）に置く方法と、作った後にやること、片付け方、使うときの注意。'
tags: [git-worktree, devcontainer, orca, git]
status: draft
verified: { by: claude-code/claude-opus-5-5, at: 2026-11-25T00:00:00Z }
stale_after: 2027-11-25T00:00:00Z
---

# Orca の worktree を Dev Container のマウントの中に置く

Orca で Dev Container に SSH 接続して worktree を作ると、worktree はマウントの外に置かれる。
Orca の置き場所をシンボリックリンクでマウントの中に向けると、worktree がリポジトリの兄弟ディレクトリ（`/home/vscode/work/<名前>`）に置かれ、ホストからも開けて、作り直しても消えない。
前提の構成は [親ディレクトリをマウントする Dev Container の構成](/knowledge/devcontainer/parent-directory-mount.md) を、worktree そのものの仕組みは [git worktree の仕組みと扱い方](/knowledge/git/worktree.md) を参照する。

## Orca で作る

1. Orca から Dev Container へ SSH 接続で開く。
   Windows 側のパス（`\\wsl.localhost\...`）で開くと、worktree がリポジトリの中に入れ子で作られる。
   手順は [Orca で Dev Container を開くときのトラブル対処](/knowledge/devcontainer/orca-troubleshooting.md) を参照する。
1. Orca で worktree を作る。
1. 作った worktree で依存をインストールする（`pnpm install` など）。
   worktree には `node_modules` のような追跡していないファイルがないためである。
   パッケージのストアをマウントの中で共有していれば、ダウンロードはほとんど起きない。

## マウントの中に置くリンク

Orca は、SSH 接続先では `~/orca/workspaces/<repo>/<名前>` に worktree を作る。
ここはマウントの外なので、そのままではホストから見えず、コンテナを作り直すと消える。
Orca の設定で作成先を変えられるかは確認できていない。
そこで `~/orca/workspaces/<repo>` を、マウントされた `/home/vscode/work` へのシンボリックリンクにする。

リンクは、コミットしない `.devcontainer/post-create.local.sh` に書く。
ひな形として `.devcontainer/post-create.local.sh.example` をコミットしておき、使う人がコピーしてからコンテナを作り直す。

```bash
#!/usr/bin/env bash
set -euo pipefail

# Orca は ~/orca/workspaces/<リポジトリ名>/<名前> に作るので、<リポジトリ名> をマウントの中へのリンクにする
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"
PARENT_DIR="$(dirname "${REPO_DIR}")"
ORCA_DIR="${HOME}/orca/workspaces"
LINK="${ORCA_DIR}/$(basename "${REPO_DIR}")"

mkdir -p "${ORCA_DIR}"
if [ -L "${LINK}" ]; then
    :
elif [ -e "${LINK}" ]; then
    echo "${LINK} は普通のディレクトリなので、リンクにしない" >&2
else
    ln -s "${PARENT_DIR}" "${LINK}"
fi
```

```bash
cp .devcontainer/post-create.local.sh.example .devcontainer/post-create.local.sh
```

- `~/orca/workspaces` そのものはリンクにしない。
  `/home/vscode/work` へのリンクにすると、worktree がリポジトリの中（`/home/vscode/work/<repo>/<名前>`）に置かれてしまう。
- git は相対パスを、リンク先の実際のパスから記録する（例: `gitdir: ../<repo>/.git/worktrees/<名前>`）。
  そのため、ホストから開いても結びつきが切れない。
- Orca は作成中の worktree を `~/orca/workspaces/.orca-preparing` に置く。
  ここはコンテナの中のままでよく、作り終えた worktree はマウントの中へ移った（2026-11-21 に確認した）。
- Orca が覚えている古いパス（`~/orca/workspaces/<repo>/<名前>`）は、リンクを通って新しい場所に届くので、そのまま開ける。

### 普通のディレクトリになっているときに移す

すでに `~/orca/workspaces/<repo>` が普通のディレクトリになっているコンテナでは、1 回だけ手で移す。
移す先に同じ名前のディレクトリがないことを先に確かめ、Orca が worktree を作っている最中には行わない。

```bash
cd ~/orca/workspaces
mv <repo>/* ~/work/
rmdir <repo>
ln -s /home/vscode/work <repo>
git -C ~/work/<repo> worktree repair ~/work/<移した worktree の名前>
```

`git worktree list` で、worktree のパスが `/home/vscode/work/<名前>` になっていれば成功である。

## 片付ける

1. 変更をコミットして push したことを確かめる。
1. `git worktree remove <パス>` で消す。
   未コミットの変更があると止まる。
1. 不要になったブランチを `git branch -d <ブランチ>` で消す。

ディレクトリを `rm` で消してしまったら、`git worktree prune` で管理情報を消す。

## 使うときの注意

- 本体がチェックアウトしているブランチでは、worktree を作れない。
  Orca で「Reuse branch」をオフにして別名で作るか、本体を `git switch main` で切り替える。
- Dev Container は本体を開いている。
  worktree で作業するときは、そのパスを別のウィンドウで開くか、`cd` で移動する。
- Orca は `<ユーザー名>/issue-<番号>` のような名前でブランチを作る。
  リポジトリにブランチ名の決まりがあるなら、push する前に `git branch -m` で名前を変える。

## 決定理由（Rationale）

- リンクを `post-create.sh` に直接書かず、コミットしないローカルのフックに書くのは、Orca を使わない人の Dev Container に Orca 専用の設定を入れないためである。
  ひな形をコミットするのは、`.env.example` と同じく、使いたい人がコピーするだけで使えるようにするためである。
- 開く場所（`workspaceFolder`）を親ディレクトリに変える案は、Orca の作成先が変わらないので選ばない。

## See also

- [git worktree の仕組みと扱い方](/knowledge/git/worktree.md)
- [親ディレクトリをマウントする Dev Container の構成](/knowledge/devcontainer/parent-directory-mount.md)
- [Orca で Dev Container を開くときのトラブル対処](/knowledge/devcontainer/orca-troubleshooting.md)
- [Dev Container を作り直したときに残るもの・消えるもの](/knowledge/devcontainer/rebuild.md)
