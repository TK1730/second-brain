---
type: reference
title: 'エージェントを用いた E2E テストを良くする 5 つのヒント'
description: e2e ブログの記事「5 Tips for Writing Good Agentic Tests with e2e」の要約で、AI エージェントによる E2E テストを壊れにくくデバッグしやすく保つ 5 つの設計原則を説明する。
tags: [ai, agent, testing, e2e, quality-assurance]
status: stable
verified: { by: antigravity/gemini-4-argon, at: 2026-11-15T00:00:00Z }
stale_after: 2027-11-15T00:00:00Z
---

# エージェントを用いた E2E テストを良くする 5 つのヒント

e2e ブログの記事「5 Tips for Writing Good Agentic Tests with e2e」(2026-11-13 公開) の要約である。
自然言語の指示によってブラウザ操作 (`agent.act`)、状態待機 (`agent.waitFor`)、結果検証 (`agent.assert`) を行うエージェント型 E2E テストにおいて、テストの壊れにくさ (耐障害性)・保守性・デバッグ容易性を高めるための 5 つの実践原則をまとめている。

## 概要

従来の E2E テスト (Playwright や Cypress など) は、CSS セレクタや `data-testid` を細かく指定して DOM 要素を直接操作するため、UI のマークアップ変更で容易に壊れるという課題があった。
AI エージェントを用いた E2E テストでは自然言語で操作や検証を記述できるが、従来のセレクタ指向の考え方のままプロンプトを書くと、かえって不安定で原因特定の難しいテストになってしまう。
記事は、エージェントの強みを活かしつつ信頼性の高いテストスイートを維持するための 5 つの原則を提示している。

## 1. 実装ではなくユーザーの意図をテストする (Don't test the implementation)

- `data-testid` や内部の DOM 構造、特定のボタン配置・CSS クラスに依存した細かい操作手順を指示してはならない。
- 代わりに、`agent.act("Generate last month's activity report")` (先月のアクティビティレポートを生成する) のように、「ユーザーが画面上で達成したいゴール (意図)」を記述する。
- ユーザーの意図レベルでテストを記述しておけば、フロントエンドの UI コンポーネントライブラリ (たとえば Bootstrap から shadcn/ui への移行など) や DOM 構造が変更されても、ユーザーから見た機能が変わらない限りテストは壊れずに動き続ける。

## 2. 固定時間ではなく結果の状態を待ってフレーキーさを減らす (Reduce flaky tests by waiting for outcomes)

- 非同期処理や重い集計処理を待つ際に、固定秒数のスリープ (`sleep(5000)`) を入れたり、ローディングスピナーの消滅といった実装詳細を監視したりするのはフレーキーテスト (時折失敗する不安定なテスト) の原因になる。
- 代わりに、`agent.waitFor("Last month's activity report is ready to view", { timeout: 15_000 })` のように、次のステップへ進むために必要な「意味的な完了状態 (Outcome)」を自然言語で指定する。
- `timeout` はあくまで最大待機時間の上限として機能し、画面上で指定した完了条件が満たされれば即座に次のステップへと進むため、テスト実行速度と安定性を両立できる。

## 3. アサーションを具体的にする (Make your assertions specific)

- 操作の実行 (`agent.act`) と結果の検証 (`agent.assert`) の責務を明確に分離する。
- 「レポートが正しく表示されていること」といった曖昧なアサーションではなく、期待するレコードの件数、特定の項目名、集計値など、合格条件を具体的に明示した `agent.assert(...)` を記述する。
- フレームワーク内部では、`assert` は操作を行ったエージェントとは別の「独立したジャッジ (審査員)」として動作し、操作時の思い込みを引きずらずに現在の画面上の証拠 (Evidence) のみに基づいて合否を客観的に評価する。

## 4. テストの焦点を絞り独立させる (Keep tests focused and independent)

- あるテストケースが「前のテストケースで作成されたデータやログイン状態」に依存するような順序依存の設計を避ける。
- テストの事前準備 (Setup) や事後処理 (Teardown) には、UI 操作だけでなくバックエンド API の直接呼び出し、クリーンアップフック、`test.extend` によるカスタムフィクスチャを活用し、毎回のテストが完全にクリーンで予測可能な初期状態から始まるようにする。
- 1 つのテストで確認する焦点を絞ることで、並列実行が可能になり、失敗時の影響範囲も局所化できる。

## 5. 失敗をデバッグしやすくする (Make failures easy to debug)

- 1 回の `agent.act` に長大で複雑な複合タスクを詰め込みすぎず、テスト内でエージェントに与えるゴールを適切な粒度に小さく保つ。
- ゴールが小さく具体的であれば、テストが失敗した際に「エージェントが何を試み、何を期待し、実際に画面上で何が起きたか」を即座に特定できる。
- 実行トレース、アプリケーションログ、各ステップのスクリーンショット、DOM スナップショットを組み合わせて確認することで、テストの誤りなのかアプリケーションのバグなのかを素早く切り分けられる。

## See also

- [5 Tips for Writing Good Agentic Tests with e2e (e2e Blog)](https://e2e.com/blog/5-tips-for-writing-good-agentic-tests)
- [エージェントの各ステップを見張らずに済ませるループとグラフ](/references/ai/hanakoxbt-loops-and-graphs.md)
- [AI エージェントに好かれるコードベースの作り方](/references/ai/aihero-codebases-ai-agents-love.md)
