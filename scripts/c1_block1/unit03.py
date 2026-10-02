#!/usr/bin/env python3
"""
Hungarian C1 Block 1 - Unit 03 Generator:
  - Track 1 (Core): Unit 3 — "Epistemic Hedging, Probability & Evidential Stance" (c1-03)
  - Track 2 (Discourse): Unit 3 — "Epistemology & Scientific Paradigm Shifts" (c1-tudomanyelmelet)
"""

from .common import mc, match, fb, sb, dc, sw, write_json, emit_instructional_lesson, emit_consolidation_lesson


def generate_unit_3():
    print("=== Generating C1 Unit 3 ===")
    
    # ----------------------------------------------------
    # TRACK 1: CORE (c1-03)
    # ----------------------------------------------------
    core_title = "Epistemic Hedging, Probability & Evidential Stance"
    core_intro = [
        "In scholarly research and analytical writing, absolute assertions are rare. Intellectual maturity requires precise calibration of certainty, skepticism, and evidentiary source.",
        "In this unit, inspired by Antal Szerb's ironic and scholarly essays in 'A varázsló eltűnik', you will master epistemic modality (aligha feltételezhető, minden bizonnyal, úgy hírlik), evidentiality markers, and the art of academic hedging."
    ]

    core_lessons = [
        {
            "num": 1,
            "stem": "c1-03-01",
            "title": "Evidentiality Markers and Reported Stance",
            "grammar_title": "Evidentiality Markers: Úgy hírlik, Állítólag, and Források szerint",
            "grammar_skill": "c1-evidentiality-markers",
            "goals": [
                "I can distinguish between direct witness evidence and reported information.",
                "I can deploy evidential markers like 'úgy hírlik', 'állítólag', and 'a források tanúsága szerint'.",
                "I can calibrate scholarly distance from unverified claims."
            ],
            "vocab": [
                {"lemma": "evidencialitás", "translation": "evidentiality", "pos": "noun"},
                {"lemma": "úgy hírlik", "translation": "rumor has it, report has it", "pos": "expression"},
                {"lemma": "állítólag", "translation": "allegedly, supposedly", "pos": "adverb"},
                {"lemma": "tanúsága szerint", "translation": "according to the testimony of", "pos": "expression"},
                {"lemma": "hivatkozás", "translation": "citation, reference", "pos": "noun"},
                {"lemma": "megbízhatóság", "translation": "reliability, dependability", "pos": "noun"},
                {"lemma": "ellenőrizhetetlen", "translation": "unverifiable", "pos": "adjective"},
                {"lemma": "elsődleges forrás", "translation": "primary source", "pos": "noun"}
            ],
            "gr_text1": "Hungarian possesses rich lexical and syntactic strategies for evidentiality. When relaying second-hand information, adverbs like *állítólag* and verbal idioms like *úgy hírlik* distance the speaker from truth commitment.",
            "gr_text2": "In academic writing, *a források tanúsága szerint* or *a rendelkezésre álló adatok alapján* frames claims strictly within verifiable documentary limits: *A korabeli krónikák tanúsága szerint az esemény másként zajlott.*",
            "gr_table": [
                ["A források tanúsága szerint...", "According to the testimony of sources..."],
                ["Úgy hírlik, a kézirat elveszett.", "Word has it that the manuscript was lost."],
                ["Állítólag a kísérletet megismételték.", "Supposedly, the experiment was repeated."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mire szolgálnak az evidencialitási jelölők a tudományos stílusban?", ["A közölt információ forrásának és megbízhatóságának pontos megjelölésére.", "A mondatok hosszának növelésére.", "A nyelvhelyességi hibák elfedésére."], 0, ["c1-03-vocab"]),
                fb("grammar", "controlled", "A korabeli dokumentumok _____ szerint a döntés már hónapokkal korábban megszületett. (testimony of / tanúsága)", "tanúsága", "According to the testimony of contemporary documents, the decision had been made months earlier.", ["c1-evidentiality-markers"]),
                match("vocabulary", "controlled", [["úgy hírlik", "word has it"], ["állítólag", "allegedly"], ["megbízhatóság", "reliability"], ["elsődleges forrás", "primary source"]], ["c1-03-vocab"]),
                fb("grammar", "practice", "A kézirat _____ évszázadokon át egy kolostor könyvtárában rejtőzött. (allegedly / állítólag)", "állítólag", "Allegedly, the manuscript hid in a monastery library for centuries.", ["c1-evidentiality-markers"]),
                sb("grammar", "practice", ["A", "források", "tanúsága", "szerint", "a", "szerző", "nem", "írt", "több", "művet."], ["A", "források", "tanúsága", "szerint", "a", "szerző", "nem", "írt", "több", "művet."], "According to the testimony of sources, the author wrote no more works.", ["c1-evidentiality-markers"]),
                dc("dialogue", [
                    {"speaker": "Kutató", "text": "Biztosak lehetünk ebben a történelmi adatban?"},
                    {"speaker": "Professzor", "text": "Aligha; a források tanúsága szerint több ellentmondás is fennáll."},
                ], ["tanúsága szerint", "kitalációja szerint", "hiánya miatt"], 0, ["c1-evidentiality-markers"]),
                sw("production", [{"prompt": "Write a sentence attributing a claim to primary sources using 'A források tanúsága szerint'.", "answer": "A források tanúsága szerint a két tudós már korábban levelezett egymással."}], ["c1-evidentiality-markers"]),
                mc("grammar", "check", "Melyik kifejezés fejezi ki a legmagasabb tudományos megbízhatóságot?", [
                    "A primer források filológiai vizsgálata alapján",
                    "Úgy hallottam valakitől a folyosón",
                    "Állítólag így történt régen"
                ], 0, ["c1-evidentiality-markers"])
            ]
        },
        {
            "num": 2,
            "stem": "c1-03-02",
            "title": "Nuanced Probability Calibration: Aligha and Minden bizonnyal",
            "grammar_title": "Probability Calibration and Epistemic Particles",
            "grammar_skill": "c1-epistemic-hedging",
            "goals": [
                "I can calibrate degrees of probability from near-certainty to extreme skepticism.",
                "I can use 'aligha', 'minden bizonnyal', and 'feltehetőleg' in argument development.",
                "I can formulate measured hypotheses without dogmatic assertiveness."
            ],
            "vocab": [
                {"lemma": "aligha", "translation": "hardly, scarcely, barely likely", "pos": "adverb"},
                {"lemma": "minden bizonnyal", "translation": "in all probability, most certainly", "pos": "expression"},
                {"lemma": "feltehetőleg", "translation": "presumably, supposedly", "pos": "adverb"},
                {"lemma": "valószínűsíthető", "translation": "probable, presumable", "pos": "adjective"},
                {"lemma": "megalapozatlan", "translation": "unfounded, baseless", "pos": "adjective"},
                {"lemma": "valószínűség", "translation": "probability", "pos": "noun"},
                {"lemma": "kétely", "translation": "doubt, misgiving", "pos": "noun"},
                {"lemma": "bizonyosság", "translation": "certainty", "pos": "noun"}
            ],
            "gr_text1": "*Aligha* (hardly / scarcely) is the cornerstone of academic skepticism in Hungarian. Paired with indicative or conditional verbs, it denies likelihood with understated elegance: *Aligha feltételezhető, hogy a hiba véletlen lett volna.*",
            "gr_text2": "*Minden bizonnyal* indicates high inferential confidence based on cumulative evidence, while *feltehetőleg* marks an informed hypothesis awaiting definitive verification.",
            "gr_table": [
                ["Aligha vitatható a felfedezés jelentősége.", "The significance of the discovery can hardly be contested."],
                ["Minden bizonnyal ez a helyes értelmezés.", "In all probability, this is the correct interpretation."],
                ["Feltehetőleg a kísérleti feltételek változtak meg.", "Presumably, the experimental conditions changed."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mit fejez ki az 'aligha' határozószó a tudományos érvelésben?", ["Kifejezetten alacsony valószínűséget vagy elegáns elutasítást.", "Teljes bizonyosságot.", "Azonnali cselekvést."], 0, ["c1-03-vocab"]),
                fb("grammar", "controlled", "Ilyen előzmények után _____ feltételezhető, hogy a tárgyalások gyorsan lezárulnak. (hardly / aligha)", "aligha", "Following such antecedents, it is hardly presumable that the negotiations will conclude quickly.", ["c1-epistemic-hedging"]),
                match("vocabulary", "controlled", [["aligha", "hardly"], ["minden bizonnyal", "in all probability"], ["feltehetőleg", "presumably"], ["kétely", "doubt"]], ["c1-03-vocab"]),
                fb("grammar", "practice", "A kutatócsoport eredményei _____ új távlatokat nyitnak a molekuláris biológiában. (in all probability / minden bizonnyal)", "minden bizonnyal", "The research group's results in all probability open new horizons in molecular biology.", ["c1-epistemic-hedging"]),
                sb("grammar", "practice", ["Aligha", "lehet", "kétségbe", "vonni", "a", "módszertan", "szakszerűségét."], ["Aligha", "lehet", "kétségbe", "vonni", "a", "módszertan", "szakszerűségét."], "One can hardly call into question the professional competence of the methodology.", ["c1-epistemic-hedging"]),
                dc("dialogue", [
                    {"speaker": "Bíráló", "text": "Elfogadhatjuk ezt a végkövetkeztetést végleges bizonyítékként?"},
                    {"speaker": "Kutató", "text": "Aligha; feltehetőleg további mérésekre lesz szükség."},
                ], ["további mérésekre lesz szükség", "mindent tudunk már", "azonnal zárjuk le"], 0, ["c1-epistemic-hedging"]),
                sw("production", [{"prompt": "Write a critical scholarly judgment using 'aligha vitatható'.", "answer": "Aligha vitatható, hogy az új adatok alapjaiban kérdőjelezik meg a korábbi hipotézist."}], ["c1-epistemic-hedging"]),
                mc("grammar", "check", "Melyik állítás fejez ki megalapozott, de nem abszolút valószínűséget?", [
                    "A rendelkezésre álló adatok fényében minden bizonnyal ez a helytálló magyarázat.",
                    "Ez az egyetlen létező igazság a világon.",
                    "Biztosan így van, mert én úgy érzem."
                ], 0, ["c1-epistemic-hedging"])
            ]
        },
        {
            "num": 3,
            "stem": "c1-03-03",
            "title": "Modal Distancing: Nem zárható ki and Fenntartással",
            "grammar_title": "Negative Potentiality and Conditional Reservations",
            "grammar_skill": "c1-modal-distancing",
            "goals": [
                "I can express negative potentiality (*nem zárható ki, hogy*).",
                "I can insert academic reservations using *azzal a fenntartással*.",
                "I can avoid overstatement (*overgeneralization*) in conclusions."
            ],
            "vocab": [
                {"lemma": "nem zárható ki", "translation": "it cannot be ruled out (that)", "pos": "expression"},
                {"lemma": "fenntartással", "translation": "with reservations, qualifiedly", "pos": "adverb"},
                {"lemma": "óvatosság", "translation": "caution, prudence", "pos": "noun"},
                {"lemma": "megkockáztat", "translation": "to venture, risk (an opinion)", "pos": "verb"},
                {"lemma": "túláltalánosítás", "translation": "overgeneralization", "pos": "noun"},
                {"lemma": "feltételes", "translation": "conditional, qualified", "pos": "adjective"},
                {"lemma": "kikötés", "translation": "stipulation, proviso", "pos": "noun"},
                {"lemma": "mértéktartás", "translation": "moderation, restraint", "pos": "noun"}
            ],
            "gr_text1": "Modal distancing prevents dogmatic vulnerability. The construction *nem zárható ki, hogy* (it cannot be excluded that) allows researchers to entertain an unorthodox hypothesis without fully endorsing it.",
            "gr_text2": "*Azzal a fenntartással élve, hogy...* or *bizonyos fenntartásokkal kezelve* establishes that an inference is contingent upon future validation.",
            "gr_table": [
                ["Nem zárható ki, hogy az eredmények félrevezetők.", "It cannot be ruled out that the results are misleading."],
                ["Azzal a fenntartással fogadjuk el, hogy...", "We accept it with the reservation that..."],
                ["Megkockáztathatjuk azt a feltevést...", "We may venture the assumption..."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Milyen célt szolgál a 'nem zárható ki, hogy' fordulat?", ["Lehetőséget ad egy alternatív magyarázat felvetésére anélkül, hogy bizonyítottnak tekintenénk.", "Kizárja a további vitát.", "Azonnali beismerést jelent."], 0, ["c1-03-vocab"]),
                fb("grammar", "controlled", "Nem _____ ki, hogy a jövőbeni felfedezések megváltoztatják az álláspontunkat. (cannot be ruled out / zárható)", "zárható", "It cannot be ruled out that future discoveries will change our standpoint.", ["c1-modal-distancing"]),
                match("vocabulary", "controlled", [["nem zárható ki", "cannot be excluded"], ["fenntartással", "with reservations"], ["mértéktartás", "restraint"], ["megkockáztat", "to venture"]], ["c1-03-vocab"]),
                fb("grammar", "practice", "Az eredményeket csak komoly módszertani _____ szabad kezelni. (reservations / fenntartásokkal)", "fenntartásokkal", "The results must only be treated with serious methodological reservations.", ["c1-modal-distancing"]),
                sb("grammar", "practice", ["Nem", "zárható", "ki,", "hogy", "további", "tényezők", "is", "közrejátszottak."], ["Nem", "zárható", "ki,", "hogy", "további", "tényezők", "is", "közrejátszottak."], "It cannot be ruled out that additional factors also played a part.", ["c1-modal-distancing"]),
                dc("dialogue", [
                    {"speaker": "Recenzens", "text": "Minden fenntartás nélkül elfogadhatjuk az elméletet?"},
                    {"speaker": "Tudós", "text": "Semmiképp sem; csak azzal a kikötéssel, ha a tesztek megismételhetők."},
                ], ["azzal a kikötéssel", "vak hittel", "habozás nélkül"], 0, ["c1-modal-distancing"]),
                sw("production", [{"prompt": "Write a cautious statement using 'Nem zárható ki, hogy'.", "answer": "Nem zárható ki, hogy a gazdasági mutatók a vártnál lassabban javulnak."}], ["c1-modal-distancing"]),
                mc("grammar", "check", "Melyik stíluserény óv meg a tudományos túláltalánosítástól?", [
                    "A mértéktartás és a módszertani fenntartások világos megfogalmazása.",
                    "A hangzatos szlogenek ismételgetése.",
                    "A statisztikai adatok teljes mellőzése."
                ], 0, ["c1-modal-distancing"])
            ]
        },
        {
            "num": 4,
            "stem": "c1-03-04",
            "title": "Subtle Epistemic Adverbs: Némiképp, Látszólag, and Mindeddig",
            "grammar_title": "Qualifying Adverbs in Fine Analytical Distinctions",
            "grammar_skill": "c1-epistemic-hedging",
            "goals": [
                "I can employ qualifying adverbs (*némiképp, némileg, látszólag, mindeddig*).",
                "I can contrast superficial appearance (*látszólag*) with structural reality.",
                "I can indicate temporal boundaries of current knowledge using *mindeddig*."
            ],
            "vocab": [
                {"lemma": "némiképp", "translation": "somewhat, to some extent", "pos": "adverb"},
                {"lemma": "látszólag", "translation": "seemingly, apparently", "pos": "adverb"},
                {"lemma": "mindeddig", "translation": "until now, hitherto", "pos": "adverb"},
                {"lemma": "jóformán", "translation": "practically, virtually, almost", "pos": "adverb"},
                {"lemma": "felszínes", "translation": "superficial", "pos": "adjective"},
                {"lemma": "megtévesztő", "translation": "deceptive, misleading", "pos": "adjective"},
                {"lemma": "alátámasztás", "translation": "corroboration, substantiation", "pos": "noun"},
                {"lemma": "tisztázatlan", "translation": "unclarified, obscure", "pos": "adjective"}
            ],
            "gr_text1": "*Látszólag* (seemingly / ostensibly) prepares the reader for an antithesis between appearance and substance: *A rendszer látszólag stabil volt, ám a mélyben súlyos feszültségek húzódtak.*",
            "gr_text2": "*Mindeddig* restricts validity to the present state of evidence without making timeless claims: *A mindeddig felgyűlt bizonyítékok alátámasztják a tételt.*",
            "gr_table": [
                ["Látszólag ellentmondásos helyzet...", "A seemingly contradictory situation..."],
                ["Mindeddig tisztázatlan körülmények...", "Circumstances hitherto unclarified..."],
                ["Némiképp eltér a megszokottól.", "It differs somewhat from the usual."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Milyen funkciót tölt be a 'látszólag' határozószó a mondatban?", ["Jelzi, hogy a külső látszat eltér a mélyebb valóságtól.", "Bizonyítja a tények megkérdőjelezhetetlenségét.", "Időbeli sietséget fejez ki."], 0, ["c1-03-vocab"]),
                fb("grammar", "controlled", "A jelenség _____ ellentmond a fizika törvényeinek, ám valójában egy ritka kölcsönhatásról van szó. (seemingly / látszólag)", "látszólag", "The phenomenon seemingly contradicts the laws of physics, but in reality it is about a rare interaction.", ["c1-epistemic-hedging"]),
                match("vocabulary", "controlled", [["némiképp", "somewhat"], ["látszólag", "seemingly"], ["mindeddig", "until now / hitherto"], ["jóformán", "practically / virtually"]], ["c1-03-vocab"]),
                fb("grammar", "practice", "A kutatás eredményei _____ megváltoztatják a korábbi elméleti modellt. (somewhat / némiképp)", "némiképp", "The research results somewhat change the earlier theoretical model.", ["c1-epistemic-hedging"]),
                sb("grammar", "practice", ["A", "kérdés", "mindezidáig", "tisztázatlan", "maradt", "a", "szakirodalomban."], ["A", "kérdés", "mindezidáig", "tisztázatlan", "maradt", "a", "szakirodalomban."], "The question has remained unclarified hitherto in the specialized literature.", ["c1-epistemic-hedging"]),
                dc("dialogue", [
                    {"speaker": "Kutató", "text": "Megbízhatunk a mérési adatokban?"},
                    {"speaker": "Asszisztens", "text": "Látszólag minden rendben van, de érdemes újra kalibrálni a műszert."},
                ], ["Látszólag minden rendben van", "Biztosan minden rossz", "Soha nem volt jó"], 0, ["c1-epistemic-hedging"]),
                sw("production", [{"prompt": "Write a contrastive sentence using 'Látszólag..., ám a valóságban...'.", "answer": "Látszólag békés volt a helyzet, ám a valóságban komoly nézeteltérések feszültek a felek között."}], ["c1-epistemic-hedging"]),
                mc("grammar", "check", "Melyik kifejezés korlátozza időben a jelenlegi tudás érvényességét?", [
                    "A mindeddig rendelkezésre álló adatok",
                    "Az örökké érvényes igazságok",
                    "A vitathatatlan jövőbeli tények"
                ], 0, ["c1-epistemic-hedging"])
            ]
        },
        {
            "num": 5,
            "stem": "c1-03-05",
            "title": "Epistemic Caution in Scholarly Prose: Szerb Antal",
            "grammar_title": "Scholarly Distance and Irony in Biographical Reflection",
            "grammar_skill": "c1-modal-distancing",
            "goals": [
                "I can analyze Antal Szerb's epistemic modesty in 'A varázsló eltűnik'.",
                "I can observe how irony dissolves scholarly arrogance.",
                "I can read biographical and historical portraits written with C1 stylistic elegance."
            ],
            "vocab": [
                {"lemma": "tudósi alázat", "translation": "scholarly humility", "pos": "noun"},
                {"lemma": "kételkedés", "translation": "skepticism, doubting", "pos": "noun"},
                {"lemma": "esendőség", "translation": "frailty, fallibility", "pos": "noun"},
                {"lemma": "megkérdőjelez", "translation": "to call into question, doubt", "pos": "verb"},
                {"lemma": "távolságtartás", "translation": "detachment, keeping distance", "pos": "noun"},
                {"lemma": "ítéletalkotás", "translation": "judgment formation, passing judgment", "pos": "noun"},
                {"lemma": "óvatos", "translation": "cautious, discreet", "pos": "adjective"},
                {"lemma": "tévedhetetlenség", "translation": "infallibility", "pos": "noun"}
            ],
            "gr_text1": "Antal Szerb's historical essays demonstrate that true wisdom lies in renouncing the illusion of infallibility (*tévedhetetlenség*). His writing employs profound scholarly humility (*tudósi alázat*), questioning sweeping claims and highlighting the frailties of human nature.",
            "gr_text2": "Scholarly distancing in this tradition is achieved by replacing grand assertions with interrogatives, tentative modals, and gentle smiles: *Biztosak lehetünk-e ebben? Aligha. De talán éppen a bizonytalanság teszi széppé a keresést.*",
            "gr_table": [
                ["A tudósi alázat és a kételkedés erénye...", "The virtue of scholarly humility and skepticism..."],
                ["Tartózkodunk a végleges ítéletalkotástól...", "We refrain from passing definitive judgment..."],
                ["Az emberi természet esendősége...", "The frailty of human nature..."]
            ],
            "classic_story": {
                "slug": "c1-03-szerb",
                "author": "Szerb Antal",
                "work": "A varázsló eltűnik (1940)",
                "title": "A kételkedés dicsérete és az emberi esendőség",
                "summary": "Antal Szerb reflections on intellectual modesty, exploring why dogmatic certainty blinds scholars while gentle skepticism illuminates human history.",
                "characters": ["Szerb Antal"],
                "paragraphs": [
                    {"type": "narration", "text": "Amikor Szerb Antal A varázsló eltűnik című kötetének lapjain a múlt nagy alakjairól és letűnt korok különceiről írt, a legfőbb fegyvere nem a tekintélyelvű tudományos ítélkezés volt, hanem a szelíd, megértő kételkedés. Úgy vélte, a történész legveszélyesebb kísértése az a gőg, amellyel a jelen embere utólag mindentudónak képzeli magát."},
                    {"type": "narration", "text": "A múltban élt emberek nem absztrakt elméletek illusztrációi voltak, hanem hús-vér, esendő lények, akik éppúgy tévedtek, reménykedtek és csalódtak, mint mi magunk. Ezért a hiteles tudós nem osztogat fekete és fehér bizonyítványokat. Inkább óvatosan közelít a forrásokhoz, tudván, hogy az igazság ritkán mutatkozik meg harsány kinyilatkoztatásokban."},
                    {"type": "narration", "text": "Szerb Antal iróniája nem gúnyolódás volt, hanem a szeretet és a tisztánlátás legmagasabb formája: annak a felismerése, hogy az emberi törekvésekben a nagyszerű és a nevetséges elválaszthatatlanul összefonódik. Aki megtanul kételkedni a saját tévedhetetlenségében, az nyerheti el a valódi intellektuális szabadságot."},
                    {"type": "narration", "text": "A tudósi alázat nem gyengeség, hanem erő. Megtanít arra, hogy a kérdezés gyakran értékesebb a kész válasznál, és hogy a világ sokkal gazdagabb annál, semhogy beleférne bármilyen merev dogmatikus rendszerbe."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Mit jelent a 'tudósi alázat' Szerb Antal felfogásában?", ["A tévedhetetlenség gőgjének elvetését és a források tiszteletteljes, óvatos megközelítését.", "A vélemény teljes hiányát.", "A könyvek olvasásának feladását."], 0, ["c1-03-vocab"]),
                fb("grammar", "practice", "A kutató tartózkodott az elhamarkodott _____ megfogalmazásától. (passing judgment / ítéletalkotástól)", "ítéletalkotástól", "The researcher refrained from formulating hasty judgments.", ["c1-modal-distancing"]),
                match("vocabulary", "controlled", [["tudósi alázat", "scholarly humility"], ["kételkedés", "skepticism"], ["esendőség", "frailty"], ["tévedhetetlenség", "infallibility"]], ["c1-03-vocab"]),
                mc("reading", "practice", "Mi a történész legveszélyesebb kísértése Szerb Antal szerint?", [
                    "Az utólagos mindentudás gőgje és a tekintélyelvű ítélkezés.",
                    "A levéltárak poros levegője.",
                    "A túl sok idegen nyelv ismerete."
                ], 0, None),
                mc("reading", "practice", "Milyen funkciót tölt be az irónia Szerb Antal esszéiben a szöveg szerint?", [
                    "A szeretet és a tisztánlátás formája, amely felismeri a nagyszerű és a nevetséges összefonódását.",
                    "Az ellenfelek kíméletlen megsemmisítését szolgálja.",
                    "Felszínes tréfa a lapok megtöltésére."
                ], 0, None),
                sb("grammar", "practice", ["A", "kérdezés", "gyakran", "értékesebb", "a", "kész", "tudományos", "válasszal."], ["A", "kérdezés", "gyakran", "értékesebb", "a", "kész", "tudományos", "válasszal."], "Questioning is often more valuable than ready scientific answers.", ["c1-modal-distancing"]),
                sw("production", [{"prompt": "Write a reflection on intellectual humility.", "answer": "A valódi tudomány a kételkedés bátorságán és az esendőség beismerésén alapul."}], ["c1-modal-distancing"]),
                mc("grammar", "check", "Melyik magatartás fejezi ki a legmagasabb intellektuális érettséget?", [
                    "A tévedhetetlenség illúziójának elvetése és a nyitott kérdezés.",
                    "A saját igazunk mindenáron való erőltetése.",
                    "Más tudósok véleményének figyelmen kívül hagyása."
                ], 0, ["c1-modal-distancing"])
            ]
        }
    ]

    for l in core_lessons:
        emit_instructional_lesson(3, "core", l, core_title, core_intro if l["num"] == 1 else None)

    # Core Consolidation
    emit_consolidation_lesson(
        3,
        "core",
        "c1-03-consolidation",
        core_title,
        [
            "I can deploy evidentiality markers and citations with academic precision.",
            "I can calibrate probabilities using 'aligha', 'minden bizonnyal', and 'feltehetőleg'.",
            "I can formulate prudent hypotheses and modal reservations."
        ],
        [
            mc("grammar", "recognize", "Melyik mondat fejez ki elegáns tudományos kételkedést?", [
                "Aligha feltételezhető, hogy a modell minden körülmények között érvényes marad.",
                "Ez a modell teljesen rossz és haszontalan.",
                "Biztos vagyok benne, hogy senki sem ért hozzá."
            ], 0, ["c1-epistemic-hedging"]),
            mc("grammar", "recognize", "Milyen funkciót tölt be a 'források tanúsága szerint' fordulat?", [
                "A közölt adat dokumentáris megalapozottságát és hatókörét jelöli meg.",
                "Csupán egy szóismétlést küszöböl ki.",
                "Feltételes kívánságot fejez ki."
            ], 0, ["c1-evidentiality-markers"]),
            match("vocabulary", "recognize", [["aligha", "hardly"], ["minden bizonnyal", "in all probability"], ["nem zárható ki", "cannot be excluded"], ["látszólag", "seemingly"], ["tudósi alázat", "scholarly humility"]], ["c1-03-vocab"]),
            fb("vocabulary", "recall", "A kísérlet eredményei _____ támasztják alá a kutatók hipotézisét. (in all probability / minden bizonnyal)", "minden bizonnyal", "The results of the experiment in all probability corroborate the researchers' hypothesis.", ["c1-03-vocab"]),
            fb("vocabulary", "recall", "A történész tartózkodott a végleges _____ megfogalmazásától. (judgment / ítélet)", "ítélet", "The historian refrained from formulating a definitive judgment.", ["c1-03-vocab"]),
            fb("grammar", "recall", "Nem _____ ki, hogy a dokumentumok egy része megsemmisült a háborúban. (cannot be ruled out / zárható)", "zárható", "It cannot be ruled out that part of the documents was destroyed in the war.", ["c1-modal-distancing"]),
            fb("grammar", "context", "A helyzet _____ stabilnak tűnt, ám a mélyben feszültségek húzódtak. (seemingly / látszólag)", "látszólag", "The situation seemingly appeared stable, but tensions lay beneath the surface.", ["c1-epistemic-hedging"]),
            fb("grammar", "context", "A korabeli levelezések _____ szerint a két gondolkodó nem értett egyet. (testimony of / tanúsága)", "tanúsága", "According to the testimony of contemporary correspondences, the two thinkers did not agree.", ["c1-evidentiality-markers"]),
            mc("grammar", "context", "Mi a különbség a 'bizonyára' és az 'aligha' között?", [
                "A 'bizonyára' magas valószínűséget, az 'aligha' kifejezetten alacsony valószínűséget jelez.",
                "Nincs köztük semmi különbség.",
                "Az 'aligha' csak a múlt időben használható."
            ], 0, ["c1-epistemic-hedging"]),
            sb("grammar", "produce", ["A", "tudományos", "haladás", "a", "kételkedés", "bátorságán", "alapul."], ["A", "tudományos", "haladás", "a", "kételkedés", "bátorságán", "alapul."], "Scientific progress is based on the courage of doubting.", ["c1-modal-distancing"]),
            sw("production", [{"prompt": "Write a hedged conclusion using 'Nem zárható ki, hogy' and 'aligha'.", "answer": "Nem zárható ki, hogy a modell hiányos, ám aligha vitatható az elméleti jelentősége."}], ["c1-modal-distancing"]),
            sw("production", [{"prompt": "Formulate a cautious evidentiary remark using 'A források tanúsága szerint'.", "answer": "A források tanúsága szerint a kézirat eredetisége mindeddig vitatott maradt."}], ["c1-evidentiality-markers"])
        ]
    )

    # ----------------------------------------------------
    # TRACK 2: DISCOURSE (c1-tudomanyelmelet)
    # ----------------------------------------------------
    slug = "tudomanyelmelet"
    disc_title = "Epistemology & Scientific Paradigm Shifts"
    disc_intro = [
        "How do scientific revolutions occur? Is scientific truth absolute and detached from human consciousness, or is knowledge always embedded in tacit commitments, paradigm shifts, and institutional dynamics?",
        "In this unit, you will explore Hungarian contributions to the philosophy of science: Michael Polanyi's theory of 'Personal Knowledge', Imre Lakatos's methodology of scientific research programmes, John von Neumann's cybernetic revolution, and 21st-century bioethics."
    ]

    disc_lessons = [
        {
            "num": 1,
            "stem": f"c1-{slug}-01",
            "title": "Tacit Knowledge: Michael Polanyi and Personal Knowing",
            "grammar_title": "Epistemology of Tacit Knowing and Scientific Commitment",
            "grammar_skill": "c1-scientific-paradigm-discourse",
            "goals": [
                "I can analyze Michael Polanyi's concept of 'tacit knowledge' (*hallgatólagos tudás*).",
                "I can discuss how subjective commitment and craftsmanship underpin scientific objectivity.",
                "I can use high-register epistemological vocabulary in Hungarian."
            ],
            "vocab": [
                {"lemma": "hallgatólagos tudás", "translation": "tacit knowledge", "pos": "expression"},
                {"lemma": "ismeretelmélet", "translation": "epistemology, theory of knowledge", "pos": "noun"},
                {"lemma": "személyes tudás", "translation": "personal knowledge", "pos": "noun"},
                {"lemma": "elköteleződés", "translation": "commitment, engagement", "pos": "noun"},
                {"lemma": "készség", "translation": "skill, knack, craftsmanship", "pos": "noun"},
                {"lemma": "kifejezhetetlen", "translation": "inexpressible, ineffable", "pos": "adjective"},
                {"lemma": "objektivizmus", "translation": "objectivism", "pos": "noun"},
                {"lemma": "tudósközösség", "translation": "scientific community", "pos": "noun"}
            ],
            "gr_text1": "Michael Polányi (Polányi Mihály) overturned the positivist dogma that science is purely impersonal and algorithmic. His famous maxim – 'we know more than we can tell' (*többet tudunk, mint amennyit el tudunk mondani*) – highlights the central role of *hallgatólagos tudás* (tacit knowledge).",
            "gr_text2": "When discussing epistemology, abstract verbal compounds and nominal predicates describe cognitive processes: *A tudományos megismerés nem pusztán szabálykövetés, hanem a személyes elköteleződés és a mesterségbeli tudás egysége.*",
            "gr_table": [
                ["A hallgatólagos tudás szerepe a megismerésben...", "The role of tacit knowledge in cognition..."],
                ["Többet tudunk, mint amennyit ki tudunk fejezni.", "We know more than we can express."],
                ["A tudósközösség konszenzusa és hagyománya...", "The consensus and tradition of the scientific community..."]
            ],
            "world_story_seg": {
                "seg_slug": "polanyi",
                "title": "Polányi Mihály és a személyes tudás forradalma",
                "summary": "How physical chemist and philosopher Michael Polanyi revealed that all human knowledge rests on personal commitment and tacit skills.",
                "paragraphs": [
                    {"type": "narration", "text": "A huszadik század derekán a tudományfilozófiát a pozitivizmus hűvös dogmája uralta: az az elképzelés, hogy a valódi tudomány teljesen független az embertől, és nem egyéb, mint személytelen adatok és matematikai algoritmusok mechanikus összessége. Ezzel a rideg mítosszal szállt szembe a magyar származású Polányi Mihály."},
                    {"type": "narration", "text": "Polányi rámutatott, hogy a legbonyolultabb laboratóriumi kísérlet mögött is ott rejtőzik az emberi tényező: a kutató mesterségbeli intuíciója, az ujjai hegyében lévő tapasztalat és a szellemi elköteleződés. Megalkotta a 'hallgatólagos tudás' (tacit knowledge) fogalmát: többet tudunk, mint amennyit szavakkal képesek vagyunk kifejezni. Ahogyan egy művész sem tudja kottára tenni zsenialitásának minden rezdülését, úgy a tudós sem redukálható merev szabálygyűjteményre."},
                    {"type": "narration", "text": "Polányi szerint az objektivizmus illúziója valójában veszélyezteti a szabadságot. Ha elhisszük, hogy a tudomány gépies igazság, elfelejtjük, hogy a tudományos közösség morális felelősségre, kölcsönös bizalomra és a szabad keresés hagyományára épül."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Mit jelent a 'hallgatólagos tudás' (tacit knowledge) Polányi Mihály elméletében?", [
                    "Azt a nem verbalizálható, tapasztalati és intuitív tudást, amely minden cselekvésünk és megismerésünk alapja.",
                    "A titkos katonai információkat.",
                    "A könyvtárakban lévő kiadatlan kéziratokat."
                ], 0, ["c1-tudomanyelmelet-vocab"]),
                fb("grammar", "practice", "Polányi szerint a tudományos megismerés elválaszthatatlan a kutató személyes erkölcsi és intellektuális _____. (commitment / elköteleződésétől)", "elköteleződésétől", "According to Polanyi, scientific cognition is inseparable from the researcher's personal moral and intellectual commitment.", ["c1-scientific-paradigm-discourse"]),
                match("vocabulary", "controlled", [["hallgatólagos tudás", "tacit knowledge"], ["ismeretelmélet", "epistemology"], ["elköteleződés", "commitment"], ["objektivizmus", "objectivism"]], ["c1-tudomanyelmelet-vocab"]),
                sb("grammar", "practice", ["Többet", "tudunk,", "mint", "amennyit", "szavakkal", "ki", "tudunk", "fejezni."], ["Többet", "tudunk,", "mint", "amennyit", "szavakkal", "ki", "tudunk", "fejezni."], "We know more than we can express with words.", ["c1-scientific-paradigm-discourse"]),
                dc("dialogue", [
                    {"speaker": "Hallgató", "text": "Helyettesítheti a mesterséges intelligencia a kutatói intuíciót?"},
                    {"speaker": "Professzor", "text": "Aligha; a hallgatólagos tudás és a morális felelősség emberi sajátosság."},
                ], ["hallgatólagos tudás", "merev algoritmus", "adatvesztés"], 0, ["c1-scientific-paradigm-discourse"]),
                sw("production", [{"prompt": "Write an epistemological assertion summarizing Polanyi's view.", "answer": "A tudományos objektivitás nem a személytelenségben, hanem a tudósközösség morális elköteleződésében gyökerezik."}], ["c1-scientific-paradigm-discourse"]),
                mc("grammar", "check", "Melyik állítás tükrözi Polányi Mihály ismeretelméletét?", [
                    "Minden tudás személyes tudás, amely a gyakorlati mesterségbeli készségeken alapul.",
                    "A tudomány kizárólag mechanikus adatgyűjtésből áll.",
                    "A szubjektív tapasztalatnak semmi helye nincs a laboratóriumban."
                ], 0, ["c1-scientific-paradigm-discourse"])
            ]
        },
        {
            "num": 2,
            "stem": f"c1-{slug}-02",
            "title": "Research Programmes: Imre Lakatos and Methodology",
            "grammar_title": "Methodology of Scientific Research Programmes: Core and Protective Belt",
            "grammar_skill": "c1-scientific-paradigm-discourse",
            "goals": [
                "I can analyze Imre Lakatos's methodology of scientific research programmes.",
                "I can understand concepts like 'hard core' (*kemény mag*) and 'protective belt' (*védőöv*).",
                "I can evaluate progressive versus degenerating problemshifts in scientific history."
            ],
            "vocab": [
                {"lemma": "kutatási program", "translation": "research programme", "pos": "noun"},
                {"lemma": "kemény mag", "translation": "hard core (of a theory)", "pos": "noun"},
                {"lemma": "védőöv", "translation": "protective belt (auxiliary hypotheses)", "pos": "noun"},
                {"lemma": "paradigmaváltás", "translation": "paradigm shift", "pos": "noun"},
                {"lemma": "cáfolat", "translation": "refutation, falsification", "pos": "noun"},
                {"lemma": "progresszív", "translation": "progressive (generating novel facts)", "pos": "adjective"},
                {"lemma": "degenerálódó", "translation": "degenerating (ad hoc modifications)", "pos": "adjective"},
                {"lemma": "heurisztika", "translation": "heuristics", "pos": "noun"}
            ],
            "gr_text1": "Imre Lakatos synthesized Karl Popper's falsificationism and Thomas Kuhn's paradigm shifts. He argued that scientists do not abandon a theory at the first anomaly; rather, theories form *kutatási programok* consisting of a non-negotiable *kemény mag* surrounded by a malleable *védőöv* of auxiliary hypotheses.",
            "gr_text2": "When a program predicts novel unexpected facts, it is *progresszív*; when it merely invents ad hoc excuses to survive counter-evidence, it becomes *degenerálódó*.",
            "gr_table": [
                ["A kutatási program kemény magja...", "The hard core of the research programme..."],
                ["A segédhipotézisek védőöve...", "The protective belt of auxiliary hypotheses..."],
                ["Progresszív vagy degenerálódó elméleti elmozdulás...", "Progressive or degenerating theoretical problemshift..."]
            ],
            "world_story_seg": {
                "seg_slug": "lakatos",
                "title": "Lakatos Imre és a kutatási programok logikája",
                "summary": "How philosopher of science Imre Lakatos resolved the clash between Popper and Kuhn by analyzing the rational growth of scientific knowledge.",
                "paragraphs": [
                    {"type": "narration", "text": "Amikor Karl Popper azt állította, hogy egyetlen cáfoló kísérlet képes megdönteni egy tudományos elméletet, Thomas Kuhn pedig azzal válaszolt, hogy a tudósok irracionális hittel ragaszkodnak paradigmáikhoz, a tudományfilozófia mély válságba jutott. A vitát a magyar származású Lakatos Imre oldotta fel ragyogó kompromisszumával."},
                    {"type": "narration", "text": "Lakatos felismerte, hogy a tudomány története nem elszigetelt elméletek, hanem hosszan tartó 'tudományos kutatási programok' küzdelme. Minden ilyen programnak van egy érinthetetlen 'kemény magja' (hard core), amelyet a kutatók nem engednek megdönteni, és egy rugalmas 'védőöve' (protective belt), amely segédhipotézisekkel felfogja a kísérleti anomáliákat."},
                    {"type": "narration", "text": "Egy elméletet nem a cáfolat öl meg, hanem egy jobb elmélet megjelenése. Ha egy program képes új, váratlan tényeket megjósolni, akkor haladó (progresszív); ha csupán utólagos magyarázatokkal mentegeti kudarcait, akkor hanyatló (degenerálódó). Lakatos ezzel megmentette a tudományos fejlődés racionalitását."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Mi a szerepe a 'védőövnek' (protective belt) Lakatos Imre elméletében?", [
                    "Segédhipotézisekkel felfogja a cáfolatokat és védi a program kemény magját.",
                    "A kutatók fizikai biztonságát védi a laboratóriumban.",
                    "A pénzügyi támogatások elosztását szabályozza."
                ], 0, ["c1-tudomanyelmelet-vocab"]),
                fb("grammar", "practice", "Egy kutatási program mindaddig _____ marad, amíg képes új, korábban ismeretlen tényeket előrejelezni. (progressive / progresszív)", "progresszív", "A research programme remains progressive as long as it is capable of predicting new, previously unknown facts.", ["c1-scientific-paradigm-discourse"]),
                match("vocabulary", "controlled", [["kemény mag", "hard core"], ["védőöv", "protective belt"], ["paradigmaváltás", "paradigm shift"], ["heurisztika", "heuristics"]], ["c1-tudomanyelmelet-vocab"]),
                sb("grammar", "practice", ["A", "tudományos", "elméleteket", "csak", "egy", "jobb", "elmélet", "képes", "felváltani."], ["A", "tudományos", "elméleteket", "csak", "egy", "jobb", "elmélet", "képes", "felváltani."], "Scientific theories can only be replaced by a better theory.", ["c1-scientific-paradigm-discourse"]),
                dc("dialogue", [
                    {"speaker": "Doktorandusz", "text": "Fel kell adnunk a hipotézist a sikertelen kísérlet miatt?"},
                    {"speaker": "Témavezető", "text": "Nem feltétlenül; először vizsgáljuk meg a védőöv segédhipotéziseit."},
                ], ["védőöv segédhipotéziseit", "azonnali feladását", "teljes tagadását"], 0, ["c1-scientific-paradigm-discourse"]),
                sw("production", [{"prompt": "Write a sentence contrasting a progressive and a degenerating research program.", "answer": "Míg a progresszív program új felfedezésekhez vezet, a degenerálódó elmélet csupán ad hoc mentegetőzésekbe bonyolódik."}], ["c1-scientific-paradigm-discourse"]),
                mc("grammar", "check", "Melyik fogalom köthető Lakatos Imre nevéhez a tudományfilozófiában?", [
                    "A tudományos kutatási programok metodológiája.",
                    "A pszichoanalitikus tudattalan elmélete.",
                    "A szubjektív idealizmus doktrínája."
                ], 0, ["c1-scientific-paradigm-discourse"])
            ]
        },
        {
            "num": 3,
            "stem": f"c1-{slug}-03",
            "title": "Cybernetics and Complexity: John von Neumann",
            "grammar_title": "Information Theory, Algorithmic Epistemology, and Artificial Thought",
            "grammar_skill": "c1-epistemic-skepticism",
            "goals": [
                "I can discuss John von Neumann's (Neumann János) revolutionary contributions to computing and cybernetics.",
                "I can analyze the philosophical implications of algorithmic thought and artificial automata.",
                "I can formulate critical questions regarding computation and human intelligence."
            ],
            "vocab": [
                {"lemma": "kibernetika", "translation": "cybernetics", "pos": "noun"},
                {"lemma": "algoritmikus", "translation": "algorithmic", "pos": "adjective"},
                {"lemma": "öntanuló", "translation": "self-learning", "pos": "adjective"},
                {"lemma": "játékelmélet", "translation": "game theory", "pos": "noun"},
                {"lemma": "számítási kapacitás", "translation": "computational capacity", "pos": "noun"},
                {"lemma": "architektúra", "translation": "architecture (computing)", "pos": "noun"},
                {"lemma": "mesterséges intelligencia", "translation": "artificial intelligence", "pos": "noun"},
                {"lemma": "döntéselmélet", "translation": "decision theory", "pos": "noun"}
            ],
            "gr_text1": "John von Neumann created the foundational architecture of modern computing and co-founded game theory (*játékelmélet*). His philosophical inquiry in 'The Computer and the Brain' compared the digital automaton with the electrochemical complexity of the human central nervous system.",
            "gr_text2": "Discussing algorithmic epistemology requires balancing technological optimism with skepticism (*kritikai távolságtartás*): *Vajon a számítási kapacitás növekedése elvezethet-e a valódi öntudat megszületéséhez?*",
            "gr_table": [
                ["A Neumann-architektúra alapelvei...", "The fundamental principles of the von Neumann architecture..."],
                ["Játékelmélet és racionális döntéshozatal...", "Game theory and rational decision-making..."],
                ["Az emberi agy és a digitális automata összevetése...", "Comparing the human brain and the digital automaton..."]
            ],
            "world_story_seg": {
                "seg_slug": "neumann",
                "title": "Neumann János és a gépi gondolkodás hajnala",
                "summary": "How polymath John von Neumann laid the mathematical foundations for digital computers, game theory, and modern cybernetics.",
                "paragraphs": [
                    {"type": "narration", "text": "Amikor Neumann János a huszadik század negyvenes éveiben megalkotta a tárolt programú számítógép elvét – amelyet a világ azóta is Neumann-architektúraként ismer –, nem egyszerűen egy új számológépet tervezett. Egy olyan egyetemes információfeldolgozó gépezetet hozott létre, amely átformálta az emberi civilizáció teljes alapját."},
                    {"type": "narration", "text": "Neumann zsenialitása nem ismert határokat. A kvantummechanika matematikai alapjaitól a játékelméleten át az önreprodukáló automaták elméletéig a legelvontabb struktúrákban látta meg a rendet. Utolsó, befejezetlen művében – A számítógép és az agy – már azt a kérdést vizsgálta, miben különbözik a digitális áramkörök logikája az emberi idegrendszer analóg, rugalmas és hibatűrő működésétől."},
                    {"type": "narration", "text": "Pontosan látta az emberiség előtt álló gigantikus dilemmákat: a technológiai fejlődés exponenciális gyorsulása előbb-utóbb olyan pontra érkezik – a technológiai szingularitáshoz –, amely után az emberi történelem már nem folytatható a korábbi formájában."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Mi az a 'Neumann-architektúra' a számítástechnikában?", [
                    "A tárolt programú számítógép alapelve, ahol a program és az adat ugyanabban a memóriában helyezkedik el.",
                    "Egy budapesti lakóház építészeti stílusa.",
                    "A kézi számológépek mechanikus alkatrésze."
                ], 0, ["c1-tudomanyelmelet-vocab"]),
                fb("grammar", "practice", "Neumann játékelmélete forradalmasította a modern közgazdaságtant és a stratégiai _____ folyamatát. (decision-making / döntéshozatal)", "döntéshozatal", "Neumann's game theory revolutionized modern economics and the process of strategic decision-making.", ["c1-epistemic-skepticism"]),
                match("vocabulary", "controlled", [["kibernetika", "cybernetics"], ["játékelmélet", "game theory"], ["architektúra", "architecture"], ["öntanuló", "self-learning"]], ["c1-tudomanyelmelet-vocab"]),
                sb("grammar", "practice", ["Neumann", "megalapozta", "a", "modern", "digitális", "korszak", "matematikai", "alapjait."], ["Neumann", "megalapozta", "a", "modern", "digitális", "korszak", "matematikai", "alapjait."], "Neumann established the mathematical foundations of the modern digital era.", ["c1-epistemic-skepticism"]),
                dc("dialogue", [
                    {"speaker": "Informatikus", "text": "Képesek a modern gépek túlszárnyalni az emberi agyat?"},
                    {"speaker": "Filozófus", "text": "Számítási kapacitásban igen, ám a jelentésadás és öntudat terén még messze vagyunk ettől."},
                ], ["számítási kapacitásban", "minden területen", "egyikben sem"], 0, ["c1-epistemic-skepticism"]),
                sw("production", [{"prompt": "Write a reflection on von Neumann's visionary warning about technological acceleration.", "answer": "Neumann felismerte, hogy a technológiai fejlődés sebessége túllépheti az emberiség erkölcsi alkalmazkodóképességét."}], ["c1-epistemic-skepticism"]),
                mc("grammar", "check", "Melyik tudományterület megalapozása NEM köthető közvetlenül Neumann Jánoshoz?", [
                    "A freudi pszichoanalízis.",
                    "A játékelmélet.",
                    "A digitális számítógépek architektúrája."
                ], 0, ["c1-epistemic-skepticism"])
            ]
        },
        {
            "num": 4,
            "stem": f"c1-{slug}-04",
            "title": "The Illusion of Pure Objectivity: The Human Factor",
            "grammar_title": "Critical Epistemology and Socio-Historical Contingency",
            "grammar_skill": "c1-epistemic-skepticism",
            "goals": [
                "I can critically evaluate the myth of absolute value-free scientific objectivity.",
                "I can analyze how social, economic, and political factors shape scientific agendas.",
                "I can discuss scientific reflexivity in Hungarian."
            ],
            "vocab": [
                {"lemma": "tárgyilagosság", "translation": "objectivity, impartiality", "pos": "noun"},
                {"lemma": "értékmentes", "translation": "value-free, axiologically neutral", "pos": "adjective"},
                {"lemma": "viszonylagosság", "translation": "relativity, contingency", "pos": "noun"},
                {"lemma": "társadalmi beágyazottság", "translation": "social embeddedness", "pos": "expression"},
                {"lemma": "reflexivitás", "translation": "reflexivity", "pos": "noun"},
                {"lemma": "tudásszociológia", "translation": "sociology of knowledge", "pos": "noun"},
                {"lemma": "elfogultság", "translation": "bias, prejudice", "pos": "noun"},
                {"lemma": "tudományos konszenzus", "translation": "scientific consensus", "pos": "noun"}
            ],
            "gr_text1": "The sociology of knowledge (*tudásszociológia*) demonstrated that scientific research is never completely value-free (*értékmentes*). What problems get funded, what methodologies are deemed respectable, and how anomalies are dismissed reflect the social embeddedness (*társadalmi beágyazottság*) of science.",
            "gr_text2": "Critical epistemological essays frame these caveats using concessive balance: *Jóllehet a természettudományok egyetemes törvényekre törekszenek, maguk a kutatók koruk társadalmi koordinátarendszerében mozognak.*",
            "gr_table": [
                ["A tisztán értékmentes tudomány illúziója...", "The illusion of purely value-free science..."],
                ["A tudományos konszenzus társadalmi beágyazottsága...", "The social embeddedness of scientific consensus..."],
                ["Kritikai reflexivitás a kutatásban...", "Critical reflexivity in research..."]
            ],
            "world_story_seg": {
                "seg_slug": "objektivitas",
                "title": "Az abszolút objektivitás illúziója",
                "summary": "How modern sociology of knowledge revealed the human, cultural, and institutional dimensions behind scientific consensus.",
                "paragraphs": [
                    {"type": "narration", "text": "Hosszú évszázadokon át tartotta magát az a felvilágosult mítosz, hogy a természettudós olyan, mint egy tiszta tükör: semlegesen, érzelmektől és társadalmi érdekektől mentesen veri vissza a természet objektív valóságát. A huszadik század tudásszociológiája azonban könyörtelenül leleplezte ezt az illúziót."},
                    {"type": "narration", "text": "A tudomány nem légüres térben létezik. Az, hogy egy társadalomban milyen kutatásokat finanszíroznak, milyen kérdéseket tekintenek tudományosnak, és milyen válaszokat rekesztenek ki mint eretnekséget, mélyen beágyazódik a politikai, gazdasági és kulturális hatalmi viszonyokba. A tudományos konszenzus nem kőbe vésett örök törvény, hanem szüntelen vitákban formálódó emberi megállapodás."},
                    {"type": "narration", "text": "Ez a felismerés azonban nem vezethet cinikus relativizmushoz. A valódi tudományos nagyság éppen a reflexivitásban rejlik: abban a képességben, hogy a kutató felismeri saját elfogultságait és korlátait, és mindezek dacára törekszik a lehető legpontosabb igazság felmutatására."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Mit vizsgál a tudásszociológia?", [
                    "Azt, hogy a társadalmi, gazdasági és hatalmi viszonyok hogyan befolyásolják a tudás és a tudomány alakulását.",
                    "A laboratóriumi vegyszerek összetételét.",
                    "A tudósok fizetésének adózását."
                ], 0, ["c1-tudomanyelmelet-vocab"]),
                fb("grammar", "practice", "A modern ismeretelmélet szerint a tisztán _____ tudomány eszméje elérhetetlen ideál. (value-free / értékmentes)", "értékmentes", "According to modern epistemology, the ideal of purely value-free science is an unattainable ideal.", ["c1-epistemic-skepticism"]),
                match("vocabulary", "controlled", [["tárgyilagosság", "objectivity"], ["értékmentes", "value-free"], ["reflexivitás", "reflexivity"], ["tudásszociológia", "sociology of knowledge"]], ["c1-tudomanyelmelet-vocab"]),
                sb("grammar", "practice", ["A", "tudományos", "kutatás", "sosem", "független", "a", "társadalmi", "kontextustól."], ["A", "tudományos", "kutatás", "sosem", "független", "a", "társadalmi", "kontextustól."], "Scientific research is never independent from social context.", ["c1-epistemic-skepticism"]),
                dc("dialogue", [
                    {"speaker": "Kritikus", "text": "Létezik-e teljes elfogulatlanság a tudományban?"},
                    {"speaker": "Szociológus", "text": "Tökéletes nem, de a kritikai reflexivitás segít felismerni a rejtett előítéleteket."},
                ], ["kritikai reflexivitás", "teljes vakság", "pénzügyi siker"], 0, ["c1-epistemic-skepticism"]),
                sw("production", [{"prompt": "Write a critical remark on the social embeddedness of scientific consensus.", "answer": "A tudományos konszenzus nem légüres térben, hanem történelmi és kulturális koordináták között formálódik."}], ["c1-epistemic-skepticism"]),
                mc("grammar", "check", "Mi a reflexivitás lényege a kutatásban?", [
                    "A saját előfeltevések és társadalmi meghatározottságok tudatos és kritikus vizsgálata.",
                    "A kísérletek automatikus megismétlése számítógéppel.",
                    "A bírálatok automatikus elutasítása."
                ], 0, ["c1-epistemic-skepticism"])
            ]
        },
        {
            "num": 5,
            "stem": f"c1-{slug}-05",
            "title": "Bioethics and Technological Limits in the 21st Century",
            "grammar_title": "Ethical Deliberation and Responsibility in Scientific Innovation",
            "grammar_skill": "c1-scientific-paradigm-discourse",
            "goals": [
                "I can debate ethical boundaries in genetic editing, AI, and biotechnology.",
                "I can use specialized bioethical vocabulary in Hungarian.",
                "I can construct nuanced arguments balancing technological progress and human dignity."
            ],
            "vocab": [
                {"lemma": "bioetika", "translation": "bioethics", "pos": "noun"},
                {"lemma": "emberi méltóság", "translation": "human dignity", "pos": "noun"},
                {"lemma": "génmódosítás", "translation": "genetic modification", "pos": "noun"},
                {"lemma": "felelősségvállalás", "translation": "assuming responsibility", "pos": "noun"},
                {"lemma": "etikai korlát", "translation": "ethical limit, boundary", "pos": "noun"},
                {"lemma": "visszafordíthatatlan", "translation": "irreversible", "pos": "adjective"},
                {"lemma": "elővigyázatosság", "translation": "precaution, vigilance", "pos": "noun"},
                {"lemma": "beavatkozás", "translation": "intervention", "pos": "noun"}
            ],
            "gr_text1": "Bioethics (*bioetika*) forces science to confront the moral limits of its own power. The debate over CRISPR genetic editing and artificial superintelligence revolves around *az elővigyázatosság elve* (the precautionary principle) and *az emberi méltóság sérthetetlensége* (the inviolability of human dignity).",
            "gr_text2": "In bioethical discourse, modal expressions of moral necessity (*kötelességünk, elengedhetetlen, megengedhetetlen*) intersect with legal and philosophical terminology.",
            "gr_table": [
                ["Az elővigyázatosság elvének betartása...", "Adherence to the precautionary principle..."],
                ["Az emberi méltóság védelmében...", "In defense of human dignity..."],
                ["Visszafordíthatatlan genetikai beavatkozások kockázata...", "The risk of irreversible genetic interventions..."]
            ],
            "world_story_seg": {
                "seg_slug": "etika",
                "title": "Bioetika és a tudomány határai a huszonegyedik században",
                "summary": "How cutting-edge genetic manipulation and autonomous artificial systems demand an unprecedented ethical framework to safeguard human dignity.",
                "paragraphs": [
                    {"type": "narration", "text": "A huszonegyedik században a tudomány elérkezett ahhoz a ponthoz, ahol már nemcsak a természet törvényeit képes megérteni, hanem magát az emberi létezés biológiai és kognitív alapjait is képes átírni. A génszerkesztési technológiák, a szintetikus biológia és a mesterséges intelligencia korábban elképzelhetetlen hatalmat adtak az emberiség kezébe."},
                    {"type": "narration", "text": "Ez a félelmetes hatalom azonban alapvető bioetikai kérdéseket vet fel. Vajon minden megengedhető-e erkölcsileg, ami technikailag megvalósítható? Az emberi méltóság sérthetetlen határ, vagy csupán meghaladandó biológiai korlát? Ha belenyúlunk az emberi génállományba, olyan visszafordíthatatlan láncreakciót indíthatunk el, amelynek következményeit ma még megbecsülni sem tudjuk."},
                    {"type": "narration", "text": "A tudomány felelőssége ma nagyobb, mint valaha. Nem vonulhat vissza a technikai szakbarbárság kényelmes bástyái mögé; nyílt, társadalmi és etikai párbeszédet kell folytatnia az emberiség jövőjéről. A haladás igazi mércéje ugyanis nem a gátlástalan technológiai hatalom, hanem az a bölcsesség, amellyel ezt a hatalmat az élet szolgálatába állítjuk."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Mi az 'elővigyázatosság elve' (precautionary principle) a bioetikában?", [
                    "Ha egy beavatkozás súlyos vagy visszafordíthatatlan károkat okozhat, a bizonyosság hiánya nem indok a védelem elhalasztására.",
                    "Minden új kísérletet azonnal emberen kell tesztelni.",
                    "A tudományos kutatások teljes betiltása."
                ], 0, ["c1-tudomanyelmelet-vocab"]),
                fb("grammar", "practice", "A biológiai kutatások legfőbb korlátja az emberi _____ feltétlen tiszteletben tartása. (dignity / méltóság)", "méltóság", "The chief limit of biological research is the unconditional respect of human dignity.", ["c1-scientific-paradigm-discourse"]),
                match("vocabulary", "controlled", [["bioetika", "bioethics"], ["emberi méltóság", "human dignity"], ["visszafordíthatatlan", "irreversible"], ["elővigyázatosság", "precaution"]], ["c1-tudomanyelmelet-vocab"]),
                sb("grammar", "practice", ["Nem", "minden", "engedhető", "meg,", "ami", "technikailag", "megvalósítható."], ["Nem", "minden", "engedhető", "meg,", "ami", "technikailag", "megvalósítható."], "Not everything is permissible that is technically feasible.", ["c1-scientific-paradigm-discourse"]),
                dc("dialogue", [
                    {"speaker": "Kutató", "text": "Megengedhető-e a génszerkesztés emberi embriókon?"},
                    {"speaker": "Bioetikus", "text": "A jelenlegi tudásunk mellett a visszafordíthatatlan kockázatok túl nagyok."},
                ], ["visszafordíthatatlan kockázatok", "teljes biztonság", "pénzügyi haszon"], 0, ["c1-scientific-paradigm-discourse"]),
                sw("production", [{"prompt": "Write a bioethical warning about technological intervention.", "answer": "A technológiai haladás nem válhat az emberi méltóság felszámolásának eszközévé."}], ["c1-scientific-paradigm-discourse"]),
                mc("grammar", "check", "Melyik fogalom áll a kortárs bioetikai viták középpontjában?", [
                    "Az emberi méltóság védelme és az elővigyázatosság elve.",
                    "A laboratóriumok tisztasági szabályzata.",
                    "A mikroszkópok nagyítási hatékonysága."
                ], 0, ["c1-scientific-paradigm-discourse"])
            ]
        }
    ]

    for l in disc_lessons:
        emit_instructional_lesson(3, "discourse", l, disc_title, disc_intro if l["num"] == 1 else None)

    # Full World Compilation Story
    write_json(
        f"stories/world/c1/{slug}.json",
        {
            "id": f"story.c1.world.{slug}",
            "title": "A megismerés határai: Polányi, Lakatos és a tudományos forradalmak",
            "level": "C1",
            "type": "world",
            "summary": "Complete exploration of Hungarian contributions to epistemology and scientific philosophy: Michael Polanyi, Imre Lakatos, John von Neumann, the critique of pure objectivity, and modern bioethics.",
            "paragraphs": [
                {"type": "narration", "text": "A huszadik század a tudomány diadalmenetének korszaka volt, de egyben az önreflexió forradalma is. Magyar származású gondolkodók sora játszott döntő szerepet abban, hogy a világ újragondolja a megismerés, a bizonyosság és a tudományos fejlődés természetét."},
                {"type": "narration", "text": "Polányi Mihály lerombolta a rideg objektivizmus mítoszát, amikor felmutatta a 'hallgatólagos tudás' és a kutatói elköteleződés nélkülözhetetlenségét. Rávilágított, hogy a tudomány legmélyén nem mechanikus algoritmusok, hanem a tudósközösség morális felelőssége és a felfedezés személyes szenvedélye pulzál."},
                {"type": "narration", "text": "Lakatos Imre a tudományos kutatási programok metodológiájával megmentette a tudomány racionalitását a popperi naiv cáfolat és a kuhni irracionális relativizmus között őrlődő filozófiában. Bebizonyította, hogy az elméletek rugalmas védőövekkel küzdenek a fennmaradásukért, és a fejlődést a progresszív problémaváltások jelzik."},
                {"type": "narration", "text": "Neumann János eközben a modern digitális civilizáció alapjait fektette le a számítógép-architektúra és a játékelmélet kidolgozásával, miközben prófétai éleslátással figyelmeztetett a technológiai fejlődés szingularitására és a gépi intelligencia határaira."},
                {"type": "narration", "text": "A huszonegyedik században ez az örökség a bioetika és a technológiaetika kihívásaiban él tovább. Amikor az emberi génállomány és a digitális tudat határait feszegetjük, újra meg kell tanulnunk: a megismerés igazi mércéje nem a gátlástalan hatalomvágy, hanem az emberi méltóság és a jövő iránti alázatos felelősségvállalás."}
            ]
        }
    )

    # Discourse Consolidation
    emit_consolidation_lesson(
        3,
        "discourse",
        f"c1-{slug}-consolidation",
        disc_title,
        [
            "I can compare the epistemological theories of Michael Polanyi and Imre Lakatos.",
            "I can analyze the philosophical dilemmas raised by cybernetics, AI, and bioethics.",
            "I can use specialized academic and scientific philosophy vocabulary in debate."
        ],
        [
            mc("grammar", "recognize", "Mit jelent a 'kemény mag' Lakatos Imre elméletében?", [
                "Egy elmélet érinthetetlen elméleti alapját, amelyet nem vetnek alá cáfolatnak.",
                "A kísérleti eszközök fém alkatrészeit.",
                "A legszigorúbb professzorok csoportját."
            ], 0, ["c1-scientific-paradigm-discourse"]),
            mc("grammar", "recognize", "Melyik állítás összegzi Polányi Mihály tanítását?", [
                "Többet tudunk, mint amennyit szavakkal képesek vagyunk kifejezni.",
                "A tudomány kizárólag mechanikus adatgyűjtésből áll.",
                "Az emberi tényező teljesen elhanyagolható a kutatásban."
            ], 0, ["c1-scientific-paradigm-discourse"]),
            match("vocabulary", "recognize", [["hallgatólagos tudás", "tacit knowledge"], ["kemény mag", "hard core"], ["védőöv", "protective belt"], ["bioetika", "bioethics"], ["emberi méltóság", "human dignity"]], ["c1-tudomanyelmelet-vocab"]),
            fb("vocabulary", "recall", "A kutatási program segédhipotézisei alkotják az elméletet védelmező _____. (protective belt / védőövet)", "védőövet", "The auxiliary hypotheses of the research programme constitute the protective belt defending the theory.", ["c1-tudomanyelmelet-vocab"]),
            fb("vocabulary", "recall", "Polányi szerint a tudomány a kutatói közösség morális _____ épül. (commitment / elköteleződésére)", "elköteleződésére", "According to Polanyi, science is built upon the moral commitment of the research community.", ["c1-tudomanyelmelet-vocab"]),
            fb("grammar", "recall", "A genetikai beavatkozások során az _____ elvét kell követni. (precaution / elővigyázatosság)", "elővigyázatosság", "In genetic interventions, one must follow the principle of precaution.", ["c1-scientific-paradigm-discourse"]),
            fb("grammar", "context", "A tudományos konszenzus nem légüres térben, hanem társadalmi _____ alakul ki. (embeddedness / beágyazottságban)", "beágyazottságban", "Scientific consensus does not evolve in a vacuum, but in social embeddedness.", ["c1-epistemic-skepticism"]),
            fb("grammar", "context", "Neumann játékelmélete forradalmasította a stratégiai _____ logikáját. (decision-making / döntéshozatal)", "döntéshozatal", "Neumann's game theory revolutionized the logic of strategic decision-making.", ["c1-epistemic-skepticism"]),
            mc("grammar", "context", "Milyen veszélyre figyelmeztet a modern bioetika?", [
                "Arra, hogy a technológiai képesség megelőzi az erkölcsi bölcsességet és a felelősségvállalást.",
                "Hogy elfogynak a laboratóriumi lombikok.",
                "Hogy a tudósok túl sokat olvasnak."
            ], 0, ["c1-scientific-paradigm-discourse"]),
            sb("grammar", "produce", ["A", "tudományos", "haladás", "igazi", "mércéje", "az", "emberi", "méltóság", "védelme."], ["A", "tudományos", "haladás", "igazi", "mércéje", "az", "emberi", "méltóság", "védelme."], "The true yardstick of scientific progress is the defense of human dignity.", ["c1-scientific-paradigm-discourse"]),
            sw("production", [{"prompt": "Write a synthesized epistemological thought comparing Polanyi and Lakatos.", "answer": "Míg Polányi a megismerés személyes és tacit dimenzióját kutatta, addig Lakatos a programok racionális versenyét elemezte."}], ["c1-scientific-paradigm-discourse"]),
            sw("production", [{"prompt": "Formulate a concluding bioethical stance.", "answer": "A technológia hatalma csak akkor szolgálja az embert, ha szigorú etikai korlátok közé szorítjuk."}], ["c1-scientific-paradigm-discourse"])
        ]
    )
    print("=== Finished C1 Unit 3 ===")


if __name__ == "__main__":
    generate_unit_3()
