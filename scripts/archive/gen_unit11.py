# -*- coding: utf-8 -*-
"""
Full Unit 11 Overhaul: Transylvania's Golden Age (b1-erdelyaranykora)
Lessons:
1. A tordai vallásbéke és a vallásszabadság (1568)
2. Bocskai István és a hajdúk felkelése (1604–1606, bécsi béke)
3. Bethlen Gábor fejedelem és az erdélyi gazdaság aranykora (1613–1629)
4. I. Rákóczi György és a linzi béke (1645)
5. Erdély és a magyar kultúra megőrzése (Vizsolyi Biblia, kollégiumok)
Consolidation: Unit 11 Capstone (20 exercises)
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
# LESSON 1: b1-erdelyaranykora-01 (A tordai vallásbéke 1568)
# ==========================================
story_1 = make_story(
    "story.b1.erdelyaranykora.01",
    "A tordai vallásbéke és a vallásszabadság (1568)",
    "1568-ban a tordai országgyűlésen a világon elsőként mondták ki a vallásszabadságot és a felekezetek békés együttélését.",
    "Torda és Kolozsvár",
    ["Legal and declaratory formulations (szabad legyen, elrendeltetik)", "Religious tolerance in history"],
    ["tordai vallásbéke", "vallásszabadság", "bevett felekezet", "János Zsigmond", "türelem"],
    [
        "A 16. században Európát véres vallásháborúk sújtották a reformáció elterjedése miatt. Ezzel szemben az Erdélyi Fejedelemségben János Zsigmond fejedelem és Dávid Ferenc udvari lelkész vezetésével a békés teológiai párbeszéd és a kölcsönös türelem kerekedett felül.",
        "1568 januárjában a tordai katolikus templomban ülésező országgyűlés történelmi határozatot hozott. A törvény kimondta: 'a hit Isten ajándéka', ezért senkit sem szabad hite miatt bántani, fenyegetni vagy fogságba vetni, és minden falu olyan lelkészt tarthat, amilyet jónak lát.",
        "A tordai ediktum a világ legelső vallásszabadsági törvényeként négy bevett felekezetet ismert el egyenjogúnak: a katolikus, a református, az evangélikus és az unitárius egyházat, miközben az ortodox vallást is megtűrték. Ez a vallási türelem tette lehetővé Erdély kulturális felvirágzását."
    ],
    [
        {"lemma": "vallásszabadság", "pos": "noun", "cefr": "B1", "gloss": "religious freedom"},
        {"lemma": "bevett vallás", "pos": "noun", "cefr": "B1", "gloss": "officially recognized / received denomination"},
        {"lemma": "türelem", "pos": "noun", "cefr": "B1", "gloss": "tolerance, patience"},
        {"lemma": "felekezet", "pos": "noun", "cefr": "B1", "gloss": "religious denomination, sect"},
        {"lemma": "elrendel", "pos": "verb", "cefr": "B1", "gloss": "to decree, order by law"}
    ],
    [
        {
            "question": "Miért számít világtörténelmi jelentőségűnek az 1568-as tordai országgyűlés?",
            "options": ["Mert a világon elsőként törvénybe iktatta a vallásszabadságot és a felekezetek türelmét", "Mert ott koronázták meg Mátyás királyt", "Mert békét kötöttek a római pápával", "Mert ott alapították meg az első egyetemet"],
            "correctIndex": 0,
            "explanation": "1568-ban Tordán a világon elsőként iktatták törvénybe a vallásszabadságot."
        }
    ]
)
write_json(STORIES_DIR / "story.b1.erdelyaranykora.01.json", story_1)

voc_1 = {
    "id": "voc.b1.erdelyaranykora.01",
    "title": "A vallásszabadság és reformáció szókincse",
    "description": "Vallásbéke, türelem, bevett felekezetek és törvényhozási kifejezések.",
    "entries": [
        {"lemma": "vallásszabadság", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "freedom of religion, religious liberty", "examples": [{"hu": "1568-ban Tordán mondták ki a vallásszabadságot.", "en": "Religious freedom was declared in Torda in 1568."}]}]},
        {"lemma": "bevett vallás", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "officially recognized/received denomination", "examples": [{"hu": "Négy bevett vallást ismert el az erdélyi törvény.", "en": "Transylvanian law recognized four accepted religions."}]}]},
        {"lemma": "türelem", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "religious tolerance", "examples": [{"hu": "A vallási türelem biztosította a belső békét.", "en": "Religious tolerance ensured internal peace."}]}]},
        {"lemma": "felekezet", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "religious denomination", "examples": [{"hu": "A különböző felekezetek békében éltek egymás mellett.", "en": "The various denominations lived peacefully alongside each other."}]}]},
        {"lemma": "elrendel", "pos": "verb", "cefr": "B1", "definitions": [{"meaning": "to decree, ordain by law", "examples": [{"hu": "Az országgyűlés elrendelte a szabad prédikálást.", "en": "The Diet decreed free preaching."}]}]}
    ]
}
write_json(VOCAB_DIR / "voc.b1.erdelyaranykora.01.json", voc_1)

gr_1 = {
    "id": "gr.b1.erdelyaranykora.01",
    "title": "Jogi és kinyilatkoztató kifejezések (szabad legyen, elrendeltetik, kimondja, hogy)",
    "description": "Formulating legal declarations, decrees, and official proclamations.",
    "rules": [
        "A jogi kinyilatkoztatásokban gyakori a ható ige vagy a felszólító mód alkalmazása: 'szabad legyen a prédikálás', 'tilos legyen a zaklatás'.",
        "A törvénycikkek gyakran a 'kimondja, hogy' vagy 'elrendeli, hogy' bevezetéssel élnek."
    ],
    "tables": [
        {"headers": ["Kifejezés", "Jogi funkció", "Példa"], "rows": [
            ["szabad legyen", "engedélyezés, jogadás", "Mindenkinek szabad legyen a vallásgyakorlat."],
            ["elrendeltetik", "törvényi határozat", "Elrendeltetik a felekezetek békéje."],
            ["kimondja, hogy", "kinyilatkoztatás", "A törvény kimondja, hogy a hit Isten ajándéka."]
        ]}
    ],
    "examples": [
        {"spanish": "A tordai törvény kimondja, hogy senkit sem szabad megbüntetni a hitéért.", "english": "The law of Torda declares that no one may be punished for their faith."},
        {"spanish": "Szabad legyen minden településen olyan lelkészt választani, akit a közösség akar.", "english": "Let it be permitted in every settlement to choose such a preacher as the community desires."},
        {"spanish": "Az országgyűlés elrendelte a négy felekezet egyenlő jogait.", "english": "The Diet ordered the equal rights of the four denominations."}
    ]
}
write_json(GRAMMAR_DIR / "gr.b1.erdelyaranykora.01.json", gr_1)

exs_1 = [
    {"id": "ex.b1.erdelyaranykora.01.01", "type": "multiple-choice", "lesson": "lesson.b1.erdelyaranykora.01", "teaches": ["tordai-vallasbeke"], "prompt": "Melyik évben született a tordai vallásbéke?", "options": ["1568-ban", "1526-ban", "1541-ben", "1606-ban"], "correctIndex": 0, "explanation": "A tordai vallásbékét 1568-ban hirdették ki."},
    {"id": "ex.b1.erdelyaranykora.01.02", "type": "fill-blank", "lesson": "lesson.b1.erdelyaranykora.01", "teaches": ["vallasszabadsag"], "prompt": "Egészítsd ki a mondatot!", "sentence": "Tordán hirdették ki a világon először a *vallásszabadságot*.", "target": "vallásszabadságot"},
    {"id": "ex.b1.erdelyaranykora.01.03", "type": "sentence-builder", "lesson": "lesson.b1.erdelyaranykora.01", "teaches": ["kimondja", "hit"], "prompt": "Rakd össze a tordai határozat híres mondatát!", "chips": ["A", "törvény", "kimondja,", "hogy", "a", "hit", "Isten", "ajándéka."], "target": "A törvény kimondja, hogy a hit Isten ajándéka.", "english": "The law declares that faith is a gift of God."},
    {"id": "ex.b1.erdelyaranykora.01.04", "type": "multiple-choice", "lesson": "lesson.b1.erdelyaranykora.01", "teaches": ["bevett-vallasok"], "prompt": "Hány 'bevett vallást' (egyenjogú felekezetet) ismert el az 1568-as törvény?", "options": ["Négyet (katolikus, református, evangélikus, unitárius)", "Csak egyet", "Kettőt", "Tízet"], "correctIndex": 0, "explanation": "Négy felekezet vált bevett vallássá: katolikus, református, evangélikus és unitárius."},
    {"id": "ex.b1.erdelyaranykora.01.05", "type": "fill-blank", "lesson": "lesson.b1.erdelyaranykora.01", "teaches": ["felekezet"], "prompt": "Egészítsd ki a mondatot a megfelelő szóval!", "sentence": "Az erdélyi országgyűlés négy bevett *felekezetet* ismert el.", "target": "felekezetet"},
    {"id": "ex.b1.erdelyaranykora.01.06", "type": "sentence-builder", "lesson": "lesson.b1.erdelyaranykora.01", "teaches": ["szabad-legyen", "vallas"], "prompt": "Alkoss szabályos jogi mondatot!", "chips": ["Minden", "embernek", "szabad", "legyen", "a", "vallásgyakorlat."], "target": "Minden embernek szabad legyen a vallásgyakorlat.", "english": "Let religious practice be free for all people."},
    {"id": "ex.b1.erdelyaranykora.01.07", "type": "multiple-choice", "lesson": "lesson.b1.erdelyaranykora.01", "teaches": ["Janos-Zsigmond"], "prompt": "Ki volt Erdély fejedelme a tordai vallásbéke elfogadásakor?", "options": ["János Zsigmond", "Bethlen Gábor", "Bocskai István", "I. Rákóczi György"], "correctIndex": 0, "explanation": "János Zsigmond volt az első erdélyi fejedelem, akinek udvarában elfogadták a vallásbékét."},
    {"id": "ex.b1.erdelyaranykora.01.08", "type": "fill-blank", "lesson": "lesson.b1.erdelyaranykora.01", "teaches": ["turelem"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A felekezetek közötti *türelem* Erdély békéjének alapja volt.", "target": "türelem"}
]
write_json(EXERCISES_DIR / "ex.b1.erdelyaranykora.01.json", make_exercise_group("ex.b1.erdelyaranykora.01", "A tordai vallásbéke gyakorlatai", "Gyakorlatok az 1568-as vallásszabadságról és a jogi nyelvezetről.", exs_1))

lesson_1 = make_lesson(
    "lesson.b1.erdelyaranykora.01",
    "A tordai vallásbéke és a vallásszabadság (1568)",
    "Jogi és kinyilatkoztató szerkezetek (szabad legyen, kimondja, hogy)",
    "Megismerjük a tordai országgyűlést, a vallásszabadság törvénybe iktatását és a négy bevett vallást.",
    ["Megérteni az 1568-as tordai vallásbéke jelentőségét", "Használni a jogi kinyilatkoztató nyelvi szerkezeteket", "Ismerni a négy bevett felekezetet (katolikus, református, evangélikus, unitárius)"],
    "story.b1.erdelyaranykora.01",
    "voc.b1.erdelyaranykora.01",
    "gr.b1.erdelyaranykora.01",
    "ex.b1.erdelyaranykora.01",
    [e["id"] for e in exs_1]
)
write_json(LESSONS_DIR / "lesson.b1.erdelyaranykora.01.json", lesson_1)


# ==========================================
# LESSON 2: b1-erdelyaranykora-02 (Bocskai és a hajdúk)
# ==========================================
story_2 = make_story(
    "story.b1.erdelyaranykora.02",
    "Bocskai István és a hajdúk felkelése (1604–1606)",
    "Bocskai István a fegyveres hajdúk élén felkelt a Habsburgok önkénye ellen, kivívva a rendi jogokat és a vallásszabadságot az 1606-os bécsi békében.",
    "Debrecen, Kassa és Bécs",
    ["Result and consequence clauses (oly módon, hogy, úgy... hogy)", "Rebellion and diplomacy"],
    ["Bocskai István", "hajdúk", "bécsi béke", "rendi jogok", "nemesítés"],
    [
        "A tizenöt éves háború pusztításai és Rudolf császár erőszakos ellenreformációs intézkedései mély elégedetlenséget szültek a magyar nemesség és a protestánsok körében. Amikor a bécsi udvar koncepciós pereket indított a gazdag magyar főurak ellen birtokaik elkobzására, Bocskai István az ellenállás élére állt.",
        "Bocskai maga mellé állította a kiválóan harcoló, marhapásztorokból lett fegyveres hajdúkat. Oly módon szervezte meg felkelését, hogy csapatai gyors egymásutánban felszabadították Erdélyt és a Felvidéket, aminek következtében a császári udvar tárgyalásokra kényszerült.",
        "Az 1606-ban megkötött bécsi békében a császár elismerte Erdély függetlenségét, garantálta a magyar nemesség rendi jogait és a protestánsok vallásszabadságát. Bocskai mintegy tízezer hajdút kollektív nemesi rangra emelt és letelepített a mai Hajdúság városaiban, örök katonai szolgálatuk fejében."
    ],
    [
        {"lemma": "hajdú", "pos": "noun", "cefr": "B1", "gloss": "armed drover / Hajdú soldier"},
        {"lemma": "rendi jogok", "pos": "noun", "cefr": "B1", "gloss": "feudal / estate rights"},
        {"lemma": "felkelés", "pos": "noun", "cefr": "B1", "gloss": "uprising, revolt"},
        {"lemma": "letelepít", "pos": "verb", "cefr": "B1", "gloss": "to settle (people) permanently"},
        {"lemma": "garantál", "pos": "verb", "cefr": "B1", "gloss": "to guarantee"}
    ],
    [
        {
            "question": "Mit ért el Bocskai István az 1606-os bécsi békével?",
            "options": ["Garantálta Erdély függetlenségét, a rendi jogokat és a vallásszabadságot", "Elfoglalta Bécset és császár lett", "Kiűzte az összes törököt Magyarországról", "Egyesítette Ausztriát és Lengyelországot"],
            "correctIndex": 0,
            "explanation": "Az 1606-os bécsi béke a rendi jogok és a vallásszabadság győzelme volt."
        }
    ]
)
write_json(STORIES_DIR / "story.b1.erdelyaranykora.02.json", story_2)

voc_2 = {
    "id": "voc.b1.erdelyaranykora.02",
    "title": "A hajdúfelkelés és a bécsi béke szókincse",
    "description": "Hajdúk, szabadságharc, nemesítés, letelepítés és nemzetközi békeszerződések.",
    "entries": [
        {"lemma": "hajdú", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "armed drover warrior, noble Hajdú", "examples": [{"hu": "Bocskai a hajdúk segítségével aratott győzelmet.", "en": "Bocskai won victory with the help of the Hajdús."}]}]},
        {"lemma": "rendi jogok", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "estate privileges and feudal constitutional rights", "examples": [{"hu": "A bécsi béke visszaállította a nemesi rendi jogokat.", "en": "The Peace of Vienna restored noble estate rights."}]}]},
        {"lemma": "felkelés", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "uprising, armed revolt", "examples": [{"hu": "A szabadságért indított felkelés sikeres volt.", "en": "The uprising launched for liberty was successful."}]}]},
        {"lemma": "letelepít", "pos": "verb", "cefr": "B1", "definitions": [{"meaning": "to settle permanently on land", "examples": [{"hu": "Bocskai a Hajdúság városaiba telepítette le a vitézeit.", "en": "Bocskai settled his warriors in the towns of Hajdúság."}]}]},
        {"lemma": "garantál", "pos": "verb", "cefr": "B1", "definitions": [{"meaning": "to guarantee by treaty", "examples": [{"hu": "A császár békében garantálta a vallásszabadságot.", "en": "The Emperor guaranteed religious freedom in the peace treaty."}]}]}
    ]
}
write_json(VOCAB_DIR / "voc.b1.erdelyaranykora.02.json", voc_2)

gr_2 = {
    "id": "gr.b1.erdelyaranykora.02",
    "title": "Következményes összetett mondatok (úgy... hogy, oly módon, hogy)",
    "description": "Expressing results, outcomes, and diplomatic consequences using consecutive clauses.",
    "rules": [
        "A következményes mellékmondatokban az 'úgy / oly módon' utalószót a 'hogy' kötőszó követi.",
        "A mellékmondat a főmondatban kifejtett cselekvés tényleges vagy elért eredményét mutatja be."
    ],
    "tables": [
        {"headers": ["Szerkezet", "Jelentés", "Példa"], "rows": [
            ["úgy... hogy", "so... that", "Úgy harcoltak, hogy a császár meghátrált."],
            ["oly módon, hogy", "in such a way that", "Oly módon egyeztek meg, hogy békét kötöttek."]
        ]}
    ],
    "examples": [
        {"spanish": "Bocskai úgy szervezte meg a sereget, hogy gyors sikereket ért el.", "english": "Bocskai organized the army in such a way that he achieved swift successes."},
        {"spanish": "A hajdúkat oly módon telepítették le, hogy védelmi sávot alkossanak.", "english": "The Hajdús were settled in such a manner that they formed a defense line."},
        {"spanish": "A bécsi béke úgy zárult le, hogy mindkét fél elfogadta a feltételeket.", "english": "The Peace of Vienna concluded in such a way that both parties accepted the conditions."}
    ]
}
write_json(GRAMMAR_DIR / "gr.b1.erdelyaranykora.02.json", gr_2)

exs_2 = [
    {"id": "ex.b1.erdelyaranykora.02.01", "type": "multiple-choice", "lesson": "lesson.b1.erdelyaranykora.02", "teaches": ["Bocskai-Istvan"], "prompt": "Ki vezette az 1604–1606-os Habsburg-ellenes felkelést?", "options": ["Bocskai István", "Zrínyi Ilona", "II. Rákóczi Ferenc", "Dobó István"], "correctIndex": 0, "explanation": "Bocskai István erdélyi fejedelem vezette a hajdúk felkelését."},
    {"id": "ex.b1.erdelyaranykora.02.02", "type": "fill-blank", "lesson": "lesson.b1.erdelyaranykora.02", "teaches": ["hajdu"], "prompt": "Egészítsd ki a mondatot!", "sentence": "Bocskai fegyveres *hajdúk* segítségével foglalta vissza a várakat.", "target": "hajdúk"},
    {"id": "ex.b1.erdelyaranykora.02.03", "type": "sentence-builder", "lesson": "lesson.b1.erdelyaranykora.02", "teaches": ["ugy", "garantal"], "prompt": "Rakd össze a következményes mondatot!", "chips": ["Úgy", "egyeztek", "meg,", "hogy", "garantálták", "a", "szabadságot."], "target": "Úgy egyeztek meg, hogy garantálták a szabadságot.", "english": "They agreed in such a way that they guaranteed liberty."},
    {"id": "ex.b1.erdelyaranykora.02.04", "type": "multiple-choice", "lesson": "lesson.b1.erdelyaranykora.02", "teaches": ["becsi-beke"], "prompt": "Melyik évben kötötték meg a bécsi békét?", "options": ["1606-ban", "1568-ban", "1526-ban", "1686-ban"], "correctIndex": 0, "explanation": "A bécsi béke 1606-ban zárta le Bocskai felkelését."},
    {"id": "ex.b1.erdelyaranykora.02.05", "type": "fill-blank", "lesson": "lesson.b1.erdelyaranykora.02", "teaches": ["letelepit"], "prompt": "Egészítsd ki a mondatot a megfelelő igealakkal!", "sentence": "A fejedelem saját birtokain *letelepítette* a hajdúkat.", "target": "letelepítette"},
    {"id": "ex.b1.erdelyaranykora.02.06", "type": "sentence-builder", "lesson": "lesson.b1.erdelyaranykora.02", "teaches": ["rendi-jogok", "becsi-beke"], "prompt": "Alkoss szabályos mondatot!", "chips": ["A", "bécsi", "béke", "visszaállította", "a", "rendi", "jogokat."], "target": "A bécsi béke visszaállította a rendi jogokat.", "english": "The Peace of Vienna restored estate rights."},
    {"id": "ex.b1.erdelyaranykora.02.07", "type": "multiple-choice", "lesson": "lesson.b1.erdelyaranykora.02", "teaches": ["Hajdusag"], "prompt": "Hol élnek ma is a Bocskai által letelepített hajdúk leszármazottai?", "options": ["A Hajdúság városaiban (Hajdúböszörmény, Hajdúszoboszló stb.)", "A Dunántúlon", "A Székelyföldön", "Buda környékén"], "correctIndex": 0, "explanation": "A hajdúvárosok alkotják a mai Hajdúság térségét."},
    {"id": "ex.b1.erdelyaranykora.02.08", "type": "fill-blank", "lesson": "lesson.b1.erdelyaranykora.02", "teaches": ["rendi-jogok"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A nemesség megvédte a magyar *rendi jogokat* a császárral szemben.", "target": "rendi jogokat"}
]
write_json(EXERCISES_DIR / "ex.b1.erdelyaranykora.02.json", make_exercise_group("ex.b1.erdelyaranykora.02", "Bocskai és a hajdúk gyakorlatai", "Gyakorlatok az 1604–1606-os felkelésről és a következményes mondatszerkezetekről.", exs_2))

lesson_2 = make_lesson(
    "lesson.b1.erdelyaranykora.02",
    "Bocskai István és a hajdúk felkelése (1604–1606)",
    "Következményes mondatok (úgy... hogy, oly módon, hogy)",
    "Megismerjük Bocskai szabadságharcát, a hajdúk felemelkedését és az 1606-os bécsi béke pontjait.",
    ["Megérteni az 1606-os bécsi béke jelentőségét", "Használni a következményes összetett mondatokat", "Ismerni a hajdúk letelepítésének történetét és a rendi jogok védelmét"],
    "story.b1.erdelyaranykora.02",
    "voc.b1.erdelyaranykora.02",
    "gr.b1.erdelyaranykora.02",
    "ex.b1.erdelyaranykora.02",
    [e["id"] for e in exs_2]
)
write_json(LESSONS_DIR / "lesson.b1.erdelyaranykora.02.json", lesson_2)


# ==========================================
# LESSON 3: b1-erdelyaranykora-03 (Bethlen Gábor aranykora)
# ==========================================
story_3 = make_story(
    "story.b1.erdelyaranykora.03",
    "Bethlen Gábor fejedelem és az erdélyi gazdaság aranykora (1613–1629)",
    "Bethlen Gábor bölcs gazdaságpolitikájával és mecénási tevékenységével európai rangú, virágzó állammá emelte az Erdélyi Fejedelemséget.",
    "Gyulafehérvár és Kolozsvár",
    ["Instrument and means structures (által, révén, segítségével, útján)", "Economic and cultural flourishing"],
    ["Bethlen Gábor", "aranykor", "merkantilizmus", "Gyulafehérvár", "mecénás"],
    [
        "Bethlen Gábor 1613-ban vette át a meggyengült fejedelemség irányítását. Rendeletei révén az állami bevételeket megsokszorozta: állami monopóliummá tette a higany-, só- és szarvasmarha-kereskedelmet, míg külföldi bányászok és iparosok (habánok) betelepítése által felvirágoztatta az erdélyi kézműipart.",
        "A gazdasági bevételek segítségével Bethlen ütőképes, modern zsoldossereget tartott fenn. Bekapcsolódott a harmincéves háborúba a protestáns hatalmak oldalán, és hadjáratai útján sikeresen védte meg a Királyi Magyarország rendi alkotmányát és vallásszabadságát az 1621-es nikolsburgi békében.",
        "Fővárosa, Gyulafehérvár a magyar és európai reneszánsz kultúra ragyogó fellegvárává vált. Bethlen fejedelem református kollégiumot és könyvtárat alapított, külföldi professzorokat hívott meg, és tehetséges diákok százait küldte nyugat-európai egyetemekre állami ösztöndíjjal."
    ],
    [
        {"lemma": "aranykor", "pos": "noun", "cefr": "B1", "gloss": "golden age"},
        {"lemma": "monopólium", "pos": "noun", "cefr": "B1", "gloss": "state monopoly"},
        {"lemma": "mecénás", "pos": "noun", "cefr": "B1", "gloss": "patron of the arts and sciences"},
        {"lemma": "felvirágoztat", "pos": "verb", "cefr": "B1", "gloss": "to cause to flourish/prosper"},
        {"lemma": "ösztöndíj", "pos": "noun", "cefr": "B1", "gloss": "scholarship, grant"}
    ],
    [
        {
            "question": "Hogyan tette virágzóvá Bethlen Gábor Erdély gazdaságát?",
            "options": ["Állami monopóliumokkal, külföldi mesterek betelepítésével és bányászat fejlesztésével", "Minden adó eltörlésével", "Aranybányák eladásával a törököknek", "Csak mezőgazdasági importtal"],
            "correctIndex": 0,
            "explanation": "Bethlen gazdasági monopóliumokkal és bányászati reformokkal gazdagította meg a kincstárat."
        }
    ]
)
write_json(STORIES_DIR / "story.b1.erdelyaranykora.03.json", story_3)

voc_3 = {
    "id": "voc.b1.erdelyaranykora.03",
    "title": "A gazdasági és kulturális aranykor szókincse",
    "description": "Monopólium, gazdaságpolitika, mecenatúra, iskolaalapítás és aranykor.",
    "entries": [
        {"lemma": "aranykor", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "golden age of culture and prosperity", "examples": [{"hu": "Bethlen Gábor kora Erdély aranykora volt.", "en": "Gabriel Bethlen's era was Transylvania's golden age."}]}]},
        {"lemma": "monopólium", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "state trading monopoly", "examples": [{"hu": "A fejedelem monopóliummá tette a sókereskedelmet.", "en": "The Prince turned salt trade into a monopoly."}]}]},
        {"lemma": "mecénás", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "patron of arts, science and education", "examples": [{"hu": "A fejedelem bőkezű mecénásként támogatta a tudományt.", "en": "The Prince supported science as a generous patron."}]}]},
        {"lemma": "felvirágoztat", "pos": "verb", "cefr": "B1", "definitions": [{"meaning": "to cause to blossom and prosper", "examples": [{"hu": "A bölcs vezetés felvirágoztatta az országot.", "en": "Wise leadership caused the country to flourish."}]}]},
        {"lemma": "ösztöndíj", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "student scholarship, study stipend", "examples": [{"hu": "A diákok fejedelmi ösztöndíjjal tanultak Leidenben.", "en": "Students studied in Leiden with princely scholarships."}]}]}
    ]
}
write_json(VOCAB_DIR / "voc.b1.erdelyaranykora.03.json", voc_3)

gr_3 = {
    "id": "gr.b1.erdelyaranykora.03",
    "title": "Eszköz- és módhatározói névutók (által, révén, segítségével, útján)",
    "description": "Expressing means, instruments, and channels of historical achievement.",
    "rules": [
        "A 'révén' és 'által' névutók a cselekvés végrehajtóját vagy közvetítő eszközét jelölik: 'rendeletek révén', 'bányászat által'.",
        "A 'segítségével' személyek vagy tárgyi eszközök igénybevételét fejezi ki: 'zsoldosok segítségével'.",
        "Az 'útján' hivatalos vagy diplomáciai csatornákat jelez: 'tárgyalások útján'."
    ],
    "tables": [
        {"headers": ["Névutó / Kifejezés", "Funkció", "Példa"], "rows": [
            ["révén", "közvetítés, eszköz", "Reformok révén gyarapodott a kincstár."],
            ["által", "okozó vagy eszköz", "Monopóliumok által nőtt a bevétel."],
            ["segítségével", "támogatás felhasználása", "A sereg segítségével győzött."],
            ["útján", "eljárásmód, csatorna", "Békeszerződés útján rendezte a jogokat."]
        ]}
    ],
    "examples": [
        {"spanish": "Bethlen Gábor reformjai révén Erdély megerősödött.", "english": "Through Gabriel Bethlen's reforms, Transylvania was strengthened."},
        {"spanish": "A diákok állami ösztöndíj segítségével tanultak külföldön.", "english": "Students studied abroad with the help of state scholarships."},
        {"spanish": "A fejedelem tárgyalások útján érte el a vallásszabadság elismerését.", "english": "The Prince achieved recognition of religious freedom by means of negotiations."}
    ]
}
write_json(GRAMMAR_DIR / "gr.b1.erdelyaranykora.03.json", gr_3)

exs_3 = [
    {"id": "ex.b1.erdelyaranykora.03.01", "type": "multiple-choice", "lesson": "lesson.b1.erdelyaranykora.03", "teaches": ["Bethlen-Gabor"], "prompt": "Melyik korszakot nevezik 'Erdély aranykorának'?", "options": ["Bethlen Gábor fejedelemségét (1613–1629)", "A mohácsi csata utáni éveket", "A tatárjárás idejét", "A dualizmus korát"], "correctIndex": 0, "explanation": "Bethlen Gábor uralkodása (1613–1629) jelentette Erdély gazdasági és kulturális aranykorát."},
    {"id": "ex.b1.erdelyaranykora.03.02", "type": "fill-blank", "lesson": "lesson.b1.erdelyaranykora.03", "teaches": ["aranykor"], "prompt": "Egészítsd ki a mondatot!", "sentence": "Bethlen Gábor fejedelemsége Erdély valódi *aranykora* volt.", "target": "aranykora"},
    {"id": "ex.b1.erdelyaranykora.03.03", "type": "sentence-builder", "lesson": "lesson.b1.erdelyaranykora.03", "teaches": ["reven", "kincstar"], "prompt": "Rakd össze a módhatározói mondatot!", "chips": ["Reformok", "révén", "megtelt", "a", "fejedelmi", "kincstár."], "target": "Reformok révén megtelt a fejedelmi kincstár.", "english": "Through reforms, the princely treasury filled up."},
    {"id": "ex.b1.erdelyaranykora.03.04", "type": "multiple-choice", "lesson": "lesson.b1.erdelyaranykora.03", "teaches": ["Gyulafehervar"], "prompt": "Melyik város volt Bethlen Gábor fejedelmi székhelye?", "options": ["Gyulafehérvár", "Buda", "Pozsony", "Debrecen"], "correctIndex": 0, "explanation": "Gyulafehérvár volt az Erdélyi Fejedelemség virágzó fővárosa."},
    {"id": "ex.b1.erdelyaranykora.03.05", "type": "fill-blank", "lesson": "lesson.b1.erdelyaranykora.03", "teaches": ["mecenas"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A fejedelem nagylelkű *mecénásként* támogatta az oktatást és a művészeteket.", "target": "mecénásként"},
    {"id": "ex.b1.erdelyaranykora.03.06", "type": "sentence-builder", "lesson": "lesson.b1.erdelyaranykora.03", "teaches": ["segitsegevel", "osztondij"], "prompt": "Alkoss helyes mondatot a megadott szavakból!", "chips": ["A", "diákok", "ösztöndíj", "segítségével", "tanultak", "Európában."], "target": "A diákok ösztöndíj segítségével tanultak Európában.", "english": "The students studied in Europe with the help of a scholarship."},
    {"id": "ex.b1.erdelyaranykora.03.07", "type": "multiple-choice", "lesson": "lesson.b1.erdelyaranykora.03", "teaches": ["monopolium"], "prompt": "Mit tett állami monopóliummá Bethlen Gábor?", "options": ["A sót, a higanyt és a szarvasmarha-kereskedelmet", "Csak a könyvnyomtatást", "A faipart", "A bortermelést"], "correctIndex": 0, "explanation": "A legfontosabb exportcikkeket, például a sót és a marhakereskedelmet vonta állami felügyelet alá."},
    {"id": "ex.b1.erdelyaranykora.03.08", "type": "fill-blank", "lesson": "lesson.b1.erdelyaranykora.03", "teaches": ["felviragoztat"], "prompt": "Egészítsd ki a mondatot a megfelelő igealakkal!", "sentence": "A fejedelem intézkedései *felvirágoztatták* a hazai ipart.", "target": "felvirágoztatták"}
]
write_json(EXERCISES_DIR / "ex.b1.erdelyaranykora.03.json", make_exercise_group("ex.b1.erdelyaranykora.03", "Bethlen Gábor kora gyakorlatok", "Gyakorlatok az aranykor gazdaságáról és az eszközhatározói névutókról.", exs_3))

lesson_3 = make_lesson(
    "lesson.b1.erdelyaranykora.03",
    "Bethlen Gábor fejedelem és az erdélyi gazdaság aranykora (1613–1629)",
    "Eszköz- és módhatározói névutók (által, révén, segítségével, útján)",
    "Részletesen elemezzük Bethlen Gábor uralkodását, a merkantilista gazdaságot, Gyulafehérvár udvarát és a tudománypártolást.",
    ["Megérteni az erdélyi aranykor fogalmát és jelentőségét", "Használni az eszközhatározói névutókat (révén, által, útján)", "Ismerni Bethlen Gábor kulturális és gazdasági eredményeit"],
    "story.b1.erdelyaranykora.03",
    "voc.b1.erdelyaranykora.03",
    "gr.b1.erdelyaranykora.03",
    "ex.b1.erdelyaranykora.03",
    [e["id"] for e in exs_3]
)
write_json(LESSONS_DIR / "lesson.b1.erdelyaranykora.03.json", lesson_3)


# ==========================================
# LESSON 4: b1-erdelyaranykora-04 (I. Rákóczi György és a linzi béke)
# ==========================================
story_4 = make_story(
    "story.b1.erdelyaranykora.04",
    "I. Rákóczi György és a linzi béke (1645)",
    "I. Rákóczi György fejedelem sikeres hadjárataival megerősítette Erdély hatalmi pozícióját, és a linzi békében a jobbágyokra is kiterjesztette a vallásszabadságot.",
    "Sárospatak és Linz",
    ["Complex relative pronouns (amelyek közül, akinek a, aminek következtében)", "International diplomacy in early modern Europe"],
    ["I. Rákóczi György", "linzi béke", "jobbágyok vallásszabadsága", "harmincéves háború"],
    [
        "Bethlen Gábor halála után I. Rákóczi György (1630–1648) lépett az Erdélyi Fejedelemség trónjára. A mélyen vallásos, 'bibliás őrálló' fejedelem szilárd kézzel kormányzott, és Sárospatak várát az ország egyik legfontosabb szellemi és katonai központjává tette feleségével, Lorántffy Zsuzsannával.",
        "1644-ben Rákóczi a svéd és francia szövetségesek oldalán bekapcsolódott a harmincéves háborúba. Hadjárataiban a magyar nemesek és hajdúk csapatai egymás után arattak győzelmeket, aminek következtében III. Ferdinánd császár kénytelen volt békét kérni.",
        "Az 1645-ös linzi béke óriási történelmi eredményt hozott: a császár hét felső-magyarországi vármegyét csatolt Erdélyhez, megújította a nemesi szabadságjogokat, és a magyar történelemben páratlan módon a jobbágyság számára is biztosította a szabad vallásgyakorlást."
    ],
    [
        {"lemma": "jobbágy", "pos": "noun", "cefr": "B1", "gloss": "serf, peasant"},
        {"lemma": "kiterjeszt", "pos": "verb", "cefr": "B1", "gloss": "to extend, expand"},
        {"lemma": "szövetséges", "pos": "noun", "cefr": "B1", "gloss": "ally"},
        {"lemma": "megújít", "pos": "verb", "cefr": "B1", "gloss": "to renew, reconfirm"},
        {"lemma": "szabadságjog", "pos": "noun", "cefr": "B1", "gloss": "constitutional liberty, civil right"}
    ],
    [
        {
            "question": "Milyen különleges jogot biztosított az 1645-ös linzi béke?",
            "options": ["A vallásszabadságot a jobbágyok számára is garantálta", "Csak a király választhatott vallást", "Minden adót megszüntetett a nemeseknek", "Erdélyt Ausztriához csatolta"],
            "correctIndex": 0,
            "explanation": "A linzi béke egyedülálló módon a jobbágyoknak is megadta a vallásszabadságot."
        }
    ]
)
write_json(STORIES_DIR / "story.b1.erdelyaranykora.04.json", story_4)

voc_4 = {
    "id": "voc.b1.erdelyaranykora.04",
    "title": "A linzi béke és diplomácia szókincse",
    "description": "Jobbágyjogok, szövetségi politika, jogkiterjesztés és nemzetközi békekötések.",
    "entries": [
        {"lemma": "jobbágy", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "serf, peasant farmer bound to land", "examples": [{"hu": "A linzi béke a jobbágyok vallásszabadságát is védte.", "en": "The Peace of Linz also protected the religious freedom of serfs."}]}]},
        {"lemma": "kiterjeszt", "pos": "verb", "cefr": "B1", "definitions": [{"meaning": "to extend, broaden application", "examples": [{"hu": "A fejedelem kiterjesztette a jogokat a parasztságra.", "en": "The Prince extended the rights to the peasantry."}]}]},
        {"lemma": "szövetséges", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "military ally", "examples": [{"hu": "A svédek és a franciák voltak a fejedelem szövetségesei.", "en": "The Swedes and the French were the Prince's allies."}]}]},
        {"lemma": "megújít", "pos": "verb", "cefr": "B1", "definitions": [{"meaning": "to renew, revalidate rights", "examples": [{"hu": "A békeszerződés megújította a magyar rendi jogokat.", "en": "The peace treaty renewed the Hungarian estate rights."}]}]},
        {"lemma": "szabadságjog", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "fundamental constitutional right/liberty", "examples": [{"hu": "A nemzet ragaszkodott ősi szabadságjogaihoz.", "en": "The nation insisted on its ancient liberties."}]}]}
    ]
}
write_json(VOCAB_DIR / "voc.b1.erdelyaranykora.04.json", voc_4)

gr_4 = {
    "id": "gr.b1.erdelyaranykora.04",
    "title": "Összetett vonatkozó névmások (amelyek közül, akinek a, aminek következtében)",
    "description": "Connecting clauses with inflected relative pronouns and possessive relations.",
    "rules": [
        "A vonatkozó névmások ragozott alakjai pontosan kapcsolják a mellékmondatot a főmondat megfelelő eleméhez.",
        "Az 'amelyek közül' szelekciót, az 'akinek a...' birtoklást, az 'aminek következtében' oksági láncolatot fejez ki."
    ],
    "tables": [
        {"headers": ["Vonatkozó névmás", "Funkció", "Példa"], "rows": [
            ["amelyek közül", "kiválasztás csoportból", "Hét vármegye, amelyek közül több fontos volt."],
            ["akinek a (birtoka)", "birtokos kapcsolat", "A fejedelem, akinek a serege győzött."],
            ["aminek következtében", "eredmény/következmény", "Győztek, aminek következtében békét kötöttek."]
        ]}
    ],
    "examples": [
        {"spanish": "A hadjárat sikeres volt, aminek következtében a császár engedményekre kényszerült.", "english": "The campaign was successful, as a result of which the Emperor was forced into concessions."},
        {"spanish": "A fejedelem, akinek a hite megingathatatlan volt, védte a reformációt.", "english": "The Prince, whose faith was unshakeable, defended the Reformation."},
        {"spanish": "Megszerezte a vármegyéket, amelyek közül Sáros volt a legfontosabb.", "english": "He acquired the counties, among which Sáros was the most important."}
    ]
}
write_json(GRAMMAR_DIR / "gr.b1.erdelyaranykora.04.json", gr_4)

exs_4 = [
    {"id": "ex.b1.erdelyaranykora.04.01", "type": "multiple-choice", "lesson": "lesson.b1.erdelyaranykora.04", "teaches": ["I-Rakoczi-Gyorgy"], "prompt": "Melyik fejedelem kötötte meg az 1645-ös linzi békét?", "options": ["I. Rákóczi György", "Bocskai István", "Bethlen Gábor", "II. Rákóczi Ferenc"], "correctIndex": 0, "explanation": "I. Rákóczi György kötötte meg a linzi békét 1645-ben."},
    {"id": "ex.b1.erdelyaranykora.04.02", "type": "fill-blank", "lesson": "lesson.b1.erdelyaranykora.04", "teaches": ["jobbagy"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A linzi béke a *jobbágyok* számára is biztosította a vallásszabadságot.", "target": "jobbágyok"},
    {"id": "ex.b1.erdelyaranykora.04.03", "type": "sentence-builder", "lesson": "lesson.b1.erdelyaranykora.04", "teaches": ["aminek", "kovetkezteben"], "prompt": "Rakd össze a mondatot a helyes vonatkozó névmással!", "chips": ["Győztek,", "aminek", "következtében", "a", "császár", "békét", "kötött."], "target": "Győztek, aminek következtében a császár békét kötött.", "english": "They won, as a result of which the Emperor made peace."},
    {"id": "ex.b1.erdelyaranykora.04.04", "type": "multiple-choice", "lesson": "lesson.b1.erdelyaranykora.04", "teaches": ["Sarospatak"], "prompt": "Melyik híres vár volt a Rákóczi család és Lorántffy Zsuzsanna székhelye?", "options": ["Sárospatak vára", "Egri vár", "Buda vára", "Szigetvár"], "correctIndex": 0, "explanation": "Sárospatak volt a Rákócziak fellegvára és a kollégium központja."},
    {"id": "ex.b1.erdelyaranykora.04.05", "type": "fill-blank", "lesson": "lesson.b1.erdelyaranykora.04", "teaches": ["kiterjeszt"], "prompt": "Egészítsd ki a mondatot a megfelelő igealakkal!", "sentence": "A törvény a szabadságjogokat a népre is *kiterjesztette*.", "target": "kiterjesztette"},
    {"id": "ex.b1.erdelyaranykora.04.06", "type": "sentence-builder", "lesson": "lesson.b1.erdelyaranykora.04", "teaches": ["amelyek", "kozul"], "prompt": "Alkoss összetett mondatot!", "chips": ["Várakat", "kapott,", "amelyek", "közül", "Patak", "volt", "a", "fő."], "target": "Várakat kapott, amelyek közül Patak volt a fő.", "english": "He received fortresses, among which Patak was the principal one."},
    {"id": "ex.b1.erdelyaranykora.04.07", "type": "multiple-choice", "lesson": "lesson.b1.erdelyaranykora.04", "teaches": ["linzi-beke-1645"], "prompt": "Hány felső-magyarországi vármegyét kapott meg Erdély a linzi békében?", "options": ["Hét vármegyét", "Három vármegyét", "Egyet sem", "Az egész országot"], "correctIndex": 0, "explanation": "A linzi béke értelmében hét vármegye került a fejedelem élethossziglani fennhatósága alá."},
    {"id": "ex.b1.erdelyaranykora.04.08", "type": "fill-blank", "lesson": "lesson.b1.erdelyaranykora.04", "teaches": ["szabadsagjog"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A bécsi udvarnak tiszteletben kellett tartania a nemesi *szabadságjogokat*.", "target": "szabadságjogokat"}
]
write_json(EXERCISES_DIR / "ex.b1.erdelyaranykora.04.json", make_exercise_group("ex.b1.erdelyaranykora.04", "A linzi béke gyakorlatai", "Gyakorlatok az 1645-ös békéről és az összetett vonatkozó névmásokról.", exs_4))

lesson_4 = make_lesson(
    "lesson.b1.erdelyaranykora.04",
    "I. Rákóczi György és a linzi béke (1645)",
    "Összetett vonatkozó névmások (amelyek közül, aminek következtében)",
    "Megtanuljuk I. Rákóczi György harmincéves háborús szerepvállalását és a linzi béke jobbágyvédelmi cikkelyeit.",
    ["Megérteni az 1645-ös linzi béke fontosságát", "Használni az összetett vonatkozó névmási szerkezeteket", "Ismerni Sárospatak és a Rákóczi család történelmi szerepét"],
    "story.b1.erdelyaranykora.04",
    "voc.b1.erdelyaranykora.04",
    "gr.b1.erdelyaranykora.04",
    "ex.b1.erdelyaranykora.04",
    [e["id"] for e in exs_4]
)
write_json(LESSONS_DIR / "lesson.b1.erdelyaranykora.04.json", lesson_4)


# ==========================================
# LESSON 5: b1-erdelyaranykora-05 (Erdély és a magyar kultúra)
# ==========================================
story_5 = make_story(
    "story.b1.erdelyaranykora.05",
    "Erdély és a magyar kultúra megőrzése (Vizsolyi Biblia, kollégiumok)",
    "A hódoltság másfél évszázada alatt Erdély és a Partium mentette meg és fejlesztette tovább a magyar anyanyelvi kultúrát, könyvnyomtatást és oktatást.",
    "Vizsoly, Debrecen és Sárospatak",
    ["Synthesizing paired conjunctions (nemcsak... hanem... is, egyrészt... másrészt)", "Cultural heritage of the Reformation"],
    ["Vizsolyi Biblia", "Károli Gáspár", "anyanyelv", "kollégium", "Apáczai Csere János"],
    [
        "Miközben az ország középső része a török uralom alatt pusztult, a keleti országrészben valóságos anyanyelvi kulturális forradalom ment végbe. 1590-ben Vizsolyban megjelent az első teljes magyar nyelvű Szentírás, a Károli Gáspár által lefordított Vizsolyi Biblia, amely az irodalmi magyar nyelv legfőbb alapkövévé vált.",
        "A reformáció szellemében virágzásnak indultak a protestáns kollégiumok Debrecenben, Sárospatakon és Kolozsváron. Ezek az intézmények nemcsak a lelkészképzést szolgálták, hanem korszerű természettudományos és társadalmi ismereteket is nyújtottak a polgárság és a parasztság gyermekeinek.",
        "Egyrészt a Comeniushoz hasonló európai tudósok meghívása, másrészt Apáczai Csere János első magyar enciklopédiája (1653) megteremtette az anyanyelvű tudományosságot. Mindezek révén Erdély nemcsak politikai menedéket, hanem a magyar szellemi élet örök túlélését is biztosította."
    ],
    [
        {"lemma": "anyanyelv", "pos": "noun", "cefr": "B1", "gloss": "mother tongue, native language"},
        {"lemma": "alapkő", "pos": "noun", "cefr": "B1", "gloss": "cornerstone, foundational stone"},
        {"lemma": "kollégium", "pos": "noun", "cefr": "B1", "gloss": "reformed college, academic academy"},
        {"lemma": "enciklopédia", "pos": "noun", "cefr": "B1", "gloss": "encyclopedia"},
        {"lemma": "menedék", "pos": "noun", "cefr": "B1", "gloss": "refuge, haven, shelter"}
    ],
    [
        {
            "question": "Ki fordította le az első teljes magyar nyelvű Bibliát (Vizsolyi Biblia, 1590)?",
            "options": ["Károli Gáspár", "Apáczai Csere János", "Dávid Ferenc", "Pázmány Péter"],
            "correctIndex": 0,
            "explanation": "Károli Gáspár gönci lelkész fordította le a teljes Bibliát magyar nyelvre Vizsolyban 1590-ben."
        }
    ]
)
write_json(STORIES_DIR / "story.b1.erdelyaranykora.05.json", story_5)

voc_5 = {
    "id": "voc.b1.erdelyaranykora.05",
    "title": "A magyar anyanyelvi műveltség szókincse",
    "description": "Anyanyelv, bibliafordítás, kollégiumok, enciklopédia és szellemi menedék.",
    "entries": [
        {"lemma": "anyanyelv", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "mother tongue, native language", "examples": [{"hu": "A reformáció az anyanyelv használatát hirdette.", "en": "The Reformation advocated the use of the mother tongue."}]}]},
        {"lemma": "alapkő", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "cornerstone, foundation", "examples": [{"hu": "A Vizsolyi Biblia az irodalmi nyelv alapköve.", "en": "The Vizsoly Bible is the cornerstone of the literary language."}]}]},
        {"lemma": "kollégium", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "reformed higher college/academy", "examples": [{"hu": "A debreceni kollégium a magyar oktatás bástyája volt.", "en": "The college of Debrecen was a bastion of Hungarian education."}]}]},
        {"lemma": "enciklopédia", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "encyclopedia of science and arts", "examples": [{"hu": "Apáczai megírta az első magyar nyelvű enciklopédiát.", "en": "Apáczai wrote the first encyclopedia in the Hungarian language."}]}]},
        {"lemma": "menedék", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "safe haven, cultural refuge", "examples": [{"hu": "Erdély a magyar kultúra menedéke lett a nehéz időkben.", "en": "Transylvania became the refuge of Hungarian culture in hard times."}]}]}
    ]
}
write_json(VOCAB_DIR / "voc.b1.erdelyaranykora.05.json", voc_5)

gr_5 = {
    "id": "gr.b1.erdelyaranykora.05",
    "title": "Páros kötőszavak és szintézis (nemcsak... hanem... is, egyrészt... másrészt)",
    "description": "Creating balanced, synthesized arguments in B1 cultural essays.",
    "rules": [
        "A 'nemcsak... hanem... is' páros kötőszó a halmozást, két pozitív tényező együttes jelenlétét erősíti meg.",
        "Az 'egyrészt... másrészt' szerkezet a különböző szempontok kiegyensúlyozott bemutatására szolgál."
    ],
    "tables": [
        {"headers": ["Páros kötőszó", "Funkció", "Példa"], "rows": [
            ["nemcsak... hanem... is", "hozzáadás, nyomatékosítás", "Nemcsak a hitet, hanem a nyelvet is védték."],
            ["egyrészt... másrészt", "két szempont felosztása", "Egyrészt iskolákat alapítottak, másrészt könyveket nyomtattak."]
        ]}
    ],
    "examples": [
        {"spanish": "A kollégiumok nemcsak lelkészeket képeztek, hanem tudósokat is neveltek.", "english": "The colleges not only trained preachers, but also educated scientists."},
        {"spanish": "Egyrészt a Biblia fordítása, másrészt az enciklopédia terjesztette az anyanyelvet.", "english": "On the one hand the translation of the Bible, on the other hand the encyclopedia spread the native language."},
        {"spanish": "Erdély nemcsak menedéket nyújtott, hanem fejlesztette is a kultúrát.", "english": "Transylvania not only provided refuge, but also developed the culture."}
    ]
}
write_json(GRAMMAR_DIR / "gr.b1.erdelyaranykora.05.json", gr_5)

exs_5 = [
    {"id": "ex.b1.erdelyaranykora.05.01", "type": "multiple-choice", "lesson": "lesson.b1.erdelyaranykora.05", "teaches": ["Vizsolyi-Biblia"], "prompt": "Melyik évben jelent meg a Vizsolyi Biblia, az első teljes magyar nyelvű Biblia?", "options": ["1590-ben", "1526-ban", "1568-ban", "1686-ban"], "correctIndex": 0, "explanation": "A Vizsolyi Biblia 1590-ben látott napvilágot Károli Gáspár fordításában."},
    {"id": "ex.b1.erdelyaranykora.05.02", "type": "fill-blank", "lesson": "lesson.b1.erdelyaranykora.05", "teaches": ["Karoli-Gaspar"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A teljes magyar Bibliát *Károli Gáspár* és munkatársai fordították le.", "target": "Károli Gáspár"},
    {"id": "ex.b1.erdelyaranykora.05.03", "type": "sentence-builder", "lesson": "lesson.b1.erdelyaranykora.05", "teaches": ["nemcsak", "hanem"], "prompt": "Rakd össze a páros kötőszavas mondatot!", "chips": ["Nemcsak", "a", "hitet,", "hanem", "a", "nyelvet", "is", "őrizték."], "target": "Nemcsak a hitet, hanem a nyelvet is őrizték.", "english": "They preserved not only the faith, but also the language."},
    {"id": "ex.b1.erdelyaranykora.05.04", "type": "multiple-choice", "lesson": "lesson.b1.erdelyaranykora.05", "teaches": ["kollegium"], "prompt": "Melyik városok voltak a leghíresebb protestáns kollégiumok központjai?", "options": ["Debrecen, Sárospatak és Kolozsvár", "Szeged, Pécs és Győr", "Esztergom és Székesfehérvár", "Bécs és Pozsony"], "correctIndex": 0, "explanation": "Debrecen, Sárospatak és Kolozsvár voltak a híres kollégiumi központok."},
    {"id": "ex.b1.erdelyaranykora.05.05", "type": "fill-blank", "lesson": "lesson.b1.erdelyaranykora.05", "teaches": ["alapko"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A Vizsolyi Biblia a magyar irodalmi nyelv legfontosabb *alapköve*.", "target": "alapköve"},
    {"id": "ex.b1.erdelyaranykora.05.06", "type": "sentence-builder", "lesson": "lesson.b1.erdelyaranykora.05", "teaches": ["egyreszt", "masreszt"], "prompt": "Alkoss kiegyensúlyozott összetett mondatot!", "chips": ["Egyrészt", "iskolákat", "nyitottak,", "másrészt", "könyveket", "nyomtattak."], "target": "Egyrészt iskolákat nyitottak, másrészt könyveket nyomtattak.", "english": "On the one hand they opened schools, on the other hand they printed books."},
    {"id": "ex.b1.erdelyaranykora.05.07", "type": "multiple-choice", "lesson": "lesson.b1.erdelyaranykora.05", "teaches": ["Apaczai"], "prompt": "Ki írta az első magyar nyelvű tudományos összefoglalást (Magyar Encyclopaedia, 1653)?", "options": ["Apáczai Csere János", "Károli Gáspár", "Bethlen Gábor", "Szenci Molnár Albert"], "correctIndex": 0, "explanation": "Apáczai Csere János írta az első magyar nyelvű enciklopédiát 1653-ban."},
    {"id": "ex.b1.erdelyaranykora.05.08", "type": "fill-blank", "lesson": "lesson.b1.erdelyaranykora.05", "teaches": ["menedek"], "prompt": "Egészítsd ki a mondatot!", "sentence": "Erdély a magyar kultúra és nyelv biztonságos *menedéke* volt.", "target": "menedéke"}
]
write_json(EXERCISES_DIR / "ex.b1.erdelyaranykora.05.json", make_exercise_group("ex.b1.erdelyaranykora.05", "Erdély kulturális öröksége gyakorlatok", "Gyakorlatok a Vizsolyi Bibliáról, kollégiumokról és a páros kötőszavakról.", exs_5))

lesson_5 = make_lesson(
    "lesson.b1.erdelyaranykora.05",
    "Erdély és a magyar kultúra megőrzése (Vizsolyi Biblia, kollégiumok)",
    "Páros kötőszavak és szintézis (nemcsak... hanem... is, egyrészt... másrészt)",
    "Összegezzük Erdély kulturális misszióját: a Vizsolyi Biblia hatását, a debreceni és sárospataki kollégiumokat, és az anyanyelvi tudományosság megteremtését.",
    ["Megérteni a Vizsolyi Biblia (1590) és Károli Gáspár alapvető szerepét", "Használni a páros kötőszavakat összetett érvelésben", "Ismerni a protestáns kollégiumok és Apáczai Csere János örökségét"],
    "story.b1.erdelyaranykora.05",
    "voc.b1.erdelyaranykora.05",
    "gr.b1.erdelyaranykora.05",
    "ex.b1.erdelyaranykora.05",
    [e["id"] for e in exs_5]
)
write_json(LESSONS_DIR / "lesson.b1.erdelyaranykora.05.json", lesson_5)


# ==========================================
# CONSOLIDATION LESSON: b1-erdelyaranykora-consolidation
# ==========================================
cons_exs = [
    {"id": "ex.b1.erdelyaranykora.cons.01", "type": "multiple-choice", "lesson": "lesson.b1.erdelyaranykora.consolidation", "teaches": ["tordai-vallasbeke"], "prompt": "Melyik évben hozták meg a vallásszabadságot kimondó tordai határozatot?", "options": ["1568-ban", "1526-ban", "1606-ban", "1645-ben"], "correctIndex": 0, "explanation": "A tordai vallásbékét 1568-ban iktatták törvénybe."},
    {"id": "ex.b1.erdelyaranykora.cons.02", "type": "fill-blank", "lesson": "lesson.b1.erdelyaranykora.consolidation", "teaches": ["vallasszabadsag"], "prompt": "A tordai ediktum a világon elsőként mondta ki a *vallásszabadságot*.", "sentence": "A tordai ediktum a világon elsőként mondta ki a *vallásszabadságot*.", "target": "vallásszabadságot"},
    {"id": "ex.b1.erdelyaranykora.cons.03", "type": "multiple-choice", "lesson": "lesson.b1.erdelyaranykora.consolidation", "teaches": ["Bocskai-Istvan"], "prompt": "Kiknek a segítségével győzött Bocskai István a felkelésben?", "options": ["A fegyveres hajdúk segítségével", "A török janicsárok segítségével", "A francia tengerészekkel", "Csak külföldi zsoldosokkal"], "correctIndex": 0, "explanation": "Bocskai a fegyveres hajdúk élén aratott győzelmet."},
    {"id": "ex.b1.erdelyaranykora.cons.04", "type": "fill-blank", "lesson": "lesson.b1.erdelyaranykora.consolidation", "teaches": ["becsi-beke"], "prompt": "Az 1606-os *bécsi béke* garantálta a magyar rendi jogokat és a vallásszabadságot.", "sentence": "Az 1606-os *bécsi béke* garantálta a magyar rendi jogokat és a vallásszabadságot.", "target": "bécsi béke"},
    {"id": "ex.b1.erdelyaranykora.cons.05", "type": "sentence-builder", "lesson": "lesson.b1.erdelyaranykora.consolidation", "teaches": ["ugy", "garantal"], "prompt": "Rakd össze a következményes mondatot!", "chips": ["Úgy", "harcoltak,", "hogy", "megvédték", "a", "rendi", "jogokat."], "target": "Úgy harcoltak, hogy megvédték a rendi jogokat.", "english": "They fought in such a way that they defended estate rights."},
    {"id": "ex.b1.erdelyaranykora.cons.06", "type": "multiple-choice", "lesson": "lesson.b1.erdelyaranykora.consolidation", "teaches": ["Bethlen-Gabor"], "prompt": "Ki volt Erdély fejedelme a fejedelemség gazdasági és kulturális aranykorában (1613–1629)?", "options": ["Bethlen Gábor", "Bocskai István", "János Zsigmond", "Szapolyai János"], "correctIndex": 0, "explanation": "Bethlen Gábor uralkodása volt Erdély aranykora."},
    {"id": "ex.b1.erdelyaranykora.cons.07", "type": "fill-blank", "lesson": "lesson.b1.erdelyaranykora.consolidation", "teaches": ["Gyulafehervar"], "prompt": "Bethlen Gábor fejedelmi központja *Gyulafehérvár* volt.", "sentence": "Bethlen Gábor fejedelmi központja *Gyulafehérvár* volt.", "target": "Gyulafehérvár"},
    {"id": "ex.b1.erdelyaranykora.cons.08", "type": "sentence-builder", "lesson": "lesson.b1.erdelyaranykora.consolidation", "teaches": ["reven", "monopolium"], "prompt": "Rakd össze a mondatot!", "chips": ["Monopóliumok", "révén", "gyarapodott", "az", "erdélyi", "kincstár."], "target": "Monopóliumok révén gyarapodott az erdélyi kincstár.", "english": "Through monopolies, the Transylvanian treasury prospered."},
    {"id": "ex.b1.erdelyaranykora.cons.09", "type": "multiple-choice", "lesson": "lesson.b1.erdelyaranykora.consolidation", "teaches": ["linzi-beke"], "prompt": "Melyik évben kötötték meg a jobbágyok vallásszabadságát is biztosító linzi békét?", "options": ["1645-ben", "1606-ban", "1568-ban", "1590-ben"], "correctIndex": 0, "explanation": "A linzi békét 1645-ben kötötte I. Rákóczi György."},
    {"id": "ex.b1.erdelyaranykora.cons.10", "type": "fill-blank", "lesson": "lesson.b1.erdelyaranykora.consolidation", "teaches": ["jobbagy"], "prompt": "A linzi szerződés a *jobbágyok* szabad vallásgyakorlását is elismerte.", "sentence": "A linzi szerződés a *jobbágyok* szabad vallásgyakorlását is elismerte.", "target": "jobbágyok"},
    {"id": "ex.b1.erdelyaranykora.cons.11", "type": "sentence-builder", "lesson": "lesson.b1.erdelyaranykora.consolidation", "teaches": ["aminek", "kovetkezteben"], "prompt": "Alkoss összetett mondatot a helyes névmással!", "chips": ["Békét", "kötöttek,", "aminek", "következtében", "megerősödtek", "a", "jogok."], "target": "Békét kötöttek, aminek következtében megerősödtek a jogok.", "english": "They made peace, as a result of which rights were strengthened."},
    {"id": "ex.b1.erdelyaranykora.cons.12", "type": "multiple-choice", "lesson": "lesson.b1.erdelyaranykora.consolidation", "teaches": ["Vizsolyi-Biblia-1590"], "prompt": "Mikor és hol jelent meg az első teljes magyar nyelvű Biblia?", "options": ["1590-ben Vizsolyban", "1568-ban Tordán", "1606-ban Bécsben", "1645-ben Linzben"], "correctIndex": 0, "explanation": "A Vizsolyi Biblia 1590-ben jelent meg Károli Gáspár fordításában."},
    {"id": "ex.b1.erdelyaranykora.cons.13", "type": "fill-blank", "lesson": "lesson.b1.erdelyaranykora.consolidation", "teaches": ["Karoli-Gaspar"], "prompt": "A Vizsolyi Bibliát *Károli Gáspár* gönci prédikátor fordította magyarra.", "sentence": "A Vizsolyi Bibliát *Károli Gáspár* gönci prédikátor fordította magyarra.", "target": "Károli Gáspár"},
    {"id": "ex.b1.erdelyaranykora.cons.14", "type": "sentence-builder", "lesson": "lesson.b1.erdelyaranykora.consolidation", "teaches": ["nemcsak", "hanem"], "prompt": "Rakd össze a páros szerkezetet!", "chips": ["Nemcsak", "az", "iskolákat,", "hanem", "a", "tudományt", "is", "támogatták."], "target": "Nemcsak az iskolákat, hanem a tudományt is támogatták.", "english": "They supported not only the schools, but also science."},
    {"id": "ex.b1.erdelyaranykora.cons.15", "type": "multiple-choice", "lesson": "lesson.b1.erdelyaranykora.consolidation", "teaches": ["Apaczai-Csere-Janos"], "prompt": "Mi fűződik Apáczai Csere János nevéhez?", "options": ["Az első magyar nyelvű enciklopédia megírása (1653)", "A budai vár visszavétele", "A hajdúk letelepítése", "A déli harangszó elrendelése"], "correctIndex": 0, "explanation": "Apáczai Csere János írta az első magyar enciklopédiát 1653-ban."},
    {"id": "ex.b1.erdelyaranykora.cons.16", "type": "fill-blank", "lesson": "lesson.b1.erdelyaranykora.consolidation", "teaches": ["alapko"], "prompt": "A magyar bibliafordítás a nemzeti nyelv legfőbb *alapköve* lett.", "sentence": "A magyar bibliafordítás a nemzeti nyelv legfőbb *alapköve* lett.", "target": "alapköve"},
    {"id": "ex.b1.erdelyaranykora.cons.17", "type": "sentence-builder", "lesson": "lesson.b1.erdelyaranykora.consolidation", "teaches": ["egyreszt", "masreszt"], "prompt": "Alkoss kiegyensúlyozott mondatot!", "chips": ["Egyrészt", "virágzott", "a", "gazdaság,", "másrészt", "fejlődött", "az", "oktatás."], "target": "Egyrészt virágzott a gazdaság, másrészt fejlődött az oktatás.", "english": "On the one hand the economy flourished, on the other hand education developed."},
    {"id": "ex.b1.erdelyaranykora.cons.18", "type": "multiple-choice", "lesson": "lesson.b1.erdelyaranykora.consolidation", "teaches": ["bevett-felekezetek"], "prompt": "Melyik NEM volt az 1568-ban elismert négy bevett vallás egyike?", "options": ["Iszlám", "Katolikus", "Református", "Unitárius"], "correctIndex": 0, "explanation": "A négy bevett vallás: katolikus, református, evangélikus és unitárius volt."},
    {"id": "ex.b1.erdelyaranykora.cons.19", "type": "fill-blank", "lesson": "lesson.b1.erdelyaranykora.consolidation", "teaches": ["menedek"], "prompt": "Erdély a magyar anyanyelvi kultúra és államiság *menedéke* volt másfél évszázadon át.", "sentence": "Erdély a magyar anyanyelvi kultúra és államiság *menedéke* volt másfél évszázadon át.", "target": "menedéke"},
    {"id": "ex.b1.erdelyaranykora.cons.20", "type": "multiple-choice", "lesson": "lesson.b1.erdelyaranykora.consolidation", "teaches": ["Sarospatak-Lorafftffy"], "prompt": "Ki volt I. Rákóczi György felesége, a sárospataki kollégium nagy mecénása?", "options": ["Lorántffy Zsuzsanna", "Szilágyi Erzsébet", "Zrínyi Ilona", "Kanizsai Dorottya"], "correctIndex": 0, "explanation": "Lorántffy Zsuzsanna fejedelemasszony virágoztatta fel a sárospataki kollégiumot."}
]
write_json(EXERCISES_DIR / "ex.b1.erdelyaranykora.consolidation.json", make_exercise_group("ex.b1.erdelyaranykora.consolidation", "Erdély aranykora összefoglaló gyakorlatok", "Átfogó teszt az Erdélyi Fejedelemség virágkoráról és a tanult nyelvtani szerkezetekről.", cons_exs))

cons_lesson = {
    "id": "lesson.b1.erdelyaranykora.consolidation",
    "title": "Transylvania's Golden Age: Unit 11 Consolidation",
    "level": "B1",
    "track": "citizenship",
    "estimatedMinutes": 25,
    "prerequisites": [
        "lesson.b1.erdelyaranykora.01",
        "lesson.b1.erdelyaranykora.02",
        "lesson.b1.erdelyaranykora.03",
        "lesson.b1.erdelyaranykora.04",
        "lesson.b1.erdelyaranykora.05"
    ],
    "grammar": ["Unit review"],
    "vocabulary": ["Unit review"],
    "culturalContext": "Magyar történelem összefoglalás (Honosítási vizsgafelkészítő)",
    "sections": [
        {
            "type": "intro",
            "title": "Unit 11 Consolidation: Transylvania's Golden Age",
            "body": "Ebben az összefoglaló leckében átismételjük a tordai vallásbékét (1568), Bocskai István felkelését és a bécsi békét (1606), Bethlen Gábor aranykorát (1613–1629), a linzi békét (1645), valamint a Vizsolyi Biblia (1590) és a kollégiumok kultúrateremtő hatását."
        },
        {
            "type": "goal",
            "title": "Consolidation Goals",
            "items": [
                "Az Erdélyi Fejedelemség fejedelmeinek és békekötéseinek pontos ismerete",
                "Eszközhatározói (révén, által), következményes (úgy... hogy) és páros kötőszavak (nemcsak... hanem... is) alkalmazása",
                "A magyar anyanyelvi kultúra és vallásszabadság történeti fogalmainak birtoklása"
            ]
        },
        {
            "type": "exercise-group",
            "title": "Comprehensive Unit 11 Practice",
            "ref": "ex.b1.erdelyaranykora.consolidation",
            "exerciseRefs": [e["id"] for e in cons_exs]
        },
        {
            "type": "checklist",
            "items": [
                "Tudom, mikor és hol született meg a vallásszabadság törvénye (1568, Torda)",
                "Ismerem Bocskai Istvánt és a hajdúk letelepítését",
                "Tudom, miért volt Bethlen Gábor kora Erdély aranykora",
                "Ismerem a Vizsolyi Biblia (1590) és Károli Gáspár nevét és jelentőségét"
            ]
        }
    ]
}
write_json(LESSONS_DIR / "lesson.b1.erdelyaranykora.consolidation.json", cons_lesson)

print("Unit 11 (b1-erdelyaranykora) complete!")
