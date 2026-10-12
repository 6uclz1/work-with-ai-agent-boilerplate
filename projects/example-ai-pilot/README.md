# 社内AI試行：架空の完成例

このフォルダの人物・数字・意思決定はすべて説明用です。実際の業務実績ではありません。

## 読み方

1. project.mdで背景を読む。
2. sources/rawの会議前の現在地・タスクと新しい会議原本を読む。
3. meetings/2026-10-09-minutes.mdと、ルートのcurrent.md・tasks.mdを比較する。
4. outputs/summary.htmlをブラウザで開き、report-outline.mdで報告の構成を確認する。

## 会議の更新を再現する

入力は **sources/raw/pre-meeting-current.md、pre-meeting-tasks.md、2026-10-09-meeting.md、trial-metrics.csv** と project.md、sources/index.md です。会議前の決定はpre-meeting-currentに記録済みです。

「この入力から会議の後処理をして、sandbox-output/に新しく議事録・現在地・タスク・決定履歴を作って」と依頼します。完成例のcurrent、tasks、decisions、meetings、outputs、lessonsを入力に使わず、作業後に比較します。

## 特に見比べる点

- 利用者5人→8人はまだ提案。現時点の人数は5人のまま。
- 15件の試行の時間比較は12件。残り3件は比較不能で、時間削減率の分母へ混ぜない。
- 240分→156分は84分の短縮、35.0%。小規模な試行の記録であり全社の効果とは言わない。
- 説明資料更新は佐藤、2026-10-13。追加比較の担当は田中、期限は未確認。
- 不具合調査は完了ではなく継続。予算追加は決まっていない。
