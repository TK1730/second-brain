---
type: guideline
title: 'Managed Agents と NVIDIA OpenShell でエージェントの実行環境を締める'
description: 'Claude Managed Agents の自己ホスト型サンドボックスと NVIDIA OpenShell による、エージェント実行の統制方針の要点。'
tags: [knowledge, ai, claude, managed-agents, security, sandbox]
status: stable
sources:
  - id: claude-article
    resource: 'https://claude.com/ja/resources/articles/giving-companies-more-control-over-their-ai-agents-with-nvidia'
generated: { by: claude-code/claude-sonnet-5-5, at: 2026-11-17T00:00:00Z }
verified: { by: claude-code/claude-sonnet-5-5, at: 2026-11-17T00:00:00Z }
stale_after: 2027-02-17T00:00:00Z
---

# Managed Agents と NVIDIA OpenShell でエージェントの実行環境を締める

Claude Managed Agents で、エージェントの実行環境を自社の管理下に置き、NVIDIA OpenShell で操作ごとに許可を絞る方針をまとめる。
内容は Anthropic の記事（2026-09-28 公開）[^claude-article] の要約である。ベンダー発表であり、セキュリティ効果は両社自身の説明で、数値や第三者評価は記事にない。
Managed Agents は公開ベータである。

## なぜ必要か

- エージェントは、クローンしたリポジトリ、Web ページ、ツール出力、インストールしたパッケージなど、信頼できない内容を扱う。そこに隠れた指示や有害なコードが含まれうる。
- 記事は、ハーネス、セッション状態、認証情報をサンドボックスの外に置き、サンドボックスを実行用の道具にとどめる構成が業界で主流になりつつあると述べる。Managed Agents はこの設計に従う。

## 構成

- 自己ホスト型サンドボックス: エージェントのループ（オーケストレーション、コンテキスト管理、エラー回復）は Anthropic 側にある。各セッションのツール呼び出しだけが、顧客が管理する環境（自社基盤またはサンドボックス事業者）で動く。
- コード、機密ファイル、パッケージ、データは、企業の境界の内側に残り、顧客のセキュリティと実行時の統制に従う。
- NVIDIA OpenShell: サンドボックスの実行基盤として使える、オープンソース（Apache 2.0）のソフトウェアである。明示的に許可されていない操作は拒否する。

## OpenShell が行うこと

- ツール呼び出しごとに確認し、ファイル、ネットワーク、データへのアクセスに規則を適用する。
- 規則はエージェントの外で強制され、許可と拒否の判断はすべて記録される。
- ポリシープローバーが、チームの規則のもとでエージェントが到達できる範囲を数学的に検証する。

## 進め方

1. 狭い権限から始める。
1. 判断ログを確認する。
1. Claude を使い、タスクに必要な最小限のアクセスへ規則を絞り込む。

## 事例

- Clay: GTM エンジニアリングのエージェント Sculptor を、外部ファイルストアのマウントやパッケージの随時導入ができるサンドボックスで動かす。
- Rogo: 規制の厳しい業界向けに、エージェントのコードを分離された microVM で動かし、コードとデータを自社の境界内に保つ。

## 補足

- NVIDIA は同日に Open Agent Safety Platform（AI セキュリティ向けのオープンな基盤と参照設計）を発表した。
- 自己ホスト型サンドボックスの文書と、サンドボックス事業者の設定用クックブックが案内されている。

## See also

- [Claude for Manufacturing で現場の下書き作業を任せる](/knowledge/ai/products/claude-for-manufacturing.md)

[^claude-article]: [Giving companies more control over their AI agents, with NVIDIA](https://claude.com/ja/resources/articles/giving-companies-more-control-over-their-ai-agents-with-nvidia)（2026-09-28）
