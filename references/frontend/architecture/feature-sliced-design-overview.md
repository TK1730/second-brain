---
type: reference
title: 'Feature-Sliced Design: 概要と構成の要約'
description: 'Feature-Sliced Design 公式ドキュメントの Overview と、リファレンスの Layers、Slices and Segments、Public API の要約（レイヤー、スライス、セグメント、レイヤー間の import の規則、公開 API、段階的な導入）。'
tags: [feature-sliced-design, fsd, architecture, frontend]
status: stable
verified: { by: claude-code/claude-sonnet-5-5, at: 2026-10-21T00:00:00Z }
stale_after: 2027-10-21T00:00:00Z
---

# Feature-Sliced Design: 概要と構成の要約

Feature-Sliced Design（FSD）の公式ドキュメントのうち、Overview と、リファレンスの Layers、Slices and Segments、Public API の 4 ページの要約である。
要約は、公式リポジトリ（feature-sliced/documentation）にある英語の原文（mdx）から作った。
外部資料の要約であり、最終的な根拠は原典を参照すること。
要点は「コードを レイヤー › スライス › セグメント の 3 段で分ける」「スライスは自分より厳密に下のレイヤーだけを import できる」「スライスの外からは公開 API だけを使う」の 3 つである。

## FSD とは

出典: Overview

- FSD は、フロントエンドのアプリケーションを組み立てるための設計の方法論である。
  端的には、コードの整理に関する規則と慣習の集まりである。
- 主な目的は、変わり続ける業務の要件のもとで、プロジェクトを理解しやすく安定した状態に保つことである。
- 対象は、フロントエンド（Web、モバイル、デスクトップなどの UI）のアプリケーションであり、ライブラリではない。
- プログラミング言語、UI フレームワーク、状態管理ライブラリに制限はない。
  段階的な導入、モノレポでの利用、アプリをパッケージに分けて各パッケージで FSD を実装することもできる。

## レイヤー

出典: Overview > Layers / Layers

- レイヤーは、組織の階層の 1 段目である。
  目的は、コードが担う責務の大きさと、アプリ内の他のモジュールへの依存の多さで、コードを分けることである。
- レイヤーの名前は、すべての FSD プロジェクトで標準化されている。
  すべてのレイヤーを使う必要はないが、名前は重要である。
- レイヤーは 7 つあり、責務と依存が大きい順に上から並ぶ。
  1. App: アプリを動かすものすべて（ルーティング、エントリーポイント、グローバルスタイル、プロバイダー）。
  1. Processes（非推奨）: 複数ページにまたがる複雑なシナリオ。
  1. Pages: ページ全体、またはネストしたルーティングでのページの大きな一部。
  1. Widgets: それだけで完結する、機能や UI の大きなまとまり。たいてい 1 つのユースケースを丸ごと実現する。
  1. Features: 製品の機能全体の、再利用される実装。ユーザーに業務上の価値をもたらす操作。
  1. Entities: プロジェクトが扱う業務上の実体（`user`、`product` など）。
  1. Shared: 再利用できる機能。特にプロジェクトや業務の個別事情から切り離されたもの（必ずしもそうでなくてよい）。
- レイヤーは小文字の名前のフォルダーである（`shared`、`pages`、`app`）。
  意味が標準化されているため、新しいレイヤーの追加は推奨されない。

## レイヤー間の import の規則

出典: Layers > Import rule on layers

> A module (file) in a slice can only import other slices when they are located on layers strictly below.

- スライスのモジュール（ファイル）は、自分より厳密に下のレイヤーにあるスライスだけを import できる。
  - 例: `~/features/aaa/api/request.ts` は、`~/features/bbb` の中のどのファイルからも import できない。
  - 例: 同じ `~/features/aaa` の中のファイル、`~/entities`、`~/shared` からは import できる。
- App と Shared は、この規則の例外である。
  この 2 つは、レイヤーであると同時にスライスでもある。
  Shared には業務ドメインがなく、App はすべての業務ドメインをまとめるためである。
- 実際には、App と Shared はセグメントで構成され、セグメント同士は自由に import し合える。

## 各レイヤーの定義

出典: Layers > Layer definitions

- Shared
  - 他の部分の土台である。
    バックエンド、サードパーティのライブラリ、環境など外の世界との接続や、自前の独立したライブラリを置く。
- Entities
  - 実世界の概念を表す（SNS なら User、Post、Group）。
  - 実体同士が関わる業務ロジックは、Features や Pages のような上のレイヤーに置くほうが望ましい。
  - 実体のデータが別の実体を含む場合は、`@x` 表記でスライスの分離を迂回し、関係を明示するのがたいてい良い。
    関連する実体は一緒にリファクタリングする必要があり、関係を見落とせないようにするためである。
- Features
  - ユーザーが行いたい、アプリの主な操作を置く。
  - すべてが Feature である必要はない。
    複数のページで再利用されることが、Feature にすべき目安である。
- Widgets
  - 再利用できる UI のまとまりを置くレイヤーである。
  - このガイドは、Widgets の使用を推奨しない。
    UI のまとまりにデータ取得や状態管理などのユーザーフローの処理が入りやすく、Features との責務が重なって境界が曖昧になるためである。
  - Widget を作らないとは、別のレイヤーへ移すことである。
    画面固有の組み合わせは `pages`、複数ページで再利用する操作は `features`、業務と関係のない共通 UI は `shared`、アプリ全体のレイアウトは `app` に置く。

## スライス

出典: Slices and Segments > Slices

