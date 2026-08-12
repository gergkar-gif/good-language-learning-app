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

# A lesson whose grammar is too much for one sitting is split into parts —
# a1-03a, a1-03b, a1-03c — which share the slot, the word target and the
# story. A part is a lesson in its own right, so it still opens on goals and
# ends on a checklist, but it carries one grammar screen and a short block of
# exercises. Only the part holding the story gets a Reading block, because the
# unit's story is read once.
PART_SPLIT = {"Practice": 4, "Dialogue": 1, "Writing": 1}
PART_READING = 4
MIN_PART_PRACTICE_TYPES = 3
PART_CHECKLIST = (2, 4)
GRAMMAR_MAX_WORDS = 300
GRAMMAR_EXAMPLES = (3, 5)
CHECKLIST_ITEMS = 4
CHECKLIST_PREFIX = "I can"

# From a1-vocabulary-themes.md, which that document declares authoritative.
NEW_WORDS = {1: 10, 2: 10, 3: 12, 4: 12, 5: 15, 6: 15, 7: 18, 8: 18, 9: 20,
             # 10 was 20: 'el deseo' dropped with 'pedir un deseo', which
             # PLANNING.md ruled out as premature at A1 — see a1-10-voc.json.
             10: 19, 11: 20, 12: 20, 13: 20, 14: 20, 15: 20, 16: 20, 17: 20}

# Lessons 18-20 consolidate rather than teach: no new words, no new grammar,
# and a different shape entirely. Holding them to the teaching-lesson spec
# would report failures nobody can act on, so they have their own, from
# a1-content-spec.md section 4c.
REVIEW_LESSONS = {18, 19, 20}
REVIEW_SPLIT = {"Recap": 8, "Reading": 4, "Dialogue": 2, "Writing": 2}
MIN_RECAP_TYPES = 5
# A review that drills one point eight times is not a review. The union of
# what its Recap exercises claim to test has to actually range.
MIN_REVIEW_POINTS = 8
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


PROPER_NOUNS = {"carlos", "meg", "daniela", "lauren", "kaylee", "hungria",
                "sudafrica", "espana", "hanoi", "ana", "mexico", "vietnam"}


def spanish_tokens(text):
    return {w for w in re.findall(r"[a-zñ]+", norm(text)) if w not in PROPER_NOUNS}


def exercise_spanish(ex):
    """The Spanish a learner must already know to answer this exercise.

    English prompts and reading comprehension, which is written in English by
    design at A1, contribute nothing."""
    kind = ex["type"]
    if kind == "matching":
        return [pair[0] for pair in ex["pairs"]]
    if kind == "fill-blank":
        return [ex["sentence"], ex["answer"]]
    if kind == "sentence-builder":
        return ex["tiles"]
    if kind == "dialogue-complete":
        return [line["text"] for line in ex["prompt"]] + ex["options"]
    if kind == "structured-writing":
        return [line["answer"] for line in ex["template"]]
    if kind == "sentence-order":
        return ex["sentences"] if ex.get("category") != "reading" else []
    if kind in ("listening-choice", "dictation"):
        return [ex["sentence"]]
    if kind == "multiple-choice":
        return [o for o in ex["options"]
                if re.search(r"[¿¡áéíóúñ]|\b(el|la|un|una|quiero|soy)\b", o.lower())]
    return []


