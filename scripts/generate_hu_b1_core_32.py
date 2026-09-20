#!/usr/bin/env python3
"""Generate Hungarian B1 Core Unit 32: Connecting Ideas (b1-32)."""

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

def build_unit_32_core():
    # -------------------------------------------------------------------------
    # 1. Vocabulary Files (4 words each = 20 words total)
    # -------------------------------------------------------------------------
    voc_01 = {
        "id": "vocab.b1.32.01",
        "lesson": "b1-32-01",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "következtetés", "translation": "conclusion, inference, deduction", "pos": "noun"},
            {"lemma": "érvelés", "translation": "argumentation, reasoning, line of argument", "pos": "noun"},
            {"lemma": "alátámasztás", "translation": "corroboration, substantiation, support", "pos": "noun"},
            {"lemma": "összefoglalás", "translation": "summary, recapitulation, synthesis", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-32-01-voc.json", voc_01)

    voc_02 = {
        "id": "vocab.b1.32.02",
        "lesson": "b1-32-02",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "összefüggés", "translation": "connection, coherence, interrelation", "pos": "noun"},
            {"lemma": "bekezdés", "translation": "paragraph, section of a text", "pos": "noun"},
            {"lemma": "gondolatmenet", "translation": "train of thought, sequence of ideas", "pos": "noun"},
            {"lemma": "átvezetés", "translation": "transition, segue, connective link", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-32-02-voc.json", voc_02)

    voc_03 = {
        "id": "vocab.b1.32.03",
        "lesson": "b1-32-03",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "ellentét", "translation": "contrast, opposition, polarity", "pos": "noun"},
            {"lemma": "szembeállítás", "translation": "juxtaposition, confronting of views", "pos": "noun"},
            {"lemma": "árnyalás", "translation": "nuancing, qualification, fine-tuning", "pos": "noun"},
            {"lemma": "megkülönböztetés", "translation": "distinction, differentiation", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-32-03-voc.json", voc_03)

    voc_04 = {
        "id": "vocab.b1.32.04",
        "lesson": "b1-32-04",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "ok-okozati viszony", "translation": "cause-and-effect relationship", "pos": "noun"},
            {"lemma": "feltétel", "translation": "condition, prerequisite, proviso", "pos": "noun"},
            {"lemma": "engedmény", "translation": "concession, allowance", "pos": "noun"},
            {"lemma": "következmény", "translation": "consequence, outcome, result", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-32-04-voc.json", voc_04)

    voc_05 = {
        "id": "vocab.b1.32.05",
        "lesson": "b1-32-05",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "szövegkohézió", "translation": "textual cohesion, coherence", "pos": "noun"},
            {"lemma": "kifejezőkészség", "translation": "expressive skill, fluency, eloquence", "pos": "noun"},
            {"lemma": "világosság", "translation": "clarity, lucidity, transparency", "pos": "noun"},
            {"lemma": "meggyőzőerő", "translation": "persuasive power, cogency", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-32-05-voc.json", voc_05)

    # -------------------------------------------------------------------------
    # 2. Grammar Files (2 per lesson = 10 files)
    # -------------------------------------------------------------------------
    # Lesson 01
    gr_01_a = {
        "id": "grammar.b1.32.01.consequence-connectors",
        "title": "Logical Consequence Connectors: Tehát, Ennélfogva & Következésképpen",
        "sections": [
            {
                "type": "text",
                "title": "Consequence Connectors",
                "content": "Hungarian connectors expressing logical consequence range from everyday speech to formal written register: *tehát* (therefore, so), *ennélfogva* (hence, accordingly), and *következésképpen* (consequently). They usually appear at the head of the consequent clause."
            },
            {
                "type": "examples",
                "title": "Consequence examples",
                "items": [
                    {"spanish": "Minden feltétel teljesült, tehát aláírhatjuk a megállapodást.", "english": "All conditions have been met, therefore we can sign the agreement."},
                    {"spanish": "A források korlátozottak, ennélfogva takarékoskodnunk kell.", "english": "Resources are limited, hence we must economize."},
                    {"spanish": "A bizonyítékok egyértelműek, következésképpen elfogadjuk az érveket.", "english": "The evidence is unambiguous, consequently we accept the arguments."}
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-32-01-a-gr.json", gr_01_a)

    gr_01_b = {
        "id": "grammar.b1.32.01.additive-connectors",
        "title": "Additive Discourse Connectors: Ráadásul, Továbbá & Mindemellett",
        "sections": [
            {
                "type": "text",
                "title": "Additive Markers",
                "content": "To accumulate arguments, Hungarian uses additive conjunctions: *ráadásul* (moreover, what is more), *továbbá* (furthermore), and *mindemellett* (along with this, in addition)."
            },
            {
                "type": "examples",
                "title": "Additive examples",
                "items": [
                    {"spanish": "A terv gazdaságos, ráadásul környezetbarát is.", "english": "The plan is economical, and moreover it is also environmentally friendly."},
                    {"spanish": "Továbbá szeretném kiemelni a kollégák áldozatos munkáját.", "english": "Furthermore, I would like to highlight the dedicated work of the colleagues."},
                    {"spanish": "Mindemellett nem szabad megfeledkeznünk a felmerülő kockázatokról sem.", "english": "In addition to this, we must not forget about the emerging risks either."}
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-32-01-b-gr.json", gr_01_b)

    # Lesson 02
    gr_02_a = {
        "id": "grammar.b1.32.02.discourse-signposts",
        "title": "Discourse Signposts & Transitions: Mindenekelőtt & Ami a ... illeti",
        "sections": [
            {
                "type": "text",
                "title": "Structuring Signposts",
                "content": "Structuring paragraphs requires explicit signposts: *mindenekelőtt* (first and foremost), *másfelől* (on the other hand), *ami a [tárgyat] illeti* (as far as [subject] is concerned)."
            },
            {
                "type": "examples",
                "title": "Signpost examples",
                "items": [
                    {"spanish": "Mindenekelőtt tisztáznunk kell a legalapvetőbb fogalmakat.", "english": "First and foremost, we must clarify the most fundamental concepts."},
                    {"spanish": "Ami a költségvetést illeti, minden részletet pontosan kiszámoltunk.", "english": "As far as the budget is concerned, we calculated every detail precisely."},
                    {"spanish": "Másfelől figyelembe kell vennünk a lakosság véleményét is.", "english": "On the other hand, we must also take the opinion of the public into account."}
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-32-02-a-gr.json", gr_02_a)

    gr_02_b = {
        "id": "grammar.b1.32.02.demonstrative-periods",
        "title": "Structuring Complex Multi-Clause Periods with Correlative Pronouns",
        "sections": [
            {
                "type": "text",
                "title": "Correlative Pronoun Pairs",
                "content": "Hungarian achieves high textual cohesion by anchoring subordinate clauses with demonstratives in the main clause: *azért..., mert...* (for that reason... because), *úgy..., ahogy...* (in such a way... as), *arról..., hogy...* (about the fact... that)."
            },
            {
                "type": "examples",
                "title": "Correlative period examples",
                "items": [
                    {"spanish": "Pontosan azért érvelünk így, mert a jövő biztonsága a célunk.", "english": "We argue in this manner precisely because our goal is the safety of the future."},
                    {"spanish": "A dolgok úgy alakultak, ahogy a szakértők előre jelezték.", "english": "Matters unfolded just as the experts had predicted."},
                    {"spanish": "Meggyőződtünk arról, hogy a javaslat minden szempontból megalapozott.", "english": "We became convinced that the proposal is substantiated in every aspect."}
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-32-02-b-gr.json", gr_02_b)

    # Lesson 03
    gr_03_a = {
        "id": "grammar.b1.32.03.adversative-contrast",
        "title": "Adversative Contrast Markers: Azonban, Viszont & Mindazonáltal",
        "sections": [
            {
                "type": "text",
                "title": "Contrast Markers",
                "content": "To introduce sharp or nuanced contrast between ideas, Hungarian uses adversative conjunctions: *azonban* (however - positioned second in the clause), *viszont* (on the other hand, but), and *mindazonáltal* (nevertheless, nonetheless)."
            },
            {
                "type": "examples",
                "title": "Contrast examples",
                "items": [
                    {"spanish": "Az elmélet vonzó, a gyakorlatban azonban komoly nehézségek adódnak.", "english": "The theory is attractive; in practice, however, serious difficulties arise."},
                    {"spanish": "Sokan elutasították a javaslatot, ő viszont határozottan kiállt mellette.", "english": "Many rejected the proposal; he, on the other hand, stood firmly by it."},
                    {"spanish": "A helyzet bonyolult, mindazonáltal van remény a békés megállapodásra.", "english": "The situation is complex; nonetheless, there is hope for a peaceful agreement."}
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-32-03-a-gr.json", gr_03_a)

    gr_03_b = {
        "id": "grammar.b1.32.03.concessive-balance",
        "title": "Concessive Balance: Jóllehet, Bár... Mégis & Ennek dacára",
        "sections": [
            {
                "type": "text",
                "title": "Concessive Structures",
                "content": "Concessive balance weighs an acknowledged drawback against a triumphant conclusion: *jóllehet* (although, albeit), *bár... mégis* (although... nevertheless), and *ennek dacára* (in spite of this)."
            },
            {
                "type": "examples",
                "title": "Concessive examples",
                "items": [
                    {"spanish": "Jóllehet sok időbe telt, sikerült befejezni a kutatást.", "english": "Although it took much time, we succeeded in finishing the research."},
                    {"spanish": "Bár a feladat rendkívül nehéz volt, mégis helytálltak a munkatársak.", "english": "Although the task was exceptionally difficult, the coworkers nevertheless stood their ground."},
                    {"spanish": "Minden akadálynak dacára elértük a kitűzött célt.", "english": "In spite of all obstacles, we reached the set goal."}
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-32-03-b-gr.json", gr_03_b)

    # Lesson 04
    gr_04_a = {
        "id": "grammar.b1.32.04.causal-conditional-linkages",
        "title": "Causal & Conditional Linkages: Mivel, Tekintettel arra & Feltéve",
        "sections": [
            {
                "type": "text",
                "title": "Causal and Conditional Formulations",
                "content": "Causal and conditional clauses articulate complex logic: *mivel* (since, inasmuch as), *tekintettel arra, hogy* (in view of the fact that), and *feltéve, ha / feltéve, hogy* (provided that)."
            },
            {
                "type": "examples",
                "title": "Causal and conditional examples",
                "items": [
                    {"spanish": "Mivel minden adat rendelkezésre áll, megalapozott döntést hozhatunk.", "english": "Since all data is available, we can make an informed decision."},
                    {"spanish": "Tekintettel arra, hogy az idő sürget, azonnal cselekednünk kell.", "english": "In view of the fact that time is pressing, we must act immediately."},
                    {"spanish": "A szerződés érvényes, feltéve, hogy mindkét fél aláírja.", "english": "The contract is valid, provided that both parties sign it."}
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-32-04-a-gr.json", gr_04_a)

    gr_04_b = {
        "id": "grammar.b1.32.04.resultative-subordination",
        "title": "Resultative Subordination: Olyannyira..., Hogy & Odáig vezetett",
        "sections": [
            {
                "type": "text",
                "title": "Resultative Intensity",
                "content": "Expressing an intense degree that culminates in an outcome uses correlative intensifiers: *olyannyira..., hogy...* (so much so that) and *odáig vezetett, hogy...* (led to the point that)."
            },
            {
                "type": "examples",
                "title": "Resultative examples",
                "items": [
                    {"spanish": "A vita olyannyira elmérgesedett, hogy meg kellett szakítani a tárgyalást.", "english": "The dispute became so bitter that the negotiation had to be interrupted."},
                    {"spanish": "A kitartó munka odáig vezetett, hogy a vállalkozás nemzetközi hírűvé vált.", "english": "Persistent work led to the point that the enterprise became internationally renowned."},
                    {"spanish": "Olyan meggyőzően érvelt, hogy mindenkit maga mellé állított.", "english": "He argued so convincingly that he won everyone over to his side."}
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-32-04-b-gr.json", gr_04_b)

    # Lesson 05
    gr_05_a = {
        "id": "grammar.b1.32.05.stylistic-anaphora",
        "title": "Stylistic Cohesive Anaphora: Az előbbi, Az utóbbi & Mindezek alapján",
        "sections": [
            {
                "type": "text",
                "title": "Pronominal and Anaphoric Linkage",
                "content": "Elegant written Hungarian connects paragraphs using contrastive anaphoric pronouns: *az előbbi* (the former), *az utóbbi* (the latter), and summarizing formulas like *mindezek alapján* (on the basis of all these)."
            },
            {
                "type": "examples",
                "title": "Anaphora examples",
                "items": [
                    {"spanish": "Két lehetőséget vizsgáltunk meg: az előbbi költségesebb, az utóbbi viszont gyorsabb.", "english": "We examined two options: the former is more costly, the latter, however, is faster."},
                    {"spanish": "Mindezek alapján egyértelmű, hogy melyik irányt kell választanunk.", "english": "On the basis of all these, it is clear which direction we must choose."},
                    {"spanish": "A gondolatmenet logikus és szerves egységet alkot.", "english": "The train of thought is logical and forms an organic unity."}
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-32-05-a-gr.json", gr_05_a)

    gr_05_b = {
        "id": "grammar.b1.32.05.rhetorical-emphasis",
        "title": "Rhetorical Emphasis: Nem pusztán..., Hanem egyenesen",
        "sections": [
            {
                "type": "text",
                "title": "Climactic Emphasis",
                "content": "Climaxing an argumentative sequence employs heightened contrastive formulas: *nem pusztán..., hanem egyenesen...* (not merely... but outright / positively) and *különös tekintettel vmire* (with particular regard to)."
            },
            {
                "type": "examples",
                "title": "Emphasis examples",
                "items": [
                    {"spanish": "A lépés nem pusztán hasznos, hanem egyenesen elengedhetetlen volt.", "english": "The step was not merely useful, but outright indispensable."},
                    {"spanish": "Különös tekintettel kell lennünk a fiatal generáció igényeire.", "english": "We must have particular regard to the needs of the younger generation."},
                    {"spanish": "Az írás világossága és meggyőzőereje példaértékű minden olvasó számára.", "english": "The clarity and persuasive power of the writing is exemplary for every reader."}
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-32-05-b-gr.json", gr_05_b)

    # -------------------------------------------------------------------------
    # 3. Exercises Files (8 exercises per lesson x 5 + consolidation = 6 files)
    # -------------------------------------------------------------------------
    ex_01 = {
        "lesson": "b1-32-01",
        "exercises": [
            {
                "id": "b1-32-01.ex01",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent a 'következtetés' levonása egy vitában?",
                "options": [
                    "A felhozott tényekből és érvekből logikusan adódó záró megállapítás megfogalmazását.",
                    "A szavazólapok megszámlálását a folyosón.",
                    "A vita azonnali félbeszakítását vacsorázás miatt."
                ],
                "correct": 0
            },
            {
                "id": "b1-32-01.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Minden feltétel teljesült, tehát aláírhatjuk a megállapodás_____. (the agreement - t)",
                "answer": "t"
            },
            {
                "id": "b1-32-01.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "bizonyítékok", "egyértelműek,", "következésképpen", "elfogadjuk", "a", "döntést."],
                "solution": ["A", "bizonyítékok", "egyértelműek,", "következésképpen", "elfogadjuk", "a", "döntést."]
            },
            {
                "id": "b1-32-01.ex04",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik kötőszó fejezi ki, hogy egy további nyomós érvet fűzünk az előzőekhez?",
                "options": [
                    "Ráadásul",
                    "Ehelyett",
                    "Noha"
                ],
                "correct": 0
            },
            {
                "id": "b1-32-01.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A precíz érvelés szilárd alátámasztás_____ igényel. (support - t)",
                "answer": "t"
            },
            {
                "id": "b1-32-01.ex06",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mi az 'összefoglalás' célja egy előadás vagy írás végén?",
                "options": [
                    "A legfontosabb gondolatok lényegretörő áttekintése és szintetizálása.",
                    "Az összes fejezet szóról szóra való újraolvasása.",
                    "Új, ismeretlen témák felvetése a hallgatóságnak."
                ],
                "correct": 0
            },
            {
                "id": "b1-32-01.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A javaslat gazdaságos, ráadásul környezetbarát _____. (also - is)",
                "answer": "is"
            },
            {
                "id": "b1-32-01.ex08",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "logikus", "érvelés", "segít", "meggyőzni", "a", "kételkedőket."],
                "solution": ["A", "logikus", "érvelés", "segít", "meggyőzni", "a", "kételkedőket."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-32-01-ex.json", ex_01)

    ex_02 = {
        "lesson": "b1-32-02",
        "exercises": [
            {
                "id": "b1-32-02.ex01",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit nevezünk 'gondolatmenetnek' egy esszében vagy szövegben?",
                "options": [
                    "A gondolatok egymásra épülő, logikus sorrendjét és haladási irányát.",
                    "Egy gyors sétát a friss levegőn ebéd után.",
                    "A szótárban szereplő szavak ábécérendjét."
                ],
                "correct": 0
            },
            {
                "id": "b1-32-02.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Mindenekelőtt tisztáznunk kell a legfontosabb alapfogalmak_____. (the concepts - at)",
                "answer": "at"
            },
            {
                "id": "b1-32-02.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Ami", "a", "költségeket", "illeti,", "minden", "tételt", "gondosan", "ellenőriztünk."],
                "solution": ["Ami", "a", "költségeket", "illeti,", "minden", "tételt", "gondosan", "ellenőriztünk."]
            },
            {
                "id": "b1-32-02.ex04",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Hogyan kapcsoljuk össze helyesen a főmondatot és a mellékmondatot mutató névmással?",
                "options": [
                    "Pontosan azért cselekedtünk így, mert a jövő biztonságát akartuk védeni.",
                    "Azért cselekedtünk mert tegnap jött a vonat.",
                    "Úgy cselekedtünk mint a fa a kertben."
                ],
                "correct": 0
            },
            {
                "id": "b1-32-02.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A két bekezdés közötti átvezetés biztosítja a szöveg gördülékenység_____. (its smoothness - ét)",
                "answer": "ét"
            },
            {
                "id": "b1-32-02.ex06",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent a 'bekezdés' egy szövegben?",
                "options": [
                    "Egy önálló gondolati egységet képező szövegrészt, amely új sorral kezdődik.",
                    "A könyvtár ajtajának bezárását délután.",
                    "A toll hegyének tintával való feltöltését."
                ],
                "correct": 0
            },
            {
                "id": "b1-32-02.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A dolgok úgy alakultak, ahogy a szakértők előre lát_____. (saw it - ták)",
                "answer": "ták"
            },
            {
                "id": "b1-32-02.ex08",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "szövegrészek", "közötti", "összefüggés", "világossá", "teszi", "az", "egész", "művet."],
                "solution": ["A", "szövegrészek", "közötti", "összefüggés", "világossá", "teszi", "az", "egész", "művet."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-32-02-ex.json", ex_02)

    ex_03 = {
        "lesson": "b1-32-03",
        "exercises": [
            {
                "id": "b1-32-03.ex01",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent az érvek 'szembeállítása'?",
                "options": [
                    "Két különböző vagy ellentétes álláspont egymás mellé helyezését és összehasonlítását.",
                    "Két ember vitáját az utcai közlekedésben.",
                    "A székek felállítását egymással szemben az ebédlőben."
                ],
                "correct": 0
            },
            {
                "id": "b1-32-03.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Az elképzelés vonzó, a gyakorlatban azonban komoly akadályok merülnek fel_____. (up - fel)",
                "answer": "fel"
            },
            {
                "id": "b1-32-03.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Bár", "a", "feladat", "rendkívül", "bonyolult", "volt,", "mégis", "sikert", "értünk", "el."],
                "solution": ["Bár", "a", "feladat", "rendkívül", "bonyolult", "volt,", "mégis", "sikert", "értünk", "el."]
            },
            {
                "id": "b1-32-03.ex04",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik mondat alkalmaz helyes megengedő szerkezetet a 'jóllehet' kötőszóval?",
                "options": [
                    "Jóllehet fáradtak voltunk, mégis végig figyeltünk az előadásra.",
                    "Jóllehet fáradt ember sétál az erdőben este.",
                    "Fáradt volt jóllehet mert sokat dolgozott."
                ],
                "correct": 0
            },
            {
                "id": "b1-32-03.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A finom árnyalás segít elkerülni a szélsőséges leegyszerűsítés_____. (simplification - t)",
                "answer": "t"
            },
            {
                "id": "b1-32-03.ex06",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent a fogalmak pontos 'megkülönböztetése'?",
                "options": [
                    "Annak világos tisztázását, hogy miben tér el egymástól két hasonló dolog.",
                    "A könyvek különböző polcokra tétele szín szerint.",
                    "Az új ruhák megjelölése névtáblával."
                ],
                "correct": 0
            },
            {
                "id": "b1-32-03.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Minden akadály dacá_____ megőrizték a hitüket a győzelemben. (in spite of - ra)",
                "answer": "ra"
            },
            {
                "id": "b1-32-03.ex08",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["Az", "ellentétek", "feloldása", "nyitja", "meg", "az", "utat", "a", "megbékéléshez."],
                "solution": ["Az", "ellentétek", "feloldása", "nyitja", "meg", "az", "utat", "a", "megbékéléshez."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-32-03-ex.json", ex_03)

    ex_04 = {
        "lesson": "b1-32-04",
        "exercises": [
            {
                "id": "b1-32-04.ex01",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent az 'ok-okozati viszony' megértése?",
                "options": [
                    "Annak felismerését, hogy mi váltott ki egy eseményt, és az milyen következményekkel járt.",
                    "A szótárban az 'O' betűs szavak megtalálását.",
                    "Egy orvosi recept helyes felolvasását a patikában."
                ],
                "correct": 0
            },
            {
                "id": "b1-32-04.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Mivel minden adat rendelkezésre áll, megalapozott döntést hoz_____ meg. (we make - unk)",
                "answer": "unk"
            },
            {
                "id": "b1-32-04.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Tekintettel", "arra,", "hogy", "az", "idő", "sürget,", "azonnal", "lépnünk", "kell."],
                "solution": ["Tekintettel", "arra,", "hogy", "az", "idő", "sürget,", "azonnal", "lépnünk", "kell."]
            },
            {
                "id": "b1-32-04.ex04",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Hogyan fejezzük ki a feltételt a 'feltéve, hogy' kifejezéssel?",
                "options": [
                    "A megállapodás érvénybe lép, feltéve, hogy mindkét fél jóváhagyja.",
                    "Feltéve a kalapot az asztalra elmentem aludni.",
                    "A kalap feltéve áll a szekrényben."
                ],
                "correct": 0
            },
            {
                "id": "b1-32-04.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A kölcsönös engedmény_____ révén sikerült kompromisszumot kötni. (concessions - ek)",
                "answer": "ek"
            },
            {
                "id": "b1-32-04.ex06",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mi az 'engedmény' egy tárgyalási folyamatban?",
                "options": [
                    "Olyan kompromisszumos lépés, amikor valaki lemond bizonyos követelésekről a megállapodás érdekében.",
                    "Egy áruházi kedvezményes kupon.",
                    "A gépkocsi sebességének csökkentése a kanyarban."
                ],
                "correct": 0
            },
            {
                "id": "b1-32-04.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A vita olyannyira elmérgesedett, hogy meg kellett szakítani a tárgyalás_____. (the negotiation - t)",
                "answer": "t"
            },
            {
                "id": "b1-32-04.ex08",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "kitartó", "munka", "odáig", "vezetett,", "hogy", "a", "cél", "megvalósult."],
                "solution": ["A", "kitartó", "munka", "odáig", "vezetett,", "hogy", "a", "cél", "megvalósult."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-32-04-ex.json", ex_04)

    ex_05 = {
        "lesson": "b1-32-05",
        "exercises": [
            {
                "id": "b1-32-05.ex01",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent a 'szövegkohézió' kifejezés?",
                "options": [
                    "A szövegelemek belső logikai és nyelvtani összefüggését, összetartó erejét.",
                    "A könyv lapjainak összeragasztását a nyomdában.",
                    "A papír vastagságának mérését milliméterben."
                ],
                "correct": 0
            },
            {
                "id": "b1-32-05.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Mindezek alapján egyértelmű, hogy melyik utat kell választanunk a jövő_____. (for future - ben)",
                "answer": "ben"
            },
            {
                "id": "b1-32-05.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "lépés", "nem", "pusztán", "hasznos,", "hanem", "egyenesen", "elengedhetetlen", "volt."],
                "solution": ["A", "lépés", "nem", "pusztán", "hasznos,", "hanem", "egyenesen", "elengedhetetlen", "volt."]
            },
            {
                "id": "b1-32-05.ex04",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Hogyan hivatkozunk két korábban említett dologra az 'előbbi' és 'utóbbi' szavakkal?",
                "options": [
                    "Két tervet vizsgáltunk meg: az előbbi túl drága, az utóbbi viszont reális és megvalósítható.",
                    "Az előbbi és az utóbbi futott a játszótéren tegnap délután.",
                    "Előbb ment el a vonat mint az utóbb."
                ],
                "correct": 0
            },
            {
                "id": "b1-32-05.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A szónok beszéde rendkívüli meggyőzőerő_____ bírt. (power - vel)",
                "answer": "vel"
            },
            {
                "id": "b1-32-05.ex06",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Miért dönt úgy Timár Mihály Jókai Mór 'Az arany ember' című regényének végén, hogy a Senki szigetén marad?",
                "options": [
                    "Mert rádöbben, hogy a gazdagság és a társadalmi dicsőség nem hozott lelki békét, s az igaz szerelmet és tiszta boldogságot Noémi mellett, a természetben találta meg.",
                    "Mert elveszítette az összes pénzét egy szerencsejátékon Bécsben.",
                    "Mert elromlott a Szent Borbála gőzhajó kormánya a Dunán."
                ],
                "correct": 0
            },
            {
                "id": "b1-32-05.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Különös tekintettel kell lennünk a fiatal generáció igényei_____. (to their needs - re)",
                "answer": "re"
            },
            {
                "id": "b1-32-05.ex08",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "gondolatok", "világossága", "és", "ereje", "minden", "olvasót", "magával", "ragad."],
                "solution": ["A", "gondolatok", "világossága", "és", "ereje", "minden", "olvasót", "magával", "ragad."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-32-05-ex.json", ex_05)

    ex_consolidation = {
        "lesson": "b1-32-consolidation",
        "exercises": [
            {
                "id": "b1-32-consolidation.ex01",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Melyik szó jelenti a kifejezés pontosságát, átláthatóságát és érthetőségét?",
                "options": [
                    "Világosság",
                    "Kétértelműség",
                    "Hanyagság"
                ],
                "correct": 0
            },
            {
                "id": "b1-32-consolidation.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Mivel minden feltétel teljesült, következésképpen megkezdhetjük a munká_____. (the work - t)",
                "answer": "t"
            },
            {
                "id": "b1-32-consolidation.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "gondolatok", "szerves", "kapcsolódása", "adja", "meg", "az", "érvelés", "erejét."],
                "solution": ["A", "gondolatok", "szerves", "kapcsolódása", "adja", "meg", "az", "érvelés", "erejét."]
            },
            {
                "id": "b1-32-consolidation.ex04",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Hogyan fejezzük ki helyesen a két ellentétes nézet egymás mellé állítását?",
                "options": [
                    "Egyfelől a fejlődés új esélyeket nyújt, másfelől viszont körültekintést igényel.",
                    "Fejlődés van másfelől egyfelől tegnap este.",
                    "Szemben áll a ház az erdővel."
                ],
                "correct": 0
            },
            {
                "id": "b1-32-consolidation.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A szövegkohézió hiánya megnehezíti az olvasó számára a megértés_____. (its understanding - t)",
                "answer": "t"
            },
            {
                "id": "b1-32-consolidation.ex06",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "meggyőzőerő", "a", "tényeken", "és", "a", "hitelességen", "alapszik."],
                "solution": ["A", "meggyőzőerő", "a", "tényeken", "és", "a", "hitelességen", "alapszik."]
            },
            {
                "id": "b1-32-consolidation.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Mindezek alapján levonhatjuk a végső következtetés_____. (the conclusion - t)",
                "answer": "t"
            },
            {
                "id": "b1-32-consolidation.ex08",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Milyen erkölcsi tanulságot hordoz Timár Mihály története Jókai remekművében?",
                "options": [
                    "Hogy a vagyon önmagában nem hoz boldogságot; a lelkiismeret tisztasága és a szeretet sokkal értékesebb minden földi kincsnél.",
                    "Hogy a dunai hajózás veszélytelen vállalkozás.",
                    "Hogy mindig a legdrágább ruhákat kell megvenni a piacon."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-32-consolidation-ex.json", ex_consolidation)

    # -------------------------------------------------------------------------
    # 4. Classic Story Adaptation for Consolidation: Az arany ember
    # -------------------------------------------------------------------------
    story_classic = {
        "id": "story.b1.32.classic",
        "title": "Az arany ember",
        "level": "B1",
        "order": 32,
        "type": "classics",
        "estimatedMinutes": 8,
        "summary": "An adaptation of Mór Jókai's immortal romantic masterpiece 'Az arany ember' (The Man with the Golden Touch / The Man of Gold, 1872). Timár Mihály, a humble cargo-ship captain on the Danube, miraculously saves the daughter of a fleeing Turkish pasha and stumbles upon a sunken fortune. Everything he touches turns to gold; he becomes a wealthy merchant, an honored councillor, and marries the cold, grateful Tímea. Yet wealth brings him agonizing guilt and emptiness. Only on the idyllic, untouched 'Senki szigete' (Nobody's Island), in the tender love of Noémi, does Timár find true redemption, ultimately leaving his fortune behind to live in peace and harmony with nature.",
        "characters": [
            "Timár Mihály, a tehetséges hajóbiztos, később gazdag kereskedő ('az arany ember')",
            "Tímea, a török pasa leánya, Timár hűséges, de hűvös felesége",
            "Noémi, a Senki szigetén élő tiszta lelkű leány",
            "Teréza mama, Noémi édesanyja, a sziget békéjének őrzője"
        ],
        "location": "A Duna, Komárom, a Balaton és a Senki szigete",
        "author": "Jókai Mór",
        "work": "Az arany ember (1872)",
        "paragraphs": [
            {
                "type": "narration",
                "text": "Timár Mihály tehetséges és becsületes hajóbiztosként vezette a 'Szent Borbála' nevű gabonaszállító hajót a Dunán. A hajón menekült a török szultán elől Ali Csorbadzsi pasa leányával, a szépséges Tímeával."
            },
            {
                "type": "narration",
                "text": "Amikor a hajó zátonyra futott és elsüllyedt, Timár kimentette Tímeát. A megázott búzászsákok között azonban felbecsülhetetlen értékű kincset: aranyat és drágaköveket talált, amelyeket a haldokló pasa a lányára bízott."
            },
            {
                "type": "dialogue",
                "speaker": "Timár Mihály",
                "text": "Mit tegyek ezzel a kinccsel? Ha bejelentem, a kapzsi hivatalnokok elveszik... Ha magam használom fel, Tímeát gazdaggá és boldoggá tehetem!"
            },
            {
                "type": "narration",
                "text": "Mihály megtartotta a kincset, és vállalkozásaiba fektette. Bármihez nyúlt, arannyá változott: az ország leggazdagabb kereskedőjévé és köztiszteletben álló tanácsosává emelkedett. Feleségül vette Tímeát, de a házasságuk nem hozott boldogságot: a leány csak hálát érzett iránta, szerelmet soha."
            },
            {
                "type": "narration",
                "text": "A lelkiismeret-furdalás és a hazugság terhe alatt roskadozó Mihály a Duna vadregényes szakaszán fekvő Senki szigetére menekült, ahol Noémi és Teréza mama élt a természet csendes összhangjában."
            },
            {
                "type": "dialogue",
                "speaker": "Noémi",
                "text": "Itt nincsenek törvények, nincsenek pénzek, nincs hazugság, Mihály. Itt csak te vagy és én, és a szeretet, amely nem kér semmit, csak önmagát adja."
            },
            {
                "type": "narration",
                "text": "Amikor a sors váratlanul megoldotta kettős életének csomóját, Timár Mihály örökre elhagyta a kincseket, a palotát és a dicsőséget. A Senki szigetén maradt kertésznek Noémi oldalán: megértette, hogy a világ legaranyosabb embere sem a vagyonból, hanem a tiszta lelkiismeretből és az őszinte szeretetből meríti az igazi életet."
            }
        ]
    }
    write_json("content/hu/stories/classics/b1/b1-32-jokai.json", story_classic)

    # -------------------------------------------------------------------------
    # 5. Lesson Files (01 to 05 + consolidation)
    # -------------------------------------------------------------------------
    lesson_titles = {
        "01": ("Következtetés, érvelés és alátámasztás", "Inference, Reasoning & Substantiation"),
        "02": ("A gondolatmenet és a bekezdések felépítése", "Train of Thought & Paragraph Structure"),
        "03": ("Ellentétek, szembeállítás és árnyalás", "Contrasts, Juxtaposition & Nuance"),
        "04": ("Ok-okozati viszonyok és feltételek", "Causal Relations, Conditions & Concessions"),
        "05": ("Szövegkohézió, világosság és meggyőzőerő", "Textual Cohesion, Clarity & Persuasion")
    }

    grammar_refs = {
        "01": ["grammar/b1/b1-32-01-a-gr.json", "grammar/b1/b1-32-01-b-gr.json"],
        "02": ["grammar/b1/b1-32-02-a-gr.json", "grammar/b1/b1-32-02-b-gr.json"],
        "03": ["grammar/b1/b1-32-03-a-gr.json", "grammar/b1/b1-32-03-b-gr.json"],
        "04": ["grammar/b1/b1-32-04-a-gr.json", "grammar/b1/b1-32-04-b-gr.json"],
        "05": ["grammar/b1/b1-32-05-a-gr.json", "grammar/b1/b1-32-05-b-gr.json"]
    }

    for i in range(1, 6):
        padded = f"0{i}"
        hu_t, en_t = lesson_titles[padded]
        lesson_data = {
            "id": f"lesson.b1.32-{padded}",
            "unit": 32,
            "title": f"{hu_t} ({en_t})",
            "level": "B1",
            "grammar": "Discourse Connectors (tehát, azonban, ráadásul) & Textual Cohesion in Hungarian",
            "sections": [
                {
                    "type": "goal",
                    "title": "Lesson Goals",
                    "items": [
                        f"I can understand and apply {en_t} in Hungarian.",
                        "I can connect ideas using formal discourse markers (tehát, azonban, mindamellett, jóllehet).",
                        "I can build coherent paragraphs with demonstrative periods and contrastive signposts.",
                        "I can appreciate Mór Jókai's masterpiece 'Az arany ember' and its themes of conscience and redemption."
                    ]
                },
                {"type": "recycle", "count": 3},
                {"type": "vocabulary", "ref": f"vocabulary/b1/b1-32-{padded}-voc.json"},
                {"type": "grammar", "ref": grammar_refs[padded][0]},
                {"type": "grammar", "ref": grammar_refs[padded][1]},
                {
                    "type": "exercise-group",
                    "title": "Practice",
                    "ref": f"exercises/b1/b1-32-{padded}-ex.json",
                    "exerciseRefs": [f"b1-32-{padded}.ex0{k}" for k in range(1, 9)]
                }
            ]
        }
        write_json(f"content/hu/lessons/b1/b1-32-{padded}.json", lesson_data)

    consolidation_data = {
        "id": "lesson.b1.32-consolidation",
        "unit": 32,
        "title": "Unit 32 Consolidation",
        "level": "B1",
        "grammar": "Consolidation of Discourse Connectors, Text Cohesion & Jókai's Az arany ember",
        "sections": [
            {
                "type": "story",
                "title": "Az arany ember (Jókai Mór)",
                "ref": "stories/classics/b1/b1-32-jokai.json"
            },
            {
                "type": "exercise-group",
                "title": "Consolidation Practice",
                "ref": "exercises/b1/b1-32-consolidation-ex.json",
                "exerciseRefs": [f"b1-32-consolidation.ex0{k}" for k in range(1, 9)]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-32-consolidation.json", consolidation_data)
    print("Successfully built Hungarian B1 Core Unit 32 (b1-32)!")

if __name__ == "__main__":
    build_unit_32_core()
