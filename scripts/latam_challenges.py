"""Turn es-es challenge drafts into es-latam ones (ROADMAP 150; user,
2026-10-16: es-latam challenges are the es-es ones with only the course
variants changed). Every string goes through course_variants.convert
(*zumo* -> *jugo*, *billete* -> *boleto*); a draft with *vosotros*/*os*
forms or a word the converter refuses is listed and left out, for the
reviewer to write by hand. Done by hand in every Spanish batch before.

    python scripts/latam_challenges.py <es-es drafts.json> <out.latam.json>
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import course_variants as cv  # noqa: E402

VOSOTROS = re.compile(r"\b(vosotr[oa]s|os|habéis|sois|estáis|tenéis|\w+áis|\w+éis)\b", re.I)


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    drafts = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    out, left = {}, []
    for stem, d in drafts.items():
        new, bad = {}, []
        for k, v in d.items():
            vals = v if isinstance(v, list) else [v]
            conv = []
            for x in vals:
                if isinstance(x, str):
                    if VOSOTROS.search(x):
                        bad.append(f"vosotros in {k}: {x}")
                    y, changes, refused = cv.convert(x, "es-latam")
                    if refused:
                        bad.append(f"refused {refused} in {k}")
                    if changes:
                        print(f"  {stem}.{k}: " + ", ".join(f"{a} -> {b}" for a, b in changes))
                    conv.append(y)
                else:
                    conv.append(x)
            new[k] = conv if isinstance(v, list) else conv[0]
        if bad:
            left.append((stem, bad))
        else:
            out[stem] = new
    Path(sys.argv[2]).write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"{len(out)} es-latam drafts in {sys.argv[2]}, {len(left)} left out")
    for stem, bad in left:
        print(f"  left out {stem}: {'; '.join(bad)}")


if __name__ == "__main__":
    main()
