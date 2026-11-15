---
type: guideline
title: 'second-brain ディレクトリ運用規約（エージェント向け指示）'
description: 'AI エージェントが second-brain を探索・作成・更新するときの行動指針。'
tags: [second-brain, docs, agents, okf, git-sync]
status: stable
verified: { by: claude-code/claude-opus-5-5, at: 2026-11-15T00:00:00Z }
stale_after: 2027-11-15T00:00:00Z
---

# second-brain ディレクトリ運用規約（エージェント向け指示）

このファイルは、AI エージェントが `second-brain/` 配下のドキュメントを参照・作成・更新する際に遵守すべきルールです。

## 1. 自動同期ルール（Git Sync）

人間が手動で `git pull` / `git push` しなくて済むよう、以下のルールに従うこと。

- 参照前: ナレッジを探索・参照するセッションの最初に、リモートが設定されていれば `git pull --rebase --autostash` を実行して最新化すること。
- 更新後: ナレッジを作成・更新した際は、目次（`index.md`）を更新し、`python3 scripts/harness/docs_check.py` で機械チェックを通した上で、ユーザーへの確認なしに自動で `git add -A`、`git commit -m "docs: update knowledge"`、`git push` を実行すること（※リモート未設定時は `commit` まで実行）。

## 2. セキュリティ・機密保持ルール

- このディレクトリは複数 PC・複数プロジェクト間で共有される「第二の脳（Second Brain）」であるため、特定の会社の機密情報、プロダクト固有の仕様、社内 URL、認証情報は絶対に記述しないこと。
- プロジェクト非依存の汎用知識（`knowledge/`、`references/`、`learning/`、汎用 `development/`）のみを配置し、個別プロジェクトのコードや固有仕様への逆向きリンクを作らないこと。

## 3. 知識の探索ルール（Progressive Disclosure）

エージェントは知識を探索する際、無差別に全ファイルを走査せず、以下の手順を踏むこと。

1. 目次の確認: まず `index.md` を参照し、関心のある領域（`knowledge/`、`references/`、`learning/`、`development/`）のディレクトリの `index.md` を開く。
1. 目的ドキュメントの特定: `index.md` の説明文とリンクを辿り、最小限の対象ドキュメントのみを読み込む。
1. 鮮度確認: YAML Frontmatter の `status` が `stable` であること、および現在時刻が `stale_after` より前であることを確認する。`verified` の `by` に `human:` があれば人が確かめた文書、なければ AI だけが確かめた文書として扱う。

## 4. ドキュメント作成・更新のルール

エージェントがドキュメントを作成または更新する場合は、書く前に `knowledge/documentation/` および `references/documentation/open-knowledge-format-spec.md` の文書を読み、そのルールに従うこと。1 ファイルに 1 つの関心ごとを書く。

| 知りたいこと                       | 読む文書                                                                                |
| :--------------------------------- | :-------------------------------------------------------------------------------------- |
| Frontmatter と索引の構造           | [Open Knowledge Format (OKF) v0.2 仕様 要約](/references/documentation/open-knowledge-format-spec.md) |
| 作成・更新・削除の流れ、レビュー   | [文書の保守](/knowledge/documentation/documentation-maintenance.md)                     |
| 1 つの文書の組み立て方、ファイル名 | [文書の構成](/knowledge/documentation/document-structure.md)                            |
| 文章の書き方                       | [文章の書き方](/knowledge/documentation/documentation-writing.md)                       |
| Markdown の記法                    | [Markdown の書き方](/knowledge/documentation/markdown-style.md)                         |
| 何をどこに書くか                   | [書く場所の選び方](/knowledge/documentation/where-to-document.md)                       |
| 機能・ライブラリの説明文書の型     | [コードを説明する文書の書き方](/knowledge/documentation/code-docs.md)                   |
| README の書き方                    | [README の書き方](/knowledge/documentation/readme-writing.md)                           |
| 判断に迷ったときの考え方           | [ドキュメントの考え方](/knowledge/documentation/documentation-philosophy.md)            |
| 半角・全角記号の使い分け           | [半角・全角記号の使い分けルール](/knowledge/documentation/bracket-and-character-rules.md) |

AI が書き、まだ人が確かめていない文書（特にハーネス設計などの判断を伴う文書）は `unreviewed/` に置く。出典の原文から要約・整理したプロジェクト非依存の文書（`references/`、`knowledge/`）は、本来の場所に直接置いてよい。

## 5. 禁止事項

- 1 つのドキュメントに無関係な関心事を混在させること（関心の分離違反）。
- `knowledge/` や `references/` に特定のプロジェクト固有の内容を書くこと、およびそこからプロジェクト固有の文書やソースコードへリンクすること（依存の向きの違反）。
- 目次（各ディレクトリの `index.md`）から辿れない孤立ファイル（孤島ドキュメント）を作ること。
- 使われなくなった古い記述を放置すること（不要になった情報は削除または `status: deprecated` にする）。

## See also

- [第二の脳（Second Brain）の目次](/index.md)
- [Open Knowledge Format (OKF) v0.2 仕様 要約](/references/documentation/open-knowledge-format-spec.md)
- [ドキュメントに関する設計知識](/knowledge/documentation/index.md)
