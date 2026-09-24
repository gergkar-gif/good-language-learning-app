# -*- coding: utf-8 -*-
"""
Full Unit 15 Overhaul: The Reform Age (b1-reformkor)
Lessons:
1. A reformkor hajnala és a Magyar Tudományos Akadémia alapítása (1825)
2. Gróf Széchenyi István, a 'legnagyobb magyar' és reformprogramja (Hitel 1830)
3. Kossuth Lajos, az érdekegyesítés és a független sajtó
4. Széchenyi és Kossuth vitája: két út a polgári átalakuláshoz
5. A magyar nyelv diadala: az 1844-es államnyelvi törvény és a nemzeti kultúra
Consolidation: Unit 15 Capstone (20 exercises)
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
# LESSON 1: b1-reformkor-01 (MTA alapítása 1825)
# ==========================================
story_1 = make_story(
    "story.b1.reformkor.01",
    "A reformkor hajnala és a Magyar Tudományos Akadémia alapítása (1825)",
    "1825-ben a pozsonyi országgyűlésen gróf Széchenyi István birtokainak egyévi teljes jövedelmét ajánlotta fel a Magyar Tudós Társaság (Akadémia) megalapítására.",
    "Pozsony",
    ["Proactive offering and purposive clauses (felajánl, abból a célból, hogy)", "Civic foundations in the Reform Era"],
    ["reformkor", "Széchenyi István", "Magyar Tudományos Akadémia", "birtokjövedelem", "nemzeti nyelv"],
    [
        "A 19. század első évtizedeiben a magyar nemesség felismerte, hogy a nemzet fennmaradásának és modernizációjának záloga az anyanyelv és a tudományok felvirágoztatása. Az 1825-ben összehívott pozsonyi országgyűlés nyitotta meg a magyar történelem dicsőséges időszakát, a reformkort (1825–1848).",
        "1825. november 3-án az alsótábla ülésén a nemesek éppen a magyar nyelv ügyéről és a pénzhiányról vitatkoztak, amikor a fiatal gróf Széchenyi István váratlanul szót kért. Kijelentette: 'Nekem nincs más szándékom, mint hazám javát előmozdítani' – és birtokainak teljes egyévi jövedelmét (60 000 forintot) ajánlotta fel egy tudós társaság megalapítására.",
        "Széchenyi nagylelkű példáját más főurak – mint Károlyi György és Teleki József – is követték. Ennek köszönhetően jött létre a Magyar Tudományos Akadémia, amely az anyanyelvi kultúra, a tudományos szókincs és az irodalom legfőbb intézményévé vált."
    ],
    [
        {"lemma": "reformkor", "pos": "noun", "cefr": "B1", "gloss": "Reform Era (1825–1848)"},
        {"lemma": "birtokjövedelem", "pos": "noun", "cefr": "B1", "gloss": "estate income / annual revenue"},
        {"lemma": "előmozdít", "pos": "verb", "cefr": "B1", "gloss": "to promote, advance, foster"},
        {"lemma": "nagylelkű", "pos": "adjective", "cefr": "B1", "gloss": "generous, magnanimous"},
        {"lemma": "tudós társaság", "pos": "noun", "cefr": "B1", "gloss": "learned society, academy"}
    ],
    [
        {
            "question": "Mit ajánlott fel gróf Széchenyi István az 1825-ös országgyűlésen?",
            "options": ["Birtokainak teljes egyévi jövedelmét a Magyar Tudományos Akadémia megalapítására", "A Lánchíd építési terveit", "Minden lovát a hadseregnek", "Egy nyomdagépet Pozsonyban"],
            "correctIndex": 0,
            "explanation": "Széchenyi egyévi birtokjövedelmét (60 000 forintot) ajánlotta fel a Tudós Társaságra."
        }
    ]
)
write_json(STORIES_DIR / "story.b1.reformkor.01.json", story_1)

voc_1 = {
    "id": "voc.b1.reformkor.01",
    "title": "A reformkor nyitányának szókincse",
    "description": "Reformkor, birtokjövedelem, előmozdítás, nagylelkűség és tudományos társaság.",
    "entries": [
        {"lemma": "reformkor", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "Reform Era in Hungary (1825–1848)", "examples": [{"hu": "A reformkor 1825-ben vette kezdetét.", "en": "The Reform Era began in 1825."}]}]},
        {"lemma": "birtokjövedelem", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "annual income generated from land estates", "examples": [{"hu": "Széchenyi egyévi birtokjövedelmét adományozta a nemzetnek.", "en": "Széchenyi donated one year of his estate income to the nation."}]}]},
        {"lemma": "előmozdít", "pos": "verb", "cefr": "B1", "definitions": [{"meaning": "to advance, foster national progress", "examples": [{"hu": "Minden tettével a haza javát mozdította elő.", "en": "With all his actions he advanced the good of the homeland."}]}]},
        {"lemma": "nagylelkű", "pos": "adjective", "cefr": "B1", "definitions": [{"meaning": "generous, noble-minded", "examples": [{"hu": "A gróf nagylelkű felajánlása megindította a nemzetet.", "en": "The count's generous offer moved the nation."}]}]},
        {"lemma": "tudós társaság", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "learned academy, scientific society", "examples": [{"hu": "A Tudós Társaság a magyar nyelv fejlesztésére jött létre.", "en": "The Learned Society was created to develop the Hungarian language."}]}]}
    ]
}
write_json(VOCAB_DIR / "voc.b1.reformkor.01.json", voc_1)

gr_1 = {
    "id": "gr.b1.reformkor.01",
    "title": "Célhatározói és felajánló szerkezetek (felajánl, abból a célból, hogy, előmozdít)",
    "description": "Expressing philanthropic acts, civic pledges, and purposeful contributions.",
    "rules": [
        "A 'felajánl valamit valamire / valamely célra' vonzat a közjóért hozott anyagi vagy erkölcsi áldozatot fejezi ki.",
        "A 'céljából' vagy 'abból a célból, hogy' összetett mondatszerkezet világosan rögzíti a társadalmi törekvést."
    ],
    "tables": [
        {"headers": ["Szerkezet", "Jelentés", "Példa"], "rows": [
            ["felajánl valamit valamire", "to donate/pledge for", "Jövedelmét az Akadémiára ajánlotta fel."],
            ["abból a célból, hogy...", "with the aim that", "Azzal a céllal hozta létre, hogy művelje a nyelvet."],
            ["előmozdít", "to foster/promote", "A tudományt kívánta előmozdítani."]
        ]}
    ],
    "examples": [
        {"spanish": "Széchenyi birtokainak jövedelmét abból a célból ajánlotta fel, hogy megalapítsák az Akadémiát.", "english": "Széchenyi offered his estates' income with the purpose of founding the Academy."},
        {"spanish": "A nemesek követték példáját, támogatva az anyanyelv fejlődését.", "english": "The nobles followed his example, supporting the development of the mother tongue."},
        {"spanish": "Az 1825-ös országgyűlés elindította a polgári átalakulást.", "english": "The 1825 Diet initiated the civic transformation."}
    ]
}
write_json(GRAMMAR_DIR / "gr.b1.reformkor.01.json", gr_1)

exs_1 = [
    {"id": "ex.b1.reformkor.01.01", "type": "multiple-choice", "lesson": "lesson.b1.reformkor.01", "teaches": ["reformkor-kezdet"], "prompt": "Melyik évhez kötjük a reformkor kezdetét a magyar történelemben?", "options": ["1825-höz (az Akadémia felajánlásához)", "1848-hoz", "1800-hoz", "1867-hez"], "correctIndex": 0, "explanation": "A reformkor nyitánya az 1825-ös pozsonyi országgyűlés volt."},
    {"id": "ex.b1.reformkor.01.02", "type": "fill-blank", "lesson": "lesson.b1.reformkor.01", "teaches": ["birtokjovedelem"], "prompt": "Egészítsd ki a mondatot!", "sentence": "Széchenyi István egyévi teljes *birtokjövedelmét* ajánlotta fel a nemzetnek.", "target": "birtokjövedelmét"},
    {"id": "ex.b1.reformkor.01.03", "type": "sentence-builder", "lesson": "lesson.b1.reformkor.01", "teaches": ["felajanl", "akademia"], "prompt": "Rakd össze a mondatot a helyes sorrendben!", "chips": ["Széchenyi", "pénzt", "ajánlott", "fel", "az", "Akadémia", "megalapítására."], "target": "Széchenyi pénzt ajánlott fel az Akadémia megalapítására.", "english": "Széchenyi offered money for the foundation of the Academy."},
    {"id": "ex.b1.reformkor.01.04", "type": "multiple-choice", "lesson": "lesson.b1.reformkor.01", "teaches": ["Szechenyi-Istvan"], "prompt": "Hogyan nevezte Kossuth Lajos gróf Széchenyi Istvánt?", "options": ["'A legnagyobb magyarnak'", "'A haza bölcsének'", "'A nemzet csalogányának'", "'A hadak villámának'"], "correctIndex": 0, "explanation": "Kossuth Széchenyit 'a legnagyobb magyarnak' nevezte."},
    {"id": "ex.b1.reformkor.01.05", "type": "fill-blank", "lesson": "lesson.b1.reformkor.01", "teaches": ["elomozdit"], "prompt": "Egészítsd ki a mondatot a megfelelő igealakkal!", "sentence": "Minden reform a haza fejlődését *mozdította elő*.", "target": "mozdította elő"},
    {"id": "ex.b1.reformkor.01.06", "type": "sentence-builder", "lesson": "lesson.b1.reformkor.01", "teaches": ["nagylelku", "adomany"], "prompt": "Alkoss szabályos mondatot!", "chips": ["A", "nagylelkű", "adomány", "lehetővé", "tette", "a", "tudomány", "fejlődését."], "target": "A nagylelkű adomány lehetővé tette a tudomány fejlődését.", "english": "The generous donation made the development of science possible."},
    {"id": "ex.b1.reformkor.01.07", "type": "multiple-choice", "lesson": "lesson.b1.reformkor.01", "teaches": ["Tudos-Tarsasag"], "prompt": "Mi volt a Magyar Tudományos Akadémia eredeti neve 1825-ben?", "options": ["Magyar Tudós Társaság", "Királyi Akadémia", "Nemzeti Múzeum", "Pesti Egyetem"], "correctIndex": 0, "explanation": "Kezdetben Magyar Tudós Társaságnak nevezték az Akadémiát."},
    {"id": "ex.b1.reformkor.01.08", "type": "fill-blank", "lesson": "lesson.b1.reformkor.01", "teaches": ["reformkor"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A *reformkor* Magyarország gazdasági és szellemi megújulásának korszaka.", "target": "reformkor"}
]
write_json(EXERCISES_DIR / "ex.b1.reformkor.01.json", make_exercise_group("ex.b1.reformkor.01", "A reformkor nyitánya gyakorlatok", "Gyakorlatok az 1825-ös országgyűlésről, Széchenyiről és a felajánló szerkezetekről.", exs_1))

lesson_1 = make_lesson(
    "lesson.b1.reformkor.01",
    "A reformkor hajnala és a Magyar Tudományos Akadémia alapítása (1825)",
    "Célhatározói és felajánló szerkezetek (felajánl valamire, előmozdít)",
    "Megismerjük a reformkor kezdetét, Széchenyi István 1825-ös nagylelkű felajánlását és az Akadémia megalakulását.",
    ["Megérteni a reformkor (1825–1848) korszakhatárát és céljait", "Használni a felajánlást és célt kifejező nyelvtani formákat", "Ismerni Széchenyi István és a Magyar Tudományos Akadémia szerepét"],
    "story.b1.reformkor.01",
    "voc.b1.reformkor.01",
    "gr.b1.reformkor.01",
    "ex.b1.reformkor.01",
    [e["id"] for e in exs_1]
)
write_json(LESSONS_DIR / "lesson.b1.reformkor.01.json", lesson_1)


# ==========================================
# LESSON 2: b1-reformkor-02 (Széchenyi reformprogramja és alkotásai)
# ==========================================
story_2 = make_story(
    "story.b1.reformkor.02",
    "Gróf Széchenyi István, a 'legnagyobb magyar' és reformprogramja (Hitel 1830)",
    "Széchenyi István 'Hitel' című művével elindította a feudális gazdaság átalakítását, miközben gőzhajózással, a Lánchíddal és a folyók szabályozásával modernizálta a hazát.",
    "Pest-Buda és a Vaskapu",
    ["Socio-economic reform arguments (szükségesnek tart, korszerűsít, akadály)", "Infrastructure and modernization"],
    ["Széchenyi István", "Hitel", "Lánchíd", "Duna-szabályozás", "ősiség törvénye"],
    [
        "1830-ban jelent meg gróf Széchenyi István korszakos műve, a 'Hitel', amely rávilágított arra, hogy a feudális törvények (mint az 1351-es ősiség) gátolják a birtokok modernizálását, mivel a nemesek nem kaphatnak banki hitelt a földjeikre. Széchenyi ezt követően a 'Világ' és a 'Stádium' című könyveiben 12 pontban foglalta össze a gazdasági átalakulás programját.",
        "Széchenyi nemcsak elméleti gondolkodó, hanem a gyakorlati alkotások embere is volt. Kezdeményezésére és finanszírozásával épült meg a Buda és Pest közötti első állandó kőhíd, a Lánchíd (Clark Ádám tervei alapján), amelyen az arisztokratáknak is hídvámot kellett fizetniük, áttörve a nemesi adómentességet.",
        "Nevéhez fűződik a Duna és a Tisza szabályozása, a Vaskapu hajózhatóvá tétele, a balatoni és dunai gőzhajózás megindítása, a lóversenyzés és a Nemzeti Kaszinó megalapítása. Mindezekkel Széchenyi kiérdemelte a kortársaktól és az utókortól a 'legnagyobb magyar' megtisztelő címet."
    ],
    [
        {"lemma": "ősiség törvénye", "pos": "noun", "cefr": "B1", "gloss": "law of aviticitas / inalienability of noble estates"},
        {"lemma": "korszerűsít", "pos": "verb", "cefr": "B1", "gloss": "to modernize, upgrade"},
        {"lemma": "gátol", "pos": "verb", "cefr": "B1", "gloss": "to hinder, obstruct, impede"},
        {"lemma": "hídvám", "pos": "noun", "cefr": "B1", "gloss": "bridge toll"},
        {"lemma": "folyószabályozás", "pos": "noun", "cefr": "B1", "gloss": "river regulation / canalization"}
    ],
    [
        {
            "question": "Melyik híres könyvet írta Széchenyi István 1830-ban a gazdasági elmaradottság felszámolására?",
            "options": ["Hitel", "Világ", "Stádium", "Kelet Népe"],
            "correctIndex": 0,
            "explanation": "Széchenyi 1830-ban kiadott 'Hitel' című könyve indította el a reformmozgalmat."
        }
    ]
)
write_json(STORIES_DIR / "story.b1.reformkor.02.json", story_2)

voc_2 = {
    "id": "voc.b1.reformkor.02",
    "title": "A polgári átalakulás és modernizáció szókincse",
    "description": "Hitel, ősiség, Lánchíd, korszerűsítés, gátlás és folyószabályozás.",
    "entries": [
        {"lemma": "ősiség törvénye", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "feudal law preventing sale and mortgage of noble land", "examples": [{"hu": "Az ősiség törvénye akadályozta a birtokosokat a hitelfelvételben.", "en": "The law of aviticitas prevented landowners from taking loans."}]}]},
        {"lemma": "korszerűsít", "pos": "verb", "cefr": "B1", "definitions": [{"meaning": "to modernize infrastructure and economy", "examples": [{"hu": "Széchenyi gőzhajókkal korszerűsítette a közlekedést.", "en": "Széchenyi modernized transport with steamboats."}]}]},
        {"lemma": "gátol", "pos": "verb", "cefr": "B1", "definitions": [{"meaning": "to impede, hinder progress", "examples": [{"hu": "A feudális szokások gátolták a fejlődést.", "en": "Feudal customs impeded development."}]}]},
        {"lemma": "hídvám", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "bridge toll paid by all travelers", "examples": [{"hu": "A Lánchídon a nemesek is kötelesek voltak hídvámot fizetni.", "en": "On the Chain Bridge, nobles too were obliged to pay bridge toll."}]}]},
        {"lemma": "folyószabályozás", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "river engineering, flood control regulation", "examples": [{"hu": "A Duna szabályozása biztonságossá tette a hajózást.", "en": "The regulation of the Danube made navigation safe."}]}]}
    ]
}
write_json(VOCAB_DIR / "voc.b1.reformkor.02.json", voc_2)

gr_2 = {
    "id": "gr.b1.reformkor.02",
    "title": "Korszerűsítést és akadályoztatást kifejező szerkezetek (gátol, korszerűsít, lehetővé tesz)",
    "description": "Expressing modernization, social obstacles, and reform initiatives.",
    "rules": [
        "A fejlődést és reformokat leíró igék ('korszerűsít', 'lehetővé tesz', 'megvalósít') pozitív eredményeket mutatnak be.",
        "A korlátokat a 'gátol', 'akadályoz', 'nehezíti a...' kifejezésekkel szemléltetjük."
    ],
    "tables": [
        {"headers": ["Ige / Szerkezet", "Jelentés", "Példa"], "rows": [
            ["korszerűsít", "to modernize", "Korszerűsítette a mezőgazdaságot."],
            ["lehetővé tesz", "to make possible", "A hitel lehetővé tette az építkezést."],
            ["gátolja a fejlődést", "to hinder progress", "Az ősiség gátolta a fejlődést."]
        ]}
    ],
    "examples": [
        {"spanish": "A bankhitel hiánya gátolta a magyar birtokosok fejlődését.", "english": "The lack of bank credit hindered the development of Hungarian landowners."},
        {"spanish": "A Lánchíd megépítése lehetővé tette Pest és Buda egyesülését.", "english": "The construction of the Chain Bridge made the unification of Pest and Buda possible."},
        {"spanish": "Széchenyi István a gyakorlatban korszerűsítette a folyami hajózást.", "english": "István Széchenyi modernized river navigation in practice."}
    ]
}
write_json(GRAMMAR_DIR / "gr.b1.reformkor.02.json", gr_2)

exs_2 = [
    {"id": "ex.b1.reformkor.02.01", "type": "multiple-choice", "lesson": "lesson.b1.reformkor.02", "teaches": ["Hitel-1830"], "prompt": "Melyik évben jelent meg Széchenyi István korszakos műve, a Hitel?", "options": ["1830-ban", "1825-ben", "1844-ben", "1848-ban"], "correctIndex": 0, "explanation": "A 'Hitel' 1830-ban látott napvilágot."},
    {"id": "ex.b1.reformkor.02.02", "type": "fill-blank", "lesson": "lesson.b1.reformkor.02", "teaches": ["Lanchid"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A Buda és Pest közötti első állandó hidat, a *Lánchidat* Széchenyi kezdeményezésére építették.", "target": "Lánchidat"},
    {"id": "ex.b1.reformkor.02.03", "type": "sentence-builder", "lesson": "lesson.b1.reformkor.02", "teaches": ["gatol", "fejlodes"], "prompt": "Rakd össze az akadályoztatást kifejező mondatot!", "chips": ["A", "feudális", "törvények", "gátolták", "a", "gazdasági", "fejlődést."], "target": "A feudális törvények gátolták a gazdasági fejlődést.", "english": "Feudal laws hindered economic development."},
    {"id": "ex.b1.reformkor.02.04", "type": "multiple-choice", "lesson": "lesson.b1.reformkor.02", "teaches": ["hidvam-nemesek"], "prompt": "Miért volt forradalmi a Lánchíd hídvámja?", "options": ["Mert a nemeseknek is kötelező volt megfizetniük (áttörve az adómentességet)", "Mert ingyenes volt mindenkinek", "Mert arannyal kellett fizetni", "Mert csak a külföldiek fizettek"], "correctIndex": 0, "explanation": "A nemesek hídvámfizetése az első lépés volt a közteherviselés felé."},
    {"id": "ex.b1.reformkor.02.05", "type": "fill-blank", "lesson": "lesson.b1.reformkor.02", "teaches": ["korszerusit"], "prompt": "Egészítsd ki a mondatot a megfelelő igealakkal!", "sentence": "Széchenyi gőzhajózással *korszerűsítette* a magyar folyami közlekedést.", "target": "korszerűsítette"},
    {"id": "ex.b1.reformkor.02.06", "type": "sentence-builder", "lesson": "lesson.b1.reformkor.02", "teaches": ["lehetove-tesz", "Duna"], "prompt": "Alkoss szabályos összetett mondatot!", "chips": ["A", "folyószabályozás", "lehetővé", "tette", "a", "biztonságos", "hajózást."], "target": "A folyószabályozás lehetővé tette a biztonságos hajózást.", "english": "The river regulation made safe navigation possible."},
    {"id": "ex.b1.reformkor.02.07", "type": "multiple-choice", "lesson": "lesson.b1.reformkor.02", "teaches": ["Szechenyi-alkotasok"], "prompt": "Melyik NEM Széchenyi István nevéhez fűződik az alábbiak közül?", "options": ["A kiegyezés aláírása 1867-ben", "A Lánchíd megépítése", "A Duna és a Tisza szabályozása", "A Nemzeti Kaszinó és a gőzhajózás"], "correctIndex": 0, "explanation": "A kiegyezés (1867) Deák Ferenc nevéhez fűződik; Széchenyi 1860-ban meghalt."},
    {"id": "ex.b1.reformkor.02.08", "type": "fill-blank", "lesson": "lesson.b1.reformkor.02", "teaches": ["folyoszabalyozas"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A Vaskapu szikláinak átvágásával megvalósult a Duna *folyószabályozása*.", "target": "folyószabályozása"}
]
write_json(EXERCISES_DIR / "ex.b1.reformkor.02.json", make_exercise_group("ex.b1.reformkor.02", "Széchenyi István alkotásai gyakorlatok", "Gyakorlatok a Hitelről, a Lánchídról és a korszerűsítő szerkezetekről.", exs_2))

lesson_2 = make_lesson(
    "lesson.b1.reformkor.02",
    "Gróf Széchenyi István, a 'legnagyobb magyar' és reformprogramja (Hitel 1830)",
    "Korszerűsítést és akadályoztatást kifejező szerkezetek (gátol, korszerűsít)",
    "Megtanuljuk Széchenyi Hitel című könyvének eszméit, a Lánchíd építését, a folyók szabályozását és a modernizáció alapjait.",
    ["Megérteni a Hitel (1830) gazdasági jelentőségét és a feudalizmus kritikáját", "Használni a korszerűsítéssel és akadályokkal kapcsolatos kifejezéseket", "Ismerni Széchenyi gyakorlati alkotásait (Lánchíd, gőzhajózás, Vaskapu)"],
    "story.b1.reformkor.02",
    "voc.b1.reformkor.02",
    "gr.b1.reformkor.02",
    "ex.b1.reformkor.02",
    [e["id"] for e in exs_2]
)
write_json(LESSONS_DIR / "lesson.b1.reformkor.02.json", lesson_2)


# ==========================================
# LESSON 3: b1-reformkor-03 (Kossuth Lajos és az érdekegyesítés)
# ==========================================
story_3 = make_story(
    "story.b1.reformkor.03",
    "Kossuth Lajos, az érdekegyesítés és a független sajtó",
    "Kossuth Lajos az Országgyűlési Tudósításokkal, a Pesti Hírlappal és a nemesek meg a jobbágyok érdekegyesítésének programjával a reformmozgalom vezéralakjává vált.",
    "Pozsony és Pest",
    ["Socio-political mobilization terms (érdekegyesítés, jobbágyfelszabadítás, sajtószabadság)", "Public opinion and press"],
    ["Kossuth Lajos", "érdekegyesítés", "Pesti Hírlap", "jobbágyfelszabadítás", "örökváltság"],
    [
        "Az 1830-as években új, lendületes politikus lépett a nyilvánosság elé: Kossuth Lajos. Mivel a bécsi cenzúra tiltotta az országgyűlési viták nyomtatását, Kossuth kézzel másolt 'Országgyűlési Tudósításokat' adott ki, eljuttatva a reformeszméket az ország minden vármegyéjébe.",
        "Kossuthot ellenzéki tevékenysége miatt börtönbe zárták, de szabadulása után, 1841-ben átvette a Pesti Hírlap szerkesztését. Vezércikkeiben megfogalmazta a nemzeti felemelkedés kulcsát: az érdekegyesítést. Vallotta, hogy a nemességnek és a jobbágyságnak egyesítenie kell erőit a nemzeti szabadságért.",
        "Programjának központi eleme a kötelező örökváltság (államilag kárpótolt jobbágyfelszabadítás), a közteherviselés (a nemesi adómentesség eltörlése) és a népképviselet volt. Zseniális szónoki tehetségével és újságírói munkásságával Kossuth a nemzet elismert vezérévé vált."
    ],
    [
        {"lemma": "érdekegyesítés", "pos": "noun", "cefr": "B1", "gloss": "harmonization of interests (nobles & serfs)"},
        {"lemma": "örökváltság", "pos": "noun", "cefr": "B1", "gloss": "redemption of serf obligations (emancipation)"},
        {"lemma": "jobbágyfelszabadítás", "pos": "noun", "cefr": "B1", "gloss": "emancipation of the serfs"},
        {"lemma": "vezércikk", "pos": "noun", "cefr": "B1", "gloss": "editorial, lead article"},
        {"lemma": "népképviselet", "pos": "noun", "cefr": "B1", "gloss": "popular representative government"}
    ],
    [
        {
            "question": "Mit jelentett Kossuth Lajos 'érdekegyesítés' programja?",
            "options": ["A nemesség és a jobbágyság érdekeinek összefogását a nemzeti szabadságért és reformokért", "Minden politikai párt betiltását", "Bécs feltétlen támogatását", "Csak a gazdag kereskedők összefogását"],
            "correctIndex": 0,
            "explanation": "Az érdekegyesítés célja a jobbágyok és nemesek közös nemzeti táborba terelése volt a jobbágyfelszabadítás révén."
        }
    ]
)
write_json(STORIES_DIR / "story.b1.reformkor.03.json", story_3)

voc_3 = {
    "id": "voc.b1.reformkor.03",
    "title": "A társadalmi mozgalmak és sajtó szókincse",
    "description": "Érdekegyesítés, örökváltság, jobbágyfelszabadítás, vezércikk és népképviselet.",
    "entries": [
        {"lemma": "érdekegyesítés", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "uniting the interests of nobility and peasantry", "examples": [{"hu": "Kossuth az érdekegyesítés elvét hirdette a Pesti Hírlapban.", "en": "Kossuth preached the principle of uniting interests in Pesti Hírlap."}]}]},
        {"lemma": "örökváltság", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "redemption payment for serf liberation", "examples": [{"hu": "A kötelező örökváltság tette szabaddá a parasztot.", "en": "Compulsory redemption made the peasant free."}]}]},
        {"lemma": "jobbágyfelszabadítás", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "emancipation of the serfs with land", "examples": [{"hu": "A jobbágyfelszabadítás a polgári társadalom alapja.", "en": "The emancipation of serfs is the foundation of civil society."}]}]},
        {"lemma": "vezércikk", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "lead editorial article in a newspaper", "examples": [{"hu": "Kossuth vezércikkei mozgósították a közvéleményt.", "en": "Kossuth's editorials mobilized public opinion."}]}]},
        {"lemma": "népképviselet", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "popular representation in parliament", "examples": [{"hu": "A rendi országgyűlést népképviseleti parlamentté kell alakítani.", "en": "The feudal diet must be transformed into a representative parliament."}]}]}
    ]
}
write_json(VOCAB_DIR / "voc.b1.reformkor.03.json", voc_3)

gr_3 = {
    "id": "gr.b1.reformkor.03",
    "title": "Társadalmi szükségességet és követelést kifejező szerkezetek (szükséges, elengedhetetlen, meg kell valósítani)",
    "description": "Expressing political imperatives, societal urgency, and reform demands.",
    "rules": [
        "A politikai programok megfogalmazásában az 'elengedhetetlen', 'szükséges', 'meg kell valósítani' kifejezések a reformok halaszthatatlanságát hangsúlyozzák.",
        "A célhatározói igék tárgyas vonzatait alkalmazzuk: 'jobbágyfelszabadítást követel'."
    ],
    "tables": [
        {"headers": ["Kifejezés", "Jelentés", "Példa"], "rows": [
            ["elengedhetetlen", "indispensable / essential", "Elengedhetetlen a jobbágyok felszabadítása."],
            ["meg kell valósítani", "must be implemented", "Meg kell valósítani a közteherviselést."],
            ["követel", "to demand", "Sajtószabadságot követeltek."]
        ]}
    ],
    "examples": [
        {"spanish": "Elengedhetetlen volt a nemesi adómentesség eltörlése az államháztartás megerősítéséhez.", "english": "Abolishing noble tax exemption was essential to strengthen state finances."},
        {"spanish": "Kossuth szerint a szabadságot csak a nemzet és a jobbágyság összefogásával lehetett kivívni.", "english": "According to Kossuth, liberty could only be won through the unity of the nation and the serfs."},
        {"spanish": "A Pesti Hírlap vezércikkei megteremtették a modern magyar politikai sajtót.", "english": "The editorials of Pesti Hírlap created the modern Hungarian political press."}
    ]
}
write_json(GRAMMAR_DIR / "gr.b1.reformkor.03.json", gr_3)

exs_3 = [
    {"id": "ex.b1.reformkor.03.01", "type": "multiple-choice", "lesson": "lesson.b1.reformkor.03", "teaches": ["Kossuth-Lajos"], "prompt": "Melyik híres újságot szerkesztette Kossuth Lajos 1841-től?", "options": ["A Pesti Hírlapot", "A Magyar Kurírt", "A Budapesti Hírlapot", "A Nemzeti Újságot"], "correctIndex": 0, "explanation": "Kossuth 1841-től a Pesti Hírlap főszerkesztőjeként írta híres vezércikkeit."},
    {"id": "ex.b1.reformkor.03.02", "type": "fill-blank", "lesson": "lesson.b1.reformkor.03", "teaches": ["erdekegyesites"], "prompt": "Egészítsd ki a mondatot!", "sentence": "Kossuth legfontosabb politikai eszméje a nemesek és jobbágyok *érdekegyesítése* volt.", "target": "érdekegyesítése"},
    {"id": "ex.b1.reformkor.03.03", "type": "sentence-builder", "lesson": "lesson.b1.reformkor.03", "teaches": ["elengedhetetlen", "jobbagyfelszabaditas"], "prompt": "Rakd össze a szükségességet kifejező mondatot!", "chips": ["Elengedhetetlen", "volt", "a", "jobbágyok", "teljes", "felszabadítása."], "target": "Elengedhetetlen volt a jobbágyok teljes felszabadítása.", "english": "The complete emancipation of serfs was indispensable."},
    {"id": "ex.b1.reformkor.03.04", "type": "multiple-choice", "lesson": "lesson.b1.reformkor.03", "teaches": ["orokvaltsag"], "prompt": "Mit jelent a 'kötelező örökváltság'?", "options": ["A jobbágyok felszabadítását a földjükkel együtt, állami kárpótlással a földesuraknak", "A parasztok eladását", "A nemesi címek öröklését", "Új adók bevezetését"], "correctIndex": 0, "explanation": "A kötelező örökváltság állami kárpótlással törölte el a jobbágyi függést."},
    {"id": "ex.b1.reformkor.03.05", "type": "fill-blank", "lesson": "lesson.b1.reformkor.03", "teaches": ["vepercikk"], "prompt": "Egészítsd ki a mondatot!", "sentence": "Kossuth bátor *vezércikkei* mozgósították az egész országot.", "target": "vezércikkei"},
    {"id": "ex.b1.reformkor.03.06", "type": "sentence-builder", "lesson": "lesson.b1.reformkor.03", "teaches": ["nepkepviselet", "parlament"], "prompt": "Alkoss szabályos politikai mondatot!", "chips": ["A", "cél", "a", "népképviseleti", "országgyűlés", "megteremtése", "volt."], "target": "A cél a népképviseleti országgyűlés megteremtése volt.", "english": "The goal was the creation of a representative parliament."},
    {"id": "ex.b1.reformkor.03.07", "type": "multiple-choice", "lesson": "lesson.b1.reformkor.03", "teaches": ["Orszaggyulesi-Tudisitasok"], "prompt": "Hogyan terjesztette Kossuth az Országgyűlési Tudósításokat a cenzúra idején?", "options": ["Kézzel másolt magánlevelek formájában küldte szét a vármegyékbe", "Rádióban közvetítette", "Bécsi nyomdában nyomtatta", "Külföldről csempészte be"], "correctIndex": 0, "explanation": "Kézzel írott levelekben másolták és küldték szét a cenzúra kikerülésére."},
    {"id": "ex.b1.reformkor.03.08", "type": "fill-blank", "lesson": "lesson.b1.reformkor.03", "teaches": ["jobbagyfelszabaditas"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A polgári fejlődés alapköve a *jobbágyfelszabadítás* megvalósítása volt.", "target": "jobbágyfelszabadítás"}
]
write_json(EXERCISES_DIR / "ex.b1.reformkor.03.json", make_exercise_group("ex.b1.reformkor.03", "Kossuth és az érdekegyesítés gyakorlatai", "Gyakorlatok a Pesti Hírlapról, az örökváltságról és a szükségességet kifejező szerkezetekről.", exs_3))

lesson_3 = make_lesson(
    "lesson.b1.reformkor.03",
    "Kossuth Lajos, az érdekegyesítés és a független sajtó",
    "Társadalmi szükségességet kifejező szerkezetek (elengedhetetlen, meg kell valósítani)",
    "Megismerjük Kossuth Lajos újságírói tevékenységét, az érdekegyesítés és a kötelező örökváltság elvét.",
    ["Megérteni Kossuth érdekegyesítési programját és reformköveteléseit", "Használni a politikai szükségességet és követeléseket kifejező formákat", "Ismerni a Pesti Hírlap és az Országgyűlési Tudósítások szerepét"],
    "story.b1.reformkor.03",
    "voc.b1.reformkor.03",
    "gr.b1.reformkor.03",
    "ex.b1.reformkor.03",
    [e["id"] for e in exs_3]
)
write_json(LESSONS_DIR / "lesson.b1.reformkor.03.json", lesson_3)


# ==========================================
# LESSON 4: b1-reformkor-04 (Széchenyi és Kossuth vitája)
# ==========================================
story_4 = make_story(
    "story.b1.reformkor.04",
    "Széchenyi és Kossuth vitája: két út a polgári átalakuláshoz",
    "Széchenyi a lassú, megfontolt, az udvarral megegyező arisztokratikus reformokban hitt, míg Kossuth a gyors, radikális és a széles néptömegekre támaszkodó átalakulást sürgette.",
    "Pest és Pozsony",
    ["Argumentative comparison and debate structures (szemben áll egymással, míg az egyik... a másik, abból indul ki)", "Ideological debates"],
    ["Széchenyi és Kossuth vitája", "Kelet Népe", "Felelet", "evolúció vs forradalom", "reformtábor"],
    [
        "Az 1840-es évekre a magyar reformtábor két nagy irányzatra oszlott, amelyeket a korszak két óriása, Széchenyi István és Kossuth Lajos vezetett. Bár mindketten a polgári, modern és függetlenebb Magyarország megteremtését akarták, a célhoz vezető útban és tempóban élesen szemben álltak egymással.",
        "Széchenyi 1841-ben megírta 'A Kelet Népe' című vitairatát, amelyben azzal vádolta Kossuthot, hogy szenvedélyes, radikális hangvételével forradalomba sodorja a nemzetet és magára haragítja a Habsburg-udvart. Széchenyi abból indult ki, hogy a gazdasági alapokat kell először kiépíteni az arisztokrácia vezetésével, békés megegyezésre törekedve Béccsel.",
        "Kossuth 'Felelet gróf Széchenyi Istvánnak' című válaszában leszögezte: a nép nem várhat évtizedeket, és a politikai jogok kiterjesztése nélkül nem lehet gazdasági sikert elérni. Míg Széchenyi a megfontolt evolúció híve volt, addig Kossuth a társadalmi tömegeket mozgósító gyors átalakulásban hitt, és a közvélemény döntő többsége végül Kossuth oldalára állt."
    ],
    [
        {"lemma": "vitairat", "pos": "noun", "cefr": "B1", "gloss": "polemical treatise, controversial tract"},
        {"lemma": "hangvétel", "pos": "noun", "cefr": "B1", "gloss": "tone, rhetorical style"},
        {"lemma": "átalakulás", "pos": "noun", "cefr": "B1", "gloss": "transformation, transition"},
        {"lemma": "megfontolt", "pos": "adjective", "cefr": "B1", "gloss": "deliberate, cautious, prudent"},
        {"lemma": "mozgósít", "pos": "verb", "cefr": "B1", "gloss": "to mobilize (society/public)"}
    ],
    [
        {
            "question": "Mi volt a fő különbség Széchenyi és Kossuth politikai programja között?",
            "options": ["Széchenyi a lassú, arisztokrata vezetésű gazdasági reformokban, Kossuth a gyors, népre támaszkodó politikai átalakulásban hitt", "Széchenyi a törökökkel, Kossuth az oroszokkal akart szövetkezni", "Széchenyi elutasította a Lánchidat", "Nem volt semmilyen különbség közöttük"],
            "correctIndex": 0,
            "explanation": "Széchenyi óvatos, Béccsel kiegyező gazdasági evolúciót, Kossuth gyors, radikális politikai változást akart."
        }
    ]
)
write_json(STORIES_DIR / "story.b1.reformkor.04.json", story_4)

voc_4 = {
    "id": "voc.b1.reformkor.04",
    "title": "A politikai viták és eszmeáramlatok szókincse",
    "description": "Vitairat, hangvétel, átalakulás, megfontoltság és társadalmi mozgósítás.",
    "entries": [
        {"lemma": "vitairat", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "polemical tract in a public debate", "examples": [{"hu": "A Kelet Népe Széchenyi híres vitairata volt.", "en": "People of the Orient was Széchenyi's famous polemical tract."}]}]},
        {"lemma": "hangvétel", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "tone, stylistic voice", "examples": [{"hu": "Kossuth újságírói hangvétele magával ragadta a fiatalokat.", "en": "Kossuth's journalistic tone swept away the youth."}]}]},
        {"lemma": "átalakulás", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "social and economic transformation", "examples": [{"hu": "A polgári átalakulás volt a reformkor legfőbb célja.", "en": "Civic transformation was the main goal of the Reform Era."}]}]},
        {"lemma": "megfontolt", "pos": "adjective", "cefr": "B1", "definitions": [{"meaning": "deliberate, cautious and prudent", "examples": [{"hu": "Széchenyi a megfontolt, lépésről lépésre haladó reformokat kedvelte.", "en": "Széchenyi favored deliberate, step-by-step reforms."}]}]},
        {"lemma": "mozgósít", "pos": "verb", "cefr": "B1", "definitions": [{"meaning": "to mobilize public opinion", "examples": [{"hu": "A Pesti Hírlap sikeresen mozgósította a nemességet.", "en": "Pesti Hírlap successfully mobilized the nobility."}]}]}
    ]
}
write_json(VOCAB_DIR / "voc.b1.reformkor.04.json", voc_4)

gr_4 = {
    "id": "gr.b1.reformkor.04",
    "title": "Összehasonlító és vitaérvelési szerkezetek (szemben áll egymással, míg az egyik... a másik, abból indul ki)",
    "description": "Comparing ideological positions and contrasting political strategies in B1 essays.",
    "rules": [
        "A két álláspont ütköztetését a 'szemben áll egymással', 'míg az egyik... a másik ezzel szemben...' párhuzamos kifejezések jelenítik meg.",
        "A politikai kiindulópontokat az 'abból indul ki, hogy...' és 'arra épít, hogy...' szerkezetekkel mutatjuk be."
    ],
    "tables": [
        {"headers": ["Kifejezés", "Funkció", "Példa"], "rows": [
            ["szemben állnak egymással", "ellentét megfogalmazása", "A két vezér álláspontja szemben állt egymással."],
            ["míg... a másik ezzel szemben", "párhuzamos összevetés", "Míg Széchenyi óvatos volt, Kossuth sietett."],
            ["abból indul ki, hogy...", "érvelési alap", "Abból indult ki, hogy a gazdaság a legfontosabb."]
        ]}
    ],
    "examples": [
        {"spanish": "Míg Széchenyi a lassú gazdasági fejlődést támogatta, Kossuth a gyors politikai reformokat sürgette.", "english": "While Széchenyi supported slow economic development, Kossuth urged swift political reforms."},
        {"spanish": "A két reformer abból indult ki, hogy Magyarországnak modernizálódnia kell.", "english": "Both reformers started from the premise that Hungary must modernize."},
        {"spanish": "A nemzet Széchenyiben a programalkotót, Kossuthban a forradalmi vezetőt látta.", "english": "The nation saw in Széchenyi the program creator, and in Kossuth the revolutionary leader."}
    ]
}
write_json(GRAMMAR_DIR / "gr.b1.reformkor.04.json", gr_4)

exs_4 = [
    {"id": "ex.b1.reformkor.04.01", "type": "multiple-choice", "lesson": "lesson.b1.reformkor.04", "teaches": ["Szechenyi-Kossuth-vita"], "prompt": "Melyik vitairatot írta Széchenyi István Kossuth radikalizmusa ellen 1841-ben?", "options": ["A Kelet Népét", "A Hitelt", "A Stádiumot", "A Világot"], "correctIndex": 0, "explanation": "'A Kelet Népe' volt Széchenyi híres vitairata Kossuth politikája ellen."},
    {"id": "ex.b1.reformkor.04.02", "type": "fill-blank", "lesson": "lesson.b1.reformkor.04", "teaches": ["vitairat"], "prompt": "Egészítsd ki a mondatot!", "sentence": "Kossuth azonnal válaszolt Széchenyi *vitairatára* a 'Felelet' című művében.", "target": "vitairatára"},
    {"id": "ex.b1.reformkor.04.03", "type": "sentence-builder", "lesson": "lesson.b1.reformkor.04", "teaches": ["mig", "szemben"], "prompt": "Rakd össze az összehasonlító mondatot!", "chips": ["Míg", "Széchenyi", "óvatos", "volt,", "Kossuth", "gyors", "reformokat", "akart."], "target": "Míg Széchenyi óvatos volt, Kossuth gyors reformokat akart.", "english": "While Széchenyi was cautious, Kossuth wanted fast reforms."},
    {"id": "ex.b1.reformkor.04.04", "type": "multiple-choice", "lesson": "lesson.b1.reformkor.04", "teaches": ["reform-tempo"], "prompt": "Miben különbözött Széchenyi és Kossuth reformtempója?", "options": ["Széchenyi a fokozatos, megfontolt lépésekben, Kossuth a gyors, társadalmi mozgósításban bízott", "Széchenyi nem akart semmilyen reformot", "Kossuth vissza akarta hozni a középkort", "Egyikük sem foglalkozott a gazdasággal"], "correctIndex": 0, "explanation": "Széchenyi a fokozatosság, Kossuth a gyors cselekvés híve volt."},
    {"id": "ex.b1.reformkor.04.05", "type": "fill-blank", "lesson": "lesson.b1.reformkor.04", "teaches": ["megfontolt"], "prompt": "Egészítsd ki a mondatot a megfelelő melléknévvel!", "sentence": "Széchenyi a *megfontolt*, békés átalakulás híve volt.", "target": "megfontolt"},
    {"id": "ex.b1.reformkor.04.06", "type": "sentence-builder", "lesson": "lesson.b1.reformkor.04", "teaches": ["abbol-indul-ki", "atalakulas"], "prompt": "Alkoss szabályos érvelő mondatot!", "chips": ["Kossuth", "abból", "indult", "ki,", "hogy", "szükséges", "a", "változás."], "target": "Kossuth abból indult ki, hogy szükséges a változás.", "english": "Kossuth started from the premise that change was necessary."},
    {"id": "ex.b1.reformkor.04.07", "type": "multiple-choice", "lesson": "lesson.b1.reformkor.04", "teaches": ["kozvelemeny-dontese"], "prompt": "Kinek az oldalára állt a magyar ifjúság és a közvélemény többsége az 1840-es években?", "options": ["Kossuth Lajos oldalára", "Széchenyi István mellé", "A bécsi kancellária mellé", "A konzervatív főurak mellé"], "correctIndex": 0, "explanation": "A reformkor végén a fiatalság és a nemesség többsége Kossuth programját választotta."},
    {"id": "ex.b1.reformkor.04.08", "type": "fill-blank", "lesson": "lesson.b1.reformkor.04", "teaches": ["mozgosit"], "prompt": "Egészítsd ki a mondatot a megfelelő igealakkal!", "sentence": "Kossuth sikeresen *mozgósította* a haladó nemességet és a polgárságot.", "target": "mozgósította"}
]
write_json(EXERCISES_DIR / "ex.b1.reformkor.04.json", make_exercise_group("ex.b1.reformkor.04", "Széchenyi és Kossuth vitája gyakorlatok", "Gyakorlatok a két reformirányzatról, a vitairatokról és az összehasonlító kifejezésekről.", exs_4))

lesson_4 = make_lesson(
    "lesson.b1.reformkor.04",
    "Széchenyi és Kossuth vitája: két út a polgári átalakuláshoz",
    "Összehasonlító és vitaérvelési szerkezetek (míg... a másik, abból indul ki)",
    "Részletesen elemezzük Széchenyi és Kossuth nézetkülönbségeit: a Kelet Népe vitát, az evolúció és radikális reformok szembenállását.",
    ["Megérteni Széchenyi és Kossuth vitájának fő kérdéseit", "Használni a vitaérvelési és összehasonlító mondatszerkezeteket", "Felismerni a két reformer közös célját és eltérő módszereit"],
    "story.b1.reformkor.04",
    "voc.b1.reformkor.04",
    "gr.b1.reformkor.04",
    "ex.b1.reformkor.04",
    [e["id"] for e in exs_4]
)
write_json(LESSONS_DIR / "lesson.b1.reformkor.04.json", lesson_4)


# ==========================================
# LESSON 5: b1-reformkor-05 (1844-es államnyelvi törvény és kultúra)
# ==========================================
story_5 = make_story(
    "story.b1.reformkor.05",
    "A magyar nyelv diadala: az 1844-es államnyelvi törvény és a nemzeti kultúra",
    "1844-ben a magyar nyelv lett Magyarország hivatalos államnyelve, miközben Kölcsey Himnusza, Vörösmarty Szózata és Erkel nemzeti operái megalapozták az újkori nemzeti identitást.",
    "Pozsony, Nemzeti Színház és Pest",
    ["Legal elevation and declarative status (államnyelvvé válik, elrendeltetik, felváltja a)", "National anthems and cultural milestones"],
    ["államnyelv", "1844. évi II. törvénycikk", "Himnusz", "Szózat", "Kölcsey Ferenc", "Vörösmarty Mihály"],
    [
        "A reformkor küzdelmeinek egyik legfényesebb győzelme a nemzeti nyelv hivatalossá tétele volt. Az 1844-es pozsonyi országgyűlésen elfogadott 1844. évi II. törvénycikk értelmében a magyar nyelv végleg felváltotta a latint a közigazgatásban, a bíróságokon és a felsőoktatásban, hivatalos államnyelvvé emelkedve Magyarországon.",
        "A nyelvi sikerrel párhuzamosan virágkorát élte a nemzeti romantikus kultúra. 1823-ban Kölcsey Ferenc megírta a 'Himnuszt' (megzenésítette Erkel Ferenc 1844-ben), amely a nemzet imádságává vált, míg Vörösmarty Mihály 1836-ban megalkotta a 'Szózatot' ('Hazádnak rendületlenül légy híve, ó magyar!'), Egressy Béni dallamával.",
        "1837-ben megnyitotta kapuit a Pesti Magyar Színház (későbbi Nemzeti Színház), megindult a Nemzeti Múzeum építése Pollack Mihály tervei alapján, és a reformkori irodalom megalapozta a modern magyar polgári öntudatot. A nemzet felkészült az 1848-as nagy történelmi fordulatra."
    ],
    [
        {"lemma": "államnyelv", "pos": "noun", "cefr": "B1", "gloss": "official state language"},
        {"lemma": "törvénycikk", "pos": "noun", "cefr": "B1", "gloss": "article of law, legislative act"},
        {"lemma": "nemzeti imádság", "pos": "noun", "cefr": "B1", "gloss": "national prayer (the Anthem)"},
        {"lemma": "rendületlenül", "pos": "adverb", "cefr": "B1", "gloss": "unwaveringly, steadfastly"},
        {"lemma": "öntudat", "pos": "noun", "cefr": "B1", "gloss": "national consciousness / self-awareness"}
    ],
    [
        {
            "question": "Melyik évben vált a magyar nyelv hivatalos államnyelvvé a latin helyett?",
            "options": ["1844-ben (az 1844. évi II. törvénycikkel)", "1825-ben", "1848-ban", "1867-ben"],
            "correctIndex": 0,
            "explanation": "Az 1844. évi II. törvénycikk tette a magyar nyelvet hivatalos államnyelvvé."
        }
    ]
)
write_json(STORIES_DIR / "story.b1.reformkor.05.json", story_5)

voc_5 = {
    "id": "voc.b1.reformkor.05",
    "title": "Az államnyelv és a nemzeti szimbólumok szókincse",
    "description": "Államnyelv, törvénycikk, Himnusz, Szózat, rendületlenség és nemzeti öntudat.",
    "entries": [
        {"lemma": "államnyelv", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "official state language of administration and courts", "examples": [{"hu": "1844-ben a magyar lett a hivatalos államnyelv.", "en": "In 1844, Hungarian became the official state language."}]}]},
        {"lemma": "törvénycikk", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "article of law passed by parliament", "examples": [{"hu": "Az 1844. évi II. törvénycikk történelmi jelentőségű volt.", "en": "The 1844 Act II was of historical significance."}]}]},
        {"lemma": "nemzeti imádság", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "national prayer, anthem of the country", "examples": [{"hu": "A Himnusz a magyar nemzet legszentebb imádsága.", "en": "The Anthem is the most sacred prayer of the Hungarian nation."}]}]},
        {"lemma": "rendületlenül", "pos": "adverb", "cefr": "B1", "definitions": [{"meaning": "steadfastly, unwaveringly", "examples": [{"hu": "'Hazádnak rendületlenül légy híve, ó magyar!'", "en": "'To your homeland be unwaveringly faithful, o Hungarian!'"}]}]},
        {"lemma": "öntudat", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "national identity consciousness", "examples": [{"hu": "A reformkori költészet megerősítette a nemzeti öntudatot.", "en": "Reform-era poetry strengthened national consciousness."}]}]}
    ]
}
write_json(VOCAB_DIR / "voc.b1.reformkor.05.json", voc_5)

gr_5 = {
    "id": "gr.b1.reformkor.05",
    "title": "Hivatalossá válást és felváltást kifejező szerkezetek (államnyelvvé válik, felváltja a, elrendeltetik)",
    "description": "Describing the official enactment of languages, symbols, and national anthems.",
    "rules": [
        "A hivatalossá válást az '-vá/-vé válik', 'államnyelvvé emelkedik' igék jelölik.",
        "A korábbi állapot felváltását a 'felváltja a...', 'helyébe lép' szerkezetekkel fogalmazzuk meg."
    ],
    "tables": [
        {"headers": ["Kifejezés", "Jelentés", "Példa"], "rows": [
            ["államnyelvvé válik", "to become state language", "A magyar nyelv államnyelvvé vált."],
            ["felváltja a...", "to replace/supersede", "A magyar felváltotta a latint."],
            ["elrendeltetik", "official enactment", "Elrendeltetett a magyar nyelv használata."]
        ]}
    ],
    "examples": [
        {"spanish": "1844-ben a magyar nyelv felváltotta a latint a törvényhozásban és az oktatásban.", "english": "In 1844, Hungarian replaced Latin in legislation and education."},
        {"spanish": "Kölcsey Ferenc Himnusza és Vörösmarty Szózata a nemzeti identitás alapjai lettek.", "english": "Ferenc Kölcsey's Anthem and Mihály Vörösmarty's Appeal became the foundations of national identity."},
        {"spanish": "A Nemzeti Színház megnyitása elősegítette az anyanyelvi kultúra fejlődését.", "english": "The opening of the National Theatre fostered the development of native language culture."}
    ]
}
write_json(GRAMMAR_DIR / "gr.b1.reformkor.05.json", gr_5)

exs_5 = [
    {"id": "ex.b1.reformkor.05.01", "type": "multiple-choice", "lesson": "lesson.b1.reformkor.05", "teaches": ["allamnyelv-1844"], "prompt": "Melyik törvénycikk tette a magyar nyelvet hivatalos államnyelvvé 1844-ben?", "options": ["Az 1844. évi II. törvénycikk", "Az 1825. évi I. törvénycikk", "Az 1848. évi III. törvénycikk", "Az 1723. évi Pragmatica Sanctio"], "correctIndex": 0, "explanation": "Az 1844. évi II. törvénycikk mondta ki a magyar államnyelvet."},
    {"id": "ex.b1.reformkor.05.02", "type": "fill-blank", "lesson": "lesson.b1.reformkor.05", "teaches": ["allamnyelv"], "prompt": "Egészítsd ki a mondatot!", "sentence": "1844-ben a magyar nyelv a közigazgatás hivatalos *államnyelvévé* vált.", "target": "államnyelvévé"},
    {"id": "ex.b1.reformkor.05.03", "type": "sentence-builder", "lesson": "lesson.b1.reformkor.05", "teaches": ["felvaltja", "latin"], "prompt": "Rakd össze a mondatot helyes sorrendben!", "chips": ["A", "magyar", "nyelv", "végleg", "felváltotta", "a", "latint."], "target": "A magyar nyelv végleg felváltotta a latint.", "english": "The Hungarian language finally replaced Latin."},
    {"id": "ex.b1.reformkor.05.04", "type": "multiple-choice", "lesson": "lesson.b1.reformkor.05", "teaches": ["Himnusz-Kolcsey"], "prompt": "Ki írta és mikor a magyar Himnusz szövegét?", "options": ["Kölcsey Ferenc 1823-ban", "Vörösmarty Mihály 1836-ban", "Petőfi Sándor 1848-ban", "Arany János 1850-ben"], "correctIndex": 0, "explanation": "Kölcsey Ferenc 1823. január 22-én fejezte be a Himnuszt (a Magyar Kultúra Napja)."},
    {"id": "ex.b1.reformkor.05.05", "type": "fill-blank", "lesson": "lesson.b1.reformkor.05", "teaches": ["Szozat-Vorosmarty"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A Szózat híres sora: 'Hazádnak *rendületlenül* légy híve, ó magyar!'.", "target": "rendületlenül"},
    {"id": "ex.b1.reformkor.05.06", "type": "sentence-builder", "lesson": "lesson.b1.reformkor.05", "teaches": ["Erkel-Ferenc", "Himnusz"], "prompt": "Alkoss szabályos mondatot!", "chips": ["A", "Himnusz", "zenéjét", "Erkel", "Ferenc", "szerezte", "1844-ben."], "target": "A Himnusz zenéjét Erkel Ferenc szerezte 1844-ben.", "english": "The music of the Anthem was composed by Ferenc Erkel in 1844."},
    {"id": "ex.b1.reformkor.05.07", "type": "multiple-choice", "lesson": "lesson.b1.reformkor.05", "teaches": ["Nemzeti-Szinhaz-1837"], "prompt": "Mikor nyílt meg a Pesti Magyar Színház (a Nemzeti Színház elődje)?", "options": ["1837-ben", "1825-ben", "1848-ban", "1867-ben"], "correctIndex": 0, "explanation": "A Pesti Magyar Színház 1837-ben nyitotta meg kapuit."},
    {"id": "ex.b1.reformkor.05.08", "type": "fill-blank", "lesson": "lesson.b1.reformkor.05", "teaches": ["ontudat"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A nemzeti kultúra megerősítette a polgári *öntudatot*.", "target": "öntudatot"}
]
write_json(EXERCISES_DIR / "ex.b1.reformkor.05.json", make_exercise_group("ex.b1.reformkor.05", "Az államnyelv és a nemzeti kultúra gyakorlatai", "Gyakorlatok az 1844-es törvényről, a Himnuszról, a Szózatról és az államnyelvi kifejezésekről.", exs_5))

lesson_5 = make_lesson(
    "lesson.b1.reformkor.05",
    "A magyar nyelv diadala: az 1844-es államnyelvi törvény és a nemzeti kultúra",
    "Hivatalossá válást és felváltást kifejező szerkezetek (államnyelvvé válik, felváltja)",
    "Összegezzük a magyar államnyelv diadalát (1844), a Himnusz és Szózat születését, valamint a reformkori nemzeti intézmények felemelkedését.",
    ["Megérteni az 1844. évi II. törvénycikk jelentőségét a magyar nyelv történetében", "Használni a hivatalossá válást és felváltást kifejező nyelvi formákat", "Ismerni Kölcsey Himnuszát, Vörösmarty Szózatát és Erkel Ferenc zenéjét"],
    "story.b1.reformkor.05",
    "voc.b1.reformkor.05",
    "gr.b1.reformkor.05",
    "ex.b1.reformkor.05",
    [e["id"] for e in exs_5]
)
write_json(LESSONS_DIR / "lesson.b1.reformkor.05.json", lesson_5)


# ==========================================
# CONSOLIDATION LESSON: b1-reformkor-consolidation
# ==========================================
cons_exs = [
    {"id": "ex.b1.reformkor.cons.01", "type": "multiple-choice", "lesson": "lesson.b1.reformkor.consolidation", "teaches": ["reformkor-evek"], "prompt": "Melyik évszámok határolják a magyar reformkort?", "options": ["1825–1848", "1703–1711", "1848–1849", "1867–1914"], "correctIndex": 0, "explanation": "A reformkor 1825-től (Akadémia) 1848-ig (forradalom) tartott."},
    {"id": "ex.b1.reformkor.cons.02", "type": "fill-blank", "lesson": "lesson.b1.reformkor.consolidation", "teaches": ["birtokjovedelem"], "prompt": "1825-ben Széchenyi István egyévi *birtokjövedelmét* ajánlotta fel a Magyar Tudományos Akadémiára.", "sentence": "1825-ben Széchenyi István egyévi *birtokjövedelmét* ajánlotta fel a Magyar Tudományos Akadémiára.", "target": "birtokjövedelmét"},
    {"id": "ex.b1.reformkor.cons.03", "type": "multiple-choice", "lesson": "lesson.b1.reformkor.consolidation", "teaches": ["Hitel-1830"], "prompt": "Melyik alapvető művet írta Széchenyi 1830-ban a gazdasági reformokról?", "options": ["Hitel", "Világ", "Stádium", "Kelet Népe"], "correctIndex": 0, "explanation": "A 'Hitel' volt Széchenyi legfontosabb gazdasági alapműve."},
    {"id": "ex.b1.reformkor.cons.04", "type": "fill-blank", "lesson": "lesson.b1.reformkor.consolidation", "teaches": ["Lanchid"], "prompt": "Széchenyi kezdeményezésére épült fel Pest és Buda első állandó kőhídja, a *Lánchíd*.", "sentence": "Széchenyi kezdeményezésére épült fel Pest és Buda első állandó kőhídja, a *Lánchíd*.", "target": "Lánchíd"},
    {"id": "ex.b1.reformkor.cons.05", "type": "sentence-builder", "lesson": "lesson.b1.reformkor.consolidation", "teaches": ["gatol", "fejlodes"], "prompt": "Rakd össze a mondatot!", "chips": ["A", "feudális", "rendszer", "gátolta", "a", "társadalmi", "haladást."], "target": "A feudális rendszer gátolta a társadalmi haladást.", "english": "The feudal system hindered social progress."},
    {"id": "ex.b1.reformkor.cons.06", "type": "multiple-choice", "lesson": "lesson.b1.reformkor.consolidation", "teaches": ["Kossuth-Pesti-Hirlap"], "prompt": "Melyik újságban fejtette ki Kossuth Lajos az érdekegyesítés programját 1841-től?", "options": ["A Pesti Hírlapban", "A Budapesti Közlönyben", "A Honderűben", "Az Akadémiai Értesítőben"], "correctIndex": 0, "explanation": "A Pesti Hírlapban jelentek meg Kossuth híres vezércikkei."},
    {"id": "ex.b1.reformkor.cons.07", "type": "fill-blank", "lesson": "lesson.b1.reformkor.consolidation", "teaches": ["erdekegyesites"], "prompt": "A nemesség és a parasztság összefogását Kossuth *érdekegyesítésnek* nevezte.", "sentence": "A nemesség és a parasztság összefogását Kossuth *érdekegyesítésnek* nevezte.", "target": "érdekegyesítésnek"},
    {"id": "ex.b1.reformkor.cons.08", "type": "sentence-builder", "lesson": "lesson.b1.reformkor.consolidation", "teaches": ["elengedhetetlen", "jobbagyfelszabaditas"], "prompt": "Alkoss szabályos mondatot!", "chips": ["Elengedhetetlen", "volt", "a", "kötelező", "örökváltság", "bevezetése."], "target": "Elengedhetetlen volt a kötelező örökváltság bevezetése.", "english": "The introduction of compulsory redemption was indispensable."},
    {"id": "ex.b1.reformkor.cons.09", "type": "multiple-choice", "lesson": "lesson.b1.reformkor.consolidation", "teaches": ["Szechenyi-Kossuth-vita"], "prompt": "Miben tért el Széchenyi és Kossuth reformútja?", "options": ["Széchenyi óvatos, Béccsel kiegyező, Kossuth gyors és radikális átalakulást akart", "Széchenyi a forradalmat, Kossuth a békét támogatta", "Széchenyi megszüntette a magyar nyelvet", "Nem volt vitájuk egymással"], "correctIndex": 0, "explanation": "Széchenyi megfontolt arisztokratikus evolúciót, Kossuth gyors társadalmi politizálást akart."},
    {"id": "ex.b1.reformkor.cons.10", "type": "fill-blank", "lesson": "lesson.b1.reformkor.consolidation", "teaches": ["vitairat"], "prompt": "Széchenyi 'A Kelet Népe' című *vitairatában* bírálta Kossuth radikalizmusát.", "sentence": "Széchenyi 'A Kelet Népe' című *vitairatában* bírálta Kossuth radikalizmusát.", "target": "vitairatában"},
    {"id": "ex.b1.reformkor.cons.11", "type": "sentence-builder", "lesson": "lesson.b1.reformkor.consolidation", "teaches": ["mig", "szemben"], "prompt": "Rakd össze az összehasonlító mondatot!", "chips": ["Míg", "Széchenyi", "az", "arisztokráciára,", "Kossuth", "a", "népre", "támaszkodott."], "target": "Míg Széchenyi az arisztokráciára, Kossuth a népre támaszkodott.", "english": "While Széchenyi relied on the aristocracy, Kossuth relied on the people."},
    {"id": "ex.b1.reformkor.cons.12", "type": "multiple-choice", "lesson": "lesson.b1.reformkor.consolidation", "teaches": ["allamnyelv-1844"], "prompt": "Melyik évben lett hivatalos államnyelv a magyar Magyarországon?", "options": ["1844-ben", "1825-ben", "1848-ban", "1830-ban"], "correctIndex": 0, "explanation": "1844-ben (az 1844. évi II. törvénycikkel) lett a magyar az államnyelv a latin helyett."},
    {"id": "ex.b1.reformkor.cons.13", "type": "fill-blank", "lesson": "lesson.b1.reformkor.consolidation", "teaches": ["allamnyelv"], "prompt": "Az 1844-es törvénnyel a magyar nyelv hivatalos *államnyelvvé* vált.", "sentence": "Az 1844-es törvénnyel a magyar nyelv hivatalos *államnyelvvé* vált.", "target": "államnyelvvé"},
    {"id": "ex.b1.reformkor.cons.14", "type": "sentence-builder", "lesson": "lesson.b1.reformkor.consolidation", "teaches": ["felvaltja", "latin"], "prompt": "Rakd össze a mondatot!", "chips": ["A", "magyar", "nyelv", "a", "közigazgatásban", "felváltotta", "a", "latint."], "target": "A magyar nyelv a közigazgatásban felváltotta a latint.", "english": "The Hungarian language replaced Latin in administration."},
    {"id": "ex.b1.reformkor.cons.15", "type": "multiple-choice", "lesson": "lesson.b1.reformkor.consolidation", "teaches": ["Himnusz-1823"], "prompt": "Ki írta a magyar nemzet imádságát, a Himnuszt?", "options": ["Kölcsey Ferenc", "Vörösmarty Mihály", "Petőfi Sándor", "Arany János"], "correctIndex": 0, "explanation": "Kölcsey Ferenc írta a Himnuszt 1823-ban."},
    {"id": "ex.b1.reformkor.cons.16", "type": "fill-blank", "lesson": "lesson.b1.reformkor.consolidation", "teaches": ["Szozat"], "prompt": "Vörösmarty Mihály 1836-ban írta meg a *Szózat* című hazafias költeményt.", "sentence": "Vörösmarty Mihály 1836-ban írta meg a *Szózat* című hazafias költeményt.", "target": "Szózat"},
    {"id": "ex.b1.reformkor.cons.17", "type": "sentence-builder", "lesson": "lesson.b1.reformkor.consolidation", "teaches": ["Erkel-Ferenc", "Himnusz"], "prompt": "Alkoss összefüggő mondatot!", "chips": ["Erkel", "Ferenc", "zenét", "szerzett", "Kölcsey", "Himnuszához."], "target": "Erkel Ferenc zenét szerzett Kölcsey Himnuszához.", "english": "Ferenc Erkel composed music for Kölcsey's Anthem."},
    {"id": "ex.b1.reformkor.cons.18", "type": "multiple-choice", "lesson": "lesson.b1.reformkor.consolidation", "teaches": ["Nemzeti-Szinhaz"], "prompt": "Melyik intézmény nyílt meg 1837-ben Pest-Budán a nemzeti színjátszás fejlesztésére?", "options": ["A Pesti Magyar Színház (Nemzeti Színház)", "Az Operaház", "A Zeneakadémia", "A Vígszínház"], "correctIndex": 0, "explanation": "1837-ben nyitotta meg kapuit a Pesti Magyar Színház."},
    {"id": "ex.b1.reformkor.cons.19", "type": "fill-blank", "lesson": "lesson.b1.reformkor.consolidation", "teaches": ["ontudat"], "prompt": "A reformkor költészete és színháza megteremtette a modern nemzeti *öntudatot*.", "sentence": "A reformkor költészete és színháza megteremtette a modern nemzeti *öntudatot*.", "target": "öntudatot"},
    {"id": "ex.b1.reformkor.cons.20", "type": "multiple-choice", "lesson": "lesson.b1.reformkor.consolidation", "teaches": ["reformkor-eredmeny"], "prompt": "Milyen történelmi eseményhez vezetett közvetlenül a reformkor szellemi és politikai előkészítése?", "options": ["Az 1848. március 15-i forradalomhoz és a polgári átalakuláshoz", "A tatárjáráshoz", "A mohácsi csatához", "A szatmári békéhez"], "correctIndex": 0, "explanation": "A reformkor készítette elő az 1848-as forradalmat és az áprilisi törvényeket."}
]
write_json(EXERCISES_DIR / "ex.b1.reformkor.consolidation.json", make_exercise_group("ex.b1.reformkor.consolidation", "A reformkor összefoglaló gyakorlatok", "Átfogó teszt a reformkor (1825–1848) történetéről, vezetőiről és nyelvtani szerkezeteiről.", cons_exs))

cons_lesson = {
    "id": "lesson.b1.reformkor.consolidation",
    "title": "The Reform Age: Unit 15 Consolidation",
    "level": "B1",
    "track": "citizenship",
    "estimatedMinutes": 25,
    "prerequisites": [
        "lesson.b1.reformkor.01",
        "lesson.b1.reformkor.02",
        "lesson.b1.reformkor.03",
        "lesson.b1.reformkor.04",
        "lesson.b1.reformkor.05"
    ],
    "grammar": ["Unit review"],
    "vocabulary": ["Unit review"],
    "culturalContext": "Magyar történelem összefoglalás (Honosítási vizsgafelkészítő)",
    "sections": [
        {
            "type": "intro",
            "title": "Unit 15 Consolidation: The Reform Age (1825–1848)",
            "body": "Ebben az összefoglaló leckében átismételjük a reformkor nyitányát és a Magyar Tudományos Akadémia megalapítását (1825), Széchenyi István gyakorlati és elméleti reformjait (Hitel, Lánchíd), Kossuth Lajos sajtómunkásságát és az érdekegyesítés politikáját, a két reformer vitáját, valamint az 1844-es államnyelvi törvényt és a nemzeti jelképek (Himnusz, Szózat) születését."
        },
        {
            "type": "goal",
            "title": "Consolidation Goals",
            "items": [
                "A reformkor kulcséveinek (1825, 1830, 1841, 1844) és vezető alakjainak pontos ismerete",
                "Célhatározói, korszerűsítési és vitaérvelési szerkezetek magabiztos alkalmazása",
                "A polgári átalakulás alapfogalmainak (érdekegyesítés, örökváltság, államnyelv, Lánchíd) birtoklása"
            ]
        },
        {
            "type": "exercise-group",
            "title": "Comprehensive Unit 15 Practice",
            "ref": "ex.b1.reformkor.consolidation",
            "exerciseRefs": [e["id"] for e in cons_exs]
        },
        {
            "type": "checklist",
            "items": [
                "Tudom, mikor kezdődött a reformkor és mit ajánlott fel Széchenyi (1825)",
                "Ismerem Széchenyi 'Hitel' című művét és gyakorlati alkotásait (Lánchíd, folyószabályozás)",
                "Értem Kossuth 'érdekegyesítés' programját és a Széchenyivel folytatott vitáját",
                "Tudom, mikor vált a magyar hivatalos államnyelvvé (1844) és kik írták a Himnuszt meg a Szózatot"
            ]
        }
    ]
}
write_json(LESSONS_DIR / "lesson.b1.reformkor.consolidation.json", cons_lesson)

print("Unit 15 (b1-reformkor) complete!")
