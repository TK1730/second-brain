---
type: guideline
title: 'Claude の Personal Finance で自分の口座データをもとに相談する'
description: 'Claude の Personal Finance（ベータ）でできること、接続方法、読み取り専用の範囲、プライバシーと利用条件の要点。'
tags: [knowledge, ai, claude, personal-finance, privacy, beta]
status: stable
sources:
  - id: claude-article
    resource: 'https://claude.com/ja/resources/articles/introducing-personal-finance-in-claude'
generated: { by: claude-code/claude-sonnet-5-5, at: 2026-11-17T00:00:00Z }
verified: { by: claude-code/claude-sonnet-5-5, at: 2026-11-17T00:00:00Z }
stale_after: 2027-02-17T00:00:00Z
---

# Claude の Personal Finance で自分の口座データをもとに相談する

銀行口座やカードを接続し、実際の残高と取引をもとにお金の質問をする機能「Personal Finance」の要点をまとめる。
内容は Anthropic の記事「Introducing Personal Finance in Claude」（2026-11-05 公開）[^claude-article] の要約で、製品発表の性格が強い。記事に精度の数値はない。

## できること

- 接続した残高と取引から、平易な言葉で答える。不慣れな金融用語も説明する。
- カテゴリ別の支出内訳を、接続した全口座にまたがって出す。
- 過去の月と比べ、今月の支出が普通かを確かめる。
- 重複請求、予期しない手数料、少しずつの値上げを、口座をまたいで探す。
- 給料日までに引き落とされる支払いと、残る資金を見通す。
- APR の説明や、一定期間に払った利息の合計を出す。
- 週次の支出グラフ、支払期限のカレンダー、調整できるダッシュボードなどの表示を作る。

## 範囲と姿勢

- 読み取り専用である。Claude はお金の移動、管理、投資をしない。
- 内容は教育目的で、投資助言ではない。
- 広告やスポンサー付きの推奨はない。Anthropic は自社のクレジットカード、ローン、貯蓄口座を提供しない。
- 記事は、Claude が間違えることがあるとして、数字の根拠となる取引を尋ね、重要な数字は銀行で確かめるよう勧める。

## 接続とプライバシー

- 口座は第三者サービスの Plaid で接続する。利用者が銀行へ直接サインインして読み取り専用の許可を出し、Claude は銀行のパスワードを受け取らない。
- Claude が見られるのは、接続した口座の銀行名、口座名、種類、下 4 桁、残高、与信枠、最大 2 年分の取引である。
- Personal Finance ハブでの会話は、モデルの学習に使われない。ハブの外の会話は通常のプライバシー設定に従う。
- 口座はいつでも接続解除でき、解除後は Claude がそのデータを見られない。

## 提供条件

- 状態: ベータ。記事の公開週から順次提供される。
- プラン: Pro、Max、Ultra。
- 地域: 米国のみ。

## 始め方

1. Claude のサイドバーから Personal Finance を開く。
1. Plaid で口座を 1 つ接続する。
1. 「この春の旅行は無理なく行けるか」「毎月いくら貯められるか」のような質問から始める。

詳しい手順とデータの扱いは、Help Center と Privacy Center にある。

## 今後

大きな金融判断では、Claude が資格を持つ専門家や規制下の事業者と連携するのがよい、と Anthropic は述べる。連携の方法を探っており、銀行や資産運用会社などの意見を募っている。

## See also

- [Claude for Manufacturing で現場の下書き作業を任せる](/knowledge/ai/products/claude-for-manufacturing.md)

[^claude-article]: [Introducing Personal Finance in Claude](https://claude.com/ja/resources/articles/introducing-personal-finance-in-claude)（2026-11-05）
