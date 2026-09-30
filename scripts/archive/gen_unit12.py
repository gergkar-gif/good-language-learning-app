# -*- coding: utf-8 -*-
"""
Full Unit 12 Overhaul: Driving Out the Ottomans (b1-torokkiuzese)
Lessons:
1. Zrínyi Miklós, a költő és hadvezér (1664-es téli hadjárat, vasvári béke)
2. Bécs ostroma (1683) és a Szent Liga megalakulása (1684)
3. Buda visszafoglalása (1686. szeptember 2.)
4. A felszabadító háborúk és a karlócai béke (1699)
5. Az újszerzeményi politika és az új feszültségek kibontakozása
Consolidation: Unit 12 Capstone (20 exercises)
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
# LESSON 1: b1-torokkiuzese-01 (Zrínyi Miklós, a hadvezér és költő)
# ==========================================
story_1 = make_story(
    "story.b1.torokkiuzese.01",
    "Zrínyi Miklós, a költő és hadvezér (1664-es téli hadjárat)",
    "A szigetvári hős dédunokája, Zrínyi Miklós hadtudományi írásaival és a híres 1664-es téli hadjárattal hívta fel a figyelmet a törökök kiűzésének szükségességére.",
    "Csáktornya és az eszéki híd",
    ["Complex cause-effect and adversative connectors (annak ellenére, hogy, következtében)", "Military and intellectual leadership"],
    ["Zrínyi Miklós", "téli hadjárat", "eszéki híd", "vasvári béke", "hadtudomány"],
    [
        "A 17. század derekán gróf Zrínyi Miklós, a költő és hadvezér ismerte fel elsőként, hogy a török hódoltság felszámolásához önálló magyar nemzeti hadseregre és európai összefogásra van szükség. Híres politikai röpiratában, a 'Török áfium ellen való orvosságban' fogalmazta meg jelmondatát: 'Ne bántsd a magyart!'.",
        "1664 telén Zrínyi zseniális téli hadjáratot vezetett: seregével mélyen benyomult a hódoltság területére, és felégette a török utánpótlást biztosító hat kilométer hosszú, fából ácsolt eszéki hidat a Dráván. Tette Európa-szerte óriási hírnevet és elismerést szerzett neki.",
        "Annak ellenére, hogy a keresztény erők a szentgotthárdi csatában is fényes győzelmet arattak, I. Lipót császár a magyarok megkérdezése nélkül megkötötte a szégyenteljes vasvári békét, amely török kézen hagyta a korábban elfoglalt területeket. Ebből kifolyólag hatalmas elkeseredés és felháborodás tört ki a magyar nemesség körében."
    ],
    [
        {"lemma": "hadvezér", "pos": "noun", "cefr": "B1", "gloss": "military commander, general"},
        {"lemma": "utánpótlás", "pos": "noun", "cefr": "B1", "gloss": "reinforcement, supply line"},
        {"lemma": "felháborodás", "pos": "noun", "cefr": "B1", "gloss": "indignation, outrage"},
        {"lemma": "röpirat", "pos": "noun", "cefr": "B1", "gloss": "political pamphlet, tract"},
        {"lemma": "elkeseredés", "pos": "noun", "cefr": "B1", "gloss": "bitterness, despair"}
    ],
    [
        {
            "question": "Mit hajtott végre Zrínyi Miklós az 1664-es téli hadjáratban?",
            "options": ["Felégette a török hadsereg kulcsfontosságú eszéki hídját a Dráván", "Visszafoglalta Budát a törököktől", "Megkoronázta saját magát királlyá", "Békét kötött a szultánnal Isztambulban"],
            "correctIndex": 0,
            "explanation": "Zrínyi 1664 telén felégette az eszéki hidat, elvágva a török utánpótlást."
        }
    ]
)
write_json(STORIES_DIR / "story.b1.torokkiuzese.01.json", story_1)

voc_1 = {
    "id": "voc.b1.torokkiuzese.01",
    "title": "A 17. századi hadművészet és ellenállás szókincse",
    "description": "Hadvezér, utánpótlás, politikai röpirat, felháborodás és haditaktika.",
    "entries": [
        {"lemma": "hadvezér", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "military commander, general", "examples": [{"hu": "Zrínyi Miklós kiemelkedő hadvezér és költő volt.", "en": "Miklós Zrínyi was an outstanding commander and poet."}]}]},
        {"lemma": "utánpótlás", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "military supply, logistics reinforcement", "examples": [{"hu": "A híd felégetésével elvágták a török utánpótlást.", "en": "By burning the bridge, they cut off the Turkish supplies."}]}]},
        {"lemma": "felháborodás", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "indignation, widespread public outrage", "examples": [{"hu": "A vasvári béke országos felháborodást keltett.", "en": "The Peace of Vasvár caused nationwide outrage."}]}]},
        {"lemma": "röpirat", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "political tract, pamphlet", "examples": [{"hu": "Zrínyi röpiratában nemzeti hadsereget sürgetett.", "en": "In his pamphlet, Zrínyi urged for a national army."}]}]},
        {"lemma": "elkeseredés", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "bitter resentment, despair", "examples": [{"hu": "A békekötés után mély elkeseredés uralkodott el.", "en": "After the peace conclusion, deep bitterness took hold."}]}]}
    ]
}
write_json(VOCAB_DIR / "voc.b1.torokkiuzese.01.json", voc_1)

gr_1 = {
    "id": "gr.b1.torokkiuzese.01",
    "title": "Összetett ellentétes és okhatározói viszonyok (annak ellenére, hogy, következtében)",
    "description": "Expressing political paradoxes and historical cause-effect chains.",
    "rules": [
        "Az 'annak ellenére, hogy' szerkezet határozott ellentétet, paradoxont mutat be (egy győzelem ellenére kedvezőtlen békekötés).",
        "A 'következtében' névutó egy esemény közvetlen történelmi eredményét fejezi ki."
    ],
    "tables": [
        {"headers": ["Kifejezés", "Jelentés", "Példa"], "rows": [
            ["annak ellenére, hogy", "in spite of the fact that", "Annak ellenére, hogy győztek, békét kötöttek."],
            ["következtében", "as a result of", "A felháborodás következtében ellenállás indult."]
        ]}
    ],
    "examples": [
        {"spanish": "Annak ellenére, hogy a keresztény hadak győztek Szentgotthárdnál, a béke megalázó volt.", "english": "In spite of the fact that Christian forces won at Szentgotthárd, the peace was humiliating."},
        {"spanish": "A hadjárat sikerének következtében Zrínyi neve egész Európában ismertté vált.", "english": "As a consequence of the campaign's success, Zrínyi's name became known across Europe."},
        {"spanish": "A vasvári béke megkötése következtében felkelések kezdődtek.", "english": "As a result of concluding the Peace of Vasvár, uprisings began."}
    ]
}
write_json(GRAMMAR_DIR / "gr.b1.torokkiuzese.01.json", gr_1)

exs_1 = [
    {"id": "ex.b1.torokkiuzese.01.01", "type": "multiple-choice", "lesson": "lesson.b1.torokkiuzese.01", "teaches": ["Zrinyi-Miklos-1664"], "prompt": "Melyik híres haditett fűződik Zrínyi Miklós nevéhez 1664 telén?", "options": ["Az eszéki híd felégetése a téli hadjáratban", "Nándorfehérvár megvédése", "Buda visszafoglalása", "A pozsonyi országgyűlés összehívása"], "correctIndex": 0, "explanation": "Zrínyi az 1664-es téli hadjáratban égette fel a stratégiai eszéki Dráva-hidat."},
    {"id": "ex.b1.torokkiuzese.01.02", "type": "fill-blank", "lesson": "lesson.b1.torokkiuzese.01", "teaches": ["hadvezer"], "prompt": "Egészítsd ki a mondatot!", "sentence": "Zrínyi Miklós nemcsak költő, hanem kiváló *hadvezér* is volt.", "target": "hadvezér"},
    {"id": "ex.b1.torokkiuzese.01.03", "type": "sentence-builder", "lesson": "lesson.b1.torokkiuzese.01", "teaches": ["annak", "ellenere"], "prompt": "Rakd össze az ellentétes mondatot!", "chips": ["Annak", "ellenére,", "hogy", "győztek,", "rossz", "békét", "kötöttek."], "target": "Annak ellenére, hogy győztek, rossz békét kötöttek.", "english": "In spite of the fact that they won, they concluded a bad peace."},
    {"id": "ex.b1.torokkiuzese.01.04", "type": "multiple-choice", "lesson": "lesson.b1.torokkiuzese.01", "teaches": ["vasvari-beke"], "prompt": "Miért váltott ki felháborodást az 1664-es vasvári béke?", "options": ["Mert a győzelem ellenére török kézen hagyta a magyar várakat", "Mert a császár elvette a koronát", "Mert új adót vezettek be a nemesekre", "Mert elmaradt a bányászat"], "correctIndex": 0, "explanation": "A vasvári béke a szentgotthárdi keresztény győzelem ellenére a törököknek kedvezett."},
    {"id": "ex.b1.torokkiuzese.01.05", "type": "fill-blank", "lesson": "lesson.b1.torokkiuzese.01", "teaches": ["felhaborodas"], "prompt": "Egészítsd ki a mondatot a megfelelő szóval!", "sentence": "A megalázó békeszerződés hatalmas *felháborodást* váltott ki.", "target": "felháborodást"},
    {"id": "ex.b1.torokkiuzese.01.06", "type": "sentence-builder", "lesson": "lesson.b1.torokkiuzese.01", "teaches": ["kovetkezteben", "elkeseredes"], "prompt": "Alkoss okhatározói mondatot!", "chips": ["A", "döntés", "következtében", "mély", "elkeseredés", "lett", "úrrá."], "target": "A döntés következtében mély elkeseredés lett úrrá.", "english": "As a result of the decision, deep bitterness took hold."},
    {"id": "ex.b1.torokkiuzese.01.07", "type": "multiple-choice", "lesson": "lesson.b1.torokkiuzese.01", "teaches": ["Ne-bantsd-a-magyart"], "prompt": "Mi volt Zrínyi Miklós híres röpiratának jelmondata?", "options": ["'Ne bántsd a magyart!'", "'Istenért és a szabadságért!'", "'Mindent a hazáért!'", "'Életünket és vérünket!'"], "correctIndex": 0, "explanation": "A 'Ne bántsd a magyart!' (Török áfium ellen való orvosság) Zrínyi híres jelmondata."},
    {"id": "ex.b1.torokkiuzese.01.08", "type": "fill-blank", "lesson": "lesson.b1.torokkiuzese.01", "teaches": ["utanpotlas"], "prompt": "Egészítsd ki a mondatot!", "sentence": "Az eszéki híd pusztulása megakadályozta a török *utánpótlást*.", "target": "utánpótlást"}
]
write_json(EXERCISES_DIR / "ex.b1.torokkiuzese.01.json", make_exercise_group("ex.b1.torokkiuzese.01", "Zrínyi Miklós kora gyakorlatok", "Gyakorlatok Zrínyi hadművészetéről és az összetett ellentétes szerkezetekről.", exs_1))

lesson_1 = make_lesson(
    "lesson.b1.torokkiuzese.01",
    "Zrínyi Miklós, a költő és hadvezér (1664-es téli hadjárat)",
    "Összetett ellentétes és okhatározói kötőszavak (annak ellenére, hogy, következtében)",
    "Megismerjük Zrínyi Miklós 1664-es téli hadjáratát, az eszéki híd felégetését és a vasvári béke politikai utóéletét.",
    ["Megérteni Zrínyi Miklós katonai és szellemi szerepét", "Használni az 'annak ellenére, hogy' és 'következtében' szerkezeteket", "Ismerni az 1664-es eseményeket és a 'Ne bántsd a magyart!' jelmondatot"],
    "story.b1.torokkiuzese.01",
    "voc.b1.torokkiuzese.01",
    "gr.b1.torokkiuzese.01",
    "ex.b1.torokkiuzese.01",
    [e["id"] for e in exs_1]
)
write_json(LESSONS_DIR / "lesson.b1.torokkiuzese.01.json", lesson_1)


# ==========================================
# LESSON 2: b1-torokkiuzese-02 (Bécs ostroma 1683 és a Szent Liga)
# ==========================================
story_2 = make_story(
    "story.b1.torokkiuzese.02",
    "Bécs ostroma (1683) és a Szent Liga megalakulása (1684)",
    "1683-ban a török fősereg megkísérelte Bécs elfoglalását, de Sobieski János felmentő serege tönkreverte őket, megnyitva az utat Magyarország felszabadításához.",
    "Bécs és a Kahlenberg",
    ["Temporal sequencing in battle narratives (először, ezt követően, mindeközben, végül)", "European coalition diplomacy"],
    ["Bécs ostroma", "Kara Musztafa", "Sobieski János", "Szent Liga", "XI. Ince pápa"],
    [
        "1683 nyarán Kara Musztafa nagyvezír hatalmas, több mint százezres oszmán sereggel vonult Bécs falai alá, hogy bevegye a Habsburg birodalom székvárosát. Először szoros ostromgyűrűt vont a császárváros köré, és heteken át hevesen ágyúzta a védőfalakat.",
        "Mindeközben XI. Ince pápa óriási diplomáciai erőfeszítéseket tett a keresztény fejedelmek egyesítésére. Ennek eredményeként Sobieski János lengyel király és Lotharingiai Károly herceg egyesült felmentő serege a Kahlenberg magaslatairól indított elsöprő erejű lovasrohammal megsemmisítette a török ostromló tábort.",
        "Ezt követően, 1684-ben a pápa kezdeményezésére megalakult a Szent Liga, a Habsburg Birodalom, Lengyelország, a Velencei Köztársaság, majd Oroszország szövetsége. Végül megindult a koordinált, történelmi nemzetközi offenzíva Magyarország török alóli felszabadítására."
    ],
    [
        {"lemma": "ostromgyűrű", "pos": "noun", "cefr": "B1", "gloss": "siege ring, encirclement"},
        {"lemma": "felmentő sereg", "pos": "noun", "cefr": "B1", "gloss": "relief army"},
        {"lemma": "elsöprő", "pos": "adjective", "cefr": "B1", "gloss": "sweeping, overwhelming"},
        {"lemma": "offenzíva", "pos": "noun", "cefr": "B1", "gloss": "military offensive"},
        {"lemma": "koordinált", "pos": "adjective", "cefr": "B1", "gloss": "coordinated"}
    ],
    [
        {
            "question": "Ki vezette a Bécs városát megmentő lengyel felmentő sereget 1683-ban?",
            "options": ["Sobieski János lengyel király", "Lotharingiai Károly", "Zrínyi Miklós", "Savoyai Jenő"],
            "correctIndex": 0,
            "explanation": "Sobieski János lengyel király lovasrohama mentette fel Bécset 1683-ban."
        }
    ]
)
write_json(STORIES_DIR / "story.b1.torokkiuzese.02.json", story_2)

voc_2 = {
    "id": "voc.b1.torokkiuzese.02",
    "title": "A nemzetközi szövetség és ostromharc szókincse",
    "description": "Felmentő sereg, szövetségi diplomácia, ostromgyűrű és offenzíva.",
    "entries": [
        {"lemma": "ostromgyűrű", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "siege encirclement", "examples": [{"hu": "A sereg szoros ostromgyűrűt vont a vár köré.", "en": "The army threw a tight siege ring around the castle."}]}]},
        {"lemma": "felmentő sereg", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "relief force, relieving army", "examples": [{"hu": "A lengyel király felmentő serege megmentette a várost.", "en": "The Polish king's relief army saved the city."}]}]},
        {"lemma": "elsöprő", "pos": "adjective", "cefr": "B1", "definitions": [{"meaning": "sweeping, devastatingly powerful", "examples": [{"hu": "A lovasság elsöprő rohamot indított.", "en": "The cavalry launched a sweeping charge."}]}]},
        {"lemma": "offenzíva", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "military campaign, offensive", "examples": [{"hu": "A Szent Liga offenzívát indított a török ellen.", "en": "The Holy League launched an offensive against the Turks."}]}]},
        {"lemma": "szövetség", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "international alliance, coalition", "examples": [{"hu": "A pápa létrehozta a Szent Liga szövetségét.", "en": "The Pope created the Holy League alliance."}]}]}
    ]
}
write_json(VOCAB_DIR / "voc.b1.torokkiuzese.02.json", voc_2)

gr_2 = {
    "id": "gr.b1.torokkiuzese.02",
    "title": "Időrendi és folyamatjelölő szövegkapcsolók (először, ezt követően, mindeközben, végül)",
    "description": "Chronological narrative sequencing in military and historical accounts.",
    "rules": [
        "A hadtörténeti leírásokban az időrendi határozószók biztosítják a feszültséget és a logikus követhetőséget.",
        "Az 'először' az indítást, a 'mindeközben' a párhuzamos eseményt, az 'ezt követően' a következő fázist, a 'végül' a tetőpontot zárja le."
    ],
    "tables": [
        {"headers": ["Időrendi kötőelem", "Szerep", "Példa"], "rows": [
            ["először", "kezdet", "Először körülzárták a várost."],
            ["mindeközben", "párhuzamosság", "Mindeközben érkezett a felmentő sereg."],
            ["ezt követően", "következő lépés", "Ezt követően megalakult a Szent Liga."],
            ["végül", "lezárás", "Végül megkezdődött a felszabadítás."]
        ]}
    ],
    "examples": [
        {"spanish": "Először Kara Musztafa megkezdte Bécs ostromát 1683-ban.", "english": "First, Kara Mustafa began the siege of Vienna in 1683."},
        {"spanish": "Mindeközben a pápa pénzt és diplomáciai támogatást gyűjtött.", "english": "Meanwhile, the Pope gathered money and diplomatic support."},
        {"spanish": "Végül a Kahlenbergről megindult a döntő lovasroham.", "english": "Finally, the decisive cavalry charge began from the Kahlenberg."}
    ]
}
write_json(GRAMMAR_DIR / "gr.b1.torokkiuzese.02.json", gr_2)

exs_2 = [
    {"id": "ex.b1.torokkiuzese.02.01", "type": "multiple-choice", "lesson": "lesson.b1.torokkiuzese.02", "teaches": ["Becs-ostroma-1683"], "prompt": "Melyik évben zajlott le Bécs sorsdöntő török ostroma?", "options": ["1683-ban", "1526-ban", "1664-ben", "1699-ben"], "correctIndex": 0, "explanation": "Bécs ostroma 1683-ban történt."},
    {"id": "ex.b1.torokkiuzese.02.02", "type": "fill-blank", "lesson": "lesson.b1.torokkiuzese.02", "teaches": ["felmento-sereg"], "prompt": "Egészítsd ki a mondatot!", "sentence": "Sobieski János *felmentő serege* mentette meg Bécset a pusztulástól.", "target": "felmentő serege"},
    {"id": "ex.b1.torokkiuzese.02.03", "type": "sentence-builder", "lesson": "lesson.b1.torokkiuzese.02", "teaches": ["mindekozben", "szent-liga"], "prompt": "Rakd össze a mondatot helyes sorrendben!", "chips": ["Mindeközben", "a", "pápa", "megszervezte", "a", "Szent", "Ligát."], "target": "Mindeközben a pápa megszervezte a Szent Ligát.", "english": "Meanwhile, the Pope organized the Holy League."},
    {"id": "ex.b1.torokkiuzese.02.04", "type": "multiple-choice", "lesson": "lesson.b1.torokkiuzese.02", "teaches": ["Szent-Liga-1684"], "prompt": "Milyen szövetség alakult meg 1684-ben a törökök kiűzésére?", "options": ["A Szent Liga", "A Három Császár Szövetsége", "A Varsói Szerződés", "A Visegrádi Négyek"], "correctIndex": 0, "explanation": "1684-ben a pápa ösztönzésére megalakult a Szent Liga nemzetközi szövetsége."},
    {"id": "ex.b1.torokkiuzese.02.05", "type": "fill-blank", "lesson": "lesson.b1.torokkiuzese.02", "teaches": ["elsopro"], "prompt": "Egészítsd ki a mondatot a megfelelő melléknévvel!", "sentence": "A lengyel lovasság *elsöprő* rohammal verte szét a török tábort.", "target": "elsöprő"},
    {"id": "ex.b1.torokkiuzese.02.06", "type": "sentence-builder", "lesson": "lesson.b1.torokkiuzese.02", "teaches": ["vegul", "offenziva"], "prompt": "Alkoss összefüggő záró mondatot!", "chips": ["Végül", "megindult", "a", "felszabadító", "offenzíva", "Magyarországon."], "target": "Végül megindult a felszabadító offenzíva Magyarországon.", "english": "Finally, the liberating offensive began in Hungary."},
    {"id": "ex.b1.torokkiuzese.02.07", "type": "multiple-choice", "lesson": "lesson.b1.torokkiuzese.02", "teaches": ["XI-Ince-papa"], "prompt": "Melyik pápa játszott döntő szerepet a Szent Liga létrehozásában?", "options": ["XI. Ince pápa", "III. Ince pápa", "II. Piusz pápa", "VII. Gergely pápa"], "correctIndex": 0, "explanation": "XI. Ince pápa volt a keresztény szövetség fő diplomáciai és pénzügyi támogatója."},
    {"id": "ex.b1.torokkiuzese.02.08", "type": "fill-blank", "lesson": "lesson.b1.torokkiuzese.02", "teaches": ["ostromgyuru"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A felmentő csapatok áttörték a várost fojtogató *ostromgyűrűt*.", "target": "ostromgyűrűt"}
]
write_json(EXERCISES_DIR / "ex.b1.torokkiuzese.02.json", make_exercise_group("ex.b1.torokkiuzese.02", "Bécs ostroma és a Szent Liga gyakorlatok", "Gyakorlatok az 1683-as felmentésről és az időrendi szövegkapcsolókról.", exs_2))

lesson_2 = make_lesson(
    "lesson.b1.torokkiuzese.02",
    "Bécs ostroma (1683) és a Szent Liga megalakulása (1684)",
    "Időrendi és folyamatjelölő szövegkapcsolók (mindeközben, ezt követően, végül)",
    "Részletesen megismerjük Bécs 1683-as ostromát, Sobieski János felmentő hadjáratát és a Szent Liga 1684-es megalakulását.",
    ["Megérteni Bécs 1683-as megmentésének jelentőségét", "Használni az időrendi és folyamatjelölő kötőszavakat", "Ismerni a Szent Liga létrejöttét és XI. Ince pápa szerepét"],
    "story.b1.torokkiuzese.02",
    "voc.b1.torokkiuzese.02",
    "gr.b1.torokkiuzese.02",
    "ex.b1.torokkiuzese.02",
    [e["id"] for e in exs_2]
)
write_json(LESSONS_DIR / "lesson.b1.torokkiuzese.02.json", lesson_2)


# ==========================================
# LESSON 3: b1-torokkiuzese-03 (Buda visszafoglalása 1686)
# ==========================================
story_3 = make_story(
    "story.b1.torokkiuzese.03",
    "Buda visszafoglalása (1686. szeptember 2.)",
    "1686. szeptember 2-án a nemzetközi keresztény haderő véres ostromban visszafoglalta Budát, véget vetve a 145 éves török uralomnak a fővárosban.",
    "Buda vára és a Várnegyed",
    ["Spatial locatives and military descriptions (falakon kívül/belül, mentén, körös-körül)", "Epic siege narratives"],
    ["Buda visszafoglalása", "Lotharingiai Károly", "Abdurrahman pasa", "Petneházy Dávid", "keresztény sereg"],
    [
        "1686 nyarán Lotharingiai Károly herceg és Miksa Emánuel bajor választófejedelem vezetésével mintegy nyolcvanezer fős nemzetközi keresztény sereg – köztük tizenötezer magyar vitéz – vette ostrom alá a budai várat. A várat a hetvenéves Abdurrahman pasa védte elszántan mintegy tízezer janicsárral és szpáhival.",
        "A falakon kívül felállított ágyúk hetekig lőtték a bástyákat, miközben a Duna mentén és a hegyoldalakon körös-körül véres rohamok követték egymást. Júliusban a lőportorony robbanása romba döntötte a vár belső épületeinek jelentős részét.",
        "1686. szeptember 2-án délután megindult a mindent eldöntő végső roham. Petneházy Dávid és Fiáth János magyar vitézek elsőként tűzték ki a keresztény zászlót a várfalra, míg Abdurrahman pasa a harc sűrűjében hősi halált halt. 145 év oszmán megszállás után Buda ismét felszabadult, és a hírre Európa összes harangja megkondult."
    ],
    [
        {"lemma": "visszafoglalás", "pos": "noun", "cefr": "B1", "gloss": "recapture, retaking"},
        {"lemma": "lőportorony", "pos": "noun", "cefr": "B1", "gloss": "gunpowder tower / magazine"},
        {"lemma": "zászló", "pos": "noun", "cefr": "B1", "gloss": "banner, flag"},
        {"lemma": "megszállás", "pos": "noun", "cefr": "B1", "gloss": "occupation"},
        {"lemma": "felszabadul", "pos": "verb", "cefr": "B1", "gloss": "to be liberated, freed"}
    ],
    [
        {
            "question": "Mikor foglalta vissza a keresztény sereg Buda várát a törököktől?",
            "options": ["1686. szeptember 2-án", "1541. augusztus 29-én", "1526. augusztus 29-én", "1699. január 26-án"],
            "correctIndex": 0,
            "explanation": "Buda visszafoglalása 1686. szeptember 2-án történt meg, 145 év hódoltság után."
        }
    ]
)
write_json(STORIES_DIR / "story.b1.torokkiuzese.03.json", story_3)

voc_3 = {
    "id": "voc.b1.torokkiuzese.03",
    "title": "Buda visszafoglalásának szókincse",
    "description": "Visszafoglalás, lőportorony, zászlótűzés, megszállás és felszabadulás.",
    "entries": [
        {"lemma": "visszafoglalás", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "recapture, retaking of fortress/city", "examples": [{"hu": "Buda visszafoglalása 1686-ban világraszóló siker volt.", "en": "The recapture of Buda in 1686 was a world-famous success."}]}]},
        {"lemma": "lőportorony", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "gunpowder magazine tower", "examples": [{"hu": "A budai lőportorony felrobbanása romba döntötte a palotát.", "en": "The explosion of the Buda powder magazine reduced the palace to ruins."}]}]},
        {"lemma": "zászló", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "flag, military standard", "examples": [{"hu": "A magyar vitézek kitűzték a keresztény zászlót a bástyára.", "en": "The Hungarian warriors planted the Christian flag on the bastion."}]}]},
        {"lemma": "megszállás", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "foreign military occupation", "examples": [{"hu": "Véget ért a 145 éves török megszállás Budán.", "en": "The 145-year Turkish occupation ended in Buda."}]}]},
        {"lemma": "felszabadul", "pos": "verb", "cefr": "B1", "definitions": [{"meaning": "to be liberated from enemy rule", "examples": [{"hu": "1686-ban Buda vára felszabadult.", "en": "In 1686, the castle of Buda was liberated."}]}]}
    ]
}
write_json(VOCAB_DIR / "voc.b1.torokkiuzese.03.json", voc_3)

gr_3 = {
    "id": "gr.b1.torokkiuzese.03",
    "title": "Helyhatározói viszonyok a csataleírásokban (falakon belül/kívül, mentén, körös-körül)",
    "description": "Spatial prepositions and postpositions in descriptive siege reporting.",
    "rules": [
        "A helyhatározói névutók ('belül', 'kívül', 'mentén', 'körös-körül') pontos térbeli tájékozódást adnak az ostromok leírásában.",
        "A birtokos személyjellel ellátott névutók (falakon kívül, a folyó mentén) megkívánják a határozott névelőt."
    ],
    "tables": [
        {"headers": ["Névutó / Kifejezés", "Irány / Hely", "Példa"], "rows": [
            ["falakon kívül / belül", "külső / belső tér", "A falakon kívül dörögtek az ágyúk."],
            ["mentén", "vonal mentén", "A Duna mentén vonultak a csapatok."],
            ["körös-körül", "minden irányban", "Körös-körül lángokban állt a vár."]
        ]}
    ],
    "examples": [
        {"spanish": "A falakon kívül állomásozó tüzérség heteken át lőtte a bástyákat.", "english": "The artillery stationed outside the walls shelled the bastions for weeks."},
        {"spanish": "A Duna mentén magyar hajdúk zárták el a török hajók útját.", "english": "Along the Danube, Hungarian Hajdús blocked the passage of Turkish boats."},
        {"spanish": "A budai vár körös-körül rommá dőlt az ostrom végére.", "english": "The castle of Buda lay all around in ruins by the end of the siege."}
    ]
}
write_json(GRAMMAR_DIR / "gr.b1.torokkiuzese.03.json", gr_3)

exs_3 = [
    {"id": "ex.b1.torokkiuzese.03.01", "type": "multiple-choice", "lesson": "lesson.b1.torokkiuzese.03", "teaches": ["Buda-1686"], "prompt": "Melyik évben és napon foglalták vissza Budát a törököktől?", "options": ["1686. szeptember 2-án", "1541. augusztus 29-én", "1526. augusztus 29-én", "1703. május 12-én"], "correctIndex": 0, "explanation": "Buda 1686. szeptember 2-án szabadult fel a 145 éves török uralom alól."},
    {"id": "ex.b1.torokkiuzese.03.02", "type": "fill-blank", "lesson": "lesson.b1.torokkiuzese.03", "teaches": ["visszafoglalas"], "prompt": "Egészítsd ki a mondatot!", "sentence": "Buda *visszafoglalása* történelmi fordulópontot jelentett.", "target": "visszafoglalása"},
    {"id": "ex.b1.torokkiuzese.03.03", "type": "sentence-builder", "lesson": "lesson.b1.torokkiuzese.03", "teaches": ["falakon-kivul", "agyuk"], "prompt": "Rakd össze a helyhatározói mondatot!", "chips": ["A", "falakon", "kívül", "ágyúk", "lőtték", "a", "bástyákat."], "target": "A falakon kívül ágyúk lőtték a bástyákat.", "english": "Outside the walls, cannons were shelling the bastions."},
    {"id": "ex.b1.torokkiuzese.03.04", "type": "multiple-choice", "lesson": "lesson.b1.torokkiuzese.03", "teaches": ["Lotharingiai-Karoly"], "prompt": "Ki volt a Budát ostromló keresztény fősereg főparancsnoka?", "options": ["Lotharingiai Károly herceg", "Zrínyi Miklós", "Hunyadi János", "Kinizsi Pál"], "correctIndex": 0, "explanation": "Lotharingiai Károly vezette a keresztény haderőt az 1686-os ostromban."},
    {"id": "ex.b1.torokkiuzese.03.05", "type": "fill-blank", "lesson": "lesson.b1.torokkiuzese.03", "teaches": ["zaszlo"], "prompt": "Egészítsd ki a mondatot a megfelelő szóval!", "sentence": "A bátor vitézek kitűzték a keresztény *zászlót* a várfalra.", "target": "zászlót"},
    {"id": "ex.b1.torokkiuzese.03.06", "type": "sentence-builder", "lesson": "lesson.b1.torokkiuzese.03", "teaches": ["felszabadul", "Buda"], "prompt": "Alkoss történelmi mondatot helyes sorrendben!", "chips": ["Száznegyvenöt", "év", "után", "Buda", "végleg", "felszabadult."], "target": "Száznegyvenöt év után Buda végleg felszabadult.", "english": "After 145 years, Buda was finally liberated."},
    {"id": "ex.b1.torokkiuzese.03.07", "type": "multiple-choice", "lesson": "lesson.b1.torokkiuzese.03", "teaches": ["Abdurrahman-pasa"], "prompt": "Ki volt az utolsó budai török pasa, aki a roham alatt elesett?", "options": ["Abdurrahman pasa", "Gül Baba", "Kara Musztafa", "Ali pasa"], "correctIndex": 0, "explanation": "Abdurrahman pasa volt az utolsó budai beglerbég, aki katonái élén halt meg a várfalon."},
    {"id": "ex.b1.torokkiuzese.03.08", "type": "fill-blank", "lesson": "lesson.b1.torokkiuzese.03", "teaches": ["megszallas"], "prompt": "Egészítsd ki a mondatot!", "sentence": "Véget ért a másfél évszázados oszmán *megszállás*.", "target": "megszállás"}
]
write_json(EXERCISES_DIR / "ex.b1.torokkiuzese.03.json", make_exercise_group("ex.b1.torokkiuzese.03", "Buda visszafoglalása gyakorlatok", "Gyakorlatok az 1686-os ostromról és a helyhatározói szerkezetekről.", exs_3))

lesson_3 = make_lesson(
    "lesson.b1.torokkiuzese.03",
    "Buda visszafoglalása (1686. szeptember 2.)",
    "Helyhatározói viszonyok (falakon kívül/belül, mentén, körös-körül)",
    "Feldolgozzuk Buda 1686-os ostromának lefolyását, Lotharingiai Károly hadvezetését és a 145 éves török uralom végét.",
    ["Megérteni az 1686. szeptember 2-i felszabadulás jelentőségét", "Használni a helyhatározói névutókat összetett mondatokban", "Ismerni Lotharingiai Károly és Petneházy Dávid nevét"],
    "story.b1.torokkiuzese.03",
    "voc.b1.torokkiuzese.03",
    "gr.b1.torokkiuzese.03",
    "ex.b1.torokkiuzese.03",
    [e["id"] for e in exs_3]
)
write_json(LESSONS_DIR / "lesson.b1.torokkiuzese.03.json", lesson_3)


# ==========================================
# LESSON 4: b1-torokkiuzese-04 (A karlócai béke 1699)
# ==========================================
story_4 = make_story(
    "story.b1.torokkiuzese.04",
    "A felszabadító háborúk és a karlócai béke (1699)",
    "Savoyai Jenő zentai döntő győzelme után az 1699-es karlócai békével végleg lezárult a török hódoltság kora Magyarországon.",
    "Zenta és Karlóca",
    ["Retrospective conditional structures (ha nem lett volna, akkor... lett volna)", "Peace treaties and territorial restoration"],
    ["karlócai béke", "Savoyai Jenő", "zentai csata", "felszabadítás", "Temesköz"],
    [
        "Buda visszafoglalása után a Szent Liga csapatai sorra szabadították fel a magyar várakat és városokat: Pécset, Székesfehérvárt, Egert és Váradot. A török hadsereg 1687-ben a 'második mohácsi csatában' (Nagyharsánynál) újabb súlyos vereséget szenvedett.",
        "A háborút a korszak zseniális ifjú hadvezére, Savoyai Jenő herceg döntötte el 1697-ben a zentai csatában. Jenő herceg csapatai a Tisza átkelőhelyén rajtaütöttek a szultán seregén, és megsemmisítő csapást mértek az oszmán erőkre, ami azonnali békekötésre kényszerítette Isztambult.",
        "1699-ben megkötötték a történelmi karlócai békét. Ennek értelmében a Temesköz (Bánság) kivételével a történelmi Magyarország egész területe és Erdély végleg felszabadult az Oszmán Birodalom uralma alól, lezárva a 150 éves török hódoltság korszakát."
    ],
    [
        {"lemma": "felszabadítás", "pos": "noun", "cefr": "B1", "gloss": "liberation"},
        {"lemma": "rajtaütés", "pos": "noun", "cefr": "B1", "gloss": "ambush, surprise attack"},
        {"lemma": "átkelőhely", "pos": "noun", "cefr": "B1", "gloss": "river crossing, ford"},
        {"lemma": "lezárul", "pos": "verb", "cefr": "B1", "gloss": "to conclude, come to a close"},
        {"lemma": "fennhatóság", "pos": "noun", "cefr": "B1", "gloss": "sovereignty, jurisdiction"}
    ],
    [
        {
            "question": "Melyik békekötéssel zárult le végleg a 150 éves török hódoltság kora?",
            "options": ["Az 1699-es karlócai békével", "Az 1538-as váradi békével", "Az 1606-os bécsi békével", "Az 1664-es vasvári békével"],
            "correctIndex": 0,
            "explanation": "Az 1699-es karlócai béke vetett véget a török jelenlétnek a Temesköz kivételével."
        }
    ]
)
write_json(STORIES_DIR / "story.b1.torokkiuzese.04.json", story_4)

voc_4 = {
    "id": "voc.b1.torokkiuzese.04",
    "title": "A karlócai béke és a felszabadulás szókincse",
    "description": "Felszabadítás, rajtaütés, átkelőhely, lezárulás és fennhatóság.",
    "entries": [
        {"lemma": "felszabadítás", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "liberation of territories", "examples": [{"hu": "Magyarország felszabadítása tizenöt évig tartott.", "en": "The liberation of Hungary lasted fifteen years."}]}]},
        {"lemma": "rajtaütés", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "surprise attack, ambush", "examples": [{"hu": "A zentai rajtaütés megsemmisítette a szultán seregét.", "en": "The ambush at Zenta destroyed the Sultan's army."}]}]},
        {"lemma": "átkelőhely", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "river crossing, crossing point", "examples": [{"hu": "A sereget a Tisza átkelőhelyén lepték meg.", "en": "The army was surprised at the Tisza river crossing."}]}]},
        {"lemma": "lezárul", "pos": "verb", "cefr": "B1", "definitions": [{"meaning": "to come to a close, conclude", "examples": [{"hu": "1699-ben lezárult a török hódoltság kora.", "en": "In 1699, the era of Ottoman occupation came to an end."}]}]},
        {"lemma": "fennhatóság", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "rule, sovereign jurisdiction", "examples": [{"hu": "Az ország kikerült az oszmán fennhatóság alól.", "en": "The country was freed from Ottoman rule."}]}]}
    ]
}
write_json(VOCAB_DIR / "voc.b1.torokkiuzese.04.json", voc_4)

gr_4 = {
    "id": "gr.b1.torokkiuzese.04",
    "title": "Visszatekintő feltételes mód (ha nem lett volna... akkor lett volna...)",
    "description": "Constructing past counterfactual conditionals reflecting on historical outcomes.",
    "rules": [
        "A múlt idejű feltételes módot a múlt idejű igealak és a 'volna' segédszó kapcsolásával képezzük: 'harcolt volna', 'lett volna'.",
        "Történelmi elemzésekben a nem bekövetkezett események következményeit vizsgáljuk ezzel a szerkezettel."
    ],
    "tables": [
        {"headers": ["Feltételes tagmondat", "Főmondat", "Példa"], "rows": [
            ["Ha nem lett volna...", "...akkor nem győztek volna.", "Ha nem lett volna összefogás, a törökök maradtak volna."],
            ["Ha Jenő nem támadott volna...", "...a szultán elmenekült volna.", "Ha nem támadott volna, a csata eldöntetlen maradt volna."]
        ]}
    ],
    "examples": [
        {"spanish": "Ha nem lett volna nemzetközi segítség, Magyarország nem szabadult volna fel 1699-ben.", "english": "If there had not been international help, Hungary would not have been liberated in 1699."},
        {"spanish": "Ha Savoyai Jenő nem győzött volna Zentánál, a háború tovább folytatódott volna.", "english": "If Eugene of Savoy had not won at Zenta, the war would have continued further."},
        {"spanish": "A karlócai béke nélkül az ország török fennhatóság alatt maradt volna.", "english": "Without the Peace of Karlowitz, the country would have remained under Turkish rule."}
    ]
}
write_json(GRAMMAR_DIR / "gr.b1.torokkiuzese.04.json", gr_4)

exs_4 = [
    {"id": "ex.b1.torokkiuzese.04.01", "type": "multiple-choice", "lesson": "lesson.b1.torokkiuzese.04", "teaches": ["karlocai-beke-1699"], "prompt": "Melyik évben írták alá a karlócai békét?", "options": ["1699-ben", "1686-ban", "1703-ban", "1664-ben"], "correctIndex": 0, "explanation": "A karlócai békét 1699. január 26-án kötötték meg."},
    {"id": "ex.b1.torokkiuzese.04.02", "type": "fill-blank", "lesson": "lesson.b1.torokkiuzese.04", "teaches": ["felszabaditas"], "prompt": "Egészítsd ki a mondatot!", "sentence": "Az 1699-es béke az ország *felszabadítását* jelentette a török uralom alól.", "target": "felszabadítását"},
    {"id": "ex.b1.torokkiuzese.04.03", "type": "sentence-builder", "lesson": "lesson.b1.torokkiuzese.04", "teaches": ["volna", "zentai-csata"], "prompt": "Rakd össze a múlt idejű feltételes mondatot!", "chips": ["Ha", "nem", "győztek", "volna,", "a", "háború", "folytatódott", "volna."], "target": "Ha nem győztek volna, a háború folytatódott volna.", "english": "If they had not won, the war would have continued."},
    {"id": "ex.b1.torokkiuzese.04.04", "type": "multiple-choice", "lesson": "lesson.b1.torokkiuzese.04", "teaches": ["Savoyai-Jeno"], "prompt": "Ki aratott döntő győzelmet a török fősereg felett 1697-ben Zentánál?", "options": ["Savoyai Jenő herceg", "Bocskai István", "Zrínyi Miklós", "Petneházy Dávid"], "correctIndex": 0, "explanation": "Savoyai Jenő herceg zentai győzelme kényszerítette békére a szultánt."},
    {"id": "ex.b1.torokkiuzese.04.05", "type": "fill-blank", "lesson": "lesson.b1.torokkiuzese.04", "teaches": ["lezarul"], "prompt": "Egészítsd ki a mondatot a megfelelő igealakkal!", "sentence": "A karlócai békével végleg *lezárult* a török hódoltság kora.", "target": "lezárult"},
    {"id": "ex.b1.torokkiuzese.04.06", "type": "sentence-builder", "lesson": "lesson.b1.torokkiuzese.04", "teaches": ["fennhatosag", "karlocai-beke"], "prompt": "Alkoss szabályos mondatot a megadott szavakból!", "chips": ["Magyarország", "kiszabadult", "az", "oszmán", "fennhatóság", "alól."], "target": "Magyarország kiszabadult az oszmán fennhatóság alól.", "english": "Hungary was freed from Ottoman rule."},
    {"id": "ex.b1.torokkiuzese.04.07", "type": "multiple-choice", "lesson": "lesson.b1.torokkiuzese.04", "teaches": ["Temeskoz"], "prompt": "Melyik terület maradt egyedüliként még török kézen 1699 után?", "options": ["A Temesköz (Bánság)", "Buda és Pest", "Erdély", "A Dunántúl"], "correctIndex": 0, "explanation": "A karlócai békében egyedül a Temesköz maradt még oszmán igazgatás alatt 1718-ig."},
    {"id": "ex.b1.torokkiuzese.04.08", "type": "fill-blank", "lesson": "lesson.b1.torokkiuzese.04", "teaches": ["rajtautes"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A zentai meglepetésszerű *rajtaütés* döntötte el a háború sorsát.", "target": "rajtaütés"}
]
write_json(EXERCISES_DIR / "ex.b1.torokkiuzese.04.json", make_exercise_group("ex.b1.torokkiuzese.04", "A karlócai béke gyakorlatai", "Gyakorlatok Savoyai Jenőről, az 1699-es békéről és a feltételes múlt időről.", exs_4))

lesson_4 = make_lesson(
    "lesson.b1.torokkiuzese.04",
    "A felszabadító háborúk és a karlócai béke (1699)",
    "Visszatekintő feltételes mondatok (ha nem lett volna... volna)",
    "Megismerjük Savoyai Jenő zentai diadalát, az 1699-es karlócai békét és a 150 éves hódoltság történelmi lezárását.",
    ["Megérteni az 1699-es karlócai béke jelentőségét", "Használni a visszatekintő feltételes múlt idejű szerkezeteket", "Ismerni Savoyai Jenő szerepét és a határok helyreállítását"],
    "story.b1.torokkiuzese.04",
    "voc.b1.torokkiuzese.04",
    "gr.b1.torokkiuzese.04",
    "ex.b1.torokkiuzese.04",
    [e["id"] for e in exs_4]
)
write_json(LESSONS_DIR / "lesson.b1.torokkiuzese.04.json", lesson_4)


# ==========================================
# LESSON 5: b1-torokkiuzese-05 (Újszerzeményi feszültségek)
# ==========================================
story_5 = make_story(
    "story.b1.torokkiuzese.05",
    "Az újszerzeményi politika és az új feszültségek kibontakozása",
    "A felszabadulást követően a bécsi udvar abszolutista politikája, a fegyverváltság és az elnéptelenedett falvak nehézségei új nemzeti ellenállást szültek.",
    "Buda, Pozsony és a felvidéki vármegyék",
    ["Contrasting old and new realities (szemben a korábbiakkal, ahelyett, hogy, többek között)", "Socio-political transitions"],
    ["Újszerzeményi Bizottság", "fegyverváltság", "elnéptelenedés", "kurtacsaták", "kuruc elégedetlenség"],
    [
        "Bár a török uralom véget ért, a magyarok számára a felszabadulás nem hozta el a várt szabadságot. A Habsburg udvar meghódított területként kezelte az országot: I. Lipót felfüggesztette a rendi alkotmányt, és idegen zsoldosokat szállásolt el a falvakban.",
        "A bécsi kormányzat felállította az Újszerzeményi Bizottságot (Neoacquistica Commissio). Ahelyett, hogy a magyar nemesek egyszerűen visszakaphatták volna ősi birtokaikat, írásos oklevelekkel kellett igazolniuk tulajdonjogukat, és meg kellett fizetniük a birtok értékének 10%-át kitevő fegyverváltságot (ius armorum).",
        "Szemben a békés újjáépítés ígéretével, az elviselhetetlen adóterhek, a katonai erőszak és az elnéptelenedett pusztaságok látványa mély elkeseredést keltett. Mindezek következtében a társadalom minden rétegében felizzott az elégedetlenség, megteremtve a Rákóczi-szabadságharc közvetlen előfeltételeit."
    ],
    [
        {"lemma": "fegyverváltság", "pos": "noun", "cefr": "B1", "gloss": "redemption tax / weapon tax (ius armorum)"},
        {"lemma": "elnéptelenedés", "pos": "noun", "cefr": "B1", "gloss": "depopulation"},
        {"lemma": "felfüggeszt", "pos": "verb", "cefr": "B1", "gloss": "to suspend (constitution/rights)"},
        {"lemma": "adóteher", "pos": "noun", "cefr": "B1", "gloss": "tax burden"},
        {"lemma": "elégedetlenség", "pos": "noun", "cefr": "B1", "gloss": "discontent, dissatisfaction"}
    ],
    [
        {
            "question": "Mit követelt az Újszerzeményi Bizottság a magyar nemesektől a birtokaik visszaadásáért?",
            "options": ["Írásos igazolást és a birtokérték 10%-át fegyverváltságként", "Teljes átkeresztelkedést", "Költözést Bécsbe", "Minden vagyonuk átadását"],
            "correctIndex": 0,
            "explanation": "A nemeseknek oklevelekkel kellett bizonyítaniuk jogukat és fegyverváltságot kellett fizetniük."
        }
    ]
)
write_json(STORIES_DIR / "story.b1.torokkiuzese.05.json", story_5)

voc_5 = {
    "id": "voc.b1.torokkiuzese.05",
    "title": "A hódoltság utáni berendezkedés és feszültségek szókincse",
    "description": "Fegyverváltság, elnéptelenedés, jogfosztás, adóterhek és elégedetlenség.",
    "entries": [
        {"lemma": "fegyverváltság", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "redemption tax on recovered noble estates", "examples": [{"hu": "A nemeseknek fegyverváltságot kellett fizetniük birtokaikért.", "en": "Nobles had to pay a weapon tax for their estates."}]}]},
        {"lemma": "elnéptelenedés", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "depopulation of war-torn lands", "examples": [{"hu": "A háborúk után súlyos elnéptelenedés sújtotta az Alföldet.", "en": "After the wars, severe depopulation afflicted the Great Plain."}]}]},
        {"lemma": "felfüggeszt", "pos": "verb", "cefr": "B1", "definitions": [{"meaning": "to suspend constitution or liberties", "examples": [{"hu": "A császár felfüggesztette a rendi alkotmányt.", "en": "The Emperor suspended the feudal constitution."}]}]},
        {"lemma": "adóteher", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "heavy tax burden", "examples": [{"hu": "A lakosság alig bírta el a hatalmas adóterheket.", "en": "The population could barely bear the immense tax burdens."}]}]},
        {"lemma": "elégedetlenség", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "social discontent, unrest", "examples": [{"hu": "A birodalmi politika országos elégedetlenséget szült.", "en": "Imperial policy bred nationwide discontent."}]}]}
    ]
}
write_json(VOCAB_DIR / "voc.b1.torokkiuzese.05.json", voc_5)

gr_5 = {
    "id": "gr.b1.torokkiuzese.05",
    "title": "Ellentétező és helyettesítő szerkezetek (ahelyett, hogy, szemben a korábbiakkal)",
    "description": "Formulating structural contrasts between expectations and harsh realities.",
    "rules": [
        "Az 'ahelyett, hogy' kötőszós szerkezet elmaradt vagy meg nem valósult elvárásokat állít szembe a valósággal.",
        "A 'szemben a korábbiakkal' kifejezés a történelmi korszakváltások drasztikus változásait emeli ki."
    ],
    "tables": [
        {"headers": ["Kifejezés", "Funkció", "Példa"], "rows": [
            ["ahelyett, hogy...", "elmaradt cselekvés", "Ahelyett, hogy segítettek volna, adót vetettek ki."],
            ["szemben a korábbiakkal", "kontraszt a múlttal", "Szemben a korábbiakkal, elvesztek a jogok."]
        ]}
    ],
    "examples": [
        {"spanish": "Ahelyett, hogy békét hozott volna, a felszabadulás új feszültségeket teremtett.", "english": "Instead of bringing peace, the liberation created new tensions."},
        {"spanish": "Szemben a korábbi ígéretekkel, a császár idegen katonaságot telepített az országba.", "english": "Contrary to earlier promises, the Emperor quartered foreign troops in the country."},
        {"spanish": "A nemeseknek fizetniük kellett, ahelyett, hogy visszakapták volna jogaikat.", "english": "The nobles had to pay, instead of regaining their rights."}
    ]
}
write_json(GRAMMAR_DIR / "gr.b1.torokkiuzese.05.json", gr_5)

exs_5 = [
    {"id": "ex.b1.torokkiuzese.05.01", "type": "multiple-choice", "lesson": "lesson.b1.torokkiuzese.05", "teaches": ["Ujszerzemenyi-Bizottsag"], "prompt": "Mi volt az Újszerzeményi Bizottság (Neoacquistica Commissio) feladata?", "options": ["A visszaszerzett birtokok tulajdonjogának felülvizsgálata és fegyverváltság szedése", "Új templomok építése", "A török katonák áttelepítése", "Új pénz verése Budán"], "correctIndex": 0, "explanation": "A bizottság vizsgálta a birtokjogokat és szedte be a 10%-os fegyverváltságot."},
    {"id": "ex.b1.torokkiuzese.05.02", "type": "fill-blank", "lesson": "lesson.b1.torokkiuzese.05", "teaches": ["fegyvervaltsag"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A birtokok visszaszerzéséért *fegyverváltságot* kellett fizetni Bécsnek.", "target": "fegyverváltságot"},
    {"id": "ex.b1.torokkiuzese.05.03", "type": "sentence-builder", "lesson": "lesson.b1.torokkiuzese.05", "teaches": ["ahelyett", "feszultseg"], "prompt": "Rakd össze az ellentétező mondatot!", "chips": ["Ahelyett,", "hogy", "béke", "lett", "volna,", "új", "feszültség", "támadt."], "target": "Ahelyett, hogy béke lett volna, új feszültség támadt.", "english": "Instead of there being peace, new tension arose."},
    {"id": "ex.b1.torokkiuzese.05.04", "type": "multiple-choice", "lesson": "lesson.b1.torokkiuzese.05", "teaches": ["Lipót-csaszar"], "prompt": "Melyik Habsburg uralkodó függesztette fel a magyar rendi jogokat a török kiűzése után?", "options": ["I. Lipót", "Mária Terézia", "II. József", "I. Mátyás"], "correctIndex": 0, "explanation": "I. Lipót császár abszolutista kormányzást vezetett be a felszabadított területeken."},
    {"id": "ex.b1.torokkiuzese.05.05", "type": "fill-blank", "lesson": "lesson.b1.torokkiuzese.05", "teaches": ["adoteher"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A lakosság nyögte a katonai beszállásolás súlyos *adóterheit*.", "target": "adóterheit"},
    {"id": "ex.b1.torokkiuzese.05.06", "type": "sentence-builder", "lesson": "lesson.b1.torokkiuzese.05", "teaches": ["szemben", "elegedetlenseg"], "prompt": "Alkoss szabályos összetett mondatot!", "chips": ["Szemben", "a", "reményekkel,", "országos", "elégedetlenség", "bontakozott", "ki."], "target": "Szemben a reményekkel, országos elégedetlenség bontakozott ki.", "english": "Contrary to hopes, nationwide discontent developed."},
    {"id": "ex.b1.torokkiuzese.05.07", "type": "multiple-choice", "lesson": "lesson.b1.torokkiuzese.05", "teaches": ["kuruc-mozgalom"], "prompt": "Milyen mozgalom kibontakozásához vezetett a Habsburg-udvar elnyomó politikája?", "options": ["A kuruc szabadságharchoz Rákóczi vezetésével", "A reformáció elterjedéséhez", "A jobbágyság azonnali felszabadításához", "A törökök visszahívásához"], "correctIndex": 0, "explanation": "A Lipót-kori elnyomás robbantotta ki a Rákóczi-szabadságharcot 1703-ban."},
    {"id": "ex.b1.torokkiuzese.05.08", "type": "fill-blank", "lesson": "lesson.b1.torokkiuzese.05", "teaches": ["felfuggeszt"], "prompt": "Egészítsd ki a mondatot a megfelelő igealakkal!", "sentence": "A bécsi udvar *felfüggesztette* a rendi alkotmány működését.", "target": "felfüggesztette"}
]
write_json(EXERCISES_DIR / "ex.b1.torokkiuzese.05.json", make_exercise_group("ex.b1.torokkiuzese.05", "Az újszerzeményi korszak gyakorlatai", "Gyakorlatok a Lipót-kori abszolutizmusról és az ellentétező szerkezetekről.", exs_5))

lesson_5 = make_lesson(
    "lesson.b1.torokkiuzese.05",
    "Az újszerzeményi politika és az új feszültségek kibontakozása",
    "Ellentétező és helyettesítő szerkezetek (ahelyett, hogy, szemben a korábbiakkal)",
    "Összegezzük a török kiűzése utáni feszültségeket: az Újszerzeményi Bizottságot, a fegyverváltságot és a kuruc mozgalom elindulását.",
    ["Megérteni az Újszerzeményi Bizottság működését és következményeit", "Használni az 'ahelyett, hogy' és 'szemben a korábbiakkal' szerkezeteket", "Felismerni a Rákóczi-szabadságharchoz vezető társadalmi okokat"],
    "story.b1.torokkiuzese.05",
    "voc.b1.torokkiuzese.05",
    "gr.b1.torokkiuzese.05",
    "ex.b1.torokkiuzese.05",
    [e["id"] for e in exs_5]
)
write_json(LESSONS_DIR / "lesson.b1.torokkiuzese.05.json", lesson_5)


# ==========================================
# CONSOLIDATION LESSON: b1-torokkiuzese-consolidation
# ==========================================
cons_exs = [
    {"id": "ex.b1.torokkiuzese.cons.01", "type": "multiple-choice", "lesson": "lesson.b1.torokkiuzese.consolidation", "teaches": ["Zrinyi-1664"], "prompt": "Melyik haditett tette híressé Zrínyi Miklóst 1664-ben?", "options": ["Az eszéki híd felégetése a téli hadjáratban", "Buda visszafoglalása", "Nándorfehérvár megvédése", "Zenta felszabadítása"], "correctIndex": 0, "explanation": "Zrínyi 1664-ben égette fel az eszéki hidat."},
    {"id": "ex.b1.torokkiuzese.cons.02", "type": "fill-blank", "lesson": "lesson.b1.torokkiuzese.consolidation", "teaches": ["hadvezer"], "prompt": "Zrínyi Miklós a korszak legnagyobb magyar *hadvezére* és költője volt.", "sentence": "Zrínyi Miklós a korszak legnagyobb magyar *hadvezére* és költője volt.", "target": "hadvezére"},
    {"id": "ex.b1.torokkiuzese.cons.03", "type": "multiple-choice", "lesson": "lesson.b1.torokkiuzese.consolidation", "teaches": ["Becs-1683"], "prompt": "Melyik évben verte vissza a lengyel felmentő sereg Bécs ostromát?", "options": ["1683-ban", "1686-ban", "1664-ben", "1526-ban"], "correctIndex": 0, "explanation": "Bécs felmentése 1683-ban történt Sobieski János vezetésével."},
    {"id": "ex.b1.torokkiuzese.cons.04", "type": "fill-blank", "lesson": "lesson.b1.torokkiuzese.consolidation", "teaches": ["Szent-Liga"], "prompt": "1684-ben XI. Ince pápa támogatásával megalakult a *Szent Liga*.", "sentence": "1684-ben XI. Ince pápa támogatásával megalakult a *Szent Liga*.", "target": "Szent Liga"},
    {"id": "ex.b1.torokkiuzese.cons.05", "type": "sentence-builder", "lesson": "lesson.b1.torokkiuzese.consolidation", "teaches": ["mindekozben", "felmento-sereg"], "prompt": "Rakd össze a mondatot!", "chips": ["Mindeközben", "megérkezett", "a", "lengyel", "felmentő", "sereg."], "target": "Mindeközben megérkezett a lengyel felmentő sereg.", "english": "Meanwhile, the Polish relief army arrived."},
    {"id": "ex.b1.torokkiuzese.cons.06", "type": "multiple-choice", "lesson": "lesson.b1.torokkiuzese.consolidation", "teaches": ["Buda-1686"], "prompt": "Melyik napon foglalta vissza a nemzetközi haderő Buda várát?", "options": ["1686. szeptember 2-án", "1541. augusztus 29-én", "1699. január 26-án", "1683. szeptember 12-én"], "correctIndex": 0, "explanation": "Buda 1686. szeptember 2-án szabadult fel."},
    {"id": "ex.b1.torokkiuzese.cons.07", "type": "fill-blank", "lesson": "lesson.b1.torokkiuzese.consolidation", "teaches": ["Lotharingiai-Karoly"], "prompt": "Buda ostromát a császári fősereg élén *Lotharingiai Károly* herceg vezette.", "sentence": "Buda ostromát a császári fősereg élén *Lotharingiai Károly* herceg vezette.", "target": "Lotharingiai Károly"},
    {"id": "ex.b1.torokkiuzese.cons.08", "type": "sentence-builder", "lesson": "lesson.b1.torokkiuzese.consolidation", "teaches": ["falakon-kivul", "ostrom"], "prompt": "Alkoss szabályos mondatot!", "chips": ["A", "falakon", "kívül", "tízezrek", "harcoltak", "az", "ostromban."], "target": "A falakon kívül tízezrek harcoltak az ostromban.", "english": "Outside the walls, tens of thousands fought in the siege."},
    {"id": "ex.b1.torokkiuzese.cons.09", "type": "multiple-choice", "lesson": "lesson.b1.torokkiuzese.consolidation", "teaches": ["Zenta-1697"], "prompt": "Melyik csatában aratott döntő győzelmet Savoyai Jenő 1697-ben?", "options": ["A zentai csatában", "A mohácsi csatában", "A szentgotthárdi csatában", "A kenyérmezei csatában"], "correctIndex": 0, "explanation": "Savoyai Jenő Zentánál verte tönkre a török fősereget 1697-ben."},
    {"id": "ex.b1.torokkiuzese.cons.10", "type": "fill-blank", "lesson": "lesson.b1.torokkiuzese.consolidation", "teaches": ["karlocai-beke"], "prompt": "Az 1699-es *karlócai béke* véget vetett a másfél évszázados hódoltságnak.", "sentence": "Az 1699-es *karlócai béke* véget vetett a másfél évszázados hódoltságnak.", "target": "karlócai béke"},
    {"id": "ex.b1.torokkiuzese.cons.11", "type": "sentence-builder", "lesson": "lesson.b1.torokkiuzese.consolidation", "teaches": ["volna", "felszabaditas"], "prompt": "Rakd össze a feltételes múlt idejű mondatot!", "chips": ["Összefogás", "nélkül", "az", "ország", "nem", "szabadult", "volna", "fel."], "target": "Összefogás nélkül az ország nem szabadult volna fel.", "english": "Without solidarity, the country would not have been liberated."},
    {"id": "ex.b1.torokkiuzese.cons.12", "type": "multiple-choice", "lesson": "lesson.b1.torokkiuzese.consolidation", "teaches": ["Ujszerzemenyi-Bizottsag"], "prompt": "Mit vizsgált az Újszerzeményi Bizottság (Neoacquistica Commissio)?", "options": ["A visszaszerzett nemesi birtokok jogosultságát és a fegyverváltság fizetését", "A várak építési anyagát", "A török katonák létszámát", "A mezőgazdasági termést"], "correctIndex": 0, "explanation": "A bizottság a birtokjogokat és a fegyverváltság befizetését ellenőrizte."},
    {"id": "ex.b1.torokkiuzese.cons.13", "type": "fill-blank", "lesson": "lesson.b1.torokkiuzese.consolidation", "teaches": ["fegyvervaltsag"], "prompt": "A nemeseknek a birtok értékének tíz százalékát kitevő *fegyverváltságot* kellett fizetniük.", "sentence": "A nemeseknek a birtok értékének tíz százalékát kitevő *fegyverváltságot* kellett fizetniük.", "target": "fegyverváltságot"},
    {"id": "ex.b1.torokkiuzese.cons.14", "type": "sentence-builder", "lesson": "lesson.b1.torokkiuzese.consolidation", "teaches": ["ahelyett", "beke"], "prompt": "Alkoss ellentétező mondatot!", "chips": ["Ahelyett,", "hogy", "megbékélés", "jött", "volna,", "új", "háború", "kezdődött."], "target": "Ahelyett, hogy megbékélés jött volna, új háború kezdődött.", "english": "Instead of reconciliation coming, a new war began."},
    {"id": "ex.b1.torokkiuzese.cons.15", "type": "multiple-choice", "lesson": "lesson.b1.torokkiuzese.consolidation", "teaches": ["hodoltsag-hossza"], "prompt": "Hány évig állt török megszállás alatt Buda városa (1541–1686)?", "options": ["145 évig", "100 évig", "50 évig", "300 évig"], "correctIndex": 0, "explanation": "Buda pontosan 145 évig (1541-től 1686-ig) volt török kézen."},
    {"id": "ex.b1.torokkiuzese.cons.16", "type": "fill-blank", "lesson": "lesson.b1.torokkiuzese.consolidation", "teaches": ["zaszlo"], "prompt": "Petneházy Dávid magyar vitéz tűzte ki a győzelmi *zászlót* a budai várfalra.", "sentence": "Petneházy Dávid magyar vitéz tűzte ki a győzelmi *zászlót* a budai várfalra.", "target": "zászlót"},
    {"id": "ex.b1.torokkiuzese.cons.17", "type": "sentence-builder", "lesson": "lesson.b1.torokkiuzese.consolidation", "teaches": ["szemben", "remeny"], "prompt": "Rakd össze a mondatot!", "chips": ["Szemben", "a", "reményekkel,", "a", "bécsi", "udvar", "elnyomást", "hozott."], "target": "Szemben a reményekkel, a bécsi udvar elnyomást hozott.", "english": "Contrary to hopes, the Viennese court brought oppression."},
    {"id": "ex.b1.torokkiuzese.cons.18", "type": "multiple-choice", "lesson": "lesson.b1.torokkiuzese.consolidation", "teaches": ["Petnehazy-David"], "prompt": "Ki volt a budai vár visszafoglalásának egyik legbátrabb magyar rohamvezetője?", "options": ["Petneházy Dávid", "Dobó István", "Szondi György", "Kinizsi Pál"], "correctIndex": 0, "explanation": "Petneházy Dávid hajdúkapitány tört be elsőként a várba 1686-ban."},
    {"id": "ex.b1.torokkiuzese.cons.19", "type": "fill-blank", "lesson": "lesson.b1.torokkiuzese.consolidation", "teaches": ["lezarul"], "prompt": "1699-ben a karlócai szerződéssel *lezárult* a török jelenlét korszaka.", "sentence": "1699-ben a karlócai szerződéssel *lezárult* a török jelenlét korszaka.", "target": "lezárult"},
    {"id": "ex.b1.torokkiuzese.cons.20", "type": "multiple-choice", "lesson": "lesson.b1.torokkiuzese.consolidation", "teaches": ["Rákóczi-elozmenyek"], "prompt": "Milyen történelmi korszak követte közvetlenül a török kiűzését és a Lipót-kori elnyomást?", "options": ["A Rákóczi-szabadságharc (1703–1711)", "A reformkor", "Az 1848-as forradalom", "A dualizmus"], "correctIndex": 0, "explanation": "A török kiűzése utáni elnyomás vezetett a Rákóczi-szabadságharchoz 1703-ban."}
]
write_json(EXERCISES_DIR / "ex.b1.torokkiuzese.consolidation.json", make_exercise_group("ex.b1.torokkiuzese.consolidation", "A török kiűzése összefoglaló gyakorlatok", "Átfogó teszt a törökök kiűzésének hadjáratairól és a kapcsolódó nyelvtani szerkezetekről.", cons_exs))

cons_lesson = {
    "id": "lesson.b1.torokkiuzese.consolidation",
    "title": "Driving Out the Ottomans: Unit 12 Consolidation",
    "level": "B1",
    "track": "citizenship",
    "estimatedMinutes": 25,
    "prerequisites": [
        "lesson.b1.torokkiuzese.01",
        "lesson.b1.torokkiuzese.02",
        "lesson.b1.torokkiuzese.03",
        "lesson.b1.torokkiuzese.04",
        "lesson.b1.torokkiuzese.05"
    ],
    "grammar": ["Unit review"],
    "vocabulary": ["Unit review"],
    "culturalContext": "Magyar történelem összefoglalás (Honosítási vizsgafelkészítő)",
    "sections": [
        {
            "type": "intro",
            "title": "Unit 12 Consolidation: Driving Out the Ottomans (1664–1699)",
            "body": "Ebben az összefoglaló leckében áttekintjük Zrínyi Miklós 1664-es hadjáratát, Bécs 1683-as ostromát és a Szent Liga megalakulását (1684), Buda 1686-os felszabadítását, az 1699-es karlócai békét, valamint az újszerzeményi feszültségeket."
        },
        {
            "type": "goal",
            "title": "Consolidation Goals",
            "items": [
                "A török kiűzésének legfontosabb évei (1683, 1686, 1697, 1699) és hadvezérei pontos ismerete",
                "Időrendi (mindeközben, ezt követően), helyhatározói és visszatekintő feltételes szerkezetek biztos alkalmazása",
                "Az Újszerzeményi Bizottság és a Rákóczi-szabadságharc előzményeinek megértése"
            ]
        },
        {
            "type": "exercise-group",
            "title": "Comprehensive Unit 12 Practice",
            "ref": "ex.b1.torokkiuzese.consolidation",
            "exerciseRefs": [e["id"] for e in cons_exs]
        },
        {
            "type": "checklist",
            "items": [
                "Tudom, mikor szabadult fel Buda (1686. szeptember 2.)",
                "Ismerem az 1699-es karlócai béke történelmi jelentőségét",
                "Tudom, kik voltak Zrínyi Miklós, Lotharingiai Károly és Savoyai Jenő",
                "Értem az Újszerzeményi Bizottság és a fegyverváltság fogalmát"
            ]
        }
    ]
}
write_json(LESSONS_DIR / "lesson.b1.torokkiuzese.consolidation.json", cons_lesson)

print("Unit 12 (b1-torokkiuzese) complete!")
