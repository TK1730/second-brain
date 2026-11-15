---
type: reference
title: 'Vitest: Browser Mode 要約'
description: 'Vitest 公式ドキュメント「Browser Mode」の要約（導入、設定、対応ブラウザ、実行方法、ヘッドレス、テストの書き方と部品の描画、制約）。'
tags: [vitest, browser-mode, testing, playwright, webdriverio]
status: stable
verified: { by: claude-code/claude-sonnet-5-5, at: 2026-10-21T00:00:00Z }
stale_after: 2027-10-21T00:00:00Z
---

# Vitest: Browser Mode 要約

Vitest の公式ドキュメント（Guide）の「Browser Mode」の要約である。
外部資料の要約であり、最終的な根拠は原典を参照すること。
要点は「テストをブラウザ内で実際に動かし、`window` や `document` などのブラウザのグローバルを使える」「プロバイダー（`preview`、`playwright`、`webdriverio`）の指定が必須」「同期ダイアログとモジュールの export への `vi.spyOn` には制約がある」の 3 つである。

## 概要

出典: Browser Mode

Browser Mode は、テストをブラウザ内でネイティブに実行する機能である。
`window` や `document` といったブラウザのグローバルにアクセスできる。
`expect`、`vi`、テストプロジェクト、型テストなどの一般的な API は、Getting Started のガイドを参照するよう案内されている。

## インストール

出典: Installation

- 手軽に始めるには、`vitest init browser` コマンドを使う。
  必要な依存関係のインストールと、ブラウザ用の設定の作成を行う。
- 手動で入れる場合も、プロバイダーの指定が常に必要である。
  選べるのは `preview`、`playwright`、`webdriverio` のいずれかである。
  - `preview` は、テストの見た目を確認するだけならこれで足りる（`@vitest/browser-preview`）。
  - `playwright` は `@vitest/browser-playwright`、`webdriverio` は `@vitest/browser-webdriverio` を入れる。
- CI でテストを動かすには、`playwright` か `webdriverio` が必要である。
  ローカルでも、どちらかに切り替えることが勧められている。
  `preview` はイベントを模擬するだけで、Chrome DevTools Protocol を使わないためである。
- どちらも使っていなければ、Playwright から始めることが勧められている。
  並列実行に対応しており、テストが速くなるためである。
  WebdriverIO は WebDriver プロトコルでローカルのテストを動かせる。

## 設定

出典: Configuration

Vitest の設定ファイルで `browser.enabled` を `true` にすると、ブラウザモードが有効になる。
少なくとも 1 つの `instances`（例: `{ browser: 'chromium' }`）が必要である。

```ts
import { defineConfig } from 'vitest/config';
import { playwright } from '@vitest/browser-playwright';

export default defineConfig({
  test: {
    browser: {
      provider: playwright(),
      enabled: true,
      instances: [{ browser: 'chromium' }],
    },
  },
});
```