def teach_tokens(lesson, all_ex):
    """Walk one lesson in order, yielding (label, introduced, required) so a
    caller can tell what was on screen before each exercise."""
    for section in lesson.get("sections", []):
        kind = section["type"]
        if kind == "grammar":
            path = ES / section["ref"]
            if not path.exists():
                continue
            found = set()
            for part in read(path).get("sections", []):
                if part["type"] == "table":
                    for row in part.get("rows", []):
                        found |= spanish_tokens(row[0])
                elif part["type"] == "examples":
                    for item in part.get("items", []):
                        found |= spanish_tokens(item["spanish"])
                elif part["type"] in ("text", "tip"):
                    found |= spanish_tokens(part.get("content", ""))
            yield None, found, None
        elif kind == "vocabulary":
            path = ES / section["ref"]
            if path.exists():
                found = set()
                for word in read(path).get("words", []):
                    found |= spanish_tokens(searchable(word["lemma"]))
                yield None, found, None
        elif kind == "story":
            path = ES / section["ref"]
            if path.exists():
                found = set()
                for para in read(path).get("paragraphs", []):
                    found |= spanish_tokens(para["text"])
                yield None, found, None
        elif kind == "exercise-group":
            for eid in section.get("exerciseRefs", []):
                ex = all_ex.get(eid)
                if not ex:
                    continue
                required = set()
                for text in exercise_spanish(ex):
                    required |= spanish_tokens(text)
                yield f"{section.get('title', '?')} / {eid}", set(), required


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


KEY = re.compile(r"^(a1|a2|b1|b2|c1)-(\d{2})([a-z]?)$")


def parse_key(key):
    """'a1-03b' -> ('a1', 3, 'b'). An empty part means an unsplit lesson."""
    m = KEY.match(key)
    if not m:
        raise ValueError(f"not a lesson key: {key}")
    return m.group(1), int(m.group(2)), m.group(3)


def lesson_keys(level="a1"):
    """Every lesson file that exists, in teaching order. Globbed rather than
    generated from a range, so parts appear without being listed anywhere."""
    folder = ES / "lessons" / level
    if not folder.exists():
        return []
    return sorted(p.stem for p in folder.glob(f"{level}-*.json") if KEY.match(p.stem))


def unit_parts(level, number):
    """The part keys sharing this slot, or [] when the lesson is not split."""
    return [k for k in lesson_keys(level)
            if parse_key(k)[1] == number and parse_key(k)[2]]


def story_ref(key):
    """The story a lesson file points at, if any."""
    path = ES / "lessons" / key.split("-")[0] / f"{key}.json"
    if not path.exists():
        return None
    for section in read(path).get("sections", []):
        if section["type"] == "story":
            return section["ref"]
    return None


