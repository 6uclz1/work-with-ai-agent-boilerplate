#!/usr/bin/env python3
"""Create an empty project without overwriting existing work. Standard library only."""
import argparse
from datetime import datetime, timezone, timedelta
from pathlib import Path
import re
import shutil


def main():
    parser = argparse.ArgumentParser(description='空の案件を作成して仕事の一覧に登録します。')
    parser.add_argument('slug', help='英小文字・数字・ハイフンによる案件ID')
    parser.add_argument('--title', required=True, help='案件名')
    args = parser.parse_args()
    if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', args.slug):
        parser.error('slugは英小文字・数字と区切りのハイフンのみです。')
    if not args.title.strip() or any(c in args.title for c in '\r\n|'):
        parser.error('案件名は改行や | を含まない文字列にしてください。')
    root = Path(__file__).resolve().parents[1]
    target = root / 'projects' / args.slug
    if target.exists():
        parser.error('既存の案件は上書きしません。別のIDを選んでください。')
    shutil.copytree(root / 'templates' / 'project', target)
    p = target / 'project.md'
    p.write_text(p.read_text(encoding='utf-8').replace('案件名：未設定', '案件名：'+args.title.strip()), encoding='utf-8')
    today = datetime.now(timezone(timedelta(hours=9))).date().isoformat()
    current = target / 'current.md'
    current.write_text(current.read_text(encoding='utf-8').replace('最終更新：未設定', '最終更新：'+today), encoding='utf-8')
    index = root / 'context' / 'work-map.md'
    with index.open('a', encoding='utf-8') as f:
        f.write('\n## '+args.slug+'\n\n')
        f.write('- 案件名：'+args.title.strip()+'\n')
        f.write('- 区分：実案件（内容・データ範囲は未設定）\n')
        f.write('- 入口：[案件の前提](../projects/'+args.slug+'/project.md)\n')
        f.write('- 状態：着手前。作成日：'+today+'（Asia/Tokyo）\n')
    print('Created: projects/'+args.slug)


if __name__ == '__main__':
    main()
