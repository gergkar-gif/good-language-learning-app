#!/usr/bin/env python3
"""Generate Hungarian B1 Core Unit 31: The Future of Society (b1-31)."""

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

def build_unit_31_core():
    # -------------------------------------------------------------------------
    # 1. Vocabulary Files (4 words each = 20 words total)
    # -------------------------------------------------------------------------
    voc_01 = {
        "id": "vocab.b1.31.01",
        "lesson": "b1-31-01",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "jövőkép", "translation": "vision of the future", "pos": "noun"},
            {"lemma": "előrejelzés", "translation": "forecast, projection, prediction", "pos": "noun"},
            {"lemma": "kibontakozás", "translation": "unfolding, emergence, development", "pos": "noun"},
            {"lemma": "lehetőség", "translation": "opportunity, possibility, potential", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-31-01-voc.json", voc_01)

    voc_02 = {
        "id": "vocab.b1.31.02",
        "lesson": "b1-31-02",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "társadalmi tendencia", "translation": "social trend, societal tendency", "pos": "noun"},
            {"lemma": "digitalizáció", "translation": "digitization, digital transformation", "pos": "noun"},
            {"lemma": "automatizáció", "translation": "automation", "pos": "noun"},
            {"lemma": "átalakulás", "translation": "transformation, radical change", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-31-02-voc.json", voc_02)

    voc_03 = {
        "id": "vocab.b1.31.03",
        "lesson": "b1-31-03",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "megoldandó feladat", "translation": "task to be solved, upcoming challenge", "pos": "noun"},
            {"lemma": "innováció", "translation": "innovation, technological novelties", "pos": "noun"},
            {"lemma": "megújulás", "translation": "renewal, rejuvenation", "pos": "noun"},
            {"lemma": "fenntarthatóság", "translation": "sustainability", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-31-03-voc.json", voc_03)

    voc_04 = {
        "id": "vocab.b1.31.04",
        "lesson": "b1-31-04",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "aggodalom", "translation": "concern, anxiety, worry", "pos": "noun"},
            {"lemma": "reményteljes", "translation": "hopeful, promising, auspicious", "pos": "adjective"},
            {"lemma": "bizonytalanság", "translation": "uncertainty, precariousness", "pos": "noun"},
            {"lemma": "kihívás", "translation": "challenge, demanding trial", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-31-04-voc.json", voc_04)

    voc_05 = {
        "id": "vocab.b1.31.05",
        "lesson": "b1-31-05",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "távlat", "translation": "perspective, outlook, horizon", "pos": "noun"},
            {"lemma": "fejlődés", "translation": "progress, evolution, development", "pos": "noun"},
            {"lemma": "következmény", "translation": "consequence, outcome, repercussion", "pos": "noun"},
            {"lemma": "nemzedékek közötti szolidaritás", "translation": "intergenerational solidarity", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-31-05-voc.json", voc_05)

    # -------------------------------------------------------------------------
    # 2. Grammar Files (2 per lesson = 10 files)
    # -------------------------------------------------------------------------
    # Lesson 01
    gr_01_a = {
        "id": "grammar.b1.31.01.predictive-registers",
        "title": "Predictive Registers: Várhatóan, Előreláthatólag & Jó eséllyel",
        "sections": [
            {
                "type": "text",
                "title": "Predictive Adverbs",
                "content": "When discussing the future of society, Hungarian uses epistemic adverbs to frame the degree of certainty. 'Várhatóan' (expectedly), 'előreláthatólag' (foreseeably), and 'jó eséllyel' (with good chances) indicate strong probability without claiming absolute certainty."
            },
            {
                "type": "examples",
                "title": "Predictive examples",
                "items": [
                    {"spanish": "A szakértők szerint a népesség várhatóan tovább növekszik.", "english": "According to experts, the population is expected to grow further."},
                    {"spanish": "Előreláthatólag új technológiák alakítják át a mindennapokat.", "english": "Foreseeably, new technologies will transform daily life."},
                    {"spanish": "Jó eséllyel megtaláljuk a megoldást az energiagondokra.", "english": "With good chances we will find the solution to energy issues."}
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-31-01-a-gr.json", gr_01_a)

    gr_01_b = {
        "id": "grammar.b1.31.01.unfolding-verbs",
        "title": "Framing Future Processes: Kibontakozik & Alakot ölt",
        "sections": [
            {
                "type": "text",
                "title": "Verbal Idioms of Evolution",
                "content": "Verbal idioms such as 'kibontakozik' (unfolds, matures), 'alakot ölt' (takes shape), and 'jövőképet vázol fel' (outlines a vision) are standard when discussing long-term socio-historical trajectories."
            },
            {
                "type": "examples",
                "title": "Unfolding process examples",
                "items": [
                    {"spanish": "A tudósok határozott jövőképet vázolnak fel a konferencián.", "english": "Scientists outline a clear vision of the future at the conference."},
                    {"spanish": "A digitális gazdaság új formája most kezd kibontakozni.", "english": "The new form of digital economy is beginning to unfold now."},
                    {"spanish": "A társadalom új értékrendje lassan alakot ölt.", "english": "The new value system of society is slowly taking shape."}
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-31-01-b-gr.json", gr_01_b)

    # Lesson 02
    gr_02_a = {
        "id": "grammar.b1.31.02.trend-narration",
        "title": "Describing Socio-Technological Trends: Teret hódít & Átalakulóban van",
        "sections": [
            {
                "type": "text",
                "title": "Narrating Expansion and Ongoing State",
                "content": "To describe expanding trends, Hungarian uses 'teret hódít' (gains ground, expands) and inessive state participles like 'átalakulóban van' (is in the process of transforming)."
            },
            {
                "type": "examples",
                "title": "Trend narration examples",
                "items": [
                    {"spanish": "A mesterséges intelligencia rohamosan teret hódít az iparban.", "english": "Artificial intelligence is rapidly gaining ground in industry."},
                    {"spanish": "A hagyományos munka világa alapvető átalakulóban van.", "english": "The world of traditional work is undergoing a fundamental transformation."},
                    {"spanish": "A társadalmi szokások folyamatos változást mutatnak.", "english": "Social habits exhibit continuous change."}
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-31-02-a-gr.json", gr_02_a)

    gr_02_b = {
        "id": "grammar.b1.31.02.nominalizing-processes",
        "title": "Nominalizing Complex Societal Processes with -ás/-és",
        "sections": [
            {
                "type": "text",
                "title": "Process Nominalization",
                "content": "Formal Hungarian discussion heavily relies on deverbal action nouns ending in -ás/-és (digitalizáció -> digitalizálás, automatizálás, felgyorsulás, elöregedés) to state abstract societal trends as grammatical subjects."
            },
            {
                "type": "examples",
                "title": "Nominalized process examples",
                "items": [
                    {"spanish": "A társadalom elöregedése komoly gazdasági kihívást jelent.", "english": "The aging of society represents a serious economic challenge."},
                    {"spanish": "Az ügyintézés digitalizálása jelentősen leegyszerűsíti a mindennapokat.", "english": "The digitization of administration significantly simplifies everyday life."},
                    {"spanish": "A technológiai folyamatok felgyorsulása alkalmazkodást kíván.", "english": "The acceleration of technological processes requires adaptation."}
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-31-02-b-gr.json", gr_02_b)

    # Lesson 03
    gr_03_a = {
        "id": "grammar.b1.31.03.future-participle",
        "title": "Future / Obligatory Participle -andó/-endő in Societal Planning",
        "sections": [
            {
                "type": "text",
                "title": "Obligation Participles",
                "content": "The future passive participle in -andó/-endő denotes an action that must, ought to, or will be carried out: 'megoldandó feladat' (task to be solved), 'követendő példa' (example to be followed), 'végrehajtandó reformok' (reforms to be executed)."
            },
            {
                "type": "examples",
                "title": "Participle examples",
                "items": [
                    {"spanish": "A klímaváltozás a legsürgősebben megoldandó probléma.", "english": "Climate change is the most urgently to-be-solved problem."},
                    {"spanish": "A jövő nemzedékek érdekei a legfontosabb figyelembe veendő szempontok.", "english": "The interests of future generations are the most important aspects to be taken into account."},
                    {"spanish": "Sok elvégzendő munka vár a kutatókra a megújuló energia terén.", "english": "Much work to be done awaits researchers in renewable energy."}
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-31-03-a-gr.json", gr_03_a)

    gr_03_b = {
        "id": "grammar.b1.31.03.potential-feasibility",
        "title": "Feasibility & Potentiality: Megvalósítható & Fenntartható",
        "sections": [
            {
                "type": "text",
                "title": "Feasibility Formations",
                "content": "Combining verbal stems with -ható/-hető expresses feasibility or capability: 'megvalósítható' (achievable, realizable), 'fenntartható' (sustainable), 'elkerülhető' (avoidable)."
            },
            {
                "type": "examples",
                "title": "Feasibility examples",
                "items": [
                    {"spanish": "A kitűzött célok gondos tervezéssel megvalósíthatók.", "english": "The set goals are achievable through careful planning."},
                    {"spanish": "A fenntartható gazdaság biztosítja gyermekeink jövőjét.", "english": "A sustainable economy secures the future of our children."},
                    {"spanish": "A súlyos válságok felelős döntésekkel elkerülhetők.", "english": "Severe crises are avoidable with responsible decisions."}
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-31-03-b-gr.json", gr_03_b)

    # Lesson 04
    gr_04_a = {
        "id": "grammar.b1.31.04.affective-anticipation",
        "title": "Expressing Anticipation, Apprehension & Hope",
        "sections": [
            {
                "type": "text",
                "title": "Anticipatory Predicates",
                "content": "Idiomatic predicates of anticipation convey emotional stances regarding the future: 'aggodalmat kelt' (causes concern), 'reménnyel tölt el' (fills with hope), 'bizakodásra ad okot' (gives cause for optimism)."
            },
            {
                "type": "examples",
                "title": "Anticipation examples",
                "items": [
                    {"spanish": "A természeti erőforrások fogyása méltán kelt aggodalmat.", "english": "The depletion of natural resources rightly causes concern."},
                    {"spanish": "A fiatalok környezettudatossága bizakodásra ad okot.", "english": "The environmental awareness of young people gives cause for optimism."},
                    {"spanish": "Az orvosi innovációk híre mindenkit reménnyel tölt el.", "english": "The news of medical innovations fills everyone with hope."}
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-31-04-a-gr.json", gr_04_a)

    gr_04_b = {
        "id": "grammar.b1.31.04.subjunctive-fear-hope",
        "title": "Subjunctive Complements with Tart attól & Bízik abban",
        "sections": [
            {
                "type": "text",
                "title": "Verbal Complements of Fear and Hope",
                "content": "Verbs of hoping or fearing take specific governed pro-forms and subjunctive or conditional clauses: 'tart attól, hogy nehogy...' (fears that lest), 'bízik abban, hogy sikerül...' (trusts that it will succeed)."
            },
            {
                "type": "examples",
                "title": "Hope and fear examples",
                "items": [
                    {"spanish": "Sokan tartanak attól, hogy a gépek elveszik az emberek munkáját.", "english": "Many fear that machines will take away people's jobs."},
                    {"spanish": "Bízunk abban, hogy a társadalom képes lesz megbirkózni a kihívással.", "english": "We trust that society will be able to cope with the challenge."},
                    {"spanish": "Mindannyian abban reménykedünk, hogy békés jövő vár ránk.", "english": "We all hope that a peaceful future awaits us."}
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-31-04-b-gr.json", gr_04_b)

    # Lesson 05
    gr_05_a = {
        "id": "grammar.b1.31.05.longitudinal-timeframes",
        "title": "Longitudinal Timeframes: Húsz év távlatából & Évtizedek múlva",
        "sections": [
            {
                "type": "text",
                "title": "Long-Term Temporal Expressions",
                "content": "Projecting into distant temporal horizons requires fixed spatial-temporal postpositional metaphors: 'húsz év távlatából' (from the perspective of twenty years), 'évtizedek múlva' (decades from now), 'hosszú távon' (in the long run)."
            },
            {
                "type": "examples",
                "title": "Temporal perspective examples",
                "items": [
                    {"spanish": "Húsz év távlatából teljesen másként tekintünk majd a mai vitákra.", "english": "From the perspective of twenty years, we will look at today's debates quite differently."},
                    {"spanish": "Évtizedek múlva a zöld energia válik az élet alapjává.", "english": "Decades from now, green energy will become the basis of life."},
                    {"spanish": "Hosszú távon csak a fenntartható megoldások bizonyulnak sikeresnek.", "english": "In the long run, only sustainable solutions prove successful."}
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-31-05-a-gr.json", gr_05_a)

    gr_05_b = {
        "id": "grammar.b1.31.05.consequential-syntax",
        "title": "Consequential Syntax: Következményekkel jár & Ennek fényében",
        "sections": [
            {
                "type": "text",
                "title": "Consequential Linkages",
                "content": "Synthesizing causal chains in future forecasts uses 'következményekkel jár' (carries consequences) and prepositional connectors like 'ennek fényében' (in light of this)."
            },
            {
                "type": "examples",
                "title": "Consequence examples",
                "items": [
                    {"spanish": "Minden mai döntésünk súlyos következményekkel jár a jövőre nézve.", "english": "Every decision of ours today carries serious consequences for the future."},
                    {"spanish": "Ennek fényében kötelességünk felelősségteljesen cselekedni.", "english": "In light of this, it is our duty to act responsibly."},
                    {"spanish": "A nemzedékek közötti szolidaritás erősítése elengedhetetlen a békéhez.", "english": "Strengthening intergenerational solidarity is indispensable for peace."}
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-31-05-b-gr.json", gr_05_b)

    # -------------------------------------------------------------------------
    # 3. Exercises Files (8 exercises per lesson x 5 + consolidation = 6 files)
    # -------------------------------------------------------------------------
    ex_01 = {
        "lesson": "b1-31-01",
        "exercises": [
            {
                "id": "b1-31-01.ex01",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent a 'jövőkép' kifejezés?",
                "options": [
                    "Egy társadalom vagy ember elképzelését és terveit a várható jövőről.",
                    "Egy régi fényképalbumot a nagyszülőkről.",
                    "Egy televíziós készüléket az áruházban."
                ],
                "correct": 0
            },
            {
                "id": "b1-31-01.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A szakértők szerint a gazdaság várható_____ növekedni fog a jövő évben. (expectedly - an)",
                "answer": "an"
            },
            {
                "id": "b1-31-01.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "tudósok", "biztató", "jövőképet", "vázolnak", "fel", "a", "világ", "számára."],
                "solution": ["A", "tudósok", "biztató", "jövőképet", "vázolnak", "fel", "a", "világ", "számára."]
            },
            {
                "id": "b1-31-01.ex04",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik kifejezés jelzi, hogy valami előre látható valószínűséggel bekövetkezik?",
                "options": [
                    "Előreláthatólag",
                    "Visszamenőleg",
                    "Hirtelenjében"
                ],
                "correct": 0
            },
            {
                "id": "b1-31-01.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "Az új technológiai forradalom lassan kezdi kibontakozás_____ elérni. (its unfolding - át)",
                "answer": "át"
            },
            {
                "id": "b1-31-01.ex06",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit nevezünk 'előrejelzésnek'?",
                "options": [
                    "Adatokon és trendeken alapuló szakmai becslést a jövőbeli eseményekről.",
                    "Egy tegnap megtörtént családi beszélgetést.",
                    "Egy könyv utolsó oldalának elolvasását."
                ],
                "correct": 0
            },
            {
                "id": "b1-31-01.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A jövő új lehetőségeket tartogat mindannyiunk számá_____. (for us - ra)",
                "answer": "ra"
            },
            {
                "id": "b1-31-01.ex08",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "technológia", "fejlődése", "új", "lehetőségeket", "teremt", "a", "fiataloknak."],
                "solution": ["A", "technológia", "fejlődése", "új", "lehetőségeket", "teremt", "a", "fiataloknak."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-31-01-ex.json", ex_01)

    ex_02 = {
        "lesson": "b1-31-02",
        "exercises": [
            {
                "id": "b1-31-02.ex01",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent a 'digitalizáció' a modern társadalomban?",
                "options": [
                    "Az információk, adatok és szolgáltatások digitális rendszerekbe való átültetését.",
                    "Kézzel írott levelek postai feladását.",
                    "A papírgyártás növelését az erdőkben."
                ],
                "correct": 0
            },
            {
                "id": "b1-31-02.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A munka világa alapvető átalakuló_____ van a modern gépek miatt. (in transformation - ban)",
                "answer": "ban"
            },
            {
                "id": "b1-31-02.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "mesterséges", "intelligencia", "rohamosan", "teret", "hódít", "minden", "ágazatban."],
                "solution": ["A", "mesterséges", "intelligencia", "rohamosan", "teret", "hódít", "minden", "ágazatban."]
            },
            {
                "id": "b1-31-02.ex04",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Hogyan fejezzük ki helyesen a társadalom elöregedésének folyamatát igéből képzett főnévvel?",
                "options": [
                    "A társadalom elöregedése komoly feladat elé állítja az egészségügyet.",
                    "A társadalom elöregszik feladat egészségügy.",
                    "Elöregedett társadalmat lát az orvos."
                ],
                "correct": 0
            },
            {
                "id": "b1-31-02.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A gyártás automatizáció_____ révén növekszik a termelékenység. (its automation - ja)",
                "answer": "ja"
            },
            {
                "id": "b1-31-02.ex06",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent a 'társadalmi tendencia' kifejezés?",
                "options": [
                    "Olyan tartós irányzatot vagy fejlődési vonalat, amely a társadalom nagy részét érinti.",
                    "Egy egyszeri divathóbortot a ruházkodásban.",
                    "Egy gyorsan elmúló pletykát az újságokban."
                ],
                "correct": 0
            },
            {
                "id": "b1-31-02.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Az új technológiák alkalmazkodás_____ kívánnak meg minden dolgozótól. (adaptation - t)",
                "answer": "t"
            },
            {
                "id": "b1-31-02.ex08",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "társadalmi", "átalakulás", "minden", "család", "életére", "hatással", "van."],
                "solution": ["A", "társadalmi", "átalakulás", "minden", "család", "életére", "hatással", "van."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-31-02-ex.json", ex_02)

    ex_03 = {
        "lesson": "b1-31-03",
        "exercises": [
            {
                "id": "b1-31-03.ex01",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit fejez ki a 'fenntarthatóság' elve?",
                "options": [
                    "Hogy a jelen igényeit úgy elégítsük ki, hogy ne veszélyeztessük a jövő nemzedékek életfeltételeit.",
                    "Hogy minden épületet betonból kell felépíteni.",
                    "Hogy nem szabad új dolgokat tanulni az iskolában."
                ],
                "correct": 0
            },
            {
                "id": "b1-31-03.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A klímaváltozás a legsürgősebben megold_____ feladat. (to be solved - andó)",
                "answer": "andó"
            },
            {
                "id": "b1-31-03.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "tudományos", "innováció", "alapvető", "feltétele", "a", "társadalmi", "megújulásnak."],
                "solution": ["A", "tudományos", "innováció", "alapvető", "feltétele", "a", "társadalmi", "megújulásnak."]
            },
            {
                "id": "b1-31-03.ex04",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Hogyan fejezzük ki a megvalósíthatóságot és fenntarthatóságot helyes melléknévi képzővel?",
                "options": [
                    "A környezetbarát gazdaság hosszú távon is fenntartható.",
                    "A környezetbarát gazdaság fenntartólag van.",
                    "A környezet fenntartása gazdasági ember."
                ],
                "correct": 0
            },
            {
                "id": "b1-31-03.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "Az energetikai innováció_____ kulcsfontosságúak az önellátásban. (innovations - k)",
                "answer": "k"
            },
            {
                "id": "b1-31-03.ex06",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent a társadalmi 'megújulás'?",
                "options": [
                    "A gondolkodásmód, az intézmények és a technológia korszerűsítését, frissítését.",
                    "A régi épületek lebontását és üresen hagyását.",
                    "A telefonkészülék napi újratöltését."
                ],
                "correct": 0
            },
            {
                "id": "b1-31-03.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Számos elvégz_____ feladat áll még a kutatók előtt. (to be done - endő)",
                "answer": "endő"
            },
            {
                "id": "b1-31-03.ex08",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "fenntarthatóság", "nem", "választás,", "hanem", "a", "jövő", "záloga."],
                "solution": ["A", "fenntarthatóság", "nem", "választás,", "hanem", "a", "jövő", "záloga."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-31-03-ex.json", ex_03)

    ex_04 = {
        "lesson": "b1-31-04",
        "exercises": [
            {
                "id": "b1-31-04.ex01",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent, ha egy jövőkép 'reményteljes'?",
                "options": [
                    "Hogy pozitív kilátásokkal kecsegtet, bizalommal és optimizmussal tölthet el bennünket.",
                    "Hogy teljesen reménytelen és sötét jövőt vetít előre.",
                    "Hogy tegnap reggel esett az eső a városban."
                ],
                "correct": 0
            },
            {
                "id": "b1-31-04.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Sokan tartanak attól, hogy a gazdasági válság bizonytalanság_____ okoz. (uncertainty - ot)",
                "answer": "ot"
            },
            {
                "id": "b1-31-04.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Bízunk", "abban,", "hogy", "az", "emberiség", "képes", "megoldani", "a", "problémákat."],
                "solution": ["Bízunk", "abban,", "hogy", "az", "emberiség", "képes", "megoldani", "a", "problémákat."]
            },
            {
                "id": "b1-31-04.ex04",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik igei kifejezés jelenti azt, hogy egy hír vagy jelenség bizakodásra késztet?",
                "options": [
                    "Reménnyel tölt el",
                    "Aggodalmat kelt",
                    "Kétségbeesésbe dönt"
                ],
                "correct": 0
            },
            {
                "id": "b1-31-04.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A természeti környezet pusztulása méltán kelt aggodalm_____. (concern - at)",
                "answer": "at"
            },
            {
                "id": "b1-31-04.ex06",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mi az a 'kihívás' társadalmi összefüggésben?",
                "options": [
                    "Egy olyan nehéz, de megoldandó feladat, amely komoly erőfeszítést és összefogást igényel.",
                    "Egy barátságtalan párbajfelhívás a múlt században.",
                    "A sportcipő felvétele a reggeli futáshoz."
                ],
                "correct": 0
            },
            {
                "id": "b1-31-04.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A fiatalok elszántsága bizakodás_____ ad okot a nehéz időkben. (cause for optimism - ra)",
                "answer": "ra"
            },
            {
                "id": "b1-31-04.ex08",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "jövő", "kihívásai", "közös", "cselekvésre", "késztetik", "az", "egész", "társadalmat."],
                "solution": ["A", "jövő", "kihívásai", "közös", "cselekvésre", "késztetik", "az", "egész", "társadalmat."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-31-04-ex.json", ex_04)

    ex_05 = {
        "lesson": "b1-31-05",
        "exercises": [
            {
                "id": "b1-31-05.ex01",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent a 'nemzedékek közötti szolidaritás'?",
                "options": [
                    "A fiatalok, az aktív korúak és az idős generációk kölcsönös tiszteletét, támogatását és felelősségvállalását.",
                    "Hogy a fiatalok nem beszélnek az idősekkel a családban.",
                    "Egy sportversenyt az iskolák és a nyugdíjas klubok között."
                ],
                "correct": 0
            },
            {
                "id": "b1-31-05.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Húsz év távlatá_____ visszatekintve látni fogjuk a mai döntések valódi értékét. (from perspective - ból)",
                "answer": "ból"
            },
            {
                "id": "b1-31-05.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "felelőtlen", "döntések", "súlyos", "következményekkel", "járnak", "a", "jövőre", "nézve."],
                "solution": ["A", "felelőtlen", "döntések", "súlyos", "következményekkel", "járnak", "a", "jövőre", "nézve."]
            },
            {
                "id": "b1-31-05.ex04",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Hogyan fogalmazzuk meg a következtetést az 'ennek fényében' kifejezéssel?",
                "options": [
                    "Ennek fényében kötelességünk felelősen megtervezni az elkövetkező évtizedeket.",
                    "Ennek fényében sötét van a szobában este.",
                    "Fényében világít a lámpa az utcán."
                ],
                "correct": 0
            },
            {
                "id": "b1-31-05.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A társadalom békés fejlődés_____ minden ember közös érdeke. (its development - e)",
                "answer": "e"
            },
            {
                "id": "b1-31-05.ex06",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Mit üzen az Úr Ádámnak Madách Imre 'Az ember tragédiája' című művének végén?",
                "options": [
                    "Hogy a küzdelem maga a cél, és a hitet, a reményt soha nem szabad elveszíteni: 'Mondottam, ember: küzdj és bízva bízzál!'",
                    "Hogy Lucifernek volt igaza minden történelmi kérdésben.",
                    "Hogy hagyja el a Földet, és költözzön a Marsra."
                ],
                "correct": 0
            },
            {
                "id": "b1-31-05.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A jövő távlat_____ tekintve optimistán kell készülnünk az előttünk álló évekre. (perspectives - ait)",
                "answer": "ait"
            },
            {
                "id": "b1-31-05.ex08",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "nemzedékek", "összefogása", "biztosítja", "a", "kultúra", "és", "az", "élet", "folytonosságát."],
                "solution": ["A", "nemzedékek", "összefogása", "biztosítja", "a", "kultúra", "és", "az", "élet", "folytonosságát."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-31-05-ex.json", ex_05)

    ex_consolidation = {
        "lesson": "b1-31-consolidation",
        "exercises": [
            {
                "id": "b1-31-consolidation.ex01",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Melyik szó jelenti a jövőre vonatkozó átfogó, inspiráló elképzelést?",
                "options": [
                    "Jövőkép",
                    "Visszaemlékezés",
                    "Záróvizsga"
                ],
                "correct": 0
            },
            {
                "id": "b1-31-consolidation.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A fenntartható energiagazdálkodás a legsürgősebben megold_____ feladatunk. (to be solved - andó)",
                "answer": "andó"
            },
            {
                "id": "b1-31-consolidation.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "technológiai", "újítások", "alapjaiban", "alakítják", "át", "a", "társadalom", "életét."],
                "solution": ["A", "technológiai", "újítások", "alapjaiban", "alakítják", "át", "a", "társadalom", "életét."]
            },
            {
                "id": "b1-31-consolidation.ex04",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Hogyan fejezzük ki helyesen a jövőbeli következményekkel járó felelősséget?",
                "options": [
                    "A mai döntések hosszú távú következményekkel járnak a jövő nemzedékekre nézve.",
                    "A mai döntés következik a jövőből tegnap.",
                    "Járnak a következmények az utcán."
                ],
                "correct": 0
            },
            {
                "id": "b1-31-consolidation.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A fenntartható gazdaság biztosítja a nemzedékek közötti szolidaritás_____. (its solidarity - t)",
                "answer": "t"
            },
            {
                "id": "b1-31-consolidation.ex06",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "tudomány", "és", "az", "emberség", "együtt", "teremthet", "élhető", "jövőt."],
                "solution": ["A", "tudomány", "és", "az", "emberség", "együtt", "teremthet", "élhető", "jövőt."]
            },
            {
                "id": "b1-31-consolidation.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Előrelátható_____ a mesterséges intelligencia minden ember munkáját befolyásolja majd. (foreseeably - lag)",
                "answer": "lag"
            },
            {
                "id": "b1-31-consolidation.ex08",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Miért számít Madách Imre Tragédiája az emberi társadalom jövőjének alapvető művészi látleletének?",
                "options": [
                    "Mert bemutatja az emberiség történelmi korszakait és lehetséges jövőbeli tévútjait, miközben az erkölcsi küzdelem és remény örök parancsát hirdeti.",
                    "Mert pontos műszaki leírást ad a 19. századi gőzgépekről.",
                    "Mert kizárólag a párizsi divatról szól."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-31-consolidation-ex.json", ex_consolidation)

    # -------------------------------------------------------------------------
    # 4. Classic Story Adaptation for Consolidation: Az ember tragédiája
    # -------------------------------------------------------------------------
    story_classic = {
        "id": "story.b1.31.classic",
        "title": "Az ember tragédiája",
        "level": "B1",
        "order": 31,
        "type": "classics",
        "estimatedMinutes": 8,
        "summary": "An adaptation of Imre Madách's philosophical dramatic poem 'Az ember tragédiája' (The Tragedy of Man, 1861), one of the supreme achievements of Hungarian literature. Adam, guided by Lucifer, travels through human history and peers into the future of society—from ancient civilizations, revolutions, and London capitalism to a sterile futuristic Phalanstery and an icy, dying Earth. Confronted with the terrifying risks of scientific coldness and loss of spirit, Adam is saved by Eve's maternal love and the Lord's transcendent command to perpetually strive and believe: 'Mondottam, ember: küzdj és bízva bízzál!'",
        "characters": [
            "Ádám, az első ember és az emberiség szellemi vándora",
            "Éva, az élet, a szerelem és a megújulás jelképe",
            "Lucifer, a tagadás és a rideg értelem szelleme",
            "Az Úr, a teremtő és a remény forrása"
        ],
        "location": "A Földön kívüli űr és a jövőbeli társadalom színterei",
        "author": "Madách Imre",
        "work": "Az ember tragédiája (1861)",
        "paragraphs": [
            {
                "type": "narration",
                "text": "A paradicsomból való kiűzetés után Ádám tudni akarta, mi vár az emberiségre az elkövetkező évezredek során. A tagadás rideg szelleme, Lucifer álmot bocsátott rá, és végigvezette a történelem nagy színterein."
            },
            {
                "type": "narration",
                "text": "Ádám látta a fáraók Egyiptomát, a demokratikus Athént, a dekadens Rómát, a keresztes hadjáratokat, a francia forradalom dicsőségét és vérét, valamint a szabadpiaci London zűrzavarát. Ám a legmegrázóbb élmény akkor érte, amikor a távoli jövő társadalmába érkezett: a Falanszterbe."
            },
            {
                "type": "dialogue",
                "speaker": "Lucifer",
                "text": "Íme, a jövő, amelyre annyira vágytál! Itt a tudomány uralkodik: nincsenek nemzetek, nincsenek háborúk, nincs művészet vagy költészet. Mindenki csak egy szám a közös gépezetben."
            },
            {
                "type": "narration",
                "text": "A Falanszterben a gyermekeket elszakították anyjuktól, Platón és Michelangelo büntetésből fazekasinas volt, és a növényeket kémiai lombikokban tenyésztették. Ádám elborzadt: megértette, hogy a rideg technológia és az érzelemmentes rend elpusztítja az igazi emberi lelket."
            },
            {
                "type": "narration",
                "text": "Amikor a Nap kihűlt, és a Föld jégmezővé változott, Ádám felébredt álmából. Kétségbeesésében a sziklaszirtről akart a mélybe ugrani, hogy véget vessen az emberiség tragikus sorsának, mielőtt az elkezdődne."
            },
            {
                "type": "dialogue",
                "speaker": "Éva",
                "text": "Ádám, állj meg! Élek, és anya vagyok... A jövő nem a halálé, hanem az életé!"
            },
            {
                "type": "narration",
                "text": "Az élet szent ígérete előtt a kétely és a cinizmus vereséget szenvedett. Megnyílt az ég, és megszólalt a Teremtő szózata, amely nem csupán Ádámnak, hanem minden jövőbeli nemzedéknek utat mutatott:"
            },
            {
                "type": "dialogue",
                "speaker": "Az Úr",
                "text": "Mondottam, ember: küzdj és bízva bízzál!"
            }
        ]
    }
    write_json("content/hu/stories/classics/b1/b1-31-madach.json", story_classic)

    # -------------------------------------------------------------------------
    # 5. Lesson Files (01 to 05 + consolidation)
    # -------------------------------------------------------------------------
    lesson_titles = {
        "01": ("Jövőkép és előrejelzések", "Vision of the Future & Projections"),
        "02": ("Társadalmi tendenciák és a digitalizáció", "Social Trends & Digital Transformation"),
        "03": ("Megoldandó feladatok és fenntarthatóság", "Tasks to Be Solved & Sustainability"),
        "04": ("Aggodalmak, remények és kihívások", "Concerns, Hopes & Challenges"),
        "05": ("Távlatok, fejlődés és a nemzedékek szolidaritása", "Long-Term Horizons & Intergenerational Solidarity")
    }

    grammar_refs = {
        "01": ["grammar/b1/b1-31-01-a-gr.json", "grammar/b1/b1-31-01-b-gr.json"],
        "02": ["grammar/b1/b1-31-02-a-gr.json", "grammar/b1/b1-31-02-b-gr.json"],
        "03": ["grammar/b1/b1-31-03-a-gr.json", "grammar/b1/b1-31-03-b-gr.json"],
        "04": ["grammar/b1/b1-31-04-a-gr.json", "grammar/b1/b1-31-04-b-gr.json"],
        "05": ["grammar/b1/b1-31-05-a-gr.json", "grammar/b1/b1-31-05-b-gr.json"]
    }

    for i in range(1, 6):
        padded = f"0{i}"
        hu_t, en_t = lesson_titles[padded]
        lesson_data = {
            "id": f"lesson.b1.31-{padded}",
            "unit": 31,
            "title": f"{hu_t} ({en_t})",
            "level": "B1",
            "grammar": "Predictive Registers, Future Participles (-andó/-endő) & Societal Discourse in Hungarian",
            "sections": [
                {
                    "type": "goal",
                    "title": "Lesson Goals",
                    "items": [
                        f"I can discuss {en_t} in Hungarian.",
                        "I can use epistemic adverbs (várhatóan, előreláthatólag) and future participles (-andó/-endő).",
                        "I can describe social and technological transformation and sustainability.",
                        "I can analyze Imre Madách's philosophical masterpiece 'Az ember tragédiája'."
                    ]
                },
                {"type": "recycle", "count": 3},
                {"type": "vocabulary", "ref": f"vocabulary/b1/b1-31-{padded}-voc.json"},
                {"type": "grammar", "ref": grammar_refs[padded][0]},
                {"type": "grammar", "ref": grammar_refs[padded][1]},
                {
                    "type": "exercise-group",
                    "title": "Practice",
                    "ref": f"exercises/b1/b1-31-{padded}-ex.json",
                    "exerciseRefs": [f"b1-31-{padded}.ex0{k}" for k in range(1, 9)]
                }
            ]
        }
        write_json(f"content/hu/lessons/b1/b1-31-{padded}.json", lesson_data)

    consolidation_data = {
        "id": "lesson.b1.31-consolidation",
        "unit": 31,
        "title": "Unit 31 Consolidation",
        "level": "B1",
        "grammar": "Consolidation of Future Projections, Participles & Madách's Az ember tragédiája",
        "sections": [
            {
                "type": "story",
                "title": "Az ember tragédiája (Madách Imre)",
                "ref": "stories/classics/b1/b1-31-madach.json"
            },
            {
                "type": "exercise-group",
                "title": "Consolidation Practice",
                "ref": "exercises/b1/b1-31-consolidation-ex.json",
                "exerciseRefs": [f"b1-31-consolidation.ex0{k}" for k in range(1, 9)]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-31-consolidation.json", consolidation_data)
    print("Successfully built Hungarian B1 Core Unit 31 (b1-31)!")

if __name__ == "__main__":
    build_unit_31_core()
