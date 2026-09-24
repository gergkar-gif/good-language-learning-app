# -*- coding: utf-8 -*-
"""
Generator for Citizenship Units 22, 23, 24:
- Unit 22: b1-horthykorszak (The Interwar Years 1920–1939)
- Unit 23: b1-masodikvh (World War II in Hungary 1938–1945)
- Unit 24: b1-rakosikorszak (The Communist Takeover & Rákosi Era 1945–1956)
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

# ==============================================================================
# UNIT 22: THE INTERWAR YEARS (b1-horthykorszak)
# ==============================================================================

# Lesson 1: A király nélküli királyság és Horthy kormányzóvá választása (1920)
story_22_1 = make_story(
    "story.b1.horthykorszak.01",
    "A király nélküli királyság és a kormányzóválasztás (1920)",
    "1920. március 1-jén a Nemzetgyűlés Magyarország államformáját királyságként állította vissza, de ideiglenes államfőként Horthy Miklóst kormányzóvá választotta.",
    "Országház és Budai Vár",
    ["Államfői tisztségeket és jogköröket kifejező igék (megválaszt vmivé, betölti a tisztséget, gyakorolja a jogkört)", "Restoration of kingdom, regency of Miklós Horthy, and head of state powers"],
    ["kormányzó", "királyság", "király nélküli királyság", "államfő", "Nemzetgyűlés"],
    [
        "1920 elején a forradalmak és a megszállás után újjáalakult magyar parlamentnek döntenie kellett az államformáról. A képviselők elvetették a köztársaságot, és a történelmi királyság fenntartása mellett döntöttek.",
        "Mivel az antant hatalmak határozottan tiltották a Habsburgok visszatérését, az uralkodói trón üresen maradt. E sajátos helyzetben – 'királyság király nélkül' – 1920. március 1-jén a Nemzetgyűlés Horthy Miklóst választotta meg Magyarország kormányzójává (királyhelyettesévé).",
        "Horthy a Budai Várba költözött, és államfőként széles jogkörökkel rendelkezett: ő nevezte ki a miniszterelnököt, feloszlathatta az Országgyűlést, és a hadsereg legfelsőbb parancsnoka volt."
    ],
    [
        {"lemma": "kormányzó", "pos": "noun", "cefr": "B1", "gloss": "Regent (head of state of the Kingdom of Hungary)"},
        {"lemma": "államforma", "pos": "noun", "cefr": "B1", "gloss": "form of state / government (monarchy/republic)"},
        {"lemma": "király nélküli királyság", "pos": "noun", "cefr": "B1", "gloss": "kingdom without a king (regency period)"},
        {"lemma": "jogkör", "pos": "noun", "cefr": "B1", "gloss": "sphere of authority, official powers"},
        {"lemma": "legfelsőbb parancsnok", "pos": "noun", "cefr": "B1", "gloss": "supreme commander"}
    ],
    [
        {
            "question": "Milyen tisztségre választotta meg a Nemzetgyűlés Horthy Miklóst 1920. március 1-jén?",
            "options": ["Magyarország kormányzójává (államfővé)", "Magyar királlyá", "Köztársasági elnökké", "Főpolgármesterré"],
            "correctIndex": 0,
            "explanation": "Horthy Miklóst 1920. március 1-jén választották kormányzóvá."
        }
    ]
)
write_json(STORIES_DIR / "story.b1.horthykorszak.01.json", story_22_1)

voc_22_1 = {
    "id": "voc.b1.horthykorszak.01",
    "title": "A kormányzói tisztség és államforma szókincse",
    "description": "Kormányzó, államforma, király nélküli királyság, jogkör és Nemzetgyűlés.",
    "entries": [
        {"lemma": "kormányzó", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "Regent, head of state in Hungary 1920–1944", "examples": [{"hu": "Horthy Miklós huszonnégy évig volt kormányzó.", "en": "Miklós Horthy was regent for twenty-four years."}]}]},
        {"lemma": "államforma", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "constitutional structure of a state", "examples": [{"hu": "Az ország államformája királyság maradt.", "en": "The country's form of government remained a kingdom."}]}]},
        {"lemma": "király nélküli királyság", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "unique interwar status where the throne was vacant", "examples": [{"hu": "Magyarország király nélküli királyságként működött.", "en": "Hungary functioned as a kingdom without a king."}]}]},
        {"lemma": "jogkör", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "legal authority and constitutional competencies", "examples": [{"hu": "A kormányzó széles jogkörrel rendelkezett.", "en": "The regent possessed wide authority."}]}]},
        {"lemma": "legfelsőbb parancsnok", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "commander-in-chief of the armed forces", "examples": [{"hu": "A hadsereg legfelsőbb parancsnoka a kormányzó volt.", "en": "The commander-in-chief of the army was the regent."}]}]}
    ]
}
write_json(VOCAB_DIR / "voc.b1.horthykorszak.01.json", voc_22_1)

gr_22_1 = {
    "id": "gr.b1.horthykorszak.01",
    "title": "Tisztségbe választást és kinevezést kifejező igék vonzatai (megválaszt vmivé, kinevez vmivé)",
    "description": "Forming election, appointment, and state leadership transitions.",
    "rules": [
        {
            "explanation": "A 'megválaszt', 'kinevez', 'jelöl' igék a '-vá/-vé' határozóraggal állnak: 'kormányzóvá választották', 'miniszterelnökké nevezte ki'.",
            "examples": [
                {"spanish": "Horthy Miklóst kormányzóvá választották.", "english": "Miklós Horthy was elected regent."},
                {"spanish": "A kormányzó Bethlen Istvánt miniszterelnökké nevezte ki.", "english": "The regent appointed István Bethlen prime minister."}
            ]
        }
    ]
}
write_json(GRAMMAR_DIR / "gr.b1.horthykorszak.01.json", gr_22_1)

exs_22_1 = [
    {"id": "ex.b1.horthykorszak.01.01", "type": "multiple-choice", "lesson": "lesson.b1.horthykorszak.01", "teaches": ["kormanyzovalasztas-1920"], "prompt": "Mikor választották meg Horthy Miklóst kormányzóvá?", "options": ["1920. március 1-jén", "1914. július 28-án", "1927. január 1-jén", "1938. november 2-án"], "correctIndex": 0, "explanation": "1920. március 1-jén választotta kormányzóvá a Nemzetgyűlés."},
    {"id": "ex.b1.horthykorszak.01.02", "type": "fill-blank", "lesson": "lesson.b1.horthykorszak.01", "teaches": ["kormanyzova"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A képviselők Horthy Miklóst *kormányzóvá* választották.", "target": "kormányzóvá"},
    {"id": "ex.b1.horthykorszak.01.03", "type": "sentence-builder", "lesson": "lesson.b1.horthykorszak.01", "teaches": ["allamforma", "kiralysag"], "prompt": "Rakd össze a mondatot!", "chips": ["Magyarország", "hivatalos", "államformája", "a", "királyság", "maradt."], "target": "Magyarország hivatalos államformája a királyság maradt.", "english": "Hungary's official form of state remained the kingdom."},
    {"id": "ex.b1.horthykorszak.01.04", "type": "multiple-choice", "lesson": "lesson.b1.horthykorszak.01", "teaches": ["kiraly-nelkuli-kiralysag"], "prompt": "Miért hívták a két háború közötti Magyarországot 'király nélküli királyságnak'?", "options": ["Mert az államforma királyság volt, de az államfői tisztséget a kormányzó töltötte be", "Mert elfelejtették megkoronázni a királyt", "Mert a király külföldön nyaralt", "Mert a köztársaságot eltitkolták"], "correctIndex": 0, "explanation": "A trón betöltetlen volt, Horthy kormányzóként állt az állam élén."},
    {"id": "ex.b1.horthykorszak.01.05", "type": "fill-blank", "lesson": "lesson.b1.horthykorszak.01", "teaches": ["jogkorrel"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A kormányzó széles államfői *jogkörrel* rendelkezett.", "target": "jogkörrel"},
    {"id": "ex.b1.horthykorszak.01.06", "type": "sentence-builder", "lesson": "lesson.b1.horthykorszak.01", "teaches": ["hadsereg", "parancsnok"], "prompt": "Alkoss szabályos összetett mondatot!", "chips": ["A", "kormányzó", "volt", "a", "hadsereg", "legfelsőbb", "parancsnoka."], "target": "A kormányzó volt a hadsereg legfelsőbb parancsnoka.", "english": "The regent was the supreme commander of the army."},
    {"id": "ex.b1.horthykorszak.01.07", "type": "multiple-choice", "lesson": "lesson.b1.horthykorszak.01", "teaches": ["Budai-Var-kormanyzo"], "prompt": "Hol volt Horthy Miklós kormányzó hivatalos rezidenciája?", "options": ["A Budai Várban (Királyi Palotában)", "A Parlamentben", "A Nemzeti Múzeumban", "Gödöllőn"], "correctIndex": 0, "explanation": "Horthy hivatala és rezidenciája a Budai Várban volt."},
    {"id": "ex.b1.horthykorszak.01.08", "type": "fill-blank", "lesson": "lesson.b1.horthykorszak.01", "teaches": ["allamfo"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A kormányzó Magyarország törvényes *államfője* volt.", "target": "államfője"}
]
write_json(EXERCISES_DIR / "ex.b1.horthykorszak.01.json", make_exercise_group("ex.b1.horthykorszak.01", "Kormányzóválasztás gyakorlatok", "Gyakorlatok az 1920-as kormányzóválasztásról, a király nélküli királyságról és a kinevezést kifejező vonzatokról.", exs_22_1))

lesson_22_1 = make_lesson(
    "lesson.b1.horthykorszak.01",
    "A király nélküli királyság és a kormányzóválasztás (1920)",
    "Tisztségbe választást kifejező szerkezetek (kormányzóvá választ, kinevez)",
    "Ismerjük meg az 1920. március 1-jei kormányzóválasztást, Horthy Miklós szerepét és a király nélküli királyság intézményét.",
    ["Tudni az 1920. március 1-i kormányzóválasztás dátumát", "Megérteni a 'király nélküli királyság' alkotmányos fogalmát", "Használni a tisztségekbe választást és kinevezést kifejező igéket"],
    "story.b1.horthykorszak.01",
    "voc.b1.horthykorszak.01",
    "gr.b1.horthykorszak.01",
    "ex.b1.horthykorszak.01",
    [e["id"] for e in exs_22_1]
)
write_json(LESSONS_DIR / "lesson.b1.horthykorszak.01.json", lesson_22_1)


# Lesson 2: Bethlen István konszolidációja (1921–1931) és a Pengő
story_22_2 = make_story(
    "story.b1.horthykorszak.02",
    "Bethlen István konszolidációja és az új valuta, a Pengő (1927)",
    "Gróf Bethlen István tízéves miniszterelnöksége (1921–1931) alatt helyreállította a politikai stabilitást, Népszövetségi kölcsönt szerzett, és 1927-ben bevezette a stabil értékálló Pengőt.",
    "Magyar Nemzeti Bank és Parlament, Budapest",
    ["Gazdasági stabilitást és pénzügyi reformot kifejező szerkezetek (stabilizál, bevezet egy új valutát, helyreállít)", "Political consolidation, League of Nations loan, and introduction of the Pengő"],
    ["konszolidáció", "Bethlen István", "Pengő", "Népszövetségi kölcsön", "értékállóság"],
    [
        "1921-ben gróf Bethlen István lett a miniszterelnök, aki a 'konszolidáció' (megszilárdítás) politikáját hirdette meg. Célja a politikai béke és a gazdasági talpra állás megteremtése volt a háború és Trianon romjain.",
        "Bethlen megkötötte a Bethlen–Peyer paktumot a szociáldemokratákkal, megerősítette a parlamenti többséget, és 1924-ben felvette a Népszövetségi kölcsönt. Megalapította a Magyar Nemzeti Bankot az infláció megfékezésére.",
        "1927. január 1-jén bevezették az új, aranyalapú magyar valutát, a Pengőt, amely hamarosan Európa egyik legstabilabb és legmegbízhatóbb pénzévé vált, megalapozva az 1920-as évek prosperitását."
    ],
    [
        {"lemma": "konszolidáció", "pos": "noun", "cefr": "B1", "gloss": "consolidation, political & economic stabilization"},
        {"lemma": "Pengő", "pos": "noun", "cefr": "B1", "gloss": "Pengő (Hungarian currency introduced in 1927)"},
        {"lemma": "Népszövetség", "pos": "noun", "cefr": "B1", "gloss": "League of Nations"},
        {"lemma": "értékálló", "pos": "adj", "cefr": "B1", "gloss": "stable in value, inflation-resistant"},
        {"lemma": "talpra állás", "pos": "noun", "cefr": "B1", "gloss": "recovery, getting back on one's feet"}
    ],
    [
        {
            "question": "Melyik évben vezették be Magyarországon a híres stabil valutát, a Pengőt?",
            "options": ["1927-ben", "1920-ban", "1938-ban", "1946-ban"],
            "correctIndex": 0,
            "explanation": "A Pengőt 1927. január 1-jén vezették be a korona helyett."
        }
    ]
)
write_json(STORIES_DIR / "story.b1.horthykorszak.02.json", story_22_2)

voc_22_2 = {
    "id": "voc.b1.horthykorszak.02",
    "title": "A konszolidáció és pénzügyek szókincse",
    "description": "Konszolidáció, Pengő, Bethlen István, Népszövetség és értékállóság.",
    "entries": [
        {"lemma": "konszolidáció", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "systematic stabilization of state and economy", "examples": [{"hu": "Bethlen István sikeres konszolidációt hajtott végre.", "en": "István Bethlen carried out a successful consolidation."}]}]},
        {"lemma": "Pengő", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "stable gold-backed Hungarian currency 1927–1946", "examples": [{"hu": "A pengő a stabilitás jelképe lett.", "en": "The pengő became the symbol of stability."}]}]},
        {"lemma": "Népszövetség", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "League of Nations (interwar international body)", "examples": [{"hu": "A Népszövetség kölcsönt nyújtott Magyarországnak.", "en": "The League of Nations granted a loan to Hungary."}]}]},
        {"lemma": "értékálló", "pos": "adj", "cefr": "B1", "definitions": [{"meaning": "retaining value without rapid inflation", "examples": [{"hu": "Az új pénz értékálló és megbízható volt.", "en": "The new currency was stable in value and reliable."}]}]},
        {"lemma": "talpra állás", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "economic and social recovery", "examples": [{"hu": "Az ország gazdasági talpra állása megkezdődött.", "en": "The economic recovery of the country began."}]}]}
    ]
}
write_json(VOCAB_DIR / "voc.b1.horthykorszak.02.json", voc_22_2)

gr_22_2 = {
    "id": "gr.b1.horthykorszak.02",
    "title": "Időbeli tartamot és folyamatosságot kifejező határozók (alatt, folyamán, során, tíz éven át)",
    "description": "Expressing continuous governance periods, economic reforms over time, and durations.",
    "rules": [
        {
            "explanation": "Kormányzási korszakok és tartós reformok leírására az 'alatt', 'során', 'folyamán' névutókat és az időtartam-határozókat (pl. 'tíz éven át') használjuk.",
            "examples": [
                {"spanish": "Bethlen István tízéves miniszterelnöksége alatt stabilizálódott az ország.", "english": "During István Bethlen's ten-year premiership, the country stabilized."},
                {"spanish": "A konszolidáció során új pénzt vezettek be.", "english": "In the course of the consolidation, a new currency was introduced."}
            ]
        }
    ]
}
write_json(GRAMMAR_DIR / "gr.b1.horthykorszak.02.json", gr_22_2)

exs_22_2 = [
    {"id": "ex.b1.horthykorszak.02.01", "type": "multiple-choice", "lesson": "lesson.b1.horthykorszak.02", "teaches": ["Bethlen-Istvan-konszolidacio"], "prompt": "Ki volt Magyarország miniszterelnöke az 1921–1931 közötti konszolidációs évtizedben?", "options": ["Gróf Bethlen István", "Károlyi Mihály", "Kun Béla", "Tisza István"], "correctIndex": 0, "explanation": "Gróf Bethlen István vezette a konszolidációt 1921 és 1931 között."},
    {"id": "ex.b1.horthykorszak.02.02", "type": "fill-blank", "lesson": "lesson.b1.horthykorszak.02", "teaches": ["konszolidaciot"], "prompt": "Egészítsd ki a mondatot!", "sentence": "Bethlen István sikeres politikai *konszolidációt* hajtott végre.", "target": "konszolidációt"},
    {"id": "ex.b1.horthykorszak.02.03", "type": "sentence-builder", "lesson": "lesson.b1.horthykorszak.02", "teaches": ["Pengo-1927", "bevezet"], "prompt": "Rakd össze a pénzügyi mondatot!", "chips": ["1927-ben", "bevezették", "az", "értékálló", "új", "magyar", "pénzt,", "a", "Pengőt."], "target": "1927-ben bevezették az értékálló új magyar pénzt, a Pengőt.", "english": "In 1927, they introduced the stable new Hungarian currency, the Pengő."},
    {"id": "ex.b1.horthykorszak.02.04", "type": "multiple-choice", "lesson": "lesson.b1.horthykorszak.02", "teaches": ["Nepszovetsegi-kolcson"], "prompt": "Mely nemzetközi szervezet kölcsöne segítette a gazdasági talpra állást 1924-ben?", "options": ["A Népszövetség kölcsöne", "A Világbank", "A Nemzetközi Valutaalap", "Az Európai Unió"], "correctIndex": 0, "explanation": "A Népszövetség (League of Nations) nyújtott újjáépítési kölcsönt."},
    {"id": "ex.b1.horthykorszak.02.05", "type": "fill-blank", "lesson": "lesson.b1.horthykorszak.02", "teaches": ["ertekallo"], "prompt": "Egészítsd ki a mondatot a megfelelő melléknévvel!", "sentence": "A pengő egy rendkívül *értékálló* valuta volt.", "target": "értékálló"},
    {"id": "ex.b1.horthykorszak.02.06", "type": "sentence-builder", "lesson": "lesson.b1.horthykorszak.02", "teaches": ["MNB-alapitas", "inflacio"], "prompt": "Alkoss szabályos mondatot!", "chips": ["Megalapították", "a", "Magyar", "Nemzeti", "Bankot", "az", "infláció", "ellen."], "target": "Megalapították a Magyar Nemzeti Bankot az infláció ellen.", "english": "They founded the Hungarian National Bank against inflation."},
    {"id": "ex.b1.horthykorszak.02.07", "type": "multiple-choice", "lesson": "lesson.b1.horthykorszak.02", "teaches": ["Bethlen-Peyer-paktum"], "prompt": "Kikkel kötött egyezséget Bethlen István a munkásság integrálására?", "options": ["A Szociáldemokrata Párttal (Bethlen–Peyer paktum)", "A kommunistákkal", "A royalistákkal", "A szomszédos országokkal"], "correctIndex": 0, "explanation": "A Bethlen–Peyer paktum törvényes működést biztosított a szociáldemokratáknak."},
    {"id": "ex.b1.horthykorszak.02.08", "type": "fill-blank", "lesson": "lesson.b1.horthykorszak.02", "teaches": ["Pengo"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A koronát az új *Pengő* váltotta fel 1927-ben.", "target": "Pengő"}
]
write_json(EXERCISES_DIR / "ex.b1.horthykorszak.02.json", make_exercise_group("ex.b1.horthykorszak.02", "A konszolidáció és Pengő gyakorlatok", "Gyakorlatok Bethlen Istvánról, a konszolidációról, a Pengőről és az időtartamot kifejező szerkezetekről.", exs_22_2))

lesson_22_2 = make_lesson(
    "lesson.b1.horthykorszak.02",
    "Bethlen István konszolidációja és az új valuta, a Pengő (1927)",
    "Időbeli tartamot és stabilitást kifejező szerkezetek (alatt, során, értékálló)",
    "Ismerjük meg Bethlen István konszolidációs politikáját, a gazdaság talpra állását és az 1927-es Pengő bevezetését.",
    ["Tudni Bethlen István miniszterelnökségének (1921–1931) főbb eredményeit", "Ismerni az 1927-es Pengő bevezetését és a Népszövetségi kölcsönt", "Használni az időbeli folyamatosságot és tartamot leíró határozókat"],
    "story.b1.horthykorszak.02",
    "voc.b1.horthykorszak.02",
    "gr.b1.horthykorszak.02",
    "ex.b1.horthykorszak.02",
    [e["id"] for e in exs_22_2]
)
write_json(LESSONS_DIR / "lesson.b1.horthykorszak.02.json", lesson_22_2)


# Lesson 3: Klebelsberg Kuno kultúrpolitikája és a népiskolák
story_22_3 = make_story(
    "story.b1.horthykorszak.03",
    "Klebelsberg Kuno kultúrpolitikája és a népiskola-program",
    "Gróf Klebelsberg Kuno vallás- és közoktatásügyi miniszter szerint a trianoni veszteségeket a szellem és a kultúra erejével kell ellensúlyozni: ötezer népiskolai tantermet épített és felvirágoztatta a szegedi egyetemet.",
    "Szegedi Tudományegyetem és alföldi tanyavilág",
    ["Oktatásfejlesztést, művelődést és építkezést kifejező szerkezetek (felépít, megalapoz, fellendít, ellensúlyoz)", "Educational reform, 5000 classrooms, cultural superiority, and Szeged University"],
    ["Klebelsberg Kuno", "népiskola", "kultúrfölény", "Szegedi Egyetem", "analfabetizmus"],
    [
        "Gróf Klebelsberg Kuno vallás- és közoktatásügyi miniszter a 'magyar kultúrfölény' és a neonacionalizmus eszméjét hirdette meg. Meggyőződése volt, hogy a nemzetet a magas színvonalú oktatás, a tudomány és a kultúra fogja újra naggyá tenni.",
        "Hatalmas népiskola-építési programot valósított meg: több mint 5000 modern tantermet és tanítói lakást építtetett, különösen az elhanyagolt alföldi tanyavilágban. Ezzel sikerült drasztikusan visszaszorítani az analfabetizmust.",
        "Kolozsvárról Szegedre telepítette a Tudományegyetemet, létrehozta a Collegium Hungaricumok külföldi hálózatát Bécsben, Berlinben és Rómában a legtehetségesebb magyar tudósok és diákok számára, támogatva olyan nagyságok kutatásait, mint Szent-Györgyi Albert."
    ],
    [
        {"lemma": "népiskola", "pos": "noun", "cefr": "B1", "gloss": "elementary school, folk school"},
        {"lemma": "analfabetizmus", "pos": "noun", "cefr": "B1", "gloss": "illiteracy"},
        {"lemma": "kultúrfölény", "pos": "noun", "cefr": "B1", "gloss": "cultural superiority / excellence doctrine"},
        {"lemma": "tanterem", "pos": "noun", "cefr": "B1", "gloss": "classroom"},
        {"lemma": "tudományos kutatás", "pos": "noun", "cefr": "B1", "gloss": "scientific research"}
    ],
    [
        {
            "question": "Ki volt a két háború közötti Magyarország legnagyobb hatású kultuszminisztere, aki ötezer tantermet építtetett?",
            "options": ["Gróf Klebelsberg Kuno", "Deák Ferenc", "Kossuth Lajos", "Széchenyi István"],
            "correctIndex": 0,
            "explanation": "Gróf Klebelsberg Kuno irányította az oktatási és kulturális felvirágzást."
        }
    ]
)
write_json(STORIES_DIR / "story.b1.horthykorszak.03.json", story_22_3)

voc_22_3 = {
    "id": "voc.b1.horthykorszak.03",
    "title": "A kultúrpolitika és oktatás szókincse",
    "description": "Klebelsberg Kuno, népiskola, analfabetizmus, tanterem és kultúrfölény.",
    "entries": [
        {"lemma": "népiskola", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "elementary school built for common people", "examples": [{"hu": "Klebelsberg országszerte népiskolákat épített.", "en": "Klebelsberg built elementary schools nationwide."}]}]},
        {"lemma": "analfabetizmus", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "inability to read and write", "examples": [{"hu": "A népiskolákkal felszámolták az analfabetizmust.", "en": "With folk schools they eliminated illiteracy."}]}]},
        {"lemma": "tanterem", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "school classroom", "examples": [{"hu": "Több mint ötezer új tanterem épült.", "en": "More than five thousand new classrooms were built."}]}]},
        {"lemma": "kultúrfölény", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "excellence in culture and science as a peaceful path to revival", "examples": [{"hu": "A kultúrfölény eszméje az oktatásra épült.", "en": "The concept of cultural excellence was built on education."}]}]},
        {"lemma": "tudományos kutatás", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "academic and scientific research", "examples": [{"hu": "Támogatta az egyetemek tudományos kutatásait.", "en": "He supported the scientific research of universities."}]}]}
    ]
}
write_json(VOCAB_DIR / "voc.b1.horthykorszak.03.json", voc_22_3)

gr_22_3 = {
    "id": "gr.b1.horthykorszak.03",
    "title": "Célt és eszközöket kifejező szerkezetek (azzal a céllal, hogy; révén, segítségével)",
    "description": "Expressing purpose, educational missions, and instruments of cultural progress.",
    "rules": [
        {
            "explanation": "Célhatározói mellékmondatokban és szerkezetekben: 'azzal a céllal, hogy...', 'azért, hogy...', 'eszközök révén / segítségével'.",
            "examples": [
                {"spanish": "Klebelsberg iskolákat épített azzal a céllal, hogy művelt nemzetet teremtsen.", "english": "Klebelsberg built schools with the goal of creating an educated nation."},
                {"spanish": "A szegedi egyetem révén Szeged igazi tudományos központtá vált.", "english": "By means of Szeged University, Szeged became a true scientific center."}
            ]
        }
    ]
}
write_json(GRAMMAR_DIR / "gr.b1.horthykorszak.03.json", gr_22_3)

exs_22_3 = [
    {"id": "ex.b1.horthykorszak.03.01", "type": "multiple-choice", "lesson": "lesson.b1.horthykorszak.03", "teaches": ["Klebelsberg-Kuno-miniszter"], "prompt": "Melyik minisztériumot vezette gróf Klebelsberg Kuno az 1920-as években?", "options": ["A Vallás- és Közoktatásügyi Minisztériumot", "A Pénzügyminisztériumot", "A Hadügyminisztériumot", "A Földművelésügyi Minisztériumot"], "correctIndex": 0, "explanation": "Klebelsberg vallás- és közoktatásügyi miniszterként tevékenykedett."},
    {"id": "ex.b1.horthykorszak.03.02", "type": "fill-blank", "lesson": "lesson.b1.horthykorszak.03", "teaches": ["nepiskolat"], "prompt": "Egészítsd ki a mondatot!", "sentence": "Ötezer korszerű *népiskolát* és tantermet adtak át.", "target": "népiskolát"},
    {"id": "ex.b1.horthykorszak.03.03", "type": "sentence-builder", "lesson": "lesson.b1.horthykorszak.03", "teaches": ["analfabetizmus", "visszaszorit"], "prompt": "Rakd össze a célt leíró mondatot!", "chips": ["A", "népiskolai", "program", "sikeresen", "visszaszorította", "az", "analfabetizmust."], "target": "A népiskolai program sikeresen visszaszorította az analfabetizmust.", "english": "The folk school program successfully suppressed illiteracy."},
    {"id": "ex.b1.horthykorszak.03.04", "type": "multiple-choice", "lesson": "lesson.b1.horthykorszak.03", "teaches": ["Szegedi-Egyetem-telepites"], "prompt": "Melyik városba telepítették át a kolozsvári egyetemet Klebelsberg döntése nyomán?", "options": ["Szegedre", "Debrecenbe", "Pécsre", "Győrbe"], "correctIndex": 0, "explanation": "A Szegedi Tudományegyetem ekkor vált az ország egyik vezető egyetemévé."},
    {"id": "ex.b1.horthykorszak.03.05", "type": "fill-blank", "lesson": "lesson.b1.horthykorszak.03", "teaches": ["tantermet"], "prompt": "Egészítsd ki a mondatot!", "sentence": "Több mint 5000 új *tantermet* építettek a tanyavilágban.", "target": "tantermet"},
    {"id": "ex.b1.horthykorszak.03.06", "type": "sentence-builder", "lesson": "lesson.b1.horthykorszak.03", "teaches": ["Collegium-Hungaricum", "kulfold"], "prompt": "Alkoss szabályos összetett mondatot!", "chips": ["Klebelsberg", "létrehozta", "a", "Collegium", "Hungaricumok", "külföldi", "hálózatát."], "target": "Klebelsberg létrehozta a Collegium Hungaricumok külföldi hálózatát.", "english": "Klebelsberg established the foreign network of Collegium Hungaricum institutes."},
    {"id": "ex.b1.horthykorszak.03.07", "type": "multiple-choice", "lesson": "lesson.b1.horthykorszak.03", "teaches": ["kulturfoleny-gondolat"], "prompt": "Mi volt a 'kultúrfölény' gondolatának lényege?", "options": ["Hogy Magyarország a tudomány, az oktatás és a kultúra kimagasló színvonalával szerezze vissza tekintélyét a világban", "Hogy betiltsák a külföldi könyveket", "Hogy bezárják a külföldi egyetemeket", "Hogy mindenki latinul beszéljen"], "correctIndex": 0, "explanation": "A szellemi és oktatási minőség révén kívánta felemelni a nemzetet."},
    {"id": "ex.b1.horthykorszak.03.08", "type": "fill-blank", "lesson": "lesson.b1.horthykorszak.03", "teaches": ["kulturpolitika"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A klebelsbergi *kultúrpolitika* maradandó értéket teremtett.", "target": "kultúrpolitika"}
]
write_json(EXERCISES_DIR / "ex.b1.horthykorszak.03.json", make_exercise_group("ex.b1.horthykorszak.03", "Klebelsberg kultúrpolitikája gyakorlatok", "Gyakorlatok a népiskolákról, Klebelsberg Kunóról, a szegedi egyetemről és a célhatározói szerkezetekről.", exs_22_3))

lesson_22_3 = make_lesson(
    "lesson.b1.horthykorszak.03",
    "Klebelsberg Kuno kultúrpolitikája és a népiskola-program",
    "Célt és eszközöket kifejező szerkezetek (azzal a céllal, révén)",
    "Tekintsük át Klebelsberg Kuno korszakos oktatási reformjait: az 5000 népiskolai tantermet és a szegedi egyetemet.",
    ["Ismerni Klebelsberg Kuno kultuszminiszter történelmi örökségét", "Tudni a népiskolai program (5000 tanterem) és a szegedi egyetem szerepét", "Használni a célt és eszközöket összekapcsoló mondatszerkezeteket"],
    "story.b1.horthykorszak.03",
    "voc.b1.horthykorszak.03",
    "gr.b1.horthykorszak.03",
    "ex.b1.horthykorszak.03",
    [e["id"] for e in exs_22_3]
)
write_json(LESSONS_DIR / "lesson.b1.horthykorszak.03.json", lesson_22_3)


# Lesson 4: A revíziós törekvések és a nemzetközi szövetségek keresése
story_22_4 = make_story(
    "story.b1.horthykorszak.04",
    "A revíziós törekvések és a nemzetközi elszigeteltség feloldása",
    "A Horthy-korszak külpolitikájának legfőbb célja a trianoni határok békés revíziója (felülvizsgálata) volt. Az 1927-es olasz–magyar barátsági szerződés törte meg a Magyarország körüli kisantant gyűrűt.",
    "Róma és Budapest",
    ["Külpolitikai szándékot, követelést és szövetségkötést kifejező szerkezetek (revíziót követel, szövetséget köt, célul tűz ki)", "Revisionism, breaking diplomatic isolation, Italian-Hungarian treaty, and Little Entente"],
    ["revízió", "kisantant", "elszigeteltség", "barátsági szerződés", "igazság"],
    [
        "A két világháború közötti teljes magyar társadalmat és politikát a revízió – a trianoni békeszerződés igazságtalan határainak megváltoztatása – eszméje határozta meg. A jelszó a 'Mindent vissza!' és a 'Nem, nem, soha!' volt.",
        "A szomszédos utódállamok (Csehszlovákia, Románia, Jugoszlávia) létrehozták a 'kisantant' nevű katonai és politikai szövetséget, hogy katonai túlerővel kényszerítsék rá Magyarországra az elszigeteltséget és megakadályozzák a határkiigazításokat.",
        "Bethlen István 1927-ben Rómában aláírta az olasz–magyar örökbarátsági szerződést Benito Mussolinivel. Ezzel Magyarország megtörte a diplomáciai blokádot, de egyúttal megkezdődött a közeledés a revíziót támogató autoriter nagyhatalmakhoz."
    ],
    [
        {"lemma": "revízió", "pos": "noun", "cefr": "B1", "gloss": "revision of borders (reversal of Trianon treaty)"},
        {"lemma": "kisantant", "pos": "noun", "cefr": "B1", "gloss": "Little Entente (alliance of Czechoslovakia, Romania, Yugoslavia)"},
        {"lemma": "elszigeteltség", "pos": "noun", "cefr": "B1", "gloss": "diplomatic isolation"},
        {"lemma": "örökbarátsági szerződés", "pos": "noun", "cefr": "B1", "gloss": "treaty of friendship"},
        {"lemma": "határkiigazítás", "pos": "noun", "cefr": "B1", "gloss": "border readjustment, rectification"}
    ],
    [
        {
            "question": "Hogyan nevezték a trianoni határok megváltoztatására irányuló magyar külpolitikai törekvést?",
            "options": ["Revíziós politikának (revíziónak)", "Passzív ellenállásnak", "Kolonizációnak", "Békemozgalomnak"],
            "correctIndex": 0,
            "explanation": "A revízió a határok békés vagy fegyveres módosításának követelése volt."
        }
    ]
)
write_json(STORIES_DIR / "story.b1.horthykorszak.04.json", story_22_4)

voc_22_4 = {
    "id": "voc.b1.horthykorszak.04",
    "title": "A revízió és külpolitika szókincse",
    "description": "Revízió, kisantant, elszigeteltség, örökbarátsági szerződés és határkiigazítás.",
    "entries": [
        {"lemma": "revízió", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "demanding review and change of unjust Trianon borders", "examples": [{"hu": "A revízió a külpolitika legfőbb célja volt.", "en": "Revision was the primary goal of foreign policy."}]}]},
        {"lemma": "kisantant", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "anti-Hungarian alliance of Czechoslovakia, Romania, and Yugoslavia", "examples": [{"hu": "A kisantant elszigetelte Magyarországot.", "en": "The Little Entente isolated Hungary."}]}]},
        {"lemma": "elszigeteltség", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "state of diplomatic isolation", "examples": [{"hu": "Sikerült megtörni az ország nemzetközi elszigeteltségét.", "en": "They succeeded in breaking the country's international isolation."}]}]},
        {"lemma": "örökbarátsági szerződés", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "bilateral friendship treaty signed with Italy in 1927", "examples": [{"hu": "1927-ben aláírták az olasz–magyar örökbarátsági szerződést.", "en": "In 1927 they signed the Italian-Hungarian friendship treaty."}]}]},
        {"lemma": "határkiigazítás", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "modification of border lines along ethnic boundaries", "examples": [{"hu": "Békés határkiigazítást követeltek.", "en": "They demanded peaceful border adjustment."}]}]}
    ]
}
write_json(VOCAB_DIR / "voc.b1.horthykorszak.04.json", voc_22_4)

gr_22_4 = {
    "id": "gr.b1.horthykorszak.04",
    "title": "Szándékot és törekvést kifejező igék vonzatai (törekszik vmire, célul tűz ki, követel vmit)",
    "description": "Expressing political aspirations, foreign policy goals, and revisionist objectives.",
    "rules": [
        {
            "explanation": "Politikai célok kifejezése: 'törekszik a revízióra', 'célul tűzi ki a határok megváltoztatását', 'követeli az igazságot'.",
            "examples": [
                {"spanish": "A kormányzat a határok békés revíziójára törekedett.", "english": "The government aimed at the peaceful revision of borders."},
                {"spanish": "A szövetség célul tűzte ki Magyarország elszigetelését.", "english": "The alliance set as its goal the isolation of Hungary."}
            ]
        }
    ]
}
write_json(GRAMMAR_DIR / "gr.b1.horthykorszak.04.json", gr_22_4)

exs_22_4 = [
    {"id": "ex.b1.horthykorszak.04.01", "type": "multiple-choice", "lesson": "lesson.b1.horthykorszak.04", "teaches": ["revizio-fogalom"], "prompt": "Mit jelentett a revízió a Horthy-korszak magyar külpolitikájában?", "options": ["A trianoni békediktátum határainak felülvizsgálatát és módosítását", "Új adók kivetését", "A vasutak ellenőrzését", "A király visszahívását"], "correctIndex": 0, "explanation": "A revízió a trianoni határok megváltoztatását jelentette."},
    {"id": "ex.b1.horthykorszak.04.02", "type": "fill-blank", "lesson": "lesson.b1.horthykorszak.04", "teaches": ["reviziora"], "prompt": "Egészítsd ki a mondatot!", "sentence": "Az egész társadalom a békés *revízióra* törekedett.", "target": "revízióra"},
    {"id": "ex.b1.horthykorszak.04.03", "type": "sentence-builder", "lesson": "lesson.b1.horthykorszak.04", "teaches": ["kisantant", "elszigetel"], "prompt": "Rakd össze a diplomáciai helyzetet leíró mondatot!", "chips": ["A", "szomszédos", "kisantant", "államok", "elszigetelték", "Magyarországot."], "target": "A szomszédos kisantant államok elszigetelték Magyarországot.", "english": "The neighboring Little Entente states isolated Hungary."},
    {"id": "ex.b1.horthykorszak.04.04", "type": "multiple-choice", "lesson": "lesson.b1.horthykorszak.04", "teaches": ["olasz-magyar-szerzodes-1927"], "prompt": "Melyik országgal kötött örökbarátsági szerződést Bethlen István 1927-ben a blokád megtörésére?", "options": ["Olaszországgal", "Nagy-Britanniával", "A Szovjetunióval", "Romániával"], "correctIndex": 0, "explanation": "1927-ben Olaszországgal kötöttek barátsági szerződést."},
    {"id": "ex.b1.horthykorszak.04.05", "type": "fill-blank", "lesson": "lesson.b1.horthykorszak.04", "teaches": ["elszigeteltséget"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A szerződéssel sikerült megtörni az *elszigeteltséget*.", "target": "elszigeteltséget"},
    {"id": "ex.b1.horthykorszak.04.06", "type": "sentence-builder", "lesson": "lesson.b1.horthykorszak.04", "teaches": ["celul-tuz-ki", "bekes"], "prompt": "Alkoss szabályos összetett mondatot!", "chips": ["A", "magyar", "diplomácia", "célul", "tűzte", "ki", "a", "békés", "határkiigazítást."], "target": "A magyar diplomácia célul tűzte ki a békés határkiigazítást.", "english": "Hungarian diplomacy set as its goal peaceful border adjustment."},
    {"id": "ex.b1.horthykorszak.04.07", "type": "multiple-choice", "lesson": "lesson.b1.horthykorszak.04", "teaches": ["kisantant-tagjai"], "prompt": "Mely országok alkották a Magyarországot körülvevő kisantantot?", "options": ["Csehszlovákia, Románia és Jugoszlávia", "Németország, Ausztria és Olaszország", "Lengyelország és Oroszország", "Franciaország és Nagy-Britannia"], "correctIndex": 0, "explanation": "Csehszlovákia, Románia és a Szerb-Horvát-Szlovén Királyság (Jugoszlávia)."},
    {"id": "ex.b1.horthykorszak.04.08", "type": "fill-blank", "lesson": "lesson.b1.horthykorszak.04", "teaches": ["orokbaratsagi"], "prompt": "Egészítsd ki a mondatot!", "sentence": "Rómában *örökbarátsági* szerződést írtak alá.", "target": "örökbarátsági"}
]
write_json(EXERCISES_DIR / "ex.b1.horthykorszak.04.json", make_exercise_group("ex.b1.horthykorszak.04", "A revízió és külpolitika gyakorlatok", "Gyakorlatok a revízióról, a kisantantról, az olasz szerződésről és a törekvést kifejező igékről.", exs_22_4))

lesson_22_4 = make_lesson(
    "lesson.b1.horthykorszak.04",
    "A revíziós törekvések és a nemzetközi elszigeteltség feloldása",
    "Törekvést és szándékot kifejező szerkezetek (törekszik vmire, célul tűz ki)",
    "Ismerjük meg a Horthy-korszak revíziós külpolitikáját, a kisantant gyűrűjét és az 1927-es olasz barátsági szerződést.",
    ["Megérteni a revízió fogalmát és központi szerepét a korszakban", "Ismerni a kisantant ellenséges szövetségét és az elszigeteltség feloldását", "Használni a külpolitikai szándékot és törekvést kifejező nyelvtani formákat"],
    "story.b1.horthykorszak.04",
    "voc.b1.horthykorszak.04",
    "gr.b1.horthykorszak.04",
    "ex.b1.horthykorszak.04",
    [e["id"] for e in exs_22_4]
)
write_json(LESSONS_DIR / "lesson.b1.horthykorszak.04.json", lesson_22_4)


# Lesson 5: A nagy gazdasági világválság (1929–1933) és Gömbös Gyula
story_22_5 = make_story(
    "story.b1.horthykorszak.05",
    "A nagy gazdasági világválság és a jobbratolódás: Gömbös Gyula",
    "Az 1929-es New York-i tőzsdekrach elérte Magyarországot is: a búza ára összeomlott, tömeges munkanélküliség támadt. 1932-ben Gömbös Gyula miniszterelnök a Nemzeti Munkatervvel és német kapcsolatokkal keresett kiutat.",
    "Budapest és vidéki agrárvidékek",
    ["Válságot, visszaesést és politikai jobbratolódást kifejező igék (összeomlik, munkanélkülivé válik, kiutat keres, közeledik)", "Great Depression 1929, agrarian crisis, Gömbös Gyula, and alignment with Germany"],
    ["világválság", "tőzsdekrach", "munkanélküliség", "Gömbös Gyula", "Nemzeti Munkaterv"],
    [
        "1929 októberében a New York-i tőzsdekrachhel kirobbant a nagy gazdasági világválság, amely súlyos csapást mért a hitelből gazdálkodó Magyarországra. A magyar búza ára a harmadára esett vissza, a bankok csődbe jutottak, és százezrek váltak munkanélkülivé.",
        "A válság politikai fordulathoz vezetett: 1931-ben Bethlen István lemondott, majd 1932-ben Horthy Miklós Gömbös Gyulát nevezte ki miniszterelnökké. Gömbös 95 pontos 'Nemzeti Munkatervével' és az államhatalom megerősítésével akarta kezelni a bajokat.",
        "Gömbös a magyar mezőgazdasági termékek számára piacot keresve szoros kapcsolatokat épített ki a fasiszta Olaszországgal és a hitleri Németországgal. Ezzel kezdetét vette Magyarország fokozatos sodródása a tengelyhatalmak felé."
    ],
    [
        {"lemma": "világválság", "pos": "noun", "cefr": "B1", "gloss": "Great Depression (global economic crisis)"},
        {"lemma": "tőzsdekrach", "pos": "noun", "cefr": "B1", "gloss": "stock market crash (1929)"},
        {"lemma": "munkanélküliség", "pos": "noun", "cefr": "B1", "gloss": "unemployment"},
        {"lemma": "Nemzeti Munkaterv", "pos": "noun", "cefr": "B1", "gloss": "National Work Plan (Gömbös's 95-point program)"},
        {"lemma": "sodródás", "pos": "noun", "cefr": "B1", "gloss": "drifting (towards totalitarian alignment)"}
    ],
    [
        {
            "question": "Melyik évben robbant ki a nagy gazdasági világválság a New York-i tőzsdekrachhel?",
            "options": ["1929-ben", "1914-ben", "1927-ben", "1938-ban"],
            "correctIndex": 0,
            "explanation": "A nagy gazdasági világválság 1929-ben kezdődött."
        }
    ]
)
write_json(STORIES_DIR / "story.b1.horthykorszak.05.json", story_22_5)

voc_22_5 = {
    "id": "voc.b1.horthykorszak.05",
    "title": "A gazdasági válság és jobbratolódás szókincse",
    "description": "Világválság, tőzsdekrach, munkanélküliség, Gömbös Gyula és sodródás.",
    "entries": [
        {"lemma": "világválság", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "severe global economic crisis of 1929–1933", "examples": [{"hu": "A világválság megbénította a magyar gazdaságot.", "en": "The world crisis paralyzed the Hungarian economy."}]}]},
        {"lemma": "munkanélküliség", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "joblessness affecting hundreds of thousands", "examples": [{"hu": "A munkanélküliség óriási méreteket öltött.", "en": "Unemployment took on enormous proportions."}]}]},
        {"lemma": "tőzsdekrach", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "1929 Wall Street stock market collapse", "examples": [{"hu": "A tőzsdekrach elindította a bankcsődöket.", "en": "The stock crash triggered the bank failures."}]}]},
        {"lemma": "Nemzeti Munkaterv", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "95-point reform plan published by Gyula Gömbös in 1932", "examples": [{"hu": "Gömbös meghirdette a Nemzeti Munkatervet.", "en": "Gömbös announced the National Work Plan."}]}]},
        {"lemma": "sodródás", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "involuntary drifting towards alliance with Germany", "examples": [{"hu": "Megkezdődött az ország politikai sodródása.", "en": "The country's political drift began."}]}]}
    ]
}
write_json(VOCAB_DIR / "voc.b1.horthykorszak.05.json", voc_22_5)

gr_22_5 = {
    "id": "gr.b1.horthykorszak.05",
    "title": "Következményt és irányt kifejező szerkezetek (oda vezet, hogy; sodródik vmi felé)",
    "description": "Expressing consequence, directionality of historical processes, and geopolitical shifts.",
    "rules": [
        {
            "explanation": "Történelmi folyamatok lefolyásának bemutatására az 'oda vezet, hogy...', 'eredményeként...', 'sodródik a háború felé' szerkezeteket alkalmazzuk.",
            "examples": [
                {"spanish": "A válság a kormány lemondásához vezetett.", "english": "The crisis led to the resignation of the government."},
                {"spanish": "Magyarország a tengelyhatalmak felé sodródott.", "english": "Hungary drifted towards the Axis powers."}
            ]
        }
    ]
}
write_json(GRAMMAR_DIR / "gr.b1.horthykorszak.05.json", gr_22_5)

exs_22_5 = [
    {"id": "ex.b1.horthykorszak.05.01", "type": "multiple-choice", "lesson": "lesson.b1.horthykorszak.05", "teaches": ["vilagvalsag-1929"], "prompt": "Mikor robbant ki a nagy gazdasági világválság?", "options": ["1929-ben", "1914-ben", "1920-ban", "1939-ben"], "correctIndex": 0, "explanation": "1929 októberében kezdődött a válság a New York-i tőzsdekrachhel."},
    {"id": "ex.b1.horthykorszak.05.02", "type": "fill-blank", "lesson": "lesson.b1.horthykorszak.05", "teaches": ["vilagvalsag"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A nagy gazdasági *világválság* összeomlást idézett elő.", "target": "világválság"},
    {"id": "ex.b1.horthykorszak.05.03", "type": "sentence-builder", "lesson": "lesson.b1.horthykorszak.05", "teaches": ["Gombos-Gyula", "Munkaterv"], "prompt": "Rakd össze a kormányprogramról szóló mondatot!", "chips": ["Gömbös", "Gyula", "meghirdette", "a", "95", "pontos", "Nemzeti", "Munkatervet."], "target": "Gömbös Gyula meghirdette a 95 pontos Nemzeti Munkatervet.", "english": "Gyula Gömbös announced the 95-point National Work Plan."},
    {"id": "ex.b1.horthykorszak.05.04", "type": "multiple-choice", "lesson": "lesson.b1.horthykorszak.05", "teaches": ["valsag-kovetkezmenye-magyar"], "prompt": "Milyen közvetlen gazdasági hatása volt a válságnak Magyarországon?", "options": ["A búza árának zuhanása, bankcsődök és tömeges munkanélküliség", "Mindenki meggazdagodott", "Új gyárak százai nyíltak meg", "Megszűnt a pénzhasználat"], "correctIndex": 0, "explanation": "A mezőgazdasági árak összeomlottak és százezrek vesztették el munkájukat."},
    {"id": "ex.b1.horthykorszak.05.05", "type": "fill-blank", "lesson": "lesson.b1.horthykorszak.05", "teaches": ["munkanelkuliseg"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A városokban hatalmasra nőtt a *munkanélküliség*.", "target": "munkanélküliség"},
    {"id": "ex.b1.horthykorszak.05.06", "type": "sentence-builder", "lesson": "lesson.b1.horthykorszak.05", "teaches": ["nemet", "piac"], "prompt": "Alkoss szabályos összetett mondatot!", "chips": ["A", "magyar", "gazdaság", "a", "német", "piac", "függőségébe", "került."], "target": "A magyar gazdaság a német piac függőségébe került.", "english": "The Hungarian economy fell into dependency on the German market."},
    {"id": "ex.b1.horthykorszak.05.07", "type": "multiple-choice", "lesson": "lesson.b1.horthykorszak.05", "teaches": ["Gombos-kulpolitika"], "prompt": "Kikkel épített ki szoros gazdasági és politikai szövetséget Gömbös Gyula?", "options": ["Németországgal és Olaszországgal", "Angliával és az Egyesült Államokkal", "A Szovjetunióval és Kínával", "A kisantant államokkal"], "correctIndex": 0, "explanation": "Gömbös a tengelyhatalmakhoz (Berlin, Róma) közeledett piacot és revíziót remélve."},
    {"id": "ex.b1.horthykorszak.05.08", "type": "fill-blank", "lesson": "lesson.b1.horthykorszak.05", "teaches": ["sodrodas"], "prompt": "Egészítsd ki a mondatot!", "sentence": "Megindult az ország veszélyes *sodródása* a tengelyhatalmak felé.", "target": "sodródása"}
]
write_json(EXERCISES_DIR / "ex.b1.horthykorszak.05.json", make_exercise_group("ex.b1.horthykorszak.05", "A világválság és Gömbös gyakorlatok", "Gyakorlatok az 1929-es világválságról, Gömbös Gyuláról, a Nemzeti Munkatervről és a következményt kifejező szerkezetekről.", exs_22_5))

lesson_22_5 = make_lesson(
    "lesson.b1.horthykorszak.05",
    "A nagy gazdasági világválság és a jobbratolódás: Gömbös Gyula",
    "Következményt és irányt kifejező szerkezetek (oda vezet, sodródik)",
    "Ismerjük meg az 1929-es nagy gazdasági világválság hatásait, Gömbös Gyula programját és a német orientáció kezdetét.",
    ["Tudni az 1929-es világválság magyarországi súlyos következményeit", "Ismerni Gömbös Gyula miniszterelnökségét és a Nemzeti Munkatervet", "Használni a politikai következményeket és irányváltásokat kifejező mondatokat"],
    "story.b1.horthykorszak.05",
    "voc.b1.horthykorszak.05",
    "gr.b1.horthykorszak.05",
    "ex.b1.horthykorszak.05",
    [e["id"] for e in exs_22_5]
)
write_json(LESSONS_DIR / "lesson.b1.horthykorszak.05.json", lesson_22_5)


# Unit 22 Consolidation
cons_22_exs = [
    {"id": "ex.b1.horthykorszak.cons.01", "type": "multiple-choice", "lesson": "lesson.b1.horthykorszak.consolidation", "teaches": ["kormanyzovalasztas-1920"], "prompt": "Melyik évben és napon választotta kormányzóvá a Nemzetgyűlés Horthy Miklóst?", "options": ["1920. március 1-jén", "1914. július 28-án", "1927. január 1-jén", "1929. október 29-én"], "correctIndex": 0, "explanation": "1920. március 1-jén választották kormányzóvá."},
    {"id": "ex.b1.horthykorszak.cons.02", "type": "fill-blank", "lesson": "lesson.b1.horthykorszak.consolidation", "teaches": ["kormanyzova"], "prompt": "Horthy Miklóst *kormányzóvá* választották a Budai Várban.", "sentence": "Horthy Miklóst *kormányzóvá* választották a Budai Várban.", "target": "kormányzóvá"},
    {"id": "ex.b1.horthykorszak.cons.03", "type": "multiple-choice", "lesson": "lesson.b1.horthykorszak.consolidation", "teaches": ["Bethlen-konszolidacio-evek"], "prompt": "Mely években volt miniszterelnök gróf Bethlen István a konszolidáció idején?", "options": ["1921 és 1931 között", "1914 és 1918 között", "1932 és 1936 között", "1944 és 1945 között"], "correctIndex": 0, "explanation": "Bethlen István 1921–1931 között vezette a kormányt."},
    {"id": "ex.b1.horthykorszak.cons.04", "type": "fill-blank", "lesson": "lesson.b1.horthykorszak.consolidation", "teaches": ["Pengot"], "prompt": "1927-ben bevezették az értékálló új valutát, a *Pengőt*.", "sentence": "1927-ben bevezették az értékálló új valutát, a *Pengőt*.", "target": "Pengőt"},
    {"id": "ex.b1.horthykorszak.cons.05", "type": "sentence-builder", "lesson": "lesson.b1.horthykorszak.consolidation", "teaches": ["Nepszovetseg", "kolcson"], "prompt": "Rakd össze a konszolidációról szóló mondatot!", "chips": ["A", "Népszövetség", "kölcsöne", "segítette", "a", "magyar", "gazdasági", "újjáépítést."], "target": "A Népszövetség kölcsöne segítette a magyar gazdasági újjáépítést.", "english": "The League of Nations loan helped Hungarian economic reconstruction."},
    {"id": "ex.b1.horthykorszak.cons.06", "type": "multiple-choice", "lesson": "lesson.b1.horthykorszak.consolidation", "teaches": ["Klebelsberg-nepiskolak-5000"], "prompt": "Hány népiskolai tantermet és tanítói lakást építtetett gróf Klebelsberg Kuno?", "options": ["Több mint ötezret (5000)", "Mindössze tízet", "Százezret", "Kettőt"], "correctIndex": 0, "explanation": "Több mint 5000 tantermet épített az analfabetizmus leküzdésére."},
    {"id": "ex.b1.horthykorszak.cons.07", "type": "fill-blank", "lesson": "lesson.b1.horthykorszak.consolidation", "teaches": ["Szegedi-Egyetemet"], "prompt": "Klebelsberg felvirágoztatta a *Szegedi Egyetemet*.", "sentence": "Klebelsberg felvirágoztatta a *Szegedi Egyetemet*.", "target": "Szegedi Egyetemet"},
    {"id": "ex.b1.horthykorszak.cons.08", "type": "sentence-builder", "lesson": "lesson.b1.horthykorszak.consolidation", "teaches": ["kulturfoleny", "oktatas"], "prompt": "Alkoss szabályos történelmi mondatot!", "chips": ["Klebelsberg", "az", "oktatás", "és", "kultúra", "fejlesztésére", "törekedett."], "target": "Klebelsberg az oktatás és kultúra fejlesztésére törekedett.", "english": "Klebelsberg aimed at the development of education and culture."},
    {"id": "ex.b1.horthykorszak.cons.09", "type": "multiple-choice", "lesson": "lesson.b1.horthykorszak.consolidation", "teaches": ["revizio-celja"], "prompt": "Mi volt a revízió célja a két háború közötti Magyarországon?", "options": ["A trianoni békediktátum határainak igazságos megváltoztatása", "Egy új császárság alapítása Ázsiában", "A vasutak bezárása", "Az oktatás betiltása"], "correctIndex": 0, "explanation": "A revízió a határok békés vagy fegyveres felülvizsgálatát célozta."},
    {"id": "ex.b1.horthykorszak.cons.10", "type": "fill-blank", "lesson": "lesson.b1.horthykorszak.consolidation", "teaches": ["revizio"], "prompt": "A *revízió* a magyar külpolitika legfontosabb vezérelve volt.", "sentence": "A *revízió* a magyar külpolitika legfontosabb vezérelve volt.", "target": "revízió"},
    {"id": "ex.b1.horthykorszak.cons.11", "type": "sentence-builder", "lesson": "lesson.b1.horthykorszak.consolidation", "teaches": ["kisantant", "szovetseg"], "prompt": "Rakd össze a diplomáciai helyzetet leíró mondatot!", "chips": ["A", "kisantant", "Magyarország", "elszigetelésére", "hozott", "létre", "szövetséget."], "target": "A kisantant Magyarország elszigetelésére hozott létre szövetséget.", "english": "The Little Entente established an alliance to isolate Hungary."},
    {"id": "ex.b1.horthykorszak.cons.12", "type": "multiple-choice", "lesson": "lesson.b1.horthykorszak.consolidation", "teaches": ["olasz-magyar-1927"], "prompt": "Melyik évben írták alá az olasz–magyar örökbarátsági szerződést Rómában?", "options": ["1927-ben", "1920-ban", "1914-ben", "1938-ban"], "correctIndex": 0, "explanation": "1927-ben írták alá az olasz–magyar szerződést."},
    {"id": "ex.b1.horthykorszak.cons.13", "type": "fill-blank", "lesson": "lesson.b1.horthykorszak.consolidation", "teaches": ["vilagvalsag"], "prompt": "1929-ben kitört a nagy gazdasági *világválság*.", "sentence": "1929-ben kitört a nagy gazdasági *világválság*.", "target": "világválság"},
    {"id": "ex.b1.horthykorszak.cons.14", "type": "sentence-builder", "lesson": "lesson.b1.horthykorszak.consolidation", "teaches": ["Gombos", "kinevezte"], "prompt": "Alkoss szabályos mondatot!", "chips": ["1932-ben", "Horthy", "kormányzó", "Gömbös", "Gyulát", "nevezte", "ki", "miniszterelnökké."], "target": "1932-ben Horthy kormányzó Gömbös Gyulát nevezte ki miniszterelnökké.", "english": "In 1932, Regent Horthy appointed Gyula Gömbös prime minister."},
    {"id": "ex.b1.horthykorszak.cons.15", "type": "multiple-choice", "lesson": "lesson.b1.horthykorszak.consolidation", "teaches": ["Gombos-Nemzeti-Munkaterv"], "prompt": "Hány pontból állt Gömbös Gyula Nemzeti Munkaterve?", "options": ["95 pontból", "12 pontból", "14 pontból", "300 pontból"], "correctIndex": 0, "explanation": "Gömbös 95 pontos Nemzeti Munkatervet hirdetett meg."},
    {"id": "ex.b1.horthykorszak.cons.16", "type": "fill-blank", "lesson": "lesson.b1.horthykorszak.consolidation", "teaches": ["munkanelkuliseg"], "prompt": "A gazdasági krach következtében drámai mértékű lett a *munkanélküliség*.", "sentence": "A gazdasági krach következtében drámai mértékű lett a *munkanélküliség*.", "target": "munkanélküliség"},
    {"id": "ex.b1.horthykorszak.cons.17", "type": "sentence-builder", "lesson": "lesson.b1.horthykorszak.consolidation", "teaches": ["sodrodas", "tengely"], "prompt": "Rakd össze a történelmi összefoglalást!", "chips": ["A", "válság", "és", "a", "revízió", "Németország", "felé", "sodorta", "az", "országot."], "target": "A válság és a revízió Németország felé sodorta az országot.", "english": "The crisis and revisionism drifted the country towards Germany."},
    {"id": "ex.b1.horthykorszak.cons.18", "type": "multiple-choice", "lesson": "lesson.b1.horthykorszak.consolidation", "teaches": ["kiraly-nelkuli-kiralysag-jellemzo"], "prompt": "Ki lakott a Budai Várban államfőként a két világháború között?", "options": ["Horthy Miklós kormányzó", "Ferenc József császár", "Mátyás király", "Kossuth Lajos"], "correctIndex": 0, "explanation": "Horthy Miklós kormányzó székhelye a Budai Vár volt."},
    {"id": "ex.b1.horthykorszak.cons.19", "type": "fill-blank", "lesson": "lesson.b1.horthykorszak.consolidation", "teaches": ["analfabetizmust"], "prompt": "A népiskolák segítettek legyőzni az *analfabetizmust*.", "sentence": "A népiskolák segítettek legyőzni az *analfabetizmust*.", "target": "analfabetizmust"},
    {"id": "ex.b1.horthykorszak.cons.20", "type": "multiple-choice", "lesson": "lesson.b1.horthykorszak.consolidation", "teaches": ["Horthy-korszak-osszegzes"], "prompt": "Milyen kettősség jellemezte a Horthy-korszakot (1920–1944)?", "options": ["A sikeres gazdasági-kulturális konszolidáció és felemelkedés, valamint a revízió miatti végzetes sodródás a totalitárius hatalmakhoz", "Kizárólagos békés elszigeteltség és tétlenség", "A kommunista eszmék gyors terjedése", "A mezőgazdaság teljes felszámolása"], "correctIndex": 0, "explanation": "A konszolidáció és kultúra sikerei mellett a revíziós kényszer a II. világháborúba sodorta az országot."}
]
write_json(EXERCISES_DIR / "ex.b1.horthykorszak.consolidation.json", make_exercise_group("ex.b1.horthykorszak.consolidation", "A Horthy-korszak összefoglaló gyakorlatok", "Átfogó teszt a Horthy-korszakról: a kormányzóválasztásról, Bethlenről, Klebelsbergről, a revízióról és a válságról.", cons_22_exs))

cons_22_lesson = {
    "id": "lesson.b1.horthykorszak.consolidation",
    "title": "The Interwar Years: Unit 22 Consolidation",
    "level": "B1",
    "track": "citizenship",
    "estimatedMinutes": 25,
    "prerequisites": [
        "lesson.b1.horthykorszak.01",
        "lesson.b1.horthykorszak.02",
        "lesson.b1.horthykorszak.03",
        "lesson.b1.horthykorszak.04",
        "lesson.b1.horthykorszak.05"
    ],
    "grammar": ["Unit review"],
    "vocabulary": ["Unit review"],
    "culturalContext": "Magyar történelem összefoglalás (Honosítási vizsgafelkészítő)",
    "sections": [
        {
            "type": "intro",
            "title": "Unit 22 Consolidation: The Interwar Years (1920–1939)",
            "body": "Ebben az összefoglaló leckében áttekintjük Horthy Miklós kormányzóvá választását (1920. március 1.), Bethlen István konszolidációját és az 1927-es Pengőt, Klebelsberg Kuno népiskola-építési programját és a szegedi egyetemet, a revíziós külpolitikát és a kisantantot, valamint az 1929-es világválságot és Gömbös Gyula miniszterelnökségét."
        },
        {
            "type": "goal",
            "title": "Consolidation Goals",
            "items": [
                "A két világháború közötti korszak kulcséveinek (1920, 1927, 1929, 1932) és folyamatainak pontos ismerete",
                "Kinevezést, időbeli folyamatosságot, célt és politikai következményeket kifejező nyelvtani szerkezetek alkalmazása",
                "A Horthy-korszak vezető személyiségeinek (Horthy, Bethlen, Klebelsberg, Gömbös) felidézése"
            ]
        },
        {
            "type": "exercise-group",
            "title": "Comprehensive Unit 22 Practice",
            "ref": "ex.b1.horthykorszak.consolidation",
            "exerciseRefs": [e["id"] for e in cons_22_exs]
        },
        {
            "type": "checklist",
            "items": [
                "Tudom, mikor választották Horthyt kormányzóvá és mi volt az államforma",
                "Ismerem Bethlen konszolidációját és az 1927-es Pengőt",
                "Megértem Klebelsberg kultúrpolitikáját és az 5000 népiskolai tantermet",
                "Ismerem a revízió eszméjét, a kisantantot és az 1929-es világválságot"
            ]
        }
    ]
}
write_json(LESSONS_DIR / "lesson.b1.horthykorszak.consolidation.json", cons_22_lesson)


# ==============================================================================
# UNIT 23: WORLD WAR II IN HUNGARY (b1-masodikvh)
# ==============================================================================

# Lesson 1: A bécsi döntések és a területgyarapodás (1938–1941)
story_23_1 = make_story(
    "story.b1.masodikvh.01",
    "A bécsi döntések és a területgyarapodás (1938–1941)",
    "Német és olasz döntőbíráskodással Magyarország 1938 és 1941 között visszacsatolta a Felvidék és Észak-Erdély magyarlakta részeit, Kárpátalját és a Délvidéket, amiért azonban súlyos politikai árat kellett fizetnie.",
    "Bécs (Belvedere palota), Kassa és Kolozsvár",
    ["Visszacsatolást, örömöt és döntőbíráskodást kifejező szerkezetek (visszacsatol, döntést hoz, ujjongva fogad)", "Vienna Awards, territorial readjustment, Northern Transylvania, Southern Slovakia"],
    ["bécsi döntés", "visszacsatolás", "Észak-Erdély", "Felvidék", "Kárpátalja"],
    [
        "1938. november 2-án az első bécsi döntéssel a Felvidék déli, túlnyomórészt magyarok lakta sávja (Kassa, Komárom, Érsekújvár) visszakerült Magyarországhoz. 1939 tavaszán a magyar hadsereg visszafoglalta a stratégiai fontosságú Kárpátalját.",
        "1940. augusztus 30-án a második bécsi döntés Észak-Erdélyt és a Székelyföldet (Kolozsvárral és Marosvásárhellyel) juttatta vissza Magyarországnak. A lakosság határtalan lelkesedéssel, virágesővel és ujjongva fogadta a bevonuló magyar honvédeket.",
        "1941 tavaszán Jugoszlávia szétesésekor a Bácska és a Muravidék (Délvidék) is visszatért. A revíziós sikerek azonban végzetesen kiszolgáltatottá tették a magyar kormányzatot a náci Németország felé."
    ],
    [
        {"lemma": "bécsi döntés", "pos": "noun", "cefr": "B1", "gloss": "Vienna Award (German-Italian territorial arbitrations)"},
        {"lemma": "visszacsatolás", "pos": "noun", "cefr": "B1", "gloss": "reannexation, reincorporation of lost lands"},
        {"lemma": "Észak-Erdély", "pos": "noun", "cefr": "B1", "gloss": "Northern Transylvania"},
        {"lemma": "Székelyföld", "pos": "noun", "cefr": "B1", "gloss": "Szeklerland"},
        {"lemma": "kiszolgáltatott", "pos": "adj", "cefr": "B1", "gloss": "vulnerable, exposed to control"}
    ],
    [
        {
            "question": "Melyik területet csatolta vissza Magyarország az 1940-es második bécsi döntéssel?",
            "options": ["Észak-Erdélyt és a Székelyföldet (Kolozsvárt)", "A délvidéki Bácskát", "Az Őrvidéket (Burgenlandot)", "Dél-Lengyelországot"],
            "correctIndex": 0,
            "explanation": "A második bécsi döntés Észak-Erdélyt és a Székelyföldet juttatta vissza."
        }
    ]
)
write_json(STORIES_DIR / "story.b1.masodikvh.01.json", story_23_1)

voc_23_1 = {
    "id": "voc.b1.masodikvh.01",
    "title": "A bécsi döntések és visszacsatolás szókincse",
    "description": "Bécsi döntés, visszacsatolás, Észak-Erdély, Székelyföld és kiszolgáltatottság.",
    "entries": [
        {"lemma": "bécsi döntés", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "arbitration awards in Vienna (1938 and 1940) returning territories", "examples": [{"hu": "Az első bécsi döntés a Felvidéket érintette.", "en": "The First Vienna Award concerned Southern Slovakia."}]}]},
        {"lemma": "visszacsatolás", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "peaceful reincorporation of ethnic Hungarian lands", "examples": [{"hu": "A visszacsatolást óriási ünneplés kísérte.", "en": "The reincorporation was accompanied by enormous celebrations."}]}]},
        {"lemma": "Észak-Erdély", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "Northern part of Transylvania returned in 1940", "examples": [{"hu": "Észak-Erdély visszatért a magyar anyaországhoz.", "en": "Northern Transylvania returned to the Hungarian motherland."}]}]},
        {"lemma": "Székelyföld", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "historic region inhabited by Szekler Hungarians", "examples": [{"hu": "A Székelyföldön virágokkal várták a honvédeket.", "en": "In Szeklerland they welcomed the soldiers with flowers."}]}]},
        {"lemma": "kiszolgáltatott", "pos": "adj", "cefr": "B1", "definitions": [{"meaning": "becoming dependent and exposed to German pressure", "examples": [{"hu": "Az ország politikailag kiszolgáltatottá vált.", "en": "The country became politically vulnerable."}]}]}
    ]
}
write_json(VOCAB_DIR / "voc.b1.masodikvh.01.json", voc_23_1)

gr_23_1 = {
    "id": "gr.b1.masodikvh.01",
    "title": "Visszatérést és helyreállítást kifejező igekötős igék (visszacsatol, visszatér, visszafoglal)",
    "description": "Using verbal prefix 'vissza-' (back, re-) to denote territorial restoration.",
    "rules": [
        {
            "explanation": "A 'vissza-' igekötő visszatérést, helyreállítást és korábbi állapotba kerülést jelöl: visszatér, visszacsatol, visszafoglal, visszakerül.",
            "examples": [
                {"spanish": "Észak-Erdély visszakerült Magyarországhoz.", "english": "Northern Transylvania returned to Hungary."},
                {"spanish": "A honvédség visszacsatolta a magyarlakta területeket.", "english": "The army reannexed the Hungarian-inhabited territories."}
            ]
        }
    ]
}
write_json(GRAMMAR_DIR / "gr.b1.masodikvh.01.json", gr_23_1)

exs_23_1 = [
    {"id": "ex.b1.masodikvh.01.01", "type": "multiple-choice", "lesson": "lesson.b1.masodikvh.01", "teaches": ["elso-becsi-dontes-1938"], "prompt": "Mely területek tértek vissza Magyarországhoz az 1938-as első bécsi döntéssel?", "options": ["A Felvidék déli magyarlakta sávja (Kassa, Komárom)", "Egész Románia", "Ausztria", "Horvátország tengerpartja"], "correctIndex": 0, "explanation": "A Felvidék déli magyarlakta részei tértek vissza 1938-ban."},
    {"id": "ex.b1.masodikvh.01.02", "type": "fill-blank", "lesson": "lesson.b1.masodikvh.01", "teaches": ["visszacsatolast"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A lakosság örömmel ünnepelte a *visszacsatolást*.", "target": "visszacsatolást"},
    {"id": "ex.b1.masodikvh.01.03", "type": "sentence-builder", "lesson": "lesson.b1.masodikvh.01", "teaches": ["masodik-becsi-dontes", "Erdely"], "prompt": "Rakd össze a történelmi tényt!", "chips": ["1940-ben", "a", "második", "bécsi", "döntéssel", "Észak-Erdély", "visszatért."], "target": "1940-ben a második bécsi döntéssel Észak-Erdély visszatért.", "english": "In 1940 with the Second Vienna Award, Northern Transylvania returned."},
    {"id": "ex.b1.masodikvh.01.04", "type": "multiple-choice", "lesson": "lesson.b1.masodikvh.01", "teaches": ["becsi-dontesek-biroi"], "prompt": "Melyik két nagyhatalom hozta meg a bécsi döntéseket döntőbíróként?", "options": ["Németország és Olaszország", "Nagy-Britannia és Franciaország", "Az USA és a Szovjetunió", "Svájc és Svédország"], "correctIndex": 0, "explanation": "Németország és Olaszország külügyminiszterei döntöttek Bécsben."},
    {"id": "ex.b1.masodikvh.01.05", "type": "fill-blank", "lesson": "lesson.b1.masodikvh.01", "teaches": ["Eszak-Erdelyt"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A magyar honvédség bevonult *Észak-Erdélybe*.", "target": "Észak-Erdélybe"},
    {"id": "ex.b1.masodikvh.01.06", "type": "sentence-builder", "lesson": "lesson.b1.masodikvh.01", "teaches": ["Szekelyfold", "honvedek"], "prompt": "Alkoss szabályos mondatot!", "chips": ["A", "Székelyföldön", "virágokkal", "köszöntötték", "a", "bevonuló", "honvédeket."], "target": "A Székelyföldön virágokkal köszöntötték a bevonuló honvédeket.", "english": "In Szeklerland they greeted the arriving soldiers with flowers."},
    {"id": "ex.b1.masodikvh.01.07", "type": "multiple-choice", "lesson": "lesson.b1.masodikvh.01", "teaches": ["ar-a-teruletekert"], "prompt": "Milyen politikai árat követelt Németország a területi revíziókért cserébe?", "options": ["Hogy Magyarország lépjen be a háborúba a tengelyhatalmak oldalán és kövesse Berlin politikáját", "Semmilyen árat nem kért", "Magyarország semlegességét garantálta", "Pénzbeli kölcsönt adott"], "correctIndex": 0, "explanation": "A revíziós sikerek végzetes német katonai elköteleződéssel jártak."},
    {"id": "ex.b1.masodikvh.01.08", "type": "fill-blank", "lesson": "lesson.b1.masodikvh.01", "teaches": ["kiszolgaltatotta"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A sikerek ára az volt, hogy az ország *kiszolgáltatottá* vált.", "target": "kiszolgáltatottá"}
]
write_json(EXERCISES_DIR / "ex.b1.masodikvh.01.json", make_exercise_group("ex.b1.masodikvh.01", "A bécsi döntések gyakorlatok", "Gyakorlatok a bécsi döntésekről, Észak-Erdélyről, a Felvidékről és a 'vissza-' igekötős szerkezetekről.", exs_23_1))

lesson_23_1 = make_lesson(
    "lesson.b1.masodikvh.01",
    "A bécsi döntések és a területgyarapodás (1938–1941)",
    "Visszatérést kifejező igekötős szerkezetek (visszacsatol, visszatér)",
    "Ismerjük meg az 1938-as és 1940-es bécsi döntéseket, a Felvidék és Észak-Erdély visszacsatolását és következményeit.",
    ["Tudni az első (1938) és második (1940) bécsi döntések területi tartalmát", "Megérteni a visszacsatolások politikai árát és a német elköteleződést", "Használni a 'vissza-' igekötővel képzett helyreállító igéket"],
    "story.b1.masodikvh.01",
    "voc.b1.masodikvh.01",
    "gr.b1.masodikvh.01",
    "ex.b1.masodikvh.01",
    [e["id"] for e in exs_23_1]
)
write_json(LESSONS_DIR / "lesson.b1.masodikvh.01.json", lesson_23_1)


# Lesson 2: Hadba lépés (1941) és a doni katasztrófa (1943)
story_23_2 = make_story(
    "story.b1.masodikvh.02",
    "Hadba lépés a Szovjetunió ellen és a doni katasztrófa (1943)",
    "1941 júniusában Kassa provokatív bombázása után Magyarország hadba lépett a Szovjetunió ellen. 1943 januárjában a fagyos Don-kanyarban a 2. magyar hadsereg megsemmisült, több mint 100 ezer honvéd pusztult el.",
    "Kassa és a Don-kanyar (Voronyezs)",
    ["Katasztrófát, fagyhalált és katonai megsemmisülést kifejező szerkezetek (megsemmisül, elesik a fagyban, áldozatul esik)", "Entry into WWII against USSR, 2nd Hungarian Army, and Don disaster 1943"],
    ["Kassa bombázása", "hadba lépés", "2. magyar hadsereg", "Don-kanyar", "doni katasztrófa"],
    [
        "1941. június 26-án ismeretlen felségjelű repülőgépek bombázták Kassát. Bárdossy László miniszterelnök ezt szovjet támadásnak minősítette, és a parlament jóváhagyása nélkül bejelentette a hadiállapot beálltát a Szovjetunióval.",
        "1942-ben a 200 ezer fős 2. magyar hadsereget a keleti frontra, a Don folyó menti 200 kilométeres szakasz védelmére küldték. A honvédek hiányos téli felszereléssel, korszerűtlen fegyverzettel és páncélelhárítás nélkül néztek szembe a Vörös Hadsereggel.",
        "1943. január 12-én a szovjet haderő mínusz 35 fokos dermesztő hidegben áttörte a magyar vonalakat Urivnál. A doni katasztrófában több mint 100-120 ezer magyar katona és munkaszolgálatos esett el, fagyott halálra vagy került fogságba: ez volt a magyar hadtörténet legnagyobb embervesztesége."
    ],
    [
        {"lemma": "doni katasztrófa", "pos": "noun", "cefr": "B1", "gloss": "Don disaster (destruction of the 2nd Army at the Don river in 1943)"},
        {"lemma": "hadiállapot", "pos": "noun", "cefr": "B1", "gloss": "state of war"},
        {"lemma": "munkaszolgálatos", "pos": "noun", "cefr": "B1", "gloss": "forced labor serviceman (unarmed Jewish and political conscripts)"},
        {"lemma": "áttörés", "pos": "noun", "cefr": "B1", "gloss": "military breakthrough"},
        {"lemma": "fagyhalál", "pos": "noun", "cefr": "B1", "gloss": "death by freezing, hypothermia"}
    ],
    [
        {
            "question": "Melyik oroszországi folyó mentén semmisült meg a 2. magyar hadsereg 1943 januárjában?",
            "options": ["A Don folyó kanyarulatában (Don-kanyar)", "A Volga mentén", "A Dnyepernél", "A Névánál"],
            "correctIndex": 0,
            "explanation": "A Don folyó mentén zajlott a magyar hadtörténet legnagyobb katasztrófája."
        }
    ]
)
write_json(STORIES_DIR / "story.b1.masodikvh.02.json", story_23_2)

voc_23_2 = {
    "id": "voc.b1.masodikvh.02",
    "title": "A hadba lépés és doni katasztrófa szókincse",
    "description": "Doni katasztrófa, hadiállapot, munkaszolgálatos, áttörés és fagyhalál.",
    "entries": [
        {"lemma": "doni katasztrófa", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "1943 destruction of the 2nd Hungarian Army in the Don bend", "examples": [{"hu": "A doni katasztrófára minden évben emlékezünk.", "en": "We remember the Don disaster every year."}]}]},
        {"lemma": "hadiállapot", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "official state of war between nations", "examples": [{"hu": "Bejelentették a hadiállapotot a Szovjetunióval.", "en": "They announced the state of war with the Soviet Union."}]}]},
        {"lemma": "munkaszolgálatos", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "unarmed conscript used for dangerous military forced labor", "examples": [{"hu": "Tízezer munkaszolgálatos pusztult el a fronton.", "en": "Ten thousand forced laborers perished on the front."}]}]},
        {"lemma": "áttörés", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "enemy offensive breaking through defense lines", "examples": [{"hu": "A szovjet áttörés megpecsételte a hadsereg sorsát.", "en": "The Soviet breakthrough sealed the fate of the army."}]}]},
        {"lemma": "fagyhalál", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "death caused by extreme sub-zero cold", "examples": [{"hu": "Sokan haltak fagyhalált a dermesztő orosz télben.", "en": "Many died of hypothermia in the freezing Russian winter."}]}]}
    ]
}
write_json(VOCAB_DIR / "voc.b1.masodikvh.02.json", voc_23_2)

gr_23_2 = {
    "id": "gr.b1.masodikvh.02",
    "title": "Katasztrófát és veszteséget kifejező határozós szerkezetek (áldozatul esik, fogságba kerül, megsemmisül)",
    "description": "Expressing tragedy, mass casualties, and military losses with idiomatic verbal expressions.",
    "rules": [
        {
            "explanation": "Katasztrófák és háborús tragédiák kifejezése: 'áldozatul esik a fagyos télnek', 'fogságba esik/kerül', 'teljesen megsemmisül'.",
            "examples": [
                {"spanish": "Több mint százezer ember esett áldozatul a doni katasztrófában.", "english": "More than one hundred thousand people fell victim in the Don disaster."},
                {"spanish": "A 2. hadsereg megsemmisült a mínusz harmincöt fokban.", "english": "The 2nd Army was destroyed in minus thirty-five degrees."}
            ]
        }
    ]
}
write_json(GRAMMAR_DIR / "gr.b1.masodikvh.02.json", gr_23_2)

exs_23_2 = [
    {"id": "ex.b1.masodikvh.02.01", "type": "multiple-choice", "lesson": "lesson.b1.masodikvh.02", "teaches": ["Kassa-bombazasa-1941"], "prompt": "Melyik város bombázása szolgált ürügyül Magyarország 1941-es hadba lépésére a Szovjetunió ellen?", "options": ["Kassa bombázása (1941. június 26.)", "Budapest bombázása", "Szeged bombázása", "Debrecen bombázása"], "correctIndex": 0, "explanation": "Kassa 1941. június 26-i bombázása után lépett hadba az ország."},
    {"id": "ex.b1.masodikvh.02.02", "type": "fill-blank", "lesson": "lesson.b1.masodikvh.02", "teaches": ["hadiallapotot"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A kormány bejelentette a *hadiállapotot* a Szovjetunióval.", "target": "hadiállapotot"},
    {"id": "ex.b1.masodikvh.02.03", "type": "sentence-builder", "lesson": "lesson.b1.masodikvh.02", "teaches": ["doni-katasztrofa", "1943"], "prompt": "Rakd össze a tragikus történelmi mondatot!", "chips": ["1943", "januárjában", "megtörtént", "a", "tragikus", "doni", "katasztrófa."], "target": "1943 januárjában megtörtént a tragikus doni katasztrófa.", "english": "In January 1943, the tragic Don disaster occurred."},
    {"id": "ex.b1.masodikvh.02.04", "type": "multiple-choice", "lesson": "lesson.b1.masodikvh.02", "teaches": ["doni-aldozatok-szama"], "prompt": "Hány magyar honvéd és munkaszolgálatos esett el vagy fagyott halálra a Don-kanyarban?", "options": ["Több mint 100-120 ezer ember", "Ötszáz ember", "Egész Európa lakossága", "Kevesebb mint ezer ember"], "correctIndex": 0, "explanation": "Több mint 100-120 000 magyar áldozata volt a doni áttörésnek."},
    {"id": "ex.b1.masodikvh.02.05", "type": "fill-blank", "lesson": "lesson.b1.masodikvh.02", "teaches": ["munkaszolgalatos"], "prompt": "Egészítsd ki a mondatot!", "sentence": "Sok fegyvertelen *munkaszolgálatos* veszett oda a fronton.", "target": "munkaszolgálatos"},
    {"id": "ex.b1.masodikvh.02.06", "type": "sentence-builder", "lesson": "lesson.b1.masodikvh.02", "teaches": ["fagyhalal", "aldozatai"], "prompt": "Alkoss szabályos mondatot!", "chips": ["A", "katonák", "áldozatul", "estek", "a", "rendkívüli", "fagyhalálnak."], "target": "A katonák áldozatul estek a rendkívüli fagyhalálnak.", "english": "The soldiers fell victim to extreme hypothermia."},
    {"id": "ex.b1.masodikvh.02.07", "type": "multiple-choice", "lesson": "lesson.b1.masodikvh.02", "teaches": ["felszereles-hianya"], "prompt": "Miért volt kiszolgáltatott a 2. magyar hadsereg a Donnál?", "options": ["Mert nem volt megfelelő téli ruházatuk, páncélelhárításuk és modern fegyverzetük a túlerővel szemben", "Mert eltévedtek az erdőben", "Mert túl sok fegyverük volt", "Mert nem akartak harcolni"], "correctIndex": 0, "explanation": "A hadsereg elavult fegyverzettel és téli felszerelés nélkül védte a hatalmas frontszakaszt."},
    {"id": "ex.b1.masodikvh.02.08", "type": "fill-blank", "lesson": "lesson.b1.masodikvh.02", "teaches": ["megsemmisult"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A 2. magyar hadsereg szinte teljesen *megsemmisült* a Donnál.", "target": "megsemmisült"}
]
write_json(EXERCISES_DIR / "ex.b1.masodikvh.02.json", make_exercise_group("ex.b1.masodikvh.02", "Hadba lépés és a Don-kanyar gyakorlatok", "Gyakorlatok Kassa bombázásáról, a 2. magyar hadseregről, a doni katasztrófáról és a veszteséget kifejező szerkezetekről.", exs_23_2))

lesson_23_2 = make_lesson(
    "lesson.b1.masodikvh.02",
    "Hadba lépés a Szovjetunió ellen és a doni katasztrófa (1943)",
    "Katasztrófát kifejező szerkezetek (áldozatul esik, megsemmisül)",
    "Ismerjük meg az 1941-es hadba lépést és az 1943. januári doni katasztrófa megrázó eseményeit.",
    ["Tudni az 1941-es szovjet elleni hadba lépés körülményeit (Kassa bombázása)", "Ismerni a 2. magyar hadsereg 1943-as doni katasztrófáját (100-120 ezer áldozat)", "Használni a katasztrófát és hadtörténeti veszteséget leíró nyelvtani formákat"],
    "story.b1.masodikvh.02",
    "voc.b1.masodikvh.02",
    "gr.b1.masodikvh.02",
    "ex.b1.masodikvh.02",
    [e["id"] for e in exs_23_2]
)
write_json(LESSONS_DIR / "lesson.b1.masodikvh.02.json", lesson_23_2)


# Lesson 3: A hintapolitika és Magyarország 1944. március 19-i német megszállása
story_23_3 = make_story(
    "story.b1.masodikvh.03",
    "A Kállay-kettős és az 1944. március 19-i német megszállás",
    "A doni katasztrófa után Kállay Miklós miniszterelnök titkos béketárgyalásokkal próbált kilépni a háborúból (hintapolitika). Hitler válaszul elrendelte a Margarethe-hadműveletet: 1944. március 19-én a Wehrmacht megszállta Magyarországot.",
    "Klessheim és Budapest",
    ["Kettős politikát, titkos tárgyalást és megszállást kifejező szerkezetek (titokban tárgyal, elrendeli a megszállást, csapdába csal)", "Kállay's swing policy, secret peace talks, Operation Margarethe, and German occupation"],
    ["hintapolitika", "Kállay Miklós", "Margarethe-hadművelet", "német megszállás", "Gestapo"],
    [
        "1942 és 1944 között Kállay Miklós kormánya a 'hintapolitikát' (Kállay-kettős) folytatta: kifelé hűséget mutatott Berlin felé, de titokban fegyverszüneti tárgyalásokat folytatott a nyugati szövetségesekkel Törökországon és Svájcon keresztül.",
        "A német hírszerzés azonban lehallgatta a kapcsolatokat. Hitler 1944. március 18-án a salzburgi Klessheim kastélyba kérette Horthy Miklóst, és kész tények elé állította a katonai megszállásról.",
        "1944. március 19-én hajnalban a náci német Wehrmacht és az SS csapatok ellenállás nélkül megszállták Magyarországot (Margarethe-hadművelet). A Gestapo azonnal letartóztatta a németellenes politikusokat, és egy engedelmes bábkormányt (Sztójay Döme) kényszerített az országra."
    ],
    [
        {"lemma": "hintapolitika", "pos": "noun", "cefr": "B1", "gloss": "swing policy (dual diplomacy balancing Axis and Allies)"},
        {"lemma": "megszállás", "pos": "noun", "cefr": "B1", "gloss": "military occupation"},
        {"lemma": "Gestapo", "pos": "noun", "cefr": "B1", "gloss": "Nazi secret state police"},
        {"lemma": "bábkormány", "pos": "noun", "cefr": "B1", "gloss": "puppet government"},
        {"lemma": "fegyverszünet", "pos": "noun", "cefr": "B1", "gloss": "armistice, truce"}
    ],
    [
        {
            "question": "Melyik napon szállta meg náci Németország katonailag Magyarországot (Margarethe-hadművelet)?",
            "options": ["1944. március 19-én", "1941. június 26-án", "1945. május 8-án", "1938. november 2-án"],
            "correctIndex": 0,
            "explanation": "A német megszállás 1944. március 19-én történt."
        }
    ]
)
write_json(STORIES_DIR / "story.b1.masodikvh.03.json", story_23_3)

voc_23_3 = {
    "id": "voc.b1.masodikvh.03",
    "title": "A hintapolitika és megszállás szókincse",
    "description": "Hintapolitika, Kállay Miklós, német megszállás, Gestapo és bábkormány.",
    "entries": [
        {"lemma": "hintapolitika", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "secret diplomatic maneuvering between Germany and Western Allies", "examples": [{"hu": "Kállay hintapolitikájával a kiugrást kereste.", "en": "With his swing policy, Kállay sought a way out."}]}]},
        {"lemma": "megszállás", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "foreign military takeover of the country", "examples": [{"hu": "1944. március 19-én történt a német megszállás.", "en": "On March 19, 1944, the German occupation took place."}]}]},
        {"lemma": "bábkormány", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "subservient government controlled by occupying power", "examples": [{"hu": "A megszállók bábkormányt ültettek hatalomra.", "en": "The occupiers installed a puppet government in power."}]}]},
        {"lemma": "Gestapo", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "secret police of Nazi Germany", "examples": [{"hu": "A Gestapo ezreket tartóztatott le Magyarországon.", "en": "The Gestapo arrested thousands in Hungary."}]}]},
        {"lemma": "fegyverszünet", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "truce or armistice agreement to stop fighting", "examples": [{"hu": "Titkos fegyverszüneti tárgyalásokat folytattak.", "en": "They conducted secret armistice negotiations."}]}]}
    ]
}
write_json(VOCAB_DIR / "voc.b1.masodikvh.03.json", voc_23_3)

gr_23_3 = {
    "id": "gr.b1.masodikvh.03",
    "title": "Kettősséget és látszatot kifejező szerkezetek (látszólag... valójában..., miközben)",
    "description": "Expressing dual diplomatic postures, covert vs overt actions in history.",
    "rules": [
        {
            "explanation": "Politikai kettősség és titkos tárgyalások leírására a 'látszólag... de valójában...', 'miközben titokban...' ellentétes szerkezeteket használjuk.",
            "examples": [
                {"spanish": "A kormány látszólag hűséges volt, de valójában békét keresett.", "english": "The government was seemingly loyal, but in reality sought peace."},
                {"spanish": "Miközben a fronton folyt a harc, diplomáciai puhatolózás zajlott.", "english": "While fighting continued on the front, diplomatic feelers were taking place."}
            ]
        }
    ]
}
write_json(GRAMMAR_DIR / "gr.b1.masodikvh.03.json", gr_23_3)

exs_23_3 = [
    {"id": "ex.b1.masodikvh.03.01", "type": "multiple-choice", "lesson": "lesson.b1.masodikvh.03", "teaches": ["nemet-megszallas-1944-marcius-19"], "prompt": "Mikor szállta meg Németország Magyarországot a Margarethe-hadművelet keretében?", "options": ["1944. március 19-én", "1941. június 26-án", "1945. április 4-én", "1938. március 15-én"], "correctIndex": 0, "explanation": "1944. március 19-én történt a német megszállás."},
    {"id": "ex.b1.masodikvh.03.02", "type": "fill-blank", "lesson": "lesson.b1.masodikvh.03", "teaches": ["megszallast"], "prompt": "Egészítsd ki a mondatot!", "sentence": "Hitler elrendelte Magyarország katonai *megszállását*.", "target": "megszállását"},
    {"id": "ex.b1.masodikvh.03.03", "type": "sentence-builder", "lesson": "lesson.b1.masodikvh.03", "teaches": ["Kallay-Miklos", "hintapolitika"], "prompt": "Rakd össze a diplomáciát leíró mondatot!", "chips": ["Kállay", "Miklós", "miniszterelnök", "titkos", "hintapolitikát", "folytatott", "a", "szövetségesekkel."], "target": "Kállay Miklós miniszterelnök titkos hintapolitikát folytatott a szövetségesekkel.", "english": "Prime Minister Miklós Kállay conducted a secret swing policy with the Allies."},
    {"id": "ex.b1.masodikvh.03.04", "type": "multiple-choice", "lesson": "lesson.b1.masodikvh.03", "teaches": ["Gestapo-letartoztatasok"], "prompt": "Mely náci szervezet kezdte meg azonnal a magyar politikusok letartóztatását 1944 márciusában?", "options": ["A Gestapo és az SS", "A Vöröskereszt", "A Népszövetség", "A bécsi rendőrség"], "correctIndex": 0, "explanation": "A Gestapo azonnal letartóztatta az ellenzéki és zsidó vezetőket."},
    {"id": "ex.b1.masodikvh.03.05", "type": "fill-blank", "lesson": "lesson.b1.masodikvh.03", "teaches": ["babkormanyt"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A németek egy engedelmes *bábkormányt* állítottak az ország élére.", "target": "bábkormányt"},
    {"id": "ex.b1.masodikvh.03.06", "type": "sentence-builder", "lesson": "lesson.b1.masodikvh.03", "teaches": ["latszolag", "valojaban"], "prompt": "Alkoss szabályos összetett mondatot!", "chips": ["Látszólag", "szövetségesek", "voltak,", "valójában", "megszállták", "az", "egész", "országot."], "target": "Látszólag szövetségesek voltak, valójában megszállták az egész országot.", "english": "Seemingly they were allies, but in reality they occupied the entire country."},
    {"id": "ex.b1.masodikvh.03.07", "type": "multiple-choice", "lesson": "lesson.b1.masodikvh.03", "teaches": ["Klessheim-kastely"], "prompt": "Hol tartotta Hitler tárgyalásra Horthy kormányzót a megszállás napjaiban?", "options": ["A salzburgi Klessheim kastélyban", "Berlinben a kancellárián", "Rómában", "Bécsben"], "correctIndex": 0, "explanation": "Klessheimben kényszerítette Hitler Horthyt a helyzet elfogadására."},
    {"id": "ex.b1.masodikvh.03.08", "type": "fill-blank", "lesson": "lesson.b1.masodikvh.03", "teaches": ["hintapolitika"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A békét kereső *hintapolitika* lelepleződött a németek előtt.", "target": "hintapolitika"}
]
write_json(EXERCISES_DIR / "ex.b1.masodikvh.03.json", make_exercise_group("ex.b1.masodikvh.03", "A német megszállás gyakorlatok", "Gyakorlatok 1944. március 19-ről, a hintapolitikáról, a Gestapóról és a látszatot kifejező szerkezetekről.", exs_23_3))

lesson_23_3 = make_lesson(
    "lesson.b1.masodikvh.03",
    "A Kállay-kettős és az 1944. március 19-i német megszállás",
    "Kettősséget és látszatot kifejező szerkezetek (látszólag... valójában)",
    "Ismerjük meg Kállay Miklós hintapolitikáját és Magyarország 1944. március 19-i német katonai megszállását.",
    ["Tudni az 1944. március 19-i német megszállás történelmi tényét és kódnevét (Margarethe)", "Ismerni a Kállay-kormány titkos kiugrási kísérleteit (hintapolitika)", "Használni a politikai kettősséget és látszatot kifejező nyelvtani szerkezeteket"],
    "story.b1.masodikvh.03",
    "voc.b1.masodikvh.03",
    "gr.b1.masodikvh.03",
    "ex.b1.masodikvh.03",
    [e["id"] for e in exs_23_3]
)
write_json(LESSONS_DIR / "lesson.b1.masodikvh.03.json", lesson_23_3)


# Lesson 4: A magyarországi holokauszt és az embermentők
story_23_4 = make_story(
    "story.b1.masodikvh.04",
    "A magyarországi holokauszt (1944) és az embermentők",
    "A német megszállás után Adolf Eichmann irányításával alig két hónap alatt több mint 430 ezer vidéki magyar zsidót deportáltak Auschwitzba. Budapesten nemzetközi embermentők (Raoul Wallenberg, Carl Lutz) ezrek életét mentették meg.",
    "Auschwitz-Birkenau, vidéki gettók és a budapesti gettó",
    ["Emlékezést, embermentést és tragédiát kifejező szerkezetek (deportál, gettóba zár, életét menti, védelmet nyújt)", "Holocaust in Hungary 1944, Auschwitz deportations, Budapest ghetto, Wallenberg, and Righteous Among the Nations"],
    ["holokauszt", "deportálási hullám", "Auschwitz", "Raoul Wallenberg", "embermentő"],
    [
        "A német megszállást követően a Sztójay-bábkormány és a csendőrség hathatós közreműködésével megkezdődött a magyar zsidóság gettósítása és megsemmisítése. Adolf Eichmann SS-különítménye irányította a gépezetet.",
        "1944 májusa és júliusa között mintegy 437 ezer vidéki zsidó honfitársunkat zsúfoltak marhavagonokba és deportáltak az auschwitz-birkenaui haláltáborba, ahol túlnyomó többségüket azonnal gázkamrákban gyilkolták meg. Horthy július elején nemzetközi nyomásra leállította a budapesti zsidóság deportálását.",
        "A budapesti gettóban és a 'védett házakban' bátor külföldi diplomaták, mint a svéd Raoul Wallenberg és a svájci Carl Lutz védőútlevelekkel (Schutzpass) tízezrek életét mentették meg a biztos pusztulástól."
    ],
    [
        {"lemma": "holokauszt", "pos": "noun", "cefr": "B1", "gloss": "Holocaust, Shoah (systematic genocide of Jews)"},
        {"lemma": "deportál", "pos": "verb", "cefr": "B1", "gloss": "to deport to extermination camps"},
        {"lemma": "gettó", "pos": "noun", "cefr": "B1", "gloss": "ghetto"},
        {"lemma": "embermentő", "pos": "noun", "cefr": "B1", "gloss": "rescuer of Jews, Righteous Among the Nations"},
        {"lemma": "védőútlevél", "pos": "noun", "cefr": "B1", "gloss": "protective passport (Schutzpass)"}
    ],
    [
        {
            "question": "Hány vidéki magyar zsidó embert deportáltak Auschwitzba 1944 májusa és júliusa között alig néhány hét alatt?",
            "options": ["Több mint 430 ezer embert", "Kétezer embert", "Ötszáz embert", "Tízmillió embert"],
            "correctIndex": 0,
            "explanation": "Körülbelül 437 000 vidéki zsidó honfitársunkat deportálták marhavagonokban."
        }
    ]
)
write_json(STORIES_DIR / "story.b1.masodikvh.04.json", story_23_4)

voc_23_4 = {
    "id": "voc.b1.masodikvh.04",
    "title": "A holokauszt és embermentés szókincse",
    "description": "Holokauszt, deportálás, gettó, embermentő és védőútlevél.",
    "entries": [
        {"lemma": "holokauszt", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "Nazi mass genocide of European and Hungarian Jews", "examples": [{"hu": "A holokauszt áldozataira mély tisztelettel emlékezünk.", "en": "We remember the victims of the Holocaust with deep respect."}]}]},
        {"lemma": "deportálás", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "mass deportation in railway boxcars to extermination camps", "examples": [{"hu": "1944 májusában kezdődtek a tömeges deportálások.", "en": "In May 1944 mass deportations began."}]}]},
        {"lemma": "gettó", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "walled segregated quarter where Jews were confined", "examples": [{"hu": "A budapesti gettóban tízezrek zsúfolódtak össze.", "en": "In the Budapest ghetto tens of thousands were crowded together."}]}]},
        {"lemma": "embermentő", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "brave individual risking life to save persecuted people", "examples": [{"hu": "Raoul Wallenberg svéd diplomata hősies embermentő volt.", "en": "Swedish diplomat Raoul Wallenberg was a heroic rescuer."}]}]},
        {"lemma": "védőútlevél", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "protective document saving Jews from deportation", "examples": [{"hu": "Wallenberg védőútlevelekkel mentette meg az embereket.", "en": "Wallenberg saved people with protective passports."}]}]}
    ]
}
write_json(VOCAB_DIR / "voc.b1.masodikvh.04.json", voc_23_4)

gr_23_4 = {
    "id": "gr.b1.masodikvh.04",
    "title": "Kockázatvállalást és megmentést kifejező szerkezetek (életét kockáztatva, védelmet nyújt, megment a haláltól)",
    "description": "Expressing heroism, moral courage, and saving human lives under persecution.",
    "rules": [
        {
            "explanation": "Hősies és humanitárius cselekedetek leírására: 'életét kockáztatva mentette az embereket', 'védelmet nyújtott az üldözötteknek', 'megmentette a biztos haláltól'.",
            "examples": [
                {"spanish": "Wallenberg az életét kockáztatva tízezreket mentett meg.", "english": "Wallenberg risked his life to save tens of thousands."},
                {"spanish": "A diplomaták védelmet nyújtottak az üldözött családoknak.", "english": "The diplomats provided protection to persecuted families."}
            ]
        }
    ]
}
write_json(GRAMMAR_DIR / "gr.b1.masodikvh.04.json", gr_23_4)

exs_23_4 = [
    {"id": "ex.b1.masodikvh.04.01", "type": "multiple-choice", "lesson": "lesson.b1.masodikvh.04", "teaches": ["holokauszt-deportaltak-szama"], "prompt": "Körülbelül hány vidéki magyar zsidó embert deportáltak Auschwitzba 1944 tavaszán?", "options": ["Több mint 430 ezer embert", "Tízezer embert", "Ötmillió embert", "Kétszáz embert"], "correctIndex": 0, "explanation": "437 ezer vidéki magyar zsidót hurcoltak el Auschwitzba."},
    {"id": "ex.b1.masodikvh.04.02", "type": "fill-blank", "lesson": "lesson.b1.masodikvh.04", "teaches": ["deportaltak"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A vidéki zsidóságot marhavagonokban *deportálták* a haláltáborokba.", "target": "deportálták"},
    {"id": "ex.b1.masodikvh.04.03", "type": "sentence-builder", "lesson": "lesson.b1.masodikvh.04", "teaches": ["Raoul-Wallenberg", "eleteket-mentett"], "prompt": "Rakd össze a diplomata hőstettét leíró mondatot!", "chips": ["Raoul", "Wallenberg", "svéd", "diplomata", "több", "tízezer", "ember", "életét", "mentette", "meg."], "target": "Raoul Wallenberg svéd diplomata több tízezer ember életét mentette meg.", "english": "Swedish diplomat Raoul Wallenberg saved the lives of several tens of thousands of people."},
    {"id": "ex.b1.masodikvh.04.04", "type": "multiple-choice", "lesson": "lesson.b1.masodikvh.04", "teaches": ["Schutzpass-vedo-level"], "prompt": "Mit állítottak ki a svéd és svájci diplomaták (Wallenberg, Lutz) a budapesti zsidók megmentésére?", "options": ["Védőútleveleket (Schutzpass) és védett házakat biztosítottak", "Katonai egyenruhát", "Vonatjegyet Párizsba", "Pénzbeli segélyt"], "correctIndex": 0, "explanation": "Védőútlevelekkel és védett házakkal mentették meg az embereket."},
    {"id": "ex.b1.masodikvh.04.05", "type": "fill-blank", "lesson": "lesson.b1.masodikvh.04", "teaches": ["embermento"], "prompt": "Egészítsd ki a mondatot!", "sentence": "Carl Lutz svájci diplomata hősies *embermentő* volt Budapesten.", "target": "embermentő"},
    {"id": "ex.b1.masodikvh.04.06", "type": "sentence-builder", "lesson": "lesson.b1.masodikvh.04", "teaches": ["getto", "Budapest"], "prompt": "Alkoss szabályos összetett mondatot!", "chips": ["A", "fővárosban", "létrehozták", "a", "budapesti", "gettó", "zárt", "területét."], "target": "A fővárosban létrehozták a budapesti gettó zárt területét.", "english": "In the capital they created the enclosed area of the Budapest ghetto."},
    {"id": "ex.b1.masodikvh.04.07", "type": "multiple-choice", "lesson": "lesson.b1.masodikvh.04", "teaches": ["Auschwitz-megsemmisites"], "prompt": "Mi történt a deportált magyar zsidók nagy többségével Auschwitz-Birkenauban?", "options": ["Azonnal gázkamrákban meggyilkolták őket", "Szabadon engedték őket", "Iskolába küldték őket", "Hazautazhattak"], "correctIndex": 0, "explanation": "A többséget közvetlenül az érkezés után meggyilkolták a nácik."},
    {"id": "ex.b1.masodikvh.04.08", "type": "fill-blank", "lesson": "lesson.b1.masodikvh.04", "teaches": ["holokauszt"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A *holokauszt* a 20. század egyik legborzalmasabb emberi tragédiája.", "target": "holokauszt"}
]
write_json(EXERCISES_DIR / "ex.b1.masodikvh.04.json", make_exercise_group("ex.b1.masodikvh.04", "A holokauszt és embermentők gyakorlatok", "Gyakorlatok a magyarországi holokausztról, Auschwitzról, Raoul Wallenbergről és az embermentő szerkezetekről.", exs_23_4))

lesson_23_4 = make_lesson(
    "lesson.b1.masodikvh.04",
    "A magyarországi holokauszt (1944) és az embermentők",
    "Megmentést és védelmet kifejező szerkezetek (életét menti, védelmet nyújt)",
    "Ismerjük meg az 1944-es magyarországi holokausztot, a 430 ezer vidéki zsidó deportálását és Raoul Wallenberg embermentő tevékenységét.",
    ["Tudni az 1944-es vidéki zsidóság deportálásának tragikus adatait (430 ezer fő)", "Ismerni Raoul Wallenberg és Carl Lutz diplomáciai embermentő szerepét", "Használni a védelmet, megmentést és kockázatvállalást leíró nyelvtani kifejezéseket"],
    "story.b1.masodikvh.04",
    "voc.b1.masodikvh.04",
    "gr.b1.masodikvh.04",
    "ex.b1.masodikvh.04",
    [e["id"] for e in exs_23_4]
)
write_json(LESSONS_DIR / "lesson.b1.masodikvh.04.json", lesson_23_4)


# Lesson 5: A kiugrási kísérlet (1944. okt. 15.), nyilas rémuralom és Budapest ostroma
story_23_5 = make_story(
    "story.b1.masodikvh.05",
    "A kiugrási kísérlet, a nyilas rémuralom és Budapest ostroma (1944–45)",
    "1944. október 15-én Horthy Miklós bejelentette a fegyverszünetet, de a kiugrási kísérlet elbukott. Szálasi Ferenc nyilasai vették át a hatalmat, miközben Budapest ostroma a második világháború egyik legvéresebb városi csatájává vált.",
    "Budai Vár és Budapest ostroma",
    ["Hatalomátvételt, városostromot és pusztulást kifejező igék (hatalomra tör, romba dönt, elbukik a kísérlet, felrobbant)", "Horthy's failed armistice attempt Oct 15 1944, Arrow Cross terror, Szálasi, and Siege of Budapest"],
    ["kiugrási kísérlet", "nyilas rémuralom", "Szálasi Ferenc", "Budapest ostroma", "Duna-parti cipők"],
    [
        "1944. október 15-én a rádióban Horthy Miklós kormányzó történelmi proklamációban jelentette be a fegyverszünetet a szovjetekkel. A németek azonban elrabolták Horthy fiát, megbénították a parancsnoki láncot, így a kiugrási kísérlet órák alatt összeomlott.",
        "A nácik Szálasi Ferencet, a Nyilaskeresztes Párt vezetőjét ('nemzetvezető') juttatták hatalomra. A nyilas rémuralom hónapjaiban a banditák védtelen embereket és zsidók ezreit lőtték a jeges Dunába a pesti rakparton.",
        "1944 karácsonyától 1945 februárjáig zajlott Budapest 50 napos ostroma: a szovjet Vörös Hadsereg bekerítette és véres házról házra vívott harcokban foglalta el a romba dőlt fővárost. A visszavonuló németek felrobbantották az összes Duna-hidat."
    ],
    [
        {"lemma": "kiugrási kísérlet", "pos": "noun", "cefr": "B1", "gloss": "attempt to exit the war / declare armistice"},
        {"lemma": "nyilas rémuralom", "pos": "noun", "cefr": "B1", "gloss": "Arrow Cross terror regime (Szálasi)"},
        {"lemma": "ostrom", "pos": "noun", "cefr": "B1", "gloss": "military siege of a city"},
        {"lemma": "nemzetvezető", "pos": "noun", "cefr": "B1", "gloss": "'Leader of the Nation' (title assumed by fascist Szálasi)"},
        {"lemma": "hídfelrobbantás", "pos": "noun", "cefr": "B1", "gloss": "blowing up of bridges"}
    ],
    [
        {
            "question": "Melyik napon jelentette be Horthy Miklós a rádióban a sikertelen kiugrási kísérletet?",
            "options": ["1944. október 15-én", "1944. március 19-én", "1945. április 4-én", "1941. június 26-án"],
            "correctIndex": 0,
            "explanation": "1944. október 15-én történt a kiugrási kísérlet."
        }
    ]
)
write_json(STORIES_DIR / "story.b1.masodikvh.05.json", story_23_5)

voc_23_5 = {
    "id": "voc.b1.masodikvh.05",
    "title": "A kiugrás, nyilas terror és ostrom szókincse",
    "description": "Kiugrási kísérlet, nyilas rémuralom, Szálasi Ferenc, Budapest ostroma és hídfelrobbantás.",
    "entries": [
        {"lemma": "kiugrási kísérlet", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "failed attempt by Regent Horthy on Oct 15 1944 to exit the war", "examples": [{"hu": "A kiugrási kísérlet a német ellenállás miatt elbukott.", "en": "The exit attempt failed due to German resistance."}]}]},
        {"lemma": "nyilas rémuralom", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "brutal terror regime of the Arrow Cross party under Szálasi", "examples": [{"hu": "A nyilas rémuralom alatt ezreket lőttek a Dunába.", "en": "Under the Arrow Cross terror regime thousands were shot into the Danube."}]}]},
        {"lemma": "ostrom", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "deadly 50-day military siege of Budapest 1944–45", "examples": [{"hu": "Budapest ostroma romba döntötte a hidakat és palotákat.", "en": "The siege of Budapest ruined the bridges and palaces."}]}]},
        {"lemma": "nemzetvezető", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "fascist dictator title taken by Ferenc Szálasi", "examples": [{"hu": "Szálasi nemzetvezetőnek neveztette magát.", "en": "Szálasi had himself called 'Leader of the Nation'."}]}]},
        {"lemma": "hídfelrobbantás", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "destruction of all Danube bridges by retreating German troops", "examples": [{"hu": "A németek minden budapesti hidat felrobbantottak.", "en": "The Germans blew up every Budapest bridge."}]}]}
    ]
}
write_json(VOCAB_DIR / "voc.b1.masodikvh.05.json", voc_23_5)

gr_23_5 = {
    "id": "gr.b1.masodikvh.05",
    "title": "Kudarcot és pusztulást kifejező szerkezetek (elbukik, romba dől, áldozatul esik, felrobban)",
    "description": "Expressing military failure, urban destruction, and tragic collapse in war.",
    "rules": [
        {
            "explanation": "Kudarcot valló politikai és katonai akciók leírására az 'elbukik', 'összeomlik', 'romba dől', 'megsemmisül' igéket alkalmazzuk.",
            "examples": [
                {"spanish": "A kiugrási kísérlet a német beavatkozás miatt elbukott.", "english": "The exit attempt failed due to German intervention."},
                {"spanish": "Budapest történelmi épületei és hídjai romba dőltek.", "english": "Budapest's historic buildings and bridges collapsed into ruins."}
            ]
        }
    ]
}
write_json(GRAMMAR_DIR / "gr.b1.masodikvh.05.json", gr_23_5)

exs_23_5 = [
    {"id": "ex.b1.masodikvh.05.01", "type": "multiple-choice", "lesson": "lesson.b1.masodikvh.05", "teaches": ["kiugrasi-kiserlet-1944-okt-15"], "prompt": "Mikor jelentette be Horthy Miklós a fegyverszünetet és a kiugrási kísérletet a rádióban?", "options": ["1944. október 15-én", "1944. március 19-én", "1945. április 4-én", "1943. január 12-én"], "correctIndex": 0, "explanation": "1944. október 15-én olvasta fel Horthy a kiugrási proklamációt."},
    {"id": "ex.b1.masodikvh.05.02", "type": "fill-blank", "lesson": "lesson.b1.masodikvh.05", "teaches": ["kiugrasi-kiserlet"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A rosszul szervezett *kiugrási kísérlet* órák alatt elbukott.", "target": "kiugrási kísérlet"},
    {"id": "ex.b1.masodikvh.05.03", "type": "sentence-builder", "lesson": "lesson.b1.masodikvh.05", "teaches": ["Szalasi-Ferenc", "nyilasok"], "prompt": "Rakd össze a mondatot!", "chips": ["Szálasi", "Ferenc", "és", "a", "nyilasok", "átvették", "a", "hatalmat."], "target": "Szálasi Ferenc és a nyilasok átvették a hatalmat.", "english": "Ferenc Szálasi and the Arrow Cross seized power."},
    {"id": "ex.b1.masodikvh.05.04", "type": "multiple-choice", "lesson": "lesson.b1.masodikvh.05", "teaches": ["Duna-parti-cipok-emlekmu"], "prompt": "Melyik híres budapesti emlékmű állít emléket a nyilasok által a Dunába lőtt áldozatoknak?", "options": ["A 'Cipők a Duna-parton' emlékmű", "A Hősök tere", "A Szabadság-szobor", "A Lánchíd oroszlánjai"], "correctIndex": 0, "explanation": "A Parlament melletti 'Cipők a Duna-parton' a nyilas terror áldozataira emlékeztet."},
    {"id": "ex.b1.masodikvh.05.05", "type": "fill-blank", "lesson": "lesson.b1.masodikvh.05", "teaches": ["ostroma"], "prompt": "Egészítsd ki a mondatot!", "sentence": "Budapest 50 napos véres *ostroma* romba döntötte a fővárost.", "target": "ostroma"},
    {"id": "ex.b1.masodikvh.05.06", "type": "sentence-builder", "lesson": "lesson.b1.masodikvh.05", "teaches": ["hidak", "felrobbantottak"], "prompt": "Alkoss szabályos összetett mondatot!", "chips": ["A", "visszavonuló", "német", "csapatok", "felrobbantották", "az", "összes", "Duna-hidat."], "target": "A visszavonuló német csapatok felrobbantották az összes Duna-hidat.", "english": "The retreating German troops blew up all the Danube bridges."},
    {"id": "ex.b1.masodikvh.05.07", "type": "multiple-choice", "lesson": "lesson.b1.masodikvh.05", "teaches": ["Budapest-ostroma-vege"], "prompt": "Mikor ért véget Budapest ostroma a szovjet csapatok győzelmével?", "options": ["1945 februárjában", "1944 márciusában", "1945 decemberében", "1946 nyarán"], "correctIndex": 0, "explanation": "1945. február 13-án fejeződött be Budapest ostroma."},
    {"id": "ex.b1.masodikvh.05.08", "type": "fill-blank", "lesson": "lesson.b1.masodikvh.05", "teaches": ["remuralom"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A nyilas *rémuralom* sok ártatlan ember halálát okozta.", "target": "rémuralom"}
]
write_json(EXERCISES_DIR / "ex.b1.masodikvh.05.json", make_exercise_group("ex.b1.masodikvh.05", "A kiugrás és ostrom gyakorlatok", "Gyakorlatok az 1944. október 15-i kiugrási kísérletről, a nyilas terrorról, Budapest ostromáról és a kudarc igéiről.", exs_23_5))

lesson_23_5 = make_lesson(
    "lesson.b1.masodikvh.05",
    "A kiugrási kísérlet, a nyilas rémuralom és Budapest ostroma (1944–45)",
    "Kudarcot és pusztulást kifejező szerkezetek (elbukik, romba dől)",
    "Ismerjük meg az 1944. október 15-i kiugrási kísérletet, Szálasi nyilas terrorját és Budapest 50 napos pusztító ostromát.",
    ["Tudni az 1944. október 15-i kiugrási kísérlet dátumát és okait", "Ismerni Szálasi nyilas rémuralmának bűneit és a Duna-parti kivégzéseket", "Megérteni Budapest ostromát (1944–45) és a hidak felrobbantását"],
    "story.b1.masodikvh.05",
    "voc.b1.masodikvh.05",
    "gr.b1.masodikvh.05",
    "ex.b1.masodikvh.05",
    [e["id"] for e in exs_23_5]
)
write_json(LESSONS_DIR / "lesson.b1.masodikvh.05.json", lesson_23_5)


# Unit 23 Consolidation
cons_23_exs = [
    {"id": "ex.b1.masodikvh.cons.01", "type": "multiple-choice", "lesson": "lesson.b1.masodikvh.consolidation", "teaches": ["becsi-dontesek-evek"], "prompt": "Melyik évben hozták az első (Felvidék) és második (Észak-Erdély) bécsi döntést?", "options": ["1938-ban és 1940-ben", "1914-ben és 1918-ban", "1920-ban és 1927-ben", "1944-ben és 1945-ben"], "correctIndex": 0, "explanation": "1938-ban és 1940-ben hozták a bécsi döntéseket."},
    {"id": "ex.b1.masodikvh.cons.02", "type": "fill-blank", "lesson": "lesson.b1.masodikvh.consolidation", "teaches": ["visszacsatolas"], "prompt": "Az 1940-es bécsi döntéssel megtörtént Észak-Erdély *visszacsatolása*.", "sentence": "Az 1940-es bécsi döntéssel megtörtént Észak-Erdély *visszacsatolása*.", "target": "visszacsatolása"},
    {"id": "ex.b1.masodikvh.cons.03", "type": "multiple-choice", "lesson": "lesson.b1.masodikvh.consolidation", "teaches": ["Kassa-bombazasa-1941"], "prompt": "Melyik esemény után lépett hadba Magyarország a Szovjetunió ellen 1941 júniusában?", "options": ["Kassa bombázása után", "A bécsi döntés után", "Budapest ostroma után", "A trianoni szerződés után"], "correctIndex": 0, "explanation": "Kassa bombázása volt a hadba lépés ürügye."},
    {"id": "ex.b1.masodikvh.cons.04", "type": "fill-blank", "lesson": "lesson.b1.masodikvh.consolidation", "teaches": ["Don-kanyarban"], "prompt": "1943 januárjában a *Don-kanyarban* megsemmisült a 2. magyar hadsereg.", "sentence": "1943 januárjában a *Don-kanyarban* megsemmisült a 2. magyar hadsereg.", "target": "Don-kanyarban"},
    {"id": "ex.b1.masodikvh.cons.05", "type": "sentence-builder", "lesson": "lesson.b1.masodikvh.consolidation", "teaches": ["doni-katasztrofa", "veszteseg"], "prompt": "Rakd össze a doni tragédiát bemutató mondatot!", "chips": ["A", "doni", "katasztrófa", "több", "mint", "százezer", "magyar", "áldozatot", "követelt."], "target": "A doni katasztrófa több mint százezer magyar áldozatot követelt.", "english": "The Don disaster claimed more than a hundred thousand Hungarian victims."},
    {"id": "ex.b1.masodikvh.cons.06", "type": "multiple-choice", "lesson": "lesson.b1.masodikvh.consolidation", "teaches": ["nemet-megszallas-1944-03-19"], "prompt": "Melyik napon szállták meg a náci német csapatok Magyarországot?", "options": ["1944. március 19-én", "1941. június 26-án", "1944. október 15-én", "1945. május 8-án"], "correctIndex": 0, "explanation": "1944. március 19-én történt a német megszállás."},
    {"id": "ex.b1.masodikvh.cons.07", "type": "fill-blank", "lesson": "lesson.b1.masodikvh.consolidation", "teaches": ["Margarethe"], "prompt": "A német megszállási hadművelet fedőneve *Margarethe* volt.", "sentence": "A német megszállási hadművelet fedőneve *Margarethe* volt.", "target": "Margarethe"},
    {"id": "ex.b1.masodikvh.cons.08", "type": "sentence-builder", "lesson": "lesson.b1.masodikvh.consolidation", "teaches": ["holokauszt", "deportaltak"], "prompt": "Alkoss szabályos összetett mondatot!", "chips": ["1944", "tavaszán", "több", "mint", "430", "ezer", "magyar", "zsidót", "deportáltak."], "target": "1944 tavaszán több mint 430 ezer magyar zsidót deportáltak.", "english": "In spring 1944, more than 430,000 Hungarian Jews were deported."},
    {"id": "ex.b1.masodikvh.cons.09", "type": "multiple-choice", "lesson": "lesson.b1.masodikvh.consolidation", "teaches": ["Raoul-Wallenberg-embermento"], "prompt": "Ki volt az a svéd diplomata, aki tízezrek életét mentette meg Budapesten Schutzpassokkal?", "options": ["Raoul Wallenberg", "Adolf Eichmann", "Sztójay Döme", "Szálasi Ferenc"], "correctIndex": 0, "explanation": "Raoul Wallenberg bátor embermentő volt."},
    {"id": "ex.b1.masodikvh.cons.10", "type": "fill-blank", "lesson": "lesson.b1.masodikvh.consolidation", "teaches": ["vedoutlevelekkel"], "prompt": "Wallenberg svéd *védőútlevelekkel* védte meg az üldözötteket.", "sentence": "Wallenberg svéd *védőútlevelekkel* védte meg az üldözötteket.", "target": "védőútlevelekkel"},
    {"id": "ex.b1.masodikvh.cons.11", "type": "sentence-builder", "lesson": "lesson.b1.masodikvh.consolidation", "teaches": ["kiugrasi-kiserlet-1944"], "prompt": "Rakd össze a fegyverszünetről szóló mondatot!", "chips": ["1944.", "október", "15-én", "Horthy", "bejelentette", "a", "kiugrási", "kísérletet."], "target": "1944. október 15-én Horthy bejelentette a kiugrási kísérletet.", "english": "On October 15, 1944, Horthy announced the exit attempt."},
    {"id": "ex.b1.masodikvh.cons.12", "type": "multiple-choice", "lesson": "lesson.b1.masodikvh.consolidation", "teaches": ["Szalasi-nyilas-terror"], "prompt": "Ki vette át a hatalmat a sikertelen kiugrási kísérlet után a nácik segítségével?", "options": ["Szálasi Ferenc és a Nyilaskeresztes Párt", "Kállay Miklós", "Bethlen István", "Nagy Imre"], "correctIndex": 0, "explanation": "Szálasi Ferenc vezetésével nyilas rémuralom kezdődött."},
    {"id": "ex.b1.masodikvh.cons.13", "type": "fill-blank", "lesson": "lesson.b1.masodikvh.consolidation", "teaches": ["Cipok-a-Duna-parton"], "prompt": "A pesti rakparton a *Cipők a Duna-parton* emlékmű őrzi az áldozatok emlékét.", "sentence": "A pesti rakparton a *Cipők a Duna-parton* emlékmű őrzi az áldozatok emlékét.", "target": "Cipők a Duna-parton"},
    {"id": "ex.b1.masodikvh.cons.14", "type": "sentence-builder", "lesson": "lesson.b1.masodikvh.consolidation", "teaches": ["Budapest-ostroma", "pusztulas"], "prompt": "Alkoss szabályos mondatot!", "chips": ["Budapest", "ötvennapos", "ostroma", "óriási", "pusztulást", "okozott", "a", "fővárosban."], "target": "Budapest ötvennapos ostroma óriási pusztulást okozott a fővárosban.", "english": "The fifty-day siege of Budapest caused enormous destruction in the capital."},
    {"id": "ex.b1.masodikvh.cons.15", "type": "multiple-choice", "lesson": "lesson.b1.masodikvh.consolidation", "teaches": ["hidak-felrobbantasa"], "prompt": "Mit tettek a visszavonuló német csapatok Budapest Duna-hídjaival?", "options": ["Mindegyiket felrobbantották (a Lánchidat, Margit hidat, Erzsébet hidat stb.)", "Érintetlenül hagyták őket", "Új hidakat építettek", "Eladták a hidakat"], "correctIndex": 0, "explanation": "A németek az összes budapesti Duna-hidat felrobbantották."},
    {"id": "ex.b1.masodikvh.cons.16", "type": "fill-blank", "lesson": "lesson.b1.masodikvh.consolidation", "teaches": ["Auschwitzba"], "prompt": "1944-ben a vidéki zsidóság döntő részét *Auschwitzba* hurcolták.", "sentence": "1944-ben a vidéki zsidóság döntő részét *Auschwitzba* hurcolták.", "target": "Auschwitzba"},
    {"id": "ex.b1.masodikvh.cons.17", "type": "sentence-builder", "lesson": "lesson.b1.masodikvh.consolidation", "teaches": ["hintapolitika", "kudarc"], "prompt": "Rakd össze a diplomáciát összegző mondatot!", "chips": ["A", "Kállay-kormány", "hintapolitikája", "nem", "tudta", "elkerülni", "a", "megszállást."], "target": "A Kállay-kormány hintapolitikája nem tudta elkerülni a megszállást.", "english": "The Kállay government's swing policy could not avoid occupation."},
    {"id": "ex.b1.masodikvh.cons.18", "type": "multiple-choice", "lesson": "lesson.b1.masodikvh.consolidation", "teaches": ["haborus-emberveszteseg-osszegzes"], "prompt": "Körülbelül mekkora volt Magyarország teljes embervesztesége a második világháborúban?", "options": ["Közel 1 millió ember (katonák, holokauszt áldozatai, polgári lakosság)", "Alig ezer ember", "Tízmillió ember", "Kétszáz katona"], "correctIndex": 0, "explanation": "Közel egymillió magyar állampolgár vesztette életét a II. világháborúban."},
    {"id": "ex.b1.masodikvh.cons.19", "type": "fill-blank", "lesson": "lesson.b1.masodikvh.consolidation", "teaches": ["remuralom"], "prompt": "A nyilas *rémuralom* 1945 tavaszán ért véget Magyarországon.", "sentence": "A nyilas *rémuralom* 1945 tavaszán ért véget Magyarországon.", "target": "rémuralom"},
    {"id": "ex.b1.masodikvh.cons.20", "type": "multiple-choice", "lesson": "lesson.b1.masodikvh.consolidation", "teaches": ["masodikvh-kovetkezmeny"], "prompt": "Milyen következményekkel zárult Magyarország számára a második világháború?", "options": ["A visszacsatolt területek újbóli elvesztésével, szovjet katonai megszállással és romokban heverő országgal", "Új területek örökös megszerzésével", "A monarchia visszaállításával", "Semmilyen hatása nem volt"], "correctIndex": 0, "explanation": "A trianoni határok visszaálltak és szovjet megszállás alá került az ország."}
]
write_json(EXERCISES_DIR / "ex.b1.masodikvh.consolidation.json", make_exercise_group("ex.b1.masodikvh.consolidation", "A II. világháború Magyarországon összefoglaló", "Átfogó teszt a bécsi döntésekről, a Don-kanyarról, az 1944-es német megszállásról, a holokausztról és Budapest ostromáról.", cons_23_exs))

cons_23_lesson = {
    "id": "lesson.b1.masodikvh.consolidation",
    "title": "World War II in Hungary: Unit 23 Consolidation",
    "level": "B1",
    "track": "citizenship",
    "estimatedMinutes": 25,
    "prerequisites": [
        "lesson.b1.masodikvh.01",
        "lesson.b1.masodikvh.02",
        "lesson.b1.masodikvh.03",
        "lesson.b1.masodikvh.04",
        "lesson.b1.masodikvh.05"
    ],
    "grammar": ["Unit review"],
    "vocabulary": ["Unit review"],
    "culturalContext": "Magyar történelem összefoglalás (Honosítási vizsgafelkészítő)",
    "sections": [
        {
            "type": "intro",
            "title": "Unit 23 Consolidation: World War II in Hungary (1938–1945)",
            "body": "Ebben az összefoglaló leckében áttekintjük az 1938-as és 1940-es bécsi döntéseket (Felvidék, Észak-Erdély), a Szovjetunió elleni 1941-es hadba lépést (Kassa bombázása), az 1943-as doni katasztrófát, a Kállay-féle hintapolitikát, az 1944. március 19-i német megszállást, a magyarországi holokausztot és Wallenberg embermentését, valamint az 1944. október 15-i kiugrási kísérletet, a nyilas terrort és Budapest ostromát."
        },
        {
            "type": "goal",
            "title": "Consolidation Goals",
            "items": [
                "A II. világháború sorsdöntő éveinek (1938, 1940, 1941, 1943, 1944. márc. 19., 1944. okt. 15.) és eseményeinek biztos ismerete",
                "Visszatérést, katasztrófát, látszatot és kudarcot kifejező nyelvtani szerkezetek helyes alkalmazása",
                "Az embermentők (Raoul Wallenberg, Carl Lutz) és az áldozatok emlékének megértése"
            ]
        },
        {
            "type": "exercise-group",
            "title": "Comprehensive Unit 23 Practice",
            "ref": "ex.b1.masodikvh.consolidation",
            "exerciseRefs": [e["id"] for e in cons_23_exs]
        },
        {
            "type": "checklist",
            "items": [
                "Tudom a bécsi döntések és a doni katasztrófa (1943) tényeit",
                "Ismerem az 1944. március 19-i német megszállást és a hintapolitikát",
                "Megértem a holokauszt tragédiáját és Wallenberg embermentő munkáját",
                "Ismerem az 1944. október 15-i kiugrási kísérletet és Budapest ostromát"
            ]
        }
    ]
}
write_json(LESSONS_DIR / "lesson.b1.masodikvh.consolidation.json", cons_23_lesson)


# ==============================================================================
# UNIT 24: THE RÁKOSI ERA & COMMUNIST TAKEOVER (b1-rakosikorszak)
# ==============================================================================

# Lesson 1: Szovjet megszállás, az 1945-ös választások és a köztársaság
story_24_1 = make_story(
    "story.b1.rakosikorszak.01",
    "Szovjet megszállás és az 1945-ös szabad választások",
    "A második világháború végén a Vörös Hadsereg kiűzte a németeket, de szovjet katonai megszállás vette kezdetét. Az 1945-ös szabad választásokon a Független Kisgazdapárt aratott elsöprő győzelmet (57%).",
    "Budapest és Debrecen",
    ["Választási győzelmet, megszállást és politikai akaratot kifejező szerkezetek (győzelmet arat, megszállva tart, kikiáltják a köztársaságot)", "Soviet occupation, 1945 free elections, Smallholders victory, and Second Republic 1946"],
    ["szovjet megszállás", "Független Kisgazdapárt", "szabad választások", "Tildy Zoltán", "második köztársaság"],
    [
        "1944 decemberében Debrecenben megalakult az Ideiglenes Nemzetgyűlés és Nemzeti Kormány. 1945 áprilisára a szovjet csapatok kiszorították a németeket Magyarországról, de az ország szuverenitása megszűnt: a Szövetséges Ellenőrző Bizottság (SZEB) révén Vorosilov szovjet marsall irányította az államot.",
        "1945 novemberében rendezték meg Magyarország történetének egyik legtisztább, általános és titkos választását. A kommunisták vereséget szenvedtek: a polgári-demokratikus Független Kisgazdapárt abszolút többséget, a szavazatok 57%-át szerezte meg.",
        "1946. február 1-jén a parlament eltörölte a királyságot, és kikiáltotta a Magyar Köztársaságot (második köztársaság), amelynek első köztársasági elnöke Tildy Zoltán, miniszterelnöke pedig Nagy Ferenc lett."
    ],
    [
        {"lemma": "szabad választások", "pos": "noun", "cefr": "B1", "gloss": "free, democratic multi-party elections (1945)"},
        {"lemma": "Független Kisgazdapárt", "pos": "noun", "cefr": "B1", "gloss": "Independent Smallholders' Party (FKgP, winner of 1945 elections)"},
        {"lemma": "abszolút többség", "pos": "noun", "cefr": "B1", "gloss": "absolute majority (over 50%)"},
        {"lemma": "köztársasági elnök", "pos": "noun", "cefr": "B1", "gloss": "President of the Republic"},
        {"lemma": "szovjet megszállás", "pos": "noun", "cefr": "B1", "gloss": "Soviet military occupation"}
    ],
    [
        {
            "question": "Melyik párt nyerte meg az 1945-ös demokratikus szabad választásokat abszolút többséggel (57%)?",
            "options": ["A Független Kisgazdapárt", "A Kommunista Párt", "A Szociáldemokrata Párt", "A Nemzeti Parasztpárt"],
            "correctIndex": 0,
            "explanation": "A Független Kisgazdapárt 57%-os abszolút többséget szerzett 1945-ben."
        }
    ]
)
write_json(STORIES_DIR / "story.b1.rakosikorszak.01.json", story_24_1)

voc_24_1 = {
    "id": "voc.b1.rakosikorszak.01",
    "title": "Az 1945-ös választások és köztársaság szókincse",
    "description": "Szabad választások, Kisgazdapárt, abszolút többség, köztársasági elnök és szovjet megszállás.",
    "entries": [
        {"lemma": "szabad választások", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "free democratic parliamentary elections held in November 1945", "examples": [{"hu": "Az 1945-ös szabad választásokon a polgári erők győztek.", "en": "In the 1945 free elections the civic forces won."}]}]},
        {"lemma": "Független Kisgazdapárt", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "agrarian civic democratic party winning 57% in 1945", "examples": [{"hu": "A Kisgazdapárt képviselte a polgári jövőt.", "en": "The Smallholders' Party represented the civic future."}]}]},
        {"lemma": "abszolút többség", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "more than half of total votes/seats", "examples": [{"hu": "A párt abszolút többséget szerzett a parlamentben.", "en": "The party won an absolute majority in parliament."}]}]},
        {"lemma": "köztársasági elnök", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "head of state of the Republic", "examples": [{"hu": "Tildy Zoltán lett az első köztársasági elnök.", "en": "Zoltán Tildy became the first President of the Republic."}]}]},
        {"lemma": "szovjet megszállás", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "post-war military occupation by the USSR Red Army", "examples": [{"hu": "A szovjet megszállás megbénította a demokráciát.", "en": "The Soviet occupation crippled democracy."}]}]}
    ]
}
write_json(VOCAB_DIR / "voc.b1.rakosikorszak.01.json", voc_24_1)

gr_24_1 = {
    "id": "gr.b1.rakosikorszak.01",
    "title": "Választási eredményeket és arányokat kifejező szerkezetek (többséget szerez, győzelmet arat, arányában)",
    "description": "Formulating election victories, vote shares, and parliamentary majority outcomes.",
    "rules": [
        {
            "explanation": "Választási folyamatok bemutatására: 'győzelmet arat a választásokon', 'abszolút többséget szerez a parlamentben', 'kikiáltják az új államformát'.",
            "examples": [
                {"spanish": "A Kisgazdapárt elsöprő győzelmet aratott a szavazatok 57%-ával.", "english": "The Smallholders' Party achieved an overwhelming victory with 57% of votes."},
                {"spanish": "1946-ban kikiáltották a köztársaságot.", "english": "In 1946 they proclaimed the republic."}
            ]
        }
    ]
}
write_json(GRAMMAR_DIR / "gr.b1.rakosikorszak.01.json", gr_24_1)

exs_24_1 = [
    {"id": "ex.b1.rakosikorszak.01.01", "type": "multiple-choice", "lesson": "lesson.b1.rakosikorszak.01", "teaches": ["1945-valasztas-gyoztes"], "prompt": "Melyik párt nyerte meg az 1945-ös szabad választásokat a szavazatok 57%-ával?", "options": ["A Független Kisgazdapárt", "A Kommunista Párt", "A Szociáldemokrata Párt", "A Nyilaskeresztes Párt"], "correctIndex": 0, "explanation": "A Független Kisgazdapárt aratott 57%-os abszolút győzelmet."},
    {"id": "ex.b1.rakosikorszak.01.02", "type": "fill-blank", "lesson": "lesson.b1.rakosikorszak.01", "teaches": ["szabad-valasztasokat"], "prompt": "Egészítsd ki a mondatot!", "sentence": "1945-ben demokratikus *szabad választásokat* tartottak.", "target": "szabad választásokat"},
    {"id": "ex.b1.rakosikorszak.01.03", "type": "sentence-builder", "lesson": "lesson.b1.rakosikorszak.01", "teaches": ["Tildy-Zoltan", "elnok"], "prompt": "Rakd össze a köztársaságról szóló mondatot!", "chips": ["Tildy", "Zoltán", "lett", "a", "második", "magyar", "köztársaság", "elnöke."], "target": "Tildy Zoltán lett a második magyar köztársaság elnöke.", "english": "Zoltán Tildy became the president of the Second Hungarian Republic."},
    {"id": "ex.b1.rakosikorszak.01.04", "type": "multiple-choice", "lesson": "lesson.b1.rakosikorszak.01", "teaches": ["koztarsasag-kikialtasa-1946"], "prompt": "Mikor kiáltotta ki a parlament a Magyar Köztársaságot a királyság helyett?", "options": ["1946. február 1-jén", "1945. április 4-én", "1949. augusztus 20-án", "1956. október 23-án"], "correctIndex": 0, "explanation": "1946. február 1-jén született meg a második magyar köztársaság."},
    {"id": "ex.b1.rakosikorszak.01.05", "type": "fill-blank", "lesson": "lesson.b1.rakosikorszak.01", "teaches": ["tobbseget"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A polgári erők abszolút *többséget* szereztek.", "target": "többséget"},
    {"id": "ex.b1.rakosikorszak.01.06", "type": "sentence-builder", "lesson": "lesson.b1.rakosikorszak.01", "teaches": ["szovjet", "megszallas"], "prompt": "Alkoss szabályos összetett mondatot!", "chips": ["A", "szovjet", "hadsereg", "megszállva", "tartotta", "az", "egész", "országot."], "target": "A szovjet hadsereg megszállva tartotta az egész országot.", "english": "The Soviet army kept the entire country under occupation."},
    {"id": "ex.b1.rakosikorszak.01.07", "type": "multiple-choice", "lesson": "lesson.b1.rakosikorszak.01", "teaches": ["SZEB-szerepe"], "prompt": "Mely szovjet vezetésű szerv irányította a magyar politikai életet a háttérből 1945 után?", "options": ["A Szövetséges Ellenőrző Bizottság (SZEB, Vorosilov marsall vezetésével)", "Az ENSZ Biztonsági Tanácsa", "A Vatikán", "A Nemzetközi Vöröskereszt"], "correctIndex": 0, "explanation": "A SZEB és a szovjet hadsereg döntő befolyást gyakorolt."},
    {"id": "ex.b1.rakosikorszak.01.08", "type": "fill-blank", "lesson": "lesson.b1.rakosikorszak.01", "teaches": ["koztarsasag"], "prompt": "Egészítsd ki a mondatot!", "sentence": "1946-ban az ország új államformája a *köztársaság* lett.", "target": "köztársaság"}
]
write_json(EXERCISES_DIR / "ex.b1.rakosikorszak.01.json", make_exercise_group("ex.b1.rakosikorszak.01", "Az 1945-ös választások gyakorlatok", "Gyakorlatok az 1945-ös szabad választásokról, a Kisgazdapártról, az 1946-os köztársaságról és a választási szerkezetekről.", exs_24_1))

lesson_24_1 = make_lesson(
    "lesson.b1.rakosikorszak.01",
    "Szovjet megszállás és az 1945-ös szabad választások",
    "Választási eredményeket kifejező szerkezetek (többséget szerez, győzelmet arat)",
    "Ismerjük meg az 1945-ös szabad választásokat, a Kisgazdapárt 57%-os győzelmét és az 1946-os köztársaságot.",
    ["Tudni az 1945-ös szabad választások eredményét (Kisgazdapárt győzelme 57%)", "Ismerni az 1946. február 1-i köztársaság kikiáltását (Tildy Zoltán)", "Használni a demokratikus választási eredményeket kifejező nyelvtani formákat"],
    "story.b1.rakosikorszak.01",
    "voc.b1.rakosikorszak.01",
    "gr.b1.rakosikorszak.01",
    "ex.b1.rakosikorszak.01",
    [e["id"] for e in exs_24_1]
)
write_json(LESSONS_DIR / "lesson.b1.rakosikorszak.01.json", lesson_24_1)


# Lesson 2: A szalámitaktika és a fordulat éve (1948)
story_24_2 = make_story(
    "story.b1.rakosikorszak.02",
    "A 'szalámitaktika' és a fordulat éve (1948)",
    "A szovjet szuronyok árnyékában a Magyar Kommunista Párt Rákosi Mátyás vezetésével 'szalámitaktikával' szeletenként semmisítette meg a demokratikus pártokat. 1948-ban, a fordulat évében létrejött az egypárti diktatúra.",
    "Budapest",
    ["Fokozatos felszámolást és politikai trükköket kifejező igék (szeletenként felszámol, bekebelez, ellehetetlenít, hatalmat ragad magához)", "Salami tactics, destruction of opposition, Year of the Turn 1948, MDP, and one-party dictatorship"],
    ["szalámitaktika", "Rákosi Mátyás", "fordulat éve", "Magyar Dolgozók Pártja", "egypártrendszer"],
    [
        "A választási vereség után a kommunisták szovjet támogatással magukhoz ragadták a belügyminisztériumot és az államvédelmet. Rákosi Mátyás kidolgozta a hírhedt 'szalámitaktikát': a nem kommunista pártokat belső ellentétek szításával, megfélemlítéssel, letartóztatásokkal és zsarolással szeletenként semmisítették meg.",
        "A Kisgazdapárt főtitkárát, Kovács Bélát 1947. február 25-én a szovjet hatóságok koholt vádakkal elhurcolták a Szovjetunióba, Nagy Ferenc miniszterelnököt pedig emigrációba kényszerítették. Az 1947-es 'kékcédulás' választásokon a kommunisták már tömeges csalással szereztek szavazatokat.",
        "1948 a 'fordulat éve' lett: a kommunista párt erőszakkal bekebelezte a Szociáldemokrata Pártot, létrehozva a Magyar Dolgozók Pártját (MDP). Megszűnt a többpártrendszer, és kiépült a totális sztálini diktatúra."
    ],
    [
        {"lemma": "szalámitaktika", "pos": "noun", "cefr": "B1", "gloss": "salami tactics (slicing away democratic opposition piece by piece)"},
        {"lemma": "fordulat éve", "pos": "noun", "cefr": "B1", "gloss": "'Year of the Turn' (1948, establishment of communist monopoly on power)"},
        {"lemma": "egypártrendszer", "pos": "noun", "cefr": "B1", "gloss": "one-party system"},
        {"lemma": "kékcédulás választás", "pos": "noun", "cefr": "B1", "gloss": "'blue slip' election (fraudulent 1947 election)"},
        {"lemma": "bekebelez", "pos": "verb", "cefr": "B1", "gloss": "to swallow up, forcefully absorb"}
    ],
    [
        {
            "question": "Hogyan nevezte Rákosi Mátyás a demokratikus pártok fokozatos, szeletenkénti megsemmisítésének módszerét?",
            "options": ["Szalámitaktikának", "Villámháborúnak", "Passzív ellenállásnak", "Kerekasztal-tárgyalásnak"],
            "correctIndex": 0,
            "explanation": "Rákosi a 'szalámitaktika' elnevezést használta az ellenzék felszámolására."
        }
    ]
)
write_json(STORIES_DIR / "story.b1.rakosikorszak.02.json", story_24_2)

voc_24_2 = {
    "id": "voc.b1.rakosikorszak.02",
    "title": "A szalámitaktika és hatalomátvétel szókincse",
    "description": "Szalámitaktika, fordulat éve, egypártrendszer, kékcédula és bekebelezés.",
    "entries": [
        {"lemma": "szalámitaktika", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "method of eliminating democratic opposition slice by slice", "examples": [{"hu": "A szalámitaktikával szétverték a Kisgazdapártot.", "en": "With salami tactics they smashed the Smallholders' Party."}]}]},
        {"lemma": "fordulat éve", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "year 1948 when communist single-party dictatorship was sealed", "examples": [{"hu": "1948 a fordulat éve volt Magyarországon.", "en": "1948 was the year of the turn in Hungary."}]}]},
        {"lemma": "egypártrendszer", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "dictatorial political system with only one legal party", "examples": [{"hu": "Felszámolták a többpártrendszert és egypártrendszer jött létre.", "en": "They abolished the multi-party system and a one-party system emerged."}]}]},
        {"lemma": "kékcédulás választás", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "1947 election rigged by communist mobile voters using blue voting slips", "examples": [{"hu": "A kékcédulás választásokon tömeges csalások történtek.", "en": "In the blue-slip elections mass fraud occurred."}]}]},
        {"lemma": "bekebelez", "pos": "verb", "cefr": "B1", "definitions": [{"meaning": "to absorb and eliminate an independent political organization", "examples": [{"hu": "A kommunisták bekebelezték a szociáldemokratákat.", "en": "The communists absorbed the social democrats."}]}]}
    ]
}
write_json(VOCAB_DIR / "voc.b1.rakosikorszak.02.json", voc_24_2)

gr_24_2 = {
    "id": "gr.b1.rakosikorszak.02",
    "title": "Fokozatosságot és befejezettséget kifejező határozók és igék (szeletenként, lépésről lépésre, felszámol)",
    "description": "Describing incremental processes, gradual erosion of democracy, and total destruction.",
    "rules": [
        {
            "explanation": "Fokozatos történelmi folyamatok leírására: 'lépésről lépésre', 'szeletenként számolták fel', 'fokozatosan építették ki a diktatúrát'.",
            "examples": [
                {"spanish": "A kommunisták lépésről lépésre számolták fel a demokráciát.", "english": "The communists eliminated democracy step by step."},
                {"spanish": "Szeletenként semmisítették meg a polgári pártokat.", "english": "They destroyed the civic parties slice by slice."}
            ]
        }
    ]
}
write_json(GRAMMAR_DIR / "gr.b1.rakosikorszak.02.json", gr_24_2)

exs_24_2 = [
    {"id": "ex.b1.rakosikorszak.02.01", "type": "multiple-choice", "lesson": "lesson.b1.rakosikorszak.02", "teaches": ["szalamitaktika-fogalom"], "prompt": "Mit jelentett a 'szalámitaktika' a kommunista hatalomátvétel idején?", "options": ["A demokratikus pártok fokozatos, szeletenkénti szétverését és megsemmisítését", "Húsipari fejlesztési programot", "Kereskedelmi szerződést Olaszországgal", "A mezőgazdasági export növelését"], "correctIndex": 0, "explanation": "A szalámitaktika az ellenzéki pártok módszeres megsemmisítése volt."},
    {"id": "ex.b1.rakosikorszak.02.02", "type": "fill-blank", "lesson": "lesson.b1.rakosikorszak.02", "teaches": ["szalamitaktikaval"], "prompt": "Egészítsd ki a mondatot!", "sentence": "Rákosi a hírhedt *szalámitaktikával* semmisítette meg ellenfeleit.", "target": "szalámitaktikával"},
    {"id": "ex.b1.rakosikorszak.02.03", "type": "sentence-builder", "lesson": "lesson.b1.rakosikorszak.02", "teaches": ["fordulat-eve-1948"], "prompt": "Rakd össze az 1948-as fordulatról szóló mondatot!", "chips": ["1948", "volt", "a", "kommunista", "fordulat", "éve", "Magyarországon."], "target": "1948 volt a kommunista fordulat éve Magyarországon.", "english": "1948 was the year of the communist turn in Hungary."},
    {"id": "ex.b1.rakosikorszak.02.04", "type": "multiple-choice", "lesson": "lesson.b1.rakosikorszak.02", "teaches": ["Kovacs-Bela-elhurcolas"], "prompt": "Kinek a szovjet elhurcolása (1947. február 25.) vált a kommunista diktatúrák áldozatainak emléknapjává?", "options": ["Kovács Bélának, a Kisgazdapárt főtitkárának", "Nagy Imrének", "Mindszenty Józsefnek", "Tildy Zoltánnak"], "correctIndex": 0, "explanation": "Kovács Béla 1947. február 25-i elhurcolása a Kommunizmus Áldozatainak Emléknapja."},
    {"id": "ex.b1.rakosikorszak.02.05", "type": "fill-blank", "lesson": "lesson.b1.rakosikorszak.02", "teaches": ["egypartrendszer"], "prompt": "Egészítsd ki a mondatot!", "sentence": "1948-ban kiépült a totális *egypártrendszer*.", "target": "egypártrendszer"},
    {"id": "ex.b1.rakosikorszak.02.06", "type": "sentence-builder", "lesson": "lesson.b1.rakosikorszak.02", "teaches": ["MDP-letrejotte"], "prompt": "Alkoss szabályos mondatot!", "chips": ["Létrejött", "a", "Magyar", "Dolgozók", "Pártja", "az", "egyetlen", "uralkodó", "pártként."], "target": "Létrejött a Magyar Dolgozók Pártja az egyetlen uralkodó pártként.", "english": "The Hungarian Working People's Party was established as the sole ruling party."},
    {"id": "ex.b1.rakosikorszak.02.07", "type": "multiple-choice", "lesson": "lesson.b1.rakosikorszak.02", "teaches": ["kekcedulas-valasztas-1947"], "prompt": "Milyen csalásról vált hírhedtté az 1947-es 'kékcédulás' választás?", "options": ["A kommunista szavazók kék cédulákkal teherautókkal járva több helyen is szavaztak", "Kék tintával írtak a szavazólapokra", "Kék zászlókat osztogattak", "Minden szavazatot kékre festettek"], "correctIndex": 0, "explanation": "A kék cédulákkal szervezett többszörös szavazással csaltak a kommunisták."},
    {"id": "ex.b1.rakosikorszak.02.08", "type": "fill-blank", "lesson": "lesson.b1.rakosikorszak.02", "teaches": ["bekebelezték"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A kommunisták erőszakkal *bekebelezték* a Szociáldemokrata Pártot.", "target": "bekebelezték"}
]
write_json(EXERCISES_DIR / "ex.b1.rakosikorszak.02.json", make_exercise_group("ex.b1.rakosikorszak.02", "A szalámitaktika gyakorlatok", "Gyakorlatok a szalámitaktikáról, az 1948-as fordulat évéről, Kovács Béla elhurcolásáról és a fokozatosság szerkezeteiről.", exs_24_2))

lesson_24_2 = make_lesson(
    "lesson.b1.rakosikorszak.02",
    "A 'szalámitaktika' és a fordulat éve (1948)",
    "Fokozatosságot kifejező szerkezetek (szeletenként, lépésről lépésre)",
    "Ismerjük meg Rákosi Mátyás szalámitaktikáját, a kékcédulás választást és az 1948-as fordulat évét.",
    ["Tudni a szalámitaktika fogalmát és a demokrácia felszámolásának lépéseit", "Ismerni az 1948-as fordulat évét és az MDP létrejöttét", "Használni a folyamatosságot és fokozatosságot kifejező határozókat"],
    "story.b1.rakosikorszak.02",
    "voc.b1.rakosikorszak.02",
    "gr.b1.rakosikorszak.02",
    "ex.b1.rakosikorszak.02",
    [e["id"] for e in exs_24_2]
)
write_json(LESSONS_DIR / "lesson.b1.rakosikorszak.02.json", lesson_24_2)


# Lesson 3: A személyi kultusz, a koncepciós perek és Mindszenty bíboros
story_24_3 = make_story(
    "story.b1.rakosikorszak.03",
    "Személyi kultusz és a koncepciós perek (Mindszenty József, Rajk László)",
    "Rákosi Mátyás Sztálin 'legjobb magyar tanítványaként' korlátlan személyi kultuszt épített ki. Koholt koncepciós perekben ítélték el Mindszenty József bíborost és végezték ki Rajk Lászlót.",
    "Andrássy út 60. (ÁVH) és bíróságok, Budapest",
    ["Koncepciós vádakat, személyi kultuszt és elítélést kifejező szerkezetek (koholt vádak alapján elítél, személyi kultuszt épít, börtönbüntetésre ítél)", "Personality cult of Rákosi, show trials, Mindszenty cardinal, and Rajk trial"],
    ["személyi kultusz", "koncepciós per", "Rákosi Mátyás", "Mindszenty József", "Rajk László"],
    [
        "Az 1949-es sztálini mintájú alkotmány bevezetésével Magyarország népköztársasággá vált. Rákosi Mátyás körül féktelen személyi kultusz alakult ki: 'a nép bölcs vezérének', 'Sztálin legjobb magyar tanítványának' és 'apánknak' kellett nevezni, arcképe minden iskolában és gyárban ott függött.",
        "A diktatúra a vélt és valós ellenségeket koholt 'koncepciós perekben' számolta fel, ahol a kínzással kicsikart hamis beismerő vallomások alapján előre megírt halálos vagy súlyos börtönítéleteket hoztak.",
        "1949-ben életfogytiglani börtönre ítélték Mindszenty József esztergomi érseket, hercegprímást, az egyház védelmezőjét. Még a saját elvtársaival is leszámolt a párt: Rajk László egykori belügyminisztert koholt vádakkal (hazaárulás, titóizmus) halálra ítélték és kivégezték."
    ],
    [
        {"lemma": "személyi kultusz", "pos": "noun", "cefr": "B1", "gloss": "cult of personality (adoration of dictator Rákosi)"},
        {"lemma": "koncepciós per", "pos": "noun", "cefr": "B1", "gloss": "show trial, staged trial with fabricated charges"},
        {"lemma": "koholt vád", "pos": "noun", "cefr": "B1", "gloss": "fabricated, trumped-up charge"},
        {"lemma": "hercegprímás", "pos": "noun", "cefr": "B1", "gloss": "Prince Primate (Cardinal Archbishop of Esztergom, Mindszenty)"},
        {"lemma": "kicsikart vallomás", "pos": "noun", "cefr": "B1", "gloss": "confession extorted under torture"}
    ],
    [
        {
            "question": "Melyik bátor egyházi vezetőt ítélte életfogytiglani börtönre a Rákosi-diktatúra koholt koncepciós perben 1949-ben?",
            "options": ["Mindszenty József bíborost, esztergomi érseket", "Pázmány Pétert", "Bakócz Tamást", "Károli Gáspárt"],
            "correctIndex": 0,
            "explanation": "Mindszenty József hercegprímást koncepciós perben ítélték el 1949-ben."
        }
    ]
)
write_json(STORIES_DIR / "story.b1.rakosikorszak.03.json", story_24_3)

voc_24_3 = {
    "id": "voc.b1.rakosikorszak.03",
    "title": "A személyi kultusz és koncepciós perek szókincse",
    "description": "Személyi kultusz, koncepciós per, koholt vád, hercegprímás és Mindszenty József.",
    "entries": [
        {"lemma": "személyi kultusz", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "unquestioning adoration of totalitarian leader Rákosi", "examples": [{"hu": "A személyi kultusz kötelező dicsőítést követelt.", "en": "The cult of personality demanded mandatory praise."}]}]},
        {"lemma": "koncepciós per", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "staged trial with predetermined guilty verdict based on forced confessions", "examples": [{"hu": "A koncepciós perekben ártatlanokat ítéltek el.", "en": "In show trials innocent people were sentenced."}]}]},
        {"lemma": "koholt vád", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "invented, fabricated accusation without factual basis", "examples": [{"hu": "Koholt vádak alapján tartóztatták le a papokat.", "en": "Priests were arrested on trumped-up charges."}]}]},
        {"lemma": "hercegprímás", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "title of the head of the Catholic Church in Hungary", "examples": [{"hu": "Mindszenty hercegprímás bátor ellenállást tanúsított.", "en": "Prince Primate Mindszenty showed brave resistance."}]}]},
        {"lemma": "kicsikart vallomás", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "confession obtained through brutal physical and mental torture", "examples": [{"hu": "Kínzással kicsikart vallomásokra támaszkodtak.", "en": "They relied on confessions extorted through torture."}]}]}
    ]
}
write_json(VOCAB_DIR / "voc.b1.rakosikorszak.03.json", voc_24_3)

gr_24_3 = {
    "id": "gr.b1.rakosikorszak.03",
    "title": "Kényszerítésen alapuló és jogi szerkezetek (alapján ítél el, bűnösnek nyilvánít, kényszerít)",
    "description": "Expressing judicial abuse, forced confessions, and totalitarian injustice.",
    "rules": [
        {
            "explanation": "Jogtalanságok és perek leírására az 'alapján ítél el' (koholt vádak alapján), 'halálra ítél vkit', 'kicsikar vmit' vonzatokat alkalmazzuk.",
            "examples": [
                {"spanish": "Mindszenty Józsefet koholt vádak alapján börtönre ítélték.", "english": "József Mindszenty was sentenced to prison on fabricated charges."},
                {"spanish": "Rajk Lászlót koncepciós perben kivégezték.", "english": "László Rajk was executed in a show trial."}
            ]
        }
    ]
}
write_json(GRAMMAR_DIR / "gr.b1.rakosikorszak.03.json", gr_24_3)

exs_24_3 = [
    {"id": "ex.b1.rakosikorszak.03.01", "type": "multiple-choice", "lesson": "lesson.b1.rakosikorszak.03", "teaches": ["Mindszenty-per-1949"], "prompt": "Mikor ítélték el Mindszenty József bíborost koncepciós perben?", "options": ["1949-ben", "1945-ben", "1956-ban", "1968-ban"], "correctIndex": 0, "explanation": "Mindszenty József bíboros pere 1949-ben zajlott."},
    {"id": "ex.b1.rakosikorszak.03.02", "type": "fill-blank", "lesson": "lesson.b1.rakosikorszak.03", "teaches": ["koncepcios-perben"], "prompt": "Egészítsd ki a mondatot!", "sentence": "Mindszenty Józsefet koholt *koncepciós perben* ítélték el.", "target": "koncepciós perben"},
    {"id": "ex.b1.rakosikorszak.03.03", "type": "sentence-builder", "lesson": "lesson.b1.rakosikorszak.03", "teaches": ["szemelyi-kultusz", "Rakosi"], "prompt": "Rakd össze a diktatúrát leíró mondatot!", "chips": ["Rákosi", "Mátyás", "körül", "hatalmas", "személyi", "kultusz", "alakult", "ki."], "target": "Rákosi Mátyás körül hatalmas személyi kultusz alakult ki.", "english": "An enormous cult of personality developed around Mátyás Rákosi."},
    {"id": "ex.b1.rakosikorszak.03.04", "type": "multiple-choice", "lesson": "lesson.b1.rakosikorszak.03", "teaches": ["Rajk-Laszlo-kivegzes"], "prompt": "Melyik korábbi kommunista belügyminisztert végezték ki koncepciós perben 1949 őszén?", "options": ["Rajk Lászlót", "Kádár Jánost", "Nagy Imrét", "Gerő Ernőt"], "correctIndex": 0, "explanation": "Rajk Lászlót a belső párttisztogatások során végezték ki 1949-ben."},
    {"id": "ex.b1.rakosikorszak.03.05", "type": "fill-blank", "lesson": "lesson.b1.rakosikorszak.03", "teaches": ["szemelyi-kultusz"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A kötelező *személyi kultusz* a vezér imádatát írta elő.", "target": "személyi kultusz"},
    {"id": "ex.b1.rakosikorszak.03.06", "type": "sentence-builder", "lesson": "lesson.b1.rakosikorszak.03", "teaches": ["koholt-vadak", "eliteltek"], "prompt": "Alkoss szabályos összetett mondatot!", "chips": ["Ártatlan", "emberek", "ezreit", "ítélték", "el", "koholt", "vádak", "alapján."], "target": "Ártatlan emberek ezreit ítélték el koholt vádak alapján.", "english": "Thousands of innocent people were sentenced based on fabricated charges."},
    {"id": "ex.b1.rakosikorszak.03.07", "type": "multiple-choice", "lesson": "lesson.b1.rakosikorszak.03", "teaches": ["1949-alkotmany-sztalintípusú"], "prompt": "Milyen jellegű volt Magyarország 1949. augusztus 20-án elfogadott új alkotmánya?", "options": ["Szovjet (sztálini) mintájú egypárti alkotmány", "Demokratikus polgári alkotmány", "Királysági törvénykönyv", "Az 1848-as áprilisi törvények másolata"], "correctIndex": 0, "explanation": "Az 1949-es alkotmány szovjet mintára rögzítette a proletárdiktatúrát."},
    {"id": "ex.b1.rakosikorszak.03.08", "type": "fill-blank", "lesson": "lesson.b1.rakosikorszak.03", "teaches": ["hercegprimas"], "prompt": "Egészítsd ki a mondatot!", "sentence": "Mindszenty József *hercegprímás* nem hódolt be a kommunistáknak.", "target": "hercegprímás"}
]
write_json(EXERCISES_DIR / "ex.b1.rakosikorszak.03.json", make_exercise_group("ex.b1.rakosikorszak.03", "Személyi kultusz és perek gyakorlatok", "Gyakorlatok a személyi kultuszról, a koncepciós perekről, Mindszenty Józsefről és a jogi igék vonzatairól.", exs_24_3))

lesson_24_3 = make_lesson(
    "lesson.b1.rakosikorszak.03",
    "Személyi kultusz és a koncepciós perek (Mindszenty József, Rajk László)",
    "Kényszerítésen alapuló szerkezetek (koholt vádak alapján elítél)",
    "Ismerjük meg Rákosi Mátyás személyi kultuszát, a koncepciós pereket és Mindszenty bíboros helytállását.",
    ["Tudni a személyi kultusz és a koncepciós perek fogalmát és működését", "Ismerni Mindszenty József hercegprímás (1949) és Rajk László perét", "Használni a vádakat, ítéleteket és totalitárius elnyomást kifejező nyelvtani szerkezeteket"],
    "story.b1.rakosikorszak.03",
    "voc.b1.rakosikorszak.03",
    "gr.b1.rakosikorszak.03",
    "ex.b1.rakosikorszak.03",
    [e["id"] for e in exs_24_3]
)
write_json(LESSONS_DIR / "lesson.b1.rakosikorszak.03.json", lesson_24_3)


# Lesson 4: Az ÁVH terrorja, Recsk és a kitelepítések
story_24_4 = make_story(
    "story.b1.rakosikorszak.04",
    "Az ÁVH rémuralma, a recski haláltábor és a kitelepítések",
    "Az Államvédelmi Hatóság (ÁVH) Péter Gábor vezetésével az Andrássy út 60.-ban kínzókamrákat rendezett be. Recsken kényszermunkatábort működtettek, Budapestről pedig tízezreket telepítettek ki a Hortobágyra.",
    "Andrássy út 60. (Terror Háza), Recsk és Hortobágy",
    ["Megfélemlítést, internálást és kényszermunkát kifejező igék (internál, kitelepít, kényszermunkára kényszerít, megkínoz)", "ÁVH secret police terror, Recsk labor camp, deportations to Hortobágy, and class enemies"],
    ["ÁVH", "Terror Háza", "Recsk", "kényszermunkatábor", "kitelepítés"],
    [
        "Az Államvédelmi Hatóság (ÁVH) – a hírhedt 'fekete autó' és a bőrkabátos titkosrendőrök szervezete – a diktatúra legfőbb fegyvere volt. Főhadiszállásukon, a budapesti Andrássy út 60. alatti pincékben (ma a Terror Háza Múzeum) válogatott kínzásokkal törtek meg tízezreket.",
        "A Mátra lábánál, Recsken hozták létre a legszigorúbb titkos kényszermunkatábort ('a magyar Gulag'), ahol kőbányában, embertelen körülmények között, éheztetve dolgoztatták az ország szellemi, polgári és politikai elitjét ítélet nélkül.",
        "1951-ben Budapestről több mint 13 ezer 'osztályidegennek' bélyegzett polgárt – volt arisztokratákat, tisztviselőket, gyárosokat – telepítettek ki egyetlen éjszaka alatt a Hortobágy zárt munkatáboraiba, elrabolva minden vagyonukat és lakásukat."
    ],
    [
        {"lemma": "ÁVH", "pos": "noun", "cefr": "B1", "gloss": "State Protection Authority (Államvédelmi Hatóság, secret police)"},
        {"lemma": "kényszermunkatábor", "pos": "noun", "cefr": "B1", "gloss": "forced labor camp (e.g. Recsk)"},
        {"lemma": "kitelepítés", "pos": "noun", "cefr": "B1", "gloss": "forced internal deportation (to Hortobágy)"},
        {"lemma": "osztályidegen", "pos": "noun", "cefr": "B1", "gloss": "'class enemy' (bourgeois, noble, official)"},
        {"lemma": "internálás", "pos": "noun", "cefr": "B1", "gloss": "internment without trial"}
    ],
    [
        {
            "question": "Melyik településen működött a leghíresebb és legkegyetlenebb magyarországi kényszermunkatábor (a 'magyar Gulag')?",
            "options": ["Recsken (a Mátra lábánál)", "Siófokon", "Esztergomban", "Sopronban"],
            "correctIndex": 0,
            "explanation": "A recski kényszermunkatáborban bírósági ítélet nélkül dolgoztatták a rabokat."
        }
    ]
)
write_json(STORIES_DIR / "story.b1.rakosikorszak.04.json", story_24_4)

voc_24_4 = {
    "id": "voc.b1.rakosikorszak.04",
    "title": "Az ÁVH, Recsk és kitelepítések szókincse",
    "description": "ÁVH, Recsk, kényszermunkatábor, kitelepítés és osztályidegen.",
    "entries": [
        {"lemma": "ÁVH", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "brutal communist secret police organization", "examples": [{"hu": "Az ÁVH éjjelente hurcolta el az embereket.", "en": "The ÁVH dragged people away at night."}]}]},
        {"lemma": "kényszermunkatábor", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "secret forced labor camp like Recsk", "examples": [{"hu": "A recski kényszermunkatábor a terror jelképe.", "en": "The Recsk forced labor camp is a symbol of terror."}]}]},
        {"lemma": "kitelepítés", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "forced deportation of families to rural detention", "examples": [{"hu": "Családok ezreit sújtotta a kitelepítés.", "en": "Thousands of families were struck by forced deportation."}]}]},
        {"lemma": "osztályidegen", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "ideological label for bourgeois or former landowners", "examples": [{"hu": "Osztályidegennek bélyegezték a polgári családokat.", "en": "They branded bourgeois families as class enemies."}]}]},
        {"lemma": "internálás", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "confinement to a camp without judicial trial", "examples": [{"hu": "Az internálás bírósági ítélet nélkül történt.", "en": "Internment took place without a court trial."}]}]}
    ]
}
write_json(VOCAB_DIR / "voc.b1.rakosikorszak.04.json", voc_24_4)

gr_24_4 = {
    "id": "gr.b1.rakosikorszak.04",
    "title": "Kényszerű elhurcolást és megbélyegzést kifejező szerkezetek (vmivé bélyegez, kitelepít vhová, elhurcol)",
    "description": "Formulations describing state terror, arbitrary arrests, and ideological stigmatization.",
    "rules": [
        {
            "explanation": "Diktatórikus megbélyegzés és kényszer leírása: 'osztályidegennek bélyegez vkit', 'kitelepíti a családokat a Hortobágyra', 'kényszermunkára kényszerít'.",
            "examples": [
                {"spanish": "Tízezreket bélyegeztek osztályidegennek és telepítettek ki.", "english": "Tens of thousands were branded class enemies and deported."},
                {"spanish": "A rabokat a recski kőbányába hurcolták.", "english": "The prisoners were dragged to the Recsk stone quarry."}
            ]
        }
    ]
}
write_json(GRAMMAR_DIR / "gr.b1.rakosikorszak.04.json", gr_24_4)

exs_24_4 = [
    {"id": "ex.b1.rakosikorszak.04.01", "type": "multiple-choice", "lesson": "lesson.b1.rakosikorszak.04", "teaches": ["Recsk-kenyszermunkatabor"], "prompt": "Melyik hírhedt kényszermunkatábor működött a Mátra lábánál 1950 és 1953 között?", "options": ["A recski kényszermunkatábor", "A siófoki tábor", "A visegrádi vár", "A debreceni laktanya"], "correctIndex": 0, "explanation": "Recsk volt a leghírhedtebb magyar kényszermunkatábor."},
    {"id": "ex.b1.rakosikorszak.04.02", "type": "fill-blank", "lesson": "lesson.b1.rakosikorszak.04", "teaches": ["kenyszermunkatabor"], "prompt": "Egészítsd ki a mondatot!", "sentence": "Recsken titkos *kényszermunkatábor* működött.", "target": "kényszermunkatábor"},
    {"id": "ex.b1.rakosikorszak.04.03", "type": "sentence-builder", "lesson": "lesson.b1.rakosikorszak.04", "teaches": ["Andrassy-ut-60", "AVH"], "prompt": "Rakd össze a mondatot!", "chips": ["Az", "Andrássy", "út", "60.", "alatt", "volt", "az", "ÁVH", "rémisztő", "központja."], "target": "Az Andrássy út 60. alatt volt az ÁVH rémisztő központja.", "english": "At 60 Andrássy Avenue was the terrifying headquarters of the ÁVH."},
    {"id": "ex.b1.rakosikorszak.04.04", "type": "multiple-choice", "lesson": "lesson.b1.rakosikorszak.04", "teaches": ["kitelepitesek-Hortobagy"], "prompt": "Hová telepítettek ki több mint 13 ezer budapesti polgárt 1951-ben?", "options": ["A Hortobágy zárt munkatáboraiba", "A Balaton partjára", "A Tátrába", "Külföldi szigetekre"], "correctIndex": 0, "explanation": "A Hortobágyra telepítették ki a megbélyegzett polgári családokat."},
    {"id": "ex.b1.rakosikorszak.04.05", "type": "fill-blank", "lesson": "lesson.b1.rakosikorszak.04", "teaches": ["osztalyidegennek"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A polgárokat megbízhatatlan *osztályidegennek* bélyegezték.", "target": "osztályidegennek"},
    {"id": "ex.b1.rakosikorszak.04.06", "type": "sentence-builder", "lesson": "lesson.b1.rakosikorszak.04", "teaches": ["kitelepites", "csaladok"], "prompt": "Alkoss szabályos összetett mondatot!", "chips": ["Egyetlen", "éjszaka", "alatt", "több", "ezer", "családot", "telepítettek", "ki."], "target": "Egyetlen éjszaka alatt több ezer családot telepítettek ki.", "english": "In a single night, several thousand families were deported."},
    {"id": "ex.b1.rakosikorszak.04.07", "type": "multiple-choice", "lesson": "lesson.b1.rakosikorszak.04", "teaches": ["Terror-Haza-Muzeum"], "prompt": "Melyik múzeum működik ma az egykori ÁVH főhadiszállás épületében (Andrássy út 60.)?", "options": ["A Terror Háza Múzeum", "A Szépművészeti Múzeum", "A Nemzeti Galéria", "A Közlekedési Múzeum"], "correctIndex": 0, "explanation": "A Terror Háza Múzeum állít emléket az áldozatoknak."},
    {"id": "ex.b1.rakosikorszak.04.08", "type": "fill-blank", "lesson": "lesson.b1.rakosikorszak.04", "teaches": ["kitelepites"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A jogtalan *kitelepítés* életeket tett tönkre.", "target": "kitelepítés"}
]
write_json(EXERCISES_DIR / "ex.b1.rakosikorszak.04.json", make_exercise_group("ex.b1.rakosikorszak.04", "Az ÁVH és Recsk gyakorlatok", "Gyakorlatok az ÁVH-ról, a recski kényszermunkatáborról, a hortobágyi kitelepítésekről és a megbélyegzés szerkezeteiről.", exs_24_4))

lesson_24_4 = make_lesson(
    "lesson.b1.rakosikorszak.04",
    "Az ÁVH rémuralma, a recski haláltábor és a kitelepítések",
    "Kényszerű megbélyegzést kifejező szerkezetek (osztályidegennek bélyegez, kitelepít)",
    "Ismerjük meg az ÁVH titkosrendőrségét, a recski kényszermunkatábort és a hortobágyi kitelepítéseket.",
    ["Tudni az ÁVH és az Andrássy út 60. (Terror Háza) történelmi szerepét", "Ismerni a recski haláltábor és a hortobágyi kitelepítések áldozatait", "Használni a megbélyegzést és kényszerű elhurcolást leíró nyelvtani formákat"],
    "story.b1.rakosikorszak.04",
    "voc.b1.rakosikorszak.04",
    "gr.b1.rakosikorszak.04",
    "ex.b1.rakosikorszak.04",
    [e["id"] for e in exs_24_4]
)
write_json(LESSONS_DIR / "lesson.b1.rakosikorszak.04.json", lesson_24_4)


# Lesson 5: Erőltetett iparosítás, téeszesítés és padlássöprések
story_24_5 = make_story(
    "story.b1.rakosikorszak.05",
    "A 'vas és acél országa', a téeszesítés és a padlássöprések",
    "A Rákosi-korszakban tervgazdálkodást vezettek be: Magyarországból a 'vas és acél országát' akarták formálni. A parasztságot erőszakkal termelőszövetkezetekbe (téesz) kényszerítették, a kulákokat pedig padlássöpréssel fosztották ki.",
    "Sztálinváros (Dunaújváros) és vidéki falvak",
    ["Gazdasági kényszert, rekvirálást és elvonást kifejező igék (begyűjt, téeszbe kényszerít, padlást söpör, kuláknak bélyegez)", "Heavy industrialization, iron & steel country, collectivization, kulaks, and sweeping the attics"],
    ["vas és acél országa", "tervgazdálkodás", "téeszesítés", "kulák", "padlássöprés"],
    [
        "A gazdaságban szovjet típusú tervgazdálkodást (ötéves terveket) vezettek be. Rákosi meghirdette, hogy Magyarországot 'a vas és acél országává' kell tenni, holott sem vasérc, sem elegendő szén nem állt rendelkezésre. Hatalmas pénzeket öltek a nehéziparba (Sztálinváros felépítése), miközben a lakosság életszínvonala drasztikusan zuhant.",
        "A falvakban megindult a kollektivizálás, a mezőgazdaság erőszakos téeszesítése (termelőszövetkezetek alapítása). A gazdákat fenyegetéssel kényszerítették földjeik és állataik beadására a közösbe.",
        "A jómódúbb parasztokat megbélyegezték: ők lettek a 'kulákok', akiket listára tettek és üldöztek. A kötelező beszolgáltatás jegyében a hatóságok 'padlássöprést' tartottak: még a vetőmagot és a család utolsó falat élelmét is elrekvirálták."
    ],
    [
        {"lemma": "vas és acél országa", "pos": "noun", "cefr": "B1", "gloss": "'country of iron and steel' (unrealistic heavy industry slogan)"},
        {"lemma": "tervgazdálkodás", "pos": "noun", "cefr": "B1", "gloss": "planned economy, five-year plans"},
        {"lemma": "téeszesítés", "pos": "noun", "cefr": "B1", "gloss": "forced collectivization into cooperatives (Tsz)"},
        {"lemma": "kulák", "pos": "noun", "cefr": "B1", "gloss": "kulak (pejorative term for wealthier independent peasant)"},
        {"lemma": "padlássöprés", "pos": "noun", "cefr": "B1", "gloss": "'sweeping the attic' (brutal total confiscation of grain/food)"}
    ],
    [
        {
            "question": "Hogyan nevezték a parasztok élelmének és vetőmagjának erőszakos, teljes elkobzását a beszolgáltatáskor?",
            "options": ["Padlássöprésnek", "Betakarításnak", "Vámvizsgálatnak", "Piacnyitásnak"],
            "correctIndex": 0,
            "explanation": "A padlássöprés során az utolsó szem gabonát is elvitték a parasztoktól."
        }
    ]
)
write_json(STORIES_DIR / "story.b1.rakosikorszak.05.json", story_24_5)

voc_24_5 = {
    "id": "voc.b1.rakosikorszak.05",
    "title": "A tervgazdálkodás és téeszesítés szókincse",
    "description": "Vas és acél országa, tervgazdálkodás, téeszesítés, kulák és padlássöprés.",
    "entries": [
        {"lemma": "vas és acél országa", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "dogmatic slogan to build heavy metallurgy without natural resources", "examples": [{"hu": "A vas és acél országa irracionális gazdasági cél volt.", "en": "The country of iron and steel was an irrational economic goal."}]}]},
        {"lemma": "tervgazdálkodás", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "centrally directed socialist planned economy", "examples": [{"hu": "Az ötéves tervgazdálkodás hiánygazdasághoz vezetett.", "en": "Five-year planned economy led to a shortage economy."}]}]},
        {"lemma": "téeszesítés", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "forced collectivization of agriculture into cooperatives", "examples": [{"hu": "Erőszakos téeszesítés zajlott a falvakban.", "en": "Forced collectivization took place in the villages."}]}]},
        {"lemma": "kulák", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "stigmatized wealthy peasant targeted by class warfare", "examples": [{"hu": "A kuláklistára került gazdákat börtön fenyegette.", "en": "Farmers placed on kulak lists faced imprisonment."}]}]},
        {"lemma": "padlássöprés", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "brutal confiscation of grain down to the last grain in attics", "examples": [{"hu": "A padlássöprések éhezésbe taszították a falvakat.", "en": "The attic sweeps plunged the villages into starvation."}]}]}
    ]
}
write_json(VOCAB_DIR / "voc.b1.rakosikorszak.05.json", voc_24_5)

gr_24_5 = {
    "id": "gr.b1.rakosikorszak.05",
    "title": "Kényszerű elvonást és beszolgáltatást kifejező szerkezetek (elkoboz vmit vkitől, beszolgáltatásra kötelez)",
    "description": "Expressing forced state requisitions, compulsory deliveries, and economic expropriation.",
    "rules": [
        {
            "explanation": "Állami elvonások és kényszer leírására: 'beszolgáltatásra kötelez vkit', 'elkobozza az élelmet a parasztoktól', 'téeszbe kényszeríti a gazdákat'.",
            "examples": [
                {"spanish": "A parasztokat kötelező beszolgáltatásra kényszerítették.", "english": "Peasants were forced into compulsory crop delivery."},
                {"spanish": "Az utolsó szem gabonát is elrekvirálták a padlásokról.", "english": "Even the last grain of corn was requisitioned from the attics."}
            ]
        }
    ]
}
write_json(GRAMMAR_DIR / "gr.b1.rakosikorszak.05.json", gr_24_5)

exs_24_5 = [
    {"id": "ex.b1.rakosikorszak.05.01", "type": "multiple-choice", "lesson": "lesson.b1.rakosikorszak.05", "teaches": ["vas-es-acel-orszaga-szlogan"], "prompt": "Milyen országgá akarta alakítani Magyarországot a Rákosi-kormány az erőltetett nehéziparosítással?", "options": ["'A vas és acél országává'", "'A virágok földjévé'", "'A világ bankjává'", "'A zöld erdők országává'"], "correctIndex": 0, "explanation": "'A vas és acél országa' volt a hivatalos dogmatikus jelszó."},
    {"id": "ex.b1.rakosikorszak.05.02", "type": "fill-blank", "lesson": "lesson.b1.rakosikorszak.05", "teaches": ["padlassopres"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A falvakban mindennapossá vált az erőszakos *padlássöprés*.", "target": "padlássöprés"},
    {"id": "ex.b1.rakosikorszak.05.03", "type": "sentence-builder", "lesson": "lesson.b1.rakosikorszak.05", "teaches": ["teeszbe-kenyszeritettek", "parasztsag"], "prompt": "Rakd össze a kollektivizálást leíró mondatot!", "chips": ["A", "parasztokat", "erőszakkal", "termelőszövetkezetbe", "(téeszbe)", "kényszerítették."], "target": "A parasztokat erőszakkal termelőszövetkezetbe (téeszbe) kényszerítették.", "english": "The peasants were forcefully coerced into cooperatives (Tsz)."},
    {"id": "ex.b1.rakosikorszak.05.04", "type": "multiple-choice", "lesson": "lesson.b1.rakosikorszak.05", "teaches": ["kulak-fogalom"], "prompt": "Kiket bélyegeztek 'kuláknak' és üldöztek a falvakban?", "options": ["A jómódúbb, önállóan gazdálkodó parasztokat", "A traktorvezetőket", "A pékeket", "A katonákat"], "correctIndex": 0, "explanation": "A kulákok a megbélyegzett és üldözött önálló gazdák voltak."},
    {"id": "ex.b1.rakosikorszak.05.05", "type": "fill-blank", "lesson": "lesson.b1.rakosikorszak.05", "teaches": ["kulaknak"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A vagyonosabb gazdát ellenséges *kuláknak* nyilvánították.", "target": "kuláknak"},
    {"id": "ex.b1.rakosikorszak.05.06", "type": "sentence-builder", "lesson": "lesson.b1.rakosikorszak.05", "teaches": ["beszolgaltatas", "gabona"], "prompt": "Alkoss szabályos mondatot!", "chips": ["A", "kötelező", "beszolgáltatás", "során", "elvitték", "az", "utolsó", "gabonát."], "target": "A kötelező beszolgáltatás során elvitték az utolsó gabonát.", "english": "During compulsory delivery they took away the last grain."},
    {"id": "ex.b1.rakosikorszak.05.07", "type": "multiple-choice", "lesson": "lesson.b1.rakosikorszak.05", "teaches": ["Sztalinvalidas-Dunaújváros"], "prompt": "Melyik új szocialista iparvárost építették fel a semmiből a nehézipar központjaként?", "options": ["Sztálinvárost (a mai Dunaújvárost)", "Siófokot", "Esztergomot", "Sopront"], "correctIndex": 0, "explanation": "Sztálinváros (Dunaújváros) volt a szocialista nehézipar szimbóluma."},
    {"id": "ex.b1.rakosikorszak.05.08", "type": "fill-blank", "lesson": "lesson.b1.rakosikorszak.05", "teaches": ["tervgazdalkodas"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A szocialista *tervgazdálkodás* súlyos hiányt idézett elő.", "target": "tervgazdálkodás"}
]
write_json(EXERCISES_DIR / "ex.b1.rakosikorszak.05.json", make_exercise_group("ex.b1.rakosikorszak.05", "A tervgazdálkodás és padlássöprés gyakorlatok", "Gyakorlatok a nehéziparosításról, a téeszesítésről, a kulákokról, a padlássöprésről és a gazdasági kényszer igéiről.", exs_24_5))

lesson_24_5 = make_lesson(
    "lesson.b1.rakosikorszak.05",
    "A 'vas és acél országa', a téeszesítés és a padlássöprések",
    "Kényszerű elvonást kifejező szerkezetek (beszolgáltatásra kötelez, elkoboz)",
    "Ismerjük meg a Rákosi-korszak gazdasági elnyomását: a tervgazdálkodást, a téeszesítést, a kuláküldözést és a padlássöpréseket.",
    ["Tudni a 'vas és acél országa' doktrína és a tervgazdálkodás kudarcát", "Ismerni a téeszesítést, a kulákok megbélyegzését és a padlássöprést", "Használni a kényszerű elvonást és elkobzást kifejező nyelvtani formákat"],
    "story.b1.rakosikorszak.05",
    "voc.b1.rakosikorszak.05",
    "gr.b1.rakosikorszak.05",
    "ex.b1.rakosikorszak.05",
    [e["id"] for e in exs_24_5]
)
write_json(LESSONS_DIR / "lesson.b1.rakosikorszak.05.json", lesson_24_5)


# Unit 24 Consolidation
cons_24_exs = [
    {"id": "ex.b1.rakosikorszak.cons.01", "type": "multiple-choice", "lesson": "lesson.b1.rakosikorszak.consolidation", "teaches": ["1945-valasztas-eredmeny"], "prompt": "Melyik párt nyerte meg az 1945-ös szabad választásokat abszolút többséggel (57%)?", "options": ["A Független Kisgazdapárt", "A Kommunista Párt", "A Szociáldemokrata Párt", "A Nemzeti Parasztpárt"], "correctIndex": 0, "explanation": "A Kisgazdapárt 57%-os győzelmet aratott."},
    {"id": "ex.b1.rakosikorszak.cons.02", "type": "fill-blank", "lesson": "lesson.b1.rakosikorszak.consolidation", "teaches": ["Tildy-Zoltan"], "prompt": "1946-ban *Tildy Zoltán* lett az új köztársaság első elnöke.", "sentence": "1946-ban *Tildy Zoltán* lett az új köztársaság első elnöke.", "target": "Tildy Zoltán"},
    {"id": "ex.b1.rakosikorszak.cons.03", "type": "multiple-choice", "lesson": "lesson.b1.rakosikorszak.consolidation", "teaches": ["szalamitaktika-lenyege"], "prompt": "Mi volt a Rákosi-féle 'szalámitaktika' célja?", "options": ["A demokratikus pártok szeletenkénti, fokozatos megsemmisítése", "Húsboltok nyitása", "Mezőgazdasági export", "Vasútépítés"], "correctIndex": 0, "explanation": "A szalámitaktika a többpártrendszer felszámolására szolgált."},
    {"id": "ex.b1.rakosikorszak.cons.04", "type": "fill-blank", "lesson": "lesson.b1.rakosikorszak.consolidation", "teaches": ["fordulat-eve"], "prompt": "1948 volt a kommunista diktatúra kiépülésének *fordulat éve*.", "sentence": "1948 volt a kommunista diktatúra kiépülésének *fordulat éve*.", "target": "fordulat éve"},
    {"id": "ex.b1.rakosikorszak.cons.05", "type": "sentence-builder", "lesson": "lesson.b1.rakosikorszak.consolidation", "teaches": ["Kovacs-Bela", "elhurcoltak"], "prompt": "Rakd össze a mondatot!", "chips": ["1947-ben", "Kovács", "Bélát", "koholt", "vádakkal", "a", "Szovjetunióba", "hurcolták."], "target": "1947-ben Kovács Bélát koholt vádakkal a Szovjetunióba hurcolták.", "english": "In 1947, Béla Kovács was dragged to the Soviet Union on fabricated charges."},
    {"id": "ex.b1.rakosikorszak.cons.06", "type": "multiple-choice", "lesson": "lesson.b1.rakosikorszak.consolidation", "teaches": ["Mindszenty-Jozsef-elitelese"], "prompt": "Melyik bíborost ítélték el koholt koncepciós perben 1949-ben?", "options": ["Mindszenty József hercegprímást", "Rajk Lászlót", "Kossuth Lajost", "Széchenyi Istvánt"], "correctIndex": 0, "explanation": "Mindszenty József bíborost életfogytiglani börtönre ítélték."},
    {"id": "ex.b1.rakosikorszak.cons.07", "type": "fill-blank", "lesson": "lesson.b1.rakosikorszak.consolidation", "teaches": ["koncepcios-perekben"], "prompt": "A diktatúra *koncepciós perekben* számolt le politikai ellenfeleivel.", "sentence": "A diktatúra *koncepciós perekben* számolt le politikai ellenfeleivel.", "target": "koncepciós perekben"},
    {"id": "ex.b1.rakosikorszak.cons.08", "type": "sentence-builder", "lesson": "lesson.b1.rakosikorszak.consolidation", "teaches": ["szemelyi-kultusz", "Rakosi"], "prompt": "Alkoss szabályos összetett mondatot!", "chips": ["Rákosi", "Mátyás", "a", "nép", "bölcs", "vezérének", "neveztette", "magát."], "target": "Rákosi Mátyás a nép bölcs vezérének neveztette magát.", "english": "Mátyás Rákosi had himself called the wise leader of the people."},
    {"id": "ex.b1.rakosikorszak.cons.09", "type": "multiple-choice", "lesson": "lesson.b1.rakosikorszak.cons.09", "teaches": ["AVH-Andrassy-60"], "prompt": "Hol volt az ÁVH rettegett központja és kínzókamrája Budapesten?", "options": ["Az Andrássy út 60. szám alatt (ma a Terror Háza)", "A Parlamentben", "A Nemzeti Színházban", "A Gellért Szállóban"], "correctIndex": 0, "explanation": "Az Andrássy út 60. volt az ÁVH székhelye."},
    {"id": "ex.b1.rakosikorszak.cons.10", "type": "fill-blank", "lesson": "lesson.b1.rakosikorszak.consolidation", "teaches": ["Recsken"], "prompt": "*Recsken* működött a legkegyetlenebb kényszermunkatábor.", "sentence": "*Recsken* működött a legkegyetlenebb kényszermunkatábor.", "target": "Recsken"},
    {"id": "ex.b1.rakosikorszak.cons.11", "type": "sentence-builder", "lesson": "lesson.b1.rakosikorszak.consolidation", "teaches": ["kitelepites", "Hortobagy"], "prompt": "Rakd össze a kitelepítésről szóló mondatot!", "chips": ["Tízezer", "polgárt", "telepítettek", "ki", "a", "Hortobágy", "zárt", "táboraiba."], "target": "Tízezer polgárt telepítettek ki a Hortobágy zárt táboraiba.", "english": "Ten thousand citizens were deported to the closed camps of Hortobágy."},
    {"id": "ex.b1.rakosikorszak.cons.12", "type": "multiple-choice", "lesson": "lesson.b1.rakosikorszak.consolidation", "teaches": ["vas-es-acel-doktrina"], "prompt": "Milyen irreális iparpolitikai jelszót erőltetett a Rákosi-rendszer?", "options": ["'A vas és acél országa'", "'A textilipar fővárosa'", "'A bor és búza hazája'", "'A napfény országa'"], "correctIndex": 0, "explanation": "'A vas és acél országa' volt a diktatúra jelszava."},
    {"id": "ex.b1.rakosikorszak.cons.13", "type": "fill-blank", "lesson": "lesson.b1.rakosikorszak.consolidation", "teaches": ["padlassopres"], "prompt": "A beszolgáltatáskor az utolsó szem gabonát is elvitte a *padlássöprés*.", "sentence": "A beszolgáltatáskor az utolsó szem gabonát is elvitte a *padlássöprés*.", "target": "padlássöprés"},
    {"id": "ex.b1.rakosikorszak.cons.14", "type": "sentence-builder", "lesson": "lesson.b1.rakosikorszak.consolidation", "teaches": ["kulakok", "uldoztek"], "prompt": "Alkoss szabályos mondatot!", "chips": ["A", "falvakban", "kegyetlenül", "üldözték", "a", "kuláknak", "bélyegzett", "gazdákat."], "target": "A falvakban kegyetlenül üldözték a kuláknak bélyegzett gazdákat.", "english": "In the villages they cruelly persecuted the farmers branded as kulaks."},
    {"id": "ex.b1.rakosikorszak.cons.15", "type": "multiple-choice", "lesson": "lesson.b1.rakosikorszak.consolidation", "teaches": ["1949-alkotmany-szovjet"], "prompt": "Melyik évben fogadták el a szovjet mintájú sztálini alkotmányt Magyarországon?", "options": ["1949-ben (augusztus 20-án)", "1945-ben", "1956-ban", "1989-ben"], "correctIndex": 0, "explanation": "1949. augusztus 20-án léptették életbe a sztálini alkotmányt."},
    {"id": "ex.b1.rakosikorszak.cons.16", "type": "fill-blank", "lesson": "lesson.b1.rakosikorszak.consolidation", "teaches": ["teeszbe"], "prompt": "A parasztokat erőszakkal kényszerítették a *téeszbe*.", "sentence": "A parasztokat erőszakkal kényszerítették a *téeszbe*.", "target": "téeszbe"},
    {"id": "ex.b1.rakosikorszak.cons.17", "type": "sentence-builder", "lesson": "lesson.b1.rakosikorszak.consolidation", "teaches": ["AVH", "terror"], "prompt": "Rakd össze a diktatúrát összegző mondatot!", "chips": ["Az", "ÁVH", "és", "a", "párt", "totális", "félelmet", "és", "terrort", "teremtett."], "target": "Az ÁVH és a párt totális félelmet és terrort teremtett.", "english": "The ÁVH and the party created total fear and terror."},
    {"id": "ex.b1.rakosikorszak.cons.18", "type": "multiple-choice", "lesson": "lesson.b1.rakosikorszak.consolidation", "teaches": ["Rajk-Laszlo-per-belso"], "prompt": "Mit bizonyított Rajk László kivégzése a Rákosi-korszakban?", "options": ["Hogy a sztálini diktatúra még a saját korábbi vezetőit és elvtársait is feláldozza a hatalomért", "Hogy a bíróságok függetlenek voltak", "Hogy a rendőrség nem létezett", "Hogy véget ért a diktatúra"], "correctIndex": 0, "explanation": "A belső párttisztogatás a totális paranoia és elnyomás csúcsa volt."},
    {"id": "ex.b1.rakosikorszak.cons.19", "type": "fill-blank", "lesson": "lesson.b1.rakosikorszak.consolidation", "teaches": ["egypartrendszer"], "prompt": "A fordulat éve után kizárólag az *egypártrendszer* maradt fenn.", "sentence": "A fordulat éve után kizárólag az *egypártrendszer* maradt fenn.", "target": "egypártrendszer"},
    {"id": "ex.b1.rakosikorszak.cons.20", "type": "multiple-choice", "lesson": "lesson.b1.rakosikorszak.consolidation", "teaches": ["Rakosi-korszak-osszegzes"], "prompt": "Mi jellemezte a Rákosi-korszakot (1948–1956) összegzésként?", "options": ["Totális diktatúra, személyi kultusz, ÁVH-terror, koncepciós perek, kényszermunka (Recsk) és a lakosság elnyomása", "Páratlan szabadság és jólét", "Szabad sajtó és többpártrendszer", "A vallásszabadság virágzása"], "correctIndex": 0, "explanation": "A Rákosi-korszak a magyar történelem legsötétebb totális diktatúrája volt, ami az 1956-os forradalomhoz vezetett."}
]
write_json(EXERCISES_DIR / "ex.b1.rakosikorszak.consolidation.json", make_exercise_group("ex.b1.rakosikorszak.consolidation", "A Rákosi-korszak összefoglaló gyakorlatok", "Átfogó teszt a Rákosi-korszakról: az 1945-ös választásokról, a szalámitaktikáról, a perekről, az ÁVH-ról és a tervgazdálkodásról.", cons_24_exs))

cons_24_lesson = {
    "id": "lesson.b1.rakosikorszak.consolidation",
    "title": "The Communist Takeover & Rákosi Era: Unit 24 Consolidation",
    "level": "B1",
    "track": "citizenship",
    "estimatedMinutes": 25,
    "prerequisites": [
        "lesson.b1.rakosikorszak.01",
        "lesson.b1.rakosikorszak.02",
        "lesson.b1.rakosikorszak.03",
        "lesson.b1.rakosikorszak.04",
        "lesson.b1.rakosikorszak.05"
    ],
    "grammar": ["Unit review"],
    "vocabulary": ["Unit review"],
    "culturalContext": "Magyar történelem összefoglalás (Honosítási vizsgafelkészítő)",
    "sections": [
        {
            "type": "intro",
            "title": "Unit 24 Consolidation: The Communist Takeover & Rákosi Era (1945–1956)",
            "body": "Ebben az összefoglaló leckében áttekintjük az 1945-ös szabad választásokat (Kisgazdapárt győzelme 57%), az 1946-os második köztársaságot, a szalámitaktikát és az 1948-as fordulat évét, Rákosi Mátyás személyi kultuszát és a koncepciós pereket (Mindszenty József, Rajk László), az ÁVH rémuralmát és a recski kényszermunkatábort, valamint a 'vas és acél országát', a téeszesítést és a padlássöpréseket."
        },
        {
            "type": "goal",
            "title": "Consolidation Goals",
            "items": [
                "A Rákosi-diktatúra kulcséveinek (1945, 1947, 1948, 1949, 1951) és intézményeinek pontos ismerete",
                "Választási eredményeket, fokozatosságot, koncepciós pereket és kényszerű elvonásokat leíró nyelvtani formák biztos alkalmazása",
                "A totalitárius kommunista diktatúra áldozatainak történelmi felidézése"
            ]
        },
        {
            "type": "exercise-group",
            "title": "Comprehensive Unit 24 Practice",
            "ref": "ex.b1.rakosikorszak.consolidation",
            "exerciseRefs": [e["id"] for e in cons_24_exs]
        },
        {
            "type": "checklist",
            "items": [
                "Tudom az 1945-ös választások és az 1946-os köztársaság történetét",
                "Ismerem a szalámitaktika (1948) és az egypártrendszer kiépülését",
                "Megértem Mindszenty József perét és a személyi kultuszt",
                "Ismerem az ÁVH-t, Recsket, a kitelepítéseket és a padlássöprést"
            ]
        }
    ]
}
write_json(LESSONS_DIR / "lesson.b1.rakosikorszak.consolidation.json", cons_24_lesson)

print("Units 22, 23, 24 complete!")
