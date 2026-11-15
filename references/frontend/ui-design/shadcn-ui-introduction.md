---
type: reference
title: 'shadcn/ui: Introduction と Components 一覧 要約'
description: 'shadcn/ui 公式ドキュメントの「Introduction」と「Components」（概要）の要約（位置づけ、5 つの原則、Open Code、Composition、Distribution、Beautiful Defaults、AI-Ready、コンポーネント名の一覧）。'
tags: [shadcn-ui, react, components, open-code, ui]
status: stable
verified: { by: claude-code/claude-sonnet-5-5, at: 2026-10-21T00:00:00Z }
stale_after: 2027-10-21T00:00:00Z
---

# shadcn/ui: Introduction と Components 一覧 要約

shadcn/ui 公式ドキュメントの「Introduction」ページと、コンポーネントの一覧ページ「Components」の要約である。
外部資料の要約であり、最終的な根拠は原典を参照すること。
要点は「shadcn/ui はコンポーネントライブラリではなく、コンポーネントライブラリを作るための方法である」「コンポーネントのコードを利用者に渡し、利用者が直接編集する」の 2 つである。

## 位置づけ

出典: Introduction

shadcn/ui は、美しく設計されたアクセシブルなコンポーネントと、コードの配布基盤である。
好みのフレームワークや AI モデルと組み合わせて使え、オープンソースで、コードも公開されている（Open Source. Open Code.）。

原典は冒頭で「これはコンポーネントライブラリではない。コンポーネントライブラリを作るための方法である」と述べている。

従来のライブラリは、NPM からパッケージを入れ、コンポーネントを import して使う。
この方式は、デザインシステムに合わせてコンポーネントを変えたいときや、ライブラリに無いコンポーネントが要るときに行き詰まる。
原典は、次のようなことになりがちだと述べている。

- ライブラリのコンポーネントを包む（ラップする）。
- スタイルを上書きするための回避策を書く。
- API が合わない複数のライブラリのコンポーネントを混ぜて使う。

shadcn/ui はこの問題の解決を目指しており、次の 5 つの原則で作られている。

| 原則               | 内容                                                                   |
| :----------------- | :--------------------------------------------------------------------- |
| Open Code          | コンポーネントのコードの最上位の層を、修正できるよう公開する。         |
| Composition        | すべてのコンポーネントが共通の組み合わせやすい形で、挙動が予測できる。 |
| Distribution       | フラットファイルのスキーマとコマンドラインツールで、配布を容易にする。 |
| Beautiful Defaults | 慎重に選んだ既定のスタイルで、そのままでも見栄えが良い。               |
| AI-Ready           | LLM が読み、理解し、改善できるよう、コードを公開している。             |

## Open Code

出典: Introduction > Open Code

shadcn/ui は、コンポーネントの実際のコードを利用者に渡す。
利用者は、必要に応じて自由にカスタマイズし、拡張できる。
これには次の利点がある。

- Full Transparency: 各コンポーネントがどう作られているかを、そのまま見られる。
- Easy Customization: デザインや機能の要件に合わせて、コンポーネントのどの部分でも変更できる。
- AI Integration: コードが見えるので、LLM が読み、理解し、改善することが容易になる。

通常のライブラリでボタンの挙動を変えるには、スタイルを上書きするか、コンポーネントを包む必要がある。
shadcn/ui では、ボタンのコードを直接編集すればよい。

### 上流の更新の取り込み

出典: Introduction > Open Code（FAQ「How do I pull upstream updates in an Open Code approach?」）

shadcn/ui は、ヘッドレスなコンポーネント構造に従っている。
そのため、アプリの中核部分は、依存パッケージ（例: `@base-ui/react`、`input-otp`）を更新することで修正を受け取れる。
デザインシステムに最も近い最上位の層は、ライブラリの実装と結び付いておらず、修正できる状態に保たれている。

## Composition

出典: Introduction > Composition

