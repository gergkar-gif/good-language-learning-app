"""Find and fix fill-blanks whose blank is glued to a word (ROADMAP 153).

The citizenship generator wrote many fill-blanks with the blank inside a
word (*a Felvidék_____*, answer *en*): the learner types an ending, and
the word lookup sees fragments. The rulebook (§ 2.5) wants the whole word
blanked. Readers fixed most of them, but HU B1 batch cit-71-75 still had
31 left after the read. This makes the blank the whole word: stem +
answer + any letters after the blank, for `answer` and every `answers`
entry. It refuses (lists, changes nothing) when an item has no answer.

    python scripts/fix_glued_blanks.py <course> <level> [<stem prefix> ...] [--apply]

Without --apply it only lists what it would change. Check the hints
afterwards: a hint that named the ending ("with", "of the") should name
the word.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GLUED = re.compile(r"(\w*)_____(\w*)")


def main():
    args = [a for a in sys.argv[1:] if a != "--apply"]
    apply = "--apply" in sys.argv
    if len(args) < 2:
        sys.exit(__doc__)
    course, level, prefixes = args[0], args[1].lower(), args[2:]
    found, refused = [], []
    for f in sorted((ROOT / f"content/{course}/exercises/{level}").glob("*.json")):
        if prefixes and not any(f.name.startswith(p) for p in prefixes):
            continue
        data = json.loads(f.read_text(encoding="utf-8"))
        items = data if isinstance(data, list) else data.get("exercises", [])
        changed = False
        for x in items:
            m = GLUED.search(x.get("sentence") or "")
            if not m or not (m.group(1) or m.group(2)):
                continue
            pre, post = m.group(1), m.group(2)
            if not x.get("answer") and not x.get("answers"):
                refused.append(f"{x.get('id')}: no answer to join")
                continue
            if x.get("answers"):
                x["answers"] = [pre + a + post for a in x["answers"]]
                word = x["answers"][0]
            else:
                x["answer"] = word = pre + x["answer"] + post
            x["sentence"] = x["sentence"][:m.start()] + "_____" + x["sentence"][m.end():]
            found.append(f"{x.get('id')}: {x['sentence']}  -> {word}  (hint: {x.get('hint')})")
            changed = True
        if changed and apply:
            f.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("\n".join(found) or "no glued blanks")
    if refused:
        print("refused:\n  " + "\n  ".join(refused))
    if found and not apply:
        print(f"{len(found)} item(s); run again with --apply to write them")


if __name__ == "__main__":
    main()
