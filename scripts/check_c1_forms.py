#!/usr/bin/env python3
"""Find C1 formulas in HU B2 teaching files (ROADMAP 153, user's rule 2026-10-30).

C1 forms are rewritten, never kept, in B2 screens, items, speaking steps, goals and
challenges (docs/unit-agent-rules.md § 6b). Readers miss them in item stems and
lesson labels (B2 culture batches 34-40 and 42-48), so this lists every hit
instead of relying on a reviewer's grep. Stories (the world segments) may keep
them and are not searched.

    python scripts/check_c1_forms.py hu b2            # the whole level
    python scripts/check_c1_forms.py hu b2 <stem> ... # e.g. b2-demografia

Exit status 1 when anything is found. A hit inside a deliberate wrong option or
a C1 unit's own file is still listed: decide it by hand.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# The C1 list of the B2 read-through (focus notes and rulebook § 6b).
C1_FORMS = [
    r"feltéve, (hogy|ha)", r"kivéve, ha", r"\bhadd\b",
    r"kellett, hogy legyen", r"összességében", r"végső soron", r"mindent egybevetve",
    r"szíveskedj", r"nem áll módomban", r"megkockáztatom", r"hajlok arra",
    r"valószínűsíthető", r"feltételezhető",
]
PATTERN = re.compile("|".join(f"(?:{p})" for p in C1_FORMS), re.IGNORECASE)
FOLDERS = ("exercises", "grammar", "lessons")


def strings(node, where=""):
    if isinstance(node, str):
        yield where, node
    elif isinstance(node, dict):
        for k, v in node.items():
            yield from strings(v, f"{where}.{k}" if where else k)
    elif isinstance(node, list):
        for i, v in enumerate(node):
            yield from strings(v, f"{where}[{i}]")


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    course, level, stems = argv[0], argv[1], argv[2:]
    hits = 0
    files = []
    for folder in FOLDERS:
        files += sorted((ROOT / "content" / course / folder / level).glob("*.json"))
    files.append(ROOT / "content" / course / "curriculum" / "challenges.json")
    for f in files:
        if stems and f.name != "challenges.json" and not any(f.name.startswith(s) for s in stems):
            continue
        data = json.loads(f.read_text(encoding="utf-8"))
        for where, text in strings(data):
            if f.name == "challenges.json" and not where.startswith(f"{level}") and f".{level}" not in where:
                # challenges.json is keyed by lesson stem; keep only this level's entries
                if not any(seg.startswith(f"{level}-") for seg in re.split(r"[.\[\]]", where)):
                    continue
            if stems and f.name == "challenges.json" and not any(s in where for s in stems):
                continue
            m = PATTERN.search(text)
            if m:
                hits += 1
                print(f"{f.relative_to(ROOT)}: {where}: *{m.group(0)}* :: {text[:100]}")
    print(f"{hits} C1 formula(s) found")
    return 1 if hits else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
