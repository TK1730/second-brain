---
type: reference
title: 'Thoughtworks Technology Radar Vol.31 の全体像と 4 つのテーマ'
description: 'Thoughtworks Technology Radar Vol.31 (2024 年 10 月) の要約のうち、Radar の読み方 (象限とリング) と、今号の 4 つのテーマ (コーディング支援のアンチパターン、Rust の広がり、WASM の台頭、生成 AI ツールのカンブリア爆発) をまとめる。'
tags: [ai, thoughtworks, technology-radar, generative-ai, rust, webassembly, coding-assistant]
status: stable
verified: { by: claude-code/claude-opus-5-5, at: 2026-11-26T00:00:00Z }
stale_after: 2027-11-26T00:00:00Z
---

# Thoughtworks Technology Radar Vol.31 の全体像と 4 つのテーマ

Thoughtworks の Technology Advisory Board (TAB) がまとめた Technology Radar Vol.31 (2024 年 10 月) の要約である。
この文書では Radar の読み方と今号のテーマを扱い、個々の項目 (blip) は象限ごとの文書に分ける。
今号は 105 項目で、生成 AI と LLM を使うための道具や手法が議論の中心だった。

- 発行: Thoughtworks
- 出典: Thoughtworks Technology Radar Volume 31 (PDF)、[thoughtworks.com/radar](https://www.thoughtworks.com/radar)
- 発行日: 2024 年 10 月 (2024 年 9 月の TAB のオンライン会議に基づく)

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

- Radar は先を見るものなので、しばらく動きのない項目は載せなくなる。価値が下がったという意味ではない。

## テーマ 1: コーディング支援のアンチパターン

- 生成 AI と LLM が今号の議論を支配し、開発者による使い方のパターンとともにアンチパターンも見え始めた。
- 例: ペアプログラミングを AI で完全に置き換えられるという誤解、提案への過度な依存、生成コードの品質の問題、コードベースの急速な肥大化。
- AI は抽象化を使わず力技で解きがちである (Strategy パターンの代わりに何十もの条件分岐を重ねるなど)。
- 「動くがひどい」コードに溺れないよう、単体テスト、アーキテクチャの適応度関数などの良い工学的実践をむしろ強化すべきである。

## テーマ 2: Rust は錆びていない

- Rust は、システムプログラミング言語の第一選択になりつつある。議論に上る道具の多くが Rust で書かれている。
- 古いシステムユーティリティの置き換えや、性能のための生態系の書き直しに使われる。Python の生態系にも Rust 製の速い代替 (uv、Ruff など) が出ている。
- 速さと、先行言語より落とし穴が少ないことで、開発者に好まれている。

## テーマ 3: WASM の着実な台頭

- WebAssembly (WASM) はスタック型仮想マシンのバイナリ命令形式で、複雑なアプリケーションをブラウザーのサンドボックス内で動かせる。
- 4 大ブラウザー (Chrome、Firefox、Safari、Edge) が WASM 1.0 に対応し、移植性の高いクロスプラットフォーム開発の実用的な配備先になってきた。

## テーマ 4: 生成 AI ツールのカンブリア爆発

- 言語モデルを支える技術の生態系が爆発的に広がった: ガードレール、評価、エージェント構築の道具、構造化出力のフレームワーク、ベクトルデータベース、クラウドサービス、可観測性の道具。
- 単純なテキストのプロンプトから、ソフトウェア製品としての工学へと移ったためである。多くの顧客で生成 AI の実用的な使い方が見られる。
- 2015 年ごろの JavaScript 生態系の爆発と同じく、この混沌とした成長はしばらく続くと予想している。

## See also

- [Thoughtworks Technology Radar Vol.31: Techniques](/references/ai/thoughtworks-technology-radar-vol-31/thoughtworks-radar-vol-31-techniques.md)
- [Thoughtworks Technology Radar Vol.31: Platforms](/references/ai/thoughtworks-technology-radar-vol-31/thoughtworks-radar-vol-31-platforms.md)
- [Thoughtworks Technology Radar Vol.31: Tools](/references/ai/thoughtworks-technology-radar-vol-31/thoughtworks-radar-vol-31-tools.md)
- [Thoughtworks Technology Radar Vol.31: Languages and frameworks](/references/ai/thoughtworks-technology-radar-vol-31/thoughtworks-radar-vol-31-languages-and-frameworks.md)
