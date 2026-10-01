"""Acceptance check for the Spanish B1 distractor rewrite (ROADMAP 117).

Usage:
    python imports/review/check-es-b1-giveaways.py            # counts + any problems
    python imports/review/check-es-b1-giveaways.py --list     # also print remaining giveaways

Reports, for every multiple-choice / dialogue-complete exercise in
content/es-es and content/es-latam level b1:
  - giveaways: a wrong option contains "ayer"/"mañana" and the correct one doesn't
  - duplicate options, and `correct` that is not a single valid index
  - es-es / es-latam copies of the same id that no longer match
    (only for ids that matched before the rewrite, listed in the work list)
"""
import glob, json, re, sys
from pathlib import Path

TIME = re.compile(r'\b(ayer|mañana)\b', re.I)
LIST = Path(__file__).with_name('es-b1-giveaways.jsonl')


def strip(s):
    return re.sub(r'\[.*?\]', '', s)


def load(course):
    out = {}
    for f in glob.glob(f'content/{course}/exercises/b1/*.json'):
        d = json.load(open(f, encoding='utf-8'))
        for e in (d.get('exercises', d) if isinstance(d, dict) else d):
            if isinstance(e, dict) and e.get('type') in ('multiple-choice', 'dialogue-complete'):
                out[e['id']] = e
    return out


def main():
    show = '--list' in sys.argv
    work = [json.loads(l) for l in open(LIST, encoding='utf-8')] if LIST.exists() else []
    shared = {w['id'] for w in work if len(w['courses']) == 2}
    data = {c: load(c) for c in ('es-es', 'es-latam')}
    problems, giveaways = [], []
    for c, exs in data.items():
        for i, e in exs.items():
            o, k = e.get('options'), e.get('correct')
            if not isinstance(o, list) or not isinstance(k, int) or not 0 <= k < len(o):
                problems.append(f'{c} {i}: correct is not a single valid index'); continue
            if len(set(o)) < len(o):
                problems.append(f'{c} {i}: duplicate options')
            if not isinstance(o[k], str):
                continue
            if any(TIME.search(strip(x)) for j, x in enumerate(o) if j != k and isinstance(x, str)) \
                    and not TIME.search(strip(o[k])):
                giveaways.append(f'{c} {i}')
    for i in sorted(shared):
        a, b = data['es-es'].get(i), data['es-latam'].get(i)
        if a and b and (a.get('options'), a.get('correct')) != (b.get('options'), b.get('correct')):
            problems.append(f'{i}: es-es and es-latam copies differ')
    print(f'giveaways remaining: {len(giveaways)}')
    print(f'problems: {len(problems)}')
    for p in problems:
        print('  ' + p)
    if show:
        for g in giveaways:
            print('  giveaway: ' + g)
    sys.exit(1 if problems else 0)


if __name__ == '__main__':
    main()
