# 日常業務のAI作業フォルダ

『［みのるん式］ビジネスパーソンのためのClaude Code仕事術』（御田 稔）の実践を始めるための、独自に作成したサンプルです。書籍付属の公式テンプレートではありません。

日常業務を一つの仕事場に集め、原本から成果物までの根拠を残し、うまくいった手順を次回に再利用します。Claude CodeとCodexのどちらでも扱えるよう、**共通指示は `AGENTS.md` が正本**です。`CLAUDE.md` は `@AGENTS.md` を読み込みます。単数形の `AGENT.md` は用意していません。

## すぐ始める

1. ZIPを展開して、**このREADMEがある `work-boilerplate` 自体を作業フォルダとして開く**。隠しフォルダ `.agents` と `.claude` も同梱されています。
2. [START-HERE.md](START-HERE.md) の最初の依頼を貼る。資料や音声メモは `inbox/` に置く。
3. 最初は架空の `projects/example-ai-pilot/` で、会議メモから現在地とタスクを更新してみる。

依存パッケージ、外部サービス、APIキーは不要です。資料の読み書きはAIに頼めます。補助スクリプトを実行する場合だけPython 3.9以上が必要です。

## 何をどこに置くか

| 場所 | 役割 |
| --- | --- |
| `AGENTS.md` / `CLAUDE.md` | AIが作業を始めるときの入口 |
| `rules/` | 根拠・確認・記録に関する共通ルール |
| `context/` | 自分の役割、文体、仕事の一覧、接続状態 |
| `inbox/` | 未整理のメモや受け取った材料 |
| `projects/` | 案件別の原本・現在地・タスク・成果物 |
| `routines/` | 経費精算など繰り返す業務 |
| `knowledge/` | 共通の学び、手順の目次、用語 |
| `.agents/skills/` | 再利用する手順の正本。Codex向け |
| `.claude/skills/` | 同じ手順の配布コピー。Claude Code向け |
| `.claude/rules/` | Claude Code用の適用範囲付きの案内 |
| `.claude/settings.json` | Claude Codeの許可設定 |
| `templates/` | 新規案件、議事録、調査、報告などのひな形 |
| `logs/` / `handoffs/` | 作業記録と次回の再開地点 |
| `archive/` | 完了済みの仕事。移動しても根拠リンクを直す |
| `docs/` | 本との対応、設定の説明、検証結果 |
| `scripts/` | 新規案件の作成・スキル同期・構造点検 |

**資料をすべて起動時に読ませる必要はありません。** 入口と短い共通ルールを読んだら、仕事の一覧から対象案件へ進み、必要な原本だけを読みます。

## 同梱した完成例

- `projects/example-ai-pilot/`：架空の社内AI試行。会議前の現在地とタスク、新しい会議の原本、整理後の議事録、更新後の現在地とタスク、5枚の報告骨子、閲覧用HTMLを同梱。
- `routines/expenses/2026-10/`：架空の明細と証憑メモから、申請候補3,740円、証憑不足1件、私用除外1件を整理。**実際の会社規程ではない**サンプル。
- `routines/weekly-review/`：作業ログから週報を作るひな形。架空の実績を実際の週報へ混ぜない。
- `templates/project/`：実務を始めるときはこちらをコピー。サンプル案件の数字を消して使う必要はありません。

詳しい依頼例は [docs/EXAMPLES.md](docs/EXAMPLES.md)、書籍との対応は [docs/BOOK-MAPPING.md](docs/BOOK-MAPPING.md) にあります。

## 仕事が終わるたびに

「現在地とタスクを更新して、今回の学びを次回の手順に残して」で終えます。会話だけに記憶を預けず、根拠・判断・未完了をファイルへ残します。記録済みの事実と仮説は区別します。

## 設定を育てる

共通指示は `AGENTS.md`、仕事別の判断は案件内の `AGENTS.md`、再現する手順は `.agents/skills/` を編集します。スキル変更後は `python3 scripts/sync_skills.py` でClaude Code側へ反映します。配布コピーの直接編集は避けます。ZIPには同期済みの実ファイルを入れているので、初回の同期やシンボリックリンクは不要です。

設定の違いと確認方法は [docs/CONFIGURATION.md](docs/CONFIGURATION.md)。本の半自動化に沿い、送信・公開・正式な申請の前に人間が結果を確認する方針です。ローカルの整理や下書きは繰り返し確認を取らずに進めます。機密案件はこのフォルダの外に、独立した仕事場として置いてください。

## 拡張：Personal Wikiと自己改善するWorkflow（2026-10）

従来の資料・判断・Skill・handoffを維持して、**何を知っているか／なぜ判断したか／どう仕事を進めたか／次回どう直すか**をつなぐ層を追加しました。

| 対象 | 役割 |
| --- | --- |
| `knowledge/wiki/` | 出典を保持する、トピック別の更新可能な知識 |
| `knowledge/decisions/` | 案件横断の判断基準、詳細判断の参照先 |
| `workflows/drafts/` | 目的から合成した実行プランと改善案 |
| `workflows/evaluations/` | 実行・失敗・修正・回帰テストの証拠 |
| `rules/delegation.md` | 4D（Delegation / Description / Discernment / Diligence）による委任 |
| `rules/learning-loop.md` | Knowledge→Decision→Workflow→評価→Skill昇格の条件 |

新Skillは `capture-context` / `plan-workflow` / `review-workflow`。実例と設計詳細は [Knowledge & Workflow設計](docs/KNOWLEDGE-WORKFLOW.md) および [使い方](docs/KNOWLEDGE-WORKFLOW-EXAMPLES.md) を参照してください。

**自動の範囲**：エージェントが起動したセッション内で、根拠を抽出し計画・評価案を生成できます。常駐エージェントや無断の自動送信、自己権限拡大を導入するものではありません。公開リポジトリに実際の個人情報・機密資料を置かないでください。
