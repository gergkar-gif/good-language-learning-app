#!/usr/bin/env python3
"""
fix_consolidation_shape.py
--------------------------
Fixes the 20 A1 Spanish consolidation lessons that fail audit-lesson.py's
'single' shape check.

Every failing lesson has the same three problems:
  1. Multiple exercise-group sections ("Practice", "Dialogue", "Writing")
     instead of one group titled exactly "Review".
  2. An "srs" section (consolidation lessons have no new words — the srs
     block will always be empty and produces a spurious audit failure).
  3. goal/checklist items that don't begin "I can" (they say "Review X"
     or "Use X" without the first-person framing).

The exercise content itself is untouched — all exerciseRefs from all
groups are merged into one "Review" group (they always all share the same
ref JSON file, so this is safe).

Usage:
    python scripts/fix_consolidation_shape.py [--dry-run]
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
LESSONS_DIR = ROOT / "content" / "es" / "lessons" / "a1"

# The 20 lessons that fail (confirmed by audit-lesson.py output).
# a1-01 through a1-10 pass, plus a1-03c and a1-04. The rest fail.
FAILING = [
    "a1-05-consolidation.json",
    "a1-06-consolidation.json",
    "a1-07-consolidation.json",
    "a1-08-consolidation.json",
    "a1-12-consolidation.json",
    "a1-20-consolidation.json",
    "a1-abilities-consolidation.json",
    "a1-cafe-consolidation.json",
    "a1-continuous-consolidation.json",
    "a1-demonstrative-consolidation.json",
    "a1-directions-consolidation.json",
    "a1-doler-consolidation.json",
    "a1-future-consolidation.json",
    "a1-gustar-consolidation.json",
    "a1-health-consolidation.json",
    "a1-hobbies-consolidation.json",
    "a1-kitchen-consolidation.json",
    "a1-reflexive-consolidation.json",
    "a1-weather-consolidation.json",
    "a1-work-consolidation.json",
]

# Rewrites for goal/checklist items that don't start with "I can".
# Key: exact current text. Value: replacement text starting with "I can".
ITEM_REWRITES = {
    # a1-06-consolidation
    "Review regular present tense, ser, tener and earlier vocabulary.":
        "I can use regular present tense, ser, and tener with earlier A1 vocabulary.",
    "Use earlier A1 language to talk about a daily routine.":
        "I can combine earlier A1 language to talk about a daily routine.",
    # a1-07-consolidation
    "Review hay, estar, articles and home vocabulary.":
        "I can use hay, estar, and articles to describe a home.",
    "Use earlier A1 language to describe a home and locate people and things.":
        "I can combine earlier A1 language to locate people and things at home.",
    # a1-08-consolidation
    "Review numbers, prices, shopping vocabulary and earlier A1 language.":
        "I can use numbers, prices, and shopping vocabulary from earlier A1.",
    "Use cumulative A1 language to handle a simple shopping interaction.":
        "I can handle a simple shopping interaction using cumulative A1 language.",
    # a1-12-consolidation
    "Review food, meals and eating-out vocabulary and grammar.":
        "I can use food, meal, and eating-out vocabulary and grammar.",
    "Use cumulative A1 language to order food and describe a meal.":
        "I can order food and describe a meal using cumulative A1 language.",
    # a1-20-consolidation
    "Review body, health, doler, estar and advice structures.":
        "I can use body, health, doler, estar, and advice structures.",
    "Use cumulative A1 language to describe a health problem and give advice.":
        "I can describe a health problem and give simple advice using cumulative A1.",
    # a1-abilities-consolidation (goal items — checklist already has "I can")
    "Review poder vs. saber for abilities and opportunities.":
        "I can use poder vs. saber to talk about abilities and opportunities.",
    "Consolidate saber vs. conocer for facts vs. people and places.":
        "I can distinguish saber vs. conocer for facts vs. people and places.",
    "Master the personal 'a' with human direct objects.":
        "I can use the personal 'a' with human direct objects.",
    # a1-cafe-consolidation
    "Review café vocabulary, ordering food and drink, and earlier A1 language.":
        "I can use café vocabulary and order food and drink with earlier A1 language.",
    "Use cumulative A1 language to handle a café interaction from start to finish.":
        "I can handle a café interaction from start to finish using cumulative A1.",
    # a1-continuous-consolidation
    "Review estar + gerund and contrast with simple present.":
        "I can use estar + gerund and contrast it with the simple present.",
    "Use cumulative A1 language to describe what is happening right now.":
        "I can describe what is happening right now using cumulative A1 language.",
    # a1-demonstrative-consolidation
    "Review este, ese, aquel and neuter forms esto, eso, aquello.":
        "I can use este, ese, aquel, and the neuter forms esto, eso, aquello.",
    "Use demonstratives accurately to point to people and things near and far.":
        "I can use demonstratives accurately to point to people and things near and far.",
    # a1-directions-consolidation
    "Review directions, town vocabulary, hay, estar and earlier A1 language.":
        "I can use directions, town vocabulary, hay, and estar with earlier A1 language.",
    "Use cumulative A1 language to give a simple route around town.":
        "I can give a simple route around town using cumulative A1 language.",
    # a1-doler-consolidation
    "Review doler, body parts, health complaints and advice structures.":
        "I can use doler, body parts, and health complaint and advice structures.",
    "Describe a health problem and give basic advice using cumulative A1 language.":
        "I can describe a health problem and give basic advice using cumulative A1.",
    # a1-future-consolidation
    "Review ir a + infinitive, tener que, time expressions and cumulative A1 language.":
        "I can use ir a + infinitive and tener que with time expressions.",
    "Use cumulative A1 language to describe an upcoming plan and its obligations.":
        "I can describe an upcoming plan and its obligations using cumulative A1.",
    # a1-gustar-consolidation
    "Review gustar-type verbs, hobbies and free-time vocabulary.":
        "I can use gustar-type verbs to talk about hobbies and free-time activities.",
    "Use cumulative A1 language to describe likes, dislikes and preferences.":
        "I can describe likes, dislikes, and preferences using cumulative A1 language.",
    # a1-health-consolidation
    "Review health vocabulary, tener expressions, questions, commands and earlier A1 language.":
        "I can use health vocabulary, tener expressions, questions, and commands.",
    "Use cumulative A1 language to describe a simple health problem and give basic advice.":
        "I can describe a simple health problem and give basic advice using cumulative A1.",
    # a1-hobbies-consolidation
    "Review hobbies, present tense, questions, time expressions and broad A1 language.":
        "I can use hobby vocabulary, present tense, questions, and time expressions.",
    "Use cumulative A1 language to describe a simple week of free-time activities.":
        "I can describe a simple week of free-time activities using cumulative A1.",
    # a1-kitchen-consolidation
    "Review kitchen vocabulary, regular verbs, imperatives and earlier A1 language.":
        "I can use kitchen vocabulary, regular verbs, and imperatives from earlier A1.",
    "Use cumulative A1 language to describe a kitchen and follow simple instructions.":
        "I can describe a kitchen and follow simple instructions using cumulative A1.",
    # a1-reflexive-consolidation
    "Review reflexive verbs for daily routine and personal care.":
        "I can use reflexive verbs to describe a daily routine and personal care.",
    "Use cumulative A1 language to describe a morning or evening routine.":
        "I can describe a morning or evening routine using cumulative A1 language.",
    # a1-weather-consolidation
    "Review weather, present tense, time expressions and earlier A1 language.":
        "I can use weather vocabulary, present tense, and time expressions.",
    "Use cumulative A1 language to describe weather and activities across a simple day or week.":
        "I can describe weather and activities across a simple day or week using cumulative A1.",
    # a1-work-consolidation
    "Review work, tener que, hay que, present tense and cumulative A1 language.":
        "I can use work vocabulary, tener que, hay que, and present tense together.",
    "Use cumulative A1 language to describe a simple working day and its obligations.":
        "I can describe a simple working day and its obligations using cumulative A1.",
    # a1-05-consolidation (goals already have "I can" — checklist matches)
    # (no rewrites needed for a1-05)
}


def rewrite_items(items):
    """Apply ITEM_REWRITES to a list of goal/checklist strings."""
    return [ITEM_REWRITES.get(item, item) for item in items]


def fix_lesson(path, dry_run=False):
    text = path.read_text(encoding="utf-8")
    data = json.loads(text)
    sections = data.get("sections", [])

    # Collect all exercise-group sections and their refs
    exercise_groups = [s for s in sections if s.get("type") == "exercise-group"]
    non_exercise = [s for s in sections if s.get("type") not in ("exercise-group", "srs")]

    if not exercise_groups:
        print(f"  SKIP {path.name} — no exercise-group sections found")
        return False

    # Check if already has a single "Review" group
    if len(exercise_groups) == 1 and exercise_groups[0].get("title") == "Review":
        print(f"  OK   {path.name} — already has single 'Review' group")
        return False

    # All groups must share the same ref (they always do for consolidation lessons)
    refs = {g.get("ref") for g in exercise_groups}
    if len(refs) > 1:
        print(f"  WARN {path.name} — multiple different refs, skipping: {refs}")
        return False

    shared_ref = refs.pop()

    # Merge all exerciseRefs into one list
    all_refs = []
    for g in exercise_groups:
        all_refs.extend(g.get("exerciseRefs", []))

    merged_group = {
        "type": "exercise-group",
        "title": "Review",
        "ref": shared_ref,
        "exerciseRefs": all_refs,
    }

    # Rebuild sections: goal → recycle → Review → checklist
    # (preserve any other non-exercise, non-srs sections in order)
    new_sections = []
    for s in non_exercise:
        if s["type"] == "goal":
            s = dict(s)
            s["items"] = rewrite_items(s.get("items", []))
        elif s["type"] == "checklist":
            s = dict(s)
            s["items"] = rewrite_items(s.get("items", []))
        new_sections.append(s)
        if s["type"] == "recycle":
            # Insert the merged Review group right after recycle
            new_sections.append(merged_group)

    # If there was no recycle section (shouldn't happen, but be safe)
    if merged_group not in new_sections:
        # Insert before checklist
        idx = next((i for i, s in enumerate(new_sections) if s["type"] == "checklist"), len(new_sections))
        new_sections.insert(idx, merged_group)

    data["sections"] = new_sections

    # Serialise preserving the original indentation style (2-space)
    new_text = json.dumps(data, ensure_ascii=False, indent=2) + "\n"

    if dry_run:
        print(f"  DRY  {path.name} -- would merge {len(exercise_groups)} groups -> 1 'Review' group")
        return True

    path.write_text(new_text, encoding="utf-8")
    print(f"  FIX  {path.name} -- merged {len(exercise_groups)} groups -> 1 'Review' group, removed srs")
    return True


def main():
    dry_run = "--dry-run" in sys.argv
    if dry_run:
        print("DRY RUN — no files will be modified\n")

    changed = 0
    for name in FAILING:
        path = LESSONS_DIR / name
        if not path.exists():
            print(f"  MISS {name} — file not found")
            continue
        if fix_lesson(path, dry_run=dry_run):
            changed += 1

    print(f"\n{'Would change' if dry_run else 'Changed'} {changed}/{len(FAILING)} lessons.")


if __name__ == "__main__":
    main()
