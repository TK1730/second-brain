---
type: guideline
title: 'Claude Code のクラウドセッションを使い分ける'
description: 'Claude Code のクラウドセッションの始め方、環境設定、GitHub 連携、ルーティン、制限事項と運用の習慣。'
tags: [knowledge, ai, claude, claude-code, cloud, github]
status: stable
sources:
  - id: claude-article
    resource: 'https://claude.dev/blog/claude-code-in-the-cloud/'
generated: { by: claude-code/claude-sonnet-5-5, at: 2026-11-17T00:00:00Z }
verified: { by: claude-code/claude-sonnet-5-5, at: 2026-11-17T00:00:00Z }
stale_after: 2027-02-17T00:00:00Z
---

# Claude Code のクラウドセッションを使い分ける

Claude Code を自分の PC ではなく専用の仮想マシン（VM）で動かす「クラウドセッション」の使い方をまとめる。
内容は Addy Osmani による記事（2026-10-06 公開）[^claude-article] の要約である。
ルーティンは研究プレビュー、プロジェクトは公開ベータ、セルフホスト環境はベータとされ、仕様は変わりうる。クラウドセッション自体はベータと明記されていないが、画面に研究プレビューの表示がある。

## 仕組み

- ローカルのセッションは、PC の作業ツリーと認証情報を使い、PC が止まれば止まる。
- クラウドセッションは、タスクごとに新しい VM を用意し、リポジトリを新しいブランチにクローンし、環境のセットアップを済ませる。終了時にプルリクエストにできるブランチが残る。
- 始め方は、claude.ai/code、モバイルアプリ、デスクトップアプリ、ターミナルの `claude --cloud`、Slack である。
- Pro、Max、Team、Enterprise に含まれ、別の計算料金はない。ただし使用量は Claude Code 全体の上限に数えられる。組織の所有者が有効化する必要がある場合がある。

## 実測例

記事は、サンプルの Node API で 3 つのセッションを 16 秒以内に並行して始めた。結果は著者の実測である。

| 作業             | 結果                                                              | 時間    |
| :--------------- | :---------------------------------------------------------------- | :------ |
| 不安定なテストの修正 | キャッシュ取得の競合を見つけ、テストではなくコードを直した。40 回連続で成功 | 約 65 秒 |
| API 文書の更新   | 全エンドポイントを curl で確かめ、5 件の誤りを直した              | 約 62 秒 |
| 構造化ログ化     | JSON 行形式に切り替え、テストを 5 件追加した                      | 約 87 秒 |

環境の再現に各回の約 3 分の 1 から半分強がかかった。通常は GitHub からのクローンで置き換わる。

## 使い方の要点

1. 先にローカルのコミットを push する。VM は GitHub からクローンする。タスクは、問題、完了の姿、証明の方法を書いた自己完結のチケットにする。
   - 例: `claude --cloud "Fix the flaky test. Prove it by running the suite 30+ times."`
1. 長く手間のかかる検証をクラウドに任せる。繰り返し実行、多数のコミットの二分探索、遅い結合テスト、実サーバーへの確認。VM ごとにプロセスとポートが別なので、並行しても衝突しない。
1. ローカルで計画し、クラウドで作り、ローカルで仕上げる。`claude --permission-mode plan` で計画を決めて push し、`claude --cloud` で実行し、`claude --teleport` でセッションを手元に引き取る。引き取りには、きれいな作業ツリーと push 済みのブランチが要る。
1. スマートフォンのアプリの Code タブから、開始、確認、指示、質問への回答ができる。
1. Claude GitHub App を入れると、CI バーの Auto-fix や `/autofix-pr` で、CI とレビューの指摘を直せる。明確なものは push し、曖昧なものは尋ねる。マージ競合は通知されないので、リベースを頼む。
1. ルーティンは、プロンプト、リポジトリ、コネクタ、環境を保存し、スケジュール（最短で 1 時間ごと）、HTTP エンドポイント、GitHub イベントで起動する。承認の確認なしに動き、既定で `claude/` 始まりのブランチへ push する。
1. 実行中のセッションへは `claude -p "..." --cloud <session-id>` で追加指示を送れる。

信頼できないコードを動かすときは、ネットワークを「None」にする。VM には SSH 鍵、クラウド CLI のセッション、ブラウザのプロフィールがない。ただし None でも Anthropic API は呼べるため、そこからデータが出る可能性は残る。

## 環境の設定

