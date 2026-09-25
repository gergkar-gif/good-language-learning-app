#!/usr/bin/env python3
"""Backfill Hungarian exercise `category` -> `category` (6 standard values) + `stage`.

For each Hungarian exercise whose `category` is not one of the six canonical values
(`vocabulary`, `grammar`, `reading`, `dialogue`, `writing`, `listening`):
- Moves the old `category` value to `stage` (preserving lesson stages and content domains
  like `civics`, `citizenship`, `history`, `literature`, `law`, `culture`, `geography`).
- Derives the new `category` from most to least certain:
  1. Direct stage mapping (`production`/`produce` -> `writing`)
  2. Exercise `type` (`matching` -> `vocabulary`, `listening-choice`/`dictation` -> `listening`,
     `dialogue-complete` -> `dialogue`, `structured-writing` -> `writing`)
  3. Existing `teaches` slugs (grammar slugs -> `grammar`, vocabulary theme slugs -> `vocabulary`,
     communicative slugs -> `dialogue`/`writing`)
  4. Lesson/question structure analysis for exercises without `teaches` (or prints unresolved
     items for review when `--strict` is used).

Usage:
    python scripts/backfill_hu_stage.py --dry-run
    python scripts/backfill_hu_stage.py --write
"""

import argparse
import json
import random
import re
import sys
from collections import Counter
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parent.parent
ALLOWED_CATEGORIES = {"vocabulary", "grammar", "reading", "dialogue", "writing", "listening"}

GRAMMAR_SLUG_KEYWORDS = (
    "alphabet", "vowel", "harmony", "consonant", "conjugat", "definite", "indefinite",
    "tense", "past", "present", "future", "conditional", "imperative", "subjunctive",
    "possessiv", "plural", "accusative", "dative", "inessive", "illative", "elative",
    "superessive", "sublative", "delative", "adessive", "allative", "ablative",
    "instrumental", "causal", "translative", "terminative", "essive", "locative",
    "case", "suffix", "prefix", "preverb", "coverb", "postposition", "article",
    "pronoun", "relative", "demonstrative", "interrogative", "reflexive", "reciprocal",
    "comparative", "superlative", "comparison", "negat", "word-order", "focus",
    "modal", "infinitive", "participle", "gerund", "causative", "potential",
    "passive", "reported", "indirect", "clause", "concord", "agreement", "number",
    "van", "nincs", "kell", "lehet", "szabad", "tilos", "ik-verb", "ige", "rag",
    "kepzo", "jel", "birtok", "nevmas", "fokozas", "hataroz", "kotojel", "kotes",
    "tudas", "szokott", "tetszik", "faj", "kerul", "adjectiv", "adverb",
    "numeral", "ordinal", "fraction", "date-format", "time-expr", "question-word",
    "linking-verb", "copula", "zero-copula", "assimilation", "val-vel", "ban-ben",
    "ba-be", "bol-bol", "on-en-on", "ra-re", "rol-rol", "nal-nel", "hoz-hez-hoz",
    "tol-tol", "nak-nek", "ig", "kent", "ert", "ul-ul", "va-ve", "hat-het",
    "tat-tet", "ando-endo", "ott-ett", "t-past", "na-ne", "ja-je", "juk-juk",
    "lak-lek", "ok-ek-ok", "sz-el", "unk-unk", "tok-tek-tok", "nak-nek",
)

VOCAB_SLUG_KEYWORDS = (
    "vocab", "words", "lexic", "theme", "greeting", "food", "drink", "family",
    "travel", "transport", "city", "town", "home", "house", "housing", "room",
    "furniture", "shopping", "market", "price", "money", "cloth", "weather",
    "season", "nature", "animal", "body", "health", "doctor", "illness",
    "work", "job", "profession", "office", "study", "school", "education",
    "hobby", "sport", "leisure", "music", "art", "media", "technology",
    "holiday", "celebration", "tradition", "history", "civics", "citizenship",
    "geography", "culture", "literature", "law", "state", "constitution",
    "symbol", "anthem", "king", "revolution", "hungaricum", "parliament",
    "rights", "election", "court", "eu", "heritage", "country", "nationality",
    "language", "color", "colour", "day", "month", "time", "number", "direction",
    "restaurant", "cafe", "hotel", "station", "airport", "post", "bank",
    "emotion", "feeling", "character", "appearance", "routine", "daily",
)


