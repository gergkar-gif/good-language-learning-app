# -*- coding: utf-8 -*-
"""
Full Unit 14 Overhaul: The 18th Century: Rebuilding & Maria Theresa (b1-mariaterezia)
Lessons:
1. A Pragmatica Sanctio (1723) és a nőági örökösödés
2. Mária Terézia és a pozsonyi országgyűlés (1741, 'Vitam et sanguinem!')
3. Mária Terézia reformjai: Urbárium (1767) és Ratio Educationis (1777)
4. II. József, a 'kalapos király' felvilágosult abszolutizmusa (1780–1790)
5. A 18. századi újjáépítés és a betelepítések következményei
Consolidation: Unit 14 Capstone (20 exercises)
"""

import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

ROOT = Path(".")
LESSONS_DIR = ROOT / "content/hu/lessons/b1"
GRAMMAR_DIR = ROOT / "content/hu/grammar/b1"
VOCAB_DIR = ROOT / "content/hu/vocabulary/b1"
EXERCISES_DIR = ROOT / "content/hu/exercises/b1"
STORIES_DIR = ROOT / "content/hu/stories/world/b1"

def write_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")

def make_story(id_str, title, summary, location, grammar_topics, vocab_topics, paragraphs_text, key_voc, comp_questions):
    paras = [{"type": "narration", "text": p} for p in paragraphs_text]
    total_time = 0.0
    segments = []
    for i, p in enumerate(paragraphs_text):
        dur = max(4.0, round(len(p.split()) * 0.45, 1))
        start = total_time
        end = round(start + dur, 1)
        total_time = end
        segments.append({
            "paraIndex": i,
            "startTime": start,
            "endTime": end,
            "speaker": "Narrator",
            "lang": "hu",
            "cues": [{"type": "pause", "durationMs": 250, "reason": "clause-boundary"}] if i < len(paragraphs_text)-1 else [],
            "pronunciations": []
        })

    return {
        "id": id_str,
        "title": title,
        "level": "B1",
        "estimatedMinutes": 5,
        "summary": summary,
        "characters": [],
        "location": location,
        "grammar": grammar_topics,
        "vocabularyTopics": vocab_topics,
        "paragraphs": paras,
        "narration": {
            "durationSeconds": total_time,
            "pacing": {
                "speedMultiplier": 1.0,
                "rate_str": "+0%",
                "rate_wpm": 150,
                "style": "natural, expressive"
            },
            "speakers": {
                "Narrator": {
                    "role": "narrator",
                    "gender": "neutral",
                    "tone": "clear, warm, steady storytelling guide"
                }
            },
            "segments": segments,
            "pedagogical": {
                "keyVocabulary": key_voc,
                "targetGrammar": grammar_topics,
                "comprehensionQuestions": comp_questions
            }
        }
    }

def make_exercise_group(group_id, title, desc, exercises):
    return {
        "id": group_id,
        "title": title,
        "description": desc,
        "exercises": exercises
    }

def make_lesson(lesson_id, title, grammar_label, intro_body, goals, story_ref, voc_ref, gr_ref, ex_ref, ex_ids):
    sections = [
        {"type": "intro", "title": title.split(" - ")[0] if " - " in title else title, "body": intro_body},
        {"type": "goal", "title": "Lesson Goals", "items": goals},
        {"type": "recycle", "count": 3},
        {"type": "story", "ref": story_ref},
        {"type": "vocabulary", "ref": voc_ref},
        {"type": "grammar", "ref": gr_ref},
        {"type": "exercise-group", "title": "Practice", "ref": ex_ref, "exerciseRefs": ex_ids},
        {"type": "srs"},
        {"type": "checklist", "items": goals}
    ]
    return {
        "id": lesson_id,
        "title": title,
        "level": "B1",
        "track": "citizenship",
        "estimatedMinutes": 15,
        "prerequisites": [],
        "grammar": [grammar_label],
        "vocabulary": [voc_ref],
        "culturalContext": "Magyar történelem és állampolgársági ismeretek (Honosítási tananyag)",
        "sections": sections
    }

# ==========================================
# LESSON 1: b1-mariaterezia-01 (Pragmatica Sanctio 1723)
# ==========================================
story_1 = make_story(
    "story.b1.mariaterezia.01",
    "A Pragmatica Sanctio (1723) és a nőági örökösödés",
    "1723-ban a magyar országgyűlés elfogadta a Pragmatica Sanctiót, amely biztosította a Habsburg-ház nőági örökösödését és a birodalom feloszthatatlanságát.",
    "Pozsony",
    ["Legal conditions and royal charters (örököl, elismeri, hogy, feloszthatatlan)", "Constitutional pacts in Hungarian history"],
    ["Pragmatica Sanctio", "nőági örökösödés", "III. Károly", "feloszthatatlan", "kölcsönös védelem"],
    [
        "A szatmári béke után III. Károly király fiúörökös nélkül maradt, ami a Habsburg Birodalom széthullásával fenyegetett. Hogy ezt elkerülje, az uralkodó az öröklési rend megváltoztatását kérte az osztrák és a magyar rendektől.",
        "Az 1722–1723-as pozsonyi országgyűlésen a magyar nemesség hosszas tárgyalások után elfogadta a Pragmatica Sanctio nevű alaptörvényt. Ez a törvény kimondta a Habsburg-ház nőági trónöröklési jogát, amennyiben a férfiág kihalna.",
        "A Pragmatica Sanctio rögzítette, hogy Magyarország és a Habsburg-tartományok 'feloszthatatlanul és elválaszthatatlanul' (indivisibiliter ac inseparabiliter) kapcsolódnak össze, és kölcsönös védelmi kötelezettséggel tartoznak egymásnak. Cserébe a király megerősítette a magyar rendi jogokat és a nemesi kiváltságokat."
    ],
    [
        {"lemma": "nőági örökösödés", "pos": "noun", "cefr": "B1", "gloss": "female-line succession"},
        {"lemma": "feloszthatatlan", "pos": "adjective", "cefr": "B1", "gloss": "indivisible"},
        {"lemma": "alaptörvény", "pos": "noun", "cefr": "B1", "gloss": "fundamental law, basic constitutional charter"},
        {"lemma": "kihal", "pos": "verb", "cefr": "B1", "gloss": "to die out, become extinct (dynasty)"},
        {"lemma": "kölcsönös", "pos": "adjective", "cefr": "B1", "gloss": "mutual, reciprocal"}
    ],
    [
        {
            "question": "Mit mondott ki az 1723-ban elfogadott Pragmatica Sanctio?",
            "options": ["A Habsburg-ház nőági örökösödését és a birodalom feloszthatatlanságát", "A nemesség adófizetését", "A jobbágyság azonnali eltörlését", "A törökök elleni háborút"],
            "correctIndex": 0,
            "explanation": "A Pragmatica Sanctio a nőági örökösödést és a feloszthatatlan birodalmi szövetséget rögzítette."
        }
    ]
)
write_json(STORIES_DIR / "story.b1.mariaterezia.01.json", story_1)

voc_1 = {
    "id": "voc.b1.mariaterezia.01",
    "title": "A dinasztikus öröklési rend szókincse",
    "description": "Nőági örökösödés, feloszthatatlanság, alaptörvény, dinasztia és kölcsönös védelem.",
    "entries": [
        {"lemma": "nőági örökösödés", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "female-line dynastic succession", "examples": [{"hu": "A Pragmatica Sanctio bevezette a nőági örökösödést.", "en": "The Pragmatic Sanction introduced female-line succession."}]}]},
        {"lemma": "feloszthatatlan", "pos": "adjective", "cefr": "B1", "definitions": [{"meaning": "indivisible, inseverable", "examples": [{"hu": "A birodalom feloszthatatlan és elválaszthatatlan volt.", "en": "The empire was indivisible and inseparable."}]}]},
        {"lemma": "alaptörvény", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "fundamental constitutional law", "examples": [{"hu": "1723-ban új alaptörvényt fogadott el a diéta.", "en": "In 1723, the Diet passed a new fundamental law."}]}]},
        {"lemma": "kihal", "pos": "verb", "cefr": "B1", "definitions": [{"meaning": "to die out in male line", "examples": [{"hu": "A dinasztia férfiága kihalt III. Károllyal.", "en": "The male line of the dynasty died out with Charles III."}]}]},
        {"lemma": "kölcsönös", "pos": "adjective", "cefr": "B1", "definitions": [{"meaning": "mutual, reciprocal obligation", "examples": [{"hu": "A felek kölcsönös védelmi kötelezettséget vállaltak.", "en": "The parties undertook a mutual defense obligation."}]}]}
    ]
}
write_json(VOCAB_DIR / "voc.b1.mariaterezia.01.json", voc_1)

