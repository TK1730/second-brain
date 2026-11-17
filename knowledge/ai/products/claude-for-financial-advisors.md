---
type: guideline
title: 'Claude for Financial Advisors で面談の準備と記録を任せる'
description: 'Claude for Financial Advisors の接続先、8 つのスキル、人の承認を前提とした運用、導入時の注意点の要点。'
tags: [knowledge, ai, claude, financial-advisor, plugin, connector]
status: stable
sources:
  - id: claude-article
    resource: 'https://claude.com/ja/resources/articles/claude-for-financial-advisors'
generated: { by: claude-code/claude-sonnet-5-5, at: 2026-11-17T00:00:00Z }
verified: { by: claude-code/claude-sonnet-5-5, at: 2026-11-17T00:00:00Z }
stale_after: 2027-11-17T00:00:00Z
---

# Claude for Financial Advisors で面談の準備と記録を任せる

ファイナンシャルアドバイザーの調査、面談準備、記録作成を支援するコネクタとスキルの一式「Claude for Financial Advisors」の要点をまとめる。
内容は Anthropic の記事（2026-09-14 公開）[^claude-article] の要約であり、製品発表の性格が強い。
記事は提供開始済みとしており、ベータやプレビューとは書いていない。

## 狙い

- 記事は Kitces の調査を引き、顧客との面談はアドバイザーの時間の約 6 分の 1 にすぎないと紹介している。残りは調査、準備、記録などの周辺作業である。
- 同じく EBRI の 2026 年調査を引き、米国の労働者の 4 割超が、金融や退職の助言を誰に聞けばよいか分からないと答えたとしている。
- 節約した時間を、既存顧客への対応と、これまで受け入れられなかった世帯への対応に回す、という位置づけである。
- 上の 2 つの数値は第三者の調査を Anthropic が引用したもので、調査方法は記事にない。製品自体の削減時間や精度の数値も記事にない。

## スキル

8 つのスキルがあり、各社の業務に合わせて、Anthropic の公開リポジトリのものをそのまま使うか改変できる。

| スキル                 | Claude が行うこと                                                           |
| :--------------------- | :-------------------------------------------------------------------------- |
| アドバイザーの導入     | ツールをつなぎ、最初の面談準備を実行する                                    |
| 面談前の準備           | 保有資産、最近の動き、前回の未了事項を 1 つのブリーフにまとめる             |
| 面談後のメモとフォロー | 文字起こしから顧客向け要約、お礼メール、CRM のタスクを作る                  |
| 見込み客の受け入れ     | 見込み客の情報を要約、アナリストへの引き継ぎメモ、次の手順のメモに整理する |
| 運用資産の再配分レビュー | 目標配分からの乖離や集中ポジションを見つけ、説明の下書きを作る              |
| 代替投資のブリーフ     | iCapital や Addepar から代替投資の保有を集め、面談の要約に統合する          |
| 不動産承継と税のブリーフ | 承継計画を口座名義や受益者と照合し、前年の税を確認し、食い違いを CRM タスクにする |
| コンプライアンスと AI 方針 | 追加レビューが要りそうな内容を設定した基準で検出し、レビュー手順や AI 統制の記録を支える |

## コネクタ

新しいコネクタは次の 11 である。

- Addepar、BlackRock、Charles Schwab、Envestnet、iCapital、Orion、SS&C Black Diamond、Wealthbox、Wealth.com、Vanguard、Zocks
- 取得できる情報は、ポートフォリオやパフォーマンス、保管機関の残高と取引、代替投資の NAV、CRM の顧客記録と面談履歴、遺言や信託の要約、会話から得た顧客の目標や出来事など、接続先ごとに異なる。
- 既存の Microsoft 365、Salesforce、DocuSign、Box、FactSet、S&P Global、Morningstar のコネクタと併用できる。

プラグインは、スキルとコネクタを 1 回のインストールで入れる。
案内に従って接続先を選べる。選べるのは BlackRock、Charles Schwab、Addepar、Envestnet、iCapital、Orion、Wealthbox、Wealth.com、Zocks である。

## 人が確認する設計

- 投資の推奨、顧客への連絡、コンプライアンス上の判断など規制対象の行為は、人のレビューと承認を前提とする。Claude はブリーフ、下書き、CRM や顧客への提案操作を用意するところまでを担う。
- コンプライアンスのスキルは、顧客向けの文言を SEC のマーケティング規則に照らして問題の可能性を指摘する。記事は、これを各社の統制の代わりではなく補助だと説明している。

## 導入時の注意

1. 登録投資顧問業者には Enterprise プランを勧めている。監査ログが記録保存を支えるためである。
1. Enterprise 以外は、フォームでライセンスを申請する。後日 Anthropic から連絡が来る。
1. 2026 年 9 月末までに新規ライセンスを申請した会社には、1 回限りの利用クレジットがある。金額は記事にない。
1. 各接続先の企業の声や運用資産の規模は、各社の自己申告であり、記事は検証していない。

## See also

- [Claude for Manufacturing で現場の下書き作業を任せる](/knowledge/ai/products/claude-for-manufacturing.md)
- [規制業種で Claude Code を展開する](/knowledge/ai/agent-platform/regulated-firm-claude-code-rollout.md)

[^claude-article]: [Claude for Financial Advisors](https://claude.com/ja/resources/articles/claude-for-financial-advisors)（2026-09-14）
