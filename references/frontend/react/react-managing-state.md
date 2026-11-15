---
type: reference
title: 'React: Managing State 要約'
description: 'React 公式ドキュメント「Managing State」（学習の章の概要ページ）の要約（宣言的な UI と見た目の状態、state の構造の選び方、state の持ち上げ、保持とリセット、reducer、context、reducer と context の組み合わせ）。'
tags: [react, state, declarative-ui, reducer, context]
status: stable
verified: { by: claude-code/claude-sonnet-5-5, at: 2026-10-21T00:00:00Z }
stale_after: 2027-10-21T00:00:00Z
---

# React: Managing State 要約

React の公式ドキュメント（Learn）の章「Managing State」の概要ページの要約である。
この章には節ごとの詳しいページがあり、この文書は概要ページそのものだけを扱う。
詳しいページのうち、次の 2 つは別の文書で要約している。

- [React: Choosing the State Structure 要約](/references/frontend/react/react-choosing-the-state-structure.md)
- [React: Sharing State Between Components 要約](/references/frontend/react/react-sharing-state-between-components.md)

外部資料の要約であり、最終的な根拠は原典を参照すること。
要点は「UI は見た目の状態ごとに宣言し、state の変化で切り替える」「state には重複した情報を持たせない」「state の置き場所と更新の書き方は、アプリの成長に合わせて整理する」の 3 つである。

## 章の概要

出典: Intro / You will learn

アプリが大きくなると、state をどう整理するか、コンポーネントの間でデータがどう流れるかを意識的に決めると役に立つ。
冗長な state や重複した state は、バグの原因としてよくある。
この章では、次のことを学ぶ。

- UI の変化を state の変化として考える方法
- state をうまく構造化する方法
- state を「持ち上げて」コンポーネントの間で共有する方法
- state を保持するか、リセットするかを制御する方法
- 複雑な state の更新ロジックを 1 つの関数にまとめる方法
- 「prop の中継（prop drilling）」なしに情報を渡す方法
- アプリの成長に合わせて state の管理を拡張する方法

## Reacting to input with state

出典: Reacting to input with state

React では、UI をコードから直接変更しない。
たとえば「ボタンを無効にする」「ボタンを有効にする」「成功メッセージを表示する」といった命令は書かない。
代わりに、コンポーネントの見た目の状態（「初期状態」「入力中」「成功」など）ごとに、見せたい UI を記述する。
そのうえで、ユーザーの入力に応じて state の変化を起こす。
これは、デザイナーが UI を考えるやり方に近い。

概要ページの例は、クイズのフォームである。
`status` という state の変数で、送信ボタンを有効にするか無効にするか、成功メッセージに差し替えるかを決めている。

```jsx
const [status, setStatus] = useState('typing');
// status が 'success' なら成功メッセージを返す
// status が 'submitting' の間は textarea と送信ボタンを無効にする
```

