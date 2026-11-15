---
type: reference
title: 'React: Passing Props to a Component 要約'
description: 'React 公式ドキュメント「Passing Props to a Component」の要約（props の渡し方と読み方、既定値、スプレッド構文での転送、children による JSX の受け渡し、props の変化と不変性）。'
tags: [react, props, children, jsx]
status: stable
verified: { by: claude-code/claude-sonnet-5-5, at: 2026-10-21T00:00:00Z }
stale_after: 2027-10-21T00:00:00Z
---

# React: Passing Props to a Component 要約

React 公式ドキュメント（Learn）の「Passing Props to a Component」の要約である。
外部資料の要約であり、最終的な根拠は原典を参照すること。
要点は「親は props で子に情報を渡し、子は引数の分割代入で読む」「JSX を入れ子にすると子では `children` として届く」「props は読み取り専用で、変えたいときは state を使う」の 3 つである。

## props とは

出典: Familiar props

- React のコンポーネントは、props を使って互いにやり取りする。
- 親コンポーネントは、子に props を渡すことで情報を伝えられる。
- props は HTML の属性に似ているが、オブジェクト、配列、関数を含む任意の JavaScript の値を渡せる。
- props は JSX タグに渡す情報である。
  たとえば `<img>` には `className`、`src`、`alt`、`width`、`height` などを渡せる。
- `<img>` に渡せる props は、あらかじめ決まっている（ReactDOM が HTML の標準に従うため）。
  自作のコンポーネント（例: `<Avatar>`）には、任意の props を渡して挙動を変えられる。

## props を渡して読む

出典: Passing props to a component

props の受け渡しは 2 段階で行う。

1. 子コンポーネントに props を渡す。
   たとえば `person`（オブジェクト）と `size`（数値）を、JSX の属性として書く。
1. 子コンポーネントの中で props を読む。
   `function Avatar({ person, size })` のように、関数名の直後の `({` と `})` の間に名前を並べる。
   これで、変数のようにコンポーネントの中で使える。

```js
function Avatar({ person, size }) {
  // person and size are available here
}
```

- `person={{ ... }}` の二重の波括弧は、JSX の波括弧の中にあるただのオブジェクトである。
- props を使うと、親と子を独立に考えられる。
  親は子の使い方を知らずに値を変えられ、子は親を見ずに props の使い方を変えられる。
- props は調整できる「つまみ」のようなものである。
  関数の引数と同じ役割を持ち、props はコンポーネントの唯一の引数である。
- コンポーネントの関数は `props` オブジェクトを 1 つだけ受け取る。
  通常は `props` 全体ではなく、個々の props に分割代入して使う。

### 分割代入の波括弧に注意

出典: Passing props to a component（Pitfall）

- props を宣言するときは、`(` と `)` の内側にある `{` と `}` を落とさない。
- この構文は「分割代入（destructuring）」と呼ばれる。
  `props` を受け取って `props.person` や `props.size` を変数に取り出す書き方と同等である。

## props の既定値

出典: Specifying a default value for a prop

- 値が指定されないときの既定値は、分割代入の中で引数の直後に `=` と値を書いて指定する。
- 既定値が使われるのは、props が渡されないときと、`size={undefined}` が渡されたときだけである。
- `size={null}` や `size={0}` を渡した場合、既定値は使われない。

```js
function Avatar({ person, size = 100 }) {
  // ...
}
```

## JSX のスプレッド構文での転送

出典: Forwarding props with the JSX spread syntax

- props の受け渡しが繰り返しになることがある。
  たとえば `Profile` が受け取った `person`、`size`、`isSepia`、`thickBorder` を、そのまま `Avatar` に 1 つずつ渡す場合である。
- 繰り返しのコードが悪いわけではなく、読みやすいこともある。
  簡潔さを重視するなら、スプレッド構文が使える。
- 自分では props を使わず、すべてを子に転送するコンポーネントでは、`<Avatar {...props} />` と書ける。
  これで `Profile` の props がすべて `Avatar` に転送される。
- スプレッド構文は控えめに使う。
  あらゆるコンポーネントで使っているなら、何かがおかしい。
  多くの場合、コンポーネントを分割して children を JSX として渡すべきだというサインである。

```js
function Profile(props) {
  return (
    <div className="card">
      <Avatar {...props} />
    </div>
  );
}
```

## children として JSX を渡す

出典: Passing JSX as children

- ブラウザの組み込みタグは入れ子にできる。
  自作のコンポーネントも、同じように入れ子にできる（例: `<Card><Avatar /></Card>`）。
- JSX のタグの中に内容を入れ子にすると、親コンポーネントはその内容を `children` という props で受け取る。
  たとえば `Card` は、`children` に設定された `<Avatar />` を受け取り、ラッパーの `div` の中に描画する。
- `Card` は、中に何が描画されるかを知る必要がない。
  `<Avatar>` をテキストなどに置き換えても、`Card` はそのまま包める。
- `children` を持つコンポーネントは、親が任意の JSX で「埋められる穴」を持つものと考えられる。
- `children` は、パネルやグリッドなどの見た目のラッパーによく使われる。

```js
function Card({ children }) {
  return <div className="card">{children}</div>;
}
```

## props は時間とともに変わる

出典: How props change over time

- コンポーネントは、時間とともに異なる props を受け取ることがある。
  props は最初だけの静的な値とは限らない。
- 例として、`Clock` は親から `color` と `time` を受け取る。
  `time` は 1 秒ごとに、`color` は別の色を選んだときに変わる。
  props は、ある時点でのコンポーネントのデータを反映する。
- ただし、props は不変（immutable）、つまり変更できない。
- コンポーネントが props を変える必要があるとき（ユーザーの操作や新しいデータへの対応など）は、親に別の props、つまり新しいオブジェクトを渡すよう「頼む」。
  古い props は捨てられ、そのメモリは JavaScript エンジンがいずれ回収する。
- 「props を変えよう」としてはいけない。
  ユーザーの入力に応える必要があるときは、state を設定する。
  state は「State: A Component's Memory」で扱われる。

## まとめ

出典: Recap

- props を渡すには、HTML の属性と同じように JSX に書く。
- props を読むには、`function Avatar({ person, size })` の分割代入を使う。
- `size = 100` のように既定値を指定でき、props が無いときと `undefined` のときに使われる。
- `<Avatar {...props} />` で、すべての props を転送できる。
  ただし使いすぎない。
- `<Card><Avatar /></Card>` のような入れ子の JSX は、`Card` の `children` として届く。
- props は、ある時点での読み取り専用のスナップショットである。
  描画のたびに、新しい版の props を受け取る。
- props は変更できない。
  対話が必要なときは、state を設定する。

## See also

- [Passing Props to a Component（react.dev）](https://react.dev/learn/passing-props-to-a-component)
- [原典の Markdown（GitHub）](https://raw.githubusercontent.com/reactjs/react.dev/main/src/content/learn/passing-props-to-a-component.md)
