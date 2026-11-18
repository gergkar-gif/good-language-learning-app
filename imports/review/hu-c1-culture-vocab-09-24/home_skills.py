"""Give optative-subjunctive, framing-markers and conclusive-markers their screens (user, 2026-11-18)."""
import json
from pathlib import Path
R = Path('/home/user/good-language-learning-app/content/hu')

def load(p): return json.loads((R/p).read_text(encoding='utf-8'))
def save(p, d): (R/p).write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

def screen(p, title, mech, appl, rows):
    d = load(p)
    d['title'] = title
    d['sections'] = [
        {"type": "text", "title": "The Structural Mechanism", "content": mech},
        {"type": "text", "title": "Rhetorical Application & Stance", "content": appl},
        {"type": "table", "title": "Patterns in Context", "rows": rows},
    ]
    save(p, d)

def items(p, changes):
    d = load(p)
    by = {e['id']: e for e in d['exercises']}
    for eid, new in changes.items():
        e = by[eid]
        keep = {k: e[k] for k in ('id', 'type', 'stage')}
        e.clear(); e.update(keep); e.update(new)
    save(p, d)

def lesson(p, grammar_title, old_goal, new_goal):
    d = load(p)
    d['grammar'] = grammar_title
    hits = 0
    def fix(lst):
        nonlocal hits
        for i, x in enumerate(lst):
            if x == old_goal: lst[i] = new_goal; hits += 1
    fix(d['goal'])
    for s in d['sections']:
        if s.get('type') == 'grammar': s['title'] = grammar_title
        if isinstance(s.get('items'), list): fix(s['items'])
    assert hits >= 2, (p, hits)
    save(p, d)

def story_add(p, para_idx, old, new):
    d = load(p)
    t = d['paragraphs'][para_idx]['text']
    assert old in t, (p, old)
    d['paragraphs'][para_idx]['text'] = t.replace(old, new, 1)
    save(p, d)

# ---------- conclusive-markers: Culture Unit 21, lesson 5 ----------
S = 'c1-munkaeropiac-05'
screen(f'grammar/c1/{S}-a-gr.json',
  "Drawing a Conclusion: összességében, végső soron",
  "You know *összegzésképpen megállapítható, hogy* from B1 Unit 21, *a fentiek tükrében* and *mindent egybevetve* from B1 Unit 34 and *mindebből következően* from C1 Unit 1. Two more close a commentary. *Összességében* ('on the whole') weighs everything said so far. *Végső soron* ('ultimately', 'in the last analysis') names what a question comes down to in the end. Both stand at the start of the closing sentence or right before the verb: `összességében lassú a felzárkózás`, `a bérek végső soron a termelékenységen múlnak`.",
  "A conclusion is still somebody's view, and the text says so: `Összességében egyes elemzők úgy látják, hogy …`. *Végső soron* is no proof; it marks the writer's judgement about what matters most: `végső soron azon múlik, hogy …` (it ultimately depends on whether …).",
  [["Összességében az ingázás a határ menti régiók életének része maradt.", "On the whole, commuting has remained part of life in the border regions."],
   ["Egyes elemzők szerint a bérek felzárkózása végső soron a termelékenységen múlik.", "According to some analysts, the catching-up of wages ultimately depends on productivity."],
   ["A fentiek tükrében a vita középpontjában a bérek felzárkózása áll.", "In the light of the above, the catching-up of wages is at the centre of the debate."]])
T = ["conclusive-markers"]
items(f'exercises/c1/{S}-ex.json', {
  f'{S}-controlled-2': {"category": "grammar", "sentence": "Egyes elemzők szerint a bérek felzárkózása _____ soron a termelékenységen múlik.", "hint": "'ultimately': in the last row", "answer": "végső", "english": "According to some analysts, the catching-up of wages ultimately depends on productivity.", "teaches": T},
  f'{S}-practice-4': {"category": "grammar", "sentence": "_____ az ingázás a határ menti régiók életének része maradt.", "hint": "'on the whole'", "answers": ["Összességében", "Mindent egybevetve"], "english": "On the whole, commuting has remained part of life in the border regions.", "teaches": T},
  f'{S}-practice-5': {"category": "grammar", "tiles": ["Összességében", "egyes", "elemzők", "szerint", "a", "felzárkózás", "lassú", "folyamat."], "solution": ["Összességében", "egyes", "elemzők", "szerint", "a", "felzárkózás", "lassú", "folyamat."], "english": "On the whole, according to some analysts, catching up is a slow process.", "teaches": T},
  f'{S}-production-7': {"category": "writing", "template": [{"prompt": "Write a concluding sentence about wage catch-up with 'összességében' or 'végső soron', saying whose view it is.", "answer": "Összességében egyes elemzők szerint a bérek felzárkózása végső soron a tudásalapú gazdaság erősítésén múlik."}], "teaches": T},
  f'{S}-check-8': {"category": "grammar", "question": "Melyik kifejezéssel zárhatunk le egy érvelést?", "options": ["Végső soron", "Ezzel szemben", "Például"], "correct": 0, "teaches": T},
})
lesson(f'lessons/c1/{S}.json', "Drawing a Conclusion: összességében, végső soron",
  "I can sum up an argument with *a fentiek tükrében*, *összegzésképpen megállapítható, hogy* and *mindebből következően*.",
  "I can close an argument with *összességében* and *végső soron*, besides *a fentiek tükrében* and *mindebből következően*.")
