#!/usr/bin/env python3
"""Generate Hungarian B1 Core Unit 34: Complex Opinions (b1-34)."""

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

def build_unit_34_core():
    # -------------------------------------------------------------------------
    # 1. Vocabulary Files (4 words each = 20 words total)
    # -------------------------------------------------------------------------
    voc_01 = {
        "id": "vocab.b1.34.01",
        "lesson": "b1-34-01",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "véleménynyilvánítás", "translation": "expression of opinion, stating one's views", "pos": "noun"},
            {"lemma": "meglátás", "translation": "insight, perspective, view", "pos": "noun"},
            {"lemma": "álláspont", "translation": "standpoint, position, point of view", "pos": "noun"},
            {"lemma": "érvelés", "translation": "reasoning, argumentation, line of argument", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-34-01-voc.json", voc_01)

    voc_02 = {
        "id": "vocab.b1.34.02",
        "lesson": "b1-34-02",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "szempont", "translation": "aspect, point of view, criteria", "pos": "noun"},
            {"lemma": "mérlegelés", "translation": "weighing, deliberation, consideration", "pos": "noun"},
            {"lemma": "viszonylagosság", "translation": "relativity, nuance, non-absoluteness", "pos": "noun"},
            {"lemma": "egyensúly", "translation": "balance, equilibrium, poise", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-34-02-voc.json", voc_02)

    voc_03 = {
        "id": "vocab.b1.34.03",
        "lesson": "b1-34-03",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "árnyalás", "translation": "nuance, qualification, shading of meaning", "pos": "noun"},
            {"lemma": "kivétel", "translation": "exception", "pos": "noun"},
            {"lemma": "megkötés", "translation": "stipulation, qualification, reservation", "pos": "noun"},
            {"lemma": "fenntartás", "translation": "reservation, qualification, doubt", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-34-03-voc.json", voc_03)

    voc_04 = {
        "id": "vocab.b1.34.04",
        "lesson": "b1-34-04",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "ellenérv", "translation": "counter-argument, opposing point", "pos": "noun"},
            {"lemma": "meggyőződés", "translation": "conviction, firm belief", "pos": "noun"},
            {"lemma": "bizonyítás", "translation": "proof, demonstration, substantiation", "pos": "noun"},
            {"lemma": "cáfolat", "translation": "refutation, rebuttal", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-34-04-voc.json", voc_04)

    voc_05 = {
        "id": "vocab.b1.34.05",
        "lesson": "b1-34-05",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "összegzés", "translation": "summary, synthesizing conclusion", "pos": "noun"},
            {"lemma": "kompromisszum", "translation": "compromise, mutual concession", "pos": "noun"},
            {"lemma": "tanulság", "translation": "moral, lesson learned, takeaway", "pos": "noun"},
            {"lemma": "végkövetkeztetés", "translation": "final conclusion, bottom line", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-34-05-voc.json", voc_05)

    # -------------------------------------------------------------------------
    # 2. Grammar Files (2 per regular lesson = 10 files)
    # -------------------------------------------------------------------------
    gr_01_a = {
        "id": "grammar.b1.34.01.nested-opinion-clauses",
        "title": "Nested Opinion Matrices: Azt gondolom, hogy... mert...",
        "sections": [
            {
                "type": "text",
                "title": "Structuring Multi-Level Opinions",
                "content": "In Hungarian, expressing nuanced beliefs involves nesting causal clauses under mental evaluation verbs (*gondol, vél, hisz, tart*). The primary matrix uses an anticipatory demonstrative pronoun (*azt gondolom, úgy vélem, amellett vagyok*), followed by *hogy* and an explanatory conjunction like *mert* or *mivel*."
            },
            {
                "type": "examples",
                "title": "Nested opinion examples",
                "items": [
                    {"spanish": "Azt gondolom, hogy a terv megvalósítható, mert elegendő forrás áll rendelkezésre.", "english": "I think that the plan is feasible because sufficient resources are available."},
                    {"spanish": "Úgy vélem, hogy a döntés helyes volt, mivel figyelembe vette a közérdeket.", "english": "I believe that the decision was correct since it took the public interest into account."},
                    {"spanish": "Amellett vagyok, hogy folytassuk a párbeszédet, hiszen mindkét fél nyitott a kompromisszumra.", "english": "I am in favor of continuing dialogue, given that both parties are open to compromise."}
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-34-01-a-gr.json", gr_01_a)

    gr_01_b = {
        "id": "grammar.b1.34.01.degree-and-nuance-adverbs",
        "title": "Degree & Nuance Modifiers: Határozottan, részben, túlnyomórészt",
        "sections": [
            {
                "type": "text",
                "title": "Calibrating Degree of Agreement",
                "content": "Rather than flat agreement or disagreement, B1 Hungarian uses degree adverbs to calibrate commitment: *határozottan* (definitely), *részben* (partially), *túlnyomórészt* (predominantly), *alapvetően* (fundamentally), and *bizonyos fokig* (to a certain extent)."
            },
            {
                "type": "examples",
                "title": "Modifier examples",
                "items": [
                    {"spanish": "Részben egyetértek az álláspontoddal, de vannak kétségeim.", "english": "I partly agree with your position, but I have doubts."},
                    {"spanish": "Határozottan úgy vélem, hogy a javaslat hosszú távon előnyös.", "english": "I definitely believe that the proposal is beneficial in the long run."},
                    {"spanish": "Túlnyomórészt megalapozottnak tartom a kritikát.", "english": "I consider the critique predominantly well-founded."}
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-34-01-b-gr.json", gr_01_b)

    gr_02_a = {
        "id": "grammar.b1.34.02.correlative-balance",
        "title": "Dual Perspectives: Egyrészt..., másrészt...",
        "sections": [
            {
                "type": "text",
                "title": "Balancing Two Sides of an Issue",
                "content": "To weigh conflicting perspectives, Hungarian pairs correlative adverbs: *egyrészt... másrészt...* (on the one hand... on the other hand...) or the more formal *egyfelől... másfelől...*. Each coordinate clause presents a distinct argument."
            },
            {
                "type": "examples",
                "title": "Correlative balance examples",
                "items": [
                    {"spanish": "Egyrészt a technológia megkönnyíti az életet, másrészt új függőségeket hoz létre.", "english": "On the one hand, technology makes life easier; on the other hand, it creates new dependencies."},
                    {"spanish": "Egyfelől megértem az anyagi szempontokat, másfelől nem szabad megfeledkeznünk az emberi tényezőről.", "english": "On the one hand I understand the financial aspects; on the other hand we must not forget the human factor."},
                    {"spanish": "Egyrészt drágább, másrészt viszont sokkal tartósabb.", "english": "On the one hand it is more expensive, but on the other hand it is far more durable."}
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-34-02-a-gr.json", gr_02_a)

    gr_02_b = {
        "id": "grammar.b1.34.02.adversative-connectors",
        "title": "Contrastive Flow: Ellenben, viszont, mindazonáltal",
        "sections": [
            {
                "type": "text",
                "title": "Expressing Contrast Across Arguments",
                "content": "To pivot between contrasting arguments within nuanced discussions, Hungarian uses post-positive *viszont* (however), literary *ellenben* (by contrast), and dignified *mindazonáltal* (nevertheless)."
            },
            {
                "type": "examples",
                "title": "Adversative examples",
                "items": [
                    {"spanish": "A kezdeti költségek magasak, a várható megtérülés viszont kedvező.", "english": "The initial costs are high; the expected return, however, is favorable."},
                    {"spanish": "Sokan elutasították a tervezetet, a szakértők ellenben támogatták.", "english": "Many rejected the draft; experts, by contrast, supported it."},
                    {"spanish": "A feladat nehéz, mindazonáltal nem lehetetlen megoldani.", "english": "The task is difficult; nevertheless, it is not impossible to solve."}
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-34-02-b-gr.json", gr_02_b)

    gr_03_a = {
        "id": "grammar.b1.34.03.concession-in-opinion",
        "title": "Concession in Opinion: Bár... mégis, jóllehet, noha",
        "sections": [
            {
                "type": "text",
                "title": "Forming Concessive Clauses",
                "content": "In sophisticated argumentation, conceding a valid counterpoint strengthens one's credibility. Hungarian uses *bár... mégis* (although... still), *jóllehet* (even though), or *noha* (albeit). The subordinate clause introduces the concession while the main clause asserts the primary thesis."
            },
            {
                "type": "examples",
                "title": "Concessive examples",
                "items": [
                    {"spanish": "Bár vannak hibái a rendszernek, mégis ez a legmegbízhatóbb megoldás.", "english": "Although the system has flaws, it is still the most reliable solution."},
                    {"spanish": "Jóllehet nem mindenki ért egyet, a többség támogatja a döntést.", "english": "Even though not everyone agrees, the majority supports the decision."},
                    {"spanish": "Noha a vita heves volt, a felek békésen váltak el.", "english": "Albeit the debate was heated, the parties parted peacefully."}
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-34-03-a-gr.json", gr_03_a)

    gr_03_b = {
        "id": "grammar.b1.34.03.stipulations-and-reservations",
        "title": "Stipulations & Conditions: Azzal a feltétellel, amennyiben",
        "sections": [
            {
                "type": "text",
                "title": "Qualifying Arguments with Conditions",
                "content": "To attach conditions to one's agreement, use *azzal a feltétellel / kikötéssel, hogy...* (on the condition that...) or formal conditional *amennyiben... úgy...* (insofar as... then...)."
            },
            {
                "type": "examples",
                "title": "Stipulation examples",
                "items": [
                    {"spanish": "Támogatom a javaslatot azzal a fenntartással, hogy átlátható marad a végrehajtás.", "english": "I support the proposal with the reservation that implementation remains transparent."},
                    {"spanish": "Amennyiben minden fél betartja a szabályokat, a megállapodás sikeres lesz.", "english": "Insofar as all parties follow the rules, the agreement will be successful."},
                    {"spanish": "Csak akkor fogadom el a kritikát, ha konkrét tényekre épül.", "english": "I only accept the criticism if it is based on concrete facts."}
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-34-03-b-gr.json", gr_03_b)

    gr_04_a = {
        "id": "grammar.b1.34.04.refuting-counterarguments",
        "title": "Refuting Counterarguments: Ezzel szemben, nem állja meg a helyét",
        "sections": [
            {
                "type": "text",
                "title": "Deconstructing Opposing Claims",
                "content": "To actively dismantle a counterargument, formal Hungarian uses *ezzel szemben úgy vélem, hogy...* (in contrast to this I hold that...) or the idiomatic rejection *nem állja meg a helyét az az állítás, hogy...* (the assertion that... does not hold water)."
            },
            {
                "type": "examples",
                "title": "Refutation examples",
                "items": [
                    {"spanish": "Nem állja meg a helyét az a vád, hogy nem tájékoztattuk a lakosságot.", "english": "The accusation that we did not inform the public does not hold water."},
                    {"spanish": "Ezzel a feltételezéssel szemben a statisztikák mást mutatnak.", "english": "In contrast to this assumption, statistics show otherwise."},
                    {"spanish": "Cáfoljuk azt a megállapítást, miszerint elkésett a beavatkozás.", "english": "We refute the finding according to which the intervention was delayed."}
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-34-04-a-gr.json", gr_04_a)

    gr_04_b = {
        "id": "grammar.b1.34.04.reinforcing-certainty",
        "title": "Epistemic Reinforcement: Kétségkívül, minden bizonnyal",
        "sections": [
            {
                "type": "text",
                "title": "Expressing Firm Conviction",
                "content": "When defending an argument with confidence, speakers deploy modal disjuncts such as *kétségkívül* (undoubtedly), *minden bizonnyal* (in all probability / most certainly), *nyilvánvalóan* (obviously), and *vitathatatlanul* (indisputably)."
            },
            {
                "type": "examples",
                "title": "Epistemic reinforcement examples",
                "items": [
                    {"spanish": "Kétségkívül ez volt az elmúlt évek legfontosabb döntése.", "english": "Undoubtedly this was the most important decision of recent years."},
                    {"spanish": "Vitathatatlanul szükség van a strukturális reformokra.", "english": "There is indisputably a need for structural reforms."},
                    {"spanish": "Minden bizonnyal pozitív hatással lesz a gazdaságra.", "english": "In all probability it will exert a positive impact on the economy."}
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-34-04-b-gr.json", gr_04_b)

    gr_05_a = {
        "id": "grammar.b1.34.05.concluding-syntheses",
        "title": "Synthesizing Conclusions: Mindent egybevetve, a fentiek tükrében",
        "sections": [
            {
                "type": "text",
                "title": "Drawing Balanced Conclusions",
                "content": "To deliver a synthesizing final verdict after weighing multiple perspectives, use introductory idioms: *mindent egybevetve* (all things considered), *a fentiek tükrében* (in light of the above), *végeredményben* (in the final analysis), and *összegzésképpen elmondható, hogy...* (in summary it can be said that...)."
            },
            {
                "type": "examples",
                "title": "Synthesis examples",
                "items": [
                    {"spanish": "Mindent egybevetve a projekt elérte a kitűzött céljait.", "english": "All things considered, the project achieved its set objectives."},
                    {"spanish": "A fentiek tükrében indokolt a javaslat elfogadása.", "english": "In light of the above, accepting the proposal is justified."},
                    {"spanish": "Végeredményben mindkét félnek engednie kellett a megegyezéshez.", "english": "In the final analysis, both parties had to make concessions to reach an agreement."}
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-34-05-a-gr.json", gr_05_a)

    gr_05_b = {
        "id": "grammar.b1.34.05.pragmatic-opinion-hedges",
        "title": "Pragmatic Opinion Hedges: Meglátásom szerint, amennyire meg tudom ítélni",
        "sections": [
            {
                "type": "text",
                "title": "Hedging Complex Assessments",
                "content": "Cultivated Hungarian speakers frame personal assessments with polite hedging formulas: *meglátásom szerint* (in my view), *amennyire meg tudom ítélni* (as far as I can judge), *ha szabad így fogalmaznom* (if I may put it this way), and *szerény véleményem szerint* (in my modest opinion)."
            },
            {
                "type": "examples",
                "title": "Hedging examples",
                "items": [
                    {"spanish": "Meglátásom szerint a kérdés sokkal összetettebb annál, semhogy gyorsan döntsünk.", "english": "In my view, the issue is far more complex than to decide hastily."},
                    {"spanish": "Amennyire meg tudom ítélni, a megállapodás mindkét fél érdekeit szolgálja.", "english": "As far as I can judge, the agreement serves both parties' interests."},
                    {"spanish": "Ha szabad így fogalmaznom, az idő a mi oldalunkon áll.", "english": "If I may put it this way, time is on our side."}
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-34-05-b-gr.json", gr_05_b)

    # -------------------------------------------------------------------------
    # 3. Classic Story: Babits Mihály - A gólyakalifa (b1-34-babits.json)
    # -------------------------------------------------------------------------
    story = {
        "id": "story.b1.34.classic",
        "title": "A gólyakalifa",
        "level": "B1",
        "order": 34,
        "type": "classics",
        "estimatedMinutes": 8,
        "summary": "An adaptation from Mihály Babits's brilliant psychological novel 'A gólyakalifa' (The Caliph Stork). Elemér Tábory, an aristocratic young intellectual, wrestles with the dual nature of reality and consciousness: in his waking hours he lives in luxury and refinement, yet each night he dreams of living as a tormented, destitute apprentice. Weighed down by opposing truths, he seeks to understand whether our identity is a single path or a complex balance of conflicting realities.",
        "characters": [
            "Tábory Elemér",
            "A professzor"
        ],
        "location": "Budapest, Tábory-palota",
        "author": "Babits Mihály",
        "work": "A gólyakalifa",
        "paragraphs": [
            {
                "type": "narration",
                "text": "A Tábory-palota csendes dolgozószobájában a zöld bársonnyal borított íróasztalon könyvek és kéziratok hevertek. Elemér, a fiatal nemes és gondolkodó, az ablaknál állt, és a pesti utcák lámpáit nézte a hűvös őszi alkonyatban."
            },
            {
                "type": "dialogue",
                "speaker": "A professzor",
                "text": "Kedves Elemér barátom, hetek óta látom rajtad a komor tépelődést. Egyrészt előtted áll a legfényesebb társadalmi jövő, másrészt úgy viselkedsz, mint aki súlyos terhet hordoz a lelkén. Mi gyötör ennyire?"
            },
            {
                "type": "dialogue",
                "speaker": "Tábory Elemér",
                "text": "Professzor úr, meglátásom szerint az emberi lélek nem egyetlen egyszerű valóság, hanem tele van feloldhatatlan ellentmondásokkal. Amikor ébren vagyok, művelt úrnak látnak az emberek; éjszakánként viszont egy szegény, megalázott asztaloslegényként élek a rémálmaimban."
            },
            {
                "type": "dialogue",
                "speaker": "A professzor",
                "text": "Bár az álmok kétségkívül élénkek és ijesztőek lehetnek, mégsem szabad összetévesztenünk a képzelet játékát a valóság szilárd tényeivel. A te életed itt zajlik, a valóságos világban."
            },
            {
                "type": "dialogue",
                "speaker": "Tábory Elemér",
                "text": "Nem állja meg a helyét az az egyszerű magyarázat, miszerint ez csupán lidérces álom! A másik világomban épp olyan valóságosnak érzem a szenvedést és a hideget, mint nappal a könyveim selymes lapjait. Ki tudja megmondani, melyik az igazi énem?"
            },
            {
                "type": "dialogue",
                "speaker": "A professzor",
                "text": "Mindent egybevetve elismerem, hogy az emberi elme mélyebb titkokat rejt, mint amit a tudomány eddig feltárt. De ha átadod magad ennek a kettősségnek, felőrlöd az erődet."
            },
            {
                "type": "narration",
                "text": "Elemér felsóhajtott, és leült az íróasztalhoz. Tudta, hogy bármilyen nehéz is a kettős lét rejtélye, meg kell küzdenie önmagáért. Az ember nem menekülhet a saját sorsa és a gondolatai elől: szembe kell néznie az igazság minden oldalával."
            }
        ]
    }
    write_json("content/hu/stories/classics/b1/b1-34-babits.json", story)

    # -------------------------------------------------------------------------
    # 4. Exercise Files (6 files, 7 exercises each = 42 exercises)
    # -------------------------------------------------------------------------
    # Lesson 01 Exercises
    ex_01 = {
        "lesson": "b1-34-01",
        "exercises": [
            {
                "id": "b1-34-01.ex01",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent az 'álláspont' kifejezés?",
                "options": [
                    "Valakinek a határozott nézőpontja vagy véleménye egy kérdésben",
                    "Egy vasútállomás hivatalos neve",
                    "A munkavállalók fizetési kategóriája"
                ],
                "correct": 0
            },
            {
                "id": "b1-34-01.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Azt gondolom, _____ a javaslat megvalósítható a gyakorlatban. (that - hogy)",
                "answer": "hogy"
            },
            {
                "id": "b1-34-01.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Úgy", "vélem,", "hogy", "a", "döntés", "helyes", "volt."],
                "solution": ["Úgy", "vélem,", "hogy", "a", "döntés", "helyes", "volt."]
            },
            {
                "id": "b1-34-01.ex04",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Melyik szó jelenti a gondolatok és érvek logikus kifejtését?",
                "options": [
                    "Érvelés",
                    "Követelés",
                    "Tiltakozás"
                ],
                "correct": 0
            },
            {
                "id": "b1-34-01.ex05",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Határozott_____ úgy vélem, hogy nem szabad feladnunk a terveinket. (definitely - an)",
                "answer": "an"
            },
            {
                "id": "b1-34-01.ex06",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Hogyan fejezzük ki, hogy csak bizonyos mértékben értünk egyet valakivel?",
                "options": [
                    "Részben egyetértek veled",
                    "Soha nem értek egyet veled",
                    "Mindenben tökéletesen egyetértek"
                ],
                "correct": 0
            },
            {
                "id": "b1-34-01.ex07",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "személyes", "meglátásom", "szerint", "változtatnunk", "kell."],
                "solution": ["A", "személyes", "meglátásom", "szerint", "változtatnunk", "kell."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-34-01-ex.json", ex_01)

    # Lesson 02 Exercises
    ex_02 = {
        "lesson": "b1-34-02",
        "exercises": [
            {
                "id": "b1-34-02.ex01",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik páros kifejezést használjuk két eltérő szempont összevetésére?",
                "options": [
                    "Egyrészt..., másrészt...",
                    "Vagy..., vagy...",
                    "Se nem..., se nem..."
                ],
                "correct": 0
            },
            {
                "id": "b1-34-02.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Egyrészt olcsó, másrészt _____ sokkal jobb a minősége. (however - viszont)",
                "answer": "viszont"
            },
            {
                "id": "b1-34-02.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Egyfelől", "értem,", "másfelől", "nem", "értek", "egyet."],
                "solution": ["Egyfelől", "értem,", "másfelől", "nem", "értek", "egyet."]
            },
            {
                "id": "b1-34-02.ex04",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent a 'mérlegelés' egy vita vagy döntés során?",
                "options": [
                    "A pro és kontra érvek alapos megfontolása",
                    "A csomagok súlyának ellenőrzése a postán",
                    "A határidők azonnali meghosszabbítása"
                ],
                "correct": 0
            },
            {
                "id": "b1-34-02.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "Minden fontos szempon_____ figyelembe kell vennünk a vitában. (aspect - tot)",
                "answer": "tot"
            },
            {
                "id": "b1-34-02.ex06",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik szó fejezi ki a választékos ellentétet ('by contrast')?",
                "options": [
                    "Ellenben",
                    "Tehát",
                    "Ráadásul"
                ],
                "correct": 0
            },
            {
                "id": "b1-34-02.ex07",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["Meg", "kell", "találnunk", "az", "egészséges", "egyensúlyt."],
                "solution": ["Meg", "kell", "találnunk", "az", "egészséges", "egyensúlyt."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-34-02-ex.json", ex_02)

    # Lesson 03 Exercises
    ex_03 = {
        "lesson": "b1-34-03",
        "exercises": [
            {
                "id": "b1-34-03.ex01",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik kötőszó fejezi ki a megengedést a mondatban?",
                "options": [
                    "Bár / Jóllehet",
                    "Mivel / Minthogy",
                    "Hacsak / Feltéve"
                ],
                "correct": 0
            },
            {
                "id": "b1-34-03.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Bár sok a nehézség, még_____ hiszek a sikerben. (still - is)",
                "answer": "is"
            },
            {
                "id": "b1-34-03.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Jóllehet", "nem", "könnyű,", "mégis", "megéri", "megpróbálni."],
                "solution": ["Jóllehet", "nem", "könnyű,", "mégis", "megéri", "megpróbálni."]
            },
            {
                "id": "b1-34-03.ex04",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent, ha valaki 'fenntartással' fogad egy hírt?",
                "options": [
                    "Nem hiszi el vakon, óvatos kételyei vannak",
                    "Azonnal megosztja a közösségi médiában",
                    "Teljesen figyelmen kívül hagyja"
                ],
                "correct": 0
            },
            {
                "id": "b1-34-03.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A szabály alól mindig akad egy-két kivé_____. (exception - tel)",
                "answer": "tel"
            },
            {
                "id": "b1-34-03.ex06",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Hogyan fejezzük ki a hivatalos feltételt: 'Insofar as'?",
                "options": [
                    "Amennyiben",
                    "Miután",
                    "Anélkül hogy"
                ],
                "correct": 0
            },
            {
                "id": "b1-34-03.ex07",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "gondolatok", "pontos", "árnyalása", "nagyon", "fontos."],
                "solution": ["A", "gondolatok", "pontos", "árnyalása", "nagyon", "fontos."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-34-03-ex.json", ex_03)

    # Lesson 04 Exercises
    ex_04 = {
        "lesson": "b1-34-04",
        "exercises": [
            {
                "id": "b1-34-04.ex01",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent az 'ellenérv' kifejezés?",
                "options": [
                    "Egy állítással szemben felhozott indok vagy érv",
                    "Egy orvosi gyógyszer ellenjavallata",
                    "A bírósági tárgyalás elnapolása"
                ],
                "correct": 0
            },
            {
                "id": "b1-34-04.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Ezzel szemben úgy tartom, hogy a tények mást mutat_____. (show - nak)",
                "answer": "nak"
            },
            {
                "id": "b1-34-04.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Nem", "állja", "meg", "a", "helyét", "a", "vád."],
                "solution": ["Nem", "állja", "meg", "a", "helyét", "a", "vád."]
            },
            {
                "id": "b1-34-04.ex04",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik kifejezés fejez ki megfellebbezhetetlen bizonyosságot?",
                "options": [
                    "Kétségkívül / Vitathatatlanul",
                    "Talán / Esetleg",
                    "Aligha / Kétlem"
                ],
                "correct": 0
            },
            {
                "id": "b1-34-04.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A vita során határozott meggyőződés_____ védte az álláspontját. (conviction - ével)",
                "answer": "ével"
            },
            {
                "id": "b1-34-04.ex06",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Melyik szó jelenti egy állítás téves voltának bemutatását?",
                "options": [
                    "Cáfolat",
                    "Jóváhagyás",
                    "Dicséret"
                ],
                "correct": 0
            },
            {
                "id": "b1-34-04.ex07",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Kétségkívül", "szükség", "van", "az", "alapos", "bizonyításra."],
                "solution": ["Kétségkívül", "szükség", "van", "az", "alapos", "bizonyításra."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-34-04-ex.json", ex_04)

    # Lesson 05 Exercises
    ex_05 = {
        "lesson": "b1-34-05",
        "exercises": [
            {
                "id": "b1-34-05.ex01",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Melyik kifejezéssel kezdhetünk elegáns összegzést egy vita végén?",
                "options": [
                    "Mindent egybevetve",
                    "Mindennek ellenére tilos",
                    "Hirtelen felindulásból"
                ],
                "correct": 0
            },
            {
                "id": "b1-34-05.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A fentiek tükré_____ a javaslat elfogadása indokolt. (light of - ben)",
                "answer": "ben"
            },
            {
                "id": "b1-34-05.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Mindent", "egybevetve", "sikeresnek", "mondható", "a", "tárgyalás."],
                "solution": ["Mindent", "egybevetve", "sikeresnek", "mondható", "a", "tárgyalás."]
            },
            {
                "id": "b1-34-05.ex04",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent a 'kompromisszum'?",
                "options": [
                    "Megegyezés, amelyben mindkét fél engedményeket tesz",
                    "Az egyik fél teljes és feltétel nélküli győzelme",
                    "A tárgyalások megszakítása vita nélkül"
                ],
                "correct": 0
            },
            {
                "id": "b1-34-05.ex05",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Meglátásom _____ a helyzet gyorsan javulni fog. (in my view - szerint)",
                "answer": "szerint"
            },
            {
                "id": "b1-34-05.ex06",
                "type": "multiple-choice",
                "category": "literature",
                "question": "Kivel vív belső küzdelmet Tábory Elemér Babits regényében?",
                "options": [
                    "A saját éjszakai rémálmaiban élő másik énjével",
                    "Egy idegen hadsereg katonájával",
                    "A királyi udvar kancellárjával"
                ],
                "correct": 0
            },
            {
                "id": "b1-34-05.ex07",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "vita", "végkövetkeztetése", "mindenki", "számára", "tanulságos", "volt."],
                "solution": ["A", "vita", "végkövetkeztetése", "mindenki", "számára", "tanulságos", "volt."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-34-05-ex.json", ex_05)

    # Consolidation Exercises
    ex_consolidation = {
        "lesson": "b1-34-consolidation",
        "exercises": [
            {
                "id": "b1-34-consolidation.ex01",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik mondat fejez ki árnyalt, kiegyensúlyozott véleményt?",
                "options": [
                    "Egyfelől megértem az aggodalmakat, másfelől bízom a szakértők munkájában.",
                    "Senkinek sincs igaza, és nem is érdekel a dolog.",
                    "Azonnal meg kell tiltani mindent kivétel nélkül."
                ],
                "correct": 0
            },
            {
                "id": "b1-34-consolidation.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Bár voltak viták, még_____ sikerült kompromisszumot kötni. (still - is)",
                "answer": "is"
            },
            {
                "id": "b1-34-consolidation.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Meglátásom", "szerint", "fontos", "az", "érvek", "mérlegelése."],
                "solution": ["Meglátásom", "szerint", "fontos", "az", "érvek", "mérlegelése."]
            },
            {
                "id": "b1-34-consolidation.ex04",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit fejez ki a 'tanulság' szó?",
                "options": [
                    "Egy tapasztalatból vagy történetből levont bölcsességet és okulást",
                    "Egy iskolai tanóra hivatalos időtartamát",
                    "A bizonyítványban szereplő érdemjegyeket"
                ],
                "correct": 0
            },
            {
                "id": "b1-34-consolidation.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A vitában elhangzott ellenérv_____ alaposan meg kell vizsgálnunk. (counter-arguments - eket)",
                "answer": "eket"
            },
            {
                "id": "b1-34-consolidation.ex06",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik állítás helytálló a 'nem állja meg a helyét' kifejezésről?",
                "options": [
                    "Azt jelenti, hogy az adott állítás alaptalan és megalapozatlan",
                    "Azt jelenti, hogy valaki nem tud felállni a székéből",
                    "Azt jelenti, hogy a helyszín nem megfelelő egy rendezvényhez"
                ],
                "correct": 0
            },
            {
                "id": "b1-34-consolidation.ex07",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Mindent", "egybevetve", "indokolt", "a", "fenntartások", "kezelése."],
                "solution": ["Mindent", "egybevetve", "indokolt", "a", "fenntartások", "kezelése."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-34-consolidation-ex.json", ex_consolidation)

    # -------------------------------------------------------------------------
    # 5. Lesson Files (6 files)
    # -------------------------------------------------------------------------
    lesson_01 = {
        "id": "lesson.b1.34-01",
        "unit": 34,
        "title": "Azt gondolom, hogy... mert... (Nested Opinion Clauses)",
        "level": "B1",
        "grammar": "Nested Opinion Matrices & Degree Modifiers in Hungarian",
        "sections": [
            {
                "type": "goal",
                "title": "Lesson Goals",
                "items": [
                    "I can construct multi-level nested opinion clauses with explanatory conjunctions.",
                    "I can calibrate my degree of agreement using nuance adverbs like határozottan and részben.",
                    "I can master 4 core vocabulary terms for intellectual viewpoints.",
                    "I can state well-grounded personal opinions with confidence."
                ]
            },
            {"type": "recycle", "count": 3},
            {"type": "vocabulary", "ref": "vocabulary/b1/b1-34-01-voc.json"},
            {"type": "grammar", "ref": "grammar/b1/b1-34-01-a-gr.json"},
            {"type": "grammar", "ref": "grammar/b1/b1-34-01-b-gr.json"},
            {
                "type": "exercise-group",
                "title": "Practice",
                "ref": "exercises/b1/b1-34-01-ex.json",
                "exerciseRefs": [
                    "b1-34-01.ex01",
                    "b1-34-01.ex02",
                    "b1-34-01.ex03",
                    "b1-34-01.ex04",
                    "b1-34-01.ex05",
                    "b1-34-01.ex06",
                    "b1-34-01.ex07"
                ]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-34-01.json", lesson_01)

    lesson_02 = {
        "id": "lesson.b1.34-02",
        "unit": 34,
        "title": "Egyrészről..., másrészről... (On the One Hand, On the Other)",
        "level": "B1",
        "grammar": "Correlative Balancing and Contrastive Connectors (viszont, ellenben)",
        "sections": [
            {
                "type": "goal",
                "title": "Lesson Goals",
                "items": [
                    "I can balance competing perspectives using egyrészt... másrészt...",
                    "I can contrast differing viewpoints using formal connectors like ellenben and viszont.",
                    "I can acquire 4 vocabulary terms for deliberation and balance.",
                    "I can conduct fair-minded comparative assessments in Hungarian."
                ]
            },
            {"type": "recycle", "count": 3},
            {"type": "vocabulary", "ref": "vocabulary/b1/b1-34-02-voc.json"},
            {"type": "grammar", "ref": "grammar/b1/b1-34-02-a-gr.json"},
            {"type": "grammar", "ref": "grammar/b1/b1-34-02-b-gr.json"},
            {
                "type": "exercise-group",
                "title": "Practice",
                "ref": "exercises/b1/b1-34-02-ex.json",
                "exerciseRefs": [
                    "b1-34-02.ex01",
                    "b1-34-02.ex02",
                    "b1-34-02.ex03",
                    "b1-34-02.ex04",
                    "b1-34-02.ex05",
                    "b1-34-02.ex06",
                    "b1-34-02.ex07"
                ]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-34-02.json", lesson_02)

    lesson_03 = {
        "id": "lesson.b1.34-03",
        "unit": 34,
        "title": "Árnyalás és feltételek (Nuance & Qualification)",
        "level": "B1",
        "grammar": "Concessive Opinion Structures (bár... mégis) & Stipulations (amennyiben)",
        "sections": [
            {
                "type": "goal",
                "title": "Lesson Goals",
                "items": [
                    "I can concede points gracefully using bár... mégis and jóllehet.",
                    "I can qualify opinions by attaching conditions with azzal a fenntartással and amennyiben.",
                    "I can use 4 vocabulary terms for qualifications and reservations.",
                    "I can articulate nuanced positions that avoid simplistic black-and-white claims."
                ]
            },
            {"type": "recycle", "count": 3},
            {"type": "vocabulary", "ref": "vocabulary/b1/b1-34-03-voc.json"},
            {"type": "grammar", "ref": "grammar/b1/b1-34-03-a-gr.json"},
            {"type": "grammar", "ref": "grammar/b1/b1-34-03-b-gr.json"},
            {
                "type": "exercise-group",
                "title": "Practice",
                "ref": "exercises/b1/b1-34-03-ex.json",
                "exerciseRefs": [
                    "b1-34-03.ex01",
                    "b1-34-03.ex02",
                    "b1-34-03.ex03",
                    "b1-34-03.ex04",
                    "b1-34-03.ex05",
                    "b1-34-03.ex06",
                    "b1-34-03.ex07"
                ]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-34-03.json", lesson_03)

    lesson_04 = {
        "id": "lesson.b1.34-04",
        "unit": 34,
        "title": "Álláspont védelme és cáfolat (Defending a Position)",
        "level": "B1",
        "grammar": "Refuting Opposing Claims & Epistemic Reinforcement (kétségkívül)",
        "sections": [
            {
                "type": "goal",
                "title": "Lesson Goals",
                "items": [
                    "I can rebut ungrounded claims using nem állja meg a helyét.",
                    "I can reinforce my arguments with certainty disjuncts like kétségkívül and vitathatatlanul.",
                    "I can deploy 4 terms for counterarguments and proof.",
                    "I can defend my perspective in a structured debate."
                ]
            },
            {"type": "recycle", "count": 3},
            {"type": "vocabulary", "ref": "vocabulary/b1/b1-34-04-voc.json"},
            {"type": "grammar", "ref": "grammar/b1/b1-34-04-a-gr.json"},
            {"type": "grammar", "ref": "grammar/b1/b1-34-04-b-gr.json"},
            {
                "type": "exercise-group",
                "title": "Practice",
                "ref": "exercises/b1/b1-34-04-ex.json",
                "exerciseRefs": [
                    "b1-34-04.ex01",
                    "b1-34-04.ex02",
                    "b1-34-04.ex03",
                    "b1-34-04.ex04",
                    "b1-34-04.ex05",
                    "b1-34-04.ex06",
                    "b1-34-04.ex07"
                ]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-34-04.json", lesson_04)

    lesson_05 = {
        "id": "lesson.b1.34-05",
        "unit": 34,
        "title": "Kiegyensúlyozott összegzés (A Balanced Opinion: Babits Mihály)",
        "level": "B1",
        "grammar": "Synthesizing Idioms (mindent egybevetve) & Pragmatic Hedges",
        "sections": [
            {
                "type": "goal",
                "title": "Lesson Goals",
                "items": [
                    "I can summarize complex arguments using mindent egybevetve and a fentiek tükrében.",
                    "I can soften statements with pragmatic hedging formulas like meglátásom szerint.",
                    "I can learn 4 words for synthesis, compromise, and moral conclusions.",
                    "I can read and analyze an adaptation of Babits Mihály's psychological masterpiece A gólyakalifa."
                ]
            },
            {"type": "recycle", "count": 3},
            {"type": "vocabulary", "ref": "vocabulary/b1/b1-34-05-voc.json"},
            {"type": "grammar", "ref": "grammar/b1/b1-34-05-a-gr.json"},
            {"type": "grammar", "ref": "grammar/b1/b1-34-05-b-gr.json"},
            {"type": "story", "ref": "stories/classics/b1/b1-34-babits.json"},
            {
                "type": "exercise-group",
                "title": "Practice",
                "ref": "exercises/b1/b1-34-05-ex.json",
                "exerciseRefs": [
                    "b1-34-05.ex01",
                    "b1-34-05.ex02",
                    "b1-34-05.ex03",
                    "b1-34-05.ex04",
                    "b1-34-05.ex05",
                    "b1-34-05.ex06",
                    "b1-34-05.ex07"
                ]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-34-05.json", lesson_05)

    lesson_consolidation = {
        "id": "lesson.b1.34-consolidation",
        "unit": 34,
        "title": "Összegzés és gyakorlás: Összetett vélemények (Consolidation)",
        "level": "B1",
        "grammar": "Review of complex opinion formulation, counterarguments, and synthesis",
        "sections": [
            {
                "type": "goal",
                "title": "Consolidation Goals",
                "items": [
                    "Review all 20 vocabulary items for advanced argumentation and perspective.",
                    "Synthesize nested opinion clauses, concession structures, and epistemic reinforcement.",
                    "Confirm mastery of balancing counter-arguments with fair-minded deliberation.",
                    "Demonstrate readiness for expressing nuanced B1-level discourse."
                ]
            },
            {
                "type": "exercise-group",
                "title": "Consolidation Practice",
                "ref": "exercises/b1/b1-34-consolidation-ex.json",
                "exerciseRefs": [
                    "b1-34-consolidation.ex01",
                    "b1-34-consolidation.ex02",
                    "b1-34-consolidation.ex03",
                    "b1-34-consolidation.ex04",
                    "b1-34-consolidation.ex05",
                    "b1-34-consolidation.ex06",
                    "b1-34-consolidation.ex07"
                ]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-34-consolidation.json", lesson_consolidation)

if __name__ == "__main__":
    build_unit_34_core()
