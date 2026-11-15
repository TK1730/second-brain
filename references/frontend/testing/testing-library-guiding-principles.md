---
type: reference
title: 'Testing Library: Guiding Principles 要約'
description: 'Testing Library 公式ドキュメント「Guiding Principles」の要約（基本の考え方、ユーティリティを入れる 3 つの指針、ライブラリの方針）。'
tags: [testing-library, testing, guiding-principles]
status: stable
verified: { by: claude-code/claude-sonnet-5-5, at: 2026-10-21T00:00:00Z }
stale_after: 2027-10-21T00:00:00Z
---

# Testing Library: Guiding Principles 要約

Testing Library の公式ドキュメント「Guiding Principles」の要約である。
外部資料の要約であり、最終的な根拠は原典を参照すること。
要点は「テストが実際の使われ方に似ているほど、テストは大きな自信を与える」ことであり、ユーティリティはこの考え方に沿って選ぶ。

## 基本の考え方

出典: （冒頭の引用）

- 「テストがソフトウェアの使われ方に似ているほど、テストはより大きな自信を与えてくれる」という考え方が掲げられている。
- Testing Library は、Web ページが実際に使われる方法に近いテストを書くことを促すメソッドとユーティリティだけを公開しようとしている。

## ユーティリティを入れる指針

出典: （本文の 3 項目の指針）

このプロジェクトのユーティリティは、次の 3 つの指針に基づいて含められる。

1. コンポーネントの描画に関わるものは、コンポーネントのインスタンスではなく DOM ノードを扱う。
   コンポーネントのインスタンスを扱うことを促してもいけない。
1. ユーザーが使う方法でアプリケーションのコンポーネントをテストするのに、おおむね役立つものであること。
   コンピューターと、多くの場合は模擬的なブラウザ環境を使うため、ここにはいくつかのトレードオフがある。
   それでも原則として、ユーティリティはコンポーネントを本来の使われ方で使うテストを促すべきである。
1. ユーティリティの実装と API は、シンプルで柔軟であること。

## ライブラリの方針

出典: （結びの一文）

- 結局のところ、このライブラリは軽量で、シンプルで、分かりやすいものにしたい、と述べられている。

## See also

- [Testing Library: Guiding Principles](https://testing-library.com/docs/guiding-principles/)
- [原典の Markdown（testing-library-docs リポジトリ）](https://github.com/testing-library/testing-library-docs/blob/main/docs/guiding-principles.mdx)
