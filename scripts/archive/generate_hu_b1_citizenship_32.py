#!/usr/bin/env python3
"""Generate Hungarian B1 Citizenship Unit 32: Government & Institutions Today (b1-allamszervezet)."""

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

def build_unit_32_citizenship():
    # -------------------------------------------------------------------------
    # 1. Vocabulary Files (6 words each = 30 words total)
    # -------------------------------------------------------------------------
    voc_01 = {
        "id": "vocab.b1.allamszervezet.01",
        "lesson": "b1-allamszervezet-01",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "Országgyűlés", "translation": "National Assembly (Hungarian Parliament)", "pos": "noun"},
            {"lemma": "parlamenti képviselő", "translation": "Member of Parliament (MP)", "pos": "noun"},
            {"lemma": "törvényhozás", "translation": "legislation, legislative authority", "pos": "noun"},
            {"lemma": "plenáris ülés", "translation": "plenary session, full assembly meeting", "pos": "noun"},
            {"lemma": "parlamenti bizottság", "translation": "parliamentary committee", "pos": "noun"},
            {"lemma": "egyösszetevős parlament", "translation": "unicameral parliament (199 MPs)", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-allamszervezet-01-voc.json", voc_01)

    voc_02 = {
        "id": "vocab.b1.allamszervezet.02",
        "lesson": "b1-allamszervezet-02",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "köztársasági elnök", "translation": "President of the Republic (Head of State)", "pos": "noun"},
            {"lemma": "Sándor-palota", "translation": "Sándor Palace (presidential seat in Buda Castle)", "pos": "noun"},
            {"lemma": "a nemzet egységének kifejezője", "translation": "expresser of the unity of the nation", "pos": "noun"},
            {"lemma": "fegyveres erők főparancsnoka", "translation": "Commander-in-Chief of the Armed Forces", "pos": "noun"},
            {"lemma": "kegyelmezési jog", "translation": "power of individual clemency / pardon", "pos": "noun"},
            {"lemma": "ötéves mandátum", "translation": "five-year presidential mandate", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-allamszervezet-02-voc.json", voc_02)

    voc_03 = {
        "id": "vocab.b1.allamszervezet.03",
        "lesson": "b1-allamszervezet-03",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "Kormány", "translation": "Government (Cabinet, supreme executive body)", "pos": "noun"},
            {"lemma": "miniszterelnök", "translation": "Prime Minister (Head of Government)", "pos": "noun"},
            {"lemma": "Karmelita kolostor", "translation": "Carmelite Monastery (Prime Minister's Office in Buda)", "pos": "noun"},
            {"lemma": "minisztérium", "translation": "ministry, government department", "pos": "noun"},
            {"lemma": "végrehajtó hatalom", "translation": "executive power / branch", "pos": "noun"},
            {"lemma": "kormányrendelet", "translation": "government decree, executive order", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-allamszervezet-03-voc.json", voc_03)

    voc_04 = {
        "id": "vocab.b1.allamszervezet.04",
        "lesson": "b1-allamszervezet-04",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "Kúria", "translation": "Curia (Supreme Court of Hungary)", "pos": "noun"},
            {"lemma": "bírósági szervezet", "translation": "court system, judicial organization", "pos": "noun"},
            {"lemma": "független bíró", "translation": "independent judge", "pos": "noun"},
            {"lemma": "ügyészség", "translation": "Prosecution Service, public prosecutor's office", "pos": "noun"},
            {"lemma": "legfőbb ügyész", "translation": "Prosecutor General of Hungary", "pos": "noun"},
            {"lemma": "igazságszolgáltatás", "translation": "administration of justice, judiciary", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-allamszervezet-04-voc.json", voc_04)

    voc_05 = {
        "id": "vocab.b1.allamszervezet.05",
        "lesson": "b1-allamszervezet-05",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "törvényjavaslat benyújtása", "translation": "submission of a legislative bill", "pos": "noun"},
            {"lemma": "törvény kihirdetése", "translation": "promulgation / publication of a law", "pos": "noun"},
            {"lemma": "Magyar Közlöny", "translation": "Hungarian Official Gazette", "pos": "noun"},
            {"lemma": "országos népszavazás", "translation": "national referendum, direct ballot", "pos": "noun"},
            {"lemma": "érvényesség és eredményesség", "translation": "validity (turnout >50%) and conclusiveness of vote", "pos": "noun"},
            {"lemma": "előzetes normakontroll", "translation": "preliminary constitutional review by President/Court", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-allamszervezet-05-voc.json", voc_05)

    # -------------------------------------------------------------------------
    # 2. Grammar Files (1 per lesson = 5 files)
    # -------------------------------------------------------------------------
    gr_01 = {
        "id": "grammar.b1.allamszervezet.01.parliamentary-powers",
        "title": "Legislative Powers & Election: Törvényt alkot & Megválaszt",
        "sections": [
            {
                "type": "text",
                "title": "Legislative Agency",
                "content": "Describing the National Assembly involves verbs of legislative agency: *törvényt alkot* (creates laws), *megválasztja a miniszterelnököt* (elects the Prime Minister), and *ellenőrzi a kormány munkáját* (supervises the work of the government)."
            },
            {
                "type": "examples",
                "title": "Parliamentary examples",
                "items": [
                    {"spanish": "Az Országgyűlés a legfőbb népképviseleti szerv Magyarországon.", "english": "The National Assembly is the supreme organ of popular representation in Hungary."},
                    {"spanish": "A képviselők törvényeket alkotnak és elfogadják a költségvetést.", "english": "The MPs make laws and adopt the state budget."},
                    {"spanish": "A parlament választja meg a köztársasági elnököt és a miniszterelnököt.", "english": "Parliament elects the President of the Republic and the Prime Minister."}
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-allamszervezet-01-gr.json", gr_01)

    gr_02 = {
        "id": "grammar.b1.allamszervezet.02.presidential-functions",
        "title": "Head of State Valencies: Kifejezi a nemzet egységét & Aláír",
        "sections": [
            {
                "type": "text",
                "title": "Presidential Representation",
                "content": "The constitutional role of the President of the Republic is expressed through standard legal formulas: *kifejezi a nemzet egységét* (expresses the unity of the nation), *őrködik a demokratikus működés felett* (guards the democratic functioning), and *aláírja a törvényt* (signs the law)."
            },
            {
                "type": "examples",
                "title": "Presidential examples",
                "items": [
                    {"spanish": "A köztársasági elnök kifejezi a nemzet egységét.", "english": "The President of the Republic expresses the unity of the nation."},
                    {"spanish": "Az elnök aláírja a törvényt, vagy megküldi az Alkotmánybíróságnak.", "english": "The President signs the law, or sends it to the Constitutional Court."},
                    {"spanish": "A köztársasági elnök a Magyar Honvédség főparancsnoka.", "english": "The President of the Republic is the Commander-in-Chief of the Hungarian Defence Forces."}
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-allamszervezet-02-gr.json", gr_02)

    gr_03 = {
        "id": "grammar.b1.allamszervezet.03.executive-governance",
        "title": "Executive Governance: Felelős az Országgyűlésnek & Rendeletet bocsát ki",
        "sections": [
            {
                "type": "text",
                "title": "Executive Responsibility",
                "content": "Executive governance is framed using *felelős valakinek* (responsible / accountable to someone) and *rendeletet bocsát ki* (issues a decree). The government directs public administration (*irányítja a közigazgatást*)."
            },
            {
                "type": "examples",
                "title": "Executive examples",
                "items": [
                    {"spanish": "A Kormány a végrehajtó hatalom általános szerve.", "english": "The Government is the general organ of executive power."},
                    {"spanish": "A Kormány működéséért felelős az Országgyűlésnek.", "english": "The Government is accountable to the National Assembly for its operation."},
                    {"spanish": "A miniszterelnök határozza meg a kormány általános politikáját.", "english": "The Prime Minister defines the general policy of the government."}
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-allamszervezet-03-gr.json", gr_03)

    gr_04 = {
        "id": "grammar.b1.allamszervezet.04.judicial-independence",
        "title": "Judicial Independence & Impartiality: Ítéletet hoz & Független",
        "sections": [
            {
                "type": "text",
                "title": "Judicial Impartiality",
                "content": "The judicial branch operates under strict constitutional autonomy: *a bírák függetlenek* (judges are independent), *csak a törvénynek vannak alávetve* (are subordinated only to the law), and *ítéletet hoz a bíróság* (the court passes judgment)."
            },
            {
                "type": "examples",
                "title": "Judicial examples",
                "items": [
                    {"spanish": "A bíróságok igazságszolgáltatási tevékenységet végeznek.", "english": "The courts administer justice."},
                    {"spanish": "A bírák függetlenek, és csak a törvénynek vannak alávetve.", "english": "Judges are independent and subordinated only to the law."},
                    {"spanish": "A Kúria Magyarország legfelsőbb bírósági szerve.", "english": "The Curia is the supreme judicial organ of Hungary."}
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-allamszervezet-04-gr.json", gr_04)

    gr_05 = {
        "id": "grammar.b1.allamszervezet.05.legislative-referendum",
        "title": "The Legislative Process & Referendums: Benyújt, Elfogad & Kihirdet",
        "sections": [
            {
                "type": "text",
                "title": "Legislative Pathway",
                "content": "The complete pathway of a bill uses a three-stage verbal sequence: *benyújtja a törvényjavaslatot* (submits the bill) -> *elfogadja az Országgyűlés* (Parliament adopts it) -> *kihirdeti a Magyar Közlönyben* (promulgates in the Official Gazette). Direct democracy is channeled via *országos népszavazás* (national referendum)."
            },
            {
                "type": "examples",
                "title": "Legislative and referendum examples",
                "items": [
                    {"spanish": "Törvényjavaslatot a köztársasági elnök, a Kormány vagy bármely képviselő benyújthat.", "english": "A bill may be submitted by the President, the Government, or any MP."},
                    {"spanish": "A törvény a Magyar Közlönyben történő kihirdetéssel lép hatályba.", "english": "The law enters into force upon promulgation in the Hungarian Gazette."},
                    {"spanish": "Az érvényes és eredményes népszavazás döntése kötelező az Országgyűlésre.", "english": "The decision of a valid and conclusive referendum is binding on the National Assembly."}
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-allamszervezet-05-gr.json", gr_05)

    # -------------------------------------------------------------------------
    # 3. Serialized Stories (5 segments + 1 combined)
    # -------------------------------------------------------------------------
    story_01 = {
        "id": "story.b1.allamszervezet.01",
        "title": "Az Országgyűlés: a népképviselet és a törvényhozás háza",
        "level": "B1",
        "lesson": 1,
        "order": 32,
        "type": "world",
        "estimatedMinutes": 5,
        "summary": "The National Assembly in the Hungarian Parliament building, its 199 representatives, unicameral structure, and legislative powers.",
        "characters": [],
        "location": "Budapest, Országház, Kossuth Lajos tér",
        "grammar": ["grammar.b1.allamszervezet.01.parliamentary-powers"],
        "vocabularyTopics": ["Országgyűlés", "parlamenti képviselő", "törvényhozás"],
        "paragraphs": [
            {"type": "narration", "text": "A Duna partján magasodó, csodálatos neogótikus Országház a magyar népképviselet és államiság szíve."},
            {"type": "narration", "text": "A magyar Országgyűlés egykamarás parlament, amely 199 megválasztott képviselőből áll."},
            {"type": "narration", "text": "A képviselőket a választópolgárok négy évre választják meg vegyes választási rendszerben: egyéni választókerületekben és országos pártlistákon."},
            {"type": "narration", "text": "Az Országgyűlés feladata a törvények megalkotása, az állami költségvetés elfogadása és a nemzetközi szerződések jóváhagyása."},
            {"type": "narration", "text": "A plenáris ülések nyilvánosak, így minden állampolgár figyelemmel kísérheti a nemzet sorsát alakító parlamenti vitákat."}
        ]
    }
    write_json("content/hu/stories/world/b1/b1-allamszervezet-01-orszaggyules.json", story_01)

    story_02 = {
        "id": "story.b1.allamszervezet.02",
        "title": "A köztársasági elnök: a nemzet egységének őre",
        "level": "B1",
        "lesson": 2,
        "order": 32,
        "type": "world",
        "estimatedMinutes": 5,
        "summary": "The President of the Republic residing in the Sándor Palace, expressing the unity of the nation and guarding democratic balance.",
        "characters": [],
        "location": "Budapest, Budai Vár, Sándor-palota",
        "grammar": ["grammar.b1.allamszervezet.02.presidential-functions"],
        "vocabularyTopics": ["köztársasági elnök", "Sándor-palota", "a nemzet egységének kifejezője"],
        "paragraphs": [
            {"type": "narration", "text": "Magyarország államfője a köztársasági elnök, akinek hivatalos rezidenciája a Budai Várban található történelmi Sándor-palota."},
            {"type": "narration", "text": "Az államfőt az Országgyűlés választja meg öt évre, és legfeljebb egy alkalommal választható újra."},
            {"type": "narration", "text": "A köztársasági elnök kifejezi a nemzet egységét, és őrködik az államszervezet demokratikus működése felett."},
            {"type": "narration", "text": "Ő a Magyar Honvédség főparancsnoka, képviseli hazánkat a nemzetközi diplomáciában, nagyköveteket és bírákat nevez ki, és egyéni kegyelmet gyakorolhat."},
            {"type": "narration", "text": "Ha egy törvénnyel nem ért egyet, azt aláírás előtt visszaküldheti a parlamentnek megfontolásra, vagy normakontrollra küldheti az Alkotmánybírósághoz."}
        ]
    }
    write_json("content/hu/stories/world/b1/b1-allamszervezet-02-elnok.json", story_02)

    story_03 = {
        "id": "story.b1.allamszervezet.03",
        "title": "A Kormány és a miniszterelnök: a végrehajtó hatalom vezetése",
        "level": "B1",
        "lesson": 3,
        "order": 32,
        "type": "world",
        "estimatedMinutes": 5,
        "summary": "The Government led by the Prime Minister in the Carmelite Monastery, managing the state and directing administration.",
        "characters": [],
        "location": "Budapest, Budai Vár, Karmelita kolostor",
        "grammar": ["grammar.b1.allamszervezet.03.executive-governance"],
        "vocabularyTopics": ["Kormány", "miniszterelnök", "végrehajtó hatalom"],
        "paragraphs": [
            {"type": "narration", "text": "A magyar államszervezetben a végrehajtó hatalom csúcsán a Kormány áll, amelyet a miniszterelnök vezet."},
            {"type": "narration", "text": "A miniszterelnököt a köztársasági elnök javaslatára az Országgyűlés választja meg a képviselők többségének szavazatával."},
            {"type": "narration", "text": "A minisztereket a miniszterelnök javaslatára a köztársasági elnök nevezi ki a különböző szakminisztériumok élére."},
            {"type": "narration", "text": "A Kormány irányítja az államigazgatást, végrehajtja a törvényeket, és rendeleteket bocsát ki, amelyek nem lehetnek ellentétesek a törvényekkel."},
            {"type": "narration", "text": "Működéséért a Kormány politikai felelősséggel tartozik az Országgyűlésnek, amely bizalmatlansági indítvánnyal ellenőrizheti."}
        ]
    }
    write_json("content/hu/stories/world/b1/b1-allamszervezet-03-kormany.json", story_03)

    story_04 = {
        "id": "story.b1.allamszervezet.04",
        "title": "A bíróságok és az ügyészség: a független igazságszolgáltatás",
        "level": "B1",
        "lesson": 4,
        "order": 32,
        "type": "world",
        "estimatedMinutes": 5,
        "summary": "The administration of justice through independent courts headed by the Curia, and the role of the public prosecution service.",
        "characters": [],
        "location": "Budapest, Kúria épülete",
        "grammar": ["grammar.b1.allamszervezet.04.judicial-independence"],
        "vocabularyTopics": ["Kúria", "független bíró", "igazságszolgáltatás"],
        "paragraphs": [
            {"type": "narration", "text": "A jogállam alapvető pillére a független igazságszolgáltatás, amelyet a bíróságok négyszintű rendszere lát el."},
            {"type": "narration", "text": "A hierarchia alján a járásbíróságok állnak, felettük a törvényszékek és az ítélőtáblák, a csúcson pedig a Kúria (a legfelsőbb bíróság)."},
            {"type": "narration", "text": "A bírák függetlenek: nem lehetnek tagjai pártnak, és döntéseikben kizárólag a törvényeknek és a lelkiismeretüknek vannak alávetve."},
            {"type": "narration", "text": "A közvádló szerepét az ügyészség tölti be, amelynek élén az Országgyűlés által megválasztott legfőbb ügyész áll."},
            {"type": "narration", "text": "Az ügyészség feladata a bűncselekmények üldözése és a törvényesség felügyelete a nyomozás során."}
        ]
    }
    write_json("content/hu/stories/world/b1/b1-allamszervezet-04-birosagok.json", story_04)

    story_05 = {
        "id": "story.b1.allamszervezet.05",
        "title": "A törvényhozás útja és a közvetlen demokrácia",
        "level": "B1",
        "lesson": 5,
        "order": 32,
        "type": "world",
        "estimatedMinutes": 5,
        "summary": "How a bill becomes law, its promulgation in the Magyar Közlöny, and the mechanism of national referendums.",
        "characters": [],
        "location": "Budapest",
        "grammar": ["grammar.b1.allamszervezet.05.legislative-referendum"],
        "vocabularyTopics": ["törvényjavaslat benyújtása", "Magyar Közlöny", "országos népszavazás"],
        "paragraphs": [
            {"type": "narration", "text": "A törvényalkotás folyamata a törvényjavaslat benyújtásával kezdődik, amelyet a bizottsági viták, majd a plenáris ülés részletes tárgyalása követ."},
            {"type": "narration", "text": "Ha az Országgyűlés megszavazza a törvényt, az Országgyűlés elnöke aláírja, majd megküldi a köztársasági elnöknek kihirdetésre."},
            {"type": "narration", "text": "A törvény a hivatalos állami lapban, a Magyar Közlönyben való megjelenéssel válik hivatalossá és kötelező érvényűvé."},
            {"type": "narration", "text": "A képviseleti demokrácia mellett a közvetlen hatalomgyakorlás legfőbb eszköze az országos népszavazás."},
            {"type": "narration", "text": "Ha legalább kétszázezer választópolgár kezdeményezi, az Országgyűlés köteles elrendelni a népszavazást, amelynek döntése kötelező az államra."}
        ]
    }
    write_json("content/hu/stories/world/b1/b1-allamszervezet-05-torvenyhozas.json", story_05)

    story_combined = {
        "id": "story.b1.allamszervezet",
        "title": "A modern magyar államszervezet és demokratikus intézményei",
        "level": "B1",
        "lesson": 32,
        "order": 32,
        "type": "world",
        "estimatedMinutes": 10,
        "summary": "A comprehensive guide to Hungary's contemporary state architecture: the National Assembly, the President of the Republic, the Government, independent courts, and the legislative process.",
        "characters": [],
        "location": "Magyarország állami intézményei",
        "grammar": [
            "grammar.b1.allamszervezet.01.parliamentary-powers",
            "grammar.b1.allamszervezet.02.presidential-functions",
            "grammar.b1.allamszervezet.03.executive-governance",
            "grammar.b1.allamszervezet.04.judicial-independence",
            "grammar.b1.allamszervezet.05.legislative-referendum"
        ],
        "vocabularyTopics": [
            "Országgyűlés",
            "köztársasági elnök",
            "Kormány",
            "Kúria",
            "Magyar Közlöny",
            "országos népszavazás"
        ],
        "paragraphs": [
            {"type": "narration", "text": "Magyarország parlamentáris köztársaság, amelyben az államhatalom a néptől származik, és a klasszikus hatalommegosztás elvén nyugszik. A legfőbb népképviseleti szerv a 199 fős egykamarás Országgyűlés, amely törvényeket alkot és ellenőrzi a végrehajtó hatalmat."},
            {"type": "narration", "text": "Az államfő a köztársasági elnök, aki a Budai Vár Sándor-palotájában működik, kifejezi a nemzet egységét, a fegyveres erők főparancsnoka, és aláírja vagy alkotmányossági kontrollra küldi a törvényeket."},
            {"type": "narration", "text": "A végrehajtó hatalmat a miniszterelnök által vezetett Kormány gyakorolja, amely a minisztériumokon keresztül irányítja az ország működését, és politikai felelősséggel tartozik a parlamentnek."},
            {"type": "narration", "text": "Az igazságszolgáltatást független bíróságok gyakorolják, amelyek csúcsán a Kúria áll. A bírák pártatlanok és csak a törvénynek vannak alávetve, munkájukat a közvádlói feladatokat ellátó ügyészség egészíti ki."},
            {"type": "narration", "text": "A törvények a Magyar Közlönyben kihirdetve lépnek hatályba, miközben a választópolgárok országos népszavazások útján közvetlenül is dönthetnek a sorsfordító társadalmi kérdésekben."}
        ]
    }
    write_json("content/hu/stories/world/b1/b1-allamszervezet.json", story_combined)

    # -------------------------------------------------------------------------
    # 4. Exercises Files (8 exercises per lesson x 5 + consolidation = 6 files)
    # -------------------------------------------------------------------------
    ex_01 = {
        "lesson": "b1-allamszervezet-01",
        "exercises": [
            {
                "id": "b1-allamszervezet-01.ex01",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Hány képviselőből áll a magyar Országgyűlés?",
                "options": [
                    "199 képviselőből.",
                    "386 képviselőből.",
                    "100 képviselőből."
                ],
                "correct": 0
            },
            {
                "id": "b1-allamszervezet-01.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Az Országgyűlés a legfőbb népképviseleti szerv Magyarország_____. (in Hungary - on)",
                "answer": "on"
            },
            {
                "id": "b1-allamszervezet-01.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "parlamenti", "képviselők", "alkotják", "a", "törvényeket", "az", "Országházban."],
                "solution": ["A", "parlamenti", "képviselők", "alkotják", "a", "törvényeket", "az", "Országházban."]
            },
            {
                "id": "b1-allamszervezet-01.ex04",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Mit jelent az, hogy a magyar parlament 'egyösszetevős' (egykamarás)?",
                "options": [
                    "Hogy nincsen felsőház (mint régen a főrendiház), csak egyetlen döntéshozó képviselői kamara.",
                    "Hogy csak egyetlen politikai párt ülhet a parlamentben.",
                    "Hogy csak egyetlen törvényt hozhatnak évente."
                ],
                "correct": 0
            },
            {
                "id": "b1-allamszervezet-01.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A plenáris ülésen szavaznak a képviselők a törvényjavaslatok_____. (on bills - ról)",
                "answer": "ról"
            },
            {
                "id": "b1-allamszervezet-01.ex06",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Hány évre választják meg az országgyűlési képviselőket?",
                "options": [
                    "Négy évre.",
                    "Öt évre.",
                    "Két évre."
                ],
                "correct": 0
            },
            {
                "id": "b1-allamszervezet-01.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A parlament ellenőrzi a kormány munká_____. (its work - ját)",
                "answer": "ját"
            },
            {
                "id": "b1-allamszervezet-01.ex08",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "törvényhozás", "feladata", "a", "társadalmi", "szabályok", "megalkotása."],
                "solution": ["A", "törvényhozás", "feladata", "a", "társadalmi", "szabályok", "megalkotása."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-allamszervezet-01-ex.json", ex_01)

    ex_02 = {
        "lesson": "b1-allamszervezet-02",
        "exercises": [
            {
                "id": "b1-allamszervezet-02.ex01",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Hol található a köztársasági elnök hivatalos rezidenciája?",
                "options": [
                    "A Budai Várban, a Sándor-palotában.",
                    "A Parlament kupolatermében.",
                    "A Magyar Nemzeti Bank épületében."
                ],
                "correct": 0
            },
            {
                "id": "b1-allamszervezet-02.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A köztársasági elnök kifejezi a nemzet egység_____. (its unity - ét)",
                "answer": "ét"
            },
            {
                "id": "b1-allamszervezet-02.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "köztársasági", "elnök", "a", "Magyar", "Honvédség", "főparancsnoka."],
                "solution": ["A", "köztársasági", "elnök", "a", "Magyar", "Honvédség", "főparancsnoka."]
            },
            {
                "id": "b1-allamszervezet-02.ex04",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Hány évre választja meg az Országgyűlés a köztársasági elnököt?",
                "options": [
                    "Öt évre.",
                    "Négy évre.",
                    "Hét évre."
                ],
                "correct": 0
            },
            {
                "id": "b1-allamszervezet-02.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "Az államfő egyéni kegyelmezési jog_____ gyakorolhat elítéltek esetében. (right - ot)",
                "answer": "ot"
            },
            {
                "id": "b1-allamszervezet-02.ex06",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit tehet a köztársasági elnök, ha úgy ítéli meg, hogy egy elfogadott törvény alaptörvény-ellenes?",
                "options": [
                    "Kihirdetés előtt normakontrollra küldheti az Alkotmánybírósághoz.",
                    "Saját kezűleg széttépheti az Országházban.",
                    "Köteles minden törvényt azonnal jóváhagyni."
                ],
                "correct": 0
            },
            {
                "id": "b1-allamszervezet-02.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A köztársasági elnök őrködik az államszervezet demokratikus működése felett_____. (over - )",
                "answer": "felett"
            },
            {
                "id": "b1-allamszervezet-02.ex08",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["Az", "államfő", "képviseli", "Magyarországot", "a", "nemzetközi", "diplomáciában."],
                "solution": ["Az", "államfő", "képviseli", "Magyarországot", "a", "nemzetközi", "diplomáciában."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-allamszervezet-02-ex.json", ex_02)

    ex_03 = {
        "lesson": "b1-allamszervezet-03",
        "exercises": [
            {
                "id": "b1-allamszervezet-03.ex01",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Ki áll a magyar végrehajtó hatalom (Kormány) élén?",
                "options": [
                    "A miniszterelnök.",
                    "A legfőbb ügyész.",
                    "A Kúria elnöke."
                ],
                "correct": 0
            },
            {
                "id": "b1-allamszervezet-03.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A Kormány a végrehajtó hatalom általános szerv_____. (its organ - e)",
                "answer": "e"
            },
            {
                "id": "b1-allamszervezet-03.ex04",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Ki választja meg a magyar miniszterelnököt?",
                "options": [
                    "Az Országgyűlés, a köztársasági elnök javaslatára.",
                    "Közvetlenül az állampolgárok népszavazáson.",
                    "A miniszterek közös tanácsa."
                ],
                "correct": 0
            },
            {
                "id": "b1-allamszervezet-03.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "Kormány", "működéséért", "felelős", "az", "Országgyűlésnek."],
                "solution": ["A", "Kormány", "működéséért", "felelős", "az", "Országgyűlésnek."]
            },
            {
                "id": "b1-allamszervezet-03.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A miniszterelnök hivatala a Budai Várban, a Karmelita kolostor_____ található. (in - ban)",
                "answer": "ban"
            },
            {
                "id": "b1-allamszervezet-03.ex06",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Milyen jogi aktust bocsáthat ki a Kormány a hatáskörében?",
                "options": [
                    "Kormányrendeletet, amely törvénnyel nem lehet ellentétes.",
                    "Alkotmányt módosító dekrétumot.",
                    "Bírósági büntetőítéletet."
                ],
                "correct": 0
            },
            {
                "id": "b1-allamszervezet-03.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A minisztereket a miniszterelnök javaslatára a köztársasági elnök nevez_____ ki. (names - i)",
                "answer": "i"
            },
            {
                "id": "b1-allamszervezet-03.ex08",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "miniszterelnök", "határozza", "meg", "a", "kormány", "általános", "politikáját."],
                "solution": ["A", "miniszterelnök", "határozza", "meg", "a", "kormány", "általános", "politikáját."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-allamszervezet-03-ex.json", ex_03)

    ex_04 = {
        "lesson": "b1-allamszervezet-04",
        "exercises": [
            {
                "id": "b1-allamszervezet-04.ex01",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Hogy hívják Magyarország legfelsőbb bírósági szervét?",
                "options": [
                    "Kúria.",
                    "Országgyűlés.",
                    "Alkotmánytanács."
                ],
                "correct": 0
            },
            {
                "id": "b1-allamszervezet-04.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A bírák függetlenek, és csak a törvénynek vannak alávet_____. (subordinated - ve)",
                "answer": "ve"
            },
            {
                "id": "b1-allamszervezet-04.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "bíróságok", "független", "igazságszolgáltatási", "tevékenységet", "végeznek."],
                "solution": ["A", "bíróságok", "független", "igazságszolgáltatási", "tevékenységet", "végeznek."]
            },
            {
                "id": "b1-allamszervezet-04.ex04",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Mi az ügyészség legfontosabb feladata a büntetőeljárásokban?",
                "options": [
                    "A közvád képviselete a bíróság előtt és a nyomozás törvényességének felügyelete.",
                    "A vádlottak felmentése a büntetés alól.",
                    "Az elítéltek börtönőrzése."
                ],
                "correct": 0
            },
            {
                "id": "b1-allamszervezet-04.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A legfőbb ügyész vezeti az önálló ügyészségi szervezet_____. (its organization - ét)",
                "answer": "ét"
            },
            {
                "id": "b1-allamszervezet-04.ex06",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Lehet-e politikai párt tagja egy magyar bíró?",
                "options": [
                    "Nem, az Alaptörvény szerint a bírák nem lehetnek pártok tagjai és nem folytathatnak politikai tevékenységet.",
                    "Igen, ha a kormánypárthoz tartoznak.",
                    "Igen, de csak szabadidejükben."
                ],
                "correct": 0
            },
            {
                "id": "b1-allamszervezet-04.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A bíróságok ítélet_____ minden állampolgár és hatóság köteles elfogadni. (their judgment - ét)",
                "answer": "ét"
            },
            {
                "id": "b1-allamszervezet-04.ex08",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "törvények", "előtti", "egyenlőség", "a", "jogállam", "szilárd", "alapköve."],
                "solution": ["A", "törvények", "előtti", "egyenlőség", "a", "jogállam", "szilárd", "alapköve."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-allamszervezet-04-ex.json", ex_04)

    ex_05 = {
        "lesson": "b1-allamszervezet-05",
        "exercises": [
            {
                "id": "b1-allamszervezet-05.ex01",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Hol hirdetik ki hivatalosan a megszavazott és aláírt magyar törvényeket?",
                "options": [
                    "A Magyar Közlöny című hivatalos lapban.",
                    "A napi hírtelevíziók esti műsorában.",
                    "A budapesti városháza hirdetőtábláján."
                ],
                "correct": 0
            },
            {
                "id": "b1-allamszervezet-05.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A törvényjavaslatot a képviselők részletes vita után fogad_____ el. (adopt - ják)",
                "answer": "ják"
            },
            {
                "id": "b1-allamszervezet-05.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "törvény", "a", "Magyar", "Közlönyben", "való", "kihirdetéssel", "lép", "hatályba."],
                "solution": ["A", "törvény", "a", "Magyar", "Közlönyben", "való", "kihirdetéssel", "lép", "hatályba."]
            },
            {
                "id": "b1-allamszervezet-05.ex04",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Mikor eredményes és érvényes egy országos népszavazás Magyarországon?",
                "options": [
                    "Ha a választópolgárok több mint fele érvényesen szavazott, és a többség azonos választ adott.",
                    "Ha legalább tíz ember elment szavazni.",
                    "Ha a parlament előzetesen egyhangúlag jóváhagyta."
                ],
                "correct": 0
            },
            {
                "id": "b1-allamszervezet-05.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "Legalább kétszázezer választópolgár kezdeményezésére kötelező az országos népszavazás elrendelés_____. (its ordering - e)",
                "answer": "e"
            },
            {
                "id": "b1-allamszervezet-05.ex06",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Ki nyújthat be törvényjavaslatot az Országgyűléshez?",
                "options": [
                    "A köztársasági elnök, a Kormány, az országgyűlési bizottságok és bármely képviselő.",
                    "Bármely külföldi turista.",
                    "Csak a legfelsőbb bíróság elnöke."
                ],
                "correct": 0
            },
            {
                "id": "b1-allamszervezet-05.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Az érvényes népszavazás döntése kötelező az Országgyűlés számá_____. (for it - ra)",
                "answer": "ra"
            },
            {
                "id": "b1-allamszervezet-05.ex08",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "népszavazás", "a", "közvetlen", "demokrácia", "legfontosabb", "intézménye."],
                "solution": ["A", "népszavazás", "a", "közvetlen", "demokrácia", "legfontosabb", "intézménye."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-allamszervezet-05-ex.json", ex_05)

    ex_consolidation = {
        "lesson": "b1-allamszervezet-consolidation",
        "exercises": [
            {
                "id": "b1-allamszervezet-consolidation.ex01",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Melyik állítás írja le helyesen a magyar államformát?",
                "options": [
                    "Magyarország parlamentáris köztársaság, ahol a hatalom megoszlik a törvényhozás, végrehajtás és bíróságok között.",
                    "Magyarország abszolút monarchia egy király vezetésével.",
                    "Magyarország szövetségi állam autonóm tartományokkal."
                ],
                "correct": 0
            },
            {
                "id": "b1-allamszervezet-consolidation.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A képviselők négy évre kapnak megbízatás_____ a választóktól. (mandate - t)",
                "answer": "t"
            },
            {
                "id": "b1-allamszervezet-consolidation.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "hatalmi", "ágak", "megosztása", "védi", "a", "demokratikus", "szabadságot."],
                "solution": ["A", "hatalmi", "ágak", "megosztása", "védi", "a", "demokratikus", "szabadságot."]
            },
            {
                "id": "b1-allamszervezet-consolidation.ex04",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Kinek tartozik felelősséggel a Kormány Magyarországon?",
                "options": [
                    "Az Országgyűlésnek, amely bizalmat szavazott neki.",
                    "Csak a nemzetközi szervezeteknek.",
                    "A Kúria elnökének személyesen."
                ],
                "correct": 0
            },
            {
                "id": "b1-allamszervezet-consolidation.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A bíróságok csúcsán álló Kúria biztosítja a bírói ítéletek egység_____. (its unity - ét)",
                "answer": "ét"
            },
            {
                "id": "b1-allamszervezet-consolidation.ex06",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "független", "igazságszolgáltatás", "minden", "polgár", "jogait", "egyformán", "védi."],
                "solution": ["A", "független", "igazságszolgáltatás", "minden", "polgár", "jogait", "egyformán", "védi."]
            },
            {
                "id": "b1-allamszervezet-consolidation.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A köztársasági elnök aláírja a kihirdetendő törvények_____. (the laws - et)",
                "answer": "et"
            },
            {
                "id": "b1-allamszervezet-consolidation.ex08",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Hogyan gyakorolhatja a nép közvetlenül a hatalmat az Alaptörvény szerint?",
                "options": [
                    "Országos népszavazás útján.",
                    "Internetes fórumokon való hozzászólásokkal.",
                    "A minisztériumi irodák elfoglalásával."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-allamszervezet-consolidation-ex.json", ex_consolidation)

    # -------------------------------------------------------------------------
    # 5. Lesson Files (01 to 05 + consolidation)
    # -------------------------------------------------------------------------
    lesson_titles = {
        "01": ("Az Országgyűlés és a törvényhozó hatalom", "The National Assembly & Legislative Authority"),
        "02": ("A köztársasági elnök és hatáskörei", "The President of the Republic & State Powers"),
        "03": ("A Kormány és a végrehajtó hatalom", "The Government & Executive Power"),
        "04": ("A bírósági szervezet és az igazságszolgáltatás", "The Judicial System & Courts"),
        "05": ("A törvényalkotás menete és a népszavazás", "The Legislative Pathway & Direct Democracy")
    }

    story_refs = {
        "01": "stories/world/b1/b1-allamszervezet-01-orszaggyules.json",
        "02": "stories/world/b1/b1-allamszervezet-02-elnok.json",
        "03": "stories/world/b1/b1-allamszervezet-03-kormany.json",
        "04": "stories/world/b1/b1-allamszervezet-04-birosagok.json",
        "05": "stories/world/b1/b1-allamszervezet-05-torvenyhozas.json"
    }

    grammar_refs = {
        "01": "grammar/b1/b1-allamszervezet-01-gr.json",
        "02": "grammar/b1/b1-allamszervezet-02-gr.json",
        "03": "grammar/b1/b1-allamszervezet-03-gr.json",
        "04": "grammar/b1/b1-allamszervezet-04-gr.json",
        "05": "grammar/b1/b1-allamszervezet-05-gr.json"
    }

    for i in range(1, 6):
        padded = f"0{i}"
        hu_t, en_t = lesson_titles[padded]
        lesson_data = {
            "id": f"lesson.b1.allamszervezet-{padded}",
            "unit": 32,
            "title": f"{hu_t} ({en_t})",
            "level": "B1",
            "grammar": "Institutional Governance, Separation of Powers & Public Law in Hungarian",
            "sections": [
                {
                    "type": "goal",
                    "title": "Lesson Goals",
                    "items": [
                        f"I can understand and discuss {en_t} in Hungarian.",
                        "I can use state institutional terms (Országgyűlés, köztársasági elnök, Kormány, Kúria, népszavazás).",
                        "I can explain Hungary's state architecture and democratic separation of powers for the citizenship examination.",
                        "I can read and analyze the serialized historical story on Hungary's governmental institutions."
                    ]
                },
                {"type": "recycle", "count": 3},
                {"type": "vocabulary", "ref": f"vocabulary/b1/b1-allamszervezet-{padded}-voc.json"},
                {"type": "grammar", "ref": grammar_refs[padded]},
                {
                    "type": "story",
                    "title": hu_t,
                    "ref": story_refs[padded]
                },
                {
                    "type": "exercise-group",
                    "title": "Practice",
                    "ref": f"exercises/b1/b1-allamszervezet-{padded}-ex.json",
                    "exerciseRefs": [f"b1-allamszervezet-{padded}.ex0{k}" for k in range(1, 9)]
                }
            ]
        }
        write_json(f"content/hu/lessons/b1/b1-allamszervezet-{padded}.json", lesson_data)

    consolidation_data = {
        "id": "lesson.b1.allamszervezet-consolidation",
        "unit": 32,
        "title": "Unit 32 Consolidation (Államszervezet és intézmények)",
        "level": "B1",
        "grammar": "Consolidation of Hungarian State Architecture, Institutions & Civic Governance",
        "sections": [
            {
                "type": "story",
                "title": "A modern magyar államszervezet és demokratikus intézményei",
                "ref": "stories/world/b1/b1-allamszervezet.json"
            },
            {
                "type": "exercise-group",
                "title": "Consolidation Practice",
                "ref": "exercises/b1/b1-allamszervezet-consolidation-ex.json",
                "exerciseRefs": [f"b1-allamszervezet-consolidation.ex0{k}" for k in range(1, 9)]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-allamszervezet-consolidation.json", consolidation_data)
    print("Successfully built Hungarian B1 Citizenship Unit 32 (b1-allamszervezet)!")

if __name__ == "__main__":
    build_unit_32_citizenship()
