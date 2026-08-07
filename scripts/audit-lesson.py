#!/usr/bin/env python3
"""Check a lesson against the A1 content specification.

scripts/validate-content.py checks the shape of each file on its own. This
checks the rules that span files and that count things — the ones that
actually go wrong when authoring at volume, and the ones a lesson generator
has to satisfy. Rules come from content/es/guides/:

  a1-content-spec.md       exercise split, grammar limits, checklist form
  a1-vocabulary-themes.md  per-lesson new-word target (authoritative)
  a1-quality-checklist.md  every new word in the story and in an exercise

    python scripts/audit-lesson.py            # every A1 lesson that has content
    python scripts/audit-lesson.py a1-01      # one lesson

Exits non-zero if any checked lesson fails.
"""

import json
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ES = ROOT / "content" / "es"

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# Block -> exercise count. Totals 15.
EXERCISE_SPLIT = {"Practice": 6, "Reading": 4, "Dialogue": 3, "Writing": 2}
MIN_PRACTICE_TYPES = 5
GRAMMAR_MAX_WORDS = 300
GRAMMAR_EXAMPLES = (3, 5)
CHECKLIST_ITEMS = 4
CHECKLIST_PREFIX = "I can"

# From a1-vocabulary-themes.md, which that document declares authoritative.
NEW_WORDS = {1: 10, 2: 10, 3: 12, 4: 12, 5: 15, 6: 15, 7: 18, 8: 18, 9: 20,
             10: 20, 11: 20, 12: 20, 13: 20, 14: 20, 15: 20, 16: 20, 17: 20}

# Lessons 18-20 consolidate rather than teach: no new words, no new grammar,
# and a different shape entirely. Holding them to the teaching-lesson spec
# would report failures nobody can act on, so they are skipped until that
# format is designed.
REVIEW_LESSONS = {18, 19, 20}
TEACHING_LESSONS = [n for n in range(1, 21) if n not in REVIEW_LESSONS]

# From a1-content-spec.md section 3. Flat across A1 rather than escalating:
# the stories that exist run 106-225 words with no upward trend, and A1 texts
# stay short on purpose.
STORY_WORDS = (100, 250)


ARTICLE = re.compile(r"^(el|la|los|las|un|una|unos|unas) ")


def norm(text):
    text = unicodedata.normalize("NFD", str(text).lower())
    text = "".join(c for c in text if unicodedata.category(c) != "Mn")
    return re.sub(r"[^a-z0-9 ]", " ", text)


def searchable(lemma):
    """A noun is listed with its article ('el café') but the story says 'un
    café' or just 'café', so the article is dropped before matching."""
    return ARTICLE.sub("", norm(lemma).strip()).strip()


def matches(term, haystack):
    if not term:
        return False
    if term in haystack:
        return True
    if " " in term:
        return False
    # Nouns and adjectives agree in gender and number, so the listed form
    # ('chileno') rarely appears verbatim ('chilena', 'chilenas'). Compare
    # stems instead, with a length floor so short stems cannot match by luck.
    stem = re.sub(r"(es|os|as|s)$", "", term)
    stem = re.sub(r"[oae]$", "", stem)
    return len(stem) >= 4 and stem in haystack


def find_missing(words, haystack):
    """Split into hard misses and ones we cannot judge.

    Verbs are listed as infinitives but appear conjugated, and stem changes
    ('querer' -> 'quiero') defeat stem matching. Resolving those needs the
    morphology index in imports/dictionary, so rather than report a false
    failure an unmatched verb is returned separately for a human to confirm."""
    missing, unsure = [], []
    for w in words:
        if matches(searchable(w["lemma"]), haystack):
            continue
        (unsure if w.get("pos", "").startswith("verb") else missing).append(w["lemma"])
    return missing, unsure


def read(path):
    return json.loads(path.read_text(encoding="utf-8"))


