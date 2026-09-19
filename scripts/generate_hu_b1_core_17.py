#!/usr/bin/env python3
"""Generate Hungarian B1 Core Unit 17: Society & Inequality (b1-17)."""

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

def build_unit_17_core():
    # -------------------------------------------------------------------------
    # 1. Vocabulary Files (4 words each = 20 words total)
    # -------------------------------------------------------------------------
    voc_01 = {
        "id": "vocab.b1.17.01",
        "lesson": "b1-17-01",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "társadalmi réteg", "translation": "social stratum, social class", "pos": "noun"},
            {"lemma": "jövedelmi különbség", "translation": "income disparity, wage gap", "pos": "noun"},
            {"lemma": "életszínvonal", "translation": "standard of living", "pos": "noun"},
            {"lemma": "szegénységi küszöb", "translation": "poverty threshold, poverty line", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-17-01-voc.json", voc_01)

    voc_02 = {
        "id": "vocab.b1.17.02",
        "lesson": "b1-17-02",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "esélyegyenlőség", "translation": "equal opportunity", "pos": "noun"},
            {"lemma": "hátrányos helyzet", "translation": "disadvantaged situation, handicap", "pos": "noun"},
            {"lemma": "társadalmi mobilitás", "translation": "social mobility", "pos": "noun"},
            {"lemma": "munkanélküliség", "translation": "unemployment", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-17-02-voc.json", voc_02)

    voc_03 = {
        "id": "vocab.b1.17.03",
        "lesson": "b1-17-03",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "méltányosság", "translation": "fairness, equity", "pos": "noun"},
            {"lemma": "igazságtalanság", "translation": "injustice, unfairness", "pos": "noun"},
            {"lemma": "társadalmi szolidaritás", "translation": "social solidarity", "pos": "noun"},
            {"lemma": "segélyezés", "translation": "social assistance, welfare aid", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-17-03-voc.json", voc_03)

    voc_04 = {
        "id": "vocab.b1.17.04",
        "lesson": "b1-17-04",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "közoktatás", "translation": "public education system", "pos": "noun"},
            {"lemma": "felzárkózás", "translation": "catching up, social integration", "pos": "noun"},
            {"lemma": "civil szervezet", "translation": "non-governmental organization (NGO)", "pos": "noun"},
            {"lemma": "önkéntes munka", "translation": "voluntary work, volunteering", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-17-04-voc.json", voc_04)

    voc_05 = {
        "id": "vocab.b1.17.05",
        "lesson": "b1-17-05",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "együttélés", "translation": "peaceful coexistence", "pos": "noun"},
            {"lemma": "társadalmi párbeszéd", "translation": "social dialogue", "pos": "noun"},
            {"lemma": "emberi méltóság", "translation": "human dignity", "pos": "noun"},
            {"lemma": "jövőkép", "translation": "vision for the future, outlook", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-17-05-voc.json", voc_05)

    # -------------------------------------------------------------------------
    # 2. Grammar Files
    # -------------------------------------------------------------------------
    gr_01_a = {
        "id": "grammar.b1.17.01.essive-formal-kent",
        "title": "The Essive-Formal Case Suffix: -ként ('as, in the capacity of')",
        "sections": [
            {
                "type": "text",
                "title": "Function and Usage of -ként",
                "content": "The suffix *-ként* expresses role, capacity, or form ('as / in the capacity of / like'): *tanárként dolgozik* ('works as a teacher'), *példaként említi* ('mentions as an example'). Unlike *-ul/-ül*, *-ként* attaches without vowel harmony changes directly to stems."
            },
            {
                "type": "examples",
                "title": "Examples with -ként",
                "items": [
                    {
                        "spanish": "Állampolgárként mindannyian felelősek vagyunk a közösségünkért.",
                        "english": "As citizens, we are all responsible for our community."
                    },
                    {
                        "spanish": "Ezt a kérdést nem egyéni, hanem társadalmi problémaként kell kezelni.",
                        "english": "This issue must be treated not as an individual but as a social problem."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-17-01-a-gr.json", gr_01_a)

    gr_01_b = {
        "id": "grammar.b1.17.01.kent-vs-mint",
        "title": "Distinction Between -ként and mint",
        "sections": [
            {
                "type": "text",
                "title": "Comparison vs Capacity: mint vs -ként",
                "content": "While *mint* is often used with nominative or inflected nouns (*úgy él, mint egy király* - 'lives like a king'), *-ként* strictly designates function or role (*vezetőként hozott döntést* - 'made a decision as a leader')."
            },
            {
                "type": "examples",
                "title": "Contrasting mint and -ként",
                "items": [
                    {
                        "spanish": "Önkéntesként segített a rászoruló családoknak a faluban.",
                        "english": "As a volunteer he helped families in need in the village."
                    },
                    {
                        "spanish": "Úgy viselkedett, mint aki pontosan ismeri a szabályokat.",
                        "english": "He behaved like someone who knows the rules precisely."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-17-01-b-gr.json", gr_01_b)

    gr_02_a = {
        "id": "grammar.b1.17.02.distributive-nkent",
        "title": "The Distributive Suffix: -nként ('per, by, at intervals')",
        "sections": [
            {
                "type": "text",
                "title": "Expressing Distribution and Regular Frequencies",
                "content": "The suffix *-nként* (or *-anként / -enként / -onként*) indicates distribution per unit or intervals: *fejenként* ('per head / per person'), *havonta / havonként* ('monthly / per month'), *csoportonként* ('by group')."
            },
            {
                "type": "examples",
                "title": "Distributive forms in social statistics",
                "items": [
                    {
                        "spanish": "A támogatást családonként és fejenként számolják ki.",
                        "english": "The support is calculated per family and per head."
                    },
                    {
                        "spanish": "Évente többször szerveznek képzéseket a hátrányos helyzetű fiataloknak.",
                        "english": "Several times a year they organize training sessions for disadvantaged youth."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-17-02-a-gr.json", gr_02_a)

    gr_02_b = {
        "id": "grammar.b1.17.02.contrast-mig-ezzel-szemben",
        "title": "Contrastive Connectors: míg, ezzel szemben, ezzel ellentétben",
        "sections": [
            {
                "type": "text",
                "title": "Highlighting Social Contrasts",
                "content": "To compare two differing realities, use *míg* ('while / whereas') and *ezzel szemben* ('by contrast / in contrast to this'): *A nagyvárosokban több a lehetőség, míg a kistelepüléseken nehezebb a munkahelyteremtés.*"
            },
            {
                "type": "examples",
                "title": "Contrasting social realities",
                "items": [
                    {
                        "spanish": "Egyes rétegek jövedelme növekszik, míg mások a megélhetésért küzdenek.",
                        "english": "The income of certain strata is increasing, while others struggle to make ends meet."
                    },
                    {
                        "spanish": "A fejlett régiókban alacsony a munkanélküliség, ezzel szemben vidéken hiányoznak a munkahelyek.",
                        "english": "In developed regions unemployment is low; in contrast, jobs are lacking in rural areas."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-17-02-b-gr.json", gr_02_b)

    gr_03_a = {
        "id": "grammar.b1.17.03.evaluative-justice",
        "title": "Evaluative Language: igazságos, méltányos, elfogadhatatlan",
        "sections": [
            {
                "type": "text",
                "title": "Judging Fairness and Equity",
                "content": "Discussing social justice involves evaluative predicate adjectives followed by *hogy*: *Igazságos, hogy minden gyermek jó oktatást kapjon.* ('It is fair that every child receive a good education.'). Negative judgments often use *elfogadhatatlan* ('unacceptable')."
            },
            {
                "type": "examples",
                "title": "Evaluating justice",
                "items": [
                    {
                        "spanish": "Nem tartom méltányosnak, hogy a lakhatási költségek ilyen gyorsan emelkednek.",
                        "english": "I do not consider it equitable that housing costs rise so rapidly."
                    },
                    {
                        "spanish": "Elengedhetetlen, hogy a rászorulók megfelelő társadalmi szolidaritást kapjanak.",
                        "english": "It is indispensable that those in need receive appropriate social solidarity."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-17-03-a-gr.json", gr_03_a)

    gr_03_b = {
        "id": "grammar.b1.17.03.passive-reflexive-reszul",
        "title": "Expressing Beneficiaries: részesül vmiben, juttat vmit",
        "sections": [
            {
                "type": "text",
                "title": "Verbs of Allocation and Entitlement",
                "content": "Official welfare descriptions use *részesül vmiben* ('receives / benefits from'): *segélyben részesül* ('receives welfare aid'), *ösztöndíjban részesül* ('receives a scholarship')."
            },
            {
                "type": "examples",
                "title": "Allocation verbs in context",
                "items": [
                    {
                        "spanish": "Több ezer rászoruló gyermek részesül ingyenes iskolai étkezésben.",
                        "english": "Several thousand needy children benefit from free school meals."
                    },
                    {
                        "spanish": "A program célja, hogy minden tehetséges fiatal megfelelő képzésben részesüljön.",
                        "english": "The goal of the program is that every talented youth receive appropriate training."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-17-03-b-gr.json", gr_03_b)

    gr_04_a = {
        "id": "grammar.b1.17.04.complex-relatives",
        "title": "Chained Relative Clauses: azok a szervezetek, amelyek...",
        "sections": [
            {
                "type": "text",
                "title": "Defining Social Initiatives with Relative Clauses",
                "content": "To specify civil actors and groups, use demonstrative + relative pairings: *azok az emberek, akik...* ('those people who...'), *olyan kezdeményezések, amelyek...* ('initiatives that...')."
            },
            {
                "type": "examples",
                "title": "Relative clauses in civic topics",
                "items": [
                    {
                        "spanish": "Azok a civil szervezetek végeznek értékes munkát, amelyek közvetlenül a közösségekben segítenek.",
                        "english": "Those civil organizations do valuable work which help directly within communities."
                    },
                    {
                        "spanish": "Olyan programokra van szükség, amelyek hosszú távon biztosítják a felzárkózást.",
                        "english": "Programs are needed which ensure social integration over the long term."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-17-04-a-gr.json", gr_04_a)

    gr_04_b = {
        "id": "grammar.b1.17.04.participle-descriptions",
        "title": "Present Participle as Attributive Adjective: segítő, támogató",
        "sections": [
            {
                "type": "text",
                "title": "Using -ó/-ő Participles for Roles",
                "content": "Hungarian frequently forms role descriptions with the active present participle: *a rászoruló emberek* ('needy people'), *támogató közösség* ('supportive community'), *felzárkóztató program* ('catch-up / integration program')."
            },
            {
                "type": "examples",
                "title": "Participles in social context",
                "items": [
                    {
                        "spanish": "A civil szféra támogató kezet nyújt a nehéz sorsú embertársainknak.",
                        "english": "The civil sphere extends a supportive hand to our fellow humans in hard circumstances."
                    },
                    {
                        "spanish": "Az önkéntes munkát végző fiatalok példát mutatnak az egész társadalomnak.",
                        "english": "Youth doing volunteer work set an example for the whole of society."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-17-04-b-gr.json", gr_04_b)

    gr_05_a = {
        "id": "grammar.b1.17.05.respectful-discourse",
        "title": "Nuanced Stance-Taking: Meggyőződésem szerint, Úgy látom...",
        "sections": [
            {
                "type": "text",
                "title": "Expressing Standpoints in Sensitive Debates",
                "content": "To voice positions on inequality politely and persuasively: *Úgy látom, hogy...* ('As I see it...'), *Véleményem szerint elengedhetetlen...* ('In my view it is indispensable...'), *Nem szabad figyelmen kívül hagynunk...* ('We must not ignore...')."
            },
            {
                "type": "examples",
                "title": "Expressing standpoints",
                "items": [
                    {
                        "spanish": "Úgy látom, hogy az emberi méltóság tisztelete a békés együttélés alapja.",
                        "english": "As I see it, respect for human dignity is the foundation of peaceful coexistence."
                    },
                    {
                        "spanish": "Meggyőződésem, hogy a valódi társadalmi párbeszéd nélkül nem építhetünk stabil jövőt.",
                        "english": "I am convinced that without genuine social dialogue we cannot build a stable future."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-17-05-a-gr.json", gr_05_a)

    gr_05_b = {
        "id": "grammar.b1.17.05.subordinate-hope-cl",
        "title": "Subjunctive of Hope and Shared Future: Bízom benne, hogy...",
        "sections": [
            {
                "type": "text",
                "title": "Formulating Hopes for Society",
                "content": "To express collective aspirations: *Bízom benne, hogy a jövő generációi egyenlőbb esélyeket kapnak.* ('I trust that future generations will receive more equal chances.')."
            },
            {
                "type": "examples",
                "title": "Hopes for future society",
                "items": [
                    {
                        "spanish": "Bízom abban, hogy a közös erőfeszítések meghozzák a várt eredményt.",
                        "english": "I trust that joint efforts will bring the expected result."
                    },
                    {
                        "spanish": "Remélem, hogy a társadalmi mobilitás minden tehetséges fiatal számára elérhető lesz.",
                        "english": "I hope that social mobility will be accessible for every talented young person."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-17-05-b-gr.json", gr_05_b)

    # -------------------------------------------------------------------------
    # 3. Exercise Files
    # -------------------------------------------------------------------------
    for i in range(1, 6):
        padded = f"0{i}"
        curr_voc = [voc_01, voc_02, voc_03, voc_04, voc_05][i-1]
        ex_data = {
            "lesson": f"b1-17-{padded}",
            "exercises": [
                {
                    "id": f"b1-17-{padded}.ex01",
                    "type": "matching",
                    "category": "vocabulary",
                    "pairs": [[w["lemma"], w["translation"]] for w in curr_voc["words"]]
                },
                {
                    "id": f"b1-17-{padded}.ex02",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "question": f"Melyik mondat használja helyesen a -ként vagy -nként ragot? (Lesson {i})",
                    "options": [
                        "Állampolgárként mindannyiunknak felelőssége van a közösségért.",
                        "Állampolgármint mindannyiunknak van felelősség.",
                        "Állampolgárnak lenni mindannyian felelősség van."
                    ],
                    "correct": 0
                },
                {
                    "id": f"b1-17-{padded}.ex03",
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "sentence": "A társadalomban fontos cél a hátrányos helyzetű családok támogatása és az _____ biztosítása. (equal opportunities)",
                    "answer": "esélyegyenlőség"
                },
                {
                    "id": f"b1-17-{padded}.ex04",
                    "type": "fill-blank",
                    "category": "grammar",
                    "sentence": "Példa____ említette azokat a szervezeteket, amelyek rászorulóknak segítenek. (as a / by way of)",
                    "answer": "ként"
                },
                {
                    "id": f"b1-17-{padded}.ex05",
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "question": "Mit jelent az esélyegyenlőség kifejezés?",
                    "options": [
                        "Azt, hogy mindenki egyenlő esélyekkel indulhat az oktatásban és a munkában.",
                        "Hogy minden ember pontosan ugyanolyan ruhát kénytelen hordani.",
                        "Hogy senki sem tanulhat tovább az alapiskola után."
                    ],
                    "correct": 0
                },
                {
                    "id": f"b1-17-{padded}.ex06",
                    "type": "fill-blank",
                    "category": "grammar",
                    "sentence": "A felmérést havi rendszerességgel, hónapok____ végzik el a szakemberek. (per month)",
                    "answer": "onként"
                },
                {
                    "id": f"b1-17-{padded}.ex07",
                    "type": "sentence-builder",
                    "category": "grammar",
                    "tiles": ["Az", "emberi", "méltóság", "tisztelete", "a", "békés", "és", "igazságos", "együttélés", "alapköve."],
                    "solution": ["Az", "emberi", "méltóság", "tisztelete", "a", "békés", "és", "igazságos", "együttélés", "alapköve."]
                },
                {
                    "id": f"b1-17-{padded}.ex08",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "Milyen szerepet játszanak a civil szervezetek a társadalomban?",
                    "options": [
                        "Közvetlen segítséget nyújtanak és erősítik a társadalmi szolidaritást.",
                        "Csak adókat szednek be a lakosságtól az állam nevében.",
                        "Megtiltják a polgároknak az önkéntes segítségnyújtást."
                    ],
                    "correct": 0
                }
            ]
        }
        write_json(f"content/hu/exercises/b1/b1-17-{padded}-ex.json", ex_data)

    # Consolidation exercises
    ex_consolidation = {
        "lesson": "b1-17-consolidation",
        "exercises": [
            {
                "id": "b1-17-consolidation.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["társadalmi réteg", "social stratum"],
                    ["esélyegyenlőség", "equal opportunity"],
                    ["méltányosság", "fairness, equity"],
                    ["emberi méltóság", "human dignity"]
                ]
            },
            {
                "id": "b1-17-consolidation.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik mondat fejezi ki helyesen a társadalmi felelősségvállalást?",
                "options": [
                    "Önkéntesként segítve az ember felismeri a közösségi szolidaritás valódi erejét.",
                    "Önkéntesként segíteni ember felismerni volt erő.",
                    "Mivel önkéntes ember ezért nem segít senkinek."
                ],
                "correct": 0
            },
            {
                "id": "b1-17-consolidation.ex03",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A jövedelmi különbségek csökkentése érdekében kulcsfontosságú a minőségi ____ fejlesztése. (public education)",
                "answer": "közoktatás"
            },
            {
                "id": "b1-17-consolidation.ex04",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A támogatást a rászorulók számára fejen____ osztják szét. (per head)",
                "answer": "ként"
            },
            {
                "id": "b1-17-consolidation.ex05",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "társadalmi", "mobilitás", "elősegíti", "a", "tehetséges", "fiatalok", "felemelkedését."],
                "solution": ["A", "társadalmi", "mobilitás", "elősegíti", "a", "tehetséges", "fiatalok", "felemelkedését."]
            },
            {
                "id": "b1-17-consolidation.ex06",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent az önkéntes munka kifejezés?",
                "options": [
                    "Olyan segítő tevékenységet, amelyet valaki anyagi ellenszolgáltatás nélkül, szabad akaratából végez a közösségért.",
                    "Kényszermunkát, amit kötelezően elrendel a hatóság.",
                    "Egy vállalat napi irodai fizetett túlóráját."
                ],
                "correct": 0
            },
            {
                "id": "b1-17-consolidation.ex07",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A békés társadalom alapja a kölcsönös tisztelet és a párbeszéd az emberek ____. (between)",
                "answer": "között"
            },
            {
                "id": "b1-17-consolidation.ex08",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Miről tanúskodik Móricz Zsigmond adaptációja a szegénységről és emberségről?",
                "options": [
                    "Arról, hogy a legnehezebb körülmények között is a szeretet és az emberi méltóság a legfőbb érték.",
                    "Hogy a pénz hiánya teljesen elpusztítja a családi összetartozást.",
                    "Egy gazdag kereskedő sikeres tőzsdei befektetéséről."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-17-consolidation-ex.json", ex_consolidation)

    # -------------------------------------------------------------------------
    # 4. Classic Story Adaptation for Lesson 5 / Consolidation
    # -------------------------------------------------------------------------
    story_classic = {
        "id": "story.b1.17.classic",
        "title": "A fillér értéke és az emberség",
        "level": "B1",
        "order": 17,
        "type": "classics",
        "estimatedMinutes": 7,
        "summary": "An adaptation from Zsigmond Móricz's heart-rending stories of social realism ('Hét krajcár'). In a small, modest home, a mother and her young son search every corner for seven lost pennies to buy soap to wash clothes, turning hardship into a moment of pure laughter, solidarity, and indestructible human dignity.",
        "characters": [
            "Az édesanya",
            "A kisfiú"
        ],
        "location": "Alföldi kis házikó",
        "author": "Móricz Zsigmond",
        "work": "Hét krajcár",
        "paragraphs": [
            {
                "type": "narration",
                "text": "A kis szobában hideg szél fújt be az ablakréseken, ám bent meleg fény áradt az édesanya mosolyából. Szappanra volt szükség, hogy a kimosott ruhák tiszták legyenek, de a pénztárca üresen feküdt az asztalon."
            },
            {
                "type": "dialogue",
                "speaker": "Az édesanya",
                "text": "Gyere, kisfiam! Keressük meg a házban a hét krajcárt! Ha elég vidáman kutatunk, a krajcárok is előbújnak a rejtett zugokból!"
            },
            {
                "type": "narration",
                "text": "A kisfiú boldogan nevetett, és négykézláb kezdte átkutatni a sublótfiókokat és a sarokba állított ládát. Az anya minden előkerülő fillérnél úgy ujjongott, mintha kincset találtak volna."
            },
            {
                "type": "dialogue",
                "speaker": "A kisfiú",
                "text": "Édesanyám, nézze! A varródoboz mélyén találtam egy fényes krajcárt! Már csak kettő hiányzik a szappan árához!"
            },
            {
                "type": "narration",
                "text": "Kacagásuk betöltötte az egész szobát. Bár a szegénység nehéz terhet rótt rájuk, a szeretet és a játékos kitartás erősebb volt minden anyagi hiánynál."
            },
            {
                "type": "dialogue",
                "speaker": "Az édesanya",
                "text": "Látod, fiam? A pénz elfogyhat, de a becsület és a vidám szív soha. Aki nevetni tud a bajban, az nem szegény, hanem a leggazdagabb ember a világon."
            },
            {
                "type": "narration",
                "text": "Délután egy koldus kopogtatott az ablakon, kenyeret kérve. Az anya az összegyűjtött utolsó krajcárt gondolkodás nélkül a rászoruló tenyerébe tette."
            },
            {
                "type": "dialogue",
                "speaker": "Az édesanya",
                "text": "Mi még fiatalok vagyunk és bírunk dolgozni. Akinek kevesebb jutott, azon kötelességünk segíteni."
            }
        ]
    }
    write_json("content/hu/stories/classics/b1/b1-17-moricz.json", story_classic)

    # -------------------------------------------------------------------------
    # 5. Lesson Files (01 to 05 + consolidation)
    # -------------------------------------------------------------------------
    for i in range(1, 6):
        padded = f"0{i}"
        titles = {
            "01": ("Talked About As...", "Társadalmi rétegek és jövedelmi különbségek"),
            "02": ("Different Groups, Different Lives", "Esélyegyenlőség és társadalmi mobilitás"),
            "03": ("Fair & Unfair", "Méltányosság, szolidaritás és segélyezés"),
            "04": ("A Social Issue, Explained", "Közoktatás, felzárkózás és civil munka"),
            "05": ("Where I Stand", "Együttélés, emberi méltóság és a jövőkép")
        }
        en_title, hu_title = titles[padded]
        lesson_data = {
            "id": f"lesson.b1.17-{padded}",
            "unit": 17,
            "title": en_title,
            "level": "B1",
            "grammar": "Essive-Formal -ként & Distributive -nként in Social Discourse",
            "goal": [
                f"I can understand and use vocabulary for {en_title.lower()}.",
                "I can use the essive-formal suffix -ként and distributive -nként in Hungarian.",
                "I can discuss social issues, equality of opportunity, and solidarity.",
                "I can master four new target vocabulary items in authentic context."
            ],
            "sections": [
                {
                    "type": "goal",
                    "title": "Lesson Goals",
                    "items": [
                        f"I can understand and use vocabulary for {en_title.lower()}.",
                        "I can use the essive-formal suffix -ként and distributive -nként in Hungarian.",
                        "I can discuss social issues, equality of opportunity, and solidarity.",
                        "I can master four new target vocabulary items in authentic context."
                    ]
                },
                {"type": "recycle", "title": "Quick Review"},
                {"type": "grammar", "ref": f"grammar/b1/b1-17-{padded}-a-gr.json"},
                {"type": "grammar", "ref": f"grammar/b1/b1-17-{padded}-b-gr.json"},
                {"type": "vocabulary", "title": "Lesson Vocabulary", "ref": f"vocabulary/b1/b1-17-{padded}-voc.json"},
                {
                    "type": "exercise-group",
                    "title": "Practice",
                    "ref": f"exercises/b1/b1-17-{padded}-ex.json",
                    "exerciseRefs": [f"b1-17-{padded}.ex0{k}" for k in range(1, 9)]
                }
            ]
        }
        write_json(f"content/hu/lessons/b1/b1-17-{padded}.json", lesson_data)

    consolidation_data = {
        "id": "lesson.b1.17-consolidation",
        "unit": 17,
        "title": "Unit 17 Consolidation",
        "level": "B1",
        "grammar": "Consolidation of Social Discourse & -ként/-nként Structures",
        "sections": [
            {
                "type": "story",
                "title": "A fillér értéke és az emberség (Móricz Zsigmond)",
                "ref": "stories/classics/b1/b1-17-moricz.json"
            },
            {
                "type": "exercise-group",
                "title": "Consolidation Practice",
                "ref": "exercises/b1/b1-17-consolidation-ex.json",
                "exerciseRefs": [f"b1-17-consolidation.ex0{k}" for k in range(1, 9)]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-17-consolidation.json", consolidation_data)
    print("Successfully built Hungarian B1 Core Unit 17 (b1-17)!")

if __name__ == "__main__":
    build_unit_17_core()
