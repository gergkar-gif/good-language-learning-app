#!/usr/bin/env python3
"""Find ES C1 forms used before the C1 screen that teaches them (2026-11-18).

check-content's `taught-later` sees tags only: a C1 form in a story, a screen
example, a wrong option or an item tagged with another skill passes it. This
lists every hit of a C1 form in a file that comes before the form's screen
(its `taught_in` in skills/es.json, or the planned screen recorded in
skills/frozen-es.json while the screen is unwritten). Only forms a pattern
can find without guessing are listed; the other C1 skills (rumour
conditional, headline style, clitic dislocation, aspectual *se*, …) are left
to the tags and the reader.

    python scripts/check_es_c1_forms.py <course> [level ...] [--track core]

Levels default to all; --track limits the search to one track's units.

Exit status 1 when anything is found. A hit in a deliberate wrong option, a
quotation or a frozen lower level is still listed: decide it by hand.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LEVELS = ["a1", "a2", "b1", "b2", "c1"]
W = r"[a-záéíóúüñ]"
FORMS = {
    "futuro-subjuntivo-reconocimiento":
        rf"\b(?:fuere|fueren|hubiere|hubieren|tuviere|estuviere|hiciere|dijere|pudiere|quisiere|supiere|viniere"
        rf"|{W}+(?<!f)(?<!g)(?<!qu)(?<!h)(?<!r)iere(?:n|s)?)\b",
    "infinitivo-compuesto-nominal": r"\b(?:el|al|tras|por|sin) haber(?:lo|la|los|las|le|les|se)? " + W + r"+(?:ado|ido|to|cho)\b",
    "relativos-el-cual": r"\b(?:el|la|los|las|lo) cual(?:es)?\b",
    "comparativas-de-lo-que": r"\b(?:más|menos|mejor|peor|mayor|menor) de (?:lo|la|el|los|las) que\b",
    # evaluative only: *con lo cansado que está*, *para lo poco que cobra*; a bare
    # *para lo que necesites* is a relative and is not listed
    "con-lo-que-para-lo-que": r"\b(?:con|para) lo " + W + r"+ que\b",
    "ni-que-exclamativo": r"\bni que " + W + r"+(?:ra|ras|ran|se|ses|sen)\b",
}
PAT = {k: re.compile(v, re.IGNORECASE) for k, v in FORMS.items()}
SKIP_KEYS = {"english", "explanation", "translation", "id", "ref", "teaches", "distractor_skills",
             "exerciseRefs", "title_en", "questionEnglish", "optionsEnglish"}


def read(p):
    try:
        return json.loads(Path(p).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None


def strings(node, path=""):
    if isinstance(node, str):
        yield path, node
    elif isinstance(node, dict):
        for k, v in node.items():
            if k not in SKIP_KEYS:
                yield from strings(v, f"{path}.{k}" if path else k)
    elif isinstance(node, list):
        for i, v in enumerate(node):
            yield from strings(v, f"{path}[{i}]")


def screen_of(slug, skill, frozen):
    if skill.get("taught_in"):
        return skill["taught_in"]
    m = re.search(r"planned taught_in (\S+)", frozen.get(slug, ""))
    return m.group(1) if m else None


def main(argv):
    if not argv:
        sys.exit(__doc__)
    track = None
    if "--track" in argv:
        i = argv.index("--track")
        track = argv[i + 1]
        argv = argv[:i] + argv[i + 2:]
    course, levels = argv[0], [a.lower() for a in argv[1:]] or LEVELS
    skills = read(ROOT / "skills/es.json")["skills"]
    frozen = read(ROOT / "skills/frozen-es.json")["skills"]
    base = ROOT / "content" / course

    order = {}          # stem -> position, every level and track in unit-table order
    wanted = set()      # stems of the --track (all stems without it)
    for lv in LEVELS:
        for u in read(base / f"curriculum/units/{lv}.json") or []:
            for st in u.get("stems", []):
                order.setdefault(st, len(order))
                if track is None or u.get("track", "core") == track:
                    wanted.add(st)

    def stem(name):
        best = None
        for st in order:
            if name == st or name.startswith(st + "-"):
                if best is None or len(st) > len(best):
                    best = st
        return best

    limits = {}
    for slug in FORMS:
        scr = screen_of(slug, skills.get(slug, {}), frozen)
        st = stem(scr) if scr else None
        if st is None:
            print(f"warning: {slug}: no screen position known ({scr!r})")
            continue
        limits[slug] = (order[st], scr)

    hits = []
    for lv in levels:
        files = []
        for folder, suffix in (("lessons", ".json"), ("exercises", "-ex.json"), ("grammar", "-gr.json"),
                               ("vocabulary", "-voc.json")):
            files += sorted((base / folder / lv).glob(f"*{suffix}"))
        files += sorted((base / "stories").glob(f"*/{lv}/*.json"))
        story_stem = {}
        for lf in sorted((base / "lessons" / lv).glob("*.json")):
            for s in (read(lf) or {}).get("sections", []):
                if s.get("type") == "story" and s.get("ref"):
                    story_stem[s["ref"]] = lf.stem
        for f in files:
            rel = f.relative_to(base).as_posix()
            st = story_stem.get(rel) or stem(f.stem)
            if st is None or st not in wanted:
                continue
            data = read(f)
            for path, text in strings(data):
                for slug, rx in PAT.items():
                    if slug in limits and order[st] < limits[slug][0]:
                        m = rx.search(text)
                        if m:
                            hits.append((slug, limits[slug][1], f.relative_to(ROOT).as_posix(), path, m.group(0), text))
        chall = (read(base / "curriculum/challenges.json") or {}).get("challenges", {})
        for key, entry in chall.items():
            if key.split("-")[0] != lv or key not in wanted:
                continue
            for path, text in strings(entry):
                for slug, rx in PAT.items():
                    if slug in limits and order[key] < limits[slug][0] and rx.search(text):
                        hits.append((slug, limits[slug][1], f"content/{course}/curriculum/challenges.json",
                                     f"{key}.{path}", rx.search(text).group(0), text))

    for slug, scr, f, path, m, text in hits:
        print(f"{slug} (taught at {scr}): {f} :: {path}: *{m}* … {text[:110]!r}")
    counts = {}
    for h in hits:
        counts[h[0]] = counts.get(h[0], 0) + 1
    print(f"{len(hits)} hit(s) before their screen" + (f": {counts}" if counts else ""))
    return 1 if hits else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
