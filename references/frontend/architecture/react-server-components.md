---
type: reference
title: 'React: Server Components 要約'
description: 'React 公式ドキュメント「Server Components」の要約（サーバーなしでの利用、サーバーありでの利用、Context の Provider、対話性の追加、async コンポーネント）。'
tags: [react, rsc, server-components, client-components, suspense]
status: stable
verified: { by: claude-code/claude-sonnet-5-5, at: 2026-10-21T00:00:00Z }
stale_after: 2027-10-21T00:00:00Z
---

# React: Server Components 要約

React 公式ドキュメントのリファレンス「Server Components」（react.dev）の要約である。
外部資料の要約であり、最終的な根拠は原典を参照すること。
要点は「Server Components はバンドルの前に、クライアントとは別の環境で描画される」「ビルド時にもリクエストごとにも動かせる」「対話が要る部分は `"use client"` の Client Component と組み合わせる」の 3 つである。

## 概要

出典: Intro / How do I build support for Server Components?

- Server Components は、バンドルの前に、クライアントのアプリや SSR サーバーとは別の環境で、あらかじめ描画される新しい種類のコンポーネントである。
- この別の環境が、React Server Components の「サーバー」である。
- Server Components は、CI サーバーでビルド時に一度だけ動かすことも、Web サーバーでリクエストごとに動かすこともできる。
- React 19 の React Server Components は安定しており、マイナーバージョン間で壊れない。
- ただし、バンドラーやフレームワークが React Server Components を実装するための内部の API は semver に従わず、React 19.x のマイナーバージョン間で壊れることがある。
- バンドラーやフレームワークとして対応する場合は、React のバージョンを固定するか、Canary リリースを使うことを勧めている。

## サーバーなしの Server Components

出典: Server Components without a Server

- Server Components はビルド時に動かして、ファイルシステムの読み取りや静的な内容の取得ができるので、Web サーバーは要らない。
  例: コンテンツ管理システムの静的なデータを読む。
- Server Components がないと、静的なデータを Effect でクライアントから取得するのが一般的である。
  - 例の Markdown 表示では、`marked` と `sanitize-html` をクライアントに読み込む。
  - 描画のあとに取得が始まる。
  - ページの存続中に変わらない静的な内容のために、ユーザーが約 75K（gzip 後）のライブラリのダウンロードと解析と、2 回目のリクエストの待ち時間を負担する。
- Server Components なら、同じコンポーネントをビルド時に一度だけ描画できる。
  - ライブラリはバンドルに含まれない。
  - データは、アプリをビルドするときの描画中に読み込まれる。
- 描画結果は SSR で HTML にして CDN へ置ける。
- クライアントには元の `Page` コンポーネントも重いライブラリも見えず、描画結果だけが渡される。
- そのため、最初の読み込みから内容が見え、バンドルに重いライブラリが入らない。
- 例の `Page` は `async` 関数である。
  async コンポーネントは、描画の中で `await` できる Server Components の新機能である。

## サーバーありの Server Components

出典: Server Components with a Server

- Server Components は、ページのリクエストの間に Web サーバーで動かすこともできる。
- API を作らずに、データ層へ直接アクセスできる。
- アプリのバンドルの前に描画され、データと JSX を Client Components に Props として渡せる。
- Server Components がないと、動的なデータも Effect でクライアントから取得するのが一般的である。
  - 例では `Note` を描画したあとに `Author` が取得を始めるので、クライアントとサーバーの間で高くつくウォーターフォール（直列の待ち）が起きる。
- Server Components なら、コンポーネントの中でデータを読んで描画できる。
  - `Note` も `Author` も描画中にデータベースから読む。
  - `Author` は `Note` の後に読み込まれるが、データが近くにあれば速い。
- バンドラーが、データ、描画済みの Server Components、動的な Client Components をまとめてバンドルにする。
- 任意で、そのバンドルを SSR して、ページの最初の HTML を作れる。
- ブラウザには元の `Note` と `Author` は見えず、描画結果だけが送られる。
- Server Components は、サーバーから再取得して、データにアクセスし直して描画し直すことで動的にできる。
- この新しい構成は、サーバー中心の Multi-Page App の単純な「リクエストとレスポンス」の考え方と、クライアント中心の Single-Page App のなめらかな対話性を組み合わせ、両方の良いところを得られるとしている。

## Server Component での Context の Provider

出典: Rendering a context provider in a Server Component

- Server Components は Context を作れない。
- ただし、Client Component のモジュールから import した Context の Provider は描画できる。
- 手順は次のとおりである。
  1. `'use client'` を付けたファイルで、Context を作って export する。
  1. Server Component からそれを import して、Provider として描画する。
- Provider の内側で描画される Client Components は、[`use`](https://react.dev/reference/react/use) または [`useContext`](https://react.dev/reference/react/useContext) で値を読める。

```js
// user-context.js
'use client';
import { createContext } from 'react';

export const UserContext = createContext(null);
```

## Server Components への対話性の追加

出典: Adding interactivity to Server Components

- Server Components はブラウザに送られないので、`useState` のような対話の API は使えない。
- 対話性を足すには、`"use client"` を付けた Client Components と組み合わせる。
- Server Components を示すディレクティブはない。
  - `"use server"` が Server Components を示す、というのはよくある誤解である。
  - `"use server"` は Server Functions のためのディレクティブである。
  - ディレクティブの詳細は [Directives](https://react.dev/reference/rsc/directives) を参照する。
- 例では、Server Component の `Notes` が、状態で `expanded` を切り替える Client Component の `Expandable` を import する。
- 仕組みは次のとおりである。
  1. 最初に `Notes` を Server Component として描画する。
  1. バンドラーに、Client Component の `Expandable` のバンドルを作るよう指示する。
  1. ブラウザの Client Components には、Server Components の出力が Props として渡される。

## Server Components での async コンポーネント

出典: Async components with Server Components

- Server Components では、async/await でコンポーネントを書ける。
- async コンポーネントで `await` すると、React は中断し、Promise が解決するまで待ってから描画を再開する。
- これは、Suspense のストリーミングに対応して、サーバーとクライアントの境界をまたいで動く。
- サーバーで Promise を作り、クライアントで `await` することもできる。
  - 例の `Page` では、重要なデータの `note` をサーバーで `await` する。
  - 画面の下にある優先度の低い comments は、サーバーで Promise を開始するだけで `await` せず、`Suspense` で包んだ Client Component に渡す。
  - Client Component は `use` API で Promise を待つ。
  - クライアントで中断しても、`note` の描画は止まらない。
- async コンポーネントはクライアントでは対応していないので、Promise は `use` で待つ。

```js
// Client Component
'use client';
import { use } from 'react';

function Comments({ commentsPromise }) {
  const comments = use(commentsPromise);
  return comments.map((comment) => <p>{comment}</p>);
}
```

## See also

- [Server Components (React)](https://react.dev/reference/rsc/server-components)
