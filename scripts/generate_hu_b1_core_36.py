#!/usr/bin/env python3
"""Generate Hungarian B1 Core Unit 36: Independent Hungarian (b1-36)."""

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

def build_unit_36_core():
    # -------------------------------------------------------------------------
    # 1. Vocabulary Files (4 words each = 20 words total)
    # -------------------------------------------------------------------------
    voc_01 = {
        "id": "vocab.b1.36.01",
        "lesson": "b1-36-01",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "önállóság", "translation": "independence, self-reliance, autonomy", "pos": "noun"},
            {"lemma": "folyékonyság", "translation": "fluency, smooth flow of speech", "pos": "noun"},
            {"lemma": "szókincs", "translation": "vocabulary, word stock", "pos": "noun"},
            {"lemma": "magabiztosság", "translation": "confidence, self-assurance", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-36-01-voc.json", voc_01)

    voc_02 = {
        "id": "vocab.b1.36.02",
        "lesson": "b1-36-02",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "társalgás", "translation": "conversation, discourse, social chat", "pos": "noun"},
            {"lemma": "spontaneitás", "translation": "spontaneity, natural unscripted ease", "pos": "noun"},
            {"lemma": "helyzetfelismerés", "translation": "reading the room, situational awareness", "pos": "noun"},
            {"lemma": "közbeszólás", "translation": "interjection, chiming in, polite interruption", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-36-02-voc.json", voc_02)

    voc_03 = {
        "id": "vocab.b1.36.03",
        "lesson": "b1-36-03",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "félreértés", "translation": "misunderstanding, misinterpretation", "pos": "noun"},
            {"lemma": "tisztázás", "translation": "clarification, clearing up", "pos": "noun"},
            {"lemma": "váratlan helyzet", "translation": "unexpected situation, surprise circumstance", "pos": "noun"},
            {"lemma": "találékonyság", "translation": "resourcefulness, ingenuity, quick-wittedness", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-36-03-voc.json", voc_03)

    voc_04 = {
        "id": "vocab.b1.36.04",
        "lesson": "b1-36-04",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "stílusárnyalat", "translation": "stylistic nuance, tone of voice", "pos": "noun"},
            {"lemma": "nyelvi regiszter", "translation": "language register, formal vs informal style", "pos": "noun"},
            {"lemma": "szófordulat", "translation": "idiomatic turn of phrase, expression", "pos": "noun"},
            {"lemma": "köznyelv", "translation": "standard everyday vernacular language", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-36-04-voc.json", voc_04)

    voc_05 = {
        "id": "vocab.b1.36.05",
        "lesson": "b1-36-05",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "nyelvtudás", "translation": "language proficiency, language mastery", "pos": "noun"},
            {"lemma": "távlat", "translation": "perspective, future horizon, vista", "pos": "noun"},
            {"lemma": "továbbfejlődés", "translation": "further advancement, continued growth", "pos": "noun"},
            {"lemma": "anyanyelvi szint", "translation": "native-like level, near-native mastery", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-36-05-voc.json", voc_05)

    # -------------------------------------------------------------------------
    # 2. Grammar Files (2 per regular lesson = 10 files)
    # -------------------------------------------------------------------------
    gr_01_a = {
        "id": "grammar.b1.36.01.discourse-particles",
        "title": "Pragmatic Discourse Particles: Ugyebár, elvégre, márpedig",
        "sections": [
            {
                "type": "text",
                "title": "Natural Conversational Connectors",
                "content": "Authentic spoken Hungarian relies on pragmatic particles to manage shared knowledge and emphasis: *ugyebár* (as you know / isn't it so?), *elvégre* (after all), *márpedig* (nevertheless / but the fact remains), and *ugyancsak* (likewise / thoroughly)."
            },
            {
                "type": "examples",
                "title": "Discourse particle examples",
                "items": [
                    {"spanish": "Elvégre nem azért tanultunk annyit, hogy most feladjuk.", "english": "After all, we didn't study so much just to give up now."},
                    {"spanish": "Ez ugyebár mindannyiunk közös érdeke.", "english": "This is, as we all know, in our shared mutual interest."},
                    {"spanish": "Márpedig a szabályokat mindenkinek be kell tartania.", "english": "And yet, rules must be obeyed by everyone."}
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-36-01-a-gr.json", gr_01_a)

    gr_01_b = {
        "id": "grammar.b1.36.01.conversational-turn-taking",
        "title": "Turn-Taking & Smooth Transitions: Apropó, erről jut eszembe",
        "sections": [
            {
                "type": "text",
                "title": "Steering Natural Conversations",
                "content": "To link remarks smoothly to a conversation partner's topic, use colloquial transitional signposts: *apropó* (speaking of which), *erről jut eszembe* (that reminds me), *ha már itt tartunk* (while we're on the subject), and *egyébként* (by the way)."
            },
            {
                "type": "examples",
                "title": "Transition examples",
                "items": [
                    {"spanish": "Apropó, hallottad a legfrissebb híreket a vizsgáról?", "english": "Speaking of which, did you hear the latest news about the exam?"},
                    {"spanish": "Erről jut eszembe, múlt héten találkoztam egy régi ismerősöddel.", "english": "That reminds me, last week I ran into an old acquaintance of yours."},
                    {"spanish": "Ha már itt tartunk, érdemes megbeszélnünk a holnapi beosztást is.", "english": "While we're on the subject, it's worth discussing tomorrow's schedule too."}
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-36-01-b-gr.json", gr_01_b)

    gr_02_a = {
        "id": "grammar.b1.36.02.spontaneous-repairs",
        "title": "Spontaneous Repairs & Self-Correction: Vagyis inkább, pontosabban",
        "sections": [
            {
                "type": "text",
                "title": "Self-Repair in Live Speech",
                "content": "Independent speakers manage real-time speech production by deploying native repair markers: *vagyis inkább* (or rather), *pontosabban szólva* (more precisely speaking), and hesitation devices like *hogy is mondjam csak* (how shall I put it?)."
            },
            {
                "type": "examples",
                "title": "Repair examples",
                "items": [
                    {"spanish": "Három éve, vagyis inkább négy éve költöztem Magyarországra.", "english": "Three years, or rather four years ago, I moved to Hungary."},
                    {"spanish": "Pontosabban szólva nem elutasították, hanem elhalasztották a döntést.", "english": "More precisely speaking, they didn't reject the decision, they postponed it."},
                    {"spanish": "Ez a feladat, hogy is mondjam csak, komoly odafigyelést igényel.", "english": "This task, how shall I put it, requires serious attention."}
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-36-02-a-gr.json", gr_02_a)

    gr_02_b = {
        "id": "grammar.b1.36.02.expressive-focal-inversion",
        "title": "Expressive Focal Inversion & Nuanced Word Order",
        "sections": [
            {
                "type": "text",
                "title": "Mastering Hungarian Information Structure",
                "content": "Hungarian word order is pragmatic rather than grammatical. By moving elements immediately before the finite verb (the focus position) or into the post-verbal field, advanced speakers highlight new information, contrast, and subtle emotional nuance."
            },
            {
                "type": "examples",
                "title": "Word order examples",
                "items": [
                    {"spanish": "Én nem mondtam semmit. vs Nem én mondtam, hogy gyere ide.", "english": "I didn't say anything. vs It wasn't me who said to come here."},
                    {"spanish": "A könyvet olvastam el, nem az újságot.", "english": "It was the book I read, not the newspaper."},
                    {"spanish": "Pontosan ezt akartam megkérdezni tőled!", "english": "This is precisely what I wanted to ask you!"}
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-36-02-b-gr.json", gr_02_b)

    gr_03_a = {
        "id": "grammar.b1.36.03.polite-clarifications",
        "title": "Negotiating Clarification: Ha jól értem, úgy érted, hogy...",
        "sections": [
            {
                "type": "text",
                "title": "Resolving Ambiguities Smoothly",
                "content": "To check comprehension in fast-paced conversations without interrupting rudely, use polite checking formulas: *ha jól értem, azt mondod, hogy...* (if I understand correctly, you're saying that...), *úgy érted, hogy...?* (do you mean that...?)."
            },
            {
                "type": "examples",
                "title": "Clarification examples",
                "items": [
                    {"spanish": "Ha jól értem a szavaidat, támogatod az új kezdeményezést.", "english": "If I understand your words correctly, you support the new initiative."},
                    {"spanish": "Úgy érted, hogy holnap reggelig be kell fejeznünk a tervezetet?", "english": "Do you mean that we have to finish the draft by tomorrow morning?"},
                    {"spanish": "Javíts ki, ha tévedek, de erről már volt szó a múltkor.", "english": "Correct me if I'm wrong, but this was already mentioned last time."}
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-36-03-a-gr.json", gr_03_a)

    gr_03_b = {
        "id": "grammar.b1.36.03.polite-assertiveness",
        "title": "Pragmatic Assertiveness: Attól tartok, hogy...",
        "sections": [
            {
                "type": "text",
                "title": "Softening Dissent Gracefully",
                "content": "Cultivated speakers avoid blunt contradictions by framing disagreement with polite modal softeners: *attól tartok, hogy...* (I'm afraid that...), *nem feltétlenül értek egyet* (I don't necessarily agree), and *hadd jegyezzem meg, hogy...* (allow me to note that...)."
            },
            {
                "type": "examples",
                "title": "Assertiveness examples",
                "items": [
                    {"spanish": "Attól tartok, hogy félreértettük egymást az időpontot illetően.", "english": "I'm afraid that we misunderstood each other regarding the time."},
                    {"spanish": "Nem feltétlenül értek egyet ezzel a szigorú megközelítéssel.", "english": "I don't necessarily agree with this strict approach."},
                    {"spanish": "Hadd tegyem hozzá, hogy a költségek is jóval alacsonyabbak.", "english": "Allow me to add that the costs are also far lower."}
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-36-03-b-gr.json", gr_03_b)

    gr_04_a = {
        "id": "grammar.b1.36.04.register-modulation",
        "title": "Register Modulation: Shifting between Formal (Ön) and Informal (Te)",
        "sections": [
            {
                "type": "text",
                "title": "Navigating Social Politeness",
                "content": "Mastering Hungarian requires fluid register management: shifting naturally between formal 3rd-person address (*Ön / Maga* with formal verb agreements) in administrative and business environments, and informal 2nd-person address (*te / ti*) among friends and colleagues."
            },
            {
                "type": "examples",
                "title": "Register modulation examples",
                "items": [
                    {"spanish": "Kérem, foglaljon helyet! vs Ülj le bátran!", "english": "Please, take a seat! (Formal) vs Sit down comfortably! (Informal)"},
                    {"spanish": "Hogy tetszik lenni? vs Hogy vagy?", "english": "How are you doing? (Polite respectful) vs How are you? (Informal)"},
                    {"spanish": "Tegeződhetünk, ha nem bánja.", "english": "We can address each other informally, if you don't mind."}
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-36-04-a-gr.json", gr_04_a)

    gr_04_b = {
        "id": "grammar.b1.36.04.colloquial-idioms",
        "title": "Essential Spoken Idioms: Lépést tart, képben van, dűlőre jut",
        "sections": [
            {
                "type": "text",
                "title": "Idiomatic Fluency in Everyday Speech",
                "content": "Reaching an independent B1 level means recognizing and deploying common verbal idioms: *lépést tart vmivel* (keep pace with), *képben van* (be in the loop / up to date), *dűlőre jut* (come to an agreement / resolve an issue), and *túl van a nehezén* (be over the worst of it)."
            },
            {
                "type": "examples",
                "title": "Spoken idiom examples",
                "items": [
                    {"spanish": "Folyamatosan tanulnom kell, hogy lépést tartsak a fejlődéssel.", "english": "I have to learn constantly to keep pace with developments."},
                    {"spanish": "Teljesen képben vagyok a legújabb változásokkal kapcsolatban.", "english": "I am completely in the loop regarding the latest changes."},
                    {"spanish": "Hosszú vita után végre dűlőre jutottunk a szerződésről.", "english": "After a long debate, we finally came to an agreement on the contract."}
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-36-04-b-gr.json", gr_04_b)

    gr_05_a = {
        "id": "grammar.b1.36.05.subordination-synthesis",
        "title": "B1 Subordination Synthesis: Multi-Clause Complex Sentences",
        "sections": [
            {
                "type": "text",
                "title": "Synthesizing Complex Sentences",
                "content": "At the B1 milestone, speakers seamlessly combine temporal (*miután, mielőtt*), causal (*mivel, azért mert*), conditional (*ha... volna*), concessive (*bár... mégis*), and reported speech clauses into articulate, multi-tiered sentences."
            },
            {
                "type": "examples",
                "title": "Synthesis examples",
                "items": [
                    {"spanish": "Bár sokan kételkedtek a tervben, miután részletesen bemutattuk, mindenki belátta, hogy működni fog.", "english": "Although many doubted the plan, after we presented it in detail, everyone realized that it would work."},
                    {"spanish": "Ha nem lett volna olyan kitartó, aligha tudta volna megoldani ezt a bonyolult feladatot.", "english": "If he hadn't been so persistent, he hardly could have solved this complicated task."},
                    {"spanish": "Azért döntöttünk a folytatás mellett, mert úgy véltük, hogy megéri a fáradságot.", "english": "We decided to continue because we believed that it was worth the effort."}
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-36-05-a-gr.json", gr_05_a)

    gr_05_b = {
        "id": "grammar.b1.36.05.autonomous-expression",
        "title": "Autonomous Expression: Saját szavaimmal, magabiztosan",
        "sections": [
            {
                "type": "text",
                "title": "Independent Language Confidence",
                "content": "Celebrating independent Hungarian language competence means speaking without relying on translation in one's head: expressing feelings, complex reasoning, and humor naturally (*saját szavaimmal kifejezve*, *képes vagyok önállóan boldogulni*)."
            },
            {
                "type": "examples",
                "title": "Autonomous expression examples",
                "items": [
                    {"spanish": "Most már képes vagyok önállóan elintézni bármilyen hivatalos ügyet.", "english": "I am now capable of handling any official matter independently."},
                    {"spanish": "Saját szavaimmal is el tudom magyarázni a magyar történelem főbb állomásait.", "english": "I can explain the main milestones of Hungarian history in my own words too."},
                    {"spanish": "Büszke vagyok arra, hogy magabiztosan és természetesen használom a magyar nyelvet.", "english": "I am proud that I use the Hungarian language with confidence and ease."}
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-36-05-b-gr.json", gr_05_b)

    # -------------------------------------------------------------------------
    # 3. Classic Story: Gárdonyi Géza - Egri csillagok (b1-36-gardonyi.json)
    # -------------------------------------------------------------------------
    story = {
        "id": "story.b1.36.classic",
        "title": "Egri csillagok: A várvédők esküje",
        "level": "B1",
        "order": 36,
        "type": "classics",
        "estimatedMinutes": 8,
        "summary": "An adaptation from Géza Gárdonyi's celebrated national epic 'Egri csillagok' (Stars of Eger). In 1552, Captain István Dobó gathers his small garrison of Hungarian defenders inside the battered stone walls of Eger Castle against the overwhelming Ottoman sultanic army. Dobó delivers his legendary oath: 'A falak ereje nem a kőben van, hanem a védők lelkében' (The strength of the walls is not in the stone, but in the soul of the defenders), inspiring his men and women to triumph through unity, determination, and independent spirit.",
        "characters": [
            "Dobó István várkapitány",
            "Bornemissza Gergely",
            "A várvédők"
        ],
        "location": "Egri vár, 1552",
        "author": "Gárdonyi Géza",
        "work": "Egri csillagok",
        "paragraphs": [
            {
                "type": "narration",
                "text": "1552 őszén az egri vár udvarán csend honolt. A szétlőtt bástyák mögött alig kétezer magyar katona, polgár és bátor asszony állt szemben a hatalmas, százezres oszmán sereggel. A vár sorsa egyben az egész ország sorsát jelentette."
            },
            {
                "type": "dialogue",
                "speaker": "Dobó István várkapitány",
                "text": "Katonák, testvéreim! Eljött a döntő óra. Sokan kérdezték, hogyan állhatunk ellen egy ilyen óriási túlerőnek. De én azt mondom nektek: a falak ereje nem a kőben van, hanem a védők lelkében!"
            },
            {
                "type": "narration",
                "text": "Dobó kihúzta kardját, és magasba emelte a magyar zászló előtt. A védők lélegzet-visszafojtva hallgatták kapitányuk hangját, amely betöltötte a füstölgő várudvart."
            },
            {
                "type": "dialogue",
                "speaker": "Dobó István várkapitány",
                "text": "Esküdjetek velem az élő Istenre, hogy ezt a várat fel nem adjátok! Se pénzért, se ígéretért, se fenyegetésért! Esküdjetek, hogy addig harcoltok, amíg a karotok bírja és a szemetek lát!"
            },
            {
                "type": "dialogue",
                "speaker": "A várvédők",
                "text": "Esküszünk! Inkább meghalunk a vár romjai alatt, de a hazát és a becsületünket megvédjük!"
            },
            {
                "type": "dialogue",
                "speaker": "Bornemissza Gergely",
                "text": "Kapitány úr, a tüzes kerekeink és bombáink készen állnak. Bármilyen heves lesz a roham, nem hátrálunk egyetlen lépést sem."
            },
            {
                "type": "narration",
                "text": "A várvédők egysége és önfeláldozó bátorsága csodát tett: a hatalmas török hadsereg hetekig tartó véres ostrom után vereséget szenvedett és visszavonult. Az egri hősök példája évszázadok óta hirdeti: a hit, a hűség és a szabad, független lélek minden túlerőnél hatalmasabb."
            }
        ]
    }
    write_json("content/hu/stories/classics/b1/b1-36-gardonyi.json", story)

    # -------------------------------------------------------------------------
    # 4. Exercise Files (6 files, 7 exercises each = 42 exercises)
    # -------------------------------------------------------------------------
    ex_01 = {
        "lesson": "b1-36-01",
        "exercises": [
            {
                "id": "b1-36-01.ex01",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik beszédpartikula jelenti, hogy 'elvégre' / 'after all'?",
                "options": [
                    "Elvégre",
                    "Mindamellett",
                    "Kivételesen"
                ],
                "correct": 0
            },
            {
                "id": "b1-36-01.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Ez ugyebár mindannyiunk közös érde_____. (interest - ke)",
                "answer": "ke"
            },
            {
                "id": "b1-36-01.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Apropó,", "hallottad", "már", "a", "jó", "híreket?"],
                "solution": ["Apropó,", "hallottad", "már", "a", "jó", "híreket?"]
            },
            {
                "id": "b1-36-01.ex04",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent a nyelvi 'önállóság'?",
                "options": [
                    "Képesség arra, hogy segítség és fordítóprogram nélkül kommunikáljunk",
                    "Egy idegen ország függetlenségi nyilatkozata",
                    "A szótárkönyv eladási ára"
                ],
                "correct": 0
            },
            {
                "id": "b1-36-01.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A rendszeres beszélgetés fejleszti a folyékonyság_____. (fluency - ot)",
                "answer": "ot"
            },
            {
                "id": "b1-36-01.ex06",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik kifejezéssel kapcsolódhatunk egy felmerülő témához?",
                "options": [
                    "Erről jut eszembe",
                    "Ezzel szemben tilos",
                    "Mindennek a tetejébe"
                ],
                "correct": 0
            },
            {
                "id": "b1-36-01.ex07",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "gazdag", "szókincs", "magabiztosságot", "ad", "a", "beszélőnek."],
                "solution": ["A", "gazdag", "szókincs", "magabiztosságot", "ad", "a", "beszélőnek."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-36-01-ex.json", ex_01)

    ex_02 = {
        "lesson": "b1-36-02",
        "exercises": [
            {
                "id": "b1-36-02.ex01",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Hogyan javítjuk ki magunkat természetesen élő beszédben: 'or rather'?",
                "options": [
                    "Vagyis inkább / Pontosabban szólva",
                    "Azonnal megállva",
                    "Teljesen mindegy"
                ],
                "correct": 0
            },
            {
                "id": "b1-36-02.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Ez a feladat, hogy is mondjam _____ komoly felkészülést igényel. (only - csak)",
                "answer": "csak"
            },
            {
                "id": "b1-36-02.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Pontosan", "ezt", "szerettem", "volna", "mondani", "neked."],
                "solution": ["Pontosan", "ezt", "szerettem", "volna", "mondani", "neked."]
            },
            {
                "id": "b1-36-02.ex04",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent a 'spontaneitás' a nyelvhasználatban?",
                "options": [
                    "Természetes, előre be nem tanult közvetlen beszédkészség",
                    "Egy előre felolvasott hivatalos beszéd",
                    "A szótárak pontos memorizálása"
                ],
                "correct": 0
            },
            {
                "id": "b1-36-02.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A jó társalgás élvezetes élmény mindkét fél számá_____. (for - ra)",
                "answer": "ra"
            },
            {
                "id": "b1-36-02.ex06",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik mondat hangsúlyozza a cselekvő személyét (fókusz)?",
                "options": [
                    "Én mentem el a boltba, nem Péter.",
                    "Elmentem a boltba tegnap.",
                    "A boltba elmentem tegnap."
                ],
                "correct": 0
            },
            {
                "id": "b1-36-02.ex07",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "jó", "helyzetfelismerés", "elengedhetetlen", "a", "sikeres", "társalgáshoz."],
                "solution": ["A", "jó", "helyzetfelismerés", "elengedhetetlen", "a", "sikeres", "társalgáshoz."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-36-02-ex.json", ex_02)

    ex_03 = {
        "lesson": "b1-36-03",
        "exercises": [
            {
                "id": "b1-36-03.ex01",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Hogyan tisztázunk egy lehetséges félreértést udvariasan?",
                "options": [
                    "Ha jól értem a szavaidat, úgy gondolod, hogy...",
                    "Egy szót sem értek abból, amit beszélsz!",
                    "Azonnal fejezd be ezt a témát!"
                ],
                "correct": 0
            },
            {
                "id": "b1-36-03.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Attól tartok, hogy félreértettük egy_____ a megbeszélésen. (each other - mást)",
                "answer": "mást"
            },
            {
                "id": "b1-36-03.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Nem", "feltétlenül", "értek", "egyet", "ezzel", "a", "véleménnyel."],
                "solution": ["Nem", "feltétlenül", "értek", "egyet", "ezzel", "a", "véleménnyel."]
            },
            {
                "id": "b1-36-03.ex04",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent a 'találékonyság' egy váratlan kommunikációs helyzetben?",
                "options": [
                    "Kreatív, gyors megoldások alkalmazása a mondanivaló kifejezésére",
                    "A beszélgetés azonnali feladása",
                    "Egy elhagyott tárgy megtalálása az utcán"
                ],
                "correct": 0
            },
            {
                "id": "b1-36-03.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A félreértés tisztázás_____ után megkönnyebbültünk. (clarification - a)",
                "answer": "a"
            },
            {
                "id": "b1-36-03.ex06",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Hogyan mondjuk udvariasan: 'Allow me to add that...'?",
                "options": [
                    "Hadd tegyem hozzá, hogy...",
                    "Követelem, hogy tudd...",
                    "Nem érdekel, de elmondom..."
                ],
                "correct": 0
            },
            {
                "id": "b1-36-03.ex07",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "váratlan", "helyzetekben", "fontos", "a", "nyugalom", "megőrzése."],
                "solution": ["A", "váratlan", "helyzetekben", "fontos", "a", "nyugalom", "megőrzése."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-36-03-ex.json", ex_03)

    ex_04 = {
        "lesson": "b1-36-04",
        "exercises": [
            {
                "id": "b1-36-04.ex01",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent a 'képben van' kifejezés a mindennapi beszédben?",
                "options": [
                    "Jól informált, ismeri a helyzet állását",
                    "Szerepel egy családi fényképen",
                    "Képzőművészeti galériában dolgozik"
                ],
                "correct": 0
            },
            {
                "id": "b1-36-04.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Folyamatosan tanulnom kell, hogy lépést tart_____ a technológiával. (keep pace - sak)",
                "answer": "sak"
            },
            {
                "id": "b1-36-04.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Végre", "dűlőre", "jutottunk", "a", "fontos", "kérdésekben."],
                "solution": ["Végre", "dűlőre", "jutottunk", "a", "fontos", "kérdésekben."]
            },
            {
                "id": "b1-36-04.ex04",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Mikor használjuk a tegeződést (te) hivatalos Önözés helyett?",
                "options": [
                    "Barátok, családtagok között, vagy ha a felek megegyeztek a tegeződésben",
                    "Hivatalos bírósági tárgyaláson a bíróval",
                    "Első találkozáskor egy minisztériumi ügyintézővel"
                ],
                "correct": 0
            },
            {
                "id": "b1-36-04.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A különböző stílusárnyalat_____ finoman jelzik a tiszteletet. (nuances - ok)",
                "answer": "ok"
            },
            {
                "id": "b1-36-04.ex06",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent a 'dűlőre jut' szófordulat?",
                "options": [
                    "Megállapodásra jut, döntést hoz a vitás ügyben",
                    "Eltéved egy vidéki földúton",
                    "Leül pihenni az árok partján"
                ],
                "correct": 0
            },
            {
                "id": "b1-36-04.ex07",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "helyes", "nyelvi", "regiszter", "megválasztása", "kulcsfontosságú."],
                "solution": ["A", "helyes", "nyelvi", "regiszter", "megválasztása", "kulcsfontosságú."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-36-04-ex.json", ex_04)

    ex_05 = {
        "lesson": "b1-36-05",
        "exercises": [
            {
                "id": "b1-36-05.ex01",
                "type": "multiple-choice",
                "category": "literature",
                "question": "Mit mondott Dobó István az egri vár falairól Gárdonyi regényében?",
                "options": [
                    "A falak ereje nem a kőben van, hanem a védők lelkében",
                    "A falak túl gyengék, azonnal menekülnünk kell",
                    "Kizárólag az aranyfalak tudják megvédeni a várost"
                ],
                "correct": 0
            },
            {
                "id": "b1-36-05.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Képes vagyok arra, hogy önállóan boldogul_____ Magyarországon. (thrive - jak)",
                "answer": "jak"
            },
            {
                "id": "b1-36-05.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Saját", "szavaimmal", "is", "ki", "tudom", "fejezni", "a", "gondolataimat."],
                "solution": ["Saját", "szavaimmal", "is", "ki", "tudom", "fejezni", "a", "gondolataimat."]
            },
            {
                "id": "b1-36-05.ex04",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent a 'nyelvtudás' fogalma a B1 szint végén?",
                "options": [
                    "Gyakorlati, önálló kommunikációs képességet a mindennapi életben",
                    "Csak néhány köszönési forma ismeretét",
                    "A teljes akadémiai nyelvészeti szótár fejből tudását"
                ],
                "correct": 0
            },
            {
                "id": "b1-36-05.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A sikeres B1 szint új távlat_____ nyit a tanulásban. (perspectives - okat)",
                "answer": "okat"
            },
            {
                "id": "b1-36-05.ex06",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Hogyan fogalmazható meg a záró összegzés büszkesége?",
                "options": [
                    "Büszke vagyok a kitartásomra és az elért nyelvtudásomra!",
                    "Semmit sem tanultam meg a kurzus során.",
                    "A magyar nyelv túl nehéz és feladom."
                ],
                "correct": 0
            },
            {
                "id": "b1-36-05.ex07",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "továbbfejlődés", "útja", "mostantól", "nyitva", "áll", "előttem."],
                "solution": ["A", "továbbfejlődés", "útja", "mostantól", "nyitva", "áll", "előttem."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-36-05-ex.json", ex_05)

    ex_consolidation = {
        "lesson": "b1-36-consolidation",
        "exercises": [
            {
                "id": "b1-36-consolidation.ex01",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik állítás jellemzi legjobban az önálló (B1) magyar nyelvhasználót?",
                "options": [
                    "Magabiztosan, összefüggően fejezi ki véleményét, megérti a lényeget és feltalálja magát váratlan helyzetekben",
                    "Kizárólag egyszerű tőmondatokat tud elismételni előre megírt papírról",
                    "Csak írásban tud kommunikálni, szóban egyáltalán nem"
                ],
                "correct": 0
            },
            {
                "id": "b1-36-consolidation.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Bár nehéz volt az út, még_____ elértem a célomat. (still - is)",
                "answer": "is"
            },
            {
                "id": "b1-36-consolidation.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Önállóan", "és", "természetesen", "beszélek", "magyarul."],
                "solution": ["Önállóan", "és", "természetesen", "beszélek", "magyarul."]
            },
            {
                "id": "b1-36-consolidation.ex04",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit üzen Gárdonyi Géza Egri csillagok című regényének híres mondata?",
                "options": [
                    "Az emberi elszántság, bátorság és összetartás legyőzi a fizikai akadályokat",
                    "A kőfalakat magasabbra kell építeni téglából",
                    "A harcban csak a fegyverek száma számít"
                ],
                "correct": 0
            },
            {
                "id": "b1-36-consolidation.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A kitartó munka meghozta a maga gyümölcs_____. (its fruit - ét)",
                "answer": "ét"
            },
            {
                "id": "b1-36-consolidation.ex06",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik szófordulat fejezi ki a megegyezést egy hosszú tárgyalás után?",
                "options": [
                    "Dűlőre jutottunk",
                    "Kútba esett a terv",
                    "Füstbe ment az elképzelés"
                ],
                "correct": 0
            },
            {
                "id": "b1-36-consolidation.ex07",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "magabiztos", "nyelvtudás", "egy", "életre", "szóló", "kincs."],
                "solution": ["A", "magabiztos", "nyelvtudás", "egy", "életre", "szóló", "kincs."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-36-consolidation-ex.json", ex_consolidation)

    # -------------------------------------------------------------------------
    # 5. Lesson Files (6 files)
    # -------------------------------------------------------------------------
    lesson_01 = {
        "id": "lesson.b1.36-01",
        "unit": 36,
        "title": "Mindent egybevetve (Putting It All Together)",
        "level": "B1",
        "grammar": "Pragmatic Discourse Particles (ugyebár, elvégre) & Conversational Transitions",
        "sections": [
            {
                "type": "goal",
                "title": "Lesson Goals",
                "items": [
                    "I can use conversational discourse particles like ugyebár and elvégre.",
                    "I can make natural conversational shifts with apropó and erről jut eszembe.",
                    "I can master 4 vocabulary words for independence, fluency, and self-confidence.",
                    "I can connect ideas smoothly across extended Hungarian speech."
                ]
            },
            {"type": "recycle", "count": 3},
            {"type": "vocabulary", "ref": "vocabulary/b1/b1-36-01-voc.json"},
            {"type": "grammar", "ref": "grammar/b1/b1-36-01-a-gr.json"},
            {"type": "grammar", "ref": "grammar/b1/b1-36-01-b-gr.json"},
            {
                "type": "exercise-group",
                "title": "Practice",
                "ref": "exercises/b1/b1-36-01-ex.json",
                "exerciseRefs": [
                    "b1-36-01.ex01",
                    "b1-36-01.ex02",
                    "b1-36-01.ex03",
                    "b1-36-01.ex04",
                    "b1-36-01.ex05",
                    "b1-36-01.ex06",
                    "b1-36-01.ex07"
                ]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-36-01.json", lesson_01)

    lesson_02 = {
        "id": "lesson.b1.36-02",
        "unit": 36,
        "title": "Egy igazi beszélgetés (A Real Conversation)",
        "level": "B1",
        "grammar": "Spontaneous Self-Correction (vagyis inkább) & Nuanced Expressive Word Order",
        "sections": [
            {
                "type": "goal",
                "title": "Lesson Goals",
                "items": [
                    "I can self-correct naturally during speech using vagyis inkább and pontosabban.",
                    "I can exploit expressive Hungarian word order for subtle focal emphasis.",
                    "I can learn 4 words for live conversation, spontaneity, and room reading.",
                    "I can participate with confidence in rapid, authentic group discussions."
                ]
            },
            {"type": "recycle", "count": 3},
            {"type": "vocabulary", "ref": "vocabulary/b1/b1-36-02-voc.json"},
            {"type": "grammar", "ref": "grammar/b1/b1-36-02-a-gr.json"},
            {"type": "grammar", "ref": "grammar/b1/b1-36-02-b-gr.json"},
            {
                "type": "exercise-group",
                "title": "Practice",
                "ref": "exercises/b1/b1-36-02-ex.json",
                "exerciseRefs": [
                    "b1-36-02.ex01",
                    "b1-36-02.ex02",
                    "b1-36-02.ex03",
                    "b1-36-02.ex04",
                    "b1-36-02.ex05",
                    "b1-36-02.ex06",
                    "b1-36-02.ex07"
                ]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-36-02.json", lesson_02)

    lesson_03 = {
        "id": "lesson.b1.36-03",
        "unit": 36,
        "title": "Váratlan helyzetek (Handling the Unexpected)",
        "level": "B1",
        "grammar": "Negotiating Clarification & Polite Assertiveness with Attól tartok, hogy...",
        "sections": [
            {
                "type": "goal",
                "title": "Lesson Goals",
                "items": [
                    "I can resolve communication misunderstandings politely using ha jól értem.",
                    "I can express disagreement with diplomatic softeners like attól tartok, hogy...",
                    "I can acquire 4 vocabulary terms for unexpected turns and resourcefulness.",
                    "I can navigate complex social misunderstandings smoothly and effectively."
                ]
            },
            {"type": "recycle", "count": 3},
            {"type": "vocabulary", "ref": "vocabulary/b1/b1-36-03-voc.json"},
            {"type": "grammar", "ref": "grammar/b1/b1-36-03-a-gr.json"},
            {"type": "grammar", "ref": "grammar/b1/b1-36-03-b-gr.json"},
            {
                "type": "exercise-group",
                "title": "Practice",
                "ref": "exercises/b1/b1-36-03-ex.json",
                "exerciseRefs": [
                    "b1-36-03.ex01",
                    "b1-36-03.ex02",
                    "b1-36-03.ex03",
                    "b1-36-03.ex04",
                    "b1-36-03.ex05",
                    "b1-36-03.ex06",
                    "b1-36-03.ex07"
                ]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-36-03.json", lesson_03)

    lesson_04 = {
        "id": "lesson.b1.36-04",
        "unit": 36,
        "title": "A sorok között olvasva (Reading Between the Lines)",
        "level": "B1",
        "grammar": "Register Modulation (Ön vs Te) & Essential Spoken Idioms (dűlőre jut, képben van)",
        "sections": [
            {
                "type": "goal",
                "title": "Lesson Goals",
                "items": [
                    "I can switch appropriately between formal (Ön) and informal (te) registers.",
                    "I can deploy key spoken idioms like dűlőre jut and lépést tart.",
                    "I can master 4 words for stylistic nuances, registers, and colloquial expressions.",
                    "I can interpret subtext, subtle humor, and implicit meaning in conversations."
                ]
            },
            {"type": "recycle", "count": 3},
            {"type": "vocabulary", "ref": "vocabulary/b1/b1-36-04-voc.json"},
            {"type": "grammar", "ref": "grammar/b1/b1-36-04-a-gr.json"},
            {"type": "grammar", "ref": "grammar/b1/b1-36-04-b-gr.json"},
            {
                "type": "exercise-group",
                "title": "Practice",
                "ref": "exercises/b1/b1-36-04-ex.json",
                "exerciseRefs": [
                    "b1-36-04.ex01",
                    "b1-36-04.ex02",
                    "b1-36-04.ex03",
                    "b1-36-04.ex04",
                    "b1-36-04.ex05",
                    "b1-36-04.ex06",
                    "b1-36-04.ex07"
                ]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-36-04.json", lesson_04)

    lesson_05 = {
        "id": "lesson.b1.36-05",
        "unit": 36,
        "title": "Merre tovább? (Where I Go From Here: Gárdonyi Géza)",
        "level": "B1",
        "grammar": "B1 Subordination Synthesis & Autonomous Expression in Hungarian",
        "sections": [
            {
                "type": "goal",
                "title": "Lesson Goals",
                "items": [
                    "I can construct multi-tiered compound and complex Hungarian sentences with ease.",
                    "I can express complex thoughts and future ambitions in my own words.",
                    "I can learn 4 words for long-term perspectives and continued mastery.",
                    "I can read the inspiring heroic oath of Dobó István from Gárdonyi's Egri csillagok."
                ]
            },
            {"type": "recycle", "count": 3},
            {"type": "vocabulary", "ref": "vocabulary/b1/b1-36-05-voc.json"},
            {"type": "grammar", "ref": "grammar/b1/b1-36-05-a-gr.json"},
            {"type": "grammar", "ref": "grammar/b1/b1-36-05-b-gr.json"},
            {"type": "story", "ref": "stories/classics/b1/b1-36-gardonyi.json"},
            {
                "type": "exercise-group",
                "title": "Practice",
                "ref": "exercises/b1/b1-36-05-ex.json",
                "exerciseRefs": [
                    "b1-36-05.ex01",
                    "b1-36-05.ex02",
                    "b1-36-05.ex03",
                    "b1-36-05.ex04",
                    "b1-36-05.ex05",
                    "b1-36-05.ex06",
                    "b1-36-05.ex07"
                ]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-36-05.json", lesson_05)

    lesson_consolidation = {
        "id": "lesson.b1.36-consolidation",
        "unit": 36,
        "title": "B1 Core Capstone: Önálló magyar nyelvhasználat (Consolidation)",
        "level": "B1",
        "grammar": "Grand synthesis of all B1 grammar structures, communicative agility, and idioms",
        "sections": [
            {
                "type": "goal",
                "title": "Consolidation Goals",
                "items": [
                    "Consolidate all 20 capstone vocabulary items for advanced fluency and autonomy.",
                    "Demonstrate effortless control over Hungarian word order, particles, and complex subordination.",
                    "Confirm full independent ability to communicate, debate, and thrive in Hungarian.",
                    "Graduate with pride from the Hungarian B1 Core Curriculum!"
                ]
            },
            {
                "type": "exercise-group",
                "title": "Consolidation Practice",
                "ref": "exercises/b1/b1-36-consolidation-ex.json",
                "exerciseRefs": [
                    "b1-36-consolidation.ex01",
                    "b1-36-consolidation.ex02",
                    "b1-36-consolidation.ex03",
                    "b1-36-consolidation.ex04",
                    "b1-36-consolidation.ex05",
                    "b1-36-consolidation.ex06",
                    "b1-36-consolidation.ex07"
                ]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-36-consolidation.json", lesson_consolidation)

if __name__ == "__main__":
    build_unit_36_core()
