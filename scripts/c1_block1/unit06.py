#!/usr/bin/env python3
"""
Hungarian C1 Block 1 - Unit 06 Generator:
  - Track 1 (Core): Unit 6 — "Metaphor, Idiomatic Resonance & Conceptual Blending" (c1-06)
  - Track 2 (Discourse): Unit 6 — "The Metaphorical Landscape of Hungarian" (c1-metaforak)
"""

from .common import mc, match, fb, sb, dc, sw, write_json, emit_instructional_lesson, emit_consolidation_lesson


def generate_unit_6():
    print("=== Generating C1 Unit 6 ===")
    
    # ----------------------------------------------------
    # TRACK 1: CORE (c1-06)
    # ----------------------------------------------------
    core_title = "Metaphor, Idiomatic Resonance & Conceptual Blending"
    core_intro = [
        "Metaphor in C1 Hungarian is not mere decorative ornament; it is the fundamental cognitive framework through which abstract concepts, moral dilemmas, and existential conditions are experienced.",
        "In this unit, inspired by János Pilinszky's radical poetic essays in 'Szög és olaj', you will master high-register idiomatic compounds (kétélű fegyver, sarokkő, vízválasztó), conceptual blending, deadjectival nominalizations, and poetic minimalism."
    ]

    core_lessons = [
        {
            "num": 1,
            "stem": "c1-06-01",
            "title": "High-Register Idiomatic Compounds: Kétélű fegyver and Sarokkő",
            "grammar_title": "Metaphoric Compound Nouns and Abstract Conceptual Idioms",
            "grammar_skill": "c1-idiomatic-compounding",
            "goals": [
                "I can employ elevated idiomatic compounds (*kétélű fegyver, sarokkő, vízválasztó, zsákutca*).",
                "I can analyze how physical source domains structure abstract intellectual discourse.",
                "I can construct arguments using metaphoric milestone terminology in Hungarian."
            ],
            "vocab": [
                {"lemma": "kétélű fegyver", "translation": "double-edged sword", "pos": "expression"},
                {"lemma": "sarokkő", "translation": "cornerstone, keystone", "pos": "noun"},
                {"lemma": "vízválasztó", "translation": "watershed moment, turning point", "pos": "noun"},
                {"lemma": "zsákutca", "translation": "dead end, cul-de-sac", "pos": "noun"},
                {"lemma": "mérföldkő", "translation": "milestone", "pos": "noun"},
                {"lemma": "forrástartomány", "translation": "source domain (cognitive metaphor)", "pos": "noun"},
                {"lemma": "céltartomány", "translation": "target domain", "pos": "noun"},
                {"lemma": "fogalmi leképezés", "translation": "conceptual mapping", "pos": "noun"}
            ],
            "gr_text1": "Advanced Hungarian discourse relies heavily on crystallized metaphoric compounds. Physical landmarks (*vízválasztó, sarokkő, mérföldkő*) map onto historical and intellectual developments, while cautionary objects (*kétélű fegyver, zsákutca*) signal peril.",
            "gr_text2": "When deploying these idioms, ensure stylistic coherence: do not mix incompatible source domains (*nem szabad képzavart teremteni*).",
            "gr_table": [
                ["A reformok igazi vízválasztónak bizonyultak.", "The reforms proved to be a real watershed."],
                ["Ez a technológia kétélű fegyver az emberiség kezében.", "This technology is a double-edged sword in humanity's hands."],
                ["A jogállamiság a demokrácia elengedhetetlen sarokköve.", "The rule of law is the indispensable cornerstone of democracy."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mit fejez ki a 'vízválasztó' metafora a történeti érvelésben?", ["Egy döntő korszakhatárt vagy visszafordíthatatlan fordulatot.", "Egy hegyvidéki patak forrását.", "A választási törvények módosítását."], 0, ["c1-06-vocab"]),
                fb("grammar", "controlled", "A mesterséges intelligencia fejlődése _____ fegyver: egyszerre hatalmas lehetőség és kockázat. (double-edged / kétélű)", "kétélű", "The development of artificial intelligence is a double-edged sword: both an immense opportunity and a risk.", ["c1-idiomatic-compounding"]),
                match("vocabulary", "controlled", [["kétélű fegyver", "double-edged sword"], ["sarokkő", "cornerstone"], ["vízválasztó", "watershed moment"], ["zsákutca", "dead end"]], ["c1-06-vocab"]),
                fb("grammar", "practice", "A megállapodás létrejötte történelmi _____ jelent a két ország kapcsolatában. (milestone / mérföldkövet)", "mérföldkövet", "The realization of the agreement marks a historic milestone in relations between the two countries.", ["c1-idiomatic-compounding"]),
                sb("grammar", "practice", ["A", "tárgyalások", "egy", "veszélyes", "zsákutcába", "jutottak", "a", "nézeteltérések", "miatt."], ["A", "tárgyalások", "egy", "veszélyes", "zsákutcába", "jutottak", "a", "nézeteltérések", "miatt."], "The negotiations reached a dangerous dead end due to disagreements.", ["c1-idiomatic-compounding"]),
                dc("dialogue", [
                    {"speaker": "Elemző", "text": "Hogyan értékeli a tegnapi választási eredményt?"},
                    {"speaker": "Politológus", "text": "Ez egyértelmű vízválasztó: a politikai korszak lezárult."},
                ], ["egyértelmű vízválasztó", "jelentéktelen apróság", "semmi sem változott"], 0, ["c1-idiomatic-compounding"]),
                sw("production", [{"prompt": "Write a sentence using 'sarokkő' to describe an intellectual or moral foundation.", "answer": "Az emberi jogok feltétlen tisztelete a modern társadalom legfontosabb sarokköve."}], ["c1-idiomatic-compounding"]),
                mc("grammar", "check", "Melyik mondat alkalmaz hibátlan, képzavarmentes metaforikus összetételt?", [
                    "A békeszerződés a stabilitás sarokköveként szolgált évtizedeken át.",
                    "A sarokkő elúszott a vízválasztó hullámain a zsákutcába.",
                    "Kétélű karddal vágta át a mérföldkő madzagját."
                ], 0, ["c1-idiomatic-compounding"])
            ]
        },
        {
            "num": 2,
            "stem": "c1-06-02",
            "title": "Abstract Nominalizations: Valóságérzék and Felelősségtudat",
            "grammar_title": "Deadjectival and Nominal Abstract Compounds in Philosophical Discourse",
            "grammar_skill": "c1-deadjectival-abstraction",
            "goals": [
                "I can form and deploy abstract mental and moral compounds (*valóságérzék, lényeglátás, felelősségtudat, hivatástudat*).",
                "I can synthesize complex emotional and philosophical states into single words.",
                "I can write elevated character and culture evaluations in Hungarian."
            ],
            "vocab": [
                {"lemma": "valóságérzék", "translation": "sense of reality, realism", "pos": "noun"},
                {"lemma": "lényeglátás", "translation": "insight, perception of essentials", "pos": "noun"},
                {"lemma": "felelősségtudat", "translation": "sense of responsibility", "pos": "noun"},
                {"lemma": "hivatástudat", "translation": "sense of vocation, professional dedication", "pos": "noun"},
                {"lemma": "önismeret", "translation": "self-knowledge, self-awareness", "pos": "noun"},
                {"lemma": "értékrend", "translation": "value system, hierarchy of values", "pos": "noun"},
                {"lemma": "szilárdság", "translation": "firmness, solidity, integrity", "pos": "noun"},
                {"lemma": "erkölcsi tartás", "translation": "moral backbone, moral posture", "pos": "noun"}
            ],
            "gr_text1": "Hungarian has exceptional capacity to create compact abstract nouns combining a nominal base with *-érzék* (sense), *-tudat* (consciousness), or *-rend* (order): *valóságérzék, felelősségtudat, értékrend*.",
            "gr_text2": "These deadjectival and nominal compounds elevate discourse from episodic narrative to timeless philosophical evaluation: *A vezető legnagyobb erénye a mélységes felelősségtudat és a csalhatatlan lényeglátás.*",
            "gr_table": [
                ["A politikus csalhatatlan valóságérzéke...", "The politician's infallible sense of reality..."],
                ["Mély felelősségtudattal viseltetni a jövő iránt...", "To bear deep sense of responsibility toward the future..."],
                ["Szilárd erkölcsi tartás és tiszta értékrend...", "Firm moral backbone and clear value system..."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mit fejez ki a 'lényeglátás' összetett főnév?", ["Azt a képességet, hogy valaki azonnal felismeri a legfontosabbat a mellékes részletek között.", "A jó látásélességet a szemészetben.", "A távoli hegyek megfigyelését."], 0, ["c1-06-vocab"]),
                fb("grammar", "controlled", "A válságban a vezetők elveszítették elemi _____ és téves döntéseket hoztak. (sense of reality / valóságérzéküket)", "valóságérzéküket", "In the crisis, leaders lost their elementary sense of reality and made mistaken decisions.", ["c1-deadjectival-abstraction"]),
                match("vocabulary", "controlled", [["valóságérzék", "sense of reality"], ["lényeglátás", "perception of essentials"], ["felelősségtudat", "sense of responsibility"], ["erkölcsi tartás", "moral backbone"]], ["c1-06-vocab"]),
                fb("grammar", "practice", "A nehéz történelmi időkben a tiszta erkölcsi _____ mentette meg a nemzetet. (moral backbone / tartás)", "tartás", "In difficult historical times, pure moral backbone saved the nation.", ["c1-deadjectival-abstraction"]),
                sb("grammar", "practice", ["A", "tudományos", "kutatás", "mély", "felelősségtudatot", "és", "alázatot", "követel."], ["A", "tudományos", "kutatás", "mély", "felelősségtudatot", "és", "alázatot", "követel."], "Scientific research demands deep sense of responsibility and humility.", ["c1-deadjectival-abstraction"]),
                dc("dialogue", [
                    {"speaker": "Egyetemi rektor", "text": "Milyen tulajdonságokat kell átadnunk a diákoknak?"},
                    {"speaker": "Professzor", "text": "A szilárd értékrendet, a lényeglátást és a valódi hivatástudatot."},
                ], ["szilárd értékrendet", "a könnyelműséget", "a felelőtlenséget"], 0, ["c1-deadjectival-abstraction"]),
                sw("production", [{"prompt": "Write a sentence using 'felelősségtudat' and 'értékrend'.", "answer": "A hiteles szellemi ember tetteit a mélységes felelősségtudat és a világos értékrend vezérli."}], ["c1-deadjectival-abstraction"]),
                mc("grammar", "check", "Melyik fogalom jelöli a moralitás és belső méltóság szilárdságát?", [
                    "Az erkölcsi tartás és a szilárd értékrend.",
                    "A pillanatnyi szeszély.",
                    "A pénzügyi vagyon."
                ], 0, ["c1-deadjectival-abstraction"])
            ]
        },
        {
            "num": 3,
            "stem": "c1-06-03",
            "title": "Conceptual Blending in Argumentation: Hidat ver and Zátonyra fut",
            "grammar_title": "Verbal Metaphoric Collocations and Conceptual Blending",
            "grammar_skill": "c1-conceptual-blending",
            "goals": [
                "I can employ verbal metaphoric collocations (*hidat ver, zátonyra fut, gúzsba köt, gyökeret ver*).",
                "I can analyze conceptual blending where multiple metaphors merge harmoniously.",
                "I can construct dynamic argument narratives using figurative verbs in Hungarian."
            ],
            "vocab": [
                {"lemma": "hidat ver", "translation": "to bridge, build a bridge (between)", "pos": "expression"},
                {"lemma": "zátonyra fut", "translation": "to run aground, fail, founder", "pos": "expression"},
                {"lemma": "gúzsba köt", "translation": "to fetter, shackle, tie down hand and foot", "pos": "expression"},
                {"lemma": "gyökeret ver", "translation": "to take root, strike root", "pos": "expression"},
                {"lemma": "tükröt tart", "translation": "to hold up a mirror", "pos": "expression"},
                {"lemma": "fogalmi integráció", "translation": "conceptual blending / integration", "pos": "noun"},
                {"lemma": "metaforikus háló", "translation": "metaphoric network / grid", "pos": "noun"},
                {"lemma": "szemléletesség", "translation": "vividness, graphic clarity", "pos": "noun"}
            ],
            "gr_text1": "Hungarian verbal metaphors (*igei metaforák*) inject physical dynamism into abstract argumentation. When negotiations fail, they *zátonyra futnak* (run aground like a ship); when an author connects cultures, they *hidat vernek* (erect a bridge).",
            "gr_text2": "Conceptual blending (*fogalmi integráció*) allows writers to combine these collocations smoothly: *A bürokrácia gúzsba köti az alkotóerőt, így az innováció könnyen zátonyra fut.*",
            "gr_table": [
                ["A párbeszéd hidat vert a két kultúra között.", "Dialogue built a bridge between the two cultures."],
                ["A merev szabályozás gúzsba köti a kezdeményezést.", "Rigid regulation shackles initiative."],
                ["A kísérlet a pénzhiány miatt zátonyra futott.", "The experiment ran aground due to lack of funds."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mit jelent a 'zátonyra fut' metaforikus kifejezés az érvelésben?", ["Egy terv vagy folyamat megakadását és kudarcát.", "Egy hajó sikeres kikötését a tengeren.", "A tengerbiológiai kutatás sikerét."], 0, ["c1-06-vocab"]),
                fb("grammar", "controlled", "A két tudományág közötti párbeszéd sikeresen _____ vert az elmélet és a gyakorlat között. (built a bridge / hidat)", "hidat", "Dialogue between the two disciplines successfully built a bridge between theory and practice.", ["c1-conceptual-blending"]),
                match("vocabulary", "controlled", [["hidat ver", "to build a bridge"], ["zátonyra fut", "to run aground"], ["gúzsba köt", "to shackle / fetter"], ["gyökeret ver", "to take root"]], ["c1-06-vocab"]),
                fb("grammar", "practice", "A túlzott bürokrácia szinte teljesen _____ köti a gazdasági kezdeményezést. (fetters / gúzsba)", "gúzsba", "Excessive bureaucracy almost completely fetters economic initiative.", ["c1-conceptual-blending"]),
                sb("grammar", "practice", ["Az", "új", "eszmék", "hamar", "mély", "gyökeret", "vertek", "a", "társadalomban."], ["Az", "új", "eszmék", "hamar", "mély", "gyökeret", "vertek", "a", "társadalomban."], "The new ideas soon took deep root in society.", ["c1-conceptual-blending"]),
                dc("dialogue", [
                    {"speaker": "Tárgyalófél", "text": "Hogyan állnak a béketárgyalások?"},
                    {"speaker": "Közvetítő", "text": "Sajnos a merev álláspontok miatt a folyamat zátonyra futott."},
                ], ["folyamat zátonyra futott", "minden megoldódott tegnap", "azonnal véget ért a háború"], 0, ["c1-conceptual-blending"]),
                sw("production", [{"prompt": "Write a sentence using 'gúzsba köt' to criticize censorship.", "answer": "A cenzúra erőszakkal gúzsba kötötte a szabad gondolatot és a művészi önkifejezést."}], ["c1-conceptual-blending"]),
                mc("grammar", "check", "Melyik állítás alkalmaz találó igei metaforát a kultúraközi megértésre?", [
                    "A műfordítás hidat ver a különböző nemzetek szellemi világa között.",
                    "A műfordítás zátonyra fut a szótárban.",
                    "A műfordítás gúzsba köti a könyveket."
                ], 0, ["c1-conceptual-blending"])
            ]
        },
        {
            "num": 4,
            "stem": "c1-06-04",
            "title": "Poetic Density and Semantic Compression in Modern Prose",
            "grammar_title": "Semantic Density, Ellipsis, and Poetic Weight in Non-Fiction",
            "grammar_skill": "c1-conceptual-blending",
            "goals": [
                "I can analyze extreme semantic compression in Hungarian modernist prose.",
                "I can evaluate how ellipsis (*kihagyás*) and silence function as rhetorical elements.",
                "I can write sentences with high conceptual density and poetic weight."
            ],
            "vocab": [
                {"lemma": "jelentéssűrítés", "translation": "semantic compression / condensation", "pos": "noun"},
                {"lemma": "kihagyás", "translation": "ellipsis, omission", "pos": "noun"},
                {"lemma": "szűkszavúság", "translation": "laconicism, brevity, reticence", "pos": "noun"},
                {"lemma": "súlyosság", "translation": "gravity, weightiness", "pos": "noun"},
                {"lemma": "áttetsző", "translation": "translucent, transparent", "pos": "adjective"},
                {"lemma": "szikár", "translation": "lean, wiry, austere (style)", "pos": "adjective"},
                {"lemma": "töredékesség", "translation": "fragmentariness", "pos": "noun"},
                {"lemma": "tömörség", "translation": "conciseness, compactness", "pos": "noun"}
            ],
            "gr_text1": "In Hungarian modernist essays, elegance is achieved not by ornamentation, but by radical stripping away (*szikár stílus*). Words carry immense associative weight, and silence (*a csend jelenléte*) becomes an active syntactic element.",
            "gr_text2": "Semantic compression (*jelentéssűrítés*) relies on juxtapositions where subordinate conjunctions are omitted, forcing the reader to contemplate the stark conceptual clash.",
            "gr_table": [
                ["Szikár, dísztelen, mégis mélyen megrendítő próza...", "Austere, unadorned, yet profoundly moving prose..."],
                ["A szavak rendkívüli jelentéssűrítése...", "The extraordinary semantic compression of words..."],
                ["A kihagyás és a csend művészete...", "The art of ellipsis and silence..."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mit jelent a 'szikár stílus' az irodalomkritikában?", ["Dísztelen, szigorúan tömör, felesleges sallangoktól mentes prózát.", "Hosszú, virágos mondatokat.", "Humoros történetmesélést."], 0, ["c1-06-vocab"]),
                fb("grammar", "controlled", "A szerző prózáját a rendkívüli formai fegyelem és a szikár _____ jellemzi. (conciseness / tömörség)", "tömörség", "The author's prose is characterized by extraordinary formal discipline and austere conciseness.", ["c1-conceptual-blending"]),
                match("vocabulary", "controlled", [["jelentéssűrítés", "semantic compression"], ["szikár", "austere / lean"], ["kihagyás", "ellipsis"], ["szűkszavúság", "laconicism"]], ["c1-06-vocab"]),
                fb("grammar", "practice", "A mű ereje a kimondatlan szavak súlyában és a csend szándékos _____ rejlik. (presence / jelenlétében)", "jelenlétében", "The power of the work lies in the weight of unspoken words and the deliberate presence of silence.", ["c1-conceptual-blending"]),
                sb("grammar", "practice", ["A", "legmélyebb", "igazságok", "gyakran", "szikár", "egyszerűségben", "mutatkoznak", "meg."], ["A", "legmélyebb", "igazságok", "gyakran", "szikár", "egyszerűségben", "mutatkoznak", "meg."], "The deepest truths often reveal themselves in austere simplicity.", ["c1-conceptual-blending"]),
                dc("dialogue", [
                    {"speaker": "Kritikus", "text": "Nem túl száraz ez a szöveg a díszek nélkül?"},
                    {"speaker": "Irodalmár", "text": "Nem száraz, hanem szikár: minden felesleges szót lehántott a lényegről."},
                ], ["minden felesleges szót lehántott", "nem volt ideje befejezni", "elfelejtette a szavakat"], 0, ["c1-conceptual-blending"]),
                sw("production", [{"prompt": "Write a sentence reflecting on the power of an austere literary style.", "answer": "A szikár próza ereje abban áll, hogy a szavak dísztelen tisztaságukban ragyognak fel."}], ["c1-conceptual-blending"]),
                mc("grammar", "check", "Melyik stíluseszköz hoz létre maximális jelentéssűrítést a mondatban?", [
                    "A szikár pontosság és a funkcionális kihagyás (ellipszis).",
                    "A jelzők és szinonimák végtelen halmozása.",
                    "A latin mondások folyamatos idézése."
                ], 0, ["c1-conceptual-blending"])
            ]
        },
        {
            "num": 5,
            "stem": "c1-06-05",
            "title": "Minimalism and Existential Silence: János Pilinszky",
            "grammar_title": "Sacred Minimalism and Existential Reductio in Pilinszky's Essays",
            "grammar_skill": "c1-deadjectival-abstraction",
            "goals": [
                "I can analyze János Pilinszky's radical poetic essays in 'Szög és olaj'.",
                "I can evaluate the concept of sacred minimalism, suffering, and existential silence.",
                "I can write on metaphysical and existential themes with C1 linguistic rigor."
            ],
            "vocab": [
                {"lemma": "minimalizmus", "translation": "minimalism", "pos": "noun"},
                {"lemma": "létállapot", "translation": "state of being, existential state", "pos": "noun"},
                {"lemma": "megszólalásig", "translation": "to the point of speaking, uncannily", "pos": "adverb"},
                {"lemma": "szótlan", "translation": "wordless, silent, mute", "pos": "adjective"},
                {"lemma": "kegyelem", "translation": "grace, mercy", "pos": "noun"},
                {"lemma": "megrendültség", "translation": "profound emotional shock, awe", "pos": "noun"},
                {"lemma": "áldozat", "translation": "sacrifice, victim", "pos": "noun"},
                {"lemma": "tisztaság", "translation": "purity, clarity", "pos": "noun"}
            ],
            "gr_text1": "János Pilinszky's essay collection *Szög és olaj* (Nail and Oil) is a monument of spiritual reduction. Writing in the shadow of Auschwitz, Pilinszky believed that post-war literature could not return to talkative rhetoric; it must stand wordless (*szótlan*) before the mystery of suffering and grace (*kegyelem*).",
            "gr_text2": "His prose strips away adjectives to achieve absolute metaphysical weight: *A művészet nem önkifejezés, hanem önfeladás: a csend megnyitása a kegyelem előtt.*",
            "gr_table": [
                ["A radikális szellemi minimalizmus ereje...", "The power of radical spiritual minimalism..."],
                ["Szótlan megrendültség a tragédia előtt...", "Wordless awe before tragedy..."],
                ["A művészet mint önfeladás és tiszta figyelem...", "Art as self-abandonment and pure attention..."]
            ],
            "classic_story": {
                "slug": "c1-06-pilinszky",
                "author": "Pilinszky János",
                "work": "Szög és olaj (1982)",
                "title": "A csend súlya és a létezés tisztasága",
                "summary": "János Pilinszky profound meditations on post-war tragedy, Simone Weil, and how authentic art renounces rhetoric to bear witness to transcendent truth.",
                "characters": ["Pilinszky János"],
                "paragraphs": [
                    {"type": "narration", "text": "Amikor Pilinszky János a Szög és olaj esszéiben tollat ragadott, nem irodalmi sikerekre vagy szellemes fordulatokra vágyott. Számára a huszadik század kataklizmái – a lágerek, a pusztulás és az emberi gonoszság mélységei – után a hagyományos, bőbeszédű irodalom végleg érvényét vesztette. Ott, ahol a borzalom meghaladja a képzeletet, a szófacsarás árulássá válik."},
                    {"type": "narration", "text": "Pilinszky a csend költője és gondolkodója volt. Nagy hatással volt rá Simone Weil keresztény misztikája: vallotta, hogy az igazi figyelem az imádság legtisztább formája. Az író nem az, aki mindent meg tud magyarázni, hanem az, aki képes szótlanul megállni a világ botránya és a létezés törékenysége előtt."},
                    {"type": "narration", "text": "Prózája rendkívül szikár, szinte aszkétikus. Lehántott minden díszt, minden felesleges melléknevet, hogy megmaradjon a lényeg: a szög és az olaj, a seb és a gyógyulás, a szenvedés és a megváltó kegyelem örök drámája. Sorai nem vitatkoznak: felmutatnak és tanúságot tesznek."},
                    {"type": "narration", "text": "Pilinszky tanítása ma is eleven mérce: arra figyelmeztet, hogy a nyelv nem az önző hiúság játékszere, hanem az igazság szentélye, ahol a legnagyobb szavak mindig a csendből születnek meg."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Miért fordult Pilinszky János a szikár minimalizmus felé a háború után?", [
                    "Mert úgy érezte, a huszadik század tragédiái után a bőbeszédű retorika érvényét vesztette, és csak a csend képes tanúságot tenni.",
                    "Mert túl drága volt a papír a könyvkiadáshoz.",
                    "Mert elfelejtette a nyelvtani szabályokat."
                ], 0, ["c1-06-vocab"]),
                fb("grammar", "practice", "Pilinszky írásait a radikális szellemi tisztaság és a mély megrendültség _____ jellemzi. (state of being / létállapota)", "létállapota", "Pilinszky's writings are characterized by the state of being of radical spiritual purity and profound awe.", ["c1-deadjectival-abstraction"]),
                match("vocabulary", "controlled", [["minimalizmus", "minimalism"], ["létállapot", "state of being"], ["kegyelem", "grace / mercy"], ["szótlan", "wordless / silent"]], ["c1-06-vocab"]),
                mc("reading", "practice", "Kinek a szellemi hatása volt meghatározó Pilinszky gondolkodására a szöveg szerint?", [
                    "Simone Weil keresztény misztikus filozófiája.",
                    "A francia szürrealisták politikai kiáltványai.",
                    "A bécsi pozitivista kör logikája."
                ], 0, None),
                mc("reading", "practice", "Hogyan határozza meg a szöveg az igazi figyelmet Pilinszky nyomán?", [
                    "Az igazi figyelem az imádság legtisztább formája.",
                    "A figyelem csupán a memóriát segíti.",
                    "A figyelem az ellenfél legyőzésének eszköze."
                ], 0, None),
                sb("grammar", "practice", ["A", "legnagyobb", "szavak", "mindig", "a", "mély", "csendből", "születnek", "meg."], ["A", "legnagyobb", "szavak", "mindig", "a", "mély", "csendből", "születnek", "meg."], "The greatest words are always born out of deep silence.", ["c1-deadjectival-abstraction"]),
                sw("production", [{"prompt": "Write a philosophical sentence on Pilinszky's view of silence and truth.", "answer": "Pilinszky művészetében a csend nem üresség, hanem a transzcendens igazság legtisztább jelenléte."}], ["c1-deadjectival-abstraction"]),
                mc("grammar", "check", "Melyik megfogalmazás ragadja meg a pilinszkyi próza legfőbb lényegét?", [
                    "A szikár, aszkétikus tömörség és a megrendült szellemi tanúságtétel.",
                    "A könnyed, vidám társasági fecsegés.",
                    "A tudományos lábjegyzetek halmozása."
                ], 0, ["c1-deadjectival-abstraction"])
            ]
        }
    ]

    for l in core_lessons:
        emit_instructional_lesson(6, "core", l, core_title, core_intro if l["num"] == 1 else None)

    # Core Consolidation
    emit_consolidation_lesson(
        6,
        "core",
        "c1-06-consolidation",
        core_title,
        [
            "I can deploy high-register idiomatic compounds (kétélű fegyver, sarokkő, vízválasztó).",
            "I can utilize abstract deverbal compounds (valóságérzék, felelősségtudat).",
            "I can integrate verbal conceptual blends and analyze poetic minimalism."
        ],
        [
            mc("grammar", "recognize", "Mit fejez ki a 'kétélű fegyver' metafora?", [
                "Olyan eszközt, amely egyszerre hordoz jelentős előnyöket és súlyos kockázatokat.",
                "Egy ókori kardot a múzeumban.",
                "Egy teljesen haszontalan dolgot."
            ], 0, ["c1-idiomatic-compounding"]),
            mc("grammar", "recognize", "Melyik kifejezés testesíti meg az erkölcsi szilárdságot és érettséget?", [
                "A felelősségtudat és a szilárd erkölcsi tartás.",
                "A pillanatnyi hirtelen harag.",
                "A szabályok állandó megszegése."
            ], 0, ["c1-deadjectival-abstraction"]),
            match("vocabulary", "recognize", [["vízválasztó", "watershed moment"], ["sarokkő", "cornerstone"], ["valóságérzék", "sense of reality"], ["hidat ver", "to build a bridge"], ["szikár", "austere / lean"]], ["c1-06-vocab"]),
            fb("vocabulary", "recall", "A tárgyalások eredménye valódi _____ bizonyult a diplomáciai kapcsolatokban. (watershed / vízválasztónak)", "vízválasztónak", "The result of the negotiations proved to be a genuine watershed in diplomatic relations.", ["c1-06-vocab"]),
            fb("vocabulary", "recall", "A tudósoknak nem szabad elveszíteniük a józan _____ a kutatás során. (sense of reality / valóságérzéküket)", "valóságérzéküket", "Scientists must not lose their sober sense of reality during research.", ["c1-06-vocab"]),
            fb("grammar", "recall", "A két kultúra közötti párbeszéd tartós _____ vert a népek között. (bridge / hidat)", "hidat", "Dialogue between the two cultures built an enduring bridge between the peoples.", ["c1-conceptual-blending"]),
            fb("grammar", "context", "A túlzott szigort alkalmazó rendszer végül veszélyes _____ futott. (ran aground / zátonyra)", "zátonyra", "The system applying excessive severity eventually ran aground dangerously.", ["c1-conceptual-blending"]),
            fb("grammar", "context", "Pilinszky szikár stílusa minden felesleges sallangot _____ a lényegről. (stripped away / lehántott)", "lehántott", "Pilinszky's austere style stripped away all superfluous frills from the essence.", ["c1-deadjectival-abstraction"]),
            mc("grammar", "context", "Hogyan kapcsolódik a szikár próza a mély jelentéssűrítéshez?", [
                "A díszek elhagyásával a megmaradó szavak rendkívüli gondolati és érzelmi súlyt kapnak.",
                "A mondatok rövidsége miatt gyorsabban lehet olvasni.",
                "Nem kapcsolódnak sehogy sem."
            ], 0, ["c1-conceptual-blending"]),
            sb("grammar", "produce", ["A", "tiszta", "erkölcsi", "tartás", "a", "társadalom", "legfőbb", "szellemi", "sarokköve."], ["A", "tiszta", "erkölcsi", "tartás", "a", "társadalom", "legfőbb", "szellemi", "sarokköve."], "Pure moral backbone is the chief intellectual cornerstone of society.", ["c1-deadjectival-abstraction"]),
            sw("production", [{"prompt": "Write a sentence using 'kétélű fegyver' and 'felelősségtudat'.", "answer": "A tudományos hatalom kétélű fegyver, amely mélységes felelősségtudatot követel."}], ["c1-idiomatic-compounding"]),
            sw("production", [{"prompt": "Formulate a thought on the power of silence in Pilinszky's spirit.", "answer": "A legnagyobb igazságok előtt a szó elnémul, és a csend válik a tisztaság egyetlen mércéjévé."}], ["c1-deadjectival-abstraction"])
        ]
    )

    # ----------------------------------------------------
    # TRACK 2: DISCOURSE (c1-metaforak)
    # ----------------------------------------------------
    slug = "metaforak"
    disc_title = "The Metaphorical Landscape of Hungarian"
    disc_intro = [
        "A language is not merely a vehicle for communication; it is a landscape of the mind. Hungarian idioms, spatial cases, body metaphors, and historical concepts encode an entire cosmology of human existence.",
        "In this unit, you will explore the rich metaphorical architecture of Hungarian: how the three-way directional case system shapes abstract thinking, how the human body models the world, how the Great Plain (puszta) and nature inform semantics, and how historical destiny is cast in metaphor."
    ]

    disc_lessons = [
        {
            "num": 1,
            "stem": f"c1-{slug}-01",
            "title": "Spatiality and the Tripartite Case System in Abstract Thought",
            "grammar_title": "Spatial Grounding and Abstract Tripartite Case Metaphors",
            "grammar_skill": "c1-embodied-spatial-metaphor",
            "goals": [
                "I can analyze how Hungarian's three-way directional cases (*honnan? hol? hová?*) structure abstract thought.",
                "I can evaluate spatial containment metaphors in mental and emotional domains.",
                "I can navigate complex spatial metaphors in academic and philosophical Hungarian."
            ],
            "vocab": [
                {"lemma": "hármas esetrendszer", "translation": "tripartite case system (from/in/to)", "pos": "noun"},
                {"lemma": "térszemlélet", "translation": "spatial perception / conception", "pos": "noun"},
                {"lemma": "tartálymetafora", "translation": "container metaphor", "pos": "noun"},
                {"lemma": "felszíni viszony", "translation": "surface relation (on/onto/from surface)", "pos": "noun"},
                {"lemma": "közelítés", "translation": "approach, approximation", "pos": "noun"},
                {"lemma": "távolodás", "translation": "moving away, distancing", "pos": "noun"},
                {"lemma": "átvitt értelem", "translation": "figurative / transferred meaning", "pos": "noun"},
                {"lemma": "fogalmi tagozódás", "translation": "conceptual articulation / structuring", "pos": "noun"}
            ],
            "gr_text1": "Hungarian grammar is deeply grounded in space. The three-way distinction (*honnan? hol? hová?*) applied across internal (*-ból, -ban, -ba*), surface (*-ról, -on, -ra*), and adessive (*-tól, -nál, -hoz*) domains serves as the universal template for abstract thought.",
            "gr_text2": "When we despair, we fall into a dark container (*kétségbe esünk*); when we trust someone, we admit them inside ourselves (*bízunk benne*); when working on a project, we bear the load on a surface (*dolgozunk rajta*).",
            "gr_table": [
                ["Kétségbe esik vs. észhez tér...", "Falls into despair vs. returns to his senses..."],
                ["Gondolkodik valamin (felszíni téri viszony)...", "Thinks upon something (surface spatial relation)..."],
                ["Kibontakozik a válságból...", "Unfolds / emerges out of the crisis..."]
            ],
            "world_story_seg": {
                "seg_slug": "ter",
                "title": "A tér törvényei a magyar gondolkodásban",
                "summary": "How the Hungarian three-way directional case system creates an exquisite, precise spatial coordinate grid for all abstract and emotional concepts.",
                "paragraphs": [
                    {"type": "narration", "text": "Amikor egy külföldi tanulni kezdi a magyar nyelvet, gyakran megretten a ragok gazdagságától: -ban, -ba, -ból, -on, -ra, -ról, -nál, -hoz, -tól. Ám amint megérti e rendszer belső logikáját, egy elképesztő építészeti csoda tárul fel előtte. A magyar nyelvtan ugyanis nem szabályok mechanikus halmaza, hanem a fizikai tér tökéletes leképezése a szellem világában."},
                    {"type": "narration", "text": "A hármas tagozódás – honnan, hol és hová – láthatatlan iránytűként vezeti a gondolkodást. Amikor szomorúak vagyunk, nem egyszerűen rossz kedvünk van: 'kétségbe esünk', vagyis egy mély, zárt tartály fenekére zuhanunk. Amikor megnyugszunk, 'észhez térünk', vagyis visszatalálunk a gondolat otthonos helyére. Ha egy problémán töprengünk, egy láthatatlan felszínen hordozzuk a terhet: 'dolgozunk rajta'."},
                    {"type": "narration", "text": "Ez a páratlan téri logika azt eredményezi, hogy a magyarul beszélő ember elméje ösztönösen három dimenzióban látja a legelvontabb filozófiai és erkölcsi viszonyokat is. A nyelv nem elszakad a valóságtól: a test és a tér konkrét tapasztalatát emeli a magasba."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Hogyan strukturálja a hármas esetrendszer az absztrakt gondolkodást a magyarban?", [
                    "A honnan-hol-hová fizikai téri irányultságát viszi át az érzelmi és elvont állapotok kifejezésére.",
                    "Megszünteti a határozószók szükségességét.",
                    "Csak a térképészetben van jelentősége."
                ], 0, ["c1-metaforak-vocab"]),
                fb("grammar", "practice", "Amikor valaki megnyugszik a trauma után, képletesen szólva visszatér az ész téri helyére, azaz észhez _____. (returns to his senses / tér)", "tér", "When someone calms down after trauma, figuratively speaking they return to the spatial place of the mind, that is, they return to their senses.", ["c1-embodied-spatial-metaphor"]),
                match("vocabulary", "controlled", [["hármas esetrendszer", "tripartite case system"], ["térszemlélet", "spatial perception"], ["tartálymetafora", "container metaphor"], ["átvitt értelem", "figurative meaning"]], ["c1-metaforak-vocab"]),
                sb("grammar", "practice", ["A", "magyar", "nyelv", "téri", "logikája", "áthatja", "az", "elvont", "gondolkodást."], ["A", "magyar", "nyelv", "téri", "logikája", "áthatja", "az", "elvont", "gondolkodást."], "The spatial logic of the Hungarian language permeates abstract thought.", ["c1-embodied-spatial-metaphor"]),
                dc("dialogue", [
                    {"speaker": "Nyelvész", "text": "Miért mondjuk, hogy 'bízom benned' és nem azt, hogy 'bízom hozzád'?"},
                    {"speaker": "Kutató", "text": "Mert a bizalom tartálymetafora: a lelkünk belső terébe fogadjuk be a másikat."},
                ], ["belső terébe fogadjuk be", "nagyon messze vagyunk tőle", "semmi jelentősége nincs"], 0, ["c1-embodied-spatial-metaphor"]),
                sw("production", [{"prompt": "Write an explanation of the metaphor 'kétségbe esik'.", "answer": "A 'kétségbe esik' kifejezésben a kétség egy veszélyes mély tartályként jelenik meg, amelybe az ember belezuhan."}], ["c1-embodied-spatial-metaphor"]),
                mc("grammar", "check", "Melyik állítás bizonyítja a téri ragok átvitt értelmű pontosságát?", [
                    "A lelki folyamatokat finoman differenciált belső és felszíni téri viszonyokként éljük meg.",
                    "Minden ragot véletlenszerűen választunk ki a mondatban.",
                    "A magyarban nincsenek helyhatározó ragok."
                ], 0, ["c1-embodied-spatial-metaphor"])
            ]
        },
        {
            "num": 2,
            "stem": f"c1-{slug}-02",
            "title": "The Body as World Model: Head, Heart, Hand, and Foot",
            "grammar_title": "Embodied Cognition and Somatic Idioms in Hungarian",
            "grammar_skill": "c1-embodied-spatial-metaphor",
            "goals": [
                "I can analyze somatic idioms (*fej, szív, kéz, láb, szem*) in Hungarian world modeling.",
                "I can evaluate embodied cognition (*testesülés*) in expressions of emotion and intellect.",
                "I can deploy high-register somatic idiomatic expressions with nuance."
            ],
            "vocab": [
                {"lemma": "testesülés", "translation": "embodiment, embodied cognition", "pos": "noun"},
                {"lemma": "szomatikus metafora", "translation": "somatic / bodily metaphor", "pos": "noun"},
                {"lemma": "fejét töri", "translation": "to rack one's brain (lit. break one's head)", "pos": "expression"},
                {"lemma": "szívére vesz", "translation": "to take to heart", "pos": "expression"},
                {"lemma": "kézbe vesz", "translation": "to take in hand, take control of", "pos": "expression"},
                {"lemma": "lábra kap", "translation": "to gain ground, take root (lit. catch foot)", "pos": "expression"},
                {"lemma": "szem előtt tart", "translation": "to keep in mind, bear in mind (lit. hold before eyes)", "pos": "expression"},
                {"lemma": "érzéki megalapozottság", "translation": "sensory groundedness", "pos": "noun"}
            ],
            "gr_text1": "Cognitive linguistics demonstrates that human concepts originate in bodily experience (*testesülés*). Hungarian features hundreds of idioms based on anatomy: the head represents intellect (*fejét töri, fejébe vesz*), the heart represents emotion and conscience (*szívére vesz, szívvel-lélekkel*), and the hand represents agency (*kézbe vesz, kezet emel*).",
            "gr_text2": "When writing advanced analytical essays, somatic metaphors ground abstract assertions in vivid physical intuition without losing register dignity.",
            "gr_table": [
                ["A vezetőség kézbe vette az irányítást.", "The management took control into hand."],
                ["A hamis pletyka gyorsan lábra kapott.", "The false rumor quickly gained ground."],
                ["Mindig szem előtt tartva a közösség javát...", "Always keeping in mind the common good..."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mit fejez ki a 'lábra kap' kifejezés az elvont folyamatok leírásában?", ["Azt, hogy egy eszme vagy hír megerősödik és gyorsan elterjed a köztudatban.", "Hogy valaki új cipőt vásárolt.", "Hogy valaki gyorsan fut."], 0, ["c1-metaforak-vocab"]),
                fb("grammar", "practice", "A döntéshozatal során mindvégig szem előtt kell _____ a hosszú távú következményeket. (to keep / tartani)", "tartani", "During decision-making, one must keep long-term consequences in mind throughout.", ["c1-embodied-spatial-metaphor"]),
                match("vocabulary", "controlled", [["testesülés", "embodied cognition"], ["fejét töri", "to rack one's brain"], ["szívére vesz", "to take to heart"], ["kézbe vesz", "to take in hand / control"]], ["c1-metaforak-vocab"]),
                sb("grammar", "practice", ["A", "kormány", "határozottan", "kézbe", "vette", "a", "válság", "kezelését."], ["A", "kormány", "határozottan", "kézbe", "vette", "a", "válság", "kezelését."], "The government decisively took management of the crisis into hand.", ["c1-embodied-spatial-metaphor"]),
                dc("dialogue", [
                    {"speaker": "Kolléga", "text": "Hogyan sikerült megoldani ezt a rendkívül bonyolult feladványt?"},
                    {"speaker": "Kutató", "text": "Napokon át törtük a fejünket, míg végül rábukkantunk a megoldásra."},
                ], ["törtük a fejünket", "aludtunk az asztalon", "nem csináltunk semmit"], 0, ["c1-embodied-spatial-metaphor"]),
                sw("production", [{"prompt": "Write a sentence using 'szem előtt tartva' in an institutional or moral context.", "answer": "Minden döntésünket az emberi méltóság feltétlen tiszteletét szem előtt tartva kell meghoznunk."}], ["c1-embodied-spatial-metaphor"]),
                mc("grammar", "check", "Melyik állítás világítja meg a szomatikus metaforák szerepét a nyelvben?", [
                    "A testi tapasztalatokból merített képek teszik átélhetővé és plasztikussá az elvont gondolatokat.",
                    "A testi szervek neveit tilos átvitt értelemben használni.",
                    "A testnek semmi köze a nyelvhez."
                ], 0, ["c1-embodied-spatial-metaphor"])
            ]
        },
        {
            "num": 3,
            "stem": f"c1-{slug}-03",
            "title": "Landscape and Nature: Light, Shadow, Earth, and Water",
            "grammar_title": "Environmental Semiotics, Puszta Landscape, and Natural Metaphors",
            "grammar_skill": "c1-cultural-semiotics",
            "goals": [
                "I can analyze how the Hungarian landscape (*a puszta, a rög, a Duna*) informs cultural semiotics.",
                "I can evaluate metaphors of light, shadow, thirst, and drought in moral and political literature.",
                "I can use evocative nature-based idioms in high-register literary analysis."
            ],
            "vocab": [
                {"lemma": "kulturális szemiotika", "translation": "cultural semiotics", "pos": "noun"},
                {"lemma": "rög", "translation": "clod of earth, native sod", "pos": "noun"},
                {"lemma": "puszta", "translation": "great plain, wasteland, barren horizon", "pos": "noun"},
                {"lemma": "virágzás", "translation": "flowering, blooming, flourishing", "pos": "noun"},
                {"lemma": "elsivatagosodás", "translation": "desertification (environmental & cultural)", "pos": "noun"},
                {"lemma": "forrásvidék", "translation": "headwaters, source region", "pos": "noun"},
                {"lemma": "gyökérzet", "translation": "root system, ancestral roots", "pos": "noun"},
                {"lemma": "éltető erő", "translation": "life-giving force, vital energy", "pos": "noun"}
            ],
            "gr_text1": "Hungarian culture draws fundamental symbols from its landscape. *A rög* (the native sod / clod of earth) represents physical attachment to homeland, while *a puszta* symbolizes both infinite freedom and existential loneliness.",
            "gr_text2": "Agricultural and hydrological metaphors (*elsivatagosodás, forrásvidék, gyökérzet*) migrate into cultural diagnosis: an era lacking creativity is described as *szellemi aszály* (intellectual drought).",
            "gr_table": [
                ["A nemzeti kultúra mély gyökérzete...", "The deep root system of national culture..."],
                ["Szellemi elsivatagosodás és aszály...", "Intellectual desertification and drought..."],
                ["Visszatérni a tiszta forrásvidékhez...", "To return to the pure source region..."]
            ],
            "world_story_seg": {
                "seg_slug": "termeszet",
                "title": "A táj és a lélek: A rög és a tiszta forrás",
                "summary": "How the Hungarian landscape, the earth, and the rivers shaped the metaphorical vocabulary of national poetry and philosophy.",
                "paragraphs": [
                    {"type": "narration", "text": "A magyar irodalom kezdetei óta elválaszthatatlan a tájtól, amelyben megszületett. A végtelen Alföld síkja, a Tisza kanyarulatai, a Bakony tölgyesei és a Balaton ezüstös tükre nem egyszerű díszletek voltak a költők számára, hanem a lélek legmélyebb belső állapotainak tükrei."},
                    {"type": "narration", "text": "Amikor Petőfi a puszta végtelen szabadságáról énekelt, vagy Ady a 'magyar Ugar' terméketlen, parlagon heverő rögét siratta, a föld valóságos metafizikai szimbólummá nemesült. A 'rög' a szülőföldhöz kötődés nehéz hűségét jelenti, a 'szomjúság' a szellemi megújulás utáni vágyat, míg Bartók Béla 'tiszta forrása' a romlatlan népi kultúra és az egyetemes emberség gyökerét idézi fel."},
                    {"type": "narration", "text": "Ez a tájszemantika ma is eleven a magyar nyelvben. Amikor a kultúra válságáról beszélünk, ösztönösen az 'elsivatagosodás' képét idézzük fel; és amikor a megújulásról álmodunk, a 'tavasz' és a 'virágzás' örök természeti metaforáiba kapaszkodunk."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Mit szimbolizál a 'tiszta forrás' fogalma Bartók Béla és a magyar kultúra szótárában?", [
                    "A romlatlan, ősi gyökerekből táplálkozó tiszta szellemi és művészi értéket.",
                    "A hegyi ásványvizek palackozását.",
                    "Egy tiszta patak földrajzi fekvését."
                ], 0, ["c1-metaforak-vocab"]),
                fb("grammar", "practice", "A művészetnek vissza kell térnie az eredeti szellemi _____ ahhoz, hogy megújuljon. (headwaters / forrásvidékhez)", "forrásvidékhez", "Art must return to the original intellectual headwaters in order to be renewed.", ["c1-cultural-semiotics"]),
                match("vocabulary", "controlled", [["kulturális szemiotika", "cultural semiotics"], ["rög", "native sod / clod of earth"], ["puszta", "great plain"], ["elsivatagosodás", "desertification"]], ["c1-metaforak-vocab"]),
                sb("grammar", "practice", ["A", "kultúra", "mély", "gyökerei", "a", "szülőföld", "hagyományaiban", "élnek."], ["A", "kultúra", "mély", "gyökerei", "a", "szülőföld", "hagyományaiban", "élnek."], "The deep roots of culture live in the traditions of the homeland.", ["c1-cultural-semiotics"]),
                dc("dialogue", [
                    {"speaker": "Kultúrakutató", "text": "Hogyan jellemezné a jelenlegi kulturális válságot?"},
                    {"speaker": "Író", "text": "Valódi szellemi elsivatagosodást látunk, amelyből csak az alkotó munka hozhat kiutat."},
                ], ["szellemi elsivatagosodást", "a legnagyobb gazdagságot", "semmi különöset"], 0, ["c1-cultural-semiotics"]),
                sw("production", [{"prompt": "Write a sentence using the metaphor of 'forrás' or 'gyökérzet'.", "answer": "Az anyanyelv gazdagsága az a kimeríthetetlen forrás, amelyből a nemzet szellemi élete táplálkozik."}], ["c1-cultural-semiotics"]),
                mc("grammar", "check", "Melyik metafora kapcsolódik a szülőföld iránti ragaszkodáshoz?", [
                    "A röghöz kötöttség és a szülőföld rögének szeretete.",
                    "A szélkakas forgása.",
                    "A vándormadarak repülése."
                ], 0, ["c1-cultural-semiotics"])
            ]
        },
        {
            "num": 4,
            "stem": f"c1-{slug}-04",
            "title": "History and Destiny: The Border Fortress and Ill Fate",
            "grammar_title": "Historical Myth-Making, Border Fortress Mentality, and Tragic Destiny",
            "grammar_skill": "c1-cultural-semiotics",
            "goals": [
                "I can analyze central historical metaphors (*végvár, balsors, védőbástya, megmaradás*).",
                "I can evaluate how historical memory and national trauma are metaphorically encoded.",
                "I can debate the psychological impact of the 'border fortress' mentality in modern Hungary."
            ],
            "vocab": [
                {"lemma": "végvár", "translation": "border fortress", "pos": "noun"},
                {"lemma": "védőbástya", "translation": "bastion of defense, bulwark", "pos": "noun"},
                {"lemma": "balsors", "translation": "ill fate, adversity, tragic destiny", "pos": "noun"},
                {"lemma": "megmaradás", "translation": "survival, preservation, enduring", "pos": "noun"},
                {"lemma": "sorscsapás", "translation": "blow of fate, calamity", "pos": "noun"},
                {"lemma": "végvári mentalitás", "translation": "border fortress mentality (defensive stance)", "pos": "noun"},
                {"lemma": "áldozathozatal", "translation": "sacrifice, sacrificial commitment", "pos": "noun"},
                {"lemma": "történelmi hivatás", "translation": "historical mission", "pos": "noun"}
            ],
            "gr_text1": "Hungarian historical consciousness is defined by defensive and sacrificial metaphors. The *végvár* (border fortress) and *védőbástya* (bulwark of Western Christendom against the Ottoman Empire) position Hungary as an outpost sacrificing itself for Europe.",
            "gr_text2": "*Balsors* (ill fate, immortalized in the National Anthem) and *megmaradás* (tenacious survival against demographic and political extinction) form the existential twin-pillars of Hungarian historiography.",
            "gr_table": [
                ["A kereszténység védőbástyája...", "The bulwark of Christianity..."],
                ["A megmaradásért vívott évszázados küzdelem...", "The centuries-old struggle for survival..."],
                ["Balsors akit régen tép...", "Ill fate who torn it for long... (Hymn quotation)"]
            ],
            "world_story_seg": {
                "seg_slug": "tortenelem",
                "title": "A végvár és a balsors: A történelem metaforái",
                "summary": "How centuries of defensive warfare, survival against empires, and Kölcsey's Hymn forged Hungary's distinct historical mythology.",
                "paragraphs": [
                    {"type": "narration", "text": "Kevés nép történelmi öntudatát határozták meg oly mélyen a védekező metaforák, mint a magyarét. A tatárjárástól a török hódoltságon át a két világháborúig a magyar sors szinte megszakítás nélküli küzdelem volt a megmaradásért egy veszélyes birodalmi ütközőzónában."},
                    {"type": "narration", "text": "A 'végvár' és a 'védőbástya' képe nem egyszerű hadtörténeti tény volt: nemzeti hivatástudattá vált. A magyarok úgy érezték, saját testükkel és vérükkel védelmezik a nyugati keresztény civilizációt a keleti hódítókkal szemben – még akkor is, ha Európa gyakran hálátlannak bizonyult e véráldozatért. Kölcsey Ferenc Himnuszában ez a tragikus érzés a 'balsors' fenséges költői képévé nemesült."},
                    {"type": "narration", "text": "Ez a 'végvári mentalitás' kettős örökséget hagyott hátra. Egyfelől páratlan szívósságot és életerőt adott a nemzetnek a túléléshez; másfelől a gyanakvás és a magányosság érzését táplálta egy olyan világban, ahol az összefogás és a nyitottság a valódi jövő záloga."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Mit jelent a 'végvári mentalitás' a magyar társadalomtörténetben?", [
                    "Azt a történelmi reflexet, amely a nemzetet a külső fenyegetésekkel szemben álló magányos védőbástyaként éli meg.",
                    "A középkori várak turisztikai látogatását.",
                    "A katonai egyenruhák viselését hétköznap."
                ], 0, ["c1-metaforak-vocab"]),
                fb("grammar", "practice", "A nemzet évszázadokon át a szellemi és fizikai _____ vívta történelmi harcát. (survival / megmaradásért)", "megmaradásért", "For centuries, the nation fought its historic battle for intellectual and physical survival.", ["c1-cultural-semiotics"]),
                match("vocabulary", "controlled", [["végvár", "border fortress"], ["védőbástya", "bulwark"], ["balsors", "ill fate"], ["megmaradás", "survival / preservation"]], ["c1-metaforak-vocab"]),
                sb("grammar", "practice", ["A", "magyar", "történelem", "a", "megmaradásért", "folytatott", "szüntelen", "küzdelem", "volt."], ["A", "magyar", "történelem", "a", "megmaradásért", "folytatott", "szüntelen", "küzdelem", "volt."], "Hungarian history was a ceaseless struggle for survival.", ["c1-cultural-semiotics"]),
                dc("dialogue", [
                    {"speaker": "Történész", "text": "Hogyan hat a végvár metaforája a mai gondolkodásra?"},
                    {"speaker": "Szociológus", "text": "Egyszerre ad erőt a nehézségekben, de elszigeteltség-érzetet is szülhet."},
                ], ["elszigeteltség-érzetet is szülhet", "azonnal megold minden problémát", "semmi jelentősége nincs"], 0, ["c1-cultural-semiotics"]),
                sw("production", [{"prompt": "Write a critical evaluation of the 'védőbástya' historical concept.", "answer": "A védőbástya metaforája az önfeláldozó történelmi felelősségvállalás és az európai hivatástudat jelképe."}], ["c1-cultural-semiotics"]),
                mc("grammar", "check", "Melyik költemény rögzítette legmélyebben a 'balsors' metaforáját a nemzeti emlékezetben?", [
                    "Kölcsey Ferenc Himnusza.",
                    "Arany János Toldija.",
                    "Petőfi Sándor Nemzeti dala."
                ], 0, ["c1-cultural-semiotics"])
            ]
        },
        {
            "num": 5,
            "stem": f"c1-{slug}-05",
            "title": "Future Horizons: Global Metaphors on Hungarian Soil",
            "grammar_title": "Metaphoric Evolution, Linguistic Innovation, and the Global Horizon",
            "grammar_skill": "c1-embodied-spatial-metaphor",
            "goals": [
                "I can analyze how international and technological metaphors adapt into Hungarian syntax.",
                "I can evaluate linguistic globalization vs. indigenous metaphoric renewal.",
                "I can debate the future vitality of Hungarian metaphorical thinking."
            ],
            "vocab": [
                {"lemma": "nyelvi megújulás", "translation": "linguistic renewal / revitalization", "pos": "noun"},
                {"lemma": "metaforikus kiterjesztés", "translation": "metaphoric extension", "pos": "noun"},
                {"lemma": "digitális tér", "translation": "digital space", "pos": "noun"},
                {"lemma": "nyelvújítás", "translation": "Language Reform (historical & modern)", "pos": "noun"},
                {"lemma": "termékeny kölcsönhatás", "translation": "fruitful interaction", "pos": "noun"},
                {"lemma": "szemantikai gazdagság", "translation": "semantic richness", "pos": "noun"},
                {"lemma": "élő szervezet", "translation": "living organism", "pos": "noun"},
                {"lemma": "jövőkép", "translation": "vision of the future", "pos": "noun"}
            ],
            "gr_text1": "Hungarian has survived through centuries by assimilating foreign concepts and reclothing them in native metaphorical garb. Just as the 19th-century *nyelvújítás* created thousands of enduring words, today the digital world undergoes natural metaphoric extension (*metaforikus kiterjesztés*).",
            "gr_text2": "The internet is not a foreign territory; it is conceived through native directional cases (*a neten, a hálóra, a felhőbe*), proving that Hungarian remains a dynamic, living organism (*élő szervezet*).",
            "gr_table": [
                ["A nyelv mint állandóan megújuló élő szervezet...", "Language as a constantly renewing living organism..."],
                ["Globális fogalmak szerves beépülése a magyar nyelvbe...", "Organic assimilation of global concepts into Hungarian..."],
                ["A metaforikus gondolkodás jövője a digitális korban...", "The future of metaphorical thought in the digital era..."]
            ],
            "world_story_seg": {
                "seg_slug": "jovo",
                "title": "A metafora jövője: Új horizontok a digitális korban",
                "summary": "How Hungarian conceptual metaphors continue to evolve, assimilating artificial intelligence and global networks into a rich national worldview.",
                "paragraphs": [
                    {"type": "narration", "text": "A magyar nyelv életereje mindig abban a csodálatos képességében rejlett, hogy nem bezárkózott a múltba, hanem magába szívta a világ újdonságait, és saját képére formálta azokat. Amikor a reformkorban Kazinczy és társai tízezer új szót alkottak, a magyar nyelv megtanulta a modern tudomány és polgári élet fogalmait. Ma, a huszonegyedik században ugyanez a feladat áll előttünk."},
                    {"type": "narration", "text": "A digitális tér, a felhőtechnológia, a virtuális valóság és a mesterséges intelligencia új metaforák milliárdjait hozza létre. És a magyar nyelvtan ma is játszi könnyedséggel öltözteti ezeket saját téri és igekötős ruhájába: 'felmegyünk a netre', 'letöltünk a felhőből', 'becsatlakozunk a hálózatba'. A nyelv nem megkopik, hanem új virágokat hoz."},
                    {"type": "narration", "text": "A metafora ugyanis a szellem szabadságának örök bizonyítéka. Amíg képesek vagyunk a világot költészetté, a gondolatot képpé, és a tapasztalatot anyanyelvi bölcsességgé formálni, addig a magyar nyelv nemcsak fennmarad, hanem a jövő embere számára is az otthon és a teremtő erő legszebb világa marad."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Hogyan alkalmazkodik a magyar nyelv a globális digitális korszakhoz?", [
                    "Saját téri logikájával és metaforikus kiterjesztéseivel szervesen asszimilálja az új fogalmakat.",
                    "Elhagyja a magyar szavakat és csak angolul beszél.",
                    "Megtiltja az internet használatát."
                ], 0, ["c1-metaforak-vocab"]),
                fb("grammar", "practice", "A magyar nyelv nem merev leltár, hanem szüntelenül fejlődő élő _____. (organism / szervezet)", "szervezet", "The Hungarian language is not a rigid inventory, but a ceaselessly developing living organism.", ["c1-embodied-spatial-metaphor"]),
                match("vocabulary", "controlled", [["nyelvi megújulás", "linguistic renewal"], ["digitális tér", "digital space"], ["szemantikai gazdagság", "semantic richness"], ["élő szervezet", "living organism"]], ["c1-metaforak-vocab"]),
                sb("grammar", "practice", ["A", "magyar", "nyelv", "kimeríthetetlen", "teremtő", "erővel", "bír."], ["A", "magyar", "nyelv", "kimeríthetetlen", "teremtő", "erővel", "bír."], "The Hungarian language possesses inexhaustible creative power.", ["c1-embodied-spatial-metaphor"]),
                dc("dialogue", [
                    {"speaker": "Nyelvész", "text": "Fenyegeti-e a globális digitalizáció a magyar nyelvet?"},
                    {"speaker": "Kutató", "text": "Csak akkor, ha feladjuk a saját metaforáinkat; amíg alkotóan használjuk, gazdagodik a nyelv."},
                ], ["alkotóan használjuk", "betiltjuk az iskolákban", "nem törődünk vele"], 0, ["c1-embodied-spatial-metaphor"]),
                sw("production", [{"prompt": "Write a visionary thought about the creative power of the Hungarian language.", "answer": "A magyar nyelv gazdag metaforavilága a szellem szabadságának és a jövőbe vetett hitnek az örök záloga."}], ["c1-embodied-spatial-metaphor"]),
                mc("grammar", "check", "Mi biztosítja a magyar nyelv metaforikus vitalitását a jövőben?", [
                    "A hagyományok tisztelete és a nyitott, kreatív megújulási képesség szerves egysége.",
                    "A szótárak elégetése.",
                    "A külföldi szavak betiltása büntetéssel."
                ], 0, ["c1-embodied-spatial-metaphor"])
            ]
        }
    ]

    for l in disc_lessons:
        emit_instructional_lesson(6, "discourse", l, disc_title, disc_intro if l["num"] == 1 else None)

    # Full World Compilation Story
    write_json(
        f"stories/world/c1/{slug}.json",
        {
            "id": f"story.c1.world.{slug}",
            "title": "A gondolat metaforái: Tér, test és lélek a magyar nyelvben",
            "level": "C1",
            "type": "world",
            "summary": "Epic synthesis of the Hungarian metaphorical universe: spatial directional cases, somatic body metaphors, the semiotics of the puszta landscape, border fortress history, and future digital horizons.",
            "paragraphs": [
                {"type": "narration", "text": "A magyar nyelv egy teljes, eleven kozmológia. Nem egyszerűen szavak gyűjteménye a tárgyak megnevezésére, hanem a szellem, a test és a természet lenyűgöző koordinátarendszere, amelyben minden emberi tapasztalat téri és metaforikus rendbe illeszkedik."},
                {"type": "narration", "text": "A hármas esetrendszer – a honnan, hol és hová tiszta logikája – belső tartályokként és nyitott felszínekként modellezi a lélek legmélyebb rezdüléseit: a kétségbeeséstől az észhez térésig. Az emberi test – a fej, a szív és a kéz – eleven világmodellként ad nevet a döntésnek, a felelősségnek és az érzelmeknek."},
                {"type": "narration", "text": "A táj szemantikája a magyar föld mély barázdáiból táplálkozik: a puszta végtelen szabadsága, a rög nehéz hűsége és a tiszta forrás romlatlan vize mind etikai mérceként ragyog a nemzeti költészetben."},
                {"type": "narration", "text": "A történelem a végvár és a balsors fenséges drámájával vértezte fel a nyelvet, megtanítva a magyarságot a megmaradás páratlan szívósságára és a szabadság feltétlen tiszteletére."},
                {"type": "narration", "text": "Ez a gazdag metaforikus tájkép a digitális korban sem enyészik el. A nyelv élő szervezetként fogadja be az új technológiák kihívásait, bizonyítva, hogy a gondolat szabadsága és az anyanyelv teremtő géniusza örök, elpusztíthatatlan kincsünk marad."}
            ]
        }
    )

    # Discourse Consolidation
    emit_consolidation_lesson(
        6,
        "discourse",
        f"c1-{slug}-consolidation",
        disc_title,
        [
            "I can analyze spatial, somatic, environmental, and historical metaphors in Hungarian.",
            "I can evaluate how conceptual metaphors embody cultural worldview and identity.",
            "I can discuss linguistic evolution and metaphorical assimilation in the digital era."
        ],
        [
            mc("grammar", "recognize", "Hogyan működik a hármas esetrendszer a magyar elvont gondolkodásban?", [
                "A fizikai tér irányultságait vetíti át a lelki és fogalmi viszonyok pontos strukturálására.",
                "Kizárólag a térképészeti szaknyelvben érvényesül.",
                "Csak a múlt időben használható."
            ], 0, ["c1-embodied-spatial-metaphor"]),
            mc("grammar", "recognize", "Mit fejez ki a 'végvár' és a 'védőbástya' metaforája?", [
                "A nemzet történelmi felelősségét és a civilizáció védelmében hozott önfeláldozását.",
                "A gazdasági elszigeteltség dicséretét.",
                "Egy kirándulóhely leírását."
            ], 0, ["c1-cultural-semiotics"]),
            match("vocabulary", "recognize", [["hármas esetrendszer", "tripartite case system"], ["testesülés", "embodied cognition"], ["rög", "native sod"], ["végvár", "border fortress"], ["nyelvi megújulás", "linguistic renewal"]], ["c1-metaforak-vocab"]),
            fb("vocabulary", "recall", "A bátor fellépés során a vezetés határozottan _____ vette az ügy intézését. (into hand / kézbe)", "kézbe", "During the courageous action, the leadership decisively took management of the matter into hand.", ["c1-metaforak-vocab"]),
            fb("vocabulary", "recall", "A nemzet évszázadokon át a fizikai és lelki _____ vívta történelmi harcát. (survival / megmaradásért)", "megmaradásért", "For centuries, the nation fought its historic battle for physical and spiritual survival.", ["c1-metaforak-vocab"]),
            fb("grammar", "recall", "A válság mélyén a polgárok nem estek kétségbe, hanem megtartották erkölcsi _____. (backbone / tartásukat)", "tartásukat", "In the depth of the crisis, citizens did not fall into despair, but preserved their moral backbone.", ["c1-embodied-spatial-metaphor"]),
            fb("grammar", "context", "A döntéshozatal során mindvégig szem előtt kell _____ a jövő nemzedékek érdekeit. (to keep / tartani)", "tartani", "During decision-making, one must keep the interests of future generations in mind throughout.", ["c1-embodied-spatial-metaphor"]),
            fb("grammar", "context", "A nyelv mint állandóan megújuló élő _____ képes befogadni az új kor kihívásait. (organism / szervezet)", "szervezet", "Language as a constantly renewing living organism is capable of assimilating the challenges of the new era.", ["c1-embodied-spatial-metaphor"]),
            mc("grammar", "context", "Mi a magyar nyelv legfőbb metafizikai ereje a kulturális szemiotika szerint?", [
                "Az a képessége, hogy a konkrét testi és téri tapasztalatot a legmagasabb szellemi igazságok hordozójává emeli.",
                "Hogy a szavak mind egyformán hosszúak.",
                "Hogy nincsenek benne magánhangzók."
            ], 0, ["c1-cultural-semiotics"]),
            sb("grammar", "produce", ["A", "magyar", "nyelv", "a", "szellem", "és", "a", "lélek", "élő", "otthona."], ["A", "magyar", "nyelv", "a", "szellem", "és", "a", "lélek", "élő", "otthona."], "The Hungarian language is the living home of mind and soul.", ["c1-cultural-semiotics"]),
            sw("production", [{"prompt": "Write a concluding synthesis sentence on the metaphorical landscape of Hungarian.", "answer": "A magyar nyelv metaforavilága bizonyítja, hogy az anyanyelv a valóság legmélyebb és legszebb megismerési formája."}], ["c1-cultural-semiotics"]),
            sw("production", [{"prompt": "Formulate a thought on the future of Hungarian thought.", "answer": "Amíg a magyar szellem alkotóan őrzi anyanyelvének metaforikus gazdagságát, addig jövője megingathatatlan."}], ["c1-cultural-semiotics"])
        ]
    )
    print("=== Finished C1 Unit 6 ===")


if __name__ == "__main__":
    generate_unit_6()
