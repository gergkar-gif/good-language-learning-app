#!/usr/bin/env python3
"""Fill the ES C1 writer and reader prompts for a batch (2026-11-18).

Writer mode writes, into <worktree>/.scratch/:
- brief-<unit id>.md: scripts/templates/new-spanish-c1.txt filled for one unit;
- writer.md: the order of work for a writer of one or more units (each unit
  finished, checked and locked before the next; its knowledge sheet generated
  only when it starts, so it sees the units before it).

The unit notes come from imports/review/es-c1-plan/notes/<unit id>.md: a first
line "Genre: <genre>", then the notes (lesson plan, words, text) as {EXTRA}.
{NOTMET} lists every C1 skill taught after the unit, and every skill of an
earlier unit that has no lesson file in the worktree and is not one of this
writer's own units (written in parallel by another writer).

Reader mode writes <worktree>/.scratch/reader-prompt.md from
scripts/templates/read-spanish-c1.txt for the given units; --norm-notes names a
file with the reviewer's notes on the screens' normative claims.

    python scripts/fill_c1_prompts.py writer <worktree> <unit id> [<unit id> ...]
    python scripts/fill_c1_prompts.py reader <worktree> --norm-notes <file> <unit id> [...]
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COURSE, LEVEL = "es-latam", "c1"


def load(w):
    table = json.loads((w / f"content/{COURSE}/curriculum/units/{LEVEL}.json").read_text(encoding="utf-8"))
    skills = json.loads((w / "skills/es.json").read_text(encoding="utf-8"))["skills"]
    frozen = json.loads((w / "skills/frozen-es.json").read_text(encoding="utf-8"))["skills"]
    return table, skills, frozen


def screen_of(slug, skills, frozen):
    if skills[slug].get("taught_in"):
        return skills[slug]["taught_in"]
    m = re.search(r"planned taught_in (\S+)", frozen.get(slug, ""))
    return m.group(1) if m else None


def unit_index(table, stem):
    for i, u in enumerate(table):
        if stem in u["stems"]:
            return i
    return None


def notmet(w, table, skills, frozen, idx, own=()):
    lines = []
    for slug, sk in skills.items():
        if sk.get("kind") != "grammar" or sk.get("level") != "C1":
            continue
        scr = screen_of(slug, skills, frozen)
        stem = re.sub(r"-[a-z]-gr$|-gr$", "", scr or "")
        j = unit_index(table, stem)
        if j is None or j == idx:
            continue
        if j > idx:
            lines.append(f"- `{slug}`: {sk['title']} (taught at {scr}, Unit {j + 1})")
        elif table[j]["id"] not in own and not (w / f"content/{COURSE}/lessons/{LEVEL}/{table[j]['stems'][0]}.json").exists():
            lines.append(f"- `{slug}`: {sk['title']} (Unit {j + 1}, being written at the same time by another writer: "
                         "not met for you; don't use it or present it)")
    return "\n".join(sorted(lines)) or "- (none)"


def notes(uid):
    p = ROOT / f"imports/review/es-c1-plan/notes/{uid}.md"
    if not p.exists():
        sys.exit(f"no unit notes: {p.relative_to(ROOT)}")
    text = p.read_text(encoding="utf-8").strip()
    first, _, rest = text.partition("\n")
    m = re.match(r"Genre:\s*(.+)", first)
    if not m:
        sys.exit(f"{p.name}: first line must be 'Genre: …'")
    return m.group(1).strip(), rest.strip()


def writer(w, uids):
    table, skills, frozen = load(w)
    tpl = (ROOT / "scripts/templates/new-spanish-c1.txt").read_text(encoding="utf-8")
    by_id = {u["id"]: i for i, u in enumerate(table)}
    order = []
    for uid in uids:
        if uid not in by_id:
            sys.exit(f"no unit {uid!r}")
        i = by_id[uid]
        u = table[i]
        num, n2 = i + 1, f"{i + 1:02d}"
        genre, extra = notes(uid)
        stems = u["stems"]
        vals = {"{W}": str(w), "{SHEET}": f".scratch/sheet-{uid}.md", "{NUM}": str(num), "{N2}": n2,
                "{UID}": uid, "{TITLE}": u["title"], "{S}": f"c1-{n2}", "{GENRE}": genre,
                "{STEMS}": ",".join(stems), "{STEMS_SP}": " ".join(stems),
                "{NOTMET}": notmet(w, table, skills, frozen, i, set(uids)), "{EXTRA}": extra,
                "{CHALLENGES}": f".scratch/challenges-{uid}.json", "{REPORT}": f".scratch/report-{uid}.md"}
        t = tpl
        for k, v in vals.items():
            t = t.replace(k, v)
        left = re.findall(r"\{[A-Z_0-9]+\}", t)
        if left:
            sys.exit(f"unfilled {left} in brief for {uid}")
        (w / ".scratch").mkdir(exist_ok=True)
        (w / f".scratch/brief-{uid}.md").write_text(t, encoding="utf-8")
        order.append((num, uid))
    steps = [f"You are writing {len(order)} new unit(s) of the Spanish C1 core of the Parlour language app, one after the "
             f"other, in the git worktree `{w}`. DO NOT COMMIT. Each unit has its own full brief; follow it exactly.", "",
             "Do the units in this order, and finish each one completely (all its checks clean, tags locked, report "
             "written) before you start the next: a later unit builds on the earlier ones (their words are known, "
             "their skills recapped, never re-taught or re-listed).", ""]
    for num, uid in order:
        steps += [f"## Unit {num} `{uid}`",
                  f"1. From `{w}`: `python scripts/set_planned_taught_in.py es c1 {uid}`, `python3 build-manifest.py`, "
                  f"`python scripts/build_word_lesson_index.py es-latam`, then "
                  f"`python scripts/prior_knowledge.py es-latam c1 {uid} --out .scratch/sheet-{uid}.md` (the knowledge "
                  "sheet; generate it only now, so it includes the units you have just finished).",
                  f"2. Read and follow `{w}/.scratch/brief-{uid}.md`.",
                  f"3. Write that unit's report to `{w}/.scratch/report-{uid}.md` before starting the next unit.", ""]
    steps += ["Your final reply: each unit's full report, in order (the files may be refused to a subagent, so make the "
              "reply complete), and the token-heavy parts you would cut next time."]
    (w / ".scratch/writer.md").write_text("\n".join(steps) + "\n", encoding="utf-8")
    print(f"wrote {w}/.scratch/writer.md and {len(order)} brief(s)")


def reader(w, uids, norm_file):
    table, *_ = load(w)
    by_id = {u["id"]: i for i, u in enumerate(table)}
    lines = []
    for k, uid in enumerate(uids, 1):
        i = by_id[uid]
        stems = table[i]["stems"]
        n2 = f"{i + 1:02d}"
        lines.append(f"- Unit {i + 1} `{uid}` (C1 core Unit {i + 1}): stems {', '.join(stems)}; story stem c1-{n2} "
                     f"(`content/es-latam/stories/original/c1/c1-{n2}.json`); knowledge sheet `.scratch/sheet-{uid}.md` "
                     f"(generate it first: `python scripts/prior_knowledge.py es-latam c1 {uid} --out .scratch/sheet-{uid}.md`); "
                     f"fixes file `.scratch/fixes-{uid}.json`.")
    words = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five"}
    t = (ROOT / "scripts/templates/read-spanish-c1.txt").read_text(encoding="utf-8")
    vals = {"{UNIT_LINES}": "\n".join(lines), "{N_WORD}": words.get(len(uids), str(len(uids))),
            "{LEVEL_UP}": "C1", "{LEVEL}": "c1", "{REPORT}": ".scratch/reader-report.md",
            "{NORM_NOTES}": Path(norm_file).read_text(encoding="utf-8").strip(), "{W}": str(w)}
    for k, v in vals.items():
        t = t.replace(k, v)
    left = re.findall(r"\{[A-Z_0-9]+\}", t)
    if left:
        sys.exit(f"unfilled {left}")
    (w / ".scratch").mkdir(exist_ok=True)
    (w / ".scratch/reader-prompt.md").write_text(t, encoding="utf-8")
    print(f"wrote {w}/.scratch/reader-prompt.md")


def main(argv):
    if len(argv) < 3 or argv[0] not in ("writer", "reader"):
        sys.exit(__doc__)
    mode, w = argv[0], Path(argv[1]).resolve()
    rest = argv[2:]
    if mode == "writer":
        writer(w, rest)
    else:
        if "--norm-notes" not in rest:
            sys.exit("reader mode needs --norm-notes <file>")
        i = rest.index("--norm-notes")
        norm = rest[i + 1]
        reader(w, rest[:i] + rest[i + 2:], norm)


if __name__ == "__main__":
    main(sys.argv[1:])
