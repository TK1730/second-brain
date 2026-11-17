---
type: guideline
title: 'Claude for Manufacturing で現場の下書き作業を任せる'
description: 'Claude for Manufacturing プラグインのスキル、コネクタ、人が確認する設計、利用開始の手順の要点。'
tags: [knowledge, ai, claude, manufacturing, plugin, connector]
status: stable
sources:
  - id: claude-article
    resource: 'https://claude.com/ja/resources/articles/claude-for-manufacturing'
generated: { by: claude-code/claude-sonnet-5-5, at: 2026-11-17T00:00:00Z }
verified: { by: claude-code/claude-sonnet-5-5, at: 2026-11-17T00:00:00Z }
stale_after: 2027-11-17T00:00:00Z
---

# Claude for Manufacturing で現場の下書き作業を任せる

既存システムからデータを取り出し、見積書、品質レポート、サプライヤー向け依頼文の下書きを作るプラグイン「Claude for Manufacturing」の要点をまとめる。
内容は Anthropic の記事「Introducing Claude for Manufacturing」（2026-11-12 公開）[^claude-article] の要約であり、製品発表の性格が強い。
17 のスキルと 4 つのコネクタを持つ。

## 狙い

- 製造現場は、データ入力などの情報収集に多くの時間を使う。記事は、2025 年の Manufacturing Leadership Council の調査で製造業者の 79% がデータを手作業で入力していたと紹介している。
- Claude が確認者の手前まで作業を進め、見積担当は価格、品質技術者は改善策、技術者は最初に確認すべき点に集中できるようにする。

## スキル

17 のスキルが、営業、品質、オペレーション、サプライチェーン、設計、セットアップを対象とする。
単独の作業もあれば、複数の工程を順に実行するものもあり、最後は必ず人のレビューで止まる。
記事が挙げる例は次の 6 つである。

| 作業                 | Claude が行うこと                                                       |
| :------------------- | :---------------------------------------------------------------------- |
| 新規案件の見積       | 依頼文を読み、不足情報を洗い出し、類似案件と原価を比べ、見積を下書きする |
| 検査不合格の調査     | 不具合を記録し、過去の報告を検索し、原因候補を順位づけ、是正処置報告書を下書きする |
| 設備故障の診断       | センサーデータ、修理メモ、写真、マニュアルから原因候補を順位づけ、技術者に確認を委ねる |
| 別サプライヤーの調達 | 見積依頼を準備し、返ってきた見積を比べる                                |
| 設計案の比較         | Autodesk Fusion で既存モデルから案を生成し、目標値で採点し、判断メモを作る |
| 生産実績のレポート   | 生産量の目標対比、設備停止時間、停止と未達による損失額を 1 つにまとめる |

スキルは出発点であり、各社の業務に合わせて拡張できる。

## コネクタ

| コネクタ         | できること                                                                   |
| :--------------- | :--------------------------------------------------------------------------- |
| Autodesk Fusion  | 既存モデルから設計案を生成し、選ぶ前に多くの案を比べる                       |
| Infor            | 発注書や在庫を照会して、行動前に確認する                                     |
| Microsoft 365    | 共有フォルダや受信トレイから、手順書、サプライヤーのメール、レポートを 1 案件にまとめる |
| Oracle NetSuite  | 受注、在庫、製造工程、案件原価を参照し、実績に基づいて価格を決める           |

コネクタのないシステムでも、定期的に書き出したファイルを Microsoft 365 に保存すれば、Claude がそれをもとに見積や生産レポートを作れる。

## Infor での変更操作

- この記事のコネクタは Infor への照会までである。Infor が公開予定の独自プラグインと組み合わせると、Claude から変更もできる。
- 例: 鋼材の出荷が 2 週間遅れたとき、バイヤーが影響する顧客受注と他拠点の在庫を尋ねる。承認後、Claude が別の仕入先へ発注書を出し、影響する生産計画を再スケジュールする。
- Claude のアクセス権は、操作するバイヤー自身の Infor 権限に従う。

## 現場が主導権を持つ設計

- 各スキルは利用者のレビューで終わる。見積は担当者が確認して出し、是正処置は品質担当が検証する。
- 数値や主張は、元データや文書にリンクされ、確認できる。
- 設備は直接操作しない。プログラム可能な設備が計測値、設定、安全上の限界を標準形式で記述するための「Model Hardware Standard」を、Anthropic が研究プレビューとして開発している。これは本プラグインとは別の提供物である。

## 利用開始

1. Team または Enterprise プランを用意する。記事に価格の記載はない。
1. プラグインをインストールし、Claude に「Set us up.」と伝える。
1. Claude が使用システムを尋ね、コネクタを試し、完全には動かないスキルを報告する。

社内システムの相談は営業チームへ問い合わせる。

## See also

- [Claude Meetings（ベータ）を会議で使う](/knowledge/ai/products/claude-meetings.md)

[^claude-article]: [Introducing Claude for Manufacturing](https://claude.com/ja/resources/articles/claude-for-manufacturing)（2026-11-12）
