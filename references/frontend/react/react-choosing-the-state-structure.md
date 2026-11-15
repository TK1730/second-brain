---
type: reference
title: 'React: Choosing the State Structure 要約'
description: 'React 公式ドキュメント「Choosing the State Structure」の要約（state の構造を決める 5 つの原則、関連する state のまとめ方、矛盾・冗長・重複・深い入れ子の避け方）。'
tags: [react, state, state-structure, normalization]
status: stable
verified: { by: claude-code/claude-sonnet-5-5, at: 2026-10-21T00:00:00Z }
stale_after: 2027-10-21T00:00:00Z
---

# React: Choosing the State Structure 要約

React 公式ドキュメント（react.dev Learn）の「Managing State: Choosing the State Structure」の要約である。
外部資料の要約であり、最終的な根拠は原典を参照すること。
要点は「関連する state をまとめる」「矛盾を避ける」「冗長な state を避ける」「重複を避ける」「深い入れ子を避ける」の 5 つの原則である。

## state の構造を決める原則

出典: Principles for structuring state

state を持つコンポーネントを書くときは、state 変数をいくつ使うか、データをどんな形にするかを選ぶ。
最適でない構造でも正しく動くプログラムは書けるが、次の 5 つの原則が良い選択の助けになる。

1. 関連する state をまとめる。
   2 つ以上の state 変数を常に同時に更新するなら、1 つの state 変数に統合することを検討する。
1. state の矛盾を避ける。
   複数の state が食い違う可能性がある構造は、間違いの余地を残す。
1. 冗長な state を避ける。
   props や既存の state 変数から描画中に計算できる情報は、state に入れない。
1. state の重複を避ける。
   同じデータが複数の state 変数や入れ子のオブジェクトに重複していると、同期を保つのが難しい。
1. 深く入れ子になった state を避ける。
   階層が深い state は更新しにくいので、可能なら平らな構造にする。

これらの原則の目的は、間違いを持ち込まずに state を更新しやすくすることである。
冗長なデータや重複したデータを state から取り除くと、すべての部品の同期が保たれる。
これは、データベース技術者がバグの可能性を減らすためにデータベースの構造を「正規化」するのに似ている。
原典は、アインシュタインの言葉を言い換えて「state は、できる限り単純に。ただし、単純すぎないように」と述べている。

## 関連する state をまとめる

出典: Group related state

1 つの state 変数にするか、複数にするかで迷うことがある。
技術的にはどちらでも書けるが、2 つの state 変数が常に一緒に変わるなら、1 つにまとめるとよい。
そうすれば、両方を同期して更新するのを忘れない。

- 例: ポインタを動かすと赤い点の座標 `x` と `y` が両方変わる。
  別々の state 変数にせず、`{ x, y }` のオブジェクトを 1 つの state 変数に持つ。
- state 変数を 1 つにまとめると、更新の関数は 1 回の呼び出しで両方の値を渡す。
- いくつの state が要るか前もって分からないときも、オブジェクトや配列にまとめる。
  例: 利用者が自分で項目を足せるフォーム。
- state をオブジェクトにしたら、1 つの項目だけを更新することはできない。
  ほかの項目も明示的に写す必要がある。
  上の例で `setPosition({ x: 100 })` とすると `y` が無くなるので、`setPosition({ ...position, x: 100 })` と書くか、2 つの state 変数に分けて `setX(100)` とする。

## state の矛盾を避ける

出典: Avoid contradictions in state

ホテルのフィードバックフォームを例にとる。
`isSending` と `isSent` の 2 つの state 変数を持たせると、`setIsSent` と `setIsSending` を一緒に呼び忘れたときに、両方が `true` になる「あり得ない」状態が生まれる。
コンポーネントが複雑になるほど、何が起きたのかが分かりにくくなる。

- `isSending` と `isSent` が同時に `true` になることはないので、1 つの `status` 変数に置き換える。
  取りうる値は `'typing'`（初期）、`'sending'`、`'sent'` の 3 つの有効な状態だけである。
- 読みやすさのために、`status` から定数を宣言してもよい。

```js
const isSending = status === 'sending';
const isSent = status === 'sent';
```

- これらは state 変数ではないので、互いの同期がずれる心配はない。

## 冗長な state を避ける

出典: Avoid redundant state

props や既存の state 変数から描画中に計算できる情報は、state に入れるべきではない。

- 例: `firstName`、`lastName`、`fullName` を state に持つフォームでは、`fullName` が冗長である。
  `fullName` は `firstName` と `lastName` からいつでも計算できるので、state から取り除く。
- 描画中に `const fullName = firstName + ' ' + lastName;` と計算すれば、変更ハンドラで特別なことをしなくてよい。
  `setFirstName` や `setLastName` を呼ぶと再描画され、次の `fullName` が新しいデータから計算される。

