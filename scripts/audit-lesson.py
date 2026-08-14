#!/usr/bin/env python3
"""Check lesson content against its content spec.

scripts/validate-content.py checks the shape of each file on its own. This
checks the rules that span files and that count things — the ones that
actually go wrong when authoring at volume.

Content is organised as units of six lesson files: five teaching lessons
(01-05) and one consolidation, e.g. a1-01-01.json ... a1-01-consolidation.json.
This script discovers units from that id shape directly (the same pattern
lesson.schema.json's `id` regex uses), rather than from a hardcoded list, so
new units are picked up automatically.

Per-lesson targets (title, new-word count, exercise count) come from
whichever planning document actually describes lessons at this grain:

  a2  content/es/guides/a2-lesson-guide.md
  b1  content/es/guides/Parlour B1 Consolidated Unit List.md (Core track only
      — Latin America units use word-slug ids the document doesn't carry;
      see b1-content-spec.md section 1a)
  a1  no such document exists. guides/a1.md describes 20 units at unit grain
      (one title/goal/grammar per unit), but the lesson files are five
      classes per unit with their own narrower titles — the two no longer
      correspond, and reconciling them is a separate, unstarted task. A1
      lessons are checked structurally only; title/word/exercise-count
      checks are skipped and reported as such rather than silently assumed
      to pass.

    python scripts/audit-lesson.py            # every unit in every level
    python scripts/audit-lesson.py a1          # every a1 unit
    python scripts/audit-lesson.py a1-01       # one unit
    python scripts/audit-lesson.py a1-01-01    # one lesson file

Exits non-zero if any checked lesson fails a hard rule. Exercise-count drift
from the plan is a warning, not a failure — actual A2 content already
diverges from a2-lesson-guide.md's stated counts in places, and that has
evidently been tolerated, so flagging it outright would fail content nobody
considers broken. Everything else a plan can check (title, new-word count)
is a hard rule.
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

LEVELS = ("a1", "a2", "b1")

# Does a teaching lesson have a Listening exercise-group? Introduced at A2
# (see guides/listening-plan in project memory); A1 predates it.
HAS_LISTENING = {"a1": False, "a2": True, "b1": True}

# Consolidation shape. "single" = one "Review" exercise-group, every exercise
# `teaches`-tagged, spanning several types and several distinct points — A1's
# design (a1-content-spec.md section 4c), adopted for B1. "split" = the same
# Practice/Listening/Dialogue/Writing blocks as a teaching lesson, just
# without grammar/vocabulary/story — what A2 actually shipped, which drifted
# from A1's design rather than deliberately choosing a different one.
CONSOLIDATION_SHAPE = {"a1": "single", "a2": "split", "b1": "single"}

MIN_PRACTICE_TYPES = {"a1": 5, "a2": 5, "b1": 6}
MIN_REVIEW_TYPES = {"a1": 5, "a2": 5, "b1": 6}
MIN_REVIEW_POINTS = {"a1": 8, "a2": 8, "b1": 10}
GRAMMAR_MAX_WORDS = 300
GRAMMAR_EXAMPLES = (3, 5)
CHECKLIST_PREFIX = "I can"

ARTICLE = re.compile(r"^(el|la|los|las|un|una|unos|unas) ")

# Proper nouns the word-coverage matcher should ignore. Shared across the
# existing A1/A2 story cast; Latin America and Core-classics stories at B1
# will introduce their own (historical figures, adapted-classic character
# names) and this list will need extending as that content is written.
PROPER_NOUNS = {"carlos", "meg", "daniela", "lauren", "kaylee", "hungria",
                "sudafrica", "espana", "hanoi", "ana", "mexico", "vietnam",
                "ninh", "binh", "madrid", "colombia", "peru", "valencia",
                "phileas", "fogg", "passepartout"}


def norm(text):
    text = unicodedata.normalize("NFD", str(text).lower())
    text = "".join(c for c in text if unicodedata.category(c) != "Mn")
    return re.sub(r"[^a-z0-9 ]", " ", text)


def searchable(lemma):
    """A noun is listed with its article ('el café') but the story says 'un
    café' or just 'café', so the article is dropped before matching."""
    return ARTICLE.sub("", norm(lemma).strip()).strip()


