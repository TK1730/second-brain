---
type: reference
title: 'AI ネイティブ SDLC プレイブック: 6 つのステージと成果物駆動の開発サイクル'
description: Anthropic の記事「The AI-Native SDLC Playbook」の要約で、コード実装が最速になった時代に開発ライフサイクルの 6 段階をバージョン管理された Markdown 成果物でつなぐ実践手法をまとめる。
tags: [ai, agent, claude, sdlc, software-engineering, workflow]
status: stable
verified: { by: antigravity/gemini-4-argon, at: 2026-11-15T00:00:00Z }
stale_after: 2027-11-15T00:00:00Z
---

# AI ネイティブ SDLC プレイブック: 6 つのステージと成果物駆動の開発サイクル

Anthropic のリソース記事 [The AI-Native SDLC Playbook](https://claude.com/ja/resources/articles/the-ai-native-sdlc-playbook) (英語版: [The AI-Native SDLC Playbook](https://claude.com/blog/the-ai-native-sdlc-playbook)) の要約。
コーディングエージェントの普及によって実装工程が劇的に高速化した現代において、計画から保守までのソフトウェア開発ライフサイクル (SDLC) 全体を、バージョン管理された Markdown 成果物 (Artifact) でつなぐ実践的なフレームワークを解説している。

## 背景と核心原則: 成果物で工程をつなぐ閉じたループ

Claude Code などのコーディングエージェントの普及により、「コードを書くこと (Build)」自体はもはや開発のボトルネックではなくなった。
一方で、従来の会議やチケットシステム、口頭での説明に依存した属人的な引き継ぎが、開発全体の律速段階 (ボトルネック) として浮き彫りになっている。

AI ネイティブ SDLC では、以下の核心原則によってこの課題を解決する。

- **1 ステージ 1 成果物の原則**: 各ステージはバージョン管理された 1 つの Markdown 成果物 (Artifact) を Git リポジトリにコミットして完了し、次のステージはその成果物を読み込むことから始まる。
- **共通コンテキストと監査証跡**: 人間と AI エージェントの双方が同じ Markdown ファイルを読み書きすることで、工程間のコンテキストの断絶を防ぎ、なぜその変更が行われたのかという監査証跡をコードと同じリポジトリ内に残す。

## 6 つのステージと主要な成果物・プレイ

AI ネイティブ SDLC は、Plan、Design、Build、Test、Deploy、Maintain の 6 つのステージで構成され、最後の Maintain から次の Plan へと還流する閉じたループを形成する。

| ステージ | 主要な成果物 / 仕組み | 役割と次工程への引き継ぎ |
| :--- | :--- | :--- |
| 1. Plan (計画) | `intent.md` | 顧客の課題や変更の意図・制約を定義し、Design の入力とする。 |
| 2. Design (設計) | `spec.md` | `intent.md` をもとに要件・設計・規約適合性を具体化する。 |
| 3. Build (構築) | `plan.md` / `CLAUDE.md` / Skills | `spec.md` から実装計画を立て、組織の規約とスキルを用いて実装する。 |
| 4. Test (テスト) | テストコード / Hooks / Evals | 画面検証やテスト実行ループを回し、品質とテスト改ざん防止を担保する。 |
| 5. Deploy (デプロイ) | PR / `REVIEW.md` / Human Gates | 非対話型エージェントのレビューとリスクに応じた人間の承認ゲートを通す。 |
| 6. Maintain (保守) | `bands.yaml` → 次の `intent.md` | 本番テレメトリの許容範囲逸脱を検知し、次の計画や Evals へ還元する。 |

### 1. Plan (計画) — `intent.md`

- 委員会で何週間もかけて要件定義を議論するのではなく、顧客からのフィードバックや現場の課題から、まだ仕様になる前の「変更の意図」を素早く言語化する。
- 「誰が・何に困り・どうなればよいか・制約は何か」を、人間と機械の双方が読める `intent.md` としてまとめ、Git でバージョン管理する。

### 2. Design (設計) — `spec.md`

- `intent.md` を入力として、AI エージェントとの対話セッションを通じて要件とアーキテクチャ設計を迅速に具体化する。
- 組織のブランド規約、セキュリティポリシー、UX 標準に適合した仕様書として `spec.md` を作成し、レビューを経てリポジトリにコミットする。

### 3. Build (構築) — `plan.md` / `CLAUDE.md` / Skills

- `spec.md` からいきなりコードを生成させるのではなく、まず計画モード (Plan Mode) 等を用いて変更対象ファイルと検証手順を定めた `plan.md` を作成する。
- リポジトリ固有の規約を記述した `CLAUDE.md` や、組織の専門知識・ワークフローをパッケージ化したスキル (Skills) およびサブエージェントを参照させながら、段階的にコードを実装する。

### 4. Test (テスト) — テストコードと継続的評価 (Evals)

- 実装が終わった後の QA ゲートを待つのではなく、実装中のエージェントに対してテスト実行やブラウザ / MCP ツールによる画面検証のフィードバックループを与える。
- エージェントがテストを通すためにテストコード自体を勝手に書き換えてしまう (Reward Hacking) のを防ぐため、フック (Hooks) による保護と CI 上での継続的評価 (Evals) を組み込む。

### 5. Deploy (デプロイ) — PR / `REVIEW.md` / 承認ゲート

- すべてのコード行を人間が目視で確認する従来のコードレビューから脱却する。
- サンドボックス環境で動作する非対話型エージェントに `REVIEW.md` の基準に沿ったレビューと検証を行わせ、高リスクな変更に対してのみフックや人間の承認ゲート (Human Gates) を要求する仕組みを CI/CD パイプラインに統合する。

### 6. Maintain (保守) — `bands.yaml` から次の `intent.md` へ

- 本番環境のテレメトリや、あらかじめ `bands.yaml` で定義した制御帯域 (メトリクスの許容範囲) からの逸脱・インシデントを継続的に監視・検知する。
- 問題が発生した際は場当たり的なホットフィックスで終わらせず、検知された事象を次のサイクルの `intent.md` や回帰防止の Evals へと恒久的に還元し、SDLC の閉じたループを回し続ける。

## See also

- [The AI-Native SDLC Playbook (日本語版)](https://claude.com/ja/resources/articles/the-ai-native-sdlc-playbook)
- [The AI-Native SDLC Playbook (英語版)](https://claude.com/blog/the-ai-native-sdlc-playbook)
- [Claude Code チームのコードレビューの進め方](/references/ai/claude-blog-claude-code-team-code-review.md)
- [PR の 60% を自動承認・自動マージするにはどうすればよいか](/references/ai/swizec-auto-approve-and-merge-60p-of-prs.md)
- [評価駆動開発 (EDD) とは何か: AI エージェントを継続的に改善する手法](/references/ai/langchain-blog-what-is-eval-driven-development.md)
