---
type: reference
title: 'Thoughtworks Technology Radar Vol.30: Techniques'
description: 'Thoughtworks Technology Radar Vol.30 (2024 年 4 月) の Techniques 象限 18 項目の要約で、RAG、従来の NLP と LLM の組み合わせ、継続的コンプライアンス、AI のチーム活用、LLM の使いすぎや性急なファインチューニングへの注意をリングごとにまとめる。'
tags: [ai, thoughtworks, technology-radar, llm, rag, security, testing]
status: stable
verified: { by: claude-code/claude-opus-5-5, at: 2026-11-26T00:00:00Z }
stale_after: 2027-11-26T00:00:00Z
---

# Thoughtworks Technology Radar Vol.30: Techniques

Thoughtworks Technology Radar Vol.30 (2024 年 4 月) の Techniques (手法) 象限の要約である。
LLM をどう使うか (RAG、従来の NLP との組み合わせ、チームでの活用) と、その使いすぎへの注意が中心である。
リングの意味と今号のテーマは [全体像の文書](/references/ai/thoughtworks-technology-radar-vol-30/thoughtworks-radar-vol-30-overview.md) を参照する。

- 出典: Thoughtworks Technology Radar Volume 30 (PDF)、[thoughtworks.com/radar](https://www.thoughtworks.com/radar)

[TOC]

## Adopt

### 1. Retrieval-augmented generation (RAG)

- LLM の応答の質を上げるために Thoughtworks のチームが第一に選ぶパターンである。信頼できる文書を、ベクトル型や効率的な文書検索に対応したデータベース (pgvector、Qdrant、Elasticsearch Relevance Engine など) に入れておく。
- プロンプトごとに関連文書を検索してプロンプトに加え、LLM に豊かな文脈を渡す。出力の質が上がり、幻覚が大きく減る。
- コンテキストウィンドウには限りがあるので、最も関連する文書を選ぶことが肝心である。再ランク付けで関連度を上げ、文書は重なりを持たせたチャンクに分ける。

## Trial

### 2. Automatically generate Backstage entity descriptors

- Backstage の各エンティティは catalog-info ファイルで設定するが、手書きで保守すると手間がかかり、漏れや更新忘れが起きる。
- AWS リソースのタグやソースファイルのメタデータなど既存の情報源から、エンティティの記述を自動生成し、1 日 1 回などの頻度で更新するほうが効率的で誤りが少ない。

### 3. Combining traditional NLP with LLMs

- LLM は自然言語処理の万能ナイフだが、高価で、いつも最適な道具ではない。
- 文書のクラスタリング、トピック抽出、分類などは従来の NLP やデータサイエンスのほうが安く効果的なことがある。長い文章の生成や大量の文書の統合など、LLM の能力が要る段階だけで LLM を使う。
- 例として、大量の個別のトレンド文書を従来のクラスタリングでまとめ、LLM で包括的なトレンドレポートを生成した。

### 4. Continuous compliance

- 自動化を最大限に使い、開発工程と技術が業界規制やセキュリティ標準に継続的に適合していることを確かめる手法である。
- 準拠のチェックをパイプラインに組み込み、規則をコード化して、脆弱性の検査、コーディング標準の強制、インフラ設定の変更追跡を行う。自動レポートで監査を簡単にする。
- SBOM の公開や SLSA の推奨事項の適用が出発点になる。ソフトウェアで動く自動車など安全性が重要な業界では、認証工程の効率と信頼性も上がる。

### 5. Edge functions

- Cloudflare Workers や Amazon CloudFront の Edge Functions など、CDN 上で利用者の近くでサーバーレスのコードを実行する仕組みである。
- 応答をエッジで作れるなら遅延が下がり、リクエストやレスポンスを場所に応じて書き換えることもできる。エッジの計算資源は限られるので、短く速い状態のない処理に向く。

### 6. Security champions

- 技術的・非技術的な判断のセキュリティ上の影響を批判的に考え、チームのリーダーに問題を提起するチームメンバーである。別の職位ではなく、既存のメンバーに割り当てる責任である。
- セキュリティの専門家から訓練を受け、チームの意識を高め、開発チームとセキュリティチームの橋渡しをする。脅威モデリングを推進するのもよい例である。
- ただしチャンピオンだけに頼るのは問題で、チーム全体と管理者の関与が要る。

### 7. Text to SQL

- 自然言語の問い合わせを、データベースで実行できる SQL に変換する手法である。自分のスキーマに合った正確な SQL を LLM に作らせるのは難しい。
- オープンソースの RAG フレームワーク Vanna は、DDL とサンプル SQL を埋め込みにしてから自然言語で質問させる。text-to-SQL 専用の LLM である NSQL の評価も勧めている。

### 8. Tracking health over debt

- 技術的負債だけを追うのではなく、システムの健全性の評価を他の SLO と同じように扱い、それに基づいて改善の優先順位を決める。
- 最も影響の大きい問題に資源を割けるので長期の保守費用が下がり、技術者と非技術者の間でシステムの状態について共通理解ができる。

## Assess

### 9. AI team assistants

- GitHub Copilot のような AI コーディング支援は個人の作業の強化として語られがちだが、ソフトウェアの提供はチーム作業である。孤立した「10 倍エンジニア」ではなく「10 倍チーム」を作る AI のチーム支援を探るべきである。
- 標準化したプロンプトで、ユーザーストーリーの書き方や脅威モデリングなどチームで合意した手法を使えるようにし、RAG で組織のガイドラインや業界知識をその場で提供する。

### 10. Graph analysis for LLM-backed chats

- LLM を使うチャットボットでは会話がさまざまな方向に進むため、利用者が実際にどう会話しているかを理解するのが難しい。
- 購入や問題解決など目的のあるチャットは、望ましい状態機械として表せる。全会話をグラフに読み込み、実際のパターンと期待する状態機械とのずれを分析して、バグや改善の機会を見つける。

### 11. LLM-backed ChatOps

- Slack などのチャットから、自然言語でソフトウェアのビルド・デプロイ・運用を行う LLM の応用である。基盤サービスを見つけやすく使いやすくできる可能性がある。
- 初期の例に PromptOps と Kubiya がある。本番環境に近づける前に十分評価すべきである。

### 12. LLM-powered autonomous agents

- Autogen や CrewAI などのフレームワークの登場で、単一エージェントや固定的なマルチエージェントを超えて発展している。役割を決めたエージェントにタスクを割り当て、委任や会話で協力させられる。
- AutoGPT のように、各エージェントはタスクを分解し、ツールを使い、人に入力を求めることができる。まだ初期段階だが、急速に発展している。

### 13. Using GenAI to understand legacy codebases

- 文書が無い、または古いレガシーコードベースの理解に生成 AI を使う。Driver AI や bloop は、コード検索と LLM を組み合わせた RAG でコードベースの道案内をする。
- コンテキストウィンドウが大きくなれば、大規模なコードベースにも使いやすくなる。メインフレームの近代化で、既存コードを理解して要件に落とすリバースエンジニアを支援する用途も有望である。

### 14. VISS

- Zoom がオープンソース化した脆弱性影響評価システム (Vulnerability Impact Scoring System) である。
- CVSS のように最悪の場合に注目するのではなく、防御側の視点から影響をより客観的に測る。プラットフォーム、インフラ、データの観点で、影響を受けるテナント数などのパラメーターから点数を出す。業界と文脈に合わせて優先度を決める評価方法は実践する価値がある。

## Hold

### 15. Broad integration tests

- 実行時の依存関係をすべて本物で動かす広い統合テストに、過剰に投資している組織が多い。完全な試験環境が要り、依存のバージョン調整でリリースが遅れ、テストは壊れやすく、失敗の原因も特定しにくい。
- 代わりに 2 段階で確かめる: サービス仮想化で依存の応答を固定してシステムの振る舞いを確かめ、契約テストで実際の依存がその前提を満たすかを確かめる。

### 16. Overenthusiastic LLM use

- LLM は複雑な問題を手軽に解けるように見えるため、だいたい動いた時点で LLM の解決策を出して次に進みたくなる。
- 感情分析や内容の分類など、LLM で解ける多くの問題は、従来の NLP でより安く簡単に解ける。LLM が本当に最終的な解決策として適切かを見極める。

### 17. Rush to fine-tune LLMs

- 製品やドメイン、組織の知識を LLM に反映させようとして、ファインチューニングに走る例が多い。
- 特定の知識や事実、組織のコードベースを LLM アプリケーションに知らせたいだけなら、ほとんどの場合 RAG のほうが良く、費用対効果も高い。
- ファインチューニングは計算資源と専門知識を多く必要とし、機密データの扱いの問題も大きい。データ不足による学習不足や、過学習の危険もある。

### 18. Web components for SSR web apps

- Next.js や htmx の普及でサーバーサイドレンダリング (SSR) が増えたが、ブラウザーの技術である Web Components をサーバーで使うのは簡単ではない。
- 開発の手間が増えるだけでなく、ブラウザーでの読み込みとハイドレーションで表示が遅れ、スタイルのない一瞬の表示やレイアウトのずれがほぼ避けられない。フレームワークが対応していても、SSR の Web アプリでの使用は避けるよう勧めている。

## See also

- [Thoughtworks Technology Radar Vol.30 の全体像と 4 つのテーマ](/references/ai/thoughtworks-technology-radar-vol-30/thoughtworks-radar-vol-30-overview.md)
- [Thoughtworks Technology Radar Vol.30: Tools](/references/ai/thoughtworks-technology-radar-vol-30/thoughtworks-radar-vol-30-tools.md)
- [Thoughtworks Technology Radar Vol.35: Techniques](/references/ai/thoughtworks-technology-radar-vol-35/thoughtworks-radar-vol-35-techniques.md)