def spanish_tokens(text):
    return {w for w in re.findall(r"[a-zñ]+", norm(text)) if w not in PROPER_NOUNS}


def exercise_spanish(ex):
    """The Spanish a learner must already know to answer this exercise."""
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


def matches(term, haystack):
    if not term:
        return False
    if term in haystack:
        return True
    if " " in term:
        return False
    stem = re.sub(r"(es|os|as|s)$", "", term)
    stem = re.sub(r"[oae]$", "", stem)
    return len(stem) >= 4 and stem in haystack


def find_missing(words, haystack):
    """Split into hard misses and ones we cannot judge (conjugated verbs)."""
    missing, unsure = [], []
    for w in words:
        if matches(searchable(w["lemma"]), haystack):
            continue
        (unsure if w.get("pos", "").startswith("verb") else missing).append(w["lemma"])
    return missing, unsure


def read(path):
    return json.loads(path.read_text(encoding="utf-8"))


# --- discovery ---------------------------------------------------------------
# Matches lesson.schema.json's own id pattern: level, then a unit token that
# is either a two-digit position (optionally lettered, for an old slot like
# 03c) or a word slug, then a two-digit lesson position or "consolidation".

KEY = re.compile(r"^(a1|a2|b1|b2|c1)-(\d{2}[a-z]?|[a-z]+)-(\d{2}|consolidation)$")


def parse_key(key):
    m = KEY.match(key)
    return m.groups() if m else None


def lesson_keys(level):
    folder = ES / "lessons" / level
    if not folder.exists():
        return []
    return sorted(p.stem for p in folder.glob(f"{level}-*.json"))


def group_units(level):
    """{unit: [parts in teaching order]}, plus keys that don't match the
    unit/lesson-group shape at all (a handful of pre-restructure files, e.g.
    a1-10.json, still sitting in the old one-file-per-lesson shape)."""
    units, legacy = {}, []
    for key in lesson_keys(level):
        parsed = parse_key(key)
        if not parsed:
            legacy.append(key)
            continue
        _, unit, part = parsed
        units.setdefault(unit, []).append(part)
    for unit in units:
        units[unit].sort(key=lambda p: (p == "consolidation", p))
    return units, legacy


def section(lesson, kind, title=None):
    for s in lesson.get("sections", []):
        if s["type"] == kind and (title is None or s.get("title") == title):
            return s
    return None


def load_exercises(lesson):
    all_ex = {}
    for s in lesson.get("sections", []):
        if s["type"] != "exercise-group":
            continue
        ep = ES / s["ref"]
        if ep.exists():
            for e in read(ep).get("exercises", []):
                all_ex[e["id"]] = e
    return all_ex


def unit_story_ref(level, unit, parts):
    for part in parts:
        path = ES / "lessons" / level / f"{level}-{unit}-{part}.json"
        if not path.exists():
            continue
        s = section(read(path), "story")
        if s:
            return s["ref"]
    return None


# --- plan sources --------------------------------------------------------------

def parse_range(raw):
    """'15' -> (15, 15). '15-17' or '15–17' -> (15, 17)."""
    m = re.match(r"^(\d+)\s*[-–]\s*(\d+)$", raw)
    if m:
        return int(m.group(1)), int(m.group(2))
    n = int(raw)
    return n, n


def load_a2_plan():
    path = ES / "guides" / "a2-lesson-guide.md"
    if not path.exists():
        return {}
    text = path.read_text(encoding="utf-8")
    row = re.compile(
        r'^(\d+)\.(\d+)\s+"([^"]+)"\s+—\s+grammar:\s+(.+?)\s+—\s+'
        r'(~?\d+)\s+new words?\s+—\s+(\d+)\s+exercises', re.MULTILINE)
    plan = {}
    for unit, lesson, title, grammar, words, exercises in row.findall(text):
        part = "consolidation" if lesson == "6" else lesson.zfill(2)
        plan[(unit.zfill(2), part)] = {
            "title": title, "grammar": grammar,
            "words": int(words.lstrip("~")), "exercises": parse_range(exercises),
        }
    return plan


