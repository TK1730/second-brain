---
type: reference
title: 'Thoughtworks Technology Radar Vol.34: Languages and frameworks'
description: 'Thoughtworks Technology Radar Vol.34 (2026 年 4 月) の Languages and frameworks 象限 21 項目の要約で、データ基盤の標準、フロントエンドとモバイルの定番、エージェントのフレームワーク、LLM の評価と文書処理、仕様駆動開発の道具をリングごとにまとめる。'
tags: [ai, thoughtworks, technology-radar, frameworks, agent, frontend, data]
status: stable
verified: { by: claude-code/claude-opus-5-5, at: 2026-11-26T00:00:00Z }
stale_after: 2027-11-26T00:00:00Z
---

# Thoughtworks Technology Radar Vol.34: Languages and frameworks

Thoughtworks Technology Radar Vol.34 (2026 年 4 月) の Languages and frameworks (言語・フレームワーク) 象限の要約である。
Apache Iceberg や React、Svelte などの定番が Adopt に入り、エージェントを作るフレームワークや LLM の評価・文書処理のライブラリが続く。
今号のこの象限に Caution の項目は無い。

- 出典: Thoughtworks Technology Radar Volume 34 (PDF)、[thoughtworks.com/radar](https://www.thoughtworks.com/radar)

[TOC]

## Adopt

### 98. Apache Iceberg

- S3 などに置く大規模な分析用データの、ファイル、メタデータ、スキーマの構成を定めるオープンなテーブル形式である。AWS、Snowflake、Databricks、BigQuery など主要な基盤すべてが対応し、ロックインを避けられる。
- 機能と統治が 1 社に握られていない点が他の形式と違う。スナップショットによる直列化可能な分離、楽観的な同時書き込み、履歴と巻き戻しを持つ。現代のデータ基盤の既定の選択肢として勧める。

### 99. Declarative Automation Bundles

- 旧称 Databricks Asset Bundles で、Databricks のクラスター、ETL パイプライン、ジョブ、機械学習モデル、ダッシュボードの大半をコードとして管理できる。
- `databricks bundle plan` で変更を事前に確かめられ、Terraform のように繰り返せるデプロイができる。Databricks を多く使うチームに勧める。

### 100. React JS

- 2016 年から JavaScript の UI 開発の既定だが、React 19 の一部として React Compiler が安定版になったので見直した。メモ化をビルド時に行うので、`useMemo` や `useCallback` はほぼ不要になる。
- Actions や `useActionState`、`useOptimistic` で、外部ライブラリなしにフォームやデータ更新を扱いやすくなった。Linux Foundation の下に React Foundation ができ、長期の安定性も高まった。

### 101. React Native

- クロスプラットフォームのモバイル開発の既定として Adopt に移った。新しいアーキテクチャ (JSI と Fabric) で、ブリッジのボトルネックと起動速度の問題が解消された。
- 1 つのコードベースのまま、ネイティブに近い反応速度が出る。Expo を含む生態系も成熟した。

### 102. Svelte

- 大きな実行時ライブラリや仮想 DOM に頼らず、ビルド時に最適化された JavaScript へコンパイルする UI フレームワークである。SvelteKit で SSR やフルスタックにも強くなり、Adopt に移った。
- 小さなバンドル、速い実行、単純な部品の作り方が利点である。Svelte 5 の runes や snippets で、リアクティビティと UI の組み立てが明示的になった。React や Vue の代替として現実的な選択肢である。

### 103. Typer

- 型注釈付きの普通の関数から、ヘルプやシェル補完付きのコマンドラインツールを作る Python のライブラリである。小さなスクリプトから複数コマンドの CLI へ無理なく育てられる。
- 社内の道具や自動化、AI まわりの開発作業を CLI にする動きが増え、重要性が増した。Python 専用である。

## Trial

### 104. Agent Development Kit (ADK)

- Google による、オーケストレーション、ツール、評価、デプロイを扱う、AI エージェントを作り運用するためのフレームワークである。生態系と運用機能が成熟した。
- Microsoft Agent Framework、Amazon Bedrock AgentCore、OpenAI Agents SDK、Claude Agent SDK など競合が多い。移植性を重視するなら LangGraph や CrewAI もある。Google の基盤に投資しているプロジェクトで成功例が増えている。

### 105. DeepEval

- LLM の性能を評価する、Python のオープンソースのフレームワークである。RAG の評価や、モデルの基準作りと比較に使える。正確さ、関連性、一貫性を測り、作り話の検出や独自の指標の定義もできる。
- エージェントのワークフローや多ターンの会話にも対応し、ツールの正しさ、手順の効率、タスクの達成、MCP サーバーとのやり取りまで評価できる。会話を模擬してテストケースを作る機能もある。

### 106. Docling

- PDF や読み取り画像を含む非構造の文書を、JSON や Markdown などの機械が読みやすい形に変換する、Python と TypeScript のオープンソースのライブラリである。画像認識でレイアウトと意味を理解する。
- Azure Document Intelligence や Amazon Textract などの商用サービスの代わりに自前で運用できる。大きなファイルでも品質と費用の釣り合いがよく、Trial に移った。

### 107. LangExtract

- 利用者の指示に基づき、LLM で非構造のテキストから構造化された情報を取り出す Python のライブラリである。取り出した各項目を原文の位置に結び付けるので、出所をたどれる。
- 長い非構造の資料に向き、短く予測しやすい入力の出力形式を縛るなら Pydantic AI が向く。

### 108. LangGraph

- 複数エージェントのシステムを、共有の状態を持つグラフとして扱う LangGraph の設計は、いつも最適ではないと分かってきた。
- Pydantic AI のように、単純なエージェントがコード実行でやり取りし、必要になってからグラフを足す方法のほうが、軽く効果的なことが多い。そのため Adopt から外した。強力な道具だが、既定の選択肢ではない。

### 109. LiteLLM

- 複数の LLM 提供者を包む薄い層から、完全な AI ゲートウェイに育った。再試行と切り替え、提供者間の負荷分散、費用の追跡と予算管理、要求の追跡、アクセス制御、鍵の管理、内容の検査などを 1 か所で扱える。
- 提供者固有の機能を使うと、提供者に依存したパラメーターが必要になり、ゲートウェイで消したはずの結合が戻る。`drop_params` は対応しないパラメーターを黙って捨てる点にも注意する。

### 110. Modern.js

- ByteDance による React のメタフレームワークで、Module Federation によるマイクロフロントエンドが必要なチーム向けに Trial とした。Next.js 向けの nextjs-mf は終了に向かっている。
- Module Federation の中心チームが、主な対応フレームワークとして Modern.js を勧めている。ByteDance の外での生態系はまだ薄く、文書も少ない。

## Assess

### 111. Agent Lightning

- 既存のエージェントを、実装を変えずにプロンプトの自動最適化、教師ありの微調整、強化学習で継続的に改善するフレームワークである。AutoGen や CrewAI に対応する。
- 学習を管理する Lightning Server と、実行時に記録を集めて送る Lightning Client の間に層を置く仕組みである。

### 112. GitHub Spec Kit

- 仕様駆動開発のフレームワークである。プロジェクトの範囲、業務の文脈、技術のバージョン、コーディング規約、リポジトリの構造をまとめた「憲法」(constitution) で、エージェントを意図した設計の範囲に留める。
- 文脈を足し続けると指示が肥大化するので、再利用できる指示をスキルに切り出す。仕様 → 計画 → タスク → コーディング → レビューの流れで、既存システムの問題を早く見つけたチームがある。
- 余計な防御的チェックや冗長な Markdown が増える問題もあり、テンプレートの調整が要る。クリーンコードや設計に強い経験者ほど価値を引き出せる。

### 113. Mastra

- TypeScript ネイティブな、AI アプリケーションとエージェントを作るオープンソースのフレームワークである。グラフ型のワークフロー、多くの LLM 提供者への統一的な接続、人の承認での一時停止と再開、RAG とメモリ、MCP サーバーの作成、評価と可観測性を備える。
- Python に切り替えず、Node.js や Next.js の中で AI の層を作りたいチームに向く。

### 114. Pipecat

- 音声認識、LLM、音声合成、通信を組み合わせる部品式のパイプラインで、リアルタイムの音声・マルチモーダルのエージェントを作るオープンソースのフレームワークである。会話の振る舞いを素早く試せ、提供者も差し替えやすい。
- LiveKit Agents より柔軟だが、本番への道筋は統合されていない。重要な業務に使うには、基盤のエンジニアリングが多く要る。

### 115. Superpowers

- 組み合わせられるスキルで作った、AI 支援のコーディングのワークフローである。コーディング前のブレインストーミング、実装前の詳細な計画、赤・緑・リファクタリングを強制する TDD、原因から探るデバッグ、実装後のコードレビューへとエージェントを導く。
- Claude Code と Cursor のプラグインマーケットプレイスで配布されている。

### 116. TanStack Start

- TanStack Router をもとにした、React と Solid 向けのフルスタックフレームワークで、SSR やキャッシュなど Next.js と同じような機能を持つ。サーバー関数、ローダー、ルーティングまでコンパイル時の型の安全性がある。
- 規約より明示的な設定を好み、普通の React に近い感覚で使える。Next.js より挙動を予測しやすい。

### 117. TOON (Token-Oriented Object Notation)

- LLM に構造化データを渡すときのトークン数を減らすための、人が読める JSON の表現形式である。既存のシステムでは JSON のままにし、モデルに渡す直前だけ変換する。
- 繰り返されるキーなどの無駄を減らせ、大きく規則的なデータに効く。API やデータベース、モデルの出力の代わりにはならず、深い入れ子や平らな表 (CSV のほうが小さい) には向かない。自分のデータで JSON や CSV と比べる。

### 118. Unsloth

- LLM の微調整と強化学習を大幅に速く、少ないメモリで行うオープンソースのフレームワークである。行列計算を NVIDIA GPU 向けの効率のよい独自カーネルに置き換える。
- H100 のクラスターがなくても、T4 以上の一般向け GPU で微調整できる。LoRA、全体の微調整、複数 GPU、最大 50 万トークンの長い文脈に対応する。

## See also

- [Thoughtworks Technology Radar Vol.34 の全体像と 4 つのテーマ](/references/ai/thoughtworks-technology-radar-vol-34/thoughtworks-radar-vol-34-overview.md)
- [Thoughtworks Technology Radar Vol.34: Techniques](/references/ai/thoughtworks-technology-radar-vol-34/thoughtworks-radar-vol-34-techniques.md)
- [Thoughtworks Technology Radar Vol.35: Languages and frameworks](/references/ai/thoughtworks-technology-radar-vol-35/thoughtworks-radar-vol-35-languages-and-frameworks.md)
