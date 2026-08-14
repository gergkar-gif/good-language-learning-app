#!/usr/bin/env python3
"""
Add a parenthetical hint to fill-blank exercises whose blank is genuinely
unrecoverable without one.

Extends the fix already applied by hand to the a2-17 unit (see the
`known-issue-underspecified-fill-blanks` note) to the rest of the
`teaches`-tagged fill-blank pool `engine/recycle.js` draws from. Only
tense/conjugation-tagged exercises are considered — the established hint
convention (a parenthetical infinitive baked into the `sentence` string,
e.g. "Ayer __ en el festival. (bailar)") only makes sense for blanks that
are genuinely open verb-identity or verb-person choices. A first pass over
the full tagged pool found most blanks are fixed/memorized phrases or test
a connector/adverb/pronoun, not a verb — those are correctly left alone.

Two cases get a hint, both derived from `generated/indexes/verb-index.json`
(no new content authored, no guessing beyond one narrow regular-participle
fallback):

  1. The answer contains an identifiable content verb (e.g. "ha llegado",
     "remado") whose *identity* isn't recoverable from the sentence ->
     append " (infinitivo)".
  2. The answer is only a `haber` auxiliary (has/han/he/hemos...) with the
     participle already given in the sentence -> the ambiguity is the
     *subject*, not the verb -> append " (pronoun)" using the auxiliary's
     own person/number.

Exercises where neither resolves (connectors, question words, pronouns,
adverbs...) are left untouched on purpose.

Usage:
    python scripts/add_fillblank_hints.py
"""
import json
import re
from pathlib import Path

VERB_INDEX_PATH = Path("generated/indexes/verb-index.json")
EXERCISES_DIR = Path("content/es/exercises")

TENSE_KEYWORDS = re.compile(
    r"preterito|indefinido|imperfecto|subjuntivo|futuro|condicional|"
    r"gerundio|perfecto|pluscuamperfecto|imperativo|preterit",
    re.I,
)

AUX_HABER_LEMMA = "haber"
PERSON_PRONOUN = {
    (1, "singular"): "yo",
    (2, "singular"): "tú",
    (3, "singular"): "él/ella/usted",
    (1, "plural"): "nosotros",
    (2, "plural"): "vosotros",
    (3, "plural"): "ellos/ustedes",
}

TOKEN_RE = re.compile(r"[^a-zA-Zà-ÿñÑ]")


def load_verb_index():
    return json.loads(VERB_INDEX_PATH.read_text(encoding="utf-8"))


def clean_token(token):
    return TOKEN_RE.sub("", token).lower()


# Regular -ar participles ("remado" -> "remar") aren't all in the verb
# index — used only as a fallback, and only for -ado (unambiguous -ar),
# never -ido (ambiguous between -er and -ir, so left unresolved instead of
# guessed).
def regular_participle_fallback(token):
    if token.endswith("ado") and len(token) > 4:
        return token[:-2] + "r"
    return None


def resolve_hint(answer, verb_index):
    """Returns (hint_text, category) or (None, None)."""
    tokens = [clean_token(t) for t in answer.split()]
    tokens = [t for t in tokens if t]

    content_lemma = None
    aux_person = None

    for tok in tokens:
        readings = verb_index.get(tok, [])
        for r in readings:
            if r["lemma"] == AUX_HABER_LEMMA:
                if r.get("person") and aux_person is None:
                    aux_person = (r["person"], r["number"])
            elif content_lemma is None:
                content_lemma = r["lemma"]
        if not readings and content_lemma is None:
            fallback = regular_participle_fallback(tok)
            if fallback:
                content_lemma = fallback

    if content_lemma:
        return f"({content_lemma})", "infinitive"
    if aux_person and aux_person in PERSON_PRONOUN:
        return f"({PERSON_PRONOUN[aux_person]})", "pronoun"
    return None, None


def process_file(path, verb_index, stats):
    # Edits are applied as surgical text replacements on the raw file rather
    # than a full json.load/json.dump round-trip — re-serializing the whole
    # file would silently reformat every array in it (some source files hand
    # -write short arrays like `["a", "b"]` on one line; a full dump expands
    # them all to one-per-line), turning a one-line content fix into a
    # file-wide formatting diff. This keeps the diff to exactly the sentence
    # values that actually changed.
    raw = path.read_text(encoding="utf-8")
    data = json.loads(raw)
    exercises = data.get("exercises", [])

    edits = []       # (start, end, replacement) into `raw`, applied back-to-front
    search_from = 0

    for ex in exercises:
        ex_id = ex.get("id", "")
        id_marker = '"id": ' + json.dumps(ex_id, ensure_ascii=False)
        id_pos = raw.find(id_marker, search_from)
        if id_pos != -1:
            search_from = id_pos  # exercises appear in file order, ids are unique

        if ex.get("type") != "fill-blank":
            continue
        teaches = ex.get("teaches") or []
        if not any(TENSE_KEYWORDS.search(t) for t in teaches):
            continue
        sentence = ex.get("sentence", "")
        if "(" in sentence:
            continue
        answer = (ex.get("answer") or "").strip()
        if not answer:
            continue

        hint, category = resolve_hint(answer, verb_index)
        if not hint:
            stats["left_alone"] += 1
            continue

        new_sentence = sentence.rstrip() + " " + hint
        old_field = '"sentence": ' + json.dumps(sentence, ensure_ascii=False)
        new_field = '"sentence": ' + json.dumps(new_sentence, ensure_ascii=False)

        field_pos = raw.find(old_field, id_pos if id_pos != -1 else 0)
        if field_pos == -1:
            stats["errors"].append((path.name, ex_id))
            continue

        edits.append((field_pos, field_pos + len(old_field), new_field))
        stats[category] += 1
        stats["examples"].append((path.name, ex_id, new_sentence))

    if edits:
        new_raw = raw
        for start, end, replacement in sorted(edits, key=lambda e: -e[0]):
            new_raw = new_raw[:start] + replacement + new_raw[end:]
        path.write_text(new_raw, encoding="utf-8")
        stats["files_changed"] += 1


def main():
    verb_index = load_verb_index()
    stats = {
        "infinitive": 0,
        "pronoun": 0,
        "left_alone": 0,
        "files_changed": 0,
        "examples": [],
        "errors": [],
    }

    for path in sorted(EXERCISES_DIR.rglob("*.json")):
        process_file(path, verb_index, stats)

    print(f"Files changed:        {stats['files_changed']}")
    print(f"Infinitive hints:     {stats['infinitive']}")
    print(f"Subject-pronoun hints:{stats['pronoun']}")
    print(f"Left alone (no verb-identity ambiguity found): {stats['left_alone']}")
    if stats["errors"]:
        print(f"\nERRORS — sentence field not found for surgical edit ({len(stats['errors'])}):")
        for name, ex_id in stats["errors"]:
            print(f"  {name} {ex_id}")
    print()
    print("Sample of hints added:")
    for name, ex_id, sentence in stats["examples"][:20]:
        print(f"  {name} {ex_id}: {sentence}")


if __name__ == "__main__":
    main()
