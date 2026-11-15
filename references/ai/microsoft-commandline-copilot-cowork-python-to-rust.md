---
type: reference
title: 'Copilot Cowork の開発から得た 6 つの教訓と稼働中の Python から Rust への移行'
description: 'Microsoft Command Line ブログの記事「Nine engineers, 1,211 pull requests in a day: Lessons from building Copilot Cowork」の要約で、エージェント駆動開発の 6 原則と本番ランタイムの Rust 移行手法を説明する。'
tags: [ai, agent, copilot, rust, python, migration, software-engineering]
status: stable
verified: { by: antigravity/gemini-4-argon, at: 2026-11-15T00:00:00Z }
stale_after: 2027-11-15T00:00:00Z
---

# Copilot Cowork の開発から得た 6 つの教訓と稼働中の Python から Rust への移行

Microsoft Command Line ブログに公開された記事「Nine engineers, 1,211 pull requests in a day: Lessons from building Copilot Cowork」 (2026-11-02 公開) の要約である。
この記事では、少人数のエンジニアチームが AI エージェントを全面的に活用して短期間で Copilot Cowork を構築・一般提供 (GA) に到達させた開発原則と、稼働中の本番ランタイムを無停止で Python から Rust へ移行した手法を報告している。

- 著者: Bas Brekelmans (Microsoft)
- 出典: [Nine engineers, 1,211 pull requests in a day: Lessons from building Copilot Cowork](https://commandline.microsoft.com/how-we-built-copilot-cowork-python-to-rust-migration/)
- 公開日: 2026-11-02

## 概要: 少人数チームによる高速なエージェント駆動開発

Copilot Cowork の開発は 2026 年 1 月 13 日に空のリポジトリから始まり、約 4.5 か月で一般提供 (GA) に到達した。
コードの大半は AI エージェントによって記述され、ピーク時の 10 月 21 日には 9 人のエンジニアが 1 日で 1,211 件の Pull Request (PR) を main ブランチにマージした。
この速度と品質を両立させるため、チームは人間のレビュー能力や手作業に頼るのではなく、エージェントの行動境界と検証基盤を厳格に設計した。

## エージェント駆動開発を支える 6 つのプラクティス

記事では、大量のエージェント出力を破綻させずに本番品質へ収束させるための 6 つの原則を挙げている。

### 1. コードの前に仕様を書く (Spec before code)

何を変更し、どのように検証し、何を壊してはいけないかを明記した Markdown の仕様書なしでのコード生成を禁止する。
エージェントにいきなり実装を書かせるのではなく、まず仕様書で合意と検証基準を固めることで、見当違いの実装や手戻りを防ぐ。

### 2. 境界内に狭いエージェントを閉じ込める (Narrow agents inside boundaries)

各エージェントは認証情報 (クレデンシャル) を持たない隔離コンテナ内で起動し、1 つの仕様・1 つのタスクだけを実行する。
アイデンティティ管理、ポリシー適用、外部操作の承認といった権限はすべてコンテナ外の信頼されたホスト側が管理し、エージェント自身の権限を極小化する。

### 3. チェック自体が機能していることを証明する (Checks must prove they checked something)

CI のグロブ指定ミスや構文エラーによって、対象ファイルが 0 件のままチェックが成功してしまう「偽のグリーン (false green)」を防ぐ。
そのため、すべての検証ステップで検査対象となったファイル数の出力を必須化し、新しいチェックを追加する際には意図的に失敗させるテストを同梱して「失敗すべきときに確実に失敗すること」を証明させる。

### 4. 組織の学びを保存する (Preserving institutional learning)

コードレビューや本番運用で見つかったバグ、エッジケース、設計上の落とし穴をその場限りの指摘で終わらせず、ドキュメントや検証ルールとしてリポジトリに体系化する。
これにより、後から起動されるエージェントが過去の失敗を自動的に参照し、同じミスを繰り返さないようにする。

### 5. 並列作業向けにコードベースを形作る (Shaping the codebase for parallel work)

多数のエージェントが同時に PR を作成してもマージ競合 (コンフリクト) が発生しないよう、アーキテクチャとモジュールの境界を疎結合に分割する。
エージェントの並列度を上げるためには、プロンプトの工夫だけでなく、コードベース自体の構造を並列変更に適した形に保つ必要がある。

### 6. 自動ループに限界を設ける (Setting limits on automated loops)

エージェントはコード変更を提案し、自動検証ループを回して修正を重ねることはできるが、main ブランチへのマージ可否だけは決してエージェント自身に決定させない。
自律ループの暴走や基準の勝手な緩和を防ぐため、最終的なゲートは決定論的なチェックと人間の管理下に置く。

## 稼働中のランタイムにおける Python から Rust への移行

開発の後半では、本番稼働中のサービスを止めずにランタイムを Python から Rust へ全面移行するプロジェクトが実施された。

### 移行の背景

本番環境の Python ランタイムにおいて、イベントループのストール (最大 11.9 秒の停止) と深刻なメモリ逼迫 (週 539 回の OOM kill) が発生していた。
これを受け、チームはサービスを継続しながら段階的に Rust へ置き換え、10 月 9 日に Python コードを完全に削除した。

### フィクスチャ再生によるパリティ検証

言語移行に伴うデグレードを防ぐため、本番の Python 実装から約 430 個の入出力 JSON フィクスチャを記録した。
これを新しい Rust 実装に対して再生 (リプレイ) し、既存の Python ランタイムと挙動が完全に一致するかを機械的に検証した。

### 移行過程で発覚・修正した 2 つのバグ

フィクスチャ検証と段階的ロールアウトの過程で、以下の 2 つの重要な問題が発見・修正された。

1. **非同期イベント順序の不整合**: Python の非同期処理が暗黙のうちに保証していたイベントの発火順序が Rust の初版実装で変化し、その順序を前提としていたクライアント側と不整合を起こした。
2. **フロントドアのバッファリングによる遅延**: Rust のフロントドア実装が、下流の全データ取得が完了するまでレスポンスの返却を待ってしまい、ストリーミング応答が従来の 6 倍遅くなっていた問題を特定し修正した。

### 移行の成果

コンテナを都度起動する従来の方式から常駐型の Rust サービスへ移行した効果も含め、9 月下旬の比較において、初回ターンの Time to First Token (TTFT) は以下のように大幅に短縮された。

| 指標 | 移行前 (Python) | 移行後 (Rust) |
| :--- | :--- | :--- |
| 初回ターン TTFT (p50) | 7.9 秒 | 2.7 秒 |
| 初回ターン TTFT (p90) | 14.5 秒 | 6.2 秒 |

## See also

- [Nine engineers, 1,211 pull requests in a day: Lessons from building Copilot Cowork (Microsoft Command Line)](https://commandline.microsoft.com/how-we-built-copilot-cowork-python-to-rust-migration/)
- `/references/ai/hanakoxbt-loops-and-graphs.md` — エージェントの検証ループと並列作業グラフの設計原則
- `/references/ai/0xarcos-claude-code-failure-ratchet.md` — 失敗を検証コードと台帳にエンコードして再発を防ぐ Failure Ratchet
- `/references/ai/beamnxw-agent-harness-loop-graph-engineering.md` — ハーネス・ループ・グラフの 3 層によるエージェント設計フレームワーク
