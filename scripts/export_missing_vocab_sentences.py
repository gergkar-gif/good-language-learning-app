#!/usr/bin/env python3
"""
Export vocabulary words lacking example sentences in translation-index.json.
Generates prompt-ready text files grouped by CEFR level for LLM backfill.

Usage:
    python scripts/export_missing_vocab_sentences.py [lang]
Default lang: es
"""

import json
import re
import sys
from pathlib import Path

CONTENT_POS = {'noun', 'verb', 'adjective', 'adverb'}
WORD_RE = re.compile(r'\w+', re.UNICODE)


def load_lexicon(lang):
    verb_idx = {}
    word_idx = {}
    if lang == 'es':
        vp = Path('generated/indexes/verb-index.json')
        wp = Path('generated/indexes/word-index.json')
        if vp.exists():
            with open(vp, encoding='utf-8') as f:
                verb_idx = json.load(f)
        if wp.exists():
            with open(wp, encoding='utf-8') as f:
                word_idx = json.load(f)
    elif lang == 'hu':
        wp = Path('content/hu/indexes/word-index.json')
        if wp.exists():
            with open(wp, encoding='utf-8') as f:
                word_idx = json.load(f)

    def get_lemmas(token):
        t_low = token.lower()
        lemmas = set()
        if t_low in verb_idx:
            for entry in verb_idx[t_low]:
                lemmas.add(entry['lemma'].lower())
        if t_low in word_idx:
            for entry in word_idx[t_low]:
                lemmas.add(entry['lemma'].lower())
        if not lemmas:
            lemmas.add(t_low)
        return lemmas

    return get_lemmas


