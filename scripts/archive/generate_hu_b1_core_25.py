#!/usr/bin/env python3
"""Generate Hungarian B1 Core Unit 25: Change & Development (b1-25)."""

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

def build_unit_25_core():
    # -------------------------------------------------------------------------
    # 1. Vocabulary Files (4 words each = 20 words total)
    # -------------------------------------------------------------------------
    voc_01 = {
        "id": "vocab.b1.25.01",
        "lesson": "b1-25-01",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "fejlődés", "translation": "development, progress, growth", "pos": "noun"},
            {"lemma": "változás", "translation": "change, alteration, shift", "pos": "noun"},
            {"lemma": "átalakulás", "translation": "transformation, metamorphosis", "pos": "noun"},
            {"lemma": "irányzat", "translation": "trend, movement, tendency", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-25-01-voc.json", voc_01)

    voc_02 = {
        "id": "vocab.b1.25.02",
        "lesson": "b1-25-02",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "fokozatosság", "translation": "gradualness, stepwise progression", "pos": "noun"},
            {"lemma": "átmenet", "translation": "transition, intermediate stage", "pos": "noun"},
            {"lemma": "áttörés", "translation": "breakthrough, decisive advance", "pos": "noun"},
            {"lemma": "kibontakozás", "translation": "unfolding, blossoming, emergence", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-25-02-voc.json", voc_02)

    voc_03 = {
        "id": "vocab.b1.25.03",
        "lesson": "b1-25-03",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "hanyatlás", "translation": "decline, decay, downturn", "pos": "noun"},
            {"lemma": "megújulás", "translation": "renewal, revitalization, revival", "pos": "noun"},
            {"lemma": "újjászületés", "translation": "rebirth, renaissance, regeneration", "pos": "noun"},
            {"lemma": "lendület", "translation": "momentum, impetus, drive", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-25-03-voc.json", voc_03)

    voc_04 = {
        "id": "vocab.b1.25.04",
        "lesson": "b1-25-04",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "tapasztalat", "translation": "experience, accumulated insight", "pos": "noun"},
            {"lemma": "érlelődés", "translation": "maturation, ripening, mellowing", "pos": "noun"},
            {"lemma": "alkalmazkodás", "translation": "adaptation, adjustment, accommodation", "pos": "noun"},
            {"lemma": "szemléletmód", "translation": "mindset, outlook, worldview", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-25-04-voc.json", voc_04)

    voc_05 = {
        "id": "vocab.b1.25.05",
        "lesson": "b1-25-05",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "irányvonal", "translation": "guideline, general line of development", "pos": "noun"},
            {"lemma": "kiteljesedés", "translation": "fulfillment, culmination, fruition", "pos": "noun"},
            {"lemma": "maradandóság", "translation": "permanence, enduring quality, durability", "pos": "noun"},
            {"lemma": "korszakváltás", "translation": "epochal shift, transition to a new era", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-25-05-voc.json", voc_05)

    # -------------------------------------------------------------------------
    # 2. Grammar Files (2 per regular lesson = 10 files)
    # -------------------------------------------------------------------------
    gr_01_a = {
        "id": "grammar.b1.25.01.verbs-of-becoming",
        "title": "Verbs of Becoming: -odik/-edik and -ul/-ül",
        "sections": [
            {
                "type": "text",
                "title": "Forming Verbs of Change",
                "content": "Hungarian forms verbs of becoming and changing from adjectives and nouns using suffixes: *-odik / -edik / -ödik* (*gazdagodik* = gets rich, *fejlődik* = develops, *tisztul* = clears up, *szépül* = becomes beautiful). *Valamivé válik* ('becomes sth') expresses full transformation."
            },
            {
                "type": "examples",
                "title": "Transformation in context",
                "items": [
                    {
                        "spanish": "A város képe rohamosan modernizálódik az utóbbi években.",
                        "english": "The city's appearance is modernizing rapidly in recent years."
                    },
                    {
                        "spanish": "A kitartó munka révén az elképzelés végül valósággá vált.",
                        "english": "Through persevering work, the concept finally became reality."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-25-01-a-gr.json", gr_01_a)

    gr_01_b = {
        "id": "grammar.b1.25.01.trend-expressions",
        "title": "Describing Trends: növekvő tendenciát mutat, teret hódít",
        "sections": [
            {
                "type": "text",
                "title": "Discourse on Societal Shifts",
                "content": "*Növekvő tendenciát mutat* ('shows a growing tendency'), *teret hódít* ('gains ground / spreads widely'), *háttérbe szorul* ('is relegated to the background')."
            },
            {
                "type": "examples",
                "title": "Trends in society",
                "items": [
                    {
                        "spanish": "A megújuló energiaforrások használata egyre nagyobb teret hódít.",
                        "english": "The use of renewable energy sources is gaining ever greater ground."
                    },
                    {
                        "spanish": "A hagyományos szokások egy része sajnos háttérbe szorult a városokban.",
                        "english": "A portion of traditional customs has unfortunately been relegated to the background in cities."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-25-01-b-gr.json", gr_01_b)

    gr_02_a = {
        "id": "grammar.b1.25.02.gradual-transition",
        "title": "Stepwise Progression: fokozatosan, lépésről lépésre",
        "sections": [
            {
                "type": "text",
                "title": "Adverbs of Gradual Change",
                "content": "*Fokozatosan* ('gradually'), *lépésről lépésre* ('step by step'), *fokról fokra* ('degree by degree'), *átmenetet képez* ('forms a transition between')."
            },
            {
                "type": "examples",
                "title": "Stepwise development",
                "items": [
                    {
                        "spanish": "A reformokat nem azonnal, hanem fokozatosan vezették be.",
                        "english": "The reforms were introduced not immediately, but gradually."
                    },
                    {
                        "spanish": "Az új épület harmonikus átmenetet képez a régi és az új városrész között.",
                        "english": "The new building forms a harmonious transition between the old and new parts of town."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-25-02-a-gr.json", gr_02_a)

    gr_02_b = {
        "id": "grammar.b1.25.02.breakthrough-kibontakozas",
        "title": "Decisive Turns: áttörést hoz, kibontakozik",
        "sections": [
            {
                "type": "text",
                "title": "Milestones and Emergence",
                "content": "*Áttörést ér el / hoz* ('achieves / brings a breakthrough'), *teljes fényében kibontakozik* ('unfolds in full splendour'), *új fejezetet nyit* ('opens a new chapter')."
            },
            {
                "type": "examples",
                "title": "Milestone expressions",
                "items": [
                    {
                        "spanish": "A kutatásban elért felfedezés valódi áttörést hozott az orvostudományban.",
                        "english": "The discovery achieved in the research brought a genuine breakthrough in medical science."
                    },
                    {
                        "spanish": "A fiatal tehetség képességei gyorsan kibontakoztak a támogató környezetben.",
                        "english": "The young talent's abilities quickly blossomed in the supportive environment."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-25-02-b-gr.json", gr_02_b)

    gr_03_a = {
        "id": "grammar.b1.25.03.decline-and-revival",
        "title": "Cycles of Decline & Renewal: hanyatlásnak indul, új lendületet kap",
        "sections": [
            {
                "type": "text",
                "title": "Historical and Personal Cycles",
                "content": "*Hanyatlásnak indul* ('begins to decline'), *új lendületet kap* ('receives new impetus/momentum'), *újjászületik hamvaiból* ('is reborn from its ashes')."
            },
            {
                "type": "examples",
                "title": "Cyclical change",
                "items": [
                    {
                        "spanish": "A gazdaság a válság után meglepően gyorsan új lendületet kapott.",
                        "english": "Following the crisis, the economy gained new momentum surprisingly quickly."
                    },
                    {
                        "spanish": "A történelmi városközpont a felújítások révén szinte újjászületett.",
                        "english": "The historic town center was almost completely reborn through the renovations."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-25-03-a-gr.json", gr_03_a)

    gr_03_b = {
        "id": "grammar.b1.25.03.past-present-contrasts",
        "title": "Contrasting Epochs: míg régen... ma viszont...",
        "sections": [
            {
                "type": "text",
                "title": "Temporal Contrast Discourse",
                "content": "*Míg korábban... mostanra viszont...* ('while earlier... by now however...'), *a múlttal ellentétben* ('in contrast to the past'), *napjainkra gyökeresen megváltozott* ('has radically changed by our days')."
            },
            {
                "type": "examples",
                "title": "Comparative eras",
                "items": [
                    {
                        "spanish": "Míg régen hetekig tartott egy levélváltás, ma másodpercek alatt elérjük egymást.",
                        "english": "While in the past an exchange of letters took weeks, today we reach each other in seconds."
                    },
                    {
                        "spanish": "A korábbi nehézségekkel ellentétben a mai diákok számtalan lehetőséggel rendelkeznek.",
                        "english": "In contrast to earlier difficulties, today's students possess countless opportunities."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-25-03-b-gr.json", gr_03_b)

    gr_04_a = {
        "id": "grammar.b1.25.04.maturation-and-adaptation",
        "title": "Maturation & Adaptation: tapasztalatot szerez, alkalmazkodik vmihez",
        "sections": [
            {
                "type": "text",
                "title": "Personal Character Growth",
                "content": "*Tapasztalatot gyűjt / szerez* ('gathers / gains experience'), *alkalmazkodik a változó körülményekhez* ('adapts to changing circumstances'), *szemléletmódot vált* ('changes one's outlook')."
            },
            {
                "type": "examples",
                "title": "Personal development",
                "items": [
                    {
                        "spanish": "A nehéz próbák során értékes élettapasztalatot szereztünk.",
                        "english": "During the difficult trials, we gained valuable life experience."
                    },
                    {
                        "spanish": "A túlélés kulcsa a megváltozott helyzethez való gyors alkalmazkodás.",
                        "english": "The key to survival is rapid adaptation to the altered situation."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-25-04-a-gr.json", gr_04_a)

    gr_04_b = {
        "id": "grammar.b1.25.04.changing-perspectives",
        "title": "Reframing Views: átértékel, más megvilágításba helyez",
        "sections": [
            {
                "type": "text",
                "title": "Cognitive Shift",
                "content": "*Átértékeli a prioritásait* ('reassesses one's priorities'), *új megvilágításba helyez vmit* ('casts sth in a new light'), *megérik benne a felismerés* ('the realization matures inside them')."
            },
            {
                "type": "examples",
                "title": "Shift in perspectives",
                "items": [
                    {
                        "spanish": "Az események után teljesen átértékeltem a saját céljaimat és kapcsolataimat.",
                        "english": "After the events, I completely reassessed my own goals and relationships."
                    },
                    {
                        "spanish": "A felfedezés teljesen új megvilágításba helyezte a korábbi elméleteket.",
                        "english": "The discovery placed earlier theories in a completely new light."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-25-04-b-gr.json", gr_04_b)

    gr_05_a = {
        "id": "grammar.b1.25.05.epochal-milestones",
        "title": "Epochal Shifts: korszakváltást jelent, mérföldkőnek számít",
        "sections": [
            {
                "type": "text",
                "title": "Monumental Transitions",
                "content": "*Korszakváltást jelent* ('marks an epochal shift'), *fontos mérföldkőnek számít* ('counts as an important milestone'), *kiteljesedik a műve* ('one's work reaches culmination')."
            },
            {
                "type": "examples",
                "title": "Historical turning points",
                "items": [
                    {
                        "spanish": "Az internet elterjedése valódi korszakváltást jelentett az emberiség történetében.",
                        "english": "The spread of the internet marked a genuine epochal shift in human history."
                    },
                    {
                        "spanish": "A törvény elfogadása döntő mérföldkő volt a jogállamiság felé vezető úton.",
                        "english": "The adoption of the law was a decisive milestone on the road toward the rule of law."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-25-05-a-gr.json", gr_05_a)

    gr_05_b = {
        "id": "grammar.b1.25.05.enduring-legacy",
        "title": "Permanence & Legacy: maradandó értéket teremt, kiállja az idő próbáját",
        "sections": [
            {
                "type": "text",
                "title": "Enduring Values",
                "content": "*Maradandó értéket teremt* ('creates lasting / enduring value'), *kiállja az idő próbáját* ('stands the test of time'), *örök érvényű igazság* ('an eternal truth')."
            },
            {
                "type": "examples",
                "title": "Permanence in culture",
                "items": [
                    {
                        "spanish": "A költő olyan verseket hagyott hátra, amelyek kiállták az idő próbáját.",
                        "english": "The poet left behind poems that stood the test of time."
                    },
                    {
                        "spanish": "A tudás és a becsület olyan értékek, amelyek soha nem veszítik el fényüket.",
                        "english": "Knowledge and honor are values that never lose their luster."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-25-05-b-gr.json", gr_05_b)

    # -------------------------------------------------------------------------
    # 3. Exercise Files (01 to 05 + consolidation)
    # -------------------------------------------------------------------------
    ex_01 = {
        "lesson": "b1-25-01",
        "exercises": [
            {
                "id": "b1-25-01.ex01",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent az 'átalakulás' kifejezés?",
                "options": [
                    "Valaminek az alakjában, szerkezetében vagy jellegében bekövetkező mélyreható változást.",
                    "A tárgyak pontos leporolását és tisztítását.",
                    "Egy könyv lapjainak megszámlálását."
                ],
                "correct": 0
            },
            {
                "id": "b1-25-01.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A kitartó munka és tanulás révén a terv valóság_____ vált. (became reality - gá)",
                "answer": "gá"
            },
            {
                "id": "b1-25-01.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "környezettudatos", "életmód", "egyre", "nagyobb", "teret", "hódít", "napjainkban."],
                "solution": ["A", "környezettudatos", "életmód", "egyre", "nagyobb", "teret", "hódít", "napjainkban."]
            },
            {
                "id": "b1-25-01.ex04",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent az 'irányzat' a kultúrában vagy gazdaságban?",
                "options": [
                    "Egy domináns mozgalmat, közös gondolkodási vagy fejlesztési tendenciát.",
                    "A szél pontos irányát mutató zászlót a tetőn.",
                    "Egy vasúti váltó mechanikus szerkezetét."
                ],
                "correct": 0
            },
            {
                "id": "b1-25-01.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A technológiai fejlő_____ rohamos ütemben alakítja át a mindennapjainkat. (development - dés)",
                "answer": "dés"
            },
            {
                "id": "b1-25-01.ex06",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik képző fejezi ki a tulajdonság felvételét (pl. 'szép' -> 'szebbé válik')?",
                "options": [
                    "-ul / -ül (szépül, tisztul, melegszik)",
                    "-gat / -get (nézeget, olvasgat)",
                    "-kodik / -kedik (vitakodik, veszekedik)"
                ],
                "correct": 0
            },
            {
                "id": "b1-25-01.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A város történelmi központja látványosan szép_____ az utóbbi években. (beautified / got nicer - ült)",
                "answer": "ült"
            },
            {
                "id": "b1-25-01.ex08",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "társadalmi", "változások", "új", "korszakot", "nyitottak", "a", "történelemben."],
                "solution": ["A", "társadalmi", "változások", "új", "korszakot", "nyitottak", "a", "történelemben."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-25-01-ex.json", ex_01)

    ex_02 = {
        "lesson": "b1-25-02",
        "exercises": [
            {
                "id": "b1-25-02.ex01",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent az 'áttörés' egy folyamatban?",
                "options": [
                    "Egy jelentős, döntő előrelépést a korábbi akadályok leküzdésével.",
                    "Egy gátszakadás okozta árvizet a folyón.",
                    "Egy faág letörését a viharos szélben."
                ],
                "correct": 0
            },
            {
                "id": "b1-25-02.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A reformokat nem kapkodva, hanem fokozato_____ vezették be a gyakorlatba. (gradually - san)",
                "answer": "san"
            },
            {
                "id": "b1-25-02.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Az", "új", "tudományos", "felfedezés", "valódi", "áttörést", "hozott", "a", "gyógyításban."],
                "solution": ["Az", "új", "tudományos", "felfedezés", "valódi", "áttörést", "hozott", "a", "gyógyításban."]
            },
            {
                "id": "b1-25-02.ex04",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit fejez ki az 'átmenet' fogalma?",
                "options": [
                    "Két különböző állapot, időszak vagy szint közötti köztes szakaszt.",
                    "A gyalogos zebra felfestését a betonútra.",
                    "Egy ideiglenes vasúti sorompót."
                ],
                "correct": 0
            },
            {
                "id": "b1-25-02.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A gyermek zenei tehetsége a kiváló tanár mellett gyorsan kibontakoz_____. (blossomed - ott)",
                "answer": "ott"
            },
            {
                "id": "b1-25-02.ex06",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik kifejezés írja le a folyamatos, apránként történő fejlődést?",
                "options": [
                    "Lépésről lépésre.",
                    "Egy szempillantás alatt.",
                    "Visszafelé haladva."
                ],
                "correct": 0
            },
            {
                "id": "b1-25-02.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A modern épület harmonikus átmenetet _____ a régi és az új városrész között. (forms - képez)",
                "answer": "képez"
            },
            {
                "id": "b1-25-02.ex08",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "fokozatosság", "elve", "kulcsfontosságú", "a", "tartós", "tudás", "elsajátításában."],
                "solution": ["A", "fokozatosság", "elve", "kulcsfontosságú", "a", "tartós", "tudás", "elsajátításában."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-25-02-ex.json", ex_02)

    ex_03 = {
        "lesson": "b1-25-03",
        "exercises": [
            {
                "id": "b1-25-03.ex01",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent az 'újjászületés'?",
                "options": [
                    "Egy pusztulás vagy hanyatlás utáni megújulást, virágzó reneszánszt.",
                    "Egy születésnapi meghívó elküldését postán.",
                    "Egy új ruhadarab felpróbálását az üzletben."
                ],
                "correct": 0
            },
            {
                "id": "b1-25-03.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Míg korábban alig volt érdeklődés, mostanra _____ hatalmas tömegek látogatják a múzeumot. (however - viszont)",
                "answer": "viszont"
            },
            {
                "id": "b1-25-03.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "gazdaság", "a", "nehéz", "időszak", "után", "új", "lendületet", "kapott."],
                "solution": ["A", "gazdaság", "a", "nehéz", "időszak", "után", "új", "lendületet", "kapott."]
            },
            {
                "id": "b1-25-03.ex04",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mi a 'hanyatlás' ellentéte?",
                "options": [
                    "Fejlődés / Megújulás.",
                    "Visszaesés.",
                    "Pusztulás."
                ],
                "correct": 0
            },
            {
                "id": "b1-25-03.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A felújításoknak köszönhetően a történelmi várnegyed szinte újjászüle_____. (was reborn - tett)",
                "answer": "tett"
            },
            {
                "id": "b1-25-03.ex06",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Hogyan fejezzük ki magyarul: 'In contrast to the past'?",
                "options": [
                    "A múlttal ellentétben.",
                    "A múltnak köszönhetően.",
                    "A múltban maradt."
                ],
                "correct": 0
            },
            {
                "id": "b1-25-03.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A régi kultúra lassú hanyatlásnak in_____, miközben új eszmék születtek. (began - dult)",
                "answer": "dult"
            },
            {
                "id": "b1-25-03.ex08",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "szellemi", "megújulás", "új", "reményt", "adott", "a", "közösségnek."],
                "solution": ["A", "szellemi", "megújulás", "új", "reményt", "adott", "a", "közösségnek."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-25-03-ex.json", ex_03)

    ex_04 = {
        "lesson": "b1-25-04",
        "exercises": [
            {
                "id": "b1-25-04.ex01",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent az 'alkalmazkodás' képessége?",
                "options": [
                    "Készséget a megváltozott körülményekhez, új helyzetekhez való rugalmas igazodásra.",
                    "Minden új szabály merev és dacos elutasítását.",
                    "A cipőfűző bekötésének képességét."
                ],
                "correct": 0
            },
            {
                "id": "b1-25-04.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A nehéz tapasztalatok során teljesen átértékeltem a korábbi céljai_____. (my goals - mat)",
                "answer": "mat"
            },
            {
                "id": "b1-25-04.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Az", "évek", "során", "felhalmozott", "tapasztalat", "segített", "a", "bölcs", "döntésben."],
                "solution": ["Az", "évek", "során", "felhalmozott", "tapasztalat", "segített", "a", "bölcs", "döntésben."]
            },
            {
                "id": "b1-25-04.ex04",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mi az a 'szemléletmód'?",
                "options": [
                    "A világról és a dolgokról alkotott alapvető gondolkodási mód, látásmód.",
                    "Egy optikai szemüveg dioptriájának értéke.",
                    "A táblára felírt matematikai képlet."
                ],
                "correct": 0
            },
            {
                "id": "b1-25-04.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A személyiség belső érlelő_____ hosszú és sokszor küzdelmes folyamat. (maturation - dése)",
                "answer": "dése"
            },
            {
                "id": "b1-25-04.ex06",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik kifejezés fejezi ki, hogy valami új értelmet nyer?",
                "options": [
                    "Új megvilágításba helyezi a dolgokat.",
                    "Sötétben hagyja a kérdést.",
                    "Kikapcsolja a villanyt."
                ],
                "correct": 0
            },
            {
                "id": "b1-25-04.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Gyorsan alkalmazkodnunk kell a megváltozott piaci körülmények_____. (to the circumstances - hez)",
                "answer": "hez"
            },
            {
                "id": "b1-25-04.ex08",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "nyitott", "szemléletmód", "nélkülözhetetlen", "az", "élethosszig", "tartó", "tanuláshoz."],
                "solution": ["A", "nyitott", "szemléletmód", "nélkülözhetetlen", "az", "élethosszig", "tartó", "tanuláshoz."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-25-04-ex.json", ex_04)

    ex_05 = {
        "lesson": "b1-25-05",
        "exercises": [
            {
                "id": "b1-25-05.ex01",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent a 'korszakváltás'?",
                "options": [
                    "Egy korábbi történelmi vagy kulturális időszak lezárulását és egy merőben új korszak kezdetét.",
                    "A falióra mutatójának átállítását a téli időszámításra.",
                    "Egy könyv fejezetcímének elolvasását."
                ],
                "correct": 0
            },
            {
                "id": "b1-25-05.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Az új technológia elterjedése döntő mérföldkőnek számí_____ a fejlődésben. (counts as - tott)",
                "answer": "tott"
            },
            {
                "id": "b1-25-05.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "nemes", "eszmék", "és", "a", "tudás", "mindig", "kiállják", "az", "idő", "próbáját."],
                "solution": ["A", "nemes", "eszmék", "és", "a", "tudás", "mindig", "kiállják", "az", "idő", "próbáját."]
            },
            {
                "id": "b1-25-05.ex04",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent a 'maradandóság' az alkotómunkában?",
                "options": [
                    "Olyan értéket, amely nem avul el, hanem évszázadokon át érvényes és értékes marad.",
                    "A műhelyben való ottmaradást a munkaidő után.",
                    "Egy eldobható műanyag pohár használatát."
                ],
                "correct": 0
            },
            {
                "id": "b1-25-05.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A tudós életműve idős korára teljesedett _____ igazán. (culminated - ki)",
                "answer": "ki"
            },
            {
                "id": "b1-25-05.ex06",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Mit fejez ki a 'kiállja az idő próbáját' szólás?",
                "options": [
                    "Azt, hogy valami az idő múlásával sem veszíti el értékét és igazságát.",
                    "Azt, hogy egy karóra vízálló és bírja a búvárkodást.",
                    "Azt, hogy valaki sokat késik a megbeszélt találkozóról."
                ],
                "correct": 0
            },
            {
                "id": "b1-25-05.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Az alkotó maradandó értéket terem_____ a nemzet számára. (created - tett)",
                "answer": "tett"
            },
            {
                "id": "b1-25-05.ex08",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "világos", "irányvonal", "biztosítja", "a", "társadalom", "hosszú", "távú", "stabilitását."],
                "solution": ["A", "világos", "irányvonal", "biztosítja", "a", "társadalom", "hosszú", "távú", "stabilitását."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-25-05-ex.json", ex_05)

    ex_consolidation = {
        "lesson": "b1-25-consolidation",
        "exercises": [
            {
                "id": "b1-25-consolidation.ex01",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik mondat fejezi ki helyesen a minőségi átalakulást?",
                "options": [
                    "A kitartó munka révén az elképzelés végül valósággá vált.",
                    "A kitartó munka révén az elképzelés valóságban állt.",
                    "A kitartó munka révén az elképzelés valóságról döntött."
                ],
                "correct": 0
            },
            {
                "id": "b1-25-consolidation.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A nehéz debreceni diákévek során Nyilas Misi jelleme fokozatosan megér_____ a viharokban. (matured - ett)",
                "answer": "ett"
            },
            {
                "id": "b1-25-consolidation.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "tapasztalatok", "és", "a", "próbatételek", "formálják", "az", "ember", "igazi", "jellemét."],
                "solution": ["A", "tapasztalatok", "és", "a", "próbatételek", "formálják", "az", "ember", "igazi", "jellemét."]
            },
            {
                "id": "b1-25-consolidation.ex04",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A tudás és az emberség maradandó érté_____ képez az emberi életben. (value - ket)",
                "answer": "ket"
            },
            {
                "id": "b1-25-consolidation.ex05",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["Az", "új", "szemléletmód", "segít", "megtalálni", "a", "helyes", "irányvonalat."],
                "solution": ["Az", "új", "szemléletmód", "segít", "megtalálni", "a", "helyes", "irányvonalat."]
            },
            {
                "id": "b1-25-consolidation.ex06",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent az, ha egy műalkotás 'kiállja az idő próbáját'?",
                "options": [
                    "Nemzedékek múlva is megőrzi esztétikai és szellemi erejét.",
                    "Egy homokóra segítségével mérik az eladási idejét.",
                    "Nem ázik el a múzeum raktárában az esőben."
                ],
                "correct": 0
            },
            {
                "id": "b1-25-consolidation.ex07",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A történelmi korszakváltás alapjaiban alakította át a társadalom szerkeze_____. (its structure - tét)",
                "answer": "tét"
            },
            {
                "id": "b1-25-consolidation.ex08",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Hogyan alakul át Nyilas Misi jelleme Móricz Zsigmond 'Légy jó mindhalálig' című művében?",
                "options": [
                    "Az igazságtalan vádak fájdalmát leküzdve megerősödik, s elhatározza, hogy egész életében a szegények tanítója lesz.",
                    "Csalódásában elhagyja az iskolát és gazdag kereskedővé válik.",
                    "Katonának áll és soha többé nem nyit ki egyetlen könyvet sem."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-25-consolidation-ex.json", ex_consolidation)

    # -------------------------------------------------------------------------
    # 4. Classic Story Adaptation for Consolidation
    # -------------------------------------------------------------------------
    story_classic = {
        "id": "story.b1.25.classic",
        "title": "Légy jó mindhalálig",
        "level": "B1",
        "order": 25,
        "type": "classics",
        "estimatedMinutes": 8,
        "summary": "An adaptation of Zsigmond Móricz's tender and profound classic 'Légy jó mindhalálig' (Be Faithful Unto Death). In the historic Reformed Collegium of Debrecen, the young student Nyilas Misi undergoes a heartbreaking and transformative maturation. Unjustly accused of stealing a lottery ticket, Misi endures humiliation, but emerges from the trial with an ironclad resolve: to remain pure, honest, and dedicated to educating humanity.",
        "characters": [
            "Nyilas Misi, debreceni kisdiák",
            "Gyéres tanár úr, az osztályfőnök",
            "A Debreceni Református Kollégium tanári kara"
        ],
        "location": "A Debreceni Református Kollégium oratóriuma és az udvar",
        "author": "Móricz Zsigmond",
        "work": "Légy jó mindhalálig (1920)",
        "paragraphs": [
            {
                "type": "narration",
                "text": "A Debreceni Református Kollégium évszázados falai között zord és komoly rend uralkodott. Nyilas Misi, a vékonyka, csöndes kisdiák a könyvek lapjain és a füstös diákbarakkban kereste a helyét. Szíve tele volt tisztasággal és a tanulás olthatatlan vágyával."
            },
            {
                "type": "narration",
                "text": "Ám a felnőttek világa könyörtelen próbatétel elé állította. Egy elveszett reskontó – egy lutriszelvény – miatt a tanári kar elé idézték. A felnőttek gyanakodtak, vádoltak és szigorú szemekkel faggatták a remegő kisfiút."
            },
            {
                "type": "dialogue",
                "speaker": "Gyéres tanár úr",
                "text": "Nyilas Mihály! Állj a tanári asztal elé, és vallj színt! Hová lett a pénz? Ne habozz, a becsületed forog kockán!"
            },
            {
                "type": "dialogue",
                "speaker": "Nyilas Misi",
                "text": "Tanár úr, kérem tisztelettel... én nem vettem el semmit! Nem vagyok tolvaj! Én csak tanultam, cipeltem a nehéz csomagokat, és odaadtam mindent, amit kértek!"
            },
            {
                "type": "narration",
                "text": "Bár végül kiderült az ártatlansága, a megaláztatás sebe mélyen beégett a kisfiú lelkébe. Ám a szenvedés nem törte meg: ez a fájdalmas törés indította el a valódi átalakulást, a lélek érett férfivá válását."
            },
            {
                "type": "dialogue",
                "speaker": "Nyilas Misi",
                "text": "Már nem sírok. Megértettem, hogy a világ tele van vak gyanakvással. De én más leszek: ember akarok lenni, aki nem bánt másokat! Tanító leszek, a szegények és elhagyottak tanítója, s jó leszek... mindhalálig!"
            }
        ]
    }
    write_json("content/hu/stories/classics/b1/b1-25-moricz.json", story_classic)

    # -------------------------------------------------------------------------
    # 5. Lesson Files (01 to 05 + consolidation)
    # -------------------------------------------------------------------------
    for i in range(1, 6):
        padded = f"0{i}"
        titles = {
            "01": ("Change and Shifts", "Változás és átalakulás: Fejlődés és új irányzatok"),
            "02": ("Gradual Transitions", "Fokozatosság és átmenetek: Lépésről lépésre az áttörésig"),
            "03": ("Decline and Renewal", "Hanyatlás és megújulás: Új lendület és összehasonlítások"),
            "04": ("Maturity & Perspectives", "Tapasztalat és érlelődés: Alkalmazkodás és új szemléletmód"),
            "05": ("Milestones & Permanence", "Korszakváltás és maradandóság: Értékek, amelyek kiállják az idő próbáját")
        }
        en_title, hu_title = titles[padded]
        lesson_data = {
            "id": f"lesson.b1.25-{padded}",
            "unit": 25,
            "title": en_title,
            "level": "B1",
            "grammar": "Verbs of Becoming (-odik/-edik, -ul/-ül), Temporal Contrasts & Epochal Milestone Idioms",
            "goal": [
                f"I can understand and use vocabulary for {en_title.lower()}.",
                "I can describe gradual growth, transformations, and contrasting eras in Hungarian.",
                "I can express maturation, personal change, adaptation, and enduring historical legacies.",
                "I can master four new target vocabulary items in authentic context."
            ],
            "sections": [
                {
                    "type": "goal",
                    "title": "Lesson Goals",
                    "items": [
                        f"I can understand and use vocabulary for {en_title.lower()}.",
                        "I can describe gradual growth, transformations, and contrasting eras in Hungarian.",
                        "I can express maturation, personal change, adaptation, and enduring historical legacies.",
                        "I can master four new target vocabulary items in authentic context."
                    ]
                },
                {"type": "recycle", "title": "Quick Review"},
                {"type": "grammar", "ref": f"grammar/b1/b1-25-{padded}-a-gr.json"},
                {"type": "grammar", "ref": f"grammar/b1/b1-25-{padded}-b-gr.json"},
                {"type": "vocabulary", "title": "Lesson Vocabulary", "ref": f"vocabulary/b1/b1-25-{padded}-voc.json"},
                {
                    "type": "exercise-group",
                    "title": "Practice",
                    "ref": f"exercises/b1/b1-25-{padded}-ex.json",
                    "exerciseRefs": [f"b1-25-{padded}.ex0{k}" for k in range(1, 9)]
                }
            ]
        }
        write_json(f"content/hu/lessons/b1/b1-25-{padded}.json", lesson_data)

    consolidation_data = {
        "id": "lesson.b1.25-consolidation",
        "unit": 25,
        "title": "Unit 25 Consolidation",
        "level": "B1",
        "grammar": "Consolidation of Growth, Personal Maturation & Enduring Cultural Legacies",
        "sections": [
            {
                "type": "story",
                "title": "Légy jó mindhalálig (Móricz Zsigmond)",
                "ref": "stories/classics/b1/b1-25-moricz.json"
            },
            {
                "type": "exercise-group",
                "title": "Consolidation Practice",
                "ref": "exercises/b1/b1-25-consolidation-ex.json",
                "exerciseRefs": [f"b1-25-consolidation.ex0{k}" for k in range(1, 9)]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-25-consolidation.json", consolidation_data)
    print("Successfully built Hungarian B1 Core Unit 25 (b1-25)!")

if __name__ == "__main__":
    build_unit_25_core()
