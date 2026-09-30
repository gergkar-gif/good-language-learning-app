# -*- coding: utf-8 -*-
"""
Full Unit 9 Overhaul: The Battle of Mohács (b1-mohacs)
Lessons:
1. A Jagelló-kor és az ország belső válsága
2. Nándorfehérvár eleste (1521) és a török fenyegetés
3. A mohácsi csata (1526. augusztus 29.)
4. Kettős királyválasztás és az ország kettészakadása
5. A középkori állam bukása és a mohácsi trauma emlékezete
Consolidation: Unit 9 Capstone (20 exercises)
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
# LESSON 1: b1-mohacs-01 (A Jagelló-kor és az ország gyengülése)
# ==========================================
story_1 = make_story(
    "story.b1.mohacs.01",
    "A Jagelló-kor és az ország belső válsága",
    "Mátyás király halála után Magyarország gazdasági és katonai helyzete meggyengült a Jagelló uralkodók idején.",
    "Buda és Visegrád",
    ["Causal conjunctions (mivel, minthogy, amiatt, hogy)", "Past tense descriptive reporting"],
    ["Jagelló-kor", "királyi hatalom", "kincstár", "nemesség"],
    [
        "Hunyadi Mátyás 1490-ben bekövetkezett váratlan halála után a magyar rendek gyenge kezű uralkodót kerestek, hogy visszaszerezzék korábbi kiváltságaikat. Így választották meg a cseh királyt, Jagelló II. Ulászlót, akit a népnyelv 'Dobzse László' néven emlegetett, mivel szinte minden javaslatra rábólintott.",
        "Mátyás hírhedt és költséges fekete seregét a királyi kincstár kiürülése miatt feloszlatták. Minthogy a nemesség megtagadta az adófizetést, a központi királyi hatalom gyorsan elenyészett, és az országnak nem maradt ütőképes állandó hadereje.",
        "A belső viszályok és a pénzhiány miatt a déli végvári vonal karbantartása is elmaradt. Amikor 1516-ban a gyermek II. Lajos került a trónra, a Magyar Királyság védtelenül állt a dinamikusan terjeszkedő Oszmán Birodalommal szemben."
    ],
    [
        {"lemma": "kincstár", "pos": "noun", "cefr": "B1", "gloss": "royal treasury"},
        {"lemma": "feloszlat", "pos": "verb", "cefr": "B1", "gloss": "to disband, dissolve"},
        {"lemma": "viszály", "pos": "noun", "cefr": "B1", "gloss": "strife, discord"},
        {"lemma": "kiváltság", "pos": "noun", "cefr": "B1", "gloss": "privilege"},
        {"lemma": "ütőképes", "pos": "adjective", "cefr": "B1", "gloss": "battle-ready, effective"}
    ],
    [
        {
            "question": "Miért oszlatták fel a fekete sereget Mátyás halála után?",
            "options": ["Mert a kincstár kiürült és a nemesek nem fizettek adót", "Mert békét kötöttek a törökökkel", "Mert a katonák elmentek Bécsbe", "Mert a király nem akart sereget"],
            "correctIndex": 0,
            "explanation": "A kincstár kiürülése és az adók elmaradása miatt nem tudták fizetni a zsoldosokat."
        }
    ]
)
write_json(STORIES_DIR / "story.b1.mohacs.01.json", story_1)

voc_1 = {
    "id": "voc.b1.mohacs.01",
    "title": "A Jagelló-kor szókincse",
    "description": "A belső hanyatlás, a királyi hatalom és a hadsereg feloszlatásának fogalmai.",
    "entries": [
        {"lemma": "kincstár", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "royal treasury, public purse", "examples": [{"hu": "A kincstár teljesen kiürült a zsoldosok fizetése nélkül.", "en": "The treasury was completely emptied without pay for the mercenaries."}]}]},
        {"lemma": "feloszlat", "pos": "verb", "cefr": "B1", "definitions": [{"meaning": "to disband, dissolve", "examples": [{"hu": "A király kénytelen volt feloszlatni az állandó hadsereget.", "en": "The king was forced to disband the standing army."}]}]},
        {"lemma": "viszály", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "internal strife, conflict", "examples": [{"hu": "A belső viszályok gyengítették az ország védelmét.", "en": "Internal strifes weakened the country's defense."}]}]},
        {"lemma": "kiváltság", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "privilege, noble entitlement", "examples": [{"hu": "A nemesek ragaszkodtak ősi kiváltságaikhoz.", "en": "The nobles insisted on their ancient privileges."}]}]},
        {"lemma": "zsoldos", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "mercenary", "examples": [{"hu": "A zsoldosok fizetség hiányában elhagyták a várakat.", "en": "Lacking payment, the mercenaries abandoned the fortresses."}]}]}
    ]
}
write_json(VOCAB_DIR / "voc.b1.mohacs.01.json", voc_1)

gr_1 = {
    "id": "gr.b1.mohacs.01",
    "title": "Okhatározói kötőszavak: mivel, minthogy, amiatt, hogy",
    "description": "Expressing cause and reasoning in complex sentences using 'mivel', 'minthogy', and 'amiatt, hogy'.",
    "rules": [
        "A 'mivel' és 'minthogy' okhatározói mellékmondatokat vezet be, amelyek megelőzhetik vagy követhetik a főmondatot.",
        "Az 'amiatt, hogy' szerkezet nyomatékosítja az okot a főmondatban található utalószóval ('amiatt')."
    ],
    "tables": [
        {"headers": ["Kötőszó", "Jelentés", "Példa"], "rows": [
            ["mivel", "since, because", "Mivel nem volt pénz, a sereg feloszlott."],
            ["minthogy", "as, seeing that", "Minthogy a király gyenge volt, a nemesek döntöttek."],
            ["amiatt, hogy", "due to the fact that", "Amiatt vesztettek, hogy nem érkezett segítség."]
        ]}
    ],
    "examples": [
        {"spanish": "Mivel a kincstár kiürült, nem tudták fenntartani a fekete sereget.", "english": "Since the treasury was emptied, they could not maintain the Black Army."},
        {"spanish": "Minthogy a főurak viszálykodtak, az ország védelme összeomlott.", "english": "As the magnates quarreled, the country's defense collapsed."},
        {"spanish": "A királyi hatalom amiatt gyengült meg, hogy nem szedtek be adókat.", "english": "Royal power weakened due to the fact that taxes were not collected."}
    ]
}
write_json(GRAMMAR_DIR / "gr.b1.mohacs.01.json", gr_1)

exs_1 = [
    {"id": "ex.b1.mohacs.01.01", "type": "multiple-choice", "lesson": "lesson.b1.mohacs.01", "teaches": ["kincstar"], "prompt": "Melyik kifejezés jelenti az állam vagy a király pénzügyi alapját?", "options": ["Kincstár", "Végvár", "Hódoltság", "Püspökség"], "correctIndex": 0, "explanation": "A kincstár a királyi és állami jövedelmek őrzőhelye és kezelője."},
    {"id": "ex.b1.mohacs.01.02", "type": "fill-blank", "lesson": "lesson.b1.mohacs.01", "teaches": ["feloszlat"], "prompt": "Egészítsd ki a mondatot a megfelelő igealakkal!", "sentence": "Pénz hiányában a király kénytelen volt *feloszlatni* a hadsereget.", "target": "feloszlatni"},
    {"id": "ex.b1.mohacs.01.03", "type": "sentence-builder", "lesson": "lesson.b1.mohacs.01", "teaches": ["mivel", "kincstar"], "prompt": "Rakd össze a mondatot helyes sorrendben!", "chips": ["Mivel", "a", "kincstár", "kiürült,", "a", "sereg", "feloszlott."], "target": "Mivel a kincstár kiürült, a sereg feloszlott.", "english": "Since the treasury was empty, the army disbanded."},
    {"id": "ex.b1.mohacs.01.04", "type": "multiple-choice", "lesson": "lesson.b1.mohacs.01", "teaches": ["viszaly"], "prompt": "Mit jelent a 'belső viszály' a politikában?", "options": ["A nemesek és vezetők közötti ellenségeskedést és harcot", "A határok védelmét", "Az új törvények békés elfogadását", "A külföldi kereskedelmet"], "correctIndex": 0, "explanation": "A viszály belső széthúzást és harcot jelent."},
    {"id": "ex.b1.mohacs.01.05", "type": "fill-blank", "lesson": "lesson.b1.mohacs.01", "teaches": ["kiváltság"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A nemesség ragaszkodott a korábbi *kiváltságaihoz* és mentességeihez.", "target": "kiváltságaihoz"},
    {"id": "ex.b1.mohacs.01.06", "type": "sentence-builder", "lesson": "lesson.b1.mohacs.01", "teaches": ["minthogy", "viszaly"], "prompt": "Rakd össze a helyes mondatot!", "chips": ["Minthogy", "viszály", "volt,", "az", "ország", "meggyengült."], "target": "Minthogy viszály volt, az ország meggyengült.", "english": "Seeing that there was discord, the country weakened."},
    {"id": "ex.b1.mohacs.01.07", "type": "multiple-choice", "lesson": "lesson.b1.mohacs.01", "teaches": ["zsoldos"], "prompt": "Kik voltak a zsoldos katonák?", "options": ["Pénzért, fizetésért szolgáló harcosok", "Önkéntes parasztok", "Csak a király rokonai", "Külföldi diplomaták"], "correctIndex": 0, "explanation": "A zsoldosok fizetésért (zsoldért) harcoltak."},
    {"id": "ex.b1.mohacs.01.08", "type": "fill-blank", "lesson": "lesson.b1.mohacs.01", "teaches": ["utokepes"], "prompt": "Egészítsd ki a mondatot a megfelelő melléknévvel!", "sentence": "Az országnak nem maradt *ütőképes* állandó hadereje.", "target": "ütőképes"}
]
write_json(EXERCISES_DIR / "ex.b1.mohacs.01.json", make_exercise_group("ex.b1.mohacs.01", "A Jagelló-kor gyakorlása", "Gyakorlatok a korszak politikai válságáról.", exs_1))

lesson_1 = make_lesson(
    "lesson.b1.mohacs.01",
    "A Jagelló-kor és az ország belső válsága",
    "Okhatározói kötőszavak (mivel, minthogy, amiatt, hogy)",
    "Ebben a leckében megismerkedünk a Mátyás király halála utáni belső hanyatlással és a hadsereg szétesésével.",
    ["Megérteni a központi királyi hatalom meggyengülésének okait", "Használni az okhatározói kötőszavakat összetett mondatokban", "Ismerni a kincstár, viszály és feloszlatás fogalmait"],
    "story.b1.mohacs.01",
    "voc.b1.mohacs.01",
    "gr.b1.mohacs.01",
    "ex.b1.mohacs.01",
    [e["id"] for e in exs_1]
)
write_json(LESSONS_DIR / "lesson.b1.mohacs.01.json", lesson_1)


# ==========================================
# LESSON 2: b1-mohacs-02 (Nándorfehérvár eleste 1521)
# ==========================================
story_2 = make_story(
    "story.b1.mohacs.02",
    "Nándorfehérvár eleste (1521) és a török fenyegetés",
    "1520-ban I. Szulejmán szultán lépett az Oszmán Birodalom trónjára, és 1521-ben elfoglalta Magyarország déli kapuját, Nándorfehérvárt.",
    "Nándorfehérvár (Belgrád)",
    ["Temporal structures (miután, mielőtt, amint, mihelyt)", "Past tense narratives"],
    ["Nándorfehérvár", "ostrom", "végvári kapu", "Szulejmán szultán"],
    [
        "1520-ban új, ambiciózus uralkodó került a török birodalom élére: I. Szulejmán szultán. Mihelyt trónra lépett, azonnal Magyarország felé fordította hatalmas haderejét, mivel Európa szívét kívánta meghódítani.",
        "1521 nyarán a szultán serege ostrom alá vette Nándorfehérvárt, az ország legfontosabb déli erősségét. A várvédők hősiesen harcoltak Oláh Balázs vezetésével, de mielőtt a királyi segítség megérkezhetett volna, a falak leomlottak, és a vár augusztus végén elesett.",
        "Nándorfehérvár elestével megnyílt a kapu a Magyar Királyság belső területei felé. Miután a déli védelmi vonal kulcsa elveszett, az oszmán hadsereg számára szabad út nyílt Buda és a Duna menti síkságok irányába."
    ],
    [
        {"lemma": "ostrom", "pos": "noun", "cefr": "B1", "gloss": "siege"},
        {"lemma": "védvonal", "pos": "noun", "cefr": "B1", "gloss": "defense line"},
        {"lemma": "erősség", "pos": "noun", "cefr": "B1", "gloss": "stronghold, fortress"},
        {"lemma": "leomlik", "pos": "verb", "cefr": "B1", "gloss": "to collapse, crumble down"},
        {"lemma": "elesik", "pos": "verb", "cefr": "B1", "gloss": "to fall (fortress or battle)"}
    ],
    [
        {
            "question": "Miért volt katasztrófa Nándorfehérvár 1521-es eleste?",
            "options": ["Mert Nándorfehérvár volt a déli határok legfontosabb védelmi kulcsa", "Mert ott volt a királyi kincstár", "Mert a szultán ott halt meg", "Mert a nemesség ott ülésezett"],
            "correctIndex": 0,
            "explanation": "Nándorfehérvár ('Magyarország kapuja') biztosította a déli védelmi vonalat."
        }
    ]
)
write_json(STORIES_DIR / "story.b1.mohacs.02.json", story_2)

voc_2 = {
    "id": "voc.b1.mohacs.02",
    "title": "A nándorfehérvári ostrom szókincse",
    "description": "Várvédelem, ostrom, védvonal és katonai veszteségek kifejezései.",
    "entries": [
        {"lemma": "ostrom", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "siege", "examples": [{"hu": "A szultán serege hosszas ostrom után bevette a várat.", "en": "The Sultan's army took the castle after a lengthy siege."}]}]},
        {"lemma": "erősség", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "stronghold, fortified bastion", "examples": [{"hu": "Nándorfehérvár volt a déli határ legfőbb erőssége.", "en": "Nándorfehérvár was the southern border's main stronghold."}]}]},
        {"lemma": "védvonal", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "defense line", "examples": [{"hu": "A déli védvonal összeomlott a vár elestével.", "en": "The southern defense line collapsed with the fall of the castle."}]}]},
        {"lemma": "leomlik", "pos": "verb", "cefr": "B1", "definitions": [{"meaning": "to crumble down, collapse", "examples": [{"hu": "Az ágyútűz miatt a kőfalak leomlottak.", "en": "Due to the cannon fire, the stone walls crumbled down."}]}]},
        {"lemma": "elesik", "pos": "verb", "cefr": "B1", "definitions": [{"meaning": "to fall in battle / to fall (fortress)", "examples": [{"hu": "1521-ben Nándorfehérvár elesett.", "en": "In 1521, Nándorfehérvár fell."}]}]}
    ]
}
write_json(VOCAB_DIR / "voc.b1.mohacs.02.json", voc_2)

gr_2 = {
    "id": "gr.b1.mohacs.02",
    "title": "Időhatározói kötőszavak: miután, mielőtt, amint, mihelyt",
    "description": "Expressing temporal relations and sequence of historical events.",
    "rules": [
        "A 'miután' (after) előidejűséget fejez ki: a mellékmondatban leírt esemény korábban történt, mint a főmondat.",
        "A 'mielőtt' (before) utóidejűséget fejez ki: a főmondat eseménye előbb következett be, mint a mellékmondaté.",
        "A 'mihelyt' és 'amint' (as soon as) azonnali egymásutániságot jelez."
    ],
    "tables": [
        {"headers": ["Kötőszó", "Jelentés", "Példa"], "rows": [
            ["miután", "after", "Miután a vár elesett, megnyílt az út."],
            ["mielőtt", "before", "Mielőtt a sereg megérkezett, a fal leomlott."],
            ["mihelyt", "as soon as", "Mihelyt trónra lépett, hadjáratot indított."]
        ]}
    ],
    "examples": [
        {"spanish": "Miután Nándorfehérvár elesett, a törökök elérték a Duna vonalát.", "english": "After Nándorfehérvár fell, the Turks reached the Danube line."},
        {"spanish": "Mielőtt a segítség megérkezett volna, a védők kénytelenek voltak feladni a várat.", "english": "Before help could arrive, the defenders were forced to surrender the castle."},
        {"spanish": "Mihelyt Szulejmán hadat üzent, megindultak az oszmán csapatok.", "english": "As soon as Suleiman declared war, the Ottoman troops advanced."}
    ]
}
write_json(GRAMMAR_DIR / "gr.b1.mohacs.02.json", gr_2)

exs_2 = [
    {"id": "ex.b1.mohacs.02.01", "type": "multiple-choice", "lesson": "lesson.b1.mohacs.02", "teaches": ["ostrom"], "prompt": "Melyik évben esett el Nándorfehérvár Szulejmán szultán ostroma alatt?", "options": ["1521-ben", "1456-ban", "1526-ban", "1541-ben"], "correctIndex": 0, "explanation": "Nándorfehérvár 1521-ben került török kézre."},
    {"id": "ex.b1.mohacs.02.02", "type": "fill-blank", "lesson": "lesson.b1.mohacs.02", "teaches": ["leomlik"], "prompt": "Egészítsd ki a mondatot a megfelelő múlt idejű igealakkal!", "sentence": "Az ágyúzástól a vár fala *leomlott* az ostrom során.", "target": "leomlott"},
    {"id": "ex.b1.mohacs.02.03", "type": "sentence-builder", "lesson": "lesson.b1.mohacs.02", "teaches": ["miutan", "vedvonal"], "prompt": "Alkoss helyes mondatot a megadott szavakból!", "chips": ["Miután", "a", "vár", "elesett,", "a", "védvonal", "összeomlott."], "target": "Miután a vár elesett, a védvonal összeomlott.", "english": "After the fortress fell, the defense line collapsed."},
    {"id": "ex.b1.mohacs.02.04", "type": "multiple-choice", "lesson": "lesson.b1.mohacs.02", "teaches": ["erosség"], "prompt": "Mit nevezünk katonai értelemben 'erősségnek'?", "options": ["Megerősített várat vagy erődítményt", "A király testi erejét", "A legdrágább fegyvert", "A lovasság rohamát"], "correctIndex": 0, "explanation": "Az erősség erődöt, stratégiailag védett várat jelent."},
    {"id": "ex.b1.mohacs.02.05", "type": "fill-blank", "lesson": "lesson.b1.mohacs.02", "teaches": ["mielott"], "prompt": "Egészítsd ki a hiányzó kötőszóval!", "sentence": "A vár elesett, *mielőtt* a felmentő sereg megérkezett volna.", "target": "mielőtt"},
    {"id": "ex.b1.mohacs.02.06", "type": "sentence-builder", "lesson": "lesson.b1.mohacs.02", "teaches": ["mihelyt", "ostrom"], "prompt": "Rakd össze a mondatot!", "chips": ["Mihelyt", "a", "szultán", "megérkezett,", "elkezdődött", "az", "ostrom."], "target": "Mihelyt a szultán megérkezett, elkezdődött az ostrom.", "english": "As soon as the Sultan arrived, the siege began."},
    {"id": "ex.b1.mohacs.02.07", "type": "multiple-choice", "lesson": "lesson.b1.mohacs.02", "teaches": ["elesik"], "prompt": "Mit jelent az, hogy 'a vár elesett'?", "options": ["Az ellenség elfoglalta a várat", "A vár összedőlt egy földrengésben", "A katonák elhagyták a várat harc nélkül", "A vár megújult"], "correctIndex": 0, "explanation": "A vár eleste azt jelenti, hogy az ellenség bevette, elfoglalta."},
    {"id": "ex.b1.mohacs.02.08", "type": "fill-blank", "lesson": "lesson.b1.mohacs.02", "teaches": ["vedvonal"], "prompt": "Egészítsd ki a mondatot!", "sentence": "Nándorfehérvár volt a déli *védvonal* legfontosabb bástyája.", "target": "védvonal"}
]
write_json(EXERCISES_DIR / "ex.b1.mohacs.02.json", make_exercise_group("ex.b1.mohacs.02", "Nándorfehérvár ostroma gyakorlatok", "Gyakorlatok az 1521-es ostromról és a török előrenyomulásról.", exs_2))

lesson_2 = make_lesson(
    "lesson.b1.mohacs.02",
    "Nándorfehérvár eleste (1521) és a török fenyegetés",
    "Időhatározói kötőszavak (miután, mielőtt, mihelyt)",
    "Megismerjük Szulejmán szultán 1521-es hadjáratát és Nándorfehérvár elestének sorsdöntő következményeit.",
    ["Megérteni az 1521-es év jelentőségét", "Használni a 'miután', 'mielőtt' és 'mihelyt' kötőszavakat", "Alkalmazni a várostrommal és védelmi vonallal kapcsolatos szókincset"],
    "story.b1.mohacs.02",
    "voc.b1.mohacs.02",
    "gr.b1.mohacs.02",
    "ex.b1.mohacs.02",
    [e["id"] for e in exs_2]
)
write_json(LESSONS_DIR / "lesson.b1.mohacs.02.json", lesson_2)


# ==========================================
# LESSON 3: b1-mohacs-03 (A mohácsi csata 1526)
# ==========================================
story_3 = make_story(
    "story.b1.mohacs.03",
    "A mohácsi csata: 1526. augusztus 29.",
    "A mohácsi síkon a Tomori Pál és II. Lajos által vezetett magyar sereg alig két óra alatt megsemmisítő vereséget szenvedett a szultán túlerőben lévő hadaitól.",
    "Mohácsi sík és Csele-patak",
    ["Participles in narrative descriptions (-va/-ve, -ó/-ő, -ott/-ett)", "Cause and effect in historical writing"],
    ["mohácsi csata", "túlerő", "fővezér", "Tomori Pál", "Csele-patak"],
    [
        "1526 nyarán Szulejmán szultán több mint hatvanezer fős reguláris és tüzérséggel felszerelt hadsereggel vonult Magyarország ellen. A magyar királyi hadsereg mindössze mintegy huszonötezer katonát számlált, és a parancsnokságot Tomori Pál kalocsai érsekre és Szapolyai Györgyre bízták.",
        "1526. augusztus 29-én délután a mohácsi síkon megindult az összecsapás. A magyar nehézlovasság bátor rohama kezdetben sikeresnek látszott, áttörve a ruméliai hadtest vonalát, de a szultán ágyúi és a fegyelmezett janicsárok pusztító sortüze megtörte a lendületet.",
        "Alig másfél-két óra leforgása alatt a magyar sereg teljesen felmorzsolódott. A menekülő fiatal király, a húszéves II. Lajos a megáradt Csele-patakba fulladt, miután páncélos lova maga alá temette. A csatamezőn elesett a magyar püspöki kar többsége, számos főúr és több tízezer vitéz."
    ],
    [
        {"lemma": "túlerő", "pos": "noun", "cefr": "B1", "gloss": "numerical superiority, overwhelming force"},
        {"lemma": "összecsapás", "pos": "noun", "cefr": "B1", "gloss": "clash, encounter"},
        {"lemma": "tüzérség", "pos": "noun", "cefr": "B1", "gloss": "artillery"},
        {"lemma": "felmorzsolódik", "pos": "verb", "cefr": "B1", "gloss": "to be decimated, ground down"},
        {"lemma": "megsemmisítő", "pos": "adjective", "cefr": "B1", "gloss": "crushing, annihilating"}
    ],
    [
        {
            "question": "Mikor zajlott a mohácsi csata és mi lett a király sorsa?",
            "options": ["1526. augusztus 29-én; II. Lajos a Csele-patakba fulladt", "1541-ben; a király fogságba esett", "1456-ban; a király győzött", "1335-ben; békét kötöttek"],
            "correctIndex": 0,
            "explanation": "1526. augusztus 29-én II. Lajos menekülés közben a Csele-patakba fulladt."
        }
    ]
)
write_json(STORIES_DIR / "story.b1.mohacs.03.json", story_3)

voc_3 = {
    "id": "voc.b1.mohacs.03",
    "title": "A mohácsi csata szókincse",
    "description": "A csata menete, katonai túlerő, tüzérség és a vereség kifejezései.",
    "entries": [
        {"lemma": "túlerő", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "numerical superiority, overwhelming force", "examples": [{"hu": "A magyar sereg nem bírt az ellenséges túlerővel.", "en": "The Hungarian army could not cope with the enemy's numerical superiority."}]}]},
        {"lemma": "összecsapás", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "clash, battle encounter", "examples": [{"hu": "A sorsdöntő összecsapás alig két órán át tartott.", "en": "The decisive clash lasted barely two hours."}]}]},
        {"lemma": "tüzérség", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "artillery", "examples": [{"hu": "A török tüzérség ágyúi megsemmisítették a lovasrohamot.", "en": "The cannons of the Ottoman artillery destroyed the cavalry charge."}]}]},
        {"lemma": "felmorzsolódik", "pos": "verb", "cefr": "B1", "definitions": [{"meaning": "to be ground down, decimated", "examples": [{"hu": "A magyar hadsereg teljesen felmorzsolódott a harcban.", "en": "The Hungarian army was completely decimated in the fight."}]}]},
        {"lemma": "megsemmisítő", "pos": "adjective", "cefr": "B1", "definitions": [{"meaning": "crushing, crushing defeat", "examples": [{"hu": "A csata megsemmisítő vereséggel ért véget.", "en": "The battle ended in a crushing defeat."}]}]}
    ]
}
write_json(VOCAB_DIR / "voc.b1.mohacs.03.json", voc_3)

gr_3 = {
    "id": "gr.b1.mohacs.03",
    "title": "Határozói és melléknévi igenevek (-va/-ve, -ó/-ő, -ott/-ett)",
    "description": "Using participles in descriptive historical narrative and clause condensing.",
    "rules": [
        "A határozói igenév (-va/-ve) állapotot vagy párhuzamos cselekvést fejez ki: 'áttörve a vonalat', 'menekülve'.",
        "A folyamatos melléknévi igenév (-ó/-ő) folyamatban lévő tulajdonságot jelez: 'pusztító sortűz', 'menekülő király'.",
        "A befejezett melléknévi igenév (-ott/-ett/-t) lezárult cselekvés eredményét jelöli: 'felszerelt hadsereg', 'megáradt patak'."
    ],
    "tables": [
        {"headers": ["Típus", "Képző", "Példa"], "rows": [
            ["Határozói igenév", "-va / -ve", "harcolva, áttörve"],
            ["Folyamatos melléknévi", "-ó / -ő", "pusztító tűz, menekülő király"],
            ["Befejezett melléknévi", "-t / -ott / -ett", "felszerelt sereg, megáradt patak"]
        ]}
    ],
    "examples": [
        {"spanish": "A nehézlovasság áttörve az első vonalat a tüzérség elé jutott.", "english": "The heavy cavalry, breaking through the first line, reached the artillery."},
        {"spanish": "A pusztító ágyútűz megállította a támadást.", "english": "The devastating cannon fire halted the attack."},
        {"spanish": "A megáradt patakba fulladt a menekülő uralkodó.", "english": "The fleeing monarch drowned in the flooded stream."}
    ]
}
write_json(GRAMMAR_DIR / "gr.b1.mohacs.03.json", gr_3)

exs_3 = [
    {"id": "ex.b1.mohacs.03.01", "type": "multiple-choice", "lesson": "lesson.b1.mohacs.03", "teaches": ["tulero"], "prompt": "Milyen arányú erők álltak szemben a mohácsi csatában?", "options": ["Körülbelül 25 ezer magyar állt szemben több mint 60 ezer oszmán katonával", "Egyenlő létszámú seregek harcoltak", "A magyar sereg volt kétszeres túlerőben", "Csak néhány száz lovas csapott össze"], "correctIndex": 0, "explanation": "A török sereg jelentős túlerőben volt (több mint kétszeres létszám és sok ágyú)."},
    {"id": "ex.b1.mohacs.03.02", "type": "fill-blank", "lesson": "lesson.b1.mohacs.03", "teaches": ["megsemmisito"], "prompt": "Egészítsd ki a mondatot a megfelelő melléknévvel!", "sentence": "A mohácsi csata *megsemmisítő* vereséggel zárult 1526-ban.", "target": "megsemmisítő"},
    {"id": "ex.b1.mohacs.03.03", "type": "sentence-builder", "lesson": "lesson.b1.mohacs.03", "teaches": ["tulero", "osszecsapas"], "prompt": "Rakd össze a mondatot helyesen!", "chips": ["A", "magyar", "sereg", "nem", "bírt", "a", "túlerővel."], "target": "A magyar sereg nem bírt a túlerővel.", "english": "The Hungarian army could not cope with the superior force."},
    {"id": "ex.b1.mohacs.03.04", "type": "multiple-choice", "lesson": "lesson.b1.mohacs.03", "teaches": ["fovezer", "Tomori Pál"], "prompt": "Ki volt a magyar sereg egyik fővezére Mohácsnál?", "options": ["Tomori Pál kalocsai érsek", "Hunyadi János", "Kinizsi Pál", "Zrínyi Miklós"], "correctIndex": 0, "explanation": "Tomori Pál kalocsai érsek vezette a sereget a csatamezőn, ahol maga is életét vesztette."},
    {"id": "ex.b1.mohacs.03.05", "type": "fill-blank", "lesson": "lesson.b1.mohacs.03", "teaches": ["tuzerseg"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A török *tüzérség* pusztító ágyútüze megtörte a magyar rohamot.", "target": "tüzérség"},
    {"id": "ex.b1.mohacs.03.06", "type": "sentence-builder", "lesson": "lesson.b1.mohacs.03", "teaches": ["felmorzsolodik"], "prompt": "Alkoss helyes mondatot a megadott szavakból!", "chips": ["A", "magyar", "hadsereg", "két", "óra", "alatt", "felmorzsolódott."], "target": "A magyar hadsereg két óra alatt felmorzsolódott.", "english": "The Hungarian army was decimated within two hours."},
    {"id": "ex.b1.mohacs.03.07", "type": "multiple-choice", "lesson": "lesson.b1.mohacs.03", "teaches": ["Csele-patak"], "prompt": "Hol vesztette életét II. Lajos király a menekülés közben?", "options": ["A megáradt Csele-patakban", "A budai várban", "A Duna túlpartján", "Egy templomban"], "correctIndex": 0, "explanation": "II. Lajos páncélos lova belecsúszott a Csele-patak mocsarába."},
    {"id": "ex.b1.mohacs.03.08", "type": "fill-blank", "lesson": "lesson.b1.mohacs.03", "teaches": ["osszecsapas"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A sorsdöntő *összecsapás* 1526. augusztus 29-én zajlott le.", "target": "összecsapás"}
]
write_json(EXERCISES_DIR / "ex.b1.mohacs.03.json", make_exercise_group("ex.b1.mohacs.03", "A mohácsi csata gyakorlatai", "Gyakorlatok a mohácsi csata történetéről és igeneveiről.", exs_3))

lesson_3 = make_lesson(
    "lesson.b1.mohacs.03",
    "A mohácsi csata: 1526. augusztus 29.",
    "Igenevek a történeti elbeszélésben (-va/-ve, -ó/-ő, -ott/-ett)",
    "Részletesen elemezzük a mohácsi csata lefolyását, okait és a katasztrófa közvetlen eseményeit.",
    ["Megérteni a mohácsi csata dátumát és lefolyását", "Használni a határozói és melléknévi igeneveket leírásokban", "Ismerni a korszak kulcsfiguráit (II. Lajos, Tomori Pál, Szulejmán)"],
    "story.b1.mohacs.03",
    "voc.b1.mohacs.03",
    "gr.b1.mohacs.03",
    "ex.b1.mohacs.03",
    [e["id"] for e in exs_3]
)
write_json(LESSONS_DIR / "lesson.b1.mohacs.03.json", lesson_3)


# ==========================================
# LESSON 4: b1-mohacs-04 (Kettős királyválasztás és váradi béke)
# ==========================================
story_4 = make_story(
    "story.b1.mohacs.04",
    "Kettős királyválasztás és a váradi béke (1526–1538)",
    "II. Lajos halála után a magyar nemesség megosztottá vált, és két királyt választott egyszerre: Szapolyai Jánost és Habsburg Ferdinándot.",
    "Székesfehérvár és Pozsony",
    ["Expressing condition and consequence (ha... akkor, amennyiben, feltéve, hogy)", "Diplomatic agreements in Hungarian"],
    ["kettős királyválasztás", "Szapolyai János", "Habsburg Ferdinánd", "váradi béke"],
    [
        "A mohácsi tragédiát követően a királyi trón üresen maradt. A magyar nemesség egyik része Székesfehérváron a leggazdagabb magyar főurat, Szapolyai János erdélyi vajdát választotta királlyá. Néhány héttel később a főurak másik csoportja Pozsonyban a Habsburg-házi I. Ferdinánd osztrák főherceget koronázta meg.",
        "A két király közötti polgárháború tovább gyengítette az országot. Ha Szapolyai nem kért volna segítséget a szultántól a Habsburgok ellen, a törökök talán nem avatkozhattak volna be ilyen mértékben a magyar belpolitikába.",
        "1538-ban a felek titkos megállapodást kötöttek Váradon. A váradi béke értelmében mindketten megtarthatták az általuk uralt országrészeket azzal a feltétellel, hogy Szapolyai halála után az egész ország Ferdinándra száll, még abban az esetben is, ha Szapolya выс szül fiúörököse születne."
    ],
    [
        {"lemma": "kettős királyválasztás", "pos": "noun", "cefr": "B1", "gloss": "dual royal election"},
        {"lemma": "megállapodás", "pos": "noun", "cefr": "B1", "gloss": "agreement, pact"},
        {"lemma": "polgárháború", "pos": "noun", "cefr": "B1", "gloss": "civil war"},
        {"lemma": "örökös", "pos": "noun", "cefr": "B1", "gloss": "heir, successor"},
        {"lemma": "beavatkozik", "pos": "verb", "cefr": "B1", "gloss": "to intervene, interfere"}
    ],
    [
        {
            "question": "Kiket választottak királlyá a magyar rendek 1526 végén?",
            "options": ["Szapolyai Jánost és Habsburg I. Ferdinándot", "Mátyás királyt és Ulászlót", "Károly Róbertet és Nagy Lajost", "Tomori Pált és II. Lajost"],
            "correctIndex": 0,
            "explanation": "A rendek megosztottsága miatt Szapolyai Jánost és Habsburg Ferdinándot is királlyá koronázták."
        }
    ]
)
write_json(STORIES_DIR / "story.b1.mohacs.04.json", story_4)

voc_4 = {
    "id": "voc.b1.mohacs.04",
    "title": "A kettős királyválasztás szókincse",
    "description": "Polgárháború, trónutódlás, örökösödési szerződések és diplomáciai feltételek.",
    "entries": [
        {"lemma": "polgárháború", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "civil war", "examples": [{"hu": "A polgárháború megosztotta a magyar nemességet.", "en": "The civil war divided the Hungarian nobility."}]}]},
        {"lemma": "megállapodás", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "agreement, accord", "examples": [{"hu": "A két király titkos megállapodást kötött Váradon.", "en": "The two kings concluded a secret agreement in Várad."}]}]},
        {"lemma": "örökös", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "heir, successor", "examples": [{"hu": "Szapolyai haláláig nem volt törvényes örököse.", "en": "Until his death, Szapolyai had no legitimate heir."}]}]},
        {"lemma": "beavatkozik", "pos": "verb", "cefr": "B1", "definitions": [{"meaning": "to intervene", "examples": [{"hu": "A szultán beavatkozott a két király harcába.", "en": "The Sultan intervened in the two kings' struggle."}]}]},
        {"lemma": "trónkövetelő", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "claimant to the throne, pretender", "examples": [{"hu": "Mindkét trónkövetelő jogot formált a koronára.", "en": "Both claimants laid claim to the crown."}]}]}
    ]
}
write_json(VOCAB_DIR / "voc.b1.mohacs.04.json", voc_4)

gr_4 = {
    "id": "gr.b1.mohacs.04",
    "title": "Feltételes összetett mondatok: ha... akkor, amennyiben, feltéve, hogy",
    "description": "Constructing conditional sentences and diplomatic stipulations.",
    "rules": [
        "A 'ha... akkor' alapvető feltételes viszonyt fejez ki a valós és nem valós feltételeknél.",
        "Az 'amennyiben' formálisabb és jogi kontextusban használatos ('insofar as / in case that').",
        "A 'feltéve, hogy' kikötést vagy különleges feltételt fogalmaz meg ('provided that')."
    ],
    "tables": [
        {"headers": ["Kifejezés", "Funkció", "Példa"], "rows": [
            ["ha... (akkor)", "alapvető feltétel", "Ha megegyeznek, béke lesz."],
            ["amennyiben", "hivatalos/jogi feltétel", "Amennyiben nem születik örökös, Ferdinánd örököl."],
            ["feltéve, hogy", "kikötés, megkötés", "Békét kötnek, feltéve, hogy megtarthatják birtokaikat."]
        ]}
    ],
    "examples": [
        {"spanish": "Amennyiben Szapolyai fiúörökös nélkül hal meg, a korona Ferdinándra száll.", "english": "In the event that Szapolyai dies without a male heir, the crown passes to Ferdinand."},
        {"spanish": "Feltéve, hogy betartják a váradi békét, elkerülhető lett volna a háború.", "english": "Provided that they kept the Peace of Várad, the war could have been avoided."},
        {"spanish": "Ha a magyar urak összefogtak volna, ellenállhattak volna a töröknek.", "english": "If the Hungarian lords had united, they could have resisted the Turks."}
    ]
}
write_json(GRAMMAR_DIR / "gr.b1.mohacs.04.json", gr_4)

exs_4 = [
    {"id": "ex.b1.mohacs.04.01", "type": "multiple-choice", "lesson": "lesson.b1.mohacs.04", "teaches": ["polgarhaboru"], "prompt": "Mit eredményezett a kettős királyválasztás 1526 után?", "options": ["Polgárháborút és az ország megosztottságát", "A törökök azonnali kiűzését", "A gazdaság gyors növekedését", "Új aranypénz bevezetését"], "correctIndex": 0, "explanation": "A két király párthívei polgárháborút vívtak egymással."},
    {"id": "ex.b1.mohacs.04.02", "type": "fill-blank", "lesson": "lesson.b1.mohacs.04", "teaches": ["megallapodas"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A felek 1538-ban titkos *megállapodást* kötöttek Váradon.", "target": "megállapodást"},
    {"id": "ex.b1.mohacs.04.03", "type": "sentence-builder", "lesson": "lesson.b1.mohacs.04", "teaches": ["amennyiben", "orokos"], "prompt": "Alkoss szabályos feltételes mondatot!", "chips": ["Amennyiben", "nincs", "örökös,", "a", "korona", "Ferdinándé."], "target": "Amennyiben nincs örökös, a korona Ferdinándé.", "english": "In case there is no heir, the crown belongs to Ferdinand."},
    {"id": "ex.b1.mohacs.04.04", "type": "multiple-choice", "lesson": "lesson.b1.mohacs.04", "teaches": ["varadi béke"], "prompt": "Miről rendelkezett az 1538-as váradi béke?", "options": ["Szapolyai halála után az egész ország Ferdinándra száll", "A szultán kapja meg Budát", "Szapolyai örökre elűzi a Habsburgokat", "Magyarország felveszi a reformációt"], "correctIndex": 0, "explanation": "A váradi béke kimondta a Habsburg öröklést Szapolyai halála esetére."},
    {"id": "ex.b1.mohacs.04.05", "type": "fill-blank", "lesson": "lesson.b1.mohacs.04", "teaches": ["beavatkozik"], "prompt": "Egészítsd ki a mondatot a megfelelő igealakkal!", "sentence": "A szultán serege azonnal *beavatkozott* a magyar trónviszályba.", "target": "beavatkozott"},
    {"id": "ex.b1.mohacs.04.06", "type": "sentence-builder", "lesson": "lesson.b1.mohacs.04", "teaches": ["feltéve", "megallapodas"], "prompt": "Rakd össze a mondatot helyesen!", "chips": ["Békét", "kötöttek,", "feltéve,", "hogy", "megosztják", "a", "hatalmat."], "target": "Békét kötöttek, feltéve, hogy megosztják a hatalmat.", "english": "They made peace, provided that they shared power."},
    {"id": "ex.b1.mohacs.04.07", "type": "multiple-choice", "lesson": "lesson.b1.mohacs.04", "teaches": ["tronkovetelo"], "prompt": "Ki volt Szapolyai János ellenfele a trónért?", "options": ["Habsburg I. Ferdinánd", "Habsburg I. Rudolf", "Hunyadi Mátyás", "IV. Béla"], "correctIndex": 0, "explanation": "Habsburg I. Ferdinánd osztrák főherceg lépett fel törvényes trónkövetelőként."},
    {"id": "ex.b1.mohacs.04.08", "type": "fill-blank", "lesson": "lesson.b1.mohacs.04", "teaches": ["polgarhaboru"], "prompt": "Egészítsd ki a mondatot a megfelelő kifejezéssel!", "sentence": "A két király hívei közötti *polgárháború* tönkretette a vármegyéket.", "target": "polgárháború"}
]
write_json(EXERCISES_DIR / "ex.b1.mohacs.04.json", make_exercise_group("ex.b1.mohacs.04", "Kettős királyválasztás gyakorlatok", "Gyakorlatok a trónviszályról és a feltételes mondatszerkezetekről.", exs_4))

lesson_4 = make_lesson(
    "lesson.b1.mohacs.04",
    "Kettős királyválasztás és a váradi béke (1526–1538)",
    "Feltételes összetett mondatok (amennyiben, feltéve, hogy)",
    "Megtanuljuk, hogyan vezetett a trónviszály és a kettős királyválasztás polgárháborúhoz és a váradi titkos egyezményhez.",
    ["Megérteni a kettős királyválasztás politikai okait", "Használni a formális feltételes kötőszavakat", "Ismerni a váradi béke feltételeit"],
    "story.b1.mohacs.04",
    "voc.b1.mohacs.04",
    "gr.b1.mohacs.04",
    "ex.b1.mohacs.04",
    [e["id"] for e in exs_4]
)
write_json(LESSONS_DIR / "lesson.b1.mohacs.04.json", lesson_4)


# ==========================================
# LESSON 5: b1-mohacs-05 (A középkori állam bukása és emlékezete)
# ==========================================
story_5 = make_story(
    "story.b1.mohacs.05",
    "A középkori állam bukása és a mohácsi trauma emlékezete",
    "A mohácsi vész a magyar történelem legnagyobb sorsfordító traumájává vált, amely a középkori független állam bukását és a másfél évszázados török uralmat hozta el.",
    "Mohács és a Nemzeti Emlékhely",
    ["Discourse markers and summary expressions (következésképpen, mindent egybevetve, ebből kifolyólag)", "Historical cultural reflection"],
    ["mohácsi vész", "sorsforduló", "történelmi trauma", "nemzeti emlékezet"],
    [
        "A mohácsi csatavesztés nem csupán egy elveszített katonai ütközet volt, hanem a virágzó középkori Magyar Királyság integritásának végső összeomlását jelentette. Következésképpen az ország elveszítette nagyhatalmi státuszát Közép-Európában, és a keresztény és oszmán világ ütközőzónájává vált.",
        "A magyar nyelvben és kultúrában a 'mohácsi vész' kifejezés mélyen gyökeret vert. A közismert szólásmondás, a 'Több is veszett Mohácsnál' arra utal, hogy a legnagyobb baj közepette is van még remény, hiszen a nemzet Mohács után is képes volt fennmaradni és újjászületni.",
        "Mindent egybevetve, Mohács a magyar történeti tudat kulcsfontosságú szimbóluma lett. Ebből kifolyólag a Mohácsi Nemzeti Emlékhely a mai napig tiszteleg az ott elesett hősök emléke előtt, figyelmeztetve az összefogás és a nemzeti felelősség fontosságára."
    ],
    [
        {"lemma": "sorsforduló", "pos": "noun", "cefr": "B1", "gloss": "turning point of destiny"},
        {"lemma": "integritás", "pos": "noun", "cefr": "B1", "gloss": "integrity, wholeness"},
        {"lemma": "ütközőzóna", "pos": "noun", "cefr": "B1", "gloss": "buffer zone"},
        {"lemma": "szólásmondás", "pos": "noun", "cefr": "B1", "gloss": "proverb, saying"},
        {"lemma": "emlékhely", "pos": "noun", "cefr": "B1", "gloss": "memorial site"}
    ],
    [
        {
            "question": "Mit jelent a magyar kultúrában a 'Több is veszett Mohácsnál' szólás?",
            "options": ["A legnagyobb bajban sem szabad kétségbeesni, mert volt már nagyobb veszteség is", "Minden pénzünket elveszítettük", "A törökök újra támadnak", "El kell felejteni a múltat"],
            "correctIndex": 0,
            "explanation": "A mondás arra emlékeztet, hogy bármilyen nagy a baj, Magyarország a mohácsi katasztrófát is túlélte."
        }
    ]
)
write_json(STORIES_DIR / "story.b1.mohacs.05.json", story_5)

voc_5 = {
    "id": "voc.b1.mohacs.05",
    "title": "A nemzeti emlékezet és történelmi szintézis szókincse",
    "description": "Sorsforduló, integritás, szólásmondások és a nemzeti emlékhelyek fogalmai.",
    "entries": [
        {"lemma": "sorsforduló", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "historical turning point", "examples": [{"hu": "1526 a magyar történelem legnagyobb sorsfordulója volt.", "en": "1526 was the greatest turning point of Hungarian history."}]}]},
        {"lemma": "ütközőzóna", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "buffer zone, battleground region", "examples": [{"hu": "Az ország két nagyhatalom közötti ütközőzónává vált.", "en": "The country became a buffer zone between two great powers."}]}]},
        {"lemma": "szólásmondás", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "proverb, folk saying", "examples": [{"hu": "A 'Több is veszett Mohácsnál' egy híres magyar szólásmondás.", "en": "'More was lost at Mohács' is a famous Hungarian saying."}]}]},
        {"lemma": "emlékhely", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "memorial site, national monument", "examples": [{"hu": "A Mohácsi Nemzeti Emlékhely a hősök előtt tiszteleg.", "en": "The Mohács National Memorial pays tribute to the heroes."}]}]},
        {"lemma": "összeomlás", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "collapse, complete downfall", "examples": [{"hu": "A középkori állam összeomlása évszázadokra meghatározta a nemzet sorsát.", "en": "The collapse of the medieval state determined the nation's fate for centuries."}]}]}
    ]
}
write_json(VOCAB_DIR / "voc.b1.mohacs.05.json", voc_5)

gr_5 = {
    "id": "gr.b1.mohacs.05",
    "title": "Következtető és összefoglaló szövegkapcsoló elemek",
    "description": "Discourse markers for summarizing arguments and drawing conclusions: következésképpen, mindent egybevetve, ebből kifolyólag.",
    "rules": [
        "A 'következésképpen' (consequently) közvetlen ok-okozati következtetést von le.",
        "A 'mindent egybevetve' (all in all / taking everything into account) átfogó összegzésre szolgál.",
        "Az 'ebből kifolyólag' (as a result of this) szoros összefüggést mutat be két történelmi jelenség között."
    ],
    "tables": [
        {"headers": ["Kifejezés", "Funkció", "Példa"], "rows": [
            ["következésképpen", "következtetés levonása", "Következésképpen az állam elvesztette függetlenségét."],
            ["mindent egybevetve", "összegzés", "Mindent egybevetve, a nemzet talpra állt."],
            ["ebből kifolyólag", "eredmény megjelölése", "Ebből kifolyólag megépült az emlékhely."]
        ]}
    ],
    "examples": [
        {"spanish": "A hadsereg elpusztult, következésképpen nem maradt erő a határok védelmére.", "english": "The army perished, consequently no force remained to defend the borders."},
        {"spanish": "Mindent egybevetve Mohács a magyar történelem legnagyobb figyelmeztető szimbóluma.", "english": "All in all, Mohács is the greatest cautionary symbol of Hungarian history."},
        {"spanish": "A király meghalt, ebből kifolyólag megindult a harc a trónért.", "english": "The king died, as a result of this the fight for the throne began."}
    ]
}
write_json(GRAMMAR_DIR / "gr.b1.mohacs.05.json", gr_5)

exs_5 = [
    {"id": "ex.b1.mohacs.05.01", "type": "multiple-choice", "lesson": "lesson.b1.mohacs.05", "teaches": ["sorsfordulo"], "prompt": "Miért tartják Mohácsot korszakhatárnak a magyar történelemben?", "options": ["Mert véget ért a független középkori Magyar Királyság korszaka", "Mert új várost alapítottak a Duna mellett", "Mert befejeződött a honfoglalás", "Mert megkoronázták Mátyás királyt"], "correctIndex": 0, "explanation": "Mohács a középkori magyar állam bukását és a három részre szakadás kezdetét jelöli."},
    {"id": "ex.b1.mohacs.05.02", "type": "fill-blank", "lesson": "lesson.b1.mohacs.05", "teaches": ["szolasmondas"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A 'Több is veszett Mohácsnál' egy közismert magyar *szólásmondás*.", "target": "szólásmondás"},
    {"id": "ex.b1.mohacs.05.03", "type": "sentence-builder", "lesson": "lesson.b1.mohacs.05", "teaches": ["kovetkezeskeppen", "osszeomlas"], "prompt": "Rakd össze a következtető mondatot!", "chips": ["Következésképpen", "a", "középkori", "magyar", "állam", "összeomlott."], "target": "Következésképpen a középkori magyar állam összeomlott.", "english": "Consequently, the medieval Hungarian state collapsed."},
    {"id": "ex.b1.mohacs.05.04", "type": "multiple-choice", "lesson": "lesson.b1.mohacs.05", "teaches": ["emlekhely"], "prompt": "Hol áll ma a mohácsi csata hőseinek szentelt emlékhely?", "options": ["Sátorhely közelében a Mohácsi Nemzeti Emlékhelyen", "A budai várban", "Visegrád fellegvárában", "A Hősök terén"], "correctIndex": 0, "explanation": "A Mohácsi Nemzeti Emlékhely a csata eredeti helyszínén található."},
    {"id": "ex.b1.mohacs.05.05", "type": "fill-blank", "lesson": "lesson.b1.mohacs.05", "teaches": ["utkozozona"], "prompt": "Egészítsd ki a mondatot a megfelelő kifejezéssel!", "sentence": "Magyarország a Nyugat és a Kelet közötti *ütközőzónává* vált.", "target": "ütközőzónává"},
    {"id": "ex.b1.mohacs.05.06", "type": "sentence-builder", "lesson": "lesson.b1.mohacs.05", "teaches": ["mindent", "sorsfordulo"], "prompt": "Alkoss összegző mondatot!", "chips": ["Mindent", "egybevetve,", "1526", "sorsfordító", "év", "volt."], "target": "Mindent egybevetve, 1526 sorsfordító év volt.", "english": "All in all, 1526 was a fate-turning year."},
    {"id": "ex.b1.mohacs.05.07", "type": "multiple-choice", "lesson": "lesson.b1.mohacs.05", "teaches": ["kovetkezeskeppen"], "prompt": "Melyik kötőszó fejez ki következtetést?", "options": ["Következésképpen", "Noha", "Bár", "Mintha"], "correctIndex": 0, "explanation": "A 'következésképpen' logikai következtetést vezet be."},
    {"id": "ex.b1.mohacs.05.08", "type": "fill-blank", "lesson": "lesson.b1.mohacs.05", "teaches": ["emlekhely"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A nemzet ma is méltósággal emlékezik a mohácsi *emlékhelyen*.", "target": "emlékhelyen"}
]
write_json(EXERCISES_DIR / "ex.b1.mohacs.05.json", make_exercise_group("ex.b1.mohacs.05", "A mohácsi emlékezet gyakorlatai", "Gyakorlatok a történelmi szintézisről és a következtető szerkezetekről.", exs_5))

lesson_5 = make_lesson(
    "lesson.b1.mohacs.05",
    "A középkori állam bukása és a mohácsi trauma emlékezete",
    "Következtető és összefoglaló kifejezések (következésképpen, mindent egybevetve)",
    "Összegezzük a mohácsi csata mély hatását a magyar kultúrára, nyelvre és a nemzeti emlékezetre.",
    ["Megérteni Mohács kulturális és szimbolikus jelentőségét", "Használni az összefoglaló és következtető kötőszavakat", "Ismerni a 'Több is veszett Mohácsnál' szólásmondás hátterét"],
    "story.b1.mohacs.05",
    "voc.b1.mohacs.05",
    "gr.b1.mohacs.05",
    "ex.b1.mohacs.05",
    [e["id"] for e in exs_5]
)
write_json(LESSONS_DIR / "lesson.b1.mohacs.05.json", lesson_5)


# ==========================================
# CONSOLIDATION LESSON: b1-mohacs-consolidation
# ==========================================
cons_exs = [
    {"id": "ex.b1.mohacs.cons.01", "type": "multiple-choice", "lesson": "lesson.b1.mohacs.consolidation", "teaches": ["mohacsi-csata"], "prompt": "Melyik évben zajlott le a mohácsi csata?", "options": ["1526-ban", "1514-ben", "1541-ben", "1490-ben"], "correctIndex": 0, "explanation": "A mohácsi csata 1526. augusztus 29-én volt."},
    {"id": "ex.b1.mohacs.cons.02", "type": "fill-blank", "lesson": "lesson.b1.mohacs.consolidation", "teaches": ["kincstar"], "prompt": "Mátyás halála után a királyi *kincstár* kiürült, ezért feloszlatták a fekete sereget.", "sentence": "Mátyás halála után a királyi *kincstár* kiürült, ezért feloszlatták a fekete sereget.", "target": "kincstár"},
    {"id": "ex.b1.mohacs.cons.03", "type": "multiple-choice", "lesson": "lesson.b1.mohacs.consolidation", "teaches": ["Nandorfehervar"], "prompt": "Melyik fontos déli végvár esett el 1521-ben?", "options": ["Nándorfehérvár", "Eger", "Szigetvár", "Kőszeg"], "correctIndex": 0, "explanation": "Nándorfehérvár 1521-es eleste nyitotta meg a kaput az ország belseje felé."},
    {"id": "ex.b1.mohacs.cons.04", "type": "fill-blank", "lesson": "lesson.b1.mohacs.consolidation", "teaches": ["ostrom"], "prompt": "1521-ben a szultán hosszas *ostrom* után foglalta el Nándorfehérvárt.", "sentence": "1521-ben a szultán hosszas *ostrom* után foglalta el Nándorfehérvárt.", "target": "ostrom"},
    {"id": "ex.b1.mohacs.cons.05", "type": "sentence-builder", "lesson": "lesson.b1.mohacs.consolidation", "teaches": ["mivel", "kincstar"], "prompt": "Rakd össze a mondatot!", "chips": ["Mivel", "a", "kincstár", "kiürült,", "nem", "volt", "sereg."], "target": "Mivel a kincstár kiürült, nem volt sereg.", "english": "Since the treasury was empty, there was no army."},
    {"id": "ex.b1.mohacs.cons.06", "type": "multiple-choice", "lesson": "lesson.b1.mohacs.consolidation", "teaches": ["II. Lajos"], "prompt": "Ki volt a magyar király a mohácsi csata idején?", "options": ["II. Lajos", "II. Ulászló", "Hunyadi Mátyás", "Szapolyai János"], "correctIndex": 0, "explanation": "A fiatal II. Lajos király vezette az országot 1526-ban."},
    {"id": "ex.b1.mohacs.cons.07", "type": "fill-blank", "lesson": "lesson.b1.mohacs.consolidation", "teaches": ["Csele-patak"], "prompt": "II. Lajos király menekülés közben a megáradt *Csele-patakba* fulladt.", "sentence": "II. Lajos király menekülés közben a megáradt *Csele-patakba* fulladt.", "target": "Csele-patakba"},
    {"id": "ex.b1.mohacs.cons.08", "type": "sentence-builder", "lesson": "lesson.b1.mohacs.consolidation", "teaches": ["miutan", "Nandorfehervar"], "prompt": "Alkoss összetett mondatot!", "chips": ["Miután", "Nándorfehérvár", "elesett,", "megnyílt", "az", "út", "Buda", "felé."], "target": "Miután Nándorfehérvár elesett, megnyílt az út Buda felé.", "english": "After Nándorfehérvár fell, the road opened towards Buda."},
    {"id": "ex.b1.mohacs.cons.09", "type": "multiple-choice", "lesson": "lesson.b1.mohacs.consolidation", "teaches": ["kettos-kiralyvalasztas"], "prompt": "Kiket választottak királlyá 1526 végén?", "options": ["Szapolyai Jánost és Habsburg Ferdinándot", "Tomori Pált és II. Lajost", "Károly Róbertet és Nagy Lajost", "Szulejmánt és Ferdinándot"], "correctIndex": 0, "explanation": "1526-ban Szapolyai János és I. Ferdinánd egyaránt király lett."},
    {"id": "ex.b1.mohacs.cons.10", "type": "fill-blank", "lesson": "lesson.b1.mohacs.consolidation", "teaches": ["polgarhaboru"], "prompt": "A két megkoronázott király hívei között pusztító *polgárháború* tört ki.", "sentence": "A két megkoronázott király hívei között pusztító *polgárháború* tört ki.", "target": "polgárháború"},
    {"id": "ex.b1.mohacs.cons.11", "type": "sentence-builder", "lesson": "lesson.b1.mohacs.consolidation", "teaches": ["amennyiben", "orokos"], "prompt": "Rakd össze a jogi feltételt!", "chips": ["Amennyiben", "nincs", "örökös,", "a", "trón", "Ferdinándé."], "target": "Amennyiben nincs örökös, a trón Ferdinándé.", "english": "If there is no heir, the throne belongs to Ferdinand."},
    {"id": "ex.b1.mohacs.cons.12", "type": "multiple-choice", "lesson": "lesson.b1.mohacs.consolidation", "teaches": ["varadi-beke"], "prompt": "Melyik évben született a váradi titkos béke?", "options": ["1538-ban", "1526-ban", "1541-ben", "1568-ban"], "correctIndex": 0, "explanation": "A váradi békeszerződést 1538-ban kötötték."},
    {"id": "ex.b1.mohacs.cons.13", "type": "fill-blank", "lesson": "lesson.b1.mohacs.consolidation", "teaches": ["szolasmondas"], "prompt": "A 'Több is veszett Mohácsnál' híres magyar *szólásmondás* a nehéz pillanatokra.", "sentence": "A 'Több is veszett Mohácsnál' híres magyar *szólásmondás* a nehéz pillanatokra.", "target": "szólásmondás"},
    {"id": "ex.b1.mohacs.cons.14", "type": "multiple-choice", "lesson": "lesson.b1.mohacs.consolidation", "teaches": ["kovetkezeskeppen"], "prompt": "Melyik szó jelenti azt, hogy 'ennek következtében / tehát'?", "options": ["Következésképpen", "Jóllehet", "Mindazonáltal", "Minthogyha"], "correctIndex": 0, "explanation": "A 'következésképpen' következtető határozószó."},
    {"id": "ex.b1.mohacs.cons.15", "type": "fill-blank", "lesson": "lesson.b1.mohacs.consolidation", "teaches": ["emlekhely"], "prompt": "A sátorhelyi *emlékhely* méltó emléket állít a csata áldozatainak.", "sentence": "A sátorhelyi *emlékhely* méltó emléket állít a csata áldozatainak.", "target": "emlékhely"},
    {"id": "ex.b1.mohacs.cons.16", "type": "sentence-builder", "lesson": "lesson.b1.mohacs.consolidation", "teaches": ["kovetkezeskeppen", "veszely"], "prompt": "Alkoss összefüggő mondatot!", "chips": ["Következésképpen", "az", "ország", "halálos", "veszélybe", "került."], "target": "Következésképpen az ország halálos veszélybe került.", "english": "Consequently, the country fell into mortal danger."},
    {"id": "ex.b1.mohacs.cons.17", "type": "multiple-choice", "lesson": "lesson.b1.mohacs.consolidation", "teaches": ["Tomori-Pal"], "prompt": "Milyen tisztséget viselt Tomori Pál a sereg élén?", "options": ["Kalocsai érsek és fővezér", "Nádor és királyi kancellár", "Egri várkapitány", "Erdélyi fejedelem"], "correctIndex": 0, "explanation": "Tomori Pál kalocsai érsek volt a csata főparancsnoka."},
    {"id": "ex.b1.mohacs.cons.18", "type": "fill-blank", "lesson": "lesson.b1.mohacs.consolidation", "teaches": ["tuzerseg"], "prompt": "A török *tüzérség* és a janicsárok sortüze döntötte el a csatát.", "sentence": "A török *tüzérség* és a janicsárok sortüze döntötte el a csatát.", "target": "tüzérség"},
    {"id": "ex.b1.mohacs.cons.19", "type": "sentence-builder", "lesson": "lesson.b1.mohacs.consolidation", "teaches": ["mindent", "sorsfordulo"], "prompt": "Rakd össze a záró mondatot!", "chips": ["Mindent", "egybevetve,", "Mohács", "a", "nemzet", "sorsfordulója", "volt."], "target": "Mindent egybevetve, Mohács a nemzet sorsfordulója volt.", "english": "All in all, Mohács was the nation's turning point."},
    {"id": "ex.b1.mohacs.cons.20", "type": "multiple-choice", "lesson": "lesson.b1.mohacs.consolidation", "teaches": ["mohacsi-vesz"], "prompt": "Hány évszázados török jelenlét kezdődött el Mohács után?", "options": ["Mintegy másfél évszázados (150 év)", "Ötven év", "Háromszáz év", "Mindössze tíz év"], "correctIndex": 0, "explanation": "A török hódoltság mintegy másfél évszázadon (150 éven) át tartott."}
]
write_json(EXERCISES_DIR / "ex.b1.mohacs.consolidation.json", make_exercise_group("ex.b1.mohacs.consolidation", "Mohács összefoglaló gyakorlatok", "Átfogó teszt a mohácsi korszak történelméről és nyelvtani szerkezeteiről.", cons_exs))

cons_lesson = {
    "id": "lesson.b1.mohacs.consolidation",
    "title": "The Battle of Mohács: Unit 9 Consolidation",
    "level": "B1",
    "track": "citizenship",
    "estimatedMinutes": 25,
    "prerequisites": [
        "lesson.b1.mohacs.01",
        "lesson.b1.mohacs.02",
        "lesson.b1.mohacs.03",
        "lesson.b1.mohacs.04",
        "lesson.b1.mohacs.05"
    ],
    "grammar": ["Unit review"],
    "vocabulary": ["Unit review"],
    "culturalContext": "Magyar történelem összefoglalás (Honosítási vizsgafelkészítő)",
    "sections": [
        {
            "type": "intro",
            "title": "Unit 9 Consolidation: The Battle of Mohács (1526)",
            "body": "Ebben az összefoglaló leckében átismételjük a Jagelló-kor válságát, Nándorfehérvár 1521-es elestét, a mohácsi csata lefolyását, a kettős királyválasztást és a mohácsi nemzeti emlékezetet."
        },
        {
            "type": "goal",
            "title": "Consolidation Goals",
            "items": [
                "A mohácsi csata okainak és következményeinek biztos ismerete",
                "Összetett okhatározói, időhatározói és feltételes mondatok magabiztos alkalmazása",
                "A honosítási vizsgán elvárt történelmi fogalmak használata"
            ]
        },
        {
            "type": "exercise-group",
            "title": "Comprehensive Unit 9 Practice",
            "ref": "ex.b1.mohacs.consolidation",
            "exerciseRefs": [e["id"] for e in cons_exs]
        },
        {
            "type": "checklist",
            "items": [
                "Tudom, mikor volt a mohácsi csata (1526. augusztus 29.)",
                "Ismerem II. Lajos és Tomori Pál nevét és szerepét",
                "Megértem a kettős királyválasztás és a váradi béke jelentőségét",
                "Ismerem a 'Több is veszett Mohácsnál' mondás értelmét"
            ]
        }
    ]
}
write_json(LESSONS_DIR / "lesson.b1.mohacs.consolidation.json", cons_lesson)

print("Unit 9 (b1-mohacs) complete!")
