---
type: guideline
title: 'Google Cloud 上の Claude Code の費用を管理し ROI を示す'
description: '管理、追跡、証明の 3 つの観点から、Google Cloud 上の Claude Code の費用統制と効果測定を進める手順の要点。'
tags: [knowledge, ai, claude-code, google-cloud, cost, roi, telemetry]
status: stable
sources:
  - id: claude-article
    resource: 'https://claude.com/ja/resources/articles/how-to-manage-costs-and-demonstrate-roi-for-claude-code-on-google-cloud'
generated: { by: claude-code/claude-sonnet-5-5, at: 2026-11-17T00:00:00Z }
verified: { by: claude-code/claude-sonnet-5-5, at: 2026-11-17T00:00:00Z }
stale_after: 2027-11-17T00:00:00Z
---

# Google Cloud 上の Claude Code の費用を管理し ROI を示す

Google Cloud 上で Claude Code を使う組織が、費用を抑え、効果を示すための進め方をまとめる。
内容は Anthropic の記事（2026-10-27 公開）[^claude-article] の要約である。
記事は「管理」「追跡」「証明」を循環させる枠組みで構成されている。

## 費用が増える理由

- Google Cloud 上の Claude は従量課金であり、請求は開発者の実際の利用量に比例する。
- Claude Code はファイルを読み、ツールを実行し、複数の手順で推論するため、チャットより 1 作業あたりのトークンが多い。
- トークン単価はモデルごとに違うため、作業に合うモデルを選ぶことが大きな調整点になる。

## 1. 管理する

方針は、開発者を制限するのではなく、ガードレールで導くことである。
記事は、費用の高いセッションはしばしば価値も高く、無駄はむしろ中間層にあると述べる。例は、定型作業での高価なモデルの使用や、不要な定期タスクの放置である。

Google Cloud の標準機能は次のとおり。

- プロジェクト単位の請求、予算とアラート
- 利用上限（プレビュー、手動で解除可能）
- BigQuery への出力
- モデル系統とリージョンごとの分あたりのクォータ
- 固定料金で容量を確保するプロビジョンドスループット

さらに「Claude apps gateway」を使うと、利用者単位で統制できる。

- 自社の GCP プロジェクト内で動かす自己ホスト型で、claude のバイナリに含まれる。
- Google Workspace などの ID プロバイダーでサインインするため、各リクエストに確認済みの ID が付く。
- ID プロバイダーのグループごとにモデルの許可リストを置き、サーバー側で強制する。
- 日次、週次、月次の費用上限を、ユーザー、グループ、組織に設定できる。グループと組織の上限は、共有の枠ではなく開発者ごとの既定値である。
- 既定のモデルを決める。多くの人は既定を変えないので効果が大きい、と記事は述べる。

上限に近づくと、CLI が 75% と 95% の時点で開発者に警告する。請求アラートは管理者向けである。
上限に達すると、期間が切り替わるか管理者が上限を上げるまで、ゲートウェイが HTTP 429 を返す。上限の変更は Admin API で自動化でき、例としてチケット運用に組み込める。

## 2. 追跡する

- Claude Code の OpenTelemetry のメトリクスとイベントで、スキル、プラグイン、エージェント、MCP サーバーごとの利用量と推定費用が分かる。OTLP で Google Cloud Monitoring などへ送れる。ゲートウェイで設定を一括配布すれば、各端末の設定が要らない。
- 環境変数 `OTEL_RESOURCE_ATTRIBUTES` でコストセンターなどのタグを付けて、部門別に配賦する。記事の例は `department=engineering,cost_center=eng-123` である。
- 請求データは Claude の SKU で絞って BigQuery へ出力できる。Cloud Monitoring のダッシュボードの雛形と、BigQuery に送る OTel のクイックスタート（開発者別とモデル別の費用などの SQL 例つき）が GitHub にある。
- ユーザーのプロンプトの記録は自動では行われない。機微な内容を含み得るため、明示的な有効化が必要である。

## 3. 証明する

効果は 3 つの観点で示す。

| 観点           | 見るもの                                                                             |
| :------------- | :----------------------------------------------------------------------------------- |
| 導入と利用     | 有効化したユーザー数、週次と日次の利用、定着、よく使う人（OTel から得る）            |
| 満足度         | 満足度、体感の時間短縮、出力への信頼、困りごと（導入前後の短いアンケートと継続的な聞き取り） |
| 影響           | 時間: PR の作成からマージまでの時間、レビュー時間。手間: PR あたりのレビュー往復、コメント数、手戻り。量: エンジニアあたりの PR、デプロイ頻度、完了した課題 |

- 影響の指標は出発点であり、検証済みの基準値ではない、と記事は断っている。
- 成果の単位は、ラベルやチケット ID、Claude の関与の有無などで種類を定めたマージ済み PR で数える。障害対応や移行のように PR にならない作業は、完了した場所で数える。
- Claude Code の標準指標には、提案の採用率、変更行数、コミット数、作成された PR 数、出力あたりの費用がある。PR 数は「Claude Code が作成した」数であり、マージされた数ではない。GitHub や GitLab、チケットのデータと突き合わせる。

## 進め方

1. 組織の既定値として、費用上限、既定のモデル、モデルの許可リストを決める。
1. コストセンターのタグ付きでテレメトリを有効にし、監視基盤へ送る。
1. Google Cloud の請求で予算とアラートを設定する。
1. 導入前に、サイクルタイム、レビューの手間、スループットの基準値を既存データから取る。
1. 導入前後に開発者へアンケートを取る。
1. 利用データがたまったら、役割やチームごとに上限と既定値を見直す。

## 注意

- 顧客事例は自己申告で、記事は検証していない。Fifth Dimension は月 30 万行超のコードと 98% の採用率、Delivery Hero は 100 コンポーネントの UI デザインシステムの再設計を数分で、と紹介されている。
- 記事に、費用の相場、価格、ROI の計算例はない。ダッシュボードの画像はサンプルデータである。

## See also

- [Code Review の一般提供で PR レビューを自動化する](/knowledge/ai/code-review-generally-available.md)
- [規制業種で Claude Code を展開する](/knowledge/ai/regulated-firm-claude-code-rollout.md)

[^claude-article]: [How to manage costs and demonstrate ROI for Claude Code on Google Cloud](https://claude.com/ja/resources/articles/how-to-manage-costs-and-demonstrate-roi-for-claude-code-on-google-cloud)（2026-10-27）
