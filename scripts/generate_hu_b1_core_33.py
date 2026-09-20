#!/usr/bin/env python3
"""Generate Hungarian B1 Core Unit 33: Reported Speech (b1-33)."""

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

def build_unit_33_core():
    # -------------------------------------------------------------------------
    # 1. Vocabulary Files (4 words each = 20 words total)
    # -------------------------------------------------------------------------
    voc_01 = {
        "id": "vocab.b1.33.01",
        "lesson": "b1-33-01",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "függő beszéd", "translation": "reported speech, indirect speech", "pos": "noun"},
            {"lemma": "idézés", "translation": "quoting, quotation, citation", "pos": "noun"},
            {"lemma": "kijelentés", "translation": "statement, declaration, assertion", "pos": "noun"},
            {"lemma": "közlés", "translation": "communication, announcement, message", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-33-01-voc.json", voc_01)

    voc_02 = {
        "id": "vocab.b1.33.02",
        "lesson": "b1-33-02",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "hírforrás", "translation": "news source, source of information", "pos": "noun"},
            {"lemma": "szóvivő", "translation": "spokesperson, press secretary", "pos": "noun"},
            {"lemma": "nyilatkozat", "translation": "official statement, declaration, press release", "pos": "noun"},
            {"lemma": "állásfoglalás", "translation": "taking a stand, statement of position", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-33-02-voc.json", voc_02)

    voc_03 = {
        "id": "vocab.b1.33.03",
        "lesson": "b1-33-03",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "kérdezősködés", "translation": "inquiry, asking around, inquisitive probing", "pos": "noun"},
            {"lemma": "érdeklődés", "translation": "interest, inquiry, paying attention", "pos": "noun"},
            {"lemma": "felvilágosítás", "translation": "clarification, enlightenment, information provided", "pos": "noun"},
            {"lemma": "tájékozódás", "translation": "orientation, finding out, getting briefed", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-33-03-voc.json", voc_03)

    voc_04 = {
        "id": "vocab.b1.33.04",
        "lesson": "b1-33-04",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "utasítás", "translation": "instruction, directive, order", "pos": "noun"},
            {"lemma": "felszólítás", "translation": "summons, formal appeal, official notice", "pos": "noun"},
            {"lemma": "kérelem", "translation": "petition, formal request, application", "pos": "noun"},
            {"lemma": "követelés", "translation": "demand, claim, requirement", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-33-04-voc.json", voc_04)

    voc_05 = {
        "id": "vocab.b1.33.05",
        "lesson": "b1-33-05",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "híresztelés", "translation": "rumor, hearsay, unverified report", "pos": "noun"},
            {"lemma": "pletyka", "translation": "gossip, idle chatter, grape-vine talk", "pos": "noun"},
            {"lemma": "cáfolat", "translation": "refutation, formal denial, rebutting statement", "pos": "noun"},
            {"lemma": "sajtóértesülés", "translation": "press report, media information", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-33-05-voc.json", voc_05)

    # -------------------------------------------------------------------------
    # 2. Grammar Files (2 per lesson = 10 files)
    # -------------------------------------------------------------------------
    gr_01_a = {
        "id": "grammar.b1.33.01.direct-to-indirect",
        "title": "Reporting Statements: No Tense Backshifting in Hungarian",
        "sections": [
            {
                "type": "text",
                "title": "Preserving Utterance Tense",
                "content": "Unlike English or Spanish, Hungarian reported speech does not shift tenses backwards into the past. The subordinate clause introduced by *azt mondta, hogy...* retains the exact grammatical tense of the original utterance relative to that moment."
            },
            {
                "type": "examples",
                "title": "Tense retention examples",
                "items": [
                    {"spanish": "Péter: „Beteg vagyok.” -> Péter azt mondta, hogy beteg.", "english": "Peter: 'I am sick.' -> Peter said that he was sick (lit. is sick)."},
                    {"spanish": "Anna: „Holnap elutazom.” -> Anna azt mondta, hogy másnap elutazik.", "english": "Anna: 'I will travel tomorrow.' -> Anna said that she would travel the next day."},
                    {"spanish": "Gábor: „Megírtam a cikket.” -> Gábor azt mondta, hogy megírta a cikket.", "english": "Gabor: 'I wrote the article.' -> Gabor said that he had written the article."}
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-33-01-a-gr.json", gr_01_a)

    gr_01_b = {
        "id": "grammar.b1.33.01.pronoun-person-shifts",
        "title": "Deictic Shifts: Pronouns, Persons & Temporal Adverbs",
        "sections": [
            {
                "type": "text",
                "title": "Shifting Point of View",
                "content": "While tense remains unchanged in Hungarian indirect speech, personal pronouns, verb inflection persons, and spatial-temporal deictic adverbs shift to reflect the reporter's perspective (*én -> ő*, *itt -> ott*, *ma -> aznap*, *holnap -> másnap*)."
            },
            {
                "type": "examples",
                "title": "Deictic shift examples",
                "items": [
                    {"spanish": "„Itt várok rád” -> Azt mondta, hogy ott vár rám.", "english": "'I wait for you here' -> He said that he was waiting for me there."},
                    {"spanish": "„Ma nem érek rá” -> Azt mondta, hogy aznap nem ér rá.", "english": "'I don't have time today' -> He said that he didn't have time that day."},
                    {"spanish": "„Segítünk nektek” -> Azt mondták, hogy segítenek nekünk.", "english": "'We help you' -> They said that they would help us."}
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-33-01-b-gr.json", gr_01_b)

    gr_02_a = {
        "id": "grammar.b1.33.02.reporting-verbs",
        "title": "Formal Reporting Verbs: Állít, Megjegyez & Hangsúlyoz",
        "sections": [
            {
                "type": "text",
                "title": "Precision in Reporting",
                "content": "In news discourse and formal writing, *mondja* is replaced by nuanced verbs: *állítja* (claims), *megjegyzi* (remarks), *bejelenti* (announces), and *hangsúlyozza* (emphasizes). These verbs anchor the subordinate clause with the demonstrative *azt* or *arról*."
            },
            {
                "type": "examples",
                "title": "Reporting verb examples",
                "items": [
                    {"spanish": "A szóvivő hangsúlyozta, hogy a tárgyalások sikeresek voltak.", "english": "The spokesperson emphasized that the negotiations were successful."},
                    {"spanish": "A miniszter bejelentette, hogy új program indul a fiataloknak.", "english": "The minister announced that a new program was launching for youth."},
                    {"spanish": "A szakértő megjegyezte, hogy a gazdasági növekedés stabil.", "english": "The expert remarked that economic growth was stable."}
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-33-02-a-gr.json", gr_02_a)

    gr_02_b = {
        "id": "grammar.b1.33.02.negative-reporting",
        "title": "Denials and Refutations: Tagadja, hogy... & Cáfolja, hogy...",
        "sections": [
            {
                "type": "text",
                "title": "Reporting Negative Claims",
                "content": "To report denials or rejections, Hungarian uses *tagadja, hogy...* (denies that...) and *cáfolja, hogy...* (refutes that...). Notice that unlike colloquial English, Hungarian keeps the subordinate clause affirmative or matches the factual intent."
            },
            {
                "type": "examples",
                "title": "Denial examples",
                "items": [
                    {"spanish": "A vállalat képviselője határozottan tagadta, hogy hibát követtek volna el.", "english": "The company representative strictly denied that they had made a mistake."},
                    {"spanish": "A politikus cáfolta azokat a sajtóértesüléseket, amelyek a lemondásáról szóltak.", "english": "The politician refuted those press reports that spoke of his resignation."},
                    {"spanish": "Nem állította azt, hogy a feladat egyszerű lenne.", "english": "He did not claim that the task would be simple."}
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-33-02-b-gr.json", gr_02_b)

    gr_03_a = {
        "id": "grammar.b1.33.03.embedded-polar-questions",
        "title": "Indirect Yes-No Questions: The Embedded -e Enclitic",
        "sections": [
            {
                "type": "text",
                "title": "Attaching the Question Particle",
                "content": "When converting a direct polar (yes/no) question into indirect speech, Hungarian introduces the clause with *hogy* and attaches the interrogative enclitic *-e* to the finite verb or to the focused constituent: *Azt kérdezte, hogy eljössz-e.*"
            },
            {
                "type": "examples",
                "title": "Embedded polar question examples",
                "items": [
                    {"spanish": "„Ismered a várost?” -> Azt kérdezte, hogy ismerem-e a várost.", "english": "'Do you know the town?' -> He asked whether I knew the town."},
                    {"spanish": "„Sikerült a vizsga?” -> Megkérdezte tőlem, hogy sikerült-e a vizsgám.", "english": "'Did the exam succeed?' -> She asked me if my exam had succeeded."},
                    {"spanish": "Érdeklődött, hogy nyitva van-e még az iroda.", "english": "He inquired whether the office was still open."}
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-33-03-a-gr.json", gr_03_a)

    gr_03_b = {
        "id": "grammar.b1.33.03.embedded-wh-questions",
        "title": "Indirect Information Questions: Azt kérdezte, hogy mikor/hol...",
        "sections": [
            {
                "type": "text",
                "title": "Reporting Wh-Questions",
                "content": "When reporting questions that begin with an interrogative pronoun or adverb (*ki, mi, hol, mikor, hogyan, miért*), Hungarian puts *hogy* immediately before the question word. The question particle *-e* is NOT used in these open questions."
            },
            {
                "type": "examples",
                "title": "Embedded wh-question examples",
                "items": [
                    {"spanish": "„Mikor kezdődik az előadás?” -> Azt kérdezte, hogy mikor kezdődik az előadás.", "english": "'When does the lecture start?' -> He asked when the lecture started."},
                    {"spanish": "„Hol találkozunk?” -> Kíváncsi volt arra, hogy hol találkozunk.", "english": "'Where do we meet?' -> She was curious about where we would meet."},
                    {"spanish": "Érdeklődtek, hogy ki vezeti a projektet.", "english": "They inquired who was leading the project."}
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-33-03-b-gr.json", gr_03_b)

    gr_04_a = {
        "id": "grammar.b1.33.04.reported-commands",
        "title": "Reporting Commands & Orders: Subjunctive-Imperative in -jon/-jen",
        "sections": [
            {
                "type": "text",
                "title": "Mandating Action",
                "content": "Direct commands (*„Gyere ide!”*, *„Írjátok meg!”*) convert into indirect speech using verbs of ordering (*utasít, parancsol, meghagyja*) followed by *hogy* and a subordinate verb in the subjunctive-imperative (*felszólító mód*: *-jon, -jen, -jön*)."
            },
            {
                "type": "examples",
                "title": "Reported command examples",
                "items": [
                    {"spanish": "„Azonnal fejezd be a munkát!” -> Azt parancsolta, hogy azonnal fejezzem be a munkát.", "english": "'Finish the work immediately!' -> He ordered me to finish the work immediately."},
                    {"spanish": "Az orvos arra utasította a beteget, hogy pihenjen sokat.", "english": "The doctor instructed the patient to rest a lot."},
                    {"spanish": "A rendőr felszólította a sofőrt, hogy állítsa le a motort.", "english": "The police officer ordered the driver to stop the engine."}
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-33-04-a-gr.json", gr_04_a)

    gr_04_b = {
        "id": "grammar.b1.33.04.reported-requests",
        "title": "Reporting Polite Requests & Invitations: Kéri, hogy...",
        "sections": [
            {
                "type": "text",
                "title": "Polite Indirect Requests",
                "content": "Polite requests and appeals are reported using *kér valakit arra, hogy...* or *megkér valakit, hogy...* governing a subjunctive clause. The ablative case (*-tól/-től*) or accusative (*-t*) marks the person being asked (*megkérte Pétert, hogy segítsen*)."
            },
            {
                "type": "examples",
                "title": "Reported request examples",
                "items": [
                    {"spanish": "„Kérlek, csukd be az ablakot!” -> Megkérte, hogy csukja be az ablakot.", "english": "'Please close the window!' -> She asked him to close the window."},
                    {"spanish": "Arra kérték a vendégeket, hogy foglaljanak helyet.", "english": "They requested the guests to take their seats."},
                    {"spanish": "A polgármester felkérte a közösséget, hogy vegyen részt az önkéntes napon.", "english": "The mayor invited the community to take part in the volunteer day."}
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-33-04-b-gr.json", gr_04_b)

    gr_05_a = {
        "id": "grammar.b1.33.05.hearsay-evidentiality",
        "title": "Hearsay and Evidentiality: Állítólag, Úgy hírlik & A hírek szerint",
        "sections": [
            {
                "type": "text",
                "title": "Expressing Unverified Rumor",
                "content": "Hungarian uses evidential adverbs and impersonal expressions to frame unverified hearsay: *állítólag* (allegedly, reportedly), *úgy hírlik, hogy...* (rumor has it that...), and *a hírek szerint* (according to the news)."
            },
            {
                "type": "examples",
                "title": "Hearsay examples",
                "items": [
                    {"spanish": "Állítólag csoda történt a faluban egy rejtélyes piros esernyővel.", "english": "Allegedly a miracle occurred in the village with a mysterious red umbrella."},
                    {"spanish": "Úgy hírlik, hogy nagy vagyon rejtőzik a régi kastélyban.", "english": "Rumor has it that great wealth is hidden in the old manor."},
                    {"spanish": "A sajtóértesülések szerint a tárgyalások hamarosan lezárulnak.", "english": "According to press reports, talks will conclude shortly."}
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-33-05-a-gr.json", gr_05_a)

    gr_05_b = {
        "id": "grammar.b1.33.05.indirect-reference",
        "title": "Attributing Sources: Arra hivatkozik & Szavai szerint",
        "sections": [
            {
                "type": "text",
                "title": "Citing and Attributing Sources",
                "content": "When referencing external accounts, journalistic Hungarian employs *hivatkozik vmire/vkire* (cites / alludes to sth/someone), *vkinek a szavai szerint* (in someone's words / according to someone), and *idézve a jelentést* (quoting the report)."
            },
            {
                "type": "examples",
                "title": "Attribution examples",
                "items": [
                    {"spanish": "A nyomozó a szemtanúk vallomására hivatkozva rekonstruálta az eseményt.", "english": "The investigator reconstructed the event citing the testimonies of eyewitnesses."},
                    {"spanish": "A falu lakói szerint Szent Péter maga hozta az esernyőt a kislánynak.", "english": "According to the villagers, Saint Peter himself brought the umbrella to the little girl."},
                    {"spanish": "A hivatalos közlemény szavai szerint a rend helyreállt.", "english": "In the words of the official statement, order has been restored."}
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-33-05-b-gr.json", gr_05_b)

    # -------------------------------------------------------------------------
    # 3. Classic Story (Lesson 05)
    # -------------------------------------------------------------------------
    story_33 = {
        "id": "story.b1.33.classic",
        "title": "Szent Péter esernyője",
        "level": "B1",
        "order": 33,
        "type": "classics",
        "estimatedMinutes": 8,
        "summary": "An adaptation of Mikszáth Kálmán's humorous and touching classic 'Szent Péter esernyője' (Saint Peter's Umbrella, 1895). In the impoverished mountain village of Glogova, a young priest finds an abandoned baby girl—his orphaned sister Veronka. During a sudden storm, a miraculous worn red umbrella is placed over her basket, giving rise to local legends that Saint Peter himself brought it. As Glogova prospers and Veronka grows up, young lawyer Gyuri Wibra discovers his late eccentric father hid a lost fortune inside the umbrella's handle. Traveling to find it, Gyuri falls in love with Veronka and realizes genuine love far surpasses all worldly riches.",
        "characters": [
            "Bélyi János, a glogovai fiatal, jámbor katolikus pap",
            "Veronka, a pap húga, akit a csodás esernyő védett meg",
            "Wibra Gyuri, tehetséges fiatal ügyvéd Besztercebányáról",
            "Gregorics Pál, Gyuri különc, gazdag édesapja",
            "Adameczné és a glogovai hívek, akik Szent Péter csodájában hisznek"
        ],
        "location": "Glogova, Besztercebánya és a felvidéki hegyek",
        "author": "Mikszáth Kálmán",
        "work": "Szent Péter esernyője (1895)",
        "paragraphs": [
            {
                "type": "narration",
                "text": "Glogova elszegényedett kis hegyi falu volt a Felvidéken, ahová a fiatal és jámbor pap, Bélyi János érkezett szolgálni. Amikor megérkezett a parókiára, nem talált ott semmit: a kamra üres volt, a hívek pedig szegények. Ráadásul hamarosan egy kosárban egy kétéves kislányt hoztak hozzá, a húgát, Veronkát, mert az édesanyjuk váratlanul elhunyt."
            },
            {
                "type": "dialogue",
                "speaker": "Bélyi János",
                "text": "Uram, hogyan nevelem fel ezt a gyermeket ebben a nyomorúságban? De bízom a te végtelen kegyelmedben."
            },
            {
                "type": "narration",
                "text": "Egy nyári délutánon a pap a templomban imádkozott, miközben Veronka a szabad ég alatt aludt az udvaron lévő kosárban. Hirtelen sötét fellegek gyülekeztek, és hatalmas zápor tört ki. János atya kétségbeesetten rohant ki a ház udvarára, ám amikor a kosárhoz ért, elámult: a gyermek fölé egy hatalmas, kopott piros esernyő volt kifeszítve, és Veronka békésen mosolygott a száraz ruhácskájában."
            },
            {
                "type": "narration",
                "text": "A faluban azonnal szárnyra kelt a híresztelés. Egy öregasszony eskü alatt állította, hogy látta az udvaron Szent Pétert, amint a piros ernyőt a gyermek fölé borította. A hír futótűzként terjedt: betegek zarándokoltak Glogovára, a pap pedig esküvőkre vitte magával a szerencsét hozó szent ernyőt. A falu hamarosan felvirágzott, Veronka pedig csodaszép leánnyá cseperedett."
            },
            {
                "type": "narration",
                "text": "Eközben Besztercebányán egy fiatal ügyvéd, Wibra Gyuri kutatni kezdett különc apja, néhai Gregorics Pál öröksége után. Gyuri rájött, hogy apja a titkos vagyonát az esernyő üreges fanyelébe rejtette, amelyet Gregorics halála után egy glogovai vándornak adtak el."
            },
            {
                "type": "dialogue",
                "speaker": "Wibra Gyuri",
                "text": "Meg kell találnom azt a piros esernyőt! Abban van az egész jövőm és a törvényes örökségem."
            },
            {
                "type": "narration",
                "text": "Gyuri Glogovára utazott, hogy megszerezze a híres kincset rejtő ernyőt. Amikor azonban találkozott Veronkával, a pap húgával, a szíve mélyen megrendült. Megértette, hogy a leány tiszta lelke és szeretete felülmúl minden vagyont: a valódi csoda a szeretetben és a jóságban lakozik."
            }
        ]
    }
    write_json("content/hu/stories/classics/b1/b1-33-mikszath.json", story_33)

    # -------------------------------------------------------------------------
    # 4. Exercise Files (6 files, 8 exercises each)
    # -------------------------------------------------------------------------
    # Lesson 01 Exercises
    ex_01 = {
        "lesson": "b1-33-01",
        "exercises": [
            {
                "id": "b1-33-01.ex01",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Mit jelent az, hogy a magyar függő beszédben nincs igeidő-visszaléptetés?",
                "options": [
                    "A mellékmondat megtartja az eredeti elhangzás igeidejét.",
                    "Minden mondatot automatikusan múlt időbe kell tenni.",
                    "A függő beszédben csak jövő idejű igéket szabad használni."
                ],
                "correct": 0
            },
            {
                "id": "b1-33-01.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Péter: „Beteg vagyok.” -> Péter azt mondta, hogy beteg_____. (is / was - no suffix needed, present tense copula omitted)",
                "answer": "volt"
            },
            {
                "id": "b1-33-01.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Azt", "mondta,", "hogy", "másnap", "korán", "érkezik."],
                "solution": ["Azt", "mondta,", "hogy", "másnap", "korán", "érkezik."]
            },
            {
                "id": "b1-33-01.ex04",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Hogyan alakul át a közvetlen beszéd 'itt' szava a függő beszédben?",
                "options": [
                    "ott",
                    "ide",
                    "onnét"
                ],
                "correct": 0
            },
            {
                "id": "b1-33-01.ex05",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Anna azt mondta, hogy holnap elutaz_____. (she travels / will travel - ik)",
                "answer": "ik"
            },
            {
                "id": "b1-33-01.ex06",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Melyik szó jelenti valakinek a pontos szavainak bemutatását?",
                "options": [
                    "Idézés",
                    "Cáfolat",
                    "Kérdezősködés"
                ],
                "correct": 0
            },
            {
                "id": "b1-33-01.ex07",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A hivatalos közlemény fontos kijelentés_____ tartalmazott. (statements - eket)",
                "answer": "eket"
            },
            {
                "id": "b1-33-01.ex08",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Közölték", "velünk,", "hogy", "a", "vonat", "késni", "fog."],
                "solution": ["Közölték", "velünk,", "hogy", "a", "vonat", "késni", "fog."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-33-01-ex.json", ex_01)

    # Lesson 02 Exercises
    ex_02 = {
        "lesson": "b1-33-02",
        "exercises": [
            {
                "id": "b1-33-02.ex01",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Melyik igét használjuk hivatalos sajtótájékoztatón döntések bejelentésére?",
                "options": [
                    "Bejelenti",
                    "Suttogja",
                    "Pletykálja"
                ],
                "correct": 0
            },
            {
                "id": "b1-33-02.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A szóvivő határozottan tagad_____ a valótlan híreket. (denied - ta)",
                "answer": "ta"
            },
            {
                "id": "b1-33-02.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "szakértő", "hangsúlyozta,", "hogy", "a", "helyzet", "stabil."],
                "solution": ["A", "szakértő", "hangsúlyozta,", "hogy", "a", "helyzet", "stabil."]
            },
            {
                "id": "b1-33-02.ex04",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent az, hogy valaki 'cáfolja a sajtóértesülést'?",
                "options": [
                    "Hivatalosan kijelenti, hogy a hír nem felel meg a valóságnak.",
                    "Megerősíti a sajtóban megjelent információt.",
                    "Kérdést tesz fel az újságírónak."
                ],
                "correct": 0
            },
            {
                "id": "b1-33-02.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A minisztérium hivatalos állásfoglalás_____ adott ki a helyzetről. (position - t)",
                "answer": "t"
            },
            {
                "id": "b1-33-02.ex06",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Hogyan mondjuk: 'A kutató megjegyezte, hogy...'?",
                "options": [
                    "A kutató megjegyezte, hogy van még megoldandó feladat.",
                    "A kutató megjegyzett, hogy feladatok voltak volna.",
                    "A kutató megjegyzés tette arról."
                ],
                "correct": 0
            },
            {
                "id": "b1-33-02.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A képviselő cáfolta a lemondásáról szóló sajtóértesülés_____ . (reports - eket)",
                "answer": "eket"
            },
            {
                "id": "b1-33-02.ex08",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "hivatalos", "szóvivő", "nyilatkozatot", "tett", "az", "eseményről."],
                "solution": ["A", "hivatalos", "szóvivő", "nyilatkozatot", "tett", "az", "eseményről."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-33-02-ex.json", ex_02)

    # Lesson 03 Exercises
    ex_03 = {
        "lesson": "b1-33-03",
        "exercises": [
            {
                "id": "b1-33-03.ex01",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Mikor kapcsolódik a közvetett kérdéshez az '-e' kérdőpartikula?",
                "options": [
                    "Közvetett eldöntendő (igen-nem) kérdésekben a finite igéhez vagy a fókuszhoz.",
                    "Minden kérdőszós (hol, mikor) kérdés végén kötelezően.",
                    "Csak múlt idejű kijelentő mondatokban."
                ],
                "correct": 0
            },
            {
                "id": "b1-33-03.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Azt kérdezte tőlem, hogy ismerem-_____ a várost. (question particle - e)",
                "answer": "e"
            },
            {
                "id": "b1-33-03.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Érdeklődött,", "hogy", "mikor", "érkezik", "meg", "a", "vonat."],
                "solution": ["Érdeklődött,", "hogy", "mikor", "érkezik", "meg", "a", "vonat."]
            },
            {
                "id": "b1-33-03.ex04",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Helyes-e kitenni az '-e' partikulát ebben: 'Azt kérdezte, hogy hol van a könyvtár'?",
                "options": [
                    "Nem, mert nyitott kérdőszós (hol) mondatban nem használunk '-e' partikulát.",
                    "Igen, kötelező: 'hol-e van'.",
                    "Csak tagadásban használható."
                ],
                "correct": 0
            },
            {
                "id": "b1-33-03.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A recepción részletes felvilágosítás_____ kaptunk a programokról. (clarification - t)",
                "answer": "t"
            },
            {
                "id": "b1-33-03.ex06",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit fejez ki a 'kérdezősködés' szó?",
                "options": [
                    "Több kérdés feltételét, alapos körbekérdezést.",
                    "Hivatalos parancs kiadását.",
                    "A válaszadás megtagadását."
                ],
                "correct": 0
            },
            {
                "id": "b1-33-03.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Megkérdezte, hogy szabad-_____ itt leülni. (question particle - e)",
                "answer": "e"
            },
            {
                "id": "b1-33-03.ex08",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["Alapos", "tájékozódás", "után", "hoztuk", "meg", "a", "döntést."],
                "solution": ["Alapos", "tájékozódás", "után", "hoztuk", "meg", "a", "döntést."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-33-03-ex.json", ex_03)

    # Lesson 04 Exercises
    ex_04 = {
        "lesson": "b1-33-04",
        "exercises": [
            {
                "id": "b1-33-04.ex01",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Milyen igemódot használ a magyar a parancsok és kérések függő beszédbe alakításakor?",
                "options": [
                    "Felszólító módot (-jon/-jen/-jön) a hogy kötőszó után.",
                    "Csak feltételes módot.",
                    "Kizárólag főnévi igenevet."
                ],
                "correct": 0
            },
            {
                "id": "b1-33-04.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Megkért engem, hogy segítse_____ neki. (that I help - k)",
                "answer": "k"
            },
            {
                "id": "b1-33-04.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "tanár", "felszólította", "a", "diákokat,", "hogy", "figyeljenek."],
                "solution": ["A", "tanár", "felszólította", "a", "diákokat,", "hogy", "figyeljenek."]
            },
            {
                "id": "b1-33-04.ex04",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent az 'utasítás' szó?",
                "options": [
                    "Pontos feladat vagy teendő elrendelését.",
                    "Bizonytalan véleményt egy könyvről.",
                    "Egy kérdés megválaszolását."
                ],
                "correct": 0
            },
            {
                "id": "b1-33-04.ex05",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Az orvos arra utasította a beteget, hogy pihen_____ sokat. (rest - jen)",
                "answer": "jen"
            },
            {
                "id": "b1-33-04.ex06",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Melyik szó jelent udvarias vagy hivatalos felterjesztett kérést?",
                "options": [
                    "Kérelem",
                    "Pletyka",
                    "Utasítás"
                ],
                "correct": 0
            },
            {
                "id": "b1-33-04.ex07",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A rendőrség felszólítás_____ küldött a szabálysértőnek. (notice - t)",
                "answer": "t"
            },
            {
                "id": "b1-33-04.ex08",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Arra", "kértem", "őt,", "hogy", "várjon", "meg", "engem."],
                "solution": ["Arra", "kértem", "őt,", "hogy", "várjon", "meg", "engem."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-33-04-ex.json", ex_04)

    # Lesson 05 Exercises
    ex_05 = {
        "lesson": "b1-33-05",
        "exercises": [
            {
                "id": "b1-33-05.ex01",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Miért tartották csodatevőnek a piros esernyőt Mikszáth regényében?",
                "options": [
                    "Mert a híresztelés szerint maga Szent Péter tette a kis Veronka kosara fölé a viharban.",
                    "Mert színaranyból készült a fogantyúja.",
                    "Mert repülni tudott a felvidéki falvak felett."
                ],
                "correct": 0
            },
            {
                "id": "b1-33-05.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "_____ csoda történt a glogovai faluban az esernyővel. (Allegedly - Állítólag)",
                "answer": "Állítólag"
            },
            {
                "id": "b1-33-05.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Úgy", "hírlik,", "hogy", "nagy", "vagyon", "rejtőzik", "az", "esernyőben."],
                "solution": ["Úgy", "hírlik,", "hogy", "nagy", "vagyon", "rejtőzik", "az", "esernyőben."]
            },
            {
                "id": "b1-33-05.ex04",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Mit rejtett valójában az öreg Gregorics Pál az esernyő fanyelébe?",
                "options": [
                    "A titkos bankutalványokat és az örökséget.",
                    "A falu régi térképét.",
                    "Egy szent imakönyvet."
                ],
                "correct": 0
            },
            {
                "id": "b1-33-05.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A faluban gyorsan szárnyra kelt a híresztelés_____ . (rumor - e)",
                "answer": "e"
            },
            {
                "id": "b1-33-05.ex06",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Mire jött rá Wibra Gyuri, amikor beleszeretett Veronkába?",
                "options": [
                    "Hogy a leány tisztasága és szeretete értékesebb minden földi kincsnél.",
                    "Hogy az esernyő már rég tönkrement.",
                    "Hogy a rokonok elvitték az összes pénzt."
                ],
                "correct": 0
            },
            {
                "id": "b1-33-05.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A tanúk vallomására hivatkoz_____ rekonstruálták az eseményt. (referring / citing - va)",
                "answer": "va"
            },
            {
                "id": "b1-33-05.ex08",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "hírek", "szerint", "a", "tárgyalások", "hamarosan", "befejeződnek."],
                "solution": ["A", "hírek", "szerint", "a", "tárgyalások", "hamarosan", "befejeződnek."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-33-05-ex.json", ex_05)

    # Consolidation Exercises
    ex_con = {
        "lesson": "b1-33-consolidation",
        "exercises": [
            {
                "id": "b1-33-consolidation.ex01",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Hogyan alakul át függő beszédben: „Holnap felhívlak titeket”?",
                "options": [
                    "Azt mondta, hogy másnap felhív minket.",
                    "Azt mondta, hogy ma felhívna titeket.",
                    "Azt mondta, hogy tegnap felhívott."
                ],
                "correct": 0
            },
            {
                "id": "b1-33-consolidation.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Az orvos arra intette a beteget, hogy pihen_____ eleget. (rest - jen)",
                "answer": "jen"
            },
            {
                "id": "b1-33-consolidation.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Azt", "kérdezte,", "hogy", "megérkezett-e", "már", "a", "küldemény."],
                "solution": ["Azt", "kérdezte,", "hogy", "megérkezett-e", "már", "a", "küldemény."]
            },
            {
                "id": "b1-33-consolidation.ex04",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent a szóvivő által kiadott 'cáfolat'?",
                "options": [
                    "Annak hivatalos bejelentését, hogy a terjedő információ nem igaz.",
                    "Egy új törvény elfogadását.",
                    "Egy interjú felvételének megszakítását."
                ],
                "correct": 0
            },
            {
                "id": "b1-33-consolidation.ex05",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A polgármester arra kérte a lakosságot, hogy vegyen részt a fórum_____ . (in the forum - on)",
                "answer": "on"
            },
            {
                "id": "b1-33-consolidation.ex06",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Mikszáth regényében mi védte meg a kis Veronkát a zivatarban?",
                "options": [
                    "Egy kopott, hatalmas piros esernyő.",
                    "Egy vastag kabát a sekrestyéből.",
                    "Egy fából ácsolt kis házikó."
                ],
                "correct": 0
            },
            {
                "id": "b1-33-consolidation.ex07",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A szemtanúk vallomása alátámasztotta a korábbi sajtóértesülés_____ . (reports - eket)",
                "answer": "eket"
            },
            {
                "id": "b1-33-consolidation.ex08",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "hivatalos", "szóvivő", "hangsúlyozta,", "hogy", "a", "hír", "valótlan."],
                "solution": ["A", "hivatalos", "szóvivő", "hangsúlyozta,", "hogy", "a", "hír", "valótlan."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-33-consolidation-ex.json", ex_con)

    # -------------------------------------------------------------------------
    # 5. Lesson Files (6 files)
    # -------------------------------------------------------------------------
    lesson_01 = {
        "id": "lesson.b1.33-01",
        "unit": 33,
        "title": "Mit mondott? Függő beszéd és nézőpontváltás (What Did They Say? Reported Speech)",
        "level": "B1",
        "grammar": "Direct & Indirect Speech, Tense Retention and Deictic Shifts in Hungarian",
        "sections": [
            {
                "type": "goal",
                "title": "Lesson Goals",
                "items": [
                    "I can report direct statements in Hungarian without tense backshifting.",
                    "I can shift personal pronouns, persons, and temporal adverbs accurately.",
                    "I can use 4 key terms for reported statements and citing.",
                    "I can transform direct utterances into elegant indirect discourse."
                ]
            },
            {"type": "recycle", "count": 3},
            {"type": "vocabulary", "ref": "vocabulary/b1/b1-33-01-voc.json"},
            {"type": "grammar", "ref": "grammar/b1/b1-33-01-a-gr.json"},
            {"type": "grammar", "ref": "grammar/b1/b1-33-01-b-gr.json"},
            {
                "type": "exercise-group",
                "title": "Practice",
                "ref": "exercises/b1/b1-33-01-ex.json",
                "exerciseRefs": [
                    "b1-33-01.ex01",
                    "b1-33-01.ex02",
                    "b1-33-01.ex03",
                    "b1-33-01.ex04",
                    "b1-33-01.ex05",
                    "b1-33-01.ex06",
                    "b1-33-01.ex07",
                    "b1-33-01.ex08"
                ]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-33-01.json", lesson_01)

    lesson_02 = {
        "id": "lesson.b1.33-02",
        "unit": 33,
        "title": "Hivatalos nyilatkozatok: Állítás és cáfolat (Official Statements & Denials)",
        "level": "B1",
        "grammar": "Formal Reporting Verbs (állít, megjegyez, bejelent) & Denials with tagad and cáfol",
        "sections": [
            {
                "type": "goal",
                "title": "Lesson Goals",
                "items": [
                    "I can use formal reporting verbs in press releases and official statements.",
                    "I can formulate clear denials and refutations using tagadja and cáfolja.",
                    "I can acquire 4 media and press reporting terms.",
                    "I can summarize news reports with accurate attribution."
                ]
            },
            {"type": "recycle", "count": 3},
            {"type": "vocabulary", "ref": "vocabulary/b1/b1-33-02-voc.json"},
            {"type": "grammar", "ref": "grammar/b1/b1-33-02-a-gr.json"},
            {"type": "grammar", "ref": "grammar/b1/b1-33-02-b-gr.json"},
            {
                "type": "exercise-group",
                "title": "Practice",
                "ref": "exercises/b1/b1-33-02-ex.json",
                "exerciseRefs": [
                    "b1-33-02.ex01",
                    "b1-33-02.ex02",
                    "b1-33-02.ex03",
                    "b1-33-02.ex04",
                    "b1-33-02.ex05",
                    "b1-33-02.ex06",
                    "b1-33-02.ex07",
                    "b1-33-02.ex08"
                ]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-33-02.json", lesson_02)

    lesson_03 = {
        "id": "lesson.b1.33-03",
        "unit": 33,
        "title": "Érdeklődés és közvetett kérdések (Indirect Questions & The -e Particle)",
        "level": "B1",
        "grammar": "Indirect Polar Questions with -e & Embedded Wh-Questions in Hungarian",
        "sections": [
            {
                "type": "goal",
                "title": "Lesson Goals",
                "items": [
                    "I can form indirect polar questions using the enclitic -e on verbs or focus.",
                    "I can report information questions beginning with question words without -e.",
                    "I can use 4 inquiry and information-gathering vocabulary words.",
                    "I can conduct polite inquiries and report interview questions."
                ]
            },
            {"type": "recycle", "count": 3},
            {"type": "vocabulary", "ref": "vocabulary/b1/b1-33-03-voc.json"},
            {"type": "grammar", "ref": "grammar/b1/b1-33-03-a-gr.json"},
            {"type": "grammar", "ref": "grammar/b1/b1-33-03-b-gr.json"},
            {
                "type": "exercise-group",
                "title": "Practice",
                "ref": "exercises/b1/b1-33-03-ex.json",
                "exerciseRefs": [
                    "b1-33-03.ex01",
                    "b1-33-03.ex02",
                    "b1-33-03.ex03",
                    "b1-33-03.ex04",
                    "b1-33-03.ex05",
                    "b1-33-03.ex06",
                    "b1-33-03.ex07",
                    "b1-33-03.ex08"
                ]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-33-03.json", lesson_03)

    lesson_04 = {
        "id": "lesson.b1.33-04",
        "unit": 33,
        "title": "Utasítások és kérések: Felszólítás függő beszédben (Commands & Requests)",
        "level": "B1",
        "grammar": "Subjunctive-Imperative (-jon/-jen) in Reported Commands and Polite Requests",
        "sections": [
            {
                "type": "goal",
                "title": "Lesson Goals",
                "items": [
                    "I can report imperative commands using subjunctive clauses with hogy.",
                    "I can report polite requests using kéri, hogy... and governing structures.",
                    "I can use 4 directive, petition, and claim vocabulary words.",
                    "I can adjust reporting tone from strict orders to polite invitations."
                ]
            },
            {"type": "recycle", "count": 3},
            {"type": "vocabulary", "ref": "vocabulary/b1/b1-33-04-voc.json"},
            {"type": "grammar", "ref": "grammar/b1/b1-33-04-a-gr.json"},
            {"type": "grammar", "ref": "grammar/b1/b1-33-04-b-gr.json"},
            {
                "type": "exercise-group",
                "title": "Practice",
                "ref": "exercises/b1/b1-33-04-ex.json",
                "exerciseRefs": [
                    "b1-33-04.ex01",
                    "b1-33-04.ex02",
                    "b1-33-04.ex03",
                    "b1-33-04.ex04",
                    "b1-33-04.ex05",
                    "b1-33-04.ex06",
                    "b1-33-04.ex07",
                    "b1-33-04.ex08"
                ]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-33-04.json", lesson_04)

    lesson_05 = {
        "id": "lesson.b1.33-05",
        "unit": 33,
        "title": "Híresztelések, sajtóhírek és a legenda (Hearsay, Rumors & Mikszáth's Classic)",
        "level": "B1",
        "grammar": "Evidential Hearsay (állítólag, úgy hírlik) & Attributing Sources in Hungarian",
        "sections": [
            {
                "type": "goal",
                "title": "Lesson Goals",
                "items": [
                    "I can express unverified rumors and hearsay using állítólag and úgy hírlik.",
                    "I can cite and attribute sources using arra hivatkozik and szavai szerint.",
                    "I can use 4 vocabulary terms for rumors, gossip, and media coverage.",
                    "I can read and analyze Mikszáth Kálmán's classic 'Szent Péter esernyője'."
                ]
            },
            {"type": "recycle", "count": 3},
            {"type": "vocabulary", "ref": "vocabulary/b1/b1-33-05-voc.json"},
            {"type": "grammar", "ref": "grammar/b1/b1-33-05-a-gr.json"},
            {"type": "grammar", "ref": "grammar/b1/b1-33-05-b-gr.json"},
            {
                "type": "exercise-group",
                "title": "Practice",
                "ref": "exercises/b1/b1-33-05-ex.json",
                "exerciseRefs": [
                    "b1-33-05.ex01",
                    "b1-33-05.ex02",
                    "b1-33-05.ex03",
                    "b1-33-05.ex04",
                    "b1-33-05.ex05",
                    "b1-33-05.ex06",
                    "b1-33-05.ex07",
                    "b1-33-05.ex08"
                ]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-33-05.json", lesson_05)

    lesson_con = {
        "id": "lesson.b1.33-consolidation",
        "unit": 33,
        "title": "Unit 33 Consolidation (Függő beszéd és híradás)",
        "level": "B1",
        "grammar": "Consolidation of Reported Speech, Indirect Inquiries & Mikszáth's Szent Péter esernyője",
        "sections": [
            {
                "type": "story",
                "title": "Szent Péter esernyője (Mikszáth Kálmán)",
                "ref": "stories/classics/b1/b1-33-mikszath.json"
            },
            {
                "type": "exercise-group",
                "title": "Consolidation Practice",
                "ref": "exercises/b1/b1-33-consolidation-ex.json",
                "exerciseRefs": [
                    "b1-33-consolidation.ex01",
                    "b1-33-consolidation.ex02",
                    "b1-33-consolidation.ex03",
                    "b1-33-consolidation.ex04",
                    "b1-33-consolidation.ex05",
                    "b1-33-consolidation.ex06",
                    "b1-33-consolidation.ex07",
                    "b1-33-consolidation.ex08"
                ]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-33-consolidation.json", lesson_con)

    print("Successfully built Hungarian B1 Core Unit 33 (b1-33)!")

if __name__ == "__main__":
    build_unit_33_core()
