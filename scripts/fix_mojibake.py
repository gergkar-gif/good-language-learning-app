#!/usr/bin/env python3
"""Undo UTF-8 text that was decoded as Windows-1252 (mojibake: *mindazonÃ¡ltal*, *endÅ‘*).

Found in all four HU level tests on 2026-11-25 (214 sequences, mostly in answer
options). Each JSON string with a mojibake marker is re-encoded as cp1252 and
decoded as UTF-8; a string that does not round-trip cleanly is left as it is
and listed, never guessed.

    python scripts/fix_mojibake.py <file.json> [...] [--dry-run]
"""
import json
import re
import sys
from pathlib import Path

MARK = re.compile(r"[ÃÅÄ][\u0080-ÿ‘-›Œ-Ÿ]")


def fix(s):
    if not MARK.search(s):
        return s, None
    try:
        out = s.encode("cp1252").decode("utf-8")
    except (UnicodeEncodeError, UnicodeDecodeError):
        # mixed strings: fix each marked run on its own
        def run(m):
            try:
                return m.group(0).encode("cp1252").decode("utf-8")
            except (UnicodeEncodeError, UnicodeDecodeError):
                return m.group(0)
        out = re.sub(r"(?:[ÃÅÄ][\u0080-ÿ‘-›Œ-Ÿ])+", run, s)
    return out, (None if not MARK.search(out) else s)


def walk(node, changed, left):
    if isinstance(node, str):
        new, bad = fix(node)
        if new != node:
            changed.append((node, new))
        if bad:
            left.append(bad)
        return new
    if isinstance(node, list):
        return [walk(v, changed, left) for v in node]
    if isinstance(node, dict):
        return {k: walk(v, changed, left) for k, v in node.items()}
    return node


def main(argv):
    dry = "--dry-run" in argv
    files = [a for a in argv if not a.startswith("--")]
    if not files:
        sys.exit(__doc__)
    for f in files:
        p = Path(f)
        raw = p.read_text(encoding="utf-8")
        changed, left = [], []
        new = walk(json.loads(raw), changed, left)
        ind = 1 if raw.startswith('{\n "') else 2
        if changed and not dry:
            p.write_text(json.dumps(new, ensure_ascii=False, indent=ind) + "\n", encoding="utf-8")
        print(f"{f}: {len(changed)} string(s) fixed, {len(left)} left unfixed")
        for s in left:
            print("   unfixed:", s[:120])


if __name__ == "__main__":
    main(sys.argv[1:])
