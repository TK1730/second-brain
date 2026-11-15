---
type: reference
title: 'The Component Gallery: Components 一覧 要約'
description: 'The Component Gallery の Components 一覧ページと About ページの要約（サイトの目的、コンポーネントの定義、名前と別名の扱い、コンポーネントの一覧と一行説明）。'
tags: [component-gallery, ui, components, design-system, naming]
status: stable
verified: { by: claude-code/claude-sonnet-5-5, at: 2026-10-21T00:00:00Z }
stale_after: 2027-10-21T00:00:00Z
---

# The Component Gallery: Components 一覧 要約

The Component Gallery の Components 一覧ページ（と、サイトの説明がある About ページ）の要約である。
このサイトは、実在のデザインシステムから集めた UI コンポーネントの事例集である。
外部資料の要約であり、最終的な根拠は原典を参照すること。
要点は「コンポーネントは再利用できる UI の部品であり、名前の揺れを別名つきで一覧にしている」である。

## サイトの位置づけ

出典: About

- The Component Gallery は、実在のデザインシステムにあるインターフェースのコンポーネントを集めたものである。
- 作者（Iain Bean）が、フロントエンド開発者として日々直面する次の問題に対処するために作った。
  - 解決済みのインターフェースの問題がある。
    他の人がすでに解いた問題を、新しいプロジェクトのたびに作り直す必要はない。
  - 名前を付けるのは難しい。
    ものの呼び方に迷ったら、他の人が似たものを何と呼んでいるかを見るのが出発点になる。
- 注意書きとして、人気があるというだけで意見や技法が正しいと考えてはいけない、としている。
  情報のカスケード（多数に流されること）に注意し、可能なら調査に基づいて判断する。
  他の全員がやっていることをそのまま真似してはいけない。
- 着想は、1977 年の建築・都市計画の本 A Pattern Language（250 を超える「パターン」を記述）にある。
  - この本のパターンは、特定の文脈に合う形、言い換えると設計上の問題の解決策である。
  - このサイトは、Web に現れるパターンを扱う。
    Web ではそれらは、より一般にコンポーネントと呼ばれる。
  - コンポーネントライブラリと違い、大半はそのまま使える部品ではない。
    自分の問題に合う解決策を設計するときの着想源になることを狙っている。

## コンポーネントとは

出典: About > Questions and Answers

- コンポーネントとは、再利用できるユーザーインターフェースの 1 つのまとまりである。
- コンポーネントを軸に設計する利点として、次の 3 つを挙げている。
  - 一貫性: 複数のインターフェースで、見た目と操作感をそろえやすい。
  - 再利用性: 試されて動くと分かっているものを使うことで、開発を速められる。
  - 共通の言葉: コンポーネントの名前を共有することで、関わるチーム全体が意思疎通しやすい。
- コンポーネントは別のコンポーネントを含められる。
  この入れ子で画面を組み立てる考え方は、Atomic Design などの方法論の基本である。
- Web Components は、ブラウザの機能と JavaScript の API の集まりであり、コンポーネントを作る標準の方法である。
  React、Vue、Angular、Svelte のコンポーネントも、コンポーネントである。
- コンポーネントは Web サイトだけのものではない。
  Web から集めているのは、公開されているデザインシステムを見つけやすいからである。
- デザインシステムとコンポーネントライブラリは別物である。
  デザインシステムは、配色、タイポグラフィ、プロセス、アクセシビリティ、ツール、トーンなどを含む、進化し続ける共有の実践である。
  使う人と貢献する人がいなければ失敗する。
  コンポーネントには、いつ、どのように使うか（と使わないか）の指針を添えるべきだとしている。

## 一覧ページの構成

出典: Components

- ページは、コンポーネントを名前の順、または事例（Example）の数の順に並べて表示できる。
- 各コンポーネントには、次の項目がある。
  - 名前
  - 事例の数（そのコンポーネントを載せたデザインシステムの事例の件数）
  - 別名（他のデザインシステムでの呼び方。ないものもある）
  - 一行の説明
- 一覧にはカテゴリの見出しによる分類はなく、コンポーネントが 1 つの平らな並びで並ぶ。
- 同じものが別の名前で呼ばれることがあるため、別名を併記している。
  例: Modal は Dialog や Popup とも呼ばれる。
- 名前が近いコンポーネントは、説明の中で違いが述べられている。
  例: Popover は Tooltip と違い、クリックで開き、操作できる要素を含められる。
  Dropdown menu は Select と違い、フォーム入力ではなく操作や移動の選択肢を示す。

## コンポーネント一覧

出典: Components

