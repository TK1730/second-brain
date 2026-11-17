---
type: guideline
title: 'Claude Managed Agents を自社環境で運用する'
description: 'Self-hosted Claude Managed Agents の構成、モデルリクエストの送信先、無人エージェントを守る 4 つのセキュリティ原則、利用開始の条件。'
tags: [knowledge, ai, claude, managed-agents, security, self-hosted]
status: stable
sources:
  - id: claude-article
    resource: 'https://claude.com/ja/resources/articles/self-hosted-claude-managed-agents'
generated: { by: claude-code/claude-sonnet-5-5, at: 2026-11-17T00:00:00Z }
verified: { by: claude-code/claude-sonnet-5-5, at: 2026-11-17T00:00:00Z }
stale_after: 2027-02-17T00:00:00Z
---

# Claude Managed Agents を自社環境で運用する

エージェント本体、認証情報、セッション履歴を自社のクラウドやオンプレミスで動かす「Self-hosted Claude Managed Agents」の要点をまとめる。
内容は Anthropic の記事「Operate Claude Managed Agents inside your security perimeter」（2026-11-12 公開）[^claude-article] の要約である。
プライベートベータの告知であり、仕様と提供条件は変わりうる。

## 何が変わったか

- Managed Agents は当初、Anthropic がインフラを運用するホスト型だった。
- 次に、コードを社内に置きたいチーム向けに、サンドボックスだけを自己ホストできるようになった。
- 今回は、ハーネス、サンドボックス、認証情報、セッション履歴を含むサービス全体を自己ホストできる。
- 背景には、エージェントが壊れたビルドの修正、リリースのテスト、アラートのトリアージを無人で行い、社内システムにも触れる必要が出てきたことがある。

## 構成

- 運用者が持つもの: Managed Agents サーバー、そのデータベース、シェルやファイル操作ツールを実行するワーカー。
- 開発者は、ホスト型と同じコア API でエージェントを作る。セッション履歴は自社のデータベースに保存される。
- Claude へのモデルリクエストの送信先は選べる。
  - Anthropic へ直接
  - Amazon Bedrock、Google の Agent Platform、Microsoft Foundry
  - 自社のゲートウェイ
- 組織で Zero Data Retention（ZDR）が有効なら、Claude へのリクエストには Messages API の通常の呼び出しと同様に適用される。
- 運用者は、サーバー、データベース、ワーカー、ネットワーク制御、シークレット管理に責任を持つ。

## 無人エージェントを守る 4 つの原則

人が逐一確認できないため、制限をアーキテクチャに組み込む。
記事は、次の 4 原則がホスト型、サンドボックスのみ自己ホスト、全体自己ホストのどれにも当てはまるとしている。

1. **頭と手を分ける**: ハーネス（頭）が Claude を呼び、サンドボックス（手）でエージェントのコードが動く。エージェントループ、セッション履歴、Vault の秘密情報はサンドボックスの外に置く。サンドボックスは、ツールが必要になったときだけ起動すればよい。
1. **認証情報をサンドボックスに入れない**: サンドボックス外のプロキシが、MCP ツールや API 呼び出しのリクエストに認証情報を付ける。自己ホストでは、自社のシークレットマネージャーに保存することもできる。
1. **ネットワークを制限する**: 環境ごとに許可するホストを決め、それ以外への通信を止める。ビルド修正エージェントなら、社内の git ホストとパッケージレジストリだけにする。サンドボックスを自己ホストするなら、同じ制限を自社のファイアウォールで設定する。
1. **すべてを記録する**: ツール呼び出しとその結果を含む全手順を記録し、OpenTelemetry でエクスポートして既存の監視ツールで見る。

## 利用開始

- プライベートベータである。Anthropic のアカウントチームに連絡してアクセスを申請する。
- 設定の詳細は、Claude Platform ドキュメントの self-hosted の章を読む。
- 一般提供の時期と料金は、記事に記載がない。

## See also

- [Claude Meetings（ベータ）を会議で使う](/knowledge/ai/products/claude-meetings.md)
- [Claude Tag をスタートアップで使い始める](/knowledge/ai/products/claude-tag-for-startups.md)

[^claude-article]: [Operate Claude Managed Agents inside your security perimeter](https://claude.com/ja/resources/articles/self-hosted-claude-managed-agents)（2026-11-12）
