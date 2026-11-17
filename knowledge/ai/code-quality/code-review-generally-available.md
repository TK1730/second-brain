---
type: guideline
title: 'Code Review の一般提供で PR レビューを自動化する'
description: 'Claude Code の Code Review の一般提供、レビューの深さ 3 段階、有効化の手順、Enterprise 向けクレジットの要点。'
tags: [knowledge, ai, claude-code, code-review, github]
status: stable
sources:
  - id: claude-article
    resource: 'https://claude.com/ja/resources/articles/code-review-is-now-generally-available'
generated: { by: claude-code/claude-sonnet-5-5, at: 2026-11-17T00:00:00Z }
verified: { by: claude-code/claude-sonnet-5-5, at: 2026-11-17T00:00:00Z }
stale_after: 2027-11-17T00:00:00Z
---

# Code Review の一般提供で PR レビューを自動化する

Claude Code の Code Review が、リサーチプレビューを終えて一般提供になった。その要点をまとめる。
内容は Anthropic の記事（2026-10-15 公開）[^claude-article] の要約である。対象は Claude Team と Enterprise の組織である。個人向けプランへの言及はない。

## 狙い

コーディングエージェントでコードを書く速度は上がったが、レビューは依然として詰まりやすい。
Code Review は、新しい PR に自動でレビューを付けて、この詰まりを減らす。Anthropic は自社の PR のレビューにも使っている。

## プレビューからの改善

- 速度: ほとんどのレビューが、プレビュー期間の約 3 倍の速さで終わる。所要時間は約 20 分から 6〜10 分になったとされる。
- 品質: 重要なバグをより多く見つける。問題の内容、起きる条件、直し方を数文で伝える。
- 柔軟性: 管理者がリポジトリごとにレビューの深さを選べる。「Quick」「Standard」（既定）「Deep」の 3 つである。
- プレビュー中の要望（不要な指摘を減らす、変更の大きさに見合った時間で終える）を反映した、と記事は述べる。

## 有効化の手順

1. 管理者が、Claude Code の設定で Code Review を有効にする。
1. GitHub アプリをインストールし、レビューの対象にするリポジトリを選ぶ。
1. 開発者は個別の設定が要らない。有効化後は、新しい PR に自動でレビューが走る。

詳細は Claude Code のドキュメントの Code Review の項にある。

## 料金とクレジット

- Team と Enterprise の通常の料金は、記事にない。
- 対象の Claude Enterprise 組織は、2027 年 1 月 15 日までに、少なくとも $10,000 分の Code Review クレジットを受け取れる。有効期限は受け取りから 30 日で、別途の利用規約が適用される。

## 注意

- 速度と品質の数値は Anthropic の自己申告で、測定方法や第三者の検証は示されていない。バグの検出率、サンプル数、比較条件もない。
- Quick と Deep の所要時間は記事にない。
- 組織の運用に組み込む設計（リスク別の承認、レビューの往復の上限など）は、別の記事が詳しい。

## See also

- [Claude Code チームのコードレビューを 7 層で設計する](/knowledge/ai/code-quality/claude-code-team-code-review.md)
- [Claude Security で継続スキャンと修正の追跡を運用する](/knowledge/ai/code-quality/claude-security-continuous-scanning.md)

[^claude-article]: [Code Review の一般提供を開始](https://claude.com/ja/resources/articles/code-review-is-now-generally-available)（2026-10-15）
