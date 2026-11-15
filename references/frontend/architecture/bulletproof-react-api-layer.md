---
type: reference
title: 'Bulletproof React: API Layer 要約'
description: 'Bulletproof React の docs/api-layer.md の要約（API クライアントのインスタンスを 1 つにする、リクエスト宣言を定義して export する）。'
tags: [bulletproof-react, react, api-layer, api-client, data-fetching]
status: stable
verified: { by: claude-code/claude-sonnet-5-5, at: 2026-10-21T00:00:00Z }
stale_after: 2027-10-21T00:00:00Z
---

# Bulletproof React: API Layer 要約

Bulletproof React（Alan Alickovic 氏による、React アプリケーションのリファレンスアーキテクチャのリポジトリ）の `docs/api-layer.md` の要約である。
外部資料の要約であり、最終的な根拠は原典を参照すること。
要点は「事前に設定した API クライアントのインスタンスを 1 つだけ使い回す」「API リクエストはその場で書かず、型・fetcher 関数・フックをまとめた宣言として定義して export する」の 2 つである。

## API クライアントのインスタンスを 1 つにする

出典: Use a Single Instance of the API Client

- REST API でも GraphQL API でも、事前に設定した API クライアントのインスタンスを 1 つ作り、アプリ全体で再利用するとよい。
- インスタンスは、標準の fetch API か、次のようなライブラリで作れる。
  設定は、あらかじめ決めておく。
  - [axios](https://github.com/axios/axios)
  - [graphql-request](https://github.com/prisma-labs/graphql-request)
  - [apollo-client](https://www.apollographql.com/docs/react/)
- 例のコードは、リポジトリの [`apps/react-vite/src/lib/api-client.ts`](https://github.com/alan2207/bulletproof-react/blob/master/apps/react-vite/src/lib/api-client.ts) にある。

## リクエスト宣言を定義して export する

出典: Define and Export Request Declarations

- API リクエストは、その場で書かず、別に定義して export することを勧めている。
- 構造立てて宣言すると、関連するものが同じ場所にまとまり、コードベースが整理された状態に保たれる。
- 1 つのリクエスト宣言は、次の 3 つで構成する。
  1. リクエストとレスポンスのデータの型と、検証用のスキーマ。
  1. API クライアントのインスタンスを使ってエンドポイントを呼ぶ fetcher 関数。
  1. fetcher 関数を使うフック。
     データの取得とキャッシュの処理を管理するために、次のようなライブラリの上に作る。
     - [react-query](https://tanstack.com/query)
     - [swr](https://swr.vercel.app/)
     - [apollo-client](https://www.apollographql.com/docs/react/)
     - [urql](https://formidable.com/open-source/urql/)
- この方法には、次の利点がある。
  - アプリで使えるエンドポイントを追いやすくなる。
  - レスポンスに型を付け、それをアプリの下流で推論することで、型安全性が高まる。
- 例のコードは、次のとおりである。
  - 取得（Query）: [`apps/react-vite/src/features/discussions/api/get-discussions.ts`](https://github.com/alan2207/bulletproof-react/blob/master/apps/react-vite/src/features/discussions/api/get-discussions.ts)
  - 更新（Mutation）: [`apps/react-vite/src/features/discussions/api/create-discussion.ts`](https://github.com/alan2207/bulletproof-react/blob/master/apps/react-vite/src/features/discussions/api/create-discussion.ts)

## See also

- [API Layer (Bulletproof React)](https://github.com/alan2207/bulletproof-react/blob/master/docs/api-layer.md)
