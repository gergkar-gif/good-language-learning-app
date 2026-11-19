#!/usr/bin/env python3
"""Spanish forms on an ES C1 unit's screens that an earlier core screen already shows (2026-11-19).

The most frequent defect of the Antigravity C1 units (Units 13-19): a screen presents as new a form
the learner already knows (*a raíz de*, *mientras que*, the accidental *se*, *como* + subjunctive).
This lists, for each screen of the unit, every italicised Spanish form that
appears italicised on an earlier core screen of es-latam (A1 to the unit before), with the first
unit that shows it, and whether the screen says it is known ("You know …" or "from <Level> Unit N"
near it). Every hit marked NOT RECAPPED must be named as known, with that unit, or dropped.

    python scripts/c1_known_forms.py <unit id>        # e.g. warnings-conditions
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import unit_numbers as un  # noqa: E402

COURSE = "es-latam"
LEVELS = ["a1", "a2", "b1", "b2", "c1"]
ITAL = re.compile(r"\*([^*]{2,60})\*")
# English grammar words writers italicise; not Spanish forms
META = {"preterite", "imperfect", "imperfecto", "subjunctive", "indicative", "pluperfect", "gerund",
        "infinitive", "conditional", "participle", "future", "present", "perfect", "passive", "clitic",
        "pretérito", "indefinido", "subjuntivo", "indicativo", "gerundio", "infinitivo", "condicional"}


def spanish_form(f):
    if re.search(r"[()\[\]=;:]|^[,.)\s]|[,\s]$", f):
        return False
    words = re.findall(r"[a-záéíóúüñ]+", f)
    return bool(words) and not all(w in META or w in ("pluperfect", "subjunctive", "past", "simple", "compound") for w in words)


def screens_of(lv, stem):
    lesson = ROOT / f"content/{COURSE}/lessons/{lv}/{stem}.json"
    if not lesson.exists():
        return []
    secs = json.loads(lesson.read_text(encoding="utf-8")).get("sections", [])
    return [ROOT / f"content/{COURSE}" / s["ref"] for s in secs if s.get("type") == "grammar" and s.get("ref")]


def forms(path):
    d = json.loads(path.read_text(encoding="utf-8"))
    out, texts = set(), []
    for s in d.get("sections", []):
        if s.get("type") in ("text", "tip"):
            c = s.get("content") or ""
            texts.append(c)
            out |= {m.strip().lower() for m in ITAL.findall(c) if spanish_form(m.strip().lower())}
    return out, " ".join(texts)


def main(argv):
    if not argv:
        sys.exit(__doc__)
    uid = argv[0]
    seen = {}                      # form -> (level, index) of the first core unit showing it
    target = None
    for lv in LEVELS:
        table = json.loads((ROOT / f"content/{COURSE}/curriculum/units/{lv}.json").read_text(encoding="utf-8"))
        for i, u in enumerate(table):
            if u.get("track", "core") != "core":
                continue
            if lv == "c1" and u["id"] == uid:
                target = (i, u)
                break
            for st in u["stems"]:
                for scr in screens_of(lv, st):
                    if scr.exists():
                        for f in forms(scr)[0]:
                            seen.setdefault(f, (lv, i))
        if target:
            break
    if not target:
        sys.exit(f"no C1 core unit {uid!r}")
    i, u = target
    total = 0
    for st in u["stems"]:
        for scr in screens_of("c1", st):
            if not scr.exists():
                continue
            fs, text = forms(scr)
            hits = sorted(f for f in fs if f in seen and len(f) > 3)
            if not hits:
                continue
            print(f"## {scr.stem}")
            for f in hits:
                lv, j = seen[f]
                name = un.name(COURSE, lv, j)
                near = re.search(rf"\*{re.escape(f)}\*[^.]{{0,160}}(Unit \d+)|(You know|from (A1|A2|B1|B2|C1) Unit \d+)[^.]{{0,200}}\*{re.escape(f)}\*", text, re.I)
                flag = "recapped" if near else "NOT RECAPPED"
                total += flag != "recapped"
                print(f"- *{f}*: first on a screen in {name} -> {flag}")
    print(f"{total} form(s) not recapped (a reading aid: decide each; a common form like *haber* needs no recap)")


if __name__ == "__main__":
    main(sys.argv[1:])
