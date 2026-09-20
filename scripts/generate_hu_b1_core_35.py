#!/usr/bin/env python3
"""Generate Hungarian B1 Core Unit 35: Hypotheticals & Possibilities (b1-35)."""

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

def build_unit_35_core():
    # -------------------------------------------------------------------------
    # 1. Vocabulary Files (4 words each = 20 words total)
    # -------------------------------------------------------------------------
    voc_01 = {
        "id": "vocab.b1.35.01",
        "lesson": "b1-35-01",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "feltételezés", "translation": "assumption, hypothesis, presupposition", "pos": "noun"},
            {"lemma": "képzeletbeli", "translation": "imaginary, fictional, hypothetical", "pos": "adjective"},
            {"lemma": "elképzelés", "translation": "idea, conception, mental notion", "pos": "noun"},
            {"lemma": "lehetőség", "translation": "possibility, opportunity, chance", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-35-01-voc.json", voc_01)

    voc_02 = {
        "id": "vocab.b1.35.02",
        "lesson": "b1-35-02",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "másként", "translation": "differently, in another manner", "pos": "adverb"},
            {"lemma": "máskülönben", "translation": "otherwise, or else", "pos": "adverb"},
            {"lemma": "eltérés", "translation": "divergence, difference, variance", "pos": "noun"},
            {"lemma": "fordulat", "translation": "turn of events, twist, pivot", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-35-02-voc.json", voc_02)

    voc_03 = {
        "id": "vocab.b1.35.03",
        "lesson": "b1-35-03",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "megbánás", "translation": "regret, remorse, repentance", "pos": "noun"},
            {"lemma": "mulasztás", "translation": "omission, failure to act, missed duty", "pos": "noun"},
            {"lemma": "kárba veszett", "translation": "wasted, gone to waste, in vain", "pos": "adjective"},
            {"lemma": "utólag", "translation": "in retrospect, after the fact, belatedly", "pos": "adverb"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-35-03-voc.json", voc_03)

    voc_04 = {
        "id": "vocab.b1.35.04",
        "lesson": "b1-35-04",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "eshetőség", "translation": "eventuality, contingency, possibility", "pos": "noun"},
            {"lemma": "forgatókönyv", "translation": "scenario, projected sequence, script", "pos": "noun"},
            {"lemma": "kockázat", "translation": "risk, hazard, jeopardy", "pos": "noun"},
            {"lemma": "kimenetel", "translation": "outcome, result, issue", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-35-04-voc.json", voc_04)

    voc_05 = {
        "id": "vocab.b1.35.05",
        "lesson": "b1-35-05",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "nosztalgia", "translation": "nostalgia, longing for the past", "pos": "noun"},
            {"lemma": "visszatekintés", "translation": "retrospection, review of the past", "pos": "noun"},
            {"lemma": "választás", "translation": "choice, election, option selected", "pos": "noun"},
            {"lemma": "sorsfordító", "translation": "fateful, destiny-altering, epochal", "pos": "adjective"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-35-05-voc.json", voc_05)

    # -------------------------------------------------------------------------
    # 2. Grammar Files (2 per regular lesson = 10 files)
    # -------------------------------------------------------------------------
    gr_01_a = {
        "id": "grammar.b1.35.01.past-conditional-volna",
        "title": "The Past Conditional: -tt volna (Unfulfilled Past Conditions)",
        "sections": [
            {
                "type": "text",
                "title": "Forming the Past Conditional",
                "content": "To express actions that would have happened in the past under counterfactual conditions, Hungarian adds the invariant auxiliary particle *volna* to the standard past tense verb form: *Ha tudtam volna, eljöttem volna* (If I had known, I would have come)."
            },
            {
                "type": "examples",
                "title": "Past conditional examples",
                "items": [
                    {"spanish": "Ha időben szóltál volna, segítettünk volna neked.", "english": "If you had spoken in time, we would have helped you."},
                    {"spanish": "Ha nem esett volna az eső, a szabadban sétáltunk volna.", "english": "If it hadn't rained, we would have walked outdoors."},
                    {"spanish": "Biztosan megértette volna a döntésünket, ha elmagyarázzuk.", "english": "He surely would have understood our decision if we had explained it."}
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-35-01-a-gr.json", gr_01_a)

    gr_01_b = {
        "id": "grammar.b1.35.01.irreal-wishes-barcsak",
        "title": "Irreal Past Wishes: Bárcsak... volna!",
        "sections": [
            {
                "type": "text",
                "title": "Expressing Past Desires",
                "content": "To voice deep, unfulfilled wishes regarding past events ('If only... had happened!'), Hungarian introduces the sentence with *bárcsak* followed by the past tense and *volna*."
            },
            {
                "type": "examples",
                "title": "Wish examples",
                "items": [
                    {"spanish": "Bárcsak korábban találkoztunk volna!", "english": "If only we had met earlier!"},
                    {"spanish": "Bárcsak maradt volna még egy kis időnk a beszélgetésre!", "english": "If only we had had a little more time left for talking!"},
                    {"spanish": "Bárcsak elfogadtam volna azt az állásajánlatot!", "english": "If only I had accepted that job offer!"}
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-35-01-b-gr.json", gr_01_b)

    gr_02_a = {
        "id": "grammar.b1.35.02.mixed-conditionals",
        "title": "Mixed Conditionals: Past Condition Leading to Present Result",
        "sections": [
            {
                "type": "text",
                "title": "Connecting Past Actions to Present State",
                "content": "When a past counterfactual condition impacts the present, the conditional clause takes the past conditional (*ha... lett volna*), while the main clause takes the present conditional (*most... lennék / tudnám*)."
            },
            {
                "type": "examples",
                "title": "Mixed conditional examples",
                "items": [
                    {"spanish": "Ha akkor megvetted volna a házat, most nem kellene albérletet fizetned.", "english": "If you had bought the house back then, you wouldn't have to pay rent now."},
                    {"spanish": "Ha többet gyakoroltam volna, most sokkal jobban beszélnék magyarul.", "english": "If I had practiced more, I would speak Hungarian much better now."},
                    {"spanish": "Ha nem mulasztotta volna el a határidőt, most már a kezében lenne az engedély.", "english": "If he hadn't missed the deadline, the permit would already be in his hands now."}
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-35-02-a-gr.json", gr_02_a)

    gr_02_b = {
        "id": "grammar.b1.35.02.alternate-scenarios-maskulonben",
        "title": "Alternate Outcomes: Máskülönben, ellenkező esetben",
        "sections": [
            {
                "type": "text",
                "title": "Specifying Alternative Consequences",
                "content": "To introduce what would have occurred had circumstances been otherwise, Hungarian uses *máskülönben* (otherwise), *ellenkező esetben* (in the contrary case), or *másként* (differently), frequently paired with *volna*."
            },
            {
                "type": "examples",
                "title": "Alternate outcome examples",
                "items": [
                    {"spanish": "Szerencsére siettünk, máskülönben lekéstük volna a vonatot.", "english": "Fortunately we hurried; otherwise, we would have missed the train."},
                    {"spanish": "Be kellett avatkozniuk, ellenkező esetben katasztrófa történt volna.", "english": "They had to intervene; in the opposite case, a catastrophe would have occurred."},
                    {"spanish": "Ha másként döntöttünk volna, ma teljesen máshol tartanánk.", "english": "If we had decided differently, we would be in a completely different place today."}
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-35-02-b-gr.json", gr_02_b)

    gr_03_a = {
        "id": "grammar.b1.35.03.expressing-regret-kellett-volna",
        "title": "Expressing Obligation & Regret: Kellett volna + Infinitive",
        "sections": [
            {
                "type": "text",
                "title": "What Should Have Happened",
                "content": "To express past obligation that was unfulfilled ('should have done'), Hungarian uses *kellett volna* governing an infinitive: *El kellett volna mennem* (I should have gone). Negation indicates past mistakes: *Nem kellett volna megvenned* (You shouldn't have bought it)."
            },
            {
                "type": "examples",
                "title": "Regret examples",
                "items": [
                    {"spanish": "Jobban oda kellett volna figyelnem az apró részletekre.", "english": "I should have paid better attention to the fine details."},
                    {"spanish": "Nem kellett volna olyan hevesen reagálnod a megjegyzésére.", "english": "You shouldn't have reacted so heatedly to his remark."},
                    {"spanish": "Már régen meg kellett volna látogatnunk a nagyszüleinket.", "english": "We should have visited our grandparents a long time ago."}
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-35-03-a-gr.json", gr_03_a)

    gr_03_b = {
        "id": "grammar.b1.35.03.missed-opportunities-lehetett-volna",
        "title": "Missed Opportunities: Lehetett volna & Megtehettem volna",
        "sections": [
            {
                "type": "text",
                "title": "What Could Have Been Done",
                "content": "To indicate unrealized possibilities in the past ('could have done / it could have been'), Hungarian pairs potential verbs with *volna*: *lehetett volna* (it could have been), *megtehettem volna* (I could have done it), *segíthettünk volna* (we could have helped)."
            },
            {
                "type": "examples",
                "title": "Missed opportunity examples",
                "items": [
                    {"spanish": "Sokkal szebb is lehetett volna az utazás, ha jobb az idő.", "english": "The journey could have been much nicer if the weather had been better."},
                    {"spanish": "Megtehettem volna, hogy elhallgatom az igazságot, de nem akartam hazudni.", "english": "I could have concealed the truth, but I didn't want to lie."},
                    {"spanish": "Elkerülhettük volna a félreértést egyetlen telefonhívással.", "english": "We could have avoided the misunderstanding with a single phone call."}
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-35-03-b-gr.json", gr_03_b)

    gr_04_a = {
        "id": "grammar.b1.35.04.hypothetical-comparisons-mintha",
        "title": "Hypothetical Comparisons: Mintha... volna",
        "sections": [
            {
                "type": "text",
                "title": "Simulating Alternate Realities",
                "content": "To compare a real experience to a hypothetical scenario ('as if... had happened'), Hungarian uses *mintha* followed by the conditional mood with *volna*."
            },
            {
                "type": "examples",
                "title": "Hypothetical comparison examples",
                "items": [
                    {"spanish": "Úgy viselkedett, mintha semmi sem történt volna.", "english": "He acted as if nothing had happened."},
                    {"spanish": "Olyan csend volt a teremben, mintha mindenki elment volna.", "english": "There was such silence in the room as if everyone had left."},
                    {"spanish": "Úgy örült a sikernek, mintha megnyerte volna a főnyereményt.", "english": "She was as overjoyed at the success as if she had won the grand prize."}
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-35-04-a-gr.json", gr_04_a)

    gr_04_b = {
        "id": "grammar.b1.35.04.speculative-past-modals",
        "title": "Speculating on Alternative Pasts: Feltehetően történt volna",
        "sections": [
            {
                "type": "text",
                "title": "Evaluating Plausible Counterfactuals",
                "content": "When evaluating historical or personal alternatives, Hungarian combines epistemic adverbs with past conditionals: *feltehetően* (presumably), *vélhetően* (plausibly), *valószínűleg* (probably)."
            },
            {
                "type": "examples",
                "title": "Speculative modal examples",
                "items": [
                    {"spanish": "Feltehetően más lett volna a kimenetel, ha felkészültebbek vagyunk.", "english": "Presumably the outcome would have been different if we had been more prepared."},
                    {"spanish": "Vélhetően nem alakult volna ki a válság az új szabályok nélkül.", "english": "Plausibly the crisis would not have developed without the new rules."},
                    {"spanish": "Minden bizonnyal hamarabb végeztünk volna segítség nélkül is.", "english": "Most certainly we would have finished sooner even without help."}
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-35-04-b-gr.json", gr_04_b)

    gr_05_a = {
        "id": "grammar.b1.35.05.retrospective-evaluations",
        "title": "Retrospective Evaluations: Utólag visszagondolva, ha újrakezdhetném",
        "sections": [
            {
                "type": "text",
                "title": "Reflecting on Life Choices",
                "content": "Philosophical reflection on past life decisions employs introductory framing phrases: *utólag visszagondolva* (thinking back in retrospect), *ha újrakezdhetném* (if I could start over), and *mai fejjel már másként csinálnám* (with today's maturity I would do it differently)."
            },
            {
                "type": "examples",
                "title": "Retrospection examples",
                "items": [
                    {"spanish": "Utólag visszagondolva az a kudarc volt életem legfontosabb tanulsága.", "english": "Thinking back in retrospect, that failure was the most important lesson of my life."},
                    {"spanish": "Ha újrakezdhetném a pályámat, ugyanezeket a nehézségeket is vállalnám.", "english": "If I could start my career over, I would take on these same difficulties again."},
                    {"spanish": "Mai fejjel már sokkal türelmesebb lennék a vitákban.", "english": "With today's mindset, I would be much more patient in arguments."}
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-35-05-a-gr.json", gr_05_a)

    gr_05_b = {
        "id": "grammar.b1.35.05.inevitability-and-fate",
        "title": "Inevitability & Acceptance: Úgyis így történt volna",
        "sections": [
            {
                "type": "text",
                "title": "Accepting Unchangeable Realities",
                "content": "To express philosophical closure and the sense that events were destined to unfold as they did, Hungarian uses *úgyis így történt volna* (it would have happened this way anyway) or *elkerülhetetlen lett volna* (it would have been unavoidable)."
            },
            {
                "type": "examples",
                "title": "Inevitability examples",
                "items": [
                    {"spanish": "Felesleges bánkódni: előbb vagy utóbb úgyis kiderült volna az igazság.", "english": "It is pointless to grieve: sooner or later the truth would have come out anyway."},
                    {"spanish": "A szakítás elkerülhetetlen lett volna a nézetkülönbségek miatt.", "english": "The parting would have been unavoidable due to differences in perspective."},
                    {"spanish": "Bármit tettünk volna, a dolgok természete nem változott volna meg.", "english": "Whatever we might have done, the nature of things would not have changed."}
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-35-05-b-gr.json", gr_05_b)

    # -------------------------------------------------------------------------
    # 3. Classic Story: Szerb Antal - Utas és holdvilág (b1-35-szerb.json)
    # -------------------------------------------------------------------------
    story = {
        "id": "story.b1.35.classic",
        "title": "Utas és holdvilág",
        "level": "B1",
        "order": 35,
        "type": "classics",
        "estimatedMinutes": 8,
        "summary": "An adaptation from Antal Szerb's masterpiece 'Utas és holdvilág' (Journey by Moonlight). Mihály, wandering alone through the ancient stone alleys of an Italian hill town beneath the moonlight, is overwhelmed by the memories of his youth in Budapest with Tamás and Éva Ulpius. He reflects on all the paths not taken: what would have happened if he had lived differently, if he had never conformed to bourgeois adulthood, and if the past could ever truly be recovered.",
        "characters": [
            "Mihály",
            "A fogadós"
        ],
        "location": "Gubbio és Umbria hegyei",
        "author": "Szerb Antal",
        "work": "Utas és holdvilág",
        "paragraphs": [
            {
                "type": "narration",
                "text": "A hold ezüstös fénnyel világította meg Gubbio ősi, középkori kőfalait. Mihály lassan sétált a meredek sikátorokban. Egyedül volt Olaszország szívében, hátrahagyva a házasságát, a budapesti polgári élet kényelmét és minden biztos kapaszkodót."
            },
            {
                "type": "dialogue",
                "speaker": "A fogadós",
                "text": "Signore, késő éjszaka van már. A város lakói mind alszanak. Nem fáradt a hosszú vándorlás után?"
            },
            {
                "type": "dialogue",
                "speaker": "Mihály",
                "text": "Nem vagyok fáradt, barátom. Olyan érzés itt sétálni a holdfényben, mintha egy másik életbe tévedtem volna át. Mintha minden kő az elfelejtett ifjúságomról mesélne."
            },
            {
                "type": "narration",
                "text": "Mihály megállt egy kőkorlátnál, és a sötét völgybe nézett. Eszébe jutott Tamás és Éva, a régi budapesti padlásszoba és a titokzatos játékok. Bárcsak soha nem nőttünk volna fel! – gondolta magában."
            },
            {
                "type": "dialogue",
                "speaker": "Mihály",
                "text": "Ha akkor, tizenöt évvel ezelőtt másként döntök, ma nem volnék ilyen magányos. Ha nem engedtem volna a józan családi elvárásoknak, talán megőrizhettem volna a lelkem szabadságát."
            },
            {
                "type": "dialogue",
                "speaker": "A fogadós",
                "text": "A múlt olyan, mint az árnyék a falon: el lehet tőle szaladni, de eltüntetni nem lehet. Talán úgyis ide kellett érkeznie, hogy megértse önmagát."
            },
            {
                "type": "narration",
                "text": "Mihály elmosolyodott a hűvös éjszakában. Tudta, hogy a múltat nem lehet újraélni: ami történt, megtörtént. De amíg az ember él és keresi a válaszokat, addig mindig van lehetőség az újrakezdésre. Az éjszaka csendje lassan megnyugtatta zaklatott szívét."
            }
        ]
    }
    write_json("content/hu/stories/classics/b1/b1-35-szerb.json", story)

    # -------------------------------------------------------------------------
    # 4. Exercise Files (6 files, 7 exercises each = 42 exercises)
    # -------------------------------------------------------------------------
    ex_01 = {
        "lesson": "b1-35-01",
        "exercises": [
            {
                "id": "b1-35-01.ex01",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Hogyan fejezzük ki a múltbeli feltételt a magyarban?",
                "options": [
                    "A múlt idejű igéhez a 'volna' szócskát kapcsoljuk",
                    "A jelen idejű igéhez a '-na/-ne' toldalékot tesszük",
                    "A jövő idő segédigéjét használjuk"
                ],
                "correct": 0
            },
            {
                "id": "b1-35-01.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Ha tudtam volna, eljött_____ volna. (I would have come - em)",
                "answer": "em"
            },
            {
                "id": "b1-35-01.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Bárcsak", "korábban", "szóltál", "volna", "a", "problémáról!"],
                "solution": ["Bárcsak", "korábban", "szóltál", "volna", "a", "problémáról!"]
            },
            {
                "id": "b1-35-01.ex04",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent a 'képzeletbeli' szó?",
                "options": [
                    "A valóságban nem létező, csupán a fantáziában élő dolog",
                    "Egy festőművész által készített rajz",
                    "Egy pontos fényképfelvétel"
                ],
                "correct": 0
            },
            {
                "id": "b1-35-01.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "Ez csupán egy hipotetikus feltételezés, nem pedig valós té_____. (fact - ny)",
                "answer": "ny"
            },
            {
                "id": "b1-35-01.ex06",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik mondat fejez ki elmulasztott múltbeli kívánságot?",
                "options": [
                    "Bárcsak megnéztem volna azt a filmet!",
                    "Bárcsak megnézem a filmet holnap!",
                    "Mindig megnézem a filmeket moziban."
                ],
                "correct": 0
            },
            {
                "id": "b1-35-01.ex07",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["Minden", "lehetőséget", "alaposan", "meg", "kellett", "fontolni."],
                "solution": ["Minden", "lehetőséget", "alaposan", "meg", "kellett", "fontolni."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-35-01-ex.json", ex_01)

    ex_02 = {
        "lesson": "b1-35-02",
        "exercises": [
            {
                "id": "b1-35-02.ex01",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik mondat kapcsolja a múltbeli feltételt a jelenbeli eredményhez (vegyes feltétel)?",
                "options": [
                    "Ha akkor többet tanultál volna, most nem aggódnál a vizsga miatt.",
                    "Ha holnap esik, otthon maradunk.",
                    "Ha tegnap esett, nem mentünk sétálni."
                ],
                "correct": 0
            },
            {
                "id": "b1-35-02.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Időben indultunk, máskülönben lekést_____ volna a gépet. (we would have missed - ük)",
                "answer": "ük"
            },
            {
                "id": "b1-35-02.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Ha", "másként", "döntöttünk", "volna,", "más", "lenne", "az", "életünk."],
                "solution": ["Ha", "másként", "döntöttünk", "volna,", "más", "lenne", "az", "életünk."]
            },
            {
                "id": "b1-35-02.ex04",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent a 'fordulat' a történetmesélésben?",
                "options": [
                    "Váratlan, döntő változás az események menetében",
                    "A gépkocsi kerekének megfordulása",
                    "A könyv lapjainak számozása"
                ],
                "correct": 0
            },
            {
                "id": "b1-35-02.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "Jelentős eltérés mutatkozott a két beszámoló köz_____. (between - ött)",
                "answer": "ött"
            },
            {
                "id": "b1-35-02.ex06",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Hogyan mondjuk másképp, hogy 'ellenkező esetben'?",
                "options": [
                    "Máskülönben",
                    "Ugyanakkor",
                    "Következésképpen"
                ],
                "correct": 0
            },
            {
                "id": "b1-35-02.ex07",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "váratlan", "fordulat", "megváltoztatta", "a", "terveket."],
                "solution": ["A", "váratlan", "fordulat", "megváltoztatta", "a", "terveket."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-35-02-ex.json", ex_02)

    ex_03 = {
        "lesson": "b1-35-03",
        "exercises": [
            {
                "id": "b1-35-03.ex01",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Hogyan fejezzük ki a múltbeli mulasztást: 'I should have called you'?",
                "options": [
                    "Fel kellett volna hívnom téged",
                    "Fel kellene hívnom téged",
                    "Felhívtalak volna téged"
                ],
                "correct": 0
            },
            {
                "id": "b1-35-03.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Nem kellett volna olyan sokat vitatkoz_____ velük. (to argue - nod)",
                "answer": "nod"
            },
            {
                "id": "b1-35-03.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Megtehettem", "volna,", "de", "mégsem", "tettem", "meg."],
                "solution": ["Megtehettem", "volna,", "de", "mégsem", "tettem", "meg."]
            },
            {
                "id": "b1-35-03.ex04",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent az 'utólag' kifejezés?",
                "options": [
                    "Az események lezajlása után, visszatekintve",
                    "Közvetlenül a kezdés előtt",
                    "Egyidejűleg a cselekvéssel"
                ],
                "correct": 0
            },
            {
                "id": "b1-35-03.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "Kárba vesz_____ minden fáradozásunk a rossz idő miatt. (went to waste - ett)",
                "answer": "ett"
            },
            {
                "id": "b1-35-03.ex06",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit fejez ki a 'mulasztás'?",
                "options": [
                    "Egy kötelesség vagy lehetőség elmulasztását",
                    "Egy szórakoztató mulatságot a faluban",
                    "A munkaidő lejártát"
                ],
                "correct": 0
            },
            {
                "id": "b1-35-03.ex07",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["Utólag", "már", "könnyű", "okosnak", "lenni."],
                "solution": ["Utólag", "már", "könnyű", "okosnak", "lenni."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-35-03-ex.json", ex_03)

    ex_04 = {
        "lesson": "b1-35-04",
        "exercises": [
            {
                "id": "b1-35-04.ex01",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Hogyan képezzük a képzeletbeli hasonlítást ('as if... had happened')?",
                "options": [
                    "A 'mintha' kötőszóval és a múlt idejű ige + volna szerkezettel",
                    "A 'minthogy' szóval és jövő idővel",
                    "A 'mint' szóval és jelen idővel"
                ],
                "correct": 0
            },
            {
                "id": "b1-35-04.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Úgy viselkedett, mintha semmi sem történ_____ volna. (had happened - t)",
                "answer": "t"
            },
            {
                "id": "b1-35-04.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Feltehetően", "más", "lett", "volna", "a", "kimenetel."],
                "solution": ["Feltehetően", "más", "lett", "volna", "a", "kimenetel."]
            },
            {
                "id": "b1-35-04.ex04",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent az 'eshetőség' egy döntési helyzetben?",
                "options": [
                    "Egy lehetséges forgatókönyv vagy jövőbeli lehetőség",
                    "Az őszi falevelek lehullása",
                    "A pénzügyi veszteség biztos bekövetkezése"
                ],
                "correct": 0
            },
            {
                "id": "b1-35-04.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "Minden lehetséges forgatókönyv_____ fel kell készülnünk. (scenario - re)",
                "answer": "re"
            },
            {
                "id": "b1-35-04.ex06",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Mit fejez ki a 'vélhetően' szó?",
                "options": [
                    "Valószínűleg, a rendelkezésre álló adatok alapján",
                    "Teljesen kizárt módon",
                    "Véletlenül és váratlanul"
                ],
                "correct": 0
            },
            {
                "id": "b1-35-04.ex07",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "kockázatot", "mindig", "időben", "fel", "kell", "mérni."],
                "solution": ["A", "kockázatot", "mindig", "időben", "fel", "kell", "mérni."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-35-04-ex.json", ex_04)

    ex_05 = {
        "lesson": "b1-35-05",
        "exercises": [
            {
                "id": "b1-35-05.ex01",
                "type": "multiple-choice",
                "category": "literature",
                "question": "Hol sétál Mihály a holdfényben Szerb Antal Utas és holdvilág című regényében?",
                "options": [
                    "Gubbio olasz középkori sikátoraiban",
                    "A londoni parlament előtti hídon",
                    "A szegedi dóm téren"
                ],
                "correct": 0
            },
            {
                "id": "b1-35-05.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Utólag visszagondolva a nehézségek ellenére hasznos vo_____ az út. (was - lt)",
                "answer": "lt"
            },
            {
                "id": "b1-35-05.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Úgyis", "így", "történt", "volna", "minden", "előbb-utóbb."],
                "solution": ["Úgyis", "így", "történt", "volna", "minden", "előbb-utóbb."]
            },
            {
                "id": "b1-35-05.ex04",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent a 'nosztalgia'?",
                "options": [
                    "Vágyakozó, édes-bús emlékezés a múltra és az ifjúságra",
                    "Egy hirtelen fellépő szívbetegség",
                    "Az utazási irodák kedvezményes ajánlata"
                ],
                "correct": 0
            },
            {
                "id": "b1-35-05.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "Ez egy sorsfordí_____ pillanat volt az életemben. (fate-altering - tó)",
                "answer": "tó"
            },
            {
                "id": "b1-35-05.ex06",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Hogyan mondjuk: 'With today's mindset I would do it differently'?",
                "options": [
                    "Mai fejjel már másként csinálnám",
                    "Ma este megcsinálom a feladatot",
                    "Fejjel lefelé csinálom a munkát"
                ],
                "correct": 0
            },
            {
                "id": "b1-35-05.ex07",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "visszatekintés", "segít", "megérteni", "a", "döntéseinket."],
                "solution": ["A", "visszatekintés", "segít", "megérteni", "a", "döntéseinket."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-35-05-ex.json", ex_05)

    ex_consolidation = {
        "lesson": "b1-35-consolidation",
        "exercises": [
            {
                "id": "b1-35-consolidation.ex01",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik mondat fejez ki elmulasztott múltbeli lehetőséget helyesen?",
                "options": [
                    "Ha időben szóltál volna, segítettünk volna.",
                    "Ha időben szólsz, segíteni fogunk.",
                    "Ha szóltál, segítettünk volna tegnapelőtt."
                ],
                "correct": 0
            },
            {
                "id": "b1-35-consolidation.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Bárcsak több időm le_____ volna a felkészülésre! (had been - tt)",
                "answer": "tt"
            },
            {
                "id": "b1-35-consolidation.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["El", "kellett", "volna", "indulnunk", "még", "naplemente", "előtt."],
                "solution": ["El", "kellett", "volna", "indulnunk", "még", "naplemente", "előtt."]
            },
            {
                "id": "b1-35-consolidation.ex04",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent a 'kárba veszett' kifejezés?",
                "options": [
                    "Haszontalanná vált, hiábavalóvá lett valami",
                    "Kártérítést fizettek utána a bíróságon",
                    "Elveszett az erdő mélyén egy kiránduláson"
                ],
                "correct": 0
            },
            {
                "id": "b1-35-consolidation.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A nehéz helyzetben váratlan fordulat áll_____ be. (occurred - t)",
                "answer": "t"
            },
            {
                "id": "b1-35-consolidation.ex06",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Hogyan folytatódik a mondat: 'Úgy nézett rám, mintha...'?",
                "options": [
                    "...soha nem látott volna korábban.",
                    "...soha nem lát engem tegnap.",
                    "...holnap látni fog engem."
                ],
                "correct": 0
            },
            {
                "id": "b1-35-consolidation.ex07",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["Utólag", "visszagondolva", "helyes", "volt", "a", "választásunk."],
                "solution": ["Utólag", "visszagondolva", "helyes", "volt", "a", "választásunk."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-35-consolidation-ex.json", ex_consolidation)

    # -------------------------------------------------------------------------
    # 5. Lesson Files (6 files)
    # -------------------------------------------------------------------------
    lesson_01 = {
        "id": "lesson.b1.35-01",
        "unit": 35,
        "title": "Ha másként lett volna... (The Past Conditional)",
        "level": "B1",
        "grammar": "The Past Conditional in -tt volna & Irreal Wishes with Bárcsak",
        "sections": [
            {
                "type": "goal",
                "title": "Lesson Goals",
                "items": [
                    "I can form past counterfactual conditions using past tense verbs plus volna.",
                    "I can voice heartfelt past wishes using Bárcsak... volna!",
                    "I can learn 4 words for hypotheses, possibilities, and conceptions.",
                    "I can imagine alternative scenarios that could have occurred in the past."
                ]
            },
            {"type": "recycle", "count": 3},
            {"type": "vocabulary", "ref": "vocabulary/b1/b1-35-01-voc.json"},
            {"type": "grammar", "ref": "grammar/b1/b1-35-01-a-gr.json"},
            {"type": "grammar", "ref": "grammar/b1/b1-35-01-b-gr.json"},
            {
                "type": "exercise-group",
                "title": "Practice",
                "ref": "exercises/b1/b1-35-01-ex.json",
                "exerciseRefs": [
                    "b1-35-01.ex01",
                    "b1-35-01.ex02",
                    "b1-35-01.ex03",
                    "b1-35-01.ex04",
                    "b1-35-01.ex05",
                    "b1-35-01.ex06",
                    "b1-35-01.ex07"
                ]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-35-01.json", lesson_01)

    lesson_02 = {
        "id": "lesson.b1.35-02",
        "unit": 35,
        "title": "Amit tettem volna (What I Would Have Done)",
        "level": "B1",
        "grammar": "Mixed Conditionals (Past Condition -> Present Result) & Máskülönben",
        "sections": [
            {
                "type": "goal",
                "title": "Lesson Goals",
                "items": [
                    "I can connect past counterfactual actions to present outcomes in mixed conditionals.",
                    "I can state alternative outcomes using máskülönben and ellenkező esetben.",
                    "I can use 4 terms for divergence, turns of events, and alternatives.",
                    "I can discuss how past choices shape our present circumstances."
                ]
            },
            {"type": "recycle", "count": 3},
            {"type": "vocabulary", "ref": "vocabulary/b1/b1-35-02-voc.json"},
            {"type": "grammar", "ref": "grammar/b1/b1-35-02-a-gr.json"},
            {"type": "grammar", "ref": "grammar/b1/b1-35-02-b-gr.json"},
            {
                "type": "exercise-group",
                "title": "Practice",
                "ref": "exercises/b1/b1-35-02-ex.json",
                "exerciseRefs": [
                    "b1-35-02.ex01",
                    "b1-35-02.ex02",
                    "b1-35-02.ex03",
                    "b1-35-02.ex04",
                    "b1-35-02.ex05",
                    "b1-35-02.ex06",
                    "b1-35-02.ex07"
                ]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-35-02.json", lesson_02)

    lesson_03 = {
        "id": "lesson.b1.35-03",
        "unit": 35,
        "title": "Megbánás és mulasztás (Regrets & What-Ifs)",
        "level": "B1",
        "grammar": "Kellett volna / Nem kellett volna & Missed Opportunities with Lehetett volna",
        "sections": [
            {
                "type": "goal",
                "title": "Lesson Goals",
                "items": [
                    "I can express unfulfilled past obligations using kellett volna.",
                    "I can discuss missed opportunities with lehetett volna and megtehettem volna.",
                    "I can acquire 4 vocabulary terms for remorse, omissions, and hindsight.",
                    "I can evaluate past actions constructively and state what should have been done."
                ]
            },
            {"type": "recycle", "count": 3},
            {"type": "vocabulary", "ref": "vocabulary/b1/b1-35-03-voc.json"},
            {"type": "grammar", "ref": "grammar/b1/b1-35-03-a-gr.json"},
            {"type": "grammar", "ref": "grammar/b1/b1-35-03-b-gr.json"},
            {
                "type": "exercise-group",
                "title": "Practice",
                "ref": "exercises/b1/b1-35-03-ex.json",
                "exerciseRefs": [
                    "b1-35-03.ex01",
                    "b1-35-03.ex02",
                    "b1-35-03.ex03",
                    "b1-35-03.ex04",
                    "b1-35-03.ex05",
                    "b1-35-03.ex06",
                    "b1-35-03.ex07"
                ]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-35-03.json", lesson_03)

    lesson_04 = {
        "id": "lesson.b1.35-04",
        "unit": 35,
        "title": "Eltérő forgatókönyvek (An Alternate Version of Events)",
        "level": "B1",
        "grammar": "Hypothetical Comparisons with Mintha... volna & Speculative Past Modals",
        "sections": [
            {
                "type": "goal",
                "title": "Lesson Goals",
                "items": [
                    "I can draw hypothetical comparisons using mintha... volna.",
                    "I can speculate on alternative scenarios using feltehetően and vélhetően.",
                    "I can master 4 words for contingencies, scripts, and outcomes.",
                    "I can analyze counterfactual scenarios in historical and personal contexts."
                ]
            },
            {"type": "recycle", "count": 3},
            {"type": "vocabulary", "ref": "vocabulary/b1/b1-35-04-voc.json"},
            {"type": "grammar", "ref": "grammar/b1/b1-35-04-a-gr.json"},
            {"type": "grammar", "ref": "grammar/b1/b1-35-04-b-gr.json"},
            {
                "type": "exercise-group",
                "title": "Practice",
                "ref": "exercises/b1/b1-35-04-ex.json",
                "exerciseRefs": [
                    "b1-35-04.ex01",
                    "b1-35-04.ex02",
                    "b1-35-04.ex03",
                    "b1-35-04.ex04",
                    "b1-35-04.ex05",
                    "b1-35-04.ex06",
                    "b1-35-04.ex07"
                ]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-35-04.json", lesson_04)

    lesson_05 = {
        "id": "lesson.b1.35-05",
        "unit": 35,
        "title": "Nosztalgia és más utak (Imagining a Different Past: Szerb Antal)",
        "level": "B1",
        "grammar": "Retrospective Evaluations (Utólag visszagondolva) & Acceptance of Fate",
        "sections": [
            {
                "type": "goal",
                "title": "Lesson Goals",
                "items": [
                    "I can articulate retrospective life evaluations using utólag visszagondolva.",
                    "I can express philosophical closure with úgyis így történt volna.",
                    "I can learn 4 words for nostalgia, life choices, and destiny.",
                    "I can read and analyze an adaptation of Szerb Antal's classic Utas és holdvilág."
                ]
            },
            {"type": "recycle", "count": 3},
            {"type": "vocabulary", "ref": "vocabulary/b1/b1-35-05-voc.json"},
            {"type": "grammar", "ref": "grammar/b1/b1-35-05-a-gr.json"},
            {"type": "grammar", "ref": "grammar/b1/b1-35-05-b-gr.json"},
            {"type": "story", "ref": "stories/classics/b1/b1-35-szerb.json"},
            {
                "type": "exercise-group",
                "title": "Practice",
                "ref": "exercises/b1/b1-35-05-ex.json",
                "exerciseRefs": [
                    "b1-35-05.ex01",
                    "b1-35-05.ex02",
                    "b1-35-05.ex03",
                    "b1-35-05.ex04",
                    "b1-35-05.ex05",
                    "b1-35-05.ex06",
                    "b1-35-05.ex07"
                ]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-35-05.json", lesson_05)

    lesson_consolidation = {
        "id": "lesson.b1.35-consolidation",
        "unit": 35,
        "title": "Összegzés és gyakorlás: Feltételezések és lehetőségek (Consolidation)",
        "level": "B1",
        "grammar": "Review of the past conditional, mixed conditionals, regrets, and hypothetical comparison",
        "sections": [
            {
                "type": "goal",
                "title": "Consolidation Goals",
                "items": [
                    "Review all 20 vocabulary words for hypotheses, regrets, and alternative possibilities.",
                    "Synthesize the past conditional (-tt volna), missed duty (kellett volna), and mintha... volna.",
                    "Demonstrate mastery of discussing alternate pasts and counterfactual scenarios.",
                    "Prepare for independent language mastery in the final B1 capstone unit."
                ]
            },
            {
                "type": "exercise-group",
                "title": "Consolidation Practice",
                "ref": "exercises/b1/b1-35-consolidation-ex.json",
                "exerciseRefs": [
                    "b1-35-consolidation.ex01",
                    "b1-35-consolidation.ex02",
                    "b1-35-consolidation.ex03",
                    "b1-35-consolidation.ex04",
                    "b1-35-consolidation.ex05",
                    "b1-35-consolidation.ex06",
                    "b1-35-consolidation.ex07"
                ]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-35-consolidation.json", lesson_consolidation)

if __name__ == "__main__":
    build_unit_35_core()
