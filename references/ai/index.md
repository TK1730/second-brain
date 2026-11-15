# AI・エージェント

- [AI エージェントに好かれるコードベースの作り方](aihero-codebases-ai-agents-love.md) - Matt Pocock の記事「How To Make Codebases AI Agents Love」の要約。Deep Module でコードベースを AI が辿りやすく検証しやすい形にする考え方。
- [効果的なエージェント自動化の作り方](claude-blog-building-effective-agent-automations.md) - Claude ブログの記事「Building effective agent automations」の要約で、定期実行で情報源を読み、前回からの変化をまとめて投稿するエージェントを Claude Managed Agents で作るときの失敗パターンと対策をまとめる。
- [Claude Code チームのコードレビューの進め方](claude-blog-claude-code-team-code-review.md) - claude.dev ブログの記事「How the Claude Code team does code review」の要約で、エージェントがコードの大半を書く状況において、人の時間を節約しつつ差し戻しを増やさないレビューの仕組みを説明する。
- [コンテキストエンジニアリング: メモリ・コンパクション・ツール結果のクリア](claude-cookbook-context-engineering-tools.md) - Claude Cookbook の「Context engineering: memory, compaction, and tool clearing」の要約で、長く動くエージェントのコンテキストを抑える 3 つの手段の違いと使い分けをまとめる。
- [Claude Managed Agents のドリーム（Dreams）](claude-docs-managed-agents-dreams.md) - 過去のセッションからメモリストアを整理・再構築する Managed Agents のドリーム機能の要約。
- [Claude Managed Agents の概要](claude-docs-managed-agents-overview.md) - Anthropic が提供するエージェント実行基盤 Claude Managed Agents の概要。
- [長時間動くエージェントのための効果的なハーネス](claude-engineering-effective-harnesses-for-long-running-agents.md) - Anthropic のエンジニアリングブログの記事「Effective harnesses for long-running agents」の要約で、記憶を持たないセッションをまたいでエージェントに開発を続けさせるための、初期化エージェントとコーディングエージェントの 2 段構成と、状態を引き継ぐファイルを説明する。
- [autonomous-coding のコーディング用プロンプト](claude-quickstarts-autonomous-coding-coding-prompt.md) - claude-quickstarts の autonomous-coding で、2 回目以降の毎セッションに送るプロンプト coding_prompt.md の要約で、記憶のない状態から状況をつかみ、1 機能を実装してブラウザで確かめ、きれいな状態で終えるまでの 10 段階の手順と、その書き方の工夫を説明する。
- [autonomous-coding の要約](claude-quickstarts-autonomous-coding.md) - Anthropic の claude-quickstarts リポジトリにある autonomous-coding の要約で、初期化エージェントとコーディングエージェントの 2 段構成で、何セッションもかけてアプリを作らせる最小のハーネスの仕組みと、Bash コマンドを許可リストで絞る安全対策を説明する。
- [モデルと働く人間のための「もっと野心的になる」方法](felixrieseberg-how-to-be-more-ambitious.md) - Felix Rieseberg の記事「How to be more ambitious: A tutorial for humans with models」の要約で、AI モデルへの頼み方を Altitude・Depth・Range の 3 方向に広げる方法を説明する。
- [Harness² の要約](google-research-harness2.md) - Google Research が公開した、エージェントのハーネスを再帰的に改良するフレームワーク Harness²（google-research/harness2）の要約。
- [エージェントの各ステップを見張らずに済ませるループとグラフ](hanakoxbt-loops-and-graphs.md) - Hanako（@hanakoxbt）の X 記事「Loops and Graphs」の要約で、作業単位を正しくするループと作業の形を決めるグラフを分け、人間の承認を最後の 1 ステップだけにする設計を説明する。
- [Claude Opus 5.5 を最小コストで最大品質に使う設定ガイド](zodchiii-claude-opus-5-5-setup-guide.md) - darkzodchi（@zodchiii）の X 記事「The Claude Opus 5.5 Setup Guide」の要約で、Opus 5 からの移行で費用を増やさないための effort・キャッシュ・API 変更点・プロンプトの設定をまとめる。
