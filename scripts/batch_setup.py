"""Set up one read batch of the Spanish pass (docs/unit-pipeline-log.md
§ "Pipeline", route A): what the reviewer used to assemble by hand at the
start of every batch.

    python scripts/batch_setup.py <level> <batch dir> A=<n>,<n>,<n> [B=<n>,...]
        [--focus focus.txt] [--no-worktrees]

Unit numbers are 1-based positions in content/es-es/curriculum/units/<level>.json.
For each reader (A, B) it:

- adds the worktree /home/user/parlour-read-<a|b> from origin/master (unless
  it exists or --no-worktrees);
- writes the knowledge sheet prior-<unit id>.md of each unit into it;
- writes <batch dir>/prompt-<a|b>.txt from scripts/templates/read-spanish.txt,
  with {FOCUS} replaced by the text of --focus (the batch's unit notes);

and writes <batch dir>/setup.md: start time, base commit, pairing, stories
per unit, baseline check-content counts per unit and course, and the files
that differ between es-es and es-latam (the reviewer reads those, and the
es-latam stories, after mirroring).
"""
import datetime
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COURSES = ("es-es", "es-latam")
WORDS = {1: "ONE", 2: "TWO", 3: "THREE", 4: "FOUR"}


def read(p):
    return json.loads(Path(p).read_text(encoding="utf-8")) if Path(p).is_file() else None


def run(cmd, cwd=ROOT):
    return subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, encoding="utf-8")


def unit_files(course, level, stems):
    """Every content file a unit's lessons reference, plus the lesson files."""
    files = []
    for s in stems:
        lp = f"content/{course}/lessons/{level}/{s}.json"
        files.append(lp)
        for sec in (read(ROOT / lp) or {}).get("sections", []):
            if sec.get("ref"):
                files.append(f"content/{course}/{sec['ref']}")
    return list(dict.fromkeys(files))


def stories(course, level, stems):
    out = []
    for f in unit_files(course, level, stems):
        m = re.search(r"/stories/.*/([^/]+)\.json$", f)
        if m:
            out.append(m.group(1))
    return out


def counts(course, level, uid):
    r = run([sys.executable, "scripts/check-content.py", course, level, uid])
    m = re.search(r"(\d+) error\(s\), (\d+) suspect\(s\)", r.stdout)
    return f"{m.group(1)} / {m.group(2)}" if m else "?"


def main():
    args = sys.argv[1:]
    focus, worktrees = "", True
    if "--focus" in args:
        i = args.index("--focus")
        focus = Path(args[i + 1]).read_text(encoding="utf-8").strip()
        del args[i:i + 2]
    if "--no-worktrees" in args:
        args.remove("--no-worktrees")
        worktrees = False
    if len(args) < 3:
        sys.exit(__doc__)
    level, batch = args[0].lower(), Path(args[1])
    readers = {}
    for a in args[2:]:
        k, v = a.split("=")
        readers[k.upper()] = [int(x) for x in v.split(",")]
    units = read(ROOT / f"content/es-es/curriculum/units/{level}.json")
    latam_ids = {u["id"] for u in read(ROOT / f"content/es-latam/curriculum/units/{level}.json") or []}
    template = (ROOT / "scripts/templates/read-spanish.txt").read_text(encoding="utf-8")
    batch.mkdir(parents=True, exist_ok=True)
    base = run(["git", "rev-parse", "--short", "origin/master"]).stdout.strip()
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    setup = [f"# es {level.upper()} batch: {batch.name}", "",
             f"Started {now} from origin/master {base}. "
             f"{len(readers)} Sonnet reader(s); es-es read once, fixes mirrored to es-latam.", ""]
    table = ["| Unit | es-es | es-latam |", "|---|---|---|"]
    differ = []
    for key, nums in readers.items():
        w = Path(f"/home/user/parlour-read-{key.lower()}")
        if worktrees and not w.exists():
            r = run(["git", "worktree", "add", "--detach", str(w), "origin/master"])
            if r.returncode:
                sys.exit(r.stderr)
        lines, desc = [], []
        for n in nums:
            u = units[n - 1]
            uid, stems = u["id"], u["stems"]
            st = stories("es-es", level, stems)
            sheet = w / f"prior-{uid}.md"
            r = run([sys.executable, "scripts/prior_knowledge.py", "es-es", level, uid, "--out", str(sheet)],
                    cwd=w if w.exists() else ROOT)
            if r.returncode:
                sys.exit(r.stderr)
            story_txt = ", ".join(f"`{s}`" for s in st) or "none"
            lines.append(f"- `es-es {level} {uid}` ({level.upper()} Unit {n}): lessons {' '.join(stems)}, "
                         f"stories {story_txt}. Knowledge sheet: `{w}/prior-{uid}.md`. "
                         f"Fixes file: `{w}/fixes-{uid}.json`. Challenges file: `{w}/challenges-{uid}.json`.")
            desc.append(f"Unit {n} {uid} ({' '.join(stems)}; stories {st})")
            table.append(f"| {n} {uid} | {counts('es-es', level, uid)} | "
                         f"{counts('es-latam', level, uid) if uid in latam_ids else 'no es-latam unit'} |")
            if uid in latam_ids:
                diff = []
                for f in unit_files("es-es", level, stems):
                    g = f.replace("content/es-es/", "content/es-latam/", 1)
                    a, b = ROOT / f, ROOT / g
                    if not b.is_file():
                        diff.append(Path(f).name + " (no es-latam file)")
                    elif a.read_bytes() != b.read_bytes():
                        diff.append(Path(f).name)
                differ.append(f"- {uid}: {', '.join(diff) or 'none'}")
            else:
                differ.append(f"- {uid}: es-es only")
        setup.append(f"- Reader {key}: " + "; ".join(desc))
        first = units[nums[0] - 1]["id"]
        prompt = (template.replace("{N_WORD}", WORDS.get(len(nums), str(len(nums))))
                  .replace("{LEVEL_UP}", level.upper()).replace("{LEVEL}", level)
                  .replace("{W}", str(w)).replace("{UNIT_LINES}", "\n".join(lines))
                  .replace("{REPORT}", f"report-{first}.md").replace("{FOCUS}", focus))
        if len(nums) == 1:
            prompt = prompt.replace("units of the", "unit of the").replace("with them", "with it")
        left = re.findall(r"\{[A-Z_]+\}", prompt)
        if left:
            sys.exit(f"unfilled placeholders: {left}")
        (batch / f"prompt-{key.lower()}.txt").write_text(prompt, encoding="utf-8")
    setup += ["", "## Baseline check-content, errors / suspects", ""] + table
    setup += ["", "## Files differing es-es vs es-latam", ""] + differ + [""]
    (batch / "setup.md").write_text("\n".join(setup), encoding="utf-8")
    print((batch / "setup.md").read_text(encoding="utf-8"))


if __name__ == "__main__":
    main()
