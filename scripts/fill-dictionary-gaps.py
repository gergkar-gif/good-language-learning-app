#!/usr/bin/env python3
"""Fill the Reader's dictionary gaps without spending tokens on glossing.

The Reader shows "Not in the dictionary yet" for words the dictionary and the
morphology rules can't resolve. scripts/audit-reader-coverage.js finds them;
this script turns that list into something ChatGPT can gloss, and merges the
reply back into the dictionary.

  1. export   python scripts/fill-dictionary-gaps.py export hu
              python scripts/fill-dictionary-gaps.py export es
        Runs the audit and writes prompt-ready batches to
        imports/dictionary/gap-batches/<lang>-words-NN.txt (ordinary words)
        and <lang>-names-NN.txt (capitalised mid-sentence words). Paste a
        batch into ChatGPT and save its reply next to it as NN.reply.txt.

  2. import   python scripts/fill-dictionary-gaps.py import <reply.txt> hu
        Validates each reply line, records it in
        imports/dictionary/additions-<lang>.json (the source of truth for
        hand and ChatGPT additions) and merges it into the dictionary file.
        Bad lines go to <reply>.rejected.txt with the reason.

  3. merge    python scripts/fill-dictionary-gaps.py merge hu
        Re-applies additions-<lang>.json to the dictionary. Run this after
        re-running import_dictionary.py / import_hu_dictionary.py, which
        rebuild the dictionary from Wiktionary and would drop the additions.

After an import, run the audit again: the remaining list shrinks, and words
whose base form was added start resolving in every inflected form too.

Reply format, one line per word, exactly as exported:
  word | lemma | pos | gloss | gender
lemma is the dictionary headword (base form), pos one of the list below,
gloss a short English gloss, gender only for Spanish nouns (m, f, m; f).
Hungarian names are stored as nouns so case endings still resolve.
"""
import argparse
import json
import re
import subprocess
import sys
import tempfile
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DICTS = {
    'hu': ROOT / 'imports/dictionary/hungarian-en.json',
    'es': ROOT / 'imports/dictionary/spanish-en.json',
}
ADDITIONS = {
    'hu': ROOT / 'imports/dictionary/additions-hu.json',
    'es': ROOT / 'imports/dictionary/additions-es.json',
}
BATCH_DIR = ROOT / 'imports/dictionary/gap-batches'
COURSES = {'hu': ['hu'], 'es': ['es-es', 'es-latam']}
LANG_NAME = {'hu': 'Hungarian', 'es': 'Spanish'}

POS = {
    'hu': {'noun', 'verb', 'adjective', 'adverb', 'pronoun', 'numeral', 'postposition',
           'conjunction', 'interjection', 'particle', 'determiner'},
    'es': {'noun', 'verb', 'adjective', 'adverb', 'proper noun', 'pronoun', 'numeral',
           'preposition', 'conjunction', 'interjection', 'determiner'},
}
GENDERS = {'', 'm', 'f', 'm; f', 'mf'}
LEMMA_RE = re.compile(r"^[a-záéíóöőúüűñ][a-záéíóöőúüűñ' -]*$")


def audit(lang):
    """word -> {count, names, sample} merged across the language's courses."""
    words = {}
    for course in COURSES[lang]:
        with tempfile.NamedTemporaryFile(suffix='.json', delete=False) as tmp:
            out = tmp.name
        subprocess.run(['node', str(ROOT / 'scripts/audit-reader-coverage.js'), course, '--top', '0', '--out', out],
                       check=True, stdout=subprocess.DEVNULL, cwd=ROOT)
        report = json.loads(Path(out).read_text(encoding='utf-8'))[0]
        Path(out).unlink()
        for m in report['misses']:
            w = words.setdefault(m['word'], {'count': 0, 'name': True, 'sample': m['sample'] or ''})
            w['count'] += m['count']
            w['name'] = w['name'] and m['likelyName']
            if len(m['sample'] or '') > len(w['sample']) and len(m['sample']) < 140:
                w['sample'] = m['sample']
    return words


HEADER = """You are helping build a {lang}-English learner's dictionary. Below are {lang} words that appear in
graded reading texts but are missing from the dictionary. Each line is: word | sentence it appears in.

For EVERY line, reply with exactly one line in this format and nothing else (no numbering, no commentary,
no markdown, no blank lines):

word | lemma | pos | gloss | gender

- word: copy the word exactly as given.
- lemma: the dictionary headword (base form), lower case. For a verb the infinitive or the form a {lang}
  dictionary lists; for a noun the nominative singular; for an adjective the base form. A proper name
  stays as the name itself, lower case.
- pos: one of {pos}.
- gloss: a short English dictionary gloss for the lemma, at most 8 words, no quotation marks, no pipes.
  For a place or person use the usual English form ("Danube", "Stephen") or the same name.
- gender: for Spanish nouns only, m or f (or "m; f"); otherwise leave empty.

If a word is not a real {lang} word (a typo, an English word, a fragment), reply:  word | - | - | -

WORDS:
"""

