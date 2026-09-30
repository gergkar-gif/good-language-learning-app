#!/usr/bin/env python3
"""Generate Hungarian B1 Core Unit 11: Cities & Communities (b1-11)."""

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

def build_unit_11_core():
    # -------------------------------------------------------------------------
    # 1. Vocabulary Files (4 words each = 20 words total)
    # -------------------------------------------------------------------------
    voc_01 = {
        "id": "vocab.b1.11.01",
        "lesson": "b1-11-01",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "település", "translation": "settlement, municipality", "pos": "noun"},
            {"lemma": "infrastruktúra", "translation": "infrastructure", "pos": "noun"},
            {"lemma": "szolgáltatás", "translation": "service, public service", "pos": "noun"},
            {"lemma": "lakosság", "translation": "population, local residents", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-11-01-voc.json", voc_01)

    voc_02 = {
        "id": "vocab.b1.11.02",
        "lesson": "b1-11-02",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "lakótelep", "translation": "housing estate, residential complex", "pos": "noun"},
            {"lemma": "zöldövezet", "translation": "green belt, parkland area", "pos": "noun"},
            {"lemma": "közbiztonság", "translation": "public safety, security", "pos": "noun"},
            {"lemma": "összetartás", "translation": "cohesion, community solidarity", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-11-02-voc.json", voc_02)

    voc_03 = {
        "id": "vocab.b1.11.03",
        "lesson": "b1-11-03",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "vidék", "translation": "countryside, rural region", "pos": "noun"},
            {"lemma": "városiasodás", "translation": "urbanization", "pos": "noun"},
            {"lemma": "ingázás", "translation": "commuting", "pos": "noun"},
            {"lemma": "életminőség", "translation": "quality of life", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-11-03-voc.json", voc_03)

    voc_04 = {
        "id": "vocab.b1.11.04",
        "lesson": "b1-11-04",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "látványosság", "translation": "sight, tourist attraction", "pos": "noun"},
            {"lemma": "idegenvezető", "translation": "tour guide", "pos": "noun"},
            {"lemma": "vendéglátás", "translation": "hospitality, catering industry", "pos": "noun"},
            {"lemma": "úticél", "translation": "travel destination", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-11-04-voc.json", voc_04)

    voc_05 = {
        "id": "vocab.b1.11.05",
        "lesson": "b1-11-05",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "önkormányzat", "translation": "local government, municipality", "pos": "noun"},
            {"lemma": "közösségi tér", "translation": "community space, public hub", "pos": "noun"},
            {"lemma": "egyesület", "translation": "association, civic club", "pos": "noun"},
            {"lemma": "rendezvény", "translation": "public event, function", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-11-05-voc.json", voc_05)

    # -------------------------------------------------------------------------
    # 2. Grammar Files
    # -------------------------------------------------------------------------
    gr_01_a = {
        "id": "grammar.b1.11.01.relative-pronouns-advanced",
        "title": "Advanced Relative Pronouns: aki, ami, amely, amelyik",
        "sections": [
            {
                "type": "text",
                "title": "Differentiating Relative Pronouns in Descriptions",
                "content": "When characterizing towns and people, choose the appropriate relative pronoun: *aki* (referring to people), *ami* (referring to whole clauses or indefinite concepts), *amely* (formal relative pronoun referring to specific things/places), and *amelyik* (selecting one specific item from a set)."
            },
            {
                "type": "examples",
                "title": "Relative pronoun examples",
                "items": [
                    {
                        "spanish": "Ez az a csendes kisváros, amely kiváló infrastruktúrával rendelkezik.",
                        "english": "This is the quiet small town that has excellent infrastructure."
                    },
                    {
                        "spanish": "Azok a helyi lakosok, akik itt élnek, nagyra becsülik a tiszta levegőt.",
                        "english": "Those local residents who live here greatly value the clean air."
                    },
                    {
                        "spanish": "Minden alapvető szolgáltatás elérhető, ami nagyon kényelmessé teszi a mindennapokat.",
                        "english": "All basic services are available, which makes daily life very convenient."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-11-01-a-gr.json", gr_01_a)

    gr_01_b = {
        "id": "grammar.b1.11.01.inflected-relatives",
        "title": "Case-Inflected Relative Pronouns: akinek, amiről, amelyben",
        "sections": [
            {
                "type": "text",
                "title": "Inflecting Relative Pronouns with Suffixes and Postpositions",
                "content": "Relative pronouns take case endings depending on their grammatical function in the subordinate clause: *akinek* (dative: to whom / whose), *amelyben* (inessive: in which), *amiről* (delative: about which), *ahová* (lative: whereto)."
            },
            {
                "type": "examples",
                "title": "Inflected relative examples",
                "items": [
                    {
                        "spanish": "A városrész, amelyben lakunk, az utóbbi években sokat fejlődött.",
                        "english": "The district in which we live has developed a lot in recent years."
                    },
                    {
                        "spanish": "Találkoztunk egy idős lakossal, akinek a családja évszázadok óta itt él.",
                        "english": "We met an elderly resident whose family has lived here for centuries."
                    },
                    {
                        "spanish": "A polgármester arról a tervről beszélt, amiről tegnap az újságok is írtak.",
                        "english": "The mayor spoke about the plan about which the newspapers also wrote yesterday."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-11-01-b-gr.json", gr_01_b)

    gr_02 = {
        "id": "grammar.b1.11.02.spatial-belonging-beli",
        "title": "Expressing Origin & Spatial Belonging: The -beli Suffix",
        "sections": [
            {
                "type": "text",
                "title": "Forming Adjectives of Neighborhood and Community Affiliation",
                "content": "The derivational suffix *-beli* forms adjectives denoting location or belonging: *környékbeli* (local, from the surrounding area), *városbeli* (townsperson / urban), *falubeli* (fellow villager), *helybeli* (local resident)."
            },
            {
                "type": "examples",
                "title": "The -beli suffix examples",
                "items": [
                    {
                        "spanish": "A környékbeli lakók szoros baráti közösséget alkotnak.",
                        "english": "The local residents from the neighborhood form a tight-knit friendly community."
                    },
                    {
                        "spanish": "A helybeli termelők minden szombaton friss zöldséget hoznak a piacra.",
                        "english": "Local producers bring fresh vegetables to the market every Saturday."
                    },
                    {
                        "spanish": "A lakótelepi környezetben a zöldövezetek javítják az emberek közérzetét.",
                        "english": "In housing estate environments, green areas improve people's wellbeing."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-11-02-gr.json", gr_02)

    gr_03 = {
        "id": "grammar.b1.11.03.contrast-connectors",
        "title": "Contrasting City & Rural Lifestyles: míg, ellenben, ezzel szemben",
        "sections": [
            {
                "type": "text",
                "title": "Forming Nuanced Contrasts Between Urban and Rural Realities",
                "content": "To balance differing lifestyles, use contrastive conjunctions and transitional adverbs: *míg* (while / whereas), *ellenben* (on the other hand), *ezzel szemben* (in contrast to this), and *ugyanakkor* (at the same time)."
            },
            {
                "type": "examples",
                "title": "Contrastive lifestyle examples",
                "items": [
                    {
                        "spanish": "A nagyvárosban pezseg a kulturális élet, míg vidéken a csend és a természet dominál.",
                        "english": "In the big city cultural life is bustling, whereas in the countryside peace and nature dominate."
                    },
                    {
                        "spanish": "A fővárosban sok a munkalehetőség, ezzel szemben a vidéki életminőség jóval nyugodtabb.",
                        "english": "In the capital there are many job opportunities; in contrast, rural quality of life is much calmer."
                    },
                    {
                        "spanish": "A napi ingázás fárasztó lehet, ellenben a saját kertes ház kárpótolja a családot.",
                        "english": "Daily commuting can be exhausting; on the other hand, a detached garden house makes up for it."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-11-03-gr.json", gr_03)

    gr_04 = {
        "id": "grammar.b1.11.04.recommending-places",
        "title": "Recommending Destinations & Local Gems: érdemes megnézni, ha teheted",
        "sections": [
            {
                "type": "text",
                "title": "Recommending sights and cultural visits",
                "content": "When playing host or advising travelers, use standard recommendation structures: *érdemes* (+ infinitive: 'it is worth...'), *mindenképpen ajánlom* ('I definitely recommend...'), and polite conditional invitations (*ha teheted, látogass el...* = 'if you can, pay a visit to...')."
            },
            {
                "type": "examples",
                "title": "Recommendation examples",
                "items": [
                    {
                        "spanish": "Ha Egerben jársz, mindenképpen érdemes meglátogatni a várat és a minaretet.",
                        "english": "If you are in Eger, it is definitely worth visiting the fortress and the minaret."
                    },
                    {
                        "spanish": "Egy tapasztalt idegenvezető segítségével sok rejtett történelmi látványosságot fedezhetünk fel.",
                        "english": "With the help of an experienced tour guide, we can discover many hidden historical sights."
                    },
                    {
                        "spanish": "A helyi vendéglátás barátságos, és a hagyományos ételek kiválóak.",
                        "english": "The local hospitality is friendly, and the traditional dishes are excellent."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-11-04-gr.json", gr_04)

    gr_05 = {
        "id": "grammar.b1.11.05.civic-participation",
        "title": "Civic Participation & Verb Governments: részt vesz vmiben, hozzájárul vmihez",
        "sections": [
            {
                "type": "text",
                "title": "Verbs of Community Engagement and Their Cases",
                "content": "Discussing community involvement requires key verb governments: *részt vesz valamiben* (inessive *-ban/-ben*: to participate in something), *hozzájárul valamihez* (allative *-hoz/-hez/-höz*: to contribute to something), and *együttműködik valakivel* (instrumental *-val/-vel*: to cooperate with someone)."
            },
            {
                "type": "examples",
                "title": "Civic engagement examples",
                "items": [
                    {
                        "spanish": "A lakosok aktívan részt vesznek a közösségi rendezvényeken és a fásítási akciókban.",
                        "english": "Residents actively participate in community events and tree-planting campaigns."
                    },
                    {
                        "spanish": "Minden egyesület hozzájárul a város kulturális életének gazdagításához.",
                        "english": "Every association contributes to enriching the town's cultural life."
                    },
                    {
                        "spanish": "Az önkormányzat új közösségi teret nyitott a fiatalok és a nyugdíjasok számára.",
                        "english": "The local municipality opened a new community space for young people and pensioners."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-11-05-gr.json", gr_05)

    # -------------------------------------------------------------------------
    # 3. Classic Literature Story
    # -------------------------------------------------------------------------
    classic_story = {
        "id": "story.b1.11.classic",
        "title": "Nyilas Misi Debrecen városában",
        "level": "B1",
        "lesson": 5,
        "order": 5,
        "type": "classics",
        "estimatedMinutes": 7,
        "characters": [
            "Nyilas Misi",
            "Pósalaky úr"
        ],
        "grammar": [
            "relative-pronouns-advanced",
            "spatial-belonging-beli",
            "civic-participation"
        ],
        "vocabularyTopics": [
            "city",
            "community",
            "school",
            "debrecen"
        ],
        "summary": "In this adapted literary excerpt from Zsigmond Móricz's beloved classic Légy jó mindhalálig, young student Misi navigates the historic streets and proud civic community of Debrecen, learning responsibility as he visits the blind old gentleman Mr. Pósalaky.",
        "source": "Adaptation inspired by the public-domain work Légy jó mindhalálig by Zsigmond Móricz",
        "paragraphs": [
            {"type": "narration", "text": "Debrecen nemcsak egy nagy alföldi település volt, hanem a magyar református műveltség és összetartás évszázados központja."},
            {"type": "narration", "text": "A Kollégium ódon falai közül kilépve Nyilas Misi büszkén sétált a Nagytemplom felé a macskaköves utcákon."},
            {"type": "narration", "text": "Délutánonként a vak Pósalaky úrhoz sietett, hogy felolvassa neki a helyi újságot és a lutri számait."},
            {"type": "dialogue", "speaker": "Pósalaky úr", "text": "Gyere csak, Misikém! Mesélj, mi újság van a városban? Milyen híreket írnak az önkormányzatról és az új építkezésekről?"},
            {"type": "dialogue", "speaker": "Nyilas Misi", "text": "Mindenki az új vasútvonalról beszél, nagytiszteletű uram, és a polgárok nagyon büszkék a virágzó városukra."},
            {"type": "narration", "text": "Az öregúr elégedetten bólintott, miközben Misi átérezte, hogy milyen felelősségteljes dolog egy igazi közösség hasznos tagjává válni."}
        ]
    }
    write_json("content/hu/stories/classics/b1/b1-11-legyjomindhalalig.json", classic_story)

    # -------------------------------------------------------------------------
    # 4. Exercise Files
    # -------------------------------------------------------------------------
    ex_01 = {
        "lesson": "b1-11-01",
        "exercises": [
            {
                "id": "b1-11-01-intro-1",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["település", "settlement / municipality"],
                    ["infrastruktúra", "infrastructure"],
                    ["szolgáltatás", "service"],
                    ["lakosság", "population / residents"]
                ]
            },
            {
                "id": "b1-11-01-intro-2",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["amely", "which / that (formal)"],
                    ["amelyben", "in which"],
                    ["akinek", "whose / to whom"],
                    ["amiről", "about which"]
                ]
            },
            {
                "id": "b1-11-01-controlled-1",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik vonatkozó névmás utal személyekre?",
                "options": ["aki", "amely", "ami"],
                "correct": 0
            },
            {
                "id": "b1-11-01-controlled-2",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik alak helyes a mondatban: „A település, ______ élünk, rendezett és tiszta.”?",
                "options": ["amelyben", "amelyről", "amelyhez"],
                "correct": 0
            },
            {
                "id": "b1-11-01-controlled-3",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik mondat köti össze szabályosan az egész tagmondatra vonatkozó gondolatot?",
                "options": [
                    "Minden bolt közel van, ami nagyon megkönnyíti a bevásárlást.",
                    "Minden bolt közel van, aki nagyon megkönnyíti a bevásárlást.",
                    "Minden bolt közel van, akitől nagyon megkönnyíti a bevásárlást."
                ],
                "correct": 0
            },
            {
                "id": "b1-11-01-controlled-4",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Mit jelent a mondatban: 'a város lakossága'?",
                "options": ["The population / inhabitants of the town", "The buildings of the town", "The shops in the street"],
                "correct": 0
            },
            {
                "id": "b1-11-01-practice-1",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Ez az a csendes kisváros, ____ kiváló iskolákkal és parkokkal rendelkezik. (which / formal)",
                "answer": "amely"
            },
            {
                "id": "b1-11-01-practice-2",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A modern közlekedési ____ révén a főváros fél óra alatt elérhető. (infrastructure)",
                "answer": "infrastruktúra"
            },
            {
                "id": "b1-11-01-practice-3",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Milyen szolgáltatásokat igényel egy modern település lakossága?",
                "options": [
                    "Egészségügyi ellátást, jó tömegközlekedést, iskolákat, üzleteket és banki szolgáltatásokat.",
                    "Kizárólag lovas hintókat.",
                    "Csak külföldi televíziós csatornákat."
                ],
                "correct": 0
            },
            {
                "id": "b1-11-01-practice-4",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Mit jelent a 'fejlett infrastruktúra' kifejezés?",
                "options": [
                    "Korszerű utakat, csatornázást, gyors internetet és megbízható villamoshálózatot.",
                    "Csak a régi városháza épületét.",
                    "A sűrű erdőket utak nélkül."
                ],
                "correct": 0
            },
            {
                "id": "b1-11-01-dialogue-1",
                "type": "multiple-choice",
                "category": "reading",
                "question": "— Miért költöztetek ebbe a külvárosi településre?\n— Mert kiváló a közlekedési ______ és gyönyörű a környezet.",
                "options": ["infrastruktúra", "kancellária", "kaució"],
                "correct": 0
            },
            {
                "id": "b1-11-01-dialogue-2",
                "type": "multiple-choice",
                "category": "reading",
                "question": "— Ismered a szomszédot?\n— Igen, ő az az orvos, ______ a rendelője a sarok túloldalán van.",
                "options": ["akinek", "amelyik", "amire"],
                "correct": 0
            },
            {
                "id": "b1-11-01-writing-1",
                "type": "fill-blank",
                "category": "production",
                "sentence": "A helyi ____ száma az utóbbi tíz évben jelentősen megemelkedett. (population / residents)",
                "answer": "lakosság"
            },
            {
                "id": "b1-11-01-writing-2",
                "type": "fill-blank",
                "category": "production",
                "sentence": "Meglátogattunk egy hangulatos falut, ____ sok hagyományos ház maradt fenn. (in which)",
                "answer": "amelyben"
            },
            {
                "id": "b1-11-01-check-1",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik szó jelenti az emberi lakóhelyet, falut vagy várost?",
                "options": ["település", "tanácsadás", "táplálkozás"],
                "correct": 0
            },
            {
                "id": "b1-11-01-check-2",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik vonatkozó névmás a legpontosabb választékos stílusban konkrét dologra?",
                "options": ["amely", "akik", "ahogy"],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-11-01-ex.json", ex_01)

    ex_02 = {
        "lesson": "b1-11-02",
        "exercises": [
            {
                "id": "b1-11-02-intro-1",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["lakótelep", "housing estate"],
                    ["zöldövezet", "green belt / parkland"],
                    ["közbiztonság", "public safety"],
                    ["összetartás", "solidarity / cohesion"]
                ]
            },
            {
                "id": "b1-11-02-intro-2",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["környékbeli", "local / from neighborhood"],
                    ["helybeli", "local resident"],
                    ["városbeli", "townsperson"],
                    ["falubeli", "fellow villager"]
                ]
            },
            {
                "id": "b1-11-02-controlled-1",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Hogyan képezzük a 'környék' szóból az ottani lakókra utaló melléknevet?",
                "options": ["környékbeli", "környéki", "környékből"],
                "correct": 0
            },
            {
                "id": "b1-11-02-controlled-2",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Mit fejez ki a '-beli' képző?",
                "options": [
                    "Térbeli vagy közösségi hovatartozást (pl. falubeli, helybeli).",
                    "Időbeli jövőt.",
                    "Tagadást."
                ],
                "correct": 0
            },
            {
                "id": "b1-11-02-controlled-3",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik kifejezés jelenti a környék biztonsági állapotát?",
                "options": ["közbiztonság", "lakótelep", "infrastruktúra"],
                "correct": 0
            },
            {
                "id": "b1-11-02-controlled-4",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik állítás igaz a magyarországi lakótelepekre?",
                "options": [
                    "Sok lakótelepen az utóbbi években szigetelték a panelházakat és zöld parkokat alakítottak ki.",
                    "Egy lakótelepen sincs villany vagy víz.",
                    "A lakótelepek kizárólag földszintes családi házakból állnak."
                ],
                "correct": 0
            },
            {
                "id": "b1-11-02-practice-1",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A házak között egy árnyas fás ____ húzódik játszótérrel és sétánnyal. (green belt)",
                "answer": "zöldövezet"
            },
            {
                "id": "b1-11-02-practice-2",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A környék____ lakosok minden évben közös utcabált szerveznek. (local / neighborhood)",
                "answer": "beli"
            },
            {
                "id": "b1-11-02-practice-3",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Mitől válik egy lakóközösség igazán összetartóvá?",
                "options": [
                    "A kölcsönös odafigyeléstől, a közös programoktól és a szomszédok közötti segítőkészségtől.",
                    "Attól, ha senki sem beszél egymással a házban.",
                    "A magas kerítésektől és a hangos vitáktól."
                ],
                "correct": 0
            },
            {
                "id": "b1-11-02-practice-4",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Milyen tényezők növelik egy környék közbiztonságát?",
                "options": [
                    "A jó közvilágítás, a rendszeres rendőri jelenlét és a figyelmes szomszédok.",
                    "A sötét, elhagyatott utcák.",
                    "Az utcai kamerák kikapcsolása."
                ],
                "correct": 0
            },
            {
                "id": "b1-11-02-dialogue-1",
                "type": "multiple-choice",
                "category": "reading",
                "question": "— Nem félsz este egyedül hazasétálni?\n— Nem, nálunk nagyon jó a ______, a rendőrség gyakran járőrözik.",
                "options": ["közbiztonság", "megtorlás", "vilajet"],
                "correct": 0
            },
            {
                "id": "b1-11-02-dialogue-2",
                "type": "multiple-choice",
                "category": "reading",
                "question": "— Milyen a hangulat a házatokban?\n— Kiváló, igazi szomszédi ______ van, mindig számíthatunk egymásra.",
                "options": ["összetartás", "széthúzás", "zsoldoshiány"],
                "correct": 0
            },
            {
                "id": "b1-11-02-writing-1",
                "type": "fill-blank",
                "category": "production",
                "sentence": "A barátunk egy felújított óbudai ____ lakik a Duna közelében. (housing estate / complex)",
                "answer": "lakótelepen"
            },
            {
                "id": "b1-11-02-writing-2",
                "type": "fill-blank",
                "category": "production",
                "sentence": "A hely____ lakosság büszke a város gazdag történelmi emlékeire. (local)",
                "answer": "beli"
            },
            {
                "id": "b1-11-02-check-1",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Mit jelent az 'összetartás' szó?",
                "options": ["Community solidarity / cohesion", "Isolation", "Moving out"],
                "correct": 0
            },
            {
                "id": "b1-11-02-check-2",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik szó jelöli a sok lakásból álló paneltömböket?",
                "options": ["lakótelep", "szigetelés", "kincstár"],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-11-02-ex.json", ex_02)

    ex_03 = {
        "lesson": "b1-11-03",
        "exercises": [
            {
                "id": "b1-11-03-intro-1",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["vidék", "countryside / rural region"],
                    ["városiasodás", "urbanization"],
                    ["ingázás", "commuting"],
                    ["életminőség", "quality of life"]
                ]
            },
            {
                "id": "b1-11-03-intro-2",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["míg", "while / whereas"],
                    ["ezzel szemben", "in contrast"],
                    ["ellenben", "on the other hand"],
                    ["ugyanakkor", "at the same time"]
                ]
            },
            {
                "id": "b1-11-03-controlled-1",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik kötőszó fejez ki párhuzamos ellentétet: „Budapesten sok a munkahely, ______ vidéken tisztább a levegő.”?",
                "options": ["míg", "mivel", "mintha"],
                "correct": 0
            },
            {
                "id": "b1-11-03-controlled-2",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Hogyan mondjuk magyarul: 'in contrast to this'?",
                "options": ["ezzel szemben", "ezért", "ennek révén"],
                "correct": 0
            },
            {
                "id": "b1-11-03-controlled-3",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Mit jelent az 'ingázás' fogalma?",
                "options": [
                    "Rendszeres napi vagy heti utazást a lakóhely és a munkahely vagy iskola között.",
                    "Egyszeri nyaralást a tengerpartra.",
                    "Költözést külföldre."
                ],
                "correct": 0
            },
            {
                "id": "b1-11-03-controlled-4",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik mondat fejezi ki helyesen az életminőség összehasonlítását?",
                "options": [
                    "A nagyvárosi élet sok lehetőséget kínál, ellenben jóval zajosabb és drágább.",
                    "A nagyvárosi élet sok lehetőséget kínál, mert nincs zaj.",
                    "A nagyvárosi élet sok lehetőséget kínál és senki nem lakik ott."
                ],
                "correct": 0
            },
            {
                "id": "b1-11-03-practice-1",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Sokan vállalják a napi ____ a békés, csendes kertes házért cserébe. (commuting)",
                "answer": "ingázást"
            },
            {
                "id": "b1-11-03-practice-2",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A fővárosban élénk a forgalom, ____ a kis falvakban alig látni autókat. (whereas / while)",
                "answer": "míg"
            },
            {
                "id": "b1-11-03-practice-3",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Milyen előnyei vannak a vidéki életnek a városival szemben?",
                "options": [
                    "Kisebb a zaj, közelebb van a természet, nagyobb a privát tér és gyakran alacsonyabbak a lakásárak.",
                    "Minden sarkon metróállomás található.",
                    "Soha nem kell semmilyen fűtést fizetni."
                ],
                "correct": 0
            },
            {
                "id": "b1-11-03-practice-4",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Mit értünk az 'életminőség' mutatói alatt?",
                "options": [
                    "Az egészségi állapotot, az anyagi biztonságot, a környezet tisztaságát és a szabadidő mennyiségét.",
                    "Csak a televízió képernyőjének méretét.",
                    "Kizárólag az autók márkáját."
                ],
                "correct": 0
            },
            {
                "id": "b1-11-03-dialogue-1",
                "type": "multiple-choice",
                "category": "reading",
                "question": "— Nem túl fárasztó a mindennapos ______ a városba?\n— Vonattal gyorsan beérek, és útközben nyugodtan tudok olvasni.",
                "options": ["ingázás", "felújítás", "koronázás"],
                "correct": 0
            },
            {
                "id": "b1-11-03-dialogue-2",
                "type": "multiple-choice",
                "category": "reading",
                "question": "— Miért költöztetek ki vidékre?\n— A gyerekeinknek sokkal jobb itt az ______, tiszta a levegő és nagy a kert.",
                "options": ["életminősége", "defterdára", "főbérlője"],
                "correct": 0
            },
            {
                "id": "b1-11-03-writing-1",
                "type": "fill-blank",
                "category": "production",
                "sentence": "A gyorsuló ____ miatt egyre többen vándorolnak be a nagyvárosokba. (urbanization)",
                "answer": "városiasodás"
            },
            {
                "id": "b1-11-03-writing-2",
                "type": "fill-blank",
                "category": "production",
                "sentence": "A budapesti lakások nagyon drágák, ezzel ____ a vidéki házak jóval elérhetőbbek. (in contrast / szemben)",
                "answer": "szemben"
            },
            {
                "id": "b1-11-03-check-1",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Mit jelent a 'vidék' kifejezés?",
                "options": ["The countryside / provinces", "The capital city", "The subway station"],
                "correct": 0
            },
            {
                "id": "b1-11-03-check-2",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik szó jelenti a minőségi emberi létet?",
                "options": ["életminőség", "életmód", "életrajz"],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-11-03-ex.json", ex_03)

    ex_04 = {
        "lesson": "b1-11-04",
        "exercises": [
            {
                "id": "b1-11-04-intro-1",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["látványosság", "sight / attraction"],
                    ["idegenvezető", "tour guide"],
                    ["vendéglátás", "hospitality / catering"],
                    ["úticél", "travel destination"]
                ]
            },
            {
                "id": "b1-11-04-intro-2",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["érdemes megnézni", "worth seeing"],
                    ["mindenképpen ajánlom", "definitely recommend"],
                    ["ha teheted", "if you can"],
                    ["rejtett kincs", "hidden gem"]
                ]
            },
            {
                "id": "b1-11-04-controlled-1",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik szerkezet fejez ki udvarias ajánlást a mondatban: „______ a szegedi Dóm teret.”?",
                "options": ["Mindenképpen érdemes megnézni", "Szigorúan tilos belépni", "Nem szabad keresni"],
                "correct": 0
            },
            {
                "id": "b1-11-04-controlled-2",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Hogyan mondjuk: 'if you have the chance / if you can' magyarul?",
                "options": ["Ha teheted", "Ha akarsz", "Ha láttad"],
                "correct": 0
            },
            {
                "id": "b1-11-04-controlled-3",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Ki az az 'idegenvezető'?",
                "options": [
                    "Aki szakszerűen bemutatja egy város látnivalóit a turistáknak.",
                    "Aki az autókat javítja.",
                    "Aki a vasútállomáson jegyet ad el."
                ],
                "correct": 0
            },
            {
                "id": "b1-11-04-controlled-4",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik mondat ajánl egy úti célt a legválasztékosabban?",
                "options": [
                    "Ha Pécsre látogatsz, szívből ajánlom a Zsolnay Kulturális Negyedet.",
                    "Menj Pécsre és ne csinálj semmit.",
                    "Pécs nem érdekel senkit."
                ],
                "correct": 0
            },
            {
                "id": "b1-11-04-practice-1",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A történelmi belvárosban lépten-nyomon híres műemlék és ____ fogadja a látogatókat. (tourist attraction)",
                "answer": "látványosság"
            },
            {
                "id": "b1-11-04-practice-2",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A tapasztalt ____ izgalmas történeteket mesélt a budavári palota rejtélyeiről. (tour guide)",
                "answer": "idegenvezető"
            },
            {
                "id": "b1-11-04-practice-3",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Melyik magyarországi város híres a borairól és a barokk belvárosáról?",
                "options": ["Eger.", "Dunaújváros.", "Százhalombatta."],
                "correct": 0
            },
            {
                "id": "b1-11-04-practice-4",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Mit jelent a minőségi 'vendéglátás' a turizmusban?",
                "options": [
                    "Finom ételeket, udvarias kiszolgálást, tiszta szállást és meleg szívű fogadtatást.",
                    "Csak a drága éttermek étlapját.",
                    "A külföldi turisták elkerülését."
                ],
                "correct": 0
            },
            {
                "id": "b1-11-04-dialogue-1",
                "type": "multiple-choice",
                "category": "reading",
                "question": "— Melyik várost válasszuk a hétvégi kirándulásunkhoz?\n— Pécs nagyszerű ______, tele van múzeumokkal és mediterrán terekkel.",
                "options": ["úticél", "defterdár", "kaució"],
                "correct": 0
            },
            {
                "id": "b1-11-04-dialogue-2",
                "type": "multiple-choice",
                "category": "reading",
                "question": "— Tudsz ajánlani egy jó éttermet?\n— Igen, a folyóparti halászcsárdában a helyi ______ egyszerűen elsőrangú.",
                "options": ["vendéglátás", "ingázás", "hadrend"],
                "correct": 0
            },
            {
                "id": "b1-11-04-writing-1",
                "type": "fill-blank",
                "category": "production",
                "sentence": "Ha a Balatonnál nyaralsz, feltétlenül ____ megnézni a tihanyi apátságot. (worth / érdemes)",
                "answer": "érdemes"
            },
            {
                "id": "b1-11-04-writing-2",
                "type": "fill-blank",
                "category": "production",
                "sentence": "Sopron a hűség városa, amely népszerű turisztikai ____ vált az utóbbi években. (destination - translative: céllá)",
                "answer": "céllá"
            },
            {
                "id": "b1-11-04-check-1",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Mi az 'úticél'?",
                "options": ["Travel destination", "Gas station", "Highway ticket"],
                "correct": 0
            },
            {
                "id": "b1-11-04-check-2",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Hogyan nevezzük az éttermek, kávézók és szállodák ágazatát?",
                "options": ["vendéglátás", "világítás", "meggyengülés"],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-11-04-ex.json", ex_04)

    ex_05 = {
        "lesson": "b1-11-05",
        "exercises": [
            {
                "id": "b1-11-05-intro-1",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["önkormányzat", "local government / municipality"],
                    ["közösségi tér", "community space"],
                    ["egyesület", "civic association"],
                    ["rendezvény", "public event / function"]
                ]
            },
            {
                "id": "b1-11-05-intro-2",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["részt vesz", "to participate in"],
                    ["hozzájárul", "to contribute to"],
                    ["együttműködik", "to cooperate with"],
                    ["megszervez", "to organize / arrange"]
                ]
            },
            {
                "id": "b1-11-05-controlled-1",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Milyen vonzattal áll a 'részt vesz' ige a mondatban: „A lakók részt vesznek a ______.”?",
                "options": ["rendezvényen (vagy rendezvényben)", "rendezvényhez", "rendezvényből"],
                "correct": 0
            },
            {
                "id": "b1-11-05-controlled-2",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Milyen ragot kíván a 'hozzájárul' ige?",
                "options": ["-hoz / -hez / -höz", "-ban / -ben", "-ról / -ről"],
                "correct": 0
            },
            {
                "id": "b1-11-05-controlled-3",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik mondat fejezi ki helyesen az együttműködést?",
                "options": [
                    "A helyi egyesület szorosan együttműködik az önkormányzattal.",
                    "A helyi egyesület szorosan együttműködik az önkormányzatot.",
                    "A helyi egyesület szorosan együttműködik az önkormányzathoz."
                ],
                "correct": 0
            },
            {
                "id": "b1-11-05-controlled-4",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Mi a szerepe a helyi 'önkormányzatnak' egy településen?",
                "options": [
                    "A helyi közügyek (iskolák, utak, tisztaság, fejlesztések) demokratikus irányítása és intézése.",
                    "Kizárólag külföldi nagykövetségek fenntartása.",
                    "Csak a katonai sorozás lebonyolítása."
                ],
                "correct": 0
            },
            {
                "id": "b1-11-05-practice-1",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A felújított művelődési ház modern ____ vált a fiatalok számára. (community space - translative: térré)",
                "answer": "térré"
            },
            {
                "id": "b1-11-05-practice-2",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A lakók önkéntes munkával járulnak ____ a park megtisztításához. (to it / contribute: hozzá)",
                "answer": "hozzá"
            },
            {
                "id": "b1-11-05-practice-3",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Milyen kulturális rendezvényeket szerveznek a magyar városokban nyaranta?",
                "options": [
                    "Fesztiválokat, színházi esteket, kézműves vásárokat és koncerteket a főtereken.",
                    "Csak kötelező katonai felvonulásokat.",
                    "Semmilyen nyilvános esemény nem engedélyezett."
                ],
                "correct": 0
            },
            {
                "id": "b1-11-05-practice-4",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Hogyan erősítheti egy civil egyesület a helyi közösséget?",
                "options": [
                    "Közös célokért dolgozva összefogja a hasonló érdeklődésű polgárokat és támogatja a rászorulókat.",
                    "Megakadályozza a szomszédok közötti beszélgetést.",
                    "Bezárja a közösségi tereket."
                ],
                "correct": 0
            },
            {
                "id": "b1-11-05-dialogue-1",
                "type": "multiple-choice",
                "category": "reading",
                "question": "— Ki szervezi a hétvégi falunapot?\n— A helyi ______ a civil egyesületekkel közösen rendezi meg.",
                "options": ["önkormányzat", "zsoldos", "szultán"],
                "correct": 0
            },
            {
                "id": "b1-11-05-dialogue-2",
                "type": "multiple-choice",
                "category": "reading",
                "question": "— Részt veszel a holnapi faültetésen?\n— Természetesen, szívesen hozzájárulok a környékünk szebbé ______.",
                "options": ["tételéhez", "rombolásához", "eladásihoz"],
                "correct": 0
            },
            {
                "id": "b1-11-05-writing-1",
                "type": "fill-blank",
                "category": "production",
                "sentence": "A sport____ célja, hogy minden gyermek számára biztosítsa a mozgás örömét. (association / club)",
                "answer": "egyesület"
            },
            {
                "id": "b1-11-05-writing-2",
                "type": "fill-blank",
                "category": "production",
                "sentence": "A múlt hétvégi kulturális ____ több ezer érdeklődő látogatott el. (to the event)",
                "answer": "rendezvényre"
            },
            {
                "id": "b1-11-05-reading-1",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Hol játszódik a Móricz Zsigmond-részlet (Légy jó mindhalálig)?",
                "options": [
                    "Debrecenben, a patinás református kollégium és a Nagytemplom városában.",
                    "Egy osztrák hegyi faluban.",
                    "A budai várnegyedben."
                ],
                "correct": 0
            },
            {
                "id": "b1-11-05-reading-2",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Kihez ment felolvasni Nyilas Misi délutánonként?",
                "options": [
                    "A vak Pósalaky úrhoz a lutri számait és az újságot felolvasni.",
                    "A polgármesterhez zongorázni.",
                    "Az egri várkapitányhoz."
                ],
                "correct": 0
            },
            {
                "id": "b1-11-05-reading-3",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Milyen érzés töltötte el Misit a debreceni utcákon sétálva?",
                "options": [
                    "Átérezte, milyen felelősségteljes dolog egy igazi közösség hasznos tagjává válni.",
                    "Nagyon unatkozott és haza akart szökni.",
                    "Haragudott az összes emberre."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-11-05-ex.json", ex_05)

    ex_consolidation = {
        "lesson": "b1-11-consolidation",
        "exercises": [
            {
                "id": "b1-11-consolidation-1",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["település", "settlement"],
                    ["infrastruktúra", "infrastructure"],
                    ["közbiztonság", "public safety"],
                    ["összetartás", "solidarity"]
                ]
            },
            {
                "id": "b1-11-consolidation-2",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["vidék", "countryside"],
                    ["ingázás", "commuting"],
                    ["életminőség", "quality of life"],
                    ["városiasodás", "urbanization"]
                ]
            },
            {
                "id": "b1-11-consolidation-3",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["önkormányzat", "local municipality"],
                    ["közösségi tér", "community hub"],
                    ["egyesület", "association"],
                    ["látványosság", "attraction"]
                ]
            },
            {
                "id": "b1-11-consolidation-4",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik vonatkozó névmás illik az élettelen konkrét főnévre: „A könyvtár, ______ felújítottak, nagyon modern.”?",
                "options": ["amelyet", "akit", "akinek"],
                "correct": 0
            },
            {
                "id": "b1-11-consolidation-5",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Hogyan képezzük a 'falu' szóból az ott lakó embertársra utaló alakot?",
                "options": ["falubeli", "faluban", "falura"],
                "correct": 0
            },
            {
                "id": "b1-11-consolidation-6",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik vonzat helyes a mondatban: „A fiatalok aktívan részt vettek a ______.”?",
                "options": ["rendezvényen", "rendezvényhez", "rendezvényért"],
                "correct": 0
            },
            {
                "id": "b1-11-consolidation-7",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A nagyvárosban sok a kulturális program, ____ vidéken békésebb a mindennapi élet. (while / whereas)",
                "answer": "míg"
            },
            {
                "id": "b1-11-consolidation-8",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A helyi lakosok szívesen járulnak hozzá a lakókörnyezetük szép____. (making it prettier - translative)",
                "answer": "tételéhez"
            },
            {
                "id": "b1-11-consolidation-9",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Ha a Dunakanyarban jársz, mindenképpen ____ meglátogatni Visegrád fellegvárát. (worth)",
                "answer": "érdemes"
            },
            {
                "id": "b1-11-consolidation-10",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Mit jelent a közösség 'összetartása' a mindennapi életben?",
                "options": [
                    "Egymás támogatását, a közös programokat és a felelősségérzetet a lakókörnyezetért.",
                    "A lakások eladását.",
                    "A rendőrségi büntetéseket."
                ],
                "correct": 0
            },
            {
                "id": "b1-11-consolidation-11",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Melyik klasszikus regényben szerepel Nyilas Misi és a debreceni kollégiumi közösség?",
                "options": [
                    "Móricz Zsigmond: Légy jó mindhalálig.",
                    "Kosztolányi Dezső: Édes Anna.",
                    "Petőfi Sándor: János vitéz."
                ],
                "correct": 0
            },
            {
                "id": "b1-11-consolidation-12",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Miért fontos a jó infrastruktúra egy fejlődő település számára?",
                "options": [
                    "Mert vonzóvá teszi a helyet a családok és a munkahelyteremtő vállalkozások számára.",
                    "Mert elriasztja a turistákat.",
                    "Mert megszünteti a boltokat."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-11-consolidation-ex.json", ex_consolidation)

    # -------------------------------------------------------------------------
    # 5. Lesson Files (6 lessons)
    # -------------------------------------------------------------------------
    lesson_01 = {
        "id": "lesson.b1.11-01",
        "unit": 11,
        "title": "A Place That Has Everything",
        "level": "B1",
        "grammar": "Relative Pronouns & Case Forms: aki, ami, amely, amelyben, akinek",
        "goal": [
            "I can describe municipalities, amenities, and population trends using relative pronouns.",
            "I can accurately decline relative pronouns (amelyben, akinek, amiről).",
            "I can differentiate between informal ami and literary amely in complex descriptions.",
            "I can use four new vocabulary items related to settlements and infrastructure."
        ],
        "sections": [
            {
                "type": "goal",
                "title": "Lesson Goals",
                "items": [
                    "I can describe municipalities, amenities, and population trends using relative pronouns.",
                    "I can accurately decline relative pronouns (amelyben, akinek, amiről).",
                    "I can differentiate between informal ami and literary amely in complex descriptions.",
                    "I can use four new vocabulary items related to settlements and infrastructure."
                ]
            },
            {"type": "recycle", "title": "Quick Review"},
            {"type": "grammar", "ref": "grammar/b1/b1-11-01-a-gr.json"},
            {"type": "grammar", "ref": "grammar/b1/b1-11-01-b-gr.json"},
            {"type": "vocabulary", "title": "Lesson Vocabulary", "ref": "vocabulary/b1/b1-11-01-voc.json"},
            {"type": "exercise-group", "title": "Introduce", "ref": "exercises/b1/b1-11-01-ex.json", "exerciseRefs": ["b1-11-01-intro-1", "b1-11-01-intro-2"]},
            {"type": "exercise-group", "title": "Controlled", "ref": "exercises/b1/b1-11-01-ex.json", "exerciseRefs": ["b1-11-01-controlled-1", "b1-11-01-controlled-2", "b1-11-01-controlled-3", "b1-11-01-controlled-4"]},
            {"type": "exercise-group", "title": "Practice", "ref": "exercises/b1/b1-11-01-ex.json", "exerciseRefs": ["b1-11-01-practice-1", "b1-11-01-practice-2", "b1-11-01-practice-3", "b1-11-01-practice-4"]},
            {"type": "exercise-group", "title": "Dialogue", "ref": "exercises/b1/b1-11-01-ex.json", "exerciseRefs": ["b1-11-01-dialogue-1", "b1-11-01-dialogue-2"]},
            {"type": "exercise-group", "title": "Production", "ref": "exercises/b1/b1-11-01-ex.json", "exerciseRefs": ["b1-11-01-writing-1", "b1-11-01-writing-2"]},
            {"type": "srs", "title": "Add to Review"},
            {"type": "exercise-group", "title": "Check", "ref": "exercises/b1/b1-11-01-ex.json", "exerciseRefs": ["b1-11-01-check-1", "b1-11-01-check-2"]},
            {
                "type": "checklist",
                "title": "Can you do this?",
                "items": [
                    "I can describe municipalities, amenities, and population trends using relative pronouns.",
                    "I can accurately decline relative pronouns (amelyben, akinek, amiről).",
                    "I can differentiate between informal ami and literary amely in complex descriptions.",
                    "I can use four new vocabulary items related to settlements and infrastructure."
                ]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-11-01.json", lesson_01)

    lesson_02 = {
        "id": "lesson.b1.11-02",
        "unit": 11,
        "title": "What Makes a Neighbourhood",
        "level": "B1",
        "grammar": "Spatial Affiliation Suffix: -beli (környékbeli, helybeli, lakótelepi)",
        "goal": [
            "I can describe housing estates, green belts, and public safety.",
            "I can derive and use adjectives of community belonging using the -beli suffix.",
            "I can discuss neighborhood solidarity and community cohesion in Hungarian.",
            "I can use four new vocabulary items related to residential zones and safety."
        ],
        "sections": [
            {
                "type": "goal",
                "title": "Lesson Goals",
                "items": [
                    "I can describe housing estates, green belts, and public safety.",
                    "I can derive and use adjectives of community belonging using the -beli suffix.",
                    "I can discuss neighborhood solidarity and community cohesion in Hungarian.",
                    "I can use four new vocabulary items related to residential zones and safety."
                ]
            },
            {"type": "recycle", "title": "Quick Review"},
            {"type": "grammar", "ref": "grammar/b1/b1-11-02-gr.json"},
            {"type": "vocabulary", "title": "Lesson Vocabulary", "ref": "vocabulary/b1/b1-11-02-voc.json"},
            {"type": "exercise-group", "title": "Introduce", "ref": "exercises/b1/b1-11-02-ex.json", "exerciseRefs": ["b1-11-02-intro-1", "b1-11-02-intro-2"]},
            {"type": "exercise-group", "title": "Controlled", "ref": "exercises/b1/b1-11-02-ex.json", "exerciseRefs": ["b1-11-02-controlled-1", "b1-11-02-controlled-2", "b1-11-02-controlled-3", "b1-11-02-controlled-4"]},
            {"type": "exercise-group", "title": "Practice", "ref": "exercises/b1/b1-11-02-ex.json", "exerciseRefs": ["b1-11-02-practice-1", "b1-11-02-practice-2", "b1-11-02-practice-3", "b1-11-02-practice-4"]},
            {"type": "exercise-group", "title": "Dialogue", "ref": "exercises/b1/b1-11-02-ex.json", "exerciseRefs": ["b1-11-02-dialogue-1", "b1-11-02-dialogue-2"]},
            {"type": "exercise-group", "title": "Production", "ref": "exercises/b1/b1-11-02-ex.json", "exerciseRefs": ["b1-11-02-writing-1", "b1-11-02-writing-2"]},
            {"type": "srs", "title": "Add to Review"},
            {"type": "exercise-group", "title": "Check", "ref": "exercises/b1/b1-11-02-ex.json", "exerciseRefs": ["b1-11-02-check-1", "b1-11-02-check-2"]},
            {
                "type": "checklist",
                "title": "Can you do this?",
                "items": [
                    "I can describe housing estates, green belts, and public safety.",
                    "I can derive and use adjectives of community belonging using the -beli suffix.",
                    "I can discuss neighborhood solidarity and community cohesion in Hungarian.",
                    "I can use four new vocabulary items related to residential zones and safety."
                ]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-11-02.json", lesson_02)

    lesson_03 = {
        "id": "lesson.b1.11-03",
        "unit": 11,
        "title": "Comparing City & Countryside",
        "level": "B1",
        "grammar": "Contrastive Conjunctions: míg, ellenben, ezzel szemben",
        "goal": [
            "I can compare and contrast city and countryside lifestyles using nuanced connectors.",
            "I can discuss urbanization, commuting (ingázás), and quality of life.",
            "I can structure persuasive arguments weighing quiet surroundings against convenience.",
            "I can use four new vocabulary items related to regional lifestyles and commuting."
        ],
        "sections": [
            {
                "type": "goal",
                "title": "Lesson Goals",
                "items": [
                    "I can compare and contrast city and countryside lifestyles using nuanced connectors.",
                    "I can discuss urbanization, commuting (ingázás), and quality of life.",
                    "I can structure persuasive arguments weighing quiet surroundings against convenience.",
                    "I can use four new vocabulary items related to regional lifestyles and commuting."
                ]
            },
            {"type": "recycle", "title": "Quick Review"},
            {"type": "grammar", "ref": "grammar/b1/b1-11-03-gr.json"},
            {"type": "vocabulary", "title": "Lesson Vocabulary", "ref": "vocabulary/b1/b1-11-03-voc.json"},
            {"type": "exercise-group", "title": "Introduce", "ref": "exercises/b1/b1-11-03-ex.json", "exerciseRefs": ["b1-11-03-intro-1", "b1-11-03-intro-2"]},
            {"type": "exercise-group", "title": "Controlled", "ref": "exercises/b1/b1-11-03-ex.json", "exerciseRefs": ["b1-11-03-controlled-1", "b1-11-03-controlled-2", "b1-11-03-controlled-3", "b1-11-03-controlled-4"]},
            {"type": "exercise-group", "title": "Practice", "ref": "exercises/b1/b1-11-03-ex.json", "exerciseRefs": ["b1-11-03-practice-1", "b1-11-03-practice-2", "b1-11-03-practice-3", "b1-11-03-practice-4"]},
            {"type": "exercise-group", "title": "Dialogue", "ref": "exercises/b1/b1-11-03-ex.json", "exerciseRefs": ["b1-11-03-dialogue-1", "b1-11-03-dialogue-2"]},
            {"type": "exercise-group", "title": "Production", "ref": "exercises/b1/b1-11-03-ex.json", "exerciseRefs": ["b1-11-03-writing-1", "b1-11-03-writing-2"]},
            {"type": "srs", "title": "Add to Review"},
            {"type": "exercise-group", "title": "Check", "ref": "exercises/b1/b1-11-03-ex.json", "exerciseRefs": ["b1-11-03-check-1", "b1-11-03-check-2"]},
            {
                "type": "checklist",
                "title": "Can you do this?",
                "items": [
                    "I can compare and contrast city and countryside lifestyles using nuanced connectors.",
                    "I can discuss urbanization, commuting (ingázás), and quality of life.",
                    "I can structure persuasive arguments weighing quiet surroundings against convenience.",
                    "I can use four new vocabulary items related to regional lifestyles and commuting."
                ]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-11-03.json", lesson_03)

    lesson_04 = {
        "id": "lesson.b1.11-04",
        "unit": 11,
        "title": "A Place I'd Recommend",
        "level": "B1",
        "grammar": "Recommending Sights & Activities: érdemes megnézni, ha teheted",
        "goal": [
            "I can recommend tourist destinations, sights, and hospitality venues in Hungary.",
            "I can offer polite travel suggestions using érdemes and conditional phrasing.",
            "I can discuss tour guides, local heritage, and hidden culinary gems.",
            "I can use four new vocabulary items related to tourism and hospitality."
        ],
        "sections": [
            {
                "type": "goal",
                "title": "Lesson Goals",
                "items": [
                    "I can recommend tourist destinations, sights, and hospitality venues in Hungary.",
                    "I can offer polite travel suggestions using érdemes and conditional phrasing.",
                    "I can discuss tour guides, local heritage, and hidden culinary gems.",
                    "I can use four new vocabulary items related to tourism and hospitality."
                ]
            },
            {"type": "recycle", "title": "Quick Review"},
            {"type": "grammar", "ref": "grammar/b1/b1-11-04-gr.json"},
            {"type": "vocabulary", "title": "Lesson Vocabulary", "ref": "vocabulary/b1/b1-11-04-voc.json"},
            {"type": "exercise-group", "title": "Introduce", "ref": "exercises/b1/b1-11-04-ex.json", "exerciseRefs": ["b1-11-04-intro-1", "b1-11-04-intro-2"]},
            {"type": "exercise-group", "title": "Controlled", "ref": "exercises/b1/b1-11-04-ex.json", "exerciseRefs": ["b1-11-04-controlled-1", "b1-11-04-controlled-2", "b1-11-04-controlled-3", "b1-11-04-controlled-4"]},
            {"type": "exercise-group", "title": "Practice", "ref": "exercises/b1/b1-11-04-ex.json", "exerciseRefs": ["b1-11-04-practice-1", "b1-11-04-practice-2", "b1-11-04-practice-3", "b1-11-04-practice-4"]},
            {"type": "exercise-group", "title": "Dialogue", "ref": "exercises/b1/b1-11-04-ex.json", "exerciseRefs": ["b1-11-04-dialogue-1", "b1-11-04-dialogue-2"]},
            {"type": "exercise-group", "title": "Production", "ref": "exercises/b1/b1-11-04-ex.json", "exerciseRefs": ["b1-11-04-writing-1", "b1-11-04-writing-2"]},
            {"type": "srs", "title": "Add to Review"},
            {"type": "exercise-group", "title": "Check", "ref": "exercises/b1/b1-11-04-ex.json", "exerciseRefs": ["b1-11-04-check-1", "b1-11-04-check-2"]},
            {
                "type": "checklist",
                "title": "Can you do this?",
                "items": [
                    "I can recommend tourist destinations, sights, and hospitality venues in Hungary.",
                    "I can offer polite travel suggestions using érdemes and conditional phrasing.",
                    "I can discuss tour guides, local heritage, and hidden culinary gems.",
                    "I can use four new vocabulary items related to tourism and hospitality."
                ]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-11-04.json", lesson_04)

    lesson_05 = {
        "id": "lesson.b1.11-05",
        "unit": 11,
        "title": "Describing My Community",
        "level": "B1",
        "grammar": "Civic Engagement Verb Governments: részt vesz vmiben, hozzájárul vmihez",
        "goal": [
            "I can discuss local government, civic associations, and community hubs.",
            "I can correctly use verb governments related to participation (részt vesz, hozzájárul).",
            "I can use four new vocabulary items related to local administration and public events.",
            "I can read and understand an adapted literary excerpt from Móricz Zsigmond's Légy jó mindhalálig."
        ],
        "sections": [
            {
                "type": "goal",
                "title": "Lesson Goals",
                "items": [
                    "I can discuss local government, civic associations, and community hubs.",
                    "I can correctly use verb governments related to participation (részt vesz, hozzájárul).",
                    "I can use four new vocabulary items related to local administration and public events.",
                    "I can read and understand an adapted literary excerpt from Móricz Zsigmond's Légy jó mindhalálig."
                ]
            },
            {"type": "recycle", "title": "Quick Review"},
            {"type": "grammar", "ref": "grammar/b1/b1-11-05-gr.json"},
            {"type": "vocabulary", "title": "Lesson Vocabulary", "ref": "vocabulary/b1/b1-11-05-voc.json"},
            {"type": "exercise-group", "title": "Introduce", "ref": "exercises/b1/b1-11-05-ex.json", "exerciseRefs": ["b1-11-05-intro-1", "b1-11-05-intro-2"]},
            {"type": "exercise-group", "title": "Controlled", "ref": "exercises/b1/b1-11-05-ex.json", "exerciseRefs": ["b1-11-05-controlled-1", "b1-11-05-controlled-2", "b1-11-05-controlled-3", "b1-11-05-controlled-4"]},
            {"type": "exercise-group", "title": "Practice", "ref": "exercises/b1/b1-11-05-ex.json", "exerciseRefs": ["b1-11-05-practice-1", "b1-11-05-practice-2", "b1-11-05-practice-3", "b1-11-05-practice-4"]},
            {"type": "exercise-group", "title": "Dialogue", "ref": "exercises/b1/b1-11-05-ex.json", "exerciseRefs": ["b1-11-05-dialogue-1", "b1-11-05-dialogue-2"]},
            {"type": "exercise-group", "title": "Production", "ref": "exercises/b1/b1-11-05-ex.json", "exerciseRefs": ["b1-11-05-writing-1", "b1-11-05-writing-2"]},
            {"type": "srs", "title": "Add to Review"},
            {
                "type": "story",
                "title": "Reading: Nyilas Misi Debrecen városában",
                "ref": "stories/classics/b1/b1-11-legyjomindhalalig.json"
            },
            {"type": "exercise-group", "title": "Reading", "ref": "exercises/b1/b1-11-05-ex.json", "exerciseRefs": ["b1-11-05-reading-1", "b1-11-05-reading-2", "b1-11-05-reading-3"]},
            {
                "type": "checklist",
                "title": "Can you do this?",
                "items": [
                    "I can discuss local government, civic associations, and community hubs.",
                    "I can correctly use verb governments related to participation (részt vesz, hozzájárul).",
                    "I can use four new vocabulary items related to local administration and public events.",
                    "I can read and understand an adapted literary excerpt from Móricz Zsigmond's Légy jó mindhalálig."
                ]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-11-05.json", lesson_05)

    lesson_consolidation = {
        "id": "lesson.b1.11-consolidation",
        "unit": 11,
        "title": "Unit 11 Consolidation",
        "level": "B1",
        "sections": [
            {
                "type": "goal",
                "title": "Consolidation Goals",
                "items": [
                    "I can use case-inflected relative pronouns to describe towns and infrastructure.",
                    "I can apply the -beli suffix for neighborhood affiliation.",
                    "I can contrast city and rural lifestyles using míg and ellenben.",
                    "I can express civic engagement using participating verb governments."
                ]
            },
            {"type": "recycle", "title": "Quick Review"},
            {"type": "exercise-group", "title": "Recognize", "ref": "exercises/b1/b1-11-consolidation-ex.json", "exerciseRefs": ["b1-11-consolidation-1", "b1-11-consolidation-2", "b1-11-consolidation-3"]},
            {"type": "exercise-group", "title": "Recall", "ref": "exercises/b1/b1-11-consolidation-ex.json", "exerciseRefs": ["b1-11-consolidation-4", "b1-11-consolidation-5", "b1-11-consolidation-6"]},
            {"type": "exercise-group", "title": "In Context", "ref": "exercises/b1/b1-11-consolidation-ex.json", "exerciseRefs": ["b1-11-consolidation-7", "b1-11-consolidation-8", "b1-11-consolidation-9"]},
            {"type": "exercise-group", "title": "Produce", "ref": "exercises/b1/b1-11-consolidation-ex.json", "exerciseRefs": ["b1-11-consolidation-10", "b1-11-consolidation-11", "b1-11-consolidation-12"]},
            {
                "type": "checklist",
                "title": "Can you do this?",
                "items": [
                    "I can use case-inflected relative pronouns to describe towns and infrastructure.",
                    "I can apply the -beli suffix for neighborhood affiliation.",
                    "I can contrast city and rural lifestyles using míg and ellenben.",
                    "I can express civic engagement using participating verb governments."
                ]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-11-consolidation.json", lesson_consolidation)

if __name__ == "__main__":
    build_unit_11_core()
    print("Successfully built Hungarian B1 Core Unit 11!")
