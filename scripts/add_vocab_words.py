"""Turn a list of words for vocabulary lists into text fixes for
apply_replacements.py (ROADMAP 153, HU B1 citizenship track: unmet words
go on the vocabulary list of the first lesson that uses them, 60-100 a
batch; user, 2026-10-22).

    python scripts/add_vocab_words.py <course> <level> <words.txt> <out.json>

Each line of words.txt is `lesson stem | lemma | translation | pos`
(lines starting with # are skipped). It appends each word to
content/<course>/vocabulary/<level>/<stem>-voc.json in that file's own
style (one entry per line or one field per line), skips a lemma the file
already lists, and refuses rather than guesses: an unknown stem, a pos the
vocabulary schema rejects, or a file whose closing bracket it can't find
(batch cit-16-22: a hand-made list put `determiner` on *mindkét*).
Apply the output with apply_replacements.py, then rebuild the word index
(build_word_lesson_index.py) before rerunning unmet-words.js.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main():
    if len(sys.argv) != 5:
        sys.exit(__doc__)
    course, level, src, out = sys.argv[1], sys.argv[2].lower(), Path(sys.argv[3]), Path(sys.argv[4])
    schema = json.loads((ROOT / f"content/{course}/schemas/vocabulary.schema.json").read_text(encoding="utf-8"))
    pos_re = re.compile(schema["definitions"]["word"]["properties"]["pos"]["pattern"])
    rows, problems = {}, []
    for n, line in enumerate(src.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        parts = [p.strip() for p in line.split("|")]
        if len(parts) != 4 or not all(parts):
            problems.append(f"line {n}: want 'stem | lemma | translation | pos': {line}")
            continue
        stem, lemma, tr, pos = parts
        if not pos_re.fullmatch(pos):
            problems.append(f"line {n}: pos {pos!r} is not allowed by the vocabulary schema")
        elif " " in lemma and pos != "expression":
            problems.append(f"line {n}: {lemma!r} is more than one word, so its pos is 'expression' (schema)")
        if not (ROOT / f"content/{course}/vocabulary/{level}/{stem}-voc.json").is_file():
            problems.append(f"line {n}: no vocabulary file for {stem}")
        rows.setdefault(stem, []).append((lemma, tr, pos))
    if problems:
        sys.exit("refused, nothing written:\n  " + "\n  ".join(problems))
    fixes = []
    for stem, items in rows.items():
        rel = f"content/{course}/vocabulary/{level}/{stem}-voc.json"
        text = (ROOT / rel).read_text(encoding="utf-8")
        have = {w["lemma"] for w in json.loads(text)["words"]}
        new, seen = [], set()
        for it in items:
            if it[0] not in have and it[0] not in seen:
                new.append(it)
                seen.add(it[0])
        if not new:
            continue
        m = list(re.finditer(r"\}\s*\n(\s*)\]\s*\n\}\s*$", text))
        if not m:
            sys.exit(f"refused, nothing written: can't find the end of the word list in {rel}")
        tail, ind = text[m[-1].start():], m[-1].group(1) + "  "
        q = lambda s: json.dumps(s, ensure_ascii=False)
        if '{ "lemma"' in text:
            add = "".join(f',\n{ind}{{ "lemma": {q(l)}, "translation": {q(t)}, "pos": {q(p)} }}' for l, t, p in new)
        else:
            add = "".join(f',\n{ind}{{\n{ind}  "lemma": {q(l)},\n{ind}  "translation": {q(t)},\n{ind}  "pos": {q(p)}\n{ind}}}'
                          for l, t, p in new)
        fixes.append({"file": rel, "old": tail, "new": "}" + add + tail[1:], "kind": "vocabulary", "id": stem})
    out.write_text(json.dumps(fixes, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"wrote {out}: {len(fixes)} file(s), {sum(len(v) for v in rows.values())} word(s) read")


if __name__ == "__main__":
    main()
