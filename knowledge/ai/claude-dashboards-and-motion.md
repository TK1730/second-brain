---
type: guideline
title: 'Claude Dashboards と Motion でデータの可視化と説明動画を作る'
description: 'Claude Dashboards と Motion（いずれもベータ）の使い方、連携先、管理者設定、Claude Design 移行時の注意点。'
tags: [knowledge, ai, claude, dashboards, motion, artifacts]
status: stable
sources:
  - id: claude-article
    resource: 'https://claude.com/ja/resources/articles/dashboards-and-motion'
generated: { by: claude-code/claude-sonnet-5-5, at: 2026-11-17T00:00:00Z }
verified: { by: claude-code/claude-sonnet-5-5, at: 2026-11-17T00:00:00Z }
stale_after: 2027-02-17T00:00:00Z
---

# Claude Dashboards と Motion でデータの可視化と説明動画を作る

データに連動するダッシュボードと、アイデアから作る説明アニメーションを Claude に任せるときの要点をまとめる。
内容は Anthropic の記事（2026-10-08 公開）[^claude-article] の要約であり、製品発表の性格が強い。
Dashboards と Motion はベータ版なので、仕様は変わりうる。

## Dashboards（ベータ）

自然な言葉で質問すると、Claude が答えを導いてダッシュボードにまとめる。元データが変わると表示も更新される。

- 接続できるデータ基盤は Amazon Redshift、BigQuery、ClickHouse、Databricks、Snowflake、Salesforce などの CRM である。
- 各グラフに最終更新時刻が出る。数値をクリックすると元のクエリを確認でき、Claude に説明も頼める。
- 用例は「今週の登録数は先月より増えたか」の確認や、Salesforce の商談の要約である。
- Amplitude、Grafana、Hex、Mixpanel、Omni、Perplexity、PostHog、Sigma へ送って深掘りできる。Databricks Genie、Looker、monday.com、Tableau は近日対応予定とされる。
- 提供対象は有料プランである。

使うときは、結果を信じる前にクエリと更新時刻を見る。分析依頼のたびにチケットや SQL を挟まずに済むが、確認の手間を省いてはならない。

## Motion（ベータ）

プロンプトで説明したアニメーションを、Claude が短い動画として作る。入力欄で `/motion` を使って選ぶ。

- 用例は、四半期レポートの 30 秒の説明、役員会資料のグラフのアニメーション化、新規顧客向けの手順説明である。
- 編集可能なコード（文章、グラフ、図形、画像）で組み立てるため、文言、数値、タイミングを後から直せる。エディタか Claude への依頼で調整し、MP4 で書き出す。
- 動画生成モデルは使わない。生成された映像や AI 生成の人物は含まれない。
- Adobe、Descript、HeyGen、Higgsfield、invideo、Luma AI、Runway で続きを編集できる。Canva と Captions は近日対応予定とされる。
- 提供対象は Team と Enterprise プランである。

## Docs、Slides、Design（一般提供）

- ベータを終え、無料プランを含む全プランで一般提供になった。記事は、これまでに 4,500 万件を超える文書、プレゼン、デザインが作られたと述べている（Anthropic の自己申告）。
- Artifacts が CMEK に対応し、管理者が組織で使うテンプレートを選べる。
- チームメンバーと Claude が、同じ文書、スライド、デザイン、ダッシュボードを共同編集できる。
- 管理者が許可すれば、組織外への共有やリンクを知る全員への公開ができる。
- PowerPoint と PDF の書き出しがエディタの見た目を保つ。スライドは編集可能なファイルとして Google スライドへ送れる。モバイルアプリでも編集できる。

## 管理者の設定

- Dashboards と Motion は既定で無効である。組織設定の Artifacts で有効にする。
- Docs、Slides、Design は 10 月 15 日に自動で有効になる。それ以前でも手動で有効にできる。

## Claude Design の移行

- 単独サイト（claude.ai/design）は 12 月 14 日で終了する。9 月 16 日から Design はすべての会話内で使える。
- 管理者は Artifacts ページの「migrate team design system」で、組織のデザインシステムを一括移行できる。終了までは元のデザインシステムも変わらない。
- 単独サイトのチャットとプロジェクトのコメントは移行されず、終了後は見られなくなる。公開リンクも使えなくなる。必要なものは期日前に保存する。

## 利用開始の手順

1. Claude で、作りたいダッシュボードやアニメーションを説明する（例: 地域別の四半期売上、料金プランの説明）。
1. Dashboards ではデータソースや CRM を接続する。
1. グラフの裏のクエリと更新時刻で結果を確認する。
1. Motion はエディタか依頼で直し、MP4 に書き出す。
1. Claude Design の単独サイトを使っていた場合は、12 月 14 日までに必要なチャットとコメントを保存する。

## See also

- [Claude for Manufacturing で現場の下書き作業を任せる](/knowledge/ai/claude-for-manufacturing.md)

[^claude-article]: [Creating data-linked dashboards and explainer animations with Claude](https://claude.com/ja/resources/articles/dashboards-and-motion)（2026-10-08）
