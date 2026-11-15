---
type: reference
title: 'Vitest: Getting Started 要約'
description: 'Vitest 公式ドキュメント「Getting Started」の要約（概要、オンラインで試す、導入、最初のテスト、設定、IDE 連携、サンプル、コミュニティ）。'
tags: [vitest, testing, vite, getting-started]
status: stable
verified: { by: claude-code/claude-sonnet-5-5, at: 2026-10-21T00:00:00Z }
stale_after: 2027-10-21T00:00:00Z
---

# Vitest: Getting Started 要約

Vitest の公式ドキュメントの「Guide: Getting Started」の要約である。
外部資料の要約であり、最終的な根拠は原典を参照すること。
要点は「Vitest は Vite を土台にしたテストフレームワークである」「`vitest` を開発依存に入れ、`.test.` か `.spec.` を含む名前のファイルにテストを書き、`vitest` で実行する」「設定は既定で `vite.config.*` を読む」の 3 つである。

## 概要

出典: Overview

Vitest（「ヴィーテスト」と読む）は、Vite を土台にした次世代のテストフレームワークである。
作られた理由は、ドキュメントの「Why Vitest」の節で詳しく説明されている。

## オンラインで試す

出典: Trying Vitest Online

StackBlitz（https://vitest.new）で、インストールなしに Vitest を試せる。
ブラウザの中で Vitest を直接動かし、ローカルの環境とほぼ同じように使える。

## プロジェクトへの導入

出典: Adding Vitest to Your Project

- パッケージマネージャー（npm、yarn、pnpm、bun、deno）で、開発依存（`-D`）として `vitest` を入れる。
  yarn の例だけは `vitest` と `vite` の両方を指定している。
- 必要な環境は、Vite v6.4.0 以上と Node v22.12.0 以上である。
- `package.json` に `vitest` を入れる方法が推奨されている。
  `vitest` を直接実行したいときは `npx vitest` も使える。
- `npx` は、次の順にコマンドを探して実行する。
  1. ローカルのプロジェクトの実行ファイル。
  1. システムの `$PATH`。
  1. どちらにもなければ、一時的な場所に入れてから実行する。
- Vitest やサードパーティの連携は、生成物の保存に `.vitest` ディレクトリを使うことがある。
  `.gitignore` に追加することが推奨されている。

```sh
pnpm add -D vitest
```

## テストを書く

出典: Writing Tests

- 例として、2 つの数を足す関数 `sum` の出力を確かめる簡単なテストを書く。
  テストは `vitest` から `expect` と `test` を import し、`expect(sum(1, 2)).toBe(3)` のように検証する。
- 既定では、テストのファイル名に `.test.` か `.spec.` を含める必要がある。
- テストを実行するには、`package.json` の `scripts` に `"test": "vitest"` を追加する。
- `npm run test`、`yarn test`、`pnpm test` のいずれか（使うパッケージマネージャーによる）を実行すると、合格したテストの数と所要時間が表示される。
- Bun をパッケージマネージャーにしている場合は、`bun test` ではなく `bun run test` を使う。
  `bun test` は Bun 自身のテストランナーを動かしてしまうためである。

```js
import { expect, test } from 'vitest';
import { sum } from './sum.js';

test('adds 1 + 2 to equal 3', () => {
  expect(sum(1, 2)).toBe(3);
});
```

## 実行の方法

出典: Writing Tests

- テストの整理の仕方、出力の読み方、毎日使う基本のパターンは、次のページ「Writing Tests」で学ぶ。
- ファイルの変更を監視せず、一度だけ実行するには `vitest run` を使う。
- `--reporter` や `--coverage` などのフラグも渡せる。
- CLI のオプションの一覧は、`npx vitest --help` か CLI ガイドで確認できる。

## Vitest の設定

出典: Configuring Vitest

- Vitest は、既定で `vite.config.*` を読む。
  そのため、既存の Vite のプラグインや設定がそのまま使える。
- テスト専用の設定には、専用の `vitest.config.*` を作ることもできる。
- 詳しくは設定リファレンス（Config Reference）を参照する。

## IDE との連携

出典: IDE Integrations

- Visual Studio Code 向けに、公式の拡張機能が提供されている。
- VS Code Marketplace からインストールできる。
- ほかの IDE との連携は、IDE Integrations のページで説明されている。

## サンプル

出典: Examples

- Vitest のリポジトリと、ブラウザ向けのサンプルのリポジトリに、フレームワークごとのサンプルがある。
- 一覧にあるもの: `basic`、`fastify`、`in-source-test`、`lit`、`vue`、`marko`、`preact`、`qwik`、`react`、`solid`、`svelte`、`profiling`、`typecheck`、`projects`。
- `profiling` 以外は、StackBlitz でオンラインで試せる。

## コミュニティ

出典: Community

質問や助けが必要なときは、Discord と GitHub Discussions で相談できる。

## See also

- [Getting Started (Vitest)](https://vitest.dev/guide/)
- [docs/guide/index.md (vitest-dev/vitest)](https://github.com/vitest-dev/vitest/blob/main/docs/guide/index.md)
