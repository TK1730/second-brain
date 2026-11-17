---
type: guideline
title: 'Claude Security で継続スキャンと修正の追跡を運用する'
description: 'Claude Security の継続監視、修正の自動追跡、脅威モデル、API 連携、公開ベータの条件と注意点の要点。'
tags: [knowledge, ai, claude, security, scanning, beta]
status: stable
sources:
  - id: claude-article
    resource: 'https://claude.com/ja/resources/articles/claude-security-now-scans-continuously-and-tracks-fixes'
generated: { by: claude-code/claude-sonnet-5-5, at: 2026-11-17T00:00:00Z }
verified: { by: claude-code/claude-sonnet-5-5, at: 2026-11-17T00:00:00Z }
stale_after: 2027-02-17T00:00:00Z
---

# Claude Security で継続スキャンと修正の追跡を運用する

コードの脆弱性を見つける Claude Security が、継続的なスキャンと修正の追跡に対応した。その要点をまとめる。
内容は Anthropic の記事（2026-10-21 公開）[^claude-article] の要約である。
Claude Enterprise 向けの公開ベータであり、機能や提供条件は変わる可能性がある。一般提供の時期は記事にない。

## 何が変わったか

これまでは、人が始めたときだけスキャンが走った。今回の更新で、コードの変更に自動で追従する。

1. プロジェクトを作り、リポジトリをつなぐ。Claude の GitHub アプリ（GitHub Enterprise Server を含む）か、GitLab などのアクセストークンを使う。
1. ブランチと対象範囲をリポジトリごとに選ぶ。
1. Claude が最初に詳細なスキャンを行い、その後は変更分を、リスクと複雑さの順に定期的にスキャンする。

1 つのプロジェクトに複数のリポジトリを入れると、サービスをまたぐ問題を見つけられる。記事の例は、クライアントが検証すべき入力をバックエンドが信用してしまう場合である。

## 修正の追跡

- 未解決の指摘を、変更されたコードと照合する。Claude Code で直しても、ほかの方法で直しても、修正済みになる。
- 後のスキャンで同じ問題が再発すれば、指摘は自動で再び開く。

## 文脈の与え方

- プロジェクトごとの知識ベースに、デプロイの形態、適用されるセキュリティ方針など、コードから分からない事情を書く。
- Claude がコードから脅威モデルを作る。チームがレビューして編集でき、以後のスキャンは、何を指摘する価値があるかの判断に使う。環境で緩和済みのリスクは除外できる。
- 深刻度はプロジェクトの脅威モデルに基づく。各指摘には、攻撃者が脆弱なコードにどう到達するかの説明が付き、攻撃経路の図が付くものもある。

## 連携とアクセス制御

- API で、プロジェクトと指摘の一覧と参照、指摘の解決と再オープン、プロジェクトとリポジトリの作成と管理ができる。個人アクセストークンの権限は、その人が持つ権限の範囲に限られる。
- Webhook で、新しい指摘を他のシステムへ通知できる。
- MCP コネクタとして Claude.ai と Claude Code で使える。1 つのセッションで、指摘の確認、修正の開始の依頼、解決済みの記録ができる。
- 管理者は、プロジェクトの閲覧、指摘の仕分け、プロジェクトの作成を誰に許すかを役割で分けられる。

## 提供条件

- 対象は Claude Enterprise で、管理者が管理コンソールで有効にし、利用者のアクセスを設定する。
- Claude のモデル群（Claude Mythos を含む）で動き、Cyber Verification Program へのアクセスは要らない。
- 2 か月間、月 $25,000 分の利用クレジットが無償で付く。対象は 2026 年 12 月 31 日までの利用である。詳しい条件はヘルプセンターにある。

## 注意

- 4 月のベータ以降、数千の組織が使い 100 万件超の脆弱性が見つかったという数字は、Anthropic の自己申告である。方法や内訳は記事にない。
- IonQ、Gusto、Vanta の声は顧客の感想であり、第三者の評価ではない。
- 誤検出率、検出精度、スキャン頻度の詳細、データの扱い、クレジット以外の価格は記事にない。

## See also

- [Code Review の一般提供で PR レビューを自動化する](/knowledge/ai/code-review-generally-available.md)
- [Claude Code チームのコードレビューの進め方](/knowledge/ai/claude-code-team-code-review.md)

[^claude-article]: [Claude Security は、継続的にスキャンを行い、修正内容を追跡するようになりました](https://claude.com/ja/resources/articles/claude-security-now-scans-continuously-and-tracks-fixes)（2026-10-21）
