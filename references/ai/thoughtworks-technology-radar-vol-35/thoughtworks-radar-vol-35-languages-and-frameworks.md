---
type: reference
title: 'Thoughtworks Technology Radar Vol.35: Languages and frameworks'
description: 'Thoughtworks Technology Radar Vol.35 (2026 年 11 月) の Languages and frameworks 象限 14 項目の要約で、データ契約の標準、エージェントのフレームワーク、認可と個人情報保護、評価とレッドチーミング、形式仕様言語をリングごとにまとめる。'
tags: [ai, thoughtworks, technology-radar, frameworks, agent, formal-methods, data-contract]
status: stable
verified: { by: claude-code/claude-opus-5-5, at: 2026-11-26T00:00:00Z }
stale_after: 2027-11-26T00:00:00Z
---

# Thoughtworks Technology Radar Vol.35: Languages and frameworks

Thoughtworks Technology Radar Vol.35 (2026 年 11 月) の Languages and frameworks (言語・フレームワーク) 象限の要約である。
データ契約の標準、エージェントを作るフレームワーク、LLM と組み合わせるセキュリティ・評価の道具、エージェントが書いたコードを確かめる形式仕様言語が並ぶ。
今号のこの象限に Caution の項目は無い。

- 出典: Thoughtworks Technology Radar Volume 35 (PDF)、[thoughtworks.com/radar](https://www.thoughtworks.com/radar)

[TOC]

## Adopt

### 104. Open Data Contract Standard (ODCS)

- データ製品のスキーマ、品質の期待値、サービスレベルを YAML で宣言的に書くデータ契約の標準である。Linux Foundation の Bitol プロジェクトが開発している。
- 競合する形式もあるが、ODCS が主流になった。宣言的なので、人もエージェントも読み、レビューし、検証しやすい。データ製品を作るときの既定の選択肢とした。

## Trial

### 105. BoTorch

- PyTorch ベースのベイズ最適化のフレームワークである。ハイパーパラメーター調整だけでなく、製品の配合や研究開発など、1 回の評価が高くつく実問題の最適化に使われている。Ax と組み合わせる。

### 106. Deep Agents

- LangChain による、長時間動くタスク向けのエージェントハーネスである。問題の分解、サブエージェントへの委任、計画、スキル、メモリ、人の承認の区切り、ファイルアクセスを備える。
- 複雑なエージェントのグラフの一部に、能力の高い長時間エージェントが要るときに役立つ。

### 107. Kagent

- エージェントを Kubernetes のカスタムリソースとして作り、動かし、管理するフレームワークと基盤である。既存の GitOps で配置・拡張・保護できる。
- OpenTelemetry、サンドボックス、メモリ、MCP 連携、エージェント間の A2A プロトコルを備える。

### 108. OpenFGA

- Google の Zanzibar に着想を得た、細かい粒度の認可システムである。利用者と資源の関係から権限を判断する (ReBAC)。
- ロールによる認可 (RBAC) では足りない、資源ごとの権限や階層的な関係を扱える。サイドカーで低遅延の権限確認をした事例がある。

### 109. Presidio

- 構造化・非構造化テキストから個人情報 (カード番号、氏名、場所など) を検出し、匿名化する SDK である。LLM と連携する際のデータ保護に使える。
- 見逃しや誤検出があるので、結果を過信しない。

### 110. Promptfoo

- プロンプトとエージェントのツール呼び出しの評価、CI のゲートに加え、レッドチーミングにも使う。用途を説明すると攻撃を生成して応答を採点し、手作業の確認を修正のたびに再実行できるテストに変える。
- stateful guardrails が実行時の制御で、Promptfoo はそれが守られているかを試す役割になる。現在は OpenAI の所有だが MIT ライセンスのままである。高度な攻撃はホスト型サービスに依存するので、外に出るデータを確かめる。

## Assess

### 111. Apple Core AI

- Apple シリコンの端末上で AI モデルを動かす新しいフレームワークで、Core ML の後継である。
- Xcode の Evaluations フレームワークで、Swift Testing を広げて生成 AI 機能を評価できる (合成データ、定量指標、モデルによる採点)。

### 112. CALM

- FINOS による、ソフトウェアアーキテクチャを機械可読な形式で定義する仕様である。図や文書ではなくコードとしてアーキテクチャを持ち、意図した構造に沿っているかを検証する土台になる。

### 113. Hindsight

- AI エージェントのためのオープンソースのメモリシステムである。会話から事実や時刻を抽出して Postgres に保存し、意味・キーワード・グラフ・時間の検索を組み合わせて思い出す。
- 記憶を統合して「観察」や「メンタルモデル」に育てる点が Mem0 と違う。追加の LLM 呼び出しとインフラに見合う効果があるかを測って比較する。

### 114. Quint

- TLA+ と同じ理論に基づく形式仕様言語で、並行処理の微妙なバグを見つける。TypeScript に似た構文で読みやすく、エージェントが書いた仕様をレビューしやすい。
- 型検査、REPL、シミュレーターを持ち、仕様からトレースを作って実装を試せる。

### 115. SolidJS

- 高性能で細かい粒度のリアクティビティを持つ UI ライブラリである。最近の更新で、API 呼び出し、キャッシュ、重複リクエストの除去を外部ライブラリなしで扱えるようになった。

### 116. spartan/ui

- shadcn の考え方を Angular に適用したものである。アクセシビリティと振る舞いは上流のライブラリが保ち、見た目のコンポーネントは自分のソースに置く。Angular Material の代替になる。

### 117. TLA+

- 分散システムの設計上の欠陥を見つける形式仕様言語である。以前は重要なシステムにしか見合わなかったが、コーディングエージェントのおかげで使う費用が下がり、エージェントが書いたコードを確かめる必要から価値が上がった。
- ミューテーションテストやプロパティベーステストと並ぶ、多様な検証手段 (polyglot verification) の流れの一部である。

## See also

- [Thoughtworks Technology Radar Vol.35 の全体像と 4 つのテーマ](/references/ai/thoughtworks-technology-radar-vol-35/thoughtworks-radar-vol-35-overview.md)
- [Thoughtworks Technology Radar Vol.35: Techniques](/references/ai/thoughtworks-technology-radar-vol-35/thoughtworks-radar-vol-35-techniques.md)
- [評価駆動開発 (EDD) とは何か: AI エージェントを継続的に改善する手法](/references/ai/langchain-blog-what-is-eval-driven-development.md)