- 既定の環境は、信頼するネットワーク、環境変数なし、セットアップスクリプトなしで、JS、Python、Go、Rust の多くのリポジトリで動く。
- セットアップスクリプトは Claude の起動前に root で動く。終了コード 0 で、約 5 分以内に終わらせるとキャッシュされる。スクリプトや許可ホストの変更時と、約 7 日ごとにキャッシュが作り直される。
- `npm install` のような準備は `.claude/settings.json` の SessionStart フックに置ける。クラウド専用の手順には環境変数 `CLAUDE_CODE_REMOTE` で分ける。
- サービス（例: データベース）のプロセスはキャッシュに残らない。セッションごとか SessionStart フックで起動する。
- ネットワークは、Trusted（主要なレジストリ、GitHub、主要クラウドの SDK ホスト）、Custom（社内レジストリを追加）、Full（制限なし）から選ぶ。変更は約 1 分で実行中のセッションに届く。
- 環境変数はその環境を使う全員に見える。Pro と Max では、API 資格情報を VM の外で付与する方式も選べる。
- テストや実行のコマンドは CLAUDE.md に書く。個人の `~/.claude` は VM に届かない。チームのスキルは `.claude/`、MCP サーバーは `.mcp.json` に移す。

## GitHub 連携

2 つの権限は別物である。GitHub でのサインインは本人の識別だけで、Claude GitHub App のインストールがプライベートリポジトリの公開に当たる。

- 推奨は、claude.ai/connect-github で接続し、所有するアカウントか組織に App を入れる経路である。
- 代替は、`/web-setup` で `gh` のトークンを送る方法である。この場合、Auto-fix や GitHub トリガーは使えない（App が要る）。
- 一度きりなら、GitHub リモートのないリポジトリで `claude --cloud` を実行すると、バンドルがアップロードされる。push で戻せるのは、GitHub 接続に push 権限がある場合に限る。

よくある失敗は次のとおり。

- プライベートリポジトリが選択画面にない: 所有アカウントか組織に App が入っていない。
- 組織のリポジトリが出ない: SAML SSO の Authorize を飛ばしている。
- 毎回認証エラー: 組織が IP 許可リストを使っている。サポートに、Anthropic ホストのサービスを除外するよう頼む。

## 制限事項

- Console API キーやサードパーティのプロバイダーでは使えない。Zero Data Retention の組織は使えない。
- ローカルのデータを持つ DB、VPN 限定のサービス、GPU、スマートフォンのシミュレーター、ハードウェア、細かい見た目の確認はローカル向きである。
- VM の資源は約 4 vCPU、16 GB RAM、30 GB ディスクである。
- フォアグラウンドのコマンドは既定 2 分（最大 10 分）でタイムアウトし、その後さらに最大 30 分バックグラウンドで続く。`BASH_DEFAULT_TIMEOUT_MS` と `BASH_MAX_TIMEOUT_MS` で調整できる。
- アイドルの VM は回収される。大事な作業はコミットする。再開すると新しい VM で会話が復元される。
- 並行セッションは互いを知らず、ブランチが衝突しうる。1 つをマージしてから、次にリベースを頼む。5 並行ならプランの上限を約 5 倍の速さで消費する。ルーティンには時間あたりの上限があり、プロジェクトは 1 日 200 スレッドまで始められる。
- GitLab と Bitbucket はバンドルのアップロードのみで、push で戻せない。GitHub Enterprise Server は Team と Enterprise で対応する。
- トランスクリプトは Anthropic が保管し、保持はプランとモデル改善の設定による。セッションを削除するとデータも消える。Team、Enterprise、API では、組織が同意しない限りコードやプロンプトで学習されない。

## 運用の習慣

- 1 セッション 1 タスクにする。
- 完了の証拠を要求し、差分より先に要約を読む。
- 起動前に push し、長いタスクではこまめにコミットする。
- Team と Enterprise ではセッションの公開範囲を Team にし、レビューアーがトランスクリプトを読めるようにする。コミットの `Claude-Session` トレーラーから元のセッションに戻れる。

## See also

- [Claude Code で評価の設計と改善の反復を自動化する](/knowledge/ai/eval-design-and-hillclimbing.md)
- [Claude Code のモッドで画面と動作を拡張する](/knowledge/ai/claude-code-mods.md)

[^claude-article]: [Claude Code in the cloud: a field guide to cloud sessions](https://claude.dev/blog/claude-code-in-the-cloud/)（2026-10-06、Addy Osmani）
