---
type: guideline
title: 'Claude for Nonprofits プラグインで非営利団体の業務を支える'
description: 'Claude for Nonprofits プラグインのスキル、割引、コネクタ、データの扱い、利用開始の手順の要点。'
tags: [knowledge, ai, claude, nonprofit, plugin, connector]
status: stable
sources:
  - id: claude-article
    resource: 'https://claude.com/ja/resources/articles/expanding-claude-for-nonprofits'
generated: { by: claude-code/claude-sonnet-5-5, at: 2026-11-17T00:00:00Z }
verified: { by: claude-code/claude-sonnet-5-5, at: 2026-11-17T00:00:00Z }
stale_after: 2027-11-17T00:00:00Z
---

# Claude for Nonprofits プラグインで非営利団体の業務を支える

非営利団体向けのプラグインと料金面の支援の要点をまとめる。
内容は Anthropic の記事「Expanding Claude for Nonprofits」（2026-10-26 公開）[^claude-article] の要約であり、製品発表の性格が強い。
数値は Anthropic の自己申告である。

## 提供内容

- Claude for Nonprofits プラグインは、約 30 の非営利団体と作ったスキルとコネクタの集まりである。団体の文脈と方針を Claude に設定し、調査から報告までの資金調達と日常業務を支える。
- 認証済みの非営利団体が Team または Enterprise プランを使う場合、プラグインは自動でインストールされ、追加費用はかからない。
- Anthropic は、米国の非営利団体に若手のフェローを配置する Claude Corps の拡大も計画している。Taproot と組み、経験豊富な専門家に短期のプロボノ支援を担ってもらう構想である。

## スキル

| 領域                 | できること                                                                         |
| :------------------- | :--------------------------------------------------------------------------------- |
| マーケティング       | 施策の計画、団体の語り口での下書き、内容のレビュー                                 |
| 採用と人事           | 面接ガイドと評価基準つきの求人票、90 日の入社計画、就業規則に基づく職員への回答   |
| 理事会と経営         | 不足スキルの分析、候補者への連絡、理事の導入資料、会議資料の企画                   |
| 資金調達             | 助成元と公募の探索（出典つき）、公募要領の適格性と競争力の評価、申請書と報告書の下書き（数値は出典つき）、助成元との面談の準備と事後のまとめ、礼状、寄付者への報告 |

## 最初に行うこと

- 団体の情報がどこにあるかを Claude に地図にさせる。寄付者データ、助成金のファイル、方針などの所在を把握し、まだ届かないツールの接続を提案する。他のスキルはこの地図に頼る。
- AI 方針の確認スキルで、ある使い方が団体自身の AI 方針で許されるかを職員が尋ねられる。

## 料金と支援

- 低中所得国の認証済み非営利団体は、標準の Team 席が 1 人あたり月 3 ドルで、約 90% の割引にあたる。9 月に国連総会に合わせて始まった。
- Team プランの最少人数が 2 人に下がった。
- 12 月の提供開始で、最大 75% の割引、Blackbaud、Candid、Benevity のコネクタ、GivingTuesday と作った無料の AI 活用講座が加わると記事は述べる。記事の日付からは、この 12 月がいつかを確認できない。
- 過去 1 年で、非営利向けプランは標準の Team と Enterprise と同じモデルを使えるようになり、Claude Code も追加費用なしで含まれる。
- 25,000 超の非営利団体が Claude を使い、75% 超が Claude の席数 10 未満である。
- 導入を支援するパートナーに、Accenture、BCG、Deloitte、Slalom などがある。

## データと管理

- 管理者が、利用者のアクセスと使えるコネクタを制御する。
- Anthropic は、既定では顧客のデータでモデルを訓練しない。
- セキュリティと法令順守の資料は Anthropic の Trust Center にある。Claude Academy に、データの扱いと AI 利用方針の作成と展開の講座がある。

## 利用開始

1. 認証済みの非営利団体が Team または Enterprise プランを用意する。まだ Claude を使っていない場合は、非営利向けのページでプランと価格を確認する。
1. 団体の情報の所在を地図にするよう Claude に頼む。
1. 管理者向け（11 月 10 日）と職員向け（11 月 12 日）のライブのウェビナー、または Claude Academy の非営利向け講座で学ぶ。
1. フィードバックのフォームで意見を送る。

## See also

- [Claude for Manufacturing で現場の下書き作業を任せる](/knowledge/ai/products/claude-for-manufacturing.md)

[^claude-article]: [Expanding Claude for Nonprofits](https://claude.com/ja/resources/articles/expanding-claude-for-nonprofits)（2026-10-26）
