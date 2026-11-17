---
type: guideline
title: 'Claude Code のモッドの権限と管理者設定'
description: 'モッドが持つ権限の範囲（ファイル、プロセス、HTTP）、権限ルールとの関係、sec-default と管理者設定、導入前の確認事項。'
tags: [knowledge, ai, claude, claude-code, mods, security, admin]
status: stable
sources:
  - id: docs-overview
    resource: 'https://code.claude.com/docs/ja/plugins/mods/overview'
  - id: docs-admin
    resource: 'https://code.claude.com/docs/ja/plugins/mods/admin'
  - id: blog
    resource: 'https://claude.dev/blog/getting-started-with-claude-code-mods/'
  - id: article
    resource: 'https://claude.com/ja/resources/articles/claude-code-mods'
generated: { by: claude-code/claude-sonnet-5-5, at: 2026-11-17T00:00:00Z }
verified: { by: claude-code/claude-sonnet-5-5, at: 2026-11-17T00:00:00Z }
stale_after: 2027-02-17T00:00:00Z
---

# Claude Code のモッドの権限と管理者設定

モッドをチームに入れる前に確認しておきたい、権限の範囲と管理者向けの制御をまとめる。
Claude Code の公式ドキュメント（overview、admin、api、reference）[^docs] と、関連する 2 つの記事 [^blog] [^article] を突き合わせた。
ドキュメントの一部は要約を経て読んでおり、バージョンで変わる可能性が高い。管理者設定を決める前に、最新の公式ドキュメントを確かめる。

## 「サンドボックス」の食い違いの整理

ブログは「モジュールは DOM も Node もないサンドボックスで動く」と書き、記事と公式ドキュメントは「モッドはサンドボックス化されない」と書く。
両者は矛盾しない。

- ブログの「サンドボックス」は、モッドの JavaScript が使える API を `$` に絞った実行環境の分離を指す。
- 公式ドキュメントの「サンドボックス化されない」は、セキュリティ上の隔離がないことを指す。モッドのファイル操作、ネットワーク通信、起動したプログラムは、Claude Code のサンドボックスの外で動く。サンドボックスが包むのは Bash、PowerShell、Monitor のコマンドだけである。

つまり、モッドはユーザー自身の権限で動くコードとして扱う。

## モッドが持つ権限

| API         | できること                                                            | 主な制限                                           |
| :---------- | :-------------------------------------------------------------------- | :------------------------------------------------- |
| `$.fs`      | ファイルの読み書き、一覧、存在確認                                    | 1 ファイル 4 MiB まで。パスの許可リストはない      |
| `$.process` | 任意のプログラムの実行（引数配列、シェルなし）                        | 既定 30 秒、最大 10 分。出力は 4 MiB まで          |
| `$.http`    | http と https の取得                                                  | 1 回 30 秒、リダイレクト 5 回、本文 4 MiB まで。ホストの許可リストはない |

- これらの呼び出しに許可の確認は出ない。
- 権限ルールと PreToolUse フックは、モッド自身の `$.fs` と `$.process` の呼び出しには適用されない。たとえば `Read(.env)` を拒否していても、モッドは `$.fs.read` でそのファイルを読める。
- `$.http` は、組織が WebFetch を拒否していれば拒否される。ただし WebFetch を環境変数や拒否ルールで切っただけでは、モッドは取得できてしまう。
- `$.process` が起動したプログラムのネットワーク通信は、ネットワークポリシーの対象外である。

## Claude のツール呼び出しとの関係

- モッドは、Claude のツール呼び出しを承認または拒否したり、書き換えたりできる。
- 組み込みの保護モッド（sec-default）が読み込まれている間は、権限ルールと PreToolUse フックがユーザーのモッドより優先される。ユーザーのモッドは、拒否ルールで止まる呼び出しを承認できない。
- 保護モッドが読み込まれない環境では、モッドが拒否ルールで止まるはずの呼び出しを承認できる。
- 保護モッドは、管理設定がある場合と、Team または Enterprise でログインしている場合に読み込まれる。API キーや Bedrock などの利用者は、管理設定のあるマシンでだけ読み込まれる。

## 管理者が使える設定

| 設定                                                          | 効果                                                           |
| :------------------------------------------------------------ | :------------------------------------------------------------- |
| `allowManagedModsOnly`（`cc-plugin-sec-default` のオプション）| ユーザーが入れたモッド（`--plugin-dir` を含む）を動かさない     |
| `allowModsToOverrideDenyRules`                                | ユーザーのモッドが、ほとんどの拒否ルールを越えて承認できるようにする |
| `disableAllHooks`                                             | 入れたプラグインのモッドとフックをすべて止める                 |
| `allowManagedHooksOnly`                                       | 組織のモッドと組み込みのモッドだけを読み込む                   |
| `disableSideloadFlags`                                        | `--plugin-dir` と `--plugin-url` を使えなくする                |
| `prependPlugins` / `appendPlugins`                            | モッドの実行順を決める                                         |

- 利用者は `/plugin`、`--safe-mode`、`disableAllHooks` でモッドを止められるが、管理設定が優先される。
- 管理者が自前のモッドを先に読み込む場合は、sec-default も一覧に入れて保護を保つ。
- 組織のモッドと認められるには、絶対パスのディレクトリ型マーケットプレイスから、有効化し、その場で読み込む必要がある。

## 導入前の確認事項

- 入れる前にリポジトリを読み、信頼できる作者のものだけにする。モッドの作者は Anthropic ではなく公開者である。
- 確実に止めたい操作は、モッドの安全網ではなく権限ルールで止める。ブログの Blast Radius は、コマンド文字列を見るだけで、`$(...)` やエイリアスで回避できる。
- 利用者のマシンに管理設定を配れるか確かめる。配れない環境では、保護モッドが読み込まれない場合がある。
- 必要な Claude Code のバージョンは、ターミナルが 2.1.287 以降、デスクトップが 2.1.286 以降である。API はリリース間で変わりうる。
- フックは 1 回 10 秒の制限があり、フックのワーカーが 3 回落ちると、そのセッションでは組み込み以外のモッドが外れる。

## See also

- [Claude Code のモッドで画面と動作を拡張する](/knowledge/ai/claude-code/claude-code-mods.md)
- [Claude Code のモッドで何ができるか、チームでどう管理するか](/knowledge/ai/claude-code/claude-code-mods-overview.md)
- [規制産業で Claude Code を全社展開するときの統制の作り方](/knowledge/ai/agent-platform/regulated-firm-claude-code-rollout.md)

[^docs]: [mods の概要（Claude Code ドキュメント）](https://code.claude.com/docs/ja/plugins/mods/overview)と、その admin ページ。
[^blog]: [Getting started with Claude Code mods](https://claude.dev/blog/getting-started-with-claude-code-mods/)（Addy Osmani、2026-10-01）
[^article]: [Customize Claude Code with mods](https://claude.com/ja/resources/articles/claude-code-mods)（2026-10-01）