### props を state に写さない

出典: Don't mirror props in state

冗長な state の典型は、props を state の初期値にするコードである。

```js
function Message({ messageColor }) {
  const [color, setColor] = useState(messageColor);
```

- state は最初の描画のときにしか初期化されない。
  親が後で別の `messageColor` を渡しても、`color` という state 変数は更新されない。
- 代わりに、props を直接使う。
  短い名前が欲しければ、定数（`const color = messageColor;`）にする。
- props を state に写すのが意味を持つのは、その props の以降の更新を無視したいときだけである。
  その場合は、新しい値が無視されることを示すため、props の名前を `initial` や `default` で始めるのが慣習である。

## state の重複を避ける

出典: Avoid duplication in state

旅行のおやつを 1 つ選ぶメニューのリストを例にとる。
選択した項目を `selectedItem` というオブジェクトで state に持つと、その中身が `items` の配列の中のオブジェクトと同じものになり、項目の情報が 2 か所に重複する。

- 項目を編集可能にすると、「選ぶ」を押した後に項目を編集しても、下のラベルに反映されない。
  重複した state のうち、`selectedItem` を更新し忘れたためである。
- `selectedItem` も更新する方法もあるが、より簡単な直し方は重複をなくすことである。
  オブジェクトの代わりに `selectedId` を state に持ち、`items` から該当する ID の項目を探して `selectedItem` を得る。
- 重複していた state は、次のように変わる。
  - 変更前: `items = [{ id: 0, title: 'pretzels' }, ...]` と `selectedItem = { id: 0, title: 'pretzels' }`
  - 変更後: `items = [{ id: 0, title: 'pretzels' }, ...]` と `selectedId = 0`
- 選択中の項目を編集すると、`setItems` が再描画を起こし、`items.find(...)` が更新後のタイトルの項目を見つけるので、メッセージもすぐに更新される。
  選択中の項目そのものを state に持つ必要はなく、本質的なのは選択中の ID だけで、残りは描画中に計算できる。

## 深く入れ子になった state を避ける

出典: Avoid deeply nested state

惑星、大陸、国からなる旅行計画を、入れ子のオブジェクトと配列で表したくなることがある。
しかし、すでに訪れた場所を削除するボタンを加えるとき、入れ子の state の更新は、変更した部分から上へ向かってオブジェクトをコピーしていく作業になる。
深く入れ子になった場所を削除するには、その親の連鎖全体のコピーが要り、コードが冗長になる。

- 入れ子が深すぎて更新しにくいときは、state を「平ら」にすることを検討する。
  各場所が子の場所の配列を持つ木構造をやめ、各場所は子の ID の配列（`childIds`）を持つ。
  そのうえで、各 ID から対応する場所への対応表（オブジェクト）を state に持つ。
- この再構成は、データベースのテーブルに似ている。
- state が平ら（「正規化」とも呼ぶ）になると、入れ子の項目の更新が簡単になる。
- 場所を削除するために更新するのは、次の 2 階層だけである。
  - 親の場所の新しい版は、`childIds` の配列から削除した ID を除く。
  - ルートの「テーブル」オブジェクトの新しい版は、更新した親の場所を含む。
- state はいくらでも入れ子にできるが、平らにすると多くの問題を解決できる。
  state が更新しやすくなり、入れ子のオブジェクトの別々の場所に重複が生じるのも防げる。

### メモリ使用量の改善

出典: Improving memory usage

理想的には、削除した項目（とその子）をテーブルのオブジェクトからも取り除いて、メモリの使用量を減らす。
原典のその版では、Immer を使って更新のロジックを簡潔にしている。

### 入れ子の state を子コンポーネントへ移す

出典: Avoid deeply nested state

入れ子になった state の一部を子コンポーネントに移すと、入れ子を減らせることもある。
これは、項目にポインタが乗っているかどうかなど、保存する必要のない一時的な UI の state に向いている。

## 要点

出典: Recap

- 2 つの state 変数が常に一緒に更新されるなら、1 つに統合することを検討する。
- 「あり得ない」状態を作らないように、state 変数を慎重に選ぶ。
- 更新で間違えにくくなるように、state を構造化する。
- 同期を保つ手間をなくすため、冗長な state と重複した state を避ける。
- 更新を無視したいと明確に意図するとき以外は、props を state に入れない。
- 選択のような UI のパターンでは、オブジェクトそのものではなく、ID やインデックスを state に持つ。
- 深く入れ子になった state の更新が複雑なら、平らにすることを試す。

## See also

- [Choosing the State Structure（原典）](https://react.dev/learn/choosing-the-state-structure)
