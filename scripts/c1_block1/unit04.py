#!/usr/bin/env python3
"""
Hungarian C1 Block 1 - Unit 04 Generator:
  - Track 1 (Core): Unit 4 — "The Mechanics of Polemics & Rhetorical Refutation" (c1-04)
  - Track 2 (Discourse): Unit 4 — "The Art of Hungarian Public Debate" (c1-vitakultura)
"""

from .common import mc, match, fb, sb, dc, sw, write_json, emit_instructional_lesson, emit_consolidation_lesson


def generate_unit_4():
    print("=== Generating C1 Unit 4 ===")
    
    # ----------------------------------------------------
    # TRACK 1: CORE (c1-04)
    # ----------------------------------------------------
    core_title = "The Mechanics of Polemics & Rhetorical Refutation"
    core_intro = [
        "In high-stakes public debate and critical intellectual polemics, refuting an opponent requires more than just denying their claims; it demands dissecting their logical fallacies, turning their premises against them, and mastering contrastive topicalization.",
        "In this unit, inspired by Endre Ady's fiery, uncompromising political essays in 'Robogunk a forradalomba', you will master the rhetorical architecture of refutation (bármennyire is, korántsem, épp ellenkezőleg, reductio ad absurdum) and the art of devastating intellectual polemic."
    ]

    core_lessons = [
        {
            "num": 1,
            "stem": "c1-04-01",
            "title": "Concession Before Demolition: Bármennyire is and Legyen bár így",
            "grammar_title": "Maximal Concession Leading to Sharp Refutation",
            "grammar_skill": "c1-rhetorical-refutation",
            "goals": [
                "I can grant an opponent's premise to its maximum extent using 'bármennyire is'.",
                "I can introduce devastating refutations following an apparent concession.",
                "I can deploy high-register adversarial discourse markers in Hungarian."
            ],
            "vocab": [
                {"lemma": "bármennyire is", "translation": "no matter how much, however much", "pos": "expression"},
                {"lemma": "legyen bár így", "translation": "be that as it may, even if it were so", "pos": "expression"},
                {"lemma": "cáfolat", "translation": "refutation, rebuttal", "pos": "noun"},
                {"lemma": "tetszetős", "translation": "specious, superficially appealing", "pos": "adjective"},
                {"lemma": "megdönthetetlen", "translation": "irrefutable", "pos": "adjective"},
                {"lemma": "elméleti sík", "translation": "theoretical plane / level", "pos": "noun"},
                {"lemma": "gyakorlati csőd", "translation": "practical failure / collapse", "pos": "noun"},
                {"lemma": "visszautasít", "translation": "to reject, rebuff", "pos": "verb"}
            ],
            "gr_text1": "The tactical concession (*engedményes cáfolat*) is among the most effective weapons in Hungarian rhetoric. By granting an opponent's point using *bármennyire is* (no matter how much...) or *legyen bár így* (be that as it may), the speaker disarms accusations of bias before delivering an irrefutable counter-blow.",
            "gr_text2": "The counter-clause is marked by strong adversative particles (*mégis, mindazonáltal, mindennek ellenére*): *Bármennyire is tetszetősnek tűnik az érvelés, a valóságban tarthatatlan.*",
            "gr_table": [
                ["Bármennyire is vonzó az elmélet, mégis téves.", "However attractive the theory seems, it is nonetheless false."],
                ["Legyen bár így, a következtetés nem állja meg a helyét.", "Be that as it may, the conclusion does not hold."],
                ["Bármennyire igyekeznek is elfedni a tényeket...", "No matter how much they try to conceal the facts..."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Miért alkalmazunk taktikai engedményt a vitában?", ["Mert az ellenfél érvének részleges elismerése hitelesíti a későbbi döntő cáfolatot.", "Mert feladjuk a vitát.", "Mert egyetértünk az ellenféllel."], 0, ["c1-04-vocab"]),
                fb("grammar", "controlled", "_____ is tetszetős az elmélet, a gyakorlatban teljesen megbukott. (However much / Bármennyire)", "Bármennyire", "However much the theory is appealing, in practice it completely failed.", ["c1-rhetorical-refutation"]),
                match("vocabulary", "controlled", [["bármennyire is", "no matter how much"], ["legyen bár így", "be that as it may"], ["tetszetős", "specious / superficially appealing"], ["cáfolat", "rebuttal"]], ["c1-04-vocab"]),
                fb("grammar", "practice", "_____ bár így a dolog, a morális felelősség alól senki sem bújhat ki. (Be that as it may / Legyen)", "Legyen", "Be that as it may, no one can evade moral responsibility.", ["c1-rhetorical-refutation"]),
                sb("grammar", "practice", ["Bármennyire", "is", "hangosak", "a", "kritikusok,", "a", "tények", "magukért", "beszélnek."], ["Bármennyire", "is", "hangosak", "a", "kritikusok,", "a", "tények", "magukért", "beszélnek."], "No matter how loud the critics are, the facts speak for themselves.", ["c1-rhetorical-refutation"]),
                dc("dialogue", [
                    {"speaker": "Vitapartner", "text": "De el kell ismernie, hogy a javaslatunk rendkívül népszerű!"},
                    {"speaker": "Felszólaló", "text": "Bármennyire is népszerű, gazdaságilag katasztrófához vezet."},
                ], ["Bármennyire is népszerű", "Nagyon örülök neki", "Mindenben támogatjuk"], 0, ["c1-rhetorical-refutation"]),
                sw("production", [{"prompt": "Write a tactical concession sentence using 'Bármennyire is... mégis...'.", "answer": "Bármennyire is meggyőzőnek látszik a felvetés, a bizonyítékok mégis cáfolják."}], ["c1-rhetorical-refutation"]),
                mc("grammar", "check", "Melyik mondat alkalmazza a legélesebb retorikai cáfolatot?", [
                    "Bármennyire is magabiztos az állítás, a történelem tanúsága szerint téves.",
                    "Az állítás talán nem olyan jó, de azért elmegy.",
                    "Nem tudom, mit mondjak erre."
                ], 0, ["c1-rhetorical-refutation"])
            ]
        },
        {
            "num": 2,
            "stem": "c1-04-02",
            "title": "Emphatic Focus and Topicalization: Korántsem and Épp ellenkezőleg",
            "grammar_title": "Emphatic Topicalization and Polar Word-Order Inversion",
            "grammar_skill": "c1-polemical-topicalization",
            "goals": [
                "I can use contrastive focus particles (*korántsem, épp ellenkezőleg, korántsem úgy*).",
                "I can manipulate Hungarian pre-verbal focus position for maximum polemical impact.",
                "I can shatter misconceptions with emphatic syntactic inversion."
            ],
            "vocab": [
                {"lemma": "korántsem", "translation": "by no means, far from it", "pos": "adverb"},
                {"lemma": "épp ellenkezőleg", "translation": "quite the contrary, exactly the opposite", "pos": "expression"},
                {"lemma": "fókuszpozíció", "translation": "focus position (syntax)", "pos": "noun"},
                {"lemma": "hangsúlyáthelyezés", "translation": "stress shift, shift of emphasis", "pos": "noun"},
                {"lemma": "téveszme", "translation": "delusion, misconception, fallacy", "pos": "noun"},
                {"lemma": "félreértés", "translation": "misunderstanding", "pos": "noun"},
                {"lemma": "megfordít", "translation": "to reverse, invert", "pos": "verb"},
                {"lemma": "kifejezetten", "translation": "expressly, explicitly, decidedly", "pos": "adverb"}
            ],
            "gr_text1": "Hungarian information structure relies on the immediately pre-verbal focus position (*fókuszpozíció*). In polemics, particles like *korántsem* (far from it / by no means) placed in focus reject an erroneous presupposition while simultaneously introducing the true predicate.",
            "gr_text2": "*Épp ellenkezőleg* triggers an inversion of the opponent's core claim: *Nem a hanyatlás kezdetéről van szó; épp ellenkezőleg, a szellemi megújulás hajnalát látjuk.*",
            "gr_table": [
                ["A helyzet korántsem olyan egyszerű.", "The situation is by no means so simple."],
                ["Nem gyengült a mozgalom; épp ellenkezőleg, megerősödött.", "The movement didn't weaken; quite the contrary, it grew stronger."],
                ["Korántsem erről van szó!", "That is far from being the issue!"]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mit fejez ki a 'korántsem' szó a mondatban?", ["Hangsúlyos, kategorikus tagadást és a feltevés elvetését.", "Feltételes egyetértést.", "Időbeli közelséget."], 0, ["c1-04-vocab"]),
                fb("grammar", "controlled", "A feladat megoldása _____ volt olyan kézenfekvő, mint ahogy a bírálók hitték. (by no means / korántsem)", "korántsem", "The solution of the task was by no means as obvious as the critics believed.", ["c1-polemical-topicalization"]),
                match("vocabulary", "controlled", [["korántsem", "by no means"], ["épp ellenkezőleg", "quite the contrary"], ["téveszme", "misconception"], ["fókuszpozíció", "focus position"]], ["c1-04-vocab"]),
                fb("grammar", "practice", "Nem vesztettük el a lendületünket; _____ ellenkezőleg, újult erővel folytatjuk a munkát. (quite / épp)", "épp", "We have not lost our momentum; quite the contrary, we continue the work with renewed vigor.", ["c1-polemical-topicalization"]),
                sb("grammar", "practice", ["A", "kérdés", "korántsem", "zárult", "le", "a", "tegnapi", "szavazással."], ["A", "kérdés", "korántsem", "zárult", "le", "a", "tegnapi", "szavazással."], "The question was by no means closed with yesterday's vote.", ["c1-polemical-topicalization"]),
                dc("dialogue", [
                    {"speaker": "Riporter", "text": "Tehát beismerik a projekt kudarcát?"},
                    {"speaker": "Képviselő", "text": "Korántsem; a vártnál sokkal jobb eredményeket értünk el."},
                ], ["Korántsem", "Természetesen", "Valószínűleg"], 0, ["c1-polemical-topicalization"]),
                sw("production", [{"prompt": "Write a polemical sentence rejecting an assumption using 'épp ellenkezőleg'.", "answer": "Nem a hagyományok feladásáról van szó; épp ellenkezőleg, azok megőrzéséért küzdünk."}], ["c1-polemical-topicalization"]),
                mc("grammar", "check", "Melyik mondat használja a leghatásosabban a fókuszhelyzetű 'korántsem' szerkezetet?", [
                    "A vita tétje korántsem csupán személyes ambíciók harca, hanem elvi kérdés.",
                    "A vita talán nem korántsem jó dolog.",
                    "Korántsem nem tetszik nekem ez a dolog."
                ], 0, ["c1-polemical-topicalization"])
            ]
        },
        {
            "num": 3,
            "stem": "c1-04-03",
            "title": "Reductio ad Absurdum: Ha elfogadnánk, abból az következne",
            "grammar_title": "Counterfactual Consequences and Logical Contradiction Framing",
            "grammar_skill": "c1-reductio-argumentation",
            "goals": [
                "I can construct 'reductio ad absurdum' arguments (*a képtelenségig való vitel*).",
                "I can use counterfactual conditional matrixes (*ha elfogadnánk..., abból az következne...*).",
                "I can expose internal contradictions in opposing logic."
            ],
            "vocab": [
                {"lemma": "képtelenség", "translation": "absurdity, preposterousness", "pos": "noun"},
                {"lemma": "önellentmondás", "translation": "self-contradiction", "pos": "noun"},
                {"lemma": "abból az következne", "translation": "from that it would follow that", "pos": "expression"},
                {"lemma": "tarthatatlan", "translation": "untenable, unsustainable", "pos": "adjective"},
                {"lemma": "következmény", "translation": "consequence", "pos": "noun"},
                {"lemma": "visszájára fordul", "translation": "to backfire, turn inside out", "pos": "expression"},
                {"lemma": "levezet", "translation": "to deduce, derive", "pos": "verb"},
                {"lemma": "érvelési hiba", "translation": "fallacy, error in reasoning", "pos": "noun"}
            ],
            "gr_text1": "*Reductio ad absurdum* temporarily adopts the opponent's premise as true and logically derives a catastrophic or absurd consequence (*képtelenség*). In Hungarian, this requires complex past or present conditional syntax (*-na/-ne*, *-na/-ne volna*).",
            "gr_text2": "The formula *Ha elfogadnánk ezt az állítást, abból szükségszerűen az következne, hogy...* demonstrates that the opponent's position is inherently self-contradictory (*önellentmondásos*).",
            "gr_table": [
                ["Ha ezt elfogadnánk, abból az következne, hogy...", "If we accepted this, from that it would follow that..."],
                ["Ez a logika önellentmondásba torkollik.", "This logic runs into a self-contradiction."],
                ["Az érv a visszájára fordul a valóságban.", "The argument turns into its opposite in reality."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mi a lényege a 'reductio ad absurdum' érvelésnek?", ["Az ellenfél tézisének ideiglenes elfogadása abból a célból, hogy logikai képtelenségre vagy önellentmondásra jussunk.", "A hangos kiabálás a vitában.", "A témától való elkalandozás."], 0, ["c1-04-vocab"]),
                fb("grammar", "controlled", "Ha elfogadnánk ezt a javaslatot, abból az _____, hogy a törvények mindenkire másként vonatkoznak. (would follow / következne)", "következne", "If we accepted this proposal, from that it would follow that laws apply differently to everyone.", ["c1-reductio-argumentation"]),
                match("vocabulary", "controlled", [["képtelenség", "absurdity"], ["önellentmondás", "self-contradiction"], ["tarthatatlan", "untenable"], ["érvelési hiba", "fallacy"]], ["c1-04-vocab"]),
                fb("grammar", "practice", "Ez az elmélet nyilvánvaló belső _____ torkollik. (self-contradiction / önellentmondásba)", "önellentmondásba", "This theory culminates in an obvious internal self-contradiction.", ["c1-reductio-argumentation"]),
                sb("grammar", "practice", ["Az", "ilyen", "érvelés", "törvényszerűen", "a", "visszájára", "fordul", "a", "gyakorlatban."], ["Az", "ilyen", "érvelés", "törvényszerűen", "a", "visszájára", "fordul", "a", "gyakorlatban."], "Such argumentation inevitably backfires in practice.", ["c1-reductio-argumentation"]),
                dc("dialogue", [
                    {"speaker": "Vitavezető", "text": "Miért tartja elfogadhatatlannak az ellenfél elvét?"},
                    {"speaker": "Szónok", "text": "Mert ha követnénk, abból az következne, hogy fel kell adnunk minden erkölcsi mércét."},
                ], ["abból az következne", "nagyon szeretjük", "mindenki egyetért vele"], 0, ["c1-reductio-argumentation"]),
                sw("production", [{"prompt": "Construct a reductio ad absurdum argument using 'Ha elfogadnánk..., abból az következne...'." , "answer": "Ha elfogadnánk ezt a logikát, abból az következne, hogy senki sem felelős a tetteiért."}], ["c1-reductio-argumentation"]),
                mc("grammar", "check", "Melyik állítás mutat rá sikeresen egy logikai tarthatatlanságra?", [
                    "A premissza elfogadása szükségszerűen önellentmondáshoz vezet, tehát tarthatatlan.",
                    "Nem tetszik nekem ez a mondat, úgyhogy rossz.",
                    "Mindenki tudja, hogy ez hülyeség."
                ], 0, ["c1-reductio-argumentation"])
            ]
        },
        {
            "num": 4,
            "stem": "c1-04-04",
            "title": "Rhetorical Questioning and Inquisitorial Assertion",
            "grammar_title": "Provocative Interrogation and Inquisitorial Rhetoric",
            "grammar_skill": "c1-rhetorical-refutation",
            "goals": [
                "I can deploy rhetorical questions to corner an opponent (*vajon joggal állítható-e?*).",
                "I can use interrogative cadence to lead an audience to inevitable conclusions.",
                "I can combine rhetorical questions with assertive declarative punchlines."
            ],
            "vocab": [
                {"lemma": "költői kérdés", "translation": "rhetorical question", "pos": "noun"},
                {"lemma": "vajon", "translation": "I wonder, is it indeed (rhetorical interrogative)", "pos": "adverb"},
                {"lemma": "joggal állítható-e", "translation": "can it rightly be claimed (that)", "pos": "expression"},
                {"lemma": "elodázhatatlan", "translation": "unpostponable, urgent", "pos": "adjective"},
                {"lemma": "szemlesütve", "translation": "eyes cast down, ashamed", "pos": "adverb"},
                {"lemma": "kihívás", "translation": "challenge", "pos": "noun"},
                {"lemma": "szembesítés", "translation": "confrontation, bringing face to face", "pos": "noun"},
                {"lemma": "elszámolás", "translation": "reckoning, accounting", "pos": "noun"}
            ],
            "gr_text1": "The rhetorical question (*költői kérdés*) is not an inquiry, but an emphatic assertion disguised as a question. The particle *vajon* introduces high-register intellectual interrogation: *Vajon joggal állítható-e, hogy a társadalom érdekeit képviselik? Aligha.*",
            "gr_text2": "In impassioned polemics, a succession of rapid rhetorical questions builds unbearable tension before the final declarative resolution.",
            "gr_table": [
                ["Vajon hihetünk-e még a szép szavaknak?", "Can we indeed still believe in fine words?"],
                ["Joggal állítható-e, hogy nem tudtunk a veszélyről?", "Can it rightly be claimed that we knew nothing of the danger?"],
                ["Hát van-e ennél nyilvánvalóbb bizonyíték?", "Why, is there any proof more obvious than this?"]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Milyen szerepet játszik a 'vajon' szó a szónoki kérdésben?", ["Emelkedett, elgondolkodtató hangsúlyt ad a költői kérdésnek.", "Kizárólag egyszerű eldöntendő kérdést tesz fel.", "Bizonytalanságot fejez ki a dátumok terén."], 0, ["c1-04-vocab"]),
                fb("grammar", "controlled", "_____ joggal állítható-e, hogy mindent megtettünk a katasztrófa elkerüléséért? (I wonder / Vajon)", "Vajon", "Can it indeed rightly be claimed that we did everything to avoid the catastrophe?", ["c1-rhetorical-refutation"]),
                match("vocabulary", "controlled", [["vajon", "I wonder (rhetorical)"], ["joggal állítható-e", "can it rightly be claimed"], ["elodázhatatlan", "unpostponable"], ["szembesítés", "confrontation"]], ["c1-04-vocab"]),
                fb("grammar", "practice", "A helyzet tisztázása és a felelősségre vonás most már _____ feladattá vált. (unpostponable / elodázhatatlan)", "elodázhatatlan", "The clarification of the situation and holding to account has now become an unpostponable task.", ["c1-rhetorical-refutation"]),
                sb("grammar", "practice", ["Vajon", "meddig", "lehet", "még", "szemet", "hunyni", "a", "tények", "felett?"], ["Vajon", "meddig", "lehet", "még", "szemet", "hunyni", "a", "tények", "felett?"], "I wonder how long one can still turn a blind eye to the facts?", ["c1-rhetorical-refutation"]),
                dc("dialogue", [
                    {"speaker": "Felszólaló", "text": "Vajon elfogadható-e a hallgatás egy ilyen történelmi pillanatban?"},
                    {"speaker": "Hallgatóság", "text": "Nem! A hallgatás ma cinkossággal ér fel."},
                ], ["hallgatás ma cinkossággal ér fel", "mindenki menjen haza", "várjunk még éveket"], 0, ["c1-rhetorical-refutation"]),
                sw("production", [{"prompt": "Write a powerful rhetorical question using 'Vajon joggal állítható-e...'.", "answer": "Vajon joggal állítható-e, hogy a jövő nemzedékek érdekeit nézzük, miközben feléljük a forrásokat?"}], ["c1-rhetorical-refutation"]),
                mc("grammar", "check", "Melyik stílushatást éri el a retorikai kérdések halmozása a szónoklatban?", [
                    "Drámai feszültséget kelt, és az elkerülhetetlen igazság felé irányítja a hallgatót.",
                    "Elaltatja a közönség figyelmét.",
                    "Nevetségessé teszi a szónokot."
                ], 0, ["c1-rhetorical-refutation"])
            ]
        },
        {
            "num": 5,
            "stem": "c1-04-05",
            "title": "Passionate Polemics: Endre Ady's Political Journalism",
            "grammar_title": "Prophetic Political Polemics and Visionary Prose",
            "grammar_skill": "c1-polemical-topicalization",
            "goals": [
                "I can analyze Endre Ady's devastating political essays in 'Robogunk a forradalomba'.",
                "I can discern apocalyptic metaphors, passionate invective, and diagnostic fury.",
                "I can write polemical critiques using expressive Hungarian vocabulary."
            ],
            "vocab": [
                {"lemma": "publicisztika", "translation": "political journalism, publicist writings", "pos": "noun"},
                {"lemma": "ostoroz", "translation": "to scourge, lash, castigate", "pos": "verb"},
                {"lemma": "megcsontosodott", "translation": "ossified, calcified, ingrained", "pos": "adjective"},
                {"lemma": "elmaradottság", "translation": "backwardness, underdevelopment", "pos": "noun"},
                {"lemma": "tisztánlátás", "translation": "clarity of vision, lucidity", "pos": "noun"},
                {"lemma": "kérlelhetetlen", "translation": "implacable, relentless", "pos": "adjective"},
                {"lemma": "látnoki", "translation": "visionary, prophetic", "pos": "adjective"},
                {"lemma": "vesztébe rohan", "translation": "to rush to one's doom", "pos": "expression"}
            ],
            "gr_text1": "Endre Ady's journalism remains the gold standard of Hungarian visionary polemics. Writing in Nagyvárad and Budapest, he lashed out (*ostorozott*) against feudal backwardness (*megcsontosodott elmaradottság*), political complacency, and national self-delusion.",
            "gr_text2": "Ady's prose relies on prophetic fronting: placing the existential crisis into the thematic slot and driving the sentence to an explosive rhythmic verdict: *Itt nem reformocskák kellenek: itt a történelem ítélőszéke előtt állunk.*",
            "gr_table": [
                ["A megcsontosodott viszonyok kérlelhetetlen ostorozása...", "The relentless castigation of ossified conditions..."],
                ["Látnoki tisztánlátás és mélységes aggodalom...", "Visionary clarity of vision and profound anxiety..."],
                ["Az ország vesztébe rohan, ha nem ébred fel...", "The country rushes to its doom if it does not awake..."]
            ],
            "classic_story": {
                "slug": "c1-04-ady",
                "author": "Ady Endre",
                "work": "Robogunk a forradalomba (1912)",
                "title": "A magyar ugar és a felrázó harag",
                "summary": "Endre Ady fiery polemical diagnostic of Hungarian political inertia, sounding the alarm against the blind sleepwalking into historical catastrophe.",
                "characters": ["Ady Endre"],
                "paragraphs": [
                    {"type": "narration", "text": "Amikor Ady Endre a huszadik század elejének újságjaiban tollat ragadott, nem egyszerű hírlapi cikkeket körmölt, hanem tüzes nyilakat lövellt a magyar társadalom megcsontosodott bástyáira. Nem volt hajlandó udvariasan hajlongani a feudális urak előtt, és nem tűrte a nemzeti önámítás kényelmes, altató hazugságait. Úgy látta: az ország vakon, alva járva robog a történelmi katasztrófa felé."},
                    {"type": "narration", "text": "Ady publicisztikája a legkíméletlenebb tisztánlátás művészete volt. Látnoki szemmel ismerte fel, hogy a látszólagos jólét és a millenniumi pompa mögött a szellem és a társadalom pusztító elmaradottsága tenyészik: a 'magyar Ugar', a 'Komp-ország', amely Ázsia és Európa között ingázik, anélkül hogy valóban megérkezne a modernitásba."},
                    {"type": "narration", "text": "Haragja azonban nem a gyűlöletből fakadt, hanem a megváltó szeretetből. Azért ostorozta oly kérlelhetetlenül nemzetét, mert forrón szerette, és mert nem tudta elviselni, hogy tehetséges, szép népe a kisszerűség és a provinciális gőg mocsarába fulladjon. Írásaival fel akarta rázni az alvókat, még mielőtt a történelem vihara mindent elsöpör."},
                    {"type": "narration", "text": "Ady prózája ma is eleven lángként éget. Megtanít arra, hogy az igazi hazaszeretet nem a hibák elfedése, hanem a bátor, kíméletlen szembenézés: a harc a fényért, a haladásért és az emberi méltóságért."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Mi jellemezte Ady Endre politikai publicisztikáját?", [
                    "A kíméletlen tisztánlátás, a látnoki harag és a megcsontosodott viszonyok bátor ostorozása.",
                    "A hatalom feltétlen és alázatos dicsérete.",
                    "A semleges és száraz gazdasági statisztikák ismertetése."
                ], 0, ["c1-04-vocab"]),
                fb("grammar", "practice", "Ady kérlelhetetlen szavakkal _____ a korabeli politikai elit felelőtlenségét. (scourged / ostorozta)", "ostorozta", "Ady with relentless words scourged the irresponsibility of the contemporary political elite.", ["c1-polemical-topicalization"]),
                match("vocabulary", "controlled", [["publicisztika", "political journalism"], ["ostoroz", "to scourge / lash"], ["elmaradottság", "backwardness"], ["tisztánlátás", "clarity of vision"]], ["c1-04-vocab"]),
                mc("reading", "practice", "Miért ostorozta Ady olyan szenvedéllyel a hazáját a szöveg szerint?", [
                    "Mert forrón szerette a nemzetét, és fel akarta rázni az alvókat a pusztulás előtt.",
                    "Mert el akart költözni külföldre végleg.",
                    "Mert fizetést kapott az ellenséges országoktól."
                ], 0, None),
                mc("reading", "practice", "Mit jelképez a 'Komp-ország' metaforája Ady gondolkodásában?", [
                    "Az Európa és Ázsia közötti bizonytalan ingázást és a modernitásba való megérkezés hiányát.",
                    "A dunai hajózás fejlődését.",
                    "A szigetek közötti kompforgalom menetrendjét."
                ], 0, None),
                sb("grammar", "practice", ["A", "nemzeti", "önámítás", "mindig", "történelmi", "katasztrófához", "vezet."], ["A", "nemzeti", "önámítás", "mindig", "történelmi", "katasztrófához", "vezet."], "National self-delusion always leads to historical catastrophe.", ["c1-polemical-topicalization"]),
                sw("production", [{"prompt": "Write a passionate polemical statement in Ady's spirit about facing hard truths.", "answer": "Az igazi hazaszeretet a gyávaság elutasításán és a kíméletlen tisztánlátáson alapul."}], ["c1-polemical-topicalization"]),
                mc("grammar", "check", "Melyik fogalom összegzi leginkább Ady haragjának forrását?", [
                    "A felelősségérzetből és féltő szeretetből fakadó prófétai tisztánlátás.",
                    "A személyes sértettség és bosszúvágy.",
                    "A hideg közöny és cinizmus."
                ], 0, ["c1-polemical-topicalization"])
            ]
        }
    ]

    for l in core_lessons:
        emit_instructional_lesson(4, "core", l, core_title, core_intro if l["num"] == 1 else None)

    # Core Consolidation
    emit_consolidation_lesson(
        4,
        "core",
        "c1-04-consolidation",
        core_title,
        [
            "I can execute tactical concessions followed by devastating refutations.",
            "I can manipulate pre-verbal focus with 'korántsem' and 'épp ellenkezőleg'.",
            "I can formulate reductio ad absurdum arguments and rhetorical challenges."
        ],
        [
            mc("grammar", "recognize", "Melyik fordulat vezeti be a legpontosabban a taktikai engedményt?", [
                "Bármennyire is vonzónak tűnik az elképzelés...",
                "Az elképzelés azért jó, mert...",
                "Nem tudom, mi a baj az elképzeléssel..."
            ], 0, ["c1-rhetorical-refutation"]),
            mc("grammar", "recognize", "Milyen hatást ér el az 'épp ellenkezőleg' kifejezés?", [
                "Gyökeresen megfordítja az ellenfél által felállított tézist.",
                "Enyhe bizonytalanságot fejez ki.",
                "Lezárja a beszélgetést köszönetnyilvánítással."
            ], 0, ["c1-polemical-topicalization"]),
            match("vocabulary", "recognize", [["bármennyire is", "no matter how much"], ["korántsem", "by no means"], ["épp ellenkezőleg", "quite the contrary"], ["önellentmondás", "self-contradiction"], ["ostoroz", "to scourge"]], ["c1-04-vocab"]),
            fb("vocabulary", "recall", "A reformok elindítása mostanra halaszthatatlan, _____ feladattá vált. (unpostponable / elodázhatatlan)", "elodázhatatlan", "Starting the reforms has by now become an unpostponable task.", ["c1-04-vocab"]),
            fb("vocabulary", "recall", "A bírálók által felhozott elmélet nyilvánvaló belső _____ torkollik. (self-contradiction / önellentmondásba)", "önellentmondásba", "The theory adduced by critics runs into an obvious internal self-contradiction.", ["c1-04-vocab"]),
            fb("grammar", "recall", "A helyzet _____ volt olyan egyszerű, mint ahogyan a hivatalos jelentések állították. (by no means / korántsem)", "korántsem", "The situation was by no means as simple as official reports claimed.", ["c1-polemical-topicalization"]),
            fb("grammar", "context", "Ha ezt elfogadnánk, abból az _____, hogy a felelősség teljesen megszűnik. (would follow / következne)", "következne", "If we accepted this, from that it would follow that responsibility ceases entirely.", ["c1-reductio-argumentation"]),
            fb("grammar", "context", "_____ joggal állítható-e, hogy a társadalom felkészült a változásokra? (I wonder / Vajon)", "Vajon", "Can it indeed rightly be claimed that society is prepared for the changes?", ["c1-rhetorical-refutation"]),
            mc("grammar", "context", "Mi a reductio ad absurdum legfontosabb lépése?", [
                "Az ellenfél premisszájából kiindulva logikailag képtelen következményt levezetni.",
                "Kinevetni az ellenfél ruháját.",
                "Megváltoztatni a beszélgetés témáját a sportra."
            ], 0, ["c1-reductio-argumentation"]),
            sb("grammar", "produce", ["A", "történelmi", "tisztánlátás", "megköveteli", "az", "önámítás", "kérlelhetetlen", "elvetését."], ["A", "történelmi", "tisztánlátás", "megköveteli", "az", "önámítás", "kérlelhetetlen", "elvetését."], "Historical clarity of vision demands the relentless rejection of self-delusion.", ["c1-polemical-topicalization"]),
            sw("production", [{"prompt": "Write a tactical refutation using 'Bármennyire is... mégis...'.", "answer": "Bármennyire is csábító a gyors siker, a hosszú távú kockázatok mégis elfogadhatatlanok."}], ["c1-rhetorical-refutation"]),
            sw("production", [{"prompt": "Write a reductio ad absurdum argument exposing an internal contradiction.", "answer": "Ha elfogadnánk ezt a tételt, abból az következne, hogy az igazság a többség szeszélye szerint változik."}], ["c1-reductio-argumentation"])
        ]
    )

    # ----------------------------------------------------
    # TRACK 2: DISCOURSE (c1-vitakultura)
    # ----------------------------------------------------
    slug = "vitakultura"
    disc_title = "The Art of Hungarian Public Debate"
    disc_intro = [
        "Hungarian political freedom was born not in silent consensus, but in fiery, disciplined parliamentary debates. The Reform Era and the Age of Dualism forged a culture of oratory where the spoken word could reshape laws, borders, and national identity.",
        "In this unit, you will explore the giants of Hungarian debate: the historic clash between Count István Széchenyi and Lajos Kossuth, Ferenc Deák's legal precision, dualist parliamentary obstruction, legendary press polemics, and the evolution of public discourse in the digital era."
    ]

    disc_lessons = [
        {
            "num": 1,
            "stem": f"c1-{slug}-01",
            "title": "The Clash of Giants: Széchenyi and Kossuth",
            "grammar_title": "Rhetorical Duels and Classical Parliamentary Debate",
            "grammar_skill": "c1-parliamentary-debate",
            "goals": [
                "I can analyze the fundamental political debate of the Reform Era between Széchenyi and Kossuth.",
                "I can contrast evolutionary organic reform with revolutionary popular enthusiasm.",
                "I can deploy high-register oratorical vocabulary in Hungarian."
            ],
            "vocab": [
                {"lemma": "reformkor", "translation": "Reform Era (1825–1848)", "pos": "noun"},
                {"lemma": "szónoki párbaj", "translation": "oratorical duel", "pos": "noun"},
                {"lemma": "szerves fejlődés", "translation": "organic development", "pos": "noun"},
                {"lemma": "lelkesedés", "translation": "enthusiasm, zeal", "pos": "noun"},
                {"lemma": "megfontoltság", "translation": "deliberation, circumspection", "pos": "noun"},
                {"lemma": "nemzetébresztés", "translation": "awakening of the nation", "pos": "noun"},
                {"lemma": "ellentétpár", "translation": "oppositional pair, dichotomy", "pos": "noun"},
                {"lemma": "érdekegyesítés", "translation": "unification of interests (between nobles & serfs)", "pos": "noun"}
            ],
            "gr_text1": "The Reform Diet of Pozsony (Bratislava) birthed modern Hungarian parliamentary debate. Count István Széchenyi championed patient economic modernization (*szerves fejlődés*), while Lajos Kossuth wielded thunderous popular rhetoric to achieve civic emancipation (*érdekegyesítés*).",
            "gr_text2": "Parliamentary debate formulas combine formal decorum with relentless political thrust: *Tisztelt Ház! Nem térhetünk ki a történelmi felelősség elől...*",
            "gr_table": [
                ["A reformkor két óriásának szellemi párbaja...", "The intellectual duel of the two giants of the Reform Era..."],
                ["Szerves gazdasági fejlődés kontra forradalmi lendület...", "Organic economic development versus revolutionary momentum..."],
                ["A nemzet érdekeinek egyesítése...", "The unification of the nation's interests..."]
            ],
            "world_story_seg": {
                "seg_slug": "reformkor",
                "title": "Széchenyi és Kossuth: A nemzet hajnalán",
                "summary": "How the ideological duel between Count István Széchenyi and Lajos Kossuth defined the two paths of Hungarian modernization.",
                "paragraphs": [
                    {"type": "narration", "text": "A tizenkilencedik század harmincas és negyvenes éveiben a pozsonyi országgyűlés falai között dőlt el a modern Magyarország sorsa. Két rendkívüli szellem állt a küzdőtér két oldalán: Gróf Széchenyi István, a 'legnagyobb magyar', és Kossuth Lajos, a nemzet lánglelkű szónoka."},
                    {"type": "narration", "text": "Széchenyi a józan, szerves fejlődés híve volt. Úgy vélte, a nemzetet először gazdaságilag és erkölcsileg kell megerősíteni: hidakat kell verni, folyókat szabályozni, akadémiát alapítani és gőzhajózást indítani. Óva intett a bécsi udvarral való korai összeütközéstől, féltve a nemzetet a vérbefojtott tragédiától. Kossuth ezzel szemben felismerte: gazdasági haladás nem létezhet politikai szabadság és a jobbágyság azonnali felszabadítása nélkül. Az érdekegyesítés jelszavával a nép millióit állította a nemzeti ügy mellé."},
                    {"type": "narration", "text": "Párbajuk nem a gyűlölet harca volt, hanem két mélységesen elkötelezett hazafi vitája a jövőről. Bár útjaik elváltak, kettejük szellemi feszültsége teremtette meg azt a történelmi energiát, amely elvezetett 1848 dicsőséges tavaszához."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Mi volt a központi vita Széchenyi és Kossuth között a reformkorban?", [
                    "A lassú, szerves gazdasági reformok és a gyors, politikai érdekegyesítés és függetlenség útja közötti választás.",
                    "Hogy hol épüljön fel az új színház.",
                    "A bécsi opera új karmesterének személye."
                ], 0, ["c1-vitakultura-vocab"]),
                fb("grammar", "practice", "Kossuth legfőbb történelmi érdeme az _____ elvének kidolgozása és megvalósítása volt. (unification of interests / érdekegyesítés)", "érdekegyesítés", "Kossuth's chief historical merit was the elaboration and realization of the principle of unification of interests.", ["c1-parliamentary-debate"]),
                match("vocabulary", "controlled", [["szónoki párbaj", "oratorical duel"], ["szerves fejlődés", "organic development"], ["érdekegyesítés", "unification of interests"], ["megfontoltság", "circumspection"]], ["c1-vitakultura-vocab"]),
                sb("grammar", "practice", ["Széchenyi", "és", "Kossuth", "vitája", "meghatározta", "a", "modern", "Magyarország", "sorsát."], ["Széchenyi", "és", "Kossuth", "vitája", "meghatározta", "a", "modern", "Magyarország", "sorsát."], "The debate between Széchenyi and Kossuth determined the destiny of modern Hungary.", ["c1-parliamentary-debate"]),
                dc("dialogue", [
                    {"speaker": "Történész", "text": "Ellenségek voltak-e valójában Széchenyi és Kossuth?"},
                    {"speaker": "Professzor", "text": "Nem; két mélységesen elkötelezett hazafi volt, akik a célban egyetértettek, de a módszerekben különböztek."},
                ], ["módszerekben különböztek", "mindent feladtak", "semmit sem csináltak"], 0, ["c1-parliamentary-debate"]),
                sw("production", [{"prompt": "Write a sentence contrasting Széchenyi's and Kossuth's approaches.", "answer": "Míg Széchenyi a gazdasági alapozás fontosságát hangsúlyozta, Kossuth a politikai szabadságjogokért harcolt."}], ["c1-parliamentary-debate"]),
                mc("grammar", "check", "Melyik állítás foglalja össze legpontosabban Széchenyi reformkori stratégiáját?", [
                    "A békés, szerves fejlődés, az intézményteremtés és az erkölcsi pallérozódás elsőbbsége.",
                    "A fegyveres felkelés azonnali kirobbantása.",
                    "A jobbágyok jogfosztottságának fenntartása."
                ], 0, ["c1-parliamentary-debate"])
            ]
        },
        {
            "num": 2,
            "stem": f"c1-{slug}-02",
            "title": "Legal Precision and Moral Force: Ferenc Deák",
            "grammar_title": "Constitutional Argumentation and Legal Eloquence",
            "grammar_skill": "c1-parliamentary-debate",
            "goals": [
                "I can analyze Ferenc Deák's masterly legal and constitutional rhetoric.",
                "I can deploy high-register jurisprudence and constitutional vocabulary.",
                "I can observe how steadfast passive resistance transforms into successful negotiation."
            ],
            "vocab": [
                {"lemma": "jogfolytonosság", "translation": "legal continuity", "pos": "noun"},
                {"lemma": "alkotmányosság", "translation": "constitutionality", "pos": "noun"},
                {"lemma": "kiegyezés", "translation": "Compromise (1867 Ausgleich)", "pos": "noun"},
                {"lemma": "haza bölcse", "translation": "Sage of the Homeland (epithet of Deák)", "pos": "noun"},
                {"lemma": "jogalap", "translation": "legal basis, ground", "pos": "noun"},
                {"lemma": "megingathatatlan", "translation": "unshakeable, steadfast", "pos": "adjective"},
                {"lemma": "törvényesség", "translation": "legality, rule of law", "pos": "noun"},
                {"lemma": "méltányosság", "translation": "equity, fairness", "pos": "noun"}
            ],
            "gr_text1": "Ferenc Deák, 'a haza bölcse' (the Sage of the Homeland), achieved the historic 1867 Compromise (*kiegyezés*) not through military arms, but through unshakeable legal argumentation (*jogfolytonosság*).",
            "gr_text2": "Constitutional rhetoric in Hungarian anchors political claims in immutable statutes and treaties: *A magyar alkotmányosságból egy jottányit sem engedhetünk, mert a jog feladása a nemzet halála.*",
            "gr_table": [
                ["A jogfolytonosság megingathatatlan elve...", "The unshakeable principle of legal continuity..."],
                ["Az alkotmányos rend helyreállítása...", "The restoration of constitutional order..."],
                ["Méltányos és tartós megegyezésre törekedve...", "Striving for an equitable and lasting agreement..."]
            ],
            "world_story_seg": {
                "seg_slug": "deak",
                "title": "Deák Ferenc és a jog ereje",
                "summary": "How the 'Sage of the Homeland' restored Hungarian constitutional sovereignty through patient, brilliant legal argumentation.",
                "paragraphs": [
                    {"type": "narration", "text": "Az 1849-es szabadságharc leverése után Magyarországra a rémuralom és az abszolutizmus sötét éjszakája borult. Ferenc József császár eltörölte a magyar alkotmányt, és az országot fegyveres erővel kormányzott tartománnyá fokozta le. Ebben a reménytelennek tűnő helyzetben lépett elő Deák Ferenc, hogy fegyverek nélkül, pusztán a jog és az erkölcs erejével vegye fel a harcot a Habsburg birodalommal."},
                    {"type": "narration", "text": "Deák a passzív ellenállás vezére lett. Nem fogadott el hivatalt, nem fizetett adót, és nem volt hajlandó tárgyalni az alkotmányellenes rezsimmel. Híres Húsvéti cikkében és felirataiban olyan acélos jogi logikával fejtette ki a magyar jogfolytonosság elvét, amelyet Bécs legkiválóbb jogászai sem tudtak megcáfolni. Tudta: a jogot erőszakkal el lehet tiporni, de önként lemondani róla megbocsáthatatlan bűn."},
                    {"type": "narration", "text": "Kitartása meghozta gyümölcsét. Amikor a birodalom katonai vereségei után a császár kénytelen volt engedni, Deák nem állt bosszút: méltányos, mindkét fél számára elfogadható kompromisszumot kötött. Az 1867-es kiegyezéssel visszaállította Magyarország önálló alkotmányos rendjét, és megnyitotta a gazdasági felemelkedés aranykorát."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Milyen alapelvre építette Deák Ferenc a tárgyalási stratégiáját Béccsel szemben?", [
                    "A magyar jogfolytonosság és az 1848-as alkotmányosság megingathatatlan elvére.",
                    "Az azonnali fegyveres háború elvére.",
                    "A birodalomhoz való feltétel nélküli csatlakozásra."
                ], 0, ["c1-vitakultura-vocab"]),
                fb("grammar", "practice", "Deák híres mondása szerint a nemzet nem adhatja fel a törvényes _____ alapját. (legal basis / jogalapját)", "jogalapját", "According to Deák's famous saying, the nation cannot surrender its lawful legal basis.", ["c1-parliamentary-debate"]),
                match("vocabulary", "controlled", [["jogfolytonosság", "legal continuity"], ["alkotmányosság", "constitutionality"], ["kiegyezés", "Compromise"], ["méltányosság", "equity / fairness"]], ["c1-vitakultura-vocab"]),
                sb("grammar", "practice", ["A", "jogot", "nem", "szabad", "feláldozni", "a", "pillanatnyi", "kényelemért."], ["A", "jogot", "nem", "szabad", "feláldozni", "a", "pillanatnyi", "kényelemért."], "The law must not be sacrificed for momentary convenience.", ["c1-parliamentary-debate"]),
                dc("dialogue", [
                    {"speaker": "Diplomata", "text": "Hogyan győzhette le egy jogász a Habsburg hadsereget?"},
                    {"speaker": "Történész", "text": "Úgy, hogy a megingathatatlan jogi érvelést párosította az erkölcsi méltósággal."},
                ], ["megingathatatlan jogi érvelést", "titkos katonai szövetséget", "pénzügyi vesztegetést"], 0, ["c1-parliamentary-debate"]),
                sw("production", [{"prompt": "Write a statement in Deák's spirit on legal continuity.", "answer": "A jog feladása a nemzet halálát jelentené, ezért a törvényességből nem engedhetünk."}], ["c1-parliamentary-debate"]),
                mc("grammar", "check", "Mi volt az 1867-es kiegyezés történelmi jelentősége?", [
                    "Visszaállította az alkotmányos rendet és megnyitotta a modern polgári fejlődés korszakát.",
                    "Magyarország elvesztette minden önrendelkezését.",
                    "Megszüntette a magyar országgyűlést."
                ], 0, ["c1-parliamentary-debate"])
            ]
        },
        {
            "num": 3,
            "stem": f"c1-{slug}-03",
            "title": "Parliamentary Obstruction and the Duel of Words",
            "grammar_title": "Parliamentary Obstruction and Procedural Oratory",
            "grammar_skill": "c1-persuasive-oratory",
            "goals": [
                "I can analyze parliamentary obstruction (*obstrukció*) in Dualist Hungary.",
                "I can evaluate procedural debate tactics, filibusters, and honor duels.",
                "I can construct elevated parliamentary motions and procedural objections."
            ],
            "vocab": [
                {"lemma": "obstrukció", "translation": "filibuster, parliamentary obstruction", "pos": "noun"},
                {"lemma": "ügyrendi", "translation": "procedural, order of business", "pos": "adjective"},
                {"lemma": "felszólalás", "translation": "speech, intervention from the floor", "pos": "noun"},
                {"lemma": "szószék", "translation": "tribune, rostrum, pulpit", "pos": "noun"},
                {"lemma": "képviselőház", "translation": "House of Representatives", "pos": "noun"},
                {"lemma": "tárgysorozat", "translation": "agenda, order of the day", "pos": "noun"},
                {"lemma": "lovagias ügy", "translation": "matter of honor, duel affair", "pos": "noun"},
                {"lemma": "jegyzőkönyv", "translation": "minutes, official record", "pos": "noun"}
            ],
            "gr_text1": "In late 19th-century Budapest, the Parliament became a theater of legendary endurance. The opposition utilized *obstrukció* (filibustering through endless procedural speeches, roll calls, and reading texts from the rostrum) to paralyze unwanted legislation.",
            "gr_text2": "Debates were fiercely oratorical; insults delivered from the floor often spilled into dawn honor duels (*lovagias ügy*). Procedural formulas (*Ügyrendi kérdésben kérek szót!*) required impeccable mastery of the rules of order.",
            "gr_table": [
                ["Ügyrendi kérdésben kérek szót, Tisztelt Elnök Úr!", "I ask for the floor on a point of order, Mr. Speaker!"],
                ["A tárgysorozat módosítását indítványozom...", "I move for the amendment of the agenda..."],
                ["A jegyzőkönyv hitelesítésének elhalasztása...", "Postponing the verification of the minutes..."]
            ],
            "world_story_seg": {
                "seg_slug": "dualizmus",
                "title": "A parlamenti csaták korszaka: Obstrukció és lovagias ügyek",
                "summary": "How the Hungarian Parliament at the turn of the century became a battlefield of epic rhetorical stamina, filibusters, and honor.",
                "paragraphs": [
                    {"type": "narration", "text": "A századforduló Budapestjén a Parlament kupolacsarnoka nemcsak a törvényhozás temploma volt, hanem a politikai gladiátorok arénája is. Tisza Kálmán, Tisza István és Apponyi Albert korában a képviselőházi ülések gyakran éjszakákon át nyúló oratorikus csatákká fajultak."},
                    {"type": "narration", "text": "Amikor az ellenzék tehetetlennek bizonyult a kormánypárti többséggel szemben, a technikai fegyverhez nyúlt: az obstrukcióhoz. A szónokok órákon, sőt napokon keresztül beszéltek a szószékről: bibliai passzusokat, mezőgazdasági statisztikákat vagy éppen receptkönyveket olvastak fel ügyrendi felszólalásként, hogy megbénítsák a szavazást. A padok recsegtek, a csengők zúgtak, és nem ritkán a verbális sértéseket másnap hajnalban kardpárbajjal intézték el a vívótermekben."},
                    {"type": "narration", "text": "Bár a kortársak sokszor botrányosnak érezték a parlamenti viharokat, e küzdelmek mégis a magyar politikai szenvedélyről és a szólásszabadság megingathatatlan tiszteletéről tanúskodtak. A szónoklat ereje itt valódi fegyver volt a nemzeti szuverenitás védelmében."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Mit jelentett a parlamenti 'obstrukció' a dualizmus korában?", [
                    "A törvényhozási munka jogszerű késleltetését vagy megbénítását végtelen beszédekkel és ügyrendi indítványokkal.",
                    "A parlamenti épület fizikai lezárását a rendőrség által.",
                    "A választások elhalasztását háború miatt."
                ], 0, ["c1-vitakultura-vocab"]),
                fb("grammar", "practice", "A képviselő azonnal _____ kérdésben kért szót a házelnöktől. (procedural / ügyrendi)", "ügyrendi", "The representative immediately asked the speaker for the floor on a procedural point.", ["c1-persuasive-oratory"]),
                match("vocabulary", "controlled", [["obstrukció", "filibuster"], ["szószék", "rostrum"], ["tárgysorozat", "agenda"], ["lovagias ügy", "matter of honor"]], ["c1-vitakultura-vocab"]),
                sb("grammar", "practice", ["A", "szónoklat", "ereje", "döntő", "fegyver", "volt", "a", "politikai", "küzdelemben."], ["A", "szónoklat", "ereje", "döntő", "fegyver", "volt", "a", "politikai", "küzdelemben."], "The power of oratory was a decisive weapon in the political struggle.", ["c1-persuasive-oratory"]),
                dc("dialogue", [
                    {"speaker": "Házelnök", "text": "Megadom a szót az ellenzék képviselőjének!"},
                    {"speaker": "Felszólaló", "text": "Tisztelt Ház! A tárgysorozat azonnali levételét indítványozom."},
                ], ["tárgysorozat azonnali levételét", "minden törvény elfogadását", "a vita azonnali bezárását"], 0, ["c1-persuasive-oratory"]),
                sw("production", [{"prompt": "Write a formal parliamentary intervention opening.", "answer": "Tisztelt Ház, Tisztelt Elnök Úr! Ügyrendi kérdésben vagyok kénytelen felszólalni."}], ["c1-persuasive-oratory"]),
                mc("grammar", "check", "Melyik kifejezés tartozik a formális parlamenti eljárásrendhez?", [
                    "A tárgysorozat módosítását indítványozom.",
                    "Hagyjuk abba az egészet most már.",
                    "Nem érdekel a jegyzőkönyv."
                ], 0, ["c1-persuasive-oratory"])
            ]
        },
        {
            "num": 4,
            "stem": f"c1-{slug}-04",
            "title": "Pamphlets and Press Polemics: The Culture of the Pamphlet",
            "grammar_title": "Pamphlet Rhetoric, Journalistic Feuds, and Satirical Sharpness",
            "grammar_skill": "c1-persuasive-oratory",
            "goals": [
                "I can analyze the historic Hungarian tradition of print polemics and pamphlets (*röpirat*).",
                "I can evaluate satirical and accusatory journalistic rhetoric.",
                "I can write a persuasive, high-impact public polemical response."
            ],
            "vocab": [
                {"lemma": "röpirat", "translation": "pamphlet, tract", "pos": "noun"},
                {"lemma": "hírlapi vita", "translation": "press polemic, newspaper debate", "pos": "noun"},
                {"lemma": "sajtószabadság", "translation": "freedom of the press", "pos": "noun"},
                {"lemma": "tollharc", "translation": "pen battle, battle of words", "pos": "noun"},
                {"lemma": "leleplező", "translation": "revelatory, exposing", "pos": "adjective"},
                {"lemma": "visszhang", "translation": "echo, public resonance", "pos": "noun"},
                {"lemma": "közvélemény", "translation": "public opinion", "pos": "noun"},
                {"lemma": "megbélyegez", "translation": "to stigmatize, brand", "pos": "verb"}
            ],
            "gr_text1": "From Bessenyei and Kazinczy's language battles to Ady's and Ignotus's literary warfare, print polemic (*tollharc*) was Hungary's primary engine of cultural renewal. The pamphlet (*röpirat*) offered rapid circulation of radical ideas outside institutional censorship.",
            "gr_text2": "Pamphlet style relies on punchy, staccato clauses, biting satire, and moral indictments designed to mobilize public opinion (*közvélemény*).",
            "gr_table": [
                ["A röpirat óriási társadalmi visszhangot váltott ki...", "The pamphlet triggered enormous public resonance..."],
                ["Hírlapi viták kereszttüzében...", "In the crossfire of newspaper polemics..."],
                ["A tollharc a szellemi megújulás záloga...", "The battle of the pen is the guarantee of intellectual renewal..."]
            ],
            "world_story_seg": {
                "seg_slug": "sajtovita",
                "title": "Hírlapi harcok és röpiratok: A toll fegyvere",
                "summary": "How uncensored pamphlets and brilliant press feuds shaped modern Hungarian political consciousness.",
                "paragraphs": [
                    {"type": "narration", "text": "Amikor 1848 márciusában a pesti ifjúság elfoglalta Landerer nyomdáját, és engedély nélkül kinyomtatta a Nemzeti dalt és a 12 pontot, a sajtószabadság nem csupán jogi cikkely lett, hanem a nemzet legféltettebb kincse. A magyar történelemben a sajtó sosem volt egyszerű hírközlő eszköz; mindig a szellemi függetlenség és a társadalmi reformok élcsapata maradt."},
                    {"type": "narration", "text": "A tizenkilencedik és huszadik század hírlapjai valóságos intellektuális csataterkekké váltak. A Pesti Hírlap, a Budapesti Szemle, majd a Nyugat hasábjain zajló 'tollharcok' formálták a közvéleményt. Egyetlen jól megírt, csípős röpirat képes volt kormányokat megingatni, irodalmi iskolákat elsöpörni és új eszmei korszakokat nyitni."},
                    {"type": "narration", "text": "A toll forgatói tudták: a leírt szónak súlya és felelőssége van. A szellemes polémia, a bátor leleplezés és az érvek tisztasága emelte a magyar hírlapírást a legmagasabb művészi és erkölcsi színvonalra."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Mi tette a röpiratot oly hatékony fegyverré a magyar történelemben?", [
                    "A gyors terjeszthetőség, a közvetlen hangvétel és a cenzúra kikerülésének képessége.",
                    "A vastag bőrkötés és az aranyozott betűk.",
                    "A kizárólag latin nyelven való megjelenés."
                ], 0, ["c1-vitakultura-vocab"]),
                fb("grammar", "practice", "A cikk megjelenése hatalmas társadalmi _____ váltott ki országszerte. (public resonance / visszhangot)", "visszhangot", "The publication of the article triggered enormous public resonance nationwide.", ["c1-persuasive-oratory"]),
                match("vocabulary", "controlled", [["röpirat", "pamphlet"], ["tollharc", "battle of words"], ["közvélemény", "public opinion"], ["leleplező", "revelatory"]], ["c1-vitakultura-vocab"]),
                sb("grammar", "practice", ["A", "sajtó", "a", "szellemi", "szabadság", "legfontosabb", "védőbástyája", "maradt."], ["A", "sajtó", "a", "szellemi", "szabadság", "legfontosabb", "védőbástyája", "maradt."], "The press remained the most important bastion of intellectual freedom.", ["c1-persuasive-oratory"]),
                dc("dialogue", [
                    {"speaker": "Szerkesztő", "text": "Nem túl éles ez a válaszcikk a vitapartnerünkkel szemben?"},
                    {"speaker": "Publicista", "text": "Egy tollharcban a határozott kiállás és az igazság kimondása a legfőbb kötelességünk."},
                ], ["határozott kiállás", "meghunyászkodás", "téma elhallgatása"], 0, ["c1-persuasive-oratory"]),
                sw("production", [{"prompt": "Write a polemical opening of a public pamphlet.", "answer": "Itt az idő, hogy a hallgatás falait áttörve nyíltan szembenézzünk a tényekkel!"}], ["c1-persuasive-oratory"]),
                mc("grammar", "check", "Melyik állítás jellemzi a klasszikus magyar tollharcok hagyományát?", [
                    "A szellemes érvelés, a nyelvi gazdagság és a társadalmi felelősségvállalás egysége.",
                    "A névtelen és gyáva személyeskedés.",
                    "A hivatalos kormánynyilatkozatok szolgalelkű másolása."
                ], 0, ["c1-persuasive-oratory"])
            ]
        },
        {
            "num": 5,
            "stem": f"c1-{slug}-05",
            "title": "Public Debate in the Digital Era: Polarization and Algorithms",
            "grammar_title": "Contemporary Media Discourse, Echo Chambers, and Deliberative Democracy",
            "grammar_skill": "c1-parliamentary-debate",
            "goals": [
                "I can analyze how algorithms and social media transform public discourse.",
                "I can evaluate echo chambers (*véleménybuborék*), polarization, and misinformation in Hungarian.",
                "I can debate the conditions for genuine deliberative democracy in the 21st century."
            ],
            "vocab": [
                {"lemma": "polarizáció", "translation": "polarization", "pos": "noun"},
                {"lemma": "véleménybuborék", "translation": "echo chamber, opinion bubble", "pos": "noun"},
                {"lemma": "álhír", "translation": "fake news, misinformation", "pos": "noun"},
                {"lemma": "deliberatív demokrácia", "translation": "deliberative democracy", "pos": "noun"},
                {"lemma": "közösségi média", "translation": "social media", "pos": "noun"},
                {"lemma": "törzsi gondolkodás", "translation": "tribal thinking", "pos": "noun"},
                {"lemma": "társadalmi párbeszéd", "translation": "social dialogue", "pos": "noun"},
                {"lemma": "érvelési kultúra", "translation": "culture of argumentation / debate", "pos": "noun"}
            ],
            "gr_text1": "The digital transition has revolutionized and fragmented the public sphere. Algorithms optimize for emotional outrage, accelerating *polarizáció* and locking citizens into hermetic *véleménybuborékok* (echo chambers).",
            "gr_text2": "Restoring *deliberatív demokrácia* requires reviving *az érvelési kultúra* (the culture of argumentation): replacing clickbait slogans with rational deliberation, evidence-based claims, and mutual listening.",
            "gr_table": [
                ["A digitális polarizáció és a véleménybuborékok veszélye...", "The danger of digital polarization and echo chambers..."],
                ["Az érdemi társadalmi párbeszéd helyreállítása...", "Restoring meaningful social dialogue..."],
                ["A demokratikus deliberáció alapvető feltételei...", "The fundamental conditions of democratic deliberation..."]
            ],
            "world_story_seg": {
                "seg_slug": "media",
                "title": "A vita jövője a digitális térben: Algoritmusok és párbeszéd",
                "summary": "How the digital sphere challenges democratic debate culture and why deliberate civil dialogue is more vital than ever.",
                "paragraphs": [
                    {"type": "narration", "text": "A huszonegyedik században a nyilvános vita színtere átköltözött a parlamentekből és kávéházakból a digitális hálózatok végtelen terébe. A közösségi média kezdetben a véleményszabadság és a demokratikus részvétel példátlan kitágulását ígérte. Ma azonban egyre nyilvánvalóbbá válik ennek az ígéretnek az árnyoldala is."},
                    {"type": "narration", "text": "Az algoritmusok logikája nem az igazság keresésére és a higgadt megértésre van kalibrálva, hanem az indulatok felkorbácsolására és a figyelem maximalizálására. A polgárok szeparált 'véleménybuborékokba' záródnak, ahol csak a saját előítéleteik visszhangját hallják. A klasszikus érvelési kultúrát felváltotta a virtuális törzsi háborúskodás és az azonnali megbélyegzés reflexe."},
                    {"type": "narration", "text": "Mégsem mondhatunk le a párbeszédről. A demokrácia lényege éppen az, hogy képesek vagyunk meghallgatni és tiszteletben tartani azt, akivel nem értünk egyet. A magyar vitakultúra legnemesebb reformkori hagyományait újra felfedezve meg kell tanulnunk: az igazi erő nem az algoritmusok által generált zajban van, hanem a felelős, érvelő emberi szó erejében."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Milyen veszélyt jelentenek a 'véleménybuborékok' a társadalmi vitára?", [
                    "Elszigetelik a polgárokat, meggátolják a valódi párbeszédet és felerősítik a polarizációt.",
                    "Túl sok tudományos cikket mutatnak.",
                    "Lassítják az internet sebességét."
                ], 0, ["c1-vitakultura-vocab"]),
                fb("grammar", "practice", "A demokratikus jövő kulcsa az érdemi és felelős társadalmi _____ helyreállítása. (dialogue / párbeszéd)", "párbeszéd", "The key to a democratic future is the restoration of meaningful and responsible social dialogue.", ["c1-parliamentary-debate"]),
                match("vocabulary", "controlled", [["polarizáció", "polarization"], ["véleménybuborék", "echo chamber"], ["társadalmi párbeszéd", "social dialogue"], ["érvelési kultúra", "culture of argumentation"]], ["c1-vitakultura-vocab"]),
                sb("grammar", "practice", ["A", "demokrácia", "lényege", "a", "kölcsönös", "tiszteleten", "alapuló", "párbeszéd."], ["A", "demokrácia", "lényege", "a", "kölcsönös", "tiszteleten", "alapuló", "párbeszéd."], "The essence of democracy is dialogue based on mutual respect.", ["c1-parliamentary-debate"]),
                dc("dialogue", [
                    {"speaker": "Elemző", "text": "Hogyan lehet kikerülni a digitális véleménybuborékokból?"},
                    {"speaker": "Szociológus", "text": "Tudatos médiatudatossággal és a vitapartnerek tiszteletben tartásával."},
                ], ["tudatos médiatudatossággal", "az internet kikapcsolásával", "a bírálók letiltásával"], 0, ["c1-parliamentary-debate"]),
                sw("production", [{"prompt": "Write a critical thought on algorithmic polarization.", "answer": "Az algoritmusok által vezérelt polarizáció megbénítja a közös megoldások keresését."}], ["c1-parliamentary-debate"]),
                mc("grammar", "check", "Mi szükséges a deliberatív demokrácia működéséhez a digitális korban?", [
                    "A racionális érvelés, a forráskritika és a nyitott társadalmi párbeszéd.",
                    "A politikai ellenfelek teljes elnémítása.",
                    "Minden vita betiltása a közösségi médiában."
                ], 0, ["c1-parliamentary-debate"])
            ]
        }
    ]

    for l in disc_lessons:
        emit_instructional_lesson(4, "discourse", l, disc_title, disc_intro if l["num"] == 1 else None)

    # Full World Compilation Story
    write_json(
        f"stories/world/c1/{slug}.json",
        {
            "id": f"story.c1.world.{slug}",
            "title": "A szónoklat ereje: A reformkori vitáktól a parlamentáris párbajokig",
            "level": "C1",
            "type": "world",
            "summary": "Epic chronicle of the Hungarian culture of public debate: from Széchenyi and Kossuth's reform duel and Deák's legal triumph to dualist filibusters, fearless print polemics, and digital age deliberation.",
            "paragraphs": [
                {"type": "narration", "text": "A magyar szabadság és a modern nemzet nem a csendes megegyezésekben, hanem a szikrázó szónoki viták tüzében született meg. A reformkori országgyűlésen Széchenyi István szerves gazdasági látomása és Kossuth Lajos népi érdekegyesítő lángelméje csapott össze, hogy kijelölje a polgári átalakulás két útját."},
                {"type": "narration", "text": "A szabadságharc leverése után Deák Ferenc bizonyította be a világnak, hogy a jog ereje képes legyőzni az abszolutista erőszakot. Megingathatatlan jogfolytonossági érvelésével kényszerítette Bécset a kiegyezésre, megteremtve a modern parlamentarizmus alapjait."},
                {"type": "narration", "text": "A századfordulón a képviselőház a szónoki kitartás és az obstrukció arénájává vált, miközben a független sajtó röpiratai és hírlapi tollharcai formálták a nemzeti öntudatot. A szónoklat nem dísz volt, hanem politikai és morális fegyver."},
                {"type": "narration", "text": "A huszonegyedik század digitális forradalma új kihívások elé állítja ezt az örökséget. A véleménybuborékok és az algoritmusok által szított polarizáció korában újra meg kell tanulnunk a vitakultúra legnemesebb szabályait: az érv erejét a hangerővel szemben, és az ellenfél emberi méltóságának tiszteletét."},
                {"type": "narration", "text": "A magyar vitakultúra történelme azt üzeni: a nemzet életereje mindig abban mutatkozik meg, hogy polgárai képesek-e szabadon, bátran és felelősséggel megvitatni a közös jövő nagy sorskérdéseit."}
            ]
        }
    )

    # Discourse Consolidation
    emit_consolidation_lesson(
        4,
        "discourse",
        f"c1-{slug}-consolidation",
        disc_title,
        [
            "I can compare the debate styles of Széchenyi, Kossuth, and Deák.",
            "I can explain historical debate phenomena such as parliamentary obstruction and print polemics.",
            "I can deploy high-register political, rhetorical, and constitutional vocabulary."
        ],
        [
            mc("grammar", "recognize", "Melyik politikai eszméhez kötődik Kossuth Lajos neve a reformkorban?", [
                "Az érdekegyesítéshez és a jobbágyfelszabadításhoz.",
                "A bécsi abszolutizmus fenntartásához.",
                "A parlamentarizmus eltörléséhez."
            ], 0, ["c1-parliamentary-debate"]),
            mc("grammar", "recognize", "Milyen módszerrel érte el Deák Ferenc az 1867-es kiegyezést?", [
                "A jogfolytonosság megingathatatlan elméletével és a békés passzív ellenállással.",
                "Külföldi hadseregek behívásával.",
                "A magyar nyelvhasználat feladásával."
            ], 0, ["c1-parliamentary-debate"]),
            match("vocabulary", "recognize", [["szónoki párbaj", "oratorical duel"], ["jogfolytonosság", "legal continuity"], ["obstrukció", "filibuster"], ["röpirat", "pamphlet"], ["deliberatív demokrácia", "deliberative democracy"]], ["c1-vitakultura-vocab"]),
            fb("vocabulary", "recall", "A pozsonyi országgyűlés a magyar politikai szónoklat klasszikus _____ vált. (arena / arénájává)", "arénájává", "The Diet of Pozsony became the classic arena of Hungarian political oratory.", ["c1-vitakultura-vocab"]),
            fb("vocabulary", "recall", "Deák Ferenc a magyar alkotmányos _____ helyreállításáért küzdött. (order / rend)", "rend", "Ferenc Deák fought for the restoration of Hungarian constitutional order.", ["c1-vitakultura-vocab"]),
            fb("grammar", "recall", "A képviselő a házszabály alapján _____ kérdésben kért szót. (procedural / ügyrendi)", "ügyrendi", "The representative asked for the floor on a procedural point based on the house rules.", ["c1-persuasive-oratory"]),
            fb("grammar", "context", "A cikk megjelenése hatalmas vitát robbantott ki a hazai _____ körében. (public opinion / közvélemény)", "közvélemény", "The publication of the article ignited an enormous debate within domestic public opinion.", ["c1-persuasive-oratory"]),
            fb("grammar", "context", "A közösségi média algoritmusai veszélyes mértékben erősítik a politikai _____ folyamatát. (polarization / polarizáció)", "polarizáció", "Social media algorithms dangerously reinforce the process of political polarization.", ["c1-parliamentary-debate"]),
            mc("grammar", "context", "Mi a legfőbb tanulsága a reformkori vitáknak a ma embere számára?", [
                "Hogy a nemzet felemelkedése a bátor, felelősségteljes és kölcsönösen tiszteletteljes vitákon alapul.",
                "Hogy a politikusoknak sosem szabad beszélniük.",
                "Hogy csak a külföldi tanácsokra szabad hallgatni."
            ], 0, ["c1-parliamentary-debate"]),
            sb("grammar", "produce", ["A", "szabad", "érvelés", "és", "vita", "a", "demokratikus", "közélet", "alapköve."], ["A", "szabad", "érvelés", "és", "vita", "a", "demokratikus", "közélet", "alapköve."], "Free argumentation and debate are the cornerstone of democratic public life.", ["c1-parliamentary-debate"]),
            sw("production", [{"prompt": "Write an evaluation comparing Széchenyi's and Deák's contributions to Hungarian debate.", "answer": "Míg Széchenyi a reformok gazdasági alapjait vetette meg, Deák a jogállamiság megingathatatlan védelmezője volt."}], ["c1-parliamentary-debate"]),
            sw("production", [{"prompt": "Formulate a concluding thought on debate culture.", "answer": "A vitakultúra minősége pontosan jelzi egy társadalom szellemi szabadságát és érettségét."}], ["c1-parliamentary-debate"])
        ]
    )
    print("=== Finished C1 Unit 4 ===")


if __name__ == "__main__":
    generate_unit_4()
