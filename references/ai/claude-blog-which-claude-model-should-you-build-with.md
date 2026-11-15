---
type: reference
title: 'どの Claude モデルで開発すべきか: Fable・Opus・Sonnet・Haiku の使い分け'
description: 'claude.dev ブログの記事「Which Claude model should you build with? Fable, Opus, Sonnet, or Haiku」の要約で、4 つの Claude モデルの性能・料金・完了タスクあたりのコストと組み合わせ方を整理する。'
tags: [ai, claude, llm, model-selection, cost-optimization, agent]
status: stable
verified: { by: antigravity/gemini-4-argon, at: 2026-11-15T00:00:00Z }
stale_after: 2027-11-15T00:00:00Z
---

# どの Claude モデルで開発すべきか: Fable・Opus・Sonnet・Haiku の使い分け

claude.dev ブログに公開された Addy Osmani 氏の記事「Which Claude model should you build with? Fable, Opus, Sonnet, or Haiku」 (2026-11-09 公開) の要約である。
この記事では、Claude の 4 つのモデルファミリ (Fable 5.2、Opus 5.5、Sonnet 5.5、Haiku 5.5) の性能・料金体系・推論 effort の調整方法、および完了タスクあたりの総コストを最適化するマルチモデル構成パターンを整理している。

- 著者: Addy Osmani
- 出典: [Which Claude model should you build with? Fable, Opus, Sonnet, or Haiku](https://claude.dev/blog/which-claude-model-should-you-build-with/)
- 公開日: 2026-11-09

## 基本方針 (TL;DR)

多くの開発タスクやエージェント構築においては、**Claude Opus 5.5 (effort: `medium`)** を既定の出発点にするのが推奨される。
そのうえで、手順が明確な定型作業は **Sonnet 5.5**、大量・低遅延の分類やデータ抽出は **Haiku 5.5** へと段階的に下げ、Opus 5.5 の `high` effort でも解けない最高難度の長期間自律タスクにのみ **Fable 5.2** を投入する。

## 4 モデルのスペックと料金比較

4 つのモデルはすべて共通して **最大 1M (100 万) トークンのコンテキストウィンドウ**と **最大 128K トークンの出力**に対応している。
100 万トークンあたりの入出力料金と主な適性は以下のとおりである。

| モデル | 入力料金 (1M トークン) | 出力料金 (1M トークン) | 主な用途と位置付け |
| :--- | :--- | :--- | :--- |
| **Haiku 5.5** | $0.10 (100K 超は $0.50) | $0.50 (100K 超は $2.50) | 大量処理、分類、構造化データ抽出、ルーティングなどの高速・低コスト処理向け。 |
| **Sonnet 5.5** | $2.00 | $10.00 | 日常的なコーディング、対話型チャット、範囲が明確なバグ修正や定型実装向け。 |
| **Opus 5.5** | $4.00 | $20.00 | 複雑なコーディング、マルチステップのエージェント実行、高度な文章作成を担う主力モデル。 |
| **Fable 5.2** | $8.00 (Fast mode は $16.00) | $40.00 (Fast mode は $80.00) | 最も困難な推論や数時間に及ぶ無人自律エージェント向け (同等の推論能力に厳格な安全ガードを備えた Mythos 5.2 も存在する)。 |

## モデル選定における 3 つのトレードオフ

### 1. トークン単価ではなく「完了タスクあたりの総コスト」で見る

モデル選びで最も陥りやすい罠は、100 万トークンあたりの単価 (sticker price) だけで比較してしまうことである。
単価の安い下位モデルが推論ミスやテスト失敗を起こし、何十ターンもリトライや手戻りを繰り返すと、累積トークン量と所要時間が膨れ上がる。
結果として、上位モデル (Opus 5.5 など) を使って少ないターン数で 1 回で解き切るほうが、「完了タスクあたりの総コスト (Cost per finished task)」もレイテンシも低く収まるケースが多い。

### 2. モデルを変える前に `effort` パラメータを調整する

期待する精度が出ない、あるいは応答が遅いと感じたとき、すぐに別のモデルへ切り替えるべきではない。
まずは同じモデル内で `effort` パラメータ (`low` / `medium` / `high` / `max`) を調整し、思考トークンの投入量によってレイテンシ・コストと精度のバランスがどう変化するかを検証する。

### 3. 1M コンテキストとプロンプトキャッシュの活用

全モデルが 1M コンテキストに対応しているため、大規模なコードベースや長い履歴をそのまま渡すことができる。
ただし、長いコンテキストをそのまま毎回送信するとコストがかさむため、プロンプトキャッシュ (Prompt Caching) を必ず併用してプレフィックスの再読み込みコストを抑える設計が求められる。

## 複数モデルを組み合わせる 4 つのパターン (Mixing models)

単一モデルでシステム全体を賄うのではなく、タスクの性質に応じて複数のモデルを組み合わせる代表的な 4 つのパターンが紹介されている。

1. **フェーズの区切りでのモデル切り替え**: アーキテクチャ設計や計画立案フェーズでは Opus 5.5 や Fable 5.2 を使い、仕様が確定した後の実装フェーズでは Sonnet 5.5 に切り替えるなど、タスクの自然な区切りでモデルを変更する。
2. **サブエージェントへの小モデル割り当て**: メインのオーケストレーターには Opus 5.5 を据えつつ、ファイル探索、コード検索、ログ要約などの補助タスクを担うサブエージェントには Haiku 5.5 や Sonnet 5.5 を割り当てる。
3. **Advisor パターンによるエスカレーション**: 通常のループは Sonnet 5.5 などの下位モデルで高速に回し、設計上の重要な分岐や難解なバグに直面したときだけ上位モデル (Opus 5.5 や Fable 5.2) を Advisor として呼び出して判断を仰ぐ。
4. **大量の並列定型ワーカーの委譲**: 仕様や入出力スキーマが完全に定まった大量の並列サブタスク (数百ファイルの機械的な移行や一括抽出など) を、Haiku 5.5 や Sonnet 5.5 のワーカー群にファンアウトして処理させる。

## See also

- [Which Claude model should you build with? Fable, Opus, Sonnet, or Haiku (claude.dev)](https://claude.dev/blog/which-claude-model-should-you-build-with/)
- `/references/ai/zodchiii-claude-opus-5-5-setup-guide.md` — Claude Opus 5.5 の effort 設定・プロンプトキャッシュ・API 変更点の詳細ガイド
- `/references/ai/hanakoxbt-loops-and-graphs.md` — スプリッター・ワーカー・コードノードを組み合わせるエージェントグラフ設計
