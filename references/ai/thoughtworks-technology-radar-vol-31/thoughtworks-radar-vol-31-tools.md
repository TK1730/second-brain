---
type: reference
title: 'Thoughtworks Technology Radar Vol.31: Tools'
description: 'Thoughtworks Technology Radar Vol.31 (2024 年 10 月) の Tools 象限 33 項目の要約で、API テスト・シークレット管理・クラウドセキュリティの定番、開発環境とコードレビューの道具、AI コーディング支援、Rust 製の速い道具をリングごとにまとめる。'
tags: [ai, thoughtworks, technology-radar, tools, developer-experience, coding-assistant, rust]
status: stable
verified: { by: claude-code/claude-opus-5-5, at: 2026-11-26T00:00:00Z }
stale_after: 2027-11-26T00:00:00Z
---

# Thoughtworks Technology Radar Vol.31: Tools

Thoughtworks Technology Radar Vol.31 (2024 年 10 月) の Tools (道具) 象限の要約である。
API テスト、シークレット管理、クラウドセキュリティなどの定番に加え、開発環境を揃える道具、AI コーディング支援、Rust で書かれた速い道具が並ぶ。

- 出典: Thoughtworks Technology Radar Volume 31 (PDF)、[thoughtworks.com/radar](https://www.thoughtworks.com/radar)

[TOC]

## Adopt

### 42. Bruno

- Postman や Insomnia に代わる、オープンソースのデスクトップの API テスト・開発・デバッグの道具である。オフライン専用の設計で、協働、プライバシー、セキュリティを重視する。
- コレクションは Bru Lang というテキスト形式でファイルシステムに置かれ、Git で共有できる。VPN やプロキシの環境では、リクエストが予期せず失敗する報告がある。

### 43. K9s

- Kubernetes を操作するターミナルの道具で、ログ、メトリクス、カスタムリソース (CRD) の表示が強化された。
- `kubectl debug` との連携やマルチクラスターへの対応が進み、ショートカットの表示で kubectl に不慣れな開発者も使いやすくなった。

### 44. SOPS

- KMS などで暗号化したファイルを編集する道具である。シークレットはソースコードから切り離すのが原則だが、インフラの立ち上げ用の初期の認証情報や、レガシーのリポジトリから外せないシークレットの管理に使う。
- AWS や GCP の KMS、Azure Key Vault、PGP 鍵と連携する。リポジトリでシークレットを扱う必要があるとき、多くのチームの既定である。

### 45. Visual regression testing tools

- 画面の見た目の差分を検出する道具で、画素の単純比較から、パターン照合や OCR、機械学習による比較へと進化した。動いた要素や動的な内容でも正確に比べられる。
- E2E の機能テストの代わりにはならないが、UI テスト戦略の一部として安全な既定の選択肢になったため Adopt にした。Applitools Eyes で良い結果を得ている。

### 46. Wiz

- 多くのプロジェクトで選ばれているクラウドセキュリティ基盤である。継続的に変更を走査し、似た道具より早く危険を見つける。
- 配備前の成果物 (コンテナイメージ、インフラのコード) と稼働中の環境の両方で、設定ミス、脆弱性、漏れたシークレットを検出する。報告機能も強力である。

## Trial

### 47. AWS Control Tower

- 複数チームでの AWS アカウント管理の第一の選択肢である。新しいランディングゾーンに、セキュリティとコンプライアンスの統制を自動で適用する (変更時点でのコンプライアンス)。
- Account Factory for Terraform (AFT) で、アカウントの用意をインフラのコードのパイプラインで行える。

### 48. CCMenu

- CI のビルドの状態を Mac のメニューバーに表示する小さなアプリで、Thoughtworks の社員が作った。リモートワークで、チーム部屋の大画面の代わりになる。
- cctray 形式を出せる CI サーバー (Jenkins、TeamCity など) に対応し、書き直しで GitHub Actions にも対応した。

### 49. ClickHouse

- リアルタイム分析のためのオープンソースの列指向 OLAP データベースである。事前集計なしで対話的なクエリを実行できる。
- OpenTelemetry のデータの保存先としても優れ、Jaeger と連携して大量のトレースを効率よく分析できる。

### 50. Devbox

- Nix パッケージマネージャーを使い、仮想マシンやコンテナなしにプロジェクトごとの再現可能なローカル開発環境を作る CLI である。
- 一度設定すれば `devbox shell` だけで新しい端末に同じ環境を再現でき、新しい開発者の受け入れが楽になった。devcontainer.json の生成もできる。

### 51. Difftastic

- 構文を理解して差分を表示する道具である。ファイルを抽象構文木に解析して比べ、プログラムの構文に影響する変更だけを強調する。50 を超える言語に対応する。
- 新しい道具ではないが、LLM のコーディング支援で人がレビューするコードが増える今、注目する価値がある。

### 52. LinearB

- エンジニアリングの指標を自動で集め、改善を支援する基盤である。ソースコード、CI/CD、コミュニケーションの道具と連携する。
- DORA 指標を重視し、手作業や複雑な自前のダッシュボードなしで追跡できる点を評価している。

### 53. pgvector

- PostgreSQL のベクトル類似検索の拡張で、ベクトルを構造化データと同じデータベースに置ける。専用のベクトル DB の高度な機能は無いが、ACID などの PostgreSQL の強みを使える。
- マネージドの PostgreSQL がある環境で、別のベクトルストアなしに一般的なベクトル検索をまかなえるため Trial に移した。

### 54. Snapcraft build tool

- 自己完結したアプリ (snap) を作るオープンソースの CLI である。自動運転システムを snap にまとめ、公開ストアではなく社内の成果物リポジトリに出している。

### 55. Spinnaker

- Netflix が作ったオープンソースの継続的デリバリー基盤である。spin CLI でパイプラインをコードとして書けるようになった。
- 単純な CD には勧めないが、複雑なデプロイパイプラインでは多くの人に選ばれている。

### 56. TypeScript OpenAPI

- tsoa とも呼ばれ、TypeScript のコントローラーとモデルを正として、注釈から OpenAPI の仕様とルートを生成する。Express、Hapi、Koa に対応する。

### 57. Unleash

- 最も単純なフィーチャートグルが推奨だが、チームの拡大で手作りのトグルの管理が難しくなったときの選択肢である。サービスとしても自前でも使える。
- 段階的な展開や利用者の区分にも対応し、大規模なフィーチャー管理に向く。OpenFeature の公式対応はまだ無い。

## Assess

### 58. Astronomer Cosmos

- Airflow で dbt core のワークフローを自然に扱うためのプラグインである。dbt のノードを Airflow のタスクに変え、依存関係と実行状況を Airflow の画面で見られる。

### 59. ColPali

- 視覚言語モデルを使う PDF 文書の検索の道具である。テキストの埋め込みや OCR ではなく、ページ全体を画像として埋め込み、図や表を含む文書の RAG の性能を上げる。
- 複数の顧客で有望な結果が出たが、まだ初期の段階である。

### 60. Cursor

- AI を前提に作られたコードエディターで、継続的な改善で質的な変化が起きた。既存のコードベースに基づく文脈の推論が強い。
- 断片のコードではなく、複数行・複数ファイルの編集ができる点が際立つ。VS Code から派生しており、AI プログラミングの道具の新たな競争を主導している。

### 61. Data Mesh Manager

- データメッシュの基盤のメタデータ層を担う。データプロダクトの定義と、データ契約の仕様を扱い、DataContract CLI でビルドパイプラインに組み込める。
- データカタログ、データ品質の指標と規則の管理による分散ガバナンスも提供する。

### 62. GitButler

- 複数のブランチやコミットの扱いを簡単にする Git の GUI クライアントである。未コミットの変更を独自に追跡し、仮想ブランチに振り分ける。
- 小さな変更を trunk に頻繁に入れれば不要な問題とも言えるが、レビューの長いプルリクエストの流れでは役立つ。GitHub と連携してプルリクエストを出せる。

### 63. JetBrains AI Assistant

- JetBrains の IDE に統合されたコーディング支援で、補完、テスト生成、スタイルガイドへの準拠を支援する。コーディングスタイルを覚えて次のセッションに生かす。
- 自社でモデルを運用していないため、第三者によるデータの扱いを懸念する顧客には合わないことがある。

### 64. Mise

- nvm、pyenv、rbenv、rustup などを 1 つで置き換え、asdf と互換のある道具である。Rust で書かれ、shim を使わず事前に PATH を変えるので asdf より速い。
- 同じ道具の複数のバージョンの同時導入、あいまいな一致を許すコマンド、プロジェクトのタスク実行の機能を持つ。

### 65. Mockoon

- オープンソースの API モックの道具である。直感的な画面、ルートと動的な応答の設定、モックデータの自動作成ができ、OpenAPI に対応する。
- 定義した呼び出しだけを偽物にして他は本物に転送する部分モックもできるが、使いすぎると複雑になる。

### 66. Raycast

- キーボードからアプリの起動、コマンド実行、ファイル検索、自動化ができる macOS のランチャーである。VS Code、Slack、Jira などと連携でき、拡張しやすい。

### 67. ReadySet

- MySQL と PostgreSQL のクエリキャッシュである。手動の無効化ではなく、データベースの複製ストリームでキャッシュを少しずつ更新する。
- 通信の互換性があるので、アプリを変えずにデータベースの前に置いて読み取りを水平に拡張できる。

### 68. Rspack

- Webpack を置き換えるために作られたバンドラーで、1.0 になった。Webpack のプラグインやローダーと互換があり、複雑な Webpack 構成の移行では Vite より有利なことがある。
- Rust で書かれ、Webpack よりかなり速く、多くの場合 Vite より速い。

### 69. Semantic Router

- 埋め込みベクトルで利用者の意図を推定し、要求を適切なエージェントやフローに振り分ける高速な判断層である。不要な LLM 呼び出しを減らし、費用を抑える。

### 70. Software engineering agents

- GitHub の課題や Jira のチケットから計画とコード変更を作り、人がレビューするプルリクエストまで出すことを目指す道具である。
- 幅広い作業を自律的にこなす汎用エージェントという目標はまだ説得力のある形になっていないが、範囲の狭い単純な作業ではまもなく実用になると見ている。ベンチマークは割り引いて見る。

### 71. uv

- Rust で書かれた Python のパッケージ管理の道具で、他の道具を大きく上回る速さをうたう。
- 秒単位の速さより生態系や長期の支援が大事だという議論もあったが、速さはフィードバックの短縮と開発者体験の向上に効き、CI のキャッシュの複雑さも減らせる。

### 72. Warp

- コマンドの出力をブロックに分けて読みやすくする macOS と Linux のターミナルである。AI によるコマンドの提案や自然言語の処理、コマンドと出力をまとめるノートブックの機能を持つ。

### 73. Zed

- Atom の作者たちが作った、Rust 製の速いエディターである。多言語対応、内蔵ターミナル、複数バッファの編集、複数の LLM との連携を持つ。
- GitHub の ID で相手を見つけ、同じワークスペースをリアルタイムで共同編集できる機能に、ペアプログラミングの観点から注目している。

## Hold

### 74. CocoaPods

- Swift と Objective-C の依存管理として広く使われてきたが、保守モードに入り、活発な開発は終わった。Xcode に統合され Apple が長く支える Swift Package Manager への移行が勧められる。

## See also

- [Thoughtworks Technology Radar Vol.31 の全体像と 4 つのテーマ](/references/ai/thoughtworks-technology-radar-vol-31/thoughtworks-radar-vol-31-overview.md)
- [Thoughtworks Technology Radar Vol.31: Techniques](/references/ai/thoughtworks-technology-radar-vol-31/thoughtworks-radar-vol-31-techniques.md)
- [Thoughtworks Technology Radar Vol.31: Platforms](/references/ai/thoughtworks-technology-radar-vol-31/thoughtworks-radar-vol-31-platforms.md)