story_add('stories/world/c1/c1-munkaeropiac-05-berfelzarkozas.json', 1,
  "A fentiek tükrében egyes elemzők úgy vélik,",
  "Összességében az ingázás a határ menti régiók életének része maradt. A fentiek tükrében egyes elemzők úgy vélik,")

# ---------- framing-markers: Culture Unit 19, lesson 1 ----------
S = 'c1-tarsadalmireteg-01'
screen(f'grammar/c1/{S}-a-gr.json',
  "Framing the Problem: felmerül a kérdés, a kérdés nem az, hogy …",
  "A commentary first says what the problem is. *Felmerül a kérdés, hogy …* ('the question arises whether …') opens it; the clause after it takes *-e* when it is a yes/no question (`… hogy a vidéki városok ellensúlyt jelenthetnek-e`). *A kérdés nem az, hogy …, hanem az, hogy …* moves the debate from one question to another. *Abból érdemes kiindulni, hogy …* ('it is worth starting from the fact that …') names the starting point. You know the images *vízfej* and *szakadék tátong* from C1 Unit 6's metaphor screens; a frame says in plain words what such an image is about.",
  "Example: `A kérdés nem az, hogy van-e különbség a főváros és a vidék között, hanem az, hogy mekkora.` The frame itself is neutral: the writer's answer to the question still needs a source (`a kutatók szerint …`).",
  [["Felmerül a kérdés, hogy a vidéki nagyvárosok ellensúlyt jelenthetnek-e a fővárosnak.", "The question arises whether regional cities can be a counterweight to the capital."],
   ["A kérdés nem az, hogy van-e különbség, hanem az, hogy mekkora.", "The question is not whether there is a difference, but how big it is."],
   ["Abból érdemes kiindulni, hogy Budapest a 19. század második felében nőtt az ország központjává.", "It is worth starting from the fact that Budapest grew into the country's centre in the second half of the 19th century."]])
T = ["framing-markers"]
items(f'exercises/c1/{S}-ex.json', {
  f'{S}-practice-4': {"category": "grammar", "sentence": "Felmerül a _____, hogy a vidéki nagyvárosok ellensúlyt jelenthetnek-e a fővárosnak.", "hint": "'question'", "answer": "kérdés", "english": "The question arises whether regional cities can be a counterweight to the capital.", "teaches": T},
  f'{S}-practice-5': {"category": "grammar", "tiles": ["A", "kérdés", "nem", "az,", "hogy", "van-e", "különbség,", "hanem", "az,", "hogy", "mekkora."], "solution": ["A", "kérdés", "nem", "az,", "hogy", "van-e", "különbség,", "hanem", "az,", "hogy", "mekkora."], "english": "The question is not whether there is a difference, but how big it is.", "teaches": T},
  f'{S}-production-7': {"category": "writing", "template": [{"prompt": "Frame the problem of regional inequality in one sentence with 'Felmerül a kérdés, hogy' or 'A kérdés nem az, hogy …, hanem az, hogy …'.", "answer": "Felmerül a kérdés, hogy hogyan lehetne csökkenteni a főváros és a vidék közötti különbséget."}], "teaches": T},
  f'{S}-check-8': {"category": "grammar", "question": "Melyik mondat vezet be egy problémát egy kommentárban?", "options": ["Felmerül a kérdés, miért ilyen nagy a főváros súlya.", "Budapest a Duna két partján fekvő nagy főváros.", "Budapest az ország legnagyobb és legrégebbi városa."], "correct": 0, "teaches": T},
})
lesson(f'lessons/c1/{S}.json', "Framing the Problem: felmerül a kérdés, a kérdés nem az, hogy …",
  "I can say in plain words what an image of inequality claims.",
  "I can frame a problem with *felmerül a kérdés, hogy*, *a kérdés nem az, hogy …, hanem az, hogy …* and *abból érdemes kiindulni, hogy*.")
