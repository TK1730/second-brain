---
type: guideline
title: 'Claude Code の effort を作業の難しさに合わせて使い分ける'
description: 'Claude Code の effort 設定の意味、レベル別の使いどころ、Terminal-Bench 3.0 での効果と限界の要点。'
tags: [knowledge, ai, claude-code, effort, benchmark]
status: stable
sources:
  - id: claude-blog
    resource: 'https://claude.dev/blog/spending-your-effort/'
generated: { by: claude-code/claude-sonnet-5-5, at: 2026-11-17T00:00:00Z }
verified: { by: claude-code/claude-sonnet-5-5, at: 2026-11-17T00:00:00Z }
stale_after: 2027-11-17T00:00:00Z
---

# Claude Code の effort を作業の難しさに合わせて使い分ける

Claude Code の effort 設定を、どの作業でどのレベルにするかの指針としてまとめる。
内容は Thariq Shihipar 氏の記事「Using Claude Code: Spending your effort」（2026-09-25 公開）[^claude-blog] の要約である。
数値は Anthropic の社内実行と筆者の個人実験によるもので、第三者の検証は受けていない。

## effort とは

- 作業の難しさに応じて、モデルがどれだけ計算量と判断を使うかを決めるつまみである。
- 高くすると、独立した検証や判断が増える。どのレベルでも、Claude は作業に妥当な形で取り組む。
- Claude Code では effort を変えてもプロンプトキャッシュは壊れない、と筆者は述べている。
- 速度だけでなく振る舞いが変わる。高いほど Claude が利用者に代わって決める事柄が増えるので、人が主導したい場面では注意する。
- 変更は `/effort` で行い、会話の途中でも切り替えられる。

## レベル別の使いどころ

| レベル | 向く作業                                                       |
| :----- | :------------------------------------------------------------- |
| low    | ブレインストーミング、スケッチ、小さな変更など、対話的な作業   |
| medium | 新機能の開発など、通常のソフトウェア開発の大半                 |
| high   | レガシーコードのバグ修正など、検証や境界ケースが重要な作業     |
| max    | 難題を人の介入なしで進める作業（アプリの一括構築、脆弱性探索） |

## 機能開発の進め方

1. 仕様を渡し、足りない点を Claude に聞き取らせる。
1. low で実装する。
1. 結果を見て、必要なら low で繰り返す。
1. 検証とテストは high で行う。

## effort が効く場面と効かない場面

- 効くのは、検証や境界ケースが成否を分ける領域である。高い effort は主に「ケースの見落とし」による失敗を減らす。
- 全体の方針の誤りや要件の読み違いは、effort を上げても残る。
- 仕様が詳細だと、effort ごとの出力の差は小さくなる。
- 規則集に沿う型の作業は、向上が最も小さい。

## 数値

筆者の個人実験は 1 回ずつの実行で、傾向を示す例にとどまる。

| 課題                                   | low    | medium | high   | max     |
| :------------------------------------- | :----- | :----- | :----- | :------ |
| 仕様が曖昧なフィットネスアプリ         | 1.5 分 | 4 分   | 11 分  | 67 分   |
| 詳細な仕様のフィットネスアプリ         | 16 分  | 22 分  | 33 分  | 79 分   |

Terminal-Bench 3.0（コミュニティ由来で、日常業務より野心的な課題が多い）の Fable 5.1 の結果は次のとおり。

- 1 レベルごとに合格率とトークン消費が増えた。各課題 5 回の試行である。
- 全体では、low が 370 試行中 140 合格（トークン中央値 73k）、max が 214 合格（同 222k）だった。
- 分野別の合格率（low から最高レベル）は、セキュリティが 64% から 87%、ハードウェアが 34% から 75%、ML が 54% から 73%、ソフトウェアが 43% から 56%、オペレーションが 12% から 22% だった。
- HTML サニタイザの課題は、low で 5 回中 1 回、xhigh で 5 回中 5 回合格した。高い effort では敵対的レビューやファジングまで行った。

## 数値の注意

- 失敗の分類は、モデルによる判定で近似である。
- セキュリティ課題はインターネットなしで実行したため、公開リーダーボードとは件数が一致しない。
- Fable 5.1 は本番の安全介入を外して実行している。
- 記事は、これらのモデルや機能がベータか一般提供かを述べていない。

## See also

- [Claude for Manufacturing で現場の下書き作業を任せる](/knowledge/ai/products/claude-for-manufacturing.md)

[^claude-blog]: [Using Claude Code: Spending your effort](https://claude.dev/blog/spending-your-effort/)（2026-09-25）
