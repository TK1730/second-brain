---
type: reference
title: 'React: Passing Data Deeply with Context 要約'
description: 'React 公式ドキュメント「Passing Data Deeply with Context」の要約（props の受け渡しの問題、Context の作り方と使い方、同じコンポーネントでの利用と提供、中間コンポーネントの通過、使う前の代替案、使いどころ）。'
tags: [react, context, hooks, props, prop-drilling]
status: stable
verified: { by: claude-code/claude-sonnet-5-5, at: 2026-10-21T00:00:00Z }
stale_after: 2027-10-21T00:00:00Z
---

# React: Passing Data Deeply with Context 要約

React 公式ドキュメント（Learn）の「Passing Data Deeply with Context」の要約である。
外部資料の要約であり、最終的な根拠は原典を参照すること。
要点は「Context は、親が下の木全体へ props を使わずに情報を渡す仕組みである」「作る・使う・提供するの 3 段階で使う」「使う前に props と children での受け渡しを検討する」の 3 つである。

## 概要

出典: 冒頭（You will learn）

- 通常、情報は props で親から子へ渡す。
  props は、間に多くのコンポーネントを挟むときや、多くのコンポーネントが同じ情報を必要とするときに、冗長で不便になることがある。
- Context を使うと、親コンポーネントが、下の木にある任意のコンポーネントへ情報を使えるようにできる。
  木の深さに関係なく、props で明示的に渡す必要はない。
- 学ぶ内容は次の 4 つである。
  - 「prop drilling」とは何か
  - 繰り返し props を渡す代わりに Context を使う方法
  - Context のよくある使いどころ
  - Context のよくある代替手段

## props で渡す場合の問題

出典: The problem with passing props

- props は、データを使うコンポーネントまで UI の木を通して明示的に渡す優れた方法である。
- しかし、props を木の深くまで渡す必要があるとき、または多くのコンポーネントが同じ props を必要とするときは、冗長で不便になる。
  最も近い共通の祖先が、データを必要とするコンポーネントから遠いことがある。
  そこまで state を持ち上げる（lifting state up）と、「prop drilling」と呼ばれる状況になりうる。
- Context は、props を渡さずに、データを必要とする木の中のコンポーネントへデータを「テレポート」させる方法として紹介されている。

## Context という代替手段

出典: Context: an alternative to passing props

- Context は、親コンポーネントが下の木全体にデータを提供できるようにする。
- 例は、サイズを表す `level` を受け取る `Heading` である。
  同じ `Section` の中の見出しは、いつも同じサイズにしたい。
  `level` を各 `<Heading>` に別々に渡す代わりに、`<Section>` に渡し、`<Heading>` からは取り除きたい。
- そのためには、`<Heading>` が、自分に最も近い `<Section>` の level を知る必要がある。
  子が、木の上のどこかからデータを「尋ねる」仕組みが要る。
  props だけではできない。
- Context を使うには、次の 3 つの手順を踏む。
  1. 作る（Create）。例では `LevelContext` とする。
  1. 使う（Use）。データを必要とする `Heading` が `LevelContext` を使う。
  1. 提供する（Provide）。データを指定する `Section` が `LevelContext` を提供する。
- 親は、遠い祖先であっても、その内側の木全体にデータを提供できる。
  近い子でも遠い子でも、同じように使える。

### 手順 1: Context を作る

出典: Step 1: Create the context

- Context は、コンポーネントから使えるように、ファイルから export して作る。
- `createContext` の引数は 1 つだけで、既定値（default value）である。
  例では最大の見出しを表す `1` を渡すが、オブジェクトを含め、どんな値でもよい。

```js
import { createContext } from 'react';

export const LevelContext = createContext(1);
```

### 手順 2: Context を使う

出典: Step 2: Use the context

- React から `useContext` フックを、自作の Context とともに import する。
- `Heading` は、`level` を props から読む代わりに、`useContext(LevelContext)` で Context から読む。
- `useContext` はフックである。
  `useState` や `useReducer` と同じく、コンポーネントの直下でだけ呼べる（ループや条件の中では呼べない）。
  `useContext` は、`Heading` が `LevelContext` を読みたいと React に伝える。
- `Heading` に `level` の props が要らなくなるので、JSX でも渡さなくてよい。
  代わりに `Section` が `level` を受け取る。
- この段階では、まだ期待どおりに動かない。
  Context を使っているが、提供していないためである。
  提供しない場合、React は `createContext` に渡した既定値を使う。
  例では `1` なので、すべての見出しが `<h1>` になる。

### 手順 3: Context を提供する

出典: Step 3: Provide the context

- `Section` は、子を Context のプロバイダで包む。
  「この `<Section>` の中のコンポーネントが `LevelContext` を求めたら、この `level` を渡す」という意味になる。
- コンポーネントは、UI の木の上で最も近い `<LevelContext>` の値を使う。
- 動きの流れは次のとおりである。
  1. `<Section>` に `level` の props を渡す。
  1. `Section` が、子を `<LevelContext value={level}>` で包む。
  1. `Heading` が、`useContext(LevelContext)` で、上にある最も近い `LevelContext` の値を尋ねる。
- 結果は元のコードと同じだが、各 `Heading` に `level` を渡さずに済む。

```jsx
<LevelContext value={level}>{children}</LevelContext>
```

## 同じコンポーネントで使い、提供する

出典: Using and providing context from the same component

- 各 `Section` に `level` を手で指定する必要は、まだ残っている。
- Context は上のコンポーネントの情報を読めるので、`Section` が上の `Section` の `level` を読み、`level + 1` を下へ渡せる。
- この変更で、`<Section>` にも `<Heading>` にも `level` の props を渡す必要がなくなる。
  `Heading` と `Section` の両方が `LevelContext` を読んで自分の深さを知る。
  `Section` は、子を `LevelContext` で包んで、その内側がより深い level であることを示す。
