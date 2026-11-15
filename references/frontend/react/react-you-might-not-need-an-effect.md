---
type: reference
title: 'React: You Might Not Need an Effect 要約'
description: 'React 公式ドキュメント「You Might Not Need an Effect」の要約（Effect が要らない 2 つの場面、描画中の計算、useMemo、key による状態のリセット、イベントハンドラへの移し方、親への通知、外部ストア、データ取得）。'
tags: [react, effect, useEffect, useMemo, state, data-fetching]
status: stable
verified: { by: claude-code/claude-sonnet-5-5, at: 2026-10-21T00:00:00Z }
stale_after: 2027-10-21T00:00:00Z
---

# React: You Might Not Need an Effect 要約

React 公式ドキュメント（Learn）の「You Might Not Need an Effect」の要約である。
外部資料の要約であり、最終的な根拠は原典を参照すること。
要点は「Effect は React の外の仕組みと同期するための抜け道である」「外部の仕組みが関わらないなら Effect は要らない」「不要な Effect を消すとコードが読みやすく速くなり、バグも減る」の 3 つである。

## Effect が要らない 2 つの場面

出典: How to remove unnecessary Effects

- 描画のためのデータ変換に Effect は要らない。
  state を更新する Effect を書くと、React は更新のたびに描画をやり直してから画面に反映するので、無駄が多い。
- ユーザーの操作の処理に Effect は要らない。
  イベントハンドラの中なら、何が起きたか（どのボタンが押されたかなど）が分かる。
  Effect が動く時点では、ユーザーが何をしたかは分からない。
- 外部のシステムとの同期には Effect が必要である。
  例: jQuery のウィジェットを React の state に合わせる、検索語に合わせて検索結果を同期する。
- データ取得の Effect は、フレームワークの組み込みの仕組みのほうが効率がよい。

## props や state から決まる値

出典: Updating state based on props or state

- 既存の props や state から計算できる値は、state に入れず、描画中に計算する。
  例: `firstName` と `lastName` から `fullName` を作るとき、`fullName` を state にして Effect で更新しない。
- 描画中の計算にすると、余計な連鎖更新がなくなって速くなり、コードが減り、state 同士のずれによるバグも防げる。

## 重い計算のキャッシュ

出典: Caching expensive calculations

- まず state と Effect を消し、描画中に計算する。たいていはこれで十分である。
- 計算が重い場合や件数が多い場合は、`useMemo` で包む。
  関係のない state の変化では再計算されず、依存する値が変わったときだけ再計算される。
- `useMemo` の中身は描画中に動くので、純粋な計算でなければならない。
- 重いかどうかは、`console.time` などで時間を測って判断する。
  数千個のオブジェクトを作ったり回したりしない限り、たいていは重くない。
  合計で 1ms 以上かかるなら、メモ化を検討する。
- `useMemo` は最初の描画を速くしない。更新時の無駄を省くだけである。
- 開発環境では Strict Mode で 2 回描画されるなど、測定が不正確になる。
  正確に測るには、本番ビルドを使い、ユーザーに近い性能の端末で試す。
- React Compiler は、重い計算を自動でメモ化できる。多くの場合、手書きの `useMemo` は要らなくなる。

## props が変わったときに state をすべてリセットする

出典: Resetting all state when a prop changes

- props が変わったときに Effect で state を空にすると、古い値で一度描画してからもう一度描画することになる。
  入れ子の部品が state を持っていれば、それぞれにも同じ処理が要る。
- 代わりに、コンポーネントを外側と内側に分け、外側から内側へ `key` を渡す。
  例: `userId` を `key` にして `Profile` を描画する。
- React は、同じ位置の同じコンポーネントの state を保つ。
  `key` が変わると別のコンポーネントとして扱い、DOM を作り直して state をリセットする。
- 外側の部品を使う側は `key` を意識せず、`userId` を普通の props として渡すだけでよい。

## props が変わったときに state の一部を調整する

出典: Adjusting some state when a prop changes

