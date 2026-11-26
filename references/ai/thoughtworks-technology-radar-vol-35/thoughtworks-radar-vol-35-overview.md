---
type: reference
title: 'Thoughtworks Technology Radar Vol.35 の全体像と 4 つのテーマ'
description: 'Thoughtworks Technology Radar Vol.35 (2026 年 11 月) の要約のうち、Radar の読み方 (象限とリング) と、今号の 4 つのテーマ (ハーネスエンジニアリングの拡大、フロンティアモデル以外の選択肢、並列エージェント、AI ファクトリー) をまとめる。'
tags: [ai, thoughtworks, technology-radar, harness-engineering, agent, llm, ai-infrastructure]
status: stable
verified: { by: claude-code/claude-opus-5-5, at: 2026-11-26T00:00:00Z }
stale_after: 2027-11-26T00:00:00Z
---

# Thoughtworks Technology Radar Vol.35 の全体像と 4 つのテーマ

Thoughtworks の Technology Advisory Board (TAB) がまとめた Technology Radar Vol.35 (2026 年 11 月) の要約である。
この文書では Radar の読み方と今号のテーマを扱い、個々の項目 (blip) は象限ごとの文書に分ける。
今号は 117 項目のうち多くが AI エージェントとその周辺 (ハーネス、モデル選定、推論基盤) に関するものである。

- 発行: Thoughtworks
- 出典: Thoughtworks Technology Radar Volume 35 (PDF)、[thoughtworks.com/radar](https://www.thoughtworks.com/radar)
- 発行日: 2026 年 11 月 (2026 年 9 月のブラジル・レシフェでの TAB 会議に基づく)

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

## テーマ 1: ハーネスエンジニアリングの拡大

- ハーネスエンジニアリングは、メモリ、コンテキスト、フィードバックループ、ガードレールなど、AI エージェントを取り巻く環境を作る活動全体を指す。
  今号では単独の項目ではなく、多くの項目をつなぐテーマとして取り上げた。
- プラグインの生態系ができつつある。例として Agent Plugins (標準形式)、agent plugin marketplace (配布)、Agent Package Manager (依存管理) がある。
- ハーネスは作って終わりではなく、所有者を決めて保守し続ける資産である。
  harness quality evaluation、self-improving harness、feedback flywheel はそのための手法である。
- 次の課題は企業規模への拡大である。
  数年前にプラットフォームエンジニアリングが製品化したように、enterprise harness が製品として現れる可能性がある。

## テーマ 2: フロンティアモデル以外の選択肢

- 何にでも独自のフロンティアモデルを使うのが当然ではない段階に入った。
- オープンウェイトモデルとフロンティアモデルの差は、多くのタスクで 12 か月前よりずっと小さい。
  費用に加え、自社クラウドや自前のハードウェアで動かせるため、プライバシー要件やベンダー依存の軽減にも効く。
  コーディングでは GLM ファミリーが一部のエージェント用途で現実的な代替になった。
- ローカルのコーディングモデル、構造化データ向けの基盤モデル、Jev のような decision model など、LLM 以外の AI の選択肢も増えている。
- タスクごとにモデルを選ぶことはエンジニアリングチームの責任になりつつあり、モデルルーティングが重要な検討事項になる。
  Radar は blanket frontier model usage (何でもフロンティアモデルを使うこと) に注意を促している。

## テーマ 3: より多くのエージェントを働かせる

- 前号はコーディングエージェントそのものが中心だったが、今号は複数のエージェントを同時に使う提案が多かった。
  開発者が複数のセッションを並列に動かして舵を取る形や、unattended overnight agentic builds のように長時間の仕事を任せる形である。
- 役割を決めた team of coding agents や、オーケストレーターが自ら仕事を分配する coding agent swarm よりも軽い方法である。
  Thoughtworks では、人が直接制御しながら複数セッションを動かす形が主流で、始める場所として妥当だとしている。
- 並列セッション管理の道具 (Claude Squad、T3 Code、Orca、Paseo、Herdr など) の多くは、応答や承認を待つセッションを優先表示する attention inbox を持つ。
  Git worktree は各セッションに作業コピーを与えるが、中途半端にマージされたブランチが残りやすい。
- エージェントを増やすほど、人の注意とレビュー能力がボトルネックになる。
  レビューが追いつかないと human-in-the-loop theater (形だけの人の承認) になる。
  変更がデリバリーパイプラインの処理能力を超えることもあるので、path-to-production mapping で詰まる場所を見つける。
- セッションを増やす前に、レビューとデリバリーの工程がどれだけ受け止められるかを考えるべきである。

## テーマ 4: AI ファクトリーの構築

- トークンの経済性は、最終的にはインフラの経済性で決まる。
  AI の費用はモデルの料金だけでなく、モデル選定、ルーティング、バッチ処理、データ移動、基盤の効率に左右される。
- Kubernetes が、AI ワークロードを大規模に動かす工業化された基盤 (AI ファクトリー) の土台になりつつある。
  - モデル提供と GPU を意識した配置: KServe、KAITO
  - 分散推論とスケジューリング: llm-d
  - モデルと推論提供者をまたぐルーティング: LiteLLM
  - ストレージ: VAST DataStore
  - ネットワーク自動化: Netris
- モデル、GPU、推論エンジン、ストレージ、ネットワークを、共通の基盤層からプログラムで扱う資源として管理する方向に進んでいる。

## See also

- [Thoughtworks Technology Radar Vol.35: Techniques](/references/ai/thoughtworks-technology-radar-vol-35/thoughtworks-radar-vol-35-techniques.md)
- [Thoughtworks Technology Radar Vol.35: Platforms](/references/ai/thoughtworks-technology-radar-vol-35/thoughtworks-radar-vol-35-platforms.md)
- [Thoughtworks Technology Radar Vol.35: Tools](/references/ai/thoughtworks-technology-radar-vol-35/thoughtworks-radar-vol-35-tools.md)
- [Thoughtworks Technology Radar Vol.35: Languages and frameworks](/references/ai/thoughtworks-technology-radar-vol-35/thoughtworks-radar-vol-35-languages-and-frameworks.md)
- [どの Claude モデルで開発すべきか: Fable・Opus・Sonnet・Haiku の使い分け](/references/ai/claude-blog-which-claude-model-should-you-build-with.md)
