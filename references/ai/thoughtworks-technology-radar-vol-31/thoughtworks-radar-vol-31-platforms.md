---
type: reference
title: 'Thoughtworks Technology Radar Vol.31: Platforms'
description: 'Thoughtworks Technology Radar Vol.31 (2024 年 10 月) の Platforms 象限 18 項目の要約で、LLM の提供・可観測性・ベクトル検索の基盤、データ基盤、WASM や Rust で作られた新しい基盤をリングごとにまとめる。'
tags: [ai, thoughtworks, technology-radar, platform, llm, vector-database, webassembly]
status: stable
verified: { by: claude-code/claude-opus-5-5, at: 2026-11-26T00:00:00Z }
stale_after: 2027-11-26T00:00:00Z
---

# Thoughtworks Technology Radar Vol.31: Platforms

Thoughtworks Technology Radar Vol.31 (2024 年 10 月) の Platforms (基盤) 象限の要約である。
LLM の提供と可観測性、ベクトル検索、データ基盤に加え、WASM や Rust で作られた新しい基盤が並ぶ。
今号の Platforms に Adopt と Hold の項目は無い。

- 出典: Thoughtworks Technology Radar Volume 31 (PDF)、[thoughtworks.com/radar](https://www.thoughtworks.com/radar)

[TOC]

## Trial

### 24. Databricks Unity Catalog

- レイクハウス内のファイル、テーブル、機械学習モデルなどのデータガバナンスの仕組みで、オープンソースの Unity Catalog のマネージド版である。
- ガバナンス、メタストア管理、データ発見を 1 つでまかなえ、複数の道具を管理する手間が減る。Databricks 管理版には自動の災害復旧が無く、バックアップは自分で用意した。

### 25. FastChat

- LLM の学習・提供・評価のためのオープンな基盤である。複数のモデル (Llama 3.1、Mistral 7B など) を OpenAI 互換の API で提供するために使っている。
- 制御器とワーカーの構成で、vLLM などのワーカーを用途 (低遅延か高スループットか) に応じて増減できる。同じモデルでハイパーパラメーターを変えたワーカーを並べて A/B テストもできる。

### 26. GCP Vertex AI Agent Builder

- 自然言語かコードで AI エージェントを作れる基盤である。外部コネクターで企業データと連携し、試作から配備まで必要な道具がそろう。
- 構造化・非構造化データを扱う知識ベースや自動サポートなどのエージェントを、少ない準備で素早く作れた。

### 27. Langfuse

- LLM アプリケーションの観測・監視・評価の基盤である。トレース、分析、評価で、精度、費用、遅延、利用状況を把握できる。
- 記録したリクエストと中間段階はテストデータにもなる。RAG では、評価の低い会話を分析して、検索前・検索・生成のどこを直すべきかを特定できる。Langsmith も選択肢である。

### 28. Qdrant

- Rust で書かれたオープンソースのベクトル類似検索エンジン兼データベースである。
- 製品ごとの知識ベースを別のコレクションに分けるマルチテナントの企業向けベクトルストアとして使っている。

### 29. Vespa

- 低遅延・高スループットが要るアプリ向けのオープンソースの検索エンジン兼大規模データ処理基盤である。
- 複数の検索手法を組み合わせたハイブリッド検索、メタデータでの絞り込み、多段のランキング、1 文書に複数のベクトルを持たせる索引付けが評価されている。

## Assess

### 30. Azure AI Search

- 旧 Cognitive Search で、RAG の知識ベースなどに使うクラウドの検索サービスである。キーワード、ベクトル、ハイブリッドの検索に対応する。
- PDF などの文書を自動で取り込み、Azure OpenAI と連携できる。Azure 上のプロジェクトで RAG を作るなら検討する価値がある。

### 31. Databricks Delta Live Tables

- 信頼でき、保守しやすく、テストしやすいデータパイプラインを宣言的に作るフレームワークである。パイプライン全体を DAG で表示し、データの系譜を追いやすい。
- Databricks に深く統合されているため、入出力の口を自由に変えにくい。使う前に互換性を確かめる。

### 32. Elastisys Compliant Kubernetes

- 医療、金融、政府など規制の厳しい業界向けの Kubernetes ディストリビューションである。GDPR や HIPAA、ISO27001 への準拠を組み込み、ゼロトラストの設計で作られている。

### 33. FoundationDB

- 厳密な直列化可能性のトランザクションを持つ分散キーバリューストアを核にしたマルチモデルデータベースである。
- 構成要素を分けた設計で、トランザクションログ、ストレージサーバー、プロキシの数を負荷に応じて個別に増減できる。大きなクラスターでも運用しやすい。

### 34. Golem

- サーバーレスの状態を明示的な状態機械として永続化し、耐障害性と復旧を高める「耐久計算 (durable computing)」の推進役の 1 つである。
- 長時間のサガや AI エージェントのワークフローに向く。対応言語で書いた WebAssembly コンポーネントを動かし、起動が速い。Temporal と並ぶ選択肢である。

### 35. Iggy

- Rust で書かれた永続的なメッセージストリーミング基盤である。複数のストリーム・トピック・パーティション、QUIC・TCP・HTTP 上の TLS に対応し、単一サーバーで高いスループットを出す。
- クラスタリングと io_uring への対応が進めば、Kafka の代替になりうる。

### 36. Iroh

- IPFS を発展させた分散ファイル保存・配信システムである。ブロックの大きさの上限が無く、範囲ベースの集合照合でデータを同期できる。
- WASM でブラウザーに持ち込む計画があり、Web アプリに分散化を組み込む可能性がある。まだ非常に初期の段階である。

### 37. Large vision model (LVM) platforms

- 映像や画像を分割・合成・再構成・分析する大規模視覚モデル (LVM) を、本番で使うための新しい種類の基盤である。V7、NVIDIA Deepstream SDK、Roboflow がある。
- 映像データの収集、ラベル付け、微調整、配備、監視には視覚的な画面が要る。Deepstream と Roboflow は、GUI の開発環境と、アプリから呼べる API を両方持つ点が興味深い。

### 38. OpenBCI Galea

- 脳とコンピューターをつなぐインターフェース (BCI) と VR ヘッドセットを組み合わせた製品である。脳波などの生体信号、空間位置、視線追跡のデータを開発者が使える。
- 低レベルの信号処理を気にせず BCI アプリを作れるオープンソースの基盤として注目している。SDK は Unity や Unreal でデータを使える。

### 39. PGLite

- PostgreSQL を WASM にビルドしたもので、Linux の仮想マシンなしにブラウザー内で完全に動く。メモリ上の一時的なデータベースにも、IndexedDB への永続化にも使える。
- Electric と組み合わせると、PostgreSQL 上でリアクティブなローカルファーストのアプリを作れる。

### 40. SpinKube

- Kubernetes 上で WebAssembly を動かすオープンソースのサーバーレス実行環境である。
- コンテナの起動の遅さのためにピークに合わせて事前に用意する必要があるのに対し、WASM はミリ秒で起動するので、必要に応じた柔軟なサーバーレスにできる。

### 41. Unblocked

- 開発ライフサイクルの成果物 (コード、議論、文書) を見つけやすくする基盤である。ALM や協働の道具と連携し、コードについての関連する文脈をすぐに示す。
- 経験者の頭の中にある知識も記録して共有し、経験の浅い人でも使えるようにする。

## See also

- [Thoughtworks Technology Radar Vol.31 の全体像と 4 つのテーマ](/references/ai/thoughtworks-technology-radar-vol-31/thoughtworks-radar-vol-31-overview.md)
- [Thoughtworks Technology Radar Vol.31: Techniques](/references/ai/thoughtworks-technology-radar-vol-31/thoughtworks-radar-vol-31-techniques.md)
- [Thoughtworks Technology Radar Vol.31: Languages and frameworks](/references/ai/thoughtworks-technology-radar-vol-31/thoughtworks-radar-vol-31-languages-and-frameworks.md)