NAMES_NOTE = """
These words are capitalised names (people, places, institutions). Use pos {name_pos} and, as the gloss, the
English form of the name, or the name itself if English uses it unchanged.
"""


def export(lang, batch_size, min_count, limit, dry_run=False):
    dictionary = json.loads(DICTS[lang].read_text(encoding='utf-8'))
    words = {w: v for w, v in audit(lang).items() if w not in dictionary and v['count'] >= min_count}
    ordered = sorted(words.items(), key=lambda kv: (-kv[1]['count'], kv[0]))
    if limit:
        ordered = ordered[:limit]
    groups = {'words': [x for x in ordered if not x[1]['name']],
              'names': [x for x in ordered if x[1]['name']]}
    if dry_run:
        print('%s gaps with count >= %d: %d words and %d names (%d batches of %d)' % (
            lang, min_count, len(groups['words']), len(groups['names']),
            -(-len(groups['words']) // batch_size) + -(-len(groups['names']) // batch_size), batch_size))
        return
    BATCH_DIR.mkdir(parents=True, exist_ok=True)
    stale = [p.name for p in BATCH_DIR.glob(lang + '-*.txt')]
    written = []
    for kind, items in groups.items():
        for n in range(0, len(items), batch_size):
            chunk = items[n:n + batch_size]
            text = HEADER.format(lang=LANG_NAME[lang], pos=', '.join(sorted(POS[lang])))
            if kind == 'names':
                note = NAMES_NOTE.format(name_pos='proper noun' if lang == 'es' else 'noun')
                text = text.replace('WORDS:\n', note + '\nWORDS:\n')
            body = []
            for word, v in chunk:
                sample = re.sub(r'\s+', ' ', v['sample']).strip()[:140]
                body.append('%s | %s' % (word, sample))
            path = BATCH_DIR / ('%s-%s-%02d.txt' % (lang, kind, n // batch_size + 1))
            path.write_text(text + '\n'.join(body) + '\n', encoding='utf-8')
            written.append((path, len(chunk)))
    if not written:
        print('No gaps found (or none at --min-count %d).' % min_count)
        return
    for path, n in written:
        print('%4d words  %s' % (n, path.relative_to(ROOT)))
    fresh = {p.name for p, _ in written}
    leftovers = [n for n in sorted(stale) if n not in fresh and not n.endswith(('.reply.txt', '.rejected.txt'))]
    if leftovers:
        print('\nNote: %d batch files from an earlier export are still in %s; delete any you no longer need.'
              % (len(leftovers), BATCH_DIR.relative_to(ROOT)))
    print('\nPaste each batch into ChatGPT, save its reply next to it (e.g. %s), then:\n'
          '  python scripts/fill-dictionary-gaps.py import <reply file> %s'
          % (written[0][0].with_suffix('.reply.txt').name, lang))


def nfc(s):
    return unicodedata.normalize('NFC', s.strip())


def parse_reply(text, lang):
    """-> (senses: {lemma: [sense]}, rejected: [(line, reason)])"""
    senses = {}
    rejected = []
    for raw in text.splitlines():
        line = raw.strip().strip('`').strip()
        line = re.sub(r'^\s*(?:[-*•]|\d+[.)])\s+', '', line)
        if not line or line.lower().startswith(('word |', 'here', 'sure')) or '|' not in line:
            continue
        cols = [nfc(c) for c in line.split('|')]
        if len(cols) < 4:
            rejected.append((raw, 'needs word | lemma | pos | gloss'))
            continue
        word, lemma, pos, gloss = cols[0], cols[1].lower(), cols[2].lower(), cols[3]
        gender = cols[4].lower() if len(cols) > 4 else ''
        if lemma in ('-', '') or pos == '-' or gloss == '-':
            continue   # the model marked it as not a real word
        if not LEMMA_RE.match(lemma):
            rejected.append((raw, 'lemma has unexpected characters'))
        elif pos not in POS[lang]:
            rejected.append((raw, 'pos %r not allowed' % pos))
        elif not gloss or len(gloss) > 90 or '"' in gloss:
            rejected.append((raw, 'gloss empty, too long or contains a quote'))
        elif gender not in GENDERS:
            rejected.append((raw, 'gender %r not allowed' % gender))
        else:
            sense = {'en': gloss, 'type': pos}
            if lang == 'es' and pos == 'noun' and gender:
                sense['gender'] = 'm; f' if gender == 'mf' else gender
            existing = senses.setdefault(lemma, [])
            if not any(s['en'] == gloss and s['type'] == pos for s in existing):
                existing.append(sense)
    return senses, rejected


def load_json(path, default):
    return json.loads(path.read_text(encoding='utf-8')) if path.exists() else default


def dump_like(data, original_raw):
    """Serialise `data` in exactly the layout of original_raw, or fail."""
    probe = json.loads(original_raw)
    for kwargs, crlf in (({'separators': (',', ':')}, False), ({'indent': 2}, True), ({'indent': 2}, False)):
        out = json.dumps(probe, ensure_ascii=False, **kwargs)
        if crlf:
            out = out.replace('\n', '\r\n')
        if out == original_raw or out == original_raw.rstrip('\r\n'):
            trailing = original_raw[len(original_raw.rstrip('\r\n')):]
            text = json.dumps(data, ensure_ascii=False, **kwargs)
            if crlf:
                text = text.replace('\n', '\r\n')
            return text + trailing
    raise SystemExit('Could not reproduce the dictionary file layout exactly; refusing to rewrite it.')


def merge(lang):
    additions = load_json(ADDITIONS[lang], {})
    if not additions:
        print('Nothing to merge (%s is empty).' % ADDITIONS[lang].name)
        return
    raw = DICTS[lang].read_bytes().decode('utf-8')
    dictionary = json.loads(raw)
    added = skipped = conflicts = 0
    for lemma, senses in additions.items():
        current = dictionary.get(lemma)
        if lang == 'hu':
            existing = current if isinstance(current, list) else []
            fresh = [s for s in senses if not any(e.get('en') == s['en'] for e in existing)]
            if fresh:
                dictionary[lemma] = existing + fresh
                added += 1
            else:
                skipped += 1
        else:
            if current is None:
                dictionary[lemma] = senses[0]   # Spanish entries hold one sense
                added += 1
            elif current.get('type') != senses[0]['type']:
                conflicts += 1
                print('  conflict (kept the existing %s entry): %s -> %s' % (current.get('type'), lemma, senses[0]['type']))
            else:
                skipped += 1
    DICTS[lang].write_bytes(dump_like(dictionary, raw).encode('utf-8'))
    print('%s dictionary: %d added, %d already covered, %d conflicts' % (lang, added, skipped, conflicts))


def do_import(reply_path, lang):
    senses, rejected = parse_reply(Path(reply_path).read_text(encoding='utf-8'), lang)
    additions = load_json(ADDITIONS[lang], {})
    for lemma, new in senses.items():
        bucket = additions.setdefault(lemma, [])
        for s in new:
            if not any(e['en'] == s['en'] and e['type'] == s['type'] for e in bucket):
                bucket.append(s)
    ADDITIONS[lang].write_text(json.dumps(dict(sorted(additions.items())), ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print('%d entries accepted, %d lines rejected' % (len(senses), len(rejected)))
    if rejected:
        rej = Path(str(reply_path) + '.rejected.txt')
        rej.write_text('\n'.join('%s    <- %s' % (l, r) for l, r in rejected) + '\n', encoding='utf-8')
        print('  rejected lines and reasons: %s' % rej)
    merge(lang)


def main():
    p = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    sub = p.add_subparsers(dest='cmd', required=True)
    e = sub.add_parser('export')
    e.add_argument('lang', choices=sorted(COURSES))
    e.add_argument('--batch-size', type=int, default=120)
    e.add_argument('--min-count', type=int, default=3)
    e.add_argument('--limit', type=int, default=0, help='only the N most frequent gaps')
    e.add_argument('--dry-run', action='store_true', help='print the counts, write nothing')
    i = sub.add_parser('import')
    i.add_argument('reply')
    i.add_argument('lang', choices=sorted(COURSES))
    m = sub.add_parser('merge')
    m.add_argument('lang', choices=sorted(COURSES))
    a = p.parse_args()
    if a.cmd == 'export':
        export(a.lang, a.batch_size, a.min_count, a.limit, a.dry_run)
    elif a.cmd == 'import':
        do_import(a.reply, a.lang)
    else:
        merge(a.lang)


if __name__ == '__main__':
    sys.exit(main())
