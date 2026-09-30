# -*- coding: utf-8 -*-
"""
Full Unit 10 Overhaul: Three Parts of Hungary (b1-haromresz)
Lessons:
1. Buda török kézre kerülése és az ország három részre szakadása (1541)
2. A három országrész berendezkedése és közigazgatása
3. A végvári élet és a kettős adóztatás
4. 1552 dicsősége: Eger és Drégely hősies védelme
5. Szigetvár ostroma és Zrínyi Miklós kirohanása (1566)
Consolidation: Unit 10 Capstone (20 exercises)
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
# LESSON 1: b1-haromresz-01 (Buda eleste 1541)
# ==========================================
story_1 = make_story(
    "story.b1.haromresz.01",
    "Buda török kézre kerülése (1541. augusztus 29.)",
    "Szapolyai János halála után Szulejmán szultán csellel elfoglalta a budai várat, ezzel Magyarország három részre szakadt.",
    "Buda vára",
    ["Passive and impersonal structures (kézre kerül, sor kerül rá)", "Historical dramatic narrative"],
    ["Buda eleste", "három részre szakadás", "csel", "Fráter György", "Izabella királyné"],
    [
        "1540-ben meghalt Szapolyai János király, alig néhány nappal fia, János Zsigmond születése után. A csecsemő védelmében Fráter György barát Szulejmán szultánhoz fordult védelemért a váradi békét érvényesíteni kívánó Habsburg Ferdinánd csapatai ellen.",
        "A szultán hatalmas sereggel érkezett Buda alá 1541 augusztusában. Miután visszaverte az osztrák ostromlókat, a szultán magához kérette a magyar főurakat és a csecsemő királyt a táborába vendégségre. Mialatt a vendéglátás zajlott, a török janicsárok fegyvertelenül, 'városnézés' ürügyén besétáltak a budai várba, majd egy adott jelre birtokba vették a kapukat.",
        "1541. augusztus 29-én – pontosan tizenöt évvel a mohácsi csata után – Buda harc nélkül került török kézre. Ezzel a történelmi eseménnyel a Magyar Királyság másfél évszázadra három részre szakadt."
    ],
    [
        {"lemma": "csel", "pos": "noun", "cefr": "B1", "gloss": "trick, ruse, stratagem"},
        {"lemma": "ürügy", "pos": "noun", "cefr": "B1", "gloss": "pretext, excuse"},
        {"lemma": "birtokba vesz", "pos": "verb", "cefr": "B1", "gloss": "to take possession of, seize"},
        {"lemma": "kézre kerül", "pos": "verb", "cefr": "B1", "gloss": "to fall into the hands of"},
        {"lemma": "három részre szakadás", "pos": "noun", "cefr": "B1", "gloss": "tripartite division"}
    ],
    [
        {
            "question": "Hogyan foglalta el a török sereg Budát 1541-ben?",
            "options": ["Csellel: a vendégség ideje alatt besétáltak a várba és elfoglalták a kapukat", "Hosszú és véres ostrommal", "Ferdinánd adta át nekik szerződésben", "A magyar lakosság önként hívta be őket"],
            "correctIndex": 0,
            "explanation": "Szulejmán szultán csellel foglalta el Budát: mialatt a főurakat vendégül látta, a janicsárok megszállták a várat."
        }
    ]
)
write_json(STORIES_DIR / "story.b1.haromresz.01.json", story_1)

voc_1 = {
    "id": "voc.b1.haromresz.01",
    "title": "Buda elestének és az ország felosztásának szókincse",
    "description": "Cselvetés, diplomáciai ürügy, megszállás és a három részre szakadás kifejezései.",
    "entries": [
        {"lemma": "csel", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "ruse, trick, deceptive tactic", "examples": [{"hu": "A szultán csellel vette be a budai várat.", "en": "The Sultan captured the castle of Buda with a ruse."}]}]},
        {"lemma": "ürügy", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "pretext, excuse", "examples": [{"hu": "A katonák városnézés ürügyén sétáltak be a kapun.", "en": "The soldiers walked in through the gate under the pretext of sightseeing."}]}]},
        {"lemma": "birtokba vesz", "pos": "verb", "cefr": "B1", "definitions": [{"meaning": "to take possession of, seize", "examples": [{"hu": "A janicsárok azonnal birtokba vették a bástyákat.", "en": "The Janissaries immediately took possession of the bastions."}]}]},
        {"lemma": "kézre kerül", "pos": "verb", "cefr": "B1", "definitions": [{"meaning": "to fall into enemy hands", "examples": [{"hu": "Buda 1541-ben került oszmán kézre.", "en": "Buda fell into Ottoman hands in 1541."}]}]},
        {"lemma": "három részre szakadás", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "tripartite division of Hungary", "examples": [{"hu": "1541-gyel megkezdődött az ország három részre szakadása.", "en": "With 1541 began the tripartite division of the country."}]}]}
    ]
}
write_json(VOCAB_DIR / "voc.b1.haromresz.01.json", voc_1)

gr_1 = {
    "id": "gr.b1.haromresz.01",
    "title": "Személytelen és passzív jellegű szerkezetek (kézre kerül, sor kerül rá, birtokba vesz)",
    "description": "Expressing events, seizures, and outcomes using impersonal Hungarian structures.",
    "rules": [
        "A 'kézre kerül' szerkezet az uralom vagy hatalom átkerülését jelöli egy adott szereplőhöz: 'török kézre került'.",
        "A 'sor kerül valamire' szerkezet egy esemény bekövetkezését, lezajlását fejezi ki: 'sor került a békekötésre'.",
        "A 'birtokba vesz' egy terület feletti közvetlen ellenőrzés átvételét jelöli."
    ],
    "tables": [
        {"headers": ["Szerkezet", "Jelentés", "Példa"], "rows": [
            ["kézre kerül", "to fall into the hands of", "A főváros ellenséges kézre került."],
            ["sor kerül valamire", "to take place, come about", "1541-ben sor került a megszállásra."],
            ["birtokba vesz", "to seize, take control", "A csapatok birtokba vették a kapukat."]
        ]}
    ],
    "examples": [
        {"spanish": "1541. augusztus 29-én Buda harc nélkül került török kézre.", "english": "On August 29, 1541, Buda fell into Turkish hands without a fight."},
        {"spanish": "A tárgyalások után sor került a magyar főurak fogva tartására.", "english": "After the negotiations, the detention of the Hungarian lords took place."},
        {"spanish": "A janicsárok egy adott jelre birtokba vették a fellegvárat.", "english": "Upon a given signal, the Janissaries took possession of the citadel."}
    ]
}
write_json(GRAMMAR_DIR / "gr.b1.haromresz.01.json", gr_1)

exs_1 = [
    {"id": "ex.b1.haromresz.01.01", "type": "multiple-choice", "lesson": "lesson.b1.haromresz.01", "teaches": ["Buda-eleste"], "prompt": "Melyik évben és milyen napon került Buda török kézre?", "options": ["1541. augusztus 29-én", "1526. augusztus 29-én", "1456. július 22-én", "1552. szeptember 11-én"], "correctIndex": 0, "explanation": "Buda 1541. augusztus 29-én esett el."},
    {"id": "ex.b1.haromresz.01.02", "type": "fill-blank", "lesson": "lesson.b1.haromresz.01", "teaches": ["csel"], "prompt": "Egészítsd ki a mondatot!", "sentence": "Szulejmán szultán katonai *csellel* foglalta el a budai várat.", "target": "csellel"},
    {"id": "ex.b1.haromresz.01.03", "type": "sentence-builder", "lesson": "lesson.b1.haromresz.01", "teaches": ["kezre-kerul", "Buda"], "prompt": "Rakd össze a mondatot a helyes sorrendben!", "chips": ["Buda", "1541-ben", "török", "kézre", "került."], "target": "Buda 1541-ben török kézre került.", "english": "Buda fell into Turkish hands in 1541."},
    {"id": "ex.b1.haromresz.01.04", "type": "multiple-choice", "lesson": "lesson.b1.haromresz.01", "teaches": ["urugy"], "prompt": "Milyen ürüggyel mentek be a janicsárok a várba?", "options": ["Városnézés és barátságos látogatás ürügyén", "Fegyverjavítás ürügyén", "Kereskedelem céljából", "Királyválasztás miatt"], "correctIndex": 0, "explanation": "A janicsárok 'városnézés' (látogatás) ürügyén fegyvertelenül sétáltak be."},
    {"id": "ex.b1.haromresz.01.05", "type": "fill-blank", "lesson": "lesson.b1.haromresz.01", "teaches": ["birtokba-vesz"], "prompt": "Egészítsd ki a mondatot a megfelelő igealakkal!", "sentence": "A janicsárok gyorsan *birtokba vették* a várkapukat.", "target": "birtokba vették"},
    {"id": "ex.b1.haromresz.01.06", "type": "sentence-builder", "lesson": "lesson.b1.haromresz.01", "teaches": ["harom-reszre-szakadas"], "prompt": "Alkoss történelmi összefüggést kifejező mondatot!", "chips": ["Magyarország", "másfél", "évszázadra", "három", "részre", "szakadt."], "target": "Magyarország másfél évszázadra három részre szakadt.", "english": "Hungary split into three parts for a century and a half."},
    {"id": "ex.b1.haromresz.01.07", "type": "multiple-choice", "lesson": "lesson.b1.haromresz.01", "teaches": ["Frater-Gyorgy"], "prompt": "Ki volt a csecsemő János Zsigmond gyámja és a korszak meghatározó politikusa?", "options": ["Fráter György (Martinuzzi)", "Dobó István", "Bakócz Tamás", "Pázmány Péter"], "correctIndex": 0, "explanation": "Fráter György barát irányította a keleti országrész politikáját."},
    {"id": "ex.b1.haromresz.01.08", "type": "fill-blank", "lesson": "lesson.b1.haromresz.01", "teaches": ["urugy"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A katonák békés látogatás *ürügyén* hatoltak be a várba.", "target": "ürügyén"}
]
write_json(EXERCISES_DIR / "ex.b1.haromresz.01.json", make_exercise_group("ex.b1.haromresz.01", "Buda eleste gyakorlatok", "Gyakorlatok az 1541-es eseményekről és az országrészek kialakulásáról.", exs_1))

lesson_1 = make_lesson(
    "lesson.b1.haromresz.01",
    "Buda török kézre kerülése (1541. augusztus 29.)",
    "Személytelen és passzív szerkezetek (kézre kerül, sor kerül rá)",
    "Részletesen megismerjük Szulejmán szultán 1541-es cselét, Buda elestét és az ország három részre szakadását.",
    ["Megérteni az 1541-es dátum jelentőségét", "Használni a 'kézre kerül' és 'birtokba vesz' szerkezeteket", "Ismerni a három részre szakadás történelmi hátterét"],
    "story.b1.haromresz.01",
    "voc.b1.haromresz.01",
    "gr.b1.haromresz.01",
    "ex.b1.haromresz.01",
    [e["id"] for e in exs_1]
)
write_json(LESSONS_DIR / "lesson.b1.haromresz.01.json", lesson_1)


# ==========================================
# LESSON 2: b1-haromresz-02 (A három országrész berendezkedése)
# ==========================================
story_2 = make_story(
    "story.b1.haromresz.02",
    "A három országrész berendezkedése és közigazgatása",
    "1541 után Magyarország területe három önálló politikai egységre tagolódott: a Királyi Magyarországra, a Török Hódoltságra és az Erdélyi Fejedelemségre.",
    "Pozsony, Buda és Gyulafehérvár",
    ["Comparative and contrastive structures (míg... addig, szemben azzal, hogy, viszont)", "Administrative categorization"],
    ["Királyi Magyarország", "Török Hódoltság", "Erdélyi Fejedelemség", "pasa", "vilajet"],
    [
        "A három részre szakadt ország mindegyik része sajátos berendezkedést alakított ki. A nyugati és északi sávot a Királyi Magyarország alkotta a Habsburg uralkodók alatt, amelynek fővárosa Pozsony lett, míg a pénzügyeket a Magyar Kamara, a katonai védelmet pedig az Udvari Haditanács irányította Bécsből.",
        "A középső termékeny síkságokon a Török Hódoltság jött létre, amelyet vilajetekre osztottak, élükön a budai pasával. Itt a szultáni kincstár közvetlen adóztatást vezetett be a keresztény lakosságra (harács), míg a keresztény templomok egy részét dzsámivá alakították át.",
        "A keleti részeken ezzel szemben létrejött az Erdélyi Fejedelemség, amely a török szultán hűbéreseként, de széles belső önállósággal (autonómiával) működött. Erdély fejedelmei és rendi gyűlése a magyar nyelv és államiság bástyájává vált a nehéz évszázadok során."
    ],
    [
        {"lemma": "hódoltság", "pos": "noun", "cefr": "B1", "gloss": "Ottoman-occupied territory"},
        {"lemma": "fejedelemség", "pos": "noun", "cefr": "B1", "gloss": "principality"},
        {"lemma": "vilajet", "pos": "noun", "cefr": "B1", "gloss": "Ottoman administrative province"},
        {"lemma": "önállóság", "pos": "noun", "cefr": "B1", "gloss": "autonomy, independence"},
        {"lemma": "hűbéres", "pos": "noun", "cefr": "B1", "gloss": "vassal, tributary state"}
    ],
    [
        {
            "question": "Melyik három országrészre szakadt Magyarország 1541 után?",
            "options": ["Királyi Magyarország, Török Hódoltság és Erdélyi Fejedelemség", "Ausztria, Lengyelország és Magyarország", "Dunántúl, Alföld és Felvidék", "Királyság, Köztársaság és Hercegség"],
            "correctIndex": 0,
            "explanation": "A három országrész: Királyi Magyarország (Habsburg), Hódoltság (Oszmán) és Erdélyi Fejedelemség."
        }
    ]
)
write_json(STORIES_DIR / "story.b1.haromresz.02.json", story_2)

voc_2 = {
    "id": "voc.b1.haromresz.02",
    "title": "A három országrész közigazgatási szókincse",
    "description": "Vilajet, pasa, autonómia, hűbéres státusz és közigazgatási felosztás.",
    "entries": [
        {"lemma": "hódoltság", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "Ottoman occupation territory in Hungary", "examples": [{"hu": "A Hódoltság területét a budai pasa irányította.", "en": "The territory of the Ottoman domain was governed by the Pasha of Buda."}]}]},
        {"lemma": "fejedelemség", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "principality", "examples": [{"hu": "Az Erdélyi Fejedelemség magyar vezetés alatt maradt.", "en": "The Principality of Transylvania remained under Hungarian leadership."}]}]},
        {"lemma": "vilajet", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "Ottoman province", "examples": [{"hu": "A szultán a meghódított földeket vilajetekre osztotta.", "en": "The Sultan divided the conquered lands into vilayets."}]}]},
        {"lemma": "önállóság", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "autonomy, self-rule", "examples": [{"hu": "Erdély jelentős belső önállóságot élvezett.", "en": "Transylvania enjoyed significant internal autonomy."}]}]},
        {"lemma": "hűbéres", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "vassal", "examples": [{"hu": "A fejedelem adót fizetett a szultánnak mint hűbéres.", "en": "The Prince paid tribute to the Sultan as a vassal."}]}]}
    ]
}
write_json(VOCAB_DIR / "voc.b1.haromresz.02.json", voc_2)

gr_2 = {
    "id": "gr.b1.haromresz.02",
    "title": "Összehasonlító és ellentétes szerkezetek (míg... addig, szemben azzal, hogy, viszont)",
    "description": "Comparing regions, administrative systems, and political structures.",
    "rules": [
        "A 'míg... addig' párhuzamos ellentétet vagy összehasonlítást fejez ki két cselekvés/állapot között.",
        "A 'szemben azzal, hogy' közvetlen kontrasztot mutat be egy korábbi állítással szemben.",
        "A 'viszont' mondatközi kötőszóként az egyszerűbb ellentétet jelzi."
    ],
    "tables": [
        {"headers": ["Kötőszó / Kifejezés", "Funkció", "Példa"], "rows": [
            ["míg... (addig)", "párhuzamos ellentét", "Míg Buda török lett, addig Pozsony a királyi főváros."],
            ["szemben azzal, hogy", "kontraszt", "Szemben a Hódoltsággal, Erdély autonóm maradt."],
            ["viszont", "enyhébb ellentét", "Adót fizettek, viszont megtarthatták vallásukat."]
        ]}
    ],
    "examples": [
        {"spanish": "Míg a Királyi Magyarországot a Habsburgok uralták, addig Erdély önálló fejedelemség lett.", "english": "While Royal Hungary was ruled by the Habsburgs, Transylvania became an independent principality."},
        {"spanish": "Szemben a török Hódoltsággal, Erdélyben fennmaradt a magyar közigazgatás.", "english": "In contrast to the Turkish territory, Hungarian administration survived in Transylvania."},
        {"spanish": "A fejedelem hűbéradóval tartozott, viszont a belső törvényeket a diéta alkotta.", "english": "The Prince owed tribute, but internal laws were made by the Diet."}
    ]
}
write_json(GRAMMAR_DIR / "gr.b1.haromresz.02.json", gr_2)

exs_2 = [
    {"id": "ex.b1.haromresz.02.01", "type": "multiple-choice", "lesson": "lesson.b1.haromresz.02", "teaches": ["Kiralyi-Magyarorszag"], "prompt": "Mi lett a Királyi Magyarország fővárosa 1541 után?", "options": ["Pozsony", "Debrecen", "Kolozsvár", "Szeged"], "correctIndex": 0, "explanation": "A Királyi Magyarország központja és a koronázóváros Pozsony lett."},
    {"id": "ex.b1.haromresz.02.02", "type": "fill-blank", "lesson": "lesson.b1.haromresz.02", "teaches": ["hodoltsag"], "prompt": "Egészítsd ki a mondatot!", "sentence": "Az ország középső területeit a Török *Hódoltság* foglalta magában.", "target": "Hódoltság"},
    {"id": "ex.b1.haromresz.02.03", "type": "sentence-builder", "lesson": "lesson.b1.haromresz.02", "teaches": ["mig", "Erdely"], "prompt": "Rakd össze az összehasonlító mondatot!", "chips": ["Míg", "Pozsony", "főváros", "lett,", "addig", "Erdély", "önálló", "maradt."], "target": "Míg Pozsony főváros lett, addig Erdély önálló maradt.", "english": "While Pozsony became the capital, Transylvania remained autonomous."},
    {"id": "ex.b1.haromresz.02.04", "type": "multiple-choice", "lesson": "lesson.b1.haromresz.02", "teaches": ["vilajet"], "prompt": "Hogy hívták az oszmán közigazgatási tartományokat a Hódoltságban?", "options": ["Vilajet", "Vármegye", "Bánság", "Kerület"], "correctIndex": 0, "explanation": "A vilajet volt az oszmán közigazgatási egység, élén a pasával."},
    {"id": "ex.b1.haromresz.02.05", "type": "fill-blank", "lesson": "lesson.b1.haromresz.02", "teaches": ["onallosag"], "prompt": "Egészítsd ki a mondatot!", "sentence": "Az Erdélyi Fejedelemség széles belső *önállóságot* élvezett a korszakban.", "target": "önállóságot"},
    {"id": "ex.b1.haromresz.02.06", "type": "sentence-builder", "lesson": "lesson.b1.haromresz.02", "teaches": ["szemben", "hodoltsag"], "prompt": "Alkoss helyes mondatot a megadott szavakból!", "chips": ["Szemben", "a", "Hódoltsággal,", "Erdély", "szabadon", "választott", "fejedelmet."], "target": "Szemben a Hódoltsággal, Erdély szabadon választott fejedelmet.", "english": "In contrast to the Ottoman domain, Transylvania freely elected its prince."},
    {"id": "ex.b1.haromresz.02.07", "type": "multiple-choice", "lesson": "lesson.b1.haromresz.02", "teaches": ["huberes"], "prompt": "Milyen viszonyban állt az Erdélyi Fejedelemség a szultánnal?", "options": ["Hűbéres adófizető volt, de belső ügyeiben független", "Teljes katonai megszállás alatt állt", "Semmilyen kapcsolata nem volt vele", "Erdély uralta a török birodalmat"], "correctIndex": 0, "explanation": "Erdély hűbéradóval tartozott, de belügyeiben autonóm maradt."},
    {"id": "ex.b1.haromresz.02.08", "type": "fill-blank", "lesson": "lesson.b1.haromresz.02", "teaches": ["fejedelemseg"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A keleti országrészből alakult ki az Erdélyi *Fejedelemség*.", "target": "Fejedelemség"}
]
write_json(EXERCISES_DIR / "ex.b1.haromresz.02.json", make_exercise_group("ex.b1.haromresz.02", "A három országrész gyakorlatai", "Gyakorlatok a három országrész intézményeiről és az összehasonlító mondatokról.", exs_2))

lesson_2 = make_lesson(
    "lesson.b1.haromresz.02",
    "A három országrész berendezkedése és közigazgatása",
    "Összehasonlító és ellentétes szerkezetek (míg... addig, szemben azzal)",
    "Megtanuljuk a Királyi Magyarország, a Hódoltság és az Erdélyi Fejedelemség politikai és társadalmi berendezkedését.",
    ["Megkülönböztetni a három országrészt és központjaikat", "Alkalmazni a 'míg... addig' és 'szemben azzal' szerkezeteket", "Ismerni a vilajet, hűbéres és autonómia fogalmait"],
    "story.b1.haromresz.02",
    "voc.b1.haromresz.02",
    "gr.b1.haromresz.02",
    "ex.b1.haromresz.02",
    [e["id"] for e in exs_2]
)
write_json(LESSONS_DIR / "lesson.b1.haromresz.02.json", lesson_2)


# ==========================================
# LESSON 3: b1-haromresz-03 (A végvári élet és kettős adóztatás)
# ==========================================
story_3 = make_story(
    "story.b1.haromresz.03",
    "A végvári élet és a kettős adóztatás",
    "A hódoltság peremén kiépült végvári vonal mindennapjait az állandó portyázások, a bajvívások és a jobbágyok kettős adóztatása jellemezte.",
    "A végvári vonal és mezővárosok",
    ["Habitual and iterative action suffixes (-gat/-get, gyakorta)", "Social history of the borderlands"],
    ["végvári vitéz", "portyázás", "kettős adóztatás", "bajvívás", "mezőváros"],
    [
        "A két világbirodalom határán több száz kilométer hosszan húzódott a végvári vonal. A végvárakban állomásozó vitézek nemcsak a várak falait védelmezték, hanem rendszeresen portyázgattak az ellenséges területeken, megakadályozva a török csapatok váratlan betöréseit.",
        "A végvári katonák élete állandó bizonytalanságban telt, mivel a zsold gyakorta hónapokat késett. A vitézek lovas párviadalokon (bajvívásokon) bizonyították bátorságukat a két tábor közötti senki földjén, amely a korszak lovagi hagyományának szerves részévé vált.",
        "A hódoltsági peremvidéken élő jobbágyok helyzete rendkívül nehéz volt: ők a kettős adóztatás terhét nyögték. Egyszerre fizettek adót a török szpáhi földesúrnak és a szultáni kincstárnak, miközben a menekült magyar nemesek és a királyi vármegye is behajtotta rajtuk a hagyományos járandóságokat."
    ],
    [
        {"lemma": "portyázás", "pos": "noun", "cefr": "B1", "gloss": "raiding, skirmishing expedition"},
        {"lemma": "kettős adóztatás", "pos": "noun", "cefr": "B1", "gloss": "double taxation"},
        {"lemma": "bajvívás", "pos": "noun", "cefr": "B1", "gloss": "duel, single combat"},
        {"lemma": "végvári vitéz", "pos": "noun", "cefr": "B1", "gloss": "border fortress warrior"},
        {"lemma": "behajt", "pos": "verb", "cefr": "B1", "gloss": "to collect/levy (taxes)"}
    ],
    [
        {
            "question": "Mit jelentett a kettős adóztatás a hódoltsági peremvidéken?",
            "options": ["A jobbágyoknak a török és a magyar földesúrnak is adózniuk kellett", "Kétszer annyi aranyat kellett fizetni a királynak", "Csak a nemesek fizettek adót", "A katonáknak nem kellett adózniuk"],
            "correctIndex": 0,
            "explanation": "A határvidék falvai a török hatóságoknak és a magyar vármegyének is adóztak."
        }
    ]
)
write_json(STORIES_DIR / "story.b1.haromresz.03.json", story_3)

voc_3 = {
    "id": "voc.b1.haromresz.03",
    "title": "A végvári élet és határvidék szókincse",
    "description": "Végvári harcok, bajvívás, portyázás és a jobbágyok adóterhei.",
    "entries": [
        {"lemma": "portyázás", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "raid, border skirmish expedition", "examples": [{"hu": "A végvári vitézek portyázásokkal zaklatták az ellenséget.", "en": "The border fortress warriors harassed the enemy with raids."}]}]},
        {"lemma": "kettős adóztatás", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "double taxation of serfs", "examples": [{"hu": "A parasztság a kettős adóztatás miatt sokat szenvedett.", "en": "The peasantry suffered greatly due to double taxation."}]}]},
        {"lemma": "bajvívás", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "duel, single combat between warriors", "examples": [{"hu": "A bajvívás a végvári vitézek lovagi erénye volt.", "en": "Single combat was a knightly virtue of border warriors."}]}]},
        {"lemma": "behajt", "pos": "verb", "cefr": "B1", "definitions": [{"meaning": "to collect, enforce tax payment", "examples": [{"hu": "A vármegye katonákkal hajtotta be a királyi adót.", "en": "The county enforced the collection of the royal tax with soldiers."}]}]},
        {"lemma": "zsold", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "military pay, soldier's wage", "examples": [{"hu": "A zsold gyakran hónapokat késett a várakban.", "en": "Pay was often delayed by months in the fortresses."}]}]}
    ]
}
write_json(VOCAB_DIR / "voc.b1.haromresz.03.json", voc_3)

gr_3 = {
    "id": "gr.b1.haromresz.03",
    "title": "Gyakorító igék és ismétlődő cselekvések (-gat/-get, gyakorta)",
    "description": "Expressing frequentative, repetitive, or habitual historical actions.",
    "rules": [
        "A '-gat / -get' képző a cselekvés ismétlődését, elnyújtott jellegét fejezi ki (portyázik -> portyázgat, néz -> nézeget).",
        "A 'gyakorta', 'rendszerint', 'nap mint nap' határozószók megerősítik a szokásos, ismétlődő történelmi tevékenységeket."
    ],
    "tables": [
        {"headers": ["Alapige", "Gyakorító alak", "Jelentés", "Példa"], "rows": [
            ["portyázik", "portyázgat", "frequent raiding", "A vitézek a határon portyázgattak."],
            ["támad", "támadgat", "repeated attacks", "Az ellenség kisebb csapatokkal támadgatott."],
            ["vált", "váltogat", "alternating", "A végvárakat sűrűn váltogatták."]
        ]}
    ],
    "examples": [
        {"spanish": "A végvári vitézek éjszakánként az ellenséges területeken portyázgattak.", "english": "The border fortress warriors frequently raided enemy territories at night."},
        {"spanish": "A katonák zsoldja gyakorta hónapokat késett.", "english": "The soldiers' pay frequently was delayed by months."},
        {"spanish": "A falvak lakói nap mint nap rettegtek a török betörésektől.", "english": "The villagers feared Turkish incursions day after day."}
    ]
}
write_json(GRAMMAR_DIR / "gr.b1.haromresz.03.json", gr_3)

exs_3 = [
    {"id": "ex.b1.haromresz.03.01", "type": "multiple-choice", "lesson": "lesson.b1.haromresz.03", "teaches": ["kettos-adoztatas"], "prompt": "Kik fizettek kettős adót a török korban?", "options": ["A hódoltsági peremterületek jobbágyai", "A budai török pasák", "A végvári kapitányok", "A királyi tanácsosok"], "correctIndex": 0, "explanation": "A végvári határvidék jobbágyai a török és magyar uraknak is adóztak."},
    {"id": "ex.b1.haromresz.03.02", "type": "fill-blank", "lesson": "lesson.b1.haromresz.03", "teaches": ["portyazas"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A végvári vitézek rendszeres *portyázásokkal* zavarták az ellenséget.", "target": "portyázásokkal"},
    {"id": "ex.b1.haromresz.03.03", "type": "sentence-builder", "lesson": "lesson.b1.haromresz.03", "teaches": ["bajvivas", "vitezek"], "prompt": "Rakd össze a mondatot a megfelelő sorrendben!", "chips": ["A", "vitézek", "bajvívásokon", "mérték", "össze", "erejüket."], "target": "A vitézek bajvívásokon mérték össze erejüket.", "english": "The warriors measured their strength in single combat."},
    {"id": "ex.b1.haromresz.03.04", "type": "multiple-choice", "lesson": "lesson.b1.haromresz.03", "teaches": ["zsold"], "prompt": "Mit jelent a katonai 'zsold'?", "options": ["A katonák rendszeres fizetségét", "A vár építésének költségét", "A zsákmányolt aranyat", "A török adót"], "correctIndex": 0, "explanation": "A zsold a katonák járandósága, pénzbeli fizetése volt."},
    {"id": "ex.b1.haromresz.03.05", "type": "fill-blank", "lesson": "lesson.b1.haromresz.03", "teaches": ["behajt"], "prompt": "Egészítsd ki a mondatot a megfelelő igealakkal!", "sentence": "A vármegye fegyverrel *hajtotta be* az elmaradt adót.", "target": "hajtotta be"},
    {"id": "ex.b1.haromresz.03.06", "type": "sentence-builder", "lesson": "lesson.b1.haromresz.03", "teaches": ["gyakorta", "zsold"], "prompt": "Alkoss szabályos mondatot!", "chips": ["A", "vitézek", "zsoldja", "gyakorta", "hónapokat", "késett."], "target": "A vitézek zsoldja gyakorta hónapokat késett.", "english": "The warriors' pay frequently was delayed by months."},
    {"id": "ex.b1.haromresz.03.07", "type": "multiple-choice", "lesson": "lesson.b1.haromresz.03", "teaches": ["bajvivas"], "prompt": "Mi volt a bajvívás lényege a végvári életben?", "options": ["Két kiválasztott vitéz párviadala a két sereg előtt", "Íjászat gyakorlása", "Kereskedelmi alku", "Közös lakoma"], "correctIndex": 0, "explanation": "A bajvívás két vitéz párharca volt a senki földjén."},
    {"id": "ex.b1.haromresz.03.08", "type": "fill-blank", "lesson": "lesson.b1.haromresz.03", "teaches": ["kettos-adoztatas"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A jobbágyok a *kettős adóztatás* terhét viselték.", "target": "kettős adóztatás"}
]
write_json(EXERCISES_DIR / "ex.b1.haromresz.03.json", make_exercise_group("ex.b1.haromresz.03", "Végvári élet gyakorlatok", "Gyakorlatok a végvári harcokról, bajvívásokról és a gyakorító igékről.", exs_3))

lesson_3 = make_lesson(
    "lesson.b1.haromresz.03",
    "A végvári élet és a kettős adóztatás",
    "Gyakorító igék és ismétlődő cselekvések (-gat/-get, gyakorta)",
    "Részletesen bemutatjuk a végvári vitézek mindennapjait, a portyákat, a bajvívást és a jobbágyság nehéz sorsát.",
    ["Megérteni a végvári vonal szerepét és működését", "Használni a gyakorító igéket (-gat/-get)", "Ismerni a kettős adóztatás és bajvívás fogalmát"],
    "story.b1.haromresz.03",
    "voc.b1.haromresz.03",
    "gr.b1.haromresz.03",
    "ex.b1.haromresz.03",
    [e["id"] for e in exs_3]
)
write_json(LESSONS_DIR / "lesson.b1.haromresz.03.json", lesson_3)


# ==========================================
# LESSON 4: b1-haromresz-04 (1552 hősei: Eger és Drégely)
# ==========================================
story_4 = make_story(
    "story.b1.haromresz.04",
    "1552 dicsősége: Eger és Drégely hősies védelme",
    "1552-ben a török hadjárat során Szondi György hősi halált halt Drégelynél, míg Dobó István és az egri várvédők megállították a hatalmas oszmán sereget.",
    "Eger vára és Drégely",
    ["Concessive clauses (bár, noha, ámbár, jóllehet)", "Heroic historical narratives"],
    ["Eger ostroma", "Dobó István", "egri nők", "Drégely", "Szondi György"],
    [
        "1552-ben Ahmed és Ali pasa egyesült serege óriási hadjáratot indított a magyar végvárak felszámolására. Drégely kis sziklai várában Szondi György várkapitány alig másfélszáz katonájával az utolsó leheletéig harcolt a tízezerszeres túlerő ellen, életét áldozva a hazáért.",
        "Az oszmán sereg ezt követően Eger alá vonult, amely az északi bányavárosok és a Felvidék kulcsa volt. Jóllehet a törökök több mint negyvenezer harcossal és nehézágyúkkal vették ostrom alá a várat, Dobó István kapitány és mintegy kétezer katonája esküvel fogadta, hogy a várat soha fel nem adják.",
        "A véres küzdelemben az egri nők is a bástyákra álltak, forró szurkot és köveket zúdítva a rohamozókra, míg Bornemissza Gergely tüzes kerekei rettenetes pusztítást végeztek. Bár a falak rommá lőttek, 1552 októberében a török sereg kénytelen volt megszégyenülten elvonulni Eger alól, megszerezve a magyar történelem egyik legfényesebb diadalát."
    ],
    [
        {"lemma": "hősiesség", "pos": "noun", "cefr": "B1", "gloss": "heroism, bravery"},
        {"lemma": "eskü", "pos": "noun", "cefr": "B1", "gloss": "oath, vow"},
        {"lemma": "tüzes kerék", "pos": "noun", "cefr": "B1", "gloss": "fire wheel (explosive weapon)"},
        {"lemma": "visszavonul", "pos": "verb", "cefr": "B1", "gloss": "to retreat, withdraw"},
        {"lemma": "diadal", "pos": "noun", "cefr": "B1", "gloss": "triumph, glorious victory"}
    ],
    [
        {
            "question": "Ki volt az egri vár kapitánya az 1552-es híres ostrom idején?",
            "options": ["Dobó István", "Szondi György", "Zrínyi Miklós", "Kinizsi Pál"],
            "correctIndex": 0,
            "explanation": "Dobó István vezette az egri várvédőket a törökök elleni diadalra 1552-ben."
        }
    ]
)
write_json(STORIES_DIR / "story.b1.haromresz.04.json", story_4)

voc_4 = {
    "id": "voc.b1.haromresz.04",
    "title": "Az 1552-es végvári diadal szókincse",
    "description": "Várvédelem, eskü, hősiesség, visszavonulás és fényes diadal.",
    "entries": [
        {"lemma": "hősiesség", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "heroism, self-sacrificing bravery", "examples": [{"hu": "A védők hősiessége megállította a túlerőt.", "en": "The defenders' heroism halted the superior force."}]}]},
        {"lemma": "eskü", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "solemn oath, vow", "examples": [{"hu": "Dobó István és katonái szent esküt tettek a vár védelmére.", "en": "István Dobó and his soldiers took a sacred oath to defend the castle."}]}]},
        {"lemma": "tüzes kerék", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "fire wheel, early incendiary explosive device", "examples": [{"hu": "Bornemissza Gergely tüzes kerekei megrémisztették a törököket.", "en": "Gergely Bornemissza's fire wheels terrified the Turks."}]}]},
        {"lemma": "visszavonul", "pos": "verb", "cefr": "B1", "definitions": [{"meaning": "to retreat, withdraw from battle", "examples": [{"hu": "A török sereg kénytelen volt visszavonulni Eger alól.", "en": "The Turkish army was forced to retreat from under Eger."}]}]},
        {"lemma": "diadal", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "triumph, glorious victory", "examples": [{"hu": "Az 1552-es egri diadal bevonult a történelembe.", "en": "The 1552 triumph of Eger entered into history."}]}]}
    ]
}
write_json(VOCAB_DIR / "voc.b1.haromresz.04.json", voc_4)

gr_4 = {
    "id": "gr.b1.haromresz.04",
    "title": "Megengedő mondatok (bár, noha, ámbár, jóllehet)",
    "description": "Constructing concessive clauses expressing contrast against overwhelming odds.",
    "rules": [
        "A megengedő kötőszavak ('bár', 'noha', 'ámbár', 'jóllehet') olyan körülményt mutatnak be, amely ellenére a főmondatban megfogalmazott cselekvés mégis megvalósul.",
        "A 'jóllehet' és 'ámbár' emelkedettebb, írásbeli és történeti stílusra jellemző."
    ],
    "tables": [
        {"headers": ["Kötőszó", "Stílus", "Példa"], "rows": [
            ["bár", "általános", "Bár túlerőben voltak, vesztettek."],
            ["noha", "formális", "Noha a falak leomlottak, Eger kitartott."],
            ["jóllehet", "irodalmi / választékos", "Jóllehet kevesen voltak, megvédték a várat."]
        ]}
    ],
    "examples": [
        {"spanish": "Bár a török sereg óriási túlerőben volt, az egriek nem adták fel a várat.", "english": "Although the Turkish army was in immense superior force, the defenders of Eger did not surrender the castle."},
        {"spanish": "Jóllehet Szondi György tudta, hogy meghal, nem fogadta el a megadási ajánlatot.", "english": "Although György Szondi knew he would die, he did not accept the surrender offer."},
        {"spanish": "Noha a bástyák rommá dőltek, a védők visszaverték az utolsó rohamot is.", "english": "Although the bastions crumbled into ruins, the defenders repelled even the last charge."}
    ]
}
write_json(GRAMMAR_DIR / "gr.b1.haromresz.04.json", gr_4)

exs_4 = [
    {"id": "ex.b1.haromresz.04.01", "type": "multiple-choice", "lesson": "lesson.b1.haromresz.04", "teaches": ["Eger-ostroma"], "prompt": "Melyik évben verte vissza Eger vára a török ostromot?", "options": ["1552-ben", "1526-ban", "1541-ben", "1566-ban"], "correctIndex": 0, "explanation": "Az egri diadal éve 1552 volt."},
    {"id": "ex.b1.haromresz.04.02", "type": "fill-blank", "lesson": "lesson.b1.haromresz.04", "teaches": ["esku"], "prompt": "Egészítsd ki a mondatot!", "sentence": "Dobó István és harcosai szent *esküt* tettek a vár védelmére.", "target": "esküt"},
    {"id": "ex.b1.haromresz.04.03", "type": "sentence-builder", "lesson": "lesson.b1.haromresz.04", "teaches": ["bar", "diadal"], "prompt": "Alkoss megengedő mondatot helyes sorrendben!", "chips": ["Bár", "kevesen", "voltak,", "fényes", "diadalt", "arattak."], "target": "Bár kevesen voltak, fényes diadalt arattak.", "english": "Although they were few, they won a glorious triumph."},
    {"id": "ex.b1.haromresz.04.04", "type": "multiple-choice", "lesson": "lesson.b1.haromresz.04", "teaches": ["Szondi-Gyorgy"], "prompt": "Melyik végvár hős kapitánya volt Szondi György 1552-ben?", "options": ["Drégely vára", "Szigetvár", "Kőszeg", "Komárom"], "correctIndex": 0, "explanation": "Szondi György Drégely sziklavárát védte hősi haláláig."},
    {"id": "ex.b1.haromresz.04.05", "type": "fill-blank", "lesson": "lesson.b1.haromresz.04", "teaches": ["egri-nok"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A falakon hősiesen küzdöttek az *egri nők* is a rohamozók ellen.", "target": "egri nők"},
    {"id": "ex.b1.haromresz.04.06", "type": "sentence-builder", "lesson": "lesson.b1.haromresz.04", "teaches": ["jollehet", "tuzes-kerek"], "prompt": "Rakd össze a megengedő mondatot!", "chips": ["Jóllehet", "támadtak,", "a", "tüzes", "kerekek", "megállították", "őket."], "target": "Jóllehet támadtak, a tüzes kerekek megállították őket.", "english": "Although they attacked, the fire wheels stopped them."},
    {"id": "ex.b1.haromresz.04.07", "type": "multiple-choice", "lesson": "lesson.b1.haromresz.04", "teaches": ["Bornemissza"], "prompt": "Milyen találmánnyal segítette Bornemissza Gergely Eger védelmét?", "options": ["Tüzes kerekekkel és robbanó bombákkal", "Páncélozott hajókkal", "Lopakodó alagutakkal", "Külföldi puskásokkal"], "correctIndex": 0, "explanation": "Bornemissza Gergely tüzes szerszámai és tüzes kerekei pusztították az ostromlókat."},
    {"id": "ex.b1.haromresz.04.08", "type": "fill-blank", "lesson": "lesson.b1.haromresz.04", "teaches": ["visszavonul"], "prompt": "Egészítsd ki a mondatot a megfelelő igealakkal!", "sentence": "Az oszmán hadsereg kénytelen volt *visszavonulni* Eger falai alól.", "target": "visszavonulni"}
]
write_json(EXERCISES_DIR / "ex.b1.haromresz.04.json", make_exercise_group("ex.b1.haromresz.04", "Eger és Drégely gyakorlatok", "Gyakorlatok az 1552-es eseményekről és a megengedő mellékmondatokról.", exs_4))

lesson_4 = make_lesson(
    "lesson.b1.haromresz.04",
    "1552 dicsősége: Eger és Drégely hősies védelme",
    "Megengedő összetett mondatok (bár, noha, jóllehet)",
    "Megismerjük az 1552-es végvári harcokat: Szondi György önfeláldozását Drégelynél és Dobó István egri diadalát.",
    ["Megérteni az 1552-es egri diadal jelentőségét", "Használni a megengedő kötőszavakat (bár, jóllehet)", "Ismerni Dobó István, Szondi György és Bornemissza Gergely nevét"],
    "story.b1.haromresz.04",
    "voc.b1.haromresz.04",
    "gr.b1.haromresz.04",
    "ex.b1.haromresz.04",
    [e["id"] for e in exs_4]
)
write_json(LESSONS_DIR / "lesson.b1.haromresz.04.json", lesson_4)


# ==========================================
# LESSON 5: b1-haromresz-05 (Szigetvár ostroma 1566)
# ==========================================
story_5 = make_story(
    "story.b1.haromresz.05",
    "Szigetvár ostroma és Zrínyi Miklós kirohanása (1566)",
    "1566-ban Zrínyi Miklós gróf maroknyi seregével heteken át tartotta Szigetvárt a szultán főserege ellen, majd hősi kirohanásban esett el.",
    "Szigetvár",
    ["Final and purpose clauses (azért, hogy, abból a célból, hogy)", "Historical heroics and legacy"],
    ["Szigetvár", "Zrínyi Miklós", "kirohanás", "Szulejmán szultán", "önfeláldozás"],
    [
        "1566-ban az idős, hetvenkét éves I. Szulejmán szultán utolsó hadjáratára indult azzal a céllal, hogy elfoglalja Bécset. Az útjában álló legfontosabb dél-dunántúli akadály Szigetvár mocsaras erődítménye volt, amelyet gróf Zrínyi Miklós védelmezett mintegy kétezer-ötszáz magyar és horvát vitéz élén.",
        "A török sereg heteken át lőtte és rohamozta a falakat, lecsapolva a várat védő mocsarat. Mielőtt az ostrom véget ért volna, a sátorában meghalt maga Szulejmán szultán is, de vezérei titokban tartották a halálhírt, azért, hogy a katonák harci kedve ne törjön meg.",
        "Amikor a belső vár is lángokban állt, Zrínyi nem a megadást választotta: ünnepi ruhát öltött, és megmaradt háromszáz hősével kinyittatta a kaput, hogy halálos rohammal rontson a törökökre. Zrínyi önfeláldozó kirohanása megmentette Bécset a támadástól, és nevét örökre a keresztény Európa leghíresebb mártírjai közé emelte."
    ],
    [
        {"lemma": "kirohanás", "pos": "noun", "cefr": "B1", "gloss": "sally, heroic sortie"},
        {"lemma": "önfeláldozás", "pos": "noun", "cefr": "B1", "gloss": "self-sacrifice"},
        {"lemma": "mocsaras", "pos": "adjective", "cefr": "B1", "gloss": "marshy, swampy"},
        {"lemma": "mártír", "pos": "noun", "cefr": "B1", "gloss": "martyr"},
        {"lemma": "akadály", "pos": "noun", "cefr": "B1", "gloss": "obstacle, impediment"}
    ],
    [
        {
            "question": "Mit tett Zrínyi Miklós 1566-ban, amikor a vár lángokban állt?",
            "options": ["Hősies kirohanást hajtott végre katonáival a kapun át", "Megadta magát és átadta a kulcsokat", "Alagúton át elmenekült Bécsbe", "Békét kötött a törökökkel"],
            "correctIndex": 0,
            "explanation": "Zrínyi Miklós és megmaradt vitézei hősies kirohanást hajtottak végre a belső várból."
        }
    ]
)
write_json(STORIES_DIR / "story.b1.haromresz.05.json", story_5)

voc_5 = {
    "id": "voc.b1.haromresz.05",
    "title": "Szigetvár és a hősi kirohanás szókincse",
    "description": "Kirohanás, önfeláldozás, mártíromság, akadály és ostromharc.",
    "entries": [
        {"lemma": "kirohanás", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "heroic sally, breakout attack from a besieged fortress", "examples": [{"hu": "Zrínyi kirohanása az önfeláldozás jelképe lett.", "en": "Zrínyi's sortie became the symbol of self-sacrifice."}]}]},
        {"lemma": "önfeláldozás", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "self-sacrifice, devotion", "examples": [{"hu": "A védők önfeláldozása feltartóztatta a szultán hadát.", "en": "The self-sacrifice of the defenders held up the Sultan's army."}]}]},
        {"lemma": "mocsaras", "pos": "adjective", "cefr": "B1", "definitions": [{"meaning": "marshy, surrounded by swamps", "examples": [{"hu": "Szigetvárt mocsaras terület vette körül.", "en": "Szigetvár was surrounded by marshy terrain."}]}]},
        {"lemma": "mártír", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "martyr", "examples": [{"hu": "Zrínyi Miklós a nemzet mártírjaként halt meg.", "en": "Miklós Zrínyi died as a martyr of the nation."}]}]},
        {"lemma": "feltartóztat", "pos": "verb", "cefr": "B1", "definitions": [{"meaning": "to halt, hold up (an advancing force)", "examples": [{"hu": "Szigetvár hetekre feltartóztatta a török előrenyomulást.", "en": "Szigetvár held up the Turkish advance for weeks."}]}]}
    ]
}
write_json(VOCAB_DIR / "voc.b1.haromresz.05.json", voc_5)

gr_5 = {
    "id": "gr.b1.haromresz.05",
    "title": "Célhatározói mondatok (azért, hogy, abból a célból, hogy)",
    "description": "Constructing purpose and final clauses in historical intentions and decisions.",
    "rules": [
        "A célhatározói összetett mondatokban a kötőszó a 'hogy', a főmondatban pedig gyakran szerepel az 'azért', 'azzal a céllal', 'abból a célból' utalószó.",
        "A mellékmondat állítmánya felszólító módban áll (-jon, -jen, -jön / -d): 'azért, hogy megvédje a hazát'."
    ],
    "tables": [
        {"headers": ["Utalószó + Kötőszó", "Mód a mellékmondatban", "Példa"], "rows": [
            ["azért... hogy", "felszólító mód", "Azért harcolt, hogy megmentse Bécset."],
            ["azzal a céllal, hogy", "felszólító mód", "Azzal a céllal indult, hogy várat foglaljon."],
            ["abból a célból, hogy", "felszólító mód", "Kirohant, abból a célból, hogy pusztítson."]
        ]}
    ],
    "examples": [
        {"spanish": "Zrínyi azért rohant ki a várból, hogy emelt fővel haljon meg a csatában.", "english": "Zrínyi sallied out of the castle in order to die in battle with his head held high."},
        {"spanish": "A pasák eltitkolták a szultán halálát, azért, hogy ne törjön meg a sereg fegyelme.", "english": "The Pashas concealed the Sultan's death in order that the army's discipline would not break."},
        {"spanish": "A katonák azért védték Szigetvárt, hogy megállítsák a török előrenyomulást.", "english": "The soldiers defended Szigetvár in order to stop the Turkish advance."}
    ]
}
write_json(GRAMMAR_DIR / "gr.b1.haromresz.05.json", gr_5)

exs_5 = [
    {"id": "ex.b1.haromresz.05.01", "type": "multiple-choice", "lesson": "lesson.b1.haromresz.05", "teaches": ["Szigetvar-1566"], "prompt": "Melyik évben zajlott Szigetvár legendás ostroma?", "options": ["1566-ban", "1552-ben", "1526-ban", "1541-ben"], "correctIndex": 0, "explanation": "Szigetvár ostroma és Zrínyi kirohanása 1566-ban történt."},
    {"id": "ex.b1.haromresz.05.02", "type": "fill-blank", "lesson": "lesson.b1.haromresz.05", "teaches": ["kirohanas"], "prompt": "Egészítsd ki a mondatot!", "sentence": "Zrínyi Miklós hősies *kirohanást* hajtott végre katonáival.", "target": "kirohanást"},
    {"id": "ex.b1.haromresz.05.03", "type": "sentence-builder", "lesson": "lesson.b1.haromresz.05", "teaches": ["azert", "onfelaldozas"], "prompt": "Rakd össze a célhatározói mondatot!", "chips": ["Azért", "harcoltak,", "hogy", "megállítsák", "a", "török", "sereget."], "target": "Azért harcoltak, hogy megállítsák a török sereget.", "english": "They fought in order to stop the Turkish army."},
    {"id": "ex.b1.haromresz.05.04", "type": "multiple-choice", "lesson": "lesson.b1.haromresz.05", "teaches": ["Szulejman-halala"], "prompt": "Melyik híres uralkodó halt meg Szigetvár ostroma alatt a táborban?", "options": ["I. Szulejmán szultán", "Habsburg Ferdinánd", "Mátyás király", "II. Lajos"], "correctIndex": 0, "explanation": "I. Szulejmán szultán az ostrom utolsó napjaiban hunyt el Szigetvár alatt."},
    {"id": "ex.b1.haromresz.05.05", "type": "fill-blank", "lesson": "lesson.b1.haromresz.05", "teaches": ["feltartoztat"], "prompt": "Egészítsd ki a mondatot a megfelelő igealakkal!", "sentence": "A szigetvári védők hetekre *feltartóztatták* a szultáni fősereget.", "target": "feltartóztatták"},
    {"id": "ex.b1.haromresz.05.06", "type": "sentence-builder", "lesson": "lesson.b1.haromresz.05", "teaches": ["martir", "onfelaldozas"], "prompt": "Alkoss szabályos mondatot!", "chips": ["Zrínyi", "a", "keresztény", "világ", "mártírjaként", "halt", "meg."], "target": "Zrínyi a keresztény világ mártírjaként halt meg.", "english": "Zrínyi died as a martyr of the Christian world."},
    {"id": "ex.b1.haromresz.05.07", "type": "multiple-choice", "lesson": "lesson.b1.haromresz.05", "teaches": ["Zrinyi-Miklos"], "prompt": "Milyen nemzetiségű vitézek harcoltak együtt Zrínyi oldalán Szigetváron?", "options": ["Magyarok és horvátok", "Angolok és spanyolok", "Oroszok és lengyelek", "Csak külföldi zsoldosok"], "correctIndex": 0, "explanation": "Zrínyi Miklós vezetése alatt magyar és horvát vitézek harcoltak együtt."},
    {"id": "ex.b1.haromresz.05.08", "type": "fill-blank", "lesson": "lesson.b1.haromresz.05", "teaches": ["onfelaldozas"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A védők példátlan *önfeláldozása* megmentette Bécset az ostromtól.", "target": "önfeláldozása"}
]
write_json(EXERCISES_DIR / "ex.b1.haromresz.05.json", make_exercise_group("ex.b1.haromresz.05", "Szigetvár ostroma gyakorlatok", "Gyakorlatok Zrínyi Miklós önfeláldozásáról és a célhatározói mondatokról.", exs_5))

lesson_5 = make_lesson(
    "lesson.b1.haromresz.05",
    "Szigetvár ostroma és Zrínyi Miklós kirohanása (1566)",
    "Célhatározói összetett mondatok (azért, hogy, abból a célból)",
    "Részletesen feldolgozzuk Szigetvár 1566-os ostromát, Szulejmán szultán halálát és Zrínyi Miklós hősies kirohanását.",
    ["Megérteni az 1566-os szigetvári ostrom lefolyását", "Használni a célhatározói kötőszókat felszólító móddal", "Ismerni Zrínyi Miklós történelmi és erkölcsi örökségét"],
    "story.b1.haromresz.05",
    "voc.b1.haromresz.05",
    "gr.b1.haromresz.05",
    "ex.b1.haromresz.05",
    [e["id"] for e in exs_5]
)
write_json(LESSONS_DIR / "lesson.b1.haromresz.05.json", lesson_5)


# ==========================================
# CONSOLIDATION LESSON: b1-haromresz-consolidation
# ==========================================
cons_exs = [
    {"id": "ex.b1.haromresz.cons.01", "type": "multiple-choice", "lesson": "lesson.b1.haromresz.consolidation", "teaches": ["Buda-1541"], "prompt": "Melyik évben került Buda vára török kézre?", "options": ["1541-ben", "1526-ban", "1552-ben", "1566-ban"], "correctIndex": 0, "explanation": "Buda 1541. augusztus 29-én esett el."},
    {"id": "ex.b1.haromresz.cons.02", "type": "fill-blank", "lesson": "lesson.b1.haromresz.consolidation", "teaches": ["csel"], "prompt": "Szulejmán szultán katonai *csellel* foglalta el Budát 1541-ben.", "sentence": "Szulejmán szultán katonai *csellel* foglalta el Budát 1541-ben.", "target": "csellel"},
    {"id": "ex.b1.haromresz.cons.03", "type": "multiple-choice", "lesson": "lesson.b1.haromresz.consolidation", "teaches": ["harom-resz"], "prompt": "Hány országrészre szakadt a történelmi Magyarország 1541 után?", "options": ["Három részre (Királyi Mo., Hódoltság, Erdély)", "Két részre", "Négy részre", "Nem szakadt részekre"], "correctIndex": 0, "explanation": "Magyarország három részre szakadt: Királyi Magyarország, Török Hódoltság és Erdélyi Fejedelemség."},
    {"id": "ex.b1.haromresz.cons.04", "type": "fill-blank", "lesson": "lesson.b1.haromresz.consolidation", "teaches": ["Pozsony"], "prompt": "A Királyi Magyarország fővárosa és koronázóvárosa *Pozsony* lett.", "sentence": "A Királyi Magyarország fővárosa és koronázóvárosa *Pozsony* lett.", "target": "Pozsony"},
    {"id": "ex.b1.haromresz.cons.05", "type": "sentence-builder", "lesson": "lesson.b1.haromresz.cons", "teaches": ["mig", "Erdely"], "prompt": "Rakd össze az összehasonlító mondatot!", "chips": ["Míg", "Buda", "török", "lett,", "addig", "Erdély", "önálló", "maradt."], "target": "Míg Buda török lett, addig Erdély önálló maradt.", "english": "While Buda became Turkish, Transylvania remained autonomous."},
    {"id": "ex.b1.haromresz.cons.06", "type": "multiple-choice", "lesson": "lesson.b1.haromresz.consolidation", "teaches": ["kettos-adoztatas"], "prompt": "Mit jelent a hódoltsági jobbágyok 'kettős adóztatása'?", "options": ["Adót fizettek a török szpáhシャル és a magyar földesúrnak is", "Két különböző pénznemben fizettek", "Minden évben kétszer szedték be az adót", "Csak a tizedet fizették meg"], "correctIndex": 0, "explanation": "A peremvidék parasztjai a török hatóságoknak és a magyar nemeseknek is adóztak."},
    {"id": "ex.b1.haromresz.cons.07", "type": "fill-blank", "lesson": "lesson.b1.haromresz.consolidation", "teaches": ["portyazas"], "prompt": "A végvári vitézek állandó *portyázásokkal* zavarták a hódítókat.", "sentence": "A végvári vitézek állandó *portyázásokkal* zavarták a hódítókat.", "target": "portyázásokkal"},
    {"id": "ex.b1.haromresz.cons.08", "type": "sentence-builder", "lesson": "lesson.b1.haromresz.consolidation", "teaches": ["bajvivas", "vitezek"], "prompt": "Rakd össze a mondatot!", "chips": ["A", "vitézek", "bajvívásokon", "mutatták", "meg", "bátorságukat."], "target": "A vitézek bajvívásokon mutatták meg bátorságukat.", "english": "The warriors demonstrated their courage in single combat."},
    {"id": "ex.b1.haromresz.cons.09", "type": "multiple-choice", "lesson": "lesson.b1.haromresz.consolidation", "teaches": ["Eger-1552"], "prompt": "Melyik vár védői arattak történelmi győzelmet 1552-ben?", "options": ["Eger várvédői Dobó István vezetésével", "Szigetvár védői", "Buda védői", "Nándorfehérvár védői"], "correctIndex": 0, "explanation": "1552-ben Dobó István vezetésével Eger megállította a török fősereget."},
    {"id": "ex.b1.haromresz.cons.10", "type": "fill-blank", "lesson": "lesson.b1.haromresz.consolidation", "teaches": ["Dobo-Istvan"], "prompt": "Az egri vár hős kapitánya *Dobó István* volt az 1552-es ostromban.", "sentence": "Az egri vár hős kapitánya *Dobó István* volt az 1552-es ostromban.", "target": "Dobó István"},
    {"id": "ex.b1.haromresz.cons.11", "type": "sentence-builder", "lesson": "lesson.b1.haromresz.consolidation", "teaches": ["bar", "diadal"], "prompt": "Alkoss megengedő mondatot!", "chips": ["Bár", "kevesen", "voltak,", "az", "egriek", "győztek."], "target": "Bár kevesen voltak, az egriek győztek.", "english": "Although they were few, the people of Eger won."},
    {"id": "ex.b1.haromresz.cons.12", "type": "multiple-choice", "lesson": "lesson.b1.haromresz.consolidation", "teaches": ["Szondi-Gyorgy"], "prompt": "Ki halt hősi halált Drégely várában 1552-ben?", "options": ["Szondi György", "Bornemissza Gergely", "Zrínyi Miklós", "Tomori Pál"], "correctIndex": 0, "explanation": "Szondi György Drégely várában esett el hősként 1552-ben."},
    {"id": "ex.b1.haromresz.cons.13", "type": "fill-blank", "lesson": "lesson.b1.haromresz.consolidation", "teaches": ["egri-nok"], "prompt": "Az ostrom során az *egri nők* is forró szurokkal harcoltak a bástyákon.", "sentence": "Az ostrom során az *egri nők* is forró szurokkal harcoltak a bástyákon.", "target": "egri nők"},
    {"id": "ex.b1.haromresz.cons.14", "type": "multiple-choice", "lesson": "lesson.b1.haromresz.consolidation", "teaches": ["Szigetvar-1566"], "prompt": "Melyik évben hajtotta végre Zrínyi Miklós a szigetvári kirohanást?", "options": ["1566-ban", "1552-ben", "1541-ben", "1686-ban"], "correctIndex": 0, "explanation": "Zrínyi Miklós 1566-ban tört ki Szigetvár égő belső várából."},
    {"id": "ex.b1.haromresz.cons.15", "type": "fill-blank", "lesson": "lesson.b1.haromresz.consolidation", "teaches": ["kirohanas"], "prompt": "Zrínyi Miklós és háromszáz vitéze a végső *kirohanásban* esett el.", "sentence": "Zrínyi Miklós és háromszáz vitéze a végső *kirohanásban* esett el.", "target": "kirohanásban"},
    {"id": "ex.b1.haromresz.cons.16", "type": "sentence-builder", "lesson": "lesson.b1.haromresz.consolidation", "teaches": ["azert", "onfelaldozas"], "prompt": "Rakd össze a célhatározói mondatot!", "chips": ["Azért", "haltak", "meg,", "hogy", "megvédjék", "a", "hazát."], "target": "Azért haltak meg, hogy megvédjék a hazát.", "english": "They died in order to protect the homeland."},
    {"id": "ex.b1.haromresz.cons.17", "type": "multiple-choice", "lesson": "lesson.b1.haromresz.consolidation", "teaches": ["vilajet"], "prompt": "Ki állt a török hódoltsági vilajet élén?", "options": ["A pasa", "A fejedelem", "A nádor", "A várispán"], "correctIndex": 0, "explanation": "A vilajetet a pasa irányította (például a budai pasa)."},
    {"id": "ex.b1.haromresz.cons.18", "type": "fill-blank", "lesson": "lesson.b1.haromresz.consolidation", "teaches": ["onallosag"], "prompt": "Erdély megőrizte belső *önállóságát* a hódoltság évszázadai alatt.", "sentence": "Erdély megőrizte belső *önállóságát* a hódoltság évszázadai alatt.", "target": "önállóságát"},
    {"id": "ex.b1.haromresz.cons.19", "type": "sentence-builder", "lesson": "lesson.b1.haromresz.consolidation", "teaches": ["szemben", "hodoltsag"], "prompt": "Alkoss összefüggő mondatot!", "chips": ["Szemben", "a", "Hódoltsággal,", "a", "Királyi", "Magyarország", "nyugathoz", "tartozott."], "target": "Szemben a Hódoltsággal, a Királyi Magyarország nyugathoz tartozott.", "english": "In contrast to the Ottoman domain, Royal Hungary belonged to the West."},
    {"id": "ex.b1.haromresz.cons.20", "type": "multiple-choice", "lesson": "lesson.b1.haromresz.consolidation", "teaches": ["Szulejman-halala"], "prompt": "Melyik magyar vár ostrománál halt meg I. Szulejmán szultán?", "options": ["Szigetvárnál", "Egernél", "Budánál", "Nándorfehérvárnál"], "correctIndex": 0, "explanation": "I. Szulejmán szultán Szigetvár ostroma alatt halt meg a táborban 1566-ban."}
]
write_json(EXERCISES_DIR / "ex.b1.haromresz.consolidation.json", make_exercise_group("ex.b1.haromresz.consolidation", "A három részre szakadt Magyarország összefoglaló gyakorlatok", "Átfogó teszt az 1541–1566 közötti korszak eseményeiről és nyelvtani szerkezeteiről.", cons_exs))

cons_lesson = {
    "id": "lesson.b1.haromresz.consolidation",
    "title": "Three Parts of Hungary: Unit 10 Consolidation",
    "level": "B1",
    "track": "citizenship",
    "estimatedMinutes": 25,
    "prerequisites": [
        "lesson.b1.haromresz.01",
        "lesson.b1.haromresz.02",
        "lesson.b1.haromresz.03",
        "lesson.b1.haromresz.04",
        "lesson.b1.haromresz.05"
    ],
    "grammar": ["Unit review"],
    "vocabulary": ["Unit review"],
    "culturalContext": "Magyar történelem összefoglalás (Honosítási vizsgafelkészítő)",
    "sections": [
        {
            "type": "intro",
            "title": "Unit 10 Consolidation: Three Parts of Hungary (1541–1686)",
            "body": "Ebben az összefoglaló leckében áttekintjük Buda 1541-es elestét, a három országrész berendezkedését, a végvári harcokat, valamint 1552 (Eger, Drégely) és 1566 (Szigetvár) hősi küzdelmeit."
        },
        {
            "type": "goal",
            "title": "Consolidation Goals",
            "items": [
                "A három országrész politikai és földrajzi felosztásának pontos ismerete",
                "Összehasonlító (míg... addig), megengedő (bár, jóllehet) és célhatározói mondatok helyes használata",
                "Az 1552-es egri diadal és az 1566-os szigetvári önfeláldozás kulcsfogalmainak magabiztos alkalmazása"
            ]
        },
        {
            "type": "exercise-group",
            "title": "Comprehensive Unit 10 Practice",
            "ref": "ex.b1.haromresz.consolidation",
            "exerciseRefs": [e["id"] for e in cons_exs]
        },
        {
            "type": "checklist",
            "items": [
                "Tudom, mikor esett el Buda (1541. augusztus 29.)",
                "Meg tudom nevezni a három országrészt (Királyi Mo., Hódoltság, Erdély)",
                "Ismerem Dobó István (1552, Eger) és Zrínyi Miklós (1566, Szigetvár) tetteit",
                "Értem a kettős adóztatás és a végvári élet jelentőségét"
            ]
        }
    ]
}
write_json(LESSONS_DIR / "lesson.b1.haromresz.consolidation.json", cons_lesson)

print("Unit 10 (b1-haromresz) complete!")
