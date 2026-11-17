---
type: guideline
title: 'Claude Marketplace で Anthropic の契約額を他社ツールに充てる'
description: 'Anthropic との契約の一部を Snowflake や Vercel など他社ツールの購入に回す仕組み、事例、条件の要点。'
tags: [knowledge, ai, claude, marketplace, procurement, snowflake, vercel]
status: stable
sources:
  - id: claude-article
    resource: 'https://claude.com/ja/resources/articles/how-coderabbit-power-digital-and-thoughtspot-scale-with-snowflake-and-vercel-on-claude-marketplace'
generated: { by: claude-code/claude-sonnet-5-5, at: 2026-11-17T00:00:00Z }
verified: { by: claude-code/claude-sonnet-5-5, at: 2026-11-17T00:00:00Z }
stale_after: 2027-02-17T00:00:00Z
---

# Claude Marketplace で Anthropic の契約額を他社ツールに充てる

Claude Marketplace で、Anthropic との契約の一部を第三者のツールの購入に回す仕組みと事例の要点をまとめる。
内容は Anthropic の記事（2026-09-23 公開）[^claude-article] の要約である。
記事の時点で、この購入方法は限定プレビューである。
提供元による紹介記事で、数値は企業側の申告とみられ、独立した検証は示されていない。

## 仕組み

- Anthropic との契約（コミットメント）がある企業は、その一部を Snowflake や Vercel など、すでに使っている他社ツールに充てられる。
- ツールごとの予算申請を避け、1 つの契約で日常のソフトウェアを多く賄うのが狙いである。
- 売り手の Snowflake と Vercel にとっては、Claude 上で開発する顧客に届き、契約のある顧客へ早い購入経路を示せる。

## 事例

| 企業          | 使い方                                                                                          |
| :------------ | :---------------------------------------------------------------------------------------------- |
| Power Digital | マーケティング代理店。顧客がデータをつなぐ基盤 Nova を Snowflake 上で動かし、Snowflake Cortex AI で顧客データ上の Claude を既存のガバナンスの下で使う。承認済みの予算を使い、Snowflake の契約をマーケットプレイス経由で拡大した |
| ThoughtSpot   | 分析基盤が Claude で動く。Snowflake の推論 API をマーケットプレイスで購入し、既存の Anthropic の契約を充てた。AI アナリスト Spotter は Claude のコネクタとして使える |
| CodeRabbit    | AI 生成コードの検証に Claude を使う。エージェントは Vercel Sandbox（作業ごとに Linux の microVM で隔離）で動き、Vercel Workflows で長い作業を管理する。従量課金から、拡大した Anthropic の契約で賄う確約プランへ移った |

記事にある数値は次のとおりで、いずれも申告である。

- Power Digital の利用は、1 月の約 12 人のエンジニアから、記事の時点で 800 人超へ広がった。
- CodeRabbit は、予算の承認から 1 週間以内にアップグレードが完了した。
- ThoughtSpot の利用量や成果の数値はない。

## 購入の手順

1. Anthropic との契約があることを確認する。
1. Anthropic のアカウント担当、またはマーケットプレイスの問い合わせフォームで、対象かどうかを確認する。
1. 対象になれば、契約の一部を Snowflake や Vercel などのパートナーツールへ充てる。

## 注意点

- 限定プレビューのため、対象になれるとは限らない。
- 既存の Anthropic の契約が前提である。
- 価格や割当の条件は記事に書かれていない。

## See also

- [Claude Meetings（ベータ）を会議で使う](/knowledge/ai/products/claude-meetings.md)

[^claude-article]: [How CodeRabbit, Power Digital, and ThoughtSpot scale with Snowflake and Vercel on Claude Marketplace](https://claude.com/ja/resources/articles/how-coderabbit-power-digital-and-thoughtspot-scale-with-snowflake-and-vercel-on-claude-marketplace)（2026-09-23）
