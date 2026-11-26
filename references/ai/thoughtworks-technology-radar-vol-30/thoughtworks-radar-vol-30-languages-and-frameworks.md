---
type: reference
title: 'Thoughtworks Technology Radar Vol.30: Languages and Frameworks'
description: 'Thoughtworks Technology Radar Vol.30 (2024 年 4 月) の Languages and Frameworks 象限 22 項目の要約で、Web とモバイルのフレームワーク、分散計算と機械学習のフレームワーク、LLM の推論・調整のライブラリ、Rust と Zig などの新しい言語、LangChain への注意をリングごとにまとめる。'
tags: [ai, thoughtworks, technology-radar, frameworks, llm, machine-learning, rust]
status: stable
verified: { by: claude-code/claude-opus-5-5, at: 2026-11-26T00:00:00Z }
stale_after: 2027-11-26T00:00:00Z
---

# Thoughtworks Technology Radar Vol.30: Languages and Frameworks

Thoughtworks Technology Radar Vol.30 (2024 年 4 月) の Languages and Frameworks (言語・フレームワーク) 象限の要約である。
Web とモバイルのフレームワーク、機械学習と LLM のためのライブラリ、Rust や Zig などの言語が並ぶ。
今号のこの象限に Adopt の項目は無く、Hold は LangChain の 1 項目である。

