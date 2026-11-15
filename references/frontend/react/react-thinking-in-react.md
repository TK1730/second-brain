---
type: reference
title: 'React: Thinking in React 要約'
description: 'React 公式ドキュメント「Thinking in React」の要約（モックアップから始める、コンポーネントの階層、静的な版、state の最小表現、state の置き場所、逆方向のデータの流れ）。'
tags: [react, components, state, props, data-flow]
status: stable
verified: { by: claude-code/claude-sonnet-5-5, at: 2026-10-21T00:00:00Z }
stale_after: 2027-10-21T00:00:00Z
---

# React: Thinking in React 要約

React 公式ドキュメント（Learn）の「Thinking in React」の要約である。
検索できる商品表を作る例を通して、UI を React で作るときの考え方を 5 つの手順で説明している。
外部資料の要約であり、最終的な根拠は原典を参照すること。
要点は「UI をコンポーネントに分ける」「まず state のない静的な版を作る」「state は最小限にして、必要な共通の親に置く」「子から親へ変更を伝える関数を渡す」の 4 つである。

## 全体の流れ

出典: Thinking in React（導入）、Start with the mockup

- React で UI を作るときは、まず UI をコンポーネントという部品に分ける。
  次に、各コンポーネントの見た目の状態を記述する。
  最後に、データが流れるようにコンポーネントをつなぐ。
- 例では、次の形の商品データを返す JSON API と、デザイナーのモックアップがあるものとする。
  - 各商品は `category`、`price`、`stocked`、`name` を持つ。
- UI を React で実装するときは、通常、同じ 5 つの手順を踏む。

## 手順 1: UI をコンポーネントの階層に分ける

出典: Step 1: Break the UI into a component hierarchy

モックアップの各コンポーネントと部分コンポーネントを枠で囲み、名前を付ける。
デザイナーと作業しているなら、デザインツールで名前が付いていることがあるので尋ねる。

- 分け方は、立場によって考え方が違う。
  - プログラミング: 関数やオブジェクトを新しく作るかどうかを決めるのと同じ技法を使う。
    その一つが関心の分離で、コンポーネントは理想的には 1 つのことだけを扱う。
    大きくなったら、小さな部分コンポーネントに分解する。
  - CSS: クラスセレクタを付けたくなる単位を考える（ただしコンポーネントのほうが少し粗い）。
  - デザイン: デザインのレイヤーをどう整理するかを考える。
- JSON がよく構造化されていれば、UI のコンポーネントの構造に自然に対応することが多い。
  UI とデータモデルは、同じ情報の構造（同じ形）を持つことが多いからである。
  コンポーネントは、データモデルの 1 つの部分に対応させる。

例の画面には 5 つのコンポーネントがある。

1. `FilterableProductTable` はアプリ全体を含む。
1. `SearchBar` はユーザーの入力を受け取る。
1. `ProductTable` は、ユーザーの入力に従って一覧を表示し、絞り込む。
1. `ProductCategoryRow` は、カテゴリごとの見出しを表示する。
1. `ProductRow` は、商品ごとの行を表示する。

- 表の見出し（Name と Price）は、独立したコンポーネントにしていない。
  これは好みの問題で、どちらでもよい。
  見出しが複雑になる（並べ替えを足すなど）なら、`ProductTableHeader` に切り出せる。
- モックアップで別のコンポーネントの中にあるコンポーネントは、階層では子にする。

```text
FilterableProductTable
  SearchBar
  ProductTable
    ProductCategoryRow
    ProductRow
```

## 手順 2: React で静的な版を作る

出典: Step 2: Build a static version in React

まず、対話を足さずに、データモデルから UI を描画するだけの版を作る。
静的な版は、たくさん打つが考えることは少ない。
対話を足すのは、たくさん考えるが打つことは少ない。
そのため、静的な版を先に作るほうが楽なことが多い。

- 静的な版では、コンポーネントが他のコンポーネントを再利用し、Props でデータを渡す。
  Props は、親から子へデータを渡す方法である。
- この版では state を使わない。
  state は、対話のため、つまり時間とともに変わるデータのために取っておくものだからである。
- 作る順は、上の階層から作る「トップダウン」と、下の階層から作る「ボトムアップ」のどちらでもよい。
  簡単な例ではトップダウンが楽なことが多く、大きなプロジェクトではボトムアップが楽である。
- 作り終えると、データモデルを描画する再利用可能なコンポーネントの集まりができる。
  静的な版なので、コンポーネントは JSX を返すだけである。
- 階層の最上位（`FilterableProductTable`）が、データモデルを Props として受け取る。
  データが最上位から木の下へ流れるので、これを一方向のデータフロー（one-way data flow）と呼ぶ。
- 注意: この時点では、state の値を使ってはいけない。

## 手順 3: UI の state の、最小で完全な表現を見つける

出典: Step 3: Find the minimal but complete representation of UI state

UI を対話的にするには、ユーザーが元のデータモデルを変えられるようにする必要がある。
そのために state を使う。

- state は、アプリが覚えておく必要のある、変化するデータの最小の集まりと考える。
- state の構造を決める最も大事な原則は、DRY（Don't Repeat Yourself）を守ることである。
  アプリに必要な state の絶対的に最小の表現を見つけ、それ以外は必要なときに計算する。
  例えば買い物リストでは、項目の配列を state に持つ。
  項目の数も表示したいときは、数を別の state にせず、配列の長さを読む。

