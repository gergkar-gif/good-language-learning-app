#!/usr/bin/env python3
"""Generate Hungarian B1 Core Unit 27: Social Life & Communication (b1-27)."""

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

def build_unit_27_core():
    # -------------------------------------------------------------------------
    # 1. Vocabulary Files (4 words each = 20 words total)
    # -------------------------------------------------------------------------
    voc_01 = {
        "id": "vocab.b1.27.01",
        "lesson": "b1-27-01",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "összejövetel", "translation": "gathering, social get-together", "pos": "noun"},
            {"lemma": "társalgás", "translation": "conversation, social discourse", "pos": "noun"},
            {"lemma": "vendégszeretet", "translation": "hospitality, welcoming nature", "pos": "noun"},
            {"lemma": "meghívás", "translation": "invitation", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-27-01-voc.json", voc_01)

    voc_02 = {
        "id": "vocab.b1.27.02",
        "lesson": "b1-27-02",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "félreértés", "translation": "misunderstanding, miscommunication", "pos": "noun"},
            {"lemma": "nézeteltérés", "translation": "disagreement, difference of opinion", "pos": "noun"},
            {"lemma": "megbeszélés", "translation": "discussion, clarification talk", "pos": "noun"},
            {"lemma": "kompromisszum", "translation": "compromise, mutual accommodation", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-27-02-voc.json", voc_02)

    voc_03 = {
        "id": "vocab.b1.27.03",
        "lesson": "b1-27-03",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "pletyka", "translation": "gossip, rumor", "pos": "noun"},
            {"lemma": "bizalom", "translation": "trust, confidence in someone", "pos": "noun"},
            {"lemma": "őszinteség", "translation": "honesty, sincerity, frankness", "pos": "noun"},
            {"lemma": "titoktartás", "translation": "confidentiality, discretion, keeping secrets", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-27-03-voc.json", voc_03)

    voc_04 = {
        "id": "vocab.b1.27.04",
        "lesson": "b1-27-04",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "közösség", "translation": "community, fellowship", "pos": "noun"},
            {"lemma": "összetartás", "translation": "cohesion, standing together, solidarity", "pos": "noun"},
            {"lemma": "bajtársiasság", "translation": "camaraderie, brotherliness among comrades", "pos": "noun"},
            {"lemma": "hűség", "translation": "loyalty, devotion to friends or cause", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-27-04-voc.json", voc_04)

    voc_05 = {
        "id": "vocab.b1.27.05",
        "lesson": "b1-27-05",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "kapcsolatápolás", "translation": "nurturing relationships, keeping in touch", "pos": "noun"},
            {"lemma": "empátia", "translation": "empathy, capacity for fellow feeling", "pos": "noun"},
            {"lemma": "figyelmesség", "translation": "thoughtfulness, attentiveness, courtesy", "pos": "noun"},
            {"lemma": "gesztus", "translation": "gesture, friendly act of goodwill", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-27-05-voc.json", voc_05)

    # -------------------------------------------------------------------------
    # 2. Grammar Files (2 per regular lesson = 10 files)
    # -------------------------------------------------------------------------
    gr_01_a = {
        "id": "grammar.b1.27.01.reported-speech-statements",
        "title": "Indirect Speech: Reporting Statements (azt mondta, hogy...)",
        "sections": [
            {
                "type": "text",
                "title": "Reported Statements with 'azt mondta, hogy...'",
                "content": "In Hungarian reported speech, the tense of the original statement is preserved (unlike English backshifting). The reporting clause regularly includes the demonstrative pronoun *azt*: *Azt mondta, hogy szívesen eljön.* ('He said he would gladly come' - original: 'Szívesen eljövök')."
            },
            {
                "type": "examples",
                "title": "Examples of reported statements",
                "items": [
                    {
                        "spanish": "Péter azt mondta, hogy nagyon örül a meghívásnak.",
                        "english": "Péter said that he was very pleased with the invitation."
                    },
                    {
                        "spanish": "A vendégek azt mesélték, hogy csodás volt a hangulat az összejövetelen.",
                        "english": "The guests recounted that the atmosphere was wonderful at the gathering."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-27-01-a-gr.json", gr_01_a)

    gr_01_b = {
        "id": "grammar.b1.27.01.polite-invitations",
        "title": "Social Etiquette: Formal Invitations & Acceptances",
        "sections": [
            {
                "type": "text",
                "title": "Invitations in Social Discourse",
                "content": "Key formulas include: *Szeretettel meghívjuk Önt/téged...*, *Nagy örömünkre szolgálna, ha eljönne...*, *Örömmel teszünk eleget a meghívásnak*, and *Hálásan köszönjük a vendégszeretetet.*"
            },
            {
                "type": "examples",
                "title": "Formal and polite phrases",
                "items": [
                    {
                        "spanish": "Nagy örömmel teszünk eleget a baráti meghívásnak.",
                        "english": "We gladly accept the friendly invitation."
                    },
                    {
                        "spanish": "A házigazdák meleg vendégszeretettel fogadták az érkezőket.",
                        "english": "The hosts welcomed the arrivals with warm hospitality."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-27-01-b-gr.json", gr_01_b)

    gr_02_a = {
        "id": "grammar.b1.27.02.reported-speech-questions",
        "title": "Indirect Questions: azt kérdezte, hogy... vajon / -e",
        "sections": [
            {
                "type": "text",
                "title": "Indirect Yes/No and Wh-Questions",
                "content": "Indirect yes/no questions use the enclitic interrogative particle *-e* attached to the finite verb or predicate, or the polite interrogative particle *vajon*: *Azt kérdezte, hogy ráérsz-e ma este.* ('He asked whether you were free tonight'). In wh-questions, the question word follows *hogy*: *Azt kérdezte, hogy mikor kezdődik a megbeszélés.*"
            },
            {
                "type": "examples",
                "title": "Indirect question examples",
                "items": [
                    {
                        "spanish": "A kollégám azt kérdezte, hogy sikerült-e tisztázni a félreértést.",
                        "english": "My colleague asked whether we managed to clarify the misunderstanding."
                    },
                    {
                        "spanish": "Azt kérdezte tőlem, hogy vajon kész vagyok-e a kompromisszumra.",
                        "english": "He asked me whether I was ready for a compromise."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-27-02-a-gr.json", gr_02_a)

    gr_02_b = {
        "id": "grammar.b1.27.02.resolving-misunderstandings",
        "title": "Dispute Resolution Phrases: tisztáz, dűlőre jut, kompromisszum",
        "sections": [
            {
                "type": "text",
                "title": "Idiomatic Disagreement & Agreement",
                "content": "Constructive conflict resolution employs specific idioms: *félreértés tisztázása* ('clearing up a misunderstanding'), *dűlőre jut vkivel* ('reaching an accord/coming to terms'), *kompromisszumot köt* ('striking a compromise'), and *közös nevezőre jut* ('finding common ground')."
            },
            {
                "type": "examples",
                "title": "Negotiating harmony",
                "items": [
                    {
                        "spanish": "Egy nyugodt személyes megbeszélés során sikerült tisztázniuk a nézeteltérést.",
                        "english": "During a calm in-person discussion, they managed to clear up the difference of opinion."
                    },
                    {
                        "spanish": "Hosszú vita után végül kompromisszumos megoldásban állapodtak meg.",
                        "english": "After a long debate, they finally agreed on a compromise solution."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-27-02-b-gr.json", gr_02_b)

    gr_03_a = {
        "id": "grammar.b1.27.03.reported-speech-imperatives",
        "title": "Indirect Imperatives: Subjunctive in Dependent Clauses",
        "sections": [
            {
                "type": "text",
                "title": "Commands and Requests in Indirect Speech",
                "content": "When reporting commands, advice, or requests, Hungarian uses the subjunctive mood (*-j-*) in the dependent clause: *Arra kért, hogy segítsek neki.* ('He asked me to help him'). *Megtiltotta, hogy továbbadjuk a titkot.* ('He forbade us to pass on the secret')."
            },
            {
                "type": "examples",
                "title": "Indirect subjunctive commands",
                "items": [
                    {
                        "spanish": "Arra kértem a barátomat, hogy tartsa meg magának ezt a bizalmas információt.",
                        "english": "I asked my friend to keep this confidential information to himself."
                    },
                    {
                        "spanish": "A főnök felszólította a csapatot, hogy őszintén beszéljenek a felmerülő problémákról.",
                        "english": "The boss urged the team to speak honestly about emerging problems."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-27-03-a-gr.json", gr_03_a)

    gr_03_b = {
        "id": "grammar.b1.27.03.confidentiality-and-trust",
        "title": "Governing Trust and Secrecy: megbízik vkiben, titkot tart",
        "sections": [
            {
                "type": "text",
                "title": "Verbal Valencies with Trust",
                "content": "*Megbízik vkiben* (trusts in someone - inessive *-ban/-ben*), *a bizalmába fogad vkit* (takes someone into one's confidence - illative *-ba/-be*), *visszaél a bizalommal* (abuses trust - instrumental *-val/-vel*), *titkot tart* (keeps a secret)."
            },
            {
                "type": "examples",
                "title": "Trust and secrecy in practice",
                "items": [
                    {
                        "spanish": "Teljes mértékben megbízom a barátomban, mert soha nem él vissza a bizalmammal.",
                        "english": "I trust my friend completely because he never abuses my trust."
                    },
                    {
                        "spanish": "A titoktartás és az őszinteség minden tartós barátság sarokköve.",
                        "english": "Confidentiality and honesty are the cornerstones of every lasting friendship."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-27-03-b-gr.json", gr_03_b)

    gr_04_a = {
        "id": "grammar.b1.27.04.reciprocal-relations",
        "title": "Reciprocal Pronouns and Mutual Action: egymás, kölcsönösen",
        "sections": [
            {
                "type": "text",
                "title": "Declension of 'egymás'",
                "content": "The reciprocal pronoun *egymás* ('each other / one another') declines with all Hungarian case suffixes: *egymást* (accusative), *egymásnak* (dative), *egymással* (instrumental), *egymásért* (causal-final), *egymás mellett* (postpositional). It expresses mutual solidarity and community bond."
            },
            {
                "type": "examples",
                "title": "Reciprocity in community",
                "items": [
                    {
                        "spanish": "A jó barátok mindig kiállnak egymásért a nehéz időkben.",
                        "english": "Good friends always stand up for one another in hard times."
                    },
                    {
                        "spanish": "A csapat tagjai kölcsönösen támogatják egymást minden helyzetben.",
                        "english": "The team members mutually support each other in every situation."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-27-04-a-gr.json", gr_04_a)

    gr_04_b = {
        "id": "grammar.b1.27.04.camaraderie-and-solidarity",
        "title": "Solidarity and Loyalty: bajtársiasság, összetartás",
        "sections": [
            {
                "type": "text",
                "title": "Expressions of Group Cohesion",
                "content": "*Összetart a csapat* ('the team sticks together'), *hű marad az elveihez/barátaihoz* ('remains faithful to his principles/friends' - allative *-hoz/-hez/-höz*), *bajtársiasságot tanúsít* ('shows camaraderie')."
            },
            {
                "type": "examples",
                "title": "Camaraderie examples",
                "items": [
                    {
                        "spanish": "A fiúk közötti szilárd összetartás tette legyőzhetetlenné a közösséget.",
                        "english": "The solid cohesion among the boys made the community invincible."
                    },
                    {
                        "spanish": "Nemecsek mindvégig hű maradt a grundhoz és a barátaihoz.",
                        "english": "Nemecsek remained faithful to the Grund and his friends all the way to the end."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-27-04-b-gr.json", gr_04_b)

    gr_05_a = {
        "id": "grammar.b1.27.05.empathy-and-tact",
        "title": "Empathy and Considerateness: empátia, figyelmesség",
        "sections": [
            {
                "type": "text",
                "title": "Expressing Sensitivity to Others",
                "content": "Interpersonal attentiveness requires expressions of empathy: *beleéli magát a másik helyzetébe* ('puts oneself in the other's shoes'), *figyelmességet tanúsít* ('shows attentiveness/kindness'), *egy apró gesztussal kedveskedik* ('charms/pleases with a small gesture')."
            },
            {
                "type": "examples",
                "title": "Empathy in action",
                "items": [
                    {
                        "spanish": "Az empátia segít megérteni a másik ember valódi érzéseit és félelmeit.",
                        "english": "Empathy helps to understand another person's true feelings and fears."
                    },
                    {
                        "spanish": "Egy apró figyelmesség vagy egy kedves gesztus is mélyen megérinti az embert.",
                        "english": "Even a tiny act of thoughtfulness or a kind gesture touches a person deeply."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-27-05-a-gr.json", gr_05_a)

    gr_05_b = {
        "id": "grammar.b1.27.05.concessive-clauses",
        "title": "Concessive Clauses: bár, noha, annak ellenére, hogy...",
        "sections": [
            {
                "type": "text",
                "title": "Concessive Connectors in Hungarian",
                "content": "Concessive relations contrast an unexpected outcome with an obstacle: *bár* ('although'), *noha* ('even though'), *annak ellenére, hogy...* ('in spite of the fact that...'). The main clause often opens with *mégis* ('yet / nevertheless'): *Bár fáradt volt, mégis elment a találkozóra.*"
            },
            {
                "type": "examples",
                "title": "Concessive examples",
                "items": [
                    {
                        "spanish": "Bár lázas és gyenge volt, Nemecsek mégis elment megvédeni a grundot.",
                        "english": "Although he was feverish and weak, Nemecsek nevertheless went to defend the Grund."
                    },
                    {
                        "spanish": "Annak ellenére, hogy sokáig nem találkoztak, a barátságuk ugyanolyan mély maradt.",
                        "english": "In spite of the fact that they hadn't met for a long time, their friendship remained just as deep."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-27-05-b-gr.json", gr_05_b)

    # -------------------------------------------------------------------------
    # 3. Exercises Files (6 files = 48 exercises total)
    # -------------------------------------------------------------------------
    ex_01 = {
        "lesson": "b1-27-01",
        "exercises": [
            {
                "id": "b1-27-01.ex01",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent az 'összejövetel' szó egy társasági környezetben?",
                "options": [
                    "Barátok, rokonok vagy ismerősök kötetlen találkozóját, társasági összejövetelt.",
                    "Egy zárt katonai hadgyakorlatot.",
                    "A közlekedési lámpa pirosra váltását."
                ],
                "correct": 0
            },
            {
                "id": "b1-27-01.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Péter azt mondta, hogy örömmel részt vesz az esti összejövetel_____. (on it - en)",
                "answer": "en"
            },
            {
                "id": "b1-27-01.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "házigazdák", "meleg", "vendégszeretettel", "fogadták", "a", "meghívott", "vendégeket."],
                "solution": ["A", "házigazdák", "meleg", "vendégszeretettel", "fogadták", "a", "meghívott", "vendégeket."]
            },
            {
                "id": "b1-27-01.ex04",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik mondat fejezi ki helyesen az udvarias meghívás elfogadását?",
                "options": [
                    "Nagy örömmel teszünk eleget a kedves meghívásnak.",
                    "A meghívást a fiókba dobjuk örömmel.",
                    "Nem érkezünk meg a meghívásra soha."
                ],
                "correct": 0
            },
            {
                "id": "b1-27-01.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A vacsoraasztal mellett kellemes és elmélyült társalg_____ alakult ki. (conversation - ás)",
                "answer": "ás"
            },
            {
                "id": "b1-27-01.ex06",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent a 'vendégszeretet' fogalma?",
                "options": [
                    "A vendégek szívélyes, odaadó és figyelmes fogadását az otthonunkban.",
                    "A vendégek azonnali hazaküldését vacsora nélkül.",
                    "A szállodai szobák kötelező takarítását."
                ],
                "correct": 0
            },
            {
                "id": "b1-27-01.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Anna azt mesélte, hogy nagyon jól érez_____ magát a szombati partin. (felt - te)",
                "answer": "te"
            },
            {
                "id": "b1-27-01.ex08",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "szívélyes", "vendégszeretet", "maradandó", "élményt", "nyújtott", "mindenkinek."],
                "solution": ["A", "szívélyes", "vendégszeretet", "maradandó", "élményt", "nyújtott", "mindenkinek."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-27-01-ex.json", ex_01)

    ex_02 = {
        "lesson": "b1-27-02",
        "exercises": [
            {
                "id": "b1-27-02.ex01",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Hogyan lehet a legkonstruktívabban kezelni egy munkahelyi nézeteltérést?",
                "options": [
                    "Nyugodt, személyes megbeszéléssel és a közös kompromisszum keresésével.",
                    "Azonnali sértődött elhallgatással és ajtócsapkodással.",
                    "A másik fél háta mögötti pletykálkodással."
                ],
                "correct": 0
            },
            {
                "id": "b1-27-02.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Azt kérdezte tőlem a kollégám, hogy ráér_____-e egy rövid egyeztetésre. (is free - ek)",
                "answer": "ek"
            },
            {
                "id": "b1-27-02.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "felek", "hosszú", "tárgyalás", "után", "méltányos", "kompromisszumot", "kötöttek."],
                "solution": ["A", "felek", "hosszú", "tárgyalás", "után", "méltányos", "kompromisszumot", "kötöttek."]
            },
            {
                "id": "b1-27-02.ex04",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Hogyan használjuk a függő kérdést a magyar nyelvben eldöntendő kérdés esetén?",
                "options": [
                    "A 'hogy' kötőszó után az igéhez kapcsoljuk az '-e' kérdőpartikulát.",
                    "Mindig felkiáltójelet teszünk a mondat végére.",
                    "Kizárólag tagadó formában tehetünk fel függő kérdést."
                ],
                "correct": 0
            },
            {
                "id": "b1-27-02.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "Egy sajnálatos félreért_____ miatt késett a közös projekt befejezése. (stem suffix - és)",
                "answer": "és"
            },
            {
                "id": "b1-27-02.ex06",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent a 'dűlőre jut' kifejezés?",
                "options": [
                    "Sikeresen megegyezésre vagy döntésre jut egy vitás kérdésben.",
                    "Eltéved a szántóföldön a dűlőúton.",
                    "Kiborítja a poharat az asztalra."
                ],
                "correct": 0
            },
            {
                "id": "b1-27-02.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A megbeszélés során sikerült tisztáz_____ a korábbi nézeteltéréseket. (to clarify - niuk)",
                "answer": "niuk"
            },
            {
                "id": "b1-27-02.ex08",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "nyílt", "párbeszéd", "segít", "megelőzni", "a", "kellemetlen", "félreértéseket."],
                "solution": ["A", "nyílt", "párbeszéd", "segít", "megelőzni", "a", "kellemetlen", "félreértéseket."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-27-02-ex.json", ex_02)

    ex_03 = {
        "lesson": "b1-27-03",
        "exercises": [
            {
                "id": "b1-27-03.ex01",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Miért rombolja a pletyka a közösségi légkört?",
                "options": [
                    "Mert aláássa az őszinte emberi bizalmat és valótlan híreszteléseket terjeszt.",
                    "Mert a pletykálkodás növeli a termelékenységet.",
                    "Mert kötelezővé teszi a napi edzést."
                ],
                "correct": 0
            },
            {
                "id": "b1-27-03.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Arra kértem a barátomat, hogy ne mond_____ el senkinek a titkomat. (tell - ja)",
                "answer": "ja"
            },
            {
                "id": "b1-27-03.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "titoktartás", "és", "az", "őszinteség", "minden", "igaz", "barátság", "alapköve."],
                "solution": ["A", "titoktartás", "és", "az", "őszinteség", "minden", "igaz", "barátság", "alapköve."]
            },
            {
                "id": "b1-27-03.ex04",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Hogyan képezzük a függő felszólítást a 'Menj el!' mondatból?",
                "options": [
                    "Azt mondta, hogy menjek el.",
                    "Azt mondta, hogy mentem el tegnap.",
                    "Azt mondta, hogy menni fog holnap."
                ],
                "correct": 0
            },
            {
                "id": "b1-27-03.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "Teljes mértékben meg_____bízom a régi barátomban. (prefix - meg)",
                "answer": "meg"
            },
            {
                "id": "b1-27-03.ex06",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent az, ha valaki 'visszaél a bizalommal'?",
                "options": [
                    "Kihasználja és elárulja a másik jóhiszeműségét és titkát a saját előnyére.",
                    "Dupla adag kávét főz a vendégének.",
                    "Kölcsönad egy könyvet a könyvtárból."
                ],
                "correct": 0
            },
            {
                "id": "b1-27-03.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A tanár felszólította a diákokat, hogy őszintén válaszol_____ a feltett kérdésre. (they answer - janak)",
                "answer": "janak"
            },
            {
                "id": "b1-27-03.ex08",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["Az", "igazi", "barát", "soha", "nem", "fecsegi", "ki", "mások", "titkait."],
                "solution": ["Az", "igazi", "barát", "soha", "nem", "fecsegi", "ki", "mások", "titkait."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-27-03-ex.json", ex_03)

    ex_04 = {
        "lesson": "b1-27-04",
        "exercises": [
            {
                "id": "b1-27-04.ex01",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent a 'bajtársiasság' a kapcsolatokban?",
                "options": [
                    "A bajban is kitartó, önfeláldozó és hűséges szolidaritást a társak iránt.",
                    "A pénzügyi befektetések közös elszámolását.",
                    "Az utcai közlekedési szabályok betartását."
                ],
                "correct": 0
            },
            {
                "id": "b1-27-04.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A jó barátok mindig kiállnak egymás_____ a legnehezebb helyzetekben is. (for each other - ért)",
                "answer": "ért"
            },
            {
                "id": "b1-27-04.ex03",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "közösség", "ereje", "a", "tagok", "közötti", "szoros", "összetartásban", "rejlik."],
                "solution": ["A", "közösség", "ereje", "a", "tagok", "közötti", "szoros", "összetartásban", "rejlik."]
            },
            {
                "id": "b1-27-04.ex04",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Hogyan ragozzuk helyesen az 'egymás' kölcsönös névmást határozói formában?",
                "options": [
                    "Egymással, egymásért, egymás mellett.",
                    "Magammal, magaddal, magával.",
                    "Valakivel, senkivel, mindenkivel."
                ],
                "correct": 0
            },
            {
                "id": "b1-27-04.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A csapat tagjai hűségesek marad_____ a közös grundhoz. (remained - tak)",
                "answer": "tak"
            },
            {
                "id": "b1-27-04.ex06",
                "type": "multiple-choice",
                "category": "literature",
                "question": "Ki volt A Pál utcai fiúkban az a kistermetű, bátor közlegény, aki életét adta a grundért?",
                "options": [
                    "Nemecsek Ernő.",
                    "Boka János.",
                    "Áts Feri."
                ],
                "correct": 0
            },
            {
                "id": "b1-27-04.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A fiúk kölcsönösen segítet_____ egymást a csata előkészületeiben. (they helped - ték)",
                "answer": "ték"
            },
            {
                "id": "b1-27-04.ex08",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "bátor", "társak", "mindig", "megbízhatnak", "egymásban."],
                "solution": ["A", "bátor", "társak", "mindig", "megbízhatnak", "egymásban."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-27-04-ex.json", ex_04)

    ex_05 = {
        "lesson": "b1-27-05",
        "exercises": [
            {
                "id": "b1-27-05.ex01",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent az 'empátia' fogalma?",
                "options": [
                    "A képességet arra, hogy beleéljük magunkat a másik ember lelkiállapotába és megértsük érzéseit.",
                    "A gyors számolási készséget pénztárnál.",
                    "A külföldi utazások iránti olthatatlan vágyat."
                ],
                "correct": 0
            },
            {
                "id": "b1-27-05.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Bár sok dolga volt, még_____ szakított időt egy telefonhívásra. (nevertheless - is)",
                "answer": "is"
            },
            {
                "id": "b1-27-05.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Egy", "apró", "figyelmesség", "is", "örömet", "szerezhet", "a", "barátainknak."],
                "solution": ["Egy", "apró", "figyelmesség", "is", "örömet", "szerezhet", "a", "barátainknak."]
            },
            {
                "id": "b1-27-05.ex04",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik mondatban találunk helyes megengedő mellékmondatot?",
                "options": [
                    "Annak ellenére, hogy fáradt volt, vidáman köszöntötte az érkezőket.",
                    "Mert fáradt volt, ezért korán lefeküdt aludni.",
                    "Ha fáradt lesz, holnap nem jön el a találkozóra."
                ],
                "correct": 0
            },
            {
                "id": "b1-27-05.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A rendszeres kapcsolatápol_____ segít megőrizni a gyermekkori barátságokat. (stem suffix - ás)",
                "answer": "ás"
            },
            {
                "id": "b1-27-05.ex06",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Milyen cselekedet tekinthető 'kedves gesztusnak'?",
                "options": [
                    "Egy szál virág, egy kézzel írt képeslap vagy egy meleg érdeklődő szó.",
                    "A másik autó elé való hirtelen bevágás a kereszteződésben.",
                    "A számla kifizetésének elfelejtése."
                ],
                "correct": 0
            },
            {
                "id": "b1-27-05.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Noha Nemecsek nagyon gyenge volt, mégis elment a grund_____ védelmére. (to its defense - ra)",
                "answer": "ra"
            },
            {
                "id": "b1-27-05.ex08",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "figyelmesség", "és", "az", "empátia", "szebbé", "teszi", "az", "emberi", "életet."],
                "solution": ["A", "figyelmesség", "és", "az", "empátia", "szebbé", "teszi", "az", "emberi", "életet."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-27-05-ex.json", ex_05)

    ex_consolidation = {
        "lesson": "b1-27-consolidation",
        "exercises": [
            {
                "id": "b1-27-consolidation.ex01",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Hogyan alakul át függő beszédben az 'Eljövök hozzátok holnap' kijelentés?",
                "options": [
                    "Azt mondta, hogy eljön hozzánk másnap.",
                    "Azt mondta, hogy elment volna tegnap.",
                    "Azt mondta, hogy ne jöjjetek hozzánk."
                ],
                "correct": 0
            },
            {
                "id": "b1-27-consolidation.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A tanácskozáson arra kérték a feleket, hogy kössenek észszerű kompromisszum_____. (accusative - ot)",
                "answer": "ot"
            },
            {
                "id": "b1-27-consolidation.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "Pál", "utcai", "fiúk", "mindannyian", "kiálltak", "a", "grundért."],
                "solution": ["A", "Pál", "utcai", "fiúk", "mindannyian", "kiálltak", "a", "grundért."]
            },
            {
                "id": "b1-27-consolidation.ex04",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Hogyan mutatja be Molnár Ferenc a bajtársiasság és az önfeláldozás eszméjét 'A Pál utcai fiúkban'?",
                "options": [
                    "Nemecsek Ernő törékeny fizikai erejét felülmúlja tiszta szíve és a grund iránti tántoríthatatlan hűsége.",
                    "A fiúk azonnal eladják a grundot egy építési vállalkozónak pénzért.",
                    "A gyerekek megunják a játékot és inkább hazamennek tanulni."
                ],
                "correct": 0
            },
            {
                "id": "b1-27-consolidation.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A kis Nemecsek bátorsága előtt még a vörösingesek vezére, Áts Feri is tisztelet_____ adózott. (with respect - tel)",
                "answer": "tel"
            },
            {
                "id": "b1-27-consolidation.ex06",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "hűség", "és", "a", "becsület", "nem", "a", "rangtól", "függ."],
                "solution": ["A", "hűség", "és", "a", "becsület", "nem", "a", "rangtól", "függ."]
            },
            {
                "id": "b1-27-consolidation.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Bár a Pál utcaiak győztek a csatában, a kis közlegény elvesztése mély gyászba borította a csapat_____. (the team - ot)",
                "answer": "ot"
            },
            {
                "id": "b1-27-consolidation.ex08",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit szimbolizál a 'grund' a magyar irodalomban és kultúrában?",
                "options": [
                    "A szabadság, a gyermeki összetartás és a szülőföld szent és féltve őrzött jelképét.",
                    "Egy egyszerű pesti építési telket fűrészteleppel.",
                    "Egy elkerített virágoskertet."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-27-consolidation-ex.json", ex_consolidation)

    # -------------------------------------------------------------------------
    # 4. Classic Story Adaptation for Consolidation: A Pál utcai fiúk
    # -------------------------------------------------------------------------
    story_classic = {
        "id": "story.b1.27.classic",
        "title": "A Pál utcai fiúk",
        "level": "B1",
        "order": 27,
        "type": "classics",
        "estimatedMinutes": 8,
        "summary": "An adaptation of Ferenc Molnár's universally celebrated masterpiece 'A Pál utcai fiúk' (The Paul Street Boys). Set in 1889 Budapest, the boys of Pál Street defend their sacred playground—the Grund—against the rival Redshirts led by Feri Áts. The quiet, fragile private Nemecsek Ernő proves that true greatness, honor, and loyalty do not belong to ranks or physical stature, giving his very life to defend his friends and the soil of freedom.",
        "characters": [
            "Nemecsek Ernő, a Pál utcaiak egyetlen közlegénye",
            "Boka János, a Pál utcaiak igazságos és érett elnöke",
            "Áts Feri, a vörösingesek nemes lelkű vezére",
            "Geréb Dezső, a megbánt áruló"
        ],
        "location": "Budapest, a Pál utcai grund és a Füvészkert",
        "author": "Molnár Ferenc",
        "work": "A Pál utcai fiúk (1906)",
        "paragraphs": [
            {
                "type": "narration",
                "text": "A Józsefvárosban, a Pál utca és a Mária utca sarkán feküdt egy üres telek, a grund. A palánkokkal körülvett, fahasábokkal teli térség a pesti fiúk számára a végtelen szabadságot, a prériről és a hazáról szőtt álmok szent birodalmát jelentette. Itt mindenki tiszt volt – csupán egyetlen kis szőke, vékony fiú maradt egyszerű közlegény: Nemecsek Ernő."
            },
            {
                "type": "narration",
                "text": "Ám a grundra szemet vetettek a Füvészkertben tanyázó vörösingesek. Vezérük, a félelmetes hírű Áts Feri elhatározta: labdázóhelynek elfoglalják a Pál utcaiak birodalmát. Amikor Geréb elárulta társait, a bátor Nemecsek egyedül lopózott be a Füvészkertbe, s a fa lombjai közül hallgatta végig az árulást."
            },
            {
                "type": "dialogue",
                "speaker": "Áts Feri vezér",
                "text": "Ki merészelt ide belopózni? Te vagy az a kis legény a Pál utcából? Állj be közénk a vörösingesekhez, és azonnal hadnagy leszel!"
            },
            {
                "type": "dialogue",
                "speaker": "Nemecsek Ernő közlegény",
                "text": "Soha! Inkább fojtsatok vízbe, de én soha nem leszek áruló! Nem hagyom el a grundot és a barátaimat semmilyen rangért!"
            },
            {
                "type": "narration",
                "text": "A vörösingesek a tó hideg vizébe fürdették a dacos kisfiút. Nemecsek súlyosan megfázott, tüdőgyulladást kapott és lázasan feküdt otthon a szegényes Rákos utcai szobában. Ám a nagy csata napján, amikor a vörösingesek rohamot indítottak a grund ellen, Nemecsek nem bírt az ágyban maradni."
            },
            {
                "type": "narration",
                "text": "Lázasan, tántorogva érkezett a harctérre a döntő pillanatban, s utolsó erejével földre terítette az erős Áts Ferit. A csata eldőlt: a Pál utcaiak győztek, a grund szabad maradt! Boka János azonnal főhadnaggyá léptette elő a kis hőst, s a Gittegylet fekete könyvében csupa nagybetűvel írták be nevét."
            },
            {
                "type": "dialogue",
                "speaker": "Boka János elnök",
                "text": "Nemecsek... kicsi Ernőm... te vagy a legbátrabb közülünk! Megmentetted a grundot mindannyiunknak!"
            },
            {
                "type": "narration",
                "text": "Néhány nappal később Nemecsek Ernő csendben elhunyt a szülei és Boka könnyei között. A grund megmenekült, ám hamarosan kiderült: a telket egy bérház építésére adták el. Boka némán nézett a deszkapalánkokra, s a gyermeki szívében megértette: a világ néha elragadja azt, amiért a legdrágábbat, az életünket is feláldoztuk."
            }
        ]
    }
    write_json("content/hu/stories/classics/b1/b1-27-molnar.json", story_classic)

    # -------------------------------------------------------------------------
    # 5. Lesson Files (01 to 05 + consolidation)
    # -------------------------------------------------------------------------
    lesson_titles = {
        "01": ("Társasági összejövetelek és vendégszeretet", "Gatherings, Conversation & Hospitality"),
        "02": ("Nézeteltérések és kompromisszumok", "Resolving Misunderstandings & Compromises"),
        "03": ("Bizalom, őszinteség és titoktartás", "Trust, Sincerity & Keeping Secrets"),
        "04": ("Közösség, bajtársiasság és összetartás", "Community, Camaraderie & Loyalty"),
        "05": ("Empátia, figyelmesség és emberi gesztusok", "Empathy, Thoughtfulness & Gestures")
    }

    grammar_refs = {
        "01": ["grammar/b1/b1-27-01-a-gr.json", "grammar/b1/b1-27-01-b-gr.json"],
        "02": ["grammar/b1/b1-27-02-a-gr.json", "grammar/b1/b1-27-02-b-gr.json"],
        "03": ["grammar/b1/b1-27-03-a-gr.json", "grammar/b1/b1-27-03-b-gr.json"],
        "04": ["grammar/b1/b1-27-04-a-gr.json", "grammar/b1/b1-27-04-b-gr.json"],
        "05": ["grammar/b1/b1-27-05-a-gr.json", "grammar/b1/b1-27-05-b-gr.json"]
    }

    for i in range(1, 6):
        padded = f"0{i}"
        hu_t, en_t = lesson_titles[padded]
        lesson_data = {
            "id": f"lesson.b1.27-{padded}",
            "unit": 27,
            "title": f"{hu_t} ({en_t})",
            "level": "B1",
            "grammar": "Reported Speech, Interpersonal Modality & Social Cohesion in Hungarian",
            "sections": [
                {
                    "type": "goal",
                    "title": "Lesson Goals",
                    "items": [
                        f"I can discuss {en_t} in fluent Hungarian.",
                        "I can report statements, questions, and requests using authentic indirect syntax.",
                        "I can use targeted interpersonal vocabulary for trust, empathy, and conflict resolution.",
                        "I can appreciate classic Hungarian cultural themes of community and sacrifice."
                    ]
                },
                {"type": "recycle", "count": 3},
                {"type": "vocabulary", "ref": f"vocabulary/b1/b1-27-{padded}-voc.json"},
                {"type": "grammar", "ref": grammar_refs[padded][0]},
                {"type": "grammar", "ref": grammar_refs[padded][1]},
                {
                    "type": "exercise-group",
                    "title": "Practice",
                    "ref": f"exercises/b1/b1-27-{padded}-ex.json",
                    "exerciseRefs": [f"b1-27-{padded}.ex0{k}" for k in range(1, 9)]
                }
            ]
        }
        write_json(f"content/hu/lessons/b1/b1-27-{padded}.json", lesson_data)

    consolidation_data = {
        "id": "lesson.b1.27-consolidation",
        "unit": 27,
        "title": "Unit 27 Consolidation",
        "level": "B1",
        "grammar": "Consolidation of Social Communication, Indirect Speech & Molnár's The Paul Street Boys",
        "sections": [
            {
                "type": "story",
                "title": "A Pál utcai fiúk (Molnár Ferenc)",
                "ref": "stories/classics/b1/b1-27-molnar.json"
            },
            {
                "type": "exercise-group",
                "title": "Consolidation Practice",
                "ref": "exercises/b1/b1-27-consolidation-ex.json",
                "exerciseRefs": [f"b1-27-consolidation.ex0{k}" for k in range(1, 9)]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-27-consolidation.json", consolidation_data)
    print("Successfully built Hungarian B1 Core Unit 27 (b1-27)!")

if __name__ == "__main__":
    build_unit_27_core()
