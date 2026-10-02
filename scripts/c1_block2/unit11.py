#!/usr/bin/env python3
"""
Hungarian C1 Block 2 - Unit 11 Generator:
  - Track 1 (Core): Unit 11 — "Human Rights, Minority Protections & International Law" (c1-11)
  - Track 2 (Discourse): Unit 11 — "Universal Human Rights & Minority Protections" (c1-emberijogok)
"""

import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT))

from scripts.c1_block1.common import mc, match, fb, sb, dc, sw, write_json, emit_instructional_lesson, emit_consolidation_lesson
from scripts.c1_block2.registry_helper import register_unit


def generate_unit_11():
    print("=== Generating C1 Unit 11 ===")
    
    # Register skills & titles
    new_skills = {
        "c1-11-vocab": {"kind": "vocabulary"},
        "c1-emberijogok-vocab": {"kind": "vocabulary"},
        "c1-correlative-rights": {"kind": "grammar"},
        "c1-minority-protection-clauses": {"kind": "grammar"},
        "c1-universal-jurisdiction": {"kind": "grammar"},
        "c1-international-treaty-framing": {"kind": "grammar"},
        "c1-collective-responsibility": {"kind": "grammar"},
    }
    new_titles = {
        "c1-11-vocab": "reading",
        "c1-emberijogok-vocab": "reading",
        "c1-correlative-rights": "correlative attributive constructions in fundamental rights declarations",
        "c1-minority-protection-clauses": "linguistic minority rights and cultural autonomy legal framing",
        "c1-universal-jurisdiction": "international humanitarian law and universal human rights discourse",
        "c1-international-treaty-framing": "international treaty integration and constitutional rights hierarchy",
        "c1-collective-responsibility": "moral accounting collective responsibility and historical reckoning",
    }
    
    core_title = "Human Rights, Minority Protections & International Law"
    core_stems = [f"c1-11-0{i}" for i in range(1, 6)] + ["c1-11-consolidation"]
    disc_title = "Universal Human Rights & Minority Protections"
    disc_stems = [f"c1-emberijogok-0{i}" for i in range(1, 6)] + ["c1-emberijogok-consolidation"]
    
    register_unit(11, core_title, core_stems, disc_title, disc_stems, new_skills, new_titles)

    # ----------------------------------------------------
    # TRACK 1: CORE (c1-11)
    # ----------------------------------------------------
    core_intro = [
        "International human rights and minority protection law in Hungarian operates through high-register correlative attributive syntax (olyan jogok, amelyek mint ilyenek elidegeníthetetlenek), treaty hierarchy predicates (tekintettel arra, hogy; összhangban a nemzetközi kötelezettségekkel), and strict non-discrimination terminology.",
        "In this unit, inspired by István Bibó's monumental postwar moral essay 'A zsidókérdés Magyarországon 1944 után' (1948), you will master fundamental rights declarations, minority linguistic autonomy, and the solemn legal register of collective moral responsibility."
    ]

    core_lessons = [
        {
            "num": 1,
            "stem": "c1-11-01",
            "title": "Correlative Attributive Structures in Human Rights Declarations",
            "grammar_title": "Correlative Clauses in Inalienable Rights Formulas",
            "grammar_skill": "c1-correlative-rights",
            "goals": [
                "I can form correlative attributive constructions (*olyan alapjogok, amelyek mint ilyenek...*).",
                "I can deploy high-register inalienability predicates (*elidegeníthetetlen, korlátozhatatlan*).",
                "I can synthesize international human rights covenants in solemn formal Hungarian."
            ],
            "vocab": [
                {"lemma": "elidegeníthetetlen", "translation": "inalienable", "pos": "adjective"},
                {"lemma": "korlátozhatatlan", "translation": "non-derogable, unlimitable", "pos": "adjective"},
                {"lemma": "mint ilyenek", "translation": "as such", "pos": "expression"},
                {"lemma": "emberi jogi egyezmény", "translation": "human rights convention", "pos": "noun"},
                {"lemma": "megkülönböztetés tilalma", "translation": "prohibition of discrimination", "pos": "noun"},
                {"lemma": "személyi méltóság", "translation": "personal dignity", "pos": "noun"},
                {"lemma": "jogalanyiság", "translation": "legal personhood / capacity", "pos": "noun"},
                {"lemma": "egyetemes érvényű", "translation": "universally valid / applicable", "pos": "adjective"}
            ],
            "gr_text1": "Solemn constitutional declarations employ correlative demonstratives (*olyan... amely*) combined with restrictive appositions like *mint ilyenek* (as such) to emphasize inviolability: *Az emberi jogok olyan születési előjogok, amelyek mint ilyenek minden államhatalmat megelőznek.*",
            "gr_text2": "Non-derogable rights (*korlátozhatatlan jogok*)—such as the prohibition of torture and arbitrary killing—admit no state derogation even in times of national emergency (*rendkívüli állapot*).",
            "gr_table": [
                ["Olyan jogok, amelyek mint ilyenek senkitől el nem vonhatók...", "Rights that as such cannot be stripped from anyone..."],
                ["Az emberi méltóság egyetemes érvényű, veleszületett alapérték.", "Human dignity is a universally valid, innate fundamental value."],
                ["A kínzás tilalma feltétlen és korlátozhatatlan kötelezettség.", "The prohibition of torture is an absolute and non-derogable duty."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mit jelent az emberi jogok 'elidegeníthetetlen' jellege?", ["Azt, hogy a jogok az embert születésénél fogva megilletik, és államhatalom nem veheti el őket.", "Hogy a jogokat külföldiek nem használhatják.", "Hogy a jogok pénzért eladhatók."], 0, ["c1-11-vocab"]),
                fb("grammar", "controlled", "Minden ember olyan alapvető szabadságjogokkal bír, amelyek mint _____ elidegeníthetetlenek. (as such / ilyenek)", "ilyenek", "Every human being possesses fundamental liberties that as such are inalienable.", ["c1-correlative-rights"]),
                match("vocabulary", "controlled", [["elidegeníthetetlen", "inalienable"], ["korlátozhatatlan", "non-derogable"], ["megkülönböztetés tilalma", "prohibition of discrimination"], ["jogalanyiság", "legal personhood"]], ["c1-11-vocab"]),
                fb("grammar", "practice", "A kínzás és a kegyetlen bánásmód tilalma abszolút és semmilyen körülmények között nem _____. (limitable / korlátozható)", "korlátozható", "The prohibition of torture and cruel treatment is absolute and cannot be limited under any circumstances.", ["c1-correlative-rights"]),
                sb("grammar", "practice", ["Az", "emberi", "méltóság", "minden", "törvényhozó", "hatalmat", "megelőző", "alapérték."], ["Az", "emberi", "méltóság", "minden", "törvényhozó", "hatalmat", "megelőző", "alapérték."], "Human dignity is a fundamental value preceding every legislative power.", ["c1-correlative-rights"]),
                dc("dialogue", [
                    {"speaker": "Jogvédő", "text": "Korlátozhatja-e a kormány a véleményszabadságot vészhelyzetben?"},
                    {"speaker": "Alkotmányjogász", "text": "Csak a legszükségesebb mértékben, de a személyes méltóság magja sohasem _____."},
                ], ["sérthető", "olvasható", "kérhető"], 0, ["c1-correlative-rights"]),
                sw("production", [{"prompt": "Draft a solemn human rights clause using 'olyan..., amelyek mint ilyenek...'.", "answer": "Minden személyt megilletnek olyan elidegeníthetetlen jogok, amelyek mint ilyenek származásra, nyelvre és vallásra való tekintet nélkül védelmet élveznek."}], ["c1-correlative-rights"]),
                mc("grammar", "check", "Melyik állítás fogalmazza meg a non-derogable (korlátozhatatlan) jogok lényegét?", [
                    "Olyan jogok, amelyeket még háború vagy rendkívüli állapot idején sem lehet felfüggeszteni.",
                    "Jogok, amelyek csak hétvégén érvényesek.",
                    "Olyan jogok, amelyeket évente meg kell újítani egy vizsgával."
                ], 0, ["c1-correlative-rights"])
            ]
        },
        {
            "num": 2,
            "stem": "c1-11-02",
            "title": "Minority Linguistic Rights and Cultural Autonomy",
            "grammar_title": "Legal Framing of National Minorities and Collective Rights",
            "grammar_skill": "c1-minority-protection-clauses",
            "goals": [
                "I can analyze national minority protection frameworks in Hungary (*nemzetiségi törvény, államalkotó tényező*).",
                "I can evaluate linguistic rights (*anyanyelvhasználat joga a hatóságok előtt*).",
                "I can formulate principles of cultural self-governance (*kulturális autonómia, önkormányzatiság*)."
            ],
            "vocab": [
                {"lemma": "államalkotó tényező", "translation": "constituent factor of the state", "pos": "expression"},
                {"lemma": "kulturális autonómia", "translation": "cultural autonomy", "pos": "noun"},
                {"lemma": "nemzetiségi önkormányzat", "translation": "nationality / minority self-government", "pos": "noun"},
                {"lemma": "anyanyelvhasználat joga", "translation": "right to use one's mother tongue", "pos": "expression"},
                {"lemma": "asszimiláció", "translation": "assimilation", "pos": "noun"},
                {"lemma": "identitás megőrzése", "translation": "preservation of identity", "pos": "expression"},
                {"lemma": "pozitív diszkrimináció", "translation": "positive discrimination / affirmative action", "pos": "noun"},
                {"lemma": "kisebbségvédelem", "translation": "minority protection", "pos": "noun"}
            ],
            "gr_text1": "Under the Hungarian Fundamental Law, the 13 recognized national minorities are declared *államalkotó tényezők* (constituent factors of the state). The constitution guarantees both individual and collective rights (*egyéni és közösségi jogok*).",
            "gr_text2": "Minorities exercise cultural autonomy (*kulturális autonómia*) through their own elected nationality self-governments (*nemzetiségi önkormányzatok*), operating schools and cultural institutions.",
            "gr_table": [
                ["A nemzetiségek a magyar politikai közösség államalkotó tényezői.", "Nationalities are constituent factors of the Hungarian political community."],
                ["Az anyanyelv szabad használata a közigazgatási eljárásokban...", "Free use of the mother tongue in administrative proceedings..."],
                ["Kulturális önkormányzatiság és a nemzeti identitás védelme...", "Cultural self-governance and preservation of national identity..."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Hogyan határozza meg a magyar Alaptörvény az elismert nemzetiségek jogállását?", ["A magyar politikai közösség részét képező államalkotó tényezőként.", "Ideiglenes vendégekként.", "Külföldi állampolgárokként."], 0, ["c1-11-vocab"]),
                fb("grammar", "controlled", "A törvény garantálja a nemzetiségi közösségek számára a kulturális _____ és az anyanyelvi oktatás jogát. (autonomy / autonómia)", "autonómia", "The statute guarantees cultural autonomy and the right to mother-tongue education for nationality communities.", ["c1-minority-protection-clauses"]),
                match("vocabulary", "controlled", [["államalkotó tényező", "constituent state factor"], ["kulturális autonómia", "cultural autonomy"], ["anyanyelvhasználat joga", "right to native language"], ["asszimiláció", "assimilation"]], ["c1-11-vocab"]),
                fb("grammar", "practice", "A nemzetiségek védelme magában foglalja az erőszakos asszimilációval szembeni fellépést és a saját önazonosság _____ jogát. (preservation / megőrzésének)", "megőrzésének", "The protection of nationalities includes acting against forced assimilation and the right of preservation of their own identity.", ["c1-minority-protection-clauses"]),
                sb("grammar", "practice", ["A", "nemzetiségi", "önkormányzatok", "saját", "iskolákat", "és", "intézményeket", "tarthatnak", "fenn."], ["A", "nemzetiségi", "önkormányzatok", "saját", "iskolákat", "és", "intézményeket", "tarthatnak", "fenn."], "Nationality self-governments may maintain their own schools and institutions.", ["c1-minority-protection-clauses"]),
                dc("dialogue", [
                    {"speaker": "Képviselő", "text": "Használhatja-e a nemzetiségi polgár az anyanyelvét a hivatalban?"},
                    {"speaker": "Jegyző", "text": "Igen, a törvény kifejezetten biztosítja a hivatali _____ jogát."},
                ], ["nyelvhasználat", "szünet", "zavarás"], 0, ["c1-minority-protection-clauses"]),
                sw("production", [{"prompt": "Write a formal statement affirming the rights of linguistic minorities in Hungary.", "answer": "A magyar jogrend elismeri a honos nemzetiségeket mint államalkotó tényezőket, garantálva anyanyelvük szabad használatát és kulturális önrendelkezésüket."}], ["c1-minority-protection-clauses"]),
                mc("grammar", "check", "Mi képezi a nemzetiségi közösségi jogok alapelvét a magyar jogban?", [
                    "Hogy a nemzetiségi jogok nemcsak egyénileg, hanem a közösség által együttesen is gyakorolhatók.",
                    "Hogy csak egyének tiltakozhatnak a bíróságon.",
                    "Hogy a kisebbségek nem tarthatnak választásokat."
                ], 0, ["c1-minority-protection-clauses"])
            ]
        },
        {
            "num": 3,
            "stem": "c1-11-03",
            "title": "International Humanitarian Law and Universal Jurisdiction",
            "grammar_title": "Geneva Conventions and Prosecuting Crimes Against Humanity",
            "grammar_skill": "c1-universal-jurisdiction",
            "goals": [
                "I can analyze international humanitarian law terminology (*Genfi Egyezmények, emberiesség elleni bűncselekmények*).",
                "I can evaluate the doctrine of universal jurisdiction (*egyetemes joghatóság*).",
                "I can discuss International Criminal Court (ICC) mechanisms in formal Hungarian."
            ],
            "vocab": [
                {"lemma": "emberiesség elleni bűncselekmény", "translation": "crime against humanity", "pos": "noun"},
                {"lemma": "háborús bűncselekmény", "translation": "war crime", "pos": "noun"},
                {"lemma": "nemzetközi humanitárius jog", "translation": "international humanitarian law", "pos": "noun"},
                {"lemma": "egyetemes joghatóság", "translation": "universal jurisdiction", "pos": "noun"},
                {"lemma": "el nem évülő", "translation": "imprescriptible, not subject to statute of limitations", "pos": "adjective"},
                {"lemma": "Nemzetközi Büntetőbíróság", "translation": "International Criminal Court (ICC / Római Statútum)", "pos": "noun"},
                {"lemma": "polgári lakosság", "translation": "civilian population", "pos": "noun"},
                {"lemma": "felelősségre vonás", "translation": "bringing to justice, prosecution", "pos": "noun"}
            ],
            "gr_text1": "International humanitarian law (*Genfi Egyezmények*) establishes that genocide and crimes against humanity are imprescriptible (*el nem évülő bűncselekmények*): they never expire under statutes of limitations.",
            "gr_text2": "The principle of *egyetemes joghatóság* (universal jurisdiction) allows national courts to prosecute perpetrators of atrocities regardless of where the crime occurred or the nationality of perpetrator and victim.",
            "gr_table": [
                ["Az emberiesség elleni bűntettek el nem évülő jellegének elve...", "The principle of imprescriptibility of crimes against humanity..."],
                ["Egyetemes joghatóság alkalmazása a nemzetközi igazságszolgáltatásban...", "Application of universal jurisdiction in international justice..."],
                ["A polgári lakosság megkérdőjelezhetetlen védelme fegyveres konfliktusban...", "Unquestionable protection of civilian populations in armed conflicts..."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mit jelent az 'egyetemes joghatóság' (universal jurisdiction) elve a büntetőjogban?", ["Bármely állam bírósága felelősségre vonhatja a legsúlyosabb nemzetközi bűntettek elkövetőit a tett helyétől függetlenül.", "Csak az ENSZ elnöke ítélkezhet.", "A bűnözők szabadon utazhatnak."], 0, ["c1-11-vocab"]),
                fb("grammar", "controlled", "A nemzetközi jog szerint a háborús bűncselekmények el nem _____ tettek, így bármikor büntethetők. (imprescriptible / évülő)", "évülő", "Under international law war crimes are imprescriptible acts, thus punishable at any time.", ["c1-universal-jurisdiction"]),
                match("vocabulary", "controlled", [["emberiesség elleni bűncselekmény", "crime against humanity"], ["háborús bűncselekmény", "war crime"], ["egyetemes joghatóság", "universal jurisdiction"], ["polgári lakosság", "civilian population"]], ["c1-11-vocab"]),
                fb("grammar", "practice", "A polgári lakosság elleni szándékos támadás a nemzetközi humanitárius jog legsúlyosabb _____ valósítja meg. (violation / sérelmét)", "sérelmét", "Deliberate attack against the civilian population constitutes the gravest violation of international humanitarian law.", ["c1-universal-jurisdiction"]),
                sb("grammar", "practice", ["A", "háborús", "bűnösök", "felelősségre", "vonása", "nemzetközi", "erkölcsi", "és", "jogi", "kötelesség."], ["A", "háborús", "bűnösök", "felelősségre", "vonása", "nemzetközi", "erkölcsi", "és", "jogi", "kötelesség."], "Prosecution of war criminals is an international moral and legal duty.", ["c1-universal-jurisdiction"]),
                dc("dialogue", [
                    {"speaker": "Ügyész", "text": "Hivatkozhat-e a vádlott parancsteljesítésre a mészárlás igazolásakor?"},
                    {"speaker": "Bíró", "text": "Nem, a nyilvánvalóan jogellenes parancs végrehajtása nem menti fel az egyéni _____ alól."},
                ], ["felelősség", "munka", "fáradtság"], 0, ["c1-universal-jurisdiction"]),
                sw("production", [{"prompt": "Explain why crimes against humanity are not subject to statutory limitation.", "answer": "Az emberiesség elleni bűncselekmények az egész emberi nemet sértik, ezért az igazságszolgáltatás elől az idő múlása nem nyújthat menekvést."}], ["c1-universal-jurisdiction"]),
                mc("grammar", "check", "Melyik bíróság gyakorol állandó nemzetközi büntető joghatóságot a legsúlyosabb atrocitások felett?", [
                    "A hágai Nemzetközi Büntetőbíróság (ICC).",
                    "A genfi postaigazgatóság.",
                    "A párizsi békebizottság."
                ], 0, ["c1-universal-jurisdiction"])
            ]
        },
        {
            "num": 4,
            "stem": "c1-11-04",
            "title": "International Treaties in the Domestic Legal Hierarchy",
            "grammar_title": "Treaty Integration and Constitutional Compatibility (Monism vs. Dualism)",
            "grammar_skill": "c1-international-treaty-framing",
            "goals": [
                "I can analyze the integration of international treaties into Hungarian domestic law (*monista vs. dualista modell*).",
                "I can navigate conflicts between domestic statutes and international human rights conventions.",
                "I can explain the European Convention on Human Rights (ECHR) ranking in Hungarian jurisprudence."
            ],
            "vocab": [
                {"lemma": "nemzetközi szerződés", "translation": "international treaty / agreement", "pos": "noun"},
                {"lemma": "kihirdetés", "translation": "promulgation / enactment", "pos": "noun"},
                {"lemma": "jogforrási hierarchia", "translation": "hierarchy of legal sources", "pos": "noun"},
                {"lemma": "összhang biztosítása", "translation": "ensuring harmony / compliance", "pos": "expression"},
                {"lemma": "megsértése", "translation": "violation / infringement of", "pos": "noun"},
                {"lemma": "nemzetközi jogi kötelezettség", "translation": "international legal obligation", "pos": "noun"},
                {"lemma": "strasbourgi bíróság", "translation": "Strasbourg court (ECtHR)", "pos": "noun"},
                {"lemma": "jogharmonizáció", "translation": "legal harmonization", "pos": "noun"}
            ],
            "gr_text1": "Hungary follows a moderate dualist system: international treaties become domestic law only upon formal statutory promulgation (*kihirdetés törvényben vagy kormányrendeletben*).",
            "gr_text2": "In the *jogforrási hierarchia*, promulgated international treaties rank below the Fundamental Law but above ordinary parliamentary Acts: an Act conflicting with an international treaty must be annulled by the Constitutional Court.",
            "gr_table": [
                ["A nemzetközi szerződésbe ütköző hazai jogszabály megsemmisítése...", "Annulment of domestic legislation conflicting with international treaties..."],
                ["A jogforrási hierarchia és a nemzetközi jog primátusa a belső törvények felett...", "Hierarchy of sources and primacy of international law over domestic acts..."],
                ["Az Emberi Jogok Európai Egyezményének kötelező ereje...", "The binding force of the European Convention on Human Rights..."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Hogyan válik egy nemzetközi egyezmény a magyar jog részévé?", ["Kihirdetéssel, azaz a parlament által hozott törvénybe iktatással.", "Automatikusan, ha a miniszter elolvassa.", "Kizárólag újságcikkek útján."], 0, ["c1-11-vocab"]),
                fb("grammar", "controlled", "Az Alkotmánybíróság megsemmisíti azt a hazai törvényt, amely nemzetközi szerződésbe _____. (collides / ütközik)", "ütközik", "The Constitutional Court annuls domestic acts that conflict with international treaties.", ["c1-international-treaty-framing"]),
                match("vocabulary", "controlled", [["nemzetközi szerződés", "international treaty"], ["kihirdetés", "promulgation"], ["jogforrási hierarchia", "hierarchy of sources"], ["összhang biztosítása", "ensuring harmony"]], ["c1-11-vocab"]),
                fb("grammar", "practice", "A jogalkotó köteles biztosítani a belső jog és a vállalt nemzetközi kötelezettségek teljes _____. (harmony / összhangját)", "összhangját", "The legislator is obligated to ensure full harmony between domestic law and assumed international obligations.", ["c1-international-treaty-framing"]),
                sb("grammar", "practice", ["A", "nemzetközi", "emberi", "jogi", "egyezmények", "a", "hazai", "törvények", "felett", "állnak."], ["A", "nemzetközi", "emberi", "jogi", "egyezmények", "a", "hazai", "törvények", "felett", "állnak."], "International human rights conventions stand above domestic statutes.", ["c1-international-treaty-framing"]),
                dc("dialogue", [
                    {"speaker": "Ügyvéd", "text": "Hivatkozhatunk-e a strasbourgi bíróság gyakorlatára a magyar perben?"},
                    {"speaker": "Bíró", "text": "Igen, a bíróságok kötelesek a hazai jogot az Emberi Jogok Európai Egyezményével _____ értelmezni."},
                ], ["összhangban", "haragban", "ellentétben"], 0, ["c1-international-treaty-framing"]),
                sw("production", [{"prompt": "Explain the hierarchy between domestic statutes and international treaties in Hungary.", "answer": "A kihirdetett nemzetközi szerződések a hazai jogforrási hierarchiában a törvények felett állnak; a velük ütköző magyar jogszabályokat az Alkotmánybíróság megsemmisíti."}], ["c1-international-treaty-framing"]),
                mc("grammar", "check", "Mi a jogkövetkezménye annak, ha a strasbourgi bíróság jogsértést állapít meg egy ügyben?", [
                    "A magyar állam kártérítést köteles fizetni, és szükség esetén felül kell vizsgálni a hazai eljárást.",
                    "A bíróság feloszlatja a parlamentet.",
                    "Semmilyen hatása nincs a magyar jogra."
                ], 0, ["c1-international-treaty-framing"])
            ]
        },
        {
            "num": 5,
            "stem": "c1-11-05",
            "title": "Moral Accounting and Collective Responsibility: István Bibó",
            "grammar_title": "Historical Reckoning and the Ethics of Political Responsibility",
            "grammar_skill": "c1-collective-responsibility",
            "goals": [
                "I can analyze István Bibó's landmark 1948 essay 'A zsidókérdés Magyarországon 1944 után'.",
                "I can distinguish between collective guilt (*kollektív bűnösség*) and political responsibility.",
                "I can evaluate Hungarian historical trauma processing with profound ethical precision."
            ],
            "vocab": [
                {"lemma": "erkölcsi elszámolás", "translation": "moral accounting / reckoning", "pos": "noun"},
                {"lemma": "kollektív bűnösség", "translation": "collective guilt", "pos": "noun"},
                {"lemma": "politikai felelősség", "translation": "political responsibility", "pos": "noun"},
                {"lemma": "történelmi önvizsgálat", "translation": "historical self-examination", "pos": "noun"},
                {"lemma": "bűnbakkeresés", "translation": "scapegoating", "pos": "noun"},
                {"lemma": "morális vakság", "translation": "moral blindness", "pos": "noun"},
                {"lemma": "társadalmi cinkosság", "translation": "societal complicity / connivance", "pos": "noun"},
                {"lemma": "emberi szolidaritás", "translation": "human solidarity", "pos": "noun"}
            ],
            "gr_text1": "István Bibó (1911–1979) was Hungary's greatest 20th-century political moralist. In his 1948 essay *A zsidókérdés Magyarországon 1944 után*, he conducted unprecedented historical self-examination regarding the Holocaust in Hungary.",
            "gr_text2": "Bibó strictly rejected the concept of *kollektív bűnösség* (collective guilt), arguing that guilt is always individual. However, he insisted on *politikai és erkölcsi felelősség* (political and moral responsibility): a nation that fails to face its own complicity poisons its future democratic development.",
            "gr_table": [
                ["A kollektív bűnösség tézisének elutasítása az egyéni felelősség mellett...", "Rejecting collective guilt in favor of individual responsibility..."],
                ["A nemzet politikai és erkölcsi felelőssége a történelmi önvizsgálatban...", "The political and moral responsibility of the nation in self-examination..."],
                ["Az igazság kimondása mint a gyógyulás egyetlen lehetséges útja...", "Speaking the truth as the only possible path to healing..."]
            ],
            "classic_story": {
                "slug": "c1-11-bibo",
                "author": "Bibó István",
                "work": "A zsidókérdés Magyarországon 1944 után (1948)",
                "title": "A nemzet lelkiismerete és a morális felelősség",
                "summary": "István Bibó's monumental postwar essay confronting the tragedy of 1944, rejecting collective guilt while demanding fearless moral reckoning.",
                "characters": ["Bibó István"],
                "paragraphs": [
                    {"type": "narration", "text": "1948-ban, a háborús romokból éppen csak ocsúdó Magyarországon megjelent egy tanulmány, amely a huszadik századi magyar szellemtörténet legbátrabb és legkíméletlenebb tükrét tartotta a nemzet elé. Bibó István, a kiváló jogtudós és politikai gondolkodó a Válasz című folyóiratban tette közzé A zsidókérdés Magyarországon 1944 után című művét, amely mindmáig a történelmi szembenézés megkerülhetetlen etikai etalonja."},
                    {"type": "narration", "text": "Bibó szigorúan elutasította a kollektív bűnösség hazug és romboló elméletét: kimondta, hogy bűnös csak az egyén lehet a saját konkrét tetteiért. Ezzel egyidejűleg azonban könyörtelen világossággal követelte meg a társadalom egészétől a politikai és erkölcsi felelősség vállalását. Nem lehetett többé a külső körülményekre, a német megszállásra vagy a szélsőségesek kis csoportjára hárítani a felelősséget azért a passzivitásért és cinkosságért, amely százezrek pusztulását kísérte."},
                    {"type": "narration", "text": "Bibó diagnózisa szerint az igazi veszély a félelem, a bűntudat elfojtása és az öncsalás: ha egy közösség nem képes szembenézni saját történelmének sötét fejezeteivel, menthetetlenül a bűnbakkeresés és a politikai hisztéria csapdájába esik. A valódi polgári demokrácia és az emberi jogok tisztelete nem jelszavakból épül, hanem az igazság bátor kimondásából és az elesettek iránti feltétlen szolidaritásból."},
                    {"type": "narration", "text": "Bibó István kristálytiszta, emelkedett mondatai ma is a magyar demokrácia alapkövét jelentik. Arra figyelmeztetnek, hogy az emberi méltóság és a szabadság védelme soha nem lehet alku tárgya, és a nemzeti nagyság igazi mércéje nem a múlt elhallgatása, hanem a felelősség bátor és tiszta felvállalása."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Hogyan viszonyult Bibó István a 'kollektív bűnösség' fogalmához?", ["Elutasította a kollektív bűnösséget, de megkövetelte a nemzet egészétől a politikai és erkölcsi felelősségvállalást.", "Minden magyar embert bűnösnek nyilvánított.", "Azt állította, hogy senki sem felelős semmiért."], 0, ["c1-11-vocab"]),
                fb("grammar", "controlled", "Bibó szerint a múlt eltagadása elkerülhetetlenül társadalmi hisztériához és morális _____ vezet. (blindness / vaksághoz)", "vaksághoz", "According to Bibó denying the past inevitably leads to societal hysteria and moral blindness.", ["c1-collective-responsibility"]),
                match("vocabulary", "controlled", [["erkölcsi elszámolás", "moral reckoning"], ["kollektív bűnösség", "collective guilt"], ["politikai felelősség", "political responsibility"], ["morális vakság", "moral blindness"]], ["c1-11-vocab"]),
                mc("reading", "practice", "Miért tekintette Bibó nélkülözhetetlennek az 1944-es eseményekkel való szembenézést?", [
                    "Mert az elfojtott bűntudat és a hazugság megmérgezi a demokratikus közélet kibontakozását.",
                    "Mert újabb háborút akart kirobbantani.",
                    "Mert nem szerette a történelmet."
                ], 0, None),
                sb("grammar", "practice", ["A", "nemzeti", "önvizsgálat", "a", "demokratikus", "megújulás", "nélkülözhetetlen", "feltétele."], ["A", "nemzeti", "önvizsgálat", "a", "demokratikus", "megújulás", "nélkülözhetetlen", "feltétele."], "National self-examination is the indispensable condition of democratic renewal.", ["c1-collective-responsibility"]),
                sw("production", [{"prompt": "Synthesize István Bibó's distinction between guilt and responsibility.", "answer": "Bibó szerint jogi értelemben bűnös csak az egyén lehet a tetteiért, ám a társadalmi közösséget politikai és erkölcsi felelősség terheli polgártársai sorsáért és az állam tetteiért."}], ["c1-collective-responsibility"]),
                mc("grammar", "check", "Melyik állítás foglalja össze legmélyebben Bibó István politikai etikáját?", [
                    "A demokrácia igazi záloga a félelem nélküli igazság kimondása és a felelősség bátor felvállalása.",
                    "A politikában az erő és az elhallgatás a legfontosabb erény.",
                    "A múlt kérdéseivel soha nem szabad foglalkozni."
                ], 0, ["c1-collective-responsibility"])
            ]
        }
    ]

    for l in core_lessons:
        emit_instructional_lesson(11, "core", l, core_title, core_intro if l["num"] == 1 else None)

    # Core Consolidation
    emit_consolidation_lesson(
        11,
        "core",
        "c1-11-consolidation",
        core_title,
        [
            "I can formulate correlative human rights clauses (olyan jogok, amelyek mint ilyenek...).",
            "I can analyze national minority protections, cultural autonomy, and linguistic rights.",
            "I can apply international humanitarian law principles and evaluate Bibó's moral accounting."
        ],
        [
            mc("grammar", "recognize", "Mit fejez ki a 'mint ilyenek' szerkezet az emberi jogi nyelvben?", [
                "A jogok önmagukban való, elválaszthatatlan és természetes jellegét hangsúlyozza.",
                "Hogy a jogok nem fontosak.",
                "Hogy a törvényt újra kell írni."
            ], 0, ["c1-correlative-rights"]),
            mc("grammar", "recognize", "Milyen jogi státuszt biztosít az Alaptörvény a magyarországi nemzetiségeknek?", [
                "Államalkotó tényezők egyéni és közösségi jogokkal.",
                "Külföldi vendégmunkások jogait.",
                "Semmilyen külön jogot nem biztosít."
            ], 0, ["c1-minority-protection-clauses"]),
            match("vocabulary", "recognize", [["elidegeníthetetlen", "inalienable"], ["államalkotó tényező", "constituent state factor"], ["kulturális autonómia", "cultural autonomy"], ["egyetemes joghatóság", "universal jurisdiction"], ["erkölcsi elszámolás", "moral accounting"]], ["c1-11-vocab"]),
            fb("vocabulary", "recall", "Az emberiesség elleni bűncselekmények el nem _____ tettek a nemzetközi jogban. (imprescriptible / évülő)", "évülő", "Crimes against humanity are imprescriptible acts in international law.", ["c1-11-vocab"]),
            fb("vocabulary", "recall", "Bibó István elutasította a kollektív bűnösséget, de követelte az erkölcsi _____ felvállalását. (responsibility / felelősség)", "felelősség", "István Bibó rejected collective guilt, but demanded assuming moral responsibility.", ["c1-11-vocab"]),
            fb("grammar", "recall", "Minden polgárt megilletnek olyan alapjogok, amelyek mint _____ korlátozhatatlanok. (as such / ilyenek)", "ilyenek", "Every citizen is entitled to fundamental rights that as such are non-derogable.", ["c1-correlative-rights"]),
            fb("grammar", "context", "A kihirdetett nemzetközi egyezmények a hazai jogforrási hierarchiában a törvények _____ állnak. (above / felett)", "felett", "Promulgated international conventions stand above statutes in the domestic hierarchy of legal sources.", ["c1-international-treaty-framing"]),
            fb("grammar", "context", "A nemzetiségek védelme kizárja az erőszakos asszimilációt és garantálja az anyanyelvhasználat _____. (right / jogát)", "jogát", "Protection of nationalities excludes forced assimilation and guarantees the right to mother-tongue usage.", ["c1-minority-protection-clauses"]),
            mc("grammar", "context", "Melyik állítás tükrözi a legpontosabban az egyetemes joghatóság lényegét?", [
                "A legsúlyosabb emberiség elleni bűntettek elkövetői a világ bármely bírósága előtt felelősségre vonhatók.",
                "Csak az elkövetés országában lehet ítéletet hozni.",
                "A bűncselekmények húsz év után törlődnek."
            ], 0, ["c1-universal-jurisdiction"]),
            sb("grammar", "produce", ["Az", "emberi", "méltóság", "védelme", "a", "nemzetközi", "jog", "legfőbb", "parancsa."], ["Az", "emberi", "méltóság", "védelme", "a", "nemzetközi", "jog", "legfőbb", "parancsa."], "Protection of human dignity is the supreme command of international law.", ["c1-correlative-rights"]),
            sw("production", [{"prompt": "Draft a solemn statement on the primacy of human rights over state power.", "answer": "Az emberi jogok olyan veleszületett alapértékek, amelyek mint ilyenek minden állami hatalmat megelőznek, és amelyek tiszteletben tartása a jogállam létezésének feltétele."}], ["c1-correlative-rights"]),
            sw("production", [{"prompt": "Synthesize István Bibó's message on historical self-examination.", "answer": "A történelmi bűnökkel való bátor szembenézés nem a nemzet gyengeségét jelenti, hanem a demokratikus erkölcsi megújulás és az igazságos jövő zálogát."}], ["c1-collective-responsibility"])
        ]
    )

    # ----------------------------------------------------
    # TRACK 2: DISCOURSE (c1-emberijogok)
    # ----------------------------------------------------
    slug = "emberijogok"
    disc_intro = [
        "Human rights and minority protection represent the moral conscience of modern constitutionalism. In Central Europe, shaped by multi-ethnic empires, border shifts, and totalitarian traumas, protecting human dignity and ethnic diversity is a historical imperative.",
        "In this unit, you will analyze the institutional framework of universal rights and minority guarantees: the European Convention on Human Rights (ECHR), minority language charters, Roma desegregation litigation, vulnerable group advocacy, and universal human rights monitoring in Hungary."
    ]

    disc_lessons = [
        {
            "num": 1,
            "stem": f"c1-{slug}-01",
            "title": "The European Convention on Human Rights and Strasbourg Jurisprudence",
            "grammar_title": "ECHR Adjudication: Articles 3, 6, 8, and Just Satisfaction",
            "grammar_skill": "c1-international-treaty-framing",
            "goals": [
                "I can analyze the application of the European Convention on Human Rights in Hungarian courts.",
                "I can evaluate landmark Strasbourg judgements against Hungary (prison overcrowding, length of proceedings).",
                "I can understand the legal concept of 'just satisfaction' (*igazságos elégtétel*) under Article 41 ECHR."
            ],
            "vocab": [
                {"lemma": "Emberi Jogok Európai Egyezménye", "translation": "European Convention on Human Rights (ECHR)", "pos": "noun"},
                {"lemma": "strasbourgi bíróság", "translation": "Strasbourg Court (ECtHR)", "pos": "noun"},
                {"lemma": "tisztességes eljárás", "translation": "fair trial / due process (Art. 6)", "pos": "noun"},
                {"lemma": "igazságos elégtétel", "translation": "just satisfaction (Art. 41)", "pos": "noun"},
                {"lemma": "embertelen bánásmód", "translation": "inhuman or degrading treatment (Art. 3)", "pos": "noun"},
                {"lemma": "túlzsúfoltság", "translation": "overcrowding (penitentiary)", "pos": "noun"},
                {"lemma": "ítélkezési gyakorlat", "translation": "jurisprudence, case law", "pos": "noun"},
                {"lemma": "jogorvoslat kimerítése", "translation": "exhaustion of domestic remedies", "pos": "expression"}
            ],
            "gr_text1": "Hungary ratified the ECHR in 1992. Before filing an application in Strasbourg, an applicant must satisfy the admissibility requirement of *hazai jogorvoslatok kimerítése* (exhaustion of domestic legal remedies).",
            "gr_text2": "Key ECtHR judgements concerning Hungary involve Article 3 (börtön-túlzsúfoltság / inhuman prison conditions) and Article 6 (ésszerű határidő túllépése / unreasonable trial delays), requiring the state to pay *igazságos elégtétel* (just satisfaction).",
            "gr_table": [
                ["A hazai jogorvoslatok kimerítésének szigorú feltétele a strasbourgi beadványoknál...", "Strict requirement of exhaustion of domestic remedies in Strasbourg petitions..."],
                ["Igazságos elégtétel megítélése az elhúzódó bírósági eljárások miatt...", "Awarding just satisfaction due to prolonged court proceedings..."],
                ["Az Emberi Jogok Európai Bíróságának precedensértékű döntései...", "Precedential decisions of the European Court of Human Rights..."]
            ],
            "world_story_seg": {
                "seg_slug": "strasbourg",
                "title": "A strasbourgi bíróság és a polgári jogok európai védőbástyája",
                "summary": "How the European Court of Human Rights provides a final beacon of justice when domestic legal avenues fail.",
                "paragraphs": [
                    {"type": "narration", "text": "Amikor egy állampolgár úgy érzi, hogy saját hazájának bíróságai cserbenhagyták, és minden törvényes jogorvoslati lehetőséget kimerített, van még egy végső fórum Európában. A strasbourgi Emberi Jogok Európai Bírósága az a nemzetközi szentély, amelyhez az Atlanti-óceántól a Kaukázusig több mint hétszázmillió európai polgár fordulhat közvetlen panasszal saját kormánya ellen."},
                    {"type": "narration", "text": "Magyarországról évente beadványok százai érkeznek a Rajna-parti városba. A bíróság döntései nyomán az állam kénytelen volt felszámolni a börtönök méltatlan túlzsúfoltságát, kártérítést fizetni az évtizedekig elhúzódó perek kárvallottjainak, és megerősíteni a tisztességes eljáráshoz való jog garanciáit. Strasbourg ítéletei nem támadást jelentenek a nemzeti szuverenitás ellen, hanem az európai civilizáció közös morális mércéjét érvényesítik."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Milyen feltételnek kell teljesülnie, mielőtt valaki a strasbourgi bírósághoz fordulhat?", ["Kimerítette az összes rendelkezésre álló hazai bírósági jogorvoslatot.", "Írt egy levelet a miniszterelnöknek.", "Kifizette a nemzetközi vámot."], 0, ["c1-emberijogok-vocab"]),
                fb("grammar", "controlled", "A strasbourgi bíróság jogsértés esetén pénzbeli kártérítést, úgynevezett igazságos _____ ítélhet meg a panaszosnak. (satisfaction / elégtételt)", "elégtételt", "In case of violation the Strasbourg court may award financial compensation, so-called just satisfaction, to the applicant.", ["c1-international-treaty-framing"]),
                match("vocabulary", "controlled", [["strasbourgi bíróság", "Strasbourg court"], ["tisztességes eljárás", "fair trial"], ["igazságos elégtétel", "just satisfaction"], ["túlzsúfoltság", "overcrowding"]], ["c1-emberijogok-vocab"]),
                sb("grammar", "practice", ["A", "tisztességes", "eljáráshoz", "való", "jog", "minden", "polgárt", "egyformán", "megillet."], ["A", "tisztességes", "eljáráshoz", "való", "jog", "minden", "polgárt", "egyformán", "megillet."], "The right to a fair trial is equally due to every citizen.", ["c1-international-treaty-framing"]),
                sw("production", [{"prompt": "Explain the significance of Article 6 ECHR (right to fair trial).", "answer": "A 6. cikk garantálja, hogy a vitás polgári jogokat és büntetőjogi vádakat független és pártatlan bíróság, észszerű határidőn belül, nyilvános tárgyaláson bírálja el."}], ["c1-international-treaty-framing"]),
                mc("grammar", "check", "Melyik bánásmódot tiltja abszolút jelleggel az Egyezmény 3. cikke?", [
                    "A kínzást, valamint az embertelen vagy megalázó bánásmódot és büntetést.",
                    "A közlekedési bírságok kiszabását.",
                    "A késedelmes adóbevallást."
                ], 0, ["c1-international-treaty-framing"])
            ]
        },
        {
            "num": 2,
            "stem": f"c1-{slug}-02",
            "title": "Minority Language Charters and Regional Mother Tongues",
            "grammar_title": "The European Charter for Regional or Minority Languages in Hungary",
            "grammar_skill": "c1-minority-protection-clauses",
            "goals": [
                "I can analyze the European Charter for Regional or Minority Languages (*Regionális vagy Kisebbségi Nyelvek Európai Kartája*).",
                "I can evaluate bilingual public signage and native-language administration in multi-ethnic settlements.",
                "I can discuss language preservation strategies for endangered minority dialects in Hungary."
            ],
            "vocab": [
                {"lemma": "Kisebbségi Nyelvi Karta", "translation": "Charter for Regional or Minority Languages", "pos": "noun"},
                {"lemma": "kétnyelvű helységnévtábla", "translation": "bilingual place-name sign", "pos": "noun"},
                {"lemma": "anyanyelvi oktatás", "translation": "native-language education", "pos": "noun"},
                {"lemma": "veszélyeztetett nyelv", "translation": "endangered language", "pos": "noun"},
                {"lemma": "nyelvi revitalizáció", "translation": "linguistic revitalization", "pos": "noun"},
                {"lemma": "hagyományos nyelvjárás", "translation": "traditional dialect", "pos": "noun"},
                {"lemma": "kulturális örökség", "translation": "cultural heritage", "pos": "noun"},
                {"lemma": "többségi társadalom", "translation": "majority society", "pos": "noun"}
            ],
            "gr_text1": "Hungary signed and ratified the *Regionális vagy Kisebbségi Nyelvek Európai Kartája*, undertaking specific commitments for 14 minority languages (including German, Slovak, Romanian, Serbian, Croatian, Romani, and Boyash).",
            "gr_text2": "Under the Charter, multi-ethnic municipalities must provide bilingual place-name signs (*kétnyelvű helységnévtáblák*), mother-tongue kindergarten instruction, and translation in official local government proceedings.",
            "gr_table": [
                ["A Kisebbségi Nyelvi Karta előírásainak végrehajtása Magyarországon...", "Implementation of Minority Language Charter rules in Hungary..."],
                ["Kétnyelvű helységnévtáblák kihelyezése és hivatali nyelvhasználat...", "Erecting bilingual place-name signs and official language use..."],
                ["A roma nyelvek (lovári és beás) elismerése és nyelvi revitalizációja...", "Recognition and revitalization of Romani languages (Lovari and Boyash)..."]
            ],
            "world_story_seg": {
                "seg_slug": "nyelvikarta",
                "title": "Sokszínű Kárpát-medence: a kisebbségi nyelvek védelme",
                "summary": "How international treaties and local communities protect the rich tapestry of minority languages in Hungarian villages and towns.",
                "paragraphs": [
                    {"type": "narration", "text": "Amikor az utazó Baranya falvait járja, sváb és horvát feliratú táblákkal találkozik; Békésben a szlovák és a román szó csendül fel a templomokban, míg Szabolcsban a lovári és a beás cigány nyelv őrzi évszázados szóbeli hagyományait. Magyarország nem egynyelvű sziget, hanem a Kárpát-medence sokszínű nyelvi és kulturális szövetének szerves része."},
                    {"type": "narration", "text": "A Regionális vagy Kisebbségi Nyelvek Európai Kartája jogi védőpajzsot von e törékeny örökség köré. A törvény garantálja, hogy a nemzetiségi közösségek saját nyelvükön tanulhassanak az óvodától az érettségiig, és saját anyanyelvüket használhassák a helyi önkormányzati testületekben. Egy nyelv kihalása pótolhatatlan veszteség az egész emberiség számára; megőrzésük a többségi nemzet legnemesebb kulturális kötelessége."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Milyen nemzetközi dokumentum védi a magyarországi kisebbségek anyanyelvét?", ["A Regionális vagy Kisebbségi Nyelvek Európai Kartája.", "A Párizsi Klímaegyezmény.", "A Nemzetközi Vasúti Szabályzat."], 0, ["c1-emberijogok-vocab"]),
                fb("grammar", "controlled", "A nemzetiségi településeken a törvény kötelezővé teszi a kétnyelvű _____ kihelyezését. (place-name signs / helységnévtáblák)", "helységnévtáblák", "In nationality settlements the statute makes erecting bilingual place-name signs mandatory.", ["c1-minority-protection-clauses"]),
                match("vocabulary", "controlled", [["Kisebbségi Nyelvi Karta", "Minority Language Charter"], ["kétnyelvű helységnévtábla", "bilingual place-name sign"], ["anyanyelvi oktatás", "mother-tongue education"], ["veszélyeztetett nyelv", "endangered language"]], ["c1-emberijogok-vocab"]),
                sb("grammar", "practice", ["A", "nyelvi", "sokszínűség", "megőrzése", "a", "közös", "kulturális", "örökség", "része."], ["A", "nyelvi", "sokszínűség", "megőrzése", "a", "közös", "kulturális", "örökség", "része."], "Preservation of linguistic diversity is part of common cultural heritage.", ["c1-minority-protection-clauses"]),
                sw("production", [{"prompt": "Explain why preserving minority languages is a duty of the majority society.", "answer": "A kisebbségi nyelvek a közös történelmi és kulturális örökség részei; megőrzésük nem kiváltság, hanem az emberi méltóság és a sokszínűség alapvető védelme."}], ["c1-minority-protection-clauses"]),
                mc("grammar", "check", "Milyen oktatási jog illeti meg a magyarországi nemzetiségeket?", [
                    "Joguk van az anyanyelvű vagy kétnyelvű oktatáshoz az óvodától a középiskoláig.",
                    "Kizárólag magyar nyelven tanulhatnak.",
                    "Nem járhatnak iskolába."
                ], 0, ["c1-minority-protection-clauses"])
            ]
        },
        {
            "num": 3,
            "stem": f"c1-{slug}-03",
            "title": "Educational Desegregation and Roma Civil Rights: The Gyöngyöspata Precedent",
            "grammar_title": "Strategic Human Rights Litigation: Desegregation and Damages",
            "grammar_skill": "c1-minority-protection-clauses",
            "goals": [
                "I can analyze strategic litigation on educational segregation (*iskolai szegregáció, deszegregáció*).",
                "I can evaluate the landmark Gyöngyöspata Kúria judgment awarding non-material damages.",
                "I can discuss systemic exclusion, prejudice, and equal opportunity policies in Hungary."
            ],
            "vocab": [
                {"lemma": "iskolai szegregáció", "translation": "school segregation", "pos": "noun"},
                {"lemma": "deszegregáció", "translation": "desegregation, integration", "pos": "noun"},
                {"lemma": "nem vagyoni kártérítés", "translation": "non-pecuniary / non-material damages (sérelemdíj)", "pos": "noun"},
                {"lemma": "egyenlő bánásmód", "translation": "equal treatment, non-discrimination", "pos": "noun"},
                {"lemma": "szisztematikus kirekesztés", "translation": "systemic exclusion", "pos": "noun"},
                {"lemma": "stratégiai pereskedés", "translation": "strategic human rights litigation", "pos": "noun"},
                {"lemma": "Kúria", "translation": "Curia of Hungary (Supreme Court)", "pos": "noun"},
                {"lemma": "esélyegyenlőség", "translation": "equality of opportunity", "pos": "noun"}
            ],
            "gr_text1": "Strategic human rights litigation (*stratégiai pereskedés*) uses court cases to dismantle systemic discrimination. In the landmark *Gyöngyöspata* lawsuit, civil rights lawyers proved that Roma children were segregated into substandard classrooms.",
            "gr_text2": "In 2020, the Hungarian Supreme Court (*Kúria*) affirmed the award of substantial non-material damages (*sérelemdíj*), establishing that educational segregation causes irreparable harm to dignity and future life chances.",
            "gr_table": [
                ["A jogellenes iskolai szegregáció bírósági megállapítása...", "Judicial establishment of unlawful school segregation..."],
                ["Nem vagyoni kártérítés (sérelemdíj) megítélése a szegregált diákoknak...", "Awarding non-material damages to segregated students..."],
                ["Az egyenlő bánásmód követelményének érvényesítése a közoktatásban...", "Enforcing the equal treatment requirement in public education..."]
            ],
            "world_story_seg": {
                "seg_slug": "szegregacio",
                "title": "A gyöngyöspatai per és az egyenlő esélyek harca",
                "summary": "How a historic strategic lawsuit against segregated education reached the Supreme Court and became a milestone of Roma civil rights.",
                "paragraphs": [
                    {"type": "narration", "text": "Amikor a Heves megyei Gyöngyöspata általános iskolájában a roma gyermekeket elkülönített osztálytermekbe, a földszintre szorították, és megfosztották őket a színvonalas oktatástól és az iskolai kirándulásoktól, nemcsak pedagógiai hiba történt: az egyenlő emberi méltóság alkotmányos parancsa sérült meg brutálisan. A roma szülők és az Esélyt a Hátrányos Helyzetű Gyerekeknek Alapítvány (CFA) jogászai elhatározták, hogy bíróság elé viszik az ügyet."},
                    {"type": "narration", "text": "A per éveken át tartott, és a legfelsőbb bírói fórumig, a Kúriáig jutott. 2020-ban a Kúria történelmi ítéletében kimondta: a szegregáció jogellenes volt, és több mint százmillió forintos nem vagyoni kártérítést (sérelemdíjat) ítélt meg a megalázott diákoknak. Az ítélet világos üzenetet küldött: a származás szerinti elkülönítés nem fogadható el egy európai jogállamban, és az oktatás valódi esélyegyenlősége minden gyermek elidegeníthetetlen joga."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Mi volt a gyöngyöspatai per legfontosabb jogi tanulsága?", ["Hogy az iskolai etnikai szegregáció jogellenes, és sérelemdíj megfizetésére kötelezi az intézményfenntartót.", "Hogy a bíróságok nem foglalkoznak iskolákkal.", "Hogy a diákoknak nem kell tanulniuk."], 0, ["c1-emberijogok-vocab"]),
                fb("grammar", "controlled", "A Kúria jogerős ítéletében megállapította az egyenlő _____ követelményének súlyos megsértését. (treatment / bánásmód)", "bánásmód", "In its final judgment the Curia established the severe violation of the equal treatment requirement.", ["c1-minority-protection-clauses"]),
                match("vocabulary", "controlled", [["iskolai szegregáció", "school segregation"], ["deszegregáció", "desegregation"], ["nem vagyoni kártérítés", "non-material damages"], ["Kúria", "Curia (Supreme Court)"]], ["c1-emberijogok-vocab"]),
                sb("grammar", "practice", ["Minden", "gyermeknek", "joga", "van", "a", "diszkriminációmentes", "és", "minőségi", "oktatáshoz."], ["Minden", "gyermeknek", "joga", "van", "a", "diszkriminációmentes", "és", "minőségi", "oktatáshoz."], "Every child has the right to non-discriminatory and quality education.", ["c1-minority-protection-clauses"]),
                sw("production", [{"prompt": "Describe the societal harm caused by ethnic school segregation.", "answer": "A szegregáció elmélyíti a társadalmi előítéleteket, megfosztja a hátrányos helyzetű gyermekeket a kitörés esélyétől, és aláássa a társadalmi integráció és békés együttélés alapjait."}], ["c1-minority-protection-clauses"]),
                mc("grammar", "check", "Milyen jogi eszközzel éltek a jogvédők a szegregált diákok képviseletében?", [
                    "Stratégiai pereskedéssel az egyenlő bánásmód megsértése miatt.",
                    "Fegyveres demonstrációval.",
                    "Az iskola bezárásának követelésével."
                ], 0, ["c1-minority-protection-clauses"])
            ]
        },
        {
            "num": 4,
            "stem": f"c1-{slug}-04",
            "title": "Advocacy for Vulnerable Groups: Disability Rights and Child Protection",
            "grammar_title": "Legal Capacity, Accessibility, and the UN CRPD Framework",
            "grammar_skill": "c1-universal-jurisdiction",
            "goals": [
                "I can analyze the UN Convention on the Rights of Persons with Disabilities (CRPD).",
                "I can evaluate supported decision-making (*támogatott döntéshozatal*) vs. legal guardianship (*gondnokság*).",
                "I can discuss child protection systems and institutional reform in Hungarian law."
            ],
            "vocab": [
                {"lemma": "fogyatékossággal élő személyek", "translation": "persons with disabilities", "pos": "expression"},
                {"lemma": "akadálymentesítés", "translation": "accessibility / removal of barriers", "pos": "noun"},
                {"lemma": "cselekvőképesség", "translation": "legal capacity", "pos": "noun"},
                {"lemma": "gondnokság alá helyezés", "translation": "placing under guardianship / conservatorship", "pos": "noun"},
                {"lemma": "támogatott döntéshozatal", "translation": "supported decision-making", "pos": "noun"},
                {"lemma": "gyermekvédelem", "translation": "child protection", "pos": "noun"},
                {"lemma": "kitagolás", "translation": "deinstitutionalization (large care homes)", "pos": "noun"},
                {"lemma": "önálló életvitel", "translation": "independent living", "pos": "noun"}
            ],
            "gr_text1": "The UN CRPD prompted a paradigm shift in Hungarian civil law: replacing plenary guardianship (*kizáró gondnokság*) with *támogatott döntéshozatal* (supported decision-making), preserving the legal capacity (*cselekvőképesség*) of persons with disabilities.",
            "gr_text2": "In child protection and disability care, international human rights law mandates *kitagolás* (deinstitutionalization): transitioning residents from isolated mega-institutions to community-based supported apartments (*támogatott lakhatás*).",
            "gr_table": [
                ["A támogatott döntéshozatal bevezetése a gondnokság helyett...", "Introducing supported decision-making instead of guardianship..."],
                ["Fizikai és infokommunikációs akadálymentesítés mint alapjog...", "Physical and info-communication accessibility as a fundamental right..."],
                ["A nagy létszámú szociális otthonok kitagolása és közösségi lakhatás...", "Deinstitutionalization of mass care homes and community living..."]
            ],
            "world_story_seg": {
                "seg_slug": "fogyatekossagjogok",
                "title": "Az önálló élet joga: a fogyatékosság és a méltóság",
                "summary": "How the modern human rights model transformed disability advocacy from paternalism to self-determination and community integration.",
                "paragraphs": [
                    {"type": "narration", "text": "Hosszú évszázadokon át a társadalom a fogyatékossággal élő személyeket szomorú sorsú, tehetetlen gondozottakként kezelte, akiket távoli, zárt intézményekbe kell zárni, és meg kell fosztani minden döntési joguktól. A huszonegyedik században azonban a fogyatékosságjogi mozgalom gyökeres szemléletváltást ért el az ENSZ egyezményének elfogadásával: a jótékonyság helyébe az emberi jogok és az önálló életvitel követelménye lépett."},
                    {"type": "narration", "text": "Magyarországon az új Polgári Törvénykönyv megteremtette a támogatott döntéshozatal intézményét. A cél többé nem a cselekvőképesség elvétele, hanem a segítés: hogy az érintettek saját akaratuk szerint köthessenek szerződést, vállalhassanak munkát és alapíthassanak családot. A fizikai és infokommunikációs akadálymentesítés, valamint a nagy intézmények felszámolása nem kegy, hanem annak elismerése, hogy minden ember teljes jogú és értékes tagja a társadalomnak."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Mi a célja a 'támogatott döntéshozatal' jogintézményének?", ["Hogy a fogyatékossággal élő személy saját jogán hozhasson döntéseket segítő támogatásával a cselekvőképesség elvétele helyett.", "Hogy a bíróság döntsön helyette mindenben.", "Hogy tiltsa a munkavállalást."], 0, ["c1-emberijogok-vocab"]),
                fb("grammar", "controlled", "A modern jog célja a nagy intézmények felszámolása és a közösségi támogatott _____ megteremtése. (living / housing / lakhatás)", "lakhatás", "The goal of modern law is the closure of large institutions and creating community supported housing.", ["c1-universal-jurisdiction"]),
                match("vocabulary", "controlled", [["cselekvőképesség", "legal capacity"], ["támogatott döntéshozatal", "supported decision-making"], ["akadálymentesítés", "accessibility"], ["kitagolás", "deinstitutionalization"]], ["c1-emberijogok-vocab"]),
                sb("grammar", "practice", ["A", "fogyatékossággal", "élő", "emberek", "méltósága", "és", "önrendelkezése", "sérthetetlen."], ["A", "fogyatékossággal", "élő", "emberek", "méltósága", "és", "önrendelkezése", "sérthetetlen."], "The dignity and self-determination of persons with disabilities is inviolable.", ["c1-universal-jurisdiction"]),
                sw("production", [{"prompt": "Contrast paternalistic guardianship with supported decision-making.", "answer": "Míg a gondnokság alá helyezés megfosztja az egyént cselekvőképességétől és másokra bízza a döntéseket, addig a támogatott döntéshozatal megőrzi a személy autonómiáját segítő bevonásával."}], ["c1-universal-jurisdiction"]),
                mc("grammar", "check", "Miért tekintendő alapjogi kérdésnek az akadálymentesítés?", [
                    "Mert az egyenlő hozzáférés hiánya elzárja a fogyatékossággal élőket az oktatástól, a munkától és a közélettől.",
                    "Mert csak a mérnökök érdekeit szolgálja.",
                    "Mert az építkezések drágábbá válnak tőle."
                ], 0, ["c1-universal-jurisdiction"])
            ]
        },
        {
            "num": 5,
            "stem": f"c1-{slug}-05",
            "title": "Human Rights Monitoring, Paris Principles and the Rule of Law",
            "grammar_title": "National Human Rights Institutions (NHRIs) and Global Compliance",
            "grammar_skill": "c1-universal-jurisdiction",
            "goals": [
                "I can analyze the Paris Principles governing National Human Rights Institutions (NHRIs).",
                "I can evaluate universal periodic reviews (UPR) before the UN Human Rights Council.",
                "I can synthesize the overarching architecture of human rights compliance in 21st-century Hungary."
            ],
            "vocab": [
                {"lemma": "Párizsi Elvek", "translation": "Paris Principles (standards for NHRIs)", "pos": "noun"},
                {"lemma": "Egyetemes Időszakos Felülvizsgálat", "translation": "Universal Periodic Review (UPR / ENSZ)", "pos": "noun"},
                {"lemma": "nemzeti emberi jogi intézmény", "translation": "National Human Rights Institution (NHRI)", "pos": "noun"},
                {"lemma": "függetlenség garanciái", "translation": "guarantees of independence", "pos": "expression"},
                {"lemma": "kormányközi szervezet", "translation": "intergovernmental organization", "pos": "noun"},
                {"lemma": "ajánlások implementációja", "translation": "implementation of recommendations", "pos": "expression"},
                {"lemma": "jogállami monitoring", "translation": "rule of law monitoring", "pos": "noun"},
                {"lemma": "társadalmi szolidaritás", "translation": "societal solidarity", "pos": "noun"}
            ],
            "gr_text1": "Under the UN Paris Principles, a National Human Rights Institution (*nemzeti emberi jogi intézmény*) must possess complete constitutional, operational, and financial independence from the government.",
            "gr_text2": "During the UN Universal Periodic Review (*Egyetemes Időszakos Felülvizsgálat / UPR*), every state's human rights record is examined every 4.5 years in Geneva by peer nations, civil society coalitions, and international rapporteurs.",
            "gr_table": [
                ["A Párizsi Elveknek megfelelő 'A-státuszú' nemzeti emberi jogi intézmény...", "An 'A-status' National Human Rights Institution complying with Paris Principles..."],
                ["Magyarország felülvizsgálata az ENSZ Emberi Jogi Tanácsa előtt...", "Hungary's review before the UN Human Rights Council..."],
                ["A nemzetközi emberi jogi ajánlások következetes végrehajtása...", "Consistent implementation of international human rights recommendations..."]
            ],
            "world_story_seg": {
                "seg_slug": "parisprinciples",
                "title": "Genftől Budapestig: az emberi jogok globális őrszemei",
                "summary": "How global human rights monitoring through the United Nations and independent national institutions holds modern states accountable.",
                "paragraphs": [
                    {"type": "narration", "text": "A genfi Nemzetek Palotájának boltíves termeiben négy és fél évente minden nemzetnek számot kell adnia arról, hogyan védi polgárai szabadságát. Az ENSZ Emberi Jogi Tanácsának Egyetemes Időszakos Felülvizsgálata (UPR) páratlan fórum: itt nincsenek szuperhatalmak és kisállamok, minden kormány egyenlő mérce alá esik. Magyarország delegációja előtt svéd, kanadai, brazil vagy dél-afrikai diplomaták tesznek fel kényelmetlen kérdéseket az igazságszolgáltatás függetlenségéről, a romák integrációjáról és a sajtószabadságról."},
                    {"type": "narration", "text": "A globális ellenőrzés hazai pillérét az úgynevezett nemzeti emberi jogi intézmények alkotják, amelyeknek meg kell felelniük az ENSZ Párizsi Elveinek. A valódi függetlenség azt jelenti, hogy a jogvédő intézmény nem szolgálhatja a pillanatnyi kormányzati érdekeket; kötelessége a legkiszolgáltatottabbak mellé állni akkor is, ha ez politikai konfliktussal jár. Mert az emberi jogok tisztelete nem nemzetközi divat vagy bürokratikus kötelezettség, hanem a szabad és méltóságteljes emberi élet egyetlen lehetséges fundamentuma."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Mit írnak elő az ENSZ 'Párizsi Elvei' a nemzeti emberi jogi intézmények számára?", ["Teljes körű törvényes, működési és pénzügyi függetlenséget a mindenkori kormányzattól.", "Közös irodát a rendőrséggel.", "A panaszosok nyilvános listázását."], 0, ["c1-emberijogok-vocab"]),
                fb("grammar", "controlled", "Az ENSZ UPR eljárásában Magyarország kormánya Genfben ad számot az emberi jogi ajánlások _____ állapotáról. (implementation / implementációjának / végrehajtásának)", "végrehajtásának", "In the UN UPR procedure the government of Hungary reports in Geneva on the status of implementation of human rights recommendations.", ["c1-universal-jurisdiction"]),
                match("vocabulary", "controlled", [["Párizsi Elvek", "Paris Principles"], ["nemzeti emberi jogi intézmény", "national human rights institution"], ["jogállami monitoring", "rule of law monitoring"], ["társadalmi szolidaritás", "societal solidarity"]], ["c1-emberijogok-vocab"]),
                sb("grammar", "practice", ["A", "független", "emberi", "jogi", "monitoring", "a", "demokrácia", "nélkülözhetetlen", "tartópillére."], ["A", "független", "emberi", "jogi", "monitoring", "a", "demokrácia", "nélkülözhetetlen", "tartópillére."], "Independent human rights monitoring is the indispensable pillar of democracy.", ["c1-universal-jurisdiction"]),
                sw("production", [{"prompt": "Explain why independence is the single most critical attribute of a National Human Rights Institution.", "answer": "Függetlenség nélkül az emberi jogi intézmény puszta kormányzati propagandaszervvé silányul, elveszítve a polgárok bizalmát és a képességét arra, hogy megvédje az áldozatokat a hatalommal szemben."}], ["c1-universal-jurisdiction"]),
                mc("grammar", "check", "Milyen célt szolgál az ENSZ Egyetemes Időszakos Felülvizsgálata (UPR)?", [
                    "Hogy a világ összes állama rendszeresen és kölcsönösen értékelje egymás emberi jogi helyzetét nemzetközi nyilvánosság előtt.",
                    "Hogy új valutát vezessenek be.",
                    "Hogy megszüntessék az ENSZ működését."
                ], 0, ["c1-universal-jurisdiction"])
            ]
        }
    ]

    for l in disc_lessons:
        emit_instructional_lesson(11, "discourse", l, disc_title, disc_intro if l["num"] == 1 else None)

    # Combined world story
    write_json(
        f"stories/world/c1/{slug}.json",
        {
            "id": f"story.c1.world.{slug}",
            "title": "Az egyetemes emberi jogok és a kisebbségvédelem krónikája",
            "level": "C1",
            "type": "world",
            "summary": "Comprehensive chronicle of international human rights and minority protections: ECHR Strasbourg litigation, the European Charter for Regional or Minority Languages, Gyöngyöspata Roma desegregation judgments, disability rights under the CRPD, to UN Paris Principles monitoring.",
            "paragraphs": [
                {"type": "narration", "text": "Az emberi jogok és a kisebbségvédelem eszméje az európai alkotmányos kultúra legfényesebb morális vívmánya. A huszadik század pusztító tragédiáira adott válaszként megszületett az a felismerés, hogy az egyén méltósága minden állami hatalom felett áll, és a nemzeti kisebbségek védelme a kontinens békéjének záloga."},
                {"type": "narration", "text": "A strasbourgi Emberi Jogok Európai Bírósága a végső menedéket jelenti az állami jogsértésekkel szemben, míg a Kisebbségi Nyelvi Karta a Kárpát-medence sokszínű nyelvi és kulturális szövetét óvja a beolvadástól."},
                {"type": "narration", "text": "A gyöngyöspatai deszegregációs per történelmi kúriai ítélete bebizonyította a stratégiai pereskedés erejét: kimondta, hogy a kirekesztés és a származás szerinti elkülönítés súlyos, kártérítést érdemlő jogsértés a modern Magyarországon."},
                {"type": "narration", "text": "A fogyatékossággal élők mozgalma az önrendelkezést és a támogatott döntéshozatalt állította a korábbi paternalizmus helyébe, miközben az ENSZ globális mechanizmusai és a Párizsi Elvek éber monitoringot gyakorolnak a jogállami normák felett."},
                {"type": "narration", "text": "Ez a sokrétű jogvédelmi háló Bibó István örökségét folytatja: arra emlékeztet, hogy a szabadság egy és oszthatatlan, és egyetlen társadalom sem nevezheti magát igazságosnak mindaddig, amíg a legkiszolgáltatottabbak méltósága veszélyben forog."}
            ]
        }
    )

    # Discourse Consolidation
    emit_consolidation_lesson(
        11,
        "discourse",
        f"c1-{slug}-consolidation",
        disc_title,
        [
            "I can navigate ECHR Strasbourg litigation, Article 6 fair trial, and just satisfaction awards.",
            "I can evaluate the European Minority Language Charter, bilingual signage, and educational desegregation.",
            "I can analyze disability rights under the CRPD, supported decision-making, and UN Paris Principles monitoring."
        ],
        [
            mc("grammar", "recognize", "Milyen feltétel szükséges a strasbourgi bírósághoz forduláshoz?", [
                "A hazai bírósági jogorvoslatok teljes kimerítése.",
                "Külföldi állampolgárság megszerzése.",
                "Az ügyvédi kamarai tagság megléte."
            ], 0, ["c1-international-treaty-framing"]),
            mc("grammar", "recognize", "Mi volt a Kúria gyöngyöspatai ítéletének legfőbb üzenete?", [
                "Az iskolai etnikai szegregáció jogellenes, és nem vagyoni kártérítéssel büntetendő.",
                "Hogy a szegregáció hasznos dolog.",
                "Hogy a bíróságok nem avatkozhatnak be az oktatásba."
            ], 0, ["c1-minority-protection-clauses"]),
            match("vocabulary", "recognize", [["strasbourgi bíróság", "Strasbourg court"], ["Kisebbségi Nyelvi Karta", "Minority Language Charter"], ["deszegregáció", "desegregation"], ["támogatott döntéshozatal", "supported decision-making"], ["Párizsi Elvek", "Paris Principles"]], ["c1-emberijogok-vocab"]),
            fb("vocabulary", "recall", "A strasbourgi bíróság jogsértés esetén igazságos _____ ítélhet meg a panaszosnak. (satisfaction / elégtételt)", "elégtételt", "In case of violation the Strasbourg court may award just satisfaction to the applicant.", ["c1-emberijogok-vocab"]),
            fb("vocabulary", "recall", "A fogyatékossággal élők számára az _____ biztosítja a társadalmi életben való egyenlő részvételt. (accessibility / akadálymentesítés)", "akadálymentesítés", "For persons with disabilities accessibility ensures equal participation in societal life.", ["c1-emberijogok-vocab"]),
            fb("grammar", "recall", "A nemzetiségi településeken a kétnyelvű helységnévtáblák kihelyezése törvényi _____ alapul. (obligation / kötelezettségen)", "kötelezettségen", "In nationality settlements erecting bilingual place-name signs is based on statutory obligation.", ["c1-minority-protection-clauses"]),
            fb("grammar", "context", "A nemzeti emberi jogi intézményeknek meg kell felelniük az ENSZ _____ Elveinek a teljes függetlenség biztosítására. (Paris / Párizsi)", "Párizsi", "National human rights institutions must comply with UN Paris Principles to ensure full independence.", ["c1-universal-jurisdiction"]),
            fb("grammar", "context", "A cselekvőképesség elvétele helyett a modern jog a _____ döntéshozatalt részesíti előnyben. (supported / támogatott)", "támogatott", "Instead of stripping legal capacity modern law prefers supported decision-making.", ["c1-universal-jurisdiction"]),
            mc("grammar", "context", "Melyik állítás foglalja össze legmélyebben az egyetemes emberi jogok filozófiáját?", [
                "Az emberi méltóság egyetemes és sérthetetlen; védelme minden államhatalmat megelőző legfőbb kötelezettség.",
                "A jogok csak a legerősebbeket illetik meg.",
                "Az emberi jogok felesleges elméletek a mindennapi életben."
            ], 0, ["c1-universal-jurisdiction"]),
            sb("grammar", "produce", ["A", "kisebbségek", "védelme", "a", "demokrácia", "és", "a", "béke", "nélkülözhetetlen", "záloga."], ["A", "kisebbségek", "védelme", "a", "demokrácia", "és", "a", "béke", "nélkülözhetetlen", "záloga."], "Protection of minorities is the indispensable pledge of democracy and peace.", ["c1-minority-protection-clauses"]),
            sw("production", [{"prompt": "Write a critical evaluation of strategic litigation in defending human rights.", "answer": "A stratégiai pereskedés hatékony jogi fegyver: egyetlen precedensértékű bírósági ítélettel képes rendszerszintű diszkriminációt felszámolni és jogszabály-módosításra kényszeríteni a döntéshozókat."}], ["c1-minority-protection-clauses"]),
            sw("production", [{"prompt": "Formulate a concluding thought on human rights advocacy in Central Europe.", "answer": "Közép-Európa történelmi viharai arra tanítanak, hogy a szabadság valódi mércéje a kisebbségek és a kiszolgáltatottak védelme a többség önkényével szemben."}], ["c1-universal-jurisdiction"])
        ]
    )
    print("=== Finished C1 Unit 11 ===")


if __name__ == "__main__":
    generate_unit_11()
