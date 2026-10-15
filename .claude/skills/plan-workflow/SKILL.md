---
name: plan-workflow
description: 曖昧な仕事から目的・入力・判断基準・停止条件を抽出し、WikiとDecisionと既存Skillを組み合わせて実行可能なワークフロー案を作る。
---

# 目的からワークフローを合成する

1. AGENTS、rules/safety、rules/delegation、rules/learning-loop、workflows/README.mdを読み、対象案件のAGENTSとcurrent/tasksを開く。
2. 目的と出力、完了条件、時間・費用・データの制約を整理する。WikiのINDEX、knowledge/decisionsのINDEX、knowledge/skills-indexから**該当するものだけ**読む。
3. Automation / Augmentation / 限定的Agencyから委任モードと理由を決め、依頼に含まれない権限を作り出さない。人間が確定していない判断はproposedとする。
4. templates/workflow.mdをworkflows/drafts/WF-YYYYMMDD-slug.mdへコピーし、必要入力、前提、段階ごとのツール・成果物・検証・失敗分岐・停止条件を埋める。根拠へのリンクも残す。
5. 実行を依頼されている場合、許されたローカル範囲の可逆な作業は進め、成功基準に照らして確かめる。外部送信・公開・正式提出・購入、権限拡大などは明示された承認境界を守る。
6. 各結果をlogsへ記録し、必要ならtemplates/workflow-evaluation.mdで評価を起こす。未実行は実施済みと書かない。
7. 反復に耐える手順でも、評価と人間の承認なしに既存Skillや共通ルールを書き換えない。
