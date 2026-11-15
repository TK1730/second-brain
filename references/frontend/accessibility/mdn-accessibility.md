---
type: reference
title: 'MDN: Accessibility 要約'
description: 'MDN Web Docs「Accessibility」トップページの要約（アクセシビリティとは、初心者向けチュートリアル、アクセシビリティのガイド一覧、リファレンス）。'
tags: [mdn, accessibility, a11y, wcag, aria]
status: stable
verified: { by: claude-code/claude-sonnet-5-5, at: 2026-10-21T00:00:00Z }
stale_after: 2027-10-21T00:00:00Z
---

# MDN: Accessibility 要約

MDN Web Docs の「Accessibility」トップページ（landing page）の要約である。
このページは、アクセシビリティの定義を述べたうえで、チュートリアルとガイドへの入口を並べている。
外部資料の要約であり、最終的な根拠は原典を参照すること。
要点は「アクセシビリティとは、能力に制限のある人も含め、できるだけ多くの人が Web サイトを使えるようにすること」「Web は本来、すべての人のために働くよう設計されている」の 2 つである。

## アクセシビリティとは

出典: （冒頭の説明）

- アクセシビリティ（Accessibility）は、しばしば A11y と略される。
  "a" の後に 11 文字が続き、最後が "y" であることに由来する。
- Web 開発におけるアクセシビリティとは、能力に何らかの制限がある人も含め、できるだけ多くの人が Web サイトを使えるようにすることである。
- 多くの人にとって、技術は物事を楽にする。
  障害のある人にとって、技術は物事を可能にする。
- アクセシビリティとは、個人の身体的・認知的な能力や、Web へのアクセス方法にかかわらず、コンテンツをできるだけアクセスしやすく作ることである。

W3C の文章が引用されている。

- Web は、ハードウェア、ソフトウェア、言語、場所、能力にかかわらず、すべての人のために働くよう根本から設計されている。
- Web がこの目標を満たすとき、聴覚、運動、視覚、認知の能力が多様な人々が Web を利用できる。

## 初心者向けのチュートリアル

出典: Beginner's tutorials

「Learn web development」の Accessibility モジュールに、アクセシビリティの基礎を扱う、最新のチュートリアルがある。
ページが挙げる記事は次の 7 つである。

- What is accessibility?
  - アクセシビリティとは何かを扱い、このモジュールの最初の記事である。
  - どのような人々を考慮すべきか、なぜか、人によって Web の操作に使う道具がどう違うか、アクセシビリティを開発の流れの一部にするにはどうするかを述べる。
- Accessibility tooling and assistive technology
  - アクセシビリティの問題の解決に使える道具と、障害のある人が Web を閲覧するときに使う支援技術を紹介する。
  - これらの道具は、以降の記事で使う。
- HTML: A good basis for accessibility
  - 正しい HTML 要素を、正しい目的でいつも使うだけで、多くの Web コンテンツをアクセシブルにできる。
  - HTML を使って最大限のアクセシビリティを確保する方法を詳しく扱う。
- CSS and JavaScript accessibility best practices
  - CSS と JavaScript は、適切に使えばアクセシブルな Web 体験を可能にするが、誤用するとアクセシビリティを大きく損なう。
  - 複雑なコンテンツでもできるだけアクセシブルにするための、ベストプラクティスを示す。
- WAI-ARIA basics
  - 意味を持たない HTML と、JavaScript で動的に更新されるコンテンツを使う複雑な UI 部品は、アクセシブルにするのが難しいことがある。
  - WAI-ARIA は、ブラウザーや支援技術が認識して利用者に状況を伝えられる意味を追加することで、そうした問題の解決を助ける技術である。
  - 基本的な使い方を示す。
- Accessible multimedia
  - 動画、音声、画像は、支援技術とその利用者が理解できるよう、適切なテキストによる代替を付ける必要がある。
  - その方法を示す。
- Mobile accessibility
  - モバイル端末での Web アクセスは普及しており、iOS や Android には本格的なアクセシビリティの道具がある。
  - モバイル特有の考慮事項を扱う。

## アクセシビリティのガイド

出典: Accessibility guides

