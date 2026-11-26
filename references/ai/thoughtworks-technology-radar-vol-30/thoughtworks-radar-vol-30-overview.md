---
type: reference
title: 'Thoughtworks Technology Radar Vol.30 の全体像と 4 つのテーマ'
description: 'Thoughtworks Technology Radar Vol.30 (2024 年 4 月) の要約のうち、Radar の読み方 (象限とリング) と、今号の 4 つのテーマ (オープンソースもどきのライセンス、AI を使うチーム開発、LLM のアーキテクチャパターン、PR を本来の CI に近づける) をまとめる。'
tags: [ai, thoughtworks, technology-radar, llm, rag, continuous-integration, open-source]
status: stable
verified: { by: claude-code/claude-opus-5-5, at: 2026-11-26T00:00:00Z }
stale_after: 2027-11-26T00:00:00Z
---

# Thoughtworks Technology Radar Vol.30 の全体像と 4 つのテーマ

Thoughtworks の Technology Advisory Board (TAB) がまとめた Technology Radar Vol.30 (2024 年 4 月) の要約である。
この文書では Radar の読み方と今号のテーマを扱い、個々の項目 (blip) は象限ごとの文書に分ける。
今号は 105 項目のうち約 3 分の 1 が AI に関するもので、RAG を LLM の出力を良くする第一の手段とする立場がはっきりしている。

- 発行: Thoughtworks
- 出典: Thoughtworks Technology Radar Volume 30 (PDF)、[thoughtworks.com/radar](https://www.thoughtworks.com/radar)
- 発行日: 2024 年 4 月 (2024 年 2 月のニューヨークでの TAB 会議に基づく)

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

- この号の最も慎重なリングは Hold である (後の号では Caution に名前が変わる)。
- Radar は先を見るものなので、しばらく動きのない項目は載せなくなる。価値が下がったという意味ではない。

## テーマ 1: オープンソースもどきのライセンス

- 長年、オープンソースの生態系は OSI が認めた少数のライセンスに支えられてきたが、最近は揺れている。
- 広く使われる道具が、突然オープンソースから商用モデルに切り替える例が続いた。追加機能を有料にするのは構わないが、生態系ができた後に中核機能を有料の壁の向こうに移すのは問題である。
- オープンソースを名乗りながら、基本的な機能が有料の契約後にしか使えないソフトウェアも、新しい AI 道具を中心に増えている。
- ライセンスの但し書きに注意し、リポジトリの全ファイルが最上位のライセンスで覆われているかを確かめる。

## テーマ 2: AI を使うソフトウェア開発チーム

- 今号の項目の 3 分の 1 が何らかの形で AI に関わる。
- GitHub Copilot、Codium AI、aider、Continue など開発者向けの道具に加え、チーム全体で AI を使うと開発のあり方がどう変わるかを議論した。
- 開発者向けの道具が最も成熟しているが、開発のあらゆる面が、AI の実用的な使い方から少しずつ恩恵を受けると見ている。
- 新しい能力は、品質とセキュリティの新しいリスクも伴う。開発者以外の人にも危険を共有し、注意を保つ必要がある。

## テーマ 3: LLM のためのアーキテクチャパターン

- LLM の利用が広がり、よくある状況に対する特有のアーキテクチャパターンが現れ始めた。
- 例: NeMo Guardrails による利用ポリシーの統制、Langfuse による LLM の出力に至る過程の可観測性、生成コードで膨らんだコードベースの扱い。
- 企業での LLM の出力品質を上げる手段として、RAG を第一に勧める。
- 安価な LLM で作った成果物を、高性能で高価な LLM が選んで確かめる手法も議論した。
- 生成 AI が開発に浸透するにつれ、パターン (と避けるべきアンチパターン) が急増すると予想している。

## テーマ 4: PR を本来の CI に近づける

- Thoughtworks は速いフィードバックのために継続的インテグレーション (CI) を強く支持してきたが、多くのチームはプルリクエスト (PR) を義務づけられ、CI の部分を実践できていない。
- PR はもともと、分散したオープンソースの開発で信頼できない貢献者を扱うための仕組みだったが、小さく結束したチームでも同僚レビューの代名詞になった。
- gitStream や GitHub merge queue など PR レビューの負担を減らす道具、stacked diffs のような統合を細かく制御する手法、PR から指標をとってボトルネックを見つける方法を検討した。
- AI コーディング支援でコードの量が増えると PR が大きくなり、非同期のコードレビューへの圧力がさらに高まる。
- 本来の CI を好む立場は変わらないが、外部の制約でできないチームには、統合の精度とフィードバックの速さを上げる工夫を勧める。

## See also

- [Thoughtworks Technology Radar Vol.30: Techniques](/references/ai/thoughtworks-technology-radar-vol-30/thoughtworks-radar-vol-30-techniques.md)
- [Thoughtworks Technology Radar Vol.30: Platforms](/references/ai/thoughtworks-technology-radar-vol-30/thoughtworks-radar-vol-30-platforms.md)
- [Thoughtworks Technology Radar Vol.30: Tools](/references/ai/thoughtworks-technology-radar-vol-30/thoughtworks-radar-vol-30-tools.md)
- [Thoughtworks Technology Radar Vol.30: Languages and Frameworks](/references/ai/thoughtworks-technology-radar-vol-30/thoughtworks-radar-vol-30-languages-and-frameworks.md)
- [Thoughtworks Technology Radar Vol.35 の全体像と 4 つのテーマ](/references/ai/thoughtworks-technology-radar-vol-35/thoughtworks-radar-vol-35-overview.md)
