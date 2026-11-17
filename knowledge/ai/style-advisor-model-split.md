---
type: guideline
title: 'スタイリスト AI の事例に学ぶ、モデルの分業と回答範囲の固定'
description: 'J.Crew の Style Advisor の事例から、計画・試作・本番でモデルを分ける構成と、社内の専門知に回答範囲を固定する設計を整理する。'
tags: [knowledge, ai, claude, case-study, model-selection, grounding]
status: stable
sources:
  - id: claude-article
    resource: 'https://claude.com/ja/resources/articles/j-crew-style-advisor-with-claude'
generated: { by: claude-code/claude-sonnet-5-5, at: 2026-11-17T00:00:00Z }
verified: { by: claude-code/claude-sonnet-5-5, at: 2026-11-17T00:00:00Z }
stale_after: 2027-11-17T00:00:00Z
---

# スタイリスト AI の事例に学ぶ、モデルの分業と回答範囲の固定

衣料小売の J.Crew が公開した AI スタイリスト「Style Advisor」の事例から、AI 機能を作るときに使える 2 つの設計を取り出す。
内容は Anthropic の事例記事（2026-11-12 公開）[^claude-article] の要約である。
記事に売上や利用者数などの成果指標はなく、効果の大きさは分からない。

## 事例の概要

- 利用者が「ビーチウェディング用の服」のように要望を文章で伝えると、カタログ撮影に基づくコーディネート写真が返り、対話で絞り込める。
- コーディネート単位で買う、1 点から組み立てる、場面から選ぶ、スタイリストの考え方を得る、という使い方ができる。
- 米国内の女性向けと男性向けのスタイルで提供された。
- 今後は、嗜好や購入履歴に合わせた個別化と、市場や商品ラインの拡大を計画している。

## 設計 1: 段階ごとにモデルを分ける

| 段階           | 使ったモデル        | 役割                                             |
| :------------- | :------------------ | :----------------------------------------------- |
| 計画           | Fable 5.1           | スタイリストとしてどう推論すべきかを設計する     |
| 試作           | Opus 5.5（Claude Code） | 動くプロトタイプを作る                       |
| 本番化         | 自社のエンジニア    | プロトタイプを本番環境へ移す                     |
| 会話中の判断   | Sonnet 5.5          | 会話の各ステップで応答の進め方を決める           |
| 高速な補助処理 | Haiku 5.5           | 素早く的を絞った処理で応答速度を保つ             |

フロンティアモデルで体験を作り、より速く効率的なモデルで運用する、という分け方である。

## 設計 2: 回答範囲を社内の専門知に固定する

- すべての推奨は、社内のスタイリストが作ったルックから始まる。生成側に自由に服を組ませない。
- 提案が自社のスタイリング方針から外れにくくなり、回答の根拠を社内の資産にそろえられる。
- 社内の専門家の知見と、カタログなどの資産を結びつけ、AI の出力範囲をそこに限る構成は、他の業種の相談窓口にも使える。

## See also

- [Opus 5.5 をナレッジワークの日常モデルとして使う](/knowledge/ai/opus-5-5-knowledge-work.md)
- [どの Claude モデルで開発すべきか: Fable・Opus・Sonnet・Haiku の使い分け](/references/ai/claude-blog-which-claude-model-should-you-build-with.md)

[^claude-article]: [J. Crew brings its signature approach to styling to life with Claude](https://claude.com/ja/resources/articles/j-crew-style-advisor-with-claude)（2026-11-12）