「Accessibility guides」は、執筆の原則、WCAG への準拠、アクセシブルなウィジェットとナビゲーション、モバイルのアクセシビリティなどの主要な話題を扱う。
アクセシビリティがなぜ Web に不可欠か、プロジェクトでどう改善するかを理解する助けになる、とされる。
ページが挙げるガイドは次の 10 件である。

- Accessibility information for web authors
  - Web サイトのアクセシビリティの問題を調べて直すための、ガイドライン、規則、手順、道具を挙げた文書である。
- Personalization to help browse safely
  - 前庭障害のある人と、その支援者のために、OS に組み込まれた個人設定やアクセシビリティ設定を活用して Web コンテンツをアクセシブルにする方法を述べる。
- Accessible web applications and widgets
  - 多くの JavaScript ライブラリーは、デスクトップの見慣れた UI を模したクライアント側のウィジェットを提供する。
  - 見た目はデスクトップのものに似るが、マークアップに含まれる意味の情報が足りず、支援技術では使えないことが多い。
  - このようなウィジェットのアクセシビリティを改善する技法を述べる。
- Keyboard-navigable JavaScript widgets
  - `<div>` や `<span>` で作った装飾付きのウィジェットをアクセシブルにする適切な技法が、これまで不足していた。
  - キーボードのアクセシビリティは、開発者が知っておくべき最低限の要件の一部である。
  - JavaScript のウィジェットをキーボードで使えるようにする技法を述べる。
- Mobile accessibility checklist
  - モバイルアプリの開発者向けに、アクセシビリティの要件を簡潔なチェックリストにまとめる。
- Understanding the Web Content Accessibility Guidelines (WCAG)
  - WCAG の推奨事項に準拠するために必要な手順を、手短に説明する一連の記事である。
- Cognitive accessibility
  - 認知や学習に障害のある人のためのアクセシビリティの考慮事項を扱う。
  - 認知や学習の違いがある人のために、Web のアクセシビリティを高める方法を紹介する。
- Accessibility and spatial patterns
  - 光感受性てんかん、前庭障害、その他の知覚の問題がある人に、身体的な症状を引き起こしうる視覚パターンを述べる。
- Web Accessibility: Understanding Colors and Luminance
  - 色、輝度、彩度の理解は、見える人すべてにとってデザインと読みやすさのために重要である。
  - 視力が低い人、色覚に特性がある人、特定の神経・認知などの障害がある人にとっては、不可欠である。
- Web accessibility for seizures and physical reactions
  - ある種の視覚的な Web コンテンツは、特定の脳の障害がある人に発作を起こしうる。
  - 問題になりうるコンテンツの種類を理解し、避けるための道具と方法を見つける助けになる。

加えて、ARIA（Accessible Rich Internet Applications）の記事集がある。
HTML 文書をよりアクセシブルにするために ARIA を使う方法を学ぶためのものである。

## リファレンス

出典: References

- ARIA reference は、ARIA の属性とロールのリファレンス文書である。

## 主な推奨事項

出典: （ページ全体）

このページ自体は、具体的な実装手順ではなく、次のような方針を示している。

- 利用者の身体的・認知的な能力や、Web へのアクセス方法にかかわらず、コンテンツをできるだけアクセシブルにする。
- 正しい HTML 要素を、正しい目的で使う。
- CSS と JavaScript は、ベストプラクティスに従って使う。誤用はアクセシビリティを大きく損なう。
- 意味を持たない HTML や動的な UI 部品には、WAI-ARIA で意味を補う。
- 動画、音声、画像には、テキストによる代替を付ける。
- キーボードで操作できるようにする。これは最低限の要件の一部である。
- モバイルでの利用も考慮する。
- 発作や身体的な反応を引き起こしうるコンテンツを避ける。
- WCAG の推奨事項に準拠するための手順を理解する。

## See also

- [MDN: Accessibility](https://developer.mozilla.org/ja/docs/Web/Accessibility)
- [mdn/content: files/en-us/web/accessibility/index.md](https://github.com/mdn/content/blob/main/files/en-us/web/accessibility/index.md)
- [W3C: Accessibility](https://www.w3.org/standards/webdesign/accessibility)
