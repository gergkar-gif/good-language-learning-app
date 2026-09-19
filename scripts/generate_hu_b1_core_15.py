#!/usr/bin/env python3
"""Generate Hungarian B1 Core Unit 15: Culture & Entertainment (b1-15)."""

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

def build_unit_15_core():
    # -------------------------------------------------------------------------
    # 1. Vocabulary Files (4 words each = 20 words total)
    # -------------------------------------------------------------------------
    voc_01 = {
        "id": "vocab.b1.15.01",
        "lesson": "b1-15-01",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "kiállítás", "translation": "exhibition", "pos": "noun"},
            {"lemma": "múzeumlátogatás", "translation": "museum visit", "pos": "noun"},
            {"lemma": "színházi előadás", "translation": "theatrical performance", "pos": "noun"},
            {"lemma": "koncertélmény", "translation": "concert experience", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-15-01-voc.json", voc_01)

    voc_02 = {
        "id": "vocab.b1.15.02",
        "lesson": "b1-15-02",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "ajánló", "translation": "recommendation, guide, preview", "pos": "noun"},
            {"lemma": "kulturális program", "translation": "cultural event, program", "pos": "noun"},
            {"lemma": "jegyvásárlás", "translation": "ticket purchase, booking", "pos": "noun"},
            {"lemma": "helyszín", "translation": "venue, location", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-15-02-voc.json", voc_02)

    voc_03 = {
        "id": "vocab.b1.15.03",
        "lesson": "b1-15-03",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "filmkritika", "translation": "film review", "pos": "noun"},
            {"lemma": "rendező", "translation": "director", "pos": "noun"},
            {"lemma": "főszereplő", "translation": "protagonist, leading actor", "pos": "noun"},
            {"lemma": "szereposztás", "translation": "cast, casting", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-15-03-voc.json", voc_03)

    voc_04 = {
        "id": "vocab.b1.15.04",
        "lesson": "b1-15-04",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "néphagyomány", "translation": "folk tradition, folklore", "pos": "noun"},
            {"lemma": "kortárs művészet", "translation": "contemporary art", "pos": "noun"},
            {"lemma": "fesztivál", "translation": "festival", "pos": "noun"},
            {"lemma": "kulturális örökség", "translation": "cultural heritage", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-15-04-voc.json", voc_04)

    voc_05 = {
        "id": "vocab.b1.15.05",
        "lesson": "b1-15-05",
        "title": "Lesson Vocabulary",
        "words": [
            {"lemma": "művészi ízlés", "translation": "artistic taste", "pos": "noun"},
            {"lemma": "élménybeszámoló", "translation": "account of an experience, review", "pos": "noun"},
            {"lemma": "műfaj", "translation": "genre", "pos": "noun"},
            {"lemma": "közönségsiker", "translation": "box-office hit, audience success", "pos": "noun"}
        ]
    }
    write_json("content/hu/vocabulary/b1/b1-15-05-voc.json", voc_05)

    # -------------------------------------------------------------------------
    # 2. Grammar Files
    # -------------------------------------------------------------------------
    gr_01_a = {
        "id": "grammar.b1.15.01.correlative-minel-annal",
        "title": "Correlative Comparative: minél... annál... (The more..., the more...)",
        "sections": [
            {
                "type": "text",
                "title": "Structure and Use of minél... annál...",
                "content": "To express proportional change, Hungarian pairs *minél* with *annál*, both governing comparative adjectives or adverbs: *Minél többet olvasunk, annál műveltebbek leszünk.* ('The more we read, the more educated we become.')."
            },
            {
                "type": "examples",
                "title": "Correlative examples",
                "items": [
                    {
                        "spanish": "Minél korábban érkezünk, annál jobb helyet találunk a nézőtéren.",
                        "english": "The earlier we arrive, the better seat we find in the auditorium."
                    },
                    {
                        "spanish": "Minél több kiállítást látogatok meg, annál jobban értem a festészetet.",
                        "english": "The more exhibitions I visit, the better I understand painting."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-15-01-a-gr.json", gr_01_a)

    gr_01_b = {
        "id": "grammar.b1.15.01.superlative-degree",
        "title": "Superlative and Emphatic Degree: leg- and legesleg-",
        "sections": [
            {
                "type": "text",
                "title": "Forming Superlatives in Hungarian",
                "content": "The prefix *leg-* is added to the comparative stem: *szép* -> *szebb* -> *legszebb*. For maximum emphasis in cultural critique, *legesleg-* can be used: *a legeslegjobb előadás* ('the very best performance')."
            },
            {
                "type": "examples",
                "title": "Superlative examples",
                "items": [
                    {
                        "spanish": "Ez volt a legizgalmasabb színházi előadás, amit idén láttam.",
                        "english": "This was the most exciting theater performance I have seen this year."
                    },
                    {
                        "spanish": "A Nemzeti Múzeum az ország egyik legfontosabb kulturális intézménye.",
                        "english": "The National Museum is one of the most important cultural institutions in the country."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-15-01-b-gr.json", gr_01_b)

    gr_02_a = {
        "id": "grammar.b1.15.02.recommending-structures",
        "title": "Structures for Recommending: érdemes, ajánlatos, kár lenne kihagyni",
        "sections": [
            {
                "type": "text",
                "title": "Cultural Recommendation Idioms",
                "content": "To recommend cultural outings, use *érdemes + inf.* (it is worth...), *ajánlatos + inf.* (it is advisable...), *kár lenne kihagyni* (it would be a pity to miss it): *Mindenképpen érdemes megnézni az új kiállítást.*"
            },
            {
                "type": "examples",
                "title": "Recommendation examples",
                "items": [
                    {
                        "spanish": "Mindenkinek ajánlom a szombati koncertet, kár lenne kihagyni!",
                        "english": "I recommend Saturday's concert to everyone; it would be a pity to miss it!"
                    },
                    {
                        "spanish": "A belvárosban érdemes előre gondoskodni a jegyvásárlásról.",
                        "english": "In the city center it is worth arranging ticket booking in advance."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-15-02-a-gr.json", gr_02_a)

    gr_02_b = {
        "id": "grammar.b1.15.02.indirect-invitations",
        "title": "Indirect Cultural Invitations: Mi lenne, ha elmennénk...?",
        "sections": [
            {
                "type": "text",
                "title": "Polite Conditional Suggestions",
                "content": "Conditional polite invitations use *Mi lenne, ha... + conditional*: *Mi lenne, ha elmennénk színházba a hétvégén?* ('What if we went to the theater this weekend?')."
            },
            {
                "type": "examples",
                "title": "Invitation examples",
                "items": [
                    {
                        "spanish": "Mit szólnál, ha megnéznénk az új magyar filmet a moziban?",
                        "english": "What would you say if we checked out the new Hungarian film in the cinema?"
                    },
                    {
                        "spanish": "Szívesen elmennék veled a pénteki kulturális fesztiválra.",
                        "english": "I would gladly go with you to the Friday cultural festival."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-15-02-b-gr.json", gr_02_b)

    gr_03_a = {
        "id": "grammar.b1.15.03.evaluating-films-plays",
        "title": "Expressing Critical Assessment: hiteles alakítás, fordulatos cselekmény",
        "sections": [
            {
                "type": "text",
                "title": "Critical Vocabulary & Collocations",
                "content": "In reviews and critiques, use standard collocations: *hiteles alakítás* (convincing/authentic performance), *fordulatos cselekmény* (twist-filled plot), *kiváló rendezés* (superb directing), *remek szereposztás* (great cast)."
            },
            {
                "type": "examples",
                "title": "Review collocations",
                "items": [
                    {
                        "spanish": "A főszereplő játéka lenyűgöző és hiteles volt a filmben.",
                        "english": "The lead actor's acting was impressive and authentic in the film."
                    },
                    {
                        "spanish": "A filmkritika kiemelte a rendező bátor és újító látásmódját.",
                        "english": "The film review highlighted the director's bold and innovative vision."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-15-03-a-gr.json", gr_03_a)

    gr_03_b = {
        "id": "grammar.b1.15.03.contrastive-evaluations",
        "title": "Contrasting Merits & Flaws: bár a zene jó, a forgatókönyv gyenge",
        "sections": [
            {
                "type": "text",
                "title": "Constructing Balanced Reviews",
                "content": "Critical assessments balance praise with caveats: *Noha a látványvilág gyönyörű, a történet néhol unalmas.* (*Although the visual world is beautiful, the story is boring in places.*)"
            },
            {
                "type": "examples",
                "title": "Balanced review examples",
                "items": [
                    {
                        "spanish": "Bár a zene kiváló volt, a párbeszédek néhol mesterkéltnek tűntek.",
                        "english": "Although the music was excellent, the dialogue seemed artificial in places."
                    },
                    {
                        "spanish": "A film hibái ellenére a nézők felállva tapsoltak a végén.",
                        "english": "Despite the film's flaws, the audience gave a standing ovation at the end."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-15-03-b-gr.json", gr_03_b)

    gr_04_a = {
        "id": "grammar.b1.15.04.heritage-tradition-expressions",
        "title": "Talking About Traditions: nemzedékről nemzedékre öröklődik, ápol",
        "sections": [
            {
                "type": "text",
                "title": "Cultural Continuity Vocabulary",
                "content": "To discuss heritage and folklore, use idiomatic predicates: *nemzedékről nemzedékre öröklődik* (is passed down from generation to generation), *ápolja a hagyományokat* (cherishes/preserves traditions), *gazdagítja a kultúrát* (enriches culture)."
            },
            {
                "type": "examples",
                "title": "Heritage examples",
                "items": [
                    {
                        "spanish": "A táncházmozgalom révén a néphagyomány ma is eleven része a kultúrának.",
                        "english": "Through the dance house movement, folk tradition remains a living part of culture today."
                    },
                    {
                        "spanish": "A magyar zenei örökség világszerte ismert és elismert kincs.",
                        "english": "Hungarian musical heritage is a treasure known and recognized worldwide."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-15-04-a-gr.json", gr_04_a)

    gr_04_b = {
        "id": "grammar.b1.15.04.passive-cultural-status",
        "title": "Stative Participles in Culture: elismert, megbecsült, nyilvántartott",
        "sections": [
            {
                "type": "text",
                "title": "Adjectival Participles in Cultural Recognition",
                "content": "Past participles function as descriptive adjectives: *világszerte elismert művész* (globally recognized artist), *UNESCO által védett örökség* (UNESCO-protected heritage)."
            },
            {
                "type": "examples",
                "title": "Stative participle examples",
                "items": [
                    {
                        "spanish": "Hollókő ófaluja az UNESCO által elismert világörökség része.",
                        "english": "The old village of Hollókő is part of the world heritage recognized by UNESCO."
                    },
                    {
                        "spanish": "A fesztiválon a legelismertebb kortárs képzőművészek állítottak ki.",
                        "english": "The most acclaimed contemporary artists exhibited at the festival."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-15-04-b-gr.json", gr_04_b)

    gr_05_a = {
        "id": "grammar.b1.15.05.expressing-preferences-taste",
        "title": "Expressing Subjective Taste: ízlések és pofonok, közel áll hozzám",
        "sections": [
            {
                "type": "text",
                "title": "Idiomatic Expressions of Taste",
                "content": "To express personal affinity: *közel áll a szívemhez* (is close to my heart), *távol áll tőlem* (is alien to me), *Ízlések és pofonok különbözők* (There's no accounting for taste / To each their own)."
            },
            {
                "type": "examples",
                "title": "Taste expressions",
                "items": [
                    {
                        "spanish": "A klasszikus zene mindig is nagyon közel állt a szívemhez.",
                        "english": "Classical music has always been very close to my heart."
                    },
                    {
                        "spanish": "Ízlések és pofonok: ami az egyiknek remekmű, az a másiknak unalmas.",
                        "english": "To each their own: what is a masterpiece to one is boring to another."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-15-05-a-gr.json", gr_05_a)

    gr_05_b = {
        "id": "grammar.b1.15.05.concluding-cultural-reflections",
        "title": "Concluding Cultural Reflections: felejthetetlen élmény marad, mély nyomot hagy",
        "sections": [
            {
                "type": "text",
                "title": "Memorable Experience Formulae",
                "content": "Concluding review phrases: *felejthetetlen élmény marad* (remains an unforgettable experience), *mély nyomot hagy az emberben* (leaves a deep impression on one)."
            },
            {
                "type": "examples",
                "title": "Cultural conclusion examples",
                "items": [
                    {
                        "spanish": "A tegnapi színházi előadás felejthetetlen élmény marad számomra.",
                        "english": "Yesterday's theater performance will remain an unforgettable experience for me."
                    },
                    {
                        "spanish": "A darab befejezése mély nyomot hagyott a nézők emlékezetében.",
                        "english": "The ending of the play left a deep impression on the audience's memory."
                    }
                ]
            }
        ]
    }
    write_json("content/hu/grammar/b1/b1-15-05-b-gr.json", gr_05_b)

    # -------------------------------------------------------------------------
    # 3. Classic Literature Story: Jókai Mór: A kőszívű ember fiai
    # -------------------------------------------------------------------------
    classic_story = {
        "id": "story.b1.15.classic",
        "title": "A bécsi színházban és a bál forgatagában",
        "level": "B1",
        "order": 15,
        "type": "classics",
        "estimatedMinutes": 7,
        "summary": "An adaptation from Mór Jókai's masterwork 'A kőszívű ember fiai' (The Baron's Sons). In glamorous imperial Vienna, young Ödön and Richard Baradlay attend the opera and the grand charity ball, experiencing the heights of high society, theater, music, and the gathering storm of Hungarian patriotism.",
        "characters": ["Baradlay Ödön", "Baradlay Richárd", "Plankenhorst Alfonsine"],
        "location": "Bécs, Császári Operaház és bálterem",
        "author": "Jókai Mór",
        "work": "A kőszívű ember fiai",
        "historicalContext": "Mór Jókai (1825–1904) was the towering titan of 19th-century Hungarian romantic literature. 'A kőszívű ember fiai' (1869) chronicles the epic choices of the three Baradlay brothers during the 1848 Revolution and War of Independence.",
        "readingQuestions": [
            {
                "question": "Hová látogatott el a két ifjú Baradlay fivér a császárvárosban?",
                "options": [
                    "A bécsi operaházba és a fényes bálterembe.",
                    "Egy vidéki kovácsműhelybe.",
                    "A dunai halászok csónakjába."
                ],
                "correct": 0,
                "explanation": "A testvérek a császári főváros kulturális központjába, a pompás operaelőadásra és az arisztokrata bálba érkeztek."
            },
            {
                "question": "Milyen művészi élmény hatott a legmélyebben Richárd szívére a színházban?",
                "options": [
                    "A zenekar csodálatos játéka és a színpad lenyűgöző látványa.",
                    "A büfében kapható hideg limonádé.",
                    "A jegyszedő bácsi fekete kabátja."
                ],
                "correct": 0,
                "explanation": "A romantikus zene harmóniája és a művészi előadás felejthetetlen élményt hagyott a fiatal katonatiszt lelkében."
            },
            {
                "question": "Miért volt a bál forgataga egyszerre vonzó és veszélyes az ifjak számára?",
                "options": [
                    "Mert a bécsi arisztokrácia fényes mosolya mögött politikai intrikák és feszültségek rejtőztek.",
                    "Mert a tánctér padlója túl csúszós volt a lakkcipőnek.",
                    "Mert a zenészek nem tudtak keringőt játszani."
                ],
                "correct": 0,
                "explanation": "A báltermek világa tele volt diplomáciai csapdákkal és titkokkal, miközben a pesti forradalom szele már közeledett."
            }
        ],
        "paragraphs": [
            {
                "type": "narration",
                "text": "A császári Bécs Operaházában a hatalmas kristálycsillárok arany fénnyel világították meg a páholyok selyemfüggönyeit. A bécsi társaság krémje gyűlt össze az ünnepi díszelőadásra."
            },
            {
                "type": "dialogue",
                "speaker": "Baradlay Richárd",
                "text": "Nézd csak, Ödön! Minél tovább nézem a színpadot, annál jobban elragad ez a csodálatos muzsika! Igazi felejthetetlen élmény ez a mai este."
            },
            {
                "type": "narration",
                "text": "Ödön mosolyogva biccentett fivérének. A zenekar fortissimóban játszott, a tenor éneke betöltötte a termet, és a közönség szűnni nem akaró tapssal jutalmazta a kiváló szereposztást."
            },
            {
                "type": "dialogue",
                "speaker": "Baradlay Ödön",
                "text": "Valóban fenséges művészet! De ne feledd, az előadás után a Plankenhorst-palota báljára vagyunk hivatalosak, ahol a diplomácia kártyáit keverik."
            },
            {
                "type": "narration",
                "text": "A színházi előadás végeztével hintójuk a kivilágított palotához gördült. A tágas bálteremben a keringő dallamára keringtek az elegáns párok, és a ragyogás elvakította a szemeket."
            },
            {
                "type": "dialogue",
                "speaker": "Plankenhorst Alfonsine",
                "text": "Örülök, hogy eljöttek, uraim! A magyar huszártisztek bátorsága éppoly híres a bálteremben, mint a csatamezőn."
            },
            {
                "type": "narration",
                "text": "Richárd gálánsan meghajolt, de a tekintete komoly maradt. A csillogó estély pompája mögött mindketten érezték a közeledő történelmi vihar előszeleit."
            },
            {
                "type": "dialogue",
                "speaker": "Baradlay Richárd",
                "text": "A zene és a szépség örök, kisasszony! De a hazánk hívó szava mindennél hangosabban cseng a fülünkben."
            }
        ]
    }
    write_json("content/hu/stories/classics/b1/b1-15-koszivuemberfiai.json", classic_story)

    # -------------------------------------------------------------------------
    # 4. Exercises Files (01 to 05 + consolidation)
    # -------------------------------------------------------------------------
    ex_01 = {
        "lesson": "b1-15-01",
        "exercises": [
            {
                "id": "b1-15-01.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["kiállítás", "art / museum exhibition"],
                    ["múzeumlátogatás", "museum visit"],
                    ["színházi előadás", "theatrical performance"],
                    ["koncertélmény", "concert experience"]
                ]
            },
            {
                "id": "b1-15-01.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Hogyan fejezzük ki a párhuzamos növekedést magyarul?",
                "options": [
                    "Minél többet olvasunk, annál műveltebbek leszünk.",
                    "Annyira olvasunk, amennyire leszünk okosak.",
                    "Minél olvasva, annál okosnak lenni."
                ],
                "correct": 0
            },
            {
                "id": "b1-15-01.ex03",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A Szépművészeti Múzeumban lenyűgöző reneszánsz ____ nyílt a hétvégén. (exhibition)",
                "answer": "kiállítás"
            },
            {
                "id": "b1-15-01.ex04",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Minél többet gyakorolsz a hangszeren, ____ szebben fog szólni a zene. (the more / all the more)",
                "answer": "annál"
            },
            {
                "id": "b1-15-01.ex05",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Mi a neve a színpadon bemutatott élő drámai vagy zenés játéknak?",
                "options": [
                    "színházi előadás",
                    "bevásárlólista",
                    "tudományos kísérlet"
                ],
                "correct": 0
            },
            {
                "id": "b1-15-01.ex06",
                "type": "sentence-builder",
                "category": "grammar",
                "sentence": "A tegnapi szimfonikus koncert felejthetetlen koncertélmény volt az egész család számára.",
                "tiles": ["A", "tegnapi", "szimfonikus", "koncert", "felejthetetlen", "koncertélmény", "volt", "az", "egész", "család", "számára."]
            },
            {
                "id": "b1-15-01.ex07",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A hétvégi budapesti ____ során megnéztük a Magyar Nemzeti Galéria kincseit. (museum visit)",
                "answer": "múzeumlátogatás"
            },
            {
                "id": "b1-15-01.ex08",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Melyik szófajképzővel képezzük a felsőfokot a melléknevekből?",
                "options": [
                    "a 'leg-' előtaggal (legszebb, legérdekesebb)",
                    "a '-ság' utótaggal",
                    "a '-kodik' igeképzővel"
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-15-01-ex.json", ex_01)

    ex_02 = {
        "lesson": "b1-15-02",
        "exercises": [
            {
                "id": "b1-15-02.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["ajánló", "recommendation / guide"],
                    ["kulturális program", "cultural event / program"],
                    ["jegyvásárlás", "ticket booking"],
                    ["helyszín", "venue / location"]
                ]
            },
            {
                "id": "b1-15-02.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Hogyan ajánlunk udvariasan egy programot: 'Mindenképpen...'?",
                "options": [
                    "érdemes megnézni a darabot",
                    "tilos megnézni a darabot",
                    "felesleges volt látni a darabot"
                ],
                "correct": 0
            },
            {
                "id": "b1-15-02.ex03",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A pénteki fesztivál ideális szabadtéri ____ lesz a Margitsziget. (venue)",
                "answer": "helyszíne"
            },
            {
                "id": "b1-15-02.ex04",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Ez a koncert annyira ritka alkalom, hogy kár ____ kihagyni! (would be a pity to)",
                "answer": "lenne"
            },
            {
                "id": "b1-15-02.ex05",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Hogyan hívjuk az újságokban megjelenő, programokat ismertető és ajánló rovatot?",
                "options": [
                    "programajánló",
                    "időjárás-jelentés",
                    "tőzsdei árfolyam"
                ],
                "correct": 0
            },
            {
                "id": "b1-15-02.ex06",
                "type": "sentence-builder",
                "category": "grammar",
                "sentence": "Mit szólnál ha a hétvégén elmennénk egy izgalmas kulturális programra a városba?",
                "tiles": ["Mit", "szólnál,", "ha", "a", "hétvégén", "elmennénk", "egy", "izgalmas", "kulturális", "programra", "a", "városba?"]
            },
            {
                "id": "b1-15-02.ex07",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "Az internetes ____ segítségével elkerülhetjük a hosszú sorban állást a pénztárnál. (ticket purchase)",
                "answer": "jegyvásárlás"
            },
            {
                "id": "b1-15-02.ex08",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Miért praktikus elővételben jegyet váltani a népszerű színházakba?",
                "options": [
                    "Mert az előadások gyakran hetekkel korábban teltházasak.",
                    "Mert a színházak csak délelőtt tartanak nyitva.",
                    "Mert a színészek nem játszanak, ha üres a nézőtér."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-15-02-ex.json", ex_02)

    ex_03 = {
        "lesson": "b1-15-03",
        "exercises": [
            {
                "id": "b1-15-03.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["filmkritika", "film review"],
                    ["rendező", "director"],
                    ["főszereplő", "lead actor / protagonist"],
                    ["szereposztás", "cast"]
                ]
            },
            {
                "id": "b1-15-03.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik kifejezés dicséri a színészi játékot egy kritikában?",
                "options": [
                    "hiteles és megrázó alakítás",
                    "unalmas és zavaros cselekmény",
                    "rosszul megvilágított díszlet"
                ],
                "correct": 0
            },
            {
                "id": "b1-15-03.ex03",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A film fiatal ____ nemzetközi díjat nyert a cannes-i fesztiválon. (director)",
                "answer": "rendezője"
            },
            {
                "id": "b1-15-03.ex04",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "Bár a forgatókönyv kissé hosszú volt, a zene és a látványvilág ____ lenyűgöző maradt. (completely)",
                "answer": "teljesen"
            },
            {
                "id": "b1-15-03.ex05",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Hogyan nevezzük a darabban játszó színészek együttesét?",
                "options": [
                    "szereposztás",
                    "zenekari árok",
                    "ruhatár"
                ],
                "correct": 0
            },
            {
                "id": "b1-15-03.ex06",
                "type": "sentence-builder",
                "category": "grammar",
                "sentence": "A szigorú filmkritika kiemelte a dráma rendkívüli erejét és a főszereplő tehetségét.",
                "tiles": ["A", "szigorú", "filmkritika", "kiemelte", "a", "dráma", "rendkívüli", "erejét", "és", "a", "főszereplő", "tehetségét."]
            },
            {
                "id": "b1-15-03.ex07",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A történelmi dráma tehetséges ____ könnyekig meghatotta a nézőket. (lead actor)",
                "answer": "főszereplője"
            },
            {
                "id": "b1-15-03.ex08",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Mi a jó kritikus legfőbb feladata?",
                "options": [
                    "Hogy tárgyilagosan és szakmai érvekkel mutassa be az alkotás értékeit és hiányosságait.",
                    "Hogy elárulja a bűnügyi film összes poénját az első mondatban.",
                    "Hogy elmondja, mennyi pattogatott kukoricát evett a moziban."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-15-03-ex.json", ex_03)

    ex_04 = {
        "lesson": "b1-15-04",
        "exercises": [
            {
                "id": "b1-15-04.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["néphagyomány", "folk tradition / folklore"],
                    ["kortárs művészet", "contemporary art"],
                    ["fesztivál", "cultural festival"],
                    ["kulturális örökség", "cultural heritage"]
                ]
            },
            {
                "id": "b1-15-04.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik állandósult szókapcsolattal fejezzük ki a szokások továbbadását?",
                "options": [
                    "nemzedékről nemzedékre öröklődik",
                    "fáról fára ugrál",
                    "szóról szóra felejtődik"
                ],
                "correct": 0
            },
            {
                "id": "b1-15-04.ex03",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A busójárás és a matyó hímzés a magyar ____ kiemelkedő értéke. (cultural heritage)",
                "answer": "kulturális örökség"
            },
            {
                "id": "b1-15-04.ex04",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A táncházmozgalom méltán ____ Hungarikumként az egész világon. (recognized / acknowledged)",
                "answer": "elismert"
            },
            {
                "id": "b1-15-04.ex05",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Hogyan hívjuk a ma élő alkotók által létrehozott modern műveket?",
                "options": [
                    "kortárs művészet",
                    "őskori lelet",
                    "óegyiptomi szobor"
                ],
                "correct": 0
            },
            {
                "id": "b1-15-04.ex06",
                "type": "sentence-builder",
                "category": "grammar",
                "sentence": "A nyári zenei fesztivál tízezreket vonz Magyarországra a világ minden tájáról.",
                "tiles": ["A", "nyári", "zenei", "fesztivál", "tízezreket", "vonz", "Magyarországra", "a", "világ", "minden", "tájáról."]
            },
            {
                "id": "b1-15-04.ex07",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A falusi közösségekben máig büszkén él a gazdag népi zenei ____. (folk tradition)",
                "answer": "néphagyomány"
            },
            {
                "id": "b1-15-04.ex08",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Miért fontos a néphagyományok és a kortárs művészet párbeszéde?",
                "options": [
                    "Mert a gyökerek megőrzése mellett új és friss gondolatokkal gazdagítja a kultúrát.",
                    "Mert a múzeumok nem szeretik a régi tárgyakat.",
                    "Mert a népdalokat csak modern hangszereken szabad énekelni."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-15-04-ex.json", ex_04)

    ex_05 = {
        "lesson": "b1-15-05",
        "exercises": [
            {
                "id": "b1-15-05.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["művészi ízlés", "artistic taste"],
                    ["élménybeszámoló", "account of an experience"],
                    ["műfaj", "genre"],
                    ["közönségsiker", "box-office / audience hit"]
                ]
            },
            {
                "id": "b1-15-05.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik híres magyar közmondás fejezi ki, hogy az esztétikai megítélés egyéni?",
                "options": [
                    "Ízlések és pofonok különbözők.",
                    "Ki korán kel, aranyat lel.",
                    "Lassan járj, tovább érsz."
                ],
                "correct": 0
            },
            {
                "id": "b1-15-05.ex03",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A történelmi kalandregény hatalmas ____ aratott a könyvolvasók körében. (audience success)",
                "answer": "közönségsikert"
            },
            {
                "id": "b1-15-05.ex04",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A klasszikus zene mindig is rendkívül közel állt a ____. (to my heart)",
                "answer": "szívemhez"
            },
            {
                "id": "b1-15-05.ex05",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Hogyan nevezzük az irodalmi vagy zenei művek kategóriáját (pl. dráma, komédia, krimi)?",
                "options": [
                    "műfaj",
                    "díszlet",
                    "belépőjegy"
                ],
                "correct": 0
            },
            {
                "id": "b1-15-05.ex06",
                "type": "sentence-builder",
                "category": "grammar",
                "sentence": "A magazinban megjelent részletes élménybeszámoló kedvet csinált a színházi esthez.",
                "tiles": ["A", "magazinban", "megjelent", "részletes", "élménybeszámoló", "kedvet", "csinált", "a", "színházi", "esthez."]
            },
            {
                "id": "b1-15-05.ex07",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A kifinomult ____ rendelkező nézők nagyra értékelték az operaelőadás finomságait. (artistic taste)",
                "answer": "művészi ízléssel"
            },
            {
                "id": "b1-15-05.ex08",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Miért tekinthető Jókai Mór 'A kőszívű ember fiai' című regénye a magyar romantika csúcsának?",
                "options": [
                    "Mert lenyűgöző stílusban, mély emberi drámával és hazaszeretettel mutatja be az 1848-as szabadságharc korát.",
                    "Mert receptkönyvként is használható a konyhában.",
                    "Mert mindössze három oldalból áll a teljes történet."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-15-05-ex.json", ex_05)

    ex_consolidation = {
        "lesson": "b1-15-consolidation",
        "exercises": [
            {
                "id": "b1-15-consolidation.ex01",
                "type": "matching",
                "category": "vocabulary",
                "pairs": [
                    ["színházi előadás", "theater performance"],
                    ["jegyvásárlás", "ticket booking"],
                    ["filmkritika", "film review"],
                    ["közönségsiker", "audience hit"]
                ]
            },
            {
                "id": "b1-15-consolidation.ex02",
                "type": "multiple-choice",
                "category": "grammar",
                "question": "Melyik mondatban szerepel helyesen a 'minél... annál...' szerkezet?",
                "options": [
                    "Minél több filmet nézel eredeti nyelven, annál gyorsabban fejlődik a szókincsed.",
                    "Minél több filmet nézel eredeti nyelven, de annál szebb a mozi.",
                    "Minél filmet nézve, annál jobb volt lenni."
                ],
                "correct": 0
            },
            {
                "id": "b1-15-consolidation.ex03",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A budapesti Művészetek Palotája nemzetközileg elismert zenei és kulturális ____. (venue)",
                "answer": "helyszín"
            },
            {
                "id": "b1-15-consolidation.ex04",
                "type": "fill-blank",
                "category": "grammar",
                "sentence": "A tegnapi operaelőadás a ____ élmény volt, amit valaha átéltem. (most beautiful)",
                "answer": "legszebb"
            },
            {
                "id": "b1-15-consolidation.ex05",
                "type": "sentence-builder",
                "category": "grammar",
                "sentence": "A gazdag magyar kulturális örökség megőrzése minden generáció közös felelőssége.",
                "tiles": ["A", "gazdag", "magyar", "kulturális", "örökség", "megőrzése", "minden", "generáció", "közös", "felelőssége."]
            },
            {
                "id": "b1-15-consolidation.ex06",
                "type": "multiple-choice",
                "category": "vocabulary",
                "question": "Hogyan jellemeznénk azt a színházi darabot, amelyre heteken át minden jegy elkelt?",
                "options": [
                    "óriási közönségsiker",
                    "zártkörű kudarc",
                    "félbehagyott próba"
                ],
                "correct": 0
            },
            {
                "id": "b1-15-consolidation.ex07",
                "type": "fill-blank",
                "category": "vocabulary",
                "sentence": "A hétvégi szegedi fesztiválon a legnépszerűbb magyar ____ léptek fel. (performers / lead actors)",
                "answer": "főszereplők"
            },
            {
                "id": "b1-15-consolidation.ex08",
                "type": "multiple-choice",
                "category": "reading",
                "question": "Hogyan ábrázolta Jókai Mór a Baradlay fivérek bécsi színházi estéjét?",
                "options": [
                    "A császárvárosi pompa, a zene és az elragadó művészet élményén keresztül, amely mögött felsejlik a haza sorsa.",
                    "Egy unalmas tanóraként a gimnáziumban.",
                    "Egy katonai börtön hideg cellájában."
                ],
                "correct": 0
            }
        ]
    }
    write_json("content/hu/exercises/b1/b1-15-consolidation-ex.json", ex_consolidation)

    # -------------------------------------------------------------------------
    # 5. Lesson Files (01 to 05 + consolidation)
    # -------------------------------------------------------------------------
    for i in range(1, 6):
        padded = f"0{i}"
        titles = {
            "01": ("The More, the Better", "Minél több, annál jobb"),
            "02": ("Recommending Something", "Ajánlások és programok"),
            "03": ("A Film or Show, Reviewed", "Színház, mozi és kritika"),
            "04": ("Hungarian Culture Today", "Kulturális élet Magyarországon"),
            "05": ("Talking About Taste", "Ízlések és élmények")
        }
        en_title, hu_title = titles[padded]
        lesson_data = {
            "id": f"lesson.b1.15-{padded}",
            "unit": 15,
            "title": en_title,
            "level": "B1",
            "grammar": "Correlative Comparatives (minél... annál...) & Cultural Discourse",
            "goal": [
                f"I can understand and use vocabulary for {en_title.lower()}.",
                "I can use correlative comparatives (minél... annál...) and superlatives in Hungarian.",
                "I can review cultural events, recommend outings, and discuss artistic taste.",
                "I can master four new target vocabulary items in authentic context."
            ],
            "sections": [
                {
                    "type": "goal",
                    "title": "Lesson Goals",
                    "items": [
                        f"I can understand and use vocabulary for {en_title.lower()}.",
                        "I can use correlative comparatives (minél... annál...) and superlatives in Hungarian.",
                        "I can review cultural events, recommend outings, and discuss artistic taste.",
                        "I can master four new target vocabulary items in authentic context."
                    ]
                },
                {"type": "recycle", "title": "Quick Review"},
                {"type": "grammar", "ref": f"grammar/b1/b1-15-{padded}-a-gr.json"},
                {"type": "grammar", "ref": f"grammar/b1/b1-15-{padded}-b-gr.json"},
                {"type": "vocabulary", "title": "Lesson Vocabulary", "ref": f"vocabulary/b1/b1-15-{padded}-voc.json"},
                {
                    "type": "practice",
                    "title": "Practice",
                    "ref": f"exercises/b1/b1-15-{padded}-ex.json"
                }
            ]
        }
        write_json(f"content/hu/lessons/b1/b1-15-{padded}.json", lesson_data)

    consolidation_data = {
        "id": "lesson.b1.15-consolidation",
        "unit": 15,
        "title": "Unit 15 Consolidation",
        "level": "B1",
        "grammar": "Consolidation of Correlatives & Cultural Competence",
        "sections": [
            {
                "type": "story",
                "title": "A bécsi színházban és a bál forgatagában",
                "ref": "stories/classics/b1/b1-15-koszivuemberfiai.json"
            },
            {
                "type": "practice",
                "title": "Consolidation Practice",
                "ref": "exercises/b1/b1-15-consolidation-ex.json"
            }
        ]
    }
    write_json("content/hu/lessons/b1/b1-15-consolidation.json", consolidation_data)
    print("Successfully built Hungarian B1 Core Unit 15 (b1-15)!")

if __name__ == "__main__":
    build_unit_15_core()
