---
type: reference
title: 'Thoughtworks Technology Radar Vol.32: Languages and Frameworks'
description: 'Thoughtworks Technology Radar Vol.32 (2025 年 4 月) の Languages and Frameworks 象限 23 項目の要約で、OpenTelemetry と React Hook Form、TypeScript のライブラリ、LangGraph や CrewAI などのエージェントのフレームワーク、新しい言語とフレームワークをリングごとにまとめる。'
tags: [ai, thoughtworks, technology-radar, frameworks, typescript, agent, observability]
status: stable
verified: { by: claude-code/claude-opus-5-5, at: 2026-11-26T00:00:00Z }
stale_after: 2027-11-26T00:00:00Z
---

# Thoughtworks Technology Radar Vol.32: Languages and Frameworks

Thoughtworks Technology Radar Vol.32 (2025 年 4 月) の Languages and Frameworks (言語・フレームワーク) 象限の要約である。
TypeScript とフロントエンドのライブラリ、LLM エージェントを作るフレームワーク、新しい言語が並ぶ。

- 出典: Thoughtworks Technology Radar Volume 32 (PDF)、[thoughtworks.com/radar](https://www.thoughtworks.com/radar)

[TOC]

## Adopt

### 83. OpenTelemetry

- 可観測性の業界標準になりつつある。OTLP の仕様で、トレース、メトリクス、ログを同じ形式で運べる。Datadog、New Relic、Grafana が対応し、ベンダーに縛られない構成が作れる。gzip や zstd の圧縮で転送量も減らせる。

### 84. React Hook Form

- 非制御コンポーネントを既定にし、大きなフォームで特に性能が良い。Yup や Zod などのスキーマ検証と統合でき、shadcn や AntD とも組み合わせられる。フォームの多いアプリケーションに向く。

## Trial

### 85. Effect

- 非同期、並行処理、状態管理、エラー処理を、関数型の手法と TypeScript の型で扱うライブラリである。fp-ts より日常の作業に合った抽象を持ち、組み合わせやテストがしやすい。使ったチームは async/await に戻る理由が無いとした。

### 86. Hasura GraphQL engine

- PostgreSQL、MongoDB、ClickHouse などの上に、すぐ GraphQL の API を作るデータアクセス層である。データプロダクトの案件で使った。強力な連合クエリと統合スキーマ管理には慎重であり続ける。LLM でデータを扱う PromptQL が加わった。

### 87. LangGraph

- LLM で状態を持つマルチエージェントのアプリケーションを作るためのオーケストレーションの枠組みである。LangChain より低レベルなノードと辺の部品で、ワークフロー、メモリ、状態の保存を細かく制御できる。学習は難しいが軽くモジュール化されている。

### 88. MarkItDown

- PDF、HTML、PowerPoint、Word を Markdown に変換する。見出しなどの構造が残るので LLM が文脈をつかみやすい。RAG の前処理で、構造を意識した分割と組み合わせて使った。

### 89. Module Federation

- マイクロフロントエンドの間で共有モジュールを指定し、依存の重複をなくす。2.0 で webpack から独立し、Rspack や Vite にも対応した。

### 90. Prisma ORM

- Node.js と TypeScript のための型安全なデータベースツールキットで、スキーマの移行を自動化し、直感的なクエリ API を持つ。デコレーターやクラスを使わず、関数型の書き方とよくなじむ。

## Assess

### 91. .NET Aspire

- 複数の .NET プロジェクト、データベース、Docker コンテナを 1 つのコマンドで手元に起動する。ログ、トレース、メトリクスのダッシュボードも手元で使え、可観測性の開発がしやすい。

### 92. Android XR SDK

- Google が Samsung、Qualcomm と作った XR ヘッドセット向けの OS である Android XR の SDK である。既存のアプリを空間対応させたり、新しい空間アプリを作ったりする。開発者プレビュー段階である。

### 93. Browser Use

- LLM のエージェントに Web ブラウザーを操作させる Python ライブラリである。Playwright で操作し、画面の理解と HTML 構造の抽出を組み合わせる。複数のタブにまたがる操作もできる。

### 94. CrewAI

- それぞれ役割を持つ AI エージェントのチームを作り、協力して複雑な仕事をさせる基盤である。企業向け版もある。販促コードの検証や取引失敗の調査などの本番の課題に使った。

### 95. ElysiaJs

- 主に Bun 向けの、端から端まで型安全な TypeScript の Web フレームワークである。tRPC と違い API の形を強制しないので、REST や OpenAPI に沿いながら型安全を得られる。BFF に向く。

### 96. FastGraphRAG

- GraphRAG のオープンソース実装で、Personalized PageRank で関係の深いノードだけを辿り、精度と性能を上げる。グラフを可視化でき、増分更新にも対応する。

### 97. Gleam

- Erlang/OTP の BEAM の上で動く、型安全な関数型言語である。コンパイル時の型検査で実行時のエラーを減らし、Erlang や Elixir と相互運用できる。

### 98. GoFr

- Go でマイクロサービスを作るフレームワークで、ログ、トレース、メトリクス、設定、Swagger の文書、DB の移行、Kafka などとの pub/sub、cron の定型コードを肩代わりする。

### 99. Java post-quantum cryptography

- JDK 24 で、量子計算機に耐える鍵カプセル化 (JEP 496) と電子署名 (JEP 497) が Java にネイティブで入る。今の暗号データを集めて後で解読される危険があるので、数十年守る必要のある用途で検討する。

### 100. Presidio

- 構造化・非構造化テキストから個人情報を検出し、匿名化する SDK である。独自の検出規則も作れる。見逃しや誤検出があるので、結果を過信しない。

### 101. PydanticAI

- Pydantic の作者による、LLM アプリケーションとエージェントの軽量なフレームワークである。主要なモデルの API と統合し、構造化出力の扱いとグラフによるワークフローの抽象を持つ。

### 102. Swift for resource-constrained applications

- Swift 6.0 で Apple 以外の OS への対応が進み、資源の限られた用途にも使いやすくなった。型安全と参照カウントによるメモリ管理で、Rust より取り組みやすいと感じる開発者もいる。安全規格の認証はまだである。

### 103. Tamagui

- React の Web と React Native の間でスタイルを共有するライブラリである。最適化コンパイラーで、Web ではアトミックな CSS に、ネイティブでは事前に作ったスタイルオブジェクトに変換する。

### 104. torchtune

- LLM の作成、事後学習、実験のための PyTorch ライブラリである。微調整、推論、評価、量子化を意識した学習を YAML のレシピで行い、複雑なフラグを避ける。

## Hold

### 105. Node overload

- 他の選択肢を考えずに Node.js を使う傾向への警告を再び出した。Node.js は計算の重い処理に向かず、データの重い処理でも苦労するチームが出ている。多言語のプログラミングを勧め続ける。

## See also

- [Thoughtworks Technology Radar Vol.32 の全体像と 4 つのテーマ](/references/ai/thoughtworks-technology-radar-vol-32/thoughtworks-radar-vol-32-overview.md)
- [Thoughtworks Technology Radar Vol.32: Platforms](/references/ai/thoughtworks-technology-radar-vol-32/thoughtworks-radar-vol-32-platforms.md)
