---
type: reference
title: 'Thoughtworks Technology Radar Vol.31: Techniques'
description: 'Thoughtworks Technology Radar Vol.31 (2024 年 10 月) の Techniques 象限 23 項目の要約で、RAG や継続的デプロイなどの定番、LLM の関数呼び出し・評価・構造化出力の手法、AI 生成コードへの慢心などのアンチパターンをリングごとにまとめる。'
tags: [ai, thoughtworks, technology-radar, llm, rag, testing, continuous-delivery]
status: stable
verified: { by: claude-code/claude-opus-5-5, at: 2026-11-26T00:00:00Z }
stale_after: 2027-11-26T00:00:00Z
---

# Thoughtworks Technology Radar Vol.31: Techniques

Thoughtworks Technology Radar Vol.31 (2024 年 10 月) の Techniques (手法) 象限の要約である。
LLM を使ったアプリケーションの作り方 (RAG、関数呼び出し、評価、構造化出力) と、AI コーディング支援に伴うアンチパターンが多く並ぶ。
リングの意味と今号のテーマは [全体像の文書](/references/ai/thoughtworks-technology-radar-vol-31/thoughtworks-radar-vol-31-overview.md) を参照する。

- 出典: Thoughtworks Technology Radar Volume 31 (PDF)、[thoughtworks.com/radar](https://www.thoughtworks.com/radar)

[TOC]

## Adopt

### 1. 1% canary

- 新機能を、利用者の分類をまたいで慎重に選んだごく一部 (例えば 1%) にだけ先に出す。速い反応を得て、性能や安定性への影響を見て対応できる。
- モバイルアプリや、エッジ機器・ソフトウェア定義車両の群れへの更新で特に重要である。大規模な展開の危険を抑えるため、少数から始めることを必須と考えている。

### 2. Component testing

- フロントエンドのテストでは、テストピラミッドかトロフィー型かに関わらず、安定して速く走るコンポーネントテストに重点を置くべきである。
- 実際には、ブラウザーでの E2E テストと、非常に狭い単体テストに偏るチームが多い。単体テストは内部の機能を外に出させがちで、ブラウザーのテストは遅く不安定でデバッグしにくい。
- jsdom などでメモリ上でコンポーネントテストを多く回す。Playwright は E2E には使うが、コンポーネントテストには使わない。

### 3. Continuous deployment

- 自動テストを通ったすべての変更を自動で本番に出す。速いフィードバックと価値の早い提供を可能にする。
- いつでもデプロイできればよい継続的デリバリーとは違い、すべての変更を実際に本番に出す。
- 成熟度が要るため以前は Adopt を見送っていたが、Valentina Servile の本「Continuous Deployment」が組織での導入の道筋を示したため Adopt にした。

### 4. Retrieval-augmented generation (RAG)

- LLM の回答の質を上げるための第一の選択肢である。信頼できる文書をデータベースに置き、プロンプトに関係する文書を取ってきて文脈として足す。幻覚が大きく減る。
- コンテキストウィンドウは大きくなったが、関係の深い文書を選ぶことは今も重要である。小さく丁寧に作った文脈のほうが、大きな文脈より良い結果を出すことが多く、速くて安い。
- ベクトル検索だけでなく、再ランキング、ハイブリッド検索、LLM で作った知識グラフを使う GraphRAG も使われている。

## Trial

### 5. Domain storytelling

- 業務の専門家に業務の流れを語ってもらい、ファシリテーターが絵文字のような図式言語で登場人物と動作の関係を描き取る手法である。
- ドメイン駆動設計 (DDD) の最初のドメインモデルを作る助けになる。Event Storming の代わりにも、補完にも使える。

### 6. Fine-tuning embedding models

- RAG では埋め込みの質が検索と回答の質を直接左右する。埋め込みモデルを特定のタスクや領域に合わせて微調整すると、精度と関連性が上がる。
- 正確な情報抽出が重要な領域特化の LLM アプリで使った。ただし急いで微調整する前に、得失を考える。

### 7. Function calling with LLMs

- 質問と関数の説明から、LLM が適切な関数・API・ツールを選んで呼び出す。情報の取得、コードの実行、API の操作など、文章生成を超えた行動ができる。
- 生成に決定性と事実性を加える。RAG やエージェントの構成の中に収まる、抽象的な使い方のパターンとして見るべきである。

### 8. LLM as a judge

- 別のシステム (それ自体 LLM のこともある) の回答を、LLM に評価させる。商品検索の結果の関連性や、チャットボットが利用者を正しく導いているかの評価に使われた。
- 評価役の LLM は慎重に設定し、調整する必要がある。効率と費用の面で大きな利点がある。

### 9. Passkeys

- FIDO アライアンスが主導し、Apple、Google、Microsoft が支える認証方式で、一般的に使える段階に近づいた。
- 登録時に鍵の組を作り、サイトは公開鍵だけを受け取り、秘密鍵は利用者の端末から出ない。生体認証か PIN で守られ、各社のパスワード管理で同期できる。
- 技術に詳しくない人には難しいという反対は自滅的である。パスワードの管理が弱い人ほど恩恵が大きい。

### 10. Small language models

- LLM は大きいため、遅く高く、第三者のクラウドに置く必要がある。これに対し、パラメーター数が 35 億〜100 億程度の小さな言語モデル (SLM) への関心が高まっている。
- 正しく設定すれば、適した場面で LLM と同等以上の性能を出す研究もある。エッジ機器で動かせる。Gemini Nano や Phi-3 などがある。

### 11. Synthetic data for testing and training models

- 機密データや入手しにくいデータに頼らず、現実を模した人工データを作る。非構造データでの利用が再び増えている。
- Bonito や AgentInstruct は、文書やコードから LLM の指示調整用データを作れる。SMOTE や GAN は、不正検知などで少ないクラスのデータを補う。

### 12. Using GenAI to understand legacy codebases

- 文書が古いか誤っているレガシーのコードベースの理解に、生成 AI を使う。メインフレームの刷新のためのリバースエンジニアリングで成功した。
- 特に有望なのは、コードベースの知識グラフに対して検索する RAG である。知識グラフはコードの文字列からは得にくい構造の情報を保ち、文書や業務知識で補強できる。

## Assess

### 13. AI team assistants

- AI コーディング支援は個人の作業の話になりがちだが、ソフトウェア開発はチームの仕事である。10 倍の個人の集まりではなく、10 倍のチームを作る AI 支援を探すべきである。
- Unblocked はチームの知識源を集めて道具に統合し、Atlassian の Rovo は協働の基盤に AI を入れる。Thoughtworks も Haiven というチーム支援をオープンソースにした。

### 14. Dynamic few-shot prompting

- few-shot プロンプトの例を、利用者の質問に近いものから動的に選んで入れる。限られたコンテキストを有効に使い、トークンを減らせる。
- scikit-llm は最近傍探索でこれを実装している。SQL 生成の vanna もこの手法で精度を上げている。

### 15. GraphQL for data products

- データプロダクトの出力ポートとして GraphQL を使う。利用者はスキーマからデータの形と関係を発見でき、慣れた道具で使える。
- LLM が利用者の質問とスキーマから GraphQL クエリを作る「データと対話する」用途で試している。

### 16. LLM-powered autonomous agents

- Autogen や CrewAI などにより、役割を持つ複数のエージェントが会話しながら複雑な作業を分担する形が広がっている。
- まだ初期段階で、無限ループや制御できない振る舞いが起きた。LangGraph はフローをグラフで定義して制御しやすくする。タイムアウトや人の監督などの安全装置を入れる。

### 17. Observability 2.0

- ばらばらの監視ツールから、構造化された高カーディナリティのイベントデータを 1 つのデータストアに置く統一的な方法への移行である。
- 生のイベントを詳しいメタデータとともに保存し、相関の分析や事後調査をしやすくする。

### 18. On-device LLM inference

- LLM をブラウザーやスマートフォン、ノート PC で動かす。機密データをクラウドに送らず、遅延が小さく、費用が減り、オフラインでも動く。
- Apple シリコン向けの MLX、ブラウザーで動く Transformers.js、WebGPU を使う Chatty などがある。

### 19. Structured output from LLMs

- LLM の回答を決められたスキーマに収める。指示で形式を求める方法と、JSON などを出すように微調整する方法がある。OpenAI は JSON Schema などで出力を縛れるようになった。
- 関数呼び出しや API 連携など、形式の正確さが重要な場面で価値が高い。幻覚を減らす効果も示されている。

## Hold

### 20. Complacency with AI-generated code

- GitHub Copilot などの AI コーディング支援は広く使われているが、中長期のコード品質への影響を懸念している。何度か良い経験をすると、AI の提案のレビューが甘くなりやすい。
- コードベースの肥大化やプルリクエストの大型化を示す調査がある。自動化バイアス、サンクコスト、アンカリング、レビュー疲れに注意し、AI を使わない場面・信じない場面の判断基準を持つ。

### 21. Enterprise-wide integration test environments

- 全社共通の結合テスト環境は、複製しにくい貴重な資源になり開発のボトルネックになる、無駄の多い慣習である。データや設定の差で誤った安心感も生む。
- 一時的な環境と、チームが所有する安く作って捨てられるテスト一式を使い、依存先は偽のスタブで置き換える。契約テストや本番でのテストなども併用する。

### 22. LLM bans

- 職場で LLM を全面禁止するのではなく、承認した AI ツールを使えるようにすべきである。禁止すると、従業員は承認されていない危険な回避策に流れる。
- 安全な企業向けの LLM を用意すれば、プライバシー、セキュリティ、コンプライアンス、費用を管理しつつ、組織として AI の使い方を学べる。

### 23. Replacing pair programming with AI

- コーディング支援はペアプログラミングの利点の一部をもたらすが、ペアプログラミングを AI で完全に置き換えることには反対する。
- ペアの大きな利点は個人ではなくチームを良くすることであり、仕掛かりの削減、引き継ぎの削減、継続的インテグレーション、コードの共同所有などは AI では得られない。

## See also

- [Thoughtworks Technology Radar Vol.31 の全体像と 4 つのテーマ](/references/ai/thoughtworks-technology-radar-vol-31/thoughtworks-radar-vol-31-overview.md)
- [Thoughtworks Technology Radar Vol.31: Tools](/references/ai/thoughtworks-technology-radar-vol-31/thoughtworks-radar-vol-31-tools.md)
- [Thoughtworks Technology Radar Vol.31: Languages and frameworks](/references/ai/thoughtworks-technology-radar-vol-31/thoughtworks-radar-vol-31-languages-and-frameworks.md)
