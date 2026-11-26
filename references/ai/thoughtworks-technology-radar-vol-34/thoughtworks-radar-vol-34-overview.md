---
type: reference
title: 'Thoughtworks Technology Radar Vol.34 の全体像と 4 つのテーマ'
description: 'Thoughtworks Technology Radar Vol.34 (2026 年 4 月) の要約のうち、Radar の読み方 (象限とリング) と、今号の 4 つのテーマ (エージェント時代の技術評価の難しさ、原則を守りパターンを手放す、権限を欲しがるエージェントの安全確保、コーディングエージェントに手綱を付ける) をまとめる。'
tags: [ai, thoughtworks, technology-radar, harness-engineering, agent, security, coding-agent]
status: stable
verified: { by: claude-code/claude-opus-5-5, at: 2026-11-26T00:00:00Z }
stale_after: 2027-11-26T00:00:00Z
---

# Thoughtworks Technology Radar Vol.34 の全体像と 4 つのテーマ

Thoughtworks の Technology Advisory Board (TAB) がまとめた Technology Radar Vol.34 (2026 年 4 月) の要約である。
この文書では Radar の読み方と今号のテーマを扱い、個々の項目 (blip) は象限ごとの文書に分ける。
今号は 118 項目で、コーディングエージェントの制御 (ハーネス) と、エージェントのセキュリティが大きな比重を占める。

- 発行: Thoughtworks
- 出典: Thoughtworks Technology Radar Volume 34 (PDF)、[thoughtworks.com/radar](https://www.thoughtworks.com/radar)
- 発行日: 2026 年 4 月 (2026 年 3 月のベンガルールでの TAB 会議に基づく)

## Radar の読み方

- Radar は、ソフトウェア開発に関わる技術や手法を blip と呼び、象限とリングの 2 軸で分類する。
- 象限は項目の種類を表す: Techniques (手法)、Platforms (基盤)、Tools (道具)、Languages and frameworks (言語・フレームワーク)。
- リングは Thoughtworks の推奨度を表す。

| リング  | 意味                                                                                       |
| :------ | :----------------------------------------------------------------------------------------- |
| Adopt   | 業界として採用すべきだと強く考える。Thoughtworks のプロジェクトで適切な場面に使っている     |
| Trial   | 追求する価値がある。リスクを許容できるプロジェクトで試してよい                             |
| Assess  | 自社にどう影響するかを理解する目的で調べる価値がある                                       |
| Caution | 慎重に進める。自分の文脈で注意深く評価すべき大きな懸念がある                               |

- Radar は先を見るものなので、しばらく動きのない項目は載せなくなる。価値が下がったという意味ではない。

## テーマ 1: エージェント時代の技術評価の難しさ

- AI の普及で、技術そのものだけでなく技術の評価の仕方も変わり、評価が難しくなっている。
- 原因の 1 つは意味の拡散 (semantic diffusion) である。spec-driven development や harness engineering のような新しい言葉が、意味が固まる前に広まり、人によって指すものが違う。
- 変化の速さも評価を難しくする。作られて 1 か月未満の道具や、1 人がコーディングエージェントと作った道具が次々に現れる。
  成熟を待てば助言が古くなり、急げばすぐ消える流行を取り上げてしまう。手軽に作れるものを誰が保守し続けるのかという持続性の問題もある。
- AI が生成するコードが増えると、仕組みを理解しないまま採用しやすくなり、codebase cognitive debt (理解の負債) が溜まる。

## テーマ 2: 原則を守り、パターンを手放す

- AI は未来だけでなく、開発の基礎も見直させている。今号ではペアプログラミング、ゼロトラスト、ミューテーションテスト、DORA 指標などの定番の手法に何度も立ち返った。
- クリーンコード、意図した設計、テストしやすさ、アクセシビリティといった原則も見直した。懐古ではなく、AI が複雑さを生む速さへの対抗として必要である。
- エージェント型の道具によって、コマンドラインが主要な画面として復活している。
- 一方で、AI 支援の開発は根本的な変化であり、チームの組み方や協働の仕方も変わる。チームトポロジーと並べてエージェントトポロジーを考える必要が出てくるかもしれない。
- 速さを規律なしに求めるとコストが膨らむという職人の伝統は、エージェントで速く動けるようになった今こそ守る価値がある。

## テーマ 3: 権限を欲しがるエージェントの安全確保

- 作る価値のあるエージェントほど、あらゆるものへのアクセスを必要とする (permission hungry)。OpenClaw や Claude Cowork は実務を受け持ち、Gas Town はコードベース全体でエージェントの群れを動かす。
- しかし安全対策が追いついていない。
  - プロンプトインジェクションにより、モデルは信頼できる指示と信頼できない入力を確実には区別できない。
  - 非公開データ、信頼できない内容、外部への行動の 3 つが揃う lethal trifecta は、設定の誤りではなく、役に立つエージェントの標準の姿になっている。
  - モデルの振る舞いは一貫せず、1 度成功しても次も成功する保証はない。悪意がなくても、データの持ち出し経路を見つけたり、触るべきでないブランチに push したりする。
- ゼロトラスト、最小権限、多層防御は最低限の前提であり、決定打はない。
  安全なエージェントシステムは、1 つの巨大なエージェントではなく、制約の強いエージェントをつないだパイプラインに強い監視と制御を付けた形になると予想している。
  MCP の代わりに制御しやすい Agent Skills を使う、永続実行するエージェント、agent instruction bloat を防ぐ手法がその方向を示している。

## テーマ 4: コーディングエージェントに手綱を付ける

- エージェントが賢くなるほど、人はループから抜けたくなる。その危険を抑えるため、チームはコーディングエージェントのハーネスに投資し始めている。
- フィードフォワード制御は、最初の試みで正しく作れるよう、エージェントが必要とするものを先に与える。
  Agent Skills (指示や規約を部品にし、必要なときに読み込む)、Superpowers のようなスキル集、プラグインマーケットプレイス、GitHub Spec Kit や OpenSpec のような仕様駆動開発のフレームワークがある。
- フィードバック制御は、エージェントが動いた後の振る舞いを観察し、自己修正のループを作る。
  コンパイラ、linter、型検査、テストなどの決定的な品質ゲートをエージェントのワークフローに組み込む feedback sensors for coding agents がその代表である。
  cargo-mutants などのミューテーションテスト、WuppieFuzz などのファジング、CodeScene などのコード品質分析が例に挙がる。
- 決定的な構造ルールと LLM による評価を組み合わせ、アーキテクチャのずれを減らしているチームもある。

## See also

- [Thoughtworks Technology Radar Vol.34: Techniques](/references/ai/thoughtworks-technology-radar-vol-34/thoughtworks-radar-vol-34-techniques.md)
- [Thoughtworks Technology Radar Vol.34: Platforms](/references/ai/thoughtworks-technology-radar-vol-34/thoughtworks-radar-vol-34-platforms.md)
- [Thoughtworks Technology Radar Vol.34: Tools](/references/ai/thoughtworks-technology-radar-vol-34/thoughtworks-radar-vol-34-tools.md)
- [Thoughtworks Technology Radar Vol.34: Languages and frameworks](/references/ai/thoughtworks-technology-radar-vol-34/thoughtworks-radar-vol-34-languages-and-frameworks.md)
- [Thoughtworks Technology Radar Vol.35 の全体像と 4 つのテーマ](/references/ai/thoughtworks-technology-radar-vol-35/thoughtworks-radar-vol-35-overview.md)