def load_b1_plan():
    """Core track only — see the module docstring."""
    path = ES / "guides" / "Parlour B1 Consolidated Unit List.md"
    if not path.exists():
        return {}
    text = path.read_text(encoding="utf-8")
    core_end = text.find("# Part II")
    core_text = text[:core_end] if core_end != -1 else text
    row = re.compile(
        r'\*\*Lesson (\d+)\.(\d+): ([^\n*]+)\*\*  \n'
        r'(?:Grammar|Focus): ([^\n]+?)  \n'
        r'New words: (~?\d+)  \n'
        r'Exercises: (\S+)\n')
    plan = {}
    for unit, lesson, title, grammar, words, exercises in row.findall(core_text):
        part = "consolidation" if lesson == "6" else lesson.zfill(2)
        plan[(unit.zfill(2), part)] = {
            "title": title, "grammar": grammar,
            "words": int(words.lstrip("~")), "exercises": parse_range(exercises),
        }
    return plan


PLAN_LOADERS = {"a2": load_a2_plan, "b1": load_b1_plan}


# --- reporting -----------------------------------------------------------------

class Report:
    def __init__(self, name):
        self.name = name
        self.failures = []
        self.warnings = []
        self.checked = 0

    def rule(self, ok, label, detail=""):
        self.checked += 1
        if not ok:
            self.failures.append(label + (f" — {detail}" if detail else ""))

    def warn(self, label, detail=""):
        self.warnings.append(label + (f" — {detail}" if detail else ""))


# --- per-lesson audits -----------------------------------------------------------

def audit_teaching_lesson(level, unit, part, plan_entry, story_ref):
    key = f"{level}-{unit}-{part}"
    r = Report(key)
    lesson_path = ES / "lessons" / level / f"{key}.json"
    lesson = read(lesson_path)

    if plan_entry:
        r.rule(lesson.get("title") == plan_entry["title"], "title matches the plan",
               f'file "{lesson.get("title")}" vs plan "{plan_entry["title"]}"')
    else:
        r.warn("no plan entry for this lesson — title/word-count checks skipped")

    # --- vocabulary ---------------------------------------------------------
    vocab_section = section(lesson, "vocabulary")
    r.rule(vocab_section is not None, "has a vocabulary section")
    words = []
    if vocab_section:
        vp = ES / vocab_section["ref"]
        if vp.exists():
            words = read(vp).get("words", [])
    if plan_entry:
        r.rule(len(words) == plan_entry["words"], "vocabulary hits its new-word target",
               f'{len(words)} words, target {plan_entry["words"]}')

    # --- grammar / Latin-America focus screen -------------------------------
    grammar_sections = [s for s in lesson.get("sections", []) if s["type"] == "grammar"]
    r.rule(len(grammar_sections) >= 1, "lesson has a grammar/focus section")
    for gs in grammar_sections:
        gp = ES / gs["ref"]
        if not gp.exists():
            r.rule(False, "grammar file exists", gs["ref"])
            continue
        g = read(gp)
        parts_ = g.get("sections", [])
        prose = sum(len(p.get("content", "").split())
                    for p in parts_ if p["type"] in ("text", "tip"))
        r.rule(prose <= GRAMMAR_MAX_WORDS, f"prose within {GRAMMAR_MAX_WORDS} words",
               f"{prose} words")
        examples = sum(len(p.get("items", [])) for p in parts_ if p["type"] == "examples")
        if examples:
            lo, hi = GRAMMAR_EXAMPLES
            r.rule(lo <= examples <= hi, f"{lo}-{hi} worked examples", f"{examples}")
        if not any(p["type"] == "external-link" for p in parts_):
            r.warn("no reference link", "may be intentional, e.g. a Latin America focus screen")

    # --- exercises -----------------------------------------------------------
    all_ex = load_exercises(lesson)
    has_story = section(lesson, "story") is not None
    block_titles = ["Practice"]
    if has_story:
        block_titles.append("Reading")
    if HAS_LISTENING[level]:
        block_titles.append("Listening")
    block_titles += ["Dialogue", "Writing"]

    used = []
    for title in block_titles:
        grp = section(lesson, "exercise-group", title)
        r.rule(grp is not None, f"has a '{title}' exercise group")
        if not grp:
            continue
        refs = grp.get("exerciseRefs", [])
        used += refs
        if title == "Practice":
            kinds = {all_ex[i]["type"] for i in refs if i in all_ex}
            min_types = MIN_PRACTICE_TYPES[level]
            r.rule(len(kinds) >= min_types, f"practice spans {min_types}+ distinct types",
                   f"{len(kinds)}: {sorted(kinds)}")
        if title == "Reading":
            tagged = [i for i in refs if i in all_ex and all_ex[i].get("teaches")]
            r.rule(not tagged, "reading exercises carry no teaches tag", str(tagged))

    if plan_entry:
        lo, hi = plan_entry["exercises"]
        total = len(used)
        if lo <= total <= hi:
            r.rule(True, f"exercise total within plan ({lo}-{hi})", str(total))
        else:
            r.warn(f"exercise total drifted from plan ({lo}-{hi})", str(total))
    r.rule(len(used) == len(set(used)), "no exercise is used twice",
           str([i for i in used if used.count(i) > 1]))

    # --- goal / checklist / srs ----------------------------------------------
    goals = (section(lesson, "goal") or {}).get("items", [])
    checks = (section(lesson, "checklist") or {}).get("items", [])
    r.rule(len(goals) == len(checks), "goals and checklist are one-to-one",
           f"{len(goals)} goals vs {len(checks)} checks")
    bad = [c for c in checks if not c.startswith(CHECKLIST_PREFIX)]
    r.rule(not bad, f'every checklist item begins "{CHECKLIST_PREFIX}"', str(bad))
    r.rule(section(lesson, "srs") is not None, "has an srs section")

    # --- coverage: every new word appears in the unit's story and in an
    #     exercise here. A lesson without its own story is still checked
    #     against the unit's shared one. ------------------------------------
    if story_ref:
        sp = ES / story_ref
        if sp.exists():
            story = read(sp)
            paras = [p["text"] for p in story.get("paragraphs", [])]
            blob = norm(" ".join(paras))
            missing, unsure = find_missing(words, blob)
            r.rule(not missing, "every new word appears in the unit's story", str(missing))
            if unsure:
                r.warn("verbs not found literally in the story (check conjugated forms)",
                       str(unsure))
    elif words:
        r.warn("unit has no story yet — word-in-story coverage not checked")

    seen_by_learner = [{k: v for k, v in all_ex[i].items() if k not in ("id", "teaches")}
                        for i in used if i in all_ex]
    ex_blob = norm(json.dumps(seen_by_learner, ensure_ascii=False))
    missing_ex, unsure_ex = find_missing(words, ex_blob)
    r.rule(not missing_ex, "every new word appears in an exercise", str(missing_ex))
    if unsure_ex:
        r.warn("verbs not found literally in an exercise (check conjugated forms)",
               str(unsure_ex))

    return r