- `items` が変わったら `selection` を `null` に戻す、のように一部だけ直したい場合も、Effect は避ける。
  Effect では、古い `selection` で描画し、DOM を更新し、`setSelection(null)` でもう一度描画することになる。
- 描画中に直接 state を調整する書き方がある。
  前回の `items` を state に保存しておき、`items !== prevItems` のときだけ `setSelection(null)` を呼ぶ。
  React は、描画を抜けた直後に、子を描画せずにすぐ描画をやり直す。
- 描画中に更新できるのは、同じコンポーネントの state だけである。
  ほかのコンポーネントの state を更新するとエラーになる。
  条件がないと無限ループになる。
- この書き方は Effect より効率がよいが、データの流れが分かりにくくなる。
  ほとんどのコンポーネントでは要らないので、先に `key` によるリセットと描画中の計算を検討する。
- 例えば、選択された項目の ID だけを state に持ち、`selection` は `items` から探して描画中に計算する。
  ID に合う項目がなければ `null` になるので、調整自体が要らなくなる。
  `items` が変わっても選択が残る挙動になり、たいていはこのほうがよい。

## イベントハンドラの間でロジックを共有する

出典: Sharing logic between event handlers

- 複数のボタン（Buy と Checkout など）で同じ通知を出したいとき、state を見る Effect にまとめない。
  ページを再読み込みすると、すでにカートに入っているだけで通知がまた出るバグになる。
- コードを置く場所に迷ったら、なぜそのコードを動かすのかを考える。
  Effect は、コンポーネントが表示されたことが理由で動かすコードにだけ使う。
- 通知はボタンを押したことが理由なので、共通の処理を関数に取り出し、それぞれのハンドラから呼ぶ。

## POST リクエストの送信

出典: Sending a POST request

- フォームの表示で送る分析用のイベントは、表示が理由なので Effect のままでよい。
- 登録ボタンを押したときの `/api/register` への POST は、その操作が理由なので、イベントハンドラに移す。
- 判断の基準は、ユーザーから見てどんな種類の処理かである。
  特定の操作が原因ならイベントハンドラ、画面に表示されたことが原因なら Effect に置く。

## 計算の連鎖

出典: Chains of computations

- ある state を直す Effect が別の state を変え、それがまた別の Effect を動かす、という連鎖は避ける。
  描画のたびに子まで描画し直す無駄が増える。
  要件が変わると連鎖が合わなくなる（過去の手に戻すと、連鎖がまた動いてしまう）。
- 描画中に計算できるものは計算し、残りの state の更新はイベントハンドラの中でまとめて行う。
- イベントハンドラの中では、state はスナップショットとして振る舞う。
  `setRound(round + 1)` の後でも、`round` は押した時点の値のままなので、次の値は `const nextRound = round + 1` のように自分で計算する。
- 次の state を直接計算できない場合もある。
  例: 前のドロップダウンの選択で、次のドロップダウンの選択肢をネットワークから取る場合は、ネットワークとの同期なので Effect の連鎖が適切である。

## アプリの初期化

出典: Initializing the application

- アプリの読み込みのときに 1 回だけ動かしたい処理を、最上位の Effect に書くと、開発環境では 2 回動く。
  認証トークンを無効にしてしまうなど、2 回呼ぶ想定のない処理だと問題になる。
- コンポーネントは、再マウントされても壊れないように作る。最上位の `App` も同じである。
- 「アプリの読み込みごとに 1 回」にしたい処理は、実行済みかを覚えておく最上位の変数で守る。
  あるいは、モジュールの初期化の時点（描画の前）で実行する。
- 最上位のコードは、インポートされただけで動く。
  この書き方は多用せず、`App.js` のような根のモジュールやエントリポイントに限る。

## 親への state 変更の通知

出典: Notifying parent components about state changes

- 子の state が変わったら Effect で `onChange` を呼ぶ書き方は、子の描画の後で親が更新され、描画が 2 回になる。
- Effect を消し、同じイベントハンドラの中で、子と親の両方の state を更新する。
  React は異なるコンポーネントの更新をまとめるので、描画は 1 回で済む。
