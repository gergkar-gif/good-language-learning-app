#!/usr/bin/env python3
"""
Hungarian C1 Block 3 - Unit 13 Generator:
  - Track 1 (Core): Unit 13 — "Macroeconomic Architecture, Fiscal Policy & Monetary Stance" (c1-13)
  - Track 2 (Discourse): Unit 13 — "Monetary Sovereignty, the Forint & the Eurozone Dilemma" (c1-monetaris)
"""

import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT))

from scripts.c1_block1.common import mc, match, fb, sb, dc, sw, write_json, emit_instructional_lesson, emit_consolidation_lesson
from scripts.c1_block3.registry_helper import register_unit


def generate_unit_13():
    print("=== Generating C1 Unit 13 ===")
    
    # Register skills & titles
    new_skills = {
        "c1-13-vocab": {"kind": "vocabulary"},
        "c1-monetaris-vocab": {"kind": "vocabulary"},
        "c1-macroeconomic-indicators": {"kind": "grammar"},
        "c1-monetary-tightening-clauses": {"kind": "grammar"},
        "c1-fiscal-counterbalancing": {"kind": "grammar"},
        "c1-inflationary-expectations": {"kind": "grammar"},
        "c1-growth-model-synthesis": {"kind": "grammar"},
    }
    new_titles = {
        "c1-13-vocab": "reading",
        "c1-monetaris-vocab": "reading",
        "c1-macroeconomic-indicators": "macroeconomic indicators nominal trends and quantitative metric relations",
        "c1-monetary-tightening-clauses": "monetary policy transmission central bank rate setting and quantitative tightening",
        "c1-fiscal-counterbalancing": "fiscal policy counterbalancing budgetary deficits and debt path stabilization",
        "c1-inflationary-expectations": "inflationary expectations core consumer pricing and price wage spiral modeling",
        "c1-growth-model-synthesis": "structural macroeconomic growth models balance of payments and external equilibrium",
    }
    
    core_title = "Macroeconomic Architecture, Fiscal Policy & Monetary Stance"
    core_stems = [f"c1-13-0{i}" for i in range(1, 6)] + ["c1-13-consolidation"]
    disc_title = "Monetary Sovereignty, the Forint & the Eurozone Dilemma"
    disc_stems = [f"c1-monetaris-0{i}" for i in range(1, 6)] + ["c1-monetaris-consolidation"]
    
    register_unit(13, core_title, core_stems, disc_title, disc_stems, new_skills, new_titles)

    # ----------------------------------------------------
    # TRACK 1: CORE (c1-13)
    # ----------------------------------------------------
    core_intro = [
        "Macroeconomic analysis and economic journalism in Hungarian rely on high-precision statistical framing (bázishatás, nominális konvergencia, reálkamat-környezet), intricate causal-concessive links (noha a keresleti nyomás enyhült, a kínálati oldali sokkok továbbra is...), and dense participial modifiers.",
        "In this unit, anchored by János Kornai's world-famous economic masterpiece 'A hiány' (Economics of Shortage, 1980), you will master central bank forward guidance, fiscal consolidation terminology, and macroeconomic structural modeling in academic Hungarian."
    ]

    core_lessons = [
        {
            "num": 1,
            "stem": "c1-13-01",
            "title": "Macroeconomic Indicators & Trend Predications",
            "grammar_title": "Quantitative Metric Relations and Nominal Trend Formulations",
            "grammar_skill": "c1-macroeconomic-indicators",
            "goals": [
                "I can analyze complex macroeconomic indicators (*bruttó hazai termék, bázishatás, reálbér-növekedés*).",
                "I can formulate trend comparisons using adverbial participles (*összevetve a megelőző negyedévvel, meghaladva a várakozásokat*).",
                "I can evaluate economic growth dynamics in formal analytical Hungarian."
            ],
            "vocab": [
                {"lemma": "bruttó hazai termék", "translation": "Gross Domestic Product (GDP)", "pos": "noun"},
                {"lemma": "bázishatás", "translation": "base effect (statistical comparison base)", "pos": "noun"},
                {"lemma": "reálbér-növekedés", "translation": "real wage growth", "pos": "noun"},
                {"lemma": "konjunktúra", "translation": "economic upturn, boom", "pos": "noun"},
                {"lemma": "recesszió", "translation": "recession, economic contraction", "pos": "noun"},
                {"lemma": "stagnál", "translation": "to stagnate", "pos": "verb"},
                {"lemma": "korrigál", "translation": "to adjust, correct (seasonally / structurally)", "pos": "verb"},
                {"lemma": "kibocsátási rés", "translation": "output gap", "pos": "noun"}
            ],
            "gr_text1": "Macroeconomic analytical prose formulates rate-of-change and index comparisons using adverbial participle clauses fronting the sentence: `Összevetve a megelőző év azonos időszakával...` (Compared to the same period of the previous year...), `Kiszűrve a szezonális hatásokat...` (Filtering out seasonal effects...).",
            "gr_text2": "Notice the use of compound postpositional and ablative structures to express variance from forecasts: `a várakozásoktól elmaradva` (falling short of expectations), `a prognózist felülmúlva` (exceeding projections).",
            "gr_table": [
                ["A gazdasági növekedés a várakozásokat felülmúlva 3,2%-ot ért el.", "Economic growth reached 3.2%, surpassing expectations."],
                ["Kiszűrve a bázishatást, a termelés stagnálást mutat.", "Filtering out the base effect, production shows stagnation."],
                ["A reálbérek emelkedése élénkíti a belső fogyasztást.", "The rise in real wages stimulates domestic consumption."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mit fejez ki a 'bázishatás' (base effect) a makrogazdasági statisztikában?", ["Az előző évi viszonyítási időszak rendkívüli szintjének torzító hatását az aktuális növekedési indexre.", "A jegybank alaptőkéjének éves kamatát.", "A minimálbér kötelező összegét."], 0, ["c1-13-vocab"]),
                fb("grammar", "controlled", "A bruttó hazai termék bővülése a várakozásokat felülmúlva elérte a három _____ növekedést. (percent / százalékos)", "százalékos", "The expansion of gross domestic product reached a three percent growth, surpassing expectations.", ["c1-macroeconomic-indicators"]),
                match("vocabulary", "controlled", [["bruttó hazai termék", "GDP"], ["bázishatás", "base effect"], ["konjunktúra", "economic boom"], ["kibocsátási rés", "output gap"]], ["c1-13-vocab"]),
                fb("grammar", "practice", "A szezonális hatásoktól megtisztított adatok szerint az ipari kibocsátás enyhén _____. (stagnated / stagnált)", "stagnált", "According to data adjusted for seasonal effects, industrial output slightly stagnated.", ["c1-macroeconomic-indicators"]),
                sb("grammar", "practice", ["A", "reálbér-növekedés", "fokozatosan", "helyreállítja", "a", "háztartások", "vásárlóerejét."], ["A", "reálbér-növekedés", "fokozatosan", "helyreállítja", "a", "háztartások", "vásárlóerejét."], "Real wage growth gradually restores household purchasing power.", ["c1-macroeconomic-indicators"]),
                dc("dialogue", [
                    {"speaker": "Elemző", "text": "Hogyan értékeli a második negyedéves GDP-adatokat?"},
                    {"speaker": "Közgazdász", "text": "A technikai recesszió után végre a mérsékelt _____ jeleit tapasztaljuk."},
                ], ["növekedés", "infláció", "válság"], 0, ["c1-macroeconomic-indicators"]),
                sw("production", [{"prompt": "Write an opening sentence for an economic report using 'összevetve a megelőző időszakkal'.", "answer": "Összevetve a megelőző negyedévvel, a magyar gazdaság teljesítménye enyhe emelkedést mutat, ám a beruházások dinamikája továbbra is visszafogott marad."}], ["c1-macroeconomic-indicators"]),
                mc("grammar", "check", "Melyik szerkezet fejezi ki a legválasztékosabban a várakozások túlszárnyalását?", [
                    "az elemzői konszenzust felülmúlva",
                    "sokkal jobb lett mint gondolták",
                    "túl jó lett a vártnál"
                ], 0, ["c1-macroeconomic-indicators"])
            ]
        },
        {
            "num": 2,
            "stem": "c1-13-02",
            "title": "Monetary Policy Transmission & Central Bank Rate Setting",
            "grammar_title": "Monetary Transmission Channels, Yield Curves and Rate Guidance",
            "grammar_skill": "c1-monetary-tightening-clauses",
            "goals": [
                "I can analyze central bank rate decisions (*irányadó alapkamat, kamatfolyosó, monetáris szigorítás*).",
                "I can evaluate monetary transmission channels (*transzmissziós mechanizmus, likviditási többlet*).",
                "I can articulate monetary policy forward guidance (*előretekintő iránymutatás*) in formal Hungarian."
            ],
            "vocab": [
                {"lemma": "irányadó kamat", "translation": "benchmark base interest rate", "pos": "noun"},
                {"lemma": "kamatfolyosó", "translation": "interest rate corridor", "pos": "noun"},
                {"lemma": "monetáris szigorítás", "translation": "monetary tightening / policy restriction", "pos": "noun"},
                {"lemma": "enyhítési ciklus", "translation": "easing cycle, rate-cut cycle", "pos": "noun"},
                {"lemma": "transzmissziós mechanizmus", "translation": "transmission mechanism", "pos": "noun"},
                {"lemma": "hozamgörbe", "translation": "yield curve", "pos": "noun"},
                {"lemma": "előretekintő iránymutatás", "translation": "forward guidance", "pos": "noun"},
                {"lemma": "hitelkondíció", "translation": "credit condition / borrowing term", "pos": "noun"}
            ],
            "gr_text1": "Monetary policy releases by the Hungarian National Bank (MNB) utilize telic clauses coupled with instrumental causal framing: `Annak érdekében, hogy a másodkörös inflációs hatások kiküszöbölhetők legyenek, a Monetáris Tanács a szigorú kamatkondíciók fenntartásáról döntött`.",
            "gr_text2": "Concessive balances express the trade-off between disinflation and economic growth: `Noha a nominális kamatszint csökkent, a reálkamat-környezet szigorú maradt` (Although the nominal rate level declined, the real interest rate environment remained restrictive).",
            "gr_table": [
                ["A Monetáris Tanács az alapkamat szinten tartása mellett döntött.", "The Monetary Council decided to maintain the base rate unchanged."],
                ["A transzmissziós mechanizmus hatékonysága kulcsfontosságú.", "The efficiency of the transmission mechanism is crucial."],
                ["Az előretekintő iránymutatás óvatos és adatvezérelt monetáris politikát vetít előre.", "Forward guidance projects cautious and data-driven monetary policy."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mi a jegybanki kamatfolyosó (interest rate corridor) feladata?", ["A bankközi egynapos kamatok ingadozásának keretek közé szorítása az alapkamat körül.", "A devizaváltási díjak megszabása a turistáknak.", "A minisztériumi bérek kifizetése."], 0, ["c1-13-vocab"]),
                fb("grammar", "controlled", "A Monetáris Tanács az inflációs kockázatok mérséklése céljából határozott monetáris _____ mellett kötelezte el magát. (tightening / szigorítás)", "szigorítás", "The Monetary Council committed itself to resolute monetary tightening to mitigate inflation risks.", ["c1-monetary-tightening-clauses"]),
                match("vocabulary", "controlled", [["irányadó kamat", "benchmark policy rate"], ["kamatfolyosó", "interest rate corridor"], ["hozamgörbe", "yield curve"], ["előretekintő iránymutatás", "forward guidance"]], ["c1-13-vocab"]),
                fb("grammar", "practice", "A jegybank a szigorú kamatkörnyezet fenntartásával kívánja biztosítani az árstabilitást és a pénzügyi piacok _____. (stability / stabilitását)", "stabilitását", "The central bank intends to ensure price stability and financial market stability by maintaining a restrictive rate environment.", ["c1-monetary-tightening-clauses"]),
                sb("grammar", "practice", ["A", "transzmissziós", "csatornák", "akadálytalan", "működése", "nélkülözhetetlen", "az", "infláció", "letöréséhez."], ["A", "transzmissziós", "csatornák", "akadálytalan", "működése", "nélkülözhetetlen", "az", "infláció", "letöréséhez."], "Unimpeded functioning of transmission channels is indispensable to bringing down inflation.", ["c1-monetary-tightening-clauses"]),
                dc("dialogue", [
                    {"speaker": "Kötvénykereskedő", "text": "Milyen irányú elmozdulásra számít a jövő heti jegybanki ülésen?"},
                    {"speaker": "Portfóliókezelő", "text": "Az óvatos kommunikáció alapján a jegybank folytatja az adatvezérelt _____ ciklust."},
                ], ["enyhítési", "válság", "hitelezési"], 0, ["c1-monetary-tightening-clauses"]),
                sw("production", [{"prompt": "Write a central bank rate-decision sentence using 'kamatfolyosó' and 'transzmisszió'.", "answer": "A Monetáris Tanács a kamatfolyosó szimmetrikus szűkítésével javította a monetáris transzmisszió hatékonyságát, miközben fenntartotta a szigorú restriktív irányvonalat."}], ["c1-monetary-tightening-clauses"]),
                mc("grammar", "check", "Mit fejez ki a 'reálkamat-környezet' fogalma?", [
                    "A nominális kamatláb és a várható inflációs ráta közötti különbséget.",
                    "A bankok által felszámított számlavezetési díjat.",
                    "A tőzsdei részvények napi árfolyamát."
                ], 0, ["c1-monetary-tightening-clauses"])
            ]
        },
        {
            "num": 3,
            "stem": "c1-13-03",
            "title": "Fiscal Policy, Budget Deficit & Debt Trajectory",
            "grammar_title": "Fiscal Counterbalancing, Primary Balance and Debt-to-GDP Ratios",
            "grammar_skill": "c1-fiscal-counterbalancing",
            "goals": [
                "I can analyze fiscal policy levers (*költségvetési hiány, adósságpálya, elsődleges egyenleg*).",
                "I can evaluate countercyclical fiscal counterbalancing (*anticiklikus költségvetési politika*).",
                "I can formulate fiscal consolidation strategies (*fiskális konszolidáció, kiadási plafon*)."
            ],
            "vocab": [
                {"lemma": "költségvetési hiány", "translation": "budget deficit, fiscal deficit", "pos": "noun"},
                {"lemma": "államadósság-ráta", "translation": "debt-to-GDP ratio", "pos": "noun"},
                {"lemma": "elsődleges egyenleg", "translation": "primary balance (budget balance excluding interest payments)", "pos": "noun"},
                {"lemma": "fiskális konszolidáció", "translation": "fiscal consolidation / austerity", "pos": "noun"},
                {"lemma": "anticiklikus", "translation": "counter-cyclical", "pos": "adjective"},
                {"lemma": "adósságfék", "translation": "debt brake (constitutional limit)", "pos": "noun"},
                {"lemma": "kamatteher", "translation": "interest burden / debt servicing cost", "pos": "noun"},
                {"lemma": "költségvetési mozgástér", "translation": "fiscal room for maneuver", "pos": "noun"}
            ],
            "gr_text1": "Fiscal analysis in Hungarian relies on conditional and consequence-driven subordination: `Amennyiben a kormányzat nem hajt végre strukturális kiadáscsökkentést, úgy az államadósság törékeny pályára kerül`.",
            "gr_text2": "Phrases expressing containment of debt deploy spatial metaphors: `lefelé ívelő adósságpályára állítja a költségvetést` (places the budget on a downward debt trajectory), `megszilárdítja a fiskális fegyelmet` (solidifies fiscal discipline).",
            "gr_table": [
                ["A fiskális fegyelem helyreállítása csökkenti az ország kockázati felárát.", "Restoring fiscal discipline lowers the country's risk premium."],
                ["Az adósságráta lefaragása érdekében elengedhetetlen a strukturális konszolidáció.", "Structural consolidation is essential to reduce the debt ratio."],
                ["A megnövekedett kamatterhek szűkítik a költségvetési mozgásteret.", "Increased interest burdens narrow fiscal leeway."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mit jelent az 'elsődleges egyenleg' (primary balance) a költségvetési gazdálkodásban?", ["A költségvetés kamatfizetések nélkül számított bevételeinek és kiadásainak egyenlegét.", "Az első félévben befolyt összes adóbevételt.", "A miniszterelnöki hivatal költségvetését."], 0, ["c1-13-vocab"]),
                fb("grammar", "controlled", "A megnövekedett államadósság kamatterhei jelentősen beszűkítették a kormányzat költségvetési _____. (room for maneuver / mozgásterét)", "mozgásterét", "The interest burdens of increased public debt significantly narrowed the government's fiscal room for maneuver.", ["c1-fiscal-counterbalancing"]),
                match("vocabulary", "controlled", [["költségvetési hiány", "budget deficit"], ["államadósság-ráta", "debt-to-GDP ratio"], ["elsődleges egyenleg", "primary budget balance"], ["fiskális konszolidáció", "fiscal consolidation"]], ["c1-13-vocab"]),
                fb("grammar", "practice", "A gazdaság lehűlése idején alkalmazott _____ fiskális politika célja a kereslet fenntartása. (counter-cyclical / anticiklikus)", "anticiklikus", "The goal of counter-cyclical fiscal policy applied during economic slowdown is maintaining demand.", ["c1-fiscal-counterbalancing"]),
                sb("grammar", "practice", ["A", "tartós", "fiskális", "konszolidáció", "elengedhetetlen", "a", "hitelminősítés", "javításához."], ["A", "tartós", "fiskális", "konszolidáció", "elengedhetetlen", "a", "hitelminősítés", "javításához."], "Sustained fiscal consolidation is indispensable to improving credit ratings.", ["c1-fiscal-counterbalancing"]),
                dc("dialogue", [
                    {"speaker": "Újságíró", "text": "Hogyan kívánja a kormány lefaragni a költségvetési hiányt?"},
                    {"speaker": "Pénzügyminiszter", "text": "A kiadási prioritások felülvizsgálatával és a fegyelmezett _____ megvalósításával."},
                ], ["konszolidáció", "költekezés", "válság"], 0, ["c1-fiscal-counterbalancing"]),
                sw("production", [{"prompt": "Write a sentence formulating the imperative of fiscal debt reduction.", "answer": "Az államadósság-ráta csökkenő pályára állítása elengedhetetlen a pénzügyi szuverenitás és a nemzetközi befektetői bizalom megőrzése érdekében."}], ["c1-fiscal-counterbalancing"]),
                mc("grammar", "check", "Mi az alkotmányos adósságfék (debt brake) célja?", [
                    "Annak jogi biztosítása, hogy az államadósság a GDP arányában évről évre mérséklődjön.",
                    "A banki hitelkamatok maximálása.",
                    "A pénzforgalom készpénzmentesítése."
                ], 0, ["c1-fiscal-counterbalancing"])
            ]
        },
        {
            "num": 4,
            "stem": "c1-13-04",
            "title": "Inflationary Dynamics, Core Index & Price-Wage Spirals",
            "grammar_title": "Inflation Modeling: Demand-Pull, Cost-Push & Inertial Expectations",
            "grammar_skill": "c1-inflationary-expectations",
            "goals": [
                "I can analyze inflation drivers (*maginfláció, költségoldali sokk, ár-bér spirál*).",
                "I can evaluate inflation expectations and inertial indexation (*várakozások horgonyzottsága*).",
                "I can explain consumer basket dynamics in formal economic Hungarian."
            ],
            "vocab": [
                {"lemma": "maginfláció", "translation": "core inflation (excluding volatile food & energy)", "pos": "noun"},
                {"lemma": "ár-bér spirál", "translation": "price-wage spiral", "pos": "noun"},
                {"lemma": "várakozások lehorgonyzása", "translation": "anchoring of inflation expectations", "pos": "expression"},
                {"lemma": "költségoldali sokk", "translation": "cost-push shock / supply shock", "pos": "noun"},
                {"lemma": "keresleti nyomás", "translation": "demand-pull pressure", "pos": "noun"},
                {"lemma": "dezinfláció", "translation": "disinflation (slowing rate of price increases)", "pos": "noun"},
                {"lemma": "fogyasztói kosár", "translation": "consumer basket / CPI basket", "pos": "noun"},
                {"lemma": "átárazás", "translation": "repricing, markup adjustment", "pos": "noun"}
            ],
            "gr_text1": "Economic discourse on inflation distinguishes between transitory supply shocks and persistent structural inflation using the concept of *lehorgonyzott várakozások* (anchored expectations).",
            "gr_text2": "Syntactically, cause-and-effect sequences express spiraling dynamics: `A megugró energiaárak átgyűrűzése a fogyasztói árakba megnöveli a bérköveteléseket, ami ár-bér spirál kialakulásával fenyeget`.",
            "gr_table": [
                ["A maginfláció pontosabban mutatja a tartós áremelkedési trendeket.", "Core inflation reflects persistent price increase trends more accurately."],
                ["A dezinflációs folyamat a fogyasztási kereslet visszaesésével gyorsult.", "The disinflationary process accelerated with the decline in consumer demand."],
                ["A várakozások lehorgonyzása nélkülözhetetlen az árstabilitáshoz.", "Anchoring expectations is essential for price stability."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Miben különbözik a 'maginfláció' a főmutatóként közzétett fogyasztói árindextől?", ["Kiszűri a hektikusan ingadozó élelmiszer- és energiaárak közvetlen hatását, feltárva a fundamentális trendeket.", "Csak az arany és ezüst árát vizsgálja.", "Kizárólag a külföldi termékek drágulását méri."], 0, ["c1-13-vocab"]),
                fb("grammar", "controlled", "A jegybank legfőbb kihívása az inflációs várakózások tartós _____ volt az ár-bér spirál elkerülése végett. (anchoring / lehorgonyzása)", "lehorgonyzása", "The central bank's greatest challenge was the durable anchoring of inflation expectations to avoid a price-wage spiral.", ["c1-inflationary-expectations"]),
                match("vocabulary", "controlled", [["maginfláció", "core inflation"], ["ár-bér spirál", "price-wage spiral"], ["dezinfláció", "disinflation"], ["költségoldali sokk", "cost-push shock"]], ["c1-13-vocab"]),
                fb("grammar", "practice", "A vállalatok agresszív év eleji _____ jelentős mértékben késleltette az infláció mérséklődését. (repricing / átárazása)", "átárazása", "The aggressive early-year repricing by enterprises significantly delayed the easing of inflation.", ["c1-inflationary-expectations"]),
                sb("grammar", "practice", ["A", "dezinfláció", "ütemét", "a", "nyersanyagárak", "csökkenése", "is", "érdemben", "támogatta."], ["A", "dezinfláció", "ütemét", "a", "nyersanyagárak", "csökkenése", "is", "érdemben", "támogatta."], "The pace of disinflation was also substantially supported by falling commodity prices.", ["c1-inflationary-expectations"]),
                dc("dialogue", [
                    {"speaker": "Elemző", "text": "Fennáll-e még a veszélye egy újabb inflációs hullámnak?"},
                    {"speaker": "Közgazdász", "text": "Amennyiben a bérnövekedés üteme elszakad a termelékenységtől, kialakulhat az _____ spirál."},
                ], ["ár-bér", "kamat", "adó"], 0, ["c1-inflationary-expectations"]),
                sw("production", [{"prompt": "Explain the concept of core inflation in analytical prose.", "answer": "A maginfláció mutatója a szezonális és volatilis tételek kiszűrésével képet ad a gazdaság belső, fundamentális árdinamikájáról, segítve a jegybanki kamatdöntések megalapozását."}], ["c1-inflationary-expectations"]),
                mc("grammar", "check", "Mit jelent a dezinfláció a gazdasági nyelvben?", [
                    "Az infláció rátájának lassulását és az áremelkedési ütem mérséklődését.",
                    "Az árak általános és folyamatos csökkenését (deflációt).",
                    "A pénzforgalom azonnali leállását."
                ], 0, ["c1-inflationary-expectations"])
            ]
        },
        {
            "num": 5,
            "stem": "c1-13-05",
            "title": "Structural Growth Models & János Kornai's Economics of Shortage",
            "grammar_title": "Soft Budget Constraints, Dual Dependence and Systemic Macroeconomics",
            "grammar_skill": "c1-growth-model-synthesis",
            "goals": [
                "I can analyze János Kornai's foundational theories (*puha költségvetési korlát, hiánygazdaság, bürokratikus koordináció*).",
                "I can evaluate balance of payments and external equilibrium (*fizetési mérleg, külső egyensúly*).",
                "I can synthesize macro-structural transitions from central planning to market economics in academic Hungarian."
            ],
            "vocab": [
                {"lemma": "puha költségvetési korlát", "translation": "soft budget constraint (Kornai)", "pos": "expression"},
                {"lemma": "hiánygazdaság", "translation": "economics of shortage", "pos": "noun"},
                {"lemma": "fizetési mérleg", "translation": "balance of payments", "pos": "noun"},
                {"lemma": "külső egyensúly", "translation": "external equilibrium", "pos": "noun"},
                {"lemma": "bürokratikus koordináció", "translation": "bureaucratic coordination", "pos": "expression"},
                {"lemma": "kényszermegtakarítás", "translation": "forced saving", "pos": "noun"},
                {"lemma": "allokációs hatékonyság", "translation": "allocative efficiency", "pos": "noun"},
                {"lemma": "átmeneti gazdaság", "translation": "transition economy", "pos": "noun"}
            ],
            "gr_text1": "János Kornai (1928–2021) transformed modern macroeconomics with *A hiány* (1980), demonstrating that chronic shortages in socialist economies stem from systemic institutional flaws—most notably the *puha költségvetési korlát* (soft budget constraint), where enterprises are perpetually bailed out by the state.",
            "gr_text2": "Syntactically, academic economic discourse operates with nominalized systemic abstractions: `A puha költségvetési korlát intézményesülése kiiktatja a csőd kockázatát, felszámolva a vállalati önmérsékletet és az allokációs hatékonyságot`.",
            "gr_table": [
                ["A puha költségvetési korlát megszünteti a vállalati pénzügyi fegyelmet.", "The soft budget constraint eliminates corporate financial discipline."],
                ["A hiány nem véletlen zavar, hanem a szocialista rendszer immanens sajátossága.", "Shortage is not an accidental glitch, but an immanent attribute of the socialist system."],
                ["A külső egyensúly és a folyó fizetési mérleg stabilitása elengedhetetlen.", "External equilibrium and current account stability are essential."]
            ],
            "classic_story": {
                "slug": "c1-13-kornai",
                "author": "Kornai János",
                "work": "A hiány (1980)",
                "title": "A puha költségvetési korlát és a hiánygazdaság anatómiája",
                "summary": "János Kornai's monumental economic treatise dissecting systemic shortages, paternalistic state bailouts, and the soft budget constraint in centrally planned economies.",
                "characters": ["Kornai János"],
                "paragraphs": [
                    {"type": "narration", "text": "1980-ban látott napvilágot a magyar közgazdaságtudomány világirodalmi rangú alapműve, Kornai János A hiány című könyve. Kornai elvetette azt a hivatalos dogmát, miszerint a szocialista gazdaságban tapasztalható krónikus áruhiány, a sorban állás és a minőségi deficit csupán a tervezés átmeneti botlásaiból fakadna."},
                    {"type": "narration", "text": "Zseniális rendszertani elemzéssel bizonyította be: a hiány a szocialista gazdasági mechanizmus immanens, törvényszerű következménye. A jelenség gyökere a 'puha költségvetési korlát': míg a kapitalista piacgazdaságban a vállalat pénzügyi felelősséggel tartozik, és veszteség esetén a csőd fenyegeti (kemény költségvetési korlát), addig a szocialista állam atyáskodó módon mindig kisegíti, megmenti és szubvencionálja a veszteséges gyárakat."},
                    {"type": "narration", "text": "Ennek következtében a vállalatok beruházási éhsége csillapíthatatlan: anélkül halmoznak fel nyersanyagot, gépeket és munkaerőt, hogy a tényleges piaci megtérüléssel törődnének. A szívó hatás kiszárítja a gazdaságot, és a termelési javak szűkössége menthetetlenül átgyűrűzik a lakossági fogyasztásba. A hiány nem piaci zavar, hanem a paternalista bürokratikus koordináció közvetlen terméke."},
                    {"type": "narration", "text": "Kornai elmélete nemcsak a szocializmus működésképtelenségét világította meg, hanem máig érvényes etalont adott a világ közgazdászainak: emlékeztet rá, hogy a gazdasági hatékonyság legfőbb záloga a felelősség, a kemény költségvetési fegyelem és a piaci verseny szabadsága."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Mi a lényege Kornai 'puha költségvetési korlát' (soft budget constraint) elméletének?", ["Az állam automatikusan megmenti a veszteséges vállalatokat, ami felelőtlen gazdálkodáshoz és krónikus hiányhoz vezet.", "A költségvetést papír helyett puha füzetbe írják.", "A bankok ingyen osztanak pénzt a polgároknak."], 0, ["c1-13-vocab"]),
                fb("grammar", "controlled", "Kornai szerint a szocialista vállalatok csillapíthatatlan beruházási éhsége a kemény költségvetési korlát _____ fakadt. (absence / hiányából)", "hiányából", "According to Kornai, the insatiable investment hunger of socialist enterprises stemmed from the absence of a hard budget constraint.", ["c1-growth-model-synthesis"]),
                match("vocabulary", "controlled", [["puha költségvetési korlát", "állami kisegítés miatti felelőtlenség"], ["hiánygazdaság", "krónikus áruhiányon alapuló rendszer"], ["bürokratikus koordináció", "központi tervezői irányítás"], ["fizetési mérleg", "nemzetközi tranzakciók összessége"]], ["c1-13-vocab"]),
                mc("reading", "practice", "Miért tekintette Kornai a hiányt immanens rendszerhibának?", [
                    "Mert a paternalista állami kimentés kiiktatja a csőd kockázatát, így a vállalatok korlátlanul halmozzák fel az erőforrásokat.",
                    "Mert kevés volt a fa a papírgyártáshoz.",
                    "Mert a lakosság túl sokat utazott külföldre."
                ], 0, None),
                sb("grammar", "practice", ["A", "puha", "költségvetési", "korlát", "felszámolása", "a", "piaci", "átmenet", "alapfeltétele", "volt."], ["A", "puha", "költségvetési", "korlát", "felszámolása", "a", "piaci", "átmenet", "alapfeltétele", "volt."], "Eliminating the soft budget constraint was the prerequisite of market transition.", ["c1-growth-model-synthesis"]),
                sw("production", [{"prompt": "Summarize János Kornai's analysis of the soft budget constraint.", "answer": "Kornai kimutatta, hogy ha a vállalatokat az állam felmenti a csőd kockázata alól, megszakad a pénzügyi fegyelem, ami csillapíthatatlan erőforrás-felhalmozáshoz és krónikus hiánygazdasághoz vezet."}], ["c1-growth-model-synthesis"]),
                mc("grammar", "check", "Milyen hatással van a puha költségvetési korlát az allokációs hatékonyságra?", [
                    "Drasztikusan rontja, mivel a források nem a versenyképes, hanem a politikai alkukban erős szereplőkhöz vándorolnak.",
                    "Javítja a hatékonyságot, mert senki sem megy tönkre.",
                    "Nincs rá semmilyen hatással."
                ], 0, ["c1-growth-model-synthesis"])
            ]
        }
    ]

    for l in core_lessons:
        emit_instructional_lesson(13, "core", l, core_title, core_intro if l["num"] == 1 else None)

    # Core Consolidation
    emit_consolidation_lesson(
        13,
        "core",
        "c1-13-consolidation",
        core_title,
        [
            "I can formulate quantitative macroeconomic trend relations and metric analyses.",
            "I can evaluate central bank forward guidance, interest rate corridors, and transmission channels.",
            "I can navigate fiscal debt-to-GDP dynamics, inflation modeling, and Kornai's soft budget constraint."
        ],
        [
            mc("grammar", "recognize", "Melyik mondat alkalmazza a legválasztékosabb gazdasági összehasonlítást?", [
                "A kibocsátás az elemzői konszenzust felülmúlva érdemi bővülést mutatott.",
                "A kibocsátás jobb lett mint a konszenzus mondta.",
                "Sokkal több lett a termelés a vártnál."
            ], 0, ["c1-macroeconomic-indicators"]),
            mc("grammar", "recognize", "Mi a jegybanki kamattranszmisszió végső célja?", [
                "Az alapkamat változásának átgyűrűzése a banki hitelkamatokba és a megtakarítási hajlandóságba az árstabilitás elérése végett.",
                "A bankok nyereségének maximalizálása.",
                "A külföldi devizák azonnali betiltása."
            ], 0, ["c1-monetary-tightening-clauses"]),
            match("vocabulary", "recognize", [["bruttó hazai termék", "GDP"], ["irányadó kamat", "benchmark rate"], ["elsődleges egyenleg", "primary budget balance"], ["maginfláció", "core inflation"], ["puha költségvetési korlát", "soft budget constraint"]], ["c1-13-vocab"]),
            fb("vocabulary", "recall", "A bázishatás kiszűrésével a gazdasági növekedés kiegyensúlyozottabb képet _____. (mutat / mutatott)", "mutatott", "Filtering out the base effect, economic growth presented a more balanced picture.", ["c1-13-vocab"]),
            fb("vocabulary", "recall", "A tartós államháztartási hiány veszélyezteti az adósságpálya _____. (sustainability / fenntarthatóságát)", "fenntarthatóságát", "Persistent fiscal deficits endanger the sustainability of the debt trajectory.", ["c1-13-vocab"]),
            fb("grammar", "recall", "A Monetáris Tanács az előretekintő _____ óvatos és adatvezérelt döntéshozatalt hirdetett. (guidance / iránymutatásban)", "iránymutatásban", "In its forward guidance the Monetary Council proclaimed cautious and data-driven decision-making.", ["c1-monetary-tightening-clauses"]),
            fb("grammar", "context", "Az ár-bér spirál megelőzése érdekében elengedhetetlen az inflációs várakozások _____. (anchoring / lehorgonyzása)", "lehorgonyzása", "In order to prevent a price-wage spiral, the anchoring of inflation expectations is essential.", ["c1-inflationary-expectations"]),
            fb("grammar", "context", "Kornai rámutatott: a puha költségvetési korlát kiiktatja a vállalatok pénzügyi _____ és a csőd fenyegetését. (discipline / fegyelmét)", "fegyelmét", "Kornai pointed out: the soft budget constraint eliminates enterprises' financial discipline and threat of bankruptcy.", ["c1-growth-model-synthesis"]),
            mc("grammar", "context", "Hogyan járul hozzá a fiskális fegyelem a monetáris politika sikeréhez?", [
                "Csökkenti az aggregált keresleti nyomást, így megkönnyíti a jegybank számára az infláció letörését.",
                "Megtiltja a pénzhasználatot a gazdaságban.",
                "Kötelezővé teszi a nulla százalékos kamatot."
            ], 0, ["c1-fiscal-counterbalancing"]),
            sb("grammar", "produce", ["A", "külső", "egyensúly", "helyreállítása", "alapfeltétele", "a", "tartós", "makrogazdasági", "stabilitásnak."], ["A", "külső", "egyensúly", "helyreállítása", "alapfeltétele", "a", "tartós", "makrogazdasági", "stabilitásnak."], "Restoring external equilibrium is the prerequisite of lasting macroeconomic stability.", ["c1-growth-model-synthesis"]),
            sw("production", [{"prompt": "Write an analytical summary on the relationship between fiscal consolidation and sovereign risk.", "answer": "A hiteles fiskális konszolidáció nem csupán az államadósság-ráta csökkenését biztosítja, hanem mérsékli az ország kockázati prémiumát és a kamatterheket, tágítva a fenntartható gazdaságpolitika mozgásterét."}], ["c1-fiscal-counterbalancing"]),
            sw("production", [{"prompt": "Synthesize János Kornai's enduring contribution to economic theory.", "answer": "Kornai János A hiány című művében bizonyította, hogy a szocializmus krónikus áruhiányát a paternalista állam által fenntartott puha költségvetési korlát okozza, amely kiöli a vállalatokból a felelősséget és a racionális gazdálkodást."}], ["c1-growth-model-synthesis"])
        ]
    )

    # ----------------------------------------------------
    # TRACK 2: DISCOURSE (c1-monetaris)
    # ----------------------------------------------------
    slug = "monetaris"
    disc_intro = [
        "From the hyperinflation of the Pengő in 1945–46 to the 1995 Bokros Package, the transition to floating exchange rate bands, and the enduring debate over Euro adoption, Hungary's monetary history reflects a continuous struggle between sovereignty, exchange rate stability, and macroeconomic discipline.",
        "In this serialized Discourse track, explore the history and contemporary dilemmas of Hungarian monetary policy: the birth of the Forint, the mechanics of speculative attacks and FX debtor crises, the Maastricht convergence criteria, and whether Eurozone entry serves Hungarian long-term prosperity."
    ]

    disc_lessons = [
        {
            "num": 1,
            "stem": f"c1-{slug}-01",
            "title": "Hyperinflation to Stabilization: The 1946 Birth of the Forint",
            "grammar_title": "Historical Monetary Stabilizations and Currency Substitution",
            "grammar_skill": "c1-macroeconomic-indicators",
            "goals": [
                "I can analyze the 1945–1946 Hungarian hyperinflation—the highest ever recorded in world history.",
                "I can evaluate the stabilization package that introduced the modern Forint on August 1, 1946.",
                "I can formulate currency replacement and monetary credibility narratives in formal Hungarian."
            ],
            "vocab": [
                {"lemma": "hiperinfláció", "translation": "hyperinflation", "pos": "noun"},
                {"lemma": "valutareform", "translation": "currency reform", "pos": "noun"},
                {"lemma": "pengő", "translation": "Pengő (former Hungarian currency until 1946)", "pos": "noun"},
                {"lemma": "aranyfedezet", "translation": "gold backing / gold reserves", "pos": "noun"},
                {"lemma": "pénzromlás", "translation": "currency depreciation, degradation of money", "pos": "noun"},
                {"lemma": "stabilizációs program", "translation": "stabilization program", "pos": "noun"},
                {"lemma": "kibocsátás", "translation": "issuance, emission (currency)", "pos": "noun"},
                {"lemma": "értékmegőrzés", "translation": "preservation of value", "pos": "noun"}
            ],
            "gr_text1": "Following World War II, Hungary suffered the most extreme hyperinflation in recorded history: prices doubled every 15 hours, culminating in the 100-quintillion Pengő banknote. On August 1, 1946, the Forint was introduced at an astronomical exchange rate of 1 Forint = 400 octillion (4x10^29) Pengő.",
            "gr_text2": "Syntactically, monetary history deploys causal fronting and resultative passive constructions: `A jegybank aranytartalékának visszaszolgáltatását követően a forint szilárd aranyfedezettel debütálhatott`.",
            "gr_table": [
                ["A pengő hiperinflációja a világtörténelem legsúlyosabb pénzromlása volt.", "The hyperinflation of the pengő was the gravest currency collapse in world history."],
                ["Az aranytartalék visszaszerzése biztosította a forint kezdeti hitelét.", "Retrieval of the gold reserves secured initial credibility for the forint."],
                ["A valutareform sikeresen állította helyre a lakosság bizalmát.", "The currency reform successfully restored public confidence."]
            ],
            "world_story_seg": {
                "seg_slug": "pengo",
                "title": "A csillagászati számoktól a stabil valutáig: A forint születése",
                "summary": "How Hungary emerged from the world's most catastrophic hyperinflation through the disciplined monetary stabilization of August 1946.",
                "paragraphs": [
                    {"type": "narration", "text": "1946 nyarán a budapesti utcákat ellepték az eldobált pengőbankjók. A háborús pusztítás, a szovjet jóvátételi terhek és a fedezetlen pénznyomtatás a világtörténelem legsúlyosabb hiperinflációjához vezetett: az árak tizenöt óránként megduplázódtak, a bankjegyek címletei a csillagászati trilliók és billiárdok világába léptek át. A pénz elveszítette minden funkcióját; az emberek cigarettával és tojással fizettek egymásnak."},
                    {"type": "narration", "text": "1946. augusztus 1-jén a kormány radikális stabilizációs programot hajtott végre: megjelent a forint. A stabilitást az amerikai hadsereg által visszaszolgáltatott harminc tonnányi jegybanki aranytartalék alapozta meg. Az új fizetőeszköz kíméletlen bér- és árplafont kapott, de sikeresen megfékezte az összeomlást. A forint megszületése bebizonyította, hogy a pénz értéke nem a papírban, hanem az intézményi hitelességben és a fegyelmezett kibocsátásban rejlik."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Milyen történelmi világrekordot tart az 1946-os magyar pengő hiperinflációja?", ["A világtörténelem valaha mért legmagasabb havi áremelkedési ütemét.", "A legszebb bankjegygrafikát.", "A leghosszabb ideig tartó devizastabilitást."], 0, ["c1-monetaris-vocab"]),
                fb("grammar", "controlled", "A forint 1946. augusztusi kibocsátása sikeresen állította meg a pengő katasztrofális _____. (currency collapse / pénzromlását)", "pénzromlását", "The issuance of the forint in August 1946 successfully halted the catastrophic currency collapse of the pengő.", ["c1-macroeconomic-indicators"]),
                match("vocabulary", "controlled", [["hiperinfláció", "szélsőséges áremelkedési hullám"], ["valutareform", "új pénz bevezetése"], ["aranyfedezet", "nemesfém alapú garancia"], ["stabilizációs program", "egyensúlyteremtő intézkedéscsomag"]], ["c1-monetaris-vocab"]),
                fb("grammar", "practice", "A forint kezdeti hitelességét a visszaszerzett harminc tonna nemzeti _____ garantálta. (gold reserve / aranytartalék)", "aranytartalék", "The initial credibility of the forint was guaranteed by the retrieved thirty tons of national gold reserve.", ["c1-macroeconomic-indicators"]),
                sb("grammar", "practice", ["A", "valutareform", "sikere", "megteremtette", "a", "háború", "utáni", "újjáépítés", "pénzügyi", "alapjait."], ["A", "valutareform", "sikere", "megteremtette", "a", "háború", "utáni", "újjáépítés", "pénzügyi", "alapjait."], "The success of currency reform created the financial foundations of post-war reconstruction.", ["c1-macroeconomic-indicators"]),
                dc("dialogue", [
                    {"speaker": "Történész", "text": "Hogyan sikerült egyetlen nap alatt megállítani az elszabadult hiperinflációt?"},
                    {"speaker": "Gazdaságtörténész", "text": "A szigorú bérplafon és a valós _____ megléte visszaadta a pénzbe vetett hitet."},
                ], ["aranyfedezet", "ígéret", "adócsökkentés"], 0, ["c1-macroeconomic-indicators"]),
                sw("production", [{"prompt": "Write a sentence reflecting on the lesson of the 1946 monetary stabilization.", "answer": "Az 1946-os valutareform máig ható tanulsága, hogy a monetáris stabilitás valódi záloga a fedezetlen pénzkibocsátás tilalma és az intézményi hitelesség megőrzése."}], ["c1-macroeconomic-indicators"]),
                mc("grammar", "check", "Miért volt elengedhetetlen a radikális bér- és árplafon a forint bevezetésekor?", [
                    "Hogy elejét vegyék az új fizetőeszköz azonnali másodlagos elértéktelenedésének.",
                    "Hogy megszüntessék a bolti vásárlásokat.",
                    "Hogy mindenki azonos fizetést kapjon országszerte."
                ], 0, ["c1-macroeconomic-indicators"])
            ]
        },
        {
            "num": 2,
            "stem": f"c1-{slug}-02",
            "title": "The 1995 Bokros Package & The Crawling Peg Regime",
            "grammar_title": "Devaluation Dynamics, Crawling Peg and External Balance Restoration",
            "grammar_skill": "c1-fiscal-counterbalancing",
            "goals": [
                "I can analyze the 1995 Bokros Package (*Bokros-csomag, kiigazítás, ikerdeficit*).",
                "I can evaluate the crawling peg exchange rate system (*csúszó leértékelés*).",
                "I can discuss twin deficits and structural macroeconomic stabilization."
            ],
            "vocab": [
                {"lemma": "Bokros-csomag", "translation": "Bokros Package (1995 austerity and stabilization program)", "pos": "noun"},
                {"lemma": "ikerdeficit", "translation": "twin deficit (simultaneous budget and current account deficit)", "pos": "noun"},
                {"lemma": "csúszó leértékelés", "translation": "crawling peg (pre-announced exchange rate depreciation)", "pos": "expression"},
                {"lemma": "leértékelődés", "translation": "depreciation, devaluation", "pos": "noun"},
                {"lemma": "folyó fizetési mérleg", "translation": "current account balance", "pos": "noun"},
                {"lemma": "vámpótlék", "translation": "customs surcharge / import surcharge", "pos": "noun"},
                {"lemma": "reálbércsökkenés", "translation": "real wage decline", "pos": "noun"},
                {"lemma": "fizetésképtelenség elkerülése", "translation": "avoidance of insolvency / sovereign default", "pos": "expression"}
            ],
            "gr_text1": "In March 1995, facing severe 'ikerdeficit' (twin deficits) and insolvency, Finance Minister Lajos Bokros announced an emergency stabilization: an immediate 9% devaluation followed by a predictable 'csúszó leértékelés' (crawling peg), an 8% import surcharge, and severe public expenditure cuts.",
            "gr_text2": "Syntactically, texts contrast short-term social costs with medium-term competitiveness gains: `Bár a csomag 12%-os reálbércsökkenést okozott a lakosságnak, helyreállította az ország nemzetközi fizetőképességét és megalapozta a későbbi exportvezérelt növekedést`.",
            "gr_table": [
                ["A csúszó leértékelési rendszer kiszámíthatóvá tette az árfolyampályát.", "The crawling peg system made the exchange rate trajectory predictable."],
                ["A csomag elhárította a fenyegető államcsődöt és az ikerdeficitet.", "The package averted looming sovereign default and twin deficits."],
                ["A reálbérek drasztikus esése magas társadalmi áldozatokkal járt.", "The drastic drop in real wages came with high social costs."]
            ],
            "world_story_seg": {
                "seg_slug": "bokros",
                "title": "A szakadék széléről a stabilitásig: Az 1995-ös Bokros-csomag",
                "summary": "How the controversial 1995 Bokros Package rescued Hungary from looming default through painful austerity and a crawling peg regime.",
                "paragraphs": [
                    {"type": "narration", "text": "1995 elején Magyarország a gazdasági összeomlás szélén táncolt: a költségvetési hiány és a folyó fizetési mérleg hiánya (az ikerdeficit) elérte a GDP tíz százalékát, a külföldi befektetők bizalma elillant, és a fizetésképtelenség réme fenyegetett. Március 12-én Bokros Lajos pénzügyminiszter drasztikus stabilizációs csomagot jelentett be."},
                    {"type": "narration", "text": "A csomag azonnali forintleértékelést, importvám-pótlékot és csúszó leértékelési árfolyamrendszert vezetett be, miközben fájdalmasan megnyirbálta a szociális kiadásokat és a reálbéreket. A társadalmi felháborodás viharos volt, ám a lépések meghozták az eredményt: az ikerdeficit megszűnt, a devizatartalék felduzzadt, és Magyarország vonzóvá vált a működőtőke-befektetések számára. A stabilizáció megalapozta a kilencvenes évek végi gazdasági fellendülést, de máig tartó politikai traumát hagyott maga után."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Milyen makrogazdasági vészhelyzet hívta életre az 1995-ös Bokros-csomagot?", ["A fenyegető fizetésképtelenség és a fenntarthatatlan ikerdeficit (költségvetési és fizetési mérleg hiány).", "A túlzottan magas devizatartalék elköltése.", "A lakossági megtakarítások kötelező megduplázása."], 0, ["c1-monetaris-vocab"]),
                fb("grammar", "controlled", "A Bokros-csomag által bevezetett _____ leértékelés kiszámíthatóvá tette az árfolyammozgást az exportőrök számára. (crawling / csúszó)", "csúszó", "The crawling peg devaluation introduced by the Bokros Package made exchange rate movements predictable for exporters.", ["c1-fiscal-counterbalancing"]),
                match("vocabulary", "controlled", [["Bokros-csomag", "1995-ös stabilizációs program"], ["ikerdeficit", "költségvetési és külső hiány egyidejűsége"], ["csúszó leértékelés", "előre bejelentett árfolyampálya"], ["vámpótlék", "importot terhelő pótlólagos teher"]], ["c1-monetaris-vocab"]),
                fb("grammar", "practice", "Bár a stabilizáció helyreállította az egyensúlyt, a lakosság számára súlyos _____ járt. (real wage decline / reálbércsökkenéssel)", "reálbércsökkenéssel", "Although stabilization restored equilibrium, it brought severe real wage decline for the public.", ["c1-fiscal-counterbalancing"]),
                sb("grammar", "practice", ["A", "csúszó", "leértékelés", "rendszere", "letörte", "az", "árfolyam-spekuláció", "kockázatait."], ["A", "csúszó", "leértékelés", "rendszere", "letörte", "az", "árfolyam-spekuláció", "kockázatait."], "The crawling peg system broke the risks of exchange rate speculation.", ["c1-fiscal-counterbalancing"]),
                dc("dialogue", [
                    {"speaker": "Közgazdász", "text": "Hogyan tekint ma a szakma az 1995-ös stabilizációs intézkedésekre?"},
                    {"speaker": "Elemző", "text": "Gazdaságilag elkerülhetetlen és sikeres lépés volt, de súlyos _____ árat fizetett érte az ország."},
                ], ["társadalmi", "katonai", "jogi"], 0, ["c1-fiscal-counterbalancing"]),
                sw("production", [{"prompt": "Analyze the trade-off of the Bokros Package in one balanced evaluative sentence.", "answer": "Bár az 1995-ös Bokros-csomag drasztikus reálbércsökkenést és társadalmi megrázkódtatást okozott, sikeresen elhárította az államcsődöt és helyreállította az ország külső pénzügyi egyensúlyát."}], ["c1-fiscal-counterbalancing"]),
                mc("grammar", "check", "Mit jelent a gazdaságpolitikában az 'ikerdeficit' fogalma?", [
                    "A költségvetési hiány és a folyó fizetési mérleg hiányának párhuzamos fennállását.",
                    "A születési ráta és a GDP egyidejű csökkenését.",
                    "Két minisztérium azonos összegű adósságát."
                ], 0, ["c1-fiscal-counterbalancing"])
            ]
        },
        {
            "num": 3,
            "stem": f"c1-{slug}-03",
            "title": "Exchange Rate Bands, Speculative Attacks & Floating the Forint",
            "grammar_title": "Intervention Limits, Exchange Rate Fluctuation Bands and Speculative Runs",
            "grammar_skill": "c1-monetary-tightening-clauses",
            "goals": [
                "I can analyze exchange rate regimes (*intervenciós sáv, sávos lebegtetés, szabad lebegtetés*).",
                "I can evaluate speculative attacks (*spekulatív támadás a forint ellen 2003-ban*).",
                "I can describe central bank reserve interventions and market dynamics in C1 Hungarian."
            ],
            "vocab": [
                {"lemma": "ingadozási sáv", "translation": "fluctuation band (+/- 15% intervention band)", "pos": "noun"},
                {"lemma": "intervenció", "translation": "central bank currency intervention", "pos": "noun"},
                {"lemma": "spekulatív támadás", "translation": "speculative attack / currency run", "pos": "noun"},
                {"lemma": "szabad lebegtetés", "translation": "free floating exchange rate regime", "pos": "expression"},
                {"lemma": "erősödési sávszél", "translation": "strong edge of the intervention band", "pos": "noun"},
                {"lemma": "devizatartalék felélése", "translation": "depletion of foreign exchange reserves", "pos": "expression"},
                {"lemma": "kamatvágás", "translation": "interest rate cut", "pos": "noun"},
                {"lemma": "árfolyamkockázat", "translation": "exchange rate / currency risk", "pos": "noun"}
            ],
            "gr_text1": "Between 2001 and 2008, Hungary operated a +/-15% fluctuation band around the Forint/Euro parity. In January 2003, international hedge funds launched a massive speculative attack against the 'erősödési sávszél' (strong edge of the band), betting the central bank would be forced to widen or break the band.",
            "gr_text2": "Syntactically, texts formulate conditional market tensions: `A jegybank kénytelen volt több milliárd eurónyi forintot vásárolni, miközben drasztikus kamatvágással próbálta megfékezni a spekulációs tőkebeáramlást`.",
            "gr_table": [
                ["A jegybank az erősödési sávszélnél hajtott végre devizapiaci intervenciót.", "The central bank executed FX intervention at the strong edge of the band."],
                ["A 2008-as válság nyomán a sávos rendszert felváltotta a szabad lebegtetés.", "Following the 2008 crisis, the band system was replaced by free floating."],
                ["A spekulatív támadások rávilágítottak a rögzített sávok sérülékenységére.", "Speculative attacks highlighted the vulnerability of pegged bands."]
            ],
            "world_story_seg": {
                "seg_slug": "savszel",
                "title": "Harc a sávszélen: A 2003-as spekulatív támadás és a forint lebegtetése",
                "summary": "How hedge funds attacked the Forint's fluctuation band in 2003, and why Hungary ultimately transitioned to a fully floating currency in 2008.",
                "paragraphs": [
                    {"type": "narration", "text": "2003 januárjában a Magyar Nemzeti Bank történetének egyik legdrámaibb ostromát élte át. A forintot egy plusz-mínusz 15 százalékos intervenciós sáv rögzítette az euróhoz, ám a nemzetközi spekulánsok úgy vélték: a forint alulértékelt, és a jegybank nem lesz képes fenntartani a sávot. Órák alatt milliárdnyi eurónyi tőke zúdult be az országba, a forint az erősödési sávszélnek feszült, a bankárok telefonjai izzottak."},
                    {"type": "narration", "text": "Járai Zsigmond jegybankelnök gigantikus devizapiaci intervencióval vásárolta fel a beáramló eurót, miközben drasztikus kamatcsökkentést hajtott végre. A sáv megvédése sikerült, de a beavatkozás hatalmas likviditási feszültséget és veszteséget okozott. A 2008-as pénzügyi világválság küszöbén a döntéshozók belátták: a rögzített sáv tarthatatlan. 2008 februárjában a forintot szabadon lebegő valutává nyilvánították, rábízva árfolyamát a globális piac keresleti és kínálati erőire."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Miért támadták meg a spekulatív alapok a forint intervenciós sávját 2003 januárjában?", ["Mert a forint felértékelődésére spekulálva arra számítottak, hogy a jegybank eltörli vagy kiszélesíti a sávot.", "Mert tönkre akarták tenni a budapesti tőzsdét.", "Mert az euró bevezetését ünnepelték."], 0, ["c1-monetaris-vocab"]),
                fb("grammar", "controlled", "A jegybank a forint védelmében kénytelen volt az erősödési _____ hatalmas összegben intervenciót végrehajtani. (band edge / sávszélnél)", "sávszélnél", "In defense of the forint the central bank was forced to execute intervention in huge amounts at the strong band edge.", ["c1-monetary-tightening-clauses"]),
                match("vocabulary", "controlled", [["ingadozási sáv", "intervenciós határok"], ["spekulatív támadás", "árfolyam elmozdítására irányuló tőkeáramlás"], ["szabad lebegtetés", "piaci árfolyamrendszer"], ["devizatartalék", "jegybanki nemzetközi tartalék"]], ["c1-monetaris-vocab"]),
                fb("grammar", "practice", "2008 februárjában a forint rögzített sávját végleg felváltotta a szabad _____. (floating / lebegtetés)", "lebegtetés", "In February 2008 the pegged band of the forint was definitively replaced by free floating.", ["c1-monetary-tightening-clauses"]),
                sb("grammar", "practice", ["A", "szabad", "lebegtetés", "lehetővé", "teszi", "a", "monetáris", "politika", "teljes", "függetlenségét."], ["A", "szabad", "lebegtetés", "lehetővé", "teszi", "a", "monetáris", "politika", "teljes", "függetlenségét."], "Free floating enables full independence of monetary policy.", ["c1-monetary-tightening-clauses"]),
                dc("dialogue", [
                    {"speaker": "Kereskedő", "text": "Miért döntött a jegybank a lebegő árfolyamrendszer bevezetése mellett?"},
                    {"speaker": "Jegybankár", "text": "Mert a rögzített sávok állandó célpontot nyújtottak a nemzetközi spekuláció és a devizapiaci _____ számára."},
                ], ["támadások", "hitelek", "adók"], 0, ["c1-monetary-tightening-clauses"]),
                sw("production", [{"prompt": "Contrast pegged exchange rate bands with free floating regimes.", "answer": "Míg az intervenciós sáv kiszámíthatóságot nyújt, de sérülékeny a spekulatív támadásokkal szemben, addig a szabad lebegtetés automatikus sokkelnyelőként működik, megőrizve a jegybank függetlenségét."}], ["c1-monetary-tightening-clauses"]),
                mc("grammar", "check", "Hogyan működik a lebegő árfolyamrendszer mint makrogazdasági sokkelnyelő?", [
                    "A forint leértékelődése külső sokkok idején automatikusan javítja az export versenyképességét és mérsékli az importot.",
                    "Azonnal leállítja a külföldi pénzküldést.",
                    "Fixálja a benzin árát az egész országban."
                ], 0, ["c1-monetary-tightening-clauses"])
            ]
        },
        {
            "num": 4,
            "stem": f"c1-{slug}-04",
            "title": "The FX Debtor Crisis & Currency Risk Socialization",
            "grammar_title": "Foreign Currency Lending, Balance Sheet Mismatch and Legislative Settlements",
            "grammar_skill": "c1-inflationary-expectations",
            "goals": [
                "I can analyze the Swiss Franc retail mortgage crisis (*devizahitelezés, devizahitel-válság, forintosítás*).",
                "I can evaluate balance sheet mismatches and exchange rate pass-through to households.",
                "I can explain statutory settlement mechanisms (*Kúria jogegységi döntése, elszámolási törvény*) in formal Hungarian."
            ],
            "vocab": [
                {"lemma": "devizahitel", "translation": "foreign currency loan (Swiss Franc / Euro)", "pos": "noun"},
                {"lemma": "árfolyamrés", "translation": "exchange rate spread (buy-sell spread applied to loans)", "pos": "noun"},
                {"lemma": "egyoldalú szerződésmódosítás", "translation": "unilateral contract modification (by banks)", "pos": "expression"},
                {"lemma": "forintosítás", "translation": "conversion of FX loans into Forint mortgages", "pos": "noun"},
                {"lemma": "törlesztőrészlet", "translation": "loan installment / monthly repayment", "pos": "noun"},
                {"lemma": "jogegységi határozat", "translation": "uniformity decision (Curia supreme court)", "pos": "noun"},
                {"lemma": "tisztességtelen szerződési feltétel", "translation": "unfair contract term", "pos": "expression"},
                {"lemma": "adósságcsapda", "translation": "debt trap", "pos": "noun"}
            ],
            "gr_text1": "Between 2004 and 2008, hundreds of thousands of Hungarian households took out Swiss Franc mortgages due to lower nominal interest rates, ignoring currency risk. When the Forint depreciated from 150 to over 250 HUF/CHF during the global crisis, monthly installments doubled, creating a systemic socio-economic crisis.",
            "gr_text2": "The Curia ruled that banks' unilateral rate hikes and exchange rate spreads (*árfolyamrés*) were unfair contract terms (*tisztességtelen szerződési feltétel*), paving the way for the 2014 mandatory conversion to Forints (*forintosítás*).",
            "gr_table": [
                ["A svájci frank meglódulása megduplázta a háztartások törlesztőrészleteit.", "The surge of the Swiss Franc doubled household loan installments."],
                ["A Kúria jogegységi határozata tisztességtelennek nyilvánította az árfolyamrést.", "The Curia's uniformity decision declared the exchange rate spread unfair."],
                ["A devizahitelek forintosítása elhárította a rendszerszintű pénzügyi kockázatot.", "The conversion of FX loans into forints eliminated systemic financial risk."]
            ],
            "world_story_seg": {
                "seg_slug": "devizahitel",
                "title": "A svájci frank csapdájában: A devizahitel-válság és a forintosítás",
                "summary": "How retail foreign currency lending brought a million Hungarians to the brink of insolvency and how the state converted the loans into Forints.",
                "paragraphs": [
                    {"type": "narration", "text": "A kétezres évek közepén a svájci frank alapú hitel csábító ígéretnek tűnt: a magas forintkamatokkal szemben a frankhitelek alacsony törlesztőrészletet kínáltak lakásvásárlásra és autóhitelekre. Családok százezrei adósodtak el anélkül, hogy felmérték volna az árfolyamkockázat halálos veszélyét. Amikor a 2008-as világválság kirobbant, a forint mélyrepülésbe kezdett, a svájci frank pedig menedékvalutaként felértékelődött: a havi részletek a duplájára, triplájára ugrottak."},
                    {"type": "narration", "text": "A devizahitel-válság nemzeti tragédiává vált: elárverezett otthonok, széteső családok és a bedőlő banki portfóliók jellemezték a korszakot. Hosszas jogi csaták után a Kúria kimondta, hogy az árfolyamrés és az egyoldalú banki kamatemelések tisztességtelenek voltak. 2014 végén a parlament törvénybe iktatta a devizahitelek kötelező forintosítását: a lakossági hitelállományt piaci árfolyamon forintosították, megelőzve az újabb frankrobbanás katasztrófáját. A krízis örök mementó maradt a lakossági devizakockázat veszélyeiről."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Miért vált tömeges tragédiává a svájci frank alapú devizahitelezés Magyarországon?", ["Mert a forint gyengülésével a háztartások törlesztőrészletei drasztikusan megugrottak, miközben jövedelmük forintban maradt.", "Mert Svájcban betiltották a forint használatát.", "Mert a bankok bezárták fiókjaikat."], 0, ["c1-monetaris-vocab"]),
                fb("grammar", "controlled", "A Kúria jogegységi döntése kimondta, hogy a bankok által alkalmazott _____ tisztességtelen szerződési feltételnek minősül. (spread / árfolyamrés)", "árfolyamrés", "The Curia's uniformity decision declared that the exchange rate spread applied by banks constitutes an unfair contract term.", ["c1-inflationary-expectations"]),
                match("vocabulary", "controlled", [["devizahitel", "külföldi pénznemhez kötött kölcsön"], ["árfolyamrés", "eladási és vételi árfolyam különbsége"], ["forintosítás", "devizahitelek nemzeti valutára váltása"], ["törlesztőrészlet", "havi rendszeres hitelfizetés"]], ["c1-monetaris-vocab"]),
                fb("grammar", "practice", "A devizahitelek 2014-es _____ megóvta a lakosságot a svájci frank későbbi drasztikus erősödésétől. (conversion to forints / forintosítása)", "forintosítása", "The 2014 conversion of FX loans to forints shielded the public from the subsequent drastic appreciation of the Swiss Franc.", ["c1-inflationary-expectations"]),
                sb("grammar", "practice", ["A", "devizahitelek", "forintosítása", "megszüntette", "a", "háztartások", "árfolyamkockázatát."], ["A", "devizahitelek", "forintosítása", "megszüntette", "a", "háztartások", "árfolyamkockázatát."], "The conversion of FX loans to forints eliminated household exchange rate risk.", ["c1-inflationary-expectations"]),
                dc("dialogue", [
                    {"speaker": "Ügyfél", "text": "Hogyan ugorhatott meg a hitelem összege, amikor éveken át pontosan fizettem?"},
                    {"speaker": "Ügyvéd", "text": "Úgy, hogy a tőketartozást devizában tartották nyilván, így a forintgyengülés automatikusan megnövelte az _____ terheit."},
                ], ["adós", "állam", "építész"], 0, ["c1-inflationary-expectations"]),
                sw("production", [{"prompt": "Explain the systemic risk of retail FX lending in one analytical sentence.", "answer": "A lakossági devizahitelezés alapvető veszélye a devizális eltérésben (mismatch) rejlik: a háztartások forintban képződő jövedelme nem nyújt fedezetet a külső sokkok által kiváltott árfolyamgyengülés törlesztési terheire."}], ["c1-inflationary-expectations"]),
                mc("grammar", "check", "Mi volt a forintosítás jogi és gazdasági következménye?", [
                    "A lakossági jelzáloghitelek átváltása forintra, ami megszüntette a közvetlen devizakockázatot a családok számára.",
                    "A devizahitelek teljes és ingyenes elengedése.",
                    "Az összes bank államosítása."
                ], 0, ["c1-inflationary-expectations"])
            ]
        },
        {
            "num": 5,
            "stem": f"c1-{slug}-05",
            "title": "The Eurozone Dilemma: Sovereignty vs. Integration",
            "grammar_title": "Maastricht Convergence Criteria and Optimal Currency Area Theory",
            "grammar_skill": "c1-growth-model-synthesis",
            "goals": [
                "I can analyze the Maastricht convergence criteria (*maastrichti kritériumok, konvergenciaprogram, ERM-II*).",
                "I can evaluate the Optimal Currency Area (OCA) theory applied to Central Europe.",
                "I can synthesize the macro-debate between monetary sovereignty and Eurozone adoption in academic Hungarian."
            ],
            "vocab": [
                {"lemma": "maastrichti kritériumok", "translation": "Maastricht convergence criteria", "pos": "noun"},
                {"lemma": "eurózóna-csatlakozás", "translation": "Eurozone accession", "pos": "noun"},
                {"lemma": "monetáris szuverenitás", "translation": "monetary sovereignty", "pos": "noun"},
                {"lemma": "árfolyam-stabilitási mechanizmus", "translation": "Exchange Rate Mechanism II (ERM-II)", "pos": "noun"},
                {"lemma": "optimális valutaövezet", "translation": "optimal currency area (Mundell)", "pos": "expression"},
                {"lemma": "tranzakciós költség", "translation": "transaction cost", "pos": "noun"},
                {"lemma": "reálkonvergencia", "translation": "real convergence (living standards / productivity)", "pos": "noun"},
                {"lemma": "nominális konvergencia", "translation": "nominal convergence (inflation / fiscal metrics)", "pos": "noun"}
            ],
            "gr_text1": "The debate over introducing the Euro in Hungary balances monetary autonomy (*önálló monetáris politika és lebegő árfolyam sokkelnyelő szerepe*) against economic integration benefits (*tranzakciós költségek és devizakockázat eliminálása*).",
            "gr_text2": "Syntactically, texts contrast nominal criteria with real convergence: `Noha a nominális maastrichti kritériumok formailag teljesíthetők volnának, a közgazdászok többsége szerint az euró bevezetése csak a reálkonvergencia megfelelő szintje mellett indokolt`.",
            "gr_table": [
                ["A maastrichti kritériumok az árstabilitást és a fiskális fegyelmet vizsgálják.", "The Maastricht criteria examine price stability and fiscal discipline."],
                ["Az euró bevezetése megszünteti a devizaváltási tranzakciós költségeket.", "Adopting the Euro eliminates currency exchange transaction costs."],
                ["Az önálló monetáris politika feladása kockázatot rejt az aszimmetrikus sokkok idején.", "Surrendering independent monetary policy entails risk during asymmetric shocks."]
            ],
            "world_story_seg": {
                "seg_slug": "eurodilemma",
                "title": "A forint vagy az euró: A nemzeti szuverenitás és a gazdasági integráció dilemmája",
                "summary": "The enduring economic and political debate over whether Hungary should join the Eurozone or retain the independent Forint.",
                "paragraphs": [
                    {"type": "narration", "text": "Húsz évvel az Európai Unióhoz való csatlakozás után a forint sorsa továbbra is a magyar gazdaságpolitika legvitatottabb kérdése. Az euró bevezetésének pártolói a nemzetközi integráció előnyeit hangsúlyozzák: az eurózóna tagjaként megszűnnének a drága tranzakciós költségek és a devizaárfolyam-ingadozás kockázatai, csökkenne a vállalati kamatfelár, és Magyarország beülhetne a frankfurti Európai Központi Bank döntéshozó asztalához."},
                    {"type": "narration", "text": "A szuverenitás hívei ezzel szemben Robert Mundell optimális valutaövezeti elméletére hivatkoznak: ha egy ország lemond önálló valutájáról, feladja a jegybanki kamatpolitika és a lebegő árfolyam rugalmas fegyverét. Aszimmetrikus gazdasági sokkok idején a forint leértékelődése védi a hazai ipart és munkahelyeket. A többségi szakmai konszenzus szerint az euró bevezetése nem politikai presztízskérdés, hanem érettségi vizsga: csak akkor szabad belépni, ha a magyar gazdaság termelékenysége és reálkonvergenciája eléri az európai magországok szintjét."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Mi a fő különbség a 'nominális' és a 'reálkonvergencia' között az eurócsatlakozás vitájában?", ["A nominális az inflációs és költségvetési mutatószámokra, míg a reálkonvergencia a fejlettségi és termelékenységi szintre vonatkozik.", "A nominális a bankjegyek méretére utal.", "Nincs különbség, a két szó azonos fogalmat takar."], 0, ["c1-monetaris-vocab"]),
                fb("grammar", "controlled", "Az euró bevezetésének előszobája az _____ mechanizmusban (ERM-II) való kétéves részvétel. (exchange rate stability / árfolyam-stabilitási)", "árfolyam-stabilitási", "The anteroom of Euro adoption is two years' participation in the exchange rate stability mechanism (ERM-II).", ["c1-growth-model-synthesis"]),
                match("vocabulary", "controlled", [["maastrichti kritériumok", "nominális konvergencia feltételei"], ["monetáris szuverenitás", "önálló jegybanki kamatpolitika"], ["tranzakciós költség", "devizaváltási kiadás"], ["reálkonvergencia", "gazdasági fejlettség felzárkózása"]], ["c1-monetaris-vocab"]),
                fb("grammar", "practice", "Az önálló monetáris politika feladása megfosztja a gazdaságot a lebegő árfolyam mint automatikus sokkelnyelő _____ lehetőségétől. (function / funkciójának)", "funkciójának", "Surrendering independent monetary policy deprives the economy of the possibility of floating exchange rate as an automatic shock absorber function.", ["c1-growth-model-synthesis"]),
                sb("grammar", "practice", ["A", "gazdasági", "felzárkózás", "nélkül", "az", "euró", "bevezetése", "súlyos", "kockázatokkal", "járhat."], ["A", "gazdasági", "felzárkózás", "nélkül", "az", "euró", "bevezetése", "súlyos", "kockázatokkal", "járhat."], "Without economic catch-up adopting the Euro may entail severe risks.", ["c1-growth-model-synthesis"]),
                dc("dialogue", [
                    {"speaker": "Politikus", "text": "Mikor célszerű bevezetni a közös európai valutát Magyarországon?"},
                    {"speaker": "Közgazdász", "text": "Amikor a magyar termelékenység és a _____ eléri a magországok szintjét."},
                ], ["reálkonvergencia", "haderő", "árfolyamrés"], 0, ["c1-growth-model-synthesis"]),
                sw("production", [{"prompt": "Formulate the core dilemma of Eurozone accession in academic Hungarian.", "answer": "Az eurózóna-csatlakozás alapvető dilemmája a tranzakciós költségek kiküszöböléséből fakadó integrációs haszon és az önálló monetáris sokkelnyelő képesség feladásából eredő makrogazdasági kockázat mérlegelése."}], ["c1-growth-model-synthesis"]),
                mc("grammar", "check", "Mi az optimális valutaövezet (Optimal Currency Area) elméletének lényege?", [
                    "Hogy a közös valuta csak olyan régiókban működik hatékonyan, ahol magas a munkaerő és tőke mobilitása a sokkok kiegyenlítésére.",
                    "Hogy minden kontinensnek pontosan egy pénznemmel kell rendelkeznie.",
                    "Hogy a pénznyomtatás költségeit minimalizálni kell."
                ], 0, ["c1-growth-model-synthesis"])
            ]
        }
    ]

    for l in disc_lessons:
        emit_instructional_lesson(13, "discourse", l, disc_title, disc_intro if l["num"] == 1 else None)

    # Combined Discourse World Story
    write_json(
        f"stories/world/c1/c1-{slug}.json",
        {
            "id": f"story.c1.{slug}",
            "title": "A forint regénye: Pénzromlás, stabilizáció és monetáris szuverenitás",
            "level": "C1",
            "type": "world",
            "order": 13,
            "lesson": 5,
            "estimatedMinutes": 8,
            "summary": "Panoramic chronicle of Hungarian monetary history: the 1946 hyperinflation and birth of the Forint, the 1995 Bokros Package and crawling peg regime, speculative attacks on currency bands, the devastating retail FX mortgage crisis, and the ongoing Eurozone accession debate.",
            "grammar": [
                "c1-macroeconomic-indicators",
                "c1-monetary-tightening-clauses",
                "c1-fiscal-counterbalancing",
                "c1-inflationary-expectations",
                "c1-growth-model-synthesis"
            ],
            "vocabularyTopics": [
                "Monetary Sovereignty, the Forint & the Eurozone Dilemma",
                "Hyperinflation to Stabilization: The 1946 Birth of the Forint",
                "The 1995 Bokros Package & The Crawling Peg Regime",
                "Exchange Rate Bands, Speculative Attacks & Floating the Forint",
                "The FX Debtor Crisis & Currency Risk Socialization",
                "The Eurozone Dilemma: Sovereignty vs. Integration"
            ],
            "paragraphs": [
                {"type": "narration", "text": "A magyar pénztörténet a rendkívüli végletek és küzdelmek krónikája. 1946-ban Magyarország a világtörténelem legsúlyosabb hiperinflációjának hamvaiból támasztotta fel a forintot, megalapozva a háború utáni újjáépítést az amerikaiak által visszaszolgáltatott harminc tonnányi nemzeti aranytartalék segítségével."},
                {"type": "narration", "text": "A rendszerváltás viharos évei után, 1995-ben a fenyegető fizetésképtelenséget és az ikerdeficitet az elhíresült Bokros-csomag hárította el, bevezetve a csúszó leértékelés kiszámítható rendszerét a magas társadalmi áldozatok árán."},
                {"type": "narration", "text": "A kétezres évek a devizapiaci liberalizációról szóltak: a spekulatív alapok 2003-as sávszéli ostroma után a jegybank 2008-ban végleg a szabad lebegtetés útjára léptette a valutát."},
                {"type": "narration", "text": "Ezzel párhuzamosan azonban a felelőtlen lakossági svájci frank hitelezés súlyos devizahitel-válságba torkollott, amelyet csak a 2014-es kötelező forintosítás tudott felszámolni."},
                {"type": "narration", "text": "Napjainkban a forint és az euró vitája a nemzeti monetáris szuverenitás és a mély európai gazdasági integráció örök dilemmáját testesíti meg: emlékeztetve arra, hogy a stabil fizetőeszköz nem csupán technikai kérdés, hanem a gazdasági felelősség és a társadalmi bizalom legmélyebb tükre."}
            ]
        }
    )

    # Discourse Consolidation
    emit_consolidation_lesson(
        13,
        "discourse",
        f"c1-{slug}-consolidation",
        disc_title,
        [
            "I can navigate the history of the 1946 hyperinflation, gold backing, and the birth of the Forint.",
            "I can analyze the 1995 Bokros Package, crawling peg regimes, and speculative currency attacks.",
            "I can evaluate the retail FX debtor crisis, statutory forint conversion, and the Eurozone adoption dilemma."
        ],
        [
            mc("grammar", "recognize", "Miért tekinthető történelmi sikernek a forint 1946-os bevezetése?", [
                "Mert a visszaszerzett aranytartalékra építve megállította a világtörténelem legsúlyosabb hiperinflációját.",
                "Mert ingyenessé tette a közlekedést.",
                "Mert megegyezett az amerikai dollárral."
            ], 0, ["c1-macroeconomic-indicators"]),
            mc("grammar", "recognize", "Mi volt az 1995-ös csúszó leértékelés (crawling peg) legfőbb gazdasági előnye?", [
                "Kiszámíthatóvá tette az árfolyam pályáját az exportőrök számára és felszámolta a leértékelési spekulációt.",
                "Azonnal megduplázta a reálbéreket.",
                "Eltörölte a vámokat."
            ], 0, ["c1-fiscal-counterbalancing"]),
            match("vocabulary", "recognize", [["pengő", "hiperinflációs valuta"], ["Bokros-csomag", "1995-ös stabilizáció"], ["spekulatív támadás", "sávszéli roham 2003-ban"], ["forintosítás", "devizahitelek átváltása"], ["ERM-II", "euró előszoba árfolyammechanizmus"]], ["c1-monetaris-vocab"]),
            fb("vocabulary", "recall", "A devizahitelek kötelező _____ megszüntette a lakosság közvetlen árfolyamkockázatát. (conversion to forints / forintosítása)", "forintosítása", "The mandatory conversion of FX loans into forints eliminated households' direct currency risk.", ["c1-monetaris-vocab"]),
            fb("vocabulary", "recall", "Az eurózóna tagság feltétele a nominális konvergenciát rögzítő _____ kritériumok teljesítése. (Maastricht / maastrichti)", "maastrichti", "The condition of Eurozone membership is fulfilling the Maastricht criteria setting nominal convergence.", ["c1-monetaris-vocab"]),
            fb("grammar", "recall", "A forint 1946. augusztusi kibocsátása sikeresen megfékezte a pengő katasztrofális _____. (depreciation / pénzromlását)", "pénzromlását", "The issuance of the forint in August 1946 successfully halted the catastrophic depreciation of the pengő.", ["c1-macroeconomic-indicators"]),
            fb("grammar", "context", "A sávos árfolyamrendszer 2008-as felszámolásával Magyarország áttért a szabad _____. (floating / lebegtetésre)", "lebegtetésre", "With the elimination of the band system in 2008 Hungary transitioned to free floating.", ["c1-monetary-tightening-clauses"]),
            fb("grammar", "context", "A közgazdászok szerint az euró bevezetése csak a gazdasági _____ megfelelő foka esetén jár nettó haszonnal. (real convergence / reálkonvergencia)", "reálkonvergencia", "According to economists adopting the Euro brings net benefits only in case of an adequate degree of real convergence.", ["c1-growth-model-synthesis"]),
            mc("grammar", "context", "Hogyan működik a lebegő árfolyam a szuverén gazdaságpolitikában?", [
                "Külső aszimmetrikus sokkok esetén leértékelődéssel tompítja a gazdaság visszaesését, megvédve a hazai termelőket.",
                "Minden devizatranzakciót betilt a belföldi piacon.",
                "Rögzíti az inflációt 0 százalékon."
            ], 0, ["c1-growth-model-synthesis"]),
            sb("grammar", "produce", ["A", "monetáris", "stabilitás", "a", "társadalom", "pénzbe", "vetett", "bizalmán", "nyugszik."], ["A", "monetáris", "stabilitás", "a", "társadalom", "pénzbe", "vetett", "bizalmán", "nyugszik."], "Monetary stability rests upon society's confidence in money.", ["c1-growth-model-synthesis"]),
            sw("production", [{"prompt": "Write a critical evaluation of the Eurozone accession dilemma for a converging economy.", "answer": "Az eurózóna-csatlakozás megszünteti az árfolyamkockázatot és a tranzakciós költségeket, ám az önálló monetáris politika feladása miatt elengedhetetlen, hogy a gazdaság termelékenysége és rugalmassága elérje a magországok szintjét."}], ["c1-growth-model-synthesis"]),
            sw("production", [{"prompt": "Formulate a concluding thought on Hungarian monetary resilience over the past century.", "answer": "A forint története a hiperinfláció megfékezésétől a devizahitel-válság rendezéséig azt bizonyítja, hogy a fenntartható gazdasági fejlődés legfontosabb fundamentuma a fegyelmezett költségvetési és monetáris politika harmóniája."}], ["c1-macroeconomic-indicators"])
        ]
    )

    print("=== Finished C1 Unit 13 ===")


if __name__ == "__main__":
    generate_unit_13()
