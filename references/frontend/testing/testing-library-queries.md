---
type: reference
title: 'Testing Library: About Queries 要約'
description: 'Testing Library 公式ドキュメント「About Queries」の要約（クエリの種類、優先順位、screen、TextMatch と正規化、手動クエリ）。'
tags: [testing-library, testing, queries, accessibility, react]
status: stable
verified: { by: claude-code/claude-sonnet-5-5, at: 2026-10-21T00:00:00Z }
stale_after: 2027-10-21T00:00:00Z
---

# Testing Library: About Queries 要約

Testing Library の公式ドキュメント「Queries: About Queries」の要約である。
外部資料の要約であり、最終的な根拠は原典を参照すること。
要点は「クエリは get、query、find の 3 種類で、要素が見つからないときの動きと再試行の有無が違う」「優先順位は、全員が使える手段（role、ラベル、テキストなど）、セマンティックな属性、テスト ID の順」「`screen` を使うのが推奨される」の 3 つである。

## 概要

出典: Overview

クエリは、ページ上の要素を探すために Testing Library が提供するメソッドである。
種類（get、find、query）の違いは、要素が見つからないときにエラーを投げるか、Promise を返して再試行するかにある。
選ぶ対象によって、適したクエリは変わる。
セマンティックなクエリを使って、アクセシビリティに沿ってページをテストするための推奨は、優先順位の節にある。

- 要素を選んだ後は、Events API や user-event で操作を起こしたり、Jest と jest-dom で要素への検証を書いたりする。
- 要素は操作に応じて現れたり消えたりするので、DOM の変化は `waitFor` や `findBy` クエリなどの非同期 API で待てる。
- 特定の要素の子孫だけを探すには `within` を使う。
- 再試行のタイムアウトや、既定の testID 属性などは設定で変えられる。

```jsx
import { render, screen } from '@testing-library/react'; // (or /dom, /vue, ...)

test('should show login form', () => {
  render(<Login />);
  const input = screen.getByLabelText('Username');
  // Events and assertions...
});
```

## クエリの種類

出典: Types of Queries

単一の要素と複数の要素で、それぞれ 3 種類ある。

- 単一の要素
  - `getBy...`: 一致した要素を返す。
    一致が 0 件、または 2 件以上のときは、説明つきのエラーを投げる（複数を期待するなら `getAllBy`）。
  - `queryBy...`: 一致した要素を返す。
    一致が 0 件なら `null` を返すので、要素が存在しないことの検証に使える。
    2 件以上のときはエラーを投げる（それで良いなら `queryAllBy`）。
  - `findBy...`: 条件に合う要素が見つかると解決する Promise を返す。
    既定の 1000ms のタイムアウトまでに、要素が見つからない、または 2 件以上見つかると、Promise は拒否される（複数なら `findAllBy`）。
- 複数の要素
  - `getAllBy...`: 一致したすべての要素の配列を返す。
    0 件ならエラーを投げる。
  - `queryAllBy...`: 一致したすべての要素の配列を返す。
    0 件なら空の配列 `[]` を返す。
  - `findAllBy...`: 要素が見つかると、その配列に解決する Promise を返す。
    既定の 1000ms のタイムアウトまでに見つからなければ、拒否される。
- `findBy` は `getBy*` と `waitFor` を組み合わせたものである。
  最後の引数で `waitFor` のオプションを受け取る（例: `await screen.findByText('text', queryOptions, waitForOptions)`）。

| 種類            | 0 件   | 1 件 | 2 件以上 | 再試行 |
| :-------------- | :----- | :--- | :------- | :----- |
| `getBy...`      | エラー | 要素 | エラー   | なし   |
| `queryBy...`    | `null` | 要素 | エラー   | なし   |
| `findBy...`     | エラー | 要素 | エラー   | あり   |
| `getAllBy...`   | エラー | 配列 | 配列     | なし   |
| `queryAllBy...` | `[]`   | 配列 | 配列     | なし   |
| `findAllBy...`  | エラー | 配列 | 配列     | あり   |

## 優先順位

出典: Priority

指針となる原則（Guiding Principles）に基づき、テストはユーザーがコードを使う方法にできるだけ似せるべきだとされる。
そのうえで、次の優先順位が推奨される。

1. 全員が使えるクエリ。
   視覚とマウスで使う人にも、支援技術を使う人にも共通する体験を反映する。
   1. `getByRole`: アクセシビリティツリーに公開されているあらゆる要素を探せる。
      `name` オプションで、アクセシブルネームによる絞り込みもできる。
      ほとんどあらゆる場面で第一の選択肢とされる。
      これで取れないなら、UI がアクセシブルでない可能性がある。
      例: `getByRole('button', {name: /submit/i})`
   1. `getByLabelText`: フォームの入力欄に向く。
      ユーザーはラベルの文字で入力欄を見つけるので、その動きを再現する。
      第一の選択肢とされる。
   1. `getByPlaceholderText`: プレースホルダーはラベルの代わりにならない。
      ただし、それしかないなら、ほかの手段よりは良い。
   1. `getByText`: フォームの外では、テキストが要素を見つける主な手段である。
      div、span、段落などの、操作しない要素を探すのに使える。
   1. `getByDisplayValue`: 値が入力済みのページを操作するとき、フォーム要素の現在の値が手がかりになる。