gr_1 = {
    "id": "gr.b1.mariaterezia.01",
    "title": "Jogi feltételek és alaptörvényi fogalmazás (amennyiben, rögzít, kimondja, hogy)",
    "description": "Formulating constitutional pacts and dynastic inheritance rules.",
    "rules": [
        "A törvényi és jogi szövegekben a 'rögzít', 'kimondja, hogy', 'garantál' igék szabatosan fejezik ki az állami döntéseket.",
        "Az 'amennyiben' formális feltételes kötőszó határozza meg a joghatóság érvényesülését: 'amennyiben a férfiág kihal'."
    ],
    "tables": [
        {"headers": ["Jogi kifejezés", "Funkció", "Példa"], "rows": [
            ["amennyiben", "hivatalos feltétel", "Amennyiben nincs fiúörökös, a lány örököl."],
            ["rögzít", "törvénybe foglalás", "A törvény rögzítette a szövetséget."],
            ["kimondja, hogy", "kinyilvánítás", "Kimondja, hogy a birodalom feloszthatatlan."]
        ]}
    ],
    "examples": [
        {"spanish": "A Pragmatica Sanctio rögzítette a Habsburgok és Magyarország közös védelmét.", "english": "The Pragmatic Sanction established the common defense of the Habsburgs and Hungary."},
        {"spanish": "Amennyiben a férfiág kihal, a korona a nőágra száll át.", "english": "In case the male line dies out, the crown passes to the female line."},
        {"spanish": "A magyar rendek elfogadták az új örökösödési alaptörvényt.", "english": "The Hungarian estates accepted the new succession fundamental law."}
    ]
}
write_json(GRAMMAR_DIR / "gr.b1.mariaterezia.01.json", gr_1)

exs_1 = [
    {"id": "ex.b1.mariaterezia.01.01", "type": "multiple-choice", "lesson": "lesson.b1.mariaterezia.01", "teaches": ["Pragmatica-Sanctio-1723"], "prompt": "Melyik évben fogadta el a magyar országgyűlés a Pragmatica Sanctiót?", "options": ["1723-ban", "1711-ben", "1740-ben", "1780-ban"], "correctIndex": 0, "explanation": "A Pragmatica Sanctiót az 1722–1723-as országgyűlés iktatta törvénybe."},
    {"id": "ex.b1.mariaterezia.01.02", "type": "fill-blank", "lesson": "lesson.b1.mariaterezia.01", "teaches": ["noagi-orokosodes"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A törvény biztosította a Habsburg-ház *nőági örökösödését*.", "target": "nőági örökösödését"},
    {"id": "ex.b1.mariaterezia.01.03", "type": "sentence-builder", "lesson": "lesson.b1.mariaterezia.01", "teaches": ["feloszthatatlan", "birodalom"], "prompt": "Rakd össze a mondatot a helyes sorrendben!", "chips": ["A", "birodalom", "és", "Magyarország", "feloszthatatlanul", "összekapcsolódott."], "target": "A birodalom és Magyarország feloszthatatlanul összekapcsolódott.", "english": "The empire and Hungary were indivisibly linked together."},
    {"id": "ex.b1.mariaterezia.01.04", "type": "multiple-choice", "lesson": "lesson.b1.mariaterezia.01", "teaches": ["III-Karoly"], "prompt": "Melyik uralkodó kezdeményezte a Pragmatica Sanctio elfogadását?", "options": ["III. Károly", "I. Lipót", "Mária Terézia", "II. József"], "correctIndex": 0, "explanation": "III. Károly király biztosította leánya trónöröklését a törvénnyel."},
    {"id": "ex.b1.mariaterezia.01.05", "type": "fill-blank", "lesson": "lesson.b1.mariaterezia.01", "teaches": ["alaptorveny"], "prompt": "Egészítsd ki a mondatot a megfelelő szóval!", "sentence": "A Pragmatica Sanctio a Monarchia legfontosabb *alaptörvénye* lett.", "target": "alaptörvénye"},
    {"id": "ex.b1.mariaterezia.01.06", "type": "sentence-builder", "lesson": "lesson.b1.mariaterezia.01", "teaches": ["amennyiben", "orokol"], "prompt": "Alkoss szabályos feltételes jogi mondatot!", "chips": ["Amennyiben", "a", "férfiág", "kihal,", "a", "lány", "örököl."], "target": "Amennyiben a férfiág kihal, a lány örököl.", "english": "In case the male line dies out, the daughter inherits."},
    {"id": "ex.b1.mariaterezia.01.07", "type": "multiple-choice", "lesson": "lesson.b1.mariaterezia.01", "teaches": ["kolcsonos-vedelem"], "prompt": "Milyen kötelezettséget jelentett az országok közötti szövetség?", "options": ["Kölcsönös védelmi kötelezettséget külső támadás esetén", "Minden pénz Bécsbe küldését", "A magyar nyelv betiltását", "Közös vallás kötelező felvételét"], "correctIndex": 0, "explanation": "A Pragmatica Sanctio kölcsönös fegyveres védelmi kötelezettséget rögzített."},
    {"id": "ex.b1.mariaterezia.01.08", "type": "fill-blank", "lesson": "lesson.b1.mariaterezia.01", "teaches": ["kolcsonos"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A két országrész *kölcsönös* segítséget nyújtott egymásnak.", "target": "kölcsönös"}
]
write_json(EXERCISES_DIR / "ex.b1.mariaterezia.01.json", make_exercise_group("ex.b1.mariaterezia.01", "A Pragmatica Sanctio gyakorlatai", "Gyakorlatok az 1723-as örökösödési alaptörvényről és a feltételes jogi kifejezésekről.", exs_1))

lesson_1 = make_lesson(
    "lesson.b1.mariaterezia.01",
    "A Pragmatica Sanctio (1723) és a nőági örökösödés",
    "Jogi feltételek és alaptörvényi fogalmazás (amennyiben, rögzít)",
    "Megtanuljuk a Pragmatica Sanctio okait, a nőági örökösödés bevezetését és a feloszthatatlan birodalmi kapcsolatot.",
    ["Megérteni az 1723-as Pragmatica Sanctio történelmi jelentőségét", "Használni a jogi és feltételes alaptörvényi nyelvezetet", "Ismerni a nőági örökösödés és a kölcsönös védelem elvét"],
    "story.b1.mariaterezia.01",
    "voc.b1.mariaterezia.01",
    "gr.b1.mariaterezia.01",
    "ex.b1.mariaterezia.01",
    [e["id"] for e in exs_1]
)
write_json(LESSONS_DIR / "lesson.b1.mariaterezia.01.json", lesson_1)


# ==========================================
# LESSON 2: b1-mariaterezia-02 (Mária Terézia és a pozsonyi országgyűlés 1741)
# ==========================================
story_2 = make_story(
    "story.b1.mariaterezia.02",
    "Mária Terézia és a pozsonyi országgyűlés (1741, 'Vitam et sanguinem!')",
    "1740-ben a fiatal Mária Terézia lépett a trónra. Amikor Európa uralkodói megtámadták a birodalmat, a magyar nemesség 'Életünket és vérünket!' felkiáltással mentette meg a királynőt.",
    "Pozsonyi Vár és Prímási Palota",
    ["Exclamatory oaths and loyalty declarations (felajánl, hűséget esküszik, megment)", "Historic royal audiences"],
    ["Mária Terézia", "Vitam et sanguinem", "pozsonyi országgyűlés", "osztrák örökösödési háború", "nemesi hűség"],
    [
        "1740-ben, alig huszonhárom évesen lépett a trónra Mária Terézia (1740–1780). A szomszédos nagyhatalmak – élükön II. Frigyes porosz királlyal – nem ismerték el a nőági örökösödést, és azonnal megtámadták a birodalmat, kitörve az osztrák örökösödési háborút.",
        "A végveszélybe került fiatal királynő 1741 szeptemberében a pozsonyi országgyűléshez fordult segítségért. Gyászruhában, csecsemő fiával (a későbbi II. Józseffel) a karján jelent meg a magyar rendek előtt, védelmet és segítséget kérve.",
        "A magyar nemességet magával ragadta a királynő személye és bizalma. A nemesek kardjukat rántva egy emberként kiáltották: 'Vitam et sanguinem pro rege nostro Maria Theresia!' (Életünket és vérünket királyunkért, Mária Teréziáért!). A magyar huszárok és felkelt nemesi csapatok döntő szerepet játszottak a birodalom és a Habsburg-trón megmentésében."
    ],
    [
        {"lemma": "örökösödési háború", "pos": "noun", "cefr": "B1", "gloss": "war of succession"},
        {"lemma": "kardot ránt", "pos": "verb", "cefr": "B1", "gloss": "to draw one's sword"},
        {"lemma": "hűségeskü", "pos": "noun", "cefr": "B1", "gloss": "oath of fealty, loyalty pledge"},
        {"lemma": "felajánl", "pos": "verb", "cefr": "B1", "gloss": "to offer, volunteer (troops/support)"},
        {"lemma": "végveszély", "pos": "noun", "cefr": "B1", "gloss": "mortal danger, extreme crisis"}
    ],
    [
        {
            "question": "Mit kiáltottak a magyar nemesek a pozsonyi országgyűlésen 1741-ben?",
            "options": ["Vitam et sanguinem! (Életünket és vérünket!)", "Eb ura fakó!", "Cum Deo pro Patria!", "Ne bántsd a magyart!"],
            "correctIndex": 0,
            "explanation": "A magyar rendek 'Vitam et sanguinem!' felkiáltással ajánlották fel segítségüket Mária Teréziának."
        }
    ]
)
write_json(STORIES_DIR / "story.b1.mariaterezia.02.json", story_2)

voc_2 = {
    "id": "voc.b1.mariaterezia.02",
    "title": "A nemesi hűség és trónvédelem szókincse",
    "description": "Örökösödési háború, kardrántás, hűségeskü, végveszély és felajánlás.",
    "entries": [
        {"lemma": "örökösödési háború", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "war of succession", "examples": [{"hu": "Az osztrák örökösödési háború 1740-ben robbant ki.", "en": "The War of the Austrian Succession broke out in 1740."}]}]},
        {"lemma": "kardot ránt", "pos": "verb", "cefr": "B1", "definitions": [{"meaning": "to draw sword in pledge", "examples": [{"hu": "A nemesek kardot rántottak a királynőért.", "en": "The nobles drew their swords for the queen."}]}]},
        {"lemma": "hűségeskü", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "oath of loyalty, fealty pledge", "examples": [{"hu": "A rendek hűségesküt tettek Pozsonyban.", "en": "The estates swore an oath of fealty in Pozsony."}]}]},
        {"lemma": "felajánl", "pos": "verb", "cefr": "B1", "definitions": [{"meaning": "to offer troops or support", "examples": [{"hu": "A magyarok katonákat és gabonát ajánlottak fel.", "en": "The Hungarians offered soldiers and grain."}]}]},
        {"lemma": "végveszély", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "extreme mortal danger", "examples": [{"hu": "A királynő a végveszély pillanatában kért segítséget.", "en": "The queen asked for help in the moment of extreme danger."}]}]}
    ]
}
write_json(VOCAB_DIR / "voc.b1.mariaterezia.02.json", voc_2)