例のアプリのデータは次の 4 つである。

1. 商品の元の一覧
1. ユーザーが入力した検索の文字列
1. チェックボックスの値
1. 絞り込んだ商品の一覧

次の問いで、state ではないものを見分ける。

- 時間が経っても変わらないか。変わらないなら、state ではない。
- 親から Props で渡されているか。渡されているなら、state ではない。
- 既存の state や Props から計算できるか。計算できるなら、state では「絶対に」ない。

残ったものが、おそらく state である。
例では、次のように判断している。

1. 商品の元の一覧は、Props で渡されるので state ではない。
1. 検索の文字列は、時間とともに変わり、何かから計算もできないので state である。
1. チェックボックスの値も、同じ理由で state である。
1. 絞り込んだ一覧は、元の一覧を検索の文字列とチェックボックスの値で絞り込めば計算できるので、state ではない。

結論として、state は検索の文字列とチェックボックスの値だけである。

### Props と state（Deep Dive）

出典: Props vs State

- Props は、関数に渡す引数のようなものである。
  親コンポーネントが子にデータを渡し、その見た目を調整できる（例: `Form` が `Button` に `color` を渡す）。
- state は、コンポーネントの記憶のようなものである。
  情報を覚えておき、操作に応じて変えられる（例: `Button` が `isHovered` を持つ）。
- 両者は別のものだが、一緒に働く。
  親が state に情報を持ち（変えられるようにするため）、それを子に Props として渡すことがよくある。

## 手順 4: state を置く場所を決める

出典: Step 4: Identify where your state should live

state を変える責任を持つコンポーネントを、その state を持つ（own する）コンポーネントと呼ぶ。
React はデータを親から子へ一方向に渡すので、どのコンポーネントがどの state を持つかは、すぐには分からないことがある。
state の 1 つひとつについて、次の手順で決める。

1. その state に基づいて何かを描画するコンポーネントを、すべて見つける。
1. それらの最も近い共通の親（階層の中で、それらすべての上にあるコンポーネント）を見つける。
1. state の置き場所を決める。
   1. 多くの場合、共通の親に直接置ける。
   1. 共通の親より上のコンポーネントに置くこともできる。
   1. state を持つのにふさわしいコンポーネントが見つからなければ、state を持つためだけのコンポーネントを新しく作り、共通の親より上の階層に足す。

例では、検索の文字列とチェックボックスの値は、いつも一緒に現れるので、同じ場所に置く。

1. state を使うコンポーネントは、`ProductTable`（絞り込みに使う）と `SearchBar`（表示に使う）である。
1. 2 つが共有する最初の親は `FilterableProductTable` である。
1. よって、state は `FilterableProductTable` に置く。

- state は `useState()` フックで足す。
  フックは、React に「フックする」ための特別な関数である。
- `FilterableProductTable` の先頭に state を 2 つ足して初期値を指定し、`filterText` と `inStockOnly` を `SearchBar` と `ProductTable` に Props として渡す。

```js
function FilterableProductTable({ products }) {
  const [filterText, setFilterText] = useState('');
  const [inStockOnly, setInStockOnly] = useState(false);
```

- ここまでで、初期値を変えると、検索の入力欄と表の両方が更新される。
  ただし、フォームを編集してもまだ動かない。
  `value` を渡しているのに `onChange` がないと、読み取り専用の欄になるという警告が、コンソールに出る。
- `ProductTable` と `SearchBar` は、Props の `filterText` と `inStockOnly` を読んで描画している。
  ユーザーの入力に応じるコードは、まだ書いていない。これが最後の手順である。

## 手順 5: 逆方向のデータの流れを足す

出典: Step 5: Add inverse data flow

ここまでで、Props と state は階層を下へ流れて正しく描画される。
ユーザーの入力に応じて state を変えるには、逆方向、つまり木の深いところにあるフォームのコンポーネントから、`FilterableProductTable` の state を更新する流れが必要になる。

- React はこのデータの流れを明示的にする。
  双方向データバインディングより、少し多く打つ必要がある。
- 前の例で入力しても無視されるのは、意図したとおりの動作である。
  `<input value={filterText} />` と書くと、`input` の `value` は、常に `FilterableProductTable` から渡された `filterText` に等しくなる。
  `filterText` を一度も更新していないので、入力欄は変わらない。
- state を持つのは `FilterableProductTable` だけなので、`setFilterText` と `setInStockOnly` を呼べるのもそのコンポーネントだけである。
  `SearchBar` が state を更新できるようにするには、これらの関数を Props として `SearchBar` に渡す。
- `SearchBar` の中では、`onChange` のイベントハンドラを足し、そこから親の state を設定する。
  - 検索の入力欄は `e.target.value` を、チェックボックスは `e.target.checked` を渡す。

```js
<input type="text" value={filterText} onChange={(e) => onFilterTextChange(e.target.value)} />
```

これでアプリは完全に動く。

## See also

- [Thinking in React（原典）](https://react.dev/learn/thinking-in-react)
- [原典の Markdown（raw）](https://raw.githubusercontent.com/reactjs/react.dev/main/src/content/learn/thinking-in-react.md)
