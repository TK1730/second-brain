---
type: reference
title: 'Thoughtworks Technology Radar Vol.30: Tools'
description: 'Thoughtworks Technology Radar Vol.30 (2024 年 4 月) の Tools 象限 40 項目の要約で、コンテナのビルドとノードの自動拡張、CI のランナー、依存関係とサプライチェーンの道具、IaC の検査、AI コーディング支援、ローカル LLM と LLM のガードレールをリングごとにまとめる。'
tags: [ai, thoughtworks, technology-radar, tools, coding-assistant, kubernetes, infrastructure-as-code, security]
status: stable
verified: { by: claude-code/claude-opus-5-5, at: 2026-11-26T00:00:00Z }
stale_after: 2027-11-26T00:00:00Z
---

# Thoughtworks Technology Radar Vol.30: Tools

Thoughtworks Technology Radar Vol.30 (2024 年 4 月) の Tools (道具) 象限の要約である。
コンテナと Kubernetes、CI、依存関係とサプライチェーン、IaC の道具に加え、AI コーディング支援とローカルで動かす LLM が並ぶ。
今号の Tools に Hold の項目は無い。

- 出典: Thoughtworks Technology Radar Volume 30 (PDF)、[thoughtworks.com/radar](https://www.thoughtworks.com/radar)

[TOC]

## Adopt

### 44. Conan

- C/C++ アプリケーションのためのオープンソースの依存関係管理の道具である。主要な OS で動き、サーバー、デスクトップ、モバイル、組み込みを対象にできる。
- ビルド済みのバイナリを使うのでビルド時間が大きく減り、CMake などと連携する。環境をまたいだビルドの再現性と開発速度が上がる。

### 45. Kaniko

- コンテナベースのパイプラインの中で、Docker を使わずにコンテナイメージをビルドする道具である。
- さまざまなパイプラインで経験を積み、柔軟性と性能を評価して、この分野の既定の道具として Adopt に移した。

### 46. Karpenter

- ワークロードと Pod のスケジューリング制約を分析し、適切なインスタンス種別を選んでノードを起動・停止する、オープンソースの Kubernetes のノード自動拡張オペレーターである。Cluster Autoscaler より柔軟である。
- AWS が EKS 向けに開発したが、Azure も AKS で対応し始め、クラウドの Kubernetes サービス全体で既定のノード自動プロビジョナーになりつつある。

## Trial

### 47. 42Crunch API Conformance Scan

- OpenAPI の仕様と、実際の API の振る舞いのずれを見つける動的テストの道具である。実際のトラフィックを生成してエンドポイントと対話する。
- ずれを早期に見つけるほか、弱い認証、安全でないデータの扱い、不十分な入力検証などの脆弱性を報告し、対策を勧める。

### 48. actions-runner-controller

- GitHub Actions のセルフホストランナーを運用する Kubernetes のコントローラーである。GitHub のクラウドのランナーから届かない資源や、特別な OS の要件がある場合に使う。
- リポジトリや組織ごとの実行中のワークフロー数に応じてランナーを増減でき、Linux と Windows の両方のランナーを扱える。

### 49. Android Emulator Container

- 複数の Android のバージョン用のエミュレーターの準備や OS の互換性の問題をなくし、Android アプリのテストを CI に組み込みやすくする。
- コミットごとの計装テストと、夜間の E2E テストに使っている。

### 50. AWS CUDOS

- 費用を適合度関数として監視するという方針のもと、AWS の CUDOS ダッシュボードで、大きな組織の部門や法人ごとの AWS Marketplace の支出を監視している。資源単位の費用と利用状況が分かる。

### 51. aws-nuke

- 開発用やサンドボックスの AWS アカウントにたまった未使用の資源を、既定のものや AWS 管理のものを除いてすべて削除し、初日の状態に戻す。除外ポリシーで重要な資源を守れる。
- 費用削減や災害復旧訓練の後片付けに使える。非常に破壊的なので本番では使わず、必ず事前に試行 (dry run) する。

### 52. Bruno

- Postman や Insomnia の代替となる、オープンソースのデスクトップの API テストの道具である。コレクションをファイルシステムに保存するので、Git で共同作業できる。オフライン専用の単純な設計が好まれている。

### 53. Develocity

- 旧 Gradle Enterprise。ビルドキャッシュと予測的なテスト選択で、大規模なプロジェクトのビルドとテストを速くする。不安定なテストの特定や、ワークフローのどこを最適化すべきかの分析にも使える。

### 54. GitHub Copilot

- AI コーディング支援の市場が混み合うなか、今も既定の選択肢である。チャット機能が大きく改善された。
- インラインチャットでコメントを書かずに指示でき、既存のコードも変更できる。`@workspace` でコードベース全体について質問できる。去年試して見切った人も、もう一度試すことを勧める。

### 55. Gradio

- 機械学習モデルに対話的な Web の画面を付けるオープンソースの Python ライブラリである。非技術者にも入力、制約、出力が分かりやすくなる。
- 実験とプロトタイプに強く、大きなイベントでの実演にも使った。こうした用途での能力を評価して Trial に移した。

### 56. Gradle Version Catalog

- Gradle で依存関係を中央の 1 か所で管理する機能である。特に Android のマルチモジュールのプロジェクトで、依存の名前とバージョンを型安全に参照できる。

### 57. Maestro

- モバイルアプリの複雑な操作の流れをテストする道具である。iOS、Android、React Native、Flutter に対応し、宣言的な YAML で UI 操作を自動化する。学びやすく、開発の流れに組み込みやすい。

### 58. Microsoft SBOM tool

- SPDX 互換の SBOM (ソフトウェア部品表) を生成するオープンソースの道具である。npm、pip、Gradle など多くのパッケージマネージャーに対応し、CI/CD にも組み込める。
- 部品が見えることで、脆弱性の特定、ライセンスの遵守、サプライチェーンの透明性が上がる。

### 59. Open Policy Agent (OPA)

- ポリシーを宣言し、強制し、制御するための統一的なフレームワークと言語である。分散システム、特に変更の時点でコンプライアンスを実装したい場面でポリシーを定義する手段として好まれている。
- Kubernetes へのデプロイの制御、サービスメッシュでのアクセス制御、アプリの資源への細かいセキュリティポリシーなどに使える。導入には一定の複雑さがある。

### 60. Philips's self-hosted GitHub runner

- AWS の EC2 スポットインスタンス上に GitHub Actions のセルフホストランナーを立てる Terraform モジュールである。Lambda で増減のライフサイクルを管理する。
- 組織のセキュリティ境界の中からしかデプロイできない場合などに、ランナーの用意と管理を大きく簡単にする。Kubernetes を使うなら actions-runner-controller が代替になる。

### 61. Pop

- 旧 Screen。複数人での画面共有、書き込み、高品質な音声と映像に対応した、リモートのペアプログラミングの道具である。ペアプロや遠隔の作業セッションで好評である。

### 62. Renovate

- 依存関係を自動で監視・更新する道具で、多くのチームが Dependabot より好んでいる。
- コードやライブラリだけでなく、実行時の道具、インフラ、外部サービスへの依存も扱え、設定とカスタマイズの自由度が高い。Dependabot も安全な既定だが、Renovate の評価を勧める。

### 63. Terrascan

- IaC の静的解析の道具で、クラウドのインフラを用意する前にセキュリティの脆弱性とコンプライアンスの問題を見つける。Terraform、Kubernetes、Helm、CloudFormation、Dockerfile などに対応する。pre-commit フックと CI で使っている。

### 64. Velero

- Kubernetes の資源と永続ボリュームをバックアップ・復元するオープンソースの道具である。オンデマンドと定期のバックアップで、災害復旧やクラスターの移行を簡単にする。etcd などの低い層ではなく Kubernetes の API に頼る点が評価されている。

## Assess

### 65. aider

- ターミナルで CLI として起動する、オープンソースの AI コーディング支援である。チャットから複数のファイルに書き込めるため、複数ファイルにまたがる変更や新しいファイル・フォルダーの作成ができる。
- 自分の OpenAI か Azure OpenAI の API キーが要る。API とのやり取りが多いので、費用と利用制限に注意する。

### 66. Akvorado

- Netflow、IPFIX、sFlow のネットワークフローを取り込み、インターフェース名や地理情報を加えて ClickHouse に保存する、オープンソースのネットワーク監視・分析の道具である。アプリの層では見えないネットワークの層の問題調査に役立つ。

### 67. Baichuan 2

- 2.6 兆トークンの高品質なコーパスで学習した、新世代のオープンソースの LLM である。中国語、英語、多言語のベンチマークで、規模の割に良い成績を出す。医療や法律の分野のコーパスでも学習しており、これらの分野で好んで使っている。

### 68. Cargo Lambda

- Rust で AWS Lambda の関数を書くための cargo のサブコマンドである。Docker や VM なしで手元で実行・テストでき、Zig のツールチェーンで Arm と Intel の Linux 向けにクロスコンパイルできる。

### 69. Codium AI

- AI によるテスト生成に特化したコーディング支援である。いきなりテストコードを出すのではなく、自然言語のシナリオの一覧を先に示し、どれをテストにするかを開発者が判断できる点を評価している。

### 70. Continue

- VS Code と JetBrains の IDE 向けの、オープンソースのコーディング支援である。チャットからのコピーと貼り付けの手間をなくす。商用とオープンソースの複数のモデル、自前で運用する LLM に対応し、オフラインでも使える。

### 71. Fern Docs

- 仕様ファイルから、使いやすい API ドキュメントの Web サイトを自動生成する。仕様は API のコードと一緒にバージョン管理できる。
- ただし独自の設定ファイルで API 情報を保守する必要がある。OpenAPI からの変換はあるが、注釈付きのソースコードから直接生成する道具のほうが望ましいとしている。

### 72. Granted

- 複数の AWS アカウントを、ブラウザーで同時に開いて切り替えやすくするコマンドラインの道具である。Firefox の Multi-Account Containers や Chromium のプロファイルで ID を分ける。AWS SSO の一時的な認証情報を平文ではなくキーチェーンに保存する。

### 73. LinearB

- ベンチマーク、ワークフローの自動化、投資の 3 領域で、エンジニアリングのリーダーにデータに基づく洞察を与える基盤である。
- DORA の 4 つの指標 (デプロイ頻度、リードタイム、変更失敗率、復旧時間) を重視した、設定済みの指標を持つ。DORA の指標の収集はこれまで難しかったので、有力な選択肢である。

### 74. LLaVA

- 画像エンコーダーと LLM をつないだ、オープンソースの大規模マルチモーダルモデルである。指示に従う能力が高く、GPT-4 Vision と比べても有望である。画像についての質問応答で試している。

### 75. Marimo

- 再現性と対話性を重視した Python のノートブックである。ノートブックを隠れた状態のない普通の Python ファイルとして保存し、依存関係に基づく決まった順序で、変数が変わると影響するセルを自動で実行する。
- Web アプリとして配置でき、デモやプロトタイプにも使える。ただしノートブックを本番に使うことには引き続き注意を促している。

### 76. Mixtral

- Mistral のオープンウェイトの LLM ファミリーで、疎な Mixture of Experts の構造を使う。7B と 8x7B があり、32,000 トークンのコンテキストを持つ。自前で運用する LLM の有力な選択肢である。
- 安全性の調整は既定ではされていないので、用途に合わせて管理する必要がある。インドの法律タスク向けに Mistral 7B を調整した Aalap を作った経験がある。

### 77. NeMo Guardrails

- NVIDIA による、対話型アプリケーションの LLM にガードレールを実装するオープンソースの道具である。事実の正確さ、偏り、悪用といった LLM の限界に対する安全策になる。
- プログラム可能な規則と実行時の統合に対応し、既存の LLM アプリに大きなコード変更なしで適用できる点を評価している。

### 78. Ollama

- 手元の機械で LLM を動かし管理するオープンソースの道具である。LLaMA-2、CodeLLaMA、Falcon、Mistral などをダウンロードし、CLI、API、SDK から使える。ローカルで LLM を扱う開発者体験を改善している。

### 79. OpenTofu

- HashiCorp のライセンス変更を受けて作られた Terraform のフォークで、Linux Foundation に受け入れられた。現在の版は、オープンソースだった最後の Terraform と互換で、1.7 でクライアント側の暗号化を加えた。
- 今後の Terraform との互換性や支援企業の長期的な関与は不透明である。リスクを管理でき、コードベースに貢献できるチーム以外は慎重に使う。

### 80. QAnything

- PDF、DOCX、PPTX、XLSX、MD など多くの形式から情報を要約・抽出する、質問応答の画面を持つ知識管理エンジンである。オフラインでの導入にも対応する。チームの知識ベース作りや、LLM と RAG の可能性を示す概念実証に使っている。

### 81. System Initiative

- インフラのデジタルツインとも言える、実験的な DevOps の道具である。画面上で状態を変えると、それに対応する変更をインフラに適用でき、インフラの変更も状態に反映される。
- GUI の道具には懐疑的だが、TypeScript で拡張やポリシーの強制ができる。IaC の現状を打ち破る創造的な発想を評価している。まだ本番向けではない。

### 82. Tetragon

- eBPF を使った、オープンソースのセキュリティの可観測性と実行時の強制の道具である。Falco のような脅威の検出を超え、Linux カーネルで実行時にセキュリティポリシーを強制する。

### 83. Winglang

- CloudFormation、Terraform、Pulumi、Kubernetes などの基盤の違いを高い抽象で覆う、IaC の新しい道具である。コンパイル時に動いてインフラ設定を生成するコードと、実行時に動くアプリのコードを書く。手元で動かすシミュレーションと、組み込みのテストの仕組みを持つ。

## See also

- [Thoughtworks Technology Radar Vol.30 の全体像と 4 つのテーマ](/references/ai/thoughtworks-technology-radar-vol-30/thoughtworks-radar-vol-30-overview.md)
- [Thoughtworks Technology Radar Vol.30: Techniques](/references/ai/thoughtworks-technology-radar-vol-30/thoughtworks-radar-vol-30-techniques.md)
- [Thoughtworks Technology Radar Vol.35: Tools](/references/ai/thoughtworks-technology-radar-vol-35/thoughtworks-radar-vol-35-tools.md)
