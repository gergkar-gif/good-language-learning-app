"""Build a fix worksheet from check-content.py findings (ROADMAP 152, release gates).

    python scripts/make_worksheet.py <out.txt> <course>:<level> [<course>:<level> ...] \
        [--checks length-giveaway,tell-absolute,tell-time-word] [--block-size 80] [--exclude id,id,...]

One entry per exercise. Identical copies (lesson + consolidation, es-es + es-latam)
are ONE entry: `files:` lists every copy, and every copy gets the same change.
Entries are grouped into blocks of about --block-size, never splitting a unit.
"""
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LINE = re.compile(r"^ERROR\s+(\S+)\s+(\S+)\s+(.*?)\s+\((content/[^)]+)\)\s*$")

HEADER = """# {title}
#
# One entry per exercise. Identical copies (lesson + consolidation file, and
# es-es + es-latam) are ONE entry; `files:` lists every copy and every copy
# gets the same change. `lesson:` is the lesson the exercise belongs to: read
# it (and the grammar it references) before deciding.
#
# `checks:` says why the entry is here:
#   length-giveaway  the correct option is over 1.3x the longest wrong one
#   tell-absolute    only wrong options carry an absolute (always, never,
#                    only, nobody, completely ...)
#   tell-time-word   only wrong options carry a time word (yesterday,
#                    tomorrow, last year ...)
#
# Fill in `decision:` for EVERY entry in a block BEFORE you edit that block:
#   shorten: <the new correct option, in full>
#   match: <each new wrong option, in full, separated by " || ">
#   keep               -> only for tell-absolute / tell-time-word: the word is
#                         the point of the exercise or can't be used to rule the
#                         option out (say why); never for length-giveaway
#   log                -> you are not certain; add it to the review-questions
#                         file, change nothing
# then one short line `why:` saying why the result has exactly one right
# answer AND why every option you wrote is correct, or wrong for exactly the
# reason you intend. The reviewer diffs every changed option against this file.
"""


def findings(course, level, checks):
    out = subprocess.run([sys.executable, str(ROOT / "scripts/check-content.py"), course, level],
                         capture_output=True, text=True, encoding="utf-8", cwd=ROOT).stdout
    for line in out.splitlines():
        m = LINE.match(line)
        if m and m.group(1) in checks:
            yield m.group(1), m.group(2), m.group(4)


def exercise(path, eid):
    for e in json.loads((ROOT / path).read_text(encoding="utf-8")).get("exercises", []):
        if e.get("id") == eid:
            return e
    raise KeyError(f"{path} :: {eid}")


def lesson_of(path, eid):
    """The lesson file whose exercise groups reference eid from this exercise file."""
    p = Path(path)
    course, level = p.parts[1], p.parts[3]
    ref = "/".join(p.parts[2:])
    for lf in sorted((ROOT / "content" / course / "lessons" / level).glob("*.json")):
        d = json.loads(lf.read_text(encoding="utf-8"))
        for s in d.get("sections", []):
            if s.get("ref") == ref and eid in (s.get("exerciseRefs") or []):
                return lf.relative_to(ROOT).as_posix()
    return "(not referenced by a lesson)"


def render(e):
    lines = []
    for turn in e.get("prompt") or []:
        if isinstance(turn, dict):
            lines.append(f"{turn.get('speaker', '')}: {turn.get('text', '')}")
    if e.get("question"):
        lines.append(e["question"])
    if e.get("audio_text") or e.get("text"):
        lines.append(f"(audio) {e.get('audio_text') or e.get('text')}")
    for i, o in enumerate(e.get("options") or []):
        lines.append(f"{'*' if i == e.get('correct') else '-'} {o}")
    return lines


def main():
    args = sys.argv[1:]
    checks = {"length-giveaway", "tell-absolute", "tell-time-word"}
    block = 80
    exclude = set()
    if "--exclude" in args:
        i = args.index("--exclude"); exclude = set(args[i + 1].split(",")); del args[i:i + 2]
    if "--checks" in args:
        i = args.index("--checks"); checks = set(args[i + 1].split(",")); del args[i:i + 2]
    if "--block-size" in args:
        i = args.index("--block-size"); block = int(args[i + 1]); del args[i:i + 2]
    out, targets = Path(args[0]), args[1:]

    entries = {}  # key -> entry
    for t in targets:
        course, level = t.split(":")
        for check, eid, path in findings(course, level, checks):
            if eid in exclude:
                continue
            e = exercise(path, eid)
            body = {k: e.get(k) for k in ("type", "prompt", "question", "options", "correct")}
            key = (eid, json.dumps(body, ensure_ascii=False, sort_keys=True))
            ent = entries.setdefault(key, {"id": eid, "e": e, "files": [], "checks": [], "lesson": None})
            if path not in ent["files"]:
                ent["files"].append(path)
            if check not in ent["checks"]:
                ent["checks"].append(check)
            ent["lesson"] = ent["lesson"] or lesson_of(path, eid)

    # Order by level then unit (the lesson stem), then id.
    def unit(ent):
        return re.sub(r"-(\d+|consolidation|[a-z])$", "", Path(ent["lesson"]).stem)
    ordered = sorted(entries.values(), key=lambda x: (Path(x["files"][0]).parts[3], x["lesson"], x["id"]))

    blocks, cur, last_unit = [], [], None
    for ent in ordered:
        u = (Path(ent["files"][0]).parts[3], unit(ent))
        if len(cur) >= block and u != last_unit:
            blocks.append(cur); cur = []
        cur.append(ent); last_unit = u
    if cur:
        blocks.append(cur)

    w = [HEADER.format(title=f"Release-gate worksheet: {', '.join(targets)}")]
    for n, b in enumerate(blocks, 1):
        lv = sorted({Path(x["files"][0]).parts[3] for x in b})
        w.append(f"\n########## Block {n}: {' + '.join(lv)} ({len(b)} exercises) ##########\n")
        for ent in b:
            e = ent["e"]
            w.append(f"### {ent['id']}   teaches: {e.get('teaches')}")
            w.append(f"checks: {', '.join(sorted(ent['checks']))}")
            w.append("files: " + ", ".join(ent["files"]))
            w.append(f"lesson: {ent['lesson']}")
            w += render(e)
            w += ["decision: ", "why: ", ""]
    out.write_text("\n".join(w), encoding="utf-8")
    counts = {c: sum(c in x["checks"] for x in entries.values()) for c in sorted(checks)}
    print(f"{out}: {len(entries)} entries in {len(blocks)} blocks; " +
          ", ".join(f"{c} {n}" for c, n in counts.items()))


if __name__ == "__main__":
    main()
