---
type: reference
title: 'Thoughtworks Technology Radar Vol.31: Languages and frameworks'
description: 'Thoughtworks Technology Radar Vol.31 (2024 年 10 月) の Languages and Frameworks 象限 31 項目の要約で、dbt と Testcontainers の定番、LLM アプリの構築・評価・ガードレールのフレームワーク、自動運転やロボット向けの基盤をリングごとにまとめる。'
tags: [ai, thoughtworks, technology-radar, frameworks, llm, data-engineering, rag]
status: stable
verified: { by: claude-code/claude-opus-5-5, at: 2026-11-26T00:00:00Z }
stale_after: 2027-11-26T00:00:00Z
---

# Thoughtworks Technology Radar Vol.31: Languages and frameworks

Thoughtworks Technology Radar Vol.31 (2024 年 10 月) の Languages and Frameworks (言語・フレームワーク) 象限の要約である。
LLM アプリを作り、評価し、守るためのフレームワークが多く、データエンジニアリング、自動運転やロボット、組み込み UI の基盤も並ぶ。
今号のこの象限に Hold の項目は無い。

- 出典: Thoughtworks Technology Radar Volume 31 (PDF)、[thoughtworks.com/radar](https://www.thoughtworks.com/radar)

[TOC]

## Adopt

### 75. dbt

- ELT パイプラインのデータ変換を実装する、堅実で妥当な選択肢である。SQL の変換をモジュール化し、テストし、再利用しやすくする。
- dbt core 1.8 以降で単体テストにネイティブ対応した。静的なテストデータと期待する出力を定義でき、自前のスクリプトを廃止できた例が多い。

### 76. Testcontainers

- データベース、キュー、クラウドサービス、ブラウザーなど、テストの依存先を Docker で用意するライブラリで、多くの言語に移植されている。信頼できるテスト環境を作る既定の選択肢である。
- デスクトップ版が出て、テストのセッションを画面で管理できるようになった。

## Trial

### 77. CAP

- Outbox パターンを実装する .NET のライブラリである。イベントを発行する意図を、そのイベントを起こしたデータベースのトランザクションの中に記録し、更新と発行を不可分にする。
- 複数のデータベースと RabbitMQ や Kafka などに対応し、少なくとも 1 回の配送を保証する。

### 78. CARLA

- 自動運転の研究用のオープンソースのシミュレーターで、本番の前に自動運転システムを試すのに使う。歩行者の飛び出しなどの場面を 3D モデルで再現できる。

### 79. Databricks Asset Bundles

- Databricks の資産 (ワークフロー、タスク、実行するコード) をまとめ、CI/CD で複数の環境に配備する道具で、データチームにソフトウェア工学の実践を広げる。
- ノートブックをそのまま本番に出すことは勧めず、工学的な実践で本番のコードを書くことを勧めている。

### 80. Instructor

- LLM から構造化された出力 (JSON や YAML) を得るためのライブラリである。出力の構造を定義し、従わなかったときの再試行を設定できる。
- ストリーミングの途中の部分的な構造も解析できる。

### 81. Kedro

- MLOps の道具として大きく改善した。データとコードを切り離す kedro-datasets パッケージ、CLI とテンプレートの改善、VS Code 拡張が加わった。

### 82. LiteLLM

- 多くの LLM 提供者の API を OpenAI 形式に揃えて使えるライブラリである。キャッシュ、ログ、流量制限、負荷分散など、本番に要る運用機能の枠組みもある。
- モデルを差し替えやすくなるが、同じプロンプトでもモデルによって応答は違い、追加機能の実装もそれぞれ違う。LiteLLM 経由で AWS Bedrock の関数呼び出しを使いにくかった例がある。

### 83. LlamaIndex

- 領域特化の、文脈を補強した LLM アプリを作るためのエンジン群である。文書の取り込み、ベクトルの索引付け、文書への質問応答などを支援する。
- 文書の取り込みから埋め込みの索引付け、検索までを自動化する RAG パイプラインを作った。LlamaHub で部品を拡張できる。

### 84. LLM Guardrails

- LLM が有害、誤解を招く、無関係な内容を生成しないようにし、入力操作などの悪用からアプリを守る指針・ポリシー・フィルターである。NeMo Guardrails、Guardrails AI、Aporia Guardrails などがある。
- すべての LLM アプリにガードレールを入れ、その規則を改善し続けることを勧めている。

### 85. Medusa

- 高度にカスタマイズできるオープンソースの EC 基盤で、「80% は簡単に作れるが残り 20% が作れない」問題に陥りにくい。Next.js と PostgreSQL で作られ、カートや注文管理から税計算まで部品がそろう。

### 86. Pkl

- Apple が社内用に作ったオープンソースの設定言語と道具である。型と検証の仕組みで、配備前に設定の誤りを見つけられる。
- 環境ごとの上書きなどの重複を減らせる。JSON、PLIST、YAML、.properties を生成でき、IDE との連携やコード生成もある。

### 87. ROS 2

- ロボットシステム開発のためのオープンソースのフレームワークである。プロセス間通信、マルチスレッド実行、サービス品質などを部品として提供する。
- 前世代よりリアルタイム性能とモジュール性が上がり、自動運転などの車載アプリで採用が広がっている。

### 88. seL4

- 形式検証で振る舞いが仕様どおりであることを数学的に保証する、高信頼・高性能の OS マイクロカーネルである。
- ソフトウェア定義車両など安全が重要な分野は少数の企業が独占しており、オープンソースの選択肢として貴重である。

### 89. SetFit

- 文の分類や意図の判定に使う sentence transformers を微調整するフレームワークである。対照学習で、25 件以下のわずかな例でも意図のクラスをはっきり分けられることが多い。
- LLM を使うチャットボットで、より厳しい入力の絞り込みのために SetFit の分類器を使った。

### 90. vLLM

- 高スループットでメモリ効率の良い LLM の推論エンジンで、クラウドでも自社環境でも動く。OpenAI の SDK と互換がある。
- GPU 基盤に Docker 化した vLLM ワーカーを置き、コーディング支援や知識検索に使っている。大規模なモデル配備の既定になりつつある。

## Assess

### 91. Apache XTable™

- Hudi、Delta、Iceberg のテーブル形式の間で、データを複製せずにメタデータを変換し、全方向の相互運用を可能にする Apache のインキュベーションプロジェクトである。
- 複数の形式を試すチームには役立つが、長く頼ると各形式の共通部分の機能しか使えなくなるおそれがある。

### 92. dbldatagen

- Databricks 環境でテストやベンチマーク用の合成データを作る Python ライブラリである。数分で数十億行を作れ、複数テーブルや変更データキャプチャにも対応する。

### 93. DeepEval

- LLM の性能を評価する Python のオープンソースのフレームワークである。RAG アプリの評価やモデルの比較に使え、幻覚の検出や回答の関連性などの指標を持つ。
- pytest と連携し、CI に評価を組み込める。

### 94. DSPy

- 手で調整したプロンプトの代わりに、モジュールの組み合わせ、最適化する指標、学習・テスト用データという高い抽象で LLM アプリを作るフレームワークである。
- 指標に基づいてプロンプトやモデルの重みを最適化する。PyTorch での学習に似たコードになり、新鮮な発想として試す価値がある。

### 95. Flutter for Web

- 同じコードから iOS、Android、ブラウザー向けのアプリを作れる。PWA、SPA、既存の Flutter のモバイルアプリの Web 化に向く。
- WASM へのコンパイルが安定版になり、JavaScript 向けよりはるかに速く動く。

### 96. kotaemon

- 知識ベースの文書に質問応答するアプリを作る、RAG ベースのオープンソースの道具・フレームワークである。PDF などを理解し、Gradio の Web 画面でチャットできる。
- 回答に出典の文書、プレビュー、関連度を示す。RAG の文書 Q&A アプリの良い出発点になる。

### 97. Lenis

- 滑らかなスクロールのための軽量なライブラリで、WebGL との同期や視差効果を作れる。縦横のスクロールでアクセシビリティの問題が起きうるので、慎重に実装する。

### 98. LLMLingua

- 小さな言語モデルで不要なトークンを取り除き、性能をほとんど落とさずにプロンプトを圧縮する。費用、遅延、長い文脈の扱いの課題に対応する。

### 99. Microsoft Autogen

- 複数の AI エージェントの作成と連携を簡単にするオープンソースのフレームワークで、自律的な流れにも人が関わる流れにも対応する。
- コード生成、レビュー、文書要約などの技能ごとにエージェントを作る基盤に使った。エージェントが増えたときの拡張性と複雑さの管理には懸念が残る。

### 100. Pingora

- Cloudflare が Nginx の弱点を補うために作った、速く信頼できるネットワークサービスを作る Rust のフレームワークである。River などの新しいプロキシがこの上に作られている。

### 101. Ragas

- RAG パイプラインの検索と生成の両方を評価するフレームワークで、忠実性、回答の関連性、文脈の利用度などの指標を持つ。
- top-k や埋め込みモデルの調整のための定期評価に使えるが、複雑な RAG の細かい相互作用までは捉えきれないので、他の評価も併用する。

### 102. Score

- コンテナのワークロードをどう配備し、どのサービスや設定が要るかを YAML で宣言する言語である。Humanitec が作り、現在は CNCF が管理している。
- 社内開発基盤の配備要件を表す共通言語になる可能性がある。Kubernetes と Docker Compose の参照実装がある。

### 103. shadcn

- コンポーネントをライブラリとして依存するのではなく、コピーして自分のコードベースの一部にする。完全な所有と制御ができ、MUI や Chakra UI より拡張しやすい。
- Radix UI と Tailwind CSS で作られ、React アプリに組み込める。コピーを助ける CLI がある。

### 104. Slint

- Rust、C++、JavaScript のアプリでネイティブの UI を作る宣言的な GUI フレームワークである。HTML に似た記法で書き、機械語にコンパイルする。
- 実行時の資源消費が小さく、選択肢の少なかった組み込みシステムの UI 開発に Web やモバイルの実践を持ち込む。

### 105. SST

- アプリケーションと、それが動くのに要るクラウドのサービスをまとめて配備するフレームワークである。TypeScript の API で環境を定義し、Git の push で配備し、管理画面も持つ。
- 最新版は Terraform と Pulumi の上に作られ、理論上はクラウドに依存しない。AWS Lambda の呼び出しを手元の関数に転送するライブモードなどの便利機能がある。

## See also

- [Thoughtworks Technology Radar Vol.31 の全体像と 4 つのテーマ](/references/ai/thoughtworks-technology-radar-vol-31/thoughtworks-radar-vol-31-overview.md)
- [Thoughtworks Technology Radar Vol.31: Techniques](/references/ai/thoughtworks-technology-radar-vol-31/thoughtworks-radar-vol-31-techniques.md)
- [Thoughtworks Technology Radar Vol.31: Platforms](/references/ai/thoughtworks-technology-radar-vol-31/thoughtworks-radar-vol-31-platforms.md)
- [評価駆動開発 (EDD) とは何か: AI エージェントを継続的に改善する手法](/references/ai/langchain-blog-what-is-eval-driven-development.md)
