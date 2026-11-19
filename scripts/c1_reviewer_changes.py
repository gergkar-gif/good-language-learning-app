#!/usr/bin/env python3
"""What the reviewer changed in the ES C1 units Antigravity wrote (2026-11-19).

Antigravity writes C1 units unattended, one after another; Claude reads and fixes
them later. Before each new unit Antigravity runs this to learn from the fixes made
so far: for every C1 unit whose first commit says "written by Antigravity", it
compares each es-latam file of the unit as Antigravity committed it with the file
now, and prints every text that changed (old -> new), item by item. Units not read
yet show no changes.

    python scripts/c1_reviewer_changes.py            # every Antigravity unit
    python scripts/c1_reviewer_changes.py --last 3   # the last three only
    python scripts/c1_reviewer_changes.py --max 60   # at most 60 changes a unit (default 80)
"""
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COURSE, LEVEL = "es-latam", "c1"


def git(*args):
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True, encoding="utf-8").stdout


def leaves(node, path=""):
    if isinstance(node, str):
        yield path, node
    elif isinstance(node, dict):
        key = node.get("id")
        for k, v in node.items():
            yield from leaves(v, f"{path}.{k}" if path else (f"[{key}].{k}" if key else k))
    elif isinstance(node, list):
        for i, v in enumerate(node):
            yield from leaves(v, f"{path}[{i}]")


def unit_files(stems):
    out = []
    for st in stems:
        out += [f"content/{COURSE}/lessons/{LEVEL}/{st}.json", f"content/{COURSE}/exercises/{LEVEL}/{st}-ex.json",
                f"content/{COURSE}/vocabulary/{LEVEL}/{st}-voc.json"]
        out += [p for p in git("ls-files", f"content/{COURSE}/grammar/{LEVEL}/{st}-*").split()]
    n2 = stems[0].split("-")[1]
    out.append(f"content/{COURSE}/stories/original/{LEVEL}/{LEVEL}-{n2}.json")
    return out


def main(argv):
    last = int(argv[argv.index("--last") + 1]) if "--last" in argv else None
    cap = int(argv[argv.index("--max") + 1]) if "--max" in argv else 80
    table = json.loads((ROOT / f"content/{COURSE}/curriculum/units/{LEVEL}.json").read_text(encoding="utf-8"))
    log = git("log", "--format=%H %s", "--", f"content/{COURSE}/lessons/{LEVEL}")
    found = []
    for i, u in enumerate(table):
        n = i + 1
        commit = next((ln.split()[0] for ln in log.splitlines()[::-1]
                       if re.search(rf"Unit {n} \(", ln) and "written by Antigravity" in ln), None)
        if commit:
            found.append((n, u, commit))
    if last:
        found = found[-last:]
    if not found:
        print("no Antigravity-written C1 unit yet")
        return
    for n, u, commit in found:
        changes = []
        chal_old = json.loads(git("show", f"{commit}:content/{COURSE}/curriculum/challenges.json") or "{}").get("challenges", {})
        chal_new = json.loads((ROOT / f"content/{COURSE}/curriculum/challenges.json").read_text(encoding="utf-8")).get("challenges", {})
        for rel in unit_files(u["stems"]):
            old_raw = git("show", f"{commit}:{rel}")
            new_p = ROOT / rel
            if not old_raw or not new_p.exists():
                continue
            old = dict(leaves(json.loads(old_raw)))
            new = dict(leaves(json.loads(new_p.read_text(encoding="utf-8"))))
            for k in sorted(set(old) | set(new)):
                if old.get(k) != new.get(k):
                    changes.append((Path(rel).name, k, old.get(k), new.get(k)))
        for st in u["stems"]:
            o, w = dict(leaves(chal_old.get(st, {}))), dict(leaves(chal_new.get(st, {})))
            for k in sorted(set(o) | set(w)):
                if o.get(k) != w.get(k):
                    changes.append((f"challenge {st}", k, o.get(k), w.get(k)))
        reviews = sorted(ROOT.glob(f"imports/review/es-c1-antigravity-{n:02d}/re*.md"))
        print(f"## Unit {n} `{u['id']}`: {len(changes)} change(s) by the reviewer since {commit[:8]}"
              + (f"; review notes: {', '.join(str(r.relative_to(ROOT)) for r in reviews)}" if reviews else ""))
        for f, k, a, b in changes[:cap]:
            a = "(none)" if a is None else a
            b = "(removed)" if b is None else b
            # show the text around the first difference, so a change late in a long
            # screen paragraph is visible
            p = next((j for j, (x, y) in enumerate(zip(a, b)) if x != y), min(len(a), len(b)))
            start = max(0, p - 80)
            cut = lambda t: ("…" if start else "") + t[start:start + 240] + ("…" if len(t) > start + 240 else "")
            print(f"- {f} {k}\n    was: {cut(a)}\n    now: {cut(b)}")
        if len(changes) > cap:
            print(f"  … {len(changes) - cap} more (--max to see them)")
        print()


if __name__ == "__main__":
    main(sys.argv[1:])
