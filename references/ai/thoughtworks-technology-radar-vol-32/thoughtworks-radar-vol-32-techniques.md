---
type: reference
title: 'Thoughtworks Technology Radar Vol.32: Techniques'
description: 'Thoughtworks Technology Radar Vol.32 (2025 年 4 月) の Techniques 象限 22 項目の要約で、データプロダクト思考、ファジング、SBOM、GraphRAG やモデル蒸留などの生成 AI の手法、AI 生成コードへの慢心などの避けるべきパターンをリングごとにまとめる。'
tags: [ai, thoughtworks, technology-radar, techniques, rag, security, coding-agent]
status: stable
verified: { by: claude-code/claude-opus-5-5, at: 2026-11-26T00:00:00Z }
stale_after: 2027-11-26T00:00:00Z
---

# Thoughtworks Technology Radar Vol.32: Techniques

Thoughtworks Technology Radar Vol.32 (2025 年 4 月) の Techniques (手法) 象限の要約である。
データとセキュリティの基本的な手法に加え、生成 AI を使う手法と、AI の使い方で避けるべきパターンが並ぶ。
リングの意味と今号のテーマは [全体像の文書](/references/ai/thoughtworks-technology-radar-vol-32/thoughtworks-radar-vol-32-overview.md) を参照する。