- 出典: Thoughtworks Technology Radar Volume 30 (PDF)、[thoughtworks.com/radar](https://www.thoughtworks.com/radar)

[TOC]

## Trial

### 84. Astro

- サーバーで HTML を描画し、送る JavaScript を最小にするマルチページアプリのフレームワークである。ブログやマーケティングサイトなど、内容中心のサイトに使った。
- アイランドアーキテクチャで、対話が必要な部分だけ好きなフロントエンドのフレームワークの部品を使える。描画とビルドが速く、構文は HTML の簡単な拡張で学びやすい。

### 85. DataComPy

- pandas や Spark などの 2 つの DataFrame を比較する Python ライブラリである。行と列の両方の単位で違いを詳しく示し、数値列の許容誤差や、報告しなくてよい既知の違いを指定できる。スモークテストに使っている。

### 86. Pinia

- Vue.js のストアと状態管理のライブラリで、現在の公式の状態管理ライブラリである。Vuex より API が簡単で手順が少なく、Composition 形式の API と TypeScript での型推論に強い。

### 87. Ray

- AI と Python のコードを、ノート PC からクラスターまで拡張するための統一フレームワークである。分散計算の仕組みと、機械学習を簡単にする AI ライブラリを持ち、PyTorch や TensorFlow と連携する。
- OpenAI や ByteDance が学習と推論に使っている。分散学習とハイパーパラメーター調整に使っており、拡張可能な機械学習のプロジェクトで試すことを勧める。

## Assess

### 88. Android Adaptability

- 負荷の高いアプリやゲームでは、発熱による性能の制限でフレームレートが上下し、動きがぎこちなくなる。
- Android Dynamic Performance Framework (ADPF) の Thermal API で熱の状態を知り、Hint API で最適な CPU の動作点を選ばせられる。Unity なら Adaptive Performance パッケージが両方に対応する。

### 89. Concrete ML

- 暗号化したデータのまま計算する完全準同型暗号 (FHE) で、プライバシーを守る機械学習を行うオープンソースの道具である。scikit-learn とほぼ同じ API で、PyTorch のネットワークも変換できる。専用のハードウェアがないと遅い。

### 90. Crabviz

- 対話的な呼び出しグラフを作る VS Code の拡張機能である。型、メソッド、関数、インターフェースをファイルごとにまとめ、呼び出しと実装の関係を示す。Language Server Protocol を使うので多くの言語に対応するが、静的解析に限られる。

### 91. Crux

- Rust で書かれた、オープンソースのクロスプラットフォームのアプリ開発フレームワークである。Elm アーキテクチャに影響を受け、副作用のない業務ロジックを Rust で書き、iOS、Android、Web で共有する。UI は SwiftUI、Jetpack Compose、React などのネイティブの仕組みで書く。

### 92. Databricks Asset Bundles

- Databricks の資産をソース管理、テスト、デプロイのためにまとめる、公式に推奨される方法になりつつある。dbx を置き換え始めている。
- ワークフロー、ジョブ、タスクの設定と実行するコードを 1 つのバンドルにして複数の環境に配置できる。ノートブックを本番に使うことには引き続き反対している。

### 93. Electric

- モバイルと Web のための local-first の同期フレームワークである。アプリは組み込みのローカルの SQLite と直接やり取りし、データは裏で中央の PostgreSQL と双方向に複製される。CRDT の考案者たちが作っている。

### 94. LiteLLM

- 各 LLM 提供者の API を OpenAI の API 形式にそろえて扱えるライブラリである。補完、埋め込み、画像生成に統一したインターフェースを提供し、各提供者の形式に変換する。
- LLM アプリの下のモデルを入れ替えるのに使った。ただし同じプロンプトでもモデルごとに応答は違うので、呼び出し方をそろえるだけでは最適にならない。

### 95. LLaMA-Factory

- LLM の性急なファインチューニングには引き続き注意を促すが、本当に必要な場合に使いやすい、オープンソースのファインチューニングと学習のフレームワークである。LLaMA、BLOOM、Mistral、Baichuan、Qwen、ChatGLM に対応し、LLaMA 7B の LoRA 調整に成功した。

### 96. MLX

- Apple シリコンで効率的に機械学習を行うための、オープンソースの配列フレームワークである。NumPy、PyTorch、Jax などに影響を受けている。
- 統合メモリのモデルで CPU と GPU の間のデータ転送の負担がなく、iPhone のような端末でのモデルの実行や端末上の AI への道を開く。

### 97. Mojo

- 研究と本番の隔たりを埋めることを目指す、AI 優先の新しいプログラミング言語である。Python の構文と生態系に、システムプログラミングとメタプログラミングの機能を組み合わせる。MLIR のコンパイラーバックエンドを使う初めての言語である。

### 98. Otter

- Go の競合のないキャッシュライブラリである。高いスループットと、S3-FIFO アルゴリズムによる高いヒット率を評価している。ジェネリクスに対応する。

### 99. Pkl

- Apple が社内で使っていた設定言語と道具で、オープンソース化された。型と検証の仕組みで、デプロイ前に設定の誤りを見つけられる。JSON、plist、YAML、properties を生成でき、IDE とコード生成の対応も広い。

### 100. Rust for UI

- WebAssembly で Rust をブラウザーでも使えるため、UI 開発に Rust を使う例が少しずつ増えている。
- Leptos や sauron は Web 開発向け、Dioxus などは Web に加えてデスクトップとモバイルにも対応する。

### 101. vLLM

- 受け取ったリクエストを連続してまとめて処理する (continuous batching) ことで、高いスループットとメモリ効率を持つ LLM の推論・提供エンジンである。Ray での分散推論や Docker での配置に対応する。
- 社内の仮想マシンで Docker の vLLM を動かし、OpenAI 互換の API でコーディング支援やチャットボットから使っている。設定を少し変えるだけで 7B から 70B のモデルに移れる。

### 102. Voyager

- Android の Jetpack Compose 向けのナビゲーションライブラリである。Linear、BottomSheet、Tab、Nested の型に対応し、Koin や Hilt と連携する。マルチプラットフォームで共通のナビゲーションを作るのに向く。

### 103. WGPU

- WebGPU の API に基づく Rust のグラフィックスライブラリで、GPU で汎用のグラフィックスと計算を効率よく扱える。OpenGL や WebGL の後を埋め、WebAssembly でブラウザーでも動く。

### 104. Zig

- C に近いが、より強い型付け、簡単なメモリ割り当て、名前空間などを持つ新しい言語である。単純で、実行を追いやすいことを目指す。
- LLVM のクロスコンパイルを簡単に使えるので、Zig のコードを書かずにクロスコンパイラーとして使う開発者もいる。C を検討中または使用中の場面で調べる価値がある。

## Hold

### 105. LangChain

- LLM のアプリを作るための多くの機能を持つが、使いにくく、複雑すぎると判断した。急速な変化に追従するなかで概念やパターンが変わり続け、API の設計も一貫せず冗長である。
- 内部で何が起きているかが見えにくく、LLM とその周辺のパターンを理解し制御しにくい。多くの場合、専用のフレームワークを最小限にした実装で足りる。用途によっては Semantic Kernel、Haystack、LiteLLM も検討する。

## See also

- [Thoughtworks Technology Radar Vol.30 の全体像と 4 つのテーマ](/references/ai/thoughtworks-technology-radar-vol-30/thoughtworks-radar-vol-30-overview.md)
- [Thoughtworks Technology Radar Vol.30: Techniques](/references/ai/thoughtworks-technology-radar-vol-30/thoughtworks-radar-vol-30-techniques.md)
- [Thoughtworks Technology Radar Vol.35: Languages and frameworks](/references/ai/thoughtworks-technology-radar-vol-35/thoughtworks-radar-vol-35-languages-and-frameworks.md)
