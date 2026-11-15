---
type: reference
title: 'Next.jsの考え方（データフェッチ）要約'
description: 'akfm 著の Zenn 無料本「Next.jsの考え方」のうち第 1 部（データフェッチ）のみの要約（Server Components でのデータフェッチ、コロケーション、Request Memoization、並行データフェッチ、N+1 と DataLoader、細粒度の REST API 設計、ユーザー操作とデータフェッチ）。'
tags: [nextjs, react, rsc, data-fetching, server-components, zenn]
status: stable
verified: { by: claude-code/claude-sonnet-5-5, at: 2026-10-21T00:00:00Z }
stale_after: 2027-10-21T00:00:00Z
---

# Next.jsの考え方（データフェッチ）要約

akfm（akfm_sato）が Zenn で公開している無料の本「Next.jsの考え方」の要約である。
本は全 5 部の構成で、この要約は第 1 部「データフェッチ」だけを扱う。
扱う章は、第 1 部の導入、データフェッチ on Server Components、データフェッチ コロケーション、Request Memoization、並行データフェッチ、N+1 と DataLoader、細粒度の REST API 設計、ユーザー操作とデータフェッチの 8 つである。
外部資料の要約であり、最終的な根拠は原典を参照すること。
要点は「データフェッチは Server Components で行い、使うコンポーネントにコロケーションし、重複・直列化・N+1 を Request Memoization、並行化、DataLoader で抑える」である。

## 第 1 部 データフェッチ（導入）

出典: 第1部 データフェッチ

Next.js がサポートする RSC では、従来の React フレームワークから多くのパラダイムシフトが必要になる。
データフェッチでは、Server Components によってセキュアでシンプルな実装が可能になった一方、従来とは全く異なる設計思想が求められる。
Next.js のデータアクセスには、バックエンド API を分離して開発する方法と、Next.js にデータベースアクセスを統合する方法の 2 つがある。
本書の「考え方」はこの選択で大きく変わる部分が少ないと思われるため、バックエンド API を分離するアプローチを前提に解説している。

## データフェッチ on Server Components

出典: データフェッチ on Server Components

要約は「データフェッチは Client Components ではなく、Server Components で行う」である。

- クライアントサイドのデータフェッチには、次のデメリットがある。
  - 通信は物理的距離や不安定なネットワークの影響で低速になりやすく、通信回数を減らすと設計とトレードオフになる。
    - 通信回数を優先すると、責務が大きい God API になりやすく、変更容易性や API 自体の性能に問題が出やすい。
    - 細粒度な API（Chatty API）はコロケーションなどの利点があるが、通信回数が増え、ウォーターフォールが起きやすい。
  - キャッシュ機能を持つ 3rd party ライブラリの学習、責務設計、公開する API のセキュリティ対策などの実装コストがかかる。
  - ライブラリ、取得処理、バリデーション、使われないかもしれないエラー時の UI などがバンドルされ、クライアントへ送られる。
- Next.js は RSC をサポートしており、データフェッチは Server Components で行うことがベストプラクティスとされている。
- Server Components で行う利点は次のとおりである。
  - Next.js サーバーと API サーバー間の通信は、多くの場合高速で安定している。
  - 非同期関数をサポートするため、3rd party ライブラリなしで `await fetch()` によりシンプルに実装できる。
  - サーバーでのみ実行されるため、API をパブリックなネットワークに公開することは必須ではなく、セキュリティリスクと対策コストを軽減できる。
  - 実行結果は HTML や RSC Payload として送られるため、取得に関するコードはバンドルに含まれない。
- トレードオフは次のとおりである。
  - ユーザー操作に基づくデータフェッチは、Server Components では難しい場合がある。
  - RSC と GraphQL の組み合わせは、メリットよりデメリットの方が多くなる可能性がある。
    - GraphQL が解消するパフォーマンスと設計のトレードオフは RSC も解消するため、利点として享受できない。
    - 協調させる知見やライブラリが不足しており、実装コストが高く、バンドルサイズも増える。