shadcn/ui のすべてのコンポーネントは、共通の組み合わせやすいインターフェースを共有している。
存在しないコンポーネントは、取り込んで組み合わせやすい形にし、ほかのデザインシステムに合うようスタイルを調整する。

インターフェースが共通なので、利用者のチームにも LLM にも予測しやすい。
新しいコンポーネントごとに別の API を覚える必要がなく、サードパーティのものでも同様である。

## Distribution

出典: Introduction > Distribution

shadcn/ui は、コードの配布の仕組みでもある。
コンポーネントのスキーマと、それを配布する CLI を定めている。

- Schema: コンポーネントとその依存関係、性質を定義するフラットファイルの構造。
- CLI: フレームワークをまたいで、コンポーネントを配布し、プロジェクトへ入れるコマンドラインツール。

このスキーマで、自分のコンポーネントをほかのプロジェクトへ配布できる。
既存のスキーマをもとに、AI に新しいコンポーネントを生成させることもできる。

## Beautiful Defaults

出典: Introduction > Beautiful Defaults

shadcn/ui には、慎重に選んだ既定のスタイルのコンポーネントが数多くある。
単独でも見栄えが良く、組み合わせても一貫した体系として働くよう設計されている。

- Good Out-of-the-Box: 追加の作業なしで、すっきりした最小限の見た目になる。
- Unified Design: 各コンポーネントがほかと合うように作られており、UI の一貫性が保たれる。
- Easily Customizable: 変えたい部分は、既定値を簡単に上書き・拡張できる。

## AI-Ready

出典: Introduction > AI-Ready

shadcn/ui の設計は、AI ツールがコードを扱いやすいようになっている。
コードが公開されていて API が一貫しているので、AI モデルはコンポーネントを読み、理解し、新しく生成できる。

AI モデルは、コンポーネントの動き方を学び、改善を提案したり、既存のデザインに合う新しいコンポーネントを作ったりできる。

## Components 一覧

出典: Components

公開ページの一覧は自動で作られるため、ここに並べた名前はリポジトリの部品のファイル名から作った。
公開ページの一覧とは、少し違うことがある。

Components ページは、ライブラリにあるすべてのコンポーネントを載せた一覧である。
原典は、コンポーネントを追加する作業を続けていると述べている。
ページは「New Components」と「All Components」の 2 つの一覧からなり、一覧の中身はドキュメントのファイルから生成される。
コミュニティが保守するコンポーネントは、registry directory で探せる。

原典のリポジトリ（`apps/v4/content/docs/components/radix`）にある、コンポーネントのページの名前は次のとおりである（各ページの内容は、このメモの対象外）。

- Accordion、Alert、Alert Dialog、Aspect Ratio、Attachment、Avatar、Badge、Breadcrumb、Bubble
- Button、Button Group、Calendar、Card、Carousel、Chart、Checkbox、Code Block、Collapsible
- Combobox、Command、Context Menu、Data Table、Date Picker、Dialog、Direction、Drawer、Dropdown Menu
- Empty、Field、Hover Card、Input、Input Group、Input OTP、Item、Kbd、Label
- Marker、Menubar、Message、Message Scroller、Native Select、Navigation Menu、Pagination、Popover、Progress
- Questionnaire、Radio Group、Resizable、Scroll Area、Select、Separator、Sheet、Sidebar、Skeleton
- Slider、Sonner、Spinner、Switch、Table、Tabs、Textarea、Toast、Toggle
- Toggle Group、Tooltip、Trace、Typography

## See also

- [Introduction - shadcn/ui](https://ui.shadcn.com/docs)
- [Components - shadcn/ui](https://ui.shadcn.com/docs/components)
- [Introduction の原典（index.mdx）](<https://github.com/shadcn-ui/ui/blob/main/apps/v4/content/docs/(root)/index.mdx>)
- [Components の原典（index.mdx）](https://github.com/shadcn-ui/ui/blob/main/apps/v4/content/docs/components/index.mdx)
