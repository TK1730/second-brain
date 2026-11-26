---
type: reference
title: 'Thoughtworks Technology Radar Vol.33: Tools'
description: 'Thoughtworks Technology Radar Vol.33 (2025 年 11 月) の Tools 象限 28 項目の要約で、分析用データベース、LLM のガードレール、Claude Code と Context7 などの AI コーディングの道具、AI によるデザインの道具、GPU と MCP の運用の道具をリングごとにまとめる。'
tags: [ai, thoughtworks, technology-radar, tools, coding-agent, mcp, design]
status: stable
verified: { by: claude-code/claude-opus-5-5, at: 2026-11-26T00:00:00Z }
stale_after: 2027-11-26T00:00:00Z
---

# Thoughtworks Technology Radar Vol.33: Tools

Thoughtworks Technology Radar Vol.33 (2025 年 11 月) の Tools (道具) 象限の要約である。
Claude Code や Context7 などの AI コーディングの道具、AI を使ったデザインとプロトタイプの道具、データと GPU の運用の道具が並ぶ。
今号の Tools に Hold の項目は無い。

- 出典: Thoughtworks Technology Radar Volume 33 (PDF)、[thoughtworks.com/radar](https://www.thoughtworks.com/radar)

[TOC]

## Adopt

### 57. ClickHouse

- リアルタイム分析のための、オープンソースの分散・列指向の OLAP データベースである。増分のマテリアライズドビュー、効率的なクエリエンジン、強い圧縮で対話的なクエリに向く。
- 近似の集計関数で精度と性能を交換できる。S3 互換ストレージで保存と計算を分けられる。OpenTelemetry のデータや Sentry のようなクラッシュ分析の保存先としても優れている。

### 58. NeMo Guardrails

- NVIDIA のオープンソースの道具で、LLM の会話アプリにプログラム可能な安全・制御の仕組みを加える。出力を安全で話題に沿った、規則に合うものに保つ。
- 専用言語 Colang で会話の流れを定義し、決められた手順を強制する。入出力の内容安全、セキュリティ、モデレーションに対応する。採用が進み、機能も成熟したため Adopt に移った。

### 59. pnpm

- Node.js のパッケージマネージャーで、速度とディスク容量の両方で他より大きく優れる。複数プロジェクトの重複したパッケージを、ディスク上の 1 か所へのハードリンクにする。
- 互換性の問題がほとんど無く、フィードバックがずっと速いため、Node.js のパッケージ管理の既定の選択肢になった。

### 60. Pydantic

- 標準の型ヒントでデータモデルを定義し、実行時にスキーマを強制する Python のライブラリである。Rust 製の高速な中核で、検証、解析、直列化を行う。
- Web API だけでなく LLM アプリでも欠かせない。構造化出力の手法で、LLM の自由な文章を型安全な Python のオブジェクトに変える安全網になる。
- 成熟度、性能、信頼性から、本番の Python の AI アプリでの既定の選択肢になった。

## Trial

### 61. AI Design Reviewer

- デザインの監査やヒューリスティック評価を行い、具体的なフィードバックを集める Figma のプラグインである。UX の批評、UI の不整合、アクセシビリティの欠落、文言の質、例外ケースを見る。
- 古いデザインの良い体験と悪い体験を見分けて刷新の目標を決めたり、開発に渡す前の仲間のレビューの代わりにしたりした。

### 62. Barman

- PostgreSQL のバックアップと災害復旧を管理するオープンソースの道具である。物理バックアップの作成、カタログ化、特定時点への復旧 (PITR) を備える。
- 移行作業での PITR の速さに感心した。スケジュールと保持期間の複雑な組み合わせにも対応できる。

### 63. Claude Code

- Anthropic のエージェント型の AI コーディングの道具で、自然言語の画面と、複雑な多段の作業を計画・実行するエージェントの実行モデルを持つ。公開から 1 年足らずで広く採用され、Trial に置いた。
- Codex CLI、Gemini CLI、OpenCode などのコンソール型エージェントや、Cursor などの IDE のエージェントモードが出ても、Claude Code は人気がある。コードだけでなく、仕様、ストーリー、設定、インフラ、文書の管理にも汎用エージェントとして使われている。
- エージェントによるコーディングは慢心を招きやすい。コンテキストエンジニアリング、チームで共有する指示、team of coding agents などで、Claude Code の働き方をしっかり管理することが欠かせない。

### 64. Cleanlab

- データ中心の AI では、モデルの調整よりデータの質の改善のほうが効果が大きいことが多い。Cleanlab は、テキスト、画像、表、音声のデータの誤ったラベル、外れ値、重複を自動で見つける Python のライブラリである。
- モデルの予測確率からラベルの雑音を推定する (confident learning)。本番で効果を確かめている。

### 65. Context7

- LLM が古い学習データに頼るせいで起きるコード生成の誤りに対処する MCP サーバーである。プロジェクトが使うライブラリの最新の文書とコード例を元のリポジトリから取り、プロンプトの時点でコンテキストに差し込む。
- コードの幻覚と古い知識への依存を大きく減らした。Claude Code、Cursor、VS Code に設定して使える。

### 66. Data Contract CLI

- Data Contract の仕様を扱うオープンソースの CLI である。データ契約の作成と編集に加え、データが契約に合っているかを検証できる。
- Avro、SQL DDL、Open Data Contract Standard など多くのスキーマ形式に対応し、版の比較で互換性を壊す変更をすぐに見つける。データメッシュで CI/CD に組み込み、データ製品間の契約を運用するのに役立つ。

### 67. Databricks Assistant

- Databricks に組み込まれた AI の対話ツールで、データの専門家のペアプログラマーとして働く。Unity Catalog のメタデータなど、Databricks の環境とデータの文脈を理解している点が汎用のアシスタントと違う。
- 多段の SQL や Python のクエリの作成、エラーの診断、ワークスペースに即した説明ができる。

### 68. Hoppscotch

- API の開発、デバッグ、テスト、共有のための軽いオープンソースの道具である。HTTP、GraphQL、WebSocket に対応し、Web、デスクトップ、CLI で使える。
- Postman などと比べ、軽く、分析を送らず、ローカルファーストの保存と自前運用に対応するプライバシーへの配慮が際立つ。

### 69. NVIDIA DCGM Exporter

- 大規模な分散 GPU 学習の監視を助けるオープンソースの道具である。NVIDIA Data Center GPU Manager の独自の計測データを、一般的な監視システムで使える形式に変える。
- GPU の使用率、温度、電力、ECC エラーを Prometheus や Grafana で見られる。1 台の遅い機械が全体を止める straggler 効果は、スループットを 10% 以上下げ、GPU 時間の最大 45% を無駄にすることがある。

### 70. RelationalAI

- Snowflake のネイティブアプリとして動き、Snowflake のテーブルに対して業務の概念、実体、複雑なロジックをモデルとして組み込む。
- Graph Reasoner で、そのモデルから関係の知識グラフを作り、分析し、可視化できる。大量で変化の速いデータから隠れたパターンを見つけるのに役立つ。

### 71. UX Pilot

- ワイヤーフレームから高い完成度の画面とレビューまで、UX デザインの複数の段階を支える AI の道具である。文章や画像から画面、流れ、レイアウトを生成し、Figma に書き出せる。
- アイデア出しや、ストーリーの一覧からプロダクトビジョンのボードを作るのに使った。プロダクトマネージャーのようなデザイナー以外も素早く試作できる。

### 72. v0

- 前回から進化し、プロダクトマネージャーが UI のプロトタイプを作って調整しやすいデザインモードが加わった。大きなコンテキストとマルチモーダルに対応した自社モデルで、文章と画像の両方から UI を生成・改善できる。
- 複雑な作業を分解し、作業ごとにモデルを選ぶエージェントモードも加わったが、まだ新しく評価は分かれている。

## Assess

### 73. Augment Code

- 大きなコードベースで文脈を深く理解した支援をする AI コーディングアシスタントである。高度なコンテキストエンジニアリングで、コードが頻繁に変わっても索引の更新と取得が速い。
- Claude や GPT のモデル、GitHub や Jira との連携、MCP に対応する。リファクタリングや依存の更新などの複雑な変更を段階的に案内する。

### 74. Azure AI Document Intelligence

- 非構造の文書から、テキスト、表、キーと値の組を取り出して構造化データにする (旧 Form Recognizer)。学習済みモデルでレイアウトと意味を読み取り、ノーコードで独自モデルも作れる。
- 手入力を大きく減らした例がある。同期的な利用者の操作に組み込むと遅延が出ることがあるので、主に非同期の処理に使う。オープンソースの代替として Docling がある。

### 75. Docling

- PDF や PowerPoint などの実際の文書を、機械が読める形式に変える「最後の一歩」を担うオープンソースの Python と TypeScript のライブラリである。
- コンピュータービジョンでレイアウトと意味の構造を読み取り、JSON や Markdown に変えるので、RAG のパイプラインに特に役立つ。IBM Research が支え、Azure の文書処理などの独自のクラウドサービスに代わる、自前運用の柔軟な選択肢になる。

### 76. E2B

- AI が生成したコードを、クラウドの安全に隔離されたサンドボックスで動かすオープンソースの道具である。Firecracker の microVM の上に作られている。
- エージェントがコードの実行、データ分析、調査、仮想マシンの操作を安全に行え、実行環境を完全に制御できる。

### 77. Helix editor

- Vim の代わりを目指すシンプルなテキストエディターの 1 つである。複数カーソル、Tree-sitter、組み込みの Language Server Protocol (LSP) 対応を持つ。
- Vim に慣れた人に馴染みやすく、現代的な便利さを少し加えた軽いモード型エディターである。プラグインの仕組みも開発中である。

### 78. Kueue

- Kubernetes ネイティブのジョブのキューの制御器で、クォータと資源の消費を管理する。優先度や資源の要求が違うワークロードについて、いつ受け入れ、いつ追い出すかを決める。
- kube-scheduler や cluster-autoscaler を置き換えず、順番、クォータ、優先度、トポロジーに基づくジョブの受け入れに集中する。Kubeflow などの機械学習のワークロードに向く。

### 79. MCP-Scan

- MCP サーバーのためのセキュリティスキャナーで、2 つのモードを持つ。scan モードは設定とツールの説明を調べ、プロンプトインジェクション、ツールの汚染、toxic flow を見つける。
- proxy モードはエージェントと MCP サーバーの間に入って通信を監視し、ツール呼び出しの検証、個人情報の検出、データの流れの制約などの規則を強制する。悪意あるプロンプトを受け入れても、有害な操作は実行させない。

### 80. oRPC

- OpenAPI の仕様に完全に従いながら、TypeScript で端から端まで型安全な API を作る。OpenAPI の仕様を自動で生成できる。
- tRPC などは新しいフレームワークの採用が必要になりがちだが、oRPC は Express、Fastify、Hono、Next.js などの既存のフレームワークにそのまま組み込める。

### 81. Power user for dbt

- dbt と dbt Cloud に直接つながる VS Code の拡張である。コード補完、クエリ結果のリアルタイム表示、モデルと列の系統 (lineage) の可視化を IDE の中で行える。
- パイプラインのエラーが減り、開発体験が良くなったという報告がある。dbt を使うなら見る価値がある。

### 82. Serena

- Claude Code などのコーディングエージェントに、IDE のような意味に基づくコードの検索と編集の能力を与える道具である。シンボル単位で動き、コードの関係の構造を理解する。
- ファイル全体を読んだり文字列置換に頼ったりせず、`find_symbol` や `insert_after_symbol` などで正確に編集できるので、トークン効率が大きく上がる。小さなプロジェクトでは効果が小さいが、コードベースが大きくなるほど価値が高い。

### 83. SweetPad

- VS Code や Cursor で、Apple のプラットフォーム向けの Swift アプリ開発の全工程を行える拡張である。Xcode に切り替えずに、ビルド、実行、デバッグ、シミュレーターの管理、実機への配置ができる。

### 84. Tape/Z (Tools for Assembly Program Exploration for Z/OS)

- メインフレームの HLASM (High-Level Assembler) のコードを解析する道具で、構文解析、制御フローのグラフ、依存関係の追跡、フローチャートの可視化を備える。Thoughtworks の社員が開発した。
- 独自製品ばかりのメインフレームの分野で、オープンでスクリプトから使える解析の道具を提供する。COBOL 向けの COBOL REKT と並ぶ前進である。

## See also

- [Thoughtworks Technology Radar Vol.33 の全体像と 4 つのテーマ](/references/ai/thoughtworks-technology-radar-vol-33/thoughtworks-radar-vol-33-overview.md)
- [Thoughtworks Technology Radar Vol.33: Techniques](/references/ai/thoughtworks-technology-radar-vol-33/thoughtworks-radar-vol-33-techniques.md)
- [Thoughtworks Technology Radar Vol.35: Tools](/references/ai/thoughtworks-technology-radar-vol-35/thoughtworks-radar-vol-35-tools.md)
