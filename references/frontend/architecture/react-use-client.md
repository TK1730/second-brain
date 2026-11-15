---
type: reference
title: 'React: use client 要約'
description: "React 公式ドキュメント「'use client'」の要約（ディレクティブの役割と注意点、クライアントのコードとして印を付ける仕組み、使うべき場面、シリアライズできる Props の型、使い方の例、サードパーティのライブラリ）。"
tags: [react, rsc, server-components, client-components, use-client]
status: stable
verified: { by: claude-code/claude-sonnet-5-5, at: 2026-10-21T00:00:00Z }
stale_after: 2027-10-21T00:00:00Z
---

# React: use client 要約

React 公式ドキュメントの「Reference > React Server Components > `'use client'`」の要約である。
外部資料の要約であり、最終的な根拠は原典を参照すること。
要点は「`'use client'` はモジュールとその推移的な依存をクライアントのコードとして印を付ける」「境界を引くのはレンダーツリーではなくモジュールの依存の木である」「Server Component から Client Component へ渡す Props はシリアライズできなければならない」の 3 つである。

## 概要

出典: `'use client'`（冒頭）

`'use client'` は React Server Components と一緒に使う。
どのコードをクライアントで動かすかを印付ける。

## ディレクティブの役割

出典: Reference > `'use client'`

- ファイルの先頭に `'use client'` を書くと、そのモジュールと推移的な依存がクライアントのコードになる。
- `'use client'` を付けたファイルを Server Component が import すると、対応するバンドラーは、その import をサーバーで動くコードとクライアントで動くコードの境界として扱う。
- `RichTextEditor` の依存である `formatDate` や `Button` は、`'use client'` を持たなくても、クライアントで評価される。
- 1 つのモジュールが、サーバーのコードから import されたときはサーバーで、クライアントのコードから import されたときはクライアントで評価されることがある。

注意点は次のとおりである。

- `'use client'` は、ファイルのいちばん先頭（import やほかのコードより上）に置く。
  コメントは前にあってよい。
  引用符は単引用符か二重引用符で、バッククォートは使えない。
- `'use client'` のモジュールを、ほかのクライアントで描画されるモジュールが import する場合、ディレクティブは効果を持たない。
- コンポーネントのモジュールが `'use client'` を持つなら、そのコンポーネントの使用は必ず Client Component になる。
  ただし、`'use client'` を持たないコンポーネントも、クライアントで評価されることはある。
  - コンポーネントの使用が Client Component になるのは、`'use client'` を持つモジュールで定義されているか、`'use client'` を持つモジュールの推移的な依存であるときである。
    それ以外は Server Component である。
- クライアントで評価するコードは、コンポーネントに限らない。
  クライアントのモジュールの部分木にあるコードは、すべてクライアントへ送られて動く。
- サーバーで評価されるモジュールが `'use client'` のモジュールから値を import するとき、その値は React のコンポーネントか、Client Component へ渡せる Props の値（シリアライズできるもの）でなければならない。
  それ以外の使い方は例外になる。

## クライアントのコードに印を付ける仕組み

出典: Reference > How `'use client'` marks client code

- Server Components を使うアプリは、既定でサーバーで描画される。
- `'use client'` は、モジュールの依存の木にサーバーとクライアントの境界を入れ、クライアントのモジュールの部分木を作る。
- 例では、`InspirationGenerator.js` の `'use client'` が、そのモジュールと推移的な依存（`FancyText.js`、`inspirations.js`）をクライアントのモジュールにする。
- 描画では、フレームワークがルートのコンポーネントをサーバーで描画し、レンダーツリーを進む。
  クライアントに印の付いたコードから import されたコードは、評価しない。
- サーバーで描画した部分のレンダーツリーはクライアントへ送られ、クライアントはダウンロードしたコードで残りを描画する。

用語は次のように定める。

- Client Component は、レンダーツリーの中でクライアントで描画されるコンポーネントである。
- Server Component は、レンダーツリーの中でサーバーで描画されるコンポーネントである。

例では、`App`、`FancyText`、`Copyright` はサーバーで描画される Server Component である。
`InspirationGenerator` と、その子の `FancyText` は Client Component である。

### FancyText が Server でも Client でもある理由

- 「コンポーネント」は、コンポーネントの定義（多くは関数）と、その定義の使用の 2 通りの意味で使われる。
- Server Component や Client Component と呼ぶときは、使用のほうを指す。
- Client Component になるのは、`'use client'` を持つモジュールで定義されたコンポーネントの使用か、Client Component の中で import されて呼ばれるコンポーネントの使用である。
  それ以外は Server Component である。
- `FancyText` の定義には `'use client'` がなく、使用が 2 つある。
  `App` の子としての使用は Server Component で、`InspirationGenerator` の下での使用は Client Component である。
