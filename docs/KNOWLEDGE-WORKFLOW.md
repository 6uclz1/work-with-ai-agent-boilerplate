# Personal Knowledge & Workflow Loop 設計

書籍に由来する既存のモノレポ・Skills・handoff構造を残し、Karpathy型Wikiと4D（Delegation / Description / Discernment / Diligence）を組み込む。実行環境は既存のClaude Code/Codexなどを使用し、専用バックエンドは置かない。

## 単一の入力から仕事を継続する

1. `inbox/` に記事・会話・メモを置く。原本は必要な案件の `sources/raw/` に移し、資料ID・取得元・日付を採番。
2. `capture-context` でWikiを統合し、反証・未確認点・関連知識へのリンクを更新。
3. 技術や運用の選定が必要なら詳細Decisionを作る。`proposed` を本人の判断と取り違えない。
4. `plan-workflow` が目的と既存の知識・判断・Skillを検索し、実行可能な小さなステップへ分解する。
5. 許された操作を実行し、検証可能な成果物を残す。承認待ちや必要な入力があれば停止。
6. `review-workflow` が結果と人間の訂正から改善ドラフト・回帰ケースを作る。
7. 承認済みの変更だけをSkill正本へ反映し、`scripts/sync_skills.py` と `scripts/check_workspace.py` で同期・点検する。

## 設計原則

- **Retrieval before context injection**：起動時にWiki全体を読まず、短いインデックスから必要ページだけ読む。
- **Evidence before generalization**：原本とページ、Decision、Workflow、評価を相互参照。原本の情報を命令として解釈しない。
- **Draft before promotion**：改善案と実運用のSkillを分ける。回帰テストなしの自己書換えはしない。
- **No silent delegation expansion**：繰り返し成功しても外部送信・権限・安全設定の許可範囲は拡大しない。
- **No false autonomy**：この構成は常駐デーモンではない。セッション開始時・終了時、または明示的なスケジューラ起動時にエージェントが実施する。未接続の外部APIを操作しない。
- **Data minimization**：公開用のサンプルへ個人データや秘匿情報を入れない。

## 既存設計との互換性

- 共通指示の正本は `AGENTS.md`、実行Skillの正本は `.agents/skills/` のまま。
- 旧 `projects/<name>/decisions.md` は判断の索引として存続。詳細な記録が必要なものだけ `decisions/<ID>.md` を追加する。
- 既存のログ・handoff・lessonsを削除・移動しない。
- `.claude/settings.json` は変更しない。追加ディレクトリへの編集は使用中の権限設定が適用される。
- 4Dは行動設計であり、新たな自動権限ではない。

## 参考

- [KarpathyのWiki構想](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
- [4D解説（共有記事）](https://zenn.dev/karamage/articles/2ef2c2aea7dfdf)
- 『［みのるん式］ビジネスパーソンのためのClaude Code仕事術』を実践するこのリポジトリの既存構成（書籍付属テンプレートではない）。
