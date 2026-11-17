# エージェントの設計

- [エージェントのメモリを層で設計し、dreaming で整理する](agent-memory-components.md) - Anthropic のエンジニアリング記事に基づく、エージェントメモリの 4 層構成、dreaming、評価結果、設計上の指針の要点。
- [Asana に学ぶ、指導できるエージェントの設計](asana-human-agent-teams.md) - Asana が人とエージェントの協働で守る 4 つの設計原則と、社内での 3 つの活用例の要点。
- [ワークフローの 3 つの基本パターンと選び方](common-workflow-patterns.md) - sequential、parallel、evaluator-optimizer の使いどころ、避ける場面、トレードオフ、単一エージェントから始める選択の指針。
- [Claude Code の動的ワークフローで大規模タスクを並列に検証しながら進める](dynamic-workflows.md) - 動的ワークフローの仕組み、並列サブエージェントと反証ループ、使いどころ、提供範囲、上限と費用の要点。
- [Claude Code で評価の設計と改善の反復を自動化する](eval-design-and-hillclimbing.md) - claude-api スキルの build-eval と hillclimb で、評価を作り、過学習を避けて性能やコストを改善する手順と数値例。
- [サブエージェントをメインのエージェントループへ統合する判断と手順](folding-subagents-into-main-agent.md) - サブエージェントを残す条件、スキルとツールへの置き換え、評価を使った段階的な統合手順の要点。
- [長時間アプリ開発ハーネスの設計: generator と evaluator の分離](harness-design-long-running-apps.md) - generator と evaluator の分離、コンテキストリセットと構造化された引き継ぎ、evaluator の調整、フロントエンド用ハーネス、数値、モデル更新時の簡素化の指針。
- [Claude で文章から知識グラフを構築するパイプライン](knowledge-graph-construction.md) - 抽出、関係の取得、名寄せ、複数ホップの問い合わせという流れと、モデル分担、評価、拡張時の注意点の要点。
- [マルチエージェントの 5 つの協調パターンと選び方](multi-agent-coordination-patterns.md) - generator-verifier、orchestrator-subagent、agent teams、message bus、shared state の使いどころ、弱点、選択の指針。
