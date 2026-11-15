---
type: reference
title: 'MDN: Using CSS custom properties 要約'
description: 'MDN Web Docs「Using CSS custom properties (variables)」の要約（宣言の方法、var() での参照、継承、@property による継承の制御、フォールバック、無効な値の扱い、JavaScript からの操作）。'
tags: [css, custom-properties, css-variables, mdn, at-property]
status: stable
verified: { by: claude-code/claude-sonnet-5-5, at: 2026-10-21T00:00:00Z }
stale_after: 2027-10-21T00:00:00Z
---

# MDN: Using CSS custom properties 要約

MDN Web Docs の「Using CSS custom properties (variables)」（CSS カスタムプロパティの使い方）の要約である。
外部資料の要約であり、最終的な根拠は原典を参照すること。
要点は「`--` で始まる名前で値を一か所に定義し `var()` で参照する」「`--` で定義したものは継承される」「`@property` で型・初期値・継承を制御できる」の 3 つである。

## 概要

出典: （冒頭の説明）

カスタムプロパティ（CSS 変数、カスケード変数とも呼ばれる）は、CSS の書き手が定義し、文書の中で再利用する値である。
`@property` at-rule、または `--primary-color: blue;` のような `--` 始まりの構文で設定する。
値の参照には `var()` 関数を使う（例: `color: var(--primary-color);`）。

- 複雑なサイトでは同じ値（例: 同じ色）が何百か所にも現れ、変えるには全ルールの検索と置換が要る。
  カスタムプロパティなら、値を一か所で定義して複数の場所から参照できる。
- `#00ff00` より `--main-text-color` のほうが意味が分かりやすい。
- `--` で定義したものは、カスケードの対象であり、親から値を継承する。
- `@property` を使うと、継承するか、初期値は何か、どの型の制約をかけるかを指定できる。

注意として、変数はメディアクエリやコンテナクエリの中では動かない。
`var()` は要素のどのプロパティの値の、どの部分にも使える。
一方、プロパティ名やセレクターなど、プロパティの値以外には使えない。

## カスタムプロパティの宣言

出典: Declaring custom properties

宣言の方法は 2 つある。

### `--` を接頭辞にする方法

- `--` に続けてプロパティ名（例: `--my-property`）を書き、値には有効な CSS の値なら何でも指定できる。
  ほかのプロパティと同じく、ルールセットの中に書く。
- ルールセットのセレクターが、そのカスタムプロパティを使える範囲（スコープ）を決める。
- 全体から参照できるよう、`:root` 擬似クラスに定義するのが一般的である。
  ただし、範囲を限る正当な理由があるなら、そうしなくてもよい。
- 名前は大文字・小文字を区別する（`--my-color` と `--My-color` は別物）。

```css
:root {
  --main-bg-color: brown;
}
```

### `@property` at-rule を使う方法

型を関連付け、既定値を決め、継承を制御するなど、より細かく定義できる。
次の例は、`<color>` を期待する `--logo-color` を作る。

```css
@property --logo-color {
  syntax: '<color>';
  inherits: false;
  initial-value: #c0ffee;
}
```

JavaScript で定義したり扱ったりするための API として、CSS Properties and Values API がある。

### `var()` での参照

どちらの方法で定義しても、標準の値の代わりに `var()` 関数の中で参照して使う。

```css
details {
  background-color: var(--main-bg-color);
}
```

## 最初の使い方と :root 擬似クラス

出典: First steps with custom properties / Using the :root pseudo-class

- 繰り返されている値は、カスタムプロパティに置き換えられる。
  例では、`.container` のスコープに `--main-bg-color: teal;` を定義し、複数のルールから `var(--main-bg-color)` で参照している。
- 宣言を階層の上位に置いて継承に任せられる場合もあるが、ある程度の規模のプロジェクトでは常にそうできるわけではない。
- `:root` に宣言して必要な所で使えば、繰り返しを減らせる。
  望む値の宣言が一か所の正本になり、後でプロジェクト全体の値を変えるときに役立つ。

## カスタムプロパティの継承

出典: Inheritance of custom properties

`@property` ではなく `--` で定義したカスタムプロパティは、常に親の値を継承する。

