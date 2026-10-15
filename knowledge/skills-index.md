# 再利用する手順

作業開始時は対象だけを読みます。パスは仕事場のルートからの相対パスです。

| 依頼 | 手順の正本 | Claude Code | Codex |
| --- | --- | --- | --- |
| まず相談／初期設定 | `.agents/skills/start-work/SKILL.md` | `/start-work` | `$start-work` |
| 会議の後処理 | `.agents/skills/process-meeting/SKILL.md` | `/process-meeting` | `$process-meeting` |
| 報告の材料・骨子 | `.agents/skills/prepare-report/SKILL.md` | `/prepare-report` | `$prepare-report` |
| 今月の経費 | `.agents/skills/prepare-expenses/SKILL.md` | `/prepare-expenses` | `$prepare-expenses` |
| 記録と引き継ぎ | `.agents/skills/close-session/SKILL.md` | `/close-session` | `$close-session` |
| 設定と仕事場の整理 | `.agents/skills/maintain-workspace/SKILL.md` | `/maintain-workspace` | `$maintain-workspace` |
| 記事・会話をWikiへ統合 | `.agents/skills/capture-context/SKILL.md` | `/capture-context` | `$capture-context` |
| 目的からWorkflowを構築 | `.agents/skills/plan-workflow/SKILL.md` | `/plan-workflow` | `$plan-workflow` |
| 実行を評価し手順改善を提案 | `.agents/skills/review-workflow/SKILL.md` | `/review-workflow` | `$review-workflow` |

コマンドが利用できなければ「このパスのSKILL.mdを読んで、○○を進めて」で同じ手順を使えます。自動検出は使用するアプリ・バージョン・起動場所によって異なります。

ワークフローの作成と実行許可・Skill昇格は別です。
