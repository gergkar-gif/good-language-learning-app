# -*- coding: utf-8 -*-
"""
Unit 3 Overhaul: The Honfoglalás (895) (b1-honfoglalas)
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
# Lesson 1: Nyugatra nyomás (Vándorlás és őshaza)
# -----------------
write_json(STORIES_DIR / "b1-honfoglalas-01-nyugatranyomas.json", make_story(
    "story.b1.honfoglalas.01",
    "A vándorlás útja: Magna Hungariától Etelközig",
    "The eastern origins and westward migration of the Magyar tribes: the Uralic homeland, Magna Hungaria, Levédia, and Etelköz between the rivers.",
    "Kelet-európai sztyeppe",
    ["időhatározói mellékmondatok: miután, mielőtt"],
    ["Magyar őstörténet", "Sztyeppei vándorlás"],
    [
        "A magyar nép ősei a finnugor nyelvcsaládhoz tartoztak, és az Urál hegység keleti oldalán éltek. A klímaváltozás és a nomád népek mozgása miatt fokozatosan nyugat felé vándoroltak.",
        "A vándorlás során a törzsek előbb Magna Hungariában, az Urál és a Volga vidékén éltek, ahol földműveléssel és állattenyésztéssel foglalkoztak, majd délnyugatabbra, Levédiába vonultak.",
        "Levédiában a magyarok szoros kapcsolatba kerültek a Kazár Birodalommal. Itt sajátították el a kettős fejedelemség rendszerét (a kende és a gyula intézményét), valamint a türk kultúra számos elemét.",
        "A 9. század második felében a hét törzs Etelközbe, a Dnyeper és a Duna közötti folyóközi síkságra költözött. Itt a nomád lovas társadalom megerősödött és felkészült az új haza keresésére.",
        "Mielőtt a Kárpátokon átkeltek volna, a törzsfők szövetséget kötöttek, amely biztosította az egységes vezetést a történelmi honfoglalás során."
    ],
    [
        {"lemma": "őshaza", "pos": "noun", "cefr": "B1", "gloss": "ancient homeland / ancestral home"},
        {"lemma": "vándorlás", "pos": "noun", "cefr": "B1", "gloss": "migration"},
        {"lemma": "szövetség", "pos": "noun", "cefr": "B1", "gloss": "alliance / confederation"},
        {"lemma": "kettős fejedelemség", "pos": "noun", "cefr": "B1", "gloss": "dual principality (sacred & military)"}
    ],
    [
        {
            "question": "Melyik nyelvcsaládhoz tartoznak a magyarok az őstörténet alapján?",
            "options": ["A finnugor (uráli) nyelvcsaládhoz", "A germán nyelvcsaládhoz", "A szláv nyelvcsaládhoz", "A latin nyelvcsaládhoz"],
            "correctIndex": 0,
            "explanation": "A magyar nyelv a finnugor (uráli) nyelvcsalád tagja."
        },
        {
            "question": "Mely területeken éltek a magyar törzsek a honfoglalás előtt?",
            "options": ["Magna Hungariában, Levédiában és Etelközben", "Csak Spanyolországban", "Kizárólag a Skandináv-félszigeten", "Az észak-amerikai prériken"],
            "correctIndex": 0,
            "explanation": "A vándorlás fő állomásai Magna Hungaria, Levédia és Etelköz voltak."
        },
        {
            "question": "Mit jelentett a kettős fejedelemség intézménye?",
            "options": ["A kende volt a szakrális főfejedelem, a gyula pedig a katonai vezér", "Két király uralkodott egyszerre két különböző földrészen", "Egy elnök és egy polgármester vezette a falut", "Minden évben sorsolással választottak új vezetőt"],
            "correctIndex": 0,
            "explanation": "A kettős fejedelemségben a kende a szakrális méltóságot, a gyula a tényleges katonai hatalmat képviselte."
        }
    ]
))

write_json(VOCAB_DIR / "b1-honfoglalas-01-voc.json", {
    "title": "A vándorlás útja és az őshaza",
    "words": [
        {"lemma": "őshaza", "pos": "noun", "cefr": "B1", "translation": "ancient homeland", "examples": [{"hungarian": "A kutatók az Urál vidékén keresik a magyar őshazát.", "english": "Researchers look for the Hungarian ancient homeland in the Ural region."}]},
        {"lemma": "vándorlás", "pos": "noun", "cefr": "B1", "translation": "migration", "examples": [{"hungarian": "A törzsek hosszú vándorlás után érkeztek a sztyeppére.", "english": "The tribes arrived on the steppe after a long migration."}]},
        {"lemma": "szövetség", "pos": "noun", "cefr": "B1", "translation": "alliance", "examples": [{"hungarian": "A hét vezér szilárd szövetséget kötött.", "english": "The seven chieftains concluded a solid alliance."}]},
        {"lemma": "fejedelemség", "pos": "noun", "cefr": "B1", "translation": "principality", "examples": [{"hungarian": "A kettős fejedelemség biztosította a rendet.", "english": "The dual principality ensured order."}]},
        {"lemma": "sztyeppe", "pos": "noun", "cefr": "B1", "translation": "steppe", "examples": [{"hungarian": "A végtelen sztyeppén lovagoltak a harcosok.", "english": "The warriors rode across the endless steppe."}]},
        {"lemma": "lovas", "pos": "adj", "cefr": "B1", "translation": "equestrian / mounted", "examples": [{"hungarian": "A lovas nomád kultúra határozta meg az életmódot.", "english": "Mounted nomadic culture defined the way of life."}]},
        {"lemma": "nyelvcsalád", "pos": "noun", "cefr": "B1", "translation": "language family", "examples": [{"hungarian": "A magyar a finnugor nyelvcsaládba tartozik.", "english": "Hungarian belongs to the Finno-Ugric language family."}]},
        {"lemma": "elsajátít", "pos": "verb", "cefr": "B1", "translation": "to master / acquire", "examples": [{"hungarian": "Új haditechnikát sajátítottak el a szomszédos népektől.", "english": "They acquired new military techniques from neighbouring peoples."}]},
        {"lemma": "törzsfő", "pos": "noun", "cefr": "B1", "translation": "tribal chieftain", "examples": [{"hungarian": "A törzsfők közösen hozták meg a fontos döntéseket.", "english": "The tribal chieftains made important decisions together."}]},
        {"lemma": "érkezés", "pos": "noun", "cefr": "B1", "translation": "arrival", "examples": [{"hungarian": "A magyarok érkezése új korszakot nyitott Európában.", "english": "The arrival of the Magyars opened a new era in Europe."}]},
        {"lemma": "kötelék", "pos": "noun", "cefr": "B1", "translation": "bond / tie", "examples": [{"hungarian": "A vérszerződés szent köteléket jelentett.", "english": "The blood oath meant a sacred bond."}]},
        {"lemma": "fokozatosan", "pos": "adv", "cefr": "B1", "translation": "gradually", "examples": [{"hungarian": "A törzsek fokozatosan haladtak nyugat felé.", "english": "The tribes moved gradually towards the west."}]}
    ]
})

write_json(GRAMMAR_DIR / "b1-honfoglalas-01-miutan-mielott-gr.json", {
    "title": "Időhatározói mellékmondatok: miután és mielőtt",
    "level": "B1",
    "rules": [
        {
            "id": "miutan-clause",
            "title": "Subordinate Clauses with 'miután' (After)",
            "text": "*Miután* expresses an action that occurred before the main clause: *Miután a törzsek elhagyták Levédiát, Etelközbe költöztek.* (After the tribes left Levédia, they moved to Etelköz.) Both verbs are usually in the past tense.",
            "tip": "Always put a comma between the subordinate and main clauses."
        },
        {
            "id": "mielott-conditional",
            "title": "Clauses with 'mielőtt' (Before)",
            "text": "*Mielőtt* introduces an event that happened later than the main action. In Hungarian, *mielőtt* is often followed by conditional or indicative past: *Mielőtt átkeltek volna a Kárpátokon, szövetséget kötöttek.* (Before they crossed the Carpathians, they formed an alliance.)",
            "tip": "The conditional form (*volna*) emphasizes anticipation."
        }
    ],
    "examples": [
        {"spanish": "Miután a törzsek szövetséget kötöttek, elindultak nyugatra.", "english": "After the tribes formed an alliance, they set off to the west."},
        {"spanish": "Mielőtt beléptek volna a Kárpát-medencébe, Etelközben éltek.", "english": "Before they entered the Carpathian Basin, they lived in Etelköz."},
        {"spanish": "Miután felderítették a vidéket, megkezdődött a honfoglalás.", "english": "After they scouted the countryside, the conquest began."}
    ]
})

write_json(EXERCISES_DIR / "b1-honfoglalas-01-ex.json", {
    "exercises": [
        {
            "id": "b1-honfoglalas-01.ex01",
            "type": "multiple-choice",
            "title": "A magyar nyelv eredete",
            "instruction": "Válaszd ki a helyes nyelvtörténeti tényt!",
            "question": "Melyik nyelvcsaládba tartozik a magyar nyelv?",
            "options": ["A finnugor (uráli) nyelvcsaládba", "Az indoeurópai nyelvcsaládba", "A sémi nyelvcsaládba", "A szino-tibeti nyelvcsaládba"],
            "correctIndex": 0,
            "explanation": "A magyar nyelv az uráli, ezen belül a finnugor nyelvcsalád tagja.",
            "teaches": ["nyelvcsalad", "oshaza"]
        },
        {
            "id": "b1-honfoglalas-01.ex02",
            "type": "fill-blank",
            "title": "Vándorlási állomások",
            "instruction": "Egészítsd ki a mondatot!",
            "sentence": "A magyarok a Dnyeper és a Duna közötti ___ éltek közvetlenül a honfoglalás előtt.",
            "correctAnswer": "Etelközben",
            "options": ["Etelközben", "Londonban", "Párizsban", "Rómában"],
            "teaches": ["oshaza", "vandorlas"]
        },
        {
            "id": "b1-honfoglalas-01.ex03",
            "type": "sentence-builder",
            "title": "Miután szövetséget kötöttek",
            "instruction": "Állítsd össze a mondatot a szavakból!",
            "words": ["Miután", "szövetséget", "kötöttek,", "a", "törzsek", "elindultak", "nyugatra."],
            "correctSentence": "Miután szövetséget kötöttek, a törzsek elindultak nyugatra.",
            "english": "After they formed an alliance, the tribes set off to the west.",
            "teaches": ["szovetseg", "vandorlas"]
        },
        {
            "id": "b1-honfoglalas-01.ex04",
            "type": "multiple-choice",
            "title": "A kettős fejedelemség",
            "instruction": "Ki volt a katonai hatalom birtokosa a kettős fejedelemségben?",
            "question": "Melyik tisztségviselő vezette a hadsereget?",
            "options": ["A gyula", "A kende", "A római pápa", "A királyi udvarmester"],
            "correctIndex": 0,
            "explanation": "A kettős fejedelemségben a gyula gyakorolta a tényleges katonai és világi hatalmat.",
            "teaches": ["fejedelemseg"]
        },
        {
            "id": "b1-honfoglalas-01.ex05",
            "type": "fill-blank",
            "title": "Mielőtt átkeltek volna",
            "instruction": "Válaszd ki a megfelelő kötőszót!",
            "sentence": "___ átkeltek volna a hegyeken, a vezérek megerősítették a szövetséget.",
            "correctAnswer": "Mielőtt",
            "options": ["Mielőtt", "Miután", "Ezért", "Pedig"],
            "teaches": ["szovetseg"]
        },
        {
            "id": "b1-honfoglalas-01.ex06",
            "type": "sentence-builder",
            "title": "Lovas nomád életmód",
            "instruction": "Rendezd helyes sorrendbe a mondatrészeket!",
            "words": ["A", "magyarok", "kiváló", "lovas", "harcosok", "voltak."],
            "correctSentence": "A magyarok kiváló lovas harcosok voltak.",
            "english": "The Magyars were excellent equestrian warriors.",
            "teaches": ["lovas", "sztyeppe"]
        },
        {
            "id": "b1-honfoglalas-01.ex07",
            "type": "multiple-choice",
            "title": "Levédia és a Kazár Birodalom",
            "instruction": "Kikkel álltak kapcsolatban a magyarok Levédiában?",
            "question": "Melyik birodalom szomszédságában éltek a magyar törzsek Levédiában?",
            "options": ["A Kazár Birodalommal", "A Brit Birodalommal", "Az Oszmán Birodalommal", "Az Orosz Cársággal"],
            "correctIndex": 0,
            "explanation": "Levédiában a magyarok a kazárokkal éltek szoros szimbiózisban.",
            "teaches": ["fejedelemseg", "elsajatit"]
        },
        {
            "id": "b1-honfoglalas-01.ex08",
            "type": "fill-blank",
            "title": "Fokozatos költözés",
            "instruction": "Egészítsd ki a mondatot!",
            "sentence": "A törzsek ___ haladtak a folyók mentén az új szállásterületek felé.",
            "correctAnswer": "fokozatosan",
            "options": ["fokozatosan", "soha", "hangosan", "autóval"],
            "teaches": ["fokozatosan"]
        }
    ]
})

write_json(LESSONS_DIR / "b1-honfoglalas-01.json", make_lesson(
    "lesson.b1.honfoglalas-01",
    "A vándorlás útja (Migration & Ancient Homeland)",
    "Időhatározói mellékmondatok: miután és mielőtt",
    [
        "Welcome to Unit 3 of the Hungarian Citizenship Track. In this unit, we explore the *Honfoglalás* (Conquest of the Carpathian Basin) in 895, a foundational milestone of Hungarian national identity.",
        "In this first lesson, we trace the origins of the Magyars from the Uralic Finno-Ugric homeland through Magna Hungaria, Levédia, and Etelköz.",
        "We also master time clauses with *miután* (after) and *mielőtt* (before), indispensable for narrating historical chronologies."
    ],
    [
        "I can explain the Finno-Ugric language origins of Hungarian and the main stations of migration (Magna Hungaria, Levédia, Etelköz).",
        "I can define the institution of dual principality (*kettős fejedelemség: kende és gyula*).",
        "I can use *miután* and *mielőtt* in complex historical sentences.",
        "I can answer citizenship interview questions about the origins of the Magyar people."
    ],
    "stories/world/b1/b1-honfoglalas-01-nyugatranyomas.json",
    "vocabulary/b1/b1-honfoglalas-01-voc.json",
    "grammar/b1/b1-honfoglalas-01-miutan-mielott-gr.json",
    "exercises/b1/b1-honfoglalas-01-ex.json",
    [f"b1-honfoglalas-01.ex{i:02d}" for i in range(1, 9)]
))

# -----------------
# Lesson 2: Átkelés a Kárpátokon (895)
# -----------------
write_json(STORIES_DIR / "b1-honfoglalas-02-atkeles.json", make_story(
    "story.b1.honfoglalas.02",
    "Átkelés a Vereckei-hágón (895)",
    "The historic crossing of the Carpathian mountain passes in 895: Árpád leads the main forces through the Verecke Pass into the Alföld, escaping the Petcheneg attack.",
    "Vereckei-hágó és a Tisza vidéke",
    ["szórend összetett mondatokban"],
    ["Vereckei-hágó", "Honfoglalás 895", "Besenyő támadás"],
    [
        "895 tavaszán a magyar fősereg Árpád vezér vezetésével elérte az Északkeleti-Kárpátok hágóit. A legismertebb és legfontosabb átkelőhely a Vereckei-hágó volt.",
        "Miközben a magyar seregek egy része a bolgárok ellen harcolt délen, Etelközt váratlan besenyő támadás érte. Ez a katonai esemény felgyorsította a törzsek átkelését a hegyeken.",
        "Családok, harcosok, asszonyok és gyermekek hatalmas állatcsordákkal és szekerekkel keltek át a meredek hegyi ösvényeken.",
        "A Kárpátok hágóin átkelve a magyarok megpillantották a gazdag, zöldellő Tisza-völgyet és a tágas Alföldet, amely bőséges legelőt biztosított lovaiknak.",
        "A honfoglalás első szakaszában a magyarok birtokba vették a Felső-Tisza vidékét és Erdélyt, kialakítva első szálláshelyeiket az új hazában."
    ],
    [
        {"lemma": "hágó", "pos": "noun", "cefr": "B1", "gloss": "mountain pass"},
        {"lemma": "fősereg", "pos": "noun", "cefr": "B1", "gloss": "main army"},
        {"lemma": "átkelés", "pos": "noun", "cefr": "B1", "gloss": "crossing"},
        {"lemma": "legelő", "pos": "noun", "cefr": "B1", "gloss": "pasture"}
    ],
    [
        {
            "question": "Melyik híres hágón keresztül érkezett Árpád serege a Kárpát-medencébe 895-ben?",
            "options": ["A Vereckei-hágón", "A Gibraltári-szoroson", "A Brenner-hágón", "A Szuezi-csatornán"],
            "correctIndex": 0,
            "explanation": "A honfoglaló magyarok főserege a Vereckei-hágón kelt át a Kárpátokon 895-ben."
        },
        {
            "question": "Milyen külső támadás gyorsította fel a magyarok beköltözését?",
            "options": ["A besenyők támadása Etelközben", "Római hadihajók ágyúzása", "A francia hadsereg támadása", "Viking tengeri rablók támadása"],
            "correctIndex": 0,
            "explanation": "A besenyők etelközi támadása felgyorsította a teljes népesség átköltözését a Kárpát-medencébe."
        },
        {
            "question": "Melyik területet vették először birtokba a magyarok?",
            "options": ["A Felső-Tisza vidékét és Erdélyt", "Csak Bécset és Berlint", "Kizárólag London városát", "Az Adriai-tenger szigeteit"],
            "correctIndex": 0,
            "explanation": "A honfoglalás első szakaszában a Felső-Tisza vidékét és Erdély folyóvölgyeit szállták meg."
        }
    ]
))

write_json(VOCAB_DIR / "b1-honfoglalas-02-voc.json", {
    "title": "Átkelés a Kárpátokon és a Vereckei-hágó",
    "words": [
        {"lemma": "hágó", "pos": "noun", "cefr": "B1", "translation": "mountain pass", "examples": [{"hungarian": "A Vereckei-hágó a magyar történelem szimbolikus helye.", "english": "The Verecke Pass is a symbolic place of Hungarian history."}]},
        {"lemma": "fősereg", "pos": "noun", "cefr": "B1", "translation": "main army", "examples": [{"hungarian": "Árpád vezette a fősereget az átkelés során.", "english": "Árpád led the main army during the crossing."}]},
        {"lemma": "átkelés", "pos": "noun", "cefr": "B1", "translation": "crossing", "examples": [{"hungarian": "Az átkelés nehéz és veszélyes feladat volt.", "english": "The crossing was a difficult and dangerous task."}]},
        {"lemma": "legelő", "pos": "noun", "cefr": "B1", "translation": "pasture", "examples": [{"hungarian": "A tágas legelők kiválóak voltak az állatoknak.", "english": "The spacious pastures were excellent for the animals."}]},
        {"lemma": "ösvény", "pos": "noun", "cefr": "B1", "translation": "path / trail", "examples": [{"hungarian": "Keskeny hegyi ösvényeken haladtak át a hegyen.", "english": "They crossed the mountain along narrow mountain paths."}]},
        {"lemma": "csorda", "pos": "noun", "cefr": "B1", "translation": "herd", "examples": [{"hungarian": "Nagy marhacsordákat tereltek magukkal.", "english": "They drove large cattle herds with them."}]},
        {"lemma": "szekér", "pos": "noun", "cefr": "B1", "translation": "wagon / cart", "examples": [{"hungarian": "A szekereken szállították a sátrakat és eszközöket.", "english": "They transported tents and tools on the wagons."}]},
        {"lemma": "felgyorsít", "pos": "verb", "cefr": "B1", "translation": "to accelerate / speed up", "examples": [{"hungarian": "A támadás felgyorsította a döntést.", "english": "The attack accelerated the decision."}]},
        {"lemma": "birtokba vesz", "pos": "verb", "cefr": "B1", "translation": "to occupy / take possession of", "examples": [{"hungarian": "A törzsek birtokba vették a folyóvölgyeket.", "english": "The tribes took possession of the river valleys."}]},
        {"lemma": "szálláshely", "pos": "noun", "cefr": "B1", "translation": "camp / quarters / settlement area", "examples": [{"hungarian": "Minden törzs kijelölte a saját szálláshelyét.", "english": "Every tribe designated its own settlement area."}]},
        {"lemma": "megpillant", "pos": "verb", "cefr": "B1", "translation": "to catch sight of / glimpse", "examples": [{"hungarian": "A hegytetőről megpillantották a virágzó alföldet.", "english": "From the mountain top they caught sight of the flourishing plain."}]},
        {"lemma": "zöldellő", "pos": "adj", "cefr": "B1", "translation": "green / lush", "examples": [{"hungarian": "Zöldellő völgyek fogadták az érkezőket.", "english": "Lush valleys greeted the arrivals."}]}
    ]
})

write_json(GRAMMAR_DIR / "b1-honfoglalas-02-sorrend-mellekmondatokkal-gr.json", {
    "title": "Szórend és fókusz összetett mondatokban",
    "level": "B1",
    "rules": [
        {
            "id": "word-order-complex",
            "title": "Word Order in Complex Sentences",
            "text": "In Hungarian subordinate clauses, the verb usually follows the focus element: *Amikor Árpád megérkezett a hágóhoz, a fősereg azonnal megállt.* (When Árpád arrived at the pass, the main army stopped immediately.)",
            "tip": "The emphasised element sits directly in front of the conjugated verb."
        },
        {
            "id": "simultaneous-actions",
            "title": "Expressing Simultaneous Actions with 'miközben'",
            "text": "*Miközben* (while / whilst) introduces concurrent actions: *Miközben a férfiak a sereget vezették, a családok a szekerekkel haladtak.* (While the men led the army, the families moved with the wagons.)",
            "tip": "Both actions take the same grammatical tense."
        }
    ],
    "examples": [
        {"spanish": "Miközben a fősereg átkelt a hágón, a felderítők megvizsgálták a völgyet.", "english": "While the main army crossed the pass, scouts inspected the valley."},
        {"spanish": "Amikor megpillantották a Tiszát, megálltak pihenni.", "english": "When they caught sight of the Tisza, they stopped to rest."},
        {"spanish": "Árpád vezér volt az, aki a honfoglalást irányította.", "english": "It was Chieftain Árpád who directed the conquest."}
    ]
})

write_json(EXERCISES_DIR / "b1-honfoglalas-02-ex.json", {
    "exercises": [
        {
            "id": "b1-honfoglalas-02.ex01",
            "type": "multiple-choice",
            "title": "A honfoglalás éve és hágója",
            "instruction": "Válaszd ki az alapvető történelmi évszámot!",
            "question": "Melyik évben kelt át Árpád főserege a Vereckei-hágón?",
            "options": ["895-ben", "1000-ben", "1222-ben", "1848-ban"],
            "correctIndex": 0,
            "explanation": "A honfoglalás hagyományos évszáma 895.",
            "teaches": ["hago", "atkeles"]
        },
        {
            "id": "b1-honfoglalas-02.ex02",
            "type": "fill-blank",
            "title": "Átkelés a hágón",
            "instruction": "Egészítsd ki a mondatot!",
            "sentence": "A magyarok a Kárpátok legismertebb hágóján, a ___ keltek át.",
            "correctAnswer": "Vereckei-hágón",
            "options": ["Vereckei-hágón", "Duna-hídon", "tengerparton", "vasútvonalon"],
            "teaches": ["hago", "atkeles"]
        },
        {
            "id": "b1-honfoglalas-02.ex03",
            "type": "sentence-builder",
            "title": "Árpád vezette a sereget",
            "instruction": "Állítsd össze a mondatot!",
            "words": ["Árpád", "vezér", "irányította", "a", "honfoglaló", "fősereget."],
            "correctSentence": "Árpád vezér irányította a honfoglaló fősereget.",
            "english": "Chieftain Árpád directed the conquering main army.",
            "teaches": ["fosereg", "atkeles"]
        },
        {
            "id": "b1-honfoglalas-02.ex04",
            "type": "multiple-choice",
            "title": "Párhuzamos cselekvések",
            "instruction": "Mit csináltak a családok az átkelés során?",
            "question": "Hogyan közlekedtek a családok a nehéz hegyi utakon?",
            "options": ["Szekerekkel és állatcsordákkal haladtak a hegyi ösvényeken", "Vonattal utaztak kényelmesen", "Gőzhajókon érkeztek a folyón", "Egyenként repülővel szálltak le"],
            "correctIndex": 0,
            "explanation": "A családok szekerekkel, szarvasmarha- és lócsordákkal vonultak át a hágókon.",
            "teaches": ["szeker", "csorda", "osveny"]
        },
        {
            "id": "b1-honfoglalas-02.ex05",
            "type": "fill-blank",
            "title": "Miközben átkeltek",
            "instruction": "Válaszd ki a megfelelő kötőszót!",
            "sentence": "___ a seregek a hágókon vonultak, a felderítők megvizsgálták a legelőket.",
            "correctAnswer": "Miközben",
            "options": ["Miközben", "Mert", "De", "Tehát"],
            "teaches": ["legelo"]
        },
        {
            "id": "b1-honfoglalas-02.ex06",
            "type": "sentence-builder",
            "title": "Új legelők a Tisza mentén",
            "instruction": "Rendezd helyes sorrendbe a szavakat!",
            "words": ["A", "tágas", "Alföld", "bőséges", "legelőt", "biztosított", "a", "lovaknak."],
            "correctSentence": "A tágas Alföld bőséges legelőt biztosított a lovaknak.",
            "english": "The spacious Great Plain provided abundant pasture for the horses.",
            "teaches": ["legelo", "megpillant"]
        },
        {
            "id": "b1-honfoglalas-02.ex07",
            "type": "multiple-choice",
            "title": "Szállásterületek kialakítása",
            "instruction": "Mit jelent a szálláshely a honfoglalás idején?",
            "question": "Mi volt a törzsek szálláshelye?",
            "options": ["Az a földrajzi terület, ahol a törzs letelepedett és legeltetett", "Egy modern szállodai szoba", "Egy katonai börtön", "Egy elhagyott barlang a hegyekben"],
            "correctIndex": 0,
            "explanation": "A szálláshely az a folyóvölgyi vagy síksági terület volt, ahol egy törzs letelepedett.",
            "teaches": ["szallashely", "birtokba-vesz"]
        },
        {
            "id": "b1-honfoglalas-02.ex08",
            "type": "fill-blank",
            "title": "Erdély és Felső-Tisza",
            "instruction": "Egészítsd ki a mondatot!",
            "sentence": "A magyarok először a Felső-Tisza vidékét és ___ vették birtokba.",
            "correctAnswer": "Erdélyt",
            "options": ["Erdélyt", "Madridot", "Párizst", "Athént"],
            "teaches": ["birtokba-vesz"]
        }
    ]
})

write_json(LESSONS_DIR / "b1-honfoglalas-02.json", make_lesson(
    "lesson.b1.honfoglalas-02",
    "Átkelés a Vereckei-hágón (Crossing the Carpathians - 895)",
    "Szórend és fókusz összetett mondatokban",
    [
        "In this second lesson, we study the dramatic entry into the Carpathian Basin in 895 through the legendary Verecke Pass (*Vereckei-hágó*).",
        "You will learn about Chieftain Árpád's leadership, the impact of the Petcheneg raid on Etelköz, and the establishment of the first settlement areas along the Upper Tisza and Transylvania.",
        "We also practice focus word order and simultaneous clauses with *miközben*."
    ],
    [
        "I can state the year of the Honfoglalás (895) and the significance of the Verecke Pass.",
        "I can describe how Árpád led the tribes into the Carpathian Basin.",
        "I can use *miközben* to describe concurrent historical events.",
        "I can explain the strategic importance of pastures and river valleys for equestrian nomads."
    ],
    "stories/world/b1/b1-honfoglalas-02-atkeles.json",
    "vocabulary/b1/b1-honfoglalas-02-voc.json",
    "grammar/b1/b1-honfoglalas-02-sorrend-mellekmondatokkal-gr.json",
    "exercises/b1/b1-honfoglalas-02-ex.json",
    [f"b1-honfoglalas-02.ex{i:02d}" for i in range(1, 9)]
))

# -----------------
# Lesson 3: A hét törzs és a vérszerződés
# -----------------
write_json(STORIES_DIR / "b1-honfoglalas-03-arpadeshettorzs.json", make_story(
    "story.b1.honfoglalas.03",
    "A vérszerződés és a hét magyar törzs",
    "The legendary blood oath (*vérszerződés*) of the seven Magyar chieftains at Pusztaszer, the seven tribes, and the leadership of Álmos and Árpád as recorded by Anonymus.",
    "Pusztaszer és Etelköz",
    ["nevesített alanyok és igei egyeztetés"],
    ["Vérszerződés", "Hét törzs", "Árpád és Álmos", "Anonymus"],
    [
        "A középkori krónikák, különösen Anonymus Gesta Hungarorum című műve szerint a magyar törzsek fejedelmei szent esküt, úgynevezett vérszerződést kötöttek egymással.",
        "A hét törzs – Nyék, Megyer, Kürtgyarmat, Tarján, Jenő, Kér és Keszi – vezérei vérüket egy közös edénybe csorgatták, kifejezve a felbonthatatlan testvériséget és hűséget.",
        "A szerződés értelmében a vezérek elismerték Álmos fejedelmet és fiát, Árpádot örökös vezetőjüknek, és megesküdtek, hogy a közösen szerzett javakból és földekből mindenki méltó részt kap.",
        "A hét magyar törzshöz csatlakozott a kazár lázadókból álló kabar népcsoport is, akik a hadsereg elővédjeként és felderítőiként szolgáltak.",
        "A vérszerződés és az Anonymus által megörökített pusztaszeri gyűlés a magyar államjogi hagyomány első, szimbolikus alkotmányos megállapodásaként él a nemzeti emlékezetben."
    ],
    [
        {"lemma": "vérszerződés", "pos": "noun", "cefr": "B1", "gloss": "blood oath / covenant"},
        {"lemma": "törzsszövetség", "pos": "noun", "cefr": "B1", "gloss": "tribal confederation"},
        {"lemma": "hűség", "pos": "noun", "cefr": "B1", "gloss": "loyalty / fidelity"},
        {"lemma": "elővéd", "pos": "noun", "cefr": "B1", "gloss": "vanguard"}
    ],
    [
        {
            "question": "Mit pecsételt meg a hét magyar vezér vérszerződése?",
            "options": ["A hét törzs örök szövetségét és Árpád nemzetségének vezetését", "Egy békét a római császárral", "A törzsek feloszlását és szétválását", "A kereskedelmi szerződést Bizánccal"],
            "correctIndex": 0,
            "explanation": "A vérszerződés a hét törzs szövetségét és Álmos, illetve Árpád nemzetségének örökös vezetését rögzítette."
        },
        {
            "question": "Melyik krónikás örökítette meg a vérszerződés és a honfoglalás történetét a Gesta Hungarorumban?",
            "options": ["Anonymus, Béla király névtelen jegyzője", "Mátyás király", "Petőfi Sándor", "Julius Caesar"],
            "correctIndex": 0,
            "explanation": "Anonymus, III. Béla király névtelen jegyzője írta meg a Gesta Hungarorumot."
        },
        {
            "question": "Hány törzs alkotta a honfoglaló magyar szövetséget?",
            "options": ["Hét törzs (kiegészülve a csatlakozott kabarokkal)", "Három törzs", "Tizenkét törzs", "Csak egyetlen család"],
            "correctIndex": 0,
            "explanation": "A hét magyar törzs (Nyék, Megyer, Kürtgyarmat, Tarján, Jenő, Kér, Keszi) és a csatlakozott kabarok."
        }
    ]
))

write_json(VOCAB_DIR / "b1-honfoglalas-03-voc.json", {
    "title": "A vérszerződés és a hét magyar törzs",
    "words": [
        {"lemma": "vérszerződés", "pos": "noun", "cefr": "B1", "translation": "blood oath", "examples": [{"hungarian": "A hét vezér vérszerződéssel pecsételte meg az egységet.", "english": "The seven chieftains sealed unity with a blood oath."}]},
        {"lemma": "törzsszövetség", "pos": "noun", "cefr": "B1", "translation": "tribal confederation", "examples": [{"hungarian": "A törzsszövetség élén Árpád fejedelem állt.", "english": "Chieftain Árpád stood at the head of the tribal confederation."}]},
        {"lemma": "hűség", "pos": "noun", "cefr": "B1", "translation": "loyalty / fidelity", "examples": [{"hungarian": "Örök hűséget esküdtek a vezérnek.", "english": "They swore eternal loyalty to the chieftain."}]},
        {"lemma": "elővéd", "pos": "noun", "cefr": "B1", "translation": "vanguard", "examples": [{"hungarian": "A kabar harcosok a sereg elővédjét alkották.", "english": "The Kabar warriors formed the vanguard of the army."}]},
        {"lemma": "krónika", "pos": "noun", "cefr": "B1", "translation": "chronicle", "examples": [{"hungarian": "A középkori krónikák megőrizték a vezérek neveit.", "english": "Medieval chronicles preserved the names of the chieftains."}]},
        {"lemma": "jegyző", "pos": "noun", "cefr": "B1", "translation": "notary / scribe", "examples": [{"hungarian": "Anonymus Béla király névtelen jegyzője volt.", "english": "Anonymus was the anonymous notary of King Béla."}]},
        {"lemma": "örökös", "pos": "adj", "cefr": "B1", "translation": "hereditary / eternal", "examples": [{"hungarian": "Árpád nemzetsége örökös jogot kapott a vezetésre.", "english": "Árpád's clan received hereditary right to the leadership."}]},
        {"lemma": "felbonthatatlan", "pos": "adj", "cefr": "B1", "translation": "indissoluble / unbreakable", "examples": [{"hungarian": "A szerződés felbonthatatlan egységet teremtett.", "english": "The covenant created an indissoluble unity."}]},
        {"lemma": "megesküszik", "pos": "verb", "cefr": "B1", "translation": "to swear an oath", "examples": [{"hungarian": "A vezérek megesküdtek a közös célokra.", "english": "The chieftains swore an oath for the common goals."}]},
        {"lemma": "nemzetség", "pos": "noun", "cefr": "B1", "translation": "clan / lineage", "examples": [{"hungarian": "Az Árpád nemzetségből származtak a későbbi királyok.", "english": "From the Árpád clan descended the later kings."}]},
        {"lemma": "emlékezet", "pos": "noun", "cefr": "B1", "translation": "memory / remembrance", "examples": [{"hungarian": "A nemzeti emlékezet tisztelettel őrzi a honalapítókat.", "english": "National memory preserves the founders of the homeland with respect."}]},
        {"lemma": "gyűlés", "pos": "noun", "cefr": "B1", "translation": "assembly / gathering", "examples": [{"hungarian": "A pusztaszeri gyűlésen osztották szét a földeket.", "english": "At the Pusztaszer assembly they distributed the lands."}]}
    ]
})

write_json(GRAMMAR_DIR / "b1-honfoglalas-03-nevesitett-alanyok-gr.json", {
    "title": "Nevesített alanyok és egyeztetés listázáskor",
    "level": "B1",
    "rules": [
        {
            "id": "plural-subject-listing",
            "title": "Subject-Verb Agreement with Multiple Named Nouns",
            "text": "When multiple singular subjects are coordinated with *és* (and), the verb is in the plural in Hungarian: *Álmos és Árpád vezették a sereget.* (Álmos and Árpád led the army.)",
            "tip": "If coordinated with *vagy* (or), the verb remains singular: *Álmos vagy Árpád döntött.*"
        },
        {
            "id": "appositions-titles",
            "title": "Appositions with Historical Titles",
            "text": "Titles follow or precede names as appositives: *Árpád fejedelem, Anonymus jegyző, Béla király*. In inflected sentences, the case suffix attaches to the noun or both elements if in apposition: *Beszéltek Árpád fejedelemről* / *Anonymusról, a névtelen jegyzőről*.",
            "tip": "In apposition with commas (*Anonymus, a király jegyzője*), both parts take the same case suffix."
        }
    ],
    "examples": [
        {"spanish": "Álmos és Árpád kötötték meg a történelmi szövetséget.", "english": "Álmos and Árpád concluded the historic alliance."},
        {"spanish": "A hét vezér megesküdött a közös hűségre.", "english": "The seven chieftains swore to mutual loyalty."},
        {"spanish": "Anonymus, a névtelen jegyző írta le a pusztaszeri gyűlést.", "english": "Anonymus, the anonymous scribe wrote down the Pusztaszer assembly."}
    ]
})

write_json(EXERCISES_DIR / "b1-honfoglalas-03-ex.json", {
    "exercises": [
        {
            "id": "b1-honfoglalas-03.ex01",
            "type": "multiple-choice",
            "title": "A vérszerződés lényege",
            "instruction": "Válaszd ki a helyes állítást!",
            "question": "Mit jelentett a hét vezér vérszerződése a magyar hagyományban?",
            "options": ["A hét törzs felbonthatatlan szövetségét és Árpád nemzetségének vezetését", "Egy békeszerződést a római császárral", "A törzsek közötti háború kezdetét", "A tengeri kereskedelem megnyitását"],
            "correctIndex": 0,
            "explanation": "A vérszerződés a hét törzs szövetségét és Árpád családjának vezető szerepét rögzítette.",
            "teaches": ["verszerzodes", "torzsszovetseg"]
        },
        {
            "id": "b1-honfoglalas-03.ex02",
            "type": "fill-blank",
            "title": "A krónikás neve",
            "instruction": "Egészítsd ki a mondatot!",
            "sentence": "A Gesta Hungarorum szerzője III. Béla király névtelen jegyzője, ___ volt.",
            "correctAnswer": "Anonymus",
            "options": ["Anonymus", "Kossuth", "Petőfi", "Mátyás"],
            "teaches": ["kronika", "jegyzo"]
        },
        {
            "id": "b1-honfoglalas-03.ex03",
            "type": "sentence-builder",
            "title": "Örök hűség esküje",
            "instruction": "Állítsd össze a mondatot a megadott szavakból!",
            "words": ["A", "hét", "vezér", "örök", "hűséget", "esküdött", "Árpádnak."],
            "correctSentence": "A hét vezér örök hűséget esküdött Árpádnak.",
            "english": "The seven chieftains swore eternal loyalty to Árpád.",
            "teaches": ["huseg", "megeskuszik"]
        },
        {
            "id": "b1-honfoglalas-03.ex04",
            "type": "multiple-choice",
            "title": "Csatlakozott népek",
            "instruction": "Melyik nép csatlakozott a hét magyar törzshöz a honfoglalás előtt?",
            "question": "Kik alkották a hadsereg elővédjét?",
            "options": ["A kabarok", "A vikingek", "A spanyolok", "A római légiósok"],
            "correctIndex": 0,
            "explanation": "A kabarok csatlakoztak a magyarokhoz és az elővédet alkották a hadjáratok során.",
            "teaches": ["eloved", "torzsszovetseg"]
        },
        {
            "id": "b1-honfoglalas-03.ex05",
            "type": "fill-blank",
            "title": "Pusztaszeri gyűlés",
            "instruction": "Válaszd ki a helyes kifejezést!",
            "sentence": "A hagyomány szerint a vezérek a ___ gyűlésen osztották szét a földeket.",
            "correctAnswer": "pusztaszeri",
            "options": ["pusztaszeri", "párizsi", "londoni", "bécsi"],
            "teaches": ["gyules", "emlekezet"]
        },
        {
            "id": "b1-honfoglalas-03.ex06",
            "type": "sentence-builder",
            "title": "Álmos és Árpád",
            "instruction": "Rendezd helyes sorrendbe a szavakat!",
            "words": ["Álmos", "és", "Árpád", "voltak", "a", "törzsszövetség", "fő", "vezetői."],
            "correctSentence": "Álmos és Árpád voltak a törzsszövetség fő vezetői.",
            "english": "Álmos and Árpád were the main leaders of the tribal confederation.",
            "teaches": ["nemzetseg", "torzsszovetseg"]
        },
        {
            "id": "b1-honfoglalas-03.ex07",
            "type": "multiple-choice",
            "title": "A hét törzs neve",
            "instruction": "Melyik név tartozik a hét magyar törzs közé?",
            "question": "A felsoroltak közül melyik egy honfoglaló magyar törzs neve?",
            "options": ["Megyer (vagy Nyék, Tarján, Jenő, Kér, Keszi, Kürtgyarmat)", "Burgund", "Szász", "Gót"],
            "correctIndex": 0,
            "explanation": "A Megyer a hét honfoglaló magyar törzs egyike volt (amelyből a magyar népnév is származik).",
            "teaches": ["torzsszovetseg"]
        },
        {
            "id": "b1-honfoglalas-03.ex08",
            "type": "fill-blank",
            "title": "Felbonthatatlan szerződés",
            "instruction": "Egészítsd ki a mondatot!",
            "sentence": "A vérrel megpecsételt megállapodás ___ egységet hozott létre.",
            "correctAnswer": "felbonthatatlan",
            "options": ["felbonthatatlan", "gyenge", "rövid", "veszélyes"],
            "teaches": ["felbonthatatlan"]
        }
    ]
})

write_json(LESSONS_DIR / "b1-honfoglalas-03.json", make_lesson(
    "lesson.b1.honfoglalas-03",
    "A vérszerződés és a hét törzs (Blood Oath & Seven Chieftains)",
    "Nevesített alanyok és igei egyeztetés listázáskor",
    [
        "In this third lesson, we discover the legendary blood oath (*vérszerződés*) concluded by the chieftains of the seven Magyar tribes (Nyék, Megyer, Kürtgyarmat, Tarján, Jenő, Kér, Keszi).",
        "You will learn about Álmos and Árpád, the chronicle of Anonymus (*Gesta Hungarorum*), the Kabar allies, and the historical assembly of Pusztaszer.",
        "We also practice grammatical agreements with multiple coordinated subjects and historical appositive titles."
    ],
    [
        "I can name the significance of the blood oath (*vérszerződés*) and the leadership of Árpád.",
        "I can identify the chronicler Anonymus and the seven Hungarian tribes.",
        "I can explain the role of the Pusztaszer assembly in Hungarian constitutional tradition.",
        "I can apply subject-verb agreement rules when listing multiple historical figures."
    ],
    "stories/world/b1/b1-honfoglalas-03-arpadeshettorzs.json",
    "vocabulary/b1/b1-honfoglalas-03-voc.json",
    "grammar/b1/b1-honfoglalas-03-nevesitett-alanyok-gr.json",
    "exercises/b1/b1-honfoglalas-03-ex.json",
    [f"b1-honfoglalas-03.ex{i:02d}" for i in range(1, 9)]
))

# -----------------
# Lesson 4: Birtokbavétel és a pozsonyi csata (907)
# -----------------
write_json(STORIES_DIR / "b1-honfoglalas-04-birtokbavetel.json", make_story(
    "story.b1.honfoglalas.04",
    "A Kárpát-medence birtokbavétele és a pozsonyi csata (907)",
    "The systematic occupation of the Carpathian Basin (895–900) and the decisive Battle of Pozsony (Bratislava, 907), where Árpád's army crushed the East Frankish invasion and secured the homeland.",
    "Dunántúl és Pozsony (Bratislava)",
    ["több szereplős időhatározói szerkezetek"],
    ["Birtokbavétel", "Pozsonyi csata 907", "Árpád győzelme"],
    [
        "895 és 900 között a magyar törzsek fokozatosan kiterjesztették ellenőrzésüket a teljes Kárpát-medencére. Miután birtokba vették az Alföldet és Erdélyt, 900-ban a Dunántúlt is elfoglalták.",
        "A szomszédos Keleti Frank Királyság azonban nem fogadta el az új hatalom berendezkedését. Gyermek Lajos frank király és Luitpold bajor őrgróf hatalmas sereget gyűjtött a magyarok kiűzésére vagy megsemmisítésére.",
        "907 júliusában Pozsony (a mai Bratislava) mellett zajlott le a korszak legnagyobb és legfontosabb összecsapása: a pozsonyi csata.",
        "A fegyelmezett magyar lovas íjászok a nomád harcmodor – a színlelt visszavonulás és a villámgyors bekerítés – segítségével tönkreverték a nehézpáncélos frank sereget.",
        "A pozsonyi diadal biztosította a magyarok végleges megmaradását a Kárpát-medencében, és kijelölte a leendő Magyar Királyság nyugati határait a Lajta folyónál."
    ],
    [
        {"lemma": "pozsonyi csata", "pos": "noun", "cefr": "B1", "gloss": "Battle of Pozsony (907)"},
        {"lemma": "diadal", "pos": "noun", "cefr": "B1", "gloss": "triumph / victory"},
        {"lemma": "harcmodor", "pos": "noun", "cefr": "B1", "gloss": "fighting style / tactics"},
        {"lemma": "megmaradás", "pos": "noun", "cefr": "B1", "gloss": "survival / permanence"}
    ],
    [
        {
            "question": "Mikor zajlott a pozsonyi csata, amely biztosította a honfoglalás végleges sikerét?",
            "options": ["907-ben", "1241-ben", "1526-ban", "1848-ban"],
            "correctIndex": 0,
            "explanation": "A pozsonyi csata 907 júliusában zajlott le, megvédve a magyar hazát a frank támadással szemben."
        },
        {
            "question": "Milyen haditaktikát alkalmaztak a magyar lovasok a frank sereg ellen?",
            "options": ["Színlelt visszavonulást és villámgyors íjász bekerítést", "Várfalak mögé bújtak", "Csak gyalogos lándzsás támadást intéztek", "Ágyútüzet zúdítottak az ellenségre"],
            "correctIndex": 0,
            "explanation": "A nomád könnyűlovasság színlelt visszavonulással csalta csapdába és nyilazta le a nehézpáncélos ellenséget."
        },
        {
            "question": "Mi volt a pozsonyi csata történelmi következménye?",
            "options": ["A magyarok végleges megmaradása és a nyugati határok biztosítása", "A törzsek visszatérése Ázsiába", "A Kárpát-medence elvesztése", "A Frank Birodalom csatlakozása Magyarországhoz"],
            "correctIndex": 0,
            "explanation": "A 907-es győzelem megvédte a Kárpát-medencét és évszázadokra biztosította a nyugati határt."
        }
    ]
))

write_json(VOCAB_DIR / "b1-honfoglalas-04-voc.json", {
    "title": "Birtokbavétel és a pozsonyi csata (907)",
    "words": [
        {"lemma": "diadal", "pos": "noun", "cefr": "B1", "translation": "triumph / glorious victory", "examples": [{"hungarian": "A pozsonyi diadal megmentette a fiatal hazát.", "english": "The triumph of Pozsony saved the young homeland."}]},
        {"lemma": "harcmodor", "pos": "noun", "cefr": "B1", "translation": "fighting style / warfare", "examples": [{"hungarian": "A nomád harcmodor meglepte a nehézpáncélos lovagokat.", "english": "Nomadic warfare surprised the heavy-armoured knights."}]},
        {"lemma": "megmaradás", "pos": "noun", "cefr": "B1", "translation": "survival / persistence", "examples": [{"hungarian": "A győzelem a nemzet megmaradását jelentette.", "english": "The victory meant the survival of the nation."}]},
        {"lemma": "összecsapás", "pos": "noun", "cefr": "B1", "translation": "clash / encounter", "examples": [{"hungarian": "A heves összecsapás a folyó partján történt.", "english": "The fierce clash occurred on the riverbank."}]},
        {"lemma": "bekerítés", "pos": "noun", "cefr": "B1", "translation": "encirclement", "examples": [{"hungarian": "A gyors bekerítés elvágta a frankok útját.", "english": "The fast encirclement cut off the Franks' path."}]},
        {"lemma": "visszavonulás", "pos": "noun", "cefr": "B1", "translation": "retreat", "examples": [{"hungarian": "A színlelt visszavonulás tőrbe csalta az ellenséget.", "english": "The feigned retreat lured the enemy into a trap."}]},
        {"lemma": "nehézpáncélos", "pos": "adj", "cefr": "B1", "translation": "heavy-armoured", "examples": [{"hungarian": "A nehézpáncélos lovasság lassabban mozgott.", "english": "The heavy-armoured cavalry moved more slowly."}]},
        {"lemma": "határfolyó", "pos": "noun", "cefr": "B1", "translation": "border river", "examples": [{"hungarian": "A Lajta lett a nyugati határfolyó évszázadokon át.", "english": "The Leitha became the western border river for centuries."}]},
        {"lemma": "megsemmisít", "pos": "verb", "cefr": "B1", "translation": "to annihilate / destroy", "examples": [{"hungarian": "A magyar íjászok megsemmisítették a támadó sereget.", "english": "The Hungarian archers destroyed the attacking army."}]},
        {"lemma": "berendezkedik", "pos": "verb", "cefr": "B1", "translation": "to settle in / establish oneself", "examples": [{"hungarian": "A törzsek békésen berendezkedtek az új földeken.", "english": "The tribes settled in peacefully in the new lands."}]},
        {"lemma": "kijelöl", "pos": "verb", "cefr": "B1", "translation": "to designate / mark out", "examples": [{"hungarian": "A szerződés kijelölte az ország határait.", "english": "The treaty marked out the country's borders."}]},
        {"lemma": "fegyelmezett", "pos": "adj", "cefr": "B1", "translation": "disciplined", "examples": [{"hungarian": "A fegyelmezett íjászcsapatok pontosan követték a parancsot.", "english": "The disciplined archer troops followed the order precisely."}]}
    ]
})

write_json(GRAMMAR_DIR / "b1-honfoglalas-04-tobb-szereplo-miutan-mielott-gr.json", {
    "title": "Összetett mondatok több szereplővel és időviszonyokkal",
    "level": "B1",
    "rules": [
        {
            "id": "multi-actor-temporal",
            "title": "Multiple Actors Across Clauses",
            "text": "When the subject changes between the subordinate and main clauses, state both subjects explicitly: *Miután a frankok megtámadták a határt, Árpád serege ellentámadásba lendült.* (After the Franks attacked the border, Árpád's army mounted a counter-attack.)",
            "tip": "Hungarian subject pronoun dropping (*pro-drop*) applies only when the subject is obvious and unchanged."
        },
        {
            "id": "adverbials-instrument",
            "title": "Instrumental Endings (-val / -vel) in Military Tactics",
            "text": "Describing weapons and methods uses *-val / -vel* with assimilation: *íj-jal, szablyá-val, csel-lel, visszavonulás-sal*.",
            "tip": "Final consonant doubles: *íj + val = íjjal*, *csel + vel = csellel*."
        }
    ],
    "examples": [
        {"spanish": "Miután a bajor sereg átlépte a határt, a magyarok csapdába csalták őket.", "english": "After the Bavarian army crossed the border, the Magyars lured them into a trap."},
        {"spanish": "A lovasok íjakkal és szablyákkal harcoltak a pozsonyi csatában.", "english": "The horsemen fought with bows and sabres in the Battle of Pozsony."},
        {"spanish": "Mielőtt a frankok felocsúdhattak volna, a magyarok bekerítették a tábort.", "english": "Before the Franks could recover, the Magyars encircled the camp."}
    ]
})

write_json(EXERCISES_DIR / "b1-honfoglalas-04-ex.json", {
    "exercises": [
        {
            "id": "b1-honfoglalas-04.ex01",
            "type": "multiple-choice",
            "title": "A pozsonyi csata éve",
            "instruction": "Mikor győzték le a magyarok a frank sereget Pozsonynál?",
            "question": "Melyik évszámhoz kötődik a pozsonyi csata diadala?",
            "options": ["907", "1000", "1222", "1456"],
            "correctIndex": 0,
            "explanation": "A pozsonyi csata 907-ben zajlott le.",
            "teaches": ["pozsonyi-csata", "diadal"]
        },
        {
            "id": "b1-honfoglalas-04.ex02",
            "type": "fill-blank",
            "title": "Haditaktika",
            "instruction": "Egészítsd ki a mondatot!",
            "sentence": "A magyar lovasok a színlelt ___ segítségével csapdába csalták a nehézpáncélos lovagokat.",
            "correctAnswer": "visszavonulás",
            "options": ["visszavonulás", "alvás", "tánc", "ünneplés"],
            "teaches": ["visszavonulas", "harcmodor"]
        },
        {
            "id": "b1-honfoglalas-04.ex03",
            "type": "sentence-builder",
            "title": "Pozsonyi győzelem",
            "instruction": "Állítsd össze a mondatot!",
            "words": ["A", "pozsonyi", "csata", "biztosította", "a", "magyarok", "végleges", "megmaradását."],
            "correctSentence": "A pozsonyi csata biztosította a magyarok végleges megmaradását.",
            "english": "The Battle of Pozsony ensured the permanent survival of the Magyars.",
            "teaches": ["megmaradas", "diadal"]
        },
        {
            "id": "b1-honfoglalas-04.ex04",
            "type": "multiple-choice",
            "title": "Nyugati határok",
            "instruction": "Melyik folyó vált a Magyar Királyság nyugati határává 907 után?",
            "question": "Hol húzódott a védett nyugati határvonal?",
            "options": ["A Lajta folyónál", "A Szajna folyónál", "A Temze folyónál", "A Rajna torkolatánál"],
            "correctIndex": 0,
            "explanation": "A Lajta folyó vált a magyar állam történelmi nyugati határává.",
            "teaches": ["hatarfolyo", "kijelol"]
        },
        {
            "id": "b1-honfoglalas-04.ex05",
            "type": "fill-blank",
            "title": "Eszközhatározó (-val/-vel)",
            "instruction": "Válaszd ki a helyes alakot!",
            "sentence": "A magyar harcosok félelmetes visszacsapó ___ harcoltak.",
            "correctAnswer": "íjakkal",
            "options": ["íjakkal", "íjban", "íjtól", "íjnál"],
            "teaches": ["harcmodor"]
        },
        {
            "id": "b1-honfoglalas-04.ex06",
            "type": "sentence-builder",
            "title": "Frank támadás elhárítása",
            "instruction": "Rendezd helyes sorrendbe a szavakat!",
            "words": ["A", "fegyelmezett", "magyar", "sereg", "megsemmisítette", "a", "támadókat."],
            "correctSentence": "A fegyelmezett magyar sereg megsemmisítette a támadókat.",
            "english": "The disciplined Hungarian army destroyed the attackers.",
            "teaches": ["megsemmisit", "fegyelmezett"]
        },
        {
            "id": "b1-honfoglalas-04.ex07",
            "type": "multiple-choice",
            "title": "A birtokbavétel teljessé válása",
            "instruction": "Mikor foglalták el a magyarok a Dunántúlt?",
            "question": "Melyik évben fejeződött be a Dunántúl birtokbavétele?",
            "options": ["900-ban", "1500-ban", "1900-ban", "800-ban"],
            "correctIndex": 0,
            "explanation": "900-ban a magyar seregek elfoglalták a Dunántúlt, ezzel teljessé vált a medence birtokbavétele.",
            "teaches": ["berendezkedik", "birtokba-vesz"]
        },
        {
            "id": "b1-honfoglalas-04.ex08",
            "type": "fill-blank",
            "title": "Gyors bekerítés",
            "instruction": "Egészítsd ki a mondatot!",
            "sentence": "A gyors ___ segítségével a könnyűlovasság elvágta az ellenség menekülési útját.",
            "correctAnswer": "bekerítés",
            "options": ["bekerítés", "levelezés", "főzés", "olvasás"],
            "teaches": ["bekerites"]
        }
    ]
})

write_json(LESSONS_DIR / "b1-honfoglalas-04.json", make_lesson(
    "lesson.b1.honfoglalas-04",
    "Birtokbavétel és a pozsonyi csata (Conquest & Pozsony - 907)",
    "Több szereplős időhatározói szerkezetek",
    [
        "In this fourth lesson, we examine the final consolidation of the Carpathian Basin (895–900) and the pivotal Battle of Pozsony (907).",
        "You will learn about the decisive military victory that annihilated the East Frankish invasion army and established Hungary's western border along the Leitha (*Lajta*) river.",
        "We also practice complex multi-actor time clauses and the instrumental case (*-val / -vel*) for military equipment."
    ],
    [
        "I can explain the strategic importance of the Battle of Pozsony (907) for the survival of the Hungarian homeland.",
        "I can describe the nomadic equestrian battle tactics (feigned retreat, mounted archery).",
        "I can state the historical role of the Leitha river (*Lajta*) as Hungary's western border.",
        "I can construct clear sentences with changing subjects across clauses."
    ],
    "stories/world/b1/b1-honfoglalas-04-birtokbavetel.json",
    "vocabulary/b1/b1-honfoglalas-04-voc.json",
    "grammar/b1/b1-honfoglalas-04-tobb-szereplo-miutan-mielott-gr.json",
    "exercises/b1/b1-honfoglalas-04-ex.json",
    [f"b1-honfoglalas-04.ex{i:02d}" for i in range(1, 9)]
))

# -----------------
# Lesson 5: A kalandozások kora és Augsburg
# -----------------
write_json(STORIES_DIR / "b1-honfoglalas-05-nemzetiemlekezet.json", make_story(
    "story.b1.honfoglalas.05",
    "A kalandozások kora és az augsburgi csata (955)",
    "The era of European raids (*kalandozások*), the famous prayer 'A sagittis Hungarorum...', the 955 Battle of Augsburg, and the strategic turn toward Christian statehood under Grand Prince Géza.",
    "Nyugat-Európa és Székesfehérvár / Esztergom",
    ["összefoglaló kötőszók és következtetés"],
    ["Kalandozások kora", "Augsburgi csata 955", "Történelmi fordulat"],
    [
        "A honfoglalást követő évtizedekben, a 10. század első felében a magyar törzsek számos katonai hadjáratot indítottak Nyugat- és Dél-Európa felé. Ezt az időszakot a történetírás kalandozások korának nevezi.",
        "A magyar lovascsapatok eljutottak a mai Németország, Franciaország, Olaszország, sőt még az Ibériai-félsziget és Bizánc területére is, zsákmányt és adót szedve a helyi fejedelmektől.",
        "A nyugati kolostorokban a híres könyörgést mondták: 'A magyarok nyilaitól ments meg, Uram, minket!' (A sagittis Hungarorum libera nos, Domine!).",
        "A kalandozásoknak a 955-ös augsburgi (lech-mezei) csata vetett véget, ahol I. Ottó német király nehézlovassága vereséget mért a magyar főseregre.",
        "A vereség világossá tette a magyar vezetők számára, hogy a nomád rablóhadjáratok kora lejárt: a megmaradáshoz a keresztény hit felvétele és egy szilárd, letelepedett európai állam felépítése szükséges."
    ],
    [
        {"lemma": "kalandozás", "pos": "noun", "cefr": "B1", "gloss": "raids / roaming campaigns (10th c.)"},
        {"lemma": "zsákmány", "pos": "noun", "cefr": "B1", "gloss": "booty / plunder"},
        {"lemma": "adó", "pos": "noun", "cefr": "B1", "gloss": "tribute / tax"},
        {"lemma": "történelmi fordulat", "pos": "noun", "cefr": "B1", "gloss": "historic turning point"}
    ],
    [
        {
            "question": "Mit jelent a 'kalandozások kora' a magyar történelemben?",
            "options": ["A 10. századi nyugat- és dél-európai hadjáratok időszakát", "A 19. századi vasútépítést", "A római császárok békés utazásait", "A magyar űrhajózási programot"],
            "correctIndex": 0,
            "explanation": "A kalandozások kora a 10. századi zsákmányszerző és adószedő hadjáratok korszaka volt."
        },
        {
            "question": "Melyik csata vetett véget a nyugati kalandozó hadjáratoknak 955-ben?",
            "options": ["Az augsburgi (lech-mezei) csata", "A mohácsi csata", "A waterlooi csata", "A rigómezei csata"],
            "correctIndex": 0,
            "explanation": "955-ben az augsburgi vereség zárta le a nyugat-európai hadjáratokat."
        },
        {
            "question": "Milyen történelmi következtetést vontak le a magyar vezetők Augsburg után?",
            "options": ["Hogy fel kell venni a kereszténységet és szilárd európai államot kell alapítani", "Hogy vissza kell költözni az Urál mögé", "Hogy fel kell adni a mezőgazdaságot", "Hogy hadat kell üzenni az egész világnak egyszerre"],
            "correctIndex": 0,
            "explanation": "Augsburg után Géza fejedelem felismerte, hogy a kereszténység és a letelepedett európai királyság a megmaradás egyetlen útja."
        }
    ]
))

write_json(VOCAB_DIR / "b1-honfoglalas-05-voc.json", {
    "title": "A kalandozások kora és az augsburgi csata",
    "words": [
        {"lemma": "kalandozás", "pos": "noun", "cefr": "B1", "translation": "raiding campaign", "examples": [{"hungarian": "A kalandozások kora fél évszázadon át tartott.", "english": "The era of raids lasted for half a century."}]},
        {"lemma": "zsákmány", "pos": "noun", "cefr": "B1", "translation": "booty / plunder", "examples": [{"hungarian": "A hadjáratokból gazdag zsákmánnyal tértek haza.", "english": "They returned home from the campaigns with rich plunder."}]},
        {"lemma": "adó", "pos": "noun", "cefr": "B1", "translation": "tribute / tax", "examples": [{"hungarian": "A fejedelmek rendszeres adót fizettek a békéért.", "english": "The princes paid regular tribute for peace."}]},
        {"lemma": "könyörgés", "pos": "noun", "cefr": "B1", "translation": "plea / prayer", "examples": [{"hungarian": "A templomokban könyörgést mondtak a védelemért.", "english": "In the churches they recited a plea for protection."}]},
        {"lemma": "vereség", "pos": "noun", "cefr": "B1", "translation": "defeat", "examples": [{"hungarian": "Az augsburgi vereség megváltoztatta a politikát.", "english": "The defeat at Augsburg changed politics."}]},
        {"lemma": "történelmi fordulat", "pos": "noun", "cefr": "B1", "translation": "historical turning point", "examples": [{"hungarian": "Ez a csata hozta el a nagy történelmi fordulatot.", "english": "This battle brought about the great historical turning point."}]},
        {"lemma": "kereszténység", "pos": "noun", "cefr": "B1", "translation": "Christianity", "examples": [{"hungarian": "A kereszténység felvétele biztosította az integrációt.", "english": "Adopting Christianity ensured integration."}]},
        {"lemma": "megmaradás", "pos": "noun", "cefr": "B1", "translation": "survival", "examples": [{"hungarian": "A letelepedés volt a tartós megmaradás záloga.", "english": "Settling down was the pledge of lasting survival."}]},
        {"lemma": "hadjárat", "pos": "noun", "cefr": "B1", "translation": "military campaign", "examples": [{"hungarian": "Messzi hadjáratokat vezettek nyugatra és délre.", "english": "They led distant military campaigns to the west and south."}]},
        {"lemma": "felismer", "pos": "verb", "cefr": "B1", "translation": "to realize / recognize", "examples": [{"hungarian": "Géza fejedelem felismerte a béke fontosságát.", "english": "Grand Prince Géza recognized the importance of peace."}]},
        {"lemma": "lecsillapodik", "pos": "verb", "cefr": "B1", "translation": "to calm down / subside", "examples": [{"hungarian": "A harcok lecsillapodtak a 10. század végére.", "english": "The fights calmed down by the end of the 10th century."}]},
        {"lemma": "nyíl", "pos": "noun", "cefr": "B1", "translation": "arrow", "examples": [{"hungarian": "A magyarok gyors nyilai rettegésben tartották Európát.", "english": "The swift arrows of the Magyars held Europe in terror."}]}
    ]
})

write_json(GRAMMAR_DIR / "b1-honfoglalas-05-synthesis-gr.json", {
    "title": "Következtető kötőszók és a történelmi szintézis",
    "level": "B1",
    "rules": [
        {
            "id": "consecutive-conjunctions",
            "title": "Expressing Conclusions and Results",
            "text": "Conclude historical analyses using: *ezért* (therefore), *ennek következtében* (consequently), *így* (thus), *tehát* (hence): *A hadjáratok lezárultak, ezért a békés építkezés kezdődött.* (The raids ended, therefore peaceful construction began.)",
            "tip": "*Ezért* connects two independent clauses or begins a new sentence."
        },
        {
            "id": "purpose-clauses",
            "title": "Purpose Clauses with 'azért, hogy' + Subjunctive",
            "text": "Express purpose and historical intent with *azért, hogy* + subjunctive (*-jon / -jen*): *Géza békét kötött azért, hogy megmentse a népét.* (Géza made peace in order to save his people.)",
            "tip": "Subjunctive verbs express intent, purpose, and goal."
        }
    ],
    "examples": [
        {"spanish": "Augsburg után világossá vált a helyzet, ezért Géza nyugati hittérítőket hívott.", "english": "After Augsburg the situation became clear, therefore Géza invited Western missionaries."},
        {"spanish": "Békét kötöttek a német császárral azért, hogy megvédjék az országot.", "english": "They concluded peace with the German Emperor in order to protect the country."},
        {"spanish": "A kalandozások lezárultak, így megkezdődhetett az államalapítás.", "english": "The raids came to an end, thus state foundation could begin."}
    ]
})

write_json(EXERCISES_DIR / "b1-honfoglalas-05-ex.json", {
    "exercises": [
        {
            "id": "b1-honfoglalas-05.ex01",
            "type": "multiple-choice",
            "title": "Az augsburgi csata",
            "instruction": "Melyik évben zárta le az augsburgi csata a nyugati kalandozásokat?",
            "question": "Mikor történt az augsburgi vereség?",
            "options": ["955-ben", "895-ben", "1000-ben", "1241-ben"],
            "correctIndex": 0,
            "explanation": "955-ben zajlott le az augsburgi csata I. Ottó német király ellen.",
            "teaches": ["vereseg", "kalandozas"]
        },
        {
            "id": "b1-honfoglalas-05.ex02",
            "type": "fill-blank",
            "title": "A híres könyörgés",
            "instruction": "Egészítsd ki a mondatot!",
            "sentence": "A nyugati templomokban így könyörögtek: 'A magyarok ___ ments meg, Uram, minket!'",
            "correctAnswer": "nyilaitól",
            "options": ["nyilaitól", "hajóitól", "könyveitől", "zenéjétől"],
            "teaches": ["nyil", "konyorges"]
        },
        {
            "id": "b1-honfoglalas-05.ex03",
            "type": "sentence-builder",
            "title": "Történelmi fordulat",
            "instruction": "Állítsd össze a mondatot!",
            "words": ["Augsburg", "után", "megkezdődött", "a", "keresztény", "állam", "kiépítése."],
            "correctSentence": "Augsburg után megkezdődött a keresztény állam kiépítése.",
            "english": "After Augsburg, the construction of the Christian state began.",
            "teaches": ["tortenelmi-fordulat", "keresztenyseg"]
        },
        {
            "id": "b1-honfoglalas-05.ex04",
            "type": "multiple-choice",
            "title": "Géza fejedelem felismerése",
            "instruction": "Mit ismert fel Géza fejedelem a 10. század végén?",
            "question": "Mi volt Géza fejedelem legfőbb politikai döntése?",
            "options": ["Nyugati hittérítőket hívott és békét kötött a német császárral", "Újabb rablóhadjáratokat indított Spanyolországba", "Eladta a Kárpát-medencét a bizánciaknak", "Megtiltotta a mezőgazdaságot"],
            "correctIndex": 0,
            "explanation": "Géza felismerte a kereszténység és a nyugati integráció elengedhetetlenségét.",
            "teaches": ["felismer", "keresztenyseg"]
        },
        {
            "id": "b1-honfoglalas-05.ex05",
            "type": "fill-blank",
            "title": "Következtetés (ezért)",
            "instruction": "Válaszd ki a helyes kötőszót!",
            "sentence": "A kalandozások veszélyessé váltak, ___ a magyarok a letelepedett életmódra tértek át.",
            "correctAnswer": "ezért",
            "options": ["ezért", "bár", "pedig", "hanem"],
            "teaches": ["tortenelmi-fordulat"]
        },
        {
            "id": "b1-honfoglalas-05.ex06",
            "type": "sentence-builder",
            "title": "Célhatározó (azért, hogy)",
            "instruction": "Rendezd helyes sorrendbe a szavakat!",
            "words": ["Géza", "békét", "kötött", "azért,", "hogy", "megmentse", "az", "országot."],
            "correctSentence": "Géza békét kötött azért, hogy megmentse az országot.",
            "english": "Géza concluded peace in order to save the country.",
            "teaches": ["megmaradas", "felismer"]
        },
        {
            "id": "b1-honfoglalas-05.ex07",
            "type": "multiple-choice",
            "title": "A hadjáratok célja",
            "instruction": "Mi volt a kalandozások fő célja?",
            "question": "Miért indítottak hadjáratokat a magyar törzsek Nyugat-Európába?",
            "options": ["Zsákmányszerzésért, adószedésért és szövetségesi segítségért", "Új kontinensek felfedezéséért", "Hogy könyvtárakat építsenek Rómában", "Hogy elhagyják a Kárpát-medencét"],
            "correctIndex": 0,
            "explanation": "A hadjáratok célja zsákmányszerzés, rendszeres adószedés és a katonai erő demonstrálása volt.",
            "teaches": ["zskmany", "ado", "hadjarat"]
        },
        {
            "id": "b1-honfoglalas-05.ex08",
            "type": "fill-blank",
            "title": "Tartós megmaradás",
            "instruction": "Egészítsd ki a mondatot!",
            "sentence": "A keresztény államalapítás biztosította a magyar nemzet európai ___.",
            "correctAnswer": "megmaradását",
            "options": ["megmaradását", "eltűnését", "elfelejtését", "elsüllyedését"],
            "teaches": ["megmaradas"]
        }
    ]
})

write_json(LESSONS_DIR / "b1-honfoglalas-05.json", make_lesson(
    "lesson.b1.honfoglalas-05",
    "A kalandozások kora és Augsburg (Raids & Turning Point - 955)",
    "Következtető kötőszók és a történelmi szintézis",
    [
        "In this fifth lesson of Unit 3, we explore the era of European campaigns (*kalandozások kora*), the decisive 955 Battle of Augsburg, and the strategic turn under Grand Prince Géza.",
        "You will learn how the cessation of raids prompted the integration of Hungary into Christian Europe, setting the stage for Saint Stephen's state foundation.",
        "We also practice consecutive connectors (*ezért, így*) and purpose clauses (*azért, hogy*)."
    ],
    [
        "I can describe the era of 10th-century raids and recall the prayer 'A sagittis Hungarorum...'.",
        "I can explain the significance of the 955 Battle of Augsburg as a turning point.",
        "I can summarize Grand Prince Géza's policies of peace and opening to Christian Europe.",
        "I can construct purpose and result clauses (*azért, hogy; ezért*) accurately."
    ],
    "stories/world/b1/b1-honfoglalas-05-nemzetiemlekezet.json",
    "vocabulary/b1/b1-honfoglalas-05-voc.json",
    "grammar/b1/b1-honfoglalas-05-synthesis-gr.json",
    "exercises/b1/b1-honfoglalas-05-ex.json",
    [f"b1-honfoglalas-05.ex{i:02d}" for i in range(1, 9)]
))

# -----------------
# Unit 3 Consolidation
# -----------------
write_json(STORIES_DIR / "b1-honfoglalas.json", make_story(
    "story.b1.honfoglalas",
    "A honfoglalás és a magyar állam bölcsője (895)",
    "A grand narrative of the Magyar Conquest: from the Uralic migration and the Blood Oath at Pusztaszer, through the Verecke Pass in 895, the triumph at Pozsony in 907, to the turning point at Augsburg in 955.",
    "Kárpát-medence",
    ["összetett mondatszerkezetek", "történeti narratíva"],
    ["Honfoglalás", "Vérszerződés", "Pozsonyi csata", "Államalapítás felé"],
    [
        "A 9. század végén a magyar törzsek hosszú kelet-európai vándorlás után elérkeztek történelmük legfontosabb fordulópontjához. Etelközben a hét vezér vérszerződéssel pecsételte meg a szövetséget, Álmos és Árpád vezetését választva.",
        "895-ben Árpád főserege a Vereckei-hágón kelt át a Kárpátok koszorúján, és birtokba vette a Felső-Tisza gazdag legelőit és Erdély völgyeit, majd 900-ra a Dunántúlt is.",
        "A fiatal hazát 907-ben érte a legnagyobb veszély, de a pozsonyi csatában a magyar lovas íjászok tönkreverték a túlerőben lévő frank inváziós sereget, évszázadokra kijelölve a Lajta menti nyugati határt.",
        "A 10. század első felének zsákmányszerző kalandozásai után a 955-ös augsburgi vereség világossá tette: a nomád harcmodor helyett a letelepedett keresztény állam jelenti a megmaradás egyetlen útját.",
        "A honfoglalás nem csupán egy terület elfoglalása volt, hanem egy ezeréves európai nemzet és állam megszületésének első fejezete."
    ],
    [
        {"lemma": "honfoglalás", "pos": "noun", "cefr": "B1", "gloss": "conquest of the homeland (895)"},
        {"lemma": "vérszerződés", "pos": "noun", "cefr": "B1", "gloss": "blood oath"},
        {"lemma": "államalapítás", "pos": "noun", "cefr": "B1", "gloss": "state foundation"},
        {"lemma": "megmaradás", "pos": "noun", "cefr": "B1", "gloss": "survival / perpetuity"}
    ],
    [
        {
            "question": "Melyik évszám jelöli a magyar honfoglalást?",
            "options": ["895", "1000", "1241", "1526"],
            "correctIndex": 0,
            "explanation": "A honfoglalás éve 895, amikor Árpád vezetésével a törzsek átkeltek a Kárpátokon."
        },
        {
            "question": "Melyik csata biztosította a honfoglalás eredményeit 907-ben a frank támadással szemben?",
            "options": ["A pozsonyi csata", "Az augsburgi csata", "A muhi csata", "A nándorfehérvári csata"],
            "correctIndex": 0,
            "explanation": "A 907-es pozsonyi csata biztosította a Kárpát-medence végleges megvédését."
        },
        {
            "question": "Milyen irányt szabott Géza fejedelem a magyarságnak a kalandozások lezárulása után?",
            "options": ["A kereszténység felvételét és a nyugat-európai típusú államszervezést", "A nomád vándorlás folytatását Ázsia felé", "A teljes elzárkózást minden szomszédtól", "A tengeri hadiflotta építését"],
            "correctIndex": 0,
            "explanation": "Géza fejedelem megnyitotta az utat a kereszténység és a nyugati integráció előtt."
        }
    ]
))

u3_cons_ex = []
u3_cons_ex.append({
    "id": "b1-honfoglalas-consolidation.ex01",
    "type": "multiple-choice",
    "title": "A honfoglalás éve",
    "instruction": "Melyik évben kezdődött a magyar honfoglalás?",
    "question": "Mikor keltek át a magyarok a Vereckei-hágón?",
    "options": ["895-ben", "1000-ben", "1222-ben", "1848-ban"],
    "correctIndex": 0,
    "explanation": "A honfoglalás éve 895.",
    "teaches": ["honfoglalas", "atkeles"]
})
u3_cons_ex.append({
    "id": "b1-honfoglalas-consolidation.ex02",
    "type": "fill-blank",
    "title": "A vérszerződés esküje",
    "instruction": "Egészítsd ki a mondatot!",
    "sentence": "A hét magyar törzs vezérei ___ pecsételték meg szövetségüket.",
    "correctAnswer": "vérszerződéssel",
    "options": ["vérszerződéssel", "aranygyűrűvel", "papírlevéllel", "békekonferenciával"],
    "teaches": ["verszerzodes", "torzsszovetseg"]
})
u3_cons_ex.append({
    "id": "b1-honfoglalas-consolidation.ex03",
    "type": "sentence-builder",
    "title": "Árpád vezér",
    "instruction": "Állítsd össze a mondatot!",
    "words": ["Árpád", "vezér", "vezette", "a", "fősereget", "a", "Vereckei-hágón", "keresztül."],
    "correctSentence": "Árpád vezér vezette a fősereget a Vereckei-hágón keresztül.",
    "english": "Chieftain Árpád led the main army across the Verecke Pass.",
    "teaches": ["fosereg", "hago"]
})
u3_cons_ex.append({
    "id": "b1-honfoglalas-consolidation.ex04",
    "type": "multiple-choice",
    "title": "Nyelvcsalád",
    "instruction": "Melyik nyelvcsaládba tartozik a magyar?",
    "question": "Mely nyelvcsalád tagja a magyar nyelv?",
    "options": ["Finnugor (uráli)", "Szláv", "Germán", "Újlatin"],
    "correctIndex": 0,
    "explanation": "A magyar a finnugor (uráli) nyelvcsalád tagja.",
    "teaches": ["nyelvcsalad", "oshaza"]
})
u3_cons_ex.append({
    "id": "b1-honfoglalas-consolidation.ex05",
    "type": "fill-blank",
    "title": "Pozsonyi diadal",
    "instruction": "Egészítsd ki a mondatot!",
    "sentence": "A 907-es ___ csata megvédte a Kárpát-medencét a frank inváziótól.",
    "correctAnswer": "pozsonyi",
    "options": ["pozsonyi", "párizsi", "londoni", "bécsi"],
    "teaches": ["pozsonyi-csata", "diadal"]
})
u3_cons_ex.append({
    "id": "b1-honfoglalas-consolidation.ex06",
    "type": "sentence-builder",
    "title": "Miután birtokba vették",
    "instruction": "Rendezd helyes sorrendbe a szavakat!",
    "words": ["Miután", "birtokba", "vették", "a", "medencét,", "berendezkedtek", "az", "új", "hazában."],
    "correctSentence": "Miután birtokba vették a medencét, berendezkedtek az új hazában.",
    "english": "After they took possession of the basin, they settled in the new homeland.",
    "teaches": ["birtokba-vesz", "berendezkedik"]
})
u3_cons_ex.append({
    "id": "b1-honfoglalas-consolidation.ex07",
    "type": "multiple-choice",
    "title": "Krónikás Anonymus",
    "instruction": "Ki írta a Gesta Hungarorumot?",
    "question": "Melyik névtelen jegyző örökítette meg a honfoglalás mondáit?",
    "options": ["Anonymus", "Kossuth Lajos", "Petőfi Sándor", "Széchenyi István"],
    "correctIndex": 0,
    "explanation": "Anonymus, Béla király névtelen jegyzője írta meg a Gesta Hungarorumot.",
    "teaches": ["kronika", "jegyzo"]
})
u3_cons_ex.append({
    "id": "b1-honfoglalas-consolidation.ex08",
    "type": "fill-blank",
    "title": "Augsburgi fordulat",
    "instruction": "Válaszd ki a megfelelő évszámot!",
    "sentence": "A kalandozó hadjáratok a ___ augsburgi vereséggel értek véget.",
    "correctAnswer": "955-ös",
    "options": ["955-ös", "1848-as", "1956-os", "1222-es"],
    "teaches": ["vereseg", "kalandozas"]
})
u3_cons_ex.append({
    "id": "b1-honfoglalas-consolidation.ex09",
    "type": "sentence-builder",
    "title": "A sagittis Hungarorum",
    "instruction": "Állítsd össze a mondatot!",
    "words": ["A", "magyarok", "nyilaitól", "rettegtek", "Nyugat-Európában."],
    "correctSentence": "A magyarok nyilaitól rettegtek Nyugat-Európában.",
    "english": "They feared the arrows of the Magyars in Western Europe.",
    "teaches": ["nyil", "konyorges"]
})
u3_cons_ex.append({
    "id": "b1-honfoglalas-consolidation.ex10",
    "type": "multiple-choice",
    "title": "Csatlakozott nép",
    "instruction": "Kik csatlakoztak a hét magyar törzshöz?",
    "question": "Melyik kazár eredetű népcsoport vált a hadsereg elővédjévé?",
    "options": ["A kabarok", "A szászok", "A vikingek", "A kelták"],
    "correctIndex": 0,
    "explanation": "A kabarok csatlakoztak a magyar törzsszövetséghez és alkották az elővédet.",
    "teaches": ["eloved", "torzsszovetseg"]
})
u3_cons_ex.append({
    "id": "b1-honfoglalas-consolidation.ex11",
    "type": "fill-blank",
    "title": "Nyugati határfolyó",
    "instruction": "Egészítsd ki a mondatot!",
    "sentence": "A 907-es győzelem után a ___ folyó lett az ország nyugati határa.",
    "correctAnswer": "Lajta",
    "options": ["Lajta", "Duna", "Tisza", "Dráva"],
    "teaches": ["hatarfolyo", "kijelol"]
})
u3_cons_ex.append({
    "id": "b1-honfoglalas-consolidation.ex12",
    "type": "sentence-builder",
    "title": "Géza fejedelem reformjai",
    "instruction": "Rendezd helyes sorrendbe a szavakat!",
    "words": ["Géza", "fejedelem", "felismerte", "a", "kereszténység", "felvételének", "szükségességét."],
    "correctSentence": "Géza fejedelem felismerte a kereszténység felvételének szükségességét.",
    "english": "Grand Prince Géza recognized the necessity of adopting Christianity.",
    "teaches": ["felismer", "keresztenyseg"]
})
u3_cons_ex.append({
    "id": "b1-honfoglalas-consolidation.ex13",
    "type": "multiple-choice",
    "title": "Harcmodor",
    "instruction": "Milyen harcmodort alkalmaztak a honfoglaló magyarok?",
    "question": "Mi jellemezte a magyar seregek taktikáját a 10. században?",
    "options": ["Könnyűlovas íjászat, színlelt visszavonulás és gyors bekerítés", "Nehéz gőzhajók használata", "Kizárólag kézzel vívott kardpárbajok", "Helyhez kötött várvédelem"],
    "correctIndex": 0,
    "explanation": "A magyarok nomád könnyűlovassággal, visszacsapó íjakkal és mozgékony harcmodorral győztek.",
    "teaches": ["harcmodor", "visszavonulas"]
})
u3_cons_ex.append({
    "id": "b1-honfoglalas-consolidation.ex14",
    "type": "fill-blank",
    "title": "Pusztaszeri emlékhely",
    "instruction": "Egészítsd ki a mondatot!",
    "sentence": "A nemzeti emlékezet szerint a vezérek ___ tartották meg az első gyűlést.",
    "correctAnswer": "Pusztaszeren",
    "options": ["Pusztaszeren", "Bécsben", "Párizsban", "Londonban"],
    "teaches": ["gyules", "emlekezet"]
})
u3_cons_ex.append({
    "id": "b1-honfoglalas-consolidation.ex15",
    "type": "sentence-builder",
    "title": "Mielőtt beléptek volna",
    "instruction": "Állítsd össze a mondatot!",
    "words": ["Mielőtt", "beléptek", "volna", "a", "hágón,", "Etelközben", "éltek."],
    "correctSentence": "Mielőtt beléptek volna a hágón, Etelközben éltek.",
    "english": "Before they entered through the pass, they lived in Etelköz.",
    "teaches": ["oshaza", "hago"]
})
u3_cons_ex.append({
    "id": "b1-honfoglalas-consolidation.ex16",
    "type": "multiple-choice",
    "title": "Kettős fejedelemség",
    "instruction": "Melyik volt a két méltóság a kazár mintájú vezetésben?",
    "question": "Hogyan nevezték a szakrális fejedelmet és a katonai vezért?",
    "options": ["Kende (szakrális) és Gyula (katonai)", "Császár és Polgármester", "Pap és Kereskedő", "Lovag és Jobbágy"],
    "correctIndex": 0,
    "explanation": "A kende volt a szakrális főfejedelem, a gyula pedig a hadsereg parancsnoka.",
    "teaches": ["fejedelemseg"]
})
u3_cons_ex.append({
    "id": "b1-honfoglalas-consolidation.ex17",
    "type": "fill-blank",
    "title": "Örök hűség",
    "instruction": "Egészítsd ki a mondatot!",
    "sentence": "A vezérek örökös ___ fogadtak Árpád nemzetségének.",
    "correctAnswer": "hűséget",
    "options": ["hűséget", "haragot", "háborút", "adósságot"],
    "teaches": ["huseg", "megeskuszik"]
})
u3_cons_ex.append({
    "id": "b1-honfoglalas-consolidation.ex18",
    "type": "sentence-builder",
    "title": "Békés építkezés",
    "instruction": "Rendezd helyes sorrendbe a mondatrészeket!",
    "words": ["A", "harcok", "után", "megkezdődött", "a", "békés", "államépítés."],
    "correctSentence": "A harcok után megkezdődött a békés államépítés.",
    "english": "After the fights, peaceful state building began.",
    "teaches": ["allamalapitas", "tortenelmi-fordulat"]
})
u3_cons_ex.append({
    "id": "b1-honfoglalas-consolidation.ex19",
    "type": "multiple-choice",
    "title": "Törzsek száma",
    "instruction": "Hány magyar törzs vett részt a vérszerződésben?",
    "question": "Hány törzs kötött szövetséget Etelközben?",
    "options": ["7 törzs", "12 törzs", "3 törzs", "100 törzs"],
    "correctIndex": 0,
    "explanation": "A hét magyar törzs: Nyék, Megyer, Kürtgyarmat, Tarján, Jenő, Kér, Keszi.",
    "teaches": ["torzsszovetseg"]
})
u3_cons_ex.append({
    "id": "b1-honfoglalas-consolidation.ex20",
    "type": "fill-blank",
    "title": "Ezeréves örökség",
    "instruction": "Egészítsd ki a mondatot!",
    "sentence": "A honfoglalás megalapozta a magyar állam ezeréves európai ___.",
    "correctAnswer": "megmaradását",
    "options": ["megmaradását", "eltűnését", "vereségét", "felejtését"],
    "teaches": ["megmaradas", "honfoglalas"]
})

write_json(EXERCISES_DIR / "b1-honfoglalas-consolidation-ex.json", {"exercises": u3_cons_ex})

write_json(LESSONS_DIR / "b1-honfoglalas-consolidation.json", make_consolidation_lesson(
    "lesson.b1.honfoglalas-consolidation",
    "The Honfoglalás (895) - Consolidation",
    [
        "Congratulations on finishing Unit 3 of the Hungarian Citizenship Track!",
        "In this unit, you have mastered the foundational epoch of Hungarian history: the eastern migration routes, the Blood Oath (*vérszerződés*), the 895 crossing at the Verecke Pass, the decisive 907 Battle of Pozsony, and the shift from nomadic campaigns to Christian statehood after Augsburg in 955.",
        "Review your vocabulary, practice the 20 consolidation exercises, and reinforce the historical and grammatical foundations tested in the Hungarian naturalization interview."
    ],
    [
        "I can summarize the key milestones of the Honfoglalás (895, Verecke Pass, Árpád).",
        "I can explain the constitutional symbolism of the Blood Oath and the seven tribes.",
        "I can describe the Battle of Pozsony (907) and the turning point of Augsburg (955).",
        "I can accurately use complex temporal (*miután, mielőtt, miközben*) and consecutive (*ezért, így*) clauses."
    ],
    "stories/world/b1/b1-honfoglalas.json",
    "exercises/b1/b1-honfoglalas-consolidation-ex.json",
    [f"b1-honfoglalas-consolidation.ex{i:02d}" for i in range(1, 21)]
))

print("Unit 3 (b1-honfoglalas) overhaul complete!")