- 出典: Thoughtworks Technology Radar Volume 32 (PDF)、[thoughtworks.com/radar](https://www.thoughtworks.com/radar)

[TOC]

## Adopt

### 1. Data product thinking

- データを、ライフサイクル、品質基準、利用者のニーズを持つ製品として扱う。データメッシュかレイクハウスかに関係なく、データ管理の既定の助言とした。
- 利用者を中心に置き、ユースケースから逆算して設計する。DataHub、Collibra、Atlan などのデータカタログで業務メタデータと技術メタデータを管理する。
- AI の取り組みを広げ、AI に使えるデータを作るのにも使う。不要になったデータを法令に沿って廃棄するところまでを管理する。

### 2. Fuzz testing

- システムにあらゆる不正な入力を与えて振る舞いを観察するテスト手法である。HTTP なら 4xx を返すべき入力で 5xx 以上が出ることがよくある。
- AI 生成コードとそれへの慢心が増えた今こそ、コードの堅牢さと安全性を保つために採用すべきとした。

### 3. Software Bill of Materials

- SBOM の生成は、2021 年の初掲載から既定の実践になった。Syft、Trivy、Snyk でソースからコンテナイメージまで生成でき、FOSSA や Chainloop で開発フローに組み込める。
- 標準は SPDX と CycloneDX が広く支持されている。英国政府や CISA の指針のとおり、AI システムにも SBOM が必要である。

### 4. Threat modeling

- 潜在的な脅威を特定・分類する手法の集まりで、生成 AI アプリケーションの固有のリスクにも当てはまる。
- 開発の最後にまとめてセキュリティを挟むのではなく、ライフサイクルを通じて定期的に行う。横断的なセキュリティ要件や自動スキャナーと組み合わせる。

## Trial

### 5. API request collection as API product artifact

- API を製品として扱うなら、OpenAPI の仕様だけでなく、すぐ動かせる例が要る。Postman、Bruno、Insomnia などのリクエスト集を API の成果物として扱う。
- 主要な流れを案内するように設計し、認証やテストデータを用意しておく。リポジトリに置き、API のリリースパイプラインに組み込んで最新に保つ。

### 6. Architecture advice process

- 誰でもアーキテクチャの判断をしてよいが、影響を受ける人と専門知識を持つ人に助言を求めることを条件にする、分散型の判断の進め方である。
- 従来のアーキテクチャレビュー委員会は流れを妨げ、組織の成果の低さと相関するという調査がある。ADR と助言の場を組み合わせ、規制の厳しい業界でも大規模に成功している。

### 7. GraphRAG

- 文書を分割して LLM で知識グラフを作り、検索時には埋め込みで見つけた断片からグラフの辺を辿って関連する断片も加える、RAG の 2 段階の手法である。
- レガシーコードの理解では、構文木や依存関係でグラフを作って効果が出た。Neo4j の GraphRAG パッケージや Graphiti などの道具が出てきた。

### 8. Just-in-time privileged access management

- 常時有効な特権 (standing privileges) は攻撃面を広げる。必要なときだけ特権を与え、終わったらすぐ取り消す。
- 軽い承認フローで一時的なロールを与え、ロールごとの有効期限 (TTL) で自動的に失効させる仕組みを作った。

### 9. Model distillation

- 大きなモデル (教師) の知識を、小さく安いモデル (生徒) に移す手法である。教師が作ったデータで生徒を微調整する。枝刈りや量子化と違い、特定分野の知識を保つことを狙う。
- DeepSeek R1 の Qwen・Llama 蒸留版が代表例である。OpenAI や Amazon Bedrock も手引きを出しており、LLM の費用を抑え、端末上での推論を可能にする。

### 10. Prompt engineering

- 推論モデルでは、few-shot が zero-shot より悪いことがあり、chain-of-thought の指示も性能を下げることがある。強化学習で思考の仕組みがすでに調整されているためと考えられる。
- それでも、ハルシネーションを減らし品質を上げるために従来の手法は役立つ。性能、応答時間、トークン費用の釣り合いでモデルを選び、プロンプトのテンプレートを磨き続ける。

### 11. Small language models

- DeepSeek R1 の完全版は 6,710 億パラメーターで巨大な GPU 構成が要るが、Qwen や Llama への蒸留版なら控えめなハードウェアで動き、従来の SLM より大きく性能が上がった。
- Llama 3.2 (1B・3B)、Phi-4 (14B)、PaliGemma 2 など、小さなモデルの公開が続いている。

### 12. Using GenAI to understand legacy codebases

- 生成 AI でレガシーコードを理解する手法が進んだ。GitHub Copilot や Sourcegraph の Cody がコードベース全体の理解を助ける。
- S3LLM のように、Fortran や Pascal の科学技術ソフトウェアを扱う枠組みも出てきた。

## Assess

### 13. AI-friendly code design

- AI が後で直すから人向けの品質は重要でないという考えは誤りで、AI のコーディング支援もよく整理されたコードのほうが良く働く。
- 意味のある命名、モジュール化と抽象化 (変更範囲と AI のコンテキストを小さく保つ)、DRY など、人に良い設計は AI にも良い。

### 14. AI-powered UI testing

- LLM で画面を解釈する UI テストである。自然言語のテストで画面を操作する道具 (QA.tech、KaneAI) や、Playwright のページ構造と組み合わせる Browser Use がある。
- 非決定的で不安定になりうるが、セレクターの無いレガシー画面や、ラベルや操作経路がよく変わる画面のテストに向く。

### 15. Competence envelope as a model for understanding system failures

- graceful extensibility の理論でいう competence envelope (システムが障害に耐えて動ける範囲) を超えると、システムはもろくなる。2024 年の Canva の障害の分析に役立つ。
- residuality theory は、わざとストレスを与えてこの範囲を試す方法を示す。

### 16. Structured output from LLMs

- LLM の応答を決めたスキーマに縛ることである。指示で形式を指定する方法と、JSON を出すよう微調整する方法がある。OpenAI は JSON Schema、pydantic、Zod で応答を縛れる。
- 関数呼び出しや外部連携で正確さを上げ、ハルシネーションも減らす。

## Hold

### 17. AI-accelerated shadow IT

- AI で、コードを書かない人が自分でソフトウェアを作って連携できるようになった。ノーコードの自動化に AI をつないで、チャットのメッセージを ERP の API 呼び出しに変えるなど、AI を応急処置のテープのように使う例が出ている。
- 統制されない、安全でない可能性のあるアプリケーションが増え、データが散らばる恐れがある。早さと長期の安定の釣り合いを考える。

### 18. Complacency with AI-generated code

- 2024 年は重複コードと手戻りが予想以上に増え、リファクタリングが減ったという調査がある。AI への信頼が批判的思考を下げるという研究もある。
- エージェントの変更が大きくなるほどレビューが難しくなる。最小限のレビューで AI に任せる「vibe coding」は試作には使えても、本番コードには強く反対する。

### 19. Local coding assistants

- コードの機密のために手元で動く AI を使いたくなるが、クラウドの大きなモデルに比べて、複雑な指示、長いコンテキスト、ツール呼び出しで大きく劣る。
- 期待を低く持って使う。IDE の 1 行補完や Qwen Coder による簡単な補完と質問、Continue と Ollama の組み合わせなど、手元で成り立つ用途はある。

### 20. Replacing pair programming with AI

- AI はペアプログラミングの一部の利点 (行き詰まりの解消、新技術の学習、オンボーディング) を与える。
- しかしペアの大きな利点はチーム全体を良くすることであり、仕掛かりの削減、引き継ぎの減少、継続的インテグレーション、コードの共同所有には役立たない。AI で完全に置き換えないこと。

### 21. Reverse ETL

- 中央の分析基盤から業務システムへデータを戻す仕組みが広がっている。集約や移行期の構成として正当な場面もある。
- しかし製品ベンダーがこれを口実に業務ロジックを自社製品に集め、中央集権型の問題を悪化させている。導入には極めて慎重になる。

### 22. SAFe™

- SAFe の標準化しすぎた段階的な工程は摩擦とサイロを生み、上からの統制が無駄を生み、チームの自律と実験を妨げる。
- 複雑な問題に簡単な解は無い。包括的な変革と組み合わせた、より軽く価値に基づく進め方を勧める。

## See also

- [Thoughtworks Technology Radar Vol.32 の全体像と 4 つのテーマ](/references/ai/thoughtworks-technology-radar-vol-32/thoughtworks-radar-vol-32-overview.md)
- [Thoughtworks Technology Radar Vol.32: Tools](/references/ai/thoughtworks-technology-radar-vol-32/thoughtworks-radar-vol-32-tools.md)
- [AI エージェントに好かれるコードベースの作り方](/references/ai/aihero-codebases-ai-agents-love.md)
