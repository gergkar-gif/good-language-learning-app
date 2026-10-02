#!/usr/bin/env python3
"""
Hungarian C1 Block 1 - Unit 05 Generator:
  - Track 1 (Core): Unit 5 — "Irony, Understatement & Sarcastic Register Shifting" (c1-05)
  - Track 2 (Discourse): Unit 5 — "Urban Satire as Political Defense" (c1-pesti-ironia)
"""

from .common import mc, match, fb, sb, dc, sw, write_json, emit_instructional_lesson, emit_consolidation_lesson


def generate_unit_5():
    print("=== Generating C1 Unit 5 ===")
    
    # ----------------------------------------------------
    # TRACK 1: CORE (c1-05)
    # ----------------------------------------------------
    core_title = "Irony, Understatement & Sarcastic Register Shifting"
    core_intro = [
        "In Central European culture, irony is not a trivial joke; it is a philosophy of existence and an intellectual armor against absurdity, tyranny, and catastrophe.",
        "In this unit, inspired by István Örkény's legendary grotesque prose in 'Gondolatok a pincében', you will master nuanced pragmatic particles of irony (ugyebár, elvégre, mégiscsak, netalán), rhetorical litotes, understatement, and the art of sarcastic register shifting."
    ]

    core_lessons = [
        {
            "num": 1,
            "stem": "c1-05-01",
            "title": "Nuanced Pragmatic Particles of Irony",
            "grammar_title": "Pragmatic Particles in Subversive Irony: Ugyebár, Elvégre, and Netalán",
            "grammar_skill": "c1-ironic-particles",
            "goals": [
                "I can deploy pragmatic particles (*ugyebár, elvégre, mégiscsak, netalán, éppenséggel*) to convey ironic subtext.",
                "I can distinguish between literal meaning and subtle conversational mockery in Hungarian.",
                "I can decode implied social criticism masked as polite agreement."
            ],
            "vocab": [
                {"lemma": "ugyebár", "translation": "is it not so?, mind you (ironic tag)", "pos": "adverb"},
                {"lemma": "elvégre", "translation": "after all, when all is said and done", "pos": "adverb"},
                {"lemma": "mégiscsak", "translation": "after all, nevertheless, surely", "pos": "adverb"},
                {"lemma": "netalán", "translation": "perchance, by any chance (ironic query)", "pos": "adverb"},
                {"lemma": "éppenséggel", "translation": "as a matter of fact, actually (concessive)", "pos": "adverb"},
                {"lemma": "élcelődés", "translation": "banter, gentle mocking", "pos": "noun"},
                {"lemma": "kétértelműség", "translation": "ambiguity, double entendre", "pos": "noun"},
                {"lemma": "gúny", "translation": "scorn, mockery, sarcasm", "pos": "noun"}
            ],
            "gr_text1": "Hungarian conversational and literary irony relies heavily on modal particles. *Ugyebár* invites complicity while secretly questioning the assertion: *A miniszter úr, ugyebár, tévedhetetlen.* (The Minister, mind you, is infallible).",
            "gr_text2": "*Elvégre* (after all) often rationalizes an absurd situation with fake fatalism, while *netalán* feigns polite innocence to suggest a scandalous possibility: *Netalán azt tetszik állítani, hogy a pénz eltűnt?*",
            "gr_table": [
                ["A szabályokat, ugyebár, mindenkinek be kell tartania.", "Rules, mind you, must be observed by everyone. (ironic)"],
                ["Elvégre nem történhetett semmi baj...", "After all, nothing bad could have happened... (feigned innocence)"],
                ["Netalán kételkedni mer a hivatalos verzióban?", "Perchance you dare doubt the official version?"]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Milyen szerepet tölt be az 'ugyebár' szó az ironikus megnyilatkozásban?", ["Ál-egyetértést színlel, miközben gúnyosan megkérdőjelezi az állítást.", "Kizárólag pontos matematikai mérést jelöl.", "Egyszerű időbeli jövő időt fejez ki."], 0, ["c1-05-vocab"]),
                fb("grammar", "controlled", "A hivatalnokok, _____ mindent a legnagyobb rendben találtak a vizsgálat során. (mind you / ugyebár)", "ugyebár", "The bureaucrats, mind you, found everything in the greatest order during the audit.", ["c1-ironic-particles"]),
                match("vocabulary", "controlled", [["ugyebár", "mind you / is it not so?"], ["elvégre", "after all"], ["netalán", "perchance"], ["kétértelműség", "double entendre"]], ["c1-05-vocab"]),
                fb("grammar", "practice", "_____ azt akarja elhitetni velünk, hogy a döntésről senki sem tudott? (Perchance / Netalán)", "Netalán", "Perchance you want to make us believe that no one knew about the decision?", ["c1-ironic-particles"]),
                sb("grammar", "practice", ["Elvégre", "a", "tévedhetetlenség", "a", "hatalom", "legfőbb", "kiváltsága."], ["Elvégre", "a", "tévedhetetlenség", "a", "hatalom", "legfőbb", "kiváltsága."], "After all, infallibility is the chief privilege of power.", ["c1-ironic-particles"]),
                dc("dialogue", [
                    {"speaker": "Főnök", "text": "Remélem, mindenki elégedett a túlórák elszámolásával?"},
                    {"speaker": "Alkalmazott", "text": "Hogyne, elvégre a meleg kézfogás a legszebb fizetség."},
                ], ["elvégre a meleg kézfogás", "nagyon sok a pénz", "azonnal távozunk"], 0, ["c1-ironic-particles"]),
                sw("production", [{"prompt": "Write an ironic comment using 'ugyebár' to mock an obvious bureaucratic failure.", "answer": "A jelentés, ugyebár, hibátlan, csak éppen a valósághoz nincs semmi köze."}], ["c1-ironic-particles"]),
                mc("grammar", "check", "Melyik mondat hordoz egyértelmű ironikus altextust?", [
                    "A szakértők, ugyebár, mindig mindent jobban tudnak nálunk.",
                    "A vonat pontosan 14:30-kor futott be az állomásra.",
                    "Kérem, adja át a sót az asztalon."
                ], 0, ["c1-ironic-particles"])
            ]
        },
        {
            "num": 2,
            "stem": "c1-05-02",
            "title": "Rhetorical Understatement and Litotes",
            "grammar_title": "Understatement, Antiphrasis, and Litotes in Satirical Registers",
            "grammar_skill": "c1-antiphrasis-understatement",
            "goals": [
                "I can employ rhetorical understatement (*litotes*) using negative antonyms (*nem éppen a legbölcsebb*).",
                "I can master antiphrasis (saying the opposite of what is meant with sarcastic inflection).",
                "I can soften brutal critiques through understated polite irony in Hungarian."
            ],
            "vocab": [
                {"lemma": "litotész", "translation": "litotes, rhetorical understatement", "pos": "noun"},
                {"lemma": "antifrázis", "translation": "antiphrasis (ironic inversion)", "pos": "noun"},
                {"lemma": "aligha nevezhető", "translation": "can hardly be called", "pos": "expression"},
                {"lemma": "nem éppen", "translation": "not exactly, hardly", "pos": "adverb"},
                {"lemma": "enyhén szólva", "translation": "to put it mildly", "pos": "expression"},
                {"lemma": "kínos", "translation": "awkward, embarrassing", "pos": "adjective"},
                {"lemma": "szerény", "translation": "modest, humble", "pos": "adjective"},
                {"lemma": "visszafogottság", "translation": "restraint, understatement", "pos": "noun"}
            ],
            "gr_text1": "Understatement (*visszafogottság*) is often far more devastating than open insult. In litotes, an affirmative idea is expressed by negating its opposite: *nem éppen a legbölcsebb döntés* (not exactly the wisest decision = an utter disaster), *aligha nevezhető diadalnak* (can hardly be called a triumph).",
            "gr_text2": "The idiom *enyhén szólva* (to put it mildly) acts as a satirical disclaimer before an outrageous understatement.",
            "gr_table": [
                ["Enyhén szólva nem volt a helyzet magaslatán.", "To put it mildly, he wasn't equal to the occasion."],
                ["Aligha nevezhető a diplomácia csúcsának.", "It can hardly be called the pinnacle of diplomacy."],
                ["Nem éppen fényes eredménnyel zárult a kísérlet.", "The experiment concluded with not exactly brilliant results."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mit jelent a litotész stilisztikai alakzata?", ["Egy állítás kifejezését az ellenkezője tagadása révén (pl. 'nem éppen okos' = buta).", "Egy szó tízszeres megismétlését.", "A hangok rímelését."], 0, ["c1-05-vocab"]),
                fb("grammar", "controlled", "A politikus felszólalása, enyhén _____, nem aratott osztatlan sikert. (to put it mildly / szólva)", "szólva", "The politician's speech, to put it mildly, did not reap undivided success.", ["c1-antiphrasis-understatement"]),
                match("vocabulary", "controlled", [["litotész", "understatement"], ["enyhén szólva", "to put it mildly"], ["aligha nevezhető", "can hardly be called"], ["nem éppen", "not exactly"]], ["c1-05-vocab"]),
                fb("grammar", "practice", "A tárgyalások kimenetele aligha _____ áttörésnek. (can be called / nevezhető)", "nevezhető", "The outcome of the negotiations can hardly be called a breakthrough.", ["c1-antiphrasis-understatement"]),
                sb("grammar", "practice", ["A", "stratégia,", "enyhén", "szólva,", "nem", "váltotta", "be", "a", "hozzáfűzött", "reményeket."], ["A", "stratégia,", "enyhén", "szólva,", "nem", "váltotta", "be", "a", "hozzáfűzött", "reményeket."], "The strategy, to put it mildly, did not fulfill the hopes pinned to it.", ["c1-antiphrasis-understatement"]),
                dc("dialogue", [
                    {"speaker": "Kritikus", "text": "Hogy tetszett a bemutatott új mű?"},
                    {"speaker": "Szerkesztő", "text": "Nos, nem éppen a világirodalom csúcsteljesítménye, enyhén szólva."},
                ], ["nem éppen a világirodalom csúcsteljesítménye", "a legszebb dolog a világon", "minden díjat megérdemel"], 0, ["c1-antiphrasis-understatement"]),
                sw("production", [{"prompt": "Write an understated critique of a poorly organized event using 'aligha nevezhető'.", "answer": "A rendezvény lebonyolítása aligha nevezhető a professzionalizmus mintapéldájának."}], ["c1-antiphrasis-understatement"]),
                mc("grammar", "check", "Melyik megfogalmazás alkalmaz finom litotészt a nyílt bírálat helyett?", [
                    "A lépés, enyhén szólva, nem bizonyult a legelőrelátóbbnak.",
                    "Ez a világ legnagyobb ostobasága volt!",
                    "Semmit sem értek az egészből."
                ], 0, ["c1-antiphrasis-understatement"])
            ]
        },
        {
            "num": 3,
            "stem": "c1-05-03",
            "title": "Subtle Disclaimers and Ironic Qualification",
            "grammar_title": "Polite Disclaimers, Feigned Modesty, and Ironic Qualification",
            "grammar_skill": "c1-subtle-disclaimer",
            "goals": [
                "I can use polite disclaimers to introduce sharp critical dissents.",
                "I can employ phrases like 'minden tiszteletem mellett', 'ha szabad így fogalmaznom'.",
                "I can dismantle authority figures with exquisite aristocratic courtesy."
            ],
            "vocab": [
                {"lemma": "minden tiszteletem mellett", "translation": "with all due respect", "pos": "expression"},
                {"lemma": "ha szabad így fogalmaznom", "translation": "if I may put it this way", "pos": "expression"},
                {"lemma": "udvariasság", "translation": "politeness, courtesy", "pos": "noun"},
                {"lemma": "ál-szerénység", "translation": "feigned modesty", "pos": "noun"},
                {"lemma": "fennkölt", "translation": "sublime, lofty, elevated", "pos": "adjective"},
                {"lemma": "ellentmondás", "translation": "contradiction, dissent", "pos": "noun"},
                {"lemma": "finomkodás", "translation": "affectation, prudery, mincing words", "pos": "noun"},
                {"lemma": "megsemmisítő", "translation": "devastating, crushing", "pos": "adjective"}
            ],
            "gr_text1": "In Hungarian intellectual disputes, the sharpest blades are wrapped in velvet. Prefacing a devastating refutation with *minden tiszteletem mellett* (with all due respect) or *bátorkodom megjegyezni* (I venture to remark) heightens the sarcastic bite while preserving formal decorum.",
            "gr_text2": "Phrases like *ha szabad egy szerény megjegyzést tennem* (if I may make a humble observation) deploy feigned modesty (*ál-szerénység*) to expose an opponent's ignorance.",
            "gr_table": [
                ["Minden tiszteletem mellett megkockáztatom, hogy a professzor téved.", "With all due respect I venture to say the professor is mistaken."],
                ["Ha szabad így fogalmaznom, az elmélet kissé elrugaszkodott a valóságtól.", "If I may put it this way, the theory has drifted somewhat from reality."],
                ["Bátorkodom megjegyezni, hogy az adatok hiányosak.", "I venture to note that the data are deficient."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Milyen funkciót tölt be a 'minden tiszteletem mellett' formula a szellemi vitában?", ["Udvarias keretet ad egy éles, elutasító bírálat megfogalmazásának.", "A teljes behódolást jelzi.", "A vita feladását jelenti."], 0, ["c1-05-vocab"]),
                fb("grammar", "controlled", "Minden _____ mellett meg kell állapítanom, hogy a javaslat kivitelezhetetlen. (respect / tiszteletem)", "tiszteletem", "With all due respect I must establish that the proposal is unfeasible.", ["c1-subtle-disclaimer"]),
                match("vocabulary", "controlled", [["minden tiszteletem mellett", "with all due respect"], ["ha szabad így fogalmaznom", "if I may put it this way"], ["ál-szerénység", "feigned modesty"], ["fennkölt", "lofty / sublime"]], ["c1-05-vocab"]),
                fb("grammar", "practice", "Ha szabad így _____, a szerző kissé összekeverte a kívánságait a valósággal. (to put it / fogalmaznom)", "fogalmaznom", "If I may put it this way, the author somewhat confused his wishes with reality.", ["c1-subtle-disclaimer"]),
                sb("grammar", "practice", ["Bátorkodom", "megjegyezni,", "hogy", "a", "számításokból", "hiányzik", "a", "fedezet."], ["Bátorkodom", "megjegyezni,", "hogy", "a", "számításokból", "hiányzik", "a", "fedezet."], "I venture to remark that the calculations lack financial backing.", ["c1-subtle-disclaimer"]),
                dc("dialogue", [
                    {"speaker": "Előadó", "text": "Gondolom, senkinek sincs ellenvetése a koncepcióval szemben?"},
                    {"speaker": "Bíráló", "text": "Minden tiszteletem mellett bátorkodom jelezni, hogy a premisszák hibásak."},
                ], ["bátorkodom jelezni", "egy szót se szólok", "minden csodálatos"], 0, ["c1-subtle-disclaimer"]),
                sw("production", [{"prompt": "Write a polite scholarly disagreement using 'Minden tiszteletem mellett megkockáztatom...'.", "answer": "Minden tiszteletem mellett megkockáztatom, hogy a hipotézis alapos felülvizsgálatra szorul."}], ["c1-subtle-disclaimer"]),
                mc("grammar", "check", "Melyik fordulat képvisel elegáns, de határozott szellemi ellenkezést?", [
                    "Ha szabad így fogalmaznom, az érvelés inkább vágyvezérelt, mintsem megalapozott.",
                    "Ön teljesen hülyeségeket beszél itt nekünk.",
                    "Nem mondok semmit, mert félek."
                ], 0, ["c1-subtle-disclaimer"])
            ]
        },
        {
            "num": 4,
            "stem": "c1-05-04",
            "title": "Register Clashes and Satirical Inflation",
            "grammar_title": "Parodic Register Clash and Linguistic Inflation",
            "grammar_skill": "c1-ironic-particles",
            "goals": [
                "I can engineer deliberate clashes between elevated and vulgar registers for satirical effect.",
                "I can mock bureaucratic jargon through hyperbolic parody in Hungarian.",
                "I can recognize how official euphemisms conceal incompetence."
            ],
            "vocab": [
                {"lemma": "stílustörés", "translation": "register clash, stylistic break", "pos": "noun"},
                {"lemma": "eufemizmus", "translation": "euphemism", "pos": "noun"},
                {"lemma": "túltengés", "translation": "hypertrophy, excess, overgrowth", "pos": "noun"},
                {"lemma": "dagályos", "translation": "turgid, bombastic, inflated", "pos": "adjective"},
                {"lemma": "kisszerű", "translation": "petty, small-minded", "pos": "adjective"},
                {"lemma": "paródia", "translation": "parody", "pos": "noun"},
                {"lemma": "bürokrata bikkfanyelv", "translation": "wooden bureaucratic jargon", "pos": "noun"},
                {"lemma": "lelepleződés", "translation": "exposure, unmasking", "pos": "noun"}
            ],
            "gr_text1": "Satire thrives on stylistic contrast (*stílustörés*). Placing bombastic, high-flown jargon (*bürokrata bikkfanyelv, dagályos stílus*) alongside mundane, petty reality instantly deflates pretensions.",
            "gr_text2": "Writers mimic official euphemisms to highlight the absurdity of institutional denial: *A gazdaság nem zuhan, csupán negatív növekedési pályára állt át.*",
            "gr_table": [
                ["Fennkölt szavak mögé rejtett kisszerűség...", "Petty-mindedness concealed behind sublime words..."],
                ["A hivatali bikkfanyelv paródiája...", "The parody of bureaucratic wooden language..."],
                ["A stílustörés mint komikus fegyver...", "The stylistic clash as a comical weapon..."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mi az a 'bürokrata bikkfanyelv' a magyar nyelvhasználatban?", ["A bonyolult, élettelen, eufemizmusokkal teli hivatali szakzsargon.", "A népmesékben szereplő fák neve.", "Egy finnugor tájszólás."], 0, ["c1-05-vocab"]),
                fb("grammar", "controlled", "A jelentés dagályos stílusa nem tudta elfedni a valóság _____ kisszerűségét. (petty / lehangoló)", "lehangoló", "The turgid style of the report could not conceal the depressing pettiness of reality.", ["c1-ironic-particles"]),
                match("vocabulary", "controlled", [["stílustörés", "register clash"], ["eufemizmus", "euphemism"], ["dagályos", "turgid / bombastic"], ["kisszerű", "petty"]], ["c1-05-vocab"]),
                fb("grammar", "practice", "A vezetés a katasztrofális visszaesést pimasz módon 'negatív növekedésnek' _____. (euphemized / titulálta)", "titulálta", "The leadership insolently titled the catastrophic decline 'negative growth'.", ["c1-ironic-particles"]),
                sb("grammar", "practice", ["A", "fennkölt", "szólamok", "mögött", "csak", "üres", "érdekek", "húzódtak."], ["A", "fennkölt", "szólamok", "mögött", "csak", "üres", "érdekek", "húzódtak."], "Behind the lofty slogans lay only empty interests.", ["c1-ironic-particles"]),
                dc("dialogue", [
                    {"speaker": "Hivatalnok", "text": "Az optimalizált átcsoportosítási folyamat folyamatban van."},
                    {"speaker": "Polgár", "text": "Magyarul: elfogyott a pénz, és nem tudnak mit csinálni."},
                ], ["elfogyott a pénz", "minden tökéletes", "nagyon örülünk"], 0, ["c1-ironic-particles"]),
                sw("production", [{"prompt": "Write a satirical translation of a bureaucratic excuse into plain Hungarian.", "answer": "A 'stratégiai átütemezés' a gyakorlatban azt jelenti, hogy a projekt teljesen leállt."}], ["c1-ironic-particles"]),
                mc("grammar", "check", "Melyik mondat alkalmaz szándékos stílustörést a nevetségessé tétel céljából?", [
                    "A globális geopolitikai kihívások csúcsértekezletén végül összevesztek a pogácsán.",
                    "A kormányküldöttség megérkezett a repülőtérre.",
                    "A felek aláírták a nemzetközi szerződést."
                ], 0, ["c1-ironic-particles"])
            ]
        },
        {
            "num": 5,
            "stem": "c1-05-05",
            "title": "The Central European Grotesque: István Örkény",
            "grammar_title": "The Grotesque Miniature and Black Humor as Survival",
            "grammar_skill": "c1-antiphrasis-understatement",
            "goals": [
                "I can analyze István Örkény's grotesque world in 'Gondolatok a pincében' and 'Egyperces novellák'.",
                "I can evaluate black humor, absurdity, and historical trauma processing in Hungarian prose.",
                "I can write concise, ironical grotesque commentaries."
            ],
            "vocab": [
                {"lemma": "groteszk", "translation": "grotesque", "pos": "noun"},
                {"lemma": "egyperces", "translation": "one-minute short story", "pos": "noun"},
                {"lemma": "abszurditás", "translation": "absurdity", "pos": "noun"},
                {"lemma": "túlélési stratégia", "translation": "survival strategy", "pos": "noun"},
                {"lemma": "fekete humor", "translation": "black humor, dark comedy", "pos": "noun"},
                {"lemma": "kiszolgáltatottság", "translation": "vulnerability, helplessness", "pos": "noun"},
                {"lemma": "hátborzongató", "translation": "chilling, spine-tingling, uncanny", "pos": "adjective"},
                {"lemma": "viszonylagosság", "translation": "relativity, contingency", "pos": "noun"}
            ],
            "gr_text1": "István Örkény created the Hungarian 'grotesque' through his *Egyperces novellák* (One-Minute Stories). Born out of the horrors of the Voronezh front and the siege of Budapest, his grotesque looks at absurdity with calm, deadpan sobriety (*hűvös tárgyilagosság*).",
            "gr_text2": "In Örkény's formula, the grotesque occurs when two irreconcilable realities collide: a matter-of-fact bureaucratic tone applied to existential horror or death.",
            "gr_table": [
                ["A groteszk mint közép-európai túlélési stratégia...", "The grotesque as a Central European survival strategy..."],
                ["Hátborzongató abszurditás és fekete humor...", "Chilling absurdity and black humor..."],
                ["Az emberi kiszolgáltatottság tükre...", "The mirror of human vulnerability..."]
            ],
            "classic_story": {
                "slug": "c1-05-orkeny",
                "author": "Örkény István",
                "work": "Gondolatok a pincében (1968)",
                "title": "A groteszk és a túlélés művészete",
                "summary": "István Örkény reflections on wartime, bomb shelters, and the grotesque as the ultimate intellectual armor of Central European existence.",
                "characters": ["Örkény István"],
                "paragraphs": [
                    {"type": "narration", "text": "Amikor 1944 telén Budapest felett bombák záporoztak, és a fél város a pincék dohos, sötét mélyére szorult, Örkény István ott ült a leplek és befőttesüvegek között, és figyelt. Nem kétségbeesett panaszokat jegyzett fel, hanem az emberi lélek legkülönösebb rezdüléseit. Azt figyelte, hogyan válik a tragédia groteszkké, és hogyan menti meg a józan észt a nevetés ott, ahol a józan észnek már semmi keresnivalója nem maradt."},
                    {"type": "narration", "text": "Örkény számára a groteszk nem esztétikai játék volt, hanem Közép-Európa egyetlen érvényes diagnózisa. Ebben a térségben a történelem túl sűrű, a hatalom túl abszurd, és az ember túl kiszolgáltatott ahhoz, hogy a klasszikus tragédia pátoszával lehessen leírni. Amikor a valóság maga válik elmebajjá, csak az marad normális, aki képes meglátni a szörnyűségben a nevetségest."},
                    {"type": "narration", "text": "A híres Egyperces novellák éppen ebből a szellemből születtek. Rendkívüli tömörségükkel, száraz használati utasításra emlékeztető nyelvükkel leleplezik a világ képtelenségeit. Örkény nem ítélkezik és nem moralizál: elénk tartja a görbe tükröt, amelyben a halálos veszedelem hirtelen felszabadító derűvé szelídül."},
                    {"type": "narration", "text": "Gondolatai a pincéből ma is a szellemi szabadság leckéjét tanítják: aki képes nevetni a saját félelmein és a történelem abszurditásán, azt soha semmilyen zsarnokság nem győzheti le végérvényesen."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Miért tekinthető a groteszk túlélési stratégiának Örkény István szerint?", [
                    "Mert a humor és az abszurditás felismerése megóvja az emberi méltóságot a történelem borzalmai közepette.",
                    "Mert segít eladni a könyveket külföldön.",
                    "Mert elfeledteti a magyar nyelvtant."
                ], 0, ["c1-05-vocab"]),
                fb("grammar", "practice", "Örkény novelláiban a tragikus valóság és a hűvös tárgyilagosság _____ alkot. (grotesque / groteszket)", "groteszket", "In Örkény's short stories, tragic reality and cool objectivity form a grotesque.", ["c1-antiphrasis-understatement"]),
                match("vocabulary", "controlled", [["groteszk", "grotesque"], ["egyperces", "one-minute story"], ["abszurditás", "absurdity"], ["kiszolgáltatottság", "vulnerability"]], ["c1-05-vocab"]),
                mc("reading", "practice", "Hol formálódott Örkény groteszk látásmódja a szöveg tanúsága szerint?", [
                    "A háború borzalmai, a front és a budapesti pincék tapasztalatai közepette.",
                    "Egy párizsi kávéház teraszán békebeli időkben.",
                    "Egy vidéki csendes kolostorban."
                ], 0, None),
                mc("reading", "practice", "Milyen nyelvi formát választott Örkény az Egyperces novellákhoz?", [
                    "Rendkívül tömör, száraz használati utasításra vagy hivatalos hirdetményre emlékeztető formát.",
                    "Virágos, tizenkilencedik századi költői nyelvet.",
                    "Hosszú, többkötetes történelmi regényfolyamot."
                ], 0, None),
                sb("grammar", "practice", ["A", "groteszk", "az", "abszurditás", "elleni", "legfőbb", "szellemi", "védőpajzs."], ["A", "groteszk", "az", "abszurditás", "elleni", "legfőbb", "szellemi", "védőpajzs."], "The grotesque is the chief intellectual shield against absurdity.", ["c1-antiphrasis-understatement"]),
                sw("production", [{"prompt": "Write a short grotesque commentary in Örkény's deadpan style.", "answer": "A túléléshez mindössze három dolog szükséges: egy mély pince, egy konzervnyitó és a humorérzék."}], ["c1-antiphrasis-understatement"]),
                mc("grammar", "check", "Melyik állítás foglalja össze legmélyebben Örkény írói üzenetét?", [
                    "A nevetés a szabadság végső menedéke az elnyomással és a félelemmel szemben.",
                    "A történelemben minden rendben van, és semmi baj nem történhet.",
                    "A szomorúság az egyetlen elfogadható emberi érzés."
                ], 0, ["c1-antiphrasis-understatement"])
            ]
        }
    ]

    for l in core_lessons:
        emit_instructional_lesson(5, "core", l, core_title, core_intro if l["num"] == 1 else None)

    # Core Consolidation
    emit_consolidation_lesson(
        5,
        "core",
        "c1-05-consolidation",
        core_title,
        [
            "I can manipulate pragmatic particles of irony (ugyebár, elvégre, netalán).",
            "I can craft devastating understatements and litotes.",
            "I can deploy polite disclaimers and analyze the Central European grotesque."
        ],
        [
            mc("grammar", "recognize", "Melyik részecske hordozza a legerősebb ironikus altextust?", [
                "ugyebár",
                "mivel",
                "azért"
            ], 0, ["c1-ironic-particles"]),
            mc("grammar", "recognize", "Mit fejez ki az 'enyhén szólva nem volt sikeres' fordulat?", [
                "Litotészt és retorikai visszafogottságot (a teljes kudarc finom megnevezését).",
                "Pontos mérési eredményt.",
                "Zenei ritmust."
            ], 0, ["c1-antiphrasis-understatement"]),
            match("vocabulary", "recognize", [["ugyebár", "mind you"], ["elvégre", "after all"], ["litotész", "understatement"], ["groteszk", "grotesque"], ["minden tiszteletem mellett", "with all due respect"]], ["c1-05-vocab"]),
            fb("vocabulary", "recall", "A döntéshozók, _____ mindent a szabályok betartásával magyaráztak. (mind you / ugyebár)", "ugyebár", "The decision-makers, mind you, explained everything by adherence to the rules.", ["c1-05-vocab"]),
            fb("vocabulary", "recall", "Az elért eredmény, enyhén _____, elmaradt a grandiózus ígéretektől. (to put it mildly / szólva)", "szólva", "The achieved result, to put it mildly, fell short of the grandiose promises.", ["c1-05-vocab"]),
            fb("grammar", "recall", "Minden _____ mellett meg kell jegyeznem, hogy a stratégia elhibázott volt. (respect / tiszteletem)", "tiszteletem", "With all due respect I must remark that the strategy was mistaken.", ["c1-subtle-disclaimer"]),
            fb("grammar", "context", "Örkény szerint a _____ a lélek végső menedéke az abszurd világban. (grotesque / groteszk)", "groteszk", "According to Örkény, the grotesque is the soul's ultimate refuge in an absurd world.", ["c1-antiphrasis-understatement"]),
            fb("grammar", "context", "A hivatalos bikkfanyelv és a valóság ütközése komikus _____ eredményez. (register clash / stílustörést)", "stílustörést", "The collision of official wooden language and reality results in a comical register clash.", ["c1-ironic-particles"]),
            mc("grammar", "context", "Mi a különbség az egyszerű vicc és a közép-európai groteszk között?", [
                "A groteszk egzisztenciális mélységű, a tragédiából fakad és a túlélést szolgálja.",
                "A groteszk mindig rövidebb három szónál.",
                "Nincs semmiféle különbség köztük."
            ], 0, ["c1-antiphrasis-understatement"]),
            sb("grammar", "produce", ["A", "nevetés", "a", "szabadság", "végső", "és", "elpusztíthatatlan", "menedéke."], ["A", "nevetés", "a", "szabadság", "végső", "és", "elpusztíthatatlan", "menedéke."], "Laughter is the ultimate and indestructible refuge of freedom.", ["c1-antiphrasis-understatement"]),
            sw("production", [{"prompt": "Write an understated critique with 'enyhén szólva'.", "answer": "A vállalkozás kimenetele, enyhén szólva, nem felelt meg az előzetes várakozásoknak."}], ["c1-antiphrasis-understatement"]),
            sw("production", [{"prompt": "Formulate a polite disagreement starting with 'Minden tiszteletem mellett'.", "answer": "Minden tiszteletem mellett bátorkodom jelezni, hogy a premisszák nem állják meg a helyüket."}], ["c1-subtle-disclaimer"])
        ]
    )

    # ----------------------------------------------------
    # TRACK 2: DISCOURSE (c1-pestiironia)
    # ----------------------------------------------------
    slug = "pestiironia"
    disc_title = "Urban Satire as Political Defense"
    disc_intro = [
        "In Budapest, humor is not entertainment; it is an institution, a trench, and an invisible republic of freedom. The 'pesti vicc' (Budapest political joke), the literary cabaret, and coffee-house wit dismantled authoritarian regimes from within.",
        "In this unit, you will explore the anatomy of urban satire: Frigyes Karinthy's brilliant literary parodies, Endre Nagy's and Géza Hofi's fearless cabaret monologues, Cold War samizdat humor, and the continuation of urban satire in modern meme culture."
    ]

    disc_lessons = [
        {
            "num": 1,
            "stem": f"c1-{slug}-01",
            "title": "The Anatomy of the Pesti Vicc: Humor as Survival",
            "grammar_title": "Urban Wit, Collective Catharsis, and Political Jokes",
            "grammar_skill": "c1-satirical-discourse",
            "goals": [
                "I can analyze the socio-cultural phenomenon of the 'pesti vicc'.",
                "I can understand how political jokes deconstructed propaganda during dictatorial regimes.",
                "I can decode multi-layered urban idioms and punchlines in Hungarian."
            ],
            "vocab": [
                {"lemma": "pesti vicc", "translation": "Budapest political joke / urban wit", "pos": "noun"},
                {"lemma": "poén", "translation": "punchline", "pos": "noun"},
                {"lemma": "önvédelem", "translation": "self-defense", "pos": "noun"},
                {"lemma": "fanyar", "translation": "tart, dry, wry", "pos": "adjective"},
                {"lemma": "túlélési ösztön", "translation": "survival instinct", "pos": "noun"},
                {"lemma": "katarzis", "translation": "catharsis", "pos": "noun"},
                {"lemma": "diktatúra", "translation": "dictatorship", "pos": "noun"},
                {"lemma": "szájhagyomány", "translation": "oral tradition", "pos": "noun"}
            ],
            "gr_text1": "The *pesti vicc* was Budapest's unofficial currency during war and dictatorship. Circulating purely through oral culture (*szájhagyomány*), it punctured total state control with instantaneous, wry (*fanyar*) humor.",
            "gr_text2": "The anatomy of the joke relies on a sudden conceptual twist (*csattanó, poén*) that unmasks official hypocrisy through common sense.",
            "gr_table": [
                ["A pesti vicc mint a szellem önvédelme...", "The Budapest joke as the self-defense of the mind..."],
                ["Fanyar humor és felszabadító katarzis...", "Wry humor and liberating catharsis..."],
                ["A hatalom leleplezése egyetlen poénnal...", "Unmasking power with a single punchline..."]
            ],
            "world_story_seg": {
                "seg_slug": "kavicsok",
                "title": "A pesti vicc: A nevető város legendája",
                "summary": "How Budapest survived invasions, sieges, and totalitarian regimes through the invincible, subversive weapon of urban political jokes.",
                "paragraphs": [
                    {"type": "narration", "text": "Budapest a huszadik században a történelem legkegyetlenebb viharait szenvedte el: világháborúkat, ostromot, nyilas terrort, szovjet megszállást és rákosista elnyomást. És mégis, a romok között, a villamosokon és a kávéházak sarkában volt valami, amit semmilyen tank és titkosrendőrség sem tudott elhallgattatni: a pesti vicc."},
                    {"type": "narration", "text": "A pesti vicc nem egyszerű tréfa volt, hanem a kollektív túlélés művészete. Amikor a rádió és az újságok a legvadabb propagandát harsogták, a város polgárai egyetlen fanyar, szellemes poénnal törölték el a hazugságok birodalmát. Ha délelőtt történt valamilyen politikai botrány, délre már az egész Nagykörút a legújabb viccen nevetett."},
                    {"type": "narration", "text": "Ez a humor nem volt kegyetlen, de nem ismert kíméletet a hatalom gőgjével szemben. Megtanította a pesti embert arra, hogy nem kell félni attól, aki nevetséges; és amíg nevetni tudunk, addig a lelkünk mélyén szabadok maradunk."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Miért tekintik a 'pesti viccet' a szellem önvédelmének?", [
                    "Mert a humor segítségével leplezte le a totalitárius hazugságokat és biztosította a belső szabadságot.",
                    "Mert a rendőrség hivatalosan kötelezte a lakosságot a viccmesélésre.",
                    "Mert a viccekből tanultak meg az emberek idegen nyelveket."
                ], 0, ["c1-pesti-ironia-vocab"]),
                fb("grammar", "practice", "A pesti vicc a diktatúrák alatt a szájhagyomány útján terjedő legfőbb szellemi _____ volt. (self-defense / önvédelem)", "önvédelem", "Under dictatorships, the Budapest joke was the chief intellectual self-defense spreading via oral tradition.", ["c1-satirical-discourse"]),
                match("vocabulary", "controlled", [["pesti vicc", "Budapest joke"], ["fanyar", "wry / dry"], ["poén", "punchline"], ["szájhagyomány", "oral tradition"]], ["c1-pesti-ironia-vocab"]),
                sb("grammar", "practice", ["A", "nevetés", "felszabadító", "ereje", "legyőzte", "a", "félelem", "légkörét."], ["A", "nevetés", "felszabadító", "ereje", "legyőzte", "a", "félelem", "légkörét."], "The liberating power of laughter overcame the atmosphere of fear.", ["c1-satirical-discourse"]),
                dc("dialogue", [
                    {"speaker": "Történész", "text": "Miért félt a hatalom annyira a politikai viccektől?"},
                    {"speaker": "Szociológus", "text": "Mert a nevetségessé válás ellen egyetlen diktatúrának sincs védelme."},
                ], ["nevetségessé válás ellen", "a sok pénz miatt", "a szép ruhák miatt"], 0, ["c1-satirical-discourse"]),
                sw("production", [{"prompt": "Write a sentence on the psychological function of urban satire.", "answer": "A pesti vicc fanyar bölcsessége a józan ész védőpajzsa volt a totalitárius őrülettel szemben."}], ["c1-satirical-discourse"]),
                mc("grammar", "check", "Melyik állítás jellemzi leginkább a pesti vicc szellemiségét?", [
                    "A fanyar önirónia, a gyors reagálás és az intellektuális szuverenitás.",
                    "A gyűlöletkeltés és a vak engedelmesség.",
                    "A külvilág eseményei iránti teljes érdektelenség."
                ], 0, ["c1-satirical-discourse"])
            ]
        },
        {
            "num": 2,
            "stem": f"c1-{slug}-02",
            "title": "Master of Parody: Frigyes Karinthy and Coffeehouse Wit",
            "grammar_title": "Literary Parody, Stylistic Mimicry, and Philosophical Wit",
            "grammar_skill": "c1-satirical-discourse",
            "goals": [
                "I can analyze Frigyes Karinthy's iconic parody collection 'Így írtok ti'.",
                "I can evaluate stylistic mimicry and caricature of famous literary styles.",
                "I can appreciate how humor and profound philosophical inquiry coexisted in Karinthy's thought."
            ],
            "vocab": [
                {"lemma": "stílusparódia", "translation": "stylistic parody", "pos": "noun"},
                {"lemma": "kávéházi kultúra", "translation": "coffeehouse culture", "pos": "noun"},
                {"lemma": "karikatúra", "translation": "caricature", "pos": "noun"},
                {"lemma": "elrajzolás", "translation": "distortion, exaggerated sketch", "pos": "noun"},
                {"lemma": "zsenialitás", "translation": "genius, brilliance", "pos": "noun"},
                {"lemma": "szójáték", "translation": "pun, wordplay", "pos": "noun"},
                {"lemma": "humorérzék", "translation": "sense of humor", "pos": "noun"},
                {"lemma": "intellektuális játék", "translation": "intellectual game", "pos": "noun"}
            ],
            "gr_text1": "Frigyes Karinthy was the uncrowned king of Budapest coffee-house wit (*kávéházi kultúra*). His masterwork *Így írtok ti* (That's How You Write) introduced brilliant literary parody: exaggerating an author's stylistic idiosyncrasies so precisely that the parody reveals the essence of the original.",
            "gr_text2": "Karinthy famously claimed: 'In humor I know no joke' (*Humorban nem ismerek tréfát*). His comedy was a deeply serious philosophical inquiry into the relativity of human existence and the boundaries of language.",
            "gr_table": [
                ["A stílusparódia zseniális lényeglátása...", "The brilliant insight of stylistic parody..."],
                ["Humorban nem ismerek tréfát...", "In humor I know no joke... (Karinthy maxim)"],
                ["A budapesti kávéházi szellem eleven közege...", "The living medium of the Budapest coffeehouse spirit..."]
            ],
            "world_story_seg": {
                "seg_slug": "karinthy",
                "title": "Karinthy Frigyes: A nevetés filozófusa",
                "summary": "How polymath Frigyes Karinthy revolutionized Hungarian literary parody and turned humor into an instrument of philosophical discovery.",
                "paragraphs": [
                    {"type": "narration", "text": "A New York kávéház vagy a Hadik márványasztalai mellett egy zseniális, fáradt szemű férfi ült, akit Karinthy Frigyesnek hívtak. Számára a világ nem komoly és unalmas tények halmaza volt, hanem a legcsodálatosabb intellektuális játszótér. Ahol mások megbotránkoztak, ott ő meglátta a dolgok rejtett logikáját; és ahol mások ünnepélyes pátosszal beszéltek, ott egyetlen szójátékkal robbantotta fel az álszentséget."},
                    {"type": "narration", "text": "Amikor 1912-ben megjelent Így írtok ti című paródiakötete, a magyar irodalom egyszerre kapott a szívéhez és tört ki hahotázásban. Karinthy nem gúnyolta ki a kortárs írókat: szerette őket, de oly tökéletesen utánozta stílusuk minden apró manírját és túlzását, hogy a paródiák maguk is klasszikus remekművekké váltak."},
                    {"type": "narration", "text": "Karinthy vallotta: a humor a legkomolyabb dolog a világon. Nem a komolyság ellentéte – a komolyság ellentéte a butaság és a merevség. A humor az a képesség, hogy felülemelkedjünk a saját korlátainkon, és meglássuk az emberi lét tragikomikus nagyszerűségét."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Mit értett Karinthy Frigyes a híres mondása alatt: 'Humorban nem ismerek tréfát'?", [
                    "Azt, hogy a humor nem felszínes szórakozás, hanem a legmélyebb filozófiai tisztánlátás és felelősség.",
                    "Azt, hogy ő maga sosem nevet semmin.",
                    "Azt, hogy a vicceket be kellene tiltani."
                ], 0, ["c1-pesti-ironia-vocab"]),
                fb("grammar", "practice", "Karinthy paródiái az írói manírok zseniális _____ révén világítják meg az eredeti művek lényegét. (exaggerated sketch / elrajzolása)", "elrajzolása", "Karinthy's parodies illuminate the essence of the original works through the brilliant exaggerated sketching of writerly mannerisms.", ["c1-satirical-discourse"]),
                match("vocabulary", "controlled", [["stílusparódia", "stylistic parody"], ["kávéházi kultúra", "coffeehouse culture"], ["karikatúra", "caricature"], ["szójáték", "wordplay"]], ["c1-pesti-ironia-vocab"]),
                sb("grammar", "practice", ["A", "humor", "a", "butaság", "és", "a", "merevség", "legfőbb", "ellenszere."], ["A", "humor", "a", "butaság", "és", "a", "merevség", "legfőbb", "ellenszere."], "Humor is the chief antidote to stupidity and rigidity.", ["c1-satirical-discourse"]),
                dc("dialogue", [
                    {"speaker": "Olvasó", "text": "Megsértődtek a Nyugat írói Karinthy paródiáin?"},
                    {"speaker": "Irodalmár", "text": "Dehogy! Elismerésnek számított, ha valakit Karinthy parodizált."},
                ], ["Elismerésnek számított", "Azonnal párbajra hívták", "Soha többé nem köszöntek"], 0, ["c1-satirical-discourse"]),
                sw("production", [{"prompt": "Write a thought in Karinthy's spirit about the connection between humor and intelligence.", "answer": "A humor nem a komolyság hiánya, hanem az intellektuális érettség legmagasabb foka."}], ["c1-satirical-discourse"]),
                mc("grammar", "check", "Melyik műfaj megújítása fűződik Karinthy Frigyes nevéhez?", [
                    "A modern magyar irodalmi stílusparódia (Így írtok ti).",
                    "A középkori latin himnuszköltészet.",
                    "A naturalista parasztballada."
                ], 0, ["c1-satirical-discourse"])
            ]
        },
        {
            "num": 3,
            "stem": f"c1-{slug}-03",
            "title": "Cabaret as Public Forum: Endre Nagy to Géza Hofi",
            "grammar_title": "Political Cabaret Monologues and Popular Dissidence",
            "grammar_skill": "c1-parodic-inversion",
            "goals": [
                "I can analyze the political cabaret tradition from Endre Nagy's stage to Géza Hofi's legendary monologues.",
                "I can evaluate subversive double talk and institutional safety valves (*szelepfunkció*).",
                "I can interpret colloquial humor infused with sharp socio-political critique."
            ],
            "vocab": [
                {"lemma": "politikai kabaré", "translation": "political cabaret", "pos": "noun"},
                {"lemma": "konferanszié", "translation": "compère, Master of Ceremonies", "pos": "noun"},
                {"lemma": "szelepfunkció", "translation": "safety valve function", "pos": "noun"},
                {"lemma": "kiszólás", "translation": "aside, subversive stage remark", "pos": "noun"},
                {"lemma": "szatíra", "translation": "satire", "pos": "noun"},
                {"lemma": "társadalomkritika", "translation": "social critique", "pos": "noun"},
                {"lemma": "közmegegyezés", "translation": "public consensus", "pos": "noun"},
                {"lemma": "szókimondó", "translation": "outspoken, forthright", "pos": "adjective"}
            ],
            "gr_text1": "Budapest cabaret was an indispensable public forum. Endre Nagy invented the literary *konferanszié* who engaged in direct political conversation with the audience. Under state socialism, Géza Hofi became the nation's court jester: using daring asides (*kiszólások*) to voice what millions thought but could not utter.",
            "gr_text2": "The regime tolerated this as a *szelepfunkció* (safety valve to vent frustration), yet Hofi's monologues permanently eroded the ideological credibility of the system.",
            "gr_table": [
                ["A politikai kabaré mint a társadalom tükre...", "The political cabaret as society's mirror..."],
                ["Hofi Géza szókimondó kiszólásai...", "Géza Hofi's outspoken stage asides..."],
                ["A humor szelepfunkciója a diktatúrában...", "The safety-valve function of humor in dictatorship..."]
            ],
            "world_story_seg": {
                "seg_slug": "kabare",
                "title": "A színpad fegyvere: Nagy Endrétől Hofi Gézáig",
                "summary": "How the Budapest cabaret transformed from literary nightclub to the fearless conscience of the nation.",
                "paragraphs": [
                    {"type": "narration", "text": "Amikor Nagy Endre a huszadik század elején felállt a pesti színpadra, és elegáns szmokingban, közvetlen hangon beszélni kezdett a közönséghez a napi politika botrányairól, megszületett a magyar politikai kabaré. A kabaré nem cirkuszi bohózat volt: a város legműveltebb értelmisége gyűlt össze esténként, hogy a szatíra éles tükrében szembesüljön a hatalom gyarlóságaival."},
                    {"type": "narration", "text": "Évtizedekkel később, a Kádár-korszak fojtogató légkörében egy zseniális színész, Hofi Géza vitte tovább ezt a lángot. A Mikroszkóp Színpad deszkáin estéről estére kimondta azt, amit az emberek otthon, lehúzott redőnyök mögött suttogtak. Karikírozta a pártfunkcionáriusok ostobaságát, a tervgazdaság csődjét és a kisemberek mindennapi nyomorúságát."},
                    {"type": "narration", "text": "A hatalom hiába próbálta biztonsági szelepként használni: Hofi nevetése halálos sebet ejtett a rendszer tekintélyén. Amikor egy nép már nevetni tud az elnyomóin, az elnyomók hatalma erkölcsileg véget ért."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Mi volt Hofi Géza kabaréjának társadalmi jelentősége a Kádár-korszakban?", [
                    "A nép kimondatlan gondolatainak bátor és szellemes megfogalmazása a színpadon.",
                    "A szocialista tervgazdaság feltétlen dicsérete.",
                    "A külföldi filmek bemutatása."
                ], 0, ["c1-pesti-ironia-vocab"]),
                fb("grammar", "practice", "A hatalom a kabaré _____ bízott, ám a gúny valójában aláásta a rendszer legitimitását. (safety valve function / szelepfunkciójában)", "szelepfunkciójában", "Power trusted in the safety valve function of cabaret, but the mockery actually undermined the regime's legitimacy.", ["c1-parodic-inversion"]),
                match("vocabulary", "controlled", [["politikai kabaré", "political cabaret"], ["konferanszié", "compère"], ["szelepfunkció", "safety valve function"], ["kiszólás", "subversive stage aside"]], ["c1-pesti-ironia-vocab"]),
                sb("grammar", "practice", ["A", "szatíra", "halálos", "sebet", "ejtett", "a", "diktatúra", "tekintélyén."], ["A", "szatíra", "halálos", "sebet", "ejtett", "a", "diktatúra", "tekintélyén."], "Satire inflicted a mortal wound on the authority of dictatorship.", ["c1-parodic-inversion"]),
                dc("dialogue", [
                    {"speaker": "Néző", "text": "Hogyan engedhették meg Hofinak ezeket a bátor kiszólásokat?"},
                    {"speaker": "Kritikus", "text": "A rendszer azt hitte, kordában tartja a feszültséget, de valójában nevetségessé vált."},
                ], ["kordában tartja a feszültséget", "nagyon büszke volt rá", "egyáltalán nem érdekelte"], 0, ["c1-parodic-inversion"]),
                sw("production", [{"prompt": "Write a sentence reflecting on Hofi Géza's cultural impact.", "answer": "Hofi Géza szókimondó humora a nemzet kollektív terápiája és lelkiismerete volt."}], ["c1-parodic-inversion"]),
                mc("grammar", "check", "Melyik állítás összegzi a pesti kabaré történelmi küldetését?", [
                    "A társadalomkritika, az intellektuális bátorság és a felszabadító nevetés összefonódása.",
                    "A közönség altatása unalmas történetekkel.",
                    "A hivatalos híradók szó szerinti felolvasása."
                ], 0, ["c1-parodic-inversion"])
            ]
        },
        {
            "num": 4,
            "stem": f"c1-{slug}-04",
            "title": "Samizdat Humor and Reading Between the Lines",
            "grammar_title": "Esopian Language, Subversive Innuendo, and Samizdat Wit",
            "grammar_skill": "c1-parodic-inversion",
            "goals": [
                "I can decode Aesopian language (*aizopusi nyelv*) used to bypass censorship.",
                "I can analyze Cold War samizdat publications and underground satire.",
                "I can craft sentences that communicate deep subversive meaning through double entendre."
            ],
            "vocab": [
                {"lemma": "aizopusi nyelv", "translation": "Aesopian language (coded dissent)", "pos": "noun"},
                {"lemma": "sorok között olvas", "translation": "to read between the lines", "pos": "expression"},
                {"lemma": "szamizdat", "translation": "samizdat (underground publication)", "pos": "noun"},
                {"lemma": "cenzúra", "translation": "censorship", "pos": "noun"},
                {"lemma": "cinkosság", "translation": "complicity (intellectual complicity with audience)", "pos": "noun"},
                {"lemma": "rejtett üzenet", "translation": "coded / hidden message", "pos": "noun"},
                {"lemma": "áthallás", "translation": "allusion, innuendo, resonance", "pos": "noun"},
                {"lemma": "felforgató", "translation": "subversive", "pos": "adjective"}
            ],
            "gr_text1": "Under state censorship (*cenzúra*), Hungarian writers perfected *aizopusi nyelv* (Aesopian language). By shifting historical settings or using coded allegories, authors established an unspoken intellectual complicity (*cinkosság*) with an audience trained to *sorok között olvasni* (read between the lines).",
            "gr_text2": "An innocent line on stage could trigger thunderous applause if it contained an undeniable contemporary allusion (*áthallás*).",
            "gr_table": [
                ["A sorok között olvasás kifinomult művészete...", "The refined art of reading between the lines..."],
                ["Áthallásokkal teli történelmi drámák...", "Historical dramas filled with contemporary allusions..."],
                ["Szamizdat lapok és a cenzúra kikerülése...", "Samizdat publications and bypassing censorship..."]
            ],
            "world_story_seg": {
                "seg_slug": "szamizdat",
                "title": "A sorok között olvasás művészete és a szamizdat",
                "summary": "How Hungarian writers and readers communicated in secret codes through Aesopian language, allegories, and underground samizdat presses.",
                "paragraphs": [
                    {"type": "narration", "text": "A diktatúra évtizedeiben a magyar irodalom és színház különleges titkos társasággá vált. A cenzorok ott ültek minden szerkesztőségben és színházi premieren, ceruzával a kézben keresve a felforgató gondolatokat. Az írók azonban kifejlesztették a védekezés legkifinomultabb eszközét: az aizopusi nyelvet."},
                    {"type": "narration", "text": "Amikor egy történelmi drámában a török hódoltságról vagy az 1849-es orosz beavatkozásról beszéltek, minden néző pontosan tudta, hogy a darab valójában az 1956 utáni szovjet megszállásról szól. A színpad és a nézőtér között láthatatlan villámok cikáztak: egyetlen hangsúly, egy megállás vagy egy sokatmondó pillantás elegendő volt ahhoz, hogy a közönség tapsviharban törjön ki."},
                    {"type": "narration", "text": "Azok pedig, akik nem akartak metaforák mögé rejtőzni, a föld alá mentek. Írógépekkel, indigóval és titkos stencilekkel sokszorosították a szamizdat folyóiratokat – a Beszélőt és a Hírmondót. A szabad gondolatot nem lehetett börtönbe zárni: a humor és a bátorság fegyverével felvértezve utat talált a szabadság hajnala felé."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Mit jelentett az 'aizopusi nyelv' a cenzúra korszakában?", [
                    "Olyan virágnyelvet és történelmi allegóriákat, amelyek rejtett üzeneteket közvetítettek a közönségnek a cenzorok kijátszásával.",
                    "Az ókori görög mesék szó szerinti fordítását.",
                    "A külföldi diplomaták titkos kódját."
                ], 0, ["c1-pesti-ironia-vocab"]),
                fb("grammar", "practice", "A darab bemutatóján a nézők azonnal felismerték a szöveg politikai _____. (innuendo / allusions / áthallásait)", "áthallásait", "At the premiere of the play, the audience immediately recognized the political innuendos of the text.", ["c1-parodic-inversion"]),
                match("vocabulary", "controlled", [["aizopusi nyelv", "Aesopian language"], ["sorok között olvas", "to read between lines"], ["áthallás", "allusion / innuendo"], ["szamizdat", "samizdat"]], ["c1-pesti-ironia-vocab"]),
                sb("grammar", "practice", ["A", "közönség", "megtanult", "a", "sorok", "között", "olvasni", "a", "cenzúra", "idején."], ["A", "közönség", "megtanult", "a", "sorok", "között", "olvasni", "a", "cenzúra", "idején."], "The audience learned to read between the lines during censorship.", ["c1-parodic-inversion"]),
                dc("dialogue", [
                    {"speaker": "Cenzor", "text": "Nem találok a szövegben nyílt rendszerellenes mondatot."},
                    {"speaker": "Szerkesztő", "text": "Természetesen; a dráma csupán a tizenhatodik századi török időkről szól."},
                ], ["tizenhatodik századi török időkről", "a szovjet kivonulásról", "a pártvezetés hibáiról"], 0, ["c1-parodic-inversion"]),
                sw("production", [{"prompt": "Write a sentence describing the phenomenon of reading between the lines.", "answer": "Az aizopusi nyelv révén a szerző és a közönség cinkos szövetséget kötött a szabadság nevében."}], ["c1-parodic-inversion"]),
                mc("grammar", "check", "Milyen funkciót töltöttek be a szamizdat kiadványok a rendszerváltás előtt?", [
                    "A cenzúrázatlan szabad gondolat, az emberi jogok és a valós hírek terjesztését.",
                    "A hivatalos pártkongresszus határozatainak nyomtatását.",
                    "A mezőgazdasági terményárak közlését."
                ], 0, ["c1-parodic-inversion"])
            ]
        },
        {
            "num": 5,
            "stem": f"c1-{slug}-05",
            "title": "Digital Meme Culture as the Successor of the Pesti Vicc",
            "grammar_title": "Internet Memes, Micro-Satire, and Digital Subversion",
            "grammar_skill": "c1-satirical-discourse",
            "goals": [
                "I can analyze digital internet memes as the contemporary successor to the 'pesti vicc'.",
                "I can evaluate visual parody, rapid satirical response, and community irony on social platforms.",
                "I can discuss how modern digital humor deconstructs authority and crisis."
            ],
            "vocab": [
                {"lemma": "internetes mém", "translation": "internet meme", "pos": "noun"},
                {"lemma": "mikroszatíra", "translation": "micro-satire", "pos": "noun"},
                {"lemma": "vírusként terjed", "translation": "to spread like a virus / go viral", "pos": "expression"},
                {"lemma": "vizuális humor", "translation": "visual humor", "pos": "noun"},
                {"lemma": "reflexió", "translation": "reflection", "pos": "noun"},
                {"lemma": "kifiguráz", "translation": "to lampoon, spoof, mock", "pos": "verb"},
                {"lemma": "közösségi élmény", "translation": "community experience", "pos": "noun"},
                {"lemma": "folytonosság", "translation": "continuity", "pos": "noun"}
            ],
            "gr_text1": "The digital era has not killed the *pesti vicc*; it has turbocharged it into internet memes. Within minutes of a political speech or gaffe, satirical images and remix videos *vírusként terjednek* (go viral) across Hungarian cyberspace.",
            "gr_text2": "Digital micro-satire preserves the essential traits of historical urban irony: lightning speed, deadpan juxtaposition, and the community catharsis of laughing at pompous authority.",
            "gr_table": [
                ["A digitális mémek mint a pesti vicc modern folytatása...", "Digital memes as the modern continuation of the Budapest joke..."],
                ["Villámgyors szatirikus reflexió a közéletre...", "Lightning-fast satirical reflection on public life..."],
                ["A hatalom kifigurázása a vizuális kultúrában...", "Lampooning power in visual culture..."]
            ],
            "world_story_seg": {
                "seg_slug": "memek",
                "title": "A nevetés digitális korszaka: Mémek és a pesti humor jövője",
                "summary": "How 21st-century internet meme creators inherited the wit, speed, and subversive courage of the historic Budapest political joke.",
                "paragraphs": [
                    {"type": "narration", "text": "Sokan féltették a pesti humort a huszonegyedik századtól. Azt hitték, a kávéházak eltűnésével és az internet elterjedésével a klasszikus pesti vicc is a múzeumok poros polcaira kerül. Ám a magyar szellem ismét rácáfolt a borúlátókra: a városi szatíra nem halt meg, hanem átköltözött a közösségi média hálózataiba."},
                    {"type": "narration", "text": "Ma az internetes mém a pesti vicc legtermészetesebb örököse. Ha a parlamentben valamilyen képtelen törvényt szavaznak meg, vagy egy közszereplő nevetséges nyilatkozatot tesz, nem kell napokat várni a válaszra. Percek múlva mémek tízezrei árasztják el a képernyőket: szellemes képmontázsok, parodisztikus videók és csattanós feliratok."},
                    {"type": "narration", "text": "A forma változott, de a lényeg változatlan maradt: a nevetés ma is a polgári függetlenség, a józan ész és a közösségi szolidaritás legfőbb biztosítéka. A mémkultúra bizonyítja, hogy a magyar nyelv és a pesti szellem a digitális korszakban is megőrzi kimeríthetetlen életerejét és szabadságszeretetét."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Hogyan kapcsolódnak a modern internetes mémek a klasszikus pesti vicchez?", [
                    "Ugyanazt a villámgyors szatirikus reflexiót és tekintélybontó humort folytatják digitális formában.",
                    "Semmi közük sincs egymáshoz.",
                    "A mémeket külföldi robotok írják kizárólag."
                ], 0, ["c1-pesti-ironia-vocab"]),
                fb("grammar", "practice", "A közösségi médiában a szatirikus mémek _____ terjednek a felhasználók között. (like a virus / vírusként)", "vírusként", "On social media, satirical memes spread like a virus among users.", ["c1-satirical-discourse"]),
                match("vocabulary", "controlled", [["internetes mém", "internet meme"], ["mikroszatíra", "micro-satire"], ["kifiguráz", "to lampoon / spoof"], ["vírusként terjed", "to spread virally"]], ["c1-pesti-ironia-vocab"]),
                sb("grammar", "practice", ["A", "digitális", "mémkultúra", "a", "városi", "szatíra", "legújabb", "formája."], ["A", "digitális", "mémkultúra", "a", "városi", "szatíra", "legújabb", "formája."], "Digital meme culture is the latest form of urban satire.", ["c1-satirical-discourse"]),
                dc("dialogue", [
                    {"speaker": "Elemző", "text": "Képesek a mémek valódi politikai hatást elérni?"},
                    {"speaker": "Médiakutató", "text": "Igen; a nevetségessé válás ma is a leghatásosabb tekintélyromboló fegyver."},
                ], ["leghatásosabb tekintélyromboló fegyver", "teljesen haszontalan dolog", "senkit sem érdekel"], 0, ["c1-satirical-discourse"]),
                sw("production", [{"prompt": "Write a sentence reflecting on the continuity between political jokes and digital memes.", "answer": "A mém a pesti vicc digitális köntöse: a nevetés örök védőpajzsa az ostobasággal szemben."}], ["c1-satirical-discourse"]),
                mc("grammar", "check", "Mi biztosítja a pesti humor folytonosságát a digitális korban?", [
                    "A hatalom gőgjének elutasítása, a gyors észjárás és a szabadság szeretete.",
                    "A régi újságok szkennelése.",
                    "A viccmesélés betiltása a munkahelyeken."
                ], 0, ["c1-satirical-discourse"])
            ]
        }
    ]

    for l in disc_lessons:
        emit_instructional_lesson(5, "discourse", l, disc_title, disc_intro if l["num"] == 1 else None)

    # Full World Compilation Story
    write_json(
        f"stories/world/c1/{slug}.json",
        {
            "id": f"story.c1.world.{slug}",
            "title": "A nevetés anatómiája: Pesti kabaré, vicc és szamizdat",
            "level": "C1",
            "type": "world",
            "summary": "Comprehensive chronicle of Budapest urban satire as intellectual armor: from the legendary pesti vicc and Karinthy's parodies through Nagy Endre, Géza Hofi, samizdat Aesopian language, to digital meme culture.",
            "paragraphs": [
                {"type": "narration", "text": "Budapest a huszadik század legnehezebb évtizedeiben sem veszítette el humorát. A romok között, a pincékben és a kávéházak asztalainál született meg a 'pesti vicc': az a villámgyors, fanyar szellemesség, amely a túlélés és az intellektuális önvédelem legfontosabb fegyverévé vált a diktatúrákkal szemben."},
                {"type": "narration", "text": "Karinthy Frigyes a New York kávéház márványasztalánál bizonyította be, hogy a humor a legmélyebb filozófiai bölcsesség. Paródiáival nemcsak az irodalmi pózokat leplezte le, hanem az emberi gondolkodás merevségeit is feloldotta a felszabadító nevetésben."},
                {"type": "narration", "text": "A kabaré színpadán Nagy Endrétől Hofi Gézáig a nemzet kollektív lelkiismerete szólalt meg. Hofi bátor kiszólásai estéről estére kimondták azt, amit milliók csak suttogni mertek, helyreállítva a józan ész és az emberi méltóság tekintélyét az ideológiai hazugságok felett."},
                {"type": "narration", "text": "A cenzúra szorításában az írók és az olvasók kifejlesztették az aizopusi nyelv és a sorok közötti olvasás cinkos művészetét, miközben a szamizdat nyomdák a szabad szó tüzét őrizték a föld alatt."},
                {"type": "narration", "text": "Ez a páratlan szellemi örökség ma a digitális mémkultúrában él tovább. A modern mémkészítők a pesti vicc igazi örökösei: emlékeztetnek arra, hogy amíg egy nemzet képes nevetni a saját nehézségein és a hatalom kisszerűségein, addig a szabadsága elpusztíthatatlan."}
            ]
        }
    )

    # Discourse Consolidation
    emit_consolidation_lesson(
        5,
        "discourse",
        f"c1-{slug}-consolidation",
        disc_title,
        [
            "I can analyze the socio-cultural functions of urban satire, cabaret, and political jokes.",
            "I can decode Aesopian language, double entendre, and satirical parody in Hungarian.",
            "I can trace the lineage of urban wit from Karinthy and Hofi to contemporary digital meme culture."
        ],
        [
            mc("grammar", "recognize", "Milyen szerepet töltött be a pesti vicc a diktatúrák idején?", [
                "A szellemi önvédelem és a belső szabadság megőrzésének legfőbb eszköze volt.",
                "A kormány hivatalos híradója volt.",
                "A mezőgazdasági statisztikák összefoglalása."
            ], 0, ["c1-satirical-discourse"]),
            mc("grammar", "recognize", "Mit jelent az 'aizopusi nyelv' a magyar irodalomtörténetben?", [
                "A cenzúra kijátszására szolgáló rejtett, allegorikus és áthallásos fogalmazásmódot.",
                "Az ókori görög verstan szabályait.",
                "Egy teljesen elfelejtett indiai dialektust."
            ], 0, ["c1-parodic-inversion"]),
            match("vocabulary", "recognize", [["pesti vicc", "Budapest joke"], ["stílusparódia", "stylistic parody"], ["szelepfunkció", "safety valve function"], ["aizopusi nyelv", "Aesopian language"], ["internetes mém", "internet meme"]], ["c1-pestiironia-vocab"]),
            fb("vocabulary", "recall", "Karinthy híres műve, az Így írtok ti a magyar irodalom legkiemelkedőbb _____ gyűjteménye. (parody / stílusparódia)", "stílusparódia", "Karinthy's famous work, That's How You Write, is the most outstanding stylistic parody collection in Hungarian literature.", ["c1-pestiironia-vocab"]),
            fb("vocabulary", "recall", "A Mikroszkóp Színpadon Hofi Géza bátor _____ nevettette meg a közönséget. (stage asides / kiszólásaival)", "kiszólásaival", "On the Mikroszkóp Stage, Géza Hofi made the audience laugh with his courageous stage asides.", ["c1-pestiironia-vocab"]),
            fb("grammar", "recall", "A diktatúrában a nézők megtanultak a sorok között _____. (to read / olvasni)", "olvasni", "In dictatorship, audiences learned to read between the lines.", ["c1-parodic-inversion"]),
            fb("grammar", "context", "A darab politikai _____ miatt a cenzúra utólag betiltotta az előadást. (innuendos / áthallásai)", "áthallásai", "Due to the political innuendos of the play, the censorship post-facto banned the performance.", ["c1-parodic-inversion"]),
            fb("grammar", "context", "A közösségi médiában a politikai hibákra válaszként született mémek _____ terjednek. (virally / vírusként)", "vírusként", "On social media, memes born in response to political errors spread virally.", ["c1-satirical-discourse"]),
            mc("grammar", "context", "Hogyan értékelhető a humor és a szabadság kapcsolata a magyar történelemben?", [
                "A nevetés a legvégső belső szabadságjog, amelyet semmilyen elnyomás nem tudott elvenni.",
                "A humor teljesen haszontalan időtöltés volt mindig.",
                "A nevetés a gyengeség és a megadás jele volt."
            ], 0, ["c1-satirical-discourse"]),
            sb("grammar", "produce", ["A", "pesti", "humor", "a", "józan", "ész", "és", "az", "emberi", "méltóság", "védőpajzsa."], ["A", "pesti", "humor", "a", "józan", "ész", "és", "az", "emberi", "méltóság", "védőpajzsa."], "Budapest humor is the shield of common sense and human dignity.", ["c1-satirical-discourse"]),
            sw("production", [{"prompt": "Write a critical reflection comparing Hofi Géza's cabaret and modern digital memes.", "answer": "Míg Hofi a színpadról formálta a nemzet lelkiismeretét, ma a mémek decentralizáltan dekonstruálják a hatalom gőgjét."}], ["c1-satirical-discourse"]),
            sw("production", [{"prompt": "Formulate a concluding thought on urban satire.", "answer": "Amíg egy társadalom képes öniróniával nevetni saját esendőségén, addig a szabadsága nem veszhet el."}], ["c1-satirical-discourse"])
        ]
    )
    print("=== Finished C1 Unit 5 ===")


if __name__ == "__main__":
    generate_unit_5()
