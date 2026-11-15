---
type: reference
title: 'Next.js: Fetching Data 要約'
description: 'Next.js 公式ドキュメント「Fetching Data」の要約（Server Component でのデータ取得、ストリーミング、Client Component でのデータ取得、順次取得と並列取得、React.cache による再利用、プリロード）。'
tags: [nextjs, react, data-fetching, streaming, suspense]
status: stable
verified: { by: claude-code/claude-sonnet-5-5, at: 2026-10-21T00:00:00Z }
stale_after: 2027-10-21T00:00:00Z
---

# Next.js: Fetching Data 要約

Next.js の公式ドキュメント（App Router）の「Getting Started: Fetching Data」の要約である。
外部資料の要約であり、最終的な根拠は原典を参照すること。
要点は「Server Component は async 関数にして `fetch` や ORM で直接取得する」「遅い取得は `loading.js` や `<Suspense>` でストリーミングする」「Client Component では `use` API か SWR・React Query で取得する」の 3 つである。

## Server Component でのデータ取得

出典: Fetching data > Server Components

Server Component では、非同期 I/O ならなんでもデータ取得に使える。
代表は `fetch` API と、ORM またはデータベースである。

### fetch API

出典: Server Components > With the `fetch` API

コンポーネントを async 関数にして、`fetch` を `await` する。

```tsx
export default async function Page() {
  const data = await fetch('https://api.vercel.app/blog');
  const posts = await data.json();
  return <ul>{/* posts を描画する */}</ul>;
}
```

- React のコンポーネントの木の中で同じ `fetch` を呼ぶと、既定でメモ化される。
  Props を受け渡さなくても、データが要るコンポーネントの中で取得できる。
- `fetch` は既定ではキャッシュされず、完了するまでページの描画を止める。
  結果をキャッシュするには `use cache` ディレクティブを使う。
  最新のデータをリクエスト時にストリーミングするには、取得するコンポーネントを `<Suspense>` で包む。
- 開発中は、`fetch` の呼び出しをログに出せる（`logging` の設定）。

### ORM またはデータベース

出典: Server Components > With an ORM or database

Server Component はサーバーで描画されるため、認証情報とクエリのロジックはクライアントのバンドルに含まれない。
そのため、ORM やデータベースのクライアントで安全にクエリを実行できる。
ただし、リクエストの認証と認可は引き続き確認する必要がある。
サーバー側のデータアクセスを守る方法は、データセキュリティのガイドを参照する。

## ストリーミング

出典: Fetching data > Streaming

Server Component で取得したデータは、リクエストごとにサーバーで取得して描画する。
遅いデータ取得があると、すべて取得し終わるまでルート全体の描画が止まる。
ページを小さなチャンクに分け、サーバーからクライアントへ少しずつ送ることを、ストリーミングと呼ぶ。
初期表示の時間とユーザー体験を良くできる。

ストリーミングの方法は 2 つある。

1. ページを `loading.js` で包む。
1. コンポーネントを `<Suspense>` で包む。

ボットやクローラーには、ストリーミングせず、データ取得の完了を待って描画し終えたページを返す。

### loading.js

出典: Streaming > With `loading.js`

- ページと同じフォルダに `loading.js` を置くと、データ取得中、ページ全体をストリーミングできる。
- 画面移動の直後、ユーザーはすぐに layout とローディング表示を見られる。
  描画が終わると、新しい内容に自動で差し替わる。
- 内部では、`loading.js` は `layout.js` の中に入れ子になり、`page.js` とその子を `<Suspense>` の境界で自動的に包む。
- そのため、キャッシュされていないデータやランタイムのデータ（`cookies()`、`headers()`、キャッシュされない fetch など）に layout がアクセスすると、同じセグメントの `loading.js` には切り替わらない。
  layout の描画が終わるまで、画面移動が止まる。
- 対処は 2 つある。
  - そのアクセスを、フォールバック付きの専用の `<Suspense>` で包む。
  - データ取得を `page.js` に移し、`loading.js` に覆わせる。
- ルートのセグメントのストリーミングには `loading.js` が向くが、ランタイムやキャッシュされないデータへのアクセスの近くに `<Suspense>` を置くことが勧められている。

### Suspense

出典: Streaming > With `<Suspense>`

`<Suspense>` を使うと、ストリーミングする範囲を細かく決められる。
境界の外にあるページの内容はすぐに表示し、境界の中の内容（例: ブログ記事の一覧）は後から流し込める。

```tsx
<Suspense fallback={<BlogListSkeleton />}>
  <BlogList />
</Suspense>
```

### 意味のあるローディング表示

出典: Streaming > Creating meaningful loading states

- 即時のローディング表示とは、画面移動の直後にすぐ見せる代替の UI である。
- アプリが応答していると分かる、意味のある表示を設計することが勧められている。
  スケルトンやスピナー、またはカバー写真やタイトルなど、次の画面の小さいが意味のある一部を使える。
- 開発中は、React Devtools でローディング表示を確認できる。

## Client Component でのデータ取得

出典: Fetching data > Client Components

Client Component でデータを取得する方法は 2 つある。

1. React の `use` API
1. SWR や React Query などのコミュニティのライブラリ

