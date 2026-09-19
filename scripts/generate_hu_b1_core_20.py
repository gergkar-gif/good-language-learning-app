#!/usr/bin/env python3
"""Generate Hungarian B1 Core Unit 20: Problems & Solutions (b1-20)."""

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

def build_unit_20_core():
    # -------------------------------------------------------------------------
    # 1. Vocabulary Files (4 words each = 20 words total)
    # -------------------------------------------------------------------------
    voc_01 = {
        "id": "vocab.b1.20.01",
        "lesson": "b1-20-01",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "hiba", "translation": "mistake, error", "pos": "noun"},
            {"lemma": "következmény", "translation": "consequence, aftermath", "pos": "noun"},
            {"lemma": "megbánás", "translation": "regret, remorse", "pos": "noun"},
            {"lemma": "váratlan fordulat", "translation": "unexpected turn of events", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-20-01-voc.json", voc_01)

    voc_02 = {
        "id": "vocab.b1.20.02",
        "lesson": "b1-20-02",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "mulasztás", "translation": "omission, lapse, negligence", "pos": "noun"},
            {"lemma": "felelősségvállalás", "translation": "taking responsibility", "pos": "noun"},
            {"lemma": "megelőzés", "translation": "prevention, precautionary measure", "pos": "noun"},
            {"lemma": "helyrehozatal", "translation": "rectification, making amends", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-20-02-voc.json", voc_02)

    voc_03 = {
        "id": "vocab.b1.20.03",
        "lesson": "b1-20-03",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "nehézség", "translation": "difficulty, hardship", "pos": "noun"},
            {"lemma": "akadály", "translation": "obstacle, barrier", "pos": "noun"},
            {"lemma": "kiút", "translation": "way out, escape route, solution", "pos": "noun"},
            {"lemma": "megoldás", "translation": "solution, resolution", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-20-03-voc.json", voc_03)

    voc_04 = {
        "id": "vocab.b1.20.04",
        "lesson": "b1-20-04",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "tapasztalat", "translation": "experience, practical knowledge", "pos": "noun"},
            {"lemma": "tanulság", "translation": "lesson learned, moral", "pos": "noun"},
            {"lemma": "hozzáállás", "translation": "attitude, approach, mindset", "pos": "noun"},
            {"lemma": "önkritika", "translation": "self-criticism, honest reflection", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-20-04-voc.json", voc_04)

    voc_05 = {
        "id": "vocab.b1.20.05",
        "lesson": "b1-20-05",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "javaslat", "translation": "proposal, suggestion", "pos": "noun"},
            {"lemma": "alternatíva", "translation": "alternative, viable option", "pos": "noun"},
            {"lemma": "megvalósítás", "translation": "implementation, execution", "pos": "noun"},
            {"lemma": "eredményesség", "translation": "effectiveness, efficacy", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-20-05-voc.json", voc_05)

    # -------------------------------------------------------------------------
    # 2. Grammar Files
    # -------------------------------------------------------------------------
    gr_01_a = {
        "id": "grammar.b1.20.01.past-conditional-volna",
        "title": "The Past Conditional: ha + past tense + volna ('if I had done...')",
        "sections": [
            {
                "type": "text",
                "title": "Forming Counterfactuals in the Past",
                "content": "To express what would have happened if past circumstances had been different, Hungarian uses the past tense followed by the auxiliary *volna*: *Ha tudtam volna, elmentem volna.* ('If I had known, I would have gone.'). Both the condition clause and the result clause use *múlt idő + volna*."
            },
            {
                "type": "examples",
                "title": "Past conditional examples",
                "items": [
                    {
                        "spanish": "Ha időben szóltál volna, elkerültük volna ezt a hibát.",
                        "english": "If you had spoken in time, we would have avoided this mistake."
                    },
                    {
                        "spanish": "Nem történt volna baj, ha körültekintőbbek lettünk volna.",
                        "english": "No harm would have happened if we had been more cautious."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-20-01-a-gr.json", gr_01_a)

    gr_01_b = {
        "id": "grammar.b1.20.01.regret-barcsak",
        "title": "Expressing Regret: bárcsak + past conditional",
        "sections": [
            {
                "type": "text",
                "title": "Wishes About the Past",
                "content": "*Bárcsak* ('if only') with past tense + *volna* expresses strong regret about an unchangeable past event: *Bárcsak jobban figyeltem volna!* ('If only I had paid better attention!')."
            },
            {
                "type": "examples",
                "title": "Sentences expressing regret",
                "items": [
                    {
                        "spanish": "Bárcsak ne követtem volna el ezt a súlyos mulasztást!",
                        "english": "If only I hadn't committed this grave omission!"
                    },
                    {
                        "spanish": "Kár, hogy nem hallgattunk a szakértő tanácsára.",
                        "english": "It is a pity that we did not listen to the expert's advice."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-20-01-b-gr.json", gr_01_b)

    gr_02_a = {
        "id": "grammar.b1.20.02.past-obligation-kellett-volna",
        "title": "Unfulfilled Past Obligation: kellett volna + infinitive ('should have')",
        "sections": [
            {
                "type": "text",
                "title": "Expressing What Should Have Been Done",
                "content": "*Kellett volna* followed by an infinitive expresses an action that ought to have been done in the past, but was omitted: *Meg kellett volna kérdeznem.* ('I should have asked.'). When the subject is explicit, the infinitive takes inflected endings: *Időben el kellett volna indulnotok.* ('You [pl.] should have left on time.')."
            },
            {
                "type": "examples",
                "title": "Unfulfilled obligation phrases",
                "items": [
                    {
                        "spanish": "Sokkal hamarabb észre kellett volna vennünk a problémát.",
                        "english": "We should have noticed the problem much sooner."
                    },
                    {
                        "spanish": "Nem lett volna szabad egyedül hagyni őt a nehéz helyzetben.",
                        "english": "One shouldn't have left him alone in that difficult situation."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-20-02-a-gr.json", gr_02_a)

    gr_02_b = {
        "id": "grammar.b1.20.02.past-advisability",
        "title": "Retrospective Advice: jobb lett volna, ha... ('it would have been better if')",
        "sections": [
            {
                "type": "text",
                "title": "Evaluating Better Past Choices",
                "content": "To evaluate choices retrospectively: *Jobb lett volna, ha azonnal szólunk.* ('It would have been better if we had said something immediately.'). *Érdemes lett volna megfontolni...* ('It would have been worth considering...')."
            },
            {
                "type": "examples",
                "title": "Retrospective advice examples",
                "items": [
                    {
                        "spanish": "Jobb lett volna, ha megbeszéljük a részleteket a szerződéskötés előtt.",
                        "english": "It would have been better if we had discussed the details before signing the contract."
                    },
                    {
                        "spanish": "Érdemes lett volna kikérni egy második véleményt is.",
                        "english": "It would have been worthwhile to ask for a second opinion as well."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-20-02-b-gr.json", gr_02_b)

    gr_03_a = {
        "id": "grammar.b1.20.03.overcoming-obstacles",
        "title": "Overcoming Obstacles: sikerült vs nem tudott in Complex Sentences",
        "sections": [
            {
                "type": "text",
                "title": "Narrating Successes and Obstacles",
                "content": "*Sikerült* + infinitive indicates achieving a solution despite difficulty: *Végül sikerült megoldást találnunk.* ('Finally we succeeded in finding a solution.'). Contrast with *nem tudtuk elkerülni* ('we could not avoid')."
            },
            {
                "type": "examples",
                "title": "Obstacle resolution phrases",
                "items": [
                    {
                        "spanish": "A nehézségek ellenére sikerült időben befejezni a munkát.",
                        "english": "Despite the difficulties, we succeeded in finishing the work on time."
                    },
                    {
                        "spanish": "Bár sok akadály merült fel, megtaláltuk a kiutat a válságból.",
                        "english": "Although many obstacles arose, we found the way out of the crisis."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-20-03-a-gr.json", gr_03_a)

    gr_03_b = {
        "id": "grammar.b1.20.03.preverbal-problem-solving",
        "title": "Verbs of Resolution: megold, leküzd, helyrehoz, elhárít",
        "sections": [
            {
                "type": "text",
                "title": "Preverbs in Problem Solving",
                "content": "Specific prefixed verbs denote active problem solving: *leküzdi az akadályokat* ('overcomes the obstacles'), *elhárítja a veszélyt* ('averts the danger'), *helyrehozza a hibát* ('rights the wrong / corrects the mistake')."
            },
            {
                "type": "examples",
                "title": "Resolution verbs in use",
                "items": [
                    {
                        "spanish": "A szakemberek gyorsan elhárították a technikai hibát.",
                        "english": "The specialists quickly averted the technical glitch."
                    },
                    {
                        "spanish": "Mindent megtettünk azért, hogy helyrehozzuk az elkövetett tévedést.",
                        "english": "We did everything in order to rectify the committed error."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-20-03-b-gr.json", gr_03_b)

    gr_04_a = {
        "id": "grammar.b1.20.04.retrospective-reflection",
        "title": "Reflective Formulations: utólag kiderült, hogy..., abból kiindulva",
        "sections": [
            {
                "type": "text",
                "title": "Analyzing Past Experiences",
                "content": "Formulas for reflecting on lessons learned: *Utólag kiderült, hogy...* ('In hindsight it turned out that...'), *Abból a tapasztalatból kiindulva...* ('Starting from that experience...'), *A tanulság az, hogy...* ('The lesson is that...')."
            },
            {
                "type": "examples",
                "title": "Reflective structures",
                "items": [
                    {
                        "spanish": "Utólag kiderült, hogy a kezdeti kudarc valójában hasznos tanulság volt.",
                        "english": "In hindsight it turned out that the initial failure was actually a useful lesson."
                    },
                    {
                        "spanish": "Az esetből azt a tanulságot vontuk le, hogy az őszinteség a legfontosabb.",
                        "english": "From the incident we drew the lesson that honesty is paramount."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-20-04-a-gr.json", gr_04_a)

    gr_04_b = {
        "id": "grammar.b1.20.04.mindset-collocations",
        "title": "Attitude & Growth: pozitív hozzáállás, tanul a hibáiból",
        "sections": [
            {
                "type": "text",
                "title": "Collocations for Resilience",
                "content": "Discussing mindset: *tanul a hibáiból* ('learns from one's mistakes'), *felelősséget vállal a tetteiért* ('takes responsibility for one's actions'), *konstruktív hozzáállást tanúsít* ('shows a constructive attitude')."
            },
            {
                "type": "examples",
                "title": "Mindset phrases",
                "items": [
                    {
                        "spanish": "A jó vezető nem keres bűnbakot, hanem tanul a hibákból.",
                        "english": "A good leader does not look for scapegoats, but learns from mistakes."
                    },
                    {
                        "spanish": "A pozitív hozzáállás elengedhetetlen a nehéz helyzetek megoldásához.",
                        "english": "A positive attitude is essential for resolving difficult situations."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-20-04-b-gr.json", gr_04_b)

    gr_05_a = {
        "id": "grammar.b1.20.05.proposing-solutions",
        "title": "Proposing Action Plans: azt javaslom, hogy... + subjunctive (-jon/-jen)",
        "sections": [
            {
                "type": "text",
                "title": "Formal and Constructive Proposals",
                "content": "To propose constructive solutions: *Azt javaslom, hogy tekintsük át újra a tervet.* ('I propose that we review the plan again.'). *Célszerű lenne, ha bevonunk egy külső tanácsadót.* ('It would be expedient if we involved an external consultant.')."
            },
            {
                "type": "examples",
                "title": "Proposal examples",
                "items": [
                    {
                        "spanish": "Azt javaslom, hogy azonnal dolgozzunk ki egy új cselekvési tervet.",
                        "english": "I suggest that we immediately work out a new action plan."
                    },
                    {
                        "spanish": "Érdemes megfontolni több alternatívát is a végső döntés előtt.",
                        "english": "It is worth considering several alternatives before the final decision."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-20-05-a-gr.json", gr_05_a)

    gr_05_b = {
        "id": "grammar.b1.20.05.evaluating-effectiveness",
        "title": "Assessing Outcomes: eredményesnek bizonyul, hatékonyságot növel",
        "sections": [
            {
                "type": "text",
                "title": "Evaluating Solution Effectiveness",
                "content": "Expressing outcome and efficiency: *eredményesnek bizonyul* ('proves to be effective'), *hosszú távon megtérül* ('pays off in the long run'), *növeli a hatékonyságot* ('increases efficiency')."
            },
            {
                "type": "examples",
                "title": "Outcome evaluation phrases",
                "items": [
                    {
                        "spanish": "Az új módszer a gyakorlatban rendkívül eredményesnek bizonyult.",
                        "english": "In practice, the new method proved to be extremely effective."
                    },
                    {
                        "spanish": "A megvalósítás során folyamatosan mérjük az eredményeket.",
                        "english": "During implementation, we continuously measure the results."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-20-05-b-gr.json", gr_05_b)

    # -------------------------------------------------------------------------
    # 3. Exercise Files (01 to 05 + consolidation)
    # -------------------------------------------------------------------------
    for i in range(1, 6):
        padded = f"0{i}"
        curr_voc = [voc_01, voc_02, voc_03, voc_04, voc_05][i-1]
        ex_data = {
            "lesson": f"b1-20-{padded}",
            "exercises": [
                {
                    "id": f"b1-20-{padded}.ex01",
                    "type": "matching",
                    "category": "vocabulary",
                    "pairs": [[w["lemma"], w["translation"]] for w in curr_voc["words"]]
                },
                {
                    "id": f"b1-20-{padded}.ex02",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "question": f"Melyik mondat fejezi ki helyesen a múltbeli feltételt? (Lesson {i})",
                    "options": [
                        "Ha időben szóltál volna, elkerültük volna ezt a súlyos hibát.",
                        "Ha időben szólnál volt, elkerüljük a hibát lett volna.",
                        "Ha szólni időben ezért nem hiba van volt."
                    ],
                    "correct": 0
                },
                {
                    "id": f"b1-20-{padded}.ex03",
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "sentence": "A nehéz helyzetben közös erővel megtaláltuk a helyes ____. (solution -t)",
                    "answer": "megoldást"
                },
                {
                    "id": f"b1-20-{padded}.ex04",
                    "type": "fill-blank",
                    "category": "grammar",
                    "sentence": "Sokkal körültekintőbbnek kellett ____ lennünk a döntés meghozatalakor. (should have - volna)",
                    "answer": "volna"
                },
                {
                    "id": f"b1-20-{padded}.ex05",
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "question": "Mit jelent a felelősségvállalás egy hiba elkövetése után?",
                    "options": [
                        "Elismerjük a tévedést, és megpróbáljuk helyrehozni a következményeket.",
                        "Más munkatársakra hárítjuk a hibát, és titokban tartjuk az esetet.",
                        "Azonnal felmondunk a munkahelyünkön szó nélkül."
                    ],
                    "correct": 0
                },
                {
                    "id": f"b1-20-{padded}.ex06",
                    "type": "fill-blank",
                    "category": "grammar",
                    "sentence": "Bárcsak jobban figyeltem ____ a tanár úr magyarázatára! (if only I had - volna)",
                    "answer": "volna"
                },
                {
                    "id": f"b1-20-{padded}.ex07",
                    "type": "sentence-builder",
                    "category": "grammar",
                    "tiles": ["A", "hibákból", "levont", "tanulság", "segít", "a", "jövőbeli", "helyes", "döntésekben."],
                    "solution": ["A", "hibákból", "levont", "tanulság", "segít", "a", "jövőbeli", "helyes", "döntésekben."]
                },
                {
                    "id": f"b1-20-{padded}.ex08",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "Miért fontos a konstruktív hozzáállás egy váratlan probléma esetén?",
                    "options": [
                        "Mert a hibáztatás helyett a lehetséges kiutakra és megoldásokra összpontosít.",
                        "Mert automatikusan törli a múltbeli eseményeket mindenki emlékezetéből.",
                        "Mert megakadályozza, hogy valaha bármilyen új feladatba kezdjünk."
                    ],
                    "correct": 0
                }
            ]
        }
        write_json(f"content/hu/exercises/b1/b1-20-{padded}-ex.json", ex_data)

    # Consolidation exercises
    ex_consolidation = {
        "lesson": "b1-20-consolidation",
        "exercises": [
            {
                "id": "b1-20-consolidation.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["hiba", "mistake"],
                    ["következmény", "consequence"],
                    ["kiút", "way out"],
                    ["tanulság", "lesson learned"]
                ]
            },
            {
                "id": "b1-20-consolidation.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik mondat fogalmazza meg helyesen az elmaradt cselekvést?",
                "options": [
                    "Jobb lett volna, ha már a kezdet kezdetén megbeszéljük a felmerülő kétségeket.",
                    "Jobb volt ha megbeszélni volt kezdettől a kétségeket volna.",
                    "Kellett volna hogy megbeszélni lett kétség nélkül."
                ],
                "correct": 0
            },
            {
                "id": "b1-20-consolidation.ex03",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A bizottság elfogadta a mérnök új szakmai ____. (proposal -át)",
                "answer": "javaslatát"
            },
            {
                "id": "b1-20-consolidation.ex04",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Ha nem segítettél volna, nem tudtam ____ megoldani a feladatot. (would have - volna)",
                "answer": "volna"
            },
            {
                "id": "b1-20-consolidation.ex05",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "pozitív", "hozzáállás", "és", "az", "őszinte", "önkritika", "a", "fejlődés", "alapja."],
                "solution": ["A", "pozitív", "hozzáállás", "és", "az", "őszinte", "önkritika", "a", "fejlődés", "alapja."]
            },
            {
                "id": "b1-20-consolidation.ex06",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent az 'alternatíva' kifejezés?",
                "options": [
                    "Egy másik lehetséges választási lehetőséget vagy megoldási módot.",
                    "Egy szigorú, megfellebbezhetetlen büntetést.",
                    "Egy régi, elavult számítógépes programot."
                ],
                "correct": 0
            },
            {
                "id": "b1-20-consolidation.ex07",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A tapasztalt vezető felelősséget ____ az egész csapat munkájáért. (takes / bears - vállal)",
                "answer": "vállal"
            },
            {
                "id": "b1-20-consolidation.ex08",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Hogyan kezeli Karinthy diák-hőse a rossz bizonyítvány problémáját a klasszikus novellában?",
                "options": [
                    "Bravúros szóbeli logikával magyarázza, hogy miért a véletlen és a tanárok szigora a hibás.",
                    "Azonnal bevallja a teljes igazságot és bocsánatot kér az apjától.",
                    "Eltépi a bizonyítványt, és új iskolát keres a szomszéd városban."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-20-consolidation-ex.json", ex_consolidation)

    # -------------------------------------------------------------------------
    # 4. Classic Story Adaptation for Lesson 5 / Consolidation
    # -------------------------------------------------------------------------
    story_classic = {
        "id": "story.b1.20.classic",
        "title": "Magyarázom a bizonyítványomat",
        "level": "B1",
        "order": 20,
        "type": "classics",
        "estimatedMinutes": 7,
        "summary": "An adaptation of Frigyes Karinthy's immortal comic masterpiece 'Magyarázom a bizonyítványomat' from 'Tanár úr kérem'. Walking home with an unfortunate report card, the student rehearses an elaborate, philosophical defense for his father, weaving past conditionals and hypothetical excuses to solve an impossible problem.",
        "characters": [
            "A diák",
            "Az édesapa"
        ],
        "location": "Budapest, hazafelé az utcán",
        "author": "Karinthy Frigyes",
        "work": "Tanár úr kérem",
        "paragraphs": [
            {
                "type": "narration",
                "text": "A pesti körúton lassan lépdelt a diák, táskájában a félévi bizonyítvánnyal. A zsebében lapuló papíron ott sötétlett egy hármas algebrából és egy kettes magatartásból. Valódi vészhelyzet volt ez, amely azonnali és zseniális megoldást kívánt."
            },
            {
                "type": "dialogue",
                "speaker": "A diák",
                "text": "Ha apa most a szemembe néz, azonnal látni fogja a nehézséget. Mit kellett volna tennem? Ha Fröhlich tanár úr nem pont engem szólít ki a másodfokú egyenletnél, hanem a Skurekket, most tiszta volna a lelkiismeretem!"
            },
            {
                "type": "narration",
                "text": "A diák megállt a kirakat előtt, és a tükörképének próbálta el a beszédet. Az önkritika nehéz dolog egy tizennégy éves fiúnak, a fantázia viszont határtalan."
            },
            {
                "type": "dialogue",
                "speaker": "A diák",
                "text": "Édesapám, hallgass meg, mielőtt haragra gerjednél! A kettes valójában egy váratlan félreértés következménye. Ha a táblánál nem köhögött volna valaki a hátsó padban, pontosan emlékeztem volna a képletre!"
            },
            {
                "type": "narration",
                "text": "Elképzelte, ahogy belép a lakás ajtaján. Apa a karosszékben ül, kezében az újsággal, és komor tekintettel várja a magyarázatot."
            },
            {
                "type": "dialogue",
                "speaker": "Az édesapa",
                "text": "Fiam, a mulasztás nem mentség. Jobb lett volna, ha a grund helyett a tankönyvet bújtad volna délutánonként!"
            },
            {
                "type": "dialogue",
                "speaker": "A diák",
                "text": "De édesapám! A tanár úr maga mondta, hogy bennem mély szunnyadó tehetség lakozik, csak a módszer nem feküdt a temperamentumomnak! A jövő félévben olyan eredményességet mutatok fel, hogy még az igazgató úr is gratulálni fog!"
            },
            {
                "type": "narration",
                "text": "A diák mély levegőt vett, felnyomta a sapkáját, és megnyomta a kapucsengőt. A hibákból tanulni kell, de amíg az embernek van humora és szellemes nyelve, minden nehézségből létezik valamilyen kiút."
            }
        ]
    }
    write_json("content/hu/stories/classics/b1/b1-20-karinthy.json", story_classic)

    # -------------------------------------------------------------------------
    # 5. Lesson Files (01 to 05 + consolidation)
    # -------------------------------------------------------------------------
    for i in range(1, 6):
        padded = f"0{i}"
        titles = {
            "01": ("If It Had Happened Differently", "Ha máshogy történt volna..."),
            "02": ("What Should Have Been Done", "Mit kellett volna tenni?"),
            "03": ("Finding a Way Through", "Kiút a nehézségekből"),
            "04": ("Learning From a Mistake", "Tanulni a hibákból"),
            "05": ("Explaining a Solution", "Megoldási javaslatok")
        }
        en_title, hu_title = titles[padded]
        lesson_data = {
            "id": f"lesson.b1.20-{padded}",
            "unit": 20,
            "title": en_title,
            "level": "B1",
            "grammar": "Past Conditional (ha + múlt idő + volna) and Unfulfilled Past Obligation (kellett volna)",
            "goal": [
                f"I can understand and use vocabulary for {en_title.lower()}.",
                "I can form past conditional sentences using volna in Hungarian.",
                "I can talk about mistakes, regrets, lessons learned, and solutions.",
                "I can master four new target vocabulary items in authentic context."
            ],
            "sections": [
                {
                    "type": "goal",
                    "title": "Lesson Goals",
                    "items": [
                        f"I can understand and use vocabulary for {en_title.lower()}.",
                        "I can form past conditional sentences using volna in Hungarian.",
                        "I can talk about mistakes, regrets, lessons learned, and solutions.",
                        "I can master four new target vocabulary items in authentic context."
                    ]
                },
                {"type": "recycle", "title": "Quick Review"},
                {"type": "grammar", "ref": f"grammar/b1/b1-20-{padded}-a-gr.json"},
                {"type": "grammar", "ref": f"grammar/b1/b1-20-{padded}-b-gr.json"},
                {"type": "vocabulary", "title": "Lesson Vocabulary", "ref": f"vocabulary/b1/b1-20-{padded}-voc.json"},
                {
                    "type": "exercise-group",
                    "title": "Practice",
                    "ref": f"exercises/b1/b1-20-{padded}-ex.json",
                    "exerciseRefs": [f"b1-20-{padded}.ex0{k}" for k in range(1, 9)]
                }
            ]
        }
        write_json(f"content/hu/lessons/b1/b1-20-{padded}.json", lesson_data)

    consolidation_data = {
        "id": "lesson.b1.20-consolidation",
        "unit": 20,
        "title": "Unit 20 Consolidation",
        "level": "B1",
        "grammar": "Consolidation of Past Conditional & Problem-Solving Strategies",
        "sections": [
            {
                "type": "story",
                "title": "Magyarázom a bizonyítványomat (Karinthy Frigyes)",
                "ref": "stories/classics/b1/b1-20-karinthy.json"
            },
            {
                "type": "exercise-group",
                "title": "Consolidation Practice",
                "ref": "exercises/b1/b1-20-consolidation-ex.json",
                "exerciseRefs": [f"b1-20-consolidation.ex0{k}" for k in range(1, 9)]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-20-consolidation.json", consolidation_data)
    print("Successfully built Hungarian B1 Core Unit 20 (b1-20)!")

if __name__ == "__main__":
    build_unit_20_core()
