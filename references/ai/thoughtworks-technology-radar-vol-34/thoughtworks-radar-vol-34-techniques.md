---
type: reference
title: 'Thoughtworks Technology Radar Vol.34: Techniques'
description: 'Thoughtworks Technology Radar Vol.34 (2026 年 4 月) の Techniques 象限 41 項目の要約で、コンテキストエンジニアリング、共有の指示、エージェントのサンドボックスとフィードバックの仕組み、避けるべきアンチパターンをリングごとにまとめる。'
tags: [ai, thoughtworks, technology-radar, context-engineering, coding-agent, harness-engineering, security]
status: stable
verified: { by: claude-code/claude-opus-5-5, at: 2026-11-26T00:00:00Z }
stale_after: 2027-11-26T00:00:00Z
---

# Thoughtworks Technology Radar Vol.34: Techniques

Thoughtworks Technology Radar Vol.34 (2026 年 4 月) の Techniques (手法) 象限の要約である。
41 項目の多くは、コーディングエージェントにどう情報を与え、どう縛り、どう結果を確かめるかに関するものである。
リングの意味と今号のテーマは [全体像の文書](/references/ai/thoughtworks-technology-radar-vol-34/thoughtworks-radar-vol-34-overview.md) を参照する。

- 出典: Thoughtworks Technology Radar Volume 34 (PDF)、[thoughtworks.com/radar](https://www.thoughtworks.com/radar)

[TOC]

## Adopt

### 1. Context engineering

- プロンプトの言い回しではなく、コンテキストウィンドウを設計の対象として扱い、AI に渡す情報の環境を意図して組み立てる。最適化の小技から、AI システムの基礎となる設計上の関心事になった。
- 生のデータを大きなコンテキストに詰め込むと、コンテキストの劣化 (context rot) で推論が悪くなる。最初は軽い索引だけを渡し、必要なものだけを引き込む progressive context disclosure へ移っている。
- 成熟しつつある手段: プロンプトキャッシュで静的な指示を先に置く、必要な MCP サーバーやツールだけを読み込む動的な取得、方針や例外を構造化する context graph、状態付きの圧縮やサブエージェントによる要約。

### 2. Curated shared instructions for software teams

- 各開発者が一からプロンプトを書くのはアンチパターンになりつつある。AI への指示を、個人の作業ではなくチームで育てる成果物として扱う。
- CLAUDE.md、AGENTS.md、`.cursorrules` などを、新しいサービスを作る雛形のリポジトリに入れておくと、雛形が指示の配布手段になる。
- 関連して、動いてコンパイルできる参照アプリケーションを正とし、そこに指示も埋め込んで、新しいリポジトリが最新の規約を受け継ぐ方法も議論した。

### 3. DORA metrics

- 変更のリードタイム、デプロイ頻度、平均復旧時間 (MTTR)、変更失敗率に、新しく手戻り率 (rework rate) を加えた指標である。手戻り率は、完了したはずの作業を直すために使われた割合を測る。
- AI 支援の開発では、生成されたコード行数ではなく、デリバリーの流れと安定性に改善が表れるかを見るべきである。安定性の指標の悪化は、見落としや技術的負債の早い警告になる。
- 複雑なダッシュボードを作るより、ふりかえりでの確認のような単純な仕組みのほうが改善に効く。

### 4. Passkeys

- FIDO Alliance が主導し、Apple、Google、Microsoft が支える、パスワードに代わる FIDO2 の認証情報である。秘密鍵は端末の安全な領域に保存され、生体認証や PIN で守られ、外に出ない。
- 認証情報はドメインに結び付くため、偽サイトには何も渡らず、構造的にフィッシングに強い。NIST SP 800-63-4 は同期型のパスキーを AAL2 準拠とした。
- 新しい認証実装の既定の出発点にしている。アカウント復旧の経路に SMS OTP のようなフィッシング可能な手段を残さないこと。

### 5. Structured output from LLMs

- モデルの応答を JSON など決められた形式に制約する手法である。LLM の応答をプログラムで扱うアプリケーションの既定とした。
- 主要な提供者はすべてネイティブに対応したが、対応する JSON Schema の範囲は違い、API も変わり続けている。Instructor や Pydantic AI で提供者間の差を吸収し、自前のモデルでは Outlines を使うことを勧める。

### 6. Zero trust architecture

- エージェントの時代でも、「決して信頼せず、常に確かめる」、ID に基づくセキュリティ、最小権限の原則を、エージェントを動かす前提として扱う。
- エージェントに SPIFFE を適用して強い ID を与え、振る舞いを継続的に監視する。CI/CD でも長期の静的な鍵を、ID を確かめた後に発行される短命のトークンに置き換えている。

## Trial

### 7. Agent Skills

- 指示、実行スクリプト、関連資料をまとめてコンテキストを部品にするオープン標準である。エージェントは説明文をもとに必要なときだけスキルを読み込むので、トークン消費と agent instruction bloat を抑えられる。
- コーディングエージェントだけでなく、OpenClaw のような個人アシスタントでも急速に広まった。多くの用途はローカルの CLI やスクリプトを指せば足りるため、MCP を既定にしない動きの一因にもなっている。
- 第三者のスキルをレビューせずに使うことは、サプライチェーンの大きなリスクになる。

### 8. Browser-based component testing

- 以前は遅く不安定だったため勧めなかったが、Playwright などで実際のブラウザーで動かすコンポーネントテストは、今では有力で多くの場合に望ましい選択肢になった。
- 実行環境と同じ条件で試せ、速度の低下も小さく、jsdom のような模擬環境より価値がある。

### 9. Feedback sensors for coding agents

- コンパイラ、linter、構造テスト、テストスイートなどの決定的な品質ゲートを、エージェントのワークフローに組み込み、失敗をきっかけにエージェントが自分で直せるようにする。人が毎回指示する手間が減る。
- チェックを動かすレビュー役のエージェントを置く方法や、並行して動くプロセスからエージェントが結果を問い合わせる方法がある。
- コミット後ではなく、コーディングの最中に動かし、コミット前に問題がない状態にするのが望ましい。

### 10. Mapping code smells to refactoring techniques

- 特定のコードの臭いに対し、決めたリファクタリングの手法で対処するようエージェントに指示する。一般的なものは書籍『Refactoring』を参照させ、独自のものは Agent Skills や AGENTS.md で対応づける。
- linter と組み合わせると、臭いを検出したときに適切な手法を起動する決定的なフィードバックになる。学習データが少ない古い技術 (.NET Framework 2.0、Java 8 など) や、独自の規約を持つチームで特に効く。

### 11. Mutation testing

- コードにわざとバグ (変異) を入れ、テストが失敗するかを確かめて、テストの本当の検出力を測る。カバレッジはどの行が実行されたかしか示さない。
- AI が生成したテストには、ロジックが変わっても通り続ける「常に緑」のテストが紛れやすい。Stryker、Pitest、cargo-mutants などでそれを見つける。

### 12. Progressive context disclosure

- 最初に指示を全部渡さず、まず軽い探索の段階で必要なものを選ばせ、関係するときだけ詳しい情報を読み込ませる。コンテキストエンジニアリングの一手法である。
- RAG で領域を特定してから詳しい指示とデータを取る使い方や、Agent Skills の読み込みに使われる。「〜せよ」「〜するな」を積み上げる指示の肥大化を避けられる。

### 13. Sandboxed execution for coding agents

- ファイルアクセス、ネットワーク、資源を制限した隔離環境でコーディングエージェントを動かす。偶発的な破壊や認証情報の漏洩を防ぐため、任意ではなく既定とすべきである。
- 選択肢は幅広い: エージェント組み込みのサンドボックス、Dev Containers、毎回作り直す microVM の Shuru、チェックポイントと復元を持つ Sprites、Linux の Bubblewrap、macOS の sandbox-exec。
- ビルドとテストに必要なもの、GitHub やモデル提供者への安全な認証、ポート転送、十分な CPU とメモリも要る。使い捨てにするか永続させるかは、セキュリティ、費用、作業の継続性から決める。

### 14. Semantic layer

- データストアと、BI、AI エージェント、API などの利用側の間に、指標の定義、結合、アクセス規則、業務用語を集めた共通の層を置く。
- これがないと業務ロジックが散らばり、指標の定義が少しずつずれる。LLM による素朴な text-to-SQL は、スキーマの外にある業務ルールを知らないため誤りやすい。
- Snowflake の Semantic Views、Databricks の Metric Views、dbt MetricFlow、Cube がある。Open Semantic Interchange (OSI) v1.0 で標準化も進んでいる。全社一斉ではなく 1 つの領域から始める。

### 15. Server-driven UI

- 画面の構造とデータをサーバーから送り、アプリ側は汎用の描画の器にする。モバイルでストアの審査を毎回待たずに変更を届けられる。
- 以前は設定過多の混乱を招くと注意したが、Airbnb や Lyft などから安定した型が出てきた。変化の激しい部分に絞って使い、何でも詰め込んだ巨大なプロトコルにしないこと。

## Assess

### 16. Agentic reinforcement learning environments

- コンテキスト、ツール、フィードバックを組み合わせ、LLM エージェントが多段のタスクをこなす訓練場である。行動ごとに報酬や罰を与え、推論やツール利用を学ばせる。RLVR などで報酬を検証可能でごまかしにくくする。
- Cursor の Composer はその例である。Environments Hub、Agent Lightning、NVIDIA NeMo Gym など、構築を助ける基盤も出てきている。

### 17. Architecture drift reduction with LLMs

- エージェントは劣化したパターンも真似るため、設計からのずれが加速する。Spectral、ArchUnit、Spring Modulith などの決定的な解析と LLM の評価を組み合わせ、構造と意味の違反を見つけて直す。
- 最初は違反が大量に出るので優先順位を付ける。修正は小さく保ち、改善になったかを確かめる検証ループを置く。OpenAI のチームはこれを「ガベージコレクション」と呼んでいる。

### 18. Code intelligence as agentic tooling

- LLM はコードを文字の列として扱い、呼び出し関係や型の階層を知らない。そのためテキスト検索に頼り、構文木 (AST) にある情報の再構築にトークンを使う。
- LSP などで AST を理解する道具をエージェントに与え、「この記号の参照をすべて探す」「この型を一括で改名する」を直接の操作にする。OpenRewrite のようなコード変換の道具も使える。
- Claude Code や OpenCode はローカルの LSP サーバーと連携でき、JetBrains の MCP サーバーや Serena MCP サーバーもある。

### 19. Context graph

- 決定、方針、例外、前例、根拠、結果をグラフのノードとして結び、AI が使える形にする。記録システムが「何が起きたか」を持つのに対し、「なぜか」を持つ。
- 例えば値引きの例外が恒常的な方針か一度きりの特例かを、エージェントが判断できるようになる。GraphRAG と違い、各辺に有効期間を持ち、古い事実を上書きではなく無効にする。

### 20. Feedback flywheel

- 仕様 → 計画 → 実装の流れに、コーディングエージェントのハーネスを改善する段階を加える。ふりかえりのように、セッションでの成功と失敗を記録し、次のセッションの予測可能性を上げる。
- 人が共有の指示やフィードバックセンサーを改善する。エージェント自身が改善を決める段階もありうるが、今はコンテキストの劣化やノイズを避けるため人が要る。新しいモデルを入れたときにハーネス全体を見直すのにも使える。

### 21. HTML Tools

- エージェントで作った小さな道具を、1 つの HTML ファイルとして配る方法である。ブラウザーで直接動かせ、どこにでも置け、ファイルを渡すだけで共有できる。
- CLI のようにバイナリやパッケージマネージャーで配る手間がなく、Web アプリのような専用のホスティングも要らない。ブラウザーのサンドボックスとソースを読めることが多少の安全策になる。

### 22. LLM evaluation using semantic entropy

- 作り話 (confabulation) を見つけるため、同じ入力に対する複数の出力の、表面の言葉ではなく意味のばらつきを測る。
- 事前知識なしにさまざまなタスクに使え、単純なエントロピーより誤った主張をうまく見分ける。

### 23. Measuring collaboration quality with coding agents

- 出力までの時間や生成行数ではなく、人とエージェントの協働の質を測る。初回の受け入れ率、タスクあたりの往復回数、マージ後の手戻り、ビルドの失敗、レビューの負担などである。
- Claude Code の `/insights` コマンドでセッションをふりかえる報告を作れる。個人ではなくチーム単位で、DORA 指標と並べて追う。

### 24. MITRE ATLAS

- AI・機械学習システムを狙う攻撃の戦術と手法の知識ベースである。MITRE ATT&CK を補う。
- 共通の語彙がないとリスクは見落とされたり形だけのチェックになったりする。脅威モデリングの支えとして、SAIF などの管理策の枠組みと組み合わせて使う。

### 25. Ralph loop

- 固定のプロンプトをエージェントに無限ループで与える手法である (Wiggum loop とも呼ばれる)。毎回新しいコンテキストで始め、仕様から 1 タスクを選んで実装し、また最初に戻る。
- 複数エージェントを組織するより単純で、繰り返すうちにコードが仕様に近づくことを期待する。コンテキストの劣化を避けられるが、トークンの費用は大きい。goose などが実装している。

### 26. Reverse engineering for design system

- ばらばらの既存画面、販促物、スクリーンショットしかない状態から、マルチモーダル LLM で色、文字、余白などのデザイントークンと、繰り返し出てくる部品を抽出し、デザインシステムを組み立てる。
- Figma と組み合わせると部品ライブラリ作りが速くなる。全面的な作り直しの前の、最初の基準作りとして実用的である。

### 27. Role-based contextual isolation in RAG

- アクセス制御を、アプリケーション層ではなく検索の層で行う。索引を作るときに各チャンクに権限を付け、問い合わせ時に利用者の ID で検索範囲を絞る。
- 権限のない情報はそもそもモデルに届かない。Milvus などメタデータでの絞り込みが速いベクトルデータベースが増え、実用的になった。

### 28. Skills as executable onboarding documentation

- スキルを「実行できるオンボーディング文書」として使う。リポジトリでは `/_setup` スキルが README とセットアップスクリプトの役を兼ね、スクリプトにできない手順は LLM が状況を見て進める。
- ライブラリや API の提供者が利用者向けにスキルを配ったり、社内基盤やデザインシステムの導入を楽にしたりする使い方もある。静的な文書より、古くなったことに早く気づける。

### 29. Small language models

- 小さな言語モデル (SLM) は、特定の用途で LLM より費用あたりの賢さが高くなりつつある。要約や簡単なコーディングでは古い LLM と競える。
- Phi-4-mini、Ministral 3 3B、Qwen3-0.6B、Gemma-3-270M などがある。古い LLM で足りていたエージェントの用途では、低コスト・低遅延の代替として検討する。

### 30. Team of coding agents

- 開発者が、役割を持つ少数のエージェントを組織して 1 つのタスクに取り組ませる。サブエージェントは多くの道具の標準機能になり、Claude Code にはエージェントチームの機能も入った。
- オーケストレーターが順序と並列化を受け持ち、エージェント同士も通信できるのが望ましい。少数の意図したチームと、大規模な swarm は区別すべきである。

### 31. Temporal fakes

- 外部の依存先を、状態機械と時間の変化まで再現した高精度の模擬環境として作る。固定の応答を返すモックとは違う。コーディングエージェントで作る手間が下がった。
- GPU データセンターの可観測性を作ったチームは、NVIDIA DCGM や InfiniBand の模擬を Go で作り、過熱による性能制限などの障害を MCP サーバー経由でエージェントに注入させ、警報やダッシュボードを確かめた。
- 模擬が現実からずれると、誤った安心を生む。

### 32. Toxic flow analysis for AI

- 非公開データへのアクセス、信頼できない内容への接触、外部との通信の 3 つが揃うと、プロンプトインジェクションやツールの汚染の危険が生じる。システム内の危険なデータの通り道を特定する分析である。
- MCP だけでなく、隠れた指示で機密を持ち出す悪意あるスキルにも同じ危険がある。Agent Scan などの道具を使う。

### 33. Vision language models for end-to-end document parsing

- レイアウト検出、OCR、後処理を重ねる従来の文書解析を、文書の画像を 1 つの入力として扱う視覚言語モデル (VLM) で置き換える。olmOCR-2、DeepSeek-OCR、PaddleOCR-VL などがある。
- 構成は単純になるが、生成モデルなので作り話をすることがある。誤りが許されない用途では、決定的な OCR との組み合わせが要る。

## Caution

### 34. Agent instruction bloat

- AGENTS.md や CLAUDE.md は、概要、設計の説明、規約、ルールが足されて長くなり、互いに矛盾し始める。モデルは長い文脈の中ほどを見落としやすく、重要なルールが無視されやすくなる。
- AI に AGENTS.md を生成させるより、人が書いたほうが効果が高いという研究もある。必要に応じて足し、最小で一貫した形へ磨き続ける。progressive context disclosure も使う。

### 35. AI-accelerated shadow IT

- AI でコードを書かない人も複雑な仕組みを作れるようになった。Claude Cowork のような道具も増えている。統制のないエージェントのワークフローは、セキュリティのリスクと、似た解決策の乱立を招く。
- 使い捨ての作業と、本番品質が要る重要な業務を見分けることが鍵である。計測できる社内のサンドボックスと、既存のワークフローの共有カタログを用意し、広く使われたものに投資する。

### 36. Codebase cognitive debt

- システムの実装と、チームが「どう動き、なぜそうなっているか」を共有して理解している状態との差が広がることである。AI で変更の速度が上がると、設計意図や隠れた結合を見失う。
- 理解が弱まるとエージェントを適切に導けなくなり、小さな変更で予期しない障害が起きる段階に至る。フィードバックセンサー、チームの認知負荷の追跡、アーキテクチャの適応度関数で対抗する。

### 37. Coding agent swarms

- 数十から数百のエージェントを、AI が構成と規模を動的に決めて問題に投入する。Gas Town や Ruflo が例である。階層的な役割、作業の台帳 (Gas Town は Beads を使う)、並列作業の衝突を解消する仕組みといった型が出てきた。
- Anthropic の C コンパイラ生成や Cursor のブラウザー作成の実験は、詳細な仕様や包括的なテストがある題材を選んでいた。通常の製品開発とは条件が違い、費用も高く未成熟である。

### 38. Coding throughput as a measure of productivity

- 生成した行数やプルリクエストの数を成功の指標にすると、行動が歪み、整合しないコードがあふれてレビューが遅れ、セキュリティのリスクも増える。
- AI の出力が手直しなしで使えた割合 (初回の受け入れ率) のほうが意味のある先行指標である。DORA 指標ともつながる。

### 39. Ignoring durability in agent workflows

- エージェントのワークフローで永続性を考えないことは、開発では動いても本番で失敗するアンチパターンである。LLM やツールの呼び出しは、ネットワークの断絶やサーバーの停止で失敗する。
- 何日も続く処理には、進捗とツール呼び出しを保存し、失敗後に再開できる永続実行が要る。LangGraph や Pydantic AI に組み込まれ始めており、Temporal、Restate、Golem などの基盤もある。

### 40. MCP by default

- 単純な手段で足りるのに、エージェントと外部システムの連携に MCP を既定で使うことに注意する。
- MCP は、構造化されたツールの契約、OAuth による認証の境界、統制された複数テナントでの利用には価値がある。しかし層を挟むたびに API の表現力が失われる「抽象化の税」がある。
- 良い `--help`、構造化された JSON の出力、予測できるエラーを持つ CLI なら、多くの場合エージェントに十分である。

### 41. Pixel-streamed development environments

- 開発を、VDI 型のリモートデスクトップの画面転送で行うことである。セキュリティ、標準化、オンボーディングのために採用されるが、遅延と入力の遅れが常に摩擦を生み、開発を遅く疲れるものにする。
- Google Cloud Workstations、Coder、VS Code Remote Development のように、画面ではなく計算をコードの近くに置く方法のほうがよい。強い規制上の理由がない限り既定にしない。

## See also

- [Thoughtworks Technology Radar Vol.34 の全体像と 4 つのテーマ](/references/ai/thoughtworks-technology-radar-vol-34/thoughtworks-radar-vol-34-overview.md)
- [Thoughtworks Technology Radar Vol.34: Tools](/references/ai/thoughtworks-technology-radar-vol-34/thoughtworks-radar-vol-34-tools.md)
- [Thoughtworks Technology Radar Vol.35: Techniques](/references/ai/thoughtworks-technology-radar-vol-35/thoughtworks-radar-vol-35-techniques.md)
- [コンテキストエンジニアリング: メモリ・コンパクション・ツール結果のクリア](/references/ai/claude-cookbook-context-engineering-tools.md)
