# -*- coding: utf-8 -*-
"""
Full Unit 16 Overhaul: The 1848–49 Revolution and War of Independence (b1-forradalom)
Lessons:
1. 1848. március 15.: A pesti forradalom és a márciusi ifjak
2. Az áprilisi törvények (1848. április 11.) és az első felelős kormány
3. Az önvédelmi harc és a pákozdi győzelem (1848 ősze)
4. A dicsőséges tavaszi hadjárat és Buda bevétele (1849)
5. A Függetlenségi Nyilatkozat és a világosi fegyverletétel (1849)
Consolidation: Unit 16 Capstone (20 exercises)
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
# LESSON 1: b1-forradalom-01 (1848. március 15.)
# ==========================================
story_1 = make_story(
    "story.b1.forradalom.01",
    "1848. március 15.: A pesti forradalom és a márciusi ifjak",
    "1848. március 15-én a pesti márciusi ifjak vérontás nélkül kivívták a sajtószabadságot, kinyomtatták a Nemzeti dalt és a 12 pontot, megnyitva a polgári szabadság korszakát.",
    "Pilvax kávéház, Nemzeti Múzeum és Buda",
    ["Revolutionary sequential narrative (elszaval, követel, kivív, kiszabadít)", "March 15 national holiday roots"],
    ["1848. március 15.", "Petőfi Sándor", "Nemzeti dal", "12 pont", "márciusi ifjak", "Táncsics Mihály"],
    [
        "1848 tavaszán forradalmi hullám söpört végig Európán. Amikor a bécsi forradalom híre eljutott Pestre, 1848. március 15-én reggel a Pilvax kávéházban gyülekező fiatal radikális értelmiségiek – Petőfi Sándor, Jókai Mór, Vasvári Pál és társaik, a 'márciusi ifjak' – úgy döntöttek, hogy tettekkel valósítják meg a nemzet követeléseit.",
        "Az egyetemi ifjúsággal kiegészült tömeg Landerer és Heckenast nyomdájához vonult, ahol a cenzúra engedélye nélkül, a sajtószabadság első gyakorlati tettével kinyomtatták a 12 pontot ('Mit kíván a magyar nemzet') és Petőfi forradalmi költeményét, a 'Nemzeti dalt'.",
        "Délután a Nemzeti Múzeum előtt tízezres népgyűlés hallgatta a szónoklatokat, majd a tömeg átvonult Budára, ahol a Helytartótanács elfogadta a követeléseket, és harc nélkül kiszabadították börtönéből a sajtóvétségért elítélt Táncsics Mihályt. A pesti forradalom vérontás nélkül győzött."
    ],
    [
        {"lemma": "márciusi ifjak", "pos": "noun", "cefr": "B1", "gloss": "Youth of March (young 1848 revolutionaries)"},
        {"lemma": "sajtószabadság", "pos": "noun", "cefr": "B1", "gloss": "freedom of the press"},
        {"lemma": "vérontás nélkül", "pos": "adverb", "cefr": "B1", "gloss": "without bloodshed, peacefully"},
        {"lemma": "elszaval", "pos": "verb", "cefr": "B1", "gloss": "to recite (poem passionately)"},
        {"lemma": "kiszabadít", "pos": "verb", "cefr": "B1", "gloss": "to liberate, free from prison"}
    ],
    [
        {
            "question": "Melyik két alapvető dokumentumot nyomtatták ki a forradalmárok 1848. március 15-én a cenzúra engedélye nélkül?",
            "options": ["A 12 pontot és a Nemzeti dalt", "A Hitelt és a Szózatot", "A Függetlenségi Nyilatkozatot és a Himnuszt", "Az Alaptörvényt és a Pragmatica Sanctiót"],
            "correctIndex": 0,
            "explanation": "Landerer nyomdájában a 12 pontot és Petőfi Nemzeti dalát nyomtatták ki."
        }
    ]
)
write_json(STORIES_DIR / "story.b1.forradalom.01.json", story_1)

voc_1 = {
    "id": "voc.b1.forradalom.01",
    "title": "A március 15-i forradalom szókincse",
    "description": "Márciusi ifjak, 12 pont, Nemzeti dal, sajtószabadság, vérontás nélkül és kiszabadítás.",
    "entries": [
        {"lemma": "márciusi ifjak", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "the young radical intellectuals of the 1848 March Revolution", "examples": [{"hu": "A márciusi ifjak a Pilvax kávéházban találkoztak.", "en": "The Youth of March met in the Pilvax cafe."}]}]},
        {"lemma": "sajtószabadság", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "freedom of the press, abolition of censorship", "examples": [{"hu": "A 12 pont első követelése a sajtószabadság volt.", "en": "The first demand of the 12 Points was freedom of the press."}]}]},
        {"lemma": "vérontás nélkül", "pos": "adverb", "cefr": "B1", "definitions": [{"meaning": "without bloodshed, through peaceful revolution", "examples": [{"hu": "A pesti forradalom vérontás nélkül győzött.", "en": "The revolution in Pest was victorious without bloodshed."}]}]},
        {"lemma": "elszaval", "pos": "verb", "cefr": "B1", "definitions": [{"meaning": "to recite poem publicly", "examples": [{"hu": "Petőfi elszavalta a Nemzeti dalt a múzeum lépcsőjén.", "en": "Petőfi recited the National Song on the museum steps."}]}]},
        {"lemma": "kiszabadít", "pos": "verb", "cefr": "B1", "definitions": [{"meaning": "to liberate prisoner", "examples": [{"hu": "A tömeg kiszabadította Táncsics Mihályt a börtönből.", "en": "The crowd liberated Mihály Táncsics from prison."}]}]}
    ]
}
write_json(VOCAB_DIR / "voc.b1.forradalom.01.json", voc_1)

gr_1 = {
    "id": "gr.b1.forradalom.01",
    "title": "Forradalmi cselekvésláncolatok és időhatározás (miután, azonnal, harc nélkül)",
    "description": "Narrating fast-paced historical events and dramatic citizen movements.",
    "rules": [
        "A forradalmi események leírásában az igekötős igék ('kivív', 'kiszabadít', 'kinyomtat', 'átvonul') határozott és eredményes cselekvést fejeznek ki.",
        "A békés forradalom sajátosságait a 'harc nélkül', 'vérontás nélkül' módhatározói kifejezések jelenítik meg."
    ],
    "tables": [
        {"headers": ["Ige / Kifejezés", "Funkció", "Példa"], "rows": [
            ["kivív", "küzdelemmel elér", "Kivívták a sajtószabadságot."],
            ["kinyomtat", "nyomdában sokszorosít", "Kinyomtatták a 12 pontot."],
            ["vérontás nélkül", "békés jelleg", "Vérontás nélkül győztek."]
        ]}
    ],
    "examples": [
        {"spanish": "1848. március 15-én a pesti ifjúság vérontás nélkül vívta ki a szabadságot.", "english": "On March 15, 1848, the youth of Pest won freedom without bloodshed."},
        {"spanish": "Miután kinyomtatták a Nemzeti dalt, a Nemzeti Múzeum elé vonultak.", "english": "After printing the National Song, they marched in front of the National Museum."},
        {"spanish": "A Helytartótanács harc nélkül elfogadta a nemzet 12 pontját.", "english": "The Governing Council accepted the nation's 12 Points without a fight."}
    ]
}
write_json(GRAMMAR_DIR / "gr.b1.forradalom.01.json", gr_1)

exs_1 = [
    {"id": "ex.b1.forradalom.01.01", "type": "multiple-choice", "lesson": "lesson.b1.forradalom.01", "teaches": ["marcius-15-1848"], "prompt": "Melyik napon tört ki a pesti forradalom?", "options": ["1848. március 15-én", "1848. április 11-én", "1849. március 15-én", "1848. október 6-án"], "correctIndex": 0, "explanation": "A forradalom 1848. március 15-én robbant ki Pesten."},
    {"id": "ex.b1.forradalom.01.02", "type": "fill-blank", "lesson": "lesson.b1.forradalom.01", "teaches": ["marciusi-ifjak"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A forradalom vezetői a fiatal radikális értelmiségiek, a *márciusi ifjak* voltak.", "target": "márciusi ifjak"},
    {"id": "ex.b1.forradalom.01.03", "type": "sentence-builder", "lesson": "lesson.b1.forradalom.01", "teaches": ["sajtoszabadsag", "kiviv"], "prompt": "Rakd össze a mondatot a helyes sorrendben!", "chips": ["A", "forradalmárok", "vérontás", "nélkül", "kivívták", "a", "sajtószabadságot."], "target": "A forradalmárok vérontás nélkül kivívták a sajtószabadságot.", "english": "The revolutionaries won freedom of the press without bloodshed."},
    {"id": "ex.b1.forradalom.01.04", "type": "multiple-choice", "lesson": "lesson.b1.forradalom.01", "teaches": ["Petofi-Nemzeti-dal"], "prompt": "Ki írta a forradalom híres költeményét, a Nemzeti dalt?", "options": ["Petőfi Sándor", "Kölcsey Ferenc", "Vörösmarty Mihály", "Arany János"], "correctIndex": 0, "explanation": "Petőfi Sándor írta a Nemzeti dalt ('Talpra magyar, hí a haza!')."},
    {"id": "ex.b1.forradalom.01.05", "type": "fill-blank", "lesson": "lesson.b1.forradalom.01", "teaches": ["kiszabadit"], "prompt": "Egészítsd ki a mondatot a megfelelő igealakkal!", "sentence": "A pesti tömeg börtönéből *kiszabadította* Táncsics Mihályt.", "target": "kiszabadította"},
    {"id": "ex.b1.forradalom.01.06", "type": "sentence-builder", "lesson": "lesson.b1.forradalom.01", "teaches": ["12-pont", "kinyomtat"], "prompt": "Alkoss szabályos összetett mondatot!", "chips": ["A", "nyomdában", "cenzúra", "nélkül", "kinyomtatták", "a", "12", "pontot."], "target": "A nyomdában cenzúra nélkül kinyomtatták a 12 pontot.", "english": "In the printing house, they printed the 12 Points without censorship."},
    {"id": "ex.b1.forradalom.01.07", "type": "multiple-choice", "lesson": "lesson.b1.forradalom.01", "teaches": ["Pilvax"], "prompt": "Melyik kávéház volt a márciusi ifjak legfőbb találkozóhelye?", "options": ["A Pilvax kávéház", "A New York kávéház", "A Centrál kávéház", "A Gerbeaud cukrászda"], "correctIndex": 0, "explanation": "A Pilvax kávéházban gyülekeztek a márciusi ifjak 1848. március 15-én reggel."},
    {"id": "ex.b1.forradalom.01.08", "type": "fill-blank", "lesson": "lesson.b1.forradalom.01", "teaches": ["verontas-nelkul"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A pesti forradalom nagyszerűsége az volt, hogy *vérontás nélkül* győzött.", "target": "vérontás nélkül"}
]
write_json(EXERCISES_DIR / "ex.b1.forradalom.01.json", make_exercise_group("ex.b1.forradalom.01", "Március 15. gyakorlatok", "Gyakorlatok az 1848. március 15-i eseményekről, Petőfiről és a forradalmi cselekvésláncolatokról.", exs_1))

lesson_1 = make_lesson(
    "lesson.b1.forradalom.01",
    "1848. március 15.: A pesti forradalom és a márciusi ifjak",
    "Forradalmi cselekvésláncolatok és igekötős szerkezetek (kivív, kinyomtat, kiszabadít)",
    "Megismerjük az 1848. március 15-i pesti eseményeket, a márciusi ifjak fellépését, a 12 pontot és a Nemzeti dalt.",
    ["Megérteni március 15. nemzeti ünnepünk történeti alapjait", "Használni a forradalmi események elbeszélő nyelvtani formáit", "Ismerni a Pilvax kávéház, a Nemzeti Múzeum és Táncsics kiszabadításának jelentőségét"],
    "story.b1.forradalom.01",
    "voc.b1.forradalom.01",
    "gr.b1.forradalom.01",
    "ex.b1.forradalom.01",
    [e["id"] for e in exs_1]
)
write_json(LESSONS_DIR / "lesson.b1.forradalom.01.json", lesson_1)


# ==========================================
# LESSON 2: b1-forradalom-02 (Az áprilisi törvények 1848)
# ==========================================
story_2 = make_story(
    "story.b1.forradalom.02",
    "Az áprilisi törvények (1848. április 11.) és az első felelős kormány",
    "1848. április 11-én V. Ferdinánd király szentesítette az áprilisi törvényeket, amelyek lerakták a modern, polgári, alkotmányos Magyarország alapjait és felállították a Batthyány-kormányt.",
    "Pozsony és Pest",
    ["Constitutional and legislative enactment (felelős kormány, szentesít, hatályba lép)", "Birth of modern parliamentary democracy"],
    ["áprilisi törvények", "Batthyány Lajos", "felelős magyar kormány", "jobbágyfelszabadítás", "közteherviselés"],
    [
        "A pesti forradalom hírére a pozsonyi országgyűlés rendkívüli gyorsasággal törvénybe foglalta a polgári átalakulás teljes programját. 1848. április 11-én V. Ferdinánd király szentesítette (aláírta) a 31 törvénycikkből álló áprilisi törvényeket.",
        "Az áprilisi törvények felszámolták a feudális rendszert: kimondták a kötelező jobbágyfelszabadítást (a parasztok a föld tulajdonosaivá váltak), az általános közteherviselést (a nemesi adómentesség megszűnt), a sajtószabadságot, valamint az Erdély és Magyarország közötti uniót.",
        "Létrejött az első független, az országgyűlésnek felelős magyar kormány, amelynek miniszterelnöke gróf Batthyány Lajos lett. Kormányában a reformkor legnagyobb alakjai kaptak tárcát: Kossuth Lajos (pénzügy), Széchenyi István (közlekedés), Deák Ferenc (igazságügy) és Eötvös József (vallás- és oktatásügy)."
    ],
    [
        {"lemma": "felelős kormány", "pos": "noun", "cefr": "B1", "gloss": "responsible parliamentary cabinet"},
        {"lemma": "szentesít", "pos": "verb", "cefr": "B1", "gloss": "to sanction, ratify into law (royal assent)"},
        {"lemma": "áprilisi törvények", "pos": "noun", "cefr": "B1", "gloss": "April Laws of 1848"},
        {"lemma": "adómentesség", "pos": "noun", "cefr": "B1", "gloss": "tax exemption"},
        {"lemma": "unió", "pos": "noun", "cefr": "B1", "gloss": "union (between Hungary & Transylvania)"}
    ],
    [
        {
            "question": "Ki lett Magyarország legelső felelős miniszterelnöke 1848-ban?",
            "options": ["Gróf Batthyány Lajos", "Kossuth Lajos", "Gróf Széchenyi István", "Deák Ferenc"],
            "correctIndex": 0,
            "explanation": "Gróf Batthyány Lajos alakította meg az első felelős magyar kormányt."
        }
    ]
)
write_json(STORIES_DIR / "story.b1.forradalom.02.json", story_2)

voc_2 = {
    "id": "voc.b1.forradalom.02",
    "title": "Az áprilisi törvények és az alkotmányosság szókincse",
    "description": "Áprilisi törvények, felelős kormány, szentesítés, adómentesség megszűnése és unió.",
    "entries": [
        {"lemma": "áprilisi törvények", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "April Laws creating modern constitutional Hungary (1848)", "examples": [{"hu": "Az áprilisi törvények modern polgári államot teremtettek.", "en": "The April Laws created a modern civil state."}]}]},
        {"lemma": "felelős kormány", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "government cabinet responsible to parliament", "examples": [{"hu": "Batthyány Lajos vezette az első felelős kormányt.", "en": "Lajos Batthyány led the first responsible government."}]}]},
        {"lemma": "szentesít", "pos": "verb", "cefr": "B1", "definitions": [{"meaning": "to give royal assent / sign bill into law", "examples": [{"hu": "A király 1848. április 11-én szentesítette a törvényeket.", "en": "The king gave royal assent to the laws on April 11, 1848."}]}]},
        {"lemma": "adómentesség", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "tax exemption privilege", "examples": [{"hu": "Megszűnt a nemesség évszázados adómentessége.", "en": "The nobility's centuries-old tax exemption ended."}]}]},
        {"lemma": "unió", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "union between Transylvania and Hungary", "examples": [{"hu": "Megvalósult az unió Erdéllyel.", "en": "The union with Transylvania was realized."}]}]}
    ]
}
write_json(VOCAB_DIR / "voc.b1.forradalom.02.json", voc_2)

gr_2 = {
    "id": "gr.b1.forradalom.02",
    "title": "Alkotmányos és jogi érvényesülést jelölő szerkezetek (szentesít, hatályba lép, felelős)",
    "description": "Formulating constitutional reforms, cabinet responsibilities, and legislative enactments.",
    "rules": [
        "A törvényhozási folyamatban a 'szentesít' (királyi aláírás), 'hatályba lép' (érvényessé válás) szakkifejezéseket alkalmazzuk.",
        "A politikai felelősséget a 'felelős valakinek / a parlamentnek' szerkezettel fogalmazzuk meg."
    ],
    "tables": [
        {"headers": ["Kifejezés", "Jogi funkció", "Példa"], "rows": [
            ["szentesít", "királyi aláírás", "A király szentesítette a törvényeket."],
            ["hatályba lép", "érvényesség kezdete", "A törvények azonnal hatályba léptek."],
            ["felelős a parlamentnek", "demokratikus elszámoltathatóság", "A kormány felelős a képviselőknek."]
        ]}
    ],
    "examples": [
        {"spanish": "1848. április 11-én az uralkodó szentesítette az áprilisi törvényeket.", "english": "On April 11, 1848, the monarch sanctioned the April Laws."},
        {"spanish": "A Batthyány-kormány a népképviseleti országgyűlésnek volt felelős.", "english": "The Batthyány cabinet was responsible to the representative parliament."},
        {"spanish": "A törvények hatályba lépésével megszűnt a jobbágyság intézménye.", "english": "With the entry into force of the laws, the institution of serfdom ceased."}
    ]
}
write_json(GRAMMAR_DIR / "gr.b1.forradalom.02.json", gr_2)

exs_2 = [
    {"id": "ex.b1.forradalom.02.01", "type": "multiple-choice", "lesson": "lesson.b1.forradalom.02", "teaches": ["aprilisi-torvenyek-1848"], "prompt": "Melyik napon szentesítette a király az áprilisi törvényeket?", "options": ["1848. április 11-én", "1848. március 15-én", "1848. szeptember 29-én", "1849. április 14-én"], "correctIndex": 0, "explanation": "Az áprilisi törvényeket 1848. április 11-én írta alá V. Ferdinánd király."},
    {"id": "ex.b1.forradalom.02.02", "type": "fill-blank", "lesson": "lesson.b1.forradalom.02", "teaches": ["Batthyany-Lajos"], "prompt": "Egészítsd ki a mondatot!", "sentence": "Az első felelős magyar miniszterelnök gróf *Batthyány Lajos* lett.", "target": "Batthyány Lajos"},
    {"id": "ex.b1.forradalom.02.03", "type": "sentence-builder", "lesson": "lesson.b1.forradalom.02", "teaches": ["szentesit", "torvenyek"], "prompt": "Rakd össze a mondatot helyes sorrendben!", "chips": ["A", "király", "aláírta", "és", "szentesítette", "az", "áprilisi", "törvényeket."], "target": "A király aláírta és szentesítette az áprilisi törvényeket.", "english": "The king signed and sanctioned the April Laws."},
    {"id": "ex.b1.forradalom.02.04", "type": "multiple-choice", "lesson": "lesson.b1.forradalom.02", "teaches": ["miniszterek-1848"], "prompt": "Milyen tárcát töltött be Kossuth Lajos a Batthyány-kormányban?", "options": ["Pénzügyminiszter", "Hadügyminiszter", "Igazságügy-miniszter", "Vallásügyi miniszter"], "correctIndex": 0, "explanation": "Kossuth Lajos volt az első kormány pénzügyminisztere."},
    {"id": "ex.b1.forradalom.02.05", "type": "fill-blank", "lesson": "lesson.b1.forradalom.02", "teaches": ["felelos-kormany"], "prompt": "Egészítsd ki a mondatot a megfelelő szókapcsolattal!", "sentence": "Magyarországon létrejött az országgyűlésnek felelős független *kormány*.", "target": "kormány"},
    {"id": "ex.b1.forradalom.02.06", "type": "sentence-builder", "lesson": "lesson.b1.forradalom.02", "teaches": ["kozteherviszeles", "adomentesseg"], "prompt": "Alkoss szabályos alkotmányos mondatot!", "chips": ["A", "törvények", "eltörölték", "a", "nemesség", "adómentességét."], "target": "A törvények eltörölték a nemesség adómentességét.", "english": "The laws abolished the tax exemption of the nobility."},
    {"id": "ex.b1.forradalom.02.07", "type": "multiple-choice", "lesson": "lesson.b1.forradalom.02", "teaches": ["unio-Erdellyel"], "prompt": "Melyik terület unióját mondták ki az 1848-as törvények?", "options": ["Erdély és Magyarország unióját", "Horvátország és Ausztria unióját", "Magyarország és Lengyelország unióját", "Buda és Bécs unióját"], "correctIndex": 0, "explanation": "Az áprilisi törvények megvalósították Magyarország és Erdély unióját."},
    {"id": "ex.b1.forradalom.02.08", "type": "fill-blank", "lesson": "lesson.b1.forradalom.02", "teaches": ["jobbagyfelszabaditas"], "prompt": "Egészítsd ki a mondatot!", "sentence": "Az áprilisi törvények elhozták a kötelező *jobbágyfelszabadítást*.", "target": "jobbágyfelszabadítást"}
]
write_json(EXERCISES_DIR / "ex.b1.forradalom.02.json", make_exercise_group("ex.b1.forradalom.02", "Az áprilisi törvények gyakorlatai", "Gyakorlatok az 1848. április 11-i törvényekről, a Batthyány-kormányról és az alkotmányos kifejezésekről.", exs_2))

lesson_2 = make_lesson(
    "lesson.b1.forradalom.02",
    "Az áprilisi törvények (1848. április 11.) és az első felelős kormány",
    "Alkotmányos és jogi érvényesülést jelölő szerkezetek (szentesít, felelős)",
    "Megtanuljuk az 1848. április 11-i áprilisi törvények tartalmát, a jobbágyfelszabadítást és az első felelős magyar kormány megalakulását.",
    ["Megérteni az áprilisi törvények alapvető jelentőségét a modern magyar államiságban", "Használni az alkotmányos és jogi érvényességi nyelvtani formákat", "Ismerni gróf Batthyány Lajos és a miniszterek szerepét"],
    "story.b1.forradalom.02",
    "voc.b1.forradalom.02",
    "gr.b1.forradalom.02",
    "ex.b1.forradalom.02",
    [e["id"] for e in exs_2]
)
write_json(LESSONS_DIR / "lesson.b1.forradalom.02.json", lesson_2)


# ==========================================
# LESSON 3: b1-forradalom-03 (Önvédelmi harc és Pákozd)
# ==========================================
story_3 = make_story(
    "story.b1.forradalom.03",
    "Az önvédelmi harc és a pákozdi győzelem (1848 ősze)",
    "Amikor a bécsi udvar fegyveres támadást indított Jellasics horvát bán vezetésével a magyar szabadság ellen, a születő honvédség Pákozdnál megállította a betörő sereget.",
    "Pákozd és az Alföld",
    ["Defensive mobilization and military resistance clauses (visszaver, toboroz, fegyverbe hív)", "Birth of the Hungarian Defence Forces (Honvédség)"],
    ["pákozdi csata", "Jellasics bán", "Honvédelmi Bizottmány", "toborzó körút", "honvédség"],
    [
        "1848 nyarán a bécsi udvar elérkezettnek látta az időt a magyar vívmányok fegyveres felszámolására. Titokban bátorította a nemzetiségi mozgalmakat, és 1848 szeptemberében Josip Jellasics horvát bán negyvenezres seregével átlépte a Drávát, megindulva Pest-Buda felé.",
        "A végveszélybe került haza védelmére Kossuth Lajos vezetésével megalakult az Országos Honvédelmi Bizottmány. Kossuth híres toborzó körútra indult az Alföldön: Cegléden, Kecskeméten és Szegeden elmondott lángoló beszédei nyomán tízezrek csatlakoztak az újonnan alakuló nemzeti hadsereghez, a honvédséghez.",
        "1848. szeptember 29-én a Velencei-tó partján, Pákozdnál a fiatal magyar honvédsereg Móga János tábornok vezetésével hősies csatában visszaverte Jellasics seregének támadását. A bán fegyverszünetet kért, majd gyáván Bécs felé menekült, megmentve a magyar fővárost az elfoglalástól."
    ],
    [
        {"lemma": "honvédség", "pos": "noun", "cefr": "B1", "gloss": "Hungarian Army / National Defence Forces"},
        {"lemma": "toborzás", "pos": "noun", "cefr": "B1", "gloss": "recruitment, rallying troops"},
        {"lemma": "önvédelmi harc", "pos": "noun", "cefr": "B1", "gloss": "war of self-defense"},
        {"lemma": "visszaver", "pos": "verb", "cefr": "B1", "gloss": "to repel, beat back (an assault)"},
        {"lemma": "fegyverszünet", "pos": "noun", "cefr": "B1", "gloss": "armistice, ceasefire"}
    ],
    [
        {
            "question": "Melyik csatában verte vissza a születő magyar honvédség Jellasics támadását 1848. szeptember 29-én?",
            "options": ["A pákozdi csatában", "Az isaszegi csatában", "A mohácsi csatában", "A trencséni csatában"],
            "correctIndex": 0,
            "explanation": "1848. szeptember 29-én a pákozdi csatában verték vissza Jellasics bán seregét."
        }
    ]
)
write_json(STORIES_DIR / "story.b1.forradalom.03.json", story_3)

voc_3 = {
    "id": "voc.b1.forradalom.03",
    "title": "A nemzetvédelem és toborzás szókincse",
    "description": "Honvédség, toborzás, önvédelmi harc, visszaverés és fegyverszünet.",
    "entries": [
        {"lemma": "honvédség", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "Hungarian Armed Forces, national defense army", "examples": [{"hu": "1848-ban megszületett a modern magyar honvédség.", "en": "In 1848, the modern Hungarian Defence Forces were born."}]}]},
        {"lemma": "toborzás", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "troop recruitment campaign", "examples": [{"hu": "Kossuth toborzó beszédei ezreket állítottak csatasorba.", "en": "Kossuth's recruitment speeches placed thousands into battle lines."}]}]},
        {"lemma": "önvédelmi harc", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "struggle for self-defense", "examples": [{"hu": "A forradalom önvédelmi szabadságharccá alakult át.", "en": "The revolution transformed into a war of self-defense."}]}]},
        {"lemma": "visszaver", "pos": "verb", "cefr": "B1", "definitions": [{"meaning": "to repel enemy attack", "examples": [{"hu": "A honvédek visszaverték az ellenséges rohamot Pákozdnál.", "en": "The honvéds repelled the enemy charge at Pákozd."}]}]},
        {"lemma": "fegyverszünet", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "temporary armistice, truce", "examples": [{"hu": "Jellasics fegyverszünetet kért a vesztes csata után.", "en": "Jellasics asked for an armistice after the lost battle."}]}]}
    ]
}
write_json(VOCAB_DIR / "voc.b1.forradalom.03.json", voc_3)

gr_3 = {
    "id": "gr.b1.forradalom.03",
    "title": "Önvédelmet és mozgósítást kifejező szerkezetek (fegyverbe hív, visszaver, csatlakozik)",
    "description": "Describing military recruitment, patriotic mobilization, and defense against aggression.",
    "rules": [
        "A mozgósítást kifejező szókapcsolatok ('fegyverbe hív', 'csatasorba állít', 'toboroz') a nép védelmi felkelését érzékeltetik.",
        "A sikeres katonai elhárítást a 'visszaver', 'feltartóztat', 'megállít' igék írják le."
    ],
    "tables": [
        {"headers": ["Kifejezés", "Funkció", "Példa"], "rows": [
            ["fegyverbe hív", "mozgósítás", "Kossuth fegyverbe hívta az Alföld népét."],
            ["visszaver", "támadás elhárítása", "Pákozdnál visszaverték a támadást."],
            ["csatlakozik a honvédséghez", "önkéntes jelentkezés", "Ezrek csatlakoztak a honvédekhez."]
        ]}
    ],
    "examples": [
        {"spanish": "Kossuth toborzó körútja során tízezrek álltak be a honvédség soraiba.", "english": "During Kossuth's recruiting tour, tens of thousands enlisted in the ranks of the army."},
        {"spanish": "A pákozdi győzelem bebizonyította, hogy a nemzet képes megvédeni szabadságát.", "english": "The victory at Pákozd proved that the nation was able to defend its freedom."},
        {"spanish": "A honvédek visszaverték a császári csapatok előrenyomulását.", "english": "The honvéds repelled the advance of the imperial troops."}
    ]
}
write_json(GRAMMAR_DIR / "gr.b1.forradalom.03.json", gr_3)

exs_3 = [
    {"id": "ex.b1.forradalom.03.01", "type": "multiple-choice", "lesson": "lesson.b1.forradalom.03", "teaches": ["pakozdi-csata-1848"], "prompt": "Melyik évben és napon zajlott a pákozdi győzelem?", "options": ["1848. szeptember 29-én", "1848. március 15-én", "1849. május 21-én", "1849. augusztus 13-án"], "correctIndex": 0, "explanation": "A pákozdi csata 1848. szeptember 29-én zárult magyar győzelemmel."},
    {"id": "ex.b1.forradalom.03.02", "type": "fill-blank", "lesson": "lesson.b1.forradalom.03", "teaches": ["honvedseg"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A haza védelmére megalakult a nemzeti *honvédség*.", "target": "honvédség"},
    {"id": "ex.b1.forradalom.03.03", "type": "sentence-builder", "lesson": "lesson.b1.forradalom.03", "teaches": ["visszaver", "tamadas"], "prompt": "Rakd össze a mondatot a megfelelő sorrendben!", "chips": ["A", "magyar", "honvédek", "Pákozdnál", "visszaverték", "a", "támadást."], "target": "A magyar honvédek Pákozdnál visszaverték a támadást.", "english": "The Hungarian soldiers repelled the attack at Pákozd."},
    {"id": "ex.b1.forradalom.03.04", "type": "multiple-choice", "lesson": "lesson.b1.forradalom.03", "teaches": ["Jellasics"], "prompt": "Ki vezette a Magyarország ellen indított támadást 1848 szeptemberében?", "options": ["Josip Jellasics horvát bán", "Haynau tábornok", "Windisch-Grätz herceg", "Paskievics herceg"], "correctIndex": 0, "explanation": "Jellasics horvát bán tört be a déli határon a bécsi udvar megbízásából."},
    {"id": "ex.b1.forradalom.03.05", "type": "fill-blank", "lesson": "lesson.b1.forradalom.03", "teaches": ["toborzas"], "prompt": "Egészítsd ki a mondatot a megfelelő szóval!", "sentence": "Kossuth Lajos alföldi *toborzó* körútja sikeres volt.", "target": "toborzó"},
    {"id": "ex.b1.forradalom.03.06", "type": "sentence-builder", "lesson": "lesson.b1.forradalom.03", "teaches": ["onvedelmi-harc", "nemzet"], "prompt": "Alkoss szabályos történelmi mondatot!", "chips": ["A", "magyar", "nemzet", "önvédelmi", "szabadságharcra", "kényszerült."], "target": "A magyar nemzet önvédelmi szabadságharcra kényszerült.", "english": "The Hungarian nation was forced into a war of self-defense."},
    {"id": "ex.b1.forradalom.03.07", "type": "multiple-choice", "lesson": "lesson.b1.forradalom.03", "teaches": ["Honvedelmi-Bizottmany"], "prompt": "Milyen testület vette át a végrehajtó hatalmat a kormány lemondása után 1848 őszén?", "options": ["Az Országos Honvédelmi Bizottmány Kossuth vezetésével", "A Királyi Tanács", "A Szenátus", "A Helytartótanács"], "correctIndex": 0, "explanation": "Az Országos Honvédelmi Bizottmány irányította a hadügyeket Kossuth elnökletével."},
    {"id": "ex.b1.forradalom.03.08", "type": "fill-blank", "lesson": "lesson.b1.forradalom.03", "teaches": ["fegyverszunet"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A vereséget szenvedett Jellasics *fegyverszünetet* kért és elmenekült.", "target": "fegyverszünetet"}
]
write_json(EXERCISES_DIR / "ex.b1.forradalom.03.json", make_exercise_group("ex.b1.forradalom.03", "Pákozd és az önvédelmi harc gyakorlatai", "Gyakorlatok a pákozdi csatáról, Kossuth toborzóútjáról és az önvédelmi kifejezésekről.", exs_3))

lesson_3 = make_lesson(
    "lesson.b1.forradalom.03",
    "Az önvédelmi harc és a pákozdi győzelem (1848 ősze)",
    "Önvédelmet és mozgósítást kifejező szerkezetek (visszaver, toboroz)",
    "Megismerjük az 1848 őszi eseményeket: Jellasics támadását, Kossuth toborzóútját és a pákozdi győzelmet.",
    ["Megérteni a szabadságharc önvédelmi jellegét és a pákozdi csata fontosságát", "Használni a katonai mozgósítás és önvédelem nyelvtani formáit", "Ismerni a Honvédelmi Bizottmány és Kossuth toborzó beszédének szerepét"],
    "story.b1.forradalom.03",
    "voc.b1.forradalom.03",
    "gr.b1.forradalom.03",
    "ex.b1.forradalom.03",
    [e["id"] for e in exs_3]
)
write_json(LESSONS_DIR / "lesson.b1.forradalom.03.json", lesson_3)


# ==========================================
# LESSON 4: b1-forradalom-04 (A tavaszi hadjárat 1849)
# ==========================================
story_4 = make_story(
    "story.b1.forradalom.04",
    "A dicsőséges tavaszi hadjárat és Buda bevétele (1849)",
    "1849 tavaszán a Görgei Artúr vezette honvédsereg zseniális hadműveletekkel egymás után győzte le a császári hadakat, és május 21-én visszafoglalta a budai várat.",
    "Hatvan, Isaszeg, Komárom és Buda vára",
    ["Military momentum and triumphant reporting clauses (felszabadít, bevesz, egymás után arat győzelmet)", "Victorious campaigns in history"],
    ["tavaszi hadjárat", "Görgei Artúr", "Isaszeg", "Buda bevétele", "1849. május 21."],
    [
        "A nehéz téli hónapok és a főváros ideiglenes kiürítése után a debreceni kormány és a hadvezetés ellentámadásra készült. 1849 áprilisában kezdetét vette a magyar hadtörténelem legdicsőségesebb hadművelete: a tavaszi hadjárat, Görgei Artúr főparancsnok, Klapka György és Damjanich János tábornokok vezetésével.",
        "A honvédek egymás után arattak fényes győzelmeket a császári fősereg felett: Hatvannál, Tápióbicskénél, Isaszegnél és Nagysallónál, felmentve a hősies Komárom várát. A császári csapatokat szinte teljesen kiszorították a Magyar Királyság területéről.",
        "A hadjárat csúcspontjaként 1849. május 21-én a honvédsereg véres, de diadalmas ostromban bevette és felszabadította Buda várát. Henczi osztrák várparancsnok elesett, és a magyar trikolór ismét büszkén lobogott a királyi palotán. E dicsőséges nap emlékére május 21. a Magyar Honvédelem Napja."
    ],
    [
        {"lemma": "tavaszi hadjárat", "pos": "noun", "cefr": "B1", "gloss": "Spring Campaign of 1849"},
        {"lemma": "főparancsnok", "pos": "noun", "cefr": "B1", "gloss": "Commander-in-Chief"},
        {"lemma": "kiszorít", "pos": "verb", "cefr": "B1", "gloss": "to push out, dislodge (enemy forces)"},
        {"lemma": "bevesz", "pos": "verb", "cefr": "B1", "gloss": "to capture, take (a fortress)"},
        {"lemma": "trikolór", "pos": "noun", "cefr": "B1", "gloss": "tricolour flag (red-white-green)"}
    ],
    [
        {
            "question": "Melyik napon foglalta vissza a honvédsereg Buda várát 1849-ben, amely ma a Magyar Honvédelem Napja?",
            "options": ["1849. május 21-én", "1848. március 15-én", "1849. április 14-én", "1848. április 11-én"],
            "correctIndex": 0,
            "explanation": "Buda visszafoglalása 1849. május 21-én történt; ez a nap a Honvédelem Napja."
        }
    ]
)
write_json(STORIES_DIR / "story.b1.forradalom.04.json", story_4)

voc_4 = {
    "id": "voc.b1.forradalom.04",
    "title": "A tavaszi hadjárat és győzelmek szókincse",
    "description": "Tavaszi hadjárat, főparancsnok, kiszorítás, várbevétel és a honvédelem napja.",
    "entries": [
        {"lemma": "tavaszi hadjárat", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "Spring Campaign of 1849 which liberated Hungary", "examples": [{"hu": "A tavaszi hadjárat során felszabadult az ország.", "en": "During the Spring Campaign, the country was liberated."}]}]},
        {"lemma": "főparancsnok", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "Commander-in-Chief of the armed forces", "examples": [{"hu": "Görgei Artúr volt a hadsereg tehetséges főparancsnoka.", "en": "Artúr Görgei was the talented commander-in-chief of the army."}]}]},
        {"lemma": "kiszorít", "pos": "verb", "cefr": "B1", "definitions": [{"meaning": "to force out / dislodge enemy troops", "examples": [{"hu": "A honvédek kiszorították a császáriakat az országból.", "en": "The honvéds pushed the imperials out of the country."}]}]},
        {"lemma": "bevesz", "pos": "verb", "cefr": "B1", "definitions": [{"meaning": "to capture a besieged fortress", "examples": [{"hu": "A honvédsereg 1849. május 21-én bevette Budát.", "en": "The army captured Buda on May 21, 1849."}]}]},
        {"lemma": "trikolór", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "national tricolour flag", "examples": [{"hu": "A piros-fehér-zöld trikolór lobogott a várban.", "en": "The red-white-green tricolour flew over the castle."}]}]}
    ]
}
write_json(VOCAB_DIR / "voc.b1.forradalom.04.json", voc_4)

gr_4 = {
    "id": "gr.b1.forradalom.04",
    "title": "Katonai sikereket és folyamatos győzelmeket leíró kifejezések (egymás után, bevesz, felszabadít)",
    "description": "Narrating swift military sequences, victories, and liberations.",
    "rules": [
        "A hadműveletek lendületét az 'egymás után arat győzelmet', 'sorra beveszi' kifejezések fejezik ki.",
        "A területi helyreállítást a 'felszabadít', 'visszafoglal' igék írják le pontosan."
    ],
    "tables": [
        {"headers": ["Kifejezés", "Funkció", "Példa"], "rows": [
            ["egymás után arat győzelmet", "folyamatos diadal", "Egymás után verték meg a seregeket."],
            ["beveszi a várat", "erőd elfoglalása", "Rohammal bevették Budát."],
            ["felszabadít", "felszabadítás", "Felszabadították az ország nagy részét."]
        ]}
    ],
    "examples": [
        {"spanish": "A tavaszi hadjáratban a honvédség egymás után győzte le a császári hadtesteket.", "english": "In the Spring Campaign, the army defeated the imperial corps one after another."},
        {"spanish": "1849. május 21-én a magyar csapatok bevették Buda várát.", "english": "On May 21, 1849, the Hungarian troops took the castle of Buda."},
        {"spanish": "Görgei hadserege felszabadította a Dunántúlt és a fővárost.", "english": "Görgei's army liberated Transdanubia and the capital."}
    ]
}
write_json(GRAMMAR_DIR / "gr.b1.forradalom.04.json", gr_4)

exs_4 = [
    {"id": "ex.b1.forradalom.04.01", "type": "multiple-choice", "lesson": "lesson.b1.forradalom.04", "teaches": ["tavaszi-hadjarat-1849"], "prompt": "Mikor zajlott a dicsőséges tavaszi hadjárat?", "options": ["1849 tavaszán", "1848 tavaszán", "1848 őszén", "1849 őszén"], "correctIndex": 0, "explanation": "A tavaszi hadjárat 1849 áprilisában és májusában zajlott le."},
    {"id": "ex.b1.forradalom.04.02", "type": "fill-blank", "lesson": "lesson.b1.forradalom.04", "teaches": ["Gorgei-Artur"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A tavaszi hadjárat zseniális fővezére *Görgei Artúr* tábornok volt.", "target": "Görgei Artúr"},
    {"id": "ex.b1.forradalom.04.03", "type": "sentence-builder", "lesson": "lesson.b1.forradalom.04", "teaches": ["bevesz", "Buda"], "prompt": "Rakd össze a diadalmas mondatot!", "chips": ["1849.", "május", "21-én", "a", "honvédek", "bevették", "Buda", "várát."], "target": "1849. május 21-én a honvédek bevették Buda várát.", "english": "On May 21, 1849, the soldiers captured the castle of Buda."},
    {"id": "ex.b1.forradalom.04.04", "type": "multiple-choice", "lesson": "lesson.b1.forradalom.04", "teaches": ["Honvedelem-Napja"], "prompt": "Milyen ünnep május 21-e Magyarországon Buda 1849-es bevétele emlékére?", "options": ["A Magyar Honvédelem Napja", "A Nemzeti Ünnep", "A Zászló Napja", "A Szabadság Napja"], "correctIndex": 0, "explanation": "Május 21. a Magyar Honvédelem Napja."},
    {"id": "ex.b1.forradalom.04.05", "type": "fill-blank", "lesson": "lesson.b1.forradalom.04", "teaches": ["kiszorit"], "prompt": "Egészítsd ki a mondatot a megfelelő igealakkal!", "sentence": "A honvédség *kiszorította* a császári sereget az országból.", "target": "kiszorította"},
    {"id": "ex.b1.forradalom.04.06", "type": "sentence-builder", "lesson": "lesson.b1.forradalom.04", "teaches": ["egymas-utan", "gyozelem"], "prompt": "Alkoss szabályos mondatot!", "chips": ["A", "magyar", "csapatok", "egymás", "után", "arattak", "fényes", "győzelmeket."], "target": "A magyar csapatok egymás után arattak fényes győzelmeket.", "english": "The Hungarian troops won brilliant victories one after another."},
    {"id": "ex.b1.forradalom.04.07", "type": "multiple-choice", "lesson": "lesson.b1.forradalom.04", "teaches": ["Isaszeg"], "prompt": "Melyik volt a tavaszi hadjárat egyik legnagyobb és legdöntőbb csatája 1849. április 6-án?", "options": ["Az isaszegi csata", "A pákozdi csata", "A mohácsi csata", "A világosi csata"], "correctIndex": 0, "explanation": "Az isaszegi csata volt a tavaszi hadjárat első szakaszának legnagyobb diadala."},
    {"id": "ex.b1.forradalom.04.08", "type": "fill-blank", "lesson": "lesson.b1.forradalom.04", "teaches": ["trikolor"], "prompt": "Egészítsd ki a mondatot!", "sentence": "Buda ormán ismét a piros-fehér-zöld *trikolór* lobogott.", "target": "trikolór"}
]
write_json(EXERCISES_DIR / "ex.b1.forradalom.04.json", make_exercise_group("ex.b1.forradalom.04", "A tavaszi hadjárat gyakorlatai", "Gyakorlatok az 1849-es győzelmekről, Buda bevételéről és a katonai elbeszélő formákról.", exs_4))

lesson_4 = make_lesson(
    "lesson.b1.forradalom.04",
    "A dicsőséges tavaszi hadjárat és Buda bevétele (1849)",
    "Katonai sikereket és győzelmeket leíró szerkezetek (egymás után, bevesz)",
    "Megtanuljuk az 1849-es tavaszi hadjárat legfőbb csatáit (Isaszeg), Görgei vezetését és Buda május 21-i visszafoglalását.",
    ["Megérteni az 1849-es tavaszi hadjárat katonai eredményeit", "Használni a katonai diadalokat és folyamatos sikereket kifejező nyelvtani szerkezeteket", "Ismerni május 21., a Magyar Honvédelem Napja eredetét"],
    "story.b1.forradalom.04",
    "voc.b1.forradalom.04",
    "gr.b1.forradalom.04",
    "ex.b1.forradalom.04",
    [e["id"] for e in exs_4]
)
write_json(LESSONS_DIR / "lesson.b1.forradalom.04.json", lesson_4)


# ==========================================
# LESSON 5: b1-forradalom-05 (Függetlenségi Nyilatkozat és Világos)
# ==========================================
story_5 = make_story(
    "story.b1.forradalom.05",
    "A Függetlenségi Nyilatkozat és a világosi fegyverletétel (1849)",
    "1849. április 14-én Debrecenben kimondták a trónfosztást, de az orosz cári hadsereg beavatkozása a hatalmas túlerő miatt augusztus 13-án a világosi fegyverletételhez vezetett.",
    "Debreceni Nagytemplom és Világos",
    ["Tragic historical turning points and intervention clauses (beavatkozás következtében, túlerő miatt, fegyverletétel)", "Tragic end of the War of Independence"],
    ["Függetlenségi Nyilatkozat", "Debrecen", "kormányzó-elnök", "cári intervenció", "világosi fegyverletétel"],
    [
        "A tavaszi hadjárat sikerei közepette az országgyűlés Debrecenben ülésezett. 1849. április 14-én a Nagytemplomban a képviselők ünnepélyesen elfogadták a Függetlenségi Nyilatkozatot: kimondták a Habsburg-dinasztia trónfosztását, Magyarországot független állammá nyilvánították, és Kossuth Lajost választották meg az ország kormányzó-elnökévé.",
        "A fiatal Ferenc József császár belátta, hogy egyedül képtelen legyőzni a magyar honvédséget, ezért a Szent Szövetség értelmében I. Miklós orosz cárhoz fordult segítségért. 1849 nyarán a kétszázezres orosz cári hadsereg Paskievics vezetésével és a megerősített osztrák sereg két tűz közé szorította a szabadságharcot.",
        "A hatalmas katonai túlerővel szemben a harc fenntarthatatlanná vált. 1849. augusztus 13-án Görgei Artúr a Bécs által elutasított békés tárgyalások után a szőlősi mezőn, Világosnál letette a fegyvert az orosz csapatok előtt, megmentve megmaradt harcosait az azonnali mészárlástól."
    ],
    [
        {"lemma": "Függetlenségi Nyilatkozat", "pos": "noun", "cefr": "B1", "gloss": "Declaration of Independence (1849)"},
        {"lemma": "kormányzó-elnök", "pos": "noun", "cefr": "B1", "gloss": "Governor-President (Kossuth's title)"},
        {"lemma": "beavatkozás", "pos": "noun", "cefr": "B1", "gloss": "military intervention, invasion"},
        {"lemma": "fegyverletétel", "pos": "noun", "cefr": "B1", "gloss": "surrender of arms"},
        {"lemma": "túlerő", "pos": "noun", "cefr": "B1", "gloss": "overwhelming military superiority"}
    ],
    [
        {
            "question": "Hol és mikor fogadták el az 1849-es Függetlenségi Nyilatkozatot?",
            "options": ["Debrecenben, a Nagytemplomban 1849. április 14-én", "Pesten a Nemzeti Múzeumban 1848. március 15-én", "Pozsonyban 1848. április 11-én", "Világosnál 1849. augusztus 13-án"],
            "correctIndex": 0,
            "explanation": "Debrecenben a Nagytemplomban mondták ki a trónfosztást és Magyarország függetlenségét 1849. április 14-én."
        }
    ]
)
write_json(STORIES_DIR / "story.b1.forradalom.05.json", story_5)

voc_5 = {
    "id": "voc.b1.forradalom.05",
    "title": "A függetlenség és a szabadságharc végének szókincse",
    "description": "Függetlenségi Nyilatkozat, kormányzó-elnök, cári intervenció, fegyverletétel és túlerő.",
    "entries": [
        {"lemma": "Függetlenségi Nyilatkozat", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "Hungarian Declaration of Independence (April 14, 1849)", "examples": [{"hu": "A Függetlenségi Nyilatkozat kimondta a Habsburgok trónfosztását.", "en": "The Declaration of Independence declared the dethronement of the Habsburgs."}]}]},
        {"lemma": "kormányzó-elnök", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "Governor-President title held by Lajos Kossuth", "examples": [{"hu": "Kossuth Lajost kormányzó-elnökké választották Debrecenben.", "en": "Lajos Kossuth was elected Governor-President in Debrecen."}]}]},
        {"lemma": "beavatkozás", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "foreign armed intervention", "examples": [{"hu": "Az orosz cári hadsereg beavatkozása eldöntötte a háborút.", "en": "The intervention of the Russian tsarist army decided the war."}]}]},
        {"lemma": "fegyverletétel", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "military capitulation / surrender of arms", "examples": [{"hu": "1849. augusztus 13-án megtörtént a világosi fegyverletétel.", "en": "On August 13, 1849, the surrender at Világos took place."}]}]},
        {"lemma": "túlerő", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "overwhelming numerical odds", "examples": [{"hu": "A honvédség a hatalmas túlerő miatt kényszerült fegyverletételre.", "en": "The army was forced to surrender due to overwhelming odds."}]}]}
    ]
}
write_json(VOCAB_DIR / "voc.b1.forradalom.05.json", voc_5)

gr_5 = {
    "id": "gr.b1.forradalom.05",
    "title": "Történelmi ok-okozati és beavatkozási viszonyok (beavatkozás következtében, túlerő miatt, kényszerül)",
    "description": "Analyzing tragic historical turns, external intervention, and forced decisions.",
    "rules": [
        "A külső kényszer kifejezésére a 'miatt' (ok), 'következtében' (eredmény) és a 'kényszerül valamire' szerkezeteket használjuk.",
        "A méltóságteljes befejezést a 'letette a fegyvert', 'lezárult a küzdelem' kifejezések írják le."
    ],
    "tables": [
        {"headers": ["Kifejezés", "Funkció", "Példa"], "rows": [
            ["beavatkozás következtében", "külső ok", "A cári beavatkozás következtében vesztettek."],
            ["túlerő miatt", "aránytalan erők", "A túlerő miatt a harc befejeződött."],
            ["kényszerül valamire", "kényszer", "Fegyverletételre kényszerültek."]
        ]}
    ],
    "examples": [
        {"spanish": "A cári beavatkozás következtében a magyar sereg két tűz közé került.", "english": "As a consequence of the tsarist intervention, the Hungarian army was caught between two fires."},
        {"spanish": "A hatalmas túlerő miatt Görgei Világosnál letette a fegyvert az oroszok előtt.", "english": "Due to overwhelming force, Görgei laid down arms before the Russians at Világos."},
        {"spanish": "A szabadságharc elbukott, de eszméi örökre meghatározták a nemzet jövőjét.", "english": "The freedom fight was defeated, but its ideals forever determined the nation's future."}
    ]
}
write_json(GRAMMAR_DIR / "gr.b1.forradalom.05.json", gr_5)

exs_5 = [
    {"id": "ex.b1.forradalom.05.01", "type": "multiple-choice", "lesson": "lesson.b1.forradalom.05", "teaches": ["Fuggetlensegi-Nyilatkozat-1849"], "prompt": "Melyik városban fogadták el az 1849. április 14-i Függetlenségi Nyilatkozatot?", "options": ["Debrecenben (a Nagytemplomban)", "Pesten (a Múzeumban)", "Pozsonyban", "Szegeden"], "correctIndex": 0, "explanation": "Debrecen volt az ország ideiglenes fővárosa, a Nagytemplomban mondták ki a függetlenséget."},
    {"id": "ex.b1.forradalom.05.02", "type": "fill-blank", "lesson": "lesson.b1.forradalom.05", "teaches": ["kormanyzo-elnok"], "prompt": "Egészítsd ki a mondatot!", "sentence": "Debrecenben Kossuth Lajost az ország *kormányzó-elnökévé* választották.", "target": "kormányzó-elnökévé"},
    {"id": "ex.b1.forradalom.05.03", "type": "sentence-builder", "lesson": "lesson.b1.forradalom.05", "teaches": ["tulero-miatt", "fegyverletetel"], "prompt": "Rakd össze az okhatározói mondatot!", "chips": ["A", "hatalmas", "túlerő", "miatt", "fegyverletételre", "kényszerültek."], "target": "A hatalmas túlerő miatt fegyverletételre kényszerültek.", "english": "Due to the immense superior force, they were forced into surrender."},
    {"id": "ex.b1.forradalom.05.04", "type": "multiple-choice", "lesson": "lesson.b1.forradalom.05", "teaches": ["vilagosi-fegyverletetel-1849"], "prompt": "Mikor és hol történt a magyar honvédsereg fegyverletétele 1849-ben?", "options": ["1849. augusztus 13-án Világosnál", "1849. október 6-án Aradon", "1848. március 15-én Pesten", "1849. május 21-én Budán"], "correctIndex": 0, "explanation": "A szabadságharc katonai része 1849. augusztus 13-án Világosnál zárult fegyverletétellel."},
    {"id": "ex.b1.forradalom.05.05", "type": "fill-blank", "lesson": "lesson.b1.forradalom.05", "teaches": ["beavatkozas"], "prompt": "Egészítsd ki a mondatot a megfelelő szóval!", "sentence": "Az orosz cári hadsereg katonai *beavatkozása* eldöntötte a küzdelmet.", "target": "beavatkozása"},
    {"id": "ex.b1.forradalom.05.06", "type": "sentence-builder", "lesson": "lesson.b1.forradalom.05", "teaches": ["Gorgei", "oroszok"], "prompt": "Alkoss szabályos összetett mondatot!", "chips": ["Görgei", "a", "cári", "orosz", "csapatok", "előtt", "tette", "le", "a", "fegyvert."], "target": "Görgei a cári orosz csapatok előtt tette le a fegyvert.", "english": "Görgei laid down arms before the tsarist Russian troops."},
    {"id": "ex.b1.forradalom.05.07", "type": "multiple-choice", "lesson": "lesson.b1.forradalom.05", "teaches": ["Szent-Szovetseg"], "prompt": "Melyik uralkodó küldött 200 ezer fős sereget Ferenc József segítségére a szabadságharc leverésére?", "options": ["I. Miklós orosz cár", "Viktória brit királynő", "III. Napóleon francia császár", "IV. Frigyes Vilmos porosz király"], "correctIndex": 0, "explanation": "I. Miklós orosz cár küldte a beavatkozó intervenciós sereget 1849 nyarán."},
    {"id": "ex.b1.forradalom.05.08", "type": "fill-blank", "lesson": "lesson.b1.forradalom.05", "teaches": ["fegyverletetel"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A szőlősi mezőn lezajlott *fegyverletétel* lezárta az 1848–49-es harcokat.", "target": "fegyverletétel"}
]
write_json(EXERCISES_DIR / "ex.b1.forradalom.05.json", make_exercise_group("ex.b1.forradalom.05", "A szabadságharc vége gyakorlatok", "Gyakorlatok a Függetlenségi Nyilatkozatról, a cári beavatkozásról és a világosi fegyverletételről.", exs_5))

lesson_5 = make_lesson(
    "lesson.b1.forradalom.05",
    "A Függetlenségi Nyilatkozat és a világosi fegyverletétel (1849)",
    "Történelmi ok-okozati és beavatkozási viszonyok (beavatkozás következtében, túlerő miatt)",
    "Összegezzük az 1849. április 14-i debreceni Függetlenségi Nyilatkozatot, Kossuth kormányzóságát, a cári intervenciót és az 1849. augusztus 13-i világosi fegyverletételt.",
    ["Megérteni az 1849-es Függetlenségi Nyilatkozat jelentőségét és a trónfosztást", "Használni a történelmi kényszert és ok-okozati láncolatokat kifejező szerkezeteket", "Ismerni a cári intervenció és a világosi fegyverletétel történeti hátterét"],
    "story.b1.forradalom.05",
    "voc.b1.forradalom.05",
    "gr.b1.forradalom.05",
    "ex.b1.forradalom.05",
    [e["id"] for e in exs_5]
)
write_json(LESSONS_DIR / "lesson.b1.forradalom.05.json", lesson_5)


# ==========================================
# CONSOLIDATION LESSON: b1-forradalom-consolidation
# ==========================================
cons_exs = [
    {"id": "ex.b1.forradalom.cons.01", "type": "multiple-choice", "lesson": "lesson.b1.forradalom.consolidation", "teaches": ["1848-marcius-15"], "prompt": "Melyik napon tört ki a forradalom Pesten a márciusi ifjak vezetésével?", "options": ["1848. március 15-én", "1848. április 11-én", "1849. május 21-én", "1848. szeptember 29-én"], "correctIndex": 0, "explanation": "1848. március 15. a nemzeti szabadság ünnepe."},
    {"id": "ex.b1.forradalom.cons.02", "type": "fill-blank", "lesson": "lesson.b1.forradalom.consolidation", "teaches": ["marciusi-ifjak"], "prompt": "A pesti forradalmat a *márciusi ifjak* (Petőfi, Jókai, Vasvári) indították el.", "sentence": "A pesti forradalmat a *márciusi ifjak* (Petőfi, Jókai, Vasvári) indították el.", "target": "márciusi ifjak"},
    {"id": "ex.b1.forradalom.cons.03", "type": "multiple-choice", "lesson": "lesson.b1.forradalom.consolidation", "teaches": ["aprilisi-torvenyek-datum"], "prompt": "Mikor szentesítette a király a polgári átalakulást hozó áprilisi törvényeket?", "options": ["1848. április 11-én", "1848. március 15-én", "1849. április 14-én", "1849. augusztus 13-án"], "correctIndex": 0, "explanation": "Az áprilisi törvények születésnapja 1848. április 11."},
    {"id": "ex.b1.forradalom.cons.04", "type": "fill-blank", "lesson": "lesson.b1.forradalom.consolidation", "teaches": ["Batthyany-Lajos"], "prompt": "Magyarország első független felelős miniszterelnöke gróf *Batthyány Lajos* volt.", "sentence": "Magyarország első független felelős miniszterelnöke gróf *Batthyány Lajos* volt.", "target": "Batthyány Lajos"},
    {"id": "ex.b1.forradalom.cons.05", "type": "sentence-builder", "lesson": "lesson.b1.forradalom.consolidation", "teaches": ["jobbagyfelszabaditas", "kozteherviszeles"], "prompt": "Rakd össze a mondatot!", "chips": ["Az", "áprilisi", "törvények", "eltörölték", "a", "feudális", "rendszert."], "target": "Az áprilisi törvények eltörölték a feudális rendszert.", "english": "The April Laws abolished the feudal system."},
    {"id": "ex.b1.forradalom.cons.06", "type": "multiple-choice", "lesson": "lesson.b1.forradalom.consolidation", "teaches": ["pakozdi-csata"], "prompt": "Melyik csatában verték vissza Jellasics bán seregét 1848. szeptember 29-én?", "options": ["A pákozdi csatában", "Az isaszegi csatában", "A világosi csatában", "A debreceni csatában"], "correctIndex": 0, "explanation": "Pákozdnál verte vissza a honvédség a horvát bán támadását."},
    {"id": "ex.b1.forradalom.cons.07", "type": "fill-blank", "lesson": "lesson.b1.forradalom.consolidation", "teaches": ["toborzas"], "prompt": "Kossuth Lajos híres *toborzó* körútja fegyverbe hívta az Alföld lakosságát.", "sentence": "Kossuth Lajos híres *toborzó* körútja fegyverbe hívta az Alföld lakosságát.", "target": "toborzó"},
    {"id": "ex.b1.forradalom.cons.08", "type": "sentence-builder", "lesson": "lesson.b1.forradalom.consolidation", "teaches": ["visszaver", "honvedek"], "prompt": "Alkoss szabályos mondatot!", "chips": ["A", "magyar", "honvédek", "visszaverték", "a", "támadó", "sereget."], "target": "A magyar honvédek visszaverték a támadó sereget.", "english": "The Hungarian soldiers repelled the attacking army."},
    {"id": "ex.b1.forradalom.cons.09", "type": "multiple-choice", "lesson": "lesson.b1.forradalom.consolidation", "teaches": ["tavaszi-hadjarat-fovezer"], "prompt": "Ki volt a dicsőséges 1849-es tavaszi hadjárat főparancsnoka?", "options": ["Görgei Artúr tábornok", "Klapka György", "Batthyány Lajos", "Móga János"], "correctIndex": 0, "explanation": "Görgei Artúr vezette a tavaszi hadjáratot."},
    {"id": "ex.b1.forradalom.cons.10", "type": "fill-blank", "lesson": "lesson.b1.forradalom.consolidation", "teaches": ["Buda-bevétele"], "prompt": "1849. május 21-én a honvédség visszafoglalta *Buda* várát.", "sentence": "1849. május 21-én a honvédség visszafoglalta *Buda* várát.", "target": "Buda"},
    {"id": "ex.b1.forradalom.cons.11", "type": "sentence-builder", "lesson": "lesson.b1.forradalom.consolidation", "teaches": ["Honvedelem-Napja", "majus-21"], "prompt": "Rakd össze az ünnepre vonatkozó mondatot!", "chips": ["Május", "21-e", "a", "Magyar", "Honvédelem", "Napja."], "target": "Május 21-e a Magyar Honvédelem Napja.", "english": "May 21 is the Day of Hungarian National Defence."},
    {"id": "ex.b1.forradalom.cons.12", "type": "multiple-choice", "lesson": "lesson.b1.forradalom.consolidation", "teaches": ["Fuggetlensegi-Nyilatkozat-1849"], "prompt": "Melyik napon mondta ki Debrecenben az országgyűlés a Habsburg-ház trónfosztását?", "options": ["1849. április 14-én", "1848. március 15-én", "1848. április 11-én", "1849. augusztus 13-án"], "correctIndex": 0, "explanation": "1849. április 14-én fogadták el a Függetlenségi Nyilatkozatot a debreceni Nagytemplomban."},
    {"id": "ex.b1.forradalom.cons.13", "type": "fill-blank", "lesson": "lesson.b1.forradalom.consolidation", "teaches": ["kormanyzo-elnok"], "prompt": "1849-ben Kossuth Lajost az ország *kormányzó-elnökévé* választották.", "sentence": "1849-ben Kossuth Lajost az ország *kormányzó-elnökévé* választották.", "target": "kormányzó-elnökévé"},
    {"id": "ex.b1.forradalom.cons.14", "type": "sentence-builder", "lesson": "lesson.b1.forradalom.consolidation", "teaches": ["beavatkozas", "orosz-car"], "prompt": "Rakd össze az összefüggést kifejező mondatot!", "chips": ["Az", "orosz", "cári", "beavatkozás", "eldöntötte", "a", "háborút."], "target": "Az orosz cári beavatkozás eldöntötte a háborút.", "english": "The Russian tsarist intervention decided the war."},
    {"id": "ex.b1.forradalom.cons.15", "type": "multiple-choice", "lesson": "lesson.b1.forradalom.consolidation", "teaches": ["vilagosi-fegyverletetel"], "prompt": "Mikor tette le a fegyvert Görgei Artúr Világosnál a cári csapatok előtt?", "options": ["1849. augusztus 13-án", "1849. október 6-án", "1848. szeptember 29-én", "1849. május 21-én"], "correctIndex": 0, "explanation": "A világosi fegyverletétel 1849. augusztus 13-án történt."},
    {"id": "ex.b1.forradalom.cons.16", "type": "fill-blank", "lesson": "lesson.b1.forradalom.consolidation", "teaches": ["tulero"], "prompt": "A magyar honvédség a kétszeres osztrák és orosz *túlerővel* szemben kényszerült meghátrálni.", "sentence": "A magyar honvédség a kétszeres osztrák és orosz *túlerővel* szemben kényszerült meghátrálni.", "target": "túlerővel"},
    {"id": "ex.b1.forradalom.cons.17", "type": "sentence-builder", "lesson": "lesson.b1.forradalom.consolidation", "teaches": ["fegyverletetel", "Vilagos"], "prompt": "Alkoss történelmi mondatot!", "chips": ["1849.", "augusztus", "13-án", "Világosnál", "letették", "a", "fegyvert."], "target": "1849. augusztus 13-án Világosnál letették a fegyvert.", "english": "On August 13, 1849, they laid down arms at Világos."},
    {"id": "ex.b1.forradalom.cons.18", "type": "multiple-choice", "lesson": "lesson.b1.forradalom.consolidation", "teaches": ["verontas-nelkuliseg"], "prompt": "Milyen jelzővel illeti a történetírás az 1848. március 15-i pesti forradalmat?", "options": ["Békés és vérontás nélküli forradalom", "Véres polgárháború", "Katonai puccs", "Idegen megszállás"], "correctIndex": 0, "explanation": "A pesti forradalom békés és vérontás nélküli volt."},
    {"id": "ex.b1.forradalom.cons.19", "type": "fill-blank", "lesson": "lesson.b1.forradalom.consolidation", "teaches": ["Nemzeti-dal"], "prompt": "Petőfi Sándor a *Nemzeti dalt* szavalta el a forradalom napján.", "sentence": "Petőfi Sándor a *Nemzeti dalt* szavalta el a forradalom napján.", "target": "Nemzeti dalt"},
    {"id": "ex.b1.forradalom.cons.20", "type": "multiple-choice", "lesson": "lesson.b1.forradalom.consolidation", "teaches": ["1848-orokseg"], "prompt": "Miért 1848–49 a modern magyar nemzet legszentebb történelmi alapköve?", "options": ["Mert megteremtette a polgári szabadságot, a jobbágyfelszabadítást és az alkotmányosságot", "Mert új királyt koronáztak", "Mert gyarmatokat szerzett az országnak", "Mert bevezette a latint"], "correctIndex": 0, "explanation": "1848 teremtette meg a modern polgári Magyarországot és a nemzeti összefogást."}
]
write_json(EXERCISES_DIR / "ex.b1.forradalom.consolidation.json", make_exercise_group("ex.b1.forradalom.consolidation", "Az 1848–49-es forradalom és szabadságharc összefoglaló gyakorlatok", "Átfogó teszt 1848–49 eseményeiről, csatáiról, vezetőiről és nyelvtani szerkezeteiről.", cons_exs))

cons_lesson = {
    "id": "lesson.b1.forradalom.consolidation",
    "title": "The 1848–49 Revolution: Unit 16 Consolidation",
    "level": "B1",
    "track": "citizenship",
    "estimatedMinutes": 25,
    "prerequisites": [
        "lesson.b1.forradalom.01",
        "lesson.b1.forradalom.02",
        "lesson.b1.forradalom.03",
        "lesson.b1.forradalom.04",
        "lesson.b1.forradalom.05"
    ],
    "grammar": ["Unit review"],
    "vocabulary": ["Unit review"],
    "culturalContext": "Magyar történelem összefoglalás (Honosítási vizsgafelkészítő)",
    "sections": [
        {
            "type": "intro",
            "title": "Unit 16 Consolidation: The 1848–49 Revolution and War of Independence",
            "body": "Ebben az összefoglaló leckében áttekintjük az 1848. március 15-i forradalmat, az április 11-i áprilisi törvényeket és a Batthyány-kormányt, a pákozdi önvédelmi győzelmet, az 1849-es dicsőséges tavaszi hadjáratot (Buda május 21-i bevétele), a debreceni Függetlenségi Nyilatkozatot és az 1849. augusztus 13-i világosi fegyverletételt."
        },
        {
            "type": "goal",
            "title": "Consolidation Goals",
            "items": [
                "Az 1848–49-es kulcsfontosságú dátumok (március 15., április 11., szeptember 29., május 21., augusztus 13.) biztos ismerete",
                "Forradalmi, alkotmányos és hadtörténeti szerkezetek pontos alkalmazása",
                "A magyar polgári államiság és honvédelem születésének (Petőfi, Kossuth, Batthyány, Görgei) megértése"
            ]
        },
        {
            "type": "exercise-group",
            "title": "Comprehensive Unit 16 Practice",
            "ref": "ex.b1.forradalom.consolidation",
            "exerciseRefs": [e["id"] for e in cons_exs]
        },
        {
            "type": "checklist",
            "items": [
                "Tudom, mikor volt a pesti forradalom (1848. március 15.) és mik voltak a 12 pont és a Nemzeti dal",
                "Ismerem az áprilisi törvényeket (1848. április 11.) és Batthyány Lajos kormányát",
                "Tudom, mi történt Pákozdnál (1848. szeptember 29.) és Budán (1849. május 21., Honvédelem Napja)",
                "Ismerem a Függetlenségi Nyilatkozatot (1849. április 14., Debrecen) és a világosi fegyverletételt"
            ]
        }
    ]
}
write_json(LESSONS_DIR / "lesson.b1.forradalom.consolidation.json", cons_lesson)

print("Unit 16 (b1-forradalom) complete!")
