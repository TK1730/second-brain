---
type: reference
title: '0xarcos による Claude Code の自動検証フックと Failure Ratchet'
description: 'Ariel Arcos (@0xarcos) の X 投稿および公開知見の要約で、Claude Code のフック機能と失敗台帳 (Failure Ratchet) を用いてエージェントの失敗を再発防止ルールへ変える仕組みを説明する。'
tags: [ai, agent, claude-code, harness-engineering, hooks, verification]
status: stable
verified: { by: antigravity/gemini-4-argon, at: 2026-11-15T00:00:00Z }
stale_after: 2027-11-15T00:00:00Z
---

# 0xarcos による Claude Code の自動検証フックと Failure Ratchet

Ariel Arcos 氏 (`@0xarcos`) による X 投稿および公開リポジトリで発信されている、Claude Code の自動検証フックと「Failure Ratchet (失敗のラチェット)」に関する設計知見の要約である。
なお、個別ポスト ID (`2119068641740091716`) の本文は検索インデックス上で直接取得できないため、本文書では公開されている `@0xarcos` の Claude Code ハーネス設計および Failure Ratchet の知見を統合して整理している。

- 著者: Ariel Arcos (X: `@0xarcos` / GitHub: [0xARCOS](https://github.com/0xARCOS))
- 出典: [Ariel Arcos の X 投稿](https://x.com/0xarcos/status/2119068641740091716) および関連公開リポジトリ (`https://github.com/0xARCOS`)

## 概要: プロンプトの注意書きから「逆戻りしない歯車」へ

Claude Code を用いた自律開発において、エージェントが犯したミスに対してプロンプトや `CLAUDE.md` に「次は気をつけて」「必ず確認して」といった口頭注意 (散文のルール) を追記するだけでは、コンテキストが長くなった際に再び同じミスが起きる。
`@0xarcos` が実践するアプローチは、フック機能 (`PostToolUse` や `Stop` フック) による決定論的な検証と、失敗台帳 (`failures.yaml`) を組み合わせることで、一度起きた失敗を「二度と逆戻りしない歯車 (Failure Ratchet)」としてハーネス側に組み込む手法である。

## フックによる決定論的な即時検証

エージェントの自己申告 (「テストが通りました」「修正完了しました」) を信用せず、Claude Code のライフサイクルフックを使って機械的な検証を強制する。

### `PostToolUse` フックによる即時フィードバック

ファイルの編集・作成ツールが実行された直後に `PostToolUse` フックを発火させ、型チェック (`tsc --noEmit` など) やリンター、フォーマッターを自動実行する。
もし型エラーや構文違反があれば、その場でエージェントのコンテキストにエラー出力をフィードバックし、次のステップへ進む前に即座に修正させる。
これにより、壊れたコードの上にさらに変更を積み重ねてしまう事態を防ぐ。

### `Stop` フック (`scripts/verify.sh`) による完了ゲートの強制

エージェントが作業完了を宣言してターンを停止しようとする瞬間に、`Stop` フックを通じて検証スクリプト (`scripts/verify.sh`) を実行する。
テストスイート、ビルド、および後述する Failure Ratchet の不変条件チェックがすべて通過していなければ、フックが非ゼロの終了コードを返して停止をブロックし、エージェントに未解決のエラーを突きつけて作業を継続させる。

## Failure Ratchet: 失敗を資産化する仕組み

Failure Ratchet は、エージェントが実際に犯した失敗を体系的に分類し、実行可能な検査コードへと変換して蓄積していく仕組みである。

### 8 つの失敗クラス (Failure Classes)

エージェントの失敗原因を曖昧な「モデルの精度不足」で片付けず、以下の 8 つのクラスに分類して診断する。

| 失敗クラス | 現象と原因 |
| :--- | :--- |
| `BLIND` | 必要なファイルや既存実装を読まず、推測だけでコードを変更してしまう。 |
| `FLOODED` | コンテキストウィンドウに不要な情報が溢れ、重要な指示や制約を見落とす。 |
| `CLUMSY` | ファイル編集ツールの指定ミスやコマンド構文エラーなど、道具の操作自体に失敗する。 |
| `AMNESIAC` | セッションの進行やコンテキスト圧縮に伴い、初期の目的や設計制約を忘却する。 |
| `OVERCONFIDENT` | テストや動作確認を実行しないまま、変更が正しく動くと誤認して完了を宣言する。 |
| `STUCK` | 同じエラーに対して同じ無効な修正を繰り返し、無限ループに陥る。 |
| `RECKLESS` | 依頼されたスコープを超え、無関係なファイルの削除や破壊的な変更を行う。 |
| `DRIFTING` | 作業の途中で枝葉の課題に気を取られ、本来のゴールから徐々に逸脱していく。 |

### 失敗を歯車に変える 6 ステップのプロトコル

エージェントの失敗に遭遇した際、以下の 6 ステップ (`CAPTURE` → `CLASSIFY` → `LOCATE` → `ENCODE` → `PROVE` → `LOG`) を踏んで再発防止策をハーネスに定着させる。

1. **`CAPTURE` (捕捉)**: エージェントが何を誤り、どのような不正な状態やエラーが生じたのかを具体的な証拠とともに記録する。
2. **`CLASSIFY` (分類)**: 上記の 8 つの失敗クラスのどれに該当するかを判定し、失敗の性質を特定する。
3. **`LOCATE` (特定)**: なぜその失敗が素通りしたのかを調べ、ハーネスのどの層 (ルール、スキル、検証スクリプト、フック) に欠陥・抜け穴があったかを特定する。
4. **`ENCODE` (コード化)**: 単なるテキストの注意書きではなく、その失敗を機械的に検出できる検査コードやアサーション (`scripts/verify.sh` 内のチェックやフック処理) として実装する。
5. **`PROVE` (証明)**: 追加した検査コードが、先ほど捕捉した失敗状態に対して「確実に失敗 (赤) になること」と、修正後に「成功 (緑) になること」の双方を実演して証明する。
6. **`LOG` (台帳記録)**: 失敗の ID、分類、原因、エンコードした検証スクリプトへの参照を失敗台帳 (`failures.yaml`) に追記し、ハーネスの恒久的な資産として保存する。

## See also

- [Ariel Arcos (@0xarcos) の X 投稿](https://x.com/0xarcos/status/2119068641740091716)
- [0xARCOS (GitHub)](https://github.com/0xARCOS)
- `/references/ai/zenn-sasadango28-claude-code-harness-engineering.md` — Claude Code における 5 層のハーネス設計パターン
- `/references/ai/microsoft-commandline-copilot-cowork-python-to-rust.md` — 「チェック自体が機能していることを証明する」など Copilot Cowork の開発教訓
- `/references/ai/beamnxw-agent-harness-loop-graph-engineering.md` — ハーネス・ループ・グラフの 3 層でエージェントの失敗を切り分ける設計論
