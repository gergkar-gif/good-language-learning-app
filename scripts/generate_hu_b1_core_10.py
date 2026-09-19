#!/usr/bin/env python3
"""Generate Hungarian B1 Core Unit 10: Home & Housing (b1-10)."""

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

def build_unit_10_core():
    # -------------------------------------------------------------------------
    # 1. Vocabulary Files (4 words each = 20 words total)
    # -------------------------------------------------------------------------
    voc_01 = {
        "id": "vocab.b1.10.01",
        "lesson": "b1-10-01",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "felújítás", "translation": "renovation, refurbishment", "pos": "noun"},
            {"lemma": "átalakítás", "translation": "remodeling, conversion", "pos": "noun"},
            {"lemma": "hangulat", "translation": "atmosphere, ambiance", "pos": "noun"},
            {"lemma": "világítás", "translation": "lighting", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-10-01-voc.json", voc_01)

    voc_02 = {
        "id": "vocab.b1.10.02",
        "lesson": "b1-10-02",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "társasház", "translation": "apartment block, condominium", "pos": "noun"},
            {"lemma": "családi ház", "translation": "detached house, family home", "pos": "noun"},
            {"lemma": "erkély", "translation": "balcony", "pos": "noun"},
            {"lemma": "udvar", "translation": "courtyard, yard", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-10-02-voc.json", voc_02)

    voc_03 = {
        "id": "vocab.b1.10.03",
        "lesson": "b1-10-03",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "bérleti szerződés", "translation": "lease agreement, rental contract", "pos": "noun"},
            {"lemma": "főbérlő", "translation": "landlord, property owner", "pos": "noun"},
            {"lemma": "kaució", "translation": "security deposit", "pos": "noun"},
            {"lemma": "rezsi", "translation": "utilities, maintenance costs", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-10-03-voc.json", voc_03)

    voc_04 = {
        "id": "vocab.b1.10.04",
        "lesson": "b1-10-04",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "berendezés", "translation": "furnishing, furniture, interior", "pos": "noun"},
            {"lemma": "elrendezés", "translation": "layout, arrangement", "pos": "noun"},
            {"lemma": "tároló", "translation": "storage room, locker", "pos": "noun"},
            {"lemma": "sarok", "translation": "corner", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-10-04-voc.json", voc_04)

    voc_05 = {
        "id": "vocab.b1.10.05",
        "lesson": "b1-10-05",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "élhető", "translation": "livable", "pos": "adjective"},
            {"lemma": "környék", "translation": "neighborhood, surroundings", "pos": "noun"},
            {"lemma": "fűtés", "translation": "heating", "pos": "noun"},
            {"lemma": "szigetelés", "translation": "insulation", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-10-05-voc.json", voc_05)

    # -------------------------------------------------------------------------
    # 2. Grammar Files
    # -------------------------------------------------------------------------
    gr_01_a = {
        "id": "grammar.b1.10.01.translative-case",
        "title": "The Translative Case: -vá / -vé (Transformation & Becoming)",
        "sections": [
            {
                "type": "text",
                "title": "Expressing transformation into a state or object",
                "content": "The translative case suffix *-vá / -vé* denotes changing or turning into something (*otthonná alakít* = convert into a home; *szebbé tesz* = make prettier). If the noun ends in a consonant, the *v* assimilates to that consonant: *ház + -vá = házzá*, *lakás + -vá = lakássá*, *kert + -vé = kertté*."
            },
            {
                "type": "examples",
                "title": "Translative case examples",
                "items": [
                    {
                        "spanish": "A festéssel és új bútorokkal igazi otthonná varázsolták a lakást.",
                        "english": "With painting and new furniture, they turned the apartment into a real home."
                    },
                    {
                        "spanish": "A régi műhelyt kényelmes dolgozószobává alakították át.",
                        "english": "They converted the old workshop into a comfortable study."
                    },
                    {
                        "spanish": "A jó világítás sokkal melegebbé és barátságosabbá teszi a nappalit.",
                        "english": "Good lighting makes the living room much warmer and friendlier."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-10-01-a-gr.json", gr_01_a)

    gr_01_b = {
        "id": "grammar.b1.10.01.valik-tesz",
        "title": "Verbs of Transformation: válik valamivé vs. tesz valamivé",
        "sections": [
            {
                "type": "text",
                "title": "Intransitive 'válik' vs. Transitive 'tesz'",
                "content": "Notice the pair: *valami válik valamivé* (intransitive: something becomes something, e.g., *a ház otthonná válik*), while *valaki tesz valamit valamivé* (transitive: someone makes/turns something into something, e.g., *a növények otthonossá teszik a szobát*)."
            },
            {
                "type": "examples",
                "title": "Transformation verb examples",
                "items": [
                    {
                        "spanish": "A gondos felújítás után az épület igazi gyöngyszemmé vált.",
                        "english": "After careful renovation, the building became a real gem."
                    },
                    {
                        "spanish": "A meleg színek kellemessé teszik a belső hangulatot.",
                        "english": "Warm colors make the interior atmosphere pleasant."
                    },
                    {
                        "spanish": "Az évek során a kis ház szűkké vált a növekvő család számára.",
                        "english": "Over the years, the small house became too tight for the growing family."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-10-01-b-gr.json", gr_01_b)

    gr_02 = {
        "id": "grammar.b1.10.02.relative-pronouns-housing",
        "title": "Relative Pronouns with Inanimate Objects and Places: amely, ami, amiben, ahol",
        "sections": [
            {
                "type": "text",
                "title": "Connecting descriptions of dwellings and rooms",
                "content": "When describing apartments and features, use relative pronouns: *amely / ami* (which / that), inflected with case suffixes such as *amiben* (in which), *amire* (onto which), or place relative adverb *ahol* (where). In formal Hungarian, *amely* is preferred for specific nouns, while *ami* refers to clauses or indefinite antecedents."
            },
            {
                "type": "examples",
                "title": "Housing relative clause examples",
                "items": [
                    {
                        "spanish": "Keresünk egy olyan társasházi lakást, amely csendes udvarra néz.",
                        "english": "We are looking for a condominium apartment that overlooks a quiet courtyard."
                    },
                    {
                        "spanish": "Ez az a tágas erkély, ahol reggelente szívesen kávézunk.",
                        "english": "This is the spacious balcony where we like to drink coffee in the mornings."
                    },
                    {
                        "spanish": "Olyan családi házat szeretnénk, amiben legalább három hálószoba található.",
                        "english": "We would like a detached family home in which at least three bedrooms are found."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-10-02-gr.json", gr_02)

    gr_03 = {
        "id": "grammar.b1.10.03.tenancy-conditions",
        "title": "Tenancy Rights & Contractual Conditions: köteles, jogosult, esetén",
        "sections": [
            {
                "type": "text",
                "title": "Formal Language of Rental Agreements",
                "content": "Rental contracts (*bérleti szerződés*) use legal expressions: *köteles* (+ infinitive: is obliged to), *jogosult* (+ infinitive / *-ra*: is entitled to), and *esetén* (+ noun: in case of, e.g., *késedelem esetén* = in case of delay)."
            },
            {
                "type": "examples",
                "title": "Tenancy contract examples",
                "items": [
                    {
                        "spanish": "A bérlő köteles a bérleti díjat minden hónap tizedik napjáig átutalni.",
                        "english": "The tenant is obliged to transfer the rent by the tenth day of each month."
                    },
                    {
                        "spanish": "A szerződés aláírásakor két havi kaució fizetendő a főbérlőnek.",
                        "english": "Upon signing the contract, a two-month security deposit must be paid to the landlord."
                    },
                    {
                        "spanish": "Bármilyen műszaki hiba esetén a bérlő haladéktalanul értesíti a tulajdonost.",
                        "english": "In case of any technical defect, the tenant shall immediately notify the owner."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-10-03-gr.json", gr_03)

    gr_04 = {
        "id": "grammar.b1.10.04.interior-postpositions",
        "title": "Interior Spatial Postpositions with Personal Suffixes: mellette, fölötte, alatta, mögötte",
        "sections": [
            {
                "type": "text",
                "title": "Locating Furniture and Spatial Relations",
                "content": "When detailing layout, spatial postpositions inflect with 3rd-person singular possessive suffixes: *mellett* -> *mellette* (next to it), *fölött* -> *fölötte* (above it), *alatt* -> *alatta* (under it), *mögött* -> *mögötte* (behind it), *között* -> *közöttük* (between them)."
            },
            {
                "type": "examples",
                "title": "Interior layout examples",
                "items": [
                    {
                        "spanish": "Az íróasztal a sarokban áll, mellette van a könyvespolc.",
                        "english": "The desk stands in the corner; next to it is the bookshelf."
                    },
                    {
                        "spanish": "A kanapé kényelmes, fölötte egy szép festmény függ a falon.",
                        "english": "The sofa is comfortable; above it hangs a beautiful painting on the wall."
                    },
                    {
                        "spanish": "A konyha és a nappali egybenyílik, köztük csak egy alacsony pult található.",
                        "english": "The kitchen and living room open into each other; between them is only a low counter."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-10-04-gr.json", gr_04)

    gr_05 = {
        "id": "grammar.b1.10.05.ideal-home-synthesis",
        "title": "Synthesizing Housing Preferences: Számomra fontos, hogy...",
        "sections": [
            {
                "type": "text",
                "title": "Stating housing criteria and lifestyle compatibility",
                "content": "Expressing your housing ideals combines opinion structures (*számomra a legfontosabb szempont az, hogy...* + subjunctive) with physical specifications (*korszerű szigetelés, alacsony rezsi, zöld környezet*)."
            },
            {
                "type": "examples",
                "title": "Housing preference synthesis examples",
                "items": [
                    {
                        "spanish": "Számomra elengedhetetlen, hogy a lakás energiatakarékos fűtéssel és modern szigeteléssel rendelkezzen.",
                        "english": "For me, it is essential that the apartment has energy-efficient heating and modern insulation."
                    },
                    {
                        "spanish": "Egy élhető környéken szeretnénk lakni, ahol sok a park és jó a tömegközlekedés.",
                        "english": "We would like to live in a livable neighborhood where there are many parks and good public transit."
                    },
                    {
                        "spanish": "Ideális esetben a lakáshoz külön tároló és kényelmes terasz is tartozik.",
                        "english": "In an ideal case, a separate storage unit and a comfortable terrace also belong to the apartment."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-10-05-gr.json", gr_05)

    # -------------------------------------------------------------------------
    # 3. Classic Literature Story
    # -------------------------------------------------------------------------
    classic_story = {
        "id": "story.b1.10.classic",
        "title": "Édes Anna a Krisztinavárosban",
        "level": "B1",
        "lesson": 5,
        "order": 5,
        "type": "classics",
        "estimatedMinutes": 7,
        "characters": [
            "Vizyné",
            "Anna"
        ],
        "grammar": [
            "translative-case",
            "interior-postpositions",
            "ideal-home-synthesis"
        ],
        "vocabularyTopics": [
            "home",
            "bourgeois-flat",
            "literature",
            "housework"
        ],
        "summary": "In this adapted excerpt from Dezső Kosztolányi's masterpiece Édes Anna, Mrs. Vizy meticulously inspects the spotless bourgeois flat in Krisztinaváros before the quiet country girl Anna steps across the threshold into her new home.",
        "source": "Adaptation inspired by the public-domain work Édes Anna by Dezső Kosztolányi",
        "paragraphs": [
            {"type": "narration", "text": "A krisztinavárosi bérház második emeletén tágas, tiszta polgári lakásban élt Vizy Kornél miniszteri tanácsos és felesége."},
            {"type": "narration", "text": "Vizyné asszony hetek óta másról sem beszélt, csak a tökéletes cselédlányról, akit a rokonai ajánlottak neki Balatonfőkajárról."},
            {"type": "narration", "text": "Amikor Anna megérkezett a vasútállomásról, szerény kis kendőjével és csomagjával megállt a tágas előszoba küszöbén."},
            {"type": "dialogue", "speaker": "Vizyné", "text": "Lépj be bátran, édes leányom! Nézz körül alaposan: itt minden szoba tiszta és rendes."},
            {"type": "narration", "text": "Anna bátortalanul tekintett körbe: a sötét, lakkozott parketta úgy csillogott, mint a tükör, a sarokban nagy állóóra ketyegett."},
            {"type": "dialogue", "speaker": "Anna", "text": "Nagyon szép a tetszős lakás, nagyságos asszonyom. Igyekezni fogok, hogy mindig ilyen tiszta maradjon."},
            {"type": "narration", "text": "Vizyné asszony büszkén mutatta meg a kis cselédszobát és a konyhát, miközben érezte, hogy a háza végre valódi otthonná válik."}
        ]
    }
    write_json("content/hu/stories/classics/b1/b1-10-edesanna.json", classic_story)

    # -------------------------------------------------------------------------
    # 4. Exercise Files
    # -------------------------------------------------------------------------
    ex_01 = {
        "lesson": "b1-10-01",
        "exercises": [
            {
                "id": "b1-10-01-intro-1",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["felújítás", "renovation"],
                    ["átalakítás", "remodeling / conversion"],
                    ["hangulat", "atmosphere / mood"],
                    ["világítás", "lighting"]
                ]
            },
            {
                "id": "b1-10-01-intro-2",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["otthonná", "into a home"],
                    ["házzá", "into a house"],
                    ["szebbé", "into prettier / making nicer"],
                    ["világosabbá", "into brighter"]
                ]
            },
            {
                "id": "b1-10-01-controlled-1",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Hogyan alakul a 'ház' szó translativus (eredményhatározói) alakja?",
                "options": ["házzá", "házvá", "házvé"],
                "correct": 0
            },
            {
                "id": "b1-10-01-controlled-2",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik alak helyes: „A gondos munka valódi otthon______ varázsolta a helyiséget.”?",
                "options": ["otthonná", "otthonvá", "otthonnak"],
                "correct": 0
            },
            {
                "id": "b1-10-01-controlled-3",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik mondatban szerepel helyesen a 'válik' ige?",
                "options": [
                    "A régi lakás az átalakítás után modernné vált.",
                    "A régi lakás az átalakítás után modernné tett.",
                    "A régi lakás az átalakítás után modernné válogatott."
                ],
                "correct": 0
            },
            {
                "id": "b1-10-01-controlled-4",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Milyen mássalhangzó-hasonulás történik a -vá / -vé ragban, ha a szó mássalhangzóra végződik?",
                "options": [
                    "A 'v' teljesen hasonul a szóvégi mássalhangzóhoz (pl. lakás + -vá = lakássá).",
                    "A 'v' kiesik és semmi sem pótolja.",
                    "A szóvégi mássalhangzó mindig megváltozik 't' betűre."
                ],
                "correct": 0
            },
            {
                "id": "b1-10-01-practice-1",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Az új lámpák sokkal melegebbé és barátságosabbá teszik a lakás ____. (atmosphere)",
                "answer": "hangulatát"
            },
            {
                "id": "b1-10-01-practice-2",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A tulajdonosok az egykori padlást hangulatos vendégszobá____ alakították át. (into - translative)",
                "answer": "vá"
            },
            {
                "id": "b1-10-01-practice-3",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Mire utal a mondat: „A felújítás során lecserélték a teljes villanyhálózatot és a világítást.”?",
                "options": [
                    "Korszerűsítették az áramvezetékeket és a lámpatesteket.",
                    "Csak a falakat festették újra.",
                    "Eladták a bútorokat."
                ],
                "correct": 0
            },
            {
                "id": "b1-10-01-practice-4",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Mi a különbség a 'felújítás' és az 'átalakítás' között?",
                "options": [
                    "A felújítás a meglévő állapot megújítását, az átalakítás pedig a funkció vagy térszerkezet megváltoztatását jelenti.",
                    "Semmi különbség nincs, a két szó pontosan azonos.",
                    "Az átalakítás csak kerti munkát jelent."
                ],
                "correct": 0
            },
            {
                "id": "b1-10-01-dialogue-1",
                "type": "multiple-choice",
                "category": "reading",
                "question": "— Sikerült már befejeznetek a felújítást?\n— Igen, a múlt héten végeztünk, és a nappali végre kellemes, világos térré ______.",
                "options": ["vált", "tett", "hozott"],
                "correct": 0
            },
            {
                "id": "b1-10-01-dialogue-2",
                "type": "multiple-choice",
                "category": "reading",
                "question": "— Mitől olyan otthonos ez a sarok?\n— A lágy rejtett ______ és a kényelmes fotel teszi azzá.",
                "options": ["világítás", "szerződés", "főbérlő"],
                "correct": 0
            },
            {
                "id": "b1-10-01-writing-1",
                "type": "fill-blank",
                "category": "production",
                "sentence": "A házaspár a régi parasztházat gyönyörű nyaraló____ varázsolta. (into a summer house)",
                "answer": "vá"
            },
            {
                "id": "b1-10-01-writing-2",
                "type": "fill-blank",
                "category": "production",
                "sentence": "A modern szigetelés révén az ingatlan jóval energiatakarékosabbá ____. (became)",
                "answer": "vált"
            },
            {
                "id": "b1-10-01-check-1",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik szókapcsolat fejezi ki a válást valamivé?",
                "options": ["otthonná válik", "otthonban lakik", "otthonról indul"],
                "correct": 0
            },
            {
                "id": "b1-10-01-check-2",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Hogyan végződik a 'kert' szó translativus alakja?",
                "options": ["kertté", "kertvé", "kerttel"],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-10-01-ex.json", ex_01)

    ex_02 = {
        "lesson": "b1-10-02",
        "exercises": [
            {
                "id": "b1-10-02-intro-1",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["társasház", "condominium / apartment block"],
                    ["családi ház", "detached house"],
                    ["erkély", "balcony"],
                    ["udvar", "courtyard / yard"]
                ]
            },
            {
                "id": "b1-10-02-intro-2",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["amely", "which (formal)"],
                    ["amiben", "in which"],
                    ["ahol", "where"],
                    ["amire", "onto which"]
                ]
            },
            {
                "id": "b1-10-02-controlled-1",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik vonatkozó névmás kapcsolja össze helyesen: „Ez az a társasház, ______ a harmadik emeleten lakunk.”?",
                "options": ["amelyben", "amitől", "amivé"],
                "correct": 0
            },
            {
                "id": "b1-10-02-controlled-2",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik vonatkozó határozószó illik a hely leírásához: „Olyan környéket keresünk, ______ sok a zöldövezet.”?",
                "options": ["ahol", "amikor", "ahogy"],
                "correct": 0
            },
            {
                "id": "b1-10-02-controlled-3",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Mikor használjuk igényes magyar szövegben az 'amely' névmást az 'ami' helyett?",
                "options": [
                    "Amikor pontosan meghatározott, konkrét főnévre utalunk vissza.",
                    "Csak személyek esetében.",
                    "Kizárólag kérdő mondatokban."
                ],
                "correct": 0
            },
            {
                "id": "b1-10-02-controlled-4",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik mondat helyes nyelvtanilag?",
                "options": [
                    "A lakáshoz tartozik egy tágas erkély, amely a zöld parkra néz.",
                    "A lakáshoz tartozik egy tágas erkély, akire a zöld parkra néz.",
                    "A lakáshoz tartozik egy tágas erkély, amivé a zöld parkra néz."
                ],
                "correct": 0
            },
            {
                "id": "b1-10-02-practice-1",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Szeretünk kiülni az erkélyre, ____ szép kilátás nyílik a budai hegyekre. (from which)",
                "answer": "ahonnan"
            },
            {
                "id": "b1-10-02-practice-2",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A belvárosi bérház közepén egy csendes, macskaköves belső ____ található. (courtyard)",
                "answer": "udvar"
            },
            {
                "id": "b1-10-02-practice-3",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Mit jelent a 'családi ház' Magyarországon?",
                "options": [
                    "Önálló telken álló, különálló lakóépületet egy család számára.",
                    "Tízemeletes lakótelepi paneltömböt.",
                    "Kizárólag irodának használt épületet."
                ],
                "correct": 0
            },
            {
                "id": "b1-10-02-practice-4",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Milyen előnyökkel jár egy társasházi lakás a családi házzal szemben?",
                "options": [
                    "A közös költség tartalmazhatja a lépcsőház takarítását és karbantartását, kevesebb kerti munka hárul a lakóra.",
                    "Soha nem kell semmilyen számlát fizetni.",
                    "Minden lakó maga építi az épület tetejét."
                ],
                "correct": 0
            },
            {
                "id": "b1-10-02-dialogue-1",
                "type": "multiple-choice",
                "category": "reading",
                "question": "— Milyen típusú lakást szeretnétek bérelni?\n— Egy új építésű ______ lakást, amelyhez erkély és mélygarázs is tartozik.",
                "options": ["társasházi", "belső udvar", "fűtési"],
                "correct": 0
            },
            {
                "id": "b1-10-02-dialogue-2",
                "type": "multiple-choice",
                "category": "reading",
                "question": "— Van a háznak saját kertje?\n— Igen, egy zárt zöld ____, ahol a gyerekek biztonságban játszhatnak.",
                "options": ["udvara", "szerződése", "bérlője"],
                "correct": 0
            },
            {
                "id": "b1-10-02-writing-1",
                "type": "fill-blank",
                "category": "production",
                "sentence": "Megtekintettünk egy tágas családi ____ a város szélén. (house)",
                "answer": "házat"
            },
            {
                "id": "b1-10-02-writing-2",
                "type": "fill-blank",
                "category": "production",
                "sentence": "Ez az a szoba, ____ a legtöbb természetes napfény árad be délután. (into which)",
                "answer": "amibe"
            },
            {
                "id": "b1-10-02-check-1",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik vonatkozó névmás illik az eszközre/tárgyra: „A fűtésrendszer, ______ korszerűsítettünk, nagyon gazdaságos.”?",
                "options": ["amelyet", "akivel", "ahová"],
                "correct": 0
            },
            {
                "id": "b1-10-02-check-2",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Mit jelent az 'erkély' szó?",
                "options": ["Balcony", "Basement", "Attic"],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-10-02-ex.json", ex_02)

    ex_03 = {
        "lesson": "b1-10-03",
        "exercises": [
            {
                "id": "b1-10-03-intro-1",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["bérleti szerződés", "lease agreement"],
                    ["főbérlő", "landlord / property owner"],
                    ["kaució", "security deposit"],
                    ["rezsi", "utilities / upkeep costs"]
                ]
            },
            {
                "id": "b1-10-03-intro-2",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["köteles", "obliged to"],
                    ["jogosult", "entitled to"],
                    ["esetén", "in case of"],
                    ["felmondási idő", "notice period"]
                ]
            },
            {
                "id": "b1-10-03-controlled-1",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Mit követel a szerződéses 'köteles' segédszó?",
                "options": ["Főnévi igenevet (pl. köteles megfizetni).", "Tárgyragos főnevet.", "Birtokos ragot."],
                "correct": 0
            },
            {
                "id": "b1-10-03-controlled-2",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Hogyan mondjuk: 'in case of damage' a szerződésben?",
                "options": ["Kár esetén", "Kár miatt", "Kár ellenére"],
                "correct": 0
            },
            {
                "id": "b1-10-03-controlled-3",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik állítás helyes a kaucióról Magyarországon?",
                "options": [
                    "A kaució általában kéthavi vagy egyhavi bérleti díjnak megfelelő összeg, amit kiköltözéskor visszakap a bérlő, ha nincs kár.",
                    "A kaució egy vissza nem térítendő adó.",
                    "A kauciót az önkormányzatnak kell befizetni."
                ],
                "correct": 0
            },
            {
                "id": "b1-10-03-controlled-4",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik mondat hivatalos és szabályos megfogalmazás?",
                "options": [
                    "A bérlő jogosult a lakást rendeltetésszerűen használni.",
                    "A bérlő jogosult a lakást eladni másnak.",
                    "A bérlő köteles a bérleti díjat soha be nem fizetni."
                ],
                "correct": 0
            },
            {
                "id": "b1-10-03-practice-1",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Szerződéskötéskor a bérlő két havi ____ fizetett letétbe. (deposit)",
                "answer": "kauciót"
            },
            {
                "id": "b1-10-03-practice-2",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A téli hónapokban a fűtés miatt némileg megemelkedik a havi ____. (utilities cost)",
                "answer": "rezsi"
            },
            {
                "id": "b1-10-03-practice-3",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Mit tartalmaz általában a lakás rezsiköltsége?",
                "options": [
                    "A víz-, gáz-, villanyszámlát, a fűtést, a szemétszállítást és a közös költséget.",
                    "Kizárólag a televízió előfizetést.",
                    "A bútorok árát."
                ],
                "correct": 0
            },
            {
                "id": "b1-10-03-practice-4",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Mi az a 'felmondási idő' a bérleti jogviszonyban?",
                "options": [
                    "Az az időtartam (általában 30 vagy 60 nap), amelynek el kell telnie a felmondás közlése és a kiköltözés között.",
                    "A kulcsok átadásának perce.",
                    "A kaució visszafizetésének végső határideje."
                ],
                "correct": 0
            },
            {
                "id": "b1-10-03-dialogue-1",
                "type": "multiple-choice",
                "category": "reading",
                "question": "— Mikor kell aláírnunk a papírokat?\n— Holnap találkozunk a ______-vel, és aláírjuk a bérleti szerződést.",
                "options": ["főbérlővel", "tárolóval", "szigeteléssel"],
                "correct": 0
            },
            {
                "id": "b1-10-03-dialogue-2",
                "type": "multiple-choice",
                "category": "reading",
                "question": "— Mennyi a havi bérleti díj?\n— Kétszázezer forint plusz a havi ______ fogyasztás alapján.",
                "options": ["rezsi", "sarok", "erkély"],
                "correct": 0
            },
            {
                "id": "b1-10-03-writing-1",
                "type": "fill-blank",
                "category": "production",
                "sentence": "A felek határozott idejű bérleti ____ kötöttek egymással egy évre. (contract / agreement)",
                "answer": "szerződést"
            },
            {
                "id": "b1-10-03-writing-2",
                "type": "fill-blank",
                "category": "production",
                "sentence": "Késedelmes fizetés ____ a bérbeadó késedelmi kamatot számíthat fel. (in case of)",
                "answer": "esetén"
            },
            {
                "id": "b1-10-03-check-1",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Ki a 'főbérlő'?",
                "options": ["A lakás tulajdonosa vagy bérbeadója.", "Aki a lakást bérli.", "A szomszéd."],
                "correct": 0
            },
            {
                "id": "b1-10-03-check-2",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik kifejezés jelenti azt, hogy joga van valamihez?",
                "options": ["jogosult valamire", "köteles valamire", "rászorul valamire"],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-10-03-ex.json", ex_03)

    ex_04 = {
        "lesson": "b1-10-04",
        "exercises": [
            {
                "id": "b1-10-04-intro-1",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["berendezés", "furnishing / furniture"],
                    ["elrendezés", "layout / arrangement"],
                    ["tároló", "storage room / locker"],
                    ["sarok", "corner"]
                ]
            },
            {
                "id": "b1-10-04-intro-2",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["mellette", "next to it"],
                    ["fölötte", "above it"],
                    ["alatta", "under it"],
                    ["mögötte", "behind it"]
                ]
            },
            {
                "id": "b1-10-04-controlled-1",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik névutós alak fejezi ki: 'above it'?",
                "options": ["fölötte", "alatta", "előtte"],
                "correct": 0
            },
            {
                "id": "b1-10-04-controlled-2",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik alak jelenti: 'between them'?",
                "options": ["közöttük", "közötte", "közülük"],
                "correct": 0
            },
            {
                "id": "b1-10-04-controlled-3",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik mondat mutatja be helyesen a szoba berendezését?",
                "options": [
                    "A sarokban áll a könyvszekrény, mellette pedig a kényelmes olvasófotel kapott helyet.",
                    "A sarok áll könyvszekrény, mellette szék van.",
                    "A sarokról van a könyvszekrény mellette fotelhez."
                ],
                "correct": 0
            },
            {
                "id": "b1-10-04-controlled-4",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Hogyan képezzük a 'mögött' névutó harmadik személyű birtokosragos alakját?",
                "options": ["mögötte", "mögöttje", "mögöttbe"],
                "correct": 0
            },
            {
                "id": "b1-10-04-practice-1",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A pincében minden lakáshoz egy zárható ____ is tartozik a biciklik számára. (storage room)",
                "answer": "tároló"
            },
            {
                "id": "b1-10-04-practice-2",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A nappali tágas, a sarok____ egy nagy zöld szobanövény áll. (in the corner)",
                "answer": "ban"
            },
            {
                "id": "b1-10-04-practice-3",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Mit értünk a lakás 'elrendezésén'?",
                "options": [
                    "A helyiségek alaprajzi elhelyezkedését, kapcsolatait és a bútorok térbeli rendjét.",
                    "A ház festésének színét.",
                    "A lakók névsorát."
                ],
                "correct": 0
            },
            {
                "id": "b1-10-04-practice-4",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Mit jelent az 'amerikai konyhás nappali' kifejezés?",
                "options": [
                    "Olyan modern elrendezést, ahol a konyha, az étkező és a nappali egyetlen közös légtérben van.",
                    "Kizárólag amerikai gépekkel felszerelt konyhát.",
                    "Külön épületben lévő főzőhelyiséget."
                ],
                "correct": 0
            },
            {
                "id": "b1-10-04-dialogue-1",
                "type": "multiple-choice",
                "category": "reading",
                "question": "— Hová tegyük az étkezőasztalt?\n— Szerintem tegyük az ablak elé, és rakjunk köré négy széket, ______ pedig egy szép szőnyeget.",
                "options": ["alá", "felé", "helyett"],
                "correct": 0
            },
            {
                "id": "b1-10-04-dialogue-2",
                "type": "multiple-choice",
                "category": "reading",
                "question": "— Tetszik a lakás új ______?\n— Igen, a világos fa bútorok és a növények nagyon modern hangulatot árasztanak.",
                "options": ["berendezése", "főbérlője", "kauciója"],
                "correct": 0
            },
            {
                "id": "b1-10-04-writing-1",
                "type": "fill-blank",
                "category": "production",
                "sentence": "Az íróasztal a fal mellett van, ____ pedig egy kényelmes forgószék található. (in front of it)",
                "answer": "előtte"
            },
            {
                "id": "b1-10-04-writing-2",
                "type": "fill-blank",
                "category": "production",
                "sentence": "A konyhaszekrény felett polcok függnek, ____ pedig a munkafelület helyezkedik el. (underneath it)",
                "answer": "alatta"
            },
            {
                "id": "b1-10-04-check-1",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik kifejezés jelöli a tárolóhelyet?",
                "options": ["tároló", "társasház", "tanácsos"],
                "correct": 0
            },
            {
                "id": "b1-10-04-check-2",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Mit jelent az 'elrendezés'?",
                "options": ["Layout / arrangement", "Painting", "Contract"],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-10-04-ex.json", ex_04)

    ex_05 = {
        "lesson": "b1-10-05",
        "exercises": [
            {
                "id": "b1-10-05-intro-1",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["élhető", "livable"],
                    ["környék", "neighborhood / surroundings"],
                    ["fűtés", "heating"],
                    ["szigetelés", "insulation"]
                ]
            },
            {
                "id": "b1-10-05-intro-2",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["energiatakarékos", "energy-efficient"],
                    ["hőszigetelt", "thermally insulated"],
                    ["zajmentes", "noise-free / quiet"],
                    ["zöldövezet", "green belt / green area"]
                ]
            },
            {
                "id": "b1-10-05-controlled-1",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik szerkezet fejezi ki legválasztékosabban a személyes prioritást?",
                "options": [
                    "Számomra az a legfontosabb szempont, hogy a környék csendes és biztonságos legyen.",
                    "Nekem kell a csendes környék lenni.",
                    "Számomra fontos környék csendben van."
                ],
                "correct": 0
            },
            {
                "id": "b1-10-05-controlled-2",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik szókapcsolat fejezi ki a jó hőtartást?",
                "options": ["korszerű hőszigetelés", "magas rezsi", "zajos lépcsőház"],
                "correct": 0
            },
            {
                "id": "b1-10-05-controlled-3",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Mit jelent a kifejezés: „ideális esetben”?",
                "options": ["In an ideal scenario / ideally", "In a bad case", "Never"],
                "correct": 0
            },
            {
                "id": "b1-10-05-controlled-4",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik állítás helyes az energiahatékonyságról?",
                "options": [
                    "A megfelelő nyílászárók és a jó szigetelés jelentősen csökkentik a fűtési költségeket.",
                    "A szigetelés növeli a téli fűtésszámlát.",
                    "A fűtést kizárólag nyáron használják Magyarországon."
                ],
                "correct": 0
            },
            {
                "id": "b1-10-05-practice-1",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Olyan lakást keresünk, amely egy nyugodt, családbarát ____ található. (neighborhood)",
                "answer": "környéken"
            },
            {
                "id": "b1-10-05-practice-2",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A ház külső falaira korszerű hőszigetelő réteg került, így a téli ____ nagyon gazdaságos. (heating)",
                "answer": "fűtés"
            },
            {
                "id": "b1-10-05-practice-3",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Mitől válik egy lakókörnyezet igazán 'élhetővé' a városlakók számára?",
                "options": [
                    "Jó közlekedéstől, tiszta levegőtől, zöld parkoktól és közeli szolgáltatásoktól (boltok, orvos, iskola).",
                    "A sűrű kamionforgalomtól és a gyárak közelségétől.",
                    "A teljes sötétségtől."
                ],
                "correct": 0
            },
            {
                "id": "b1-10-05-practice-4",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Milyen modern fűtési megoldások terjednek Magyarországon?",
                "options": [
                    "A hőszivattyús fűtés, a padlófűtés és a napkollektorok.",
                    "Csak a nyílt tábortűz.",
                    "Kizárólag a petróleumlámpák."
                ],
                "correct": 0
            },
            {
                "id": "b1-10-05-dialogue-1",
                "type": "multiple-choice",
                "category": "reading",
                "question": "— Mi a legfontosabb szempontotok az új otthon kiválasztásakor?\n— Számunkra az, hogy a lakás valóban ______ legyen, közel a munkahelyünkhöz és a természethez.",
                "options": ["élhető", "széthúzó", "kiváltó"],
                "correct": 0
            },
            {
                "id": "b1-10-05-dialogue-2",
                "type": "multiple-choice",
                "category": "reading",
                "question": "— Nem aggódtok a téli gázszámla miatt?\n— Egyáltalán nem, mert az új műanyag ablakok és a vastag ______ minimálisra csökkentik a hőveszteséget.",
                "options": ["szigetelés", "kaució", "parasztfelkelés"],
                "correct": 0
            },
            {
                "id": "b1-10-05-writing-1",
                "type": "fill-blank",
                "category": "production",
                "sentence": "Ideális esetben a lakáshoz külön garázs és zöld ____ is tartozik. (yard / courtyard)",
                "answer": "udvar"
            },
            {
                "id": "b1-10-05-writing-2",
                "type": "fill-blank",
                "category": "production",
                "sentence": "Számomra elengedhetetlen, hogy a lakás világos és csendes ____. (be - subjunctive / optative)",
                "answer": "legyen"
            },
            {
                "id": "b1-10-05-reading-1",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Hol játszódik az adapted Kosztolányi-részlet (Édes Anna)?",
                "options": [
                    "Budapesten, a krisztinavárosi bérházban Vizyék lakásában.",
                    "Egy debreceni tanyán.",
                    "Bécsben a császári palotában."
                ],
                "correct": 0
            },
            {
                "id": "b1-10-05-reading-2",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Milyen benyomást tett a lakás Annára, amikor belépett az előszobába?",
                "options": [
                    "Rendkívül tiszta és fényes volt, a lakkozott parketta úgy csillogott, mint a tükör.",
                    "Piszkos és elhanyagolt volt.",
                    "Üres volt minden bútor nélkül."
                ],
                "correct": 0
            },
            {
                "id": "b1-10-05-reading-3",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Hogyan érezte magát Vizyné asszony Anna érkezésekor?",
                "options": [
                    "Büszkén mutatta meg a lakást, érezve, hogy a ház végre valódi otthonná válik.",
                    "Azonnal elküldte a lányt vissza a falujába.",
                    "Nagyon dühös volt a bútorok miatt."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-10-05-ex.json", ex_05)

    ex_consolidation = {
        "lesson": "b1-10-consolidation",
        "exercises": [
            {
                "id": "b1-10-consolidation-1",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["felújítás", "renovation"],
                    ["bérleti szerződés", "lease contract"],
                    ["kaució", "security deposit"],
                    ["rezsi", "utilities"]
                ]
            },
            {
                "id": "b1-10-consolidation-2",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["társasház", "apartment condominium"],
                    ["családi ház", "detached house"],
                    ["berendezés", "furnishing"],
                    ["elrendezés", "layout"]
                ]
            },
            {
                "id": "b1-10-consolidation-3",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["élhető", "livable"],
                    ["környék", "neighborhood"],
                    ["szigetelés", "insulation"],
                    ["tároló", "storage locker"]
                ]
            },
            {
                "id": "b1-10-consolidation-4",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Hogyan alakul a 'szép' melléknév translativus alakja a mondatban: „A virágok ______ tették a teraszt.”?",
                "options": ["szebbé", "szépvé", "széppé"],
                "correct": 0
            },
            {
                "id": "b1-10-consolidation-5",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik vonatkozó névmás utal helyesen az élettelen tárgyra?",
                "options": [
                    "Kibéreltük azt a lakást, amely a belső kertre néz.",
                    "Kibéreltük azt a lakást, aki a belső kertre néz.",
                    "Kibéreltük azt a lakást, amivel a belső kertre néz."
                ],
                "correct": 0
            },
            {
                "id": "b1-10-consolidation-6",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik névutós kifejezés helyes: 'next to it'?",
                "options": ["mellette", "mögötte", "fölötte"],
                "correct": 0
            },
            {
                "id": "b1-10-consolidation-7",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A felújítás után a régi lakás modern otthon____ alakult át. (into - translative)",
                "answer": "ná"
            },
            {
                "id": "b1-10-consolidation-8",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A bérlő szerződéskötéskor két havi ____ fizet a főbérlőnek. (deposit)",
                "answer": "kauciót"
            },
            {
                "id": "b1-10-consolidation-9",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A téli fűtésszámlát a korszerű fal____ és a modern ablakok csökkentik. (insulation)",
                "answer": "szigetelés"
            },
            {
                "id": "b1-10-consolidation-10",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Mit kell tisztázni a bérleti szerződésben a beköltözés előtt?",
                "options": [
                    "A havi bérleti díjat, a kaució összegét, a rezsi fizetésének módját és a felmondási időt.",
                    "Csak a főbérlő kedvenc színét.",
                    "Semmit, elég egy kézfogás."
                ],
                "correct": 0
            },
            {
                "id": "b1-10-consolidation-11",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Melyik klasszikus magyar regény mutatja be a krisztinavárosi polgári lakás világát és Édes Anna történetét?",
                "options": [
                    "Kosztolányi Dezső: Édes Anna.",
                    "Gárdonyi Géza: Egri csillagok.",
                    "Móricz Zsigmond: Légy jó mindhalálig."
                ],
                "correct": 0
            },
            {
                "id": "b1-10-consolidation-12",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Mit fejez ki a mondat: „Számomra a legfontosabb szempont egy csendes, zöld környék.”?",
                "options": [
                    "A beszélő számára a lakás helyszíne és nyugalma a legfőbb döntési tényező.",
                    "A beszélő egy forgalmas belvárosi autópálya mellett akar lakni.",
                    "A beszélő nem akar lakást vásárolni vagy bérelni."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-10-consolidation-ex.json", ex_consolidation)

    # -------------------------------------------------------------------------
    # 5. Lesson Files (6 lessons)
    # -------------------------------------------------------------------------
    lesson_01 = {
        "id": "lesson.b1.10-01",
        "unit": 10,
        "title": "Turning a House into a Home",
        "level": "B1",
        "grammar": "Translative Case -vá / -vé & Transformation Verbs (válik, tesz)",
        "goal": [
            "I can express transformation and change of state using the translative case -vá / -vé.",
            "I can describe home remodeling, renovation, and interior improvements.",
            "I can contrast intransitive válik with transitive tesz in transformation clauses.",
            "I can use four new vocabulary items related to ambiance, lighting, and renovation."
        ],
        "sections": [
            {
                "type": "goal",
                "title": "Lesson Goals",
                "items": [
                    "I can express transformation and change of state using the translative case -vá / -vé.",
                    "I can describe home remodeling, renovation, and interior improvements.",
                    "I can contrast intransitive válik with transitive tesz in transformation clauses.",
                    "I can use four new vocabulary items related to ambiance, lighting, and renovation."
                ]
            },
            {"type": "recycle", "title": "Quick Review"},
            {"type": "grammar", "ref": "grammar/b1/b1-10-01-a-gr.json"},
            {"type": "grammar", "ref": "grammar/b1/b1-10-01-b-gr.json"},
            {"type": "vocabulary", "title": "Lesson Vocabulary", "ref": "vocabulary/b1/b1-10-01-voc.json"},
            {"type": "exercise-group", "title": "Introduce", "ref": "exercises/b1/b1-10-01-ex.json", "exerciseRefs": ["b1-10-01-intro-1", "b1-10-01-intro-2"]},
            {"type": "exercise-group", "title": "Controlled", "ref": "exercises/b1/b1-10-01-ex.json", "exerciseRefs": ["b1-10-01-controlled-1", "b1-10-01-controlled-2", "b1-10-01-controlled-3", "b1-10-01-controlled-4"]},
            {"type": "exercise-group", "title": "Practice", "ref": "exercises/b1/b1-10-01-ex.json", "exerciseRefs": ["b1-10-01-practice-1", "b1-10-01-practice-2", "b1-10-01-practice-3", "b1-10-01-practice-4"]},
            {"type": "exercise-group", "title": "Dialogue", "ref": "exercises/b1/b1-10-01-ex.json", "exerciseRefs": ["b1-10-01-dialogue-1", "b1-10-01-dialogue-2"]},
            {"type": "exercise-group", "title": "Production", "ref": "exercises/b1/b1-10-01-ex.json", "exerciseRefs": ["b1-10-01-writing-1", "b1-10-01-writing-2"]},
            {"type": "srs", "title": "Add to Review"},
            {"type": "exercise-group", "title": "Check", "ref": "exercises/b1/b1-10-01-ex.json", "exerciseRefs": ["b1-10-01-check-1", "b1-10-01-check-2"]},
            {
                "type": "checklist",
                "title": "Can you do this?",
                "items": [
                    "I can express transformation and change of state using the translative case -vá / -vé.",
                    "I can describe home remodeling, renovation, and interior improvements.",
                    "I can contrast intransitive válik with transitive tesz in transformation clauses.",
                    "I can use four new vocabulary items related to ambiance, lighting, and renovation."
                ]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-10-01.json", lesson_01)

    lesson_02 = {
        "id": "lesson.b1.10-02",
        "unit": 10,
        "title": "The Place I Live In",
        "level": "B1",
        "grammar": "Relative Pronouns with Places & Inanimates: amely, amiben, ahol",
        "goal": [
            "I can connect descriptive details of dwellings using relative pronouns (amely, amiben, ahol).",
            "I can distinguish between detached homes (családi ház) and apartments (társasház).",
            "I can discuss balconies, yards, and common condominium features.",
            "I can use four new vocabulary items related to residential property types."
        ],
        "sections": [
            {
                "type": "goal",
                "title": "Lesson Goals",
                "items": [
                    "I can connect descriptive details of dwellings using relative pronouns (amely, amiben, ahol).",
                    "I can distinguish between detached homes (családi ház) and apartments (társasház).",
                    "I can discuss balconies, yards, and common condominium features.",
                    "I can use four new vocabulary items related to residential property types."
                ]
            },
            {"type": "recycle", "title": "Quick Review"},
            {"type": "grammar", "ref": "grammar/b1/b1-10-02-gr.json"},
            {"type": "vocabulary", "title": "Lesson Vocabulary", "ref": "vocabulary/b1/b1-10-02-voc.json"},
            {"type": "exercise-group", "title": "Introduce", "ref": "exercises/b1/b1-10-02-ex.json", "exerciseRefs": ["b1-10-02-intro-1", "b1-10-02-intro-2"]},
            {"type": "exercise-group", "title": "Controlled", "ref": "exercises/b1/b1-10-02-ex.json", "exerciseRefs": ["b1-10-02-controlled-1", "b1-10-02-controlled-2", "b1-10-02-controlled-3", "b1-10-02-controlled-4"]},
            {"type": "exercise-group", "title": "Practice", "ref": "exercises/b1/b1-10-02-ex.json", "exerciseRefs": ["b1-10-02-practice-1", "b1-10-02-practice-2", "b1-10-02-practice-3", "b1-10-02-practice-4"]},
            {"type": "exercise-group", "title": "Dialogue", "ref": "exercises/b1/b1-10-02-ex.json", "exerciseRefs": ["b1-10-02-dialogue-1", "b1-10-02-dialogue-2"]},
            {"type": "exercise-group", "title": "Production", "ref": "exercises/b1/b1-10-02-ex.json", "exerciseRefs": ["b1-10-02-writing-1", "b1-10-02-writing-2"]},
            {"type": "srs", "title": "Add to Review"},
            {"type": "exercise-group", "title": "Check", "ref": "exercises/b1/b1-10-02-ex.json", "exerciseRefs": ["b1-10-02-check-1", "b1-10-02-check-2"]},
            {
                "type": "checklist",
                "title": "Can you do this?",
                "items": [
                    "I can connect descriptive details of dwellings using relative pronouns (amely, amiben, ahol).",
                    "I can distinguish between detached homes (családi ház) and apartments (társasház).",
                    "I can discuss balconies, yards, and common condominium features.",
                    "I can use four new vocabulary items related to residential property types."
                ]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-10-02.json", lesson_02)

    lesson_03 = {
        "id": "lesson.b1.10-03",
        "unit": 10,
        "title": "Renting & Tenancy Agreements",
        "level": "B1",
        "grammar": "Contractual Clauses: köteles, jogosult, esetén",
        "goal": [
            "I can understand and discuss terms in a rental lease (bérleti szerződés).",
            "I can negotiate security deposits (kaució) and utility payments (rezsi) with a landlord.",
            "I can express rights and contractual duties using köteles, jogosult, and esetén.",
            "I can use four new vocabulary items related to leases and rental management."
        ],
        "sections": [
            {
                "type": "goal",
                "title": "Lesson Goals",
                "items": [
                    "I can understand and discuss terms in a rental lease (bérleti szerződés).",
                    "I can negotiate security deposits (kaució) and utility payments (rezsi) with a landlord.",
                    "I can express rights and contractual duties using köteles, jogosult, and esetén.",
                    "I can use four new vocabulary items related to leases and rental management."
                ]
            },
            {"type": "recycle", "title": "Quick Review"},
            {"type": "grammar", "ref": "grammar/b1/b1-10-03-gr.json"},
            {"type": "vocabulary", "title": "Lesson Vocabulary", "ref": "vocabulary/b1/b1-10-03-voc.json"},
            {"type": "exercise-group", "title": "Introduce", "ref": "exercises/b1/b1-10-03-ex.json", "exerciseRefs": ["b1-10-03-intro-1", "b1-10-03-intro-2"]},
            {"type": "exercise-group", "title": "Controlled", "ref": "exercises/b1/b1-10-03-ex.json", "exerciseRefs": ["b1-10-03-controlled-1", "b1-10-03-controlled-2", "b1-10-03-controlled-3", "b1-10-03-controlled-4"]},
            {"type": "exercise-group", "title": "Practice", "ref": "exercises/b1/b1-10-03-ex.json", "exerciseRefs": ["b1-10-03-practice-1", "b1-10-03-practice-2", "b1-10-03-practice-3", "b1-10-03-practice-4"]},
            {"type": "exercise-group", "title": "Dialogue", "ref": "exercises/b1/b1-10-03-ex.json", "exerciseRefs": ["b1-10-03-dialogue-1", "b1-10-03-dialogue-2"]},
            {"type": "exercise-group", "title": "Production", "ref": "exercises/b1/b1-10-03-ex.json", "exerciseRefs": ["b1-10-03-writing-1", "b1-10-03-writing-2"]},
            {"type": "srs", "title": "Add to Review"},
            {"type": "exercise-group", "title": "Check", "ref": "exercises/b1/b1-10-03-ex.json", "exerciseRefs": ["b1-10-03-check-1", "b1-10-03-check-2"]},
            {
                "type": "checklist",
                "title": "Can you do this?",
                "items": [
                    "I can understand and discuss terms in a rental lease (bérleti szerződés).",
                    "I can negotiate security deposits (kaució) and utility payments (rezsi) with a landlord.",
                    "I can express rights and contractual duties using köteles, jogosult, and esetén.",
                    "I can use four new vocabulary items related to leases and rental management."
                ]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-10-03.json", lesson_03)

    lesson_04 = {
        "id": "lesson.b1.10-04",
        "unit": 10,
        "title": "Interior Layout & Spatial Relations",
        "level": "B1",
        "grammar": "Interior Spatial Postpositions: mellette, fölötte, alatta, mögötte",
        "goal": [
            "I can describe the layout and arrangement of furniture in an apartment.",
            "I can use inflected spatial postpositions (mellette, fölötte, alatta, mögötte).",
            "I can specify storage rooms, corners, and functional zones in a home.",
            "I can use four new vocabulary items related to furniture layout and storage."
        ],
        "sections": [
            {
                "type": "goal",
                "title": "Lesson Goals",
                "items": [
                    "I can describe the layout and arrangement of furniture in an apartment.",
                    "I can use inflected spatial postpositions (mellette, fölötte, alatta, mögötte).",
                    "I can specify storage rooms, corners, and functional zones in a home.",
                    "I can use four new vocabulary items related to furniture layout and storage."
                ]
            },
            {"type": "recycle", "title": "Quick Review"},
            {"type": "grammar", "ref": "grammar/b1/b1-10-04-gr.json"},
            {"type": "vocabulary", "title": "Lesson Vocabulary", "ref": "vocabulary/b1/b1-10-04-voc.json"},
            {"type": "exercise-group", "title": "Introduce", "ref": "exercises/b1/b1-10-04-ex.json", "exerciseRefs": ["b1-10-04-intro-1", "b1-10-04-intro-2"]},
            {"type": "exercise-group", "title": "Controlled", "ref": "exercises/b1/b1-10-04-ex.json", "exerciseRefs": ["b1-10-04-controlled-1", "b1-10-04-controlled-2", "b1-10-04-controlled-3", "b1-10-04-controlled-4"]},
            {"type": "exercise-group", "title": "Practice", "ref": "exercises/b1/b1-10-04-ex.json", "exerciseRefs": ["b1-10-04-practice-1", "b1-10-04-practice-2", "b1-10-04-practice-3", "b1-10-04-practice-4"]},
            {"type": "exercise-group", "title": "Dialogue", "ref": "exercises/b1/b1-10-04-ex.json", "exerciseRefs": ["b1-10-04-dialogue-1", "b1-10-04-dialogue-2"]},
            {"type": "exercise-group", "title": "Production", "ref": "exercises/b1/b1-10-04-ex.json", "exerciseRefs": ["b1-10-04-writing-1", "b1-10-04-writing-2"]},
            {"type": "srs", "title": "Add to Review"},
            {"type": "exercise-group", "title": "Check", "ref": "exercises/b1/b1-10-04-ex.json", "exerciseRefs": ["b1-10-04-check-1", "b1-10-04-check-2"]},
            {
                "type": "checklist",
                "title": "Can you do this?",
                "items": [
                    "I can describe the layout and arrangement of furniture in an apartment.",
                    "I can use inflected spatial postpositions (mellette, fölötte, alatta, mögötte).",
                    "I can specify storage rooms, corners, and functional zones in a home.",
                    "I can use four new vocabulary items related to furniture layout and storage."
                ]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-10-04.json", lesson_04)

    lesson_05 = {
        "id": "lesson.b1.10-05",
        "unit": 10,
        "title": "My Ideal Home, Explained",
        "level": "B1",
        "grammar": "Synthesis: Housing Criteria & Subjunctive (Számomra fontos, hogy...)",
        "goal": [
            "I can formulate comprehensive criteria for an ideal, livable home.",
            "I can discuss energy efficiency, heating, insulation, and neighborhood amenities.",
            "I can use four new vocabulary items related to housing quality and surroundings.",
            "I can read and understand an adapted excerpt from Kosztolányi Dezső's Édes Anna."
        ],
        "sections": [
            {
                "type": "goal",
                "title": "Lesson Goals",
                "items": [
                    "I can formulate comprehensive criteria for an ideal, livable home.",
                    "I can discuss energy efficiency, heating, insulation, and neighborhood amenities.",
                    "I can use four new vocabulary items related to housing quality and surroundings.",
                    "I can read and understand an adapted excerpt from Kosztolányi Dezső's Édes Anna."
                ]
            },
            {"type": "recycle", "title": "Quick Review"},
            {"type": "grammar", "ref": "grammar/b1/b1-10-05-gr.json"},
            {"type": "vocabulary", "title": "Lesson Vocabulary", "ref": "vocabulary/b1/b1-10-05-voc.json"},
            {"type": "exercise-group", "title": "Introduce", "ref": "exercises/b1/b1-10-05-ex.json", "exerciseRefs": ["b1-10-05-intro-1", "b1-10-05-intro-2"]},
            {"type": "exercise-group", "title": "Controlled", "ref": "exercises/b1/b1-10-05-ex.json", "exerciseRefs": ["b1-10-05-controlled-1", "b1-10-05-controlled-2", "b1-10-05-controlled-3", "b1-10-05-controlled-4"]},
            {"type": "exercise-group", "title": "Practice", "ref": "exercises/b1/b1-10-05-ex.json", "exerciseRefs": ["b1-10-05-practice-1", "b1-10-05-practice-2", "b1-10-05-practice-3", "b1-10-05-practice-4"]},
            {"type": "exercise-group", "title": "Dialogue", "ref": "exercises/b1/b1-10-05-ex.json", "exerciseRefs": ["b1-10-05-dialogue-1", "b1-10-05-dialogue-2"]},
            {"type": "exercise-group", "title": "Production", "ref": "exercises/b1/b1-10-05-ex.json", "exerciseRefs": ["b1-10-05-writing-1", "b1-10-05-writing-2"]},
            {"type": "srs", "title": "Add to Review"},
            {
                "type": "story",
                "title": "Reading: Édes Anna a Krisztinavárosban",
                "ref": "stories/classics/b1/b1-10-edesanna.json"
            },
            {"type": "exercise-group", "title": "Reading", "ref": "exercises/b1/b1-10-05-ex.json", "exerciseRefs": ["b1-10-05-reading-1", "b1-10-05-reading-2", "b1-10-05-reading-3"]},
            {
                "type": "checklist",
                "title": "Can you do this?",
                "items": [
                    "I can formulate comprehensive criteria for an ideal, livable home.",
                    "I can discuss energy efficiency, heating, insulation, and neighborhood amenities.",
                    "I can use four new vocabulary items related to housing quality and surroundings.",
                    "I can read and understand an adapted excerpt from Kosztolányi Dezső's Édes Anna."
                ]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-10-05.json", lesson_05)

    lesson_consolidation = {
        "id": "lesson.b1.10-consolidation",
        "unit": 10,
        "title": "Unit 10 Consolidation",
        "level": "B1",
        "sections": [
            {
                "type": "goal",
                "title": "Consolidation Goals",
                "items": [
                    "I can use the translative case -vá / -vé to describe home improvements.",
                    "I can connect dwelling descriptions using relative pronouns (amely, amiben, ahol).",
                    "I can navigate tenancy agreements, security deposits (kaució), and utility bills (rezsi).",
                    "I can describe furniture placement using inflected postpositions (mellette, fölötte, alatta)."
                ]
            },
            {"type": "recycle", "title": "Quick Review"},
            {"type": "exercise-group", "title": "Recognize", "ref": "exercises/b1/b1-10-consolidation-ex.json", "exerciseRefs": ["b1-10-consolidation-1", "b1-10-consolidation-2", "b1-10-consolidation-3"]},
            {"type": "exercise-group", "title": "Recall", "ref": "exercises/b1/b1-10-consolidation-ex.json", "exerciseRefs": ["b1-10-consolidation-4", "b1-10-consolidation-5", "b1-10-consolidation-6"]},
            {"type": "exercise-group", "title": "In Context", "ref": "exercises/b1/b1-10-consolidation-ex.json", "exerciseRefs": ["b1-10-consolidation-7", "b1-10-consolidation-8", "b1-10-consolidation-9"]},
            {"type": "exercise-group", "title": "Produce", "ref": "exercises/b1/b1-10-consolidation-ex.json", "exerciseRefs": ["b1-10-consolidation-10", "b1-10-consolidation-11", "b1-10-consolidation-12"]},
            {
                "type": "checklist",
                "title": "Can you do this?",
                "items": [
                    "I can use the translative case -vá / -vé to describe home improvements.",
                    "I can connect dwelling descriptions using relative pronouns (amely, amiben, ahol).",
                    "I can navigate tenancy agreements, security deposits (kaució), and utility bills (rezsi).",
                    "I can describe furniture placement using inflected postpositions (mellette, fölötte, alatta)."
                ]
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-10-consolidation.json", lesson_consolidation)

if __name__ == "__main__":
    build_unit_10_core()
    print("Successfully built Hungarian B1 Core Unit 10!")
