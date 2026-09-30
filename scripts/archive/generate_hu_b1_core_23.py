#!/usr/bin/env python3
"""Generate Hungarian B1 Core Unit 23: Making Decisions (b1-23)."""

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

def build_unit_23_core():
    # -------------------------------------------------------------------------
    # 1. Vocabulary Files (4 words each = 20 words total)
    # -------------------------------------------------------------------------
    voc_01 = {
        "id": "vocab.b1.23.01",
        "lesson": "b1-23-01",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "döntés", "translation": "decision, choice", "pos": "noun"},
            {"lemma": "választás", "translation": "choice, election, selection", "pos": "noun"},
            {"lemma": "alternatíva", "translation": "alternative, optional path", "pos": "noun"},
            {"lemma": "határozat", "translation": "formal resolution, decree", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-23-01-voc.json", voc_01)

    voc_02 = {
        "id": "vocab.b1.23.02",
        "lesson": "b1-23-02",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "mérlegelés", "translation": "weighing, deliberation, consideration", "pos": "noun"},
            {"lemma": "tényező", "translation": "factor, influential element", "pos": "noun"},
            {"lemma": "előny", "translation": "advantage, benefit, pro", "pos": "noun"},
            {"lemma": "hátrány", "translation": "disadvantage, drawback, con", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-23-02-voc.json", voc_02)

    voc_03 = {
        "id": "vocab.b1.23.03",
        "lesson": "b1-23-03",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "dilemma", "translation": "dilemma, difficult choice", "pos": "noun"},
            {"lemma": "habozás", "translation": "hesitation, vacillation", "pos": "noun"},
            {"lemma": "elhatározás", "translation": "determination, resolve, resolution", "pos": "noun"},
            {"lemma": "kétely", "translation": "scruple, inner doubt", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-23-03-voc.json", voc_03)

    voc_04 = {
        "id": "vocab.b1.23.04",
        "lesson": "b1-23-04",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "következmény", "translation": "consequence, aftermath", "pos": "noun"},
            {"lemma": "felelősségvállalás", "translation": "taking responsibility, accountability", "pos": "noun"},
            {"lemma": "kompromisszum", "translation": "compromise, mutual concession", "pos": "noun"},
            {"lemma": "egyezség", "translation": "agreement, pact, accord", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-23-04-voc.json", voc_04)

    voc_05 = {
        "id": "vocab.b1.23.05",
        "lesson": "b1-23-05",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "véglegesítés", "translation": "finalization, finalizing a decision", "pos": "noun"},
            {"lemma": "elköteleződés", "translation": "commitment, pledging dedication", "pos": "noun"},
            {"lemma": "megvalósítás", "translation": "implementation, execution", "pos": "noun"},
            {"lemma": "visszalépés", "translation": "withdrawal, backing out, retreat", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-23-05-voc.json", voc_05)

    # -------------------------------------------------------------------------
    # 2. Grammar Files (2 per regular lesson = 10 files)
    # -------------------------------------------------------------------------
    gr_01_a = {
        "id": "grammar.b1.23.01.decision-verbs",
        "title": "Verbs of Deciding: dönt vmiről, határoz vmi mellett",
        "sections": [
            {
                "type": "text",
                "title": "Government of Decision Verbs",
                "content": "The primary verb *dönt* ('to decide') takes *-ról/-ről* for the subject matter (*dönt a kérdésről*), or *mellett / ellen* for deciding in favor of or against something (*az új ajánlat mellett döntöttünk*). *Elhatároz* ('to make up one's mind') takes an infinitive (*elhatároztam, hogy továbbtanulok*)."
            },
            {
                "type": "examples",
                "title": "Decision verbs in context",
                "items": [
                    {
                        "spanish": "Hosszas gondolkodás után a cég vezetése a bővítés mellett döntött.",
                        "english": "After lengthy consideration, the company management decided in favor of expansion."
                    },
                    {
                        "spanish": "Nehéz dönteni arról, hogy melyik szakmát válasszam az egyetem után.",
                        "english": "It is difficult to decide which profession I should choose after university."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-23-01-a-gr.json", gr_01_a)

    gr_01_b = {
        "id": "grammar.b1.23.01.deliberative-valasztas",
        "title": "Deliberative Formulations: választás előtt áll, döntésre jut",
        "sections": [
            {
                "type": "text",
                "title": "Idiomatic Decision States",
                "content": "Hungarian uses picturesque prepositional and nominal idioms for decision stages: *választás előtt áll* ('to face a choice'), *döntésre jut* ('to reach a decision'), *határozatot hoz* ('to adopt a formal resolution')."
            },
            {
                "type": "examples",
                "title": "Decision phases",
                "items": [
                    {
                        "spanish": "A bizottság tegnap délután végre egyhangú döntésre jutott.",
                        "english": "The committee finally reached a unanimous decision yesterday afternoon."
                    },
                    {
                        "spanish": "Mindannyian nehéz választás előtt állunk a jövő évi költségvetést illetően.",
                        "english": "We all face a difficult choice regarding next year's budget."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-23-01-b-gr.json", gr_01_b)

    gr_02_a = {
        "id": "grammar.b1.23.02.weighing-pros-cons",
        "title": "Weighing Options: mérlegeli az előnyöket és hátrányokat",
        "sections": [
            {
                "type": "text",
                "title": "Balancing Pros and Cons",
                "content": "To weigh arguments analytically: *mérlegeli a lehetőségeket* ('weighs the options'), *számba vesz minden tényezőt* ('takes every factor into account'), *több előnye van, mint hátránya* ('has more pros than cons')."
            },
            {
                "type": "examples",
                "title": "Weighing factors",
                "items": [
                    {
                        "spanish": "Mielőtt aláírnád a szerződést, alaposan mérlegeld az előnyöket és a kockázatokat!",
                        "english": "Before signing the contract, thoroughly weigh the advantages and risks!"
                    },
                    {
                        "spanish": "Minden lényeges tényezőt számba kell vennünk a felelős lépésekhez.",
                        "english": "We must take every essential factor into account for responsible steps."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-23-02-a-gr.json", gr_02_a)

    gr_02_b = {
        "id": "grammar.b1.23.02.egyreszt-masreszt",
        "title": "Contrasting Deliberations: egyrészt... másrészt...",
        "sections": [
            {
                "type": "text",
                "title": "Balancing Paired Adverbs",
                "content": "*Egyrészt... másrészt...* ('on the one hand... on the other hand...') is the classical rhetorical device for balancing conflicting aspects of a difficult choice."
            },
            {
                "type": "examples",
                "title": "Paired contrast",
                "items": [
                    {
                        "spanish": "Egyrészt vonzó a magasabb fizetés, másrészt nem szeretnék elköltözni a szülővárosomból.",
                        "english": "On the one hand the higher salary is attractive, on the other hand I wouldn't like to move away from my hometown."
                    },
                    {
                        "spanish": "Egyrészt sürgős a döntés, másrészt nem szabad elhamarkodott lépést tenni.",
                        "english": "On the one hand the decision is urgent, on the other hand one must not make a hasty step."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-23-02-b-gr.json", gr_02_b)

    gr_03_a = {
        "id": "grammar.b1.23.03.dilemma-expressions",
        "title": "Dilemmas and Hesitation: habozik, kétségek gyötrik",
        "sections": [
            {
                "type": "text",
                "title": "Expressing Indecision",
                "content": "Verbs of hesitation and moral conflict: *habozik* ('to hesitate'), *huzakodik* ('to waver/drag one's feet'), *kétségek között őrlődik* ('to be torn between doubts'), *dilemma elé állít vkit* ('to confront someone with a dilemma')."
            },
            {
                "type": "examples",
                "title": "Hesitation in discourse",
                "items": [
                    {
                        "spanish": "Nem szabad sokáig habozni, mert a kedvező alkalom hamar elszáll.",
                        "english": "One must not hesitate for long, because the favorable opportunity quickly passes."
                    },
                    {
                        "spanish": "A bíró nehéz erkölcsi dilemma elé került a per során.",
                        "english": "The judge was confronted with a difficult moral dilemma during the trial."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-23-03-a-gr.json", gr_03_a)

    gr_03_b = {
        "id": "grammar.b1.23.03.conditional-deliberation",
        "title": "Hypothetical Advice: Mit tennél a helyemben?",
        "sections": [
            {
                "type": "text",
                "title": "Asking for and Giving Guidance",
                "content": "To solicit advice in a dilemma: *Mit tennél a helyemben?* ('What would you do in my shoes?'). Giving advice: *A helyedben én... conditional* (*A helyedben én elfogadnám az ajánlatot*)."
            },
            {
                "type": "examples",
                "title": "Hypothetical advice in action",
                "items": [
                    {
                        "spanish": "Ha a helyemben lennél, te melyik ajánlatot választanád?",
                        "english": "If you were in my place, which offer would you choose?"
                    },
                    {
                        "spanish": "A te helyedben nem haboznék egyetlen percig sem.",
                        "english": "In your place I wouldn't hesitate for a single minute."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-23-03-b-gr.json", gr_03_b)

    gr_04_a = {
        "id": "grammar.b1.23.04.taking-responsibility",
        "title": "Responsibility & Consequences: felelősséget vállal vmiért",
        "sections": [
            {
                "type": "text",
                "title": "Causality of Outcomes",
                "content": "*Felelősséget vállal vmiért* ('to take responsibility for sth'), *viseli a következményeket* ('to bear the consequences'), *számol a hatásokkal* ('to anticipate the effects')."
            },
            {
                "type": "examples",
                "title": "Accountability phrases",
                "items": [
                    {
                        "spanish": "A vezető kész volt személyesen vállalni a felelősséget a csapat döntéséért.",
                        "english": "The leader was ready to personally take responsibility for the team's decision."
                    },
                    {
                        "spanish": "Minden felnőtt embernek viselnie kell tettei következményeit.",
                        "english": "Every adult must bear the consequences of their actions."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-23-04-a-gr.json", gr_04_a)

    gr_04_b = {
        "id": "grammar.b1.23.04.compromise-connectors",
        "title": "Compromise and Concession: kompromisszumot köt, megegyezik vmiben",
        "sections": [
            {
                "type": "text",
                "title": "Achieving Consensus",
                "content": "*Kompromisszumot köt* ('to make a compromise'), *közös nevezőre jut* ('to find common ground'), *megegyezik vmiben* ('to agree on something')."
            },
            {
                "type": "examples",
                "title": "Consensus phrases",
                "items": [
                    {
                        "spanish": "A felek ésszerű kompromisszumot kötöttek a békés együttműködés érdekében.",
                        "english": "The parties made a sensible compromise in the interest of peaceful cooperation."
                    },
                    {
                        "spanish": "Hosszú vita után végre sikerült közös nevezőre jutniuk a vitás kérdésekben.",
                        "english": "After a long debate they finally succeeded in finding common ground on disputed issues."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-23-04-b-gr.json", gr_04_b)

    gr_05_a = {
        "id": "grammar.b1.23.05.finalizing-decisions",
        "title": "Finalizing Choices: pontot tesz a végére, elkötelezi magát",
        "sections": [
            {
                "type": "text",
                "title": "Sealing Decisions",
                "content": "*Pontot tesz az ügy végére* ('to put an end to the matter / conclude'), *elkötelezi magát vmi mellett* ('to commit oneself to sth'), *végérvényesen eldönt* ('to decide definitively')."
            },
            {
                "type": "examples",
                "title": "Finalizing idioms",
                "items": [
                    {
                        "spanish": "Ideje pontot tenni a bizonytalanság végére, és végre cselekedni!",
                        "english": "It is time to put an end to uncertainty and finally act!"
                    },
                    {
                        "spanish": "A kutatócsoport véglegesítette a következő öt évre szóló munkatervet.",
                        "english": "The research group finalized the work plan for the next five years."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-23-05-a-gr.json", gr_05_a)

    gr_05_b = {
        "id": "grammar.b1.23.05.no-turning-back",
        "title": "Points of No Return: nincs visszaút, el van vetve a kocka",
        "sections": [
            {
                "type": "text",
                "title": "Irreversible Commitments",
                "content": "*Nincs visszaút* ('there is no turning back'), *a kocka el van vetve* ('the die is cast'), *kitart a döntése mellett* ('stands firmly by one's decision')."
            },
            {
                "type": "examples",
                "title": "Irreversibility idioms",
                "items": [
                    {
                        "spanish": "Miután elindult a hajó a kikötőből, már nem volt visszaút.",
                        "english": "Once the ship departed from the harbor, there was no turning back."
                    },
                    {
                        "spanish": "A polgármester a kritikák ellenére szilárdan kitartott a döntése mellett.",
                        "english": "Despite the criticisms, the mayor firmly stood by his decision."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-23-05-b-gr.json", gr_05_b)

    # -------------------------------------------------------------------------
    # 3. Exercise Files (01 to 05 + consolidation)
    # -------------------------------------------------------------------------
    ex_01 = {
        "lesson": "b1-23-01",
        "exercises": [
            {
                "id": "b1-23-01.ex01",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent az 'alternatíva' szó a döntéshozatalban?",
                "options": [
                    "Egy lehetséges másik választási lehetőség vagy megoldási út.",
                    "Egy visszavonhatatlan kötelező büntetés.",
                    "Egy kizárólag katonai célra gyártott jármű."
                ],
                "correct": 0
            },
            {
                "id": "b1-23-01.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Hosszas vita után a vezetőség az új technológia bevezetése _____ döntött. (in favor of - mellett)",
                "answer": "mellett"
            },
            {
                "id": "b1-23-01.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "bizottság", "tegnap", "délután", "egyhangú", "döntésre", "jutott."],
                "solution": ["A", "bizottság", "tegnap", "délután", "egyhangú", "döntésre", "jutott."]
            },
            {
                "id": "b1-23-01.ex04",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Melyik kifejezés jelenti azt, hogy hivatalos határozatot fogad el egy testület?",
                "options": [
                    "Határozatot hoz.",
                    "Határozatot veszít.",
                    "Határozatot felejt el."
                ],
                "correct": 0
            },
            {
                "id": "b1-23-01.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "Mindannyian rendkívül nehéz válasz_____ előtt állunk a jövőnket illetően. (choice - tás)",
                "answer": "tás"
            },
            {
                "id": "b1-23-01.ex06",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Hogyan mondjuk helyesen magyarul: 'I decided to learn Hungarian'?",
                "options": [
                    "Elhatároztam, hogy megtanulok magyarul.",
                    "Döntöttem bele, hogy magyarul tanulok.",
                    "Elhatároztam magyarul tanulásról."
                ],
                "correct": 0
            },
            {
                "id": "b1-23-01.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Nehéz dönteni arról, _____ melyik ajánlat a legkedvezőbb hosszú távon. (that - hogy)",
                "answer": "hogy"
            },
            {
                "id": "b1-23-01.ex08",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "két", "alternatíva", "között", "jelentős", "különbség", "van."],
                "solution": ["A", "két", "alternatíva", "között", "jelentős", "különbség", "van."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-23-01-ex.json", ex_01)

    ex_02 = {
        "lesson": "b1-23-02",
        "exercises": [
            {
                "id": "b1-23-02.ex01",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent a 'mérlegelés' folyamata?",
                "options": [
                    "A mellette és ellene szóló érvek, előnyök és hátrányok alapos átgondolását.",
                    "Kizárólag a boltban vásárolt zöldségek súlyának megmérését.",
                    "Egy gyors és meggondolatlan cselekedetet."
                ],
                "correct": 0
            },
            {
                "id": "b1-23-02.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Egyrészt vonzó a feladat, más_____ rendkívül sok utazással jár. (on the other hand - részt)",
                "answer": "részt"
            },
            {
                "id": "b1-23-02.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Minden", "lényeges", "tényezőt", "alaposan", "számba", "kell", "vennünk."],
                "solution": ["Minden", "lényeges", "tényezőt", "alaposan", "számba", "kell", "vennünk."]
            },
            {
                "id": "b1-23-02.ex04",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mi az 'előny' ellentéte?",
                "options": [
                    "Hátrány.",
                    "Győzelem.",
                    "Eredmény."
                ],
                "correct": 0
            },
            {
                "id": "b1-23-02.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A döntés meghozatala előtt minden lényeges tény_____ mérlegelni kell. (factor - ezőt)",
                "answer": "ezőt"
            },
            {
                "id": "b1-23-02.ex06",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik kifejezés fejezi ki a szempontok összehasonlítását?",
                "options": [
                    "Egyrészt... másrészt...",
                    "Se nem... se nem...",
                    "Ezért... tehát..."
                ],
                "correct": 0
            },
            {
                "id": "b1-23-02.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A javaslatnak több előnye van, _____ hátránya. (than - mint)",
                "answer": "mint"
            },
            {
                "id": "b1-23-02.ex08",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["Alaposan", "mérlegeltük", "a", "döntés", "összes", "várható", "következményét."],
                "solution": ["Alaposan", "mérlegeltük", "a", "döntés", "összes", "várható", "következményét."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-23-02-ex.json", ex_02)

    ex_03 = {
        "lesson": "b1-23-03",
        "exercises": [
            {
                "id": "b1-23-03.ex01",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mi az a 'dilemma'?",
                "options": [
                    "Olyan nehéz helyzet, amelyben két egyformán nehéz vagy kellemetlen lehetőség közül kell választani.",
                    "Egy orvosi gyógyszer neve lázcsillapításra.",
                    "Egy zenei ritmus a reneszánsz táncokban."
                ],
                "correct": 0
            },
            {
                "id": "b1-23-03.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Mit tennél a hely_____ ebben a bonyolult helyzetben? (in my shoes - emben)",
                "answer": "emben"
            },
            {
                "id": "b1-23-03.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "helyedben", "én", "nem", "haboznék", "egy", "pillanatig", "sem."],
                "solution": ["A", "helyedben", "én", "nem", "haboznék", "egy", "pillanatig", "sem."]
            },
            {
                "id": "b1-23-03.ex04",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent a 'habozás'?",
                "options": [
                    "Bizonytalanságból fakadó tétovázást, a döntés halogatását.",
                    "Gyors és azonnali határozott cselekvést.",
                    "Tiszteletteljes meghajlást egy idősebb előtt."
                ],
                "correct": 0
            },
            {
                "id": "b1-23-03.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "Mély elhatározás és szilárd akarat kell a nehéz célok elérésé_____. (to achieve - hez)",
                "answer": "hez"
            },
            {
                "id": "b1-23-03.ex06",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Hogyan fejezzük ki magyarul: 'I have serious doubts about it'?",
                "options": [
                    "Komoly kétségeim vannak felőle.",
                    "Komoly habozásom van benne.",
                    "Komoly alternatívám van erre."
                ],
                "correct": 0
            },
            {
                "id": "b1-23-03.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Ha a helyemben lennél, te bele_____ az ismeretlenbe? (would jump - vágnál)",
                "answer": "vágnál"
            },
            {
                "id": "b1-23-03.ex08",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "bírót", "komoly", "erkölcsi", "dilemma", "gyötörte", "az", "ítélethozatalban."],
                "solution": ["A", "bírót", "komoly", "erkölcsi", "dilemma", "gyötörte", "az", "ítélethozatalban."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-23-03-ex.json", ex_03)

    ex_04 = {
        "lesson": "b1-23-04",
        "exercises": [
            {
                "id": "b1-23-04.ex01",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent a 'kompromisszum' szó?",
                "options": [
                    "Kölcsönös engedményeken alapuló békés megegyezést.",
                    "A másik fél teljes megsemmisítését a vitában.",
                    "Egy egyoldalú, diktatórikus parancsot."
                ],
                "correct": 0
            },
            {
                "id": "b1-23-04.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Kész vagyok személyesen felelősséget vállalni a döntésért és annak következményei_____. (for its consequences - ért)",
                "answer": "ért"
            },
            {
                "id": "b1-23-04.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "tárgyalópartnerek", "végül", "ésszerű", "kompromisszumot", "kötöttek."],
                "solution": ["A", "tárgyalópartnerek", "végül", "ésszerű", "kompromisszumot", "kötöttek."]
            },
            {
                "id": "b1-23-04.ex04",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit fejez ki a 'felelősségvállalás'?",
                "options": [
                    "Azt, hogy valaki elismeri és vállalja tettei vagy döntései hatásait.",
                    "A felelősség áthárítását más kollégákra.",
                    "A törvényes határidők figyelmen kívül hagyását."
                ],
                "correct": 0
            },
            {
                "id": "b1-23-04.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "Minden döntésnek elkerülhetetlen követ_____ vannak a jövőre nézve. (consequences - kezményei)",
                "answer": "kezményei"
            },
            {
                "id": "b1-23-04.ex06",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik kifejezés jelenti a közös megegyezést egy vitában?",
                "options": [
                    "Közös nevezőre jutnak.",
                    "Külön utakon járnak.",
                    "Ellenségeskedésbe kezdenek."
                ],
                "correct": 0
            },
            {
                "id": "b1-23-04.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A feleknek sikerült közös _____ jutniuk a vitás kérdésekben. (common ground - nevezőre)",
                "answer": "nevezőre"
            },
            {
                "id": "b1-23-04.ex08",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "kölcsönös", "tisztelet", "és", "a", "bizalom", "minden", "egyezség", "alapja."],
                "solution": ["A", "kölcsönös", "tisztelet", "és", "a", "bizalom", "minden", "egyezség", "alapja."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-23-04-ex.json", ex_04)

    ex_05 = {
        "lesson": "b1-23-05",
        "exercises": [
            {
                "id": "b1-23-05.ex01",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent az 'elköteleződés' szó?",
                "options": [
                    "Hűséges és tartós odaadást egy cél, eszme vagy döntés mellett.",
                    "Egy szerződés felbontását néhány nap után.",
                    "Bizonytalan várakozást egy folyosón."
                ],
                "correct": 0
            },
            {
                "id": "b1-23-05.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Ideje pontot tenni a végére, mert innen már nincs vissza_____. (turning back - út)",
                "answer": "út"
            },
            {
                "id": "b1-23-05.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "kocka", "el", "van", "vetve,", "nincs", "többé", "visszaút."],
                "solution": ["A", "kocka", "el", "van", "vetve,", "nincs", "többé", "visszaút."]
            },
            {
                "id": "b1-23-05.ex04",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit fejez ki a 'visszalépés' egy döntési folyamatban?",
                "options": [
                    "Azt, hogy valaki eláll korábbi szándékától, visszavonul.",
                    "Azt, hogy azonnal megkezdi a terv kivitelezését.",
                    "Azt, hogy megduplázza a pénzügyi befektetést."
                ],
                "correct": 0
            },
            {
                "id": "b1-23-05.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A tervek véglegesítése után azonnal megkezdődik a megvaló_____. (implementation - sítás)",
                "answer": "sítás"
            },
            {
                "id": "b1-23-05.ex06",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Mit jelent az a kifejezés, hogy 'pontot tesz az ügy végére'?",
                "options": [
                    "Végérvényesen lezárja a vitát vagy döntést.",
                    "Írásbeli dolgozatot kezd írni a füzetbe.",
                    "Megkérdőjelezi a korábban elfogadott tényeket."
                ],
                "correct": 0
            },
            {
                "id": "b1-23-05.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A vezető a bírálatok ellenére szilárdan kitartott döntése _____. (by / beside - mellett)",
                "answer": "mellett"
            },
            {
                "id": "b1-23-05.ex08",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "hosszú", "távú", "elköteleződés", "nélkülözhetetlen", "a", "sikerhez."],
                "solution": ["A", "hosszú", "távú", "elköteleződés", "nélkülözhetetlen", "a", "sikerhez."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-23-05-ex.json", ex_05)

    ex_consolidation = {
        "lesson": "b1-23-consolidation",
        "exercises": [
            {
                "id": "b1-23-consolidation.ex01",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik vonzattal áll a 'dönt' ige, amikor a támogatott lehetőségre utalunk?",
                "options": [
                    "mellett (Az új terv mellett döntöttünk.)",
                    "felett (Az új terv felett döntöttünk.)",
                    "alatt (Az új terv alatt döntöttünk.)"
                ],
                "correct": 0
            },
            {
                "id": "b1-23-consolidation.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Alaposan mérlegelnünk kell az előnyöket és a hátrányokat, mielőtt döntésre jut_____. (we reach - nánk)",
                "answer": "nánk"
            },
            {
                "id": "b1-23-consolidation.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Egyrészt", "sürgős", "a", "döntés,", "másrészt", "nem", "szabad", "hibázni."],
                "solution": ["Egyrészt", "sürgős", "a", "döntés,", "másrészt", "nem", "szabad", "hibázni."]
            },
            {
                "id": "b1-23-consolidation.ex04",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "Fabriczy bíró úr súlyos di_____ elé került a lőcsei perben. (dilemma - lemmá)",
                "answer": "lemmá"
            },
            {
                "id": "b1-23-consolidation.ex05",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "felelősségteljes", "döntéshozatal", "minden", "vezető", "legfőbb", "kötelessége."],
                "solution": ["A", "felelősségteljes", "döntéshozatal", "minden", "vezető", "legfőbb", "kötelessége."]
            },
            {
                "id": "b1-23-consolidation.ex06",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit fejez ki a 'kompromisszum' egy vitás tárgyaláson?",
                "options": [
                    "Mindkét fél enged valamit a békés megállapodásért.",
                    "Egyik fél sem hajlandó beszélni a másikkal.",
                    "A vita bírósági perré alakul át azonnal."
                ],
                "correct": 0
            },
            {
                "id": "b1-23-consolidation.ex07",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A felek kölcsönös engedmények árán ésszerű egyez_____ jutottak. (accord - ségre)",
                "answer": "ségre"
            },
            {
                "id": "b1-23-consolidation.ex08",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Milyen sorsdöntő választással szembesülnek a szereplők Mikszáth 'A fekete város' című regényében?",
                "options": [
                    "A személyes bosszú, a városi büszkeség és a törvényes igazságszolgáltatás közötti tragikus dilemmával.",
                    "Azzal, hogy melyik színházi előadásra váltsanak páholybérletet.",
                    "A vasúti menetrend módosításának technikai kérdéseivel."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-23-consolidation-ex.json", ex_consolidation)

    # -------------------------------------------------------------------------
    # 4. Classic Story Adaptation for Consolidation
    # -------------------------------------------------------------------------
    story_classic = {
        "id": "story.b1.23.classic",
        "title": "A fekete város",
        "level": "B1",
        "order": 23,
        "type": "classics",
        "estimatedMinutes": 8,
        "summary": "An adaptation of Kálmán Mikszáth's masterwork 'A fekete város'. In the historic Zipser town of Lőcse, Judge Fabriczy and the town council face a fateful dilemma after the killing of the county deputy lieutenant: should they adhere strictly to the unbending letter of municipal law, or seek a peaceful political compromise before hatred engulfs both city and county?",
        "characters": [
            "Fabriczy Pál, Lőcse város bírája",
            "Görgey Pál, szepesi alispán",
            "Németh úr, a városi tanács esküdtje"
        ],
        "location": "A lőcsei városháza tanácsterme és a piactér",
        "author": "Mikszáth Kálmán",
        "work": "A fekete város (1910)",
        "paragraphs": [
            {
                "type": "narration",
                "text": "Lőcse ősi városházájának gótikus boltívei alatt nehéz csend ült a tanácsteremre. Az ablakon túl a felvidéki szél zúgott a Magas-Tátra felől, de bent még fagyosabb volt a hangulat. A városi tanács tagjai élet-halál kérdésében álltak választás előtt."
            },
            {
                "type": "dialogue",
                "speaker": "Fabriczy Pál bíró",
                "text": "Uraim, a törvény nem ismer alkut! A szepesi alispán megsértette Lőcse szabad királyi város privilégiumait. Ha most meghátrálunk, oda a szabadságunk, oda az ősi autonómiánk!"
            },
            {
                "type": "dialogue",
                "speaker": "Németh tanácsos",
                "text": "Bíró uram, kérve kérem, mérlegelje a következményeket! Egyrészt igaz, hogy a város joga szent, másrészt a vármegye fegyveres serege bármikor körülzárhatja falainkat. Nem lenne bölcsebb ésszerű kompromisszumra törekedni, mielőtt vér folyik?"
            },
            {
                "type": "narration",
                "text": "A bíró homlokát ráncolta, ujjai a nehéz pecsétgyűrűt forgatták. Lelke mélyén tudta, hogy a dilemma feloldhatatlan: a büszkeség és a jog merev betűje a pusztulás felé viszi a várost, ám a meghátrálást a polgárok árulásnak tekintenék."
            },
            {
                "type": "dialogue",
                "speaker": "Fabriczy Pál bíró",
                "text": "Mit tennél a helyemben, tanácsos úr? Átengednéd a város kulcsait a vármegye gőgös urainak? Nincs visszaút! A kocka el van vetve, s vállalom a felelősséget a döntésemért a történelem előtt!"
            },
            {
                "type": "narration",
                "text": "A határozat megszületett: Lőcse nem hátrált meg. A városi polgárok fekete posztóba öltöztették a városházát és önmagukat, gyászolva a békét. Mikszáth megrázó regénye örök figyelmeztetés maradt: a legnehezebb döntések nem a jó és a rossz, hanem a kétféle igazság összecsapásából születnek."
            }
        ]
    }
    write_json("content/hu/stories/classics/b1/b1-23-mikszath.json", story_classic)

    # -------------------------------------------------------------------------
    # 5. Lesson Files (01 to 05 + consolidation)
    # -------------------------------------------------------------------------
    for i in range(1, 6):
        padded = f"0{i}"
        titles = {
            "01": ("Facing a Choice", "Választás előtt: Döntés és alternatívák"),
            "02": ("Weighing the Factors", "Mérlegelés és tényezők: Előnyök és hátrányok"),
            "03": ("Dilemmas and Advice", "Dilemmák és habozás: Mit tennél a helyemben?"),
            "04": ("Consequences and Compromise", "Következmények és felelősség: A kompromisszum művészete"),
            "05": ("Finalizing the Decision", "Véglegesítés és elköteleződés: Nincs visszaút")
        }
        en_title, hu_title = titles[padded]
        lesson_data = {
            "id": f"lesson.b1.23-{padded}",
            "unit": 23,
            "title": en_title,
            "level": "B1",
            "grammar": "Decision-Making Idioms, Deliberative Conditionals & Concession Connectors",
            "goal": [
                f"I can understand and use vocabulary for {en_title.lower()}.",
                "I can weigh pros and cons and formulate balanced decisions in Hungarian.",
                "I can ask for advice in difficult dilemmas and negotiate compromises.",
                "I can master four new target vocabulary items in authentic context."
            ],
            "sections": [
                {
                    "type": "goal",
                    "title": "Lesson Goals",
                    "items": [
                        f"I can understand and use vocabulary for {en_title.lower()}.",
                        "I can weigh pros and cons and formulate balanced decisions in Hungarian.",
                        "I can ask for advice in difficult dilemmas and negotiate compromises.",
                        "I can master four new target vocabulary items in authentic context."
                    ]
                },
                {"type": "recycle", "title": "Quick Review"},
                {"type": "grammar", "ref": f"grammar/b1/b1-23-{padded}-a-gr.json"},
                {"type": "grammar", "ref": f"grammar/b1/b1-23-{padded}-b-gr.json"},
                {"type": "vocabulary", "title": "Lesson Vocabulary", "ref": f"vocabulary/b1/b1-23-{padded}-voc.json"},
                {
                    "type": "exercise-group",
                    "title": "Practice",
                    "ref": f"exercises/b1/b1-23-{padded}-ex.json",
                    "exerciseRefs": [f"b1-23-{padded}.ex0{k}" for k in range(1, 9)]
                }
            ]
        }
        write_json(f"content/hu/lessons/b1/b1-23-{padded}.json", lesson_data)

    consolidation_data = {
        "id": "lesson.b1.23-consolidation",
        "unit": 23,
        "title": "Unit 23 Consolidation",
        "level": "B1",
        "grammar": "Consolidation of Deliberative Rhetoric, Compromise & Ethical Decisions",
        "sections": [
            {
                "type": "story",
                "title": "A fekete város (Mikszáth Kálmán)",
                "ref": "stories/classics/b1/b1-23-mikszath.json"
            },
            {
                "type": "exercise-group",
                "title": "Consolidation Practice",
                "ref": "exercises/b1/b1-23-consolidation-ex.json",
                "exerciseRefs": [f"b1-23-consolidation.ex0{k}" for k in range(1, 9)]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-23-consolidation.json", consolidation_data)
    print("Successfully built Hungarian B1 Core Unit 23 (b1-23)!")

if __name__ == "__main__":
    build_unit_23_core()
