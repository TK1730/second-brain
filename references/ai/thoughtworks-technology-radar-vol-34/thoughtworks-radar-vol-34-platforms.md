---
type: reference
title: 'Thoughtworks Technology Radar Vol.34: Platforms'
description: 'Thoughtworks Technology Radar Vol.34 (2026 年 4 月) の Platforms 象限 24 項目の要約で、エージェントの UI と実行基盤、LLM の可観測性、時間を扱う知識グラフ、OpenTelemetry ベースの可観測性、リモート開発環境、PyTorch の大規模学習基盤をリングごとにまとめる。'
tags: [ai, thoughtworks, technology-radar, platform, agent, observability, ai-infrastructure]
status: stable
verified: { by: claude-code/claude-opus-5-5, at: 2026-11-26T00:00:00Z }
stale_after: 2027-11-26T00:00:00Z
---

# Thoughtworks Technology Radar Vol.34: Platforms

Thoughtworks Technology Radar Vol.34 (2026 年 4 月) の Platforms (基盤) 象限の要約である。
エージェントを動かす基盤と UI のプロトコル、LLM とシステムの可観測性、データ基盤、大規模なモデル学習の基盤が並ぶ。
今号の Platforms に Adopt と Caution の項目は無い。

- 出典: Thoughtworks Technology Radar Volume 34 (PDF)、[thoughtworks.com/radar](https://www.thoughtworks.com/radar)

[TOC]

## Trial

### 42. AG-UI Protocol

- 豊かな UI とバックエンドの AI エージェントの間の通信を標準化するオープンなプロトコルとライブラリである。SSE や WebSocket で、推論の過程の配信、状態の同期、動的な UI の描画をイベント駆動で扱う。
- ただし、MCP サーバーやスキルの中に HTML や UI 部品を直接入れる方法 (MCP Apps、MCP-UI) が出てきて、別の UI プロトコル層の必要性が問われている。

### 43. Apache APISIX

- Nginx と LuaJIT (OpenResty) 上に作られた、高性能なオープンソースのクラウドネイティブゲートウェイである。設定を etcd に置き、再読み込みによる遅延がない。
- 交通制御、セキュリティ、可観測性を API とプラグイン (WASM を含む) で動的に変えられる。Kubernetes Gateway API に対応し、古い Nginx の Ingress コントローラーの置き換え候補になる。

### 44. Amazon Bedrock AgentCore

- インフラを管理せずにエージェントを大規模に作り、動かし、運用する AWS の基盤である。
- 丸ごと採用するより、セッションの分離、セキュリティ、可観測性などの本番の関心事は AgentCore の実行環境に任せ、オーケストレーションは LangGraph などの外部フレームワークに残す分離した構成のほうがうまくいった。

### 45. Graphiti

- Zep による、時間を扱うオープンソースの知識グラフエンジンで、LLM の記憶の問題に本番で使えることを示したため Trial に移った。
- データを出来事の単位で取り込み、グラフの辺に 2 種類の有効期間を持たせて、古い事実を上書きではなく無効にする。グラフを少しずつ更新し、意味検索、BM25、グラフ探索を組み合わせて、問い合わせ時に LLM を呼ばずに高速に取得する。
- MCP サーバーがあり、エージェントに時間を意識した記憶を簡単に付けられる。書き込みごとの LLM 抽出の費用と、1.0 前であることに注意する。

### 46. Langfuse

- 可観測性、プロンプト管理、評価、データセット管理を備えたオープンソースの LLM エンジニアリング基盤である。v3 で ClickHouse、Redis、S3 を使う構成になり、拡張しやすくなった代わりに自前運用は複雑になった。
- SDK は OpenTelemetry ベースになり、実験の実行やプロンプト実験の構造化出力にも対応して、追跡だけでなく体系的な評価に使える。
- 一覧では Trial に置かれているが、本文には「Assess に留める」とあり、PDF 内で表記が揃っていない。規模に見合うか、Helicone のような狭い道具で足りるかを見極める。

### 47. Port

- ソフトウェア資産を集約し、ワークフローを自動化し、技術標準を守らせる商用の社内開発者ポータルである。API と MCP の層を通じて IDE からも使える。
- 大きな基盤エンジニアリングの投資なしに、少人数の基盤チームで何千人もの開発者にセルフサービスを提供できた。ベンダー依存を受け入れられる組織向けである。

### 48. Replit

- ブラウザーの中で、すぐ使える開発環境、リアルタイムの共同編集、AI 支援、実行、デプロイを一体にしたクラウドの開発基盤である。
- 準備なしに始められ、チームでの試作、研修、ブートキャンプに向く。趣味の場と見られがちだが、手元の IDE と競える力がある。

### 49. SigNoz

- ログ、メトリクス、トレースを一体で扱う、OpenTelemetry ネイティブのオープンソースの可観測性基盤である。ClickHouse を保存先に使い、速く安く大量のデータを扱える。
- Datadog などの代わりに自前で運用でき、資源の消費と費用を下げられた。Docker イメージや Helm チャートで導入しやすい。

## Assess

### 50. Agent Trace

- Cursor が提案した、AI によるコードの帰属を標準化するオープンな仕様である。git blame では、変更が人か AI か両方かが分からない。
- 人、AI、混在、不明などの種類と、各変更の出所の記録を定める。保存方法は決めず、Git、Mercurial、Jujutsu に対応する。Cline、OpenCode、Git AI が対応し始めている。

### 51. ClickStack

- ログ、トレース、メトリクス、セッションを ClickHouse 上の 1 つの高速な保存先にまとめる、OpenTelemetry 互換のオープンソースの可観測性基盤である。断片化した道具と高い商用基盤に代わる、単純で安い土台になる。

### 52. Coder

- コードを動かす場所と、開発者が操作する方法を分ける。画面を転送せず、手元の VS Code やブラウザーからリモート環境につなぐので、反応がよい。
- 環境をコードで定義して標準化でき、オンボーディング、社内システムへのアクセス管理、承認済みの AI エージェントの提供がしやすい。ローカル開発と画面転送の VDI の中間にあたる。

### 53. Databricks Agent Bricks

- 知識アシスタントやデータ分析のような一般的な AI の型を、目的とデータを宣言するだけで作れる、自動で最適化される部品群である。データ基盤がエージェントをネイティブに支える方向の例である。
- Databricks にすでに投資していて、チャットボットや文書抽出などを試すなら検討する。

### 54. DuckLake

- カタログとメタデータを SQLite、PostgreSQL、DuckDB などの普通の SQL データベースに置き、データは Parquet ファイルとして保存する、データレイクとカタログの形式である。
- Iceberg や Delta Lake のファイルベースの複雑なメタデータより、計画の遅延と同時更新の信頼性がよい。DuckDB で問い合わせ、タイムトラベルや ACID にも対応する。Spark や Trino の運用負担を避けたい場合の軽い選択肢である。

### 55. FalkorDB

- Redis をもとにした、Cypher に対応するグラフデータベースである。重いグラフ基盤を入れずにグラフの機能が欲しいチームに向く。拡張性、運用の道具、生態系の成熟度は確かめる必要がある。

### 56. Google Dialogflow CX

- Flows と Pages による状態機械と、Vertex AI Gemini による生成機能を組み合わせた、Google Cloud のマネージドな会話 AI 基盤である。Generative Playbooks や Data Store RAG がある。
- 自然言語から SQL への変換をするデータ探索エージェントを、自前の SDK より速く作れた。無料枠がなく、Google Cloud への強い依存がある。

### 57. MCP Apps

- MCP サーバーが、ダッシュボード、フォーム、可視化などの対話型の HTML を返し、会話の中に表示できるようにする、MCP の最初の公式拡張である。Anthropic や OpenAI などが共同で作った。
- `ui://` で UI のテンプレートを宣言し、サンドボックスの iframe で描画する。対応しない環境では文字にフォールバックする。Claude、ChatGPT、VS Code、Goose が対応している。

### 58. Monarch

- 1 台での PyTorch の書き方のまま、大規模な GPU クラスターで動かせる分散プログラミングのフレームワークである。リモートのプロセスやアクターを束ねて扱い、監督の木による耐障害性や RDMA による転送を持つ。
- 分散したテンソルを手元のテンソルのように扱える抽象が、大規模学習の複雑さを大きく下げる。まだ初期段階である。

### 59. Neutree

- 自前の基盤で LLM を管理・提供するオープンソースの基盤で、NVIDIA、AMD、Intel などの混在したハードウェアをまたいで、モデルのライフサイクル、推論、計算資源の割り当てを 1 つの制御面で扱う。
- 複数テナント、アクセス制御、利用量の集計を備える。まだ新しく、慎重に試す必要がある。

### 60. OptScale

- AI・機械学習で急に膨らむ GPU などの費用に対応した、オープンソースのマルチクラウドの FinOps 基盤である。費用の可視化、最適化の提案、予算管理、異常検知を持つ。
- OpenCost より広い範囲を扱い、商用製品よりベンダー依存が少ない。運用の負担は大きく、そのまま使える製品ではなく基盤への投資として扱う。

### 61. Rhesis

- 期待する振る舞いを自然言語で定め、敵対的なテストを生成し、結果を評価する、LLM とエージェント向けのオープンソースのテスト基盤である。会話のシミュレーター、OpenTelemetry による追跡、Docker での自前運用がある。
- 製品、業務、エンジニアリングのチームが同じテストの流れに参加できる。評価の費用、LLM-as-judge の限界、要件を事前に定める必要があることに注意する。

### 62. Runpod

- 世界に分散した GPU の市場として、H100 のクラスターから RTX 4090 まで、大手クラウドより安く使える計算資源を提供する。長期契約やロックインなしに学習や推論を試したいチーム向けである。

### 63. Sprites

- Fly.io による、AI コーディングエージェントを隔離して動かすための、状態を持つサンドボックスである。使い捨てではなく永続する Linux 環境で、何度でもチェックポイントを取り、復元できる。
- 依存関係や実行時の設定まで含めた環境全体を戻せるので、Git だけでは戻せないものも回復できる。使い捨ての Dev Containers と比べて選ぶ。

### 64. torchforge

- 言語モデルの大規模な事後学習のための、PyTorch ネイティブな強化学習ライブラリである。Monarch、vLLM、torchtitan を束ね、アルゴリズムの記述と分散実行を分ける。成熟度は確かめる必要がある。

### 65. torchtitan

- 生成 AI モデルの大規模な事前学習のための、PyTorch ネイティブな基盤で、データ、テンソル、パイプライン、コンテキストの 4 次元の並列化を備えた参照実装である。自前の事前学習基盤を作るチーム向けである。

## See also

- [Thoughtworks Technology Radar Vol.34 の全体像と 4 つのテーマ](/references/ai/thoughtworks-technology-radar-vol-34/thoughtworks-radar-vol-34-overview.md)
- [Thoughtworks Technology Radar Vol.34: Techniques](/references/ai/thoughtworks-technology-radar-vol-34/thoughtworks-radar-vol-34-techniques.md)
- [Thoughtworks Technology Radar Vol.35: Platforms](/references/ai/thoughtworks-technology-radar-vol-35/thoughtworks-radar-vol-35-platforms.md)
