"""Put each Spanish course in its own words (user, 2026-10-16; ROADMAP 153).

es-es uses Spain's words, es-latam Latin America's (scripts/course_variants.py
lists them: *zumo/jugo, coche/carro, billete/boleto, camarero/mesero,
salón/sala* ...). This rewrites every target-language string of the given
levels (exercises, screens, lessons, vocabulary lists, stories, drills and
the levels' challenges) with `course_variants.convert`, which fixes the
article of a noun whose gender changes (*el salón* -> *la sala*).

It refuses rather than guesses, and lists each refusal for a hand fix:
a gendered word next to the noun (*la sala nueva*), or an option list that
would end up with the same option twice. Story text changes need the story's
narration audio regenerated (the report lists the stories).

    python scripts/fix_variant_vocab.py <course> <level> [<level> ...] [--write] [--report <file>]
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import course_variants as cv  # noqa: E402

# Keys that are never target-language text
SKIP = {"id", "ref", "type", "category", "teaches", "stage", "audio", "src", "path", "file", "speaker", "gender",
        "tone", "role", "voice", "lang", "pos", "cefr", "distractor_skills", "image", "icon", "level", "tier",
        "segments", "pacing", "speakers", "rate_str", "style"}
DIRS = ["exercises", "grammar", "lessons", "vocabulary", "stories", "drills"]


def load(p):
    text = p.read_text(encoding="utf-8")
    m = re.search(r'\n( +)"', text)
    return json.loads(text), (len(m.group(1)) if m else 2), text.endswith("\n")


def walk(node, course, path, changes, refused, skip=SKIP):
    """Convert strings; returns the new node. `speaker` is converted in exercises
    (the learner sees "Camarero:"), not in stories, where it names the narration voice."""
    if isinstance(node, str):
        new, ch, rf = cv.convert(node, course)
        for o, n in ch:
            changes.append((path, o, n))
        for r in rf:
            refused.append((path, r))
        return new
    if isinstance(node, list):
        out = [walk(v, course, f"{path}[{i}]", changes, refused, skip) for i, v in enumerate(node)]
        strs = [x for x in out if isinstance(x, str)]
        if len(strs) == len(out) and len(set(strs)) < len(set(x for x in node if isinstance(x, str))):
            refused.append((path, "the list would repeat an option: " + ", ".join(map(str, node))[:80]))
            del changes[len(changes) - sum(1 for c in changes if c[0].startswith(path + "[")):]
            return node
        return out
    if isinstance(node, dict):
        return {k: (v if k in skip else walk(v, course, f"{path}.{k}", changes, refused, skip)) for k, v in node.items()}
    return node


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    report = None
    if "--report" in sys.argv:
        report = Path(sys.argv[sys.argv.index("--report") + 1])
        args = [a for a in args if a != str(report) and a != sys.argv[sys.argv.index("--report") + 1]]
    if len(args) < 2 or args[0] not in ("es-es", "es-latam"):
        sys.exit(__doc__)
    course, levels, write = args[0], [a.lower() for a in args[1:]], "--write" in sys.argv
    base = ROOT / "content" / course
    files = [p for d in DIRS for lv in levels for p in sorted((base / d).rglob(f"{lv}/*.json"))]
    lines, n_changes, n_refused, stories = [], 0, 0, []
    for p in files:
        try:
            data, indent, nl = load(p)
        except (json.JSONDecodeError, UnicodeDecodeError):
            continue
        changes, refused = [], []
        new = walk(data, course, "", changes, refused, SKIP if "/stories/" in p.as_posix() else SKIP - {"speaker"})
        rel = p.relative_to(ROOT).as_posix()
        if changes or refused:
            lines.append(f"## {rel}")
            lines += [f"- {path}: {o} -> {n}" for path, o, n in changes]
            lines += [f"- REFUSED {path}: {r}" for path, r in refused]
        if changes:
            n_changes += len(changes)
            if "/stories/" in rel and any(".paragraphs" in c[0] for c in changes):
                stories.append(rel)
            if write:
                p.write_text(json.dumps(new, ensure_ascii=False, indent=indent) + ("\n" if nl else ""), encoding="utf-8")
        n_refused += len(refused)
    # challenges of the levels
    cp = base / "curriculum" / "challenges.json"
    if cp.is_file():
        data, indent, nl = load(cp)
        changes, refused = [], []
        ch = data.get("challenges", {})
        for k in list(ch):
            if any(k.startswith(lv + "-") for lv in levels):
                ch[k] = walk(ch[k], course, f".challenges.{k}", changes, refused)
        if changes or refused:
            lines.append(f"## {cp.relative_to(ROOT).as_posix()}")
            lines += [f"- {path}: {o} -> {n}" for path, o, n in changes]
            lines += [f"- REFUSED {path}: {r}" for path, r in refused]
            n_changes += len(changes)
            n_refused += len(refused)
            if write and changes:
                cp.write_text(json.dumps(data, ensure_ascii=False, indent=indent) + ("\n" if nl else ""), encoding="utf-8")
    head = (f"{course} {' '.join(levels)}: {n_changes} change(s) {'written' if write else 'to make'}, "
            f"{n_refused} refused; story text changed (needs new narration audio): {', '.join(stories) or 'none'}")
    if report:
        report.write_text(head + "\n\n" + "\n".join(lines) + "\n", encoding="utf-8")
    print(head)
    if not report:
        print("\n".join(lines))


if __name__ == "__main__":
    main()