def audit_consolidation(level, unit, plan_entry):
    key = f"{level}-{unit}-consolidation"
    r = Report(key)
    lesson = read(ES / "lessons" / level / f"{key}.json")

    if plan_entry:
        r.rule(lesson.get("title") == plan_entry["title"], "title matches the plan",
               f'file "{lesson.get("title")}" vs plan "{plan_entry["title"]}"')
    else:
        r.warn("no plan entry for this lesson — title/word-count checks skipped")

    r.rule(section(lesson, "grammar") is None, "no grammar/focus screen",
           "a consolidation teaches nothing new")
    r.rule(section(lesson, "vocabulary") is None, "no vocabulary section",
           "a consolidation introduces no words")

    all_ex = load_exercises(lesson)
    shape = CONSOLIDATION_SHAPE[level]
    used = []

    if shape == "single":
        r.rule(section(lesson, "srs") is None, "no SRS step",
               "there are no new words to offer; the block's words are in Decks")
        grp = section(lesson, "exercise-group", "Review")
        r.rule(grp is not None, "has a 'Review' exercise group")
        if grp:
            refs = grp.get("exerciseRefs", [])
            used = refs
            kinds = {all_ex[i]["type"] for i in refs if i in all_ex}
            min_types = MIN_REVIEW_TYPES[level]
            r.rule(len(kinds) >= min_types, f"review spans {min_types}+ distinct types",
                   f"{len(kinds)}: {sorted(kinds)}")
            missing_tag = [i for i in refs if i in all_ex and not all_ex[i].get("teaches")]
            r.rule(not missing_tag, "every review exercise says what it tests",
                   str(missing_tag))
            points = set()
            for i in refs:
                points |= set(all_ex.get(i, {}).get("teaches", []))
            min_points = MIN_REVIEW_POINTS[level]
            r.rule(len(points) >= min_points, f"review ranges over {min_points}+ points",
                   f"{len(points)}: {sorted(points)}")
    else:
        block_titles = ["Practice"] + (["Listening"] if HAS_LISTENING[level] else []) + \
                       ["Dialogue", "Writing"]
        for title in block_titles:
            grp = section(lesson, "exercise-group", title)
            r.rule(grp is not None, f"has a '{title}' exercise group")
            if grp:
                used += grp.get("exerciseRefs", [])

    if plan_entry:
        lo, hi = plan_entry["exercises"]
        total = len(used)
        if lo <= total <= hi:
            r.rule(True, f"exercise total within plan ({lo}-{hi})", str(total))
        else:
            r.warn(f"exercise total drifted from plan ({lo}-{hi})", str(total))
    r.rule(len(used) == len(set(used)), "no exercise is used twice",
           str([i for i in used if used.count(i) > 1]))

    goals = (section(lesson, "goal") or {}).get("items", [])
    checks = (section(lesson, "checklist") or {}).get("items", [])
    r.rule(len(goals) == len(checks), "goals and checklist are one-to-one",
           f"{len(goals)} goals vs {len(checks)} checks")
    bad = [c for c in checks if not c.startswith(CHECKLIST_PREFIX)]
    r.rule(not bad, f'every checklist item begins "{CHECKLIST_PREFIX}"', str(bad))
    return r


