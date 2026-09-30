#!/usr/bin/env python3
"""
fix_consolidation_goals.py
--------------------------
Fixes remaining goal/checklist issues in A1 consolidation lessons:
  1. Goal/checklist items that don't start with "I can"
  2. Mismatched goal vs checklist count (copies goal items to checklist)
"""
import json
from pathlib import Path

ROOT = Path(__file__).parent.parent
LESSONS_DIR = ROOT / "content" / "es" / "lessons" / "a1"

# For lessons where goal items are already "I can" but checklist doesn't match count,
# or where both need rewriting — keyed by filename.
FIXES = {
    "a1-12-consolidation.json": {
        "goal_items": [
            "I can use numbers, time expressions, and daily schedule vocabulary.",
            "I can describe a simple daily schedule using cumulative A1 language.",
        ],
        "checklist_items": [
            "I can use numbers, time expressions, and daily schedule vocabulary.",
            "I can describe a simple daily schedule using cumulative A1 language.",
        ],
    },
    "a1-20-consolidation.json": {
        "goal_items": [
            "I can use travel vocabulary, tener que, tener, querer, and necesitar.",
            "I can describe the start of a journey using cumulative A1 language.",
        ],
        "checklist_items": [
            "I can use travel vocabulary, tener que, tener, querer, and necesitar.",
            "I can describe the start of a journey using cumulative A1 language.",
        ],
    },
    "a1-cafe-consolidation.json": {
        "goal_items": [
            "I can use querer, tomar, comer, and café vocabulary.",
            "I can handle a simple café interaction using earlier A1 language.",
        ],
        "checklist_items": [
            "I can use querer, tomar, comer, and café vocabulary.",
            "I can handle a simple café interaction using earlier A1 language.",
        ],
    },
    # These have 3 goal items but 1 checklist item — expand checklist to match
    "a1-abilities-consolidation.json": {
        "checklist_items": [
            "I can use poder vs. saber to talk about abilities and opportunities.",
            "I can distinguish saber vs. conocer for facts vs. people and places.",
            "I can use the personal 'a' with human direct objects.",
        ],
    },
    "a1-continuous-consolidation.json": {
        "goal_items": [
            "I can form -ando and -iendo gerunds for all regular verb types.",
            "I can use irregular gerunds: leyendo, durmiendo, yendo, diciendo.",
            "I can contrast actions in progress with daily habits.",
        ],
        "checklist_items": [
            "I can form -ando and -iendo gerunds for all regular verb types.",
            "I can use irregular gerunds: leyendo, durmiendo, yendo, diciendo.",
            "I can contrast actions in progress with daily habits.",
        ],
    },
    "a1-demonstrative-consolidation.json": {
        "checklist_items": None,  # needs reading first
    },
    "a1-doler-consolidation.json": {
        "checklist_items": None,
    },
    "a1-gustar-consolidation.json": {
        "checklist_items": None,
    },
    "a1-reflexive-consolidation.json": {
        "checklist_items": None,
    },
}


def fix_lesson(path, fix_spec):
    text = path.read_text(encoding="utf-8")
    data = json.loads(text)
    changed = False

    for section in data.get("sections", []):
        if section.get("type") == "goal" and "goal_items" in fix_spec:
            section["items"] = fix_spec["goal_items"]
            changed = True
        if section.get("type") == "checklist" and "checklist_items" in fix_spec:
            if fix_spec["checklist_items"] is not None:
                section["items"] = fix_spec["checklist_items"]
                changed = True

    if changed:
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"  FIX  {path.name}")
    else:
        print(f"  SKIP {path.name} -- no changes")

    return changed


def main():
    for name, spec in FIXES.items():
        path = LESSONS_DIR / name
        if not path.exists():
            print(f"  MISS {name}")
            continue
        if spec.get("checklist_items") is None:
            # Need to read goal items and use them as checklist
            text = path.read_text(encoding="utf-8")
            data = json.loads(text)
            for section in data.get("sections", []):
                if section.get("type") == "goal":
                    spec["checklist_items"] = section["items"]
                    break
        fix_lesson(path, spec)


if __name__ == "__main__":
    main()