- この例は、入れ子のコンポーネントが Context を上書きする様子を目で見せるために、見出しの level を使っている。
  Context は、現在の配色テーマや、ログイン中のユーザーなど、サブツリー全体が必要とする情報なら何でも渡せる。

## 間のコンポーネントを通り抜ける

出典: Context passes through intermediate components

- Context を提供するコンポーネントと使うコンポーネントの間には、好きなだけコンポーネントを挟める。
  `<div>` のような組み込みのコンポーネントも、自作のコンポーネントも挟める。
- 同じ `Post` を 2 つの異なる入れ子の深さで描画しても、中の `<Heading>` は、最も近い `<Section>` から自動で level を得る。
  特別な処理は要らない。
- Context により、「周囲に合わせて適応する」コンポーネントを書ける。
  描画される場所（どの Context の中か）によって、表示が変わる。

### CSS の継承との類似

- Context の仕組みは、CSS のプロパティの継承に似ている。
  `<div>` に `color: blue` を指定すると、その内側の DOM ノードは、深さに関係なくその色を継承する。
  間の DOM ノードが `color: green` で上書きすれば、そこから内側は変わる。
- React でも、上から来る Context を上書きする唯一の方法は、異なる値のプロバイダで子を包むことである。
- CSS では、`color` と `background-color` のように、異なるプロパティは互いを上書きしない。
  同様に、異なる React の Context は互いを上書きしない。
  `createContext()` で作った Context は、それぞれ完全に独立していて、その Context を使う・提供するコンポーネントだけを結びつける。
  1 つのコンポーネントが、複数の異なる Context を使ったり提供したりしても問題ない。

## Context を使う前に

出典: Before you use context

- Context は使いたくなりやすく、使いすぎやすい。
  props を何階層か深く渡す必要があるからといって、その情報を Context に入れるべきとは限らない。
- 使う前に、次の代替案を検討する。
  1. まず props で渡す。
     コンポーネントが単純でなければ、十数個の props を十数個のコンポーネントに渡すことも珍しくない。
     面倒に感じるが、どのコンポーネントがどのデータを使うかがはっきり分かる。
     コードを保守する人にとって、props でデータの流れが明示されていることはありがたい。
  1. コンポーネントを取り出し、JSX を `children` として渡す。
     データを使わず、下へ渡すだけの中間コンポーネントを何層も通すなら、途中でコンポーネントの取り出しを忘れていることが多い。
     例えば `posts` を、それを直接使わない `<Layout posts={posts} />` に渡すのではなく、`Layout` が `children` を受け取り、`<Layout><Posts posts={posts} /></Layout>` と描画する。
     データを指定するコンポーネントと、それを必要とするコンポーネントの間の層が減る。
- どちらの方法でもうまくいかないときに、Context を検討する。

## Context の使いどころ

出典: Use cases for context

- テーマ（Theming）: ダークモードのように見た目を変えられるアプリでは、アプリの最上部に Context のプロバイダを置き、見た目を調整するコンポーネントがそれを使う。
- 現在のアカウント（Current account）: 多くのコンポーネントが、ログイン中のユーザーを知る必要がある。
  Context に入れると、木のどこからでも読める。
  複数のアカウントを同時に操作できるアプリでは、UI の一部を別のアカウントの値の入れ子のプロバイダで包むと便利なことがある。
- ルーティング（Routing）: 多くのルーティングの仕組みは、現在のルートを持つために内部で Context を使う。
  各リンクが、自分が有効かどうかを「知っている」のはこのためである。
  自作のルーターでも同じ方法を使える。
- 状態の管理（Managing state）: アプリが大きくなると、木の上のほうに多くの state ができ、離れた多くのコンポーネントがそれを変更したくなる。
  複雑な state を管理して離れたコンポーネントへ渡すために、reducer と Context を組み合わせて使うことが多い。
- Context は静的な値に限らない。
  次の描画で別の値を渡すと、React はそれを読む下のコンポーネントをすべて更新する。
  このため、Context は state と組み合わせて使われることが多い。
- 一般に、木の離れた部分にある複数のコンポーネントが同じ情報を必要とするなら、Context が役立つ目安になる。

## まとめ

出典: Recap

- Context は、コンポーネントが下の木全体へ情報を提供できるようにする。
- Context を渡す手順は次のとおりである。
  1. `export const MyContext = createContext(defaultValue)` で作って export する。
  1. 子コンポーネントで `useContext(MyContext)` フックに渡して読む。深さは問わない。
  1. 親から提供するには、子を `<MyContext value={...}>` で包む。
- Context は、間にあるどのコンポーネントも通り抜ける。
- Context により、「周囲に適応する」コンポーネントを書ける。
- Context を使う前に、props で渡すか、JSX を `children` として渡すことを試す。

## 演習

出典: Challenges（Replace prop drilling with context）

- 原典の演習は、`App` から `List`、`Place`、`PlaceImage` へと渡している `imageSize` の props を、Context に置き換えるものである。
- `Context.js` で `ImageSizeContext` を作って export する。
- すべてのコンポーネントから `imageSize` の props を取り除く。
- `List` を `<ImageSizeContext value={imageSize}>` で包んで値を渡し、`PlaceImage` で `useContext(ImageSizeContext)` で読む。
- 間のコンポーネントは、`imageSize` を渡さなくてよくなる。

## See also

- [Passing Data Deeply with Context (React)](https://react.dev/learn/passing-data-deeply-with-context)
- [原典の Markdown (react.dev リポジトリ)](https://raw.githubusercontent.com/reactjs/react.dev/main/src/content/learn/passing-data-deeply-with-context.md)
