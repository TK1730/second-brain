---
type: guideline
title: 'Claude Code のモッドで画面と動作を拡張する'
description: 'Claude Code のモッド（セッション内で動く小さなスクリプト）の構造、作り方、検証、共有方法と安全面の注意点。'
tags: [knowledge, ai, claude, claude-code, mods, plugin]
status: stable
sources:
  - id: claude-article
    resource: 'https://claude.dev/blog/getting-started-with-claude-code-mods/'
generated: { by: claude-code/claude-sonnet-5-5, at: 2026-11-17T00:00:00Z }
verified: { by: claude-code/claude-sonnet-5-5, at: 2026-11-17T00:00:00Z }
stale_after: 2027-02-17T00:00:00Z
---

# Claude Code のモッドで画面と動作を拡張する

Claude Code のセッション内で動く小さなスクリプト「モッド」の作り方と使い方をまとめる。
内容は Addy Osmani による記事（2026-10-01 公開）[^claude-article] の要約である。
記事はモッドをベータとは記していないが、API がリリース間で変わりうると警告している。

## モッドとは

- JavaScript か TypeScript の小さなファイルで、ターミナルでもデスクトップアプリでも動く。動作の観察、挙動の変更、独自の画面表示ができる。
- プラグインに入れたフックとして実装される。設定ファイルのシェルフックと違い、1 度読み込まれて常駐し、状態を持ち、イベントで更新される画面を描き、ペインを開く、プロセスを動かす、スラッシュコマンドやモデル向けツールを登録するといった呼び出しもできる。
- 必要な環境は Claude Code 2.1.287 以降で、既定で有効である。型定義はモッドの読み込みごとに `.claude-plugin/types/` へ書かれ、そのバージョンの正本になる。
- Claude Code 自身の AGENTS.md 対応や `/diff` ペインもモッドで作られている。ソースは `anthropics/claude-code` リポジトリの `mods/` にある。
- コードを書かずに、作りたいモッドを Claude Code に説明して作らせる方法もある。ホットリロードを許可すると、ターンの終了時に現れる。ただしそのセッションだけで読み込まれ、後で片づけられるため、残すならフォルダをコピーする。

## 構造

- プラグインフォルダに `.claude-plugin/plugin.json` と `hooks/hooks.json` を置き、後者が 1 つのモジュールを指す。
- モジュールは `register(on, options)` を公開し、`on(event, matcher?, hook)` でフックを足す。
- フックは `$`（`ui`、`session`、`state`、`fs`、`process`、`http`、`command` などの API）、`e`（イベント）、`next`（連鎖の次へ渡す）を受け取る。

ミドルウェアのように、3 つの動きができる。

| 動き   | 方法                                          | 用途               |
| :----- | :-------------------------------------------- | :----------------- |
| 観察   | `await next(e)` の後に調べる                  | ログ、計測         |
| 書き換え | `next({ ...e, command: safer })`            | 入力の変更         |
| 応答   | `next` を呼ばず `{ deny: "..." }` を返す      | 呼び出しの阻止や代行 |

イベントは、ツール呼び出し、プロンプト送信、ターンの開始と完了、セッションの開始と終了、スラッシュコマンド、`ui.render` などである。
モジュールは DOM も Node もない独自の実行環境で動き、外部への操作は全て `$` を通す。
この「サンドボックス」は JavaScript の実行環境の分離を指し、セキュリティ上の隔離ではない。公式ドキュメントはモッドを「サンドボックス化されない」と明記しており、`$.fs` や `$.process` はユーザーと同じ権限で動く（詳細は[モッドの権限と管理者設定](/knowledge/ai/claude-code-mods-security-admin.md)）。

## 例: Token Weather（約 80 行）

プロンプトの上に 1 行で、コンテキストの使用率に応じた天気、使用トークン数、直近ターンの推移を出す。

| 使用率    | 表示            |
| :-------- | :-------------- |
| 25% 未満  | Clear           |
| 25 から 49% | Cloudy        |
| 50 から 74% | Showers       |
| 75 から 89% | Storm         |
| 90% 以上  | Compact soon    |

手順は次のとおり。

1. プラグインのフォルダを作る。マニフェスト、フック定義、モジュール、型定義、テストを置く。
1. `ui.render` を `AbovePrompt` に対してフックし、`$.ui.resolve(e)` の部品（`Box`、`Text`）で画面を返す。`claude --plugin-dir ./token-weather` で起動すると、保存のたびにホットリロードされる。
1. `$.session.usage()` から `context.tokens`、`context.window`、`context.percent` を読む。`session.start` と、メインループの `turn.complete` で記録する（サブエージェントのターンは `e.agentId` で除く）。履歴は `$.state` に置く。ホットリロードのたびにモジュール変数は消えるためである。
1. 表示は、12 件の履歴、棒文字、`134.4k` のような短縮で描く。アンケート表示時は譲り、幅が 60 列以上のときだけ推移の棒を出す。絵文字ではなく幅が 1 の記号を使い、桁を揃える。
1. 検証する。`claude plugin validate ./token-weather` でマニフェストとモジュールを調べ、`claude plugin test ./token-weather` で `*.test.ts` をスタブの使用量データで走らせる。
1. 共有する。マーケットプレイスのフォルダに `.claude-plugin/marketplace.json` を置き、`claude plugin marketplace add ./my-mods`、`claude plugin install token-weather@my-mods --scope user` で入れる。

## ほかの例

- Blast Radius: `rm -rf`、`git reset --hard`、`git clean`、強制 push、データベースのマイグレーションなど危険な Bash を止め、変更される内容を見せて、進めるか中止かを選ばせる。ドライランは `$.process.run` に引数配列で渡す。選択待ちは短い `sleep` の繰り返しで行う。`$` の呼び出し中の時間は、フックの 10 秒の制限に数えられない。記事のデモでは `rm -rf build` が止まり、9 ファイル（1.1 MB）が並んだ。
- Replay Theater: ターン中の Edit と Write の前後の文面を記録し、`r` キーか `/replay` で差分を 1 つずつ見られるペインを開く。編集は止めず、観察だけを行う。

3 つ全てのコードは `anthropics/claude-code-playground` にある。

## 運用のコツ

- エディタ補完と `tsc` には、生成された型定義を使う。
- 画面部品の props は `e` ではなく `e.props` から読む。
- 状態は `$.state` に置き、ホットリロードに耐えさせる。
- 描画が検証で落ちるときは `claude --debug` で調べる。
- 各フックの処理時間は、1 回の呼び出しにつき 10 秒までである。

## 共有と安全面

- GitHub のリポジトリにマーケットプレイスのファイルを置き、利用者は `/plugin marketplace add your-org/my-mods`、`/plugin install token-weather@my-mods`、`/reload-plugins` で入れる。出てこなければ再起動する。claude.ai/directory/manage から Claude ディレクトリへの申請もできる。
- モッドは Claude Code の権限で動き、作者は Anthropic ではなく公開者である。入れる前にソースを読み、信頼できる入手元だけを使う。
- Blast Radius はコマンドの文字列を照合するため、`$(...)`、エイリアス、`rm` を呼ぶスクリプトで回避できる。安全網であって権限の仕組みではない。確実に止めるなら権限ルールを使う。

## See also

- [Claude Code のクラウドセッションを使い分ける](/knowledge/ai/claude-code-cloud-sessions.md)

[^claude-article]: [Getting started with Claude Code mods](https://claude.dev/blog/getting-started-with-claude-code-mods/)（2026-10-01、Addy Osmani）
