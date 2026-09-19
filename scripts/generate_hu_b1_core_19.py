#!/usr/bin/env python3
"""Generate Hungarian B1 Core Unit 19: Money & the Economy (b1-19)."""

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

def build_unit_19_core():
    # -------------------------------------------------------------------------
    # 1. Vocabulary Files (4 words each = 20 words total)
    # -------------------------------------------------------------------------
    voc_01 = {
        "id": "vocab.b1.19.01",
        "lesson": "b1-19-01",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "költségvetés", "translation": "budget", "pos": "noun"},
            {"lemma": "kiadás", "translation": "expenditure, expense", "pos": "noun"},
            {"lemma": "bevétel", "translation": "revenue, income", "pos": "noun"},
            {"lemma": "megtakarítás", "translation": "savings", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-19-01-voc.json", voc_01)

    voc_02 = {
        "id": "vocab.b1.19.02",
        "lesson": "b1-19-02",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "bankszámla", "translation": "bank account", "pos": "noun"},
            {"lemma": "utalás", "translation": "wire transfer, bank transfer", "pos": "noun"},
            {"lemma": "hitel", "translation": "credit, bank loan", "pos": "noun"},
            {"lemma": "kamatláb", "translation": "interest rate", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-19-02-voc.json", voc_02)

    voc_03 = {
        "id": "vocab.b1.19.03",
        "lesson": "b1-19-03",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "infláció", "translation": "inflation", "pos": "noun"},
            {"lemma": "áremelkedés", "translation": "price increase, price rise", "pos": "noun"},
            {"lemma": "valuta", "translation": "foreign currency (physical cash)", "pos": "noun"},
            {"lemma": "árfolyam", "translation": "exchange rate", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-19-03-voc.json", voc_03)

    voc_04 = {
        "id": "vocab.b1.19.04",
        "lesson": "b1-19-04",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "vállalkozás", "translation": "business, enterprise", "pos": "noun"},
            {"lemma": "befektetés", "translation": "investment", "pos": "noun"},
            {"lemma": "nyereség", "translation": "profit, gain", "pos": "noun"},
            {"lemma": "adóbevallás", "translation": "tax return, tax declaration", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-19-04-voc.json", voc_04)

    voc_05 = {
        "id": "vocab.b1.19.05",
        "lesson": "b1-19-05",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "gazdasági növekedés", "translation": "economic growth", "pos": "noun"},
            {"lemma": "munkanélküliség", "translation": "unemployment", "pos": "noun"},
            {"lemma": "versenyképesség", "translation": "competitiveness", "pos": "noun"},
            {"lemma": "vásárlóerő", "translation": "purchasing power", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-19-05-voc.json", voc_05)

    # -------------------------------------------------------------------------
    # 2. Grammar Files
    # -------------------------------------------------------------------------
    gr_01_a = {
        "id": "grammar.b1.19.01.fractions-percentages",
        "title": "Numbers in the Economy: Fractions and Percentages (százalék)",
        "sections": [
            {
                "type": "text",
                "title": "Expressing Percentages in Hungarian",
                "content": "In Hungarian, percentages use the noun *százalék* preceded by a numeral: *öt százalék* (5%), *húsz százalék* (20%). Case suffixes attach directly to *százalék*: *öt százalékkal nőtt* ('increased by 5%'), *három százalékra csökkent* ('decreased to 3%'). Fractions use ordinal stems + *-ad/-ed/-öd*: *egyharmad* (1/3), *kétharmad* (2/3), *háromnegyed* (3/4)."
            },
            {
                "type": "examples",
                "title": "Fractions and percentages in context",
                "items": [
                    {
                        "spanish": "Az infláció ebben az évben négy százalékra csökkent.",
                        "english": "Inflation decreased to four percent this year."
                    },
                    {
                        "spanish": "A havi költségvetés egyharmadát lakbérre költöm.",
                        "english": "I spend one third of the monthly budget on rent."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-19-01-a-gr.json", gr_01_a)

    gr_01_b = {
        "id": "grammar.b1.19.01.financial-verbs",
        "title": "Key Financial Verbs: költ, megtakarít, befektet",
        "sections": [
            {
                "type": "text",
                "title": "Verbal Government with Money",
                "content": "*Költ* (to spend) governs *-ra/-re*: *pénzt költ könyvekre* ('spends money on books'). *Megtakarít* (to save) takes an accusative object: *havi ötvenezer forintot takarít meg*. *Befektet* (to invest) governs *-ba/-be*: *ingatlanba fektet be* ('invests in real estate')."
            },
            {
                "type": "examples",
                "title": "Using spending and saving verbs",
                "items": [
                    {
                        "spanish": "Sokkal kevesebb pénzt költünk felesleges kiadásokra.",
                        "english": "We spend much less money on unnecessary expenses."
                    },
                    {
                        "spanish": "A család minden hónapban igyekszik megtakarítani egy kis összeget.",
                        "english": "The family tries to save a small sum every month."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-19-01-b-gr.json", gr_01_b)

    gr_02_a = {
        "id": "grammar.b1.19.02.correlative-annyi-mint",
        "title": "Proportional Comparisons: annyi... mint ('as much / as many as')",
        "sections": [
            {
                "type": "text",
                "title": "Equal Amounts: annyi ... mint",
                "content": "To compare quantities, use *annyi [főnév], mint...* ('as much/many [noun] as...'): *Idén annyi bevételem volt, mint tavaly.* ('This year I had as much revenue as last year.'). For actions: *annyit költ, mint amennyit keres* ('spends as much as he earns')."
            },
            {
                "type": "examples",
                "title": "Proportional comparisons with annyi",
                "items": [
                    {
                        "spanish": "Nem költök annyi pénzt, mint a barátaim.",
                        "english": "I do not spend as much money as my friends."
                    },
                    {
                        "spanish": "A vállalkozásnak kétszer annyi bevétele lett, mint amennyire számítottak.",
                        "english": "The business had twice as much revenue as they expected."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-19-02-a-gr.json", gr_02_a)

    gr_02_b = {
        "id": "grammar.b1.19.02.banking-collocations",
        "title": "Banking Transactions: számlát nyit, utalást indít, hitelt vesz fel",
        "sections": [
            {
                "type": "text",
                "title": "Banking Collocations",
                "content": "Standard banking expressions: *bankszámlát nyit* ('opens a bank account'), *átutalást indít valakinek* ('initiates a bank transfer to someone'), *hitelt vesz fel* ('takes out a loan'), *kamatot fizet* ('pays interest')."
            },
            {
                "type": "examples",
                "title": "Bank expressions in practice",
                "items": [
                    {
                        "spanish": "Lakáshitelt szeretnék felvenni alacsony kamatláb mellett.",
                        "english": "I would like to take out a housing loan at a low interest rate."
                    },
                    {
                        "spanish": "Online indítottam el az átutalást a bankszámlámról.",
                        "english": "I initiated the bank transfer online from my bank account."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-19-02-b-gr.json", gr_02_b)

    gr_03_a = {
        "id": "grammar.b1.19.03.proportional-minel-annal",
        "title": "Correlative Conditionals: minél... annál... ('the more... the more...')",
        "sections": [
            {
                "type": "text",
                "title": "The Comparative Correlative in Economics",
                "content": "*Minél [középfok], annál [középfok]* expresses linked progression: *Minél magasabb az infláció, annál gyorsabban csökken a vásárlóerő.* ('The higher the inflation, the faster purchasing power decreases.')."
            },
            {
                "type": "examples",
                "title": "Minél... annál... sentences",
                "items": [
                    {
                        "spanish": "Minél többet takarítunk meg, annál nyugodtabb a jövőnk.",
                        "english": "The more we save, the calmer our future is."
                    },
                    {
                        "spanish": "Minél kedvezőbb az árfolyam, annál érdemesebb valutát váltani.",
                        "english": "The more favorable the exchange rate, the more worthwhile it is to exchange currency."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-19-03-a-gr.json", gr_03_a)

    gr_03_b = {
        "id": "grammar.b1.19.03.price-fluctuations",
        "title": "Verbs of Fluctuation: emelkedik, csökken, ingadozik",
        "sections": [
            {
                "type": "text",
                "title": "Describing Market Trends",
                "content": "Intransitive price changes: *az ár emelkedik* (prices rise), *az árfolyam ingadozik* (the exchange rate fluctuates), *a kamat csökken* (interest drops). Note transitive pairs: *emeli az árat* (raises the price), *csökkenti a kiadást* (reduces expenses)."
            },
            {
                "type": "examples",
                "title": "Trend verbs",
                "items": [
                    {
                        "spanish": "Az elmúlt hetekben a forint árfolyama stabilizálódott az euróval szemben.",
                        "english": "In recent weeks, the forint exchange rate stabilized against the euro."
                    },
                    {
                        "spanish": "A nemzetközi piacon jelentősen csökkent az energia ára.",
                        "english": "Energy prices decreased significantly on the international market."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-19-03-b-gr.json", gr_03_b)

    gr_04_a = {
        "id": "grammar.b1.19.04.business-modal-structures",
        "title": "Business Decisions: érdemes, szükséges, elkerülhetetlen + inf.",
        "sections": [
            {
                "type": "text",
                "title": "Impersonal Predicates in Enterprise Management",
                "content": "Evaluating business choices: *érdemes befektetni* ('it is worthwhile investing'), *szükséges csökkenteni a költségeket* ('it is necessary to reduce costs'), *elkerülhetetlen az adó megfizetése* ('paying tax is unavoidable')."
            },
            {
                "type": "examples",
                "title": "Business decision phrases",
                "items": [
                    {
                        "spanish": "Egy induló vállalkozásba óvatosan érdemes tőkét fektetni.",
                        "english": "In a startup enterprise, it is wise to invest capital cautiously."
                    },
                    {
                        "spanish": "A könyvelő szerint határidőre szükséges leadni az adóbevallást.",
                        "english": "According to the accountant, it is necessary to submit the tax return on deadline."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-19-04-a-gr.json", gr_04_a)

    gr_04_b = {
        "id": "grammar.b1.19.04.compound-economic-nouns",
        "title": "Compound Economic Nouns: jövedelemadó, költségvetési hiány",
        "sections": [
            {
                "type": "text",
                "title": "Building Technical Compounds",
                "content": "Hungarian creates precise economic terminology through compounding: *jövedelem* + *adó* = *jövedelemadó* (income tax); *költségvetés* + *hiány* = *költségvetési hiány* (budget deficit); *üzleti* + *terv* = *üzleti terv* (business plan)."
            },
            {
                "type": "examples",
                "title": "Compound nouns in context",
                "items": [
                    {
                        "spanish": "A személyi jövedelemadó mértéke Magyarországon tizenöt százalék.",
                        "english": "The personal income tax rate in Hungary is fifteen percent."
                    },
                    {
                        "spanish": "A részletes üzleti terv nélkülözhetetlen egy sikeres hiteligényléshez.",
                        "english": "A detailed business plan is indispensable for a successful loan application."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-19-04-b-gr.json", gr_04_b)

    gr_05_a = {
        "id": "grammar.b1.19.05.macro-trends",
        "title": "Reporting Macroeconomic Trends: mutatók, tendenciák és kilátások",
        "sections": [
            {
                "type": "text",
                "title": "Discourse of Economic Analysis",
                "content": "Discussing macro statistics: *a statisztikai adatok szerint* ('according to statistical data'), *a mutatók javulást jeleznek* ('indicators indicate improvement'), *a gazdasági növekedés üteme lassult* ('the rate of economic growth slowed down')."
            },
            {
                "type": "examples",
                "title": "Macro analysis sentences",
                "items": [
                    {
                        "spanish": "A legfrissebb felmérések szerint a munkanélküliség rekordalacsony szintre süllyedt.",
                        "english": "According to the latest surveys, unemployment has sunk to a record low level."
                    },
                    {
                        "spanish": "A hazai vállalatok versenyképessége nagymértékben javult a régióban.",
                        "english": "The competitiveness of domestic companies has improved substantially in the region."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-19-05-a-gr.json", gr_05_a)

    gr_05_b = {
        "id": "grammar.b1.19.05.causal-economic-connectors",
        "title": "Causal Links in Finance: ennek következtében, abból adódóan",
        "sections": [
            {
                "type": "text",
                "title": "Cause and Effect in Economics",
                "content": "Expressing consequence: *ennek következtében* ('as a consequence of this'), *abból adódóan, hogy...* ('arising from the fact that...'): *Csökkentek a kiadások, ennek következtében nőtt a nyereség.* ('Expenditures decreased; as a consequence, profits grew.')."
            },
            {
                "type": "examples",
                "title": "Economic consequence phrases",
                "items": [
                    {
                        "spanish": "Nőtt a vásárlóerő, ennek következtében a belső fogyasztás is megélénkült.",
                        "english": "Purchasing power increased; consequently, domestic consumption also revived."
                    },
                    {
                        "spanish": "A beruházásokból adódóan új munkahelyek százai jöttek létre a térségben.",
                        "english": "Arising from investments, hundreds of new jobs were created in the region."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-19-05-b-gr.json", gr_05_b)

    # -------------------------------------------------------------------------
    # 3. Exercise Files (01 to 05 + consolidation)
    # -------------------------------------------------------------------------
    for i in range(1, 6):
        padded = f"0{i}"
        curr_voc = [voc_01, voc_02, voc_03, voc_04, voc_05][i-1]
        ex_data = {
            "lesson": f"b1-19-{padded}",
            "exercises": [
                {
                    "id": f"b1-19-{padded}.ex01",
                    "type": "matching",
                    "category": "vocabulary",
                    "pairs": [[w["lemma"], w["translation"]] for w in curr_voc["words"]]
                },
                {
                    "id": f"b1-19-{padded}.ex02",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "question": f"Melyik mondat fejezi ki helyesen a pénzügyi vagy mennyiségi viszonyt? (Lesson {i})",
                    "options": [
                        "Minél többet takarítunk meg havonta, annál nagyobb biztonságban vagyunk.",
                        "Minél sok pénzt költeni annál nem marad semmi a számlán.",
                        "Annyi van pénzem mint amennyi költöttem volt tegnap."
                    ],
                    "correct": 0
                },
                {
                    "id": f"b1-19-{padded}.ex03",
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "sentence": "A család gondosan megtervezi az éves családi ____ összegét. (budget -t)",
                    "answer": "költségvetést"
                },
                {
                    "id": f"b1-19-{padded}.ex04",
                    "type": "fill-blank",
                    "category": "grammar",
                    "sentence": "Az infláció ebben az évben három ____ csökkent. (percent -ra/-re)",
                    "answer": "százalékra"
                },
                {
                    "id": f"b1-19-{padded}.ex05",
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "question": "Mit jelent a kamatláb fogalma a banki hiteleknél?",
                    "options": [
                        "A kölcsönvett összeg után fizetendő, százalékban kifejezett díjat.",
                        "A bankfiók nyitvatartási idejének hosszát.",
                        "A bankkártya lejárati évszámát."
                    ],
                    "correct": 0
                },
                {
                    "id": f"b1-19-{padded}.ex06",
                    "type": "fill-blank",
                    "category": "grammar",
                    "sentence": "Minél magasabb a hozam, ____ nagyobb kockázatot kell vállalni. (the [more] - correlative pair of minél)",
                    "answer": "annál"
                },
                {
                    "id": f"b1-19-{padded}.ex07",
                    "type": "sentence-builder",
                    "category": "grammar",
                    "tiles": ["A", "sikeres", "vállalkozás", "kulcsa", "a", "pontos", "üzleti", "terv", "és", "a", "jó", "költségvetés."],
                    "solution": ["A", "sikeres", "vállalkozás", "kulcsa", "a", "pontos", "üzleti", "terv", "és", "a", "jó", "költségvetés."]
                },
                {
                    "id": f"b1-19-{padded}.ex08",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "Miért fontos a megtakarítás a modern gazdaságban?",
                    "options": [
                        "Mert anyagi biztonságot nyújt váratlan kiadások és jövőbeli tervek esetén.",
                        "Mert megakadályozza, hogy valaha bankba menjünk.",
                        "Mert mindenféle adófizetés alól automatikusan mentesít."
                    ],
                    "correct": 0
                }
            ]
        }
        write_json(f"content/hu/exercises/b1/b1-19-{padded}-ex.json", ex_data)

    # Consolidation exercises
    ex_consolidation = {
        "lesson": "b1-19-consolidation",
        "exercises": [
            {
                "id": "b1-19-consolidation.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["költségvetés", "budget"],
                    ["bankszámla", "bank account"],
                    ["infláció", "inflation"],
                    ["versenyképesség", "competitiveness"]
                ]
            },
            {
                "id": "b1-19-consolidation.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik állítás fejezi ki helyesen a pénzügyi tudatosság elvét?",
                "options": [
                    "Minél pontosabban követjük a kiadásokat, annál könnyebb kiegyensúlyozott költségvetést fenntartani.",
                    "Annyi költünk amennyi akartunk mert a pénz mindig terem.",
                    "Hiába nincs bevétel mert a bankhitel ingyenes ajándék."
                ],
                "correct": 0
            },
            {
                "id": "b1-19-consolidation.ex03",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A cég éves nyeresége tíz ____ nőtt a tavalyi évhez képest. (percent -al/-el)",
                "answer": "százalékkal"
            },
            {
                "id": "b1-19-consolidation.ex04",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Az ügyfél lakáshitelt vett ____ az új lakás megvásárlásához. (took out - verbal prefix)",
                "answer": "fel"
            },
            {
                "id": "b1-19-consolidation.ex05",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "növekvő", "vásárlóerő", "és", "az", "alacsony", "munkanélküliség", "erősíti", "az", "ország", "gazdaságát."],
                "solution": ["A", "növekvő", "vásárlóerő", "és", "az", "alacsony", "munkanélküliség", "erősíti", "az", "ország", "gazdaságát."]
            },
            {
                "id": "b1-19-consolidation.ex06",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent az árfolyam a devizapiacon?",
                "options": [
                    "Egyik pénznem átszámítási értékét egy másik pénznemhez viszonyítva.",
                    "A bolti árucikkek súlyát kilogrammban.",
                    "A bank épületének hivatalos címét."
                ],
                "correct": 0
            },
            {
                "id": "b1-19-consolidation.ex07",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "Minden év májusában a munkavállalók elkészítik a személyi adó____. (declaration / return -t)",
                "answer": "bevallást"
            },
            {
                "id": "b1-19-consolidation.ex08",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Milyen tanulságot hordoz Mikszáth klasszikus novellája a pénzről és a birtokról?",
                "options": [
                    "A könnyelmű kölcsönök és a látszat fenntartása helyett a becsületes munka és a józanság a tartós vagyon alapja.",
                    "A gazdagság kizárólag a szerencsejátékokból származik.",
                    "A bankok nélkül az emberiség képtelen lenne bármit megtermelni."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-19-consolidation-ex.json", ex_consolidation)

    # -------------------------------------------------------------------------
    # 4. Classic Story Adaptation for Lesson 5 / Consolidation
    # -------------------------------------------------------------------------
    story_classic = {
        "id": "story.b1.19.classic",
        "title": "A gavallérok és a bankhitel",
        "level": "B1",
        "order": 19,
        "type": "classics",
        "estimatedMinutes": 7,
        "summary": "An adaptation inspired by Kálmán Mikszáth's sharp satirical masterpiece 'A gavallérok' (The Cavaliers). In the 19th-century Hungarian countryside, aristocratic gentlemen who live beyond their means gather at the county fair, attempting to negotiate loans and keep up the appearance of wealth with wit, charm, and empty pockets.",
        "characters": [
            "Garanvölgyi úr",
            "A felvidéki bankár",
            "Pálffy Menyhért gazda"
        ],
        "location": "Vármegyei kaszinó és vásár, Felvidék",
        "author": "Mikszáth Kálmán",
        "work": "A gavallérok",
        "paragraphs": [
            {
                "type": "narration",
                "text": "A vármegyei kaszinó kártyaszobájában sűrű szivarfüst lebegett. A gavallérok finom posztókabátban, aranyóralánccal a mellényükön úgy beszéltek a százezres összegekről, mintha aprópénz volna a zsebükben."
            },
            {
                "type": "dialogue",
                "speaker": "Garanvölgyi úr",
                "text": "Tisztelt bankár úr! A birtokom aranybánya, csupán egy csekély átmeneti hitelre van szükségem a tavaszi vetésig. Százezer forint azonnali utalása megoldaná minden gondomat!"
            },
            {
                "type": "narration",
                "text": "A szemüveges bankár lassan lapozgatta a vastag bőrkötéses könyvelési naplót. Pontosan ismerte a gavallérok furcsa számításait, ahol a bevétel mindig álom volt, a kiadás viszont mindennapos valóság."
            },
            {
                "type": "dialogue",
                "speaker": "A felvidéki bankár",
                "text": "Tekintetes uram, a költségvetés nem tűri a képzeletbeli vagyont. A múlt évi kamatláb után még a törlesztés sem érkezett meg a bankszámlára. Miből fizeti vissza az újabb hitelt?"
            },
            {
                "type": "narration",
                "text": "Garanvölgyi megigazította a nyakkendőjét, és olyan méltósággal mosolygott, mintha ő maga birtokolná a Nemzeti Bankot."
            },
            {
                "type": "dialogue",
                "speaker": "Garanvölgyi úr",
                "text": "Kedves barátom! Hát a jó hírnevem semmit sem ér? Minél kevesebb készpénzem van, annál büszkébb a nevem ebben a megyében! A gavallér nem alkuszik garasokra!"
            },
            {
                "type": "narration",
                "text": "A szomszéd asztalnál ülő Pálffy Menyhért, a józan és takarékos parasztgazda csendesen hallgatta az urakat, miközben a vásárban eladott gabona tiszta nyereségét számolta össze."
            },
            {
                "type": "dialogue",
                "speaker": "Pálffy Menyhért",
                "text": "Látja, tekintetes uram, a föld nem gavallérkodik. Csak annyit ad vissza ősszel, amennyi munkát és magot tavasszal belefektettünk. A megtakarítás és a munka az igazi gazdagság, nem a kölcsönkért aranyak csillogása."
            },
            {
                "type": "narration",
                "text": "A bankár bólintott, Garanvölgyi pedig mélyen a szivarjába szívott. A régi világ gavallérjai még büszkén tartották a fejüket, de a modern gazdaság és a polgári észjárás lassan már más szabályok szerint mérte az értékeket."
            }
        ]
    }
    write_json("content/hu/stories/classics/b1/b1-19-mikszath.json", story_classic)

    # -------------------------------------------------------------------------
    # 5. Lesson Files (01 to 05 + consolidation)
    # -------------------------------------------------------------------------
    for i in range(1, 6):
        padded = f"0{i}"
        titles = {
            "01": ("Budgeting and Expenses", "Költségvetés, kiadások és megtakarítás"),
            "02": ("Banking and Accounts", "Bankszámla, utalás és banki hitelek"),
            "03": ("Inflation and Exchange Rates", "Infláció, árak és devizaárfolyamok"),
            "04": ("Starting a Business", "Vállalkozás, befektetések és adózás"),
            "05": ("The National Economy", "Gazdasági növekedés és a munkaerőpiac")
        }
        en_title, hu_title = titles[padded]
        lesson_data = {
            "id": f"lesson.b1.19-{padded}",
            "unit": 19,
            "title": en_title,
            "level": "B1",
            "grammar": "Numerals, Fractions, Percentages & Correlative Comparisons in Economics",
            "goal": [
                f"I can understand and use vocabulary for {en_title.lower()}.",
                "I can express numbers, percentages and proportional comparisons in Hungarian.",
                "I can discuss money management, banking, investments, and economic news.",
                "I can master four new target vocabulary items in authentic context."
            ],
            "sections": [
                {
                    "type": "goal",
                    "title": "Lesson Goals",
                    "items": [
                        f"I can understand and use vocabulary for {en_title.lower()}.",
                        "I can express numbers, percentages and proportional comparisons in Hungarian.",
                        "I can discuss money management, banking, investments, and economic news.",
                        "I can master four new target vocabulary items in authentic context."
                    ]
                },
                {"type": "recycle", "title": "Quick Review"},
                {"type": "grammar", "ref": f"grammar/b1/b1-19-{padded}-a-gr.json"},
                {"type": "grammar", "ref": f"grammar/b1/b1-19-{padded}-b-gr.json"},
                {"type": "vocabulary", "title": "Lesson Vocabulary", "ref": f"vocabulary/b1/b1-19-{padded}-voc.json"},
                {
                    "type": "exercise-group",
                    "title": "Practice",
                    "ref": f"exercises/b1/b1-19-{padded}-ex.json",
                    "exerciseRefs": [f"b1-19-{padded}.ex0{k}" for k in range(1, 9)]
                }
            ]
        }
        write_json(f"content/hu/lessons/b1/b1-19-{padded}.json", lesson_data)

    consolidation_data = {
        "id": "lesson.b1.19-consolidation",
        "unit": 19,
        "title": "Unit 19 Consolidation",
        "level": "B1",
        "grammar": "Consolidation of Financial Discourse & Comparative Correlatives",
        "sections": [
            {
                "type": "story",
                "title": "A gavallérok és a bankhitel (Mikszáth Kálmán)",
                "ref": "stories/classics/b1/b1-19-mikszath.json"
            },
            {
                "type": "exercise-group",
                "title": "Consolidation Practice",
                "ref": "exercises/b1/b1-19-consolidation-ex.json",
                "exerciseRefs": [f"b1-19-consolidation.ex0{k}" for k in range(1, 9)]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-19-consolidation.json", consolidation_data)
    print("Successfully built Hungarian B1 Core Unit 19 (b1-19)!")

if __name__ == "__main__":
    build_unit_19_core()
