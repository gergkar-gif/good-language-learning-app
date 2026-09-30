#!/usr/bin/env python3
"""Generate Hungarian B1 Core Unit 18: Politics & Public Life (b1-18)."""

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

def build_unit_18_core():
    # -------------------------------------------------------------------------
    # 1. Vocabulary Files (4 words each = 20 words total)
    # -------------------------------------------------------------------------
    voc_01 = {
        "id": "vocab.b1.18.01",
        "lesson": "b1-18-01",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "országgyűlés", "translation": "parliament, national assembly", "pos": "noun"},
            {"lemma": "képviselő", "translation": "member of parliament, representative", "pos": "noun"},
            {"lemma": "törvényjavaslat", "translation": "draft bill, legislative proposal", "pos": "noun"},
            {"lemma": "szavazás", "translation": "vote, voting, ballot", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-18-01-voc.json", voc_01)

    voc_02 = {
        "id": "vocab.b1.18.02",
        "lesson": "b1-18-02",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "választási rendszer", "translation": "electoral system", "pos": "noun"},
            {"lemma": "szavazati jog", "translation": "suffrage, right to vote", "pos": "noun"},
            {"lemma": "politikai párt", "translation": "political party", "pos": "noun"},
            {"lemma": "koalíció", "translation": "coalition government", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-18-02-voc.json", voc_02)

    voc_03 = {
        "id": "vocab.b1.18.03",
        "lesson": "b1-18-03",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "közvita", "translation": "public debate, public discussion", "pos": "noun"},
            {"lemma": "érvelés", "translation": "argumentation, reasoning", "pos": "noun"},
            {"lemma": "kompromisszum", "translation": "compromise", "pos": "noun"},
            {"lemma": "közérdek", "translation": "public interest", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-18-03-voc.json", voc_03)

    voc_04 = {
        "id": "vocab.b1.18.04",
        "lesson": "b1-18-04",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "alapvető jogok", "translation": "fundamental rights and liberties", "pos": "noun"},
            {"lemma": "állampolgári kötelesség", "translation": "civic duty, citizen's obligation", "pos": "noun"},
            {"lemma": "önkormányzat", "translation": "local government, municipality", "pos": "noun"},
            {"lemma": "jogállamiság", "translation": "rule of law", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-18-04-voc.json", voc_04)

    voc_05 = {
        "id": "vocab.b1.18.05",
        "lesson": "b1-18-05",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "közélet", "translation": "public affairs, political life", "pos": "noun"},
            {"lemma": "sajtótájékoztató", "translation": "press conference", "pos": "noun"},
            {"lemma": "hírháttér", "translation": "news background, in-depth context", "pos": "noun"},
            {"lemma": "álláspontok ütköztetése", "translation": "confronting opposing viewpoints", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-18-05-voc.json", voc_05)

    # -------------------------------------------------------------------------
    # 2. Grammar Files
    # -------------------------------------------------------------------------
    gr_01_a = {
        "id": "grammar.b1.18.01.concessive-annak-ellenere",
        "title": "Concessive Clauses: annak ellenére, hogy... ('despite the fact that')",
        "sections": [
            {
                "type": "text",
                "title": "Expressing Concession in Political Discourse",
                "content": "*Annak ellenére, hogy...* ('in spite of the fact that / despite') introduces concessive facts that did not prevent an outcome: *Annak ellenére, hogy heves vita alakult ki, a parlament elfogadta a törvényt.*"
            },
            {
                "type": "examples",
                "title": "Examples with annak ellenére, hogy",
                "items": [
                    {
                        "spanish": "Annak ellenére, hogy késő este volt, a képviselők folytatták a szavazást.",
                        "english": "Despite the fact that it was late evening, representatives continued voting."
                    },
                    {
                        "spanish": "A javaslatot elfogadták, annak ellenére, hogy több módosítást is benyújtottak.",
                        "english": "The proposal was adopted, despite the fact that several amendments were submitted."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-18-01-a-gr.json", gr_01_a)

    gr_01_b = {
        "id": "grammar.b1.18.01.concessive-bar-habar",
        "title": "Concessive Conjunctions: bár, habár, noha",
        "sections": [
            {
                "type": "text",
                "title": "Everyday Concessives: bár and habár",
                "content": "*Bár* and *habár* ('although / even though') are versatile concessive conjunctions used at the start of subordinate clauses: *Bár a pártok nézetei eltérnek, a nemzeti érdekben megegyeztek.*"
            },
            {
                "type": "examples",
                "title": "Sentences with bár and habár",
                "items": [
                    {
                        "spanish": "Bár a szavazás szoros volt, a többség egyértelmű döntést hozott.",
                        "english": "Although the vote was tight, the majority made a clear decision."
                    },
                    {
                        "spanish": "Habár nem mindenki értett egyet, a vita békés mederben maradt.",
                        "english": "Even though not everyone agreed, the debate remained in peaceful channels."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-18-01-b-gr.json", gr_01_b)

    gr_02_a = {
        "id": "grammar.b1.18.02.concessive-hiaba",
        "title": "Futility and In vain: hiába ('in vain, no matter how much')",
        "sections": [
            {
                "type": "text",
                "title": "Expressing Futile Attempts with hiába",
                "content": "*Hiába* indicates an effort that failed to produce the desired result: *Hiába tiltakoztak a módosítás ellen, a javaslat nem változott.* ('In vain did they protest against the amendment, the bill did not change.')."
            },
            {
                "type": "examples",
                "title": "Using hiába in debate",
                "items": [
                    {
                        "spanish": "Hiába érveltek órákon át, a bizottság nem változtatta meg a határozatot.",
                        "english": "No matter how much they argued for hours, the committee did not change the resolution."
                    },
                    {
                        "spanish": "Hiába volt hideg az idő, a polgárok nagy számban mentek el szavazni.",
                        "english": "Even though the weather was cold, citizens turned out to vote in large numbers."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-18-02-a-gr.json", gr_02_a)

    gr_02_b = {
        "id": "grammar.b1.18.02.adversative-ugyanakkor",
        "title": "Adversative Balancing: mindazonáltal, ugyanakkor",
        "sections": [
            {
                "type": "text",
                "title": "Balancing Differing Arguments",
                "content": "In formal parliamentary and public discussions, *ugyanakkor* ('at the same time') and *mindazonáltal* ('nevertheless') link contrasting viewpoints with nuance."
            },
            {
                "type": "examples",
                "title": "Balancing expressions",
                "items": [
                    {
                        "spanish": "A törvény fontos lépés előre, ugyanakkor további pontosításokra van szükség.",
                        "english": "The law is an important step forward; at the same time, further clarifications are needed."
                    },
                    {
                        "spanish": "A vita nehéz volt, mindazonáltal sikerült elérni a kompromisszumot.",
                        "english": "The debate was arduous; nevertheless, they succeeded in reaching a compromise."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-18-02-b-gr.json", gr_02_b)

    gr_03_a = {
        "id": "grammar.b1.18.03.compromise-register",
        "title": "Negotiation & Agreement Verbs: megállapodik, engedményt tesz",
        "sections": [
            {
                "type": "text",
                "title": "Formulas for Reaching Consensus",
                "content": "Key parliamentary collocations include: *megállapodásra jut* ('reaches an agreement'), *engedményt tesz* ('makes a concession'), *közös nevezőre jut* ('finds common ground')."
            },
            {
                "type": "examples",
                "title": "Negotiation vocabulary",
                "items": [
                    {
                        "spanish": "A frakciók végül megállapodásra jutottak a költségvetésről.",
                        "english": "The parliamentary groups ultimately reached an agreement on the budget."
                    },
                    {
                        "spanish": "A siker érdekében mindkét oldalnak engedményeket kellett tennie.",
                        "english": "For the sake of success both sides had to make concessions."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-18-03-a-gr.json", gr_03_a)

    gr_03_b = {
        "id": "grammar.b1.18.03.formal-declarative",
        "title": "Parliamentary Formulations: javaslatot tesz, napirendre tűz",
        "sections": [
            {
                "type": "text",
                "title": "Procedural Legislative Expressions",
                "content": "Procedural terms include: *napirendre tűz* ('places on the agenda'), *javaslatot terjeszt elő* ('submits a proposal'), *határozatot hoz* ('passes a resolution')."
            },
            {
                "type": "examples",
                "title": "Procedural phrases in use",
                "items": [
                    {
                        "spanish": "Az országgyűlés elnöke jövő hétre tűzte napirendre a vitát.",
                        "english": "The Speaker of Parliament placed the debate on the agenda for next week."
                    },
                    {
                        "spanish": "A képviselők kétharmados többséggel hozták meg a történelmi határozatot.",
                        "english": "Representatives passed the historic resolution with a two-thirds majority."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-18-03-b-gr.json", gr_03_b)

    gr_04_a = {
        "id": "grammar.b1.18.04.rights-and-duties",
        "title": "Civic Obligations and Rights: joga van hozzá, kötelessége",
        "sections": [
            {
                "type": "text",
                "title": "Expressing Constitutional Rights and Civic Duties",
                "content": "*Joga van ahhoz, hogy...* ('has the right to...') vs *kötelessége, hogy...* ('has the obligation to...'). Both structures take subjunctive clauses."
            },
            {
                "type": "examples",
                "title": "Rights and duties in civic life",
                "items": [
                    {
                        "spanish": "Minden állampolgárnak joga van ahhoz, hogy részt vegyen a választásokon.",
                        "english": "Every citizen has the right to take part in elections."
                    },
                    {
                        "spanish": "A törvények betartása minden ember alapvető állampolgári kötelessége.",
                        "english": "Observing the laws is every person's fundamental civic duty."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-18-04-a-gr.json", gr_04_a)

    gr_04_b = {
        "id": "grammar.b1.18.04.impersonal-modal-forms",
        "title": "Institutional Impersonal Rules: kötelező, megengedett, tilos",
        "sections": [
            {
                "type": "text",
                "title": "Legal and Institutional Norms",
                "content": "Rules in public administration are stated with predicate adjectives: *kötelező* ('mandatory'), *megengedett* ('permitted'), *tilos* ('prohibited') followed by infinitives."
            },
            {
                "type": "examples",
                "title": "Institutional rules",
                "items": [
                    {
                        "spanish": "A választások idején tilos a szavazóhelyiségben pártpropagandát folytatni.",
                        "english": "During elections it is prohibited to conduct party propaganda inside polling stations."
                    },
                    {
                        "spanish": "Az önkormányzatok számára kötelező a közmeghallgatások megtartása.",
                        "english": "It is mandatory for local municipalities to hold public hearings."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-18-04-b-gr.json", gr_04_b)

    gr_05_a = {
        "id": "grammar.b1.18.05.public-speaking",
        "title": "Structuring a Public Presentation: Elöljáróban, Másodszor, Végezetül",
        "sections": [
            {
                "type": "text",
                "title": "Public Discourse Discourse Markers",
                "content": "Presenting arguments logically: *Elöljáróban le kell szögeznünk...* ('First and foremost we must state...'), *Másrészről figyelembe kell venni...* ('On the other hand we must take into account...'), *Végezetül megállapíthatjuk...* ('Finally we may conclude...')."
            },
            {
                "type": "examples",
                "title": "Presentation connectors",
                "items": [
                    {
                        "spanish": "Elöljáróban szeretném bemutatni a törvényjavaslat legfőbb céljait.",
                        "english": "First of all, I would like to present the draft bill's primary objectives."
                    },
                    {
                        "spanish": "Végezetül felkérem a tisztelt házat, hogy támogassa a kezdeményezést.",
                        "english": "In conclusion, I request the esteemed assembly to support the initiative."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-18-05-a-gr.json", gr_05_a)

    gr_05_b = {
        "id": "grammar.b1.18.05.nuanced-agreement",
        "title": "Partial Agreement: egyetértek azzal, hogy..., de...",
        "sections": [
            {
                "type": "text",
                "title": "Agreeing Up to a Point in Debate",
                "content": "Mature democratic dialogue at B1: *Egyetértek azzal a felvetéssel, hogy..., de nem szabad elfelejtenünk...* ('I agree with the suggestion that..., but we must not forget...')."
            },
            {
                "type": "examples",
                "title": "Debating courteously",
                "items": [
                    {
                        "spanish": "Egyetértek azzal, hogy reformokra van szükség, de a részletekben még vita van.",
                        "english": "I agree that reforms are necessary, but on the details debate still remains."
                    },
                    {
                        "spanish": "Megértem a képviselő úr aggodalmait, de a költségvetés nem enged több kiadást.",
                        "english": "I understand the representative's concerns, but the budget permits no further expenditures."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-18-05-b-gr.json", gr_05_b)

    # -------------------------------------------------------------------------
    # 3. Exercise Files
    # -------------------------------------------------------------------------
    for i in range(1, 6):
        padded = f"0{i}"
        curr_voc = [voc_01, voc_02, voc_03, voc_04, voc_05][i-1]
        ex_data = {
            "lesson": f"b1-18-{padded}",
            "exercises": [
                {
                    "id": f"b1-18-{padded}.ex01",
                    "type": "matching",
                    "category": "vocabulary",
                    "pairs": [[w["lemma"], w["translation"]] for w in curr_voc["words"]]
                },
                {
                    "id": f"b1-18-{padded}.ex02",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "question": f"Melyik mondat fejezi ki helyesen a megengedő viszonyt? (Lesson {i})",
                    "options": [
                        "Annak ellenére, hogy késő este volt, a parlament folytatta a szavazást.",
                        "Annak ellenére mert késő este volt hogy a parlament szavazni.",
                        "Bár késő volt este ezért a parlament nem szavazott volt."
                    ],
                    "correct": 0
                },
                {
                    "id": f"b1-18-{padded}.ex03",
                    "type": "fill-blank",
                    "category": "vocabulary",
                    "sentence": "A képviselők az _____ vitatják meg az új törvényjavaslatokat és a közérdekű ügyeket. (Parliament / Országházban)",
                    "answer": "Országházban"
                },
                {
                    "id": f"b1-18-{padded}.ex04",
                    "type": "fill-blank",
                    "category": "grammar",
                    "sentence": "Annak ellenére, ____ több módosítást benyújtottak, a törvényt elfogadták. (that)",
                    "answer": "hogy"
                },
                {
                    "id": f"b1-18-{padded}.ex05",
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "question": "Mit jelent a szavazati jog a demokratikus államban?",
                    "options": [
                        "A polgárok jogát arra, hogy választásokon vegyenek részt és véleményt nyilvánítsanak.",
                        "Kizárólag a miniszterek jogát arra, hogy törvényt hozzanak.",
                        "Egy külföldi utazási engedély kiváltásának lehetőségét."
                    ],
                    "correct": 0
                },
                {
                    "id": f"b1-18-{padded}.ex06",
                    "type": "fill-blank",
                    "category": "grammar",
                    "sentence": "Hiába érveltek órákon át, a bizottság nem változtatott a döntés____. (on -on/-en/-ön)",
                    "answer": "én"
                },
                {
                    "id": f"b1-18-{padded}.ex07",
                    "type": "sentence-builder",
                    "category": "grammar",
                    "tiles": ["A", "jogállamiság", "és", "az", "alapvető", "jogok", "tisztelete", "a", "demokratikus", "társadalom", "alapja."],
                    "solution": ["A", "jogállamiság", "és", "az", "alapvető", "jogok", "tisztelete", "a", "demokratikus", "társadalom", "alapja."]
                },
                {
                    "id": f"b1-18-{padded}.ex08",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "Mi a kompromisszum lényege a közéleti vitákban?",
                    "options": [
                        "A felek kölcsönös engedményeket tesznek a közös megegyezés érdekében.",
                        "Egyik fél teljesen megsemmisíti a másik érveit anélkül, hogy meghallgatná.",
                        "A vita azonnali berekesztése szavazás nélkül."
                    ],
                    "correct": 0
                }
            ]
        }
        write_json(f"content/hu/exercises/b1/b1-18-{padded}-ex.json", ex_data)

    # Consolidation exercises
    ex_consolidation = {
        "lesson": "b1-18-consolidation",
        "exercises": [
            {
                "id": "b1-18-consolidation.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["országgyűlés", "parliament"],
                    ["törvényjavaslat", "draft bill"],
                    ["szavazati jog", "right to vote"],
                    ["jogállamiság", "rule of law"]
                ]
            },
            {
                "id": "b1-18-consolidation.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik mondat fogalmazza meg helyesen a demokratikus állampolgári magatartást?",
                "options": [
                    "Bár a vélemények gyakran különböznek, a nyílt párbeszéd és a kompromisszum elengedhetetlen.",
                    "Annak ellenére mert vélemények különbözik nem beszélnek semmit.",
                    "Mivel vita van ezért tilos szavazni választáson."
                ],
                "correct": 0
            },
            {
                "id": "b1-18-consolidation.ex03",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A törvényjavaslatról a képviselők kétharmados többséggel hoztak ____. (decision / resolution)",
                "answer": "határozatot"
            },
            {
                "id": "b1-18-consolidation.ex04",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Minden állampolgárnak joga van ahhoz, ____ szavazzon a választáson. (that / in order that)",
                "answer": "hogy"
            },
            {
                "id": "b1-18-consolidation.ex05",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "helyi", "önkormányzatok", "a", "polgárok", "mindennapi", "életét", "segítő", "döntéseket", "hoznak."],
                "solution": ["A", "helyi", "önkormányzatok", "a", "polgárok", "mindennapi", "életét", "segítő", "döntéseket", "hoznak."]
            },
            {
                "id": "b1-18-consolidation.ex06",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent a közérdek fogalma?",
                "options": [
                    "Az egész társadalom, a közösség javát és biztonságát szolgáló célt.",
                    "Egyetlen magánszemély kizárólagos anyagi hasznát.",
                    "Egy külföldi vállalat titkos üzleti tervét."
                ],
                "correct": 0
            },
            {
                "id": "b1-18-consolidation.ex07",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A sajtó képviselői részére a miniszter hivatalos sajtó____ tartott. (conference)",
                "answer": "tájékoztatót"
            },
            {
                "id": "b1-18-consolidation.ex08",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Hogyan ábrázolja Mikszáth Kálmán a választási beszédeket híres szatírájában?",
                "options": [
                    "Finom humorral, bemutatva a választók józanságát és a politikusok túlzó ígéreteit.",
                    "Véres csataként, ahol a jelöltek párbajt vívnak egymással.",
                    "Unos-untalan felolvasott törvényszövegek száraz gyűjteményeként."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-18-consolidation-ex.json", ex_consolidation)

    # -------------------------------------------------------------------------
    # 4. Classic Story Adaptation for Lesson 5 / Consolidation
    # -------------------------------------------------------------------------
    story_classic = {
        "id": "story.b1.18.classic",
        "title": "A képviselő úr választási beszéde",
        "level": "B1",
        "order": 18,
        "type": "classics",
        "estimatedMinutes": 7,
        "summary": "An adaptation from Kálmán Mikszáth's satirical masterpieces on Hungarian parliamentary politics and election campaigns ('A képviselő úr'). In a small county town, the aspiring MP delivers a grand, flowery speech promising golden bridges and prosperity, while the sensible townspeople listen with wry humor and shrewd common sense.",
        "characters": [
            "A képviselőjelölt",
            "Bíró uram",
            "A vármegyei polgárok"
        ],
        "location": "Kisvárosi főtér, Magyarország",
        "author": "Mikszáth Kálmán",
        "work": "A képviselő úr",
        "paragraphs": [
            {
                "type": "narration",
                "text": "A kisváros piacterén a nyári délelőttön összesereglettek a polgárok, a csizmadiák és a tekintélyes gazdák. A városháza előtti emelvényre fellépett a budapesti képviselőjelölt, fénylő cilinderben és díszes atillában."
            },
            {
                "type": "dialogue",
                "speaker": "A képviselőjelölt",
                "text": "Tisztelt választópolgárok! Ha engem küldenek az országgyűlésbe, vasutat viszek minden faluba, hidat építek a patakra, és eltörlöm a legnehezebb adókat is!"
            },
            {
                "type": "narration",
                "text": "A tömeg csendesen hallgatta a szép szavakat. Az öreg bíró a pipáját szívta, szemében huncut fény csillant meg."
            },
            {
                "type": "dialogue",
                "speaker": "Bíró uram",
                "text": "Igen szép beszéd, nagyságos képviselő úr! De mondja csak: patakunk ugyan nincsen a falu határában, hát akkor hová építi azt a szép új hidat?"
            },
            {
                "type": "narration",
                "text": "A tömegből halk kuncogás hallatszott. A képviselőjelölt azonban nem jött zavarba, kezét a magasba lendítette, mint aki a világ legtermészetesebb dologáról beszél."
            },
            {
                "type": "dialogue",
                "speaker": "A képviselőjelölt",
                "text": "Bíró uram, ne aggódjék! Ha híd lesz, hát patakot is ásatunk hozzá a kormánnyal, mégpedig kristálytiszta vizűt!"
            },
            {
                "type": "narration",
                "text": "Erre már az egész tér hahotázásban tört ki. A polgárok szerették a szép beszédeket, de a magyar ember józanságát és éles eszét még a legfényesebb ígéretek sem tudták elhomályosítani."
            },
            {
                "type": "dialogue",
                "speaker": "Bíró uram",
                "text": "No, látja, képviselő úr! A szavazatunkat megkapja, mert megnevettetett minket. De a gátakat és a földeket magunknak kell megművelnünk, akármit mondanak is Pesten."
            }
        ]
    }
    write_json("content/hu/stories/classics/b1/b1-18-mikszath.json", story_classic)

    # -------------------------------------------------------------------------
    # 5. Lesson Files (01 to 05 + consolidation)
    # -------------------------------------------------------------------------
    for i in range(1, 6):
        padded = f"0{i}"
        titles = {
            "01": ("Even Though...", "Parlament, képviselők és a törvényhozás"),
            "02": ("How Decisions Get Made", "Választási rendszer és politikai pártok"),
            "03": ("A Public Debate", "Közvita, érvelés és a kompromisszum"),
            "04": ("Rights & Responsibilities, Revisited", "Alapvető jogok és állampolgári kötelességek"),
            "05": ("Talking About Current Events", "Közélet, sajtó és nyilvános beszéd")
        }
        en_title, hu_title = titles[padded]
        lesson_data = {
            "id": f"lesson.b1.18-{padded}",
            "unit": 18,
            "title": en_title,
            "level": "B1",
            "grammar": "Concessive Connectors (annak ellenére, hogy / bár / hiába) in Political Context",
            "goal": [
                f"I can understand and use vocabulary for {en_title.lower()}.",
                "I can form concessive clauses with annak ellenére, hogy, bár, and hiába in Hungarian.",
                "I can discuss public affairs, parliament, elections, and civic duties.",
                "I can master four new target vocabulary items in authentic context."
            ],
            "sections": [
                {
                    "type": "goal",
                    "title": "Lesson Goals",
                    "items": [
                        f"I can understand and use vocabulary for {en_title.lower()}.",
                        "I can form concessive clauses with annak ellenére, hogy, bár, and hiába in Hungarian.",
                        "I can discuss public affairs, parliament, elections, and civic duties.",
                        "I can master four new target vocabulary items in authentic context."
                    ]
                },
                {"type": "recycle", "title": "Quick Review"},
                {"type": "grammar", "ref": f"grammar/b1/b1-18-{padded}-a-gr.json"},
                {"type": "grammar", "ref": f"grammar/b1/b1-18-{padded}-b-gr.json"},
                {"type": "vocabulary", "title": "Lesson Vocabulary", "ref": f"vocabulary/b1/b1-18-{padded}-voc.json"},
                {
                    "type": "exercise-group",
                    "title": "Practice",
                    "ref": f"exercises/b1/b1-18-{padded}-ex.json",
                    "exerciseRefs": [f"b1-18-{padded}.ex0{k}" for k in range(1, 9)]
                }
            ]
        }
        write_json(f"content/hu/lessons/b1/b1-18-{padded}.json", lesson_data)

    consolidation_data = {
        "id": "lesson.b1.18-consolidation",
        "unit": 18,
        "title": "Unit 18 Consolidation",
        "level": "B1",
        "grammar": "Consolidation of Political Discourse & Concessive Connectors",
        "sections": [
            {
                "type": "story",
                "title": "A képviselő úr választási beszéde (Mikszáth Kálmán)",
                "ref": "stories/classics/b1/b1-18-mikszath.json"
            },
            {
                "type": "exercise-group",
                "title": "Consolidation Practice",
                "ref": "exercises/b1/b1-18-consolidation-ex.json",
                "exerciseRefs": [f"b1-18-consolidation.ex0{k}" for k in range(1, 9)]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-18-consolidation.json", consolidation_data)
    print("Successfully built Hungarian B1 Core Unit 18 (b1-18)!")

if __name__ == "__main__":
    build_unit_18_core()
