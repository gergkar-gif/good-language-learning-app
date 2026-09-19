#!/usr/bin/env python3
"""Generate Hungarian B1 Core Unit 22: Possibilities & Predictions (b1-22)."""

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

def build_unit_22_core():
    # -------------------------------------------------------------------------
    # 1. Vocabulary Files (4 words each = 20 words total)
    # -------------------------------------------------------------------------
    voc_01 = {
        "id": "vocab.b1.22.01",
        "lesson": "b1-22-01",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "lehetőség", "translation": "possibility, opportunity", "pos": "noun"},
            {"lemma": "valószínűség", "translation": "probability, likelihood", "pos": "noun"},
            {"lemma": "kockázat", "translation": "risk, hazard", "pos": "noun"},
            {"lemma": "esély", "translation": "chance, odds", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-22-01-voc.json", voc_01)

    voc_02 = {
        "id": "vocab.b1.22.02",
        "lesson": "b1-22-02",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "előrejelzés", "translation": "forecast, projection", "pos": "noun"},
            {"lemma": "jóslat", "translation": "prediction, prophecy", "pos": "noun"},
            {"lemma": "jövőkép", "translation": "vision of the future", "pos": "noun"},
            {"lemma": "távlat", "translation": "prospect, perspective, long-term outlook", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-22-02-voc.json", voc_02)

    voc_03 = {
        "id": "vocab.b1.22.03",
        "lesson": "b1-22-03",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "kétség", "translation": "doubt, hesitation", "pos": "noun"},
            {"lemma": "kétkedés", "translation": "skepticism, disbelief", "pos": "noun"},
            {"lemma": "bizakodás", "translation": "optimism, hopefulness", "pos": "noun"},
            {"lemma": "számítás", "translation": "calculation, expectation", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-22-03-voc.json", voc_03)

    voc_04 = {
        "id": "vocab.b1.22.04",
        "lesson": "b1-22-04",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "elképzelhető", "translation": "conceivable, imaginable", "pos": "adjective"},
            {"lemma": "kiszámíthatatlan", "translation": "unpredictable, erratic", "pos": "adjective"},
            {"lemma": "véletlen", "translation": "coincidence, accident, chance event", "pos": "noun"},
            {"lemma": "megérzés", "translation": "hunch, intuition, gut feeling", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-22-04-voc.json", voc_04)

    voc_05 = {
        "id": "vocab.b1.22.05",
        "lesson": "b1-22-05",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "forgatókönyv", "translation": "scenario, projected plan", "pos": "noun"},
            {"lemma": "megvalósulás", "translation": "realization, fulfillment, coming true", "pos": "noun"},
            {"lemma": "eshetőség", "translation": "contingency, possibility, eventuality", "pos": "noun"},
            {"lemma": "várakozás", "translation": "expectation, anticipation", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-22-05-voc.json", voc_05)

    # -------------------------------------------------------------------------
    # 2. Grammar Files (2 per regular lesson = 10 files)
    # -------------------------------------------------------------------------
    gr_01_a = {
        "id": "grammar.b1.22.01.lehet-hogy",
        "title": "Expressing Possibility: Lehet, hogy...",
        "sections": [
            {
                "type": "text",
                "title": "Impersonal Modal 'Lehet, hogy...'",
                "content": "To express that an event is possible, Hungarian commonly uses *Lehet, hogy...* ('It is possible that...') followed by a clause in the indicative or conditional. Unlike English 'might/may', Hungarian handles this epistemic modality through the impersonal verb *lehet* or *megtörténhet, hogy...*."
            },
            {
                "type": "examples",
                "title": "Possibility in Context",
                "items": [
                    {
                        "spanish": "Lehet, hogy holnap megváltozik az időjárás, és kisüt a nap.",
                        "english": "It is possible that the weather will change tomorrow and the sun will shine."
                    },
                    {
                        "spanish": "Megtörténhet, hogy a vonat késéssel érkezik a pályaudvarra.",
                        "english": "It can happen that the train arrives at the station with a delay."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-22-01-a-gr.json", gr_01_a)

    gr_01_b = {
        "id": "grammar.b1.22.01.talan-esetleg",
        "title": "Adverbs of Possibility: talán, esetleg, hátha",
        "sections": [
            {
                "type": "text",
                "title": "Nuances of Possibility Adverbs",
                "content": "*Talán* indicates moderate uncertainty ('perhaps, maybe'). *Esetleg* suggests a tentative alternative or condition ('possibly, if so'). *Hátha* introduces an optimistic or wishful possibility ('who knows, perhaps / in the hope that')."
            },
            {
                "type": "examples",
                "title": "Subtle distinctions",
                "items": [
                    {
                        "spanish": "Talán érdemes lenne még egyszer átolvasni a szerződés feltételeit.",
                        "english": "Perhaps it would be worthwhile to read through the contract terms once more."
                    },
                    {
                        "spanish": "Siessünk, hátha még elérjük az utolsó villamost!",
                        "english": "Let's hurry, perhaps we can still catch the last tram!"
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-22-01-b-gr.json", gr_01_b)

    gr_02_a = {
        "id": "grammar.b1.22.02.future-auxiliary",
        "title": "Future Reference: The Auxiliary 'fog' vs. Present Tense",
        "sections": [
            {
                "type": "text",
                "title": "Forecasting with 'fog' + Infinitive",
                "content": "In predictions and official forecasts, Hungarian uses the auxiliary verb *fog* conjugated with an infinitive (*változni fog*, *emelkedni fognak az árak*). When the future action is already scheduled or certain, the present tense with a time adverb (*holnap indulok*) is preferred."
            },
            {
                "type": "examples",
                "title": "Future predictions",
                "items": [
                    {
                        "spanish": "Az előrejelzés szerint a következő években gyorsan növekedni fog a digitális gazdaság.",
                        "english": "According to the forecast, the digital economy will grow rapidly in the coming years."
                    },
                    {
                        "spanish": "A szakértők úgy látják, hogy új technológiák fognak megjelenni a piacon.",
                        "english": "Experts believe that new technologies will appear on the market."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-22-02-a-gr.json", gr_02_a)

    gr_02_b = {
        "id": "grammar.b1.22.02.minden-bizonnyal",
        "title": "High Probability vs. Low Probability: minden bizonnyal and aligha",
        "sections": [
            {
                "type": "text",
                "title": "Polarity of Predictions",
                "content": "*Minden bizonnyal* expresses strong likelihood ('in all probability, almost certainly'). Conversely, *aligha* expresses extreme skepticism or negative probability ('hardly, scarcely, unlikely to happen')."
            },
            {
                "type": "examples",
                "title": "Strong vs weak probability",
                "items": [
                    {
                        "spanish": "Minden bizonnyal sikerrel zárul a hosszú kutatómunka.",
                        "english": "In all probability, the lengthy research work will conclude successfully."
                    },
                    {
                        "spanish": "Aligha fogja bárki is kétségbe vonni az elért eredmények hitelességét.",
                        "english": "Hardly anyone will question the credibility of the achieved results."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-22-02-b-gr.json", gr_02_b)

    gr_03_a = {
        "id": "grammar.b1.22.03.ketlem-hogy",
        "title": "Expressing Doubt: Kétlem, hogy... / Semmi kétség",
        "sections": [
            {
                "type": "text",
                "title": "Verbs of Skepticism",
                "content": "*Kétlem, hogy...* ('I doubt that...') introduces a clause expressing disbelief. When there is zero doubt, Hungarian states *Semmi kétség nem fér hozzá, hogy...* ('There is no shadow of a doubt that...')."
            },
            {
                "type": "examples",
                "title": "Expressing doubt and certainty",
                "items": [
                    {
                        "spanish": "Kétlem, hogy a terv a jelenlegi költségvetéssel végrehajtható lenne.",
                        "english": "I doubt that the plan would be executable with the current budget."
                    },
                    {
                        "spanish": "Kétségtelen, hogy az új fejlesztés sok ember életét fogja megkönnyíteni.",
                        "english": "It is indubitable that the new development will make many people's lives easier."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-22-03-a-gr.json", gr_03_a)

    gr_03_b = {
        "id": "grammar.b1.22.03.szamitasok-szerint",
        "title": "Calculations and Optimism: Számításaink szerint, bízva abban",
        "sections": [
            {
                "type": "text",
                "title": "Projecting Expectations",
                "content": "*Számításaink szerint...* ('According to our calculations/estimates...') introduces analytical expectations. *Bízva abban, hogy...* ('In the hope/trust that...') or *bizakodással tekintünk a jövőbe* expresses grounded optimism."
            },
            {
                "type": "examples",
                "title": "Expectations in discourse",
                "items": [
                    {
                        "spanish": "A mérnökök számításai szerint a híd teherbírása tökéletesen elegendő lesz.",
                        "english": "According to the engineers' calculations, the load capacity of the bridge will be perfectly sufficient."
                    },
                    {
                        "spanish": "Bizakodással várjuk a tárgyalások kedvező kimenetelét.",
                        "english": "We await the favorable outcome of the negotiations with optimism."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-22-03-b-gr.json", gr_03_b)

    gr_04_a = {
        "id": "grammar.b1.22.04.elkepzelheto",
        "title": "Epistemic Modal Modifiers: Elképzelhető, hogy... / Kizárt dolog",
        "sections": [
            {
                "type": "text",
                "title": "Gradations of Conceivability",
                "content": "*Elképzelhető, hogy...* ('It is conceivable/imaginable that...'), *Könnyen megeshet, hogy...* ('It could easily happen that...'), and on the negative extreme: *Kizárt dolog, hogy...* ('It is ruled out / out of the question that...')."
            },
            {
                "type": "examples",
                "title": "Conceivability clauses",
                "items": [
                    {
                        "spanish": "Elképzelhető, hogy a technológia már tíz éven belül elterjed a mindennapokban.",
                        "english": "It is conceivable that the technology will spread in everyday life within ten years."
                    },
                    {
                        "spanish": "Kizárt dolog, hogy az emberi tényezőt teljesen ki lehessen iktatni.",
                        "english": "It is out of the question that the human factor could be completely eliminated."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-22-04-a-gr.json", gr_04_a)

    gr_04_b = {
        "id": "grammar.b1.22.04.veletlen-szeszelye",
        "title": "Randomness and Chance: Véletlenül, a sors szeszélye folytán",
        "sections": [
            {
                "type": "text",
                "title": "Expressing Coincidence",
                "content": "*Véletlenül* ('by chance, accidentally'), *a véletlen műve* ('the work of coincidence'), *a szerencsének köszönhetően* ('thanks to good fortune'), and *kiszámíthatatlan körülmények* ('unpredictable circumstances')."
            },
            {
                "type": "examples",
                "title": "Randomness idioms",
                "items": [
                    {
                        "spanish": "Nem a véletlen műve volt a felfedezés, hanem évek kitartó kísérletezése.",
                        "english": "The discovery was not the work of chance, but years of persistent experimentation."
                    },
                    {
                        "spanish": "A vihar kiszámíthatatlan erővel csapott le a tengerparti városra.",
                        "english": "The storm struck the coastal city with unpredictable force."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-22-04-b-gr.json", gr_04_b)

    gr_05_a = {
        "id": "grammar.b1.22.05.forgatokonyv-eshetoseg",
        "title": "Scenarios and Contingencies: Arra az esetre, ha...",
        "sections": [
            {
                "type": "text",
                "title": "Contingency Subordinators",
                "content": "*Arra az esetre / eshetőségre, ha...* ('In the event that / in case...'), *a legrosszabb forgatókönyv szerint* ('according to the worst-case scenario'), *minden eshetőségre készen állva* ('ready for every eventuality')."
            },
            {
                "type": "examples",
                "title": "Contingency planning",
                "items": [
                    {
                        "spanish": "Több különböző forgatókönyvet dolgoztunk ki a felmerülő kockázatok kezelésére.",
                        "english": "We worked out several different scenarios to manage the emerging risks."
                    },
                    {
                        "spanish": "Minden eshetőségre fel kell készülnünk, még a legváratlanabb eseményekre is.",
                        "english": "We must prepare for every contingency, even the most unexpected events."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-22-05-a-gr.json", gr_05_a)

    gr_05_b = {
        "id": "grammar.b1.22.05.valora-valik",
        "title": "Fulfillment: Valóra válik, beigazolódik",
        "sections": [
            {
                "type": "text",
                "title": "Fulfillment Verbs",
                "content": "To express that a prediction came true or materialized: *valóra válik* ('comes true'), *beigazolódik a jóslat* ('the prophecy is verified / confirmed'), *megvalósul az elképzelés* ('the concept is realized')."
            },
            {
                "type": "examples",
                "title": "Predictions coming true",
                "items": [
                    {
                        "spanish": "Végül valóra vált a merész jövőkép, amelyben sokáig csak kevesen hittek.",
                        "english": "In the end, the daring vision of the future came true, which for a long time only a few believed in."
                    },
                    {
                        "spanish": "A kutatók legoptimistább várakozásai is gyorsan beigazolódtak a tesztek során.",
                        "english": "Even the researchers' most optimistic expectations were quickly verified during testing."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-22-05-b-gr.json", gr_05_b)

    # -------------------------------------------------------------------------
    # 3. Exercise Files (01 to 05 + consolidation)
    # -------------------------------------------------------------------------
    ex_01 = {
        "lesson": "b1-22-01",
        "exercises": [
            {
                "id": "b1-22-01.ex01",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent a 'kockázat' kifejezés?",
                "options": [
                    "Egy esetleges veszély vagy veszteség bekövetkezésének a lehetősége.",
                    "Egy előre biztosan garantált siker és haszon.",
                    "Egy történelmi emlékmű építési költsége."
                ],
                "correct": 0
            },
            {
                "id": "b1-22-01.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Lehet, _____ holnap délutánra eláll az eső, és kisüt a nap. (that - hogy)",
                "answer": "hogy"
            },
            {
                "id": "b1-22-01.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Megtörténhet,", "hogy", "a", "vonat", "késve", "érkezik", "meg."],
                "solution": ["Megtörténhet,", "hogy", "a", "vonat", "késve", "érkezik", "meg."]
            },
            {
                "id": "b1-22-01.ex04",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Melyik mondat fejezi ki a legnagyobb valószínűséget?",
                "options": [
                    "Minden bizonnyal befejezzük a munkát péntekig.",
                    "Aligha fog sikerülni a vizsga felkészülés nélkül.",
                    "Talán majd egyszer elolvasom ezt a hosszú könyvet."
                ],
                "correct": 0
            },
            {
                "id": "b1-22-01.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "Jó _____ van arra, hogy a csapat megnyerje az idei bajnokságot. (chance/odds - esély)",
                "answer": "esély"
            },
            {
                "id": "b1-22-01.ex06",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Mikor használjuk a 'hátha' szócskát?",
                "options": [
                    "Amikor reménykedve bízunk egy kedvező lehetőség bekövetkeztében.",
                    "Amikor teljesen kizártnak tartunk egy eseményt.",
                    "Amikor múltbeli tényeket sorolunk fel kronológiai sorrendben."
                ],
                "correct": 0
            },
            {
                "id": "b1-22-01.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Induljunk most azonnal, _____ még nyitva találjuk a postahivatalt! (who knows, maybe - hátha)",
                "answer": "hátha"
            },
            {
                "id": "b1-22-01.ex08",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["Minden", "új", "vállalkozás", "bizonyos", "pénzügyi", "kockázattal", "jár."],
                "solution": ["Minden", "új", "vállalkozás", "bizonyos", "pénzügyi", "kockázattal", "jár."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-22-01-ex.json", ex_01)

    ex_02 = {
        "lesson": "b1-22-02",
        "exercises": [
            {
                "id": "b1-22-02.ex01",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent az 'előrejelzés' szó?",
                "options": [
                    "Tudományos vagy szakmai adatokon alapuló jövőbeli becslés.",
                    "Egy múltbeli történelmi esemény leírása.",
                    "Hivatalos bírósági határozat fellebbezése."
                ],
                "correct": 0
            },
            {
                "id": "b1-22-02.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A meteorológusok szerint holnap jelentősen csökkenni _____ a hőmérséklet. (will - fog)",
                "answer": "fog"
            },
            {
                "id": "b1-22-02.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Az", "új", "technológiák", "alapjaiban", "fogják", "megváltoztatni", "az", "életünket."],
                "solution": ["Az", "új", "technológiák", "alapjaiban", "fogják", "megváltoztatni", "az", "életünket."]
            },
            {
                "id": "b1-22-02.ex04",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit fejez ki az 'aligha' szó egy kijelentésben?",
                "options": [
                    "Azt, hogy valami nagyon valószínűtlen, szinte lehetetlen.",
                    "Azt, hogy valami azonnal és kétségtelenül bekövetkezik.",
                    "Azt, hogy a döntés kizárólag a miniszter kezében van."
                ],
                "correct": 0
            },
            {
                "id": "b1-22-02.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A fiatal mérnöknek világos és vonzó jövő_____ van a város fejlődéséről. (vision of future - képe)",
                "answer": "képe"
            },
            {
                "id": "b1-22-02.ex06",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik mondat helyes és természetes a jövő kifejezésére?",
                "options": [
                    "Minden bizonnyal meg fogjuk találni a megfelelő megoldást.",
                    "Minden bizonnyal meg fogjuk találunk a megfelelő megoldást.",
                    "Minden bizonnyal találtunk meg a megfelelő megoldásokat holnap."
                ],
                "correct": 0
            },
            {
                "id": "b1-22-02.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Ilyen zord téli időben _____ fogunk a hegyekbe kirándulni. (hardly / scarcely - aligha)",
                "answer": "aligha"
            },
            {
                "id": "b1-22-02.ex08",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "hosszú", "távú", "távlatok", "nagyon", "biztatóak", "a", "kutatásban."],
                "solution": ["A", "hosszú", "távú", "távlatok", "nagyon", "biztatóak", "a", "kutatásban."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-22-02-ex.json", ex_02)

    ex_03 = {
        "lesson": "b1-22-03",
        "exercises": [
            {
                "id": "b1-22-03.ex01",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit fejez ki a 'kétkedés' kifejezés?",
                "options": [
                    "A bizonytalanságot és a szkeptikus, óvatos hozzáállást.",
                    "A feltétel nélküli bizalmat és rajongást.",
                    "A törvényes határidők pontos betartását."
                ],
                "correct": 0
            },
            {
                "id": "b1-22-03.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Kétlem, _____ az elképzelés ilyen formában működőképes lenne. (that - hogy)",
                "answer": "hogy"
            },
            {
                "id": "b1-22-03.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Semmi", "kétség", "nem", "fér", "hozzá,", "hogy", "igazad", "van."],
                "solution": ["Semmi", "kétség", "nem", "fér", "hozzá,", "hogy", "igazad", "van."]
            },
            {
                "id": "b1-22-03.ex04",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent a 'bizakodás' szó?",
                "options": [
                    "Reményteli, optimista várakozást a jövővel kapcsolatban.",
                    "Mély kétségbeesést és a küzdelem feladását.",
                    "Számítógépes programozási hibát."
                ],
                "correct": 0
            },
            {
                "id": "b1-22-03.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A pénzügyi szakértők előzetes _____ szerint nyereséges lesz az év. (calculations - számításai)",
                "answer": "számításai"
            },
            {
                "id": "b1-22-03.ex06",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Hogyan mondjuk helyesen magyarul: 'I trust that everything will be fine'?",
                "options": [
                    "Bízom benne, hogy minden rendben lesz.",
                    "Bízom arról, hogy minden rendben fog.",
                    "Bízom bele, hogy minden rendeződik majd."
                ],
                "correct": 0
            },
            {
                "id": "b1-22-03.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Nem fér hozzá semmi _____, hogy a kísérlet meghozza a várva várt áttörést. (doubt - kétség)",
                "answer": "kétség"
            },
            {
                "id": "b1-22-03.ex08",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["Nagy", "bizakodással", "tekintünk", "a", "jövő", "kihívásai", "elé."],
                "solution": ["Nagy", "bizakodással", "tekintünk", "a", "jövő", "kihívásai", "elé."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-22-03-ex.json", ex_03)

    ex_04 = {
        "lesson": "b1-22-04",
        "exercises": [
            {
                "id": "b1-22-04.ex01",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent a 'kiszámíthatatlan' melléknév?",
                "options": [
                    "Olyan dolgot vagy személyt, amelynek viselkedése előre nem látható.",
                    "Olyan matematikai egyenletet, amelyet könnyű kiszámolni.",
                    "Egy előre megtervezett és pontos napirendet."
                ],
                "correct": 0
            },
            {
                "id": "b1-22-04.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Teljesen _____ dolog, hogy a határidőt meghosszabbítsák. (ruled out / out of the question - kizárt)",
                "answer": "kizárt"
            },
            {
                "id": "b1-22-04.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Könnyen", "megeshet,", "hogy", "váratlan", "akadályokba", "ütközünk", "az", "úton."],
                "solution": ["Könnyen", "megeshet,", "hogy", "váratlan", "akadályokba", "ütközünk", "az", "úton."]
            },
            {
                "id": "b1-22-04.ex04",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mi az a 'megérzés'?",
                "options": [
                    "Egy ösztönös, belső sejtelem, intuíció egy jövőbeli dologról.",
                    "Egy orvosi műszer által mért hőmérséklet.",
                    "Egy hivatalos bérleti szerződés felbontása."
                ],
                "correct": 0
            },
            {
                "id": "b1-22-04.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "Nem a _____ műve volt a siker, hanem az alapos és kitartó felkészülésé. (coincidence / accident - véletlen)",
                "answer": "véletlen"
            },
            {
                "id": "b1-22-04.ex06",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik kifejezés jelenti azt, hogy 'It is easily conceivable'?",
                "options": [
                    "Könnyen elképzelhető.",
                    "Nehezen hihető el.",
                    "Kizártnak tartom."
                ],
                "correct": 0
            },
            {
                "id": "b1-22-04.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Könnyen el_____, hogy a találmány forradalmasítja az egész iparágat. (imaginable / conceivable - képzelhető)",
                "answer": "képzelhető"
            },
            {
                "id": "b1-22-04.ex08",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "belső", "megérzésem", "azt", "súgta,", "hogy", "óvatosnak", "kell", "lennem."],
                "solution": ["A", "belső", "megérzésem", "azt", "súgta,", "hogy", "óvatosnak", "kell", "lennem."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-22-04-ex.json", ex_04)

    ex_05 = {
        "lesson": "b1-22-05",
        "exercises": [
            {
                "id": "b1-22-05.ex01",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent a 'forgatókönyv' a stratégiai tervezésben?",
                "options": [
                    "Egy előre kidolgozott cselekvési terv a lehetséges eseményekre.",
                    "Kizárólag egy színházi színdarab kézzel írt szövege.",
                    "A pénztárban vásárolt vonatjegy nyugtája."
                ],
                "correct": 0
            },
            {
                "id": "b1-22-05.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Arra az _____ készülünk fel, ha a tárgyalások elhúzódnának. (contingency / eventuality - eshetőségre)",
                "answer": "eshetőségre"
            },
            {
                "id": "b1-22-05.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Végül", "valóra", "vált", "a", "tudósok", "merész", "jóslata."],
                "solution": ["Végül", "valóra", "vált", "a", "tudósok", "merész", "jóslata."]
            },
            {
                "id": "b1-22-05.ex04",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit fejez ki a 'megvalósulás' fogalma?",
                "options": [
                    "Egy terv vagy álom gyakorlati formába öntését, valóra válását.",
                    "Egy megbeszélés váratlan lemondását vagy elhalasztását.",
                    "Az elméleti fizika matematikai bizonyítását."
                ],
                "correct": 0
            },
            {
                "id": "b1-22-05.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A kutatócsoport várakozásai a tesztelés alatt teljesen be_____. (verified / confirmed - igazolódtak)",
                "answer": "igazolódtak"
            },
            {
                "id": "b1-22-05.ex06",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Mit jelent az, hogy 'a legrosszabb forgatókönyv szerint'?",
                "options": [
                    "Ha a legkedvezőtlenebb körülmények valósulnak meg.",
                    "Ha egy filmrendező rossz forgatókönyvet olvas fel.",
                    "Ha azonnal megkezdődik a tavaszi napsütéses időszak."
                ],
                "correct": 0
            },
            {
                "id": "b1-22-05.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Minden _____ készen állunk, a legkedvezőbbtől a legváratlanabbig. (eventuality - eshetőségre)",
                "answer": "eshetőségre"
            },
            {
                "id": "b1-22-05.ex08",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "tervek", "gyors", "megvalósulása", "minden", "várakozást", "felülmúlt."],
                "solution": ["A", "tervek", "gyors", "megvalósulása", "minden", "várakozást", "felülmúlt."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-22-05-ex.json", ex_05)

    ex_consolidation = {
        "lesson": "b1-22-consolidation",
        "exercises": [
            {
                "id": "b1-22-consolidation.ex01",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik kötőszóval kapcsoljuk össze a 'Lehet' és a mellékmondatot?",
                "options": [
                    "hogy (Lehet, hogy holnap találkozunk.)",
                    "mert (Lehet, mert holnap találkozunk.)",
                    "holott (Lehet, holott holnap találkozunk.)"
                ],
                "correct": 0
            },
            {
                "id": "b1-22-consolidation.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A jövőbeli fejlesztések minden _____ át fogják formálni a közlekedést. (in all probability - bizonnyal)",
                "answer": "bizonnyal"
            },
            {
                "id": "b1-22-consolidation.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Kétlem,", "hogy", "bárki", "is", "megkérdőjelezné", "a", "felfedezés", "értékét."],
                "solution": ["Kétlem,", "hogy", "bárki", "is", "megkérdőjelezné", "a", "felfedezés", "értékét."]
            },
            {
                "id": "b1-22-consolidation.ex04",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "Tatrangi Dávid találmánya a regényben végül valóra _____. (came true - vált)",
                "answer": "vált"
            },
            {
                "id": "b1-22-consolidation.ex05",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "tudományos", "előrejelzések", "és", "jóslatok", "mindig", "kockázattal", "járnak."],
                "solution": ["A", "tudományos", "előrejelzések", "és", "jóslatok", "mindig", "kockázattal", "járnak."]
            },
            {
                "id": "b1-22-consolidation.ex06",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent az, ha valami 'kiszámíthatatlan'?",
                "options": [
                    "Nem lehet előre látni vagy megbízhatóan megbecsülni a lefolyását.",
                    "Könnyen beilleszthető a meglévő menetrendbe.",
                    "Mindenki által ismert és elfogadott matematikai szabály."
                ],
                "correct": 0
            },
            {
                "id": "b1-22-consolidation.ex07",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "Bizakodással tekintünk a jövő elé, bízva a merész tervek meg_____. (realization - valósulásában)",
                "answer": "valósulásában"
            },
            {
                "id": "b1-22-consolidation.ex08",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Mit jósolt meg Jókai Mór 'A jövő század regénye' című művében az 1870-es években?",
                "options": [
                    "A repülés elterjedését az 'Aerodrom' géppel és a modern technikai vívmányokat.",
                    "A gőzhajózás teljes megszűnését és a vitorlások visszatérését.",
                    "Azt, hogy a könyvnyomtatás örökre megszűnik a huszadik század elején."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-22-consolidation-ex.json", ex_consolidation)

    # -------------------------------------------------------------------------
    # 4. Classic Story Adaptation for Consolidation
    # -------------------------------------------------------------------------
    story_classic = {
        "id": "story.b1.22.classic",
        "title": "A jövő század regénye",
        "level": "B1",
        "order": 22,
        "type": "classics",
        "estimatedMinutes": 8,
        "summary": "An adaptation of Mór Jókai's visionary science-fiction work 'A jövő század regénye' (1872). The brilliant Hungarian inventor Dávid Tatrangi develops the 'Aerodrom'—an electrically-powered flying machine made of an indestructible lightweight alloy ('ichor'). Looking ahead into the future, the characters discuss the breathtaking possibilities, the technological risks, and whether visionary predictions can truly alter the fate of humanity.",
        "characters": [
            "Tatrangi Dávid, a zseniális magyar feltaláló",
            "Hermina, Dávid hitvese és segítőtársa",
            "Kins- gating és a nemzetközi tudósok"
        ],
        "location": "A Duna-parti kísérleti műhely és az égbolt",
        "author": "Jókai Mór",
        "work": "A jövő század regénye (1872)",
        "paragraphs": [
            {
                "type": "narration",
                "text": "A Duna csendes partján, a sűrű fűzfák takarásában állt a titokzatos műhely. Bent különös szerkezet pihent az állványon: szárnyai kecsesen íveltek, váza pedig egy addig soha nem látott, csillogó és törhetetlen anyagból, az úgynevezett ichorból készült. Ez volt az Aerodrom, a jövő század repülőgépe."
            },
            {
                "type": "dialogue",
                "speaker": "Hermina",
                "text": "Dávid, valóban lehetséges ez? Tényleg elérkezik a pillanat, amikor az ember madár módjára átszeli a felhőket, és a távolság megszűnik létezni?"
            },
            {
                "type": "dialogue",
                "speaker": "Tatrangi Dávid",
                "text": "Nemcsak lehetséges, kedvesem, hanem minden bizonnyal be is fog következni! A számításaim nem csalnak. Az elektromosság és a könnyű szárnyak erejével nemcsak az eget hódítjuk meg, hanem a népek közötti békét is megalapozzuk. A repülőgép előtt nincsenek országhatárok."
            },
            {
                "type": "narration",
                "text": "A feltaláló barátai és a tudósok sokáig kétkedéssel fogadták a merész jóslatokat. Sokan úgy vélték, a kockázat túlságosan hatalmas, s az emberi erő képtelen legyőzni a nehézkedést. Ám Dávid belső megérzése és a precíz fizikai törvények nem hagytak kétséget."
            },
            {
                "type": "dialogue",
                "speaker": "Kins-gating",
                "text": "Még ha a gép működik is, Dávid, gondoltál a legrosszabb forgatókönyvre? Mi történik, ha ezt a csodás hatalmat pusztításra használják a jövő háborúiban?"
            },
            {
                "type": "dialogue",
                "speaker": "Tatrangi Dávid",
                "text": "Minden eshetőségre fel kell készülnünk, barátom. De hiszem, hogy a tudomány felemeli az emberiséget. Az Aerodrom nem a pusztítás, hanem az egyetemes megértés eszköze lesz. Amikor a felhők felett repülünk, a földi viszályok törpévé és jelentéktelenné válnak."
            },
            {
                "type": "narration",
                "text": "Dávid meghúzta az indítókart. A szárnyak halkan felzúgtak, s az Aerodrom fenségesen emelkedett a levegőbe. Jókai Mór látnoki regénye nem puszta mese volt: a következő század valóban meghozta a repülés csodáját, beváltva a lánglelkű magyar író legszebb jóslatát."
            }
        ]
    }
    write_json("content/hu/stories/classics/b1/b1-22-jokai.json", story_classic)

    # -------------------------------------------------------------------------
    # 5. Lesson Files (01 to 05 + consolidation)
    # -------------------------------------------------------------------------
    for i in range(1, 6):
        padded = f"0{i}"
        titles = {
            "01": ("Possibility and Chance", "Lehetőség és esély: Lehet, hogy... és a kockázat"),
            "02": ("Forecasting the Future", "Előrejelzések és jóslatok: A jövő idő és távlatok"),
            "03": ("Doubt and Confidence", "Kétség és bizakodás: Kétlem, hogy... és a számítások"),
            "04": ("The Unpredictable", "A kiszámíthatatlan és a véletlen: Elképzelhető és kizárt"),
            "05": ("Scenarios and Reality", "Forgatókönyvek és megvalósulás: Felkészülés minden eshetőségre")
        }
        en_title, hu_title = titles[padded]
        lesson_data = {
            "id": f"lesson.b1.22-{padded}",
            "unit": 22,
            "title": en_title,
            "level": "B1",
            "grammar": "Epistemic Modality (lehet hogy, kétlem hogy, elképzelhető) and Future Forecasting",
            "goal": [
                f"I can understand and use vocabulary for {en_title.lower()}.",
                "I can express possibilities, predictions, doubts, and contingencies in Hungarian.",
                "I can discuss future outlooks and calculate risks with authentic modal constructions.",
                "I can master four new target vocabulary items in authentic context."
            ],
            "sections": [
                {
                    "type": "goal",
                    "title": "Lesson Goals",
                    "items": [
                        f"I can understand and use vocabulary for {en_title.lower()}.",
                        "I can express possibilities, predictions, doubts, and contingencies in Hungarian.",
                        "I can discuss future outlooks and calculate risks with authentic modal constructions.",
                        "I can master four new target vocabulary items in authentic context."
                    ]
                },
                {"type": "recycle", "title": "Quick Review"},
                {"type": "grammar", "ref": f"grammar/b1/b1-22-{padded}-a-gr.json"},
                {"type": "grammar", "ref": f"grammar/b1/b1-22-{padded}-b-gr.json"},
                {"type": "vocabulary", "title": "Lesson Vocabulary", "ref": f"vocabulary/b1/b1-22-{padded}-voc.json"},
                {
                    "type": "exercise-group",
                    "title": "Practice",
                    "ref": f"exercises/b1/b1-22-{padded}-ex.json",
                    "exerciseRefs": [f"b1-22-{padded}.ex0{k}" for k in range(1, 9)]
                }
            ]
        }
        write_json(f"content/hu/lessons/b1/b1-22-{padded}.json", lesson_data)

    consolidation_data = {
        "id": "lesson.b1.22-consolidation",
        "unit": 22,
        "title": "Unit 22 Consolidation",
        "level": "B1",
        "grammar": "Consolidation of Epistemic Modality, Forecasts & Scientific Predictions",
        "sections": [
            {
                "type": "story",
                "title": "A jövő század regénye (Jókai Mór)",
                "ref": "stories/classics/b1/b1-22-jokai.json"
            },
            {
                "type": "exercise-group",
                "title": "Consolidation Practice",
                "ref": "exercises/b1/b1-22-consolidation-ex.json",
                "exerciseRefs": [f"b1-22-consolidation.ex0{k}" for k in range(1, 9)]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-22-consolidation.json", consolidation_data)
    print("Successfully built Hungarian B1 Core Unit 22 (b1-22)!")

if __name__ == "__main__":
    build_unit_22_core()
