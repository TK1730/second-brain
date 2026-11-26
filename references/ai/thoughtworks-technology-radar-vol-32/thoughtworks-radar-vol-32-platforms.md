---
type: reference
title: 'Thoughtworks Technology Radar Vol.32: Platforms'
description: 'Thoughtworks Technology Radar Vol.32 (2025 年 4 月) の Platforms 象限 28 項目の要約で、CI/CD と分散 SQL、Grafana の可観測性基盤、LLM の可観測性と評価の基盤、MCP や推論モデル、PostgreSQL 拡張やテストデータ生成の基盤をリングごとにまとめる。'
tags: [ai, thoughtworks, technology-radar, platform, observability, llm, database]
status: stable
verified: { by: claude-code/claude-opus-5-5, at: 2026-11-26T00:00:00Z }
stale_after: 2027-11-26T00:00:00Z
---

# Thoughtworks Technology Radar Vol.32: Platforms

Thoughtworks Technology Radar Vol.32 (2025 年 4 月) の Platforms (基盤) 象限の要約である。
Grafana の可観測性の基盤と LLM の可観測性・評価の基盤が多く、MCP や推論モデルもここに入っている。

- 出典: Thoughtworks Technology Radar Volume 32 (PDF)、[thoughtworks.com/radar](https://www.thoughtworks.com/radar)

[TOC]

## Adopt

### 23. GitLab CI/CD

- コードの統合からテスト、デプロイ、監視までを GitLab の中で完結させる。多段のパイプライン、キャッシュ、並列実行、自動で増減するランナーを持つ。
- SAST や DAST などのセキュリティ・コンプライアンスの機能が組み込まれ、要件の厳しい用途に向く。

### 24. Trino

- データがある場所のまま、対話的な分析クエリを投げられる分散 SQL エンジンである。リレーショナル DB、Parquet、Apache Iceberg などをコネクターで扱う。
- 複数の情報源を 1 つの論理テーブルとして問い合わせられ、AWS Athena や Starburst の中核でもある。

## Trial

### 25. ABsmartly

- A/B テストと実験の基盤で、Group Sequential Testing により従来より最大 80% 速く結果が出る。API ファーストで、Web、モバイル、マイクロサービス、ML モデルの実験に使える。

### 26. Dapr

- 前回の掲載から大きく進化した。ジョブのスケジュール、仮想アクター、高度な再試行ポリシー、暗号化などの部品が増え、mTLS や distroless イメージなど安全な既定値も重視している。

### 27. Grafana Alloy

- 旧 Grafana Agent で、ログ、メトリクス、トレースをまとめて集めるオープンソースの OpenTelemetry Collector である。Promtail の非推奨化に伴い、Grafana の構成では特にログ収集の第一候補になった。

### 28. Grafana Loki

- Prometheus に着想を得た、水平に拡張できるマルチテナントのログ集約システムである。ログ本体ではなくラベルだけを索引付けし、本体は S3 などに置くので運用と保存の費用が下がる。
- 3.0 で OpenTelemetry にネイティブ対応した。テナントを分離し、問題のあるテナントが他に影響しないようにできる。

### 29. Grafana Tempo

- オブジェクトストレージに長期保存する、費用効率の良い分散トレースの基盤である。Parquet ベースの形式で、TraceQL で問い合わせる。GKE で MinIO と組み合わせて自前運用した。

### 30. Railway

- GitHub や Docker からのデプロイから本番の可観測性までをまとめた、フルスタック向けの PaaS である。Vercel がフロントエンド向けなのに対し、多くのフレームワークやデータベースを扱える。長期運用なら費用を比較する。

### 31. Unblocked

- リポジトリ、社内文書、プロジェクト管理、チャットとつなぎ、業務や技術の概念、設計、運用手順についての質問に答える既製の AI チームアシスタントである。
- チームはコード生成より、文脈の情報にすぐたどり着けることを評価した。大きなコード生成には専用のエージェントが向く。

### 32. Weights & Biases

- LLM 向けの機能を増やし、Weave でエージェントシステムの追跡、評価、独自指標、LLM による採点、データセットの保存ができる。人のフィードバックも集めて後の微調整に使える。

## Assess

### 33. Arize Phoenix

- LLM の可観測性の基盤で、トレース、評価、プロンプト管理を持ち、主要な LLM 提供者やフレームワークと簡単につながる。出力、遅延、トークン使用量を少ない設定で把握できる。

### 34. Chainloop

- オープンソースのサプライチェーンセキュリティ基盤である。セキュリティチームが、どの成果物 (SBOM や脆弱性レポート) を集めてどう評価するかを契約として決め、CI/CD の中の CLI が証明 (attestation) を作って送る。
- Rego で検証し、SLSA レベル 3 に沿った単一の記録を作る。

### 35. Deepseek R1

- DeepSeek の最初の推論モデルである。MLA、MoE、FP8 学習などでハードウェアを使い切り、はるかに低い費用で最先端に匹敵する。
- R1-Zero は教師あり微調整なしの強化学習だけで推論能力を引き出した。重みは公開されている。Llama・Qwen ベースの蒸留版もある。

### 36. Deno

- Node.js の作者が、Node.js の誤りを正すために作った実行環境である。厳しいサンドボックス、依存管理の内蔵、TypeScript のネイティブ対応を持つ。
- Deno 2 で Node.js と npm の互換性、長期サポート版が入り、移行の壁が下がった。ただし多言語を避けるためだけに選ぶことには注意する。

### 37. Graphiti

- 時間の経過で変わる事実と関係をとらえる知識グラフを作る。グラフの辺に時間のメタデータを持ち、時間・全文・意味・グラフの検索を組み合わせる。RAG やエージェントに長期の記憶を与える。

### 38. Helicone

- LLM の費用管理、投資対効果の評価、リスク低減のためのオープンソースの LLMOps 基盤である。プロンプトの実験、監視、デバッグを提供する。まだ新しく、使いこなすには知識が要る。

### 39. Humanloop

- 重要な判断点に人のフィードバックを入れ、AI システムを信頼できるものにする基盤である。人によるラベル付け、評価、バージョン管理されたプロンプト、CI/CD 連携、ガードレールを持つ。規制の厳しい分野に向く。

### 40. Model Context Protocol (MCP)

- Anthropic が公開した、LLM アプリケーションを外部のデータやツールとつなぐオープン標準である。サーバーがデータにアクセスし、クライアントがそれをプロンプトに使う。
- 多くのコーディング支援がクライアントとして対応した。現状はローカルでサーバーを動かす使い方が主で、技術者以外には使いにくく、統制や更新管理の課題がある。

### 41. Open WebUI

- 自前で運用する AI 基盤で、OpenAI 互換の API や Ollama のローカルモデルにつなぎ、完全にオフラインでも動く。RAG、細かい権限管理、Python で拡張できる Functions、モデルを並べて比べる機能を持つ。

### 42. pg_mooncake

- PostgreSQL に列指向の保存とベクトル化実行を加える拡張である。列指向テーブルを Iceberg や Delta Lake の形式で保存し、専用の列指向データベースを足さずに重い分析ができる。

### 43. Reasoning models

- 段階的な思考や自己修正を強化学習などで鍛えた「考えるモデル」が急増した (o1・o3、DeepSeek R1、Gemini 2.0 Flash Thinking)。
- 応答が遅く、トークンも多く使う。要約や即答のチャットには一般的な LLM が向き、推論モデルは STEM、複雑な問題解決、LLM による採点などに使う。

### 44. Restate

- Apache Flink の作者による、Temporal に似た永続実行基盤である。Rust 製の単一バイナリで、ワークフローをコードで書け、saga パターンや永続的な状態機械を持つ。
- 分散トランザクションは避けるのが最善だが、避けられない環境では評価する価値がある。

### 45. Supabase

- PostgreSQL を土台にした、Firebase のオープンソースの代替である。認証、即時の API、Edge Functions、リアルタイム購読、ストレージ、ベクトル埋め込みを持つ。試作や MVP に向き、後で別の SQL 基盤へ移りやすい。

### 46. Synthesized

- 本番データのマスキングと部分抽出、または統計的に妥当な合成データの生成で、テストデータを作る基盤である。ハッシュや乱数化などで属性ごとに不可逆に匿名化し、ビルドパイプラインに組み込める。

### 47. Tonic.ai

- 本番に近く、個人を特定できない合成データを作る基盤である。差分プライバシーで統計的性質を保ち、非構造化データの機密情報を検出して伏せる。RAG や微調整に非構造化データを使うための機能もある。

### 48. turbopuffer

- オブジェクトストレージ上で、ベクトル検索と全文検索を組み合わせたサーバーレスの検索エンジンである。クエリノードは状態を持たず、何十億件の文書でも低遅延で検索できる。Cursor などで使われているが、招待制である。

### 49. VectorChord

- pgvecto.rs の後継となる PostgreSQL のベクトル検索拡張で、pgvector のデータ型と互換がある。IVF 索引と RaBitQ 量子化で、ディスク効率よく速く検索する。まだ初期段階である。

## Hold

### 50. Tyk hybrid API management

- 管理された制御面と自前のデータ面を組み合わせる構成で、制御面の障害を Tyk より先に自分たちが見つけるなど、可観測性の欠落が疑われる事例が複数あった。
- 障害時のサポートが遅く、文書も複雑な場面には不十分だった。特にハイブリッド構成には慎重に進める。

## See also

- [Thoughtworks Technology Radar Vol.32 の全体像と 4 つのテーマ](/references/ai/thoughtworks-technology-radar-vol-32/thoughtworks-radar-vol-32-overview.md)
- [Thoughtworks Technology Radar Vol.32: Techniques](/references/ai/thoughtworks-technology-radar-vol-32/thoughtworks-radar-vol-32-techniques.md)