## データフェッチ コロケーション

出典: データフェッチ コロケーション

要約は「データフェッチはデータを参照するコンポーネントにコロケーションし、コンポーネントの独立性を高める」である。
コロケーションとは、コードをできるだけ関連性のある場所に配置することを指す。

- Pages Router では、`getServerSideProps` や `getStaticProps` をページの外側で宣言し、結果を props としてページに渡す設計だった。
  - 親から子・孫へ props を渡し続けるバケツリレー（Props Drilling）が必要になり、冗長で依存関係が広がりやすい。
  - 開発者に常にページという単位を意識させ、コンポーネント指向な開発と親和性が低く、認知負荷が高い。
- App Router では Server Components が使えるため、末端のコンポーネントへデータフェッチをコロケーションすることを推奨している。
  - 小規模な実装ならページコンポーネントでの取得でも問題ない。
  - ページが肥大化すると中間層でバケツリレーが起きやすいので、できるだけ末端で取得することを推奨している。
  - 同じ取得が何度も実行される懸念は、Request Memoization で同一のデータフェッチがメモ化されることで解消される。
- コロケーションにより、バケツリレーがなくなる。
  子コンポーネントは必要な情報を自身で取得するため、ページ全体でどんな取得をしているかを気にする必要がなくなる。
- トレードオフは、コロケーションの要が Request Memoization であるため、その理解と最適な設計が重要になる点である。

## Request Memoization

出典: Request Memoization

要約は「データフェッチ層を分離して、Request Memoization を生かせる設計を心がける」である。

- Next.js は、レンダリング中の同一リクエストを Request Memoization で排除する。
  ただし重複と判定されるには、同一 URL・同一オプションが必要で、オプションが 1 つでも違えば別リクエストになる。
- オプションの指定ミスで Request Memoization が効かなくなることを避けるため、複数のコンポーネントで使いうる取得処理は、データフェッチ層として分離する。
- データフェッチ層をファイル分離する場合も、ファイルコロケーションすることが推奨される。
  筆者は規模に応じて、次のいずれかの形で分離するとしている。
  - 取得関数が少なく、ファイルも少ない場合は `app/products/fetcher.ts`。
  - ファイルが多く、取得関数は少ない場合は `app/products/_lib/fetcher.ts`。
  - 取得関数が多い場合は `app/products/_lib/fetcher/product.ts`。
  - 命名やディレクトリは開発規模や流儀によって異なるため、チームでルールを決めておく。
- データフェッチ層を誤ってクライアントで使うことを防ぐため、`server-only` でモジュールを保護することを推奨している。
  Client Bundle 内で import するとエラーになる。
- トレードオフは、特になしとされている。

## 並行データフェッチ

出典: 並行データフェッチ

要約は「データフェッチが可能な限り並行になるよう、コンポーネント分割、並行 `fetch()`、preload パターンを駆使して設計する」である。

- データ間に依存関係があれば直列（ウォーターフォール）にせざるを得ないが、依存関係がなければ並行化で優れた性能を得られる。
- コードの凝集度を考えると、まずは可能な限り、データフェッチ単位のコンポーネント分割を行うのがベストである。
  ただし必ず分割できるとは限らないため、他のパターンも理解しておく。
- データフェッチ単位のコンポーネント分割
  - データ間に依存関係がなく、参照単位も異なる場合に使う。
  - 非同期コンポーネントは、兄弟もしくは兄弟の子孫として配置されていれば並行にレンダリングされる。
  - 非同期コンポーネントがネストしている場合は、実行が直列になる。
- 並行 `fetch()`
  - 取得順に依存関係はないが、参照の単位が不可分な場合に使う。
  - `Promise.all()` や `Promise.allSettled()` で複数の取得を並行に実行する。
