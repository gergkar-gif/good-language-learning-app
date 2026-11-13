"""What the learner already knows before a unit, for regeneration and read
prompts (ROADMAP 153; docs/unit-pipeline-log.md § "Pipeline").

Agents used to open earlier units to work out what was taught, and still
presented earlier material as new. This prints one sheet instead:

- grammar taught in earlier units (skill title, slug, the screen that
  teaches it), grouped by unit;
- grammar this unit's own screens teach (taught_in here);
- grammar taught later in the level (don't use it, or mark it as new);
- every earlier grammar screen's title, grouped by unit (a skill's later
  screens extend it: *közben* after *előtt/után*, *-on* for countries);
- words first taught in earlier units (from the vocabulary lists, via
  indexes/word-lesson-index.json), grouped by unit.

    python scripts/prior_knowledge.py <course> <level> <unit id> [--out file.md]

Run `python scripts/build_word_lesson_index.py <lang>` first if vocabulary
lists changed.
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

ROOT = Path(__file__).resolve().parent.parent
LEVELS = ["a1", "a2", "b1", "b2", "c1", "c2"]


def read(rel):
    p = ROOT / rel
    return json.loads(p.read_text(encoding="utf-8")) if p.is_file() else None


def main():
    args = sys.argv[1:]
    out_path = None
    if "--out" in args:
        i = args.index("--out")
        out_path = args[i + 1]
        del args[i:i + 2]
    if len(args) != 3:
        sys.exit(__doc__)
    course, level, unit_id = args[0], args[1].lower(), args[2]
    lang = course.split("-")[0]

    # course order: every unit up to and including this level
    units = []                       # [(level, unit)]
    for lv in LEVELS[:LEVELS.index(level) + 1]:
        units += [(lv, u) for u in read(f"content/{course}/curriculum/units/{lv}.json") or []]
    pos = next((i for i, (lv, u) in enumerate(units) if lv == level and u.get("id") == unit_id), None)
    if pos is None:
        sys.exit(f"no unit {unit_id!r} in content/{course}/curriculum/units/{level}.json")
    unit_of = {}                     # stem -> unit index
    for i, (lv, u) in enumerate(units):
        for s in u.get("stems", []):
            unit_of[s] = i
    # Units of a hidden track (HIDDEN_TRACKS in build-manifest.py, "hidden": true in
    # the generated curriculum.json) are not shown: what only they teach is not met.
    hidden_slugs = {(lk.lower(), u.get("slug")) for lk, L in ((read(f"content/{course}/curriculum/curriculum.json") or {})
                    .get("levels") or {}).items() for u in L.get("units", []) if u.get("hidden")}
    hidden = {i for i, (lv, u) in enumerate(units) if (lv, u.get("id")) in hidden_slugs}
    if pos in hidden:
        hidden = set()               # reading a hidden unit: its own track counts

    def stem_of(name):
        """The stem a screen id or file name belongs to: the longest stem it
        starts with. HU screens are `<stem>-a-gr`, Spanish ones `<stem>-gr` or
        `<stem>-<topic>-gr` (`a1-06-02-ar-verbs-gr`)."""
        name = re.sub(r"-gr(\.json)?$", "", name)
        best = None
        for s in unit_of:
            if (name == s or name.startswith(s + "-")) and (best is None or len(s) > len(best)):
                best = s
        return best
    # "You know … from Unit N": the number the app shows (scripts/unit_numbers.py:
    # per track; "B1 Unit 11" is core, another track is named, "B1 Citizenship Unit 7")
    import unit_numbers as un
    tables = {lv: un.table(course, lv) for lv in LEVELS}
    idx_in_level = {}
    for i, (lv, u) in enumerate(units):
        idx_in_level[i] = sum(1 for lv2, _ in units[:i] if lv2 == lv)
    num = {i: un.number(course, units[i][0], idx_in_level[i], tables[units[i][0]])[1] for i in idx_in_level}
    name = lambda i: f"{un.name(course, units[i][0], idx_in_level[i], tables[units[i][0]])} {units[i][1].get('id')}"

    skills = (read(f"skills/{lang}.json") or {}).get("skills", {})
    before, here, later, hidden_skills = {}, [], [], []
    # skills of the next level in a family this unit's exercises drill: a lesson
    # teaching one of them under a neighbouring tag is invisible to the validator
    next_level = LEVELS[LEVELS.index(level) + 1] if level != LEVELS[-1] else None
    above, families = [], set()
    for stem in units[pos][1].get("stems", []):
        for ex in (read(f"content/{course}/exercises/{level}/{stem}-ex.json") or {}).get("exercises", []):
            for slug in ex.get("teaches") or []:
                if skills.get(slug, {}).get("kind") == "grammar":
                    families.add(skills[slug].get("family"))
    for slug, sk in skills.items():
        if sk.get("kind") != "grammar" or sk.get("variant") not in (None, course):
            continue
        scr = sk.get("taught_in") or ""
        i = unit_of.get(stem_of(scr)) if scr else None
        if i is None:
            if sk.get("level", "").lower() == next_level:
                above.append(sk)
            continue
        line = f"{sk.get('title', slug)} (`{slug}`, {scr})"
        if i in hidden:
            hidden_skills.append(f"{name(i)}: {line}")
        elif i < pos:
            before.setdefault(i, []).append(line)
        elif i == pos:
            here.append(line)
        elif units[i][0] == level:
            later.append((i, line))

    words = {}
    # lesson id = "lesson." + stem with "." for "-": lesson.a1.16a, lesson.a1.01.01
    by_lid = {"lesson." + s.replace("-", "."): s for s in unit_of}
    for lemma, lid in ((read(f"content/{course}/indexes/word-lesson-index.json") or {}).get("byLemma") or {}).items():
        i = unit_of.get(by_lid.get(lid))
        if i is not None and i < pos and i not in hidden:
            words.setdefault(i, []).append(lemma)

    titles = {}
    for lv in sorted({lv for lv, _ in units[:pos]}, key=LEVELS.index):
        for f in sorted((ROOT / f"content/{course}/grammar/{lv}").glob("*-gr.json")):
            i = unit_of.get(stem_of(f.name))
            if i is None or i >= pos or i in hidden:
                continue
            g = read(f.relative_to(ROOT))
            if isinstance(g, dict) and g.get("title"):
                titles.setdefault(i, []).append((units[i][1]["stems"].index(stem_of(f.name)), f"{f.name[:-8]} {g['title']}"))
    titles = {i: [x for _, x in sorted(v)] for i, v in titles.items()}

    u = units[pos][1]
    lines = [f"# Before {course} {level.upper()} Unit {num[pos]} `{unit_id}` ({', '.join(u.get('stems', []))})", "",
             "Generated by scripts/prior_knowledge.py. Everything under \"Known\" is met: a screen that",
             "uses it says so (\"You know …\") and never presents it as new. \"Later\" is not met yet.",
             "Recap wording: \"You know … from Unit N\" with N as below, the number the app shows",
             "(per track: B2 core Unit 2 is the second core unit; an A1 unit: \"from A1\").", "",
             "## Known grammar (earlier units)", ""]
    for i in sorted(before):
        lines.append(f"- **{name(i)}:** " + "; ".join(sorted(before[i])))
    lines += ["", "## Grammar this unit teaches", ""] + [f"- {x}" for x in sorted(here)] or ["- (none)"]
    lines += ["", f"## Grammar later in {level.upper()} (not met: don't use, or present as new only if this unit teaches it)", ""]
    lines += [f"- {name(i)}: {x}" for i, x in sorted(later)] or ["- (none)"]
    if hidden_skills:
        lines += ["", "## Taught only on a screen of a hidden track (the learner has NOT met it: used or drilled here = a defect to report, the skill needs a screen in a core unit)", ""]
        lines += [f"- {x}" for x in sorted(hidden_skills)]
    lines += ["", f"## Same family as this unit's grammar, taught at {(next_level or '').upper()} (presented or drilled here = a defect, or the skill's level is wrong: report it)", ""]
    same = sorted((s.get("level", ""), s.get("family", ""), f"{s.get('title', slug)} (`{slug}`, {s.get('taught_in')})")
                  for slug, s in skills.items() if s in above and s.get("family") in families)
    lines += [f"- {lv} {fam}: {x}" for lv, fam, x in same] or ["- (none)"]
    lines += ["", "## Earlier grammar screens (titles)", ""]
    for i in sorted(titles):
        lines.append(f"- **{name(i)}:** " + "; ".join(titles[i]))
    lines += ["", "## Known words (first taught in earlier units)", ""]
    for i in sorted(words):
        lines.append(f"- **{name(i)}:** " + ", ".join(sorted(words[i])))
    text = "\n".join(lines) + "\n"
    if out_path:
        Path(out_path).write_text(text, encoding="utf-8")
        print(f"wrote {out_path}: {sum(map(len, before.values()))} known skills, {sum(map(len, words.values()))} known words")
    else:
        sys.stdout.write(text)


if __name__ == "__main__":
    main()