詳しくは [Reacting to Input with State](https://react.dev/learn/reacting-to-input-with-state) を参照する。

## Choosing the state structure

出典: Choosing the state structure

state をうまく構造化できるかどうかで、変更やデバッグがしやすいコンポーネントになるか、バグの源になり続けるコンポーネントになるかが分かれる。
最も大事な原則は、state に冗長な情報や重複した情報を含めないことである。
不要な state があると、更新を忘れやすく、バグを招く。

例として、`firstName` と `lastName` に加えて `fullName` も state に持つフォームを挙げている。
`fullName` は冗長なので、state から外し、描画の間に `firstName + ' ' + lastName` から計算すればコードが簡単になる。
この程度の小さな変更に見えても、React アプリの多くのバグはこのやり方で直せる、としている。

詳しくは [Choosing the State Structure](https://react.dev/learn/choosing-the-state-structure) を参照する。
要約は [React: Choosing the State Structure 要約](/references/frontend/react/react-choosing-the-state-structure.md) にある。

## Sharing state between components

出典: Sharing state between components

2 つのコンポーネントの state を、常に一緒に変えたいことがある。
そのときは、両方から state を取り除き、最も近い共通の親へ移して、props で渡す。
これが「state の持ち上げ（lifting state up）」であり、React のコードを書くときに最もよく行うことの 1 つである。

例は、一度に 1 つのパネルだけを開くアコーディオンである。
各パネルが開閉の state を持つ代わりに、親が `activeIndex` を持ち、子には `isActive` と `onShow` を props で渡す。

詳しくは [Sharing State Between Components](https://react.dev/learn/sharing-state-between-components) を参照する。
要約は [React: Sharing State Between Components 要約](/references/frontend/react/react-sharing-state-between-components.md) にある。

## Preserving and resetting state

出典: Preserving and resetting state

コンポーネントを再描画するとき、React は木のどの部分を残して更新し、どの部分を捨てて作り直すかを決める。
多くの場合、React の自動の動作で十分である。
既定では、前回描画した木と「対応する」部分を保持する。

ただし、これが望む動作ではないこともある。
概要ページのチャットの例では、メッセージを入力してから宛先を切り替えても、入力欄がリセットされない。
そのため、誤った相手にメッセージを送ってしまうおそれがある。

React では、`<Chat key={email} />` のように別の `key` を渡して、state のリセットを強制できる。
宛先が違えば別の `Chat` コンポーネントとみなされ、新しいデータで一から作り直される（入力欄などの UI も同様）。
同じコンポーネントを描画していても、宛先を切り替えると入力欄がリセットされる。

詳しくは [Preserving and Resetting State](https://react.dev/learn/preserving-and-resetting-state) を参照する。

## Extracting state logic into a reducer

出典: Extracting state logic into a reducer

多くのイベントハンドラに state の更新が散らばったコンポーネントは、手に負えなくなることがある。
そのような場合は、state の更新ロジックをすべてコンポーネントの外の 1 つの関数にまとめられる。
この関数を「reducer」と呼ぶ。

- イベントハンドラは、ユーザーの「action」を指定するだけになり、簡潔になる。
- reducer の関数が、各 action に対して state をどう更新するかを定める。

概要ページの例は、旅程のタスク一覧である。
`useReducer(tasksReducer, initialTasks)` で state と `dispatch` を得て、ハンドラは `dispatch({ type: 'added', ... })` のように action を送る。
reducer の `switch` が、`added`、`changed`、`deleted` の各 action に応じて新しい配列を返す。

詳しくは [Extracting State Logic into a Reducer](https://react.dev/learn/extracting-state-logic-into-a-reducer) を参照する。

## Passing data deeply with context

出典: Passing data deeply with context

通常は、親のコンポーネントから子へ props で情報を渡す。
しかし、多くのコンポーネントを経由して prop を渡す必要があるときや、多くのコンポーネントが同じ情報を必要とするときは、props での受け渡しが不便になる。
context を使うと、親のコンポーネントが、下の木にあるどのコンポーネントにも（どれだけ深くても）、props で明示的に渡さずに情報を利用可能にできる。

概要ページの例では、`Heading` が最も近い `Section` に「尋ねて」見出しのレベルを決める。
各 `Section` は、親の `Section` に尋ねて 1 を足し、自分のレベルとする。
各 `Section` は、props を使わず、context を通して下のすべてのコンポーネントに情報を提供する。

詳しくは [Passing Data Deeply with Context](https://react.dev/learn/passing-data-deeply-with-context) を参照する。
関連する要約は [React: Passing Data Deeply with Context 要約](/references/frontend/react/react-passing-data-deeply-with-context.md) にある。

## Scaling up with reducer and context

出典: Scaling up with reducer and context

reducer は、コンポーネントの state の更新ロジックをまとめる。
context は、情報を深い位置のコンポーネントに渡す。
この 2 つを組み合わせて、複雑な画面の state を管理できる。

この方法では、複雑な state を持つ親のコンポーネントが、reducer でそれを管理する。
木の深いところにある他のコンポーネントは、context を通じてその state を読める。
さらに action を dispatch して、その state を更新することもできる。

概要ページの例では、`TasksProvider` が `useReducer` で state と `dispatch` を持ち、それぞれ別の context で提供する。
`useTasks` と `useTasksDispatch` というカスタムフックで、各コンポーネントがそれらを読む。

詳しくは [Scaling Up with Reducer and Context](https://react.dev/learn/scaling-up-with-reducer-and-context) を参照する。

## What's next?

出典: What's next?

章を 1 ページずつ読み進めるには、[Reacting to Input with State](https://react.dev/learn/reacting-to-input-with-state) から始める。
これらの話題にすでに慣れているなら、次の章の [Escape Hatches](https://react.dev/learn/escape-hatches) を読むことを勧めている。

## See also

- [Managing State（react.dev）](https://react.dev/learn/managing-state)
- [managing-state.md（原典の Markdown）](https://raw.githubusercontent.com/reactjs/react.dev/main/src/content/learn/managing-state.md)