gr_2 = {
    "id": "gr.b1.mariaterezia.02",
    "title": "Felkiáltó és elköteleződést kifejező szerkezetek (felajánl, hűséget fogad, kiált)",
    "description": "Expressing dramatic historical speeches, collective oaths, and noble declarations.",
    "rules": [
        "A felkiáltó és hűségnyilatkozatokban a tárgyas és határozós vonzatok ('életét adja valamiért', 'hűséget esküszik valakinek') jelenítik meg a drámai elkötelezettséget.",
        "Az egyenes idézés beékelése ('Vitam et sanguinem!') hitelesíti a történelmi narratívát."
    ],
    "tables": [
        {"headers": ["Szerkezet", "Jelentés", "Példa"], "rows": [
            ["hűséget esküszik", "to swear fealty", "Hűséget esküdtek a királynőnek."],
            ["felajánl valamit valamiért", "to offer in sacrifice", "Életüket ajánlották fel a trónért."],
            ["kiáltja, hogy...", "to exclaim", "Egy emberként kiáltották: segítünk!"]
        ]}
    ],
    "examples": [
        {"spanish": "A nemesek felajánlották fegyvereiket és életüket Mária Terézia megvédésére.", "english": "The nobles offered their weapons and lives to defend Maria Theresa."},
        {"spanish": "Pozsonyban a rendek hűséget esküdtek a fiatal uralkodónőnek.", "english": "In Pozsony, the estates swore loyalty to the young sovereign."},
        {"spanish": "A magyar huszárok megmentették a birodalmat a porosz és francia támadásoktól.", "english": "The Hungarian hussars saved the empire from Prussian and French attacks."}
    ]
}
write_json(GRAMMAR_DIR / "gr.b1.mariaterezia.02.json", gr_2)

exs_2 = [
    {"id": "ex.b1.mariaterezia.02.01", "type": "multiple-choice", "lesson": "lesson.b1.mariaterezia.02", "teaches": ["Maria-Terezia-1740"], "prompt": "Melyik évszámok között uralkodott Mária Terézia?", "options": ["1740–1780", "1703–1711", "1780–1790", "1848–1849"], "correctIndex": 0, "explanation": "Mária Terézia negyven évig, 1740-től 1780-ig uralkodott."},
    {"id": "ex.b1.mariaterezia.02.02", "type": "fill-blank", "lesson": "lesson.b1.mariaterezia.02", "teaches": ["felajanl"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A nemesek katonai segítséget *ajánlottak fel* a királynőnek.", "target": "ajánlottak fel"},
    {"id": "ex.b1.mariaterezia.02.03", "type": "sentence-builder", "lesson": "lesson.b1.mariaterezia.02", "teaches": ["Vitam-et-sanguinem", "nemesseg"], "prompt": "Rakd össze a híres felkiáltást helyes sorrendben!", "chips": ["Életünket", "és", "vérünket", "ajánljuk", "a", "királynőért!"], "target": "Életünket és vérünket ajánljuk a királynőért!", "english": "We offer our life and our blood for the queen!"},
    {"id": "ex.b1.mariaterezia.02.04", "type": "multiple-choice", "lesson": "lesson.b1.mariaterezia.02", "teaches": ["pozsonyi-1741"], "prompt": "Hol tartották az 1741-es híres országgyűlést?", "options": ["Pozsonyban", "Budán", "Bécsben", "Székesfehérváron"], "correctIndex": 0, "explanation": "A koronázóvárosban, Pozsonyban rendezték meg az 1741-es országgyűlést."},
    {"id": "ex.b1.mariaterezia.02.05", "type": "fill-blank", "lesson": "lesson.b1.mariaterezia.02", "teaches": ["husegesku"], "prompt": "Egészítsd ki a mondatot a megfelelő szóval!", "sentence": "A magyar nemesség letette a *hűségesküt* a pozsonyi várban.", "target": "hűségesküt"},
    {"id": "ex.b1.mariaterezia.02.06", "type": "sentence-builder", "lesson": "lesson.b1.mariaterezia.02", "teaches": ["kardot-rant", "rendek"], "prompt": "Alkoss szabályos mondatot!", "chips": ["A", "magyar", "rendek", "lelkesen", "kardot", "rántottak."], "target": "A magyar rendek lelkesen kardot rántottak.", "english": "The Hungarian estates enthusiastically drew their swords."},
    {"id": "ex.b1.mariaterezia.02.07", "type": "multiple-choice", "lesson": "lesson.b1.mariaterezia.02", "teaches": ["huszarok"], "prompt": "Melyik híres magyar fegyvernem mentette meg a királynő trónját?", "options": ["A magyar huszárok (könnyűlovasság)", "A tengerészek", "A nehéztüzérség", "A janicsárok"], "correctIndex": 0, "explanation": "A magyar huszárok bravúros haditettei döntő szerepet játszottak a háborúban."},
    {"id": "ex.b1.mariaterezia.02.08", "type": "fill-blank", "lesson": "lesson.b1.mariaterezia.02", "teaches": ["vegveszely"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A Habsburg Birodalom a szétesés közvetlen *végveszélyében* volt.", "target": "végveszélyében"}
]
write_json(EXERCISES_DIR / "ex.b1.mariaterezia.02.json", make_exercise_group("ex.b1.mariaterezia.02", "Mária Terézia és az 1741-es országgyűlés gyakorlatai", "Gyakorlatok a 'Vitam et sanguinem' eseményről és a hűségnyilatkozatokról.", exs_2))

lesson_2 = make_lesson(
    "lesson.b1.mariaterezia.02",
    "Mária Terézia és a pozsonyi országgyűlés (1741, 'Vitam et sanguinem!')",
    "Felkiáltó és elköteleződést kifejező szerkezetek (felajánl, hűséget esküszik)",
    "Megismerjük Mária Terézia trónra lépését, az 1741-es pozsonyi országgyűlést és a magyar nemesség 'Vitam et sanguinem' felajánlását.",
    ["Megérteni az 1741-es pozsonyi jelenet történelmi hátterét", "Használni a hűségnyilatkozatok és felajánlások kifejezéseit", "Ismerni Mária Terézia és a magyar nemesség kapcsolatát"],
    "story.b1.mariaterezia.02",
    "voc.b1.mariaterezia.02",
    "gr.b1.mariaterezia.02",
    "ex.b1.mariaterezia.02",
    [e["id"] for e in exs_2]
)
write_json(LESSONS_DIR / "lesson.b1.mariaterezia.02.json", lesson_2)


# ==========================================
# LESSON 3: b1-mariaterezia-03 (Urbárium és Ratio Educationis)
# ==========================================
story_3 = make_story(
    "story.b1.mariaterezia.03",
    "Mária Terézia reformjai: Urbárium (1767) és Ratio Educationis (1777)",
    "Mária Terézia felvilágosult rendeleteivel védte a jobbágyokat a túlzott földesúri kizsákmányolástól, és megteremtette a kötelező állami alapfokú oktatást.",
    "Bécs és Buda",
    ["Regulatory and reform structures (szabályoz, elrendel, köteles)", "Educational and social reforms"],
    ["Urbárium", "Ratio Educationis", "jobbágyvédelem", "robot", "oktatási reform"],
    [
        "Mária Terézia uralkodása második felében felvilágosult abszolutista reformokkal modernizálta az országot. Felismerte, hogy az adófizető jobbágyság túlzott kizsákmányolása a kincstár bevételeit veszélyezteti, ezért 1767-ben kiadta az Urbárium nevű rendeletet.",
        "Az Urbárium pontosan rögzítette a jobbágytelkek nagyságát, és maximálta a földesúrnak teljesítendő kötelezettségeket: a heti robot mértékét évi 52 igás vagy 104 gyalogos napban szabta meg. Ezzel a királynő törvényi védelmet nyújtott a parasztságnak az önkénnyel szemben.",
        "1777-ben Mária Terézia kibocsátotta az oktatás átfogó reformját, a Ratio Educationist. Ez a rendelet az állam feladatává tette az iskolák felügyeletét, egységes tantervet vezetett be, és 6-tól 12 éves korig minden gyermek számára kötelezővé tette az alapfokú anyanyelvi iskoláztatást."
    ],
    [
        {"lemma": "jobbágyvédelem", "pos": "noun", "cefr": "B1", "gloss": "serf / peasant protection by royal decree"},
        {"lemma": "robot", "pos": "noun", "cefr": "B1", "gloss": "corvée, unpaid feudal forced labor"},
        {"lemma": "tanterv", "pos": "noun", "cefr": "B1", "gloss": "curriculum, syllabus"},
        {"lemma": "kötelező", "pos": "adjective", "cefr": "B1", "gloss": "compulsory, mandatory"},
        {"lemma": "szabályoz", "pos": "verb", "cefr": "B1", "gloss": "to regulate, standardize"}
    ],
    [
        {
            "question": "Mit szabályozott Mária Terézia 1767-es Urbárium rendelete?",
            "options": ["A jobbágyok földesúri terheit és a robot pontos mértékét", "A nemesség adófizetését", "A vasútvonalak építését", "A hadsereg egyenruháját"],
            "correctIndex": 0,
            "explanation": "Az Urbárium rögzítette a jobbágytelkek méretét és korlátozta a robot mértékét."
        }
    ]
)
write_json(STORIES_DIR / "story.b1.mariaterezia.03.json", story_3)

voc_3 = {
    "id": "voc.b1.mariaterezia.03",
    "title": "A felvilágosult reformok és oktatás szókincse",
    "description": "Urbárium, Ratio Educationis, robot, tanterv, szabályozás és kötelező oktatás.",
    "entries": [
        {"lemma": "jobbágyvédelem", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "royal policy protecting peasants against noble exploitation", "examples": [{"hu": "Az Urbárium a jobbágyvédelem fontos lépése volt.", "en": "The Urbarium was an important step in peasant protection."}]}]},
        {"lemma": "robot", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "unpaid corvée labor owed to the landlord", "examples": [{"hu": "A rendelet korlátozta a heti robot mértékét.", "en": "The decree limited the amount of weekly corvée labor."}]}]},
        {"lemma": "tanterv", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "curriculum, educational syllabus", "examples": [{"hu": "A Ratio Educationis egységes tantervet vezetett be.", "en": "The Ratio Educationis introduced a standardized curriculum."}]}]},
        {"lemma": "kötelező", "pos": "adjective", "cefr": "B1", "definitions": [{"meaning": "compulsory, mandatory by law", "examples": [{"hu": "Az alapfokú oktatás kötelezővé vált a gyermekeknek.", "en": "Primary education became compulsory for children."}]}]},
        {"lemma": "szabályoz", "pos": "verb", "cefr": "B1", "definitions": [{"meaning": "to regulate, standardize by decree", "examples": [{"hu": "A királynő rendelettel szabályozta az iskolákat.", "en": "The queen regulated schools by decree."}]}]}
    ]
}
write_json(VOCAB_DIR / "voc.b1.mariaterezia.03.json", voc_3)

