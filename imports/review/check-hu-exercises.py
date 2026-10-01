"""Mechanical checks for the Hungarian exercise review (ROADMAP 117).

Usage:
    python imports/review/check-hu-exercises.py [a1|a2|b1|b2|c1 ...]   # default: all levels
    python imports/review/check-hu-exercises.py a1 --list              # print every hit

ERRORS (must be 0 before committing):
  - choice exercise whose `correct` is not a single valid index
  - duplicate options
SUSPECTS (each must be fixed, or left on purpose and noted in the commit
message; they are patterns, not proof):
  - giveaway: a wrong option has tegnap/holnap/... and the correct one doesn't
  - dont-know: "Nem tudom." / "Nem értem." as a wrong option (answers anything)
  - case: a noun that takes -n/-ra/-ról used with -ban/-ba/-ból
    (postába, állomásban, a helyben, ...). "helyben" meaning "locally" is fine.
"""
import glob, json, re, sys
from pathlib import Path

TIME = re.compile(r'\b(tegnap|holnap|tegnapelőtt|holnapután|tavaly|jövőre)\b', re.I)
DONT_KNOW = {'nem tudom', 'nem értem'}
# nouns that take the superessive family (-n/-ra/-ról), not -ban/-ba/-ból
ON_NOUNS = r'(posta|állomás|pályaudvar|piac|egyetem|repülőtér|repülőtere|munkahely|hely|tér|tere|sziget|strand|' \
           r'Budapest|Magyarország|koncert|előadás|tanfolyam|meccs|kirándulás|konferencia|értekezlet)'
CASE = re.compile(r'\b' + ON_NOUNS + r'(ba|be|ban|ben|ból|ből)\b', re.I)
CHOICE = ('multiple-choice', 'dialogue-complete', 'listening-choice')


def texts(x):
    if isinstance(x, str):
        yield x
    elif isinstance(x, list):
        for y in x:
            yield from texts(y)
    elif isinstance(x, dict):
        for k, v in x.items():
            if k not in ('id', 'teaches', 'type', 'category', 'stage', 'english', 'audio'):
                yield from texts(v)


def norm(s):
    return s.strip().rstrip('.!?').lower()


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    levels = args or ['a1', 'a2', 'b1', 'b2', 'c1']
    show = '--list' in sys.argv
    errors, suspects = [], []
    for lvl in levels:
        for f in sorted(glob.glob(f'content/hu/exercises/{lvl}/*.json')):
            d = json.load(open(f, encoding='utf-8'))
            for e in (d.get('exercises', d) if isinstance(d, dict) else d):
                if not isinstance(e, dict):
                    continue
                i = e.get('id')
                o, k = e.get('options'), e.get('correct')
                if e.get('type') in CHOICE and isinstance(o, list) and all(isinstance(x, str) for x in o):
                    if not isinstance(k, int) or not 0 <= k < len(o):
                        errors.append(f'{i}: correct is not a single valid index')
                        continue
                    if len(set(o)) < len(o):
                        errors.append(f'{i}: duplicate options')
                    wrong = [x for j, x in enumerate(o) if j != k]
                    if any(TIME.search(x) for x in wrong) and not TIME.search(o[k]):
                        suspects.append(f'giveaway   {i}')
                    if any(norm(x) in DONT_KNOW for x in wrong):
                        suspects.append(f'dont-know  {i}')
                for t in texts(e):
                    m = CASE.search(t)
                    if m:
                        suspects.append(f'case       {i}: {m.group(0)}')
                        break
    kinds = {}
    for s in suspects:
        kinds[s.split()[0]] = kinds.get(s.split()[0], 0) + 1
    print(f'levels: {" ".join(levels)}')
    print(f'errors: {len(errors)}')
    for e in errors:
        print('  ' + e)
    print(f'suspects: {len(suspects)} {kinds}')
    if show:
        for s in suspects:
            print('  ' + s)
    sys.exit(1 if errors else 0)


if __name__ == '__main__':
    main()
