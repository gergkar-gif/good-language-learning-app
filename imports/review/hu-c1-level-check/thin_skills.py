"""C1 level checklist: consolidation replays for four thin skills (2026-11-18)."""
import json
from pathlib import Path
R = Path('/home/user/good-language-learning-app/content/hu/exercises/c1')
def edit(stem, changes):
    p = R / f'{stem}-consolidation-ex.json'
    d = json.loads(p.read_text(encoding='utf-8'))
    by = {e['id']: e for e in d['exercises']}
    for n, new in changes.items():
        e = by[f'{stem}-consolidation-{n}']
        keep = {k: e[k] for k in ('id', 'type', 'stage')}
        if new is None: continue
        if 'patch' in new:
            e.update(new['patch']); continue
        e.clear(); e.update(keep); e.update(new)
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

edit('c1-munkaeropiac', {
  8: {"category": "grammar", "sentence": "Egyes elemzők szerint az ingázás _____ soron a bérkülönbségek következménye.", "hint": "'ultimately'", "answer": "végső", "english": "According to some analysts, commuting is ultimately a consequence of wage differences.", "teaches": ["conclusive-markers"]},
  12: {"category": "writing", "template": [{"prompt": "Write a concluding sentence about wages and commuting to Austria with 'összességében', saying whose view it is.", "answer": "Összességében egyes elemzők szerint az ausztriai ingázás addig marad jelentős, amíg nagy a bérkülönbség."}], "teaches": ["conclusive-markers"]},
})
edit('c1-tarsadalmireteg', {
  10: {"category": "grammar", "tiles": ["Felmerül", "a", "kérdés,", "hogy", "a", "falu", "megtartó", "ereje", "a", "helyi", "munkahelyektől", "függ-e."], "solution": ["Felmerül", "a", "kérdés,", "hogy", "a", "falu", "megtartó", "ereje", "a", "helyi", "munkahelyektől", "függ-e."], "english": "The question arises whether a village's holding power depends on local jobs.", "teaches": ["framing-markers"]},
  12: {"category": "writing", "template": [{"prompt": "Frame the debate on decentralisation with 'A kérdés nem az, hogy …, hanem az, hogy …', saying whose view it is.", "answer": "Egyes szakértők szerint a kérdés nem az, hogy kell-e decentralizáció, hanem az, hogy milyen formában."}], "teaches": ["framing-markers"]},
})
edit('c1-mestersegesintelligencia', {
  10: {"category": "grammar", "tiles": ["Sok", "szakértő", "szerint", "hadd", "döntsön", "az", "ember,", "ne", "a", "gép."], "solution": ["Sok", "szakértő", "szerint", "hadd", "döntsön", "az", "ember,", "ne", "a", "gép."], "english": "According to many experts, let the human decide, not the machine.", "teaches": ["optative-subjunctive"]},
  12: {"category": "writing", "template": [{"prompt": "Write a closing thought on AI and human agency: a deliberative question, then an attributed answer with 'hadd'.", "answer": "Mit tegyünk, ha a gép gyorsabban dönt, mint mi? Sok szakértő szerint hadd maradjon az ember felelős a végső döntésért."}], "teaches": ["optative-subjunctive"]},
})
# fix the SZTAKI pair in place
p = R / 'c1-mestersegesintelligencia-consolidation-ex.json'
x = p.read_text(encoding='utf-8')
assert x.count('"magyar kutatóhálózat"') == 1
p.write_text(x.replace('"magyar kutatóhálózat"', '"a HUN-REN egyik kutatóintézete"'), encoding='utf-8')
edit('c1-05', {
  7: {"category": "grammar", "sentence": "Hivatalosan a gazdaság nem zuhan, csupán negatív növekedési pályára állt át; _____ szólva: csökken.", "hint": "'in plain words'", "answer": "magyarán", "english": "Officially the economy is not collapsing, it has merely switched to a negative growth path; in plain words: it is shrinking.", "teaches": ["satire-parody"]},
  10: {"category": "grammar", "tiles": ["Magyarán", "szólva:", "elfogyott", "a", "pénz."], "solution": ["Magyarán", "szólva:", "elfogyott", "a", "pénz."], "english": "In plain words: the money has run out.", "teaches": ["satire-parody"]},
})
print('done')