gr_3 = {
    "id": "gr.b1.mariaterezia.03",
    "title": "Szabályozó és kötelezettséget kifejező szerkezetek (szabályoz, köteles, előír)",
    "description": "Expressing state regulations, compulsory laws, and legal duties.",
    "rules": [
        "A kötelezettség kifejezésére a 'köteles + főnévi igenév' (köteles iskolába járni) vagy az 'előírja, hogy + felszólító mód' szerkezetet használjuk.",
        "A rendeleti szabályozást a 'szabályoz', 'elrendel', 'maximál' igék írják le pontosan."
    ],
    "tables": [
        {"headers": ["Kifejezés", "Funkció", "Példa"], "rows": [
            ["köteles (tenni)", "kötelezettség", "Minden gyermek köteles volt tanulni."],
            ["előírja, hogy...", "szabályozás", "A rendelet előírja, hogy csökkenjen a robot."],
            ["szabályoz", "rendszerezés", "Az Urbárium szabályozta az adókat."]
        ]}
    ],
    "examples": [
        {"spanish": "A Ratio Educationis előírta, hogy a gyermekek 6 és 12 éves kor között iskolába járjanak.", "english": "The Ratio Educationis prescribed that children between ages 6 and 12 attend school."},
        {"spanish": "A földesúr nem követelhetett több robotot, mint amennyit a rendelet engedélyezett.", "english": "The landlord could not demand more corvée than the decree permitted."},
        {"spanish": "Mária Terézia felvilágosult rendeletekkel szabályozta az ország életét.", "english": "Maria Theresa regulated the country's life with enlightened decrees."}
    ]
}
write_json(GRAMMAR_DIR / "gr.b1.mariaterezia.03.json", gr_3)

exs_3 = [
    {"id": "ex.b1.mariaterezia.03.01", "type": "multiple-choice", "lesson": "lesson.b1.mariaterezia.03", "teaches": ["Urbarium-1767"], "prompt": "Melyik évben adta ki Mária Terézia az Urbáriumot?", "options": ["1767-ben", "1741-ben", "1777-ben", "1723-ban"], "correctIndex": 0, "explanation": "Az úrbéri rendeletet (Urbárium) 1767-ben bocsátotta ki a királynő."},
    {"id": "ex.b1.mariaterezia.03.02", "type": "fill-blank", "lesson": "lesson.b1.mariaterezia.03", "teaches": ["robot"], "prompt": "Egészítsd ki a mondatot!", "sentence": "Az Urbárium pontosan meghatározta a földesúrnak járó *robot* mértékét.", "target": "robot"},
    {"id": "ex.b1.mariaterezia.03.03", "type": "sentence-builder", "lesson": "lesson.b1.mariaterezia.03", "teaches": ["koteles", "iskola"], "prompt": "Rakd össze a kötelezettséget kifejező mondatot!", "chips": ["Minden", "gyermek", "köteles", "volt", "iskolába", "járni."], "target": "Minden gyermek köteles volt iskolába járni.", "english": "Every child was obliged to attend school."},
    {"id": "ex.b1.mariaterezia.03.04", "type": "multiple-choice", "lesson": "lesson.b1.mariaterezia.03", "teaches": ["Ratio-Educationis-1777"], "prompt": "Miről rendelkezett az 1777-es Ratio Educationis?", "options": ["Az egységes és kötelező állami alapfokú oktatásról", "A hadsereg toborzásáról", "A vámhatárokról", "Az erdők védelméről"], "correctIndex": 0, "explanation": "A Ratio Educationis az oktatásügy átfogó állami szabályozása volt 1777-ben."},
    {"id": "ex.b1.mariaterezia.03.05", "type": "fill-blank", "lesson": "lesson.b1.mariaterezia.03", "teaches": ["tanterv"], "prompt": "Egészítsd ki a mondatot!", "sentence": "Az oktatási rendelet egységes *tantervet* vezetett be az iskolákban.", "target": "tantervet"},
    {"id": "ex.b1.mariaterezia.03.06", "type": "sentence-builder", "lesson": "lesson.b1.mariaterezia.03", "teaches": ["szabalyoz", "jobbagyvedelem"], "prompt": "Alkoss szabályos összetett mondatot!", "chips": ["A", "királynő", "rendelettel", "szabályozta", "a", "jobbágyok", "terheit."], "target": "A királynő rendelettel szabályozta a jobbágyok terheit.", "english": "The queen regulated the burdens of the serfs by decree."},
    {"id": "ex.b1.mariaterezia.03.07", "type": "multiple-choice", "lesson": "lesson.b1.mariaterezia.03", "teaches": ["eletkor-oktatas"], "prompt": "Hány éves kortól hány éves korig tette kötelezővé az oktatást a Ratio Educationis?", "options": ["6-tól 12 éves korig", "10-től 18 éves korig", "Csak 14 éves kor felett", "Minden korban önkéntes maradt"], "correctIndex": 0, "explanation": "A 6 és 12 év közötti gyermekek számára írta elő az iskoláztatást."},
    {"id": "ex.b1.mariaterezia.03.08", "type": "fill-blank", "lesson": "lesson.b1.mariaterezia.03", "teaches": ["kotelezove-tesz"], "prompt": "Egészítsd ki a mondatot a megfelelő szóval!", "sentence": "Az állam *kötelezővé* tette az anyanyelvi alapoktatást.", "target": "kötelezővé"}
]
write_json(EXERCISES_DIR / "ex.b1.mariaterezia.03.json", make_exercise_group("ex.b1.mariaterezia.03", "Mária Terézia reformjai gyakorlatok", "Gyakorlatok az Urbáriumról, a Ratio Educationisról és a kötelezettséget kifejező szerkezetekről.", exs_3))