1. セマンティッククエリ。
   HTML5 と ARIA に沿った選択子である。
   これらの属性の体験は、ブラウザーや支援技術によって大きく異なる。
   1. `getByAltText`: `alt` テキストを持てる要素（`img`、`area`、`input`、カスタム要素）を探す。
   1. `getByTitle`: title 属性は、スクリーンリーダーで一貫して読み上げられず、視覚で見る人にも既定では見えない。
1. テスト ID。
   1. `getByTestId`: ユーザーには見えず、聞こえない。
      role やテキストで探せない、または意味をなさない場合（例: テキストが動的）にだけ推奨される。

## クエリの使い方

出典: Using Queries

- DOM Testing Library の基本のクエリは、最初の引数に `container` を渡す必要がある。
- 多くのフレームワーク向けの実装は、描画時に container を結びつけた版を提供するので、container の指定は要らない。
- `document.body` を対象にするだけなら、`screen` を使う（`screen` の使用が推奨される）。
- クエリの主な引数には、文字列、正規表現、関数を渡せる。
  ノードのテキストの解釈を調整するオプションもある（TextMatch の節）。
- 各クエリのオプションは `queryOptions` として渡せる。
  使えるオプションは、クエリごとの文書（例: byRole の API）を参照する。

```js
import { screen, getByLabelText } from '@testing-library/dom';

// With screen:
const inputNode1 = screen.getByLabelText('Username');

// Without screen, you need to provide a container:
const container = document.querySelector('#app');
const inputNode2 = getByLabelText(container, 'Username');
```

## screen

出典: screen

- DOM Testing Library のクエリは、どれも最初の引数に `container` を取る。
- `document.body` 全体を探すことは多いので、すべてのクエリを `document.body` に結びつけた `screen` オブジェクトも提供される（`within` の機能を使っている）。
- React Testing Library などのラッパーも `screen` を再エクスポートしているので、同じように使える。
- `screen` を使うには、グローバルな DOM 環境が必要である。
  Jest では `testEnvironment` を `jsdom` にすると使える。
- テストを `script` タグで読み込むなら、`body` より後に置く。

## TextMatch

出典: TextMatch

クエリの多くは、`TextMatch` を引数に取る。
`TextMatch` は、文字列、正規表現、または `(content?: string, element?: Element | null) => boolean` の形の関数である。
関数は、一致なら `true`、不一致なら `false` を返す。

HTML が `<div>Hello World</div>` のとき、次は div が見つかる。

```javascript
screen.getByText('Hello World'); // full string match
screen.getByText('llo Worl', { exact: false }); // substring match
screen.getByText('hello world', { exact: false }); // ignore case
screen.getByText(/world/i); // substring match, ignore case
screen.getByText((content, element) => content.startsWith('Hello'));
```

次は見つからない。

- 文字列が全体として一致しない（`'Goodbye World'`）。
- 大文字・小文字が違う、大文字・小文字を区別する正規表現（`/hello world/`）。
- 実際は div なのに、span を探す関数。

### 精度

出典: TextMatch > Precision

`TextMatch` を取るクエリは、最後の引数に、文字列の一致の精度を変えるオプションの object も取る。

- `exact`: 既定は `true` で、全体の一致を、大文字・小文字を区別して判定する。
  `false` なら、部分一致で、大文字・小文字を区別しない。
  - 正規表現や関数の引数と一緒に使っても効果はない。
  - ほとんどの場合、文字列と `{exact: false}` の組み合わせより、正規表現のほうがあいまい一致を細かく制御できるので、正規表現が望ましい。
- `normalizer`: 正規化の動作を上書きする任意の関数。

### 正規化

出典: TextMatch > Normalization

- 一致を判定する前に、DOM Testing Library は DOM 内のテキストを自動的に正規化する。
- 既定では、前後の空白を削り、文字列の中で連続する空白を 1 つの空白にまとめる。
- これを止める、または別の正規化（例: Unicode の制御文字を除く）にするには、オプションに `normalizer` 関数を渡す。
  文字列を受け取り、正規化した文字列を返す関数である。
- `normalizer` を指定すると、組み込みの正規化は置き換えられる。
  組み込みの正規化は `getDefaultNormalizer` で取得でき、調整したり、自作の関数から呼んだりできる。
- `getDefaultNormalizer` のオプション。
  - `trim`: 既定は `true`。前後の空白を削る。
  - `collapseWhitespace`: 既定は `true`。内側の空白（改行、タブ、連続する空白）を 1 つの空白にまとめる。

```javascript
screen.getByText('text', {
  normalizer: getDefaultNormalizer({ trim: false }),
});
```

## 手動のクエリ

出典: Manual Queries

- Testing Library のクエリのほかに、通常の `querySelector` の DOM API でも要素を探せる。
- クラスや id で探す逃げ道として使うことは推奨されない。
  これらはユーザーには見えないためである。
- どうしても必要なら、testid を使う。
  非セマンティックなクエリへ頼ることを明示でき、HTML に安定した取り決めを作れる。

## 補助ツール

出典: Browser extension / Playground

- Chrome の拡張機能 Testing Playground は、要素の階層を開発者ツールで調べ、どう選ぶべきかの提案を出す。
- testing-playground.com では、自分の HTML に対して各クエリを試し、結果を視覚的に確かめられる。

## See also

- [Testing Library: About Queries](https://testing-library.com/docs/queries/about/)
- [原典の Markdown（testing-library-docs）](https://github.com/testing-library/testing-library-docs/blob/main/docs/queries/about.mdx)
