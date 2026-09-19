#!/usr/bin/env python3
"""Generate Hungarian B1 Core Unit 13: Media & Information (b1-13)."""

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

def build_unit_13_core():
    # -------------------------------------------------------------------------
    # 1. Vocabulary Files (4 words each = 20 words total)
    # -------------------------------------------------------------------------
    voc_01 = {
        "id": "vocab.b1.13.01",
        "lesson": "b1-13-01",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "híradás", "translation": "news report, broadcast", "pos": "noun"},
            {"lemma": "hírforrás", "translation": "news source", "pos": "noun"},
            {"lemma": "tudósító", "translation": "reporter, correspondent", "pos": "noun"},
            {"lemma": "főcím", "translation": "headline", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-13-01-voc.json", voc_01)

    voc_02 = {
        "id": "vocab.b1.13.02",
        "lesson": "b1-13-02",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "nyilatkozat", "translation": "statement, declaration", "pos": "noun"},
            {"lemma": "állítás", "translation": "claim, assertion", "pos": "noun"},
            {"lemma": "szóvivő", "translation": "spokesperson", "pos": "noun"},
            {"lemma": "közlemény", "translation": "announcement, official release", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-13-02-voc.json", voc_02)

    voc_03 = {
        "id": "vocab.b1.13.03",
        "lesson": "b1-13-03",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "híresztelés", "translation": "rumor, hearsay", "pos": "noun"},
            {"lemma": "álhír", "translation": "fake news, hoax", "pos": "noun"},
            {"lemma": "megbízhatóság", "translation": "reliability, trustworthiness", "pos": "noun"},
            {"lemma": "tényellenőrzés", "translation": "fact-checking", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-13-03-voc.json", voc_03)

    voc_04 = {
        "id": "vocab.b1.13.04",
        "lesson": "b1-13-04",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "riport", "translation": "report, feature story", "pos": "noun"},
            {"lemma": "interjúalany", "translation": "interviewee", "pos": "noun"},
            {"lemma": "közvélemény", "translation": "public opinion", "pos": "noun"},
            {"lemma": "nyomozás", "translation": "investigation, investigative reporting", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-13-04-voc.json", voc_04)

    voc_05 = {
        "id": "vocab.b1.13.05",
        "lesson": "b1-13-05",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "összegzés", "translation": "summary, synthesis", "pos": "noun"},
            {"lemma": "álláspont", "translation": "standpoint, point of view", "pos": "noun"},
            {"lemma": "véleménycikk", "translation": "opinion piece, op-ed", "pos": "noun"},
            {"lemma": "tanulság", "translation": "lesson, moral takeaway", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-13-05-voc.json", voc_05)

    # -------------------------------------------------------------------------
    # 2. Grammar Files
    # -------------------------------------------------------------------------
    gr_01_a = {
        "id": "grammar.b1.13.01.reported-speech-statements",
        "title": "Reported Speech in News: azt mondta, hogy... and Tense Retention",
        "sections": [
            {
                "type": "text",
                "title": "Retaining Original Tense in Hungarian Indirect Speech",
                "content": "Unlike English backshifting, Hungarian reported speech generally keeps the original tense of the speaker: *A tudósító azt mondta, hogy a tárgyalások ma kezdődnek* ('The reporter said that the negotiations [start / were starting] today'). The introductory clause commonly uses *azt mondta / jelentette ki / közölte, hogy...*."
            },
            {
                "type": "examples",
                "title": "Reported statements in news",
                "items": [
                    {
                        "spanish": "A riporter azt mondta, hogy a miniszter hamarosan megérkezik.",
                        "english": "The reporter said that the minister would arrive soon."
                    },
                    {
                        "spanish": "A cikk szerzője kijelentette, hogy a hírek megbízható forrásból származnak.",
                        "english": "The author of the article stated that the news came from a reliable source."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-13-01-a-gr.json", gr_01_a)

    gr_01_b = {
        "id": "grammar.b1.13.01.attributive-reporting",
        "title": "Attributive Quotations: a hírek szerint, a szóvivő szerint",
        "sections": [
            {
                "type": "text",
                "title": "Using 'szerint' for Attribution",
                "content": "Journalistic register relies heavily on *szerint* ('according to'): *a hírek szerint* (according to the news), *a rendőrség szerint* (according to the police), *a szóvivő állítása szerint* (according to the spokesperson's assertion)."
            },
            {
                "type": "examples",
                "title": "Examples with szerint",
                "items": [
                    {
                        "spanish": "A hivatalos közlemény szerint a helyzet már stabil.",
                        "english": "According to the official release, the situation is already stable."
                    },
                    {
                        "spanish": "A szemtanúk szerint a baleset reggel nyolc órakor történt.",
                        "english": "According to eyewitnesses, the accident happened at eight in the morning."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-13-01-b-gr.json", gr_01_b)

    gr_02_a = {
        "id": "grammar.b1.13.02.indirect-questions",
        "title": "Indirect Questions in Reporting: azt kérdezte, hogy... -e",
        "sections": [
            {
                "type": "text",
                "title": "Embedded Yes/No and Wh- Questions",
                "content": "Reported yes/no questions take the interrogative clitic *-e*: *A riporter azt kérdezte, hogy megérkezett-e a segély.* Wh-questions embed the interrogative pronoun directly: *Azt kérdezte, hogy mikor kezdődik a sajtótájékoztató.*"
            },
            {
                "type": "examples",
                "title": "Examples of reported questions",
                "items": [
                    {
                        "spanish": "Megkérdezték a szóvivőt, hogy igaz-e a tegnapi állítás.",
                        "english": "They asked the spokesperson whether yesterday's assertion was true."
                    },
                    {
                        "spanish": "A szerkesztő arról érdeklődött, hogy mikor készül el a teljes riport.",
                        "english": "The editor inquired about when the full report would be ready."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-13-02-a-gr.json", gr_02_a)

    gr_02_b = {
        "id": "grammar.b1.13.02.reporting-verbs",
        "title": "Nuanced Reporting Verbs: hangsúlyoz, állít, cáfol, megerősít",
        "sections": [
            {
                "type": "text",
                "title": "Beyond 'mond': Nuanced Verbs of Communication",
                "content": "Quality journalism uses specific verbs of attribution: *állít* (claims), *cáfol* (refutes), *megerősít* (confirms), *hangsúlyoz* (emphasizes), *hozzáfűz* (adds/remarks)."
            },
            {
                "type": "examples",
                "title": "Attribution verbs in action",
                "items": [
                    {
                        "spanish": "A hatóság határozottan cáfolta a közösségi médiában terjedő pletykákat.",
                        "english": "The authority firmly refuted the rumors spreading on social media."
                    },
                    {
                        "spanish": "A szóvivő megerősítette, hogy újabb vizsgálat indul az ügyben.",
                        "english": "The spokesperson confirmed that a new inquiry would be launched into the case."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-13-02-b-gr.json", gr_02_b)

    gr_03_a = {
        "id": "grammar.b1.13.03.epistemic-doubt",
        "title": "Expressing Doubt & Verification: úgy tűnik, állítólag, kétséges",
        "sections": [
            {
                "type": "text",
                "title": "Epistemic Markers in Fact-Checking",
                "content": "To distance oneself from unverified claims, use evidential adverbs and clauses: *állítólag* (allegedly), *úgy tűnik, hogy...* (it seems that...), *kétséges, hogy...* (it is doubtful whether...), *nem zárható ki, hogy...* (it cannot be ruled out that...)."
            },
            {
                "type": "examples",
                "title": "Distancing and checking expressions",
                "items": [
                    {
                        "spanish": "Az interneten terjedő hír állítólag egy névtelen forrásból származik.",
                        "english": "The news circulating on the internet allegedly originates from an anonymous source."
                    },
                    {
                        "spanish": "Kétséges, hogy a videó felvétele valódi vagy manipulált.",
                        "english": "It is doubtful whether the video recording is genuine or manipulated."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-13-03-a-gr.json", gr_03_a)

    gr_03_b = {
        "id": "grammar.b1.13.03.evaluating-credibility",
        "title": "Adjectival Modifiers of Credibility: megbízható, hiteles, kétes",
        "sections": [
            {
                "type": "text",
                "title": "Describing Information Quality",
                "content": "Common evaluative pairs include *hiteles hírforrás* (authentic/credible news source), *megbízható adat* (reliable data), *kétes híresztelés* (dubious rumor), *megalapozott vélemény* (well-founded opinion)."
            },
            {
                "type": "examples",
                "title": "Evaluating credibility",
                "items": [
                    {
                        "spanish": "A tudatos olvasó mindig ellenőrzi, hogy hiteles-e a forrás.",
                        "english": "A conscious reader always checks whether the source is credible."
                    },
                    {
                        "spanish": "A tényellenőrző csoport bebizonyította, hogy a fénykép hamisítvány volt.",
                        "english": "The fact-checking team proved that the photograph was a fake."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-13-03-b-gr.json", gr_03_b)

    gr_04_a = {
        "id": "grammar.b1.13.04.narrating-investigations",
        "title": "Narrating Journalistic Inquiries: miután kiderült, kiderül, fény derül",
        "sections": [
            {
                "type": "text",
                "title": "Idiomatic Expressions of Discovery",
                "content": "Investigative reports use characteristic expressions: *fény derül valamire* (light is shed on something / comes to light), *kiderül, hogy...* (it turns out that...), *nyomozást folytat* (conducts an investigation)."
            },
            {
                "type": "examples",
                "title": "Discovery idioms",
                "items": [
                    {
                        "spanish": "A hetekig tartó újságírói nyomozás során fény derült a titkos adatokra.",
                        "english": "During the weeks-long journalistic investigation, light was shed on the secret data."
                    },
                    {
                        "spanish": "Gyorsan kiderült, hogy a hír mögött szervezett kampány állt.",
                        "english": "It quickly turned out that an organized campaign was behind the news."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-13-04-a-gr.json", gr_04_a)

    gr_04_b = {
        "id": "grammar.b1.13.04.temporal-sequencing-news",
        "title": "Temporal Sequencing in News: azt követően, hogy / amint / időközben",
        "sections": [
            {
                "type": "text",
                "title": "Sequencing Complex Events",
                "content": "Advanced news narration relies on formal connectors: *azt követően, hogy...* (following the fact that...), *időközben* (in the meantime), *amint nyilvánosságra került* (as soon as it became public)."
            },
            {
                "type": "examples",
                "title": "Sequencing examples",
                "items": [
                    {
                        "spanish": "Azt követően, hogy a nyilatkozat megjelent, a közvélemény megnyugodott.",
                        "english": "Following the release of the statement, public opinion settled down."
                    },
                    {
                        "spanish": "Időközben a rendőrség befejezte a helyszíni vizsgálatot.",
                        "english": "In the meantime, the police concluded the on-site investigation."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-13-04-b-gr.json", gr_04_b)

    gr_05_a = {
        "id": "grammar.b1.13.05.synthesizing-opinions",
        "title": "Structuring Op-Eds & Syntheses: egyfelől... másfelől, mindent összevetve",
        "sections": [
            {
                "type": "text",
                "title": "Balance and Concluding Discourse Markers",
                "content": "Opinion columns balance perspectives using correlatives: *egyfelől... másfelől...* (on the one hand... on the other hand), *mindent összevetve* (all things considered), *összegzésként elmondható, hogy...* (in summary, it can be said that...)."
            },
            {
                "type": "examples",
                "title": "Synthesis discourse markers",
                "items": [
                    {
                        "spanish": "Egyfelől a digitális hírek gyorsak, másfelől sok a pontatlan információ.",
                        "english": "On the one hand digital news is fast; on the other hand there is much inaccurate information."
                    },
                    {
                        "spanish": "Mindent összevetve a média felelőssége ma nagyobb, mint valaha.",
                        "english": "All things considered, the responsibility of the media today is greater than ever."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-13-05-a-gr.json", gr_05_a)

    gr_05_b = {
        "id": "grammar.b1.13.05.concluding-lessons",
        "title": "Drawing Conclusions & Lessons: a tanulság az, hogy... / végeredményben",
        "sections": [
            {
                "type": "text",
                "title": "Expressing Takeaways",
                "content": "To conclude a journalistic piece or essay, state the main takeaway: *A legfontosabb tanulság az, hogy mindig több forrásból kell tájékozódni.* (*The most important takeaway is that one must always gather information from multiple sources.*)"
            },
            {
                "type": "examples",
                "title": "Drawing conclusions",
                "items": [
                    {
                        "spanish": "Végeredményben a kritikus gondolkodás a legjobb védelem az álhírek ellen.",
                        "english": "In the end, critical thinking is the best defense against fake news."
                    },
                    {
                        "spanish": "A cikk tanulsága szerint a gyorsaság nem mehet a pontosság rovására.",
                        "english": "According to the article's takeaway, speed must not come at the expense of accuracy."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-13-05-b-gr.json", gr_05_b)

    # -------------------------------------------------------------------------
    # 3. Classic Literature Story: Molnár Ferenc: A Pál utcai fiúk
    # -------------------------------------------------------------------------
    classic_story = {
        "id": "story.b1.13.classic",
        "title": "A vörösingesek követe és a kiáltvány a grundon",
        "level": "B1",
        "order": 13,
        "type": "classics",
        "estimatedMinutes": 7,
        "summary": "An adaptation from Ferenc Molnár's immortal classic novel 'A Pál utcai fiúk'. On the Paul Street playground, Boka and his friends receive startling news: the rival Redshirts intend to conquer their lot. Boka drafts an official proclamation and posts it for everyone to read.",
        "characters": ["Boka János", "Nemecsek Ernő", "Geréb Dezső", "Csónakos"],
        "location": "Budapest, Pál utcai grund",
        "author": "Molnár Ferenc",
        "work": "A Pál utcai fiúk",
        "historicalContext": "Published in 1906, Ferenc Molnár's novel is the most famous Hungarian youth classic in world literature. It dramatizes childhood honor, democracy, camaraderie, and self-sacrifice amid the rapidly expanding tenements of turn-of-the-century Budapest.",
        "readingQuestions": [
            {
                "question": "Milyen rendkívüli hírt hozott Csónakos és Nemecsek a grundra?",
                "options": [
                    "Azt a hírt hozták, hogy a vörösingesek el akarják foglalni a Pál utcai grundot.",
                    "Azt jelentették, hogy a tanár úr bezáratta az iskola kapuját.",
                    "Azt mondták, hogy új házat kezdenek építeni a faárutelepen."
                ],
                "correct": 0,
                "explanation": "Nemecsek és Csónakos azzal a hírrel érkeztek a grundra, hogy a füvészkerti vörösingesek hadjáratot terveznek a terület megszerzésére."
            },
            {
                "question": "Mit tett Boka János, miután meghallgatta a riasztó beszámolót?",
                "options": [
                    "Kétségbeesett és feladta a küzdelmet.",
                    "Hivatalos kiáltványt fogalmazott meg, és kifüggesztette a palánkra.",
                    "Azonnal elszaladt a rendőrségre segítségért."
                ],
                "correct": 1,
                "explanation": "Boka János mint elnök írásos hadparancsot és kiáltványt szerkesztett, amelyben fegyelemre és összetartásra szólította fel a fiúkat."
            },
            {
                "question": "Hogyan fogadták a grund védői Boka határozott kiáltványát?",
                "options": [
                    "Csendben és elszánt figyelemmel hallgatták az elnök szavait, és elfogadták a haditervet.",
                    "Kinevették a kis Nemecseket és hazamentek tanulni.",
                    "Megtagadták a parancs teljesítését a délutáni játék miatt."
                ],
                "correct": 0,
                "explanation": "A fiúk fegyelmezetten felsorakoztak, egyhangúlag elfogadták Boka rendelkezéseit, és készen álltak a grund megvédésére."
            }
        ],
        "paragraphs": [
            {
                "type": "narration",
                "text": "A Pál utcai grundon a délutáni napsütésben békésen száradt a farakások friss fűrészporos illata. Ám a kapun hirtelen lihegve rontott be Csónakos és a kis közlegény, Nemecsek Ernő."
            },
            {
                "type": "dialogue",
                "speaker": "Csónakos",
                "text": "Boka! Fontos híradás érkezett a Füvészkertből! A vörösingesek vezére, Áts Feri kijelentette, hogy eljönnek és elfoglalják a birodalmunkat!"
            },
            {
                "type": "narration",
                "text": "Boka János komoly arccal hallgatta a hírt. Nemecsek megerősítette a beszámolót, mondván, hogy saját szemével látta a vörösingesek készülődését a szigeten."
            },
            {
                "type": "dialogue",
                "speaker": "Boka János",
                "text": "Nyugalom, fiúk! A pánik a legrosszabb tanácsadó. Nem hagyjuk, hogy elvegyék a hazánkat. Most azonnal kiáltványt és hadi szabályzatot szerkesztek!"
            },
            {
                "type": "narration",
                "text": "Boka leült a kunyhó melletti ládára, elővette a noteszét, és tiszta, határozott betűkkel megfogalmazta az üzenetet. A kiáltványban felszólított minden tisztet és közlegényt a fegyelemre és a hűségre."
            },
            {
                "type": "narration",
                "text": "Miután a kiáltvány elkészült, Nemecsek büszkén felszegezte a nagy fapalánkra. A fiúk köré gyűltek, és Boka felolvasta az írást: a grundért mindenki harcolni fog az utolsó leheletéig."
            },
            {
                "type": "dialogue",
                "speaker": "Nemecsek Ernő",
                "text": "Én is ott leszek az első sorban, Boka! Bár csak közlegény vagyok, a grundot én is tiszta szívből szeretem!"
            },
            {
                "type": "narration",
                "text": "A bátor kis csapat egy emberként zúgta a választ. A hír igaznak bizonyult, a veszély óriási volt, de a Pál utcai fiúk szívében nem volt helye a félelemnek."
            }
        ]
    }
    write_json("content/hu/stories/classics/b1/b1-13-palutcaifiuk.json", classic_story)

    # -------------------------------------------------------------------------
    # 4. Exercises Files (01 to 05 + consolidation)
    # -------------------------------------------------------------------------
    ex_01 = {
        "lesson": "b1-13-01",
        "exercises": [
            {
                "id": "b1-13-01.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["híradás", "news report / broadcast"],
                    ["hírforrás", "news source"],
                    ["tudósító", "reporter / correspondent"],
                    ["főcím", "headline"]
                ]
            },
            {
                "id": "b1-13-01.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Hogyan mondjuk helyesen közvetett beszédben: 'A tudósító azt mondta, hogy...'?",
                "options": [
                    "A tudósító azt mondta, hogy a miniszter most érkezik meg.",
                    "A tudósító azt mondta, hogy a miniszter tegnapelőtt érkezett volna meg volt.",
                    "A tudósító azt mondta, hogy a miniszter fog megérkezni legyen."
                ],
                "correct": 0
            },
            {
                "id": "b1-13-01.ex03",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "Az újságíró nem árulta el, hogy ki volt a titkos ____ a cikkhez. (source of news)",
                "answer": "hírforrás"
            },
            {
                "id": "b1-13-01.ex04",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A rendőrségi közlemény ____ a balesetben senki sem sérült meg súlyosan. (according to)",
                "answer": "szerint"
            },
            {
                "id": "b1-13-01.ex05",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mi a lap tetején lévő, nagy betűkkel szedett cím?",
                "options": [
                    "főcím",
                    "lábjegyzet",
                    "apróhirdetés"
                ],
                "correct": 0
            },
            {
                "id": "b1-13-01.ex06",
                "type": "sentence-builder",
                "category": "grammar",
                "sentence": "A hírek szerint holnap jelentős havazás várható a hegyekben.",
                "tiles": ["A", "hírek", "szerint", "holnap", "jelentős", "havazás", "várható", "a", "hegyekben."]
            },
            {
                "id": "b1-13-01.ex07",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Miért fontos a hírforrás megbízhatósága a híradásban?",
                "options": [
                    "Mert a hiteles híradás csak pontos és ellenőrzött adatokra épülhet.",
                    "Mert a tévében csak rövid filmeket szabad vetíteni.",
                    "Mert a nyomdákban nincs elég fekete festék."
                ],
                "correct": 0
            },
            {
                "id": "b1-13-01.ex08",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A lap külföldi ____ részletesen beszámolt a választás eredményéről. (correspondent)",
                "answer": "tudósítója"
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-13-01-ex.json", ex_01)

    ex_02 = {
        "lesson": "b1-13-02",
        "exercises": [
            {
                "id": "b1-13-02.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["nyilatkozat", "official statement"],
                    ["állítás", "claim / assertion"],
                    ["szóvivő", "spokesperson"],
                    ["közlemény", "announcement / press release"]
                ]
            },
            {
                "id": "b1-13-02.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Hogyan alakítjuk át a kérdést közvetett kérdéssé: 'Igaz a hír?'",
                "options": [
                    "Megkérdezték, hogy igaz-e a hír.",
                    "Megkérdezték, hogy igaz vajon a hír volt-e.",
                    "Megkérdezték, hogy vajon igaz volna a hír."
                ],
                "correct": 0
            },
            {
                "id": "b1-13-02.ex03",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A kormányzati ____ válaszolt az újságírók kérdéseire a sajtótájékoztatón. (spokesperson)",
                "answer": "szóvivő"
            },
            {
                "id": "b1-13-02.ex04",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A riporter arról érdeklődött, hogy mikor hozzák ____ a hivatalos döntést. (public / to light)",
                "answer": "nyilvánosságra"
            },
            {
                "id": "b1-13-02.ex05",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Melyik szó jelenti az intézmény által kiadott hivatalos tájékoztató szöveget?",
                "options": [
                    "közlemény",
                    "magánlevél",
                    "regényrészlet"
                ],
                "correct": 0
            },
            {
                "id": "b1-13-02.ex06",
                "type": "sentence-builder",
                "category": "grammar",
                "sentence": "A minisztérium határozottan cáfolta a sajtóban megjelent téves állításokat.",
                "tiles": ["A", "minisztérium", "határozottan", "cáfolta", "a", "sajtóban", "megjelent", "téves", "állításokat."]
            },
            {
                "id": "b1-13-02.ex07",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A társaság hivatalos ____ adott ki a tegnapi műszaki hibáról. (statement)",
                "answer": "nyilatkozatot"
            },
            {
                "id": "b1-13-02.ex08",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik igével fejezzük ki, hogy valaki egyetért és igaznak fogad el egy információt?",
                "options": [
                    "megerősít",
                    "megtagad",
                    "félrevezet"
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-13-02-ex.json", ex_02)

    ex_03 = {
        "lesson": "b1-13-03",
        "exercises": [
            {
                "id": "b1-13-03.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["híresztelés", "rumor / hearsay"],
                    ["álhír", "fake news / hoax"],
                    ["megbízhatóság", "reliability"],
                    ["tényellenőrzés", "fact-checking"]
                ]
            },
            {
                "id": "b1-13-03.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik határozószó fejezi ki, hogy az információ nem bizonyított, csak mások mondják?",
                "options": [
                    "állítólag",
                    "kétségkívül",
                    "bizonyítottan"
                ],
                "correct": 0
            },
            {
                "id": "b1-13-03.ex03",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A független szerkesztőség alapos ____ vetette alá a gyanús internetes videót. (fact-checking)",
                "answer": "tényellenőrzésnek"
            },
            {
                "id": "b1-13-03.ex04",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A közösségi oldalakon futótűzként terjedt a veszélyes ____. (fake news)",
                "answer": "álhír"
            },
            {
                "id": "b1-13-03.ex05",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mi az a hír, amelynek nincs valóságalapja, és csak pletykákon alapul?",
                "options": [
                    "alaptalan híresztelés",
                    "tudományos dolgozat",
                    "bírósági ítélet"
                ],
                "correct": 0
            },
            {
                "id": "b1-13-03.ex06",
                "type": "sentence-builder",
                "category": "grammar",
                "sentence": "Nagyon kétséges, hogy a névtelen forrásból származó információ valóban hiteles.",
                "tiles": ["Nagyon", "kétséges,", "hogy", "a", "névtelen", "forrásból", "származó", "információ", "valóban", "hiteles."]
            },
            {
                "id": "b1-13-03.ex07",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A kutatók szerint a tudományos források ____ sokkal magasabb a bulvárlapokénál. (reliability)",
                "answer": "megbízhatósága"
            },
            {
                "id": "b1-13-03.ex08",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Hogyan mondjuk: 'Úgy tűnik, hogy a hír valótlan'?",
                "options": [
                    "Úgy tűnik, hogy a hír nem felel meg a valóságnak.",
                    "Úgy tűnne, ha a hír valótlan lett legyen.",
                    "Tűnve van, hogy a hír valótlanul volt."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-13-03-ex.json", ex_03)

    ex_04 = {
        "lesson": "b1-13-04",
        "exercises": [
            {
                "id": "b1-13-04.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["riport", "feature report / story"],
                    ["interjúalany", "interviewee"],
                    ["közvélemény", "public opinion"],
                    ["nyomozás", "investigative inquiry"]
                ]
            },
            {
                "id": "b1-13-04.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik kifejezés jelenti, hogy titkos vagy elhallgatott dolgok nyilvánosságra kerülnek?",
                "options": [
                    "fény derül valamire",
                    "ködbe vész valami",
                    "lábát teszi valahova"
                ],
                "correct": 0
            },
            {
                "id": "b1-13-04.ex03",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A televíziós stáb megrázó ____ készített a természeti katasztrófa áldozatairól. (feature report)",
                "answer": "riportot"
            },
            {
                "id": "b1-13-04.ex04",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A tapasztalt újságíró türelmesen kérdezte a meghatott ____. (interviewee)",
                "answer": "interjúalanyt"
            },
            {
                "id": "b1-13-04.ex05",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mi fejezi ki a társadalom többségének gondolatait és reakcióját?",
                "options": [
                    "közvélemény",
                    "személyes titok",
                    "családi ebéd"
                ],
                "correct": 0
            },
            {
                "id": "b1-13-04.ex06",
                "type": "sentence-builder",
                "category": "grammar",
                "sentence": "Azt követően, hogy a cikk megjelent, azonnal vizsgálat indult az ügyben.",
                "tiles": ["Azt", "követően,", "hogy", "a", "cikk", "megjelent,", "azonnal", "vizsgálat", "indult", "az", "ügyben."]
            },
            {
                "id": "b1-13-04.ex07",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A sajtó által folytatott kitartó ____ megmentette az ártatlanul elítélt férfit. (journalistic investigation)",
                "answer": "nyomozás"
            },
            {
                "id": "b1-13-04.ex08",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Miért fontos, hogy egy riporter több szemtanút is meghallgasson?",
                "options": [
                    "Mert így több különböző szemszögből látja az eseményeket.",
                    "Mert a riporter nem tud egyedül jegyzetelni.",
                    "Mert a televízióban kötelező sok embernek beszélnie."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-13-04-ex.json", ex_04)

    ex_05 = {
        "lesson": "b1-13-05",
        "exercises": [
            {
                "id": "b1-13-05.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["összegzés", "summary / synthesis"],
                    ["álláspont", "standpoint / perspective"],
                    ["véleménycikk", "opinion piece / op-ed"],
                    ["tanulság", "lesson / moral takeaway"]
                ]
            },
            {
                "id": "b1-13-05.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik kifejezéssel vonhatunk le kiegyensúlyozott összefoglaló véleményt?",
                "options": [
                    "Mindent összevetve",
                    "Sehogy se nézve",
                    "Hirtelen felindulásból"
                ],
                "correct": 0
            },
            {
                "id": "b1-13-05.ex03",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A publicista egy gondolatébresztő ____ fejtette ki érveit a hétvégi számban. (op-ed piece)",
                "answer": "véleménycikkben"
            },
            {
                "id": "b1-13-05.ex04",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Egyfelől fontos a gyorsaság, ____ elengedhetetlen a pontosság megőrzése. (on the other hand)",
                "answer": "másfelől"
            },
            {
                "id": "b1-13-05.ex05",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mi a tanulság jelentése egy történet vagy vita végén?",
                "options": [
                    "A tapasztalatokból levonható erkölcsi vagy gyakorlati következtetés.",
                    "A nyomtatott papír mérete és súlya.",
                    "A televíziós készülék ára a boltban."
                ],
                "correct": 0
            },
            {
                "id": "b1-13-05.ex06",
                "type": "sentence-builder",
                "category": "grammar",
                "sentence": "Összegzésként megállapíthatjuk, hogy a média szerepe döntő fontosságú a demokráciában.",
                "tiles": ["Összegzésként", "megállapíthatjuk,", "hogy", "a", "média", "szerepe", "döntő", "fontosságú", "a", "demokráciában."]
            },
            {
                "id": "b1-13-05.ex07",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A vitában a szakértők határozott és világos ____ képviseltek a környezetvédelem mellett. (standpoint)",
                "answer": "álláspontot"
            },
            {
                "id": "b1-13-05.ex08",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Miben különbözik egy véleménycikk egy egyszerű híradástól?",
                "options": [
                    "A véleménycikk a szerző személyes nézőpontját és érvelését tükrözi, nem csupán a puszta tényeket.",
                    "A véleménycikkben nincsenek mondatok és szavak.",
                    "A véleménycikket csak gyerekek írhatják iskolai füzetbe."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-13-05-ex.json", ex_05)

    ex_consolidation = {
        "lesson": "b1-13-consolidation",
        "exercises": [
            {
                "id": "b1-13-consolidation.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["hírforrás", "news source"],
                    ["szóvivő", "spokesperson"],
                    ["álhír", "fake news"],
                    ["véleménycikk", "op-ed"]
                ]
            },
            {
                "id": "b1-13-consolidation.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik mondat alkalmaz helyes közvetett beszédet magyarul?",
                "options": [
                    "A riporter azt mondta, hogy a tárgyalások ma fejeződnek be.",
                    "A riporter azt mondta, hogy a tárgyalások ma fejeződnének be volt.",
                    "A riporter mondta azt, hogy befejeződnek lennének ma a tárgyalások."
                ],
                "correct": 0
            },
            {
                "id": "b1-13-consolidation.ex03",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A tudatos olvasó mindig végez alapos ____, mielőtt megoszt egy hírt az interneten. (fact-checking)",
                "answer": "tényellenőrzést"
            },
            {
                "id": "b1-13-consolidation.ex04",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Mindent ____, a kritikus gondolkodás elengedhetetlen az információs társadalomban. (all things considered)",
                "answer": "összevetve"
            },
            {
                "id": "b1-13-consolidation.ex05",
                "type": "sentence-builder",
                "category": "grammar",
                "sentence": "A hivatalos közlemény szerint a kár sokkal kisebb volt a vártnál.",
                "tiles": ["A", "hivatalos", "közlemény", "szerint", "a", "kár", "sokkal", "kisebb", "volt", "a", "vártnál."]
            },
            {
                "id": "b1-13-consolidation.ex06",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Melyik szó jelenti a híradás összefoglaló fő üzenetét?",
                "options": [
                    "összegzés",
                    "nyomtatás",
                    "helyesírás"
                ],
                "correct": 0
            },
            {
                "id": "b1-13-consolidation.ex07",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A lap címoldalán feltűnő nagy ____ azonnal magára vonta az olvasók figyelmét. (headline)",
                "answer": "főcím"
            },
            {
                "id": "b1-13-consolidation.ex08",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Hogyan fogalmazta meg Boka János a grund védelmének felhívását Molnár Ferenc regényében?",
                "options": [
                    "Írásos kiáltványban hívta fel a Pál utcai fiúkat a fegyelmezett és hősies kitartásra.",
                    "Feladta a harcot és elment fagyizni a barátaival.",
                    "Megkérte a tanárokat, hogy ők védjék meg a grundot a vörösingesektől."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-13-consolidation-ex.json", ex_consolidation)

    # -------------------------------------------------------------------------
    # 5. Lesson Files (01 to 05 + consolidation)
    # -------------------------------------------------------------------------
    for i in range(1, 6):
        padded = f"0{i}"
        titles = {
            "01": ("According to the News", "A hírek szerint"),
            "02": ("She Said That...", "Azt mondta, hogy..."),
            "03": ("Is It True?", "Igaz vagy nem?"),
            "04": ("Following a Story", "Egy esemény nyomában"),
            "05": ("Summarizing What You Heard", "Összefoglalás és vélemény")
        }
        en_title, hu_title = titles[padded]
        lesson_data = {
            "id": f"lesson.b1.13-{padded}",
            "unit": 13,
            "title": en_title,
            "level": "B1",
            "grammar": "Reported Speech and Indirect Statements in Media",
            "goal": [
                f"I can understand and use vocabulary for {en_title.lower()}.",
                "I can form reported speech statements and indirect questions in Hungarian.",
                "I can evaluate source credibility and critically analyze media messages.",
                "I can master four new target vocabulary items in authentic context."
            ],
            "sections": [
                {
                    "type": "goal",
                    "title": "Lesson Goals",
                    "items": [
                        f"I can understand and use vocabulary for {en_title.lower()}.",
                        "I can form reported speech statements and indirect questions in Hungarian.",
                        "I can evaluate source credibility and critically analyze media messages.",
                        "I can master four new target vocabulary items in authentic context."
                    ]
                },
                {"type": "recycle", "title": "Quick Review"},
                {"type": "grammar", "ref": f"grammar/b1/b1-13-{padded}-a-gr.json"},
                {"type": "grammar", "ref": f"grammar/b1/b1-13-{padded}-b-gr.json"},
                {"type": "vocabulary", "title": "Lesson Vocabulary", "ref": f"vocabulary/b1/b1-13-{padded}-voc.json"},
                {
                    "type": "practice",
                    "title": "Practice",
                    "ref": f"exercises/b1/b1-13-{padded}-ex.json"
                }
            ]
        }
        write_json(f"content/hu/lessons/b1/b1-13-{padded}.json", lesson_data)

    consolidation_data = {
        "id": "lesson.b1.13-consolidation",
        "unit": 13,
        "title": "Unit 13 Consolidation",
        "level": "B1",
        "grammar": "Consolidation of Reported Speech & Information Literacy",
        "sections": [
            {
                "type": "story",
                "title": "A vörösingesek követe és a kiáltvány a grundon",
                "ref": "stories/classics/b1/b1-13-palutcaifiuk.json"
            },
            {
                "type": "practice",
                "title": "Consolidation Practice",
                "ref": "exercises/b1/b1-13-consolidation-ex.json"
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-13-consolidation.json", consolidation_data)
    print("Successfully built Hungarian B1 Core Unit 13 (b1-13)!")

if __name__ == "__main__":
    build_unit_13_core()
