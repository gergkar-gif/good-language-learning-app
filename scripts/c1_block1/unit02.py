#!/usr/bin/env python3
"""
Hungarian C1 Block 1 - Unit 02 Generator:
  - Track 1 (Core): Unit 2 — "Syntactic Compression & Dense Participial Modification" (c1-02)
  - Track 2 (Discourse): Unit 2 — "The Golden Age of the Hungarian Essay" (c1-esszemuveszet)
"""

from .common import mc, match, fb, sb, dc, sw, write_json, emit_instructional_lesson, emit_consolidation_lesson


def generate_unit_2():
    print("=== Generating C1 Unit 2 ===")
    
    # ----------------------------------------------------
    # TRACK 1: CORE (c1-02)
    # ----------------------------------------------------
    core_title = "Syntactic Compression & Dense Participial Modification"
    core_intro = [
        "In academic and literary Hungarian, communicative density is achieved not by piling up short main clauses, but by condensing entire subordinate clauses into pre-nominal participial structures.",
        "In this unit, inspired by Dezső Kosztolányi's profound essay collection 'Nyelv és lélek', you will master left-branching participial clauses with multiple oblique arguments, adverbial participles (-va/-ve, -ván/-vén), and the art of elegant syntactic compression."
    ]

    core_lessons = [
        {
            "num": 1,
            "stem": "c1-02-01",
            "title": "Left-Branching Participial Modification",
            "grammar_title": "Dense Pre-nominal Participial Clauses",
            "grammar_skill": "c1-dense-participles",
            "goals": [
                "I can construct pre-nominal participial clauses carrying multiple oblique arguments.",
                "I can compress relative clauses into elegant left-branching adjectival participles (-ó/-ő, -ott/-ett/-ött).",
                "I can analyze high-register prose syntax in scholarly Hungarian texts."
            ],
            "vocab": [
                {"lemma": "balra ágazó", "translation": "left-branching", "pos": "adjective"},
                {"lemma": "melléknévi igenév", "translation": "participle", "pos": "noun"},
                {"lemma": "tömörítés", "translation": "compression, condensation", "pos": "noun"},
                {"lemma": "hátravetett", "translation": "postposed", "pos": "adjective"},
                {"lemma": "szerkezeti", "translation": "structural", "pos": "adjective"},
                {"lemma": "tagoltság", "translation": "articulation, structural segmentation", "pos": "noun"},
                {"lemma": "egyértelműsít", "translation": "to disambiguate", "pos": "verb"},
                {"lemma": "szórendi", "translation": "word-order related", "pos": "adjective"}
            ],
            "gr_text1": "Hungarian syntax allows extensive left-branching pre-nominal modification. Instead of a relative clause ('a törvénytervezet, amelyet a parlament a múlt héten fogadott el'), formal Hungarian compresses this into a participle preceding the noun: 'a parlament által a múlt héten elfogadott törvénytervezet'.",
            "gr_text2": "When stacking oblique modifiers before a participle, the chronological or topical elements precede the agent ('által') or instrument ('-val/-vel'), which immediately precedes the participle head.",
            "gr_table": [
                ["a nemrég napvilágot látott tanulmány", "the study that recently came to light"],
                ["a szakértők által régóta vitatott elmélet", "the theory long contested by experts"],
                ["a gazdasági válság következtében előállt helyzet", "the situation that arose in consequence of the crisis"]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mit nevezünk balra ágazó szerkezetnek a magyar mondattanban?", ["A főnévi alaptag elé helyezett, bővítményekkel teli igeneves szerkezetet.", "A mondat végére vetett mellékmondatot.", "A zárójelbe tett megjegyzéseket."], 0, ["c1-02-vocab"]),
                fb("grammar", "controlled", "A bizottság _____ régóta vizsgált kérdés végre napirendre került. (by the committee / által)", "által", "The question investigated for a long time by the committee finally made the agenda.", ["c1-dense-participles"]),
                match("vocabulary", "controlled", [["tömörítés", "compression"], ["tagoltság", "structural segmentation"], ["egyértelműsít", "to disambiguate"], ["melléknévi igenév", "participle"]], ["c1-02-vocab"]),
                fb("grammar", "practice", "A konferencián bemutatták a kutatók _____ kidolgozott új módszertant. (developed by the researchers)", "által", "At the conference they presented the new methodology developed by the researchers.", ["c1-dense-participles"]),
                sb("grammar", "practice", ["A", "szakértők", "által", "régóta", "vitatott", "tétel", "bebizonyosodott."], ["A", "szakértők", "által", "régóta", "vitatott", "tétel", "bebizonyosodott."], "The thesis long contested by experts has been proven.", ["c1-dense-participles"]),
                dc("dialogue", [
                    {"speaker": "Szerkesztő", "text": "Nem túl nehézkes ez a vonatkozó mellékmondat?"},
                    {"speaker": "Szerző", "text": "Valóban, érdemes balra ágazó igeneves szerkezettel tömöríteni a kifejezést."},
                ], ["tömöríteni a kifejezést", "elhagyni a témát", "megtoldani egy kötőszóval"], 0, ["c1-dense-participles"]),
                sw("production", [{"prompt": "Compress the clause 'a javaslat, amelyet a minisztérium tegnap terjesztett elő' into a left-branching participial phrase.", "answer": "a minisztérium által tegnap előterjesztett javaslat"}], ["c1-dense-participles"]),
                mc("grammar", "check", "Melyik mondat alkalmazza a legautentikusabb C1 szintű igeneves tömörítést?", [
                    "A kormány által nemrég elfogadott intézkedéscsomag azonnal életbe lép.",
                    "Az intézkedéscsomag, amit a kormány tegnap elfogadott, életbe lép.",
                    "A kormány intézkedése elfogadott és életbe lép."
                ], 0, ["c1-dense-participles"])
            ]
        },
        {
            "num": 2,
            "stem": "c1-02-02",
            "title": "Adverbial Participial Structures: -va/-ve and -ván/-vén",
            "grammar_title": "Literary Adverbial Participles in Complex Framing",
            "grammar_skill": "c1-complex-adverbials",
            "goals": [
                "I can employ adverbial participles (-va/-ve) for secondary state predication.",
                "I can recognize and interpret archaic and literary forms in -ván/-vén.",
                "I can ensure precise subject agreement in participial background clauses."
            ],
            "vocab": [
                {"lemma": "határozói igenév", "translation": "adverbial participle", "pos": "noun"},
                {"lemma": "tekintetbe véve", "translation": "taking into consideration", "pos": "expression"},
                {"lemma": "felismerve", "translation": "recognizing, realizing", "pos": "adverb"},
                {"lemma": "kiindulva", "translation": "proceeding from, starting from", "pos": "adverb"},
                {"lemma": "összegezve", "translation": "summing up, in summary", "pos": "adverb"},
                {"lemma": "eltekintve", "translation": "disregarding, setting aside", "pos": "adverb"},
                {"lemma": "lévén", "translation": "being (archaic/formal)", "pos": "conjunction"},
                {"lemma": "tudván", "translation": "knowing (that) (literary)", "pos": "adverb"}
            ],
            "gr_text1": "Adverbial participles ending in *-va / -ve* function as circumstantial modifiers, establishing background state, simultaneity, or manner. In formal C1 prose, absolute constructions like *tekintetbe véve a körülményeket* (taking circumstances into consideration) allow concise qualification.",
            "gr_text2": "The archaic *-ván / -vén* suffix survives in refined essayistic prose to express anteriority or causal background: *Tudván a veszélyt, mégis útra kelt.* (Knowing the danger, he set out nonetheless). *Lévén* functions as an elevated causal connector synonymous with *mivel van*.",
            "gr_table": [
                ["A helyzet súlyát felismerve cselekedtek.", "Recognizing the gravity of the situation, they acted."],
                ["Mindezektől eltekintve a terv életképes.", "Disregarding all these things, the plan is viable."],
                ["Nagy tekintélyű tudós lévén, mindenki hallgatott rá.", "Being a scholar of great authority, everyone listened to him."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Milyen jelentésárnyalatot fejez ki a 'lévén' alak?", ["Okhatározói hátteret teremt ('mivel az, lévén...').", "Célhatározót fejez ki.", "Kizárólag tagadást jelent."], 0, ["c1-02-vocab"]),
                fb("grammar", "controlled", "A körülményeket tekintetbe _____, az eredmény kiemelkedőnek minősíthető. (taking into consideration)", "véve", "Taking the circumstances into consideration, the result can be qualified as outstanding.", ["c1-complex-adverbials"]),
                match("vocabulary", "controlled", [["tekintetbe véve", "taking into consideration"], ["felismerve", "recognizing"], ["eltekintve", "disregarding"], ["lévén", "being (causal)"]], ["c1-02-vocab"]),
                fb("grammar", "practice", "A tényekből kiindul_____ megállapíthatjuk, hogy az elmélet helytálló. (proceeding / starting from)", "va", "Proceeding from the facts, we can establish that the theory is correct.", ["c1-complex-adverbials"]),
                sb("grammar", "practice", ["A", "veszélyt", "felismerve", "azonnal", "módosították", "a", "stratégiát."], ["A", "veszélyt", "felismerve", "azonnal", "módosították", "a", "stratégiát."], "Recognizing the danger, they immediately modified the strategy.", ["c1-complex-adverbials"]),
                dc("dialogue", [
                    {"speaker": "Kritikus", "text": "Hogyan értékelhető a döntés a gazdasági válság tükrében?"},
                    {"speaker": "Elemző", "text": "A nehézségekből kiindulva a vezetés a legóvatosabb utat választotta."},
                ], ["kiindulva", "távolodva", "lemaradva"], 0, ["c1-complex-adverbials"]),
                sw("production", [{"prompt": "Write an elevated sentence using 'tekintetbe véve'.", "answer": "A történelmi kontextust tekintetbe véve a szerző álláspontja teljesen érthető."}], ["c1-complex-adverbials"]),
                mc("grammar", "check", "Melyik mondatban szerepel helyesen az emelkedett 'lévén' szerkezet?", [
                    "Kiváló szakember lévén, azonnal átlátta a probléma gyökerét.",
                    "Lévén megérkezett a vonat, felszálltunk.",
                    "A ház lévén szép, megvettük tegnap."
                ], 0, ["c1-complex-adverbials"])
            ]
        },
        {
            "num": 3,
            "stem": "c1-02-03",
            "title": "Nominal Compression & Abstract Deverbal Nouns",
            "grammar_title": "Abstract Nominalizations and Syntactic Condensation",
            "grammar_skill": "c1-nominal-compression",
            "goals": [
                "I can replace verbal predicates with abstract deverbal nouns (-ás/-és, -ság/-ség).",
                "I can form dense relational chains using genitive and postpositional dependencies.",
                "I can calibrate the register between verbal dynamics and nominal elegance."
            ],
            "vocab": [
                {"lemma": "főnevesítés", "translation": "nominalization", "pos": "noun"},
                {"lemma": "függvényében", "translation": "as a function of, depending on", "pos": "postposition"},
                {"lemma": "tekintetében", "translation": "with regard to, in respect of", "pos": "postposition"},
                {"lemma": "érdekében", "translation": "in the interest of, for the sake of", "pos": "postposition"},
                {"lemma": "tükrében", "translation": "in the mirror of, in light of", "pos": "postposition"},
                {"lemma": "tisztázás", "translation": "clarification", "pos": "noun"},
                {"lemma": "érvényesülés", "translation": "prevailing, taking effect", "pos": "noun"},
                {"lemma": "megvalósulás", "translation": "realization, materialization", "pos": "noun"}
            ],
            "gr_text1": "Academic Hungarian heavily utilizes deverbal nominalization (*tisztáz, tisztázás; érvényesül, érvényesülés*). Rather than writing 'amikor tisztázzuk a kérdést', formal prose uses 'a kérdés tisztázása során' or 'a kérdés tisztázásának függvényében'.",
            "gr_text2": "Abstract postpositional compounds (*tekintetében, függvényében, tükrében, érdekében*) connect multiple nominal heads into rigorous logical dependencies.",
            "gr_table": [
                ["a kérdés elvi tisztázása", "the theoretical clarification of the issue"],
                ["az eredmények függvényében", "depending on / as a function of the results"],
                ["az új adatok fényében és tükrében", "in light and reflection of the new data"]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mit fejez ki a 'függvényében' névutós szerkezet?", ["Feltételes függőséget egy adott tényezőtől ('annak függvényében').", "Fizikai távolságot.", "Időbeli késlekedést."], 0, ["c1-02-vocab"]),
                fb("grammar", "controlled", "A reformok végrehajtása a költségvetési keretek _____ történik. (depending on / as a function of)", "függvényében", "The implementation of the reforms takes place depending on the budgetary frameworks.", ["c1-nominal-compression"]),
                match("vocabulary", "controlled", [["függvényében", "as a function of"], ["tekintetében", "in respect of"], ["tükrében", "in light of"], ["tisztázás", "clarification"]], ["c1-02-vocab"]),
                fb("grammar", "practice", "A helyzet alapos _____ után hozták meg a végső döntést. (clarification / tisztázás + -a)", "tisztázása", "Following the thorough clarification of the situation, they made the final decision.", ["c1-nominal-compression"]),
                sb("grammar", "practice", ["A", "jogszabályok", "érvényesülése", "minden", "állampolgár", "közös", "érdeke."], ["A", "jogszabályok", "érvényesülése", "minden", "állampolgár", "közös", "érdeke."], "The enforcement of laws is the common interest of every citizen.", ["c1-nominal-compression"]),
                dc("dialogue", [
                    {"speaker": "Jogász", "text": "Hogyan fogalmazzuk meg ezt a passzust a szerződésben?"},
                    {"speaker": "Partner", "text": "A kötelezettségek teljesítésének tekintetében mindkét fél egyetért."},
                ], ["tekintetében", "helyett", "ellenére"], 0, ["c1-nominal-compression"]),
                sw("production", [{"prompt": "Rephrase 'amikor megvalósul a terv' using nominalization and 'tükrében' or 'függvényében'.", "answer": "A terv megvalósulásának függvényében értékeljük az eredményeket."}], ["c1-nominal-compression"]),
                mc("grammar", "check", "Melyik szerkezet képvisel professzionális akadémiai stílust?", [
                    "A premisszák elméleti tisztázásának tükrében a következtetés helytálló.",
                    "Mert tisztáztuk a dolgokat, azért jó a vége.",
                    "A tisztázás jó dolog a vége felé."
                ], 0, ["c1-nominal-compression"])
            ]
        },
        {
            "num": 4,
            "stem": "c1-02-04",
            "title": "Dense Appositive and Restrictive Modification",
            "grammar_title": "Complex Restrictive and Appositive Adjectival Stacking",
            "grammar_skill": "c1-dense-participles",
            "goals": [
                "I can stack complex restrictive and descriptive adjectival phrases before noun heads.",
                "I can integrate participial and prepositional attributes smoothly.",
                "I can maintain grammatical agreement and rhythmic cadence in long noun phrases."
            ],
            "vocab": [
                {"lemma": "értelmező jelző", "translation": "appositive modifier", "pos": "noun"},
                {"lemma": "halmozott", "translation": "accumulated, stacked", "pos": "adjective"},
                {"lemma": "példa nélküli", "translation": "unprecedented", "pos": "expression"},
                {"lemma": "mélyreható", "translation": "profound, deep-reaching", "pos": "adjective"},
                {"lemma": "kikezdhetetlen", "translation": "unassailable, flawless", "pos": "adjective"},
                {"lemma": "összetett", "translation": "complex, composite", "pos": "adjective"},
                {"lemma": "meghatározó", "translation": "defining, decisive", "pos": "adjective"},
                {"lemma": "sokrétű", "translation": "multifaceted", "pos": "adjective"}
            ],
            "gr_text1": "In C1 descriptive discourse, multiple adjectives and participles frequently modify a single noun. When stacked pre-nominally, descriptive qualities follow objective categorizations: *egy mind ez idáig példa nélküli, mélyreható és visszafordíthatatlan átalakulás*.",
            "gr_text2": "Appositive modifiers (*értelmező jelző*) placed after the noun head must agree in case and number with the noun (*a szerződésről, erről a mindkét fél számára előnyös megállapodásról*).",
            "gr_table": [
                ["egy mindeddig páratlannak tartott felfedezés", "a discovery considered peerless until now"],
                ["a sokrétű, mélyreható elemzés", "the multifaceted, profound analysis"],
                ["a vitáról, mint meghatározó szellemi eseményről", "about the debate, as a defining intellectual event"]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Milyen jelentést hordoz a 'mélyreható' jelző?", ["Alapos, gyökeres és átfogó jellegűt.", "Felszíneset és sietőset.", "Kizárólag negatívat."], 0, ["c1-02-vocab"]),
                fb("grammar", "controlled", "A reformok következtében egy mindeddig példa _____ átalakulás ment végbe. (unprecedented / nélküli)", "nélküli", "As a consequence of the reforms, an unprecedented transformation took place.", ["c1-dense-participles"]),
                match("vocabulary", "controlled", [["mélyreható", "profound"], ["kikezdhetetlen", "unassailable"], ["sokrétű", "multifaceted"], ["halmozott", "stacked"]], ["c1-02-vocab"]),
                fb("grammar", "practice", "A kutatás során egy rendkívül _____, több szempontot egyesítő modellt alkottak. (multifaceted / sokrétű)", "sokrétű", "During the research, they created an exceptionally multifaceted model combining multiple aspects.", ["c1-dense-participles"]),
                sb("grammar", "practice", ["A", "bizottság", "egy", "minden", "szempontból", "kikezdhetetlen", "jelentést", "fogadott", "el."], ["A", "bizottság", "egy", "minden", "szempontból", "kikezdhetetlen", "jelentést", "fogadott", "el."], "The committee adopted a report that is unassailable from all points of view.", ["c1-dense-participles"]),
                dc("dialogue", [
                    {"speaker": "Tudós", "text": "Hogyan jellemezné a felfedezés jelentőségét?"},
                    {"speaker": "Recenzens", "text": "Ez egy mind ez idáig példa nélküli, korszakalkotó eredmény."},
                ], ["korszakalkotó eredmény", "jelentéktelen részlet", "hibás adat"], 0, ["c1-dense-participles"]),
                sw("production", [{"prompt": "Write a sentence stacking three modifiers before the noun 'kutatás'.", "answer": "Egy mélyreható, sokrétű és nemzetközileg elismert kutatás eredményeit publikálták."}], ["c1-dense-participles"]),
                mc("grammar", "check", "Melyik mondatban egyezik helyesen az értelmező jelző a főnévvel?", [
                    "Beszéltünk az új elméletről, erről a sokak által vitatott tézisről.",
                    "Beszéltünk az új elméletről, ez a sokak által vitatott tézis.",
                    "Beszéltünk az új elméletről, erről a sokak által vitatott tézist."
                ], 0, ["c1-dense-participles"])
            ]
        },
        {
            "num": 5,
            "stem": "c1-02-05",
            "title": "Syntactic Contraction in Master Prose: Kosztolányi",
            "grammar_title": "Stylistic Elegance and Cadence in Hungarian Prose",
            "grammar_skill": "c1-nominal-compression",
            "goals": [
                "I can analyze Dezső Kosztolányi's syntactic mastery in 'Nyelv és lélek'.",
                "I can discern the balance between verbal flow and nominal precision.",
                "I can read and interpret complex Hungarian literary non-fiction."
            ],
            "vocab": [
                {"lemma": "mondatritmus", "translation": "sentence rhythm, prose cadence", "pos": "noun"},
                {"lemma": "lélekbúvár", "translation": "psychologist, explorer of the soul", "pos": "noun"},
                {"lemma": "stílusművészet", "translation": "stylistic mastery, artistry of style", "pos": "noun"},
                {"lemma": "lebegtetés", "translation": "suspension, deliberate ambiguity", "pos": "noun"},
                {"lemma": "árnyalás", "translation": "shading, subtle nuancing", "pos": "noun"},
                {"lemma": "hajlékonyság", "translation": "suppleness, agility", "pos": "noun"},
                {"lemma": "hangulatfestő", "translation": "mood-painting, evocative", "pos": "adjective"},
                {"lemma": "életszerűség", "translation": "vividness, lifelikeness", "pos": "noun"}
            ],
            "gr_text1": "Dezső Kosztolányi's essays demonstrate how the Hungarian sentence can achieve maximum intellectual agility (*hajlékonyság*). He avoided heavy bureaucratic nominal stacking, favoring organic rhythmic cadence (*mondatritmus*) where compressed participial modifiers build musical suspense.",
            "gr_text2": "In masterly C1 prose, syntactic contraction is deployed deliberately: condensed participial structures slow down the pace to invite contemplation, followed by brisk verbal clauses that drive the argument home.",
            "gr_table": [
                ["A szavak lebegtetése...", "The delicate suspension of words..."],
                ["A magyar mondat páratlan hajlékonysága...", "The peerless agility of the Hungarian sentence..."],
                ["Az árnyalás finom művészete...", "The fine art of nuanced shading..."]
            ],
            "classic_story": {
                "slug": "c1-02-kosztolanyi",
                "author": "Kosztolányi Dezső",
                "work": "Nyelv és lélek (1930)",
                "title": "A magyar mondat élete és ritmusa",
                "summary": "Kosztolányi Dezső reflections on the living anatomy of Hungarian prose, exploring how the sentence breathes through its natural word order and musical cadence.",
                "characters": ["Kosztolányi Dezső"],
                "paragraphs": [
                    {"type": "narration", "text": "A magyar mondat nem merev sínpár, amelyen a gondolat előre kiszámított állomások felé robog, hanem élő szervezet: lélegzik, pulzál, hajlik és feszül a mondanivaló belső súlya alatt. Amikor Kosztolányi Dezső a Nyelv és lélek esszéiben a magyar próza természetét vizsgálta, nem száraz grammatikai törvényeket keresett, hanem a nyelv vérkeringését tapintotta ki."},
                    {"type": "narration", "text": "A nyelv nem holt matéria, amelyet kívülről kényszerítünk logikai kalodába. Az igazi stílusművész ott ismeri fel anyanyelve géniuszát, ahol az a látszólagos könnyedség mögött a legszigorúbb fegyelmet követeli meg. A balra ágazó, sűrített szerkezetek nem arra valók, hogy elnehezítsék a mondatot, hanem arra, hogy mint íjfeszítés a nyilat, felhalmozzák az értelmi és érzelmi energiát a főmondat végső felpattanásáig."},
                    {"type": "narration", "text": "Ez a ritmikai lebegtetés teszi a magyar esszét oly különlegessé az európai irodalomban. Kosztolányi rámutatott: a magyar nyelvben a szórend nem merev előírás, hanem a figyelem szüntelen finomhangolása. Amit előre helyezünk, az a gondolat fényudvarába lép; amit hátrább vonunk, az finom árnyékká válik."},
                    {"type": "narration", "text": "Aki megtanulja ezt a ritmust, az nem csupán helyesen beszél, hanem megismeri a gondolkodás legmagasabb rendű szabadságát. A mondatritmus ugyanis maga a lélek rezdülése: a bizonyíték arra, hogy a nyelvben a forma és a tartalom elválaszthatatlan egységbe forr össze."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Mit jelent a 'hajlékonyság' a stilisztikában?", ["A nyelv rugalmas, könnyed alkalmazkodóképességét.", "A szótárak lapjainak vékonyságát.", "A beszélt nyelv bizonytalanságát."], 0, ["c1-02-vocab"]),
                fb("grammar", "practice", "Kosztolányi szerint a magyar mondat legfőbb erénye a páratlan ritmikai _____. (suppleness / hajlékonyság)", "hajlékonysága", "According to Kosztolányi, the chief virtue of the Hungarian sentence is its peerless rhythmic suppleness.", ["c1-nominal-compression"]),
                match("vocabulary", "controlled", [["mondatritmus", "sentence rhythm"], ["hajlékonyság", "suppleness"], ["lebegtetés", "suspension"], ["árnyalás", "nuanced shading"]], ["c1-02-vocab"]),
                mc("reading", "practice", "Hogyan jellemzi Kosztolányi a magyar mondatot a szövegben?", [
                    "Nem merev sínpár, hanem lélegző, élő szervezet.",
                    "Matematikai képletek pontos gyűjteménye.",
                    "Idegen minták utánzása."
                ], 0, None),
                mc("reading", "practice", "Milyen szerepet töltenek be a balra ágazó sűrített szerkezetek a szerző szerint?", [
                    "Felhalmozzák az értelmi és érzelmi energiát a végső felpattanásig.",
                    "Elnehezítik és érthetetlenné teszik a prózát.",
                    "Fölösleges díszként szolgálnak."
                ], 0, None),
                sb("grammar", "practice", ["A", "magyar", "mondat", "szórendje", "a", "figyelem", "szüntelen", "finomhangolása."], ["A", "magyar", "mondat", "szórendje", "a", "figyelem", "szüntelen", "finomhangolása."], "The word order of the Hungarian sentence is the constant fine-tuning of attention.", ["c1-nominal-compression"]),
                sw("production", [{"prompt": "Summarize Kosztolányi's view of sentence rhythm in one sentence.", "answer": "A mondatritmus nem csupán formai elem, hanem a gondolkodás eleven lélegzetvétele."}], ["c1-nominal-compression"]),
                mc("grammar", "check", "Melyik stílusesszencia ragadja meg a kosztolányiánus próza lényegét?", [
                    "A zeneiség, a formai fegyelem és a belső szabadság tökéletes harmóniája.",
                    "A hivatalos bürokratikus fogalmazás szigorú követése.",
                    "A rövid, tagolatlan tőmondatok kizárólagos alkalmazása."
                ], 0, ["c1-nominal-compression"])
            ]
        }
    ]

    for l in core_lessons:
        emit_instructional_lesson(2, "core", l, core_title, core_intro if l["num"] == 1 else None)

    # Core Consolidation
    emit_consolidation_lesson(
        2,
        "core",
        "c1-02-consolidation",
        core_title,
        [
            "I can synthesize dense left-branching participial clauses with high accuracy.",
            "I can select between verbal predicates and elegant nominal compression.",
            "I can reproduce masterly Hungarian sentence cadences inspired by Kosztolányi."
        ],
        [
            mc("grammar", "recognize", "Melyik szerkezet képvisel balra ágazó igeneves tömörítést?", [
                "A szakértők által tegnap nyilvánosságra hozott jelentés.",
                "A jelentés, amit a szakértők hoztak tegnap.",
                "A jelentés megjelent, mert a szakértők hozták."
            ], 0, ["c1-dense-participles"]),
            mc("grammar", "recognize", "Milyen funkciót lát el a 'tekintetbe véve' kifejezés?", [
                "Körülményhatározói hátteret és mérlegelést fejez ki.",
                "Időbeli tiltást fejez ki.",
                "Feltételes tagadást jelent."
            ], 0, ["c1-complex-adverbials"]),
            match("vocabulary", "recognize", [["balra ágazó", "left-branching"], ["tömörítés", "compression"], ["függvényében", "as a function of"], ["mélyreható", "profound"], ["hajlékonyság", "suppleness"]], ["c1-02-vocab"]),
            fb("vocabulary", "recall", "A reformok végrehajtása a költségvetés _____ történik. (as a function of / függvényében)", "függvényében", "The execution of reforms takes place as a function of the budget.", ["c1-02-vocab"]),
            fb("vocabulary", "recall", "A bizottság elnöke egy mind ez idáig példa _____ sikerről számolt be. (unprecedented / nélküli)", "nélküli", "The committee president reported an unprecedented success.", ["c1-02-vocab"]),
            fb("grammar", "recall", "A szerzők a helyzet súlyát felismer_____ változtatták meg a koncepciót. (recognizing / -ve)", "ve", "Recognizing the gravity of the situation, the authors changed the concept.", ["c1-complex-adverbials"]),
            fb("grammar", "context", "A parlament _____ nemrég elfogadott törvény azonnal életbe lép. (by the parliament / által)", "által", "The law recently passed by the parliament takes effect immediately.", ["c1-dense-participles"]),
            fb("grammar", "context", "A kérdés alapos tisztázásának _____ értékelték az eredményeket. (in light of / tükrében)", "tükrében", "In light of the thorough clarification of the issue, they evaluated the results.", ["c1-nominal-compression"]),
            mc("grammar", "context", "Mi a fő stilisztikai előnye a balra ágazó melléknévi igenévnek?", [
                "Kerüli a nehézkes vonatkozó mellékmondatok halmozását, és tömöríti a gondolatot.",
                "Mindig vicces hangulatot kölcsönöz a mondatnak.",
                "Lerövidíti a szavak betűszámát."
            ], 0, ["c1-dense-participles"]),
            sb("grammar", "produce", ["A", "magyar", "mondat", "ritmusa", "a", "gondolat", "belső", "szabadságát", "tükrözi."], ["A", "magyar", "mondat", "ritmusa", "a", "gondolat", "belső", "szabadságát", "tükrözi."], "The rhythm of the Hungarian sentence reflects the internal freedom of thought.", ["c1-nominal-compression"]),
            sw("production", [{"prompt": "Write a compressed sentence about an economic decision using 'által elfogadott'.", "answer": "A kormány által elfogadott gazdasági intézkedések stabilizálták a piacot."}], ["c1-dense-participles"]),
            sw("production", [{"prompt": "Write an elevated statement with 'tekintetbe véve'.", "answer": "A történelmi előzményeket tekintetbe véve a megegyezés történelmi jelentőségű."}], ["c1-complex-adverbials"])
        ]
    )

    # ----------------------------------------------------
    # TRACK 2: DISCOURSE (c1-esszemuveszet)
    # ----------------------------------------------------
    slug = "esszemuveszet"
    disc_title = "The Golden Age of the Hungarian Essay"
    disc_intro = [
        "The Hungarian essay is not simply an academic commentary; it is a battleground of ideas, spiritual self-examination, and sublime prose style.",
        "From Péter Pázmány's thundering baroque rhetoric to the polished intellectual portraits of Antal Szerb and László Németh's impassioned cultural diagnoses, in this unit you will explore the rich heritage of the Hungarian essayistic tradition."
    ]

    disc_lessons = [
        {
            "num": 1,
            "stem": f"c1-{slug}-01",
            "title": "Baroque Rhetoric: Péter Pázmány and Hungarian Prose",
            "grammar_title": "Baroque Rhetorical Architecture and Emphatic Tropes",
            "grammar_skill": "c1-essayistic-register",
            "goals": [
                "I can analyze Péter Pázmány's foundational role in creating literary Hungarian prose.",
                "I can identify baroque periodic cadence and rhetorical antithesis.",
                "I can employ elevated, historically resonant vocabulary."
            ],
            "vocab": [
                {"lemma": "retorika", "translation": "rhetoric", "pos": "noun"},
                {"lemma": "szónoklat", "translation": "oration, speech", "pos": "noun"},
                {"lemma": "kifejezőerő", "translation": "expressive power", "pos": "noun"},
                {"lemma": "érvelő próza", "translation": "argumentative prose", "pos": "noun"},
                {"lemma": "pátosz", "translation": "pathos, elevated passion", "pos": "noun"},
                {"lemma": "képszerűség", "translation": "vividness of imagery", "pos": "noun"},
                {"lemma": "áradó", "translation": "overflowing, torrent-like", "pos": "adjective"},
                {"lemma": "alapkő", "translation": "cornerstone, foundation stone", "pos": "noun"}
            ],
            "gr_text1": "Péter Pázmány established the Hungarian literary sentence in the 17th century. His style is characterized by majestic periodic periods (*körmondat*), rich sensory metaphors drawn from everyday peasant life, and thundering antitheses.",
            "gr_text2": "In modern C1 prose, echoing baroque cadence means balancing passionate rhetorical conviction (*pátosz*) with rigorous logical clarity (*logikai fegyelem*).",
            "gr_table": [
                ["A magyar próza alapkieve...", "The foundation stone of Hungarian prose..."],
                ["Áradó szónoki pátosz és éles logika...", "Torrent-like oratorical pathos and razor-sharp logic..."],
                ["Képszerű hasonlatok sokasága...", "A multitude of vivid similes..."]
            ],
            "world_story_seg": {
                "seg_slug": "pazmany",
                "title": "Pázmány Péter és a magyar mondat hajnala",
                "summary": "How Archbishop Péter Pázmány transformed Hungarian into a flexible, powerful medium for intellectual combat and theology.",
                "paragraphs": [
                    {"type": "narration", "text": "A tizenhetedik század elején a magyar nyelv még nem volt a magas teológia és a filozófiai viták elfogadott közege. A tudomány Európa-szerte latinul szólt. Ekkor lépett a küzdőtérre Pázmány Péter esztergomi érsek, aki felismerte: a lelkekért vívott küzdelmet csak azon a nyelven lehet megnyerni, amelyen az emberek álmodnak és éreznek."},
                    {"type": "narration", "text": "Pázmány nem félt a népnyelv zamatos, vaskos fordulatait beemelni a barokk körmondatok méltóságteljes boltívei alá. Hasonlatai az alföldi parasztok és a végvári vitézek világából vett képekkel ragyogtak, miközben érvelése a tomista teológia legszigorúbb logikáját követte. Nála a magyar mondat egyszerre lett áradó folyam és acélos kard."},
                    {"type": "narration", "text": "Az ő tollán született meg a modern magyar érvelő próza. Bebizonyította, hogy a magyar nyelv nemcsak lírai dalokra vagy katonai parancsokra alkalmas, hanem a legelvontabb metafizikai igazságok és a legélesebb szellemi viták kifejezésére is."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Miért tekintik Pázmány Pétert a magyar próza megalapozójának?", [
                    "Mert a barokk retorikát ötvözte a népnyelv eleven kifejezőerejével, megteremtve az érvelő prózát.",
                    "Mert ő írta az első magyar verseskötetet.",
                    "Mert betiltotta a latin nyelvű misézést."
                ], 0, ["c1-esszemuveszet-vocab"]),
                fb("grammar", "practice", "Pázmány szónoklatai az áradó barokk pátosz és a szigorú logikai fegyelem remekbe szabott _____ alkotják. (synthesis / szintézisét)", "szintézisét", "Pázmány's speeches constitute a masterfully crafted synthesis of overflowing baroque pathos and strict logical discipline.", ["c1-essayistic-register"]),
                match("vocabulary", "controlled", [["retorika", "rhetoric"], ["szónoklat", "oration"], ["érvelő próza", "argumentative prose"], ["pátosz", "pathos"]], ["c1-esszemuveszet-vocab"]),
                sb("grammar", "practice", ["Pázmány", "megteremtette", "a", "magyar", "érvelő", "próza", "klasszikus", "alapjait."], ["Pázmány", "megteremtette", "a", "magyar", "érvelő", "próza", "klasszikus", "alapjait."], "Pázmány established the classical foundations of Hungarian argumentative prose.", ["c1-essayistic-register"]),
                dc("dialogue", [
                    {"speaker": "Irodalomtörténész", "text": "Hogyan hat Pázmány stílusa a mai esszéírásra?"},
                    {"speaker": "Professzor", "text": "A képszerűség és a szigorú érveléstechnika ötvözése ma is a legmagasabb mérce."},
                ], ["legmagasabb mérce", "elavult szabály", "felesleges dísz"], 0, ["c1-essayistic-register"]),
                sw("production", [{"prompt": "Write a sentence evaluating Pázmány's prose style.", "answer": "Pázmány szónoki művészete a magyar nyelv kifejezőerejének örök érvényű bizonyítéka."}], ["c1-essayistic-register"]),
                mc("grammar", "check", "Melyik jellemző NEM igaz Pázmány Péter prózájára?", [
                    "Száraz, képektől mentes, kizárólag latin terminusokat használó fogalmazásmód.",
                    "Gazdag és érzékletes képszerűség.",
                    "Hatalmas ívű, harmonikus körmondatok."
                ], 0, ["c1-essayistic-register"])
            ]
        },
        {
            "num": 2,
            "stem": f"c1-{slug}-02",
            "title": "The Nyugat Essayists: Babits and Kosztolányi",
            "grammar_title": "Literary Critical Essay Registers and Stylistic Balance",
            "grammar_skill": "c1-essayistic-register",
            "goals": [
                "I can analyze the essayistic models established by the Nyugat generation.",
                "I can distinguish between Babits' philosophical depth and Kosztolányi's aesthetic sparkle.",
                "I can compose nuanced literary critical evaluations in Hungarian."
            ],
            "vocab": [
                {"lemma": "esszéista", "translation": "essayist", "pos": "noun"},
                {"lemma": "szellemtörténet", "translation": "intellectual history, history of ideas", "pos": "noun"},
                {"lemma": "esztétikai", "translation": "aesthetic", "pos": "adjective"},
                {"lemma": "bírálat", "translation": "critique, review", "pos": "noun"},
                {"lemma": "mércéje", "translation": "yardstick of, criterion of", "pos": "noun"},
                {"lemma": "lényeglátás", "translation": "insight, perception of the essence", "pos": "noun"},
                {"lemma": "pallérozott", "translation": "polished, cultivated", "pos": "adjective"},
                {"lemma": "szellemi horizont", "translation": "intellectual horizon", "pos": "noun"}
            ],
            "gr_text1": "The writers of the *Nyugat* journal transformed the essay from an academic treatise into a work of art. Babits brought European intellectual breadth (*szellemtörténeti távlat*), while Kosztolányi introduced sparkling conversational lightness and psychological acuity.",
            "gr_text2": "Essays of this tradition make frequent use of evaluative noun phrases (*mércéje, lényeglátása, szellemi horizontja*) combined with cultivated adjectives (*pallérozott, szabatos*).",
            "gr_table": [
                ["A Nyugat esszéistáinak szellemi horizontja...", "The intellectual horizon of the Nyugat essayists..."],
                ["Pallérozott stílus és páratlan lényeglátás...", "Cultivated style and peerless insight..."],
                ["Az esztétikai autonómia védelmében...", "In defense of aesthetic autonomy..."]
            ],
            "world_story_seg": {
                "seg_slug": "nyugat",
                "title": "A Nyugat esszéművészete: Babits és Kosztolányi",
                "summary": "How the Nyugat generation created an intellectual golden age where literature became the laboratory of modern Hungarian thought.",
                "paragraphs": [
                    {"type": "narration", "text": "A huszadik század első évtizedeiben a Nyugat című folyóirat körül tömörülő írók forradalmasították a magyar szellemi életet. Számukra az esszé nem tudományos szakcikk volt, és nem is publicisztikai fecsegés, hanem a legmagasabb rendű intellektuális vallomás: a gondolkodó ember párbeszéde az európai kultúrával."},
                    {"type": "narration", "text": "Babits Mihály a világirodalom roppant katedrálisát építette be esszéibe. nála minden kritikai bírálat morális állásfoglalássá nemesült, amely az örök értékek védelmére kelt. Kosztolányi Dezső ezzel szemben a pillanat varázsát, a szavak rejtett zenéjét és az emberi lélek finom rebbenéseit kereste. Kettejük stílusa a magyar esszé két pólusát jelölte ki: a fenséges erkölcsi méltóságot és a csillogó esztétikai könnyedséget."},
                    {"type": "narration", "text": "Ez a kettősség emelte a magyar esszét világirodalmi színvonalra. Megmutatták, hogy a magyar nyelv képes a legfinomabb európai szellemi áramlatok befogadására úgy, hogy közben megőrzi sajátos, utánozhatatlan nemzeti karakterét."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Mi jellemezte a Nyugat folyóirat esszéit?", [
                    "A művészi igényesség, az európai távlat és a személyes intellektuális hangvétel ötvözése.",
                    "A kizárólag pártpolitikai propaganda terjesztése.",
                    "A népi költészet kizárólagos utánzása."
                ], 0, ["c1-esszemuveszet-vocab"]),
                fb("grammar", "practice", "Babits esszéit a rendkívül mély szellemtörténeti _____ és morális felelősség jellemzi. (insight / lényeglátás)", "lényeglátás", "Babits' essays are characterized by exceptionally deep intellectual-historical insight and moral responsibility.", ["c1-essayistic-register"]),
                match("vocabulary", "controlled", [["esszéista", "essayist"], ["szellemtörténet", "history of ideas"], ["pallérozott", "cultivated"], ["szellemi horizont", "intellectual horizon"]], ["c1-esszemuveszet-vocab"]),
                sb("grammar", "practice", ["A", "Nyugat", "esszéistái", "európai", "horizontot", "nyitottak", "a", "magyar", "gondolkodásnak."], ["A", "Nyugat", "esszéistái", "európai", "horizontot", "nyitottak", "a", "magyar", "gondolkodásnak."], "The essayists of Nyugat opened a European horizon for Hungarian thought.", ["c1-essayistic-register"]),
                dc("dialogue", [
                    {"speaker": "Egyetemi hallgató", "text": "Miben különbözik Babits és Kosztolányi esszéírói alkata?"},
                    {"speaker": "Irodalmár", "text": "Babits a szigorú morális mércét képviseli, míg Kosztolányi a csillogó esztétikai szabadságot."},
                ], ["morális mércét", "napi politikát", "katonai erényt"], 0, ["c1-essayistic-register"]),
                sw("production", [{"prompt": "Write a critical remark about the stylistic refinement of Nyugat essays.", "answer": "A Nyugat esszéművészete a pallérozott stílus és az európai műveltség csúcspontja."}], ["c1-essayistic-register"]),
                mc("grammar", "check", "Melyik állítás fogalmazza meg legpontosabban a polgári esszé lényegét?", [
                    "A személyes szubjektív élmény és az egyetemes kulturális műveltség párbeszéde.",
                    "Hivatalos statisztikai jelentések tényszerű ismertetése.",
                    "Kitalált mesebeli történetek elbeszélése."
                ], 0, ["c1-essayistic-register"])
            ]
        },
        {
            "num": 3,
            "stem": f"c1-{slug}-03",
            "title": "Irony and Erudition: Antal Szerb's Scholarly Charm",
            "grammar_title": "Polite Irony, Conversational Warmth, and Essayistic Distance",
            "grammar_skill": "c1-stylistic-politeness",
            "goals": [
                "I can analyze Antal Szerb's unique synthesis of scholarly erudition and playful irony.",
                "I can use polite disclaimers and witty intellectual hedges in Hungarian.",
                "I can appreciate how literary portraiture balances humor and profound melancholy."
            ],
            "vocab": [
                {"lemma": "erudíció", "translation": "erudition, profound learning", "pos": "noun"},
                {"lemma": "önirónia", "translation": "self-irony, self-deprecating humor", "pos": "noun"},
                {"lemma": "könnyedség", "translation": "lightness, effortless grace", "pos": "noun"},
                {"lemma": "szellemesség", "translation": "wittiness, cleverness", "pos": "noun"},
                {"lemma": "melankólia", "translation": "melancholy", "pos": "noun"},
                {"lemma": "megbocsátó", "translation": "forgiving, indulgent", "pos": "adjective"},
                {"lemma": "báj", "translation": "charm, grace", "pos": "noun"},
                {"lemma": "olvasmányos", "translation": "eminently readable, engaging", "pos": "adjective"}
            ],
            "gr_text1": "Antal Szerb mastered the art of wearing monumental erudition (*erudíció*) with effortless lightness (*könnyedség*). His prose employs delicate conversational understatement, gentle self-irony (*önirónia*), and witty parentheticals: *ahogy a kedves olvasó bizonyára sejti*.",
            "gr_text2": "Stylistic politeness in C1 literary essays softens dogmatic assertions: modal conditionals (*megkockáztathatjuk azt a feltevést*, *aligha tévedünk, ha úgy véljük*) invite the reader into a collegial conspiracy of cultivated minds.",
            "gr_table": [
                ["A tudós erudíció és a szellemes könnyedség ötvözete...", "The synthesis of scholarly erudition and witty lightness..."],
                ["Megkockáztathatjuk azt a feltevést, hogy...", "We may venture the assumption that..."],
                ["Finom öniróniával szemléli a világot...", "He observes the world with subtle self-irony..."]
            ],
            "world_story_seg": {
                "seg_slug": "szerb",
                "title": "Szerb Antal: A tudás varázsa és iróniája",
                "summary": "How Antal Szerb made the history of literature an unforgettable adventure of human eccentricities and poetic wonder.",
                "paragraphs": [
                    {"type": "narration", "text": "Kevesen tudtak olyan ellenállhatatlan bájjal és szeretettel írni a könyvekről, mint Szerb Antal. Számára a világirodalom története nem halott szerzők unalmas lexikona volt, hanem eleven, színes és kissé különc emberek találkozóhelye. Úgy beszélt Dantéról, Goethéről vagy éppen Kazinczyról, mintha tegnap délután teázott volna velük egy budapesti kávéház teraszán."},
                    {"type": "narration", "text": "Hatalmas, szinte enciklopédikus tudását olyan könnyedén hordozta, mint egy elegáns felöltőt. Ahol a hagyományos pozitivista tudósok száraz filológiai lábjegyzetekbe temetkeztek, ott Szerb Antal egyetlen szellemes fordulattal vagy finom öniróniával világította meg egy korszak lényegét. Pontosan tudta, hogy a humor és a melankólia a legmélyebb emberség két testvére."},
                    {"type": "narration", "text": "A varázsló eltűnik című esszékötetében és világirodalmi műveiben megmutatta: a legnagyobb tudományos teljesítmény nem az, ha elijesztjük az olvasót a tárgy nehézségével, hanem ha bevonjuk őt a megismerés és az intellektuális öröm közös kalandjába."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Miben rejlik Szerb Antal esszéírói stílusának titka?", [
                    "A hatalmas tudás és a játékos, önironikus könnyedség páratlan harmóniájában.",
                    "A könyörtelen és kíméletlen politikai támadásokban.",
                    "A nehezen érthető elvont filozófiai szakzsargonban."
                ], 0, ["c1-esszemuveszet-vocab"]),
                fb("grammar", "practice", "Szerb Antal írásait a mélységes tudós _____ és az olvasmányos báj egyedülálló ötvözete teszi halhatatlanná. (erudition / erudíció)", "erudíció", "Antal Szerb's writings are rendered immortal by the unique combination of profound scholarly erudition and readable charm.", ["c1-stylistic-politeness"]),
                match("vocabulary", "controlled", [["erudíció", "profound learning"], ["önirónia", "self-irony"], ["könnyedség", "effortless grace"], ["olvasmányos", "eminently readable"]], ["c1-esszemuveszet-vocab"]),
                sb("grammar", "practice", ["Szerb", "Antal", "a", "tudást", "az", "intellektuális", "öröm", "forrásává", "tette."], ["Szerb", "Antal", "a", "tudást", "az", "intellektuális", "öröm", "forrásává", "tette."], "Antal Szerb made knowledge a source of intellectual joy.", ["c1-stylistic-politeness"]),
                dc("dialogue", [
                    {"speaker": "Kritikus", "text": "Nem túl frivol dolog ilyen könnyedén írni klasszikusokról?"},
                    {"speaker": "Olvasó", "text": "Ellenkezőleg: ez a könnyedség valójában a legmélyebb tisztelet és megértés jele."},
                ], ["legmélyebb tisztelet", "teljes hozzáértés hiánya", "felszínes gúny"], 0, ["c1-stylistic-politeness"]),
                sw("production", [{"prompt": "Write a polite scholarly conjecture using 'Megkockáztathatjuk azt a feltevést'.", "answer": "Megkockáztathatjuk azt a feltevést, hogy a szerző célja az olvasó szórakoztatva tanítása volt."}], ["c1-stylistic-politeness"]),
                mc("grammar", "check", "Melyik stíluselem NEM jellemző Szerb Antal esszéire?", [
                    "Dogmatikus, száraz és rideg kinyilatkoztatás.",
                    "Finom irónia és megértő mosoly.",
                    "Olvasmányos, lenyűgöző mesélőkedv."
                ], 0, ["c1-stylistic-politeness"])
            ]
        },
        {
            "num": 4,
            "stem": f"c1-{slug}-04",
            "title": "European Perspectives: László Cs. Szabó",
            "grammar_title": "Cosmopolitan Geocultural Synthesis and Travel Essays",
            "grammar_skill": "c1-stylistic-politeness",
            "goals": [
                "I can evaluate László Cs. Szabó's geocultural essays and European synthesis.",
                "I can describe spatial and cultural migrations using elevated aesthetic terms.",
                "I can weave architectural, artistic, and historical threads into unified prose."
            ],
            "vocab": [
                {"lemma": "látóhatár", "translation": "horizon", "pos": "noun"},
                {"lemma": "geokultúra", "translation": "geoculture, cultural geography", "pos": "noun"},
                {"lemma": "európaiság", "translation": "Europeanness, European identity", "pos": "noun"},
                {"lemma": "vándorévek", "translation": "years of wandering, peregrination", "pos": "noun"},
                {"lemma": "tájkép", "translation": "landscape", "pos": "noun"},
                {"lemma": "beágyazottság", "translation": "embeddedness", "pos": "noun"},
                {"lemma": "szintézis", "translation": "synthesis", "pos": "noun"},
                {"lemma": "szellemi haza", "translation": "spiritual homeland", "pos": "noun"}
            ],
            "gr_text1": "László Cs. Szabó expanded the Hungarian essay to encompass the physical and spiritual landscape of the entire European continent. His geocultural essays connect Italian renaissance frescoes, English parliamentary traditions, and Transylvanian wooden belfries.",
            "gr_text2": "When constructing essays on cultural geography, use compound spatial nouns (*látóhatár, beágyazottság, szellemi haza*) and balancing adverbials to merge distant historical epochs into a single panoramic vision.",
            "gr_table": [
                ["Az európai szellemi haza határai...", "The borders of the European spiritual homeland..."],
                ["Mély kulturális beágyazottság...", "Deep cultural embeddedness..."],
                ["A táj és a történelem elválaszthatatlan szintézise...", "The inseparable synthesis of landscape and history..."]
            ],
            "world_story_seg": {
                "seg_slug": "csszabo",
                "title": "Cs. Szabó László: Európa vándora",
                "summary": "How László Cs. Szabó navigated European civilizations, building bridges between Hungarian heritage and universal Western culture.",
                "paragraphs": [
                    {"type": "narration", "text": "Cs. Szabó László számára Európa nem elvont politikai eszme vagy földrajzi térkép volt, hanem eleven, lélegző szellemi haza. Erdélyi származású íróként magában hordozta a határvidékek éber érzékenységét, miközben Rómában, Párizsban vagy Londonban sétálva otthonosan mozgott az európai művészet évszázadai között."},
                    {"type": "narration", "text": "Esszéiben a táj, a festészet és a történelem elválaszthatatlan szintézissé olvadt össze. Amikor egy toszkán dombtetőről vagy egy flamand csatornáról írt, sosem felejtette el megkeresni azokat a láthatatlan szálakat, amelyek a magyar sorsot a kontinens nagy drámájához kötik. Nála az utazás nem turizmus volt, hanem intellektuális zarándoklat."},
                    {"type": "narration", "text": "Bebizonyította, hogy az igazi magyarság és az egyetemes európaiság nem zárják ki egymást; éppen ellenkezőleg: minél mélyebben gyökerezik valaki saját anyanyelvében, annál tágasabb szellemi horizonttal képes befogadni a világ sokszínűségét."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Mi képezi Cs. Szabó László esszéinek sajátos tárgyát?", [
                    "A táj, a képzőművészet és a történelem egyetemes európai szintézise.",
                    "A modern gyáripar technológiai újításai.",
                    "A katonai taktika elméleti kérdései."
                ], 0, ["c1-esszemuveszet-vocab"]),
                fb("grammar", "practice", "Cs. Szabó esszéi a magyarság és az európaiság mélyreható szellemi _____ tanúsítják. (synthesis / szintézisét)", "szintézisét", "Cs. Szabó's essays attest to the profound intellectual synthesis of Hungarian identity and Europeanness.", ["c1-stylistic-politeness"]),
                match("vocabulary", "controlled", [["látóhatár", "horizon"], ["európaiság", "European identity"], ["beágyazottság", "embeddedness"], ["szellemi haza", "spiritual homeland"]], ["c1-esszemuveszet-vocab"]),
                sb("grammar", "practice", ["Az", "utazás", "számára", "egy", "mély", "szellemi", "zarándoklat", "volt."], ["Az", "utazás", "számára", "egy", "mély", "szellemi", "zarándoklat", "volt."], "Travel was a deep intellectual pilgrimage for him.", ["c1-stylistic-politeness"]),
                dc("dialogue", [
                    {"speaker": "Olvasó", "text": "Hogyan képes Cs. Szabó összekötni Erdélyt és Nyugat-Európát?"},
                    {"speaker": "Esszéíró", "text": "Úgy, hogy a lokális gyökereket mindig az egyetemes kultúra koordináta-rendszerébe helyezi."},
                ], ["egyetemes kultúra", "gazdasági érdek", "véletlen szerencse"], 0, ["c1-stylistic-politeness"]),
                sw("production", [{"prompt": "Write a sentence on the relationship between national roots and European horizon.", "answer": "A nemzeti kultúra legszebb virágait a tágas európai horizont fényében bontja ki."}], ["c1-stylistic-politeness"]),
                mc("grammar", "check", "Melyik fogalom fejezi ki Cs. Szabó László legfontosabb szellemi hitvallását?", [
                    "Az egyetemes európaiság és a nemzeti önazonosság szerves egysége.",
                    "A külvilágtól való teljes elzárkózás szükségessége.",
                    "A művészetek gazdasági haszonra váltása."
                ], 0, ["c1-stylistic-politeness"])
            ]
        },
        {
            "num": 5,
            "stem": f"c1-{slug}-05",
            "title": "Passionate Diagnosis: László Németh's Cultural Debates",
            "grammar_title": "Polemics of Moral Responsibility and Social Diagnosis",
            "grammar_skill": "c1-essayistic-register",
            "goals": [
                "I can analyze László Németh's prophetic, diagnostic essayistic register.",
                "I can understand key Hungarian intellectual debates (e.g., 'mélymagyar' vs. 'hígmagyar').",
                "I can deploy high-register analytical vocabulary regarding social responsibility."
            ],
            "vocab": [
                {"lemma": "kórkép", "translation": "clinical diagnosis, pathology of an era", "pos": "noun"},
                {"lemma": "küldetéstudat", "translation": "sense of mission, vocational awareness", "pos": "noun"},
                {"lemma": "minőségelv", "translation": "principle of quality", "pos": "noun"},
                {"lemma": "felelősségérzet", "translation": "sense of responsibility", "pos": "noun"},
                {"lemma": "sorskérdés", "translation": "vital question of national destiny", "pos": "noun"},
                {"lemma": "önvizsgálat", "translation": "self-examination, introspection", "pos": "noun"},
                {"lemma": "prófétai", "translation": "prophetic", "pos": "adjective"},
                {"lemma": "hivatástudat", "translation": "sense of calling, professional devotion", "pos": "noun"}
            ],
            "gr_text1": "László Németh represents the passionate, diagnostic stream of the Hungarian essay. Influenced by his medical background, he viewed cultural and social dilemmas as vital questions of destiny (*sorskérdés*) that demanded relentless self-examination (*önvizsgálat*) and an uncompromising principle of quality (*minőségelv*).",
            "gr_text2": "The diagnostic register employs medical and architectural metaphors (*kórkép, tünet, diagnózis, tartóoszlop*) combined with solemn duty markers (*erkölcsi parancs, történelmi felelősség*).",
            "gr_table": [
                ["A nemzeti sorskérdések könyörtelen elemzése...", "The relentless analysis of vital questions of destiny..."],
                ["A minőségelv megalkuvást nem ismerő követelménye...", "The uncompromising demand of the principle of quality..."],
                ["Mélységes erkölcsi felelősségérzet és önvizsgálat...", "Profound moral sense of responsibility and self-examination..."]
            ],
            "world_story_seg": {
                "seg_slug": "nemeth",
                "title": "Németh László és a minőség forradalma",
                "summary": "How László Németh sought to diagnose national crises through relentless intellectual rigor and the uncompromising principle of quality.",
                "paragraphs": [
                    {"type": "narration", "text": "Németh László nem egyszerűen szemlélője volt korának, hanem orvosa és prófétája. Orvosi diplomájával felvértezve úgy tekintett a társadalom és a kultúra válságaira, mint egy beteg szervezet lázas küzdelmére, ahol a tüneti kezelés helyett a baj legmélyebb gyökerét kell feltárni."},
                    {"type": "narration", "text": "Híres esszéiben – mint amilyen A minőség forradalma – azt hirdette, hogy egy kis nép egyetlen túlélési esélye a legmagasabb rendű szellemi és erkölcsi igényességben rejlik. Nem engedhetjük meg magunknak a középszerűséget, a provinciális önelégültséget vagy a felületes kompromisszumokat. Minden területen a 'minőségelvet' kell érvényesíteni."},
                    {"type": "narration", "text": "Írásai heves vitákat váltottak ki, sokan vádolták túlzott szigorral vagy utópizmussal. Ám szenvedélyes hite abban, hogy a kultúra a nemzet gerince és erkölcsi tartóoszlopa, a modern magyar esszé egyik legmegrázóbb és legmeghatározóbb fejezetévé avatta életművét."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Mit jelent a 'minőségelv' Németh László felfogásában?", [
                    "A legmagasabb rendű szellemi és erkölcsi igényesség megalkuvás nélküli követelményét.",
                    "A termékek ipari szabványosítását.",
                    "A külföldi áruk előnyben részesítését."
                ], 0, ["c1-esszemuveszet-vocab"]),
                fb("grammar", "practice", "Németh László esszéi a nemzeti sorskérdések könyörtelen _____ és morális elemzését nyújtják. (self-examination / önvizsgálatát)", "önvizsgálatát", "László Németh's essays provide a relentless self-examination and moral analysis of vital national destiny questions.", ["c1-essayistic-register"]),
                match("vocabulary", "controlled", [["kórkép", "pathology / diagnosis"], ["küldetéstudat", "sense of mission"], ["minőségelv", "principle of quality"], ["sorskérdés", "question of destiny"]], ["c1-esszemuveszet-vocab"]),
                sb("grammar", "practice", ["A", "nemzet", "egyetlen", "esélye", "a", "minőségelv", "következetes", "érvényesítése."], ["A", "nemzet", "egyetlen", "esélye", "a", "minőségelv", "következetes", "érvényesítése."], "The nation's only chance is the consistent enforcement of the principle of quality.", ["c1-essayistic-register"]),
                dc("dialogue", [
                    {"speaker": "Vitapartner", "text": "Nem túl idealista a minőség forradalmát követelni egy válságos korban?"},
                    {"speaker": "Esszéíró", "text": "Éppen a válság mutatja meg, hogy a középszerűség pusztuláshoz vezet."},
                ], ["középszerűség pusztuláshoz vezet", "nincs szükség változásra", "minden jól van így"], 0, ["c1-essayistic-register"]),
                sw("production", [{"prompt": "Write a sentence reflecting on Németh László's sense of mission.", "answer": "Németh László prófétai küldetéstudata az önvizsgálat és a szellemi minőség melletti kiállás."}], ["c1-essayistic-register"]),
                mc("grammar", "check", "Melyik állítás foglalja össze legtalálóbban Németh László esszéírói örökségét?", [
                    "A megalkuvást nem ismerő erkölcsi felelősségvállalás és szellemi szigorúság.",
                    "A felhőtlen és gondtalan szórakoztatás igénye.",
                    "A történelmi vitáktól való teljes távolságtartás."
                ], 0, ["c1-essayistic-register"])
            ]
        }
    ]

    for l in disc_lessons:
        emit_instructional_lesson(2, "discourse", l, disc_title, disc_intro if l["num"] == 1 else None)

    # Full World Compilation Story
    write_json(
        f"stories/world/c1/{slug}.json",
        {
            "id": f"story.c1.world.{slug}",
            "title": "Az esszé dicsérete: Pázmánytól Szerb Antalig",
            "level": "C1",
            "type": "world",
            "summary": "Comprehensive exploration of the Golden Age of the Hungarian Essay: from Péter Pázmány's baroque orations through Nyugat, Antal Szerb, Cs. Szabó, and László Németh.",
            "paragraphs": [
                {"type": "narration", "text": "A tizenhetedik század elején Pázmány Péter tollán született meg a modern magyar érvelő próza. A barokk szónok felismerte, hogy a lelkekért vívott küzdelmet csak azon a nyelven lehet megnyerni, amelyen az emberek álmodnak és éreznek. Áradó körmondataival és érzékletes képeivel a magyar mondatot acélos intellektuális fegyverré kovácsolta."},
                {"type": "narration", "text": "Három évszázaddal később a Nyugat folyóirat írói, Babits Mihály és Kosztolányi Dezső emelték az esszét az autonóm művészet rangjára. Babits az európai kultúra morális és szellemtörténeti katedrálisát építette fel műveiben, míg Kosztolányi a szavak rejtett zenéjét, az anyanyelv belső életét és a stílus páratlan hajlékonyságát kutatta."},
                {"type": "narration", "text": "Szerb Antal ehhez a gazdag örökséghez a sziporkázó erudíció és a megértő önirónia báját tette hozzá. Számára a világirodalom nem száraz akadémiai tananyag volt, hanem a legcsodálatosabb emberi kaland, ahol a humor és a melankólia elválaszthatatlanul kiegészítik egymást."},
                {"type": "narration", "text": "Cs. Szabó László geokultúrája tágas európai horizontot nyitott a magyar prózának: a toszkán tájak, flamand városok és erdélyi falvak szintézisében felmutatta a közös szellemi hazát. Németh László pedig a minőségelv és az önvizsgálat szigorú orvosi felelősségével figyelmeztetett a sorskérdésekre."},
                {"type": "narration", "text": "Ez a sokrétű, lüktető hagyomány bizonyítja: a magyar esszé nem csupán irodalmi műfaj, hanem nemzeti önismeretünk legfontosabb tükre és szellemi szabadságunk örök záloga."}
            ]
        }
    )

    # Discourse Consolidation
    emit_consolidation_lesson(
        2,
        "discourse",
        f"c1-{slug}-consolidation",
        disc_title,
        [
            "I can analyze the stylistic characteristics of the Hungarian essay tradition.",
            "I can compare the rhetorical strategies of Pázmány, Babits, Szerb, Cs. Szabó, and Németh László.",
            "I can employ elevated essayistic and literary critical vocabulary with confidence."
        ],
        [
            mc("grammar", "recognize", "Melyik szerző nevéhez kötődik a 'minőségelv' fogalma?", [
                "Németh Lászlóhoz",
                "Szerb Antalhoz",
                "Pázmány Péterhez"
            ], 0, ["c1-essayistic-register"]),
            mc("grammar", "recognize", "Milyen stílusjegy jellemzi leginkább Szerb Antal esszéit?", [
                "A mély tudományos erudíció és a szellemes önirónia harmonikus ötvözete.",
                "A száraz bürokratikus fogalmazásmód.",
                "A vallási pátosz kizárólagos alkalmazása."
            ], 0, ["c1-stylistic-politeness"]),
            match("vocabulary", "recognize", [["retorika", "rhetoric"], ["erudíció", "profound learning"], ["minőségelv", "principle of quality"], ["látóhatár", "horizon"], ["önvizsgálat", "self-examination"]], ["c1-esszemuveszet-vocab"]),
            fb("vocabulary", "recall", "A Nyugat írói az esszét az egyetemes szellemi _____ tágas terébe helyezték. (horizon / horizontjának)", "horizontjának", "The writers of Nyugat placed the essay into the spacious space of its universal intellectual horizon.", ["c1-esszemuveszet-vocab"]),
            fb("vocabulary", "recall", "Pázmány Péter szónoklatai a magyar érvelő próza megkerülhetetlen _____ képezik. (cornerstone / alapkövét)", "alapkövét", "Péter Pázmány's speeches constitute the inescapable cornerstone of Hungarian argumentative prose.", ["c1-esszemuveszet-vocab"]),
            fb("grammar", "recall", "Szerb Antal írásait az önirónia és a melankólia finom _____ teszi egyedivé. (nuanced shading / árnyalása)", "árnyalása", "Antal Szerb's writings are made unique by the subtle nuancing of self-irony and melancholy.", ["c1-stylistic-politeness"]),
            fb("grammar", "context", "Cs. Szabó László esszéiben a lokális tapasztalat és az európaiság tökéletes _____ alkot. (synthesis / szintézist)", "szintézist", "In László Cs. Szabó's essays, local experience and European identity form a perfect synthesis.", ["c1-stylistic-politeness"]),
            fb("grammar", "context", "Németh László szerint a nemzet sorskérdéseit csak szigorú erkölcsi _____ lehet tisztázni. (self-examination / önvizsgálattal)", "önvizsgálattal", "According to László Németh, the nation's vital destiny questions can only be clarified through strict moral self-examination.", ["c1-essayistic-register"]),
            mc("grammar", "context", "Hogyan járult hozzá a Nyugat nemzedéke a magyar esszé felemelkedéséhez?", [
                "Művészi rangra emelte a műfajt, egyesítve a filozófiai mélységet és a stilisztikai fegyelmet.",
                "Kizárólag politikai röpiratokat adott közre.",
                "Leegyszerűsítette a nyelvet tőmondatokra."
            ], 0, ["c1-essayistic-register"]),
            sb("grammar", "produce", ["A", "magyar", "esszé", "a", "nemzeti", "önismeret", "legfontosabb", "szellemi", "tükre."], ["A", "magyar", "esszé", "a", "nemzeti", "önismeret", "legfontosabb", "szellemi", "tükre."], "The Hungarian essay is the most important intellectual mirror of national self-awareness.", ["c1-essayistic-register"]),
            sw("production", [{"prompt": "Write a critical synthesis sentence comparing Szerb Antal and Babits Mihály.", "answer": "Míg Babits az erkölcsi fenség pátoszát képviseli, addig Szerb Antal a tudás ironikus bájával hódít."}], ["c1-essayistic-register"]),
            sw("production", [{"prompt": "Formulate a concluding thought on the Hungarian essayistic tradition.", "answer": "Az esszé hagyománya bizonyítja, hogy a magyar nyelv a legelvontabb eszmék kifejezésére is tökéletesen alkalmas."}], ["c1-essayistic-register"])
        ]
    )
    print("=== Finished C1 Unit 2 ===")


if __name__ == "__main__":
    generate_unit_2()