- そのため `FancyText` の定義は、サーバーで評価され、クライアントにもダウンロードされる。

### Copyright が Server Component である理由

- `'use client'` が境界を定めるのは、レンダーツリーではなく、モジュールの依存の木である。
- `App.js` が `Copyright.js` を import して呼んでおり、`Copyright.js` には `'use client'` がないので、その使用はサーバーで描画される。
- Client Component は、JSX を Props として渡されることで、Server Component を描画できる。
  `InspirationGenerator` は `Copyright` を children として受け取る。
- `InspirationGenerator` のモジュールは `Copyright` のモジュールを直接 import せず、呼びもしない。
  `Copyright` は、`InspirationGenerator` が描画を始める前に、完全に実行される。
- コンポーネント同士の親子の描画の関係は、同じ描画環境を保証しない。

## `'use client'` を使う場面

出典: Reference > When to use `'use client'`

Server Component が既定なので、どこにクライアントの印を付けるかは、Server Component の利点と限界から判断する。
以下はサーバーで動くコード全般にも当てはまる。

Server Component の利点は次のとおりである。

- クライアントへ送って動かすコードの量を減らせる。
  クライアントがバンドルして評価するのは、Client のモジュールだけである。
- サーバーで動く利点を得られる。
  ローカルのファイルシステムにアクセスでき、データの取得やネットワークのリクエストの遅延が小さいことがある。

Server Component の限界は次のとおりである。

- 対話を扱えない。
  イベントハンドラはクライアントが登録して起動するもので、`onClick` などは Client Component でしか定義できない。
- ほとんどのフックを使えない。
  Server Component の出力は、クライアントが描画するコンポーネントの一覧のようなものである。
  描画の後にメモリに残らないので、自分の状態を持てない。

## シリアライズできる型

出典: Reference > Serializable types returned by Server Components

Server Component から Client Component へ渡す Props の値は、シリアライズできなければならない。
描画される環境が異なるため、データを渡すときには追加の配慮が要る。

シリアライズできる Props は次のとおりである。

- プリミティブ: string、number、bigint、boolean、undefined、null、symbol（`Symbol.for` でグローバルなレジストリに登録したものだけ）
- シリアライズできる値を含むイテラブル: String、Array、Map、Set、TypedArray と ArrayBuffer
- Date
- オブジェクト初期化子で作ったプレーンなオブジェクト（プロパティがシリアライズできるもの）
- Server Function である関数
- Client Component か Server Component の要素（JSX）
- Promise

サポートされないものは次のとおりである。

- クライアントのモジュールから export されていない、または `'use server'` で印を付けていない関数
- クラス
- 組み込みを除くクラスのインスタンスであるオブジェクトや、null プロトタイプのオブジェクト
- グローバルに登録されていない Symbol（例: `Symbol('my new symbol')`）

## 使い方

出典: Usage

### 対話と状態を持たせる

- `Counter` は `useState` とイベントハンドラを使うので、Client Component であり、先頭に `'use client'` が要る。
- 対話のない UI を描画するだけのコンポーネントは、Client Component にしなくてよい。
- 親の `CounterContainer` は、対話も状態もなく、サーバーのローカルファイルシステムを読むので、Server Component でなければならない。
- サーバー専用にもクライアント専用にも頼らず、どちらで描画されてもよいコンポーネントもある（`FancyText` など）。
  `'use client'` を付けなければ、Server Component から参照されたとき、ソースコードではなく出力がブラウザへ送られる。
- ただし、依存を含むソースコードに比べて HTML の出力が大きいなら、常に Client Component にするほうが効率的かもしれない。
  長い SVG のパスの文字列を返すコンポーネントが一例である。

### クライアントの API を使う

- Web ストレージ、音声や動画の操作、デバイスのハードウェアなど、ブラウザの API はクライアントでしか使えない。
- 例の `Circle` は DOM の API で `canvas` を操作するので、Client Component にする。

### サードパーティのライブラリを使う

次の React の API を使うサードパーティのコンポーネントは、クライアントで動かさなければならない。

- `createContext`
- `react` と `react-dom` のフック（`use` と `useId` を除く）
- `forwardRef`
- `memo`
- `startTransition`
- DOM の挿入やネイティブのプラットフォームのビューなど、クライアントの API を使う場合

- Server Components に対応済みのライブラリは、自分で `'use client'` を持っているので、Server Component から直接使える。
- 未対応のライブラリや、イベントハンドラなどクライアントでしか指定できない Props が要る場合は、サードパーティの Client Component と Server Component の間に、自分の Client Component のファイルを挟む必要があるかもしれない。

## See also

- [`'use client'` (React)](https://react.dev/reference/rsc/use-client)
