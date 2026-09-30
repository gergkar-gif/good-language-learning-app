#!/usr/bin/env python3
"""Generate Hungarian B1 Core Unit 7: Education & Learning (b1-07)."""

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

def build_unit_7_core():
    # -------------------------------------------------------------------------
    # 1. Vocabulary Files
    # -------------------------------------------------------------------------
    voc_01 = {
        "id": "vocab.b1.07.01",
        "lesson": "b1-07-01",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "iskolarendszer", "translation": "school system", "pos": "noun"},
            {"lemma": "általános iskola", "translation": "primary / elementary school", "pos": "noun"},
            {"lemma": "gimnázium", "translation": "grammar school / academic secondary school", "pos": "noun"},
            {"lemma": "érettségi", "translation": "school-leaving examination / matura", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-07-01-voc.json", voc_01)

    voc_02 = {
        "id": "vocab.b1.07.02",
        "lesson": "b1-07-02",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "képzés", "translation": "training, education, course", "pos": "noun"},
            {"lemma": "szakismeret", "translation": "specialised knowledge, expertise", "pos": "noun"},
            {"lemma": "célkitűzés", "translation": "objective, goal", "pos": "noun"},
            {"lemma": "fejleszt", "translation": "to develop, improve", "pos": "verb"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-07-02-voc.json", voc_02)

    voc_03 = {
        "id": "vocab.b1.07.03",
        "lesson": "b1-07-03",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "jegyzetel", "translation": "to take notes", "pos": "verb"},
            {"lemma": "összpontosít", "translation": "to concentrate, focus", "pos": "verb"},
            {"lemma": "ismétlés", "translation": "revision, repetition", "pos": "noun"},
            {"lemma": "módszer", "translation": "method, technique", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-07-03-voc.json", voc_03)

    voc_04 = {
        "id": "vocab.b1.07.04",
        "lesson": "b1-07-04",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "szóbeli", "translation": "oral examination / oral", "pos": "noun"},
            {"lemma": "írásbeli", "translation": "written examination / written", "pos": "noun"},
            {"lemma": "érdemjegy", "translation": "grade, mark", "pos": "noun"},
            {"lemma": "bizonyítvány", "translation": "report card, certificate", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-07-04-voc.json", voc_04)

    voc_05 = {
        "id": "vocab.b1.07.05",
        "lesson": "b1-07-05",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "önképzés", "translation": "self-education, self-study", "pos": "noun"},
            {"lemma": "átképzés", "translation": "retraining, vocational retraining", "pos": "noun"},
            {"lemma": "kíváncsiság", "translation": "curiosity", "pos": "noun"},
            {"lemma": "lehetőség", "translation": "opportunity, possibility", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-07-05-voc.json", voc_05)

    # -------------------------------------------------------------------------
    # 2. Grammar Files
    # -------------------------------------------------------------------------
    gr_01_a = {
        "id": "grammar.b1.07.01.potential-hat-het",
        "title": "The Potential Suffix: -hat / -het in Rules & Possibilities",
        "sections": [
            {
                "type": "text",
                "title": "Expressing capability and permission with -hat / -het",
                "content": "The suffix *-hat / -het* is attached directly to the verb stem before any personal endings. It indicates possibility, permission, or capability ('may', 'can'). In educational and institutional contexts, it is widely used to state rules, admissions criteria, and rights."
            },
            {
                "type": "table",
                "title": "Forming the potential verb stem",
                "rows": [
                    ["jelentkezik", "jelentkezhet (one may apply / can apply)"],
                    ["tanul", "tanulhat (one can study / may study)"],
                    ["felvételizik", "felvételizhet (one may sit the entrance exam)"],
                    ["választ", "választhat (one can choose / is allowed to choose)"]
                ]
            },
            {
                "type": "examples",
                "title": "Examples in educational contexts",
                "items": [
                    {
                        "spanish": "A diákok az általános iskola után gimnáziumba jelentkezhetnek.",
                        "english": "Students can apply to a grammar school after primary school."
                    },
                    {
                        "spanish": "Az érettségi vizsgán két idegen nyelvet is választhatsz.",
                        "english": "At the school-leaving exam, you can choose two foreign languages as well."
                    },
                    {
                        "spanish": "Mindenki ingyenesen tanulhat az állami iskolákban.",
                        "english": "Everyone can study free of charge in state schools."
                    }
                ]
            },
            {
                "type": "tip",
                "content": "Vowel harmony applies: back-vowel verbs take *-hat* (*tanulhat*, *maradhat*), while front-vowel verbs take *-het* (*kérhet*, *jelentkezhet*). Note that the potential stem conjugates regularly in definite and indefinite conjugations: *megtanulhatja* (he can learn it)."
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-07-01-a-gr.json", gr_01_a)

    gr_01_b = {
        "id": "grammar.b1.07.01.school-postpositions",
        "title": "Institutional Stages: után, előtt, közben",
        "sections": [
            {
                "type": "text",
                "title": "Sequencing educational stages with postpositions",
                "content": "To describe the chronological flow through the school system, temporal postpositions like *után* (after), *előtt* (before), and *közben* (during) follow nouns in the nominative case."
            },
            {
                "type": "examples",
                "title": "Postpositions in education narratives",
                "items": [
                    {
                        "spanish": "Az érettségi előtt a diákok sokat ismételnek.",
                        "english": "Before the school-leaving exam, students revise a lot."
                    },
                    {
                        "spanish": "A gimnázium után egyetemre szeretnék menni.",
                        "english": "After grammar school, I would like to go to university."
                    },
                    {
                        "spanish": "A képzés közben sok gyakorlati tapasztalatot szerzünk.",
                        "english": "During the course, we gain a lot of practical experience."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-07-01-b-gr.json", gr_01_b)

    gr_02 = {
        "id": "grammar.b1.07.02.purpose-azert-hogy",
        "title": "Expressing Purpose: azért, hogy + Subjunctive",
        "sections": [
            {
                "type": "text",
                "title": "Explaining purpose with azért, hogy",
                "content": "To explain the purpose behind an action ('in order to', 'so that'), Hungarian uses the correlative pair *azért ..., hogy ...* followed by the subjunctive/imperative mood (*-jon / -jen / -jön*)."
            },
            {
                "type": "examples",
                "title": "Purpose clauses in study motivation",
                "items": [
                    {
                        "spanish": "Azért járok erre a tanfolyamra, hogy új szakismeretet szerezzek.",
                        "english": "I attend this course in order to acquire specialized knowledge."
                    },
                    {
                        "spanish": "Azért tanulunk nyelveket, hogy könnyebben találjunk munkát.",
                        "english": "We learn languages so that we can find a job more easily."
                    },
                    {
                        "spanish": "A cég új képzést szervez, hogy fejlessze a munkatársak tudását.",
                        "english": "The company is organizing a new training program so as to develop employees' skills."
                    }
                ]
            },
            {
                "type": "tip",
                "content": "In speech, the main clause *azért* can be placed right next to the verb or emphatic position: *Azért tanulok, hogy átmenjek a vizsgán.* (I am studying in order to pass the exam)."
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-07-02-gr.json", gr_02)

    gr_03 = {
        "id": "grammar.b1.07.03.effective-study-verbs",
        "title": "Verbs of Study & Attention: összpontosít, jegyzetel",
        "sections": [
            {
                "type": "text",
                "title": "Case government with study verbs",
                "content": "Certain verbs describing cognitive effort take specific Hungarian noun cases: *összpontosít vmire* takes the sublative case (*-ra / -re* = onto), while *figyel vmire* behaves similarly."
            },
            {
                "type": "examples",
                "title": "Study verbs with cases",
                "items": [
                    {
                        "spanish": "A nehéz feladatokra kell összpontosítanunk.",
                        "english": "We must focus on the difficult exercises."
                    },
                    {
                        "spanish": "Óra alatt mindig füzetbe jegyzetelek.",
                        "english": "During class, I always take notes in a notebook."
                    },
                    {
                        "spanish": "A rendszeres ismétlés a leghatékonyabb módszer.",
                        "english": "Regular revision is the most effective method."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-07-03-gr.json", gr_03)

    gr_04 = {
        "id": "grammar.b1.07.04.exam-collocations",
        "title": "Collocations for Exams & Grades: vizsgázik, átmegy, megbukik",
        "sections": [
            {
                "type": "text",
                "title": "Talking about exam results and grading",
                "content": "In Hungarian, students say *átmegy a vizsgán* (to pass an exam, lit. go across on the exam with superessive *-n*) and *megbukik a vizsgán* (to fail an exam). Grades are referred to as *érdemjegyek* from 1 to 5."
            },
            {
                "type": "examples",
                "title": "Exam expressions",
                "items": [
                    {
                        "spanish": "A szóbeli vizsga után kaptam meg a jó érdemjegyet.",
                        "english": "After the oral exam, I received the good mark."
                    },
                    {
                        "spanish": "Mindenki sikeresen átment az írásbeli vizsgán.",
                        "english": "Everyone successfully passed the written exam."
                    },
                    {
                        "spanish": "Jó bizonyítvánnyal fejezte be a tanévet.",
                        "english": "He finished the school year with a good report card."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-07-04-gr.json", gr_04)

    gr_05 = {
        "id": "grammar.b1.07.05.synthesis",
        "title": "Synthesizing Potential, Purpose & Lifelong Learning",
        "sections": [
            {
                "type": "text",
                "title": "Expressing continuous self-improvement",
                "content": "By combining *-hat / -het* potential forms with purpose clauses (*azért, hogy*) and nominal compounds (*önképzés*, *átképzés*), you can discuss adult education, changing careers, and intellectual curiosity."
            },
            {
                "type": "examples",
                "title": "Lifelong learning reflections",
                "items": [
                    {
                        "spanish": "Az önképzés révén az ember bármilyen életkorban új szakmát tanulhat.",
                        "english": "Through self-education, a person can learn a new profession at any age."
                    },
                    {
                        "spanish": "A felnőttkori átképzés nagyszerű lehetőség a munkaerőpiacon.",
                        "english": "Adult retraining is a wonderful opportunity on the job market."
                    },
                    {
                        "spanish": "A szellemi kíváncsiság segít abban, hogy friss maradjon a gondolkodásunk.",
                        "english": "Intellectual curiosity helps in keeping our thinking sharp."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-07-05-gr.json", gr_05)

    # -------------------------------------------------------------------------
    # 3. Classic Reading: Karinthy Frigyes: Tanár úr kérem
    # -------------------------------------------------------------------------
    classic_07 = {
        "id": "story.b1.07.classic",
        "title": "A rossz tanuló felel",
        "level": "B1",
        "lesson": 5,
        "order": 5,
        "type": "classics",
        "estimatedMinutes": 6,
        "characters": ["A tanár úr", "Steinmann", "A rossz tanuló"],
        "grammar": ["potential-hat-het", "purpose-azert-hogy", "exam-collocations"],
        "vocabularyTopics": ["education", "school", "exams", "psychology"],
        "summary": "An adapted retelling inspired by Frigyes Karinthy's humorous masterpiece Tanár úr kérem: an unprepared student is called up to the blackboard, experiencing the universal drama of school oral examination and attempting to bluff his way through.",
        "source": "Adaptation inspired by the public-domain work Tanár úr kérem by Frigyes Karinthy",
        "author": "Frigyes Karinthy",
        "work": "Tanár úr kérem",
        "paragraphs": [
            {
                "type": "narration",
                "text": "A tanteremben hirtelen nagy csend támadt. A tanár úr lassan felnyitotta a nagy, vörös osztálynaplót, és a ceruzája hegyével végigfutott a neveken. Minden diák visszatartotta a lélegzetét: vajon ki felel ma fizikából?"
            },
            {
                "type": "narration",
                "text": "A hátsó padban ülő diák görcsösen a füzetét bámulja. Egész este azért ült az asztalnál, hogy megtanulja a nehéz leckét, de alig maradt valami a fejében. „Bárcsak ne engem szólítana!” — gondolja magában kétségbeesve."
            },
            {
                "type": "narration",
                "text": "„Felelni fog... Steinmann!” — hangzik a rettegett döntés. A rossz tanuló lassan feláll, mintha nehéz köveket cipelne a hátán. Kilép a padból, és végtelenül hosszú percek alatt elér a fekete tábláig. A krétát remegő kézzel veszi fel a tartóból."
            },
            {
                "type": "narration",
                "text": "„Nos, fiam, mondja el a leckét az elektromos áramról!” — szól a tanár úr nyugodt hangon. A diák köhécsel, megigazítja az ingét, és próbál magabiztosnak látszani. „Az elektromos áram... az egy olyan dolog, tanár úr kérem... ami áramlik. És azért van, hogy világítson a lámpa.”"
            },
            {
                "type": "narration",
                "text": "Az osztályban néhányan fojtottan nevetnek, de a tanár úr szeme szigorúan villan. „Ne mellébeszéljen, fiam! Mi a pontos törvény?” A diák a táblára rajzol egy bizonytalan vonalat, miközben az ablakon túli tavaszi napsütésre pillant: kint szabadság van, madarak énekelnek, itt bent viszont élet-halál harc folyik egy kettesért."
            },
            {
                "type": "narration",
                "text": "Végül a tanár úr sóhajt egy nagyot, és becsukja a naplót: „Üljön le, fiam. Magának még sokat kell ismételnie, hogy átmenjen az év végi vizsgán.” A diák visszasiet a helyére, és boldog sóhajjal roskad le: a vihar elmúlt, ma már senki sem hívhatja ki a táblához."
            }
        ]
    }
    write_json("content/hu/stories/classics/b1/b1-07-tanarurkerem.json", classic_07)

    # -------------------------------------------------------------------------
    # 4. Exercise Files
    # -------------------------------------------------------------------------
    ex_01 = {
        "lesson": "b1-07-01",
        "exercises": [
            {
                "id": "b1-07-01-intro-1",
                "type": "multiple-choice",
                "category": "introduce",
                "question": "Which suffix attaches to verb stems to express potential/permission ('can', 'may')?",
                "options": ["-hat / -het", "-gat / -get", "-oz / -ez"],
                "correct": 0,
                "teaches": ["potential-hat-het"]
            },
            {
                "id": "b1-07-01-intro-2",
                "type": "multiple-choice",
                "category": "introduce",
                "question": "What is the Hungarian term for the secondary school-leaving exam?",
                "options": ["érettségi", "általános iskola", "képzés"],
                "correct": 0,
                "teaches": ["school-vocab"]
            },
            {
                "id": "b1-07-01-controlled-1",
                "type": "matching",
                "category": "controlled",
                "pairs": [
                    ["iskolarendszer", "school system"],
                    ["általános iskola", "primary school"],
                    ["gimnázium", "grammar school"],
                    ["érettségi", "graduation exam"]
                ],
                "teaches": ["school-vocab"]
            },
            {
                "id": "b1-07-01-controlled-2",
                "type": "multiple-choice",
                "category": "controlled",
                "question": "Choose the correct potential form: 'A diákok könyvtárban is (tanul).' -> ...",
                "options": ["tanulhatnak", "tanulnak", "tanultak"],
                "correct": 0,
                "teaches": ["potential-hat-het"]
            },
            {
                "id": "b1-07-01-controlled-3",
                "type": "fill-blank",
                "category": "controlled",
                "sentence": "A nyolcadik osztály után a diákok gimnáziumba ____. (they can apply)",
                "answer": "jelentkezhetnek",
                "teaches": ["potential-hat-het"]
            },
            {
                "id": "b1-07-01-controlled-4",
                "type": "multiple-choice",
                "category": "controlled",
                "question": "Which word order is natural?",
                "options": [
                    "Az érettségi előtt a diákok sokat tanulnak.",
                    "Előtt az érettségi a diákok tanulnak sokat.",
                    "A diákok az előtt érettségi tanulnak."
                ],
                "correct": 0,
                "teaches": ["school-postpositions"]
            },
            {
                "id": "b1-07-01-practice-1",
                "type": "matching",
                "category": "practice",
                "pairs": [
                    ["jelentkezhet", "he/she may apply"],
                    ["választhat", "he/she can choose"],
                    ["tanulhat", "he/she can study"],
                    ["kérdezhet", "he/she may ask"]
                ],
                "teaches": ["potential-hat-het"]
            },
            {
                "id": "b1-07-01-practice-2",
                "type": "multiple-choice",
                "category": "practice",
                "question": "Hány évig tart általában a magyar általános iskola?",
                "options": ["Nyolc évig.", "Négy évig.", "Tizenkét évig."],
                "correct": 0,
                "teaches": ["hungarian-school-facts"]
            },
            {
                "id": "b1-07-01-practice-3",
                "type": "fill-in-the-blank",
                "category": "practice",
                "sentence": "Az állami iskolákban minden gyermek ingyen [tanulhat].",
                "options": ["tanulhat", "tanul", "tanult"],
                "correct": 0,
                "teaches": ["potential-hat-het"]
            },
            {
                "id": "b1-07-01-practice-4",
                "type": "multiple-choice",
                "category": "practice",
                "question": "Mit tesznek a diákok a gimnázium végén?",
                "options": ["Érettségi vizsgát tesznek.", "Általános iskolába mennek.", "Nyugdíjba mennek."],
                "correct": 0,
                "teaches": ["hungarian-school-facts"]
            },
            {
                "id": "b1-07-01-dialogue-1",
                "type": "multiple-choice",
                "category": "dialogue",
                "question": "— Hová jelentkezik a fiad az általános iskola után?\n— ...",
                "options": [
                    "Egy jó nevű gimnáziumba szeretne járni.",
                    "Már megkapta a nyugdíját.",
                    "Tegnap vett egy autót."
                ],
                "correct": 0,
                "teaches": ["school-dialogue"]
            },
            {
                "id": "b1-07-01-dialogue-2",
                "type": "multiple-choice",
                "category": "dialogue",
                "question": "— Nehéz volt az érettségi vizsga?\n— ...",
                "options": [
                    "Igen, de szerencsére jól sikerült.",
                    "Nem, mert nem vettem jegyet a vonatra.",
                    "Holnap reggel hétkor indul a repülőgép."
                ],
                "correct": 0,
                "teaches": ["school-dialogue"]
            },
            {
                "id": "b1-07-01-writing-1",
                "type": "multiple-choice",
                "category": "production",
                "question": "How do you say: 'Anyone can apply for this course.'?",
                "options": [
                    "Bárki jelentkezhet erre a képzésre.",
                    "Mindenki jelentkezik a képzésről.",
                    "Bárki jelentkezett a képzésen."
                ],
                "correct": 0,
                "teaches": ["production-potential"]
            },
            {
                "id": "b1-07-01-writing-2",
                "type": "multiple-choice",
                "category": "production",
                "question": "How do you say: 'The Hungarian school system is well structured.'?",
                "options": [
                    "A magyar iskolarendszer jól felépített.",
                    "A magyar iskola rendszere rosszul van.",
                    "Az iskolában a rendszer állandóan működik."
                ],
                "correct": 0,
                "teaches": ["production-school"]
            },
            {
                "id": "b1-07-01-check-1",
                "type": "multiple-choice",
                "category": "check",
                "question": "Which verb contains the potential suffix -hat/-het?",
                "options": ["választhat", "választott", "választás"],
                "correct": 0,
                "teaches": ["potential-check"]
            },
            {
                "id": "b1-07-01-check-2",
                "type": "multiple-choice",
                "category": "check",
                "question": "Which school comes immediately after primary school for academic students?",
                "options": ["gimnázium", "óvoda", "bölcsőde"],
                "correct": 0,
                "teaches": ["school-check"]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-07-01-ex.json", ex_01)

    ex_02 = {
        "lesson": "b1-07-02",
        "exercises": [
            {
                "id": "b1-07-02-intro-1",
                "type": "multiple-choice",
                "category": "introduce",
                "question": "Which clause construction expresses purpose ('in order that / so that')?",
                "options": ["azért ..., hogy ...", "akkor ..., amikor ...", "ott ..., ahol ..."],
                "correct": 0,
                "teaches": ["purpose-azert-hogy"]
            },
            {
                "id": "b1-07-02-intro-2",
                "type": "multiple-choice",
                "category": "introduce",
                "question": "What does 'szakismeret' mean?",
                "options": ["specialized knowledge / expertise", "hobby", "daily newspaper"],
                "correct": 0,
                "teaches": ["vocab-szakismeret"]
            },
            {
                "id": "b1-07-02-controlled-1",
                "type": "matching",
                "category": "controlled",
                "pairs": [
                    ["képzés", "training, course"],
                    ["szakismeret", "specialized knowledge"],
                    ["célkitűzés", "objective, goal"],
                    ["fejleszt", "to develop, improve"]
                ],
                "teaches": ["vocab-motivation"]
            },
            {
                "id": "b1-07-02-controlled-2",
                "type": "multiple-choice",
                "category": "controlled",
                "question": "Azért járok tanfolyamra, hogy új dolgokat ...",
                "options": ["tanuljak", "tanulok", "tanultam"],
                "correct": 0,
                "teaches": ["purpose-subjunctive"]
            },
            {
                "id": "b1-07-02-controlled-3",
                "type": "fill-in-the-blank",
                "category": "controlled",
                "sentence": "A cég képzést szervez, hogy [fejlessze] a dolgozók szaktudását.",
                "options": ["fejlessze", "fejleszti", "fejlesztette"],
                "correct": 0,
                "teaches": ["purpose-subjunctive"]
            },
            {
                "id": "b1-07-02-controlled-4",
                "type": "multiple-choice",
                "category": "controlled",
                "question": "Which sentence expresses a clear personal study goal?",
                "options": [
                    "Az a célkitűzésem, hogy folyékonyan beszéljek magyarul.",
                    "Tegnap megnéztem egy filmet a moziban.",
                    "A boltban kenyeret és tejet vásároltam."
                ],
                "correct": 0,
                "teaches": ["celkituzes-expression"]
            },
            {
                "id": "b1-07-02-practice-1",
                "type": "matching",
                "category": "practice",
                "pairs": [
                    ["fejleszti a tudását", "develops one's knowledge"],
                    ["fontos célkitűzés", "an important objective"],
                    ["hasznos képzés", "a useful training course"],
                    ["új szakismeret", "new specialized knowledge"]
                ],
                "teaches": ["vocab-collocations"]
            },
            {
                "id": "b1-07-02-practice-2",
                "type": "multiple-choice",
                "category": "practice",
                "question": "Miért fontos a szakmai képzés a mai világban?",
                "options": [
                    "Azért, hogy a munkavállalók korszerű ismeretekkel rendelkezzenek.",
                    "Azért, hogy senki ne dolgozzon soha.",
                    "Azért, hogy a könyvtárak bezárjanak."
                ],
                "correct": 0,
                "teaches": ["purpose-reading"]
            },
            {
                "id": "b1-07-02-practice-3",
                "type": "fill-in-the-blank",
                "category": "practice",
                "sentence": "Azért költöztem Budapestre, hogy egyetemre [járhassak].",
                "options": ["járhassak", "járok", "jártam"],
                "correct": 0,
                "teaches": ["purpose-potential"]
            },
            {
                "id": "b1-07-02-practice-4",
                "type": "multiple-choice",
                "category": "practice",
                "question": "Which sentence means 'We study so that we can find a good job'?",
                "options": [
                    "Azért tanulunk, hogy jó munkát találjunk.",
                    "Akkor tanulunk, amikor jó munkát találunk.",
                    "Addig tanulunk, amíg jó munkát nem kapunk."
                ],
                "correct": 0,
                "teaches": ["purpose-translation"]
            },
            {
                "id": "b1-07-02-dialogue-1",
                "type": "multiple-choice",
                "category": "dialogue",
                "question": "— Miért iratkoztál be erre az esti tanfolyamra?\n— ...",
                "options": [
                    "Azért, hogy elmélyítsem a szakmai tudásomat.",
                    "Mert elromlott a telefonom.",
                    "Tegnap este finom vacsorát főztem."
                ],
                "correct": 0,
                "teaches": ["dialogue-purpose"]
            },
            {
                "id": "b1-07-02-dialogue-2",
                "type": "multiple-choice",
                "category": "dialogue",
                "question": "— Milyen célkitűzéseid vannak az év végéig?\n— ...",
                "options": [
                    "Szeretném sikeresen befejezni a nyelvi képzést.",
                    "Nem szeretem az esős őszi napokat.",
                    "A vonat pontosan délben érkezik a pályaudvarra."
                ],
                "correct": 0,
                "teaches": ["dialogue-goals"]
            },
            {
                "id": "b1-07-02-writing-1",
                "type": "multiple-choice",
                "category": "production",
                "question": "How do you express: 'I practice every day so that I can improve.'?",
                "options": [
                    "Minden nap gyakorlok azért, hogy fejlődjek.",
                    "Minden nap gyakoroltam, mikor fejlődtem.",
                    "Gyakorolni fogok, holott fejlődök."
                ],
                "correct": 0,
                "teaches": ["production-purpose"]
            },
            {
                "id": "b1-07-02-writing-2",
                "type": "multiple-choice",
                "category": "production",
                "question": "How do you express: 'Specialized knowledge is necessary for the position.'?",
                "options": [
                    "A beosztáshoz megfelelő szakismeret szükséges.",
                    "A beosztásban nincsen semmilyen ismeret.",
                    "A pozícióról senki nem tud semmit."
                ],
                "correct": 0,
                "teaches": ["production-szakismeret"]
            },
            {
                "id": "b1-07-02-check-1",
                "type": "multiple-choice",
                "category": "check",
                "question": "Which verb form completes: 'Azért ment el, hogy ...'?",
                "options": ["beszéljen a tanárral", "beszélt a tanárral", "beszélni fog a tanárral"],
                "correct": 0,
                "teaches": ["check-purpose"]
            },
            {
                "id": "b1-07-02-check-2",
                "type": "multiple-choice",
                "category": "check",
                "question": "What is 'képzés' in English?",
                "options": ["training / course", "building", "vacation"],
                "correct": 0,
                "teaches": ["check-vocab"]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-07-02-ex.json", ex_02)

    # Lessons 03, 04, 05 and consolidation for Core 7
    ex_03 = {
        "lesson": "b1-07-03",
        "exercises": [
            {
                "id": "b1-07-03-intro-1",
                "type": "multiple-choice",
                "category": "introduce",
                "question": "Which case does the verb 'összpontosít' (to concentrate) take?",
                "options": ["sublative (-ra / -re)", "inessive (-ban / -ben)", "instrumental (-val / -vel)"],
                "correct": 0,
                "teaches": ["case-osszpontosit"]
            },
            {
                "id": "b1-07-03-intro-2",
                "type": "multiple-choice",
                "category": "introduce",
                "question": "What does 'jegyzetel' mean?",
                "options": ["to take notes", "to buy tickets", "to read loudly"],
                "correct": 0,
                "teaches": ["vocab-jegyzetel"]
            },
            {
                "id": "b1-07-03-controlled-1",
                "type": "matching",
                "category": "controlled",
                "pairs": [
                    ["jegyzetel", "to take notes"],
                    ["összpontosít", "to concentrate"],
                    ["ismétlés", "revision / repetition"],
                    ["módszer", "method / technique"]
                ],
                "teaches": ["vocab-study-methods"]
            },
            {
                "id": "b1-07-03-controlled-2",
                "type": "multiple-choice",
                "category": "controlled",
                "question": "A diák a nehéz feladatra ...",
                "options": ["összpontosít", "jegyzetel", "ismétel"],
                "correct": 0,
                "teaches": ["verb-government"]
            },
            {
                "id": "b1-07-03-controlled-3",
                "type": "fill-in-the-blank",
                "category": "controlled",
                "sentence": "A sikeres tanuláshoz jó [módszer] szükséges.",
                "options": ["módszer", "jegyzet", "óra"],
                "correct": 0,
                "teaches": ["modszer-usage"]
            },
            {
                "id": "b1-07-03-controlled-4",
                "type": "multiple-choice",
                "category": "controlled",
                "question": "Which collocation means 'regular revision'?",
                "options": ["rendszeres ismétlés", "gyors tanuló", "hangos jegyzet"],
                "correct": 0,
                "teaches": ["collocation-ismatles"]
            },
            {
                "id": "b1-07-03-practice-1",
                "type": "matching",
                "category": "practice",
                "pairs": [
                    ["figyelmesen jegyzetel", "takes notes attentively"],
                    ["a lényegre összpontosít", "focuses on the essence"],
                    ["hatékony tanulási módszer", "effective study method"],
                    ["alapos ismétlés", "thorough revision"]
                ],
                "teaches": ["study-phrases"]
            },
            {
                "id": "b1-07-03-practice-2",
                "type": "multiple-choice",
                "category": "practice",
                "question": "Hogyan lehet a legkönnyebben megjegyezni az új szavakat?",
                "options": [
                    "Rendszeres ismétléssel és mondatokban való gyakorlással.",
                    "Úgy, hogy soha nem nyitjuk ki a könyvet.",
                    "Csak este tizenegy után tévénézéssel."
                ],
                "correct": 0,
                "teaches": ["study-comprehension"]
            },
            {
                "id": "b1-07-03-practice-3",
                "type": "fill-in-the-blank",
                "category": "practice",
                "sentence": "Az előadáson a hallgatók a füzetükbe [jegyzetelnek].",
                "options": ["jegyzetelnek", "olvasnak", "alszanak"],
                "correct": 0,
                "teaches": ["jegyzetel-conjugation"]
            },
            {
                "id": "b1-07-03-practice-4",
                "type": "multiple-choice",
                "category": "practice",
                "question": "Mit jelent: 'Összpontosíts a vizsgára!'?",
                "options": ["Focus on the exam!", "Forget the exam!", "Sign up for the exam!"],
                "correct": 0,
                "teaches": ["translation-osszpontosit"]
            },
            {
                "id": "b1-07-03-dialogue-1",
                "type": "multiple-choice",
                "category": "dialogue",
                "question": "— Nem bírom megjegyezni ezt a sok szabályt!\n— ...",
                "options": [
                    "Próbálj meg sémákat rajzolni és rendszeresen ismételni!",
                    "Akkor kapcsold ki a villanyt és aludj!",
                    "Vegyél egy kiló almát a piacon!"
                ],
                "correct": 0,
                "teaches": ["study-advice-dialogue"]
            },
            {
                "id": "b1-07-03-dialogue-2",
                "type": "multiple-choice",
                "category": "dialogue",
                "question": "— Szoktál jegyzetelni az órákon?\n— ...",
                "options": [
                    "Igen, mert a leírt gondolatokra jobban tudok emlékezni.",
                    "Nem, mert a vonat már elment.",
                    "Tegnap este kenyeret sütöttem."
                ],
                "correct": 0,
                "teaches": ["note-taking-dialogue"]
            },
            {
                "id": "b1-07-03-writing-1",
                "type": "multiple-choice",
                "category": "production",
                "question": "How do you say: 'I cannot concentrate because of the noise.'?",
                "options": [
                    "A zaj miatt nem tudok összpontosítani.",
                    "A zajra nem figyelek soha.",
                    "Zajosan jegyzetelek az irodában."
                ],
                "correct": 0,
                "teaches": ["production-focus"]
            },
            {
                "id": "b1-07-03-writing-2",
                "type": "multiple-choice",
                "category": "production",
                "question": "How do you say: 'Which method do you find most effective?'?",
                "options": [
                    "Melyik módszert találod a leghatékonyabbnak?",
                    "Mikor kezded a tanulást a szobában?",
                    "Hány füzetbe jegyzeteltél ma délután?"
                ],
                "correct": 0,
                "teaches": ["production-method"]
            },
            {
                "id": "b1-07-03-check-1",
                "type": "multiple-choice",
                "category": "check",
                "question": "Which noun means 'repetition' or 'revision'?",
                "options": ["ismétlés", "tanítás", "vizsgázás"],
                "correct": 0,
                "teaches": ["check-ismatles"]
            },
            {
                "id": "b1-07-03-check-2",
                "type": "multiple-choice",
                "category": "check",
                "question": "Fill in: 'Összpontosíts a ...' (the exercise)",
                "options": ["feladatra", "feladatban", "feladatról"],
                "correct": 0,
                "teaches": ["check-government"]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-07-03-ex.json", ex_03)

    ex_04 = {
        "lesson": "b1-07-04",
        "exercises": [
            {
                "id": "b1-07-04-intro-1",
                "type": "multiple-choice",
                "category": "introduce",
                "question": "What is the difference between 'szóbeli' and 'írásbeli'?",
                "options": ["oral vs written", "easy vs hard", "morning vs evening"],
                "correct": 0,
                "teaches": ["exam-types"]
            },
            {
                "id": "b1-07-04-intro-2",
                "type": "multiple-choice",
                "category": "introduce",
                "question": "Which phrase means 'to pass an exam'?",
                "options": ["átmegy a vizsgán", "megbukik a vizsgán", "vizsgát ír"],
                "correct": 0,
                "teaches": ["pass-exam-phrase"]
            },
            {
                "id": "b1-07-04-controlled-1",
                "type": "matching",
                "category": "controlled",
                "pairs": [
                    ["szóbeli", "oral exam"],
                    ["írásbeli", "written exam"],
                    ["érdemjegy", "grade, mark"],
                    ["bizonyítvány", "report card, certificate"]
                ],
                "teaches": ["vocab-exams"]
            },
            {
                "id": "b1-07-04-controlled-2",
                "type": "multiple-choice",
                "category": "controlled",
                "question": "Péter kitűnő ... kapott a dolgozatára.",
                "options": ["érdemjegyet", "bizonyítványt", "iskolát"],
                "correct": 0,
                "teaches": ["erdemjegy-usage"]
            },
            {
                "id": "b1-07-04-controlled-3",
                "type": "fill-in-the-blank",
                "category": "controlled",
                "sentence": "A sikeres érettségi után mindenki átvehette a [bizonyítványát].",
                "options": ["bizonyítványát", "jegyzetét", "tollát"],
                "correct": 0,
                "teaches": ["bizonyitvany-usage"]
            },
            {
                "id": "b1-07-04-controlled-4",
                "type": "multiple-choice",
                "category": "controlled",
                "question": "Which sentence is correct?",
                "options": [
                    "Anna sikeresen átment a szóbeli vizsgán.",
                    "Anna sikeresen átment a szóbeli vizsgára.",
                    "Anna szóbeli vizsgában átment sikeresen."
                ],
                "correct": 0,
                "teaches": ["exam-case-governance"]
            },
            {
                "id": "b1-07-04-practice-1",
                "type": "matching",
                "category": "practice",
                "pairs": [
                    ["kitűnő érdemjegy", "excellent grade (5)"],
                    ["elégtelen osztályzat", "failing grade (1)"],
                    ["szóbeli felelet", "oral recitation"],
                    ["írásbeli teszt", "written test"]
                ],
                "teaches": ["grading-terms"]
            },
            {
                "id": "b1-07-04-practice-2",
                "type": "multiple-choice",
                "category": "practice",
                "question": "Milyen érdemjegy a legjobb a magyar iskolákban?",
                "options": ["Az ötös (jeles/kitűnő).", "Az egyes.", "A tízes."],
                "correct": 0,
                "teaches": ["hungarian-grading-system"]
            },
            {
                "id": "b1-07-04-practice-3",
                "type": "fill-in-the-blank",
                "category": "practice",
                "sentence": "Sokat tanultam, ezért biztosan nem [bukom] meg a vizsgán.",
                "options": ["bukom", "megyek", "írok"],
                "correct": 0,
                "teaches": ["megbukik-usage"]
            },
            {
                "id": "b1-07-04-practice-4",
                "type": "multiple-choice",
                "category": "practice",
                "question": "Mit jelent a 'bizonyítványosztás'?",
                "options": [
                    "Distribution of end-of-year report cards.",
                    "Writing an exam.",
                    "Buying school textbooks."
                ],
                "correct": 0,
                "teaches": ["cultural-school-terms"]
            },
            {
                "id": "b1-07-04-dialogue-1",
                "type": "multiple-choice",
                "category": "dialogue",
                "question": "— Hogy sikerült a szóbeli vizsgád?\n— ...",
                "options": [
                    "Nagyon jól, ötöst kaptam a tanár úrtól!",
                    "A vonat tíz percet késett.",
                    "Nem vettem új cipőt tegnap."
                ],
                "correct": 0,
                "teaches": ["exam-result-dialogue"]
            },
            {
                "id": "b1-07-04-dialogue-2",
                "type": "multiple-choice",
                "category": "dialogue",
                "question": "— Mikor kapjátok meg a bizonyítványt?\n— ...",
                "options": [
                    "Június végén, a tanévzáró ünnepségen.",
                    "Minden kedden délután kettőkor.",
                    "A postás hozza majd a levelet."
                ],
                "correct": 0,
                "teaches": ["report-card-dialogue"]
            },
            {
                "id": "b1-07-04-writing-1",
                "type": "multiple-choice",
                "category": "production",
                "question": "How do you say: 'I passed both the written and oral exams.'?",
                "options": [
                    "Az írásbeli és a szóbeli vizsgán is átmentem.",
                    "Az írásbeliről és szóbeliről eljöttem.",
                    "Írásban és szóban vizsgát csináltam."
                ],
                "correct": 0,
                "teaches": ["production-exam-pass"]
            },
            {
                "id": "b1-07-04-writing-2",
                "type": "multiple-choice",
                "category": "production",
                "question": "How do you say: 'He received a good grade on his essay.'?",
                "options": [
                    "Jó érdemjegyet kapott az esszéjére.",
                    "Jó bizonyítvánnyal esszét írt.",
                    "Érdemes volt esszét olvasnia."
                ],
                "correct": 0,
                "teaches": ["production-grade"]
            },
            {
                "id": "b1-07-04-check-1",
                "type": "multiple-choice",
                "category": "check",
                "question": "What is 'írásbeli' in English?",
                "options": ["written (exam)", "oral (exam)", "practical"],
                "correct": 0,
                "teaches": ["check-irasbeli"]
            },
            {
                "id": "b1-07-04-check-2",
                "type": "multiple-choice",
                "category": "check",
                "question": "Which verb pairs with 'meg a vizsgán' to mean fail?",
                "options": ["megbukik", "megy", "áll"],
                "correct": 0,
                "teaches": ["check-megbukik"]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-07-04-ex.json", ex_04)

    ex_05 = {
        "lesson": "b1-07-05",
        "exercises": [
            {
                "id": "b1-07-05-intro-1",
                "type": "multiple-choice",
                "category": "introduce",
                "question": "What does 'önképzés' mean?",
                "options": ["self-education / independent learning", "school test", "group project"],
                "correct": 0,
                "teaches": ["vocab-onkepzes"]
            },
            {
                "id": "b1-07-05-intro-2",
                "type": "multiple-choice",
                "category": "introduce",
                "question": "What does 'átképzés' mean?",
                "options": ["retraining (for a new field)", "failing an exam", "graduating"],
                "correct": 0,
                "teaches": ["vocab-atkepzes"]
            },
            {
                "id": "b1-07-05-controlled-1",
                "type": "matching",
                "category": "controlled",
                "pairs": [
                    ["önképzés", "self-education"],
                    ["átképzés", "retraining"],
                    ["kíváncsiság", "curiosity"],
                    ["lehetőség", "opportunity"]
                ],
                "teaches": ["vocab-lifelong-learning"]
            },
            {
                "id": "b1-07-05-controlled-2",
                "type": "multiple-choice",
                "category": "controlled",
                "question": "A felnőttkori tanulás új ... nyit a munkaerőpiacon.",
                "options": ["lehetőségeket", "vizsgákat", "naplókat"],
                "correct": 0,
                "teaches": ["lehetoseg-usage"]
            },
            {
                "id": "b1-07-05-controlled-3",
                "type": "fill-in-the-blank",
                "category": "controlled",
                "sentence": "A szellemi [kíváncsiság] segít abban, hogy mindig új dolgokat fedezzünk fel.",
                "options": ["kíváncsiság", "fáradtság", "unalom"],
                "correct": 0,
                "teaches": ["kivancsisag-usage"]
            },
            {
                "id": "b1-07-05-controlled-4",
                "type": "multiple-choice",
                "category": "controlled",
                "question": "Which sentence reflects lifelong learning?",
                "options": [
                    "Az ember élete végéig tanulhat és fejlődhet.",
                    "Az iskola után soha többé nem szabad könyvet olvasni.",
                    "A tanulás csak a gyerekek feladata."
                ],
                "correct": 0,
                "teaches": ["lifelong-concept"]
            },
            {
                "id": "b1-07-05-practice-1",
                "type": "matching",
                "category": "practice",
                "pairs": [
                    ["szakmai átképzés", "vocational retraining"],
                    ["folyamatos önképzés", "continuous self-study"],
                    ["kiváló lehetőség", "excellent opportunity"],
                    ["természetes kíváncsiság", "natural curiosity"]
                ],
                "teaches": ["collocations-lifelong"]
            },
            {
                "id": "b1-07-05-practice-2",
                "type": "multiple-choice",
                "category": "practice",
                "question": "Miért van szükség ma felnőttkori átképzésre?",
                "options": [
                    "Mert a gazdaság és a technológia gyorsan változik.",
                    "Mert nincsenek általános iskolák.",
                    "Mert mindenki tanár akar lenni."
                ],
                "correct": 0,
                "teaches": ["lifelong-reading"]
            },
            {
                "id": "b1-07-05-practice-3",
                "type": "fill-in-the-blank",
                "category": "practice",
                "sentence": "Az internet segítségével az [önképzés] mindenki számára elérhetővé vált.",
                "options": ["önképzés", "érettségi", "érdemjegy"],
                "correct": 0,
                "teaches": ["onkepzes-context"]
            },
            {
                "id": "b1-07-05-practice-4",
                "type": "multiple-choice",
                "category": "practice",
                "question": "Mit jelent az 'élethosszig tartó tanulás'?",
                "options": [
                    "Lifelong learning.",
                    "Studying all night.",
                    "Ten years of university."
                ],
                "correct": 0,
                "teaches": ["elethosszig-translation"]
            },
            {
                "id": "b1-07-05-dialogue-1",
                "type": "multiple-choice",
                "category": "dialogue",
                "question": "— Nem félsz negyvenévesen új szakmát tanulni?\n— ...",
                "options": [
                    "Nem, mert az átképzés nagyszerű lehetőség az újrakezdésre.",
                    "De igen, a tegnapi vacsora hideg volt.",
                    "Nem találtam meg a villamosbérletemet."
                ],
                "correct": 0,
                "teaches": ["retraining-dialogue"]
            },
            {
                "id": "b1-07-05-dialogue-2",
                "type": "multiple-choice",
                "category": "dialogue",
                "question": "— Hogyan fejleszted az angoltudásodat az egyetem után?\n— ...",
                "options": [
                    "Önképzéssel: mindennap podcastokat hallgatok és cikkeket olvasok.",
                    "Minden reggel taxival járok a munkahelyemre.",
                    "Nem vettem új számítógépet a boltban."
                ],
                "correct": 0,
                "teaches": ["self-study-dialogue"]
            },
            {
                "id": "b1-07-05-writing-1",
                "type": "multiple-choice",
                "category": "production",
                "question": "How do you say: 'Curiosity drives us to discover new things.'?",
                "options": [
                    "A kíváncsiság ösztönöz minket új dolgok felfedezésére.",
                    "A kíváncsi ember sosem tanul semmit.",
                    "Kíváncsian néztem a televíziót este."
                ],
                "correct": 0,
                "teaches": ["production-kivancsisag"]
            },
            {
                "id": "b1-07-05-writing-2",
                "type": "multiple-choice",
                "category": "production",
                "question": "How do you say: 'Retraining offers new career paths.'?",
                "options": [
                    "Az átképzés új karrierutakat kínál.",
                    "Az átképzésről senki nem beszélt az irodában.",
                    "A képzés alatt sokat sétáltam a városban."
                ],
                "correct": 0,
                "teaches": ["production-retraining"]
            },
            {
                "id": "b1-07-05-reading-1",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Karinthy Frigyes elbeszélésében kihez lép oda a rossz tanuló?",
                "options": [
                    "A fekete táblához és a tanár úrhoz.",
                    "A büféhez az udvaron.",
                    "A szomszéd iskola igazgatójához."
                ],
                "correct": 0,
                "teaches": ["karinthy-reading-1"]
            },
            {
                "id": "b1-07-05-reading-2",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Milyen tantárgyból szólítják fel felelni a diákot?",
                "options": ["Fizikából.", "Magyar irodalomból.", "Ének-zenéből."],
                "correct": 0,
                "teaches": ["karinthy-reading-2"]
            },
            {
                "id": "b1-07-05-reading-3",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Mit érez a rossz tanuló, amikor végül visszaülhet a helyére?",
                "options": [
                    "Hatalmas megkönnyebbülést, hogy véget ért a megpróbáltatás.",
                    "Haragot, hogy nem kapott ötöst.",
                    "Kedvet ahhoz, hogy újra feleljen."
                ],
                "correct": 0,
                "teaches": ["karinthy-reading-3"]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-07-05-ex.json", ex_05)

    ex_consolidation = {
        "lesson": "b1-07-consolidation",
        "exercises": [
            {
                "id": "b1-07-consolidation-1",
                "type": "matching",
                "category": "recognize",
                "pairs": [
                    ["iskolarendszer", "school system"],
                    ["érettségi", "school-leaving exam"],
                    ["szakismeret", "specialized knowledge"],
                    ["önképzés", "self-education"]
                ]
            },
            {
                "id": "b1-07-consolidation-2",
                "type": "matching",
                "category": "recognize",
                "pairs": [
                    ["gimnázium", "grammar school"],
                    ["jegyzetel", "to take notes"],
                    ["érdemjegy", "grade, mark"],
                    ["átképzés", "retraining"]
                ]
            },
            {
                "id": "b1-07-consolidation-3",
                "type": "multiple-choice",
                "category": "recognize",
                "question": "Which suffix indicates possibility/permission ('can/may')?",
                "options": ["-hat / -het", "-gat / -get", "-ság / -ség"],
                "correct": 0
            },
            {
                "id": "b1-07-consolidation-4",
                "type": "multiple-choice",
                "category": "recall",
                "question": "Complete: 'Azért tanulok, hogy sikeresen ...' (I pass)",
                "options": ["átmenjek a vizsgán", "átmegyek a vizsgán", "átmentem a vizsgán"],
                "correct": 0
            },
            {
                "id": "b1-07-consolidation-5",
                "type": "fill-in-the-blank",
                "category": "recall",
                "sentence": "A nehéz tananyagra kell [összpontosítanunk].",
                "options": ["összpontosítanunk", "jegyzetelnünk", "pihennünk"],
                "correct": 0
            },
            {
                "id": "b1-07-consolidation-6",
                "type": "multiple-choice",
                "category": "recall",
                "question": "What is the highest grade in the Hungarian school system?",
                "options": ["ötös (5)", "egyes (1)", "tízes (10)"],
                "correct": 0
            },
            {
                "id": "b1-07-consolidation-7",
                "type": "multiple-choice",
                "category": "in-context",
                "question": "A gimnázium után a diákok egyetemi képzésre ...",
                "options": ["jelentkezhetnek", "jelentkezik", "jelentkeztél"],
                "correct": 0
            },
            {
                "id": "b1-07-consolidation-8",
                "type": "fill-in-the-blank",
                "category": "in-context",
                "sentence": "A tanfolyam célja, hogy [fejlessze] a diákok szaktudását.",
                "options": ["fejlessze", "fejleszti", "fejlesztette"],
                "correct": 0
            },
            {
                "id": "b1-07-consolidation-9",
                "type": "multiple-choice",
                "category": "in-context",
                "question": "Mit jelent az 'élethosszig tartó tanulás' a felnőttek számára?",
                "options": [
                    "Folyamatos önképzést és új készségek elsajátítását.",
                    "Hogy soha nem hagyhatják el az iskolapadot.",
                    "Hogy minden évben érettségizniük kell."
                ],
                "correct": 0
            },
            {
                "id": "b1-07-consolidation-10",
                "type": "multiple-choice",
                "category": "produce",
                "question": "Translate: 'Anyone can study in state schools.'",
                "options": [
                    "Bárki tanulhat az állami iskolákban.",
                    "Mindenki tanult az iskola előtt.",
                    "Senki nem tanulhat az iskolában."
                ],
                "correct": 0
            },
            {
                "id": "b1-07-consolidation-11",
                "type": "multiple-choice",
                "category": "produce",
                "question": "Translate: 'I take notes attentively during the lecture.'",
                "options": [
                    "Figyelmesen jegyzetelek az előadás alatt.",
                    "Figyelmetlenül írok egy levelet tegnap.",
                    "Jegyzeteket veszek a boltban reggel."
                ],
                "correct": 0
            },
            {
                "id": "b1-07-consolidation-12",
                "type": "multiple-choice",
                "category": "produce",
                "question": "Translate: 'We passed both the oral and written examinations.'",
                "options": [
                    "A szóbeli és az írásbeli vizsgán is átmentünk.",
                    "A szóbeli és írásbeli vizsgát megbuktuk.",
                    "A vizsgáról szóban és írásban hallottunk."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-07-consolidation-ex.json", ex_consolidation)

    # -------------------------------------------------------------------------
    # 5. Lesson Files
    # -------------------------------------------------------------------------
    lesson_01 = {
        "id": "lesson.b1.07-01",
        "unit": 7,
        "title": "The Hungarian School System",
        "level": "B1",
        "grammar": "Potential suffix -hat/-het in institutional rules; schooling stages (általános iskola, gimnázium)",
        "goal": [
            "I can explain the main stages of the Hungarian education system.",
            "I can use the -hat/-het potential suffix to describe what students may or can do.",
            "I can use four new vocabulary items related to schools and qualifications.",
            "I can discuss admission requirements and graduation exams in natural Hungarian."
        ],
        "sections": [
            {
                "type": "goal",
                "title": "Lesson Goals",
                "items": [
                    "I can explain the main stages of the Hungarian education system.",
                    "I can use the -hat/-het potential suffix to describe what students may or can do.",
                    "I can use four new vocabulary items related to schools and qualifications.",
                    "I can discuss admission requirements and graduation exams in natural Hungarian."
                ]
            },
            {"type": "recycle", "title": "Quick Review"},
            {"type": "grammar", "ref": "grammar/b1/b1-07-01-a-gr.json"},
            {"type": "grammar", "ref": "grammar/b1/b1-07-01-b-gr.json"},
            {"type": "vocabulary", "title": "Lesson Vocabulary", "ref": "vocabulary/b1/b1-07-01-voc.json"},
            {"type": "exercise-group", "title": "Introduce", "ref": "exercises/b1/b1-07-01-ex.json", "exerciseRefs": ["b1-07-01-intro-1", "b1-07-01-intro-2"]},
            {"type": "exercise-group", "title": "Controlled", "ref": "exercises/b1/b1-07-01-ex.json", "exerciseRefs": ["b1-07-01-controlled-1", "b1-07-01-controlled-2", "b1-07-01-controlled-3", "b1-07-01-controlled-4"]},
            {"type": "exercise-group", "title": "Practice", "ref": "exercises/b1/b1-07-01-ex.json", "exerciseRefs": ["b1-07-01-practice-1", "b1-07-01-practice-2", "b1-07-01-practice-3", "b1-07-01-practice-4"]},
            {"type": "exercise-group", "title": "Dialogue", "ref": "exercises/b1/b1-07-01-ex.json", "exerciseRefs": ["b1-07-01-dialogue-1", "b1-07-01-dialogue-2"]},
            {"type": "exercise-group", "title": "Production", "ref": "exercises/b1/b1-07-01-ex.json", "exerciseRefs": ["b1-07-01-writing-1", "b1-07-01-writing-2"]},
            {"type": "srs", "title": "Add to Review"},
            {"type": "exercise-group", "title": "Check", "ref": "exercises/b1/b1-07-01-ex.json", "exerciseRefs": ["b1-07-01-check-1", "b1-07-01-check-2"]},
            {
                "type": "checklist",
                "title": "Can you do this?",
                "items": [
                    "I can explain the main stages of the Hungarian education system.",
                    "I can use the -hat/-het potential suffix to describe what students may or can do.",
                    "I can use four new vocabulary items related to schools and qualifications.",
                    "I can discuss admission requirements and graduation exams in natural Hungarian."
                ]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-07-01.json", lesson_01)

    lesson_02 = {
        "id": "lesson.b1.07-02",
        "unit": 7,
        "title": "Why I'm Learning This",
        "level": "B1",
        "grammar": "Purpose clauses: azért, hogy + subjunctive; expressing personal motivations",
        "goal": [
            "I can express purpose and goals using azért, hogy + subjunctive.",
            "I can explain why I am studying Hungarian or professional subjects.",
            "I can use four new vocabulary items related to objectives and skill development.",
            "I can discuss long-term training plans with peers."
        ],
        "sections": [
            {
                "type": "goal",
                "title": "Lesson Goals",
                "items": [
                    "I can express purpose and goals using azért, hogy + subjunctive.",
                    "I can explain why I am studying Hungarian or professional subjects.",
                    "I can use four new vocabulary items related to objectives and skill development.",
                    "I can discuss long-term training plans with peers."
                ]
            },
            {"type": "recycle", "title": "Quick Review"},
            {"type": "grammar", "ref": "grammar/b1/b1-07-02-gr.json"},
            {"type": "vocabulary", "title": "Lesson Vocabulary", "ref": "vocabulary/b1/b1-07-02-voc.json"},
            {"type": "exercise-group", "title": "Introduce", "ref": "exercises/b1/b1-07-02-ex.json", "exerciseRefs": ["b1-07-02-intro-1", "b1-07-02-intro-2"]},
            {"type": "exercise-group", "title": "Controlled", "ref": "exercises/b1/b1-07-02-ex.json", "exerciseRefs": ["b1-07-02-controlled-1", "b1-07-02-controlled-2", "b1-07-02-controlled-3", "b1-07-02-controlled-4"]},
            {"type": "exercise-group", "title": "Practice", "ref": "exercises/b1/b1-07-02-ex.json", "exerciseRefs": ["b1-07-02-practice-1", "b1-07-02-practice-2", "b1-07-02-practice-3", "b1-07-02-practice-4"]},
            {"type": "exercise-group", "title": "Dialogue", "ref": "exercises/b1/b1-07-02-ex.json", "exerciseRefs": ["b1-07-02-dialogue-1", "b1-07-02-dialogue-2"]},
            {"type": "exercise-group", "title": "Production", "ref": "exercises/b1/b1-07-02-ex.json", "exerciseRefs": ["b1-07-02-writing-1", "b1-07-02-writing-2"]},
            {"type": "srs", "title": "Add to Review"},
            {"type": "exercise-group", "title": "Check", "ref": "exercises/b1/b1-07-02-ex.json", "exerciseRefs": ["b1-07-02-check-1", "b1-07-02-check-2"]},
            {
                "type": "checklist",
                "title": "Can you do this?",
                "items": [
                    "I can express purpose and goals using azért, hogy + subjunctive.",
                    "I can explain why I am studying Hungarian or professional subjects.",
                    "I can use four new vocabulary items related to objectives and skill development.",
                    "I can discuss long-term training plans with peers."
                ]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-07-02.json", lesson_02)

    lesson_03 = {
        "id": "lesson.b1.07-03",
        "unit": 7,
        "title": "Studying Effectively",
        "level": "B1",
        "grammar": "Verbs of attention & note-taking (összpontosít vmire, jegyzetel)",
        "goal": [
            "I can discuss effective study techniques, focus, and memory.",
            "I can use verbs with their proper noun cases like összpontosít valamire.",
            "I can use four new vocabulary items related to study methods and revision.",
            "I can advise someone on how to organize their study schedule."
        ],
        "sections": [
            {
                "type": "goal",
                "title": "Lesson Goals",
                "items": [
                    "I can discuss effective study techniques, focus, and memory.",
                    "I can use verbs with their proper noun cases like összpontosít valamire.",
                    "I can use four new vocabulary items related to study methods and revision.",
                    "I can advise someone on how to organize their study schedule."
                ]
            },
            {"type": "recycle", "title": "Quick Review"},
            {"type": "grammar", "ref": "grammar/b1/b1-07-03-gr.json"},
            {"type": "vocabulary", "title": "Lesson Vocabulary", "ref": "vocabulary/b1/b1-07-03-voc.json"},
            {"type": "exercise-group", "title": "Introduce", "ref": "exercises/b1/b1-07-03-ex.json", "exerciseRefs": ["b1-07-03-intro-1", "b1-07-03-intro-2"]},
            {"type": "exercise-group", "title": "Controlled", "ref": "exercises/b1/b1-07-03-ex.json", "exerciseRefs": ["b1-07-03-controlled-1", "b1-07-03-controlled-2", "b1-07-03-controlled-3", "b1-07-03-controlled-4"]},
            {"type": "exercise-group", "title": "Practice", "ref": "exercises/b1/b1-07-03-ex.json", "exerciseRefs": ["b1-07-03-practice-1", "b1-07-03-practice-2", "b1-07-03-practice-3", "b1-07-03-practice-4"]},
            {"type": "exercise-group", "title": "Dialogue", "ref": "exercises/b1/b1-07-03-ex.json", "exerciseRefs": ["b1-07-03-dialogue-1", "b1-07-03-dialogue-2"]},
            {"type": "exercise-group", "title": "Production", "ref": "exercises/b1/b1-07-03-ex.json", "exerciseRefs": ["b1-07-03-writing-1", "b1-07-03-writing-2"]},
            {"type": "srs", "title": "Add to Review"},
            {"type": "exercise-group", "title": "Check", "ref": "exercises/b1/b1-07-03-ex.json", "exerciseRefs": ["b1-07-03-check-1", "b1-07-03-check-2"]},
            {
                "type": "checklist",
                "title": "Can you do this?",
                "items": [
                    "I can discuss effective study techniques, focus, and memory.",
                    "I can use verbs with their proper noun cases like összpontosít valamire.",
                    "I can use four new vocabulary items related to study methods and revision.",
                    "I can advise someone on how to organize their study schedule."
                ]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-07-03.json", lesson_03)

    lesson_04 = {
        "id": "lesson.b1.07-04",
        "unit": 7,
        "title": "Exams & Results",
        "level": "B1",
        "grammar": "Exam result collocations: átmegy a vizsgán, megbukik, érdemjegyet kap",
        "goal": [
            "I can describe exam preparation, taking an exam, and results.",
            "I can distinguish between oral (szóbeli) and written (írásbeli) examinations.",
            "I can use four new vocabulary items related to grades and certificates.",
            "I can talk about the Hungarian 1-to-5 grading scale comfortably."
        ],
        "sections": [
            {
                "type": "goal",
                "title": "Lesson Goals",
                "items": [
                    "I can describe exam preparation, taking an exam, and results.",
                    "I can distinguish between oral (szóbeli) and written (írásbeli) examinations.",
                    "I can use four new vocabulary items related to grades and certificates.",
                    "I can talk about the Hungarian 1-to-5 grading scale comfortably."
                ]
            },
            {"type": "recycle", "title": "Quick Review"},
            {"type": "grammar", "ref": "grammar/b1/b1-07-04-gr.json"},
            {"type": "vocabulary", "title": "Lesson Vocabulary", "ref": "vocabulary/b1/b1-07-04-voc.json"},
            {"type": "exercise-group", "title": "Introduce", "ref": "exercises/b1/b1-07-04-ex.json", "exerciseRefs": ["b1-07-04-intro-1", "b1-07-04-intro-2"]},
            {"type": "exercise-group", "title": "Controlled", "ref": "exercises/b1/b1-07-04-ex.json", "exerciseRefs": ["b1-07-04-controlled-1", "b1-07-04-controlled-2", "b1-07-04-controlled-3", "b1-07-04-controlled-4"]},
            {"type": "exercise-group", "title": "Practice", "ref": "exercises/b1/b1-07-04-ex.json", "exerciseRefs": ["b1-07-04-practice-1", "b1-07-04-practice-2", "b1-07-04-practice-3", "b1-07-04-practice-4"]},
            {"type": "exercise-group", "title": "Dialogue", "ref": "exercises/b1/b1-07-04-ex.json", "exerciseRefs": ["b1-07-04-dialogue-1", "b1-07-04-dialogue-2"]},
            {"type": "exercise-group", "title": "Production", "ref": "exercises/b1/b1-07-04-ex.json", "exerciseRefs": ["b1-07-04-writing-1", "b1-07-04-writing-2"]},
            {"type": "srs", "title": "Add to Review"},
            {"type": "exercise-group", "title": "Check", "ref": "exercises/b1/b1-07-04-ex.json", "exerciseRefs": ["b1-07-04-check-1", "b1-07-04-check-2"]},
            {
                "type": "checklist",
                "title": "Can you do this?",
                "items": [
                    "I can describe exam preparation, taking an exam, and results.",
                    "I can distinguish between oral (szóbeli) and written (írásbeli) examinations.",
                    "I can use four new vocabulary items related to grades and certificates.",
                    "I can talk about the Hungarian 1-to-5 grading scale comfortably."
                ]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-07-04.json", lesson_04)

    lesson_05 = {
        "id": "lesson.b1.07-05",
        "unit": 7,
        "title": "Lifelong Learning",
        "level": "B1",
        "grammar": "Synthesis: adult education, retraining, and lifelong curiosity",
        "goal": [
            "I can discuss lifelong learning, retraining, and personal development.",
            "I can use four new vocabulary items related to adult education.",
            "I can express complex aspirations and educational opportunities.",
            "I can read and understand an adapted excerpt from Karinthy's Tanár úr kérem."
        ],
        "sections": [
            {
                "type": "goal",
                "title": "Lesson Goals",
                "items": [
                    "I can discuss lifelong learning, retraining, and personal development.",
                    "I can use four new vocabulary items related to adult education.",
                    "I can express complex aspirations and educational opportunities.",
                    "I can read and understand an adapted excerpt from Karinthy's Tanár úr kérem."
                ]
            },
            {"type": "recycle", "title": "Quick Review"},
            {"type": "grammar", "ref": "grammar/b1/b1-07-05-gr.json"},
            {"type": "vocabulary", "title": "Lesson Vocabulary", "ref": "vocabulary/b1/b1-07-05-voc.json"},
            {"type": "exercise-group", "title": "Introduce", "ref": "exercises/b1/b1-07-05-ex.json", "exerciseRefs": ["b1-07-05-intro-1", "b1-07-05-intro-2"]},
            {"type": "exercise-group", "title": "Controlled", "ref": "exercises/b1/b1-07-05-ex.json", "exerciseRefs": ["b1-07-05-controlled-1", "b1-07-05-controlled-2", "b1-07-05-controlled-3", "b1-07-05-controlled-4"]},
            {"type": "exercise-group", "title": "Practice", "ref": "exercises/b1/b1-07-05-ex.json", "exerciseRefs": ["b1-07-05-practice-1", "b1-07-05-practice-2", "b1-07-05-practice-3", "b1-07-05-practice-4"]},
            {"type": "exercise-group", "title": "Dialogue", "ref": "exercises/b1/b1-07-05-ex.json", "exerciseRefs": ["b1-07-05-dialogue-1", "b1-07-05-dialogue-2"]},
            {"type": "exercise-group", "title": "Production", "ref": "exercises/b1/b1-07-05-ex.json", "exerciseRefs": ["b1-07-05-writing-1", "b1-07-05-writing-2"]},
            {"type": "srs", "title": "Add to Review"},
            {
                "type": "story",
                "title": "Reading: A rossz tanuló felel",
                "ref": "stories/classics/b1/b1-07-tanarurkerem.json"
            },
            {"type": "exercise-group", "title": "Reading", "ref": "exercises/b1/b1-07-05-ex.json", "exerciseRefs": ["b1-07-05-reading-1", "b1-07-05-reading-2", "b1-07-05-reading-3"]},
            {
                "type": "checklist",
                "title": "Can you do this?",
                "items": [
                    "I can discuss lifelong learning, retraining, and personal development.",
                    "I can use four new vocabulary items related to adult education.",
                    "I can express complex aspirations and educational opportunities.",
                    "I can read and understand an adapted excerpt from Karinthy's Tanár úr kérem."
                ]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-07-05.json", lesson_05)

    lesson_consolidation = {
        "id": "lesson.b1.07-consolidation",
        "unit": 7,
        "title": "Unit 7 Consolidation",
        "level": "B1",
        "sections": [
            {
                "type": "goal",
                "title": "Consolidation Goals",
                "items": [
                    "I can describe the Hungarian education system and school stages accurately.",
                    "I can use the -hat/-het potential suffix and azért, hogy purpose clauses.",
                    "I can discuss exams, grading, and study techniques.",
                    "I can discuss lifelong learning, retraining, and personal growth."
                ]
            },
            {"type": "recycle", "title": "Quick Review"},
            {"type": "exercise-group", "title": "Recognize", "ref": "exercises/b1/b1-07-consolidation-ex.json", "exerciseRefs": ["b1-07-consolidation-1", "b1-07-consolidation-2", "b1-07-consolidation-3"]},
            {"type": "exercise-group", "title": "Recall", "ref": "exercises/b1/b1-07-consolidation-ex.json", "exerciseRefs": ["b1-07-consolidation-4", "b1-07-consolidation-5", "b1-07-consolidation-6"]},
            {"type": "exercise-group", "title": "In Context", "ref": "exercises/b1/b1-07-consolidation-ex.json", "exerciseRefs": ["b1-07-consolidation-7", "b1-07-consolidation-8", "b1-07-consolidation-9"]},
            {"type": "exercise-group", "title": "Produce", "ref": "exercises/b1/b1-07-consolidation-ex.json", "exerciseRefs": ["b1-07-consolidation-10", "b1-07-consolidation-11", "b1-07-consolidation-12"]},
            {
                "type": "checklist",
                "title": "Can you do this?",
                "items": [
                    "I can describe the Hungarian education system and school stages accurately.",
                    "I can use the -hat/-het potential suffix and azért, hogy purpose clauses.",
                    "I can discuss exams, grading, and study techniques.",
                    "I can discuss lifelong learning, retraining, and personal growth."
                ]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-07-consolidation.json", lesson_consolidation)

if __name__ == "__main__":
    build_unit_7_core()
    print("Successfully built Hungarian B1 Core Unit 7!")
