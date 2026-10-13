"""Resolve a challenges.json conflict from a cherry-pick or merge.

Two units written in parallel both add entries to
content/<course>/curriculum/challenges.json, so git conflicts on the file
even though no entry is shared. This takes our side (HEAD) and adds every
entry the incoming commit added or changed, refusing if both sides changed
the same entry differently, then stages the file.

    python scripts/merge_challenges.py <course> <incoming commit>
"""
import json
import re
import subprocess
import sys


def show(ref, path):
    return subprocess.check_output(["git", "show", f"{ref}:{path}"]).decode("utf-8")


def entries(doc):
    return doc.get("challenges", doc) if isinstance(doc, dict) else doc


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    course, commit = sys.argv[1], sys.argv[2]
    path = f"content/{course}/curriculum/challenges.json"
    ours_text = show("HEAD", path)
    ours, theirs, base = json.loads(ours_text), json.loads(show(commit, path)), json.loads(show(f"{commit}~1", path))
    o, t, b = entries(ours), entries(theirs), entries(base)
    incoming = {k: v for k, v in t.items() if b.get(k) != v}
    clash = [k for k in incoming if k in o and o[k] != b.get(k) and o[k] != incoming[k]]
    if clash:
        sys.exit(f"both sides changed: {', '.join(clash)}; resolve by hand")
    o.update(incoming)
    indent = len(re.search(r'\n( +)"', ours_text).group(1))
    with open(path, "w", encoding="utf-8") as f:
        f.write(json.dumps(ours, ensure_ascii=False, indent=indent) + "\n")
    subprocess.check_call(["git", "add", path])
    print(f"merged {len(incoming)} entr{'y' if len(incoming) == 1 else 'ies'}: {', '.join(incoming)}")


if __name__ == "__main__":
    main()
