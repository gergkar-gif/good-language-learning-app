#!/usr/bin/env python3
"""Generate Hungarian B1 Core Unit 14: Technology & Communication (b1-14)."""

import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def write_json(rel_path, data):
    full_path = os.path.join(ROOT, rel_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print(f"Wrote {rel_path}")

def build_unit_14_core():
    # -------------------------------------------------------------------------
    # 1. Vocabulary Files (4 words each = 20 words total)
    # -------------------------------------------------------------------------
    voc_01 = {
        "id": "vocab.b1.14.01",
        "lesson": "b1-14-01",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "okoseszköz", "translation": "smart device", "pos": "noun"},
            {"lemma": "mesterséges intelligencia", "translation": "artificial intelligence", "pos": "noun"},
            {"lemma": "fejlesztés", "translation": "development, enhancement", "pos": "noun"},
            {"lemma": "felhasználó", "translation": "user", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-14-01-voc.json", voc_01)

    voc_02 = {
        "id": "vocab.b1.14.02",
        "lesson": "b1-14-02",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "üzenetküldés", "translation": "messaging, text messaging", "pos": "noun"},
            {"lemma": "közösségi média", "translation": "social media", "pos": "noun"},
            {"lemma": "értesítés", "translation": "notification, alert", "pos": "noun"},
            {"lemma": "hálózat", "translation": "network, web", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-14-02-voc.json", voc_02)

    voc_03 = {
        "id": "vocab.b1.14.03",
        "lesson": "b1-14-03",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "képernyőidő", "translation": "screen time", "pos": "noun"},
            {"lemma": "adatvédelem", "translation": "data protection, privacy", "pos": "noun"},
            {"lemma": "függőség", "translation": "addiction, dependency", "pos": "noun"},
            {"lemma": "kiberbiztonság", "translation": "cybersecurity", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-14-03-voc.json", voc_03)

    voc_04 = {
        "id": "vocab.b1.14.04",
        "lesson": "b1-14-04",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "alkalmazás", "translation": "application, app", "pos": "noun"},
            {"lemma": "beállítás", "translation": "settings, configuration", "pos": "noun"},
            {"lemma": "frissítés", "translation": "update, refresh", "pos": "noun"},
            {"lemma": "kezelőfelület", "translation": "user interface", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-14-04-voc.json", voc_04)

    voc_05 = {
        "id": "vocab.b1.14.05",
        "lesson": "b1-14-05",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "távmunka", "translation": "remote work, telecommuting", "pos": "noun"},
            {"lemma": "digitális írástudás", "translation": "digital literacy", "pos": "noun"},
            {"lemma": "automatizálás", "translation": "automation", "pos": "noun"},
            {"lemma": "mindennapi rutin", "translation": "daily routine", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-14-05-voc.json", voc_05)

    # -------------------------------------------------------------------------
    # 2. Grammar Files
    # -------------------------------------------------------------------------
    gr_01_a = {
        "id": "grammar.b1.14.01.future-participle-ando",
        "title": "The Future / Obligatory Participle in -andó / -endő",
        "sections": [
            {
                "type": "text",
                "title": "Formation and Core Meaning: That Which Must / Will Be Done",
                "content": "The suffix *-andó / -endő* attaches to verb stems to express obligation or future action: *megoldandó feladat* (a task to be solved / that must be solved), *követendő példa* (an example to be followed), *fejlesztendő terület* (an area to be developed)."
            },
            {
                "type": "examples",
                "title": "Examples of -andó / -endő",
                "items": [
                    {
                        "spanish": "A digitális átállás során sok a megoldandó probléma.",
                        "english": "During the digital transition, there are many problems to be solved."
                    },
                    {
                        "spanish": "A biztonságos jelszó használata mindenki számára követendő szabály.",
                        "english": "Using a secure password is a rule to be followed by everyone."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-14-01-a-gr.json", gr_01_a)

    gr_01_b = {
        "id": "grammar.b1.14.01.participle-obligations",
        "title": "Participles in Tech Tasks: elvégzendő, megválaszolandó",
        "sections": [
            {
                "type": "text",
                "title": "Task Management Register in Hungarian",
                "content": "In technical and professional contexts, the *-andó / -endő* participle acts as a concise adjective: *az elvégzendő munka* ('the work to be done'), *a megválaszolandó üzenetek* ('the messages to be answered')."
            },
            {
                "type": "examples",
                "title": "Task participle examples",
                "items": [
                    {
                        "spanish": "Reggel átnézem az elvégzendő feladatok listáját a telefonomon.",
                        "english": "In the morning I review the list of tasks to be completed on my phone."
                    },
                    {
                        "spanish": "A mérnökök kijelölték a sürgősen tesztelendő funkciókat.",
                        "english": "The engineers designated the features to be tested urgently."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-14-01-b-gr.json", gr_01_b)

    gr_02_a = {
        "id": "grammar.b1.14.02.spatial-internet-postpositions",
        "title": "Expressing Virtual Location & Motion: -n/-on, felé, felületen",
        "sections": [
            {
                "type": "text",
                "title": "Digital Spatial Postpositions and Suffixes",
                "content": "Hungarian consistently uses the superessive (*-on/-en/-ön*) for digital media: *az interneten* (on the internet), *a közösségi médián* (on social media), *a kezelőfelületen* (on the user interface), *a hálózaton keresztül* (across the network)."
            },
            {
                "type": "examples",
                "title": "Digital location examples",
                "items": [
                    {
                        "spanish": "A hálózaton keresztül másodpercek alatt elküldhetjük a fájlokat.",
                        "english": "Across the network we can send files in a matter of seconds."
                    },
                    {
                        "spanish": "A közösségi médián rengeteg új értesítés vár ránk.",
                        "english": "A lot of new notifications await us on social media."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-14-02-a-gr.json", gr_02_a)

    gr_02_b = {
        "id": "grammar.b1.14.02.verbal-prefixes-telecom",
        "title": "Verbal Prefixes in Communication: fel-, le-, át-, be-",
        "sections": [
            {
                "type": "text",
                "title": "Action Prefixes in Tech",
                "content": "Tech terms use directional prefixes metaphorically: *letölt* (download), *feltölt* (upload), *beállít* (configure/set), *átküld* (forward/send over), *bekapcsol* (turn on)."
            },
            {
                "type": "examples",
                "title": "Prefixes in action",
                "items": [
                    {
                        "spanish": "Kérlek, töltsd le a legújabb frissítést az alkalmazáshoz!",
                        "english": "Please download the latest update for the app!"
                    },
                    {
                        "spanish": "Azonnal átküldöm neked a dokumentumot az üzenetküldőn.",
                        "english": "I will immediately send the document over to you on the messenger."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-14-02-b-gr.json", gr_02_b)

    gr_03_a = {
        "id": "grammar.b1.14.03.expressing-risks-causes",
        "title": "Expressing Risks and Consequences: veszélyeztet, függőséget okoz",
        "sections": [
            {
                "type": "text",
                "title": "Causal Verbs of Risk",
                "content": "To discuss the risks of digital technology, use transitive causation: *függőséget okoz* (causes addiction), *veszélyezteti az adatvédelmet* (threatens data protection), *káros hatással van valamire* (has a harmful effect on)."
            },
            {
                "type": "examples",
                "title": "Risk expressions",
                "items": [
                    {
                        "spanish": "A túlzott képernyőidő rontja a szemünket és alvászavart okoz.",
                        "english": "Excessive screen time damages our eyes and causes sleep disorders."
                    },
                    {
                        "spanish": "A gondatlan jelszóválasztás komolyan veszélyezteti a kiberbiztonságot.",
                        "english": "Careless password choice seriously threatens cybersecurity."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-14-03-a-gr.json", gr_03_a)

    gr_03_b = {
        "id": "grammar.b1.14.03.prevention-modalities",
        "title": "Preventive Advice: elkerülése érdekében, óvintézkedésként",
        "sections": [
            {
                "type": "text",
                "title": "Expressing Preventive Measures",
                "content": "Formal advice uses purpose postpositional structures: *a veszély elkerülése érdekében* (in order to avoid danger), *óvintézkedésként* (as a precaution), *megelőzés céljából* (for prevention purposes)."
            },
            {
                "type": "examples",
                "title": "Prevention examples",
                "items": [
                    {
                        "spanish": "Az adatvesztés elkerülése érdekében rendszeresen készítsünk biztonsági mentést!",
                        "english": "In order to avoid data loss, let us make regular backup copies!"
                    },
                    {
                        "spanish": "A kiberbiztonság megőrzése érdekében kétlépcsős azonosítást használunk.",
                        "english": "In order to preserve cybersecurity, we use two-step verification."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-14-03-b-gr.json", gr_03_b)

    gr_04_a = {
        "id": "grammar.b1.14.04.instructing-processes",
        "title": "Giving Technical Instructions: kattintson a..., válassza ki a...",
        "sections": [
            {
                "type": "text",
                "title": "Instructional Imperatives in Software Menus",
                "content": "Software manuals use third-person polite imperative (*-jon/-jen/-szon*): *Kattintson a beállítások menüre* (Click on the settings menu), *Válassza ki a megfelelő opciót* (Select the appropriate option)."
            },
            {
                "type": "examples",
                "title": "Technical instruction examples",
                "items": [
                    {
                        "spanish": "Nyissa meg a beállításokat, és frissítse a programot!",
                        "english": "Open the settings and update the program!"
                    },
                    {
                        "spanish": "Érintse meg a képernyőt a menü megjelenítéséhez!",
                        "english": "Tap the screen to display the menu!"
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-14-04-a-gr.json", gr_04_a)

    gr_04_b = {
        "id": "grammar.b1.14.04.conditional-troubleshooting",
        "title": "Troubleshooting Conditionals: amennyiben nem működik, ha lefagy",
        "sections": [
            {
                "type": "text",
                "title": "Formal Conditional Registers in Troubleshooting",
                "content": "Troubleshooting guides frequently employ *amennyiben* ('in the event that / should it...') or standard *ha*: *Amennyiben a telefon lefagy, indítsa újra a készüléket.*"
            },
            {
                "type": "examples",
                "title": "Troubleshooting examples",
                "items": [
                    {
                        "spanish": "Amennyiben hibaüzenet jelenik meg, ellenőrizze az internetkapcsolatot!",
                        "english": "Should an error message appear, check the internet connection!"
                    },
                    {
                        "spanish": "Ha az alkalmazás nem indul el, törölje és telepítse újra!",
                        "english": "If the application does not start, delete and reinstall it!"
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-14-04-b-gr.json", gr_04_b)

    gr_05_a = {
        "id": "grammar.b1.14.05.transformative-valik",
        "title": "Expressing Transformation: automatizálttá válik, nélkülözhetetlen lesz",
        "sections": [
            {
                "type": "text",
                "title": "Translative Transformations with válni",
                "content": "To describe how modern life shifts through technology, combine translative *-vá/-vé* with *válik*: *A távmunka elterjedtté vált.* (Remote work has become widespread.) *A digitális írástudás nélkülözhetetlenné válik.* (Digital literacy is becoming indispensable.)"
            },
            {
                "type": "examples",
                "title": "Transformation examples",
                "items": [
                    {
                        "spanish": "Az okostelefon a mindennapi élet nélkülözhetetlen részévé vált.",
                        "english": "The smartphone has become an indispensable part of everyday life."
                    },
                    {
                        "spanish": "Sok monoton irodai munka mára teljesen automatizálttá lett.",
                        "english": "Many monotonous office jobs have by now become completely automated."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-14-05-a-gr.json", gr_05_a)

    gr_05_b = {
        "id": "grammar.b1.14.05.comparing-past-present-tech",
        "title": "Contrasting Tech Eras: míg korábban... addig manapság...",
        "sections": [
            {
                "type": "text",
                "title": "Temporal Contrast Discourse Markers",
                "content": "Use correlative contrasts to compare lifestyle changes: *Míg korábban órákig tartott az ügyintézés, addig manapság néhány kattintással elintézhető.*"
            },
            {
                "type": "examples",
                "title": "Contrasting eras",
                "items": [
                    {
                        "spanish": "Míg korábban könyvtárba jártunk információért, addig manapság a zsebünkben van a tudás.",
                        "english": "Whereas earlier we went to the library for information, nowadays knowledge is in our pocket."
                    },
                    {
                        "spanish": "Míg régen levélben tartottuk a kapcsolatot, addig ma azonnal látjuk egymást videón.",
                        "english": "Whereas in the past we stayed in touch by letter, today we instantly see each other on video."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-14-05-b-gr.json", gr_05_b)

    # -------------------------------------------------------------------------
    # 3. Classic Literature Story: Karinthy Frigyes: A delejes gépember és a jövő
    # -------------------------------------------------------------------------
    classic_story = {
        "id": "story.b1.14.classic",
        "title": "A delejes gépember és a jövő masinái",
        "level": "B1",
        "order": 14,
        "type": "classics",
        "estimatedMinutes": 7,
        "summary": "An adaptation inspired by the visionary satirical writings of Frigyes Karinthy on technology, thinking machines, and communication. Karinthy visits an eccentric inventor's workshop in Budapest, where a thinking metal machine attempts to write poetry.",
        "characters": ["Karinthy Frigyes", "A professzor"],
        "location": "Budapest, New York kávéház és műhely",
        "author": "Karinthy Frigyes",
        "work": "Így írtok ti / Tanár úr kérem és egyéb tárcák",
        "historicalContext": "Frigyes Karinthy (1887–1938) was Hungary's most celebrated humorist, philosopher, and science-fiction pioneer. He coined the 'six degrees of separation' concept in 1929 and was fascinated by radio, airplanes, and automata.",
        "readingQuestions": [
            {
                "question": "Milyen különleges szerkezetet mutatott be a professzor Karinthynak?",
                "options": [
                    "Egy delejes gondolkodógépet, amely verseket próbált írni.",
                    "Egy gőzzel működő zongorát.",
                    "Egy fából faragott lovaskocsit."
                ],
                "correct": 0,
                "explanation": "A professzor egy automatizált, delejes masinát készített, amely az emberi gondolkodást és a költészetet igyekezett utánozni."
            },
            {
                "question": "Hogyan reagált Karinthy a gép által írt első verssorra?",
                "options": [
                    "Jókedvűen felnevetett, és megjegyezte, hogy a gép stílusa kísértetiesen hasonlít a modern költőkére.",
                    "Megijedt és kimenekült a szobából.",
                    "Azonnal összetörte a masinát a sétapálcájával."
                ],
                "correct": 0,
                "explanation": "Karinthy a rá jellemző szellemes iróniával állapította meg, hogy a gép pont olyan értelmetlen rímeket farag, mint némely kortárs költő."
            },
            {
                "question": "Mi Karinthy filozófiai tanulsága a technikai fejlődésről?",
                "options": [
                    "Hogy a gép bármilyen okos is lehet, az emberi lélek és a szeretet nem helyettesíthető.",
                    "Hogy a gépeket be kell tiltani a városokban.",
                    "Hogy az embereknek nem kell többé iskolába járniuk."
                ],
                "correct": 0,
                "explanation": "Karinthy szerint a technika megkönnyítheti az életet, de a valódi művészet és az emberi érzés mindig megismételhetetlen marad."
            }
        ],
        "paragraphs": [
            {
                "type": "narration",
                "text": "A pesti kávéház füstös sarkában a különc professzor egy nagy, sárgaréz alkatrészekből álló dobozt tett az asztalra. Karinthy Frigyes kíváncsian hajolt közelebb."
            },
            {
                "type": "dialogue",
                "speaker": "A professzor",
                "text": "Nézze csak, kedves barátom! Ez a jövő csodája: egy automata delejes készülék, amely gombok nyomására gondolatokat közvetít!"
            },
            {
                "type": "narration",
                "text": "A szerkezet belsejében fogaskerekek kattogtak, apró villanykörték gyúltak ki, és a gép finom zümmögéssel életre kelt."
            },
            {
                "type": "dialogue",
                "speaker": "Karinthy Frigyes",
                "text": "Bámulatos! De vajon meg tudja-e oldani a legnehezebb feladatot? Képes-e ez a fémdoboz szerelmes verset írni a New York kávéház kisasszonyának?"
            },
            {
                "type": "narration",
                "text": "A professzor beállította a kart, és a gép egy hosszú papírcsíkot dobott ki. Karinthy felolvasta a szöveget: 'A delej kattog, a lélek csattog, jaj, de hideg a vas!'"
            },
            {
                "type": "dialogue",
                "speaker": "Karinthy Frigyes",
                "text": "Egészen kiváló modern költemény! Ha nem mondja, hogy masina költötte, azt hinném, a legújabb folyóirat vezércikke!"
            },
            {
                "type": "narration",
                "text": "A vendégek körülöttük nevetésben törtek ki. Karinthy elgondolkodva simította meg a hideg fémet: a jövő gépei bármilyen okosak is lesznek, a nevetést soha nem tanulják meg."
            },
            {
                "type": "dialogue",
                "speaker": "Karinthy Frigyes",
                "text": "A technika nagyszerű szolga, de veszedelmes úr. Tanuljunk meg embernek maradni a masinák között!"
            }
        ]
    }
    write_json("content/hu/stories/classics/b1/b1-14-karinthy.json", classic_story)

    # -------------------------------------------------------------------------
    # 4. Exercises Files (01 to 05 + consolidation)
    # -------------------------------------------------------------------------
    ex_01 = {
        "lesson": "b1-14-01",
        "exercises": [
            {
                "id": "b1-14-01.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["okoseszköz", "smart device"],
                    ["mesterséges intelligencia", "artificial intelligence"],
                    ["fejlesztés", "advancement / development"],
                    ["felhasználó", "user"]
                ]
            },
            {
                "id": "b1-14-01.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik szóalak fejezi ki, hogy a feladatot kötelező elvégezni?",
                "options": [
                    "elvégzendő",
                    "elvégzett",
                    "elvégezhető"
                ],
                "correct": 0
            },
            {
                "id": "b1-14-01.ex03",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A kutatók szerint a ____ forradalmasítja az orvosi diagnosztikát. (artificial intelligence)",
                "answer": "mesterséges intelligencia"
            },
            {
                "id": "b1-14-01.ex04",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A biztonsági hiba miatt ez a legfontosabb ____ probléma a rendszerben. (to be solved)",
                "answer": "megoldandó"
            },
            {
                "id": "b1-14-01.ex05",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Hogyan nevezzük az internethez kapcsolódó intelligens készülékeket?",
                "options": [
                    "okoseszköz",
                    "postagalamb",
                    "gőzgép"
                ],
                "correct": 0
            },
            {
                "id": "b1-14-01.ex06",
                "type": "sentence-builder",
                "category": "grammar",
                "sentence": "A cég új okoseszközök fejlesztésén dolgozik a mindennapi élet megkönnyítésére.",
                "tiles": ["A", "cég", "új", "okoseszközök", "fejlesztésén", "dolgozik", "a", "mindennapi", "élet", "megkönnyítésére."]
            },
            {
                "id": "b1-14-01.ex07",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "Minden regisztrált ____ személyre szabott beállításokat választhat. (user)",
                "answer": "felhasználó"
            },
            {
                "id": "b1-14-01.ex08",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Miért fontos a technológiai fejlesztések etikus alkalmazása?",
                "options": [
                    "Mert az új eszközöknek az ember javát kell szolgálniuk, nem a kizsákmányolását.",
                    "Mert a gépek nem szeretnek áramot fogyasztani.",
                    "Mert a számítógépek csak hétvégén működnek jól."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-14-01-ex.json", ex_01)

    ex_02 = {
        "lesson": "b1-14-02",
        "exercises": [
            {
                "id": "b1-14-02.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["üzenetküldés", "instant messaging"],
                    ["közösségi média", "social media"],
                    ["értesítés", "notification / alert"],
                    ["hálózat", "network"]
                ]
            },
            {
                "id": "b1-14-02.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik ragot használjuk a virtuális térben való tartózkodásra?",
                "options": [
                    "-on / -en / -ön (az interneten, a hálózaton)",
                    "-ban / -ben (a netben)",
                    "-ból / -ből (a médiából)"
                ],
                "correct": 0
            },
            {
                "id": "b1-14-02.ex03",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A telefonomon kikapcsoltam az összes hangos ____, hogy tudjak koncentrálni. (notification)",
                "answer": "értesítést"
            },
            {
                "id": "b1-14-02.ex04",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Kérlek, töltsd ____ a fájlt a számítógépedre! (down)",
                "answer": "le"
            },
            {
                "id": "b1-14-02.ex05",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Melyik felületen tartanak kapcsolatot a barátok fotók és posztok megosztásával?",
                "options": [
                    "a közösségi médián",
                    "a telefonkönyvben",
                    "a vasúti menetrendben"
                ],
                "correct": 0
            },
            {
                "id": "b1-14-02.ex06",
                "type": "sentence-builder",
                "category": "grammar",
                "sentence": "A modern hálózat segítségével a Föld túlsó felén élő rokonainkkal is beszélhetünk.",
                "tiles": ["A", "modern", "hálózat", "segítségével", "a", "Föld", "túlsó", "felén", "élő", "rokonainkkal", "is", "beszélhetünk."]
            },
            {
                "id": "b1-14-02.ex07",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A gyors mobil ____ teljesen felváltotta a hagyományos postai levelezést. (messaging)",
                "answer": "üzenetküldés"
            },
            {
                "id": "b1-14-02.ex08",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Mi az online kapcsolattartás legnagyobb előnye?",
                "options": [
                    "A távolságok megszűnése és az azonnali információcserének lehetősége.",
                    "Hogy soha nem kell senkivel személyesen találkozni.",
                    "Hogy a telefonok ingyen kaphatók a boltokban."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-14-02-ex.json", ex_02)

    ex_03 = {
        "lesson": "b1-14-03",
        "exercises": [
            {
                "id": "b1-14-03.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["képernyőidő", "screen time"],
                    ["adatvédelem", "data protection"],
                    ["függőség", "addiction / dependency"],
                    ["kiberbiztonság", "cybersecurity"]
                ]
            },
            {
                "id": "b1-14-03.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik kifejezéssel adunk hivatalos megelőző tanácsot?",
                "options": [
                    "az adatvesztés elkerülése érdekében",
                    "az adatvesztés kedvéért",
                    "az adatvesztés ellenére"
                ],
                "correct": 0
            },
            {
                "id": "b1-14-03.ex03",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A szakemberek szerint a napi öt órát meghaladó ____ káros a gyermekek fejlődésére. (screen time)",
                "answer": "képernyőidő"
            },
            {
                "id": "b1-14-03.ex04",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A pénzügyi adatok védelmében kiemelten fontos a szigorú ____. (cybersecurity)",
                "answer": "kiberbiztonság"
            },
            {
                "id": "b1-14-03.ex05",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Hogyan hívjuk azt az állapotot, amikor valaki képtelen letenni a telefonját?",
                "options": [
                    "digitális függőség",
                    "jókedvű pihenés",
                    "egészséges sportolás"
                ],
                "correct": 0
            },
            {
                "id": "b1-14-03.ex06",
                "type": "sentence-builder",
                "category": "grammar",
                "sentence": "A személyes adatvédelem megsértése súlyos jogi következményekkel járhat az interneten.",
                "tiles": ["A", "személyes", "adatvédelem", "megsértése", "súlyos", "jogi", "következményekkel", "járhat", "az", "interneten."]
            },
            {
                "id": "b1-14-03.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A vírusfertőzések megelőzése ____ soha ne nyissunk meg gyanús e-maileket! (in order to / for the purpose of)",
                "answer": "érdekében"
            },
            {
                "id": "b1-14-03.ex08",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Milyen módszerrel csökkenthetjük az okostelefon-függőséget?",
                "options": [
                    "Tudatos digitális szünetekkel és a képernyőidő ésszerű korlátozásával.",
                    "Ha még több játékot töltünk le a telefonra.",
                    "Ha éjszaka sem kapcsoljuk ki az értesítéseket."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-14-03-ex.json", ex_03)

    ex_04 = {
        "lesson": "b1-14-04",
        "exercises": [
            {
                "id": "b1-14-04.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["alkalmazás", "application / app"],
                    ["beállítás", "settings / configuration"],
                    ["frissítés", "software update"],
                    ["kezelőfelület", "user interface"]
                ]
            },
            {
                "id": "b1-14-04.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Hogyan szól a felszólítás udvarias formája szoftvereknél?",
                "options": [
                    "Kattintson a mentés gombra!",
                    "Kattintsál a mentésre voltál!",
                    "Kattintani kellene lenni a mentéshez!"
                ],
                "correct": 0
            },
            {
                "id": "b1-14-04.ex03",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A telefon új operációs rendszere sokkal letisztultabb és átláthatóbb ____ kapott. (user interface)",
                "answer": "kezelőfelületet"
            },
            {
                "id": "b1-14-04.ex04",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A banki ____ segítségével sorban állás nélkül fizethetjük be a számlákat. (app)",
                "answer": "alkalmazás"
            },
            {
                "id": "b1-14-04.ex05",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit kell letölteni a programhoz, ha javítani akarják a hibáit?",
                "options": [
                    "egy frissítést",
                    "egy konyhai receptet",
                    "egy régi újságot"
                ],
                "correct": 0
            },
            {
                "id": "b1-14-04.ex06",
                "type": "sentence-builder",
                "category": "grammar",
                "sentence": "Amennyiben a telefon lefagy indítsa újra a készüléket a főgomb hosszú megnyomásával.",
                "tiles": ["Amennyiben", "a", "telefon", "lefagy,", "indítsa", "újra", "a", "készüléket", "a", "főgomb", "hosszú", "megnyomásával."]
            },
            {
                "id": "b1-14-04.ex07",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A menüben módosíthatja a hangerő és a kijelző egyéni ____. (settings)",
                "answer": "beállításait"
            },
            {
                "id": "b1-14-04.ex08",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Mit jelent az, hogy egy alkalmazás felhasználóbarát?",
                "options": [
                    "Hogy a kezelőfelülete egyszerűen, logikusan és könnyen megtanulható.",
                    "Hogy az alkalmazás képeket rajzol a falra.",
                    "Hogy az alkalmazás csak angol nyelven működik."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-14-04-ex.json", ex_04)

    ex_05 = {
        "lesson": "b1-14-05",
        "exercises": [
            {
                "id": "b1-14-05.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["távmunka", "remote work / telework"],
                    ["digitális írástudás", "digital literacy"],
                    ["automatizálás", "automation"],
                    ["mindennapi rutin", "daily routine"]
                ]
            },
            {
                "id": "b1-14-05.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik igével fejezzük ki a tartós átalakulást: 'A digitális eszközök nélkülözhetetlenné...'?",
                "options": [
                    "váltak",
                    "álltak",
                    "ültek"
                ],
                "correct": 0
            },
            {
                "id": "b1-14-05.ex03",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A járvány óta sok munkavállaló számára a teljes vagy részleges ____ lett az alapértelmezett. (remote work)",
                "answer": "távmunka"
            },
            {
                "id": "b1-14-05.ex04",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A modern munkaerőpiacon elengedhetetlen a magas szintű ____ elsajátítása. (digital literacy)",
                "answer": "digitális írástudás"
            },
            {
                "id": "b1-14-05.ex05",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent a munkafolyamatok gépesítése és szoftveres irányítása emberi beavatkozás nélkül?",
                "options": [
                    "automatizálás",
                    "kézi szövés",
                    "lóháton utazás"
                ],
                "correct": 0
            },
            {
                "id": "b1-14-05.ex06",
                "type": "sentence-builder",
                "category": "grammar",
                "sentence": "Míg korábban a gyárakban mindent kézzel végeztek addig mára sok folyamat automatizálttá vált.",
                "tiles": ["Míg", "korábban", "a", "gyárakban", "mindent", "kézzel", "végeztek,", "addig", "mára", "sok", "folyamat", "automatizálttá", "vált."]
            },
            {
                "id": "b1-14-05.ex07",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "Az ébredés utáni hírolvasás a reggeli ____ szerves részévé vált. (daily routine)",
                "answer": "mindennapi rutin"
            },
            {
                "id": "b1-14-05.ex08",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Hogyan vélekedett Karinthy Frigyes az ember és a gép kapcsolatáról?",
                "options": [
                    "A gépek csodálatosak, de az emberi melegséget, humort és szeretetet soha nem pótolhatják.",
                    "Hogy a gőzgépeket le kell szerelni az összes vonatról.",
                    "Hogy az embereknek gépként kellene viselkedniük."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-14-05-ex.json", ex_05)

    ex_consolidation = {
        "lesson": "b1-14-consolidation",
        "exercises": [
            {
                "id": "b1-14-consolidation.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["okoseszköz", "smart device"],
                    ["adatvédelem", "data privacy"],
                    ["kezelőfelület", "user interface"],
                    ["távmunka", "remote work"]
                ]
            },
            {
                "id": "b1-14-consolidation.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik mondatban szerepel helyesen a beálló melléknévi igenév?",
                "options": [
                    "A holnap elvégzendő feladatokat pontosan be kell osztani.",
                    "A tegnap elvégzendő munkát már befejeztük volt.",
                    "Az elvégzendeni munka készen állott."
                ],
                "correct": 0
            },
            {
                "id": "b1-14-consolidation.ex03",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A digitális korban a megfelelő jelszavak használata alapvető ____ kérdés. (cybersecurity)",
                "answer": "kiberbiztonsági"
            },
            {
                "id": "b1-14-consolidation.ex04",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Az új technológiák segítségével sok nehéz folyamat teljesen automatizálttá ____. (became / has become)",
                "answer": "vált"
            },
            {
                "id": "b1-14-consolidation.ex05",
                "type": "sentence-builder",
                "category": "grammar",
                "sentence": "A rendszeres szoftverfrissítés elengedhetetlen a telefon zavartalan működéséhez.",
                "tiles": ["A", "rendszeres", "szoftverfrissítés", "elengedhetetlen", "a", "telefon", "zavartalan", "működéséhez."]
            },
            {
                "id": "b1-14-consolidation.ex06",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Miért hasznos a mobil üzenetküldés a mindennapokban?",
                "options": [
                    "Mert gyors és rugalmas kapcsolattartást tesz lehetővé a családdal és kollégákkal.",
                    "Mert elnémítja a rádiót a szobában.",
                    "Mert helyettesíti a napi testmozgást."
                ],
                "correct": 0
            },
            {
                "id": "b1-14-consolidation.ex07",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "Az új mobiltelefonos ____ segítségével könnyedén ellenőrizhetjük a vonatmenetrendet. (app)",
                "answer": "alkalmazás"
            },
            {
                "id": "b1-14-consolidation.ex08",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Milyen tanácsot adna egy tudatos okostelefon-használó?",
                "options": [
                    "Használjuk a technológiát okosan, de iktassunk be képernyőmentes időt is a pihenésre.",
                    "Töltsünk napi tizenöt órát folyamatosan a kijelző előtt.",
                    "Soha ne válaszoljunk a barátaink üzeneteire."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-14-consolidation-ex.json", ex_consolidation)

    # -------------------------------------------------------------------------
    # 5. Lesson Files (01 to 05 + consolidation)
    # -------------------------------------------------------------------------
    for i in range(1, 6):
        padded = f"0{i}"
        titles = {
            "01": ("What's About to Change", "A digitális fordulat"),
            "02": ("Staying in Touch", "Kapcsolattartás a hálón"),
            "03": ("The Upsides & Downsides", "Előnyök és kockázatok"),
            "04": ("Explaining How an App Works", "Alkalmazások és eszközök"),
            "05": ("Technology in Daily Life", "Technológia a mindennapokban")
        }
        en_title, hu_title = titles[padded]
        lesson_data = {
            "id": f"lesson.b1.14-{padded}",
            "unit": 14,
            "title": en_title,
            "level": "B1",
            "grammar": "Future and Obligatory Participle (-andó/-endő) in Technology",
            "goal": [
                f"I can understand and use vocabulary for {en_title.lower()}.",
                "I can express future and obligatory actions with -andó / -endő.",
                "I can discuss smart devices, cybersecurity, and digital lifestyle in Hungarian.",
                "I can master four new target vocabulary items in authentic context."
            ],
            "sections": [
                {
                    "type": "goal",
                    "title": "Lesson Goals",
                    "items": [
                        f"I can understand and use vocabulary for {en_title.lower()}.",
                        "I can express future and obligatory actions with -andó / -endő.",
                        "I can discuss smart devices, cybersecurity, and digital lifestyle in Hungarian.",
                        "I can master four new target vocabulary items in authentic context."
                    ]
                },
                {"type": "recycle", "title": "Quick Review"},
                {"type": "grammar", "ref": f"grammar/b1/b1-14-{padded}-a-gr.json"},
                {"type": "grammar", "ref": f"grammar/b1/b1-14-{padded}-b-gr.json"},
                {"type": "vocabulary", "title": "Lesson Vocabulary", "ref": f"vocabulary/b1/b1-14-{padded}-voc.json"},
                {
                    "type": "practice",
                    "title": "Practice",
                    "ref": f"exercises/b1/b1-14-{padded}-ex.json"
                }
            ]
        }
        write_json(f"content/hu/lessons/b1/b1-14-{padded}.json", lesson_data)

    consolidation_data = {
        "id": "lesson.b1.14-consolidation",
        "unit": 14,
        "title": "Unit 14 Consolidation",
        "level": "B1",
        "grammar": "Consolidation of Tech Participles & Digital Literacy",
        "sections": [
            {
                "type": "story",
                "title": "A delejes gépember és a jövő masinái",
                "ref": "stories/classics/b1/b1-14-karinthy.json"
            },
            {
                "type": "practice",
                "title": "Consolidation Practice",
                "ref": "exercises/b1/b1-14-consolidation-ex.json"
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-14-consolidation.json", consolidation_data)
    print("Successfully built Hungarian B1 Core Unit 14 (b1-14)!")

if __name__ == "__main__":
    build_unit_14_core()
