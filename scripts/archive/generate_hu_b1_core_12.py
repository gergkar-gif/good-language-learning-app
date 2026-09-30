#!/usr/bin/env python3
"""Generate Hungarian B1 Core Unit 12: Food & Lifestyle (b1-12)."""

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

def build_unit_12_core():
    # -------------------------------------------------------------------------
    # 1. Vocabulary Files (4 words each = 20 words total)
    # -------------------------------------------------------------------------
    voc_01 = {
        "id": "vocab.b1.12.01",
        "lesson": "b1-12-01",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "hozzávaló", "translation": "ingredient", "pos": "noun"},
            {"lemma": "fűszer", "translation": "spice, seasoning", "pos": "noun"},
            {"lemma": "alapanyag", "translation": "raw ingredient, staple", "pos": "noun"},
            {"lemma": "előkészítés", "translation": "preparation, prepping", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-12-01-voc.json", voc_01)

    voc_02 = {
        "id": "vocab.b1.12.02",
        "lesson": "b1-12-02",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "táplálkozási szokás", "translation": "dietary habit, eating pattern", "pos": "noun"},
            {"lemma": "fogyókúra", "translation": "weight-loss diet, slimming cure", "pos": "noun"},
            {"lemma": "rost", "translation": "dietary fiber", "pos": "noun"},
            {"lemma": "vitaminbevitel", "translation": "vitamin intake", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-12-02-voc.json", voc_02)

    voc_03 = {
        "id": "vocab.b1.12.03",
        "lesson": "b1-12-03",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "recept", "translation": "recipe", "pos": "noun"},
            {"lemma": "elkészítési mód", "translation": "preparation method, instructions", "pos": "noun"},
            {"lemma": "sütési idő", "translation": "baking / cooking time", "pos": "noun"},
            {"lemma": "adag", "translation": "portion, serving", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-12-03-voc.json", voc_03)

    voc_04 = {
        "id": "vocab.b1.12.04",
        "lesson": "b1-12-04",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "gasztronómia", "translation": "gastronomy, culinary culture", "pos": "noun"},
            {"lemma": "hungarikum", "translation": "Hungarikum (unique national treasure)", "pos": "noun"},
            {"lemma": "hagyományőrzés", "translation": "preservation of culinary tradition", "pos": "noun"},
            {"lemma": "ízvilág", "translation": "flavor profile, taste spectrum", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-12-04-voc.json", voc_04)

    voc_05 = {
        "id": "vocab.b1.12.05",
        "lesson": "b1-12-05",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "fogás", "translation": "course, dish in a meal", "pos": "noun"},
            {"lemma": "pincér", "translation": "waiter, server", "pos": "noun"},
            {"lemma": "borravaló", "translation": "tip, gratuity", "pos": "noun"},
            {"lemma": "számla", "translation": "restaurant bill, check", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-12-05-voc.json", voc_05)

    # -------------------------------------------------------------------------
    # 2. Grammar Files
    # -------------------------------------------------------------------------
    gr_01_a = {
        "id": "grammar.b1.12.01.mediopassive-cooking",
        "title": "Mediopassive & Inchoative Verbs in Cooking: -ódik / -ődik, -ul / -ül",
        "sections": [
            {
                "type": "text",
                "title": "Describing Cooking Processes Without Specifying the Agent",
                "content": "To describe how food cooks and transforms, Hungarian employs mediopassive verbs (*-ódik / -ődik*) and inchoative verbs (*-ul / -ül*): *megsül* (bakes/roasts), *megfő* (cooks/boils), *megpuhul* (becomes soft/tender), *összekeveredik* (gets mixed together), *elkészül* (gets completed/done)."
            },
            {
                "type": "examples",
                "title": "Cooking process examples",
                "items": [
                    {
                        "spanish": "A leves lassú tűzön, gyöngyözve fő meg két óra alatt.",
                        "english": "The soup simmers gently on low heat and finishes cooking in two hours."
                    },
                    {
                        "spanish": "Amikor a hús teljesen megpuhul, hozzáadjuk a friss zöldségeket.",
                        "english": "When the meat becomes completely tender, we add the fresh vegetables."
                    },
                    {
                        "spanish": "A tészta a forró sütőben szép pirosra sül.",
                        "english": "The dough bakes to a nice golden-red in the hot oven."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-12-01-a-gr.json", gr_01_a)

    gr_01_b = {
        "id": "grammar.b1.12.01.preparatory-prefixes",
        "title": "Verbal Prefixes in Food Preparation: fel-, le-, össze-, át-",
        "sections": [
            {
                "type": "text",
                "title": "Action Prefixes for Kitchen Verbs",
                "content": "Specific prefixes refine culinary actions: *felaprít* (chop up finely), *letisztít* (clean/peel), *összekever* (mix together), *átpasszíroz* (strain through a sieve), *megízesít* (season/flavor)."
            },
            {
                "type": "examples",
                "title": "Kitchen prefix examples",
                "items": [
                    {
                        "spanish": "A hagymát apróra vágjuk és kevés olajon megdinszteljük.",
                        "english": "We chop the onion finely and sauté it in a little oil."
                    },
                    {
                        "spanish": "A hozzávalókat egy nagy tálban alaposan összekeverjük.",
                        "english": "We mix the ingredients together thoroughly in a large bowl."
                    },
                    {
                        "spanish": "A paprikás mártást átpasszírozzuk a selymes állag eléréséhez.",
                        "english": "We strain the paprika sauce through to achieve a silky texture."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-12-01-b-gr.json", gr_01_b)

    gr_02 = {
        "id": "grammar.b1.12.02.dietary-frequency",
        "title": "Expressing Habitual Routine & Frequency in Lifestyle",
        "sections": [
            {
                "type": "text",
                "title": "Describing Eating Habits and Nutritional Regularity",
                "content": "To formulate lifestyle habits, use frequency adverbs: *rendszeresen* (regularly), *naponta kétszer* (twice a day), *időnként* (from time to time), *ritkán* (rarely), and temporal postpositions: *étkezés előtt* (before meals), *vacsora után* (after dinner)."
            },
            {
                "type": "examples",
                "title": "Dietary routine examples",
                "items": [
                    {
                        "spanish": "Az egészséges életmódhoz fontos, hogy rendszeresen fogyasszunk friss zöldséget.",
                        "english": "For a healthy lifestyle, it is important to consume fresh vegetables regularly."
                    },
                    {
                        "spanish": "A megfelelő vitaminbevitel érdekében naponta többször eszem gyümölcsöt.",
                        "english": "In order to ensure proper vitamin intake, I eat fruit several times a day."
                    },
                    {
                        "spanish": "A szigorú fogyókúra helyett a kiegyensúlyozott táplálkozásban hiszek.",
                        "english": "Instead of strict weight-loss diets, I believe in balanced nutrition."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-12-02-gr.json", gr_02)

    gr_03 = {
        "id": "grammar.b1.12.03.recipe-sequencing",
        "title": "Sequential Instructions in Recipes: először, miután, amint, végül",
        "sections": [
            {
                "type": "text",
                "title": "Chronological Recipe Connectors",
                "content": "Writing and following recipes requires sequential temporal markers: *először* (first), *majd / ezt követően* (then / subsequently), *miután* (+ past: after having...), *amint* (as soon as), *végül* (finally / to finish)."
            },
            {
                "type": "examples",
                "title": "Recipe sequence examples",
                "items": [
                    {
                        "spanish": "Először hevítsük fel az olajat, majd pirítsuk meg benne a hagymát aranysárgára.",
                        "english": "First heat up the oil, then sauté the onion in it to a golden yellow."
                    },
                    {
                        "spanish": "Miután a hús megpuhult, adjuk hozzá a tejfölt és a fűszerpaprikát.",
                        "english": "After the meat has softened, add the sour cream and paprika."
                    },
                    {
                        "spanish": "Végül szórjuk meg friss petrezselyemmel, és tálaljuk melegen nokedlivel.",
                        "english": "Finally, sprinkle with fresh parsley and serve hot with dumplings."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-12-03-gr.json", gr_03)

    gr_04 = {
        "id": "grammar.b1.12.04.culinary-tradition",
        "title": "Describing Cultural Food Traditions & Taste: ízvilág, hungarikum",
        "sections": [
            {
                "type": "text",
                "title": "Cultural Gastronomy and Characteristic Flavors",
                "content": "To characterize Hungarian cuisine, use flavor adjectives with *-ú / -ű*: *jellegzetes ízű* (distinctively flavored), *fűszeres* (spicy), *enyhe* (mild), *csípős* (hot/piquant), and appositive terms: *hagyományos hungarikumként* (as a traditional Hungarikum)."
            },
            {
                "type": "examples",
                "title": "Culinary tradition examples",
                "items": [
                    {
                        "spanish": "A magyar gasztronómia gazdag ízvilágát a fűszerpaprika, a hagyma és a tejföl határozza meg.",
                        "english": "The rich flavor profile of Hungarian gastronomy is defined by paprika, onion, and sour cream."
                    },
                    {
                        "spanish": "A gulyásleves és a kürtőskalács hivatalosan is elismert nemzeti hungarikum.",
                        "english": "Goulash soup and chimney cake are officially recognized national Hungarikums."
                    },
                    {
                        "spanish": "A vidéki falvakban a hagyományőrzés legfontosabb része a közös disznótor és sütés-főzés.",
                        "english": "In rural villages, the most vital part of preserving tradition is communal pig feast and cooking."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-12-04-gr.json", gr_04)

    gr_05 = {
        "id": "grammar.b1.12.05.restaurant-etiquette",
        "title": "Restaurant Etiquette & Polite Requests: Legyen szíves, kérhetnénk...",
        "sections": [
            {
                "type": "text",
                "title": "Ordering, Paying, and Tipping in Hungarian Restaurants",
                "content": "Dining out combines polite requests (*Legyen szíves...* = 'Could you please...', *Szeretnénk kérni egy...* = 'We would like to ask for a...'), requesting the bill (*A számlát kérnénk szépen* = 'We would like the bill, please'), and inquiring about service charges (*Benne van a számlában a szervizdíj?*)."
            },
            {
                "type": "examples",
                "title": "Restaurant dialogue examples",
                "items": [
                    {
                        "spanish": "Legyen szíves, hozna nekünk még egy kancsó szénsavmentes vizet?",
                        "english": "Could you please bring us another jug of still water?"
                    },
                    {
                        "spanish": "A számlát kérnénk szépen! Kártyával vagy készpénzzel fizethetünk?",
                        "english": "We'd like the bill, please! Can we pay with card or cash?"
                    },
                    {
                        "spanish": "A kitűnő kiszolgálásért tíz százalék borravalót adtunk a pincérnek.",
                        "english": "For the excellent service, we gave the waiter a ten percent tip."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-12-05-gr.json", gr_05)

    # -------------------------------------------------------------------------
    # 3. Classic Literature Story
    # -------------------------------------------------------------------------
    classic_story = {
        "id": "story.b1.12.classic",
        "title": "Szindbád és a vasárnapi ebéd",
        "level": "B1",
        "lesson": 5,
        "order": 5,
        "type": "classics",
        "estimatedMinutes": 7,
        "characters": [
            "Szindbád",
            "A vendéglős"
        ],
        "grammar": [
            "mediopassive-cooking",
            "recipe-sequencing",
            "restaurant-etiquette"
        ],
        "vocabularyTopics": [
            "food",
            "restaurant",
            "hungarian-cuisine",
            "soup"
        ],
        "summary": "In this adapted excerpt from Gyula Krúdy's world-famous Szindbád stories, the nostalgic traveler Szindbád savors the sacred ritual of Sunday lunch in a quiet old-world tavern, contemplating the steaming golden broth, marrow bones, and freshly grated horseradish.",
        "source": "Adaptation inspired by the public-domain work Szindbád by Gyula Krúdy",
        "paragraphs": [
            {"type": "narration", "text": "A kis óbudai kiskocsmában csend volt, csak az öreg falióra ketyegett békésen a kockás abroszos asztalok felett."},
            {"type": "narration", "text": "Szindbád a sarokba ült, ahol a délutáni őszi napfény megvilágította a kristálytiszta borospoharakat."},
            {"type": "dialogue", "speaker": "A vendéglős", "text": "Jó napot kívánok, nagyságos uram! Mit hozhatok ma ebédre a konyhából?"},
            {"type": "dialogue", "speaker": "Szindbád", "text": "Egy forró húslevest szeretnék kérni aranyló velős csonttal, friss pirítóssal és csípős fokhagymával."},
            {"type": "narration", "text": "Amikor a vendéglős kihozta a gőzölgő fazekat, Szindbád áhítattal nézte a sárga zsírkarikákat a leves felszínén."},
            {"type": "narration", "text": "Gondosan kiütötte a forró velőt a csontból a pirítósra, megsózta, és érezte, hogy az élet minden szépsége egyetlen tökéletes falatban összpontosul."}
        ]
    }
    write_json("content/hu/stories/classics/b1/b1-12-szindbad.json", classic_story)

    # -------------------------------------------------------------------------
    # 4. Exercise Files
    # -------------------------------------------------------------------------
    ex_01 = {
        "lesson": "b1-12-01",
        "exercises": [
            {
                "id": "b1-12-01-intro-1",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["hozzávaló", "ingredient"],
                    ["fűszer", "spice / seasoning"],
                    ["alapanyag", "raw staple ingredient"],
                    ["előkészítés", "preparation / prepping"]
                ]
            },
            {
                "id": "b1-12-01-intro-2",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["megsül", "bakes / roasts"],
                    ["megfő", "cooks / boils"],
                    ["megpuhul", "becomes soft / tender"],
                    ["elkészül", "gets done / finished"]
                ]
            },
            {
                "id": "b1-12-01-controlled-1",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik ige fejezi ki, hogy a hús puha lett a főzés során?",
                "options": ["megpuhul", "megsóz", "megszárad"],
                "correct": 0
            },
            {
                "id": "b1-12-01-controlled-2",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik igekötő illik az aprításra: „A fokhagymát finomra ______aprítjuk.”?",
                "options": ["fel", "le", "ki"],
                "correct": 0
            },
            {
                "id": "b1-12-01-controlled-3",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik mondat mutatja be helyesen a sütési folyamatot?",
                "options": [
                    "A sütemény húsz perc alatt szép aranybarnára sül a forró sütőben.",
                    "A sütemény húsz perc alatt aranybarnára süt a sütő.",
                    "A sütemény húsz perc alatt sütőnek megy."
                ],
                "correct": 0
            },
            {
                "id": "b1-12-01-controlled-4",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Mit jelent az 'alapanyag' szó a konyhaművészetben?",
                "options": ["The raw, foundational ingredient (e.g. flour, meat)", "The cookbook", "The kitchen knife"],
                "correct": 0
            },
            {
                "id": "b1-12-01-practice-1",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A finom pörkölthöz a legjobb minőségű marhahús a legfontosabb ____. (basic raw ingredient)",
                "answer": "alapanyag"
            },
            {
                "id": "b1-12-01-practice-2",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Lassú tűzön a zöldség húsz perc alatt teljesen meg____. (softens / tenderizes: puhul)",
                "answer": "puhul"
            },
            {
                "id": "b1-12-01-practice-3",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Mi a konyhai 'előkészítés' lényege?",
                "options": [
                    "A zöldségek megmosása, meghámozása, felaprítása és a hozzávalók kimérése a főzés előtt.",
                    "Az ételek elfogyasztása a vendégekkel.",
                    "A tányérok elmosása az ebéd után."
                ],
                "correct": 0
            },
            {
                "id": "b1-12-01-practice-4",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Melyek a leggyakoribb hagyományos magyar fűszerek?",
                "options": [
                    "A fűszerpaprika, a majoránna, a köménymag, a feketebors és a fokhagyma.",
                    "A curry és a wasabi.",
                    "Kizárólag a fehér kristálycukor."
                ],
                "correct": 0
            },
            {
                "id": "b1-12-01-dialogue-1",
                "type": "multiple-choice",
                "category": "reading",
                "question": "— Mindent megvettél a piacon a vacsorához?\n— Igen, az összes szükséges ______ a kosaramban van.",
                "options": ["hozzávaló", "defterdár", "rendezvény"],
                "correct": 0
            },
            {
                "id": "b1-12-01-dialogue-2",
                "type": "multiple-choice",
                "category": "reading",
                "question": "— Mikor ülhetünk le enni?\n— Amint a húsleves teljesen ______, már tálalom is.",
                "options": ["elkészül", "elnéptelenedik", "felújít"],
                "correct": 0
            },
            {
                "id": "b1-12-01-writing-1",
                "type": "fill-blank",
                "category": "production",
                "sentence": "A kalácstészta a meleg konyhában gyorsan meg____. (rises / kel)",
                "answer": "kel"
            },
            {
                "id": "b1-12-01-writing-2",
                "type": "fill-blank",
                "category": "production",
                "sentence": "A magyar ételek jellegzetes ízét a minőségi szegedi és kalocsai fűszer____ adja. (paprika)",
                "answer": "paprika"
            },
            {
                "id": "b1-12-01-check-1",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Mit jelent az 'előkészítés' szó?",
                "options": ["Preparation / prepping", "Eating", "Shopping"],
                "correct": 0
            },
            {
                "id": "b1-12-01-check-2",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik ige fejezi ki, hogy a kenyér elkészült a sütőben?",
                "options": ["megsül", "megfőz", "megiszik"],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-12-01-ex.json", ex_01)

    ex_02 = {
        "lesson": "b1-12-02",
        "exercises": [
            {
                "id": "b1-12-02-intro-1",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["táplálkozási szokás", "dietary habit"],
                    ["fogyókúra", "weight-loss diet"],
                    ["rost", "dietary fiber"],
                    ["vitaminbevitel", "vitamin intake"]
                ]
            },
            {
                "id": "b1-12-02-intro-2",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["rendszeresen", "regularly"],
                    ["naponta", "daily"],
                    ["időnként", "from time to time"],
                    ["ritkán", "rarely"]
                ]
            },
            {
                "id": "b1-12-02-controlled-1",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik határozószó fejezi ki az ismétlődő napi rutint?",
                "options": ["naponta", "tegnap", "mindjárt"],
                "correct": 0
            },
            {
                "id": "b1-12-02-controlled-2",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Hogyan mondjuk magyarul: 'before eating / before meals'?",
                "options": ["étkezés előtt", "étkezés után", "étkezés alatt"],
                "correct": 0
            },
            {
                "id": "b1-12-02-controlled-3",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Miért fontos a rostban gazdag táplálkozás?",
                "options": [
                    "Mert támogatja az emésztést és a kiegyensúlyozott bélflórát.",
                    "Mert azonnal elaltatja az embert.",
                    "Mert helyettesíti a vizet."
                ],
                "correct": 0
            },
            {
                "id": "b1-12-02-controlled-4",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik állítás felel meg a modern egészségtudatos életmódnak?",
                "options": [
                    "A túlzott cukor és zsiradék kerülése, valamint a bőséges zöldségfogyasztás.",
                    "Napi tíz liter energiaital fogyasztása.",
                    "Minden friss zöldség mellőzése."
                ],
                "correct": 0
            },
            {
                "id": "b1-12-02-practice-1",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A téli hónapokban citrusfélékkel és savanyú káposztával biztosítható a megfelelő ____. (vitamin intake)",
                "answer": "vitaminbevitel"
            },
            {
                "id": "b1-12-02-practice-2",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A teljes kiőrlésű gabonák sok értékes élelmi ____ tartalmaznak. (fiber - accusative: rostot)",
                "answer": "rostot"
            },
            {
                "id": "b1-12-02-practice-3",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Mit jelent a 'fogyókúra' kifejezés?",
                "options": [
                    "Tudatosan szabályozott étrend a testsúly csökkentése érdekében.",
                    "Egy gyorséttermi menüsor rendelése.",
                    "Az ételek elégetése a tűzhelyen."
                ],
                "correct": 0
            },
            {
                "id": "b1-12-02-practice-4",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Milyen tényezők befolyásolják egy ember táplálkozási szokásait?",
                "options": [
                    "A családi hagyományok, a kultúra, az életkor, a fizikai aktivitás és az egészségi állapot.",
                    "Csak a cipőméret.",
                    "Kizárólag a lakás fűtési rendszere."
                ],
                "correct": 0
            },
            {
                "id": "b1-12-02-dialogue-1",
                "type": "multiple-choice",
                "category": "reading",
                "question": "— Miért változtattál a táplálkozásodon?\n— Mert a régi ______ sok fáradtságot és emésztési panaszokat okoztak.",
                "options": ["szokásaim", "receptjeim", "pincéreim"],
                "correct": 0
            },
            {
                "id": "b1-12-02-dialogue-2",
                "type": "multiple-choice",
                "category": "reading",
                "question": "— Nem túl nehéz ez a szigorú ______?\n— Nem, ha sok zöldséget és elegendő fehérjét eszem mellette.",
                "options": ["fogyókúra", "infrastruktúra", "kancellária"],
                "correct": 0
            },
            {
                "id": "b1-12-02-writing-1",
                "type": "fill-blank",
                "category": "production",
                "sentence": "A dietetikus szerint érdemes naponta legalább két liter vizet inni ____. (regularly: rendszeresen)",
                "answer": "rendszeresen"
            },
            {
                "id": "b1-12-02-writing-2",
                "type": "fill-blank",
                "category": "production",
                "sentence": "A reggeli zabkása gazdag élelmi ____ forrása. (fiber: rost)",
                "answer": "rost"
            },
            {
                "id": "b1-12-02-check-1",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Mit jelent a 'táplálkozási szokás'?",
                "options": ["Eating pattern / dietary habit", "Sleeping habit", "Exercise routine"],
                "correct": 0
            },
            {
                "id": "b1-12-02-check-2",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Hogyan mondjuk: 'twice a day'?",
                "options": ["naponta kétszer", "naponta kettő", "napi kettőkor"],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-12-02-ex.json", ex_02)

    ex_03 = {
        "lesson": "b1-12-03",
        "exercises": [
            {
                "id": "b1-12-03-intro-1",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["recept", "recipe"],
                    ["elkészítési mód", "preparation method"],
                    ["sütési idő", "baking time"],
                    ["adag", "portion / serving"]
                ]
            },
            {
                "id": "b1-12-03-intro-2",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["először", "first / at first"],
                    ["majd", "then / next"],
                    ["miután", "after having"],
                    ["végül", "finally"]
                ]
            },
            {
                "id": "b1-12-03-controlled-1",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik időhatározó jelzi az első lépést egy receptben?",
                "options": ["Először", "Végül", "Soha"],
                "correct": 0
            },
            {
                "id": "b1-12-03-controlled-2",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Hogyan mondjuk: 'cooking / baking time'?",
                "options": ["sütési idő (főzési idő)", "sütőóra", "időjárás"],
                "correct": 0
            },
            {
                "id": "b1-12-03-controlled-3",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik mondat mutatja be a recept logikus lépéseit?",
                "options": [
                    "Először pirítsuk meg a hagymát, majd adjuk hozzá a húst, és miután megpuhult, ízesítsük fűszerekkel.",
                    "Végül tálaljuk a nyers ételt a sütés előtt.",
                    "Először mossuk el a tányérokat, mielőtt ételt vennénk."
                ],
                "correct": 0
            },
            {
                "id": "b1-12-03-controlled-4",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Mit jelent az 'adag' szó az étlapokon vagy receptekben?",
                "options": ["Egy személyre szabott ételmennyiség (portion / serving).", "Az étel ára.", "A szakács neve."],
                "correct": 0
            },
            {
                "id": "b1-12-03-practice-1",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A sütemény pontos ____ leírása lépésről lépésre megtalálható a szakácskönyvben. (recipe: recept)",
                "answer": "receptjének"
            },
            {
                "id": "b1-12-03-practice-2",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A pogácsa sütési ____ körülbelül huszonöt perc 180 fokos sütőben. (time: ideje)",
                "answer": "ideje"
            },
            {
                "id": "b1-12-03-practice-3",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Mit kell ellenőrizni a recept elolvasásakor a főzés megkezdése előtt?",
                "options": [
                    "Hogy minden hozzávaló rendelkezésre áll-e a szükséges mennyiségben.",
                    "Hogy hány oldalas a könyv borítója.",
                    "Hogy milyen színű a konyhabútor."
                ],
                "correct": 0
            },
            {
                "id": "b1-12-03-practice-4",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Hány adagra szólnak általában a családi receptek?",
                "options": ["Általában négy vagy hat személyre (adagra).", "Száz adagra.", "Fél adagra."],
                "correct": 0
            },
            {
                "id": "b1-12-03-dialogue-1",
                "type": "multiple-choice",
                "category": "reading",
                "question": "— Elkérhetem a híres almás pite ______?\n— Szívesen, leírom neked a hozzávalókat és a pontos elkészítési módot.",
                "options": ["receptjét", "számláját", "önkormányzatát"],
                "correct": 0
            },
            {
                "id": "b1-12-03-dialogue-2",
                "type": "multiple-choice",
                "category": "reading",
                "question": "— Hány ______ süssünk a pörköltből a vacsorára?\n— Legalább négy személyre elegendő mennyiséget készítsünk.",
                "options": ["adagot", "rostot", "pincért"],
                "correct": 0
            },
            {
                "id": "b1-12-03-writing-1",
                "type": "fill-blank",
                "category": "production",
                "sentence": "____ keverjük össze a lisztet a sütőporral, majd adjuk hozzá a vajat. (First: először)",
                "answer": "Először"
            },
            {
                "id": "b1-12-03-writing-2",
                "type": "fill-blank",
                "category": "production",
                "sentence": "Miután a mártás besűrűsödött, ____ szórjuk meg friss petrezselyemmel. (finally: végül)",
                "answer": "végül"
            },
            {
                "id": "b1-12-03-check-1",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Mit jelent az 'elkészítési mód'?",
                "options": ["Method of preparation", "Shopping list", "Restaurant menu"],
                "correct": 0
            },
            {
                "id": "b1-12-03-check-2",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik szó jelenti a tányérra mért ételmennyiséget?",
                "options": ["adag", "alapanyag", "fűszer"],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-12-03-ex.json", ex_03)

    ex_04 = {
        "lesson": "b1-12-04",
        "exercises": [
            {
                "id": "b1-12-04-intro-1",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["gasztronómia", "gastronomy"],
                    ["hungarikum", "Hungarikum (national value)"],
                    ["hagyományőrzés", "preservation of tradition"],
                    ["ízvilág", "flavor profile"]
                ]
            },
            {
                "id": "b1-12-04-intro-2",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["fűszeres", "spicy / seasoned"],
                    ["csípős", "hot / piquant"],
                    ["enyhe", "mild"],
                    ["zamatos", "flavorful / juicy"]
                ]
            },
            {
                "id": "b1-12-04-controlled-1",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Mi a 'hungarikum' hivatalos definíciója?",
                "options": [
                    "Olyan megkülönböztetésre méltó érték, amely a magyarságra jellemző csúcsteljesítményt képvisel.",
                    "Bármilyen külföldről behozott áru.",
                    "Egy műanyag konyhai eszköz."
                ],
                "correct": 0
            },
            {
                "id": "b1-12-04-controlled-2",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Hogyan jellemezzük a jellegzetes ízű ételeket?",
                "options": ["gazdag ízvilágú", "ízmentes", "íztelen"],
                "correct": 0
            },
            {
                "id": "b1-12-04-controlled-3",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Mely ételek számítanak hungarikumnak a gasztronómiában?",
                "options": [
                    "A gulyásleves, a csabai kolbász, a kalocsai fűszerpaprika és a karcagi birkapörkölt.",
                    "A pizza és a hamburger.",
                    "A sushi és a paella."
                ],
                "correct": 0
            },
            {
                "id": "b1-12-04-controlled-4",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Mit jelent a 'hagyományőrzés' a konyhában?",
                "options": [
                    "A generációkon át öröklődő receptek, alapanyagok és elkészítési technikák ápolását.",
                    "Minden régi recept elégetését.",
                    "Kizárólag konzerv ételek fogyasztását."
                ],
                "correct": 0
            },
            {
                "id": "b1-12-04-practice-1",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A kalocsai és szegedi fűszerpaprika elismert nemzeti ____. (Hungarikum)",
                "answer": "hungarikum"
            },
            {
                "id": "b1-12-04-practice-2",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A magyar konyha gazdag ____ világszerte nagy sikert arat a külföldiek körében. (flavor profile: ízvilága)",
                "answer": "ízvilága"
            },
            {
                "id": "b1-12-04-practice-3",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Melyik híres magyar desszert hungarikum, amelyet faszénparázson sütnek forgatva?",
                "options": ["A kürtőskalács.", "A somlói galuska.", "A túrógombóc."],
                "correct": 0
            },
            {
                "id": "b1-12-04-practice-4",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Melyik borvidékünk bora kapta a 'királyok bora, borok királya' elnevezést?",
                "options": ["Tokaji aszú.", "Egri bikavér.", "Villányi vörösbor."],
                "correct": 0
            },
            {
                "id": "b1-12-04-dialogue-1",
                "type": "multiple-choice",
                "category": "reading",
                "question": "— Kóstoltad már a valódi szegedi halászlét?\n— Igen, nagyon gazdag és testes az ______, csodálatosan harmonizál a ponty és a paprika.",
                "options": ["ízvilága", "ingázása", "kancelláriája"],
                "correct": 0
            },
            {
                "id": "b1-12-04-dialogue-2",
                "type": "multiple-choice",
                "category": "reading",
                "question": "— Miért fontos a magyar családoknak a karácsonyi bejgli sütése?\n— Mert ez a legszebb családi ______, minden generáció továbbadja a titkos receptet.",
                "options": ["hagyományőrzés", "összetartás", "zsoldoshiány"],
                "correct": 0
            },
            {
                "id": "b1-12-04-writing-1",
                "type": "fill-blank",
                "category": "production",
                "sentence": "A csabai és a gyulai kolbász világhírű magyar ____. (Hungarikum)",
                "answer": "hungarikum"
            },
            {
                "id": "b1-12-04-writing-2",
                "type": "fill-blank",
                "category": "production",
                "sentence": "A magyar ____ egyik legfontosabb alapja a jó minőségű sertészsír és a fűszerpaprika. (gastronomy: gasztronómiának)",
                "answer": "gasztronómiának"
            },
            {
                "id": "b1-12-04-check-1",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Mit jelent az 'ízvilág' szó?",
                "options": ["Flavor profile / taste spectrum", "Geography book", "Grocery store"],
                "correct": 0
            },
            {
                "id": "b1-12-04-check-2",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik szó jelenti a kiemelkedő magyar értéket?",
                "options": ["hungarikum", "húsleves", "hozzávaló"],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-12-04-ex.json", ex_04)

    ex_05 = {
        "lesson": "b1-12-05",
        "exercises": [
            {
                "id": "b1-12-05-intro-1",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["fogás", "course / dish in a meal"],
                    ["pincér", "waiter / server"],
                    ["borravaló", "tip / gratuity"],
                    ["számla", "bill / check"]
                ]
            },
            {
                "id": "b1-12-05-intro-2",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["legyen szíves", "could you please"],
                    ["szeretnénk kérni", "we would like to ask for"],
                    ["készpénzzel fizet", "pay in cash"],
                    ["kártyával fizet", "pay by card"]
                ]
            },
            {
                "id": "b1-12-05-controlled-1",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Hogyan kérjük el udvariasan a számlát a magyar étteremben?",
                "options": [
                    "„A számlát kérnénk szépen!”",
                    "„Add ide a pénzt!”",
                    "„Nem akarunk fizetni!”"
                ],
                "correct": 0
            },
            {
                "id": "b1-12-05-controlled-2",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Mit jelent a 'borravaló' szokása?",
                "options": [
                    "Önkéntes pénzbeli elismerés az udvarias és figyelmes kiszolgálásért (általában 10–15%).",
                    "A bor palackjának ára.",
                    "A pincér köténye."
                ],
                "correct": 0
            },
            {
                "id": "b1-12-05-controlled-3",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik udvarias formula illik a pincér megszólítására?",
                "options": [
                    "„Legyen szíves, hozna egy étlapot?”",
                    "„Hé, gyere ide azonnal!”",
                    "„Miért állsz ott?”"
                ],
                "correct": 0
            },
            {
                "id": "b1-12-05-controlled-4",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Hány fogásból áll egy klasszikus háromfogásos magyar vasárnapi ebéd?",
                "options": [
                    "Háromból: levesből (előétel), főételből és desszertből.",
                    "Egyetlen szelet kenyérből.",
                    "Húsz különböző italból."
                ],
                "correct": 0
            },
            {
                "id": "b1-12-05-practice-1",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A kitűnő vacsora és a figyelmes kiszolgálás után tíz százalék ____ adtunk a pincérnek. (tip: borravalót)",
                "answer": "borravalót"
            },
            {
                "id": "b1-12-05-practice-2",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Fő____ rántott csirkemellet rendeltünk petrezselymes burgonyával és uborkasalátával. (course - essive: fogásként)",
                "answer": "fogásként"
            },
            {
                "id": "b1-12-05-practice-3",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Mit kérdez a pincér a vacsora végén?",
                "options": [
                    "„Együtt vagy külön fizetnek? Készpénzzel vagy kártyával óhajtanak fizetni?”",
                    "„Mikor mennek haza gyalog?”",
                    "„Hány óra van a telefonjukon?”"
                ],
                "correct": 0
            },
            {
                "id": "b1-12-05-practice-4",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Mit jelent, ha a számla már tartalmazza a 'szervizdíjat'?",
                "options": [
                    "A kiszolgálás díja már benne van a végösszegben, így nem szükséges külön borravalót adni.",
                    "Az asztalt meg kell venni a vacsora után.",
                    "A konyhai gépek javítását a vendég fizeti."
                ],
                "correct": 0
            },
            {
                "id": "b1-12-05-dialogue-1",
                "type": "multiple-choice",
                "category": "reading",
                "question": "— Jó estét kívánok! Választottak már?\n— Igen, a ______ ajánlatából a harcsapaprikást szeretnénk kérni túrós csuszával.",
                "options": ["pincér", "főbérlő", "defterdár"],
                "correct": 0
            },
            {
                "id": "b1-12-05-dialogue-2",
                "type": "multiple-choice",
                "category": "reading",
                "question": "— Hozhatom a kávét a desszerthez?\n— Igen, köszönjük, és utána a ______ is kérnénk szépen.",
                "options": ["számlát", "fogyókúrát", "vilajetet"],
                "correct": 0
            },
            {
                "id": "b1-12-05-writing-1",
                "type": "fill-blank",
                "category": "production",
                "sentence": "Legyen ____, hozna még két pohár ásványvizet? (polite request: szíves)",
                "answer": "szíves"
            },
            {
                "id": "b1-12-05-writing-2",
                "type": "fill-blank",
                "category": "production",
                "sentence": "A vacsora végén a pincér kihozta az elszámoló ____. (bill: számlát)",
                "answer": "számlát"
            },
            {
                "id": "b1-12-05-reading-1",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Hol játszódik a Krúdy Gyula-részlet (Szindbád)?",
                "options": [
                    "Egy békés, ódon óbudai kiskocsmában a vasárnapi ebéd idején.",
                    "Egy tengerparti kikötőben.",
                    "A bécsi császári operaházban."
                ],
                "correct": 0
            },
            {
                "id": "b1-12-05-reading-2",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Mit rendelt Szindbád a vendéglőstől a kiskocsmában?",
                "options": [
                    "Forró húslevest aranyló velős csonttal, pirítóssal és fokhagymával.",
                    "Hideg tejet és száraz kenyeret.",
                    "Sült halat krumplival."
                ],
                "correct": 0
            },
            {
                "id": "b1-12-05-reading-3",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Milyen életérzést fejez ki Szindbád gasztronómiai élvezete Krúdynál?",
                "options": [
                    "Hogy az élet minden költészete és szépsége egyetlen tökéletesen megfőzött falatban és pillanatban összpontosul.",
                    "Hogy a sietség és a gyorsétkezés a legfontosabb.",
                    "Hogy a vendéglőkbe csak felesleges pénzkidobás járni."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-12-05-ex.json", ex_05)

    ex_consolidation = {
        "lesson": "b1-12-consolidation",
        "exercises": [
            {
                "id": "b1-12-consolidation-1",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["hozzávaló", "ingredient"],
                    ["alapanyag", "staple ingredient"],
                    ["fűszer", "spice / seasoning"],
                    ["előkészítés", "preparation"]
                ]
            },
            {
                "id": "b1-12-consolidation-2",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["recept", "recipe"],
                    ["elkészítési mód", "method of preparation"],
                    ["sütési idő", "baking time"],
                    ["adag", "portion / serving"]
                ]
            },
            {
                "id": "b1-12-consolidation-3",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["gasztronómia", "gastronomy"],
                    ["hungarikum", "Hungarikum"],
                    ["fogás", "course / dish"],
                    ["borravaló", "tip / gratuity"]
                ]
            },
            {
                "id": "b1-12-consolidation-4",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik mediopasszív ige fejezi ki, hogy a hús jól megpuhult a főzésben?",
                "options": ["megpuhul", "megkeményedik", "megszárad"],
                "correct": 0
            },
            {
                "id": "b1-12-consolidation-5",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik időhatározó köti össze az egymást követő lépéseket: „Először pirítsuk meg a hagymát, ______ adjuk hozzá a húst.”?",
                "options": ["majd", "soha", "alatt"],
                "correct": 0
            },
            {
                "id": "b1-12-consolidation-6",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Hogyan kérjük el a számlát a legudvariasabban?",
                "options": [
                    "A számlát kérnénk szépen!",
                    "Fizetni kell azonnal!",
                    "Nem kérek számlát!"
                ],
                "correct": 0
            },
            {
                "id": "b1-12-consolidation-7",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A tészta a sütőben szép pirosra ____. (bakes: sül)",
                "answer": "sül"
            },
            {
                "id": "b1-12-consolidation-8",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A magyar konyha gazdag fűszerezésű ____ világszerte ismert. (flavor profile: ízvilága)",
                "answer": "ízvilága"
            },
            {
                "id": "b1-12-consolidation-9",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Legyen ____, hozna még két tiszta poharat az asztalhoz? (polite request: szíves)",
                "answer": "szíves"
            },
            {
                "id": "b1-12-consolidation-10",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Melyik író örökítette meg a magyar vendéglők hangulatát és a húsleves velős csonttal való rituáléját?",
                "options": [
                    "Krúdy Gyula a Szindbád-történetekben.",
                    "Gárdonyi Géza az Egri csillagokban.",
                    "Karinthy Frigyes a Tanár úr kéremben."
                ],
                "correct": 0
            },
            {
                "id": "b1-12-consolidation-11",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Milyen hagyományos magyar ételek ismertek hungarikumként?",
                "options": [
                    "A gulyásleves, a csabai kolbász, a kürtőskalács és a bajai halászlé.",
                    "A bécsi szelet és a spagetti.",
                    "A hot dog és a sült krumpli."
                ],
                "correct": 0
            },
            {
                "id": "b1-12-consolidation-12",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Mit fejez ki a vendéglátásban a borravaló adása?",
                "options": [
                    "A figyelmes, udvarias felszolgálásért nyújtott önkéntes elismerést.",
                    "Egy kötelező állami adófajtát.",
                    "A rossz kiszolgálás miatti panaszt."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-12-consolidation-ex.json", ex_consolidation)

    # -------------------------------------------------------------------------
    # 5. Lesson Files (6 lessons)
    # -------------------------------------------------------------------------
    lesson_01 = {
        "id": "lesson.b1.12-01",
        "unit": 12,
        "title": "How a Dish Gets Made",
        "level": "B1",
        "grammar": "Mediopassive & Inchoative Verbs in Cooking: -ódik / -ődik, -ul / -ül",
        "goal": [
            "I can describe cooking and baking processes using mediopassive verbs (megfő, megsül, megpuhul).",
            "I can use food preparation prefixes (felaprít, összekever, átpasszíroz).",
            "I can discuss fresh ingredients, spices, and kitchen preparation stages.",
            "I can use four new vocabulary items related to culinary ingredients and seasoning."
        ],
        "sections": [
            {
                "type": "goal",
                "title": "Lesson Goals",
                "items": [
                    "I can describe cooking and baking processes using mediopassive verbs (megfő, megsül, megpuhul).",
                    "I can use food preparation prefixes (felaprít, összekever, átpasszíroz).",
                    "I can discuss fresh ingredients, spices, and kitchen preparation stages.",
                    "I can use four new vocabulary items related to culinary ingredients and seasoning."
                ]
            },
            {"type": "recycle", "title": "Quick Review"},
            {"type": "grammar", "ref": "grammar/b1/b1-12-01-a-gr.json"},
            {"type": "grammar", "ref": "grammar/b1/b1-12-01-b-gr.json"},
            {"type": "vocabulary", "title": "Lesson Vocabulary", "ref": "vocabulary/b1/b1-12-01-voc.json"},
            {"type": "exercise-group", "title": "Introduce", "ref": "exercises/b1/b1-12-01-ex.json", "exerciseRefs": ["b1-12-01-intro-1", "b1-12-01-intro-2"]},
            {"type": "exercise-group", "title": "Controlled", "ref": "exercises/b1/b1-12-01-ex.json", "exerciseRefs": ["b1-12-01-controlled-1", "b1-12-01-controlled-2", "b1-12-01-controlled-3", "b1-12-01-controlled-4"]},
            {"type": "exercise-group", "title": "Practice", "ref": "exercises/b1/b1-12-01-ex.json", "exerciseRefs": ["b1-12-01-practice-1", "b1-12-01-practice-2", "b1-12-01-practice-3", "b1-12-01-practice-4"]},
            {"type": "exercise-group", "title": "Dialogue", "ref": "exercises/b1/b1-12-01-ex.json", "exerciseRefs": ["b1-12-01-dialogue-1", "b1-12-01-dialogue-2"]},
            {"type": "exercise-group", "title": "Production", "ref": "exercises/b1/b1-12-01-ex.json", "exerciseRefs": ["b1-12-01-writing-1", "b1-12-01-writing-2"]},
            {"type": "srs", "title": "Add to Review"},
            {"type": "exercise-group", "title": "Check", "ref": "exercises/b1/b1-12-01-ex.json", "exerciseRefs": ["b1-12-01-check-1", "b1-12-01-check-2"]},
            {
                "type": "checklist",
                "title": "Can you do this?",
                "items": [
                    "I can describe cooking and baking processes using mediopassive verbs (megfő, megsül, megpuhul).",
                    "I can use food preparation prefixes (felaprít, összekever, átpasszíroz).",
                    "I can discuss fresh ingredients, spices, and kitchen preparation stages.",
                    "I can use four new vocabulary items related to culinary ingredients and seasoning."
                ]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-12-01.json", lesson_01)

    lesson_02 = {
        "id": "lesson.b1.12-02",
        "unit": 12,
        "title": "Eating Habits & Nutrition",
        "level": "B1",
        "grammar": "Habitual Expressions & Frequency Adverbs: rendszeresen, naponta, időnként",
        "goal": [
            "I can discuss dietary habits, healthy choices, and weight-loss routines.",
            "I can describe frequency and regular lifestyle habits in natural Hungarian.",
            "I can explain the benefits of dietary fiber, vitamins, and fresh nutrition.",
            "I can use four new vocabulary items related to health and dietary habits."
        ],
        "sections": [
            {
                "type": "goal",
                "title": "Lesson Goals",
                "items": [
                    "I can discuss dietary habits, healthy choices, and weight-loss routines.",
                    "I can describe frequency and regular lifestyle habits in natural Hungarian.",
                    "I can explain the benefits of dietary fiber, vitamins, and fresh nutrition.",
                    "I can use four new vocabulary items related to health and dietary habits."
                ]
            },
            {"type": "recycle", "title": "Quick Review"},
            {"type": "grammar", "ref": "grammar/b1/b1-12-02-gr.json"},
            {"type": "vocabulary", "title": "Lesson Vocabulary", "ref": "vocabulary/b1/b1-12-02-voc.json"},
            {"type": "exercise-group", "title": "Introduce", "ref": "exercises/b1/b1-12-02-ex.json", "exerciseRefs": ["b1-12-02-intro-1", "b1-12-02-intro-2"]},
            {"type": "exercise-group", "title": "Controlled", "ref": "exercises/b1/b1-12-02-ex.json", "exerciseRefs": ["b1-12-02-controlled-1", "b1-12-02-controlled-2", "b1-12-02-controlled-3", "b1-12-02-controlled-4"]},
            {"type": "exercise-group", "title": "Practice", "ref": "exercises/b1/b1-12-02-ex.json", "exerciseRefs": ["b1-12-02-practice-1", "b1-12-02-practice-2", "b1-12-02-practice-3", "b1-12-02-practice-4"]},
            {"type": "exercise-group", "title": "Dialogue", "ref": "exercises/b1/b1-12-02-ex.json", "exerciseRefs": ["b1-12-02-dialogue-1", "b1-12-02-dialogue-2"]},
            {"type": "exercise-group", "title": "Production", "ref": "exercises/b1/b1-12-02-ex.json", "exerciseRefs": ["b1-12-02-writing-1", "b1-12-02-writing-2"]},
            {"type": "srs", "title": "Add to Review"},
            {"type": "exercise-group", "title": "Check", "ref": "exercises/b1/b1-12-02-ex.json", "exerciseRefs": ["b1-12-02-check-1", "b1-12-02-check-2"]},
            {
                "type": "checklist",
                "title": "Can you do this?",
                "items": [
                    "I can discuss dietary habits, healthy choices, and weight-loss routines.",
                    "I can describe frequency and regular lifestyle habits in natural Hungarian.",
                    "I can explain the benefits of dietary fiber, vitamins, and fresh nutrition.",
                    "I can use four new vocabulary items related to health and dietary habits."
                ]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-12-02.json", lesson_02)

    lesson_03 = {
        "id": "lesson.b1.12-03",
        "unit": 12,
        "title": "A Recipe, Step by Step",
        "level": "B1",
        "grammar": "Recipe Sequence Connectors: először, majd, miután, végül",
        "goal": [
            "I can understand and follow recipes step by step in Hungarian.",
            "I can sequence instructions clearly using először, majd, and végül.",
            "I can specify baking times, temperatures, and portion sizes.",
            "I can use four new vocabulary items related to cooking instructions and servings."
        ],
        "sections": [
            {
                "type": "goal",
                "title": "Lesson Goals",
                "items": [
                    "I can understand and follow recipes step by step in Hungarian.",
                    "I can sequence instructions clearly using először, majd, and végül.",
                    "I can specify baking times, temperatures, and portion sizes.",
                    "I can use four new vocabulary items related to cooking instructions and servings."
                ]
            },
            {"type": "recycle", "title": "Quick Review"},
            {"type": "grammar", "ref": "grammar/b1/b1-12-03-gr.json"},
            {"type": "vocabulary", "title": "Lesson Vocabulary", "ref": "vocabulary/b1/b1-12-03-voc.json"},
            {"type": "exercise-group", "title": "Introduce", "ref": "exercises/b1/b1-12-03-ex.json", "exerciseRefs": ["b1-12-03-intro-1", "b1-12-03-intro-2"]},
            {"type": "exercise-group", "title": "Controlled", "ref": "exercises/b1/b1-12-03-ex.json", "exerciseRefs": ["b1-12-03-controlled-1", "b1-12-03-controlled-2", "b1-12-03-controlled-3", "b1-12-03-controlled-4"]},
            {"type": "exercise-group", "title": "Practice", "ref": "exercises/b1/b1-12-03-ex.json", "exerciseRefs": ["b1-12-03-practice-1", "b1-12-03-practice-2", "b1-12-03-practice-3", "b1-12-03-practice-4"]},
            {"type": "exercise-group", "title": "Dialogue", "ref": "exercises/b1/b1-12-03-ex.json", "exerciseRefs": ["b1-12-03-dialogue-1", "b1-12-03-dialogue-2"]},
            {"type": "exercise-group", "title": "Production", "ref": "exercises/b1/b1-12-03-ex.json", "exerciseRefs": ["b1-12-03-writing-1", "b1-12-03-writing-2"]},
            {"type": "srs", "title": "Add to Review"},
            {"type": "exercise-group", "title": "Check", "ref": "exercises/b1/b1-12-03-ex.json", "exerciseRefs": ["b1-12-03-check-1", "b1-12-03-check-2"]},
            {
                "type": "checklist",
                "title": "Can you do this?",
                "items": [
                    "I can understand and follow recipes step by step in Hungarian.",
                    "I can sequence instructions clearly using először, majd, and végül.",
                    "I can specify baking times, temperatures, and portion sizes.",
                    "I can use four new vocabulary items related to cooking instructions and servings."
                ]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-12-03.json", lesson_03)

    lesson_04 = {
        "id": "lesson.b1.12-04",
        "unit": 12,
        "title": "Food & Identity",
        "level": "B1",
        "grammar": "Flavor Profiles & National Values: ízvilág, hungarikum",
        "goal": [
            "I can discuss traditional Hungarian culinary heritage and Hungarikums.",
            "I can characterize flavor profiles using specialized adjectives (fűszeres, csípős, zamatos).",
            "I can explain how food connects to family traditions and national identity.",
            "I can use four new vocabulary items related to gastronomy and national treasures."
        ],
        "sections": [
            {
                "type": "goal",
                "title": "Lesson Goals",
                "items": [
                    "I can discuss traditional Hungarian culinary heritage and Hungarikums.",
                    "I can characterize flavor profiles using specialized adjectives (fűszeres, csípős, zamatos).",
                    "I can explain how food connects to family traditions and national identity.",
                    "I can use four new vocabulary items related to gastronomy and national treasures."
                ]
            },
            {"type": "recycle", "title": "Quick Review"},
            {"type": "grammar", "ref": "grammar/b1/b1-12-04-gr.json"},
            {"type": "vocabulary", "title": "Lesson Vocabulary", "ref": "vocabulary/b1/b1-12-04-voc.json"},
            {"type": "exercise-group", "title": "Introduce", "ref": "exercises/b1/b1-12-04-ex.json", "exerciseRefs": ["b1-12-04-intro-1", "b1-12-04-intro-2"]},
            {"type": "exercise-group", "title": "Controlled", "ref": "exercises/b1/b1-12-04-ex.json", "exerciseRefs": ["b1-12-04-controlled-1", "b1-12-04-controlled-2", "b1-12-04-controlled-3", "b1-12-04-controlled-4"]},
            {"type": "exercise-group", "title": "Practice", "ref": "exercises/b1/b1-12-04-ex.json", "exerciseRefs": ["b1-12-04-practice-1", "b1-12-04-practice-2", "b1-12-04-practice-3", "b1-12-04-practice-4"]},
            {"type": "exercise-group", "title": "Dialogue", "ref": "exercises/b1/b1-12-04-ex.json", "exerciseRefs": ["b1-12-04-dialogue-1", "b1-12-04-dialogue-2"]},
            {"type": "exercise-group", "title": "Production", "ref": "exercises/b1/b1-12-04-ex.json", "exerciseRefs": ["b1-12-04-writing-1", "b1-12-04-writing-2"]},
            {"type": "srs", "title": "Add to Review"},
            {"type": "exercise-group", "title": "Check", "ref": "exercises/b1/b1-12-04-ex.json", "exerciseRefs": ["b1-12-04-check-1", "b1-12-04-check-2"]},
            {
                "type": "checklist",
                "title": "Can you do this?",
                "items": [
                    "I can discuss traditional Hungarian culinary heritage and Hungarikums.",
                    "I can characterize flavor profiles using specialized adjectives (fűszeres, csípős, zamatos).",
                    "I can explain how food connects to family traditions and national identity.",
                    "I can use four new vocabulary items related to gastronomy and national treasures."
                ]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-12-04.json", lesson_04)

    lesson_05 = {
        "id": "lesson.b1.12-05",
        "unit": 12,
        "title": "Describing a Meal Out",
        "level": "B1",
        "grammar": "Dining Requests & Restaurant Etiquette: Legyen szíves, kérhetnénk...",
        "goal": [
            "I can interact politely with restaurant staff, order multi-course meals, and request the bill.",
            "I can navigate tipping (borravaló), payment methods, and service charge etiquette.",
            "I can use four new vocabulary items related to dining out and restaurant service.",
            "I can read and understand an adapted literary excerpt from Gyula Krúdy's Szindbád."
        ],
        "sections": [
            {
                "type": "goal",
                "title": "Lesson Goals",
                "items": [
                    "I can interact politely with restaurant staff, order multi-course meals, and request the bill.",
                    "I can navigate tipping (borravaló), payment methods, and service charge etiquette.",
                    "I can use four new vocabulary items related to dining out and restaurant service.",
                    "I can read and understand an adapted literary excerpt from Gyula Krúdy's Szindbád."
                ]
            },
            {"type": "recycle", "title": "Quick Review"},
            {"type": "grammar", "ref": "grammar/b1/b1-12-05-gr.json"},
            {"type": "vocabulary", "title": "Lesson Vocabulary", "ref": "vocabulary/b1/b1-12-05-voc.json"},
            {"type": "exercise-group", "title": "Introduce", "ref": "exercises/b1/b1-12-05-ex.json", "exerciseRefs": ["b1-12-05-intro-1", "b1-12-05-intro-2"]},
            {"type": "exercise-group", "title": "Controlled", "ref": "exercises/b1/b1-12-05-ex.json", "exerciseRefs": ["b1-12-05-controlled-1", "b1-12-05-controlled-2", "b1-12-05-controlled-3", "b1-12-05-controlled-4"]},
            {"type": "exercise-group", "title": "Practice", "ref": "exercises/b1/b1-12-05-ex.json", "exerciseRefs": ["b1-12-05-practice-1", "b1-12-05-practice-2", "b1-12-05-practice-3", "b1-12-05-practice-4"]},
            {"type": "exercise-group", "title": "Dialogue", "ref": "exercises/b1/b1-12-05-ex.json", "exerciseRefs": ["b1-12-05-dialogue-1", "b1-12-05-dialogue-2"]},
            {"type": "exercise-group", "title": "Production", "ref": "exercises/b1/b1-12-05-ex.json", "exerciseRefs": ["b1-12-05-writing-1", "b1-12-05-writing-2"]},
            {"type": "srs", "title": "Add to Review"},
            {
                "type": "story",
                "title": "Reading: Szindbád és a vasárnapi ebéd",
                "ref": "stories/classics/b1/b1-12-szindbad.json"
            },
            {"type": "exercise-group", "title": "Reading", "ref": "exercises/b1/b1-12-05-ex.json", "exerciseRefs": ["b1-12-05-reading-1", "b1-12-05-reading-2", "b1-12-05-reading-3"]},
            {
                "type": "checklist",
                "title": "Can you do this?",
                "items": [
                    "I can interact politely with restaurant staff, order multi-course meals, and request the bill.",
                    "I can navigate tipping (borravaló), payment methods, and service charge etiquette.",
                    "I can use four new vocabulary items related to dining out and restaurant service.",
                    "I can read and understand an adapted literary excerpt from Gyula Krúdy's Szindbád."
                ]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-12-05.json", lesson_05)

    lesson_consolidation = {
        "id": "lesson.b1.12-consolidation",
        "unit": 12,
        "title": "Unit 12 Consolidation",
        "level": "B1",
        "sections": [
            {
                "type": "goal",
                "title": "Consolidation Goals",
                "items": [
                    "I can describe food cooking processes using mediopassive verbs.",
                    "I can follow and write step-by-step recipes with sequential connectors.",
                    "I can discuss dietary habits, Hungarikums, and flavor profiles.",
                    "I can order and pay comfortably in Hungarian restaurants."
                ]
            },
            {"type": "recycle", "title": "Quick Review"},
            {"type": "exercise-group", "title": "Recognize", "ref": "exercises/b1/b1-12-consolidation-ex.json", "exerciseRefs": ["b1-12-consolidation-1", "b1-12-consolidation-2", "b1-12-consolidation-3"]},
            {"type": "exercise-group", "title": "Recall", "ref": "exercises/b1/b1-12-consolidation-ex.json", "exerciseRefs": ["b1-12-consolidation-4", "b1-12-consolidation-5", "b1-12-consolidation-6"]},
            {"type": "exercise-group", "title": "In Context", "ref": "exercises/b1/b1-12-consolidation-ex.json", "exerciseRefs": ["b1-12-consolidation-7", "b1-12-consolidation-8", "b1-12-consolidation-9"]},
            {"type": "exercise-group", "title": "Produce", "ref": "exercises/b1/b1-12-consolidation-ex.json", "exerciseRefs": ["b1-12-consolidation-10", "b1-12-consolidation-11", "b1-12-consolidation-12"]},
            {
                "type": "checklist",
                "title": "Can you do this?",
                "items": [
                    "I can describe food cooking processes using mediopassive verbs.",
                    "I can follow and write step-by-step recipes with sequential connectors.",
                    "I can discuss dietary habits, Hungarikums, and flavor profiles.",
                    "I can order and pay comfortably in Hungarian restaurants."
                ]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-12-consolidation.json", lesson_consolidation)

if __name__ == "__main__":
    build_unit_12_core()
    print("Successfully built Hungarian B1 Core Unit 12!")
