---
type: reference
title: 'Thoughtworks Technology Radar Vol.30: Platforms'
description: 'Thoughtworks Technology Radar Vol.30 (2024 年 4 月) の Platforms 象限 25 項目の要約で、イベントの標準形式、クラウドの Arm、Azure のマネージドサービス、IaC のオーケストレーション基盤、LLM アプリの開発・可観測性基盤、ベクトルデータベースをリングごとにまとめる。'
tags: [ai, thoughtworks, technology-radar, platform, cloud, llm, observability, data]
status: stable
verified: { by: claude-code/claude-opus-5-5, at: 2026-11-26T00:00:00Z }
stale_after: 2027-11-26T00:00:00Z
---

# Thoughtworks Technology Radar Vol.30: Platforms

Thoughtworks Technology Radar Vol.30 (2024 年 4 月) の Platforms (基盤) 象限の要約である。
クラウドとインフラの基盤に加え、LLM アプリケーションを作り観測するための基盤やベクトルデータベースが並ぶ。
今号の Platforms に Hold の項目は無い。

- 出典: Thoughtworks Technology Radar Volume 30 (PDF)、[thoughtworks.com/radar](https://www.thoughtworks.com/radar)

[TOC]

## Adopt

### 19. CloudEvents

- イベントデータを共通の形式で記述し、サービス・基盤・システムをまたいで相互運用できるようにする仕様である。CNCF の卒業プロジェクトで、複数言語の SDK がある。
- クラウドをまたぐ用途だけでなく、ドメインイベントの仕様にも使っている。イベント駆動アーキテクチャを作るときの既定として Adopt に移した。

## Trial

### 20. Arm in the cloud

- クラウドの Arm インスタンスは、x86 より費用とエネルギーの効率が良い。AWS、Azure、GCP が提供している。
- JVM のサービスや RDS などのデータベースも、コードを変えずビルドスクリプトの小さな変更で移行できた例が多い。アーキテクチャ固有の依存が無い限り、すべてのワークロードに Arm を勧める。マルチアーキテクチャの Docker イメージで構築も簡単になる。

### 21. Azure Container Apps

- コンテナのデプロイを簡単にする、マネージドな Kubernetes アプリ基盤である。AKS より運用の負担は小さいが、柔軟性と制御は減る。
- Azure Container Instances は本番には制約が多すぎることが多い。Container Apps は大きなコンテナでも良い結果が出ており、Dapr と KEDA にも対応する。

### 22. Azure OpenAI Service

- GPT-4、GPT-35-Turbo、埋め込み、DALL-E などのモデルを REST API、Python SDK、Web 画面から使えるサービスである。
- OpenAI 自身の API と比べ、Azure の企業向けセキュリティとコンプライアンス、プライベートネットワーク、コンテンツフィルター、モデルのバージョン管理がある。Azure を使っている企業には OpenAI API の代わりに勧める。

### 23. DataHub

- データ製品の考え方でデータを作るときに必要な、データの来歴、発見しやすさ、統治を支えるデータカタログである。
- プラグイン構造で独自のメタデータモデルを作れるようになった。データソースから処理、利用まで端から端の来歴を、push 型と自動収集の pull 型の両方で取れる。オープンソースのデータカタログとして既定の選択肢になりつつある。

### 24. Infrastructure orchestration platforms

- 自前のインフラのオーケストレーションのコードは、保守と障害対応に時間を取られがちである。インフラのコードの提供とデプロイの流れを標準化・製品化する基盤が出てきた。
- Terragrunt や Terraspace、Terraform Cloud や Pulumi Cloud、env0 や Spacelift、Terraform 専用の TACOS (Atlantis、Digger、Scalr、Terramate、Terrateam) などがある。差別化にならない自前のコードを減らすために使うことを勧める。

### 25. Pulumi

- Java と YAML への対応、大規模なインフラ管理、多くのクラウドの設定と連携を加えた。複数のクラウド向けにコードを書く場合の、Terraform の主な代替である。

### 26. Rancher Desktop

- Docker Desktop のライセンス変更を受けた代替で、無料のオープンソースのアプリである。macOS、Windows、Linux で、GUI 付きのローカル Kubernetes クラスターを使える。
- Colima は CLI 中心だが、Rancher Desktop は Docker Desktop の GUI を手放したくない人に向く。コンテナランタイムに dockerd と containerd を選べる。

### 27. Weights & Biases

- 実験の追跡、データセットのバージョン管理、モデルの性能の可視化と管理で、機械学習モデルを速く作るための基盤である。
- Traces で LLM の可観測性にも広がった。プロンプトチェーンの実行の流れ、途中の入出力、使用トークンや時間を可視化し、チェーンのデバッグに役立つ。

## Assess

### 28. Bun

- WebKit の JavaScriptCore で作られた新しい JavaScript ランタイムで、Node.js の置き換えを目指す。Zig で書かれた単一のバイナリが、バンドラー、トランスパイラー、パッケージマネージャーを兼ねる。
- 1.0 の安定版になった。起動の速さ、SSR の改善、高速なパッケージマネージャーがあり、評価を勧める。

### 29. Chronosphere

- 可観測性データの利用状況を追跡し、メトリクスごとの費用と価値を比べられるようにする。Metrics Usage Analyzer で、ほとんど使わないメトリクスを見つけて除外し、費用を大きく減らせる。

### 30. DataOS

- データメッシュの普及に合わせ、データ製品を第一級のものとして扱うデータ基盤である。データ製品の設計から運用までのライフサイクルを、YAML の宣言的な仕様で管理する。
- ABAC によるアクセス制御、データのフィルターやマスク、複数のデータソースの連合ができる。新規構築に向き、既存のデータ基盤との連携はまだ発展途上である。

### 31. Dify

- 画面操作で LLM アプリケーションを開発する基盤で、プロトタイプ作りを手軽にする。プロンプトテンプレートを使うチャットや文章生成のアプリ、取り込んだデータでの RAG、複数モデルに対応する。
- 一部の機能にバグや未完成な部分があり、本番にはまだ早い。ただし、これより良い競合は知らないとしている。

### 32. Elasticsearch Relevance Engine

- RAG ではベクトルデータベースが人気だが、全文検索とベクトル検索を組み合わせたハイブリッド検索のほうが良い結果になるという研究や報告がある。
- Elasticsearch Relevance Engine (ESRE) は、埋め込みモデル、ベクトル検索、Reciprocal Rank Fusion などによるハイブリッド検索に対応する。意味検索に対応した既存の検索基盤も見落とすべきではない。

### 33. FOCUS

- クラウドや SaaS の請求データは複雑で提供者ごとに違う。FinOps Open Cost and Usage Specification (FOCUS) は、用語、スキーマ、最低限の要件を定めた請求データの仕様である。
- まだ初期段階だが、普及すれば多数のクラウドと SaaS の支出を一望しやすくなる。

### 34. Gemini Nano

- Google の LLM ファミリー Gemini のうち、モバイルの専用チップで動くよう小さく最適化したモデルである。要約、文脈に合った返信、文法の修正などができる。
- 端末上で動くので遅延とプライバシーの懸念が減り、オフラインでも使える。Android AICore で組み込めるが、対応端末はまだ少ない。

### 35. HyperDX

- ログ、メトリクス、トレースの 3 つを統合したオープンソースの可観測性基盤である。ブラウザーのセッションの再生からログやトレースまで数クリックでたどれる。ClickHouse に全テレメトリを保存する。

### 36. IcePanel

- C4 モデルで、技術者と事業側が必要な詳細度までズームできるアーキテクチャのモデリングと作図を共同で行う道具である。オブジェクトとその接続を図の間で再利用でき、現状と将来像などの状態をバージョンとタグで管理できる。
- 図をコードとして扱いたいなら Structurizr がある。

### 37. Langfuse

- LLM アプリケーションの可観測性、テスト、監視のための基盤である。Python、JavaScript、TypeScript、OpenAI、LangChain、LiteLLM などに対応し、自前で運用するか有料のクラウドで使う。
- 複雑な LLM チェーンのデバッグ、出力の分析、利用者やモデルの版ごとの費用と遅延の監視で良い経験を得た。

### 38. Qdrant

- Rust で書かれたオープンソースのベクトルデータベースである。複数ノードへの水平拡張が必要なら、PostgreSQL 拡張の pgvector より Qdrant の評価を勧める。SIMD による高速化があり、ベクトルに JSON のペイロードを付けられる。

### 39. RISC-V for embedded

- RISC-V は性能や効率で Arm を上回るわけではないが、オープンでモジュール化され、特定の企業に縛られない。独自アーキテクチャのライセンス料が問題になる組み込み機器で魅力がある。
- SiFive や Espressif が開発ボードや SoC を出しており、Linux を動かせるものもある。今後の普及を見込んでいる。

### 40. Tigerbeetle

- 財務会計のためのオープンソースの分散データベースである。安全性と性能のためにドメイン専用の状態機械として設計され、Viewstamped Replication でノード間に決まった順序で複製する。
- 厳密な直列化可能性を保証した複式簿記の実装という設計判断を評価している。

### 41. WebTransport

- HTTP/3 の上に作られた、サーバーとアプリの双方向通信のプロトコルである。WebSocket より接続が速く遅延が低く、順序付きの信頼できるストリームと UDP のような順序なしのデータの両方を扱える。
- 1 つの接続で複数のストリームを先頭のブロッキングなしで扱える。ブラウザーの対応は進行中で、リアルタイムの IoT アプリへの利用を評価している。

### 42. Zarf

- オフラインや接続が限られる Kubernetes 環境のための、宣言的なパッケージマネージャーである。ネットにつながる環境でアプリをまとめ、切り離された環境に運んでデプロイする。
- SBOM の自動生成、組み込みの Docker レジストリ、Gitea、K9s のダッシュボードを持つ。

### 43. ZITADEL

- Keycloak の代替となる、オープンソースの ID・利用者管理の道具である。Go で書かれて軽く、設定と運用が簡単である。
- マルチテナントで、特に B2B アプリの認証に向き、多要素認証や監査証跡を備える。

## See also

- [Thoughtworks Technology Radar Vol.30 の全体像と 4 つのテーマ](/references/ai/thoughtworks-technology-radar-vol-30/thoughtworks-radar-vol-30-overview.md)
- [Thoughtworks Technology Radar Vol.30: Techniques](/references/ai/thoughtworks-technology-radar-vol-30/thoughtworks-radar-vol-30-techniques.md)
- [Thoughtworks Technology Radar Vol.35: Platforms](/references/ai/thoughtworks-technology-radar-vol-35/thoughtworks-radar-vol-35-platforms.md)
