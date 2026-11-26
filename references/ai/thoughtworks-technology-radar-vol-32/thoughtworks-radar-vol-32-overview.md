---
type: reference
title: 'Thoughtworks Technology Radar Vol.32 の全体像と 4 つのテーマ'
description: 'Thoughtworks Technology Radar Vol.32 (2025 年 4 月) の要約のうち、Radar の読み方 (象限とリング) と、今号の 4 つのテーマ (コーディング支援の監督付きエージェント、可観測性の進化、RAG の検索部分、複雑なデータの扱い) をまとめる。'
tags: [ai, thoughtworks, technology-radar, coding-agent, observability, rag, data]
status: stable
verified: { by: claude-code/claude-opus-5-5, at: 2026-11-26T00:00:00Z }
stale_after: 2027-11-26T00:00:00Z
---

# Thoughtworks Technology Radar Vol.32 の全体像と 4 つのテーマ

Thoughtworks の Technology Advisory Board (TAB) がまとめた Technology Radar Vol.32 (2025 年 4 月) の要約である。
この文書では Radar の読み方と今号のテーマを扱い、個々の項目 (blip) は象限ごとの文書に分ける。
今号は 105 項目で、IDE の中で人が監督しながら動かすコーディングエージェント、LLM の可観測性、RAG の検索の改善が目立つ。

- 発行: Thoughtworks
- 出典: Thoughtworks Technology Radar Volume 32 (PDF)、[thoughtworks.com/radar](https://www.thoughtworks.com/radar)
- 発行日: 2025 年 4 月 (2025 年 2 月のバンコクでの TAB 会議に基づく)

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

- しばらく動きのない項目は載せなくなる。価値が下がったという意味ではない。

## テーマ 1: コーディング支援の監督付きエージェント

- IDE の AI チャットから実装を進める使い方 (agentic、prompt-to-code、chat-oriented programming (CHOP) と呼ばれる) が広がった。AI がコードを辿って書き換え、テストを更新し、コマンドを実行し、lint やコンパイルのエラーも直す。
- 大きな仕事を完全に自律で進めるエージェントには懐疑的だが、開発者が導き監督する形では良い結果が出ている。
- IDE 統合型では Cursor、Cline、Windsurf が先行し、GitHub Copilot も追っている。ターミナル型には aider、goose、Claude Code がある。
- 一方で、AI 生成コードへの慢心 (complacency) が増すことを警戒しており、コードレビューでの舵取りと注意は引き続き必要である。

## テーマ 2: 可観測性の進化

- 分散アーキテクチャの複雑化に合わせ、可観測性の分野が大きく動いた。
- LLM の可観測性 (性能の監視と評価) の道具が急増した: Weights & Biases Weave、Arize Phoenix、Helicone、Humanloop など。
- AI で分析を助ける可観測性も広がっている。
- OpenTelemetry の採用が進み、ベンダーに依存しない構成が取りやすくなった。Alloy、Tempo、Loki などの主要な道具が対応している。

## テーマ 3: RAG の R (検索)

- 生成 AI の各部分は違う速さで進化しており、今号では RAG の検索 (retrieval) の部分が特に動いた。
- 取り上げた手法: 結果を評価して検索をやり直す corrective RAG、複数の情報源と検索戦略を組み合わせる Fusion-RAG、必要なときだけ取りに行く Self-RAG、人が辿れるグラフを作る FastGraphRAG。

## テーマ 4: データの最前線を飼い慣らす

- 議論の中心はデータの量ではなく、豊かで複雑なデータ、特に非構造化データをどう管理し、AI や分析に使える形にするかだった。
- ベクトルデータベースの道具から Metabase のような分析製品まで、多くの項目がデータの扱いに関わる。
- 道具だけでなく、プロダクト思考を分析データに当てはめる data product thinking を取り上げた。データの規律の必要性はかつてなく高い。

## See also

- [Thoughtworks Technology Radar Vol.32: Techniques](/references/ai/thoughtworks-technology-radar-vol-32/thoughtworks-radar-vol-32-techniques.md)
- [Thoughtworks Technology Radar Vol.32: Platforms](/references/ai/thoughtworks-technology-radar-vol-32/thoughtworks-radar-vol-32-platforms.md)
- [Thoughtworks Technology Radar Vol.32: Tools](/references/ai/thoughtworks-technology-radar-vol-32/thoughtworks-radar-vol-32-tools.md)
- [Thoughtworks Technology Radar Vol.32: Languages and Frameworks](/references/ai/thoughtworks-technology-radar-vol-32/thoughtworks-radar-vol-32-languages-and-frameworks.md)
