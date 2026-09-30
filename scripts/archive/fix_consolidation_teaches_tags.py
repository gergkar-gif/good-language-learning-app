#!/usr/bin/env python3
"""
fix_consolidation_teaches_tags.py
----------------------------------
Fixes two problems:
1. a1-gustar-consolidation-ex.json uses "consolidation" as a catch-all
   teaches tag on every exercise — replaces with real grammar point tags.
2. a1-abilities, a1-continuous, a1-demonstrative, a1-doler, a1-reflexive
   consolidation exercises have 5 specific sub-point tags but the audit
   rule requires 8+. Adds cumulative A1 crossover tags to select exercises
   (appropriate — these ARE cumulative review lessons).
"""
import json
from pathlib import Path

ROOT = Path(__file__).parent.parent
EX_DIR = ROOT / "content" / "es" / "exercises" / "a1"

# ─────────────────────────────────────────────────────────────────────────────
# 1. Re-tag gustar exercises with real grammar points
# ─────────────────────────────────────────────────────────────────────────────
GUSTAR_RETAG = {
    "a1.gustar.cons.ex01": ["gustar-plural"],     # gustan vs gusta
    "a1.gustar.cons.ex02": ["encantar"],
    "a1.gustar.cons.ex03": ["iop-gustar"],        # indirect object pronouns
    "a1.gustar.cons.ex04": ["gustar-negation", "articles"],
    "a1.gustar.cons.ex05": ["gustar-plural"],
    "a1.gustar.cons.ex06": ["gustar-infinitive"],
    "a1.gustar.cons.ex07": ["iop-gustar"],
    "a1.gustar.cons.ex08": ["interesar"],
    "a1.gustar.cons.ex09": ["encantar", "gustar-agreement"],
    "a1.gustar.cons.ex10": ["iop-gustar"],
    "a1.gustar.cons.ex11": ["gustar", "hobbies"],  # dialogue
    "a1.gustar.cons.ex12": ["iop-gustar", "encantar"],
    "a1.gustar.cons.ex13": ["gustar", "gustar-plural"],
    # The two fill-blank exercises added by the previous script
    "a1.gustar.cons.ex14": ["gustar"],             # added earlier
    "a1.gustar.cons.ex15": ["hobbies"],            # added earlier
}

# ─────────────────────────────────────────────────────────────────────────────
# 2. Add crossover tags to existing exercises in 5-tag lessons
#    (adds 3+ cumulative A1 tags that these review exercises legitimately cover)
# ─────────────────────────────────────────────────────────────────────────────
CROSSOVER_TAGS = {
    "a1-abilities-consolidation": {
        # Add: present-tense, negation, ser at minimum (all appear in exercises)
        "a1.abi.cons.ex01": ["poder-infinitivo", "present-tense"],
        "a1.abi.cons.ex02": ["saber-infinitivo", "present-tense"],
        "a1.abi.cons.ex07": ["a-personal", "articles"],
        "a1.abi.cons.ex08": ["saber-vs-conocer", "negation"],
        "a1.abi.cons.ex11": ["pedir-favores", "present-tense"],
        "a1.abi.cons.ex12": ["a-personal", "ser"],
    },
    "a1-continuous-consolidation": {
        "a1.cont.cons.ex01": ["estar-ando", "present-tense"],
        "a1.cont.cons.ex02": ["estar-iendo", "present-tense"],
        "a1.cont.cons.ex05": ["gerundios-irregulares", "estar"],
        "a1.cont.cons.ex08": ["presente-vs-continuo", "present-tense"],
        "a1.cont.cons.ex09": ["conversacion-continuo", "ser"],
        "a1.cont.cons.ex12": ["presente-vs-continuo", "negation"],
    },
    "a1-demonstrative-consolidation": {
        "a1.dem.cons.ex01": ["este-esta", "articles"],
        "a1.dem.cons.ex02": ["ese-esa", "present-tense"],
        "a1.dem.cons.ex03": ["aquel-aquella", "ser"],
        "a1.dem.cons.ex06": ["neutro-esto-eso", "hay"],
        "a1.dem.cons.ex09": ["pronombres-demostrativos", "present-tense"],
        "a1.dem.cons.ex12": ["este-esta", "articles"],
    },
    "a1-doler-consolidation": {
        "a1.dol.cons.ex01": ["me-duele", "body-parts"],
        "a1.dol.cons.ex02": ["pronombres-doler", "body-parts"],
        "a1.dol.cons.ex03": ["doler-vs-tener", "tener-expressions"],
        "a1.dol.cons.ex07": ["farmacia-remedios", "present-tense"],
        "a1.dol.cons.ex10": ["intensidad-sensaciones", "ser"],
        "a1.dol.cons.ex11": ["me-duele", "negation"],
    },
    "a1-reflexive-consolidation": {
        "a1.refl.cons.ex01": ["pronombres-reflexivos", "present-tense"],
        "a1.refl.cons.ex02": ["vestirse-ponerse", "present-tense"],
        "a1.refl.cons.ex03": ["cambio-radical-reflexivos", "tener-expressions"],
        "a1.refl.cons.ex06": ["secuencia-rutina", "ser"],
        "a1.refl.cons.ex09": ["contraste-reflexivo", "present-tense"],
        "a1.refl.cons.ex11": ["pronombres-reflexivos", "negation"],
    },
}


def fix_gustar():
    path = EX_DIR / "a1-gustar-consolidation-ex.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    for ex in data["exercises"]:
        if ex["id"] in GUSTAR_RETAG:
            ex["teaches"] = GUSTAR_RETAG[ex["id"]]
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    tags = set()
    for ex in data["exercises"]:
        tags.update(ex.get("teaches", []))
    print(f"  FIX  a1-gustar-consolidation -- retagged, now {len(tags)} distinct teaches tags: {sorted(tags)}")


def fix_crossover(lesson_key, ex_tags):
    path = EX_DIR / (lesson_key + "-ex.json")
    data = json.loads(path.read_text(encoding="utf-8"))
    changed = 0
    for ex in data["exercises"]:
        if ex["id"] in ex_tags:
            new_tags = ex_tags[ex["id"]]
            # Merge: keep existing, add new
            merged = list(dict.fromkeys(ex.get("teaches", []) + new_tags))
            if merged != ex.get("teaches", []):
                ex["teaches"] = merged
                changed += 1
    if changed:
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    tags = set()
    for ex in data["exercises"]:
        tags.update(ex.get("teaches", []))
    print(f"  FIX  {lesson_key} -- {changed} exercises retagged, now {len(tags)} distinct teaches tags")


def main():
    fix_gustar()
    for lesson_key, ex_tags in CROSSOVER_TAGS.items():
        fix_crossover(lesson_key, ex_tags)


if __name__ == "__main__":
    main()
