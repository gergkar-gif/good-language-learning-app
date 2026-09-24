# -*- coding: utf-8 -*-
"""
Complete Block 1 Builder (Units 2 to 6):
- Unit 2: b1-karpatmedence
- Unit 3: b1-honfoglalas
- Unit 4: b1-istvankiraly
- Unit 5: b1-arpadhaz
- Unit 6: b1-tatarjaras
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

# ==========================================
# UNIT 2: b1-karpatmedence
# ==========================================
print("Building Unit 2: b1-karpatmedence...")

# Unit 2 Lesson 1
u2_01_story = make_story(
    "story.b1.karpatmedence.01",
    "A medence korai népei",
    "Who lived in the Carpathian Basin long before the Magyars arrived: the Illyrian-related Pannon tribes, then the Celtic peoples who settled and left their mark on the land.",
    "Kárpát-medence",
    ["több alany és múlt idejű igei egyeztetés"],
    ["A medence korai népei", "Kelta települések"],
    [
        "Évszázadokkal a honfoglalás előtt a Kárpát-medence már sűrűn lakott, virágzó térség volt. A vaskor és az ókor idején kelta és illír törzsek népesítették be a Duna menti termékeny síkságokat és völgyeket.",
        "A kelták különösen fejlett anyagi kultúrával rendelkeztek. Ismerték a vasolvasztást, a fazekaskorong használatát, és erődített településeket, úgynevezett oppidumokat építettek a dombtetőkön.",
        "A régészeti leletek tanúsága szerint a kelta kézművesek és kereskedők kiterjedt kapcsolatokat ápoltak a Földközi-tenger térségével. Pénzt is vertek, ami élénk kereskedelmi életről tanúskodik.",
        "A Kárpátok természetes koszorúja már ekkor is védelmet és menedéket nyújtott az itt élő népeknek a külső támadásokkal szemben.",
        "Ezek a korai kultúrák mély nyomot hagytak a tájban és a földrajzi nevekben, előkészítve a terepet a későbbi birodalmi hódítások számára."
    ],
    [
        {"lemma": "őslakos", "pos": "noun", "cefr": "B1", "gloss": "indigenous inhabitant / native"},
        {"lemma": "letelepedik", "pos": "verb", "cefr": "B1", "gloss": "to settle down"},
        {"lemma": "kézművesség", "pos": "noun", "cefr": "B1", "gloss": "handicraft / craftmanship"},
        {"lemma": "erődítmény", "pos": "noun", "cefr": "B1", "gloss": "fortification / stronghold"}
    ],
    [
        {
            "question": "Melyik nép élt a Kárpát-medencében a római hódítás előtt a vaskorban?",
            "options": ["A kelták és illír törzsek", "A honfoglaló magyarok", "A szláv fejedelmek", "A török csapatok"],
            "correctIndex": 0,
            "explanation": "A vaskorban a kelták és illír törzsek népesítették be a Kárpát-medencét."
        },
        {
            "question": "Milyen technológiai és gazdasági vívmányokat hoztak a kelták?",
            "options": ["Gőzgépeket és gyárakat", "Vasolvasztást, fazekaskorongot és pénzverést", "Piramisokat és kőolajbányászatot", "Csak egyszerű faeszközöket"],
            "correctIndex": 1,
            "explanation": "A kelták ismerték a vasolvasztást, a fazekaskorongot és kiterjedt kereskedelmet folytattak, még pénzt is vertek."
        },
        {
            "question": "Mi jellemezte a kelták településeit?",
            "options": ["Vándorló sátortáborokban laktak", "Erődített településeket (oppidumokat) építettek dombtetőkön", "Földalatti barlangokban éltek kizárólag", "Óceáni kikötővárosokat alapítottak"],
            "correctIndex": 1,
            "explanation": "A kelták erődített településeket, úgynevezett oppidumokat hoztak létre dombtetőkön."
        }
    ]
)
write_json(STORIES_DIR / "b1-karpatmedence-01-korainepek.json", u2_01_story)

u2_01_voc = {
    "title": "A medence korai népei",
    "words": [
        {"lemma": "őslakos", "pos": "noun", "cefr": "B1", "translation": "indigenous inhabitant / native", "examples": [{"hungarian": "A kelták a térség korai őslakosai közé tartoztak.", "english": "The Celts were among the early native inhabitants of the region."}]},
        {"lemma": "törzs", "pos": "noun", "cefr": "B1", "translation": "tribe", "examples": [{"hungarian": "Több kelta törzs élt a Duna völgyében.", "english": "Several Celtic tribes lived in the Danube valley."}]},
        {"lemma": "vaskor", "pos": "noun", "cefr": "B1", "translation": "Iron Age", "examples": [{"hungarian": "A vaskor idején fejlett technológiák jelentek meg.", "english": "During the Iron Age, advanced technologies appeared."}]},
        {"lemma": "letelepedik", "pos": "verb", "cefr": "B1", "translation": "to settle down", "examples": [{"hungarian": "A pásztornépek letelepedtek a termékeny völgyben.", "english": "The pastoral peoples settled down in the fertile valley."}]},
        {"lemma": "erődítmény", "pos": "noun", "cefr": "B1", "translation": "fortification / fort", "examples": [{"hungarian": "Erős erődítményt emeltek a domb tetején.", "english": "They erected a strong fortification on the hilltop."}]},
        {"lemma": "település", "pos": "noun", "cefr": "B1", "translation": "settlement", "examples": [{"hungarian": "A folyó mentén virágzó települések jöttek létre.", "english": "Prospering settlements came into being along the river."}]},
        {"lemma": "kézművesség", "pos": "noun", "cefr": "B1", "translation": "handicraft / craft", "examples": [{"hungarian": "A fémfeldolgozás és a kézművesség magas szintű volt.", "english": "Metalworking and handicraft were of a high level."}]},
        {"lemma": "kereskedelem", "pos": "noun", "cefr": "B1", "translation": "trade / commerce", "examples": [{"hungarian": "A távolsági kereskedelem összekötötte a medencét a déli vidékekkel.", "english": "Long-distance trade connected the basin with southern regions."}]},
        {"lemma": "lelet", "pos": "noun", "cefr": "B1", "translation": "find / archaeological artifact", "examples": [{"hungarian": "A régészeti leletek gazdag kultúráról tanúskodnak.", "english": "The archaeological finds testify to a rich culture."}]},
        {"lemma": "pénzverés", "pos": "noun", "cefr": "B1", "translation": "coinage / minting", "examples": [{"hungarian": "A kelta pénzverés az önálló gazdaság bizonyítéka.", "english": "Celtic coinage is evidence of an independent economy."}]},
        {"lemma": "tanúskodik", "pos": "verb", "cefr": "B1", "translation": "to testify / bear witness", "examples": [{"hungarian": "A sírok gazdagsága virágzó társadalomról tanúskodik.", "english": "The wealth of the graves testifies to a flourishing society."}]},
        {"lemma": "menedék", "pos": "noun", "cefr": "B1", "translation": "shelter / refuge", "examples": [{"hungarian": "A hegyek biztonságos menedéket nyújtottak a lakosságnak.", "english": "The mountains offered safe shelter to the population."}]}
    ]
}
write_json(VOCAB_DIR / "b1-karpatmedence-01-voc.json", u2_01_voc)

u2_01_gr = {
    "title": "Múlt idejű igék és alany-ige egyeztetés történeti leírásban",
    "level": "B1",
    "rules": [
        {
            "id": "past-tense-narrative",
            "title": "Past Tense in Historical Narratives",
            "text": "When narrating past historical events in Hungarian, we use past tense suffixes (*-t / -tt*). When plural subjects (*kelták, törzsek, telepesek*) perform an action, the verb must agree in plural (*-tak / -tek, -ttak / -ttek*).",
            "tip": "Distinguish between indefinite past (*letelepedtek*) and definite past (*felépítették az erődítményt*)."
        },
        {
            "id": "locative-postpositions",
            "title": "Locative Noun Endings for Settlements",
            "text": "Describing where tribes lived uses locative suffixes like *-ban / -ben* (inside a region: *a Kárpát-medencében, a völgyben*), *-n / -on / -en / -ön* (on a surface: *a dombtetőn, a síkságon*), and *-nál / -nél* (by a river: *a Dunánál*).",
            "tip": "Pay close attention to vowel harmony: *medencé-ben*, but *folyó-nál*."
        }
    ],
    "examples": [
        {"spanish": "A kelta törzsek letelepedtek a termékeny Kárpát-medencében.", "english": "The Celtic tribes settled down in the fertile Carpathian Basin."},
        {"spanish": "Erős erődítményeket építettek a folyók mentén.", "english": "They built strong fortifications along the rivers."},
        {"spanish": "A régészeti leletek virágzó kultúráról tanúskodnak.", "english": "The archaeological finds testify to a flourishing culture."}
    ]
}
write_json(GRAMMAR_DIR / "b1-karpatmedence-01-gr.json", u2_01_gr)

u2_01_ex = {
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
            "options": ["Pénzt vertek és távoli vidékekkel kereskedtek", "Nem volt semmilyen kapcsolatuk más népekkel", "Csak cserekereskedelmet folytattak kőbaltákkal", "Minden árut tengeri kikötőben adtak el"],
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
}
write_json(EXERCISES_DIR / "b1-karpatmedence-01-ex.json", u2_01_ex)

u2_01_les = make_lesson(
    "lesson.b1.karpatmedence-01",
    "A medence korai népei (Early Peoples of the Basin)",
    "Múlt idejű igék és alany-ige egyeztetés történeti leírásban",
    [
        "Welcome to Unit 2 of the Hungarian Citizenship Track. Before exploring the Hungarian state and national history, we examine the rich history of the Carpathian Basin before the arrival of the Magyars.",
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
)
write_json(LESSONS_DIR / "b1-karpatmedence-01.json", u2_01_les)

print("Unit 2 Lesson 1 generated successfully.")
