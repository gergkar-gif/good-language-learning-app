#!/usr/bin/env python3
"""Generate Hungarian B1 Core Unit 26: Work, Ambition & Balance (b1-26)."""

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

def build_unit_26_core():
    # -------------------------------------------------------------------------
    # 1. Vocabulary Files (4 words each = 20 words total)
    # -------------------------------------------------------------------------
    voc_01 = {
        "id": "vocab.b1.26.01",
        "lesson": "b1-26-01",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "hivatás", "translation": "vocation, calling, life's work", "pos": "noun"},
            {"lemma": "karrier", "translation": "career, professional track", "pos": "noun"},
            {"lemma": "pályafutás", "translation": "career path, course of employment", "pos": "noun"},
            {"lemma": "szakértelem", "translation": "expertise, professional skill", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-26-01-voc.json", voc_01)

    voc_02 = {
        "id": "vocab.b1.26.02",
        "lesson": "b1-26-02",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "túlóra", "translation": "overtime work, extra hours", "pos": "noun"},
            {"lemma": "leterheltség", "translation": "workload, being overburdened", "pos": "noun"},
            {"lemma": "kimerültség", "translation": "exhaustion, burnout, fatigue", "pos": "noun"},
            {"lemma": "pihenés", "translation": "rest, recreation, relaxation", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-26-02-voc.json", voc_02)

    voc_03 = {
        "id": "vocab.b1.26.03",
        "lesson": "b1-26-03",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "egyensúly", "translation": "balance, equilibrium", "pos": "noun"},
            {"lemma": "prioritás", "translation": "priority, primary importance", "pos": "noun"},
            {"lemma": "időbeosztás", "translation": "time management, daily schedule", "pos": "noun"},
            {"lemma": "rugalmasság", "translation": "flexibility, adaptability", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-26-03-voc.json", voc_03)

    voc_04 = {
        "id": "vocab.b1.26.04",
        "lesson": "b1-26-04",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "ambíció", "translation": "ambition, professional aspiration", "pos": "noun"},
            {"lemma": "érvényesülés", "translation": "advancement, making one's way, succeeding", "pos": "noun"},
            {"lemma": "elismerés", "translation": "recognition, appreciation, praise", "pos": "noun"},
            {"lemma": "előléptetés", "translation": "promotion, advancement in rank", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-26-04-voc.json", voc_04)

    voc_05 = {
        "id": "vocab.b1.26.05",
        "lesson": "b1-26-05",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "elégedettség", "translation": "satisfaction, contentment", "pos": "noun"},
            {"lemma": "munkahelyi légkör", "translation": "workplace atmosphere / office morale", "pos": "noun"},
            {"lemma": "önmegvalósítás", "translation": "self-realization, self-actualization", "pos": "noun"},
            {"lemma": "hűség", "translation": "loyalty, fidelity, dedication", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-26-05-voc.json", voc_05)

    # -------------------------------------------------------------------------
    # 2. Grammar Files (2 per regular lesson = 10 files)
    # -------------------------------------------------------------------------
    gr_01_a = {
        "id": "grammar.b1.26.01.vocation-and-calling",
        "title": "Expressing Vocation: hivatásának tekinti, szenteli magát",
        "sections": [
            {
                "type": "text",
                "title": "Verbal Expressions of Calling",
                "content": "*Hivatásának tekinti a munkáját* ('considers one's work a calling'), *a szakmának szenteli az életét* ('dedicates one's life to the profession'), *elmélyíti a szakértelmét* ('deepens one's expertise')."
            },
            {
                "type": "examples",
                "title": "Vocation in context",
                "items": [
                    {
                        "spanish": "Az orvos nem csupán pénzkeresetként, hanem valódi hivatásként tekint a munkájára.",
                        "english": "The doctor looks upon his work not merely as earning money, but as a true calling."
                    },
                    {
                        "spanish": "Hosszú és sikeres szakmai pályafutás áll a kutató mögött.",
                        "english": "A long and successful professional career path stands behind the researcher."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-26-01-a-gr.json", gr_01_a)

    gr_01_b = {
        "id": "grammar.b1.26.01.professional-qualifications",
        "title": "Skill and Competence: szakértelemmel végez, jártas vmiben",
        "sections": [
            {
                "type": "text",
                "title": "Describing Expertise",
                "content": "*Szakértelemmel látja el a feladatot* ('carries out the task with expertise'), *jártas a szakmában* ('is well-versed in the profession'), *kiváló minősítést szerez* ('obtains excellent qualification')."
            },
            {
                "type": "examples",
                "title": "Competence in practice",
                "items": [
                    {
                        "spanish": "A mérnökök lenyűgöző szakértelemmel tervezték meg az új hidat.",
                        "english": "The engineers designed the new bridge with impressive expertise."
                    },
                    {
                        "spanish": "Minden kollégánk magabiztosan jártas a modern digitális eszközök használatában.",
                        "english": "All our colleagues are confidently versed in using modern digital tools."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-26-01-b-gr.json", gr_01_b)

    gr_02_a = {
        "id": "grammar.b1.26.02.overtime-and-limits",
        "title": "Limits and Overburden: túlzásba visz, határt szab",
        "sections": [
            {
                "type": "text",
                "title": "Setting Healthy Boundaries",
                "content": "*Nem szabad túlzásba vinni a munkát* ('one must not overdo work'), *határt szab a túlórának* ('sets a limit to overtime'), *túlterheltség alatt roskadozik* ('is overburdened under excess workload')."
            },
            {
                "type": "examples",
                "title": "Setting boundaries",
                "items": [
                    {
                        "spanish": "Ha nem szabsz határt a túlórának, a folyamatos leterheltség kimerültséghez vezet.",
                        "english": "If you don't set a boundary to overtime, continuous workload leads to burnout."
                    },
                    {
                        "spanish": "Fontos felismerni a fáradtság jeleit, mielőtt túl késő lenne.",
                        "english": "It is important to recognize the signs of fatigue before it is too late."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-26-02-a-gr.json", gr_02_a)

    gr_02_b = {
        "id": "grammar.b1.26.02.recreation-and-recovery",
        "title": "Rest and Recharging: időt szán a pihenésre, feltöltődik",
        "sections": [
            {
                "type": "text",
                "title": "Recharging Idioms",
                "content": "*Időt szán a pihenésre* ('sets aside time for rest'), *energiával töltődik fel* ('recharges with energy'), *kikapcsolódik a barátokkal* ('unwinds with friends')."
            },
            {
                "type": "examples",
                "title": "Recreation in discourse",
                "items": [
                    {
                        "spanish": "A hétvégét a természetben töltötte, hogy feltöltődjön a következő hétre.",
                        "english": "He spent the weekend in nature in order to recharge for the next week."
                    },
                    {
                        "spanish": "A rendszeres kikapcsolódás elengedhetetlen a szellemi frissesség megőrzéséhez.",
                        "english": "Regular relaxation is essential for maintaining mental freshness."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-26-02-b-gr.json", gr_02_b)

    gr_03_a = {
        "id": "grammar.b1.26.03.work-life-balance",
        "title": "Work-Life Balance: megteremti az egyensúlyt, összeegyeztet",
        "sections": [
            {
                "type": "text",
                "title": "Harmonizing Demands",
                "content": "*Megteremti az egyensúlyt a munka és a magánélet között* ('creates balance between work and private life'), *összeegyezteti a kötelességeket a családdal* ('harmonizes obligations with family')."
            },
            {
                "type": "examples",
                "title": "Harmonizing domains",
                "items": [
                    {
                        "spanish": "Nehéz, de nem lehetetlen megteremteni az egyensúlyt a karrier és a család között.",
                        "english": "It is difficult, but not impossible, to create balance between career and family."
                    },
                    {
                        "spanish": "A rugalmas munkaidő sokat segít a napi teendők összeegyeztetésében.",
                        "english": "Flexible working hours help a lot in harmonizing daily tasks."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-26-03-a-gr.json", gr_03_a)

    gr_03_b = {
        "id": "grammar.b1.26.03.priorities-and-scheduling",
        "title": "Time Management: prioritást élvez, hatékonyan beoszt",
        "sections": [
            {
                "type": "text",
                "title": "Structuring Days",
                "content": "*Prioritást élvez* ('enjoys priority'), *elsőbbséget élvez* ('takes precedence'), *hatékonyan osztja be az idejét* ('schedules one's time efficiently')."
            },
            {
                "type": "examples",
                "title": "Time management in practice",
                "items": [
                    {
                        "spanish": "A sürgős feladatok mindig prioritást élveznek a napi beosztásban.",
                        "english": "Urgent tasks always enjoy priority in the daily schedule."
                    },
                    {
                        "spanish": "Aki megtanulja okosan beosztani az idejét, sokkal kevesebb stresszt él át.",
                        "english": "Whoever learns to allocate their time smartly experiences far less stress."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-26-03-b-gr.json", gr_03_b)

    gr_04_a = {
        "id": "grammar.b1.26.04.career-advancement",
        "title": "Aspiration & Advancement: törekszik vmire, érvényesül",
        "sections": [
            {
                "type": "text",
                "title": "Ambition Verbs",
                "content": "*Törekszik az előléptetésre* ('strives for promotion'), *érvényesül a munkaerőpiacon* ('succeeds / makes one's mark on the labor market'), *elismerést vív ki magának* ('earns recognition for oneself')."
            },
            {
                "type": "examples",
                "title": "Advancement phrases",
                "items": [
                    {
                        "spanish": "A tehetséges fiatal szakember gyorsan érvényesült a nemzetközi piacon.",
                        "english": "The talented young professional quickly made his mark on the international market."
                    },
                    {
                        "spanish": "A kitartó munka meghozta a méltó szakmai elismerést és az előléptetést.",
                        "english": "Persevering work brought worthy professional recognition and promotion."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-26-04-a-gr.json", gr_04_a)

    gr_04_b = {
        "id": "grammar.b1.26.04.recognition-and-reward",
        "title": "Recognition & Feedback: elismerésben részesül, méltatja a munkát",
        "sections": [
            {
                "type": "text",
                "title": "Appreciating Performance",
                "content": "*Elismerésben részesül* ('receives recognition'), *méltatja az elért eredményeket* ('praises the achieved results'), *jutalomban részesít* ('rewards')."
            },
            {
                "type": "examples",
                "title": "Feedback idioms",
                "items": [
                    {
                        "spanish": "A vezetőség nyilvánosan méltatta a csapat kiemelkedő éves teljesítményét.",
                        "english": "The management publicly praised the team's outstanding annual performance."
                    },
                    {
                        "spanish": "Az év végén a leglelkiismeretesebb dolgozók külön elismerésben részesültek.",
                        "english": "At the end of the year, the most conscientious workers received special recognition."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-26-04-b-gr.json", gr_04_b)

    gr_05_a = {
        "id": "grammar.b1.26.05.workplace-climate",
        "title": "Workplace Atmosphere: kellemes légkört teremt, támogatja a kollégákat",
        "sections": [
            {
                "type": "text",
                "title": "Office Morale",
                "content": "*Kellemes munkahelyi légkört teremt* ('creates pleasant workplace climate'), *támogató közösségben dolgozik* ('works in a supportive community'), *hozzájárul a jó hangulathoz* ('contributes to good morale')."
            },
            {
                "type": "examples",
                "title": "Climate in practice",
                "items": [
                    {
                        "spanish": "A barátságos munkahelyi légkör kulcsfontosságú a dolgozók elégedettségéhez.",
                        "english": "A friendly workplace atmosphere is key to employee satisfaction."
                    },
                    {
                        "spanish": "A kollégák önzetlenül segítették egymást a feszített határidők idején.",
                        "english": "Colleagues unselfishly helped one another during tight deadlines."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-26-05-a-gr.json", gr_05_a)

    gr_05_b = {
        "id": "grammar.b1.26.05.self-fulfillment-loyalty",
        "title": "Self-Actualization: örömét leli a munkában, hű marad az elveihez",
        "sections": [
            {
                "type": "text",
                "title": "Inner Fulfillment",
                "content": "*Örömét leli a feladatban* ('finds joy in the task'), *eléri az önmegvalósítást* ('achieves self-fulfillment'), *hű marad az értékeihez* ('remains faithful to one's values')."
            },
            {
                "type": "examples",
                "title": "Fulfillment discourse",
                "items": [
                    {
                        "spanish": "Akkor a legboldogabb az ember, ha az alkotásban leli örömét és önmegvalósítását.",
                        "english": "One is happiest when one finds joy and self-realization in creation."
                    },
                    {
                        "spanish": "A nehézségek ellenére mindvégig hű maradt a becsületéhez és hivatásához.",
                        "english": "Despite hardships, she remained faithful to her honor and vocation throughout."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-26-05-b-gr.json", gr_05_b)

    # -------------------------------------------------------------------------
    # 3. Exercise Files (01 to 05 + consolidation)
    # -------------------------------------------------------------------------
    ex_01 = {
        "lesson": "b1-26-01",
        "exercises": [
            {
                "id": "b1-26-01.ex01",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent a 'hivatás' szó a puszta munkahelyhez képest?",
                "options": [
                    "Olyan szakmai tevékenységet, amelyet valaki belső elhivatottságból, szívvel-lélekkel végez.",
                    "Egy ideiglenes diákmunkát a nyári szünetben.",
                    "A havi fizetési papír átvételét a pénztárnál."
                ],
                "correct": 0
            },
            {
                "id": "b1-26-01.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A tanárnő valódi hivatásá_____ tekinti a gyermekek oktatását és nevelését. (considers as her calling - nak)",
                "answer": "nak"
            },
            {
                "id": "b1-26-01.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "mérnök", "kiváló", "szakértelemmel", "tervezte", "meg", "az", "új", "házat."],
                "solution": ["A", "mérnök", "kiváló", "szakértelemmel", "tervezte", "meg", "az", "új", "házat."]
            },
            {
                "id": "b1-26-01.ex04",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent a 'szakértelem' kifejezés?",
                "options": [
                    "Egy adott szakmában szerzett alapos elméleti és gyakorlati tudást.",
                    "Egy idegen nyelvű szótár megvásárlását.",
                    "Egy irodai szék összeszerelésének idejét."
                ],
                "correct": 0
            },
            {
                "id": "b1-26-01.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "Hosszú és sikeres szakmai pálya_____ áll az elismert sebészorvos mögött. (career - futás)",
                "answer": "futás"
            },
            {
                "id": "b1-26-01.ex06",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik vonzattal áll a 'jártas' melléknév?",
                "options": [
                    "-ban / -ben (Jártas a pénzügyekben.)",
                    "-val / -vel (Jártas a pénzügyekkel.)",
                    "-ra / -re (Jártas a pénzügyekre.)"
                ],
                "correct": 0
            },
            {
                "id": "b1-26-01.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A fiatal kutató egész életét a tudománynak szente_____. (dedicated - lte)",
                "answer": "lte"
            },
            {
                "id": "b1-26-01.ex08",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "mély", "szakértelem", "és", "a", "hivatástudat", "a", "siker", "titka."],
                "solution": ["A", "mély", "szakértelem", "és", "a", "hivatástudat", "a", "siker", "titka."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-26-01-ex.json", ex_01)

    ex_02 = {
        "lesson": "b1-26-02",
        "exercises": [
            {
                "id": "b1-26-02.ex01",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mihez vezet a tartós leterheltség és a túl sok túlóra?",
                "options": [
                    "Fizikai és szellemi kimerültséghez, kiégéshez.",
                    "Azonnali sportbajnoki győzelemhez.",
                    "A szabadságos napok automatikus megduplázódásához."
                ],
                "correct": 0
            },
            {
                "id": "b1-26-02.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Fontos, hogy határt szabjunk a túlórának, és időt szánjunk a pihenés_____. (for rest - re)",
                "answer": "re"
            },
            {
                "id": "b1-26-02.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "hétvégi", "kiránduláson", "új", "energiával", "töltődött", "fel", "a", "család."],
                "solution": ["A", "hétvégi", "kiránduláson", "új", "energiával", "töltődött", "fel", "a", "család."]
            },
            {
                "id": "b1-26-02.ex04",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent a 'kimerültség' szó?",
                "options": [
                    "A szervezet testi és lelki energiatartalékainak súlyos elfogyását.",
                    "Egy vödör víz kiöntését a kertben.",
                    "A pontos érkezést a megbeszélésre."
                ],
                "correct": 0
            },
            {
                "id": "b1-26-02.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A megnövekedett leterhelts_____ miatt több munkatársat kellett felvenni. (workload - ég)",
                "answer": "ég"
            },
            {
                "id": "b1-26-02.ex06",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Hogyan fejezzük ki: 'One must not overdo work'?",
                "options": [
                    "Nem szabad túlzásba vinni a munkát.",
                    "Nem szabad túlzásba hozni a munkát.",
                    "Nem szabad túlzásba tenni a munkát."
                ],
                "correct": 0
            },
            {
                "id": "b1-26-02.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A dolgozóknak joguk van a rendszeres és nyugodt pihenés_____. (to rest - hez)",
                "answer": "hez"
            },
            {
                "id": "b1-26-02.ex08",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "rendszeres", "pihenés", "megelőzi", "a", "súlyos", "munkahelyi", "kimerültséget."],
                "solution": ["A", "rendszeres", "pihenés", "megelőzi", "a", "súlyos", "munkahelyi", "kimerültséget."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-26-02-ex.json", ex_02)

    ex_03 = {
        "lesson": "b1-26-03",
        "exercises": [
            {
                "id": "b1-26-03.ex01",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent az 'egyensúly' a munka és a magánélet viszonylatában?",
                "options": [
                    "Azt, hogy a szakmai kötelezettségek és a személyes élet egészséges összhangban vannak.",
                    "Azt, hogy a munkavállaló soha nem megy haza az irodából.",
                    "Egy mérleg használatát a laboratóriumban."
                ],
                "correct": 0
            },
            {
                "id": "b1-26-03.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A sürgős határidők mindig prioritást élvez_____ a napi feladatok között. (enjoy - nek)",
                "answer": "nek"
            },
            {
                "id": "b1-26-03.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "rugalmas", "munkaidő", "segít", "megteremteni", "a", "kívánt", "egyensúlyt."],
                "solution": ["A", "rugalmas", "munkaidő", "segít", "megteremteni", "a", "kívánt", "egyensúlyt."]
            },
            {
                "id": "b1-26-03.ex04",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mi az 'időbeosztás'?",
                "options": [
                    "A rendelkezésre álló idő tudatos és célszerű megtervezése.",
                    "A falióra felakasztása a falra.",
                    "Egy késés miatti hivatalos figyelmeztetés."
                ],
                "correct": 0
            },
            {
                "id": "b1-26-03.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A munkahelyi rugalmas_____ lehetővé teszi az otthoni munkavégzést is. (flexibility - ság)",
                "answer": "ság"
            },
            {
                "id": "b1-26-03.ex06",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Hogyan mondjuk: 'He manages his time efficiently'?",
                "options": [
                    "Hatékonyan osztja be az idejét.",
                    "Hatékonyan adja be az idejét.",
                    "Hatékonyan teszi fel az idejét."
                ],
                "correct": 0
            },
            {
                "id": "b1-26-03.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Meg kell tanulnunk összeegyeztetni a hivatást a család_____. (with family - val)",
                "answer": "val"
            },
            {
                "id": "b1-26-03.ex08",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "helyes", "prioritások", "felállítása", "megkönnyíti", "a", "mindennapi", "életet."],
                "solution": ["A", "helyes", "prioritások", "felállítása", "megkönnyíti", "a", "mindennapi", "életet."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-26-03-ex.json", ex_03)

    ex_04 = {
        "lesson": "b1-26-04",
        "exercises": [
            {
                "id": "b1-26-04.ex01",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent az 'ambíció' szó?",
                "options": [
                    "Erős törekvést a fejlődésre, magasabb célok elérésére, érvényesülésre.",
                    "A munkaidő előtti távozást a munkahelyről.",
                    "Egy unalmas feladat gépies elvégzését."
                ],
                "correct": 0
            },
            {
                "id": "b1-26-04.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A tehetséges mérnök komoly előléptetés_____ törekszik a vállalatnál. (strives for - re)",
                "answer": "re"
            },
            {
                "id": "b1-26-04.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "kitartó", "szorgalom", "meghozta", "a", "megérdemelt", "szakmai", "elismerést."],
                "solution": ["A", "kitartó", "szorgalom", "meghozta", "a", "megérdemelt", "szakmai", "elismerést."]
            },
            {
                "id": "b1-26-04.ex04",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit fejez ki az 'előléptetés'?",
                "options": [
                    "Magasabb pozícióba vagy rangba való kinevezést a munkahelyen.",
                    "Egy lépéssel előrébb állást a buszmegállóban.",
                    "A szerződés váratlan felbontását."
                ],
                "correct": 0
            },
            {
                "id": "b1-26-04.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A nemzetközi piacon való érvényesül_____ kitartó felkészülést igényel. (advancement - és)",
                "answer": "és"
            },
            {
                "id": "b1-26-04.ex06",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik kifejezés jelenti a munka elismerését?",
                "options": [
                    "Méltatja az elért eredményeket.",
                    "Kétségbe vonja a sikereket.",
                    "Elhallgatja a tényeket."
                ],
                "correct": 0
            },
            {
                "id": "b1-26-04.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Az év végén a kiemelkedő dolgozók pénzjutalomban része_____. (received - sültek)",
                "answer": "sültek"
            },
            {
                "id": "b1-26-04.ex08",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["Az", "egészséges", "ambíció", "előreviszi", "az", "egyéni", "karriert."],
                "solution": ["Az", "egészséges", "ambíció", "előreviszi", "az", "egyéni", "karriert."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-26-04-ex.json", ex_04)

    ex_05 = {
        "lesson": "b1-26-05",
        "exercises": [
            {
                "id": "b1-26-05.ex01",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent az 'önmegvalósítás' a karrierben?",
                "options": [
                    "Képességeink, tehetségünk és értékeink kiteljesítését az alkotó munkában.",
                    "Kizárólag a pénzügyi bevételek növelését minden áron.",
                    "Egy önéletrajz kinyomtatását a fénymásolóval."
                ],
                "correct": 0
            },
            {
                "id": "b1-26-05.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A dolgozó örömét leli a napi alkotó munka_____ és a feladatokban. (in the work - ban)",
                "answer": "ban"
            },
            {
                "id": "b1-26-05.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "támogató", "munkahelyi", "légkör", "növeli", "a", "dolgozók", "elégedettségét."],
                "solution": ["A", "támogató", "munkahelyi", "légkör", "növeli", "a", "dolgozók", "elégedettségét."]
            },
            {
                "id": "b1-26-05.ex04",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mi a 'munkahelyi légkör'?",
                "options": [
                    "A kollégák és vezetők közötti emberi hangulat, munkamorál és kapcsolatrendszer.",
                    "A szoba légkondicionáló berendezése által fújt hideg levegő.",
                    "Az ablakon beszűrődő utcai zaj mértéke."
                ],
                "correct": 0
            },
            {
                "id": "b1-26-05.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A hivatásához való hű_____ és a becsület mindennél fontosabb érték. (loyalty - ség)",
                "answer": "ség"
            },
            {
                "id": "b1-26-05.ex06",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Hogyan fejezzük ki: 'He remained faithful to his principles'?",
                "options": [
                    "Hű maradt az elveihez.",
                    "Hű maradt az elveivel.",
                    "Hű maradt az elveire."
                ],
                "correct": 0
            },
            {
                "id": "b1-26-05.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A magas fokú munkahelyi elégedett_____ növeli a cég iránti hűséget. (satisfaction - ség)",
                "answer": "ség"
            },
            {
                "id": "b1-26-05.ex08",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "valódi", "önmegvalósítás", "mély", "belső", "békét", "és", "örömöt", "ad."],
                "solution": ["A", "valódi", "önmegvalósítás", "mély", "belső", "békét", "és", "örömöt", "ad."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-26-05-ex.json", ex_05)

    ex_consolidation = {
        "lesson": "b1-26-consolidation",
        "exercises": [
            {
                "id": "b1-26-consolidation.ex01",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik kifejezés fejezi ki a munka és a magánélet harmonikus viszonyát?",
                "options": [
                    "Megteremti az egyensúlyt a hivatás és a család között.",
                    "Elhanyagolja a családját a karrierje miatt.",
                    "Feladja a hivatását az első nehézségnél."
                ],
                "correct": 0
            },
            {
                "id": "b1-26-consolidation.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Édes Anna fáradhatatlanul dolgozott, de a házaspár nem becsülte meg az emberi méltósá_____. (her dignity - gát)",
                "answer": "gát"
            },
            {
                "id": "b1-26-consolidation.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "szakértelem", "és", "az", "emberség", "együttesen", "teremtik", "meg", "a", "sikert."],
                "solution": ["A", "szakértelem", "és", "az", "emberség", "együttesen", "teremtik", "meg", "a", "sikert."]
            },
            {
                "id": "b1-26-consolidation.ex04",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A túlzott leterheltség és a pihenés hiánya súlyos kimerült_____ vezethet. (exhaustion - séghez)",
                "answer": "séghez"
            },
            {
                "id": "b1-26-consolidation.ex05",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "munkahelyi", "légkör", "alapvetően", "befolyásolja", "a", "mindennapi", "hangulatot."],
                "solution": ["A", "munkahelyi", "légkör", "alapvetően", "befolyásolja", "a", "mindennapi", "hangulatot."]
            },
            {
                "id": "b1-26-consolidation.ex06",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent az, ha valaki 'nem szab határt a munkának'?",
                "options": [
                    "Pihenés nélkül túlhajszolja magát, veszélyeztetve az egészségét.",
                    "Egy telekhatárra kerítést épít fel téglából.",
                    "Azonnal felmond az első munkanap után."
                ],
                "correct": 0
            },
            {
                "id": "b1-26-consolidation.ex07",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A tehetséges szakember előtt nyitva áll a gyors előléptet_____ lehetősége. (promotion - és)",
                "answer": "és"
            },
            {
                "id": "b1-26-consolidation.ex08",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Milyen mély emberi drámát ábrázol Kosztolányi Dezső 'Édes Anna' című regénye a munkáról és az egyensúlyról?",
                "options": [
                    "Azt a tragédiát, amikor a munkavállalót puszta dolognak, gépi munkaerőnek tekintik, megfosztva a pihenéstől és a méltóságtól.",
                    "A budapesti villamoshálózat technikai fejlesztésének költségvetési vitáját.",
                    "Egy gazdag kereskedőcsalád nyári velencei utazásának bonyodalmait."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-26-consolidation-ex.json", ex_consolidation)

    # -------------------------------------------------------------------------
    # 4. Classic Story Adaptation for Consolidation
    # -------------------------------------------------------------------------
    story_classic = {
        "id": "story.b1.26.classic",
        "title": "Édes Anna",
        "level": "B1",
        "order": 26,
        "type": "classics",
        "estimatedMinutes": 8,
        "summary": "An adaptation of Dezső Kosztolányi's masterpiece 'Édes Anna' (1926). Set in Budapest in the autumn of 1919, Anna arrives as a maid at the bourgeois Vizy household. Untiring, silent, and obedient, she works day and night without boundaries, keeping the apartment spotless. Yet while Mrs. Vizy boasts of her 'perfect machine', Anna's soul is crushed by the total absence of human warmth, rest, and personal balance—a haunting warning against treating human beings merely as working tools.",
        "characters": [
            "Édes Anna, a tiszta lelkű cselédlány",
            "Vizyné, a polgári úrasszony",
            "Moviszter doktor, a könyörületes orvos"
        ],
        "location": "Budapest, Krisztinaváros, a Vizy-ház lakása",
        "author": "Kosztolányi Dezső",
        "work": "Édes Anna (1926)",
        "paragraphs": [
            {
                "type": "narration",
                "text": "A krisztinavárosi polgári lakásban Vizyné büszkén mutatta körbe barátnőit a ragyogó szalonban. A parketta tükörként fénylett, a rézkilincsek csillogtak, a porcelánok katonás rendben sorakoztak a vitrinben. Mindez egyetlen ember keze munkáját dicsérte: Édes Annáét."
            },
            {
                "type": "dialogue",
                "speaker": "Vizyné",
                "text": "Nézzétek csak! Ez a lány nem ember, hanem valóságos kincs, egy tökéletes gépezet! Hajnaltól késő estig talpon van, nem kér szabadnapot, nem panaszkodik, és soha egyetlen szót sem szól vissza!"
            },
            {
                "type": "narration",
                "text": "Anna valóban szótlanul és fáradhatatlan hűséggel végezte a legsúlyosabb munkát is. Ám a látszólagos rend mögött a lány lelke napról napra sorvadt. Nem volt saját élete, nem voltak határok a munka és a pihenés között. Az úri ház hideg ridegsége megfosztotta a legalapvetőbb emberi melegtől."
            },
            {
                "type": "dialogue",
                "speaker": "Moviszter doktor",
                "text": "Nagyságos asszonyom, figyelmeztetem: az ember nem gép! Minden léleknek szüksége van elismerésre, pihenésre és meleg szóra. Ha valakitől csak követelnek, de semmit sem adnak cserébe, az egyensúly felborul, és a lélek elpusztul."
            },
            {
                "type": "narration",
                "text": "A figyelmeztetés süket fülekre talált. Anna belső világa végzetesen kimerült a szüntelen túlterheltségben. Kosztolányi halhatatlan regénye a magyar irodalom legmegrázóbb kiáltása maradt: az emberi méltóság és a lelki egyensúly nem áldozható fel a munka oltárán."
            }
        ]
    }
    write_json("content/hu/stories/classics/b1/b1-26-kosztolanyi.json", story_classic)

    # -------------------------------------------------------------------------
    # 5. Lesson Files (01 to 05 + consolidation)
    # -------------------------------------------------------------------------
    for i in range(1, 6):
        padded = f"0{i}"
        titles = {
            "01": ("Vocation & Calling", "Hivatás és szakértelem: Karrier és szakmai életút"),
            "02": ("Workload and Limits", "Túlóra és kimerültség: Határok és a pihenés fontossága"),
            "03": ("Finding Balance", "Egyensúly és prioritások: Munka és magánélet összhangja"),
            "04": ("Ambition & Recognition", "Ambíció és elismerés: Szakmai érvényesülés és előléptetés"),
            "05": ("Workplace & Fulfillment", "Munkahelyi légkör és önmegvalósítás: Elégedettség és hűség")
        }
        en_title, hu_title = titles[padded]
        lesson_data = {
            "id": f"lesson.b1.26-{padded}",
            "unit": 26,
            "title": en_title,
            "level": "B1",
            "grammar": "Work-Life Balance Idioms, Professional Boundary Markers & Career Discourse",
            "goal": [
                f"I can understand and use vocabulary for {en_title.lower()}.",
                "I can discuss career aspirations, professional expertise, and workloads in Hungarian.",
                "I can express strategies for maintaining healthy work-life balance and preventing burnout.",
                "I can master four new target vocabulary items in authentic context."
            ],
            "sections": [
                {
                    "type": "goal",
                    "title": "Lesson Goals",
                    "items": [
                        f"I can understand and use vocabulary for {en_title.lower()}.",
                        "I can discuss career aspirations, professional expertise, and workloads in Hungarian.",
                        "I can express strategies for maintaining healthy work-life balance and preventing burnout.",
                        "I can master four new target vocabulary items in authentic context."
                    ]
                },
                {"type": "recycle", "title": "Quick Review"},
                {"type": "grammar", "ref": f"grammar/b1/b1-26-{padded}-a-gr.json"},
                {"type": "grammar", "ref": f"grammar/b1/b1-26-{padded}-b-gr.json"},
                {"type": "vocabulary", "title": "Lesson Vocabulary", "ref": f"vocabulary/b1/b1-26-{padded}-voc.json"},
                {
                    "type": "exercise-group",
                    "title": "Practice",
                    "ref": f"exercises/b1/b1-26-{padded}-ex.json",
                    "exerciseRefs": [f"b1-26-{padded}.ex0{k}" for k in range(1, 9)]
                }
            ]
        }
        write_json(f"content/hu/lessons/b1/b1-26-{padded}.json", lesson_data)

    consolidation_data = {
        "id": "lesson.b1.26-consolidation",
        "unit": 26,
        "title": "Unit 26 Consolidation",
        "level": "B1",
        "grammar": "Consolidation of Career Discourse, Work-Life Boundaries & Personal Dignity",
        "sections": [
            {
                "type": "story",
                "title": "Édes Anna (Kosztolányi Dezső)",
                "ref": "stories/classics/b1/b1-26-kosztolanyi.json"
            },
            {
                "type": "exercise-group",
                "title": "Consolidation Practice",
                "ref": "exercises/b1/b1-26-consolidation-ex.json",
                "exerciseRefs": [f"b1-26-consolidation.ex0{k}" for k in range(1, 9)]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-26-consolidation.json", consolidation_data)
    print("Successfully built Hungarian B1 Core Unit 26 (b1-26)!")

if __name__ == "__main__":
    build_unit_26_core()
