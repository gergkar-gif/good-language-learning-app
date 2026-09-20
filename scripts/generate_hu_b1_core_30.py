#!/usr/bin/env python3
"""Generate Hungarian B1 Core Unit 30: Culture, Language & Society (b1-30)."""

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

def build_unit_30_core():
    # -------------------------------------------------------------------------
    # 1. Vocabulary Files (4 words each = 20 words total)
    # -------------------------------------------------------------------------
    voc_01 = {
        "id": "vocab.b1.30.01",
        "lesson": "b1-30-01",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "tulajdonság", "translation": "property, characteristic, attribute", "pos": "noun"},
            {"lemma": "sajátosság", "translation": "peculiarity, unique feature, trait", "pos": "noun"},
            {"lemma": "jellegzetesség", "translation": "distinguishing mark, distinctive characteristic", "pos": "noun"},
            {"lemma": "összefüggés", "translation": "connection, correlation, context", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-30-01-voc.json", voc_01)

    voc_02 = {
        "id": "vocab.b1.30.02",
        "lesson": "b1-30-02",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "kifejezőerő", "translation": "expressive power, eloquence", "pos": "noun"},
            {"lemma": "szókincs", "translation": "vocabulary, lexicon of a language", "pos": "noun"},
            {"lemma": "árnyalat", "translation": "nuance, subtle shade of meaning", "pos": "noun"},
            {"lemma": "nyelvművelés", "translation": "language cultivation, purism, speech refinement", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-30-02-voc.json", voc_02)

    voc_03 = {
        "id": "vocab.b1.30.03",
        "lesson": "b1-30-03",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "népszokás", "translation": "folk custom, popular tradition", "pos": "noun"},
            {"lemma": "hagyományőrzés", "translation": "preservation of traditions, heritage keeping", "pos": "noun"},
            {"lemma": "szertartás", "translation": "ceremony, ritual, solemn rite", "pos": "noun"},
            {"lemma": "nemzedék", "translation": "generation", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-30-03-voc.json", voc_03)

    voc_04 = {
        "id": "vocab.b1.30.04",
        "lesson": "b1-30-04",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "sokszínűség", "translation": "diversity, cultural variety, multifacetedness", "pos": "noun"},
            {"lemma": "kölcsönhatás", "translation": "interaction, mutual influence among cultures", "pos": "noun"},
            {"lemma": "tolerancia", "translation": "tolerance, broad-minded respect", "pos": "noun"},
            {"lemma": "nyitottság", "translation": "openness, receptiveness to new ideas", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-30-04-voc.json", voc_04)

    voc_05 = {
        "id": "vocab.b1.30.05",
        "lesson": "b1-30-05",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "szellemi örökség", "translation": "intellectual / spiritual heritage", "pos": "noun"},
            {"lemma": "értékrend", "translation": "value system, set of moral and social values", "pos": "noun"},
            {"lemma": "összetartozás-érzés", "translation": "feeling of cohesion, community solidarity", "pos": "noun"},
            {"lemma": "kultúraközvetítés", "translation": "cultural mediation, transmission of art and values", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-30-05-voc.json", voc_05)

    # -------------------------------------------------------------------------
    # 2. Grammar Files (2 per regular lesson = 10 files)
    # -------------------------------------------------------------------------
    gr_01_a = {
        "id": "grammar.b1.30.01.chained-relative-clauses",
        "title": "Chained Relative Clauses: az, aki... és ami...",
        "sections": [
            {
                "type": "text",
                "title": "Chaining Demonstratives and Relative Pronouns",
                "content": "Complex descriptive discourse links multiple relative clauses: *Az a könyv, amelyet tavaly olvastam, és amely olyan mély nyomot hagyott bennem...* Note agreement between the head demonstrative (*az, azok*) and relative pronouns (*aki, ami, amely*)."
            },
            {
                "type": "examples",
                "title": "Chained clause examples",
                "items": [
                    {
                        "spanish": "Az az ember, aki tiszteli mások kultúráját, és aki nyitott a világra, igazi polgár.",
                        "english": "That person who respects others' cultures and who is open to the world is a true citizen."
                    },
                    {
                        "spanish": "Azok a hagyományok, amelyeket őseinktől örököltünk, és amelyeket ma is ápolunk, erőt adnak.",
                        "english": "Those traditions that we inherited from our ancestors and that we still cultivate today give strength."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-30-01-a-gr.json", gr_01_a)

    gr_01_b = {
        "id": "grammar.b1.30.01.relative-pronouns-amely-amelyik",
        "title": "Distinguishing 'amely' and 'amelyik'",
        "sections": [
            {
                "type": "text",
                "title": "Literary 'amely' vs Selective 'amelyik'",
                "content": "*Amely* is the formal, literary relative pronoun ('which / that'). *Amelyik* is selective ('which one of several'): *a festmény, amely a falon függ* ('the painting which hangs on the wall') vs *Válaszd azt a könyvet, amelyik a legjobban tetszik!* ('Choose that book which you like best!')."
            },
            {
                "type": "examples",
                "title": "Pronoun distinction examples",
                "items": [
                    {
                        "spanish": "A magyar nyelv gazdag kifejezőereje olyan kincs, amelyet gondosan őriznünk kell.",
                        "english": "The rich expressive power of the Hungarian language is a treasure which we must carefully guard."
                    },
                    {
                        "spanish": "Közülük azt a megoldást választották, amelyik a legkevesebb konfliktussal járt.",
                        "english": "From among them they chose that solution which entailed the fewest conflicts."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-30-01-b-gr.json", gr_01_b)

    gr_02_a = {
        "id": "grammar.b1.30.02.nuances-and-shades-of-meaning",
        "title": "Nuance and Precision: árnyalatnyi különbség, finom",
        "sections": [
            {
                "type": "text",
                "title": "Lexical Precision and Shades of Meaning",
                "content": "*Árnyalatnyi különbség van a két szó között* ('there is a nuanced difference between the two words'), *finom különbséget tesz* ('makes a subtle distinction'), *pontosan és árnyaltan fogalmaz* ('phrases precisely and with nuance')."
            },
            {
                "type": "examples",
                "title": "Nuance examples",
                "items": [
                    {
                        "spanish": "A gazdag szókincs lehetővé teszi, hogy gondolatainkat pontosan és árnyaltan fejezzük ki.",
                        "english": "A rich vocabulary makes it possible to express our thoughts precisely and with nuance."
                    },
                    {
                        "spanish": "Csupán árnyalatnyi eltérés van a két fogalom jelentése között.",
                        "english": "There is merely a nuanced variance between the meanings of the two concepts."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-30-02-a-gr.json", gr_02_a)

    gr_02_b = {
        "id": "grammar.b1.30.02.verbal-adjectives-hatatlan-hetetlen",
        "title": "Privative Potential Participles: -hatatlan / -hetetlen",
        "sections": [
            {
                "type": "text",
                "title": "Adjectives of Unshakeable and Inescapable Quality",
                "content": "The suffix *-hatatlan/-hetetlen* corresponds to '-able/-ible' with negation ('un-...-able'): *felejthetetlen* ('unforgettable'), *megingathatatlan* ('unshakeable'), *megmagyarázhatatlan* ('unexplainable'), *pótolhatatlan* ('irreplaceable')."
            },
            {
                "type": "examples",
                "title": "Participle examples",
                "items": [
                    {
                        "spanish": "Abigél titka és Kőnig tanár úr bátorsága felejthetetlen élményt nyújt az olvasónak.",
                        "english": "The secret of Abigail and teacher Kőnig's bravery provide an unforgettable experience to the reader."
                    },
                    {
                        "spanish": "A lány hite a barátaiban és az igazságban megingathatatlan maradt.",
                        "english": "The girl's faith in her friends and in truth remained unshakeable."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-30-02-b-gr.json", gr_02_b)

    gr_03_a = {
        "id": "grammar.b1.30.03.generational-transmission",
        "title": "Generational Transmission: nemzedékről nemzedékre öröklődik",
        "sections": [
            {
                "type": "text",
                "title": "Expressions of Cultural Continuity",
                "content": "*Nemzedékről nemzedékre száll/öröklődik* ('passes/inherits from generation to generation'), *apáról fiúra száll* ('passes from father to son'), *hagyományozódik* ('gets handed down as tradition')."
            },
            {
                "type": "examples",
                "title": "Continuity examples",
                "items": [
                    {
                        "spanish": "A népdalok és a balladák nemzedékről nemzedékre szálltak a falusi közösségekben.",
                        "english": "Folk songs and ballads passed from generation to generation in village communities."
                    },
                    {
                        "spanish": "A nagymama féltve őrzött receptjei apáról fiúra öröklődtek a családban.",
                        "english": "Grandmother's jealously guarded recipes were passed down from father to son in the family."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-30-03-a-gr.json", gr_03_a)

    gr_03_b = {
        "id": "grammar.b1.30.03.traditional-festive-verbs",
        "title": "Festive Observances: ünnepel, megül, hűen ápol",
        "sections": [
            {
                "type": "text",
                "title": "Observance and Celebration Verbs",
                "content": "*Megüli az ünnepet* ('celebrates the festive occasion'), *hűen ápolja a népszokásokat* ('faithfully cultivates folk customs'), *szertartást végez* ('performs a solemn rite')."
            },
            {
                "type": "examples",
                "title": "Festive examples",
                "items": [
                    {
                        "spanish": "Húsvétkor és karácsonykor a családok hűen ápolják az ősi népszokásokat.",
                        "english": "At Easter and Christmas, families faithfully cultivate ancient folk customs."
                    },
                    {
                        "spanish": "A közösség méltóságteljes szertartás keretében ünnepelte meg az évfordulót.",
                        "english": "The community celebrated the anniversary in the framework of a dignified ceremony."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-30-03-b-gr.json", gr_03_b)

    gr_04_a = {
        "id": "grammar.b1.30.04.cultural-comparison-contrast",
        "title": "Cultural Contrast: eltérően vmitől, ellentétben vmivel",
        "sections": [
            {
                "type": "text",
                "title": "Formulas of Cross-Cultural Comparison",
                "content": "*Eltérően a nyugati szokásoktól* ('differently from Western customs' - ablative *-tól/-től*), *ellentétben más népekkel* ('in contrast to other peoples' - instrumental *-val/-vel*), *összhangban a hagyományokkal* ('in harmony with traditions')."
            },
            {
                "type": "examples",
                "title": "Cultural comparison examples",
                "items": [
                    {
                        "spanish": "Ellentétben a modern fogyasztói kultúrával, a néphagyomány a természet tiszteletére tanít.",
                        "english": "In contrast to modern consumer culture, folk tradition teaches respect for nature."
                    },
                    {
                        "spanish": "A különböző kultúrák közötti párbeszéd gazdagítja a gondolkodásunkat.",
                        "english": "Dialogue among different cultures enriches our thinking."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-30-04-a-gr.json", gr_04_a)

    gr_04_b = {
        "id": "grammar.b1.30.04.mutual-respect-and-tolerance",
        "title": "Mutual Respect: kölcsönös tisztelet övezi, nyitottságot tanúsít",
        "sections": [
            {
                "type": "text",
                "title": "Expressing Tolerance and Openness",
                "content": "*Kölcsönös tiszteletet tanúsít vki iránt* ('shows mutual respect toward sb' - postposition *iránt*), *nyitottsággal fogad* ('receives with openness'), *tiszteletben tartja a másságot* ('respects difference')."
            },
            {
                "type": "examples",
                "title": "Respect examples",
                "items": [
                    {
                        "spanish": "A valódi tolerancia azt jelenti, hogy őszinte tisztelettel fordulunk a másik ember felé.",
                        "english": "True tolerance means turning with sincere respect toward the other person."
                    },
                    {
                        "spanish": "A sokszínű társadalom alapja a kölcsönös megbecsülés és a nyitottság.",
                        "english": "The foundation of a diverse society is mutual esteem and openness."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-30-04-b-gr.json", gr_04_b)

    gr_05_a = {
        "id": "grammar.b1.30.05.values-and-worldview",
        "title": "Value Systems: értékrendet képvisel, értéket tulajdonít",
        "sections": [
            {
                "type": "text",
                "title": "Governing Principles and Worldview",
                "content": "*Szilárd értékrendet képvisel* ('represents a solid value system'), *kiemelt értéket tulajdonít vminek* ('attributes outstanding value to sth' - dative *-nak/-nek*), *hű marad az elveihez* ('remains faithful to principles')."
            },
            {
                "type": "examples",
                "title": "Value system examples",
                "items": [
                    {
                        "spanish": "A matulás nevelés szilárd erkölcsi értékrendet adott a fiatal lányoknak.",
                        "english": "The Matula education provided a solid moral value system to the young girls."
                    },
                    {
                        "spanish": "A közösség nagy értéket tulajdonít a szolidaritásnak és az emberségnek.",
                        "english": "The community attributes great value to solidarity and humanity."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-30-05-a-gr.json", gr_05_a)

    gr_05_b = {
        "id": "grammar.b1.30.05.cultural-mediation",
        "title": "Cultural Mediation: közvetít, hidat képez, hozzáférhetővé tesz",
        "sections": [
            {
                "type": "text",
                "title": "Transmitting Culture and Building Bridges",
                "content": "*Hidat képez a kultúrák között* ('forms a bridge between cultures'), *hozzáférhetővé teszi az irodalmat* ('makes literature accessible'), *kultúrát közvetít* ('mediates culture')."
            },
            {
                "type": "examples",
                "title": "Mediation examples",
                "items": [
                    {
                        "spanish": "A jó műfordító hidat képez két különböző nyelv és gondolkodásmód között.",
                        "english": "A good literary translator forms a bridge between two different languages and mindsets."
                    },
                    {
                        "spanish": "A múzeumok és könyvtárak mindenki számára hozzáférhetővé teszik a nemzeti örökséget.",
                        "english": "Museums and libraries make national heritage accessible to everyone."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-30-05-b-gr.json", gr_05_b)

    # -------------------------------------------------------------------------
    # 3. Exercises Files (6 files = 48 exercises total)
    # -------------------------------------------------------------------------
    ex_01 = {
        "lesson": "b1-30-01",
        "exercises": [
            {
                "id": "b1-30-01.ex01",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent a 'sajátosság' kifejezés?",
                "options": [
                    "Egy olyan egyedi, megkülönböztető tulajdonságot, amely csak az adott dologra vagy kultúrára jellemző.",
                    "A cipőfűző bekötésének módját.",
                    "Egy eldobott műanyag palackot."
                ],
                "correct": 0
            },
            {
                "id": "b1-30-01.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Az az ember, a_____ tiszteli a hagyományokat, méltó a megbecsülésre. (who - ki)",
                "answer": "ki"
            },
            {
                "id": "b1-30-01.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "magyar", "nyelv", "egyik", "fő", "sajátossága", "a", "gazdag", "toldalékrendszer."],
                "solution": ["A", "magyar", "nyelv", "egyik", "fő", "sajátossága", "a", "gazdag", "toldalékrendszer."]
            },
            {
                "id": "b1-30-01.ex04",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik mondatban látunk helyes vonatkozó névmást?",
                "options": [
                    "A regény, amelyet tegnap fejeztem be, mély hatást tett rám.",
                    "A regény, amit tegnap este sétált az erdőben.",
                    "A regény, kivel vacsoráztunk a vendéglőben."
                ],
                "correct": 0
            },
            {
                "id": "b1-30-01.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A kutató világos összefüggés_____ mutatott ki a nyelv és a gondolkodás között. (accusative - t)",
                "answer": "t"
            },
            {
                "id": "b1-30-01.ex06",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent a 'jellegzetesség' szó?",
                "options": [
                    "Olyan szembetűnő vonást, amelyről valami vagy valaki könnyen felismerhető.",
                    "A bolt zárva tartását ünnepnapokon.",
                    "Egy autópálya-matricát."
                ],
                "correct": 0
            },
            {
                "id": "b1-30-01.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Azok a művek, amely_____ kiállják az idő próbáját, klasszikussá válnak. (which - ek)",
                "answer": "ek"
            },
            {
                "id": "b1-30-01.ex08",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "kulturális", "jellegzetességek", "színesítik", "az", "emberiség", "életét."],
                "solution": ["A", "kulturális", "jellegzetességek", "színesítik", "az", "emberiség", "életét."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-30-01-ex.json", ex_01)

    ex_02 = {
        "lesson": "b1-30-02",
        "exercises": [
            {
                "id": "b1-30-02.ex01",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit értünk egy nyelv 'kifejezőerején'?",
                "options": [
                    "Azt a képességet, hogy gondolatainkat, érzelmeinket finoman, pontosan és érzékletesen tudjuk megfogalmazni.",
                    "A szavak hangerejét mikrofonban.",
                    "A betűk nyomtatási méretét az újságban."
                ],
                "correct": 0
            },
            {
                "id": "b1-30-02.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A regény felejthetet_____ élményt nyújtott minden olvasónak. (unforgettable - len)",
                "answer": "len"
            },
            {
                "id": "b1-30-02.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "gazdag", "szókincs", "lehetővé", "teszi", "az", "árnyalt", "fogalmazást."],
                "solution": ["A", "gazdag", "szókincs", "lehetővé", "teszi", "az", "árnyalt", "fogalmazást."]
            },
            {
                "id": "b1-30-02.ex04",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Mit fejez ki a '-hatatlan/-hetetlen' fosztóképzős melléknév?",
                "options": [
                    "Olyan tulajdonságot, amely el nem múló, meg nem változtatható (pl. megingathatatlan, pótolhatatlan).",
                    "A cselekvés gyorsaságát a jövőben.",
                    "A színek fényességét a festményen."
                ],
                "correct": 0
            },
            {
                "id": "b1-30-02.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A két rokonértelmű szó között csupán finom árnyal_____ van. (stem suffix - at)",
                "answer": "at"
            },
            {
                "id": "b1-30-02.ex06",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mi a 'nyelvművelés' fő célja?",
                "options": [
                    "A nyelv tisztaságának, szépségének és helyes használatának ápolása és fejlesztése.",
                    "A régi szótárak elégetése.",
                    "Minden idegen szó kötelező betiltása a magánbeszélgetésekben."
                ],
                "correct": 0
            },
            {
                "id": "b1-30-02.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A tudós megingathatat_____ hittel dolgozott a kutatásán. (unshakeable - lan)",
                "answer": "lan"
            },
            {
                "id": "b1-30-02.ex08",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "szavak", "pontos", "használata", "az", "igényes", "gondolkodás", "tükre."],
                "solution": ["A", "szavak", "pontos", "használata", "az", "igényes", "gondolkodás", "tükre."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-30-02-ex.json", ex_02)

    ex_03 = {
        "lesson": "b1-30-03",
        "exercises": [
            {
                "id": "b1-30-03.ex01",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent a 'hagyományőrzés' egy közösség életében?",
                "options": [
                    "Az ősi szokások, dalok, mesék és mesterségek továbbadását a jövő nemzedékeknek.",
                    "A múzeumok bezárását hétvégén.",
                    "A naptárak lecserélését minden hónapban."
                ],
                "correct": 0
            },
            {
                "id": "b1-30-03.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A népszokások nemzedékről nemzedék_____ szálltak az évszázadok során. (sublative - re)",
                "answer": "re"
            },
            {
                "id": "b1-30-03.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "falusi", "közösségek", "hűen", "megőrizték", "az", "ünnepi", "szertartásokat."],
                "solution": ["A", "falusi", "közösségek", "hűen", "megőrizték", "az", "ünnepi", "szertartásokat."]
            },
            {
                "id": "b1-30-03.ex04",
                "type": "multiple-choice",
                "category": "culture",
                "question": "Melyik híres magyar népszokás kapcsolódik a húsvét hétfőhöz?",
                "options": [
                    "A húsvéti locsolkodás és a hímes tojás ajándékozása.",
                    "A busójárás és télbúcsúztatás.",
                    "A szüreti felvonulás ősszel."
                ],
                "correct": 0
            },
            {
                "id": "b1-30-03.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A karácsonyi szertartás meghitt pillanatot jelentett a család száma_____. (for them - ra)",
                "answer": "ra"
            },
            {
                "id": "b1-30-03.ex06",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent a 'nemzedék' szó?",
                "options": [
                    "A nagyjából egy időben született, hasonló történelmi és társadalmi élményeket átélő korosztályt.",
                    "Egy háromnapos kirándulást a hegyekbe.",
                    "A vasúti menetrendet."
                ],
                "correct": 0
            },
            {
                "id": "b1-30-03.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A népdalok apáról fiú_____ öröklődtek a családokban. (sublative - ra)",
                "answer": "ra"
            },
            {
                "id": "b1-30-03.ex08",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "hagyományok", "összekötik", "a", "múltat", "a", "jelennel."],
                "solution": ["A", "hagyományok", "összekötik", "a", "múltat", "a", "jelennel."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-30-03-ex.json", ex_03)

    ex_04 = {
        "lesson": "b1-30-04",
        "exercises": [
            {
                "id": "b1-30-04.ex01",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent a kulturális 'sokszínűség' értéke?",
                "options": [
                    "Különböző hagyományok, nyelvek és látásmódok békés és gazdagító együttélését a társadalomban.",
                    "Kizárólag színes ruhák viselését tavasszal.",
                    "A televíziós csatornák gyakori váltogatását."
                ],
                "correct": 0
            },
            {
                "id": "b1-30-04.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Ellentétben a bezárkózással, a nyitottság új távlatokat nyi_____. (opens - t)",
                "answer": "t"
            },
            {
                "id": "b1-30-04.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "kultúrák", "közötti", "párbeszéd", "kölcsönös", "tiszteleten", "alapszik."],
                "solution": ["A", "kultúrák", "közötti", "párbeszéd", "kölcsönös", "tiszteleten", "alapszik."]
            },
            {
                "id": "b1-30-04.ex04",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Hogyan fejezzük ki helyesen a tiszteletet valaki iránt?",
                "options": [
                    "Kölcsönös tiszteletet tanúsít a másik iránt.",
                    "Kölcsönös tiszteletet alszik a másikhoz.",
                    "Kölcsönös tiszteletben repül a másikról."
                ],
                "correct": 0
            },
            {
                "id": "b1-30-04.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A különböző népek kölcsönhatás_____ formálta a Kárpát-medence gazdag kultúráját. (its interaction - a)",
                "answer": "a"
            },
            {
                "id": "b1-30-04.ex06",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent az igazi 'tolerancia' a mindennapi életben?",
                "options": [
                    "A másik ember véleményének, hitének és másságának békés tiszteletben tartását.",
                    "A hangos zenehallgatást az éjszaka közepén.",
                    "A kötelező egyetértést minden vitában."
                ],
                "correct": 0
            },
            {
                "id": "b1-30-04.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Eltérően más országok szokásai_____, nálunk a névnapokat is megünnepeljük. (ablative - tól)",
                "answer": "tól"
            },
            {
                "id": "b1-30-04.ex08",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "nyitottság", "és", "a", "tisztelet", "békés", "együttélést", "teremt."],
                "solution": ["A", "nyitottság", "és", "a", "tisztelet", "békés", "együttélést", "teremt."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-30-04-ex.json", ex_04)

    ex_05 = {
        "lesson": "b1-30-05",
        "exercises": [
            {
                "id": "b1-30-05.ex01",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mit jelent a társadalmi 'értékrend' fogalma?",
                "options": [
                    "Azoknak az erkölcsi és szellemi elveknek az összességét, amelyek vezérlik döntéseinket és cselekedeteinket.",
                    "A banki árfolyamok listáját a kijelzőn.",
                    "Az élelmiszerbolt árcéduláinak sorrendjét."
                ],
                "correct": 0
            },
            {
                "id": "b1-30-05.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A műfordítás hidat képez a nemzetek kultúrája közöt_____. (postposition - t)",
                "answer": "t"
            },
            {
                "id": "b1-30-05.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["A", "közösség", "kiemelt", "értéket", "tulajdonít", "a", "szolidaritásnak."],
                "solution": ["A", "közösség", "kiemelt", "értéket", "tulajdonít", "a", "szolidaritásnak."]
            },
            {
                "id": "b1-30-05.ex04",
                "type": "multiple-choice",
                "category": "literature",
                "question": "Ki volt valójában 'Abigél' Szabó Magda híres regényében?",
                "options": [
                    "Kőnig tanár úr, a látszólag szelíd latin tanár, aki titokban emberéleteket mentett.",
                    "Egy életre kelt kerti kőszobor.",
                    "A Matula leányintézet igazgatónője."
                ],
                "correct": 0
            },
            {
                "id": "b1-30-05.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A nemzeti összetartozás-érzés erőt ad a nehéz idők_____. (inessive - ben)",
                "answer": "ben"
            },
            {
                "id": "b1-30-05.ex06",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Mit tanul meg Vitay Gina a Matula zárt intézetében töltött hónapok alatt?",
                "options": [
                    "Hogy az önzés helyét az összetartásnak, a bajtársiasságnak és az igaz emberi jóságnak kell átvennie.",
                    "Hogy jobb lett volna megszöknie Amerikába.",
                    "Hogy a latin nyelv felesleges tantárgy."
                ],
                "correct": 0
            },
            {
                "id": "b1-30-05.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A könyvtárak hozzáférhetővé teszik az irodalmat mindenki számá_____. (for them - ra)",
                "answer": "ra"
            },
            {
                "id": "b1-30-05.ex08",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "szellemi", "örökség", "megőrzése", "mindannyiunk", "közös", "felelőssége."],
                "solution": ["A", "szellemi", "örökség", "megőrzése", "mindannyiunk", "közös", "felelőssége."]
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-30-05-ex.json", ex_05)

    ex_consolidation = {
        "lesson": "b1-30-consolidation",
        "exercises": [
            {
                "id": "b1-30-consolidation.ex01",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik mondatban látunk helyesen egymásba fűzött vonatkozó mellékmondatokat?",
                "options": [
                    "Az az ember, aki becsüli az anyanyelvét, és aki nyitott más kultúrákra, tiszteletet érdemel.",
                    "Az az ember, aki alszik a házban, és hogy holnap esik az eső.",
                    "Az az ember, miért jött el a partira tegnap délután."
                ],
                "correct": 0
            },
            {
                "id": "b1-30-consolidation.ex02",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Gina meglelte igazi helyét a közösségben, amely befogadta ő_____. (her - t)",
                "answer": "t"
            },
            {
                "id": "b1-30-consolidation.ex03",
                "type": "sentence-builder",
                "category": "grammar",
                "tiles": ["Kőnig", "tanár", "úr", "önfeláldozó", "bátorsága", "példát", "mutat", "mindannyiunknak."],
                "solution": ["Kőnig", "tanár", "úr", "önfeláldozó", "bátorsága", "példát", "mutat", "mindannyiunknak."]
            },
            {
                "id": "b1-30-consolidation.ex04",
                "type": "multiple-choice",
                "category": "literature",
                "question": "Hogyan ábrázolja Szabó Magda a valódi hősiességet az 'Abigél' című regényben?",
                "options": [
                    "Nem a hangos kérkedésben, hanem a csendes, önfeláldozó és veszélyeket vállaló segítőkészségben.",
                    "A katonai kardforgatásban és a parancsolgatásban.",
                    "A pénz felhalmozásában és a gazdagság mutogatásában."
                ],
                "correct": 0
            },
            {
                "id": "b1-30-consolidation.ex05",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A szilárd értékrend vezérli a közösség tagjait a nehéz próbatételek ide_____. (at its time - jén)",
                "answer": "jén"
            },
            {
                "id": "b1-30-consolidation.ex06",
                "type": "sentence-builder",
                "category": "vocabulary",
                "tiles": ["A", "kultúra", "és", "a", "nyelv", "a", "nemzet", "legdrágább", "kincse."],
                "solution": ["A", "kultúra", "és", "a", "nyelv", "a", "nemzet", "legdrágább", "kincse."]
            },
            {
                "id": "b1-30-consolidation.ex07",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A népszokások ápolása révén megerősödik a nemzeti összetartozás érzé_____. (its feeling - se)",
                "answer": "se"
            },
            {
                "id": "b1-30-consolidation.ex08",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Mit jelent az 'Abigél-szobor' legendája a diáklányok számára?",
                "options": [
                    "A jóság, a segítség és a vigasztalás reményét, amelyhez baj esetén bizalommal fordulhatnak.",
                    "Egy múzeumi kőfaragványt, amihez nem szabad hozzáérni.",
                    "Egy postaállomást a város szélén."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-30-consolidation-ex.json", ex_consolidation)

    # -------------------------------------------------------------------------
    # 4. Classic Story Adaptation for Consolidation: Abigél
    # -------------------------------------------------------------------------
    story_classic = {
        "id": "story.b1.30.classic",
        "title": "Abigél",
        "level": "B1",
        "order": 30,
        "type": "classics",
        "estimatedMinutes": 8,
        "summary": "An adaptation of Magda Szabó's universally beloved masterpiece 'Abigél' (Abigail). Set in 1943-44, the pampered Budapest general's daughter Gina Vitay is abruptly hidden in the strict Calvinist girls' boarding school 'Matula' in the eastern fortress town of Árkod. Rebellious at first, Gina slowly discovers that behind the school's austere discipline lies profound humanity. When mortal danger closes in, Gina discovers that the legendary miracle-working statue 'Abigél'—who secretly assists desperate girls—is actually the gentle, mocked Latin teacher Kőnig, an unheralded hero saving innocent lives from the horrors of war.",
        "characters": [
            "Vitay Gina, elkényeztetett, majd megedződött diáklány",
            "Kőnig tanár úr, a Matula szelíd latin tanára (a titkos Abigél)",
            "Zsuzsanna testvér, szigorú diakonissza nevelő",
            "Torma Piroska, hűséges osztálytárs"
        ],
        "location": "Árkod, a Matula leánynevelő intézet és a park",
        "author": "Szabó Magda",
        "work": "Abigél (1970)",
        "paragraphs": [
            {
                "type": "narration",
                "text": "1943 őszén a tizenöt éves Vitay Ginát édesapja, a magyar katonai ellenállásban részt vevő tábornok váratlanul kiszakította ragyogó budapesti életéből. A háború veszélyei elől a távoli Árkodra, a Matula református leánynevelő intézet zord falai közé rejtette el."
            },
            {
                "type": "narration",
                "text": "A kislány lázadt a szigorú szabályok, az egyenruha és a zárt világ ellen. Összeveszett osztálytársaival, és gőgösen elutasította a lányok szent titkát: a kertben álló kőszobrot, Abigélt, akinek korsójába a bajba jutott diákok levelet rejtettek, s a titokzatos jótevő mindig segített rajtuk."
            },
            {
                "type": "dialogue",
                "speaker": "Vitay Gina",
                "text": "Gyerekes butaság az egész! Egy kőszobor nem tud segíteni senkin! Én katonalány vagyok, nem hiszek a tündérmesékben!"
            },
            {
                "type": "narration",
                "text": "Amikor azonban édesapja életveszélybe került, és a Gestapo megjelent Magyarországon, Gina megértette apja szavait. Egyedül maradt a világban, s kétségbeesésében maga is levelet írt Abigélnek. Csodák csodájára a válasz megérkezett: pontos utasítások, hamis iratok és megmentő kéz segítette át a halálos veszélyeken."
            },
            {
                "type": "dialogue",
                "speaker": "Kőnig tanár úr",
                "text": "Ne félj, Gina... Amíg én élek, senki sem árthat neked. Az igazi jóság nem csinál zajt, csak csendben teszi a dolgát, amikor a legnagyobb a sötétség."
            },
            {
                "type": "narration",
                "text": "A döntő pillanatban, a menekülés éjszakáján hullott le a lepel: Abigél nem kőszobor volt, hanem a Matula legszelídebb, a diákok által sokat gúnyolt latin tanára, Kőnig úr, aki az életét kockáztatva mentette az üldözötteket."
            },
            {
                "type": "narration",
                "text": "Gina megrendülten borult le a tanár úr nagysága előtt. A dacos úrilány felnőtt nővé érett: megtanulta, hogy a kultúra, a szeretet és az önfeláldozó emberség a legfényesebb fegyver a világ minden kegyetlenségével szemben."
            }
        ]
    }
    write_json("content/hu/stories/classics/b1/b1-30-szabo.json", story_classic)

    # -------------------------------------------------------------------------
    # 5. Lesson Files (01 to 05 + consolidation)
    # -------------------------------------------------------------------------
    lesson_titles = {
        "01": ("Összetett összefüggések és tulajdonságok", "Complex Relations & Distinguishing Characteristics"),
        "02": ("A nyelv kifejezőereje és a szókincs gazdagsága", "Expressive Power of Language & Nuance"),
        "03": ("Népszokások, szertartások és hagyományőrzés", "Folk Customs, Rituals & Generational Transmission"),
        "04": ("Kultúrák találkozása, sokszínűség és tolerancia", "Intercultural Dialogue, Diversity & Mutual Respect"),
        "05": ("Közös értékek, szellemi örökség és identitás", "Shared Values, Spiritual Heritage & Cultural Mediation")
    }

    grammar_refs = {
        "01": ["grammar/b1/b1-30-01-a-gr.json", "grammar/b1/b1-30-01-b-gr.json"],
        "02": ["grammar/b1/b1-30-02-a-gr.json", "grammar/b1/b1-30-02-b-gr.json"],
        "03": ["grammar/b1/b1-30-03-a-gr.json", "grammar/b1/b1-30-03-b-gr.json"],
        "04": ["grammar/b1/b1-30-04-a-gr.json", "grammar/b1/b1-30-04-b-gr.json"],
        "05": ["grammar/b1/b1-30-05-a-gr.json", "grammar/b1/b1-30-05-b-gr.json"]
    }

    for i in range(1, 6):
        padded = f"0{i}"
        hu_t, en_t = lesson_titles[padded]
        lesson_data = {
            "id": f"lesson.b1.30-{padded}",
            "unit": 30,
            "title": f"{hu_t} ({en_t})",
            "level": "B1",
            "grammar": "Chained Relative Clauses, Privative Participles & Cultural Discourse in Hungarian",
            "sections": [
                {
                    "type": "goal",
                    "title": "Lesson Goals",
                    "items": [
                        f"I can understand and discuss {en_t} in Hungarian.",
                        "I can construct chained relative clauses (amely, amelyik, aki) and privative adjectives (-hatatlan/-hetetlen).",
                        "I can express cultural traditions, intercultural dialogue, and moral value systems.",
                        "I can appreciate Magda Szabó's celebrated novel 'Abigél' and its themes of solidarity and sacrifice."
                    ]
                },
                {"type": "recycle", "count": 3},
                {"type": "vocabulary", "ref": f"vocabulary/b1/b1-30-{padded}-voc.json"},
                {"type": "grammar", "ref": grammar_refs[padded][0]},
                {"type": "grammar", "ref": grammar_refs[padded][1]},
                {
                    "type": "exercise-group",
                    "title": "Practice",
                    "ref": f"exercises/b1/b1-30-{padded}-ex.json",
                    "exerciseRefs": [f"b1-30-{padded}.ex0{k}" for k in range(1, 9)]
                }
            ]
        }
        write_json(f"content/hu/lessons/b1/b1-30-{padded}.json", lesson_data)

    consolidation_data = {
        "id": "lesson.b1.30-consolidation",
        "unit": 30,
        "title": "Unit 30 Consolidation",
        "level": "B1",
        "grammar": "Consolidation of Cultural Discourse, Language Nuance & Magda Szabó's Abigél",
        "sections": [
            {
                "type": "story",
                "title": "Abigél (Szabó Magda)",
                "ref": "stories/classics/b1/b1-30-szabo.json"
            },
            {
                "type": "exercise-group",
                "title": "Consolidation Practice",
                "ref": "exercises/b1/b1-30-consolidation-ex.json",
                "exerciseRefs": [f"b1-30-consolidation.ex0{k}" for k in range(1, 9)]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-30-consolidation.json", consolidation_data)
    print("Successfully built Hungarian B1 Core Unit 30 (b1-30)!")

if __name__ == "__main__":
    build_unit_30_core()
