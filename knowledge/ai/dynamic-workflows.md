---
type: guideline
title: 'Claude Code の動的ワークフローで大規模タスクを並列に検証しながら進める'
description: '動的ワークフローの仕組み、並列サブエージェントと反証ループ、使いどころ、提供範囲、上限と費用の要点。'
tags: [knowledge, ai, claude, claude-code, workflow, subagent, parallel]
status: stable
sources:
  - id: claude-article
    resource: 'https://claude.com/resources/articles/introducing-dynamic-workflows-in-claude-code'
  - id: claude-cookbook
    resource: 'https://platform.claude.com/cookbook/claude-agent-sdk-08-dynamic-workflows'
generated: { by: claude-code/claude-sonnet-5-5, at: 2026-11-17T00:00:00Z }
verified: { by: claude-code/claude-sonnet-5-5, at: 2026-11-17T00:00:00Z }
stale_after: 2027-11-17T00:00:00Z
---

# Claude Code の動的ワークフローで大規模タスクを並列に検証しながら進める

1 つの会話では扱いきれない規模の作業を、Claude Code の動的ワークフロー（dynamic workflows）で進めるときの仕組みと判断基準をまとめる。
内容は Anthropic の記事「Introducing dynamic workflows in Claude Code」（2026-05-28 公開）[^claude-article] と、Claude Agent SDK のクックブック [^claude-cookbook] の要約である。
数値は、各資料が示す個別の事例や実行結果であり、一般化した測定ではない。

## 動的ワークフローとは

- Claude が、利用者の依頼から計画を立て、サブタスクに分けるオーケストレーション用のスクリプトを書く。そのスクリプトが、数十から数百のサブエージェントを 1 つのセッションで並列に走らせる。[^claude-article]
- 結果は、利用者に渡す前に検証される。利用者は、まとまった 1 つの答えを受け取る。[^claude-article]
- 調整は会話の外で行われるため、タスクが大きくなっても計画がぶれにくい。進捗は保存され、中断しても最初からではなく途中から再開できる。実行は数時間から数日に及ぶことがある。[^claude-article]
- 記事は、本来は四半期かけて計画する作業が数日で終わりうると述べる。[^claude-article]

## 仕組み

クックブックによると、Claude は JavaScript のスクリプトを書いて `Workflow` ツールへ渡す。ランタイムがそれをバックグラウンドで実行する。[^claude-cookbook]

- スクリプトが、サブエージェントを並列または段階的に起動し、結果を変数に保存し、絞り込み、ループ、検証を通常のコードで書く。
- 各サブエージェントは、まっさらな文脈を持つ完全な Claude Code のエージェントである。スクリプトが渡したプロンプトだけを見て、セッションの作業ディレクトリで、設定されたツールの許可リストの範囲で動く。
- モデルはセッションのものが既定である。段階ごとに別のモデルへ振り分けられる。環境変数 `CLAUDE_CODE_SUBAGENT_MODEL` で全エージェントを一括で上書きできる。

スクリプトの部品は次のとおりである。[^claude-cookbook]

| 部品                                   | 役割                                                                           |
| :------------------------------------- | :----------------------------------------------------------------------------- |
| `export const meta`                    | ワークフローの名前、説明、フェーズを宣言する                                   |
| `agent(prompt, options)`               | サブエージェントを 1 つ起動する。`label`、`phase`、JSON の `schema`、`model` を指定できる |
| `parallel([...])`                      | エージェントを同時に走らせ、すべての完了を待つ                                 |
| `pipeline(items, stage1, stage2, ...)` | 各項目を、互いに独立に複数の段階へ通す                                         |
| `phase("...")`                         | 以降のエージェントをフェーズへ割り当てる                                       |
| 通常の JavaScript                      | 絞り込み、重複排除、統合、ループ。トークンを消費しない                         |
| `return {...}`                         | 結果をセッションへ返す                                                         |

## 単一エージェントやサブエージェントとの違い

| 観点               | 単一のエージェント | サブエージェント         | 動的ワークフロー         |
| :----------------- | :----------------- | :----------------------- | :----------------------- |
| 次を決めるのは     | Claude（ターンごと）| Claude（ターンごと）     | スクリプト               |
| 途中結果の置き場所 | Claude の文脈      | 親のエージェントの文脈   | スクリプトの変数         |
| 規模               | 1 つの文脈の範囲   | 1 ターンに数タスク       | 1 回の実行に数十から数百 |
| 中断               | ターンをやり直す   | ターンをやり直す         | 同じセッション内で再開   |

検証の手順がスクリプトの制御フローに組み込まれるため、プロンプトの指示のようにエージェントが飛ばすことがない。[^claude-cookbook]
サブエージェントの扱い自体を見直す観点は、[サブエージェントをメインのエージェントループへ統合する判断と手順](/knowledge/ai/folding-subagents-into-main-agent.md)を参照する。

## 検証と反証のループ

- 複数のエージェントが、独立した角度から問題に取り組む。別のエージェントが、その発見を反証しようとする。答えが収束するまで繰り返す。1 回の実行では得られない結果に届く方法として、記事はこれを挙げる。[^claude-article]
- 失敗の代償が大きい作業では、独立した試行に加えて、結果を壊そうとする敵対的なエージェントを置く。[^claude-article]
- セキュリティ監査では、指摘のひとつひとつに独立した検証を走らせ、実在する問題だけを報告に残す。[^claude-article]

クックブックの例は、投資家向け更新資料の事実確認である。4 つの段階で構成する。[^claude-cookbook]