def main():
    lang = sys.argv[1] if len(sys.argv) > 1 else 'es'
    decks_path = Path(f'content/{lang}/decks/decks.json')
    trans_path = Path(f'content/{lang}/indexes/translation-index.json')

    if not decks_path.exists() or not trans_path.exists():
        print(f"[{lang}] Missing decks.json or translation-index.json")
        return

    with open(decks_path, encoding='utf-8') as f:
        deck_data = json.load(f)
    with open(trans_path, encoding='utf-8') as f:
        trans_data = json.load(f)

    get_lemmas = load_lexicon(lang)

    # Build context lemmas from sentences with >= 5 words
    context_lemmas = set()
    for pair in trans_data.get('pairs', []):
        text = pair.get('spanish', '')
        tokens = WORD_RE.findall(text)
        if len(tokens) < 5:
            continue
        for t in tokens:
            for lem in get_lemmas(t):
                context_lemmas.add(lem)
            context_lemmas.add(t.lower())

    # Map words to levels from lesson decks
    lemma_levels = {}
    for d in deck_data.get('decks', []):
        lvl = d.get('level')
        for lem in d.get('lemmas', []):
            if lem not in lemma_levels and lvl:
                lemma_levels[lem] = lvl

    words = deck_data.get('words', {})
    missing_by_level = {}

    es_article_re = re.compile(r'^(el|la|los|las)\s+')

    for word, info in words.items():
        if info.get('pos') not in CONTENT_POS:
            continue
        lvl = lemma_levels.get(word, 'other')
        if lvl not in missing_by_level:
            missing_by_level[lvl] = []

        w_clean = word.lower().strip()
        if lang == 'es':
            # decks.json stores many ES nouns with their article ("el
            # cumpleaños"), but sentence tokens never contain that whole
            # phrase as one token -- match against the noun alone too.
            w_clean = es_article_re.sub('', w_clean)
        matched = False
        # Multi-word dictionary keys (ES adverbial phrases like "a menudo",
        # or a conjugated phrase used as the key like "me sentía") never
        # appear verbatim as a single sentence token -- also try each
        # content-bearing subword (skip short function words).
        parts = [p.strip() for p in re.split(r'[/,()]', w_clean) if p.strip()]
        space_parts = [sp for p in parts for sp in p.split(' ') if len(sp) >= 4]
        for p in parts + space_parts:
            if p in context_lemmas or any(l in context_lemmas for l in get_lemmas(p)):
                matched = True
                break
            # Agglutinative fallback: Hungarian (and some Spanish) surface
            # forms attach suffixes/prefixes the lemma index doesn't cover
            # (e.g. "farmer" -> "farmerom", "próbál" -> "felpróbálni").
            # A two-way prefix check on longer words catches most of these
            # without risking false matches on short/common words.
            if len(p) >= 4 and any(
                ct.startswith(p) or p.startswith(ct)
                for ct in context_lemmas if len(ct) >= 4
            ):
                matched = True
                break
            # ES conjugation fallback: verb-index.json doesn't cover every
            # regular conjugated form, but stripping the infinitive/
            # reflexive ending and prefix-matching the stem catches most
            # regular verbs the lemma index misses (e.g. "remar" -> "rem"
            # matches "remaba"; "mojarse" -> "moj" matches "mojé").
            if lang == 'es':
                stem = re.sub(r'(arse|erse|irse|ar|er|ir)$', '', p)
                if len(stem) >= 3 and any(
                    ct.startswith(stem) for ct in context_lemmas if len(ct) >= 3
                ):
                    matched = True
                    break
            # HU infinitive fallback: same idea for Hungarian "-ni"
            # infinitives, whose conjugated forms drop -ni and often
            # change the stem's final consonant(s) (e.g. "ráérni" ->
            # "ráér" matches "ráérsz"; "bújni" -> "búj" matches "bújik").
            if lang == 'hu' and p.endswith('ni'):
                stem = p[:-2]
                if len(stem) >= 3 and any(
                    ct.startswith(stem) for ct in context_lemmas if len(ct) >= 3
                ):
                    matched = True
                    break
            # HU "-ik" citation-form fallback: many dictionary headwords
            # are the 3sg present ikes-verb form itself (e.g. "felöltözik",
            # "kikapcsolódik"), but sentences use other conjugated forms
            # ("felöltözött") -- strip -ik and prefix-match the stem.
            if lang == 'hu' and p.endswith('ik'):
                stem = p[:-2]
                if len(stem) >= 3 and any(
                    ct.startswith(stem) for ct in context_lemmas if len(ct) >= 3
                ):
                    matched = True
                    break

        if not matched:
            missing_by_level[lvl].append({
                'word': word,
                'en': info.get('en', ''),
                'pos': info.get('pos', ''),
                'level': lvl
            })

    out_dir = Path(f'content/{lang}/backfill_prompts')
    out_dir.mkdir(parents=True, exist_ok=True)

    print(f"=== {lang.upper()} Missing Vocabulary Sentences Summary ===")
    total_missing = sum(len(v) for v in missing_by_level.values())
    print(f"Total missing: {total_missing}")

    lang_name = "Hungarian" if lang == "hu" else "Spanish"
    target_key = "hungarian" if lang == "hu" else "spanish"

    level_instructions = {
        'es': {
            'A1': "Keep sentences strictly at CEFR A1 level: present tense (presente de indicativo), simple subject-verb-object structures, basic everyday vocabulary.",
            'A2': "Keep sentences at CEFR A2 level: preterite (pretérito indefinido) and imperfect (pretérito imperfecto) tenses, simple compound sentences with 'porque', 'cuando', 'pero'.",
            'B1': "Keep sentences at CEFR B1 level: subjunctive mood where natural (presente de subjuntivo), conditional, future, relative clauses, intermediate vocabulary."
        },
        'hu': {
            'A1': "Keep sentences strictly at CEFR A1 level: present tense (jelen idő), simple SVO/SOV, basic case endings (-ban/-ben, -ba/-be, -ból/-ből, -on/-en/-ön, -t accusative), basic everyday vocabulary.",
            'A2': "Keep sentences at CEFR A2 level: past tense (múlt idő: -t/-tt), definite vs indefinite conjugation, compound sentences with 'mert', 'amikor', 'de', verbal prefixes (el-, meg-, be-, ki-).",
            'B1': "Keep sentences at CEFR B1 level: conditional mood (feltételes mód: -na/-ne/-ná/-né), subjunctive/imperative (-jon/-jen), relative clauses with 'amely', 'aki', civic/cultural/abstract vocabulary."
        }
    }

    BATCH_SIZE = 100

    for lvl in sorted(missing_by_level.keys()):
        items = missing_by_level[lvl]
        print(f"  Level {lvl}: {len(items)} words")

        lang_guides = level_instructions.get(lang, {})
        instr = lang_guides.get(lvl, f"Keep sentences natural and appropriate for CEFR level {lvl} in {lang_name}.")

        for batch_idx in range(0, len(items), BATCH_SIZE):
            chunk = items[batch_idx:batch_idx + BATCH_SIZE]
            batch_num = (batch_idx // BATCH_SIZE) + 1
            total_batches = (len(items) + BATCH_SIZE - 1) // BATCH_SIZE

            filename = f"{lvl.lower()}_batch_{batch_num:02d}_of_{total_batches:02d}.txt"
            filepath = out_dir / filename

            with open(filepath, 'w', encoding='utf-8') as f:
                f.write("SYSTEM PROMPT / INSTRUCTIONS:\n")
                f.write(f"You are an expert {lang_name} curriculum writer for a language learning application.\n")
                f.write(f"Your task is to generate ONE natural example sentence for each of the {lang_name} vocabulary words below.\n\n")
                f.write("RULES:\n")
                f.write(f"1. LEVEL: {instr}\n")
                f.write(f"2. MINIMUM LENGTH: The {lang_name} sentence MUST contain at least 6 to 12 words (minimum 5 words strictly required). Do not write short fragments.\n")
                f.write("3. INFERABLE CONTEXT: The sentence must provide enough context that the meaning of the target word is clear and makes sense in context.\n")
                f.write("4. USAGE: Use the target word naturally (conjugated, inflected with cases, or derived form is welcome).\n")
                f.write("5. TRANSLATION: Provide an accurate, natural English translation for the full sentence.\n")
                f.write("6. OUTPUT FORMAT: Output ONLY a valid JSON array of objects, with NO markdown commentary. Each object must have:\n")
                f.write('   {\n     "word": "<target word as listed>",\n     "' + target_key + '": "<full ' + lang_name + ' sentence>",\n     "english": "<full English translation>",\n     "level": "' + lvl + '"\n   }\n\n')
                f.write(f"VOCABULARY WORDS ({len(chunk)} words):\n")
                for it in chunk:
                    f.write(f"- {it['word']} ({it['pos']}): {it['en']}\n")

    print(f"\nPrompt files generated in: {out_dir}")


if __name__ == '__main__':
    main()
