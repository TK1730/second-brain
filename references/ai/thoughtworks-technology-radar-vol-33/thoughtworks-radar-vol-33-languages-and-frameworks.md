---
type: reference
title: 'Thoughtworks Technology Radar Vol.33: Languages and Frameworks'
description: 'Thoughtworks Technology Radar Vol.33 (2025 年 11 月) の Languages and Frameworks 象限 30 項目の要約で、Node.js と Web のフレームワーク、LangGraph や Pydantic AI などのエージェントのフレームワーク、LLM の推論と評価、MCP サーバーの開発をリングごとにまとめる。'
tags: [ai, thoughtworks, technology-radar, frameworks, agent, llm, typescript, python]
status: stable
verified: { by: claude-code/claude-opus-5-5, at: 2026-11-26T00:00:00Z }
stale_after: 2027-11-26T00:00:00Z
---

# Thoughtworks Technology Radar Vol.33: Languages and Frameworks

Thoughtworks Technology Radar Vol.33 (2025 年 11 月) の Languages and Frameworks (言語・フレームワーク) 象限の要約である。
エージェントを作るフレームワーク、LLM の推論・評価・可観測性のライブラリ、TypeScript と Web のフレームワークが並ぶ。
今号のこの象限に Hold の項目は無い。

- 出典: Thoughtworks Technology Radar Volume 33 (PDF)、[thoughtworks.com/radar](https://www.thoughtworks.com/radar)

[TOC]

## Adopt

### 85. Fastify

- Node.js の高速で、考え方を押しつけず、オーバーヘッドの小さい Web フレームワークである。解析、検証、直列化と、強いプラグインの仕組みを持つ。
- Express.js などと比べて目立った欠点が無く、測れる性能の向上があった。

### 86. LangGraph

- LLM を使った、状態を持つマルチエージェントのアプリを作るためのオーケストレーションのフレームワークである。ノードとエッジという低水準の部品で、ワークフロー、メモリ、状態の保存を細かく制御できる。
- ストリーミング、高度なコンテキスト管理、モデルのフォールバックやツールのエラー処理を備える。軽くモジュール化された設計で、マルチエージェントのシステムで良い結果を出している。

### 87. vLLM

- クラウドでも自社環境でも動く、高スループットでメモリ効率の良い LLM の推論エンジンである。多くのモデルの構造と人気のオープンソースモデルに対応する。
- Docker 化した vLLM のワーカーを GPU 基盤で動かし、コーディング支援や知識検索に使っている。OpenAI の SDK の形式に互換で、Azure の AI Model Catalog も既定の推論エンジンにしている。大規模なモデルの配置での定番になった。

## Trial

### 88. Crossplane

- Kubernetes のクラスターを拡張する用途で採用が増えている。ただし汎用の IaC ではなく、特定の用途で真価を発揮する。
- Kubernetes 内のワークロードに寄り添う補助として使うのが最良で、Terraform の完全な代替にはしない。主要な IaC に全面的に採用したチームは苦労し、特定の用途に絞ったチームは良い結果を得た。IaC を土台にし、その上に Crossplane を重ねる。

### 89. DeepEval

- LLM の性能を評価する、オープンソースの Python のフレームワークである。RAG や、LlamaIndex や LangChain で作ったアプリの評価、モデルの比較に使える。
- 単語の一致を超えて、正確さ、関連性、一貫性を評価する。幻覚の検出や、独自の指標を作る GEval を備え、pytest や CI/CD に組み込める。規制の厳しい環境では、監査に強い Inspect AI も選択肢である。

### 90. FastMCP

- MCP サーバーの実装には、準備、プロトコルの処理、エラー管理の決まりきったコードが多く要る。FastMCP は、Python のデコレーターで MCP の資源とツールを定義できるようにし、プロトコルの複雑さを隠すフレームワークである。
- FastMCP 1.0 は公式の SDK に取り込まれている。MCP の標準は変化が速いので、2.0 の動向と公式の仕様の変更を追う。

### 91. LiteLLM

- 標準の OpenAI の API 形式で、多くの LLM の提供者につながる SDK である。テキスト生成、埋め込み、画像生成を統一した画面で扱い、提供者ごとの API の違いを吸収する。
- プロキシの仕組みで、ガードレール、キャッシュ、ログ、流量制限、負荷分散を備える。AI ゲートウェイとして、組織全体の AI の利用を標準化し、安全にし、可視化するのに使っている。

### 92. MLForecast

- 機械学習のモデルで大規模な時系列予測を行う Python のフレームワークである。ラグや移動統計などの特徴量の生成を自動化し、Spark や Dask の分散処理にネイティブに対応する。
- 共形予測などで予測の不確かさも示せる。評価では数百万件のデータに効率よく拡張し、比較した道具を上回った。

### 93. Nuxt

- Vue.js の上に作られた、フルスタックの Web アプリのためのメタフレームワークで、「Vue.js 版の Next.js」と呼ばれる。事前描画、サーバーサイドレンダリング、メタデータ管理など SEO に強い機能を持つ。
- Next.js と同じ Vercel が支え、画像処理やサイトマップ、Tailwind CSS などのモジュールが充実している。

### 94. Phoenix

- Elixir で書かれたサーバーサイドの MVC フレームワークである。Ruby on Rails の開発体験の学びを生かしつつ、関数型の考え方に進んでいる。
- Phoenix LiveView 1.0 が出た。HTMX や Hotwire に似た、サーバーで描画した HTML でリアルタイムの体験を作る仕組みで、React や Vue.js のようなコンポーネントの構造を持つ。完全な JavaScript のフレームワークなしに対話的な画面を作れる。

### 95. Presidio

- 構造化・非構造化テキストから個人情報 (カード番号、氏名、場所など) を検出し、匿名化する SDK である。固有表現抽出、正規表現、規則を使い、独自の認識器や匿名化の流れも作れる。
- LLM と連携する厳しいデータ共有の環境で使った。見逃しや誤検出があるので、結果を過信しない。

### 96. Pydantic AI

- 本番で GenAI のエージェントを作るための、安定してよく支えられたオープンソースのフレームワークである。Pydantic の土台の上に、強い型安全、OpenTelemetry による可観測性、評価の道具を備える。
- 2025 年 9 月 4 日に 1.0 が出た。MCP のサーバーとクライアントの実装がしやすくなり、AG-UI や A2A にも対応した。

### 97. Tauri

- 1 つの Web UI のコードから高性能なデスクトップアプリを作るフレームワークである。Electron と違い Rust で作られ、OS 標準の Web ビューを使うので、バイナリが小さく安全である。
- iOS と Android にも対応した。最新版は柔軟な権限とスコープの仕組みと強化したプロセス間通信を持ち、外部のセキュリティ監査も受けている。

## Assess

### 98. Agent Development Kit (ADK)

- プロンプトだけに頼らず、ソフトウェアエンジニアリングの規律で AI エージェントを開発・配置するフレームワークである。クラス、メソッド、ワークフローのパターン、CLI など馴染みのある抽象を持つ。
- Google の AI 基盤と深く統合され、A2A プロトコルにも対応する。GCP を使う組織には有望な土台だが、まだ初期段階である。

### 99. Agno

- マルチエージェントのシステムを作り、動かし、管理するフレームワークである。完全に自律したエージェントも、段階を決めたワークフローも作れ、人の承認、セッション管理、メモリ、知識を備える。
- 起動が速くメモリ消費が少ない。FastAPI 製の実行環境 AgentOS で、テスト、監視、管理ができる。

### 100. assistant-ui

- AI のチャット画面のための、オープンソースの TypeScript と React のライブラリである。ストリーミング、メッセージの編集と分岐の状態管理など、チャット画面の難しい部分を受け持つ。
- 部品は Radix のプリミティブで自分で作れる。Vercel AI SDK や LangGraph と連携できる。

### 101. AutoRound

- Intel による、LLM や VLM などの大きなモデルを、精度をほとんど落とさずに圧縮する量子化のアルゴリズムである。2〜4 ビットまで下げ、層ごとにビット幅を変える。
- 70 億パラメーターのモデルを 1 台の GPU で数分で量子化できる。vLLM や Transformers と連携する。

### 102. Browser Use

- LLM のエージェントが Web ブラウザーを操作するためのオープンソースの Python のライブラリである。移動、入力、テキストの抽出、複数タブの操作ができ、Playwright で画面の理解と HTML の構造を組み合わせる。
- Pytest と Allure に組み込み、自然言語で書いたテスト手順をエージェントに実行させる試みをした。結果は有望だが、失敗の説明が不足しがちで、独自のエラー報告が要る。

### 103. DeepSpeed

- 深層学習の分散学習と推論を最適化する Python のライブラリである。学習では ZeRO と 3D 並列で何千もの GPU に拡張し、推論では複数の並列化と専用カーネルで遅延を減らす。
- Megatron-Turing NLG や BLOOM などの巨大なモデルを支えた。Hugging Face Transformers などと連携する。

### 104. Drizzle

- 軽い TypeScript の ORM で、SQL に近い API と従来の ORM 風の問い合わせの両方を持つ。既存のデータベースからスキーマを取り出せ、データベース起点とコード起点の両方に対応する。
- サーバーレスを意識し、バンドルが小さく、事前にコンパイルした文 (prepared statement) を使える。

### 105. Java post-quantum cryptography

- Java 24 で、ML-KEM や ML-DSA などの耐量子暗号のアルゴリズムが使えるようになった。.NET 10 も対応を広げた。
- これらの言語で作るなら、将来に備えて今から耐量子のアルゴリズムを採用し始めることを勧めている。

### 106. kagent

- Kubernetes のクラスターの中でエージェントの AI を動かすオープンソースのフレームワークである。LLM のエージェントが、問題の診断や設定の修正などの運用作業を、Kubernetes の API や MCP を通じて計画・実行する。
- CNCF の Sandbox 段階で、LLM に運用の権限を与えるリスクがあるので慎重に導入する。toxic flow analysis でリスクを評価する。

### 107. LangExtract

- 利用者が決めた指示に基づき、LLM で非構造のテキストから構造化された情報を取り出す Python のライブラリである。取り出した各データ点を元の文章にたどれる。
- 結果を .jsonl で書き出し、対話的な HTML で確かめられる。ドメインの知識グラフを作るための実体の抽出に有効だった。

### 108. Langflow

- LLM のワークフローを作り可視化する、オープンソースのローコード基盤である。LangChain の上に作られ、プロンプト、ツール、ベクトル DB、メモリをドラッグ & ドロップでつなぐ。Python のコードも書ける。
- 本番にはまだ粗い部分がある。ワークフローをコードとして定義しバージョン管理できる点で、ローコードの欠点を一部和らげられる。

### 109. LMCache

- LLM の提供基盤を速くする KV キャッシュの仕組みである。会話の履歴や文書群など、何度も処理されるテキストの KV キャッシュを推論エンジンの間で保存し、ディスクにも残す。
- prefill の計算を GPU から外し、最初のトークンまでの時間と推論の費用を減らす。vLLM や NVIDIA Dynamo と連携できる。

### 110. Mem0

- AI エージェントのためのメモリ層である。会話の履歴を丸ごと保存して再利用する素朴な方法はトークンを浪費する。
- 短期の記憶と、重要な事実と関係だけを取り出して保存する長期の層に分ける。ベクトルストアによる意味の類似と、知識グラフによる時間と関係の理解を組み合わせ、トークンを大きく減らしつつ長期の記憶を保つ。

### 111. Open Security Control Assessment Language (OSCAL)

- NIST が主導する、コンプライアンスとリスク管理の自動化を進めるための機械可読な情報交換の形式である。SOC 2、PCI、FedRAMP などのセキュリティ統制を XML、JSON、YAML で表す。
- 公共部門以外ではまだ広まっていないが、表計算やチェックの作業を減らし、継続的コンプライアンスに組み込めば自動化できる可能性がある。

### 112. OpenInference

- AI アプリを観測するための、OpenTelemetry を補う約束事とプラグインの集まりである。LLM の呼び出しと、ベクトル検索やツール呼び出しなどの周辺の文脈を追跡できる。
- スパンは OpenTelemetry 互換の収集器に送れる。Langfuse など他の基盤にもトレースを記録できる。

### 113. Valibot

- TypeScript のスキーマ検証ライブラリで、Zod や Ajv と同じく型推論を持つ。モジュール化した設計で、使う検証関数だけを取り込める。
- 最適な場合で Zod よりバンドルを最大 95% 小さくできる。クライアント側の検証やサーバーレスなど、バンドルの大きさが重要な場面に向く。

### 114. Vercel AI SDK

- TypeScript で AI アプリやエージェントを作るための、オープンソースのフルスタックの道具一式である。AI SDK Core はモデルに依存しない LLM 呼び出し (テキスト生成、構造化出力、ツール呼び出し) を標準化する。
- AI SDK UI は React、Vue、Next.js、Svelte でのストリーミングと状態管理を簡単にする。TypeScript と Next.js を使うチームに向く。

## See also

- [Thoughtworks Technology Radar Vol.33 の全体像と 4 つのテーマ](/references/ai/thoughtworks-technology-radar-vol-33/thoughtworks-radar-vol-33-overview.md)
- [Thoughtworks Technology Radar Vol.33: Platforms](/references/ai/thoughtworks-technology-radar-vol-33/thoughtworks-radar-vol-33-platforms.md)
- [Thoughtworks Technology Radar Vol.35: Languages and frameworks](/references/ai/thoughtworks-technology-radar-vol-35/thoughtworks-radar-vol-35-languages-and-frameworks.md)
