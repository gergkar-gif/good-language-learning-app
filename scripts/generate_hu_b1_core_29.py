#!/usr/bin/env python3
"""Generate Hungarian B1 Core Unit 29: Migration & Identity (b1-29)."""

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

def build_unit_29_core():
    # -------------------------------------------------------------------------
    # 1. Vocabulary Files (4 words each = 20 words total)
    # -------------------------------------------------------------------------
    voc_01 = {
        "id": "vocab.b1.29.01",
        "lesson": "b1-29-01",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "kivándorlás", "translation": "emigration, migrating abroad", "pos": "noun"},
            {"lemma": "áttelepülés", "translation": "resettlement, relocation to another country", "pos": "noun"},
            {"lemma": "megélhetés", "translation": "livelihood, earning a living", "pos": "noun"},
            {"lemma": "honvágy", "translation": "homesickness, longing for one's homeland", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-29-01-voc.json", voc_01)

    voc_02 = {
        "id": "vocab.b1.29.02",
        "lesson": "b1-29-02",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "úti cél", "translation": "destination, travel goal", "pos": "noun"},
            {"lemma": "letelepedés", "translation": "settling down, permanent settlement", "pos": "noun"},
            {"lemma": "beilleszkedés", "translation": "integration, fitting into society", "pos": "noun"},
            {"lemma": "alkalmazkodás", "translation": "adaptation, adjusting to new circumstances", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-29-02-voc.json", voc_02)

    voc_03 = {
        "id": "vocab.b1.29.03",
        "lesson": "b1-29-03",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "kettős identitás", "translation": "dual identity, belonging to two cultures", "pos": "noun"},
            {"lemma": "kötődés", "translation": "attachment, bond, tie to a place", "pos": "noun"},
            {"lemma": "szülőföld", "translation": "homeland, native soil, birthplace", "pos": "noun"},
            {"lemma": "idegenség", "translation": "strangeness, feeling of foreignness", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-29-03-voc.json", voc_03)

    voc_04 = {
        "id": "vocab.b1.29.04",
        "lesson": "b1-29-04",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "származás", "translation": "origin, descent, ancestry", "pos": "noun"},
            {"lemma": "anyanyelv", "translation": "mother tongue, native language", "pos": "noun"},
            {"lemma": "örökség", "translation": "heritage, cultural legacy", "pos": "noun"},
            {"lemma": "emlékőrzés", "translation": "preservation of memories and roots", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-29-04-voc.json", voc_04)

    voc_05 = {
        "id": "vocab.b1.29.05",
        "lesson": "b1-29-05",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "otthonérzet", "translation": "sense of home, feeling at ease", "pos": "noun"},
            {"lemma": "biztonságérzet", "translation": "sense of security and peace of mind", "pos": "noun"},
            {"lemma": "befogadás", "translation": "acceptance, welcoming, embracing", "pos": "noun"},
            {"lemma": "hovatartozás", "translation": "sense of belonging, affiliation", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-29-05-voc.json", voc_05)

    # -------------------------------------------------------------------------
    # 2. Grammar Files (2 per regular lesson = 10 files)
    # -------------------------------------------------------------------------
    gr_01_a = {
        "id": "grammar.b1.29.01.causal-postpositions",
        "title": "Causal Postpositions: miatt, folytán, következtében",
        "sections": [
            {
                "type": "text",
                "title": "Expressing Causes and Reasons for Migration",
                "content": "To explain external drivers of movement, Hungarian uses causal postpositions: *miatt* ('because of'), *folytán* ('as a consequence of' - usually with instrumental *-val/-vel*), and *következtében* ('as a result of' - preceded by the noun's unmarked or possessive form)."
            },
            {
                "type": "examples",
                "title": "Causal examples",
                "items": [
                    {
                        "spanish": "A jobb megélhetés és a tanulási lehetőségek miatt sok fiatal költözik külföldre.",
                        "english": "Because of better livelihoods and study opportunities, many young people move abroad."
                    },
                    {
                        "spanish": "A történelmi viharok következtében százezrek kényszerültek elhagyni szülőföldjüket.",
                        "english": "As a consequence of historical storms, hundreds of thousands were forced to leave their homeland."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-29-01-a-gr.json", gr_01_a)

    gr_01_b = {
        "id": "grammar.b1.29.01.concessive-postpositions",
        "title": "Concession with Postpositions: ellenére, dacára",
        "sections": [
            {
                "type": "text",
                "title": "Overcoming Obstacles with 'ellenére' and 'dacára'",
                "content": "Both *ellenére* and *dacára* express 'in spite of / despite'. They take the possessive or unmarked form: *a nehézségek ellenére* ('despite the difficulties'), *a honvágy dacára* ('in spite of homesickness')."
            },
            {
                "type": "examples",
                "title": "Concessive examples",
                "items": [
                    {
                        "spanish": "A kezdeti nehézségek ellenére sikeresen megalapozta új életét.",
                        "english": "In spite of initial difficulties, he successfully established his new life."
                    },
                    {
                        "spanish": "Az eltelő évtizedek dacára sem felejtette el gyermekkori barátait.",
                        "english": "Despite the passing decades, she did not forget her childhood friends."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-29-01-b-gr.json", gr_01_b)

    gr_02_a = {
        "id": "grammar.b1.29.02.verbs-of-relocation",
        "title": "Verbs of Relocation & Adaptation: letelepszik, beilleszkedik",
        "sections": [
            {
                "type": "text",
                "title": "Government of Settlement and Integration Verbs",
                "content": "*Letelepszik vhol/vhová* (settles down in a place - superessive *-on/-en/-ön* or inessive *-ban/-ben*), *beilleszkedik a társadalomba* (integrates into society - illative *-ba/-be*), *alkalmazkodik a helyi szokásokhoz* (adapts to local customs - allative *-hoz/-hez/-höz*)."
            },
            {
                "type": "examples",
                "title": "Settlement in practice",
                "items": [
                    {
                        "spanish": "A család végül egy csendes külvárosi negyedben telepedett le.",
                        "english": "The family finally settled down in a quiet suburban quarter."
                    },
                    {
                        "spanish": "A gyerekek gyorsan és könnyen beilleszkedtek az új iskolai közösségbe.",
                        "english": "The children integrated quickly and easily into the new school community."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-29-02-a-gr.json", gr_02_a)

    gr_02_b = {
        "id": "grammar.b1.29.02.temporal-clauses-during",
        "title": "Simultaneity in Journey: miközben, mialatt, során",
        "sections": [
            {
                "type": "text",
                "title": "Expressing Parallel Actions and Long Processes",
                "content": "*Miközben / mialatt* ('while / as') introduce temporal clauses describing overlapping events. In noun phrases, the postposition *során* ('in the course of / during') governs processes: *az utazás során* ('during the journey')."
            },
            {
                "type": "examples",
                "title": "Simultaneity examples",
                "items": [
                    {
                        "spanish": "Miközben új nyelvet tanult, folyamatosan ápolta az anyanyelvét is.",
                        "english": "While he was learning a new language, he also continuously cultivated his mother tongue."
                    },
                    {
                        "spanish": "A beilleszkedés folyamata során számos értékes barátra lelt.",
                        "english": "In the course of the integration process, she found numerous valuable friends."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-29-02-b-gr.json", gr_02_b)

    gr_03_a = {
        "id": "grammar.b1.29.03.expressing-belonging",
        "title": "Belonging and Ties: tartozik vhová, kötődik vmihez",
        "sections": [
            {
                "type": "text",
                "title": "Verbs Expressing Affiliation and Emotional Ties",
                "content": "*Tartozik vhová* (belongs somewhere - allative *-hoz/-hez/-höz* or sublative *-ra/-re*), *kötődik a szülőföldjéhez* (is attached to his homeland - allative *-hoz/-hez/-höz*), *erős kötelék fűzi vkihez* (strong bonds tie him to sb)."
            },
            {
                "type": "examples",
                "title": "Belonging examples",
                "items": [
                    {
                        "spanish": "Bár messze él, a szíve mélyén mindig ehhez a tájhoz tartozik.",
                        "english": "Although he lives far away, in the depth of his heart he always belongs to this landscape."
                    },
                    {
                        "spanish": "Ezer láthatatlan szállal kötődik a nagyszülei szülőfalujához.",
                        "english": "She is tied by a thousand invisible threads to the native village of her grandparents."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-29-03-a-gr.json", gr_03_a)

    gr_03_b = {
        "id": "grammar.b1.29.03.dual-identity-constructions",
        "title": "Dual Identity: egyszerre... és..., nemcsak... hanem...",
        "sections": [
            {
                "type": "text",
                "title": "Correlative Conjunctions in Complex Identity",
                "content": "Expressing bicultural identity relies on paired correlatives: *egyszerre... és...* ('at once... and...'), *nemcsak... hanem... is* ('not only... but also...'): *Egyszerre érzi magát európainak és büszke magyarnak.*"
            },
            {
                "type": "examples",
                "title": "Correlative examples",
                "items": [
                    {
                        "spanish": "A kétnyelvű fiatalok nemcsak két kultúrát ismernek, hanem mindkettőben otthon is vannak.",
                        "english": "Bilingual youth not only know two cultures, but are also at home in both."
                    },
                    {
                        "spanish": "Egyszerre tiszteli az új hazája törvényeit és őrzi ősei hagyományait.",
                        "english": "At once he respects the laws of his new homeland and preserves the traditions of his ancestors."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-29-03-b-gr.json", gr_03_b)

    gr_04_a = {
        "id": "grammar.b1.29.04.origin-and-roots",
        "title": "Origins and Ancestry: származik vhonnan, gyökerezik vmiben",
        "sections": [
            {
                "type": "text",
                "title": "Verbal Valencies for Lineage and Roots",
                "content": "*Származik vhonnan* (originates from / is descended from - elative *-ból/-ből* or delative *-ról/-ről*), *gyökerezik vmiben* (is rooted in - inessive *-ban/-ben*), *visszanyúlik vmeddig* (reaches back to - terminative *-ig*)."
            },
            {
                "type": "examples",
                "title": "Lineage examples",
                "items": [
                    {
                        "spanish": "A családja egy régi felvidéki polgári nemzetségből származik.",
                        "english": "His family is descended from an old Upper Hungarian bourgeois lineage."
                    },
                    {
                        "spanish": "Gondolkodásmódja mélyen a klasszikus európai műveltségben gyökerezik.",
                        "english": "Her way of thinking is deeply rooted in classical European culture."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-29-04-a-gr.json", gr_04_a)

    gr_04_b = {
        "id": "grammar.b1.29.04.preservation-of-language",
        "title": "Language Retention: megőrzi az anyanyelvét, ápolja",
        "sections": [
            {
                "type": "text",
                "title": "Aspectual Verbs with Cultural Heritage",
                "content": "*Megőrzi a nyelvtudását* ('preserves one's language ability'), *ápolja a nemzeti hagyományokat* ('cultivates national traditions'), *átadja az utódoknak* ('passes on to descendants' - dative *-nak/-nek*)."
            },
            {
                "type": "examples",
                "title": "Preservation examples",
                "items": [
                    {
                        "spanish": "Az emigrációban élő szülők gondosan átadták az anyanyelvet gyermekeiknek.",
                        "english": "Parents living in emigration carefully passed on the mother tongue to their children."
                    },
                    {
                        "spanish": "Márai Sándor emigrációjának évtizedei alatt is hűségesen megőrizte a magyar nyelvet.",
                        "english": "Sándor Márai faithfully preserved the Hungarian language throughout the decades of his exile."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-29-04-b-gr.json", gr_04_b)

    gr_05_a = {
        "id": "grammar.b1.29.05.feeling-at-home",
        "title": "Sense of Home: otthon érzi magát, megleli a nyugalmát",
        "sections": [
            {
                "type": "text",
                "title": "Reflexive Comfort and Belated Belonging",
                "content": "*Otthon érzi magát* ('feels at home'), *megtalálja a helyét* ('finds one's place'), *befogadásra talál* ('finds acceptance/welcoming - sublative *-ra/-re*)."
            },
            {
                "type": "examples",
                "title": "Feeling at home examples",
                "items": [
                    {
                        "spanish": "Hosszú vándorlás után végre békére és igazi otthonra talált.",
                        "english": "After long wandering, he finally found peace and a true home."
                    },
                    {
                        "spanish": "Ott vagyok otthon, ahol megértik a szavaimat és tiszteletben tartják a személyiségemet.",
                        "english": "I am at home where they understand my words and respect my personality."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-29-05-a-gr.json", gr_05_a)

    gr_05_b = {
        "id": "grammar.b1.29.05.complex-adverbial-participle",
        "title": "Adverbial Participle in Retrospective: visszatekintve, megérkezve",
        "sections": [
            {
                "type": "text",
                "title": "The -va / -ve Adverbial Participle in Narrative Reflection",
                "content": "In reflective personal memoirs, adverbial participles (*-va/-ve*) set background circumstance or temporal vantage point: *visszatekintve a múltra* ('looking back at the past'), *az új városba megérkezve* ('having arrived in the new city')."
            },
            {
                "type": "examples",
                "title": "Participle reflection examples",
                "items": [
                    {
                        "spanish": "Visszatekintve az eltelt évekre, megértette a vándorlás igazi értelmét.",
                        "english": "Looking back upon the elapsed years, he understood the true meaning of the wandering."
                    },
                    {
                        "spanish": "A hajó korlátjára támaszkodva némán nézte az eltűnő partokat.",
                        "english": "Leaning on the ship's railing, he silently watched the receding shores."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-29-05-b-gr.json", gr_05_b)

    # -------------------------------------------------------------------------
    # 3. Exercises Files (6 files = 48 exercises total)
    # -------------------------------------------------------------------------
    ex_01 = {
        "lesson": "b1-29-01",
        "exercises": [
            {
                "id": "b1-29-01.ex01",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent a 'honvágy' fogalma?",
                "options": [
                    "A szülőföld, a család és a távoli hazai otthon utáni mély lelki vágyakozást.",
                    "A repülőjegyet vásárolni vágyó turista örömét.",
                    "A szállodai szoba lemondását."
                ],
                "correct": 0
            },
            {
                "id": "b1-29-01.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A nehéz gazdasági körülmények mi_____ döntöttek az áttelepülés mellett. (because of - att)",
                "answer": "att"
            },
            {
                "id": "b1-29-01.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "jobb", "megélhetés", "reményében", "sokan", "választják", "a", "külföldi", "munkát."],
                "solution": ["A", "jobb", "megélhetés", "reményében", "sokan", "választják", "a", "külföldi", "munkát."]
            },
            {
                "id": "b1-29-01.ex04",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik mondat fejezi ki helyesen az akadály leküzdését az 'ellenére' névutóval?",
                "options": [
                    "A nehézségek ellenére soha nem veszítette el a reményt.",
                    "A nehézségek miatt azonnal feladta a küzdelmet.",
                    "A nehézségekben sétált az utcán."
                ],
                "correct": 0
            },
            {
                "id": "b1-29-01.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A háború következtében megindult a tömeges ki_____vándorlás. (prefix - ki)",
                "answer": "ki"
            },
            {
                "id": "b1-29-01.ex06",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent az 'áttelepülés' kifejezés?",
                "options": [
                    "Végleges elköltözést egy másik városba vagy országba új élet kezdése céljából.",
                    "Egy délutáni kirándulást a szomszéd faluba.",
                    "A fák átültetését a kert másik sarkába."
                ],
                "correct": 0
            },
            {
                "id": "b1-29-01.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A nyelvi akadályok dacá_____ sikeresen elhelyezkedett a szakmájában. (in spite of - ra)",
                "answer": "ra"
            },
            {
                "id": "b1-29-01.ex08",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "honvágy", "érzése", "gyakran", "megérinti", "a", "távol", "élőket."],
                "solution": ["A", "honvágy", "érzése", "gyakran", "megérinti", "a", "távol", "élőket."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-29-01-ex.json", ex_01)

    ex_02 = {
        "lesson": "b1-29-02",
        "exercises": [
            {
                "id": "b1-29-02.ex01",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent a társadalmi 'beilleszkedés' folyamata egy új országban?",
                "options": [
                    "A helyi nyelv elsajátítását, a szokások megértését és az új közösség egyenrangú tagjává válást.",
                    "A teljes elszigetelődést a szomszédoktól.",
                    "A bőröndök kicsomagolásának elhalasztását."
                ],
                "correct": 0
            },
            {
                "id": "b1-29-02.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A fiatal család végül Budapesten telepedett _____ tartósan. (settled down - le)",
                "answer": "le"
            },
            {
                "id": "b1-29-02.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "beilleszkedés", "során", "nagyon", "fontos", "a", "nyelvtudás", "fejlesztése."],
                "solution": ["A", "beilleszkedés", "során", "nagyon", "fontos", "a", "nyelvtudás", "fejlesztése."]
            },
            {
                "id": "b1-29-02.ex04",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Hogyan fejezzük ki helyesen az alkalmazkodást a helyi szokásokhoz?",
                "options": [
                    "Alkalmazkodik a helyi szokásokhoz.",
                    "Alkalmazkodik a helyi szokásokat.",
                    "Alkalmazkodik a helyi szokásokban."
                ],
                "correct": 0
            },
            {
                "id": "b1-29-02.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A hosszú utazás után elérték a végső úti cél_____ . (their destination - jukat)",
                "answer": "jukat"
            },
            {
                "id": "b1-29-02.ex06",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent a 'letelepedés' egy új otthonban?",
                "options": [
                    "Állandó lakhely létesítését és tartós otthonteremtést egy választott helyen.",
                    "Egy sátor felverését két órára az erdőben.",
                    "Egy kávé elfogyasztását az állomáson."
                ],
                "correct": 0
            },
            {
                "id": "b1-29-02.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Miközben a szülők dolgoztak, a gyerekek az iskolában tanul_____. (they studied - tak)",
                "answer": "tak"
            },
            {
                "id": "b1-29-02.ex08",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "rugalmas", "alkalmazkodás", "megkönnyíti", "az", "új", "életkezdést."],
                "solution": ["A", "rugalmas", "alkalmazkodás", "megkönnyíti", "az", "új", "életkezdést."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-29-02-ex.json", ex_02)

    ex_03 = {
        "lesson": "b1-29-03",
        "exercises": [
            {
                "id": "b1-29-03.ex01",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent a 'kettős identitás' egy két kultúrában élő ember számára?",
                "options": [
                    "Azt, hogy két kultúrához és közösséghez is mély érzelmi és szellemi kötődés fűzi.",
                    "Azt, hogy két személyi igazolványt hord a pénztárcájában.",
                    "Azt, hogy mindkét fülében van fülbevaló."
                ],
                "correct": 0
            },
            {
                "id": "b1-29-03.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Ezer szállal kötődik a szülőföldjé_____. (allative - hez)",
                "answer": "hez"
            },
            {
                "id": "b1-29-03.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Egyszerre", "érzi", "magát", "európai", "polgárnak", "és", "magyarnak."],
                "solution": ["Egyszerre", "érzi", "magát", "európai", "polgárnak", "és", "magyarnak."]
            },
            {
                "id": "b1-29-03.ex04",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik mondatban találunk helyes páros kötőszót?",
                "options": [
                    "Nemcsak a múltját becsüli, hanem a jövőjét is építi.",
                    "Nemcsak a múltját becsüli, de a jövőjét alszik.",
                    "Vagy a múltját becsüli, és a jövőjét fut."
                ],
                "correct": 0
            },
            {
                "id": "b1-29-03.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A kezdeti idegens_____ lassan felváltotta a megszokás és a biztonság. (stem suffix - ég)",
                "answer": "ég"
            },
            {
                "id": "b1-29-03.ex06",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent a 'szülőföld' fogalma?",
                "options": [
                    "Azt a vidéket vagy hazát, ahol az ember született, és ahol a gyökerei találhatók.",
                    "A veteményeskertbe hozott fekete földet.",
                    "A játszótéri homokozót."
                ],
                "correct": 0
            },
            {
                "id": "b1-29-03.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Bár messze él a határoktól, a szívében mégis ehhez a néphez tartoz_____. (belongs - ik)",
                "answer": "ik"
            },
            {
                "id": "b1-29-03.ex08",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "szülőföld", "emléke", "egész", "életünkben", "elkísér", "bennünket."],
                "solution": ["A", "szülőföld", "emléke", "egész", "életünkben", "elkísér", "bennünket."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-29-03-ex.json", ex_03)

    ex_04 = {
        "lesson": "b1-29-04",
        "exercises": [
            {
                "id": "b1-29-04.ex01",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Miért kiemelkedő jelentőségű az 'anyanyelv' az identitás megőrzésében?",
                "options": [
                    "Mert az anyanyelv az a legmélyebb belső közeg, amelyben az érzéseink és gondolataink születnek.",
                    "Mert az anyanyelven lehet a leggyorsabban számolni.",
                    "Mert csak egy nyelvet szabad beszélni az életben."
                ],
                "correct": 0
            },
            {
                "id": "b1-29-04.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A családja egy régi kassai polgárcsaládból származ_____. (is descended - ik)",
                "answer": "ik"
            },
            {
                "id": "b1-29-04.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Az", "anyanyelv", "ápolása", "és", "az", "emlékőrzés", "közös", "kötelességünk."],
                "solution": ["Az", "anyanyelv", "ápolása", "és", "az", "emlékőrzés", "közös", "kötelességünk."]
            },
            {
                "id": "b1-29-04.ex04",
                "type": "multiple-choice",
                "category": "literature",
                "question": "Melyik felvidéki város polgári világát örökítette meg Márai Sándor az 'Egy polgár vallomásaiban'?",
                "options": [
                    "Kassát.",
                    "Bécsot.",
                    "Kolozsvárt."
                ],
                "correct": 0
            },
            {
                "id": "b1-29-04.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A kulturális örök_____ generációról generációra hagyományozódik át. (stem suffix - ség)",
                "answer": "ség"
            },
            {
                "id": "b1-29-04.ex06",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Mit jelentett Márai Sándor számára a magyar nyelv az emigráció évtizedeiben?",
                "options": [
                    "Az egyetlen igazi hazát, a lelki menedéket és a szellemi hűség legmagasabb formáját.",
                    "Egy elfelejtendő nyelvet, amit nem használt többé.",
                    "Kizárólag a hivatalos ügyintézés eszközét."
                ],
                "correct": 0
            },
            {
                "id": "b1-29-04.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A szülők gondosan átadták az anyanyelvet a gyermekeik_____. (to their children - nek)",
                "answer": "nek"
            },
            {
                "id": "b1-29-04.ex08",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "származás", "tudata", "biztos", "támaszt", "nyújt", "az", "életben."],
                "solution": ["A", "származás", "tudata", "biztos", "támaszt", "nyújt", "az", "életben."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-29-04-ex.json", ex_04)

    ex_05 = {
        "lesson": "b1-29-05",
        "exercises": [
            {
                "id": "b1-29-05.ex01",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent a valódi 'otthonérzet' egy ember számára?",
                "options": [
                    "Azt a mély belső nyugalmat és biztonságot, amikor valaki elfogadottnak és megbecsültnek érzi magát.",
                    "A bútorok megvásárlását az áruházban.",
                    "A ház kulcsának zsebben tartását."
                ],
                "correct": 0
            },
            {
                "id": "b1-29-05.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Visszatekintve az eltelt évtizedekre, meglel_____ a belső békét. (found - te)",
                "answer": "te"
            },
            {
                "id": "b1-29-05.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "szerető", "közösségben", "mindenki", "igazi", "otthonra", "találhat."],
                "solution": ["A", "szerető", "közösségben", "mindenki", "igazi", "otthonra", "találhat."]
            },
            {
                "id": "b1-29-05.ex04",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Hogyan használjuk a határozói igenevet visszatekintő gondolat kifejezésére?",
                "options": [
                    "Visszatekintve a múltra, hálás vagyok minden tapasztalatért.",
                    "Visszatekintett a múltra tegnap este az ablakban.",
                    "Visszatekintő ember sétál a járdán."
                ],
                "correct": 0
            },
            {
                "id": "b1-29-05.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A meleg fogadtatás erősítette az új lakók biztonságérzet_____. (their sense - ét)",
                "answer": "ét"
            },
            {
                "id": "b1-29-05.ex06",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent a 'hovatartozás' tudata?",
                "options": [
                    "Annak a biztos tudatát, hogy melyik nemzethez, családhoz és kultúrához kötődik a lelkünk.",
                    "A vonatok indulási idejének ismeretét.",
                    "A postai címzés helyes felírását a borítékra."
                ],
                "correct": 0
            },
            {
                "id": "b1-29-05.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Hosszú keresés után meglelte igazi hely_____ a világban. (his/her place - ét)",
                "answer": "ét"
            },
            {
                "id": "b1-29-05.ex08",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["Az", "igazi", "otthon", "nemcsak", "egy", "hely,", "hanem", "egy", "érzés."],
                "solution": ["Az", "igazi", "otthon", "nemcsak", "egy", "hely,", "hanem", "egy", "érzés."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-29-05-ex.json", ex_05)

    ex_consolidation = {
        "lesson": "b1-29-consolidation",
        "exercises": [
            {
                "id": "b1-29-consolidation.ex01",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik mondatban látunk helyes okhatározói kifejezést?",
                "options": [
                    "A történelmi átalakulások következtében megváltozott az emberek élete.",
                    "A történelmi átalakulások miatt alszik a ház.",
                    "A történelmi átalakulások dacára esik a hó."
                ],
                "correct": 0
            },
            {
                "id": "b1-29-consolidation.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Bár egész Európát bejárta, Márai mindvégig megőrizte hűség_____ a magyar anyanyelvhez. (his fidelity - ét)",
                "answer": "ét"
            },
            {
                "id": "b1-29-consolidation.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "szülőföld", "és", "az", "anyanyelv", "örök", "köteléket", "jelent."],
                "solution": ["A", "szülőföld", "és", "az", "anyanyelv", "örök", "köteléket", "jelent."]
            },
            {
                "id": "b1-29-consolidation.ex04",
                "type": "multiple-choice",
                "category": "literature",
                "question": "Hogyan ábrázolja Márai Sándor az identitást és a polgári kultúrát az 'Egy polgár vallomásaiban'?",
                "options": [
                    "A szigorú erkölcsi tartás, a kassai polgári gyökerek és az európai műveltség elválaszthatatlan egységeként.",
                    "Egy gyorsan elfelejtendő, felesleges gyermekkori álomként.",
                    "Kizárólag anyagi javak és bankbetétek gyűjteményeként."
                ],
                "correct": 0
            },
            {
                "id": "b1-29-consolidation.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A kettős identitás gazdagítja az ember személyiség_____. (his personality - ét)",
                "answer": "ét"
            },
            {
                "id": "b1-29-consolidation.ex06",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "beilleszkedés", "nem", "jelenti", "a", "saját", "gyökerek", "feladását."],
                "solution": ["A", "beilleszkedés", "nem", "jelenti", "a", "saját", "gyökerek", "feladását."]
            },
            {
                "id": "b1-29-consolidation.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A szülőföldjétől távol élve is meglelte a lelki béké_____. (his peace - t)",
                "answer": "t"
            },
            {
                "id": "b1-29-consolidation.ex08",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Mit jelent az a felismerés, hogy az ember igazi hazája az anyanyelve?",
                "options": [
                    "Azt, hogy a határok vagy az országhatárok változhatnak, de a nyelv által hordozott gondolatok és emlékek elvehetetlenek.",
                    "Azt, hogy az embernek nem kell sehol laknia.",
                    "Azt, hogy nem szükséges idegen nyelveket tanulni."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-29-consolidation-ex.json", ex_consolidation)

    # -------------------------------------------------------------------------
    # 4. Classic Story Adaptation for Consolidation: Egy polgár vallomásai
    # -------------------------------------------------------------------------
    story_classic = {
        "id": "story.b1.29.classic",
        "title": "Egy polgár vallomásai",
        "level": "B1",
        "order": 29,
        "type": "classics",
        "estimatedMinutes": 8,
        "summary": "An adaptation of Sándor Márai's immortal autobiographical classic 'Egy polgár vallomásai' (Confessions of a Bourgeois). Raised in the patrician harmony of historic Kassa (Košice), young Márai absorbs the stern European bourgeois virtues: intellectual honesty, civic duty, and devotion to culture. Leaving his native town to wander across Weimar Germany and Paris, he experiences the dislocation of exile, yet discovers that no matter how far he travels, his true, indestructible homeland is the Hungarian language.",
        "characters": [
            "Márai Sándor, az elbeszélő",
            "Az édesapa, tekintélyes kassai közjegyző",
            "A kassai polgárok világa"
        ],
        "location": "Kassa, a Fő utca és Nyugat-Európa nagyvárosai",
        "author": "Márai Sándor",
        "work": "Egy polgár vallomásai (1934)",
        "paragraphs": [
            {
                "type": "narration",
                "text": "A felvidéki Kassa Fő utcáján, a dóm árnyékában évszázados rend uralkodott. A polgári házak hűvös, könyvekkel teli szobáiban komoly tisztelet övezte a munkát, a becsületet és a klasszikus európai műveltséget. Itt nevelkedett Márai Sándor, a királyi közjegyző fia."
            },
            {
                "type": "dialogue",
                "speaker": "Az édesapa",
                "text": "Fiam, a polgári lét nem kiváltság, hanem szigorú felelősség. Nem a pénz teszi az embert polgárrá, hanem az önfegyelem, a műveltség és a közösség iránti rendíthetetlen hűség!"
            },
            {
                "type": "narration",
                "text": "Ám a fiatalembert hajtotta a megismerés vágya. Elhagyta az ősi fészket: Berlinben, Frankfurtban és Párizsban tanult, kávéházakban írt, és a nyugat-európai nagyvárosok lüktető életébe vetette magát. Megismerte a világot, de a vándorlás évei alatt megérezte az idegenség magányát is."
            },
            {
                "type": "dialogue",
                "speaker": "Márai Sándor",
                "text": "Bejártam a kontinenst, láttam a Rajna menti katedrálisokat és a Szajna hídjait. De éjszaka, amikor a papír fölé hajoltam, a mondatok csakis magyarul szólaltak meg bennem. Az anyanyelv volt az egyetlen szilárd talaj a lábam alatt!"
            },
            {
                "type": "narration",
                "text": "A történelmi viharok később örökre elszakították szülővárosától. Ám Márai megértette az emigráció és a vándorlás legmélyebb titkát: az ember igazi szülőföldje nem egyetlen földrajzi pont, hanem a lelkében hordozott kultúra és a tiszta anyanyelv, amit semmilyen határ vagy száműzetés nem vehet el."
            }
        ]
    }
    write_json("content/hu/stories/classics/b1/b1-29-marai.json", story_classic)

    # -------------------------------------------------------------------------
    # 5. Lesson Files (01 to 05 + consolidation)
    # -------------------------------------------------------------------------
    lesson_titles = {
        "01": ("Okok, akadályok és a honvágy", "Reasons for Migration, Obstacles & Homesickness"),
        "02": ("Úti célok, letelepedés és beilleszkedés", "Destinations, Settlement & Integration"),
        "03": ("Két világ között: a kettős identitás", "Between Two Worlds: Dual Identity & Roots"),
        "04": ("Származás, anyanyelv és az emlékőrzés", "Ancestry, Mother Tongue & Cultural Memory"),
        "05": ("Mit jelent az otthon? Biztonság és befogadás", "What Home Means: Belonging & Acceptance")
    }

    grammar_refs = {
        "01": ["grammar/b1/b1-29-01-a-gr.json", "grammar/b1/b1-29-01-b-gr.json"],
        "02": ["grammar/b1/b1-29-02-a-gr.json", "grammar/b1/b1-29-02-b-gr.json"],
        "03": ["grammar/b1/b1-29-03-a-gr.json", "grammar/b1/b1-29-03-b-gr.json"],
        "04": ["grammar/b1/b1-29-04-a-gr.json", "grammar/b1/b1-29-04-b-gr.json"],
        "05": ["grammar/b1/b1-29-05-a-gr.json", "grammar/b1/b1-29-05-b-gr.json"]
    }

    for i in range(1, 6):
        padded = f"0{i}"
        hu_t, en_t = lesson_titles[padded]
        lesson_data = {
            "id": f"lesson.b1.29-{padded}",
            "unit": 29,
            "title": f"{hu_t} ({en_t})",
            "level": "B1",
            "grammar": "Causal & Concessive Postpositions, Identity Correlatives & Narrative Participles in Hungarian",
            "sections": [
                {
                    "type": "goal",
                    "title": "Lesson Goals",
                    "items": [
                        f"I can discuss {en_t} in Hungarian.",
                        "I can use causal and concessive postpositions (miatt, ellenére, folytán, során).",
                        "I can express complex themes of dual identity, homesickness, and belonging.",
                        "I can appreciate Sándor Márai's masterpiece on European bourgeois identity and native language."
                    ]
                },
                {"type": "recycle", "count": 3},
                {"type": "vocabulary", "ref": f"vocabulary/b1/b1-29-{padded}-voc.json"},
                {"type": "grammar", "ref": grammar_refs[padded][0]},
                {"type": "grammar", "ref": grammar_refs[padded][1]},
                {
                    "type": "exercise-group",
                    "title": "Practice",
                    "ref": f"exercises/b1/b1-29-{padded}-ex.json",
                    "exerciseRefs": [f"b1-29-{padded}.ex0{k}" for k in range(1, 9)]
                }
            ]
        }
        write_json(f"content/hu/lessons/b1/b1-29-{padded}.json", lesson_data)

    consolidation_data = {
        "id": "lesson.b1.29-consolidation",
        "unit": 29,
        "title": "Unit 29 Consolidation",
        "level": "B1",
        "grammar": "Consolidation of Migration, Dual Identity, Belonging & Sándor Márai's Memoir",
        "sections": [
            {
                "type": "story",
                "title": "Egy polgár vallomásai (Márai Sándor)",
                "ref": "stories/classics/b1/b1-29-marai.json"
            },
            {
                "type": "exercise-group",
                "title": "Consolidation Practice",
                "ref": "exercises/b1/b1-29-consolidation-ex.json",
                "exerciseRefs": [f"b1-29-consolidation.ex0{k}" for k in range(1, 9)]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-29-consolidation.json", consolidation_data)
    print("Successfully built Hungarian B1 Core Unit 29 (b1-29)!")

if __name__ == "__main__":
    build_unit_29_core()
