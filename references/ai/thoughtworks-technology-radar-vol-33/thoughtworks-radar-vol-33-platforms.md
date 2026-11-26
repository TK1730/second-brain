---
type: reference
title: 'Thoughtworks Technology Radar Vol.33: Platforms'
description: 'Thoughtworks Technology Radar Vol.33 (2025 年 11 月) の Platforms 象限 25 項目の要約で、クラウドの Arm、データレイクとデータ共有、LLM の可観測性、MCP と A2A・AG-UI のプロトコル、Kubernetes 上の運用基盤をリングごとにまとめる。'
tags: [ai, thoughtworks, technology-radar, platform, mcp, kubernetes, data-platform]
status: stable
verified: { by: claude-code/claude-opus-5-5, at: 2026-11-26T00:00:00Z }
stale_after: 2027-11-26T00:00:00Z
---

# Thoughtworks Technology Radar Vol.33: Platforms

Thoughtworks Technology Radar Vol.33 (2025 年 11 月) の Platforms (基盤) 象限の要約である。
エージェントのためのプロトコル (MCP、A2A、AG-UI) と LLM の可観測性に加え、データ基盤や Kubernetes 上の運用基盤が並ぶ。
今号の Platforms に Hold の項目は無い。

- 出典: Thoughtworks Technology Radar Volume 33 (PDF)、[thoughtworks.com/radar](https://www.thoughtworks.com/radar)

[TOC]

## Adopt

### 32. Arm in the cloud

- クラウドの Arm のインスタンスは、x86 より費用とエネルギーの効率が良い。AWS、Azure、GCP のすべてが提供している。
- マイクロサービス、オープンソースのデータベース、HPC まで、わずかなコードとビルドスクリプトの変更で移行できた。特定のアーキテクチャへの依存が無ければ、ほとんどのワークロードで Arm を勧める。マルチアーキテクチャの Docker イメージで両方への配置も容易である。

## Trial

### 33. Apache Paimon

- レイクハウスのためのオープンソースのデータレイク形式である。Flink や Spark と連携し、ストリーミングとバッチの両方を扱う。
- データレイク形式に LSM ツリーを組み合わせ、データレイクの弱点だった高速な更新と低遅延の読み取りを両立させる。主キー付きテーブル、重複除去や部分更新のためのマージエンジン、ACID トランザクション、タイムトラベル、スキーマの変更に対応する。

### 34. DataDog LLM Observability

- LLM とエージェントのワークフローを端から端まで追跡・監視する機能である。プロンプト、ツール呼び出し、途中の段階をスパンとトレースにし、遅延、トークン量、エラー、品質を追う。
- すでに Datadog を使い費用の構造に慣れている組織には手軽な選択肢である。計装の設定には、ワークロードと実装への理解が要る。

### 35. Delta Sharing

- Databricks と Linux Foundation によるデータ共有のオープン標準とプロトコルである。クラウドや自社環境をまたいで、データを複製せずに最新のまま共有できる。
- 短時間だけ有効な署名付き URL を発行する REST API を使い、受け手は pandas、Spark、Power BI で大きなデータを取得できる。クラウドのデータ転送料金が大きなリスクになりうる点に注意する。

### 36. Dovetail

- 散らばりがちな定性調査のデータ (インタビュー、書き起こし、気づき) を 1 か所に集め、分析できる資産に変える基盤である。
- 顧客の発言とまとめたテーマを、プロダクトの仮説や見込みの ROI に直接結びつけられ、プロダクトの意思決定での定性データの役割を強める。

### 37. Langdock

- 組織内の業務のための生成 AI のエージェントとワークフローを作って動かす基盤である。社内チャット、複数の LLM への API 層、Slack や Confluence などと連携するワークフローの構築を備える。
- オンプレミスや EU 内のホスティングでデータ主権を重視している。それでもデータの統制には注意し、toxic flow analysis で lethal trifecta を避ける。

### 38. LangSmith

- LangChain のチームによる、LLM アプリの可観測性、トレース、評価のためのホスト型基盤である。チェーン、ツール、プロンプトの詳細なトレースを取り、性能の後退を追える。
- 独自の SaaS で LangChain 以外への対応は限られるので、LangChain を使うチームに向く。プロンプトの評価と実験の機能は Langfuse などのオープンソースより洗練されている。

### 39. Model Context Protocol (MCP)

- LLM アプリやエージェントが外部のデータやツールとつながる方法を定めるオープン標準である。エージェント同士の通信を扱う A2A とは役割が違う。
- 前回から採用が急増し、JetBrains や Apple も加わった。公開・非公開のツールを探せる MCP Registry の標準も出てきた。
- 進化が速いぶん、確立した RPC の作法を見落としているという批判もある。本番では MCP-Scan で toxic flow を抑え、認可のモジュールの動向を注視する。

### 40. n8n

- Zapier や Make に似たワークフロー自動化の基盤で、自前で運用でき、拡張やコードでの制御を重視する開発者向けである。JavaScript や Python のコードも書ける。
- LLM と、設定可能なデータ源、メモリ、ツールをつなげられる。チャットや Webhook をきっかけにするエージェントのワークフローを素早く試作するのに使われている。ローコード基盤を本番で使うときは注意が要る。

### 41. OpenThread

- Google が開発した Thread ネットワークプロトコルのオープンソース実装である。IPv6、6LoWPAN などの層と、機器がノードにも境界ルーターにもなれるメッシュネットワークを備える。
- 多くのハードウェアで動き、商用製品で広く使われている。電池で動く低消費電力の機器から大規模なセンサーのメッシュまで、IoT で信頼できる。

## Assess

### 42. AG-UI Protocol

- リッチな UI とエージェントの間の通信を標準化するオープンなプロトコルとライブラリである。利用者と直接やり取りするエージェントに焦点を当てる。
- バックエンドのエージェントとフロントエンドが、状態を持ったリアルタイムの協働をするための一貫した方法を定める。SSE や WebSocket に対応し、LangGraph や Pydantic AI が組み込みで対応している。

### 43. Agent-to-Agent (A2A) Protocol

- 複雑なマルチエージェントのワークフローで、エージェント同士が通信するための標準である。Agent Card で、スキルの発見、通信方式、セキュリティの方式を記述する。
- エージェントの内部 (状態やメモリ) を見せずに通信する点で MCP を補う。長時間のタスクのための非同期を前提とした設計、ストリーミング、HTTPS と認証・認可を推奨する。Python、JavaScript、Java、C# の SDK がある。

### 44. Amazon S3 Vectors

- S3 にベクトルの保存と類似検索の機能を加えたものである。Amazon Bedrock や OpenSearch と連携し、メタデータでの絞り込みや IAM による統制もできる。
- まだプレビューで制限もあるが、データ量が多く、低遅延が最優先でない用途では、費用の安いベクトルの保存先になりうる。

### 45. Ardoq

- エンタープライズアーキテクチャ (EA) の基盤で、既存のシステムから情報を集め、状況の変化に合わせて更新される知識グラフを作る。古くなりやすい静的な文書の代わりになる。
- Ardoq Scenarios では、Git のような分岐とマージで「もしも」の将来の状態を視覚的に作れる。

### 46. CloudNativePG

- Kubernetes 上で高可用な PostgreSQL のクラスターを動かすためのオペレーターである。クラスター全体を宣言的な 1 つの資源として扱う。
- ストリーミングレプリケーションによるプライマリとスタンバイの構成、自己修復、自動フェイルオーバー、壊れたレプリカの自動再作成を備える。Kubernetes で PostgreSQL を動かすなら良い出発点である。

### 47. Coder

- 標準化した開発環境を素早く用意する基盤で、クラウドの開発環境という実践に沿ったものである。Gitpod (現 Ona) や GitHub Codespaces より、Terraform で環境を細かく調整できる。
- 自社の基盤 (クラウドかデータセンター) で動かすので、AI コーディングエージェントを走らせたり社内システムにつないだりしやすい。代わりに、テンプレートの保守とエージェントのワークフローのデータセキュリティの責任が増える。

### 48. Graft

- エッジや分散環境の間で、強い一貫性を保ちつつ効率よくデータを同期するトランザクショナルなストレージエンジンである。必要なときだけ同期し (遅延レプリケーション)、一部だけを複製して帯域を節約する。
- オブジェクトストレージを、データ形式を押しつけずにページ単位で一貫した更新ができるトランザクショナルなシステムに変える点が独特である。ローカルファーストのモバイルアプリなどに向く。

### 49. groundcover

- ログ、トレース、メトリクス、Kubernetes のイベントを 1 か所にまとめるクラウドネイティブの可観測性基盤である。eBPF を使い、アプリのコードに手を入れずにデータを集める。
- データを自社のクラウドに置く構成 (BYOC) と、データ量に左右されない料金体系を持つ。

### 50. Karmada

- 複数の Kubernetes クラスター、クラウド、データセンターにまたがってワークロードを配置する基盤である。Kubernetes ネイティブの API を使い、既存のアプリを変えずに使える。
- 比較的新しいので、頼る機能の成熟度を確かめる。ネットワーク、状態、ストレージのクラスター間管理は対象外で、Istio や Linkerd などのサービスメッシュは引き続き必要である。

### 51. OpenFeature

- フィーチャーフラグの定義と利用を標準化する、ベンダー中立の API 仕様である。アプリのコードとフラグの管理製品を切り離し、環境変数から ConfigCat や LaunchDarkly まで提供者を切り替えられる。
- フラグの種類ごとに規律をもって管理しないと、フラグの乱立、アプリの複雑化、テストの負担の増加を招く。

### 52. Oxide

- 計算、ネットワーク、ストレージと統合されたシステムソフトウェアを備えたラックを提供する。自社のインフラを一から組み立てる代わりになり、Terraform などから IaaS の API で扱える。
- 部品を寄せ集めるのではなく、基板や電源からファームウェアまで全体を設計している。Rust 製の組み込み向けカーネル Hubris などもオープンソースにしており、ライセンス料が無い点も評価している。

### 53. Restate

- 状態を持ち障害に強いアプリを作るための永続実行基盤である。実行の全段階を記録し、確実な復旧とサービス間の厳密に 1 回の通信を保証する。
- Basic Services (状態を持たない関数)、Virtual Objects (並行して動く状態を持つ実体)、Workflows (多段の処理) の 3 種類に分けて作る。大規模な保険システムで評価中で、性能に満足している。

### 54. SkyPilot

- UC Berkeley の Sky Computing Lab による、AI ワークロードを自社環境やクラウドで動かし拡張するオープンソースの基盤である。主要なクラウドと Kubernetes から、最も安く空いている GPU を自動で探して確保する。
- Slurm のような使いやすさ、Pod への直接の SSH、ギャングスケジューリング、複数クラスターへの対応を備える。

### 55. StarRocks

- 従来の OLAP の速さとレイクハウスの柔軟さを組み合わせた分析用データベースである。SIMD に最適化した実行エンジン、列指向の保存、コストベースの最適化で、大規模でも 1 秒未満で応答する。
- Apache Iceberg などのオープンな形式の上で、事前計算やコピーなしに複雑な分析を実行できる。高い同時実行と鮮度の両方が要る用途の候補である。

### 56. Uncloud

- Docker Compose のアプリを、Kubernetes の運用負担なしに本番へ持っていける軽いコンテナオーケストレーションの道具である。WireGuard のメッシュと Caddy で、複数台への拡張、無停止デプロイ、自動 HTTPS を実現する。
- 中央の制御面を持たない完全な分散設計で、一部の機械が落ちてもクラスターの操作を続けられる。クラウドの VM と物理サーバーを混ぜて使える。

## See also

- [Thoughtworks Technology Radar Vol.33 の全体像と 4 つのテーマ](/references/ai/thoughtworks-technology-radar-vol-33/thoughtworks-radar-vol-33-overview.md)
- [Thoughtworks Technology Radar Vol.33: Techniques](/references/ai/thoughtworks-technology-radar-vol-33/thoughtworks-radar-vol-33-techniques.md)
- [Thoughtworks Technology Radar Vol.35: Platforms](/references/ai/thoughtworks-technology-radar-vol-35/thoughtworks-radar-vol-35-platforms.md)
