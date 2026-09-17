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
# B1 content uses a completely different gloss convention than A1/A2's
# parens -- a full-sentence English translation in square brackets, e.g.
# "La pobreza puede aumentar debido al desempleo. [Poverty can increase due
# to unemployment.]" (found 2026-09-17, scoping ES B1: 204 files / 4,320
# instances of this pattern, the single largest source of B1's flags).
SQUARE_BRACKET_HINT = re.compile(r"\[([^\]]+)\]")
SPANISH_MARKER = re.compile(r"[áéíóúñ¿¡]")
SPANISH_ARTICLE = re.compile(r"^(el|la|los|las|un|una)\s")
# Short, accent-free Spanish sentences ("Era abogado.") don't trip either
# check above, so bracket_gloss() defaulted to guessing -- and guessed
# wrong more than half the time (found 2026-09-17, b1-06-05.ex09: "He was
# a copyist in a law office. [Era copista en una oficina de abogados.]"'s
# sibling options "He was a lawyer. [Era abogado.]" had no marker on
# either side, so the default silently kept the Spanish side and
# discarded the English "lawyer"/"manager" as if THEY were the gloss).
# These common function words settle most of the remaining ambiguous
# cases without needing accents.
SPANISH_WORDS = re.compile(
    r"\b(era|fue|son|es|hay|que|para|con|muy|pero|porque|cuando|donde|"
    r"como|si|no|se|su|sus|le|les|lo|los|las|del|al|más|también|puede|"
    r"debe|tiene|está|están|estaba|vamos|voy|va|un|una|unos|unas|"
    # present-perfect "haber" forms -- "he" deliberately excluded, see
    # ENGLISH_WORDS below (found 2026-09-17, b1-16-04.ex14: "han" was
    # missing, so an all-Spanish sentence with no accents scored 0 and the
    # English bracket never got excluded)
    r"has|ha|hemos|han)\b"
)
ENGLISH_WORDS = re.compile(
    # "he" deliberately excluded: it collides with Spanish "he" (the
    # present-perfect auxiliary, "he comido" = "I have eaten") badly
    # enough to actively misfire rather than just miss (found 2026-09-17,
    # b1-14-02.ex03 -- "he" sentence-initial in a present-perfect exercise
    # made an otherwise all-Spanish sentence outscore its own English
    # bracket, so bracket_gloss() kept the Spanish side and discarded it
    # as if it were the gloss). Better to stay silent on this signal than
    # be confidently wrong on an entire grammar topic's worth of exercises.
    r"\b(the|was|were|is|are|she|they|we|you|it|his|her|their|this|"
    r"that|with|for|because|when|where|how|if|not|can|could|would|"
    r"should|must|going|will)\b"
)


def spanish_score(text):
    t = text.lower()
    return len(SPANISH_MARKER.findall(t)) + len(SPANISH_WORDS.findall(t)) + (2 if SPANISH_ARTICLE.match(t) else 0)


def english_score(text):
    return len(ENGLISH_WORDS.findall(text.lower()))


def looks_spanish(text):
    t = text.lower()
    return bool(SPANISH_MARKER.search(t) or SPANISH_ARTICLE.match(t))


def bracket_gloss(text):
    """The non-Spanish side of a "main text [bracket]" pair. Normally the
    bracket holds the English gloss and the main text is Spanish, but 573
    of B1's ~3,200 bracket pairs have it backwards -- English main text,
    [Spanish] in the bracket (found 2026-09-17, e.g. "The consequence of
    trusting too easily. [La consecuencia de confiar demasiado.]").
    Whichever side scores more Spanish is the real content; the other side
    is the gloss to discard. Short, accent-free sentences ("Era abogado.")
    can score 0 on both sides -- found the same day, b1-06-05.ex09's
    sibling options had no signal either way, so the old two-branch
    version (spanish-or-not) silently defaulted to keeping the Spanish
    side and discarding "lawyer"/"manager" as if THEY were the gloss.
    When neither side scores, don't guess -- return nothing rather than
    risk picking the wrong one."""
    m = SQUARE_BRACKET_HINT.search(text)
    if not m:
        return ""
    inner = m.group(1)
    outer = (text[: m.start()] + text[m.end():]).strip()
    inner_es, outer_es = spanish_score(inner), spanish_score(outer)
    if inner_es > outer_es:
        return outer
    if outer_es > inner_es:
        return inner
    inner_en, outer_en = english_score(inner), english_score(outer)
    if outer_en > inner_en:
        return outer
    if inner_en > outer_en:
        return inner
    return ""


