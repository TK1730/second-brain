---
type: reference
title: 'React: Sharing State Between Components 要約'
description: 'React 公式ドキュメント「Sharing State Between Components」の要約（state を共通の親へ持ち上げる 3 つの手順、制御されたコンポーネントと制御されていないコンポーネント、state ごとに 1 つの情報源）。'
tags: [react, state, lifting-state-up, controlled-components]
status: stable
verified: { by: claude-code/claude-sonnet-5-5, at: 2026-10-21T00:00:00Z }
stale_after: 2027-10-21T00:00:00Z
---

# React: Sharing State Between Components 要約

React 公式ドキュメント（Learn）の「Sharing State Between Components」の要約である。
外部資料の要約であり、最終的な根拠は原典を参照すること。
要点は「2 つのコンポーネントの state を常に一緒に変えたいときは、state を共通の親へ移し、props で渡す」「この操作を state の持ち上げ（lifting state up）と呼ぶ」の 2 つである。

## state の持ち上げとは

出典: Sharing State Between Components（冒頭）

- 2 つのコンポーネントの state を、常に一緒に変えたいことがある。
- そのときは、両方から state を取り除き、最も近い共通の親へ移し、props で渡す。
- この操作を lifting state up（state の持ち上げ）と呼ぶ。
  React のコードを書くうえで、最もよく行う操作の 1 つである。

## 例: Accordion と Panel

出典: Lifting state up by example

- 例では、親の `Accordion` が 2 つの `Panel` を描画する。
- 各 `Panel` は、内容を表示するかどうかを決める真偽値の `isActive` を、自分の state として持つ。
- 初期状態では、どちらの `isActive` も `false` で、両方とも閉じている。
- 片方のボタンを押しても、その `Panel` の `isActive` だけが変わる。
  2 つの `Panel` は互いに独立している。
- 2 つを連動させ、一度に 1 つだけ開くようにするには、次の 3 つの手順で state を親へ持ち上げる。
  1. 子コンポーネントから state を取り除く（Remove）。
  1. 共通の親から、固定値のデータを渡す（Pass）。
  1. 共通の親に state を追加し、イベントハンドラと一緒に渡す（Add）。

## 手順 1: 子から state を取り除く

出典: Step 1: Remove state from the child components

- `Panel` の `isActive` を制御する権限を、親へ渡す。
- そのため、`Panel` 内の `isActive` の state の宣言を消し、代わりに `isActive` を `Panel` の props の一覧に加える。

```js
function Panel({ title, children, isActive }) {
```

- これで、親は `isActive` を props として渡して制御できる。
- 逆に、`Panel` は `isActive` の値を制御できなくなる。
  値は親しだいになる。

## 手順 2: 共通の親から固定値を渡す

出典: Step 2: Pass hardcoded data from the common parent

- state を持ち上げるには、連動させたい子のすべてを含む、最も近い共通の親を見つける。
- この例では `Accordion` がそれにあたる。
  両方の `Panel` の上にあり、それぞれの props を制御できるので、どちらが開いているかの「情報源（source of truth）」になる。
- まず `Accordion` から、両方の `Panel` に固定値の `isActive`（たとえば `true`）を渡す。
- 固定値を書き換えて、画面の変化を試せる。

## 手順 3: 共通の親に state を追加する

出典: Step 3: Add state to the common parent

- state を持ち上げると、state として持つものの性質が変わることが多い。
- この例では、同時に開く `Panel` は 1 つだけなので、`Accordion` は「どの `Panel` が開いているか」を覚える必要がある。
  真偽値ではなく、開いている `Panel` の番号（index）を数値で持てる。

```js
const [activeIndex, setActiveIndex] = useState(0);
```

- `activeIndex` が `0` なら 1 つ目、`1` なら 2 つ目が開いている。
- `Panel` の「Show」ボタンを押したときに、`Accordion` の index を変える必要がある。
  ただし、`activeIndex` は `Accordion` の中で定義されているので、`Panel` が直接は変えられない。
- そこで `Accordion` が、イベントハンドラを props として明示的に渡し、`Panel` に変更を許可する。

```js
<Panel isActive={activeIndex === 0} onShow={() => setActiveIndex(0)}>
```

- `Panel` 内の `<button>` は、`onShow` の props をクリックのイベントハンドラとして使う。
- これで state の持ち上げは完了する。
  - state を共通の親へ移したことで、2 つの `Panel` を連動させられた。
  - 「表示中」の真偽値を 2 つ持つ代わりに index を使ったことで、同時に開くのが 1 つだけになることが保証された。
  - イベントハンドラを子へ渡したことで、子が親の state を変えられるようになった。

## 制御されたコンポーネントと制御されていないコンポーネント

出典: Controlled and uncontrolled components

- ローカルな state を持つコンポーネントを、「制御されていない（uncontrolled）」と呼ぶのが一般的である。
  state を持っていた最初の `Panel` は、親が開閉に影響できないので、制御されていない。
- 重要な情報が、自分のローカルな state ではなく props で決まるコンポーネントを、「制御された（controlled）」と呼べる。
  親が振る舞いを完全に指定できる。
  props の `isActive` を使う最終形の `Panel` は、`Accordion` に制御されている。
- 制御されていないコンポーネントは、設定が少なくて済むので、親の中で使いやすい。
  ただし、複数をまとめて連動させたいときの柔軟性は低い。
- 制御されたコンポーネントは、最大限に柔軟である。
  ただし、親が props ですべてを設定する必要がある。
- 実際には、この 2 つは厳密な技術用語ではない。
  多くのコンポーネントは、ローカルな state と props の両方を、ある程度ずつ持つ。
  それでも、コンポーネントの設計と機能を語るうえで役に立つ言い方である。
- コンポーネントを書くときは、どの情報を（props で）制御し、どの情報を（state で）制御しないかを考える。
  あとから考えを変えて、書き直してもよい。

## state ごとに 1 つの情報源

出典: A single source of truth for each state

- React のアプリでは、多くのコンポーネントが自分の state を持つ。
  - 入力欄のように、木の末端（leaf）に近いところに置かれる state がある。
  - アプリの上のほうに置かれる state もある。
    クライアント側のルーティングのライブラリも、多くは現在のルートを React の state に保存し、props で渡して実装されている。
- 作業を進めると、アプリは変わっていく。
  それぞれの state をどこに置くかを探る間は、state を下へ移したり、また上へ戻したりすることがよくある。
  これも作業の一部である。
- 実際の感覚をもっとつかむには、原典は Thinking in React を読むよう勧めている。

## 例題

出典: Challenges

- 同期する入力欄（Synced inputs）
  - 2 つの入力欄は独立している。
    片方を編集すると、もう片方も同じ文字列になり、逆も同じになるようにする課題である。
  - 解き方は、`text` の state と `handleChange` を親へ移し、2 つの `Input` に props として渡すことである。
- リストの絞り込み（Filtering a list）
  - `SearchBar` が検索語の `query` を state として持ち、親の `FilterableList` は、それを考慮せずに `List` を表示している。
    検索語に応じて一覧を絞り込む課題である。
  - 解き方は、`query` の state と `handleChange` を `SearchBar` から `FilterableList` へ持ち上げ、`SearchBar` へは `query` と `onChange` の props として渡すことである。
    さらに、`FilterableList` で `filterItems(foods, query)` を呼び、絞り込んだ一覧を `List` へ渡す。

## See also

- [Sharing State Between Components (React)](https://react.dev/learn/sharing-state-between-components)
- [原典の Markdown (GitHub)](https://raw.githubusercontent.com/reactjs/react.dev/main/src/content/learn/sharing-state-between-components.md)