- 例では、`.two` に `--box-color: teal`、`.three` に `--box-color: pink` を設定し、すべての `div` が `background-color: var(--box-color)` を使う。
  結果は次の通りである。
  - `.one`: 無効な値（この方法で定義したものの既定値）
  - `.two`: `teal`
  - `.three`: `pink`
  - `.four`: `teal`（親から継承）
- カスタムプロパティは、ほかのプログラミング言語の変数とまったく同じには振る舞わない。
  値は使われる場所で計算され、スタイルシートの別の場所で使うために保存されるわけではない。
  たとえば、ある所で設定した値を、兄弟要素の子孫のルールで取り出すことはできない。
  設定されるのは、一致したセレクターとその子孫だけである。

### `@property` による継承の制御

`@property` では、継承するかどうかを明示できる。
例では、`inherits: false`、`<color>` 型、初期値 `teal` で `--box-color` を定義している。
親は `--box-color` を `green` にして背景色に使う。
子は `--box-color` を宣言していないので、`inherits: false` により、継承した `green` ではなく初期値の `teal` が使われる。

## フォールバック値

出典: Custom property fallback values

フォールバックは、`var()` 関数と `@property` の `initial-value` で定義できる。

注意として、フォールバックはカスタムプロパティ自体に未対応のブラウザの互換性の問題を直すものではない。
対応しているブラウザで、目的の変数がまだ未定義か値が無効なときに、別の値を使えるようにするものである。

### `var()` でのフォールバック

- 第 1 引数がカスタムプロパティの名前、第 2 引数が省略可能なフォールバック値で、参照先が無効なときの代わりの値になる。
  Custom Elements や Shadow DOM を扱うときに役立つ。
- 最初のカンマ以降のすべてが第 2 引数として扱われる。
  第 2 引数が無効ならフォールバックは失敗する。
- 複数のフォールバックを持たせる正しい方法は、フォールバックにカスタムプロパティを入れ子にすることである。
  ただし、入れ子の変数を辿るのに時間がかかるので、性能への影響に注意する。
- フォールバックに別のカスタムプロパティを使うときは、`var(--my-var, var(--my-background, pink))` のように `var()` を入れ子にする。
  `var(--my-var, --my-background, pink)` と書くと、`--my-background, pink` 全体が 1 つの値とみなされ、意図どおりに動かない。
- フォールバックにもカンマを含められる。
  `var(--foo, red, blue)` のフォールバックは `red, blue` である。

### `@property` の初期値によるフォールバック

`@property` で定義した `initial-value` も、フォールバックとして使える。
`<color>` を期待する `--box-color` に、綴りを誤った値（`peenk`）や色ではない値（`2rem`）を設定すると、どちらも無効な色なので、初期値の `teal` が適用される。

## 無効なカスタムプロパティ

出典: Invalid custom properties

- 通常のプロパティに無効な値（例: `color` に `16px`）があると、ブラウザはその宣言を捨てる。
  要素は、その宣言がなかった場合の値になる。
- カスタムプロパティの値を解析する時点では、ブラウザはそれがどこで使われるかを知らない。
  そのため、ほぼすべての値を有効とみなさなければならない。
  この値は `var()` を通じて、意味をなさない文脈で使われうる。
  これが「計算時に有効（valid at computed time）」という考え方につながる。
- 無効な `var()` の置換に出会うと、そのプロパティの初期値または継承値が使われる。
  `--text-color: 16px` を `color: var(--text-color)` で使う例では、次の 2 段階で処理される。
  1. `color` が継承されるプロパティかを確認する。そうだが、この `<p>` には `color` を設定した親がないので、次へ進む。
  1. 既定の初期値（黒）にする。
- `@property` で初期値を定義すると、このような予期しない結果を防げる。
  例では、`--text-color` を `<color>` 型、初期値 `teal` で定義している。

## JavaScript での値

出典: Values in JavaScript

カスタムプロパティの値の扱いは、標準のプロパティと同じである。

```js
// インラインスタイルから取得
element.style.getPropertyValue('--my-var');

// どこからでも（計算済みスタイルから）取得
getComputedStyle(element).getPropertyValue('--my-var');

// インラインスタイルに設定
element.style.setProperty('--my-var', jsVar + 4);
```

## See also

- [Using CSS custom properties (variables) - MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascading_variables/Using_custom_properties)
- [原典の Markdown (mdn/content)](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/cascading_variables/using_custom_properties/index.md)