### use API によるストリーミング

出典: Client Components > Streaming data with the `use` API

- Server Component でデータ取得を始め、その Promise を Props で Client Component に渡す。
  このとき、取得する関数を `await` しない。
- Client Component では、`use(posts)` で Promise を読む。
- `<Suspense>` で Client Component を包むと、Promise が解決するまでフォールバックが表示される。
- Promise は、Server Component で `await` して解決することも、Client Component で `use()` で解決することもできる。
  どちらで解決するかは、React のドキュメントが説明している。
- 1 つの Promise を多くの Client Component で共有するには、Props ではなく Context で渡す。

```tsx
// Server Component: await しない
const posts = getPosts();
return (
  <Suspense fallback={<div>Loading...</div>}>
    <Posts posts={posts} />
  </Suspense>
);
```

### コミュニティのライブラリ

出典: Client Components > Community libraries

- SWR や React Query は、キャッシュやストリーミングなどについて、それぞれ独自の動作を持つ。
- 例: SWR の `useSWR` は `data`、`error`、`isLoading` を返す。
  読み込み中とエラーの表示は、これらを見て分岐する。
- ブラウザから直接取得する方法、Server Component から初期データを渡す方法、ライブラリのキャッシュと Next.js のキャッシュの調整は、「Client-side data fetching」のガイドを参照する。

## 順次取得と並列取得

出典: Examples > Sequential data fetching / Parallel data fetching

### 順次取得

- 順次取得は、あるリクエストが別のリクエストのデータに依存するときに起こる。
  例: `<Playlists>` は、`getArtist()` が返す `artistID` が要るので、その後でしか取得できない。
- `<Suspense>` で、プレイリストを後から流し込める。
  それでも、アーティストのデータが届くまでは何も表示されない。
  ページ全体を `<Suspense>`（例: `loading.js`）で包めば、ローディング表示をすぐに出せる。
- 最初のリクエストはほかのすべてを止めるので、データ元が速く返せるようにする。
  それ以上速くできなければ、変化が少ないデータはキャッシュを検討する。

### 並列取得

- 並列取得は、ルートの中のリクエストを先に始め、同時に動かすことである。
- layout と page は既定で並列に描画されるので、各セグメントはできるだけ早くデータ取得を始める。
- 1 つのコンポーネントの中でも、`await` を続けて書くと順次になる。
  例: `getAlbums` は、`getArtist` が終わるまで待たされる。
- 並列にするには、先に関数を呼んで Promise を受け取り、`Promise.all` で待つ。
  リクエストは、`fetch` を呼んだ時点で始まる。
- `Promise.all` は、1 つでも失敗すると全体が失敗する。
  これを避けるには `Promise.allSettled` を使う。

```tsx
const artistData = getArtist(username);
const albumsData = getAlbums(username);
const [artist, albums] = await Promise.all([artistData, albumsData]);
```

## React.cache による再利用

出典: Examples > Reusing data with `React.cache`

- ORM やデータベースのクエリなど、`fetch` を使わないデータアクセスは、関数を `React.cache` で包む。
  同じリクエストの中で複数のコンポーネントが呼んでも、1 つの結果を共有する。
- 同じ引数（例: 同じ `id`）の呼び出しは、1 回のリクエストの中で同じメモ化された結果を返す。
- `React.cache` の有効範囲は現在のリクエストだけである。
  リクエストごとに別のメモ化の範囲を持ち、リクエストの間では共有されない。

```ts
export const getUser = cache(async (id: string) => {
  return db.query.users.findFirst({ where: eq(users.id, id) });
});
```

## データのプリロード

出典: Examples > Preloading data

- ほかの処理を待ってからコンポーネントが描画されると、入力が揃っていても、データ取得が遅れて始まる。
  プリロードは、リクエストを早く始めて、その処理と並行して進め、リクエストの連鎖（ウォーターフォール）を避ける。
- やり方は、ブロックする処理の前に、データ取得の関数を `await` せずに呼ぶ。
  そのあと、結果を使うコンポーネントで同じ関数を呼ぶ。
- 同じ呼び出しを重複排除する関数でなければならない。
  - `fetch` は、同一のリクエストが自動でメモ化される。
  - ORM やデータベースは、関数を `React.cache` で包む。
  - Cache Components では、関数に `'use cache'` を付ける。
    `cookies()` や `headers()` などのリクエスト API を読むなら、`'use cache: private'` を使う。
- 本番では、private な Cache Function の同じ呼び出しは、1 回のリクエストの中で同じ結果を再利用できる。
  リクエストをまたいでサーバーのキャッシュに結果を保存せずに済む。
- プリロードの関数は、データを使うコンポーネントの隣に置く。
  コンポーネントを動かしたり消したりするとき、依存を見つけやすくなる。

```tsx
export const preload = (id: string) => {
  void getItem(id);
};
```

呼び出し側では、別のブロックするリクエストの前に `preload(id)` を呼ぶ。
`checkIsAvailable()` の実行中も item のリクエストは進み、`<Item>` を描画するときは、同一の `fetch` が `preload()` で始めたリクエストを再利用する。

## See also

- [Fetching Data (Next.js)](https://nextjs.org/docs/app/getting-started/fetching-data)