- Vitest はポート `23315` を割り当てる。
  開発サーバーと衝突せず、並行して動かせる。
  変更は [`api`](https://vitest.dev/config/api) オプションで行う。
  ポートは、最初のブラウザを起動するとき（`api` や `ui` が有効なら起動時）に確保される。
- Vite を使ったことがなければ、フレームワークのプラグインを入れて設定に書く。
  フレームワークによっては追加の設定が要るので、その Vite 関連のドキュメントを確認する。
  原典には React、Vue、Svelte、Solid、Marko、Qwik の設定例がある。
- Node ベースのランナーで動かすテストが混ざる場合は、[`projects`](https://vitest.dev/guide/projects) オプションで設定を分ける。
  例として、`unit`（`environment: 'node'`）と `browser`（`browser.enabled: true`）の 2 つのプロジェクトを定義している。
  ファイル名の規約は例であり、従う必要はない。

## ブラウザの指定

出典: Browser Option Types

browser の指定はプロバイダーによって決まる。
`--browser` を渡しても、設定ファイルにブラウザ名がなければ失敗する。

- `webdriverio` は `firefox`、`chrome`、`edge`、`safari` に対応する。
- `playwright` は `firefox`、`webkit`、`chromium` に対応する。

## ブラウザの互換性

出典: Browser Compatibility

テストの実行に Vite の開発サーバーを使うので、[`esbuild.target`](https://vitejs.dev/config/shared-options.html#esbuild)（既定は `esnext`）で指定された機能だけが使える。
Vite の既定は、ネイティブの ES Modules、動的 import、`import.meta` に対応するブラウザである。
加えて、iframe 間の通信に `BroadcastChannel` を、ガベージコレクションを妨げずにモックを追跡するために `WeakRef` と `FinalizationRegistry` を使う。
結果として、次のバージョン以上が対象となる。

- Chrome 87 以上
- Firefox 79 以上
- Safari 15.4 以上
- Edge 88 以上

## テストの実行

出典: Running Tests

- ブラウザ名を指定すると、既定では `preview` でそのブラウザを起動してテストを動かす。
  `preview` を使わないときは `browser.provider` で指定する。
- CLI では `--browser=chromium` のようにブラウザを指定する。
  `--browser.headless` のように、ドット記法でもブラウザのオプションを渡せる。
- Vitest 3.2 以降は、設定に `browser` がないまま `--browser` を指定すると失敗する。
  その設定がブラウザ用か Node.js 用かを推測できないためである。
- 開発時は、ブラウザの UI が自動で開き、中央の iframe の中でテストが動く。
  ビューポートは、UI での選択、テスト内の `page.viewport`、[設定](https://vitest.dev/config/browser/viewport)の既定値のいずれかで決める。
- テストごとに DOM のスナップショットを取る別のデバッグ方法として、[Trace View](https://vitest.dev/guide/browser/trace-view) が案内されている。

## ヘッドレス

出典: Headless

- ヘッドレスは、ブラウザが UI なしでバックグラウンドで動くモードで、自動テストに向く。
  `headless` に真偽値を設定するか、CLI の `--browser.headless` で有効にする。
- ヘッドレスでは、UI は自動で開かない。
  UI を使いつつヘッドレスで動かすには、[`@vitest/ui`](https://vitest.dev/guide/ui) を入れて `--ui` を渡す。
- ヘッドレスは既定では使えず、`playwright` か `webdriverio` のプロバイダーが必要である。

## テストの書き方と部品の描画

出典: Examples

- 外部パッケージがなくても、`vitest/browser` の `page` を使ってテストを書ける。
  `render` で DOM を作り、`page.getByText` などで要素を探し、`await expect.element(...)` で検証する。
  入力は `locator.fill` で行う。
- 主要なフレームワーク向けに、部品を描画するパッケージが提供されている。
  - Vitest 側のもの: `vitest-browser-vue`、`vitest-browser-svelte`、`vitest-browser-react`、`vitest-browser-angular`。
  - コミュニティ製のもの: `vitest-browser-lit`、`vitest-browser-preact`、`vitest-browser-qwik`。
- 対応するパッケージがなければ自作してもよい。
  フレームワークの描画関数と `page.elementLocator` API を包む簡単なラッパーで、名前は `vitest-browser-` で始める。
- 検証には、`@testing-library/jest-dom` をフォークした DOM アサーションが組み込まれている。
  詳細は Assertions API（`/api/browser/assertions`）を参照する。
- クリックや入力などの操作には、`vitest/browser` の `userEvent` を使う。
  詳細は Interactivity API（`/api/browser/interactivity`）を、ユーティリティ全般は Context API（`/api/browser/context`）を参照する。
- 非対応のフレームワーク（Solid、Marko）には、`testing-library` のパッケージを使うことが勧められている。
  サンプルは [`browser-examples`](https://github.com/vitest-tests/browser-examples) リポジトリにもある。
- `@testing-library/user-event` を直接使うことは勧められていない。
  イベントを模擬するだけで、実際には発生させないためである。
  代わりに `vitest/browser` の `userEvent` を使う。
  プロバイダーに応じて、内部で Chrome DevTools Protocol か WebDriver を使う。

## 制約

出典: Limitations

### スレッドを止めるダイアログ

`alert`、`confirm`、`print` のようなスレッドを止めるダイアログは、ネイティブには使えない。
ページが止まり、Vitest がページと通信できなくなって、実行が固まるためである。
同期のポップアップ API を誤って使っても固まらないよう、Vitest は既定の戻り値を返すモックを用意している。
それでも、これらの Web API は自分でモックすることが勧められている（[Mocking](https://vitest.dev/guide/mocking)）。

### モジュールの export への spyOn

- Browser Mode は、ブラウザのネイティブな ESM でモジュールを配信する。
  モジュールの名前空間オブジェクトは封印されていて再設定できないので、インポートしたオブジェクトに `vi.spyOn` を呼ぶとエラーになる。
  Node.js のテストでは、Vitest が Module Runner を書き換えられるため、この制約はない。
- 回避策は、`vi.mock('./module.js', { spy: true })` である。
  モジュールのすべての export を、偽物に差し替えずにスパイする。
- export された変数をモックできる方法は、内部の値を変える関数を export することだけである。

```ts
vi.mock('./module.js', { spy: true });
vi.mocked(module.method).mockImplementation(() => {});
```

## See also

- [Browser Mode | Guide（Vitest）](https://vitest.dev/guide/browser/)
- [docs/guide/browser/index.md（GitHub）](https://github.com/vitest-dev/vitest/blob/main/docs/guide/browser/index.md)
