---
type: guideline
title: 'Claude ディレクトリへのプラグイン提出ポータルを使う'
description: 'プラグインの構成要素、2 つの提出経路、審査の流れ、公開後の分析、MCP 拡張の要点。'
tags: [knowledge, ai, claude, plugin, mcp, directory]
status: stable
sources:
  - id: claude-article
    resource: 'https://claude.com/ja/resources/articles/build-plugins-for-claude'
generated: { by: claude-code/claude-sonnet-5-5, at: 2026-11-17T00:00:00Z }
verified: { by: claude-code/claude-sonnet-5-5, at: 2026-11-17T00:00:00Z }
stale_after: 2027-11-17T00:00:00Z
---

# Claude ディレクトリへのプラグイン提出ポータルを使う

Claude のディレクトリへプラグインを提出し、審査状況と公開後の利用状況を確認する開発者ポータルの要点をまとめる。
内容は Anthropic の記事「Build plugins for Claude with the directory submission portal」（2026-09-25 公開）[^claude-article] の要約であり、製品発表の性格が強い。

## プラグインの構成要素

プラグインは、第三者が Claude を拡張する主な手段で、次を束ねる。

- MCP コネクタ（リモート MCP サーバー）
- Agent Skills
- Claude Code のみ: LSP、コマンド、フック、エージェント

## 提出の手順

1. 対象: 有料の Claude プランの開発者が使える。
1. 経路を選ぶ。
   - 単体の MCP コネクタ: リモート MCP サーバーの URL を提出する。
   - プラグインのバンドル: MCP サーバーとスキルを GitHub リポジトリにまとめ、そのリポジトリを提出する。
1. 提出直後に自動検証と安全性スキャンが走り、問題を早く把握できる。
1. 審査状況、スキャン結果、推奨される修正を、ポータルで追える。
1. 承認後、公開時期は開発者が決める。承認済みのプラグインはディレクトリに載る。

スキャンの指摘と推奨修正は、再提出の前に直す。

## 公開後の分析

- 利用状況: インストール数を、利用面（プロダクトの画面）とバージョン別に見られる。修正や機能の優先順位づけに使う。
- 発見状況: 掲載ページの閲覧数と、そこへ至った検索語を見られる。掲載内容の改善に使う。

## MCP の新仕様と拡張

- Claude は最新の MCP 仕様（記事では MCP 2.0。ステートレスなコアを持つ）に対応している。
- 記事が挙げる拡張は 2 つある。MCP Apps はチャット内で対話的な UI を出す。Enterprise Managed Auth は企業利用者向けの、操作不要の OAuth である。
- 追加の MCP 機能や拡張への対応は予定とされている。
- 対話的な体験には MCP Apps、企業向けのサインインには Enterprise Managed Auth を検討する。

## 今後の予定

- プラグインの統合された探索体験が、数週間かけて Claude と Claude Code に展開される。
- スキルと MCP コネクタは引き続き構成部品で、ディレクトリに掲載される。将来は、コネクタの掲載をプラグインに変換できるようになる。
- 既存のスキル、コネクタ、プラグインは変更不要である。

## See also

- [Claude for Manufacturing で現場の下書き作業を任せる](/knowledge/ai/products/claude-for-manufacturing.md)

[^claude-article]: [Build plugins for Claude with the directory submission portal](https://claude.com/ja/resources/articles/build-plugins-for-claude)（2026-09-25）
