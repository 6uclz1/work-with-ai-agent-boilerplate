---
name: review-workflow
description: ワークフローの実行と人間の訂正を評価し、再発防止・回帰テスト・Skill改善案を作る。未検証の変更を自動昇格させない。
---

# 結果から実行手順を改善する

1. AGENTS、rules/evidence、rules/safety、rules/learning-loop、workflows/README.md、対象ワークフローを読む。
2. 成功基準と観測出力を分け、実行ログ・元資料・人間の訂正を照合する。未実行、失敗、理由不明を明示する。
3. templates/workflow-evaluation.mdに沿ってworkflows/evaluationsへ評価を保存。何が起き、どう修正したか、他案件に適用してよい根拠を残す。
4. 誤入力・不足入力、代表的な正常ケース、既存処理への回帰ケースを定義する。試していないものは未実行と記載する。
5. 改善はworkflows/draftsに新バージョン案として保存し、元の手順へ戻す方法を明記する。個別の訂正を無条件に共通ルールへ追加しない。
6. Skill正本を変えるには評価根拠、適用範囲、人間の承認を確認する。承認後はsync_skills.pyとcheck_workspace.pyで同期・構造点検する。
7. 権限・接続先・安全設定の緩和は別の明示的な許可を必要とする。レビュー処理そのものには権限昇格機能を持たせない。
