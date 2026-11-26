---
type: reference
title: 'Thoughtworks Technology Radar Vol.33 の全体像と 4 つのテーマ'
description: 'Thoughtworks Technology Radar Vol.33 (2025 年 11 月) の要約のうち、Radar の読み方 (象限とリング) と、今号の 4 つのテーマ (AI のためのインフラのオーケストレーション、MCP とエージェントの台頭、AI コーディングのワークフロー、AI のアンチパターン) をまとめる。'
tags: [ai, thoughtworks, technology-radar, mcp, agent, ai-infrastructure, coding-agent]
status: stable
verified: { by: claude-code/claude-opus-5-5, at: 2026-11-26T00:00:00Z }
stale_after: 2027-11-26T00:00:00Z
---

# Thoughtworks Technology Radar Vol.33 の全体像と 4 つのテーマ

Thoughtworks の Technology Advisory Board (TAB) がまとめた Technology Radar Vol.33 (2025 年 11 月) の要約である。
この文書では Radar の読み方と今号のテーマを扱い、個々の項目 (blip) は象限ごとの文書に分ける。
今号は 114 項目で、MCP とエージェント、AI コーディングのワークフロー、GPU を扱うインフラが中心である。

- 発行: Thoughtworks
- 出典: Thoughtworks Technology Radar Volume 33 (PDF)、[thoughtworks.com/radar](https://www.thoughtworks.com/radar)
- 発行日: 2025 年 11 月 (2025 年 9 月のブカレストでの TAB 会議に基づく)

## Radar の読み方

- Radar は、ソフトウェア開発に関わる技術や手法を blip と呼び、象限とリングの 2 軸で分類する。
- 象限は項目の種類を表す: Techniques (手法)、Platforms (基盤)、Tools (道具)、Languages and Frameworks (言語・フレームワーク)。
- リングは Thoughtworks の推奨度を表す。

| リング | 意味                                                                                   |
| :----- | :------------------------------------------------------------------------------------- |
| Adopt  | 業界として採用すべきだと強く考える。Thoughtworks のプロジェクトで適切な場面に使っている |
| Trial  | 追求する価値がある。リスクを許容できるプロジェクトで試してよい                         |
| Assess | 自社にどう影響するかを理解する目的で調べる価値がある                                   |
| Hold   | 慎重に進める                                                                           |

- この号の最も外側のリングは Hold である (Vol.35 では Caution と呼ぶ)。
- Radar は先を見るものなので、しばらく動きのない項目は載せなくなる。価値が下がったという意味ではない。

## テーマ 1: AI のためのインフラのオーケストレーション

- AI のワークロードで、学習と推論の両方に大量の GPU を扱う必要が出てきた。1 つのアクセラレーター (80 GB の HBM) に収まらないモデルが増え、分散学習と複数 GPU での推論が当たり前になりつつある。
- Kubernetes は引き続き AI ワークロードを大規模に扱う土台である。Kueue によるキューとクォータ、トポロジーを考えた配置、ギャングスケジューリングで、複数 GPU のジョブを高速な GPU 間リンク (NVLink など) の近くにまとめる。
- GPU を意識したオーケストレーションは必須になりつつあり、トポロジーはスケジューリングの第一級の関心事になった。

## テーマ 2: MCP とエージェントの台頭

- MCP とエージェント、その周辺のプロトコルや道具が今号を占めている。主要ベンダーのほとんどが MCP に対応し始め、MCP はエージェントを動かすための統合プロトコルになった。
- エージェントのワークフローでは、振る舞いと資源消費の両方を最適化するコンテキストエンジニアリングが重要である。
- A2A や AG-UI などの新しいプロトコルが、利用者向けのマルチエージェントアプリを作る手間を減らしている。
- 前号の主役が RAG だったのに対し、今号はエージェントのワークフローと、それを支える道具・手法・基盤、そして新しいアンチパターンが主役である。

## テーマ 3: AI コーディングのワークフロー

- AI はレガシーコードの理解から新しい実装 (フォワードエンジニアリング) まで、ソフトウェアの価値の流れ全体に入り込んでいる。
- コーディングエージェントに知識を渡す方法が試されている: AGENTS.md による独自の指示、Context7 のような MCP サーバーによる最新の依存ライブラリの文書の取得。
- AI は個人ではなくチーム全体を底上げすべきだという認識が広がり、チームで共有する指示 (curated shared instructions) やカスタムコマンドが現れている。
- 仕様駆動開発 (spec-driven development) の範囲や粒度は議論が続いている。AI が生成したコードへの慢心は共通の懸念で、人の判断は欠かせない。

## テーマ 4: 現れつつある AI のアンチパターン

- GenAI による使い捨ての UI プロトタイプは有用だが、AI で加速したシャドー IT につながる恐れがある。
- MCP が広まるにつれ、既存の API をそのまま MCP に変換する (naive API-to-MCP conversion) チームが増えている。
- Text to SQL は期待ほどの効果が出ていない。AI が生成したコードへの慢心も引き続き問題である。
- 仕様駆動開発でも、重い事前仕様と一括リリースという昔のアンチパターンに戻る危険がある。
- 最初は効果的に見えても、時間とともにフィードバックを遅らせ、適応力を損ない、責任の所在をあいまいにするパターンに注意し続ける必要がある。

## See also

- [Thoughtworks Technology Radar Vol.33: Techniques](/references/ai/thoughtworks-technology-radar-vol-33/thoughtworks-radar-vol-33-techniques.md)
- [Thoughtworks Technology Radar Vol.33: Platforms](/references/ai/thoughtworks-technology-radar-vol-33/thoughtworks-radar-vol-33-platforms.md)
- [Thoughtworks Technology Radar Vol.33: Tools](/references/ai/thoughtworks-technology-radar-vol-33/thoughtworks-radar-vol-33-tools.md)
- [Thoughtworks Technology Radar Vol.33: Languages and Frameworks](/references/ai/thoughtworks-technology-radar-vol-33/thoughtworks-radar-vol-33-languages-and-frameworks.md)
- [Thoughtworks Technology Radar Vol.35 の全体像と 4 つのテーマ](/references/ai/thoughtworks-technology-radar-vol-35/thoughtworks-radar-vol-35-overview.md)
