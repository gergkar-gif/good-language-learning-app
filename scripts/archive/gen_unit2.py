# -*- coding: utf-8 -*-
"""
Unit 2 Overhaul: The Carpathian Basin Before the Magyars (b1-karpatmedence)
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
# Lesson 1: Korai népek
# -----------------
write_json(STORIES_DIR / "b1-karpatmedence-01-korainepek.json", make_story(
    "story.b1.karpatmedence.01",
    "A medence korai népei",
    "Who lived in the Carpathian Basin long before the Magyars arrived: the Celtic and Illyrian tribes, their crafts, and hilltop fortifications.",
    "Kárpát-medence",
    ["több alany és múlt idejű igei egyeztetés"],
    ["A medence korai népei", "Kelta kultúra"],
    [
        "Évszázadokkal a honfoglalás előtt a Kárpát-medence már virágzó, sűrűn lakott térség volt. A vaskor idején kelta és illír törzsek népesítették be a folyóvölgyeket és a termékeny síkságokat.",
        "A kelták különösen fejlett technológiával rendelkeztek: ismerték a vasolvasztást, a fazekaskorong használatát, és megerősített településeket, úgynevezett oppidumokat építettek a dombtetőkön.",
        "A régészeti feltárások szerint a kelta kézművesek és kereskedők kiterjedt kapcsolatokat ápoltak a Földközi-tenger térségével, és saját ezüstpénzt is vertek.",
        "A Kárpátok hegyvonulata már ekkor is természetes védelmet nyújtott a medence lakóinak a külső támadásokkal szemben.",
        "Ezek az ősi kultúrák gazdag régészeti leleteket és földrajzi neveket hagytak maguk után, megteremtve a térség későbbi fejlődésének alapjait."
    ],
    [
        {"lemma": "őslakos", "pos": "noun", "cefr": "B1", "gloss": "indigenous inhabitant / native"},
        {"lemma": "letelepedik", "pos": "verb", "cefr": "B1", "gloss": "to settle down"},
        {"lemma": "kézművesség", "pos": "noun", "cefr": "B1", "gloss": "craftsmanship / handicraft"},
        {"lemma": "erődítmény", "pos": "noun", "cefr": "B1", "gloss": "fortification"}
    ],
    [
        {
            "question": "Kik laktak a Kárpát-medencében a vaskorban a római hódítás előtt?",
            "options": ["Kelta és illír törzsek", "A honfoglaló magyarok", "Oszmán-török hadseregek", "Germán hercegek a 19. században"],
            "correctIndex": 0,
            "explanation": "A római kor előtt kelta és illír törzsek népesítették be a Kárpát-medencét."
        },
        {
            "question": "Milyen technológiai vívmányokat alkalmaztak a kelták?",
            "options": ["Gőzgépeket és gyárakat", "Vasolvasztást, fazekaskorongot és pénzverést", "Piramisépítést és olajfúrást", "Csak egyszerű kőszerszámokat"],
            "correctIndex": 1,
            "explanation": "A kelták ismerték a vasolvasztást, a fazekaskorongot és pénzt is vertek."
        },
        {
            "question": "Hogyan védték magukat a kelták a támadásokkal szemben?",
            "options": ["Erődített hegyi településeket (oppidumokat) építettek", "Mély tengeri árkokat ástak", "Földalatti alagutakban bújtak el", "Nem építettek semmilyen védelmet"],
            "correctIndex": 0,
            "explanation": "A kelták dombtetőkön megerősített településeket, oppidumokat hoztak létre."
        }
    ]
))

write_json(VOCAB_DIR / "b1-karpatmedence-01-voc.json", {
    "title": "A medence korai népei",
    "words": [
        {"lemma": "őslakos", "pos": "noun", "cefr": "B1", "translation": "indigenous inhabitant / native", "examples": [{"hungarian": "A kelták a térség korai őslakosai közé tartoztak.", "english": "The Celts belonged to the early native inhabitants of the region."}]},
        {"lemma": "törzs", "pos": "noun", "cefr": "B1", "translation": "tribe", "examples": [{"hungarian": "Különböző törzsek éltek a folyóvölgyekben.", "english": "Various tribes lived in the river valleys."}]},
        {"lemma": "vaskor", "pos": "noun", "cefr": "B1", "translation": "Iron Age", "examples": [{"hungarian": "A vaskor idején gyorsan fejlődött a fémfeldolgozás.", "english": "During the Iron Age, metalworking developed rapidly."}]},
        {"lemma": "letelepedik", "pos": "verb", "cefr": "B1", "translation": "to settle down", "examples": [{"hungarian": "A népek letelepedtek a termékeny vidéken.", "english": "The peoples settled down in the fertile countryside."}]},
        {"lemma": "erődítmény", "pos": "noun", "cefr": "B1", "translation": "fortification / fort", "examples": [{"hungarian": "Erős erődítményt emeltek a dombtetőre.", "english": "They erected a strong fortification on the hilltop."}]},
        {"lemma": "település", "pos": "noun", "cefr": "B1", "translation": "settlement", "examples": [{"hungarian": "A Duna partján virágzó települések jöttek létre.", "english": "Flourishing settlements were established along the banks of the Danube."}]},
        {"lemma": "kézművesség", "pos": "noun", "cefr": "B1", "translation": "handicraft / craftsmanship", "examples": [{"hungarian": "A kelta kézművesség magas színvonalat ért el.", "english": "Celtic craftsmanship reached a high standard."}]},
        {"lemma": "kereskedelem", "pos": "noun", "cefr": "B1", "translation": "trade / commerce", "examples": [{"hungarian": "A távolsági kereskedelem összekötötte a déli népekkel.", "english": "Long-distance trade connected them with southern peoples."}]},
        {"lemma": "lelet", "pos": "noun", "cefr": "B1", "translation": "archaeological find / relic", "examples": [{"hungarian": "A régészeti leletek gazdag anyagi kultúráról tanúskodnak.", "english": "The archaeological finds testify to a rich material culture."}]},
        {"lemma": "pénzverés", "pos": "noun", "cefr": "B1", "translation": "coinage / minting", "examples": [{"hungarian": "A helyi pénzverés az önálló gazdaság jele volt.", "english": "Local coinage was a sign of an independent economy."}]},
        {"lemma": "tanúskodik", "pos": "verb", "cefr": "B1", "translation": "to testify / bear witness", "examples": [{"hungarian": "A sírok díszes tárgyai virágzó életről tanúskodnak.", "english": "The ornate objects of the graves testify to a flourishing life."}]},
        {"lemma": "menedék", "pos": "noun", "cefr": "B1", "translation": "shelter / refuge", "examples": [{"hungarian": "A hegyek biztos menedéket nyújtottak a lakosságnak.", "english": "The mountains provided safe shelter for the population."}]}
    ]
})

write_json(GRAMMAR_DIR / "b1-karpatmedence-01-gr.json", {
    "title": "Múlt idejű igék és egyeztetés történeti leírásban",
    "level": "B1",
    "rules": [
        {
            "id": "past-tense-narrative",
            "title": "Past Tense in Historical Narratives",
            "text": "When narrating historical events, Hungarian uses past-tense suffixes (*-t / -tt*). When plural subjects (*kelták, törzsek*) perform an action, the verb takes plural endings (*-tak / -tek* or *-ttak / -ttek*).",
            "tip": "Distinguish between indefinite (*letelepedtek*) and definite conjugation (*felépítették az erődöt*)."
        },
        {
            "id": "locative-relations",
            "title": "Locative Expressions in History",
            "text": "Locative suffixes describe where populations lived: *-ban / -ben* (*a medencében, a völgyben*), *-n / -on / -en / -ön* (*a dombtetőn, a síkságon*), *-nál / -nél* (*a folyóknál*).",
            "tip": "Always observe back and front vowel harmony."
        }
    ],
    "examples": [
        {"spanish": "A kelta törzsek letelepedtek a termékeny Kárpát-medencében.", "english": "The Celtic tribes settled down in the fertile Carpathian Basin."},
        {"spanish": "Erős erődítményeket építettek a dombtetőkön.", "english": "They built strong fortifications on the hilltops."},
        {"spanish": "A régészeti leletek virágzó kultúráról tanúskodnak.", "english": "The archaeological finds testify to a flourishing culture."}
    ]
})

write_json(EXERCISES_DIR / "b1-karpatmedence-01-ex.json", {
    "exercises": [
        {
            "id": "b1-karpatmedence-01.ex01",
            "type": "multiple-choice",
            "title": "Korai népek a medencében",
            "instruction": "Válaszd ki a helyes választ a szöveg alapján!",
            "question": "Kik laktak a Kárpát-medencében a vaskorban a római hódítás előtt?",
            "options": ["Kelta és illír törzsek", "A honfoglaló magyarok", "Oszmán-török hadseregek", "Germán hercegek a 19. században"],
            "correctIndex": 0,
            "explanation": "A római kor előtt kelta és illír törzsek népesítették be a Kárpát-medencét.",
            "teaches": ["oslakos", "torzs", "vaskor"]
        },
        {
            "id": "b1-karpatmedence-01.ex02",
            "type": "fill-blank",
            "title": "Kelta kultúra és technológia",
            "instruction": "Egészítsd ki a mondatot a megfelelő szóval!",
            "sentence": "A kelták ismerték a vasolvasztást és a fazekaskorongot, ami fejlett ___ tanúskodik.",
            "correctAnswer": "kézművességről",
            "options": ["kézművességről", "háborúról", "repülésről", "óceánról"],
            "teaches": ["kezmuvesseg", "tanuskodik"]
        },
        {
            "id": "b1-karpatmedence-01.ex03",
            "type": "sentence-builder",
            "title": "Erődítmények a dombtetőkön",
            "instruction": "Állítsd össze a helyes mondatot a megadott szavakból!",
            "words": ["A", "kelták", "erős", "erődítményeket", "építettek", "a", "dombtetőkön."],
            "correctSentence": "A kelták erős erődítményeket építettek a dombtetőkön.",
            "english": "The Celts built strong fortifications on the hilltops.",
            "teaches": ["eroditmeny", "letelepedik"]
        },
        {
            "id": "b1-karpatmedence-01.ex04",
            "type": "multiple-choice",
            "title": "Kereskedelem és gazdaság",
            "instruction": "Válaszd ki az igaz állítást!",
            "question": "Milyen bizonyíték mutatja, hogy a kelták fejlett kereskedelmet folytattak?",
            "options": ["Pénzt vertek és távoli vidékekkel kereskedtek", "Nem volt kapcsolatuk más népekkel", "Csak cserekereskedelmet folytattak kövekkel", "Minden árut tengeri kikötőben adtak el"],
            "correctIndex": 0,
            "explanation": "A kelta pénzverés és a mediterrán leletek a távolsági kereskedelem bizonyítékai.",
            "teaches": ["penzveres", "kereskedelem"]
        },
        {
            "id": "b1-karpatmedence-01.ex05",
            "type": "fill-blank",
            "title": "Letelepedés a medencében",
            "instruction": "Válaszd ki a mondatba illő igealakot!",
            "sentence": "A törzsek a folyók közelében ___ és falvakat alapítottak.",
            "correctAnswer": "letelepedtek",
            "options": ["letelepedtek", "menekültek", "romboltak", "elúsztak"],
            "teaches": ["letelepedik", "telepules"]
        },
        {
            "id": "b1-karpatmedence-01.ex06",
            "type": "sentence-builder",
            "title": "Régészeti leletek",
            "instruction": "Rendezd helyes sorrendbe a mondatrészeket!",
            "words": ["A", "gazdag", "leletek", "virágzó", "társadalomról", "tanúskodnak."],
            "correctSentence": "A gazdag leletek virágzó társadalomról tanúskodnak.",
            "english": "The rich finds bear witness to a flourishing society.",
            "teaches": ["lelet", "tanuskodik"]
        },
        {
            "id": "b1-karpatmedence-01.ex07",
            "type": "multiple-choice",
            "title": "A hegyek szerepe",
            "instruction": "Miért nyújtott ideális otthont a Kárpát-medence?",
            "question": "Hogyan segítették a Kárpátok hegyei a letelepedett lakosságot?",
            "options": ["Természetes védelmet és menedéket nyújtottak a támadásokkal szemben", "Teljesen elzárták a vizet és a napfényt", "Lehetetlenné tették a mezőgazdaságot", "Semmilyen hatásuk nem volt a védelemre"],
            "correctIndex": 0,
            "explanation": "A hegyvonulatok természetes védőbástyaként szolgáltak a külső hódítókkal szemben.",
            "teaches": ["menedek"]
        },
        {
            "id": "b1-karpatmedence-01.ex08",
            "type": "fill-blank",
            "title": "Őslakosok emléke",
            "instruction": "Egészítsd ki a mondatot!",
            "sentence": "A kelta korai ___ emléke a földrajzi nevekben is fennmaradt.",
            "correctAnswer": "őslakosok",
            "options": ["őslakosok", "katonák", "autók", "gépek"],
            "teaches": ["oslakos"]
        }
    ]
})

write_json(LESSONS_DIR / "b1-karpatmedence-01.json", make_lesson(
    "lesson.b1.karpatmedence-01",
    "A medence korai népei (Early Peoples of the Basin)",
    "Múlt idejű igék és alany-ige egyeztetés történeti leírásban",
    [
        "Welcome to Unit 2 of the Hungarian Citizenship Track. Before exploring Hungarian national history, we examine the rich history of the Carpathian Basin before the arrival of the Magyars.",
        "In this lesson, you will learn about the Celtic and Illyrian tribes who inhabited the basin during the Iron Age, their advanced metalworking, coinage, and fortified hilltop settlements (*oppidumok*).",
        "Grammatically, we practice past tense narrative verbs and subject-verb agreements essential for discussing historical epochs in your citizenship interview."
    ],
    [
        "I can identify the early Celtic and Illyrian inhabitants of the Carpathian Basin.",
        "I can describe the technological advancements of the Iron Age such as pottery, metallurgy, and coinage.",
        "I can use past-tense plural verbs accurately in historical narratives.",
        "I can explain why the Carpathian Basin offered natural protection and fertile land for settlements."
    ],
    "stories/world/b1/b1-karpatmedence-01-korainepek.json",
    "vocabulary/b1/b1-karpatmedence-01-voc.json",
    "grammar/b1/b1-karpatmedence-01-gr.json",
    "exercises/b1/b1-karpatmedence-01-ex.json",
    [f"b1-karpatmedence-01.ex{i:02d}" for i in range(1, 9)]
))

# -----------------
# Lesson 2: Pannonia provincia
# -----------------
write_json(STORIES_DIR / "b1-karpatmedence-02-pannonia.json", make_story(
    "story.b1.karpatmedence.02",
    "Pannonia provincia és a római örökség",
    "The Roman Empire in Pannonia: the Danube limes border, paved military roads, and ancient Roman cities like Aquincum, Savaria, and Sopianae.",
    "Pannonia (Dunántúl)",
    ["helyhatározói ragok és névutók"],
    ["Római birodalom", "Pannonia városai"],
    [
        "Az időszámításunk szerinti 1. században a Római Birodalom meghódította a Dunántúlt, és megalapította Pannonia provinciát. A Duna folyó a birodalom északi és keleti határává, a híres limesszé vált.",
        "A rómaiak fejlett közigazgatást és kiváló úthálózatot építettek ki. Katonai táborok és virágzó városok jöttek létre: Aquincum a mai Óbuda területén, Savaria a mai Szombathelyen, Scarbantia Sopronban, és Sopianae Pécsen.",
        "Aquincumban vízvezeték, amfiteátrumok és padlófűtéses villák szolgálták a lakók kényelmét. Sopianae korai keresztény sírkamrái ma az UNESCO világörökség részét képezik.",
        "A rómaiak vezették be a szőlőtermesztést és a borkészítést a Balaton-felvidéken és a Szerémségben, ami a magyar borkultúra gyökereit jelenti.",
        "Bár a birodalom a népvándorlás viharaiban felbomlott, a római kőépületek és utak évszázadokon át formálták a Dunántúl arculatát."
    ],
    [
        {"lemma": "provincia", "pos": "noun", "cefr": "B1", "gloss": "province (Roman)"},
        {"lemma": "határvonal", "pos": "noun", "cefr": "B1", "gloss": "borderline / boundary"},
        {"lemma": "vízvezeték", "pos": "noun", "cefr": "B1", "gloss": "aqueduct / plumbing"},
        {"lemma": "világörökség", "pos": "noun", "cefr": "B1", "gloss": "World Heritage"}
    ],
    [
        {
            "question": "Mi volt a Duna szerepe a Római Birodalom idején?",
            "options": ["A birodalom megerősített határvonala (limes) volt", "Egy elhagyatott, néptelen mocsárvidék", "Kizárólag kereskedelmi tengeri út Ázsiába", "A birodalom legbelső folyója"],
            "correctIndex": 0,
            "explanation": "A Duna képezte a Római Birodalom északi védelmi határát, a limest."
        },
        {
            "question": "Melyik mai magyar város felel meg az ókori Aquincumnak?",
            "options": ["Budapest (Óbuda)", "Szeged", "Debrecen", "Miskolc"],
            "correctIndex": 0,
            "explanation": "Aquincum a mai Budapest (Óbuda) területén feküdt, Pannonia Inferior fővárosaként."
        },
        {
            "question": "Milyen kulturális és gazdasági hagyományt honosítottak meg a rómaiak Pannoniában?",
            "options": ["A szőlőtermesztést és borkultúrát", "A teaültetvényeket", "A kávépörkölést", "A rizstermesztést"],
            "correctIndex": 0,
            "explanation": "A rómaiak virágoztatták fel a szőlőművelést és a borkészítést a Dunántúlon."
        }
    ]
))

write_json(VOCAB_DIR / "b1-karpatmedence-02-voc.json", {
    "title": "Pannonia provincia és a római örökség",
    "words": [
        {"lemma": "provincia", "pos": "noun", "cefr": "B1", "translation": "province", "examples": [{"hungarian": "Pannonia a Római Birodalom fontos provinciája volt.", "english": "Pannonia was an important province of the Roman Empire."}]},
        {"lemma": "határvonal", "pos": "noun", "cefr": "B1", "translation": "borderline / frontier", "examples": [{"hungarian": "A Duna képezte a birodalom északi határvonalát.", "english": "The Danube formed the empire's northern frontier."}]},
        {"lemma": "hadsereg", "pos": "noun", "cefr": "B1", "translation": "army", "examples": [{"hungarian": "A római hadsereg erődöket épített a part mentén.", "english": "The Roman army built forts along the bank."}]},
        {"lemma": "úthálózat", "pos": "noun", "cefr": "B1", "translation": "road network", "examples": [{"hungarian": "A kiváló úthálózat biztosította a gyors közlekedést.", "english": "The excellent road network ensured fast transportation."}]},
        {"lemma": "vízvezeték", "pos": "noun", "cefr": "B1", "translation": "aqueduct", "examples": [{"hungarian": "Aquincumban római vízvezeték maradványai láthatók.", "english": "Remains of a Roman aqueduct can be seen in Aquincum."}]},
        {"lemma": "fürdőkultúra", "pos": "noun", "cefr": "B1", "translation": "bath culture", "examples": [{"hungarian": "A római fürdőkultúra nagy hatást gyakorolt a térségre.", "english": "Roman bath culture had a great impact on the region."}]},
        {"lemma": "sírkamra", "pos": "noun", "cefr": "B1", "translation": "burial chamber / catacomb", "examples": [{"hungarian": "A pécsi ókeresztény sírkamrák híres műemlékek.", "english": "The early Christian burial chambers of Pécs are famous monuments."}]},
        {"lemma": "világörökség", "pos": "noun", "cefr": "B1", "translation": "World Heritage", "examples": [{"hungarian": "Sopianae emlékei a világörökség részét képezik.", "english": "The relics of Sopianae form part of the World Heritage."}]},
        {"lemma": "szőlőtermesztés", "pos": "noun", "cefr": "B1", "translation": "viticulture / grape cultivation", "examples": [{"hungarian": "A szőlőtermesztés a római korban virágzott fel.", "english": "Viticulture flourished during the Roman era."}]},
        {"lemma": "maradvány", "pos": "noun", "cefr": "B1", "translation": "remains / relic", "examples": [{"hungarian": "A kőfalak maradványai ma is látogathatók.", "english": "The remains of the stone walls can still be visited today."}]},
        {"lemma": "amfiteátrum", "pos": "noun", "cefr": "B1", "translation": "amphitheatre", "examples": [{"hungarian": "Aquincumban két amfiteátrumot is feltártak.", "english": "Two amphitheatres were excavated in Aquincum."}]},
        {"lemma": "közigazgatás", "pos": "noun", "cefr": "B1", "translation": "public administration", "examples": [{"hungarian": "A római közigazgatás jól szervezett volt.", "english": "Roman public administration was well organized."}]}
    ]
})

write_json(GRAMMAR_DIR / "b1-karpatmedence-02-gr.json", {
    "title": "Helyhatározók és névutók a földrajzi leírásban",
    "level": "B1",
    "rules": [
        {
            "id": "postpositions-spatial",
            "title": "Spatial Postpositions in Hungarian",
            "text": "Postpositions follow nouns directly without suffixes (or with possessive harmony): *mentén* (along), *közelében* (near), *területén* (on the territory of), *részét képezi* (forms part of).",
            "tip": "Example: *a Duna mentén* (along the Danube), *a város területén* (in the territory of the city)."
        },
        {
            "id": "locative-names",
            "title": "Ancient Towns and Modern Hungarian Names",
            "text": "When expressing location in Hungarian towns, note the suffix variations: *Pécs-en, Sopron-ban, Szombathely-en, Óbudá-n*.",
            "tip": "Hungarian city names take either *-ban/-ben* or *-n/-on/-en/-ön* by established historical convention."
        }
    ],
    "examples": [
        {"spanish": "A Duna mentén katonai erődök épültek.", "english": "Military forts were built along the Danube."},
        {"spanish": "Aquincum a mai Óbuda területén feküdt.", "english": "Aquincum lay on the territory of modern Óbuda."},
        {"spanish": "Pécsen korai keresztény sírkamrákat találtak.", "english": "Early Christian burial chambers were found in Pécs."}
    ]
})

write_json(EXERCISES_DIR / "b1-karpatmedence-02-ex.json", {
    "exercises": [
        {
            "id": "b1-karpatmedence-02.ex01",
            "type": "multiple-choice",
            "title": "Pannonia határai",
            "instruction": "Válaszd ki a helyes állítást!",
            "question": "Mi volt Pannonia provincia északi és keleti határa?",
            "options": ["A Duna folyó megerősített vonala (limes)", "A Tisza folyó", "Az Adriai-tenger partja", "A Kárpátok legmagasabb csúcsa"],
            "correctIndex": 0,
            "explanation": "A Duna alkotta a római birodalom határvonalát Pannoniában.",
            "teaches": ["provincia", "hatarvonal"]
        },
        {
            "id": "b1-karpatmedence-02.ex02",
            "type": "fill-blank",
            "title": "Ókori római városok",
            "instruction": "Egészítsd ki a mondatot!",
            "sentence": "Savaria a mai Szombathely, Sopianae pedig a mai ___ területén helyezkedett el.",
            "correctAnswer": "Pécs",
            "options": ["Pécs", "Debrecen", "Szeged", "Győr"],
            "teaches": ["telepules", "kozigazgatas"]
        },
        {
            "id": "b1-karpatmedence-02.ex03",
            "type": "sentence-builder",
            "title": "Római úthálózat",
            "instruction": "Állítsd össze a mondatot a megadott szavakból!",
            "words": ["A", "rómaiak", "kiváló", "úthálózatot", "építettek", "ki", "Pannoniában."],
            "correctSentence": "A rómaiak kiváló úthálózatot építettek ki Pannoniában.",
            "english": "The Romans built an excellent road network in Pannonia.",
            "teaches": ["uthalozat", "provincia"]
        },
        {
            "id": "b1-karpatmedence-02.ex04",
            "type": "multiple-choice",
            "title": "Sopianae ókeresztény emlékei",
            "instruction": "Melyik állítás igaz a pécsi emlékekről?",
            "question": "Miért különlegesek Sopianae ókeresztény sírkamrái?",
            "options": ["Az UNESCO világörökség részét képezik", "Modern felhőkarcolók alatt épültek tegnap", "Csak fából készültek és elpusztultak", "Nem maradt róluk semmilyen lelet"],
            "correctIndex": 0,
            "explanation": "A pécsi korai keresztény sírkamrák védett UNESCO világörökségi helyszínek.",
            "teaches": ["sirkamra", "vilagorokseg"]
        },
        {
            "id": "b1-karpatmedence-02.ex05",
            "type": "fill-blank",
            "title": "Borkultúra és szőlő",
            "instruction": "Válaszd ki a helyes kifejezést!",
            "sentence": "A rómaiak vezették be a Dunántúlon a ___ és a borkészítést.",
            "correctAnswer": "szőlőtermesztést",
            "options": ["szőlőtermesztést", "kávéfőzést", "csokoládékészítést", "papírgyártást"],
            "teaches": ["szolotermesztes"]
        },
        {
            "id": "b1-karpatmedence-02.ex06",
            "type": "sentence-builder",
            "title": "Aquincum emlékei",
            "instruction": "Rendezd helyes sorrendbe a szavakat!",
            "words": ["Aquincumban", "vízvezetékek", "és", "amfiteátrumok", "maradványai", "láthatók."],
            "correctSentence": "Aquincumban vízvezetékek és amfiteátrumok maradványai láthatók.",
            "english": "In Aquincum, remains of aqueducts and amphitheatres can be seen.",
            "teaches": ["vizvezetek", "amfiteatrum", "maradvany"]
        },
        {
            "id": "b1-karpatmedence-02.ex07",
            "type": "multiple-choice",
            "title": "A római limes jelentése",
            "instruction": "Mit jelent a limes fogalma?",
            "question": "Mi volt a limes az ókori Pannoniában?",
            "options": ["Megerősített katonai határvonal őrtornyokkal", "Egyfajta római aranypénz", "Egy ünnepi római étel", "A császári palota kertje"],
            "correctIndex": 0,
            "explanation": "A limes a Római Birodalom erődített, őrtornyokkal ellátott védelmi határvonala volt.",
            "teaches": ["hatarvonal", "hadsereg"]
        },
        {
            "id": "b1-karpatmedence-02.ex08",
            "type": "fill-blank",
            "title": "Közigazgatás és városok",
            "instruction": "Egészítsd ki a mondatot!",
            "sentence": "A tartományban jól szervezett római ___ működött.",
            "correctAnswer": "közigazgatás",
            "options": ["közigazgatás", "vadászat", "zűrzavar", "futballbajnokság"],
            "teaches": ["kozigazgatas"]
        }
    ]
})

write_json(LESSONS_DIR / "b1-karpatmedence-02.json", make_lesson(
    "lesson.b1.karpatmedence-02",
    "Pannonia provincia és a római örökség (Roman Pannonia)",
    "Helyhatározók és névutók a földrajzi leírásban",
    [
        "In this second lesson, we explore the Roman conquest of Transdanubia (*Dunántúl*) and the creation of Pannonia province.",
        "You will discover the Danube *limes*, military fortifications, and thriving Roman towns such as Aquincum (modern Óbuda), Savaria (Szombathely), and Sopianae (Pécs), renowned for its UNESCO World Heritage early Christian tombs.",
        "We also practice spatial postpositions (*mentén, területén, közelében*) used to describe geographic locations."
    ],
    [
        "I can describe the role of Pannonia within the Roman Empire and locate the Danube limes.",
        "I can connect Roman city names (Aquincum, Savaria, Sopianae) with their modern Hungarian counterparts.",
        "I can explain the Roman roots of viticulture and architecture in Transdanubia.",
        "I can use spatial postpositions and locative suffixes correctly in descriptive sentences."
    ],
    "stories/world/b1/b1-karpatmedence-02-pannonia.json",
    "vocabulary/b1/b1-karpatmedence-02-voc.json",
    "grammar/b1/b1-karpatmedence-02-gr.json",
    "exercises/b1/b1-karpatmedence-02-ex.json",
    [f"b1-karpatmedence-02.ex{i:02d}" for i in range(1, 9)]
))

# -----------------
# Lesson 3: Népvándorlás kora
# -----------------
write_json(STORIES_DIR / "b1-karpatmedence-03-nepvandorlas.json", make_story(
    "story.b1.karpatmedence.03",
    "A népvándorlás kora és a hunok birodalma",
    "The turbulent Migration Period: Attila the Hun's center of power in the Great Plain, followed by Germanic kingdoms of Gepids, Ostrogoths, and Lombards.",
    "Alföld és Dunántúl",
    ["időhatározók és ok-határozói kifejezések"],
    ["Népvándorlás", "Hun birodalom", "Germán törzsek"],
    [
        "Az 5. században a Római Birodalom meggyengült, és megkezdődött a népvándorlás kora. Kelet felől nomád lovas népek és germán törzsek érkeztek hullámokban a Kárpát-medencébe.",
        "A leghatalmasabb nomád birodalmat a hunok hozták létre. Uralkodójuk, Attila a Tisza vidékén építette ki birodalmának központját, ahonnan egész Európát rettegésben tartotta.",
        "Attila 453-ban bekövetkezett halála után a Hun Birodalom gyorsan felbomlott. A hatalomért folytatott küzdelemben germán törzsek ragadták magukhoz az irányítást.",
        "A keleti területeken és a Tiszántúlon a gepidák hoztak létre tartós királyságot, míg a Dunántúlt a keleti gótok, majd a longobárdok uralták.",
        "A népvándorlás viharos évszázadai alatt a Kárpát-medence népessége folyamatosan cserélődött, új kultúrákat és haditechnikát hozva a térségbe."
    ],
    [
        {"lemma": "népvándorlás", "pos": "noun", "cefr": "B1", "gloss": "Migration Period"},
        {"lemma": "nomád", "pos": "adj", "cefr": "B1", "gloss": "nomadic"},
        {"lemma": "uralkodó", "pos": "noun", "cefr": "B1", "gloss": "ruler / monarch"},
        {"lemma": "felbomlik", "pos": "verb", "cefr": "B1", "gloss": "to disintegrate / dissolve"}
    ],
    [
        {
            "question": "Ki volt a leghíresebb hun uralkodó, aki a Kárpát-medencében rendezte be székhelyét?",
            "options": ["Attila", "Julius Caesar", "Nagy Károly", "Szent István"],
            "correctIndex": 0,
            "explanation": "Attila király a Tisza vidékén építette ki hatalmas hun birodalmának központját."
        },
        {
            "question": "Mi történt a Hun Birodalommal Attila halála után?",
            "options": ["Gyorsan felbomlott, és germán népek vették át a hatalmat", "Tovább virágzott még ezer évig", "Békésen átadta a területet a rómaiaknak", "Európa egyetlen örök államává vált"],
            "correctIndex": 0,
            "explanation": "Attila 453-as halála után a Hun Birodalom felbomlott a belső viszályok és germán felkelések miatt."
        },
        {
            "question": "Mely germán népek éltek a Kárpát-medencében a hunok után?",
            "options": ["Gepidák, keleti gótok és longobárdok", "Csak spanyol telepesek", "Viking hajósok kizárólag", "Ókori egyiptomiak"],
            "correctIndex": 0,
            "explanation": "A hunok után gepidák, keleti gótok és longobárdok alapítottak királyságokat a térségben."
        }
    ]
))

write_json(VOCAB_DIR / "b1-karpatmedence-03-voc.json", {
    "title": "A népvándorlás kora és a hunok birodalma",
    "words": [
        {"lemma": "népvándorlás", "pos": "noun", "cefr": "B1", "translation": "Migration Period", "examples": [{"hungarian": "A népvándorlás kora átalakította Európa térképét.", "english": "The Migration Period reshaped the map of Europe."}]},
        {"lemma": "nomád", "pos": "adj", "cefr": "B1", "translation": "nomadic", "examples": [{"hungarian": "A nomád lovasok kiváló íjászok voltak.", "english": "The nomadic horsemen were excellent archers."}]},
        {"lemma": "uralkodó", "pos": "noun", "cefr": "B1", "translation": "ruler / monarch", "examples": [{"hungarian": "Attila félelmetes hírű uralkodó volt.", "english": "Attila was a ruler of fearsome renown."}]},
        {"lemma": "székhely", "pos": "noun", "cefr": "B1", "translation": "headquarters / seat", "examples": [{"hungarian": "A király székhelye a Tisza mellett volt.", "english": "The king's seat was located beside the Tisza."}]},
        {"lemma": "felbomlik", "pos": "verb", "cefr": "B1", "translation": "to disintegrate / break up", "examples": [{"hungarian": "A birodalom hamar felbomlott a vezér halála után.", "english": "The empire quickly disintegrated after the leader's death."}]},
        {"lemma": "viharos", "pos": "adj", "cefr": "B1", "translation": "turbulent / stormy", "examples": [{"hungarian": "Viharos évszázadok következtek a térségben.", "english": "Turbulent centuries followed in the region."}]},
        {"lemma": "hódítás", "pos": "noun", "cefr": "B1", "translation": "conquest", "examples": [{"hungarian": "A katonai hódítások megrázták a kontinenst.", "english": "The military conquests shook the continent."}]},
        {"lemma": "haditechnika", "pos": "noun", "cefr": "B1", "translation": "military technology", "examples": [{"hungarian": "A visszacsapó íj a kor modern haditechnikája volt.", "english": "The recurve bow was the modern military technology of the age."}]},
        {"lemma": "hullám", "pos": "noun", "cefr": "B1", "translation": "wave", "examples": [{"hungarian": "Újabb népek érkeztek több hullámban.", "english": "New peoples arrived in multiple waves."}]},
        {"lemma": "uralom", "pos": "noun", "cefr": "B1", "translation": "rule / reign", "examples": [{"hungarian": "A gepidák uralma évtizedekig tartott a Tiszántúlon.", "english": "Gepid rule lasted for decades in the Transtisza region."}]},
        {"lemma": "örökség", "pos": "noun", "cefr": "B1", "translation": "heritage / legacy", "examples": [{"hungarian": "A hun hagyomány fontos része lett a későbbi magyar krónikáknak.", "english": "Hun tradition became an important part of later Hungarian chronicles."}]},
        {"lemma": "meggyengül", "pos": "verb", "cefr": "B1", "translation": "to weaken / grow frail", "examples": [{"hungarian": "A római védelem meggyengült a határokon.", "english": "Roman defense weakened along the frontiers."}]}
    ]
})

write_json(GRAMMAR_DIR / "b1-karpatmedence-03-gr.json", {
    "title": "Időhatározók és ok-határozók a történeti összefüggésekben",
    "level": "B1",
    "rules": [
        {
            "id": "temporal-expressions",
            "title": "Expressing Time in Centuries and Eras",
            "text": "Expressing centuries: *az 5. században* (in the 5th century), *Attila halála után* (after Attila's death), *a népvándorlás idején* (during the Migration Period).",
            "tip": "Ordinal numbers take the suffix *-ban/-ben*: *az ötödik században*."
        },
        {
            "id": "causal-conjunctions",
            "title": "Causal Clauses in Hungarian",
            "text": "To express cause and consequence in history, use *miatt* (because of + noun), *mivel* / *mert* (since / because + clause), and *következtében* (as a consequence of).",
            "tip": "Example: *A belső harcok miatt a birodalom felbomlott.* (Because of internal fighting, the empire dissolved.)"
        }
    ],
    "examples": [
        {"spanish": "Az ötödik században nomád törzsek érkeztek a medencébe.", "english": "In the fifth century, nomadic tribes arrived in the basin."},
        {"spanish": "Attila halála után a Hun Birodalom felbomlott.", "english": "After Attila's death, the Hun Empire disintegrated."},
        {"spanish": "A belső viszályok következtében meggyengült a hatalmuk.", "english": "As a consequence of internal strife, their power weakened."}
    ]
})

write_json(EXERCISES_DIR / "b1-karpatmedence-03-ex.json", {
    "exercises": [
        {
            "id": "b1-karpatmedence-03.ex01",
            "type": "multiple-choice",
            "title": "A hunok vezére",
            "instruction": "Válaszd ki a helyes választ!",
            "question": "Ki irányította a Kárpát-medencéből a Hun Birodalmat?",
            "options": ["Attila", "Nagy Sándor", "Árpád vezér", "Mátyás király"],
            "correctIndex": 0,
            "explanation": "Attila volt a hunok leghíresebb uralkodója az 5. században.",
            "teaches": ["uralkodo", "szekhely"]
        },
        {
            "id": "b1-karpatmedence-03.ex02",
            "type": "fill-blank",
            "title": "A birodalom sorsa",
            "instruction": "Egészítsd ki a mondatot!",
            "sentence": "Attila halála után a hatalmas Hun Birodalom gyorsan ___.",
            "correctAnswer": "felbomlott",
            "options": ["felbomlott", "megerősödött", "elrepült", "bővült"],
            "teaches": ["felbomlik", "uralkodo"]
        },
        {
            "id": "b1-karpatmedence-03.ex03",
            "type": "sentence-builder",
            "title": "Nomád lovasok",
            "instruction": "Állítsd össze a mondatot!",
            "words": ["A", "nomád", "lovasok", "hullámokban", "érkeztek", "a", "Kárpát-medencébe."],
            "correctSentence": "A nomád lovasok hullámokban érkeztek a Kárpát-medencébe.",
            "english": "The nomadic horsemen arrived in waves into the Carpathian Basin.",
            "teaches": ["nomad", "hullam", "nepvandorlas"]
        },
        {
            "id": "b1-karpatmedence-03.ex04",
            "type": "multiple-choice",
            "title": "Germán királyságok",
            "instruction": "Melyik nép uralta a Tiszántúlt a hunok után?",
            "options": ["A gepidák", "A vikingek", "A föníciaiak", "A római császárok"],
            "correctIndex": 0,
            "explanation": "A hunok után a gepidák alapítottak erős királyságot a Tisza vidékén.",
            "teaches": ["uralom", "nepvandorlas"]
        },
        {
            "id": "b1-karpatmedence-03.ex05",
            "type": "fill-blank",
            "title": "Időpontok a történelemben",
            "instruction": "Válaszd ki a helyes alakot!",
            "sentence": "A népvándorlás az 5. ___ alakította át Európa képét.",
            "correctAnswer": "században",
            "options": ["században", "percben", "hétben", "utcában"],
            "teaches": ["nepvandorlas"]
        },
        {
            "id": "b1-karpatmedence-03.ex06",
            "type": "sentence-builder",
            "title": "Belső viszályok",
            "instruction": "Rendezd helyes sorrendbe a szavakat!",
            "words": ["A", "belső", "harcok", "miatt", "meggyengült", "a", "védelem."],
            "correctSentence": "A belső harcok miatt meggyengült a védelem.",
            "english": "Because of internal fights, the defense was weakened.",
            "teaches": ["meggyengul"]
        },
        {
            "id": "b1-karpatmedence-03.ex07",
            "type": "multiple-choice",
            "title": "Haditechnika a nomád korban",
            "instruction": "Mi tette félelmetessé a nomád lovasok hadviselését?",
            "question": "Milyen fegyvert és harcmodort használtak a nomádok?",
            "options": ["Kiváló lovastudást és visszacsapó íjakat", "Ágyúkat és puskákat", "Nehéz páncélos gőzhajókat", "Csak fakardokat"],
            "correctIndex": 0,
            "explanation": "A lovas nomádok gyors mozgásukról és félelmetes íjásztudásukról voltak híresek.",
            "teaches": ["haditechnika", "nomad"]
        },
        {
            "id": "b1-karpatmedence-03.ex08",
            "type": "fill-blank",
            "title": "Viharos évszázadok",
            "instruction": "Egészítsd ki a mondatot!",
            "sentence": "A térségben ___ évszázadok következtek sok népcsoport érkezésével.",
            "correctAnswer": "viharos",
            "options": ["viharos", "unalmas", "csendes", "hideg"],
            "teaches": ["viharos"]
        }
    ]
})

write_json(LESSONS_DIR / "b1-karpatmedence-03.json", make_lesson(
    "lesson.b1.karpatmedence-03",
    "A népvándorlás kora és a hunok (The Migration Period & Huns)",
    "Időhatározók és ok-határozói kifejezések",
    [
        "In this third lesson, we study the stormy Migration Period (*népvándorlás kora*) in the 5th and 6th centuries.",
        "You will learn about Attila the Hun and his powerhouse along the Tisza, followed by the Germanic kingdoms of Gepids and Lombards.",
        "We also focus on time adverbials (*században, után*) and causal constructions (*miatt, következtében*)."
    ],
    [
        "I can describe the impact of the Migration Period on the Carpathian Basin.",
        "I can explain the historical role of Attila and the Hun Empire.",
        "I can identify the Germanic peoples (Gepids, Lombards) who ruled after the Huns.",
        "I can form complex B1 sentences expressing historical cause and chronological sequence."
    ],
    "stories/world/b1/b1-karpatmedence-03-nepvandorlas.json",
    "vocabulary/b1/b1-karpatmedence-03-voc.json",
    "grammar/b1/b1-karpatmedence-03-gr.json",
    "exercises/b1/b1-karpatmedence-03-ex.json",
    [f"b1-karpatmedence-03.ex{i:02d}" for i in range(1, 9)]
))

# -----------------
# Lesson 4: Az avarok és szlávok
# -----------------
write_json(STORIES_DIR / "b1-karpatmedence-04-kikeltekitt.json", make_story(
    "story.b1.karpatmedence.04",
    "Az Avar Kaganátus és a szláv letelepedés",
    "The 250-year rule of the Avar Khaganate: their nomadic military power, ring fortifications, belt-mount treasures, and coexistence with Slavic agricultural communities.",
    "Kárpát-medence",
    ["melléknévi igenevek és leíró szerkezetek"],
    ["Avarok", "Szláv népesség", "Kaganátus"],
    [
        "568-ban új nomád lovas nép érkezett Belső-Ázsiából a Kárpát-medencébe: az avarok. Baján kagán vezetésével legyőzték a gepidákat, és több mint két évszázadon át fennálló birodalmat alapítottak.",
        "Az Avar Kaganátus korában a medence lakossága kiegészült a földműveléssel és állattartással foglalkozó szláv törzsekkel, akik a völgyekben és a Dunántúlon telepedtek le.",
        "Az avarok hatalmas kincseket halmoztak fel a bizánci hadjáratok során, és híres gyűrű alakú erődítményekben, úgynevezett hringekben őrizték vagyonukat.",
        "A régészek tízezrével tártak fel avar sírokat Magyarországon: a finom griffes-indás övdíszek, szablyák és kengyelek a nomád kézművesség csúcsát jelentették.",
        "A 8. század végén Nagy Károly frank császár hadjáratai megdöntötték az Avar Birodalmat, utat nyitva a helyi szláv fejedelemségek megerősödése előtt."
    ],
    [
        {"lemma": "kaganátus", "pos": "noun", "cefr": "B1", "gloss": "khaganate"},
        {"lemma": "földművelés", "pos": "noun", "cefr": "B1", "gloss": "agriculture / farming"},
        {"lemma": "kincs", "pos": "noun", "cefr": "B1", "gloss": "treasure"},
        {"lemma": "övdísz", "pos": "noun", "cefr": "B1", "gloss": "belt ornament / mount"}
    ],
    [
        {
            "question": "Milyen jellegű államot hoztak létre az avarok 568 után a Kárpát-medencében?",
            "options": ["Avar Kaganátus nevű nomád lovas birodalmat", "Tengeri köztársaságot", "Római tartományt", "Modern parlamenti monarchiát"],
            "correctIndex": 0,
            "explanation": "Az avarok 568-ban megalapították az Avar Kaganátust, amely több mint két évszázadig uralta a medencét."
        },
        {
            "question": "Milyen régészeti tárgyak jellemzik az avar kultúrát?",
            "options": ["Griffes-indás övdíszek, szablyák és kengyelek", "Műanyag játékok", "Gőzgép alkatrészek", "Csak papírtekercsek"],
            "correctIndex": 0,
            "explanation": "A régészeti leletek között a jellegzetes griffes-indás bronz övdíszek és kengyelek emelkednek ki."
        },
        {
            "question": "Ki győzte le az avarokat a 8. század végén?",
            "options": ["Nagy Károly frank uralkodó", "Julius Caesar", "Mátyás király", "Napóleon császár"],
            "correctIndex": 0,
            "explanation": "Nagy Károly frank uralkodó hadjáratai döntötték meg az Avar Kaganátust 800 körül."
        }
    ]
))

write_json(VOCAB_DIR / "b1-karpatmedence-04-voc.json", {
    "title": "Az Avar Kaganátus és a szláv letelepedés",
    "words": [
        {"lemma": "kaganátus", "pos": "noun", "cefr": "B1", "translation": "khaganate", "examples": [{"hungarian": "Az Avar Kaganátus két évszázadon át uralta a térséget.", "english": "The Avar Khaganate ruled the region for two centuries."}]},
        {"lemma": "földművelés", "pos": "noun", "cefr": "B1", "translation": "agriculture / crop farming", "examples": [{"hungarian": "A szláv lakosság békés földműveléssel foglalkozott.", "english": "The Slavic population engaged in peaceful agriculture."}]},
        {"lemma": "állattartás", "pos": "noun", "cefr": "B1", "translation": "animal husbandry", "examples": [{"hungarian": "Az állattartás a nomád gazdálkodás alapja volt.", "english": "Animal husbandry was the basis of the nomadic economy."}]},
        {"lemma": "kincs", "pos": "noun", "cefr": "B1", "translation": "treasure", "examples": [{"hungarian": "Hatalmas aranykincset találtak az erődökben.", "english": "They found immense gold treasures in the forts."}]},
        {"lemma": "övdísz", "pos": "noun", "cefr": "B1", "translation": "belt mount / ornament", "examples": [{"hungarian": "A griffes-indás övdíszek az avar kézművesség remekei.", "english": "The griffin-and-vine belt mounts are masterpieces of Avar craft."}]},
        {"lemma": "szablya", "pos": "noun", "cefr": "B1", "translation": "sabre", "examples": [{"hungarian": "Az avar harcosok éles szablyával harcoltak.", "english": "The Avar warriors fought with sharp sabres."}]},
        {"lemma": "kengyel", "pos": "noun", "cefr": "B1", "translation": "stirrup", "examples": [{"hungarian": "A vaskengyel használata forradalmasította a lovaglást.", "english": "The use of the iron stirrup revolutionized riding."}]},
        {"lemma": "hadjárat", "pos": "noun", "cefr": "B1", "translation": "military campaign", "examples": [{"hungarian": "Nagy Károly több hadjáratot indított az avarok ellen.", "english": "Charlemagne launched multiple campaigns against the Avars."}]},
        {"lemma": "együttélés", "pos": "noun", "cefr": "B1", "translation": "coexistence", "examples": [{"hungarian": "A békés együttélés jellemezte a falvakat.", "english": "Peaceful coexistence characterized the villages."}]},
        {"lemma": "megdönt", "pos": "verb", "cefr": "B1", "translation": "to overthrow / topple", "examples": [{"hungarian": "A frank sereg megdöntötte az avarok hatalmát.", "english": "The Frankish army toppled the power of the Avars."}]},
        {"lemma": "feltár", "pos": "verb", "cefr": "B1", "translation": "to excavate / uncover", "examples": [{"hungarian": "A régészek gazdag sírokat tártak fel.", "english": "The archaeologists excavated rich graves."}]},
        {"lemma": "fejedelemség", "pos": "noun", "cefr": "B1", "translation": "principality", "examples": [{"hungarian": "Szláv fejedelemségek alakultak ki a térség peremén.", "english": "Slavic principalities developed on the fringes of the region."}]}
    ]
})

write_json(GRAMMAR_DIR / "b1-karpatmedence-04-gr.json", {
    "title": "Melléknévi igenevek és összetett leíró mondatok",
    "level": "B1",
    "rules": [
        {
            "id": "participles-present-past",
            "title": "Present and Past Participles as Adjectives",
            "text": "Participles allow rich, compact B1 descriptions: Present participle (*-ó / -ő*): *földműveléssel foglalkozó törzsek* (tribes engaged in farming); Past participle (*-t / -tt*): *a feltárt sírok* (the excavated graves), *megerősített erődök* (fortified strongholds).",
            "tip": "Participles precede the noun they modify, just like standard adjectives."
        },
        {
            "id": "relative-pronouns",
            "title": "Relative Clauses with 'amely' and 'aki'",
            "text": "Use *aki / akik* for people (*a szlávok, akik letelepedtek*) and *amely / amelyek* for objects and entities (*a birodalom, amelyet megdöntöttek*).",
            "tip": "Always place a comma before relative pronouns in Hungarian."
        }
    ],
    "examples": [
        {"spanish": "A földműveléssel foglalkozó szláv törzsek a völgyekben éltek.", "english": "The Slavic tribes engaged in agriculture lived in the valleys."},
        {"spanish": "A régészek által feltárt sírok gazdagok voltak.", "english": "The graves excavated by archaeologists were rich."},
        {"spanish": "Az avarok olyan nép voltak, akik szablyával és íjjal harcoltak.", "english": "The Avars were a people who fought with sabre and bow."}
    ]
})

write_json(EXERCISES_DIR / "b1-karpatmedence-04-ex.json", {
    "exercises": [
        {
            "id": "b1-karpatmedence-04.ex01",
            "type": "multiple-choice",
            "title": "Az Avar Birodalom",
            "instruction": "Válaszd ki az igaz állítást!",
            "question": "Mikor érkeztek az avarok a Kárpát-medencébe?",
            "options": ["568-ban Baján kagán vezetésével", "1914-ben a világháborúban", "Időszámításunk előtt 2000-ben", "1492-ben Amerika felfedezésekor"],
            "correctIndex": 0,
            "explanation": "Az avarok 568-ban hozták létre az Avar Kaganátust a Kárpát-medencében.",
            "teaches": ["kaganatus", "hadjarat"]
        },
        {
            "id": "b1-karpatmedence-04.ex02",
            "type": "fill-blank",
            "title": "Avar régészet",
            "instruction": "Egészítsd ki a mondatot!",
            "sentence": "A sírokban talált finom ___ az avar kézművesség magas színvonalát bizonyítják.",
            "correctAnswer": "övdíszek",
            "options": ["övdíszek", "repülőgépek", "telefonok", "műanyagok"],
            "teaches": ["ovdisz", "feltar"]
        },
        {
            "id": "b1-karpatmedence-04.ex03",
            "type": "sentence-builder",
            "title": "Földművelő szlávok",
            "instruction": "Állítsd össze a mondatot!",
            "words": ["A", "földműveléssel", "foglalkozó", "szlávok", "a", "völgyekben", "telepedtek", "le."],
            "correctSentence": "A földműveléssel foglalkozó szlávok a völgyekben telepedtek le.",
            "english": "The Slavs engaged in agriculture settled down in the valleys.",
            "teaches": ["foldmuveles", "egyutteles"]
        },
        {
            "id": "b1-karpatmedence-04.ex04",
            "type": "multiple-choice",
            "title": "Az avar birodalom bukása",
            "instruction": "Ki döntötte meg az Avar Kaganátust?",
            "question": "Melyik nyugati uralkodó vezette a győztes hadjáratot az avarok ellen?",
            "options": ["Nagy Károly frank császár", "I. István magyar király", "Julius Caesar római hadvezér", "Mátyás király"],
            "correctIndex": 0,
            "explanation": "Nagy Károly frank császár hadjáratai döntötték meg az avarok uralmát a 8. század végén.",
            "teaches": ["megdont", "hadjarat"]
        },
        {
            "id": "b1-karpatmedence-04.ex05",
            "type": "fill-blank",
            "title": "Haditechnikai újítás",
            "instruction": "Válaszd ki a megfelelő szót!",
            "sentence": "A vaskos ___ használata stabilabbá tette a lovas harcosokat a nyeregben.",
            "correctAnswer": "kengyel",
            "options": ["kengyel", "kalap", "cipőfűző", "zászló"],
            "teaches": ["kengyel", "szablya"]
        },
        {
            "id": "b1-karpatmedence-04.ex06",
            "type": "sentence-builder",
            "title": "Régészeti feltárások",
            "instruction": "Rendezd helyes sorrendbe a mondatrészeket!",
            "words": ["A", "régészek", "több", "ezer", "avar", "sírt", "tártak", "fel."],
            "correctSentence": "A régészek több ezer avar sírt tártak fel.",
            "english": "The archaeologists excavated several thousand Avar graves.",
            "teaches": ["feltar", "kincs"]
        },
        {
            "id": "b1-karpatmedence-04.ex07",
            "type": "multiple-choice",
            "title": "Gazdasági tevékenységek",
            "instruction": "Mivel foglalkozott a szláv lakosság?",
            "question": "Mi jellemezte a szlávok gazdálkodását a medencében?",
            "options": ["Földműveléssel és békés falusi élettel", "Csak tengeri halászattal", "Kizárólag zsoldos katonáskodással", "Piramisok építésével"],
            "correctIndex": 0,
            "explanation": "A szláv törzsek elsősorban földműveléssel és letelepedett falusi gazdálkodással foglalkoztak.",
            "teaches": ["foldmuveles", "allattartas"]
        },
        {
            "id": "b1-karpatmedence-04.ex08",
            "type": "fill-blank",
            "title": "Kincsek és erődök",
            "instruction": "Egészítsd ki a mondatot!",
            "sentence": "Az avar vezetők hatalmas ___ halmoztak fel erődített táboraikban.",
            "correctAnswer": "kincseket",
            "options": ["kincseket", "könyveket", "gépeket", "hóviharokat"],
            "teaches": ["kincs"]
        }
    ]
})

write_json(LESSONS_DIR / "b1-karpatmedence-04.json", make_lesson(
    "lesson.b1.karpatmedence-04",
    "Az Avar Kaganátus és a szlávok (The Avar Khaganate & Slavs)",
    "Melléknévi igenevek és összetett leíró mondatok",
    [
        "In this fourth lesson, we examine the Avar Khaganate (568–c. 800) and the Slavic populations living alongside them.",
        "You will learn about Avar equestrian innovations (stirrups, sabres, ring-forts), the renowned griffin-and-vine belt mounts, and Charlemagne's campaigns.",
        "We practice Hungarian present and past participles (*foglalkozó, feltárt*) to construct rich descriptive clauses."
    ],
    [
        "I can describe the 250-year history of the Avar Khaganate in the Carpathian Basin.",
        "I can explain the coexistence between nomadic Avars and agricultural Slavs.",
        "I can recognize key archaeological terms such as stirrup (*kengyel*), sabre (*szablya*), and belt mounts (*övdíszek*).",
        "I can use present and past participles to create concise, sophisticated B1 sentences."
    ],
    "stories/world/b1/b1-karpatmedence-04-kikeltekitt.json",
    "vocabulary/b1/b1-karpatmedence-04-voc.json",
    "grammar/b1/b1-karpatmedence-04-gr.json",
    "exercises/b1/b1-karpatmedence-04-ex.json",
    [f"b1-karpatmedence-04.ex{i:02d}" for i in range(1, 9)]
))

# -----------------
# Lesson 5: Honfoglalás előestéjén
# -----------------
write_json(STORIES_DIR / "b1-karpatmedence-05-honfoglalaselott.json", make_story(
    "story.b1.karpatmedence.05",
    "A Kárpát-medence a 9. század végén",
    "The geopolitical landscape right before the Magyar conquest: the Frankish march in Transdanubia, Pribina and Kocel at Mosaburg (Zalavár), the Moravian state, and the Bulgarian realm.",
    "Mosaburg (Zalavár) és a medence peremei",
    ["feltételes mód és történeti összefoglalás"],
    ["9. századi geopolitika", "Zalavár és Morvaország", "Honfoglalás előtt"],
    [
        "A 9. század végén, közvetlenül a magyar honfoglalás előtt, a Kárpát-medencében nem létezett egységes, erős központi hatalom. A térség a környező birodalmak ütközőzónájává vált.",
        "A Dunántúl a Keleti Frank Királyság fennhatósága alá tartozott. A Balaton délnyugati partján fekvő Mosaburg (a mai Zalavár) lett a frank hűbéres szláv fejedelmek, Pribina és Kocel virágzó székhelye.",
        "Mosaburgban kőtemplomok, fejedelmi palota és kolostor épült, ahol a szláv apostolok, Cirill és Metód is megfordultak tanítani.",
        "Északon a Morva Fejedelemség, délen és a Tiszántúl déli részein pedig az Első Bolgár Birodalom gyakorolt laza ellenőrzést, miközben a medence belső síkságai ritkán lakottak voltak.",
        "Ez a politikai tagoltság és a hatalmi űr ideális feltételeket teremtett Árpád magyarjainak érkezéséhez, akik 895-ben birtokba vették új hazájukat."
    ],
    [
        {"lemma": "hatalmi űr", "pos": "noun", "cefr": "B1", "gloss": "power vacuum"},
        {"lemma": "fennhatóság", "pos": "noun", "cefr": "B1", "gloss": "sovereignty / jurisdiction"},
        {"lemma": "ütközőzóna", "pos": "noun", "cefr": "B1", "gloss": "buffer zone"},
        {"lemma": "hűbéres", "pos": "adj", "cefr": "B1", "gloss": "vassal / tributary"}
    ],
    [
        {
            "question": "Milyen volt a Kárpát-medence politikai helyzete a 9. század végén a honfoglalás előtt?",
            "options": ["Nem volt egységes hatalom, megosztott volt a frankok, morvák és bolgárok között", "Egyetlen hatalmas egységes császárság uralta", "Teljesen lakatlan volt minden falu és erdő", "Római légiók uralták szilárdan"],
            "correctIndex": 0,
            "explanation": "A 9. század végén hatalmi űr és politikai tagoltság jellemezte a medencét a környező birodalmak határán."
        },
        {
            "question": "Mi volt Mosaburg (Zalavár) jelentősége a Dunántúlon?",
            "options": ["Fontos egyházi és politikai központ volt templomokkal és fejedelmi udvarral", "Egy tengerparti katonai kikötő volt", "Egy lakatlan sivatagi oázis", "A Római Birodalom fővárosa"],
            "correctIndex": 0,
            "explanation": "Mosaburg (Zalavár) Pribina és Kocel székhelyeként virágzó frank-szláv egyházi és közigazgatási központ volt."
        },
        {
            "question": "Hogyan segítette a térség helyzete a honfoglaló magyarokat 895-ben?",
            "options": ["A politikai megosztottság és hatalmi űr megkönnyítette az új haza elfoglalását", "Erős fallal zárta el a határokat", "Nem engedte be a törzseket", "Mindenkit elűzött a hegyekből"],
            "correctIndex": 0,
            "explanation": "Az egységes központi ellenállás hiánya és a ritkán lakott alföldi tájak megkönnyítették a letelepedést."
        }
    ]
))

write_json(VOCAB_DIR / "b1-karpatmedence-05-voc.json", {
    "title": "A Kárpát-medence a 9. század végén",
    "words": [
        {"lemma": "hatalmi űr", "pos": "noun", "cefr": "B1", "translation": "power vacuum", "examples": [{"hungarian": "A hatalmi űr megkönnyítette a magyarok letelepedését.", "english": "The power vacuum made the settlement of the Magyars easier."}]},
        {"lemma": "fennhatóság", "pos": "noun", "cefr": "B1", "translation": "sovereignty / authority", "examples": [{"hungarian": "A Dunántúl frank fennhatóság alatt állt.", "english": "Transdanubia was under Frankish sovereignty."}]},
        {"lemma": "ütközőzóna", "pos": "noun", "cefr": "B1", "translation": "buffer zone", "examples": [{"hungarian": "A medence a nagy birodalmak ütközőzónája lett.", "english": "The basin became a buffer zone for great empires."}]},
        {"lemma": "hűbéres", "pos": "adj", "cefr": "B1", "translation": "vassal / tributary", "examples": [{"hungarian": "Pribina a frank király hűbéres fejedelme volt.", "english": "Pribina was a vassal prince of the Frankish king."}]},
        {"lemma": "politikai tagoltság", "pos": "noun", "cefr": "B1", "translation": "political fragmentation", "examples": [{"hungarian": "A térség politikai tagoltsága kedvezett a honfoglalásnak.", "english": "The political fragmentation of the region favoured the conquest."}]},
        {"lemma": "székhely", "pos": "noun", "cefr": "B1", "translation": "seat / centre", "examples": [{"hungarian": "Zalavár jelentős fejedelmi székhely volt.", "english": "Zalavár was a significant princely seat."}]},
        {"lemma": "kolostor", "pos": "noun", "cefr": "B1", "translation": "monastery", "examples": [{"hungarian": "A kolostorban kódexeket másoltak és tanítottak.", "english": "In the monastery, they copied codices and taught."}]},
        {"lemma": "birtokba vesz", "pos": "verb", "cefr": "B1", "translation": "to take possession of", "examples": [{"hungarian": "A magyarok 895-ben birtokba vették a medencét.", "english": "The Magyars took possession of the basin in 895."}]},
        {"lemma": "apostol", "pos": "noun", "cefr": "B1", "translation": "apostle", "examples": [{"hungarian": "Cirill és Metód a szlávok apostolai voltak.", "english": "Cyril and Methodius were the apostles of the Slavs."}]},
        {"lemma": "központi hatalom", "pos": "noun", "cefr": "B1", "translation": "central power", "examples": [{"hungarian": "Nem volt erős központi hatalom a területen.", "english": "There was no strong central power in the territory."}]},
        {"lemma": "megfordul", "pos": "verb", "cefr": "B1", "translation": "to visit / spend time at", "examples": [{"hungarian": "Neves hittérítők is megfordultak Mosaburgban.", "english": "Prominent missionaries also spent time in Mosaburg."}]},
        {"lemma": "ellentét", "pos": "noun", "cefr": "B1", "translation": "conflict / rivalry", "examples": [{"hungarian": "A frankok és morvák közötti ellentét gyengítette a védelmet.", "english": "The conflict between Franks and Moravians weakened the defense."}]}
    ]
})

write_json(GRAMMAR_DIR / "b1-karpatmedence-05-gr.json", {
    "title": "Feltételes mód és összefoglaló mondatszerkezetek",
    "level": "B1",
    "rules": [
        {
            "id": "conditional-mood-present",
            "title": "Conditional Mood in Historical Analysis",
            "text": "When discussing historical possibilities and hypotheses, use the present conditional (*-na / -ne / -nó / -nő*): *könnyebb lett volna* (it would have been easier), *segítené a letelepedést* (it would assist settlement).",
            "tip": "Form: stem + *-(a)nák / -(e)nék* in 3rd person plural (*elfoglalnák*)."
        },
        {
            "id": "synthesis-connectors",
            "title": "Discourse Markers of Contrast and Result",
            "text": "Structure sophisticated arguments with connectors: *ugyanakkor* (at the same time), *mindazonáltal* (nevertheless), *ennek köszönhetően* (thanks to this), *végül pedig* (and finally).",
            "tip": "Use these markers in your citizenship oral exam to link ideas smoothly."
        }
    ],
    "examples": [
        {"spanish": "A politikai megosztottságnak köszönhetően a magyarok könnyebben birtokba vehették a hazát.", "english": "Thanks to political division, the Magyars could take possession of the homeland more easily."},
        {"spanish": "Ugyanakkor Mosaburgban virágzó egyházi élet folyt.", "english": "At the same time, flourishing ecclesiastical life took place in Mosaburg."},
        {"spanish": "Erős központi hatalom nélkül nem tudták volna megvédeni a határt.", "english": "Without strong central power, they would not have been able to defend the border."}
    ]
})

write_json(EXERCISES_DIR / "b1-karpatmedence-05-ex.json", {
    "exercises": [
        {
            "id": "b1-karpatmedence-05.ex01",
            "type": "multiple-choice",
            "title": "Politikai helyzet a 9. században",
            "instruction": "Válaszd ki az igaz állítást!",
            "question": "Milyen hatalmi viszonyok uralkodtak a medencében a honfoglalás előtt?",
            "options": ["Politikai tagoltság és hatalmi űr jellemezte a térséget", "Egyetlen hatalmas császár uralkodott minden város felett", "Minden település teljesen elnéptelenedett", "Csak tengeri flották állomásoztak itt"],
            "correctIndex": 0,
            "explanation": "A Kárpát-medence megosztott volt a Frank Birodalom, a Morva Állam és a Bolgár Kaganátus peremén.",
            "teaches": ["hatalmi-ur", "politikai-tagoltsag"]
        },
        {
            "id": "b1-karpatmedence-05.ex02",
            "type": "fill-blank",
            "title": "Zalavár jelentősége",
            "instruction": "Egészítsd ki a mondatot!",
            "sentence": "Mosaburg (Zalavár) a frank hűbéres szláv fejedelmek virágzó ___ volt.",
            "correctAnswer": "székhelye",
            "options": ["székhelye", "börtöne", "hajója", "romja"],
            "teaches": ["szekhely", "huberes"]
        },
        {
            "id": "b1-karpatmedence-05.ex03",
            "type": "sentence-builder",
            "title": "Birtokbavétel 895-ben",
            "instruction": "Állítsd össze a helyes mondatot!",
            "words": ["A", "magyarok", "895-ben", "birtokba", "vették", "új", "hazájukat."],
            "correctSentence": "A magyarok 895-ben birtokba vették új hazájukat.",
            "english": "The Magyars took possession of their new homeland in 895.",
            "teaches": ["birtokba-vesz"]
        },
        {
            "id": "b1-karpatmedence-05.ex04",
            "type": "multiple-choice",
            "title": "Szláv térítők a Dunántúlon",
            "instruction": "Kik tanítottak Mosaburgban a 9. században?",
            "question": "Mely híres szláv apostolok fordultak meg Zalaváron?",
            "options": ["Cirill és Metód", "Rómeó és Júlia", "Kossuth és Petőfi", "Arisztotelész és Platón"],
            "correctIndex": 0,
            "explanation": "Cirill és Metód, a szlávok térítő apostolai meglátogatták Kocel fejedelmet Mosaburgban.",
            "teaches": ["apostol", "megfordul"]
        },
        {
            "id": "b1-karpatmedence-05.ex05",
            "type": "fill-blank",
            "title": "Központi hatalom hiánya",
            "instruction": "Válaszd ki a hiányzó kifejezést!",
            "sentence": "A térségben nem volt erős ___ hatalom a honfoglalás idején.",
            "correctAnswer": "központi",
            "options": ["központi", "égi", "tengeri", "földalatti"],
            "teaches": ["kozponti-hatalom"]
        },
        {
            "id": "b1-karpatmedence-05.ex06",
            "type": "sentence-builder",
            "title": "Hatalmi viszonyok",
            "instruction": "Rendezd helyes sorrendbe a szavakat!",
            "words": ["A", "Kárpát-medence", "a", "birodalmak", "ütközőzónájává", "vált."],
            "correctSentence": "A Kárpát-medence a birodalmak ütközőzónájává vált.",
            "english": "The Carpathian Basin became a buffer zone of empires.",
            "teaches": ["utkozozona", "fennhatosag"]
        },
        {
            "id": "b1-karpatmedence-05.ex07",
            "type": "multiple-choice",
            "title": "Környező hatalmak",
            "instruction": "Melyik birodalom fennhatósága alá tartozott a Dunántúl a 9. században?",
            "question": "Kik gyakoroltak felügyeletet a Balaton térségében a magyarok előtt?",
            "options": ["A Keleti Frank Királyság", "A Kínai Császárság", "A Spanyol Birodalom", "A Brit Korona"],
            "correctIndex": 0,
            "explanation": "A Dunántúl a Keleti Frank Királyság tartománya volt a 9. század folyamán.",
            "teaches": ["fennhatosag", "huberes"]
        },
        {
            "id": "b1-karpatmedence-05.ex08",
            "type": "fill-blank",
            "title": "Új haza születése",
            "instruction": "Egészítsd ki a mondatot!",
            "sentence": "A kedvező feltételek segítették a magyar törzsek letelepedését az új ___.",
            "correctAnswer": "hazában",
            "options": ["hazában", "hajóban", "felhőben", "erdőben"],
            "teaches": ["birtokba-vesz"]
        }
    ]
})

write_json(LESSONS_DIR / "b1-karpatmedence-05.json", make_lesson(
    "lesson.b1.karpatmedence-05",
    "A Kárpát-medence a 9. század végén (Eve of the Conquest)",
    "Feltételes mód és összefoglaló mondatszerkezetek",
    [
        "In this final topical lesson of Unit 2, we explore the geopolitical situation immediately before the Magyar conquest of 895.",
        "You will learn about Frankish dominion in Transdanubia, the princely seat of Mosaburg (Zalavár), the visits of Cyril and Methodius, and the power vacuum that welcomed Árpád's tribes.",
        "We also practice conditional sentences and historical discourse connectors."
    ],
    [
        "I can describe the fragmented geopolitical state of the Carpathian Basin on the eve of the Honfoglalás.",
        "I can explain the significance of Mosaburg (Zalavár) and Frankish-Slavic relations.",
        "I can identify the neighbouring powers (East Franks, Moravians, Bulgars) bordering the basin.",
        "I can use discourse markers and conditional forms to construct persuasive historical explanations."
    ],
    "stories/world/b1/b1-karpatmedence-05-honfoglalaselott.json",
    "vocabulary/b1/b1-karpatmedence-05-voc.json",
    "grammar/b1/b1-karpatmedence-05-gr.json",
    "exercises/b1/b1-karpatmedence-05-ex.json",
    [f"b1-karpatmedence-05.ex{i:02d}" for i in range(1, 9)]
))

# -----------------
# Consolidation Story, Exercises, Lesson
# -----------------
write_json(STORIES_DIR / "b1-karpatmedence.json", make_story(
    "story.b1.karpatmedence",
    "A Kárpát-medence a magyarok előtt",
    "A comprehensive historical overview of the Carpathian Basin before 895: Celts, Roman Pannonia, Huns under Attila, Avars, Slavs, and the prelude to the Honfoglalás.",
    "Kárpát-medence",
    ["összetett mondatok", "történeti igeidők"],
    ["Kárpát-medence története", "Népek és kultúrák"],
    [
        "A Kárpát-medence földrajzi adottságai – a védelmező hegykoszorú, a bővizű folyók és a termékeny síkságok – évezredeken át vonzották a vándorló és letelepedni vágyó népeket.",
        "A vaskor kelta kézművesei és hegyi erődítményei után a Római Birodalom megalapította Pannonia provinciát. A rómaiak kiépítették a dunai limest, szilárd úthálózatot, virágzó városokat és fejlett borkultúrát teremtettek a Dunántúlon.",
        "Az 5. században a népvándorlás vihara elmosta a római uralmat. Attila hunjai a Tisza mentéről irányították hatalmas európai birodalmukat, majd germán törzsek (gepidák, longobárdok) hoztak létre királyságokat.",
        "568-tól az Avar Kaganátus két és fél évszázados korszaka következett, amely a mezőgazdasággal foglalkozó szláv lakosság békés betelepülését és gazdag lovas nomád kultúrát hozott a medencébe.",
        "Amikor 895-ben Árpád vezetésével megérkeztek a magyar törzsek, egy gazdag történelmi rétegekkel teli, de egységes központi hatalom nélküli vidéket vehettek birtokba, megalapozva a magyar állam jövőjét."
    ],
    [
        {"lemma": "hegykoszorú", "pos": "noun", "cefr": "B1", "gloss": "ring of mountains"},
        {"lemma": "letelepedés", "pos": "noun", "cefr": "B1", "gloss": "settlement"},
        {"lemma": "történelmi korszak", "pos": "noun", "cefr": "B1", "gloss": "historical era"},
        {"lemma": "birtokbavétel", "pos": "noun", "cefr": "B1", "gloss": "taking possession / conquest"}
    ],
    [
        {
            "question": "Mely népek és birodalmak váltották egymást a Kárpát-medencében a honfoglalás előtt?",
            "options": ["Kelták, rómaiak, hunok, germánok, avarok és szlávok", "Csak a vikingek", "Kizárólag ókori görög városállamok", "Senki sem lakott a térségben"],
            "correctIndex": 0,
            "explanation": "A Kárpát-medence gazdag rétegekben kelták, rómaiak, hunok, germánok, avarok és szlávok otthona volt a magyarok előtt."
        },
        {
            "question": "Milyen tartós örökséget hagyott a Római Birodalom a Dunántúlon?",
            "options": ["Városokat, utakat, borkultúrát és ókeresztény emlékeket", "Gyárakat és autókat", "Piramisokat a Duna partján", "Semmilyen nyomuk nem maradt"],
            "correctIndex": 0,
            "explanation": "A rómaiak úthálózatot, városokat (Aquincum, Savaria, Sopianae) és virágzó borkultúrát hagytak hátra."
        },
        {
            "question": "Miért volt kedvező a geopolitikai helyzet a magyarok számára 895-ben?",
            "options": ["Mert nem létezett egységes központi hatalom a medencében", "Mert a frankok minden földet ingyen átadtak", "Mert hatalmas óceán védte a határokat", "Mert a római légiók segítették őket"],
            "correctIndex": 0,
            "explanation": "A hatalmi űr és a környező birodalmak széttagoltsága kedvezett a honfoglaló törzsek letelepedésének."
        }
    ]
))

cons_exercises = []
# 20 consolidation exercises
cons_exercises.append({
    "id": "b1-karpatmedence-consolidation.ex01",
    "type": "multiple-choice",
    "title": "Korai lakók",
    "instruction": "Válaszd ki a helyes választ!",
    "question": "Melyik nép épített oppidumoknak nevezett megerősített hegyi falvakat a vaskorban?",
    "options": ["A kelták", "A hunok", "A rómaiak", "A magyarok"],
    "correctIndex": 0,
    "explanation": "A kelták jellegzetes erődített magaslati települései voltak az oppidumok.",
    "teaches": ["oslakos", "eroditmeny"]
})
cons_exercises.append({
    "id": "b1-karpatmedence-consolidation.ex02",
    "type": "fill-blank",
    "title": "Római határvonal",
    "instruction": "Egészítsd ki a mondatot!",
    "sentence": "A Római Birodalom dunai megerősített határvonalát ___ nevezték.",
    "correctAnswer": "limesnek",
    "options": ["limesnek", "óceánnak", "oppidumnak", "szablyának"],
    "teaches": ["hatarvonal", "provincia"]
})
cons_exercises.append({
    "id": "b1-karpatmedence-consolidation.ex03",
    "type": "sentence-builder",
    "title": "Aquincum elhelyezkedése",
    "instruction": "Állítsd össze a mondatot!",
    "words": ["Aquincum", "a", "mai", "Óbuda", "területén", "virágzott."],
    "correctSentence": "Aquincum a mai Óbuda területén virágzott.",
    "english": "Aquincum flourished on the territory of modern Óbuda.",
    "teaches": ["telepules", "provincia"]
})
cons_exercises.append({
    "id": "b1-karpatmedence-consolidation.ex04",
    "type": "multiple-choice",
    "title": "Attila székhelye",
    "instruction": "Hol volt a hun birodalom központja?",
    "question": "Hol rendezte be királyi székhelyét Attila?",
    "options": ["A Tisza vidékén", "A tengerparton", "A Rajna torkolatánál", "Londonban"],
    "correctIndex": 0,
    "explanation": "Attila hun király a Tisza menti síkságon építette ki birodalmi központját.",
    "teaches": ["szekhely", "uralkodo"]
})
cons_exercises.append({
    "id": "b1-karpatmedence-consolidation.ex05",
    "type": "fill-blank",
    "title": "Avar régészet",
    "instruction": "Egészítsd ki a mondatot!",
    "sentence": "Az avar sírokban gyönyörű bronz és arany ___ találtak a kutatók.",
    "correctAnswer": "övdíszeket",
    "options": ["övdíszeket", "telefonokat", "automobilokat", "repülőket"],
    "teaches": ["ovdisz", "kincs"]
})
cons_exercises.append({
    "id": "b1-karpatmedence-consolidation.ex06",
    "type": "sentence-builder",
    "title": "Szláv földművelés",
    "instruction": "Rendezd helyes sorrendbe a szavakat!",
    "words": ["A", "szláv", "törzsek", "békés", "földműveléssel", "és", "állattartással", "foglalkoztak."],
    "correctSentence": "A szláv törzsek békés földműveléssel és állattartással foglalkoztak.",
    "english": "The Slavic tribes engaged in peaceful crop farming and animal husbandry.",
    "teaches": ["foldmuveles", "allattartas"]
})
cons_exercises.append({
    "id": "b1-karpatmedence-consolidation.ex07",
    "type": "multiple-choice",
    "title": "Zalavár szerepe",
    "instruction": "Mi volt Mosaburg (Zalavár) a 9. században?",
    "question": "Milyen központ működött a Balaton mellett a honfoglalás előtt?",
    "options": ["Frank hűbéres fejedelmi székhely templomokkal", "Lakatlan mocsár", "Római légiós kikötő", "Avar fegyvergyár"],
    "correctIndex": 0,
    "explanation": "Zalavár (Mosaburg) Pribina és fia, Kocel székhelyeként fontos frank-szláv keresztény központ volt.",
    "teaches": ["szekhely", "huberes"]
})
cons_exercises.append({
    "id": "b1-karpatmedence-consolidation.ex08",
    "type": "fill-blank",
    "title": "Hatalmi űr a medencében",
    "instruction": "Válaszd ki a megfelelő kifejezést!",
    "sentence": "A 9. század végén kialakult ___ megkönnyítette Árpád népének letelepedését.",
    "correctAnswer": "hatalmi űr",
    "options": ["hatalmi űr", "világháború", "tengeri vihar", "hómező"],
    "teaches": ["hatalmi-ur"]
})
cons_exercises.append({
    "id": "b1-karpatmedence-consolidation.ex09",
    "type": "sentence-builder",
    "title": "Pécsi sírkamrák",
    "instruction": "Állítsd össze a mondatot!",
    "words": ["Sopianae", "ókeresztény", "sírkamrái", "az", "UNESCO", "világörökség", "részei."],
    "correctSentence": "Sopianae ókeresztény sírkamrái az UNESCO világörökség részei.",
    "english": "The early Christian burial chambers of Sopianae are part of the UNESCO World Heritage.",
    "teaches": ["sirkamra", "vilagorokseg"]
})
cons_exercises.append({
    "id": "b1-karpatmedence-consolidation.ex10",
    "type": "multiple-choice",
    "title": "Avar lovas hadviselés",
    "instruction": "Milyen lovas eszközt terjesztettek el az avarok Európában?",
    "question": "Melyik találmány tette stabilabbá a harcost a nyeregben?",
    "options": ["A vaskengyel", "A gőzhajtású nyereg", "A műanyag kantár", "A kerékpárpedál"],
    "correctIndex": 0,
    "explanation": "A vaskengyel széles körű elterjesztése a lovas nomád népeknek, köztük az avaroknak köszönhető.",
    "teaches": ["kengyel", "haditechnika"]
})
cons_exercises.append({
    "id": "b1-karpatmedence-consolidation.ex11",
    "type": "fill-blank",
    "title": "Római borkultúra",
    "instruction": "Egészítsd ki a mondatot!",
    "sentence": "A Dunántúl dombjain a rómaiak honosították meg a virágzó ___.",
    "correctAnswer": "szőlőtermesztést",
    "options": ["szőlőtermesztést", "teafőzést", "kakaóültetést", "rizstermesztést"],
    "teaches": ["szolotermesztes"]
})
cons_exercises.append({
    "id": "b1-karpatmedence-consolidation.ex12",
    "type": "sentence-builder",
    "title": "Nagy Károly hadjáratai",
    "instruction": "Rendezd helyes sorrendbe a szavakat!",
    "words": ["Nagy", "Károly", "hadjáratai", "megdöntötték", "az", "Avar", "Kaganátust."],
    "correctSentence": "Nagy Károly hadjáratai megdöntötték az Avar Kaganátust.",
    "english": "Charlemagne's campaigns overthrew the Avar Khaganate.",
    "teaches": ["megdont", "hadjarat"]
})
cons_exercises.append({
    "id": "b1-karpatmedence-consolidation.ex13",
    "type": "multiple-choice",
    "title": "Kelta pénzverés",
    "instruction": "Mit bizonyít a kelta ezüstpénzek felfedezése?",
    "question": "Milyen gazdasági életről tanúskodnak a kelta érmék?",
    "options": ["Fejlett helyi és távolsági kereskedelemről", "Kizárólag primitív vándorlásról", "Semmilyen kapcsolatról más népekkel", "A pénz teljes hiányáról"],
    "correctIndex": 0,
    "explanation": "A saját pénzverés az önálló gazdaság és az élénk kereskedelem bizonyítéka.",
    "teaches": ["penzveres", "kereskedelem"]
})
cons_exercises.append({
    "id": "b1-karpatmedence-consolidation.ex14",
    "type": "fill-blank",
    "title": "Attila halála",
    "instruction": "Egészítsd ki a mondatot!",
    "sentence": "Attila halála után a Hun Birodalom belső viszályok miatt ___.",
    "correctAnswer": "felbomlott",
    "options": ["felbomlott", "megkettőződött", "feltámadt", "kitágult"],
    "teaches": ["felbomlik", "uralkodo"]
})
cons_exercises.append({
    "id": "b1-karpatmedence-consolidation.ex15",
    "type": "sentence-builder",
    "title": "Szláv apostolok",
    "instruction": "Állítsd össze a mondatot!",
    "words": ["Cirill", "és", "Metód", "megfordultak", "Zalavár", "templomaiban."],
    "correctSentence": "Cirill és Metód megfordultak Zalavár templomaiban.",
    "english": "Cyril and Methodius visited the churches of Zalavár.",
    "teaches": ["apostol", "megfordul"]
})
cons_exercises.append({
    "id": "b1-karpatmedence-consolidation.ex16",
    "type": "multiple-choice",
    "title": "Római városnevek",
    "instruction": "Melyik ókori név felel meg Szombathelynek?",
    "question": "Hogyan nevezték a rómaiak a mai Szombathely városát?",
    "options": ["Savaria", "Aquincum", "Sopianae", "Scarbantia"],
    "correctIndex": 0,
    "explanation": "Savaria a mai Szombathely ókori római neve volt.",
    "teaches": ["provincia", "telepules"]
})
cons_exercises.append({
    "id": "b1-karpatmedence-consolidation.ex17",
    "type": "fill-blank",
    "title": "Kárpátok védelme",
    "instruction": "Egészítsd ki a mondatot!",
    "sentence": "A hegykoszorú természetes ___ nyújtott a medencében élőknek.",
    "correctAnswer": "menedéket",
    "options": ["menedéket", "autópályát", "tengert", "akadályversenyt"],
    "teaches": ["menedek"]
})
cons_exercises.append({
    "id": "b1-karpatmedence-consolidation.ex18",
    "type": "sentence-builder",
    "title": "Honfoglalás 895",
    "instruction": "Rendezd helyes sorrendbe a mondatrészeket!",
    "words": ["Árpád", "magyarjai", "895-ben", "megérkeztek", "a", "Kárpát-medencébe."],
    "correctSentence": "Árpád magyarjai 895-ben megérkeztek a Kárpát-medencébe.",
    "english": "Árpád's Magyars arrived in the Carpathian Basin in 895.",
    "teaches": ["birtokba-vesz"]
})
cons_exercises.append({
    "id": "b1-karpatmedence-consolidation.ex19",
    "type": "multiple-choice",
    "title": "Gepidák lakhelye",
    "instruction": "Hol éltek a gepidák a hunok bukása után?",
    "question": "A Kárpát-medence melyik részén alapítottak királyságot a gepidák?",
    "options": ["A Tiszántúlon és Kelet-Magyarországon", "Az Atlanti-óceánon", "Csak az Alpok legmagasabb csúcsain", "Itália déli részén kizárólag"],
    "correctIndex": 0,
    "explanation": "A gepidák a Tiszántúlon és Erdély nyugati felén rendezkedtek be a hunok után.",
    "teaches": ["uralom", "nepvandorlas"]
})
cons_exercises.append({
    "id": "b1-karpatmedence-consolidation.ex20",
    "type": "fill-blank",
    "title": "Történelmi örökség",
    "instruction": "Egészítsd ki a mondatot!",
    "sentence": "A medencében élt korai népek gazdag tárgyi ___ hagytak maguk után.",
    "correctAnswer": "örökséget",
    "options": ["örökséget", "hóembert", "mobiltelefont", "űrrakétát"],
    "teaches": ["orokseg", "lelet"]
})

write_json(EXERCISES_DIR / "b1-karpatmedence-consolidation-ex.json", {"exercises": cons_exercises})

write_json(LESSONS_DIR / "b1-karpatmedence-consolidation.json", make_consolidation_lesson(
    "lesson.b1.karpatmedence-consolidation",
    "The Carpathian Basin Before the Magyars - Consolidation",
    [
        "Congratulations on completing Unit 2 of the Hungarian Citizenship Track!",
        "In this consolidation lesson, you review the complete pre-Hungarian history of the Carpathian Basin: Celtic Iron Age craftsmen, Roman Pannonia, Attila's Huns, the Germanic kingdoms, the Avar Khaganate, and Slavic settlements up to the eve of the 895 conquest.",
        "Take this opportunity to test your knowledge across all 20 consolidation exercises and solidify the vocabulary and grammar needed for the constitutional citizenship examination."
    ],
    [
        "I can summarize the key historical periods of the Carpathian Basin prior to 895.",
        "I can identify Roman landmarks, towns, and their lasting cultural legacy in Transdanubia.",
        "I can describe the nomadic cultures of the Huns and Avars and their archaeological finds.",
        "I can explain why the geopolitical situation in 895 enabled the successful Magyar conquest."
    ],
    "stories/world/b1/b1-karpatmedence.json",
    "exercises/b1/b1-karpatmedence-consolidation-ex.json",
    [f"b1-karpatmedence-consolidation.ex{i:02d}" for i in range(1, 21)]
))

print("Unit 2 (b1-karpatmedence) overhaul complete!")
