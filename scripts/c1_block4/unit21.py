#!/usr/bin/env python3
"""
Hungarian C1 Block 4 - Unit 21 Generator:
  - Track 1 (Core): Unit 21 — "Labor Economics, Technological Displacement & Collective Bargaining" (c1-21)
  - Track 2 (Discourse): Unit 21 — "The Dual Labor Market: Guest Workers, Gig Economy & Wage Convergence" (c1-munkaeropiac)
"""

import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT))

from scripts.c1_block1.common import mc, match, fb, sb, dc, sw, write_json, emit_instructional_lesson, emit_consolidation_lesson
from scripts.c1_block4.registry_helper import register_unit


def generate_unit_21():
    print("=== Generating C1 Unit 21 ===")
    
    # Register skills & titles
    new_skills = {
        "c1-21-vocab": {"kind": "vocabulary"},
        "c1-munkaeropiac-vocab": {"kind": "vocabulary"},
        "c1-adv-economic-concession-markers": {"kind": "grammar"},
        "c1-passive-institutional-impersonals": {"kind": "grammar"},
        "c1-rhetorical-causal-participles": {"kind": "grammar"},
        "c1-adv-scalar-wage-disparities": {"kind": "grammar"},
        "c1-modal-deontic-labor-rights": {"kind": "grammar"},
        "c1-discourse-polarization-antithesis": {"kind": "grammar"},
        "c1-adv-temporal-succession-chains": {"kind": "grammar"},
        "c1-modal-teleological-labor-policy": {"kind": "grammar"},
        "c1-epistemic-labor-market-projections": {"kind": "grammar"},
        "c1-adv-synthetic-collective-evaluatives": {"kind": "grammar"},
    }
    new_titles = {
        "c1-21-vocab": "reading",
        "c1-munkaeropiac-vocab": "reading",
        "c1-adv-economic-concession-markers": "concessive adverbial structures weighing industrial modernization against labor precarity",
        "c1-passive-institutional-impersonals": "impersonal passive verbal constructions conveying structural labor market conditions",
        "c1-rhetorical-causal-participles": "complex causal participial modifiers diagnosing systemic employment vulnerability",
        "c1-adv-scalar-wage-disparities": "scalar disparity adverbials measuring wage divergence and inflation erosion",
        "c1-modal-deontic-labor-rights": "deontic modal expressions articulating collective bargaining and statutory worker rights",
        "c1-discourse-polarization-antithesis": "antithetical discourse markers contrasting corporate flexibility with worker vulnerability",
        "c1-adv-temporal-succession-chains": "temporal succession adverbials mapping sequential shifts in industrial employment structures",
        "c1-modal-teleological-labor-policy": "teleological postpositional structures formulating statutory employment policy targets",
        "c1-epistemic-labor-market-projections": "epistemic stance adverbials calibrating certainty in macroeconomic labor forecasts",
        "c1-adv-synthetic-collective-evaluatives": "evaluative synthesis particles formulating comprehensive assessments of labor rights",
    }
    
    core_title = "Labor Economics, Technological Displacement & Collective Bargaining"
    core_stems = [f"c1-21-0{i}" for i in range(1, 6)] + ["c1-21-consolidation"]
    disc_title = "The Dual Labor Market: Guest Workers, Gig Economy & Wage Convergence"
    disc_stems = [f"c1-munkaeropiac-0{i}" for i in range(1, 6)] + ["c1-munkaeropiac-consolidation"]
    
    register_unit(21, core_title, core_stems, disc_title, disc_stems, new_skills, new_titles)

    # ----------------------------------------------------
    # TRACK 1: CORE (c1-21)
    # ----------------------------------------------------
    core_intro = [
        "The transformation of labor in Central Europe is marked by severe structural tensions: the legacy of industrial proletarianization, the vulnerability of unskilled workers, the erosion of strike rights, and the rise of digital and automated production.",
        "In this unit, anchored by Nagy Lajos's merciless 1934 sociographical investigation 'Kiskunhalom', you will master the elevated academic register used to analyze labor precarity, institutional impersonals, wage disparities, and collective bargaining rights at the C1 level."
    ]

    core_lessons = [
        {
            "num": 1,
            "stem": "c1-21-01",
            "title": "Industrial Modernization vs. Labor Precarity: Economic Concessives",
            "grammar_title": "Concessive Adverbial Structures Weighing Industrial Modernization Against Labor Precarity",
            "grammar_skill": "c1-adv-economic-concession-markers",
            "goals": [
                "I can analyze industrial restructuring, labor market precarity, and automation (*munkaerőpiaci prekariátus, reindusztrializáció, technológiai munkanélküliség*).",
                "I can construct elevated economic concessive structures (*jóllehet... mindamellett, noha... ugyanakkor, ámbátor... mégsem*).",
                "I can debate the trade-offs between corporate competitiveness and worker vulnerability in academic prose."
            ],
            "vocab": [
                {"lemma": "prekariátus", "translation": "precariat / precarious workforce", "pos": "noun"},
                {"lemma": "reindusztrializáció", "translation": "re-industrialization", "pos": "noun"},
                {"lemma": "technológiai munkanélküliség", "translation": "technological unemployment", "pos": "expression"},
                {"lemma": "munkaerőpiaci polarizáció", "translation": "labor market polarization", "pos": "expression"},
                {"lemma": "szerkezeti munkanélküliség", "translation": "structural unemployment", "pos": "expression"},
                {"lemma": "bérköltség-versenyképesség", "translation": "wage cost competitiveness", "pos": "expression"},
                {"lemma": "hozzáadott érték", "translation": "added value", "pos": "expression"},
                {"lemma": "munkaerő-elszívás", "translation": "labor drain / brain drain", "pos": "noun"}
            ],
            "gr_text1": "Economic concessives balance industrial macroeconomic growth against localized social vulnerability: `jóllehet... mindamellett` (even though... nonetheless), `noha... ugyanakkor` (while... at the same time), `ámbátor... mégsem` (although... yet not). Example: `Jóllehet a reindusztrializáció növelte a GDP-t, mindamellett a munkavállalók kiszolgáltatottsága és a prekariátus aránya aggasztóan emelkedett`.",
            "gr_text2": "These constructions prevent simplistic binary arguments and allow nuanced evaluation of complex industrial transformations.",
            "gr_table": [
                ["Jóllehet a gyárak robotizálása növelte a hatékonyságot, mindamellett ezrek veszítették el állásukat.", "Even though factory robotization increased efficiency, nonetheless thousands lost their jobs."],
                ["Noha a gazdaság növekszik, ugyanakkor a reálbérek vásárlóereje csökkent.", "While the economy is growing, at the same time the purchasing power of real wages decreased."],
                ["Ámbátor az új üzemek munkahelyet teremtenek, mégsem garantálnak biztos jövőt.", "Although the new plants create jobs, they yet do not guarantee a secure future."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mit nevez a szociológia 'prekariátusnak' a munka világában?", [
                    "A létbizonytalanságban élő, határozott idejű, kiszolgáltatott szerződésekkel foglalkoztatott dolgozói réteget.",
                    "A legmagasabb fizetéssel rendelkező banki vezetőket.",
                    "A nyugdíjas korú művészek önkéntes szövetségét."
                ], 0, ["c1-21-vocab"]),
                fb("grammar", "controlled", "Jóllehet a gyárak termelése csúcsot döntött, _____ a szalagmunkások bére alig emelkedett. (nonetheless / mindamellett)", "mindamellett", "Even though factory output broke records, nonetheless the wage of assembly workers barely rose.", ["c1-adv-economic-concession-markers"]),
                match("vocabulary", "controlled", [["prekariátus", "létbizonytalanságban élő kiszolgáltatott munkavállalók"], ["reindusztrializáció", "az ipar gazdasági súlyának újbóli növelése"], ["technológiai munkanélküliség", "gépesítés és automatizáció miatti állásvesztés"], ["szerkezeti munkanélküliség", "a meglévő képzettség és a munkaerő-kereslet eltérése"]], ["c1-21-vocab"]),
                fb("grammar", "practice", "Noha a kormány teljes foglalkoztatást hirdet, _____ a reálkeresetek értéke erodálódott. (at the same time / ugyanakkor)", "ugyanakkor", "While the government proclaims full employment, at the same time the value of real earnings eroded.", ["c1-adv-economic-concession-markers"]),
                sb("grammar", "practice", ["Jóllehet", "nő", "a", "termelés,", "mindamellett", "a", "bérfeszültség", "mélyül."], ["Jóllehet", "nő", "a", "termelés,", "mindamellett", "a", "bérfeszültség", "mélyül."], "Even though production grows, nonetheless wage tension deepens.", ["c1-adv-economic-concession-markers"]),
                dc("dialogue", [
                    {"speaker": "Közgazdász", "text": "Hozott-e valódi jólétet a hazai iparosítási hullám?"},
                    {"speaker": "Munkaügyi kutató", "text": "Jóllehet nőttek a beruházások, _____ a dolgozói kiszolgáltatottság mérséklődött volna."},
                    {"speaker": "Közgazdász", "text": "Tehát az alacsony hozzáadott érték csapdájában maradtunk."}
                ], ["mégsem mondható, hogy", "mindenki gazdag lett", "örömmel kijelenthetjük"], 0, ["c1-adv-economic-concession-markers"]),
                sw("production", [{"prompt": "Write a sentence weighing industrial production against worker vulnerability using 'Jóllehet... mindamellett'.", "answer": "Jóllehet az autóipari óriásberuházások felpörgették az exportot, mindamellett a munkások alacsony bérezése és a fokozódó kizsigerelés mély társadalmi elégedetlenséget szül."}], ["c1-adv-economic-concession-markers"]),
                mc("grammar", "check", "Melyik kötőszói szerkezet fejez ki cizellált gazdasági ellentételezést és megengedést?", [
                    "Jóllehet... mindamellett / Noha... ugyanakkor",
                    "Ezért és emiatt",
                    "Sem... sem..."
                ], 0, ["c1-adv-economic-concession-markers"])
            ]
        },
        {
            "num": 2,
            "stem": "c1-21-02",
            "title": "Institutional Impersonals & Structural Working Conditions",
            "grammar_title": "Impersonal Passive Verbal Constructions Conveying Structural Labor Market Conditions",
            "grammar_skill": "c1-passive-institutional-impersonals",
            "goals": [
                "I can analyze institutional labor policies, corporate restructuring, and formal employer demands (*munkaköri leírás, munkáltatói önkény, felmondási hullám*).",
                "I can employ elevated archaic and institutional passive verbs in `-atik/-etik`, `-tatatik/-tetetik` (*megköveteltetik, elvárásként támasztatik, feladatául szabatik*).",
                "I can deconstruct bureaucratic workplace directives in elevated official register."
            ],
            "vocab": [
                {"lemma": "munkáltatói önkény", "translation": "employer arbitrariness", "pos": "expression"},
                {"lemma": "felmondási hullám", "translation": "wave of dismissals / layoffs", "pos": "expression"},
                {"lemma": "munkaszerződés", "translation": "employment contract", "pos": "noun"},
                {"lemma": "túlóráztatás", "translation": "excessive overtime imposition", "pos": "noun"},
                {"lemma": "kiszolgáltatottság", "translation": "vulnerability / defenselessness", "pos": "noun"},
                {"lemma": "munkaerő-kölcsönzés", "translation": "temporary agency work / labor leasing", "pos": "noun"},
                {"lemma": "szervezeti átvilágítás", "translation": "organizational audit", "pos": "expression"},
                {"lemma": "munkavédelmi audit", "translation": "occupational safety audit", "pos": "expression"}
            ],
            "gr_text1": "Impersonal passive constructions in `-atik/-etik` or `-tatatik/-tetetik` evoke institutional inevitability and bureaucratic power dynamics: `megköveteltetik` (it is demanded/required of), `elvárásként támasztatik` (it is posed as an expectation), `feladatául szabatik` (it is assigned as a duty).",
            "gr_text2": "Example: `A munkavállalótól feltétlen lojalitás és rugalmas túlórázás követeltetik meg, miközben a béremelés elutasíttatik a vezetőség által`.",
            "gr_table": [
                ["A dolgozóktól heti hatvan óra munka követeltetik meg a főszezonban.", "From the workers sixty hours of work per week is demanded during the peak season."],
                ["A szakszervezeti fellépés ellehetetlenítése célként tűzetik ki a menedzsment által.", "The disabling of trade union action is set as a goal by management."],
                ["A munkavédelmi előírások betartása elengedhetetlen feltételként támasztatik.", "The adherence to occupational safety regulations is posed as an indispensable condition."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mit jelent a 'munkaerő-kölcsönzés' a modern foglalkoztatásban?", [
                    "Egy olyan foglalkoztatási formát, ahol a munkavállaló egy közvetítő céggel áll szerződésben, de harmadik félnél végez munkát, csökkentve a munkáltató felelősségét.",
                    "A szomszédos irodák közötti tollak és füzetek cseréjét.",
                    "A diákok nyári könyvtári munkáját."
                ], 0, ["c1-21-vocab"]),
                fb("grammar", "controlled", "A szalagmunkástól feltétlen fegyelem és maximális rugalmasság _____ meg a multinacionális vállalatnál. (is demanded / követeltetik)", "követeltetik", "From the assembly worker unconditional discipline and maximum flexibility is demanded at the multinational company.", ["c1-passive-institutional-impersonals"]),
                match("vocabulary", "controlled", [["munkáltatói önkény", "a vezetőség korlátlan, dolgozókat hátrányosan érintő hatalma"], ["munkaerő-kölcsönzés", "közvetítőn keresztüli, rugalmas, bizonytalan munka"], ["túlóráztatás", "a törvényes munkaidőn túli rendszeres foglalkoztatás"], ["felmondási hullám", "tömeges elbocsátások gazdasági válság idején"]], ["c1-21-vocab"]),
                fb("grammar", "practice", "A bértárgyalások megkezdése határozottan _____ a vezérigazgatóság által. (is rejected / elutasíttatik)", "elutasíttatik", "The commencement of wage negotiations is resolutely rejected by the general directorate.", ["c1-passive-institutional-impersonals"]),
                sb("grammar", "practice", ["A", "maximális", "erőfeszítés", "elvárásként", "támasztatik", "minden", "dolgozóval", "szemben."], ["A", "maximális", "erőfeszítés", "elvárásként", "támasztatik", "minden", "dolgozóval", "szemben."], "Maximum effort is posed as an expectation toward every worker.", ["c1-passive-institutional-impersonals"]),
                dc("dialogue", [
                    {"speaker": "Üzemi tanácstag", "text": "Hogyan fogadta a vezetőség a béremelési követelést?"},
                    {"speaker": "Munkavédelmi képviselő", "text": "Minden kérés azonnal elutasíttatott, és fegyelmi vizsgálat _____ a szervezők ellen."},
                ], ["rendeltetett el", "dicséretet kapott", "elnézést kértek"], 0, ["c1-passive-institutional-impersonals"]),
                sw("production", [{"prompt": "Write a sentence describing institutional corporate pressure using a passive verb in '-atik/-etik'.", "answer": "A futószalagon dolgozóktól embertelen munkatempó követeltetik meg, miközben a pihenőidő minimálisra szűkíttetik a gyártási normák fenntartása érdekében."}], ["c1-passive-institutional-impersonals"]),
                mc("grammar", "check", "Melyik igealak testesíti meg az intézményi szenvedő szerkezetet a munkaügyi zsargonban?", [
                    "követeltetik / elutasíttatik",
                    "követelni fognak",
                    "követelhetnének"
                ], 0, ["c1-passive-institutional-impersonals"])
            ]
        },
        {
            "num": 3,
            "stem": "c1-21-03",
            "title": "Systemic Vulnerability & Rhetorical Causal Participles",
            "grammar_title": "Complex Causal Participial Modifiers Diagnosing Systemic Employment Vulnerability",
            "grammar_skill": "c1-rhetorical-causal-participles",
            "goals": [
                "I can analyze the mechanics of wage depression, union-busting, and sub-contracting chains (*bérletörés, szakszervezet-ellenesség, alvállalkozói lánc*).",
                "I can form causal adverbial participles in `-va/-ve` articulating multi-step socioeconomic degradation (*kiszolgáltatottságot szülve, bérletörést okozva, létbizonytalanságot teremtve*).",
                "I can diagnose structural imbalances between capital and organized labor."
            ],
            "vocab": [
                {"lemma": "bérletörés", "translation": "wage depression / suppression", "pos": "noun"},
                {"lemma": "alvállalkozói lánc", "translation": "sub-contracting chain", "pos": "expression"},
                {"lemma": "sztrájkjog kiüresítése", "translation": "hollowing out of the right to strike", "pos": "expression"},
                {"lemma": "létbizonytalanság", "translation": "existential insecurity / precarity", "pos": "noun"},
                {"lemma": "üzemi baleset", "translation": "workplace accident / occupational injury", "pos": "expression"},
                {"lemma": "érdekegyeztetés", "translation": "interest reconciliation / conciliation", "pos": "noun"},
                {"lemma": "kollektív szerződés", "translation": "collective agreement / bargaining agreement", "pos": "expression"},
                {"lemma": "szakszervezeti lefedettség", "translation": "union density / coverage", "pos": "expression"}
            ],
            "gr_text1": "Complex causal adverbial participles in `-va/-ve` articulate the downstream social consequences of corporate labor practices: `kiszolgáltatottságot szülve` (spawning vulnerability), `bérletörést okozva` (causing wage suppression), `létbizonytalanságot teremtve` (creating existential insecurity), `mély sebeket ejtve` (inflicting deep wounds).",
            "gr_text2": "Example: `A multinacionális cégek a szakszervezeti fellépést adminisztratív eszközökkel akadályozzák, tartós bérletörést okozva és mély létbizonytalanságot szülve a térség családjai számára`.",
            "gr_table": [
                ["A határozott idejű szerződések állandósultak, tartós létbizonytalanságot teremtve a fiatalok körében.", "Fixed-term contracts became permanent, creating lasting existential insecurity among youth."],
                ["Az olcsó külföldi munkaerő tömeges beáramlása megállította a bérek növekedését, bérletörést okozva a hazai fizikai dolgozóknak.", "The mass influx of cheap foreign labor stopped wage growth, causing wage suppression for domestic manual workers."],
                ["A sztrájkjog korlátozása megtörte az érdekvédelmet, védtelenné téve az alkalmazottakat.", "The restriction of the right to strike broke interest representation, rendering employees defenseless."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mit jelent a 'bérletörés' folyamata a munkaerőpiacon?", [
                    "A bérek mesterséges alacsonyan tartását olcsóbb munkaerő bevonásával vagy az érdekvédelmi jogok csorbításával.",
                    "A készpénzes kifizetések papírpénzeinek elszakadását.",
                    "A fizetésemelések automatikus havi átutalását."
                ], 0, ["c1-21-vocab"]),
                fb("grammar", "controlled", "A törvényi védelem leépítése kiszolgáltatottságot _____, évtizedekre visszavetette a munkavállalói érdekérvényesítést. (spawning / szülve)", "szülve", "The dismantling of statutory protection spawning vulnerability set back worker interest assertion for decades.", ["c1-rhetorical-causal-participles"]),
                match("vocabulary", "controlled", [["bérletörés", "a fizetések szintjének tudatos leszorítása"], ["alvállalkozói lánc", "több lépcsős megbízási rendszer a felelősség elhárítására"], ["kollektív szerződés", "a munkáltató és a szakszervezet közötti átfogó megállapodás"], ["létbizonytalanság", "a biztos megélhetés és kiszámíthatóság hiánya"]], ["c1-21-vocab"]),
                fb("grammar", "practice", "A vállalat felszámolta a cafeteria-juttatásokat, súlyos jövedelemkiesést _____ a többgyermekes családoknak. (causing / okozva)", "okozva", "The company abolished fringe benefits, causing severe income loss to families with multiple children.", ["c1-rhetorical-causal-participles"]),
                sb("grammar", "practice", ["A", "sztrájkjog", "korlátozása", "létbizonytalanságot", "teremtve", "gyengíti", "a", "dolgozókat."], ["A", "sztrájkjog", "korlátozása", "létbizonytalanságot", "teremtve", "gyengíti", "a", "dolgozókat."], "The restriction of strike rights, creating existential insecurity, weakens workers.", ["c1-rhetorical-causal-participles"]),
                dc("dialogue", [
                    {"speaker": "Szakszervezeti vezető", "text": "Miért nem emelkednek a hazai gyári bérek?"},
                    {"speaker": "Elemző", "text": "A túlóratörvény lazítása elvette a dolgozók alkupozícióját, tartós bérletörést _____."},
                ], ["eredményezve", "örömmel ünnepelve", "elfelejtve"], 0, ["c1-rhetorical-causal-participles"]),
                sw("production", [{"prompt": "Write a sentence diagnosing labor exploitation using a causal participle (-va/-ve).", "answer": "A munkáltatók a rugalmasság jelszavával szétverték a kollektív védelmet, mélységes létbizonytalanságot teremtve és bérletörést okozva a legkiszolgáltatottabb gyári munkások körében."}], ["c1-rhetorical-causal-participles"]),
                mc("grammar", "check", "Melyik igeneves szerkezet fejez ki társadalmi következményt és ok-okozati láncolatot?", [
                    "kiszolgáltatottságot szülve / bérletörést okozva",
                    "miután megebédeltek a menzán",
                    "ha holnap esni fog az eső"
                ], 0, ["c1-rhetorical-causal-participles"])
            ]
        },
        {
            "num": 4,
            "stem": "c1-21-04",
            "title": "Wage Divergence, Inflation Erosion & Scalar Disparity Adverbials",
            "grammar_title": "Scalar Disparity Adverbials Measuring Wage Divergence and Inflation Erosion",
            "grammar_skill": "c1-adv-scalar-wage-disparities",
            "goals": [
                "I can analyze wage divergence, purchasing power erosion, and executive-to-worker income ratios (*bérszakadék, reálbércsökkenés, bérfeszültség*).",
                "I can deploy scalar disparity adverbials (*számottevően, kirívóan, elenyésző mértékben, drasztikusan, szembeötlően*).",
                "I can critique macroeconomic wage convergence metrics versus ground-level inflation reality."
            ],
            "vocab": [
                {"lemma": "bérszakadék", "translation": "wage gap / divide", "pos": "noun"},
                {"lemma": "reálbércsökkenés", "translation": "real wage decline", "pos": "noun"},
                {"lemma": "bérfeszültség", "translation": "wage tension", "pos": "noun"},
                {"lemma": "vásárlóerő-paritás", "translation": "purchasing power parity", "pos": "expression"},
                {"lemma": "inflációs erózió", "translation": "inflationary erosion", "pos": "expression"},
                {"lemma": "minimálbér-emelés", "translation": "minimum wage increase", "pos": "noun"},
                {"lemma": "fizetési szakadék", "translation": "pay gap", "pos": "expression"},
                {"lemma": "megélhetési válság", "translation": "cost-of-living crisis", "pos": "expression"}
            ],
            "gr_text1": "Scalar disparity adverbials measure the severity and trajectory of wage polarization and real income decline: `számottevően` (significantly), `kirívóan` (flagrantly/conspicuously), `elenyésző mértékben` (to a negligible degree), `drasztikusan` (drastically), `szembeötlően` (strikingly).",
            "gr_text2": "Example: `Míg a felsővezetői prémiumok kirívóan növekedtek, addig a futószalagon dolgozók reálbére számottevően csökkent az inflációs erózió következtében`.",
            "gr_table": [
                ["A dolgozók vásárlóereje drasztikusan visszaesett az élelmiszer-infláció miatt.", "The purchasing power of workers dropped drastically due to food inflation."],
                ["A minimálbér emelése elenyésző mértékben tudta csak kompenzálni az áremelkedést.", "The minimum wage hike was able to compensate for price increases only to a negligible degree."],
                ["A nyugat-európai és hazai bérek közötti különbség kirívóan nagy maradt.", "The gap between Western European and domestic wages remained flagrantly large."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mit jelent az 'inflációs erózió' a bérek tekintetében?", [
                    "A pénzromlás és áremelkedés miatti folyamatos vásárlóerő-csökkenést, amely a névleges fizetésemelést is felemészti.",
                    "A bankjegyek fizikai kopását és elhasználódását.",
                    "A külföldi devizák átváltásának költségeit."
                ], 0, ["c1-21-vocab"]),
                fb("grammar", "controlled", "A gyári dolgozók reálbére _____ csökkent az elmúlt két év rekordinflációja nyomán. (drastically / drasztikusan)", "drasztikusan", "The real wage of factory workers decreased drastically in the wake of the record inflation of the past two years.", ["c1-adv-scalar-wage-disparities"]),
                match("vocabulary", "controlled", [["bérszakadék", "a legmagasabb és legalacsonyabb fizetések közötti mély különbség"], ["inflációs erózió", "a drágulás miatti életszínvonal-romlás"], ["reálbércsökkenés", "a fizetés tényleges bolti értékének elvesztése"], ["megélhetési válság", "a legalapvetőbb szükségletek kielégítésének ellehetetlenülése"]], ["c1-21-vocab"]),
                fb("grammar", "practice", "A menedzserek juttatásai _____ meghaladják az üzemi átlagbért. (flagrantly / kirívóan)", "kirívóan", "Managers' benefits flagrantly exceed the plant average wage.", ["c1-adv-scalar-wage-disparities"]),
                sb("grammar", "practice", ["A", "fizetések", "vásárlóereje", "drasztikusan", "apad", "a", "válságban."], ["A", "fizetések", "vásárlóereje", "drasztikusan", "apad", "a", "válságban."], "The purchasing power of wages dwindles drastically in the crisis.", ["c1-adv-scalar-wage-disparities"]),
                dc("dialogue", [
                    {"speaker": "Gazdasági újságíró", "text": "Hogyan alakult a bérfelzárkózás Ausztriához képest?"},
                    {"speaker": "Közgazdász", "text": "A magyar bérszínvonal sajnálatos módon csak _____ mértékben közeledett a bécsihez."},
                ], ["elenyésző", "hatalmas", "végtelen"], 0, ["c1-adv-scalar-wage-disparities"]),
                sw("production", [{"prompt": "Write a sentence analyzing wage polarization using a scalar disparity adverb.", "answer": "Az elmúlt évek brutális élelmiszer-inflációja következtében a kétkezi munkások reálkeresete drasztikusan megcsappant, tovább tágítva a kirívóan mély társadalmi ollót."}], ["c1-adv-scalar-wage-disparities"]),
                mc("grammar", "check", "Melyik határozószó fejez ki kirívó, extrém mértékű vagy nagyságrendi béraránytalanságot?", [
                    "kirívóan / drasztikusan",
                    "együttműködve",
                    "időben érkezve"
                ], 0, ["c1-adv-scalar-wage-disparities"])
            ]
        },
        {
            "num": 5,
            "stem": "c1-21-05",
            "title": "Nagy Lajos: Kiskunhalom & Deontic Labor Rights",
            "grammar_title": "Deontic Modal Expressions Articulating Collective Bargaining and Statutory Worker Rights",
            "grammar_skill": "c1-modal-deontic-labor-rights",
            "goals": [
                "I can analyze Nagy Lajos's merciless 1934 sociography 'Kiskunhalom' and the exploitation of day laborers and agrarian proletariat.",
                "I can employ deontic modal expressions formulating collective bargaining and fundamental labor rights (*köteles biztosítani, elidegeníthetetlen jogát képezi, kógens szabályként írja elő*).",
                "I can synthesize the historical lineage of Hungarian working-class literature from the interwar period to modern industrial realities."
            ],
            "vocab": [
                {"lemma": "napszámos sors", "translation": "day laborer's fate / lot", "pos": "expression"},
                {"lemma": "szociográfiai látlelet", "translation": "sociographical diagnostic / clinical diagnosis", "pos": "expression"},
                {"lemma": "kógens szabály", "translation": "mandatory / cogent rule (cannot be derogated)", "pos": "expression"},
                {"lemma": "elidegeníthetetlen jog", "translation": "inalienable right", "pos": "expression"},
                {"lemma": "agrárproletariátus", "translation": "agrarian proletariat", "pos": "noun"},
                {"lemma": "kizsákmányolás", "translation": "exploitation", "pos": "noun"},
                {"lemma": "kollektív alku", "translation": "collective bargaining", "pos": "noun"},
                {"lemma": "méltányos bér", "translation": "fair / living wage", "pos": "expression"}
            ],
            "gr_text1": "Deontic modal expressions define mandatory legal rights and non-negotiable protections for labor: `köteles biztosítani` (is obligated to ensure), `elidegeníthetetlen jogát képezi` (forms their inalienable right), `kógens szabályként írja elő` (stipulates as a mandatory rule), `törvényi garanciát követel` (demands statutory guarantee).",
            "gr_text2": "Example: `A munkáltató köteles biztosítani az egészséget nem veszélyeztető munkafeltételeket, és a tisztességes, emberhez méltó megélhetést biztosító bér minden dolgozó elidegeníthetetlen jogát képezi`.",
            "gr_table": [
                ["A jogállam köteles biztosítani a szabad szakszervezetalapítás és a sztrájk jogát.", "The constitutional state is obligated to ensure the right to free union formation and strike."],
                ["A méltányos munkaidő betartása kógens szabályként írja elő a pihenőnapok kötelező kiadását.", "The observance of fair working time stipulates as a mandatory rule the compulsory granting of rest days."],
                ["A munkabiztonság nem alku tárgya, hanem alapvető emberi jogot képez.", "Work safety is not a subject of negotiation, but forms a fundamental human right."]
            ],
            "classic_story": {
                "slug": "c1-21-nagylajos",
                "author": "Nagy Lajos",
                "work": "Kiskunhalom (1934)",
                "title": "Nagy Lajos: Kiskunhalom és a cselédsors valósága",
                "summary": "Nagy Lajos's groundbreaking 1934 sociographical report dissecting the rigid class hierarchy, poverty, and brutal exploitation of agrarian day laborers in the market town of Kiskunhalom.",
                "characters": ["Nagy Lajos"],
                "paragraphs": [
                    {"type": "narration", "text": "Amikor Nagy Lajos 1934-ben közzétette 'Kiskunhalom' című szociográfiáját, a magyar irodalom és társadalomkritika egyik legkegyetlenebb, illúziómentes tükrét tartotta a Horthy-korszak elé. Kiskunhalom a magyar vidék sűrítménye volt: egy gazdag mezőváros, amelynek csillogó főterétől alig néhány utcányira a mélységes nyomor, a kiszolgáltatottság és a megaláztatás világa húzódott meg. Nagy Lajos nem szépített, nem lírizált; mérnöki pontossággal és statisztikai ridegséggel leplezte le a falusi és kisvárosi társadalom kasztrendszerét."},
                    {"type": "narration", "text": "A könyv lapjain megelevenedett a napszámosok, cselédek és kubikosok tragédiája: azoké az embereké, akik hajnaltól alkonyatig görnyedtek a gazdák és a nagybirtok földjein pár garasért, miközben télen a fűtetlen putrijaikban éheztek a gyermekeikkel. A munkabér nem a megélhetést szolgálta, hanem épp csak arra volt elég, hogy a munkás másnap újra talpra tudjon állni a földeken. Mindenféle érdekvédelmi jog vagy szakszervezeti összefogás lázadásnak minősült, amelyet a csendőrség kíméletlenül megtorolt."},
                    {"type": "narration", "text": "Nagy Lajos rámutatott: a munkaadó és munkavállaló közötti szerződés nem egyenrangú felek szabad megállapodása volt, hanem tiszta és brutális zsarolás. 'Aki nem dolgozik ennyiért, az éhen dögölhet' – ez volt a törvény. A munkavállalónak semmiféle joga nem volt, a munkaadót viszont semmilyen kógens szabály nem kötötte a méltányos bánásmódra."},
                    {"type": "narration", "text": "A 'Kiskunhalom' tanulsága ma is eleven figyelmeztetés. A modern kori futószalagok, az akkumulátorgyárak és a platformgazdaság világában újra fel kell tennünk a kérdést: vajon meghaladtuk-e a kiszolgáltatottság ősi reflexeit, vagy csupán digitális díszletek közé költöztettük a napszámos sorsot? A méltányos munka és az emberi méltóság feltétlen tisztelete a társadalom legfontosabb kógens kötelezettsége marad."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Miért tekintik Nagy Lajos 'Kiskunhalom' című művét a magyar szociográfia mérföldkövének?", [
                    "Mert rideg, dokumentarista pontossággal és kompromisszummentes őszinteséggel tárta fel a napszámosok és cselédek brutális kizsákmányolását.",
                    "Mert vidám anekdotákat mesélt a kiskunhalmi borászatról.",
                    "Mert ez volt az első színes fényképekkel illusztrált útikönyv a városról."
                ], 0, ["c1-21-vocab"]),
                fb("grammar", "controlled", "A demokratikus állam köteles _____ a munkavállalók sztrájkhoz és kollektív tárgyaláshoz való jogát. (ensure / biztosítani)", "biztosítani", "The democratic state is obligated to ensure workers' right to strike and collective bargaining.", ["c1-modal-deontic-labor-rights"]),
                match("vocabulary", "controlled", [["napszámos sors", "napról napra élő, bizonytalan és kiszolgáltatott fizikai munka"], ["kógens szabály", "eltérést nem engedő, kötelező érvényű törvény"], ["elidegeníthetetlen jog", "az embertől elvehetetlen alapvető szabadságjog"], ["méltányos bér", "az emberhez méltó életet garantáló jövedelem"]], ["c1-21-vocab"]),
                mc("reading", "practice", "Hogyan jellemezte Nagy Lajos a munkáltatók és munkások közötti viszonyt Kiskunhalmon?", [
                    "Nem egyenlő felek szerződéseként, hanem a nélkülözésre és kiszolgáltatottságra épülő nyers zsarolásként.",
                    "Harmonikus, családi együttműködésként a földeken.",
                    "A városi önkormányzat által gondosan felügyelt demokratikus partnerségként."
                ], 0, None),
                sb("grammar", "practice", ["A", "méltányos", "megélhetés", "minden", "dolgozó", "elidegeníthetetlen", "joga."], ["A", "méltányos", "megélhetés", "minden", "dolgozó", "elidegeníthetetlen", "joga."], "A fair living is every worker's inalienable right.", ["c1-modal-deontic-labor-rights"]),
                sw("production", [{"prompt": "Write a critical reflection on Nagy Lajos's sociography using a deontic modal expression.", "answer": "Nagy Lajos Kiskunhalom című műve ma is érvényes lecke arra, hogy a munkavállalói jogok védelme nem adomány a tőke részéről, hanem a társadalomnak kógens szabályként kell előírnia a méltányos munkakörülmények garantálását."}], ["c1-modal-deontic-labor-rights"]),
                mc("grammar", "check", "Melyik kifejezés testesíti meg a kötelező erejű munkajogi imperatívuszt?", [
                    "köteles biztosítani / kógens szabályként írja elő",
                    "esetleg megfontolhatja",
                    "talán eljöhet holnap"
                ], 0, ["c1-modal-deontic-labor-rights"])
            ]
        }
    ]

    for l in core_lessons:
        emit_instructional_lesson(21, "core", l, core_title, core_intro if l["num"] == 1 else None)

    # Core Consolidation Lesson
    emit_consolidation_lesson(
        21,
        "core",
        "c1-21-consolidation",
        core_title,
        [
            "I can master C1 academic vocabulary of labor precarity, structural unemployment, and exploitation.",
            "I can deploy economic concessives, institutional impersonals, and causal participial chains.",
            "I can critically evaluate wage disparity metrics, Nagy Lajos's 'Kiskunhalom', and statutory collective rights."
        ],
        [
            mc("grammar", "recognize", "Melyik mondat fejez ki formális gazdasági megengedést és ellentételezést?", [
                "Jóllehet a gyárak termelése felpörgött, mindamellett a munkások reálbére érzékelhetően csökkent.",
                "A munkások bementek a gyárkapun és felvették a védőruhát.",
                "Mivel szép volt a reggel, mindenki vidáman kezdte a műszakot."
            ], 0, ["c1-adv-economic-concession-markers"]),
            mc("grammar", "recognize", "Melyik szerkezet képvisel formális intézményi szenvedő alakot?", [
                "a dolgozóktól feltétlen engedelmesség követeltetik meg",
                "a munkás megkérdezi a főnökét a fizetésről",
                "amikor a gyár dudája megszólal este hatkor"
            ], 0, ["c1-passive-institutional-impersonals"]),
            match("vocabulary", "recognize", [["prekariátus", "létbizonytalanságban élő kiszolgáltatott dolgozói réteg"], ["bérletörés", "a fizetések szintjének mesterséges leszorítása"], ["kógens szabály", "eltérést nem engedő kötelező munkajogi előírás"], ["inflációs erózió", "a drágulás miatti vásárlóerő-vesztés"], ["napszámos sors", "napról napra küzdő cselédek és idénymunkások helyzete"]], ["c1-21-vocab"]),
            fb("vocabulary", "recall", "A modern gazdaság bizonytalan munkaszerződésekkel sújtott rétegét _____ nevezzük. (precariat / prekariátusnak)", "prekariátusnak", "The stratum of modern economy stricken by precarious work contracts is called precariat.", ["c1-21-vocab"]),
            fb("vocabulary", "recall", "A tisztességes fizetés garantálása a munkajogban eltérést nem engedő, _____ kell legyen. (mandatory rule / kógens szabály)", "kógens szabály", "Guaranteeing a fair wage must be a non-derogable, mandatory rule in labor law.", ["c1-21-vocab"]),
            fb("grammar", "recall", "A vezetőség az alacsony bérekkel létbizonytalanságot _____, megtörte az ellenállást. (creating / teremtve)", "teremtve", "Management, creating existential insecurity with low wages, broke resistance.", ["c1-rhetorical-causal-participles"]),
            fb("grammar", "context", "A dolgozók vásárlóereje _____ megcsappant a legutóbbi megélhetési krízisben. (drastically / drasztikusan)", "drasztikusan", "The purchasing power of workers dwindled drastically in the latest cost-of-living crisis.", ["c1-adv-scalar-wage-disparities"]),
            fb("grammar", "context", "Az állam köteles _____ a munkavállalói érdekképviseletek függetlenségét. (guarantee / garantálni)", "garantálni", "The state is obligated to guarantee the independence of employee interest representations.", ["c1-modal-deontic-labor-rights"]),
            mc("grammar", "context", "Mi a célja a szenvedő igék használatának a munkaügyi előírások szövegezésekor?", [
                "A személytelen, rendszerszintű intézményi kényszer és a vállalati hatalmi hierarchia kifejezése.",
                "Annak bizonyítása, hogy a menedzsment nem tud magyarul.",
                "A mondatok hosszának felesleges megkettőzése."
            ], 0, ["c1-passive-institutional-impersonals"]),
            sb("grammar", "produce", ["A", "munka", "méltósága", "minden", "demokrácia", "legfőbb", "alapköve."], ["A", "munka", "méltósága", "minden", "demokrácia", "legfőbb", "alapköve."], "The dignity of labor is the foremost cornerstone of every democracy.", ["c1-modal-deontic-labor-rights"]),
            sw("production", [{"prompt": "Write a diagnostic sentence about the modern precariat using an economic concessive structure.", "answer": "Jóllehet a gazdasági mutatók teljes foglalkoztatottságot jeleznek, mindamellett a prekariátus körében tapasztalható alacsony bérek és kiszolgáltatottság súlyos társadalmi feszültséget generálnak."}], ["c1-adv-economic-concession-markers"]),
            sw("production", [{"prompt": "Formulate a concluding thought on labor dignity and collective bargaining rights.", "answer": "A munkavállalók elidegeníthetetlen joga a tisztességes, inflációt követő bérezés és a kollektív alku szabadsága, amelyet a jogállamnak kógens garanciákkal kötelessége védeni."}], ["c1-modal-deontic-labor-rights"])
        ]
    )

    # ----------------------------------------------------
    # TRACK 2: DISCOURSE (c1-munkaeropiac)
    # ----------------------------------------------------
    slug = "munkaeropiac"
    disc_intro = [
        "Hungary's labor landscape is increasingly bifurcated: while high-tech industrial parks rely heavily on imported third-country guest workers to suppress wage pressures, platform capitalism erodes social protections, and tens of thousands of skilled Hungarians commute daily to Austria.",
        "In this unit, you will master the elevated discourse of labor market dualism, corporate antithesis, temporal industrial succession, and collective policy evaluation in contemporary Hungarian economic life."
    ]

    disc_lessons = [
        {
            "num": 1,
            "stem": f"c1-{slug}-01",
            "title": "Guest Workers, Third-Country Labor & Polarization Antithesis",
            "grammar_title": "Antithetical Discourse Markers Contrasting Corporate Flexibility with Worker Vulnerability",
            "grammar_skill": "c1-discourse-polarization-antithesis",
            "goals": [
                "I can analyze the importation of Asian guest workers in Hungarian industrial hubs (*harmadik országbeli munkavállaló, vendégmunkás-kvóta, munkásszállók*).",
                "I can deploy antithetical discourse markers contrasting corporate interests and social friction (*míg egyfelől... addig másfelől, egyrészről... ezzel szemben*).",
                "I can debate the demographic and wage consequences of state-subsidized labor importation."
            ],
            "vocab": [
                {"lemma": "vendégmunkás", "translation": "guest worker", "pos": "noun"},
                {"lemma": "harmadik országbeli állampolgár", "translation": "third-country national", "pos": "expression"},
                {"lemma": "munkásszálló", "translation": "workers' hostel / dormitory", "pos": "noun"},
                {"lemma": "bérverseny visszafogása", "translation": "curbing / dampening of wage competition", "pos": "expression"},
                {"lemma": "munkaerő-hiány", "translation": "labor shortage", "pos": "noun"},
                {"lemma": "társadalmi feszültség", "translation": "social tension", "pos": "expression"},
                {"lemma": "kiszorítási hatás", "translation": "crowding-out effect", "pos": "expression"},
                {"lemma": "munkaerő-toborzás", "translation": "labor recruitment", "pos": "noun"}
            ],
            "gr_text1": "Antithetical markers contrast contradictory realities within the dual labor market: `míg egyfelől... addig másfelől` (while on the one hand... yet on the other hand), `egyrészről... ezzel szemben` (on the one part... in contrast with this), `egyfelől... ugyanakkor` (on one hand... simultaneously).",
            "gr_text2": "Example: `Míg egyfelől a multinacionális vállalatok az olcsó vendégmunkásokkal oldják meg a munkaerőhiányt, addig másfelől ez a gyakorlat megakadályozza a hazai bérek felzárkózását és feszültséget kelt a helyi lakosságban`.",
            "gr_table": [
                ["Míg egyfelől a gyárak üdvözlik az ázsiai dolgozókat, addig másfelől a helyi közösségek elszigeteltségtől tartanak.", "While on the one hand factories welcome Asian workers, on the other hand local communities fear isolation."],
                ["Egyrészről az ipar folyamatos termelést követel, ezzel szemben a hazai bérek stagnálnak.", "On the one hand industry demands continuous production, in contrast domestic wages stagnate."],
                ["Egyfelől a toborzás felgyorsult, ugyanakkor a kulturális integrációra semmilyen forrás nem jut.", "On the one hand recruitment accelerated, simultaneously no resources are allocated to cultural integration."]
            ],
            "world_story_seg": {
                "seg_slug": "vendegmunkas",
                "title": "Távoli vidékekről a magyar gyárakba: vendégmunkások a futószalag mellett",
                "summary": "Exploring the rapid transformation of provincial industrial towns like Tiszaújváros, Győr, and Iváncsa, where thousands of Filipino, Kazakh, and Vietnamese guest workers operate assembly lines.",
                "paragraphs": [
                    {"type": "narration", "text": "Tiszaújváros és Iváncsa határában az utóbbi években szürke, konténerszerű épületekből álló egész városrészek nőttek ki a földből: ezek a külföldi munkavállalókat befogadó munkásszállók. A kora reggeli és esti műszakváltáskor fülöp-szigeteki, vietnámi és kirgiz férfiak és nők százai lépnek ki a kapukon, csendben, rendezett sorokban várakozva a gyári buszokra. Azokért a gépekért felelnek, amelyeket a kivándorlás és az alacsony fizetések miatt a hazai munkavállalók már nem akartak működtetni."},
                    {"type": "narration", "text": "Ez a folyamat a magyar gazdaságpolitika egyik legélesebb belső paradoxona. Miközben a politikai retorika hivatalosan a munkahelyek megvédéséről és a nemzeti szuverenitásról beszél, a valóságban a gazdaságpolitika a harmadik országbeli vendégmunkások tömeges importjával fojtja el a hazai bérnyomást. Míg egyfelől a gyárak zavartalanul termelnek, addig másfelől a hazai dolgozók alkupozíciója gyengül, és mély társadalmi szakadék keletkezik a konténerfalvak zárt világa és a helyi lakosság között."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Mi a fő gazdasági indoka a vendégmunkások magyarországi alkalmazásának a multinacionális üzemekben?", [
                    "A krónikus munkaerőhiány gyors kezelése és a hazai gyári bérek emelkedésének fékezése olcsó, kötött munkaerővel.",
                    "A magyar nyelv ázsiai népszerűsítése a gyári műszakok során.",
                    "A turisztikai vendéglátás szezonális fellendítése télen."
                ], 0, ["c1-munkaeropiac-vocab"]),
                fb("grammar", "controlled", "Míg egyfelől a gyárak olcsó munkaerőhöz jutnak, _____ másfelől a hazai bérek növekedése megtorpan. (meanwhile / addig)", "addig", "While on the one hand factories get cheap labor, meanwhile on the other hand domestic wage growth halts.", ["c1-discourse-polarization-antithesis"]),
                match("vocabulary", "controlled", [["vendégmunkás", "meghatározott időre dolgozni érkező külföldi állampolgár"], ["munkásszálló", "a gyári alkalmazottak számára létesített zárt szálláshely"], ["bérverseny visszafogása", "a fizetések emelkedésének megakadályozása olcsó munkaerővel"], ["kiszorítási hatás", "a hazai munkavállalók háttérbe szorulása a munkaerőpiacon"]], ["c1-munkaeropiac-vocab"]),
                fb("grammar", "practice", "Egyrészről a termelés pörög, ezzel _____ a helyi dolgozók elvándorlása folytatódik. (in contrast / szemben)", "szemben", "On the one hand production is booming, in contrast with this the out-migration of local workers continues.", ["c1-discourse-polarization-antithesis"]),
                sb("grammar", "practice", ["Míg", "egyfelől", "nő", "a", "profit,", "addig", "másfelől", "apad", "a", "bér."], ["Míg", "egyfelől", "nő", "a", "profit,", "addig", "másfelől", "apad", "a", "bér."], "While on the one hand profit grows, on the other hand wages dwindle.", ["c1-discourse-polarization-antithesis"]),
                dc("dialogue", [
                    {"speaker": "Munkaerőpiaci elemző", "text": "Miért támogatják a gyárak a vendégmunkás-kvóták emelését?"},
                    {"speaker": "Szakszervezeti aktivista", "text": "Míg egyfelől a gyárosok rugalmasságot nyernek, addig másfelől ez a hazai fizetések _____ jár."},
                ], ["letörésével", "megduplázásával", "ünneplésével"], 0, ["c1-discourse-polarization-antithesis"]),
                sw("production", [{"prompt": "Write an antithetical sentence on guest worker employment using 'Míg egyfelől... addig másfelől'.", "answer": "Míg egyfelől a harmadik országbeli vendégmunkások alkalmazása megoldást nyújt a gyárak azonnali munkaerőhiányára, addig másfelől megakadályozza a magyar dolgozók bérének valódi európai felzárkózását."}], ["c1-discourse-polarization-antithesis"]),
                mc("grammar", "check", "Melyik szerkezet fejez ki éles ellentétezést és megosztottságot a munkaerőpiaci érvelésben?", [
                    "Míg egyfelől... addig másfelől",
                    "Ezért tehát azonnal",
                    "Valamint és továbbá"
                ], 0, ["c1-discourse-polarization-antithesis"])
            ]
        },
        {
            "num": 2,
            "stem": f"c1-{slug}-02",
            "title": "Industrial Assembly Lines & Temporal Succession Chains",
            "grammar_title": "Temporal Succession Adverbials Mapping Sequential Shifts in Industrial Employment Structures",
            "grammar_skill": "c1-adv-temporal-succession-chains",
            "goals": [
                "I can analyze factory assembly lines, wage suppression mechanisms, and work intensity (*futószalag-munka, normaemelés, háromműszakos munkarend*).",
                "I can deploy temporal succession adverbials mapping stages of industrial transformation (*kezdetben, ezt követően, végül, fokozatosan kibontakozva*).",
                "I can critique the physical and mental toll of high-intensity manufacturing on the workforce."
            ],
            "vocab": [
                {"lemma": "futószalag-munka", "translation": "assembly-line work", "pos": "expression"},
                {"lemma": "normaemelés", "translation": "raising of production quotas / norms", "pos": "noun"},
                {"lemma": "háromműszakos munkarend", "translation": "three-shift work schedule", "pos": "expression"},
                {"lemma": "kimerültség", "translation": "exhaustion / burnout", "pos": "noun"},
                {"lemma": "monotonitás", "translation": "monotony", "pos": "noun"},
                {"lemma": "bérstagnálás", "translation": "wage stagnation", "pos": "noun"},
                {"lemma": "fluktuáció", "translation": "turnover / attrition of staff", "pos": "noun"},
                {"lemma": "teljesítménybér", "translation": "piece rate / performance wage", "pos": "noun"}
            ],
            "gr_text1": "Temporal succession chains map chronological and evolutionary steps in workplace regimes: `kezdetben` (initially), `ezt követően` (subsequently / following this), `fokozatosan kibontakozva` (gradually unfolding), `végezetül` (finally / in the end).",
            "gr_text2": "Example: `Kezdetben a beruházók versenyképes fizetéseket ígértek, ezt követően azonban fokozatosan felemelték a gyártási normákat, végezetül pedig a túlórák kifizetésének visszatartásával bérstagnálást kényszerítettek a dolgozókra`.",
            "gr_table": [
                ["Kezdetben a munkások bíztak a gyárban, ezt követően azonban a folyamatos normaemelés elkeseredést szült.", "Initially the workers trusted the factory, subsequently however continuous quota-raising bred bitterness."],
                ["A reformok fokozatosan kibontakozva átalakították az üzem életét, végezetül elűzve a tapasztalt dolgozókat.", "The reforms gradually unfolding transformed the plant's life, in the end driving away experienced workers."],
                ["Ezt követően a vállalat a bérköltségek lefaragására törekedett, felgyorsítva a fluktuációt.", "Subsequently the company strove to cut wage costs, accelerating employee turnover."]
            ],
            "world_story_seg": {
                "seg_slug": "akkugyar-munka",
                "title": "A futószalag fogságában: az akkumulátorgyárak embert próbáló műszakai",
                "summary": "Investigating working conditions on the assembly floors of battery megafactories: twelve-hour rotating shifts, hazardous chemicals, relentless speed-ups, and structural burnout.",
                "paragraphs": [
                    {"type": "narration", "text": "Amikor a gödi vagy komáromi akkumulátorgyárak tiszta terének zsilipkapui becsukódnak a munkások mögött, egy steril, de kíméletlen világ veszi kezdetét. Fehér védőruhákban, maszkokban és gumikesztyűkben dolgoznak tizenkét órás forgó műszakokban a forró vegyi gőzök és a precíziós prések között. A modern akkumulátorgyártásban a ritmust nem az ember, hanem a számítógép által vezérelt szalag diktálja: másodpercek alatt kell elvégezni minden mozdulatot, a pihenőidőt pedig percre pontosan mérik az érzékelők."},
                    {"type": "narration", "text": "A munkaerő-utánpótlás története klasszikus egymásutániságot mutat. Kezdetben a külföldi tulajdonosok vonzó kezdőbéreket ígértek a környék lakóinak. Ezt követően azonban a termelési kvóták folyamatos emelésével és a szakszervezeti kezdeményezések elfojtásával a munkakörülmények drasztikusan romlottak. Végül, amikor a hazai dolgozók a kimerültség és az egészségügyi kockázatok miatt tömegesen mondtak fel, a menedzsment közvetítő cégeken keresztül, harmadik országbeli munkaerővel töltötte fel a sorokat, konzerválva az alacsony bérszínvonalat."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Mit jelent a 'normaemelés' fogalma az ipari gyártásban?", [
                    "Az egységnyi idő alatt elvárt termelési darabszám mesterséges növelését, ami a munka intenzitásának fokozásához vezet.",
                    "A munkások számára biztosított ebédszünet meghosszabbítását.",
                    "A karácsonyi prémiumok összegének hivatalos növelését."
                ], 0, ["c1-munkaeropiac-vocab"]),
                fb("grammar", "controlled", "Kezdetben stabil béreket kínáltak, ezt _____ azonban a gyártási elvárásokat embertelenné tették. (subsequently / követően)", "követően", "Initially they offered stable wages, subsequently however they made production expectations inhumane.", ["c1-adv-temporal-succession-chains"]),
                match("vocabulary", "controlled", [["futószalag-munka", "gépi tempóhoz kötött, ismétlődő ipari tevékenység"], ["normaemelés", "a kötelezően előírt teljesítmény növelése azonos bérért"], ["háromműszakos munkarend", "a nap 24 óráját lefedő, váltakozó beosztás"], ["fluktuáció", "a dolgozók gyakori cserélődése a rossz körülmények miatt"]], ["c1-munkaeropiac-vocab"]),
                fb("grammar", "practice", "A munkakörülmények fokozatosan kibontakozva romlottak, _____ pedig tömeges felmondáshoz vezettek. (in the end / végül)", "végül", "Working conditions gradually unfolding deteriorated, and in the end led to mass resignations.", ["c1-adv-temporal-succession-chains"]),
                sb("grammar", "practice", ["Kezdetben", "ígértek,", "ezt", "követően", "azonban", "visszavonták", "a", "bónuszt."], ["Kezdetben", "ígértek,", "ezt", "követően", "azonban", "visszavonták", "a", "bónuszt."], "Initially they promised, subsequently however they revoked the bonus.", ["c1-adv-temporal-succession-chains"]),
                dc("dialogue", [
                    {"speaker": "Gyári operátor", "text": "Hogyan vált elviselhetetlenné a munka a szalagon?"},
                    {"speaker": "Munkatárs", "text": "Kezdetben még bírtuk a tempót, ezt követően azonban _____ emelték a darabszámot."},
                ], ["tovább", "kevesebbre", "ingyen"], 0, ["c1-adv-temporal-succession-chains"]),
                sw("production", [{"prompt": "Write a sentence describing the deterioration of factory work using temporal succession markers.", "answer": "Kezdetben a munkáltató magas bónuszokat helyezett kilátásba, ezt követően azonban az elérhetetlen normaemeléssel megfosztotta a dolgozókat a prémiumtól, végül pedig a fluktuáció robbanásszerű növekedését idézte elő."}], ["c1-adv-temporal-succession-chains"]),
                mc("grammar", "check", "Melyik kifejezéssor fejez ki kronologikus egymásra épülést egy folyamat leírásában?", [
                    "Kezdetben... ezt követően... végül",
                    "Talán... néha... aligha",
                    "Ott... amott... bent"
                ], 0, ["c1-adv-temporal-succession-chains"])
            ]
        },
        {
            "num": 3,
            "stem": f"c1-{slug}-03",
            "title": "Platform Capitalism, Gig Economy & Teleological Labor Policy",
            "grammar_title": "Teleological Postpositional Structures Formulating Statutory Employment Policy Targets",
            "grammar_skill": "c1-modal-teleological-labor-policy",
            "goals": [
                "I can analyze platform capitalism, food delivery couriers, and the abolition of the KATA tax regime (*platformkapitalizmus, ételfutárok, KATA-átalakítás, látszatvállalkozás*).",
                "I can formulate teleological postpositional phrases targeting employment security (*a munkavállalói védelem megerősítése céljából, a bérbiztonság szavatolása végett*).",
                "I can evaluate the legal reclassification of gig workers from self-employed contractors to salaried employees."
            ],
            "vocab": [
                {"lemma": "platformkapitalizmus", "translation": "platform capitalism", "pos": "noun"},
                {"lemma": "kényszervállalkozás", "translation": "forced / bogus self-employment", "pos": "expression"},
                {"lemma": "futár", "translation": "courier / delivery rider", "pos": "noun"},
                {"lemma": "algoritmikus irányítás", "translation": "algorithmic management / control", "pos": "expression"},
                {"lemma": "KATA-adózás", "translation": "KATA itemized small-tax regime", "pos": "noun"},
                {"lemma": "társadalombiztosítási hiány", "translation": "social security contribution shortfall", "pos": "expression"},
                {"lemma": "rugalmas foglalkoztatás", "translation": "flexible employment", "pos": "expression"},
                {"lemma": "munkajogi átsorolás", "translation": "labor law reclassification", "pos": "expression"}
            ],
            "gr_text1": "Teleological postpositional structures formulate targeted public policy goals in employment regulation: `céljából` (for the purpose of), `végett` (with a view to / in order to), `érdekében` (in the interest of), `előmozdítására` (for the promotion of).",
            "gr_text2": "Example: `A gig-economy munkásainak védelme céljából az Európai Unió irányelvet fogadott el az algoritmusok átláthatóságának szavatolása és a kényszervállalkozók átsorolása végett`.",
            "gr_table": [
                ["A dolgozók biztonságának megóvása céljából szigorúbb ellenőrzésekre van szükség.", "For the purpose of preserving workers' safety, stricter inspections are needed."],
                ["A társadalombiztosítási jogviszony megteremtése végett kötelezővé tették a bejelentést.", "With a view to creating social security status, formal registration was made mandatory."],
                ["A valós munkaviszony elismerése érdekében a bíróságok újrasorolják a futárokat.", "In the interest of recognizing genuine employment, courts are reclassifying couriers."]
            ],
            "world_story_seg": {
                "seg_slug": "gig-economy",
                "title": "A két keréken száguldó prekariátus: ételfutárok és a KATA végnapjai",
                "summary": "Exploring the lives of Budapest delivery riders after the sudden abolition of the KATA small-business tax regime: algorithmic control, accident risks, and the fight for worker classification.",
                "paragraphs": [
                    {"type": "narration", "text": "Budapest belvárosában nincs olyan utcasarok, ahol ne tűnne fel egy türkizkék vagy rózsaszín hőtáskás kerékpáros vagy robogós ételfutár. Esőben, hóban, fagyban és tikkasztó kánikulában száguldanak a forgalomban, hogy a megrendelt hamburgert húsz percen belül az irodákba vagy lakásokba szállítsák. Nem emberi főnök, hanem egy mobilalkalmazás láthatatlan algoritmusa osztja ki a címeket, pontozza a sebességet és szab ki büntetéseket az elkésett percek miatt. Ez a platformkapitalizmus színtiszta valósága: a maximális rugalmasság ígérete, amely a valóságban a jogfosztottság legmodernebb formája."},
                    {"type": "narration", "text": "Amikor 2022-ben a parlament egyetlen nap alatt, társadalmi egyeztetés nélkül szétverte a kisadózók KATA-rendszerét, futárok és kisvállalkozók tízezrei vonultak az utcára, lezárva a Margit hidat. A jogalkotó ugyan a bújtatott munkaviszonyok felszámolására hivatkozott, a valóságban azonban az intézkedés a legkiszolgáltatottabb dolgozók adóterheit többszörözte meg, miközben valódi munkavállalói védelmet nem teremtett. Az európai uniós irányelvek szellemében elkerülhetetlenné vált az átsorolás: a munkavállalói státusz szavatolása végett a platformcégeket kötelezni kell a társadalombiztosítás és a táppénz megfizetésére."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Mi a lényege a platformkapitalizmusban tapasztalható 'algoritmikus irányításnak'?", [
                    "A munkavállalók feladatainak, teljesítményének és bérezésének automatizált, algoritmusok általi felügyelete, emberi főnök nélkül.",
                    "A számítógépes játékok tesztelésére felvett diákok munkája.",
                    "A cégvezetés által szervezett évi egyszeri számítástechnikai tanfolyam."
                ], 0, ["c1-munkaeropiac-vocab"]),
                fb("grammar", "controlled", "A futárok baleseti kockázatának csökkentése _____ kötelező biztosítást kell előírni a cégeknek. (for the purpose of / céljából)", "céljából", "For the purpose of reducing couriers' accident risk mandatory insurance must be prescribed for companies.", ["c1-modal-teleological-labor-policy"]),
                match("vocabulary", "controlled", [["platformkapitalizmus", "digitális közvetítőkre épülő, jogilag laza gazdasági modell"], ["algoritmikus irányítás", "mesterséges intelligencia általi munkairányítás"], ["kényszervállalkozás", "alkalmazotti helyett vállalkozói státuszba kényszerített munka"], ["munkajogi átsorolás", "a futárok törvényes munkavállalóként való elismerése"]], ["c1-munkaeropiac-vocab"]),
                fb("grammar", "practice", "A tisztes nyugdíjjogosultság biztosítása _____ a platformokat bejelentési kötelezettség terheli. (with a view to / végett)", "végett", "With a view to ensuring fair pension entitlement, platforms bear a registration obligation.", ["c1-modal-teleological-labor-policy"]),
                sb("grammar", "practice", ["A", "munkabiztonság", "megóvása", "céljából", "új", "törvényi", "kereteket", "hoznak."], ["A", "munkabiztonság", "megóvása", "céljából", "új", "törvényi", "kereteket", "hoznak."], "For the purpose of preserving work safety, they bring new legal frameworks.", ["c1-modal-teleological-labor-policy"]),
                dc("dialogue", [
                    {"speaker": "Kerékpáros futár", "text": "Miért tüntettünk a Margit hídon a KATA ellen?"},
                    {"speaker": "Szakszervezeti jogász", "text": "A megélhetési biztonság védelme _____ vonultatok ki a hídra."},
                ], ["érdekében", "kárára", "helyett"], 0, ["c1-modal-teleological-labor-policy"]),
                sw("production", [{"prompt": "Write a sentence formulating an employment policy goal using 'céljából' or 'végett'.", "answer": "A bújtatott munkaviszonyok visszaszorítása és a dolgozói társadalombiztosítás szavatolása céljából a jogalkotónak kötelezővé kell tennie a platformcégek munkavállalóinak azonnali munkajogi átsorolását."}], ["c1-modal-teleological-labor-policy"]),
                mc("grammar", "check", "Melyik névutó fejez ki tudatos, szakpolitikai célirányultságot a jogalkotásban?", [
                    "céljából / végett / érdekében",
                    "nélkül / ellenére",
                    "mögött / felé"
                ], 0, ["c1-modal-teleological-labor-policy"])
            ]
        },
        {
            "num": 4,
            "stem": f"c1-{slug}-04",
            "title": "Strike Rights, Wildcat Actions & Epistemic Forecasts",
            "grammar_title": "Epistemic Stance Adverbials Calibrating Certainty in Macroeconomic Labor Forecasts",
            "grammar_skill": "c1-epistemic-labor-market-projections",
            "goals": [
                "I can analyze strike law restrictions, wildcat strikes, and teacher civil disobedience (*sztrájkjog korlátozása, vadsztrájk, polgári engedetlenség, elégséges szolgáltatás*).",
                "I can employ calibrated epistemic stance adverbials in labor forecasts (*minden valószínűség szerint, előreláthatólag, prognosztizálható módon, feltételezhetően*).",
                "I can debate the political neutralization of public sector unions vs. spontaneous grassroots solidarity."
            ],
            "vocab": [
                {"lemma": "sztrájkjog korlátozása", "translation": "restriction of the right to strike", "pos": "expression"},
                {"lemma": "vadsztrájk", "translation": "wildcat strike (unauthorized walkout)", "pos": "noun"},
                {"lemma": "polgári engedetlenség", "translation": "civil disobedience", "pos": "expression"},
                {"lemma": "még elégséges szolgáltatás", "translation": "minimum statutory service (during strikes)", "pos": "expression"},
                {"lemma": "bérfeszültség robbanása", "translation": "explosion of wage tensions", "pos": "expression"},
                {"lemma": "pedagógustüntetések", "translation": "teachers' protests", "pos": "noun"},
                {"lemma": "szolidaritási sztrájk", "translation": "solidarity strike", "pos": "expression"},
                {"lemma": "szakszervezeti megosztottság", "translation": "trade union fragmentation", "pos": "expression"}
            ],
            "gr_text1": "Epistemic stance adverbials calibrate the analytical certainty of economic and sociological labor projections: `minden valószínűség szerint` (in all probability), `előreláthatólag` (foreseeably), `prognosztizálható módon` (in a predictable manner), `feltételezhetően` (presumably), `várhatóan` (expectedly).",
            "gr_text2": "Example: `A sztrájkjog jogi kiüresítése minden valószínűség szerint nem a békét hozza el, hanem előreláthatólag spontán vadsztrájkokhoz és a munkaerő elvándorlásához vezet`.",
            "gr_table": [
                ["A szigorítások minden valószínűség szerint fokozzák a pedagógusok felmondási kedvét.", "The tightenings in all probability increase teachers' inclination to resign."],
                ["Előreláthatólag újabb munkabeszüntetésekre lehet számítani a közszférában.", "Foreseeably further work stoppages can be expected in the public sector."],
                ["Prognosztizálható módon a bérfeszültségek robbanása elkerülhetetlenné válik a gyárakban.", "In a predictable manner the explosion of wage tensions becomes unavoidable in factories."]
            ],
            "world_story_seg": {
                "seg_slug": "szakszervezet",
                "title": "Amikor elfogy a türelem: polgári engedetlenség és a megbénított sztrájkjog",
                "summary": "Investigating how statutory restrictions on strikes transformed Hungarian protest culture: from paralyzed formal union negotiations to teacher walkouts and student human chains.",
                "paragraphs": [
                    {"type": "narration", "text": "Amikor 2022 tavaszán a kormány rendeleti úton úgy határozott, hogy a pedagógussztrájk ideje alatt a tanórák jelentős részét és a gyermekfelügyeletet kötelezően meg kell tartani, a sztrájk intézménye lényegében elveszítette értelmét. A 'még elégséges szolgáltatás' abszurd jogi kiterjesztésével egy olyan sztrájkot írtak elő, amelyet a külvilág észre sem vehetett: tanítani kellett volna a sztrájk alatt is. A jogi zsákutcába szorított tanárok válasza a polgári engedetlenség lett: ezrek tagadták meg a munkát, vállalva az azonnali elbocsátás kockázatát is."},
                    {"type": "narration", "text": "A társadalomkutatók elemzései szerint a sztrájkjog adminisztratív elfojtása paradox következményekkel járt. Minden valószínűség szerint a jogi utak lezárása nem csillapította, hanem radikalizálta az elégedetlenséget: diákok tízezrei alkottak élőláncot a hidakon, a gyárakban pedig megjelentek a be nem jelentett, villámgyors vadsztrájkok. Prognosztizálható módon a szakszervezeti jogok csorbítása hosszú távon nem fegyelmezett munkaerőt, hanem az állami intézmények működésképtelenségét és a legképzettebb szakemberek végleges pályaelhagyását eredményezi."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Hogyan üresítette ki a 'még elégséges szolgáltatás' rendeleti előírása a sztrájkjogot a közoktatásban?", [
                    "Olyan magas szintű kötelező tanítást írt elő a sztrájk idejére, amely láthatatlanná és hatástalanná tette a munkabeszüntetést.",
                    "Megtiltotta a pedagógusoknak, hogy az iskolák udvarán beszélgessenek.",
                    "Kötelezővé tette az ingyenes fagylaltosztást a sztrájkoló diákoknak."
                ], 0, ["c1-munkaeropiac-vocab"]),
                fb("grammar", "controlled", "A szigorú tiltások minden _____ szerint csak felerősítik a dolgozók felháborodását. (probability / valószínűség)", "valószínűség", "Strict prohibitions in all probability only strengthen workers' indignation.", ["c1-epistemic-labor-market-projections"]),
                match("vocabulary", "controlled", [["vadsztrájk", "törvényi engedély és szakszervezeti jóváhagyás nélküli spontán leállás"], ["polgári engedetlenség", "a lelkiismereti alapú, tudatos jogszabály-megszegés tiltakozásul"], ["szolidaritási sztrájk", "más szakmák dolgozóiért vállalt támogató munkabeszüntetés"], ["még elégséges szolgáltatás", "a sztrájk alatt is kötelezően nyújtandó minimális alapellátás"]], ["c1-munkaeropiac-vocab"]),
                fb("grammar", "practice", "Az alacsony fizetések miatt _____ felgyorsul a tanárok és orvosok elvándorlása. (foreseeably / előreláthatólag)", "előreláthatólag", "Due to low wages foreseeably the out-migration of teachers and doctors accelerates.", ["c1-epistemic-labor-market-projections"]),
                sb("grammar", "practice", ["A", "feszültség", "prognosztizálható", "módon", "robbanáshoz", "vezet", "a", "gyárakban."], ["A", "feszültség", "prognosztizálható", "módon", "robbanáshoz", "vezet", "a", "gyárakban."], "The tension in a predictable manner leads to an explosion in factories.", ["c1-epistemic-labor-market-projections"]),
                dc("dialogue", [
                    {"speaker": "Oktatáskutató", "text": "Megoldotta-e a státusztörvény a pedagógushiányt?"},
                    {"speaker": "Szociológus", "text": "Minden valószínűség szerint a jogfosztás csak _____ a pályaelhagyást."},
                ], ["gyorsította", "megállította", "megjutalmazta"], 0, ["c1-epistemic-labor-market-projections"]),
                sw("production", [{"prompt": "Write a sentence projecting the outcome of union suppression using an epistemic stance adverbial.", "answer": "A sztrájkjog adminisztratív elfojtása minden valószínűség szerint nem az engedelmességet növeli, hanem prognosztizálható módon spontán vadsztrájkokat és a fiatal munkavállalók külföldre vándorlását idézi elő."}], ["c1-epistemic-labor-market-projections"]),
                mc("grammar", "check", "Melyik kifejezés tölt be tudományos valószínűséget és előrejelzést kifejező szerepet?", [
                    "minden valószínűség szerint / prognosztizálható módon",
                    "egyértelműen tegnap este",
                    "nagyon lassan futva"
                ], 0, ["c1-epistemic-labor-market-projections"])
            ]
        },
        {
            "num": 5,
            "stem": f"c1-{slug}-05",
            "title": "Brain Drain, Austrian Commuting & Synthetic Collective Evaluation",
            "grammar_title": "Evaluative Synthesis Particles Formulating Comprehensive Assessments of Labor Rights",
            "grammar_skill": "c1-adv-synthetic-collective-evaluatives",
            "goals": [
                "I can analyze western cross-border commuting to Austria, brain drain, and wage convergence limits (*nyugati ingázás, burgenlandi munkavállalás, agyelszívás, bérfelzárkózás*).",
                "I can employ elevated evaluative synthesis particles (*mindent összegezve, végső konklúzióként, egyértelműen megállapítható*).",
                "I can synthesize the macro-future of Hungarian labor: low-wage assembly colony vs. high added-value innovation."
            ],
            "vocab": [
                {"lemma": "határ menti ingázás", "translation": "cross-border commuting", "pos": "expression"},
                {"lemma": "agyelszívás", "translation": "brain drain", "pos": "noun"},
                {"lemma": "bérkonvergencia", "translation": "wage convergence", "pos": "noun"},
                {"lemma": "összeszerelő üzem", "translation": "assembly plant / maquiladora", "pos": "expression"},
                {"lemma": "hozzáadott érték hiánya", "translation": "lack of added value", "pos": "expression"},
                {"lemma": "tudásalapú gazdaság", "translation": "knowledge-based economy", "pos": "expression"},
                {"lemma": "munkavállalói autonómia", "translation": "worker autonomy", "pos": "expression"},
                {"lemma": "társadalmi kohézió", "translation": "social cohesion", "pos": "expression"}
            ],
            "gr_text1": "Synthetic evaluative particles draw systemic conclusions from multifaceted economic arguments: `mindent összegezve` (summarizing everything), `végső konklúzióként` (as a final conclusion), `egyértelműen megállapítható` (it can be unambiguously established), `végeredményben` (in the final analysis), `összességében tekintve` (looking at it comprehensively).",
            "gr_text2": "Example: `Mindent összegezve, az olcsó munkaerőre és az adókedvezményekre épülő gazdaságpolitika végső konklúzióként egy alacsony bérű összeszerelő üzemmé degradálta az országot`.",
            "gr_table": [
                ["Mindent összegezve, a bérfelzárkózás elmaradása miatt tízezrek kényszerülnek ausztriai ingázásra.", "Summarizing everything, due to the failure of wage convergence tens of thousands are forced into Austrian commuting."],
                ["Végső konklúzióként levonható, hogy valódi bérfejlesztés nélkül a hazai gazdaság versenyképtelen marad.", "As a final conclusion it can be deduced that without genuine wage development the domestic economy remains uncompetitive."],
                ["Egyértelműen megállapítható, hogy a jövő a tudásalapú gazdaság és a munkavállalói méltóság tiszteletében rejlik.", "It can be unambiguously established that the future lies in the knowledge-based economy and the respect for worker dignity."]
            ],
            "world_story_seg": {
                "seg_slug": "berfelzarkozas",
                "title": "Hajnali vonatok Bécs felé: a határ menti ingázás és a magyar jövő",
                "summary": "Following the thousands of Hungarian commuters crossing the border daily from Sopron, Szombathely, and Mosonmagyaróvár to Austria, and synthesizing the future of domestic labor.",
                "paragraphs": [
                    {"type": "narration", "text": "Hajnali öt órakor a soproni és szombathelyi vasútállomásokon még sötét van, de a peronok zsúfolásig megteltek. Pékek, ápolók, vendéglátósok, mérnökök és építőipari szakemberek szállnak fel az Ausztria felé induló vonatokra. Noha otthonuk, családjuk és szívük Magyarországhoz köti őket, a határon túli háromszoros vagy négyszeres fizetés, a megbecsülés és a kiszámítható szociális biztonság mindennapi ingázásra kényszeríti őket. Nyugat-Magyarország gazdasági élete ma már elválaszthatatlanul összefonódott a burgenlandi és bécsi munkaerőpiaccal."},
                    {"type": "narration", "text": "Mindent összegezve, ez a mindennapi népvándorlás a magyar bérfelzárkózás drámai kudarcának legtisztább bizonyítéka. Egy olyan gazdaságmodell, amely a képzetlen munkaerő alacsony bérével és a multiknak nyújtott milliárdos állami támogatásokkal próbál versenyezni, szükségszerűen vesztes marad a huszonegyedik században. Végső konklúzióként kimondható: Magyarország csak akkor tarthatja meg legtehetségesebb dolgozóit és állíthatja meg a pusztító agyelszívást, ha az összeszerelő üzemek helyett a tudásalapú innovációra és a dolgozói méltóság megkérdőjelezhetetlen tiszteletére alapozza a jövőjét."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Miért ingáznak naponta tízezrek Nyugat-Magyarországról Ausztriába dolgozni?", [
                    "Mert a határon túl a hazai bérszínvonal többszörösét kereshetik meg, jobb munkakörülmények és stabil szociális biztonság mellett.",
                    "Mert Ausztriában tilos a kerékpározás a városokban.",
                    "Mert a magyar hatóságok kötelezővé tették a heti külföldi utazást."
                ], 0, ["c1-munkaeropiac-vocab"]),
                fb("grammar", "controlled", "Mindent _____, a hazai bérfelzárkózás megtorpanása gyorsítja az agyelszívást. (summarizing / összegezve)", "összegezve", "Summarizing everything, the halting of domestic wage convergence accelerates brain drain.", ["c1-adv-synthetic-collective-evaluatives"]),
                match("vocabulary", "controlled", [["határ menti ingázás", "a szomszédos országban végzett mindennapi munka lakóhelyváltás nélkül"], ["agyelszívás", "a képzett értelmiség és szakmunkások elvándorlása"], ["összeszerelő üzem", "alacsony hozzáadott értékű, betanított munkára épülő gyár"], ["tudásalapú gazdaság", "az innovációra, oktatásra és magas szakértelemre épülő gazdaság"]], ["c1-munkaeropiac-vocab"]),
                fb("grammar", "practice", "Végső _____ megállapítható, hogy a tisztességes bérek nélkül nincs gazdasági felemelkedés. (conclusion / konklúzióként)", "konklúzióként", "As a final conclusion it can be established that without fair wages there is no economic rise.", ["c1-adv-synthetic-collective-evaluatives"]),
                sb("grammar", "practice", ["Mindent", "összegezve,", "a", "dolgozók", "megbecsülése", "a", "siker", "kulcsa."], ["Mindent", "összegezve,", "a", "dolgozók", "megbecsülése", "a", "siker", "kulcsa."], "Summarizing everything, the appreciation of workers is the key to success.", ["c1-adv-synthetic-collective-evaluatives"]),
                dc("dialogue", [
                    {"speaker": "Közgazdász kutató", "text": "Hogyan foglalható össze a hazai munkaerőpiac legfőbb kihívása?"},
                    {"speaker": "Társadalomtudós", "text": "Mindent összegezve, az összeszerelő üzemek helyett a tudásalapú innovációra kell _____."},
                ], ["támaszkodnunk", "haragudnunk", "felejtenünk"], 0, ["c1-adv-synthetic-collective-evaluatives"]),
                sw("production", [{"prompt": "Write a concluding policy synthesis on the Hungarian labor market using 'Mindent összegezve'.", "answer": "Mindent összegezve, Magyarország gazdasági felemelkedésének egyetlen fenntartható útja az olcsó összeszerelő modell meghaladása, a tudásalapú bérek európai felzárkóztatása és a dolgozói méltóság védelme."}], ["c1-adv-synthetic-collective-evaluatives"]),
                mc("grammar", "check", "Melyik kifejezés alkalmas átfogó makrogazdasági értékelés és összegzés megfogalmazására?", [
                    "Mindent összegezve / Végső konklúzióként",
                    "A lépcsőn leszaladva",
                    "Egy pillanatra megállva"
                ], 0, ["c1-adv-synthetic-collective-evaluatives"])
            ]
        }
    ]

    for l in disc_lessons:
        emit_instructional_lesson(21, "discourse", l, disc_title, disc_intro if l["num"] == 1 else None)

    # Combined World Story
    write_json(
        ROOT / "content" / "hu" / "stories" / "world" / "c1" / f"c1-{slug}.json",
        {
            "id": f"story.c1.{slug}",
            "title": "A kettészakadt munka világa: vendégmunkások, futószalagok és az elvándorlás kora",
            "level": "C1",
            "type": "world",
            "order": 21,
            "lesson": 5,
            "estimatedMinutes": 8,
            "summary": "Panoramic investigation of Hungary's dual labor market: the rapid importation of third-country guest workers, assembly-line exhaustion in battery megafactories, the gig economy under algorithmic control, the paralysis of strike rights, and the thousands commuting daily across the Austrian border.",
            "grammar": [
                "c1-discourse-polarization-antithesis",
                "c1-adv-temporal-succession-chains",
                "c1-modal-teleological-labor-policy",
                "c1-epistemic-labor-market-projections",
                "c1-adv-synthetic-collective-evaluatives"
            ],
            "vocabularyTopics": [
                "The Dual Labor Market: Guest Workers, Gig Economy & Wage Convergence",
                "Guest Workers, Third-Country Labor & Polarization Antithesis",
                "Industrial Assembly Lines & Temporal Succession Chains",
                "Platform Capitalism, Gig Economy & Teleological Labor Policy",
                "Strike Rights, Wildcat Actions & Epistemic Forecasts",
                "Brain Drain, Austrian Commuting & Synthetic Collective Evaluation"
            ],
            "paragraphs": [
                {"type": "narration", "text": "A huszonegyedik század harmadik évtizedében a magyar munkaerőpiac mély és drámai átalakuláson megy keresztül. A kormányzati gazdaságpolitika az újraiparosítás és az akkumulátorgyártás zászlaja alatt hatalmas nemzetközi tőkét vonzott az országba, ám e beruházások nyomán nem az ígért polgári jólét, hanem egy élesen kettészakadt, törékeny és polarizált munkavilág jött létre."},
                {"type": "narration", "text": "A gyárak és ipari parkok környékén vendégmunkások tízezrei dolgoznak szigorúan ellenőrzött konténerszállásokról ingázva a futószalagokhoz, míg a hazai fizikai munkások a bérletörés és az embertelen normaemelések szorításában vergődnek. Ezzel párhuzamosan a nagyvárosokban a platformkapitalizmus hozott létre egy új, jogfosztott réteget: az algoritmusok által vezérelt ételfutárokat és kisvállalkozókat, akik a KATA eltörlése után minden korábbinál kiszolgáltatottabbá váltak."},
                {"type": "narration", "text": "Amikor pedig a munkavállalók szót emelnének az érdekeikért, a sztrájkjog adminisztratív elfojtásával és a minimális szolgáltatások kényszerével találják szemben magukat. A tanárok polgári engedetlensége és a gyári vadsztrájkok világosan jelzik: a törvényes érdekvédelmi utak eltorlaszolása nem békét, hanem radikalizálódást és a társadalmi kohézió felbomlását eredményezi."},
                {"type": "narration", "text": "Mindent összegezve, a hajnali soproni vonatokon Ausztriába ingázó tízezrek a hazai bérfelzárkózás elmaradásának élő mementói. Magyarország nem maradhat fenn tartósan egy olcsó, jogfosztott összeszerelő gyarmatként. A nemzeti megmaradás és az emberi méltóság elemi követelménye, hogy a gazdaságpolitika a dolgozói jogok garantálására, a tisztes európai bérekre és a tudásalapú innovációra építse a jövőjét."}
            ]
        }
    )

    # Discourse Consolidation
    emit_consolidation_lesson(
        21,
        "discourse",
        f"c1-{slug}-consolidation",
        disc_title,
        [
            "I can analyze the dual labor market, guest worker policies, and assembly-line intensity.",
            "I can evaluate platform capitalism, algorithmic management, and cross-border commuting to Austria.",
            "I can debate strike law restrictions, wildcat protest actions, and the future of Hungarian labor sovereignty."
        ],
        [
            mc("grammar", "recognize", "Milyen szerkezettel fejezhetünk ki éles munkaerőpiaci ellentétezést?", [
                "míg egyfelől a vállalatok profitja nő, addig másfelől a dolgozók reálbére csökken",
                "mivel mindenki időben beért a munkahelyére reggel",
                "amikor süt a nap az ipari park épületei felett"
            ], 0, ["c1-discourse-polarization-antithesis"]),
            mc("grammar", "recognize", "Melyik kifejezés fogalmaz meg célirányos szakpolitikai törekvést?", [
                "a dolgozói jogok szavatolása céljából / a bérfelzárkózás előmozdítása végett",
                "hogyha van kedvük sztrájkolni",
                "anélkül, hogy elolvasták volna a híreket"
            ], 0, ["c1-modal-teleological-labor-policy"]),
            match("vocabulary", "recognize", [["vendégmunkás", "harmadik országbeli kötött munkavállaló"], ["algoritmikus irányítás", "applikációk és szoftverek általi emberi munkavezérlés"], ["határ menti ingázás", "napi átjárás a jobb fizetésért Ausztriába"], ["vadsztrájk", "törvényi jóváhagyás nélküli spontán munkabeszüntetés"], ["összeszerelő üzem", "alacsony hozzáadott értékű, betanított gyári modell"]], ["c1-munkaeropiac-vocab"]),
            fb("vocabulary", "recall", "A távol-keleti országokból érkező _____ száma rohamosan emelkedett a magyar gyárakban. (guest workers / vendégmunkások)", "vendégmunkások", "The number of guest workers arriving from Far Eastern countries increased rapidly in Hungarian factories.", ["c1-munkaeropiac-vocab"]),
            fb("vocabulary", "recall", "A magasan képzett orvosok és mérnökök elvándorlását az országból _____ nevezzük. (brain drain / agyelszívásnak)", "agyelszívásnak", "The out-migration of highly qualified doctors and engineers from the country is called brain drain.", ["c1-munkaeropiac-vocab"]),
            fb("grammar", "recall", "A munkavállalók biztonságának megóvása _____ új szabályokat fogadtak el. (for the purpose of / céljából)", "céljából", "For the purpose of preserving workers' safety new rules were adopted.", ["c1-modal-teleological-labor-policy"]),
            fb("grammar", "context", "Míg egyfelől nőttek a gyári beruházások, _____ másfelől az elvándorlás tovább gyorsult. (meanwhile / addig)", "addig", "While on the one hand factory investments grew, meanwhile on the other hand out-migration further accelerated.", ["c1-discourse-polarization-antithesis"]),
            fb("grammar", "context", "Mindent _____, a tisztességes bérezés a társadalmi béke egyetlen záloga. (summarizing / összegezve)", "összegezve", "Summarizing everything, fair compensation is the sole pledge of social peace.", ["c1-adv-synthetic-collective-evaluatives"]),
            mc("grammar", "context", "Mi az 'algoritmikus irányítás' legfőbb munkajogi veszélye a futárok szerint?", [
                "Hogy a munkavállaló nem tud emberi vezetővel egyeztetni, és a szoftver azonnali, fellebbezhetetlen büntetéseket oszt ki.",
                "Hogy túl szép színekben pompázik az okostelefon kijelzője.",
                "Hogy túl gyorsan merül le az akkumulátor zenehallgatás közben."
            ], 0, ["c1-munkaeropiac-vocab"]),
            sb("grammar", "produce", ["A", "méltányos", "munka", "a", "jövő", "legfontosabb", "értéke."], ["A", "méltányos", "munka", "a", "jövő", "legfontosabb", "értéke."], "Fair work is the most important value of the future.", ["c1-adv-synthetic-collective-evaluatives"]),
            sw("production", [{"prompt": "Write a critical diagnostic sentence on the dual labor market using an antithetical structure.", "answer": "Míg egyfelől az akkumulátorgyárak rekordprofitot termelnek a külföldi befektetőknek, addig másfelől a magyar dolgozók kimerültsége és az elfojtott bérnövekedés mély társadalmi elkeseredést szül."}], ["c1-discourse-polarization-antithesis"]),
            sw("production", [{"prompt": "Formulate a concluding thought on Hungarian wage convergence and Austrian cross-border commuting.", "answer": "Mindent összegezve, az országhatáron túli ingázás tömeges jelensége félreérthetetlenül bizonyítja: valódi európai bérkonvergencia és a munkavállalói méltóság védelme nélkül a magyar vidék elkerülhetetlenül elveszíti legértékesebb munkaerejét."}], ["c1-adv-synthetic-collective-evaluatives"])
        ]
    )

    print("=== Finished C1 Unit 21 ===")


if __name__ == "__main__":
    generate_unit_21()