def load_master():
    """The Overview table of guides/a1.md, which owns every lesson's title and
    communicative goal. Only the first numbered table is read — the file has
    others further down."""
    path = ES / "guides" / "a1.md"
    if not path.exists():
        return {}

    master, started = {}, False
    for line in path.read_text(encoding="utf-8").splitlines():
        row = re.match(r"^\|\s*(\d{1,2})\s*\|(.+)\|\s*$", line)
        if row:
            started = True
            cells = [c.strip() for c in row.group(2).split("|")]
            if len(cells) >= 3:
                master.setdefault(int(row.group(1)), {
                    "title": cells[0], "goal": cells[1], "grammar": cells[2]
                })
        elif started and line.startswith("#"):
            break
    return master


MASTER = load_master()


class Report:
    def __init__(self, name):
        self.name = name
        self.failures = []
        self.warnings = []
        self.checked = 0

    def rule(self, ok, label, detail=""):
        self.checked += 1
        if not ok:
            self.failures.append(f"{label}" + (f" — {detail}" if detail else ""))

    def warn(self, label, detail=""):
        self.warnings.append(f"{label}" + (f" — {detail}" if detail else ""))


def audit(key):
    """key is like 'a1-01'. Returns None for a lesson with no file, and the
    string 'review' for a consolidation lesson that this spec does not cover."""
    number = int(key.split("-")[1])
    if number in REVIEW_LESSONS:
        return "review"
    r = Report(key)

    lesson_path = ES / "lessons" / "a1" / f"{key}.json"
    if not lesson_path.exists():
        return None
    lesson = read(lesson_path)

    # --- agrees with the master curriculum -------------------------------
    # guides/a1.md owns title and goal. They drifted once, silently, because
    # nothing compared them; this is what stops that happening again.
    row = MASTER.get(number)
    if row:
        r.rule(lesson.get("title") == row["title"], "title matches guides/a1.md",
               f'file "{lesson.get("title")}" vs master "{row["title"]}"')
        r.rule(lesson.get("goal") == row["goal"], "goal matches guides/a1.md",
               f'file "{lesson.get("goal")}" vs master "{row["goal"]}"')
        r.rule(lesson.get("grammar") == row["grammar"], "grammar matches guides/a1.md",
               f'file "{lesson.get("grammar")}" vs master "{row["grammar"]}"')
    else:
        r.warn("no row in guides/a1.md for this lesson")

    sections = lesson.get("sections", [])
    if not sections:
        r.rule(False, "lesson has sections", "sections is empty")
        return r

    def section(t, title=None):
        for s in sections:
            if s["type"] == t and (title is None or s.get("title") == title):
                return s
        return None

    # --- vocabulary -------------------------------------------------------
    vocab_section = section("vocabulary")
    words = []
    if vocab_section:
        vp = ES / vocab_section["ref"]
        if vp.exists():
            words = read(vp).get("words", [])
    target = NEW_WORDS.get(number)
    if target:
        r.rule(len(words) == target, "vocabulary hits its new-word target",
               f"{len(words)} words, target {target}")

    # --- grammar ----------------------------------------------------------
    grammar_sections = [s for s in sections if s["type"] == "grammar"]
    r.rule(bool(grammar_sections), "lesson has at least one grammar section")
    for gs in grammar_sections:
        gp = ES / gs["ref"]
        if not gp.exists():
            r.rule(False, "grammar file exists", gs["ref"])
            continue
        g = read(gp)
        name = gp.stem
        parts = g.get("sections", [])
        prose = sum(len(p.get("content", "").split())
                    for p in parts if p["type"] in ("text", "tip"))
        r.rule(prose <= GRAMMAR_MAX_WORDS, f"{name}: prose within {GRAMMAR_MAX_WORDS} words",
               f"{prose} words")
        examples = sum(len(p.get("items", [])) for p in parts if p["type"] == "examples")
        if examples:
            lo, hi = GRAMMAR_EXAMPLES
            r.rule(lo <= examples <= hi, f"{name}: {lo}-{hi} worked examples",
                   f"{examples} examples")
        r.rule(any(p["type"] == "external-link" for p in parts),
               f"{name}: has a reference link", "none found")

    # --- exercises --------------------------------------------------------
    all_ex = {}
    for s in sections:
        if s["type"] != "exercise-group":
            continue
        ep = ES / s["ref"]
        if ep.exists():
            for e in read(ep).get("exercises", []):
                all_ex[e["id"]] = e

    total_expected = sum(EXERCISE_SPLIT.values())
    used = []
    for title, count in EXERCISE_SPLIT.items():
        grp = section("exercise-group", title)
        if not grp:
            r.rule(False, f"has a '{title}' exercise group", "missing")
            continue
        refs = grp.get("exerciseRefs", [])
        used += refs
        r.rule(len(refs) == count, f"'{title}' has {count} exercises", f"{len(refs)}")
        if title == "Practice":
            types = {all_ex[i]["type"] for i in refs if i in all_ex}
            r.rule(len(types) >= MIN_PRACTICE_TYPES,
                   f"practice spans {MIN_PRACTICE_TYPES}+ distinct types",
                   f"{len(types)}: {sorted(types)}")

    r.rule(len(used) == total_expected, f"lesson uses {total_expected} exercises",
           f"{len(used)}")
    r.rule(len(used) == len(set(used)), "no exercise is used twice",
           str([i for i in used if used.count(i) > 1]))

    # --- goals and checklist ---------------------------------------------
    goals = (section("goal") or {}).get("items", [])
    checks = (section("checklist") or {}).get("items", [])
    r.rule(len(checks) == CHECKLIST_ITEMS, f"exactly {CHECKLIST_ITEMS} checklist items",
           f"{len(checks)}")
    r.rule(len(goals) == len(checks), "goals and checklist are one-to-one",
           f"{len(goals)} goals vs {len(checks)} checks")
    bad = [c for c in checks if not c.startswith(CHECKLIST_PREFIX)]
    r.rule(not bad, f'every checklist item begins "{CHECKLIST_PREFIX}"', str(bad))

    # --- coverage: every new word in the story and in an exercise ---------
    story_section = section("story")
    story_words = 0
    if story_section:
        sp = ES / story_section["ref"]
        if sp.exists():
            story = read(sp)
            paras = [p["text"] for p in story.get("paragraphs", [])]
            story_words = sum(len(p.split()) for p in paras)
            blob = norm(" ".join(paras))
            missing, unsure = find_missing(words, blob)
            r.rule(not missing, "every new word appears in the story", str(missing))
            if unsure:
                r.warn("verbs not found literally in the story (check conjugated forms)",
                       str(unsure))
            lo, hi = STORY_WORDS
            r.rule(lo <= story_words <= hi, f"story is {lo}-{hi} words", f"{story_words}")

    ex_blob = norm(json.dumps([all_ex[i] for i in used if i in all_ex], ensure_ascii=False))
    missing_ex, unsure_ex = find_missing(words, ex_blob)
    r.rule(not missing_ex, "every new word appears in an exercise", str(missing_ex))
    if unsure_ex:
        r.warn("verbs not found literally in an exercise (check conjugated forms)",
               str(unsure_ex))

    return r


def main():
    keys = sys.argv[1:] or [f"a1-{n:02d}" for n in TEACHING_LESSONS]

    failed = skipped = 0
    for key in keys:
        r = audit(key)
        if r == "review":
            skipped += 1
            print(f"{key}: skipped — review lesson, format not yet designed")
            continue
        if r is None:
            continue
        if r.failures:
            failed += 1
            print(f"\n{r.name}: {r.checked - len(r.failures)}/{r.checked} rules pass")
            for f in r.failures:
                print(f"  FAIL  {f}")
        else:
            print(f"{r.name}: all {r.checked} rules pass")
        for w in r.warnings:
            print(f"  warn  {w}")

    print()
    if skipped:
        print(f"{skipped} review lesson(s) skipped")
    if failed:
        print(f"{failed} lesson(s) need work")
        return 1
    print("All audited lessons satisfy the A1 content spec")
    return 0


if __name__ == "__main__":
    sys.exit(main())