- さらに、子の state をなくし、親から `isOn` を受け取る形（state のリフトアップ）にもできる。
  親の処理は増えるが、気にする state は減る。
  2 つの state を同期させようとしたら、まずリフトアップを検討する。

## 親へのデータの受け渡し

出典: Passing data to the parent

- 子が取得したデータを Effect で親に渡すと、データの流れが追いにくくなる。
- React ではデータは親から子へ流れる。
  おかしな表示を見つけたら、親を辿って原因を探せることが前提である。
- 親でデータを取得し、子へ props として渡す。

## 外部ストアの購読

出典: Subscribing to an external store

- React の state の外にあるデータ（サードパーティのライブラリやブラウザの API）は、React が知らないうちに変わるので、購読が必要になる。
  例: `navigator.onLine` の変化を Effect で購読して state に反映する。
- この用途には、専用の Hook である `useSyncExternalStore` を使うほうがよい。
  変わりうるデータを Effect で state に手で同期するより、間違いにくい。
- 繰り返しを避けるため、`useOnlineStatus()` のようなカスタムフックにまとめる。

## データの取得

出典: Fetching data

- データ取得の Effect は、イベントハンドラに移さなくてよい。
  検索欄は URL から初期値を入れることがあり、ユーザーが入力せずに戻る・進むこともあるので、取得の理由は入力のイベントではない。
  表示している間、現在の `page` と `query` の結果をネットワークと同期するので、Effect が適切である。
- ただし、素朴な実装には競合状態（race condition）のバグがある。
  素早く入力すると取得が何度も始まり、応答の順序は保証されない。
  古い応答が最後に届くと、誤った結果が表示される。
- 対策は、クリーンアップ関数で古い応答を無視することである（`ignore` フラグを立てる）。
- 競合状態のほかにも、応答のキャッシュ、サーバーでの取得（最初の HTML に内容を含める）、ネットワークの滝（子が親の取得を待つ遅延）の回避などの課題がある。
  これらは React に限らずどの UI ライブラリにもあり、簡単ではない。
  そのため、Effect での取得より、フレームワークの組み込みの取得の仕組みのほうが効率がよい。
- フレームワークを使わない場合は、取得のロジックを `useData` のようなカスタムフックに取り出す。
  エラー処理や読み込み中の管理も必要で、React の周辺にある既存の解決策を使ってもよい。
  フレームワークの仕組みほど効率はよくないが、後で移行しやすくなる。
- 素の `useEffect` を減らし、目的に合った宣言的な API のカスタムフックにすると、保守しやすくなる。

## まとめ

出典: Recap

- 描画中に計算できるものに、Effect は要らない。
- 重い計算のキャッシュには、`useEffect` ではなく `useMemo` を使う。
- コンポーネントの木全体の state をリセットするには、別の `key` を渡す。
- props の変化に応じて state の一部を直すには、描画中に設定する。
- 表示されたことが理由で動かすコードは Effect に、それ以外はイベントに置く。
- 複数のコンポーネントの state を更新するときは、1 回のイベントの中で行う。
- 別のコンポーネントの state を同期させようとしたら、リフトアップを検討する。
- Effect でデータを取得できるが、競合状態を防ぐクリーンアップが必要である。

## 練習問題

出典: Challenges

- 不要な state と Effect を消す（Transform data without Effects）。
  state は `todos` とチェックボックスの状態だけにし、表示する一覧とフッターの件数は描画中に計算する。
- Effect なしで計算をキャッシュする（Cache a calculation without Effects）。
  `useMemo` で包む。
  別の解として、入力欄の state を子コンポーネントに移すと、入力しても親が再描画されない。
- Effect なしで state をリセットする（Reset state without Effects）。
  フォームを内側のコンポーネントに分け、外側から ID を `key` として渡す。
- Effect なしでフォームを送信する（Submit a form without Effects）。
  メッセージの送信は、フォームの表示ではなく送信操作が理由なので、`handleSubmit` の中に移す。

## See also

- [You Might Not Need an Effect (React)](https://react.dev/learn/you-might-not-need-an-effect)
