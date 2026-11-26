---
type: reference
title: 'Thoughtworks Technology Radar Vol.32: Tools'
description: 'Thoughtworks Technology Radar Vol.32 (2025 年 4 月) の Tools 象限 32 項目の要約で、Renovate・uv・Vite などの定番の道具、Cline・Cursor・Windsurf などの監督付きコーディングエージェント、図や API テスト、マージ支援、LLM 関連の道具をリングごとにまとめる。'
tags: [ai, thoughtworks, technology-radar, tools, coding-agent, developer-experience]
status: stable
verified: { by: claude-code/claude-opus-5-5, at: 2026-11-26T00:00:00Z }
stale_after: 2027-11-26T00:00:00Z
---

# Thoughtworks Technology Radar Vol.32: Tools

Thoughtworks Technology Radar Vol.32 (2025 年 4 月) の Tools (道具) 象限の要約である。
依存関係の更新やビルドの定番の道具と、IDE の中で監督しながら動かすコーディングエージェントが中心である。
今号の Tools に Hold の項目は無い。

- 出典: Thoughtworks Technology Radar Volume 32 (PDF)、[thoughtworks.com/radar](https://www.thoughtworks.com/radar)

[TOC]

## Adopt

### 51. Renovate

- 依存関係のバージョンを先回りして管理する道具として多くのチームが選んでいる。GitHub なら Dependabot も安全な既定だが、Renovate はより包括的でカスタマイズしやすい。
- ツール、インフラ、社内の依存まで監視させ、更新 PR の自動マージで開発者の疲れを減らす。

### 52. uv

- Rust で書かれた次世代の Python のパッケージ・プロジェクト管理ツールで、「極めて速い」ことが最大の価値である。Poetry、pyenv、pipx を置き換える。
- 新しい道具なので Adopt は大胆だが、現場の開発者は今使える最良の道具として一貫して勧めている。

### 53. Vite

- 高速なホットリロードを持つフロントエンドのビルドツールで、Vue、SvelteKit、React (create-react-app は非推奨) の既定の選択肢になった。開発のための組織 VoidZero ができ、長期の持続性も高まった。

## Trial

### 54. Claude Sonnet

- コーディング、文章、分析、画像の理解に優れた言語モデルで、ブラウザー、ターミナル、主要な IDE、GitHub Copilot から使える。3.5 を広く使い、生産性が大きく上がった。
- 新規開発、特に設計やアーキテクチャの議論で優れる。AI モデルを「安定」と呼ぶには早いが、最も信頼できるモデルの 1 つである。

### 55. Cline

- 監督付きのソフトウェアエンジニアリングエージェントとして最有力の 1 つである、オープンソースの VS Code 拡張である。Plan & Act モード、トークン使用量の表示、MCP 連携を持つ。
- データを手元に保存する。コンテキストの組み立てが効果的な分トークン費用がかさみ、レート制限にもかかりやすい。OpenRouter のような提供者を使うとよい。

### 56. Cursor

- AI ファーストのコードエディターで、コンテキストの組み立てが効果的で、多くのモデルを使える。git の差分、過去の会話、Web 検索、ライブラリの文書、MCP をコンテキストに使える。
- エージェントモードが強く、ファイルの読み書きやコマンド実行を行い、lint やコンパイルのエラーを自ら直す。

### 57. D2

- テキストから図を作る、オープンソースの diagrams-as-code の道具である。簡潔さより読みやすさを重んじた宣言的な構文で、ソフトウェアの文書やアーキテクチャ図向けに作られている。

### 58. Databricks Delta Live Tables

- ストリーミングとバッチのデータパイプラインを宣言的に管理し、チェックポイント管理などを自動化する。
- 癖を理解する必要がある: 1 度に 1 つのパイプラインからしか書き込めない、ストリーミングテーブルは追記のみ、パイプラインを消すとテーブルとデータも消える。

### 59. JSON Crack

- テキストのデータを対話的なグラフで表示する VS Code 拡張である。YAML、TOML、XML も扱え、枝やノードを隠しながらデータを探索できる。ノード数に上限がある。

### 60. MailSlurp

- メールと SMS のテスト用サービスで、受信箱や電話番号を REST API で作り、コードの中でメールを検証できる。手動テスト向けのダッシュボードもある。

### 61. Metabase

- 多様なデータソースからデータを可視化・分析するオープンソースの BI ツールである。ダッシュボードをアプリケーションに埋め込む SDK もあり、軽量な BI として使いやすい。

### 62. NeMo Guardrails

- 対話型アプリケーションの LLM にガードレールを付ける、NVIDIA のオープンソースのツールキットである。チームで採用が広がり、文書の改善、Colang 2.0、出力レールでのストリーミング、コンテンツ安全性や脱獄検出のマイクロサービスとの統合が進んだため Trial に移った。

### 63. Nyx

- 言語に依存しない、セマンティックリリースの道具である。Conventional Commits から変更履歴を自動生成する。Gitflow なども支えるが、長命なブランチには注意を促しており、トランクベース開発での利用を勧める。

### 64. OpenRewrite

- ライブラリの新しい API への移行など、規則に沿った大規模なリファクタリングの道具である。JavaScript にも対応した。
- 規則に沿った変更なら、AI コーディング支援より速く、安く、確実である。変更内容を書いたレシピの一覧が付いている。

### 65. Plerion

- AWS に特化したクラウドセキュリティ基盤で、インフラ、サーバー、アプリケーションの設定不備や脆弱性を見つけ、リスクで優先順位を付ける。

### 66. Software engineering agents

- 完全自律のエージェントはまだ説得力が無いが、IDE の中で監督しながら動かすエージェントモードが大きく進んだ。チャットから複数ファイルの変更、コマンド実行、テスト、lint への対応まで行う。
- Cursor、Cline、Windsurf が先行し、モデルは Claude の Sonnet が最先端である。問題の範囲を小さく保ち、AI に優しいコードベースで使う。慢心の危険が高まるので、ペアプログラミングなどのレビュー規律を保つ。

### 67. Tuple

- リモートのペアプログラミングに特化した道具で、Windows にも対応した。画面共有で私的なウィンドウを隠せるようになり、IDE 以外の協働にも使える。
- 相手はデスクトップ全体にアクセスできるので、プライバシー設定と作法を事前に教える。

### 68. Turborepo

- 大きな JavaScript・TypeScript のモノレポで、ビルドタスクを解析、キャッシュ、並列化して速くする。Nx と違い、プロジェクトごとの `package.json` で同じ依存の複数バージョンを持てる。

## Assess

### 69. AnythingLLM

- 大きな文書と対話できるオープンソースのデスクトップアプリで、LLM とベクトルデータベースがすぐ使える。ワークスペースで文書と会話を整理し、スキルをエージェントとして組める。

### 70. Gemma Scope

- LLM の内部の働きを理解する機械論的解釈可能性 (mechanistic interpretability) の道具で、Gemma 2 の内部を調べられる。ハルシネーションや偏りの原因の特定に役立つ。

### 71. Hurl

- 独自の構文のテキストファイルで、HTTP リクエストの連続を定義して実行する。応答の検証、値の抽出と連結、HTML や JSON のテストレポートができ、テストをリポジトリに置ける。

### 72. Jujutsu

- Git リポジトリを保存先に使いながら、Git に代わる完全なバージョン管理の操作を提供する。使いやすさを重んじ、競合の解決を第一級に扱う。

### 73. kubenetmon

- ClickHouse が公開した、Kubernetes のデータ転送量を主要なクラウドにまたがって計測する道具である。不透明なデータ転送費用に悩むなら調べる価値がある。

### 74. Mergiraf

- コードを行ではなく構文木として見て、マージの競合を解決する。git のマージドライバーとして設定でき、merge や cherry-pick で自動的に使われる。AI で変更が大きくなりがちなので有効である。

### 75. ModernBERT

- BERT の後継のエンコーダー専用モデル群で、性能と精度を上げ、はるかに長いコンテキストを扱える。自然言語処理では、汎用の生成モデルを選ぶ前に検討する。

### 76. OpenRouter

- 複数の LLM に 1 つの API でつなぐ。実験しやすく、ベンダー依存を減らし、レート制限を回避できる。上乗せ料金があるので、本当にモデルを切り替える必要があるかを考える。

### 77. Redactive

- 規制のある組織が、非構造化データを AI 用に安全に準備する基盤である。Confluence などから RAG 用の索引を作り、元のシステムの権限を実時間で適用する。

### 78. System Initiative

- Infrastructure as Code とまったく違う方向を示す実験的な DevOps の道具である。ベータを終えて Apache 2.0 で公開されたが、大企業の規模に耐えるにはまだ先がある。

### 79. TabPFN

- 小さな表形式データの分類を、学習やハイパーパラメーター調整なしに文脈内学習で行う Transformer モデルである。大きなデータや回帰には課題がある。

### 80. v0

- Vercel の、スクリーンショット、Figma のデザイン、プロンプトからフロントエンドのコードを生成する AI の道具である。プレビューと Vercel への 1 回のデプロイができ、試作の出発点に向く。

### 81. Windsurf

- Codeium の AI コーディング支援で、エージェントの機能が強い。ブラウザープレビュー (DOM やコンソールへのアクセス) や Web での調査機能を次々に追加している。

### 82. YOLO

- Ultralytics による画像認識モデルのシリーズで、YOLO11 は精度と効率を高め、エッジ端末での実時間処理に向く。特定の作業では、LLM より従来の機械学習モデルが強いことを思い出させる。

## See also

- [Thoughtworks Technology Radar Vol.32 の全体像と 4 つのテーマ](/references/ai/thoughtworks-technology-radar-vol-32/thoughtworks-radar-vol-32-overview.md)
- [Thoughtworks Technology Radar Vol.32: Techniques](/references/ai/thoughtworks-technology-radar-vol-32/thoughtworks-radar-vol-32-techniques.md)
