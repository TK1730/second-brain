---
type: reference
title: 'Bulletproof React: Project Structure 要約'
description: 'Bulletproof React の「Project Structure」の要約（src 直下の構成、機能ごとのフォルダ、バレルファイル、機能間 import の禁止、一方向のコード構成、ESLint による強制）。'
tags: [react, project-structure, features, eslint, architecture]
status: stable
verified: { by: claude-code/claude-sonnet-5-5, at: 2026-10-21T00:00:00Z }
stale_after: 2027-10-21T00:00:00Z
---

# Bulletproof React: Project Structure 要約

React アプリケーションの設計例集 Bulletproof React の、プロジェクト構成を説明する文書「Project Structure」の要約である。
外部資料の要約であり、最終的な根拠は原典を参照すること。
要点は「コードの大半を機能ごとのフォルダ（features）に置く」「機能どうしで import しない」「コードは shared -> features -> app の一方向に流す」の 3 つである。

## src 直下の構成

出典: Project Structure（冒頭）

コードの大半は `src` フォルダに置く。
`src` 直下は次のフォルダで構成される。

| フォルダ     | 役割                                                               |
| :----------- | :----------------------------------------------------------------- |
| `app`        | アプリケーション層。使うメタフレームワークによって異なることがある |
| `assets`     | 画像やフォントなどの静的ファイル                                   |
| `components` | アプリケーション全体で共有するコンポーネント                       |
| `config`     | グローバルな設定、export した環境変数など                          |
| `features`   | 機能ごとのモジュール                                               |
| `hooks`      | アプリケーション全体で共有するフック                               |
| `lib`        | アプリケーション向けに設定済みの、再利用できるライブラリ           |
| `stores`     | グローバルな状態のストア                                           |
| `testing`    | テスト用のユーティリティとモック                                   |
| `types`      | アプリケーション全体で共有する型                                   |
| `utils`      | 共有するユーティリティ関数                                         |

`app` フォルダには、次のものが入る。

- `routes`: アプリケーションのルート（pages の場合もある）。
- `app.tsx`: アプリケーションの主要なコンポーネント。
- `provider.tsx`: 複数のグローバルなプロバイダーでアプリケーション全体を包むもの。メタフレームワークによって異なることがある。
- `router.tsx`: ルーターの設定。

## 機能ごとのフォルダ

出典: Project Structure（features の説明）

保守しやすく拡張しやすくするため、コードの大半を `features` フォルダの中に整理することを勧めている。
各機能のフォルダには、その機能専用のコードを置き、きれいに分けておく。
共有コンポーネントと機能のコードが混ざるのを防げる。
フラットなフォルダに多数のファイルを置くより、管理と保守が楽になる。
この方法で、協力しやすさ、読みやすさ、拡張しやすさが高まるとしている。

1 つの機能は、たとえば次の構成を持てる（`src/features/awesome-feature`）。

- `api`: その機能に関する API リクエストの宣言と、API のフック。
- `assets`: その機能専用の静的ファイル。
- `components`: その機能に閉じたコンポーネント。
- `hooks`: その機能に閉じたフック。
- `stores`: その機能の状態ストア。
- `types`: その機能の中で使う TypeScript の型。
- `utils`: その機能専用のユーティリティ関数。

すべての機能にこれらのフォルダが全部必要なわけではない。
その機能に必要なものだけを置く。

機能間で共有する API 呼び出しが多い場合は、すべての API 呼び出しを、features の外にある専用の `api` フォルダに定義するほうが実用的なこともある。

## バレルファイル

出典: Project Structure（barrel files の説明）

以前は、バレルファイル（機能内のファイルをまとめて export するファイル）で機能のファイルを export することが勧められていた。
しかし、Vite がツリーシェイキング（使われないコードの除去）をしにくくなり、性能の問題につながりうる。
そのため、ファイルは直接 import することを勧めている。

## 機能間の import の禁止

出典: Project Structure（cross-feature imports の説明）

機能をまたいで import するのは、良くないことがある。
代わりに、アプリケーション層で複数の機能を組み合わせる。
こうすると、各機能が独立し、コードベースが込み入りにくくなる。

機能間の import を禁止するには、ESLint の `import/no-restricted-paths` を使える。
機能ごとに、`target` をその機能、`from` を `./src/features`、`except` をその機能自身とするゾーンを定義する。
原典の例は、auth、comments、discussions、teams、users の各機能に対して同じ形のゾーンを並べている。

```js
{
  target: './src/features/auth',
  from: './src/features',
  except: ['./auth'],
},
```

## 一方向のコード構成

出典: Project Structure（unidirectional codebase の説明）

コードが共有部分からアプリケーションへ一方向に流れる構成（shared -> features -> app）を強制することも勧めている。
コードベースが予測しやすく、理解しやすくなるためである。

- 共有部分は、コードベースのどこからでも使える。
- features は、共有部分からだけ import できる。
- app は、features と共有部分から import できる。

これも ESLint の `import/no-restricted-paths` で強制できる。
原典の設定は 2 つのゾーンからなる。

- `./src/features` は `./src/app` から import できない。
- 共有部分（`./src/components`、`./src/hooks`、`./src/lib`、`./src/types`、`./src/utils`）は、`./src/features` と `./src/app` から import できない。

## まとめ

出典: Project Structure（結び）

この方法で、コードベースは整理され、拡張しやすく、保守しやすくなり、チームが効率よく作業できるとしている。
同様の構成は、Next.js、Remix、React Native で作るアプリにも適用しやすくなると述べている。

## See also

- [Bulletproof React: Project Structure（原典）](https://github.com/alan2207/bulletproof-react/blob/master/docs/project-structure.md)
- [原典の raw ファイル](https://raw.githubusercontent.com/alan2207/bulletproof-react/master/docs/project-structure.md)
