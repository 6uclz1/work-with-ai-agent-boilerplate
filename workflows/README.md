# 目的から合成するワークフロー

Workflowは「目的 → 必要入力 → 計画 → 実行 → 検証 → 振り返り」を一つの再利用可能な仕事の定義として記録する。最初はMarkdownで運用し、専用のワークフローエンジンや外部DBは必要になってから検討する。

- `drafts/`：AIが提案・試行するワークフロー。**この時点では安定版Skillではない**。
- `evaluations/`：実行ごとの予測・観測・テスト・失敗・人間の訂正・改善差分。
- テンプレート：[workflow](../templates/workflow.md) / [evaluation](../templates/workflow-evaluation.md)
- レビュー済みで再利用価値のある手順だけ `.agents/skills/` に反映し、Claude Code側へ同期する。
- 使用時は [4D委任基準](../rules/delegation.md) と [学習ループ](../rules/learning-loop.md) を参照する。

## ライフサイクル

1. `plan-workflow`：既存の知識・判断・Skillから手順を自動提案する。曖昧な点は `未確認`。
2. 実行：**既存の**ツール権限と依頼範囲のみで進める。ステップごとに完了条件と停止条件を点検。
3. `review-workflow`：実行後の証拠を評価し、改善をdraftに提案する。承認済みSkillを無検証で上書きしない。
4. 回帰テスト・人間の承認を経てapprovedへ移す。廃止時はdeprecatedとして後継へリンク。

## 重要な区別

「実行できた」≠「完了条件を満たした」≠「今後も自動実行してよい」。未確認・失敗・人間の保留をそれぞれ記録する。