def load_master():
    """The Overview table of guides/a1.md, which owns every lesson's title and
    communicative goal. Only the first numbered table is read — the file has
    others further down."""
    path = ES / "guides" / "a1.md"
    if not path.exists():
        return {}

    master, started = {}, False
    for line in path.read_text(encoding="utf-8").splitlines():
        # Keyed by the label in the first column — "3" for a whole lesson,
        # "3a" for a part of a split one.
        row = re.match(r"^\|\s*(\d{1,2}[a-z]?)\s*\|(.+)\|\s*$", line)
        if row:
            started = True
            cells = [c.strip() for c in row.group(2).split("|")]
            if len(cells) >= 3:
                master.setdefault(row.group(1), {
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


def audit_review(key, lesson, r):
    """A consolidation lesson: no new words, no new grammar, and a story that
    is read first rather than last. See a1-content-spec.md section 4c."""
    sections = lesson.get("sections", [])

    def section(t, title=None):
        for s in sections:
            if s["type"] == t and (title is None or s.get("title") == title):
                return s
        return None

    # --- what a review must NOT have ------------------------------------
    r.rule(not section("grammar"), "no grammar screen",
           "a review teaches nothing new")
    r.rule(not section("vocabulary"), "no vocabulary section",
           "a review introduces no words")
    r.rule(not section("srs"), "no SRS step",
           "there are no new words to offer; the block's words are in Decks")

    # --- story, read first ----------------------------------------------
    story_section = section("story")
    r.rule(bool(story_section), "has a story")
    types = [s["type"] for s in sections]
    if story_section and "exercise-group" in types:
        r.rule(types.index("story") < types.index("exercise-group"),
               "story comes before the exercises",
               "in a review the story is the warm-up, not the payoff")
    if story_section:
        sp = ES / story_section["ref"]
        if sp.exists():
            paras = [p["text"] for p in read(sp).get("paragraphs", [])]
            words = sum(len(p.split()) for p in paras)
            lo, hi = STORY_WORDS
            r.rule(lo <= words <= hi, f"story is {lo}-{hi} words", f"{words}")

    # --- exercises --------------------------------------------------------
    all_ex = {}
    for s in sections:
        if s["type"] != "exercise-group":
            continue
        ep = ES / s["ref"]
        if ep.exists():
            for e in read(ep).get("exercises", []):
                all_ex[e["id"]] = e

    used, points = [], set()
    for title, count in REVIEW_SPLIT.items():
        grp = section("exercise-group", title)
        if not grp:
            r.rule(False, f"has a '{title}' exercise group", "missing")
            continue
        refs = grp.get("exerciseRefs", [])
        used += refs
        r.rule(len(refs) == count, f"'{title}' has {count} exercises", f"{len(refs)}")

        if title == "Recap":
            kinds = {all_ex[i]["type"] for i in refs if i in all_ex}
            r.rule(len(kinds) >= MIN_RECAP_TYPES,
                   f"recap spans {MIN_RECAP_TYPES}+ distinct types",
                   f"{len(kinds)}: {sorted(kinds)}")
            missing_tag = [i for i in refs
                           if i in all_ex and not all_ex[i].get("teaches")]
            r.rule(not missing_tag, "every recap exercise says what it tests",
                   str(missing_tag))
            for i in refs:
                points |= set(all_ex.get(i, {}).get("teaches", []))

    r.rule(len(points) >= MIN_REVIEW_POINTS,
           f"recap ranges over {MIN_REVIEW_POINTS}+ points",
           f"{len(points)}: {sorted(points)}")

    total = sum(REVIEW_SPLIT.values())
    r.rule(len(used) == total, f"lesson uses {total} exercises", f"{len(used)}")
    r.rule(len(used) == len(set(used)), "no exercise is used twice",
           str([i for i in used if used.count(i) > 1]))

    # --- goals and checklist ---------------------------------------------
    goals = (section("goal") or {}).get("items", [])
    checks = (section("checklist") or {}).get("items", [])
    r.rule(len(checks) == CHECKLIST_ITEMS,
           f"exactly {CHECKLIST_ITEMS} checklist items", f"{len(checks)}")
    r.rule(len(goals) == len(checks), "goals and checklist are one-to-one",
           f"{len(goals)} goals vs {len(checks)} checks")
    bad = [c for c in checks if not c.startswith(CHECKLIST_PREFIX)]
    r.rule(not bad, f'every checklist item begins "{CHECKLIST_PREFIX}"', str(bad))

    return r


def audit(key):
    """key is like 'a1-01', or 'a1-03b' for one part of a split lesson."""
    level, number, part = parse_key(key)
    r = Report(key)

    lesson_path = ES / "lessons" / level / f"{key}.json"
    if not lesson_path.exists():
        return None

    if number in REVIEW_LESSONS:
        row = MASTER.get(str(number))
        lesson = read(lesson_path)
        if row:
            r.rule(lesson.get("title") == row["title"], "title matches guides/a1.md",
                   f'file "{lesson.get("title")}" vs master "{row["title"]}"')
        return audit_review(key, lesson, r)

    lesson = read(lesson_path)
    siblings = unit_parts(level, number) if part else []

    # --- agrees with the master curriculum -------------------------------
    # guides/a1.md owns title and goal. They drifted once, silently, because
    # nothing compared them; this is what stops that happening again.
    row = MASTER.get(f"{number}{part}")
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
    if target and siblings:
        # A split lesson shares one slot's word budget between its parts.
        share = target // len(siblings)
        r.rule(len(words) == share, "vocabulary hits its share of the target",
               f"{len(words)} words, share {share} of {target}")
    elif target:
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
        # Not required: PLANNING.md asks for these third-party citations to
        # come out, starting with lessons 1-3. A missing one is a choice, not
        # a defect, so it's a warning rather than a failed rule.
        if not any(p["type"] == "external-link" for p in parts):
            r.warn(f"{name}: no reference link", "may be intentional — see PLANNING.md")

    # --- exercises --------------------------------------------------------
    all_ex = {}
    for s in sections:
        if s["type"] != "exercise-group":
            continue
        ep = ES / s["ref"]
        if ep.exists():
            for e in read(ep).get("exercises", []):
                all_ex[e["id"]] = e

    story_section = section("story")

    # A part carries the short block; only the part that owns the unit's story
    # also asks Reading questions about it.
    if siblings:
        split = dict(PART_SPLIT)
        if story_section:
            split["Reading"] = PART_READING
        min_types = MIN_PART_PRACTICE_TYPES
    else:
        split = dict(EXERCISE_SPLIT)
        min_types = MIN_PRACTICE_TYPES

    total_expected = sum(split.values())
    used = []
    for title, count in split.items():
        grp = section("exercise-group", title)
        if not grp:
            r.rule(False, f"has a '{title}' exercise group", "missing")
            continue
        refs = grp.get("exerciseRefs", [])
        used += refs
        r.rule(len(refs) == count, f"'{title}' has {count} exercises", f"{len(refs)}")
        if title == "Practice":
            types = {all_ex[i]["type"] for i in refs if i in all_ex}
            r.rule(len(types) >= min_types,
                   f"practice spans {min_types}+ distinct types",
                   f"{len(types)}: {sorted(types)}")

    r.rule(len(used) == total_expected, f"lesson uses {total_expected} exercises",
           f"{len(used)}")
    r.rule(len(used) == len(set(used)), "no exercise is used twice",
           str([i for i in used if used.count(i) > 1]))

    # --- goals and checklist ---------------------------------------------
    goals = (section("goal") or {}).get("items", [])
    checks = (section("checklist") or {}).get("items", [])
    if siblings:
        lo, hi = PART_CHECKLIST
        r.rule(lo <= len(checks) <= hi, f"{lo}-{hi} checklist items", f"{len(checks)}")
    else:
        r.rule(len(checks) == CHECKLIST_ITEMS,
               f"exactly {CHECKLIST_ITEMS} checklist items", f"{len(checks)}")
    r.rule(len(goals) == len(checks), "goals and checklist are one-to-one",
           f"{len(goals)} goals vs {len(checks)} checks")
    bad = [c for c in checks if not c.startswith(CHECKLIST_PREFIX)]
    r.rule(not bad, f'every checklist item begins "{CHECKLIST_PREFIX}"', str(bad))

    # --- coverage: every new word in the story and in an exercise ---------
    # A part without a story is still checked against the unit's story, which
    # one of its siblings owns: the words are met in the same reading.
    own_story = story_section["ref"] if story_section else None
    unit_story = own_story or next(
        (ref for k in siblings if k != key for ref in [story_ref(k)] if ref), None)

    if unit_story:
        sp = ES / unit_story
        if sp.exists():
            story = read(sp)
            paras = [p["text"] for p in story.get("paragraphs", [])]
            blob = norm(" ".join(paras))
            missing, unsure = find_missing(words, blob)
            r.rule(not missing, "every new word appears in the story", str(missing))
            if unsure:
                r.warn("verbs not found literally in the story (check conjugated forms)",
                       str(unsure))
            if own_story:
                story_words = sum(len(p.split()) for p in paras)
                lo, hi = STORY_WORDS
                r.rule(lo <= story_words <= hi, f"story is {lo}-{hi} words",
                       f"{story_words}")

    # Ids and teaches slugs are metadata, not content the learner ever sees.
    # Left in, they satisfy this rule by accident: 'la semana' counted as
    # practised because an exercise was called a1-06-writing-semana.
    seen_by_learner = [{k: v for k, v in all_ex[i].items()
                        if k not in ("id", "teaches")}
                       for i in used if i in all_ex]
    ex_blob = norm(json.dumps(seen_by_learner, ensure_ascii=False))
    missing_ex, unsure_ex = find_missing(words, ex_blob)
    r.rule(not missing_ex, "every new word appears in an exercise", str(missing_ex))
    if unsure_ex:
        r.warn("verbs not found literally in an exercise (check conjugated forms)",
               str(unsure_ex))

    return r


def check_teaching_order(keys):
    """Nothing may be asked for before it has been taught.

    Runs across lessons in order, because a word introduced in Lesson 1 is
    fair game in Lesson 5. Within a lesson the order matters too: the practice
    block sits before the vocabulary screen, so anything it tests has to have
    appeared on a grammar screen first."""
    issues = []
    known = set()

    # Always walk from Lesson 1, even when auditing a single lesson: 'tengo'
    # is fair game in Lesson 7 because Lesson 5 taught it, and starting from
    # an empty set reports half of a good lesson as untaught. Only the
    # requested lessons are reported on.
    requested = set(keys)
    limit = max(requested)
    walk = [k for k in sorted(set(lesson_keys("a1")) | requested) if k <= limit]

    for key in walk:
        level, number, _ = parse_key(key)
        if number in REVIEW_LESSONS:
            continue
        lesson_path = ES / "lessons" / level / f"{key}.json"
        if not lesson_path.exists():
            continue
        lesson = read(lesson_path)

        all_ex = {}
        for section in lesson.get("sections", []):
            if section["type"] == "exercise-group":
                path = ES / section["ref"]
                if path.exists():
                    for ex in read(path).get("exercises", []):
                        all_ex[ex["id"]] = ex

        for label, introduced, required in teach_tokens(lesson, all_ex):
            if label is None:
                known |= introduced
                continue
            unseen = sorted(t for t in required
                            if t not in known and not matches(t, " " + " ".join(known) + " "))
            if unseen and key in requested:
                issues.append(f"{key} {label} needs: {', '.join(unseen)}")
            known |= required

    return issues


def check_units(keys):
    """Rules that belong to a split lesson as a whole rather than to a part."""
    issues = []
    numbers = sorted({parse_key(k)[1] for k in keys if parse_key(k)[2]})

    for number in numbers:
        parts = unit_parts("a1", number)
        label = "/".join(p.split("-")[1] for p in parts)

        with_story = [k for k in parts if story_ref(k)]
        if len(with_story) != 1:
            issues.append(f"a1-{label}: exactly one part carries the story — "
                          f"{len(with_story)} do")

        total = 0
        for k in parts:
            lesson = read(ES / "lessons" / "a1" / f"{k}.json")
            for section in lesson.get("sections", []):
                if section["type"] == "vocabulary":
                    vp = ES / section["ref"]
                    if vp.exists():
                        total += len(read(vp).get("words", []))
        target = NEW_WORDS.get(number)
        if target and total != target:
            issues.append(f"a1-{label}: parts teach {total} new words, "
                          f"slot target {target}")

    return issues


def main():
    # Globbed, not generated from a range, so a lesson split into parts is
    # picked up without being listed anywhere. Review lessons are included
    # and reported as skipped.
    keys = sys.argv[1:] or lesson_keys("a1")

    failed = 0
    for key in keys:
        r = audit(key)
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

    unit_issues = check_units(keys)
    if unit_issues:
        print("\nSplit lessons:")
        for issue in unit_issues:
            print(f"  FAIL  {issue}")

    order_issues = check_teaching_order(keys)
    if order_issues:
        print("\nAsked for before it was taught:")
        for issue in order_issues:
            print(f"  FAIL  {issue}")

    print()
    if failed or order_issues or unit_issues:
        if failed:
            print(f"{failed} lesson(s) need work")
        if unit_issues:
            print(f"{len(unit_issues)} split-lesson rule(s) broken")
        if order_issues:
            print(f"{len(order_issues)} exercise(s) test untaught Spanish")
        return 1
    print("All audited lessons satisfy the A1 content spec")
    return 0


if __name__ == "__main__":
    sys.exit(main())