lesson_3 = make_lesson(
    "lesson.b1.mariaterezia.03",
    "Mária Terézia reformjai: Urbárium (1767) és Ratio Educationis (1777)",
    "Szabályozó és kötelezettséget kifejező szerkezetek (köteles, szabályoz, előír)",
    "Részletesen elemezzük az 1767-es Urbárium jobbágyvédelmi cikkelyeit és az 1777-es Ratio Educationis oktatási reformját.",
    ["Megérteni az Urbárium (1767) és Ratio Educationis (1777) jelentőségét", "Használni a szabályozó és kötelezettséget kifejező nyelvtani szerkezeteket", "Ismerni a robot és az alapfokú oktatás történeti szabályait"],
    "story.b1.mariaterezia.03",
    "voc.b1.mariaterezia.03",
    "gr.b1.mariaterezia.03",
    "ex.b1.mariaterezia.03",
    [e["id"] for e in exs_3]
)
write_json(LESSONS_DIR / "lesson.b1.mariaterezia.03.json", lesson_3)


# ==========================================
# LESSON 4: b1-mariaterezia-04 (II. József a kalapos király)
# ==========================================
story_4 = make_story(
    "story.b1.mariaterezia.04",
    "II. József, a 'kalapos király' felvilágosult abszolutizmusa (1780–1790)",
    "II. József nem koronáztatta meg magát a Szent Koronával, és rendeletek ezreivel próbálta modernizálni a birodalmat, de a nemesi ellenállás miatt halálos ágyán szinte mindent visszavont.",
    "Bécs és Buda",
    ["Contrast of enlightened reforms and resistance (annak ellenére, hogy, visszavon, kötelezővé tesz)", "Enlightened absolutism and national resistance"],
    ["II. József", "kalapos király", "türelmi rendelet", "jobbágyrendelet", "nyelvrendelet"],
    [
        "Mária Terézia fia, II. József (1780–1790) a felvilágosult abszolutizmus legkövetkezetesebb képviselője volt. Nem koronáztatta meg magát a magyar Szent Koronával, hogy ne kösse a rendi alkotmány és a koronázási eskü – ezért nevezte el a nép 'kalapos királynak'.",
        "Több mint hatezer rendeletet adott ki tízéves uralkodása alatt. 1781-ben kiadta a korszakalkotó türelmi rendeletet (szabad vallásgyakorlat a protestánsoknak és ortodoxoknak, hivatalviselési jog), majd 1785-ben eltörölte az örökös jobbágyságot, biztosítva a parasztok szabad költözködési jogát.",
        "Azonban amikor 1784-ben a birodalmi egységesítés nevében a német nyelvet tette kötelezővé a közigazgatásban a latin helyett, országos nemzeti ellenállás robbant ki. 1790-ben halálos ágyán – a türelmi rendelet és a jobbágyrendelet kivételével – az úgynevezett 'nevezetes tollvonással' minden rendeletét visszavonta."
    ],
    [
        {"lemma": "kalapos király", "pos": "noun", "cefr": "B1", "gloss": "the 'Hatted King' (uncrowned Joseph II)"},
        {"lemma": "türelmi rendelet", "pos": "noun", "cefr": "B1", "gloss": "Edict of Toleration"},
        {"lemma": "jobbágyrendelet", "pos": "noun", "cefr": "B1", "gloss": "Serfdom Edict (abolishing perpetual serfdom)"},
        {"lemma": "visszavon", "pos": "verb", "cefr": "B1", "gloss": "to withdraw, revoke, repeal"},
        {"lemma": "ellenállás", "pos": "noun", "cefr": "B1", "gloss": "resistance, opposition"}
    ],
    [
        {
            "question": "Miért nevezték II. Józsefet 'kalapos királynak'?",
            "options": ["Mert nem koronáztatta meg magát a magyar Szent Koronával, hogy ne kössék a törvények", "Mert divatos kalapokat hordott", "Mert a kalaposok céhének tagja volt", "Mert a katonái kalapot viseltek"],
            "correctIndex": 0,
            "explanation": "II. József elutasította a megkoronázást, ezért kapta a 'kalapos király' nevet."
        }
    ]
)
write_json(STORIES_DIR / "story.b1.mariaterezia.04.json", story_4)

voc_4 = {
    "id": "voc.b1.mariaterezia.04",
    "title": "A felvilágosult abszolutizmus szókincse",
    "description": "Kalapos király, türelmi rendelet, jobbágyrendelet, nyelvrendelet és ellenállás.",
    "entries": [
        {"lemma": "kalapos király", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "popular moniker for Joseph II who refused coronation", "examples": [{"hu": "II. Józsefet a népnyelv kalapos királynak nevezte.", "en": "Folk language named Joseph II the hatted king."}]}]},
        {"lemma": "türelmi rendelet", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "Edict of Toleration for non-Catholics (1781)", "examples": [{"hu": "Az 1781-es türelmi rendelet vallásszabadságot hozott.", "en": "The 1781 Edict of Toleration brought religious freedom."}]}]},
        {"lemma": "jobbágyrendelet", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "edict granting free movement to serfs (1785)", "examples": [{"hu": "A jobbágyrendelet megszüntette az örökös jobbágyságot.", "en": "The serfdom edict ended perpetual bondage."}]}]},
        {"lemma": "visszavon", "pos": "verb", "cefr": "B1", "definitions": [{"meaning": "to revoke, repeal edicts on deathbed", "examples": [{"hu": "A király halála előtt visszavonta rendeleteit.", "en": "The king revoked his decrees before his death."}]}]},
        {"lemma": "ellenállás", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "resistance against centralizing reforms", "examples": [{"hu": "A német nyelvrendelet nemzeti ellenállást váltott ki.", "en": "The German language decree provoked national resistance."}]}]}
    ]
}
write_json(VOCAB_DIR / "voc.b1.mariaterezia.04.json", voc_4)

gr_4 = {
    "id": "gr.b1.mariaterezia.04",
    "title": "Reformok és ellentmondások kifejezése (annak ellenére, hogy, visszavon, kivételével)",
    "description": "Contrasting radical modernizing attempts with conservative resistance.",
    "rules": [
        "A 'kivételével' névutó a rendeleti kivételeket jelöli pontosan: 'két rendelet kivételével minden mást visszavont'.",
        "A reformok gyorsaságát és ellenhatását az 'annak ellenére, hogy...' és 'eredményeként' szerkezetek illusztrálják."
    ],
    "tables": [
        {"headers": ["Kifejezés", "Funkció", "Példa"], "rows": [
            ["kivételével", "kivétel megjelölése", "A türelmi rendelet kivételével mindent visszavont."],
            ["annak ellenére, hogy", "ellentét / paradoxon", "Annak ellenére, hogy jót akart, megbukott."],
            ["visszavon", "hatálytalanítás", "Visszavonta a törvényeket."]
        ]}
    ],
    "examples": [
        {"spanish": "A türelmi rendelet és a jobbágyrendelet kivételével II. József minden rendelkezését visszavonta.", "english": "With the exception of the Edict of Toleration and the Serfdom Edict, Joseph II revoked all his provisions."},
        {"spanish": "Annak ellenére, hogy a király modernizálni akart, nemesi ellenállásba ütközött.", "english": "Despite the fact that the king wanted to modernize, he ran into noble resistance."},
        {"spanish": "A német nyelvrendelet felébresztette a magyar nemzeti öntudatot.", "english": "The German language edict awakened Hungarian national consciousness."}
    ]
}
write_json(GRAMMAR_DIR / "gr.b1.mariaterezia.04.json", gr_4)

