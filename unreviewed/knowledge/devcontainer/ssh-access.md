---
type: guideline
title: 'Dev Container への SSH 接続'
description: 'ホストや外部エディタから Dev Container へパスワード認証で SSH 接続できるようにする設定と、接続の手順。'
tags: [devcontainer, ssh, wsl, setup]
status: draft
verified:
  - { by: antigravity/gemini-4-argon, at: 2026-11-04T00:00:00Z }
  - { by: claude-code/claude-opus-5-5, at: 2026-11-25T00:00:00Z }
stale_after: 2027-11-25T00:00:00Z
---

# Dev Container への SSH 接続

ホスト（Windows / WSL）や外部エディタから、起動中の Dev Container へパスワード認証で SSH 接続できるようにする。
コンテナ内の `sshd`（2222 番ポート）をホストの `127.0.0.1:22222` に転送し、`vscode` ユーザーでログインする。

## 設定

2 つのファイルに設定を書く。

1. SSH サーバーの起動とポート転送（`.devcontainer/devcontainer.json`）

   ```jsonc
   {
     "features": {
       "ghcr.io/devcontainers/features/sshd:1": {}
     },
     "runArgs": ["-p", "127.0.0.1:22222:2222"]
   }
   ```

   - `sshd` の feature が、コンテナ内の 2222 番ポートで OpenSSH サーバーを起動する。
   - `runArgs` の `-p 127.0.0.1:22222:2222` が、ホストの `127.0.0.1:22222` をコンテナ内の 2222 番ポートへ転送する。

1. パスワードの設定（`.devcontainer/post-create.sh`）

   ```bash
   echo "vscode:vscode" | sudo chpasswd
   ```

   - Dev Container の標準イメージでは `vscode` ユーザーにパスワードが設定されておらず、そのままではパスワード認証が拒否される。
   - `postCreateCommand` で動かすので、この行を足す前に作ったコンテナには、作り直すまで反映されない。

## 接続情報と手順

Dev Container が起動している状態で、次の接続情報を使う。

| 項目       | 値                         |
| :--------- | :------------------------- |
| ホスト名   | `127.0.0.1`（`localhost`） |
| ポート番号 | `22222`                    |
| ユーザー名 | `vscode`                   |
| パスワード | `vscode`                   |

### ターミナルから接続する

```bash
ssh -p 22222 vscode@localhost
```

パスワードを求められたら `vscode` を入力する。

### `~/.ssh/config` に登録する

クライアント側の `~/.ssh/config` に次を足すと、`ssh devcontainer` やエディタの SSH ホスト一覧から接続できる。

```sshconfig
Host devcontainer
    HostName 127.0.0.1
    Port 22222
    User vscode
    StrictHostKeyChecking no
    UserKnownHostsFile /dev/null
```

コンテナを作り直すとホスト鍵が変わるので、`StrictHostKeyChecking no` と `UserKnownHostsFile /dev/null` でホスト鍵が変わったときの警告を出さないようにしている。

## 決定理由（Rationale）

- ポートのバインド先を `127.0.0.1` に限るのは、同じネットワーク（LAN / Wi-Fi）の他の端末から入れないようにし、自分の PC からの接続だけを受け付けるためである。
- 外から届かない前提のもとで、WSL と Windows（外部エディタ）の間で秘密鍵やパスフレーズを共有しなくてもすぐ接続できるよう、パスワード認証にしている。
  外から届く場所でコンテナを動かすときは、この前提が崩れるので鍵認証にする。

## See also

- [親ディレクトリをマウントする Dev Container の構成](/knowledge/devcontainer/parent-directory-mount.md)
- [Orca で Dev Container を開くときのトラブル対処](/knowledge/devcontainer/orca-troubleshooting.md)
- [sshd feature（Development Containers 公式）](https://github.com/devcontainers/features/tree/main/src/sshd)
