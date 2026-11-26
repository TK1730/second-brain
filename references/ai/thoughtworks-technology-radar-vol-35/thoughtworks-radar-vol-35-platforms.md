---
type: reference
title: 'Thoughtworks Technology Radar Vol.35: Platforms'
description: 'Thoughtworks Technology Radar Vol.35 (2026 年 11 月) の Platforms 象限 22 項目の要約で、可観測性基盤、永続実行基盤、Kubernetes 上の推論基盤、AI ゲートウェイ、エージェント実行基盤とプロトコルをリングごとにまとめる。'
tags: [ai, thoughtworks, technology-radar, platform, kubernetes, ai-infrastructure, observability, agent]
status: stable
verified: { by: claude-code/claude-opus-5-5, at: 2026-11-26T00:00:00Z }
stale_after: 2027-11-26T00:00:00Z
---

# Thoughtworks Technology Radar Vol.35: Platforms

Thoughtworks Technology Radar Vol.35 (2026 年 11 月) の Platforms (基盤) 象限の要約である。
大量のデータを扱う可観測性や永続実行の基盤に加え、AI ファクトリーを支える推論・ストレージ・ネットワークの基盤と、エージェントを動かす基盤が並ぶ。
今号の Platforms に Caution の項目は無い。

- 出典: Thoughtworks Technology Radar Volume 35 (PDF)、[thoughtworks.com/radar](https://www.thoughtworks.com/radar)

[TOC]

## Adopt

### 46. VictoriaMetrics

- 高性能なオープンソースの時系列データベースで、Prometheus では厳しい大量・高カーディナリティのメトリクスを扱える。毎秒 500 万サンプルを処理した事例がある。
- 単一ノード版と、取り込み・検索・保存を個別に拡張できるクラスター版がある。OpenTelemetry、Prometheus の API、remote write に対応し、既存の計装やダッシュボードを変えずに導入できる。

## Trial

### 47. Kafka share groups

- Kafka v4.2 で本番利用可能になった、キューのような消費モデルである (KIP-932)。従来はコンシューマー数がパーティション数を超えられなかったが、その制約が無くなる。
- レコードごとにロックを取って確認応答し、失敗やタイムアウトで再配送する (少なくとも 1 回の配送で、重複はありうる)。パーティション内の順序は保証しない。デッドレターキューはまだ無い。
- Kafka と別のキューを併用していた構成を Kafka に寄せられる。

### 48. KServe

- 予測 AI と生成 AI の推論を Kubernetes のカスタムリソースで管理するオペレーターである。自身は推論エンジンではなく、vLLM、SGLang、NVIDIA Triton などを束ねる。
- InferenceService (従来の機械学習と簡単な LLM 向け) と LLMInferenceService (高度な LLM 提供向け。複数ノード推論、prefill と decode の分離、KV キャッシュを意識したルーティング) がある。
- CNCF のインキュベーション段階で、Kubernetes 上に自前の推論基盤を作るときに Thoughtworks が好んで使う。

### 49. LibreChat

- 複数の提供者のモデルを 1 つの画面から使える、自前で運用する AI チャット基盤である。SSO、ロールによる権限、アップロード文書への RAG を持つ。
- 管理者が使える MCP サーバーを決め、権限のある利用者はコードを書かずにエージェントを作って共有できる。エンジニア以外に、確認済みの AI 道具を統制された形で渡す手段であり、AI-accelerated shadow IT への答えになる。

### 50. LiteLLM

- 100 を超える LLM 提供者に対応するオープンソースの AI ゲートウェイで、ルーティング、形式の変換、認証、予算、ガードレールを持つ。ライブラリではなくインフラとして見るようになり、Platforms に移った。
- 今年だけで 25 件を超える CVE が出ており、セキュリティの懸念から Adopt ではなく Trial とした。MCP やエージェント間の通信も統制するなら agentgateway と組み合わせる。

### 51. Microsoft Copilot Retrieval API

- SharePoint、OneDrive、Copilot コネクターの内容から、RAG 用の関連テキストを取り出す API である。呼び出した利用者の権限でアクセス制御が効く。
- 分割、索引付け、同期などを Microsoft に任せられ、Microsoft の道具に知識がある組織のエージェントに向く。

### 52. Restate

- 実行の全段階を記録し、失敗したサービスが途中から再開できる永続実行基盤である。サービス間の通信は厳密に 1 回を保証する。
- 人の承認を待つ長い処理や、レガシーシステムへの再試行が多い処理に向く。SDK は MIT ライセンスだが、サーバーは Business Source License で、第三者向けのマネージドサービスとしては提供できない。

### 53. Talos Linux

- Kubernetes を動かすための最小限で不変の Linux である。SSH もパッケージマネージャーも対話シェルも無く、mTLS の gRPC API で宣言的に設定し、更新は OS イメージごと置き換える。
- 攻撃面と設定の揺れを減らし、ノードを交換可能な部品にする。自分でノードを運用するチーム向けである。

### 54. Temporal

- 再試行、途中状態の保存、タイムアウト、人の承認の区切り、再開、進捗の可視化を備えた永続実行基盤である。
- 社内開発者基盤や AI クラウドの制御面など、長時間かかるインフラ構築の処理で有効だった。Restate と同じ役割を担う。

### 55. vCluster

- 仮想化した Kubernetes の制御面を提供し、テナントごとに API サーバー、RBAC、CRD を持たせる。名前空間による分離と、クラスターを丸ごと分ける方法の中間にあたる。
- 顧客ごとに GPU オペレーターや推論フレームワークが違う AI 基盤で特に有効である。

### 56. VictoriaLogs

- VictoriaMetrics の作者によるログ管理基盤で、事前の索引を作らずに大量のログを取り込み、圧縮して保存し、速く検索する。
- Elasticsearch より運用が軽く、Grafana Loki よりラベル設計の手間が少ない。OpenTelemetry、Elasticsearch、Loki の取り込み形式に対応する。

## Assess

### 57. Agent Client Protocol (ACP)

- AI エージェントと、それを使う環境 (IDE、ターミナル、CI/CD) の間の標準の境界である。Language Server Protocol のように JSON-RPC でセッション、ストリーミング、権限要求、取り消しを定める。
- MCP がエージェントとツールの間をつなぐのに対し、ACP はクライアントとエージェントの間をつなぐ。ハーネス全体を差し替え可能な部品にする。

### 58. Agent Plugins

- 再利用できるエージェントの部品 (スキルや MCP サーバー) を持ち運べるプラグインにまとめるオープン標準である。Amazon、Microsoft、OpenAI などが共同で始めた。
- 仕様は最小限だが、既存のスキル集を少し拡張するだけで Agent Plugin としても使える。

### 59. agentgateway

- Linux Foundation がホストする、LLM の推論、MCP、A2A の通信をまとめて扱うゲートウェイである。費用や遅延によるルーティング、フォールバック、支出上限、ガードレール、MCP ツールの制御を持つ。
- Kubernetes 版は、必要なコンテキストをすでにキャッシュしている GPU のレプリカや、実際に空いているサーバーへ振り分けられる。

### 60. AWS DevOps Agent

- 警報や課題をきっかけに、資源の関係を調べ、テレメトリとデプロイ履歴を突き合わせて根本原因と対策を示すマネージドなエージェントである。
- 調査の秒数で課金されるため費用が読みにくい。すべての結論を人が確かめ、きっかけとなるイベントを絞り、費用を追跡しながら評価する。

### 61. Claude Managed Agents

- Anthropic が提供する、汎用エージェントを動かすホスト型サービスである。チームはモデル、プロンプト、ツール、MCP サーバー、スキルを決め、ループ、サンドボックス、スケジュール、可観測性は Anthropic が受け持つ。
- 認証情報の保管庫が、エージェントに見せずに外向きの通信へ認証情報を差し込む。定義はファイルで持ち CI で適用できる。
- Anthropic のハーネスと Claude モデルだけに対応する。セッションを保存するので Zero Data Retention の対象外である。ベータ版で経験が 1 チームに限られるため Assess とした。

### 62. Decision models

- 文章ではなく、決められた構造の値を出す新しい種類のモデルである (Jev、Laya、Nimble、Kev など)。人の好みではなく、確率が実際の頻度に合うように学習する。
- 質問は Noul (はい・いいえの確率)、Choice (選択肢)、Score (段階や数値) の 3 種類に対応させる。
- 用途は LLM-as-a-judge の代替、モデルやツールのルーティング、ポリシーのゲート、大量のラベル付けなどである。分類用途で LLM を置き換えられるかを評価基準を決めて確かめる。

### 63. KAITO

- 自分の Kubernetes クラスターでオープンウェイトモデルを動かすための準備を自動化するオペレーターである。モデルと GPU の種類を宣言すると、GPU ノードの用意、メモリ見積もり、vLLM での提供まで行う。
- 対象はノードの用意とモデルの配置に絞られ、推論基盤全体では KServe のほうが成熟している。

### 64. llm-d

- vLLM や SGLang などのモデルサーバーを複数の Kubernetes ノードにまたがって動かす分散推論の仕組みである。
- LLM の推論は KV キャッシュがあるため状態を持つ。キャッシュの一致、待ち行列の深さ、予測遅延をもとに振り分け、prefill と decode を別の GPU に分けて使用率を上げる。

### 65. Netris

- 物理データセンターと AI インフラのためのネットワーク自動化・マルチテナント基盤である。スイッチの設定をクラウド風の VPC や ACL に抽象化し、宣言的に管理する。
- 制御器が止まっても通信は続く。AI の高帯域ワークロード向けの機能 (EVPN、RoCE の制御、DPU によるテナント分離) を持つ。

### 66. Omnigent

- Databricks が公開した、Claude Code、OpenAI Codex、Pi などのコーディングエージェントの上に乗るメタハーネスである。
- 支出上限や危険な操作の承認などのポリシー、OS のサンドボックス、認証情報の差し込み、セッションの再開を共通の層として提供する。共有サーバーにすると SSO やポリシーの一括管理ができる。
- コーディングエージェントの上にどんな抽象を置くのが正しいかはまだ分からず、本体もアルファ版である。

### 67. VAST DataStore

- ファイル、オブジェクト、ブロックを 1 つの名前空間で扱えるストレージで、計算ノードと NVMe ストレージを分けて個別に拡張できる。
- 学習、チェックポイント、モデルの読み込みで GPU がストレージ待ちになる問題に効く。ただし高価で VAST の基盤に縛られるので、大規模な学習や推論をしないなら過剰である。

## See also

- [Thoughtworks Technology Radar Vol.35 の全体像と 4 つのテーマ](/references/ai/thoughtworks-technology-radar-vol-35/thoughtworks-radar-vol-35-overview.md)
- [Thoughtworks Technology Radar Vol.35: Techniques](/references/ai/thoughtworks-technology-radar-vol-35/thoughtworks-radar-vol-35-techniques.md)
- [Claude Managed Agents の概要](/references/ai/claude-docs-managed-agents-overview.md)
