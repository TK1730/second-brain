---
type: reference
title: 'atomRDF: 原子スケール計算材料科学のためのオントロジー基盤ナレッジグラフ'
description: atomRDF 公式ドキュメントの要約で、計算材料科学の原子構造とシミュレーションワークフローを OCDO オントロジーと RDF グラフで構造化・クエリする Python ライブラリの仕組みをまとめる。
tags: [knowledge-graph, rdf, ontology, materials-science, python, sparql]
status: stable
verified: { by: antigravity/gemini-4-argon, at: 2026-11-15T00:00:00Z }
stale_after: 2027-11-15T00:00:00Z
---

# atomRDF: 原子スケール計算材料科学のためのオントロジー基盤ナレッジグラフ

計算材料科学向けの Python ライブラリ `atomRDF` (旧称 `pyscal-rdf`) の公式ドキュメントおよび論文 (Guzmán et al., 2026, arXiv:2604.06230) に基づく要約である。
原子スケールの結晶構造・欠陥構造データとシミュレーションの計算ワークフローを、ドメインオントロジーに基づいて RDF (Resource Description Framework) ナレッジグラフとして構築・操作・SPARQL クエリするための仕組みを整理する。

## 概要

計算材料科学では、分子動力学 (MD) や密度汎関数理論 (DFT) などの多様なシミュレーションコードが使われており、入力構造・計算条件・出力物性のデータ形式がツールごとに分断されやすい。
`atomRDF` は、OCDO (Open Computational Materials Science Domain Ontologies / Conceptual Dictionary for Computational Materials Science) オントロジー群から自動生成された Pydantic データモデルを基盤とすることで、この課題を解決する。
研究者は複雑な RDF トリプルや SPARQL の詳細を最初から意識することなく、通常の Python オブジェクト、JSON / YAML ファイル、および RDF ナレッジグラフの間で情報を一切失わずに相互変換 (ロスレスなラウンドトリップ) を行うことができる。

## サポートするオントロジー体系 (OCDO)

`atomRDF` は、材料の結晶構造から格子欠陥、シミュレーション手法までを体系化した以下のオントロジー群を統合的にサポートしている。

| オントロジー略称 | 正式名称・対象領域 | 記述される主な概念・データ |
| :--- | :--- | :--- |
| CMSO | Computational Material Sample Ontology | 結晶構造、空間群、ブラベ格子、単位格子、格子定数、原子座標、化学種・元素組成などの材料サンプルの基本表現。 |
| CDCO | Crystal Defect Core Ontology | 結晶欠陥全般を扱うコアオントロジーであり、各種の具体的な欠陥オントロジーの上位概念を提供する。 |
| PODO | Point Defect Ontology | 空孔 (Vacancy)、格子間原子 (Interstitial)、置換原子 (Substitutional) などの点欠陥の記述。 |
| PLDO | Planar Defect Ontology | 結晶粒界 (Grain boundary) や積層欠陥 (Stacking fault) などの面欠陥の幾何学・構造情報の記述。 |
| LDO | Line Defect Ontology | 転位 (Dislocation) やバーガースベクトルなど、線欠陥に関する構造情報の記述。 |
| ASMO | Atomistic Simulation Methods Ontology | 原子間ポテンシャル、計算手法 (分子動力学・DFT など)、入出力パラメータ、引張試験や構造緩和などの計算ワークフロー、および W3C PROV ベースの計算来歴 (Provenance) の記述。 |

## 主な構成コンポーネントと API

ライブラリは、データモデル層とグラフ操作層を明確に分離した以下の主要コンポーネントで構成されている。

### 1. `KnowledgeGraph` クラス

- RDF トリプルストアを管理し、ナレッジグラフへのデータ追加、グラフ構造の可視化、SPARQL クエリの実行、および共有可能なアーカイブ形式でのエクスポート・インポートを担う中核クラスである。
- バックエンドのトリプルストアとして、インメモリストアのほか、高速な Rust 製 RDF ストアである Oxigraph や SQLAlchemy ベースの永続化ストアなどを用途に応じて選択できる。
- ドメイン固有の語彙を意識せずにクエリを組み立てられる補助機能や、計算結果の系譜 (どの構造からどのポテンシャル・手法でどの物性値が得られたか) を辿る機能を備える。

### 2. `System` クラス

- `AtomicSystem` Pydantic データモデルのラッパーとして機能する高水準クラスである。
- ASE (Atomic Simulation Environment)、pymatgen、LAMMPS などの材料科学で標準的なフォーマットのファイルを読み書きできる。
- 単位格子の生成、点欠陥・粒界などの欠陥構造の作成、ボロノイ解析や結晶構造解析などの処理を行い、その結果を `KnowledgeGraph` へ直接シリアライズして登録する役割を持つ。

### 3. `WorkflowParser` と `datamodels`

- `datamodels`: OCDO の各オントロジー定義から自動生成された Pydantic モデル群であり、型安全なバリデーションと JSON / YAML / RDF 間の双方向シリアライズを提供する。
- `WorkflowParser`: LAMMPS や各種ワークフロー管理ツールのシミュレーション出力ファイルをパースし、使用したポテンシャルや熱力学条件、計算結果の物性値を ASMO および PROV オントロジーに準拠した来歴 (Provenance) 付きでナレッジグラフへ自動登録する。

## See also

- [atomRDF Documentation (公式ドキュメント)](https://atomrdf.pyscal.org/en/latest/)
- [国内企業の AI × ナレッジグラフ活用事例: 因果推論と実装パターン](/references/ai/zenn-kg-japan-case-studies.md)