以下は、サイトの説明の要約である。
別名はサイトに書かれているものをそのまま載せる（ないものは「-」）。

並びは原典と同じく名前順にした。

| 名前               | 別名                                                                                                                  | 説明                                                                                                                         |
| :----------------- | :-------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------- |
| Accordion          | Arrow toggle, Collapse, Collapsible sections, Collapsible, Details, Disclosure, Expandable, Expander, ShowyHideyThing | 縦に並んだ見出しで、項目ごとに追加の情報を開閉する。閉じると短いラベルだけが見える。                                         |
| Alert              | Notification, Feedback, Message, Banner, Callout                                                                      | 重要な変更を目立つ形で利用者に知らせる。                                                                                     |
| Avatar             | -                                                                                                                     | 利用者を表す図。写真、イラスト、頭文字などが使われる。                                                                       |
| Badge              | Tag, Label, Chip                                                                                                      | 別の大きな部品の中や近くに置く小さなラベル。状態や属性などのメタデータを表す。                                               |
| Breadcrumbs        | Breadcrumb trail                                                                                                      | ナビゲーション階層における現在のページの位置を示すリンクの並び。                                                             |
| Button             | -                                                                                                                     | フォームの送信や、他の部品の表示と非表示など、操作を起こす。                                                                 |
| Button group       | Toolbar                                                                                                               | 関連する複数のボタンを包む入れ物。                                                                                           |
| Card               | Tile                                                                                                                  | 連絡先、記事、タスクなど、1 つの対象を表す内容の入れ物。                                                                     |
| Carousel           | Content slider                                                                                                        | 複数のスライドを 1 つまたは複数ずつ表示する。スワイプ、スクロール、ボタンで移動できる。                                      |
| Checkbox           | -                                                                                                                     | 定義済みの選択肢から選ぶ入力。単独では二択（オン/オフ）、グループでは複数を選べる。                                          |
| Color picker       | -                                                                                                                     | 色を選ぶ入力。                                                                                                               |
| Combobox           | Autocomplete, Autosuggest                                                                                             | Select に似るが、選択肢を絞り込む自由入力のテキストがある。                                                                  |
| Date input         | -                                                                                                                     | 日付を入力する手段。日、月、年を別々の欄に分けることが多い。                                                                 |
| Datepicker         | Calendar, Datetime picker                                                                                             | カレンダーの表示で日付を選ぶ視覚的な方法。                                                                                   |
| Drawer             | Tray, Flyout, Sheet                                                                                                   | 画面の端からスライドして出るパネル。                                                                                         |
| Dropdown menu      | Select menu                                                                                                           | 選択肢が最初は隠れていて、ボタン操作で表示されるメニュー。フォーム入力ではなく操作やナビゲーションを示す点が Select と違う。 |
| Empty state        | -                                                                                                                     | 現在の表示に出すデータがないことを示す。別の操作（検索語を変えるなど）を添えることが多い。                                   |
| Fieldset           | -                                                                                                                     | 関連するフォーム欄をまとめる入れ物。                                                                                         |
| File               | Attachment, Download                                                                                                  | アップロードした添付ファイルや、ダウンロードできる PDF などのファイルの表現。                                                |
| File upload        | File input, File uploader, Dropzone                                                                                   | 利用者が自分の端末からファイルをアップロードできる入力。                                                                     |
| Footer             | -                                                                                                                     | ページや節の下部に置き、著作権や法的情報、関連内容へのリンクを示す。                                                         |
| Form               | -                                                                                                                     | 利用者が情報をサーバーへ送るための入力部品のまとまり。                                                                       |
| Header             | -                                                                                                                     | 全ページの上部に出る要素。通常はサイト名と主要なナビゲーションを含む。                                                       |
| Heading            | -                                                                                                                     | 新しい節を始めるための題名や見出し。                                                                                         |
| Hero               | Jumbotron, Banner                                                                                                     | ページの最初のほうに置く大きなバナー。幅いっぱいの画像を含むことが多い。                                                     |
| Icon               | -                                                                                                                     | インターフェースの要素の目的を視覚的に示す記号の絵。                                                                         |
| Image              | Picture                                                                                                               | 画像を埋め込む要素。                                                                                                         |
| Label              | Form label                                                                                                            | フォームの入力に付けるテキストのラベル。                                                                                     |
| Link               | Anchor, Hyperlink                                                                                                     | 資源への参照。外部（別のページ）でも内部（同じ文書内の要素）でもよい。                                                       |
| List               | -                                                                                                                     | 関連する項目をまとめる。HTML には順序なし、順序つき、説明（キーと値の組）の 3 種類がある。                                   |
| Modal              | Dialog, Popup, Modal window                                                                                           | 他の内容の上に現れ、下に戻る前に利用者の操作を求める要素。                                                                   |
| Navigation         | Nav, Menu                                                                                                             | ナビゲーションのリンクの入れ物。他のページ向けでも、現在のページ内の要素（目次など）向けでもよい。                           |
| Pagination         | -                                                                                                                     | 情報を複数のページに分けること。また、そのページ間を移動するための部品の名前でもある。                                       |
| Popover            | -                                                                                                                     | 別の要素から他の内容の上に現れる要素。Tooltip と違い、通常はクリックで開き、操作できる要素を含められる。                     |
| Progress bar       | Progress                                                                                                              | 長い処理の完了状況を示す横棒。段階ではなく連続的に更新されることが多い。                                                     |
| Progress indicator | Progress tracker, Stepper, Steps, Timeline, Meter                                                                     | 複数の離散的な段階のうち、利用者がどこまで進んだかの表現。                                                                   |
| Quote              | Pull quote, Block quote                                                                                               | 人や外部の資料からの引用、または文書内の一節を強調するための引用を表示する。                                                 |
| Radio button       | Radio, Radio group                                                                                                    | 定義済みの選択肢から 1 つだけ選ばせる。                                                                                      |
| Rating             | -                                                                                                                     | 商品などの星評価を見せる、または設定させる。                                                                                 |
| Rich text editor   | RTE, wysiwyg editor                                                                                                   | 書式つきの「リッチテキスト」を、通常は WYSIWYG の画面で編集する。                                                            |
| Search input       | Search                                                                                                                | 検索語を入力して内容を探させる。                                                                                             |
| Segmented control  | Toggle button group                                                                                                   | Button group、Radio button、Tabs の中間のような部品。選択肢や表示を切り替える。                                              |
| Select             | Dropdown, Select input                                                                                                | 値を選ぶフォーム入力。閉じると選択中の項目、開くとスクロールできる定義済みの選択肢の一覧を示す。                             |
| Separator          | Divider, Horizonal rule, Vertical rule                                                                                | 2 つの要素の間の区切り。通常は横線。                                                                                         |
| Skeleton           | Skeleton loader                                                                                                       | まだ読み込まれていない内容の場所取り。灰色の箱で組むことが多い。                                                             |
| Skip link          | -                                                                                                                     | ページ内の別の節へ飛ぶためのリンク。主にキーボードで操作する利用者向け。                                                     |
| Slider             | Range input                                                                                                           | あらかじめ決めた範囲の中から値を選ぶフォームの部品。                                                                         |
| Spinner            | Loader, Loading                                                                                                       | 裏で処理が進んでいて、まだ操作できないことを示す視覚的な表示。                                                               |
| Stack              | -                                                                                                                     | 部品の間に一定の余白を入れるための包む部品。                                                                                 |
| Stepper            | Nudger, Quantity, Counter                                                                                             | ボタンで数値を増減して編集する部品。                                                                                         |
| Table              | -                                                                                                                     | 大量のデータを行と列で表示する。並べ替えや絞り込みがあるものは「Data Table」と呼ばれる。                                     |
| Tabs               | Tabbed interface                                                                                                      | 複数のパネルを切り替えて、散らかりを減らし、狭い場所に多くを収める。                                                         |
| Text input         | -                                                                                                                     | 1 行のテキストを受け付けるフォームの部品。                                                                                   |
| Textarea           | Textbox, Text box                                                                                                     | 複数行のテキストを編集するフォームの部品。                                                                                   |
| Toast              | Snackbar                                                                                                              | 他の内容の上の層に現れる Alert の一種。モバイルやデスクトップのプッシュ通知に似る。                                          |
| Toggle             | Switch, Lightswitch, Toggle button                                                                                    | 2 つの状態（多くはオンとオフ）を切り替える部品。                                                                             |
| Tooltip            | Toggletip                                                                                                             | 要素の説明や追加情報を、通常はホバーで、クリックやタップでも表示する。                                                       |
| Tree view          | -                                                                                                                     | 目次やディレクトリ構造のように、入れ子の階層的な情報を表示する。                                                             |
| Video              | Video player                                                                                                          | 動画を表示する部品。再生を操作するコントロールを含むことが多い。                                                             |
| Visually hidden    | Screenreader only                                                                                                     | 支援技術の利用者に追加の文脈を伝えるための、見えないテキスト。                                                               |

## See also

- [The Component Gallery: Components](https://component.gallery/components/)
- [The Component Gallery: About](https://component.gallery/about/)