def load_grammar_known_slugs():
    known = set()
    gt_path = ROOT / "content/hu/indexes/grammar-titles.json"
    if gt_path.is_file():
        known.update(json.loads(gt_path.read_text(encoding="utf-8")).keys())

    gi_path = ROOT / "content/hu/indexes/grammar-index.json"
    if gi_path.is_file():
        known.update(json.loads(gi_path.read_text(encoding="utf-8")).get("bySkill", {}).keys())

    for gf in (ROOT / "content/hu/grammar").rglob("*.json"):
        try:
            gd = json.loads(gf.read_text(encoding="utf-8"))
            gid = gd.get("id", "")
            if gid:
                known.add(gid.split(".")[-1])
        except Exception:
            pass
    return known


def classify_slug(slug, known_grammar_slugs):
    if slug in known_grammar_slugs:
        return "grammar"
    if any(k in slug for k in GRAMMAR_SLUG_KEYWORDS):
        return "grammar"
    if any(k in slug for k in VOCAB_SLUG_KEYWORDS):
        return "vocabulary"
    return "grammar"


def derive_category(ex, known_grammar_slugs):
    old_cat = ex.get("category", "")
    ex_type = ex.get("type", "")
    teaches = ex.get("teaches") or []

    # Rule 1: direct stage mapping
    if old_cat == "dialogue":
        return "dialogue", "rule1_direct_stage"
    if old_cat in ("writing", "production", "produce"):
        return "writing", "rule1_direct_stage"
    if old_cat == "reading":
        return "reading", "rule1_direct_stage"
    if old_cat == "listening":
        return "listening", "rule1_direct_stage"

    # Rule 2: exercise type
    if ex_type == "matching":
        return "vocabulary", "rule2_exercise_type"
    if ex_type in ("listening-choice", "dictation"):
        return "listening", "rule2_exercise_type"
    if ex_type == "dialogue-complete":
        return "dialogue", "rule2_exercise_type"
    if ex_type == "structured-writing":
        return "writing", "rule2_exercise_type"

    # Rule 3: existing teaches slugs
    if teaches:
        slug_kinds = [classify_slug(s, known_grammar_slugs) for s in teaches if isinstance(s, str)]
        if "grammar" in slug_kinds:
            return "grammar", "rule3_teaches_grammar"
        if "vocabulary" in slug_kinds:
            return "vocabulary", "rule3_teaches_vocabulary"

    # Rule 4: deterministic analysis of exercise structure/prompt when teaches is absent
    if ex_type in ("sentence-builder", "sentence-order", "substitution", "error-correction"):
        return "grammar", "rule4_structure_grammar"

    q = (ex.get("question") or "").strip()
    s = (ex.get("sentence") or "").strip()

    # Conversational exchange prompt (e.g. "Complete: Szia! -> ____.")
    if "→" in q and any(g in q.lower() for g in ("szia", "jó napot", "jó estét", "köszönöm", "viszlát", "hogy vagy")):
        return "dialogue", "rule4_exchange_dialogue"

    if ex_type == "fill-blank":
        # Check if parenthetical hint or blank targets a grammatical suffix/case/conjugation
        gram_hints = (
            "accusative", "dative", "plural", "possessive", "subjunctive", "conditional",
            "imperative", "past", "definite", "indefinite", "suffix", "case", "conjugat",
            "concentrate", "develop", "through the", "as far as", "towards", "in the",
            "on the", "to the", "from the", "with", "must", "can", "would",
        )
        if re.search(r"[a-záéíóöőúüű]____", s, re.IGNORECASE) or any(h in s.lower() for h in gram_hints):
            return "grammar", "rule4_fillblank_grammar"
        if old_cat in ("civics", "citizenship", "history", "literature", "law", "culture", "geography"):
            return "vocabulary", "rule4_domain_vocabulary"
        return "grammar", "rule4_fillblank_grammar"

    if ex_type == "multiple-choice":
        q_lower = q.lower()
        # Explicit grammar questions
        if any(
            kw in q_lower
            for kw in (
                "which suffix", "which postposition", "which case", "which form",
                "which ending", "which prefix", "which pronoun", "which noun phrase expresses generic",
                "complete:", "how do you say \"", "how do you say '",
            )
        ) or "____" in q:
            return "grammar", "rule4_mc_grammar"

        # Lexical / terminology / civic-historical concept questions
        if any(
            kw in q_lower
            for kw in (
                "which means", "which word means", "what does", "which phrase means",
                "which can mean", "which asks", "mit jelent", "where does one",
                "what is the highest",
            )
        ) or old_cat in ("civics", "citizenship", "history", "literature", "law", "culture", "geography", "review", "in-context", "recall", "recognize", "consolidation"):
            return "vocabulary", "rule4_mc_vocabulary"

    return None, "unresolved"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()

    known_grammar_slugs = load_grammar_known_slugs()
    rule_counts = Counter()
    unresolved_items = []
    samples = []
    files_modified = 0

    for path in sorted((ROOT / "content/hu/exercises").glob("*/*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        changed = False
        for ex in data.get("exercises", []):
            old_cat = ex.get("category")
            if old_cat in ALLOWED_CATEGORIES:
                continue

            new_cat, rule = derive_category(ex, known_grammar_slugs)
            rule_counts[rule] += 1

            if new_cat is None:
                unresolved_items.append((path.relative_to(ROOT).as_posix(), ex.get("id"), old_cat, ex.get("type"), ex.get("question") or ex.get("sentence") or ex.get("english") or ""))
                continue

            samples.append({
                "file": path.relative_to(ROOT).as_posix(),
                "id": ex.get("id"),
                "type": ex.get("type"),
                "old_category": old_cat,
                "new_category": new_cat,
                "new_stage": old_cat,
                "teaches": ex.get("teaches"),
                "rule": rule,
            })

            ex["stage"] = old_cat
            ex["category"] = new_cat
            changed = True

        if changed and args.write:
            with open(path, "w", encoding="utf-8", newline="\n") as f:
                f.write(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
            files_modified += 1

    print("=== Hungarian Category -> Category + Stage Summary ===")
    for rule, count in rule_counts.most_common():
        print(f"  {rule:<28}: {count:,}")
    print(f"  Total processed             : {sum(rule_counts.values()):,}")
    print(f"  Unresolved                  : {len(unresolved_items):,}")
    if args.write:
        print(f"  Files written               : {files_modified:,}")

    rng = random.Random(42)
    picked = rng.sample(samples, min(20, len(samples)))
    print("\n=== 20 Random Before/After Samples ===")
    for s in picked:
        print(
            f"  [{s['file']} :: {s['id']}] type={s['type']} teaches={s['teaches']} "
            f"| category: '{s['old_category']}' -> '{s['new_category']}', stage: '{s['new_stage']}' ({s['rule']})"
        )

    if unresolved_items:
        print(f"\n=== Unresolved Items ({len(unresolved_items)}) ===")
        by_file = Counter(item[0] for item in unresolved_items)
        for fp, c in by_file.most_common(30):
            print(f"  {fp}: {c} unresolved exercises")
        print("  Sample unresolved items:")
        for item in unresolved_items[:15]:
            print(f"    {item[0]} :: {item[1]} (old_cat={item[2]}, type={item[3]}) -> {item[4][:80]}")


if __name__ == "__main__":
    main()