def is_meaning_check(ex):
    """'What does X mean?' comprehension checks are entirely English options
    by design (testing recognition of a Spanish word's meaning, not testing
    Spanish) -- ported from the same fix in triage-teaching-order-hu.py
    (found 2026-09-17), confirmed to also exist in ES content (31 such
    questions). Deliberately narrow (startswith, or the quoted-sentence
    dash-prefixed variant), not "contains 'What does' anywhere" -- see the
    HU version's docstring for why a loose substring check is unsafe."""
    q = ex.get("question", "")
    if ex.get("type") != "multiple-choice":
        return False
    return q.startswith("What does") or "— What does" in q or "-- What does" in q


def english_text(ex):
    """Text fields in an exercise that are meant to be English, not Spanish."""
    parts = []
    if "english" in ex:
        parts.append(ex["english"])
    if ex.get("type") == "multiple-choice" and "question" in ex:
        parts.append(ex["question"])
    if is_meaning_check(ex):
        parts += ex.get("options", [])
    for field in ("sentence", "question"):
        if field in ex:
            parts += ENGLISH_HINT.findall(ex[field])
            parts.append(bracket_gloss(ex[field]))
    # A "(...)" or "[...]" gloss can sit inside an option string too, not
    # just sentence/question -- ported from the same HU fix (found
    # 2026-09-17). Only pull the gloss part, not the whole option.
    for o in ex.get("options", []):
        if isinstance(o, str):
            parts += ENGLISH_HINT.findall(o)
            parts.append(bracket_gloss(o))
    # sentence-order's "sentences" list (used for non-reading-category
    # exercises, e.g. reordering opinion sentences) carries the same
    # bracket-gloss convention and was never scanned at all before this.
    for s in ex.get("sentences", []):
        if isinstance(s, str):
            parts.append(bracket_gloss(s))
    # sentence-builder tiles and structured-writing template answers can
    # carry a bracket gloss on the whole phrase too.
    for t in ex.get("tiles", []):
        if isinstance(t, str):
            parts.append(bracket_gloss(t))
    for line in ex.get("template", []):
        if isinstance(line, dict) and isinstance(line.get("answer"), str):
            parts.append(bracket_gloss(line["answer"]))
    # dialogue-complete prompt lines
    for line in ex.get("prompt", []):
        if isinstance(line, dict) and isinstance(line.get("text"), str):
            parts.append(bracket_gloss(line["text"]))
    # matching pairs are normally [spanish, english], but 4 exercises store
    # a handful of pairs backwards (found 2026-09-17, a1.10.01.ex13 /
    # a1.10.02.ex13 flagging "balloon"/"colour" as unrecognised Spanish).
    # Rather than assume an order, treat whichever side of a pair lacks any
    # Spanish-specific character as the gloss, regardless of position.
    if ex.get("type") == "matching":
        for pair in ex.get("pairs", []):
            if len(pair) != 2 or not all(isinstance(p, str) for p in pair):
                continue
            a, b = pair
            if looks_spanish(a) and not looks_spanish(b):
                parts.append(b)
            elif looks_spanish(b) and not looks_spanish(a):
                parts.append(a)
    return " ".join(parts)


def correct_option_text(ex):
    # dialogue-complete exercises have the same options[]/correct shape as
    # multiple-choice -- ported from the same HU fix (found 2026-09-17,
    # a1-11-dialogue-1/2's unselected wrong option flagging as a real gap).
    # ES has 1,528 dialogue-complete exercises with a "correct" field, far
    # more than HU had, so this fix matters more here. Keyed on the fields
    # actually being present, not the type name.
    if "correct" in ex and "options" in ex:
        try:
            return ex["options"][ex["correct"]]
        except (IndexError, TypeError):
            return ""
    return ""


def classify_token(ex, token):
    if token in al.spanish_tokens(english_text(ex)):
        return "english-leak"
    if "correct" in ex and "options" in ex:
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
