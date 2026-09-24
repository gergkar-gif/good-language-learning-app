# -*- coding: utf-8 -*-
"""
Full Unit 17 Overhaul: Kossuth, Petőfi & the National Cause (b1-nemzetiugy)
Lessons:
1. Petőfi Sándor élete és költészete a szabadság szolgálatában
2. Kossuth Lajos emigrációja és világkörüli hatása
3. Az aradi vértanúk és Batthyány Lajos mártírhalála (1849. október 6.)
4. Széchenyi István döblingi évei és szellemi végrendelete
5. Az 1848-as eszmék továbbélése és a nemzeti identitás
Consolidation: Unit 17 Capstone (20 exercises)
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
# LESSON 1: b1-nemzetiugy-01 (Petőfi Sándor)
# ==========================================
story_1 = make_story(
    "story.b1.nemzetiugy.01",
    "Petőfi Sándor élete és költészete a szabadság szolgálatában",
    "Petőfi Sándor, a magyar költészet zsenije, életét és művészetét a nép felemelkedésének és a világszabadságnak szentelte, hősi halált halva Segesvárnál.",
    "Kiskőrös, Pest és Segesvár",
    ["Literary and existential dedication expressions (életét áldozza, szentel valaminek, mindhalálig)", "Romantic patriotic poetry"],
    ["Petőfi Sándor", "Nemzeti dal", "világszabadság", "Segesvár", "hősi halál"],
    [
        "Petőfi Sándor (1823–1849) a magyar irodalom és nemzettudat legfényesebb alakja. Kiskőrösön született egyszerű családban, és alig huszonhat esztendős élete alatt forradalmasította a magyar költészetet: a népi nyelvet és a szabadság eszméjét emelte a legmagasabb művészi szintre.",
        "Verseiben – mint az 'Egy gondolat bánt engemet' vagy a 'Nemzeti dal' – a világszabadság látnoki prófétájaként énekelt. Nemcsak szavakkal, hanem tettekkel is szolgálta hazáját: március 15-én a forradalom élére állt, majd honvéd őrnagyként és Bem József tábornok hű segédtisztjeként küzdött az erdélyi csatatereken.",
        "1849. július 31-én a segesvári csatában, a cári kozák lovasok elleni harcban esett el mindhalálig hűen saját költői fogadalmához: életét áldozta a hazáért és a szabadságért. Rejtélyes eltűnése és halhatatlan költészete a magyar nép örök legendájává emelte őt."
    ],
    [
        {"lemma": "világszabadság", "pos": "noun", "cefr": "B1", "gloss": "universal freedom, world liberty"},
        {"lemma": "látnok", "pos": "noun", "cefr": "B1", "gloss": "visionary, prophet"},
        {"lemma": "segédtiszt", "pos": "noun", "cefr": "B1", "gloss": "aide-de-camp, adjutant"},
        {"lemma": "hősi halál", "pos": "noun", "cefr": "B1", "gloss": "heroic death on battlefield"},
        {"lemma": "mindhalálig", "pos": "adverb", "cefr": "B1", "gloss": "unto death, faithfully to the end"}
    ],
    [
        {
            "question": "Melyik csatában esett el Petőfi Sándor 1849. július 31-én?",
            "options": ["A segesvári csatában", "A pákozdi csatában", "Az isaszegi csatában", "A mohácsi csatában"],
            "correctIndex": 0,
            "explanation": "Petőfi 1849. július 31-én Segesvár mellett vesztette életét a harcban."
        }
    ]
)
write_json(STORIES_DIR / "story.b1.nemzetiugy.01.json", story_1)

voc_1 = {
    "id": "voc.b1.nemzetiugy.01",
    "title": "Petőfi Sándor és a forradalmi költészet szókincse",
    "description": "Világszabadság, látnok, segédtiszt, hősi halál, elköteleződés és mindhalálig tartó hűség.",
    "entries": [
        {"lemma": "világszabadság", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "universal freedom of all humanity", "examples": [{"hu": "Petőfi a világszabadság eszméjét hirdette verseiben.", "en": "Petőfi preached the idea of universal freedom in his poems."}]}]},
        {"lemma": "látnok", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "prophetic visionary poet", "examples": [{"hu": "A költő látnokként jósolta meg saját harctéri halálát.", "en": "The poet as a visionary predicted his own death on the battlefield."}]}]},
        {"lemma": "segédtiszt", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "military aide-de-camp", "examples": [{"hu": "Petőfi Bem tábornok segédtisztjeként szolgált Erdélyben.", "en": "Petőfi served as General Bem's aide-de-camp in Transylvania."}]}]},
        {"lemma": "hősi halál", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "heroic death in battle for freedom", "examples": [{"hu": "Segesvárnál halt hősi halált a költő.", "en": "The poet died a hero's death at Segesvár."}]}]},
        {"lemma": "mindhalálig", "pos": "adverb", "cefr": "B1", "definitions": [{"meaning": "unto death, until the very end", "examples": [{"hu": "Mindhalálig hű maradt a szabadság eszméjéhez.", "en": "He remained faithful to the idea of freedom unto death."}]}]}
    ]
}
write_json(VOCAB_DIR / "voc.b1.nemzetiugy.01.json", voc_1)

gr_1 = {
    "id": "gr.b1.nemzetiugy.01",
    "title": "Elkötelezettséget és áldozatot kifejező szerkezetek (életét áldozza, szentel valaminek, hű marad)",
    "description": "Expressing existential dedication, poetic destiny, and patriotic sacrifice.",
    "rules": [
        "Az önfeláldozást és életcélt a 'valaminek szenteli az életét', 'életét áldozza valamiért' határozós igék fejezik ki.",
        "A hűséget a 'hű marad valamihez mindhalálig' szerkezettel nyomatékosítjuk."
    ],
    "tables": [
        {"headers": ["Kifejezés", "Jelentés", "Példa"], "rows": [
            ["szenteli az életét", "to dedicate one's life", "A szabadságnak szentelte életét."],
            ["életét áldozza valamiért", "to sacrifice life for", "Életét áldozta a hazáért."],
            ["hű marad mindhalálig", "faithful unto death", "Mindhalálig hű maradt a néphez."]
        ]}
    ],
    "examples": [
        {"spanish": "Petőfi Sándor egész életét és művészetét a magyar nemzet szabadságának szentelte.", "english": "Sándor Petőfi dedicated his entire life and art to the freedom of the Hungarian nation."},
        {"spanish": "A költő életét áldozta a csatamezőn a hazáért.", "english": "The poet sacrificed his life on the battlefield for the homeland."},
        {"spanish": "Segesvárnál mindhalálig harcolt a szabadságért.", "english": "At Segesvár, he fought for freedom unto death."}
    ]
}
write_json(GRAMMAR_DIR / "gr.b1.nemzetiugy.01.json", gr_1)

exs_1 = [
    {"id": "ex.b1.nemzetiugy.01.01", "type": "multiple-choice", "lesson": "lesson.b1.nemzetiugy.01", "teaches": ["Petofi-eletrajz"], "prompt": "Melyik évben született és hunyt el Petőfi Sándor?", "options": ["1823–1849", "1800–1860", "1848–1867", "1825–1890"], "correctIndex": 0, "explanation": "Petőfi Sándor 1823. január 1-jén született és 1849. július 31-én esett el."},
    {"id": "ex.b1.nemzetiugy.01.02", "type": "fill-blank", "lesson": "lesson.b1.nemzetiugy.01", "teaches": ["vilagszabadsag"], "prompt": "Egészítsd ki a mondatot!", "sentence": "Petőfi Sándor a magyar nép és a *világszabadság* költője volt.", "target": "világszabadság"},
    {"id": "ex.b1.nemzetiugy.01.03", "type": "sentence-builder", "lesson": "lesson.b1.nemzetiugy.01", "teaches": ["szentel", "szabadsag"], "prompt": "Rakd össze az elkötelezettséget kifejező mondatot!", "chips": ["Életét", "és", "tehetségét", "a", "haza", "szabadságának", "szentelte."], "target": "Életét és tehetségét a haza szabadságának szentelte.", "english": "He dedicated his life and talent to the freedom of the homeland."},
    {"id": "ex.b1.nemzetiugy.01.04", "type": "multiple-choice", "lesson": "lesson.b1.nemzetiugy.01", "teaches": ["Bem-Jozsef"], "prompt": "Kinek a segédtisztjeként küzdött Petőfi az erdélyi hadjáratban?", "options": ["Bem József tábornok ('Bem apó')", "Görgei Artúr", "Klapka György", "Damjanich János"], "correctIndex": 0, "explanation": "Petőfi Bem József tábornok hű és szeretett segédtisztje volt Erdélyben."},
    {"id": "ex.b1.nemzetiugy.01.05", "type": "fill-blank", "lesson": "lesson.b1.nemzetiugy.01", "teaches": ["hosi-halal"], "prompt": "Egészítsd ki a mondatot a megfelelő szóval!", "sentence": "A költő a segesvári csatamezőn halt *hősi halált*.", "target": "hősi halált"},
    {"id": "ex.b1.nemzetiugy.01.06", "type": "sentence-builder", "lesson": "lesson.b1.nemzetiugy.01", "teaches": ["mindhalalig", "hu"], "prompt": "Alkoss szabályos összetett mondatot!", "chips": ["Petőfi", "mindhalálig", "hű", "maradt", "szent", "eszméihez."], "target": "Petőfi mindhalálig hű maradt szent eszméihez.", "english": "Petőfi remained faithful to his sacred ideals unto death."},
    {"id": "ex.b1.nemzetiugy.01.07", "type": "multiple-choice", "lesson": "lesson.b1.nemzetiugy.01", "teaches": ["Egy-gondolat-bant-engemet"], "prompt": "Melyik híres versében jövendölte meg Petőfi, hogy a csatamezőn kíván meghalni a szabadságért?", "options": ["Egy gondolat bánt engemet", "János vitéz", "A Tisza", "Szeptember végén"], "correctIndex": 0, "explanation": "Az 'Egy gondolat bánt engemet' című látnoki versében kérte a csatatéri hősi halált."},
    {"id": "ex.b1.nemzetiugy.01.08", "type": "fill-blank", "lesson": "lesson.b1.nemzetiugy.01", "teaches": ["segesvari-csata"], "prompt": "Egészítsd ki a mondatot!", "sentence": "1849. július 31-én zajlott le a végzetes *segesvári* csata.", "target": "segesvári"}
]
write_json(EXERCISES_DIR / "ex.b1.nemzetiugy.01.json", make_exercise_group("ex.b1.nemzetiugy.01", "Petőfi Sándor gyakorlatok", "Gyakorlatok Petőfi életéről, verseiről és az önfeláldozást kifejező szerkezetekről.", exs_1))

lesson_1 = make_lesson(
    "lesson.b1.nemzetiugy.01",
    "Petőfi Sándor élete és költészete a szabadság szolgálatában",
    "Elkötelezettséget és áldozatot kifejező szerkezetek (szentel valaminek, mindhalálig)",
    "Megismerjük Petőfi Sándor forradalmi költészetét, segédtiszti szerepét Bem oldalán és a segesvári hősi halált.",
    ["Megérteni Petőfi Sándor költői és forradalmi örökségét", "Használni az elkötelezettséget és áldozatvállalást kifejező nyelvi szerkezeteket", "Ismerni az 1849. július 31-i segesvári csata jelentőségét"],
    "story.b1.nemzetiugy.01",
    "voc.b1.nemzetiugy.01",
    "gr.b1.nemzetiugy.01",
    "ex.b1.nemzetiugy.01",
    [e["id"] for e in exs_1]
)
write_json(LESSONS_DIR / "lesson.b1.nemzetiugy.01.json", lesson_1)


# ==========================================
# LESSON 2: b1-nemzetiugy-02 (Kossuth Lajos emigrációja)
# ==========================================
story_2 = make_story(
    "story.b1.nemzetiugy.02",
    "Kossuth Lajos emigrációja és világkörüli hatása",
    "A szabadságharc leverése után Kossuth Törökországba, Angliába és az Egyesült Államokba utazott, ahol 'a szabadság apostolaként' milliók ünnepelték a magyar függetlenség ügyét.",
    "Kütahya, London, New York és Torino",
    ["Global reception and historical impact clauses (fogadják, ünneplik, elismeri a világ)", "International diplomacy in exile"],
    ["Kossuth Lajos", "emigráció", "amerikai körút", "szabadság apostola", "Kasszandra-levél"],
    [
        "A világosi fegyverletétel után Kossuth Lajos kénytelen volt elhagyni a hazát. Törökországban (Kütahyában) lelt menedéket hű társaival, majd az amerikai kormány által küldött hadihajó fedélzetén nyugatra indult, hogy nemzetközi támogatást szerezzen a magyar ügynek.",
        "1851-ben és 1852-ben Angliában és az Egyesült Államokban valódi 'Kossuth-láz' tört ki. Százezres tömegek fogadták lelkes éljenzéssel; az amerikai kongresszus és az elnök díszvendégként fogadta (ő volt a második külföldi Lafayette után, aki beszédet mondhatott a Capitoliumban), és szónoklataival a modern szabadság élő szimbólumává vált.",
        "Élete hátralévő évtizedeit az olaszországi Torinóban (Turinban) töltötte tiszta emigrációban. 1867-ben megírta híres 'Kasszandra-levelét' Deák Ferencnek, amelyben látnoki erővel figyelmeztetett a kiegyezés veszélyeire és a birodalom elkerülhetetlen felbomlására. 1894-ben bekövetkezett halálakor az egész nemzet gyászolta 'Kossuth apánkat'."
    ],
    [
        {"lemma": "Kossuth-láz", "pos": "noun", "cefr": "B1", "gloss": "Kossuth mania (popular enthusiasm in US & UK)"},
        {"lemma": "éljenzés", "pos": "noun", "cefr": "B1", "gloss": "cheering, ovation"},
        {"lemma": "Kasszandra-levél", "pos": "noun", "cefr": "B1", "gloss": "Cassandra Letter (Kossuth's warning on the Compromise)"},
        {"lemma": "szónoklat", "pos": "noun", "cefr": "B1", "gloss": "oratory speech, address"},
        {"lemma": "díszvendég", "pos": "noun", "cefr": "B1", "gloss": "guest of honor"}
    ],
    [
        {
            "question": "Hogyan fogadták Kossuth Lajost az Egyesült Államokban és Angliában 1851–52-es emigrációs útján?",
            "options": ["Hatalmas lelkesedéssel ('Kossuth-láz'), a szabadság élő hősének tekintve őt", "Közömbösen, senki nem hallgatta meg", "Börtönbe zárták", "Csak az osztrák nagykövet fogadta"],
            "correctIndex": 0,
            "explanation": "Kossuthot százezres tömegek és az amerikai kongresszus is ünnepelte díszvendégként."
        }
    ]
)
write_json(STORIES_DIR / "story.b1.nemzetiugy.02.json", story_2)

voc_2 = {
    "id": "voc.b1.nemzetiugy.02",
    "title": "A nemzetközi hatás és politikai emigráció szókincse",
    "description": "Kossuth-láz, éljenzés, Kasszandra-levél, szónoklat és nemzetközi díszvendég.",
    "entries": [
        {"lemma": "Kossuth-láz", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "immense popular enthusiasm for Kossuth in Britain and the US", "examples": [{"hu": "Amerikában Kossuth-láz söpört végig.", "en": "Kossuth mania swept across America."}]}]},
        {"lemma": "éljenzés", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "enthusiastic cheering, public ovation", "examples": [{"hu": "A tömeg viharos éljenzéssel fogadta a szónokot.", "en": "The crowd received the orator with stormy cheering."}]}]},
        {"lemma": "Kasszandra-levél", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "open letter by Kossuth warning against the 1867 Compromise", "examples": [{"hu": "A Kasszandra-levél megjósolta a Monarchia szétesését.", "en": "The Cassandra Letter predicted the collapse of the Monarchy."}]}]},
        {"lemma": "szónoklat", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "masterful political speech, oration", "examples": [{"hu": "Kossuth angol nyelvű szónoklatai elragadták a hallgatóságot.", "en": "Kossuth's English speeches captivated the audience."}]}]},
        {"lemma": "díszvendég", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "official guest of honor", "examples": [{"hu": "Az amerikai kongresszus díszvendégként fogadta Kossuthot.", "en": "The US Congress received Kossuth as a guest of honor."}]}]}
    ]
}
write_json(VOCAB_DIR / "voc.b1.nemzetiugy.02.json", voc_2)

gr_2 = {
    "id": "gr.b1.nemzetiugy.02",
    "title": "Nemzetközi elismertséget és fogadtatást leíró szerkezetek (ünneplik, díszvendégként fogadják, figyelmeztet)",
    "description": "Expressing international recognition, public receptions, and prophetic political warnings.",
    "rules": [
        "A nyilvános fogadtatást a 'díszvendégként fogadják', 'lelkesen ünneplik' határozós kifejezések jelenítik meg.",
        "A figyelmeztető politikai jóslatokat a 'figyelmeztet arra, hogy...', 'megjósolja a...' szerkezetek alkotják."
    ],
    "tables": [
        {"headers": ["Kifejezés", "Funkció", "Példa"], "rows": [
            ["díszvendégként fogadják", "hivatalos tisztelet", "A Capitoliumban díszvendégként fogadták."],
            ["figyelmeztet arra, hogy...", "politikai intés", "Figyelmeztetett a szövetség veszélyeire."],
            ["szimbólumává válik", "jelképesség", "A szabadság szimbólumává vált."]
        ]}
    ],
    "examples": [
        {"spanish": "Kossuth Lajost Amerikában a népek szabadságának bajnokaként ünnepelték.", "english": "Lajos Kossuth was celebrated in America as the champion of the freedom of nations."},
        {"spanish": "A Kasszandra-levélben Kossuth figyelmeztetett a Habsburgokkal kötött alku veszélyeire.", "english": "In the Cassandra Letter, Kossuth warned of the dangers of the deal with the Habsburgs."},
        {"spanish": "A világ közvéleménye elismerte a magyar függetlenségi küzdelem nagyságát.", "english": "World public opinion recognized the greatness of the Hungarian independence struggle."}
    ]
}
write_json(GRAMMAR_DIR / "gr.b1.nemzetiugy.02.json", gr_2)

exs_2 = [
    {"id": "ex.b1.nemzetiugy.02.01", "type": "multiple-choice", "lesson": "lesson.b1.nemzetiugy.02", "teaches": ["Kossuth-emigracio"], "prompt": "Melyik olasz városban élte le Kossuth Lajos életének utolsó évtizedeit?", "options": ["Torinóban (Turinban)", "Rómában", "Velencében", "Nápolyban"], "correctIndex": 0, "explanation": "Kossuth a 'turini remeteként' élt Torinóban 1894-ben bekövetkezett haláláig."},
    {"id": "ex.b1.nemzetiugy.02.02", "type": "fill-blank", "lesson": "lesson.b1.nemzetiugy.02", "teaches": ["Kossuth-laz"], "prompt": "Egészítsd ki a mondatot!", "sentence": "Amerikában és Angliában valódi *Kossuth-láz* tört ki 1851-ben.", "target": "Kossuth-láz"},
    {"id": "ex.b1.nemzetiugy.02.03", "type": "sentence-builder", "lesson": "lesson.b1.nemzetiugy.02", "teaches": ["diszvendeg", "fogad"], "prompt": "Rakd össze a mondatot a helyes sorrendben!", "chips": ["Az", "amerikai", "kongresszus", "díszvendégként", "fogadta", "Kossuth", "Lajost."], "target": "Az amerikai kongresszus díszvendégként fogadta Kossuth Lajost.", "english": "The US Congress received Lajos Kossuth as a guest of honor."},
    {"id": "ex.b1.nemzetiugy.02.04", "type": "multiple-choice", "lesson": "lesson.b1.nemzetiugy.02", "teaches": ["Kasszandra-level-1867"], "prompt": "Mit tartalmazott Kossuth 1867-es híres Kasszandra-levele?", "options": ["Figyelmeztette Deák Ferencet a kiegyezés veszélyeire és a birodalom jövőbeli bukására", "Azonnali hazatérését jelentette be", "Pénzt kért az államtól", "Megköszönte a kiegyezést"], "correctIndex": 0, "explanation": "A levélben Kossuth megjósolta, hogy a Habsburgokhoz való láncolás a birodalommal együtt pusztítja majd el Magyarországot."},
    {"id": "ex.b1.nemzetiugy.02.05", "type": "fill-blank", "lesson": "lesson.b1.nemzetiugy.02", "teaches": ["szonoklat"], "prompt": "Egészítsd ki a mondatot a megfelelő szóval!", "sentence": "Kossuth lenyűgöző angol nyelvű *szónoklatai* bejárták a világsajtót.", "target": "szónoklatai"},
    {"id": "ex.b1.nemzetiugy.02.06", "type": "sentence-builder", "lesson": "lesson.b1.nemzetiugy.02", "teaches": ["figyelmeztet", "Kasszandra"], "prompt": "Alkoss szabályos összetett mondatot!", "chips": ["Kossuth", "figyelmeztetett", "a", "kiegyezés", "végzetes", "veszélyeire."], "target": "Kossuth figyelmeztetett a kiegyezés végzetes veszélyeire.", "english": "Kossuth warned of the fatal dangers of the Compromise."},
    {"id": "ex.b1.nemzetiugy.02.07", "type": "multiple-choice", "lesson": "lesson.b1.nemzetiugy.02", "teaches": ["Kossuth-apank"], "prompt": "Hogyan nevezte a magyar népnyelv a hazájából száműzött Kossuth Lajost?", "options": ["'Kossuth apánknak'", "'A haza bölcsének'", "'A kalapos királynak'", "'A legnagyobb magyarnak'"], "correctIndex": 0, "explanation": "A népdalokban és a népnyelvben 'Kossuth apánk' néven emlegették."},
    {"id": "ex.b1.nemzetiugy.02.08", "type": "fill-blank", "lesson": "lesson.b1.nemzetiugy.02", "teaches": ["Kasszandra-level"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A nyílt levél, amelyet Deákhoz intézett, *Kasszandra-levélként* híresült el.", "target": "Kasszandra-levélként"}
]
write_json(EXERCISES_DIR / "ex.b1.nemzetiugy.02.json", make_exercise_group("ex.b1.nemzetiugy.02", "Kossuth emigrációja gyakorlatok", "Gyakorlatok Kossuth nemzetközi körútjáról, a Kasszandra-levélről és az elismertséget kifejező kifejezésekről.", exs_2))

lesson_2 = make_lesson(
    "lesson.b1.nemzetiugy.02",
    "Kossuth Lajos emigrációja és világkörüli hatása",
    "Nemzetközi elismertséget és fogadtatást leíró szerkezetek (ünneplik, figyelmeztet)",
    "Megismerjük Kossuth Lajos emigrációs diplomáciáját, amerikai diadalútját, a torinói éveket és a Kasszandra-levelet.",
    ["Megérteni Kossuth emigrációs tevékenységének nemzetközi súlyát", "Használni a nemzetközi fogadtatás és politikai intés nyelvtani kifejezéseit", "Ismerni a Kasszandra-levél (1867) történelmi próféciáját"],
    "story.b1.nemzetiugy.02",
    "voc.b1.nemzetiugy.02",
    "gr.b1.nemzetiugy.02",
    "ex.b1.nemzetiugy.02",
    [e["id"] for e in exs_2]
)
write_json(LESSONS_DIR / "lesson.b1.nemzetiugy.02.json", lesson_2)


# ==========================================
# LESSON 3: b1-nemzetiugy-03 (Aradi vértanúk 1849. október 6.)
# ==========================================
story_3 = make_story(
    "story.b1.nemzetiugy.03",
    "Az aradi vértanúk és Batthyány Lajos mártírhalála (1849. október 6.)",
    "1849. október 6-án Haynau tábornagy véres megtorlásában kivégezték a 13 aradi honvédtábornokot és Pesten gróf Batthyány Lajos miniszterelnököt, megteremtve a nemzet legszentebb gyásznapját.",
    "Arad és a pesti Újépület",
    ["Solemn remembrance and martyrdom structures (kivégez, mártírhalált hal, nemzeti gyásznap)", "National day of mourning"],
    ["aradi vértanúk", "1849. október 6.", "Batthyány Lajos", "Haynau megtorlása", "nemzeti gyásznap"],
    [
        "A szabadságharc leverése után Ferenc József megbízásából Julius Jacob von Haynau tábornagy kíméletlen katonai diktatúrát és véres megtorlást vezetett be Magyarországon. A bécsi udvar célja a függetlenségi törekvések örök elrettentése és a nemzeti vezetők elpusztítása volt.",
        "1849. október 6-án hajnalban Aradon kivégezték a magyar honvédsereg 13 tábornokát (köztük Aulich Lajost, Damjanich Jánost, Kiss Ernőt, Poeltenberg Ernőt és Lahner Györgyöt). Négyüket golyó által, kilencüket kötél által végezték ki. Mindannyian emelt fővel, a magyar haza iránti hűséggel léptek a vesztőhelyre.",
        "Ugyanezen a napon Pesten, az Újépület udvarán golyó általi halállal végezték ki az első független magyar miniszterelnököt, gróf Batthyány Lajost. Október 6. a magyar nemzet hivatalos nemzeti gyásznapja, amelyen az egész ország néma tiszteletadással hajt fejet a szabadságért mártírhalált halt hősök emléke előtt."
    ],
    [
        {"lemma": "aradi vértanúk", "pos": "noun", "cefr": "B1", "gloss": "13 Martyrs of Arad (executed generals)"},
        {"lemma": "megtorlás", "pos": "noun", "cefr": "B1", "gloss": "bloody retaliation, retribution"},
        {"lemma": "nemzeti gyásznap", "pos": "noun", "cefr": "B1", "gloss": "national day of mourning (October 6)"},
        {"lemma": "mártírhalál", "pos": "noun", "cefr": "B1", "gloss": "martyrdom, martyr's death"},
        {"lemma": "vesztőhely", "pos": "noun", "cefr": "B1", "gloss": "place of execution, scaffold"}
    ],
    [
        {
            "question": "Kiket végeztek ki 1849. október 6-án Aradon és Pesten?",
            "options": ["A 13 aradi honvédtábornokot és gróf Batthyány Lajos miniszterelnököt", "Petőfi Sándort és Kossuth Lajost", "Széchenyi Istvánt és Deák Ferencet", "Görgei Artúrt és Bem Józsefet"],
            "correctIndex": 0,
            "explanation": "1849. október 6-án Aradon a 13 honvédtábornokot, Pesten pedig Batthyány Lajost végezték ki."
        }
    ]
)
write_json(STORIES_DIR / "story.b1.nemzetiugy.03.json", story_3)

voc_3 = {
    "id": "voc.b1.nemzetiugy.03",
    "title": "Az aradi vértanúk és a nemzeti gyász szókincse",
    "description": "Aradi vértanúk, megtorlás, nemzeti gyásznap, mártírhalál és tiszteletadás.",
    "entries": [
        {"lemma": "aradi vértanúk", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "the 13 Hungarian generals executed at Arad on October 6, 1849", "examples": [{"hu": "Az aradi vértanúk emléke örökké él a nemzet szívében.", "en": "The memory of the martyrs of Arad lives forever in the nation's heart."}]}]},
        {"lemma": "megtorlás", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "bloody post-revolution retribution", "examples": [{"hu": "Haynau véres megtorlást hajtott végre Magyarországon.", "en": "Haynau carried out bloody retribution in Hungary."}]}]},
        {"lemma": "nemzeti gyásznap", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "official national day of mourning", "examples": [{"hu": "Október 6-a a magyar nemzet hivatalos gyásznapja.", "en": "October 6 is the official day of mourning of the Hungarian nation."}]}]},
        {"lemma": "mártírhalál", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "death as a martyr for one's nation", "examples": [{"hu": "Batthyány Lajos mártírhalált halt a hazáért.", "en": "Lajos Batthyány died a martyr's death for the homeland."}]}]},
        {"lemma": "vesztőhely", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "execution site, scaffold", "examples": [{"hu": "A tábornokok emelt fővel léptek a vesztőhelyre.", "en": "The generals stepped onto the scaffold with heads held high."}]}]}
    ]
}
write_json(VOCAB_DIR / "voc.b1.nemzetiugy.03.json", voc_3)

gr_3 = {
    "id": "gr.b1.nemzetiugy.03",
    "title": "Ünnepélyes megemlékezést és gyászt kifejező szerkezetek (kivégez, fejet hajt, tiszteleg)",
    "description": "Expressing commemorative respect, historical martyrdom, and national mourning.",
    "rules": [
        "A történelmi kegyelet kifejezésére a 'fejet hajt valaki előtt', 'tiszteleg valaki emléke előtt' kifejezéseket használjuk.",
        "A megtorlás eseményeit a 'kivégezték', 'mártírhalált halt' igék írják le."
    ],
    "tables": [
        {"headers": ["Kifejezés", "Funkció", "Példa"], "rows": [
            ["fejet hajt", "tiszteletadás, gyász", "A nemzet fejet hajt a hősök előtt."],
            ["mártírhalált hal", "önfeláldozás", "Mártírhalált halt a hazáért."],
            ["kivégezték", "végrehajtott ítélet", "Aradon kivégezték a tábornokokat."]
        ]}
    ],
    "examples": [
        {"spanish": "Október 6-án Magyarország néma tiszteletadással hajt fejet az aradi vértanúk emléke előtt.", "english": "On October 6, Hungary bows its head in silent respect before the memory of the martyrs of Arad."},
        {"spanish": "A tizenhárom tábornok és Batthyány miniszterelnök mártírhalála a szabadság szimbóluma.", "english": "The martyrdom of the thirteen generals and Prime Minister Batthyány is a symbol of freedom."},
        {"spanish": "A vesztőhelyen mondott utolsó szavaik a hazaszeretet példái.", "english": "Their last words spoken at the execution site are examples of patriotism."}
    ]
}
write_json(GRAMMAR_DIR / "gr.b1.nemzetiugy.03.json", gr_3)

exs_3 = [
    {"id": "ex.b1.nemzetiugy.03.01", "type": "multiple-choice", "lesson": "lesson.b1.nemzetiugy.03", "teaches": ["oktober-6-1849"], "prompt": "Melyik nap a magyar nemzet hivatalos nemzeti gyásznapja az aradi vértanúk emlékére?", "options": ["Október 6-a", "Március 15-e", "Május 21-e", "Augusztus 20-a"], "correctIndex": 0, "explanation": "Október 6. az 1849-es kivégzések nemzeti gyásznapja."},
    {"id": "ex.b1.nemzetiugy.03.02", "type": "fill-blank", "lesson": "lesson.b1.nemzetiugy.03", "teaches": ["aradi-vertanuk"], "prompt": "Egészítsd ki a mondatot!", "sentence": "Aradon végezték ki a tizenhárom honvédtábornokot, az *aradi vértanúkat*.", "target": "aradi vértanúkat"},
    {"id": "ex.b1.nemzetiugy.03.03", "type": "sentence-builder", "lesson": "lesson.b1.nemzetiugy.03", "teaches": ["fejet-hajt", "vertanuk"], "prompt": "Rakd össze a megemlékező mondatot!", "chips": ["A", "nemzet", "fejet", "hajt", "az", "aradi", "vértanúk", "előtt."], "target": "A nemzet fejet hajt az aradi vértanúk előtt.", "english": "The nation bows its head before the martyrs of Arad."},
    {"id": "ex.b1.nemzetiugy.03.04", "type": "multiple-choice", "lesson": "lesson.b1.nemzetiugy.03", "teaches": ["Batthyany-kivegzes"], "prompt": "Hol és hogyan végezték ki gróf Batthyány Lajos első miniszterelnököt 1849. október 6-án?", "options": ["Pesten az Újépület udvarán, golyó által", "Aradon kötélen", "Bécsben a börtönben", "Pozsonyban a várfalnál"], "correctIndex": 0, "explanation": "Batthyány Lajost Pesten az Újépületnél lőtték agyon 1849. október 6-án este."},
    {"id": "ex.b1.nemzetiugy.03.05", "type": "fill-blank", "lesson": "lesson.b1.nemzetiugy.03", "teaches": ["martirhalal"], "prompt": "Egészítsd ki a mondatot a megfelelő szóval!", "sentence": "A hősök *mártírhalált* haltak a magyar szabadságért.", "target": "mártírhalált"},
    {"id": "ex.b1.nemzetiugy.03.06", "type": "sentence-builder", "lesson": "lesson.b1.nemzetiugy.03", "teaches": ["Haynau", "megtorlas"], "prompt": "Alkoss szabályos összetett mondatot!", "chips": ["Haynau", "kegyetlen", "megtorlást", "vezetett", "be", "a", "vereség", "után."], "target": "Haynau kegyetlen megtorlást vezetett be a vereség után.", "english": "Haynau introduced cruel retribution after the defeat."},
    {"id": "ex.b1.nemzetiugy.03.07", "type": "multiple-choice", "lesson": "lesson.b1.nemzetiugy.03", "teaches": ["vertanuk-szama"], "prompt": "Hány honvédtábornokot végeztek ki Aradon 1849. október 6-án?", "options": ["Tizenhárom (13)", "Tíz", "Tizenkettő", "Húsz"], "correctIndex": 0, "explanation": "Aradon 13 honvédtábornokot végeztek ki ezen a napon."},
    {"id": "ex.b1.nemzetiugy.03.08", "type": "fill-blank", "lesson": "lesson.b1.nemzetiugy.03", "teaches": ["nemzeti-gyasznap"], "prompt": "Egészítsd ki a mondatot!", "sentence": "Október 6. Magyarország hivatalos *nemzeti gyásznapja*.", "target": "nemzeti gyásznapja"}
]
write_json(EXERCISES_DIR / "ex.b1.nemzetiugy.03.json", make_exercise_group("ex.b1.nemzetiugy.03", "Az aradi vértanúk gyakorlatai", "Gyakorlatok az 1849. október 6-i vértanúkról, Batthyány Lajosról és a megemlékező kifejezésekről.", exs_3))

lesson_3 = make_lesson(
    "lesson.b1.nemzetiugy.03",
    "Az aradi vértanúk és Batthyány Lajos mártírhalála (1849. október 6.)",
    "Ünnepélyes megemlékezést és gyászt kifejező szerkezetek (fejet hajt, mártírhalál)",
    "Megismerjük az 1849. október 6-i aradi és pesti kivégzéseket, Haynau megtorlását és a nemzeti gyásznap jelentőségét.",
    ["Megérteni október 6. nemzeti gyásznapunk történetét és áldozatait", "Használni a kegyelet és ünnepélyes megemlékezés nyelvtani formáit", "Ismerni a 13 aradi vértanú és Batthyány Lajos miniszterelnök mártíromságát"],
    "story.b1.nemzetiugy.03",
    "voc.b1.nemzetiugy.03",
    "gr.b1.nemzetiugy.03",
    "ex.b1.nemzetiugy.03",
    [e["id"] for e in exs_3]
)
write_json(LESSONS_DIR / "lesson.b1.nemzetiugy.03.json", lesson_3)


# ==========================================
# LESSON 4: b1-nemzetiugy-04 (Széchenyi István döblingi évei)
# ==========================================
story_4 = make_story(
    "story.b1.nemzetiugy.04",
    "Széchenyi István döblingi évei és szellemi végrendelete",
    "Széchenyi István a bécsi Döblingben gyógyulva az elnyomó Bach-korszak legélesebb bírálójává vált: 'Ein Blick' című művében leleplezte az abszolutizmus hazugságait.",
    "Döbling és Nagycenk",
    ["Evaluative synthesis and political satire (leleplez, szellemi örökség, figyelmeztet arra, hogy)", "Intellectual resistance to tyranny"],
    ["Széchenyi István", "Döbling", "Ein Blick", "Bach-korszak", "szellemi végrendelet"],
    [
        "Az 1848 szeptemberében bekövetkezett idegösszeomlása után gróf Széchenyi István a Bécs melletti döblingi gyógyintézetbe vonult vissza. Bár a világ azt hitte, hogy a gróf elméje megbomlott, az 1850-es években szellemi ereje teljesen visszatért, és Döbling a magyar politikai ellenállás titkos szellemi központjává vált.",
        "Amikor Alexander Bach belügyminiszter névtelen propagandairatban dicsérte a magyarok elnyomását és a modernizáció állítólagos sikereit, Széchenyi 1859-ben Londonban névtelenül megjelentette zseniális és megsemmisítő szatíráját, az 'Ein Blick' (Egy pillantás) című könyvet, nevetségessé téve és leleplezve az abszolutizmust.",
        "A bécsi titkosrendőrség házkutatást tartott nála és súlyosan megfenyegette a grófot. Hogy elkerülje a megalázó letartóztatást és börtönt, Széchenyi 1860. április 8-án saját kezével vetett véget életének. Temetése Nagycenken tízezres néma nemzeti tüntetéssé vált, és szellemi öröksége elindította a kiegyezéshez vezető folyamatokat."
    ],
    [
        {"lemma": "szatíra", "pos": "noun", "cefr": "B1", "gloss": "satire, polemical ridicule"},
        {"lemma": "leleplez", "pos": "verb", "cefr": "B1", "gloss": "to unmask, expose (lies/tyranny)"},
        {"lemma": "házkutatás", "pos": "noun", "cefr": "B1", "gloss": "police search of residence"},
        {"lemma": "szellemi örökség", "pos": "noun", "cefr": "B1", "gloss": "intellectual / spiritual legacy"},
        {"lemma": "megtorlás", "pos": "noun", "cefr": "B1", "gloss": "retribution, suppression"}
    ],
    [
        {
            "question": "Melyik híres szatirikus művében leplezte le Széchenyi a Bach-rendszer elnyomását 1859-ben?",
            "options": ["Ein Blick (Egy pillantás)", "Hitel", "Világ", "Stádium"],
            "correctIndex": 0,
            "explanation": "Az 1859-ben kiadott 'Ein Blick' volt Széchenyi zseniális politikai szatírája Bach ellen."
        }
    ]
)
write_json(STORIES_DIR / "story.b1.nemzetiugy.04.json", story_4)

voc_4 = {
    "id": "voc.b1.nemzetiugy.04",
    "title": "A döblingi ellenállás és szellemi örökség szókincse",
    "description": "Ein Blick, szatíra, leleplezés, házkutatás, szellemi örökség és ellenállás.",
    "entries": [
        {"lemma": "szatíra", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "sharp political satire ridiculing oppression", "examples": [{"hu": "Széchenyi megsemmisítő szatírát írt a rendszerről.", "en": "Széchenyi wrote a crushing satire of the system."}]}]},
        {"lemma": "leleplez", "pos": "verb", "cefr": "B1", "definitions": [{"meaning": "to unmask, expose deception", "examples": [{"hu": "A könyv leleplezte az abszolutizmus igazi arcát.", "en": "The book exposed the true face of absolutism."}]}]},
        {"lemma": "házkutatás", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "police search of premises", "examples": [{"hu": "A rendőrség házkutatást tartott a döblingi szobában.", "en": "The police conducted a search in the Döbling room."}]}]},
        {"lemma": "szellemi örökség", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "intellectual and moral legacy", "examples": [{"hu": "Széchenyi szellemi öröksége máig útmutató a nemzetnek.", "en": "Széchenyi's intellectual legacy is a guide for the nation to this day."}]}]},
        {"lemma": "elnyomás", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "tyrannical political oppression", "examples": [{"hu": "A Bach-korszak elnyomása nem törte meg a magyarságot.", "en": "The oppression of the Bach era did not break the Hungarians."}]}]}
    ]
}
write_json(VOCAB_DIR / "voc.b1.nemzetiugy.04.json", voc_4)

gr_4 = {
    "id": "gr.b1.nemzetiugy.04",
    "title": "Kritikai és leleplező szerkezetek (leleplez, rámutat arra, hogy, nevetségessé tesz)",
    "description": "Formulating political critique, satire analysis, and intellectual exposures.",
    "rules": [
        "A leleplezést és bírálatot a 'leleplezi a valóságot', 'rámutat a hibákra', 'nevetségessé tesz' kifejezések fejezik ki.",
        "A történelmi hatást a 'szellemi öröksége utat nyit a...' szerkezettel írjuk le."
    ],
    "tables": [
        {"headers": ["Kifejezés", "Funkció", "Példa"], "rows": [
            ["leleplez", "valóság feltárása", "Leleplezte a bécsi udvar hazugságait."],
            ["rámutat arra, hogy...", "kritikai érvelés", "Rámutatott arra, hogy a rendszer megbukott."],
            ["nevetségessé tesz", "szatirikus gúny", "Nevetségessé tette Bach minisztert."]
        ]}
    ],
    "examples": [
        {"spanish": "Széchenyi István Döblingből irányította a passzív ellenállás szellemi erőit.", "english": "István Széchenyi directed the intellectual forces of passive resistance from Döbling."},
        {"spanish": "Az 'Ein Blick' rámutatott arra, hogy a Bach-rendszer elnyomja a magyar népet.", "english": "'Ein Blick' pointed out that the Bach system was oppressing the Hungarian people."},
        {"spanish": "Temetése Nagycenken a nemzet egységét és háláját mutatta meg.", "english": "His funeral in Nagycenk demonstrated the unity and gratitude of the nation."}
    ]
}
write_json(GRAMMAR_DIR / "gr.b1.nemzetiugy.04.json", gr_4)

exs_4 = [
    {"id": "ex.b1.nemzetiugy.04.01", "type": "multiple-choice", "lesson": "lesson.b1.nemzetiugy.04", "teaches": ["Dobling-Szechenyi"], "prompt": "Hol töltötte Széchenyi István életének utolsó éveit 1848 után?", "options": ["A Bécs melletti Döblingben", "Nagycenken", "Pesten", "Londonban"], "correctIndex": 0, "explanation": "Széchenyi a döblingi szanatóriumban élt 1848-tól 1860-ig."},
    {"id": "ex.b1.nemzetiugy.04.02", "type": "fill-blank", "lesson": "lesson.b1.nemzetiugy.04", "teaches": ["Ein-Blick"], "prompt": "Egészítsd ki a mondatot!", "sentence": "Széchenyi 1859-es zseniális szatírájának címe *Ein Blick* volt.", "target": "Ein Blick"},
    {"id": "ex.b1.nemzetiugy.04.03", "type": "sentence-builder", "lesson": "lesson.b1.nemzetiugy.04", "teaches": ["leleplez", "abszolutizmus"], "prompt": "Rakd össze a leleplező mondatot!", "chips": ["A", "mű", "leleplezte", "a", "Bach-korszak", "zsarnoki", "elnyomását."], "target": "A mű leleplezte a Bach-korszak zsarnoki elnyomását.", "english": "The work unmasked the tyrannical oppression of the Bach era."},
    {"id": "ex.b1.nemzetiugy.04.04", "type": "multiple-choice", "lesson": "lesson.b1.nemzetiugy.04", "teaches": ["Bach-korszak"], "prompt": "Hogy nevezték az 1850-es évek nyílt osztrák abszolutista elnyomását?", "options": ["Bach-korszaknak (Alexander Bach belügyminiszterről)", "Rákóczi-korszaknak", "Reformkornak", "Dualizmusnak"], "correctIndex": 0, "explanation": "Az 1850-es évek diktatúrája a Bach-korszak nevet viseli."},
    {"id": "ex.b1.nemzetiugy.04.05", "type": "fill-blank", "lesson": "lesson.b1.nemzetiugy.04", "teaches": ["szellemi-orokseg"], "prompt": "Egészítsd ki a mondatot a megfelelő szóval!", "sentence": "Széchenyi gazdag *szellemi örökséget* hagyott a nemzetre.", "target": "szellemi örökséget"},
    {"id": "ex.b1.nemzetiugy.04.06", "type": "sentence-builder", "lesson": "lesson.b1.nemzetiugy.04", "teaches": ["Nagy-cenk", "temetes"], "prompt": "Alkoss szabályos történelmi mondatot!", "chips": ["Széchenyi", "nagycenki", "temetése", "néma", "nemzeti", "tüntetéssé", "vált."], "target": "Széchenyi nagycenki temetése néma nemzeti tüntetéssé vált.", "english": "Széchenyi's funeral at Nagycenk became a silent national demonstration."},
    {"id": "ex.b1.nemzetiugy.04.07", "type": "multiple-choice", "lesson": "lesson.b1.nemzetiugy.04", "teaches": ["Szechenyi-halala-1860"], "prompt": "Melyik évben hunyt el gróf Széchenyi István Döblingben?", "options": ["1860-ban (április 8-án)", "1848-ban", "1867-ben", "1894-ben"], "correctIndex": 0, "explanation": "Széchenyi 1860. április 8-án hunyt el Döblingben."},
    {"id": "ex.b1.nemzetiugy.04.08", "type": "fill-blank", "lesson": "lesson.b1.nemzetiugy.04", "teaches": ["szatira"], "prompt": "Egészítsd ki a mondatot!", "sentence": "Az Ein Blick csípős és megsemmisítő politikai *szatíra* volt.", "target": "szatíra"}
]
write_json(EXERCISES_DIR / "ex.b1.nemzetiugy.04.json", make_exercise_group("ex.b1.nemzetiugy.04", "Széchenyi döblingi évei gyakorlatok", "Gyakorlatok a Bach-korszakról, az Ein Blickről és a szatirikus leleplező kifejezésekről.", exs_4))

lesson_4 = make_lesson(
    "lesson.b1.nemzetiugy.04",
    "Széchenyi István döblingi évei és szellemi végrendelete",
    "Kritikai és leleplező szerkezetek (leleplez, rámutat arra, hogy)",
    "Megismerjük Széchenyi döblingi ellenállását, az Ein Blick című politikai szatírát és 1860-as halálának nemzeti hatását.",
    ["Megérteni a Bach-korszak elnyomását és Széchenyi szellemi ellenállását", "Használni a kritikai és politikai leleplezés nyelvtani formáit", "Ismerni az Ein Blick és a nagycenki temetés történelmi jelentőségét"],
    "story.b1.nemzetiugy.04",
    "voc.b1.nemzetiugy.04",
    "gr.b1.nemzetiugy.04",
    "ex.b1.nemzetiugy.04",
    [e["id"] for e in exs_4]
)
write_json(LESSONS_DIR / "lesson.b1.nemzetiugy.04.json", lesson_4)


# ==========================================
# LESSON 5: b1-nemzetiugy-05 (1848 eszméinek továbbélése)
# ==========================================
story_5 = make_story(
    "story.b1.nemzetiugy.05",
    "Az 1848-as eszmék továbbélése és a nemzeti identitás",
    "A szabadság, egyenlőség és testvériség 1848-as eszméi, a polgári jogok és a függetlenség vágya a magyar nemzeti identitás örök alapköveivé váltak.",
    "Budapest és az egész Kárpát-medence",
    ["Core values and continuous heritage clauses (továbbél, megalapoz, meghatároz, büszkeséggel tölt el)", "Civic foundations of modern Hungarian nationhood"],
    ["1848 öröksége", "szabadság és egyenlőség", "nemzeti identitás", "továbbélés", "polgári jogok"],
    [
        "Noha az 1848–49-es szabadságharcot fegyveres túlerővel eltiporták, a forradalom vívmányait – a jobbágyfelszabadítást, a törvény előtti egyenlőséget és a közteherviselést – már soha többé nem lehetett visszacsinálni. A feudális világ örökre eltűnt, és helyébe a modern polgári társadalom lépett.",
        "1848 eszméi továbbéltek a passzív ellenállásban, a népdalokban, a költészetben és a családok emlékezetében. Petőfi, Kossuth, Széchenyi és Batthyány alakja a hazafiság, az erkölcsi tartás és a nemzeti összefogás örök mércéjévé vált minden magyar nemzedék számára.",
        "A mai modern Magyarország alaptörvénye, demokratikus intézményrendszere és nemzeti ünnepei mind az 1848-as polgári forradalom vívmányaiban gyökereznek. Ezért mondhatjuk, hogy a magyar nemzet identitása, szabadságszeretete és állampolgári öntudata mindmáig az 1848-as eszmékből táplálkozik."
    ],
    [
        {"lemma": "továbbélés", "pos": "noun", "cefr": "B1", "gloss": "survival, continuity of ideas"},
        {"lemma": "törvény előtti egyenlőség", "pos": "noun", "cefr": "B1", "gloss": "equality before the law"},
        {"lemma": "erkölcsi tartás", "pos": "noun", "cefr": "B1", "gloss": "moral integrity / uprightness"},
        {"lemma": "gyökerezik", "pos": "verb", "cefr": "B1", "gloss": "to be rooted in"},
        {"lemma": "nemzedék", "pos": "noun", "cefr": "B1", "gloss": "generation"}
    ],
    [
        {
            "question": "Miért nem lehetett eltörölni az 1848-as vívmányokat a szabadságharc leverése után sem?",
            "options": ["Mert a jobbágyfelszabadítás és a törvény előtti egyenlőség visszafordíthatatlanul megteremtette a polgári társadalmat", "Mert a császár elfelejtette visszavonni", "Mert a törökök nem engedték", "Mert nem maradtak bírók"],
            "correctIndex": 0,
            "explanation": "A jobbágyfelszabadítás és a polgári egyenlőség megmaradt a modern társadalom alapjaként."
        }
    ]
)
write_json(STORIES_DIR / "story.b1.nemzetiugy.05.json", story_5)

voc_5 = {
    "id": "voc.b1.nemzetiugy.05",
    "title": "A nemzeti identitás és továbbélés szókincse",
    "description": "Továbbélés, törvény előtti egyenlőség, erkölcsi tartás, gyökerezés és nemzedékek.",
    "entries": [
        {"lemma": "továbbélés", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "continuity, living on of historic ideals", "examples": [{"hu": "1848 eszméinek továbbélése biztosította a jövőt.", "en": "The survival of the ideals of 1848 secured the future."}]}]},
        {"lemma": "törvény előtti egyenlőség", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "equality of all citizens before the law", "examples": [{"hu": "A törvény előtti egyenlőség a demokrácia alapja.", "en": "Equality before the law is the basis of democracy."}]}]},
        {"lemma": "erkölcsi tartás", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "moral integrity, steadfastness", "examples": [{"hu": "A mártírok erkölcsi tartása példát mutat.", "en": "The moral integrity of the martyrs sets an example."}]}]},
        {"lemma": "gyökerezik", "pos": "verb", "cefr": "B1", "definitions": [{"meaning": "to be rooted in historic heritage", "examples": [{"hu": "A modern jogrendszer az 1848-as törvényekben gyökerezik.", "en": "The modern legal system is rooted in the 1848 laws."}]}]},
        {"lemma": "nemzedék", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "generation of citizens", "examples": [{"hu": "Minden új nemzedék megőrzi a szabadság tüzét.", "en": "Every new generation preserves the fire of freedom."}]}]}
    ]
}
write_json(VOCAB_DIR / "voc.b1.nemzetiugy.05.json", voc_5)

gr_5 = {
    "id": "gr.b1.nemzetiugy.05",
    "title": "Történelmi örökséget és folytonosságot kifejező szerkezetek (továbbél, gyökerezik, megalapoz)",
    "description": "Describing historical continuity, civic values, and enduring national identity.",
    "rules": [
        "A történelmi eszmék folytonosságát a 'továbbél', 'gyökerezik valamiben', 'táplálkozik valamiből' metaforikus igékkel fejezzük ki.",
        "A nemzeti értékek szintézisét az 'alapkövévé válik', 'örök mércéül szolgál' kifejezések alkotják."
    ],
    "tables": [
        {"headers": ["Kifejezés", "Funkció", "Példa"], "rows": [
            ["továbbél", "eszmei folytonosság", "A szabadság eszméje továbbél."],
            ["gyökerezik valamiben", "eredet kifejezése", "Az alkotmány 1848-ban gyökerezik."],
            ["alapkövévé válik", "szilárd alap", "A polgári egyenlőség alapkő lett."]
        ]}
    ],
    "examples": [
        {"spanish": "A modern magyar demokrácia intézményei az 1848-as forradalom vívmányaiban gyökereznek.", "english": "The institutions of modern Hungarian democracy are rooted in the achievements of the 1848 revolution."},
        {"spanish": "A törvény előtti egyenlőség és a szabadság eszméje mindmáig továbbél a nemzetben.", "english": "Equality before the law and the idea of freedom live on in the nation to this day."},
        {"spanish": "1848 nagyjai erkölcsi mércét állítottak minden későbbi nemzedék elé.", "english": "The giants of 1848 set a moral standard for every subsequent generation."}
    ]
}
write_json(GRAMMAR_DIR / "gr.b1.nemzetiugy.05.json", gr_5)

exs_5 = [
    {"id": "ex.b1.nemzetiugy.05.01", "type": "multiple-choice", "lesson": "lesson.b1.nemzetiugy.05", "teaches": ["1848-eszmek"], "prompt": "Melyek az 1848-as forradalom legfőbb egyetemes és nemzeti eszméi?", "options": ["A szabadság, a törvény előtti egyenlőség és a testvériség", "A királyi abszolutizmus és cenzúra", "A feudalizmus visszaállítása", "Az adómentesség kiterjesztése"], "correctIndex": 0, "explanation": "A szabadság, az egyenlőség és a nemzeti függetlenség alkotják 1848 lényegét."},
    {"id": "ex.b1.nemzetiugy.05.02", "type": "fill-blank", "lesson": "lesson.b1.nemzetiugy.05", "teaches": ["torveny-elotti-egyenloseg"], "prompt": "Egészítsd ki a mondatot!", "sentence": "Az 1848-as forradalom legfőbb vívmánya a *törvény előtti egyenlőség* megteremtése volt.", "target": "törvény előtti egyenlőség"},
    {"id": "ex.b1.nemzetiugy.05.03", "type": "sentence-builder", "lesson": "lesson.b1.nemzetiugy.05", "teaches": ["gyokerezik", "eszme"], "prompt": "Rakd össze az eszmei folytonosságot kifejező mondatot!", "chips": ["A", "modern", "demokrácia", "az", "1848-as", "eszmékben", "gyökerezik."], "target": "A modern demokrácia az 1848-as eszmékben gyökerezik.", "english": "Modern democracy is rooted in the ideas of 1848."},
    {"id": "ex.b1.nemzetiugy.05.04", "type": "multiple-choice", "lesson": "lesson.b1.nemzetiugy.05", "teaches": ["nemzeti-identitas"], "prompt": "Milyen szerepet játszanak 1848 nagyjai (Petőfi, Kossuth, Széchenyi, Batthyány) a nemzeti identitásban?", "options": ["A hazafiság, az erkölcsi tartás és a szabadságszeretet örök példaképei", "Csak történelmi tankönyvek szereplői", "Külföldi uralkodók képviselői", "Nincs hatásuk a mai életre"], "correctIndex": 0, "explanation": "Ők a magyar szabadságszeretet és nemzeti öntudat örök példaképei."},
    {"id": "ex.b1.nemzetiugy.05.05", "type": "fill-blank", "lesson": "lesson.b1.nemzetiugy.05", "teaches": ["tovabbeles"], "prompt": "Egészítsd ki a mondatot a megfelelő szóval!", "sentence": "A szabadságharc eszméinek *továbbélése* megerősítette a passzív ellenállást.", "target": "továbbélése"},
    {"id": "ex.b1.nemzetiugy.05.06", "type": "sentence-builder", "lesson": "lesson.b1.nemzetiugy.05", "teaches": ["erkolcsi-tartas", "nemzedek"], "prompt": "Alkoss szabályos összetett mondatot!", "chips": ["A", "mártírok", "erkölcsi", "tartása", "példát", "ad", "minden", "nemzedéknek."], "target": "A mártírok erkölcsi tartása példát ad minden nemzedéknek.", "english": "The moral integrity of the martyrs sets an example for every generation."},
    {"id": "ex.b1.nemzetiugy.05.07", "type": "multiple-choice", "lesson": "lesson.b1.nemzetiugy.05", "teaches": ["marcius-15-mai-unneples"], "prompt": "Miért ünnepli ma is minden magyar a kokárda kitűzésével március 15-ét?", "options": ["A polgári szabadság, a függetlenség és a nemzeti összefogás tiszteletére", "Egy katonai győzelem megünneplésére", "A vasút megnyitása miatt", "Egy királyi születésnap tiszteletére"], "correctIndex": 0, "explanation": "A kokárda viselése március 15-én a szabadság és összetartozás jelképe."},
    {"id": "ex.b1.nemzetiugy.05.08", "type": "fill-blank", "lesson": "lesson.b1.nemzetiugy.05", "teaches": ["nemzedek"], "prompt": "Egészítsd ki a mondatot!", "sentence": "1848 üzenete generációról generációra, *nemzedékről nemzedékre* öröklődik.", "target": "nemzedékről nemzedékre"}
]
write_json(EXERCISES_DIR / "ex.b1.nemzetiugy.05.json", make_exercise_group("ex.b1.nemzetiugy.05", "1848 eszméinek továbbélése gyakorlatok", "Gyakorlatok a nemzeti identitásról, az egyenlőségről és a folytonosságot kifejező szerkezetekről.", exs_5))

lesson_5 = make_lesson(
    "lesson.b1.nemzetiugy.05",
    "Az 1848-as eszmék továbbélése és a nemzeti identitás",
    "Történelmi örökséget és folytonosságot kifejező szerkezetek (továbbél, gyökerezik)",
    "Összegezzük 1848 egyetemes és nemzeti örökségét: a törvény előtti egyenlőséget, a polgári szabadságjogokat és a nemzeti identitást.",
    ["Megérteni az 1848-as eszmék továbbélését és modern államiságunk alapjait", "Használni a folytonosságot és történelmi gyökereket kifejező nyelvi formákat", "Felismerni 1848 erkölcsi mércéjét és a kokárda viselésének jelentését"],
    "story.b1.nemzetiugy.05",
    "voc.b1.nemzetiugy.05",
    "gr.b1.nemzetiugy.05",
    "ex.b1.nemzetiugy.05",
    [e["id"] for e in exs_5]
)
write_json(LESSONS_DIR / "lesson.b1.nemzetiugy.05.json", lesson_5)


# ==========================================
# CONSOLIDATION LESSON: b1-nemzetiugy-consolidation
# ==========================================
cons_exs = [
    {"id": "ex.b1.nemzetiugy.cons.01", "type": "multiple-choice", "lesson": "lesson.b1.nemzetiugy.consolidation", "teaches": ["Petofi-Segesvar"], "prompt": "Melyik csatában esett el Petőfi Sándor 1849. július 31-én?", "options": ["A segesvári csatában", "A pákozdi csatában", "Az isaszegi csatában", "A világosi csatában"], "correctIndex": 0, "explanation": "Petőfi Segesvárnál halt hősi halált 1849-ben."},
    {"id": "ex.b1.nemzetiugy.cons.02", "type": "fill-blank", "lesson": "lesson.b1.nemzetiugy.consolidation", "teaches": ["vilagszabadsag"], "prompt": "Petőfi költészetének legfőbb vezérgondolata a nemzeti függetlenség és a *világszabadság* volt.", "sentence": "Petőfi költészetének legfőbb vezérgondolata a nemzeti függetlenség és a *világszabadság* volt.", "target": "világszabadság"},
    {"id": "ex.b1.nemzetiugy.cons.03", "type": "multiple-choice", "lesson": "lesson.b1.nemzetiugy.consolidation", "teaches": ["Kossuth-emigracio"], "prompt": "Hogyan fogadták Kossuth Lajost Angliában és Amerikában 1851–52-ben?", "options": ["'Kossuth-lázzal', a szabadság hőseként és a Capitolium díszvendégeként", "Ellenségesen", "Közömbösen", "Titokban tartották látogatását"], "correctIndex": 0, "explanation": "Kossuthot milliók ünnepelték angliai és amerikai körútján."},
    {"id": "ex.b1.nemzetiugy.cons.04", "type": "fill-blank", "lesson": "lesson.b1.nemzetiugy.consolidation", "teaches": ["Kasszandra-level"], "prompt": "Kossuth 1867-ben a *Kasszandra-levélben* figyelmeztette Deák Ferencet a kiegyezés veszélyeire.", "sentence": "Kossuth 1867-ben a *Kasszandra-levélben* figyelmeztette Deák Ferencet a kiegyezés veszélyeire.", "target": "Kasszandra-levélben"},
    {"id": "ex.b1.nemzetiugy.cons.05", "type": "sentence-builder", "lesson": "lesson.b1.nemzetiugy.cons", "teaches": ["szentel", "szabadsag"], "prompt": "Rakd össze az elkötelezettséget kifejező mondatot!", "chips": ["Petőfi", "életét", "a", "haza", "szabadságának", "szentelte."], "target": "Petőfi életét a haza szabadságának szentelte.", "english": "Petőfi dedicated his life to the freedom of the homeland."},
    {"id": "ex.b1.nemzetiugy.cons.06", "type": "multiple-choice", "lesson": "lesson.b1.nemzetiugy.consolidation", "teaches": ["oktober-6-vertanuk"], "prompt": "Kiket végeztek ki 1849. október 6-án Aradon és Pesten?", "options": ["A 13 aradi honvédtábornokot és gróf Batthyány Lajos miniszterelnököt", "Petőfit és Kossuthot", "Széchenyit és Deákot", "Görgeit és Klapkát"], "correctIndex": 0, "explanation": "Aradon a 13 tábornokot, Pesten Batthyány Lajost végezték ki ezen a napon."},
    {"id": "ex.b1.nemzetiugy.cons.07", "type": "fill-blank", "lesson": "lesson.b1.nemzetiugy.consolidation", "teaches": ["nemzeti-gyasznap"], "prompt": "Október 6-a a magyar nemzet hivatalos *nemzeti gyásznapja*.", "sentence": "Október 6-a a magyar nemzet hivatalos *nemzeti gyásznapja*.", "target": "nemzeti gyásznapja"},
    {"id": "ex.b1.nemzetiugy.cons.08", "type": "sentence-builder", "lesson": "lesson.b1.nemzetiugy.consolidation", "teaches": ["fejet-hajt", "aradi-vertanuk"], "prompt": "Alkoss szabályos megemlékező mondatot!", "chips": ["A", "nemzet", "fejet", "hajt", "az", "aradi", "mártírok", "előtt."], "target": "A nemzet fejet hajt az aradi mártírok előtt.", "english": "The nation bows its head before the martyrs of Arad."},
    {"id": "ex.b1.nemzetiugy.cons.09", "type": "multiple-choice", "lesson": "lesson.b1.nemzetiugy.consolidation", "teaches": ["Ein-Blick-Dobling"], "prompt": "Mit leplezett le Széchenyi István az 1859-es 'Ein Blick' című döblingi szatírájában?", "options": ["A Bach-rendszer elnyomó abszolutizmusát és hazugságait", "A magyar nyelvtan hibáit", "A Lánchíd építésének költségeit", "Az orosz hadsereget"], "correctIndex": 0, "explanation": "Az Ein Blick a Bach-korszak abszolutizmusának megsemmisítő szatírája volt."},
    {"id": "ex.b1.nemzetiugy.cons.10", "type": "fill-blank", "lesson": "lesson.b1.nemzetiugy.consolidation", "teaches": ["Dobling"], "prompt": "Széchenyi István életének utolsó éveiben a Bécs melletti *Döblingben* élt.", "sentence": "Széchenyi István életének utolsó éveiben a Bécs melletti *Döblingben* élt.", "target": "Döblingben"},
    {"id": "ex.b1.nemzetiugy.cons.11", "type": "sentence-builder", "lesson": "lesson.b1.nemzetiugy.consolidation", "teaches": ["leleplez", "abszolutizmus"], "prompt": "Rakd össze a leleplező mondatot!", "chips": ["Széchenyi", "leleplezte", "a", "bécsi", "abszolutizmus", "hazugságait."], "target": "Széchenyi leleplezte a bécsi abszolutizmus hazugságait.", "english": "Széchenyi unmasked the lies of Viennese absolutism."},
    {"id": "ex.b1.nemzetiugy.cons.12", "type": "multiple-choice", "lesson": "lesson.b1.nemzetiugy.consolidation", "teaches": ["1848-orokseg"], "prompt": "Mely vívmányok maradtak érvényben 1848 után visszavonhatatlanul?", "options": ["A jobbágyfelszabadítás és a törvény előtti egyenlőség", "A nemesi adómentesség", "A cenzúra örök fennmaradása", "A feudalizmus"], "correctIndex": 0, "explanation": "A jobbágyfelszabadítás és a polgári egyenlőség végleg megmaradt."},
    {"id": "ex.b1.nemzetiugy.cons.13", "type": "fill-blank", "lesson": "lesson.b1.nemzetiugy.consolidation", "teaches": ["torveny-elotti-egyenloseg"], "prompt": "A modern polgári társadalom legfőbb alapelve a *törvény előtti egyenlőség*.", "sentence": "A modern polgári társadalom legfőbb alapelve a *törvény előtti egyenlőség*.", "target": "törvény előtti egyenlőség"},
    {"id": "ex.b1.nemzetiugy.cons.14", "type": "sentence-builder", "lesson": "lesson.b1.nemzetiugy.consolidation", "teaches": ["gyokerezik", "1848"], "prompt": "Rakd össze az eszmei mondatot!", "chips": ["A", "magyar", "demokrácia", "az", "1848-as", "törvényekben", "gyökerezik."], "target": "A magyar demokrácia az 1848-as törvényekben gyökerezik.", "english": "Hungarian democracy is rooted in the laws of 1848."},
    {"id": "ex.b1.nemzetiugy.cons.15", "type": "multiple-choice", "lesson": "lesson.b1.nemzetiugy.consolidation", "teaches": ["szentseg-szabadsag"], "prompt": "Ki volt Bem tábornok hű segédtisztje az 1849-es erdélyi harcokban?", "options": ["Petőfi Sándor", "Kossuth Lajos", "Széchenyi István", "Arany János"], "correctIndex": 0, "explanation": "Petőfi Sándor honvéd őrnagyként Bem segédtisztje volt."},
    {"id": "ex.b1.nemzetiugy.cons.16", "type": "fill-blank", "lesson": "lesson.b1.nemzetiugy.consolidation", "teaches": ["martirhalal"], "prompt": "Gróf Batthyány Lajos miniszterelnök *mártírhalált* halt Pesten 1849. október 6-án.", "sentence": "Gróf Batthyány Lajos miniszterelnök *mártírhalált* halt Pesten 1849. október 6-án.", "target": "mártírhalált"},
    {"id": "ex.b1.nemzetiugy.cons.17", "type": "sentence-builder", "lesson": "lesson.b1.nemzetiugy.consolidation", "teaches": ["erkolcsi-tartas", "vertanuk"], "prompt": "Alkoss összefoglaló mondatot!", "chips": ["Az", "aradi", "vértanúk", "erkölcsi", "tartása", "örök", "példakép."], "target": "Az aradi vértanúk erkölcsi tartása örök példakép.", "english": "The moral integrity of the martyrs of Arad is an eternal role model."},
    {"id": "ex.b1.nemzetiugy.cons.18", "type": "multiple-choice", "lesson": "lesson.b1.nemzetiugy.consolidation", "teaches": ["kokarda"], "prompt": "Mit jelképez a piros-fehér-zöld kokárda viselése március 15-én?", "options": ["A szabadság, a hazafiság és a nemzeti összefogás eszméit", "Egy párt hovatartozását", "A katonai szolgálatot", "A tavaszi virágzást"], "correctIndex": 0, "explanation": "A kokárda a nemzeti szabadság és összetartozás jelképe."},
    {"id": "ex.b1.nemzetiugy.cons.19", "type": "fill-blank", "lesson": "lesson.b1.nemzetiugy.consolidation", "teaches": ["tovabbel"], "prompt": "1848 szelleme mindmáig *továbbél* a magyar nemzet szívében.", "sentence": "1848 szelleme mindmáig *továbbél* a magyar nemzet szívében.", "target": "továbbél"},
    {"id": "ex.b1.nemzetiugy.cons.20", "type": "multiple-choice", "lesson": "lesson.b1.nemzetiugy.consolidation", "teaches": ["Kossuth-apank-kultusz"], "prompt": "Hogyan őrizte meg a magyar nép Kossuth Lajos emlékét?", "options": ["Dalaiban, Kossuth-nótáiban és szobraiban mint 'Kossuth apánkat'", "Csak külföldi könyvekben", "Elfelejtette a nevét", "Kizárólag pénzeken"], "correctIndex": 0, "explanation": "Kossuth neve a népdalokban (Kossuth-nóták) és szobrokban élt tovább."},
]
write_json(EXERCISES_DIR / "ex.b1.nemzetiugy.consolidation.json", make_exercise_group("ex.b1.nemzetiugy.consolidation", "A nemzeti ügy és 1848 hősei összefoglaló gyakorlatok", "Átfogó teszt Petőfiről, Kossuthról, az aradi vértanúkról és 1848 eszméinek továbbéléséről.", cons_exs))

cons_lesson = {
    "id": "lesson.b1.nemzetiugy.consolidation",
    "title": "Kossuth, Petőfi & the National Cause: Unit 17 Consolidation",
    "level": "B1",
    "track": "citizenship",
    "estimatedMinutes": 25,
    "prerequisites": [
        "lesson.b1.nemzetiugy.01",
        "lesson.b1.nemzetiugy.02",
        "lesson.b1.nemzetiugy.03",
        "lesson.b1.nemzetiugy.04",
        "lesson.b1.nemzetiugy.05"
    ],
    "grammar": ["Unit review"],
    "vocabulary": ["Unit review"],
    "culturalContext": "Magyar történelem összefoglalás (Honosítási vizsgafelkészítő)",
    "sections": [
        {
            "type": "intro",
            "title": "Unit 17 Consolidation: Kossuth, Petőfi & the National Cause",
            "body": "Ebben az összefoglaló leckében áttekintjük Petőfi Sándor költészetét és segesvári hősi halálát (1849. július 31.), Kossuth Lajos emigrációját és a Kasszandra-levelet (1867), az aradi vértanúk és Batthyány Lajos mártírhalálát (1849. október 6.), Széchenyi döblingi ellenállását (Ein Blick 1859), valamint 1848 eszméinek örök továbbélését."
        },
        {
            "type": "goal",
            "title": "Consolidation Goals",
            "items": [
                "Petőfi Sándor, Kossuth Lajos, Széchenyi István és az aradi vértanúk történelmi örökségének pontos ismerete",
                "Megemlékező, önfeláldozó és eszmei folytonosságot kifejező szerkezetek magabiztos alkalmazása",
                "Október 6. nemzeti gyásznapunk és a modern polgári identitás alapjainak megértése"
            ]
        },
        {
            "type": "exercise-group",
            "title": "Comprehensive Unit 17 Practice",
            "ref": "ex.b1.nemzetiugy.consolidation",
            "exerciseRefs": [e["id"] for e in cons_exs]
        },
        {
            "type": "checklist",
            "items": [
                "Tudom, mikor és hol esett el Petőfi Sándor (1849. július 31., Segesvár)",
                "Ismerem Kossuth világkörüli emigrációját és a Kasszandra-levelet (1867)",
                "Tudom, kik voltak az aradi vértanúk és miért nemzeti gyásznap október 6.",
                "Értem Széchenyi döblingi művét (Ein Blick) és 1848 eszméinek továbbélését"
            ]
        }
    ]
}
write_json(LESSONS_DIR / "lesson.b1.nemzetiugy.consolidation.json", cons_lesson)

print("Unit 17 (b1-nemzetiugy) complete!")
