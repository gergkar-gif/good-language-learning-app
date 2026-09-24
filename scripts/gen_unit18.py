# -*- coding: utf-8 -*-
"""
Full Unit 18 Overhaul: The Compromise of 1867 (b1-kiegyezes)
Lessons:
1. Az önkényuralom kora és a passzív ellenállás (Deák Ferenc Kehidán)
2. Deák Ferenc, 'a haza bölcse' és a Húsvéti cikk (1865)
3. Az 1867-es kiegyezés és Ferenc József megkoronázása (Andrássy Gyula, Sisi)
4. A dualista államszervezet és a közös ügyek rendszere
5. Eötvös József reformjai: az 1868-as népiskolai és nemzetiségi törvény
Consolidation: Unit 18 Capstone (20 exercises)
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
# LESSON 1: b1-kiegyezes-01 (Passzív ellenállás)
# ==========================================
story_1 = make_story(
    "story.b1.kiegyezes.01",
    "Az önkényuralom kora és a passzív ellenállás (Deák Ferenc Kehidán)",
    "Az 1850-es évek osztrák abszolutizmusa alatt a magyar nemzet Deák Ferenc vezetésével békés, de szilárd passzív ellenállással védte meg az 1848-as alkotmányosság jogfolytonosságát.",
    "Kehida és Pest",
    ["Passive resistance and non-cooperation structures (megtagad, nem vállal hivatalt, kitart)", "Civil resistance to absolutism"],
    ["passzív ellenállás", "Deák Ferenc", "Bach-korszak", "jogfolytonosság", "Kehida"],
    [
        "A szabadságharc leverését követően a bécsi kormányzat megszüntette Magyarország ezeréves önállóságát: feloszlatta a vármegyéket, eltörölte az alkotmányt, és az országot idegen osztrák bürokratákkal ('Bach-huszárokkal') kormányozta. A fegyveres harc lehetetlenné vált, de a nemzet nem hódolt be.",
        "A békés nemzeti dac vezéralakja Deák Ferenc, az egykori igazságügy-miniszter lett, aki zalai birtokára, Kehidára vonult vissza. Deák a jogfolytonosság elvét vallotta: a magyarok nem ismerik el a törvénytelen abszolutizmust, nem vállalnak hivatalt a császári közigazgatásban, nem fizetnek önként adót, és nem vesznek részt a bécsi birodalmi gyűlésen.",
        "A magyar társadalom egységesen követte Deák példáját: a passzív ellenállás megbénította a Bach-rendszer működését. A nemzet békésen, de rendíthetetlenül kivárta azt a pillanatot, amikor Ausztria kénytelen lesz tárgyalóasztalhoz ülni."
    ],
    [
        {"lemma": "passzív ellenállás", "pos": "noun", "cefr": "B1", "gloss": "passive resistance, civil non-cooperation"},
        {"lemma": "jogfolytonosság", "pos": "noun", "cefr": "B1", "gloss": "legal / constitutional continuity"},
        {"lemma": "megtagad", "pos": "verb", "cefr": "B1", "gloss": "to refuse, deny (tax, cooperation)"},
        {"lemma": "behódol", "pos": "verb", "cefr": "B1", "gloss": "to submit, surrender obedience"},
        {"lemma": "megbénít", "pos": "verb", "cefr": "B1", "gloss": "to paralyze, cripple"}
    ],
    [
        {
            "question": "Mit jelentett a passzív ellenállás az 1850-es évek Bach-korszakában?",
            "options": ["A hivatali tisztségek elutasítását, az adófizetés megtagadását és a törvénytelen rendelkezések békés bojkottját", "Fegyveres partizánharcot az erdőkben", "Azonnali kivándorlást Amerikába", "A bécsi udvar feltétlen támogatását"],
            "correctIndex": 0,
            "explanation": "A passzív ellenállás a törvénytelen osztrák uralommal való békés együttműködés teljes megtagadása volt."
        }
    ]
)
write_json(STORIES_DIR / "story.b1.kiegyezes.01.json", story_1)

voc_1 = {
    "id": "voc.b1.kiegyezes.01",
    "title": "A passzív ellenállás és jogfolytonosság szókincse",
    "description": "Passzív ellenállás, jogfolytonosság, megtagadás, behódolás és megbénítás.",
    "entries": [
        {"lemma": "passzív ellenállás", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "peaceful civil non-cooperation against tyranny", "examples": [{"hu": "Deák Ferenc a passzív ellenállást választotta.", "en": "Ferenc Deák chose passive resistance."}]}]},
        {"lemma": "jogfolytonosság", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "constitutional and legal continuity of 1848 laws", "examples": [{"hu": "A nemzet ragaszkodott a jogfolytonosság elvéhez.", "en": "The nation insisted on the principle of legal continuity."}]}]},
        {"lemma": "megtagad", "pos": "verb", "cefr": "B1", "definitions": [{"meaning": "to refuse compliance or tax payment", "examples": [{"hu": "A lakosok megtagadták az önkéntes adófizetést.", "en": "The residents refused voluntary tax payment."}]}]},
        {"lemma": "behódol", "pos": "verb", "cefr": "B1", "definitions": [{"meaning": "to submit to foreign rule", "examples": [{"hu": "A magyar nemesség sosem hódolt be az abszolutizmusnak.", "en": "The Hungarian nobility never submitted to absolutism."}]}]},
        {"lemma": "megbénít", "pos": "verb", "cefr": "B1", "definitions": [{"meaning": "to paralyze an administrative apparatus", "examples": [{"hu": "A bojkott megbénította az osztrák bürokráciát.", "en": "The boycott paralyzed the Austrian bureaucracy."}]}]}
    ]
}
write_json(VOCAB_DIR / "voc.b1.kiegyezes.01.json", voc_1)

gr_1 = {
    "id": "gr.b1.kiegyezes.01",
    "title": "Elutasítást és megtagadást kifejező szerkezetek (megtagad, elutasít, nem hajlandó)",
    "description": "Expressing civil non-cooperation, refusal of illegitimate orders, and constitutional stance.",
    "rules": [
        "A tiltakozás és együttműködés hiányát a 'nem hajlandó + főnévi igenév', 'megtagadja a...', 'elutasítja a...' igék fejezik ki.",
        "A kitartást a 'ragaszkodik a jogaihoz', 'kitart az elvei mellett' határozós vonzatok jelenítik meg."
    ],
    "tables": [
        {"headers": ["Kifejezés", "Funkció", "Példa"], "rows": [
            ["megtagadja az adófizetést", "engedetlenség", "Megtagadták az adófizetést."],
            ["nem hajlandó tenni", "elutasítás", "Nem volt hajlandó hivatalt vállalni."],
            ["ragaszkodik a jogokhoz", "kitartás", "Ragaszkodtak az 1848-as törvényekhez."]
        ]}
    ],
    "examples": [
        {"spanish": "A magyar nemesség nem volt hajlandó együttműködni a Bach-rendszerrel.", "english": "The Hungarian nobility was not willing to cooperate with the Bach system."},
        {"spanish": "Deák Ferenc megtagadta a részvételt a törvénytelen birodalmi tanácsban.", "english": "Ferenc Deák refused participation in the illegitimate imperial council."},
        {"spanish": "A nemzet békés daccal ragaszkodott ősi alkotmányos önállóságához.", "english": "The nation insisted on its ancient constitutional independence with peaceful defiance."}
    ]
}
write_json(GRAMMAR_DIR / "gr.b1.kiegyezes.01.json", gr_1)

exs_1 = [
    {"id": "ex.b1.kiegyezes.01.01", "type": "multiple-choice", "lesson": "lesson.b1.kiegyezes.01", "teaches": ["passziv-ellenallas"], "prompt": "Ki volt a magyar passzív ellenállás vezéralakja az 1850-es években?", "options": ["Deák Ferenc", "Kossuth Lajos", "Andrássy Gyula", "Széchenyi István"], "correctIndex": 0, "explanation": "Deák Ferenc irányította a passzív ellenállást zalai birtokáról."},
    {"id": "ex.b1.kiegyezes.01.02", "type": "fill-blank", "lesson": "lesson.b1.kiegyezes.01", "teaches": ["passziv-ellenallas"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A magyar társadalom a *passzív ellenállás* eszközével védte meg jogait.", "target": "passzív ellenállás"},
    {"id": "ex.b1.kiegyezes.01.03", "type": "sentence-builder", "lesson": "lesson.b1.kiegyezes.01", "teaches": ["megtagad", "adofizetes"], "prompt": "Rakd össze az elutasítást kifejező mondatot!", "chips": ["A", "magyarok", "megtagadták", "az", "önkényes", "adók", "fizetését."], "target": "A magyarok megtagadták az önkényes adók fizetését.", "english": "The Hungarians refused the payment of arbitrary taxes."},
    {"id": "ex.b1.kiegyezes.01.04", "type": "multiple-choice", "lesson": "lesson.b1.kiegyezes.01", "teaches": ["jogfolytonossag"], "prompt": "Mit jelent a 'jogfolytonosság' elve Deák politikájában?", "options": ["Az 1848-as áprilisi törvények érvényességéhez való szigorú ragaszkodást", "Új király választását", "A török törvények elfogadását", "A feudalizmushoz való visszatérést"], "correctIndex": 0, "explanation": "A jogfolytonosság azt jelentette, hogy az 1848-as törvények érvényesek maradtak, mert a nemzet nem törölte el őket."},
    {"id": "ex.b1.kiegyezes.01.05", "type": "fill-blank", "lesson": "lesson.b1.kiegyezes.01", "teaches": ["behodol"], "prompt": "Egészítsd ki a mondatot a megfelelő igealakkal!", "sentence": "A nemzet a legnehezebb időkben sem *hódolt be* az elnyomóknak.", "target": "hódolt be"},
    {"id": "ex.b1.kiegyezes.01.06", "type": "sentence-builder", "lesson": "lesson.b1.kiegyezes.01", "teaches": ["nem-hajlando", "hivatal"], "prompt": "Alkoss szabályos mondatot!", "chips": ["A", "nemesek", "nem", "voltak", "hajlandók", "hivatalt", "vállalni."], "target": "A nemesek nem voltak hajlandók hivatalt vállalni.", "english": "The nobles were not willing to take office."},
    {"id": "ex.b1.kiegyezes.01.07", "type": "multiple-choice", "lesson": "lesson.b1.kiegyezes.01", "teaches": ["Bach-huszarok"], "prompt": "Kiket gúnyolt a népnyelv 'Bach-huszároknak' az abszolutizmus idején?", "options": ["A Magyarországra vezényelt idegen osztrák hivatalnokokat", "A magyar honvédeket", "A pesti színészeket", "A vasutasokat"], "correctIndex": 0, "explanation": "A Bach-huszárok a díszmagyart hordó osztrák bürokraták voltak."},
    {"id": "ex.b1.kiegyezes.01.08", "type": "fill-blank", "lesson": "lesson.b1.kiegyezes.01", "teaches": ["megbenit"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A nemzeti összefogás teljesen *megbénította* az önkényuralmi rendszert.", "target": "megbénította"}
]
write_json(EXERCISES_DIR / "ex.b1.kiegyezes.01.json", make_exercise_group("ex.b1.kiegyezes.01", "A passzív ellenállás gyakorlatai", "Gyakorlatok Deák Ferencről, a Bach-korszakról és az elutasító kifejezésekről.", exs_1))

lesson_1 = make_lesson(
    "lesson.b1.kiegyezes.01",
    "Az önkényuralom kora és a passzív ellenállás (Deák Ferenc Kehidán)",
    "Elutasítást és megtagadást kifejező szerkezetek (megtagad, nem hajlandó)",
    "Megismerjük az 1850-es évek Bach-korszakát, Deák Ferenc kehidai passzív ellenállását és a jogfolytonosság elvét.",
    ["Megérteni a passzív ellenállás módszereit és történelmi sikerét", "Használni a politikai elutasítást és nonkonformizmust kifejező nyelvi formákat", "Ismerni Deák Ferenc és a 'Bach-huszárok' korszakát"],
    "story.b1.kiegyezes.01",
    "voc.b1.kiegyezes.01",
    "gr.b1.kiegyezes.01",
    "ex.b1.kiegyezes.01",
    [e["id"] for e in exs_1]
)
write_json(LESSONS_DIR / "lesson.b1.kiegyezes.01.json", lesson_1)


# ==========================================
# LESSON 2: b1-kiegyezes-02 (A Húsvéti cikk 1865)
# ==========================================
story_2 = make_story(
    "story.b1.kiegyezes.02",
    "Deák Ferenc, 'a haza bölcse' és a Húsvéti cikk (1865)",
    "1865 húsvétján Deák Ferenc a Pesti Naplóban megjelentette korszakos cikkét, amelyben a Pragmatica Sanctio alapján kompromisszumot ajánlott Ferenc Józsefnek.",
    "Pest (Angol Királynő Szálló)",
    ["Constitutional conciliation and basis clauses (alapul vesz, megegyezésre törekszik, összhangba hoz)", "Peaceful constitutional negotiation"],
    ["Deák Ferenc", "a haza bölcse", "Húsvéti cikk", "1865", "Pragmatica Sanctio"],
    [
        "Az 1860-as évekre az Osztrák Császárság súlyos nemzetközi vereségeket szenvedett Itáliában, és a birodalom pénzügyileg az államcsőd szélére sodródott. Ferenc József belátta, hogy a birodalom fenntartása lehetetlen a magyarsággal való megbékélés nélkül.",
        "A helyzetet felismerve Deák Ferenc – akit a nemzet 'a haza bölcseként' tisztelt – 1865. április 16-án a Pesti Napló hasábjain megjelentette híres 'Húsvéti cikkét'. Ebben kinyújtotta a békejobbot az uralkodónak, kimondva: a magyarok készek megegyezni a birodalommal a közös védelem kérdésében.",
        "Deák abból indult ki, hogy az 1723-as Pragmatica Sanctio biztosítja az együttműködés alapját: összhangba kell hozni a Monarchia biztonságát és a magyar nemzet alkotmányos önállóságát. A Húsvéti cikk megnyitotta az utat a közvetlen tárgyalásokhoz és az 1867-es történelmi kiegyezéshez."
    ],
    [
        {"lemma": "a haza bölcse", "pos": "noun", "cefr": "B1", "gloss": "the 'Sage of the Homeland' (Ferenc Deák)"},
        {"lemma": "Húsvéti cikk", "pos": "noun", "cefr": "B1", "gloss": "Easter Article of 1865"},
        {"lemma": "megbékélés", "pos": "noun", "cefr": "B1", "gloss": "reconciliation"},
        {"lemma": "békejobb", "pos": "noun", "cefr": "B1", "gloss": "hand of peace / olive branch"},
        {"lemma": "összhangba hoz", "pos": "verb", "cefr": "B1", "gloss": "to bring into harmony / align"}
    ],
    [
        {
            "question": "Mit ajánlott fel Deák Ferenc az 1865-ös híres Húsvéti cikkben?",
            "options": ["A megegyezést a Habsburgokkal a Pragmatica Sanctio és a közös védelem alapján", "Azonnali fegyveres támadást Bécs ellen", "Minden magyar törvény eltörlését", "Külföldi hadsereg behívását"],
            "correctIndex": 0,
            "explanation": "Deák a Pragmatica Sanctio alapján állva a birodalmi biztonság és a magyar önállóság összehangolását ajánlotta."
        }
    ]
)
write_json(STORIES_DIR / "story.b1.kiegyezes.02.json", story_2)

voc_2 = {
    "id": "voc.b1.kiegyezes.02",
    "title": "A Húsvéti cikk és a megbékélés szókincse",
    "description": "A haza bölcse, Húsvéti cikk, megbékélés, békejobb és érdekek összehangolása.",
    "entries": [
        {"lemma": "a haza bölcse", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "honorific title of Ferenc Deák", "examples": [{"hu": "Deák Ferencet méltán nevezték a haza bölcsének.", "en": "Ferenc Deák was deservedly named the Sage of the Homeland."}]}]},
        {"lemma": "Húsvéti cikk", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "historic 1865 article proposing terms for Compromise", "examples": [{"hu": "A Húsvéti cikk elindította a kiegyezési tárgyalásokat.", "en": "The Easter Article launched the Compromise negotiations."}]}]},
        {"lemma": "megbékélés", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "political and national reconciliation", "examples": [{"hu": "A megbékélés mindkét fél érdeke volt.", "en": "Reconciliation was in the interest of both parties."}]}]},
        {"lemma": "békejobb", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "hand of peace, olive branch", "examples": [{"hu": "Deák békejobbot nyújtott az uralkodónak.", "en": "Deák extended the hand of peace to the monarch."}]}]},
        {"lemma": "összhangba hoz", "pos": "verb", "cefr": "B1", "definitions": [{"meaning": "to reconcile, harmonize competing interests", "examples": [{"hu": "Összhangba hozták a birodalom és Magyarország érdekeit.", "en": "They brought the interests of the empire and Hungary into harmony."}]}]}
    ]
}
write_json(VOCAB_DIR / "voc.b1.kiegyezes.02.json", voc_2)

gr_2 = {
    "id": "gr.b1.kiegyezes.02",
    "title": "Kompromisszumot és összehangolást kifejező szerkezetek (összhangba hoz, alapul vesz, törekszik)",
    "description": "Expressing diplomatic alignment, mutual concession, and constitutional reconciliation.",
    "rules": [
        "A diplomáciai megállapodások leírásakor az 'összhangba hoz valamit valamivel', 'alapul vesz valamit' kifejezéseket használjuk.",
        "A tárgyalási szándékot a 'megegyezésre törekszik', 'kompromisszumot keres' igék jelenítik meg."
    ],
    "tables": [
        {"headers": ["Kifejezés", "Funkció", "Példa"], "rows": [
            ["összhangba hoz", "érdekek egyeztetése", "Összhangba hozták a jogokat a biztonsággal."],
            ["alapul vesz", "hivatkozási pont", "A Pragmatica Sanctiót vették alapul."],
            ["törekszik a megegyezésre", "szándék", "A nemzet megegyezésre törekedett."]
        ]}
    ],
    "examples": [
        {"spanish": "Deák Ferenc a Pragmatica Sanctiót vette alapul a kiegyezési javaslatában.", "english": "Ferenc Deák took the Pragmatic Sanction as the basis in his Compromise proposal."},
        {"spanish": "A cikk célja az volt, hogy összhangba hozza az alkotmányos önállóságot a birodalmi érdekekkel.", "english": "The article's aim was to harmonize constitutional autonomy with imperial interests."},
        {"spanish": "A haza bölcse békés tárgyalások útján érte el a magyar alkotmányosság visszaállítását.", "english": "The Sage of the Homeland achieved the restoration of Hungarian constitutionality through peaceful negotiations."}
    ]
}
write_json(GRAMMAR_DIR / "gr.b1.kiegyezes.02.json", gr_2)

exs_2 = [
    {"id": "ex.b1.kiegyezes.02.01", "type": "multiple-choice", "lesson": "lesson.b1.kiegyezes.02", "teaches": ["Husveti-cikk-1865"], "prompt": "Melyik évben jelent meg Deák Ferenc Húsvéti cikke a Pesti Naplóban?", "options": ["1865-ben", "1848-ban", "1867-ben", "1860-ban"], "correctIndex": 0, "explanation": "A Húsvéti cikk 1865. április 16-án látott napvilágot."},
    {"id": "ex.b1.kiegyezes.02.02", "type": "fill-blank", "lesson": "lesson.b1.kiegyezes.02", "teaches": ["a-haza-bolcse"], "prompt": "Egészítsd ki a mondatot!", "sentence": "Deák Ferencet a nemzet hálából *a haza bölcsének* nevezte.", "target": "a haza bölcsének"},
    {"id": "ex.b1.kiegyezes.02.03", "type": "sentence-builder", "lesson": "lesson.b1.kiegyezes.02", "teaches": ["osszhangba-hoz", "erdekek"], "prompt": "Rakd össze az összehangolást kifejező mondatot!", "chips": ["Összhangba", "kellett", "hozni", "a", "két", "ország", "érdekeit."], "target": "Összhangba kellett hozni a két ország érdekeit.", "english": "The interests of the two countries had to be brought into harmony."},
    {"id": "ex.b1.kiegyezes.02.04", "type": "multiple-choice", "lesson": "lesson.b1.kiegyezes.02", "teaches": ["Pragmatica-Sanctio-alap"], "prompt": "Melyik történelmi alaptörvényre hivatkozott Deák a megegyezés alapjaként?", "options": ["Az 1723-as Pragmatica Sanctióra", "Az Aranybullára", "A Vérszerződésre", "A Tripartitumra"], "correctIndex": 0, "explanation": "Deák a Pragmatica Sanctio közös védelmi elvét fogadta el a tárgyalások alapjául."},
    {"id": "ex.b1.kiegyezes.02.05", "type": "fill-blank", "lesson": "lesson.b1.kiegyezes.02", "teaches": ["bekejobb"], "prompt": "Egészítsd ki a mondatot a megfelelő szóval!", "sentence": "Deák Ferenc *békejobbot* nyújtott a bécsi udvarnak a Húsvéti cikkben.", "target": "békejobbot"},
    {"id": "ex.b1.kiegyezes.02.06", "type": "sentence-builder", "lesson": "lesson.b1.kiegyezes.02", "teaches": ["megbekeles", "fontos"], "prompt": "Alkoss szabályos mondatot!", "chips": ["A", "kölcsönös", "megbékélés", "megmentette", "az", "ország", "jövőjét."], "target": "A kölcsönös megbékélés megmentette az ország jövőjét.", "english": "Mutual reconciliation saved the country's future."},
    {"id": "ex.b1.kiegyezes.02.07", "type": "multiple-choice", "lesson": "lesson.b1.kiegyezes.02", "teaches": ["Angol-Kiralyno"], "prompt": "Melyik pesti szállodában élt Deák Ferenc a kiegyezés előkészítésekor?", "options": ["Az Angol Királynő Szállóban", "A Gellért Szállóban", "A Duna Palotában", "A Hungária Szállóban"], "correctIndex": 0, "explanation": "Deák szerény lakosztálya az Angol Királynő Szállóban volt a politikai élet központja."},
    {"id": "ex.b1.kiegyezes.02.08", "type": "fill-blank", "lesson": "lesson.b1.kiegyezes.02", "teaches": ["alapul-vesz"], "prompt": "Egészítsd ki a mondatot a megfelelő igealakkal!", "sentence": "A tárgyalások során a jogfolytonosságot *vették alapul*.", "target": "vették alapul"}
]
write_json(EXERCISES_DIR / "ex.b1.kiegyezes.02.json", make_exercise_group("ex.b1.kiegyezes.02", "A Húsvéti cikk gyakorlatai", "Gyakorlatok Deák Ferencről, az 1865-ös Húsvéti cikkről és a kompromisszumos kifejezésekről.", exs_2))

lesson_2 = make_lesson(
    "lesson.b1.kiegyezes.02",
    "Deák Ferenc, 'a haza bölcse' és a Húsvéti cikk (1865)",
    "Kompromisszumot és összehangolást kifejező szerkezetek (összhangba hoz, alapul vesz)",
    "Megismerjük Deák Ferenc 'a haza bölcse' történelmi alakját, az 1865-ös Húsvéti cikket és a megegyezés feltételeit.",
    ["Megérteni a Húsvéti cikk (1865) jelentőségét a kiegyezés előkészítésében", "Használni a kompromisszumot és érdekegyeztetést leíró nyelvtani szerkezeteket", "Ismerni a Pragmatica Sanctio és az alkotmányosság összhangját"],
    "story.b1.kiegyezes.02",
    "voc.b1.kiegyezes.02",
    "gr.b1.kiegyezes.02",
    "ex.b1.kiegyezes.02",
    [e["id"] for e in exs_2]
)
write_json(LESSONS_DIR / "lesson.b1.kiegyezes.02.json", lesson_2)


# ==========================================
# LESSON 3: b1-kiegyezes-03 (A kiegyezés megkötése 1867)
# ==========================================
story_3 = make_story(
    "story.b1.kiegyezes.03",
    "Az 1867-es kiegyezés és Ferenc József megkoronázása (Andrássy Gyula, Sisi)",
    "1867-ben létrejött az Osztrák–Magyar Monarchia, felállt a gróf Andrássy Gyula vezette felelős magyar kormány, és a budai Mátyás-templomban megkoronázták Ferenc Józsefet és Erzsébet királynét.",
    "Buda, Mátyás-templom és a Várkert",
    ["Bilateral state formation and coronation terminology (megkoronáz, miniszterelnökké kinevez, szövetség)", "The 1867 Coronation in Buda"],
    ["kiegyezés", "1867", "Andrássy Gyula", "Ferenc József", "Erzsébet királyné (Sisi)"],
    [
        "1867 tavaszán a magyar országgyűlés elfogadta az 1867. évi XII. törvénycikket, a kiegyezési törvényt. Ferenc József kinevezte a független magyar miniszterelnököt, a szabadságharc után egykor távollétében halálra ítélt gróf Andrássy Gyulát, akit 'a szép akasztottnak' is neveztek.",
        "1867. június 8-án fényes ünnepség keretében a budai Mátyás-templomban Simor János hercegprímás és Andrássy miniszterelnök a Szent Koronával magyar királlyá koronázta Ferenc Józsefet, és megkoronázták a magyarokat rajongásig szerető Erzsébet királynét (Sisit) is.",
        "A koronázás után a király felesküdött a magyar alkotmányra, és általános közkegyelmet (amnesztiát) hirdetett a szabadságharc minden résztvevőjének. A kiegyezéssel fél évszázados békés, virágzó korszak köszöntött Magyarországra."
    ],
    [
        {"lemma": "kiegyezés", "pos": "noun", "cefr": "B1", "gloss": "Compromise of 1867 (Ausgleich)"},
        {"lemma": "koronázás", "pos": "noun", "cefr": "B1", "gloss": "coronation"},
        {"lemma": "hercegprímás", "pos": "noun", "cefr": "B1", "gloss": "Prince Primate (Archbishop of Esztergom)"},
        {"lemma": "közkegyelem", "pos": "noun", "cefr": "B1", "gloss": "general amnesty / royal pardon"},
        {"lemma": "felesküszik", "pos": "verb", "cefr": "B1", "gloss": "to take a solemn constitutional oath"}
    ],
    [
        {
            "question": "Kiket koronáztak meg a budai Mátyás-templomban 1867. június 8-án?",
            "options": ["Ferenc Józsefet magyar királlyá és Erzsébetet (Sisit) magyar királynévá", "Batthyány Lajost és feleségét", "Deák Ferencet és Erzsébetet", "Kossuth Lajost"],
            "correctIndex": 0,
            "explanation": "Ferenc Józsefet és Erzsébet királynét (Sisit) koronázták meg a Mátyás-templomban."
        }
    ]
)
write_json(STORIES_DIR / "story.b1.kiegyezes.03.json", story_3)

voc_3 = {
    "id": "voc.b1.kiegyezes.03",
    "title": "A kiegyezés és a koronázási ünnep szókincse",
    "description": "Kiegyezés, koronázás, hercegprímás, közkegyelem, felesküvés és Sisi emléke.",
    "entries": [
        {"lemma": "kiegyezés", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "The Austro-Hungarian Compromise of 1867", "examples": [{"hu": "Az 1867-es kiegyezés békés korszakot nyitott.", "en": "The 1867 Compromise opened a peaceful era."}]}]},
        {"lemma": "koronázás", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "solemn coronation with the Holy Crown", "examples": [{"hu": "A koronázás a budai Mátyás-templomban zajlott.", "en": "The coronation took place in Buda's Matthias Church."}]}]},
        {"lemma": "hercegprímás", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "Prince Primate, Archbishop of Esztergom", "examples": [{"hu": "A hercegprímás helyezte a koronát a király fejére.", "en": "The Prince Primate placed the crown on the king's head."}]}]},
        {"lemma": "közkegyelem", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "general royal amnesty", "examples": [{"hu": "A király közkegyelmet adott a forradalmároknak.", "en": "The king granted general amnesty to the revolutionaries."}]}]},
        {"lemma": "felesküszik", "pos": "verb", "cefr": "B1", "definitions": [{"meaning": "to swear a formal constitutional oath", "examples": [{"hu": "Ferenc József felesküdött a magyar alkotmányra.", "en": "Franz Joseph swore an oath to the Hungarian constitution."}]}]}
    ]
}
write_json(VOCAB_DIR / "voc.b1.kiegyezes.03.json", voc_3)

gr_3 = {
    "id": "gr.b1.kiegyezes.03",
    "title": "Kinevezést és állami szertartásokat kifejező szerkezetek (kinevez, megkoronáz, felesküszik)",
    "description": "Describing formal state appointments, coronations, and constitutional oaths.",
    "rules": [
        "A kinevezést és beiktatást a '-vá/-vé kinevez', '-vá/-vé koronáz' szerkezetek jelenítik meg.",
        "Az alkotmányos kötelezettségvállalást a 'felesküszik valamire' (felesküszik az alkotmányra) vonzatos ige fejezi ki."
    ],
    "tables": [
        {"headers": ["Ige / Szerkezet", "Jelentés", "Példa"], "rows": [
            ["miniszterelnökké kinevez", "kinevezés", "Andrássy Gyulát kinevezték miniszterelnökké."],
            ["királlyá koronáz", "megkoronázás", "Ferenc Józsefet megkoronázták."],
            ["felesküszik az alkotmányra", "eskütétel", "Az uralkodó felesküdött a törvényekre."]
        ]}
    ],
    "examples": [
        {"spanish": "1867-ben Ferenc József kinevezte gróf Andrássy Gyulát miniszterelnökké.", "english": "In 1867, Franz Joseph appointed Count Gyula Andrássy Prime Minister."},
        {"spanish": "A Mátyás-templomban ünnepélyesen megkoronázták Ferenc Józsefet és Erzsébet királynét.", "english": "In Matthias Church, Franz Joseph and Queen Elisabeth were solemnly crowned."},
        {"spanish": "A koronázás után a király felesküdött a magyar törvények betartására.", "english": "After the coronation, the king swore an oath to observe Hungarian laws."}
    ]
}
write_json(GRAMMAR_DIR / "gr.b1.kiegyezes.03.json", gr_3)

exs_3 = [
    {"id": "ex.b1.kiegyezes.03.01", "type": "multiple-choice", "lesson": "lesson.b1.kiegyezes.03", "teaches": ["kiegyezes-1867"], "prompt": "Melyik évben született meg a kiegyezés és jött létre az Osztrák–Magyar Monarchia?", "options": ["1867-ben", "1848-ban", "1865-ben", "1896-ban"], "correctIndex": 0, "explanation": "A kiegyezés éve 1867 volt."},
    {"id": "ex.b1.kiegyezes.03.02", "type": "fill-blank", "lesson": "lesson.b1.kiegyezes.03", "teaches": ["Andrassy-Gyula"], "prompt": "Egészítsd ki a mondatot!", "sentence": "Az 1867-es kiegyezés után gróf *Andrássy Gyula* lett a miniszterelnök.", "target": "Andrássy Gyula"},
    {"id": "ex.b1.kiegyezes.03.03", "type": "sentence-builder", "lesson": "lesson.b1.kiegyezes.03", "teaches": ["megkoronaz", "Ferenc-Jozsef"], "prompt": "Rakd össze a koronázást leíró mondatot!", "chips": ["A", "budai", "Mátyás-templomban", "királlyá", "koronázták", "Ferenc", "Józsefet."], "target": "A budai Mátyás-templomban királlyá koronázták Ferenc Józsefet.", "english": "In Matthias Church of Buda, Franz Joseph was crowned king."},
    {"id": "ex.b1.kiegyezes.03.04", "type": "multiple-choice", "lesson": "lesson.b1.kiegyezes.03", "teaches": ["Sisi-Erzsebet"], "prompt": "Ki volt a magyarok által rajongásig szeretett királyné, aki sokat segített a kiegyezésben?", "options": ["Erzsébet királyné (Sisi)", "Mária Terézia", "Zrínyi Ilona", "Kanizsai Dorottya"], "correctIndex": 0, "explanation": "Erzsébet királyné (Sisi) rendkívül népszerű volt a magyarok körében, és támogatta a kiegyezést."},
    {"id": "ex.b1.kiegyezes.03.05", "type": "fill-blank", "lesson": "lesson.b1.kiegyezes.03", "teaches": ["feleskuszik"], "prompt": "Egészítsd ki a mondatot a megfelelő igealakkal!", "sentence": "A király ünnepélyesen *felesküdött* a magyar alkotmányra.", "target": "felesküdött"},
    {"id": "ex.b1.kiegyezes.03.06", "type": "sentence-builder", "lesson": "lesson.b1.kiegyezes.03", "teaches": ["kozkegyelem", "amnesztia"], "prompt": "Alkoss szabályos állami döntést kifejező mondatot!", "chips": ["A", "koronázás", "után", "általános", "közkegyelmet", "hirdettek", "a", "honvédeknek."], "target": "A koronázás után általános közkegyelmet hirdettek a honvédeknek.", "english": "After the coronation, general amnesty was proclaimed for the soldiers."},
    {"id": "ex.b1.kiegyezes.03.07", "type": "multiple-choice", "lesson": "lesson.b1.kiegyezes.03", "teaches": ["Matyas-templom"], "prompt": "Melyik híres budai templomban zajlott az 1867-es királykoronázás?", "options": ["A Mátyás-templomban (Budavári Nagyboldogasszony-templom)", "A Szent István-bazilikában", "A Belvárosi Plébániatemplomban", "Az esztergomi bazilikában"], "correctIndex": 0, "explanation": "A budai Várban álló Mátyás-templomban koronázták meg a királyi párt."},
    {"id": "ex.b1.kiegyezes.03.08", "type": "fill-blank", "lesson": "lesson.b1.kiegyezes.03", "teaches": ["kiegyezes"], "prompt": "Egészítsd ki a mondatot!", "sentence": "Az 1867-es *kiegyezés* fél évszázados gazdasági fejlődést indított el.", "target": "kiegyezés"}
]
write_json(EXERCISES_DIR / "ex.b1.kiegyezes.03.json", make_exercise_group("ex.b1.kiegyezes.03", "Az 1867-es kiegyezés gyakorlatai", "Gyakorlatok a koronázásról, Andrássy Gyuláról, Sisiről és az állami szertartások kifejezéseiről.", exs_3))

lesson_3 = make_lesson(
    "lesson.b1.kiegyezes.03",
    "Az 1867-es kiegyezés és Ferenc József megkoronázása (Andrássy Gyula, Sisi)",
    "Kinevezést és állami szertartásokat kifejező szerkezetek (kinevez, megkoronáz)",
    "Megismerjük az 1867-es kiegyezési törvényt, Andrássy Gyula miniszterelnökségét és Ferenc József megkoronázását a Mátyás-templomban.",
    ["Megérteni az 1867-es kiegyezés körülményeit és a monarchia megalakulását", "Használni a kinevezést és alkotmányos esküt kifejező nyelvi formákat", "Ismerni gróf Andrássy Gyula és Erzsébet királyné (Sisi) szerepét"],
    "story.b1.kiegyezes.03",
    "voc.b1.kiegyezes.03",
    "gr.b1.kiegyezes.03",
    "ex.b1.kiegyezes.03",
    [e["id"] for e in exs_3]
)
write_json(LESSONS_DIR / "lesson.b1.kiegyezes.03.json", lesson_3)


# ==========================================
# LESSON 4: b1-kiegyezes-04 (A dualista államszervezet és közös ügyek)
# ==========================================
story_4 = make_story(
    "story.b1.kiegyezes.04",
    "A dualista államszervezet és a közös ügyek rendszere",
    "A dualista Osztrák–Magyar Monarchia két egyenrangú állam szövetsége volt: mindkét fél önálló parlamenttel rendelkezett, miközben a hadügy, külügy és pénzügy közös maradt.",
    "Bécs és Budapest",
    ["Institutional parity and dual governance structures (paritás, közös ügyek, delegációk útján intéz)", "Constitutional structure of Austria-Hungary"],
    ["Osztrák-Magyar Monarchia", "dualizmus", "közös ügyek", "hadügy", "külügy", "pénzügy", "delegáció"],
    [
        "Az 1867-es kiegyezéssel létrejött államalakulat a dualizmus rendszerére épült. Az Osztrák–Magyar Monarchia két egyenrangú, belső ügyeiben független államból állt: a Magyar Királyságból (központja Budapest) és az Osztrák Császárságból (központja Bécs), amelyeket a közös uralkodó személye fűzött egybe.",
        "A két állam a Pragmatica Sanctio szellemében három területet nyilvánított közös ügynek: a külügyet, a hadügyet (a császári és királyi, közös hadsereget) és az ezek fedezésére szolgáló pénzügyet. A közös minisztériumok működését a két parlamentből választott 60-60 fős delegációk ellenőrizték felváltva Bécsben és Pesten.",
        "Emellett tízévente megújított gazdasági kiegyezést kötöttek: közös maradt a vámterület, a valuta (az osztrák értékű forint, majd a korona) és a szabad piac. A dualista berendezkedés biztosította Magyarország szuverenitását, miközben megtartotta a birodalom nagyhatalmi státuszát."
    ],
    [
        {"lemma": "dualizmus", "pos": "noun", "cefr": "B1", "gloss": "Dualism (Austro-Hungarian dual monarchy system)"},
        {"lemma": "közös ügyek", "pos": "noun", "cefr": "B1", "gloss": "joint affairs (foreign, defense, finance)"},
        {"lemma": "delegáció", "pos": "noun", "cefr": "B1", "gloss": "parliamentary delegation monitoring joint affairs"},
        {"lemma": "vámunió", "pos": "noun", "cefr": "B1", "gloss": "customs union"},
        {"lemma": "egyenrangú", "pos": "adjective", "cefr": "B1", "gloss": "equal in status, parity-based"}
    ],
    [
        {
            "question": "Melyik három terület számított 'közös ügynek' az Osztrák–Magyar Monarchiában?",
            "options": ["A külügy, a hadügy és az ezekre vonatkozó pénzügy", "Az oktatás, az egészségügy és a mezőgazdaság", "A vallásügy, a rendőrség és a bányászat", "A posta, a vasút és a színházak"],
            "correctIndex": 0,
            "explanation": "A három közös ügy a külügy, a hadügy és a hadügyi pénzügy volt."
        }
    ]
)
write_json(STORIES_DIR / "story.b1.kiegyezes.04.json", story_4)

voc_4 = {
    "id": "voc.b1.kiegyezes.04",
    "title": "A dualista államszervezet és közigazgatás szókincse",
    "description": "Dualizmus, közös ügyek, delegáció, vámunió, egyenrangúság és közös minisztériumok.",
    "entries": [
        {"lemma": "dualizmus", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "system of the Austro-Hungarian Dual Monarchy (1867–1918)", "examples": [{"hu": "A dualizmus kora rendkívüli gazdasági fejlődést hozott.", "en": "The era of dualism brought extraordinary economic development."}]}]},
        {"lemma": "közös ügyek", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "joint imperial affairs: foreign policy, army and defense finance", "examples": [{"hu": "A hadügy és a külügy közös ügy maradt a birodalomban.", "en": "Defense and foreign policy remained joint affairs in the empire."}]}]},
        {"lemma": "delegáció", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "60-member parliamentary delegation overseeing joint ministries", "examples": [{"hu": "A két ország delegációi felügyelték a közös költségvetést.", "en": "The delegations of the two countries supervised the joint budget."}]}]},
        {"lemma": "vámunió", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "customs union and common market", "examples": [{"hu": "A vámunió biztosította a magyar mezőgazdasági termékek piacát.", "en": "The customs union secured a market for Hungarian agricultural products."}]}]},
        {"lemma": "egyenrangú", "pos": "adjective", "cefr": "B1", "definitions": [{"meaning": "equal in political status and rights", "examples": [{"hu": "Magyarország egyenrangú féllé vált a Monarchiában.", "en": "Hungary became an equal party in the Monarchy."}]}]}
    ]
}
write_json(VOCAB_DIR / "voc.b1.kiegyezes.04.json", voc_4)

gr_4 = {
    "id": "gr.b1.kiegyezes.04",
    "title": "Közös és önálló hatáskörök megkülönböztetése (közös ügyként kezeli, felügyel, kiterjed vmire)",
    "description": "Distinguishing shared jurisdictions from autonomous national competencies.",
    "rules": [
        "A dualista struktúrában a megosztott hatásköröket a 'közös ügyként intéz', 'önállóan dönt', 'felügyelete alá tartozik' szerkezetekkel mutatjuk be.",
        "A paritást a 'mindkét fél', 'egyenrangú partnerként' határozók fejezik ki."
    ],
    "tables": [
        {"headers": ["Kifejezés", "Funkció", "Példa"], "rows": [
            ["közös ügyként intéz", "megosztott hatáskör", "A hadügyet közös ügyként intézték."],
            ["önállóan irányít", "belső függetlenség", "A belügyet önállóan irányította a kormány."],
            ["delegációk útján felügyel", "parlamenti kontroll", "A kiadásokat delegációk útján felügyelték."]
        ]}
    ],
    "examples": [
        {"spanish": "A külügy, a hadügy és a pénzügy közös minisztériumok felügyelete alá tartozott.", "english": "Foreign affairs, defense, and finance belonged under the supervision of joint ministries."},
        {"spanish": "A Magyar Királyság minden belső kérdésben teljes önállóságot élvezett.", "english": "The Kingdom of Hungary enjoyed complete autonomy in all internal matters."},
        {"spanish": "A közös vámterület elősegítette az ipar és a kereskedelem fellendülését.", "english": "The common customs area promoted the boom of industry and trade."}
    ]
}
write_json(GRAMMAR_DIR / "gr.b1.kiegyezes.04.json", gr_4)

exs_4 = [
    {"id": "ex.b1.kiegyezes.04.01", "type": "multiple-choice", "lesson": "lesson.b1.kiegyezes.04", "teaches": ["kozos-ugyek-1867"], "prompt": "Mely három minisztérium volt közös a Monarchiában?", "options": ["Külügyminisztérium, Hadügyminisztérium és Pénzügyminisztérium", "Oktatásügyi, Igazságügyi és Földművelésügyi", "Kereskedelmi, Vasúti és Belügyminisztérium", "Nem voltak közös minisztériumok"], "correctIndex": 0, "explanation": "A külügy, hadügy és az ezekre vonatkozó pénzügy volt közös."},
    {"id": "ex.b1.kiegyezes.04.02", "type": "fill-blank", "lesson": "lesson.b1.kiegyezes.04", "teaches": ["dualizmus"], "prompt": "Egészítsd ki a mondatot!", "sentence": "Az 1867 utáni államrendszert *dualizmusnak* nevezzük.", "target": "dualizmusnak"},
    {"id": "ex.b1.kiegyezes.04.03", "type": "sentence-builder", "lesson": "lesson.b1.kiegyezes.04", "teaches": ["egyenrangu", "allam"], "prompt": "Rakd össze a dualista berendezkedést kifejező mondatot!", "chips": ["A", "Monarchia", "két", "egyenrangú", "állam", "szövetsége", "volt."], "target": "A Monarchia két egyenrangú állam szövetsége volt.", "english": "The Monarchy was an alliance of two equal states."},
    {"id": "ex.b1.kiegyezes.04.04", "type": "multiple-choice", "lesson": "lesson.b1.kiegyezes.04", "teaches": ["delegaciok"], "prompt": "Hány fős delegációk ellenőrizték a közös minisztériumok munkáját?", "options": ["60-60 fős delegációk a két parlamentből", "10-10 fős bizottságok", "100-100 képviselő", "Csak a király személyesen"], "correctIndex": 0, "explanation": "A magyar és az osztrák parlament 60-60 fős delegációi felügyelték a közös ügyeket."},
    {"id": "ex.b1.kiegyezes.04.05", "type": "fill-blank", "lesson": "lesson.b1.kiegyezes.04", "teaches": ["vamunio"], "prompt": "Egészítsd ki a mondatot a megfelelő szóval!", "sentence": "A két ország közötti *vámunió* hatalmas szabad piacot teremtett.", "target": "vámunió"},
    {"id": "ex.b1.kiegyezes.04.06", "type": "sentence-builder", "lesson": "lesson.b1.kiegyezes.04", "teaches": ["kozos-ugy", "hadugy"], "prompt": "Alkoss szabályos összetett mondatot!", "chips": ["A", "hadügyet", "és", "a", "külügyet", "közös", "ügyként", "kezelték."], "target": "A hadügyet és a külügyet közös ügyként kezelték.", "english": "Defense and foreign policy were treated as joint affairs."},
    {"id": "ex.b1.kiegyezes.04.07", "type": "multiple-choice", "lesson": "lesson.b1.kiegyezes.04", "teaches": ["fovarosok"], "prompt": "Melyik két város volt az Osztrák–Magyar Monarchia két egyenrangú fővárosa?", "options": ["Bécs és Budapest", "Bécs és Pozsony", "Prága és Zágráb", "Budapest és Kolozsvár"], "correctIndex": 0, "explanation": "A Monarchia két fővárosa Bécs és Budapest volt."},
    {"id": "ex.b1.kiegyezes.04.08", "type": "fill-blank", "lesson": "lesson.b1.kiegyezes.04", "teaches": ["kozos-ugyek"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A *közös ügyek* költségvetését tízévente tárgyalták újra a felek.", "target": "közös ügyek"}
]
write_json(EXERCISES_DIR / "ex.b1.kiegyezes.04.json", make_exercise_group("ex.b1.kiegyezes.04", "A dualista államszervezet gyakorlatai", "Gyakorlatok a közös ügyekről, delegációkról, vámunióról és az államszervezeti szerkezetekről.", exs_4))

lesson_4 = make_lesson(
    "lesson.b1.kiegyezes.04",
    "A dualista államszervezet és a közös ügyek rendszere",
    "Közös és önálló hatáskörök megkülönböztetése (közös ügyként kezeli, felügyel)",
    "Megismerjük az Osztrák–Magyar Monarchia dualista szerkezetét, a három közös ügyet (hadügy, külügy, pénzügy), a delegációkat és a vámuniót.",
    ["Megérteni a dualista állam felépítését és a közös ügyek rendszerét", "Használni a megosztott és önálló hatásköröket kifejező nyelvtani formákat", "Ismerni a paritásos elvet és a gazdasági kiegyezést"],
    "story.b1.kiegyezes.04",
    "voc.b1.kiegyezes.04",
    "gr.b1.kiegyezes.04",
    "ex.b1.kiegyezes.04",
    [e["id"] for e in exs_4]
)
write_json(LESSONS_DIR / "lesson.b1.kiegyezes.04.json", lesson_4)


# ==========================================
# LESSON 5: b1-kiegyezes-05 (Eötvös József törvényei 1868)
# ==========================================
story_5 = make_story(
    "story.b1.kiegyezes.05",
    "Eötvös József reformjai: az 1868-as népiskolai és nemzetiségi törvény",
    "Báró Eötvös József kultuszminiszterként megteremtette az ingyenes és kötelező állami alapfokú oktatást, valamint Európa korabeli legliberálisabb nemzetiségi törvényét.",
    "Pest és az elemi iskolák",
    ["Legislative tolerance and educational rights (biztosítja a jogot, kötelezővé teszi, anyanyelvű oktatás)", "Liberal reforms of 1868"],
    ["Eötvös József", "1868. évi népiskolai törvény", "nemzetiségi törvény", "elemi iskola", "anyanyelvhasználat"],
    [
        "A kiegyezés utáni kormány kultuszminisztere, a nagy formátumú író és politikus, báró Eötvös József két korszakalkotó törvénnyel alapozta meg a polgári Magyarország társadalmi békéjét és modern műveltségét 1868-ban.",
        "Az 1868. évi XXXVIII. törvénycikk (népiskolai törvény) a kontinensen az elsők között vezette be a hatosztályos kötelező és ingyenes elemi iskoláztatást (6-tól 12 éves korig). Elrendelte, hogy minden 30 gyermeknél népesebb faluban iskolát kell építeni, és biztosította a gyermekek anyanyelvi oktatásának jogát.",
        "Ugyanebben az évben fogadták el az 1868. évi XLIV. törvénycikket, a híres nemzetiségi törvényt. Bár a törvény a politikai nemzet egységét vallotta ('egy politikai nemzet, a magyar'), széles körű jogokat garantált a nemzetiségeknek: szabad anyanyelvhasználatot az alsófokú bíróságokon, a közigazgatásban, az iskolákban és az egyházi életben, a világ egyik legtürelmesebb jogszabályaként."
    ],
    [
        {"lemma": "népiskolai törvény", "pos": "noun", "cefr": "B1", "gloss": "Primary Education Act of 1868"},
        {"lemma": "nemzetiségi törvény", "pos": "noun", "cefr": "B1", "gloss": "Nationalities Act of 1868"},
        {"lemma": "elemi iskola", "pos": "noun", "cefr": "B1", "gloss": "primary elementary school"},
        {"lemma": "anyanyelvhasználat", "pos": "noun", "cefr": "B1", "gloss": "use of mother tongue"},
        {"lemma": "türelmes", "pos": "adjective", "cefr": "B1", "gloss": "tolerant, liberal"}
    ],
    [
        {
            "question": "Miről rendelkezett báró Eötvös József 1868-as népiskolai törvénye?",
            "options": ["A 6–12 éves kor közötti kötelező és ingyenes elemi anyanyelvi oktatásról", "Az egyetemek bezárásáról", "Csak a latin nyelvű iskolák működéséről", "A tanárok katonai szolgálatáról"],
            "correctIndex": 0,
            "explanation": "Az 1868-as népiskolai törvény tette kötelezővé és általánossá az alapfokú oktatást."
        }
    ]
)
write_json(STORIES_DIR / "story.b1.kiegyezes.05.json", story_5)

voc_5 = {
    "id": "voc.b1.kiegyezes.05",
    "title": "A modern oktatás és nemzetiségi jogok szókincse",
    "description": "Népiskolai törvény, nemzetiségi törvény, elemi iskola, anyanyelvhasználat és liberalizmus.",
    "entries": [
        {"lemma": "népiskolai törvény", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "1868 Primary Education Act establishing compulsory schooling", "examples": [{"hu": "A népiskolai törvény felszámolta az analfabetizmust.", "en": "The primary education act eliminated illiteracy."}]}]},
        {"lemma": "nemzetiségi törvény", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "1868 liberal law regulating the rights of nationalities", "examples": [{"hu": "A nemzetiségi törvény szabad anyanyelvhasználatot biztosított.", "en": "The nationalities act ensured free use of mother tongue."}]}]},
        {"lemma": "elemi iskola", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "primary elementary school for children", "examples": [{"hu": "Minden faluban épült elemi iskola.", "en": "An elementary school was built in every village."}]}]},
        {"lemma": "anyanyelvhasználat", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "right to use one's native language in administration and school", "examples": [{"hu": "Garantálták a nemzetiségek anyanyelvhasználatát.", "en": "The mother tongue usage of nationalities was guaranteed."}]}]},
        {"lemma": "türelmes", "pos": "adjective", "cefr": "B1", "definitions": [{"meaning": "tolerant, liberal toward ethnic and religious minorities", "examples": [{"hu": "A törvény türelmes és méltányos szabályozást hozott.", "en": "The law brought tolerant and equitable regulation."}]}]}
    ]
}
write_json(VOCAB_DIR / "voc.b1.kiegyezes.05.json", voc_5)

gr_5 = {
    "id": "gr.b1.kiegyezes.05",
    "title": "Jogbiztosítást és kötelezettséget előíró szerkezetek (biztosítja a jogot, kötelezővé teszi, garantál)",
    "description": "Formulating educational entitlements, minority language rights, and state obligations.",
    "rules": [
        "A törvényi jogok biztosítását a 'biztosítja a jogot valamire', 'garantálja a szabad használatot' szerkezetekkel fejezzük ki.",
        "Az általános kötelezettséget a 'kötelezővé teszi a...', 'elrendeli, hogy...' kifejezések írják le."
    ],
    "tables": [
        {"headers": ["Kifejezés", "Funkció", "Példa"], "rows": [
            ["biztosítja a jogot", "jogadás", "Biztosította a szabad nyelvhasználatot."],
            ["kötelezővé teszi", "állami kötelezés", "Kötelezővé tette az iskoláztatást."],
            ["garantál", "garanciavállalás", "Garantálta a nemzetiségi jogokat."]
        ]}
    ],
    "examples": [
        {"spanish": "Az 1868-as törvény biztosította a nemzetiségek számára az anyanyelvi oktatás jogát.", "english": "The 1868 law secured the right to native language education for nationalities."},
        {"spanish": "Eötvös József kötelezővé tette az elemi iskoláztatást minden gyermek számára.", "english": "József Eötvös made elementary schooling compulsory for all children."},
        {"spanish": "A törvény garantálta a polgárok vallási és nyelvi szabadságát.", "english": "The law guaranteed the religious and linguistic freedom of citizens."}
    ]
}
write_json(GRAMMAR_DIR / "gr.b1.kiegyezes.05.json", gr_5)

exs_5 = [
    {"id": "ex.b1.kiegyezes.05.01", "type": "multiple-choice", "lesson": "lesson.b1.kiegyezes.05", "teaches": ["nepiskolai-torveny-1868"], "prompt": "Melyik évben alkotta meg báró Eötvös József a népiskolai és a nemzetiségi törvényt?", "options": ["1868-ban", "1848-ban", "1867-ben", "1896-ban"], "correctIndex": 0, "explanation": "Eötvös József mindkét korszakalkotó törvénye 1868-ban született meg."},
    {"id": "ex.b1.kiegyezes.05.02", "type": "fill-blank", "lesson": "lesson.b1.kiegyezes.05", "teaches": ["Eotvos-Jozsef"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A népoktatás és a nemzetiségi jogok nagy reformere báró *Eötvös József* volt.", "target": "Eötvös József"},
    {"id": "ex.b1.kiegyezes.05.03", "type": "sentence-builder", "lesson": "lesson.b1.kiegyezes.05", "teaches": ["kotelezove-tesz", "oktatas"], "prompt": "Rakd össze a törvényi rendelkezést kifejező mondatot!", "chips": ["A", "törvény", "kötelezővé", "tette", "a", "hatosztályos", "elemi", "oktatást."], "target": "A törvény kötelezővé tette a hatosztályos elemi oktatást.", "english": "The law made six-grade elementary education compulsory."},
    {"id": "ex.b1.kiegyezes.05.04", "type": "multiple-choice", "lesson": "lesson.b1.kiegyezes.05", "teaches": ["nemzetisegi-torveny-1868"], "prompt": "Milyen jogokat garantált az 1868-as nemzetiségi törvény?", "options": ["Széles körű anyanyelvhasználatot az alsófokú közigazgatásban, bíróságokon és iskolákban", "Önálló hadsereget a nemzetiségeknek", "Külön nemzetiségi államok alapítását", "Minden nyelv betiltását a magyar kivételével"], "correctIndex": 0, "explanation": "A törvény szabad anyanyelvhasználatot és anyanyelvi iskolázást biztosított."},
    {"id": "ex.b1.kiegyezes.05.05", "type": "fill-blank", "lesson": "lesson.b1.kiegyezes.05", "teaches": ["anyanyelvhasznalat"], "prompt": "Egészítsd ki a mondatot a megfelelő szóval!", "sentence": "A törvény garantálta a nemzetiségek szabad *anyanyelvhasználatát*.", "target": "anyanyelvhasználatát"},
    {"id": "ex.b1.kiegyezes.05.06", "type": "sentence-builder", "lesson": "lesson.b1.kiegyezes.05", "teaches": ["biztositja", "jog"], "prompt": "Alkoss szabályos jogi mondatot!", "chips": ["A", "jogszabály", "biztosította", "az", "anyanyelvi", "tanulás", "jogát."], "target": "A jogszabály biztosította az anyanyelvi tanulás jogát.", "english": "The statute secured the right to mother-tongue learning."},
    {"id": "ex.b1.kiegyezes.05.07", "type": "multiple-choice", "lesson": "lesson.b1.kiegyezes.05", "teaches": ["elemi-iskola-eletkor"], "prompt": "Hány éves korig volt kötelező az elemi iskola az 1868-as törvény szerint?", "options": ["6-tól 12 éves korig", "8-tól 14 éves korig", "10-től 18 éves korig", "Csak 16 év felett"], "correctIndex": 0, "explanation": "A 6 és 12 év közötti gyermekek számára volt kötelező a népiskola."},
    {"id": "ex.b1.kiegyezes.05.08", "type": "fill-blank", "lesson": "lesson.b1.kiegyezes.05", "teaches": ["turelmes"], "prompt": "Egészítsd ki a mondatot!", "sentence": "Az 1868-as törvény a korabeli Európa egyik leginkább *türelmes* és liberális jogszabálya volt.", "target": "türelmes"}
]
write_json(EXERCISES_DIR / "ex.b1.kiegyezes.05.json", make_exercise_group("ex.b1.kiegyezes.05", "Eötvös József reformjai gyakorlatok", "Gyakorlatok a népiskolai és nemzetiségi törvényről, az anyanyelvhasználatról és a jogbiztosító szerkezetekről.", exs_5))

lesson_5 = make_lesson(
    "lesson.b1.kiegyezes.05",
    "Eötvös József reformjai: az 1868-as népiskolai és nemzetiségi törvény",
    "Jogbiztosítást és kötelezettséget előíró szerkezetek (biztosítja a jogot, kötelezővé teszi)",
    "Összegezzük báró Eötvös József 1868-as törvényeit: a kötelező népiskolai oktatást és az európai hírű nemzetiségi törvényt.",
    ["Megérteni az 1868-as népiskolai és nemzetiségi törvények polgári jelentőségét", "Használni a jogbiztosítást és oktatási kötelezettséget kifejező formákat", "Ismerni báró Eötvös József kultuszminiszteri örökségét"],
    "story.b1.kiegyezes.05",
    "voc.b1.kiegyezes.05",
    "gr.b1.kiegyezes.05",
    "ex.b1.kiegyezes.05",
    [e["id"] for e in exs_5]
)
write_json(LESSONS_DIR / "lesson.b1.kiegyezes.05.json", lesson_5)


# ==========================================
# CONSOLIDATION LESSON: b1-kiegyezes-consolidation
# ==========================================
cons_exs = [
    {"id": "ex.b1.kiegyezes.cons.01", "type": "multiple-choice", "lesson": "lesson.b1.kiegyezes.consolidation", "teaches": ["passziv-ellenallas-Deak"], "prompt": "Ki vezette a magyar passzív ellenállást az 1850-es évek Bach-korszakában?", "options": ["Deák Ferenc ('a haza bölcse')", "Andrássy Gyula", "Széchenyi István", "Eötvös József"], "correctIndex": 0, "explanation": "Deák Ferenc vezette a passzív ellenállást."},
    {"id": "ex.b1.kiegyezes.cons.02", "type": "fill-blank", "lesson": "lesson.b1.kiegyezes.consolidation", "teaches": ["jogfolytonossag"], "prompt": "A passzív ellenállás a magyar alkotmányos *jogfolytonosság* elvén alapult.", "sentence": "A passzív ellenállás a magyar alkotmányos *jogfolytonosság* elvén alapult.", "target": "jogfolytonosság"},
    {"id": "ex.b1.kiegyezes.cons.03", "type": "multiple-choice", "lesson": "lesson.b1.kiegyezes.consolidation", "teaches": ["Husveti-cikk-1865"], "prompt": "Melyik híres cikkével indította el Deák Ferenc a kiegyezési tárgyalásokat 1865-ben?", "options": ["A Húsvéti cikkel a Pesti Naplóban", "A Hitellel", "Az Ein Blickkel", "A Kasszandra-levéllel"], "correctIndex": 0, "explanation": "Az 1865-ös Húsvéti cikk indította el a kiegyezés folyamatát."},
    {"id": "ex.b1.kiegyezes.cons.04", "type": "fill-blank", "lesson": "lesson.b1.kiegyezes.consolidation", "teaches": ["a-haza-bolcse"], "prompt": "Deák Ferencet bölcs kompromisszumkeresése miatt *a haza bölcsének* nevezték.", "sentence": "Deák Ferencet bölcs kompromisszumkeresése miatt *a haza bölcsének* nevezték.", "target": "a haza bölcsének"},
    {"id": "ex.b1.kiegyezes.cons.05", "type": "sentence-builder", "lesson": "lesson.b1.kiegyezes.cons", "teaches": ["osszhangba-hoz", "erdek"], "prompt": "Rakd össze a mondatot!", "chips": ["Összhangba", "hozták", "a", "két", "fél", "alkotmányos", "érdekeit."], "target": "Összhangba hozták a két fél alkotmányos érdekeit.", "english": "They brought the constitutional interests of both parties into harmony."},
    {"id": "ex.b1.kiegyezes.cons.06", "type": "multiple-choice", "lesson": "lesson.b1.kiegyezes.consolidation", "teaches": ["kiegyezes-1867"], "prompt": "Melyik évben született meg az osztrák–magyar kiegyezés?", "options": ["1867-ben", "1848-ban", "1865-ben", "1873-ban"], "correctIndex": 0, "explanation": "A kiegyezést 1867-ben iktatták törvénybe."},
    {"id": "ex.b1.kiegyezes.cons.07", "type": "fill-blank", "lesson": "lesson.b1.kiegyezes.consolidation", "teaches": ["Andrassy-Gyula"], "prompt": "A kiegyezés után gróf *Andrássy Gyula* lett Magyarország miniszterelnöke.", "sentence": "A kiegyezés után gróf *Andrássy Gyula* lett Magyarország miniszterelnöke.", "target": "Andrássy Gyula"},
    {"id": "ex.b1.kiegyezes.cons.08", "type": "sentence-builder", "lesson": "lesson.b1.kiegyezes.consolidation", "teaches": ["megkoronaz", "Sisi"], "prompt": "Alkoss szabályos mondatot!", "chips": ["Budán", "magyar", "királlyá", "koronázták", "Ferenc", "Józsefet", "és", "Erzsébetet."], "target": "Budán magyar királlyá koronázták Ferenc Józsefet és Erzsébetet.", "english": "In Buda, Franz Joseph and Elisabeth were crowned Hungarian monarchs."},
    {"id": "ex.b1.kiegyezes.cons.09", "type": "multiple-choice", "lesson": "lesson.b1.kiegyezes.consolidation", "teaches": ["kozos-ugyek"], "prompt": "Melyek voltak a közös ügyek a dualizmusban?", "options": ["A külügy, a hadügy és a pénzügy", "Az oktatás és az egészségügy", "A posta és a rendőrség", "A vallás és az ipar"], "correctIndex": 0, "explanation": "A külügy, a hadügy és az ezekre vonatkozó pénzügy volt közös."},
    {"id": "ex.b1.kiegyezes.cons.10", "type": "fill-blank", "lesson": "lesson.b1.kiegyezes.consolidation", "teaches": ["dualizmus"], "prompt": "Az 1867 és 1918 közötti időszakot *dualizmusnak* nevezzük.", "sentence": "Az 1867 és 1918 közötti időszakot *dualizmusnak* nevezzük.", "target": "dualizmusnak"},
    {"id": "ex.b1.kiegyezes.cons.11", "type": "sentence-builder", "lesson": "lesson.b1.kiegyezes.consolidation", "teaches": ["delegacio", "felugyelet"], "prompt": "Rakd össze a felügyeletet leíró mondatot!", "chips": ["A", "parlamenti", "delegációk", "felügyelték", "a", "közös", "kiadásokat."], "target": "A parlamenti delegációk felügyelték a közös kiadásokat.", "english": "The parliamentary delegations supervised the joint expenditures."},
    {"id": "ex.b1.kiegyezes.cons.12", "type": "multiple-choice", "lesson": "lesson.b1.kiegyezes.consolidation", "teaches": ["Eotvos-nepiskola-1868"], "prompt": "Melyik törvény tette kötelezővé és ingyenessé az alapfokú oktatást 1868-ban?", "options": ["Az 1868-as népiskolai törvény (Eötvös József)", "Az áprilisi törvények", "A Ratio Educationis", "Az Urbárium"], "correctIndex": 0, "explanation": "Az 1868-as népiskolai törvény írta elő a kötelező elemi oktatást."},
    {"id": "ex.b1.kiegyezes.cons.13", "type": "fill-blank", "lesson": "lesson.b1.kiegyezes.consolidation", "teaches": ["nemzetisegi-torveny"], "prompt": "Az 1868-as *nemzetiségi törvény* szabad anyanyelvhasználatot biztosított.", "sentence": "Az 1868-as *nemzetiségi törvény* szabad anyanyelvhasználatot biztosított.", "target": "nemzetiségi törvény"},
    {"id": "ex.b1.kiegyezes.cons.14", "type": "sentence-builder", "lesson": "lesson.b1.kiegyezes.consolidation", "teaches": ["kotelezove-tesz", "elemi-iskola"], "prompt": "Alkoss szabályos összetett mondatot!", "chips": ["Eötvös", "József", "kötelezővé", "tette", "az", "elemi", "iskoláztatást."], "target": "Eötvös József kötelezővé tette az elemi iskoláztatást.", "english": "József Eötvös made elementary schooling compulsory."},
    {"id": "ex.b1.kiegyezes.cons.15", "type": "multiple-choice", "lesson": "lesson.b1.kiegyezes.consolidation", "teaches": ["vamunio-piac"], "prompt": "Mit biztosított a Monarchia közös vámterülete és valutája a magyar gazdaságnak?", "options": ["Hatalmas, több tízmilliós belső piacot és gyors iparosodást", "A külkereskedelem teljes megszűnését", "A gabonatermesztés visszaesését", "A bankok bezárását"], "correctIndex": 0, "explanation": "A vámunió óriási belső piacot és gyors gazdasági felvirágzást teremtett."},
    {"id": "ex.b1.kiegyezes.cons.16", "type": "fill-blank", "lesson": "lesson.b1.kiegyezes.consolidation", "teaches": ["Sisi-kiralyno"], "prompt": "A magyarok rajongásig szerették *Erzsébet királynét* (Sisit).", "sentence": "A magyarok rajongásig szerették *Erzsébet királynét* (Sisit).", "target": "Erzsébet királynét"},
    {"id": "ex.b1.kiegyezes.cons.17", "type": "sentence-builder", "lesson": "lesson.b1.kiegyezes.consolidation", "teaches": ["egyenrangu", "partner"], "prompt": "Rakd össze a mondatot!", "chips": ["Magyarország", "egyenrangú", "partnerként", "vett", "részt", "a", "Monarchiában."], "target": "Magyarország egyenrangú partnerként vett részt a Monarchiában.", "english": "Hungary participated as an equal partner in the Monarchy."},
    {"id": "ex.b1.kiegyezes.cons.18", "type": "multiple-choice", "lesson": "lesson.b1.kiegyezes.consolidation", "teaches": ["Matyas-templom-koronazas"], "prompt": "Hol koronázták meg Ferenc Józsefet 1867-ben?", "options": ["A budai Mátyás-templomban", "Pozsonyban a Szent Márton-dómban", "A pesti Bazilikában", "Bécsben a Stephansdomban"], "correctIndex": 0, "explanation": "A koronázásra a budai Mátyás-templomban került sor."},
    {"id": "ex.b1.kiegyezes.cons.19", "type": "fill-blank", "lesson": "lesson.b1.kiegyezes.consolidation", "teaches": ["anyanyelvhasznalat"], "prompt": "A nemzetiségi törvény garantálta a kisebbségek széles körű *anyanyelvhasználatát*.", "sentence": "A nemzetiségi törvény garantálta a kisebbségek széles körű *anyanyelvhasználatát*.", "target": "anyanyelvhasználatát"},
    {"id": "ex.b1.kiegyezes.cons.20", "type": "multiple-choice", "lesson": "lesson.b1.kiegyezes.consolidation", "teaches": ["kiegyezes-eredmeny"], "prompt": "Mit hozott a kiegyezés Magyarország számára a következő évtizedekben?", "options": ["Példátlan gazdasági, kulturális és városfejlődést (Budapest világvárossá válását)", "Azonnali háborút és szegénységet", "A nemesi kiváltságok visszatérését", "A vasutak lebontását"], "correctIndex": 0, "explanation": "A kiegyezés indította el a 'boldog békeidők' óriási gazdasági és kulturális felvirágzását."}
]
write_json(EXERCISES_DIR / "ex.b1.kiegyezes.consolidation.json", make_exercise_group("ex.b1.kiegyezes.consolidation", "A kiegyezés és a dualizmus összefoglaló gyakorlatok", "Átfogó teszt az 1867-es kiegyezésről, Deák Ferencről, Andrássy Gyuláról és az 1868-as reformokról.", cons_exs))

cons_lesson = {
    "id": "lesson.b1.kiegyezes.consolidation",
    "title": "The Compromise of 1867: Unit 18 Consolidation",
    "level": "B1",
    "track": "citizenship",
    "estimatedMinutes": 25,
    "prerequisites": [
        "lesson.b1.kiegyezes.01",
        "lesson.b1.kiegyezes.02",
        "lesson.b1.kiegyezes.03",
        "lesson.b1.kiegyezes.04",
        "lesson.b1.kiegyezes.05"
    ],
    "grammar": ["Unit review"],
    "vocabulary": ["Unit review"],
    "culturalContext": "Magyar történelem összefoglalás (Honosítási vizsgafelkészítő)",
    "sections": [
        {
            "type": "intro",
            "title": "Unit 18 Consolidation: The Compromise of 1867 (1849–1868)",
            "body": "Ebben az összefoglaló leckében áttekintjük a passzív ellenállás éveit, Deák Ferenc Húsvéti cikkét (1865), az 1867-es kiegyezést és Ferenc József megkoronázását, a dualista államszervezet közös ügyeit (hadügy, külügy, pénzügy), valamint Eötvös József 1868-as népiskolai és nemzetiségi törvényét."
        },
        {
            "type": "goal",
            "title": "Consolidation Goals",
            "items": [
                "A kiegyezés kulcséveinek (1865, 1867, 1868) és intézményeinek pontos ismerete",
                "Elutasító, kompromisszumos és államszervezeti szerkezetek magabiztos alkalmazása",
                "Deák Ferenc, gróf Andrássy Gyula, Sisi és báró Eötvös József történelmi szerepének megértése"
            ]
        },
        {
            "type": "exercise-group",
            "title": "Comprehensive Unit 18 Practice",
            "ref": "ex.b1.kiegyezes.consolidation",
            "exerciseRefs": [e["id"] for e in cons_exs]
        },
        {
            "type": "checklist",
            "items": [
                "Tudom, mit jelentett a passzív ellenállás és a jogfolytonosság",
                "Ismerem a Húsvéti cikk (1865) és a kiegyezés (1867) tartalmát",
                "Megértem a dualizmus és a három közös ügy rendszerét",
                "Ismerem az 1868-as népiskolai és nemzetiségi törvényeket"
            ]
        }
    ]
}
write_json(LESSONS_DIR / "lesson.b1.kiegyezes.consolidation.json", cons_lesson)

print("Unit 18 (b1-kiegyezes) complete!")
