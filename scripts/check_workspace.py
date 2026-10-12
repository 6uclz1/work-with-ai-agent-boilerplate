#!/usr/bin/env python3
"""Check local structure and links. Does not judge business correctness."""
import json
from html.parser import HTMLParser
from pathlib import Path
import re
from urllib.parse import unquote
from sync_skills import sync, NAMES


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        for name, value in attrs:
            if name in ('href', 'src') and value:
                self.links.append(value)


def main():
    root = Path(__file__).resolve().parents[1]
    errors = []
    required = ('AGENTS.md','CLAUDE.md','README.md','START-HERE.md',
                'rules/safety.md','rules/evidence.md','rules/records.md',
                'context/profile.md','context/work-map.md','knowledge/skills-index.md',
                '.claude/settings.json','templates/project/project.md')
    for name in required:
        if not (root/name).is_file():
            errors.append('必須ファイル不足: '+name)
    for name in NAMES:
        path = root/'.agents/skills'/name/'SKILL.md'
        if not path.is_file():
            errors.append('スキル不足: '+name)
            continue
        text = path.read_text(encoding='utf-8')
        match = re.match(r'^---\nname: ([a-z0-9-]+)\ndescription: ([^\n]+)\n---\n', text)
        if not match or match[1] != name or not match[2].strip():
            errors.append('スキルの名前・説明が不正: '+name)
        if '[TODO:' in text:
            errors.append('未完成のスキル: '+name)
    for path in root.rglob('*.json'):
        try:
            json.loads(path.read_text(encoding='utf-8'))
        except (ValueError, UnicodeError):
            errors.append('JSON不正: '+str(path.relative_to(root)))
    for path in root.rglob('*'):
        if not path.is_file() or '.git' in path.parts:
            continue
        links = []
        if path.suffix == '.md':
            text = path.read_text(encoding='utf-8')
            links = re.findall(r'\[[^\]]*\]\(([^)]+)\)', text)
            if path.name == 'CLAUDE.md':
                links += re.findall(r'^@([^\s]+)$', text, re.M)
        elif path.suffix == '.html':
            parser = Links()
            parser.feed(path.read_text(encoding='utf-8'))
            links = parser.links
        for link in links:
            if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', link) or link.startswith('#'):
                continue
            clean = unquote(link.split('#',1)[0].split('?',1)[0])
            if clean and not (path.parent/clean).exists():
                errors.append(str(path.relative_to(root))+': リンク切れ '+link)
    if sync(root, check=True):
        errors.append('スキルの同期が必要、または競合があります')
    for error in errors:
        print('ERROR: '+error)
    if errors:
        return 1
    print('OK: 指示ファイル、6スキル、JSON、ローカルリンクを点検')
    print('この点検は業務内容・認証・外部サービスの権限を検証しません。')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
