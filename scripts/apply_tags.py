#!/usr/bin/env python3
"""Apply read-through tag decisions to a course's exercise files (ROADMAP 125 step 3).

    python scripts/apply_tags.py hu a1 decisions.json

decisions.json: {"<exercise id>": {"teaches": "<slug>", "category": "<only if it changes>",
                                   "ds": {"<option index>": "<slug>"}}}

Every exercise in a touched file must have a decision, so nothing is skipped
silently. Rewrites only `teaches`, `category` and `distractor_skills`; keeps
key order and line endings. Lock the unit afterwards with lock_tags.py.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main():
    course, level, dec_path = sys.argv[1], sys.argv[2], sys.argv[3]
    dec = json.loads(Path(dec_path).read_text(encoding="utf-8"))
    seen = set()
    for p in sorted((ROOT / "content" / course / "exercises" / level).glob("*.json")):
        raw = p.read_bytes().decode("utf-8")
        d = json.loads(raw)
        exs = d.get("exercises", [])
        if not any(e.get("id") in dec for e in exs):
            continue
        missing = [e.get("id") for e in exs if e.get("id") not in dec]
        if missing:
            sys.exit(f"{p.name}: no decision for {missing}")
        new_exs = []
        for e in exs:
            dd = dec[e["id"]]
            seen.add(e["id"])
            out = {}
            for k, v in e.items():
                if k == "distractor_skills":
                    continue
                if k == "category" and dd.get("category"):
                    v = dd["category"]
                if k == "teaches":
                    if not dd.get("teaches"):
                        continue  # reading items stay untagged: no key, not []
                    v = [dd["teaches"]]
                out[k] = v
                if k == "teaches" and dd.get("ds"):
                    out["distractor_skills"] = dd["ds"]
            if "teaches" not in out and dd.get("teaches"):
                # item had no teaches key (e.g. a reading item now tagged): add it
                out["teaches"] = [dd["teaches"]]
                if dd.get("ds"):
                    out["distractor_skills"] = dd["ds"]
            new_exs.append(out)
        d["exercises"] = new_exs
        nl = "\r\n" if "\r\n" in raw else "\n"
        text = json.dumps(d, ensure_ascii=False, indent=2).replace("\n", nl)
        if raw.endswith("\n"):
            text += nl
        p.write_bytes(text.encode("utf-8"))
        print("wrote", p.name, len(exs))
    left = set(dec) - seen
    if left:
        sys.exit(f"decisions for unknown exercises: {sorted(left)}")


if __name__ == "__main__":
    main()
