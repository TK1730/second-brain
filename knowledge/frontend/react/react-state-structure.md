---
type: guideline
title: 'React の state の持ち方'
description: 'React の state を設計するときの原則と、state を Effect で導出・同期しない考え方（関連する state のまとめ方、矛盾・冗長・重複・深い入れ子の避け方、描画中の計算、key によるリセット）。'
tags: [knowledge, react, state, effect, state-structure]
status: stable
verified: { by: claude-code/claude-sonnet-5-5, at: 2026-10-21T00:00:00Z }
stale_after: 2027-10-21T00:00:00Z
---

# React の state の持ち方

state は、間違いを持ち込まずに更新しやすい形にして持つ。
要点は「関連する state をまとめる」「矛盾・冗長・重複・深い入れ子を避ける」「計算できる値は Effect で同期せず描画中に計算する」ことである。
内容は React 公式ドキュメントの Choosing the State Structure と You Might Not Need an Effect にもとづく。

## 関連する state をまとめる

- 2 つ以上の state 変数が常に同時に更新されるなら、1 つにまとめる。
  更新の呼び出しが 1 回になり、片方の更新を忘れない。
- 必要な数が前もって分からないときも、オブジェクトや配列にまとめる。
- オブジェクトにしたら、1 項目だけを更新できなくなる。
  ほかの項目も明示的に写す。

```tsx
// 分ける: x と y を別々に更新する
const [x, setX] = useState(0);
const [y, setY] = useState(0);

// まとめる: 1 回の呼び出しで両方を渡す
const [position, setPosition] = useState({ x: 0, y: 0 });
setPosition({ ...position, x: 100 }); // y を写し忘れると消える
```

## 矛盾する state を避ける

- 複数の state が食い違えるなら、あり得ない状態が生まれる余地を残している。
  例: `isSending` と `isSent` の更新を片方忘れて、両方が `true` になる。
- 同時に `true` にならない値は、有効な状態だけを取る 1 つの変数に置き換える。
- 読みやすさのための `isSending` などは、state ではなく描画中に導出する定数にする。
  導出した定数は同期がずれない。

```tsx
const [status, setStatus] = useState<'typing' | 'sending' | 'sent'>('typing');
const isSending = status === 'sending';
const isSent = status === 'sent';
```

## 冗長な state を避ける

- props や既存の state から描画中に計算できる情報は、state に入れない。
  例: `firstName` と `lastName` があれば、`fullName` は計算で得られる。
- 描画中に計算すれば、変更ハンドラで特別な処理をしなくても、再描画のたびに新しいデータから計算される。

```tsx
const fullName = firstName + ' ' + lastName;
```

### props を state に写さない

- props を `useState` の初期値にしても、state が初期化されるのは最初の描画のときだけである。
  親が後で別の値を渡しても、state は更新されない。
- props を直接使う。
  短い名前が欲しければ定数にする。
- 写してよいのは、その props の以降の更新を無視したいときだけである。
  その場合は、`initial` や `default` で始まる名前にして、更新が無視されることを示す。

```tsx
function Message({ messageColor }: { messageColor: string }) {
  const color = messageColor; // useState(messageColor) にしない
  return <p style={{ color }}>...</p>;
}
```

## state の重複を避ける

- 同じデータが複数の場所にあると、片方の更新を忘れて食い違う。
  例: `items` と、その中の 1 つと同じ内容の `selectedItem` を両方 state に持つと、項目を編集しても `selectedItem` は古いままになる。
- 選択のような UI では、オブジェクトそのものではなく ID（またはインデックス）を state に持つ。
  選択中の項目は、描画中に一覧から探して得る。

```tsx
const [items, setItems] = useState(initialItems);
const [selectedId, setSelectedId] = useState(0);
const selectedItem = items.find((item) => item.id === selectedId);
```

## 深く入れ子になった state を避ける

