---
type: guideline
title: 'Dev Container を作り直したときに残るもの・消えるもの'
description: 'Dev Container を作り直す（rebuild）と、マウントの中のものは残り、外のものは消えること、消えたものを何が戻すか、作り直す前に確かめること。'
tags: [devcontainer, rebuild, setup, troubleshooting]
status: draft
verified: { by: claude-code/claude-opus-5-5, at: 2026-11-25T00:00:00Z }
stale_after: 2027-11-25T00:00:00Z
---

# Dev Container を作り直したときに残るもの・消えるもの

Dev Container を作り直す（VS Code の「Dev Containers: Rebuild Container」など）と、マウントしたディレクトリの中身は残り、それ以外のコンテナの中身は消える。
消えるものの多くは `post-create.sh` で作り直せるが、マウントの外に置いた作業は戻らない。
ここでは、[親ディレクトリをマウントする Dev Container の構成](/knowledge/devcontainer/parent-directory-mount.md) を例にする。

## 残るもの

| もの                                           | 場所の例                                      | 残る理由                       |
| :--------------------------------------------- | :-------------------------------------------- | :----------------------------- |
| リポジトリ、未コミットの変更、`node_modules`   | `/home/vscode/work/<repo>`                    | マウントの中                   |
| 兄弟に置いた worktree                          | `/home/vscode/work/<名前>`                    | マウントの中                   |
| マウントの中に置いたパッケージのストア         | `/home/vscode/work/.pnpm-store`               | マウントの中                   |
| ツールのログインと設定                         | `~/.claude`、`~/.claude.json`、`~/.config/gh` | `mounts` でホストと共有        |
| ホストの Docker で動かしているコンテナとデータ | ホストの Docker                               | Dev Container の外で動いている |

## 消えるもの

| もの                                                | 場所の例                               | 戻すもの                                           |
| :-------------------------------------------------- | :------------------------------------- | :------------------------------------------------- |
| `vscode` ユーザーのパスワード                       | コンテナの中                           | `post-create.sh`                                   |
| ホームの下のキャッシュ（Playwright のブラウザなど） | `~/.cache/ms-playwright`               | `post-create.sh`                                   |
| マウントの外のモジュールキャッシュ                  | `/go/pkg/mod`                          | `post-create.sh`（`go mod download` など）         |
| Orca の worktree の置き場所へのリンク               | `~/orca/workspaces/<repo>`             | `post-create.local.sh`（ひな形をコピーしていれば） |
| マウントの外に作った worktree                       | `~/orca/workspaces/<repo>/<名前>` など | 戻らない                                           |
| Orca が作成中の worktree                            | `~/orca/workspaces/.orca-preparing`    | 戻らない                                           |
| シェルの履歴、手で入れたツール                      | コンテナの中                           | 戻らない                                           |

- Orca の置き場所をリンクにしないまま作業していた場合、その中の worktree は消える。
  移し方は [Orca の worktree を Dev Container のマウントの中に置く](/knowledge/devcontainer/orca-worktree.md) を参照する。
- `containerEnv` に書いた環境変数（`GITHUB_TOKEN` など）は、ホストの値を変えたら作り直さないと反映されない。

## 作り直す前に確かめること

1. worktree がすべてマウントの中にあるか。

   ```bash
   git -C /home/vscode/work/<repo> worktree list
   ```

   パスが `/home/vscode/work/` で始まらない worktree があれば、push するか、マウントの中へ移す。
   リポジトリの中に作った worktree（ツールが一時的に作るものなど）は、マウントの中にあるので残る。

1. Orca などのツールが worktree を作っている最中ではないか。

## 作り直すべきとき

`post-create.sh`、`Dockerfile`、`devcontainer.json` を変えたら作り直す。
`post-create.sh` はコンテナを作るときにしか動かないので、作り直さないと今のコンテナには反映されない。

## See also

- [親ディレクトリをマウントする Dev Container の構成](/knowledge/devcontainer/parent-directory-mount.md)
- [Dev Container のライフサイクルコマンドとマウント](/knowledge/devcontainer/lifecycle.md)
- [Orca の worktree を Dev Container のマウントの中に置く](/knowledge/devcontainer/orca-worktree.md)
