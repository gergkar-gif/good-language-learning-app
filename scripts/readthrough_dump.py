#!/usr/bin/env python3
"""Print one unit for the skill-tag read-through (ROADMAP 125 step 3).

    python scripts/readthrough_dump.py hu a1 objects-locations > unit.txt

Shows the unit's grammar screens and lesson vocabulary, then every exercise
with its current tags, followed by the skills a tag may use: the course's
grammar skills at or below the level (with the screen that teaches each) and
the vocabulary skills of this and earlier units. Each grammar skill is marked
[taught in this unit] or [taught LATER] by table position. For es-es / es-latam
(one registry, shared exercise ids) it ends with the exercises whose content
differs between the two courses, since one decision covers both.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LEVELS = ["A1", "A2", "B1", "B2", "C1", "C2"]
HIDE = {"id", "teaches", "category", "distractor_skills", "stage", "explanation",
        "feedback", "tts", "audio", "difficulty"}


def load(p):
    return json.loads(Path(p).read_text(encoding="utf-8"))


def stem_positions(course, level):
    order, screen = {}, {}
    for u in load(course / "curriculum" / "units" / f"{level}.json"):
        for stem in u["stems"]:
            order[stem] = len(order)
            lp = course / "lessons" / level / f"{stem}.json"
            if lp.exists():
                for sec in load(lp).get("sections", []):
                    if sec.get("type") == "grammar" and sec.get("ref"):
                        screen.setdefault(Path(sec["ref"]).stem, stem)
    return order, screen


def main():
    lang, level, uid = sys.argv[1], sys.argv[2].lower(), sys.argv[3]
    course = ROOT / "content" / lang
    table = load(course / "curriculum" / "units" / f"{level}.json")
    idx = next(i for i, u in enumerate(table) if u["id"] == uid)
    unit = table[idx]
    print(f"# Unit {uid} ({unit.get('title', '')}), stems {unit['stems']}\n")

    for stem in unit["stems"]:
        lp = course / "lessons" / level / f"{stem}.json"
        if not lp.exists():
            continue
        lesson = load(lp)
        print(f"## Lesson {stem}: {lesson.get('title', '')}")
        for sec in lesson.get("sections", []):
            if sec.get("type") == "goal":
                print("  goals:", "; ".join(sec.get("items", [])))
            ref = sec.get("ref")
            if sec.get("type") == "grammar" and ref:
                g = load(course / ref)
                print(f"  [grammar screen {Path(ref).stem}] {g.get('title', '')}")
                for s in g.get("sections", []):
                    body = s.get("content") or s.get("rows") or s.get("items")
                    print("    ", json.dumps(body, ensure_ascii=False)[:700])
            if sec.get("type") == "vocabulary" and ref and (course / ref).exists():
                v = load(course / ref)
                items = v.get("words") or v.get("items") or v.get("vocabulary") or []
                words = [f"{w.get('lemma') or w.get('word') or w.get('hu') or w.get('term')}={w.get('translation') or w.get('en') or w.get('meaning')}"
                         for w in items if isinstance(w, dict)]
                print("  [vocabulary]", "; ".join(words))
        print()

    print("## Exercises\n")
    for stem in unit["stems"]:
        ep = course / "exercises" / level / f"{stem}-ex.json"
        if not ep.exists():
            continue
        print(f"### {stem}")
        for e in load(ep).get("exercises", []):
            rest = {k: v for k, v in e.items() if k not in HIDE}
            print(f"{e['id']} [{e.get('category')}/{e.get('stage', '')}] T={e.get('teaches')} DS={e.get('distractor_skills', '')}")
            print("   ", json.dumps(rest, ensure_ascii=False))
        print()

    reg = load(ROOT / "skills" / f"{lang.split('-')[0]}.json")["skills"]
    upto = LEVELS[: LEVELS.index(level.upper()) + 1]
    print("## Grammar skills at or below this level (slug | taught_in | title)")
    rows = [(k, v) for k, v in reg.items()
            if v.get("kind") == "grammar" and v.get("level") in upto and not v.get("retired")]
    order, screen = stem_positions(course, level)
    mine = {order[s] for s in unit["stems"]}
    for k, v in sorted(rows, key=lambda kv: (LEVELS.index(kv[1]["level"]), order.get(screen.get(kv[1].get("taught_in")), 999), kv[1].get("taught_in") or "")):
        pos = order.get(screen.get(v.get("taught_in")))
        mark = "" if pos is None or v["level"] != level.upper() else (" [taught in this unit]" if pos in mine else (" [taught LATER]" if pos > max(mine) else ""))
        print(f"  {k} | {v.get('taught_in')} | {v.get('title')}{mark}")
    print("\n## Vocabulary skills of this and earlier units")
    earlier = {u["id"] for u in table[: idx + 1]}
    for k, v in reg.items():
        if v.get("kind") == "vocabulary" and v.get("unit") in earlier and v.get("level") == level.upper():
            print(f"  {k}")

    other = {"es-es": "es-latam", "es-latam": "es-es"}.get(lang)
    if other:
        print(f"\n## Exercises whose content differs between {lang} and {other} (one decision covers both; the tag must fit both)")
        n = 0
        for stem in unit["stems"]:
            a = course / "exercises" / level / f"{stem}-ex.json"
            b = ROOT / "content" / other / "exercises" / level / f"{stem}-ex.json"
            if not (a.exists() and b.exists()):
                continue
            theirs = {e["id"]: e for e in load(b).get("exercises", [])}
            for e in load(a).get("exercises", []):
                o = theirs.get(e["id"])
                mine = {k: v for k, v in e.items() if k not in HIDE}
                if o is None:
                    print(f"{e['id']}: ONLY in {lang}")
                elif mine != {k: v for k, v in o.items() if k not in HIDE}:
                    n += 1
                    print(e["id"])
                    print(f"   {lang}: {json.dumps(mine, ensure_ascii=False)}")
                    print(f"   {other}: {json.dumps({k: v for k, v in o.items() if k not in HIDE}, ensure_ascii=False)}")
        print(f"({n} differ)")


if __name__ == "__main__":
    main()