exs_4 = [
    {"id": "ex.b1.mariaterezia.04.01", "type": "multiple-choice", "lesson": "lesson.b1.mariaterezia.04", "teaches": ["kalapos-kiraly"], "prompt": "Melyik uralkodót nevezték 'kalapos királynak'?", "options": ["II. Józsefet", "Mária Teréziát", "III. Károlyt", "I. Ferencet"], "correctIndex": 0, "explanation": "II. József volt a 'kalapos király' (1780–1790)."},
    {"id": "ex.b1.mariaterezia.04.02", "type": "fill-blank", "lesson": "lesson.b1.mariaterezia.04", "teaches": ["turelmi-rendelet"], "prompt": "Egészítsd ki a mondatot!", "sentence": "Az 1781-es *türelmi rendelet* szabad vallásgyakorlatot biztosított a protestánsoknak.", "target": "türelmi rendelet"},
    {"id": "ex.b1.mariaterezia.04.03", "type": "sentence-builder", "lesson": "lesson.b1.mariaterezia.04", "teaches": ["kivetelevel", "visszavon"], "prompt": "Rakd össze a mondatot helyes sorrendben!", "chips": ["Két", "rendelet", "kivételével", "mindent", "visszavont", "a", "halálos", "ágyán."], "target": "Két rendelet kivételével mindent visszavont a halálos ágyán.", "english": "With the exception of two decrees, he revoked everything on his deathbed."},
    {"id": "ex.b1.mariaterezia.04.04", "type": "multiple-choice", "lesson": "lesson.b1.mariaterezia.04", "teaches": ["jobbagyrendelet-1785"], "prompt": "Mit adott meg a parasztoknak az 1785-ös jobbágyrendelet?", "options": ["A szabad költözködés jogát és az örökös jobbágyság megszüntetését", "Ingyen földet", "Nemesi rangot mindenkinek", "Adómentességet"], "correctIndex": 0, "explanation": "A jobbágyrendelet megszüntette a röghöz kötöttséget (szabad költözködés)."},
    {"id": "ex.b1.mariaterezia.04.05", "type": "fill-blank", "lesson": "lesson.b1.mariaterezia.04", "teaches": ["visszavon"], "prompt": "Egészítsd ki a mondatot a megfelelő igealakkal!", "sentence": "A király halála előtt *visszavonta* a legtöbb rendeletét.", "target": "visszavonta"},
    {"id": "ex.b1.mariaterezia.04.06", "type": "sentence-builder", "lesson": "lesson.b1.mariaterezia.04", "teaches": ["nemet-nyelv", "ellenallas"], "prompt": "Alkoss szabályos történelmi mondatot!", "chips": ["A", "német", "nyelvrendelet", "hatalmas", "nemzeti", "ellenállást", "szült."], "target": "A német nyelvrendelet hatalmas nemzeti ellenállást szült.", "english": "The German language decree bred immense national resistance."},
    {"id": "ex.b1.mariaterezia.04.07", "type": "multiple-choice", "lesson": "lesson.b1.mariaterezia.04", "teaches": ["nevezetes-tollvonas"], "prompt": "Mit nevez a történelem II. József 'nevezetes tollvonásának'?", "options": ["A rendeletei visszavonását a halálos ágyán 1790-ben", "A korona átvételét", "A bécsi palota megépítését", "Az új pénz bevezetését"], "correctIndex": 0, "explanation": "A halálos ágyán tett tollvonással vonta vissza majdnem minden reformját."},
    {"id": "ex.b1.mariaterezia.04.08", "type": "fill-blank", "lesson": "lesson.b1.mariaterezia.04", "teaches": ["ellenallas"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A magyar nemesség az alkotmányos jogokért küzdve tanúsított *ellenállást*.", "target": "ellenállást"}
]
write_json(EXERCISES_DIR / "ex.b1.mariaterezia.04.json", make_exercise_group("ex.b1.mariaterezia.04", "II. József kora gyakorlatok", "Gyakorlatok a kalapos királyról, a türelmi rendeletről és a kivételt kifejező szerkezetekről.", exs_4))

lesson_4 = make_lesson(
    "lesson.b1.mariaterezia.04",
    "II. József, a 'kalapos király' felvilágosult abszolutizmusa (1780–1790)",
    "Reformok és ellentmondások kifejezése (kivételével, visszavon)",
    "Megismerjük II. József uralkodását, a türelmi és jobbágyrendeletet, a nyelvrendeletet és a halálos ágyon tett tollvonást.",
    ["Megérteni II. József felvilágosult reformjait és hibáit", "Használni a kivételt és ellentmondást kifejező szerkezeteket (kivételével)", "Ismerni a 'kalapos király' és a türelmi rendelet fogalmát"],
    "story.b1.mariaterezia.04",
    "voc.b1.mariaterezia.04",
    "gr.b1.mariaterezia.04",
    "ex.b1.mariaterezia.04",
    [e["id"] for e in exs_4]
)
write_json(LESSONS_DIR / "lesson.b1.mariaterezia.04.json", lesson_4)


# ==========================================
# LESSON 5: b1-mariaterezia-05 (18. századi újjáépítés és betelepítések)
# ==========================================
story_5 = make_story(
    "story.b1.mariaterezia.05",
    "A 18. századi újjáépítés és a betelepítések következményei",
    "A török hódoltság után a 18. században az elnéptelenedett területek betelepítésével Magyarország soknemzetiségű országgá vált, miközben virágzásnak indult a mezőgazdaság.",
    "Bácska, Bánát és a Duna menti sváb falvak",
    ["Demographic and population development clauses (arányában, következtében, betelepül)", "Socio-demographic transformations"],
    ["újjáépítés", "betelepítés", "dunai svábok", "soknemzetiségű ország", "mezőgazdasági fejlődés"],
    [
        "A másfél évszázados török háborúk és a járványok következtében a Magyar Királyság népessége katasztrofális mértékben lecsökkent: a termékeny Alföld és a déli végek szinte teljesen elnéptelenedtek. A 18. századi béke idején megindult a hatalmas méretű újjáépítés és népességpótlás.",
        "A Habsburg kormányzat és a nagybirtokosok szervezett betelepítésekkel katolikus német (sváb) telepeseket hoztak be a birodalom nyugati tartományaiból, adókedvezményekkel segítve letelepedésüket. Emellett spontán belső vándorlással szlovákok költöztek délebbre, míg a határokon át nagyszámú román és szerb népesség érkezett Erdélybe és a Bánságba.",
        "A folyamat következtében a 18. század végére Magyarország lakossága megháromszorozódott (mintegy 9,5 millió főre emelkedett), azonban a magyarság számaránya saját hazájában 50% alá esett. Ezzel Magyarország jellegzetesen soknemzetiségű állammá alakult át, ami meghatározta a következő évszázadok nemzetiségi kérdéseit."
    ],
    [
        {"lemma": "betelepítés", "pos": "noun", "cefr": "B1", "gloss": "settlement / organized resettlement of populations"},
        {"lemma": "dunai svábok", "pos": "noun", "cefr": "B1", "gloss": "Danube Swabians (German settlers)"},
        {"lemma": "soknemzetiségű", "pos": "adjective", "cefr": "B1", "gloss": "multiethnic, multinational"},
        {"lemma": "számarány", "pos": "noun", "cefr": "B1", "gloss": "proportion, percentage of population"},
        {"lemma": "megháromszorozódik", "pos": "verb", "cefr": "B1", "gloss": "to triple in number"}
    ],
    [
        {
            "question": "Hogyan változott meg Magyarország etnikai összetétele a 18. századi betelepítések nyomán?",
            "options": ["Soknemzetiségű országgá vált, ahol a magyarság aránya 50% körülire csökkent", "Teljesen homogén magyar állam lett", "Csak németek éltek az országban", "Minden lakos elköltözött külföldre"],
            "correctIndex": 0,
            "explanation": "A betelepítések nyomán (svábok, szlovákok, románok, szerbek) az ország soknemzetiségűvé vált."
        }
    ]
)
write_json(STORIES_DIR / "story.b1.mariaterezia.05.json", story_5)

voc_5 = {
    "id": "voc.b1.mariaterezia.05",
    "title": "A demográfia és betelepítések szókincse",
    "description": "Betelepítés, svábok, soknemzetiségű állam, számarány és népességgyarapodás.",
    "entries": [
        {"lemma": "betelepítés", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "organized colonization / resettlement", "examples": [{"hu": "A kormányzat német telepesek betelepítését támogatta.", "en": "The government supported the resettlement of German colonists."}]}]},
        {"lemma": "dunai svábok", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "Danube Swabian German settlers in Hungary", "examples": [{"hu": "A dunai svábok virágzó falvakat hoztak létre a Bánságban.", "en": "The Danube Swabians established thriving villages in the Banat."}]}]},
        {"lemma": "soknemzetiségű", "pos": "adjective", "cefr": "B1", "definitions": [{"meaning": "multiethnic, composed of many nationalities", "examples": [{"hu": "Magyarország a 18. században soknemzetiségű országgá vált.", "en": "Hungary became a multiethnic country in the 18th century."}]}]},
        {"lemma": "számarány", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "demographic proportion, percentage ratio", "examples": [{"hu": "A magyarság számaránya lecsökkent a betelepülések miatt.", "en": "The demographic proportion of Hungarians decreased due to immigration."}]}]},
        {"lemma": "megháromszorozódik", "pos": "verb", "cefr": "B1", "definitions": [{"meaning": "to triple in size or number", "examples": [{"hu": "A lakosság száma megháromszorozódott a békés évtizedekben.", "en": "The population tripled in the peaceful decades."}]}]}
    ]
}
write_json(VOCAB_DIR / "voc.b1.mariaterezia.05.json", voc_5)

gr_5 = {
    "id": "gr.b1.mariaterezia.05",
    "title": "Népességi és aránymeghatározó kifejezések (arányában, következtében, betelepül)",
    "description": "Describing demographic trends, migration flows, and ethnic ratios.",
    "rules": [
        "A demográfiai változások kifejezésére a mértéket és arányt jelölő igék ('megduplázódik', 'megháromszorozódik', 'csökken') és névutók ('arányában', 'folyamán') szolgálnak.",
        "A folyamatokat a 'következtében' és 'eredményeképpen' okhatározói viszonyok fogják össze."
    ],
    "tables": [
        {"headers": ["Kifejezés", "Demográfiai jelentés", "Példa"], "rows": [
            ["számarányában", "arány szerinti változás", "Számarányában csökkent a népesség."],
            ["megháromszorozódik", "háromszoros növekedés", "A lakosság megháromszorozódott."],
            ["betelepül", "bevándorlás és letelepedés", "Német telepesek települtek be."]
        ]}
    ],
    "examples": [
        {"spanish": "A betelepítések következtében a 18. század végére Magyarország soknemzetiségű lett.", "english": "As a consequence of resettlements, Hungary became multiethnic by the end of the 18th century."},
        {"spanish": "A békés évtizedek alatt a lakosság száma megháromszorozódott.", "english": "During the peaceful decades, the population tripled."},
        {"spanish": "Számos nemzetiség élt békében egymás mellett a Kárpát-medencében.", "english": "Numerous nationalities lived peacefully alongside each other in the Carpathian Basin."}
    ]
}
write_json(GRAMMAR_DIR / "gr.b1.mariaterezia.05.json", gr_5)

