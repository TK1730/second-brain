---
type: reference
title: 'Playwright: Installation 要約'
description: 'Playwright 公式ドキュメント「Installation」の要約（Playwright Test の概要、インストール、インストールされるもの、テストの実行、HTML レポート、UI モード、更新、動作環境）。'
tags: [playwright, e2e, testing, installation]
status: stable
verified: { by: claude-code/claude-sonnet-5-5, at: 2026-10-21T00:00:00Z }
stale_after: 2027-10-21T00:00:00Z
---

# Playwright: Installation 要約

Playwright 公式ドキュメント（Node.js 版）の「Installation」の要約である。
外部資料の要約であり、最終的な根拠は原典を参照すること。
要点は「1 つのコマンドで設定とブラウザが入る」「`playwright test` で 3 種類のブラウザを並列に実行する」「結果は HTML レポートで確認する」の 3 つである。

## Playwright Test とは

出典: Introduction

- Playwright Test は、モダンな Web アプリ向けのエンドツーエンド（E2E）テストのフレームワークである。
- テストランナー、アサーション、テスト間の分離、並列実行、充実したツール群をまとめて備える。
- Chromium、WebKit、Firefox を、Windows、Linux、macOS で使える。
  ローカルでも CI でも、ヘッドレス（画面なし）でもヘッドあり（画面あり）でも動かせる。
  Chrome（Android）と Mobile Safari のモバイルエミュレーションも、ネイティブに備える。

## Playwright のインストール

出典: Installing Playwright > Using npm, yarn or pnpm

- `npm init playwright@latest` は、新しいプロジェクトを初期化するか、既存のプロジェクトに Playwright を追加する。
  yarn と pnpm には、`yarn create playwright` と `pnpm create playwright` がある。
- VS Code 拡張機能でも、テストの作成と実行ができる。
- 実行すると、次の項目を聞かれる。
  - TypeScript と JavaScript のどちらを使うか（既定は TypeScript）。
  - テストを置くフォルダ名（既定は `tests`。すでに `tests` があるときは `e2e`）。
  - GitHub Actions のワークフローを追加するか（CI 向けに推奨）。
  - ブラウザをインストールするか（既定はインストールする）。
- このコマンドは後から再実行でき、既存のテストを上書きしない。

## インストールされるもの

出典: What's Installed

- Playwright は、必要なブラウザのバイナリをダウンロードし、次の構成を作る。
  設定ファイル、`package.json`、ロックファイル、`tests/` とサンプルテストである。
- `playwright.config` は、対象のブラウザ、タイムアウト、リトライ、プロジェクト、レポーターなどの設定を 1 か所にまとめる。
- 既存のプロジェクトでは、依存関係が現在の `package.json` に追加される。
  `tests/` には、最小限のサンプルテストが入る。

## サンプルテストの実行

出典: Running the Example Test

- 既定では、テストはヘッドレスで、Chromium、Firefox、WebKit にまたがって並列に実行される。
  この既定は `playwright.config` で変えられる。
  出力と集計結果は、ターミナルに表示される。
- 実行のコマンドは `npx playwright test` である（pnpm は `pnpm exec playwright test`）。
- 実行時のヒントは次のとおりである。
  - ブラウザの画面を見るには `--headed` を付ける。
  - 1 つのプロジェクト（ブラウザ）だけで実行するには `--project=chromium` を付ける。
  - 1 つのファイルだけ実行するには、`npx playwright test tests/example.spec.ts` のようにパスを渡す。
  - テスト用の UI を開くには `--ui` を付ける。

## HTML テストレポート

出典: HTML Test Reports

- テストの実行後、HTML レポーターがダッシュボードを表示する。
  ブラウザ、成功、失敗、スキップ、不安定（flaky）などで絞り込める。
- テストをクリックすると、エラー、添付ファイル、ステップを調べられる。
  レポートは、失敗があったときだけ自動で開く。
- 手動で開くには `npx playwright show-report` を実行する（pnpm は `pnpm exec playwright show-report`）。

## UI モードでの実行

出典: Running the Example Test in UI Mode

- UI モード（`npx playwright test --ui`）では、ウォッチモード、ステップのライブ表示、タイムトラベルデバッグなどが使える。

## Playwright の更新

出典: Updating Playwright

- 更新して新しいブラウザのバイナリと依存関係をダウンロードするには、`npm install -D @playwright/test@latest` と `npx playwright install --with-deps` を実行する。
  yarn と pnpm にも、同じ働きのコマンドがある。
- バージョンは `npx playwright --version` で確認できる。

## システム要件

出典: System requirements

- Node.js は、22.x、24.x、26.x のそれぞれの最新版である。
- Windows 11 以降、Windows Server 2019 以降、または Windows Subsystem for Linux（WSL）。
- macOS 14（Sonoma）以降。
- Debian 12 / 13、Ubuntu 22.04 / 24.04 / 26.04（x86-64 または arm64）。

## See also

- [Installation (Playwright)](https://playwright.dev/docs/intro)
- [intro-js.md (microsoft/playwright)](https://github.com/microsoft/playwright/blob/main/docs/src/intro-js.md)
