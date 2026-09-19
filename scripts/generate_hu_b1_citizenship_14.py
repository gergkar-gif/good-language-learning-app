#!/usr/bin/env python3
"""Generate Hungarian B1 Citizenship Unit 14: The 18th Century & Rebuilding (b1-mariaterezia)."""

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

def build_unit_14_citizenship():
    # -------------------------------------------------------------------------
    # 1. Vocabulary Files (8 words each = 40 words total)
    # -------------------------------------------------------------------------
    voc_01 = {
        "id": "vocab.b1.mariaterezia.01",
        "lesson": "b1-mariaterezia-01",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "újranépesítés", "translation": "repopulation", "pos": "noun"},
            {"lemma": "telepes", "translation": "settler, colonist", "pos": "noun"},
            {"lemma": "sváb", "translation": "Danube Swabian (German settler)", "pos": "noun"},
            {"lemma": "nemzetiség", "translation": "ethnic minority, nationality", "pos": "noun"},
            {"lemma": "többnemzetiségű ország", "translation": "multinational country", "pos": "noun"},
            {"lemma": "pusztaság", "translation": "wasteland, desolate plain", "pos": "noun"},
            {"lemma": "letelepedési engedély", "translation": "settlement permit, charter", "pos": "noun"},
            {"lemma": "újjáéledés", "translation": "revival, rebirth", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-mariaterezia-01-voc.json", voc_01)

    voc_02 = {
        "id": "vocab.b1.mariaterezia.02",
        "lesson": "b1-mariaterezia-02",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "Mária Terézia", "translation": "Maria Theresa", "pos": "noun"},
            {"lemma": "Pragmatica Sanctio", "translation": "Pragmatic Sanction (1723)", "pos": "noun"},
            {"lemma": "pozsonyi országgyűlés", "translation": "Diet of Pozsony (1741)", "pos": "noun"},
            {"lemma": "nemesi felajánlás", "translation": "noble offer ('Vitam et sanguinem!')", "pos": "noun"},
            {"lemma": "női trónöröklés", "translation": "female royal succession", "pos": "noun"},
            {"lemma": "osztrák örökösödési háború", "translation": "War of the Austrian Succession", "pos": "noun"},
            {"lemma": "uralkodónő", "translation": "reigning queen, female monarch", "pos": "noun"},
            {"lemma": "hűségeskü", "translation": "oath of fealty, loyalty pledge", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-mariaterezia-02-voc.json", voc_02)

    voc_03 = {
        "id": "vocab.b1.mariaterezia.03",
        "lesson": "b1-mariaterezia-03",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "Ratio Educationis", "translation": "Ratio Educationis (1777 education decree)", "pos": "noun"},
            {"lemma": "Urbárium", "translation": "Urbarium (1767 peasant regulation)", "pos": "noun"},
            {"lemma": "jobbágyvédelem", "translation": "protection of serfs", "pos": "noun"},
            {"lemma": "iskolakötelezettség", "translation": "mandatory school attendance", "pos": "noun"},
            {"lemma": "alapfokú oktatás", "translation": "primary education, elementary schooling", "pos": "noun"},
            {"lemma": "robot", "translation": "corvée, unpaid feudal labor", "pos": "noun"},
            {"lemma": "felvilágosult abszolutizmus", "translation": "enlightened absolutism", "pos": "noun"},
            {"lemma": "állami rendelet", "translation": "state decree, royal ordinance", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-mariaterezia-03-voc.json", voc_03)

    voc_04 = {
        "id": "vocab.b1.mariaterezia.04",
        "lesson": "b1-mariaterezia-04",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "II. József", "translation": "Joseph II", "pos": "noun"},
            {"lemma": "kalapos király", "translation": "the 'hatted king'", "pos": "noun"},
            {"lemma": "türelmi rendelet", "translation": "Edict of Tolerance (1781)", "pos": "noun"},
            {"lemma": "nyelvrendelet", "translation": "Language Edict (1784)", "pos": "noun"},
            {"lemma": "német hivatalos nyelv", "translation": "German as official state language", "pos": "noun"},
            {"lemma": "Szent Korona elszállítása", "translation": "removal of Holy Crown to Vienna", "pos": "noun"},
            {"lemma": "rendeleti kormányzás", "translation": "governance by decree", "pos": "noun"},
            {"lemma": "halálos ágy", "translation": "deathbed", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-mariaterezia-04-voc.json", voc_04)

    voc_05 = {
        "id": "vocab.b1.mariaterezia.05",
        "lesson": "b1-mariaterezia-05",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "nemzeti ébredés", "translation": "national awakening", "pos": "noun"},
            {"lemma": "anyanyelvi mozgalom", "translation": "mother-tongue language movement", "pos": "noun"},
            {"lemma": "Bessenyei György", "translation": "György Bessenyei (Enlightenment writer)", "pos": "noun"},
            {"lemma": "irodalmi élet", "translation": "literary life, intellectual scene", "pos": "noun"},
            {"lemma": "nemesi ellenállás", "translation": "noble resistance to centralism", "pos": "noun"},
            {"lemma": "hagyománytisztelet", "translation": "respect for national traditions", "pos": "noun"},
            {"lemma": "nemzeti öntudat", "translation": "national self-awareness, identity", "pos": "noun"},
            {"lemma": "felvilágosodás", "translation": "the Enlightenment", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-mariaterezia-05-voc.json", voc_05)

    # -------------------------------------------------------------------------
    # 2. Grammar Files
    # -------------------------------------------------------------------------
    gr_01 = {
        "id": "grammar.b1.mariaterezia.01.postpositions-altal-reven",
        "title": "Postpositions of Instrumentality: által and révén",
        "sections": [
            {
                "type": "text",
                "title": "Expressing Agency and Means with által and révén",
                "content": "*Által* denotes the agent or intermediary ('by, through'): *a királynő által kiadott rendelet* ('the decree issued by the queen'). *Révén* expresses the means or medium ('by means of, through'): *a betelepítések révén népesült be a vidék* ('through colonization the land became populated')."
            },
            {
                "type": "examples",
                "title": "Examples of által and révén",
                "items": [
                    {
                        "spanish": "Az új törvények révén megerősödött a gazdaság és az oktatás.",
                        "english": "Through the new laws, the economy and education grew stronger."
                    },
                    {
                        "spanish": "Mária Terézia által létrehozott reformok védték a jobbágyokat.",
                        "english": "The reforms created by Maria Theresa protected the serfs."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-mariaterezia-01-gr.json", gr_01)

    gr_02 = {
        "id": "grammar.b1.mariaterezia.02.instrumental-agency",
        "title": "The Instrumental Case in Historical Reforms: -val/-vel",
        "sections": [
            {
                "type": "text",
                "title": "Combining Instrumental with Reform Verbs",
                "content": "To explain historical actions, pair verbs with the instrumental case: *rendelettel szabályoz* (regulates by decree), *szerződéssel biztosít* (secures by treaty), *hűségesküvel pecsétel meg* (seals with an oath of fealty)."
            },
            {
                "type": "examples",
                "title": "Instrumental reform examples",
                "items": [
                    {
                        "spanish": "A Pragmatica Sanctio törvénnyel fogadták el a női trónöröklést.",
                        "english": "They accepted female succession by the law of the Pragmatic Sanction."
                    },
                    {
                        "spanish": "A nemesek kardrántással és hűségesküvel fogadták a fiatal uralkodónőt.",
                        "english": "The nobles welcomed the young monarch with drawn swords and an oath of fealty."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-mariaterezia-02-gr.json", gr_02)

    gr_03 = {
        "id": "grammar.b1.mariaterezia.03.expressing-obligation-modal",
        "title": "Modal Obligation in Royal Decrees: köteles, kötelezővé tesz",
        "sections": [
            {
                "type": "text",
                "title": "Legal Register of Feudal Decrees",
                "content": "Decrees define rights and duties using formal adjectives: *köteles + infinitive* (is obliged to...), *kötelezővé tesz* (makes mandatory), *megszabja a határokat* (sets the boundaries)."
            },
            {
                "type": "examples",
                "title": "Legal obligation examples",
                "items": [
                    {
                        "spanish": "Az Urbárium rendelet kötelezővé tette a jobbágyi robot pontos korlátozását.",
                        "english": "The Urbarium decree made the exact limitation of peasant labor mandatory."
                    },
                    {
                        "spanish": "Minden gyermek köteles volt alapfokú iskolába járni a Ratio Educationis szerint.",
                        "english": "Every child was obliged to attend primary school according to the Ratio Educationis."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-mariaterezia-03-gr.json", gr_03)

    gr_04 = {
        "id": "grammar.b1.mariaterezia.04.concessive-contrast-dacara",
        "title": "Formal Concessive Structures: dacára, ellenére, noha",
        "sections": [
            {
                "type": "text",
                "title": "Expressing Resistance to Decrees",
                "content": "To describe conflicts between central royal policy and national pushback: *a nemesi ellenállás ellenére / dacára* (in spite of noble resistance), *noha jószándékú volt...* (although it was well-intentioned...)."
            },
            {
                "type": "examples",
                "title": "Resistance and contrast examples",
                "items": [
                    {
                        "spanish": "A heves ellenállás dacára II. József rendeletekkel kormányzott.",
                        "english": "In spite of fierce resistance, Joseph II governed by decree."
                    },
                    {
                        "spanish": "Noha a császár modernizálni akarta a birodalmat, megsértette a magyar alkotmányt.",
                        "english": "Although the emperor wanted to modernize the empire, he violated the Hungarian constitution."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-mariaterezia-04-gr.json", gr_04)

    gr_05 = {
        "id": "grammar.b1.mariaterezia.05.causative-verbal-derivations",
        "title": "Causative Verbs of Cultural Renewal: megerősít, felvirágoztat, ébreszt",
        "sections": [
            {
                "type": "text",
                "title": "Causative Verbs in National Awakening",
                "content": "Intellectual movements trigger action: *felvirágoztat* (causes to flourish), *felébreszt* (awakens), *terjeszt* (spreads/diffuses), *ösztönöz* (encourages/stimulates)."
            },
            {
                "type": "examples",
                "title": "Cultural revival verbs",
                "items": [
                    {
                        "spanish": "Bessenyei György művei felébresztették a nemzeti öntudatot a nemesség körében.",
                        "english": "György Bessenyei's works awakened national consciousness among the nobility."
                    },
                    {
                        "spanish": "A magyar írók elszánt munkája felvirágoztatta az anyanyelvi kultúrát.",
                        "english": "The determined work of Hungarian writers caused the mother-tongue culture to flourish."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-mariaterezia-05-gr.json", gr_05)

    # -------------------------------------------------------------------------
    # 3. World Stories (01 to 05 + Omnibus) in TRIH Narrative Style
    # -------------------------------------------------------------------------
    stories_content = {
        "b1-mariaterezia-01-telepesek.json": [
            "A török hódoltság után a Duna mentén és az Alföldön elképesztő pusztaság és üres földek fogadták az utazót.",
            "A bécsi udvar és a nagybirtokosok azonnal felismerték: a virágzó újjáéledés alapja a gyors újranépesítés.",
            "Különleges letelepedési engedély és adómentesség ígéretével hívtak be szorgalmas katolikus földműveseket Európából.",
            "Ekkor érkezett a legtöbb német ajkú sváb telepes a Dunántúlra és a Bácskába, miközben szlovákok és románok is letelepedtek.",
            "Ezzel Magyarország sokszínű, többnemzetiségű ország lett, ahol minden nemzetiség hozzátette saját kultúráját a közös hazához."
        ],
        "b1-mariaterezia-02-uralkodono.json": [
            "1740-ben egy huszonhárom éves fiatal nő örökölte a Habsburg trónt. Ki gondolta volna, hogy negyven évig fog uralkodni?",
            "Az 1723-ban elfogadott Pragmatica Sanctio törvény garantálta a női trónöröklés jogát a birodalomban.",
            "Ám európai riválisai azonnal megtámadták, és kitört a véres osztrák örökösödési háború a birodalom felosztására.",
            "A fiatal uralkodónő, Mária Terézia személyesen jelent meg a pozsonyi országgyűlés termében a magyar nemesek előtt.",
            "A magyar urak meghatódva rántottak kardot, és elhangzott a legendás nemesi felajánlás: Életünket és vérünket! Ezzel megerősítették a szent hűségeskü kötelékét."
        ],
        "b1-mariaterezia-03-reformok.json": [
            "Mária Terézia a felvilágosult abszolutizmus bölcs szellemében kormányozta virágzó országait. Milyen reformokat hozott?",
            "Az 1767-es Urbárium állami rendelet a jobbágyvédelem legfőbb bástyájává vált a földesúri önkénnyel szemben.",
            "Pontosan megszabta a jobbágyok jogait, és szigorúan korlátozta a heti ingyen végzendő robot mértékét.",
            "1777-ben kiadta az iskolarendszert megalapozó híres Ratio Educationis rendeletet a tudás terjesztésére.",
            "A törvény kötelezővé tette az iskolakötelezettség elvét, megteremtve az ingyenes alapfokú oktatás alapjait országszerte."
        ],
        "b1-mariaterezia-04-kalaposkiraly.json": [
            "Fia, II. József császár még radikálisabb eszmékkel lépett a trónra. De miért hívta a nép kalapos királynak?",
            "Mivel nem akart esküt tenni a magyar alkotmányra, megtagadta a koronázást, és Bécsbe vitette a Szent Korona kincsét. A rendeleti kormányzás útjára lépett.",
            "1781-ben kiadta a korszakalkotó türelmi rendelet szövegét, amely teljes vallásszabadságot biztosított a protestánsoknak.",
            "Ám 1784-ben kiadta a vitatott nyelvrendelet intézkedést, amely a német hivatalos nyelv bevezetését írta elő minden hivatalban.",
            "A magyar nemesség felháborodott az elnémetesítés miatt, és a császár végül a halálos ágyán szinte minden rendeletét visszavonta."
        ],
        "b1-mariaterezia-05-ebredes.json": [
            "A német nyelvrendelet óriási megrázkódtatást okozott a nemzetben. De paradox módon ez indította el a megújulást.",
            "A sértett nemesség körében azonnal heves nemesi ellenállás és büszke hagyománytisztelet lángolt fel a megyékben.",
            "Bessenyei György bécsi testőríró vezetésével megszületett az anyanyelvi mozgalom a magyar nyelv megmentésére.",
            "A felvilágosodás eszméi nyomán megindult a pezsgő irodalmi élet, megjelentek az első magyar újságok és színházak.",
            "Ez a csodálatos nemzeti ébredés megerősítette a nemzeti öntudat érzését, és egyenesen elvezetett a dicső reformkor küszöbéhez."
        ],
        "b1-mariaterezia.json": [
            "A török kiűzése után az elnéptelenedett országot sváb és más telepesek újranépesítették, gazdagítva a kultúrát.",
            "1741-ben Pozsonyban a magyar nemesség Életünket és vérünket felkiáltással állt ki a fiatal Mária Terézia mellett.",
            "A királynő az Urbáriummal védte a jobbágyokat, a Ratio Educationis rendelettel pedig bevezette a kötelező iskoláztatást.",
            "Fia, II. József türelmi rendeletet adott a protestánsoknak, de német nyelvrendeletével hatalmas felháborodást keltett.",
            "A nemzeti ellenállásból megszületett az anyanyelvi mozgalom és a nemzeti ébredés, megalapozva a magyar reformkort."
        ]
    }

    write_json("content/hu/stories/world/b1/b1-mariaterezia-01-telepesek.json", {
        "id": "story.b1.mariaterezia.01",
        "title": "Az ország újranépesítése a 18. században",
        "level": "B1",
        "lesson": 1,
        "order": 1,
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "How the devastated plains of Hungary were repopulated after the Ottoman wars by German Swabians, Slovaks, and Serbs, creating a colorful multinational state.",
        "characters": ["Telepes gazdák", "Földesurak"],
        "location": "Dunántúl, Bácska, Bánát",
        "paragraphs": [{"type": "narration", "text": t} for t in stories_content["b1-mariaterezia-01-telepesek.json"]]
    })

    write_json("content/hu/stories/world/b1/b1-mariaterezia-02-uralkodono.json", {
        "id": "story.b1.mariaterezia.02",
        "title": "Mária Terézia és az 1741-es pozsonyi országgyűlés",
        "level": "B1",
        "lesson": 2,
        "order": 2,
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "The dramatic moment in Pozsony when the Hungarian nobility drew their swords for Maria Theresa with the famous cry: 'Vitam et sanguinem!'",
        "characters": ["Mária Terézia", "Magyar főurak"],
        "location": "Pozsony (Bratislava)",
        "paragraphs": [{"type": "narration", "text": t} for t in stories_content["b1-mariaterezia-02-uralkodono.json"]]
    })

    write_json("content/hu/stories/world/b1/b1-mariaterezia-03-reformok.json", {
        "id": "story.b1.mariaterezia.03",
        "title": "Felvilágosult reformok: Urbárium és Ratio Educationis",
        "level": "B1",
        "lesson": 3,
        "order": 3,
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "Maria Theresa's enlightened decrees: the Urbarium limiting feudal peasant labor, and the Ratio Educationis establishing modern primary education.",
        "characters": ["Mária Terézia", "Jobbágyok", "Tanítók"],
        "location": "Bécs, Magyar Királyság",
        "paragraphs": [{"type": "narration", "text": t} for t in stories_content["b1-mariaterezia-03-reformok.json"]]
    })

    write_json("content/hu/stories/world/b1/b1-mariaterezia-04-kalaposkiraly.json", {
        "id": "story.b1.mariaterezia.04",
        "title": "II. József, a kalapos király és rendeletei",
        "level": "B1",
        "lesson": 4,
        "order": 4,
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "Joseph II's controversial rule by decree: the progressive Edict of Tolerance, the resented German language decree, and his deathbed revocations.",
        "characters": ["II. József", "Bécsi miniszterek"],
        "location": "Bécs, Buda",
        "paragraphs": [{"type": "narration", "text": t} for t in stories_content["b1-mariaterezia-04-kalaposkiraly.json"]]
    })

    write_json("content/hu/stories/world/b1/b1-mariaterezia-05-ebredes.json", {
        "id": "story.b1.mariaterezia.05",
        "title": "Nemzeti ébredés és a magyar nyelv mozgalma",
        "level": "B1",
        "lesson": 5,
        "order": 5,
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "How noble resistance to Germanization sparked the mother-tongue revival, György Bessenyei's writings, and the birth of modern Hungarian national identity.",
        "characters": ["Bessenyei György", "Kazinczy Ferenc"],
        "location": "Bécs, Pest",
        "paragraphs": [{"type": "narration", "text": t} for t in stories_content["b1-mariaterezia-05-ebredes.json"]]
    })

    write_json("content/hu/stories/world/b1/b1-mariaterezia.json", {
        "id": "story.b1.mariaterezia",
        "title": "A 18. század: újjáépítés és felvilágosodás",
        "level": "B1",
        "order": 14,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "The comprehensive saga of 18th-century Hungary: repopulation, Maria Theresa's enlightened absolutism, Joseph II's decrees, and the dawn of national awakening.",
        "characters": ["Mária Terézia", "II. József", "Bessenyei György"],
        "location": "Magyarország, Pozsony, Bécs",
        "paragraphs": [{"type": "narration", "text": t} for t in stories_content["b1-mariaterezia.json"]]
    })

    # -------------------------------------------------------------------------
    # 4. Exercises Files (01 to 05 + consolidation)
    # -------------------------------------------------------------------------
    ex_01 = {
        "lesson": "b1-mariaterezia-01",
        "exercises": [
            {
                "id": "b1-mariaterezia-01.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["újranépesítés", "repopulation"],
                    ["telepes", "settler / colonist"],
                    ["sváb", "Danube Swabian"],
                    ["nemzetiség", "ethnic minority / nationality"]
                ]
            },
            {
                "id": "b1-mariaterezia-01.ex01b",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["többnemzetiségű ország", "multinational country"],
                    ["pusztaság", "wasteland"],
                    ["letelepedési engedély", "settlement permit"],
                    ["újjáéledés", "revival / resurgence"]
                ]
            },
            {
                "id": "b1-mariaterezia-01.ex02",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Honnan érkeztek a legnagyobb számban német nyelvű telepesek Magyarországra a 18. században?",
                "options": [
                    "Dél-Németországból (svábok).",
                    "Spanyolországból.",
                    "Svédországból."
                ],
                "correct": 0
            },
            {
                "id": "b1-mariaterezia-01.ex03",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A betelepítések ____ a lakatlan területek gyorsan benépesültek. (through / by means of)",
                "answer": "révén"
            },
            {
                "id": "b1-mariaterezia-01.ex04",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A török háborúk után a gazdag mezők helyén sivár ____ maradt. (wasteland)",
                "answer": "pusztaság"
            },
            {
                "id": "b1-mariaterezia-01.ex05",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Milyen országgá vált Magyarország a 18. századi betelepítések következtében?",
                "options": [
                    "többnemzetiségű országgá",
                    "tengerparti királysággá",
                    "sivatagi birodalommá"
                ],
                "correct": 0
            },
            {
                "id": "b1-mariaterezia-01.ex06",
                "type": "sentence-builder",
                "category": "grammar",
                "sentence": "A szorgalmas telepesek munkája által a mezőgazdaság gyorsan fejlődött.",
                "tiles": ["A", "szorgalmas", "telepesek", "munkája", "által", "a", "mezőgazdaság", "gyorsan", "fejlődött."]
            },
            {
                "id": "b1-mariaterezia-01.ex07",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A bécsi udvar kedvező adómentességgel biztosított ____ az érkezőknek. (settlement permit)",
                "answer": "letelepedési engedélyt"
            },
            {
                "id": "b1-mariaterezia-01.ex08",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Mi jellemezte a Magyar Királyság lakosságát a 18. század végén?",
                "options": [
                    "A magyarok mellett jelentős német, szlovák, román, szerb és horvát közösségek éltek.",
                    "Csak egyetlen közös nyelvet beszéltek az egész országban.",
                    "A városokban senki sem foglalkozott kereskedelemmel."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-mariaterezia-01-ex.json", ex_01)

    ex_02 = {
        "lesson": "b1-mariaterezia-02",
        "exercises": [
            {
                "id": "b1-mariaterezia-02.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["Mária Terézia", "Maria Theresa"],
                    ["Pragmatica Sanctio", "Pragmatic Sanction (1723)"],
                    ["női trónöröklés", "female succession"],
                    ["pozsonyi országgyűlés", "Diet of Pozsony (1741)"]
                ]
            },
            {
                "id": "b1-mariaterezia-02.ex01b",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["nemesi felajánlás", "noble pledge ('Vitam et sanguinem!')"],
                    ["osztrák örökösödési háború", "War of Austrian Succession"],
                    ["uralkodónő", "female monarch"],
                    ["hűségeskü", "oath of fealty"]
                ]
            },
            {
                "id": "b1-mariaterezia-02.ex02",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Mit kiáltottak a magyar nemesek 1741-ben Pozsonyban a fiatal királynő előtt?",
                "options": [
                    "Vitam et sanguinem! (Életünket és vérünket!)",
                    "Alea iacta est! (A kocka el van vetve!)",
                    "Carpe diem! (Élj a mának!)"
                ],
                "correct": 0
            },
            {
                "id": "b1-mariaterezia-02.ex03",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "Az 1723-as ____ törvény tette lehetővé a női ági trónöröklést a Habsburg-házban. (Pragmatic Sanction)",
                "answer": "Pragmatica Sanctio"
            },
            {
                "id": "b1-mariaterezia-02.ex04",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A nemesek ünnepélyes ____ pecsételték meg szövetségüket a királynővel. (with an oath of fealty)",
                "answer": "hűségesküvel"
            },
            {
                "id": "b1-mariaterezia-02.ex05",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Melyik háború tört ki, amikor Mária Terézia elfoglalta a trónt?",
                "options": [
                    "az osztrák örökösödési háború",
                    "a napóleoni háború",
                    "a trójai háború"
                ],
                "correct": 0
            },
            {
                "id": "b1-mariaterezia-02.ex06",
                "type": "sentence-builder",
                "category": "grammar",
                "sentence": "A magyar huszárok bátor kiállása megmentette a fiatal uralkodónő birodalmát a vereségtől.",
                "tiles": ["A", "magyar", "huszárok", "bátor", "kiállása", "megmentette", "a", "fiatal", "uralkodónő", "birodalmát", "a", "vereségtől."]
            },
            {
                "id": "b1-mariaterezia-02.ex07",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A pozsonyi országgyűlésen megtett nemesi ____ után a magyar ezredek azonnal hadba vonultak. (offer / pledge)",
                "answer": "felajánlás"
            },
            {
                "id": "b1-mariaterezia-02.ex08",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Hány évig uralkodott Mária Terézia a Magyar Királyság élén?",
                "options": [
                    "Negyven évig (1740-től 1780-ig).",
                    "Mindössze két évig.",
                    "Százötven évig."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-mariaterezia-02-ex.json", ex_02)

    ex_03 = {
        "lesson": "b1-mariaterezia-03",
        "exercises": [
            {
                "id": "b1-mariaterezia-03.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["Ratio Educationis", "1777 education decree"],
                    ["Urbárium", "1767 peasant regulation"],
                    ["jobbágyvédelem", "protection of serfs"],
                    ["iskolakötelezettség", "mandatory schooling"]
                ]
            },
            {
                "id": "b1-mariaterezia-03.ex01b",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["alapfokú oktatás", "primary education"],
                    ["robot", "unpaid corvée labor"],
                    ["felvilágosult abszolutizmus", "enlightened absolutism"],
                    ["állami rendelet", "royal state decree"]
                ]
            },
            {
                "id": "b1-mariaterezia-03.ex02",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Melyik rendeletével szabályozta Mária Terézia a jobbágyok kötelezettségeit és a földesúri terheket?",
                "options": [
                    "az 1767-es Urbáriummal",
                    "az Aranybullával",
                    "a vérszerződéssel"
                ],
                "correct": 0
            },
            {
                "id": "b1-mariaterezia-03.ex03",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "Az 1777-ben kiadott ____ az egész országban egységes iskolarendszert vezetett be. (education decree)",
                "answer": "Ratio Educationis"
            },
            {
                "id": "b1-mariaterezia-03.ex04",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A törvény értelmében minden földesúr köteles volt betartani a jobbágyok jogait. (was obliged to)",
                "answer": "köteles volt"
            },
            {
                "id": "b1-mariaterezia-03.ex05",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Hogyan nevezték a jobbágyok által a földesúrnak kötelezően végzett ingyenes munkát?",
                "options": [
                    "robotnak",
                    "tizednek",
                    "bányajognak"
                ],
                "correct": 0
            },
            {
                "id": "b1-mariaterezia-03.ex06",
                "type": "sentence-builder",
                "category": "grammar",
                "sentence": "A királynő állami rendeletek útján védte a parasztokat a túlzott földesúri elnyomástól.",
                "tiles": ["A", "királynő", "állami", "rendeletek", "útján", "védte", "a", "parasztokat", "a", "túlzott", "földesúri", "elnyomástól."]
            },
            {
                "id": "b1-mariaterezia-03.ex07",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A Ratio Educationis előírta az általános ____ hat és tizenkét éves kor között. (compulsory schooling)",
                "answer": "iskolakötelezettséget"
            },
            {
                "id": "b1-mariaterezia-03.ex08",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Mi volt Mária Terézia felvilágosult abszolutizmusának legfőbb politikai célja?",
                "options": [
                    "A birodalom modernizálása, a gazdaság erősítése és az adófizető jobbágyság védelme.",
                    "Minden iskola bezárása az országban.",
                    "A városok felégetése és lerombolása."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-mariaterezia-03-ex.json", ex_03)

    ex_04 = {
        "lesson": "b1-mariaterezia-04",
        "exercises": [
            {
                "id": "b1-mariaterezia-04.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["II. József", "Joseph II"],
                    ["kalapos király", "the 'hatted king'"],
                    ["türelmi rendelet", "Edict of Tolerance (1781)"],
                    ["nyelvrendelet", "Language Edict (1784)"]
                ]
            },
            {
                "id": "b1-mariaterezia-04.ex01b",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["német hivatalos nyelv", "German official language"],
                    ["Szent Korona elszállítása", "removal of Holy Crown"],
                    ["rendeleti kormányzás", "governance by decree"],
                    ["halálos ágy", "deathbed"]
                ]
            },
            {
                "id": "b1-mariaterezia-04.ex02",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Miért nevezték II. Józsefet kalapos királynak a magyarok?",
                "options": [
                    "Mert nem koronáztatta meg magát a Szent Koronával, nehogy esküt kelljen tennie az alkotmányra.",
                    "Mert divattervezőként dolgozott Párizsban.",
                    "Mert kalapgyárat alapított Pozsonyban."
                ],
                "correct": 0
            },
            {
                "id": "b1-mariaterezia-04.ex03",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "Az 1781-es ____ lehetővé tette a protestánsok számára a szabad vallásgyakorlást és a hivatalviselést. (edict of tolerance)",
                "answer": "türelmi rendelet"
            },
            {
                "id": "b1-mariaterezia-04.ex04",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A heves nemesi tiltakozás ellenére a császár bevezette a német nyelvet. (in spite of / despite)",
                "answer": "ellenére"
            },
            {
                "id": "b1-mariaterezia-04.ex05",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit rendelt el II. József az 1784-es nyelvrendeletben?",
                "options": [
                    "Hogy a latin helyett a német legyen a hivatalos államnyelv a közigazgatásban.",
                    "Hogy mindenki csak franciául beszélhet.",
                    "Hogy tilos könyveket nyomtatni."
                ],
                "correct": 0
            },
            {
                "id": "b1-mariaterezia-04.ex06",
                "type": "sentence-builder",
                "category": "grammar",
                "sentence": "II. József a halálos ágyán a türelmi rendelet kivételével minden rendeletét visszavonta.",
                "tiles": ["II.", "József", "a", "halálos", "ágyán", "a", "türelmi", "rendelet", "kivételével", "minden", "rendeletét", "visszavonta."]
            },
            {
                "id": "b1-mariaterezia-04.ex07",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A nemesség mélységesen felháborodott, amikor megtörtént a ____ Bécsbe. (removal of the Holy Crown)",
                "answer": "Szent Korona elszállítása"
            },
            {
                "id": "b1-mariaterezia-04.ex08",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Mit tett a halálos ágyán II. József 1790-ben?",
                "options": [
                    "Visszavonta szinte az összes magyarországi rendeletét, és visszaküldte Budára a Szent Koronát.",
                    "Újabb háborút indított Oroszország ellen.",
                    "Eladta az országházat a franciáknak."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-mariaterezia-04-ex.json", ex_04)

    ex_05 = {
        "lesson": "b1-mariaterezia-05",
        "exercises": [
            {
                "id": "b1-mariaterezia-05.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["nemzeti ébredés", "national awakening"],
                    ["anyanyelvi mozgalom", "mother-tongue movement"],
                    ["Bessenyei György", "Enlightenment writer & guard"],
                    ["irodalmi élet", "literary life"]
                ]
            },
            {
                "id": "b1-mariaterezia-05.ex01b",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["nemesi ellenállás", "noble resistance"],
                    ["hagyománytisztelet", "respect for tradition"],
                    ["nemzeti öntudat", "national self-awareness"],
                    ["felvilágosodás", "the Enlightenment"]
                ]
            },
            {
                "id": "b1-mariaterezia-05.ex02",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Ki volt Bessenyei György, és mi volt híres jelmondata a magyar nyelvről?",
                "options": [
                    "Bécsi magyar testőr és író: 'Minden nemzet a maga nyelvén lett tudós'.",
                    "Osztrák zeneszerző Bécsben.",
                    "Török hadvezér Budán."
                ],
                "correct": 0
            },
            {
                "id": "b1-mariaterezia-05.ex03",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A német nyelvrendelet ellen kibontakozó nemesi ____ felébresztette a nemzetet. (resistance)",
                "answer": "ellenállás"
            },
            {
                "id": "b1-mariaterezia-05.ex04",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Az írók kitartó munkája révén felvirágzott a magyar irodalmi élet. (flourished)",
                "answer": "felvirágzott"
            },
            {
                "id": "b1-mariaterezia-05.ex05",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mi a neve annak a 18. század végi eszmei folyamatnak, amely a nemzeti kultúra és nyelv megújítását célozta?",
                "options": [
                    "nemzeti ébredés",
                    "török hódoltság",
                    "tatárjárás"
                ],
                "correct": 0
            },
            {
                "id": "b1-mariaterezia-05.ex06",
                "type": "sentence-builder",
                "category": "grammar",
                "sentence": "A felvilágosodás eszméi és a nemzeti öntudat megerősödése elvezetett a reformkor hajnalához.",
                "tiles": ["A", "felvilágosodás", "eszméi", "és", "a", "nemzeti", "öntudat", "megerősödése", "elvezetett", "a", "reformkor", "hajnalához."]
            },
            {
                "id": "b1-mariaterezia-05.ex07",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A magyar írók elindították a történelmi jelentőségű ____ a nyelv megújításáért. (mother-tongue movement)",
                "answer": "anyanyelvi mozgalmat"
            },
            {
                "id": "b1-mariaterezia-05.ex08",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Hogyan kapcsolódik a 18. század végi szellemi mozgalom a későbbi 19. századi reformkorhoz?",
                "options": [
                    "Közvetlen előzménye volt: megteremtette az anyanyelv, a sajtó és a polgárosodás szilárd alapjait.",
                    "Semmilyen kapcsolatban nem állt vele.",
                    "Megakadályozta a reformkor kibontakozását."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-mariaterezia-05-ex.json", ex_05)

    ex_consolidation = {
        "lesson": "b1-mariaterezia-consolidation",
        "exercises": [
            {
                "id": "b1-mariaterezia-consolidation.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["Mária Terézia", "reigning queen 1740-1780"],
                    ["Urbárium", "peasant protection decree 1767"],
                    ["Ratio Educationis", "education regulation 1777"],
                    ["kalapos király", "Joseph II (1780-1790)"]
                ]
            },
            {
                "id": "b1-mariaterezia-consolidation.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik mondat alkalmazza helyesen az 'által' névutót?",
                "options": [
                    "A Mária Terézia által kibocsátott rendeletek megvédték a jobbágyokat.",
                    "A rendeletek által királynő volt jóakaró.",
                    "Általa rendeletnek a királyi hatalom nőtt."
                ],
                "correct": 0
            },
            {
                "id": "b1-mariaterezia-consolidation.ex03",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A pozsonyi nemesség híres felkiáltása: Vitam et ____! (and blood)",
                "answer": "sanguinem"
            },
            {
                "id": "b1-mariaterezia-consolidation.ex04",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A reformok ____ az ország gazdasága gyors fejlődésnek indult. (through / by means of)",
                "answer": "révén"
            },
            {
                "id": "b1-mariaterezia-consolidation.ex05",
                "type": "sentence-builder",
                "category": "grammar",
                "sentence": "A nemzeti ébredés eszméi megerősítették a magyar nyelv és irodalom pozícióját a társadalomban.",
                "tiles": ["A", "nemzeti", "ébredés", "eszméi", "megerősítették", "a", "magyar", "nyelv", "és", "irodalom", "pozícióját", "a", "társadalomban."]
            },
            {
                "id": "b1-mariaterezia-consolidation.ex06",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Melyik rendelet biztosított szabad vallásgyakorlást a protestánsoknak 1781-ben?",
                "options": [
                    "a türelmi rendelet",
                    "az Aranybulla",
                    "a vérszerződés"
                ],
                "correct": 0
            },
            {
                "id": "b1-mariaterezia-consolidation.ex07",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A betelepítések révén érkező német ajkú ____ virágzó falvakat építettek. (Swabians)",
                "answer": "svábok"
            },
            {
                "id": "b1-mariaterezia-consolidation.ex08",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Milyen kérdés hangozhat el a magyar állampolgársági interjún Mária Teréziáról és koráról?",
                "options": [
                    "Kik voltak a 18. századi felvilágosult abszolutizmus legfontosabb uralkodói és milyen reformokat hoztak?",
                    "Melyik budapesti moziban vetítették Mária Terézia első filmjét?",
                    "Mikor nyert II. József teniszbajnokságot?"
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-mariaterezia-consolidation-ex.json", ex_consolidation)

    # -------------------------------------------------------------------------
    # 5. Lesson Files (01 to 05 + consolidation)
    # -------------------------------------------------------------------------
    lesson_titles = {
        "01": ("Az ország újranépesítése a 18. században", "Repopulating the Country"),
        "02": ("Mária Terézia és az 1741-es pozsonyi országgyűlés", "Maria Theresa & Hungary"),
        "03": ("Felvilágosult reformok: Urbárium és Ratio Educationis", "Enlightenment Reforms"),
        "04": ("II. József, a kalapos király és rendeletei", "Joseph II's Controversial Rule"),
        "05": ("Nemzeti ébredés és a magyar nyelv mozgalma", "A Country Recovering")
    }

    story_refs = {
        "01": "stories/world/b1/b1-mariaterezia-01-telepesek.json",
        "02": "stories/world/b1/b1-mariaterezia-02-uralkodono.json",
        "03": "stories/world/b1/b1-mariaterezia-03-reformok.json",
        "04": "stories/world/b1/b1-mariaterezia-04-kalaposkiraly.json",
        "05": "stories/world/b1/b1-mariaterezia-05-ebredes.json"
    }

    for i in range(1, 6):
        padded = f"0{i}"
        hu_t, en_t = lesson_titles[padded]
        lesson_obj = {
            "id": f"lesson.b1.mariaterezia-{padded}",
            "title": f"{hu_t} ({en_t})",
            "level": "B1",
            "grammar": "Postpositions of Instrumentality (által, révén) and Enlightened Reforms",
            "sections": [
                {
                    "type": "goal",
                    "title": "Lesson Goals",
                    "items": [
                        f"I can discuss the events and figures of {en_t}.",
                        "I can use postpositions (által, révén) to explain methods and causes.",
                        "I can understand key concepts tested in the Hungarian naturalization interview.",
                        "I can master eight new vocabulary items related to 18th-century rebuilding."
                    ]
                },
                {"type": "recycle", "count": 3},
                {"type": "story", "ref": story_refs[padded]},
                {"type": "vocabulary", "ref": f"vocabulary/b1/b1-mariaterezia-{padded}-voc.json"},
                {"type": "grammar", "ref": f"grammar/b1/b1-mariaterezia-{padded}-gr.json"},
                {
                    "type": "exercise-group",
                    "title": "Practice",
                    "ref": f"exercises/b1/b1-mariaterezia-{padded}-ex.json",
                    "exerciseRefs": [
                        f"b1-mariaterezia-{padded}.ex01",
                        f"b1-mariaterezia-{padded}.ex01b",
                        f"b1-mariaterezia-{padded}.ex02",
                        f"b1-mariaterezia-{padded}.ex03",
                        f"b1-mariaterezia-{padded}.ex04",
                        f"b1-mariaterezia-{padded}.ex05",
                        f"b1-mariaterezia-{padded}.ex06",
                        f"b1-mariaterezia-{padded}.ex07",
                        f"b1-mariaterezia-{padded}.ex08"
                    ]
                }
            ]
        }
        write_json(f"content/hu/lessons/b1/b1-mariaterezia-{padded}.json", lesson_obj)

    consolidation_obj = {
        "id": "lesson.b1.mariaterezia-consolidation",
        "title": "A 18. század: újjáépítés és felvilágosodás összefoglalása (Unit 14 Consolidation)",
        "level": "B1",
        "grammar": "Synthesis: Enlightened Absolutism & National Awakening",
        "sections": [
            {
                "type": "goal",
                "title": "Consolidation Goals",
                "items": [
                    "I can synthesize 18th-century repopulation, Maria Theresa's reforms, and Joseph II's reign.",
                    "I can confidently answer Hungarian citizenship questions on Maria Theresa and the Enlightenment.",
                    "I can review and apply all 40 unit vocabulary items and instrumental structures."
                ]
            },
            {"type": "story", "ref": "stories/world/b1/b1-mariaterezia.json"},
            {
                "type": "exercise-group",
                "title": "Consolidation Practice",
                "ref": "exercises/b1/b1-mariaterezia-consolidation-ex.json",
                "exerciseRefs": [
                    "b1-mariaterezia-consolidation.ex01",
                    "b1-mariaterezia-consolidation.ex02",
                    "b1-mariaterezia-consolidation.ex03",
                    "b1-mariaterezia-consolidation.ex04",
                    "b1-mariaterezia-consolidation.ex05",
                    "b1-mariaterezia-consolidation.ex06",
                    "b1-mariaterezia-consolidation.ex07",
                    "b1-mariaterezia-consolidation.ex08"
                ]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-mariaterezia-consolidation.json", consolidation_obj)
    print("Successfully built Hungarian B1 Citizenship Unit 14 (b1-mariaterezia)!")

if __name__ == "__main__":
    build_unit_14_citizenship()
