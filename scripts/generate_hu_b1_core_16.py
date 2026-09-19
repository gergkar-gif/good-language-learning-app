#!/usr/bin/env python3
"""Generate Hungarian B1 Core Unit 16: The Environment (b1-16)."""

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

def build_unit_16_core():
    # -------------------------------------------------------------------------
    # 1. Vocabulary Files (4 words each = 20 words total)
    # -------------------------------------------------------------------------
    voc_01 = {
        "id": "vocab.b1.16.01",
        "lesson": "b1-16-01",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "környezetvédelem", "translation": "environmental protection", "pos": "noun"},
            {"lemma": "szelektív hulladékgyűjtés", "translation": "selective waste collection, recycling", "pos": "noun"},
            {"lemma": "műanyaghulladék", "translation": "plastic waste", "pos": "noun"},
            {"lemma": "megújuló energia", "translation": "renewable energy", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-16-01-voc.json", voc_01)

    voc_02 = {
        "id": "vocab.b1.16.02",
        "lesson": "b1-16-02",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "klímaváltozás", "translation": "climate change", "pos": "noun"},
            {"lemma": "üvegházhatás", "translation": "greenhouse effect", "pos": "noun"},
            {"lemma": "szén-dioxid-kibocsátás", "translation": "carbon dioxide emissions", "pos": "noun"},
            {"lemma": "ökológiai lábnyom", "translation": "ecological footprint", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-16-02-voc.json", voc_02)

    voc_03 = {
        "id": "vocab.b1.16.03",
        "lesson": "b1-16-03",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "vízszennyezés", "translation": "water pollution", "pos": "noun"},
            {"lemma": "levegőszennyezettség", "translation": "air pollution level", "pos": "noun"},
            {"lemma": "erdőirtás", "translation": "deforestation", "pos": "noun"},
            {"lemma": "természetvédelmi terület", "translation": "nature reserve, protected area", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-16-03-voc.json", voc_03)

    voc_04 = {
        "id": "vocab.b1.16.04",
        "lesson": "b1-16-04",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "fenntarthatóság", "translation": "sustainability", "pos": "noun"},
            {"lemma": "újrahasznosítás", "translation": "recycling, reprocessing", "pos": "noun"},
            {"lemma": "energiatakarékosság", "translation": "energy saving, energy efficiency", "pos": "noun"},
            {"lemma": "zöld átállás", "translation": "green transition", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-16-04-voc.json", voc_04)

    voc_05 = {
        "id": "vocab.b1.16.05",
        "lesson": "b1-16-05",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "környezettudatosság", "translation": "environmental awareness", "pos": "noun"},
            {"lemma": "fogyasztói szokás", "translation": "consumer habit", "pos": "noun"},
            {"lemma": "helyi termelő", "translation": "local producer", "pos": "noun"},
            {"lemma": "hulladékcsökkentés", "translation": "waste reduction", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-16-05-voc.json", voc_05)

    # -------------------------------------------------------------------------
    # 2. Grammar Files
    # -------------------------------------------------------------------------
    gr_01_a = {
        "id": "grammar.b1.16.01.cause-result-ezert",
        "title": "Connectors of Result: ezért and így",
        "sections": [
            {
                "type": "text",
                "title": "Stating Results in Environmental Discourse",
                "content": "To express logical results and consequences, Hungarian uses *ezért* ('therefore / that is why') and *így* ('thus / in this way'). Notice that *ezért* connects an observed environmental fact with an action or outcome: *Sok műanyaghulladék keletkezik, ezért szelektíven gyűjtjük a szemetet.*"
            },
            {
                "type": "examples",
                "title": "Using ezért in sentences",
                "items": [
                    {
                        "spanish": "A városban magas a légszennyezés, ezért többen járnak kerékpárral.",
                        "english": "Air pollution is high in the city, therefore more people travel by bicycle."
                    },
                    {
                        "spanish": "Kevés az eső, ezért takarékoskodnunk kell az ivóvízzel.",
                        "english": "There is little rain, that is why we must conserve drinking water."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-16-01-a-gr.json", gr_01_a)

    gr_01_b = {
        "id": "grammar.b1.16.01.obligation-kell",
        "title": "Expressing Environmental Responsibility: meg kell tennünk",
        "sections": [
            {
                "type": "text",
                "title": "Impersonal and Personal Obligation with kell",
                "content": "When discussing ecological duties, *kell* combines with inflected infinitives (*meg kell tennünk* - 'we must do') or subjunctive clauses (*szükséges, hogy óvjuk* - 'it is necessary that we protect')."
            },
            {
                "type": "examples",
                "title": "Expressing ecological obligation",
                "items": [
                    {
                        "spanish": "Mindent meg kell tennünk a tiszta vizek megőrzéséért.",
                        "english": "We must do everything for the preservation of clean waters."
                    },
                    {
                        "spanish": "A gyáraknak csökkenteniük kell a károsanyag-kibocsátást.",
                        "english": "Factories must reduce their harmful emissions."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-16-01-b-gr.json", gr_01_b)

    gr_02_a = {
        "id": "grammar.b1.16.02.emiatt-kovetkezteben",
        "title": "Causal Connectors: emiatt and aminek következtében",
        "sections": [
            {
                "type": "text",
                "title": "Complex Cause-and-Effect Connectors",
                "content": "In formal and expository Hungarian, *emiatt* ('on account of this / due to this') and *aminek következtében* ('as a consequence of which') link broader climatic causes to specific ecological impacts."
            },
            {
                "type": "examples",
                "title": "Examples with emiatt and aminek következtében",
                "items": [
                    {
                        "spanish": "Nő az üvegházhatás, aminek következtében emelkedik az átlaghőmérséklet.",
                        "english": "The greenhouse effect increases, as a consequence of which average temperature rises."
                    },
                    {
                        "spanish": "A fosszilis tüzelőanyagok elégetése miatt nő a szén-dioxid szintje, és emiatt melegszik a Föld.",
                        "english": "Due to burning fossil fuels carbon dioxide levels rise, and on account of this the Earth warms."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-16-02-a-gr.json", gr_02_a)

    gr_02_b = {
        "id": "grammar.b1.16.02.noun-compounds",
        "title": "Environmental Compound Nouns in Hungarian",
        "sections": [
            {
                "type": "text",
                "title": "Forming Complex Environmental Terms",
                "content": "Hungarian forms precise scientific compound nouns: *szén-dioxid-kibocsátás* (written with hyphens due to length/rules), *ökológiai lábnyom*, *klímaváltozás*."
            },
            {
                "type": "examples",
                "title": "Compound nouns in context",
                "items": [
                    {
                        "spanish": "Minden repülőút jelentősen növeli az egyéni ökológiai lábnyomot.",
                        "english": "Every flight significantly increases one's individual ecological footprint."
                    },
                    {
                        "spanish": "A megújuló energiaforrások használata kulcsfontosságú a jövőnk szempontjából.",
                        "english": "The use of renewable energy sources is vital from the viewpoint of our future."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-16-02-b-gr.json", gr_02_b)

    gr_03_a = {
        "id": "grammar.b1.16.03.conditional-risks",
        "title": "Real and Unreal Conditions: Ha nem lépünk időben...",
        "sections": [
            {
                "type": "text",
                "title": "Hypothetical Scenarios and Environmental Warnings",
                "content": "Predicting consequences uses real conditions with present or future indicative: *Ha nem védjük az erdőket, a talaj erodálódni fog.* Past or unreal conditions use the conditional: *Ha korábban elkezdtük volna, most jobb helyzetben lennénk.*"
            },
            {
                "type": "examples",
                "title": "Conditionals in environmental warnings",
                "items": [
                    {
                        "spanish": "Ha megállítjuk az erdőirtást, megóvhatjuk a veszélyeztetett állatfajokat.",
                        "english": "If we halt deforestation, we can protect endangered animal species."
                    },
                    {
                        "spanish": "Ha nem vigyázunk a vizeinkre, a jövő generációi tiszta ivóvíz nélkül maradhatnak.",
                        "english": "If we do not take care of our waters, future generations may be left without clean drinking water."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-16-03-a-gr.json", gr_03_a)

    gr_03_b = {
        "id": "grammar.b1.16.03.passive-mediopassive",
        "title": "Mediopassive Verbs: szennyeződik, pusztul, megújul",
        "sections": [
            {
                "type": "text",
                "title": "Natural Processes with -ódik/-ődik and Intransitive Stems",
                "content": "Rather than passive voice, Hungarian uses reflexive/mediopassive verbs to describe spontaneous or environmental changes: *a folyó szennyeződik* ('the river becomes polluted'), *a természet megújul* ('nature renews itself')."
            },
            {
                "type": "examples",
                "title": "Describing environmental processes",
                "items": [
                    {
                        "spanish": "Tavasszal a természet csodálatos módon megújul.",
                        "english": "In spring nature renews itself in a wonderful way."
                    },
                    {
                        "spanish": "A nem kezelt szennyvíz miatt a természetes élőhely gyorsan pusztul.",
                        "english": "Due to untreated wastewater the natural habitat is rapidly degrading."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-16-03-b-gr.json", gr_03_b)

    gr_04_a = {
        "id": "grammar.b1.16.04.purpose-clauses",
        "title": "Purpose Clauses: azért, hogy fenntartható legyen",
        "sections": [
            {
                "type": "text",
                "title": "Expressing Environmental Goals with azért, hogy",
                "content": "To explain the purpose of ecological programs, use *azért... hogy + subjunctive (-jon/-jen)*: *Azért támogatják a zöld átállást, hogy tisztább legyen a levegő.*"
            },
            {
                "type": "examples",
                "title": "Purpose clauses for green initiatives",
                "items": [
                    {
                        "spanish": "Azért fejlesztik a tömegközlekedést, hogy csökkenjen az autók forgalma.",
                        "english": "They are developing public transport so that car traffic decreases."
                    },
                    {
                        "spanish": "Azért vezették be az újrahasznosítást, hogy kevesebb szemét kerüljön a lerakókba.",
                        "english": "They introduced recycling so that less garbage ends up in landfills."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-16-04-a-gr.json", gr_04_a)

    gr_04_b = {
        "id": "grammar.b1.16.04.nominalization",
        "title": "Nominalization with -ás/-és: újrahasznosítás, energiatakarékosság",
        "sections": [
            {
                "type": "text",
                "title": "Abstract Environmental Action Nouns",
                "content": "Verbal nouns ending in *-ás / -és* form the core vocabulary of sustainability: *újrahasznosít* -> *újrahasznosítás*, *takarékoskodik* -> *energiatakarékosság*."
            },
            {
                "type": "examples",
                "title": "Action nouns in practice",
                "items": [
                    {
                        "spanish": "Az energiatakarékosság nemcsak a környezetet védi, hanem pénzt is spórol.",
                        "english": "Energy efficiency not only protects the environment but also saves money."
                    },
                    {
                        "spanish": "A modern technológia megkönnyíti az ipari hulladék újrahasznosítását.",
                        "english": "Modern technology facilitates the recycling of industrial waste."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-16-04-b-gr.json", gr_04_b)

    gr_05_a = {
        "id": "grammar.b1.16.05.personal-habits",
        "title": "Habitual Aspects and Frequency: szokott, naponta, rendszeresen",
        "sections": [
            {
                "type": "text",
                "title": "Talking About Personal Green Habits",
                "content": "Discussing daily ecological habits uses *szokott + infinitive* ('tends to / usually does') alongside frequency adverbs: *mindennap*, *rendszeresen*, *tudatosan*."
            },
            {
                "type": "examples",
                "title": "Describing habits",
                "items": [
                    {
                        "spanish": "Mindig saját vászonszatyrot szoktam vinni a piacra, hogy ne használjak műanyagot.",
                        "english": "I usually bring my own canvas bag to the market so as not to use plastic."
                    },
                    {
                        "spanish": "Igyekszem helyi termelőktől vásárolni a szezonális zöldségeket.",
                        "english": "I endeavor to buy seasonal vegetables from local producers."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-16-05-a-gr.json", gr_05_a)

    gr_05_b = {
        "id": "grammar.b1.16.05.advocacy-stating-opinion",
        "title": "Stating Stances on Green Policies: Véleményem szerint, Meggyőződésem...",
        "sections": [
            {
                "type": "text",
                "title": "Structuring an Environmental Opinion",
                "content": "To formulate clear arguments at B1: *Meggyőződésem, hogy a környezettudatosság az iskolában kezdődik.* ('I am convinced that environmental awareness begins in school.')."
            },
            {
                "type": "examples",
                "title": "Formulating opinions",
                "items": [
                    {
                        "spanish": "Véleményem szerint a hulladékcsökkentés a legfontosabb lépés a tiszta jövő felé.",
                        "english": "In my opinion waste reduction is the most important step towards a clean future."
                    },
                    {
                        "spanish": "Úgy gondolom, hogy a fogyasztói szokások megváltoztatása mindannyiunk felelőssége.",
                        "english": "I think that changing consumer habits is a shared responsibility for all of us."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-16-05-b-gr.json", gr_05_b)

    # -------------------------------------------------------------------------
    # 3. Exercise Files
    # -------------------------------------------------------------------------
    for i in range(1, 6):
        padded = f"0{i}"
        ex_data = {
            "lesson": f"b1-16-{padded}",
            "exercises": [
                {
                    "id": f"b1-16-{padded}.ex01",
                    "type": "matching",
                    "category": "vocabulary",
                    "pairs": [
                        [voc_01["words"][0]["lemma"] if i == 1 else (voc_02["words"][0]["lemma"] if i == 2 else (voc_03["words"][0]["lemma"] if i == 3 else (voc_04["words"][0]["lemma"] if i == 4 else voc_05["words"][0]["lemma"]))), "concept 1"],
                        [voc_01["words"][1]["lemma"] if i == 1 else (voc_02["words"][1]["lemma"] if i == 2 else (voc_03["words"][1]["lemma"] if i == 3 else (voc_04["words"][1]["lemma"] if i == 4 else voc_05["words"][1]["lemma"]))), "concept 2"],
                        [voc_01["words"][2]["lemma"] if i == 1 else (voc_02["words"][2]["lemma"] if i == 2 else (voc_03["words"][2]["lemma"] if i == 3 else (voc_04["words"][2]["lemma"] if i == 4 else voc_05["words"][2]["lemma"]))), "concept 3"],
                        [voc_01["words"][3]["lemma"] if i == 1 else (voc_02["words"][3]["lemma"] if i == 2 else (voc_03["words"][3]["lemma"] if i == 3 else (voc_04["words"][3]["lemma"] if i == 4 else voc_05["words"][3]["lemma"]))), "concept 4"]
                    ]
                },
                {
                    "id": f"b1-16-{padded}.ex02",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "question": f"Melyik mondat fejezi ki helyesen az összefüggést? (Lesson {i})",
                    "options": [
                        "A környezet védelme közös érdek, ezért odafigyelünk a szelektív gyűjtésre.",
                        "A környezet védelme közös érdek, mert odafigyelünk gyűjteni.",
                        "A környezet védelme ezért közös, mert gyűjteni szemetet."
                    ],
                    "correct": 0
                },
                {
                    "id": f"b1-16-{padded}.ex03",
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "sentence": "A városban egyre fontosabb a tudatos hulladékkezelés és a zöld _____ védelme. (environment)",
                    "answer": "környezet"
                },
                {
                    "id": f"b1-16-{padded}.ex04",
                    "type": "fill-blank",
                    "category": "grammar",
                    "sentence": "Sok szemetet termelünk, ____ változtatnunk kell a szokásainkon. (therefore)",
                    "answer": "ezért"
                },
                {
                    "id": f"b1-16-{padded}.ex05",
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "question": "Mit jelent a megújuló energiaforrások használata?",
                    "options": [
                        "Olyan források használatát, mint a napenergia vagy a szélenergia.",
                        "Csak a szén és a kőolaj elégetését.",
                        "A műanyaghulladék folyóba dobását."
                    ],
                    "correct": 0
                },
                {
                    "id": f"b1-16-{padded}.ex06",
                    "type": "fill-blank",
                    "category": "grammar",
                    "sentence": "Az erdőirtás növeli a szén-dioxid szintjét, aminek ____ melegszik a légkör. (consequence)",
                    "answer": "következtében"
                },
                {
                    "id": f"b1-16-{padded}.ex07",
                    "type": "sentence-builder",
                    "category": "grammar",
                    "tiles": ["A", "megújuló", "energia", "használata", "kulcsfontosságú", "a", "tiszta", "jövő", "szempontjából."],
                    "solution": ["A", "megújuló", "energia", "használata", "kulcsfontosságú", "a", "tiszta", "jövő", "szempontjából."]
                },
                {
                    "id": f"b1-16-{padded}.ex08",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "Hogyan csökkentheti az egyén a saját ökológiai lábnyomát?",
                    "options": [
                        "Tudatos vásárlással, újrahasznosítással és energiatakarékossággal.",
                        "Több egyszer használatos műanyag vásárlásával.",
                        "Minden nap felesleges autóhasználattal."
                    ],
                    "correct": 0
                }
            ]
        }
        # Refine matching exercise translations with real values
        curr_voc = [voc_01, voc_02, voc_03, voc_04, voc_05][i-1]
        ex_data["exercises"][0]["pairs"] = [[w["lemma"], w["translation"]] for w in curr_voc["words"]]
        write_json(f"content/hu/exercises/b1/b1-16-{padded}-ex.json", ex_data)

    # Consolidation exercises
    ex_consolidation = {
        "lesson": "b1-16-consolidation",
        "exercises": [
            {
                "id": "b1-16-consolidation.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["környezetvédelem", "environmental protection"],
                    ["klímaváltozás", "climate change"],
                    ["fenntarthatóság", "sustainability"],
                    ["újrahasznosítás", "recycling"]
                ]
            },
            {
                "id": "b1-16-consolidation.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik mondat kapcsolja össze helyesen az okot és a következményt?",
                "options": [
                    "A globális felmelegedés miatt olvadnak a gleccserek, aminek következtében nő a tengerszint.",
                    "A globális felmelegedés ezért olvadnak gleccserek hogy növekedjen.",
                    "Mivel olvadnak gleccserek ezért melegszik globális felmelegedés."
                ],
                "correct": 0
            },
            {
                "id": "b1-16-consolidation.ex03",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A természeti értékek védelmére kijelölt terület neve ____ terület. (nature reserve)",
                "answer": "természetvédelmi"
            },
            {
                "id": "b1-16-consolidation.ex04",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Mindent meg kell tennünk, ____ megóvjuk a tiszta ivóvizet a jövő generációi számára. (in order that)",
                "answer": "hogy"
            },
            {
                "id": "b1-16-consolidation.ex05",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "tudatos", "hulladékcsökkentés", "és", "a", "szelektív", "gyűjtés", "védi", "a", "természeti", "környezetet."],
                "solution": ["A", "tudatos", "hulladékcsökkentés", "és", "a", "szelektív", "gyűjtés", "védi", "a", "természeti", "környezetet."]
            },
            {
                "id": "b1-16-consolidation.ex06",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent az energiatakarékosság a mindennapi életben?",
                "options": [
                    "A villany lekapcsolását, ha elhagyjuk a szobát, és korszerű gépek használatát.",
                    "Feleslegesen égve hagyott lámpákat a ház minden helyiségében.",
                    "A fűtés maximális fokozatra állítását nyitott ablak mellett."
                ],
                "correct": 0
            },
            {
                "id": "b1-16-consolidation.ex07",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A műanyaghulladék helyett használjunk tartós, természetes anyagból készült ____ szatyrot. (canvas)",
                "answer": "vászon"
            },
            {
                "id": "b1-16-consolidation.ex08",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Miről szól Gárdonyi Géza novellája az erdőről és a természet csendjéről?",
                "options": [
                    "A természet tiszteletéről, az erdő bölcs nyugalmáról és az ember felelősségéről.",
                    "Egy modern ipari gyár felépítéséről az erdő közepén.",
                    "Egy autós versenyről a hegyi szerpentineken."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-16-consolidation-ex.json", ex_consolidation)

    # -------------------------------------------------------------------------
    # 4. Classic Story Adaptation for Lesson 5 / Consolidation
    # -------------------------------------------------------------------------
    story_classic = {
        "id": "story.b1.16.classic",
        "title": "A lámpás és az erdő csendje",
        "level": "B1",
        "order": 16,
        "type": "classics",
        "estimatedMinutes": 7,
        "summary": "An adaptation from Géza Gárdonyi's celebrated writings on Hungarian village nature and forests. The village teacher walks through the ancient Bakony forest at twilight, reflecting on the beauty of nature, the harmony of living creatures, and mankind's sacred duty to protect the woods.",
        "characters": [
            "A tanító",
            "János bácsi, a vadőr"
        ],
        "location": "Bakonyi erdőség",
        "author": "Gárdonyi Géza",
        "work": "A lámpás",
        "paragraphs": [
            {
                "type": "narration",
                "text": "A falu felett emelkedő bakonyi hegyoldalon hűvös, tiszta őszi szél lengette a tölgyfák lombjait. A falu fiatal tanítója lassan sétált felfelé a szűk erdei ösvényen."
            },
            {
                "type": "dialogue",
                "speaker": "János bácsi",
                "text": "Jó estét, tanító úr! Nem fél egyedül az erdőben ilyen késői órán, mikor már száll le az alkonyat?"
            },
            {
                "type": "dialogue",
                "speaker": "A tanító",
                "text": "Jó estét, János bácsi! Miért félnék a fáktól? Az erdő nem ellenségünk, hanem a leghűségesebb barátunk. Itt minden levél a békességről beszél."
            },
            {
                "type": "narration",
                "text": "Az öreg erdész megállt, pipáját zsebébe süllyesztette, és elismerően bólintott. Évtizedek óta járta ezeket a hegyeket, és ismerte a vadon minden titkos rezdülését."
            },
            {
                "type": "dialogue",
                "speaker": "János bácsi",
                "text": "Igaza van, fiam. De kevesen látják ezt így. Sokan csak fát és hasznot látnak a rengetegben, s elfelejtik, hogy a tiszta forrás és a jó levegő a legnagyobb kincsünk."
            },
            {
                "type": "narration",
                "text": "A tanító felnézett a csillagosodó égre. Kezében csendesen világított a kis viharlámpás, amely meleg sárga fényt vetett a mohos fatörzsekre és a párás avarra."
            },
            {
                "type": "dialogue",
                "speaker": "A tanító",
                "text": "Az iskolában tanítom a gyermekeknek: a természetet védeni kell, nem elpusztítani. Mert aki egy fát ültet, az a jövő nemzedékeknek ad árnyékot és életet."
            },
            {
                "type": "narration",
                "text": "Az erdő mélyéről egy bagoly hívása hallatszott. A két ember békességben állt a fák között; tudták, hogy amíg tisztelettel lépnek a rengetegbe, az erdő mindig otthont ad nekik."
            }
        ]
    }
    write_json("content/hu/stories/classics/b1/b1-16-gardonyi.json", story_classic)

    # -------------------------------------------------------------------------
    # 5. Lesson Files (01 to 05 + consolidation)
    # -------------------------------------------------------------------------
    for i in range(1, 6):
        padded = f"0{i}"
        titles = {
            "01": ("One Has To...", "Meg kell tennünk: Környezetünk védelme"),
            "02": ("Cause & Effect", "Ok és okozat: A klímaváltozás hatásai"),
            "03": ("A Problem, Explained", "Egy környezeti probléma: Vizeink és erdőink"),
            "04": ("What's Being Done", "Mit teszünk ellene? A fenntartható jövő"),
            "05": ("My Own Habits", "Saját szokásaim: Zöld gondolkodás a mindennapokban")
        }
        en_title, hu_title = titles[padded]
        lesson_data = {
            "id": f"lesson.b1.16-{padded}",
            "unit": 16,
            "title": en_title,
            "level": "B1",
            "grammar": "Causal and Consequence Connectors (ezért, emiatt, aminek következtében)",
            "goal": [
                f"I can understand and use vocabulary for {en_title.lower()}.",
                "I can form causal and result clauses using ezért and emiatt in Hungarian.",
                "I can discuss environmental issues, conservation, and sustainable habits.",
                "I can master four new target vocabulary items in authentic context."
            ],
            "sections": [
                {
                    "type": "goal",
                    "title": "Lesson Goals",
                    "items": [
                        f"I can understand and use vocabulary for {en_title.lower()}.",
                        "I can form causal and result clauses using ezért and emiatt in Hungarian.",
                        "I can discuss environmental issues, conservation, and sustainable habits.",
                        "I can master four new target vocabulary items in authentic context."
                    ]
                },
                {"type": "recycle", "title": "Quick Review"},
                {"type": "grammar", "ref": f"grammar/b1/b1-16-{padded}-a-gr.json"},
                {"type": "grammar", "ref": f"grammar/b1/b1-16-{padded}-b-gr.json"},
                {"type": "vocabulary", "title": "Lesson Vocabulary", "ref": f"vocabulary/b1/b1-16-{padded}-voc.json"},
                {
                    "type": "exercise-group",
                    "title": "Practice",
                    "ref": f"exercises/b1/b1-16-{padded}-ex.json",
                    "exerciseRefs": [f"b1-16-{padded}.ex0{k}" for k in range(1, 9)]
                }
            ]
        }
        write_json(f"content/hu/lessons/b1/b1-16-{padded}.json", lesson_data)

    consolidation_data = {
        "id": "lesson.b1.16-consolidation",
        "unit": 16,
        "title": "Unit 16 Consolidation",
        "level": "B1",
        "grammar": "Consolidation of Environmental Discourse & Cause-Result Structures",
        "sections": [
            {
                "type": "story",
                "title": "A lámpás és az erdő csendje (Gárdonyi Géza)",
                "ref": "stories/classics/b1/b1-16-gardonyi.json"
            },
            {
                "type": "exercise-group",
                "title": "Consolidation Practice",
                "ref": "exercises/b1/b1-16-consolidation-ex.json",
                "exerciseRefs": [f"b1-16-consolidation.ex0{k}" for k in range(1, 9)]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-16-consolidation.json", consolidation_data)
    print("Successfully built Hungarian B1 Core Unit 16 (b1-16)!")

if __name__ == "__main__":
    build_unit_16_core()
