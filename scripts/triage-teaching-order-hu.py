#!/usr/bin/env python3
"""Same triage as scripts/triage-teaching-order.py, for audit-lesson-hu.py's
output. Turns out HU has the same noise sources as Spanish: multiple-choice
distractors mixing in English words (e.g. a1-155-introduce-2's options are
["paprika", "chocolate", "tea"] for a Hungarian-only question -- "chocolate"
and "tea" are English decoys, not Hungarian the learner needs), the same
pattern in dialogue-complete exercises' wrong options (e.g. a1-11-dialogue-1's
unselected "Én itt lakom."), and a whole exercise shape unique to HU: "What
does 'X' mean?" comprehension checks, where every option is deliberately
English (testing recognition, not testing Hungarian). Read-only, doesn't
touch content.

    python scripts/triage-teaching-order-hu.py            # summary + samples
    python scripts/triage-teaching-order-hu.py --all      # list every flag
"""

import importlib.util
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
_spec = importlib.util.spec_from_file_location("audit_lesson_hu", ROOT / "scripts" / "audit-lesson-hu.py")
al = importlib.util.module_from_spec(_spec)
sys.modules["audit_lesson_hu"] = al
_spec.loader.exec_module(al)

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ENGLISH_HINT = re.compile(r"\(([^)]+)\)")
ENGLISH_WORD = re.compile(r"[a-z]+")


def is_meaning_check(ex):
    """'What does X mean?' comprehension checks (and the variant that quotes
    a whole Hungarian sentence then asks 'What does this describe?') are
    entirely English options by design -- testing recognition of meaning,
    not testing Hungarian. Deliberately narrow (startswith, or the quoted-
    sentence dash-prefixed variant) rather than "contains 'What does'
    anywhere": a1-160-consolidation-6's question is "How do you ask 'What
    does this word mean?'" but its OPTIONS are real Hungarian phrases
    (testing how to phrase the question, not what a word means) -- a loose
    substring check would have wrongly swallowed a real content check."""
    q = ex.get("question", "")
    if ex.get("type") != "multiple-choice":
        return False
    return q.startswith("What does") or "— What does" in q or "-- What does" in q


def english_text(ex):
    parts = []
    if ex.get("type") == "multiple-choice" and "question" in ex:
        parts.append(ex["question"])
    if is_meaning_check(ex):
        parts += ex.get("options", [])
    for field in ("sentence", "question"):
        if field in ex:
            parts += ENGLISH_HINT.findall(ex[field])
    # A "(...)" gloss can sit inside an option string too, not just
    # sentence/question -- e.g. "Virágcsokor (flower bouquet)" (found
    # 2026-09-17, a2-184-controlled-4). Only pull the parenthetical part,
    # not the whole option -- the Hungarian word before it still needs to
    # be checked normally, just not the English translation next to it.
    for o in ex.get("options", []):
        if isinstance(o, str):
            parts += ENGLISH_HINT.findall(o)
    return " ".join(parts)


def correct_option_text(ex):
    # dialogue-complete exercises have the same options[]/correct shape as
    # multiple-choice (found 2026-09-17: a1-11-dialogue-1/2's wrong option
    # "Én itt lakom."/"Hol laksz?" was flagging as a real gap because this
    # check was multiple-choice-only) -- keyed on the fields actually being
    # present, not the type name, so any future exercise type with the same
    # shape is covered automatically.
    if "correct" in ex and "options" in ex:
        try:
            return ex["options"][ex["correct"]]
        except (IndexError, TypeError):
            return ""
    return ""


def classify_token(ex, token):
    if token in al.hu_tokens(english_text(ex)):
        return "english-leak"
    if "correct" in ex and "options" in ex:
        correct_tokens = al.hu_tokens(correct_option_text(ex))
        all_tokens = set()
        for o in ex.get("options", []):
            all_tokens |= al.hu_tokens(o)
        if token in all_tokens and token not in correct_tokens:
            return "wrong-distractor-or-english-option"
    return "real-gap-candidate"


def verdict(kinds):
    if "real-gap-candidate" in kinds:
        return "real-gap-candidate"
    if "wrong-distractor-or-english-option" in kinds:
        return "wrong-distractor-or-english-option"
    return "english-leak"


def triage_level(level):
    known = al.KnownWords()
    for earlier in al.LEVELS[:al.LEVELS.index(level)]:
        known.update(al.accumulate_known(earlier))

    results = []
    for unit in al.load_units(level):
        for l in unit["lessons"]:
            if l["id"].endswith("-consolidation"):
                continue
            path = al.lesson_path(level, l["id"])
            if not path.exists():
                continue
            lesson = al.read(path)
            all_ex = al.load_exercises(lesson)
            for label, introduced, required in al.teach_tokens(lesson, all_ex):
                if label is None:
                    known.update(introduced)
                    continue
                unseen = sorted(t for t in required if not known.covers(t))
                if unseen:
                    eid = label.split(" / ")[-1]
                    ex = all_ex.get(eid, {})
                    kinds = {classify_token(ex, t) for t in unseen}
                    results.append((l["id"], label, unseen, verdict(kinds)))
                known.update(required)
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

    by_level = Counter((r[0].split(".")[1], r[3]) for r in all_results)
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
