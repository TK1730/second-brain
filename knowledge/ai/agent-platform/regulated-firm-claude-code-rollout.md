---
type: guideline
title: '規制産業で Claude Code を全社展開するときの統制の作り方'
description: 'JPMorganChase の事例から、管理された環境での実行、認証情報の隔離、段階的な権限拡大、自動ゲートによる変更統制を整理する。'
tags: [knowledge, ai, claude-code, enterprise, governance, security, case-study]
status: stable
sources:
  - id: claude-article
    resource: 'https://claude.com/ja/resources/articles/jpmorganchase-expands-claude-code'
generated: { by: claude-code/claude-sonnet-5-5, at: 2026-11-17T00:00:00Z }
verified: { by: claude-code/claude-sonnet-5-5, at: 2026-11-17T00:00:00Z }
stale_after: 2027-11-17T00:00:00Z
---

# 規制産業で Claude Code を全社展開するときの統制の作り方

金融大手の JPMorganChase が Claude Code をエンジニア以外も含む全社へ広げた事例から、規制産業で AI エージェントを展開するときの統制の作り方を取り出す。
内容は Anthropic の事例記事（2026-11-09 公開）[^claude-article] の要約である。
記事に削減率や利用人数などの定量的な成果はなく、「速くなった」「厳密になった」は定性的な記述にとどまる。

## 広がった用途

- **エンジニアリング**: レガシーシステムの近代化。PR レビューや自己修復型など、チームごとのエージェント作り。
- **インフラ・運用**: 監視、アラート対応、根本原因分析。
- **セキュリティ**: 脆弱性の発見と修正。
- **プロダクト**: 要件を直接エンジニアリングのバックログに落とす。リスクと統制の評価、プログラム計画。
- **資産運用**: 業務、技術、プロダクトの専門家を小規模なチームにまとめ、顧客向けの投資ソリューションを作る。変更は、顧客に届く前により厳密なテストを通る。
- **アドバイザー向け**: コネクタ経由で、税務を考慮したポートフォリオ移行分析を日常業務に組み込む。

製品開発の多くはコードの外（調査、要件定義、設計、計画）で進むため、ナレッジワークへの利用も広がっている。

## 統制の作り方

1. **管理された環境で動かす**: 自社のインフラ上の、コンテナ型開発基盤の中で Claude Code を動かす。
1. **認証情報を渡さない**: エージェントが、社員の認証情報や社内システムへ直接アクセスしないようにする。
1. **権限を段階的に広げる**: 新しい Claude モデルは、社内の承認プロセスを通るまで誰も使えない。
1. **自動ゲートで変更を検査する**: 数千件の自動テストと承認ゲートがすべての変更を検査し、合格か停止かをパイプラインが強制する。
1. **自己承認を禁じる**: Claude は自分の作業を承認できない。本番変更には人が責任を持つ。

## 取り入れるときの観点

- 「何をさせるか」より先に、「どこで動かし、何に触れさせないか」を決める。
- 人の注意に頼る確認ではなく、パイプラインが機械的に止める仕組みにする。
- 規制の厳しい組織の要求は、他の組織にも使える統制の型になる。

## See also

- [Claude Managed Agents を自社環境で運用する](/knowledge/ai/agent-platform/self-hosted-managed-agents.md)
- [Claude Tag をスタートアップで使い始める](/knowledge/ai/products/claude-tag-for-startups.md)

[^claude-article]: [JPMorganChase expands Claude Code to more employees across the firm](https://claude.com/ja/resources/articles/jpmorganchase-expands-claude-code)（2026-11-09）
