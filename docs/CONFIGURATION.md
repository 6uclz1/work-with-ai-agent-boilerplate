# 指示と設定の仕組み

## 正本を一つにする

`AGENTS.md` を共通指示の正本にし、`CLAUDE.md` から `@AGENTS.md` で取り込みます。Codexの標準の指示名は複数形のAGENTS.mdです。単数形のAGENT.mdを追加しても、本サンプルでは自動認識を前提にしません。

`rules/` は両ツール共通の詳細ルールです。AGENTS.mdの読む順序から明示的に参照します。Claude Codeの `.claude/rules/expenses.md` は対象パスに応じた補助の案内だけを持ち、経費規程の本体を重複させません。

下位のAGENTS.mdは、ルートで開始したCodexが対象フォルダへ移るだけで必ず追加するとは限りません。そのため共通指示と各スキルで、対象のAGENTS.mdを明示的に開くよう指定しています。Claude Code側は下位のCLAUDE.mdから、その場所のAGENTS.mdを参照します。

## スキルを両方で使う

正本：`.agents/skills/<name>/SKILL.md`。配布コピー：`.claude/skills/<name>/SKILL.md`。同梱済みのコピーは通常の実ファイルなので、Windowsの展開でもシンボリックリンクは不要です。

```bash
python3 scripts/sync_skills.py --check
python3 scripts/sync_skills.py
python3 scripts/check_workspace.py
```

1行目は比較のみ。2行目はこのテンプレートが管理する6スキルだけを同期します。手元で作った別スキルは削除しません。配布コピーに独自変更がある場合は上書きを止め、どちらを採用するか整理してから再実行します。

各スキルのagents/openai.yamlはCodex向けの表示メタデータです。API・接続・追加ツールの権限は宣言していません。Claude Codeで自動検出されないときは、作業ルートと隠しフォルダの展開を確認し、SKILL.mdを直接パスで指定してください。

## 初期の許可設定

`.claude/settings.json` はClaude Codeにだけ適用されます。次の意図の、狭い範囲の初期設定です。

- 案件の成果物・議事録・正規化データ・状態、定常業務の成果物、ログと引き継ぎの通常編集を許可。
- raw配下の原本変更、安全ルール・入口・settings.json変更、よく使う削除やpushコマンドに確認を要求。
- `.env`、`.secrets` 配下、秘密鍵の通常読み取り・編集を拒否。
- シェルの包括許可、任意のMCPの許可、bypassPermissionsは設定しない。

実務用に許可を広げるときは、CLIの `/permissions` で実際の適用ルールを確認してください。このテンプレートより上位の組織設定・ユーザー設定が影響することがあります。アプリのUIに同じ設定機能がない場合は、その環境の許可設定を使います。

**文章の指示、Git除外、Claude Codeの権限設定は、それぞれ役割が違います。** ファイルのdenyは任意のPython等による間接アクセスをすべて隔離する仕組みではありません。settings.jsonはCodexには適用されません。強い境界が必要ならOS・sandboxのアクセス制御と独立した作業環境を使います。機密案件は一般の仕事場のサブフォルダへ置く方法では隔離できません。

Codex向けの実行ポリシーはこのZIPから自動設定しません。使う環境のsandboxと承認設定を確認し、AGENTS.mdを技術的なアクセス制御として扱わないでください。

## 最初の動作確認

「読んだ指示ファイルと、送信する前の確認点を短く説明して」と依頼します。Claude Code CLIでは `/memory` と `/permissions`、Codexでは新しいセッションで読み込んだ指示を確認できます。どちらも実行テストは利用する環境で行ってください。同梱の検証は構造・同期・補助スクリプト・例の整合性の点検です。

## 個人共通の好みと機密案件

このサンプルはフォルダ内で完結し、ホームディレクトリの設定を書き換えません。慣れたら全案件共通の短い好みだけをユーザースコープへ移せます。案件固有の情報や機密資料の場所をそこへ書かないでください。

機密案件を独立させるときは、templates/projectを別の作業ルートへコピーし、匿名化した共通指示とルールだけを選んで持ち込みます。外部フォルダの資料へのシンボリックリンクや、他顧客の所在を含む台帳は持ち込みません。

## 参照した公式仕様（2026-10-12確認）

- [CodexのAGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md)
- [CodexのSkills](https://learn.chatgpt.com/docs/build-skills)
- [Claude CodeのMemory](https://code.claude.com/docs/en/memory)
- [Claude CodeのSkills](https://code.claude.com/docs/en/skills)
- [Claude CodeのSettings](https://code.claude.com/docs/en/settings)
- [Claude CodeのPermissions](https://code.claude.com/docs/en/permissions)

製品の仕様は変わるため、拡張時は使用中のバージョンと公式文書を確認します。
