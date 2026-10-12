#!/usr/bin/env python3
"""Copy only the managed skills; refuse to overwrite locally modified copies."""
import argparse
import hashlib
import json
from pathlib import Path

NAMES = ('start-work', 'process-meeting', 'prepare-report', 'prepare-expenses',
         'close-session', 'maintain-workspace')
FILES = ('SKILL.md', 'agents/openai.yaml')


def digest(data):
    return hashlib.sha256(data).hexdigest()


def sync(root, check=False):
    source = root / '.agents' / 'skills'
    dest = root / '.claude' / 'skills'
    state_path = dest / '.sync-state.json'
    state = json.loads(state_path.read_text(encoding='utf-8')) if state_path.exists() else {}
    desired = {}
    changes = []
    errors = []
    for name in NAMES:
        for rel in FILES:
            key = name+'/'+rel
            src = source / key
            dst = dest / key
            if src.is_symlink() or dst.is_symlink() or any(p.is_symlink() for p in (source, source/name, dest, dest/name, dst.parent)):
                errors.append(key+': symlinkはこの実ファイル同期の対象外です')
                continue
            if not src.is_file():
                errors.append(key+': 正本が見つかりません')
                continue
            payload = src.read_bytes()
            wanted = digest(payload)
            desired[key] = wanted
            actual = digest(dst.read_bytes()) if dst.is_file() else None
            if actual != wanted:
                # If the copy differs from both source and last synced version,
                # preserve it for human reconciliation, including untracked copies.
                if actual is not None and actual != state.get(key):
                    errors.append(key+': 配布コピーに独自変更があります。正本へ取り込むか退避してください')
                else:
                    changes.append((dst, payload, key))
    if errors:
        for error in errors:
            print('ERROR: '+error)
        return 1
    if check:
        for _, _, key in changes:
            print('DIFF: '+key)
        if desired != state:
            print('DIFF: 同期台帳')
        if changes or desired != state:
            return 1
        print('OK: 6スキルの正本と配布コピーが一致')
        return 0
    for dst, payload, _ in changes:
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_bytes(payload)
    dest.mkdir(parents=True, exist_ok=True)
    state_path.write_text(json.dumps(desired, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print('Synced: '+str(len(changes))+' files; other skills unchanged')
    return 0


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='管理対象のスキルだけをClaude Code側へ同期します。')
    parser.add_argument('--check', action='store_true', help='比較だけ行い、変更しない')
    args = parser.parse_args()
    raise SystemExit(sync(Path(__file__).resolve().parents[1], args.check))
