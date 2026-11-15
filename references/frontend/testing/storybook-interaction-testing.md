---
type: reference
title: 'Storybook: Interaction tests 要約'
description: 'Storybook 公式ドキュメント「Interaction tests」の要約（play 関数、canvas と Testing Library のクエリ、userEvent、expect、fn、mount、beforeEach と afterEach、step、モックしたモジュール、実行、デバッグ、CI、トラブルシューティング）。'
tags: [storybook, testing, interaction-testing, play-function, testing-library]
status: stable
verified: { by: claude-code/claude-sonnet-5-5, at: 2026-10-21T00:00:00Z }
stale_after: 2027-10-21T00:00:00Z
---

# Storybook: Interaction tests 要約

Storybook 公式ドキュメント「Writing tests」の「Interaction tests」の要約である。
外部資料の要約であり、最終的な根拠は原典を参照すること。
要点は「インタラクションテストはストーリーの一部として書く」「play 関数でユーザーの操作を再現し、結果を assert する」「Interactions パネルでデバッグし、Vitest アドオンで自動実行する」の 3 つである。

## 概要

出典: Interaction tests（冒頭）

- インタラクションテストは、ストーリーの一部として作る。
  ストーリーが、必要な props と context を与えて、コンポーネントを初期状態で描画する。
- そのあと play 関数で、クリック、入力、フォームの送信といったユーザーの操作を再現し、最終的な結果を assert する。
- Storybook の UI の Interactions パネルで、テストをプレビューしてデバッグできる。
- Vitest アドオンで自動化でき、Storybook、ターミナル、CI のどこでも実行できる。

## インタラクションテストの書き方

出典: Writing interaction tests

- すべてのストーリーは、描画テスト（render test）にできる。
  描画テストは、あるコンポーネントが、ある状態で描画できるかだけを調べる簡易版のインタラクションテストである。
  Button のような単純で静的なコンポーネントなら、これで足りる。
- より複雑で対話のあるコンポーネントでは、`play` 関数で DOM の構造や関数の呼び出しといった機能面も assert できる。
  コンポーネントをテストするとき、play 関数が実行され、その中の assertion が検証される。
- 原典の例では、LoginForm コンポーネントに対して、EmptyForm ストーリーが描画を、FilledForm ストーリーがフォームの送信をテストしている。
  以降は、この例で使う API を 1 つずつ説明している。

## canvas でクエリする

出典: Querying the `canvas`

- `canvas` は、テスト対象のストーリーを含む、クエリできる要素である。
  play 関数の引数として渡される。
- クエリのメソッドはすべて Testing Library のもので、`<type><subject>` の形をしている。

| 種類            | 0 件   | 1 件       | 2 件以上   | await  |
| :-------------- | :----- | :--------- | :--------- | :----- |
| `getBy...`      | エラー | 要素を返す | エラー     | しない |
| `queryBy...`    | `null` | 要素を返す | エラー     | しない |
| `findBy...`     | エラー | 要素を返す | エラー     | する   |
| `getAllBy...`   | エラー | 配列を返す | 配列を返す | しない |
| `queryAllBy...` | `[]`   | 配列を返す | 配列を返す | しない |
| `findAllBy...`  | エラー | 配列を返す | 配列を返す | する   |

- subject は次の 8 種類で、原典はこの順に使うことを勧めている。
  1. `ByRole`: アクセシブルなロールで探す。
  1. `ByLabelText`: 関連付けられたラベルのテキストで探す。
  1. `ByPlaceholderText`: placeholder の値で探す。
  1. `ByText`: 含まれるテキストで探す。
  1. `ByDisplayValue`: `input`、`textarea`、`select` を現在の値で探す。
  1. `ByAltText`: `alt` 属性の値で探す。
  1. `ByTitle`: `title` 属性の値で探す。
  1. `ByTestId`: `data-testid` 属性の値で探す。
- 実際の人が UI を操作する形に近いクエリを使うことを、Storybook と Testing Library は強く勧めている。
  たとえばロールで探せば、より多くの人がそのコンポーネントを使えることの確認にもなる。
  `data-testid` は、ほかの方法をすべて試したあとの最後の手段である。
- 原典には、`findByRole('button', { name: 'Submit' })`、`getByText`、`getAllByRole('listitem')` といった典型的なクエリの例がある。
- Web Components では、shadow DOM の中を `shadow-dom-testing-library` で探せる。
  `findByRole` に対する `findByShadowRole` のように、境界を越えるクエリが用意されている。
  `.storybook/preview.*` に設定を足すと、`canvas` からも使える。

## userEvent で操作を再現する

出典: Simulating behavior with `userEvent`

- クエリで要素を見つけたあと、`userEvent` でその要素を操作する。
  `userEvent` も play 関数の引数として渡され、ボタンのクリック、入力欄への入力、選択肢の選択などを再現する。
