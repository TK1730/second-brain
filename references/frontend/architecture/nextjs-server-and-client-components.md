---
type: reference
title: 'Next.js: Server and Client Components 要約'
description: 'Next.js 公式ドキュメント「Server and Client Components」の要約（使い分け、サーバーとクライアントでの描画の流れ、use client の境界、データの渡し方、組み合わせ方、Context、サードパーティの部品、サーバー専用コードの保護）。'
tags: [nextjs, react, rsc, server-components, client-components]
status: stable
verified: { by: claude-code/claude-opus-5-5, at: 2026-10-21T00:00:00Z }
stale_after: 2027-10-21T00:00:00Z
---

# Next.js: Server and Client Components 要約

Next.js の公式ドキュメント（App Router）の「Getting Started: Server and Client Components」の要約である。
外部資料の要約であり、最終的な根拠は原典を参照すること。
要点は「layout と page は既定で Server Component」「対話やブラウザの API が要るところだけ Client Component にする」「`'use client'` はモジュールの境界を宣言する」の 3 つである。

## Server Component と Client Component の使い分け

出典: When to use Server and Client Components?

layout と page は、既定で Server Component である。
サーバーでデータを取得して UI の一部を描画し、結果をキャッシュしてクライアントへ少しずつ送れる（ストリーミング）。

| 使う場面                                                                               | 使うもの         |
| :------------------------------------------------------------------------------------- | :--------------- |
| 状態とイベントハンドラ（`onClick`、`onChange` など）                                   | Client Component |
| ライフサイクルの処理（`useEffect` など）                                               | Client Component |
| ブラウザ専用の API（`localStorage`、`window`、`navigator.geolocation` など）           | Client Component |
| カスタムフック                                                                         | Client Component |
| データベースや API に近い場所でのデータ取得                                            | Server Component |
| API キーやトークンなどの秘密を、クライアントに見せずに使う                             | Server Component |
| ブラウザへ送る JavaScript を減らす                                                     | Server Component |
| First Contentful Paint（最初に内容が表示されるまでの時間）を良くし、内容を少しずつ送る | Server Component |

例: 投稿のデータを取得する `<Page>` は Server Component にし、取得したデータを Props で `<LikeButton>`（Client Component）に渡して、クリックの処理はそちらで行う。

## 描画の流れ

出典: How do Server and Client Components work in Next.js?

- サーバーでは、ルートのまとまり（layout と page）ごとに描画を分けて進める。
  - Server Component は、RSC Payload（React Server Component Payload）という特別なデータ形式に描画される。
  - Client Component と RSC Payload から、HTML を事前に描画する。
- RSC Payload は、描画した Server Component の木を小さく直列化したものである。
  Server Component の描画結果、Client Component を描画する位置とその JavaScript ファイルへの参照、Server Component から Client Component へ渡した Props を含む。
- 最初の読み込みでは、クライアントは次の順に動く。
  1. HTML で、すぐに操作できないプレビューを表示する。
  1. RSC Payload で、Client Component と Server Component の木を突き合わせる。
  1. JavaScript で Client Component をハイドレーションし（静的な HTML にイベントハンドラを付け）、操作できるようにする。
- 2 回目以降の画面移動では、RSC Payload を先読みしてキャッシュし、Client Component はサーバーで描画した HTML を使わず、クライアントだけで描画する。

## use client の境界

出典: Examples > Using Client Components / Reducing JS bundle size

- Client Component は、ファイルの先頭（import より上）に `"use client"` を書いて作る。
- `"use client"` は、サーバーとクライアントのモジュールの木の境界を宣言する。
  印を付けたファイルが import するものと、直接描画する部品は、すべてクライアントのバンドルに入る。
  そのため、クライアントで動かす部品のすべてに印を付ける必要はない。
- ただし、children などの Props として渡された Server Component は、Client Component のモジュールの木に入らない。
  それらはサーバーで描画され、描画結果として Client Component に渡される。
- クライアントの JavaScript を減らすには、UI の大きな範囲を Client Component にせず、対話が必要な部品を定義するファイルにだけ `'use client'` を付ける。
  例: layout は Server Component のままにし、その中の検索欄（`<Search>`）だけを Client Component にする。

## データの渡し方

出典: Examples > Passing data from Server to Client Components

- Server Component から Client Component へは、Props でデータを渡す。
- React の `use` API を使えば、データをストリーミングで渡すこともできる。
- Client Component へ渡す Props は、React が直列化できる値でなければならない。

## Server Component と Client Component の組み合わせ

出典: Examples > Interleaving Server and Client Components

- Server Component を、Props として Client Component に渡せる。
  これで、サーバーで描画した UI を、Client Component の中に入れ子で表示できる。
- よくある形は、`children` で Client Component に「差し込み口（スロット）」を作るものである。
  例: 表示の切り替えにクライアントの状態を使う `<Modal>` の中に、サーバーでデータを取得する `<Cart>` を入れる。
  親の Server Component（`<Page>` など）で、`<Cart>` を `<Modal>` の子として渡す。
- この形でも、Server Component は前もってサーバーで描画される。

## Context の Provider

出典: Examples > Context providers

- React の Context は Server Component では使えない。
- Context を使うには、`children` を受け取る Client Component（Provider）を作り、それを Server Component（layout など）から描画する。
- Provider は、木のできるだけ深い位置に置く。
  例では、`<html>` 全体ではなく `{children}` だけを包んでいる。
  Next.js が Server Component の静的な部分を最適化しやすくなる。

## サードパーティの部品

出典: Examples > Third-party components

- クライアント専用の機能に頼るサードパーティの部品は、Client Component の中で使えば動く。
- Server Component の中で直接使いたいときは、その部品を自分の Client Component（`'use client'` を付けて再 export するだけのファイル）で包む。
- 部品のライブラリを作る人は、クライアント専用の機能に頼る入口に `"use client"` を付けておくと、使う人が包まずに済む。

## サーバー専用のコードを守る

出典: Examples > Preventing environment poisoning

- JavaScript のモジュールは、Server Component と Client Component の両方から import できる。
  そのため、サーバー専用のコード（API キーを使う関数など）を、うっかりクライアントから import してしまうことがある。
- Next.js では、`NEXT_PUBLIC_` で始まる環境変数だけがクライアントのバンドルに入る。
  それ以外は空の文字列に置き換わるので、サーバー専用の関数をクライアントで動かしても、期待どおりには動かない。
- うっかり使うのを防ぐには、サーバー専用のコードを含むファイルで `server-only` パッケージを import する。
  Client Component から import すると、ビルドのときにエラーになる。
- 逆に、`window` を使うなどクライアント専用のコードには、`client-only` パッケージを使う。
- Next.js では、これらのパッケージを入れるのは任意である。
  Next.js が内部で扱い、間違った環境で使ったときに分かりやすいエラーを出す。

## See also

- [Server and Client Components (Next.js)](https://nextjs.org/docs/app/getting-started/server-and-client-components)
- [The Server and Client Boundary (Next.js)](https://nextjs.org/docs/app/guides/server-and-client-boundary)