exs_5 = [
    {"id": "ex.b1.mariaterezia.05.01", "type": "multiple-choice", "lesson": "lesson.b1.mariaterezia.05", "teaches": ["soknemzetisegu-allam"], "prompt": "Milyen etnikai jellegűvé vált Magyarország a 18. századi betelepítések után?", "options": ["Soknemzetiségű állammá (magyarok, németek, szlovákok, románok, szerbek stb.)", "Egynemzetiségű állammá", "Csak német nyelvű országgá", "Kizárólag szláv állammá"], "correctIndex": 0, "explanation": "A szervezett és spontán betelepülések nyomán soknemzetiségűvé vált az ország."},
    {"id": "ex.b1.mariaterezia.05.02", "type": "fill-blank", "lesson": "lesson.b1.mariaterezia.05", "teaches": ["betelepites"], "prompt": "Egészítsd ki a mondatot!", "sentence": "Az elnéptelenedett vidékekre szervezett *betelepítésekkel* hoztak lakosokat.", "target": "betelepítésekkel"},
    {"id": "ex.b1.mariaterezia.05.03", "type": "sentence-builder", "lesson": "lesson.b1.mariaterezia.05", "teaches": ["kovetkezteben", "soknemzetisegu"], "prompt": "Rakd össze a demográfiai összefüggést kifejező mondatot!", "chips": ["A", "betelepítések", "következtében", "az", "ország", "soknemzetiségűvé", "vált."], "target": "A betelepítések következtében az ország soknemzetiségűvé vált.", "english": "As a result of the resettlements, the country became multiethnic."},
    {"id": "ex.b1.mariaterezia.05.04", "type": "multiple-choice", "lesson": "lesson.b1.mariaterezia.05", "teaches": ["dunai-svabok"], "prompt": "Hogyan nevezték a 18. században betelepített német lakosságot?", "options": ["Dunai sváboknak", "Szászoknak", "Cipszereknek", "Hajdúknak"], "correctIndex": 0, "explanation": "A 18. században érkező német telepeseket összefoglalóan dunai sváboknak hívják."},
    {"id": "ex.b1.mariaterezia.05.05", "type": "fill-blank", "lesson": "lesson.b1.mariaterezia.05", "teaches": ["szamarany"], "prompt": "Egészítsd ki a mondatot a megfelelő szóval!", "sentence": "A magyarság *számaránya* a lakosság felére esett vissza a 18. század végére.", "target": "számaránya"},
    {"id": "ex.b1.mariaterezia.05.06", "type": "sentence-builder", "lesson": "lesson.b1.mariaterezia.05", "teaches": ["megharomszorozodik", "lakossag"], "prompt": "Alkoss szabályos mondatot a megadott szavakból!", "chips": ["A", "békés", "évtizedekben", "a", "lakosság", "száma", "megháromszorozódott."], "target": "A békés évtizedekben a lakosság száma megháromszorozódott.", "english": "In the peaceful decades, the number of the population tripled."},
    {"id": "ex.b1.mariaterezia.05.07", "type": "multiple-choice", "lesson": "lesson.b1.mariaterezia.05", "teaches": ["nepessegpótlás"], "prompt": "Milyen területekre érkezett a legtöbb telepes a 18. században?", "options": ["A déli végekre: a Bácskába, Bánátba és a Dunántúlra", "Csak a Felvidék bányavárosaiba", "Kizárólag Budára", "Csak a Magas-Tátrába"], "correctIndex": 0, "explanation": "A leginkább elnéptelenedett déli területek (Bácska, Bánát, Temesköz) fogadták a legtöbb új lakost."},
    {"id": "ex.b1.mariaterezia.05.08", "type": "fill-blank", "lesson": "lesson.b1.mariaterezia.05", "teaches": ["soknemzetisegu"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A Kárpát-medence jellegzetesen *soknemzetiségű* térséggé formálódott.", "target": "soknemzetiségű"}
]
write_json(EXERCISES_DIR / "ex.b1.mariaterezia.05.json", make_exercise_group("ex.b1.mariaterezia.05", "A 18. századi újjáépítés gyakorlatai", "Gyakorlatok a betelepítésekről, a demográfiai fejlődésről és az aránymeghatározó kifejezésekről.", exs_5))

lesson_5 = make_lesson(
    "lesson.b1.mariaterezia.05",
    "A 18. századi újjáépítés és a betelepítések következményei",
    "Népességi és aránymeghatározó kifejezések (arányában, következtében)",
    "Összegezzük a török kor utáni demográfiai robbanást, a svábok és más nemzetiségek betelepülését és a soknemzetiségű Magyarország kialakulását.",
    ["Megérteni a 18. századi népességmozgások és betelepítések hatását", "Használni a demográfiai és aránymeghatározó kifejezéseket", "Ismerni a dunai svábok és a soknemzetiségű együttélés hátterét"],
    "story.b1.mariaterezia.05",
    "voc.b1.mariaterezia.05",
    "gr.b1.mariaterezia.05",
    "ex.b1.mariaterezia.05",
    [e["id"] for e in exs_5]
)
write_json(LESSONS_DIR / "lesson.b1.mariaterezia.05.json", lesson_5)


# ==========================================
# CONSOLIDATION LESSON: b1-mariaterezia-consolidation
# ==========================================
cons_exs = [
    {"id": "ex.b1.mariaterezia.cons.01", "type": "multiple-choice", "lesson": "lesson.b1.mariaterezia.consolidation", "teaches": ["Pragmatica-Sanctio-1723"], "prompt": "Melyik évben fogadták el a Pragmatica Sanctiót?", "options": ["1723-ban", "1741-ben", "1767-ben", "1777-ben"], "correctIndex": 0, "explanation": "A Pragmatica Sanctio éve 1723."},
    {"id": "ex.b1.mariaterezia.cons.02", "type": "fill-blank", "lesson": "lesson.b1.mariaterezia.consolidation", "teaches": ["noagi-orokosodes"], "prompt": "A Pragmatica Sanctio biztosította a Habsburgok *nőági örökösödését*.", "sentence": "A Pragmatica Sanctio biztosította a Habsburgok *nőági örökösödését*.", "target": "nőági örökösödését"},
    {"id": "ex.b1.mariaterezia.cons.03", "type": "multiple-choice", "lesson": "lesson.b1.mariaterezia.consolidation", "teaches": ["Vitam-et-sanguinem"], "prompt": "Melyik évben hangzott el a pozsonyi országgyűlésen a 'Vitam et sanguinem!' felkiáltás?", "options": ["1741-ben", "1723-ban", "1780-ban", "1707-ben"], "correctIndex": 0, "explanation": "1741-ben ajánlották fel a nemesek életüket és vérüket Mária Teréziáért."},
    {"id": "ex.b1.mariaterezia.cons.04", "type": "fill-blank", "lesson": "lesson.b1.mariaterezia.consolidation", "teaches": ["felajanl"], "prompt": "A magyar rendek fegyveres támogatást *ajánlottak fel* a szorult helyzetben lévő királynőnek.", "sentence": "A magyar rendek fegyveres támogatást *ajánlottak fel* a szorult helyzetben lévő királynőnek.", "target": "ajánlottak fel"},
    {"id": "ex.b1.mariaterezia.cons.05", "type": "sentence-builder", "lesson": "lesson.b1.mariaterezia.consolidation", "teaches": ["feloszthatatlan", "kapcsolat"], "prompt": "Rakd össze a mondatot!", "chips": ["A", "birodalom", "és", "Magyarország", "feloszthatatlanul", "kapcsolódott", "össze."], "target": "A birodalom és Magyarország feloszthatatlanul kapcsolódott össze.", "english": "The empire and Hungary were indivisibly linked together."},
    {"id": "ex.b1.mariaterezia.cons.06", "type": "multiple-choice", "lesson": "lesson.b1.mariaterezia.consolidation", "teaches": ["Urbarium-1767"], "prompt": "Melyik rendelet rögzítette a jobbágyok földesúri kötelezettségeit és a robot mértékét 1767-ben?", "options": ["Az Urbárium", "A Ratio Educationis", "A türelmi rendelet", "A Pragmatica Sanctio"], "correctIndex": 0, "explanation": "Mária Terézia 1767-es rendelete az Urbárium volt."},
    {"id": "ex.b1.mariaterezia.cons.07", "type": "fill-blank", "lesson": "lesson.b1.mariaterezia.consolidation", "teaches": ["robot"], "prompt": "Az Urbárium pontosan maximálta a parasztok heti *robot* kötelezettségét.", "sentence": "Az Urbárium pontosan maximálta a parasztok heti *robot* kötelezettségét.", "target": "robot"},
    {"id": "ex.b1.mariaterezia.cons.08", "type": "sentence-builder", "lesson": "lesson.b1.mariaterezia.consolidation", "teaches": ["koteles", "iskola"], "prompt": "Rakd össze a mondatot!", "chips": ["A", "gyermekek", "hatéves", "kortól", "kötelesek", "voltak", "tanulni."], "target": "A gyermekek hatéves kortól kötelesek voltak tanulni.", "english": "Children from age six were obliged to study."},
    {"id": "ex.b1.mariaterezia.cons.09", "type": "multiple-choice", "lesson": "lesson.b1.mariaterezia.consolidation", "teaches": ["Ratio-Educationis-1777"], "prompt": "Melyik évben bocsátotta ki Mária Terézia a Ratio Educationis oktatási rendeletet?", "options": ["1777-ben", "1767-ben", "1741-ben", "1790-ben"], "correctIndex": 0, "explanation": "A Ratio Educationis 1777-ben született meg."},
    {"id": "ex.b1.mariaterezia.cons.10", "type": "fill-blank", "lesson": "lesson.b1.mariaterezia.consolidation", "teaches": ["tanterv"], "prompt": "A Ratio Educationis egységes állami *tantervet* vezetett be az iskolákban.", "sentence": "A Ratio Educationis egységes állami *tantervet* vezetett be az iskolákban.", "target": "tantervet"},
    {"id": "ex.b1.mariaterezia.cons.11", "type": "sentence-builder", "lesson": "lesson.b1.mariaterezia.consolidation", "teaches": ["szabalyoz", "alapfoku-oktatas"], "prompt": "Alkoss szabályos összetett mondatot!", "chips": ["A", "rendelet", "részletesen", "szabályozta", "az", "alapfokú", "oktatást."], "target": "A rendelet részletesen szabályozta az alapfokú oktatást.", "english": "The decree regulated primary education in detail."},
    {"id": "ex.b1.mariaterezia.cons.12", "type": "multiple-choice", "lesson": "lesson.b1.mariaterezia.consolidation", "teaches": ["kalapos-kiraly-II-Jozsef"], "prompt": "Miért nem koronáztatta meg magát II. József a magyar Szent Koronával?", "options": ["Mert nem akarta letenni a nemesi jogokat védő koronázási esküt", "Mert elveszett a korona", "Mert a pápa megtiltotta", "Mert nem volt ideje elutazni Pozsonyba"], "correctIndex": 0, "explanation": "II. József nem akart esküt tenni a rendi alkotmányra, hogy szabadon kormányozhasson."},
    {"id": "ex.b1.mariaterezia.cons.13", "type": "fill-blank", "lesson": "lesson.b1.mariaterezia.consolidation", "teaches": ["turelmi-rendelet"], "prompt": "Az 1781-es *türelmi rendelet* vallásszabadságot adott a nem katolikusoknak.", "sentence": "Az 1781-es *türelmi rendelet* vallásszabadságot adott a nem katolikusoknak.", "target": "türelmi rendelet"},
    {"id": "ex.b1.mariaterezia.cons.14", "type": "sentence-builder", "lesson": "lesson.b1.mariaterezia.consolidation", "teaches": ["kivetelevel", "visszavon"], "prompt": "Rakd össze a mondatot!", "chips": ["Két", "rendelet", "kivételével", "mindent", "visszavont", "1790-ben."], "target": "Két rendelet kivételével mindent visszavont 1790-ben.", "english": "With the exception of two decrees, he revoked everything in 1790."},
    {"id": "ex.b1.mariaterezia.cons.15", "type": "multiple-choice", "lesson": "lesson.b1.mariaterezia.consolidation", "teaches": ["jobbagyrendelet-1785"], "prompt": "Mit biztosított II. József 1785-ös jobbágyrendelete?", "options": ["A jobbágyok szabad költözködési jogát és a mesterségtanulást", "Az ingyenes nemesi címeket", "A katonai szolgálat alóli mentességet", "A templomok ingyenességét"], "correctIndex": 0, "explanation": "A jobbágyrendelet eltörölte az örökös jobbágyságot és megengedte a szabad költözést."},
    {"id": "ex.b1.mariaterezia.cons.16", "type": "fill-blank", "lesson": "lesson.b1.mariaterezia.consolidation", "teaches": ["dunai-svabok"], "prompt": "A 18. században betelepített német lakosságot *dunai sváboknak* nevezték.", "sentence": "A 18. században betelepített német lakosságot *dunai sváboknak* nevezték.", "target": "dunai sváboknak"},
    {"id": "ex.b1.mariaterezia.cons.17", "type": "sentence-builder", "lesson": "lesson.b1.mariaterezia.consolidation", "teaches": ["soknemzetisegu", "Magyarorszag"], "prompt": "Alkoss összefüggő mondatot!", "chips": ["Magyarország", "a", "betelepítések", "után", "soknemzetiségű", "állammá", "vált."], "target": "Magyarország a betelepítések után soknemzetiségű állammá vált.", "english": "Hungary became a multiethnic state after the resettlements."},
    {"id": "ex.b1.mariaterezia.cons.18", "type": "multiple-choice", "lesson": "lesson.b1.mariaterezia.consolidation", "teaches": ["Maria-Terezia-evek"], "prompt": "Hány éven át ült a trónon Mária Terézia királynő?", "options": ["40 évig (1740–1780)", "10 évig", "25 évig", "50 évig"], "correctIndex": 0, "explanation": "Mária Terézia pontosan négy évtizeden át (1740–1780) kormányozta a birodalmat."},
    {"id": "ex.b1.mariaterezia.cons.19", "type": "fill-blank", "lesson": "lesson.b1.mariaterezia.consolidation", "teaches": ["megharomszorozodik"], "prompt": "A 18. század békés éveiben az ország lakossága *megháromszorozódott*.", "sentence": "A 18. század békés éveiben az ország lakossága *megháromszorozódott*.", "target": "megháromszorozódott"},
    {"id": "ex.b1.mariaterezia.cons.20", "type": "multiple-choice", "lesson": "lesson.b1.mariaterezia.consolidation", "teaches": ["nemet-nyelvrendelet"], "prompt": "Melyik rendelet váltotta ki a legnagyobb nemzeti felháborodást II. József korában?", "options": ["Az 1784-es német nyelvrendelet", "A türelmi rendelet", "A jobbágyrendelet", "A kórházépítési rendelet"], "correctIndex": 0, "explanation": "A német nyelv hivatalossá tétele váltotta ki a legélesebb nemzeti ellenállást."}
]
write_json(EXERCISES_DIR / "ex.b1.mariaterezia.consolidation.json", make_exercise_group("ex.b1.mariaterezia.consolidation", "A 18. század és Mária Terézia kora összefoglaló gyakorlatok", "Átfogó teszt a 18. századi reformokról, a felvilágosult abszolutizmusról és a tanult nyelvtani szerkezetekről.", cons_exs))

cons_lesson = {
    "id": "lesson.b1.mariaterezia.consolidation",
    "title": "The 18th Century: Rebuilding: Unit 14 Consolidation",
    "level": "B1",
    "track": "citizenship",
    "estimatedMinutes": 25,
    "prerequisites": [
        "lesson.b1.mariaterezia.01",
        "lesson.b1.mariaterezia.02",
        "lesson.b1.mariaterezia.03",
        "lesson.b1.mariaterezia.04",
        "lesson.b1.mariaterezia.05"
    ],
    "grammar": ["Unit review"],
    "vocabulary": ["Unit review"],
    "culturalContext": "Magyar történelem összefoglalás (Honosítási vizsgafelkészítő)",
    "sections": [
        {
            "type": "intro",
            "title": "Unit 14 Consolidation: The 18th Century: Rebuilding & Maria Theresa (1711–1790)",
            "body": "Ebben az összefoglaló leckében áttekintjük a Pragmatica Sanctiót (1723), Mária Terézia trónra lépését és a pozsonyi országgyűlést (1741, 'Vitam et sanguinem!'), a felvilágosult reformokat (Urbárium 1767, Ratio Educationis 1777), II. József uralkodását és rendeleteit, valamint a 18. századi újjáépítést és a soknemzetiségűvé válást."
        },
        {
            "type": "goal",
            "title": "Consolidation Goals",
            "items": [
                "A 18. századi kulcsfontosságú törvények és rendeletek (1723, 1741, 1767, 1777, 1781, 1785) pontos ismerete",
                "Jogi feltételes (amennyiben), kötelezettséget kifejező (köteles) és demográfiai szerkezetek biztos alkalmazása",
                "Mária Terézia és II. József politikájának és a nemesi alkotmány védelmének megértése"
            ]
        },
        {
            "type": "exercise-group",
            "title": "Comprehensive Unit 14 Practice",
            "ref": "ex.b1.mariaterezia.consolidation",
            "exerciseRefs": [e["id"] for e in cons_exs]
        },
        {
            "type": "checklist",
            "items": [
                "Tudom, mit jelent a Pragmatica Sanctio és a nőági örökösödés (1723)",
                "Ismerem a 'Vitam et sanguinem!' felkiáltást és az 1741-es pozsonyi országgyűlést",
                "Megértem az Urbárium (1767) és a Ratio Educationis (1777) jelentőségét",
                "Tudom, ki volt a 'kalapos király' és hogyan lett soknemzetiségűvé Magyarország"
            ]
        }
    ]
}
write_json(LESSONS_DIR / "lesson.b1.mariaterezia.consolidation.json", cons_lesson)

print("Unit 14 (b1-mariaterezia) complete!")
