#!/usr/bin/env python3
"""Generate Hungarian B1 Citizenship Unit 13: Rákóczi's War of Independence (b1-rakoczi)."""

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

def build_unit_13_citizenship():
    # -------------------------------------------------------------------------
    # 1. Vocabulary Files (8 words each = 40 words total)
    # -------------------------------------------------------------------------
    voc_01 = {
        "id": "vocab.b1.rakoczi.01",
        "lesson": "b1-rakoczi-01",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "vezérlő fejedelem", "translation": "ruling prince, leader of the confederation", "pos": "noun"},
            {"lemma": "Brezáni kiáltvány", "translation": "Brezán proclamation", "pos": "noun"},
            {"lemma": "nemesi származás", "translation": "noble descent, ancestry", "pos": "noun"},
            {"lemma": "birtokelkobzás", "translation": "confiscation of estates", "pos": "noun"},
            {"lemma": "fegyverbe szólít", "translation": "to call to arms", "pos": "verb"},
            {"lemma": "jobbágyság", "translation": "serfdom, peasant class", "pos": "noun"},
            {"lemma": "szabadságvágy", "translation": "yearning for freedom", "pos": "noun"},
            {"lemma": "jelmondat", "translation": "motto, slogan", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-rakoczi-01-voc.json", voc_01)

    voc_02 = {
        "id": "vocab.b1.rakoczi.02",
        "lesson": "b1-rakoczi-02",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "kuruc felkelés", "translation": "Kuruc uprising", "pos": "noun"},
            {"lemma": "labanc", "translation": "Labanc (pro-Habsburg imperial soldier)", "pos": "noun"},
            {"lemma": "könnyűlovasság", "translation": "light cavalry", "pos": "noun"},
            {"lemma": "tárogató", "translation": "tárogató (traditional wooden horn)", "pos": "noun"},
            {"lemma": "zászlóbontás", "translation": "unfurling the banner of revolt", "pos": "noun"},
            {"lemma": "hadjárat", "translation": "military campaign", "pos": "noun"},
            {"lemma": "felszabadított terület", "translation": "liberated territory", "pos": "noun"},
            {"lemma": "hadviselés", "translation": "conduct of war, warfare", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-rakoczi-02-voc.json", voc_02)

    voc_03 = {
        "id": "vocab.b1.rakoczi.03",
        "lesson": "b1-rakoczi-03",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "ónodi országgyűlés", "translation": "Diet of Ónód (1707)", "pos": "noun"},
            {"lemma": "trónfosztás", "translation": "dethronement, detronization", "pos": "noun"},
            {"lemma": "közteherviselés", "translation": "universal taxation, public burden sharing", "pos": "noun"},
            {"lemma": "nemesi adózás", "translation": "taxation of nobility", "pos": "noun"},
            {"lemma": "rézpénz", "translation": "copper money, libertás coin", "pos": "noun"},
            {"lemma": "infláció", "translation": "inflation, currency devaluation", "pos": "noun"},
            {"lemma": "trencséni csata", "translation": "Battle of Trencsén (1708)", "pos": "noun"},
            {"lemma": "hadi szerencse", "translation": "fortune of war", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-rakoczi-03-voc.json", voc_03)

    voc_04 = {
        "id": "vocab.b1.rakoczi.04",
        "lesson": "b1-rakoczi-04",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "szatmári béke", "translation": "Peace of Szatmár (1711)", "pos": "noun"},
            {"lemma": "amnesztia", "translation": "general amnesty, pardon", "pos": "noun"},
            {"lemma": "alku", "translation": "compromise, negotiated bargain", "pos": "noun"},
            {"lemma": "Károlyi Sándor", "translation": "Count Sándor Károlyi", "pos": "noun"},
            {"lemma": "zászlók letétele", "translation": "laying down of banners / arms", "pos": "noun"},
            {"lemma": "alkotmányos rend", "translation": "constitutional order", "pos": "noun"},
            {"lemma": "rendi jogok", "translation": "estate rights and liberties", "pos": "noun"},
            {"lemma": "megbékélés", "translation": "reconciliation, pacification", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-rakoczi-04-voc.json", voc_04)

    voc_05 = {
        "id": "vocab.b1.rakoczi.05",
        "lesson": "b1-rakoczi-05",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "rodostói emigráció", "translation": "exile at Rodostó", "pos": "noun"},
            {"lemma": "Mikes Kelemen", "translation": "Kelemen Mikes", "pos": "noun"},
            {"lemma": "törökországi levelek", "translation": "Letters from Turkey", "pos": "noun"},
            {"lemma": "hűség", "translation": "loyalty, fidelity", "pos": "noun"},
            {"lemma": "nemzeti függetlenség", "translation": "national independence", "pos": "noun"},
            {"lemma": "szabadsághős", "translation": "hero of freedom", "pos": "noun"},
            {"lemma": "nemzeti himnusz", "translation": "national anthem", "pos": "noun"},
            {"lemma": "történelmi emlékezet", "translation": "historical memory", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-rakoczi-05-voc.json", voc_05)

    # -------------------------------------------------------------------------
    # 2. Grammar Files
    # -------------------------------------------------------------------------
    gr_01 = {
        "id": "grammar.b1.rakoczi.01.past-conditional-volna",
        "title": "The Past Conditional with volna: Expressing Historical Alternatives",
        "sections": [
            {
                "type": "text",
                "title": "Forming the Past Conditional in Hungarian",
                "content": "To express past unfulfilled events ('would have happened'), Hungarian combines the regular past tense verb with the invariant auxiliary *volna*: *Ha a fejedelem nem küzdött volna, a nemzet elveszett volna.* ('If the prince had not fought, the nation would have been lost.')."
            },
            {
                "type": "examples",
                "title": "Past conditional examples",
                "items": [
                    {
                        "spanish": "Ha a császár nem növelte volna az adókat, nem tört volna ki a felkelés.",
                        "english": "If the emperor had not raised taxes, the uprising would not have broken out."
                    },
                    {
                        "spanish": "A nemesség nem fogadta volna el a békét biztosítékok nélkül.",
                        "english": "The nobility would not have accepted the peace without guarantees."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-rakoczi-01-gr.json", gr_01)

    gr_02 = {
        "id": "grammar.b1.rakoczi.02.unfulfilled-conditions",
        "title": "Complex Counterfactual Conditionals: ha... akkor... volna",
        "sections": [
            {
                "type": "text",
                "title": "Hypothetical Scenarios in Historical Analysis",
                "content": "In analyzing historical turning points, use *ha + past + volna*, followed by *akkor + past + volna*: *Ha a kurucok fegyelmezettebbek lettek volna, akkor megnyerték volna a trencséni csatát.* ('If the Kurucs had been more disciplined, they would have won the battle of Trencsén.')."
            },
            {
                "type": "examples",
                "title": "Counterfactual conditionals",
                "items": [
                    {
                        "spanish": "Ha Franciaország több pénzt küldött volna, a szabadságharc tovább tartott volna.",
                        "english": "If France had sent more funds, the war of independence would have lasted longer."
                    },
                    {
                        "spanish": "A jobbágyok nem harcoltak volna, ha nem bíztak volna a fejedelemben.",
                        "english": "The serfs would not have fought if they had not trusted the prince."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-rakoczi-02-gr.json", gr_02)

    gr_03 = {
        "id": "grammar.b1.rakoczi.03.concessive-clauses-habar",
        "title": "Concessive Clauses in Military History: habár, jóllehet, annak dacára",
        "sections": [
            {
                "type": "text",
                "title": "Balancing Triumphs and Setbacks",
                "content": "Historical narratives use formal concessive conjunctions: *habár / jóllehet* (although, even though), *annak dacára, hogy...* (despite the fact that): *Jóllehet a sereg vereséget szenvedett, a nemzet nem adta fel a küzdelmet.*"
            },
            {
                "type": "examples",
                "title": "Concessive clauses",
                "items": [
                    {
                        "spanish": "Habár a kurucok elfoglalták az ország nagy részét, a várakat nehezen tudták bevenni.",
                        "english": "Although the Kurucs occupied most of the country, they could capture the fortresses only with difficulty."
                    },
                    {
                        "spanish": "Annak dacára, hogy a rézpénz elértéktelenedett, az ónodi gyűlésen kimondták a trónfosztást.",
                        "english": "Despite the fact that the copper coin devalued, they declared the dethronement at the Ónód Diet."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-rakoczi-03-gr.json", gr_03)

    gr_04 = {
        "id": "grammar.b1.rakoczi.04.diplomatic-compromise",
        "title": "Expressing Compromise & Resolution: megállapodás születik, elfogad, garantál",
        "sections": [
            {
                "type": "text",
                "title": "Verbal Expressions of Political Settlements",
                "content": "Diplomatic treaties rely on set phrases: *megállapodás születik* (an agreement is born/reached), *amnesztiát biztosít* (grants amnesty), *garantálja a jogokat* (guarantees the rights), *leteszik a fegyvert* (lay down arms)."
            },
            {
                "type": "examples",
                "title": "Compromise expressions",
                "items": [
                    {
                        "spanish": "A szatmári síkon megállapodás született, amely lezárta a nyolcéves háborút.",
                        "english": "On the plain of Szatmár an agreement was reached that brought the eight-year war to an end."
                    },
                    {
                        "spanish": "A bécsi udvar garantálta, hogy a nemesség megtarthatja ősi kiváltságait.",
                        "english": "The Viennese court guaranteed that the nobility could retain its ancestral privileges."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-rakoczi-04-gr.json", gr_04)

    gr_05 = {
        "id": "grammar.b1.rakoczi.05.historical-legacy",
        "title": "Expressing Lasting Legacy & Reverence: méltán tekintenek rá, örök emléket állít",
        "sections": [
            {
                "type": "text",
                "title": "Memorial Discourse in Hungarian",
                "content": "To describe national heroes and memory, Hungarian uses elevated commemorative phrases: *méltán tekintenek rá mint...* (they rightly regard him as...), *örök emléket állít* (erects an eternal memorial to), *tisztelet övezi* (is surrounded by reverence)."
            },
            {
                "type": "examples",
                "title": "Memorial discourse",
                "items": [
                    {
                        "spanish": "A magyar utókor méltán tekinti Rákóczit a nemzeti önrendelkezés jelképének.",
                        "english": "Hungarian posterity rightly regards Rákóczi as the symbol of national self-determination."
                    },
                    {
                        "spanish": "Mikes Kelemen hűsége és irodalmi műve örök emléket állított a bujdosóknak.",
                        "english": "Kelemen Mikes's loyalty and literary work erected an eternal monument to the exiles."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-rakoczi-05-gr.json", gr_05)

    # -------------------------------------------------------------------------
    # 3. World Stories (01 to 05 + Omnibus) in TRIH Narrative Style
    # -------------------------------------------------------------------------
    stories_content = {
        "b1-rakoczi-01-vezérlo.json": [
            "Hogyan válik a leggazdagabb magyar főnemes a szegény jobbágyok bálványozott vezérévé? Ez Rákóczi életének nagy rejtélye.",
            "II. Rákóczi Ferenc büszke nemesi származás örököse volt, de Bécsben nevelték fel, távol hazájától.",
            "Amikor hazatért, látta a nép nyomorát és a jogtalan birtokelkobzás súlyos sebeit.",
            "1703-ban a lengyelországi Brezán várából a Brezáni kiáltvány üzenetével bátor fegyverbe szólít lépést tett.",
            "Zászlajára arany betűkkel írta a jelmondat szavait: Cum Deo pro Patria et Libertate! A jobbágyság égő szabadságvágy érzése azonnal mellé állította a népet mint vezérlő fejedelem mögé."
        ],
        "b1-rakoczi-02-kurucok.json": [
            "Képzeljük el a tavaszi síkságot, ahol a lovasok kürtje, a tárogató hangja zengi be a hajnalt! Kik voltak a kurucok?",
            "Megkezdődött a dicsőséges kuruc felkelés a császárhű labanc csapatok kíméletlen elnyomása ellen.",
            "A zászlóbontás hírére ezrek sereglettek Rákóczi zászlaja alá a hegyekből és a falvakból.",
            "A villámgyors magyar könnyűlovasság meglepetésszerű hadviselés módszerével sorra nyerte az összecsapásokat.",
            "A diadalmas hadjárat eredményeként rövid idő alatt hatalmas felszabadított terület került a felkelők kezére."
        ],
        "b1-rakoczi-03-onod.json": [
            "1707 nyarán az ónodi országgyűlés viharos sátraiban sorsdöntő és drámai döntés született. Meddig mehet el egy felkelés?",
            "A rendek ünnepélyesen kimondták a Habsburg-ház trónfosztás határozatát: az ország nem ismer el többé bécsi királyt.",
            "Rákóczi bevezette a forradalmi közteherviselés elvét, amely szerint a nemesi adózás is kötelezővé vált a hadsereg fenntartására.",
            "A háború költségeire kibocsátott rézpénz értéke azonban gyorsan csökkent, és a pusztító infláció elégedetlenséget szült.",
            "Amikor az 1708-as trencséni csata magyar vereséggel végződött, a hadiszerencse végleg elpártolt a fejedelem mellől."
        ],
        "b1-rakoczi-04-szatmar.json": [
            "1711 tavaszán a majtényi síkon csend borult a csatamezőre. Hogyan zárulhat le békével egy nyolcéves véres szabadságharc?",
            "Károlyi Sándor gróf nehéz tárgyalások után elfogadta a császári udvar ajánlatát, mert nem maradt más reális kiút.",
            "Megszületett a történelmi szatmári béke, amely teljes körű amnesztia ígéretét biztosította minden felkelőnek.",
            "A zászlók letétele után helyreállt a törvényes alkotmányos rend, és a nemesség megőrizte ősi rendi jogok kiváltságait.",
            "Bár Rákóczi személyesen nem fogadta el a feltételeket, ez az okos alku és megbékélés megmentette Magyarországot a megsemmisüléstől."
        ],
        "b1-rakoczi-05-emlekezet.json": [
            "A fejedelem soha nem kért kegyelmet a császártól. Hová vezetett a büszke magyar szabadsághős száműzetése?",
            "A rodostói emigráció csendes törökországi tengerpartján Rákóczi mindvégig méltósággal és hittel viselte a magányt.",
            "Hűséges apródja, Mikes Kelemen csodálatos irodalmi műben, a Törökországi levelek lapjain örökítette meg a bujdosók életét.",
            "A fejedelem iránti rendíthetetlen hűség és a nemzeti függetlenség eszméje generációkon át élt a nép lelkében.",
            "Rákóczi neve örökre bekerült a történelmi emlékezet kincstárába, mint akit Kölcsey is megénekelt, amikor megszületett a nemzeti himnusz."
        ],
        "b1-rakoczi.json": [
            "1703-ban II. Rákóczi Ferenc a Brezáni kiáltvánnyal fegyverbe szólította a nemzetet a Habsburg elnyomás ellen.",
            "A kuruc könnyűlovasság a tárogató szavára gyors sikereket aratott, és felszabadította az ország jelentős részét.",
            "Az 1707-es ónodi gyűlésen kimondták a Habsburgok trónfosztását, de a gazdasági nehézségek és az infláció felőrölték az erőt.",
            "1711-ben a szatmári béke amnesztiát adott és biztosította a magyar rendi jogokat, lezárva a nyolcéves küzdelmet.",
            "Rákóczi a rodostói emigrációba vonult, és alakja a magyar szabadságvágy és hűség halhatatlan jelképévé vált."
        ]
    }

    write_json("content/hu/stories/world/b1/b1-rakoczi-01-vezerlo.json", {
        "id": "story.b1.rakoczi.01",
        "title": "II. Rákóczi Ferenc és a Brezáni kiáltvány",
        "level": "B1",
        "lesson": 1,
        "order": 1,
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "How Prince Ferenc Rákóczi II, the wealthiest landowner in Hungary, answered the call of the peasants and launched the war of independence from Brezán Castle in 1703.",
        "characters": ["II. Rákóczi Ferenc", "Esze Tamás"],
        "location": "Brezán, Munkács",
        "paragraphs": [{"type": "narration", "text": t} for t in stories_content["b1-rakoczi-01-vezérlo.json"]]
    })

    write_json("content/hu/stories/world/b1/b1-rakoczi-02-kurucok.json", {
        "id": "story.b1.rakoczi.02",
        "title": "A kurucok felkelése és hadviselése",
        "level": "B1",
        "lesson": 2,
        "order": 2,
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "The rapid spread of the Kuruc uprising, light cavalry tactics, the melancholy music of the tárogató, and the liberation of Hungarian territories from the Labanc troops.",
        "characters": ["II. Rákóczi Ferenc", "Vak Bottyán"],
        "location": "Felvidék, Alföld",
        "paragraphs": [{"type": "narration", "text": t} for t in stories_content["b1-rakoczi-02-kurucok.json"]]
    })

    write_json("content/hu/stories/world/b1/b1-rakoczi-03-onod.json", {
        "id": "story.b1.rakoczi.03",
        "title": "Az ónodi országgyűlés és a trónfosztás",
        "level": "B1",
        "lesson": 3,
        "order": 3,
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "The dramatic 1707 Diet of Ónód: declaring the dethronement of the Habsburgs, introducing taxation for nobles, copper money inflation, and the turn of military fortune at Trencsén.",
        "characters": ["II. Rákóczi Ferenc", "Bercsényi Miklós"],
        "location": "Ónód, Trencsén",
        "paragraphs": [{"type": "narration", "text": t} for t in stories_content["b1-rakoczi-03-onod.json"]]
    })

    write_json("content/hu/stories/world/b1/b1-rakoczi-04-szatmar.json", {
        "id": "story.b1.rakoczi.04",
        "title": "A szatmári béke és a megbékélés",
        "level": "B1",
        "lesson": 4,
        "order": 4,
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "The 1711 Peace of Szatmár: Count Sándor Károlyi negotiates an honorable compromise that preserves Hungarian constitutional rights and gives general amnesty.",
        "characters": ["Károlyi Sándor", "Pálffy János"],
        "location": "Szatmár, Majtényi sík",
        "paragraphs": [{"type": "narration", "text": t} for t in stories_content["b1-rakoczi-04-szatmar.json"]]
    })

    write_json("content/hu/stories/world/b1/b1-rakoczi-05-emlekezet.json", {
        "id": "story.b1.rakoczi.05",
        "title": "Rodostó és a nemzeti emlékezet",
        "level": "B1",
        "lesson": 5,
        "order": 5,
        "type": "world",
        "estimatedMinutes": 6,
        "summary": "Rákóczi's dignified exile in the Turkish town of Rodostó, Kelemen Mikes's famous letters, and how Rákóczi's memory became an eternal pillar of Hungarian patriotism.",
        "characters": ["II. Rákóczi Ferenc", "Mikes Kelemen"],
        "location": "Rodostó, Tekirdağ",
        "paragraphs": [{"type": "narration", "text": t} for t in stories_content["b1-rakoczi-05-emlekezet.json"]]
    })

    write_json("content/hu/stories/world/b1/b1-rakoczi.json", {
        "id": "story.b1.rakoczi",
        "title": "A Rákóczi-szabadságharc (1703–1711)",
        "level": "B1",
        "order": 13,
        "type": "world",
        "estimatedMinutes": 8,
        "summary": "The complete historical saga of Rákóczi's War of Independence: from the Brezán proclamation to the Diet of Ónód, the Szatmár compromise, and the immortal exile at Rodostó.",
        "characters": ["II. Rákóczi Ferenc", "Mikes Kelemen", "Károlyi Sándor"],
        "location": "Magyarország, Rodostó",
        "paragraphs": [{"type": "narration", "text": t} for t in stories_content["b1-rakoczi.json"]]
    })

    # -------------------------------------------------------------------------
    # 4. Exercises Files (01 to 05 + consolidation)
    # -------------------------------------------------------------------------
    ex_01 = {
        "lesson": "b1-rakoczi-01",
        "exercises": [
            {
                "id": "b1-rakoczi-01.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["vezérlő fejedelem", "ruling prince / leader"],
                    ["Brezáni kiáltvány", "Brezán proclamation"],
                    ["szabadságvágy", "yearning for freedom"],
                    ["jelmondat", "motto / slogan"]
                ]
            },
            {
                "id": "b1-rakoczi-01.ex01b",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["nemesi származás", "noble ancestry"],
                    ["birtokelkobzás", "confiscation of estates"],
                    ["fegyverbe szólít", "to call to arms"],
                    ["jobbágyság", "serfdom / peasant class"]
                ]
            },
            {
                "id": "b1-rakoczi-01.ex02",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Milyen jelmondatot íratott Rákóczi a felkelők zászlajára?",
                "options": [
                    "Cum Deo pro Patria et Libertate! (Istennel a hazáért és a szabadságért!)",
                    "Regnum Mariae (Mária országa)",
                    "Veni, vidi, vici (Jöttem, láttam, győztem)"
                ],
                "correct": 0
            },
            {
                "id": "b1-rakoczi-01.ex03",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Ha Rákóczi nem állt volna az élre, nem tört volna ki a felkelés. (would have broken out)",
                "answer": "tört volna"
            },
            {
                "id": "b1-rakoczi-01.ex04",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "1703-ban a fejedelem a híres ____ szólította hadba a magyar népet. (proclamation)",
                "answer": "Brezáni kiáltvánnyal"
            },
            {
                "id": "b1-rakoczi-01.ex05",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Melyik tisztséget viselte Rákóczi a szabadságharc élén?",
                "options": [
                    "vezérlő fejedelem",
                    "római császár",
                    "budai pasa"
                ],
                "correct": 0
            },
            {
                "id": "b1-rakoczi-01.ex06",
                "type": "sentence-builder",
                "category": "grammar",
                "sentence": "Ha a bécsi udvar nem vett volna el minden birtokot, kevesebb lett volna az elégedetlen ember.",
                "tiles": ["Ha", "a", "bécsi", "udvar", "nem", "vett", "volna", "el", "minden", "birtokot,", "kevesebb", "lett", "volna", "az", "elégedetlen", "ember."]
            },
            {
                "id": "b1-rakoczi-01.ex07",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A népet nem a pénz, hanem a mély ____ hajtotta a csatába. (desire for freedom)",
                "answer": "szabadságvágy"
            },
            {
                "id": "b1-rakoczi-01.ex08",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Honnan bocsátotta ki Rákóczi a híres kiáltványát?",
                "options": [
                    "A lengyelországi Brezán várából.",
                    "A budai várból.",
                    "A bécsi császári palotából."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-rakoczi-01-ex.json", ex_01)

    ex_02 = {
        "lesson": "b1-rakoczi-02",
        "exercises": [
            {
                "id": "b1-rakoczi-02.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["kuruc felkelés", "Kuruc uprising"],
                    ["labanc", "pro-Habsburg soldier"],
                    ["könnyűlovasság", "light cavalry"],
                    ["tárogató", "tárogató horn"]
                ]
            },
            {
                "id": "b1-rakoczi-02.ex01b",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["zászlóbontás", "raising banner of revolt"],
                    ["hadjárat", "military campaign"],
                    ["felszabadított terület", "liberated territory"],
                    ["hadviselés", "conduct of warfare"]
                ]
            },
            {
                "id": "b1-rakoczi-02.ex02",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Hogyan nevezték a császárhű, osztrák oldalon harcoló katonákat?",
                "options": [
                    "labancoknak",
                    "hajdúknak",
                    "janicsároknak"
                ],
                "correct": 0
            },
            {
                "id": "b1-rakoczi-02.ex03",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A kuruc táborokban este bús hangon szólalt meg a fából készült ____. (traditional horn)",
                "answer": "tárogató"
            },
            {
                "id": "b1-rakoczi-02.ex04",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A kurucok győztek volna, ha a várak jobban fel lettek ____ szerelve. (had been equipped)",
                "answer": "volna"
            },
            {
                "id": "b1-rakoczi-02.ex05",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Melyik fegyvernem jellemezte a leginkább a kuruc hadsereget?",
                "options": [
                    "a gyors könnyűlovasság",
                    "a nehéztüzérség",
                    "a páncélos hadihajók"
                ],
                "correct": 0
            },
            {
                "id": "b1-rakoczi-02.ex06",
                "type": "sentence-builder",
                "category": "grammar",
                "sentence": "A kuruc könnyűlovasság gyors mozgással zavarta meg a nehézkes labanc sereget.",
                "tiles": ["A", "kuruc", "könnyűlovasság", "gyors", "mozgással", "zavarta", "meg", "a", "nehézkes", "labanc", "sereget."]
            },
            {
                "id": "b1-rakoczi-02.ex07",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A sikeres tavaszi ____ után a kurucok bekerítették a fontos várakat. (campaign)",
                "answer": "hadjárat"
            },
            {
                "id": "b1-rakoczi-02.ex08",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Mi történt a tiszaháti zászlóbontás után?",
                "options": [
                    "Rövid idő alatt a magyar föld jelentős része felszabadított terület lett.",
                    "A kurucok azonnal letették a fegyvert a császár előtt.",
                    "Rákóczi visszament Franciaországba tanulni."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-rakoczi-02-ex.json", ex_02)

    ex_03 = {
        "lesson": "b1-rakoczi-03",
        "exercises": [
            {
                "id": "b1-rakoczi-03.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["ónodi országgyűlés", "Diet of Ónód (1707)"],
                    ["trónfosztás", "dethronement of Habsburgs"],
                    ["közteherviselés", "universal taxation"],
                    ["nemesi adózás", "taxation of nobility"]
                ]
            },
            {
                "id": "b1-rakoczi-03.ex01b",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["rézpénz", "copper currency (libertás)"],
                    ["infláció", "inflation"],
                    ["trencséni csata", "Battle of Trencsén (1708)"],
                    ["hadi szerencse", "fortune of war"]
                ]
            },
            {
                "id": "b1-rakoczi-03.ex02",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Mit mondott ki az ónodi országgyűlés 1707-ben?",
                "options": [
                    "A Habsburg-ház trónfosztását Magyarországon.",
                    "A béke azonnali elfogadását Béccsel.",
                    "A török szultán visszahívását Budára."
                ],
                "correct": 0
            },
            {
                "id": "b1-rakoczi-03.ex03",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A háború idején kibocsátott ____ felirata Pro Libertate volt. (copper coin)",
                "answer": "rézpénz"
            },
            {
                "id": "b1-rakoczi-03.ex04",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Habár a nemesek egy része tiltakozott, az ónodi gyűlésen elfogadták a közös terheket. (although)",
                "answer": "Habár"
            },
            {
                "id": "b1-rakoczi-03.ex05",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Melyik csatában szenvedett sorsdöntő vereséget Rákóczi serege 1708-ban?",
                "options": [
                    "a trencséni csatában",
                    "a mohácsi csatában",
                    "a muhi csatában"
                ],
                "correct": 0
            },
            {
                "id": "b1-rakoczi-03.ex06",
                "type": "sentence-builder",
                "category": "grammar",
                "sentence": "A vágtató infláció miatt a lakosság egyre nehezebben fogadta el a libertás érméket.",
                "tiles": ["A", "vágtató", "infláció", "miatt", "a", "lakosság", "egyre", "nehezebben", "fogadta", "el", "a", "libertás", "érméket."]
            },
            {
                "id": "b1-rakoczi-03.ex07",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A vereség után a forgandó ____ végleg elfordult a szabadságharctól. (fortune of war)",
                "answer": "hadiszerencse"
            },
            {
                "id": "b1-rakoczi-03.ex08",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Milyen rendkívüli elvet hirdetett meg Rákóczi Ónodon a nemesi kiváltságok ellenében?",
                "options": [
                    "A közteherviselést, vagyis hogy a gazdag nemeseknek is adót kell fizetniük.",
                    "Hogy a nemeseknek ingyen kell aranyat osztogatni a városokban.",
                    "Hogy a parasztok nem viselhetnek fegyvert."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-rakoczi-03-ex.json", ex_03)

    ex_04 = {
        "lesson": "b1-rakoczi-04",
        "exercises": [
            {
                "id": "b1-rakoczi-04.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["szatmári béke", "Peace of Szatmár (1711)"],
                    ["amnesztia", "general pardon / amnesty"],
                    ["alku", "compromise / bargain"],
                    ["Károlyi Sándor", "Count Sándor Károlyi"]
                ]
            },
            {
                "id": "b1-rakoczi-04.ex01b",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["zászlók letétele", "laying down of banners"],
                    ["alkotmányos rend", "constitutional order"],
                    ["rendi jogok", "estate rights"],
                    ["megbékélés", "reconciliation"]
                ]
            },
            {
                "id": "b1-rakoczi-04.ex02",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Ki vezette a magyar felkelők nevében a szatmári béketárgyalásokat?",
                "options": [
                    "Károlyi Sándor tábornok",
                    "Hunyadi János",
                    "Zrínyi Miklós"
                ],
                "correct": 0
            },
            {
                "id": "b1-rakoczi-04.ex03",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "1711-ben a majtényi síkon békésen megtörtént a kuruc ____. (laying down of banners)",
                "answer": "zászlók letétele"
            },
            {
                "id": "b1-rakoczi-04.ex04",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A szatmári síkon olyan megállapodás ____, amely biztosította a békét. (was reached / born)",
                "answer": "született"
            },
            {
                "id": "b1-rakoczi-04.ex05",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit garantált a szatmári béke a fegyvert letevő kuruc harcosoknak?",
                "options": [
                    "teljes körű amnesztiát és a rendi jogok tiszteletben tartását",
                    "örökös börtönbüntetést Ausztriában",
                    "mindegyiküknek arany palotát Bécsben"
                ],
                "correct": 0
            },
            {
                "id": "b1-rakoczi-04.ex06",
                "type": "sentence-builder",
                "category": "grammar",
                "sentence": "A szatmári béke történelmi alku volt a bécsi udvar és a magyar nemesség között.",
                "tiles": ["A", "szatmári", "béke", "történelmi", "alku", "volt", "a", "bécsi", "udvar", "és", "a", "magyar", "nemesség", "között."]
            },
            {
                "id": "b1-rakoczi-04.ex07",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A hosszú háborúskodás után megvalósult a nemzeti ____ az országban. (reconciliation)",
                "answer": "megbékélés"
            },
            {
                "id": "b1-rakoczi-04.ex08",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Miért nem tekinthető a szatmári béke megalázó feltétel nélküli megadásnak?",
                "options": [
                    "Mert megmentette a magyar alkotmányos rendet és a nemesség ősi jogait.",
                    "Mert Rákóczi lett Ausztria új császára.",
                    "Mert a kurucok eladták a fegyvereiket a franciáknak."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-rakoczi-04-ex.json", ex_04)

    ex_05 = {
        "lesson": "b1-rakoczi-05",
        "exercises": [
            {
                "id": "b1-rakoczi-05.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["rodostói emigráció", "exile at Rodostó"],
                    ["Mikes Kelemen", "faithful page & writer"],
                    ["törökországi levelek", "Letters from Turkey"],
                    ["hűség", "loyalty / fidelity"]
                ]
            },
            {
                "id": "b1-rakoczi-05.ex01b",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["nemzeti függetlenség", "national independence"],
                    ["szabadsághős", "hero of freedom"],
                    ["nemzeti himnusz", "national anthem"],
                    ["történelmi emlékezet", "historical memory"]
                ]
            },
            {
                "id": "b1-rakoczi-05.ex02",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Hová vonult Rákóczi fejedelem a szabadságharc befejezése után?",
                "options": [
                    "A törökországi Rodostóba (Tekirdağ).",
                    "Londonba a királyi udvarba.",
                    "Rómába a pápai palotába."
                ],
                "correct": 0
            },
            {
                "id": "b1-rakoczi-05.ex03",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "Mikes Kelemen halhatatlan műve a ____ címen maradt fenn az utókorra. (Letters from Turkey)",
                "answer": "Törökországi levelek"
            },
            {
                "id": "b1-rakoczi-05.ex04",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A magyar utókor méltán tekinti Rákóczit a nemzeti ____ jelképének. (independence)",
                "answer": "függetlenség"
            },
            {
                "id": "b1-rakoczi-05.ex05",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Ki volt az a hűséges erdélyi nemes, aki mindvégig Rákóczi mellett maradt a száműzetésben?",
                "options": [
                    "Mikes Kelemen",
                    "Kossuth Lajos",
                    "Karinthy Frigyes"
                ],
                "correct": 0
            },
            {
                "id": "b1-rakoczi-05.ex06",
                "type": "sentence-builder",
                "category": "grammar",
                "sentence": "Mikes Kelemen hűsége és írásai örök emléket állítottak a rodostói bujdosóknak.",
                "tiles": ["Mikes", "Kelemen", "hűsége", "és", "írásai", "örök", "emléket", "állítottak", "a", "rodostói", "bujdosóknak."]
            },
            {
                "id": "b1-rakoczi-05.ex07",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "II. Rákóczi Ferenc emléke ma is tiszteletre méltó igazi nemzeti ____. (hero of freedom)",
                "answer": "szabadsághős"
            },
            {
                "id": "b1-rakoczi-05.ex08",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Hogyan él Rákóczi alakja a mai magyar kultúrában és oktatásban?",
                "options": [
                    "A hazafiság, az önfeláldozás és a nemzeti önrendelkezés örök szimbólumaként.",
                    "Csak mint egy feledésbe merült középkori földbirtokos.",
                    "Mint egy osztrák zsoldosvezér a sok közül."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-rakoczi-05-ex.json", ex_05)

    ex_consolidation = {
        "lesson": "b1-rakoczi-consolidation",
        "exercises": [
            {
                "id": "b1-rakoczi-consolidation.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["vezérlő fejedelem", "ruling prince"],
                    ["kuruc felkelés", "Kuruc uprising"],
                    ["ónodi országgyűlés", "Diet of Ónód (1707)"],
                    ["szatmári béke", "Peace of Szatmár (1711)"]
                ]
            },
            {
                "id": "b1-rakoczi-consolidation.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik mondat fejezi ki helyesen a múltbeli feltételt?",
                "options": [
                    "Ha Rákóczi elfogadta volna a császár kegyelmét, hazatérhetett volna.",
                    "Ha Rákóczi elfogadja lett a császár kegyelmét, hazatérne volt.",
                    "Ha Rákóczi elfogadta lenni a császárt, hazatért volna lenni."
                ],
                "correct": 0
            },
            {
                "id": "b1-rakoczi-consolidation.ex03",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A fejedelem híres jelmondata: Cum Deo pro Patria et ____! (Liberty)",
                "answer": "Libertate"
            },
            {
                "id": "b1-rakoczi-consolidation.ex04",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Habár a hadiszerencse elfordult, a szabadságvágy soha nem hunyt ____ a szívekben. (out)",
                "answer": "ki"
            },
            {
                "id": "b1-rakoczi-consolidation.ex05",
                "type": "sentence-builder",
                "category": "grammar",
                "sentence": "A szatmári béke biztosította a rendi jogokat és a nemzet túlélését a nehéz időkben.",
                "tiles": ["A", "szatmári", "béke", "biztosította", "a", "rendi", "jogokat", "és", "a", "nemzet", "túlélését", "a", "nehéz", "időkben."]
            },
            {
                "id": "b1-rakoczi-consolidation.ex06",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Melyik tenger partján élt Rákóczi az emigrációban?",
                "options": [
                    "A Márvány-tenger partján, Rodostóban.",
                    "Az Északi-tenger partján, Londonban.",
                    "A Balti-tenger partján, Stockholmban."
                ],
                "correct": 0
            },
            {
                "id": "b1-rakoczi-consolidation.ex07",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A kuruc seregben harcoló katonák büszkén fújták a fából készült ____. (horn)",
                "answer": "tárogatót"
            },
            {
                "id": "b1-rakoczi-consolidation.ex08",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Milyen kérdés hangozhat el a magyar állampolgársági vizsgán Rákócziról?",
                "options": [
                    "Ki volt II. Rákóczi Ferenc, és mi volt az 1703–1711-es szabadságharc jelentősége?",
                    "Mikor nyert Rákóczi aranyérmet az olimpián?",
                    "Melyik budapesti villamosvonalat tervezte Rákóczi?"
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-rakoczi-consolidation-ex.json", ex_consolidation)

    # -------------------------------------------------------------------------
    # 5. Lesson Files (01 to 05 + consolidation)
    # -------------------------------------------------------------------------
    lesson_titles = {
        "01": ("II. Rákóczi Ferenc és a Brezáni kiáltvány", "Ferenc Rákóczi II"),
        "02": ("A kurucok felkelése és hadviselése", "The Kurucok Rise Up"),
        "03": ("Az ónodi országgyűlés és a trónfosztás", "Years of War & The Diet of Ónód"),
        "04": ("A szatmári béke 1711-ben", "The Peace of Szatmár"),
        "05": ("A rodostói emigráció és a nemzeti emlékezet", "Exile & Historical Memory")
    }

    story_refs = {
        "01": "stories/world/b1/b1-rakoczi-01-vezerlo.json",
        "02": "stories/world/b1/b1-rakoczi-02-kurucok.json",
        "03": "stories/world/b1/b1-rakoczi-03-onod.json",
        "04": "stories/world/b1/b1-rakoczi-04-szatmar.json",
        "05": "stories/world/b1/b1-rakoczi-05-emlekezet.json"
    }

    for i in range(1, 6):
        padded = f"0{i}"
        hu_t, en_t = lesson_titles[padded]
        lesson_obj = {
            "id": f"lesson.b1.rakoczi-{padded}",
            "title": f"{hu_t} ({en_t})",
            "level": "B1",
            "grammar": "The Past Conditional with volna and Historical Turning Points",
            "sections": [
                {
                    "type": "goal",
                    "title": "Lesson Goals",
                    "items": [
                        f"I can discuss the events and figures of {en_t}.",
                        "I can use the past conditional (volna) to discuss historical alternatives.",
                        "I can understand key concepts tested in the Hungarian naturalization interview.",
                        "I can master eight new vocabulary items related to Rákóczi's War of Independence."
                    ]
                },
                {"type": "recycle", "count": 3},
                {"type": "story", "ref": story_refs[padded]},
                {"type": "vocabulary", "ref": f"vocabulary/b1/b1-rakoczi-{padded}-voc.json"},
                {"type": "grammar", "ref": f"grammar/b1/b1-rakoczi-{padded}-gr.json"},
                {
                    "type": "exercise-group",
                    "title": "Practice",
                    "ref": f"exercises/b1/b1-rakoczi-{padded}-ex.json",
                    "exerciseRefs": [
                        f"b1-rakoczi-{padded}.ex01",
                        f"b1-rakoczi-{padded}.ex01b",
                        f"b1-rakoczi-{padded}.ex02",
                        f"b1-rakoczi-{padded}.ex03",
                        f"b1-rakoczi-{padded}.ex04",
                        f"b1-rakoczi-{padded}.ex05",
                        f"b1-rakoczi-{padded}.ex06",
                        f"b1-rakoczi-{padded}.ex07",
                        f"b1-rakoczi-{padded}.ex08"
                    ]
                }
            ]
        }
        write_json(f"content/hu/lessons/b1/b1-rakoczi-{padded}.json", lesson_obj)

    consolidation_obj = {
        "id": "lesson.b1.rakoczi-consolidation",
        "title": "A Rákóczi-szabadságharc összefoglalása (Unit 13 Consolidation)",
        "level": "B1",
        "grammar": "Synthesis: Past Conditional & Rákóczi's Historical Legacy",
        "sections": [
            {
                "type": "goal",
                "title": "Consolidation Goals",
                "items": [
                    "I can synthesize the full 1703–1711 Rákóczi War of Independence saga.",
                    "I can confidently answer Hungarian citizenship questions on Rákóczi and the Peace of Szatmár.",
                    "I can review and apply all 40 unit vocabulary items and past conditional structures."
                ]
            },
            {"type": "story", "ref": "stories/world/b1/b1-rakoczi.json"},
            {
                "type": "exercise-group",
                "title": "Consolidation Practice",
                "ref": "exercises/b1/b1-rakoczi-consolidation-ex.json",
                "exerciseRefs": [
                    "b1-rakoczi-consolidation.ex01",
                    "b1-rakoczi-consolidation.ex02",
                    "b1-rakoczi-consolidation.ex03",
                    "b1-rakoczi-consolidation.ex04",
                    "b1-rakoczi-consolidation.ex05",
                    "b1-rakoczi-consolidation.ex06",
                    "b1-rakoczi-consolidation.ex07",
                    "b1-rakoczi-consolidation.ex08"
                ]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-rakoczi-consolidation.json", consolidation_obj)
    print("Successfully built Hungarian B1 Citizenship Unit 13 (b1-rakoczi)!")

if __name__ == "__main__":
    build_unit_13_citizenship()
