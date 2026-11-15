---
type: reference
title: '評価駆動開発 (EDD) とは何か: AI エージェントを継続的に改善する手法'
description: LangChain ブログの記事「What Is Eval-Driven Development? How to Improve AI Agents」の要約で、感覚的な確認に頼らず評価データセットと実験比較を軸にエージェントを開発する 3 段階のサイクルを説明する。
tags: [ai, agent, evaluation, edd, testing, langchain, langsmith]
status: stable
verified: { by: antigravity/gemini-4-argon, at: 2026-11-15T00:00:00Z }
stale_after: 2027-11-15T00:00:00Z
---

# 評価駆動開発 (EDD) とは何か: AI エージェントを継続的に改善する手法

LangChain ブログの記事 [What Is Eval-Driven Development? How to Improve AI Agents](https://www.langchain.com/blog/what-is-eval-driven-development) の要約。
確率的に動作する AI エージェントの開発において、開発者の感覚的な確認 (Vibe check) に頼るのではなく、評価 (Eval) を軸にして品質測定と改善サイクルを回す「評価駆動開発 (Eval-Driven Development: EDD)」の考え方と実践手順を解説している。

## 評価駆動開発 (Eval-Driven Development: EDD) の背景

- **TDD の AI エージェント版**: 評価駆動開発 (EDD) は、従来の決定論的なソフトウェア開発におけるテスト駆動開発 (TDD) に対応する AI エージェント開発手法である。
- **感覚的な確認 (Vibe check) の限界**: LLM や自律エージェントは確率的に振る舞い、入力のわずかな違いや複数ステップのツール呼び出しによって出力が変化するため、開発者が手元で数回試して「良さそうに見える」と判断するだけの感覚的な確認では、品質の実際の変化や他ケースでの退行 (リグレッション) を正確に捉えることができない。
- **Day 0 からの組み込み**: そのため EDD では、評価をリリース直前の後付けの品質チェックとして扱うのではなく、開発初日 (Day 0) の要件としてワークフローの中心に組み込む。

## EDD の中核となる 3 ステップ

EDD の開発サイクルは、以下の 3 つのステップを繰り返すことで進行する。

### 1. 「良い状態 (Good)」を定義する (Define What "Good" Looks Like)

- プロンプトやエージェントのコード、ツール定義を書き始める前に、そのエージェントが何を達成すれば成功なのかという明確な評価基準とベンチマークを定める。
- 正確性、フォーマット遵守、適切なツールの選択、レイテンシなど、ユースケースに応じた成功の定義を明文化する。

### 2. 実装の前に評価を書く (Write the Eval First)

- エージェントの挙動を実装・変更する前に、具体的なテスト入力例、期待される振る舞い、参照出力 (Reference output) から構成されるオフライン評価データセットを作成する。
- 評価が先に存在することで、以降のあらゆる実装変更が客観的に測定可能になる。

### 3. 変更を加えて実験を比較する (Make Changes and Compare Experiments)

- プロンプトの修正、ベースモデルの変更、ツール定義やアーキテクチャの調整などを行った各バリアントを、評価ハーネスを通じて同じデータセットに対して実行する。
- このとき、データセット全体の平均スコアを見るだけでなく、「個別サンプルごと (per example)」の差分を並べて比較し、あるケースの改善が別のケースのリグレッションを引き起こしていないかを確認する。

## エコシステムを支える 4 つの構成要素

LangSmith などの評価プラットフォームを用いて EDD を実践する際、以下の 4 つの構成要素がサイクルを支える。

| 構成要素 | 役割 |
| :--- | :--- |
| Datasets (データセット) | バージョン管理されたテスト入力と期待出力 (または参照情報) のコレクション。 |
| Experiments (実験) | 特定バージョンのエージェントをデータセットに対して実行し、測定可能な結果を記録する単位。 |
| Evaluators (評価器) | 決定論的ルールや LLM-as-a-judge を用い、最終回答や実行軌跡を自動採点する仕組み。 |
| Online Evaluation / Production Traces | 本番環境の対話ログから失敗ケースを検知し、オフラインデータセットへ還元するループ。 |

### Datasets (データセット)

- 典型的なユースケース、エッジケース、過去に失敗したケースを集めた、バージョン管理されたテスト入力と期待出力のコレクションである。

### Experiments (実験)

- 特定のコミットや設定を持つエージェントをデータセットに対して走らせ、出力・レイテンシ・トークン消費量・評価スコアを紐づけて記録する実行単位である。

### Evaluators (評価器)

- エージェントの出力を自動採点する仕組みであり、コードによる決定論的アサーション (正規表現、JSON スキーマ検証、完全一致など) と、LLM-as-a-judge (ルーブリックに基づく LLM の採点) を組み合わせて使う。
- 最終的な回答テキスト (Final Response) だけでなく、どのツールをどの引数で呼び出したかという単一ステップの評価や、解決に至るまでの実行軌跡 (Trajectory) 全体の妥当性も評価対象とする。

### Online Evaluation / Production Traces (本番トレースからの還元)

- オフラインのテストだけでは本番環境の多様なユーザー入力を網羅できないため、本番環境での実際の対話トレースや失敗モードをオンライン評価で継続的にトラッキングする。
- 本番で見つかった失敗ケースや想定外の振る舞いを抽出し、オフライン評価データセットの新しいテストケースとして継続的に追加することで、評価スイート自体を育てていく閉じたループを回す。

## See also

- [What Is Eval-Driven Development? How to Improve AI Agents (LangChain Blog)](https://www.langchain.com/blog/what-is-eval-driven-development)
- [AI ネイティブ SDLC プレイブック: 6 つのステージと成果物駆動の開発サイクル](/references/ai/claude-resources-the-ai-native-sdlc-playbook.md)
- [エージェントの各ステップを見張らずに済ませるループとグラフ](/references/ai/hanakoxbt-loops-and-graphs.md)