- preload パターン
  - コンポーネント構造上、親子関係にせざるを得ずウォーターフォールが起きる場合に、Request Memoization を活用して並行化する。
  - 取得関数を `await` せずに呼ぶだけの preload 専用関数を用意し、親（ページレベル）で呼ぶ。
  - preload した後で子孫から参照されなくなった場合、preload が残っていると不要な取得が発生する。
    無駄な preload が残らないよう注意する。
- トレードオフは、取得単位を小さく分割すると N+1 データフェッチが起きうる点である。

## N+1とDataLoader

出典: N+1とDataLoader

要約は「コンポーネント単位の独立性を高めると N+1 データフェッチが発生しやすくなるので、DataLoader のバッチ処理で解消する」である。

- コロケーションや並行データフェッチで取得とコンポーネントを細かく分割すると、ページ全体の取得の管理が難しくなり、2 つの問題が起きる。
  - 重複した取得は、データフェッチ層を共通化していれば Request Memoization によってほとんど問題ない。
  - N+1 な取得は、細粒度に分解するほど起きやすい。
    例として、投稿一覧を 1 回取得した後、子コンポーネントが投稿ごとに著者情報を取得すると、1 + N 回の取得になる。
- N+1 を避けるには、API 側で ID を複数指定して一括取得できるように設計し、Next.js 側で DataLoader を使うパターンがよく知られている。
- DataLoader は GraphQL サーバーなどでよく使われ、データアクセスのバッチ処理とキャッシュを提供するライブラリである。
  使い方は次の流れである。
  1. バッチ処理する関数を定義する。
  1. DataLoader のインスタンスを生成する。
  1. 短期間に `load(id)` を複数回呼ぶと、ID の配列がバッチ処理に渡される。
  1. バッチ処理が完了すると、`load(id)` の Promise が解決される。
- Server Components の兄弟もしくは兄弟の子孫は並行レンダリングされるため、それぞれが `await loader.load(id)` と書いてもバッチされる。
- DataLoader にはキャッシュ機能があるため、ユーザーのリクエストをまたいでインスタンスを共有すると、予期せぬデータ共有につながる。
  そのため、リクエスト単位でインスタンスを生成する必要があり、React の `cache()` で生成関数を包んでこれを実現している。
- この方法なら、`getUser()` のインターフェースを変えずに N+1 を解消できる。
- トレードオフは次のとおりである。
  - ここで紹介した設計は Lazy Loading パターンの一種である。
  - バックエンド API の実装や性能の観点で適さない場合は、Eager Loading（最初の 1 回で関連情報を全て取得する）を検討する。
  - Eager Loading に偏りすぎると、密結合で責務が大きい God API になる。

## 細粒度のREST API設計

出典: 細粒度のREST API設計

要約は「バックエンド API の設計はフロントエンドの設計にも大きく影響する。Next.js に対する API は細粒度な単位に分割されていることが望ましく、可能な限りこれを意識して設計する」である。

- REST API のリソース単位は、識別子を持つデータやオブジェクト単位でできるだけ細かい細粒度に分割するのが基本である。
  一方、通信回数を避けるために粗粒度で設計されることも多い。
- 細粒度で通信回数が多い状態を Chatty API、粗粒度で汎用性に乏しい状態を God API と呼ぶ。
  どちらも一概にアンチパターンではなく、観点次第で最適解が異なるトレードオフとして捉えるべきである。
  - 細粒度は設計の観点では良く、低速な通信ではパフォーマンスが悪く、高速な通信では良い。
  - 粗粒度は設計の観点では悪く、通信の速さにかかわらずパフォーマンスは良い。
- App Router 登場以前は、API 設計がページと密結合になり、汎用性や保守性に乏しくなるケースが多かった。
  - クライアントでの取得は通信が低速になりやすく、ページごとに 1 回で完結する粗粒度の API が採られがちだった。
  - `getServerSideProps()` を使う BFF と API 間は高速な通信だが、ページ単位で定義するため、API にページ単位の要求が反映されて粗粒度になりがちだった。
