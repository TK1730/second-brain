# 未確認の文書

AI が書き、まだ人が内容を確かめていない文書の置き場所である。ここにある文書は正しい情報として扱わない。

確かめ終わった文書は、パスから `unreviewed/` を外した場所へ移し、移動先の `index.md` に項目を足す。文書内のリンクは移動先の場所を前提に書いてあるので、ここに置いている間は切れているものがある。

出典の原文から要約・整理したプロジェクト非依存の文書（`references/`、`knowledge/`）は、人の確認を待たずに本来の場所に置く。ここには、人が確かめる必要がある文書だけを置く。

## 開発・ハーネス（development）

- [ハーネス改善の仕組み](development/harness-improvement/) - AI と開発するときのやり方を、記録をもとに目的ごとに良くしていく仕組みの使い方。

## 共通設計ナレッジ（knowledge）

### devcontainer

- [親ディレクトリをマウントする Dev Container の構成](knowledge/devcontainer/parent-directory-mount.md) - リポジトリの親ディレクトリをマウントし、worktree を相対パスで記録して、ホストとコンテナの両方から同じ worktree を開けるようにする Dev Container の構成と、設定スクリプトの分け方。
- [Dev Container を作り直したときに残るもの・消えるもの](knowledge/devcontainer/rebuild.md) - Dev Container を作り直す（rebuild）と、マウントの中のものは残り、外のものは消えること、消えたものを何が戻すか、作り直す前に確かめること。
- [Dev Container への SSH 接続](knowledge/devcontainer/ssh-access.md) - ホストや外部エディタから Dev Container へパスワード認証で SSH 接続できるようにする設定と、接続の手順。
- [Orca で Dev Container を開くときのトラブル対処](knowledge/devcontainer/orca-troubleshooting.md) - Windows の Orca から WSL 上の Dev Container を開くときに起きる SSH 認証失敗と git worktree の不具合の原因、および SSH 接続経由で開く手順。
- [Orca の worktree を Dev Container のマウントの中に置く](knowledge/devcontainer/orca-worktree.md) - Orca が Dev Container の中に作る git worktree を、シンボリックリンクでマウントの中（リポジトリの兄弟ディレクトリ）に置く方法と、作った後にやること、片付け方、使うときの注意。

## 戻すときに足す目次の項目

`development/index.md` には、`harness-improvement/` の項目を足す。
`knowledge/devcontainer/index.md` には、`lifecycle.md` の後に `parent-directory-mount.md`、`rebuild.md`、`ssh-access.md`、`orca-troubleshooting.md`、`orca-worktree.md` の項目を足す。