- 入れ子が深いと、更新は変更した部分から上へ向かって、親の連鎖全体をコピーする作業になる。
- 更新しにくいときは、state を平らにする（「正規化」とも呼ぶ）。
  各項目は子の ID の配列（`childIds`）を持ち、ID から項目への対応表を state に持つ。
- 平らにすると、更新するのは親の項目と対応表の 2 階層だけになり、別々の場所に重複が生じるのも防げる。
- 保存する必要のない一時的な UI の state（ポインタが乗っているかなど）は、子コンポーネントに移すと入れ子を減らせる。

```tsx
// 入れ子: 子の配列をたどって更新する
{ id: 1, title: 'Earth', childPlaces: [{ id: 2, title: 'Africa', childPlaces: [] }] }

// 平ら: ID から項目への対応表
{ 1: { id: 1, title: 'Earth', childIds: [2] }, 2: { id: 2, title: 'Africa', childIds: [] } }
```

## 導出できる値を Effect で同期しない

state の構造を整えても、導出できる値を Effect で state に写すと、冗長な state を作り直してしまう。
Effect は React の外の仕組みと同期するためのもので、描画のためのデータ変換には要らない。

- 既存の props や state から計算できる値は、描画中に計算する。
  Effect で state を更新すると、余計な再描画が起きる。
  描画中の計算なら、連鎖更新がなくなって速くなり、state 同士のずれによるバグも防げる。
- 計算が重いときは、まず state と Effect を消して描画中に計算し、それでも重ければ `useMemo` で包む。
  `useMemo` の中身は描画中に動くので、純粋な計算にする。
  `useMemo` は最初の描画を速くせず、更新時の無駄を省くだけである。
  重いかどうかは、時間を測って判断する（合計 1ms 以上かかるなら検討する）。

```tsx
const visibleTodos = useMemo(() => getFilteredTodos(todos, filter), [todos, filter]);
```

### props が変わったときの state のリセット

- props が変わったときに Effect で state を空にすると、古い値で一度描画してから、もう一度描画することになる。
- コンポーネントを外側と内側に分け、外側から内側へ `key` を渡す。
  `key` が変わると別のコンポーネントとして扱われ、内側の state がすべてリセットされる。
- 位置と state の関係は [React の画面の切り替えと state のリセット](/knowledge/frontend/react/react-state-reset-by-position.md) を参照する。

```tsx
<Profile userId={userId} key={userId} />
```

### props が変わったときの state の一部の調整

state の一部だけを直したいときは、次の順に検討する。

1. 先に、ID だけを state に持ち、選択中の項目を描画中に計算できないか考える。
   ID に合う項目がなければ `null` になるので、調整自体が要らない。
1. 次に、`key` によるリセットを検討する。
1. それでも必要なら、描画中に前回の props を state に保存して比べ、違うときだけ同じコンポーネントの state を更新する。
   この書き方は Effect より効率がよいが、データの流れが分かりにくくなる。
   ほかのコンポーネントの state は更新できず、条件がないと無限ループになる。

### 計算の連鎖を避ける

- ある state を直す Effect が別の state を変え、それがまた別の Effect を動かす連鎖は避ける。
  描画のたびに子まで描画し直す無駄が増え、要件が変わると連鎖が合わなくなる。
- 描画中に計算できるものは計算し、残りの state の更新は 1 つのイベントハンドラの中で行う。
- イベントハンドラの中の state はスナップショットなので、次の値は自分で計算する。
  例: `const nextRound = round + 1`
- 次の選択肢をネットワークから取るなど、外部との同期が理由なら、Effect の連鎖が適切である。

## See also

- [React の画面の切り替えと state のリセット](/knowledge/frontend/react/react-state-reset-by-position.md)
- [React: Choosing the State Structure 要約](/references/frontend/react/react-choosing-the-state-structure.md)
- [React: You Might Not Need an Effect 要約](/references/frontend/react/react-you-might-not-need-an-effect.md)
