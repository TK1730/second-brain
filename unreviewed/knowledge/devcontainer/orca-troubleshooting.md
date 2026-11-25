---
type: guideline
title: 'Orca で Dev Container を開くときのトラブル対処'
description: 'Windows の Orca から WSL 上の Dev Container を開くときに起きる SSH 認証失敗と git worktree の不具合の原因、および SSH 接続経由で開く手順。'
tags: [devcontainer, ssh, orca, git-worktree, wsl, troubleshooting]
status: draft
verified:
  - { by: antigravity/gemini-4-hydrogen, at: 2026-11-16T00:00:00Z }
  - { by: claude-code/claude-opus-5-5, at: 2026-11-21T00:00:00Z }
  - { by: claude-code/claude-opus-5-5, at: 2026-11-25T00:00:00Z }
stale_after: 2027-11-25T00:00:00Z
---

# Orca で Dev Container を開くときのトラブル対処

Windows の Orca（エディタ）から、WSL 上で起動した Dev Container を開くときに起きた不具合と、その対処をまとめる。
git worktree が使えないときは、Windows 側のパス（`\\wsl.localhost\...`）で開かず、SSH 接続（`127.0.0.1:22222`）経由で開く。

接続の設定そのものは [Dev Container への SSH 接続](/knowledge/devcontainer/ssh-access.md) を参照する。

## 前提

- 開発者は Windows を使い、Dev Container は WSL 上で起動している。
- Orca は Windows 側で動く。
- リポジトリの親ディレクトリを `/home/vscode/work` にマウントし、worktree を相対パスで記録している。
  仕組みは [親ディレクトリをマウントする Dev Container の構成](/knowledge/devcontainer/parent-directory-mount.md) を参照する。

## 症状 1: SSH で「sign-in を受け付けない」と言われる

Orca に次のエラーが出る。

```text
The host didn't accept any sign-in Orca offered. (All configured authentication methods failed)
```

接続先やユーザー名が合っていても起きる。

### 原因

コンテナ内の `vscode` ユーザーにパスワードが設定されていない。
パスワードを `postCreateCommand` で設定している場合、それはコンテナを作成したときの 1 回しか動かないため、SSH の設定を足す前に作ったコンテナには反映されない。

### 確認

WSL のターミナルで、コンテナ名を確かめてから実行する。

```bash
docker ps --format '{{.Names}} {{.Ports}}'
docker exec <コンテナ名> passwd -S vscode
```

2 列目が `L` ならパスワードが未設定（ロック状態）である。
`P` なら設定済みである。

### 対処

次のどちらか一方を行う。

1. 今すぐ試す場合は、パスワードを設定する。
   コンテナを作り直すとこの設定は消える。

   ```bash
   docker exec -u root <コンテナ名> sh -c 'echo "vscode:vscode" | chpasswd'
   ```

1. 恒久的に直す場合は、VS Code で「Dev Containers: Rebuild Container」を実行する。
   `post-create.sh` が動き、パスワードが設定される。

## 症状 2: worktree を作れない、または使えない

### 2-a: 同じブランチをチェックアウト済みと言われる

```text
Branch "feature/35" is already checked out at "...". Open that workspace, or turn off Reuse branch to create a separate branch.
```

git は、同じブランチを複数の worktree で同時にチェックアウトすることを禁止している。
本体のリポジトリがそのブランチを使っている間は、同じ名前のブランチで worktree を作れない。

対処は次のどちらか一方である。

1. Orca で「Reuse branch」をオフにして、別名のブランチで作る。
1. 本体を別のブランチに切り替える（`git switch main`）。
   未コミットの変更が切り替え先と衝突すると、git が中断するので変更は失われない。

### 2-b: worktree が作れても Dev Container から使えない

Windows 側のパス（`\\wsl.localhost\Ubuntu\home\...`）でリポジトリを開いて worktree を作ると、作成先がリポジトリ本体の中（`<repo>/<repo>/main`）になり、本体の `git status` に `?? <repo>/` が出た。
入れ子の構成なので、誤ってコミットされるおそれがある。

SSH 接続経由で開き直すと、この問題は起きなくなった。
SSH 接続では、Orca は作成先をコンテナ内のパス（`/home/vscode/orca/workspaces`）に決めた。

なぜ Windows のパス経由だと入れ子になるのかは、確認できていない。
Orca の作成先の基準が、リポジトリのパスになったと推測している。

## 正しい開き方

Windows のパスではなく、SSH 接続経由で開く。

1. Dev Container を起動しておく。
1. Orca で SSH 接続先を追加する。

   | 項目       | 値          |
   | :--------- | :---------- |
   | ホスト名   | `127.0.0.1` |
   | ポート番号 | `22222`     |
   | ユーザー名 | `vscode`    |
   | パスワード | `vscode`    |

1. 接続したあと、リポジトリはコンテナ内のパスで追加する。
   Windows のパス（`\\wsl.localhost\...`）は選ばない。

   ```text
   /home/vscode/work/<repo>
   ```

1. worktree を作る。
   ブランチ名の入力欄が出れば正常である。

## 確認

コンテナ内で次を実行する（WSL 側では自分のリポジトリのパスを指定する）。

```bash
git -C /home/vscode/work/<repo> worktree list
```

新しい worktree のパスが出れば成功である。
本体の `git status` に `?? <repo>/` が出ていなければ、入れ子にはなっていない。

## worktree の置き場所

SSH 接続で作った worktree は、そのままではマウントの外に置かれる。
マウントの中に置くリンクの作り方は [Orca の worktree を Dev Container のマウントの中に置く](/knowledge/devcontainer/orca-worktree.md) を参照する。

## 決定理由（Rationale）

- 開き方の対処を「SSH 接続経由」に絞っているのは、実際にその方法で worktree が開けたことを確認したためである。
  Windows のパスを直す方法は、原因が確認できていないので書かない。

## See also

- [Dev Container への SSH 接続](/knowledge/devcontainer/ssh-access.md)
- [Orca の worktree を Dev Container のマウントの中に置く](/knowledge/devcontainer/orca-worktree.md)
- [git worktree の仕組みと扱い方](/knowledge/git/worktree.md)
