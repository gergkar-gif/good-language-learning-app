#!/usr/bin/env python3
"""Split audit-lesson.py's teaching-order flags into real gaps vs. noise.

audit-lesson.py's check_teaching_order() flags an exercise whenever it uses
a Spanish word/form that was never shown on the unit's grammar/vocabulary/
story screens. That check has no idea an exercise's own English gloss text
or a deliberately-wrong multiple-choice distractor isn't something the
learner needs to already know — so a chunk of its flags are noise, not
content gaps. This re-runs the same walk and buckets each flagged exercise:

  english-leak          every unseen token only appears in English text
                         embedded in the exercise (an "english" field, a
                         multiple-choice "question", or a "(...)" gloss)
  wrong-distractor-only  every unseen token only appears in an incorrect
                         multiple-choice option, never the correct one
  real-gap-candidate     at least one unseen token isn't explained by
                         either of the above — an actual candidate for
                         "this word/form was tested before it was taught"

    python scripts/triage-teaching-order.py            # summary + samples
    python scripts/triage-teaching-order.py --all      # list every flag

This doesn't fix anything or edit content — it's a lens on audit-lesson.py's
raw output so a real backfill pass can start from the ~86% that are likely
real instead of wading through all of it by hand.
"""

import importlib.util
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
_spec = importlib.util.spec_from_file_location("audit_lesson", ROOT / "scripts" / "audit-lesson.py")
al = importlib.util.module_from_spec(_spec)
sys.modules["audit_lesson"] = al
_spec.loader.exec_module(al)

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ENGLISH_HINT = re.compile(r"\(([^)]+)\)")


def english_text(ex):
    """Text fields in an exercise that are meant to be English, not Spanish."""
    parts = []
    if "english" in ex:
        parts.append(ex["english"])
    if ex.get("type") == "multiple-choice" and "question" in ex:
        parts.append(ex["question"])
    for field in ("sentence", "question"):
        if field in ex:
            parts += ENGLISH_HINT.findall(ex[field])
    return " ".join(parts)


def correct_option_text(ex):
    if ex.get("type") == "multiple-choice" and "correct" in ex and "options" in ex:
        try:
            return ex["options"][ex["correct"]]
        except (IndexError, TypeError):
            return ""
    return ""


def classify_token(ex, token):
    if token in al.spanish_tokens(english_text(ex)):
        return "english-leak"
    if ex.get("type") == "multiple-choice":
        correct_tokens = al.spanish_tokens(correct_option_text(ex))
        all_tokens = set()
        for o in ex.get("options", []):
            all_tokens |= al.spanish_tokens(o)
        if token in all_tokens and token not in correct_tokens:
            return "wrong-distractor-only"
    return "real-gap-candidate"


def verdict(kinds):
    if "real-gap-candidate" in kinds:
        return "real-gap-candidate"
    if "wrong-distractor-only" in kinds:
        return "wrong-distractor-only"
    return "english-leak"


def triage_level(level):
    numeric_units = sorted((u for u, parts in al.group_units(level)[0].items() if u.isdigit()), key=int)
    if not numeric_units:
        return []
    units, _ = al.group_units(level)
    known = set()
    prior = al.LEVELS[:al.LEVELS.index(level)] if level in al.LEVELS else ()
    for earlier in prior:
        known |= al.accumulate_known(earlier)

    results = []
    for unit in numeric_units:
        for part in units[unit]:
            if part == "consolidation":
                continue
            key = f"{level}-{unit}-{part}"
            path = al.ES / "lessons" / level / f"{key}.json"
            if not path.exists():
                continue
            lesson = al.read(path)
            all_ex = al.load_exercises(lesson)
            for label, introduced, required in al.teach_tokens(lesson, all_ex):
                if label is None:
                    known |= introduced
                    continue
                unseen = sorted(t for t in required
                                 if t not in known and not al.matches(t, " " + " ".join(known) + " "))
                if unseen:
                    eid = label.split(" / ")[-1]
                    ex = all_ex.get(eid, {})
                    kinds = {classify_token(ex, t) for t in unseen}
                    results.append((key, label, unseen, verdict(kinds)))
                known |= required
    return results


def main():
    show_all = "--all" in sys.argv[1:]
    all_results = []
    for level in al.LEVELS:
        all_results += triage_level(level)

    counts = Counter(r[3] for r in all_results)
    print(f"Total flagged exercises: {len(all_results)}")
    for bucket, n in counts.most_common():
        print(f"  {bucket}: {n} ({100 * n / len(all_results):.0f}%)")

    by_level = Counter((r[0].split("-")[0], r[3]) for r in all_results)
    print("\nBy level:")
    for lvl in al.LEVELS:
        row = {k[1]: v for k, v in by_level.items() if k[0] == lvl}
        print(f"  {lvl}: {row}")

    real = [r for r in all_results if r[3] == "real-gap-candidate"]
    print(f"\n--- real-gap-candidate flags ({'all' if show_all else 'first 30'}) ---")
    for key, label, unseen, _ in (real if show_all else real[:30]):
        print(f"  {key} {label} needs: {', '.join(unseen)}")
    if not show_all and len(real) > 30:
        print(f"  ... {len(real) - 30} more (rerun with --all)")


if __name__ == "__main__":
    main()