story_add('stories/world/c1/c1-tarsadalmireteg-01-vizfej.json', 1,
  "a bírálók a főváros túlsúlyára a 'vízfej' képét használják.",
  "a bírálók a főváros túlsúlyára a 'vízfej' képét használják. Felmerül a kérdés, hogy a vidéki nagyvárosok ellensúlyt jelenthetnek-e a fővárosnak.")

# ---------- optative-subjunctive: Culture Unit 15, lesson 4 ----------
S = 'c1-mestersegesintelligencia-04'
screen(f'grammar/c1/{S}-a-gr.json',
  "Let the Doctor Decide: hadd and the Deliberative Subjunctive",
  "You know the subjunctive after *hogy* from B1 Unit 3 (*fontos, hogy az orvos döntsön*) and wishes with *bárcsak* + conditional from B1 Unit 3. The subjunctive also stands on its own. With *hadd* it asks or allows that someone do something: `hadd döntsön az orvos` ('let the doctor decide'), `hadd tegyem hozzá` ('let me add'). In a question it deliberates, asking what should be done: `Mit tegyünk, ha az algoritmus téved?`, `Bízzunk-e a gépben?` ('should we trust the machine?'). The verb is the same subjunctive form as after *hogy*: *döntsön, tegyük, bízzunk*.",
  "Commentary on medical AI uses deliberative questions to set out a dilemma, and *hadd* to state whose decision it should be. Both are positions, so say whose: `Sok orvos szerint hadd hozza meg a végső döntést az orvos.`",
  [["Hadd döntsön az orvos a beteggel együtt.", "Let the doctor decide together with the patient."],
   ["Mit tegyünk, ha az algoritmus téved?", "What should we do if the algorithm is wrong?"],
   ["Bízzunk-e a gépben, ha nem tudjuk, hogyan döntött?", "Should we trust the machine if we don't know how it decided?"]])
T = ["optative-subjunctive"]
items(f'exercises/c1/{S}-ex.json', {
  f'{S}-controlled-2': {"category": "grammar", "sentence": "Sok orvos szerint _____ döntsön az orvos a beteggel együtt.", "hint": "'let'", "answer": "hadd", "english": "According to many doctors, let the doctor decide together with the patient.", "teaches": T},
  f'{S}-practice-5': {"category": "grammar", "tiles": ["Mit", "tegyünk,", "ha", "az", "algoritmus", "téved?"], "solution": ["Mit", "tegyünk,", "ha", "az", "algoritmus", "téved?"], "english": "What should we do if the algorithm is wrong?", "teaches": T},
  f'{S}-production-7': {"category": "writing", "template": [{"prompt": "Write a sentence with 'hadd' about who should make the final decision, saying whose view it is.", "answer": "Sok orvos szerint hadd hozza meg a végső döntést az orvos a beteggel együtt."}], "teaches": T},
  f'{S}-check-8': {"category": "grammar", "question": "Melyik mondat kérdezi, mit kellene tenni?", "options": ["Bízzunk-e a gépben, ha nem tudjuk, hogyan döntött?", "Bízunk a gépben, mert tudjuk, hogyan döntött.", "Bíztunk a gépben, bár nem tudtuk, hogyan döntött."], "correct": 0, "teaches": T},
})
lesson(f'lessons/c1/{S}.json', "Let the Doctor Decide: hadd and the Deliberative Subjunctive",
  "I can say what is important with *fontos, hogy* and concede a point with *bármilyen … is*.",
  "I can say whose decision something should be with *hadd* and ask what should be done with the subjunctive (*Mit tegyünk?*, *Bízzunk-e …?*).")
story_add('stories/world/c1/c1-mestersegesintelligencia-04-orvoslas.json', 1,
  "A klinikai döntéstámogatás területén magyar kutatócsoportok is dolgoznak.",
  "A klinikai döntéstámogatás területén magyar kutatócsoportok is dolgoznak. Az orvosok gyakran felteszik a kérdést: mit tegyünk, ha az algoritmus téved? Sokan úgy válaszolnak: hadd döntsön az orvos a beteggel együtt.")
print('done')
