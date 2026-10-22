"""Dump the exercises check-content flags for the mechanical pre-pass of a
batch (HU B1 plan, ROADMAP 153): the items a fixer rewrites before the read,
so readers spend their tokens reading rather than evening out options.

    python scripts/dump_flagged.py <course> <level> <out.md> <unit id> [<unit id> ...]
        [--checks length-giveaway,tell-absolute,tell-time-word]

For each unit it writes one section: every flagged exercise as compact JSON
(only the fields a fix touches) with its findings and file. The fixer answers
with one fixes file per unit (format: scripts/apply_replacements.py), which
check_fixes.py then sorts as usual; a fix that brings an unmet word or a new
finding is rejected there, so the dump carries no word lists.
"""
import json
import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEFAULT = "length-giveaway,tell-absolute,tell-time-word"
FIELDS = ("type", "question", "sentence", "prompt", "options", "correct", "answer", "answers", "english", "hint")


def main():
    args = sys.argv[1:]
    checks = DEFAULT
    if "--checks" in args:
        i = args.index("--checks")
        checks = args[i + 1]
        del args[i:i + 2]
    if len(args) < 4:
        sys.exit(__doc__)
    course, level, out, units = args[0], args[1].lower(), Path(args[2]), args[3:]
    wanted = set(checks.split(","))
    parts, total = [], 0
    for uid in units:
        r = subprocess.run([sys.executable, "scripts/check-content.py", course, level, uid],
                           cwd=ROOT, capture_output=True, text=True, encoding="utf-8")
        hits = defaultdict(list)
        for line in r.stdout.splitlines():
            m = re.match(r"(?:ERROR|suspect)\s+(\S+)\s+(\S+)\s+(.*?)\s+\((content/\S+)\)$", line)
            if m and m.group(1) in wanted:
                hits[(m.group(4), m.group(2))].append(f"{m.group(1)}: {m.group(3)}")
        parts.append(f"## {uid} ({len(hits)} items)\n\nFixes file: `fixes-{uid}.json`\n")
        cache = {}
        for (f, eid), found in sorted(hits.items()):
            if f not in cache:
                cache[f] = {e["id"]: e for e in json.loads((ROOT / f).read_text(encoding="utf-8")).get("exercises", [])}
            e = cache[f].get(eid)
            if e is None:
                continue
            item = {k: e[k] for k in FIELDS if k in e}
            parts.append(f"- `{eid}` in `{f}`: {'; '.join(found)}\n  `{json.dumps(item, ensure_ascii=False)}`")
            total += 1
        parts.append("")
    out.write_text("\n".join(parts), encoding="utf-8")
    print(f"wrote {out}: {total} flagged item(s) in {len(units)} unit(s)")


if __name__ == "__main__":
    main()