- よく使うメソッドは次のとおりである。全体は `user-event` のドキュメントにある。

| メソッド          | 内容                               |
| :---------------- | :--------------------------------- |
| `click`           | 要素をクリックする                 |
| `dblClick`        | 要素を 2 回クリックする            |
| `hover`           | 要素にホバーする                   |
| `unhover`         | 要素からホバーを外す               |
| `tab`             | Tab キーを押す                     |
| `type`            | 入力欄や textarea に文字を入力する |
| `keyboard`        | キーボードのイベントを再現する     |
| `selectOptions`   | select の選択肢を選ぶ              |
| `deselectOptions` | select の選択肢の選択を外す        |
| `clear`           | 入力欄のテキストを選択して削除する |

- `userEvent` のメソッドは、play 関数の中で必ず `await` する。
  そうすると、Interactions パネルで正しく記録され、デバッグできる。

## expect で assert する

出典: Asserting with `expect`

- クエリと操作のあと、結果を `expect` で assert する。
  assertion は、テストの実行時に検証される。
- `expect` は `storybook/test` モジュールから import する。

```js
import { expect } from 'storybook/test';
```

- この `expect` は、Vitest の `expect` と `@testing-library/jest-dom` のマッチャーを合わせたものである。
  jest-dom は名前に jest とあるが、Vitest のテストでも使える。
- よく使うメソッドは次のとおりである。
  - `toBeInTheDocument()`: 要素が DOM にあるか。
  - `toBeVisible()`: 要素がユーザーに見えているか。
  - `toHaveAttribute()`: 要素が属性を持つか。
  - `toHaveBeenCalled()`: スパイした関数が呼ばれたか。
  - `toHaveBeenCalledWith()`: スパイした関数が特定の引数で呼ばれたか。
- `expect` の呼び出しも、play 関数の中で必ず `await` する。
  理由は `userEvent` と同じで、Interactions パネルでの記録とデバッグのためである。

## fn で関数をスパイする

出典: Spying on functions with `fn`

- コンポーネントが関数を呼ぶとき、Vitest の `fn` でその関数をスパイし、挙動を assert できる。
  `fn` も `storybook/test` から import する。
- 多くの場合、ストーリーを書くときに `fn` を `arg` の値として渡し、テストの中でその `arg` を参照する。

```js
import { fn } from 'storybook/test';
```

## 描画の前にコードを実行する

出典: Run code before the component gets rendered

- Angular 以外では、play 関数の `mount` で、描画の前にコードを実行できる。
  原典の例では、`mockdate` パッケージで `Date` をモックし、ストーリーを常に同じ状態で描画している。
- `mount` を使うには 2 つの条件がある。
  1. play 関数に渡される `context` から、`mount` を分割代入で受け取る。
     こうしないと、play 関数が始まる前に Storybook が描画を始めてしまう。
  1. フレームワークまたはビルダーが、ES2017 以上へトランスパイルする設定になっている。
     そうでないと、分割代入と async/await が変換され、Storybook が `mount` の使用を認識できない。
- React、Vue、Svelte では、`mount` でモックデータを作ってから渡せる。
  play 関数でデータ（原典の例ではモックのノート）を作り、それを設定したコンポーネントで `mount` を呼ぶ。
  - 引数なしで `mount()` を呼ぶと、ストーリーの描画関数（暗黙の既定、または明示した独自の定義）で描画される。
  - `mount` の中で特定のコンポーネントを指定すると、ストーリーの描画関数は無視される。
    そのため、`args` をそのコンポーネントへ渡す必要がある。
- Angular では、非同期の `beforeEach` 関数を定義して、描画の前にコードを実行する。

## ファイル内の各ストーリーの前にコードを実行する

出典: Run code before each story in a file

- 同じファイルのすべてのストーリーの前に同じコードを実行したいときは、コンポーネントの meta に非同期の `beforeEach` を足す。
  コンポーネントやモジュールの初期状態の設定が、その例である。
- `beforeEach` からクリーンアップ関数を返すと、各ストーリーの後（再マウントされたとき、または別のストーリーへ移ったとき）に実行される。
- 一般には、状態のリセットはプレビューファイルの `beforeAll` か `beforeEach` に書き、プロジェクト全体に効かせることを勧めている。
  コンポーネントに特有の事情があるときだけ、meta の `beforeEach` が返すクリーンアップ関数を使う。

## すべてのテストの状態を設定、リセットする

出典: Set up or reset state for all tests

- コンポーネントの状態を変えたら、テスト同士を独立に保つため、別のストーリーを描画する前にその状態をリセットする。
  リセットには `beforeAll` と `beforeEach` の 2 つがある。
