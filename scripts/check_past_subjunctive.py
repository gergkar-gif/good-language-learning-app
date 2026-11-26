#!/usr/bin/env python3
"""List imperfect subjunctive forms after *que* outside a *si* clause (ES B1 latam, 2026-11-26).

    python scripts/check_past_subjunctive.py <course> <level> <unit id> [<unit id> ...]

At B1 the imperfect subjunctive is met only in *si* + imperfect subjunctive hypotheticals (B1 Unit 4).
After a past verb (*pidió que protegiera*, *era injusto que pagaran*, *para que aprendieran*) it is
`correlacion-temporal-subjuntivo`, taught in B1 Unit 38: a B1 latam unit (after core Unit 36) must not
use it. The reviewer's own unit notes suggested it three times before Reader B caught it.

Heuristic, a report for reading: a word ending -ara(n/s), -iera(n/s), -ase(n/s), -iese(n/s) (or
*fuera(n)*, *hubiera(n)*) within four words after *que* (incl. *para que*, *antes de que*), with no
*si* in the six words before it. Scans the unit's lesson texts, screens, exercises and vocabulary.
Exits 1 when it finds any.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FORM = re.compile(r"^[a-záéíóúñ]+(?:aras?|aran|ieras?|ieran|ases?|asen|ieses?|iesen)$")
NOT = {"para", "cara", "clara", "claras", "separa", "declara", "prepara", "compara", "ampara", "repara",
       "dispara", "vara", "base", "bases", "clase", "clases", "fase", "fases", "frase", "frases", "casa",
       "pase", "caso", "masa", "tasa", "tasas", "raza", "fiera", "fieras", "pradera", "carrera", "bandera",
       "frontera", "fronteras", "manera", "maneras", "primera", "primeras", "tercera", "cualquiera",
       "madera", "escalera", "cartera", "ribera", "costera", "minera", "mineras", "petrolera", "extranjera",
       "extranjeras", "entera", "enteras", "sera", "hiera", "hacienda", "guaraní", "guaranís", "jase"}


def strings(x):
    if isinstance(x, str):
        yield x
    elif isinstance(x, dict):
        for k, v in x.items():
            if k not in ("english", "id", "teaches", "category", "type", "ref"):
                yield from strings(v)
    elif isinstance(x, list):
        for v in x:
            yield from strings(v)


def hits(text):
    words = re.findall(r"[a-záéíóúñü]+", text.lower())
    for i, w in enumerate(words):
        if w in NOT or not (FORM.match(w) or w in ("fuera", "fueran", "hubiera", "hubieran")):
            continue
        before = words[max(0, i - 4):i]
        if "que" in before and "si" not in words[max(0, i - 6):i]:
            yield w


def main():
    if len(sys.argv) < 4:
        sys.exit(__doc__)
    course, level, uids = sys.argv[1], sys.argv[2].lower(), sys.argv[3:]
    units = {u["id"]: u for u in json.loads((ROOT / f"content/{course}/curriculum/units/{level}.json").read_text(encoding="utf-8"))}
    found = 0
    for uid in uids:
        for stem in units[uid]["stems"]:
            lp = ROOT / f"content/{course}/lessons/{level}/{stem}.json"
            les = json.loads(lp.read_text(encoding="utf-8"))
            files = [lp] + [ROOT / f"content/{course}/{s['ref']}" for s in les.get("sections", []) if s.get("ref")]
            for f in files:
                if not f.is_file():
                    continue
                for s in strings(json.loads(f.read_text(encoding="utf-8"))):
                    for w in hits(s):
                        found += 1
                        print(f"{f.relative_to(ROOT)}  {w}  | {s[:140]}")
    print(f"{found} possible past-sequence subjunctive(s)")
    sys.exit(1 if found else 0)


if __name__ == "__main__":
    main()
