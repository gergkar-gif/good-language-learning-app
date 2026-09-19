#!/usr/bin/env python3
"""Generate Hungarian B1 Core Unit 9: Health & Wellbeing (b1-09)."""

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

def build_unit_9_core():
    # -------------------------------------------------------------------------
    # 1. Vocabulary Files (4 words each = 20 words total)
    # -------------------------------------------------------------------------
    voc_01 = {
        "id": "vocab.b1.09.01",
        "lesson": "b1-09-01",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "életmód", "translation": "lifestyle", "pos": "noun"},
            {"lemma": "táplálkozás", "translation": "nutrition, diet", "pos": "noun"},
            {"lemma": "megelőzés", "translation": "prevention", "pos": "noun"},
            {"lemma": "szervezet", "translation": "organism, body", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-09-01-voc.json", voc_01)

    voc_02 = {
        "id": "vocab.b1.09.02",
        "lesson": "b1-09-02",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "káros", "translation": "harmful, detrimental", "pos": "adjective"},
            {"lemma": "szokás", "translation": "habit, custom", "pos": "noun"},
            {"lemma": "mérték", "translation": "measure, moderation", "pos": "noun"},
            {"lemma": "fogyasztás", "translation": "consumption", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-09-02-voc.json", voc_02)

    voc_03 = {
        "id": "vocab.b1.09.03",
        "lesson": "b1-09-03",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "panasz", "translation": "symptom, medical complaint", "pos": "noun"},
            {"lemma": "vizsgálat", "translation": "examination, checkup", "pos": "noun"},
            {"lemma": "recept", "translation": "prescription, recipe", "pos": "noun"},
            {"lemma": "gyógyszertár", "translation": "pharmacy, chemist's", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-09-03-voc.json", voc_03)

    voc_04 = {
        "id": "vocab.b1.09.04",
        "lesson": "b1-09-04",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "feszültség", "translation": "tension, stress", "pos": "noun"},
            {"lemma": "egyensúly", "translation": "balance, equilibrium", "pos": "noun"},
            {"lemma": "pihenés", "translation": "rest, relaxation", "pos": "noun"},
            {"lemma": "levezetés", "translation": "winding down, releasing (stress)", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-09-04-voc.json", voc_04)

    voc_05 = {
        "id": "vocab.b1.09.05",
        "lesson": "b1-09-05",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "jóllét", "translation": "wellbeing", "pos": "noun"},
            {"lemma": "egészséges", "translation": "healthy", "pos": "adjective"},
            {"lemma": "kezelés", "translation": "treatment, medical therapy", "pos": "noun"},
            {"lemma": "gyógyulás", "translation": "recovery, healing", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-09-05-voc.json", voc_05)

    # -------------------------------------------------------------------------
    # 2. Grammar Files
    # -------------------------------------------------------------------------
    gr_01_a = {
        "id": "grammar.b1.09.01.general-subject-ember",
        "title": "General Impersonal Subject: az ember",
        "sections": [
            {
                "type": "text",
                "title": "Expressing generalized truths and rules with 'az ember'",
                "content": "To speak about people in general, general human experience, or common rules ('one should...', 'you ought to...'), Hungarian frequently uses *az ember* with third-person singular verbs. It corresponds to English generic 'one' or generalized 'you'."
            },
            {
                "type": "examples",
                "title": "Generic human experience",
                "items": [
                    {
                        "spanish": "Ha az ember fáradt, nehezebben tud összpontosítani.",
                        "english": "When one is tired, one can concentrate with greater difficulty."
                    },
                    {
                        "spanish": "Az embernek oda kell figyelnie a mindennapi táplálkozásra.",
                        "english": "One must pay attention to daily nutrition."
                    },
                    {
                        "spanish": "A rendszeres testmozgással az ember megelőzheti a betegségeket.",
                        "english": "With regular exercise, one can prevent illnesses."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-09-01-a-gr.json", gr_01_a)

    gr_01_b = {
        "id": "grammar.b1.09.01.modal-kell-lehet",
        "title": "The Modal System: kell, lehet, muszáj",
        "sections": [
            {
                "type": "text",
                "title": "Necessity and possibility in health advice",
                "content": "Modals like *kell* (must / have to), *lehet* (can / may / is possible), and *muszáj* (compulsory / must) take a dative subject (*-nak / -nek*) and an infinitive."
            },
            {
                "type": "examples",
                "title": "Modal health advice",
                "items": [
                    {
                        "spanish": "Sok vizet kell inni a meleg nyári napokon.",
                        "english": "One must drink plenty of water on hot summer days."
                    },
                    {
                        "spanish": "A rendelőben bejelentkezés nélkül is lehet orvossal beszélni.",
                        "english": "In the surgery, one can speak with a doctor even without an appointment."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-09-01-b-gr.json", gr_01_b)

    gr_02 = {
        "id": "grammar.b1.09.02.szabad-tilos",
        "title": "Permissions & Prohibitions: szabad, tilos, nem szabad",
        "sections": [
            {
                "type": "text",
                "title": "Stating health prohibitions and permissions",
                "content": "*Szabad* indicates permission ('is allowed'), while *tilos* or *nem szabad* indicates strict prohibition ('forbidden / not permitted'). Both govern the infinitive."
            },
            {
                "type": "examples",
                "title": "Prohibition and permission in practice",
                "items": [
                    {
                        "spanish": "A kórházban szigorúan tilos a dohányzás.",
                        "english": "In the hospital, smoking is strictly forbidden."
                    },
                    {
                        "spanish": "Gyógyszerszedés mellett nem szabad alkoholt fogyasztani.",
                        "english": "Along with taking medication, it is not permitted to consume alcohol."
                    },
                    {
                        "spanish": "Lázas állapotban szabad sokat pihenni és aludni.",
                        "english": "In a feverish state, one is permitted (and advised) to rest and sleep a lot."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-09-02-gr.json", gr_02)

    gr_03 = {
        "id": "grammar.b1.09.03.doctor-collocations",
        "title": "Medical Checkups & Symptoms: panaszkodik, felír, kivált",
        "sections": [
            {
                "type": "text",
                "title": "At the doctor's and the pharmacy",
                "content": "Key medical collocations include: *panaszkodik vmire* (to complain of a symptom, sublative *-ra / -re*), *receptet felír* (to write a prescription), and *gyógyszert kivált* (to pick up / fill a prescription at the pharmacy)."
            },
            {
                "type": "examples",
                "title": "Clinic collocations",
                "items": [
                    {
                        "spanish": "A beteg erős fejfájásra panaszkodott a háziorvosnak.",
                        "english": "The patient complained of a severe headache to the general practitioner."
                    },
                    {
                        "spanish": "Az orvos antibiotikumot írt fel a fertőzésre.",
                        "english": "The doctor prescribed antibiotics for the infection."
                    },
                    {
                        "spanish": "A legközelebbi gyógyszertárban váltottam ki a gyógyszert.",
                        "english": "I picked up the medication in the nearest pharmacy."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-09-03-gr.json", gr_03)

    gr_04 = {
        "id": "grammar.b1.09.04.stress-and-balance",
        "title": "Emotional & Physical Wellbeing: feszültséget levezet, egyensúlyt tart",
        "sections": [
            {
                "type": "text",
                "title": "Handling mental balance and stress",
                "content": "Verbal collocations for wellness include *feszültséget levezet* (to relieve / release tension), *megtalálja az egyensúlyt* (to find one's balance), and *kikapcsolódik* (to unwind / switch off)."
            },
            {
                "type": "examples",
                "title": "Stress and balance expressions",
                "items": [
                    {
                        "spanish": "A sport és a séta segít levezetni a napi feszültséget.",
                        "english": "Sports and walking help to release daily tension."
                    },
                    {
                        "spanish": "Nehéz megtalálni az egyensúlyt a munka és a magánélet között.",
                        "english": "It is difficult to find the balance between work and private life."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-09-04-gr.json", gr_04)

    gr_05 = {
        "id": "grammar.b1.09.05.health-advice-synthesis",
        "title": "Synthesizing Health Advice: érdemes, ajánlott, tanácsos",
        "sections": [
            {
                "type": "text",
                "title": "Gentle advisory predicates with infinitives",
                "content": "To offer courteous and natural health recommendations, Hungarian uses impersonal adjectives followed by the infinitive: *érdemes* (it is worthwhile), *ajánlott* (it is recommended), and *tanácsos* (it is advisable)."
            },
            {
                "type": "examples",
                "title": "Advisory structures",
                "items": [
                    {
                        "spanish": "Évente legalább egyszer érdemes elmenni orvosi vizsgálatra.",
                        "english": "At least once a year, it is worthwhile to go for a medical checkup."
                    },
                    {
                        "spanish": "A gyors gyógyulás érdekében ajánlott ágyban maradni.",
                        "english": "In the interest of rapid recovery, it is recommended to stay in bed."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-09-05-gr.json", gr_05)

    # -------------------------------------------------------------------------
    # 3. Classic Reading: Kosztolányi Dezső: Esti Kornél
    # -------------------------------------------------------------------------
    classic_09 = {
        "id": "story.b1.09.classic",
        "title": "Esti Kornél és az orvosi vizsgálat",
        "level": "B1",
        "lesson": 5,
        "order": 5,
        "type": "classics",
        "estimatedMinutes": 6,
        "characters": ["Esti Kornél", "A professzor úr"],
        "grammar": ["general-subject-ember", "doctor-collocations", "health-advice-synthesis"],
        "vocabularyTopics": ["health", "doctor", "wellbeing", "philosophy"],
        "summary": "An adapted retelling inspired by Dezső Kosztolányi's witty literary masterpiece Esti Kornél: Esti visits an elderly, experienced professor for a medical checkup, reflecting on human vulnerability, the art of reassurance, and the profound connection between bodily health and peace of mind.",
        "source": "Adaptation inspired by the public-domain work Esti Kornél by Dezső Kosztolányi",
        "author": "Dezső Kosztolányi",
        "work": "Esti Kornél",
        "paragraphs": [
            {
                "type": "narration",
                "text": "Esti Kornél egy ködös, hűvös novemberi délelőttön lépett be a híres belgyógyász professzor tágas, csendes várószobájába. Az ember ilyen helyen mindig akaratlanul elcsendesedik: a fehér falak és a gyógyszerszag emlékeztetik a test törékenységére."
            },
            {
                "type": "narration",
                "text": "„Fáradjon be, kedves uram!” — szólt ki a professzor az ajtóból. Hófehér hajú, derűs tekintetű idős orvos volt, aki évtizedek óta vizsgálta az emberek szívét és lelkét. Esti leült az íróasztallal szemközti kényelmes bőrfotelbe."
            },
            {
                "type": "narration",
                "text": "„Nos, mi a panasza? Mire panaszkodik?” — kérdezte az orvos szelíden. Esti elmosolyodott, megigazította a nyakkendőjét: „Igazából semmire, professzor úr... vagy talán mindenre. Néha túl gyorsan ver a szívem, néha fáradt vagyok, és úgy érzem, felborult bennem a belső egyensúly.”"
            },
            {
                "type": "narration",
                "text": "A professzor felvette a sztetoszkópot, és gondos alapossággal megvizsgálta Esti mellkasát és hátát. Megmérte a vérnyomását, és megnézte a pulzusát. Esti feszülten várta a diagnózist: vajon milyen súlyos betegséget fedez fel a tapasztalt tudós?"
            },
            {
                "type": "narration",
                "text": "Az orvos azonban lassan letette a műszert, levette a pápaszemét, és barátságosan ránézett: „Kedves barátom, a szervezete teljesen egészséges. A szíve pontos, mint a svájci óra. Magának nem erős gyógyszerek kellenek a gyógyszertárból, hanem sokkal inkább nyugodt pihenés, kevesebb éjszakai kávé és több séta a fák alatt.”"
            },
            {
                "type": "narration",
                "text": "Esti megkönnyebbülten sóhajtott fel, és zsebre tette a papírt, amelyre az orvos csupán ennyit írt: 'Napi két óra séta és belső béke.' Ahogy kilépett az őszi utcára, a levegő frissnek tűnt, és úgy érezte, a valódi gyógyulás nem a patikában kezdődik, hanem a gondolataink tisztaságában."
            }
        ]
    }
    write_json("content/hu/stories/classics/b1/b1-09-estikornel.json", classic_09)

    # -------------------------------------------------------------------------
    # 4. Exercise Files
    # -------------------------------------------------------------------------
    ex_01 = {
        "lesson": "b1-09-01",
        "exercises": [
            {
                "id": "b1-09-01-intro-1",
                "type": "multiple-choice",
                "category": "introduce",
                "question": "Which noun phrase expresses generic 'one' or 'people in general'?",
                "options": ["az ember", "az autó", "a ház"],
                "correct": 0,
                "teaches": ["general-subject-ember"]
            },
            {
                "id": "b1-09-01-intro-2",
                "type": "multiple-choice",
                "category": "introduce",
                "question": "What is 'megelőzés' in healthcare?",
                "options": ["prevention", "surgery", "prescription"],
                "correct": 0,
                "teaches": ["vocab-megelozes"]
            },
            {
                "id": "b1-09-01-controlled-1",
                "type": "matching",
                "category": "controlled",
                "pairs": [
                    ["életmód", "lifestyle"],
                    ["táplálkozás", "nutrition / diet"],
                    ["megelőzés", "prevention"],
                    ["szervezet", "organism / body"]
                ],
                "teaches": ["vocab-lifestyle"]
            },
            {
                "id": "b1-09-01-controlled-2",
                "type": "multiple-choice",
                "category": "controlled",
                "question": "Ha fáradt az ember, sokat ... aludnia.",
                "options": ["kell", "tilos", "szabad"],
                "correct": 0,
                "teaches": ["modal-kell"]
            },
            {
                "id": "b1-09-01-controlled-3",
                "type": "fill-blank",
                "category": "controlled",
                "sentence": "A rendszeres testmozgás erősíti az emberi ____. (body / organism)",
                "answer": "szervezetet",
                "teaches": ["szervezet-usage"]
            },
            {
                "id": "b1-09-01-controlled-4",
                "type": "multiple-choice",
                "category": "controlled",
                "question": "Which sentence expresses healthy living?",
                "options": [
                    "Az egészséges életmódhoz a helyes táplálkozás is hozzátartozik.",
                    "Az ember soha nem alszik éjszaka.",
                    "A betegség jobb, mint a megelőzés."
                ],
                "correct": 0,
                "teaches": ["health-concept"]
            },
            {
                "id": "b1-09-01-practice-1",
                "type": "matching",
                "category": "practice",
                "pairs": [
                    ["egészséges életmód", "healthy lifestyle"],
                    ["kiegyensúlyozott táplálkozás", "balanced nutrition"],
                    ["a betegségek megelőzése", "prevention of diseases"],
                    ["az emberi szervezet", "the human body"]
                ],
                "teaches": ["health-collocations"]
            },
            {
                "id": "b1-09-01-practice-2",
                "type": "multiple-choice",
                "category": "practice",
                "question": "Miért fontos a megelőzés az orvostudományban?",
                "options": [
                    "Mert könnyebb megelőzni a bajt, mint gyógyítani a súlyos betegséget.",
                    "Mert a gyógyszerek ingyen vannak.",
                    "Mert senki nem szeret orvoshoz járni."
                ],
                "correct": 0,
                "teaches": ["prevention-reading"]
            },
            {
                "id": "b1-09-01-practice-3",
                "type": "fill-blank",
                "category": "practice",
                "sentence": "A zöldségek és gyümölcsök fontos szerepet játszanak az egészséges ____. (nutrition / inessive)",
                "answer": "táplálkozásban",
                "teaches": ["taplalkozas-case"]
            },
            {
                "id": "b1-09-01-practice-4",
                "type": "multiple-choice",
                "category": "practice",
                "question": "Mit jelent: 'Az embernek vigyáznia kell az egészségére'?",
                "options": [
                    "One must take care of one's health.",
                    "People do not care about health.",
                    "Doctors are always busy."
                ],
                "correct": 0,
                "teaches": ["az-embernek-translation"]
            },
            {
                "id": "b1-09-01-dialogue-1",
                "type": "multiple-choice",
                "category": "dialogue",
                "question": "— Mit teszel az egészséged megőrzéséért?\n— ...",
                "options": [
                    "Figyelek a táplálkozásra és heti háromszor úszni járok.",
                    "Tegnap megnéztem a menetrendet a pályaudvaron.",
                    "Nem vettem új cipőt a boltban."
                ],
                "correct": 0,
                "teaches": ["health-dialogue-1"]
            },
            {
                "id": "b1-09-01-dialogue-2",
                "type": "multiple-choice",
                "category": "dialogue",
                "question": "— Nem érzed magad fáradtnak mostanában?\n— ...",
                "options": [
                    "De igen, úgy érzem, az embernek néha kötelező pihennie.",
                    "A vonat tíz percet késett tegnap.",
                    "Nem szeretem az esős őszi napokat."
                ],
                "correct": 0,
                "teaches": ["health-dialogue-2"]
            },
            {
                "id": "b1-09-01-writing-1",
                "type": "multiple-choice",
                "category": "production",
                "question": "How do you say: 'Prevention is better than cure.'?",
                "options": [
                    "A megelőzés jobb, mint a gyógyítás.",
                    "A betegség gyorsabban jön, mint a megelőzés.",
                    "Az orvos gyógyszert írt fel reggel."
                ],
                "correct": 0,
                "teaches": ["production-prevention"]
            },
            {
                "id": "b1-09-01-writing-2",
                "type": "multiple-choice",
                "category": "production",
                "question": "How do you say: 'One must drink plenty of fluids.'?",
                "options": [
                    "Az embernek sok folyadékot kell innia.",
                    "Az ember folyadékot ivott tegnap este.",
                    "Folyadék nélkül utazunk Szegedre."
                ],
                "correct": 0,
                "teaches": ["production-modals"]
            },
            {
                "id": "b1-09-01-check-1",
                "type": "multiple-choice",
                "category": "check",
                "question": "What does 'életmód' mean?",
                "options": ["lifestyle", "lifelong", "lifetime"],
                "correct": 0,
                "teaches": ["check-eletmod"]
            },
            {
                "id": "b1-09-01-check-2",
                "type": "multiple-choice",
                "category": "check",
                "question": "Complete: 'Az embernek figyelnie ...' (must / has to)",
                "options": ["kell", "tilos", "szabad"],
                "correct": 0,
                "teaches": ["check-kell"]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-09-01-ex.json", ex_01)

    ex_02 = {
        "lesson": "b1-09-02",
        "exercises": [
            {
                "id": "b1-09-02-intro-1",
                "type": "multiple-choice",
                "category": "introduce",
                "question": "What is the difference between 'szabad' and 'tilos'?",
                "options": ["allowed vs forbidden", "easy vs hard", "healthy vs sick"],
                "correct": 0,
                "teaches": ["szabad-tilos-intro"]
            },
            {
                "id": "b1-09-02-intro-2",
                "type": "multiple-choice",
                "category": "introduce",
                "question": "What does 'káros szokás' mean?",
                "options": ["harmful habit", "good hobby", "daily meal"],
                "correct": 0,
                "teaches": ["vocab-karos-szokas"]
            },
            {
                "id": "b1-09-02-controlled-1",
                "type": "matching",
                "category": "controlled",
                "pairs": [
                    ["káros", "harmful, detrimental"],
                    ["szokás", "habit, custom"],
                    ["mérték", "measure, moderation"],
                    ["fogyasztás", "consumption"]
                ],
                "teaches": ["vocab-moderation"]
            },
            {
                "id": "b1-09-02-controlled-2",
                "type": "multiple-choice",
                "category": "controlled",
                "question": "A kórház épületében szigorúan ... a dohányzás.",
                "options": ["tilos", "szabad", "kell"],
                "correct": 0,
                "teaches": ["tilos-usage"]
            },
            {
                "id": "b1-09-02-controlled-3",
                "type": "fill-blank",
                "category": "controlled",
                "sentence": "A túlzott cukorfogyasztás rendkívül ____ az egészségre. (harmful)",
                "answer": "káros",
                "teaches": ["karos-context"]
            },
            {
                "id": "b1-09-02-controlled-4",
                "type": "multiple-choice",
                "category": "controlled",
                "question": "Which sentence expresses moderation?",
                "options": [
                    "A táplálkozásban minden dologban a mérték a legfontosabb.",
                    "Bármennyi cukrot szabad enni korlátlanul.",
                    "A dohányzás nem káros semmire."
                ],
                "correct": 0,
                "teaches": ["mertek-concept"]
            },
            {
                "id": "b1-09-02-practice-1",
                "type": "matching",
                "category": "practice",
                "pairs": [
                    ["káros szenvedély", "harmful addiction"],
                    ["helyes mérték", "proper moderation / measure"],
                    ["túlzott fogyasztás", "excessive consumption"],
                    ["egészséges szokások", "healthy habits"]
                ],
                "teaches": ["moderation-phrases"]
            },
            {
                "id": "b1-09-02-practice-2",
                "type": "multiple-choice",
                "category": "practice",
                "question": "Mit jelent az, hogy 'Mértékkel fogyaszd!'?",
                "options": ["Consume it in moderation!", "Do not buy it!", "Eat as much as possible!"],
                "correct": 0,
                "teaches": ["mertekkel-reading"]
            },
            {
                "id": "b1-09-02-practice-3",
                "type": "fill-blank",
                "category": "practice",
                "sentence": "A rossz ____ nehéz lemondani, de érdemes megpróbálni. (habits / delative)",
                "answer": "szokásokról",
                "teaches": ["szokasokrol-case"]
            },
            {
                "id": "b1-09-02-practice-4",
                "type": "multiple-choice",
                "category": "practice",
                "question": "Mit jelent: 'Itt nem szabad leülni'?",
                "options": ["It is not allowed to sit here.", "One must sit here.", "Please take a seat."],
                "correct": 0,
                "teaches": ["nem-szabad-translation"]
            },
            {
                "id": "b1-09-02-dialogue-1",
                "type": "multiple-choice",
                "category": "dialogue",
                "question": "— Szabad itt rágyújtani a teraszon?\n— ...",
                "options": [
                    "Sajnos nem, az egész területen tilos a dohányzás.",
                    "Igen, tegnap vettem egy új táskát.",
                    "A busz pontosan érkezett a megállóba."
                ],
                "correct": 0,
                "teaches": ["smoking-dialogue"]
            },
            {
                "id": "b1-09-02-dialogue-2",
                "type": "multiple-choice",
                "category": "dialogue",
                "question": "— Hogyan tudtál leszokni a sok kávéról?\n— ...",
                "options": [
                    "Fokozatosan csökkentettem a napi fogyasztást és gyógyteát ittam.",
                    "Nem találtam meg a szemüvegemet reggel.",
                    "A múzeum hétfőnként zárva tart."
                ],
                "correct": 0,
                "teaches": ["habit-change-dialogue"]
            },
            {
                "id": "b1-09-02-writing-1",
                "type": "multiple-choice",
                "category": "production",
                "question": "How do you say: 'Excessive salt consumption is harmful.'?",
                "options": [
                    "A túlzott sófogyasztás káros a szervezetre.",
                    "A sófogyasztás soha nem árt senkinek.",
                    "Sót vettem a boltban délután."
                ],
                "correct": 0,
                "teaches": ["production-karos"]
            },
            {
                "id": "b1-09-02-writing-2",
                "type": "multiple-choice",
                "category": "production",
                "question": "How do you say: 'Smoking is strictly prohibited.'?",
                "options": [
                    "A dohányzás szigorúan tilos.",
                    "A dohányzás mindenhol szabad.",
                    "Nem dohányoztam a múlt héten."
                ],
                "correct": 0,
                "teaches": ["production-tilos"]
            },
            {
                "id": "b1-09-02-check-1",
                "type": "multiple-choice",
                "category": "check",
                "question": "Which word means 'forbidden'?",
                "options": ["tilos", "szabad", "lehet"],
                "correct": 0,
                "teaches": ["check-tilos"]
            },
            {
                "id": "b1-09-02-check-2",
                "type": "multiple-choice",
                "category": "check",
                "question": "What is 'fogyasztás'?",
                "options": ["consumption", "weight loss", "production"],
                "correct": 0,
                "teaches": ["check-fogyasztas"]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-09-02-ex.json", ex_02)

    ex_03 = {
        "lesson": "b1-09-03",
        "exercises": [
            {
                "id": "b1-09-03-intro-1",
                "type": "multiple-choice",
                "category": "introduce",
                "question": "Which case does 'panaszkodik' (to complain of a symptom) take?",
                "options": ["sublative (-ra / -re)", "inessive (-ban / -ben)", "instrumental (-val / -vel)"],
                "correct": 0,
                "teaches": ["case-panaszkodik"]
            },
            {
                "id": "b1-09-03-intro-2",
                "type": "multiple-choice",
                "category": "introduce",
                "question": "What does an Hungarian doctor do with a 'recept'?",
                "options": ["felírja (prescribes it)", "megeszi", "eltépi"],
                "correct": 0,
                "teaches": ["vocab-felir-recept"]
            },
            {
                "id": "b1-09-03-controlled-1",
                "type": "matching",
                "category": "controlled",
                "pairs": [
                    ["panasz", "symptom / complaint"],
                    ["vizsgálat", "medical examination"],
                    ["recept", "prescription"],
                    ["gyógyszertár", "pharmacy"]
                ],
                "teaches": ["vocab-clinic"]
            },
            {
                "id": "b1-09-03-controlled-2",
                "type": "multiple-choice",
                "category": "controlled",
                "question": "A beteg magas lázra és köhögésre ...",
                "options": ["panaszkodott.", "receptezett.", "vizsgált."],
                "correct": 0,
                "teaches": ["panaszkodik-usage"]
            },
            {
                "id": "b1-09-03-controlled-3",
                "type": "fill-blank",
                "category": "controlled",
                "sentence": "Az orvos alapos ____ után felírt egy hatékony gyógyszert. (examination / nom)",
                "answer": "vizsgálat",
                "teaches": ["vizsgalat-context"]
            },
            {
                "id": "b1-09-03-controlled-4",
                "type": "multiple-choice",
                "category": "controlled",
                "question": "Hol lehet kiváltani a felírt orvosságot?",
                "options": ["A legközelebbi gyógyszertárban.", "A postán.", "A könyvtárban."],
                "correct": 0,
                "teaches": ["pharmacy-comprehension"]
            },
            {
                "id": "b1-09-03-practice-1",
                "type": "matching",
                "category": "practice",
                "pairs": [
                    ["orvosi vizsgálat", "medical examination"],
                    ["receptet felír", "to prescribe medication"],
                    ["gyógyszert kivált", "to pick up prescription"],
                    ["panaszt meghallgat", "to listen to complaints"]
                ],
                "teaches": ["medical-collocations"]
            },
            {
                "id": "b1-09-03-practice-2",
                "type": "multiple-choice",
                "category": "practice",
                "question": "Mit kérdez a háziorvos a rendelőben legelőször?",
                "options": [
                    "„Mi a panasza? Hol fáj?”",
                    "„Mikor utazik Bécsbe?”",
                    "„Mennyi pénz van a pénztárcájában?”"
                ],
                "correct": 0,
                "teaches": ["clinic-dialogue-reading"]
            },
            {
                "id": "b1-09-03-practice-3",
                "type": "fill-blank",
                "category": "practice",
                "sentence": "A háziorvos erős antibiotikumot írt fel a fertőzésre a ____. (on the prescription)",
                "answer": "receptre",
                "teaches": ["receptre-case"]
            },
            {
                "id": "b1-09-03-practice-4",
                "type": "multiple-choice",
                "category": "practice",
                "question": "Mit jelent a 'gyógyszerkiváltás'?",
                "options": [
                    "Filling / picking up a prescription at the pharmacy.",
                    "Taking pills with water.",
                    "Cancelling an appointment."
                ],
                "correct": 0,
                "teaches": ["kivaltas-translation"]
            },
            {
                "id": "b1-09-03-dialogue-1",
                "type": "multiple-choice",
                "category": "dialogue",
                "question": "— Jó napot kívánok, doktor úr! Napok óta fáj a torkom.\n— ...",
                "options": [
                    "Nyissa ki a száját, kérem, megvizsgálom a torkát!",
                    "A vonat mindjárt indul a hármas vágányról.",
                    "Nem ettem tegnap ebédet."
                ],
                "correct": 0,
                "teaches": ["doctor-patient-dialogue"]
            },
            {
                "id": "b1-09-03-dialogue-2",
                "type": "multiple-choice",
                "category": "dialogue",
                "question": "— Hol van itt a legközelebbi gyógyszertár?\n— ...",
                "options": [
                    "A sarkon túl, a posta mellett van egy éjjel-nappali patika.",
                    "Nem szeretem az esős délutánokat.",
                    "A könyvet a könyvtárból kölcsönöztem."
                ],
                "correct": 0,
                "teaches": ["pharmacy-direction-dialogue"]
            },
            {
                "id": "b1-09-03-writing-1",
                "type": "multiple-choice",
                "category": "production",
                "question": "How do you say: 'The doctor prescribed me medicine for the fever.'?",
                "options": [
                    "Az orvos gyógyszert írt fel a lázamra.",
                    "Az orvos lázat kapott tegnap este.",
                    "A gyógyszert elfelejtettem bevenni reggel."
                ],
                "correct": 0,
                "teaches": ["production-prescribe"]
            },
            {
                "id": "b1-09-03-writing-2",
                "type": "multiple-choice",
                "category": "production",
                "question": "How do you say: 'I picked up the prescription at the pharmacy.'?",
                "options": [
                    "Kiváltottam a receptet a gyógyszertárban.",
                    "A gyógyszertárban orvossal beszéltem.",
                    "A recept nélkül vettem egy könyvet."
                ],
                "correct": 0,
                "teaches": ["production-pharmacy"]
            },
            {
                "id": "b1-09-03-check-1",
                "type": "multiple-choice",
                "category": "check",
                "question": "What is 'recept' in a pharmacy?",
                "options": ["prescription", "cooking recipe", "cash receipt"],
                "correct": 0,
                "teaches": ["check-recept"]
            },
            {
                "id": "b1-09-03-check-2",
                "type": "multiple-choice",
                "category": "check",
                "question": "Which verb forms 'gyógyszert ...' (to pick up / fill medication)?",
                "options": ["kivált", "kivesz", "kikér"],
                "correct": 0,
                "teaches": ["check-kivalt"]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-09-03-ex.json", ex_03)

    ex_04 = {
        "lesson": "b1-09-04",
        "exercises": [
            {
                "id": "b1-09-04-intro-1",
                "type": "multiple-choice",
                "category": "introduce",
                "question": "What does 'egyensúly' mean?",
                "options": ["balance / equilibrium", "tension", "illness"],
                "correct": 0,
                "teaches": ["vocab-egyensuly"]
            },
            {
                "id": "b1-09-04-intro-2",
                "type": "multiple-choice",
                "category": "introduce",
                "question": "Which verb pairs with 'feszültséget' to mean release / relieve stress?",
                "options": ["levezet", "felvesz", "megállít"],
                "correct": 0,
                "teaches": ["collocation-levezet"]
            },
            {
                "id": "b1-09-04-controlled-1",
                "type": "matching",
                "category": "controlled",
                "pairs": [
                    ["feszültség", "tension, stress"],
                    ["egyensúly", "balance"],
                    ["pihenés", "rest, relaxation"],
                    ["levezetés", "winding down / release"]
                ],
                "teaches": ["vocab-stress-management"]
            },
            {
                "id": "b1-09-04-controlled-2",
                "type": "multiple-choice",
                "category": "controlled",
                "question": "A séta a természetben segít levezetni a felgyülemlett ...",
                "options": ["feszültséget.", "receptet.", "vizsgálatot."],
                "correct": 0,
                "teaches": ["feszultseg-context"]
            },
            {
                "id": "b1-09-04-controlled-3",
                "type": "fill-blank",
                "category": "controlled",
                "sentence": "Fontos megtartani a munka és a magánélet közötti ____. (balance / acc)",
                "answer": "egyensúlyt",
                "teaches": ["egyensuly-case"]
            },
            {
                "id": "b1-09-04-controlled-4",
                "type": "multiple-choice",
                "category": "controlled",
                "question": "Which activity supports mental relaxation?",
                "options": [
                    "Csendes pihenés egy jó könyvvel vagy egy kiadós alvás.",
                    "Egész éjjel túlórázni az irodában.",
                    "Feszülten vitatkozni a kollégákkal."
                ],
                "correct": 0,
                "teaches": ["relaxation-concept"]
            },
            {
                "id": "b1-09-04-practice-1",
                "type": "matching",
                "category": "practice",
                "pairs": [
                    ["lelki egyensúly", "mental balance"],
                    ["napi stressz", "daily stress"],
                    ["aktív pihenés", "active recreation / rest"],
                    ["feszültségmentes környezet", "stress-free environment"]
                ],
                "teaches": ["stress-phrases"]
            },
            {
                "id": "b1-09-04-practice-2",
                "type": "multiple-choice",
                "category": "practice",
                "question": "Miért van szüksége a szervezetnek rendszeres pihenésre?",
                "options": [
                    "Hogy regenerálódjon és megőrizze a belső egyensúlyát.",
                    "Hogy ne kelljen soha dolgozni.",
                    "Hogy elfelejtsük a barátainkat."
                ],
                "correct": 0,
                "teaches": ["rest-reading"]
            },
            {
                "id": "b1-09-04-practice-3",
                "type": "fill-blank",
                "category": "practice",
                "sentence": "Hétvégén mindenkinek szüksége van a zavartalan ____. (rest / sublative)",
                "answer": "pihenésre",
                "teaches": ["pihenesre-case"]
            },
            {
                "id": "b1-09-04-practice-4",
                "type": "multiple-choice",
                "category": "practice",
                "question": "Mit jelent az 'aktív kikapcsolódás'?",
                "options": [
                    "Recreation through movement, sports, or nature walks.",
                    "Turning off the lights.",
                    "Drinking coffee at night."
                ],
                "correct": 0,
                "teaches": ["kikapcsolodas-translation"]
            },
            {
                "id": "b1-09-04-dialogue-1",
                "type": "multiple-choice",
                "category": "dialogue",
                "question": "— Nagyon kimerültnek látszol, mi a baj?\n— ...",
                "options": [
                    "Túl sok a feszültség a munkahelyemen, rám férne egy kis pihenés.",
                    "A metró nagyon gyorsan ment reggel.",
                    "Nem találtam meg a cipőmet."
                ],
                "correct": 0,
                "teaches": ["stress-dialogue-1"]
            },
            {
                "id": "b1-09-04-dialogue-2",
                "type": "multiple-choice",
                "category": "dialogue",
                "question": "— Hogyan vezeted le a napi feszültséget?\n— ...",
                "options": [
                    "Futni járok a parkba vagy halk zenét hallgatok otthon.",
                    "Megírom a holnapi menetrendet.",
                    "Kiváltottam a receptet tegnap."
                ],
                "correct": 0,
                "teaches": ["stress-dialogue-2"]
            },
            {
                "id": "b1-09-04-writing-1",
                "type": "multiple-choice",
                "category": "production",
                "question": "How do you say: 'Sport helps relieve stress.'?",
                "options": [
                    "A sport segít levezetni a feszültséget.",
                    "A sportban nincsen semmilyen feszültség.",
                    "Feszülten sportoltam a szobában."
                ],
                "correct": 0,
                "teaches": ["production-stress-relief"]
            },
            {
                "id": "b1-09-04-writing-2",
                "type": "multiple-choice",
                "category": "production",
                "question": "How do you say: 'We must find balance in life.'?",
                "options": [
                    "Meg kell találnunk az egyensúlyt az életben.",
                    "Az egyensúly elveszett a házban tegnap.",
                    "Egyensúly nélkül él mindenki a városban."
                ],
                "correct": 0,
                "teaches": ["production-balance"]
            },
            {
                "id": "b1-09-04-check-1",
                "type": "multiple-choice",
                "category": "check",
                "question": "What is 'egyensúly'?",
                "options": ["balance", "headache", "weight"],
                "correct": 0,
                "teaches": ["check-egyensuly"]
            },
            {
                "id": "b1-09-04-check-2",
                "type": "multiple-choice",
                "category": "check",
                "question": "Complete: 'A sport segít ... a feszültséget.' (relieve / wind down)",
                "options": ["levezetni", "elvinni", "behozni"],
                "correct": 0,
                "teaches": ["check-levezetni"]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-09-04-ex.json", ex_04)

    ex_05 = {
        "lesson": "b1-09-05",
        "exercises": [
            {
                "id": "b1-09-05-intro-1",
                "type": "multiple-choice",
                "category": "introduce",
                "question": "What does 'jóllét' mean?",
                "options": ["wellbeing", "illness", "good morning"],
                "correct": 0,
                "teaches": ["vocab-jollet"]
            },
            {
                "id": "b1-09-05-intro-2",
                "type": "multiple-choice",
                "category": "introduce",
                "question": "Which advisory adjective means 'worthwhile'?",
                "options": ["érdemes", "káros", "tilos"],
                "correct": 0,
                "teaches": ["advisory-erdemes"]
            },
            {
                "id": "b1-09-05-controlled-1",
                "type": "matching",
                "category": "controlled",
                "pairs": [
                    ["jóllét", "wellbeing"],
                    ["egészséges", "healthy"],
                    ["kezelés", "medical treatment"],
                    ["gyógyulás", "recovery, healing"]
                ],
                "teaches": ["vocab-wellbeing-synthesis"]
            },
            {
                "id": "b1-09-05-controlled-2",
                "type": "multiple-choice",
                "category": "controlled",
                "question": "A gyors gyógyulás érdekében ... ágyban maradni.",
                "options": ["ajánlott", "tilos", "káros"],
                "correct": 0,
                "teaches": ["ajanlott-usage"]
            },
            {
                "id": "b1-09-05-controlled-3",
                "type": "fill-blank",
                "category": "controlled",
                "sentence": "A helyes orvosi ____ meghozta a várt eredményt. (treatment / nom)",
                "answer": "kezelés",
                "teaches": ["kezeles-context"]
            },
            {
                "id": "b1-09-05-controlled-4",
                "type": "multiple-choice",
                "category": "controlled",
                "question": "Which sentence provides gentle health advice?",
                "options": [
                    "Érdemes naponta legalább fél órát a friss levegőn tölteni.",
                    "Soha senkinek nem szabad orvoshoz mennie.",
                    "A betegség magától elmúlik azonnal."
                ],
                "correct": 0,
                "teaches": ["advisory-concept"]
            },
            {
                "id": "b1-09-05-practice-1",
                "type": "matching",
                "category": "practice",
                "pairs": [
                    ["teljes gyógyulás", "complete recovery"],
                    ["orvosi kezelés", "medical treatment"],
                    ["fizikai jóllét", "physical wellbeing"],
                    ["egészséges szervezet", "healthy organism"]
                ],
                "teaches": ["recovery-collocations"]
            },
            {
                "id": "b1-09-05-practice-2",
                "type": "multiple-choice",
                "category": "practice",
                "question": "Hogyan segíthetjük a szervezet természetes gyógyulását?",
                "options": [
                    "Bőséges folyadékfogyasztással, nyugalommal és az orvosi tanácsok betartásával.",
                    "Kemény éjszakai munkával.",
                    "Gyógyszerek elutasításával."
                ],
                "correct": 0,
                "teaches": ["recovery-reading"]
            },
            {
                "id": "b1-09-05-practice-3",
                "type": "fill-blank",
                "category": "practice",
                "sentence": "Mindenkinek szívből kívánunk mielőbbi ____. (recovery / acc)",
                "answer": "gyógyulást",
                "teaches": ["gyogyulast-acc"]
            },
            {
                "id": "b1-09-05-practice-4",
                "type": "multiple-choice",
                "category": "practice",
                "question": "Mit jelent az, hogy 'Jobbulást kívánok!'?",
                "options": ["Get well soon! / I wish you a speedy recovery!", "Good night!", "Bon voyage!"],
                "correct": 0,
                "teaches": ["jobbulast-translation"]
            },
            {
                "id": "b1-09-05-dialogue-1",
                "type": "multiple-choice",
                "category": "dialogue",
                "question": "— Hallom, beteg voltál a múlt héten. Hogy vagy most?\n— ...",
                "options": [
                    "Köszönöm, a kezelés után már sokkal jobban vagyok, túl vagyok a nehezén.",
                    "A vonat pontosan tízkor érkezik.",
                    "Nem találtam meg a térképet tegnap."
                ],
                "correct": 0,
                "teaches": ["recovery-dialogue-1"]
            },
            {
                "id": "b1-09-05-dialogue-2",
                "type": "multiple-choice",
                "category": "dialogue",
                "question": "— Mit tanácsolsz a megfázás ellen?\n— ...",
                "options": [
                    "Érdemes forró mézes teát inni és sok C-vitamint szedni.",
                    "Semmit, menjünk moziba most rögtön.",
                    "A postán adtam fel a csomagot."
                ],
                "correct": 0,
                "teaches": ["advice-dialogue-2"]
            },
            {
                "id": "b1-09-05-writing-1",
                "type": "multiple-choice",
                "category": "production",
                "question": "How do you say: 'I wish you a speedy recovery.'?",
                "options": [
                    "Mielőbbi gyógyulást kívánok neked.",
                    "Gyógyulás nélkül utaztam haza.",
                    "A gyógyulásról nem beszéltem senkivel."
                ],
                "correct": 0,
                "teaches": ["production-get-well"]
            },
            {
                "id": "b1-09-05-writing-2",
                "type": "multiple-choice",
                "category": "production",
                "question": "How do you say: 'It is recommended to rest a lot.'?",
                "options": [
                    "Ajánlott sokat pihenni.",
                    "Pihenni tilos az ágyban.",
                    "Nem tudtam pihenni tegnap éjjel."
                ],
                "correct": 0,
                "teaches": ["production-ajanlott"]
            },
            {
                "id": "b1-09-05-reading-1",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Kosztolányi elbeszélésében hová látogat el Esti Kornél?",
                "options": [
                    "Egy híres belgyógyász idős professzor csendes rendelőjébe.",
                    "Egy gyógyszergyárba.",
                    "A budai színházba."
                ],
                "correct": 0,
                "teaches": ["kosztolanyi-reading-1"]
            },
            {
                "id": "b1-09-05-reading-2",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Mit állapít meg a professzor az alapos orvosi vizsgálat után?",
                "options": [
                    "Hogy Esti szervezete és szíve teljesen egészséges.",
                    "Hogy azonnal kórházba kell feküdnie.",
                    "Hogy elvesztette a receptjét."
                ],
                "correct": 0,
                "teaches": ["kosztolanyi-reading-2"]
            },
            {
                "id": "b1-09-05-reading-3",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Milyen különleges 'gyógyszert' ír fel a professzor Estinek?",
                "options": [
                    "Napi két óra sétát a friss levegőn és belső békét.",
                    "Erős altatót a patikából.",
                    "Szigorú kórházi diétát."
                ],
                "correct": 0,
                "teaches": ["kosztolanyi-reading-3"]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-09-05-ex.json", ex_05)

    ex_consolidation = {
        "lesson": "b1-09-consolidation",
        "exercises": [
            {
                "id": "b1-09-consolidation-1",
                "type": "matching",
                "category": "recognize",
                "pairs": [
                    ["életmód", "lifestyle"],
                    ["megelőzés", "prevention"],
                    ["recept", "prescription"],
                    ["jóllét", "wellbeing"]
                ]
            },
            {
                "id": "b1-09-consolidation-2",
                "type": "matching",
                "category": "recognize",
                "pairs": [
                    ["káros", "harmful"],
                    ["egyensúly", "balance"],
                    ["feszültség", "tension, stress"],
                    ["gyógyulás", "recovery"]
                ]
            },
            {
                "id": "b1-09-consolidation-3",
                "type": "multiple-choice",
                "category": "recognize",
                "question": "Which noun phrase expresses generic 'one' or 'people in general'?",
                "options": ["az ember", "az autó", "a térkép"],
                "correct": 0
            },
            {
                "id": "b1-09-consolidation-4",
                "type": "multiple-choice",
                "category": "recall",
                "question": "Complete: 'A kórházban szigorúan ... a dohányzás.'",
                "options": ["tilos", "szabad", "kell"],
                "correct": 0
            },
            {
                "id": "b1-09-consolidation-5",
                "type": "fill-blank",
                "category": "recall",
                "sentence": "A beteg erős torokfájásra ____ a háziorvosnak. (complained / past)",
                "answer": "panaszkodott",
                "teaches": ["panaszkodott-recall"]
            },
            {
                "id": "b1-09-consolidation-6",
                "type": "multiple-choice",
                "category": "recall",
                "question": "Where does one pick up prescription medication in Hungarian?",
                "options": ["a gyógyszertárban (patikában)", "a postahivatalban", "a vágányon"],
                "correct": 0
            },
            {
                "id": "b1-09-consolidation-7",
                "type": "multiple-choice",
                "category": "in-context",
                "question": "A sport és a séta a természetben segít levezetni a napi ...",
                "options": ["feszültséget.", "menetrendet.", "alagutat."],
                "correct": 0
            },
            {
                "id": "b1-09-consolidation-8",
                "type": "fill-blank",
                "category": "in-context",
                "sentence": "A gyors felépüléshez sok pihenés és orvosi ____ szükséges. (treatment / nom)",
                "answer": "kezelés",
                "teaches": ["kezeles-recall"]
            },
            {
                "id": "b1-09-consolidation-9",
                "type": "multiple-choice",
                "category": "in-context",
                "question": "Mit jelent az, hogy 'Jobbulást kívánok'?",
                "options": [
                    "I wish you a speedy recovery.",
                    "Have a nice trip.",
                    "Congratulations on the exam."
                ],
                "correct": 0
            },
            {
                "id": "b1-09-consolidation-10",
                "type": "multiple-choice",
                "category": "produce",
                "question": "Translate: 'One must pay attention to daily nutrition.'",
                "options": [
                    "Az embernek oda kell figyelnie a mindennapi táplálkozásra.",
                    "Az ember táplálkozás nélkül él a városban.",
                    "A táplálkozásról senki nem beszélt tegnap."
                ],
                "correct": 0
            },
            {
                "id": "b1-09-consolidation-11",
                "type": "multiple-choice",
                "category": "produce",
                "question": "Translate: 'Smoking is strictly forbidden here.'",
                "options": [
                    "Itt szigorúan tilos a dohányzás.",
                    "Itt szabad dohányozni reggel.",
                    "Nem dohányoztunk az irodában."
                ],
                "correct": 0
            },
            {
                "id": "b1-09-consolidation-12",
                "type": "multiple-choice",
                "category": "produce",
                "question": "Translate: 'It is recommended to take a walk every day.'",
                "options": [
                    "Ajánlott mindennap sétálni egyet.",
                    "Sétálni tilos a parkban.",
                    "Nem mentünk sétálni délután."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-09-consolidation-ex.json", ex_consolidation)

    # -------------------------------------------------------------------------
    # 5. Lesson Files
    # -------------------------------------------------------------------------
    lesson_01 = {
        "id": "lesson.b1.09-01",
        "unit": 9,
        "title": "One Should...",
        "level": "B1",
        "grammar": "Impersonal general subject 'az ember'; full modal paradigm (kell, lehet)",
        "goal": [
            "I can express generalized health advice and truths using az ember.",
            "I can use modals like kell and lehet with dative subjects.",
            "I can use four new vocabulary items related to lifestyle and nutrition.",
            "I can discuss prevention and healthy daily habits."
        ],
        "sections": [
            {
                "type": "goal",
                "title": "Lesson Goals",
                "items": [
                    "I can express generalized health advice and truths using az ember.",
                    "I can use modals like kell and lehet with dative subjects.",
                    "I can use four new vocabulary items related to lifestyle and nutrition.",
                    "I can discuss prevention and healthy daily habits."
                ]
            },
            {"type": "recycle", "title": "Quick Review"},
            {"type": "grammar", "ref": "grammar/b1/b1-09-01-a-gr.json"},
            {"type": "grammar", "ref": "grammar/b1/b1-09-01-b-gr.json"},
            {"type": "vocabulary", "title": "Lesson Vocabulary", "ref": "vocabulary/b1/b1-09-01-voc.json"},
            {"type": "exercise-group", "title": "Introduce", "ref": "exercises/b1/b1-09-01-ex.json", "exerciseRefs": ["b1-09-01-intro-1", "b1-09-01-intro-2"]},
            {"type": "exercise-group", "title": "Controlled", "ref": "exercises/b1/b1-09-01-ex.json", "exerciseRefs": ["b1-09-01-controlled-1", "b1-09-01-controlled-2", "b1-09-01-controlled-3", "b1-09-01-controlled-4"]},
            {"type": "exercise-group", "title": "Practice", "ref": "exercises/b1/b1-09-01-ex.json", "exerciseRefs": ["b1-09-01-practice-1", "b1-09-01-practice-2", "b1-09-01-practice-3", "b1-09-01-practice-4"]},
            {"type": "exercise-group", "title": "Dialogue", "ref": "exercises/b1/b1-09-01-ex.json", "exerciseRefs": ["b1-09-01-dialogue-1", "b1-09-01-dialogue-2"]},
            {"type": "exercise-group", "title": "Production", "ref": "exercises/b1/b1-09-01-ex.json", "exerciseRefs": ["b1-09-01-writing-1", "b1-09-01-writing-2"]},
            {"type": "srs", "title": "Add to Review"},
            {"type": "exercise-group", "title": "Check", "ref": "exercises/b1/b1-09-01-ex.json", "exerciseRefs": ["b1-09-01-check-1", "b1-09-01-check-2"]},
            {
                "type": "checklist",
                "title": "Can you do this?",
                "items": [
                    "I can express generalized health advice and truths using az ember.",
                    "I can use modals like kell and lehet with dative subjects.",
                    "I can use four new vocabulary items related to lifestyle and nutrition.",
                    "I can discuss prevention and healthy daily habits."
                ]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-09-01.json", lesson_01)

    lesson_02 = {
        "id": "lesson.b1.09-02",
        "unit": 9,
        "title": "It's Not Allowed To...",
        "level": "B1",
        "grammar": "Prohibitions and permissions: szabad, tilos, nem szabad; moderation",
        "goal": [
            "I can express strict prohibitions and permissions using szabad and tilos.",
            "I can discuss harmful habits and the principle of moderation (mérték).",
            "I can use four new vocabulary items related to consumption and habits.",
            "I can understand health warnings and public health signs in Hungary."
        ],
        "sections": [
            {
                "type": "goal",
                "title": "Lesson Goals",
                "items": [
                    "I can express strict prohibitions and permissions using szabad and tilos.",
                    "I can discuss harmful habits and the principle of moderation (mérték).",
                    "I can use four new vocabulary items related to consumption and habits.",
                    "I can understand health warnings and public health signs in Hungary."
                ]
            },
            {"type": "recycle", "title": "Quick Review"},
            {"type": "grammar", "ref": "grammar/b1/b1-09-02-gr.json"},
            {"type": "vocabulary", "title": "Lesson Vocabulary", "ref": "vocabulary/b1/b1-09-02-voc.json"},
            {"type": "exercise-group", "title": "Introduce", "ref": "exercises/b1/b1-09-02-ex.json", "exerciseRefs": ["b1-09-02-intro-1", "b1-09-02-intro-2"]},
            {"type": "exercise-group", "title": "Controlled", "ref": "exercises/b1/b1-09-02-ex.json", "exerciseRefs": ["b1-09-02-controlled-1", "b1-09-02-controlled-2", "b1-09-02-controlled-3", "b1-09-02-controlled-4"]},
            {"type": "exercise-group", "title": "Practice", "ref": "exercises/b1/b1-09-02-ex.json", "exerciseRefs": ["b1-09-02-practice-1", "b1-09-02-practice-2", "b1-09-02-practice-3", "b1-09-02-practice-4"]},
            {"type": "exercise-group", "title": "Dialogue", "ref": "exercises/b1/b1-09-02-ex.json", "exerciseRefs": ["b1-09-02-dialogue-1", "b1-09-02-dialogue-2"]},
            {"type": "exercise-group", "title": "Production", "ref": "exercises/b1/b1-09-02-ex.json", "exerciseRefs": ["b1-09-02-writing-1", "b1-09-02-writing-2"]},
            {"type": "srs", "title": "Add to Review"},
            {"type": "exercise-group", "title": "Check", "ref": "exercises/b1/b1-09-02-ex.json", "exerciseRefs": ["b1-09-02-check-1", "b1-09-02-check-2"]},
            {
                "type": "checklist",
                "title": "Can you do this?",
                "items": [
                    "I can express strict prohibitions and permissions using szabad and tilos.",
                    "I can discuss harmful habits and the principle of moderation (mérték).",
                    "I can use four new vocabulary items related to consumption and habits.",
                    "I can understand health warnings and public health signs in Hungary."
                ]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-09-02.json", lesson_02)

    lesson_03 = {
        "id": "lesson.b1.09-03",
        "unit": 9,
        "title": "At the Doctor's, in Detail",
        "level": "B1",
        "grammar": "Doctor-patient interactions: panaszkodik vmire, felír, kivált",
        "goal": [
            "I can describe medical symptoms and complaints clearly to a physician.",
            "I can understand doctors' examination instructions and prescriptions.",
            "I can use four new vocabulary items related to clinics and pharmacies.",
            "I can navigate picking up prescription medicine at a Hungarian pharmacy."
        ],
        "sections": [
            {
                "type": "goal",
                "title": "Lesson Goals",
                "items": [
                    "I can describe medical symptoms and complaints clearly to a physician.",
                    "I can understand doctors' examination instructions and prescriptions.",
                    "I can use four new vocabulary items related to clinics and pharmacies.",
                    "I can navigate picking up prescription medicine at a Hungarian pharmacy."
                ]
            },
            {"type": "recycle", "title": "Quick Review"},
            {"type": "grammar", "ref": "grammar/b1/b1-09-03-gr.json"},
            {"type": "vocabulary", "title": "Lesson Vocabulary", "ref": "vocabulary/b1/b1-09-03-voc.json"},
            {"type": "exercise-group", "title": "Introduce", "ref": "exercises/b1/b1-09-03-ex.json", "exerciseRefs": ["b1-09-03-intro-1", "b1-09-03-intro-2"]},
            {"type": "exercise-group", "title": "Controlled", "ref": "exercises/b1/b1-09-03-ex.json", "exerciseRefs": ["b1-09-03-controlled-1", "b1-09-03-controlled-2", "b1-09-03-controlled-3", "b1-09-03-controlled-4"]},
            {"type": "exercise-group", "title": "Practice", "ref": "exercises/b1/b1-09-03-ex.json", "exerciseRefs": ["b1-09-03-practice-1", "b1-09-03-practice-2", "b1-09-03-practice-3", "b1-09-03-practice-4"]},
            {"type": "exercise-group", "title": "Dialogue", "ref": "exercises/b1/b1-09-03-ex.json", "exerciseRefs": ["b1-09-03-dialogue-1", "b1-09-03-dialogue-2"]},
            {"type": "exercise-group", "title": "Production", "ref": "exercises/b1/b1-09-03-ex.json", "exerciseRefs": ["b1-09-03-writing-1", "b1-09-03-writing-2"]},
            {"type": "srs", "title": "Add to Review"},
            {"type": "exercise-group", "title": "Check", "ref": "exercises/b1/b1-09-03-ex.json", "exerciseRefs": ["b1-09-03-check-1", "b1-09-03-check-2"]},
            {
                "type": "checklist",
                "title": "Can you do this?",
                "items": [
                    "I can describe medical symptoms and complaints clearly to a physician.",
                    "I can understand doctors' examination instructions and prescriptions.",
                    "I can use four new vocabulary items related to clinics and pharmacies.",
                    "I can navigate picking up prescription medicine at a Hungarian pharmacy."
                ]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-09-03.json", lesson_03)

    lesson_04 = {
        "id": "lesson.b1.09-04",
        "unit": 9,
        "title": "Stress & Balance",
        "level": "B1",
        "grammar": "Mental wellness collocations: feszültséget levezet, egyensúlyt talál",
        "goal": [
            "I can discuss stress management, work-life balance, and relaxation.",
            "I can use collocations like feszültséget levezet and egyensúlyt tart.",
            "I can use four new vocabulary items related to mental wellbeing.",
            "I can describe relaxing activities and active recovery techniques."
        ],
        "sections": [
            {
                "type": "goal",
                "title": "Lesson Goals",
                "items": [
                    "I can discuss stress management, work-life balance, and relaxation.",
                    "I can use collocations like feszültséget levezet and egyensúlyt tart.",
                    "I can use four new vocabulary items related to mental wellbeing.",
                    "I can describe relaxing activities and active recovery techniques."
                ]
            },
            {"type": "recycle", "title": "Quick Review"},
            {"type": "grammar", "ref": "grammar/b1/b1-09-04-gr.json"},
            {"type": "vocabulary", "title": "Lesson Vocabulary", "ref": "vocabulary/b1/b1-09-04-voc.json"},
            {"type": "exercise-group", "title": "Introduce", "ref": "exercises/b1/b1-09-04-ex.json", "exerciseRefs": ["b1-09-04-intro-1", "b1-09-04-intro-2"]},
            {"type": "exercise-group", "title": "Controlled", "ref": "exercises/b1/b1-09-04-ex.json", "exerciseRefs": ["b1-09-04-controlled-1", "b1-09-04-controlled-2", "b1-09-04-controlled-3", "b1-09-04-controlled-4"]},
            {"type": "exercise-group", "title": "Practice", "ref": "exercises/b1/b1-09-04-ex.json", "exerciseRefs": ["b1-09-04-practice-1", "b1-09-04-practice-2", "b1-09-04-practice-3", "b1-09-04-practice-4"]},
            {"type": "exercise-group", "title": "Dialogue", "ref": "exercises/b1/b1-09-04-ex.json", "exerciseRefs": ["b1-09-04-dialogue-1", "b1-09-04-dialogue-2"]},
            {"type": "exercise-group", "title": "Production", "ref": "exercises/b1/b1-09-04-ex.json", "exerciseRefs": ["b1-09-04-writing-1", "b1-09-04-writing-2"]},
            {"type": "srs", "title": "Add to Review"},
            {"type": "exercise-group", "title": "Check", "ref": "exercises/b1/b1-09-04-ex.json", "exerciseRefs": ["b1-09-04-check-1", "b1-09-04-check-2"]},
            {
                "type": "checklist",
                "title": "Can you do this?",
                "items": [
                    "I can discuss stress management, work-life balance, and relaxation.",
                    "I can use collocations like feszültséget levezet and egyensúlyt tart.",
                    "I can use four new vocabulary items related to mental wellbeing.",
                    "I can describe relaxing activities and active recovery techniques."
                ]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-09-04.json", lesson_04)

    lesson_05 = {
        "id": "lesson.b1.09-05",
        "unit": 9,
        "title": "Giving Health Advice",
        "level": "B1",
        "grammar": "Synthesis: gentle health advice with érdemes, ajánlott, tanácsos",
        "goal": [
            "I can offer polite, natural health advice using érdemes and ajánlott.",
            "I can discuss treatments, medical therapies, and complete recovery.",
            "I can use four new vocabulary items related to wellbeing and healing.",
            "I can read and understand an adapted literary excerpt from Kosztolányi's Esti Kornél."
        ],
        "sections": [
            {
                "type": "goal",
                "title": "Lesson Goals",
                "items": [
                    "I can offer polite, natural health advice using érdemes and ajánlott.",
                    "I can discuss treatments, medical therapies, and complete recovery.",
                    "I can use four new vocabulary items related to wellbeing and healing.",
                    "I can read and understand an adapted literary excerpt from Kosztolányi's Esti Kornél."
                ]
            },
            {"type": "recycle", "title": "Quick Review"},
            {"type": "grammar", "ref": "grammar/b1/b1-09-05-gr.json"},
            {"type": "vocabulary", "title": "Lesson Vocabulary", "ref": "vocabulary/b1/b1-09-05-voc.json"},
            {"type": "exercise-group", "title": "Introduce", "ref": "exercises/b1/b1-09-05-ex.json", "exerciseRefs": ["b1-09-05-intro-1", "b1-09-05-intro-2"]},
            {"type": "exercise-group", "title": "Controlled", "ref": "exercises/b1/b1-09-05-ex.json", "exerciseRefs": ["b1-09-05-controlled-1", "b1-09-05-controlled-2", "b1-09-05-controlled-3", "b1-09-05-controlled-4"]},
            {"type": "exercise-group", "title": "Practice", "ref": "exercises/b1/b1-09-05-ex.json", "exerciseRefs": ["b1-09-05-practice-1", "b1-09-05-practice-2", "b1-09-05-practice-3", "b1-09-05-practice-4"]},
            {"type": "exercise-group", "title": "Dialogue", "ref": "exercises/b1/b1-09-05-ex.json", "exerciseRefs": ["b1-09-05-dialogue-1", "b1-09-05-dialogue-2"]},
            {"type": "exercise-group", "title": "Production", "ref": "exercises/b1/b1-09-05-ex.json", "exerciseRefs": ["b1-09-05-writing-1", "b1-09-05-writing-2"]},
            {"type": "srs", "title": "Add to Review"},
            {
                "type": "story",
                "title": "Reading: Esti Kornél és az orvosi vizsgálat",
                "ref": "stories/classics/b1/b1-09-estikornel.json"
            },
            {"type": "exercise-group", "title": "Reading", "ref": "exercises/b1/b1-09-05-ex.json", "exerciseRefs": ["b1-09-05-reading-1", "b1-09-05-reading-2", "b1-09-05-reading-3"]},
            {
                "type": "checklist",
                "title": "Can you do this?",
                "items": [
                    "I can offer polite, natural health advice using érdemes and ajánlott.",
                    "I can discuss treatments, medical therapies, and complete recovery.",
                    "I can use four new vocabulary items related to wellbeing and healing.",
                    "I can read and understand an adapted literary excerpt from Kosztolányi's Esti Kornél."
                ]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-09-05.json", lesson_05)

    lesson_consolidation = {
        "id": "lesson.b1.09-consolidation",
        "unit": 9,
        "title": "Unit 9 Consolidation",
        "level": "B1",
        "sections": [
            {
                "type": "goal",
                "title": "Consolidation Goals",
                "items": [
                    "I can give natural health advice using generic az ember and modal verbs.",
                    "I can navigate medical consultations, prescriptions, and pharmacy visits.",
                    "I can discuss stress relief, moderation, and work-life balance in Hungarian.",
                    "I can formulate polite recommendations using érdemes and ajánlott."
                ]
            },
            {"type": "recycle", "title": "Quick Review"},
            {"type": "exercise-group", "title": "Recognize", "ref": "exercises/b1/b1-09-consolidation-ex.json", "exerciseRefs": ["b1-09-consolidation-1", "b1-09-consolidation-2", "b1-09-consolidation-3"]},
            {"type": "exercise-group", "title": "Recall", "ref": "exercises/b1/b1-09-consolidation-ex.json", "exerciseRefs": ["b1-09-consolidation-4", "b1-09-consolidation-5", "b1-09-consolidation-6"]},
            {"type": "exercise-group", "title": "In Context", "ref": "exercises/b1/b1-09-consolidation-ex.json", "exerciseRefs": ["b1-09-consolidation-7", "b1-09-consolidation-8", "b1-09-consolidation-9"]},
            {"type": "exercise-group", "title": "Produce", "ref": "exercises/b1/b1-09-consolidation-ex.json", "exerciseRefs": ["b1-09-consolidation-10", "b1-09-consolidation-11", "b1-09-consolidation-12"]},
            {
                "type": "checklist",
                "title": "Can you do this?",
                "items": [
                    "I can give natural health advice using generic az ember and modal verbs.",
                    "I can navigate medical consultations, prescriptions, and pharmacy visits.",
                    "I can discuss stress relief, moderation, and work-life balance in Hungarian.",
                    "I can formulate polite recommendations using érdemes and ajánlott."
                ]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-09-consolidation.json", lesson_consolidation)

if __name__ == "__main__":
    build_unit_9_core()
    print("Successfully built Hungarian B1 Core Unit 9!")