- プレビューファイル（`.storybook/preview.*`）の `beforeAll` は、プロジェクトのどのストーリーよりも前に 1 回だけ実行される。
  - ストーリー間では再実行されない。
    プレビューファイルが更新されない限り、最初の実行以外では動かない。
  - プロジェクト全体が依存する初期設定に向いている。
  - クリーンアップ関数を返すと、`beforeAll` の再実行の前、またはテストランナーの終了処理のときに実行される。
- プレビューファイルの `beforeEach` は、プロジェクトの各ストーリーの前に実行される。
  - ほとんどのストーリーが使う状態やモジュールのリセットに向いている。
    原典の例では、モックした Date のリセットに使っている。
  - 返したクリーンアップ関数は、各ストーリーの後に実行される。
- `fn()` のモックは、描画の前に Storybook が自動で復元するので、自分で復元する必要はない。
  詳細は `parameters.test.restoreMocks` の API にある。

## 操作のあとに assert する

出典: Make assertions after interactions

- `afterEach` は、ストーリーが描画され、play 関数が終わったあとに実行される。
  - プロジェクト全体はプレビューファイル、コンポーネントは meta、ストーリー単体はストーリーの定義に書ける。
  - 最終的な描画結果の確認や、情報の記録に向いている。
  - play 関数と同じく `context`（`args`、`canvas` など）を受け取る。
- 状態のリセットには `afterEach` を使わない。
  ストーリーの後にリセットすると、ストーリーの最終的な状態を正しく見られなくなる恐れがある。
  代わりに `beforeEach` が返すクリーンアップ関数を使う。
  これは、別のストーリーへ移るときだけ実行されるので、最終状態が保たれる。

## step で操作をまとめる

出典: Group interactions with the step function

- 複雑な流れでは、関連する操作を `step` 関数でまとめ、内容を表すラベルを付けられる。
- Interactions パネルでは、まとめた操作が折りたためるグループとして入れ子で表示される。

## モックしたモジュール

出典: Mocked modules

- コンポーネントが import しているモジュールに依存するときは、そのモジュールをモックして、挙動を制御し、assert できる。
  方法は、別の「mocking modules」のガイドにある。
- モックしたモジュールには Vitest のモック関数のメソッドがあり、ストーリーに import して、コンポーネントの挙動の assert に使える。

## インタラクションテストを実行する

出典: Running interaction tests

- Vitest アドオンを使っていれば、次のいずれかで実行できる。
  - Storybook の UI
  - エディタ
  - CLI
  - CI 環境
- Storybook の UI では、サイドバーの展開したテストウィジェットの「Run component tests」ボタンで実行できる。
  ストーリーやフォルダのコンテキストメニュー（3 点）から「Run component tests」を選んでもよい。

## インタラクションテストをデバッグする

出典: Debugging interaction tests

- Interactions パネルには、各ストーリーの play 関数に書いた流れが 1 つずつ表示される。
  一時停止、再開、巻き戻し、1 つずつ進めるといった操作もできる。
- テストの失敗もここに表示され、失敗した箇所をすぐに特定できる。
  原典の例では、Log in ボタンを押したあとに `submitted` の状態を設定する処理が抜けている。
- Storybook は Web アプリなので、URL を知っていれば誰でも、環境の設定やツールなしに、同じ詳しい情報で失敗を再現できる。
  プルリクエストごとに Storybook を自動で公開すると、チームが共通の参照先としてテストとデバッグに使える。

## CI で自動化する

出典: Automate with CI

- Vitest アドオンでテストを実行していれば、自動化は CI でそのテストを実行するだけでよい。
  詳細は「testing in CI」のガイドにある。
- Vitest アドオンには、Vite ベースのフレームワークが必要である。
  Webpack を使っているプロジェクトは、先に Vite へ移行する。

## トラブルシューティング

出典: Troubleshooting

- インタラクションテストと視覚テストの違い。
  - すべてのコンポーネントにインタラクションテストを適用すると、保守に手間がかかる。
  - 視覚テストなどほかの方法と組み合わせると、保守の手間を抑えて広く確認できる。
- インタラクションテストと、Vitest と Testing Library だけを使う場合との違い。
  - インタラクションテストは、Vitest と Testing Library を Storybook に統合したものである。
  - 最大の利点は、テスト対象のコンポーネントを実ブラウザで見られることである。
    コマンドラインに偽の DOM のダンプが出るだけの状況や、JSDOM によるブラウザ機能のモックの限界を避けられる。
  - ストーリーとテストを 1 つのファイルにまとめられるのも便利である。

## See also

- [Interaction tests (Storybook)](https://storybook.js.org/docs/writing-tests/interaction-testing)
- [interaction-testing.mdx (storybookjs/storybook)](https://github.com/storybookjs/storybook/blob/next/docs/writing-tests/interaction-testing.mdx)