def audit_unit(level, unit, parts, plan):
    if not parts:
        return []
    story_ref = unit_story_ref(level, unit, parts)
    reports = []
    for part in parts:
        plan_entry = plan.get((unit, part))
        if part == "consolidation":
            reports.append(audit_consolidation(level, unit, plan_entry))
        else:
            reports.append(audit_teaching_lesson(level, unit, part, plan_entry, story_ref))
    if not any(p != "consolidation" and unit_story_ref(level, unit, [p]) for p in parts):
        pass  # covered per-lesson by the "unit has no story yet" warning
    return reports


# --- teaching order --------------------------------------------------------------
# Nothing may be asked for before it has been taught. Only walks units with a
# purely numeric id, in ascending order — word-slug units (a1's thematic
# ones, and every Latin America unit at B1) have no inherent sequence
# recoverable from the filename alone, so they are left out of this pass
# rather than guessed at.

def teach_tokens(lesson, all_ex):
    for s in lesson.get("sections", []):
        kind = s["type"]
        if kind == "grammar":
            path = ES / s["ref"]
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
            path = ES / s["ref"]
            if path.exists():
                found = set()
                for word in read(path).get("words", []):
                    found |= spanish_tokens(searchable(word["lemma"]))
                yield None, found, None
        elif kind == "story":
            path = ES / s["ref"]
            if path.exists():
                found = set()
                for para in read(path).get("paragraphs", []):
                    found |= spanish_tokens(para["text"])
                yield None, found, None
        elif kind == "exercise-group":
            for eid in s.get("exerciseRefs", []):
                ex = all_ex.get(eid)
                if not ex:
                    continue
                required = set()
                for text in exercise_spanish(ex):
                    required |= spanish_tokens(text)
                yield f"{s.get('title', '?')} / {eid}", set(), required


def accumulate_known(level):
    """Every token taught anywhere in a level — grammar, vocabulary, story,
    exercises, all units, all parts, order within the level not enforced.
    Used to seed a later level's walk: A2 lesson 1 assumes the whole of A1
    is already known, not an empty vocabulary."""
    known = set()
    units, _ = group_units(level)
    for unit, parts in units.items():
        for part in parts:
            path = ES / "lessons" / level / f"{level}-{unit}-{part}.json"
            if not path.exists():
                continue
            lesson = read(path)
            all_ex = load_exercises(lesson)
            for label, introduced, required in teach_tokens(lesson, all_ex):
                known |= introduced
                if label is not None:
                    known |= required
    return known


