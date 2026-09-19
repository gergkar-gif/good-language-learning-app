#!/usr/bin/env python3
"""Generate Hungarian B1 Core Unit 28: Rules, Rights & Responsibilities (b1-28)."""

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

def build_unit_28_core():
    # -------------------------------------------------------------------------
    # 1. Vocabulary Files (4 words each = 20 words total)
    # -------------------------------------------------------------------------
    voc_01 = {
        "id": "vocab.b1.28.01",
        "lesson": "b1-28-01",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "szabályzat", "translation": "code of regulations, official rulebook", "pos": "noun"},
            {"lemma": "előírás", "translation": "prescription, statutory requirement, directive", "pos": "noun"},
            {"lemma": "betartás", "translation": "observance, adherence to rules", "pos": "noun"},
            {"lemma": "megszegés", "translation": "infringement, violation, breach of rules", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-28-01-voc.json", voc_01)

    voc_02 = {
        "id": "vocab.b1.28.02",
        "lesson": "b1-28-02",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "jog", "translation": "right, entitlement, law", "pos": "noun"},
            {"lemma": "kötelesség", "translation": "duty, civic obligation", "pos": "noun"},
            {"lemma": "felelősség", "translation": "responsibility, accountability", "pos": "noun"},
            {"lemma": "számonkérés", "translation": "holding accountable, auditing, calling to account", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-28-02-voc.json", voc_02)

    voc_03 = {
        "id": "vocab.b1.28.03",
        "lesson": "b1-28-03",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "engedély", "translation": "permit, license, authorization", "pos": "noun"},
            {"lemma": "tiltás", "translation": "prohibition, ban, interdiction", "pos": "noun"},
            {"lemma": "kivétel", "translation": "exception, exemption", "pos": "noun"},
            {"lemma": "méltányosság", "translation": "equity, fairness, leniency, clemency", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-28-03-voc.json", voc_03)

    voc_04 = {
        "id": "vocab.b1.28.04",
        "lesson": "b1-28-04",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "szerződés", "translation": "contract, formal legal agreement", "pos": "noun"},
            {"lemma": "megállapodás", "translation": "accord, pact, mutual settlement", "pos": "noun"},
            {"lemma": "kötelezettségvállalás", "translation": "commitment, undertaking of liability", "pos": "noun"},
            {"lemma": "garancia", "translation": "warranty, guarantee, assurance", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-28-04-voc.json", voc_04)

    voc_05 = {
        "id": "vocab.b1.28.05",
        "lesson": "b1-28-05",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "igazságosság", "translation": "justice, righteousness, impartiality", "pos": "noun"},
            {"lemma": "jogorvoslat", "translation": "legal remedy, right of appeal, redress", "pos": "noun"},
            {"lemma": "vita", "translation": "dispute, controversy, litigation", "pos": "noun"},
            {"lemma": "megegyezés", "translation": "agreement, consensus, conciliation", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-28-05-voc.json", voc_05)

    # -------------------------------------------------------------------------
    # 2. Grammar Files (2 per regular lesson = 10 files)
    # -------------------------------------------------------------------------
    gr_01_a = {
        "id": "grammar.b1.28.01.impersonal-necessity-rules",
        "title": "Impersonal Prescriptions: kötelező, tilos, szabályos, szabad",
        "sections": [
            {
                "type": "text",
                "title": "Impersonal Predicates in Rule Discourse",
                "content": "In regulatory contexts, Hungarian relies on impersonal predicates + infinitive: *tilos belépni* ('entry prohibited'), *kötelező viselni* ('mandatory to wear'), *szabad használni* ('permitted to use'), *nem szabályos eljárni* ('improper to proceed')."
            },
            {
                "type": "examples",
                "title": "Impersonal rule examples",
                "items": [
                    {
                        "spanish": "Az épület területén szigorúan tilos a dohányzás.",
                        "english": "Smoking is strictly prohibited on the premises of the building."
                    },
                    {
                        "spanish": "A munkavédelmi előírások betartása minden dolgozó számára kötelező.",
                        "english": "Observance of occupational safety regulations is mandatory for all workers."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-28-01-a-gr.json", gr_01_a)

    gr_01_b = {
        "id": "grammar.b1.28.01.rule-adherence-verbs",
        "title": "Verbal Valencies of Compliance: betart, eleget tesz, áthág",
        "sections": [
            {
                "type": "text",
                "title": "Governing Rules and Directives",
                "content": "*Betartja a szabályokat* (observes rules - accusative), *eleget tesz az előírásnak* (satisfies requirements - dative *-nak/-nek*), *megszegi/áthágja a törvényt* (breaks/transgresses the law - accusative)."
            },
            {
                "type": "examples",
                "title": "Compliance in practice",
                "items": [
                    {
                        "spanish": "A vállalat maradéktalanul eleget tett a hatósági előírásoknak.",
                        "english": "The company fully satisfied all official statutory requirements."
                    },
                    {
                        "spanish": "Aki szándékosan megszegi a házirendet, az bírságra számíthat.",
                        "english": "Whoever intentionally violates house rules can expect a fine."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-28-01-b-gr.json", gr_01_b)

    gr_02_a = {
        "id": "grammar.b1.28.02.verbal-participle-ando-endo",
        "title": "Future/Obligation Participles: -andó / -endő",
        "sections": [
            {
                "type": "text",
                "title": "Adjectival Participles of Necessity (-andó/-endő)",
                "content": "The suffix *-andó/-endő* attaches to verb stems to form adjectives expressing that an action must or should be performed: *a megoldandó feladat* ('the task to be solved'), *a betartandó szabály* ('the rule to be observed'), *a fizetendő összeg* ('the amount payable')."
            },
            {
                "type": "examples",
                "title": "Obligation participles in context",
                "items": [
                    {
                        "spanish": "A szerződésben világosan rögzítették a követendő eljárást.",
                        "english": "In the contract, they clearly recorded the procedure to be followed."
                    },
                    {
                        "spanish": "A határidőre elvégzendő munka komoly odafigyelést igényel.",
                        "english": "The work to be performed by the deadline requires serious attention."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-28-02-a-gr.json", gr_02_a)

    gr_02_b = {
        "id": "grammar.b1.28.02.taking-responsibility",
        "title": "Accountability and Duty: felelősséget vállal, számon kér",
        "sections": [
            {
                "type": "text",
                "title": "Formulas of Responsibility",
                "content": "*Felelősséget vállal vmiért* ('takes responsibility for sth' - causal-final *-ért*), *felelős vmiért* ('responsible for sth'), *számon kéri a hibákat* ('holds sb accountable for errors')."
            },
            {
                "type": "examples",
                "title": "Accountability examples",
                "items": [
                    {
                        "spanish": "A vezető teljes felelősséget vállalt a projekt sikeréért.",
                        "english": "The leader took full responsibility for the success of the project."
                    },
                    {
                        "spanish": "A vezetőség szigorúan számon kéri az előírások pontos betartását.",
                        "english": "Management strictly holds staff accountable for the exact adherence to directives."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-28-02-b-gr.json", gr_02_b)

    gr_03_a = {
        "id": "grammar.b1.28.03.permissive-exceptions",
        "title": "Exceptions and Discretion: kivételt tesz, méltányosságból",
        "sections": [
            {
                "type": "text",
                "title": "Phrasing Exemptions and Equity",
                "content": "*Kivételt tesz vkivel/vmiben* ('makes an exception with sb/in sth'), *méltányossági alapon engedélyez* ('grants on grounds of equity/fairness'), *kivételes esetben* ('in exceptional cases')."
            },
            {
                "type": "examples",
                "title": "Exceptions in practice",
                "items": [
                    {
                        "spanish": "A dékán méltányosságból engedélyezte a vizsga halasztását a beteg hallgatónak.",
                        "english": "The dean granted the postponement of the exam on grounds of equity to the ill student."
                    },
                    {
                        "spanish": "A törvény előtt mindenkire ugyanazok a szabályok vonatkoznak, nincs kivétel.",
                        "english": "Before the law the same rules apply to everyone; there is no exception."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-28-03-a-gr.json", gr_03_a)

    gr_03_b = {
        "id": "grammar.b1.28.03.modal-auxiliaries-muszaj-kell",
        "title": "Nuances of Necessity: kell, muszáj, kénytelen",
        "sections": [
            {
                "type": "text",
                "title": "Modal Shades of Compulsion",
                "content": "*Kell* (objective or general necessity), *muszáj* (urgent, inescapable physical or practical pressure), *kénytelen* (reluctantly forced by external circumstances: *kénytelen volt elismerni*)."
            },
            {
                "type": "examples",
                "title": "Modal contrasts",
                "items": [
                    {
                        "spanish": "A bizonyítékok láttán a vádlott kénytelen volt beismerni a tévedését.",
                        "english": "In view of the evidence, the accused was forced to admit his mistake."
                    },
                    {
                        "spanish": "Ha el akarjuk kerülni a bírságot, most muszáj azonnal cselekednünk.",
                        "english": "If we want to avoid the fine, we simply must act immediately right now."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-28-03-b-gr.json", gr_03_b)

    gr_04_a = {
        "id": "grammar.b1.28.04.contractual-clauses",
        "title": "Contractual Commitments: kötelezettséget vállal, garanciát nyújt",
        "sections": [
            {
                "type": "text",
                "title": "Formal Contractual Grammar",
                "content": "*Kötelezettséget vállal arra, hogy...* ('undertakes the obligation that...'), *garanciát vállal/nyújt vmire* ('provides a guarantee for sth'), *szerződést köt vkivel* ('enters into a contract with sb')."
            },
            {
                "type": "examples",
                "title": "Contractual examples",
                "items": [
                    {
                        "spanish": "A bérlő kötelezettséget vállal arra, hogy a lakást rendeltetésszerűen használja.",
                        "english": "The tenant undertakes the obligation to use the apartment in accordance with its intended purpose."
                    },
                    {
                        "spanish": "A gyártó három év teljes körű garanciát nyújt a berendezésre.",
                        "english": "The manufacturer provides a full three-year guarantee on the equipment."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-28-04-a-gr.json", gr_04_a)

    gr_04_b = {
        "id": "grammar.b1.28.04.conditional-in-agreements",
        "title": "Formal Conditions: amennyiben, feltéve, hogy...",
        "sections": [
            {
                "type": "text",
                "title": "Higher-Register Conditionals",
                "content": "Formal, legal agreements replace casual *ha* with elevated conditional conjunctions: *amennyiben* ('in the event that / in so far as'), *feltéve, hogy...* ('provided that...'), *abban az esetben, ha...* ('in the case that...')."
            },
            {
                "type": "examples",
                "title": "Formal conditional examples",
                "items": [
                    {
                        "spanish": "Amennyiben bármelyik fél megszegi a megállapodást, kártérítést köteles fizetni.",
                        "english": "In the event that either party breaches the agreement, they are obliged to pay damages."
                    },
                    {
                        "spanish": "A szerződés érvényes, feltéve, hogy mindkét fél aláírásával hitelesíti.",
                        "english": "The contract is valid, provided that both parties authenticate it with their signatures."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-28-04-b-gr.json", gr_04_b)

    gr_05_a = {
        "id": "grammar.b1.28.05.seeking-justice-and-redress",
        "title": "Legal Redress and Dispute Resolution: jogorvoslat, fellebbez",
        "sections": [
            {
                "type": "text",
                "title": "Remedies Against Unfair Decisions",
                "content": "*Jogorvoslattal él* ('exercises right of legal redress/appeal' - instrumental *-val/-vel*), *fellebbez a döntés ellen* ('appeals against the decision'), *igazságot követel* ('demands justice')."
            },
            {
                "type": "examples",
                "title": "Legal appeal examples",
                "items": [
                    {
                        "spanish": "Az elutasító határozat kézhezvétele után a polgár jogorvoslattal élt.",
                        "english": "After receiving the rejection decision, the citizen exercised his right to legal redress."
                    },
                    {
                        "spanish": "A felek peren kívüli megegyezésre törekedtek a hosszú pereskedés helyett.",
                        "english": "The parties strove for an out-of-court settlement instead of prolonged litigation."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-28-05-a-gr.json", gr_05_a)

    gr_05_b = {
        "id": "grammar.b1.28.05.adversative-and-compromise",
        "title": "Adversative Contrast in Legal Disputes: ezzel szemben, holott",
        "sections": [
            {
                "type": "text",
                "title": "Contrasting Legal Arguments",
                "content": "*Ezzel szemben* ('in contrast to this / on the contrary'), *ugyanakkor* ('at the same time'), *holott* ('whereas / although in reality')."
            },
            {
                "type": "examples",
                "title": "Argumentative contrasts",
                "items": [
                    {
                        "spanish": "A felperes kártérítést követelt, ezzel szemben az alperes bizonyította ártatlanságát.",
                        "english": "The plaintiff demanded damages; in contrast, the defendant proved his innocence."
                    },
                    {
                        "spanish": "A vitát végül kölcsönös megegyezéssel és kézfogással zárták le.",
                        "english": "The dispute was finally concluded with a mutual agreement and a handshake."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-28-05-b-gr.json", gr_05_b)

    # -------------------------------------------------------------------------
    # 3. Exercises Files (6 files = 48 exercises total)
    # -------------------------------------------------------------------------
    ex_01 = {
        "lesson": "b1-28-01",
        "exercises": [
            {
                "id": "b1-28-01.ex01",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent az 'előírás' szó?",
                "options": [
                    "Hivatalos kötelező utasítást vagy szabályt, amit mindenkinek követnie kell.",
                    "Egy régi regény bevezető fejezetét.",
                    "A ceruza hegyezését az írás megkezdése előtt."
                ],
                "correct": 0
            },
            {
                "id": "b1-28-01.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A laboratórium területén szigorúan til_____ védőszemüveg nélkül tartózkodni. (forbidden - os)",
                "answer": "os"
            },
            {
                "id": "b1-28-01.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "biztonsági", "előírások", "pontos", "betartása", "életet", "menthet."],
                "solution": ["A", "biztonsági", "előírások", "pontos", "betartása", "életet", "menthet."]
            },
            {
                "id": "b1-28-01.ex04",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik mondatban találunk helyes vonzatot az 'eleget tesz' kifejezéssel?",
                "options": [
                    "A vállalat maradéktalanul eleget tett a hatósági előírásoknak.",
                    "A vállalat eleget tett a szabályzatot.",
                    "A vállalat eleget tett a törvénnyel."
                ],
                "correct": 0
            },
            {
                "id": "b1-28-01.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A szabályzat szándékos meg_____szegése fegyelmi eljárást von maga után. (prefix - meg)",
                "answer": "meg"
            },
            {
                "id": "b1-28-01.ex06",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent az 'áthágja a szabályt' kifejezés?",
                "options": [
                    "Megszegi, figyelmen kívül hagyja vagy megsérti az érvényes előírást.",
                    "Lépcsőn megy fel az emeletre.",
                    "Átlép egy pocsolyán az utcán."
                ],
                "correct": 0
            },
            {
                "id": "b1-28-01.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A könyvtár olvasótermében kötelező csendben marad_____. (to remain - ni)",
                "answer": "ni"
            },
            {
                "id": "b1-28-01.ex08",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "szabályzat", "minden", "munkavállalóra", "egyformán", "érvényes."],
                "solution": ["A", "szabályzat", "minden", "munkavállalóra", "egyformán", "érvényes."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-28-01-ex.json", ex_01)

    ex_02 = {
        "lesson": "b1-28-02",
        "exercises": [
            {
                "id": "b1-28-02.ex01",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mi az alapvető összefüggés a jogok és a kötelességek között egy demokráciában?",
                "options": [
                    "A jogok és kötelességek elválaszthatatlanok: a szabadságjogok gyakorlása felelősséggel jár.",
                    "A polgároknak csak jogaik vannak, kötelességeik nincsenek.",
                    "Csak a rendőrségnek vannak kötelességei."
                ],
                "correct": 0
            },
            {
                "id": "b1-28-02.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A megbeszélésen kijelölték a határidőre elvégz_____ feladatokat. (to be performed - endő)",
                "answer": "endő"
            },
            {
                "id": "b1-28-02.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "vezető", "teljes", "felelősséget", "vállalt", "a", "döntésért."],
                "solution": ["A", "vezető", "teljes", "felelősséget", "vállalt", "a", "döntésért."]
            },
            {
                "id": "b1-28-02.ex04",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik kifejezés fejezi ki helyesen a beálló melléknévi igenév (-andó/-endő) használatát?",
                "options": [
                    "A betartandó törvények mindenkit köteleznek.",
                    "A betartott törvények tegnap este készültek.",
                    "A betartó törvények sétálnak a téren."
                ],
                "correct": 0
            },
            {
                "id": "b1-28-02.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A polgároknak nemcsak jogaik, hanem állampolgári kötelessége_____ is vannak. (plural possessive - ik)",
                "answer": "ik"
            },
            {
                "id": "b1-28-02.ex06",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent a 'számonkérés' a munkahelyen?",
                "options": [
                    "Annak ellenőrzését és felülvizsgálatát, hogy valaki pontosan teljesítette-e a rábízott feladatokat.",
                    "A telefonkönyvben való lapozgatást.",
                    "A matekfeladat összeadását."
                ],
                "correct": 0
            },
            {
                "id": "b1-28-02.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Mindenki felelős a saját tettei_____. (for them - ért)",
                "answer": "ért"
            },
            {
                "id": "b1-28-02.ex08",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "jogok", "gyakorlása", "együtt", "jár", "a", "társadalmi", "felelősséggel."],
                "solution": ["A", "jogok", "gyakorlása", "együtt", "jár", "a", "társadalmi", "felelősséggel."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-28-02-ex.json", ex_02)

    ex_03 = {
        "lesson": "b1-28-03",
        "exercises": [
            {
                "id": "b1-28-03.ex01",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent a 'méltányosság' a hatósági döntéshozatalban?",
                "options": [
                    "A szabályok emberies, könyörületes és rugalmas alkalmazását rendkívüli helyzetekben.",
                    "A legsúlyosabb büntetés automatikus kiszabását.",
                    "A törvénykönyv elégetését."
                ],
                "correct": 0
            },
            {
                "id": "b1-28-03.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A bizonyítékok alapján a bíróság kénytelen vol_____ felmenteni a vádlottat. (was - t)",
                "answer": "t"
            },
            {
                "id": "b1-28-03.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "hivatal", "méltányosságból", "meghosszabbította", "a", "kérelmező", "határidejét."],
                "solution": ["A", "hivatal", "méltányosságból", "meghosszabbította", "a", "kérelmező", "határidejét."]
            },
            {
                "id": "b1-28-03.ex04",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Miben különbözik a 'muszáj' a szokásos 'kell' segédigétől?",
                "options": [
                    "A 'muszáj' sokkal sürgetőbb, elkerülhetetlen kényszert fejez ki.",
                    "A 'muszáj' csak múlt időben létezik.",
                    "A 'muszáj' tilalmat jelent."
                ],
                "correct": 0
            },
            {
                "id": "b1-28-03.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "Az építkezés megkezdéséhez hivatalos engedély_____ van szükség. (allative - re)",
                "answer": "re"
            },
            {
                "id": "b1-28-03.ex06",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent a 'kivételt tesz' kifejezés?",
                "options": [
                    "Egyedi esetben eltekint az általános szabály szigorú alkalmazásától.",
                    "Kiveszi a pénzt a zsebéből.",
                    "Kiteszi a virágot az erkélyre."
                ],
                "correct": 0
            },
            {
                "id": "b1-28-03.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Sajnos nem tehetek kivétel_____ ebben a kényes kérdésben. (accusative - t)",
                "answer": "t"
            },
            {
                "id": "b1-28-03.ex08",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "méltányos", "elbírálás", "figyelembe", "veszi", "az", "egyéni", "körülményeket."],
                "solution": ["A", "méltányos", "elbírálás", "figyelembe", "veszi", "az", "egyéni", "körülményeket."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-28-03-ex.json", ex_03)

    ex_04 = {
        "lesson": "b1-28-04",
        "exercises": [
            {
                "id": "b1-28-04.ex01",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mi a 'szerződés' jogi lényege?",
                "options": [
                    "Két vagy több fél jogilag kötelező erejű, kölcsönös megállapodása jogokról és kötelezettségekről.",
                    "Egy baráti beszélgetés a kávézóban kötelezettség nélkül.",
                    "Egy reklámfüzet a postaládában."
                ],
                "correct": 0
            },
            {
                "id": "b1-28-04.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Amennyiben a bérlő késik a fizetéssel, kamatot kötele_____ fizetni. (obliged - s)",
                "answer": "s"
            },
            {
                "id": "b1-28-04.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "cég", "három", "év", "teljes", "körű", "garanciát", "vállal", "a", "termékre."],
                "solution": ["A", "cég", "három", "év", "teljes", "körű", "garanciát", "vállal", "a", "termékre."]
            },
            {
                "id": "b1-28-04.ex04",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik kötőszó használatos formális, jogi feltételes mondatokban a köznapi 'ha' helyett?",
                "options": [
                    "Amennyiben / feltéve, hogy...",
                    "Mert / mivelhogy...",
                    "Hacsak nem / bár..."
                ],
                "correct": 0
            },
            {
                "id": "b1-28-04.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A szerződő felek írásbeli megállapodás_____ rögzítették a feltételeket. (inessive - ban)",
                "answer": "ban"
            },
            {
                "id": "b1-28-04.ex06",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent a 'kötelezettségvállalás' fogalma?",
                "options": [
                    "Hivatalos és kötelező ígéretet egy feladat elvégzésére vagy fizetés teljesítésére.",
                    "A vállfára akasztott kabát felvételét.",
                    "A munkahelyről való korai távozást."
                ],
                "correct": 0
            },
            {
                "id": "b1-28-04.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A vállalkozó kötelezettséget vállalt ar_____, hogy időben befejezi az építkezést. (sublative - ra)",
                "answer": "ra"
            },
            {
                "id": "b1-28-04.ex08",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "szerződés", "mindkét", "felet", "kölcsönösen", "köti", "az", "aláírás", "után."],
                "solution": ["A", "szerződés", "mindkét", "felet", "kölcsönösen", "köti", "az", "aláírás", "után."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-28-04-ex.json", ex_04)

    ex_05 = {
        "lesson": "b1-28-05",
        "exercises": [
            {
                "id": "b1-28-05.ex01",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent a 'jogorvoslat' fogalma a magyar közigazgatásban?",
                "options": [
                    "A polgár törvényes lehetőségét arra, hogy panasszal vagy fellebbezéssel éljen egy jogsértő határozat ellen.",
                    "Az orvos által felírt recept beváltását a patikában.",
                    "A tornatermi gyógytornát."
                ],
                "correct": 0
            },
            {
                "id": "b1-28-05.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Az elutasító döntés kézhezvétele után az ügyfél jogorvoslattal él_____. (exercised - t)",
                "answer": "t"
            },
            {
                "id": "b1-28-05.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "bíróság", "pártatlan", "és", "igazságos", "ítéletet", "hozott."],
                "solution": ["A", "bíróság", "pártatlan", "és", "igazságos", "ítéletet", "hozott."]
            },
            {
                "id": "b1-28-05.ex04",
                "type": "multiple-choice",
                "category": "literature",
                "question": "Mi vezette Wibra Györgyöt Glogovára Mikszáth 'Szent Péter esernyője' című regényében?",
                "options": [
                    "A gazdag nagybácsi elveszett örökségét és a pénzt rejtő legendás esernyőt kereste.",
                    "Házat akart vásárolni a hegyekben.",
                    "Meg akarta látogatni a besztercei püspököt."
                ],
                "correct": 0
            },
            {
                "id": "b1-28-05.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A felek peren kívüli megegyezés_____ jutottak. (allative - re)",
                "answer": "re"
            },
            {
                "id": "b1-28-05.ex06",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Mit ismert fel végül Wibra György, amikor megismerte a tisztaszívű Veronkát?",
                "options": [
                    "Hogy a szerelem, az emberség és a boldogság sokkal értékesebb minden kapzsi örökséghajszolásnál.",
                    "Hogy jobb lett volna katonának állni.",
                    "Hogy az esernyő fabatkát sem ér."
                ],
                "correct": 0
            },
            {
                "id": "b1-28-05.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A felperes igazságot követel_____, ezzel szemben az alperes bizonyította ártatlanságát. (demanded - t)",
                "answer": "t"
            },
            {
                "id": "b1-28-05.ex08",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "hosszadalmas", "vita", "végén", "békés", "megegyezés", "született."],
                "solution": ["A", "hosszadalmas", "vita", "végén", "békés", "megegyezés", "született."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-28-05-ex.json", ex_05)

    ex_consolidation = {
        "lesson": "b1-28-consolidation",
        "exercises": [
            {
                "id": "b1-28-consolidation.ex01",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik mondatban látunk helyes beálló melléknévi igenevet?",
                "options": [
                    "A szerződésben rögzítették a követendő eljárási szabályokat.",
                    "A szerződésben rögzítették a követett eljárási szabályokat holnapra.",
                    "A szerződésben rögzítették a követő embereket."
                ],
                "correct": 0
            },
            {
                "id": "b1-28-consolidation.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Amennyiben bármelyik fél megszegi a megállapodást, kártérítést kötele_____ fizetni. (obliged - s)",
                "answer": "s"
            },
            {
                "id": "b1-28-consolidation.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "törvények", "előtt", "minden", "ember", "egyenlő", "jogokkal", "rendelkezik."],
                "solution": ["A", "törvények", "előtt", "minden", "ember", "egyenlő", "jogokkal", "rendelkezik."]
            },
            {
                "id": "b1-28-consolidation.ex04",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Hogyan oldódik fel a jogi és anyagi érdekek konfliktusa Mikszáth 'Szent Péter esernyője' című művében?",
                "options": [
                    "A kapzsi vagyonszerzés helyét a tiszta szerelem, a méltányosság és az emberi tisztesség veszi át.",
                    "Minden vagyont felgyújtanak a haragos rokonok.",
                    "A bíróság börtönbe zárja Glogova összes lakóját."
                ],
                "correct": 0
            },
            {
                "id": "b1-28-consolidation.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A hatóság méltányosságból engedélyezte a kérelmező kérés_____. (its request - ét)",
                "answer": "ét"
            },
            {
                "id": "b1-28-consolidation.ex06",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "szerződéses", "garanciák", "védik", "a", "fogyasztók", "jogait."],
                "solution": ["A", "szerződéses", "garanciák", "védik", "a", "fogyasztók", "jogait."]
            },
            {
                "id": "b1-28-consolidation.ex07",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A jogorvoslat alapvető alkotmányos jog minden polgár számá_____. (for him/her - ra)",
                "answer": "ra"
            },
            {
                "id": "b1-28-consolidation.ex08",
                "type": "multiple-choice",
                "category": "literature",
                "question": "Milyen csodatevő tárgy köré épül a felvidéki Glogova falu meggazdagodásának mesés története?",
                "options": [
                    "Egy ócska, vörös színű esernyő köré, amit a legenda szerint maga Szent Péter borított a kis árvára.",
                    "Egy aranyból készült csodálatos korona köré.",
                    "Egy varázserejű kard köré."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-28-consolidation-ex.json", ex_consolidation)

    # -------------------------------------------------------------------------
    # 4. Classic Story Adaptation for Consolidation: Szent Péter esernyője
    # -------------------------------------------------------------------------
    story_classic = {
        "id": "story.b1.28.classic",
        "title": "Szent Péter esernyője",
        "level": "B1",
        "order": 28,
        "type": "classics",
        "estimatedMinutes": 8,
        "summary": "An adaptation of Kálmán Mikszáth's warm, ironical, and delightful masterpiece 'Szent Péter esernyője' (St. Peter's Umbrella). In the impoverished Upper Hungarian hamlet of Glogova, a ragged red umbrella mysteriously left over an orphan baby girl during a rainstorm is heralded by superstitious peasants as a miracle from Saint Peter. Years later, brilliant young lawyer György Wibra searches the region for the umbrella, believing his eccentric late father hid a fortune in negotiable bonds in its hollow handle. But upon discovering Veronka, Wibra realizes that love and integrity far eclipse lost bank notes.",
        "characters": [
            "Bélyi János, a glogovai szegény pap",
            "Veronka, a pap kishúga",
            "Wibra György, fiatal besztercei ügyvéd",
            "Sztolarik közjegyző úr"
        ],
        "location": "Glogova és Besztercebánya vidéke",
        "author": "Mikszáth Kálmán",
        "work": "Szent Péter esernyője (1895)",
        "paragraphs": [
            {
                "type": "narration",
                "text": "A zord felvidéki hegyek között fekvő Glogova a világ legszegényebb faluja volt. Amikor a fiatal, jóságos Bélyi János pap megérkezett a romos parókiára, édesanyja halála után odaállítottak hozzá egy kétéves kislányt: a húgát, Veronkát. A pap kétségbeesetten imádkozott a templomban, miközben odakint eleredt a záporeső."
            },
            {
                "type": "narration",
                "text": "Mire visszatért, csodát látott: a kosárban fekvő kislány fölé valaki egy kopott, piros esernyőt feszített ki, hogy ne ázzon meg. Egy öreg falusi asszony látni vélte, amint egy ősz szakállú, glóriás öregember lépkedett el az udvarról: 'Maga Szent Péter volt az, aki leszállt az égből a kis árvához!'"
            },
            {
                "type": "dialogue",
                "speaker": "Glogovai hívő paraszt",
                "text": "Szent Péter megáldotta Glogovát! Ez az esernyő szent ereklye! Aki alá áll a templomban, meggyógyul, s boldog házasság vár rá!"
            },
            {
                "type": "narration",
                "text": "A hír futótűzként terjedt. Zarándokok ezrei sereglettek Glogovára, a falu felvirágzott, új templom és gazdag gazdaság épült. Eközben Besztercén egy fiatal és tehetséges ügyvéd, Wibra György nyomozni kezdett különc nagybátyja, Gregorics Pál mesés vagyona után. Rájött a titokra: a milliókat érő utalványt a nagybácsi a piros esernyő üreges fa fogantyújába rejtette el!"
            },
            {
                "type": "dialogue",
                "speaker": "Wibra György ügyvéd",
                "text": "Meg kell találnom azt az esernyőt! Az a vagyon jog szerint engem illet, a kapzsi rokonok elől rejtette el az apám! Nem nyugszom, amíg a kezembe nem veszem a nyelet!"
            },
            {
                "type": "narration",
                "text": "György elutazott Glogovára. Ám amikor megérkezett a virágzó parókiára, és meglátta a felserdült, angyali tisztaságú és kedves Veronkát, a szíve hirtelen megdobbant. A pap húga nemcsak szép volt, de tiszta lelkű, őszinte és hűséges teremtés."
            },
            {
                "type": "narration",
                "text": "Amikor végül kiderült, hogy az esernyő régi fa nyele régen elégett, és az elveszett bankutalványok mind hamuvá váltak, György nem érzett haragot vagy kétségbeesést. Ránézett Veronkára, s arcán megjelent a megkönnyebbülés mosolya."
            },
            {
                "type": "dialogue",
                "speaker": "Wibra György",
                "text": "Hadd égjen el az a kincses papír! A legdrágább örökséget már megtaláltam itt Glogován: Veronkát és az igaz szerelmet, ami ezer bankjegynél is többet ér!"
            }
        ]
    }
    write_json("content/hu/stories/classics/b1/b1-28-mikszath.json", story_classic)

    # -------------------------------------------------------------------------
    # 5. Lesson Files (01 to 05 + consolidation)
    # -------------------------------------------------------------------------
    lesson_titles = {
        "01": ("Szabályzatok és az előírások betartása", "Regulations & Adherence to Directives"),
        "02": ("Jogok, kötelességek és felelősségvállalás", "Rights, Duties & Accountability"),
        "03": ("Engedélyek, tiltások és a méltányosság", "Permits, Prohibitions & Equity"),
        "04": ("Szerződések, garanciák és megállapodások", "Contracts, Warranties & Formal Agreements"),
        "05": ("Igazságosság, jogorvoslat és megegyezés", "Justice, Legal Redress & Dispute Settlement")
    }

    grammar_refs = {
        "01": ["grammar/b1/b1-28-01-a-gr.json", "grammar/b1/b1-28-01-b-gr.json"],
        "02": ["grammar/b1/b1-28-02-a-gr.json", "grammar/b1/b1-28-02-b-gr.json"],
        "03": ["grammar/b1/b1-28-03-a-gr.json", "grammar/b1/b1-28-03-b-gr.json"],
        "04": ["grammar/b1/b1-28-04-a-gr.json", "grammar/b1/b1-28-04-b-gr.json"],
        "05": ["grammar/b1/b1-28-05-a-gr.json", "grammar/b1/b1-28-05-b-gr.json"]
    }

    for i in range(1, 6):
        padded = f"0{i}"
        hu_t, en_t = lesson_titles[padded]
        lesson_data = {
            "id": f"lesson.b1.28-{padded}",
            "unit": 28,
            "title": f"{hu_t} ({en_t})",
            "level": "B1",
            "grammar": "Prescriptive Modality, Future Participles & Juridical Syntax in Hungarian",
            "sections": [
                {
                    "type": "goal",
                    "title": "Lesson Goals",
                    "items": [
                        f"I can understand and discuss {en_t} in Hungarian.",
                        "I can use impersonal rules, future obligation participles (-andó/-endő), and formal conditional clauses.",
                        "I can express legal rights, duties, contracts, and dispute resolution in professional and civic registers.",
                        "I can appreciate classic Hungarian literature addressing law, greed, and moral integrity."
                    ]
                },
                {"type": "recycle", "count": 3},
                {"type": "vocabulary", "ref": f"vocabulary/b1/b1-28-{padded}-voc.json"},
                {"type": "grammar", "ref": grammar_refs[padded][0]},
                {"type": "grammar", "ref": grammar_refs[padded][1]},
                {
                    "type": "exercise-group",
                    "title": "Practice",
                    "ref": f"exercises/b1/b1-28-{padded}-ex.json",
                    "exerciseRefs": [f"b1-28-{padded}.ex0{k}" for k in range(1, 9)]
                }
            ]
        }
        write_json(f"content/hu/lessons/b1/b1-28-{padded}.json", lesson_data)

    consolidation_data = {
        "id": "lesson.b1.28-consolidation",
        "unit": 28,
        "title": "Unit 28 Consolidation",
        "level": "B1",
        "grammar": "Consolidation of Legal & Regulatory Registers, Equity & Mikszáth's St. Peter's Umbrella",
        "sections": [
            {
                "type": "story",
                "title": "Szent Péter esernyője (Mikszáth Kálmán)",
                "ref": "stories/classics/b1/b1-28-mikszath.json"
            },
            {
                "type": "exercise-group",
                "title": "Consolidation Practice",
                "ref": "exercises/b1/b1-28-consolidation-ex.json",
                "exerciseRefs": [f"b1-28-consolidation.ex0{k}" for k in range(1, 9)]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-28-consolidation.json", consolidation_data)
    print("Successfully built Hungarian B1 Core Unit 28 (b1-28)!")

if __name__ == "__main__":
    build_unit_28_core()
