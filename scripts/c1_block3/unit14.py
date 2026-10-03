#!/usr/bin/env python3
"""
Hungarian C1 Block 3 - Unit 14 Generator:
  - Track 1 (Core): Unit 14 — "Ecological System Dynamics, Energy Transition & Green Taxonomy" (c1-14)
  - Track 2 (Discourse): Unit 14 — "Nuclear Energy, the Paks Dilemma & Renewables in the Carpathian Basin" (c1-energetika)
"""

import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT))

from scripts.c1_block1.common import mc, match, fb, sb, dc, sw, write_json, emit_instructional_lesson, emit_consolidation_lesson
from scripts.c1_block3.registry_helper import register_unit


def generate_unit_14():
    print("=== Generating C1 Unit 14 ===")
    
    # Register skills & titles
    new_skills = {
        "c1-14-vocab": {"kind": "vocabulary"},
        "c1-energetika-vocab": {"kind": "vocabulary"},
        "c1-ecological-system-dynamics": {"kind": "grammar"},
        "c1-energy-transition-clauses": {"kind": "grammar"},
        "c1-green-taxonomy-criteria": {"kind": "grammar"},
        "c1-nuclear-governance": {"kind": "grammar"},
        "c1-circular-economy-syntax": {"kind": "grammar"},
    }
    new_titles = {
        "c1-14-vocab": "reading",
        "c1-energetika-vocab": "reading",
        "c1-ecological-system-dynamics": "ecological system dynamics environmental degradation and resilience predicates",
        "c1-energy-transition-clauses": "decarbonization pathways renewable energy penetration and grid balancing",
        "c1-green-taxonomy-criteria": "sustainable finance environmental taxonomy and non financial reporting standards",
        "c1-nuclear-governance": "nuclear safety regulatory licensing and long term radioactive waste management",
        "c1-circular-economy-syntax": "circular economy resource loops and lifecycle assessment terminology",
    }
    
    core_title = "Ecological System Dynamics, Energy Transition & Green Taxonomy"
    core_stems = [f"c1-14-0{i}" for i in range(1, 6)] + ["c1-14-consolidation"]
    disc_title = "Nuclear Energy, the Paks Dilemma & Renewables in the Carpathian Basin"
    disc_stems = [f"c1-energetika-0{i}" for i in range(1, 6)] + ["c1-energetika-consolidation"]
    
    register_unit(14, core_title, core_stems, disc_title, disc_stems, new_skills, new_titles)

    # ----------------------------------------------------
    # TRACK 1: CORE (c1-14)
    # ----------------------------------------------------
    core_intro = [
        "Ecological sustainability, energy transition, and green finance terminology in Hungarian employ specialized systemic syntax (ökoszisztéma-szolgáltatások degradációja, karbontalanítási pálya, zöld taxonómia), precise participial causals, and technical environmental predicates.",
        "In this unit, inspired by István Fekete's profound ecological contemplation of wetland ecosystems in 'Tüskevár' and 'Csend' (1957–1965), you will master environmental impact assessment, decarbonization policy, and sustainable finance taxonomy in elevated C1 Hungarian."
    ]

    core_lessons = [
        {
            "num": 1,
            "stem": "c1-14-01",
            "title": "Ecological System Dynamics & Biodiversity Degradation",
            "grammar_title": "Environmental Systems, Resilience and Ecological Predicates",
            "grammar_skill": "c1-ecological-system-dynamics",
            "goals": [
                "I can analyze ecosystem services and biodiversity indicators (*ökoszisztéma-szolgáltatás, fajdiverzitás, élőhelyfragmentáció*).",
                "I can formulate environmental causality using participial chains (*hozzájárulva a talajerózióhoz, veszélyeztetve az őshonos flórát*).",
                "I can evaluate ecological resilience in academic Hungarian."
            ],
            "vocab": [
                {"lemma": "ökoszisztéma-szolgáltatás", "translation": "ecosystem service", "pos": "noun"},
                {"lemma": "biodiverzitás", "translation": "biodiversity, species richness", "pos": "noun"},
                {"lemma": "élőhelyfragmentáció", "translation": "habitat fragmentation", "pos": "noun"},
                {"lemma": "talajerózió", "translation": "soil erosion", "pos": "noun"},
                {"lemma": "vízvisszatartás", "translation": "water retention", "pos": "noun"},
                {"lemma": "özönfaj", "translation": "invasive species", "pos": "noun"},
                {"lemma": "reziliencia", "translation": "ecological resilience, recovery capacity", "pos": "noun"},
                {"lemma": "degradáció", "translation": "environmental degradation", "pos": "noun"}
            ],
            "gr_text1": "Ecosystem and environmental prose links causal and consequence clauses via adverbial participles (*-va/-ve*, *-ván/-vén*): `A folyószabályozás drasztikusan lecsökkentette a hullámterek kiterjedését, visszafordíthatatlan károkat okozva az ártéri élővilágban`.",
            "gr_text2": "Abstract technical terms deploy compound nominal prefixes expressing ecological systemic interactions: `élőhelyfragmentáció`, `fajdiverzitás-csökkenés`, `talajpusztulás-kockázat`.",
            "gr_table": [
                ["A vizes élőhelyek megőrzése létfontosságú a biodiverzitás szempontjából.", "Preserving wetlands is vital from the perspective of biodiversity."],
                ["Az élőhelyek feldarabolódása megnehezíti az őshonos fajok vándorlását.", "Habitat fragmentation hinders the migration of native species."],
                ["A táj természetes vízvisszatartó képessége csökkenti az aszálykárokat.", "The natural water retention capacity of the landscape mitigates drought damage."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mit jelent a 'reziliencia' az ökológiai rendszerekben?", ["A természetes rendszerek azon képességét, hogy külső zavarok vagy sokkok után helyreállítsák működési egyensúlyukat.", "A fák magasságának mérőszámát.", "A kémiai növényvédő szerek mérgező hatását."], 0, ["c1-14-vocab"]),
                fb("grammar", "controlled", "A monokultúrás mezőgazdasági művelés súlyos mértékben hozzájárult a talaj termőképességének _____. (degradation / degradációjához)", "degradációjához", "Monoculture agricultural cultivation contributed heavily to the degradation of soil fertility.", ["c1-ecological-system-dynamics"]),
                match("vocabulary", "controlled", [["biodiverzitás", "fajgazdagság"], ["élőhelyfragmentáció", "természetes területek széttagolódása"], ["vízvisszatartás", "tájban való nedvességmegőrzés"], ["özönfaj", "agresszíven terjedő jövevényfaj"]], ["c1-14-vocab"]),
                fb("grammar", "practice", "A folyók gátak közé szorítása drasztikusan lecsökkentette az ártéri erdők _____ képességét. (water retention / vízvisszatartó)", "vízvisszatartó", "Confining rivers between dykes drastically reduced the water retention capacity of floodplain forests.", ["c1-ecological-system-dynamics"]),
                sb("grammar", "practice", ["A", "természetes", "élőhelyek", "megóvása", "alapfeltétele", "a", "Kárpát-medence", "ökológiai", "stabilitásának."], ["A", "természetes", "élőhelyek", "megóvása", "alapfeltétele", "a", "Kárpát-medence", "ökológiai", "stabilitásának."], "Preserving natural habitats is the prerequisite of the Carpathian Basin's ecological stability.", ["c1-ecological-system-dynamics"]),
                dc("dialogue", [
                    {"speaker": "Ökológus", "text": "Hogyan védekezhetünk a szélsőséges aszályok pusztítása ellen?"},
                    {"speaker": "Hidrológus", "text": "A víz gyors elvezetése helyett a táji szintű _____ stratégiáját kell alkalmaznunk."},
                ], ["vízvisszatartás", "fakivágás", "betonozás"], 0, ["c1-ecological-system-dynamics"]),
                sw("production", [{"prompt": "Write an environmental statement linking habitat fragmentation to biodiversity loss.", "answer": "Az intenzív infrastruktúra-fejlesztés okozta élőhelyfragmentáció elszigeteli a vadállomány populációit, felgyorsítva a genetikai leromlást és a helyi biodiverzitás csökkenését."}], ["c1-ecological-system-dynamics"]),
                mc("grammar", "check", "Melyik állítás írja le helyesen az ökoszisztéma-szolgáltatások fogalmát?", [
                    "A természet által a társadalom számára biztosított ingyenes javak és funkciók összessége (pl. tiszta ivóvíz, beporzás, szén-dioxid-megkötés).",
                    "A nemzeti parkok belépődíjaiból származó bevétel.",
                    "A faipari vállalatok által fizetett környezetvédelmi bírság."
                ], 0, ["c1-ecological-system-dynamics"])
            ]
        },
        {
            "num": 2,
            "stem": "c1-14-02",
            "title": "Decarbonization Pathways & Renewable Grid Integration",
            "grammar_title": "Energy Transition Metrics, Grid Balancing and Intermittent Sources",
            "grammar_skill": "c1-energy-transition-clauses",
            "goals": [
                "I can analyze energy transition pathways (*karbontalanítás, energiamix, hálózatkiegyenlítés*).",
                "I can evaluate technical integration of intermittent renewables (*időjárásfüggő megújulók, napenergia-csúcs*).",
                "I can discuss electricity grid flexibility and storage capacity in formal technical Hungarian."
            ],
            "vocab": [
                {"lemma": "karbontalanítás", "translation": "decarbonization", "pos": "noun"},
                {"lemma": "energiamix", "translation": "energy mix, power generation portfolio", "pos": "noun"},
                {"lemma": "hálózatkiegyenlítés", "translation": "grid balancing / balancing power reserves", "pos": "noun"},
                {"lemma": "időjárásfüggő megújuló", "translation": "weather-dependent / intermittent renewable", "pos": "expression"},
                {"lemma": "csúcsfogyasztás", "translation": "peak consumption / peak load", "pos": "noun"},
                {"lemma": "energiatárolás", "translation": "energy storage, battery storage", "pos": "noun"},
                {"lemma": "rendszerirányító", "translation": "Transmission System Operator (TSO / MAVIR)", "pos": "noun"},
                {"lemma": "rugalmassági deficit", "translation": "flexibility deficit", "pos": "noun"}
            ],
            "gr_text1": "Energy transition discourse employs technical conditional clauses balancing volatile production against demand: `Amennyiben a fotovoltaikus kapacitások meghaladják az azonnali fogyasztást, a rendszerirányítónak szabályozó kapacitásokat kell bevetnie a frekvencia stabilitásának megőrzésére`.",
            "gr_text2": "Notice the use of instrumental-delative phrases expressing system transitions: `a fosszilis energiahordozókról a zéró kibocsátású forrásokra való áttérés révén` (by means of transitioning from fossil fuels to zero-emission sources).",
            "gr_table": [
                ["A naperőművek gyors terjedése kihívás elé állítja a hálózatirányítót.", "The rapid expansion of solar power plants challenges the grid operator."],
                ["Az energiatárolási kapacitások kiépítése elengedhetetlen a zöld átálláshoz.", "Building out energy storage capacities is indispensable for the green transition."],
                ["A szén-dioxid-kibocsátásmentes energiamix garantálja az ellátásbiztonságot.", "A carbon-free energy mix guarantees security of supply."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Miért jelent technológiai kihívást az időjárásfüggő megújulók (nap- és szélenergia) hálózati integrációja?", ["Mert a termelés ingadozása nem követi a fogyasztási igényeket, így gyors reagálású kiegyenlítő kapacitásokat igényel.", "Mert a zöld áram nem vezeti az elektromosságot.", "Mert a napelemek elhasználják a napfényt."], 0, ["c1-14-vocab"]),
                fb("grammar", "controlled", "A napenergia-termelés hirtelen megugrása komoly _____ feladatot ró a magyar villamosenergia-rendszer irányítójára. (grid balancing / hálózatkiegyenlítési)", "hálózatkiegyenlítési", "The sudden surge in solar power generation imposes a serious grid balancing task on the Hungarian power grid operator.", ["c1-energy-transition-clauses"]),
                match("vocabulary", "controlled", [["karbontalanítás", "kibocsátáscsökkentés"], ["energiamix", "energiaforrások megoszlása"], ["rendszerirányító", "villamosenergia-hálózat felügyelője"], ["energiatárolás", "akkumulátoros tartalékképzés"]], ["c1-14-vocab"]),
                fb("grammar", "practice", "A klímasemlegességi célok eléréséhez elengedhetetlen a fosszilis energiahordozók kivezetése és az _____ zöldítése. (energy mix / energiamix)", "energiamix", "To achieve climate neutrality targets, phasing out fossil fuels and greening the energy mix are indispensable.", ["c1-energy-transition-clauses"]),
                sb("grammar", "practice", ["Az", "akkumulátoros", "tárolók", "elengedhetetlenek", "a", "hálózati", "rugalmasság", "biztosításához."], ["Az", "akkumulátoros", "tárolók", "elengedhetetlenek", "a", "hálózati", "rugalmasság", "biztosításához."], "Battery storage units are indispensable for ensuring grid flexibility.", ["c1-energy-transition-clauses"]),
                dc("dialogue", [
                    {"speaker": "Energetikus", "text": "Hogyan kezelhető a déli órákban fellépő hatalmas áramtermelési csúcs?"},
                    {"speaker": "Mérnök", "text": "Ipari méretű tárolókkal és a dinamikus fogyasztói _____ ösztönzésével."},
                ], ["kereslet", "korlátozás", "hiány"], 0, ["c1-energy-transition-clauses"]),
                sw("production", [{"prompt": "Write a sentence analyzing grid balancing challenges with intermittent renewables.", "answer": "Az időjárásfüggő megújulók robbanásszerű integrációja a villamosenergia-hálózatba rugalmassági deficitet idéz elő, amit csak korszerű energiatárolási és hálózatkiegyenlítő rendszerekkel lehet orvosolni."}], ["c1-energy-transition-clauses"]),
                mc("grammar", "check", "Mit takar a 'villamosenergia-rendszerirányító' (TSO / MAVIR) feladatköre?", [
                    "A termelés és a fogyasztás másodpercről másodpercre történő egyensúlyban tartását és a hálózati frekvencia biztosítását.",
                    "A lakossági villanyszámlák postázását.",
                    "Új szénbányák megnyitását."
                ], 0, ["c1-energy-transition-clauses"])
            ]
        },
        {
            "num": 3,
            "stem": "c1-14-03",
            "title": "Green Taxonomy, ESG Standards & Sustainable Finance",
            "grammar_title": "EU Taxonomy Criteria, Non-Financial Reporting and Greenwashing Defense",
            "grammar_skill": "c1-green-taxonomy-criteria",
            "goals": [
                "I can analyze the EU Green Taxonomy framework (*taxonómia-rendelet, zöldrefestés, fenntarthatósági jelentéstétel*).",
                "I can evaluate ESG metrics (*környezeti, társadalmi és vállalatirányítási szempontok*).",
                "I can formulate green capital allocation criteria in formal financial Hungarian."
            ],
            "vocab": [
                {"lemma": "taxonómia-rendelet", "translation": "EU Taxonomy Regulation", "pos": "noun"},
                {"lemma": "zöldrefestés", "translation": "greenwashing (misleading environmental claims)", "pos": "noun"},
                {"lemma": "fenntarthatósági jelentéstétel", "translation": "sustainability reporting (CSRD)", "pos": "expression"},
                {"lemma": "zöldkötvény", "translation": "green bond", "pos": "noun"},
                {"lemma": "éghajlatváltozás mérséklése", "translation": "climate change mitigation", "pos": "expression"},
                {"lemma": "jelentős károkozás elkerülése", "translation": "Do No Significant Harm (DNSH principle)", "pos": "expression"},
                {"lemma": "tőkeallokáció", "translation": "capital allocation", "pos": "noun"},
                {"lemma": "karbonlábnyom", "translation": "carbon footprint", "pos": "noun"}
            ],
            "gr_text1": "Sustainable finance in the EU and Hungary operates within the strict criteria of the EU Taxonomy Regulation. A business activity qualifies as environmentally sustainable only if it contributes substantially to at least one environmental objective while complying with the *jelentős károkozás elkerülése* (Do No Significant Harm - DNSH) principle.",
            "gr_text2": "Syntactically, texts employ precise normative qualifiers: `Kizárólag azon beruházások sorolhatók a zöld taxonómia hatálya alá, amelyek objektív tudományos mérőszámokkal igazolják kibocsátáscsökkentési potenciáljukat`.",
            "gr_table": [
                ["A taxonómia-rendelet célja a tőkeáramlások fenntartható projektek felé terelése.", "The aim of the Taxonomy Regulation is channeling capital flows toward sustainable projects."],
                ["A vállalatok kötelesek auditált fenntarthatósági jelentéstételt közzétenni.", "Companies are required to publish audited sustainability reporting."],
                ["A szigorú átvilágítás védi a befektetőket a zöldrefestés kockázatától.", "Strict due diligence protects investors from the risk of greenwashing."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mit jelent a 'zöldrefestés' (greenwashing) fogalma a pénzügyi piacokon?", ["Olyan megtévesztő marketinggyakorlatot, amely egy vállalatot környezetbarátnak tüntet fel anélkül, hogy valós ökológiai intézkedéseket tenne.", "Az épületek környezetbarát zöld festékkel történő mázolását.", "A parkosítás költségeinek elszámolását."], 0, ["c1-14-vocab"]),
                fb("grammar", "controlled", "A beruházás minősítésekor kötelezően alkalmazni kell a 'jelentős károkozás _____' (DNSH) szigorú elvét. (avoidance / elkerülésének)", "elkerülésének", "When evaluating the investment, the strict principle of 'Do No Significant Harm' (DNSH) must be applied.", ["c1-green-taxonomy-criteria"]),
                match("vocabulary", "controlled", [["taxonómia-rendelet", "zöld gazdasági tevékenységek uniós osztályozása"], ["zöldrefestés", "félrevezető környezeti állítások"], ["zöldkötvény", "klímacélokat finanszírozó értékpapír"], ["karbonlábnyom", "üvegházhatású gázkibocsátás mértéke"]], ["c1-14-vocab"]),
                fb("grammar", "practice", "Az MNB által meghirdetett zöld tőkekövetelmény-kedvezmény a környezetileg fenntartható _____ ösztönzi. (lending / hitelezést)", "hitelezést", "The green capital requirement discount announced by the MNB incentivizes environmentally sustainable lending.", ["c1-green-taxonomy-criteria"]),
                sb("grammar", "practice", ["A", "fenntarthatósági", "jelentéstétel", "kötelezővé", "vált", "a", "nagyvállalatok", "számára."], ["A", "fenntarthatósági", "jelentéstétel", "kötelezővé", "vált", "a", "nagyvállalatok", "számára."], "Sustainability reporting has become mandatory for large corporations.", ["c1-green-taxonomy-criteria"]),
                dc("dialogue", [
                    {"speaker": "Befektető", "text": "Hogyan bizonyosodhatok meg arról, hogy a kötvénykibocsátó valóban zöld projektet finanszíroz?"},
                    {"speaker": "Bankár", "text": "A független szakértői vélemény és az uniós _____ való megfelelés vizsgálatával."},
                ], ["taxonómiának", "hirdetésnek", "árfolyamnak"], 0, ["c1-green-taxonomy-criteria"]),
                sw("production", [{"prompt": "Write a sentence defining the DNSH principle in sustainable corporate finance.", "answer": "Az uniós taxonómia értelmében egy gazdasági tevékenység csak akkor minősül fenntarthatónak, ha érdemben hozzájárul a klímacélokhoz, miközben nem sérti a jelentős károkozás elkerülésének elvét más környezeti célok tekintetében."}], ["c1-green-taxonomy-criteria"]),
                mc("grammar", "check", "Mi az ESG-szempontok (Environmental, Social, Governance) lényege a vállalatértékelésben?", [
                    "A pénzügyi mutatókon túlmenően a környezeti lábnyom, a társadalmi felelősség és az átlátható cégvezetés együttes vizsgálata.",
                    "A dolgozók kötelező heti sportolásának ellenőrzése.",
                    "A külföldi devizaszámlák könyvelése."
                ], 0, ["c1-green-taxonomy-criteria"])
            ]
        },
        {
            "num": 4,
            "stem": "c1-14-04",
            "title": "Nuclear Safety Governance & Radioactive Waste Lifecycle",
            "grammar_title": "Nuclear Regulatory Oversight, Operational Licensing and Deep Geological Repositories",
            "grammar_skill": "c1-nuclear-governance",
            "goals": [
                "I can analyze nuclear safety governance (*Országos Atomenergia Hivatal, üzemidő-hosszabbítás, nukleáris biztonság*).",
                "I can evaluate radioactive waste management (*mélységi geológiai tároló, kiégett fűtőelemek*).",
                "I can articulate environmental risk assessment and radiation protection in formal Hungarian."
            ],
            "vocab": [
                {"lemma": "Országos Atomenergia Hivatal", "translation": "Hungarian Atomic Energy Authority (OAH)", "pos": "noun"},
                {"lemma": "üzemidő-hosszabbítás", "translation": "lifetime extension / license extension", "pos": "noun"},
                {"lemma": "kiégett fűtőelem", "translation": "spent fuel element / assembly", "pos": "noun"},
                {"lemma": "mélységi geológiai tároló", "translation": "deep geological repository", "pos": "noun"},
                {"lemma": "nukleáris biztonság", "translation": "nuclear safety", "pos": "noun"},
                {"lemma": "sugárvédelem", "translation": "radiation protection", "pos": "noun"},
                {"lemma": "leszerelés", "translation": "decommissioning (reactor)", "pos": "noun"},
                {"lemma": "alapterhelés", "translation": "baseload power generation", "pos": "noun"}
            ],
            "gr_text1": "Nuclear safety legislation requires rigorous causal and passive modal syntax: `Az üzemidő-hosszabbítás feltétele a reaktortartály anyagfáradásának és a biztonsági rendszerek integritásának kimerítő felülvizsgálata az atomenergia-felügyelet által`.",
            "gr_text2": "Phrases concerning final waste disposal deploy high-precision geological terminology: `a nagy aktivitású radioaktív hulladékok végleges elhelyezése stabil mélységi agyagkő formációkban`.",
            "gr_table": [
                ["A nukleáris biztonság abszolút elsőbbséget élvez minden gazdasági szemponttal szemben.", "Nuclear safety enjoys absolute priority over all economic considerations."],
                ["A kiégett fűtőelemek kezelése több százezer éves felelősséget jelent.", "Management of spent fuel assemblies represents hundreds of thousands of years of responsibility."],
                ["A mélységi geológiai tároló helyszínének kiválasztása szigorú kutatásokon alapszik.", "Selecting the site of the deep geological repository rests upon rigorous research."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mi az Országos Atomenergia Hivatal (OAH) legfőbb közjogi feladata?", ["A nukleáris létesítmények és a radioaktív anyagok biztonságos alkalmazásának független hatósági felügyelete.", "Az áram árának meghatározása.", "Új atomerőművek megépítése állami költségvetésből."], 0, ["c1-14-vocab"]),
                fb("grammar", "controlled", "A nagy aktivitású radioaktív hulladékok elhelyezésére végleges _____ geológiai tároló létesítése szükséges. (deep / mélységi)", "mélységi", "For the disposal of high-level radioactive waste the establishment of a deep geological repository is required.", ["c1-nuclear-governance"]),
                match("vocabulary", "controlled", [["üzemidő-hosszabbítás", "reaktor engedélyének meghosszabbítása"], ["kiégett fűtőelem", "elhasznált radioaktív üzemanyag"], ["alapterhelés", "folyamatosan biztosított áramtermelés"], ["leszerelés", "leállított atomerőmű elbontása"]], ["c1-14-vocab"]),
                fb("grammar", "practice", "A nukleáris energia zéró kibocsátású _____ biztosít, megkönnyítve a fosszilis kapacitások kiváltását. (baseload / alapterhelést)", "alapterhelést", "Nuclear energy provides zero-emission baseload, facilitating the replacement of fossil capacities.", ["c1-nuclear-governance"]),
                sb("grammar", "practice", ["A", "nukleáris", "biztonság", "garanciái", "nem", "lehetnek", "politikai", "alku", "tárgyai."], ["A", "nukleáris", "biztonság", "garanciái", "nem", "lehetnek", "politikai", "alku", "tárgyai."], "Guarantees of nuclear safety cannot be objects of political bargaining.", ["c1-nuclear-governance"]),
                dc("dialogue", [
                    {"speaker": "Környezetvédő", "text": "Hogyan oldható meg a kiégett fűtőelemek évszázadokon át tartó biztonságos tárolása?"},
                    {"speaker": "Geológus", "text": "Tektonikailag stabil kőzetformációkban kialakított mélységi geológiai _____ révén."},
                ], ["tároló", "tó", "kamion"], 0, ["c1-nuclear-governance"]),
                sw("production", [{"prompt": "Write a regulatory sentence affirming the primacy of nuclear safety in licensing.", "answer": "Az Országos Atomenergia Hivatal kizárólag abban az esetben engedélyezi az üzemidő-hosszabbítást, amennyiben a reaktorblokkok minden nemzetközi nukleáris biztonsági és sugárvédelmi követelménynek maradéktalanul eleget tesznek."}], ["c1-nuclear-governance"]),
                mc("grammar", "check", "Mit jelent az 'alapterhelés' (baseload) funkciója a villamosenergia-rendszerben?", [
                    "A rendszer azon folyamatos, stabil áramszintjét, amely napszaktól és időjárástól függetlenül szünetmentesen rendelkezésre áll.",
                    "A legmagasabb díjú villanyáram tarifáját.",
                    "A hálózat túlterhelése miatti áramszünetet."
                ], 0, ["c1-nuclear-governance"])
            ]
        },
        {
            "num": 5,
            "stem": "c1-14-05",
            "title": "Ecological Consciousness & István Fekete's Wetland Ethic",
            "grammar_title": "Nature Writing, Wetland Conservation and Systemic Environmental Ethics",
            "grammar_skill": "c1-circular-economy-syntax",
            "goals": [
                "I can analyze István Fekete's ecological philosophy in 'Tüskevár' and 'Csend'.",
                "I can evaluate circular economy principles and natural resource loops (*körforgásos gazdaság, életciklus-elemzés*).",
                "I can synthesize traditional ecological knowledge with contemporary environmental science in academic Hungarian."
            ],
            "vocab": [
                {"lemma": "körforgásos gazdaság", "translation": "circular economy", "pos": "expression"},
                {"lemma": "életciklus-elemzés", "translation": "life cycle assessment (LCA)", "pos": "noun"},
                {"lemma": "tájökológia", "translation": "landscape ecology", "pos": "noun"},
                {"lemma": "vizes élőhely", "translation": "wetland ecosystem (Kis-Balaton / Berek)", "pos": "noun"},
                {"lemma": "erőforrás-hatékonyság", "translation": "resource efficiency", "pos": "noun"},
                {"lemma": "természeti egyensúly", "translation": "natural equilibrium", "pos": "noun"},
                {"lemma": "ártér", "translation": "floodplain", "pos": "noun"},
                {"lemma": "alázat", "translation": "humility, reverence (toward nature)", "pos": "noun"}
            ],
            "gr_text1": "István Fekete (1900–1970) was Hungary's premier ecological writer. In *Tüskevár* (1957) and *Csend* (1965), he depicted the Kis-Balaton wetland wilderness not as a wild terrain to conquer, but as a delicate, sovereign ecosystem requiring human humility (*alázat*) and systemic respect.",
            "gr_text2": "Syntactically, texts blend evocative landscape descriptions with circular economy principles: `A természetben nem létezik hulladék: minden lebomló szerves anyag a következő életciklus tápanyagává válik, mintául szolgálva a modern körforgásos gazdaság számára`.",
            "gr_table": [
                ["A természetben minden folyamat zárt körforgást alkot.", "In nature every process forms a closed loop."],
                ["Matula bácsi alakja a természettel harmóniában élő ember ősi tudását testesíti meg.", "The figure of Uncle Matula embodies the ancient knowledge of man living in harmony with nature."],
                ["A körforgásos gazdaság célja a nyersanyagok életciklusának maximalizálása.", "The goal of circular economy is maximizing the life cycle of raw materials."]
            ],
            "classic_story": {
                "slug": "c1-14-fekete",
                "author": "Fekete István",
                "work": "Tüskevár és Csend (1957–1965)",
                "title": "A Berek csendje és a természet törvényei",
                "summary": "István Fekete's enduring ecological masterpiece on the Kis-Balaton wetlands, revealing the sacred equilibrium of nature and the timeless ethic of ecological humility.",
                "characters": ["Matula Gergely", "Tutajos"],
                "paragraphs": [
                    {"type": "narration", "text": "Amikor a nádi szél megcsendül a Kis-Balaton végtelen rekettyéseiben, nem a puszta pusztaság beszél: a természet ősi, tökéletes organizmusa lélegzik. Fekete István Tüskevár című műve és későbbi vallomásos esszéi a huszadik századi magyar irodalom legmélyebb ökológiai kátéját alkotják."},
                    {"type": "narration", "text": "Tutajos és Bütyök a Berekben nemcsak a fizikai önállóságot tanulja meg, hanem valami sokkal lényegesebbet: a természeti alázatot. Matula bácsi kérges tenyerű, szűkszavú alakja nem vadászati trófeákat hajszol, hanem ismeri a mocsár minden neszét, a madarak fészkelési ritmusát és a halak járását. Tudja, hogy a természetben nincsen felesleges lény: a szúnyog, a gém, a nád és a hínár mind egymást éltető, szétválaszthatatlan láncszem."},
                    {"type": "narration", "text": "Fekete István figyelmeztetése ma érvényesebb, mint valaha. A modern civilizáció technokrata gőgje mocsárlecsapolásokkal, folyószabályozásokkal és betonágyakkal próbálta leigázni a tájat, nem sejtve, hogy ezzel saját éltető vízgyűjtőit szárítja ki. A Kis-Balaton későbbi rekonstrukciója, a Berek visszaárasztása bizonyította be Fekete igazát: a természetet nem legyőzni kell, hanem megérteni és szolgálni."},
                    {"type": "narration", "text": "A Berek csendje nem halotti némaság, hanem a mindenség harmóniája. Arra tanít, hogy a jövő gazdasága csak körforgásos lehet: amely a természet mintájára tiszteletben tartja az erőforrások határait, és felismeri, hogy az ember nem a teremtés ura, hanem annak felelős gondviselője."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Mi Fekete István műveinek alapvető ökológiai üzenete?", ["Hogy az ember nem a természet legyőzője, hanem annak szerves része, akinek alázattal kell tisztelnie a természetes egyensúlyt.", "Hogy minden vizes élőhelyet le kell csapolni építkezésekhez.", "Hogy a természetben csak a hasznot hozó állatoknak van helye."], 0, ["c1-14-vocab"]),
                fb("grammar", "controlled", "A modern ipar számára a természeti folyamatok zárt körforgása jelenti a _____ gazdaság legfőbb modelljét. (circular / körforgásos)", "körforgásos", "For modern industry, the closed loops of natural processes represent the foremost model of circular economy.", ["c1-circular-economy-syntax"]),
                match("vocabulary", "controlled", [["körforgásos gazdaság", "hulladékmentes zárt ciklus"], ["vizes élőhely", "mocsaras ökoszisztéma"], ["életciklus-elemzés", "termék környezeti hatásának felmérése"], ["alázat", "természet tisztelete"]], ["c1-14-vocab"]),
                mc("reading", "practice", "Mit testesít meg Matula bácsi karaktere a Tüskevárban?", [
                    "A természettel harmóniában élő, annak törvényeit és határait tisztelő hagyományos ökológiai bölcsességet.",
                    "Egy szigorú és könyörtelen gyári felügyelőt.",
                    "Egy modern városi üzletembert."
                ], 0, None),
                sb("grammar", "practice", ["A", "körforgásos", "gazdaságban", "a", "hulladék", "értékes", "másodnyersanyaggá", "alakul."], ["A", "körforgásos", "gazdaságban", "a", "hulladék", "értékes", "másodnyersanyaggá", "alakul."], "In a circular economy waste is transformed into valuable secondary raw material.", ["c1-circular-economy-syntax"]),
                sw("production", [{"prompt": "Synthesize István Fekete's wetland philosophy in relation to modern sustainability.", "answer": "Fekete István regényei arra figyelmeztetnek, hogy a technikai haladás önmagában pusztítóvá válik a természeti alázat nélkül: a fenntartható jövő alapja a természet zárt ökológiai rendszereinek és vízháztartásának tisztelete."}], ["c1-circular-economy-syntax"]),
                mc("grammar", "check", "Mi az életciklus-elemzés (LCA) célja a környezetvédelemben?", [
                    "Egy termék teljes környezeti lábnyomának feltárása a nyersanyag-kitermeléstől a gyártáson át az újrahasznosításig.",
                    "A termékek szavatossági idejének meghosszabbítása adalékanyagokkal.",
                    "A gyárak reklámköltésének ellenőrzése."
                ], 0, ["c1-circular-economy-syntax"])
            ]
        }
    ]

    for l in core_lessons:
        emit_instructional_lesson(14, "core", l, core_title, core_intro if l["num"] == 1 else None)

    # Core Consolidation
    emit_consolidation_lesson(
        14,
        "core",
        "c1-14-consolidation",
        core_title,
        [
            "I can evaluate ecosystem dynamics, habitat fragmentation, and water retention predicates.",
            "I can analyze grid balancing, intermittent renewable integration, and decarbonization paths.",
            "I can navigate EU green taxonomy, nuclear safety governance, and circular economy lifecycles."
        ],
        [
            mc("grammar", "recognize", "Mit fejez ki a 'jelentős károkozás elkerülésének' elve (DNSH) az uniós taxonómiában?", [
                "Azt, hogy egy zöld projekt nem sérthet súlyosan más környezetvédelmi célkitűzéseket.",
                "Hogy a gyáraknak tilos adót fizetniük.",
                "Hogy a munkavállalóknak védősisakot kell viselniük."
            ], 0, ["c1-green-taxonomy-criteria"]),
            mc("grammar", "recognize", "Miért nélkülözhetetlen az energiatárolás a napenergia térnyerésével?", [
                "Mert lehetővé teszi a nappali csúcstermelés elraktározását az esti fogyasztási csúcs idejére.",
                "Mert a napelemek éjszaka hőt vonnak el a földtől.",
                "Mert a villanyáram néhány másodperc alatt megromlik."
            ], 0, ["c1-energy-transition-clauses"]),
            match("vocabulary", "recognize", [["biodiverzitás", "fajgazdagság"], ["karbontalanítás", "kibocsátáscsökkentés"], ["zöldrefestés", "félrevezető zöld állítások"], ["alapterhelés", "stabil áramtermelés"], ["körforgásos gazdaság", "zárt anyagáramlási modell"]], ["c1-14-vocab"]),
            fb("vocabulary", "recall", "A táj természetes _____ képességének visszaállítása enyhíti a mezőgazdasági aszálykárokat. (water retention / vízvisszatartó)", "vízvisszatartó", "Restoring the natural water retention capacity of the landscape eases agricultural drought damage.", ["c1-14-vocab"]),
            fb("vocabulary", "recall", "Az OAH szigorú vizsgálatnak veti alá az atomerőművi reaktorok _____ kérelmét. (lifetime extension / üzemidő-hosszabbítási)", "üzemidő-hosszabbítási", "The OAH subjects the lifetime extension requests of nuclear reactors to strict inspection.", ["c1-14-vocab"]),
            fb("grammar", "recall", "A hálózatirányítónak szabályozó kapacitásokat kell bevetnie a _____ stabilitása végett. (grid balancing / hálózatkiegyenlítés)", "hálózatkiegyenlítés", "The grid operator must deploy regulatory capacities for the sake of grid balancing stability.", ["c1-energy-transition-clauses"]),
            fb("grammar", "context", "A zöld taxonómia célja, hogy kizárja a felelőtlen _____ kockázatát a pénzügyi piacokon. (greenwashing / zöldrefestés)", "zöldrefestés", "The goal of green taxonomy is eliminating the risk of irresponsible greenwashing in financial markets.", ["c1-green-taxonomy-criteria"]),
            fb("grammar", "context", "A Berek világa Fekete Istvánnál a természeti _____ és a felelősség örök jelképe. (humility / alázat)", "alázat", "The world of the Berek in István Fekete is the timeless symbol of nature humility and responsibility.", ["c1-circular-economy-syntax"]),
            mc("grammar", "context", "Hogyan járul hozzá a nukleáris energia a klímacélok eléréséhez?", [
                "Szén-dioxid-mentes alapterhelést biztosít, miközben nem terheli a légkört üvegházhatású gázokkal.",
                "Hőenergiát von el a környezettől.",
                "Csökkenti az ipari vízhasználatot nullára."
            ], 0, ["c1-nuclear-governance"]),
            sb("grammar", "produce", ["A", "környezeti", "fenntarthatóság", "a", "jövő", "gazdaságának", "legfontosabb", "mérföldköve."], ["A", "környezeti", "fenntarthatóság", "a", "jövő", "gazdaságának", "legfontosabb", "mérföldköve."], "Environmental sustainability is the most important milestone of the future economy.", ["c1-green-taxonomy-criteria"]),
            sw("production", [{"prompt": "Write an evaluation of the balance between nuclear power and renewables in energy transition.", "answer": "A dekarbonizáció hatékony megvalósítása megköveteli a nukleáris energia által nyújtott stabil, kibocsátásmentes alapterhelés és a megújuló források rugalmas, tárolókkal támogatott integrációjának szintézisét."}], ["c1-energy-transition-clauses"]),
            sw("production", [{"prompt": "Formulate a concluding thought on István Fekete's ecological wisdom.", "answer": "Fekete István munkássága arra emlékeztet, hogy a valódi ökológiai fordulat nem csupán technológiai innováció, hanem erkölcsi megtisztulás: a természeti egyensúly és a teremtett világ iránti mélységes tisztelet helyreállítása."}], ["c1-circular-economy-syntax"])
        ]
    )

    # ----------------------------------------------------
    # TRACK 2: DISCOURSE (c1-energetika)
    # ----------------------------------------------------
    slug = "energetika"
    disc_intro = [
        "From the construction of the Paks Nuclear Power Plant in the 1970s and 80s through the Bős–Nagymaros dam controversy, the geothermal potential of the Pannonian Basin, and the explosive boom in solar PV farms, energy policy in Hungary is at the crossroads of sovereignty, geopolitical dependence, and green transition.",
        "In this serialized Discourse track, explore the technical and geopolitical history of Hungarian energy: the Paks I base and Paks II Russian expansion dilemmas, the Danube riverbed conflicts, deep geothermal heating networks, and solar grid balancing realities in Central Europe."
    ]

    disc_lessons = [
        {
            "num": 1,
            "stem": f"c1-{slug}-01",
            "title": "Paks I: The Construction and Life-Extension of Hungarian Nuclear Power",
            "grammar_title": "VVER-440 Reactor Architecture, Baseline Power and 20-Year Life Extensions",
            "grammar_skill": "c1-nuclear-governance",
            "goals": [
                "I can analyze the history and operation of the Paks Nuclear Power Plant (*Paks I, VVER-440 blokkok, Paksi Atomerőmű*).",
                "I can evaluate technical life-extension programs (*üzemidő-hosszabbítás, biztonsági felülvizsgálat*).",
                "I can discuss nuclear baseload generation representing ~50% of Hungarian electricity."
            ],
            "vocab": [
                {"lemma": "Paksi Atomerőmű", "translation": "Paks Nuclear Power Plant", "pos": "noun"},
                {"lemma": "blokk", "translation": "reactor unit / block (Paks 1-4)", "pos": "noun"},
                {"lemma": "nyomottvizes reaktor", "translation": "pressurized water reactor (PWR / VVER)", "pos": "expression"},
                {"lemma": "ellátásbiztonság", "translation": "security of electricity supply", "pos": "noun"},
                {"lemma": "fűtőelem-kazetta", "translation": "fuel assembly", "pos": "noun"},
                {"lemma": "primer kör", "translation": "primary cooling loop", "pos": "noun"},
                {"lemma": "üzemkiesés", "translation": "outage, forced shutdown", "pos": "noun"},
                {"lemma": "termelési volumen", "translation": "production volume", "pos": "noun"}
            ],
            "gr_text1": "Built between 1974 and 1987, the four VVER-440/213 pressurized water reactor blocks at Paks produce roughly half of Hungary's domestic electricity. In the 2000s, safety upgrades enabled a 20-year lifetime extension (to 2032–2037), and a further 20-year extension to 2052–2057 is currently underway.",
            "gr_text2": "Syntactically, engineering evaluations combine technical passive structures with causal postpositions: `A reaktortartály állapotának roncsolásmentes vizsgálata révén bizonyítást nyert, hogy a blokkok biztonságosan üzemeltethetők további évtizedeken át`.",
            "gr_table": [
                ["A paksi blokkok a hazai villamosenergia-termelés felét biztosítják.", "The Paks units provide half of domestic electricity generation."],
                ["Az üzemidő meghosszabbítása a legolcsóbb dekarbonizált kapacitásfenntartás.", "Extending operating lifetimes is the cheapest decarbonized capacity maintenance."],
                ["A biztonsági rendszerek kettőzése kizárja a súlyos üzemzavarok kockázatát.", "Redundancy of safety systems eliminates the risk of severe incidents."]
            ],
            "world_story_seg": {
                "seg_slug": "paks1",
                "title": "A Duna menti atomóriás: A Paksi Atomerőmű fél évszázada",
                "summary": "How Hungary built its nuclear flagship at Paks and why its four VVER-440 reactors remain the bedrock of national electricity supply.",
                "paragraphs": [
                    {"type": "narration", "text": "Amikor 1982 decemberében az 1-es blokk rákapcsolódott az országos villamosenergia-hálózatra, Magyarország belépett a nukleáris energiát alkalmazó nemzetek elit klubjába. A Tolna megyei Paks mellett felépült négy szovjet típusú VVER-440-es nyomottvizes reaktorblokk a szocialista korszak legnagyobb és legmegbízhatóbb ipari beruházásának bizonyult."},
                    {"type": "narration", "text": "Az évtizedek során a magyar mérnökök kiváló biztonsági kultúrát honosítottak meg, aminek köszönhetően Paks a nemzetközi rangsorokban is a legbiztonságosabb és leghatékonyabb atomerőművek közé emelkedett. A létesítmény ma a hazai áramtermelés mintegy felét adja tiszta, szén-dioxid-mentes alapterhelésként. A 2000-es években végrehajtott húszéves üzemidő-hosszabbítás nélkül az ország energiaellátása megroppant volna; ma pedig már a blokkok hatvanéves korukig történő működtetésének műszaki előkészítése zajlik."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Mekkora hányadát adja a Paksi Atomerőmű a magyarországi villamosenergia-termelésnek?", ["Körülbelül a felét (mintegy 45–50%-át) szén-dioxid-mentes alapterhelésként.", "Mindössze 2 százalékát.", "Az összes energiát 100%-ban."], 0, ["c1-energetika-vocab"]),
                fb("grammar", "controlled", "A paksi atomerőművi blokkok folyamatos és stabil _____ termeléssel szavatolják a hazai ellátásbiztonságot. (baseload / alapterheléses)", "alapterheléses", "The Paks nuclear power units guarantee domestic security of supply with continuous and stable baseload generation.", ["c1-nuclear-governance"]),
                match("vocabulary", "controlled", [["Paksi Atomerőmű", "hazai nukleáris létesítmény"], ["nyomottvizes reaktor", "VVER technológia"], ["ellátásbiztonság", "folyamatos áramellátás garanciája"], ["primer kör", "reaktort hűtő zárt vízkör"]], ["c1-energetika-vocab"]),
                fb("grammar", "practice", "A reaktorok biztonságos működését az OAH szigorú és független hatósági _____ garantálja. (supervision / felügyelete)", "felügyelete", "The safe operation of the reactors is guaranteed by the strict and independent regulatory supervision of the OAH.", ["c1-nuclear-governance"]),
                sb("grammar", "practice", ["A", "nukleáris", "energia", "biztosítja", "a", "hazai", "karbonmentes", "áramtermelés", "gerincét."], ["A", "nukleáris", "energia", "biztosítja", "a", "hazai", "karbonmentes", "áramtermelés", "gerincét."], "Nuclear energy provides the backbone of domestic carbon-free electricity generation.", ["c1-nuclear-governance"]),
                dc("dialogue", [
                    {"speaker": "Politikus", "text": "Miért van szükség a paksi blokkok üzemidejének további meghosszabbítására?"},
                    {"speaker": "Energetikai mérnök", "text": "Mert a leállításuk hatalmas _____ hiányt okozna a magyar villamosenergia-hálózatban."},
                ], ["kapacitásbeli", "szén", "papír"], 0, ["c1-nuclear-governance"]),
                sw("production", [{"prompt": "Write a sentence summarizing the strategic role of Paks I in Hungary's energy mix.", "answer": "A Paksi Atomerőmű négy reaktorblokkja a hazai villamosenergia-mix megkerülhetetlen gerincét alkotja, szén-dioxid-kibocsátás nélküli alapterhelést nyújtva az országos hálózat számára."}], ["c1-nuclear-governance"]),
                mc("grammar", "check", "Mi indokolja a meglévő blokkok üzemidő-hosszabbítását gazdaságilag?", [
                    "A meglévő, amortizálódott blokkok élettartamának növelése töredékébe kerül egy vadonatúj erőmű felépítésének.",
                    "Hogy eladják a turbinákat külföldre.",
                    "Hogy kevesebb fizetést kapjanak a mérnökök."
                ], 0, ["c1-nuclear-governance"])
            ]
        },
        {
            "num": 2,
            "stem": f"c1-{slug}-02",
            "title": "Paks II: Geopolitics, Financing & Technology Transfer",
            "grammar_title": "Intergovernmental Agreements, EPC Contracts and Sanctions Resilience",
            "grammar_skill": "c1-nuclear-governance",
            "goals": [
                "I can analyze the Paks II expansion agreement (*Roszatom, orosz államközi hitel, VVER-1200*).",
                "I can evaluate geopolitical energy dependence and sanctions impacts.",
                "I can discuss turnkey EPC contracts and European Commission state aid clearance."
            ],
            "vocab": [
                {"lemma": "államközi szerződés", "translation": "intergovernmental agreement (IGA)", "pos": "noun"},
                {"lemma": "fővállalkozói szerződés", "translation": "EPC contract (Engineering, Procurement, Construction)", "pos": "noun"},
                {"lemma": "geopolitikai függőség", "translation": "geopolitical dependence", "pos": "noun"},
                {"lemma": "állami támogatás vizsgálata", "translation": "state aid investigation (European Commission)", "pos": "expression"},
                {"lemma": "létesítési engedély", "translation": "construction license / site license", "pos": "noun"},
                {"lemma": "kulcsrakész kivitelezés", "translation": "turnkey implementation", "pos": "expression"},
                {"lemma": "hitelkonstrukció", "translation": "credit structure / loan framework", "pos": "noun"},
                {"lemma": "szankciós kitettség", "translation": "sanctions exposure / vulnerability", "pos": "noun"}
            ],
            "gr_text1": "The 2014 intergovernmental pact with Russia for two VVER-1200 generation 3+ reactors sparked intense debate concerning financing (10 billion Euro Russian state loan) and geopolitical energy dependence.",
            "gr_text2": "Syntactically, texts contrast legal-procedural hurdles with geopolitical dilemmas: `Noha az Európai Bizottság jóváhagyta az állami támogatást, a háborús szankciók és az engedélyeztetési csúszások komolyan lelassították a beruházás ütemét`.",
            "gr_table": [
                ["A Paks II beruházás célja a kieső régi blokkok pótlása a 2030-as évektől.", "The aim of Paks II is replacing retiring old blocks from the 2030s."],
                ["Az államközi hitelszerződés heves vitákat váltott ki a szuverenitás kapcsán.", "The intergovernmental loan contract triggered fierce debates on sovereignty."],
                ["A szankciók és engedélyezési késedelmek áthangolták az építési ütemtervet.", "Sanctions and licensing delays recalibrated the construction timetable."]
            ],
            "world_story_seg": {
                "seg_slug": "paks2",
                "title": "A moszkvai paktumtól a gödörig: A Paks II beruházás kálváriája",
                "summary": "The geopolitical and technical saga of the Paks II nuclear project: from the 2014 Putin–Orbán pact to licensing delays and war sanctions.",
                "paragraphs": [
                    {"type": "narration", "text": "2014 januárjában a moszkvai elnöki rezidencián született meg a modern magyar gazdaságtörténet legvitatottabb megállapodása: a magyar kormány versenytárgyalás nélkül a Roszatomot bízta meg két új, 1200 megawattos atomerőművi blokk felépítésével, egy tízmilliárd eurós orosz állami hitelkeret terhére. A döntés azonnal heves belpolitikai és nemzetközi tiltakozást váltott ki."},
                    {"type": "narration", "text": "A bírálók a Moszkvától való hosszú távú pénzügyi és technológiai kiszolgáltatottságot, valamint az átláthatatlan hitelszerződést kárhoztatták, míg a kormányzat az olcsó áram és az ipari ellátásbiztonság zálogaként mutatta fel a projektet. Az Európai Bizottság évekig vizsgálta az állami támogatást és a közbeszerzési szabályokat, mire zöld utat adott. Az ukrajnai háború kitörése és a nemzetközi szankciók azonban újabb akadályokat gördítettek a beruházás elé: a megkezdett talajelőkészítés dacára a Paks II átadási céldátuma folyamatosan kitolódik."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Miért váltott ki nemzetközi vitát a Paks II beruházás 2014-es megkötése?", ["Mert versenytárgyalás nélkül, orosz államközi szerződéssel és hitellel bízták meg a Roszatomot.", "Mert a Tisza partjára akarták építeni.", "Mert széntüzelésű reaktort választottak."], 0, ["c1-energetika-vocab"]),
                fb("grammar", "controlled", "A Paks II projekt kulcsrakész _____ szerződés keretében valósul meg a fővállalkozóval. (EPC / fővállalkozói)", "fővállalkozói", "The Paks II project is implemented within an EPC general contracting agreement framework with the contractor.", ["c1-nuclear-governance"]),
                match("vocabulary", "controlled", [["államközi szerződés", "két kormány közötti megállapodás"], ["fővállalkozói szerződés", "kivitelezést végző EPC kontraktus"], ["létesítési engedély", "építési jogot megadó határozat"], ["szankciós kitettség", "nemzetközi korlátozások miatti kockázat"]], ["c1-energetika-vocab"]),
                fb("grammar", "practice", "Az ukrajnai háború után elrendelt nemzetközi intézkedések fokozták a beruházás _____ kitettségét. (sanctions / szankciós)", "szankciós", "International measures enacted after the war in Ukraine increased the investment's sanctions exposure.", ["c1-nuclear-governance"]),
                sb("grammar", "practice", ["A", "geopolitikai", "kockázatok", "és", "a", "technológiai", "függőség", "lassítják", "a", "beruházást."], ["A", "geopolitikai", "kockázatok", "és", "a", "technológiai", "függőség", "lassítják", "a", "beruházást."], "Geopolitical risks and technological dependence slow down the investment.", ["c1-nuclear-governance"]),
                dc("dialogue", [
                    {"speaker": "Diplomata", "text": "Hogyan érintik az európai szankciók a Paks II projekt alkatrész-beszerzéseit?"},
                    {"speaker": "Szakértő", "text": "Bár a nukleáris ipar mentesül a szankciók alól, a nyugati irányítástechnika szállítása komoly _____ ütközik."},
                ], ["akadályokba", "pénzbe", "segítségbe"], 0, ["c1-nuclear-governance"]),
                sw("production", [{"prompt": "Analyze the geopolitical controversy of Paks II in one objective sentence.", "answer": "A Paks II projekt a hazai villamosenergia-igény hosszú távú biztosítását célozza, ám az orosz kivitelező és hitelkonstrukció révén mély geopolitikai és szuverenitási aggályokat vet fel a változó európai környezetben."}], ["c1-nuclear-governance"]),
                mc("grammar", "check", "Milyen feltétellel hagyta jóvá az Európai Bizottság a Paks II állami támogatását?", [
                    "A piaci megtérülés igazolásával és a termelt áram jelentős részének transzparens tőzsdei értékesítésével.",
                    "Az összes magyar erdő kivágásával.",
                    "A forint árfolyamának azonnali euróra váltásával."
                ], 0, ["c1-nuclear-governance"])
            ]
        },
        {
            "num": 3,
            "stem": f"c1-{slug}-03",
            "title": "Bős–Nagymaros & The Trauma of Damming the Danube",
            "grammar_title": "Cross-Border River Ecology, The Hague Judgment and Environmental Movements",
            "grammar_skill": "c1-ecological-system-dynamics",
            "goals": [
                "I can analyze the Bős–Nagymaros barrage system controversy (*vízlépcső, Duna Kör, C-variáns*).",
                "I can evaluate the 1997 International Court of Justice (The Hague) landmark environmental judgment.",
                "I can describe ecological riverbed alteration and civic environmental mobilization in formal Hungarian."
            ],
            "vocab": [
                {"lemma": "vízlépcsőrendszer", "translation": "barrage system, hydroelectric dam system", "pos": "noun"},
                {"lemma": "Duna Kör", "translation": "Danube Circle (historic dissident environmental NGO)", "pos": "noun"},
                {"lemma": "elterelés", "translation": "diversion (river course diversion / C-variant)", "pos": "noun"},
                {"lemma": "Szigetköz", "translation": "Szigetköz (Danube wetland inland delta)", "pos": "noun"},
                {"lemma": "Hágai Nemzetközi Bíróság", "translation": "International Court of Justice in The Hague", "pos": "noun"},
                {"lemma": "talajvízszint", "translation": "groundwater table", "pos": "noun"},
                {"lemma": "mederelfajulás", "translation": "riverbed degradation / incision", "pos": "noun"},
                {"lemma": "ökocídium", "translation": "ecocide, massive environmental destruction", "pos": "noun"}
            ],
            "gr_text1": "The 1977 Czechoslovak-Hungarian treaty on the Gabčíkovo-Nagymaros dam catalyzed the Hungarian democratic opposition: the *Duna Kör* organized massive protest against ecological destruction. In 1989 Hungary suspended construction, prompting Slovakia's 1992 unilateral diversion of the Danube (*C-variáns*).",
            "gr_text2": "The 1997 International Court of Justice judgment at The Hague declared both parties violated international law, mandating joint environmental negotiation without resolving Szigetköz's ecological desiccation.",
            "gr_table": [
                ["A Duna egyoldalú elterelése drasztikusan lecsökkentette a Szigetköz vízhozamát.", "Unilateral diversion of the Danube drastically reduced Szigetköz water discharge."],
                ["A Duna Kör fellépése a magyar rendszerváltás bölcsőjévé vált.", "The action of Danube Circle became the cradle of Hungarian democratic transition."],
                ["A hágai perben mindkét felet elmarasztalták a szerződés megsértéséért.", "In the Hague lawsuit both parties were censured for breach of treaty."]
            ],
            "world_story_seg": {
                "seg_slug": "bosnagymaros",
                "title": "A Duna elterelése és a zöld ébredés: A Bős–Nagymaros vita",
                "summary": "How the struggle against the Gabčíkovo–Nagymaros dam sparked the Hungarian environmental movement and led to the historic Hague international court battle.",
                "paragraphs": [
                    {"type": "narration", "text": "A Bős–Nagymaros vízlépcsőrendszer története a közép-európai környezetvédelem legnagyobb és legfájdalmasabb traumája. Az 1977-ben aláírt gigantomán szocialista terv a Duna elgátolásával és dunakanyari betonmonstrumok felépítésével fenyegetett, ami a Szigetköz páratlan ártéri erdeinek és ivóvízbázisának pusztulásával járt volna. A nyolcvanas évek közepén létrejött Duna Kör a tiltakozások élére állt: a természetvédelem a kommunista diktatúra elleni polgári ellenállás legfontosabb fedőszervezetévé vált."},
                    {"type": "narration", "text": "1989-ben a demokratizálódó magyar kormány felmondta a nagymarosi építkezést, mire 1992 októberében Szlovákia az úgynevezett C-variánssal egyoldalúan elterelte a határfolyót, szárazra kényszerítve a régi Duna-medret és az ágrendszereket. A vita a Hágai Nemzetközi Bíróság elé került, amely 1997-es ítéletében mindkét felet elmarasztalta. Bár a szlovák oldalon a bősi erőmű ma is termel áramot, a Szigetköz ökológiai egyensúlya csak mesterséges vízpótlással tartható fenn: mementóként arra, milyen jóvátehetetlen károkat okoz a természet megerőszakolása."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Miért játszott történelmi szerepet a Duna Kör a magyar rendszerváltásban?", ["Mert a vízlépcső elleni környezetvédelmi tiltakozás a kommunista diktatúrával szembeni békés polgári ellenzék központjává vált.", "Mert megnyerte az evezős olimpiai bajnokságot.", "Mert privatizálta a budapesti hidakat."], 0, ["c1-energetika-vocab"]),
                fb("grammar", "controlled", "A Duna 1992-es egyoldalú szlovák _____ katasztrofális talajvízszint-csökkenést okozott a Szigetközben. (diversion / elterelése)", "elterelése", "The unilateral Slovak diversion of the Danube in 1992 caused a catastrophic groundwater table drop in Szigetköz.", ["c1-ecological-system-dynamics"]),
                match("vocabulary", "controlled", [["vízlépcsőrendszer", "duzzasztógátak és erőművek láncolata"], ["Duna Kör", "rendszerváltó környezetvédő mozgalom"], ["Szigetköz", "Duna ártéri szigetvilága"], ["Hágai Nemzetközi Bíróság", "államközi vitákat eldöntő ENSZ-fórum"]], ["c1-energetika-vocab"]),
                fb("grammar", "practice", "A Hágai Nemzetközi Bíróság 1997-ben kimondta, hogy mindkét állam megsértette a nemzetközi _____ kötelezettségeit. (treaty / szerződéses)", "szerződéses", "The International Court of Justice in The Hague ruled in 1997 that both states breached their international treaty obligations.", ["c1-ecological-system-dynamics"]),
                sb("grammar", "practice", ["A", "Szigetköz", "ökológiai", "egyensúlyát", "csak", "mesterséges", "vízpótlással", "lehetett", "megmenteni."], ["A", "Szigetköz", "ökológiai", "egyensúlyát", "csak", "mesterséges", "vízpótlással", "lehetett", "megmenteni."], "The ecological balance of Szigetköz could only be saved through artificial water replenishment.", ["c1-ecological-system-dynamics"]),
                dc("dialogue", [
                    {"speaker": "Környezetvédő", "text": "Milyen következményekkel járt a Duna elterelése a szigetközi élővilágra?"},
                    {"speaker": "Biológus", "text": "A mellékágak kiszáradásával összeomlott a halállomány és lesüllyedt a környékbeli _____."},
                ], ["talajvízszint", "árfolyam", "turizmus"], 0, ["c1-ecological-system-dynamics"]),
                sw("production", [{"prompt": "Summarize the Bős-Nagymaros controversy from an ecological and legal perspective.", "answer": "A Bős–Nagymaros vita rávilágított arra, hogy a határokon átnyúló folyók egyoldalú elterelése nemcsak súlyos nemzetközi jogsértést jelent, hanem visszafordíthatatlan ökológiai károkat okoz a térség vizes élőhelyeiben és talajvízkészletében."}], ["c1-ecological-system-dynamics"]),
                mc("grammar", "check", "Mit mondott ki a Hágai Nemzetközi Bíróság 1997-es döntése?", [
                    "Hogy Magyarország jogtalanul állította le az építkezést, de Szlovákia is jogellenesen terelte el a Dunát a C-variánssal.",
                    "Hogy az egész folyót ki kell szárítani.",
                    "Hogy Nagymaroson egy harmadik gátat kell építeni."
                ], 0, ["c1-ecological-system-dynamics"])
            ]
        },
        {
            "num": 4,
            "stem": f"c1-{slug}-04",
            "title": "Geothermal Potential of the Pannonian Basin",
            "grammar_title": "Thermal Water Reservoirs, District Heating and Enhanced Geothermal Systems (EGS)",
            "grammar_skill": "c1-energy-transition-clauses",
            "goals": [
                "I can analyze the unique geothermal endowment of the Pannonian Basin (*geotermikus gradiens, hévízkészlet, távfűtés*).",
                "I can evaluate municipal district heating decarbonization (*szegedi geotermikus fűtési rendszer*).",
                "I can discuss reservoir reinjection and environmental sustainability in advanced Hungarian."
            ],
            "vocab": [
                {"lemma": "geotermikus gradiens", "translation": "geothermal gradient (temperature rise per depth)", "pos": "noun"},
                {"lemma": "hévízkút", "translation": "thermal water well", "pos": "noun"},
                {"lemma": "távfűtési hálózat", "translation": "district heating network", "pos": "noun"},
                {"lemma": "visszasajtolás", "translation": "reinjection (of cooled thermal water into aquifers)", "pos": "noun"},
                {"lemma": "Pannon-medence", "translation": "Pannonian Basin (geothermal sweet spot)", "pos": "noun"},
                {"lemma": "földgázkiváltás", "translation": "natural gas displacement / substitution", "pos": "noun"},
                {"lemma": "hőtermelés", "translation": "heat generation", "pos": "noun"},
                {"lemma": "vízadó réteg", "translation": "aquifer, water-bearing formation", "pos": "noun"}
            ],
            "gr_text1": "Due to thin continental crust, the Pannonian Basin boasts Europe's highest geothermal gradient (~45°C/km vs 30°C world average). Cities like Szeged have executed Europe's largest municipal geothermal district heating conversion, replacing fossil Russian gas with deep thermal water loops.",
            "gr_text2": "Syntactically, texts describe technical environmental loops using nominal compounds: `A kitermelt és lehűlt termálvíz kötelező visszasajtolása a vízadó rétegbe biztosítja a hidrotermális rezervoár nyomásának és hőmérsékletének fenntarthatóságát`.",
            "gr_table": [
                ["A Pannon-medence geotermikus adottságai európai szinten egyedülállóak.", "Geothermal endowments of the Pannonian Basin are unique on a European scale."],
                ["Szeged városa sikeresen váltotta ki a földgázt geotermikus távfűtéssel.", "The city of Szeged successfully displaced natural gas with geothermal district heating."],
                ["A visszasajtolás elengedhetetlen a hévízkészletek kimerülésének megelőzésére.", "Reinjection is essential to prevent depletion of thermal water reserves."]
            ],
            "world_story_seg": {
                "seg_slug": "geotermia",
                "title": "A föld mélyének rejtett kincse: Geotermia a Pannon-medencében",
                "summary": "How Hungary's extraordinarily thin crust makes it a geothermal superpower, and how Szeged built Europe's largest geothermal district heating network.",
                "paragraphs": [
                    {"type": "narration", "text": "Magyarország alatt a földkéreg szokatlanul vékony: míg a világátlag szerint kilométerenként harminc fokkal emelkedik a hőmérséklet a mélybe fúrva, a Pannon-medencében ez az érték eléri a negyvenöt-ötven Celsius-fokot is. A Kárpát-medence mélye forró hévizek gigantikus kazánja, amelyet az ókori rómaiak és a hódoltság kori törökök még csak gyógyfürdőzésre használtak, ma viszont a tiszta energiaforradalom legígéretesebb pillére."},
                    {"type": "narration", "text": "A legsikeresebb áttörést Szeged városa hajtotta végre, ahol felépült Európa legnagyobb geotermikus távhőrendszere: huszonhét kúttal és korszerű hőközpontokkal huszonhétezer lakás és több száz középület fűtését állították át földgázról a földből feltörő forró víz energiájára. A rendszer legnagyobb erénye az időjárásfüggetlenség: sem a szélcsend, sem a felhős égbolt nem akadályozza a működését. A használt víz visszasajtolásával pedig zárt, megújuló körfolyamat jön létre, amely bizonyítja, hogy a magyar energiafüggetlenség kulcsa ott rejtőzik közvetlenül a talpunk alatt."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Miért kiemelkedő a Pannon-medence geotermikus adottsága európai viszonylatban?", ["Mert a földkéreg vékonysága miatt a geotermikus gradiens sokkal magasabb az európai átlagnál, forró vízkészleteket rejtve.", "Mert nincsenek folyók a térségben.", "Mert télen nem esik hó."], 0, ["c1-energetika-vocab"]),
                fb("grammar", "controlled", "A használt termálvíz mélybe történő _____ kötelező a vízkészletek kimerülésének elkerülése végett. (reinjection / visszasajtolása)", "visszasajtolása", "Reinjection of used thermal water into the deep is mandatory to avoid depletion of water resources.", ["c1-energy-transition-clauses"]),
                match("vocabulary", "controlled", [["geotermikus gradiens", "mélységgel arányos hőmérséklet-emelkedés"], ["távfűtési hálózat", "települési központi fűtési rendszer"], ["visszasajtolás", "lehűlt víz visszanyomása a mélybe"], ["földgázkiváltás", "fosszilis import csökkentése zöld hővel"]], ["c1-energetika-vocab"]),
                fb("grammar", "practice", "Szeged városa sikeresen hajtotta végre a távfűtés _____ a geotermikus energia hasznosításával. (decarbonization / dekarbonizációját)", "dekarbonizációját", "The city of Szeged successfully executed the decarbonization of district heating utilizing geothermal energy.", ["c1-energy-transition-clauses"]),
                sb("grammar", "practice", ["A", "geotermikus", "energia", "időjárásfüggetlen", "zöld", "hőforrást", "biztosít", "a", "városoknak."], ["A", "geotermikus", "energia", "időjárásfüggetlen", "zöld", "hőforrást", "biztosít", "a", "városoknak."], "Geothermal energy provides a weather-independent green heat source for cities.", ["c1-energy-transition-clauses"]),
                dc("dialogue", [
                    {"speaker": "Városvezető", "text": "Hogyan csökkenthetjük az önkormányzat fűtési gázszámláit tartósan?"},
                    {"speaker": "Mérnök", "text": "A helyi mélyfúrású hévízkutakra támaszkodó _____ rendszer kiépítésével."},
                ], ["geotermikus", "széntüzelésű", "nukleáris"], 0, ["c1-energy-transition-clauses"]),
                sw("production", [{"prompt": "Write an evaluative statement highlighting the advantages of geothermal district heating.", "answer": "A geotermikus távhő legnagyobb előnye az időjárásfüggetlenség és a helyi megújuló jelleg: hatékony visszasajtolással párosítva tartósan kiváltja a fosszilis földgázimportot a települési fűtésben."}], ["c1-energy-transition-clauses"]),
                mc("grammar", "check", "Miért elengedhetetlen a termálvíz visszasajtolása a rétegbe?", [
                    "Mert megakadályozza a vízadó réteg nyomáscsökkenését és védi a felszíni vizeket a sókiválástól és túlmelegedéstől.",
                    "Mert megolvasztja a havat az utakon.",
                    "Mert törvény írja elő a víz forralását."
                ], 0, ["c1-energy-transition-clauses"])
            ]
        },
        {
            "num": 5,
            "stem": f"c1-{slug}-05",
            "title": "The Solar Boom & Central European Grid Realities",
            "grammar_title": "Photovoltaic Penetration, Balancing Volatility and Market Price Cannibalization",
            "grammar_skill": "c1-circular-economy-syntax",
            "goals": [
                "I can analyze the solar boom in Hungary (>6,000 MW PV installed capacity).",
                "I can evaluate price cannibalization and negative wholesale power prices (*negatív áramárak*).",
                "I can synthesize the future of renewable integration, battery storage, and green hydrogen in Central Europe."
            ],
            "vocab": [
                {"lemma": "fotovoltaikus kapacitás", "translation": "photovoltaic (PV) capacity", "pos": "expression"},
                {"lemma": "naperőmű-boom", "translation": "solar power boom", "pos": "noun"},
                {"lemma": "negatív áramár", "translation": "negative electricity price (surplus hours)", "pos": "expression"},
                {"lemma": "áramtúltermelés", "translation": "power overproduction / excess generation", "pos": "noun"},
                {"lemma": "akku-kapacitás", "translation": "battery capacity", "pos": "noun"},
                {"lemma": "zöldhidrogén", "translation": "green hydrogen (electrolysis via renewables)", "pos": "noun"},
                {"lemma": "árkannibalizáció", "translation": "price cannibalization (renewables lowering peak prices)", "pos": "noun"},
                {"lemma": "hálózati csatlakozási stop", "translation": "grid connection freeze / moratorium", "pos": "expression"}
            ],
            "gr_text1": "Between 2018 and 2024, Hungary experienced one of Europe's fastest solar expansions, exceeding 6,000 MW. On sunny summer afternoons, solar generation frequently covers over 100% of national electricity demand, causing wholesale prices to drop below zero (*negatív áramárak*) and stressing the grid.",
            "gr_text2": "Syntactically, texts formulate economic and infrastructural tensions: `A termelési túlcsordulás és az árkannibalizáció elkerülésére a szabályozó hatóság akkumulátoros energiatárolók telepítéséhez kötötte az új naperőművek hálózati csatlakozását`.",
            "gr_table": [
                ["A beépített napelemes kapacitás meghaladta a 6000 megawattot.", "Installed solar PV capacity exceeded 6,000 megawatts."],
                ["A déli túltermelés negatív áramárakat idéz elő a tőzsdén.", "Midday overproduction triggers negative electricity prices on the exchange."],
                ["Az akkumulátoros energiatárolás és a zöldhidrogén jelenti a jövő tárolási megoldását.", "Battery storage and green hydrogen represent future storage solutions."]
            ],
            "world_story_seg": {
                "seg_slug": "napenergia",
                "title": "A napfény forradalma: Napelem-robbanás és hálózati kihívások",
                "summary": "How Hungary became a European solar heavyweight within five years, and how grid balancing and battery storage define the next frontier.",
                "paragraphs": [
                    {"type": "narration", "text": "Alig egy évtizeddel ezelőtt a napenergia még csak elenyésző egzotikumnak számított a magyar energiamixben. Ám az elmúlt években olyan robbanásszerű boom ment végbe, amelyre a legoptimistább elemzők sem számítottak: a háztartási méretű kiserőművek és a gigantikus ipari napelemfarmok együttes kapacitása 2024-re átlépte a hatezer megawattot. Ez a hatalmas volumen verőfényes nyári délidőben képes egymagában fedezni az egész ország pillanatnyi áramigényét."},
                    {"type": "narration", "text": "A siker azonban új, égető dilemmákat hozott magával. Amikor a nap süt, a túltermelés miatt az áram ára a nemzetközi tőzsdéken nemegyszer negatív tartományba zuhan; ám amint lemegy a nap, azonnal fosszilis vagy importált energiára van szükség a fogyasztás kielégítésére. A hálózat telítődött, ami miatt a kormány átmeneti csatlakozási moratóriumot rendelt el. A jövő kulcsa ezért a rugalmasságban rejlik: ipari akkumulátoros energiatárolókban, zöldhidrogén-fejlesztésekben és az intelligens okoshálózatokban, amelyek képesek a déli napfény bőségét az esti sötétség óráira átmenteni."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Mi okozza a 'negatív áramárak' jelenségét a villamosenergia-piacon?", ["A napsütéses órákban fellépő masszív napenergia-túltermelés, amikor több áram termelődik, mint amennyit a piac el tud fogyasztani.", "A bankok által fizetett kamat.", "A vezetékhálózat hibája."], 0, ["c1-energetika-vocab"]),
                fb("grammar", "controlled", "A napenergia-boom következtében fellépő árkannibalizáció csökkenti a naperőművek piaci _____ megtérülését. (economic / gazdasági)", "gazdasági", "Price cannibalization occurring as a result of the solar boom reduces the economic return of solar power plants.", ["c1-circular-economy-syntax"]),
                match("vocabulary", "controlled", [["fotovoltaikus kapacitás", "napelemes áramtermelő teljesítmény"], ["negatív áramár", "túltermelés miatti piaci jelenség"], ["akku-kapacitás", "villamosenergia-tároló egység"], ["zöldhidrogén", "megújuló árammal bontott hidrogén"]], ["c1-energetika-vocab"]),
                fb("grammar", "practice", "A megújulók integrációjának következő fázisában a hálózatfejlesztés mellett az ipari méretű energiatárolás kap _____ szerepet. (key / kulcsszerepet)", "kulcsszerepet", "In the next phase of renewable integration, industrial-scale energy storage receives a key role alongside grid development.", ["c1-circular-economy-syntax"]),
                sb("grammar", "practice", ["A", "tárolókapacitások", "kiépítése", "elengedhetetlen", "a", "megújuló", "energia", "rugalmas", "felhasználásához."], ["A", "tárolókapacitások", "kiépítése", "elengedhetetlen", "a", "megújuló", "energia", "rugalmas", "felhasználásához."], "Building storage capacities is indispensable for the flexible utilization of renewable energy.", ["c1-circular-economy-syntax"]),
                dc("dialogue", [
                    {"speaker": "Beruházó", "text": "Miért nem tudunk újabb naperőművet rákapcsolni a körzeti hálózatra?"},
                    {"speaker": "Hálózatüzemeltető", "text": "Mert a körzetben betelt a kapacitás, és a hálózatfejlesztésig _____ van érvényben."},
                ], ["moratórium", "engedély", "kedvezmény"], 0, ["c1-circular-economy-syntax"]),
                sw("production", [{"prompt": "Synthesize the challenge of negative electricity prices and storage solutions.", "answer": "A fotovoltaikus termeléscsúcsok által kiváltott negatív áramárak jelensége rámutat arra, hogy a megújulók további térnyerése zátonyra fut az ipari akkumulátoros tárolás és a zöldhidrogén-technológiák gyors bevezetése nélkül."}], ["c1-circular-economy-syntax"]),
                mc("grammar", "check", "Hogyan segíti a zöldhidrogén-előállítás a megújuló energia tárolását?", [
                    "A felesleges napárammal elektrolízis útján vizet bont hidrogénre, amely gázként hosszú távon tárolható és később árammá alakítható.",
                    "Megakadályozza a szél fújását.",
                    "Közvetlenül felmelegíti az utcai lámpákat."
                ], 0, ["c1-circular-economy-syntax"])
            ]
        }
    ]

    for l in disc_lessons:
        emit_instructional_lesson(14, "discourse", l, disc_title, disc_intro if l["num"] == 1 else None)

    # Combined Discourse World Story
    write_json(
        f"stories/world/c1/c1-{slug}.json",
        {
            "id": f"story.c1.{slug}",
            "title": "Fény és hasadás: A magyar energetika és környezetvédelem nagy fejezetei",
            "level": "C1",
            "type": "world",
            "order": 14,
            "lesson": 5,
            "estimatedMinutes": 8,
            "summary": "Panoramic exploration of Hungarian energy history and the green transition: from the construction and lifetime extension of Paks I, the geopolitical dilemmas of Paks II, the trauma and legal battles of Bős-Nagymaros, to Pannonian geothermal district heating and the contemporary solar power boom.",
            "grammar": [
                "c1-ecological-system-dynamics",
                "c1-energy-transition-clauses",
                "c1-green-taxonomy-criteria",
                "c1-nuclear-governance",
                "c1-circular-economy-syntax"
            ],
            "vocabularyTopics": [
                "Nuclear Energy, the Paks Dilemma & Renewables in the Carpathian Basin",
                "Paks I: The Construction and Life-Extension of Hungarian Nuclear Power",
                "Paks II: Geopolitics, Financing & Technology Transfer",
                "Bős–Nagymaros & The Trauma of Damming the Danube",
                "Geothermal Potential of the Pannonian Basin",
                "The Solar Boom & Central European Grid Realities"
            ],
            "paragraphs": [
                {"type": "narration", "text": "A magyar energetika története a természeti adottságok, a technológiai bátorság és a geopolitikai kiszolgáltatottság összefonódó küzdelme. A huszadik század második felében a Tolna megyei Paks mellett felépült négy reaktorblokk a nemzeti áramellátás megingathatatlan bázisává vált, amely ma is szén-dioxid-mentesen fedezi a hazai áramfogyasztás felét."},
                {"type": "narration", "text": "A Paks II beruházás 2014-es moszkvai megállapodása azonban rávilágított arra a mély dilemmára, amely a stabil alapterhelés biztosítása és a geopolitikai függőség elkerülése között feszül egy háborús szankcióktól sújtott európai térben."},
                {"type": "narration", "text": "Ezzel egyidőben a Bős–Nagymaros vízlépcső története a közép-európai zöld mozgalmak bölcsőjévé vált: emlékeztetve arra, hogy a természet megerőszakolása és a határokon átnyúló folyók elterelése jóvátehetetlen sebeket ejt a Szigetköz páratlan ökoszisztémáján."},
                {"type": "narration", "text": "A jövő útja a megújuló források szintézisében bontakozik ki: a Pannon-medence forró mélységi hévízkincse, amelyet Szeged városa Európa-bajnok távfűtési rendszerré formált, időjárásfüggetlen tiszta hőt szolgáltat a lakosságnak."},
                {"type": "narration", "text": "Mindeközben a hatezer megawattot meghaladó napenergia-boom Magyarországot a fotovoltaikus forradalom élvonalába emelte. A huszonegyedik század nagy feladata e tiszta források integrálása: az atomenergia fegyelmének, a geotermia stabilitásának és a napfény bőségének olyan intelligens hálózatba rendezése, amely szavatolja a nemzeti szuverenitást és megóvja a Kárpát-medence törékeny ökológiai jövőjét."}
            ]
        }
    )

    # Discourse Consolidation
    emit_consolidation_lesson(
        14,
        "discourse",
        f"c1-{slug}-consolidation",
        disc_title,
        [
            "I can evaluate the history and 20-year lifetime extension of Paks I nuclear units.",
            "I can analyze the Paks II expansion financing and geopolitical sanctions framework.",
            "I can discuss Bős-Nagymaros riverbed ecology, Pannonian geothermal district heating, and solar grid balancing."
        ],
        [
            mc("grammar", "recognize", "Mi a Paksi Atomerőmű szerepe a hazai dekarbonizációban?", [
                "Szén-dioxid-mentes alapterhelést nyújt, megtermelve a hazai villamos energia mintegy felét.",
                "Kizárólag exportra termel áramot.",
                "Csak az éjszakai órákban működik."
            ], 0, ["c1-nuclear-governance"]),
            mc("grammar", "recognize", "Mi volt a Bős-Nagymaros vízlépcsővita legfőbb ökológiai tanulsága?", [
                "A Duna elterelése drasztikusan károsította az ártéri vizes élőhelyeket és a talajvízszintet a Szigetközben.",
                "Hogy a folyók nem tartalmaznak halakat.",
                "Hogy a beton védelmet nyújt a szárazság ellen."
            ], 0, ["c1-ecological-system-dynamics"]),
            match("vocabulary", "recognize", [["Paks I", "hazai atomerőmű 4 blokkal"], ["Paks II", "két új VVER-1200 reaktor terve"], ["Duna Kör", "rendszerváltó környezetvédő NGO"], ["geotermikus távhő", "hévízzel fűtött szegedi hálózat"], ["negatív áramár", "napenergia túltermelés következménye"]], ["c1-energetika-vocab"]),
            fb("vocabulary", "recall", "A Paks II beruházást nemzetközi szinten a geopolitikai és pénzügyi _____ miatt érte heves bírálat. (dependence / függőség)", "függőség", "The Paks II investment faced fierce criticism internationally due to geopolitical and financial dependence.", ["c1-energetika-vocab"]),
            fb("vocabulary", "recall", "Szeged városa földgáz helyett mélyfúrású _____ alapozta meg a távfűtés dekarbonizációját. (thermal water / hévízre)", "hévízre", "The city of Szeged based the decarbonization of district heating on deep-drilled thermal water instead of natural gas.", ["c1-energetika-vocab"]),
            fb("grammar", "recall", "A meglévő reaktorok biztonságos _____ a legolcsóbb eszköz a tiszta áramkapacitás fenntartására. (lifetime extension / üzemidő-hosszabbítása)", "üzemidő-hosszabbítása", "Safe lifetime extension of existing reactors is the cheapest tool to maintain clean electricity capacity.", ["c1-nuclear-governance"]),
            fb("grammar", "context", "A Hágai Bíróság döntése dacára a Duna elterelése súlyos _____ seb maradt a Szigetközben. (ecological / ökológiai)", "ökológiai", "Despite the Hague Court ruling, the diversion of the Danube remained a severe ecological wound in Szigetköz.", ["c1-ecological-system-dynamics"]),
            fb("grammar", "context", "A fotovoltaikus termelés hirtelen megugrása ipari méretű _____ kapacitások kiépítését teszi elengedhetetlenné. (storage / energiatárolási)", "energiatárolási", "The sudden surge in photovoltaic generation makes the build-out of industrial-scale energy storage capacities indispensable.", ["c1-circular-economy-syntax"]),
            mc("grammar", "context", "Hogyan egészíti ki egymást a geotermia és a napenergia a zöld átállásban?", [
                "A napenergia az áramtermelésben nyújt tiszta forrást, míg a geotermia időjárásfüggetlen zöld hőt szolgáltat a fűtésben.",
                "A napenergia felmelegíti a geotermikus kutakat.",
                "Mindkettő csak éjszaka működik."
            ], 0, ["c1-energy-transition-clauses"]),
            sb("grammar", "produce", ["A", "fenntartható", "energiagazdálkodás", "a", "nemzeti", "szuverenitás", "legfontosabb", "záloga."], ["A", "fenntartható", "energiagazdálkodás", "a", "nemzeti", "szuverenitás", "legfontosabb", "záloga."], "Sustainable energy management is the most important pledge of national sovereignty.", ["c1-energy-transition-clauses"]),
            sw("production", [{"prompt": "Write a critical evaluation of Hungary's energy transition balancing nuclear and renewables.", "answer": "Magyarország energetikai jövője a nukleáris energia által garantált stabil alapterhelés, a geotermikus hőhasznosítás és a tárolókkal megtámasztott napenergia szerves ötvözésén múlik, amely egyszerre csökkenti a karbonkibocsátást és az importkitettséget."}], ["c1-energy-transition-clauses"]),
            sw("production", [{"prompt": "Formulate a concluding thought on environmental ethics in water management and energy.", "answer": "A Bős-Nagymaros vita és a Kis-Balaton ökológiai tanulsága arra figyelmeztet, hogy az energetikai beruházások nem írhatják felül a természet törvényeit: a táji egyensúly megőrzése minden gazdasági haszonnál előbbre való."}], ["c1-ecological-system-dynamics"])
        ]
    )

    print("=== Finished C1 Unit 14 ===")


if __name__ == "__main__":
    generate_unit_14()
