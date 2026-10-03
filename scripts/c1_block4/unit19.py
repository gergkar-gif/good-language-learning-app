#!/usr/bin/env python3
"""
Hungarian C1 Block 4 - Unit 19 Generator:
  - Track 1 (Core): Unit 19 — "Sociological Stratification, Class Structures & Social Mobility" (c1-19)
  - Track 2 (Discourse): Unit 19 — "Center vs. Periphery: Spatial Inequalities & Rural Transformations" (c1-tarsadalmireteg)
"""

import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT))

from scripts.c1_block1.common import mc, match, fb, sb, dc, sw, write_json, emit_instructional_lesson, emit_consolidation_lesson
from scripts.c1_block4.registry_helper import register_unit


def generate_unit_19():
    print("=== Generating C1 Unit 19 ===")
    
    # Register skills & titles
    new_skills = {
        "c1-19-vocab": {"kind": "vocabulary"},
        "c1-tarsadalmireteg-vocab": {"kind": "vocabulary"},
        "c1-adv-sociological-comparative-proportions": {"kind": "grammar"},
        "c1-participle-temporal-anteriority": {"kind": "grammar"},
        "c1-adv-contrastive-restrictive-markers": {"kind": "grammar"},
        "c1-complex-sociological-causatives": {"kind": "grammar"},
        "c1-adv-scalar-evaluative-adverbials": {"kind": "grammar"},
        "c1-discourse-spatial-disparity-markers": {"kind": "grammar"},
        "c1-adv-concessive-spatial-correlatives": {"kind": "grammar"},
        "c1-rhetorical-sociodemographic-adversatives": {"kind": "grammar"},
        "c1-modal-teleological-policy-syntax": {"kind": "grammar"},
        "c1-adv-evaluative-polarization-particles": {"kind": "grammar"},
    }
    new_titles = {
        "c1-19-vocab": "reading",
        "c1-tarsadalmireteg-vocab": "reading",
        "c1-adv-sociological-comparative-proportions": "proportional relational adverbials expressing comparative socio-demographic ratios",
        "c1-participle-temporal-anteriority": "adverbial participial structures expressing chronological anteriority in sociological historiography",
        "c1-adv-contrastive-restrictive-markers": "contrastive restrictive adverbial modifiers qualifying quantitative social stratification",
        "c1-complex-sociological-causatives": "complex participial causative chains articulating multifaceted socioeconomic causality",
        "c1-adv-scalar-evaluative-adverbials": "scalar evaluative adverbials calibrating magnitude and trajectory in inequality metrics",
        "c1-discourse-spatial-disparity-markers": "spatial disparity discourse markers characterizing territorial economic divides",
        "c1-adv-concessive-spatial-correlatives": "concessive spatial correlatives mapping pervasive regional structural phenomena",
        "c1-rhetorical-sociodemographic-adversatives": "rhetorical adversative structures contrasting urban center and rural periphery dynamics",
        "c1-modal-teleological-policy-syntax": "teleological postpositional phrases formulating structural development goals",
        "c1-adv-evaluative-polarization-particles": "evaluative polarization particles emphasizing societal fragmentation and divergence",
    }
    
    core_title = "Sociological Stratification, Class Structures & Social Mobility"
    core_stems = [f"c1-19-0{i}" for i in range(1, 6)] + ["c1-19-consolidation"]
    disc_title = "Center vs. Periphery: Spatial Inequalities & Rural Transformations"
    disc_stems = [f"c1-tarsadalmireteg-0{i}" for i in range(1, 6)] + ["c1-tarsadalmireteg-consolidation"]
    
    register_unit(19, core_title, core_stems, disc_title, disc_stems, new_skills, new_titles)

    # ----------------------------------------------------
    # TRACK 1: CORE (c1-19)
    # ----------------------------------------------------
    core_intro = [
        "Hungarian sociological discourse has long been preoccupied with the structural fractures of society: the coexistence of feudal habits and modern capitalism, the erosion of the middle class, and intergenerational immobility.",
        "In this unit, anchored by Ferenc Erdei's landmark 1943 sociological analysis 'A magyar társadalom', you will master the elevated academic register used to analyze social stratification, mobility matrices, and demographic reproduction at the C1 level."
    ]

    core_lessons = [
        {
            "num": 1,
            "stem": "c1-19-01",
            "title": "Social Stratification, Status Inconsistency & Class Cleavages",
            "grammar_title": "Proportional Relational Adverbials Expressing Comparative Socio-Demographic Ratios",
            "grammar_skill": "c1-adv-sociological-comparative-proportions",
            "goals": [
                "I can analyze social stratification, status inconsistency, and socio-demographic indicators (*társadalmi rétegződés, státuszkongruencia, osztálytagozódás*).",
                "I can construct relational comparisons using proportional postpositional adverbials (*viszonylatában, arányában, tekintetében, mérvén*).",
                "I can debate the structural transformation of the Hungarian middle class in academic prose."
            ],
            "vocab": [
                {"lemma": "társadalmi rétegződés", "translation": "social stratification", "pos": "expression"},
                {"lemma": "státuszkongruencia", "translation": "status consistency / congruence", "pos": "noun"},
                {"lemma": "társadalmi olló", "translation": "social scissor (wealth gap)", "pos": "expression"},
                {"lemma": "középosztálybeli lecsúszás", "translation": "middle-class downward mobility", "pos": "expression"},
                {"lemma": "jövedelmi polarizáció", "translation": "income polarization", "pos": "expression"},
                {"lemma": "társadalmi újratermelődés", "translation": "social reproduction", "pos": "expression"},
                {"lemma": "presztízsveszteség", "translation": "loss of prestige", "pos": "noun"},
                {"lemma": "osztálytudat", "translation": "class consciousness", "pos": "noun"}
            ],
            "gr_text1": "In sociological analysis, relational proportions are articulated via formal postpositions and derivative adverbs: `viszonylatában` (in relation to), `arányában` (in proportion to), `tekintetében` (with regard to), and `összevetésben` (in comparison with). Example: `A felsőfokú végzettségűek jövedelmi előnye a mediánbér viszonylatában továbbra is markáns, jóllehet a diplomás munkaerő presztízsvesztesége számottevő`.",
            "gr_text2": "These postpositional structures govern nominal complements with bare nouns or possessive inflections, allowing precise statistical calibration.",
            "gr_table": [
                ["A jövedelmi olló a mediánbér viszonylatában az elmúlt évtizedben drámaian kinyílt.", "The social scissor in relation to the median wage has opened dramatically over the past decade."],
                ["A társadalmi mobilitás az iskolázottsági szint emelkedése arányában növekszik.", "Social mobility increases in proportion to the rise in educational attainment."],
                ["A státuszkongruencia hiánya tekintetében a hazai értelmiség sajátos pozíciót foglal el.", "With regard to the lack of status consistency, the domestic intelligentsia occupies a peculiar position."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mit ért a szociológia a 'státuszkongruencia' hiánya alatt?", [
                    "Azt az állapotot, amikor az egyén iskolázottsága, jövedelme és társadalmi presztízse nincs összhangban egymással (pl. magasan képzett, de alulfizetett).",
                    "Azt, hogy valaki nem tudja megjegyezni a munkatársai nevét.",
                    "A bankszámlakivonatok havi rendszeres ellenőrzését."
                ], 0, ["c1-19-vocab"]),
                fb("grammar", "controlled", "A szegénység kockázata a gyermekek száma _____ növekszik a háztartásokban. (in proportion to / arányában)", "arányában", "The risk of poverty increases in proportion to the number of children in households.", ["c1-adv-sociological-comparative-proportions"]),
                match("vocabulary", "controlled", [["társadalmi olló", "a gazdagok és szegények közötti növekvő távolság"], ["középosztálybeli lecsúszás", "az anyagi biztonság és státusz elvesztése"], ["jövedelmi polarizáció", "a társadalom szélsőséges vagyoni kettészakadása"], ["társadalmi újratermelődés", "a társadalmi pozíciók átörökítése generációk között"]], ["c1-19-vocab"]),
                fb("grammar", "practice", "A diplomás pályakezdők fizetése az átlagkereset _____ még mindig kedvezőbb. (in relation to / viszonylatában)", "viszonylatában", "The salary of graduate career starters in relation to average earnings is still more favorable.", ["c1-adv-sociological-comparative-proportions"]),
                sb("grammar", "practice", ["A", "társadalmi", "mobilitás", "mértéke", "az", "iskolázottság", "arányában", "változik."], ["A", "társadalmi", "mobilitás", "mértéke", "az", "iskolázottság", "arányában", "változik."], "The degree of social mobility varies in proportion to education.", ["c1-adv-sociological-comparative-proportions"]),
                dc("dialogue", [
                    {"speaker": "Kutató", "text": "Hogyan alakult a magyar középosztály helyzete az elmúlt években?"},
                    {"speaker": "Szociológus", "text": "A jövedelmi adatok viszonylatában egyértelmű _____ figyelhető meg az alsóbb rétegek felé."},
                ], ["lecsúszás", "gazdagodás", "egyesülés"], 0, ["c1-adv-sociological-comparative-proportions"]),
                sw("production", [{"prompt": "Write a sociological observation about wage inequalities using 'arányában' or 'viszonylatában'.", "answer": "A legfelső tized vagyoni gyarapodása a társadalom alsó felének jövedelmi stagnálása viszonylatában a társadalmi olló aggasztó kinyílását jelzi."}], ["c1-adv-sociological-comparative-proportions"]),
                mc("grammar", "check", "Melyik névutó fejez ki arányossági és viszonyítási kapcsolatot szociológiai szövegben?", [
                    "viszonylatában / arányában",
                    "mögött",
                    "alatt"
                ], 0, ["c1-adv-sociological-comparative-proportions"])
            ]
        },
        {
            "num": 2,
            "stem": "c1-19-02",
            "title": "Historical Social Formations & Participial Anteriority",
            "grammar_title": "Adverbial Participial Structures Expressing Chronological Anteriority in Sociological Historiography",
            "grammar_skill": "c1-participle-temporal-anteriority",
            "goals": [
                "I can evaluate historical social formations, agrarian proletariat, and urban bourgeois emergence (*úri középosztály, cselédsors, polgárosodás*).",
                "I can deploy adverbial participial structures expressing chronological anteriority (*felbontván, elnyerve, megalapozódva, felszámolódván*).",
                "I can interpret the historical roots of Hungarian social inequality from the 19th century to the interwar era."
            ],
            "vocab": [
                {"lemma": "úri középosztály", "translation": "gentry middle class (historical)", "pos": "expression"},
                {"lemma": "dzsentri réteg", "translation": "gentry stratum", "pos": "expression"},
                {"lemma": "agrárproletariátus", "translation": "agrarian proletariat", "pos": "noun"},
                {"lemma": "cselédsors", "translation": "servant's / farmhand's lot", "pos": "noun"},
                {"lemma": "polgárosodás", "translation": "embourgeoisement / civic development", "pos": "noun"},
                {"lemma": "birtokstruktúra", "translation": "landholding structure", "pos": "expression"},
                {"lemma": "társadalmi zártság", "translation": "social closure / insularity", "pos": "expression"},
                {"lemma": "feudális csökevény", "translation": "feudal vestige", "pos": "expression"}
            ],
            "gr_text1": "Adverbial participles in `-va/-ve` and the elevated archaic-literary `-ván/-vén` establish prior completed conditions in historical socio-economic exposition: `A jobbágyságot felszámolván a reformkor megnyitotta az utat a polgárosodás előtt` (Having abolished serfdom, the Reform Era paved the way for embourgeoisement).",
            "gr_text2": "In contemporary C1 register, `-va/-ve` clauses typically compress temporal subordinates: `A nagybirtokrendszert lebontva az ország új társadalmi osztályok felemelkedését tette lehetővé`.",
            "gr_table": [
                ["A felemelkedés zálogát elnyerve az új polgárság gyorsan gazdasági hatalommá vált.", "Having won the pledge of advancement, the new bourgeoisie quickly became an economic power."],
                ["A feudális privilégiumokat lebontván a társadalom a modern intézmények kiépítésébe kezdett.", "Having dismantled feudal privileges, society began constructing modern institutions."],
                ["A dzsentri réteg elszegényedve az állami hivatalnoki pozíciókba menekült a deklasszálódás elől.", "Having become impoverished, the gentry stratum fled into state bureaucratic positions to escape downward declassing."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Kiket nevezett a történeti szociológia 'úri középosztálynak' a két háború közötti Magyarországon?", [
                    "A birtokaikat vesztett, állami hivatalokban és a katonaságban menedéket kereső, feudális értékrendet őrző elitet.",
                    "A gyárakban dolgozó szakmunkásokat.",
                    "A falusi kisiparosokat és molnárokat."
                ], 0, ["c1-19-vocab"]),
                fb("grammar", "controlled", "A jobbágyrendszer felszámolását _____ a magyar társadalom még évtizedekig hordozta a rendi reflexeket. (Having experienced / megélve)", "megélve", "Having experienced the abolition of the serf system, Hungarian society still bore estate reflexes for decades.", ["c1-participle-temporal-anteriority"]),
                match("vocabulary", "controlled", [["dzsentri réteg", "elszegényedett nemesi hivatalnokréteg"], ["agrárproletariátus", "földtelen falusi bérmunkások tömege"], ["birtokstruktúra", "a termőföld megoszlása a gazdaságban"], ["feudális csökevény", "a rendi korszakból visszamaradt merev szokás"]], ["c1-19-vocab"]),
                fb("grammar", "practice", "A vagyont elveszítve a gentry családok az állami apparátusba menekültek a _____ elől. (declassing / deklasszálódás)", "deklasszálódás", "Having lost their wealth the gentry families fled into the state apparatus to escape declassing.", ["c1-participle-temporal-anteriority"]),
                sb("grammar", "practice", ["A", "földet", "felosztván", "az", "állam", "átalakította", "a", "falusi", "társadalmat."], ["A", "földet", "felosztván", "az", "állam", "átalakította", "a", "falusi", "társadalmat."], "Having divided the land, the state restructured village society.", ["c1-participle-temporal-anteriority"]),
                dc("dialogue", [
                    {"speaker": "Történész", "text": "Hogyan maradhatott fenn a rendi szemlélet a tőkés átalakulás után is?"},
                    {"speaker": "Kutató", "text": "A polgárosodást félig elvégezve a gazdasági tőke nem párosult valódi politikai _____."},
                ], ["demokráciával", "csődökkel", "békével"], 0, ["c1-participle-temporal-anteriority"]),
                sw("production", [{"prompt": "Write a historical sentence on social transformation using an anterior participle in '-va/-ve' or '-ván/-vén'.", "answer": "A kiegyezést követően a nemzeti szuverenitás részleges garanciáit elnyervén a magyar vezető réteg mégsem tudta felszámolni az agrárproletariátus nyomorúságát."}], ["c1-participle-temporal-anteriority"]),
                mc("grammar", "check", "Melyik igeneves szerkezet fejez ki emelkedett előidejű lezárt cselekvést?", [
                    "felszámolván / elnyerve",
                    "felszámolni",
                    "felszámoláskor"
                ], 0, ["c1-participle-temporal-anteriority"])
            ]
        },
        {
            "num": 3,
            "stem": "c1-19-03",
            "title": "Poverty, Deprivation & Contrastive Restrictive Modifiers",
            "grammar_title": "Contrastive Restrictive Adverbial Modifiers Qualifying Quantitative Social Stratification",
            "grammar_skill": "c1-adv-contrastive-restrictive-markers",
            "goals": [
                "I can analyze deep poverty, cumulative deprivation, and social exclusion (*mélyszegénység, halmozott hátrány, depriváció*).",
                "I can employ contrastive restrictive adverbials (*mindössze, pusztán csak, kizárólagosan, alig-alig*).",
                "I can critically evaluate child poverty and generational social traps in contemporary sociological data."
            ],
            "vocab": [
                {"lemma": "mélyszegénység", "translation": "deep poverty", "pos": "noun"},
                {"lemma": "halmozott hátrány", "translation": "cumulative disadvantage", "pos": "expression"},
                {"lemma": "anyagi depriváció", "translation": "material deprivation", "pos": "expression"},
                {"lemma": "szegénységi küszöb", "translation": "poverty threshold", "pos": "expression"},
                {"lemma": "társadalmi kirekesztődés", "translation": "social exclusion", "pos": "expression"},
                {"lemma": "társadalmi csapda", "translation": "social trap", "pos": "expression"},
                {"lemma": "segélyfüggőség", "translation": "welfare dependency", "pos": "noun"},
                {"lemma": "szegregátum", "translation": "segregated settlement / slum", "pos": "noun"}
            ],
            "gr_text1": "To qualify exact quantitative thresholds and emphasize systemic limits, C1 Hungarian deploys contrastive restrictive modifiers: `mindössze` (merely/scarcely), `pusztán csak` (purely and only), `kizárólagosan` (exclusively), and `alig-alig` (hardly/scarcely).",
            "gr_text2": "Example: `A leszakadó kistérségekben a lakosság mindössze egynegyede rendelkezik stabil bejelentett munkaviszonnyal, pusztán csak a közfoglalkoztatás biztosít minimális túlélést`.",
            "gr_table": [
                ["A hátrányos helyzetű tanulók közül mindössze néhány százalék jut el a felsőoktatásig.", "Among disadvantaged students merely a few percent make it to higher education."],
                ["A szegregátumokban élők pusztán csak az alkalmi munkákból képesek fenntartani magukat.", "Those living in segregated settlements are able to sustain themselves purely from casual labor."],
                ["A támogatás kizárólagosan a legmélyebb krízishelyzeteket enyhíti, strukturális megoldást nem nyújt.", "The subsidy exclusively eases the deepest crisis situations; it provides no structural solution."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mit nevez a szociológia 'halmozott hátránynak' (cumulative disadvantage)?", [
                    "Amikor az anyagi szegénység, az alacsony iskolázottság, a rossz lakáskörülmények és a földrajzi elszigeteltség együttesen sújtja az egyént.",
                    "A sportversenyeken kapott büntetőpontok összegét.",
                    "A banki hitelkártyák kamatterheit."
                ], 0, ["c1-19-vocab"]),
                fb("grammar", "controlled", "A mélyszegénységben élő családok gyermekeinek _____ töredéke tanulhat tovább érettségit adó iskolában. (merely / mindössze)", "mindössze", "Merely a fraction of children in families living in deep poverty can study further in a school granting matura.", ["c1-adv-contrastive-restrictive-markers"]),
                match("vocabulary", "controlled", [["anyagi depriváció", "az alapvető javak nélkülözése"], ["szegénységi küszöb", "a megélhetési minimum statisztikai határa"], ["szegregátum", "elkülönült, leszakadt településrész"], ["társadalmi kirekesztődés", "a társadalmi fősodorból való kényszerű kiszorulás"]], ["c1-19-vocab"]),
                fb("grammar", "practice", "A segélyezés _____ az akut krízis enyhítésére elég, a kitöréshez nem nyújt eszközt. (purely / pusztán csak)", "pusztán csak", "Welfare is purely enough for easing acute crisis; it provides no tool for breakout.", ["c1-adv-contrastive-restrictive-markers"]),
                sb("grammar", "practice", ["Mindössze", "kevés", "család", "képes", "kitörni", "a", "szegénységi", "csapdából."], ["Mindössze", "kevés", "család", "képes", "kitörni", "a", "szegénységi", "csapdából."], "Merely few families are able to break out of the poverty trap.", ["c1-adv-contrastive-restrictive-markers"]),
                dc("dialogue", [
                    {"speaker": "Szociális munkás", "text": "Hányan jutnak ki a szegregátumok világából?"},
                    {"speaker": "Településvezető", "text": "Mindössze a fiatalok elenyésző része, pusztán azok, akik korai ösztöndíjat és mentort _____."},
                ], ["kapnak", "tagadnak", "felejtenek"], 0, ["c1-adv-contrastive-restrictive-markers"]),
                sw("production", [{"prompt": "Formulate a sentence about educational inequality using 'mindössze' and 'pusztán'.", "answer": "A szegregált iskolákból mindössze elenyésző számú diák jut be az egyetemekre, pusztán a kivételes családi támogatás képes ellensúlyozni a rendszer hibáit."}], ["c1-adv-contrastive-restrictive-markers"]),
                mc("grammar", "check", "Melyik kifejezés szolgál a mennyiségi korlátozottság hangsúlyos kifejezésére?", [
                    "mindössze / pusztán csak",
                    "rendkívül bőségesen",
                    "határtalanul"
                ], 0, ["c1-adv-contrastive-restrictive-markers"])
            ]
        },
        {
            "num": 4,
            "stem": "c1-19-04",
            "title": "Intergenerational Mobility & Complex Causative Chains",
            "grammar_title": "Complex Participial Causative Chains Articulating Multifaceted Socioeconomic Causality",
            "grammar_skill": "c1-complex-sociological-causatives",
            "goals": [
                "I can analyze intergenerational social mobility, glass ceilings, and educational bottlenecks (*társadalmi mobilitás, üvegplafon, iskolai szelekció*).",
                "I can construct complex participial causative chains (*előidézve, maga után vonva, eredményezve, meggátolva*).",
                "I can evaluate statistical mobility tables and meritocratic myths in modern European societies."
            ],
            "vocab": [
                {"lemma": "társadalmi mobilitás", "translation": "social mobility", "pos": "expression"},
                {"lemma": "generációk közötti átörökítés", "translation": "intergenerational transmission", "pos": "expression"},
                {"lemma": "üvegplafon", "translation": "glass ceiling", "pos": "noun"},
                {"lemma": "iskolai szelekció", "translation": "school selection / streaming", "pos": "expression"},
                {"lemma": "meritokrácia", "translation": "meritocracy", "pos": "noun"},
                {"lemma": "társadalmi tőke", "translation": "social capital (Bourdieu)", "pos": "expression"},
                {"lemma": "kulturális tőke", "translation": "cultural capital", "pos": "expression"},
                {"lemma": "merev mobilitási struktúra", "translation": "rigid mobility structure", "pos": "expression"}
            ],
            "gr_text1": "Multifaceted sociological causality connects structural preconditions to long-term systemic effects via chained participial clauses: `előidézve` (inducing), `maga után vonva` (entailing), `eredményezve` (resulting in), `meggátolva` (thwarting).",
            "gr_text2": "Example: `A korai iskolai szelekció korán kettészakítja a diákokat, meggátolva a hátrányos helyzetűek mobilitását, és végső soron a társadalmi egyenlőtlenségek merev újratermelődését eredményezve`.",
            "gr_table": [
                ["A korai szakosodás lemorzsolódást idéz elő, maga után vonva az alacsony jövedelmű csoportok tartós bezáródását.", "Early specialization induces dropout, entailing the permanent containment of low-income groups."],
                ["A kulturális tőke hiánya gátolja az érvényesülést, a társadalmi olló kinyílását eredményezve.", "The lack of cultural capital hinders advancement, resulting in the opening of the social scissor."],
                ["A merev mobilitási struktúra elfojtja a tehetséget, súlyos gazdasági versenyképességi veszteséget okozva a nemzetnek.", "The rigid mobility structure suffocates talent, causing severe economic competitiveness loss for the nation."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mit bizonyítanak a Pierre Bourdieu szociológiájára épülő mobilitásvizsgálatok?", [
                    "Hogy az iskolarendszer nem semlegesíti a családi hátteret, hanem a kulturális és társadalmi tőke révén újratermeli a meglévő osztálykülönbségeket.",
                    "Hogy a könyvolvasás csökkenti a számítógépes játékok népszerűségét.",
                    "Hogy minden diák pontosan ugyanannyi pénzt költ tanszerekre."
                ], 0, ["c1-19-vocab"]),
                fb("grammar", "controlled", "A szelektív iskolarendszer elmélyíti a társadalmi szakadékot, a tehetséges fiatalok elvesztését _____ az országnak. (causing / okozva)", "okozva", "The selective school system deepens the social divide, causing the loss of talented youth for the country.", ["c1-complex-sociological-causatives"]),
                match("vocabulary", "controlled", [["társadalmi tőke", "hasznos kapcsolati háló és bizalom"], ["kulturális tőke", "otthonról hozott műveltség és nyelvi kód"], ["üvegplafon", "láthatatlan akadály az előléptetésben"], ["meritokrácia", "érdemeken alapuló társadalmi felemelkedés"]], ["c1-19-vocab"]),
                fb("grammar", "practice", "A szociális háló meggyengülése elszegényedést szült, maga után _____ a bűnözési ráta növekedését. (entailing / vonva)", "vonva", "The weakening of the social safety net spawned impoverishment, entailing an increase in crime rates.", ["c1-complex-sociological-causatives"]),
                sb("grammar", "practice", ["A", "szelekció", "lemorzsolódást", "szül,", "mélyítve", "a", "társadalmi", "egyenlőtlenségeket."], ["A", "szelekció", "lemorzsolódást", "szül,", "mélyítve", "a", "társadalmi", "egyenlőtlenségeket."], "Selection spawns dropout, deepening social inequalities.", ["c1-complex-sociological-causatives"]),
                dc("dialogue", [
                    {"speaker": "Oktatáskutató", "text": "Valóban esélyt ad az iskola a kitörésre a szegénységből?"},
                    {"speaker": "Szociológus", "text": "Sajnos a korai szétválogatás meggátolja a felzárkózást, az egyenlőtlenségek újratermelődését _____."},
                ], ["eredményezve", "tiltva", "titkolva"], 0, ["c1-complex-sociological-causatives"]),
                sw("production", [{"prompt": "Write a complex causal sentence about social immobility using 'maga után vonva' or 'eredményezve'.", "answer": "A hátrányos helyzetű kistelepülések infrastrukturális elhanyagolása a minőségi oktatás ellehetetlenülését idézi elő, maga után vonva az ott élők generációkon átívelő mozdulatlanságát."}], ["c1-complex-sociological-causatives"]),
                mc("grammar", "check", "Melyik igeneves szerkezet fejez ki kauzális láncolatot és következményi viszonyt?", [
                    "maga után vonva / eredményezve",
                    "miután meglátta",
                    "annak dacára"
                ], 0, ["c1-complex-sociological-causatives"])
            ]
        },
        {
            "num": 5,
            "stem": "c1-19-05",
            "title": "Ferenc Erdei & The Dual Society of Hungary",
            "grammar_title": "Scalar Evaluative Adverbials Calibrating Magnitude and Trajectory in Inequality Metrics",
            "grammar_skill": "c1-adv-scalar-evaluative-adverbials",
            "goals": [
                "I can analyze Ferenc Erdei's classical sociological essay 'A magyar társadalom' (1943) and the 'dual society' concept.",
                "I can employ scalar evaluative adverbs to calibrate magnitude in social inequality analysis (*számottevően, elhanyagolható mértékben, drasztikusan, radikálisan*).",
                "I can critique historical dualism: historical-national gentry culture versus modern civic-bourgeois economic actors."
            ],
            "vocab": [
                {"lemma": "kettős társadalom", "translation": "dual society (Erdei's thesis)", "pos": "expression"},
                {"lemma": "történelmi-nemzeti társadalom", "translation": "historical-national society (gentry-feudal)", "pos": "expression"},
                {"lemma": "polgári társadalom", "translation": "bourgeois-civic society (market-commercial)", "pos": "expression"},
                {"lemma": "társadalomszerkezet", "translation": "social structure", "pos": "noun"},
                {"lemma": "paraszti létforma", "translation": "peasant way of life", "pos": "expression"},
                {"lemma": "hivatali bürokrácia", "translation": "officialdom / bureaucratic state apparatus", "pos": "expression"},
                {"lemma": "társadalmi integráció", "translation": "social integration", "pos": "expression"},
                {"lemma": "történeti tehetetlenség", "translation": "historical inertia", "pos": "expression"}
            ],
            "gr_text1": "Scalar evaluative adverbs measure the extent and severity of social shifts: `számottevően` (significantly/appreciably), `elhanyagolható mértékben` (to a negligible extent), `drasztikusan` (drastically), `szembeötlően` (conspicuously), `radikálisan` (radically).",
            "gr_text2": "Example: `A történeti nemesi réteg és a polgárság jövedelmi helyzete ugyan hasonlított, értékrendjük és viselkedéskultúrájuk mindazonáltal számottevően különbözött`.",
            "gr_table": [
                ["A társadalom kettészakadása az elmúlt évtizedekben számottevően felerősödött.", "The tearing in two of society has strengthened significantly in past decades."],
                ["A mobilitás mértéke a szegregátumokban elhanyagolható mértékben növekedett.", "The rate of mobility in segregated areas increased to a negligible extent."],
                ["A jövedelmi olló drasztikusan szétnyílt a főváros és az aprófalvas vidék között.", "The income scissor opened drastically between the capital and the tiny-village countryside."]
            ],
            "classic_story": {
                "slug": "c1-19-erdei",
                "author": "Erdei Ferenc",
                "work": "A magyar társadalom (1943)",
                "title": "Erdei Ferenc: A kettős társadalom és a magyar sors",
                "summary": "Ferenc Erdei's landmark 1943 sociographical analysis diagnosing Hungary as a 'dual society' split between a feudal-gentry bureaucratic hierarchy and a modern bourgeois-capitalist market society.",
                "characters": ["Erdei Ferenc"],
                "paragraphs": [
                    {"type": "narration", "text": "Amikor Erdei Ferenc a szárszói konferencián 1943-ban kifejtette 'A magyar társadalom' című előadását, a hazai szociológia egyik legmélyebb és legmaradandóbb diagnózisát adta. Erdei rámutatott: a magyar társadalomfejlődés tragédiája az, hogy az országban nem jött létre egységes, szerves polgári társadalom. Ehelyett két, egymás mellett létező, de lényegileg eltérő társadalomszerkezet alakult ki, amely mint két külön világ élt a közös haza keretein belül."},
                    {"type": "narration", "text": "Az egyik a 'történelmi-nemzeti társadalom' volt: a régi rendi világ örököse, a nemesi és dzsentri hagyományokból táplálkozó úri középosztály, amely az állami hivatali bürokráciát, a katonaságot és a megyei igazgatást uralta. E réteg számára az államhatalom nem a polgárok szolgálatát, hanem a rendi privilégiumok és az úri tekintély fenntartását jelentette. Gazdaságilag gyakran erőtlen volt, ám társadalmi presztízsét és politikai monopóliumát féltékenyen őrizte."},
                    {"type": "narration", "text": "Mellette épült fel a modern kapitalizmus által létrehozott 'polgári társadalom': a gyárosok, kereskedők, bankárok, orvosok és ügyvédek világa, amely döntően asszimilálódó zsidó és német polgárokból verbuválódott. Ez a szféra dinamikus gazdasági erőt képviselt, ám politikai legitimációját a történelmi elit folytonosan vitatta, idegen testnek bélyegezve a modern tőkés polgárosodást."},
                    {"type": "narration", "text": "És e két világ alatt ott sínylődött a hatalmas, néma tömeg: a hárommillió koldus országa, az agrárproletariátus és a kisparasztság, amely el volt zárva a felemelkedés minden útjától. Erdei zseniális meglátása szerint a magyar fejlődés legnagyobb akadálya a történelmi tehetetlenség volt: az, hogy a nemzeti elit a múltba révedve megakadályozta a valódi, demokratikus és szolidáris nemzeti integráció megvalósulását."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Mi a lényege Erdei Ferenc híres 'kettős társadalom' modelljének?", [
                    "Hogy a magyar társadalom egy rendi-nemesi származású történelmi elitre és egy modern gazdasági polgárságra hasadt ketté, miközben a parasztság kirekesztve maradt.",
                    "Hogy Magyarországon két különböző miniszterelnök uralkodott egyszerre.",
                    "Hogy az ország két hivatalos pénznemet használt a kereskedelemben."
                ], 0, ["c1-19-vocab"]),
                fb("grammar", "controlled", "A két társadalmi szféra értékrendje _____ különbözött egymástól a Horthy-korszakban. (significantly / számottevően)", "számottevően", "The value system of the two social spheres differed significantly from each other in the Horthy era.", ["c1-adv-scalar-evaluative-adverbials"]),
                match("vocabulary", "controlled", [["kettős társadalom", "a rendi és polgári világ párhuzamos létezése"], ["paraszti létforma", "a földhöz kötött hagyományos vidéki élet"], ["hivatali bürokrácia", "az államapparátust uraló úri közigazgatás"], ["történeti tehetetlenség", "a fejlődést fékező múltbeli struktúrák merevsége"]], ["c1-19-vocab"]),
                mc("reading", "practice", "Miért tekintette Erdei a parasztság helyzetét a nemzet legnagyobb tragédiájának?", [
                    "Mert a hárommilliós paraszti tömeg el volt zárva az oktatástól, a földtől és a politikai jogoktól, így a társadalom többsége nem válhatott cselekvő polgárrá.",
                    "Mert a parasztok nem akartak modern ruhákban járni.",
                    "Mert a parasztság nem értett a gépjárművezetéshez."
                ], 0, None),
                sb("grammar", "practice", ["A", "társadalmi", "szakadék", "drasztikusan", "mélyült", "a", "két", "világ", "között."], ["A", "társadalmi", "szakadék", "drasztikusan", "mélyült", "a", "két", "világ", "között."], "The social divide deepened drastically between the two worlds.", ["c1-adv-scalar-evaluative-adverbials"]),
                sw("production", [{"prompt": "Write a reflection on Erdei Ferenc's dual society thesis using a scalar evaluative adverb.", "answer": "Erdei Ferenc diagnózisa számottevően hozzájárult annak megértéséhez, hogy a polgári demokratikus értékek miért verték oly nehezen gyökeret a rendi reflexekkel terhelt magyar közéletben."}], ["c1-adv-scalar-evaluative-adverbials"]),
                mc("grammar", "check", "Melyik határozószó fejez ki mértéki és skálázási fokozatot szociológiai értékelésben?", [
                    "számottevően / drasztikusan",
                    "holnapután",
                    "odakint"
                ], 0, ["c1-adv-scalar-evaluative-adverbials"])
            ]
        }
    ]

    for l in core_lessons:
        emit_instructional_lesson(19, "core", l, core_title, core_intro if l["num"] == 1 else None)

    # Core Consolidation Lesson
    emit_consolidation_lesson(
        19,
        "core",
        "c1-19-consolidation",
        core_title,
        [
            "I can master C1 academic vocabulary of social stratification, status inconsistency, and mobility.",
            "I can deploy relational proportions, anterior participles, restrictive modifiers, causative chains, and scalar evaluative adverbs.",
            "I can critically evaluate Erdei Ferenc's 'Dual Society' thesis and historical class formations."
        ],
        [
            mc("grammar", "recognize", "Melyik mondat alkalmaz helyes arányossági névutót szociológiai kontextusban?", [
                "A társadalmi mobilitás az iskolai végzettség arányában és viszonylatában mérhető a legpontosabban.",
                "A mobilitás mögött sétálnak a diákok az utcán.",
                "A szociológus az iskola mellett várakozott."
            ], 0, ["c1-adv-sociological-comparative-proportions"]),
            mc("grammar", "recognize", "Milyen szerkezettel fejezhetünk ki kauzális láncolatot a szociológiai érvelésben?", [
                "előidézve a leszakadást, maga után vonva a szegregációt és a mobilitás gátlását eredményezve",
                "miközben kávéztak a konferencián",
                "hogyha szép idő lesz a hétvégén"
            ], 0, ["c1-complex-sociological-causatives"]),
            match("vocabulary", "recognize", [["kettős társadalom", "Erdei elmélete: rendi és polgári szféra kettőssége"], ["státuszkongruencia", "iskolázottság, jövedelem és presztízs harmóniája"], ["anyagi depriváció", "alapvető megélhetési források hiánya"], ["társadalmi újratermelődés", "osztálykülönbségek generációs átörökítése"], ["üvegplafon", "láthatatlan akadály a társadalmi felemelkedésben"]], ["c1-19-vocab"]),
            fb("vocabulary", "recall", "A gazdagok és szegények közötti szakadék tágulását a szociológia a _____ kinyílásaként írja le. (social scissor / társadalmi olló)", "társadalmi olló", "The widening of the divide between rich and poor is described by sociology as the opening of the social scissor.", ["c1-19-vocab"]),
            fb("vocabulary", "recall", "A kistelepüléseken élők számára a legnagyobb kihívást a kumulatív, _____ jelenti. (cumulative disadvantage / halmozott hátrány)", "halmozott hátrány", "For those living in small settlements, the greatest challenge is cumulative disadvantage.", ["c1-19-vocab"]),
            fb("grammar", "recall", "A feudális kötelékeket _____ a társadalom elindult a polgárosodás útján. (having severed / felbontván)", "felbontván", "Having severed feudal bonds, society embarked upon the path of embourgeoisement.", ["c1-participle-temporal-anteriority"]),
            fb("grammar", "context", "A hátrányos helyzetű diákok közül _____ néhányan jutnak be az orvosi egyetemekre. (merely / mindössze)", "mindössze", "Among disadvantaged students merely a few get admitted to medical universities.", ["c1-adv-contrastive-restrictive-markers"]),
            fb("grammar", "context", "A jövedelmi olló a főváros és a falvak között _____ mélyült az utóbbi évtizedben. (drastically / drasztikusan)", "drasztikusan", "The income scissor between the capital and villages deepened drastically in the past decade.", ["c1-adv-scalar-evaluative-adverbials"]),
            mc("grammar", "context", "Mi a szerepe a 'mindössze' és 'pusztán csak' partikuláknak a szociológiai statisztikák bemutatásakor?", [
                "Hangsúlyozzák a pozitív kitörési arányok drámai elégtelenségét és a strukturális bezártságot.",
                "Megkérdőjelezik a felmérést végző matematikusok hitelességét.",
                "Kijelentik, hogy a számok egyáltalán nem fontosak."
            ], 0, ["c1-adv-contrastive-restrictive-markers"]),
            sb("grammar", "produce", ["A", "társadalmi", "mobilitás", "a", "demokrácia", "egyik", "legfőbb", "próbaköve."], ["A", "társadalmi", "mobilitás", "a", "demokrácia", "egyik", "legfőbb", "próbaköve."], "Social mobility is one of the foremost touchstones of democracy.", ["c1-adv-scalar-evaluative-adverbials"]),
            sw("production", [{"prompt": "Write a critical evaluation of social mobility in Hungary using 'maga után vonva'.", "answer": "A hazai oktatási rendszer korai szelekciója meggátolja a hátrányos helyzetű tehetségek kibontakozását, maga után vonva a társadalmi egyenlőtlenségek generációkon átívelő merev újratermelődését."}], ["c1-complex-sociological-causatives"]),
            sw("production", [{"prompt": "Formulate a concluding thought on Erdei Ferenc's dual society model.", "answer": "Erdei Ferenc felismerése mindmáig érvényes: a magyar társadalom csak akkor válhat valóban szerves egésszé, ha képes meghaladni a rendi reflexeket és valódi polgári esélyegyenlőséget teremteni minden polgárának."}], ["c1-adv-scalar-evaluative-adverbials"])
        ]
    )

    # ----------------------------------------------------
    # TRACK 2: DISCOURSE (c1-tarsadalmireteg)
    # ----------------------------------------------------
    slug = "tarsadalmireteg"
    disc_intro = [
        "Hungary's territorial geography is defined by a massive structural distortion: the overwhelming centralization of Budapest (the 'waterhead') contrasted against rapidly depopulating peripheries, infrastructural deserts, and rural crisis zones.",
        "In this unit, you will master the elevated discourse of spatial disparity analysis, transport poverty, rural resilience, and decentralization policy in contemporary Hungary."
    ]

    disc_lessons = [
        {
            "num": 1,
            "stem": f"c1-{slug}-01",
            "title": "Budapest Primacy, The 'Waterhead' & Regional Disconnect",
            "grammar_title": "Spatial Disparity Discourse Markers Characterizing Territorial Economic Divides",
            "grammar_skill": "c1-discourse-spatial-disparity-markers",
            "goals": [
                "I can analyze capital city primacy, the Budapest 'waterhead' syndrome, and regional economic divides (*fővárosi vízfej, területi egyenlőtlenség, regionális szakadék*).",
                "I can deploy spatial disparity discourse markers (*éles cezúra feszül, markáns szakadék tátong, látványos aszimmetria mutatkozik*).",
                "I can debate the concentration of GDP, culture, and investment capital in the central agglomeration."
            ],
            "vocab": [
                {"lemma": "fővárosi vízfej", "translation": "capital city 'waterhead' (extreme centralization)", "pos": "expression"},
                {"lemma": "területi egyenlőtlenség", "translation": "territorial / regional inequality", "pos": "expression"},
                {"lemma": "regionális szakadék", "translation": "regional gap / abyss", "pos": "expression"},
                {"lemma": "centrum-periféria viszony", "translation": "center-periphery relation", "pos": "expression"},
                {"lemma": "agglomerációs robbanás", "translation": "agglomeration sprawl / explosion", "pos": "expression"},
                {"lemma": "erőforrás-elszívás", "translation": "drainage / extraction of resources", "pos": "noun"},
                {"lemma": "fejlettségi aszimmetria", "translation": "developmental asymmetry", "pos": "expression"},
                {"lemma": "egyfókuszú térszerkezet", "translation": "monocentric spatial structure", "pos": "expression"}
            ],
            "gr_text1": "Disparity markers in regional geography express structural economic divergence through dramatic spatial metaphors: `éles cezúra feszül` (a sharp caesura/rupture stretches), `markáns szakadék tátong` (a distinct chasm yawns), `látványos aszimmetria mutatkozik` (spectacular asymmetry appears), `mély törésvonal húzódik` (a deep fault line runs).",
            "gr_text2": "Example: `A fővárosi régió gazdasági teljesítménye és a keleti határszél között markáns szakadék tátong: Budapest egyfókuszú vízfejként szívja el a vidéki térségek fiatal humántőkéjét`.",
            "gr_table": [
                ["A fejlett északnyugati országrész és az északkeleti határvidék között éles cezúra feszül.", "Between the developed northwestern part of the country and the northeastern borderland stretches a sharp caesura."],
                ["A főváros és a vidék életszínvonala tekintetében markáns szakadék tátong.", "Regarding the standard of living of the capital and the countryside a distinct chasm yawns."],
                ["A tőkeberuházások eloszlásában látványos aszimmetria mutatkozik Budapest javára.", "In the distribution of capital investments spectacular asymmetry appears in favor of Budapest."]
            ],
            "world_story_seg": {
                "seg_slug": "vizfej",
                "title": "A vízfej országa: Budapest aranykora és a leszakadó vidék valósága",
                "summary": "Exploring the historical roots of Budapest's overwhelming economic and cultural centrality and how the monocentric spatial structure starves the outer regions of vitality.",
                "paragraphs": [
                    {"type": "narration", "text": "Amikor a repülőgép éjszaka megközelíti a Kárpát-medencét, a magasból döbbenetes látvány tárul a szemünk elé. A Duna partján gigantikus, ragyogó fényóceánként izzik Budapest metropolisza, amely mintha egyetlen hatalmas mágnesként rántaná magához az ország összes energiáját. És ezen a káprázatos fényburkon túl, alig ötven-hatvan kilométerre, hirtelen elenyésznek a fények: sötétbe és csendbe burkolózik a magyar vidék, ahol falvak százai élik mindennapi, elfeledett életüket."},
                    {"type": "narration", "text": "Ez az egyfókuszú térszerkezet nem új keletű: a trianoni határok meghúzása óta a főváros valódi 'vízfejként' magasodik a megcsonkított hátország fölé. Itt koncentrálódik a hazai GDP több mint negyven százaléka, az egyetemek, a kulturális intézmények és a nemzetközi nagyvállalatok központjai. A centrum-periféria viszony brutális következménye az erőforrás-elszívás: a legtehetségesebb vidéki fiatalok nemzedékről nemzedékre Budapestre költöznek, miközben az elnéptelenedő falvakban megáll az idő."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Mit jelent a 'fővárosi vízfej' kifejezés a magyar urbanisztikában?", [
                    "Azt a torz térszerkezetet, amelyben Budapest gazdasági, lakossági és kulturális súlya aránytalanul meghaladja az összes többi hazai városét.",
                    "A parlament épületének kupolaszerkezetét.",
                    "A Duna legmélyebb pontján lévő árvízvédelmi műtárgyat."
                ], 0, ["c1-tarsadalmireteg-vocab"]),
                fb("grammar", "controlled", "A főváros és a leszakadó kistelepülések között markáns _____ az életszínvonal tekintetében. (chasm yawns / szakadék tátong)", "szakadék tátong", "Between the capital and lagging small settlements a distinct chasm yawns regarding living standard.", ["c1-discourse-spatial-disparity-markers"]),
                match("vocabulary", "controlled", [["egyfókuszú térszerkezet", "egyetlen központra épülő országos hálózat"], ["erőforrás-elszívás", "a tehetség és tőke áramlása a centrumba"], ["fejlettségi aszimmetria", "a régiók egyenlőtlen gazdasági ereje"], ["agglomerációs robbanás", "a főváros környéki települések túlnépesedése"]], ["c1-tarsadalmireteg-vocab"]),
                fb("grammar", "practice", "A nyugati határszél és a keleti végek gazdasági mutatói között éles _____ feszül. (caesura stretches / cezúra feszül)", "cezúra feszül", "Between the economic indicators of the western borderland and the eastern margins stretches a sharp caesura.", ["c1-discourse-spatial-disparity-markers"]),
                sb("grammar", "practice", ["A", "térszerkezeti", "aszimmetria", "mély", "törésvonalat", "húz", "az", "országban."], ["A", "térszerkezeti", "aszimmetria", "mély", "törésvonalat", "húz", "az", "országban."], "Spatial structural asymmetry draws a deep fault line in the country.", ["c1-discourse-spatial-disparity-markers"]),
                dc("dialogue", [
                    {"speaker": "Városkutató", "text": "Megtörhető-e Budapest egyeduralma a magyar térgazdaságban?"},
                    {"speaker": "Regionális tervező", "text": "Csak akkor, ha a vidéki egyetemi nagyvárosokat valódi ellensúlyozó _____ építjük ki."},
                ], ["pólusokká", "falvakká", "múzeumokká"], 0, ["c1-discourse-spatial-disparity-markers"]),
                sw("production", [{"prompt": "Write a sentence diagnosing regional inequality in Hungary using 'markáns szakadék tátong'.", "answer": "A budapesti agglomeráció dinamikus tőkevonzása és az északkeleti aprófalvak gazdasági elszigeteltsége között markáns szakadék tátong, amely veszélyezteti az ország belső kohézióját."}], ["c1-discourse-spatial-disparity-markers"]),
                mc("grammar", "check", "Melyik kifejezés írja le plasztikusan a területi egyenlőtlenségek drámai mértékét?", [
                    "markáns szakadék tátong / éles cezúra feszül",
                    "apró eltérés adódik",
                    "teljesen azonos a helyzet"
                ], 0, ["c1-discourse-spatial-disparity-markers"])
            ]
        },
        {
            "num": 2,
            "stem": f"c1-{slug}-02",
            "title": "Transport Poverty, Rail Line Closures & Mobility Traps",
            "grammar_title": "Concessive Spatial Correlatives Mapping Pervasive Regional Structural Phenomena",
            "grammar_skill": "c1-adv-concessive-spatial-correlatives",
            "goals": [
                "I can analyze transport poverty, rural branch line rail closures, and physical mobility traps (*közlekedési szegénység, szárnyvonal-bezárás, ingázási kényszer*).",
                "I can employ concessive spatial correlatives (*bárhol... mindenütt; amerre csak... ott; bárhová... mindenhol*).",
                "I can evaluate how public transit cutbacks entrench social exclusion in small villages."
            ],
            "vocab": [
                {"lemma": "közlekedési szegénység", "translation": "transport poverty", "pos": "expression"},
                {"lemma": "szárnyvonal-bezárás", "translation": "branch line rail closure", "pos": "expression"},
                {"lemma": "ingázási kényszer", "translation": "forced commuting", "pos": "expression"},
                {"lemma": "zsákfalu", "translation": "cul-de-sac village (dead-end village)", "pos": "noun"},
                {"lemma": "menetrendi ritkítás", "translation": "timetable reduction / cutback", "pos": "expression"},
                {"lemma": "fizikai elérhetetlenség", "translation": "physical inaccessibility", "pos": "expression"},
                {"lemma": "közszolgáltatás-leépítés", "translation": "public service retrenchment", "pos": "expression"},
                {"lemma": "térbeli bezáródás", "translation": "spatial entrapment / confinement", "pos": "expression"}
            ],
            "gr_text1": "Concessive spatial correlatives map systemic patterns across an entire geography: `bárhol [ige], mindenütt [ige]` (wherever..., everywhere...), `amerre csak a szem ellát, ott...` (as far as the eye can see, there...), `bárhová utazzunk is a végeken, mindenhol...` (wherever we travel in the borderlands, everywhere...).",
            "gr_text2": "Example: `Bárhová látogatunk is az ormánsági vagy zempléni kistelepüléseken, mindenütt a bezárt vasútállomások és az elvágott közlekedési folyosók néma tanúságtételével szembesülünk`.",
            "gr_table": [
                ["Bárhová tekintünk a perifériákon, mindenütt a szárnyvonalak elhagyatott síneit látjuk.", "Wherever we look on the peripheries, everywhere we see the abandoned rails of branch lines."],
                ["Amerre csak ritkítják a buszjáratokat, ott azonnal felgyorsul a lakosság elvándorlása.", "Wherever they reduce bus services, there population out-migration immediately accelerates."],
                ["Bárhol szűnik meg a vasúti összeköttetés, mindenütt felerősödik a közlekedési szegénység.", "Wherever railway connection ceases, everywhere transport poverty intensifies."]
            ],
            "world_story_seg": {
                "seg_slug": "kozlekedes",
                "title": "A vágányok vége: Közlekedési szegénység és a zsákfalvak csendje",
                "summary": "Documenting how railway branch line closures and bus schedule cutbacks turn peripheral villages into cut-off mobility traps for the elderly and jobseekers.",
                "paragraphs": [
                    {"type": "narration", "text": "A vasútállomás falán még kivehető az egykori zománctábla, de az ablakokat régen bedeszkázták, a vágányok között pedig derékig ér a gaz. Amikor a szárnyvonalakon leállt a személyszállítás, nem egyszerűen vonatok tűntek el a menetrendből: egy egész életforma és a külvilággal való kapcsolat szakadt meg. Az aprófalvas Baranyában, Nógrádban és a Csereháton a vasút jelentette a biztonságos, olcsó és kiszámítható utat a gimnáziumokba, szakrendelőkre és gyárakba."},
                    {"type": "narration", "text": "A bezárások nyomán kialakult a 'közlekedési szegénység': egy autó nélküli család számára a járási központ elérése is félnapos küzdelemmé vált a ritkított buszjáratok miatt. A zsákfalvak lakói fizikai csapdába estek. A fiatalok, amint tehetik, elmenekülnek; az idősek pedig magukra maradnak a bolt, posta és orvos nélküli településeken, bizonyítva, hogy a tömegközlekedés felszámolása nem megtakarítás, hanem a vidék lassú halálra ítélése."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Mit jelent a 'közlekedési szegénység' (transport poverty) szociológiai fogalma?", [
                    "Azt a helyzetet, amikor a lakosok jövedelem vagy tömegközlekedés hiányában nem tudnak eljutni a munkahelyekre, iskolákba és kórházakba.",
                    "Azt, hogy valaki nem tud prémium kategóriás autót vásárolni.",
                    "A repülőjegyek árának emelkedését az ünnepek alatt."
                ], 0, ["c1-tarsadalmireteg-vocab"]),
                fb("grammar", "controlled", "_____ utazunk a keleti határ mentén, mindenütt a szárnyvonal-bezárások szomorú nyomait látjuk. (Wherever / Bárhová)", "Bárhová", "Wherever we travel along the eastern border, everywhere we see the sad traces of branch line closures.", ["c1-adv-concessive-spatial-correlatives"]),
                match("vocabulary", "controlled", [["zsákfalu", "csak egyetlen bevezető úttal rendelkező település"], ["szárnyvonal-bezárás", "mellékvonali vasúti személyszállítás leállítása"], ["térbeli bezáródás", "a mobilitás hiánya miatti elszigeteltség"], ["közszolgáltatás-leépítés", "posta, iskola vagy orvosi ellátás elvonása"]], ["c1-tarsadalmireteg-vocab"]),
                fb("grammar", "practice", "Amerre csak ritkítják a járatokat, _____ felerősödik az elvándorlás. (there / ott)", "ott", "Wherever they reduce runs, there out-migration intensifies.", ["c1-adv-concessive-spatial-correlatives"]),
                sb("grammar", "practice", ["Bárhol", "zárják", "be", "a", "vasutat,", "mindenütt", "elszigetelődés", "következik."], ["Bárhol", "zárják", "be", "a", "vasutat,", "mindenütt", "elszigetelődés", "következik."], "Wherever they close the railway, everywhere isolation follows.", ["c1-adv-concessive-spatial-correlatives"]),
                dc("dialogue", [
                    {"speaker": "Polgármester", "text": "Hogyan tarthatjuk itt a fiatalokat a faluban vasút nélkül?"},
                    {"speaker": "Szakpolitikus", "text": "Bárhová nézünk a vidéken, mindenütt világos: a mobilitás hiánya azonnali térbeli _____ vezet."},
                ], ["bezáródáshoz", "gazdagsághoz", "ünnepléshez"], 0, ["c1-adv-concessive-spatial-correlatives"]),
                sw("production", [{"prompt": "Write a sentence about rural transport isolation using 'Bárhová... mindenütt'.", "answer": "Bárhová látogatunk is a leszakadó kistérségekben, mindenütt szembetűnő, hogy a tömegközlekedés hiánya miként fosztja meg az embereket a munkavállalás alapvető jogától."}], ["c1-adv-concessive-spatial-correlatives"]),
                mc("grammar", "check", "Melyik páros kötőszóval fejezhetünk ki általánosító, megengedő térbeli összefüggést?", [
                    "bárhová... mindenütt / amerre csak... ott",
                    "ezért... mert",
                    "mintha... úgy"
                ], 0, ["c1-adv-concessive-spatial-correlatives"])
            ]
        },
        {
            "num": 3,
            "stem": f"c1-{slug}-03",
            "title": "Welfare Deserts: Healthcare & Educational Disparities",
            "grammar_title": "Rhetorical Adversative Structures Contrasting Urban Center and Rural Periphery Dynamics",
            "grammar_skill": "c1-rhetorical-sociodemographic-adversatives",
            "goals": [
                "I can critique healthcare deserts, doctor shortages, and school segregation in peripheral counties (*orvoshiány, betöltetlen praxisok, iskolai szegregáció, ellátási sivatag*).",
                "I can construct rhetorical adversatives contrasting urban vs. rural outcomes (*míg a centrumban..., addig a periférián...; jóllehet Budapesten..., a kistelepüléseken viszont...*).",
                "I can debate the constitutional right to equal healthcare and educational access across regions."
            ],
            "vocab": [
                {"lemma": "orvoshiány", "translation": "doctor shortage", "pos": "noun"},
                {"lemma": "betöltetlen háziorvosi praxis", "translation": "unfilled GP practice", "pos": "expression"},
                {"lemma": "iskolai szegregáció", "translation": "school segregation", "pos": "expression"},
                {"lemma": "ellátási sivatag", "translation": "service / welfare desert", "pos": "expression"},
                {"lemma": "szakorvosi ellátás", "translation": "specialist medical care", "pos": "expression"},
                {"lemma": "pedagógushiány", "translation": "teacher shortage", "pos": "noun"},
                {"lemma": "esélyegyenlőtlenség", "translation": "inequality of opportunity", "pos": "noun"},
                {"lemma": "strukturális diszkrimináció", "translation": "structural discrimination", "pos": "expression"}
            ],
            "gr_text1": "To contrast center and periphery in sociological policy prose, balanced adversative clauses deploy parallel syntax: `Míg a [centrum-jellemző], addig a [periféria-jellemző]` (While in the center..., in the periphery...).",
            "gr_text2": "Example: `Míg a fővárosi egyetemi klinikákon a legmodernebb robotsebészeti eljárások válnak elérhetővé, addig a keleti végeken egész járások maradnak állandó háziorvosi és gyermekorvosi ellátás nélkül`.",
            "gr_table": [
                ["Míg a budapesti elitgimnáziumokban anyanyelvi tanárok oktatnak, addig a vidéki kistelepüléseken drámai a pedagógushiány.", "While in Budapest elite gymnasiums native teachers instruct, in rural small settlements teacher shortage is dramatic."],
                ["Míg a nagyvárosokban percek alatt elérhető a szakorvos, addig a periférián heteket kell várni egy vizsgálatra.", "While in big cities a specialist is reachable in minutes, in the periphery one must wait weeks for an examination."],
                ["Egyfelől adott az alkotmányos egyenlőség elve, másfelől a gyakorlatban ellátási sivatagok alakultak ki.", "On one hand the principle of constitutional equality is given; on the other hand in practice welfare deserts have formed."]
            ],
            "world_story_seg": {
                "seg_slug": "szolgaltatas",
                "title": "A végek csendje: Üres rendelők és elszigetelt iskolák",
                "summary": "Investigating the human reality of healthcare deserts and educational segregation where hundreds of GP practices sit permanently empty.",
                "paragraphs": [
                    {"type": "narration", "text": "A rendelő ajtaján sárguló papírlap hirdeti: helyettesítés heti egy alkalommal, két órában. Magyarországon több mint nyolcszáz háziorvosi praxis áll tartósan betöltetlenül, és e praxisok elsöprő többsége a leszakadó észak-magyarországi és dél-dunántúli kistelepüléseken található. Egy hetvenéves cukorbeteg vagy szívbeteg falusi ember számára az alapvető gyógyszerek felíratása vagy egy rutin vérnyomásmérés is megoldhatatlan logisztikai kihívássá vált."},
                    {"type": "narration", "text": "Nem jobb a helyzet az iskolákban sem. Míg a főváros és a megyeszékhelyek elit intézményei a digitális oktatás élvonalában járnak, a periféria általános iskoláiban a szaktanárok hiánya mindennapos rögvalóság: gyakran a testnevelő tanár kénytelen fizikát vagy kémiát oktatni. A szabad iskolaválasztás köntösébe bújtatott szegregáció következtében a tehetősebb szülők elviszik gyermekeiket a városokba, így a falusi iskolákban a halmozottan hátrányos helyzetű tanulók maradnak magukra – megfosztva a kitörés minden reményétől."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Mit nevezünk 'ellátási sivatagnak' (welfare/service desert) a közszolgáltatások terén?", [
                    "Olyan földrajzi térséget, ahol a lakosság számára a mindennapi élethez szükséges alapvető közszolgáltatások (orvos, gyógyszertár, posta, iskola) tartósan hiányoznak.",
                    "Olyan homokos területet, ahol nem esik az eső.",
                    "A bevásárlóközpontok éjszakai zárva tartását."
                ], 0, ["c1-tarsadalmireteg-vocab"]),
                fb("grammar", "controlled", "Míg a nagyvárosokban bőséges a szakorvosi kínálat, _____ a kistelepüléseken százszámra állnak üresen a praxisok. (meanwhile / addig)", "addig", "While in big cities specialist supply is plentiful, meanwhile in small settlements practices stand empty by the hundreds.", ["c1-rhetorical-sociodemographic-adversatives"]),
                match("vocabulary", "controlled", [["betöltetlen háziorvosi praxis", "tartósan orvos nélkül működő körzet"], ["pedagógushiány", "szaktanárok elégtelen száma az iskolákban"], ["ellátási sivatag", "alapvető intézmények nélküli térség"], ["iskolai szegregáció", "hátrányos helyzetű diákok elkülönített oktatása"]], ["c1-tarsadalmireteg-vocab"]),
                fb("grammar", "practice", "Egyfelől a jogszabályok egyenlő ellátást írnak elő, másfelől _____ a perifériákon mélyül a szegregáció. (on the other hand / viszont)", "viszont", "On one hand laws prescribe equal service; on the other hand however segregation deepens in peripheries.", ["c1-rhetorical-sociodemographic-adversatives"]),
                sb("grammar", "practice", ["Míg", "a", "centrumban", "fejlődés", "van,", "addig", "a", "periférián", "hanyatlás."], ["Míg", "a", "centrumban", "fejlődés", "van,", "addig", "a", "periférián", "hanyatlás."], "While in the center there is development, in the periphery there is decline.", ["c1-rhetorical-sociodemographic-adversatives"]),
                dc("dialogue", [
                    {"speaker": "Egészségügyi szakértő", "text": "Miért nem mennek a fiatal orvosok a falusi praxisokba?"},
                    {"speaker": "Háziorvos", "text": "Míg a városban karrierlehetőség és jó fizetés várja őket, addig a periférián magányos és alulfinanszírozott _____ szembesülnek."},
                ], ["küzdelemmel", "díjakkal", "ünnepségekkel"], 0, ["c1-rhetorical-sociodemographic-adversatives"]),
                sw("production", [{"prompt": "Write a comparative sentence contrasting urban and rural educational quality using 'Míg... addig...'.", "answer": "Míg a budapesti tehetős kerületek iskoláiban korszerű laboratóriumok és nyelvtanárok állnak rendelkezésre, addig a hátrányos helyzetű falvakban a szaktanárok hiánya miatt generációk esnek el a felemelkedés esélyétől."}], ["c1-rhetorical-sociodemographic-adversatives"]),
                mc("grammar", "check", "Melyik szerkezettel állíthatunk szembe hatásosan két eltérő társadalmi valóságot?", [
                    "Míg a centrumban..., addig a periférián...",
                    "Mivel a centrumban..., azért a periférián...",
                    "Hogyha a centrumban..., akkor a periférián..."
                ], 0, ["c1-rhetorical-sociodemographic-adversatives"])
            ]
        },
        {
            "num": 4,
            "stem": f"c1-{slug}-04",
            "title": "Rural Resilience, Social Farming & Community Revitalization",
            "grammar_title": "Teleological Postpositional Phrases Formulating Structural Development Goals",
            "grammar_skill": "c1-modal-teleological-policy-syntax",
            "goals": [
                "I can analyze rural revitalization, community-supported agriculture, and local economic resilience (*társadalmi vállalkozás, helyi önellátás, szociális mezőgazdaság*).",
                "I can deploy teleological postpositional phrases to express systemic policy aims (*felszámolása céljából, felzárkóztatása érdekében, előmozdítására tekintettel*).",
                "I can evaluate grassroots community models that resist rural decline in Hungary."
            ],
            "vocab": [
                {"lemma": "helyi önellátás", "translation": "local self-sufficiency", "pos": "expression"},
                {"lemma": "szociális mezőgazdaság", "translation": "social farming", "pos": "expression"},
                {"lemma": "közösségi gazdaságfejlesztés", "translation": "community economic development", "pos": "expression"},
                {"lemma": "település-revitalizáció", "translation": "settlement revitalization", "pos": "expression"},
                {"lemma": "alulról szerveződő kezdeményezés", "translation": "grassroots initiative", "pos": "expression"},
                {"lemma": "helyi termelői piac", "translation": "local farmers' market", "pos": "expression"},
                {"lemma": "megtartó erő", "translation": "retaining capacity / holding power", "pos": "expression"},
                {"lemma": "társadalmi innováció", "translation": "social innovation", "pos": "expression"}
            ],
            "gr_text1": "Teleological formulation in regional development policy uses high-register postpositional phrases to express explicit developmental objectives: `megőrzése céljából / végett` (for the purpose of preserving), `felzárkóztatása érdekében` (in the interest of catching up), `előmozdítására tekintettel` (with a view to advancing), `helyreállítása szándékával` (with the intent of restoring).",
            "gr_text2": "Example: `A leszakadó térségek gazdasági felzárkóztatása érdekében az államnak nem segélyeket, hanem a helyi termelői közösségeket támogató beruházásokat kell finanszíroznia`.",
            "gr_table": [
                ["A falvak megtartó erejének növelése céljából új közösségi szövetkezeteket hoztak létre.", "For the purpose of increasing the holding power of villages, new community cooperatives were established."],
                ["A vidéki népesség helyben maradása érdekében helyi munkahelyteremtésre van szükség.", "In the interest of rural population remaining in place, local job creation is needed."],
                ["A biodiverzitás és az önellátás előmozdítására tekintettel szociális mintagazdaságok indultak.", "With a view to promoting biodiversity and self-sufficiency, social model farms were launched."]
            ],
            "world_story_seg": {
                "seg_slug": "revitalizacio",
                "title": "A talpra álló vidék: Helyi önellátás és a közösség ereje",
                "summary": "Highlighting inspiring grassroots models across Hungary (e.g. Alsómocsolád, Bicsérd, Cserdi) where social farming and community enterprise defied rural decay.",
                "paragraphs": [
                    {"type": "narration", "text": "A kilátástalanság árnyékában mégis születnek olyan csodák, amelyek megmutatják: a vidék nem halálra ítélt múzeum, hanem élő és cselekvőképes közösség. Az ormánsági és tolnai dombok között rejtőző falvakban – mint Alsómocsoládon vagy egykor Cserdiben – karizmatikus helyi vezetők és elkötelezett polgárok bizonyították be, hogy a külső segítség hiánya ellenére is van kiút a nyomorból."},
                    {"type": "narration", "text": "A siker kulcsa a szociális mezőgazdaság és a helyi önellátás volt. Az önkormányzatok a parlagon heverő földeken zöldségtermesztésbe és állattartásba kezdtek, feldolgozóüzemeket és hűtőházakat építettek, munkát és méltóságot adva a korábban reményvesztett közmunkásoknak. A falu saját bioélelmiszerrel látja el az óvodai és iskolai konyhákat, a felesleget pedig helyi termelői piacokon értékesíti. Ezek a társadalmi innovációk bebizonyították: a vidék jövője nem a lemondásban, hanem az önrendelkező közösségi összefogásban gyökerezik."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Mi a célja a 'szociális mezőgazdaságnak' (social farming) a hátrányos helyzetű térségekben?", [
                    "A helyi munkanélküliek és rászorulók bevonása a közösségi termelésbe, önellátást és értékteremtő munkát biztosítva számukra.",
                    "A szántóföldek beépítése raktárbázisokkal.",
                    "A mezőgazdasági gépek exportálása távoli országokba."
                ], 0, ["c1-tarsadalmireteg-vocab"]),
                fb("grammar", "controlled", "A falu megtartó erejének növelése _____ helyi munkahelyeket és bölcsődét hoztak létre. (for the purpose of / céljából)", "céljából", "For the purpose of increasing the village's holding power, they created local jobs and a nursery.", ["c1-modal-teleological-policy-syntax"]),
                match("vocabulary", "controlled", [["helyi önellátás", "élelmiszer- és energiaszükséglet helyi megtermelése"], ["megtartó erő", "a település képessége a lakosok helyben tartására"], ["társadalmi innováció", "közösségi problémák új típusú kreatív megoldása"], ["alulról szerveződő kezdeményezés", "polgárok által indított önkéntes összefogás"]], ["c1-tarsadalmireteg-vocab"]),
                fb("grammar", "practice", "A vidék elnéptelenedésének megállítása _____ komplex fejlesztési programra van szükség. (in the interest of / érdekében)", "érdekében", "In the interest of stopping rural depopulation, a complex development program is needed.", ["c1-modal-teleological-policy-syntax"]),
                sb("grammar", "practice", ["A", "közösségi", "összefogás", "a", "falu", "fennmaradása", "érdekében", "elengedhetetlen."], ["A", "közösségi", "összefogás", "a", "falu", "fennmaradása", "érdekében", "elengedhetetlen."], "Community solidarity in the interest of the village's survival is indispensable.", ["c1-modal-teleological-policy-syntax"]),
                dc("dialogue", [
                    {"speaker": "Falufejlesztő", "text": "Hogyan teremthetünk valódi autonómiát egy kistelepülésen?"},
                    {"speaker": "Polgármester", "text": "A helyi élelmiszer- és energia-önellátás megteremtése _____ kell minden erőforrást mozgósítanunk."},
                ], ["érdekében", "ellenére", "helyett"], 0, ["c1-modal-teleological-policy-syntax"]),
                sw("production", [{"prompt": "Write a policy proposal sentence about rural revitalization using 'érdekében' or 'céljából'.", "answer": "A falvak demográfiai hanyatlásának megállítása és a fiatal családok letelepedése érdekében az államnak decentralizált adókedvezményekkel kell ösztönöznie a helyi vállalkozásokat."}], ["c1-modal-teleological-policy-syntax"]),
                mc("grammar", "check", "Melyik névutós kifejezés fejez ki tudatos, szakpolitikai célkitűzést (teleological purpose)?", [
                    "céljából / érdekében",
                    "mellett",
                    "mögött"
                ], 0, ["c1-modal-teleological-policy-syntax"])
            ]
        },
        {
            "num": 5,
            "stem": f"c1-{slug}-05",
            "title": "Decentralization, Territorial Cohesion & The Future",
            "grammar_title": "Evaluative Polarization Particles Emphasizing Societal Fragmentation and Divergence",
            "grammar_skill": "c1-adv-evaluative-polarization-particles",
            "goals": [
                "I can articulate visionary decentralization strategies and territorial cohesion frameworks (*területi kohézió, decentralizáció, kiegyensúlyozott térszerkezet*).",
                "I can deploy evaluative polarization particles to emphasize critical divides (*egyértelműen, vitathatatlanul, drámai módon, feltartóztathatatlanul*).",
                "I can synthesize debates on federalism, regional autonomy, and counterbalancing Budapest's dominance."
            ],
            "vocab": [
                {"lemma": "területi kohézió", "translation": "territorial cohesion", "pos": "expression"},
                {"lemma": "decentralizáció", "translation": "decentralization", "pos": "noun"},
                {"lemma": "kiegyensúlyozott térszerkezet", "translation": "balanced spatial structure", "pos": "expression"},
                {"lemma": "régióközpont", "translation": "regional center / hub", "pos": "noun"},
                {"lemma": "helyi autonómia", "translation": "local autonomy / self-government", "pos": "expression"},
                {"lemma": "felzárkóztatási stratégia", "translation": "catch-up / cohesion strategy", "pos": "expression"},
                {"lemma": "társadalmi integráció", "translation": "social integration", "pos": "expression"},
                {"lemma": "fenntartható vidék", "translation": "sustainable countryside", "pos": "expression"}
            ],
            "gr_text1": "To formulate urgent strategic verdicts in regional development, evaluative polarization particles amplify the necessity of reform: `egyértelműen` (unambiguously/clearly), `vitathatatlanul` (undisputedly), `drámai módon` (in a dramatic manner), `feltartóztathatatlanul` (unstoppably).",
            "gr_text2": "Example: `A jelenlegi központosító politika, vitathatatlanul, drámai módon mélyíti a főváros és a vidék közötti szakadékot; egyértelműen szükség van a valódi decentralizációra`.",
            "gr_table": [
                ["A területi egyenlőtlenségek, vitathatatlanul, veszélyeztetik a nemzet egységét és stabilitását.", "Territorial inequalities, undisputedly, endanger the unity and stability of the nation."],
                ["A falvak elnéptelenedése feltartóztathatatlanul zajlik, hacsak nem történik radikális beavatkozás.", "The depopulation of villages is proceeding unstoppably, unless radical intervention occurs."],
                ["Egyértelműen bizonyított, hogy a centralizáció gyengíti a helyi közösségek önvédelmi képességét.", "It is clearly proven that centralization weakens local communities' self-defense capacity."]
            ],
            "world_story_seg": {
                "seg_slug": "jovo",
                "title": "A kiegyensúlyozott haza: Decentralizáció és a jövő térképe",
                "summary": "Synthesizing the historic imperative for true decentralization, empowering secondary regional cities (Debrecen, Szeged, Győr, Pécs), and safeguarding the countryside.",
                "paragraphs": [
                    {"type": "narration", "text": "Magyarország huszonegyedik századi sorsa azon áll vagy bukik, hogy képes-e felszámolni a feudális gyökerű vízfej-szindrómát. A modern európai tapasztalatok azt mutatják: egyetlen nemzet sem maradhat sikeres és virágzó, ha területének kilencven százalékát pusztán nyersanyagforrásnak vagy üdülőövezetnek tekinti, miközben a teljes szellemi és gazdasági tőkét egyetlen megapoliszba zsúfolja össze."},
                    {"type": "narration", "text": "A megoldás a bátor és következetes decentralizáció: a valódi pénzügyi és döntési autonómia visszaadása az önkormányzatoknak, valamint a regionális ellenpólusok – Győr, Pécs, Szeged, Debrecen és Miskolc – megerősítése. A kiegyensúlyozott térszerkezet megteremtése nemcsak gazdasági hatékonysági kérdés, hanem a polgári demokrácia legmélyebb fundamentuma: mert az a nemzet, amely elveszíti a vidékét, elkerülhetetlenül elveszíti saját kulturális gyökereit és jövőjét is."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Mit jelent a 'kiegyensúlyozott térszerkezet' (balanced spatial structure) eszménye?", [
                    "Olyan országos hálózatot, ahol a gazdasági erő, az oktatás és a minőségi életfeltételek több erős regionális pólus között oszlanak meg, nem pedig egyetlen városban összpontosulnak.",
                    "A vasúti talpfák vízszintezését a vágányokon.",
                    "A házak homlokzatának kötelezően egyforma színre festését."
                ], 0, ["c1-tarsadalmireteg-vocab"]),
                fb("grammar", "controlled", "A decentralizáció hiánya, _____ gátolja a vidéki nagyvárosok nemzetközi felemelkedését. (undisputedly / vitathatatlanul)", "vitathatatlanul", "The lack of decentralization, undisputedly, hinders the international rise of regional cities.", ["c1-adv-evaluative-polarization-particles"]),
                match("vocabulary", "controlled", [["területi kohézió", "a térségek közötti egyenlőtlenségek csökkentése"], ["decentralizáció", "hatáskörök és pénzek átadása a helyi szinteknek"], ["régióközpont", "térségi gazdasági és kulturális központ"], ["helyi autonómia", "a település joga saját ügyei önálló intézésére"]], ["c1-tarsadalmireteg-vocab"]),
                fb("grammar", "practice", "A kutatási adatok alapján _____ látszik, hogy a helyi autonómia erősíti a gazdaságot. (clearly / egyértelműen)", "egyértelműen", "Based on research data it clearly appears that local autonomy strengthens the economy.", ["c1-adv-evaluative-polarization-particles"]),
                sb("grammar", "practice", ["A", "decentralizáció", "vitathatatlanul", "a", "fejlődés", "legfőbb", "záloga."], ["A", "decentralizáció", "vitathatatlanul", "a", "fejlődés", "legfőbb", "záloga."], "Decentralization is undisputedly the foremost pledge of development.", ["c1-adv-evaluative-polarization-particles"]),
                dc("dialogue", [
                    {"speaker": "Urbanista", "text": "Hogyan teremthetünk valóban kiegyensúlyozott térszerkezetet?"},
                    {"speaker": "Közgazdász", "text": "Egyértelműen a vidéki egyetemi pólusok és az önkormányzati pénzügyi _____ megerősítésével."},
                ], ["autonómia", "függés", "adósság"], 0, ["c1-adv-evaluative-polarization-particles"]),
                sw("production", [{"prompt": "Write a concluding argument on territorial cohesion using 'vitathatatlanul' or 'egyértelműen'.", "answer": "A valódi területi kohézió megteremtése, vitathatatlanul, nem puszta gazdaságpolitikai feladat, hanem a magyar nemzeti szolidaritás és a demokratikus jogállamiság alapvető próbája."}], ["c1-adv-evaluative-polarization-particles"]),
                mc("grammar", "check", "Melyik partikula szolgál a szakpolitikai állítás megkérdőjelezhetetlenségének nyomatékosítására?", [
                    "vitathatatlanul / egyértelműen",
                    "valószínűleg talán",
                    "csekély eséllyel"
                ], 0, ["c1-adv-evaluative-polarization-particles"])
            ]
        }
    ]

    for l in disc_lessons:
        emit_instructional_lesson(19, "discourse", l, disc_title, disc_intro if l["num"] == 1 else None)

    # Combined Discourse World Story
    write_json(
        f"stories/world/c1/c1-{slug}.json",
        {
            "id": f"story.c1.{slug}",
            "title": "A vízfej és a végek: Térbeli egyenlőtlenségek, leszakadó vidék és a jövő esélyei",
            "level": "C1",
            "type": "world",
            "order": 19,
            "lesson": 5,
            "estimatedMinutes": 8,
            "summary": "Panoramic exploration of Hungary's territorial divide: the extreme centralization of Budapest ('vízfej'), transport poverty and rail line closures in dead-end villages, healthcare and educational deserts, grassroots social farming revivals, and the imperative for democratic decentralization.",
            "grammar": [
                "c1-discourse-spatial-disparity-markers",
                "c1-adv-concessive-spatial-correlatives",
                "c1-rhetorical-sociodemographic-adversatives",
                "c1-modal-teleological-policy-syntax",
                "c1-adv-evaluative-polarization-particles"
            ],
            "vocabularyTopics": [
                "Center vs. Periphery: Spatial Inequalities & Rural Transformations",
                "Budapest Primacy, The 'Waterhead' & Regional Disconnect",
                "Transport Poverty, Rail Line Closures & Mobility Traps",
                "Welfare Deserts: Healthcare & Educational Disparities",
                "Rural Resilience, Social Farming & Community Revitalization",
                "Decentralization, Territorial Cohesion & The Future"
            ],
            "paragraphs": [
                {"type": "narration", "text": "Magyarország térszerkezetét több mint egy évszázada egyetlen gigantikus aszimmetria határozza meg: a főváros és a vidék közötti mély, sokszor áthidalhatatlannak tűnő szakadék. Miközben Budapest az ország vitathatatlan gazdasági, intellektuális és kulturális motorja, a 'vízfej' szindróma a hátország lassú elsorvadásához vezetett. Az erőforrások és a képzett munkaerő folyamatos elszívása miatt a külső régiók kiszolgáltatott perifériákká váltak."},
                {"type": "narration", "text": "A perifériák válsága a mindennapi mobilitás terén a legkézzelfoghatóbb: a vasúti szárnyvonalak bezárása és a buszközlekedés leépítése közlekedési szegénységbe taszította a zsákfalvak tízezreit. A fizikailag elzárt településeken megszűnt a helyi posta, az iskola és a háziorvosi rendelő; a felnövekvő generációk így már születésük pillanatában halmozottan hátrányos helyzetbe kerülnek a centrum lakóihoz képest."},
                {"type": "narration", "text": "A felülről vezérelt tehetetlenség ellenére a vidéki Magyarország mégsem mondott le a jövőjéről: az alulról szerveződő szociális mintagazdaságok, a helyi termelői szövetkezetek és az önellátó falumodellek bizonyítják, hogy a közösségi szolidaritás képes életet lehelni a legreménytelenebbnek hitt tájakba is. Ahol az önkormányzatok visszaszerzik a döntési autonómiát, ott újra megteremthető a falu megtartó ereje."},
                {"type": "narration", "text": "Mindent egybevetve, a huszonegyedik századi Magyarország nem maradhat fenn a vidék feláldozása árán. A nemzeti integráció és a demokratikus stabilitás alapköve a valódi területi kohézió: egy olyan kiegyensúlyozott térszerkezet, amelyben az erős vidéki egyetemi központok és az önrendelkező helyi közösségek garantálják, hogy a szülőföldön való boldogulás joga ne csupán a fővárosi elit kiváltsága legyen, hanem minden magyar polgár elidegeníthetetlen valósága."}
            ]
        }
    )

    # Discourse Consolidation
    emit_consolidation_lesson(
        19,
        "discourse",
        f"c1-{slug}-consolidation",
        disc_title,
        [
            "I can analyze regional disparities, capital city primacy, and transport poverty in Hungary.",
            "I can evaluate welfare deserts, unfilled GP practices, and school segregation in peripheral areas.",
            "I can debate grassroots social farming models, local economic resilience, and decentralization policy."
        ],
        [
            mc("grammar", "recognize", "Milyen szerkezettel fejezhetünk ki éles területi gazdasági különbséget?", [
                "markáns szakadék tátong / éles cezúra feszül / mély törésvonal húzódik",
                "mivel egyhangúlag elfogadták a költségvetést",
                "amikor szép napos idő van a faluban"
            ], 0, ["c1-discourse-spatial-disparity-markers"]),
            mc("grammar", "recognize", "Milyen kifejezésekkel írhatunk le tudatos szakpolitikai fejlesztési célt?", [
                "a megtartó erő növelése céljából / a felzárkóztatás érdekében",
                "anélkül, hogy megkérdezték volna őket",
                "hogyha elutaznak a fővárosba"
            ], 0, ["c1-modal-teleological-policy-syntax"]),
            match("vocabulary", "recognize", [["fővárosi vízfej", "Budapest aránytalan centralizációja"], ["közlekedési szegénység", "mobilitáshiány miatti elszigeteltség"], ["ellátási sivatag", "alapvető orvosi és iskolai hiány"], ["helyi önellátás", "közösségi szociális mezőgazdaság"], ["területi kohézió", "régiók közötti egyensúly eszménye"]], ["c1-tarsadalmireteg-vocab"]),
            fb("vocabulary", "recall", "A vasúti szárnyvonalak felszámolása miatt sok kistelepülés fizikai _____ vált. (mobility trap / közlekedési szegénységbe)", "közlekedési szegénységbe", "Due to the abolition of branch railway lines many small settlements fell into transport poverty.", ["c1-tarsadalmireteg-vocab"]),
            fb("vocabulary", "recall", "A kistelepülések elnéptelenedésének megállításához a falu belső _____ kell megerősíteni. (retaining capacity / megtartó erejét)", "megtartó erejét", "To stop the depopulation of small settlements, the village's internal retaining capacity must be strengthened.", ["c1-tarsadalmireteg-vocab"]),
            fb("grammar", "recall", "_____ utazunk a perifériákon, mindenütt az elvándorlás nyomaival találkozunk. (Wherever / Bárhová)", "Bárhová", "Wherever we travel in the peripheries, everywhere we encounter the traces of out-migration.", ["c1-adv-concessive-spatial-correlatives"]),
            fb("grammar", "context", "Míg a fővárosban bőséges az orvosválaszték, _____ a perifériákon praxisok százai állnak üresen. (meanwhile / addig)", "addig", "While in the capital doctor choice is plentiful, meanwhile in peripheries hundreds of practices stand empty.", ["c1-rhetorical-sociodemographic-adversatives"]),
            fb("grammar", "context", "A területi kohézió megteremtése, _____ az ország belső békéjének záloga. (undisputedly / vitathatatlanul)", "vitathatatlanul", "Creating territorial cohesion, undisputedly, is the pledge of the country's internal peace.", ["c1-adv-evaluative-polarization-particles"]),
            mc("grammar", "context", "Mi a funkciója a 'Míg... addig...' ellentétezésnek a centrum-periféria elemzésekben?", [
                "Párhuzamosan és plasztikusan szembesíti a fővárosi kiváltságokat a vidéki szolgáltatáshiánnyal.",
                "Megváltoztatja a vitatott törvénytervezet szövegét.",
                "Elnézést kér az olvasótól a statisztikai adatok miatt."
            ], 0, ["c1-rhetorical-sociodemographic-adversatives"]),
            sb("grammar", "produce", ["A", "vidék", "megtartó", "ereje", "a", "nemzet", "jövőjének", "záloga."], ["A", "vidék", "megtartó", "ereje", "a", "nemzet", "jövőjének", "záloga."], "The countryside's holding power is the pledge of the nation's future.", ["c1-adv-evaluative-polarization-particles"]),
            sw("production", [{"prompt": "Write a critical diagnostic sentence about regional inequalities using 'markáns szakadék tátong'.", "answer": "A budapesti agglomeráció és az északkeleti aprófalvak között markáns szakadék tátong, amely aláássa a társadalmi kohéziót és az esélyegyenlőséget."}], ["c1-discourse-spatial-disparity-markers"]),
            sw("production", [{"prompt": "Formulate a concluding thought on decentralization and the future of the Hungarian countryside.", "answer": "Vitathatatlanul a bátor decentralizáció és a helyi önkormányzatiság megerősítése jelenti az egyetlen járható utat egy virágzó és kiegyensúlyozott haza megteremtéséhez."}], ["c1-adv-evaluative-polarization-particles"])
        ]
    )

    print("=== Finished C1 Unit 19 ===")


if __name__ == "__main__":
    generate_unit_19()