1. 抽出: 1 つのエージェントが、10 件の主張を構造化して取り出す。
1. 検証: 主張ごとに 1 つのエージェントを並列に走らせる。情報源を新しく読み、`confirmed`、`contradicted`、`unverifiable` のいずれかを、根拠の行の引用つきで返す。
1. 懐疑: `confirmed` の判定だけを、懐疑役のエージェントが再検証する。`contradicted` へ覆すこともできる。確認済みだけを回すので、余計な費用がかからない。
1. 報告: 1 つのエージェントが、表と修正リストをまとめて返す。

結果は、矛盾 4 件、確認不能 2 件、確認 4 件で、懐疑役は確認をすべて支持した。実行は約 1.3 分、費用は 0.60 ドルだった。段階が失敗して再試行されると、費用は増えうる。[^claude-cookbook]

## 使いどころ

- 並列に進められる長時間の作業と、誤った答えの代償が大きい重要な作業に向く。[^claude-article]
- 記事が挙げる題材は、サービス全体のバグ探し、プロファイラを使った最適化の監査、セキュリティ監査、数百から数千ファイルにおよぶ移行や近代化（フレームワークの入れ替え、API の廃止対応、言語の移植）、決める前にあらゆる角度から検証したい計画である。[^claude-article]
- クックブックの基準では、タスクが 1 つの文脈に収まらないとき、検証を構造で強制したいとき、オーケストレーションを再利用する価値があるときに使う。代償はトークンである。[^claude-cookbook]

事例として、記事は Bun を Zig から Rust へ移植した取り組みを紹介する。[^claude-article]

- 既存のテストの 99.8% が通り、Rust は約 75 万行、最初のコミットからマージまで 11 日だった。
- 1 つのワークフローが、構造体の各フィールドの Rust でのライフタイムを割り出した。
- 数百のエージェントが、各 `.rs` ファイルを対応する `.zig` ファイルと同じ振る舞いの移植として書き、ファイルごとに 2 人のレビュー役が付いた。
- 修正のループが、ビルドとテストが通るまで回った。
- 記事は、これがまだ本番には入っていないと注記している。

## 始め方

- Claude へ直接「ワークフローを作って」と頼む。[^claude-article]
- effort のメニューから、Claude Code 固有の `ultracode` 設定を有効にする。effort が xhigh になり、ワークフローが妥当かどうかを Claude が判断する。[^claude-article]
- 初回は、実行する内容が表示され、確認を求められる。[^claude-article]
- 記事は、最良の体験のために auto モードを有効にすることを勧める。[^claude-article]
- Python の SDK から使うには、`allowed_tools` へ `Workflow` を入れ、プロンプトに「ワークフローを使って」と明記し、`query()` で実行を流す。バックグラウンド実行では、ターンごと（起動と完了）に `ResultMessage` が 1 つ届くので、最後のものを最終結果にする。[^claude-cookbook]

## 提供範囲

- 提供状況は一般提供である。当初は早期アクセスとして紹介された。[^claude-article]
- 利用先は、Claude Code の CLI、デスクトップ版、VS Code 拡張、Claude API、Amazon Bedrock、Vertex AI、Microsoft Foundry である。[^claude-article]
- 対象のプランは、Pro、Max、Ultra、Team、Enterprise である。Max、Ultra、Team、Enterprise と、API 経由の Claude Code では既定で有効になる。Pro は `/config` で有効にする。管理者は、設定で提供を管理でき、管理設定で無効にもできる。[^claude-article]
- SDK の要件は、Python 3.11 以上、`claude-agent-sdk` 0.2.90 以上（Claude Code CLI v2.1.154 以上を同梱）、`ANTHROPIC_API_KEY` である。[^claude-cookbook]

## 上限と注意

- 同時に動くエージェントは最大 16 で、CPU コアが少ない環境ではさらに少ない。超えた分は空きが出るまで待つ。1 回の実行の上限は 1,000 エージェントである。[^claude-cookbook]
- 通常のセッションより、トークンも利用量も大きく増える。小さく絞ったタスクから始めて、自分の作業での消費量をつかむ。[^claude-article]
- スクリプト自体は、ファイルシステムやシェルに触れられない。触れるのは起動されたエージェントだけである。[^claude-cookbook]
- SDK には対話的な確認がない。サブエージェントは `acceptEdits` モードで動き、許可リストを引き継ぐ。[^claude-cookbook]
- 止めた実行は、同じセッション内なら再開できる。新しいセッションでは最初からになる。段階が失敗すると、Claude が再起動するのが通常で、完了済みのエージェントは保存された結果を返す。[^claude-cookbook]
- スクリプトは `~/.claude/projects/` の下に `.js` として保存される。プロジェクトの `.claude/workflows/` へ置けば、名前で再実行できる。[^claude-cookbook]
- 発見は、レポート用のファイルではなく、値としてスクリプトへ返させる。変換した文書やコードなど、本来の成果物は通常どおりディスクへ書く。[^claude-cookbook]

## 費用を抑える習慣

1. 検証の段階や、安いモデルで足りる段階を含め、望む構造をプロンプトで明示する。
1. 実行ごとの費用を確認する。
1. 小さなデータで試す。構造は同じまま拡大できるが、トークンの予算も同じ比率で増える。

出典は、これらをクックブックの実践的な習慣として挙げている。[^claude-cookbook]

## See also

- [サブエージェントをメインのエージェントループへ統合する判断と手順](/knowledge/ai/folding-subagents-into-main-agent.md)
- [HanakoXBT のループとグラフ](/references/ai/hanakoxbt-loops-and-graphs.md)

[^claude-article]: [Introducing dynamic workflows in Claude Code](https://claude.com/resources/articles/introducing-dynamic-workflows-in-claude-code)（2026-05-28）
[^claude-cookbook]: [Dynamic workflows（Claude Agent SDK クックブック）](https://platform.claude.com/cookbook/claude-agent-sdk-08-dynamic-workflows)