- App Router では、Server Components によりデータフェッチのコロケーションと分割が容易になった。
  そのため細粒度で設計された REST API と非常に相性が良く、API 側の実装もシンプルになることが多い。
- 細粒度な API 設計は、従来から GraphQL BFF に対する API でも好まれており、RSC と GraphQL には共通の思想が見える。
  RSC の最初の RFC は Relay の初期開発者の 1 人である Joe Savona 氏が提案しており、RSC には GraphQL の精神的後継という側面がある。
- トレードオフは次のとおりである。
  - サーバー間通信は多くの場合高速で安定しているため、通信回数の多さはデメリットになりづらいが、アプリケーション特性による。
    並行データフェッチ、DataLoader、Data Cache を活用して通信頻度と性能を最適化する。
  - API には複数の利用者がいる場合もあり、Next.js 側の都合だけでは決められない。
    最終判断がバックエンド開発チームにあるとしても、メリットと Next.js 側の背景を伝え、理解を得る努力をする。

## ユーザー操作とデータフェッチ

出典: ユーザー操作とデータフェッチ

要約は「ユーザー操作に基づくデータフェッチと再レンダリングには、Server Functions と `useActionState()` を使う」である。

- Server Components はユーザー操作に基づく取得や再レンダリングに向かない。
  `router.refresh()` などでページ全体を再レンダリングできるが、部分的に再レンダリングしたい場合には不適切である。
- `useActionState()` は、関数と初期値を渡すことで、Server Functions を通して更新できる State を管理する。
  例として、検索の Server Function を第 1 引数に渡すと、form が submit されるたびにそれが実行され、結果が State になる。
  Server Function はファイル先頭に `"use server"` を書いて定義し、form を持つ側は Client Component にする。
- トレードオフは次のとおりである。
  - Server Functions と `useActionState()` だけでは、リロード復元や URL 共有が難しい。
  - form 以外の要素がほとんどない単純なページなら、公式チュートリアルのように `router.replace()` で URL を更新し、ページ全体を再レンダリングする手段がある。
    検索が主のページでは、状態を URL に保存することを検討すべきである。
    URL への保存には `location-state` や `nuqs` などのライブラリが便利で、`useActionState()` と併用もできる。
  - サイドナビゲーションや cmd+k の検索モーダルのように、リロード復元や URL 共有が不要なケースでは、Server Functions と `useActionState()` が非常に役立つ。
  - ここで扱ったのはデータ操作を伴わないユーザー操作である。
    データを操作して結果を再取得する場合は、Server Actions（データ操作を伴う Server Functions）と `revalidatePath()` / `revalidateTag()` を組み合わせる。
    詳細は後続の「データ操作とServer Actions」の章で解説されている（今回は未読）。

## See also

- [Next.jsの考え方（本のトップ）](https://zenn.dev/akfm/books/nextjs-basic-principle)
- [第1部 データフェッチ](https://zenn.dev/akfm/books/nextjs-basic-principle/viewer/part_1)
- [データフェッチ on Server Components](https://zenn.dev/akfm/books/nextjs-basic-principle/viewer/part_1_server_components)
- [データフェッチ コロケーション](https://zenn.dev/akfm/books/nextjs-basic-principle/viewer/part_1_colocation)
- [Request Memoization](https://zenn.dev/akfm/books/nextjs-basic-principle/viewer/part_1_request_memoization)
- [並行データフェッチ](https://zenn.dev/akfm/books/nextjs-basic-principle/viewer/part_1_concurrent_fetch)
- [N+1とDataLoader](https://zenn.dev/akfm/books/nextjs-basic-principle/viewer/part_1_data_loader)
- [細粒度のREST API設計](https://zenn.dev/akfm/books/nextjs-basic-principle/viewer/part_1_fine_grained_api_design)
- [ユーザー操作とデータフェッチ](https://zenn.dev/akfm/books/nextjs-basic-principle/viewer/part_1_interactive_fetch)
