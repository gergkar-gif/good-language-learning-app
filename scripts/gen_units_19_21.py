# -*- coding: utf-8 -*-
"""
Generator for Citizenship Units 19, 20, 21:
- Unit 19: b1-monarchia (Austria-Hungary / Boldog békeidők)
- Unit 20: b1-vilaghaboru (World War I & Collapse)
- Unit 21: b1-trianon (The Treaty of Trianon 1920)
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
# UNIT 19: AUSTRIA-HUNGARY & THE GOLDEN AGE (b1-monarchia)
# ==============================================================================

# Lesson 1: Budapest világvárossá válása (1873)
story_19_1 = make_story(
    "story.b1.monarchia.01",
    "Budapest világvárossá válása (1873)",
    "Pest, Buda és Óbuda 1873-as egyesítésével létrejött Budapest, amely alig néhány évtized alatt Európa egyik leggyorsabban fejlődő világvárosává nőtt.",
    "Budapest",
    ["Városfejlődést és átalakulást kifejező igék (-vá/-vé válik, kiépül, egyesül)", "Urbanization and architectural expansion"],
    ["városegyesítés", "világváros", "Andrássy út", "Nagykörút", "Közmunkatanács"],
    [
        "1873. november 17-én történelmi jelentőségű esemény történt: Pest, Buda és Óbuda hivatalosan egyesült, megalapítva a modern Budapest székesfővárost. Az új főváros a kiegyezést követő gazdasági fellendülés központjává és a Kárpát-medence szellemi szívévé vált.",
        "A Fővárosi Közmunkatanács irányításával lenyűgöző léptékű városrendezés vette kezdetét. Sugárutak és körutak épültek ki: a pesti Nagykörút és a párizsi eleganciájú Andrássy út, amely mentén paloták sora és az Operaház magasodott.",
        "Budapest lakossága néhány évtized alatt megháromszorozódott, és a Duna menti ikerváros igazi modern metropoliszként ragyogott a Monarchia központjában."
    ],
    [
        {"lemma": "városegyesítés", "pos": "noun", "cefr": "B1", "gloss": "unification of cities"},
        {"lemma": "világváros", "pos": "noun", "cefr": "B1", "gloss": "world metropolis, global city"},
        {"lemma": "kiépül", "pos": "verb", "cefr": "B1", "gloss": "to be built up, fully developed"},
        {"lemma": "sugárút", "pos": "noun", "cefr": "B1", "gloss": "avenue, boulevard (radial)"},
        {"lemma": "metropolisz", "pos": "noun", "cefr": "B1", "gloss": "metropolis"}
    ],
    [
        {
            "question": "Melyik évben egyesült Pest, Buda és Óbuda Budapest néven?",
            "options": ["1873-ban", "1848-ban", "1867-ben", "1896-ban"],
            "correctIndex": 0,
            "explanation": "A három városrész 1873. november 17-én egyesült Budapestté."
        }
    ]
)
write_json(STORIES_DIR / "story.b1.monarchia.01.json", story_19_1)

voc_19_1 = {
    "id": "voc.b1.monarchia.01",
    "title": "A városegyesítés és városfejlődés szókincse",
    "description": "Városegyesítés, világváros, sugárút, körút és kiépülés.",
    "entries": [
        {"lemma": "városegyesítés", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "unification of separate cities into one capital", "examples": [{"hu": "Az 1873-as városegyesítés elindította a fejlődést.", "en": "The 1873 unification launched the development."}]}]},
        {"lemma": "világváros", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "world metropolis", "examples": [{"hu": "Budapest gyorsan világvárossá vált.", "en": "Budapest quickly became a world metropolis."}]}]},
        {"lemma": "sugárút", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "radial grand avenue", "examples": [{"hu": "Az Andrássy út az ország leghíresebb sugárútja.", "en": "Andrássy Avenue is the country's most famous boulevard."}]}]},
        {"lemma": "kiépül", "pos": "verb", "cefr": "B1", "definitions": [{"meaning": "to be constructed, developed over time", "examples": [{"hu": "A pesti Nagykörút évtizedek alatt épült ki.", "en": "The Grand Boulevard of Pest was built up over decades."}]}]},
        {"lemma": "metropolisz", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "major metropolis", "examples": [{"hu": "Budapest európai hírű metropolisz lett.", "en": "Budapest became a European-renowned metropolis."}]}]}
    ]
}
write_json(VOCAB_DIR / "voc.b1.monarchia.01.json", voc_19_1)

gr_19_1 = {
    "id": "gr.b1.monarchia.01",
    "title": "Átváltozást és eredményt kifejező határozóragok (-vá/-vé válik, -ként működik)",
    "description": "Expressing transformation, becoming, and functional roles in urban and historical context.",
    "rules": [
        {
            "explanation": "A -vá/-vé rag az igékkel (válik, nő, alakul) átváltozást, új állapottá válást fejez ki. Mássalhangzó után hasonul: világvárossá, központtá.",
            "examples": [
                {"spanish": "Budapest világvárossá nőtte ki magát.", "english": "Budapest grew into a world metropolis."},
                {"spanish": "A város a Kárpát-medence szellemi központjává vált.", "english": "The city became the intellectual center of the Carpathian Basin."}
            ]
        }
    ]
}
write_json(GRAMMAR_DIR / "gr.b1.monarchia.01.json", gr_19_1)

exs_19_1 = [
    {"id": "ex.b1.monarchia.01.01", "type": "multiple-choice", "lesson": "lesson.b1.monarchia.01", "teaches": ["varosegyesites-1873"], "prompt": "Mely városok egyesülésével jött létre Budapest 1873-ban?", "options": ["Pest, Buda és Óbuda", "Pest, Debrecen és Szeged", "Buda, Pozsony és Győr", "Pest, Székesfehérvár és Veszprém"], "correctIndex": 0, "explanation": "Pest, Buda és Óbuda egyesült 1873-ban."},
    {"id": "ex.b1.monarchia.01.02", "type": "fill-blank", "lesson": "lesson.b1.monarchia.01", "teaches": ["vilagvarossa"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A városegyesítés után Budapest igazi *világvárossá* vált.", "target": "világvárossá"},
    {"id": "ex.b1.monarchia.01.03", "type": "sentence-builder", "lesson": "lesson.b1.monarchia.01", "teaches": ["egyesul", "fovaros"], "prompt": "Rakd össze a történelmi mondatot!", "chips": ["1873-ban", "Pest,", "Buda", "és", "Óbuda", "egy", "fővárossá", "egyesült."], "target": "1873-ban Pest, Buda és Óbuda egy fővárossá egyesült.", "english": "In 1873, Pest, Buda and Óbuda merged into a single capital."},
    {"id": "ex.b1.monarchia.01.04", "type": "multiple-choice", "lesson": "lesson.b1.monarchia.01", "teaches": ["Andrassy-ut-sugarut"], "prompt": "Melyik híres budapesti sugárút épült ki ebben a korszakban a párizsi mintát követve?", "options": ["Az Andrássy út", "A Váci utca", "A Rákóczi út", "Az Üllői út"], "correctIndex": 0, "explanation": "Az Andrássy út a kor legreprezentatívabb sugárútja volt."},
    {"id": "ex.b1.monarchia.01.05", "type": "fill-blank", "lesson": "lesson.b1.monarchia.01", "teaches": ["sugarut"], "prompt": "Egészítsd ki a mondatot!", "sentence": "Az Andrássy út a főváros legszebb *sugárútja*.", "target": "sugárútja"},
    {"id": "ex.b1.monarchia.01.06", "type": "sentence-builder", "lesson": "lesson.b1.monarchia.01", "teaches": ["kiepul", "korut"], "prompt": "Alkoss szabályos mondatot!", "chips": ["A", "Duna", "mentén", "modern", "körutak", "és", "hidak", "épültek", "ki."], "target": "A Duna mentén modern körutak és hidak épültek ki.", "english": "Along the Danube modern boulevards and bridges were built up."},
    {"id": "ex.b1.monarchia.01.07", "type": "multiple-choice", "lesson": "lesson.b1.monarchia.01", "teaches": ["Kozmunkatanacs"], "prompt": "Mely intézmény irányította a nagyszabású budapesti városrendezést?", "options": ["A Fővárosi Közmunkatanács", "A Helytartótanács", "A Magyar Tudományos Akadémia", "A Magyar Országos Levéltár"], "correctIndex": 0, "explanation": "A Fővárosi Közmunkatanács felelt a várostervezésért és az építkezésekért."},
    {"id": "ex.b1.monarchia.01.08", "type": "fill-blank", "lesson": "lesson.b1.monarchia.01", "teaches": ["metropolisz"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A századfordulóra Budapest pezsgő európai *metropolisz* lett.", "target": "metropolisz"}
]
write_json(EXERCISES_DIR / "ex.b1.monarchia.01.json", make_exercise_group("ex.b1.monarchia.01", "Budapest világvárossá válása gyakorlatok", "Gyakorlatok a városegyesítésről, a sugárutakról és az átváltozást kifejező határozóragokról.", exs_19_1))

lesson_19_1 = make_lesson(
    "lesson.b1.monarchia.01",
    "Budapest világvárossá válása (1873)",
    "Átváltozást kifejező szerkezetek (-vá/-vé válik, metropoliszként fejlődik)",
    "Ismerjük meg Budapest 1873-as megalapítását és világvárossá válásának lenyűgöző korszakát.",
    ["Tudni az 1873-as városegyesítés tényét és jelentőségét", "Használni a -vá/-vé átváltozást kifejező határozóragokat", "Ismerni a korszak főbb városrendezési fejlesztéseit (Andrássy út, Nagykörút)"],
    "story.b1.monarchia.01",
    "voc.b1.monarchia.01",
    "gr.b1.monarchia.01",
    "ex.b1.monarchia.01",
    [e["id"] for e in exs_19_1]
)
write_json(LESSONS_DIR / "lesson.b1.monarchia.01.json", lesson_19_1)


# Lesson 2: A Millennium (1896): Kisföldalatti, Hősök tere és Parlament
story_19_2 = make_story(
    "story.b1.monarchia.02",
    "A Millennium (1896) és a nemzeti nagyság ünnepe",
    "1896-ban Magyarország fennállásának ezeréves évfordulóját ünnepelte: átadták az európai kontinens első földalatti vasútját, megnyitották a Városligeti Millenniumi Kiállítást, és épülni kezdett a Parlament.",
    "Városliget és Országház, Budapest",
    ["Időbeli mérföldköveket és ünnepi eseményeket kifejező szerkezetek (évfordulójára, megünnepel, átad)", "Monumental achievements and national anniversaries"],
    ["millennium", "honfoglalás", "Kisföldalatti", "Hősök tere", "Országház"],
    [
        "1896-ban Magyarország káprázatos pompával ünnepelte a honfoglalás ezeréves évfordulóját, a millenniumot. Az ország az elmúlt három évtized páratlan gazdasági és kulturális felemelkedését mutatta be a világnak.",
        "A jubileumra megépült a Milleniumi Földalatti Vasút (a Kisföldalatti), amely London után a világ második, az európai kontinens legelső földalattija volt. Az Andrássy út torkolatánál elkezdték kialakítani a grandiózus Hősök terét és a Millenniumi emlékművet a hét honfoglaló vezér és a magyar királyok szobraival.",
        "Ugyancsak ebben a korszakban épült fel a Duna partján Steindl Imre tervei alapján a monumentális neogótikus Országház, amely a magyar alkotmányosság és törvényhozás szimbóluma lett."
    ],
    [
        {"lemma": "millennium", "pos": "noun", "cefr": "B1", "gloss": "millennium (1000-year anniversary of the conquest)"},
        {"lemma": "jubileum", "pos": "noun", "cefr": "B1", "gloss": "jubilee, major anniversary"},
        {"lemma": "földalatti", "pos": "noun", "cefr": "B1", "gloss": "underground railway, subway"},
        {"lemma": "emlékmű", "pos": "noun", "cefr": "B1", "gloss": "monument, memorial"},
        {"lemma": "Országház", "pos": "noun", "cefr": "B1", "gloss": "Parliament building"}
    ],
    [
        {
            "question": "Melyik jelentős történelmi esemény ezeréves évfordulóját ünnepelte Magyarország 1896-ban?",
            "options": ["A honfoglalás (896) ezeréves évfordulóját", "Szent István koronázását", "A nándorfehérvári diadalt", "Az 1848-as forradalmat"],
            "correctIndex": 0,
            "explanation": "A millennium a 896-os magyar honfoglalás ezeréves jubileuma volt."
        }
    ]
)
write_json(STORIES_DIR / "story.b1.monarchia.02.json", story_19_2)

voc_19_2 = {
    "id": "voc.b1.monarchia.02",
    "title": "A millennium és a nemzeti emlékek szókincse",
    "description": "Millennium, jubileum, földalatti vasút, emlékmű és Országház.",
    "entries": [
        {"lemma": "millennium", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "1000th anniversary celebration of the Hungarian Conquest in 1896", "examples": [{"hu": "1896-ban rendezték meg a millenniumi ünnepségeket.", "en": "In 1896, the millennium celebrations were held."}]}]},
        {"lemma": "földalatti", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "underground railway", "examples": [{"hu": "A budapesti földalatti a kontinens legelső földalattija volt.", "en": "The Budapest subway was the very first underground on the continent."}]}]},
        {"lemma": "emlékmű", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "monument or memorial", "examples": [{"hu": "A Hősök terén áll a Millenniumi emlékmű.", "en": "The Millennium Monument stands on Heroes' Square."}]}]},
        {"lemma": "Országház", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "Hungarian Parliament building on the Danube bank", "examples": [{"hu": "Az Országház Steindl Imre tervei alapján épült.", "en": "The Parliament was built according to Imre Steindl's designs."}]}]},
        {"lemma": "jubileum", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "jubilee anniversary", "examples": [{"hu": "A jubileum tiszteletére hatalmas kiállítást szerveztek.", "en": "A massive exhibition was organized in honor of the jubilee."}]}]}
    ]
}
write_json(VOCAB_DIR / "voc.b1.monarchia.02.json", voc_19_2)

gr_19_2 = {
    "id": "gr.b1.monarchia.02",
    "title": "Évfordulókra és tiszteletadásra utaló szerkezetek (tiszteletére, emlékére, jubileumára)",
    "description": "Postpositional phrases and nominal suffixes used to commemorate historical events.",
    "rules": [
        {
            "explanation": "A 'tiszteletére', 'emlékére', 'alkalmából' névutók évfordulók, ünnepségek és emlékművek kontextusában a megemlékezés célját jelölik.",
            "examples": [
                {"spanish": "A honfoglalás ezeréves évfordulójának emlékére épült a Hősök tere.", "english": "Heroes' Square was built to commemorate the 1000th anniversary of the Conquest."},
                {"spanish": "A millennium tiszteletére nyitották meg a földalattit.", "english": "The underground was opened in honor of the millennium."}
            ]
        }
    ]
}
write_json(GRAMMAR_DIR / "gr.b1.monarchia.02.json", gr_19_2)

exs_19_2 = [
    {"id": "ex.b1.monarchia.02.01", "type": "multiple-choice", "lesson": "lesson.b1.monarchia.02", "teaches": ["millennium-1896"], "prompt": "Mikor ünnepelte Magyarország a millenniumot?", "options": ["1896-ban", "1873-ban", "1900-ban", "1848-ban"], "correctIndex": 0, "explanation": "A millenniumot 1896-ban ünnepelték a honfoglalás 1000. évfordulóján."},
    {"id": "ex.b1.monarchia.02.02", "type": "fill-blank", "lesson": "lesson.b1.monarchia.02", "teaches": ["millenniumot"], "prompt": "Egészítsd ki a mondatot!", "sentence": "Az egész ország büszkén ünnepelte a *millenniumot*.", "target": "millenniumot"},
    {"id": "ex.b1.monarchia.02.03", "type": "sentence-builder", "lesson": "lesson.b1.monarchia.02", "teaches": ["foldalatti", "kontinens"], "prompt": "Rakd össze az állítást!", "chips": ["A", "budapesti", "Kisföldalatti", "volt", "a", "kontinens", "első", "földalatti", "vasútja."], "target": "A budapesti Kisföldalatti volt a kontinens első földalatti vasútja.", "english": "The Budapest Kisföldalatti was the continent's first underground railway."},
    {"id": "ex.b1.monarchia.02.04", "type": "multiple-choice", "lesson": "lesson.b1.monarchia.02", "teaches": ["Hosok-tere-emlekmu"], "prompt": "Kiknek a szobrai találhatók a Hősök terén álló Millenniumi emlékművön?", "options": ["A hét honfoglaló vezér és a magyar történelem nagy királyai és fejedelmei", "Csak osztrák császárok", "Ókori római istenek", "Csak a 1848-as tábornokok"], "correctIndex": 0, "explanation": "A hét vezér és a magyar történelem kiemelkedő uralkodói állnak a Hősök terén."},
    {"id": "ex.b1.monarchia.02.05", "type": "fill-blank", "lesson": "lesson.b1.monarchia.02", "teaches": ["emlekere"], "prompt": "Egészítsd ki a mondatot a megfelelő névutóval!", "sentence": "A teret az ezeréves honfoglalás *emlékére* építették.", "target": "emlékére"},
    {"id": "ex.b1.monarchia.02.06", "type": "sentence-builder", "lesson": "lesson.b1.monarchia.02", "teaches": ["Orszaghaz", "Steindl"], "prompt": "Alkoss szabályos mondatot!", "chips": ["Az", "Országházat", "Steindl", "Imre", "tervezte", "neogótikus", "stílusban."], "target": "Az Országházat Steindl Imre tervezte neogótikus stílusban.", "english": "The Parliament building was designed by Imre Steindl in neo-Gothic style."},
    {"id": "ex.b1.monarchia.02.07", "type": "multiple-choice", "lesson": "lesson.b1.monarchia.02", "teaches": ["Varosliget-kiallitas"], "prompt": "Hol rendezték meg az 1896-os nagyszabású Millenniumi Országos Kiállítást?", "options": ["A Városligetben", "A Margitszigeten", "A Gellért-hegyen", "A Budai Várban"], "correctIndex": 0, "explanation": "A Városliget volt a millenniumi ünnepségek fő helyszíne."},
    {"id": "ex.b1.monarchia.02.08", "type": "fill-blank", "lesson": "lesson.b1.monarchia.02", "teaches": ["Orszaghaz"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A Duna partján magasodik a monumentális *Országház*.", "target": "Országház"}
]
write_json(EXERCISES_DIR / "ex.b1.monarchia.02.json", make_exercise_group("ex.b1.monarchia.02", "A millennium gyakorlatok", "Gyakorlatok az 1896-os millenniumról, a Kisföldalattiról, a Hősök teréről és az Országházról.", exs_19_2))

lesson_19_2 = make_lesson(
    "lesson.b1.monarchia.02",
    "A Millennium (1896) és a nemzeti nagyság ünnepe",
    "Évfordulók és emlékezés nyelvtani szerkezetei (tiszteletére, emlékére)",
    "Fedezzük fel az 1896-os millenniumi év csúcsteljesítményeit: a földalattit, a Hősök terét és a Parlamentet.",
    ["Ismerni a millennium (1896) és a honfoglalás ezeréves kapcsolatát", "Tudni a kontinens legelső földalattijának budapesti megépítését", "Használni a megemlékezést és jubileumot kifejező névutós szerkezeteket"],
    "story.b1.monarchia.02",
    "voc.b1.monarchia.02",
    "gr.b1.monarchia.02",
    "ex.b1.monarchia.02",
    [e["id"] for e in exs_19_2]
)
write_json(LESSONS_DIR / "lesson.b1.monarchia.02.json", lesson_19_2)


# Lesson 3: Ipari és technikai forradalom: Ganz, MÁV, malomipar és feltalálók
story_19_3 = make_story(
    "story.b1.monarchia.03",
    "Ipari és technikai forradalom a boldog békeidőkben",
    "A 19. század végén Magyarország agrárországból modern ipari-agrár gazdasággá vált: a vasúthálózat kiépült, a budapesti malomipar világelső lett, a Ganz gyár pedig a világ élvonalába tört a villamosiparban.",
    "Ganz gyár és MÁV pályaudvarok, Budapest",
    ["Eredményt, növekedést és technikai újítást kifejező igék (fejleszt, feltalál, élvonalba tör)", "Industrial revolution, innovations, and economic boom"],
    ["iparosodás", "vasúthálózat", "Ganz gyár", "malomipar", "transzformátor"],
    [
        "A dualizmus korszaka a magyar gazdaság aranykora volt. A korszerű gőzhengeres őrlési eljárásnak köszönhetően Budapest a világ legnagyobb malomipari központjává fejlődött, megelőzve az európai vetélytársakat.",
        "Kiépült a sűrű magyar vasúthálózat a Magyar Államvasutak (MÁV) vezetésével, Baross Gábor, a 'vasminiszter' reformjainak hatására. A vasút összekötötte a mezőgazdasági vidékeket a kikötőkkel és piacokkal.",
        "A Ganz gyárban világhírű mérnökök alkottak: Bláthy Ottó, Déri Miksa és Zipernowsky Károly feltalálták a zárt vasmagos transzformátort, Kandó Kálmán pedig úttörő volt a villamos vasúti vontatásban. Puskás Tivadar pedig feltalálta a telefonhírmondót és a telefonközpont elvét."
    ],
    [
        {"lemma": "iparosodás", "pos": "noun", "cefr": "B1", "gloss": "industrialization"},
        {"lemma": "vasúthálózat", "pos": "noun", "cefr": "B1", "gloss": "railway network"},
        {"lemma": "malomipar", "pos": "noun", "cefr": "B1", "gloss": "milling industry, flour milling"},
        {"lemma": "transzformátor", "pos": "noun", "cefr": "B1", "gloss": "electrical transformer"},
        {"lemma": "feltaláló", "pos": "noun", "cefr": "B1", "gloss": "inventor"}
    ],
    [
        {
            "question": "Melyik jelentős találmány fűződik a Ganz gyár három világhírű magyar mérnökéhez (Bláthy, Déri, Zipernowsky)?",
            "options": ["A zárt vasmagos transzformátor", "A gőzgép", "A belső égésű motor", "A távíró"],
            "correctIndex": 0,
            "explanation": "Bláthy, Déri és Zipernowsky 1885-ben szabadalmaztatta a transzformátort a Ganz gyárban."
        }
    ]
)
write_json(STORIES_DIR / "story.b1.monarchia.03.json", story_19_3)

voc_19_3 = {
    "id": "voc.b1.monarchia.03",
    "title": "Az iparosodás és találmányok szókincse",
    "description": "Iparosodás, vasúthálózat, malomipar, transzformátor és feltaláló.",
    "entries": [
        {"lemma": "iparosodás", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "rapid industrial development", "examples": [{"hu": "A dualizmus alatt gyors ütemű iparosodás ment végbe.", "en": "Rapid industrialization took place during the Dualism."}]}]},
        {"lemma": "vasúthálózat", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "railway network", "examples": [{"hu": "A MÁV létrehozta az egységes országos vasúthálózatot.", "en": "MÁV created a unified nationwide railway network."}]}]},
        {"lemma": "malomipar", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "grain and flour milling industry", "examples": [{"hu": "A pesti malomipar világszerte híres volt.", "en": "The flour milling industry in Pest was world-famous."}]}]},
        {"lemma": "transzformátor", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "electrical transformer", "examples": [{"hu": "A transzformátor forradalmasította a villamos energiát.", "en": "The transformer revolutionized electrical power."}]}]},
        {"lemma": "feltaláló", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "inventor", "examples": [{"hu": "A magyar feltalálók a technika élvonalába tartoztak.", "en": "Hungarian inventors belonged to the forefront of engineering."}]}]}
    ]
}
write_json(VOCAB_DIR / "voc.b1.monarchia.03.json", voc_19_3)

gr_19_3 = {
    "id": "gr.b1.monarchia.03",
    "title": "Eredményt és hatást kifejező összetett mondatok (köszönhetően, hatására, révén)",
    "description": "Expressing cause, instrument, and resulting success using postpositions and case markers.",
    "rules": [
        {
            "explanation": "A 'köszönhetően' (+ részeshatározó), 'hatására', 'révén' kifejezések pozitív eredményeket, fejlődést és sikeres innovációt kötnek össze.",
            "examples": [
                {"spanish": "A mérnökök zsenialitásának köszönhetően a Ganz gyár világcég lett.", "english": "Thanks to the genius of engineers, Ganz factory became a world firm."},
                {"spanish": "A vasútfejlesztés révén a gabona gyorsan eljutott a kikötőkbe.", "english": "By means of railway development, grain quickly reached ports."}
            ]
        }
    ]
}
write_json(GRAMMAR_DIR / "gr.b1.monarchia.03.json", gr_19_3)

exs_19_3 = [
    {"id": "ex.b1.monarchia.03.01", "type": "multiple-choice", "lesson": "lesson.b1.monarchia.03", "teaches": ["Ganz-gyar-transzformator"], "prompt": "Melyik híres magyar gyár volt a korszak elektromos és gépipari csúcsvállalata?", "options": ["A Ganz és Társa gyár", "A Csepeli Vas- és Fémművek", "A Rába Vagongyár", "A Zsolnay Porcelángyár"], "correctIndex": 0, "explanation": "A Ganz gyár a világ egyik vezető gép- és elektrotechnikai vállalata volt."},
    {"id": "ex.b1.monarchia.03.02", "type": "fill-blank", "lesson": "lesson.b1.monarchia.03", "teaches": ["iparosodas"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A korszakban rohamos *iparosodás* jellemezte az országot.", "target": "iparosodás"},
    {"id": "ex.b1.monarchia.03.03", "type": "sentence-builder", "lesson": "lesson.b1.monarchia.03", "teaches": ["vasut", "Baross-Gabor"], "prompt": "Rakd össze a közlekedéstörténeti mondatot!", "chips": ["Baross", "Gábor", "miniszter", "kiépítette", "a", "modern", "magyar", "vasúthálózatot."], "target": "Baross Gábor miniszter kiépítette a modern magyar vasúthálózatot.", "english": "Minister Gábor Baross built up the modern Hungarian railway network."},
    {"id": "ex.b1.monarchia.03.04", "type": "multiple-choice", "lesson": "lesson.b1.monarchia.03", "teaches": ["malomipar-Budapest"], "prompt": "Melyik élelmiszeripari ágban volt Budapest a világ élvonalában a 19. század végén?", "options": ["A malomiparban (gőzmalmok)", "A csokoládégyártásban", "A citrusfélék feldolgozásában", "A kávépörkölésben"], "correctIndex": 0, "explanation": "Budapest gőzmalmai a világ egyik legnagyobb malomipari központját alkották."},
    {"id": "ex.b1.monarchia.03.05", "type": "fill-blank", "lesson": "lesson.b1.monarchia.03", "teaches": ["transzformatort"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A Ganz mérnökei megalkották a modern *transzformátort*.", "target": "transzformátort"},
    {"id": "ex.b1.monarchia.03.06", "type": "sentence-builder", "lesson": "lesson.b1.monarchia.03", "teaches": ["feltalalo", "Puskas-Tivadar"], "prompt": "Alkoss szabályos mondatot!", "chips": ["Puskás", "Tivadar", "feltalálta", "a", "világhírű", "telefonhírmondót."], "target": "Puskás Tivadar feltalálta a világhírű telefonhírmondót.", "english": "Tivadar Puskás invented the world-famous Telefonhírmondó."},
    {"id": "ex.b1.monarchia.03.07", "type": "multiple-choice", "lesson": "lesson.b1.monarchia.03", "teaches": ["Kando-Kalman"], "prompt": "Kandó Kálmán melyik technikai területen végzett úttörő munkát?", "options": ["A vasút-villamosításban és a villamos mozdonyok megalkotásában", "A repülőgépgyártásban", "A nyomdászatban", "A bányászatban"], "correctIndex": 0, "explanation": "Kandó Kálmán a nagyvasúti villamos vontatás világhírű megteremtője volt."},
    {"id": "ex.b1.monarchia.03.08", "type": "fill-blank", "lesson": "lesson.b1.monarchia.03", "teaches": ["feltalalok"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A tehetséges magyar *feltalálók* gazdagították a világ tudományát.", "target": "feltalálók"}
]
write_json(EXERCISES_DIR / "ex.b1.monarchia.03.json", make_exercise_group("ex.b1.monarchia.03", "Ipari és technikai forradalom gyakorlatok", "Gyakorlatok a Ganz gyárról, a malomiparról, a vasútfejlesztésről és a magyar feltalálókról.", exs_19_3))

lesson_19_3 = make_lesson(
    "lesson.b1.monarchia.03",
    "Ipari és technikai forradalom a boldog békeidőkben",
    "Eredményt és innovációt kifejező szerkezetek (köszönhetően, révén)",
    "Tekintsük át a dualizmus gazdasági és mérnöki sikereit: a Ganz gyárat, a MÁV hálózatát és a transzformátort.",
    ["Ismerni a korszak vezető iparágait (malomipar, gépgyártás, villamosipar)", "Tudni a Ganz gyár és mérnökei (Bláthy, Déri, Zipernowsky, Kandó) jelentőségét", "Használni a sikert és eredményt indokló nyelvtani kifejezéseket"],
    "story.b1.monarchia.03",
    "voc.b1.monarchia.03",
    "gr.b1.monarchia.03",
    "ex.b1.monarchia.03",
    [e["id"] for e in exs_19_3]
)
write_json(LESSONS_DIR / "lesson.b1.monarchia.03.json", lesson_19_3)


# Lesson 4: A társadalom árnyoldalai: nemzetiségi feszültségek és kivándorlás
story_19_4 = make_story(
    "story.b1.monarchia.04",
    "Társadalmi feszültségek: a nemzetiségi kérdés és a kivándorlás",
    "A látványos gazdasági fejlődés mellett súlyos feszültségek terhelték az országot: a soknemzetiségű lakosság nemzeti törekvései és az elszegényedő parasztság tömeges kivándorlása Amerikába.",
    "Fiume kikötője és vidéki Magyarország",
    ["Ellentétet és társadalmi problémákat kifejező szerkezetek (annak ellenére, hogy; feszültséget okoz; kivándorol)", "Social tensions, nationality issues, and emigration"],
    ["többnemzetiségű", "kivándorlás", "elszegényedés", "Fiume", "nemzetiségi arány"],
    [
        "A Magyar Királyság lakosságának alig több mint a fele volt magyar anyanyelvű; az országban jelentős számban éltek románok, szlovákok, németek, szerbek és ruszinok. Bár az 1868-as nemzetiségi törvény liberális volt, a kormányzatok a magyarosítás politikáját szorgalmazták, ami növelte a nemzetiségek ellenállását.",
        "A mezőgazdaság gépesítése és a nagybirtokrendszer miatt a falusi zsellérek és cselédek százezrei maradtak föld és megélhetés nélkül. A mélyülő szegénység hatalmas kivándorlási hullámot indított el a tengerentúlra.",
        "A századforduló évtizedeiben mintegy másfél millió ember hagyta el az országot Fiume kikötőjén keresztül, hogy az Egyesült Államok gyáraiban és bányáiban próbáljon szerencsét."
    ],
    [
        {"lemma": "kivándorlás", "pos": "noun", "cefr": "B1", "gloss": "emigration"},
        {"lemma": "többnemzetiségű", "pos": "adj", "cefr": "B1", "gloss": "multi-ethnic, multinational"},
        {"lemma": "elszegényedés", "pos": "noun", "cefr": "B1", "gloss": "impoverishment"},
        {"lemma": "magyarosítás", "pos": "noun", "cefr": "B1", "gloss": "Magyarization policies"},
        {"lemma": "tengerentúl", "pos": "noun", "cefr": "B1", "gloss": "overseas (America)"}
    ],
    [
        {
            "question": "Hová vándorolt ki mintegy másfél millió ember a mélyülő szegénység miatt a dualizmus végén?",
            "options": ["Az Egyesült Államokba (Amerikába)", "Oroszországba", "Ausztráliába", "Afrikába"],
            "correctIndex": 0,
            "explanation": "A kivándorlók döntő többsége az Egyesült Államokba ment új életet kezdeni."
        }
    ]
)
write_json(STORIES_DIR / "story.b1.monarchia.04.json", story_19_4)

voc_19_4 = {
    "id": "voc.b1.monarchia.04",
    "title": "A nemzetiségek és kivándorlás szókincse",
    "description": "Kivándorlás, többnemzetiségű, elszegényedés, tengerentúl és feszültség.",
    "entries": [
        {"lemma": "kivándorlás", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "mass emigration to escape poverty", "examples": [{"hu": "A gazdasági nehézségek miatt felerősödött a kivándorlás.", "en": "Due to economic hardships, emigration intensified."}]}]},
        {"lemma": "többnemzetiségű", "pos": "adj", "cefr": "B1", "definitions": [{"meaning": "multi-ethnic country composed of different language groups", "examples": [{"hu": "A történelmi Magyarország többnemzetiségű állam volt.", "en": "Historical Hungary was a multi-ethnic state."}]}]},
        {"lemma": "elszegényedés", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "process of becoming impoverished", "examples": [{"hu": "A földnélküli parasztság elszegényedése súlyos gond volt.", "en": "The impoverishment of landless peasantry was a grave issue."}]}]},
        {"lemma": "tengerentúl", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "overseas, especially North America", "examples": [{"hu": "Sokan a tengerentúlon kerestek munkát.", "en": "Many sought work overseas."}]}]},
        {"lemma": "magyarosítás", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "cultural and linguistic Magyarization policies", "examples": [{"hu": "A magyarosítási törekvések ellenállást szültek.", "en": "Magyarization efforts generated resistance."}]}]}
    ]
}
write_json(VOCAB_DIR / "voc.b1.monarchia.04.json", voc_19_4)

gr_19_4 = {
    "id": "gr.b1.monarchia.04",
    "title": "Ellentétet és korlátozást kifejező kötőszavak (bár, ámbár, noha, annak ellenére, hogy)",
    "description": "Expressing concession, contrasts, and historical paradoxes in complex sentences.",
    "rules": [
        {
            "explanation": "A 'bár', 'noha', 'annak ellenére, hogy' kötőszók megengedő mellékmondatokat vezetnek be, megvilágítva az egyidejű sikerek és nehézségek ellentétét.",
            "examples": [
                {"spanish": "Bár a gazdaság virágzott, sok paraszt mély szegénységben élt.", "english": "Although the economy boomed, many peasants lived in deep poverty."},
                {"spanish": "Noha a törvények biztosították a jogokat, a feszültségek nőttek.", "english": "Even though laws secured rights, tensions increased."}
            ]
        }
    ]
}
write_json(GRAMMAR_DIR / "gr.b1.monarchia.04.json", gr_19_4)

exs_19_4 = [
    {"id": "ex.b1.monarchia.04.01", "type": "multiple-choice", "lesson": "lesson.b1.monarchia.04", "teaches": ["tobbnemzetisegu-allam"], "prompt": "Milyen volt a történelmi Magyarország etnikai összetétele a dualizmusban?", "options": ["Többnemzetiségű állam (románok, szlovákok, németek, szerbek és magyarok)", "Teljesen egynyelvű, homogén magyar állam", "Kizárólag osztrák és magyar lakosság", "Csak szláv népek lakták"], "correctIndex": 0, "explanation": "Magyarország lakosságának jelentős részét nemzetiségek alkották."},
    {"id": "ex.b1.monarchia.04.02", "type": "fill-blank", "lesson": "lesson.b1.monarchia.04", "teaches": ["kivandorlas"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A szegénység miatt hatalmas *kivándorlás* indult Amerikába.", "target": "kivándorlás"},
    {"id": "ex.b1.monarchia.04.03", "type": "sentence-builder", "lesson": "lesson.b1.monarchia.04", "teaches": ["tengerentul", "szerencse"], "prompt": "Rakd össze a mondatot!", "chips": ["Másfél", "millió", "ember", "próbált", "szerencsét", "a", "tengerentúlon."], "target": "Másfél millió ember próbált szerencsét a tengerentúlon.", "english": "One and a half million people tried their fortune overseas."},
    {"id": "ex.b1.monarchia.04.04", "type": "multiple-choice", "lesson": "lesson.b1.monarchia.04", "teaches": ["Fiume-kikoto"], "prompt": "Melyik magyar tengeri kikötővároson keresztül vándoroltak ki a legtöbben?", "options": ["Fiume kikötőjén keresztül", "Triesztből", "Hamburgból", "Konstancából"], "correctIndex": 0, "explanation": "Fiume volt a Magyar Királyság hivatalos tengeri kikötője."},
    {"id": "ex.b1.monarchia.04.05", "type": "fill-blank", "lesson": "lesson.b1.monarchia.04", "teaches": ["elszegenyedett"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A föld nélküli parasztság gyorsan *elszegényedett*.", "target": "elszegényedett"},
    {"id": "ex.b1.monarchia.04.06", "type": "sentence-builder", "lesson": "lesson.b1.monarchia.04", "teaches": ["bar", "viragzott"], "prompt": "Alkoss megengedő összetett mondatot!", "chips": ["Bár", "a", "város", "gazdagodott,", "a", "falvakban", "szegénység", "uralkodott."], "target": "Bár a város gazdagodott, a falvakban szegénység uralkodott.", "english": "Although the city grew rich, poverty reigned in the villages."},
    {"id": "ex.b1.monarchia.04.07", "type": "multiple-choice", "lesson": "lesson.b1.monarchia.04", "teaches": ["nemzetisegek-feszultseg"], "prompt": "Miért mélyültek el a nemzetiségi ellentétek a századfordulón?", "options": ["Mert a nemzetiségek autonómiát és elismerést követeltek az erőszakos magyarosítással szemben", "Mert a nemzetiségek nem akartak adót fizetni", "Mert a kormány minden iskolát bezárt", "Mert el akartak költözni Ázsiába"], "correctIndex": 0, "explanation": "A nemzetiségek anyanyelvi jogaikért és önrendelkezésükért küzdöttek."},
    {"id": "ex.b1.monarchia.04.08", "type": "fill-blank", "lesson": "lesson.b1.monarchia.04", "teaches": ["tobbnemzetisegu"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A Monarchia egy sokszínű, *többnemzetiségű* birodalom volt.", "target": "többnemzetiségű"}
]
write_json(EXERCISES_DIR / "ex.b1.monarchia.04.json", make_exercise_group("ex.b1.monarchia.04", "Társadalmi feszültségek gyakorlatok", "Gyakorlatok a nemzetiségi kérdésről, a kivándorlásról és a megengedő mondatszerkezetekről.", exs_19_4))

lesson_19_4 = make_lesson(
    "lesson.b1.monarchia.04",
    "Társadalmi feszültségek: a nemzetiségi kérdés és a kivándorlás",
    "Megengedő és ellentétet kifejező szerkezetek (bár, noha, annak ellenére, hogy)",
    "Ismerjük meg a boldog békeidők árnyoldalait: a nemzetiségi feszültségeket és a kivándorlási hullámot.",
    ["Megérteni a többnemzetiségű Magyarország etnikai viszonyait", "Tudni a szegénység miatti tömeges amerikai kivándorlás okait és méreteit", "Használni a 'bár' és 'noha' kötőszavakkal képzett megengedő mondatokat"],
    "story.b1.monarchia.04",
    "voc.b1.monarchia.04",
    "gr.b1.monarchia.04",
    "ex.b1.monarchia.04",
    [e["id"] for e in exs_19_4]
)
write_json(LESSONS_DIR / "lesson.b1.monarchia.04.json", lesson_19_4)


# Lesson 5: Kulturális és szellemi virágkor: kávéházak, Nyugat és Eötvös Loránd
story_19_5 = make_story(
    "story.b1.monarchia.05",
    "Kulturális és tudományos aranykor a századfordulón",
    "A századforduló a magyar kultúra és tudomány egyik legragyogóbb korszaka: a pezsgő budapesti kávéházi élet, a Nyugat folyóirat indulása és Eötvös Loránd világhírű fizikai kísérletei fémjelezték.",
    "New York Kávéház és Tudományegyetem, Budapest",
    ["Szellemi hatást és kulturális megújulást kifejező igék (fémjelez, megújít, teret nyit, kísérletezik)", "Cultural flourishing, coffeehouse culture, and scientific breakthroughs"],
    ["kávéház", "Nyugat", "irodalom", "Eötvös Loránd", "torziós inga"],
    [
        "A századfordulós Budapestet a kávéházak világaként is emlegetik. A New York, a Japán és a Centrál kávéház az írók, költők, újságírók és művészek törzshelyévé vált, ahol remekművek születtek az asztaloknál.",
        "1908-ban elindult a 'Nyugat' című legendás irodalmi folyóirat, amely Ady Endre, Móricz Zsigmond, Babits Mihály és Kosztolányi Dezső vezetésével megújította a magyar irodalmat és európai színvonalra emelte a modern lírát és prózát.",
        "A tudományban báró Eötvös Loránd fizikus ért el korszakalkotó eredményeket: torziós ingája a gravitációs tér és a nehézségi erő mérésének legpontosabb eszköze lett világszerte, megalapozva a modern geofizikát és az olajkutatást."
    ],
    [
        {"lemma": "kávéház", "pos": "noun", "cefr": "B1", "gloss": "coffeehouse, literary café"},
        {"lemma": "folyóirat", "pos": "noun", "cefr": "B1", "gloss": "literary journal, periodical"},
        {"lemma": "líra", "pos": "noun", "cefr": "B1", "gloss": "poetry, lyric literature"},
        {"lemma": "torziós inga", "pos": "noun", "cefr": "B1", "gloss": "torsion pendulum (Eötvös pendulum)"},
        {"lemma": "korszakalkotó", "pos": "adj", "cefr": "B1", "gloss": "epoch-making, ground-breaking"}
    ],
    [
        {
            "question": "Melyik korszakalkotó irodalmi folyóirat indult útjára 1908-ban a modern magyar irodalom megújítására?",
            "options": ["A Nyugat", "A Hitel", "A Pesti Hírlap", "A Magyar Hírmondó"],
            "correctIndex": 0,
            "explanation": "A Nyugat folyóirat 1908-ban indult és a modern magyar irodalom szimbóluma lett."
        }
    ]
)
write_json(STORIES_DIR / "story.b1.monarchia.05.json", story_19_5)

voc_19_5 = {
    "id": "voc.b1.monarchia.05",
    "title": "A kávéházi kultúra és tudomány szókincse",
    "description": "Kávéház, folyóirat, irodalom, torziós inga és korszakalkotó.",
    "entries": [
        {"lemma": "kávéház", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "literary and artistic meeting place", "examples": [{"hu": "A New York kávéház az írók találkozóhelye volt.", "en": "The New York Café was a meeting place for writers."}]}]},
        {"lemma": "folyóirat", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "periodical or literary magazine", "examples": [{"hu": "A Nyugat folyóirat megújította a magyar lírát.", "en": "The Nyugat journal revolutionized Hungarian poetry."}]}]},
        {"lemma": "torziós inga", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "torsion pendulum invented by Loránd Eötvös to measure gravity", "examples": [{"hu": "Az Eötvös-féle torziós ingát világszerte alkalmazták.", "en": "The Eötvös torsion pendulum was applied worldwide."}]}]},
        {"lemma": "korszakalkotó", "pos": "adj", "cefr": "B1", "definitions": [{"meaning": "epoch-making, breakthrough", "examples": [{"hu": "Eötvös Loránd korszakalkotó fizikai kísérleteket végzett.", "en": "Loránd Eötvös conducted epoch-making physics experiments."}]}]},
        {"lemma": "líra", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "lyric poetry", "examples": [{"hu": "Ady Endre új hangot hozott a magyar lírába.", "en": "Endre Ady brought a new voice to Hungarian lyric poetry."}]}]}
    ]
}
write_json(VOCAB_DIR / "voc.b1.monarchia.05.json", voc_19_5)

gr_19_5 = {
    "id": "gr.b1.monarchia.05",
    "title": "Értékelést és elismerést kifejező melléknevek és határozószók (korszakalkotó, világhírű, kiemelkedően)",
    "description": "Appreciative evaluative descriptors for cultural and scientific achievements.",
    "rules": [
        {
            "explanation": "Történelmi és kulturális nagyságok bemutatásakor összetett értékelő mellékneveket használunk: 'korszakalkotó', 'világhírű', 'páratlan', 'kiemelkedő'.",
            "examples": [
                {"spanish": "Eötvös Loránd világhírű fizikus volt.", "english": "Loránd Eötvös was a world-famous physicist."},
                {"spanish": "A Nyugat korszakalkotó szerepet játszott az irodalomban.", "english": "Nyugat played an epoch-making role in literature."}
            ]
        }
    ]
}
write_json(GRAMMAR_DIR / "gr.b1.monarchia.05.json", gr_19_5)

exs_19_5 = [
    {"id": "ex.b1.monarchia.05.01", "type": "multiple-choice", "lesson": "lesson.b1.monarchia.05", "teaches": ["Nyugat-folyoirat-1908"], "prompt": "Melyik évben indult el a Nyugat című korszakalkotó folyóirat?", "options": ["1908-ban", "1896-ban", "1873-ban", "1848-ban"], "correctIndex": 0, "explanation": "A Nyugat 1908-ban indult Ady Endre és társai vezetésével."},
    {"id": "ex.b1.monarchia.05.02", "type": "fill-blank", "lesson": "lesson.b1.monarchia.05", "teaches": ["folyoirat"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A Nyugat a leghíresebb magyar irodalmi *folyóirat*.", "target": "folyóirat"},
    {"id": "ex.b1.monarchia.05.03", "type": "sentence-builder", "lesson": "lesson.b1.monarchia.05", "teaches": ["kavehaz", "irok"], "prompt": "Rakd össze a kávéházi kultúrát leíró mondatot!", "chips": ["A", "New", "York", "kávéházban", "írók", "és", "művészek", "alkottak."], "target": "A New York kávéházban írók és művészek alkottak.", "english": "In the New York Café writers and artists created works."},
    {"id": "ex.b1.monarchia.05.04", "type": "multiple-choice", "lesson": "lesson.b1.monarchia.05", "teaches": ["Eotvos-Lorand-inga"], "prompt": "Melyik világhírű műszert találta fel Eötvös Loránd fizikus a gravitáció mérésére?", "options": ["A torziós ingát", "A távcsövet", "A mikroszkópot", "A barométert"], "correctIndex": 0, "explanation": "Eötvös Loránd a torziós ingával vált világhírűvé."},
    {"id": "ex.b1.monarchia.05.05", "type": "fill-blank", "lesson": "lesson.b1.monarchia.05", "teaches": ["korszakalkoto"], "prompt": "Egészítsd ki a mondatot a megfelelő melléknévvel!", "sentence": "Eötvös Loránd *korszakalkotó* felfedezést tett a geofizikában.", "target": "korszakalkotó"},
    {"id": "ex.b1.monarchia.05.06", "type": "sentence-builder", "lesson": "lesson.b1.monarchia.05", "teaches": ["Ady-Endre", "lira"], "prompt": "Alkoss szabályos mondatot!", "chips": ["Ady", "Endre", "megújította", "a", "modern", "magyar", "líra", "nyelvét."], "target": "Ady Endre megújította a modern magyar líra nyelvét.", "english": "Endre Ady renewed the language of modern Hungarian lyric poetry."},
    {"id": "ex.b1.monarchia.05.07", "type": "multiple-choice", "lesson": "lesson.b1.monarchia.05", "teaches": ["irodalom-szazadfordulo"], "prompt": "Kik tartoztak a Nyugat első nagy nemzedékéhez?", "options": ["Ady Endre, Móricz Zsigmond, Babits Mihály és Kosztolányi Dezső", "Petőfi Sándor és Arany János", "Kazinczy Ferenc és Batsányi János", "Kölcsey Ferenc és Vörösmarty Mihály"], "correctIndex": 0, "explanation": "Ady, Babits, Kosztolányi és Móricz a Nyugat első nemzedékének vezéralakjai voltak."},
    {"id": "ex.b1.monarchia.05.08", "type": "fill-blank", "lesson": "lesson.b1.monarchia.05", "teaches": ["kavehazak"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A budapesti *kávéházak* a szellemi élet központjai voltak.", "target": "kávéházak"}
]
write_json(EXERCISES_DIR / "ex.b1.monarchia.05.json", make_exercise_group("ex.b1.monarchia.05", "Kulturális és tudományos virágkor gyakorlatok", "Gyakorlatok a Nyugatról, a kávéházi kultúráról, Eötvös Lorándról és az értékelő szerkezetekről.", exs_19_5))

lesson_19_5 = make_lesson(
    "lesson.b1.monarchia.05",
    "Kulturális és tudományos aranykor a századfordulón",
    "Értékelést kifejező szerkezetek (korszakalkotó, világhírű)",
    "Fedezzük fel a századforduló szellemi csúcsait: a kávéházi világot, a Nyugat íróit és Eötvös Loránd torziós ingáját.",
    ["Ismerni a kávéházi kultúra és a Nyugat (1908) kiemelkedő szerepét", "Tudni Eötvös Loránd geofizikai és fizikai jelentőségét", "Használni a kulturális teljesítményeket elismerő mellékneveket"],
    "story.b1.monarchia.05",
    "voc.b1.monarchia.05",
    "gr.b1.monarchia.05",
    "ex.b1.monarchia.05",
    [e["id"] for e in exs_19_5]
)
write_json(LESSONS_DIR / "lesson.b1.monarchia.05.json", lesson_19_5)


# Unit 19 Consolidation
cons_19_exs = [
    {"id": "ex.b1.monarchia.cons.01", "type": "multiple-choice", "lesson": "lesson.b1.monarchia.consolidation", "teaches": ["varosegyesites-1873"], "prompt": "Melyik évben egyesült Pest, Buda és Óbuda Budapestté?", "options": ["1873-ban", "1848-ban", "1867-ben", "1896-ban"], "correctIndex": 0, "explanation": "1873-ban született meg Budapest."},
    {"id": "ex.b1.monarchia.cons.02", "type": "fill-blank", "lesson": "lesson.b1.monarchia.consolidation", "teaches": ["vilagvarossa"], "prompt": "Budapest gyorsan pezsgő *világvárossá* nőtt.", "sentence": "Budapest gyorsan pezsgő *világvárossá* nőtt.", "target": "világvárossá"},
    {"id": "ex.b1.monarchia.cons.03", "type": "multiple-choice", "lesson": "lesson.b1.monarchia.consolidation", "teaches": ["millennium-1896"], "prompt": "Melyik évben tartották a honfoglalás 1000 éves millenniumi jubileumát?", "options": ["1896-ban", "1900-ban", "1873-ban", "1867-ben"], "correctIndex": 0, "explanation": "A millennium 1896-ban volt."},
    {"id": "ex.b1.monarchia.cons.04", "type": "fill-blank", "lesson": "lesson.b1.monarchia.consolidation", "teaches": ["Kisfoldalatti"], "prompt": "A kontinens legelső földalatti vasútja a budapesti *Kisföldalatti* volt.", "sentence": "A kontinens legelső földalatti vasútja a budapesti *Kisföldalatti* volt.", "target": "Kisföldalatti"},
    {"id": "ex.b1.monarchia.cons.05", "type": "sentence-builder", "lesson": "lesson.b1.monarchia.consolidation", "teaches": ["Hosok-tere", "szobrok"], "prompt": "Rakd össze a mondatot!", "chips": ["A", "Hősök", "terén", "állnak", "a", "honfoglaló", "vezérek", "szobrai."], "target": "A Hősök terén állnak a honfoglaló vezérek szobrai.", "english": "On Heroes' Square stand the statues of the conquering chieftains."},
    {"id": "ex.b1.monarchia.cons.06", "type": "multiple-choice", "lesson": "lesson.b1.monarchia.consolidation", "teaches": ["Orszaghaz-Steindl"], "prompt": "Ki volt a budapesti Országház neogótikus épületének tervezője?", "options": ["Steindl Imre", "Ybl Miklós", "Hild József", "Pollack Mihály"], "correctIndex": 0, "explanation": "Steindl Imre tervezte a Parlamentet."},
    {"id": "ex.b1.monarchia.cons.07", "type": "fill-blank", "lesson": "lesson.b1.monarchia.consolidation", "teaches": ["transzformatort"], "prompt": "A Ganz gyár mérnökei feltalálták a zárt vasmagos *transzformátort*.", "sentence": "A Ganz gyár mérnökei feltalálták a zárt vasmagos *transzformátort*.", "target": "transzformátort"},
    {"id": "ex.b1.monarchia.cons.08", "type": "sentence-builder", "lesson": "lesson.b1.monarchia.consolidation", "teaches": ["vasut", "halozat"], "prompt": "Alkoss szabályos összetett mondatot!", "chips": ["A", "MÁV", "kiépítette", "az", "egységes", "országos", "vasúthálózatot."], "target": "A MÁV kiépítette az egységes országos vasúthálózatot.", "english": "MÁV built up the unified nationwide railway network."},
    {"id": "ex.b1.monarchia.cons.09", "type": "multiple-choice", "lesson": "lesson.b1.monarchia.consolidation", "teaches": ["Baross-Gabor-vasminiszter"], "prompt": "Hogyan nevezték a közlekedést forradalmasító Baross Gábor minisztert?", "options": ["A 'vasminiszternek'", "A 'haza bölcsének'", "A 'legnagyobb magyarnak'", "A 'nemzet csalogányának'"], "correctIndex": 0, "explanation": "Baross Gábort a vasúti fejlesztések miatt a vasminiszternek hívták."},
    {"id": "ex.b1.monarchia.cons.10", "type": "fill-blank", "lesson": "lesson.b1.monarchia.consolidation", "teaches": ["kivandorlas"], "prompt": "A szegénység miatt mintegy másfél millió magyarországi lakos választotta a *kivándorlást*.", "sentence": "A szegénység miatt mintegy másfél millió magyarországi lakos választotta a *kivándorlást*.", "target": "kivándorlást"},
    {"id": "ex.b1.monarchia.cons.11", "type": "sentence-builder", "lesson": "lesson.b1.monarchia.consolidation", "teaches": ["Fiume", "kikoto"], "prompt": "Rakd össze a kivándorlásról szóló mondatot!", "chips": ["A", "kivándorlók", "Fiume", "kikötőjéből", "indultak", "a", "tengerentúlra."], "target": "A kivándorlók Fiume kikötőjéből indultak a tengerentúlra.", "english": "The emigrants departed from the port of Fiume overseas."},
    {"id": "ex.b1.monarchia.cons.12", "type": "multiple-choice", "lesson": "lesson.b1.monarchia.consolidation", "teaches": ["Nyugat-1908"], "prompt": "Melyik évben indult el a korszakalkotó Nyugat folyóirat?", "options": ["1908-ban", "1896-ban", "1873-ban", "1848-ban"], "correctIndex": 0, "explanation": "A Nyugat 1908-ban indult útjára."},
    {"id": "ex.b1.monarchia.cons.13", "type": "fill-blank", "lesson": "lesson.b1.monarchia.consolidation", "teaches": ["kavehazak"], "prompt": "A budapesti *kávéházak* asztalainál születtek a modern irodalom remekei.", "sentence": "A budapesti *kávéházak* asztalainál születtek a modern irodalom remekei.", "target": "kávéházak"},
    {"id": "ex.b1.monarchia.cons.14", "type": "sentence-builder", "lesson": "lesson.b1.monarchia.consolidation", "teaches": ["Eotvos-Lorand", "inga"], "prompt": "Alkoss szabályos mondatot!", "chips": ["Eötvös", "Loránd", "megalkotta", "a", "világhírű", "torziós", "ingát."], "target": "Eötvös Loránd megalkotta a világhírű torziós ingát.", "english": "Loránd Eötvös created the world-famous torsion pendulum."},
    {"id": "ex.b1.monarchia.cons.15", "type": "multiple-choice", "lesson": "lesson.b1.monarchia.consolidation", "teaches": ["Kando-Kalman-villamos"], "prompt": "Melyik területen alkotott forradalmit Kandó Kálmán mérnök?", "options": ["A vasúti villamos vontatásban", "A könyvnyomtatásban", "A textiliparban", "A növénytermesztésben"], "correctIndex": 0, "explanation": "Kandó Kálmán a villanymozdonyok és a villamos vontatás úttörője volt."},
    {"id": "ex.b1.monarchia.cons.16", "type": "fill-blank", "lesson": "lesson.b1.monarchia.consolidation", "teaches": ["Andrassy-ut"], "prompt": "Az elegáns *Andrássy út* mentén épült fel az Operaház.", "sentence": "Az elegáns *Andrássy út* mentén épült fel az Operaház.", "target": "Andrássy út"},
    {"id": "ex.b1.monarchia.cons.17", "type": "sentence-builder", "lesson": "lesson.b1.monarchia.consolidation", "teaches": ["iparosodas", "fejlodes"], "prompt": "Rakd össze az összefoglaló mondatot!", "chips": ["A", "dualizmus", "kora", "páratlan", "gazdasági", "fejlődést", "hozott."], "target": "A dualizmus kora páratlan gazdasági fejlődést hozott.", "english": "The era of Dualism brought unparalleled economic progress."},
    {"id": "ex.b1.monarchia.cons.18", "type": "multiple-choice", "lesson": "lesson.b1.monarchia.consolidation", "teaches": ["Puskas-Tivadar-telefon"], "prompt": "Melyik hírközlési találmány fűződik Puskás Tivadar nevéhez?", "options": ["A Telefonhírmondó és a telefonközpont", "A televízió", "Az internet", "A mobiltelefon"], "correctIndex": 0, "explanation": "Puskás Tivadar a Telefonhírmondó és a telefonközpont atyja volt."},
    {"id": "ex.b1.monarchia.cons.19", "type": "fill-blank", "lesson": "lesson.b1.monarchia.consolidation", "teaches": ["boldog-bekeidok"], "prompt": "A kiegyezéstől az első világháborúig tartó időszakot *boldog békeidőknek* is nevezik.", "sentence": "A kiegyezéstől az első világháborúig tartó időszakot *boldog békeidőknek* is nevezik.", "target": "boldog békeidőknek"},
    {"id": "ex.b1.monarchia.cons.20", "type": "multiple-choice", "lesson": "lesson.b1.monarchia.consolidation", "teaches": ["tobbnemzetisegu-Monarchia"], "prompt": "Milyen belső feszültség vezetett végül a történelmi Magyarország felbomlásához?", "options": ["A többnemzetiségű lakosság megoldatlan nemzetiségi kérdése és a világháború", "A vasútvonalak túlzott sűrűsége", "A kávéházak túl nagy száma", "A földalatti építése"], "correctIndex": 0, "explanation": "A nemzetiségi ellentétek és az első világháború pusztítása vezettek a felbomláshoz."}
]
write_json(EXERCISES_DIR / "ex.b1.monarchia.consolidation.json", make_exercise_group("ex.b1.monarchia.consolidation", "Ausztria-Magyarország és a boldog békeidők összefoglaló", "Átfogó teszt a millenniumról, Budapest fejlődéséről, a Ganz gyárról, a kultúráról és a feszültségekről.", cons_19_exs))

cons_19_lesson = {
    "id": "lesson.b1.monarchia.consolidation",
    "title": "Austria-Hungary: Unit 19 Consolidation",
    "level": "B1",
    "track": "citizenship",
    "estimatedMinutes": 25,
    "prerequisites": [
        "lesson.b1.monarchia.01",
        "lesson.b1.monarchia.02",
        "lesson.b1.monarchia.03",
        "lesson.b1.monarchia.04",
        "lesson.b1.monarchia.05"
    ],
    "grammar": ["Unit review"],
    "vocabulary": ["Unit review"],
    "culturalContext": "Magyar történelem összefoglalás (Honosítási vizsgafelkészítő)",
    "sections": [
        {
            "type": "intro",
            "title": "Unit 19 Consolidation: Austria-Hungary & The Golden Age (1867–1914)",
            "body": "Ebben az összefoglaló leckében áttekintjük Budapest 1873-as létrejöttét és világvárossá válását, az 1896-os Millennium ünnepét és a Kisföldalattit, a Ganz gyárat és a korszak feltalálóit, a többnemzetiségű társadalom feszültségeit és a kivándorlást, valamint a Nyugat és a kávéházi kultúra aranykorát."
        },
        {
            "type": "goal",
            "title": "Consolidation Goals",
            "items": [
                "A boldog békeidők kulcséveinek (1873, 1896, 1908) és technikai csúcsteljesítményeinek pontos ismerete",
                "Átváltozást, megemlékezést és társadalmi ellentéteket kifejező nyelvtani formák biztos alkalmazása",
                "A korszak történelmi személyiségeinek (Baross Gábor, Eötvös Loránd, Steindl Imre, feltalálók) felidézése"
            ]
        },
        {
            "type": "exercise-group",
            "title": "Comprehensive Unit 19 Practice",
            "ref": "ex.b1.monarchia.consolidation",
            "exerciseRefs": [e["id"] for e in cons_19_exs]
        },
        {
            "type": "checklist",
            "items": [
                "Tudom, mikor és hogyan egyesült Budapest (1873)",
                "Ismerem az 1896-os millenniumot és a kontinens első földalattiját",
                "Megértem a gazdasági és mérnöki sikereket (Ganz, MÁV, malomipar)",
                "Ismerem a kivándorlást, a Nyugatot (1908) és Eötvös Loránd ingáját"
            ]
        }
    ]
}
write_json(LESSONS_DIR / "lesson.b1.monarchia.consolidation.json", cons_19_lesson)


# ==============================================================================
# UNIT 20: WORLD WAR I & COLLAPSE (b1-vilaghaboru)
# ==============================================================================

# Lesson 1: Az első világháború kitörése (1914) és Tisza István
story_20_1 = make_story(
    "story.b1.vilaghaboru.01",
    "Az első világháború kitörése (1914) és Tisza István dilemmája",
    "1914. június 28-án a szarajevói merénylet kirobbantotta az első világháborút. Gróf Tisza István magyar miniszterelnök kezdetben ellenezte a hadba lépést, de a Monarchia végül hadat üzent Szerbiának.",
    "Szarajevó, Bécs és Budapest",
    ["Feltételességet, aggodalmat és hadüzenetet kifejező szerkezetek (ellenez, aggódik amiatt, hadat üzen)", "Outbreak of World War I, political dilemmas, and declarations of war"],
    ["szarajevói merénylet", "Tisza István", "hadüzenet", "központi hatalmak", "hátország"],
    [
        "1914. június 28-án Szarajevóban Gavrilo Princip szerb merénylő meggyilkolta Ferenc Ferdinánd trónörököst és feleségét. A Monarchia vezetése a háború mellett döntött, és ultimátumot intézett Szerbiához.",
        "Gróf Tisza István miniszterelnök kezdetben határozottan ellenezte a fegyveres konfliktust. Aggódott amiatt, hogy a háború Oroszország és Románia beavatkozásához vezethet, ami végzetes fenyegetést jelenthet a történelmi Magyarország épségére.",
        "Németország határozott biztatására és a közös minisztertanács nyomására Tisza végül feladta ellenállását. 1914. július 28-án a Monarchia hadat üzent Szerbiának, elindítva az emberiség addigi legvéresebb világégését."
    ],
    [
        {"lemma": "merénylet", "pos": "noun", "cefr": "B1", "gloss": "assassination, terrorist attack"},
        {"lemma": "hadüzenet", "pos": "noun", "cefr": "B1", "gloss": "declaration of war"},
        {"lemma": "ultimátum", "pos": "noun", "cefr": "B1", "gloss": "ultimatum"},
        {"lemma": "hadba lépés", "pos": "noun", "cefr": "B1", "gloss": "entry into war"},
        {"lemma": "világégés", "pos": "noun", "cefr": "B1", "gloss": "world conflagration, global war"}
    ],
    [
        {
            "question": "Melyik esemény robbantotta ki az első világháborút 1914 nyarán?",
            "options": ["A szarajevói merénylet (Ferenc Ferdinánd trónörökös meggyilkolása)", "A berlini fal megépítése", "A mohácsi csata", "Budapest ostroma"],
            "correctIndex": 0,
            "explanation": "A Ferenc Ferdinánd elleni 1914. június 28-i szarajevói merénylet indította el a konfliktust."
        }
    ]
)
write_json(STORIES_DIR / "story.b1.vilaghaboru.01.json", story_20_1)

voc_20_1 = {
    "id": "voc.b1.vilaghaboru.01",
    "title": "A világháború kitörésének szókincse",
    "description": "Merénylet, hadüzenet, ultimátum, hadba lépés és Tisza István.",
    "entries": [
        {"lemma": "merénylet", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "assassination attempt", "examples": [{"hu": "A szarajevói merénylet robbantotta ki a háborút.", "en": "The Sarajevo assassination triggered the war."}]}]},
        {"lemma": "hadüzenet", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "declaration of war", "examples": [{"hu": "A Monarchia hadüzenetet küldött Szerbiának.", "en": "The Monarchy sent a declaration of war to Serbia."}]}]},
        {"lemma": "hadba lépés", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "entry into active warfare", "examples": [{"hu": "Tisza István kezdetben ellenezte a hadba lépést.", "en": "István Tisza initially opposed the entry into war."}]}]},
        {"lemma": "ultimátum", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "final non-negotiable demand", "examples": [{"hu": "Bécs kemény ultimátumot adott a szerb kormánynak.", "en": "Vienna gave a harsh ultimatum to the Serbian government."}]}]},
        {"lemma": "világégés", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "destructive global war", "examples": [{"hu": "A háború négy évig tartó világégéssé vált.", "en": "The war became a four-year global conflagration."}]}]}
    ]
}
write_json(VOCAB_DIR / "voc.b1.vilaghaboru.01.json", voc_20_1)

gr_20_1 = {
    "id": "gr.b1.vilaghaboru.01",
    "title": "Aggodalmat és ellenzést kifejező vonzatok (aggódik amiatt, hogy; ellenzi a...-t)",
    "description": "Expressing apprehension, opposition, and geopolitical concerns with subordinating conjunctions.",
    "rules": [
        {
            "explanation": "Az 'aggódik amiatt, hogy...' és 'ellenzi, hogy...' összetett mondatokban a politikai döntések kockázatait és vitáit fejezzük ki.",
            "examples": [
                {"spanish": "Tisza István aggódott amiatt, hogy a Monarchia elbukhat.", "english": "István Tisza was worried that the Monarchy might fall."},
                {"spanish": "A miniszterelnök ellenezte az azonnali hadüzenetet.", "english": "The prime minister opposed the immediate declaration of war."}
            ]
        }
    ]
}
write_json(GRAMMAR_DIR / "gr.b1.vilaghaboru.01.json", gr_20_1)

exs_20_1 = [
    {"id": "ex.b1.vilaghaboru.01.01", "type": "multiple-choice", "lesson": "lesson.b1.vilaghaboru.01", "teaches": ["szarajevoi-merenylet-1914"], "prompt": "Mikor történt a szarajevói merénylet?", "options": ["1914. június 28-án", "1918. október 31-én", "1920. június 4-én", "1848. március 15-én"], "correctIndex": 0, "explanation": "1914. június 28-án gyilkolták meg Ferenc Ferdinándot."},
    {"id": "ex.b1.vilaghaboru.01.02", "type": "fill-blank", "lesson": "lesson.b1.vilaghaboru.01", "teaches": ["merenylet"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A szarajevói *merénylet* világméretű háborút robbantott ki.", "target": "merénylet"},
    {"id": "ex.b1.vilaghaboru.01.03", "type": "sentence-builder", "lesson": "lesson.b1.vilaghaboru.01", "teaches": ["Tisza-Istvan", "hadba-lepes"], "prompt": "Rakd össze a történelmi tényt!", "chips": ["Tisza", "István", "miniszterelnök", "kezdetben", "ellenezte", "a", "hadba", "lépést."], "target": "Tisza István miniszterelnök kezdetben ellenezte a hadba lépést.", "english": "Prime Minister István Tisza initially opposed entering the war."},
    {"id": "ex.b1.vilaghaboru.01.04", "type": "multiple-choice", "lesson": "lesson.b1.vilaghaboru.01", "teaches": ["haduzenat-Szerbia"], "prompt": "Kinek üzent hadat az Osztrák–Magyar Monarchia 1914. július 28-án?", "options": ["Szerbiának", "Angliának", "Franciaországnak", "Amerikának"], "correctIndex": 0, "explanation": "A Monarchia Szerbiának üzent hadat elsőként."},
    {"id": "ex.b1.vilaghaboru.01.05", "type": "fill-blank", "lesson": "lesson.b1.vilaghaboru.01", "teaches": ["haduzenet"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A bécsi udvar *hadüzenetet* küldött Belgrádba.", "target": "hadüzenetet"},
    {"id": "ex.b1.vilaghaboru.01.06", "type": "sentence-builder", "lesson": "lesson.b1.vilaghaboru.01", "teaches": ["aggodott", "veszely"], "prompt": "Alkoss szabályos alárendelő mondatot!", "chips": ["Tisza", "aggódott", "amiatt,", "hogy", "Magyarország", "veszélybe", "kerül."], "target": "Tisza aggódott amiatt, hogy Magyarország veszélybe kerül.", "english": "Tisza was worried that Hungary would be put in danger."},
    {"id": "ex.b1.vilaghaboru.01.07", "type": "multiple-choice", "lesson": "lesson.b1.vilaghaboru.01", "teaches": ["kozponti-hatalmak"], "prompt": "Melyik katonai szövetséghez tartozott Magyarország az első világháborúban?", "options": ["A Központi Hatalmakhoz (Németország, Monarchia, Oszmán Birodalom)", "Az Antanthoz (Nagy-Britannia, Franciaország, Oroszország)", "A Varsói Szerződéshez", "A NATO-hoz"], "correctIndex": 0, "explanation": "A Monarchia a Központi Hatalmak tagja volt Németországgal együtt."},
    {"id": "ex.b1.vilaghaboru.01.08", "type": "fill-blank", "lesson": "lesson.b1.vilaghaboru.01", "teaches": ["vilageges"], "prompt": "Egészítsd ki a mondatot!", "sentence": "Négy évig tombolt a pusztító *világégés*.", "target": "világégés"}
]
write_json(EXERCISES_DIR / "ex.b1.vilaghaboru.01.json", make_exercise_group("ex.b1.vilaghaboru.01", "Az első világháború kitörése gyakorlatok", "Gyakorlatok a szarajevói merényletről, Tisza Istvánról, a hadüzenetről és az aggodalmat kifejező szerkezetekről.", exs_20_1))

lesson_20_1 = make_lesson(
    "lesson.b1.vilaghaboru.01",
    "Az első világháború kitörése (1914) és Tisza István dilemmája",
    "Aggodalmat és ellenzést kifejező szerkezetek (aggódik amiatt, hogy; ellenzi)",
    "Ismerjük meg az első világháború kitörését (1914), a szarajevói merényletet és Tisza István miniszterelnök vívódását.",
    ["Tudni az 1914. június 28-i szarajevói merénylet történelmi tényét", "Ismerni Tisza István aggályait és a hadüzenet következményeit", "Használni az aggodalmat és elutasítást kifejező alárendelő mondatokat"],
    "story.b1.vilaghaboru.01",
    "voc.b1.vilaghaboru.01",
    "gr.b1.vilaghaboru.01",
    "ex.b1.vilaghaboru.01",
    [e["id"] for e in exs_20_1]
)
write_json(LESSONS_DIR / "lesson.b1.vilaghaboru.01.json", lesson_20_1)


# Lesson 2: Frontok, Doberdó és a hátország kimerülése
story_20_2 = make_story(
    "story.b1.vilaghaboru.02",
    "A frontok pokla: Doberdó, Isonzó és a hátország szenvedése",
    "Több mint 3,8 millió magyar katona küzdött a keleti és olasz frontokon, miközben a hátországban éhezés, jegyrendszer és hadi gazdálkodás nehezítette a mindennapi életet.",
    "Doberdó-fennsík és Budapest",
    ["Szenvedést, nélkülözést és kimerülést leíró kifejezések (nélkülöz, elesik a fronton, kimerül)", "Frontline battles, trench warfare, and home front hardships"],
    ["Doberdó", "Isonzó", "lövészárok", "jegyrendszer", "hadifogság"],
    [
        "A magyar honvédek rendkívüli bátorsággal harcoltak a Kárpátokban, a galíciai fronton és a dél-tiroli hegyekben. A legvéresebb ütközetek az olasz fronton, az Isonzó folyó mentén és a sziklás Doberdó-fennsíkon zajlottak, ahol százezrek vesztették életüket a gránáttűzben.",
        "A több évig elhúzódó állóháború kimerítette az országot. A hátországban bevezették a jegyrendszert: hiánycikk lett a kenyér, a liszt, a zsír és a szén. Nők és gyermekek dolgoztak a hadianyaggyárakban a fronton harcoló férfiak helyett.",
        "A háború végére több mint 660 ezer magyar katona esett el, több százezren sebesültek meg vagy kerültek szibériai hadifogságba, ami mérhetetlen társadalmi és emberi tragédiát okozott."
    ],
    [
        {"lemma": "lövészárok", "pos": "noun", "cefr": "B1", "gloss": "trench"},
        {"lemma": "hátország", "pos": "noun", "cefr": "B1", "gloss": "home front"},
        {"lemma": "jegyrendszer", "pos": "noun", "cefr": "B1", "gloss": "rationing system"},
        {"lemma": "hadifogság", "pos": "noun", "cefr": "B1", "gloss": "captivity as POW (prisoner of war)"},
        {"lemma": "nélkülözés", "pos": "noun", "cefr": "B1", "gloss": "privation, hardship, destitution"}
    ],
    [
        {
            "question": "Melyik olaszországi fennsík vált a magyar katonák hősies és tragikus harcának szimbólumává?",
            "options": ["A Doberdó-fennsík", "A Vezúv lejtője", "Az Alpok csúcsa", "A szicíliai part"],
            "correctIndex": 0,
            "explanation": "Doberdó és az Isonzó a magyar katonai helytállás és tragédia jelképe lett."
        }
    ]
)
write_json(STORIES_DIR / "story.b1.vilaghaboru.02.json", story_20_2)

voc_20_2 = {
    "id": "voc.b1.vilaghaboru.02",
    "title": "A front és a hátország szókincse",
    "description": "Lövészárok, hátország, jegyrendszer, hadifogság és Doberdó.",
    "entries": [
        {"lemma": "lövészárok", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "trench used in warfare", "examples": [{"hu": "A katonák hónapokat töltöttek a fagyos lövészárkokban.", "en": "Soldiers spent months in freezing trenches."}]}]},
        {"lemma": "hátország", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "civilian population and economy during war", "examples": [{"hu": "A hátország gazdaságilag teljesen kimerült.", "en": "The home front became economically exhausted."}]}]},
        {"lemma": "jegyrendszer", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "rationing system for food and fuel", "examples": [{"hu": "A kenyérre és zsiradékra jegyrendszert vezettek be.", "en": "A rationing system was introduced for bread and fat."}]}]},
        {"lemma": "hadifogság", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "captivity as prisoner of war", "examples": [{"hu": "Sokan csak évek múlva tértek haza a hadifogságból.", "en": "Many returned home from captivity only years later."}]}]},
        {"lemma": "nélkülözés", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "severe material privation and starvation", "examples": [{"hu": "A lakosság hősiesen viselte a nélkülözést.", "en": "The population heroically bore the privation."}]}]}
    ]
}
write_json(VOCAB_DIR / "voc.b1.vilaghaboru.02.json", voc_20_2)

gr_20_2 = {
    "id": "gr.b1.vilaghaboru.02",
    "title": "Szenvedő és állapotváltozást kifejező szerkezetek (kimerül, bevezetésre kerül, fogságba esik)",
    "description": "Expressing passive conditions, suffering, and exhaustion in historical narratives.",
    "rules": [
        {
            "explanation": "A történelmi veszteségek és háborús terhek leírására állapotváltozást és szenvedő értelmű körülírásokat használunk (fogságba kerül, bevezetik a jegyrendszert, kimerül).",
            "examples": [
                {"spanish": "Több százezer katona esett hadifogságba Oroszországban.", "english": "Hundreds of thousands of soldiers fell into captivity in Russia."},
                {"spanish": "A lakosság kimerült a hosszú évek nélkülözéseiben.", "english": "The population was exhausted by years of privation."}
            ]
        }
    ]
}
write_json(GRAMMAR_DIR / "gr.b1.vilaghaboru.02.json", gr_20_2)

exs_20_2 = [
    {"id": "ex.b1.vilaghaboru.02.01", "type": "multiple-choice", "lesson": "lesson.b1.vilaghaboru.02", "teaches": ["Doberdo-Isonzo"], "prompt": "Melyik folyó és fennsík mentén zajlottak a legvéresebb magyar vonatkozású harcok az olasz fronton?", "options": ["Az Isonzó folyó és a Doberdó-fennsík", "A Pó folyó", "A Rajna", "A Dnyeper"], "correctIndex": 0, "explanation": "Az Isonzó és Doberdó melletti csaták követelték a legnagyobb áldozatot."},
    {"id": "ex.b1.vilaghaboru.02.02", "type": "fill-blank", "lesson": "lesson.b1.vilaghaboru.02", "teaches": ["hatorszagban"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A *hátországban* súlyos élelmiszerhiány alakult ki.", "target": "hátországban"},
    {"id": "ex.b1.vilaghaboru.02.03", "type": "sentence-builder", "lesson": "lesson.b1.vilaghaboru.02", "teaches": ["jegyrendszer", "bevezet"], "prompt": "Rakd össze az ellátást leíró mondatot!", "chips": ["A", "kormány", "jegyrendszert", "vezetett", "be", "az", "élelmiszerekre."], "target": "A kormány jegyrendszert vezetett be az élelmiszerekre.", "english": "The government introduced a rationing system for food."},
    {"id": "ex.b1.vilaghaboru.02.04", "type": "multiple-choice", "lesson": "lesson.b1.vilaghaboru.02", "teaches": ["vesztesegek-szama"], "prompt": "Körülbelül hány magyar katona vesztette életét az első világháborúban?", "options": ["Több mint 660 ezer katona", "Körülbelül 5 ezer katona", "Tízmillió katona", "Kevesebb mint ezer katona"], "correctIndex": 0, "explanation": "Több mint 660 000 magyar katona esett el a harctereken."},
    {"id": "ex.b1.vilaghaboru.02.05", "type": "fill-blank", "lesson": "lesson.b1.vilaghaboru.02", "teaches": ["hadifogsagba"], "prompt": "Egészítsd ki a mondatot!", "sentence": "Százezer honvéd esett orosz *hadifogságba*.", "target": "hadifogságba"},
    {"id": "ex.b1.vilaghaboru.02.06", "type": "sentence-builder", "lesson": "lesson.b1.vilaghaboru.02", "teaches": ["katonak", "harcoltak"], "prompt": "Alkoss szabályos mondatot!", "chips": ["A", "magyar", "katonák", "hősiesen", "harcoltak", "a", "lövészárkokban."], "target": "A magyar katonák hősiesen harcoltak a lövészárkokban.", "english": "Hungarian soldiers fought heroically in the trenches."},
    {"id": "ex.b1.vilaghaboru.02.07", "type": "multiple-choice", "lesson": "lesson.b1.vilaghaboru.02", "teaches": ["haborus-kimerules"], "prompt": "Hogyan érintette a hosszú állóháború a magyar gazdaságot?", "options": ["Teljesen kimerítette az ipart, a mezőgazdaságot és a lakosságot", "Gyors gazdagodást hozott mindenkinek", "Megszüntette az adókat", "Nem volt semmilyen hatása"], "correctIndex": 0, "explanation": "A háború teljesen felélte az ország anyagi és emberi tartalékait."},
    {"id": "ex.b1.vilaghaboru.02.08", "type": "fill-blank", "lesson": "lesson.b1.vilaghaboru.02", "teaches": ["nelkulozest"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A lakosság nehezen viselte a mindennapi *nélkülözést*.", "target": "nélkülözést"}
]
write_json(EXERCISES_DIR / "ex.b1.vilaghaboru.02.json", make_exercise_group("ex.b1.vilaghaboru.02", "Frontok és hátország gyakorlatok", "Gyakorlatok a Doberdóról, a jegyrendszerről, a veszteségekről és a nélkülözés kifejezéséről.", exs_20_2))

lesson_20_2 = make_lesson(
    "lesson.b1.vilaghaboru.02",
    "A frontok pokla: Doberdó, Isonzó és a hátország szenvedése",
    "Szenvedést és állapotváltozást kifejező szerkezetek (fogságba esik, bevezetésre kerül)",
    "Tekintsük át a háború véres frontjait (Doberdó, Isonzó), a hátország jegyrendszerét és a súlyos emberáldozatokat.",
    ["Ismerni a doberdói és isonzói harcok szimbolikus jelentőségét", "Tudni a hátország kimerülését és a jegyrendszer bevezetését", "Használni a háborús nélkülözést és veszteségeket leíró nyelvtani formákat"],
    "story.b1.vilaghaboru.02",
    "voc.b1.vilaghaboru.02",
    "gr.b1.vilaghaboru.02",
    "ex.b1.vilaghaboru.02",
    [e["id"] for e in exs_20_2]
)
write_json(LESSONS_DIR / "lesson.b1.vilaghaboru.02.json", lesson_20_2)


# Lesson 3: 1918: Az Őszirózsás forradalom és a Monarchia felbomlása
story_20_3 = make_story(
    "story.b1.vilaghaboru.03",
    "Az Őszirózsás forradalom (1918) és az első köztársaság",
    "1918 őszén az Osztrák–Magyar Monarchia katonailag összeomlott. Október 31-én Budapesten kitört az Őszirózsás forradalom, IV. Károly király lemondott az államügyek intézéséről, és kikiáltották az első népköztársaságot.",
    "Budapest",
    ["Rendszerváltást, lemondást és kikiáltást kifejező igék (kikiált, lemond, összeomlik, hatalomra kerül)", "Collapse of the Monarchy, Aster Revolution, and proclamation of the Republic"],
    ["Őszirózsás forradalom", "Károlyi Mihály", "IV. Károly", "köztársaság", "fegyverszünet"],
    [
        "1918 októberének végére a Monarchia hadserege felbomlott, a birodalom nemzetiségei sorra kikiáltották függetlenségüket. Október 31-én a felkelt tömeg és a katonák őszirózsát tűztek a sapkájukra: győzött a vérontás nélküli Őszirózsás forradalom.",
        "A forradalom gróf Károlyi Mihályt juttatta a miniszterelnöki székbe. November 13-án az utolsó Habsburg uralkodó, IV. Károly eckartsaui nyilatkozatában visszavonult az államügyek gyakorlásától.",
        "1918. november 16-án az Országház előtt ünnepélyesen kikiáltották a független Magyar Népköztársaságot. A háborús vereség és a határok fenyegetettsége azonban súlyos válságba sodorta az új kormányt."
    ],
    [
        {"lemma": "őszirózsa", "pos": "noun", "cefr": "B1", "gloss": "autumn aster (flower, symbol of 1918 revolution)"},
        {"lemma": "köztársaság", "pos": "noun", "cefr": "B1", "gloss": "republic"},
        {"lemma": "kikiált", "pos": "verb", "cefr": "B1", "gloss": "to proclaim, declare (a republic)"},
        {"lemma": "lemond", "pos": "verb", "cefr": "B1", "gloss": "to resign, abdicate (the throne)"},
        {"lemma": "összeomlás", "pos": "noun", "cefr": "B1", "gloss": "collapse, disintegration"}
    ],
    [
        {
            "question": "Melyik virág lett az 1918. október 31-i budapesti forradalom szimbóluma?",
            "options": ["Az őszirózsa", "A vörös rózsa", "A tulipán", "A hóvirág"],
            "correctIndex": 0,
            "explanation": "A katonák őszirózsát tűztek a sapkájukra a sapkarózsa helyett."
        }
    ]
)
write_json(STORIES_DIR / "story.b1.vilaghaboru.03.json", story_20_3)

voc_20_3 = {
    "id": "voc.b1.vilaghaboru.03",
    "title": "Az Őszirózsás forradalom szókincse",
    "description": "Őszirózsa, köztársaság, kikiált, lemond és Károlyi Mihály.",
    "entries": [
        {"lemma": "őszirózsa", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "autumn flower, symbol of the 1918 Budapest revolution", "examples": [{"hu": "A katonák őszirózsát tűztek a sapkájukra.", "en": "Soldiers pinned asters onto their caps."}]}]},
        {"lemma": "köztársaság", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "republic form of government", "examples": [{"hu": "1918-ban kikiáltották a népköztársaságot.", "en": "In 1918, the people's republic was proclaimed."}]}]},
        {"lemma": "kikiált", "pos": "verb", "cefr": "B1", "definitions": [{"meaning": "to proclaim a new state or political form", "examples": [{"hu": "Ünnepélyesen kikiáltották a függetlenséget.", "en": "Independence was solemnly proclaimed."}]}]},
        {"lemma": "lemond", "pos": "verb", "cefr": "B1", "definitions": [{"meaning": "to step down from power or the throne", "examples": [{"hu": "IV. Károly lemondott az uralkodói jogokról.", "en": "Charles IV stepped down from ruling rights."}]}]},
        {"lemma": "összeomlás", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "total military and political breakdown", "examples": [{"hu": "A Monarchia összeomlása új határokat teremtett.", "en": "The collapse of the Monarchy created new borders."}]}]}
    ]
}
write_json(VOCAB_DIR / "voc.b1.vilaghaboru.03.json", voc_20_3)

gr_20_3 = {
    "id": "gr.b1.vilaghaboru.03",
    "title": "Politikai változást kifejező igék vonzatai (kikiált vmit vmivé, lemond vmiről)",
    "description": "Government verbs of declaration, abdication, and state transformations.",
    "rules": [
        {
            "explanation": "A politikai fordulatokat leíró igék sajátos vonzatokkal állnak: 'kikiált vmit vmivé' (kikiáltja a köztársaságot), 'lemond vmiről' (lemond a trónról).",
            "examples": [
                {"spanish": "1918-ban kikiáltották a köztársaságot.", "english": "In 1918 they proclaimed the republic."},
                {"spanish": "A király lemondott az államügyek intézéséről.", "english": "The king stepped down from conducting state affairs."}
            ]
        }
    ]
}
write_json(GRAMMAR_DIR / "gr.b1.vilaghaboru.03.json", gr_20_3)

exs_20_3 = [
    {"id": "ex.b1.vilaghaboru.03.01", "type": "multiple-choice", "lesson": "lesson.b1.vilaghaboru.03", "teaches": ["Oszirozsa-forradalom-datum"], "prompt": "Mikor győzött az Őszirózsás forradalom Budapesten?", "options": ["1918. október 31-én", "1914. június 28-án", "1920. június 4-én", "1848. március 15-én"], "correctIndex": 0, "explanation": "1918. október 31-én zajlott az Őszirózsás forradalom."},
    {"id": "ex.b1.vilaghaboru.03.02", "type": "fill-blank", "lesson": "lesson.b1.vilaghaboru.03", "teaches": ["koztarsasagot"], "prompt": "Egészítsd ki a mondatot!", "sentence": "Az Országház előtt kikiáltották a *köztársaságot*.", "target": "köztársaságot"},
    {"id": "ex.b1.vilaghaboru.03.03", "type": "sentence-builder", "lesson": "lesson.b1.vilaghaboru.03", "teaches": ["Karolyi-Mihaly", "kormanyfo"], "prompt": "Rakd össze a mondatot!", "chips": ["Gróf", "Károlyi", "Mihály", "lett", "az", "új", "kormány", "vezetője."], "target": "Gróf Károlyi Mihály lett az új kormány vezetője.", "english": "Count Mihály Károlyi became the leader of the new government."},
    {"id": "ex.b1.vilaghaboru.03.04", "type": "multiple-choice", "lesson": "lesson.b1.vilaghaboru.03", "teaches": ["IV-Karoly-lemondas"], "prompt": "Ki volt az utolsó magyar király (Habsburg uralkodó), aki 1918-ban lemondott az államügyek viteléről?", "options": ["IV. Károly", "Ferenc József", "I. Lipót", "Mária Terézia"], "correctIndex": 0, "explanation": "IV. Károly volt az utolsó megkoronázott magyar király."},
    {"id": "ex.b1.vilaghaboru.03.05", "type": "fill-blank", "lesson": "lesson.b1.vilaghaboru.03", "teaches": ["lemondott"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A király *lemondott* az uralkodói jogok gyakorlásáról.", "target": "lemondott"},
    {"id": "ex.b1.vilaghaboru.03.06", "type": "sentence-builder", "lesson": "lesson.b1.vilaghaboru.03", "teaches": ["Monarchia", "osszeomlott"], "prompt": "Alkoss szabályos történelmi mondatot!", "chips": ["A", "háború", "végén", "az", "Osztrák–Magyar", "Monarchia", "felbomlott", "és", "összeomlott."], "target": "A háború végén az Osztrák–Magyar Monarchia felbomlott és összeomlott.", "english": "At the end of the war, the Austro-Hungarian Monarchy disintegrated and collapsed."},
    {"id": "ex.b1.vilaghaboru.03.07", "type": "multiple-choice", "lesson": "lesson.b1.vilaghaboru.03", "teaches": ["fegyverszunet-1918"], "prompt": "Mit kötött a Monarchia küldöttsége Padovában 1918. november 3-án?", "options": ["Fegyverszünetet az antant hatalmakkal", "Új kereskedelmi szerződést", "Katonai szövetséget Oroszországgal", "Közös vámegyezményt"], "correctIndex": 0, "explanation": "1918. november 3-án írták alá a padovai fegyverszünetet."},
    {"id": "ex.b1.vilaghaboru.03.08", "type": "fill-blank", "lesson": "lesson.b1.vilaghaboru.03", "teaches": ["oszirozsat"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A katonák fehér *őszirózsát* tűztek a sapkájukra.", "target": "őszirózsát"}
]
write_json(EXERCISES_DIR / "ex.b1.vilaghaboru.03.json", make_exercise_group("ex.b1.vilaghaboru.03", "Az Őszirózsás forradalom gyakorlatok", "Gyakorlatok az 1918-as forradalomról, Károlyi Mihályról, IV. Károlyról és a politikai változás igéiről.", exs_20_3))

lesson_20_3 = make_lesson(
    "lesson.b1.vilaghaboru.03",
    "Az Őszirózsás forradalom (1918) és az első köztársaság",
    "Politikai változást kifejező szerkezetek (kikiált, lemond vmiről)",
    "Ismerjük meg az 1918. október 31-i Őszirózsás forradalmat, a Monarchia szétesését és az első köztársaságot.",
    ["Tudni az Őszirózsás forradalom (1918. okt. 31.) eseményeit és jelképét", "Ismerni Károlyi Mihály és IV. Károly szerepét az átmenetben", "Használni az államforma-váltást és lemondást leíró vonzatos igéket"],
    "story.b1.vilaghaboru.03",
    "voc.b1.vilaghaboru.03",
    "gr.b1.vilaghaboru.03",
    "ex.b1.vilaghaboru.03",
    [e["id"] for e in exs_20_3]
)
write_json(LESSONS_DIR / "lesson.b1.vilaghaboru.03.json", lesson_20_3)


# Lesson 4: 1919: A Tanácsköztársaság (133 nap) és a vörösterror
story_20_4 = make_story(
    "story.b1.vilaghaboru.04",
    "A Magyarországi Tanácsköztársaság (1919) és a vörösterror",
    "1919 tavaszán a kommunisták Kun Béla vezetésével átvették a hatalmat. A 133 napig tartó proletárdiktatúra államosításokat, vallásellenes intézkedéseket és vörösterrort hozott magával.",
    "Budapest",
    ["Diktatúrát, erőszakot és ideológiai kényszert kifejező igék (államosít, hatalmat ragad magához, elnyom)", "Soviet Republic 1919, red terror, nationalization, and communist dictatorship"],
    ["Tanácsköztársaság", "Kun Béla", "vörösterror", "Lenin-fiúk", "államosítás"],
    [
        "1919. március 21-én az antant újabb területi követelései (a Vix-jegyzék) miatt a Károlyi-kormány lemondott. A szociáldemokraták és kommunisták egyesülésével kikiáltották a Magyarországi Tanácsköztársaságot, amely szovjet mintájú proletárdiktatúrát vezetett be.",
        "A rendszer tényleges vezetője Kun Béla külügyi népbiztos volt. A tanácskormány minden magántulajdont, gyárat, bankot és földbirtokot államosított, bezáratta a felekezeti iskolákat, és fegyverrel lépett fel a vallásos hagyományok ellen.",
        "A belső elégedetlenség elfojtására Szamuely Tibor és a hírhedt 'Lenin-fiúk' különítményei vörösterrort alkalmaztak: több száz ártatlan embert végeztek ki bírósági ítélet nélkül a 133 napos rémuralom alatt."
    ],
    [
        {"lemma": "Tanácsköztársaság", "pos": "noun", "cefr": "B1", "gloss": "Soviet Republic (Hungarian Republic of Councils 1919)"},
        {"lemma": "proletárdiktatúra", "pos": "noun", "cefr": "B1", "gloss": "dictatorship of the proletariat"},
        {"lemma": "vörösterror", "pos": "noun", "cefr": "B1", "gloss": "Red Terror (executions by Bolshevik detachments)"},
        {"lemma": "államosítás", "pos": "noun", "cefr": "B1", "gloss": "nationalization, confiscation by state"},
        {"lemma": "népbiztos", "pos": "noun", "cefr": "B1", "gloss": "people's commissar (minister in 1919)"}
    ],
    [
        {
            "question": "Hány napig tartott a Magyarországi Tanácsköztársaság diktatúrája 1919-ben?",
            "options": ["133 napig", "30 napig", "Egy évig", "Ötszáz napig"],
            "correctIndex": 0,
            "explanation": "A Tanácsköztársaság 1919. március 21-től augusztus 1-ig, pontosan 133 napig állt fenn."
        }
    ]
)
write_json(STORIES_DIR / "story.b1.vilaghaboru.04.json", story_20_4)

voc_20_4 = {
    "id": "voc.b1.vilaghaboru.04",
    "title": "A Tanácsköztársaság és terror szókincse",
    "description": "Tanácsköztársaság, vörösterror, államosítás, népbiztos és Kun Béla.",
    "entries": [
        {"lemma": "Tanácsköztársaság", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "1919 Bolshevik Soviet Republic in Hungary", "examples": [{"hu": "A Tanácsköztársaság 133 napig tartott.", "en": "The Soviet Republic lasted for 133 days."}]}]},
        {"lemma": "vörösterror", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "Bolshevik violent terror against political opponents", "examples": [{"hu": "A vörösterror százak halálát okozta.", "en": "The Red Terror caused the deaths of hundreds."}]}]},
        {"lemma": "államosítás", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "state confiscation of private enterprises and land", "examples": [{"hu": "A kommunisták azonnali államosítást rendeltek el.", "en": "The communists ordered immediate nationalization."}]}]},
        {"lemma": "népbiztos", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "commissar, government leader in 1919", "examples": [{"hu": "Kun Béla külügyi népbiztos volt a tényleges vezető.", "en": "Béla Kun, people's commissar for foreign affairs, was the actual leader."}]}]},
        {"lemma": "proletárdiktatúra", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "dictatorship of the working class / communist party", "examples": [{"hu": "A proletárdiktatúra eltörölte a polgári szabadságjogokat.", "en": "The dictatorship of the proletariat abolished civil liberties."}]}]}
    ]
}
write_json(VOCAB_DIR / "voc.b1.vilaghaboru.04.json", voc_20_4)

gr_20_4 = {
    "id": "gr.b1.vilaghaboru.04",
    "title": "Kényszert és erőszakos beavatkozást kifejező igék (elrendel, elkoboz, államosít, felszámol)",
    "description": "Expressing dictatorial measures, coercive state actions, and expropriation.",
    "rules": [
        {
            "explanation": "Diktatúrák és önkényuralmi rendszerek intézkedéseit leíró igék: 'államosít', 'elrendel', 'megtilt', 'felszámol', 'kivégez'.",
            "examples": [
                {"spanish": "A tanácskormány elrendelte a magántulajdon államosítását.", "english": "The council government ordered the nationalization of private property."},
                {"spanish": "A terrorcsapatok bírósági ítélet nélkül végeztek ki embereket.", "english": "The terror detachments executed people without court verdicts."}
            ]
        }
    ]
}
write_json(GRAMMAR_DIR / "gr.b1.vilaghaboru.04.json", gr_20_4)

exs_20_4 = [
    {"id": "ex.b1.vilaghaboru.04.01", "type": "multiple-choice", "lesson": "lesson.b1.vilaghaboru.04", "teaches": ["Tanacskoztarsasag-Kun-Bela"], "prompt": "Ki volt az 1919-es Magyarországi Tanácsköztársaság tényleges vezetője?", "options": ["Kun Béla", "Károlyi Mihály", "Tisza István", "Horthy Miklós"], "correctIndex": 0, "explanation": "Kun Béla külügyi népbiztos irányította a diktatúrát."},
    {"id": "ex.b1.vilaghaboru.04.02", "type": "fill-blank", "lesson": "lesson.b1.vilaghaboru.04", "teaches": ["allamositast"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A tanácskormány elrendelte a magánvagyonok *államosítását*.", "target": "államosítását"},
    {"id": "ex.b1.vilaghaboru.04.03", "type": "sentence-builder", "lesson": "lesson.b1.vilaghaboru.04", "teaches": ["Tanacskoztarsasag", "nap"], "prompt": "Rakd össze az időtartamot kifejező mondatot!", "chips": ["A", "Tanácsköztársaság", "összesen", "133", "napig", "volt", "hatalmon."], "target": "A Tanácsköztársaság összesen 133 napig volt hatalmon.", "english": "The Soviet Republic was in power for a total of 133 days."},
    {"id": "ex.b1.vilaghaboru.04.04", "type": "multiple-choice", "lesson": "lesson.b1.vilaghaboru.04", "teaches": ["vorosterror-Lenin-fiuk"], "prompt": "Hogyan nevezték a Tanácsköztársaság alatt működő hírhedt fegyveres terrorkülönítményt?", "options": ["A 'Lenin-fiúknak'", "A 'Bach-huszároknak'", "A 'kurucoknak'", "A 'fekete seregnek'"], "correctIndex": 0, "explanation": "A Lenin-fiúk Szamuely Tibor vezetésével hajtották végre a vörösterrort."},
    {"id": "ex.b1.vilaghaboru.04.05", "type": "fill-blank", "lesson": "lesson.b1.vilaghaboru.04", "teaches": ["vorosterror"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A *vörösterror* megfélemlítette a lakosságot.", "target": "vörösterror"},
    {"id": "ex.b1.vilaghaboru.04.06", "type": "sentence-builder", "lesson": "lesson.b1.vilaghaboru.04", "teaches": ["nepbiztosok", "rendeletek"], "prompt": "Alkoss szabályos mondatot!", "chips": ["A", "népbiztosok", "diktatórikus", "rendeletekkel", "irányították", "az", "országot."], "target": "A népbiztosok diktatórikus rendeletekkel irányították az országot.", "english": "The people's commissars governed the country with dictatorial decrees."},
    {"id": "ex.b1.vilaghaboru.04.07", "type": "multiple-choice", "lesson": "lesson.b1.vilaghaboru.04", "teaches": ["magantulajdon-elvetel"], "prompt": "Milyen gazdasági intézkedést hozott a Tanácsköztársaság?", "options": ["Minden magántulajdont, gyárat és földet állami kézbe vett", "Csökkentette az adókat és szabadpiacot vezetett be", "Mindenkinek ingyen földet osztott", "Visszaállította a nemesi birtokokat"], "correctIndex": 0, "explanation": "A bolsevik vezetés mindent államosított."},
    {"id": "ex.b1.vilaghaboru.04.08", "type": "fill-blank", "lesson": "lesson.b1.vilaghaboru.04", "teaches": ["proletardiktatura"], "prompt": "Egészítsd ki a mondatot!", "sentence": "Szovjet típusú *proletárdiktatúra* jött létre.", "target": "proletárdiktatúra"}
]
write_json(EXERCISES_DIR / "ex.b1.vilaghaboru.04.json", make_exercise_group("ex.b1.vilaghaboru.04", "A Tanácsköztársaság gyakorlatok", "Gyakorlatok az 1919-es Tanácsköztársaságról, Kun Béláról, a vörösterrorról és a kényszert kifejező igékről.", exs_20_4))

lesson_20_4 = make_lesson(
    "lesson.b1.vilaghaboru.04",
    "A Magyarországi Tanácsköztársaság (1919) és a vörösterror",
    "Kényszert és önkényuralmi intézkedéseket kifejező szerkezetek (államosít, elrendel)",
    "Ismerjük meg az 1919-es 133 napos Tanácsköztársaságot, az államosításokat és a vörösterror eseményeit.",
    ["Tudni a Tanácsköztársaság (1919. márc. 21. – aug. 1., 133 nap) létrejöttét", "Ismerni Kun Béla szerepét, az államosításokat és a vörösterror áldozatait", "Használni a diktatúrát és erőszakos hatalomgyakorlást leíró igéket"],
    "story.b1.vilaghaboru.04",
    "voc.b1.vilaghaboru.04",
    "gr.b1.vilaghaboru.04",
    "ex.b1.vilaghaboru.04",
    [e["id"] for e in exs_20_4]
)
write_json(LESSONS_DIR / "lesson.b1.vilaghaboru.04.json", lesson_20_4)


# Lesson 5: Román megszállás és a Nemzeti Hadsereg: Horthy bevonulása
story_20_5 = make_story(
    "story.b1.vilaghaboru.05",
    "Román megszállás és Horthy Miklós bevonulása Budapestre (1919)",
    "1919 augusztusában a Tanácsköztársaság megbukott a román királyi hadsereg támadása alatt, amely megszállta és kifosztotta Budapestet. November 16-án Horthy Miklós a Nemzeti Hadsereg élén bevonult a fővárosba.",
    "Gellért Szálló és Budapest",
    ["Megszállást, felszabadulást és rendteremtést kifejező szerkezetek (megszáll, bevonul az élén, rendet teremt)", "Romanian occupation, pillaging, National Army, and Horthy's entry into Budapest"],
    ["román megszállás", "Nemzeti Hadsereg", "Horthy Miklós", "bevonulás", "fehérterror"],
    [
        "1919. augusztus elején a román csapatok behatoltak Budapestre. A román katonai megszállás hónapjaiban gyárak gépeit, vasúti mozdonyokat, műkincseket és élelmiszerkészleteket vagonok ezrein szállítottak el Magyarországról.",
        "Eközben Szegeden megszerveződött az antikommunista Nemzeti Hadsereg, amelynek fővezére Horthy Miklós, az Osztrák–Magyar Monarchia egykori flottaparancsnoka lett. A hadsereg egyes különítményei brutális leszámolást, 'fehérterrort' folytattak a kommunista gyanúsítottakkal szemben a Dunántúlon és az Alföldön.",
        "Az antant nyomására a románok november közepén kivonultak a fővárosból. 1919. november 16-án Horthy Miklós fehér lovon lovagolva bevonult Budapestre, megkezdve az új korszak konszolidációját."
    ],
    [
        {"lemma": "megszállás", "pos": "noun", "cefr": "B1", "gloss": "military occupation"},
        {"lemma": "Nemzeti Hadsereg", "pos": "noun", "cefr": "B1", "gloss": "National Army formed in Szeged"},
        {"lemma": "bevonulás", "pos": "noun", "cefr": "B1", "gloss": "entry, ceremonial military marching in"},
        {"lemma": "fehérterror", "pos": "noun", "cefr": "B1", "gloss": "White Terror (reprisals against communists)"},
        {"lemma": "fővezér", "pos": "noun", "cefr": "B1", "gloss": "commander-in-chief"}
    ],
    [
        {
            "question": "Melyik évben és napon vonult be Horthy Miklós a Nemzeti Hadsereg élén Budapestre?",
            "options": ["1919. november 16-án", "1914. június 28-án", "1920. június 4-én", "1918. október 31-én"],
            "correctIndex": 0,
            "explanation": "Horthy Miklós 1919. november 16-án vonult be a fővárosba."
        }
    ]
)
write_json(STORIES_DIR / "story.b1.vilaghaboru.05.json", story_20_5)

voc_20_5 = {
    "id": "voc.b1.vilaghaboru.05",
    "title": "A megszállás és bevonulás szókincse",
    "description": "Megszállás, Nemzeti Hadsereg, Horthy Miklós, bevonulás és fehérterror.",
    "entries": [
        {"lemma": "megszállás", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "foreign military occupation", "examples": [{"hu": "A román hadsereg hónapokig tartotta megszállva Budapestet.", "en": "The Romanian army occupied Budapest for months."}]}]},
        {"lemma": "Nemzeti Hadsereg", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "anti-communist military force founded in Szeged in 1919", "examples": [{"hu": "A Nemzeti Hadsereg élén Horthy Miklós állt.", "en": "Miklós Horthy stood at the head of the National Army."}]}]},
        {"lemma": "bevonulás", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "ceremonial entry into a city", "examples": [{"hu": "A budapesti bevonulás új politikai korszakot nyitott.", "en": "The entry into Budapest opened a new political era."}]}]},
        {"lemma": "fehérterror", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "right-wing reprisal violence following the collapse of the Soviet Republic", "examples": [{"hu": "A fehérterror különítményei megtorlásokat hajtottak végre.", "en": "The detachments of the White Terror carried out reprisals."}]}]},
        {"lemma": "fővezér", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "supreme military commander", "examples": [{"hu": "Horthy Miklóst választották meg a hadsereg fővezérének.", "en": "Miklós Horthy was chosen supreme commander of the army."}]}]}
    ]
}
write_json(VOCAB_DIR / "voc.b1.vilaghaboru.05.json", voc_20_5)

gr_20_5 = {
    "id": "gr.b1.vilaghaboru.05",
    "title": "Helyváltoztatást és vezetést kifejező szerkezetek (élén vonul be, kivonul vhonnan)",
    "description": "Spatial and leadership verbal expressions in military and historical movements.",
    "rules": [
        {
            "explanation": "Katonai és politikai események leírásakor az 'élén áll', 'élén vonul be', 'kivonul vhonnan' kifejezéseket használjuk a vezetés és mozgás bemutatására.",
            "examples": [
                {"spanish": "Horthy Miklós a hadsereg élén vonult be a fővárosba.", "english": "Miklós Horthy marched into the capital at the head of the army."},
                {"spanish": "A megszálló csapatok kivonultak Budapestről.", "english": "The occupying troops withdrew from Budapest."}
            ]
        }
    ]
}
write_json(GRAMMAR_DIR / "gr.b1.vilaghaboru.05.json", gr_20_5)

exs_20_5 = [
    {"id": "ex.b1.vilaghaboru.05.01", "type": "multiple-choice", "lesson": "lesson.b1.vilaghaboru.05", "teaches": ["Horthy-bevonulas-1919"], "prompt": "Mikor vonult be Horthy Miklós a Nemzeti Hadsereg élén Budapestre?", "options": ["1919. november 16-án", "1914. augusztus 1-jén", "1920. június 4-én", "1918. október 31-én"], "correctIndex": 0, "explanation": "Horthy Miklós 1919. november 16-án vonult be a Gellért téren át Budapestre."},
    {"id": "ex.b1.vilaghaboru.05.02", "type": "fill-blank", "lesson": "lesson.b1.vilaghaboru.05", "teaches": ["bevonulas"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A budapesti *bevonulás* véget vetett az 1919-es káosznak.", "target": "bevonulás"},
    {"id": "ex.b1.vilaghaboru.05.03", "type": "sentence-builder", "lesson": "lesson.b1.vilaghaboru.05", "teaches": ["elen", "bevonult"], "prompt": "Rakd össze a mondatot!", "chips": ["Horthy", "Miklós", "a", "Nemzeti", "Hadsereg", "élén", "bevonult", "Budapestre."], "target": "Horthy Miklós a Nemzeti Hadsereg élén bevonult Budapestre.", "english": "Miklós Horthy marched into Budapest at the head of the National Army."},
    {"id": "ex.b1.vilaghaboru.05.04", "type": "multiple-choice", "lesson": "lesson.b1.vilaghaboru.05", "teaches": ["roman-megszallas-1919"], "prompt": "Melyik szomszédos ország hadserege szállta meg Budapestet 1919 augusztusa és novembere között?", "options": ["A román királyi hadsereg", "Az osztrák rendőrség", "A lengyel hadsereg", "A svájci gárda"], "correctIndex": 0, "explanation": "A román hadsereg tartotta megszállva Budapestet."},
    {"id": "ex.b1.vilaghaboru.05.05", "type": "fill-blank", "lesson": "lesson.b1.vilaghaboru.05", "teaches": ["megszallas"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A román katonai *megszállás* súlyos károkat okozott.", "target": "megszállás"},
    {"id": "ex.b1.vilaghaboru.05.06", "type": "sentence-builder", "lesson": "lesson.b1.vilaghaboru.05", "teaches": ["fovezer", "flottaparancsnok"], "prompt": "Alkoss szabályos összetett mondatot!", "chips": ["Horthy", "Miklós", "korábban", "az", "Osztrák–Magyar", "Monarchia", "flottaparancsnoka", "volt."], "target": "Horthy Miklós korábban az Osztrák–Magyar Monarchia flottaparancsnoka volt.", "english": "Miklós Horthy had previously been the fleet commander of the Austro-Hungarian Monarchy."},
    {"id": "ex.b1.vilaghaboru.05.07", "type": "multiple-choice", "lesson": "lesson.b1.vilaghaboru.05", "teaches": ["feherterror-fogalom"], "prompt": "Mit jelent a 'fehérterror' fogalma 1919–1920-ban?", "options": ["A Tanácsköztársaság bukása utáni antikommunista megtorlásokat a tisztikülönítmények részéről", "Téli havazást", "Egy orvosi kifejezést", "A parlament feloszlatását"], "correctIndex": 0, "explanation": "A fehérterror a kommunistákkal és baloldaliakkal szembeni fegyveres megtorlás volt."},
    {"id": "ex.b1.vilaghaboru.05.08", "type": "fill-blank", "lesson": "lesson.b1.vilaghaboru.05", "teaches": ["feherterror"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A vidéken tomboló *fehérterror* sok áldozatot követelt.", "target": "fehérterror"}
]
write_json(EXERCISES_DIR / "ex.b1.vilaghaboru.05.json", make_exercise_group("ex.b1.vilaghaboru.05", "Megszállás és bevonulás gyakorlatok", "Gyakorlatok a román megszállásról, Horthy Miklós 1919-es bevonulásáról és a vezetést kifejező szerkezetekről.", exs_20_5))

lesson_20_5 = make_lesson(
    "lesson.b1.vilaghaboru.05",
    "Román megszállás és Horthy Miklós bevonulása Budapestre (1919)",
    "Helyváltoztatást és vezetést kifejező szerkezetek (élén bevonul, megszáll)",
    "Tekintsük át a román megszállás nehéz hónapjait és Horthy Miklós 1919. november 16-i budapesti bevonulását.",
    ["Ismerni a román megszállás (1919) történelmi körülményeit", "Tudni Horthy Miklós budapesti bevonulásának dátumát (1919. nov. 16.)", "Használni a katonai és állami mozgásokat kifejező kifejezéseket"],
    "story.b1.vilaghaboru.05",
    "voc.b1.vilaghaboru.05",
    "gr.b1.vilaghaboru.05",
    "ex.b1.vilaghaboru.05",
    [e["id"] for e in exs_20_5]
)
write_json(LESSONS_DIR / "lesson.b1.vilaghaboru.05.json", lesson_20_5)


# Unit 20 Consolidation
cons_20_exs = [
    {"id": "ex.b1.vilaghaboru.cons.01", "type": "multiple-choice", "lesson": "lesson.b1.vilaghaboru.consolidation", "teaches": ["szarajevoi-merenylet-1914"], "prompt": "Melyik évben robbant ki az első világháború a szarajevói merénylet után?", "options": ["1914-ben", "1918-ban", "1920-ban", "1848-ban"], "correctIndex": 0, "explanation": "1914-ben robbant ki az I. világháború."},
    {"id": "ex.b1.vilaghaboru.cons.02", "type": "fill-blank", "lesson": "lesson.b1.vilaghaboru.consolidation", "teaches": ["Tisza-Istvan"], "prompt": "Gróf *Tisza István* miniszterelnök kezdetben aggódott a hadba lépés miatt.", "sentence": "Gróf *Tisza István* miniszterelnök kezdetben aggódott a hadba lépés miatt.", "target": "Tisza István"},
    {"id": "ex.b1.vilaghaboru.cons.03", "type": "multiple-choice", "lesson": "lesson.b1.vilaghaboru.consolidation", "teaches": ["Doberdo-harcok"], "prompt": "Melyik fennsík vált a magyar honvédek hősies és tragikus harcának jelképévé az olasz fronton?", "options": ["A Doberdó-fennsík", "A Mátrában", "A Tátrában", "A Hortobágyon"], "correctIndex": 0, "explanation": "A Doberdó az I. világháborús áldozatok szimbóluma."},
    {"id": "ex.b1.vilaghaboru.cons.04", "type": "fill-blank", "lesson": "lesson.b1.vilaghaboru.consolidation", "teaches": ["jegyrendszert"], "prompt": "A háborús hátországban *jegyrendszert* vezettek be az élelmiszerekre.", "sentence": "A háborús hátországban *jegyrendszert* vezettek be az élelmiszerekre.", "target": "jegyrendszert"},
    {"id": "ex.b1.vilaghaboru.cons.05", "type": "sentence-builder", "lesson": "lesson.b1.vilaghaboru.consolidation", "teaches": ["Oszirozsa", "forradalom"], "prompt": "Rakd össze a forradalomról szóló mondatot!", "chips": ["1918.", "október", "31-én", "kitört", "az", "Őszirózsás", "forradalom."], "target": "1918. október 31-én kitört az Őszirózsás forradalom.", "english": "On October 31, 1918, the Aster Revolution broke out."},
    {"id": "ex.b1.vilaghaboru.cons.06", "type": "multiple-choice", "lesson": "lesson.b1.vilaghaboru.consolidation", "teaches": ["Karolyi-Mihaly-koztarsasag"], "prompt": "Ki lett a miniszterelnök, majd az első köztársasági elnök az Őszirózsás forradalom után?", "options": ["Károlyi Mihály", "Kun Béla", "Horthy Miklós", "Tisza István"], "correctIndex": 0, "explanation": "Károlyi Mihály vezette az 1918-as kormányt."},
    {"id": "ex.b1.vilaghaboru.cons.07", "type": "fill-blank", "lesson": "lesson.b1.vilaghaboru.consolidation", "teaches": ["IV-Karoly"], "prompt": "Az utolsó magyar király *IV. Károly* volt, aki 1918-ban visszavonult az államügyektől.", "sentence": "Az utolsó magyar király *IV. Károly* volt, aki 1918-ban visszavonult az államügyektől.", "target": "IV. Károly"},
    {"id": "ex.b1.vilaghaboru.cons.08", "type": "sentence-builder", "lesson": "lesson.b1.vilaghaboru.consolidation", "teaches": ["Tanacskoztarsasag", "allamositas"], "prompt": "Alkoss szabályos történelmi mondatot!", "chips": ["A", "Tanácsköztársaság", "elrendelte", "az", "üzemek", "és", "földek", "államosítását."], "target": "A Tanácsköztársaság elrendelte az üzemek és földek államosítását.", "english": "The Soviet Republic ordered the nationalization of factories and lands."},
    {"id": "ex.b1.vilaghaboru.cons.09", "type": "multiple-choice", "lesson": "lesson.b1.vilaghaboru.consolidation", "teaches": ["Tanacskoztarsasag-napok"], "prompt": "Hány napig állt fenn a Tanácsköztársaság 1919-ben?", "options": ["133 napig", "365 napig", "48 napig", "600 napig"], "correctIndex": 0, "explanation": "A Tanácsköztársaság 133 napig tartott."},
    {"id": "ex.b1.vilaghaboru.cons.10", "type": "fill-blank", "lesson": "lesson.b1.vilaghaboru.consolidation", "teaches": ["Kun-Bela"], "prompt": "A Tanácsköztársaság külügyi népbiztosa és tényleges vezetője *Kun Béla* volt.", "sentence": "A Tanácsköztársaság külügyi népbiztosa és tényleges vezetője *Kun Béla* volt.", "target": "Kun Béla"},
    {"id": "ex.b1.vilaghaboru.cons.11", "type": "sentence-builder", "lesson": "lesson.b1.vilaghaboru.consolidation", "teaches": ["vorosterror", "aldozatok"], "prompt": "Rakd össze a mondatot!", "chips": ["A", "vörösterror", "különítményei", "sok", "ártatlan", "áldozatot", "követeltek."], "target": "A vörösterror különítményei sok ártatlan áldozatot követeltek.", "english": "The detachments of the Red Terror claimed many innocent victims."},
    {"id": "ex.b1.vilaghaboru.cons.12", "type": "multiple-choice", "lesson": "lesson.b1.vilaghaboru.consolidation", "teaches": ["roman-megszallas-1919"], "prompt": "Melyik hadsereg szállta meg Budapestet 1919 augusztusában a Tanácsköztársaság bukása után?", "options": ["A román hadsereg", "A francia flotta", "Az angol sereg", "A török haderő"], "correctIndex": 0, "explanation": "A román hadsereg vonult be Budapestre."},
    {"id": "ex.b1.vilaghaboru.cons.13", "type": "fill-blank", "lesson": "lesson.b1.vilaghaboru.consolidation", "teaches": ["Nemzeti-Hadsereg"], "prompt": "Horthy Miklós a szegedi *Nemzeti Hadsereg* fővezére volt.", "sentence": "Horthy Miklós a szegedi *Nemzeti Hadsereg* fővezére volt.", "target": "Nemzeti Hadsereg"},
    {"id": "ex.b1.vilaghaboru.cons.14", "type": "sentence-builder", "lesson": "lesson.b1.vilaghaboru.consolidation", "teaches": ["Horthy", "bevonult"], "prompt": "Alkoss szabályos összetett mondatot!", "chips": ["1919.", "november", "16-án", "Horthy", "Miklós", "bevonult", "Budapestre."], "target": "1919. november 16-án Horthy Miklós bevonult Budapestre.", "english": "On November 16, 1919, Miklós Horthy marched into Budapest."},
    {"id": "ex.b1.vilaghaboru.cons.15", "type": "multiple-choice", "lesson": "lesson.b1.vilaghaboru.consolidation", "teaches": ["vesztesegek-katonak"], "prompt": "Körülbelül hány magyar honvéd esett el az I. világháborúban?", "options": ["Több mint 660 ezer", "Körülbelül 20 ezer", " egymillió ötszázezer", "Alig kétszáz"], "correctIndex": 0, "explanation": "Több mint 660 ezer magyar katona vesztette életét."},
    {"id": "ex.b1.vilaghaboru.cons.16", "type": "fill-blank", "lesson": "lesson.b1.vilaghaboru.consolidation", "teaches": ["hadifogsagba"], "prompt": "A harcok során százezrek kerültek szibériai *hadifogságba*.", "sentence": "A harcok során százezrek kerültek szibériai *hadifogságba*.", "target": "hadifogságba"},
    {"id": "ex.b1.vilaghaboru.cons.17", "type": "sentence-builder", "lesson": "lesson.b1.vilaghaboru.consolidation", "teaches": ["Monarchia", "szetesett"], "prompt": "Rakd össze az állítást!", "chips": ["Az", "első", "világháború", "végén", "felbomlott", "az", "Osztrák–Magyar", "Monarchia."], "target": "Az első világháború végén felbomlott az Osztrák–Magyar Monarchia.", "english": "At the end of World War I, the Austro-Hungarian Monarchy disintegrated."},
    {"id": "ex.b1.vilaghaboru.cons.18", "type": "multiple-choice", "lesson": "lesson.b1.vilaghaboru.consolidation", "teaches": ["feherterror-tisztikülonitmeny"], "prompt": "Mi követte a Tanácsköztársaság bukását 1919 őszén a tisztikülönítmények részéről?", "options": ["A fehérterror megtorlásai", "Azonnali általános választások", "A jobbágyság visszaállítása", "Békekötés minden szomszéddal"], "correctIndex": 0, "explanation": "A fehérterror során fegyveres különítmények üldözték a baloldaliakat."},
    {"id": "ex.b1.vilaghaboru.cons.19", "type": "fill-blank", "lesson": "lesson.b1.vilaghaboru.consolidation", "teaches": ["oszirozsat"], "prompt": "1918-ban a forradalmárok *őszirózsát* viseltek a kabátjukon.", "sentence": "1918-ban a forradalmárok *őszirózsát* viseltek a kabátjukon.", "target": "őszirózsát"},
    {"id": "ex.b1.vilaghaboru.cons.20", "type": "multiple-choice", "lesson": "lesson.b1.vilaghaboru.consolidation", "teaches": ["1914-1919-osszegzes"], "prompt": "Milyen korszakos következményekkel járt az 1914 és 1919 közötti időszak Magyarország számára?", "options": ["A Monarchia szétesésével, súlyos emberáldozatokkal, forradalmakkal és a trianoni béke előkészítésével", "Teljes gazdasági meggazdagodással és a birodalom kiterjesztésével", "A monarchikus határok sértetlenségével", "A fegyverkezés teljes eltörlésével Európában"], "correctIndex": 0, "explanation": "A háború és az 1918–19-es válság vezetett a történelmi Magyarország felbomlásához."}
]
write_json(EXERCISES_DIR / "ex.b1.vilaghaboru.consolidation.json", make_exercise_group("ex.b1.vilaghaboru.consolidation", "Az I. világháború és összeomlás összefoglaló", "Átfogó teszt 1914–1919 eseményeiről: a háborúról, Doberdóról, 1918-ról, a Tanácsköztársaságról és 1919-ről.", cons_20_exs))

cons_20_lesson = {
    "id": "lesson.b1.vilaghaboru.consolidation",
    "title": "World War I & Collapse: Unit 20 Consolidation",
    "level": "B1",
    "track": "citizenship",
    "estimatedMinutes": 25,
    "prerequisites": [
        "lesson.b1.vilaghaboru.01",
        "lesson.b1.vilaghaboru.02",
        "lesson.b1.vilaghaboru.03",
        "lesson.b1.vilaghaboru.04",
        "lesson.b1.vilaghaboru.05"
    ],
    "grammar": ["Unit review"],
    "vocabulary": ["Unit review"],
    "culturalContext": "Magyar történelem összefoglalás (Honosítási vizsgafelkészítő)",
    "sections": [
        {
            "type": "intro",
            "title": "Unit 20 Consolidation: World War I & Collapse (1914–1919)",
            "body": "Ebben az összefoglaló leckében áttekintjük az első világháború kitörését (1914. jún. 28., szarajevói merénylet), a frontok véres harcait (Doberdó, Isonzó), a hátország kimerülését, az 1918. október 31-i Őszirózsás forradalmat, a 133 napos Tanácsköztársaságot (1919), valamint a román megszállást és Horthy Miklós 1919. november 16-i bevonulását."
        },
        {
            "type": "goal",
            "title": "Consolidation Goals",
            "items": [
                "Az 1914–1919 közötti időszak sorsdöntő dátumainak és fordulópontjainak biztos ismerete",
                "Aggodalmat, politikai átalakulást és katonai eseményeket leíró nyelvtani szerkezetek helyes alkalmazása",
                "A korszak vezető politikai és katonai szereplőinek (Tisza István, Károlyi Mihály, Kun Béla, Horthy Miklós) felidézése"
            ]
        },
        {
            "type": "exercise-group",
            "title": "Comprehensive Unit 20 Practice",
            "ref": "ex.b1.vilaghaboru.consolidation",
            "exerciseRefs": [e["id"] for e in cons_20_exs]
        },
        {
            "type": "checklist",
            "items": [
                "Tudom, hogyan robbant ki az I. világháború és mit jelent Doberdó",
                "Ismerem az 1918-as Őszirózsás forradalmat és IV. Károly lemondását",
                "Megértem a Tanácsköztársaság (133 nap) és a vörösterror jellegét",
                "Tudom a román megszállás és Horthy 1919-es bevonulásának körülményeit"
            ]
        }
    ]
}
write_json(LESSONS_DIR / "lesson.b1.vilaghaboru.consolidation.json", cons_20_lesson)


# ==============================================================================
# UNIT 21: THE TREATY OF TRIANON 1920 (b1-trianon)
# ==============================================================================

# Lesson 1: A párizsi békekonferencia és Apponyi Albert védőbeszéde
story_21_1 = make_story(
    "story.b1.trianon.01",
    "A békekonferencia és gróf Apponyi Albert védőbeszéde (1920)",
    "1920 januárjában a magyar békedelegáció megérkezett Párizsba. Gróf Apponyi Albert három nyelven elmondott híres védőbeszéde és Teleki Pál 'vörös térképe' a történelmi és etnikai igazság mellett érvelt.",
    "Neuilly és Párizs",
    ["Érvelést, meggyőzést és igazságkeresést kifejező szerkezetek (érvel vmi mellett, rámutat arra, hogy; védelmére kel)", "Peace delegation, Apponyi's speech, red map, and diplomatic defense"],
    ["békedelegáció", "Apponyi Albert", "védőbeszéd", "vörös térkép", "Teleki Pál"],
    [
        "1920 januárjában a gróf Apponyi Albert vezette magyar békedelegáció megérkezett Párizsba, hogy átvegye a győztes antanthatalmak által kidolgozott békefeltételeket. A magyar küldöttséget a külvilágtól elzárva tartották Neuillyben, és érdemi tárgyalásokra nem adtak lehetőséget.",
        "1920. január 16-án Apponyi Albert a békekonferencia Legfelsőbb Tanácsa előtt mondta el történelmi beszédét egymás után franciául, angolul és olaszul. Beszédében rámutatott: a tervezett határok nem az etnikai elvet követik, hanem több millió magyart szakítanak el anyanemzetüktől idegen uralom alá.",
        "A delegáció bemutatta Teleki Pál híres 'vörös térképét' (carte rouge), amely pontosan ábrázolta a Kárpát-medence népességeloszlását. Bár a beszédet mély tisztelettel hallgatták a diplomaták, a geopolitikai döntést a győztesek már korábban meghozták."
    ],
    [
        {"lemma": "békedelegáció", "pos": "noun", "cefr": "B1", "gloss": "peace delegation"},
        {"lemma": "védőbeszéd", "pos": "noun", "cefr": "B1", "gloss": "defense speech, pleading"},
        {"lemma": "vörös térkép", "pos": "noun", "cefr": "B1", "gloss": "'Red Map' (Teleki's ethnic map showing Hungarians in red)"},
        {"lemma": "békefeltételek", "pos": "noun", "cefr": "B1", "gloss": "peace terms, conditions"},
        {"lemma": "érvel", "pos": "verb", "cefr": "B1", "gloss": "to argue, plead for"}
    ],
    [
        {
            "question": "Ki vezette a magyar békedelegációt Párizsban 1920 januárjában?",
            "options": ["Gróf Apponyi Albert", "Horthy Miklós", "Károlyi Mihály", "Deák Ferenc"],
            "correctIndex": 0,
            "explanation": "Gróf Apponyi Albert volt a békedelegáció vezetője és a híres védőbeszéd elmondója."
        }
    ]
)
write_json(STORIES_DIR / "story.b1.trianon.01.json", story_21_1)

voc_21_1 = {
    "id": "voc.b1.trianon.01",
    "title": "A békedelegáció és érvelés szókincse",
    "description": "Békedelegáció, védőbeszéd, vörös térkép, békefeltételek és érvelés.",
    "entries": [
        {"lemma": "békedelegáció", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "official delegation representing the state at peace negotiations", "examples": [{"hu": "A békedelegáció Párizsba utazott.", "en": "The peace delegation traveled to Paris."}]}]},
        {"lemma": "védőbeszéd", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "impassioned speech in defense of national rights", "examples": [{"hu": "Apponyi védőbeszéde világhírűvé vált.", "en": "Apponyi's defense speech became world-famous."}]}]},
        {"lemma": "vörös térkép", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "ethnographic map of the Carpathian Basin drawn by Pál Teleki", "examples": [{"hu": "A vörös térkép pontosan mutatta a magyar lakosságot.", "en": "The red map precisely showed the Hungarian population."}]}]},
        {"lemma": "érvel", "pos": "verb", "cefr": "B1", "definitions": [{"meaning": "to put forward logical arguments and evidence", "examples": [{"hu": "Apponyi az etnikai határok és az igazságosság mellett érvelt.", "en": "Apponyi argued for ethnic borders and justice."}]}]},
        {"lemma": "békefeltételek", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "conditions dictated in peace treaties", "examples": [{"hu": "A békefeltételek rendkívül súlyosak voltak.", "en": "The peace conditions were extremely harsh."}]}]}
    ]
}
write_json(VOCAB_DIR / "voc.b1.trianon.01.json", voc_21_1)

gr_21_1 = {
    "id": "gr.b1.trianon.01",
    "title": "Érvelést és álláspontot kifejező szerkezetek (érvel vmi mellett, rámutat arra, hogy)",
    "description": "Formulating argumentative positions, evidence presentation, and persuasive discourse.",
    "rules": [
        {
            "explanation": "Diplomáciai érvelésnél és történelmi vitákban az 'érvel vmi mellett/ellen', 'rámutat arra, hogy...', 'hangsúlyozza, hogy...' igéket alkalmazzuk.",
            "examples": [
                {"spanish": "Apponyi Albert az igazságos határok mellett érvelt.", "english": "Albert Apponyi argued for just borders."},
                {"spanish": "A delegáció rámutatott arra, hogy a döntés népszavazás nélkül született.", "english": "The delegation pointed out that the decision was made without a plebiscite."}
            ]
        }
    ]
}
write_json(GRAMMAR_DIR / "gr.b1.trianon.01.json", gr_21_1)

exs_21_1 = [
    {"id": "ex.b1.trianon.01.01", "type": "multiple-choice", "lesson": "lesson.b1.trianon.01", "teaches": ["Apponyi-Albert-vedobeszed"], "prompt": "Milyen nyelveken mondta el gróf Apponyi Albert a védőbeszédét 1920. január 16-án Párizsban?", "options": ["Franciául, angolul és olaszul", "Csak magyarul", "Németül és oroszul", "Latinul és görögül"], "correctIndex": 0, "explanation": "Apponyi tolmács nélkül, franciául, angolul és olaszul beszélt."},
    {"id": "ex.b1.trianon.01.02", "type": "fill-blank", "lesson": "lesson.b1.trianon.01", "teaches": ["vedobeszedet"], "prompt": "Egészítsd ki a mondatot!", "sentence": "Apponyi Albert történelmi *védőbeszédet* tartott Párizsban.", "target": "védőbeszédet"},
    {"id": "ex.b1.trianon.01.03", "type": "sentence-builder", "lesson": "lesson.b1.trianon.01", "teaches": ["Teleki-Pal", "voros-terkep"], "prompt": "Rakd össze a történelmi tényt!", "chips": ["Teleki", "Pál", "elkészítette", "a", "híres", "vörös", "térképet."], "target": "Teleki Pál elkészítette a híres vörös térképet.", "english": "Pál Teleki created the famous Red Map."},
    {"id": "ex.b1.trianon.01.04", "type": "multiple-choice", "lesson": "lesson.b1.trianon.01", "teaches": ["voros-terkep-lenyege"], "prompt": "Miért nevezték 'vörös térképnek' Teleki Pál néprajzi térképét?", "options": ["Mert a magyar nemzetiségű lakosságot piros (vörös) színnel jelölte", "Mert a kommunisták rajzolták", "Mert vér folyt rá", "Mert a határokat vörössel húzták meg"], "correctIndex": 0, "explanation": "A térkép vörös színnel ábrázolta a tömbben élő magyar népességet."},
    {"id": "ex.b1.trianon.01.05", "type": "fill-blank", "lesson": "lesson.b1.trianon.01", "teaches": ["békedelegációt"], "prompt": "Egészítsd ki a mondatot!", "sentence": "Apponyi Albert vezette a magyar *békedelegációt*.", "target": "békedelegációt"},
    {"id": "ex.b1.vilaghaboru.01.06_tri", "type": "sentence-builder", "lesson": "lesson.b1.trianon.01", "teaches": ["ramutatott", "igazsagtalansag"], "prompt": "Alkoss szabályos alárendelő mondatot!", "chips": ["Apponyi", "rámutatott", "arra,", "hogy", "a", "feltételek", "méltánytalanok."], "target": "Apponyi rámutatott arra, hogy a feltételek méltánytalanok.", "english": "Apponyi pointed out that the terms were unfair."},
    {"id": "ex.b1.trianon.01.07", "type": "multiple-choice", "lesson": "lesson.b1.trianon.01", "teaches": ["nepszavazas-koveteles"], "prompt": "Mit javasolt a magyar delegáció a vitatott területek hovatartozásának eldöntésére?", "options": ["Demokratikus népszavazást a lakosság megkérdezésével", "Azonnali új háborút", "A területek pénzbeli eladását", "A határok sorsolással való kijelölését"], "correctIndex": 0, "explanation": "A küldöttség népszavazást követelt az önrendelkezési jog alapján."},
    {"id": "ex.b1.trianon.01.08", "type": "fill-blank", "lesson": "lesson.b1.trianon.01", "teaches": ["ervelt"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A delegáció az etnikai elv és a népszavazás mellett *érvelt*.", "target": "érvelt"}
]
write_json(EXERCISES_DIR / "ex.b1.trianon.01.json", make_exercise_group("ex.b1.trianon.01", "A békekonferencia és Apponyi beszéde gyakorlatok", "Gyakorlatok Apponyi Albert védőbeszédéről, a vörös térképről és az érvelő nyelvtani szerkezetekről.", exs_21_1))

lesson_21_1 = make_lesson(
    "lesson.b1.trianon.01",
    "A békekonferencia és gróf Apponyi Albert védőbeszéde (1920)",
    "Érvelést kifejező szerkezetek (érvel vmi mellett, rámutat arra, hogy)",
    "Ismerjük meg a magyar békedelegáció párizsi fellépését, Apponyi Albert híres védőbeszédét és Teleki Pál vörös térképét.",
    ["Tudni Apponyi Albert védőbeszédének jelentőségét és nyelvtudását", "Ismerni a Teleki-féle 'vörös térkép' néprajzi célját", "Használni az érvelést és népszavazási követelést kifejező mondatokat"],
    "story.b1.trianon.01",
    "voc.b1.trianon.01",
    "gr.b1.trianon.01",
    "ex.b1.trianon.01",
    [e["id"] for e in exs_21_1]
)
write_json(LESSONS_DIR / "lesson.b1.trianon.01.json", lesson_21_1)


# Lesson 2: 1920. június 4.: A trianoni békeszerződés aláírása
story_21_2 = make_story(
    "story.b1.trianon.02",
    "1920. június 4.: A trianoni békeszerződés aláírása",
    "1920. június 4-én 16 óra 32 perckor a versailles-i Nagy Trianon kastélyban a magyar megbízottak aláírták a békediktátumot. Budapesten megkondultak a harangok, megállt a közlekedés, és gyászba borult az egész nemzet.",
    "Grand Trianon kastély (Versailles) és Budapest",
    ["Időpontot, aláírást és nemzeti gyászt kifejező szerkezetek (aláír, életbe lép, gyászba borul, megkondul)", "Signing of Treaty of Trianon, national mourning, and historic tragedy"],
    ["Trianon", "Grand Trianon", "aláírás", "nemzeti gyász", "harangzúgás"],
    [
        "1920. június 4-én délután a Párizs melletti Versailles-ban, a Nagy Trianon (Grand Trianon) kastély folyosóján Drasche-Lázár Alfréd rendkívüli követ és Benárd Ágost népjóléti miniszter aláírta a trianoni békediktátumot.",
        "Magyarország kényszer hatására írta alá az okmányt, mivel a megtagadás azonnali katonai megszállást és az ország teljes megsemmisítését jelentette volna.",
        "Az aláírás pillanatában, pontosan 16 óra 32 perckor Budapesten és országszerte megkondultak a templomharangok, megszólaltak a gyárak szirénái. Tíz percre leállt a vasúti és villamosközlekedés, bezártak az üzletek és iskolák: a nemzet néma gyásszal tiltakozott a szétszakítás ellen."
    ],
    [
        {"lemma": "békediktátum", "pos": "noun", "cefr": "B1", "gloss": "dictated peace treaty (imposed without genuine negotiation)"},
        {"lemma": "nemzeti gyász", "pos": "noun", "cefr": "B1", "gloss": "national mourning"},
        {"lemma": "aláírás", "pos": "noun", "cefr": "B1", "gloss": "signing, signature"},
        {"lemma": "harangzúgás", "pos": "noun", "cefr": "B1", "gloss": "tolling of church bells"},
        {"lemma": "kényszer", "pos": "noun", "cefr": "B1", "gloss": "coercion, duress, compulsion"}
    ],
    [
        {
            "question": "Melyik évben és napon írták alá a trianoni békediktátumot?",
            "options": ["1920. június 4-én", "1918. október 31-én", "1914. június 28-án", "1848. március 15-én"],
            "correctIndex": 0,
            "explanation": "A trianoni békeszerződést 1920. június 4-én írták alá."
        }
    ]
)
write_json(STORIES_DIR / "story.b1.trianon.02.json", story_21_2)

voc_21_2 = {
    "id": "voc.b1.trianon.02",
    "title": "A trianoni aláírás és gyász szókincse",
    "description": "Békediktátum, nemzeti gyász, aláírás, harangzúgás és kényszer.",
    "entries": [
        {"lemma": "békediktátum", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "dictated peace treaty without fair negotiations", "examples": [{"hu": "A trianoni békediktátumot kényszer alatt írták alá.", "en": "The Trianon peace dictate was signed under duress."}]}]},
        {"lemma": "nemzeti gyász", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "official state or popular mourning", "examples": [{"hu": "A szerződés aláírásakor nemzeti gyász borult az országra.", "en": "Upon signing the treaty, national mourning fell over the country."}]}]},
        {"lemma": "aláírás", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "act of signing an official document", "examples": [{"hu": "Az aláírás 1920. június 4-én történt.", "en": "The signing took place on June 4, 1920."}]}]},
        {"lemma": "harangzúgás", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "solemn tolling of church bells across the country", "examples": [{"hu": "Harangzúgás kísérte a gyászos eseményt.", "en": "Tolling of bells accompanied the mournful event."}]}]},
        {"lemma": "kényszer", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "coercion, unavoidable pressure", "examples": [{"hu": "A kormány kényszer hatására cselekedett.", "en": "The government acted under coercion."}]}]}
    ]
}
write_json(VOCAB_DIR / "voc.b1.trianon.02.json", voc_21_2)

gr_21_2 = {
    "id": "gr.b1.trianon.02",
    "title": "Pontos időpontot és egyidejűséget kifejező határozók (pillanatában, -kor, közben)",
    "description": "Temporal precision in historical milestones and simultaneous nationwide reactions.",
    "rules": [
        {
            "explanation": "Történelmi események egyidejűségének kifejezésére a '-kor' időhatározó ragot és a 'pillanatában', 'alatt', 'közben' időbeli kifejezéseket használjuk.",
            "examples": [
                {"spanish": "16 óra 32 perckor megkondultak a harangok.", "english": "At 16:32 the bells tolled."},
                {"spanish": "Az aláírás pillanatában megállt a közlekedés a fővárosban.", "english": "At the moment of signing, traffic stopped in the capital."}
            ]
        }
    ]
}
write_json(GRAMMAR_DIR / "gr.b1.trianon.02.json", gr_21_2)

exs_21_2 = [
    {"id": "ex.b1.trianon.02.01", "type": "multiple-choice", "lesson": "lesson.b1.trianon.02", "teaches": ["Trianon-alairas-datum-hely"], "prompt": "Hol és mikor írták alá a trianoni békeszerződést?", "options": ["A versailles-i Nagy Trianon kastélyban 1920. június 4-én", "Bécsben 1867-ben", "Párizsban 1914-ben", "Budapesten 1918-ban"], "correctIndex": 0, "explanation": "A Nagy Trianon palotában írták alá 1920. június 4-én."},
    {"id": "ex.b1.trianon.02.02", "type": "fill-blank", "lesson": "lesson.b1.trianon.02", "teaches": ["bekediktatumot"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A küldöttek kényszer hatására írták alá a *békediktátumot*.", "target": "békediktátumot"},
    {"id": "ex.b1.trianon.02.03", "type": "sentence-builder", "lesson": "lesson.b1.trianon.02", "teaches": ["harangok", "megkondultak"], "prompt": "Rakd össze az egyidejűséget kifejező mondatot!", "chips": ["Az", "aláírás", "pillanatában", "megkondultak", "a", "templomok", "harangjai."], "target": "Az aláírás pillanatában megkondultak a templomok harangjai.", "english": "At the moment of signing, the bells of the churches tolled."},
    {"id": "ex.b1.trianon.02.04", "type": "multiple-choice", "lesson": "lesson.b1.trianon.02", "teaches": ["trianon-tiltakozas-Budapest"], "prompt": "Hogyan fejezte ki gyászát Budapest lakossága az aláírás időpontjában?", "options": ["Tíz percre leállt a közlekedés, bezártak az üzletek és gyászlobogókat tűztek ki", "Tűzijátékot tartottak", "Katonai parádét rendeztek", "Koncertet szerveztek a téren"], "correctIndex": 0, "explanation": "Megállt az élet a városban, tíz perces néma gyásszal tiltakoztak."},
    {"id": "ex.b1.trianon.02.05", "type": "fill-blank", "lesson": "lesson.b1.trianon.02", "teaches": ["nemzeti-gyasz"], "prompt": "Egészítsd ki a mondatot!", "sentence": "Országszerte *nemzeti gyász* volt a békediktátum napján.", "target": "nemzeti gyász"},
    {"id": "ex.b1.trianon.02.06", "type": "sentence-builder", "lesson": "lesson.b1.trianon.02", "teaches": ["kenyszer", "alairtak"], "prompt": "Alkoss szabályos összetett mondatot!", "chips": ["Magyarország", "a", "megszállás", "elkerülése", "miatt", "kényszerből", "írt", "alá."], "target": "Magyarország a megszállás elkerülése miatt kényszerből írt alá.", "english": "Hungary signed under duress to avoid military occupation."},
    {"id": "ex.b1.trianon.02.07", "type": "multiple-choice", "lesson": "lesson.b1.trianon.02", "teaches": ["pontos-idopont-1632"], "prompt": "Melyik órában és percben történt az aláírás 1920. június 4-én?", "options": ["16 óra 32 perckor", "Délben 12:00-kor", "Reggel 8:00-kor", "Éjfélkor"], "correctIndex": 0, "explanation": "A történelmi feljegyzések szerint 16:32-kor írták alá az okmányt."},
    {"id": "ex.b1.trianon.02.08", "type": "fill-blank", "lesson": "lesson.b1.trianon.02", "teaches": ["harangzugas"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A néma csendet csak a fájdalmas *harangzúgás* törte meg.", "target": "harangzúgás"}
]
write_json(EXERCISES_DIR / "ex.b1.trianon.02.json", make_exercise_group("ex.b1.trianon.02", "A trianoni aláírás gyakorlatok", "Gyakorlatok 1920. június 4-ről, a Nagy Trianon kastélyról, a nemzeti gyászról és az időhatározókról.", exs_21_2))

lesson_21_2 = make_lesson(
    "lesson.b1.trianon.02",
    "1920. június 4.: A trianoni békeszerződés aláírása",
    "Pontos időpontot és egyidejűséget kifejező szerkezetek (pillanatában, -kor)",
    "Ismerjük meg az 1920. június 4-i trianoni békediktátum aláírásának körülményeit és a nemzeti gyász megnyilvánulásait.",
    ["Tudni a trianoni szerződés aláírásának pontos dátumát és helyszínét (1920. június 4., Grand Trianon)", "Ismerni a kényszer alatti aláírás okait és a nemzeti gyászt", "Használni a pontos időpontot és történelmi egyidejűséget jelölő nyelvtani formákat"],
    "story.b1.trianon.02",
    "voc.b1.trianon.02",
    "gr.b1.trianon.02",
    "ex.b1.trianon.02",
    [e["id"] for e in exs_21_2]
)
write_json(LESSONS_DIR / "lesson.b1.trianon.02.json", lesson_21_2)


# Lesson 3: A trianoni döntés területi, emberi és gazdasági következményei
story_21_3 = make_story(
    "story.b1.trianon.03",
    "A trianoni döntés területi, népességi és gazdasági sokkja",
    "A trianoni szerződés következtében Magyarország elveszítette területének több mint kétharmadát (67%) és lakosságának 60%-át. 3,3 millió magyar került az új országhatárokon kívülre kisebbségi sorba.",
    "Kárpát-medence és elcsatolt területek",
    ["Mértéket, arányt és veszteséget kifejező számnevek és szerkezetek (kétharmada, elcsatol, kisebbségbe kerül)", "Territorial, demographic, and economic consequences of Trianon"],
    ["elcsatolt területek", "kisebbség", "nyersanyagforrás", "erdővagyon", "vasúthálózat"],
    [
        "A békediktátum példátlanul súlyos csapást mért az ezeréves magyar államra. A történelmi Magyarország területe (Horvátország nélkül) 282 ezer négyzetkilométerről 93 ezerre csökkent, lakossága pedig 18,2 millióról 7,6 millióra apadt.",
        "A legfájdalmasabb veszteség az emberi dimenzió volt: mintegy 3,3 millió magyar anyanyelvű ember – a teljes magyarság egyharmada – egyik napról a másikra az új utódállamok (Románia, Csehszlovákia, Szerb-Horvát-Szlovén Királyság, Ausztria) határai közé került, többségük közvetlenül a határ menti színmagyar tömbökben.",
        "A gazdaság is összeomlott: az ország elveszítette vasérc- és sóbányáinak 100%-át, erdővagyonának 88%-át, valamint a vasúti körgyűrűt és a természetes hegyvidéki védvonalakat."
    ],
    [
        {"lemma": "elcsatolt", "pos": "adj", "cefr": "B1", "gloss": "annexed, severed, detached (territories)"},
        {"lemma": "kétharmad", "pos": "num", "cefr": "B1", "gloss": "two-thirds (2/3)"},
        {"lemma": "utódállam", "pos": "noun", "cefr": "B1", "gloss": "successor state (neighboring states after 1920)"},
        {"lemma": "erdővagyon", "pos": "noun", "cefr": "B1", "gloss": "forest assets / resources"},
        {"lemma": "kisebbségi sors", "pos": "noun", "cefr": "B1", "gloss": "minority fate / status"}
    ],
    [
        {
            "question": "Területének mekkora részét veszítette el a Magyar Királyság a trianoni döntés következtében?",
            "options": ["Több mint kétharmadát (kb. 67–71%-át)", "Egytizedét", "A felét", "Semmit sem veszített"],
            "correctIndex": 0,
            "explanation": "Magyarország területének több mint kétharmadát elcsatolták."
        }
    ]
)
write_json(STORIES_DIR / "story.b1.trianon.03.json", story_21_3)

voc_21_3 = {
    "id": "voc.b1.trianon.03",
    "title": "A területi és gazdasági veszteségek szókincse",
    "description": "Elcsatolt területek, kétharmad, utódállam, erdővagyon és kisebbségi sors.",
    "entries": [
        {"lemma": "elcsatolt", "pos": "adj", "cefr": "B1", "definitions": [{"meaning": "territory severed from Hungary by the peace treaty", "examples": [{"hu": "Az elcsatolt területeken milliók éltek.", "en": "Millions lived in the severed territories."}]}]},
        {"lemma": "kétharmad", "pos": "num", "cefr": "B1", "definitions": [{"meaning": "fraction two thirds (2/3)", "examples": [{"hu": "Az ország területének kétharmadát elveszítette.", "en": "The country lost two-thirds of its territory."}]}]},
        {"lemma": "utódállam", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "successor states that received territory", "examples": [{"hu": "Az utódállamokban a magyarok kisebbségbe kerültek.", "en": "In the successor states, Hungarians became a minority."}]}]},
        {"lemma": "erdővagyon", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "forest resources and timber assets", "examples": [{"hu": "A fenyvesek és az erdővagyon nagy része a határon túlra került.", "en": "Most of the pine forests and timber assets fell beyond the border."}]}]},
        {"lemma": "kisebbségi sors", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "status of living as an ethnic minority under foreign rule", "examples": [{"hu": "A külhoni magyarság vállalta a kisebbségi sorsot.", "en": "Hungarians abroad undertook the minority fate."}]}]}
    ]
}
write_json(VOCAB_DIR / "voc.b1.trianon.03.json", voc_21_3)

gr_21_3 = {
    "id": "gr.b1.trianon.03",
    "title": "Törtszámok és arányok kifejezése (kétharmada, egyharmada, 60%-a)",
    "description": "Expressing fractions, percentages, and proportions in statistical and historical context.",
    "rules": [
        {
            "explanation": "Törtszámok és arányok képzése: a tőszámnévhez a '-ad/-ed/-öd' képző járul (fél, harmad, negyed). A birtokos szerkezetben: 'a terület kétharmada', 'a lakosság 60%-a'.",
            "examples": [
                {"spanish": "Az ország területének több mint kétharmada elveszett.", "english": "More than two-thirds of the country's territory was lost."},
                {"spanish": "3,3 millió magyar került a határokon kívülre.", "english": "3.3 million Hungarians fell outside the borders."}
            ]
        }
    ]
}
write_json(GRAMMAR_DIR / "gr.b1.trianon.03.json", gr_21_3)

exs_21_3 = [
    {"id": "ex.b1.trianon.03.01", "type": "multiple-choice", "lesson": "lesson.b1.trianon.03", "teaches": ["trianon-magyarok-szama"], "prompt": "Körülbelül hány magyar anyanyelvű ember került az új határokon túlra 1920-ban?", "options": ["Körülbelül 3,3 millió magyar", "Ötvenezer ember", "Tízmillió ember", "Kétszáz ember"], "correctIndex": 0, "explanation": "3,3 millió magyar ember került kisebbségi sorsba."},
    {"id": "ex.b1.trianon.03.02", "type": "fill-blank", "lesson": "lesson.b1.trianon.03", "teaches": ["ketharmadat"], "prompt": "Egészítsd ki a mondatot!", "sentence": "Magyarország elveszítette korábbi területének *kétharmadát*.", "target": "kétharmadát"},
    {"id": "ex.b1.trianon.03.03", "type": "sentence-builder", "lesson": "lesson.b1.trianon.03", "teaches": ["utodallamok", "kisebbseg"], "prompt": "Rakd össze a mondatot!", "chips": ["A", "magyarság", "egyharmada", "az", "utódállamokban", "kisebbségbe", "került."], "target": "A magyarság egyharmada az utódállamokban kisebbségbe került.", "english": "One third of the Hungarian population became a minority in the successor states."},
    {"id": "ex.b1.trianon.03.04", "type": "multiple-choice", "lesson": "lesson.b1.trianon.03", "teaches": ["elcsatolt-teruletek-reszei"], "prompt": "Mely történelmi országrészeket csatolták el többek között a békeszerződéssel?", "options": ["Erdélyt, a Felvidéket, Kárpátalját és a Délvidéket", "Csak a Balatont", "A Dunakanyart és a Bakonyt", "Bécset és Prágát"], "correctIndex": 0, "explanation": "Erdély, a Felvidék, Kárpátalja, a Délvidék és az Őrvidék kerültek más országokhoz."},
    {"id": "ex.b1.trianon.03.05", "type": "fill-blank", "lesson": "lesson.b1.trianon.03", "teaches": ["elcsatolt"], "prompt": "Egészítsd ki a mondatot!", "sentence": "Az *elcsatolt* területeken a magyar iskolákat bezárták.", "target": "elcsatolt"},
    {"id": "ex.b1.trianon.03.06", "type": "sentence-builder", "lesson": "lesson.b1.trianon.03", "teaches": ["banyaszat", "erdo"], "prompt": "Alkoss szabályos összetett mondatot!", "chips": ["Az", "ország", "elveszítette", "a", "sóbányák", "és", "erdők", "nagy", "részét."], "target": "Az ország elveszítette a sóbányák és erdők nagy részét.", "english": "The country lost most of the salt mines and forests."},
    {"id": "ex.b1.trianon.03.07", "type": "multiple-choice", "lesson": "lesson.b1.trianon.03", "teaches": ["gazdasagi-kovetkezmeny"], "prompt": "Hogyan befolyásolta a határhúzás a magyar gazdaságot és vasutat?", "options": ["Megszűnt a nyersanyagellátás és elvágták a körkörös vasútvonalakat", "Olcsóbb lett a szállítás", "Megduplázódott a gyárak száma", "Nem történt semmilyen változás"], "correctIndex": 0, "explanation": "A természetes gazdasági egységek és vasúti fővonalak kettészakadtak."},
    {"id": "ex.b1.trianon.03.08", "type": "fill-blank", "lesson": "lesson.b1.trianon.03", "teaches": ["kisebbsegi"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A határon túliak a nehéz *kisebbségi* sorsot választották.", "target": "kisebbségi"}
]
write_json(EXERCISES_DIR / "ex.b1.trianon.03.json", make_exercise_group("ex.b1.trianon.03", "Trianoni veszteségek gyakorlatok", "Gyakorlatok a területi, emberi és gazdasági veszteségekről, a törtszámokról és a mértékekről.", exs_21_3))

lesson_21_3 = make_lesson(
    "lesson.b1.trianon.03",
    "A trianoni döntés területi, népességi és gazdasági sokkja",
    "Törtszámok és arányok kifejezése (kétharmada, 3,3 millió)",
    "Tekintsük át a trianoni határok következményeit: a terület 67%-ának elvesztését és a 3,3 millió külhoni magyart.",
    ["Ismerni a területi (2/3) és népességi veszteségek pontos számait", "Tudni a 3,3 millió határon túlra került magyar nemzettársunk sorsát", "Használni a törtszámokat és arányokat kifejező nyelvtani szerkezeteket"],
    "story.b1.trianon.03",
    "voc.b1.trianon.03",
    "gr.b1.trianon.03",
    "ex.b1.trianon.03",
    [e["id"] for e in exs_21_3]
)
write_json(LESSONS_DIR / "lesson.b1.trianon.03.json", lesson_21_3)


# Lesson 4: Menekültek és vagonlakók: a trianoni trauma a mindennapokban
story_21_4 = make_story(
    "story.b1.trianon.04",
    "Menekültválság és a 'vagonlakók' világa (1920–1924)",
    "A trianoni békeszerződés után több mint 350 ezer magyar menekült el az elcsatolt területekről az anyaországba. A budapesti pályaudvarokon évekig vasúti marhavagonokban éltek a hazájukat vesztett családok.",
    "Budapesti pályaudvarok (Keleti, Nyugati, Józsefváros)",
    ["Nehézséget, kényszerű áttelepülést és szolidaritást kifejező szerkezetek (menekülni kényszerül, vagonokban tengődik, befogad)", "Refugee crisis, wagon dwellers, displacement, and national solidarity"],
    ["menekült", "vagonlakó", "pályaudvar", "kényszerű áttelepülés", "szolidaritás"],
    [
        "Az utódállamok hatóságai sok helyen azonnali hűségesküt követeltek a magyar tisztviselőktől, tanároktól, vasutasoktól és papoktól. Aki ezt megtagadta, azt elbocsátották állásából, vagy kiutasították az országból.",
        "1920 és 1924 között mintegy 350-400 ezer magyar menekült érkezett a csonka anyaországba. A lakáshiánnyal küzdő Budapesten a Keleti, Nyugati és Józsefvárosi pályaudvarok mellékvágányain rendeztek be szükségotthonokat: megszületett a 'vagonlakók' tragikus világa.",
        "Egész családok, tanárok, orvosok és tisztviselők éltek évekig hideg, fűtetlen vasúti kocsikban, miközben az országos Menekültügyi Hivatal és a társadalom segélyakciókkal igyekezett enyhíteni a nyomort."
    ],
    [
        {"lemma": "vagonlakó", "pos": "noun", "cefr": "B1", "gloss": "wagon dweller (refugee living in railway boxcars)"},
        {"lemma": "menekült", "pos": "noun", "cefr": "B1", "gloss": "refugee, displaced person"},
        {"lemma": "hűségeskü", "pos": "noun", "cefr": "B1", "gloss": "oath of allegiance"},
        {"lemma": "szükséglakás", "pos": "noun", "cefr": "B1", "gloss": "emergency shelter, makeshift housing"},
        {"lemma": "kiutasít", "pos": "verb", "cefr": "B1", "gloss": "to expel, deport"}
    ],
    [
        {
            "question": "Hol éltek évekig a trianoni elcsatolt területekről Budapestre menekült magyar családok ezrei?",
            "options": ["A budapesti pályaudvarok vágányain álló vasúti vagonokban ('vagonlakók')", "Luxusszállodákban", "Külföldi kastélyokban", "A Parlament folyosóin"],
            "correctIndex": 0,
            "explanation": "A menekültek vasúti kocsikban, marhavagonokban éltek a pályaudvarokon."
        }
    ]
)
write_json(STORIES_DIR / "story.b1.trianon.04.json", story_21_4)

voc_21_4 = {
    "id": "voc.b1.trianon.04",
    "title": "A menekültek és vagonlakók szókincse",
    "description": "Vagonlakó, menekült, hűségeskü, szükséglakás és kiutasítás.",
    "entries": [
        {"lemma": "vagonlakó", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "refugee living in railway freight wagons in Budapest", "examples": [{"hu": "A vagonlakók méltósággal viselték a nehéz sorsot.", "en": "The wagon dwellers bore their hard fate with dignity."}]}]},
        {"lemma": "menekült", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "refugee fleeing from annexed territories", "examples": [{"hu": "Több mint 350 ezer menekült érkezett az anyaországba.", "en": "Over 350,000 refugees arrived in the motherland."}]}]},
        {"lemma": "hűségeskü", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "oath of loyalty demanded by new state authorities", "examples": [{"hu": "A magyar tanárok megtagadták az idegen hűségesküt.", "en": "Hungarian teachers refused the foreign oath of loyalty."}]}]},
        {"lemma": "szükséglakás", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "makeshift temporary housing", "examples": [{"hu": "A vagonok éveken át szükséglakásként szolgáltak.", "en": "The boxcars served as makeshift housing for years."}]}]},
        {"lemma": "kiutasít", "pos": "verb", "cefr": "B1", "definitions": [{"meaning": "to expel people from their homeland", "examples": [{"hu": "Sok magyar értelmiségit kiutasítottak a határon túlra.", "en": "Many Hungarian intellectuals were expelled across the border."}]}]}
    ]
}
write_json(VOCAB_DIR / "voc.b1.trianon.04.json", voc_21_4)

gr_21_4 = {
    "id": "gr.b1.trianon.04",
    "title": "Kényszerűséget és állapotot kifejező szerkezetek (kénytelen volt, kényszerült, tengődik)",
    "description": "Expressing forced displacement, involuntary actions, and enduring harsh conditions.",
    "rules": [
        {
            "explanation": "A kényszerű történelmi cselekvések kifejezésére a 'kénytelen volt + főnévi igenév', 'menekülni kényszerült' formákat használjuk.",
            "examples": [
                {"spanish": "Több százezer ember volt kénytelen elhagyni a szülőföldjét.", "english": "Hundreds of thousands of people were forced to leave their homeland."},
                {"spanish": "A családok vasúti vagonokban kényszerültek élni.", "english": "The families were forced to live in railway boxcars."}
            ]
        }
    ]
}
write_json(GRAMMAR_DIR / "gr.b1.trianon.04.json", gr_21_4)

exs_21_4 = [
    {"id": "ex.b1.trianon.04.01", "type": "multiple-choice", "lesson": "lesson.b1.trianon.04", "teaches": ["menekultek-szama-1920"], "prompt": "Körülbelül hány magyar menekült érkezett az anyaországba Trianon után?", "options": ["Körülbelül 350–400 ezer menekült", "Ötszáz ember", "Tízmillió ember", "Kétezer ember"], "correctIndex": 0, "explanation": "Mintegy 350-400 ezer magyar menekült érkezett az anyaországba."},
    {"id": "ex.b1.trianon.04.02", "type": "fill-blank", "lesson": "lesson.b1.trianon.04", "teaches": ["vagonlakok"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A budapesti pályaudvarokon éltek a hazátlan *vagonlakók*.", "target": "vagonlakók"},
    {"id": "ex.b1.trianon.04.03", "type": "sentence-builder", "lesson": "lesson.b1.trianon.04", "teaches": ["kenytelenek-voltak", "elhagyni"], "prompt": "Rakd össze a mondatot!", "chips": ["Sokan", "kénytelenek", "voltak", "elhagyni", "ősi", "szülőföldjüket."], "target": "Sokan kénytelenek voltak elhagyni ősi szülőföldjüket.", "english": "Many were forced to leave their ancestral homeland."},
    {"id": "ex.b1.trianon.04.04", "type": "multiple-choice", "lesson": "lesson.b1.trianon.04", "teaches": ["husegesku-elutasitas"], "prompt": "Miért bocsátották el vagy utasították ki a magyar tisztviselőket és tanárokat az utódállamokból?", "options": ["Mert megtagadták az új államra teendő hűségesküt", "Mert nem akartak tanítani", "Mert túl sokat kerestek", "Mert orvosok akartak lenni"], "correctIndex": 0, "explanation": "A magyar nemzeti öntudatuk miatt nem tették le az idegen hűségesküt."},
    {"id": "ex.b1.trianon.04.05", "type": "fill-blank", "lesson": "lesson.b1.trianon.04", "teaches": ["husegeskut"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A magyar tanárok nem tették le a *hűségesküt*.", "target": "hűségesküt"},
    {"id": "ex.b1.trianon.04.06", "type": "sentence-builder", "lesson": "lesson.b1.trianon.04", "teaches": ["vagonokban", "eltek"], "prompt": "Alkoss szabályos összetett mondatot!", "chips": ["A", "menekült", "családok", "évekig", "hideg", "vagonokban", "éltek", "Budapesten."], "target": "A menekült családok évekig hideg vagonokban éltek Budapesten.", "english": "The refugee families lived for years in cold boxcars in Budapest."},
    {"id": "ex.b1.trianon.04.07", "type": "multiple-choice", "lesson": "lesson.b1.trianon.04", "teaches": ["menekultugy-segely"], "prompt": "Hogyan segített a magyar társadalom a nincstelen vagonlakókon?", "options": ["Országos segélyakciókkal, népkonyhákkal és új lakótelepek építésével", "Külföldre küldték őket", "Elzárták a pályaudvarokat", "Nem foglalkoztak velük"], "correctIndex": 0, "explanation": "Társadalmi összefogással és segélyprogramokkal enyhítették a nyomort."},
    {"id": "ex.b1.trianon.04.08", "type": "fill-blank", "lesson": "lesson.b1.trianon.04", "teaches": ["menekult"], "prompt": "Egészítsd ki a mondatot!", "sentence": "Több százezer *menekült* talált menedéket az anyaországban.", "target": "menekült"}
]
write_json(EXERCISES_DIR / "ex.b1.trianon.04.json", make_exercise_group("ex.b1.trianon.04", "A menekültek és vagonlakók gyakorlatok", "Gyakorlatok a trianoni menekültválságról, a vagonlakókról és a kényszerűséget kifejező szerkezetekről.", exs_21_4))

lesson_21_4 = make_lesson(
    "lesson.b1.trianon.04",
    "Menekültválság és a 'vagonlakók' világa (1920–1924)",
    "Kényszerűséget kifejező szerkezetek (kénytelen volt, kényszerült)",
    "Ismerjük meg a Trianon utáni 350 ezer menekült sorsát, a budapesti vagonlakók megrendítő mindennapjait.",
    ["Tudni a menekültek számarányát (kb. 350–400 ezer fő)", "Megérteni a vagonlakók fogalmát és a budapesti pályaudvarok szerepét", "Használni a kényszerűséget és áttelepülést kifejező nyelvtani formákat"],
    "story.b1.trianon.04",
    "voc.b1.trianon.04",
    "gr.b1.trianon.04",
    "ex.b1.trianon.04",
    [e["id"] for e in exs_21_4]
)
write_json(LESSONS_DIR / "lesson.b1.trianon.04.json", lesson_21_4)


# Lesson 5: A Nemzeti Összetartozás Napja (június 4.) és a 21. századi emlékezet
story_21_5 = make_story(
    "story.b1.trianon.05",
    "A Nemzeti Összetartozás Napja (június 4.) és a nemzeti egység",
    "2010-ben a Magyar Országgyűlés június 4-ét a Nemzeti Összetartozás Napjává nyilvánította. A törvény kimondja, hogy minden magyar a határokon átívelő egységes magyar nemzet része.",
    "Országház és Kárpát-medence",
    ["Összetartozást, nemzeti egységet és megemlékezést kifejező szerkezetek (összetartozik, kinyilvánít, határokon átível)", "National Cohesion Day, June 4, cross-border unity, and constitutional remembrance"],
    ["Nemzeti Összetartozás Napja", "határokon átívelő", "nemzeti egység", "honosítás", "Alaptörvény"],
    [
        "2010-ben a magyar parlament törvénybe iktatta, hogy június 4-e, a trianoni békediktátum évfordulója hivatalosan a Nemzeti Összetartozás Napja legyen. A jogszabály a gyászon felülemelkedve a nemzeti egység és a jövőbe tekintő szolidaritás szimbólumává emelte e napot.",
        "A törvény kimondja: 'A több állam fennhatósága alá vetett magyarság minden tagja és közössége része az egységes magyar nemzetnek, melynek határok feletti összetartozása valóság.'",
        "Ezen elv alapján vezette be Magyarország a kedvezményes honosítás intézményét, amely lehetővé tette, hogy a határon túli magyarok visszaszerezzék magyar állampolgárságukat. Június 4-én világszerte megemlékeznek arról, hogy a határok elválaszthatnak területeket, de a közös nyelv, kultúra és történelem örökre összeköti a magyarságot."
    ],
    [
        {"lemma": "Nemzeti Összetartozás Napja", "pos": "noun", "cefr": "B1", "gloss": "Day of National Cohesion (June 4 memorial day)"},
        {"lemma": "határokon átívelő", "pos": "adj", "cefr": "B1", "gloss": "cross-border, spanning borders"},
        {"lemma": "nemzeti egység", "pos": "noun", "cefr": "B1", "gloss": "national unity"},
        {"lemma": "honosítás", "pos": "noun", "cefr": "B1", "gloss": "naturalization, citizenship acquisition"},
        {"lemma": "összetartozás", "pos": "noun", "cefr": "B1", "gloss": "belonging together, cohesion"}
    ],
    [
        {
            "question": "Melyik nap a Nemzeti Összetartozás Napja Magyarországon 2010 óta?",
            "options": ["Június 4-e (a trianoni békeszerződés emléknapja)", "Március 15-e", "Augusztus 20-a", "Október 23-a"],
            "correctIndex": 0,
            "explanation": "Június 4-e a Nemzeti Összetartozás Napja."
        }
    ]
)
write_json(STORIES_DIR / "story.b1.trianon.05.json", story_21_5)

voc_21_5 = {
    "id": "voc.b1.trianon.05",
    "title": "A nemzeti összetartozás szókincse",
    "description": "Nemzeti Összetartozás Napja, határokon átívelő, nemzeti egység, honosítás és összetartozás.",
    "entries": [
        {"lemma": "Nemzeti Összetartozás Napja", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "official national memorial day on June 4 established in 2010", "examples": [{"hu": "Június 4-én ünnepeljük a Nemzeti Összetartozás Napját.", "en": "On June 4 we commemorate the Day of National Cohesion."}]}]},
        {"lemma": "határokon átívelő", "pos": "adj", "cefr": "B1", "definitions": [{"meaning": "transcending physical borders", "examples": [{"hu": "A magyar kultúra határokon átívelő kincs.", "en": "Hungarian culture is a cross-border treasure."}]}]},
        {"lemma": "nemzeti egység", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "spiritual and cultural unity of all Hungarians worldwide", "examples": [{"hu": "A törvény megerősíti a nemzeti egységet.", "en": "The law reinforces national unity."}]}]},
        {"lemma": "honosítás", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "simplified naturalization process for ethnic Hungarians", "examples": [{"hu": "A kedvezményes honosítással százezrek lettek állampolgárok.", "en": "Through simplified naturalization, hundreds of thousands became citizens."}]}]},
        {"lemma": "összetartozás", "pos": "noun", "cefr": "B1", "definitions": [{"meaning": "spiritual bond of belonging together", "examples": [{"hu": "Az összetartozás érzése él minden magyar szívében.", "en": "The feeling of belonging together lives in every Hungarian heart."}]}]}
    ]
}
write_json(VOCAB_DIR / "voc.b1.trianon.05.json", voc_21_5)

gr_21_5 = {
    "id": "gr.b1.trianon.05",
    "title": "Közösséget és összekapcsolódást kifejező szerkezetek (része vminek, határokon átívelően összeköt)",
    "description": "Formulations expressing shared identity, belonging to a community, and solidarity.",
    "rules": [
        {
            "explanation": "A nemzeti egységet és jogi tartozást leíró szerkezetek: 'része az egységes nemzetnek', 'összeköti a magyarságot', 'kinyilvánítja az összetartozást'.",
            "examples": [
                {"spanish": "Minden magyar része az egységes magyar nemzetnek.", "english": "Every Hungarian is part of the unified Hungarian nation."},
                {"spanish": "A közös nyelv és kultúra összeköti a határon túli közösségeket.", "english": "Shared language and culture unite communities beyond the borders."}
            ]
        }
    ]
}
write_json(GRAMMAR_DIR / "gr.b1.trianon.05.json", gr_21_5)

exs_21_5 = [
    {"id": "ex.b1.trianon.05.01", "type": "multiple-choice", "lesson": "lesson.b1.trianon.05", "teaches": ["Nemzeti-Osszetartozas-Napja-datum"], "prompt": "Melyik nap a Nemzeti Összetartozás Napja a magyar törvények szerint?", "options": ["Június 4-e", "Március 15-e", "Augusztus 20-a", "Október 23-a"], "correctIndex": 0, "explanation": "Június 4-e a Nemzeti Összetartozás Napja."},
    {"id": "ex.b1.trianon.05.02", "type": "fill-blank", "lesson": "lesson.b1.trianon.05", "teaches": ["osszetartozas"], "prompt": "Egészítsd ki a mondatot!", "sentence": "Június 4-e a nemzeti *összetartozás* szimbóluma.", "target": "összetartozás"},
    {"id": "ex.b1.trianon.05.03", "type": "sentence-builder", "lesson": "lesson.b1.trianon.05", "teaches": ["hatarokon-ativelo", "nemzet"], "prompt": "Rakd össze a nemzeti összetartozást kifejező mondatot!", "chips": ["Minden", "magyar", "része", "az", "egységes", "magyar", "nemzetnek."], "target": "Minden magyar része az egységes magyar nemzetnek.", "english": "Every Hungarian is part of the unified Hungarian nation."},
    {"id": "ex.b1.trianon.05.04", "type": "multiple-choice", "lesson": "lesson.b1.trianon.05", "teaches": ["kedvezmenyes-honositas-2010"], "prompt": "Mely intézmény tette lehetővé a határon túli magyarok számára a magyar állampolgárság megszerzését?", "options": ["A 2010-ben bevezetett egyszerűsített (kedvezményes) honosítás", "Az útlevélvásárlás", "A vízumkényszer", "A határzár"], "correctIndex": 0, "explanation": "A kedvezményes honosítás révén nyerhetik vissza állampolgárságukat."},
    {"id": "ex.b1.trianon.05.05", "type": "fill-blank", "lesson": "lesson.b1.trianon.05", "teaches": ["honositas"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A kedvezményes *honosítás* összekapcsolja a magyarságot.", "target": "honosítás"},
    {"id": "ex.b1.trianon.05.06", "type": "sentence-builder", "lesson": "lesson.b1.trianon.05", "teaches": ["nyelv", "kultura", "osszekot"], "prompt": "Alkoss szabályos összetett mondatot!", "chips": ["A", "közös", "nyelv", "és", "kultúra", "összeköti", "a", "világ", "magyarságát."], "target": "A közös nyelv és kultúra összeköti a világ magyarságát.", "english": "Shared language and culture unite the world's Hungarians."},
    {"id": "ex.b1.trianon.05.07", "type": "multiple-choice", "lesson": "lesson.b1.trianon.05", "teaches": ["Alaptorveny-nemzet-felelosseg"], "prompt": "Mit mond ki Magyarország Alaptörvénye a határon túli magyarokról?", "options": ["Magyarország felelősséget visel a határain kívül élő magyarok sorsáért és támogatja közösségeiket", "Nem foglalkozik velük", "Megtiltja a kapcsolatot", "Csak a határig érvényes a gondoskodás"], "correctIndex": 0, "explanation": "Az Alaptörvény rögzíti az anyaország felelősségvállalását a külhoni magyarságért."},
    {"id": "ex.b1.trianon.05.08", "type": "fill-blank", "lesson": "lesson.b1.trianon.05", "teaches": ["egyseg"], "prompt": "Egészítsd ki a mondatot!", "sentence": "A határok felett létezik a lelki és kulturális *egység*.", "target": "egység"}
]
write_json(EXERCISES_DIR / "ex.b1.trianon.05.json", make_exercise_group("ex.b1.trianon.05", "Nemzeti összetartozás gyakorlatok", "Gyakorlatok a Nemzeti Összetartozás Napjáról (június 4.), a honosításról és a nemzeti egységet kifejező szerkezetekről.", exs_21_5))

lesson_21_5 = make_lesson(
    "lesson.b1.trianon.05",
    "A Nemzeti Összetartozás Napja (június 4.) és a nemzeti egység",
    "Közösséget és összetartozást kifejező szerkezetek (része a nemzetnek, összeköt)",
    "Ismerjük meg június 4-ét, a Nemzeti Összetartozás Napját, a kedvezményes honosítást és a 21. századi nemzeti összetartozást.",
    ["Tudni a Nemzeti Összetartozás Napjának dátumát (június 4.) és törvényi jelentőségét", "Ismerni a kedvezményes honosítás intézményét és a határokon átívelő nemzeti egységet", "Használni a közösséget és összetartozást kifejező nyelvtani formákat"],
    "story.b1.trianon.05",
    "voc.b1.trianon.05",
    "gr.b1.trianon.05",
    "ex.b1.trianon.05",
    [e["id"] for e in exs_21_5]
)
write_json(LESSONS_DIR / "lesson.b1.trianon.05.json", lesson_21_5)


# Unit 21 Consolidation
cons_21_exs = [
    {"id": "ex.b1.trianon.cons.01", "type": "multiple-choice", "lesson": "lesson.b1.trianon.consolidation", "teaches": ["Apponyi-vedobeszed-1920"], "prompt": "Ki vezette a magyar békedelegációt Párizsban 1920-ban?", "options": ["Gróf Apponyi Albert", "Teleki Pál", "Horthy Miklós", "Kossuth Lajos"], "correctIndex": 0, "explanation": "Apponyi Albert vezette a delegációt."},
    {"id": "ex.b1.trianon.cons.02", "type": "fill-blank", "lesson": "lesson.b1.trianon.consolidation", "teaches": ["voros-terkepet"], "prompt": "Teleki Pál elkészítette a Kárpát-medence néprajzi *vörös térképét*.", "sentence": "Teleki Pál elkészítette a Kárpát-medence néprajzi *vörös térképét*.", "target": "vörös térképét"},
    {"id": "ex.b1.trianon.cons.03", "type": "multiple-choice", "lesson": "lesson.b1.trianon.consolidation", "teaches": ["trianon-datum-1920"], "prompt": "Melyik napon írták alá a trianoni békeszerződést?", "options": ["1920. június 4-én", "1914. június 28-án", "1918. október 31-én", "1848. március 15-én"], "correctIndex": 0, "explanation": "1920. június 4-én írták alá a Nagy Trianon kastélyban."},
    {"id": "ex.b1.trianon.cons.04", "type": "fill-blank", "lesson": "lesson.b1.trianon.consolidation", "teaches": ["Grand-Trianon"], "prompt": "A szerződést a Versailles melletti *Grand Trianon* kastélyban írták alá.", "sentence": "A szerződést a Versailles melletti *Grand Trianon* kastélyban írták alá.", "target": "Grand Trianon"},
    {"id": "ex.b1.trianon.cons.05", "type": "sentence-builder", "lesson": "lesson.b1.trianon.consolidation", "teaches": ["harangok", "nemzeti-gyasz"], "prompt": "Rakd össze a nemzeti gyászt leíró mondatot!", "chips": ["Az", "aláíráskor", "harangzúgás", "és", "nemzeti", "gyász", "kísérte", "a", "döntést."], "target": "Az aláíráskor harangzúgás és nemzeti gyász kísérte a döntést.", "english": "At the signing, tolling of bells and national mourning accompanied the decision."},
    {"id": "ex.b1.trianon.cons.06", "type": "multiple-choice", "lesson": "lesson.b1.trianon.consolidation", "teaches": ["teruleti-veszteseg-arany"], "prompt": "Területének mekkora részét veszítette el a Magyar Királyság Trianonban?", "options": ["Több mint kétharmadát (kb. 67%-át)", "Csak a tizedét", "A felét", "Egy százalékát"], "correctIndex": 0, "explanation": "Területének több mint kétharmadát veszítette el az ország."},
    {"id": "ex.b1.trianon.cons.07", "type": "fill-blank", "lesson": "lesson.b1.trianon.consolidation", "teaches": ["harom-egesz-harom"], "prompt": "Mintegy *3,3 millió* magyar került az országhatárokon kívülre.", "sentence": "Mintegy *3,3 millió* magyar került az országhatárokon kívülre.", "target": "3,3 millió"},
    {"id": "ex.b1.trianon.cons.08", "type": "sentence-builder", "lesson": "lesson.b1.trianon.consolidation", "teaches": ["utodallamok", "kisebbseg"], "prompt": "Alkoss szabályos mondatot!", "chips": ["A", "magyarok", "az", "új", "utódállamokban", "kisebbségbe", "kerültek."], "target": "A magyarok az új utódállamokban kisebbségbe kerültek.", "english": "The Hungarians became a minority in the new successor states."},
    {"id": "ex.b1.trianon.cons.09", "type": "multiple-choice", "lesson": "lesson.b1.trianon.consolidation", "teaches": ["vagonlakok-Budapest"], "prompt": "Kiket neveztek 'vagonlakóknak' az 1920-as évek elején?", "options": ["Az elcsatolt területekről elmenekült magyar családokat, akik pályaudvari vasúti vagonokban éltek", "Vasutas munkásokat", "Külföldi turistákat", "Hajléktalan katonákat"], "correctIndex": 0, "explanation": "A pályaudvarokon vagonokban lakó elmenekült családokat hívták így."},
    {"id": "ex.b1.trianon.cons.10", "type": "fill-blank", "lesson": "lesson.b1.trianon.consolidation", "teaches": ["menekult"], "prompt": "Több mint 350 ezer *menekült* érkezett a csonka anyaországba.", "sentence": "Több mint 350 ezer *menekült* érkezett a csonka anyaországba.", "target": "menekült"},
    {"id": "ex.b1.trianon.cons.11", "type": "sentence-builder", "lesson": "lesson.b1.trianon.consolidation", "teaches": ["husegesku", "megtagad"], "prompt": "Rakd össze az elutasításról szóló mondatot!", "chips": ["Sokan", "megtagadták", "az", "új", "államoknak", "tett", "hűségesküt."], "target": "Sokan megtagadták az új államoknak tett hűségesküt.", "english": "Many refused the oath of loyalty made to the new states."},
    {"id": "ex.b1.trianon.cons.12", "type": "multiple-choice", "lesson": "lesson.b1.trianon.consolidation", "teaches": ["Nemzeti-Osszetartozas-Napja-datum"], "prompt": "Melyik nap a Nemzeti Összetartozás Napja?", "options": ["Június 4-e", "Március 15-e", "Augusztus 20-a", "Október 23-a"], "correctIndex": 0, "explanation": "Június 4-e a Nemzeti Összetartozás Napja."},
    {"id": "ex.b1.trianon.cons.13", "type": "fill-blank", "lesson": "lesson.b1.trianon.consolidation", "teaches": ["Nemzeti-Osszetartozas-Napja"], "prompt": "2010 óta június 4-e a *Nemzeti Összetartozás Napja*.", "sentence": "2010 óta június 4-e a *Nemzeti Összetartozás Napja*.", "target": "Nemzeti Összetartozás Napja"},
    {"id": "ex.b1.trianon.cons.14", "type": "sentence-builder", "lesson": "lesson.b1.trianon.consolidation", "teaches": ["egyseges", "nemzet"], "prompt": "Alkoss szabályos összetett mondatot!", "chips": ["A", "határon", "túli", "magyarság", "az", "egységes", "nemzet", "része."], "target": "A határon túli magyarság az egységes nemzet része.", "english": "Hungarians beyond the borders are part of the unified nation."},
    {"id": "ex.b1.trianon.cons.15", "type": "multiple-choice", "lesson": "lesson.b1.trianon.consolidation", "teaches": ["kedvezmenyes-honositas"], "prompt": "Hogyan szerezhetnek magyar állampolgárságot a határon túli magyarok 2010 óta?", "options": ["Kedvezményes (egyszerűsített) honosítási eljárással", "Kizárólag áttelepüléssel", "Útlevélvásárlással", "Nem szerezhetnek állampolgárságot"], "correctIndex": 0, "explanation": "A kedvezményes honosítás biztosítja az állampolgárság megszerzését."},
    {"id": "ex.b1.trianon.cons.16", "type": "fill-blank", "lesson": "lesson.b1.trianon.consolidation", "teaches": ["honositas"], "prompt": "A kedvezményes *honosítás* jogi köteléket teremt az anyaországgal.", "sentence": "A kedvezményes *honosítás* jogi köteléket teremt az anyaországgal.", "target": "honosítás"},
    {"id": "ex.b1.trianon.cons.17", "type": "sentence-builder", "lesson": "lesson.b1.trianon.consolidation", "teaches": ["hatarok", "kultura"], "prompt": "Rakd össze az összetartozást kifejező mondatot!", "chips": ["A", "határok", "nem", "választhatják", "szét", "a", "közös", "kultúrát."], "target": "A határok nem választhatják szét a közös kultúrát.", "english": "Borders cannot divide the shared culture."},
    {"id": "ex.b1.trianon.cons.18", "type": "multiple-choice", "lesson": "lesson.b1.trianon.consolidation", "teaches": ["gazdasagi-vesztesegek"], "prompt": "Milyen természeti kincsek és bányák vesztek el Trianonban?", "options": ["Az erdővagyon 88%-a, a só- és vasércbányák 100%-a", "Csak homokbányák", "A Duna vize", "Semmilyen természeti kincs"], "correctIndex": 0, "explanation": "Az ipari és természeti kincsek szinte teljes egésze a határon túlra került."},
    {"id": "ex.b1.trianon.cons.19", "type": "fill-blank", "lesson": "lesson.b1.trianon.consolidation", "teaches": ["bekediktatum"], "prompt": "A trianoni *békediktátum* mély sebet ejtett a magyarság történetében.", "sentence": "A trianoni *békediktátum* mély sebet ejtett a magyarság történetében.", "target": "békediktátum"},
    {"id": "ex.b1.trianon.cons.20", "type": "multiple-choice", "lesson": "lesson.b1.trianon.consolidation", "teaches": ["Alaptorveny-nemzeti-felelosseg"], "prompt": "Mit fejez ki Magyarország a határon túli magyarság iránt az Alaptörvényben?", "options": ["Felelősséget visel a sorsukért és támogatja közösségeik megmaradását", "Lemond róluk", "Kötelezi őket a hazatelepülésre", "Megtiltja a nyelvhasználatot"], "correctIndex": 0, "explanation": "Az Alaptörvény nemzeti felelősségvállalást rögzít a külhoni magyarságért."}
]
write_json(EXERCISES_DIR / "ex.b1.trianon.consolidation.json", make_exercise_group("ex.b1.trianon.consolidation", "A trianoni békediktátum összefoglaló", "Átfogó teszt 1920 eseményeiről: Apponyiról, az aláírásról, a veszteségekről, a menekültekről és a Nemzeti Összetartozás Napjáról.", cons_21_exs))

cons_21_lesson = {
    "id": "lesson.b1.trianon.consolidation",
    "title": "The Treaty of Trianon (1920): Unit 21 Consolidation",
    "level": "B1",
    "track": "citizenship",
    "estimatedMinutes": 25,
    "prerequisites": [
        "lesson.b1.trianon.01",
        "lesson.b1.trianon.02",
        "lesson.b1.trianon.03",
        "lesson.b1.trianon.04",
        "lesson.b1.trianon.05"
    ],
    "grammar": ["Unit review"],
    "vocabulary": ["Unit review"],
    "culturalContext": "Magyar történelem összefoglalás (Honosítási vizsgafelkészítő)",
    "sections": [
        {
            "type": "intro",
            "title": "Unit 21 Consolidation: The Treaty of Trianon (1920)",
            "body": "Ebben az összefoglaló leckében áttekintjük a párizsi békekonferenciát és Apponyi Albert védőbeszédét (1920. jan. 16.), a trianoni békediktátum aláírását (1920. június 4. 16:32), a területi (2/3) és népességi (3,3 millió határon túli magyar) veszteségeket, a budapesti vagonlakók menekültválságát, valamint a Nemzeti Összetartozás Napját (június 4.) és a kedvezményes honosítást."
        },
        {
            "type": "goal",
            "title": "Consolidation Goals",
            "items": [
                "A trianoni döntés kulcsdátumainak (1920. június 4., 2010. június 4.) és számainak (2/3 terület, 3,3 millió magyar) biztos ismerete",
                "Érvelést, időpontot, arányokat és kényszerűséget leíró nyelvtani szerkezetek magabiztos alkalmazása",
                "A 21. századi nemzeti összetartozás és a kedvezményes honosítás fogalmának megértése"
            ]
        },
        {
            "type": "exercise-group",
            "title": "Comprehensive Unit 21 Practice",
            "ref": "ex.b1.trianon.consolidation",
            "exerciseRefs": [e["id"] for e in cons_21_exs]
        },
        {
            "type": "checklist",
            "items": [
                "Tudom Apponyi Albert védőbeszédének és a vörös térképnek a jelentőségét",
                "Ismerem az 1920. június 4-i aláírás körülményeit és a nemzeti gyászt",
                "Megértem a 2/3-os területi és a 3,3 milliós emberi veszteségeket",
                "Ismerem a vagonlakók sorsát, a Nemzeti Összetartozás Napját és a honosítást"
            ]
        }
    ]
}
write_json(LESSONS_DIR / "lesson.b1.trianon.consolidation.json", cons_21_lesson)

print("Units 19, 20, 21 complete!")