- スライスは、組織の階層の 2 段目である。
  主な目的は、コードを製品、業務、アプリにとっての意味でまとめることである。
- 名前は標準化されておらず、アプリの業務ドメインで決まる。
  例: 写真ギャラリーなら `photo`、`effects`、`gallery-page`。SNS なら `post`、`comments`、`news-feed`。
- Shared と App にスライスがないのは、Shared には業務ロジックがなく、App にはアプリ全体のコードしかないためである。
- 理想のスライスは、同じレイヤーの他のスライスから独立し（結合ゼロ）、主な目的に関わるコードの大半を含む（高い凝集）。
  この独立性は、レイヤー間の import の規則で守られる。
- 関連の深いスライスは、フォルダーにまとめてよい。
  ただし他のスライスと同じ分離の規則に従い、そのフォルダーの中でコードを共有してはならない。

## セグメント

出典: Slices and Segments > Segments / Overview > Segments

- セグメントは、組織の階層の 3 段目（最後）で、コードを技術的な性質でまとめる。
- 標準化された名前は次の 5 つである。
  - `ui`: UI の表示に関するものすべて（UI の部品、日付の整形、スタイルなど）。
  - `api`: バックエンドとのやり取り（リクエストの関数、データ型、マッパーなど）。
  - `model`: データモデル（スキーマ、インターフェース、ストア、業務ロジック）。
  - `lib`: そのスライスの他のモジュールが必要とするライブラリのコード。
  - `config`: 設定ファイルとフィーチャーフラグ。
- 独自のセグメントも作れる。
  最も多いのは、スライスが意味をなさない App と Shared である。
- 名前は、中身の本質ではなく目的を表す。
  `components`、`hooks`、`types` は、コードを探すときに役立たないので悪い名前である。

## 公開 API

出典: Public API / Slices and Segments > Public API rule on slices

- 公開 API（public API）は、スライスのようなモジュールの集まりと、それを使うコードとの間の契約である。
  特定のオブジェクトにだけ、その公開 API を通してアクセスできるようにする門の役目もある。
- 実際には、再エクスポートを並べた index ファイルで実装することが多い。
- スライスの公開 API の規則は次のとおりである。
  - すべてのスライス（スライスのないレイヤーではセグメント）は、公開 API の定義を含まなければならない。
  - 外のモジュールが参照できるのは公開 API だけで、内部のファイル構成は参照できない。
- よい公開 API の目標は次の 3 つである。
  1. スライスの構造の変更（リファクタリングなど）から、アプリの他の部分を守る。
  1. 以前の期待を壊すような振る舞いの大きな変更は、公開 API の変更として表れるようにする。
  1. スライスの必要な部分だけを公開する。

## スライス間の相互 import

出典: Public API > Public API for cross-imports

- 相互 import（cross-import）は、あるスライスが同じレイヤーの別のスライスから import することである。
  通常はレイヤーの規則で禁止されるが、正当な理由がある場合もある。
  例: 業務の実体は実世界で互いを参照し合うことが多く、その関係はコードにも表すのがよい。
- そのための特別な公開 API が `@x` 表記である。
  実体 B が実体 A から import する必要があるとき、A は B 専用の公開 API を宣言できる。
  - `entities/A/@x/B.ts` は、`entities/B/` の中のコード専用の特別な公開 API である。
  - `entities/A/index.ts` は、通常の公開 API である。
- `entities/B/` のコードは、`entities/A/@x/B` から import する。
  `A/@x/B` は「A と B の交差」と読む。
- 相互 import は最小限にし、この表記は Entities レイヤーでだけ使う。
  Entities では、相互 import をなくすことがしばしば現実的でない。

## index ファイルの問題

出典: Public API > Issues with index files

- バレルファイル（`index.js` など）は公開 API を定義する最も一般的な方法で、作りやすいが、バンドラーやフレームワークによっては問題を起こす。
- 循環 import: ファイルが輪になって import し合う状態で、バンドラーが扱いにくく、デバッグの難しい実行時エラーになることがある。
  同じスライスの中では相対パス、別のスライスからは絶対パス（エイリアスなど）で import して防ぐ。
- Shared でのバンドルの肥大: `shared/ui` や `shared/lib` は無関係なものの集まりで、ツリーシェイキングが効きにくい場合がある。
  その場合は、部品やライブラリごとに別の index ファイルを持たせる。
- 公開 API の迂回を防げない: index ファイルがあっても、直接の import は禁止されない。
  自動で検出するには、FSD の規則を持つリンター Steiger を勧める。
- 大きなプロジェクトでの性能低下: index ファイルが多いと、開発サーバーが遅くなることがある。
  対策は、`shared/ui` と `shared/lib` で index を分けること、スライスのあるレイヤーのセグメントに index を置かないこと、巨大なプロジェクトを FSD のルートごとのパッケージ（モノレポ）に分けることである。

## See also

- [Feature-Sliced Design: Overview](https://feature-sliced.design/docs/get-started/overview)
- [Feature-Sliced Design: Layers](https://feature-sliced.design/docs/reference/layers)
- [Feature-Sliced Design: Slices and Segments](https://feature-sliced.design/docs/reference/slices-segments)
- [Feature-Sliced Design: Public API](https://feature-sliced.design/docs/reference/public-api)
- 読んだ原文: [get-started/overview.mdx、reference/layers.mdx、reference/slices-segments.mdx、reference/public-api.mdx（feature-sliced/documentation の src/content/docs/docs/）](https://github.com/feature-sliced/documentation/tree/master/src/content/docs/docs)
