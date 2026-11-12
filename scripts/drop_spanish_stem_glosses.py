"""Drop the Spanish gloss from English question stems (ROADMAP 153, ES B1).

The generator wrote many B1 question stems as "English question? [¿Spanish
question?]". The Spanish half is metalanguage the learner has not met
(*conector, concesión, subjuntivo, expresa*), so `unmet-words.js` flags it,
and the English half already asks the question. Readers removed these by hand
in every batch; this does it by script, per batch:

    python scripts/drop_spanish_stem_glosses.py <course> <level> <stem prefix> [...] [--apply]

Only a `question` that has English before the bracket and a bracket that
starts with ¿ or ¡ is changed; anything else is left alone.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAT = re.compile(r'^(?P<en>[A-Z][^\[\]¿¡]*?[?.:»"])\s*\[\s*[¿¡][^\]]*\]\s*$')


def main():
    args = [a for a in sys.argv[1:] if a != "--apply"]
    apply = "--apply" in sys.argv
    if len(args) < 3:
        sys.exit(__doc__)
    course, level, prefixes = args[0], args[1], args[2:]
    folder = ROOT / "content" / course / "exercises" / level
    total = 0
    for f in sorted(folder.glob("*-ex.json")):
        if not any(f.name.startswith(p) for p in prefixes):
            continue
        raw = f.read_text(encoding="utf-8")
        data = json.loads(raw)
        n = 0
        for e in data.get("exercises", []):
            q = e.get("question")
            if isinstance(q, str):
                m = PAT.match(q)
                if m:
                    e["question"] = m.group("en")
                    n += 1
        if n:
            total += n
            print(f"{'fixed' if apply else 'would fix'} {f.name}: {n}")
            if apply:
                ind = len(re.search(r'\n( +)"', raw).group(1))
                f.write_text(json.dumps(data, ensure_ascii=False, indent=ind) + ("\n" if raw.endswith("\n") else ""), encoding="utf-8")
    print(f"{total} stem(s) {'fixed' if apply else 'to fix'}")


if __name__ == "__main__":
    main()
