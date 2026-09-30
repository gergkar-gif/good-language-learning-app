# -*- coding: utf-8 -*-
"""
Full Unit 8 Overhaul: Matthias Corvinus & the Renaissance Court (b1-matyas)
Lessons:
1. Mátyás királlyá választása a Duna jegén (1458)
2. A Fekete Sereg és az adópolitika (Kinizsi Pál, rendkívüli hadiadó, füstpénz)
3. A reneszánsz udvar és a Bibliotheca Corviniana (Beatrix, corvinák, humanizmus)
4. "Meghalt Mátyás, oda az igazság" – Igazságos Mátyás és a jogrend
5. Mátyás hódításai (Bécs 1485) és az Anjou-Mátyás korszak öröksége (1490)
Consolidation: Unit 8 Capstone
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
        "grammar": grammar_label,
        "sections": sections,
        "goal": goals
    }

def make_consolidation_lesson(lesson_id, title, intro_body, goals, story_ref, ex_ref, ex_ids):
    sections = [
        {"type": "intro", "title": title.split(" - ")[0] if " - " in title else title, "body": intro_body},
        {"type": "goal", "title": "Unit Goals", "items": goals},
        {"type": "recycle", "count": 4},
        {"type": "story", "ref": story_ref},
        {"type": "exercise-group", "title": "Consolidation Practice", "ref": ex_ref, "exerciseRefs": ex_ids},
        {"type": "srs"},
        {"type": "checklist", "items": goals}
    ]
    return {
        "id": lesson_id,
        "title": title,
        "level": "B1",
        "grammar": "összefoglalás és ismétlés",
        "sections": sections,
        "goal": goals
    }

# -----------------
# Lesson 1: Mátyás megválasztása (1458)
# -----------------
write_json(STORIES_DIR / "b1-matyas-01-megvalasztas.json", make_story(
    "story.b1.matyas.01",
    "Hunyadi Mátyás megválasztása a Duna jegén (1458)",
    "The legendary election of 15-year-old Matthias Corvinus as King of Hungary on the frozen Danube in Pest (January 1458), freed from Prague captivity with the help of Uncle Mihály Szilágyi and Archbishop János Vitéz.",
    "Pest, Duna-jég és Buda",
    ["múlt idejű cselekvéssorok és életkor-kifejezések"],
    ["Hunyadi Mátyás", "Királyválasztás 1458", "Duna jege", "Szilágyi Mihály"],
    [
        "Hunyadi János 1456-os halála után fiai a bárói viszályok áldozataivá váltak: az idősebb fiút, Lászlót Budán kivégezték, a fiatalabb Mátyást pedig Prágában fogságban tartották.",
        "Amikor V. László király hirtelen elhunyt, 1458 januárjában a magyar nemesség és a pesti polgárság a Duna vastag jegén gyűlt össze királyválasztó országgyűlésre.",
        "A nép és a köznemesség lelkesen a törökverő hős fiát, a mindössze 15 éves Hunyadi Mátyást kiáltotta ki Magyarország királyává.",
        "Nagybátyja, Szilágyi Mihály és nevelője, Vitéz János esztergomi érsek diplomáciai tárgyalásokkal kiszabadította Mátyást a prágai fogságból, és diadalmenetben Budára kísérte.",
        "Mátyás azonnal önálló kézbe vette a hatalmat: lemondatta a kormányzót, és tehetséges, modern központosított királyi uralmat kezdett kiépíteni."
    ],
    [
        {"lemma": "királyválasztás", "pos": "noun", "cefr": "B1", "gloss": "royal election"},
        {"lemma": "kikiált", "pos": "verb", "cefr": "B1", "gloss": "to proclaim / acclaim (king)"},
        {"lemma": "köznemesség", "pos": "noun", "cefr": "B1", "gloss": "gentry / lesser nobility"},
        {"lemma": "központosítás", "pos": "noun", "cefr": "B1", "gloss": "centralization"}
    ],
    [
        {"question": "Hol gyűlt össze a magyar nemesség Mátyás királlyá választására 1458 januárjában?", "options": ["A Duna vastag jegén Pest és Buda között", "A bécsi császári várban", "Rómában a Vatikán téren", "A szegedi tanyákon"], "correctIndex": 0, "explanation": "A nemesség a Duna jegén gyűlt össze és kiáltotta ki Mátyást királynak."},
        {"question": "Hány éves volt Hunyadi Mátyás, amikor királlyá választották?", "options": ["15 éves volt", "50 éves volt", "35 éves volt", "80 éves volt"], "correctIndex": 0, "explanation": "Mátyás mindössze 15 éves fiatal volt megválasztásakor 1458-ban."},
        {"question": "Ki volt Hunyadi Mátyás édesapja?", "options": ["A törökverő hadvezér, Hunyadi János", "Szent István király", "Károly Róbert", "Luxemburgi Zsigmond"], "correctIndex": 0, "explanation": "Hunyadi Mátyás a nándorfehérvári hős, Hunyadi János fia volt."}
    ]
))

write_json(VOCAB_DIR / "b1-matyas-01-voc.json", {
    "title": "Hunyadi Mátyás megválasztása (1458)",
    "words": [
        {"lemma": "királyválasztás", "pos": "noun", "cefr": "B1", "translation": "royal election", "examples": [{"hungarian": "Az 1458-as királyválasztás történelmi pillanat volt.", "english": "The 1458 royal election was a historic moment."}]},
        {"lemma": "kikiált", "pos": "verb", "cefr": "B1", "translation": "to proclaim / acclaim", "examples": [{"hungarian": "A nép királlyá kiáltotta ki Mátyást.", "english": "The people proclaimed Matthias king."}]},
        {"lemma": "köznemesség", "pos": "noun", "cefr": "B1", "translation": "gentry / lesser nobility", "examples": [{"hungarian": "A köznemesség támogatta a Hunyadi-családot.", "english": "The lesser nobility supported the Hunyadi family."}]},
        {"lemma": "központosítás", "pos": "noun", "cefr": "B1", "translation": "centralization", "examples": [{"hungarian": "A központosítás megtörte a bárók önkényét.", "english": "Centralization broke the arbitrariness of the barons."}]},
        {"lemma": "fogság", "pos": "noun", "cefr": "B1", "translation": "captivity", "examples": [{"hungarian": "Mátyást Prágában tartották fogságban.", "english": "Matthias was held in captivity in Prague."}]},
        {"lemma": "diadalmenet", "pos": "noun", "cefr": "B1", "translation": "triumphal procession", "examples": [{"hungarian": "Diadalmenetben kísérték a fiatal királyt Budára.", "english": "They escorted the young king to Buda in a triumphal procession."}]},
        {"lemma": "kormányzó", "pos": "noun", "cefr": "B1", "translation": "governor / regent", "examples": [{"hungarian": "Hunyadi János az ország kormányzója volt.", "english": "John Hunyadi was the governor of the country."}]},
        {"lemma": "tárgyalás", "pos": "noun", "cefr": "B1", "translation": "negotiation", "examples": [{"hungarian": "Diplomáciai tárgyalásokkal érték el a szabadulást.", "english": "They achieved his release through diplomatic negotiations."}]},
        {"lemma": "lelkes", "pos": "adj", "cefr": "B1", "translation": "enthusiastic", "examples": [{"hungarian": "Lelkes tömeg fogadta az új uralkodót.", "english": "An enthusiastic crowd welcomed the new monarch."}]},
        {"lemma": "önálló", "pos": "adj", "cefr": "B1", "translation": "independent", "examples": [{"hungarian": "Önálló döntéseket hozott már fiatalon.", "english": "He made independent decisions already when young."}]},
        {"lemma": "nevelő", "pos": "noun", "cefr": "B1", "translation": "educator / tutor", "examples": [{"hungarian": "Vitéz János volt a király tudós nevelője.", "english": "János Vitéz was the king's scholarly tutor."}]},
        {"lemma": "kivégez", "pos": "verb", "cefr": "B1", "translation": "to execute", "examples": [{"hungarian": "Bátyját, Lászlót jogtalanul kivégezték.", "english": "His elder brother László was unlawfully executed."}]}
    ]
})

write_json(GRAMMAR_DIR / "b1-matyas-01-gr.json", {
    "title": "Életkor kifejezése és kikiáltási szerkezetek (mindössze, -vá/-vé kiált)",
    "level": "B1",
    "rules": [
        {
            "id": "age-expressions",
            "title": "Expressing Age in Hungarian (évesen, éves korában)",
            "text": "*Mindössze 15 évesen választották meg.* (He was elected at only 15 years of age.) *15 éves korában lépett a trónra.*",
            "tip": "Combines numbers + *évesen* or *éves korában*."
        },
        {
            "id": "proclamation-translative",
            "title": "Verbs of Proclamation with Translative Case (-vá / -vé)",
            "text": "*Királlyá kiáltották ki.* (They proclaimed him king.) *Vezérré választották.*",
            "tip": "*Kikiált* takes the translative case on the role/title."
        }
    ],
    "examples": [
        {"spanish": "A Duna jegén Mátyást királlyá kiáltották ki.", "english": "On the ice of the Danube, Matthias was proclaimed king."},
        {"spanish": "Mindössze tizenöt éves korában vette át az ország vezetését.", "english": "At only fifteen years of age, he took over the leadership of the country."},
        {"spanish": "Szilágyi Mihály tárgyalásokkal kiszabadította Mátyást a fogságból.", "english": "Mihály Szilágyi freed Matthias from captivity through negotiations."}
    ]
})

write_json(EXERCISES_DIR / "b1-matyas-01-ex.json", {
    "exercises": [
        {"id": "b1-matyas-01.ex01", "type": "multiple-choice", "title": "Mátyás király megválasztása", "instruction": "Melyik évben választották királlyá Hunyadi Mátyást?", "question": "Mikor választották meg Mátyást a Duna jegén?", "options": ["1458-ban", "1000-ben", "1222-ben", "1526-ban"], "correctIndex": 0, "explanation": "Mátyást 1458 januárjában választották királlyá.", "teaches": ["kiralyvalasztas", "kikialt"]},
        {"id": "b1-matyas-01.ex02", "type": "fill-blank", "title": "A választás helyszíne", "instruction": "Egészítsd ki a mondatot!", "sentence": "A nemesség a Duna vastag ___ gyűlt össze Pest és Buda között.", "correctAnswer": "jegén", "options": ["jegén", "hídján", "vizén", "hajóján"], "teaches": ["kiralyvalasztas"]},
        {"id": "b1-matyas-01.ex03", "type": "sentence-builder", "title": "Királlyá kikiáltás", "instruction": "Állítsd össze a mondatot!", "words": ["A", "tömeg", "lelkesen", "királlyá", "kiáltotta", "ki", "a", "fiatal", "Mátyást."], "correctSentence": "A tömeg lelkesen királlyá kiáltotta ki a fiatal Mátyást.", "english": "The crowd enthusiastically proclaimed young Matthias king.", "teaches": ["kikialt", "lelkes"]},
        {"id": "b1-matyas-01.ex04", "type": "multiple-choice", "title": "Mátyás életkora", "instruction": "Hány éves volt Mátyás 1458-ban?", "question": "Hány évesen lett Magyarország uralkodója Hunyadi Mátyás?", "options": ["15 évesen", "30 évesen", "50 évesen", "8 évesen"], "correctIndex": 0, "explanation": "Mátyás 15 éves volt megválasztásakor.", "teaches": ["kiralyvalasztas"]},
        {"id": "b1-matyas-01.ex05", "type": "fill-blank", "title": "Fogság Prágában", "instruction": "Válaszd ki a várost!", "sentence": "A királyválasztás előtt Mátyást ___ tartották fogságban.", "correctAnswer": "Prágában", "options": ["Prágában", "Londonban", "Rómában", "Párizsban"], "teaches": ["fogsag", "targyalas"]},
        {"id": "b1-matyas-01.ex06", "type": "sentence-builder", "title": "Központosított hatalom", "instruction": "Rendezd helyes sorrendbe a szavakat!", "words": ["Mátyás", "erős", "központosított", "királyi", "hatalmat", "épített", "ki."], "correctSentence": "Mátyás erős központosított királyi hatalmat épített ki.", "english": "Matthias built up strong centralized royal power.", "teaches": ["kozpontositas", "onallo"]},
        {"id": "b1-matyas-01.ex07", "type": "multiple-choice", "title": "Mátyás apja", "instruction": "Ki volt Mátyás édesapja?", "question": "Kinek a fia volt Hunyadi Mátyás?", "options": ["Hunyadi János nándorfehérvári hősé", "Nagy Lajos királyé", "Károly Róberté", "Szent Lászlóé"], "correctIndex": 0, "explanation": "Hunyadi Mátyás a híres hadvezér, Hunyadi János fia volt.", "teaches": ["kormanyzo"]},
        {"id": "b1-matyas-01.ex08", "type": "fill-blank", "title": "Diadalmenet Budára", "instruction": "Egészítsd ki a mondatot!", "sentence": "A nép ünnepélyes ___ kísérte az ifjú királyt a Budai Várba.", "correctAnswer": "diadalmenetben", "options": ["diadalmenetben", "haragban", "futásban", "fogságban"], "teaches": ["diadalmenet"]}
    ]
})

write_json(LESSONS_DIR / "b1-matyas-01.json", make_lesson(
    "lesson.b1.matyas-01",
    "Hunyadi Mátyás megválasztása (The Election of Matthias - 1458)",
    "Életkor kifejezése és kikiáltási szerkezetek (mindössze, -vá/-vé kiált)",
    [
        "Welcome to Unit 8 of the Hungarian Citizenship Track, exploring the golden age of King Matthias Corvinus (*Hunyadi Mátyás*, 1458–1490).",
        "In this first lesson, we explore his dramatic election at age 15 on the frozen Danube in January 1458, his release from Prague captivity, and his immediate consolidation of centralized royal power.",
        "We also practice expressions of age (*mindössze 15 évesen*) and verbs of proclamation with the translative case (*királlyá kiált*)."
    ],
    [
        "I can state the year (1458) and location (frozen Danube) of Matthias's election.",
        "I can explain his lineage as the son of John Hunyadi (*Hunyadi János*).",
        "I can describe how young Matthias took independent control of state administration.",
        "I can use age adverbials and proclamation structures accurately in Hungarian."
    ],
    "stories/world/b1/b1-matyas-01-megvalasztas.json",
    "vocabulary/b1/b1-matyas-01-voc.json",
    "grammar/b1/b1-matyas-01-gr.json",
    "exercises/b1/b1-matyas-01-ex.json",
    [f"b1-matyas-01.ex{i:02d}" for i in range(1, 9)]
))

# -----------------
# Lesson 2: Fekete Sereg és adópolitika
# -----------------
write_json(STORIES_DIR / "b1-matyas-02-feketesereg.json", make_story(
    "story.b1.matyas.02",
    "A Fekete Sereg és Mátyás pénzügyi reformjai",
    "King Matthias's famous standing mercenary army, the Black Army (*Fekete Sereg*) led by legends like Pál Kinizsi and Balázs Magyar, and his rigorous tax system: the extraordinary war tax (*rendkívüli hadiadó*) and the smoke tax (*füstpénz*).",
    "Buda, Szabács és Kenyérmező",
    ["pénzügyi és hadügyi szakkifejezések, feltételes igék"],
    ["Fekete Sereg", "Kinizsi Pál", "Rendkívüli hadiadó", "Füstpénz", "Kenyérmezei csata 1479"],
    [
        "Hunyadi Mátyás felismerte, hogy a nemesi felkelés lassú és megbízhatatlan. Ezért Európában az elsők között állandó, fegyelmezett zsoldoshadsereget hozott létre, amelyet a történetírás Fekete Seregként ismer.",
        "A Fekete Sereg mintegy 20–30 ezer nehézlovagból, gyalogosból, tüzérből és folyami flottából állt. Legfélelmetesebb hadvezére a legendás erejű Kinizsi Pál volt, aki 1479-ben a kenyérmezei csatában döntő vereséget mért az Erdélybe betörő oszmán seregre.",
        "Az állandó zsoldoshadsereg és a végvárrendszer fenntartása óriási pénzösszegeket igényelt. Mátyás ezért átalakította az adórendszert: a kapuadó helyett bevezette a füstpénzt (királyi kincstár adója), amelyet nem telkenként, hanem családi háztartásonként (kéményenként) kellett megfizetni, megszüntetve a korábbi adóelkerülést.",
        "Rendszeresen kivetette a rendkívüli hadiadót is, amely évi egy aranyforintot jelentett jobbágyonként. Ezzel a királyi bevételek elérték az évi egymillió aranyforintot, ami vetekedett a nyugati nagyhatalmak költségvetésével.",
        "A Fekete Sereg és a szilárd pénzügyi háttér biztosította Magyarország határainak sérthetetlenségét és a király hódító hadjáratait."
    ],
    [
        {"lemma": "Fekete Sereg", "pos": "noun", "cefr": "B1", "gloss": "Black Army (Matthias's standing mercenary army)"},
        {"lemma": "zsoldoshadsereg", "pos": "noun", "cefr": "B1", "gloss": "mercenary army / standing army"},
        {"lemma": "füstpénz", "pos": "noun", "cefr": "B1", "gloss": "smoke tax / chimney tax"},
        {"lemma": "rendkívüli hadiadó", "pos": "noun", "cefr": "B1", "gloss": "extraordinary war tax"}
    ],
    [
        {
            "question": "Hogyan nevezték Mátyás király híres állandó zsoldoshadseregét?",
            "options": ["A Fekete Seregnek", "A Vörös Hadseregnek", "A Kék Lovagoknak", "A Zöld Gárdának"],
            "correctIndex": 0,
            "explanation": "Mátyás zsoldoshadserege Fekete Sereg néven vált világhírűvé."
        },
        {
            "question": "Ki volt a Fekete Sereg legendás erejű hadvezére, a kenyérmezei csata (1479) hőse?",
            "options": ["Kinizsi Pál", "Dugovics Titusz", "Dobó István", "Zrínyi Miklós"],
            "correctIndex": 0,
            "explanation": "Kinizsi Pál volt Mátyás legkiválóbb hadvezére, aki soha nem vesztett csatát."
        },
        {
            "question": "Milyen új adót vezetett be Mátyás a kapuadó helyett a bevételek növelésére?",
            "options": ["A füstpénzt (családi kéményenként) és a rendkívüli hadiadót", "Az internetadót", "A tengeri vámot", "Az aranybehozatali büntetést"],
            "correctIndex": 0,
            "explanation": "A füstpénz háztartásonkénti fizetése és a rendkívüli hadiadó megtöbbszörözte a bevételeket."
        }
    ]
))

write_json(VOCAB_DIR / "b1-matyas-02-voc.json", {
    "title": "A Fekete Sereg és Mátyás adópolitikája",
    "words": [
        {"lemma": "Fekete Sereg", "pos": "noun", "cefr": "B1", "translation": "Black Army", "examples": [{"hungarian": "A Fekete Sereg Európa egyik legjobb hadserege volt.", "english": "The Black Army was one of Europe's best armies."}]},
        {"lemma": "zsoldoshadsereg", "pos": "noun", "cefr": "B1", "translation": "mercenary army", "examples": [{"hungarian": "Az állandó zsoldoshadsereg fegyelmezett volt.", "english": "The standing mercenary army was disciplined."}]},
        {"lemma": "füstpénz", "pos": "noun", "cefr": "B1", "translation": "smoke / chimney tax", "examples": [{"hungarian": "A füstpénzt minden kémény után beszedték.", "english": "The smoke tax was collected on every chimney."}]},
        {"lemma": "rendkívüli hadiadó", "pos": "noun", "cefr": "B1", "translation": "extraordinary war tax", "examples": [{"hungarian": "A rendkívüli hadiadó aranyforintban fizetendő adó volt.", "english": "The extraordinary war tax was payable in golden florins."}]},
        {"lemma": "tüzérség", "pos": "noun", "cefr": "B1", "translation": "artillery", "examples": [{"hungarian": "A modern tüzérség ágyúkkal ostromolta a várakat.", "english": "The modern artillery besieged the castles with cannons."}]},
        {"lemma": "hadvezér", "pos": "noun", "cefr": "B1", "translation": "commander / general", "examples": [{"hungarian": "Kinizsi Pál veretlen hadvezér maradt.", "english": "Pál Kinizsi remained an undefeated commander."}]},
        {"lemma": "költségvetés", "pos": "noun", "cefr": "B1", "translation": "budget", "examples": [{"hungarian": "A királyi költségvetés elérte az egymillió aranyat.", "english": "The royal budget reached one million gold florins."}]},
        {"lemma": "adóelkerülés", "pos": "noun", "cefr": "B1", "translation": "tax avoidance", "examples": [{"hungarian": "A reform megszüntette a korábbi adóelkerülést.", "english": "The reform put an end to earlier tax avoidance."}]},
        {"lemma": "sérthetetlenség", "pos": "noun", "cefr": "B1", "translation": "inviolability", "examples": [{"hungarian": "Biztosította a határok sérthetetlenségét.", "english": "He ensured the inviolability of the borders."}]},
        {"lemma": "háztartás", "pos": "noun", "cefr": "B1", "translation": "household", "examples": [{"hungarian": "Minden önálló háztartás adózott.", "english": "Every independent household was taxed."}]},
        {"lemma": "zsoldos", "pos": "noun", "cefr": "B1", "translation": "mercenary", "examples": [{"hungarian": "A zsoldosok rendszeres fizetést kaptak.", "english": "The mercenaries received regular pay."}]},
        {"lemma": "veretlen", "pos": "adj", "cefr": "B1", "translation": "undefeated", "examples": [{"hungarian": "Kinizsi Pál veretlen hős volt a török elleni harcban.", "english": "Pál Kinizsi was an undefeated hero in the fight against the Turks."}]}
    ]
})

write_json(GRAMMAR_DIR / "b1-matyas-02-gr.json", {
    "title": "Helyettesítő kifejezések és összehasonlító számszerkezetek (helyett, -ként)",
    "level": "B1",
    "rules": [
        {
            "id": "postposition-helyett",
            "title": "Postposition 'helyett' (Instead of)",
            "text": "*A kapuadó helyett füstpénzt vezetett be.* (Instead of the gate tax, he introduced the smoke tax.) *A nemesi sereg helyett zsoldosokat alkalmazott.*",
            "tip": "*Helyett* follows simple nominative nouns."
        },
        {
            "id": "distributive-kent",
            "title": "Distributive Suffix '-ként' (Per / As a)",
            "text": "*Jobbágyonként évi egy forint.* (One florin per serf per year.) *Háztartásonként fizették az adót.*",
            "tip": "Expresses unit rates without prepositions."
        }
    ],
    "examples": [
        {"spanish": "A kapuadó helyett a füstpénzt vezette be.", "english": "Instead of the gate tax, he introduced the smoke tax."},
        {"spanish": "Családonként egy aranyforint rendkívüli hadiadót vetett ki.", "english": "He levied an extraordinary war tax of one gold florin per family."},
        {"spanish": "A Fekete Sereg fegyelmezett zsoldoshadsereg volt.", "english": "The Black Army was a disciplined mercenary army."}
    ]
})

write_json(EXERCISES_DIR / "b1-matyas-02-ex.json", {
    "exercises": [
        {"id": "b1-matyas-02.ex01", "type": "multiple-choice", "title": "A Fekete Sereg", "instruction": "Mi volt a Fekete Sereg?", "question": "Hogyan működött Mátyás király hadserege?", "options": ["Állandó, fegyelmezett zsoldoshadsereg volt", "Önkéntes paraszti sereg", "Külföldi segélycsapat", "Csak tengeri flotta"], "correctIndex": 0, "explanation": "A Fekete Sereg Mátyás állandó zsoldoshadserege volt.", "teaches": ["Fekete-Sereg", "zsoldoshadsereg"]},
        {"id": "b1-matyas-02.ex02", "type": "fill-blank", "title": "Füstpénz bevezetése", "instruction": "Egészítsd ki a mondatot!", "sentence": "A kapuadó helyett Mátyás a ___ vezette be háztartásonként.", "correctAnswer": "füstpénzt", "options": ["füstpénzt", "vízdíjat", "autópályadíjat", "gázszámlát"], "teaches": ["fustpenz", "haztartas"]},
        {"id": "b1-matyas-02.ex03", "type": "sentence-builder", "title": "Kinizsi Pál hadvezér", "instruction": "Állítsd össze a mondatot!", "words": ["Kinizsi", "Pál", "a", "Fekete", "Sereg", "legendás", "hadvezére", "volt."], "correctSentence": "Kinizsi Pál a Fekete Sereg legendás hadvezére volt.", "english": "Pál Kinizsi was the legendary commander of the Black Army.", "teaches": ["hadvezer", "veretlen"]},
        {"id": "b1-matyas-02.ex04", "type": "multiple-choice", "title": "Kenyérmezei csata", "instruction": "Mikor győzte le Kinizsi a törököket Kenyérmezőnél?", "question": "Melyik évben zajlott a kenyérmezei csata?", "options": ["1479-ben", "1241-ben", "1526-ban", "1848-ban"], "correctIndex": 0, "explanation": "A kenyérmezei diadal 1479-ben történt.", "teaches": ["hadvezer", "veretlen"]},
        {"id": "b1-matyas-02.ex05", "type": "fill-blank", "title": "Helyett (helyett)", "instruction": "Válaszd ki a helyes névutót!", "sentence": "A nemesi felkelés ___ állandó zsoldosokat fogadott fel a király.", "correctAnswer": "helyett", "options": ["helyett", "után", "miatt", "nélkül"], "teaches": ["zsoldos"]},
        {"id": "b1-matyas-02.ex06", "type": "sentence-builder", "title": "Rendkívüli hadiadó", "instruction": "Rendezd helyes sorrendbe a szavakat!", "words": ["Mátyás", "rendszeresen", "kivetette", "a", "rendkívüli", "hadiadót."], "correctSentence": "Mátyás rendszeresen kivetette a rendkívüli hadiadót.", "english": "Matthias regularly levied the extraordinary war tax.", "teaches": ["rendkivuli-hadiado", "koltsegvetes"]},
        {"id": "b1-matyas-02.ex07", "type": "multiple-choice", "title": "Költségvetés nagysága", "instruction": "Mennyi bevétele volt Mátyás királynak évente?", "question": "Mekkora összeg folyt be a királyi kincstárba a reformok után?", "options": ["Mintegy egymillió aranyforint évente", "Csak 100 forint", "Tízmilliárd dollár", "Semmi bevétele nem volt"], "correctIndex": 0, "explanation": "Mátyás bevétele elérte az évi 1 millió aranyforintot, vetekedve a nyugati uralkodókkal.", "teaches": ["koltsegvetes", "kincstar"]},
        {"id": "b1-matyas-02.ex08", "type": "fill-blank", "title": "Disztributív rag (-ként)", "instruction": "Egészítsd ki a mondatot!", "sentence": "Évente egy aranyforintot kellett fizetni jobbágyon___.", "correctAnswer": "ként", "options": ["ként", "ban", "ról", "hoz"], "teaches": ["rendkivuli-hadiado"]}
    ]
})

write_json(LESSONS_DIR / "b1-matyas-02.json", make_lesson(
    "lesson.b1.matyas-02",
    "A Fekete Sereg és az adópolitika (The Black Army & Taxation)",
    "Helyettesítő kifejezések és összehasonlító számszerkezetek (helyett, -ként)",
    [
        "In this second lesson, we study King Matthias's military power and fiscal genius.",
        "You will learn about Europe's premier standing mercenary force, the Black Army (*Fekete Sereg*), legendary commander Pál Kinizsi (Battle of Kenyérmező, 1479), and the revenue reforms: the smoke tax (*füstpénz*) and extraordinary war tax (*rendkívüli hadiadó*).",
        "We also practice the postposition *helyett* (instead of) and distributive rates with *-ként*."
    ],
    [
        "I can describe the composition and discipline of the Black Army (*Fekete Sereg*).",
        "I can explain Pál Kinizsi's role as general and hero of Kenyérmező (1479).",
        "I can identify Matthias's tax reforms (*füstpénz, rendkívüli hadiadó*).",
        "I can use *helyett* and *-ként* correctly in economic descriptions."
    ],
    "stories/world/b1/b1-matyas-02-feketesereg.json",
    "vocabulary/b1/b1-matyas-02-voc.json",
    "grammar/b1/b1-matyas-02-gr.json",
    "exercises/b1/b1-matyas-02-ex.json",
    [f"b1-matyas-02.ex{i:02d}" for i in range(1, 9)]
))

# -----------------
# Lesson 3: Reneszánsz udvar és Corviniana
# -----------------
write_json(STORIES_DIR / "b1-matyas-03-reneszanszudvar.json", make_story(
    "story.b1.matyas.03",
    "A reneszánsz udvar, Beatrix királyné és a Bibliotheca Corviniana",
    "The Renaissance Court of King Matthias: Queen Beatrice of Naples, Italian humanists (Bonfini, Galeotto Marzio), the magnificent marble fountains of Visegrád, and the world-famous Bibliotheca Corviniana with over 2,000 illuminated codices (*corvinák*).",
    "Buda és Visegrád",
    ["művészeti és kulturális szakkifejezések, melléknévképzés"],
    ["Reneszánsz udvar", "Bibliotheca Corviniana", "Beatrix királyné", "Humanizmus", "Visegrádi palota"],
    [
        "Hunyadi Mátyás udvara Itália után Európa legkorábbi és legfényesebb reneszánsz kulturális központjává vált. A reneszánsz művészet és a humanizmus elterjedését nagyban segítette Mátyás második házassága Aragóniai Beatrix nápolyi hercegnővel 1476-ban.",
        "A királyi udvarba itáliai építészek, szobrászok, festők és humanista tudósok érkeztek, köztük Antonio Bonfini történetíró és Galeotto Marzio költő.",
        "Mátyás újjáépítette a budai és a visegrádi királyi palotát: a visegrádi palota híres vörösmárvány szökőkútjaiból és függőkertjeiből ünnepnapokon bor folyt a vendégeknek.",
        "Mátyás legnagyobb kulturális büszkesége a Bibliotheca Corviniana volt, amely a vatikáni könyvtár után a korabeli Európa második legnagyobb könyvgyűjteményének számított több mint kétezer kézzel másolt, díszes corvina kódexével.",
        "A hollós címerrel díszített corvinák és a reneszánsz műemlékek a mai napig az egyetemes emberi és magyar nemzeti kulturális örökség legféltettebb kincsei."
    ],
    [
        {"lemma": "reneszánsz", "pos": "adj", "cefr": "B1", "gloss": "Renaissance"},
        {"lemma": "corvina", "pos": "noun", "cefr": "B1", "gloss": "Corvina (illuminated Renaissance codex of Matthias)"},
        {"lemma": "humanizmus", "pos": "noun", "cefr": "B1", "gloss": "humanism"},
        {"lemma": "kódex", "pos": "noun", "cefr": "B1", "gloss": "codex / illuminated manuscript"}
    ],
    [
        {
            "question": "Melyik híres könyvtárat hozta létre Mátyás király Budán?",
            "options": ["A Bibliotheca Corvinianát (a Corvina-könyvtárat)", "Az Országos Széchényi Könyvtárat", "A londoni Nemzeti Könyvtárat", "Az alexandriai könyvtárat"],
            "correctIndex": 0,
            "explanation": "A Bibliotheca Corviniana Mátyás világhírű reneszánsz könyvtára volt."
        },
        {
            "question": "Ki volt Mátyás nápolyi származású felesége, aki segített elterjeszteni az itáliai reneszánszt?",
            "options": ["Aragóniai Beatrix királyné", "Gizella hercegnő", "Mária Terézia", "Erzsébet királyné (Sisi)"],
            "correctIndex": 0,
            "explanation": "Aragóniai Beatrix királyné révén az olasz reneszánsz kultúra közvetlenül Budára és Visegrádra költözött."
        },
        {
            "question": "Milyen madár látható a Hunyadi-család és a Corvinák címerében?",
            "options": ["A gyűrűt tartó holló (corvus)", "A sas", "A galamb", "A sólyom"],
            "correctIndex": 0,
            "explanation": "A holló (latinul corvus) a Hunyadiak címerállata, innen ered a Corvinus név."
        }
    ]
))

write_json(VOCAB_DIR / "b1-matyas-03-voc.json", {
    "title": "A reneszánsz udvar és a Bibliotheca Corviniana",
    "words": [
        {"lemma": "reneszánsz", "pos": "adj", "cefr": "B1", "translation": "Renaissance", "examples": [{"hungarian": "A reneszánsz művészet Budán virágzott először Itálián kívül.", "english": "Renaissance art flourished in Buda first outside Italy."}]},
        {"lemma": "corvina", "pos": "noun", "cefr": "B1", "translation": "Corvina codex", "examples": [{"hungarian": "A corvinák díszes reneszánsz kódexek voltak.", "english": "The corvinas were ornate Renaissance codices."}]},
        {"lemma": "humanizmus", "pos": "noun", "cefr": "B1", "translation": "humanism", "examples": [{"hungarian": "A humanizmus az embert és a tudományt helyezte a középpontba.", "english": "Humanism placed man and science at the center."}]},
        {"lemma": "kódex", "pos": "noun", "cefr": "B1", "translation": "codex / manuscript", "examples": [{"hungarian": "Kézzel másolt és festett kódexeket gyűjtött a király.", "english": "The king collected hand-copied and painted codices."}]},
        {"lemma": "szökőkút", "pos": "noun", "cefr": "B1", "translation": "fountain", "examples": [{"hungarian": "Vörösmárvány szökőkút díszítette a visegrádi palotát.", "english": "A red marble fountain decorated the Visegrád palace."}]},
        {"lemma": "függőkert", "pos": "noun", "cefr": "B1", "translation": "hanging garden", "examples": [{"hungarian": "Gyönyörű függőkertekben sétáltak a humanisták.", "english": "Humanists walked in beautiful hanging gardens."}]},
        {"lemma": "holló", "pos": "noun", "cefr": "B1", "translation": "raven", "examples": [{"hungarian": "A gyűrűt tartó holló a Hunyadi-címer jelképe.", "english": "The raven holding a ring is the symbol of the Hunyadi coat of arms."}]},
        {"lemma": "címer", "pos": "noun", "cefr": "B1", "translation": "coat of arms", "examples": [{"hungarian": "Minden corvina borítóján ott volt a királyi címer.", "english": "The royal coat of arms was on the cover of every corvina."}]},
        {"lemma": "könyvgyűjtemény", "pos": "noun", "cefr": "B1", "translation": "book collection", "examples": [{"hungarian": "Hatalmas könyvgyűjteményt hozott létre Budán.", "english": "He created an immense book collection in Buda."}]},
        {"lemma": "történetíró", "pos": "noun", "cefr": "B1", "translation": "chronicler / historian", "examples": [{"hungarian": "Antonio Bonfini volt a király történetírója.", "english": "Antonio Bonfini was the king's historian."}]},
        {"lemma": "második", "pos": "adj", "cefr": "B1", "translation": "second", "examples": [{"hungarian": "A vatikáni után a második legnagyobb gyűjtemény volt.", "english": "It was the second largest collection after the Vatican."}]},
        {"lemma": "világhírű", "pos": "adj", "cefr": "B1", "translation": "world-famous", "examples": [{"hungarian": "A könyvtár világhírűvé tette Mátyás udvarát.", "english": "The library made Matthias's court world-famous."}]}
    ]
})

write_json(GRAMMAR_DIR / "b1-matyas-03-gr.json", {
    "title": "Művészeti leírások és sorszámnevek (után a második)",
    "level": "B1",
    "rules": [
        {
            "id": "ordinal-rankings",
            "title": "Rankings with 'után a leg- / második'",
            "text": "*A Vatikán után a második legnagyobb könyvtár volt.* (It was the second largest library after the Vatican.)",
            "tip": "*Után* + definite article + ordinal (*második, harmadik*) + superlative (*legnagyobb*)."
        },
        {
            "id": "adjective-forming-i",
            "title": "Forming Adjectives from Names and Eras (-i)",
            "text": "*reneszánsz kori, itáliai, visegrádi, nápolyi*. Lowercase spelling applies to derived adjectives.",
            "tip": "Hungarian adjectives from proper nouns are written in lowercase."
        }
    ],
    "examples": [
        {"spanish": "A Bibliotheca Corviniana a Vatikán után a legnagyobb gyűjtemény volt.", "english": "The Bibliotheca Corviniana was the largest collection after the Vatican."},
        {"spanish": "Mátyás budai és visegrádi palotája reneszánsz remekmű volt.", "english": "Matthias's palace in Buda and Visegrád was a Renaissance masterpiece."},
        {"spanish": "A corvinák a magyar nemzeti örökség részei.", "english": "The corvinas are part of the Hungarian national heritage."}
    ]
})

write_json(EXERCISES_DIR / "b1-matyas-03-ex.json", {
    "exercises": [
        {"id": "b1-matyas-03.ex01", "type": "multiple-choice", "title": "Mátyás könyvtára", "instruction": "Hogy hívták Mátyás király híres könyvtárát?", "question": "Mi volt Mátyás budai könyvtárának a neve?", "options": ["Bibliotheca Corviniana", "Alexandriai Könyvtár", "Brit Nemzeti Könyvtár", "Vatikáni Archívum"], "correctIndex": 0, "explanation": "A Bibliotheca Corviniana volt Mátyás reneszánsz könyvgyűjteménye.", "teaches": ["corvina", "konyvgyujtemeny"]},
        {"id": "b1-matyas-03.ex02", "type": "fill-blank", "title": "Reneszánsz királyné", "instruction": "Egészítsd ki a mondatot!", "sentence": "Mátyás nápolyi felesége, Aragóniai ___ segítette a reneszánsz kultúra elterjedését.", "correctAnswer": "Beatrix", "options": ["Beatrix", "Gizella", "Erzsébet", "Mária"], "teaches": ["reneszansz", "humanizmus"]},
        {"id": "b1-matyas-03.ex03", "type": "sentence-builder", "title": "A hollós címer", "instruction": "Állítsd össze a mondatot!", "words": ["A", "holló", "a", "Hunyadi-család", "és", "a", "corvinák", "címere", "volt."], "correctSentence": "A holló a Hunyadi-család és a corvinák címere volt.", "english": "The raven was the coat of arms of the Hunyadi family and the corvinas.", "teaches": ["hollo", "cimer"]},
        {"id": "b1-matyas-03.ex04", "type": "multiple-choice", "title": "A könyvtár rangja", "instruction": "Hányadik legnagyobb volt a Corviniana Európában?", "question": "Mekkora volt a Corviniana gyűjteménye a korban?", "options": ["A vatikáni után a 2. legnagyobb Európában", "A legkisebb gyűjtemény", "Nem volt benne könyv", "A 100. helyen állt"], "correctIndex": 0, "explanation": "A Corviniana Európa második legnagyobb könyvtára volt a Vatikán után.", "teaches": ["masodik", "vilaghiru"]},
        {"id": "b1-matyas-03.ex05", "type": "fill-blank", "title": "Visegrádi szökőkút", "instruction": "Válaszd ki a megfelelő anyagot!", "sentence": "A visegrádi reneszánsz palotát vörös márvány ___ díszítette.", "correctAnswer": "szökőkút", "options": ["szökőkút", "autó", "vasút", "híd"], "teaches": ["szokokut", "fuggokert"]},
        {"id": "b1-matyas-03.ex06", "type": "sentence-builder", "title": "Kódexek másolása", "instruction": "Rendezd helyes sorrendbe a szavakat!", "words": ["A", "corvinák", "kézzel", "másolt", "díszes", "kódexek", "voltak."], "correctSentence": "A corvinák kézzel másolt díszes kódexek voltak.", "english": "The corvinas were hand-copied ornate codices.", "teaches": ["kodex", "corvina"]},
        {"id": "b1-matyas-03.ex07", "type": "multiple-choice", "title": "Udvari történetíró", "instruction": "Ki volt Mátyás olasz származású történetírója?", "question": "Hogy hívták a király történetíróját?", "options": ["Antonio Bonfini", "Julius Caesar", "Anonymus", "Kölcsey Ferenc"], "correctIndex": 0, "explanation": "Antonio Bonfini írta meg a magyarok történetét Mátyás megbízásából.", "teaches": ["tortenetiro", "humanizmus"]},
        {"id": "b1-matyas-03.ex08", "type": "fill-blank", "title": "Világhírű kincsek", "instruction": "Egészítsd ki a mondatot!", "sentence": "A corvinák a magyar nemzeti örökség féltett ___.", "correctAnswer": "kincsei", "options": ["kincsei", "fegyverei", "autói", "börtönei"], "teaches": ["vilaghiru", "corvina"]}
    ]
})

write_json(LESSONS_DIR / "b1-matyas-03.json", make_lesson(
    "lesson.b1.matyas-03",
    "A reneszánsz udvar és a Corviniana (The Renaissance Court & Library)",
    "Művészeti leírások és sorszámnevek (után a második)",
    [
        "In this third lesson, we explore the cultural zenith of King Matthias's court, the first Renaissance center outside Italy.",
        "You will learn about Queen Beatrice of Naples, Italian humanists (Bonfini, Galeotto Marzio), the red marble fountains of Visegrád, and the legendary *Bibliotheca Corviniana* (over 2,000 illuminated codices).",
        "We also practice ranking expressions (*a Vatikán után a második*) and derived adjectival forms."
    ],
    [
        "I can describe King Matthias's Renaissance court and the influence of Queen Beatrice.",
        "I can explain the significance of the *Bibliotheca Corviniana* and Corvina codices.",
        "I can identify the raven symbol (*holló*) in the Hunyadi coat of arms.",
        "I can construct cultural and artistic comparative rankings in Hungarian."
    ],
    "stories/world/b1/b1-matyas-03-reneszanszudvar.json",
    "vocabulary/b1/b1-matyas-03-voc.json",
    "grammar/b1/b1-matyas-03-gr.json",
    "exercises/b1/b1-matyas-03-ex.json",
    [f"b1-matyas-03.ex{i:02d}" for i in range(1, 9)]
))

# -----------------
# Lesson 4: "Meghalt Mátyás, oda az igazság"
# -----------------
write_json(STORIES_DIR / "b1-matyas-04-igazsagossag.json", make_story(
    "story.b1.matyas.04",
    "\"Meghalt Mátyás, oda az igazság\" – Mátyás, az igazságos király",
    "Matthias the Just in folk memory: the tales of the disguised king inspecting judges and helping the poor, his central judicial reform (Royal Personal Presence / Curia), and the famous proverb 'Meghalt Mátyás, oda az igazság'.",
    "Buda és az ország falvai",
    ["közmondások és mesemondó szerkezetek"],
    ["Igazságos Mátyás", "Álruhás király", "Közmondás", "Királyi bíróság"],
    [
        "A magyar néphagyományban és mondavilágban Hunyadi Mátyás az 'igazságos király' alakjává nemesült. Számtalan népmese és monda szól arról, hogyan járt a király álruhában a nép között, hogy saját szemével lássa az egyszerű emberek sorsát és leleplezze a kapzsi bírákat és földesurakat.",
        "A valóságban Mátyás szigorú jogi és közigazgatási reformokat hajtott végre: megerősítette a királyi bíróságokat (királyi személyes jelenlét bírósága), szakképzett jogászokat alkalmazott, és korlátozta a bárók önkényes bíráskodását.",
        "Mátyás törvényei szigorúan büntették a korrupciót és a hatalommal való visszaélést, védve a jobbágyokat és a polgárokat a földesúri elnyomástól.",
        "Amikor 1490-ben váratlanul elhunyt, az ország népe azonnal megérezte a védelmező erős kéz hiányát, és megszületett a híres magyar közmondás: 'Meghalt Mátyás király, oda az igazság!'",
        "Ez a mondás évszázadokon át a törvényes rend, az igazságos kormányzás és a népét védő uralkodó iránti vágy jelképévé vált."
    ],
    [
        {"lemma": "igazságos", "pos": "adj", "cefr": "B1", "gloss": "just / righteous"},
        {"lemma": "álruha", "pos": "noun", "cefr": "B1", "gloss": "disguise"},
        {"lemma": "közmondás", "pos": "noun", "cefr": "B1", "gloss": "proverb / saying"},
        {"lemma": "visszaélés", "pos": "noun", "cefr": "B1", "gloss": "abuse of power / malpractice"}
    ],
    [
        {
            "question": "Hogyan nevezi a magyar néphagyomány Mátyás királyt?",
            "options": ["Mátyás, az igazságos", "Mátyás, a rettegett", "Mátyás, a szomorú", "Mátyás, a gazdag"],
            "correctIndex": 0,
            "explanation": "A néphagyományban Mátyás az 'igazságos király' jelzőt kapta."
        },
        {
            "question": "Melyik híres magyar közmondás született Mátyás király halála után 1490-ben?",
            "options": ["'Meghalt Mátyás király, oda az igazság!'", "'Ki korán kel, aranyat lel'", "'Sok lúd disznót győz'", "'Jobb későn, mint soha'"],
            "correctIndex": 0,
            "explanation": "A 'Meghalt Mátyás, oda az igazság' a legismertebb történelmi közmondásunk."
        },
        {
            "question": "Hogyan vizsgálta a mondák szerint Mátyás a bírák és urak igazságosságát?",
            "options": ["Álruhát öltve járt a nép között titokban", "Leveleket írt Rómába", "Mindenkit börtönbe záratott", "Újsághirdetést adott fel"],
            "correctIndex": 0,
            "explanation": "A mondák szerint Mátyás álruhás vándorként vagy diákként járta az országot."
        }
    ]
))

write_json(VOCAB_DIR / "b1-matyas-04-voc.json", {
    "title": "Mátyás, az igazságos király és a jogrend",
    "words": [
        {"lemma": "igazságos", "pos": "adj", "cefr": "B1", "translation": "just / righteous", "examples": [{"hungarian": "Mátyás az igazságos királyként él a mesékben.", "english": "Matthias lives in tales as the just king."}]},
        {"lemma": "álruha", "pos": "noun", "cefr": "B1", "translation": "disguise", "examples": [{"hungarian": "Álruhában járta az országot a mondák szerint.", "english": "According to legends, he walked the country in disguise."}]},
        {"lemma": "közmondás", "pos": "noun", "cefr": "B1", "translation": "proverb", "examples": [{"hungarian": "A 'Meghalt Mátyás, oda az igazság' híres közmondás.", "english": "'Matthias died, justice is gone' is a famous proverb."}]},
        {"lemma": "visszaélés", "pos": "noun", "cefr": "B1", "translation": "abuse of power", "examples": [{"hungarian": "Szigorúan büntette a hatalommal való visszaélést.", "english": "He strictly punished abuse of power."}]},
        {"lemma": "leleplez", "pos": "verb", "cefr": "B1", "translation": "to expose / unmask", "examples": [{"hungarian": "Leleplezte a kapzsi bírót.", "english": "He unmasked the greedy judge."}]},
        {"lemma": "kapzsi", "pos": "adj", "cefr": "B1", "translation": "greedy", "examples": [{"hungarian": "A kapzsi földesúr igazságtalanul adóztatta a parasztokat.", "english": "The greedy landlord taxed the peasants unjustly."}]},
        {"lemma": "bíráskodás", "pos": "noun", "cefr": "B1", "translation": "administration of justice", "examples": [{"hungarian": "A királyi bíráskodás szakszerűvé vált.", "english": "Royal justice administration became professional."}]},
        {"lemma": "mondavilág", "pos": "noun", "cefr": "B1", "translation": "world of legends", "examples": [{"hungarian": "A magyar mondavilág gazdag Mátyás-történetekben.", "english": "Hungarian folklore is rich in Matthias stories."}]},
        {"lemma": "korrupció", "pos": "noun", "cefr": "B1", "translation": "corruption", "examples": [{"hungarian": "Harcolt a korrupció ellen az igazságszolgáltatásban.", "english": "He fought against corruption in the justice system."}]},
        {"lemma": "elnyomás", "pos": "noun", "cefr": "B1", "translation": "oppression", "examples": [{"hungarian": "Megvédte a szegényeket a bárói elnyomástól.", "english": "He protected the poor from baronial oppression."}]},
        {"lemma": "megérez", "pos": "verb", "cefr": "B1", "translation": "to sense / feel the loss", "examples": [{"hungarian": "A nép megérezte a jó király hiányát.", "english": "The people felt the loss of the good king."}]},
        {"lemma": "igazságérzet", "pos": "noun", "cefr": "B1", "translation": "sense of justice", "examples": [{"hungarian": "Erős igazságérzete vezette a reformokat.", "english": "His strong sense of justice guided the reforms."}]}
    ]
})

write_json(GRAMMAR_DIR / "b1-matyas-04-gr.json", {
    "title": "Közmondások és mesemondó szerkezetek (szól arról, hogyan)",
    "level": "B1",
    "rules": [
        {
            "id": "reporting-tales",
            "title": "Reporting Tales with 'szól arról, hogy...'",
            "text": "*A monda arról szól, hogyan járt a király álruhában.* (The legend tells about how the king walked in disguise.)",
            "tip": "Anticipatory pronoun *arról* matches the subclause."
        },
        {
            "id": "proverb-syntax",
            "title": "Elliptical Syntax in Proverbs (oda az igazság)",
            "text": "*Oda a/az...* expresses irreparable loss: *Oda az igazság!* (Justice is gone / lost!) *Oda a békesség.*",
            "tip": "Fixed historical idiom used in everyday Hungarian."
        }
    ],
    "examples": [
        {"spanish": "A népmese arról szól, hogyan leplezte le Mátyás a kapzsi bírót.", "english": "The folk tale tells about how Matthias exposed the greedy judge."},
        {"spanish": "Meghalt Mátyás, oda az igazság.", "english": "Matthias died, justice is gone."},
        {"spanish": "Mátyás király szigorúan büntette a korrupciót.", "english": "King Matthias strictly punished corruption."}
    ]
})

write_json(EXERCISES_DIR / "b1-matyas-04-ex.json", {
    "exercises": [
        {"id": "b1-matyas-04.ex01", "type": "multiple-choice", "title": "A híres közmondás", "instruction": "Melyik közmondás kapcsolódik Mátyás királyhoz?", "question": "Hogyan szól a híres közmondás Mátyás halála után?", "options": ["'Meghalt Mátyás király, oda az igazság!'", "'Néma gyereknek anyja sem érti a szavát'", "'Addig jár a korsó a kútra, míg el nem törik'", "'Aki mer, az nyer'"], "correctIndex": 0, "explanation": "A 'Meghalt Mátyás, oda az igazság' a legismertebb történelmi közmondás.", "teaches": ["kozmondas", "igazsagos"]},
        {"id": "b1-matyas-04.ex02", "type": "fill-blank", "title": "Álruhás király", "instruction": "Egészítsd ki a mondatot!", "sentence": "A mondák szerint Mátyás ___ járt a nép között a törvények ellenőrzésére.", "correctAnswer": "álruhában", "options": ["álruhában", "aranyhintón", "páncélban", "repülőn"], "teaches": ["alruha", "mondavilag"]},
        {"id": "b1-matyas-04.ex03", "type": "sentence-builder", "title": "Korrupció büntetése", "instruction": "Állítsd össze a mondatot!", "words": ["A", "király", "szigorúan", "büntette", "a", "hatalommal", "való", "visszaélést."], "correctSentence": "A király szigorúan büntette a hatalommal való visszaélést.", "english": "The king strictly punished abuse of power.", "teaches": ["visszaeles", "korrupció"]},
        {"id": "b1-matyas-04.ex04", "type": "multiple-choice", "title": "Mátyás jelzője", "instruction": "Hogyan tisztelte a nép Mátyást?", "question": "Milyen uralkodóként él Mátyás a mondákban?", "options": ["Mátyás, az igazságos", "Mátyás, a kegyetlen", "Mátyás, az idegen", "Mátyás, a lusta"], "correctIndex": 0, "explanation": "Mátyás az 'igazságos' jelzőt érdemelte ki a nép védelmével.", "teaches": ["igazsagos", "igazsagérzet"]},
        {"id": "b1-matyas-04.ex05", "type": "fill-blank", "title": "Mondák témája (szól arról)", "instruction": "Válaszd ki a megfelelő szót!", "sentence": "A mese arról ___, hogyan segített a király a szegény embernek.", "correctAnswer": "szól", "options": ["szól", "fut", "alszik", "főz"], "teaches": ["mondavilag"]},
        {"id": "b1-matyas-04.ex06", "type": "sentence-builder", "title": "Igazságos bíráskodás", "instruction": "Rendezd helyes sorrendbe a szavakat!", "words": ["Mátyás", "megvédte", "a", "jobbágyokat", "a", "bárók", "önkényétől."], "correctSentence": "Mátyás megvédte a jobbágyokat a bárók önkényétől.", "english": "Matthias protected the serfs from the barons' arbitrariness.", "teaches": ["elnyomas", "biraskodas"]},
        {"id": "b1-matyas-04.ex07", "type": "multiple-choice", "title": "Mátyás halálának éve", "instruction": "Melyik évben halt meg Mátyás király?", "question": "Mikor hunyt el Hunyadi Mátyás Bécsben?", "options": ["1490-ben", "1458-ban", "1526-ban", "1222-ben"], "correctIndex": 0, "explanation": "Mátyás király 1490. április 6-án hunyt el Bécsben.", "teaches": ["kozmondas", "megerez"]},
        {"id": "b1-matyas-04.ex08", "type": "fill-blank", "title": "Kapzsi bíró leleplezése", "instruction": "Egészítsd ki a mondatot!", "sentence": "Az álruhás király hamar ___ az igazságtalan bírót.", "correctAnswer": "leleplezte", "options": ["leleplezte", "megdicsérte", "jutalmazta", "meghívta"], "teaches": ["leleplez", "kapzsi"]}
    ]
})

write_json(LESSONS_DIR / "b1-matyas-04.json", make_lesson(
    "lesson.b1.matyas-04",
    "\"Meghalt Mátyás, oda az igazság\" (Matthias the Just in Folk Memory)",
    "Közmondások és mesemondó szerkezetek (szól arról, hogyan)",
    [
        "In this fourth lesson, we study the enduring folkloric and legal legacy of 'Matthias the Just' (*Igazságos Mátyás*).",
        "You will learn about the folk tales of the disguised king inspecting judges, his actual court reforms and anti-corruption measures, and the origin of the national proverb: *'Meghalt Mátyás király, oda az igazság!'* (King Matthias died, justice is gone).",
        "We also practice narrative frameworks with *szól arról, hogy* and proverbial structures."
    ],
    [
        "I can explain why King Matthias is honored as 'the Just' in folk tradition.",
        "I can quote and contextualize the proverb *'Meghalt Mátyás király, oda az igazság'*.",
        "I can describe his legal and judicial reforms protecting commoners.",
        "I can use folk narrative and reporting structures fluently in Hungarian."
    ],
    "stories/world/b1/b1-matyas-04-igazsagossag.json",
    "vocabulary/b1/b1-matyas-04-voc.json",
    "grammar/b1/b1-matyas-04-gr.json",
    "exercises/b1/b1-matyas-04-ex.json",
    [f"b1-matyas-04.ex{i:02d}" for i in range(1, 9)]
))

# -----------------
# Lesson 5: Mátyás hódításai és az aranykor vége (1490)
# -----------------
write_json(STORIES_DIR / "b1-matyas-05-orokseg.json", make_story(
    "story.b1.matyas.05",
    "Mátyás hódításai, Bécs bevétele (1485) és a virágkor lezárulása (1490)",
    "King Matthias's western foreign policy: capturing Vienna in 1485 and becoming Duke of Austria, his goal of the Holy Roman Imperial crown, his sudden death in Vienna in 1490 without a legitimate heir, and the end of the medieval golden age.",
    "Bécs (Hofburg) és Székesfehérvár",
    ["külpolitikai szakkifejezések és összetett zárómondatok"],
    ["Bécs bevétele 1485", "Habsburg-Mátyás háború", "1490", "Középkori aranykor vége"],
    [
        "Uralkodása második felében Mátyás külpolitikája a nyugati hódítások felé fordult. Felismerte, hogy az Oszmán Birodalom végleges legyőzéséhez a közép-európai erők – a Német-Római Birodalom – erőforrásaira van szükség.",
        "Hosszú háborúban legyőzte III. Frigyes Habsburg császárt, és 1485-ben a Fekete Sereg élén bevonult Bécsbe. Mátyás felvette az Ausztria hercege címet, és székhelyét átmenetileg Bécsbe helyezte át.",
        "A császári trón megszerzésére és a török elleni nagy európai szövetség megteremtésére irányuló nagyszabású terveit azonban váratlan halála kettétörte.",
        "1490. április 6-án, virágvasárnap után Mátyás király 47 évesen hirtelen elhunyt Bécsben. Törvényes örökös hiányában házasságon kívül született fiára, Corvin Jánosra próbálta hagyni a koronát, de a bárók gyenge kezű uralkodót akartak.",
        "Mátyás halálával lezárult a középkori Magyar Királyság aranykora. A Fekete Sereg feloszlott, a királyi hatalom meggyengült, megnyitva az utat a mohácsi katasztrófa (1526) felé."
    ],
    [
        {"lemma": "Bécs bevétele", "pos": "noun", "cefr": "B1", "gloss": "capture of Vienna (1485)"},
        {"lemma": "erőforrás", "pos": "noun", "cefr": "B1", "gloss": "resource / power base"},
        {"lemma": "kettétör", "pos": "verb", "cefr": "B1", "gloss": "to shatter / break in two (plans)"},
        {"lemma": "aranykor", "pos": "noun", "cefr": "B1", "gloss": "golden age"}
    ],
    [
        {
            "question": "Melyik híres nyugati fővárost foglalta el Mátyás király 1485-ben?",
            "options": ["Bécset (ahol Ausztria hercegévé vált)", "Párizst", "Londont", "Rómát"],
            "correctIndex": 0,
            "explanation": "Mátyás 1485-ben elfoglalta Bécset és felvette Ausztria hercegének címét."
        },
        {
            "question": "Mikor halt meg Mátyás király Bécsben?",
            "options": ["1490-ben", "1526-ban", "1458-ban", "1241-ben"],
            "correctIndex": 0,
            "explanation": "Mátyás király 1490. április 6-án hunyt el Bécsben."
        },
        {
            "question": "Mi történt a Magyar Királysággal Mátyás 1490-es halála után?",
            "options": ["A királyi hatalom meggyengült, a Fekete Sereg feloszlott, és véget ért az aranykor", "Az ország azonnal meghódította egész Ázsiát", "A törökök békét kötöttek ezer évre", "A királyság örökre császársággá vált"],
            "correctIndex": 0,
            "explanation": "Mátyás halála után a központi hatalom meggyengült, előkészítve a későbbi mohácsi válságot."
        }
    ]
))

write_json(VOCAB_DIR / "b1-matyas-05-voc.json", {
    "title": "Mátyás hódításai és az aranykor lezárulása (1490)",
    "words": [
        {"lemma": "Bécs bevétele", "pos": "noun", "cefr": "B1", "translation": "capture of Vienna", "examples": [{"hungarian": "Bécs bevétele 1485-ben Mátyás legnagyobb hadi sikere volt.", "english": "The capture of Vienna in 1485 was Matthias's greatest military success."}]},
        {"lemma": "erőforrás", "pos": "noun", "cefr": "B1", "translation": "resource", "examples": [{"hungarian": "Nagyobb erőforrásokra volt szükség a török ellen.", "english": "Greater resources were needed against the Turks."}]},
        {"lemma": "kettétör", "pos": "verb", "cefr": "B1", "translation": "to shatter / cut short", "examples": [{"hungarian": "A hirtelen halál kettétörte a nagy terveket.", "english": "Sudden death cut short the grand plans."}]},
        {"lemma": "aranykor", "pos": "noun", "cefr": "B1", "translation": "golden age", "examples": [{"hungarian": "Mátyás uralkodása volt a középkori magyar aranykor.", "english": "Matthias's reign was the medieval Hungarian golden age."}]},
        {"lemma": "hódítás", "pos": "noun", "cefr": "B1", "translation": "conquest", "examples": [{"hungarian": "A nyugati hódítások kiterjesztették a határokat.", "english": "The western conquests expanded the borders."}]},
        {"lemma": "törvényes örökös", "pos": "noun", "cefr": "B1", "translation": "legitimate heir", "examples": [{"hungarian": "Nem volt törvényes örökös a trónra.", "english": "There was no legitimate heir to the throne."}]},
        {"lemma": "feloszlik", "pos": "verb", "cefr": "B1", "translation": "to disband / dissolve", "examples": [{"hungarian": "A Fekete Sereg pénz hiányában feloszlott.", "english": "The Black Army disbanded due to lack of money."}]},
        {"lemma": "meggyengül", "pos": "verb", "cefr": "B1", "translation": "to weaken", "examples": [{"hungarian": "A központi királyi hatalom gyorsan meggyengült.", "english": "Central royal power weakened rapidly."}]},
        {"lemma": "külpolitika", "pos": "noun", "cefr": "B1", "translation": "foreign policy", "examples": [{"hungarian": "Mátyás külpolitikája a császári címre törekedett.", "english": "Matthias's foreign policy aimed at the imperial title."}]},
        {"lemma": "herceg", "pos": "noun", "cefr": "B1", "translation": "duke / prince", "examples": [{"hungarian": "Felvette az Ausztria hercege címet.", "english": "He took the title of Duke of Austria."}]},
        {"lemma": "lezárul", "pos": "verb", "cefr": "B1", "translation": "to come to a close", "examples": [{"hungarian": "1490-ben lezárult a virágzó korszak.", "english": "In 1490, the flourishing era came to a close."}]},
        {"lemma": "nagyszabású", "pos": "adj", "cefr": "B1", "translation": "grand / ambitious", "examples": [{"hungarian": "Nagyszabású európai tervei voltak.", "english": "He had grand European plans."}]}
    ]
})

write_json(GRAMMAR_DIR / "b1-matyas-05-gr.json", {
    "title": "Külpolitikai és korszakzáró összetett szerkezetek (hiányában, megnyitva az utat)",
    "level": "B1",
    "rules": [
        {
            "id": "postposition-hianyaban",
            "title": "Postposition 'hiányában' (In the absence / lack of)",
            "text": "*Törvényes örökös hiányában trónviszály tört ki.* (In the absence of a legitimate heir, a succession dispute broke out.)",
            "tip": "Requires nouns in possessive form."
        },
        {
            "id": "participial-clause-open",
            "title": "Participle 'megnyitva az utat' (Opening the way)",
            "text": "*A központi hatalom meggyengült, megnyitva az utat a válság felé.* (Central power weakened, opening the path toward crisis.)",
            "tip": "Adverbial participle *-va / -ve* provides transition to subsequent epochs."
        }
    ],
    "examples": [
        {"spanish": "Mátyás 1485-ben elfoglalta Bécset.", "english": "Matthias captured Vienna in 1485."},
        {"spanish": "Törvényes örökös hiányában meggyengült a királyság.", "english": "In the absence of a legitimate heir, the kingdom weakened."},
        {"spanish": "Mátyás halálával lezárult a középkori magyar aranykor.", "english": "With Matthias's death, the medieval Hungarian golden age came to a close."}
    ]
})

write_json(EXERCISES_DIR / "b1-matyas-05-ex.json", {
    "exercises": [
        {"id": "b1-matyas-05.ex01", "type": "multiple-choice", "title": "Bécs bevétele", "instruction": "Melyik évben foglalta el Mátyás Bécset?", "question": "Mikor vonult be Mátyás király Bécsbe?", "options": ["1485-ben", "1458-ban", "1526-ban", "1241-ben"], "correctIndex": 0, "explanation": "Mátyás 1485-ben foglalta el Bécset.", "teaches": ["Becs-bevetele", "hoditas"]},
        {"id": "b1-matyas-05.ex02", "type": "fill-blank", "title": "Mátyás halálának éve", "instruction": "Egészítsd ki a mondatot!", "sentence": "Hunyadi Mátyás király ___ áprilisában hunyt el Bécsben.", "correctAnswer": "1490", "options": ["1490", "1526", "1848", "1000"], "teaches": ["aranykor", "lezarul"]},
        {"id": "b1-matyas-05.ex03", "type": "sentence-builder", "title": "Ausztria hercege", "instruction": "Állítsd össze a mondatot!", "words": ["Mátyás", "1485-ben", "felvette", "az", "Ausztria", "hercege", "címet."], "correctSentence": "Mátyás 1485-ben felvette az Ausztria hercege címet.", "english": "Matthias took the title of Duke of Austria in 1485.", "teaches": ["herceg", "Becs-bevetele"]},
        {"id": "b1-matyas-05.ex04", "type": "multiple-choice", "title": "Törvényes örökös", "instruction": "Kire próbálta hagyni Mátyás a trónt?", "question": "Ki volt Mátyás király fia?", "options": ["Corvin János", "Kinizsi Pál", "Vitéz János", "Bakócz Tamás"], "correctIndex": 0, "explanation": "Mátyás fiára, Corvin Jánosra akarta hagyni a koronát.", "teaches": ["torvenyes-orokos"]},
        {"id": "b1-matyas-05.ex05", "type": "fill-blank", "title": "Hiányában (hiányában)", "instruction": "Válaszd ki a megfelelő névutót!", "sentence": "Törvényes örökös ___ a bárók gyenge királyt választottak.", "correctAnswer": "hiányában", "options": ["hiányában", "után", "miatt", "nélkül"], "teaches": ["torvenyes-orokos"]},
        {"id": "b1-matyas-05.ex06", "type": "sentence-builder", "title": "A Fekete Sereg sorsa", "instruction": "Rendezd helyes sorrendbe a szavakat!", "words": ["Mátyás", "halála", "után", "a", "Fekete", "Sereg", "feloszlott."], "correctSentence": "Mátyás halála után a Fekete Sereg feloszlott.", "english": "After Matthias's death, the Black Army disbanded.", "teaches": ["feloszlik", "meggyengul"]},
        {"id": "b1-matyas-05.ex07", "type": "multiple-choice", "title": "Az aranykor vége", "instruction": "Mit jelentett 1490 a magyar történelemben?", "question": "Hogyan értékeli a történettudomány 1490-et?", "options": ["A virágzó középkori magyar aranykor lezárulását", "A törökök végleges kiűzését", "A vasútvonalak megnyitását", "A köztársaság megalakulását"], "correctIndex": 0, "explanation": "Mátyás 1490-es halála a középkori magyar nagyhatalom és aranykor végét jelentette.", "teaches": ["aranykor", "lezarul"]},
        {"id": "b1-matyas-05.ex08", "type": "fill-blank", "title": "Kettétört tervek", "instruction": "Egészítsd ki a mondatot!", "sentence": "A király váratlan halála ___ a nagy európai terveket.", "correctAnswer": "kettétörte", "options": ["kettétörte", "megvalósította", "segítette", "megnyitotta"], "teaches": ["kettetor", "nagyszabasu"]}
    ]
})

write_json(LESSONS_DIR / "b1-matyas-05.json", make_lesson(
    "lesson.b1.matyas-05",
    "Mátyás hódításai és az aranykor vége (Conquests & End of Golden Age - 1490)",
    "Külpolitikai és korszakzáró összetett szerkezetek (hiányában, megnyitva az utat)",
    [
        "In this fifth lesson, we examine King Matthias's western conquests, his capture of Vienna in 1485, his sudden death in 1490, and the close of the medieval golden age.",
        "You will learn about his strategy to acquire the Imperial crown to counter the Ottoman threat, the succession crisis with Corvin János, the disbanding of the Black Army, and the path leading toward the 1526 crisis.",
        "We also practice postpositions of absence (*hiányában*) and epoch-closing participial transitions."
    ],
    [
        "I can describe Matthias's capture of Vienna (1485) and his foreign policy.",
        "I can state the date (1490) and historical consequence of King Matthias's death.",
        "I can explain the disbanding of the Black Army and the weakening of royal power.",
        "I can construct complex historical sentences describing the end of an era."
    ],
    "stories/world/b1/b1-matyas-05-orokseg.json",
    "vocabulary/b1/b1-matyas-05-voc.json",
    "grammar/b1/b1-matyas-05-gr.json",
    "exercises/b1/b1-matyas-05-ex.json",
    [f"b1-matyas-05.ex{i:02d}" for i in range(1, 9)]
))

# -----------------
# Unit 8 Consolidation
# -----------------
write_json(STORIES_DIR / "b1-matyas.json", make_story(
    "story.b1.matyas",
    "Hunyadi Mátyás és a reneszánsz aranykor (1458–1490)",
    "A grand synthesis of King Matthias Corvinus's reign: his election on the ice of the Danube (1458), the Black Army and Kinizsi Pál, the Renaissance court and Bibliotheca Corviniana, the lore of the Just King ('Meghalt Mátyás, oda az igazság'), and the capture of Vienna (1485).",
    "Kárpát-medence és Bécs",
    ["összetett mondatszerkezetek", "történeti szintézis"],
    ["Hunyadi Mátyás", "Fekete Sereg", "Bibliotheca Corviniana", "Igazságos Mátyás", "Bécs 1485"],
    [
        "1458 januárjában a Duna jegén a nép lelkesen királlyá kiáltotta ki a nándorfehérvári hős fiát, a 15 éves Hunyadi Mátyást. Uralkodása a középkori Magyar Királyság legfényesebb aranykorát hozta el.",
        "Mátyás korszerű zsoldoshadsereget (Fekete Sereg) hozott létre Kinizsi Pál vezetésével, és szilárd adórendszert (füstpénz, rendkívüli hadiadó) vezetett be, amely évi egymillió aranyforintra növelte a királyi kincstár jövedelmét.",
        "Beatrix királynéval együtt Budát és Visegrádot Európa legelső Itálián kívüli reneszánsz központjává emelte. Világhírű könyvtára, a Bibliotheca Corviniana több mint kétezer kódexével a kor második legnagyobb gyűjteménye volt.",
        "Szigorú és igazságos bíráskodásával kivívta az 'Igazságos Mátyás' nevet, amelyről a híres mondás emlékezik: 'Meghalt Mátyás király, oda az igazság!'.",
        "1485-ben bevonult Bécsbe és felvette Ausztria hercegének címét, mielőtt 1490-ben bekövetkezett váratlan halálával lezárult volna a virágzó középkori magyar birodalom korszaka."
    ],
    [
        {"lemma": "Hunyadi Mátyás", "pos": "noun", "cefr": "B1", "gloss": "King Matthias Corvinus"},
        {"lemma": "Fekete Sereg", "pos": "noun", "cefr": "B1", "gloss": "Black Army"},
        {"lemma": "Bibliotheca Corviniana", "pos": "noun", "cefr": "B1", "gloss": "Corvina Library"},
        {"lemma": "Igazságos Mátyás", "pos": "noun", "cefr": "B1", "gloss": "Matthias the Just"}
    ],
    [
        {"question": "Melyik évszámok határolják Hunyadi Mátyás uralkodását?", "options": ["1458–1490", "1000–1038", "1308–1342", "1526–1541"], "correctIndex": 0, "explanation": "Mátyás király 1458-tól 1490-ig uralkodott."},
        {"question": "Mi jellemezte Mátyás hadseregét és kultúráját?", "options": ["A Fekete Sereg zsoldoshadsereg és a Bibliotheca Corviniana reneszánsz kincsei", "A hadsereg teljes hiánya", "Csak primitív fatemplomok", "Külföldi rabszolgaság"], "correctIndex": 0, "explanation": "Mátyás a Fekete Seregre és a páratlan reneszánsz udvarra támaszkodott."},
        {"question": "Melyik fővárost foglalta el Mátyás 1485-ben?", "options": ["Bécset", "Párizst", "Madridot", "Rómát"], "correctIndex": 0, "explanation": "Mátyás 1485-ben bevette Bécset és Ausztria hercege lett."}
    ]
))

u8_cons_ex = []
u8_cons_ex.append({"id": "b1-matyas-consolidation.ex01", "type": "multiple-choice", "title": "Mátyás megválasztása", "instruction": "Melyik évben választották Mátyást királlyá a Duna jegén?", "question": "Mikor kezdődött Mátyás uralkodása?", "options": ["1458-ban", "1000-ben", "1222-ben", "1526-ban"], "correctIndex": 0, "explanation": "Mátyást 1458-ban választották meg.", "teaches": ["kiralyvalasztas"]})
u8_cons_ex.append({"id": "b1-matyas-consolidation.ex02", "type": "fill-blank", "title": "Fekete Sereg", "instruction": "Egészítsd ki a mondatot!", "sentence": "Mátyás állandó zsoldoshadseregét ___ Seregnek nevezték.", "correctAnswer": "Fekete", "options": ["Fekete", "Fehér", "Piros", "Kék"], "teaches": ["Fekete-Sereg"]})
u8_cons_ex.append({"id": "b1-matyas-consolidation.ex03", "type": "sentence-builder", "title": "Bibliotheca Corviniana", "instruction": "Állítsd össze a mondatot!", "words": ["A", "Bibliotheca", "Corviniana", "Mátyás", "világhírű", "reneszánsz", "könyvtára", "volt."], "correctSentence": "A Bibliotheca Corviniana Mátyás világhírű reneszánsz könyvtára volt.", "english": "The Bibliotheca Corviniana was Matthias's world-famous Renaissance library.", "teaches": ["corvina", "reneszansz"]})
u8_cons_ex.append({"id": "b1-matyas-consolidation.ex04", "type": "multiple-choice", "title": "Kinizsi Pál", "instruction": "Ki volt Mátyás leghíresebb hadvezére?", "question": "Melyik hős győzött 1479-ben Kenyérmezőnél?", "options": ["Kinizsi Pál", "Dugovics Titusz", "Dobó István", "Zrínyi Miklós"], "correctIndex": 0, "explanation": "Kinizsi Pál volt a Fekete Sereg veretlen hadvezére.", "teaches": ["hadvezer"]})
u8_cons_ex.append({"id": "b1-matyas-consolidation.ex05", "type": "fill-blank", "title": "Bécs bevétele", "instruction": "Egészítsd ki a mondatot!", "sentence": "Mátyás király ___ foglalta el Bécset.", "correctAnswer": "1485-ben", "options": ["1485-ben", "1241-ben", "1526-ban", "1848-ban"], "teaches": ["Becs-bevetele"]})
u8_cons_ex.append({"id": "b1-matyas-consolidation.ex06", "type": "sentence-builder", "title": "Híres közmondás", "instruction": "Rendezd helyes sorrendbe a szavakat!", "words": ["Meghalt", "Mátyás", "király,", "oda", "az", "igazság."], "correctSentence": "Meghalt Mátyás király, oda az igazság.", "english": "King Matthias died, justice is gone.", "teaches": ["kozmondas", "igazsagos"]})
u8_cons_ex.append({"id": "b1-matyas-consolidation.ex07", "type": "multiple-choice", "title": "Füstpénz adó", "instruction": "Milyen adót vezetett be Mátyás a kapuadó helyett?", "question": "Hogyan szedte be Mátyás az adót?", "options": ["Füstpénzként (háztartásonként és kéményenként)", "Csak a nemesektől", "Kizárólag hajóvámként", "Nem vetett ki adót"], "correctIndex": 0, "explanation": "A füstpénz megszüntette a kapuadó kikerülésének lehetőségét.", "teaches": ["fustpenz"]})
u8_cons_ex.append({"id": "b1-matyas-consolidation.ex08", "type": "fill-blank", "title": "Mátyás felesége", "instruction": "Válaszd ki a királyné nevét!", "sentence": "Aragóniai ___ királyné hozta el a nápolyi reneszánszt Budára.", "correctAnswer": "Beatrix", "options": ["Beatrix", "Gizella", "Erzsébet", "Mária"], "teaches": ["reneszansz"]})
u8_cons_ex.append({"id": "b1-matyas-consolidation.ex09", "type": "sentence-builder", "title": "Visegrádi palota", "instruction": "Állítsd össze a mondatot!", "words": ["A", "visegrádi", "palotát", "márvány", "szökőkutak", "díszítették."], "correctSentence": "A visegrádi palotát márvány szökőkutak díszítették.", "english": "Marble fountains decorated the palace of Visegrád.", "teaches": ["szokokut"]})
u8_cons_ex.append({"id": "b1-matyas-consolidation.ex10", "type": "multiple-choice", "title": "Mátyás halála", "instruction": "Melyik évben hunyt el Mátyás Bécsben?", "question": "Mikor ért véget Mátyás király uralkodása?", "options": ["1490-ben", "1458-ban", "1526-ban", "1222-ben"], "correctIndex": 0, "explanation": "Mátyás 1490-ben hunyt el Bécsben.", "teaches": ["aranykor", "lezarul"]})
u8_cons_ex.append({"id": "b1-matyas-consolidation.ex11", "type": "fill-blank", "title": "Címerállat", "instruction": "Egészítsd ki a mondatot!", "sentence": "A gyűrűt tartó ___ volt a Hunyadiak címermadara.", "correctAnswer": "holló", "options": ["holló", "sas", "galamb", "veréb"], "teaches": ["hollo", "cimer"]})
u8_cons_ex.append({"id": "b1-matyas-consolidation.ex12", "type": "sentence-builder", "title": "Álruhás királyjárás", "instruction": "Rendezd helyes sorrendbe a szavakat!", "words": ["Mátyás", "álruhában", "vizsgálta", "a", "bírák", "igazságosságát."], "correctSentence": "Mátyás álruhában vizsgálta a bírák igazságosságát.", "english": "Matthias inspected the justice of judges in disguise.", "teaches": ["alruha", "igazsagos"]})
u8_cons_ex.append({"id": "b1-matyas-consolidation.ex13", "type": "multiple-choice", "title": "Rendkívüli hadiadó", "instruction": "Mekkora volt a rendkívüli hadiadó összege?", "question": "Mennyit fizetett egy jobbágy rendkívüli hadiadóként?", "options": ["Évi egy aranyforintot", "Száz aranyat", "Egy garast", "Semmit"], "correctIndex": 0, "explanation": "A rendkívüli hadiadó évi 1 aranyforint volt jobbágytelkenként.", "teaches": ["rendkivuli-hadiado"]})
u8_cons_ex.append({"id": "b1-matyas-consolidation.ex14", "type": "fill-blank", "title": "Humanista tudósok", "instruction": "Egészítsd ki a mondatot!", "sentence": "Antonio ___ Mátyás udvari történetírója volt.", "correctAnswer": "Bonfini", "options": ["Bonfini", "Petőfi", "Kossuth", "Kölcsey"], "teaches": ["tortenetiro", "humanizmus"]})
u8_cons_ex.append({"id": "b1-matyas-consolidation.ex15", "type": "sentence-builder", "title": "Ausztria hercege cím", "instruction": "Állítsd össze a mondatot!", "words": ["Bécs", "bevétele", "után", "Mátyás", "Ausztria", "hercege", "lett."], "correctSentence": "Bécs bevétele után Mátyás Ausztria hercege lett.", "english": "After the capture of Vienna, Matthias became Duke of Austria.", "teaches": ["Becs-bevetele", "herceg"]})
u8_cons_ex.append({"id": "b1-matyas-consolidation.ex16", "type": "multiple-choice", "title": "Mátyás fia", "instruction": "Kire akarta hagyni Mátyás a trónt?", "question": "Hogy hívták Mátyás fiát?", "options": ["Corvin János", "Kinizsi Pál", "Szilágyi Mihály", "Vitéz János"], "correctIndex": 0, "explanation": "Corvin János volt Mátyás fia.", "teaches": ["torvenyes-orokos"]})
u8_cons_ex.append({"id": "b1-matyas-consolidation.ex17", "type": "fill-blank", "title": "Kenyérmezei hős", "instruction": "Egészítsd ki a mondatot!", "sentence": "1479-ben Kinizsi Pál legyőzte a törököket ___.", "correctAnswer": "Kenyérmezőnél", "options": ["Kenyérmezőnél", "Mohácsnál", "Budán", "Bécsben"], "teaches": ["hadvezer"]})
u8_cons_ex.append({"id": "b1-matyas-consolidation.ex18", "type": "sentence-builder", "title": "Aranykor lezárulása", "instruction": "Rendezd helyes sorrendbe a szavakat!", "words": ["1490-ben", "lezárult", "a", "középkori", "magyar", "aranykor."], "correctSentence": "1490-ben lezárult a középkori magyar aranykor.", "english": "In 1490, the medieval Hungarian golden age came to a close.", "teaches": ["aranykor", "lezarul"]})
u8_cons_ex.append({"id": "b1-matyas-consolidation.ex19", "type": "multiple-choice", "title": "Hadsereg feloszlása", "instruction": "Mi történt a Fekete Sereggel 1490 után?", "question": "Miért oszlott fel a zsoldoshadsereg Mátyás halála után?", "options": ["Pénz és erős királyi akarat hiányában feloszlott", "Elhajóztak Amerikába", "Csatlakoztak a törökökhöz", "Megvédték az országot 1526-ban"], "correctIndex": 0, "explanation": "A bárók nem fizették a zsoldot, így a Fekete Sereg feloszlott.", "teaches": ["feloszlik", "meggyengul"]})
u8_cons_ex.append({"id": "b1-matyas-consolidation.ex20", "type": "fill-blank", "title": "Királyválasztás a jégen", "instruction": "Egészítsd ki a mondatot!", "sentence": "Mátyást mindössze 15 ___ korában választották királlyá.", "correctAnswer": "éves", "options": ["éves", "napos", "hónapos", "perces"], "teaches": ["kiralyvalasztas"]})

write_json(EXERCISES_DIR / "b1-matyas-consolidation-ex.json", {"exercises": u8_cons_ex})

write_json(LESSONS_DIR / "b1-matyas-consolidation.json", make_consolidation_lesson(
    "lesson.b1.matyas-consolidation",
    "Matthias Corvinus & the Renaissance Court (1458–1490) - Consolidation",
    [
        "Congratulations on completing Unit 8 of the Hungarian Citizenship Track!",
        "In this unit, you have mastered the golden era of King Matthias Corvinus (*Hunyadi Mátyás*, 1458–1490): his election at age 15 on the frozen Danube (1458), the mercenary Black Army (*Fekete Sereg*) and general Pál Kinizsi, the Renaissance court and *Bibliotheca Corviniana*, the lore of Matthias the Just (*'Meghalt Mátyás, oda az igazság'*), the capture of Vienna (1485), and the close of the golden age in 1490.",
        "Review your vocabulary and test your mastery across all 20 consolidation exercises."
    ],
    [
        "I can summarize the reign of King Matthias Corvinus (1458–1490) and his election on the Danube.",
        "I can describe the Black Army (*Fekete Sereg*), Kinizsi Pál, and taxation reforms (*füstpénz, hadiadó*).",
        "I can explain the cultural radiance of the *Bibliotheca Corviniana* and Renaissance Buda and Visegrád.",
        "I can analyze the proverb *'Meghalt Mátyás király, oda az igazság'* and the historical shift after 1490."
    ],
    "stories/world/b1/b1-matyas.json",
    "exercises/b1/b1-matyas-consolidation-ex.json",
    [f"b1-matyas-consolidation.ex{i:02d}" for i in range(1, 21)]
))

print("Unit 8 (b1-matyas) complete!")
