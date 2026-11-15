---
type: reference
title: 'Tencent WeKnora: ハイブリッド RAG・ReAct エージェント・自動 Wiki を統合したナレッジ基盤'
description: Tencent のオープンソースナレッジ基盤「WeKnora」の要約で、ハイブリッド検索・自律エージェント・自動 Wiki 構築の 3 機能とローカル完結・通信制御の構成をまとめる。
tags: [ai, agent, rag, knowledge-graph, mcp, local-first, self-hosted]
status: stable
verified: { by: antigravity/gemini-4-argon, at: 2026-11-15T00:00:00Z }
stale_after: 2027-11-15T00:00:00Z
---

# Tencent WeKnora: ハイブリッド RAG・ReAct エージェント・自動 Wiki を統合したナレッジ基盤

Tencent が公開しているオープンソースのエンタープライズ向け LLM ナレッジ基盤「WeKnora」 (`Tencent/WeKnora`) の概要と、ローカル運用・外部通信の制御方法をまとめる。

## 概要

WeKnora は、PDF、Word、Excel、画像などの非構造化ドキュメントを取り込み、ハイブリッド RAG による Q&A、自律的な ReAct エージェント、自己更新型の構造化 Wiki / ナレッジグラフへと変換するセルフホスト可能なプラットフォームである。
バックエンドは Go (`app`)、ドキュメント解析は Python (`docreader`、gRPC 通信)、フロントエンドは Vue で構成され、Docker Compose または Kubernetes Helm チャートでオンプレミス・ローカル環境へデプロイできる。

## 3 つの主要機能モード

### 1. RAG ベースのクイック Q&A (ハイブリッド検索エンジン)

単一のベクトル検索に頼るのではなく、複数の検索戦略を組み合わせて検索漏れや文脈欠落を防ぐ。

- **ハイブリッド検索**: キーワード一致に強い BM25 (スパース検索)、意味的類似性を捉えるベクトル検索 (デンス検索)、エンティティ間の関係性を辿る GraphRAG (ナレッジグラフ検索) を統合する。
- **親子チャンキング (Parent-Child Chunking)**: 検索時は細かいチャンクで高精度にヒットさせ、LLM には親チャンクの広い文脈を渡すことで文脈の断絶を防ぐ。
- **インライン引用と `@mention`**: 回答の根拠となったドキュメントの該当チャンクをインラインで引用表示し、チャット内で `@` を使って特定のナレッジベースやファイルを直接指定できる。

### 2. 自律型 ReAct エージェントとツール連携

1 回の検索では解決できない複合的な問いに対して、計画・検索・ツール実行を繰り返す ReAct (Reasoning and Acting) エージェントが動作する。

- **MCP (Model Context Protocol) 統合**: 外部の MCP サーバーをエージェントのツールとして利用できるほか、WeKnora 自身が MCP サーバーを内蔵しており、Claude Code や Cursor などの外部 AI エージェントから WeKnora のナレッジベースを直接検索・参照できる。
- **隔離サンドボックスとデータ分析**: Docker や E2B などのサンドボックス内で Python スクリプトを安全に実行し、CSV や Excel シートを解釈するビルトインのデータアナリストエージェントを備える。
- **Human-in-the-Loop 操作**: DeepSeek R1 や QwQ などの思考過程 (Thinking) を可視化し、実行中のエージェントの一時停止・軌道修正・フォーク・巻き戻しを行える。

### 3. Auto-Wiki モードとナレッジグラフ

取り込んだ生ドキュメント群から、バックグラウンドのエージェントが人物・プロダクト・概念などのエンティティと関係性を自動抽出する。

- **自動 Wiki 生成**: 相互リンクされた Markdown の Wiki ページ群と、ページ間の関係を示すインタラクティブなナレッジグラフを自動構築する。
- **リビジョン管理**: ブラウザ上で Markdown を直接編集でき、変更差分の履歴管理とワンクリックでのロールバックに対応する。

## マイクロサービス構成とローカル・外部通信の制御

WeKnora の標準スタックは、すべてローカルの Docker ネットワーク内で自己完結するように設計されている。

- **`app` (Go)**: コアロジック、REST API、MCP サーバー、エージェントオーケストレーションを担う。
- **`docreader` (Python / gRPC)**: PDF・Office 文書・画像のレイアウト解析と OCR をローカルコンテナ内で処理する。
- **`postgres` (ParadeDB / PostgreSQL)**: 全文検索 (BM25)、リレーショナルデータ、ベクトル検索 (`pgvector` + HNSW) を 1 つの DB で完結させる (オプションで Qdrant、Milvus、Neo4j なども選択可能)。
- **`redis` (Asynq)**: 非同期ジョブキューとワーカープールの制御を担う。

### 外部通信を AI エージェント関連のみに閉じる構成

ドキュメントの保管・解析・インデックス作成をすべてローカルに閉じ、外部との通信範囲を以下の 3 段階で厳密に制御できる。

1. **完全オフライン・ローカル AI エージェント連携 (外部通信ゼロ)**
   - LLM と Embedding モデルの両方をローカルの Ollama (`OLLAMA_BASE_URL=http://host.docker.internal:11434/v1`、例: `qwen2.5` + `bge-m3`) に設定し、Web 検索ツールと外部トレース (`LANGFUSE_ENABLED=false`) を無効化する。
   - インターネット通信を一切行わずに全機能がローカルで完結し、同じマシン上の Claude Code や Cursor などの AI エージェントから `localhost` の MCP / API 経由でナレッジを参照させる構成も可能である。
2. **インデックス作成はローカル完結・推論のみ外部 LLM API を呼ぶ構成**
   - 文書解析 (`docreader`) と Embedding 生成をローカルの Ollama (`bge-m3` 等) で処理し、DB 保存までを完全にオフラインで行う。
   - 外部通信は、エージェントが回答を生成する際にヒットした数チャンクを外部の商用 LLM API (Claude や OpenAI 等) へ送信する通信だけに限定できるため、社内文書全体を外部へ送信せずに済む。
3. **Docker ネットワークによる通信制御**
   - `postgres`、`redis`、`docreader` などのバックエンドコンテナを `internal: true` の Docker ネットワークに配置し、外部通信可能なコンテナを LLM API や MCP を呼び出す `app` コンテナのみに物理的に絞ることができる。

## See also

- [Tencent/WeKnora GitHub リポジトリ](https://github.com/Tencent/WeKnora)
- [国内企業の AI × ナレッジグラフ活用事例: 因果推論と実装パターン](/references/ai/zenn-kg-japan-case-studies.md)
- [常時稼働エージェントの作り方: 5 つの基本部品](/references/ai/claude-resources-building-always-on-agents.md)