def check_teaching_order(level, requested_units):
    numeric_units = sorted((u for u, parts in group_units(level)[0].items() if u.isdigit()),
                            key=int)
    if not numeric_units:
        return []
    limit = max((u for u in requested_units if u.isdigit()), key=int, default=numeric_units[-1])
    walk = [u for u in numeric_units if int(u) <= int(limit)]

    issues = []
    known = set()
    prior = LEVELS[:LEVELS.index(level)] if level in LEVELS else ()
    for earlier in prior:
        known |= accumulate_known(earlier)
    units, _ = group_units(level)
    for unit in walk:
        for part in units[unit]:
            if part == "consolidation":
                continue
            key = f"{level}-{unit}-{part}"
            path = ES / "lessons" / level / f"{key}.json"
            if not path.exists():
                continue
            lesson = read(path)
            all_ex = load_exercises(lesson)
            for label, introduced, required in teach_tokens(lesson, all_ex):
                if label is None:
                    known |= introduced
                    continue
                unseen = sorted(t for t in required
                                if t not in known and not matches(t, " " + " ".join(known) + " "))
                if unseen and unit in requested_units:
                    issues.append(f"{key} {label} needs: {', '.join(unseen)}")
                known |= required
    return issues


# --- main ------------------------------------------------------------------------

def resolve_targets(args):
    """Returns {level: set(unit) or None (meaning "all units")}."""
    if not args:
        return {lvl: None for lvl in LEVELS}
    targets = {}
    for arg in args:
        if arg in LEVELS:
            targets[arg] = None
            continue
        parsed = parse_key(arg) or (arg.split("-", 1) + [None] if "-" in arg else None)
        # accept both "a1-01" (unit) and "a1-01-01" (single lesson, audited
        # as its whole unit since coverage checks are unit-scoped)
        m = re.match(r"^(a1|a2|b1|b2|c1)-(\d{2}[a-z]?|[a-z]+)", arg)
        if not m:
            print(f"Unrecognised target: {arg}", file=sys.stderr)
            continue
        level, unit = m.groups()
        targets.setdefault(level, set())
        if targets[level] is not None:
            targets[level].add(unit)
    return targets


def main():
    targets = resolve_targets(sys.argv[1:])

    failed = 0
    all_order_issues = []
    for level in LEVELS:
        if level not in targets:
            continue
        units, legacy = group_units(level)
        plan = PLAN_LOADERS[level]() if level in PLAN_LOADERS else {}
        if level not in PLAN_LOADERS:
            print(f"[{level}] no per-lesson plan document — title/word/exercise "
                  f"checks skipped for every unit\n")

        wanted_units = sorted(units) if targets[level] is None else sorted(targets[level] & set(units))
        if targets[level] is not None:
            missing = targets[level] - set(units)
            for u in missing:
                print(f"[{level}] no unit '{u}' found (looked for {level}-{u}-*.json)")

        for unit in wanted_units:
            parts = units[unit]
            reports = audit_unit(level, unit, parts, plan)
            for r in reports:
                if r.failures:
                    failed += 1
                    print(f"\n{r.name}: {r.checked - len(r.failures)}/{r.checked} rules pass")
                    for f in r.failures:
                        print(f"  FAIL  {f}")
                else:
                    print(f"{r.name}: all {r.checked} rules pass")
                for w in r.warnings:
                    print(f"  warn  {w}")

        if legacy:
            print(f"\n[{level}] {len(legacy)} lesson file(s) in the old one-file-per-lesson "
                  f"shape, not audited by this script — migrate to the unit/lesson-group "
                  f"layout to get coverage: {', '.join(legacy)}")

        order_issues = check_teaching_order(level, wanted_units)
        if order_issues:
            print(f"\n[{level}] Asked for before it was taught:")
            for issue in order_issues:
                print(f"  FAIL  {issue}")
            all_order_issues += order_issues

    print()
    if failed or all_order_issues:
        if failed:
            print(f"{failed} lesson(s) need work")
        if all_order_issues:
            print(f"{len(all_order_issues)} exercise(s) test untaught Spanish")
        return 1
    print("All audited lessons satisfy their content spec")
    return 0


if __name__ == "__main__":
    sys.exit(main())
