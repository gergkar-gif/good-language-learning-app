#!/usr/bin/env python3
"""
Hungarian C1 Block 5 - Unit 28 Generator:
  - Track 1 (Core): Unit 28 — "Transport Geography, Railway Modernization & Modal Infrastructure" (c1-28)
  - Track 2 (Discourse): Unit 28 — "Railway Decay vs. Highway Megaprojects: The MÁV Crisis, Branch Closures & Concessions" (c1-kozlekedespolitika)
"""

import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT))

from scripts.c1_block1.common import mc, match, fb, sb, dc, sw, write_json, emit_instructional_lesson, emit_consolidation_lesson
from scripts.c1_block5.registry_helper import register_unit


def generate_unit_28():
    print("=== Generating C1 Unit 28 ===")
    
    new_skills = {
        "c1-28-vocab": {"kind": "vocabulary"},
        "c1-kozlekedespolitika-vocab": {"kind": "vocabulary"},
        "c1-adv-infrastructural-efficiency-logistics": {"kind": "grammar"},
        "c1-participle-multimodal-connectivity": {"kind": "grammar"},
        "c1-adv-adversative-modal-shift": {"kind": "grammar"},
        "c1-modal-teleological-network-planning": {"kind": "grammar"},
        "c1-adv-scalar-macroeconomic-integration": {"kind": "grammar"},
        "c1-discourse-railway-crisis-framing": {"kind": "grammar"},
        "c1-modal-deontic-public-mobility-rights": {"kind": "grammar"},
        "c1-adv-proportional-concession-deficits": {"kind": "grammar"},
        "c1-epistemic-geopolitical-megaproject-critique": {"kind": "grammar"},
        "c1-adv-conclusive-green-transit-synthesis": {"kind": "grammar"},
    }
    new_titles = {
        "c1-28-vocab": "reading",
        "c1-kozlekedespolitika-vocab": "reading",
        "c1-adv-infrastructural-efficiency-logistics": "infrastructural efficiency adverbials evaluating network logistics and transport capacities",
        "c1-participle-multimodal-connectivity": "complex participial structures mapping multimodal connectivity and regional network integration",
        "c1-adv-adversative-modal-shift": "adversative connectors contrasting road transport expansion with sustainable rail transit",
        "c1-modal-teleological-network-planning": "teleological modal structures framing national railway electrification and modernization goals",
        "c1-adv-scalar-macroeconomic-integration": "scalar evaluative adverbials calibrating transport infrastructure impact on national development",
        "c1-discourse-railway-crisis-framing": "discourse framing markers diagnosing rolling stock obsolescence and railway collapse",
        "c1-modal-deontic-public-mobility-rights": "deontic modal structures asserting statutory citizen rights to public transport access",
        "c1-adv-proportional-concession-deficits": "proportional correlative conjunctions mapping highway concession costs against railway underfunding",
        "c1-epistemic-geopolitical-megaproject-critique": "epistemic stance markers critiquing nontransparent infrastructure megaprojects and debt traps",
        "c1-adv-conclusive-green-transit-synthesis": "evaluative synthesis particles formulating comprehensive manifestos for sustainable public mobility",
    }
    
    core_title = "Transport Geography, Railway Modernization & Modal Infrastructure"
    core_stems = [f"c1-28-0{i}" for i in range(1, 6)] + ["c1-28-consolidation"]
    disc_title = "Railway Decay vs. Highway Megaprojects: The MÁV Crisis, Branch Closures & Concessions"
    disc_stems = [f"c1-kozlekedespolitika-0{i}" for i in range(1, 6)] + ["c1-kozlekedespolitika-consolidation"]
    
    register_unit(28, core_title, core_stems, disc_title, disc_stems, new_skills, new_titles)

    # ----------------------------------------------------
    # TRACK 1: CORE (c1-28)
    # ----------------------------------------------------
    core_intro = [
        "A country's transport infrastructure is the circulatory system of its economy, social integration, and territorial cohesion. In 19th-century Hungary, Gábor Baross ('a vasminiszter') pioneered modern transport policy through the nationalization of railway trunk lines and the revolutionary zone-tariff system, unlocking unprecedented mobility for citizens and industry alike.",
        "In this unit, grounded in Baross Gábor's visionary economic essays 'A zónatarifa és a nemzeti vasútpolitika' (1889), you will master the elevated academic register of transport geography, multimodal logistics, network topology, infrastructure planning, and green modal shifts at the C1 level."
    ]

    core_lessons = [
        {
            "num": 1,
            "stem": "c1-28-01",
            "title": "Logistics Efficiency & Infrastructural Adverbials",
            "grammar_title": "Infrastructural Efficiency Adverbials Evaluating Network Logistics and Transport Capacities",
            "grammar_skill": "c1-adv-infrastructural-efficiency-logistics",
            "goals": [
                "I can analyze transport logistics, network topology, and capacity utilization (*hálózati topológia, kapacitáskihasználtság, intermodális csomópont, logisztikai hatékonyság*).",
                "I can employ elevated infrastructural efficiency adverbials (*logisztikailag optimálisan, hálózatilag összehangoltan, üzemgazdaságilag kifizetődő módon*).",
                "I can evaluate freight transit routes and passenger flow models in technical academic prose."
            ],
            "vocab": [
                {"lemma": "hálózati topológia", "translation": "network topology", "pos": "expression"},
                {"lemma": "kapacitáskihasználtság", "translation": "capacity utilization", "pos": "noun"},
                {"lemma": "intermodális csomópont", "translation": "intermodal hub / terminal", "pos": "expression"},
                {"lemma": "kötöttpályás közlekedés", "translation": "rail / fixed-track transport", "pos": "expression"},
                {"lemma": "átbocsátóképesség", "translation": "throughput capacity", "pos": "noun"},
                {"lemma": "forgalomszervezés", "translation": "traffic management / organization", "pos": "noun"},
                {"lemma": "törzshálózat", "translation": "trunk network / core corridor", "pos": "noun"},
                {"lemma": "menetrendi szinkron", "translation": "timetable synchronization (takt)", "pos": "expression"}
            ],
            "gr_text1": "Infrastructural efficiency adverbials formulate technical evaluations of network performance and logistics synergy: `logisztikailag optimálisan megtervezett útvonal` (logistically optimally planned route), `hálózatilag összehangolt menetrend` (network-wise synchronized timetable), `üzemgazdaságilag kifizetődő módon működtetett vonal` (line operated in an operationally profitable manner), `kapacitáskihasználtság szempontjából kiemelkedően` (outstanding in terms of capacity utilization).",
            "gr_text2": "Example: `A vasúttársaság logisztikailag optimálisan, hálózatilag összehangoltan szervezte meg a személy- és teherforgalom menetrendi szinkronját`.",
            "gr_table": [
                ["A járatok logisztikailag optimálisan csatlakoznak a fővonalakhoz.", "Services logistically optimally connect to main lines."],
                ["Hálózatilag összehangoltan kell megtervezni az átszállási pontokat.", "Transfer points must be planned network-wise synchronized."],
                ["A vonal üzemgazdaságilag kifizetődően szállítja a nemzetközi teherárut.", "The line operationally profitably carries international freight."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mit jelent az 'intermodális csomópont' a korszerű közlekedésföldrajzban?", [
                    "Olyan közlekedési állomást vagy terminált, ahol a különböző közlekedési módok (vasút, közút, kerékpár, vízi út) közvetlenül és akadálymentesen kapcsolódnak egymáshoz.",
                    "Egy olyan vasúti váltót, amit csak kézzel lehet átállítani.",
                    "A kalauzok pihenőszobáját a pályaudvaron."
                ], 0, ["c1-28-vocab"]),
                fb("grammar", "controlled", "A vasútvonalakat _____ optimálisan kell integrálni az európai folyosókba. (logistically / logisztikailag)", "logisztikailag", "Railway lines must be logistically optimally integrated into European corridors.", ["c1-adv-infrastructural-efficiency-logistics"]),
                match("vocabulary", "controlled", [["hálózati topológia", "a közlekedési vonalak térbeli elrendeződése"], ["átbocsátóképesség", "a pálya által egységnyi idő alatt átengedhető vonatok száma"], ["menetrendi szinkron", "csatlakozásokat biztosító ütemes menetrend"], ["kötöttpályás közlekedés", "síneken futó vasúti és villamoshálózat"]], ["c1-28-vocab"]),
                fb("grammar", "practice", "A menetrendet hálózatilag _____ módon dolgozták ki az átszállások megkönnyítésére. (synchronized / összehangolt)", "összehangolt", "The timetable was elaborated in a network-wise synchronized manner to facilitate transfers.", ["c1-adv-infrastructural-efficiency-logistics"]),
                sb("grammar", "practice", ["A", "vasút", "logisztikailag", "optimálisan", "szolgálja", "ki", "az", "ipari", "parkokat."], ["A", "vasút", "logisztikailag", "optimálisan", "szolgálja", "ki", "az", "ipari", "parkokat."], "The railway logistically optimally serves the industrial parks.", ["c1-adv-infrastructural-efficiency-logistics"]),
                dc("dialogue", [
                    {"speaker": "Közlekedésmérnök", "text": "Hogyan csökkenthetjük az agglomerációs ingázás menetidejét?"},
                    {"speaker": "Tervező", "text": "Csak akkor, ha hálózatilag _____ ütemes menetrendet és intermodális csomópontokat létesítünk."},
                    {"speaker": "Közlekedésmérnök", "text": "Akkor erre alapozzuk az új vasútfejlesztési tervet."}
                ], ["összehangolt", "véletlen", "lassú"], 0, ["c1-adv-infrastructural-efficiency-logistics"]),
                sw("production", [{"prompt": "Write a sentence evaluating transport efficiency using an infrastructural adverbial.", "answer": "Az új törzshálózati fejlesztés logisztikailag optimálisan, a menetrendi szinkront hálózatilag összehangoltan biztosítva növeli a vasúti áruszállítás átbocsátóképességét."}], ["c1-adv-infrastructural-efficiency-logistics"]),
                mc("grammar", "check", "Melyik határozói kifejezés méri a logisztikai hálózat működését a legszakszerűbben?", [
                    "logisztikailag optimálisan / hálózatilag összehangoltan",
                    "többnyire vidám vonatozással",
                    "időnként dudálva"
                ], 0, ["c1-adv-infrastructural-efficiency-logistics"])
            ]
        },
        {
            "num": 2,
            "stem": "c1-28-02",
            "title": "Multimodal Connectivity & Participial Integration",
            "grammar_title": "Complex Participial Structures Mapping Multimodal Connectivity and Regional Network Integration",
            "grammar_skill": "c1-participle-multimodal-connectivity",
            "goals": [
                "I can analyze multimodal transport networks, suburban commuter lines, and regional connectivity (*multimodális hálózat, elővárosi közlekedés, agglomerációs integráció, P+R parkolók*).",
                "I can construct complex participial structures detailing transport integration (*a vasutat a busszal összekapcsoló, az agglomerációt tehermentesítő, az utasforgalmat lebonyolító*).",
                "I can critique regional spatial connectivity models in transport economics register."
            ],
            "vocab": [
                {"lemma": "multimodalitás", "translation": "multimodality", "pos": "noun"},
                {"lemma": "elővárosi vasút", "translation": "suburban / commuter rail (S-Bahn)", "pos": "expression"},
                {"lemma": "agglomerációs ingázás", "translation": "metropolitan commuting", "pos": "expression"},
                {"lemma": "hálózati integráció", "translation": "network integration", "pos": "expression"},
                {"lemma": "térségi elérhetőség", "translation": "regional accessibility", "pos": "expression"},
                {"lemma": "tehermentesítés", "translation": "traffic relief / decongestion", "pos": "noun"},
                {"lemma": "járműpark-megújítás", "translation": "fleet renewal / rolling stock renewal", "pos": "expression"},
                {"lemma": "P+R rendszer", "translation": "Park and Ride system", "pos": "expression"}
            ],
            "gr_text1": "Complex participial structures specify the functional linkages between transportation modes: `a vasutat az autóbusz-hálózattal összekapcsoló intermodális terminál` (intermodal terminal linking railway with bus network), `az agglomerációs közúti forgalmat tehermentesítő elővárosi vasút` (commuter rail relieving suburban road traffic), `a térségi elérhetőséget javító integrált díjszabás` (integrated tariff improving regional accessibility).",
            "gr_text2": "Example: `A főváros körüli, a kötöttpályás vonalakat P+R parkolókkal összekötő és a belvárost tehermentesítő elővárosi rendszer megduplázta az utasszámot`.",
            "gr_table": [
                ["A vasúti és buszjáratokat összehangoló közös jegyrendszer megkönnyíti az utazást.", "The common ticketing system coordinating train and bus services facilitates travel."],
                ["Az autópályákat tehermentesítő vasúti folyosók környezetvédelmi jelentősége óriási.", "Environmental significance of rail corridors relieving motorways is huge."],
                ["A periférikus régiókat bekötő szárnyvonalak elengedhetetlenek a helyi közösségeknek.", "Branch lines connecting peripheral regions are indispensable for local communities."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mi a lényege a 'multimodalitásnak' az utasok szemszögéből?", [
                    "Az utazási lánc zökkenőmentes megvalósítása különböző közlekedési eszközök (pl. kerékpár, vonat, villamos) összehangolt igénybevételével.",
                    "A vonatok több színre való lefestése.",
                    "Különböző nyelvű újságok olvasása a fülkében."
                ], 0, ["c1-28-vocab"]),
                fb("grammar", "controlled", "A közúti forgalmat hatékonyan _____ kötöttpályás beruházások zöld jövőt teremtenek. (relieving / tehermentesítő)", "tehermentesítő", "Fixed-track investments effectively relieving road traffic create a green future.", ["c1-participle-multimodal-connectivity"]),
                match("vocabulary", "controlled", [["multimodalitás", "több közlekedési eszköz zökkenőmentes kombinációja"], ["elővárosi vasút", "nagyvárosok vonzáskörzetét kiszolgáló gyorsvasút"], ["térségi elérhetőség", "egy régió megközelíthetőségének gyorsasága"], ["P+R rendszer", "parkolóhelyek létesítése a vasútállomások mellett"]], ["c1-28-vocab"]),
                fb("grammar", "practice", "A buszokat a vonatokkal _____ menetrendi reform vonzóvá tette az ingázást. (connecting / összekapcsoló)", "összekapcsoló", "The timetable reform connecting buses with trains made commuting attractive.", ["c1-participle-multimodal-connectivity"]),
                sb("grammar", "practice", ["A", "vasutat", "és", "buszt", "összekapcsoló", "terminál", "megkönnyíti", "az", "átszállást."], ["A", "vasutat", "és", "buszt", "összekapcsoló", "terminál", "megkönnyíti", "az", "átszállást."], "The terminal connecting train and bus facilitates transferring.", ["c1-participle-multimodal-connectivity"]),
                dc("dialogue", [
                    {"speaker": "Várostervező", "text": "Hogyan szüntethetjük meg a reggeli autós dugókat az autópálya-bevezetőn?"},
                    {"speaker": "Vasúti szakértő", "text": "Kizárólag az agglomerációt hatékonyan _____ és P+R parkolókkal ellátott elővárosi gyorsvasúttal."},
                    {"speaker": "Várostervező", "text": "Ezért kell sűríteni a vasúti járatokat."}
                ], ["tehermentesítő", "lassító", "zavaró"], 0, ["c1-participle-multimodal-connectivity"]),
                sw("production", [{"prompt": "Write a sentence detailing multimodal transit integration using a participial modifier.", "answer": "A vasúti törzshálózatot a helyközi buszokkal harmonikusan összekapcsoló és a térségi elérhetőséget javító közlekedési szövetségek jelentik az élhető régiók alapját."}], ["c1-participle-multimodal-connectivity"]),
                mc("grammar", "check", "Melyik melléknévi igeneves szerkezet fejezi ki a hálózati összekapcsoltságot a legpontosabban?", [
                    "a kötöttpályás vonalakat a buszhálózattal harmonikusan összekapcsoló",
                    "az állomáson békésen várakozó utasok",
                    "egy szép zöldre festett új mozdony"
                ], 0, ["c1-participle-multimodal-connectivity"])
            ]
        },
        {
            "num": 3,
            "stem": "c1-28-03",
            "title": "Modal Shift & Adversative Transit Connectors",
            "grammar_title": "Adversative Connectors Contrasting Road Transport Expansion with Sustainable Rail Transit",
            "grammar_skill": "c1-adv-adversative-modal-shift",
            "goals": [
                "I can analyze modal shift policies, carbon footprint of transport, and highway saturation (*modális váltás, karbonlábnyom, közúti telítettség, klímabarát tranzit*).",
                "I can deploy elevated adversative connectors contrasting road vs. rail transit (*a környezetszennyező közúti szállítással szemben a valóságban, nemhogy nem gazdaságtalan a vasút, hanem éppen környezetkímélő, mindazonáltal stratégiailag nélkülözhetetlen*).",
                "I can argue against short-sighted highway expansion in climate policy debates."
            ],
            "vocab": [
                {"lemma": "modális váltás", "translation": "modal shift (from road to rail)", "pos": "expression"},
                {"lemma": "karbonlábnyom", "translation": "carbon footprint", "pos": "noun"},
                {"lemma": "közúti telítettség", "translation": "road saturation / congestion", "pos": "expression"},
                {"lemma": "kamionforgalom", "translation": "heavy truck / freight traffic", "pos": "noun"},
                {"lemma": "klímasemlegesség", "translation": "climate neutrality", "pos": "noun"},
                {"lemma": "energiahatékonyság", "translation": "energy efficiency", "pos": "noun"},
                {"lemma": "aszfaltozási lobbi", "translation": "asphalt / highway construction lobby", "pos": "expression"},
                {"lemma": "külső környezeti kár", "translation": "external environmental cost", "pos": "expression"}
            ],
            "gr_text1": "Adversative connectors emphasize the ecological superiority and efficiency of rail over asphalt dominance: `a környezetterhelő kamionos áruszállítással szemben a vasút` (in contrast with environmentally polluting truck transport rail), `nemhogy nem veszteséges a kötöttpályás fejlesztés, hanem éppen energiatakarékos` (far from fixed-track development being loss-making, but rather energy-saving), `mindazonáltal ökológiailag cáfolhatatlan előnyt élvez` (nevertheless enjoys ecologically irrefutable advantage).",
            "gr_text2": "Example: `A folyamatos autópálya-építéssel szemben a valóságban nemhogy nem oldódnak meg a dugók, hanem éppen a vasútra való modális váltás jelenthet fenntartható kiutat`.",
            "gr_table": [
                ["A környezetszennyező kamionforgalommal szemben a vasút energiatakarékos.", "In contrast with polluting truck traffic rail is energy-saving."],
                ["A vasút nemhogy nem elavult, hanem éppen a jövő zöld közlekedési eszköze.", "Rail is far from obsolete; on the contrary, it is the green transport tool of the future."],
                ["A beruházás mindazonáltal ökológiailag vitathatatlan előnyöket biztosít.", "The investment nevertheless secures ecologically indisputable benefits."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mit jelent a 'modális váltás' (modal shift) a fenntartható közlekedéspolitikában?", [
                    "A személy- és teherforgalom tudatos átterelését a környezetszennyező közúti és légi szállításból a környezetkímélő vasúti és vízi közlekedésbe.",
                    "A vezetői engedélyek megújítását ötévente.",
                    "Az autóbuszok üléshuzatának cseréjét."
                ], 0, ["c1-28-vocab"]),
                fb("grammar", "controlled", "A szennyező kamionforgalommal szemben a _____ a kötöttpályás szállítás harmadannyi energiát fogyaszt. (in reality / valóságban)", "valóságban", "Contrary to polluting truck traffic, in reality fixed-track transport consumes one third the energy.", ["c1-adv-adversative-modal-shift"]),
                match("vocabulary", "controlled", [["modális váltás", "forgalom átterelése közútról kötöttpályára"], ["karbonlábnyom", "közlekedés által kibocsátott üvegházhatású gáz"], ["külső környezeti kár", "zaj, légszennyezés és baleseti költségek"], ["klímasemlegesség", "zéró nettó károsanyag-kibocsátás elérése"]], ["c1-28-vocab"]),
                fb("grammar", "practice", "A villamosított vasút nemhogy nem környezetszennyező, hanem éppen klímabarát _____ bizonyult. (transit / tranzitnak)", "tranzitnak", "Electrified rail is far from polluting; on the contrary, it proved to be climate-friendly transit.", ["c1-adv-adversative-modal-shift"]),
                sb("grammar", "practice", ["A", "közúti", "lobbival", "szemben", "a", "vasút", "a", "jövő", "záloga."], ["A", "közúti", "lobbival", "szemben", "a", "vasút", "a", "jövő", "záloga."], "Against the road lobby rail is the pledge of the future.", ["c1-adv-adversative-modal-shift"]),
                dc("dialogue", [
                    {"speaker": "Zöld aktivista", "text": "Megoldást jelent-e az új autópályasávok építése a közlekedési dugókra?"},
                    {"speaker": "Közgazdász", "text": "Nem; az aszfaltozással szemben a valóságban nemhogy nem csökken a forgalom, hanem éppen a vasúti modális váltás hozhat _____ enyhülést."},
                    {"speaker": "Zöld aktivista", "text": "Ezért kell a forrásokat a vasútba fektetni."}
                ], ["valódi", "lassú", "drága"], 0, ["c1-adv-adversative-modal-shift"]),
                sw("production", [{"prompt": "Write a sentence arguing for a modal shift to rail using 'A közúttal szemben a valóságban'.", "answer": "A folyamatos autópálya-bővítéssel szemben a valóságban a vasúti korszerűsítés nemhogy nem elavult, hanem éppen a modális váltás és a klímasemlegesség egyetlen járható útja."}], ["c1-adv-adversative-modal-shift"]),
                mc("grammar", "check", "Melyik kötőszószerkezet állítja szembe a vasút és a közút fenntarthatóságát a leghatásosabban?", [
                    "A közúti környezetszennyezéssel szemben a valóságban nemhogy nem... hanem éppen",
                    "Lehet hogy jobb autóval menni nyáron",
                    "Ha nem jön a busz, gyalogolunk"
                ], 0, ["c1-adv-adversative-modal-shift"])
            ]
        },
        {
            "num": 4,
            "stem": "c1-28-04",
            "title": "Railway Modernization & Teleological Planning",
            "grammar_title": "Teleological Modal Structures Framing National Railway Electrification and Modernization Goals",
            "grammar_skill": "c1-modal-teleological-network-planning",
            "goals": [
                "I can analyze railway electrification, European TEN-T corridors, and high-speed rail masterplans (*vasútvillamosítás, TEN-T hálózat, ETCS biztosítóberendezés, nagysebességű vasút*).",
                "I can employ teleological modal structures framing infrastructure goals (*a menetidő radikális csökkentése céljából, a zöld átállás elősegítése végett, az interoperabilitás biztosítása érdekében*).",
                "I can evaluate long-term national railway development strategies."
            ],
            "vocab": [
                {"lemma": "vasútvillamosítás", "translation": "railway electrification", "pos": "noun"},
                {"lemma": "TEN-T folyosó", "translation": "Trans-European Transport Network (TEN-T) corridor", "pos": "expression"},
                {"lemma": "ETCS rendszer", "translation": "European Train Control System (ETCS)", "pos": "noun"},
                {"lemma": "nagysebességű vasút", "translation": "high-speed railway (HSR)", "pos": "expression"},
                {"lemma": "pályafelújítás", "translation": "track renewal / track reconstruction", "pos": "noun"},
                {"lemma": "interoperabilitás", "translation": "interoperability", "pos": "noun"},
                {"lemma": "tengelyterhelés", "translation": "axle load", "pos": "noun"},
                {"lemma": "menetidő-csökkentés", "translation": "travel time reduction", "pos": "expression"}
            ],
            "gr_text1": "Teleological postpositional phrases specify strategic infrastructure investments: `a menetidő radikális csökkentése céljából` (for the purpose of radically reducing travel time), `az európai interoperabilitás megteremtése végett` (with a view to creating European interoperability), `a teherforgalom gyorsítása érdekében` (in the interest of accelerating freight traffic), `a zöld mobilitásra való áttérés biztosítására törekedve` (striving to secure transition to green mobility).",
            "gr_text2": "Example: `A kormány a nemzetközi folyosók interoperabilitásának megteremtése céljából új ETCS biztosítóberendezéseket telepített a menetbiztonság növelése végett`.",
            "gr_table": [
                ["A menetidő csökkentése céljából felújították a fővonali pályaszakaszokat.", "For the purpose of reducing travel time they reconstructed main line track sections."],
                ["A dízelvontatás kiváltása végett átfogó villamosítási program indult.", "With a view to replacing diesel traction a comprehensive electrification program was launched."],
                ["A vasúti biztonság fokozása érdekében modern ETCS rendszert építettek ki.", "In the interest of enhancing railway safety they deployed a modern ETCS system."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mi a szerepe az európai ETCS (European Train Control System) biztosítóberendezésnek a modern vasúton?", [
                    "Egységes európai digitális vonatbefolyásoló rendszer, amely megakadályozza a vonatok ütközését és lehetővé teszi a határokon átnyúló mozdonyközlekedést.",
                    "Egy automata jegykezelő automata a restiben.",
                    "A kalauzok egyenruhájának tisztítására szolgáló gép."
                ], 0, ["c1-28-vocab"]),
                fb("grammar", "controlled", "A menetidő radikális csökkentése _____ átfogó pályafelújítás kezdődött a keleti országrészben. (for the purpose of / céljából)", "céljából", "For the purpose of radically reducing travel time comprehensive track renewal began in the eastern region.", ["c1-modal-teleological-network-planning"]),
                match("vocabulary", "controlled", [["vasútvillamosítás", "felsővezeték kiépítése a dízelmozdonyok kiváltására"], ["TEN-T folyosó", "kiemelt páneurópai közlekedési fővonal"], ["interoperabilitás", "vasúti rendszerek határokon átnyúló műszaki kompatibilitása"], ["ETCS rendszer", "európai digitális vonatbefolyásoló rendszer"]], ["c1-28-vocab"]),
                fb("grammar", "practice", "A határkeresztező interoperabilitás megteremtése _____ modern mozdonyokat vásárolt a vasút. (with a view to / végett)", "végett", "With a view to creating cross-border interoperability the railway purchased modern locomotives.", ["c1-modal-teleological-network-planning"]),
                sb("grammar", "practice", ["A", "menetidő", "csökkentése", "érdekében", "korszerűsítették", "a", "vasúti", "pályát."], ["A", "menetidő", "csökkentése", "érdekében", "korszerűsítették", "a", "vasúti", "pályát."], "In the interest of reducing travel time they modernized the railway track.", ["c1-modal-teleological-network-planning"]),
                dc("dialogue", [
                    {"speaker": "Közlekedéspolitikus", "text": "Miért szükséges a nemzetközi folyosók teljes villamosítása?"},
                    {"speaker": "Főmérnök", "text": "A szén-dioxid-kibocsátás visszaszorítása és a gazdasági versenyképesség növelése _____ nélkülözhetetlen a felsővezeték."},
                    {"speaker": "Közlekedéspolitikus", "text": "Akkor erre pályázunk uniós forrásokra."}
                ], ["végett", "dacára", "kárára"], 0, ["c1-modal-teleological-network-planning"]),
                sw("production", [{"prompt": "Write a sentence formulating an infrastructure modernization goal using 'céljából' or 'végett'.", "answer": "A vasúti törzshálózat átbocsátóképességének növelése és az európai interoperabilitás megteremtése céljából a mérnökök új ETCS rendszereket telepítettek a menetidő csökkentése végett."}], ["c1-modal-teleological-network-planning"]),
                mc("grammar", "check", "Melyik névutós szerkezet fejez ki infrastrukturális célkitűzést emelkedett technikai regiszterben?", [
                    "a menetidő radikális csökkentése céljából / a versenyképesség növelése végett",
                    "hogy ne unatkozzon a mozdonyvezető",
                    "mert szép új síneket találtak a raktárban"
                ], 0, ["c1-modal-teleological-network-planning"])
            ]
        },
        {
            "num": 5,
            "stem": "c1-28-05",
            "title": "Baross Gábor: The Zone Tariff & Macroeconomic Integration",
            "grammar_title": "Scalar Evaluative Adverbials Calibrating Transport Infrastructure Impact on National Development",
            "grammar_skill": "c1-adv-scalar-macroeconomic-integration",
            "goals": [
                "I can analyze Baross Gábor's railway nationalization, the zone-tariff revolution (1889), and national market integration.",
                "I can deploy scalar evaluative adverbials calibrating economic transformation (*nemzetgazdaságilag felbecsülhetetlen mértékben, társadalomföldrajzilag meghatározó módon, a fejlődést alapjaiban felgyorsítva*).",
                "I can synthesize the historical lessons of the Dualist era's infrastructural golden age."
            ],
            "vocab": [
                {"lemma": "zónatarifa-rendszer", "translation": "zone-tariff system (1889)", "pos": "expression"},
                {"lemma": "vasútállamosítás", "translation": "railway nationalization", "pos": "noun"},
                {"lemma": "nemzetgazdasági integráció", "translation": "national economic integration", "pos": "expression"},
                {"lemma": "vasminiszter", "translation": "Iron Minister (Baross Gábor)", "pos": "noun"},
                {"lemma": "egységes díjszabás", "translation": "unified tariff", "pos": "expression"},
                {"lemma": "társadalmi mobilitás", "translation": "social mobility", "pos": "expression"},
                {"lemma": "belső piac egységesülése", "translation": "internal market unification", "pos": "expression"},
                {"lemma": "infrastrukturális aranykor", "translation": "infrastructural golden age", "pos": "expression"}
            ],
            "gr_text1": "Scalar evaluative adverbials calibrate the monumental socioeconomic transformations sparked by public infrastructure: `nemzetgazdaságilag felbecsülhetetlen mértékben` (to an inestimable degree national-economically), `társadalomföldrajzilag meghatározó módon` (in a socio-geographically defining manner), `a polgárosodást és iparosodást alapjaiban felgyorsítva` (fundamentally accelerating bourgeois development and industrialization), `történelmi távlatban is példaértékűen` (exemplary even in historical perspective).",
            "gr_text2": "Example: `Baross Gábor zónatarifája nemzetgazdaságilag felbecsülhetetlen mértékben, az ország belső piacát egységesítve forradalmasította a magyar személy- és áruszállítást`.",
            "gr_table": [
                ["Baross reformja nemzetgazdaságilag felbecsülhetetlen mértékben segítette a magyar ipart.", "Baross's reform to an inestimable degree national-economically helped Hungarian industry."],
                ["A zónarendszer társadalomföldrajzilag meghatározó módon tette elérhetővé a fővárost.", "The zone system in a socio-geographically defining manner made the capital accessible."],
                ["A vasútállamosítás az ország modernizációját alapjaiban felgyorsítva teremtett jólétet.", "Railway nationalization fundamentally accelerating the country's modernization created prosperity."]
            ],
            "classic_story": {
                "slug": "baross-zonatarifa-vasut",
                "title": "A zónatarifa és a nemzeti vasútpolitika",
                "author": "Baross Gábor",
                "work": "A zónatarifa és a nemzeti vasútpolitika (1889)",
                "summary": "Baross Gábor, a dualizmus korszakának legendás 'vasminisztere' felismerte, hogy a magánvasúti társaságok kaotikus, drága és külföldi érdekeket szolgáló tarifái megbénítják a magyar gazdaságot. Államosította a fővonalakat, megteremtette a Magyar Királyi Államvasutakat (MÁV), és 1889-ben bevezette a zseniális zónatarifát. A távolsági utazást radikálisan olcsóvá tevő rendszer nyomán az utasszám egyetlen év alatt a négyszeresére nőtt, s a magyar mezőgazdaság és ipar árui akadálytalanul jutottak el a fiumei tengeri kikötőbe és Európa piacaiba.",
                "characters": ["Baross Gábor, a vasminiszter és gazdasági látnok"],
                "paragraphs": [
                    {"type": "narration", "text": "A tizenkilencedik század végén a magyar gazdaság sorsa a síneken dőlt el. Az Osztrák-Magyar Monarchia idején a magánvasutak kartelljei gátlástalanul sarcolták meg a hazai gabonatermelőket és kereskedőket, s az egyszerű polgár számára a vasúti utazás elérhetetlen luxusnak számított."},
                    {"type": "dialogue", "speaker": "Baross Gábor", "text": "A vasút nem a magántőke spekulációjának eszköze, hanem a nemzet közös vérkeringése! Az államnak kötelessége kézbe venni a fővonalakat, és olyan tarifát adni a nép kezébe, amely a legtávolabbi székely falut és az alföldi tanyát is összeköti Budapesttel és a fiumei kikötővel."},
                    {"type": "narration", "text": "1889. augusztus 1-jén életbe lépett a zónatarifa: a távolsági zónákban a jegyárak a korábbi töredékére zuhantak. A hatás felrobbantotta a statisztikákat: parasztok, kisiparosok, diákok milliói keltek útra, s a MÁV bevételei a tarifa csökkentése ellenére megduplázódtak az óriási forgalomnövekedés révén."},
                    {"type": "narration", "text": "Baross Gábor nemzetgazdaságilag felbecsülhetetlen mértékben forradalmasította a magyar közlekedést: a fejlődést alapjaiban felgyorsítva tette Magyarországot modern, integrált közép-európai állammá, megteremtve a kötöttpályás közlekedés máig fénylő aranykorát."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Hogyan működött Baross Gábor 1889-es 'zónatarifa-rendszere'?", [
                    "Koncentrikus zónákra osztotta az országot, és a távoli zónákban fix, rendkívül alacsony díjakat szabott meg, így a messziről utazók kilométerenként sokkal kevesebbet fizettek.",
                    "Csak a vasárnapi vonatokra adott 5% kedvezményt a katonáknak.",
                    "Megkövetelte, hogy minden utas hozzon magával egy zsák búzát a fűtéshez."
                ], 0, ["c1-28-vocab"]),
                fb("grammar", "controlled", "Baross Gábor reformja nemzetgazdaságilag _____ mértékben lendítette fel a hazai kereskedelmet. (to an inestimable / felbecsülhetetlen)", "felbecsülhetetlen", "Gábor Baross's reform to an inestimable degree boosted domestic commerce.", ["c1-adv-scalar-macroeconomic-integration"]),
                match("vocabulary", "controlled", [["vasminiszter", "Baross Gábor tisztelt megnevezése"], ["zónatarifa-rendszer", "a távolsági utazást radikálisan megolcsóbbító díjszabás"], ["vasútállamosítás", "a magánvonalak állami tulajdonba vétele"], ["infrastrukturális aranykor", "a magyar vasútépítés dualizmuskori fénykora"]], ["c1-28-vocab"]),
                fb("grammar", "practice", "A zónarendszer társadalomföldrajzilag _____ módon integrálta a távoli régiókat. (defining / meghatározó)", "meghatározó", "The zone system in a socio-geographically defining manner integrated distant regions.", ["c1-adv-scalar-macroeconomic-integration"]),
                sb("grammar", "practice", ["A", "vasútállamosítás", "alapjaiban", "gyorsította", "fel", "a", "magyar", "gazdaságot."], ["A", "vasútállamosítás", "alapjaiban", "gyorsította", "fel", "a", "magyar", "gazdaságot."], "Railway nationalization fundamentally accelerated the Hungarian economy.", ["c1-adv-scalar-macroeconomic-integration"]),
                mc("reading", "context", "Miért tekintették zseniális lépésnek a zónatarifát a kortársak?", [
                    "Mert a jegyárak drasztikus csökkentése nem csődöt hozott, hanem a négyszeresére ugró forgalom révén megduplázta a MÁV bevételeit és egyesítette a nemzeti piacot.",
                    "Mert Baross ingyen adott mozdonyokat a földbirtokosoknak.",
                    "Mert a vonatokon ingyen szolgálták fel az ebédet."
                ], 0, ["c1-28-vocab"]),
                sw("production", [{"prompt": "Write a reflection on Baross Gábor's transport reforms using a scalar integration adverbial.", "answer": "Baross Gábor nemzetgazdaságilag felbecsülhetetlen mértékben, a gazdasági fejlődést alapjaiban felgyorsítva bizonyította be, hogy a kötöttpályás infrastruktúra állami fejlesztése a nemzeti integráció legfőbb motorja."}], ["c1-adv-scalar-macroeconomic-integration"]),
                mc("grammar", "check", "Melyik határozó fejezi ki a makrogazdasági hatást a legmagasabb elméleti regiszterben?", [
                    "nemzetgazdaságilag felbecsülhetetlen mértékben / társadalomföldrajzilag meghatározó módon",
                    "meglehetősen jól sikerült módon",
                    "egy szép napon váratlanul"
                ], 0, ["c1-adv-scalar-macroeconomic-integration"])
            ]
        }
    ]

    for l in core_lessons:
        emit_instructional_lesson(28, "core", l, core_title, core_intro if l["num"] == 1 else None)

    # Core Consolidation Lesson
    emit_consolidation_lesson(
        28,
        "core",
        "c1-28-consolidation",
        core_title,
        [
            "I can master the academic vocabulary of transport geography, multimodal logistics, and railway engineering.",
            "I can employ logistical efficiency adverbials, participial connectivity structures, and adversative modal-shift connectors.",
            "I can evaluate teleological infrastructure planning and synthesize Baross Gábor's macroeconomic zone-tariff model."
        ],
        [
            mc("grammar", "recognize", "Melyik kifejezés jellemez szakszerűen egy korszerű logisztikai hálózatot?", [
                "logisztikailag optimálisan / hálózatilag összehangoltan működő",
                "szép színes síneken futó",
                "reggelente vidáman zakatoló"
            ], 0, ["c1-adv-infrastructural-efficiency-logistics"]),
            mc("grammar", "recognize", "Milyen szerkezettel fejezhetjük ki a több közlekedési mód közötti integrációt?", [
                "a kötöttpályás vonalakat a buszhálózattal harmonikusan összekapcsoló terminál",
                "amikor az utasok leszállnak és kinyújtóztatják a lábukat",
                "hogyha meleg teát árulnak az állomáson"
            ], 0, ["c1-participle-multimodal-connectivity"]),
            match("vocabulary", "recognize", [["intermodális csomópont", "különböző közlekedési ágak átszállóhelye"], ["modális váltás", "forgalom átterelése közútról vasútra"], ["ETCS rendszer", "európai digitális vasúti vonatbefolyásoló rendszer"], ["zónatarifa-rendszer", "Baross Gábor távolsági díjszabási forradalma"], ["átbocsátóképesség", "a pálya által lebonyolítható maximális forgalom"]], ["c1-28-vocab"]),
            fb("vocabulary", "recall", "A közúti forgalom vasútra való tudatos átterelését _____ váltásnak nevezzük. (modal / modális)", "modális", "The conscious shifting of road traffic to rail is called modal shift.", ["c1-28-vocab"]),
            fb("vocabulary", "recall", "Baross Gábor legendás történelmi elnevezése a _____ . (Iron Minister / vasminiszter)", "vasminiszter", "The legendary historical designation of Gábor Baross is the Iron Minister.", ["c1-28-vocab"]),
            fb("grammar", "recall", "A vasútfejlesztést logisztikailag _____ módon kell megtervezni. (optimally / optimális)", "optimális", "Railway development must be planned in a logistically optimal manner.", ["c1-adv-infrastructural-efficiency-logistics"]),
            fb("grammar", "context", "A közúti kamionáradattal szemben a _____ a vasút a klímasemlegesség záloga. (in reality / valóságban)", "valóságban", "Contrary to the road truck flood, in reality rail is the pledge of climate neutrality.", ["c1-adv-adversative-modal-shift"]),
            fb("grammar", "context", "Baross reformja nemzetgazdaságilag _____ mértékben gyorsította fel a fejlődést. (to an inestimable / felbecsülhetetlen)", "felbecsülhetetlen", "Baross's reform to an inestimable degree accelerated development.", ["c1-adv-scalar-macroeconomic-integration"]),
            mc("grammar", "context", "Mi a szerepe az ellentétező szerkezeteknek a közlekedéspolitikai vitákban?", [
                "Rámutatnak az autópálya-építés rejtett környezeti és társadalmi káraira a vasút ökológiai fölényével szemben.",
                "Megmagyarázzák, hogy miért kell jegyet váltani a vonatra.",
                "Elnézést kérnek az elhúzódó építkezések miatti porért."
            ], 0, ["c1-adv-adversative-modal-shift"]),
            sb("grammar", "produce", ["A", "kötöttpályás", "közlekedés", "a", "fenntartható", "zöld", "jövő", "alapja."], ["A", "kötöttpályás", "közlekedés", "a", "fenntartható", "zöld", "jövő", "alapja."], "Fixed-track transport is the foundation of a sustainable green future.", ["c1-adv-adversative-modal-shift"]),
            sw("production", [{"prompt": "Formulate a statement on multimodal logistics using an infrastructural adverbial.", "answer": "A modern közlekedéstervezésnek logisztikailag optimálisan, a kötöttpályás törzshálózatot a buszos és mikromobilitási rendszerekkel hálózatilag összehangoltan kell megvalósítania."}], ["c1-adv-infrastructural-efficiency-logistics"]),
            sw("production", [{"prompt": "Write a critical reflection on Baross Gábor's zone-tariff legacy and modern transit policy.", "answer": "Baross Gábor zónatarifa-reformja nemzetgazdaságilag felbecsülhetetlen mértékben bizonyította be, hogy a kötöttpályás közlekedés az esélyteremtés és az országos társadalmi integráció legfőbb állami eszköze."}], ["c1-adv-scalar-macroeconomic-integration"])
        ]
    )

    # ----------------------------------------------------
    # TRACK 2: DISCOURSE (c1-kozlekedespolitika)
    # ----------------------------------------------------
    slug = "kozlekedespolitika"
    disc_intro = [
        "In the 2020s, Hungarian transportation policy became a battleground between physical infrastructure decay and nontransparent political megaprojects. While the national railway company (MÁV) suffered from catastrophic delays, burning diesel engines, and branch line closures, the state privatized motorways via a 35-year oligarchic concession and channeled billions of euros into the high-speed Budapest–Belgrade railway line funded by Chinese loans.",
        "In this discourse unit, through five serialized investigative accounts, you will analyze the mechanics of railway deterioration, the debate over branch line closures, motorway concessions, political clashes between Vitézy and Lázár, and the struggle for sustainable public mobility at the C1 level."
    ]

    disc_lessons = [
        {
            "num": 1,
            "stem": f"c1-{slug}-01",
            "title": "MÁV Deterioration, Delays & Railway Crisis Framing",
            "grammar_title": "Discourse Framing Markers Diagnosing Rolling Stock Obsolescence and Railway Collapse",
            "grammar_skill": "c1-discourse-railway-crisis-framing",
            "goals": [
                "I can analyze MÁV's systemic rolling stock obsolescence, chronic delay statistics, and speed restrictions (*járműpark elöregedése, krónikus késések, lassújelek szaporodása, MÁV-válság*).",
                "I can deploy discourse framing markers diagnosing infrastructure decay (*a vasúti infrastruktúra drámai lepusztulása, a menetrendszerűség szisztematikus összeomlása, a forráskivonás katasztrofális következményeként*).",
                "I can critique operational breakdowns in public transit networks."
            ],
            "vocab": [
                {"lemma": "járműpark elöregedése", "translation": "rolling stock aging / obsolescence", "pos": "expression"},
                {"lemma": "lassújel", "translation": "temporary speed restriction (track defect)", "pos": "noun"},
                {"lemma": "menetrendszerűség összeomlása", "translation": "collapse of punctuality / timetable reliability", "pos": "expression"},
                {"lemma": "pályaromlás", "translation": "track deterioration", "pos": "noun"},
                {"lemma": "forráskivonás", "translation": "capital withdrawal / funding cuts", "pos": "noun"},
                {"lemma": "mozdonyhiány", "translation": "locomotive shortage", "pos": "noun"},
                {"lemma": "műszaki meghibásodás", "translation": "technical failure / breakdown", "pos": "expression"},
                {"lemma": "klímaberendezés hiánya", "translation": "lack of air conditioning", "pos": "expression"}
            ],
            "gr_text1": "Discourse framing markers diagnose systemic transit breakdown and technical decay: `a vasúti infrastruktúra drámai és évtizedes lepusztulása` (the dramatic and decades-long decay of rail infrastructure), `a menetrendszerűség szisztematikus összeomlásaként értékelhető módon` (in a manner evaluable as the systematic collapse of timetable reliability), `a krónikus forráskivonás és a karbantartás elmaradásának következtében` (as a consequence of chronic capital withdrawal and delayed maintenance).",
            "gr_text2": "Example: `A közlekedési elemzők a menetrendszerűség szisztematikus összeomlásaként írták le a nyári hőségben sorra kigyulladó mozdonyok és a pályaromlások okozta késéshullámot`.",
            "gr_table": [
                ["A vasúti infrastruktúra drámai lepusztulása napi szintű fennakadásokat okoz.", "The dramatic decay of railway infrastructure causes daily disruptions."],
                ["A menetrendszerűség szisztematikus összeomlása elriasztja az utasokat a vonattól.", "The systematic collapse of punctuality scares passengers away from the train."],
                ["A lassújelek szaporodása a pályakarbantartás krónikus elmaradásának bizonyítéka.", "The multiplication of speed restrictions proves chronic failure of track maintenance."]
            ],
            "world_story_seg": {
                "seg_slug": "mav-valsag-lassujelek",
                "title": "A MÁV-összeomlás és a kigyulladó mozdonyok nyara",
                "summary": "2023 és 2024 forró nyarain a magyar vasút a működésképtelenség határára sodródott: az elöregedett mozdonyok kigyulladtak, a vágányok deformálódtak, s a vonatok tízezer órákat késtek.",
                "paragraphs": [
                    {"type": "narration", "text": "Amikor a nyári kánikulában a hőmérő higanyszála negyven fok fölé kúszott, a magyar államvasutak országszerte megbénult. A negyven-ötven éves Bzmot motorkocsikban és a klíma nélküli kocsikban elviselhetetlenné vált a hőség, miközben a Nyugati pályaudvar előtt sorra gyulladtak ki a vontatómozdonyok."},
                    {"type": "dialogue", "speaker": "Takács Dániel közlekedési szakújságíró", "text": "Ez nem egyszerű balszerencse, hanem a vasúti infrastruktúra drámai lepusztulásának és a menetrendszerűség szisztematikus összeomlásának egyenes következménye. Évtizedeken át minden fejlesztési forrást elvontak a karbantartástól."},
                    {"type": "narration", "text": "A vasúti pályákon elszaporodtak a lassújelek: a Budapest-Győr-Bécs fővonalon, az ország legfontosabb nemzetközi folyosóján a sínek romlása miatt húsz kilométer per órás sebességkorlátozást kellett bevezetni a balesetveszély elkerülésére."},
                    {"type": "narration", "text": "Az utasok százezrei szembesültek azzal, hogy az állam alapvető közszolgáltatási kötelezettsége a fizikai megsemmisülés szélére jutott."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Mit jelent a 'lassújel' a vasúti közlekedésben?", [
                    "A pálya műszaki romlása, sínhibák vagy elhasználódás miatt elrendelt kényszerű sebességkorlátozást egy adott szakaszon.",
                    "Egy udvarias figyelmeztető táblát a madarak számára.",
                    "A kalauzok lassú jegykezelési tempóját jelző lámpát."
                ], 0, ["c1-kozlekedespolitika-vocab"]),
                fb("grammar", "controlled", "A szakértők a vasúti infrastruktúra _____ lepusztulásaként értékelték az állapotokat. (dramatic / drámai)", "drámai", "Experts evaluated the conditions as the dramatic decay of railway infrastructure.", ["c1-discourse-railway-crisis-framing"]),
                match("vocabulary", "controlled", [["lassújel", "pályahiba miatti kényszerű sebességcsökkentés"], ["járműpark elöregedése", "évtizedes mozdonyok és vagonok kopása"], ["menetrendszerűség összeomlása", "a vonatok kiszámíthatatlan, tömeges késése"], ["pályaromlás", "sínek és alépítmények fizikai tönkremenetele"]], ["c1-kozlekedespolitika-vocab"]),
                fb("grammar", "practice", "A menetrendszerűség szisztematikus _____ miatt az ingázók feladták a vasúti utazást. (collapse / összeomlása)", "összeomlása", "Due to the systematic collapse of timetable reliability commuters gave up train travel.", ["c1-discourse-railway-crisis-framing"]),
                sb("grammar", "practice", ["A", "vasúti", "pályák", "karbantartásának", "elmaradása", "veszélyes", "lassújeleket", "szült."], ["A", "vasúti", "pályák", "karbantartásának", "elmaradása", "veszélyes", "lassújeleket", "szült."], "The neglect of railway track maintenance gave birth to dangerous speed restrictions.", ["c1-discourse-railway-crisis-framing"]),
                dc("dialogue", [
                    {"speaker": "Ingázó utas", "text": "Miért késik minden nap legalább negyven percet a reggeli vonat?"},
                    {"speaker": "Vasúti dolgozó", "text": "A menetrendszerűség szisztematikus _____ küzdünk a mozdonyok meghibásodása és a rossz pálya miatt."},
                    {"speaker": "Ingázó utas", "text": "Így lassan lehetetlen időben beérni a munkahelyre."}
                ], ["összeomlásával", "javulásával", "ünneplésével"], 0, ["c1-discourse-railway-crisis-framing"]),
                sw("production", [{"prompt": "Write a sentence diagnosing railway infrastructure decay using a crisis framing marker.", "answer": "A vasúti infrastruktúra drámai lepusztulása és a forráskivonások nyomán a magyar vasúthálózat a menetrendszerűség szisztematikus összeomlásával szembesül nap mint nap."}], ["c1-discourse-railway-crisis-framing"]),
                mc("grammar", "check", "Melyik kifejezés írja le a vasúti műszaki krízist a legpontosabb publicisztikai regiszterben?", [
                    "a vasúti infrastruktúra drámai lepusztulása / a menetrendszerűség szisztematikus összeomlása",
                    "kicsit meleg van a kocsikban",
                    "túl sok állomás van a vonalon"
                ], 0, ["c1-discourse-railway-crisis-framing"])
            ]
        },
        {
            "num": 2,
            "stem": f"c1-{slug}-02",
            "title": "Branch Line Closures & Citizen Mobility Rights",
            "grammar_title": "Deontic Modal Structures Asserting Statutory Citizen Rights to Public Transport Access",
            "grammar_skill": "c1-modal-deontic-public-mobility-rights",
            "goals": [
                "I can analyze the closure of rural railway branch lines, bus substitutions, and territorial isolation (*mellékvonal-bezárások, vonathelyettesítő busz, eljutási alapjog, vidék elszigetelődése*).",
                "I can formulate deontic modal structures asserting mobility rights (*az államnak kötelessége garantálni az eljutási jogot, nem zárhatja el a kistelepüléseket, biztosítania kell a közszolgáltatást*).",
                "I can debate the socioeconomic consequences of cutting rural public transit."
            ],
            "vocab": [
                {"lemma": "mellékvonal-bezárás", "translation": "branch line closure / suspension", "pos": "expression"},
                {"lemma": "vonathelyettesítő busz", "translation": "rail-replacement bus", "pos": "expression"},
                {"lemma": "eljutási alapjog", "translation": "fundamental right to public mobility", "pos": "expression"},
                {"lemma": "vidéki elszigetelődés", "translation": "rural isolation / disconnection", "pos": "expression"},
                {"lemma": "közszolgáltatási kötelezettség", "translation": "public service obligation (PSO)", "pos": "expression"},
                {"lemma": "területi kohézió", "translation": "territorial cohesion", "pos": "expression"},
                {"lemma": "forgalomszüneteltetés", "translation": "service suspension (euphemism for closure)", "pos": "noun"},
                {"lemma": "mobilitási szegénység", "translation": "transport / mobility poverty", "pos": "expression"}
            ],
            "gr_text1": "Deontic modal structures articulate statutory state duties guaranteeing universal mobility access for citizens: `az államnak kötelessége garantálni az állampolgárok eljutási alapjogát` (the state has a duty to guarantee citizens' fundamental right to mobility), `nem vághatja el a vidéki kistelepüléseket a közösségi közlekedéstől` (cannot cut rural small settlements off from public transit), `biztosítania kell az egyenlő hozzáférést a közszolgáltatásokhoz` (must ensure equal access to public services), `nem hivatkozhat pusztán gazdasági megtérülésre` (cannot refer solely to economic return).",
            "gr_text2": "Example: `A kormánynak alkotmányos kötelessége szavatolni a vidéki régiók eljutási jogát, és nem szüntetheti meg önkényesen a helyi vasúti közszolgáltatást`.",
            "gr_table": [
                ["Az államnak kötelessége garantálni az eljutási alapjogot minden településen.", "The state has a duty to guarantee the fundamental right to mobility in every settlement."],
                ["A minisztérium nem vághatja el a vidéki falvakat a vasúti közlekedéstől.", "The ministry cannot cut rural villages off from rail transport."],
                ["A közlekedési vezetésnek szavatolnia kell a területi kohézió feltételeit.", "Transport leadership must guarantee conditions of territorial cohesion."]
            ],
            "world_story_seg": {
                "seg_slug": "mellekvonalak-felszamolasa",
                "title": "A szárnyvonalak bezárása és a vonathelyettesítő buszok korszaka",
                "summary": "2023 augusztusában a minisztérium tíz vasúti mellékvonalon rendelt el 'módszerváltást', buszokkal váltva ki a vonatokat. A falvak lakói a mobilitási szegénység csapdájába estek.",
                "paragraphs": [
                    {"type": "narration", "text": "Egyetlen kormányzati bejelentéssel tíz vidéki vasúti mellékvonalon némult el a sínek csattogása az Északi-középhegységtől az Alföldig. A hivatalos kommunikáció 'járműhiány miatti forgalomszüneteltetésről' beszélt, de a helyiek pontosan tudták: a fűvel benőtt sínek a vonal végleges halálát jelentik."},
                    {"type": "dialogue", "speaker": "Takács Dániel", "text": "Az államnak kötelessége volna garantálni a polgárok eljutási alapjogát. A szárnyvonalak bezárása és a zötykölődő, légkondi nélküli pótlóbuszok beállítása a vidéki Magyarország cserbenhagyása. Egy falu, amely elveszíti a vasútját, elveszíti a jövőjét is."},
                    {"type": "narration", "text": "A kisgyermekes családok, az idős nyugdíjasok és a városi iskolákba ingázó diákok számára a vasút megszüntetése a mobilitási szegénység közvetlen növekedését hozta."},
                    {"type": "narration", "text": "A civil szervezetek tiltakozása rámutatott: a közszolgáltatás nem profitorientált üzlet, hanem a társadalmi integráció állami záloga."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Miért bírálták szakértők a vasúti mellékvonalak 'forgalomszüneteltetését'?", [
                    "Mert a buszos pótlás lassabb, kényelmetlenebb, nem alkalmas kerékpárok szállítására, és a vidéki kistelepülések elszigetelődését okozza.",
                    "Mert a pótlóbuszokon kötelező volt énekelni.",
                    "Mert a buszok csak hátramenetben közlekedhettek."
                ], 0, ["c1-kozlekedespolitika-vocab"]),
                fb("grammar", "controlled", "Az államnak kötelessége _____ garantálni a kistelepülések eljutási alapjogát. (would be / volna)", "volna", "It would be the state's duty to guarantee the fundamental right of small settlements to mobility.", ["c1-modal-deontic-public-mobility-rights"]),
                match("vocabulary", "controlled", [["mellékvonal-bezárás", "helyi érdekű vasútvonalak megszüntetése"], ["vonathelyettesítő busz", "vonatok helyett indított pótlójárat"], ["eljutási alapjog", "a közösségi közlekedéshez való alkotmányos jog"], ["mobilitási szegénység", "a közlekedési lehetőségektől való elzártság állapota"]], ["c1-kozlekedespolitika-vocab"]),
                fb("grammar", "practice", "A közlekedési minisztérium nem _____ el a vidéki lakosságot a tisztes eljutástól. (must not cut off / vághatja)", "vághatja", "The transport ministry must not cut rural population off from decent mobility.", ["c1-modal-deontic-public-mobility-rights"]),
                sb("grammar", "practice", ["Az", "államnak", "garantálnia", "kell", "az", "eljutási", "alapjogot", "mindenkinek."], ["Az", "államnak", "garantálnia", "kell", "az", "eljutási", "alapjogot", "mindenkinek."], "The state must guarantee the fundamental right to mobility for everyone.", ["c1-modal-deontic-public-mobility-rights"]),
                dc("dialogue", [
                    {"speaker": "Polgármester", "text": "Hogyan jutnak be a gyerekeink a gimnáziumba, ha bezárják a helyi vasutat?"},
                    {"speaker": "Közlekedési szakértő", "text": "Az állam nem _____ meg a falvakat a kötöttpályás kapcsolattól, ez sérti az eljutási alapjogot."},
                    {"speaker": "Polgármester", "text": "Petíciót indítunk a vonal megmaradásáért."}
                ], ["foszthatja", "védheti", "kérheti"], 0, ["c1-modal-deontic-public-mobility-rights"]),
                sw("production", [{"prompt": "Write a sentence formulating citizens' public mobility rights using a deontic modal structure.", "answer": "Az államnak kötelessége szavatolni a kistérségi polgárok eljutási alapjogát, és nem szüntetheti meg a helyi vasútvonalakat a területi kohézió és az egyenlő esélyek védelmében."}], ["c1-modal-deontic-public-mobility-rights"]),
                mc("grammar", "check", "Melyik modális kifejezés írja elő az állami mobilitási garanciát a legszigorúbban?", [
                    "kötelessége garantálni az eljutási alapjogot / nem vághatja el a falvakat",
                    "talán egyszer elküldhetne egy autót",
                    "jó lenne ha nem sétálnának annyit"
                ], 0, ["c1-modal-deontic-public-mobility-rights"])
            ]
        },
        {
            "num": 3,
            "stem": f"c1-{slug}-03",
            "title": "Highway Concessions vs. Rail Drain Proportional Correlatives",
            "grammar_title": "Proportional Correlative Conjunctions Mapping Highway Concession Costs Against Railway Underfunding",
            "grammar_skill": "c1-adv-proportional-concession-deficits",
            "goals": [
                "I can analyze the 35-year highway concession contract, private equity monopoly, and infrastructure funding reallocation (*autópálya-koncesszió, magántőke-konzorcium, rendelkezésre állási díj, forrásátszivattyúzás*).",
                "I can deploy proportional correlative conjunctions mapping financial distortion (*minél több százmilliárdot fizet ki az állam a koncessziós magántőkének, annál kevesebb forrás jut a vasút felújítására*).",
                "I can critique long-term public-private partnership (PPP) concession contracts in transport economics."
            ],
            "vocab": [
                {"lemma": "autópálya-koncesszió", "translation": "highway concession (35-year contract)", "pos": "expression"},
                {"lemma": "rendelkezésre állási díj", "translation": "availability fee (state payment to concessionaire)", "pos": "expression"},
                {"lemma": "magántőke-alap", "translation": "private equity fund (nontransparent ownership)", "pos": "expression"},
                {"lemma": "forrásátszivattyúzás", "translation": "reallocation / siphoning of public funds", "pos": "noun"},
                {"lemma": "állami garanciavállalás", "translation": "state guarantee / sovereign backing", "pos": "expression"},
                {"lemma": "profitgarancia", "translation": "guaranteed return / profit margin", "pos": "expression"},
                {"lemma": "költségvetési aszimmetria", "translation": "budgetary asymmetry", "pos": "expression"},
                {"lemma": "hosszú távú kötöttség", "translation": "long-term commitment / encumbrance", "pos": "expression"}
            ],
            "gr_text1": "Proportional correlative structures map the direct fiscal trade-off between highway concession payouts and public rail starvation: `Minél több százmilliárdos rendelkezésre állási díjat utal ki az állam a koncessziós társaságnak, annál kevesebb pénz marad a vasúti pályafelújításokra` (The more hundreds of billions of availability fees the state transfers to the concession company, the less money remains for railway track renewals), `Amilyen mértékben növekszik a magántőke garantált haszna, olyan arányban szegényedik el a közösségi közlekedés` (In proportion as private capital's guaranteed profit increases, to that extent public transit is impoverished).",
            "gr_text2": "Example: `Minél inkább a koncessziós autópályák fenntartását részesíti előnyben a kormányzat, annál mélyebbre süllyed a MÁV a forráshiányos krízisben`.",
            "gr_table": [
                ["Minél több pénzt visz el az autópálya-koncesszió, annál kevesebb jut a vasútra.", "The more money the motorway concession takes, the less goes to the railway."],
                ["Amilyen mértékben nő a magánkonzorcium bevétele, olyan arányban növekszik az államháztartási teher.", "To the extent the private consortium's revenue increases, to that extent fiscal burden grows."],
                ["Minél hosszabb távra kötik meg a koncessziót, annál inkább megkötik a jövő kormányainak kezét.", "The longer term the concession is signed for, the more future governments' hands are tied."]
            ],
            "world_story_seg": {
                "seg_slug": "autopalya-koncesszio-35ev",
                "title": "A 35 éves autópálya-koncesszió és a költségvetési elszívás",
                "summary": "2022-ben a kormány harmincöt évre koncesszióba adta a teljes magyar gyorsforgalmi úthálózatot egy kormánypárti magántőkealapnak, évi százmilliárdos fix kifizetéseket garantálva.",
                "paragraphs": [
                    {"type": "narration", "text": "Míg a vasúti kocsikban nem működött a fűtés és a hűtés, 2022 nyarán az állam példátlan üzletet kötött: 35 évre privatizálta csaknem kétezer kilométernyi autópálya üzemeltetését és fejlesztését egy oligarchikus magántőke-konzorcium javára."},
                    {"type": "dialogue", "speaker": "Takács Dániel", "text": "Minél több százmilliárdot szív el ez a koncessziós szerződés rendelkezésre állási díjak formájában, annál kevesebb forrás marad a MÁV leromlott pályáinak felújítására. Ez a döntés évtizedekre bebetonozta a közúti lobbi hegemóniáját a zöld vasúttal szemben."},
                    {"type": "narration", "text": "Az Európai Bizottság vizsgálatot indított a koncessziós pályázat versenytisztaságának hiánya miatt, ám a szerződés érvényben maradt: a magyar adófizetők pénze a közösségi közlekedés helyett a magánprofitot garantálta."},
                    {"type": "narration", "text": "A költségvetési aszimmetria nyilvánvalóvá tette: a politikai elit számára az aszfaltépítés és a kapcsolódó tőkés érdekek előrébb valók voltak az állampolgárok mindennapi vasúti biztonságánál."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Milyen kötelezettséget vállalt a magyar állam a 35 éves autópálya-koncessziós szerződésben?", [
                    "Évente több százmilliárd forint 'rendelkezésre állási díjat' fizet a magánkonzorciumnak az autópályák fenntartásáért és bővítéséért, garantálva a magántőke profitját.",
                    "Azt, hogy minden autópályán kötelező kerékpárutat építeni.",
                    "Azt, hogy ingyenes benzint oszt a hétvégi kirándulóknak."
                ], 0, ["c1-kozlekedespolitika-vocab"]),
                fb("grammar", "controlled", "Minél több pénzt visz el az autópálya-koncesszió, _____ kevesebb jut a vasúti járműpark megújítására. (the more / annál)", "annál", "The more money the highway concession takes, the less goes to rolling stock renewal.", ["c1-adv-proportional-concession-deficits"]),
                match("vocabulary", "controlled", [["autópálya-koncesszió", "gyorsforgalmi utak 35 éves magánüzemeltetése"], ["rendelkezésre állási díj", "az állam által a koncesszornak fizetett fix díj"], ["magántőke-alap", "a tulajdonosok kilétét elrejtő pénzügyi alap"], ["forrásátszivattyúzás", "közpénzek magánzsebekbe való átcsatornázása"]], ["c1-kozlekedespolitika-vocab"]),
                fb("grammar", "practice", "Amilyen mértékben növekszik a koncessziós kifizetés, olyan _____ csökken a vasútbiztonsági költségvetés. (proportion / arányban)", "arányban", "In proportion as concession payout increases, to that extent railway safety budget decreases.", ["c1-adv-proportional-concession-deficits"]),
                sb("grammar", "practice", ["Minél", "drágább", "a", "koncesszió,", "annál", "kevesebb", "forrás", "jut", "a", "vasútra."], ["Minél", "drágább", "a", "koncesszió,", "annál", "kevesebb", "forrás", "jut", "a", "vasútra."], "The more expensive the concession, the fewer funds go to the railway.", ["c1-adv-proportional-concession-deficits"]),
                dc("dialogue", [
                    {"speaker": "Közgazdász", "text": "Miért nincs pénz a MÁV leromlott mozdonyainak cseréjére?"},
                    {"speaker": "Elemző", "text": "Mert minél több forrást köt le a 35 éves autópálya-szerződés, _____ kevesebb mozgástere marad a költségvetésnek a vasútra."},
                    {"speaker": "Közgazdász", "text": "Ez a közpénzek aránytalan és káros elosztása."}
                ], ["annál", "mindig", "soha"], 0, ["c1-adv-proportional-concession-deficits"]),
                sw("production", [{"prompt": "Write a sentence analyzing infrastructure funding distortion using 'Minél... annál...'.", "answer": "Minél több százmilliárd forintot fizet ki az állam a 35 éves autópálya-koncesszió rendelkezésre állási díjaira, annál kevesebb forrás marad a MÁV elöregedett járműparkjának megújítására."}], ["c1-adv-proportional-concession-deficits"]),
                mc("grammar", "check", "Melyik szerkezet írja le az aszfaltkoncesszió és a vasúti forráskivonás arányosságát a legpontosabban?", [
                    "Minél több forrást von el a koncesszió... annál kevesebb jut a vasútra / Amilyen mértékben... olyan arányban",
                    "Ha sok az autó, gyorsan megyünk",
                    "Szépek az új pihenőhelyek az út mentén"
                ], 0, ["c1-adv-proportional-concession-deficits"])
            ]
        },
        {
            "num": 4,
            "stem": f"c1-{slug}-04",
            "title": "Budapest-Belgrade Megaproject vs. Suburban Transit",
            "grammar_title": "Epistemic Stance Markers Critiquing Nontransparent Infrastructure Megaprojects and Debt Traps",
            "grammar_skill": "c1-epistemic-geopolitical-megaproject-critique",
            "goals": [
                "I can analyze the Budapest–Belgrade railway reconstruction (Chinese loan, classification of contracts, transit corridor vs. suburban neglect).",
                "I can deploy elevated epistemic stance markers critiquing megaproject viability (*gazdaságilag megtérülhetetlen beruházásként, vélelmezhetően geopolitikai függőséget okozó, orvosolhatatlan adósságteherként*).",
                "I can evaluate the public clash between Vitézy Dávid (urban suburban rail) and Lázár János (centralized cuts)."
            ],
            "vocab": [
                {"lemma": "Budapest–Belgrád vasútvonal", "translation": "Budapest–Belgrade railway line", "pos": "expression"},
                {"lemma": "kínai hitel", "translation": "Chinese sovereign loan", "pos": "expression"},
                {"lemma": "szerződések titkosítása", "translation": "classification of contracts (for 10 years)", "pos": "expression"},
                {"lemma": "adásságcsapda-diplomácia", "translation": "debt-trap diplomacy", "pos": "expression"},
                {"lemma": "geopolitikai kitettség", "translation": "geopolitical exposure / dependency", "pos": "expression"},
                {"lemma": "megtérülési idő", "translation": "payback period (return on investment)", "pos": "expression"},
                {"lemma": "elővárosi fejlesztések leállítása", "translation": "cancellation of suburban transit projects", "pos": "expression"},
                {"lemma": "szakmai vita", "translation": "professional public dispute (Vitézy vs. Lázár)", "pos": "expression"}
            ],
            "gr_text1": "Epistemic stance markers formulate rigorous economic and geopolitical critiques of non-transparent prestige investments: `gazdaságilag nyilvánvalóan megtérülhetetlen beruházás` (an investment manifestly economically unviable), `vélelmezhetően a kínai geopolitikai érdekeket szolgáló projekt` (a project presumptively serving Chinese geopolitical interests), `minden szakmai és pénzügyi racionalitást nélkülöző döntés` (decision lacking all professional and financial rationality), `joggal tekinthető aránytalan adósságcsapdának` (can rightfully be regarded as a disproportionate debt trap).",
            "gr_text2": "Example: `A közgazdászok a Budapest–Belgrád vasutat gazdaságilag nyilvánvalóan megtérülhetetlen, a magyar utasok számára csekély hasznot hajtó projektként írták le`.",
            "gr_table": [
                ["A Budapest–Belgrád projekt gazdaságilag nyilvánvalóan megtérülhetetlen beruházás.", "The Budapest–Belgrade project is a manifestly economically unviable investment."],
                ["A szerződések titkosítása vélelmezhetően a korrupciós kockázatokat leplezi.", "The classification of contracts presumptively covers up corruption risks."],
                ["A kínai hitelből épülő vonal joggal tekinthető geopolitikai adósságcsapdának.", "The line built from Chinese loans can rightfully be regarded as a geopolitical debt trap."]
            ],
            "world_story_seg": {
                "seg_slug": "budapest-belgrad-visszassagok",
                "title": "A Budapest–Belgrád gigaberuházás és az elhalt elővárosi álmok",
                "summary": "Több mint ezer milliárd forintos kínai hitelből indult a Budapest–Belgrád vasút építése, miközben Lázár János minisztériuma sorra törölte az agglomerációs hév- és vasútfejlesztéseket.",
                "paragraphs": [
                    {"type": "narration", "text": "A magyar vasút legnagyobb beruházása a 150-es számú, Budapest–Belgrád vasútvonal lett: több mint ezer milliárd forintos kínai hitelből épülő kétvágányú pálya, amelynek szerződéseit a kormány tíz évre titkosította. A beruházás számítások szerint legfeljebb több száz év alatt térülhet meg, miközben elkerüli a nagyobb magyar városokat."},
                    {"type": "dialogue", "speaker": "Takács Dániel", "text": "A Budapest–Belgrád projekt gazdaságilag nyilvánvalóan megtérülhetetlen, s joggal tekinthető geopolitikai kitettségnek. Miközben erre a kínai teherforgalmi vonalra ezer milliárdot költünk, Lázár János egyetlen tollvonással kaszálta el az elővárosi HÉV-járműcserét és a budapesti vasúti fejlesztéseket."},
                    {"type": "narration", "text": "A Vitézy Dávid által kidolgozott Budapesti Agglomerációs Vasúti Stratégia kukába dobása azt jelentette: a napi egymillió ingázó korszerűsítése helyett a kínai áruk tranzitja kapott abszolút prioritást."},
                    {"type": "narration", "text": "A szakmai közvélemény döbbenten figyelte, miként áldozza fel az állam a hazai utazóközönség érdekeit az átláthatatlan geopolitikai gigaprojektek kedvéért."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Miért bírálták élesen a Budapest–Belgrád vasútvonal újjáépítését a független közlekedési szakértők?", [
                    "Mert gigantikus, titkosított kínai hitelből valósul meg, elkerüli a nagyobb hazai városokat, a megtérülése évszázadokig tarthat, s főként a kínai teherárut szolgálja ki a magyar utasok helyett.",
                    "Mert túl sok fát ültettek a vasút mellé.",
                    "Mert csak gőzmozdonyok közlekedhetnek rajta."
                ], 0, ["c1-kozlekedespolitika-vocab"]),
                fb("grammar", "controlled", "A szakértők szerint a kínai hitelből finanszírozott gigaprojekt gazdaságilag _____ megtérülhetetlen. (manifestly / nyilvánvalóan)", "nyilvánvalóan", "According to experts the megaproject financed from Chinese loans is manifestly economically unviable.", ["c1-epistemic-geopolitical-megaproject-critique"]),
                match("vocabulary", "controlled", [["Budapest–Belgrád vasútvonal", "több mint ezer milliárdos kínai vasútberuházás"], ["kínai hitel", "államadósságot növelő külföldi kölcsön"], ["szerződések titkosítása", "közérdekű adatok elzárása a nyilvánosság elől"], ["adásságcsapda-diplomácia", "gazdasági függést kialakító nagyhatalmi hitelezés"]], ["c1-kozlekedespolitika-vocab"]),
                fb("grammar", "practice", "A beruházás vélelmezhetően a kínai geopolitikai _____ szolgálja a magyar utasok helyett. (interests / érdekeit)", "érdekeit", "The investment presumptively serves Chinese geopolitical interests instead of Hungarian passengers.", ["c1-epistemic-geopolitical-megaproject-critique"]),
                sb("grammar", "practice", ["A", "Budapest–Belgrád", "projekt", "nyilvánvalóan", "gazdaságtalan", "a", "magyar", "utasoknak."], ["A", "Budapest–Belgrád", "projekt", "nyilvánvalóan", "gazdaságtalan", "a", "magyar", "utasoknak."], "The Budapest–Belgrade project is manifestly uneconomical for Hungarian passengers.", ["c1-epistemic-geopolitical-megaproject-critique"]),
                dc("dialogue", [
                    {"speaker": "Közlekedésmérnök", "text": "Hoz-e érdemi javulást a magyar ingázóknak a Belgrád-vonal felújítása?"},
                    {"speaker": "Elemző", "text": "Aligha; a projekt gazdaságilag nyilvánvalóan _____ a hazai személyszállítás szempontjából."},
                    {"speaker": "Közlekedésmérnök", "text": "Közben pedig leállították az agglomerációs HÉV-fejlesztéseket."}
                ], ["megtérülhetetlen", "gyors", "olcsó"], 0, ["c1-epistemic-geopolitical-megaproject-critique"]),
                sw("production", [{"prompt": "Write a sentence critiquing infrastructure megaprojects using an epistemic stance marker.", "answer": "A kínai hitelből finanszírozott és titkosított Budapest–Belgrád gigaprojekt gazdaságilag nyilvánvalóan megtérülhetetlen, s joggal tekinthető kockázatos geopolitikai adósságcsapdának."}], ["c1-epistemic-geopolitical-megaproject-critique"]),
                mc("grammar", "check", "Melyik episztemikus kifejezés mond ki gazdasági megalapozatlanságot a legmagasabb bizonyossággal?", [
                    "gazdaságilag nyilvánvalóan megtérülhetetlen / minden pénzügyi racionalitást nélkülöző",
                    "talán nem a legolcsóbb ötlet volt",
                    "majd meglátjuk kétszáz év múlva"
                ], 0, ["c1-epistemic-geopolitical-megaproject-critique"])
            ]
        },
        {
            "num": 5,
            "stem": f"c1-{slug}-05",
            "title": "Pass Populism vs. Green Transit Modernization",
            "grammar_title": "Evaluative Synthesis Particles Formulating Comprehensive Manifestos for Sustainable Public Mobility",
            "grammar_skill": "c1-adv-conclusive-green-transit-synthesis",
            "goals": [
                "I can analyze the 'County and Country Pass' (*ország- és vármegyebérlet*), tariff populism vs. capital starvation, and green transit visions.",
                "I can deploy evaluative synthesis particles formulating sustainable mobility manifestos (*végső soron elengedhetetlen a vasút prioritása, összegzésként leszögezhető, mindent egybevetve a jövő zöld záloga*).",
                "I can synthesize strategic proposals for the revival of Hungarian public transport."
            ],
            "vocab": [
                {"lemma": "vármegyebérlet", "translation": "county transit pass (subsidized flat-rate)", "pos": "noun"},
                {"lemma": "országbérlet", "translation": "national country pass", "pos": "noun"},
                {"lemma": "tarifapopulizmus", "translation": "tariff / fare populism", "pos": "noun"},
                {"lemma": "forráskivéreztetés", "translation": "revenue bleed / starvation of capital", "pos": "expression"},
                {"lemma": "fenntartható mobilitás", "translation": "sustainable mobility", "pos": "expression"},
                {"lemma": "járműbeszerzés", "translation": "rolling stock procurement", "pos": "noun"},
                {"lemma": "közösségi közlekedés reneszánsza", "translation": "renaissance of public transport", "pos": "expression"},
                {"lemma": "zöld közlekedési fordulat", "translation": "green transport transition", "pos": "expression"}
            ],
            "gr_text1": "Evaluative synthesis particles formulate definitive visions for modern, sustainable transportation policy: `végső soron elengedhetetlen a vasútfejlesztés prioritása` (ultimately the priority of railway development is indispensable), `mindent egybevetve a kötöttpálya a modern mobilitás legfőbb záloga` (all in all rail transit is the supreme pledge of modern mobility), `konklúzióként leszögezhető` (can be stated as a conclusion), `összességében tekintve az élhető ország alapfeltétele` (taking it as a whole the prerequisite of a liveable country).",
            "gr_text2": "Example: `Végső soron elengedhetetlen felismerni, hogy az olcsó tarifák önmagukban mit sem érnek minőségi járműpark nélkül, s mindent egybevetve a vasúti reneszánsz jelenti a jövő zálogát`.",
            "gr_table": [
                ["Végső soron elengedhetetlen a vasúti járműpark azonnali és tömeges megújítása.", "Ultimately immediate and mass renewal of rolling stock is indispensable."],
                ["Mindent egybevetve a kötöttpályás közlekedés a fenntartható zöld jövő fundamentuma.", "All in all rail transport is the foundation of a sustainable green future."],
                ["Konklúzióként leszögezhető, hogy a tarifapopulizmus nem helyettesíti a pályafelújítást.", "It can be stated as a conclusion that fare populism does not replace track renewal."]
            ],
            "world_story_seg": {
                "seg_slug": "orszageberlet-valsag-jovo",
                "title": "A vármegyebérlet paradoxona és a vasúti reneszánsz esélye",
                "summary": "A rendkívül olcsó ország- és vármegyebérletek bevezetése népszerű lépés volt, ám a jegybevétel-kiesés tovább mélyítette a MÁV tőkehiányát. A jövő a bátor zöld modernizációban rejlik.",
                "paragraphs": [
                    {"type": "narration", "text": "2023 tavaszán a kormány bevezette az ország- és vármegyebérleteket: néhány ezer forintért bárki korlátlanul utazhatott a MÁV és a Volánbusz járatain. Az intézkedés politikai szempontból átütő sikert hozott a kispénzű ingázók körében, ám a szakma kongatni kezdte a vészharangot."},
                    {"type": "dialogue", "speaker": "Takács Dániel", "text": "A tarifapopulizmus veszélyes csapda: miközben a jegyárakat mesterségesen lenyomták, a kieső bevételeket a költségvetés nem pótolta. Olcsó jeggyel a zsebben állni a késő, klíma nélküli vonaton nem valódi segítség az utasnak."},
                    {"type": "narration", "text": "A valódi megoldást nem az állagmegóvás elhagyása és a szárnyvonalak bezárása jelenti, hanem a bátor járműbeszerzés, az ütemes menetrend kiterjesztése és az európai uniós források célzott kötöttpályás felhasználása."},
                    {"type": "narration", "text": "Végső soron elengedhetetlen a vasút reneszánsza: mindent egybevetve a modern, tiszta és gyors kötöttpályás hálózat Magyarország gazdasági felemelkedésének és zöld jövőjének legfontosabb záloga."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Mi a közlekedéspolitikai paradoxona a magyarországi 'ország- és vármegyebérleteknek'?", [
                    "Az, hogy bár rendkívül olcsóvá tette az utazást, a MÁV jegybevételeinek kiesése miatt tovább csökkent a pályakarbantartásra és új járművekre fordítható forrás.",
                    "Az, hogy a bérleteket csak postagalambbal lehetett megrendelni.",
                    "Az, hogy a bérletek csak éjfél és hajnali kettő között voltak érvényesek."
                ], 0, ["c1-kozlekedespolitika-vocab"]),
                fb("grammar", "controlled", "_____ soron elengedhetetlen a vasúti járműállomány modern, klímabarát megújítása. (Ultimately / Végső)", "Végső", "Ultimately the modern, climate-friendly renewal of rolling stock is indispensable.", ["c1-adv-conclusive-green-transit-synthesis"]),
                match("vocabulary", "controlled", [["vármegyebérlet", "megyei szintű kedvezményes bérlet"], ["tarifapopulizmus", "politikai célú, fedezet nélküli jegyárcsökkentés"], ["fenntartható mobilitás", "a környezetet kímélő, jövőbiztos közlekedés"], ["közösségi közlekedés reneszánsza", "a vasút és buszközlekedés átfogó újjászületése"]], ["c1-kozlekedespolitika-vocab"]),
                fb("grammar", "practice", "Mindent _____, a tiszta és gyors vasút a zöld gazdasági fordulat sarokköve. (taking into account / egybevetve)", "egybevetve", "All in all, clean and fast rail is the cornerstone of green economic transition.", ["c1-adv-conclusive-green-transit-synthesis"]),
                sb("grammar", "practice", ["Végső", "soron", "elengedhetetlen", "a", "vasúti", "fejlesztések", "prioritása", "Magyarországon."], ["Végső", "soron", "elengedhetetlen", "a", "vasúti", "fejlesztések", "prioritása", "Magyarországon."], "Ultimately the priority of railway developments in Hungary is indispensable.", ["c1-adv-conclusive-green-transit-synthesis"]),
                dc("dialogue", [
                    {"speaker": "Közlekedésmérnök", "text": "Elegendő-e az olcsó vármegyebérlet a tömegközlekedés megmentéséhez?"},
                    {"speaker": "Vasúti szakértő", "text": "Konklúzióként leszögezhető: az olcsó jegy nem helyettesíti a biztonságos pályát, mindent egybevetve a vasút korszerűsítése a jövő _____ ."},
                    {"speaker": "Közlekedésmérnök", "text": "Ezért kell új mozdonyokat és kocsikat beszerezni."}
                ], ["záloga", "ára", "féke"], 0, ["c1-adv-conclusive-green-transit-synthesis"]),
                sw("production", [{"prompt": "Write a concluding manifesto on sustainable railway revival using 'Végső soron elengedhetetlen'.", "answer": "Végső soron elengedhetetlen a vasúti közlekedés kiemelt állami prioritássá emelése, az elavult járművek cseréje és a pályák felújítása az élhető, zöld jövő érdekében."}], ["c1-adv-conclusive-green-transit-synthesis"]),
                mc("grammar", "check", "Melyik szintéziskifejezés formulázza meg a fenntartható közlekedés melletti kiállást a legátfogóbban?", [
                    "Végső soron elengedhetetlen a vasút prioritása / mindent egybevetve a zöld jövő záloga",
                    "Hát valahogy majd eljutunk hazáig",
                    "Talán holnap nem fognak késni a vonatok"
                ], 0, ["c1-adv-conclusive-green-transit-synthesis"])
            ]
        }
    ]

    for l in disc_lessons:
        emit_instructional_lesson(28, "discourse", l, disc_title, disc_intro if l["num"] == 1 else None)

    # Combined World Story
    write_json(
        f"stories/world/c1/c1-{slug}-vasuti-valsag.json",
        {
            "id": f"story.c1.{slug}.combined",
            "title": "Sínpáron a jövő: Kötöttpályás válság és a közlekedés jövője",
            "level": "C1",
            "lesson": 5,
            "order": 28,
            "type": "world",
            "estimatedMinutes": 8,
            "grammar": ["c1-adv-conclusive-green-transit-synthesis"],
            "summary": "Tényfeltáró krónika a MÁV műszaki válságáról és a kigyulladó mozdonyokról, a vidéki mellékvonalak bezárásáról, a 35 éves autópálya-koncesszióról, a vitatott Budapest–Belgrád kínai gigaprojektről, valamint az ország- és vármegyebérletek paradoxonáról.",
            "vocabularyTopics": [
                "Railway Decay vs. Highway Megaprojects: The MÁV Crisis, Branch Closures & Concessions",
                "Pass Populism vs. Green Transit Modernization"
            ],
            "paragraphs": [
                {"type": "narration", "text": "A magyar közlekedéspolitika a 2020-as évek derekára mély, szerkezeti válságba jutott. A nemzeti vasúttársaság (MÁV) a járműpark elöregedése, a krónikus karbantartási forráskivonások és az infrastruktúra drámai lepusztulása nyomán a menetrendszerűség szisztematikus összeomlásával nézett farkasszemet. A nyári kánikulában kigyulladó mozdonyok és a balesetveszélyes lassújelek mindennapossá váltak a hazai törzshálózaton."},
                {"type": "narration", "text": "A minisztérium a válságra szárnyvonal-bezárásokkal reagált: tíz vidéki mellékvonalon állították le a személyforgalmat, zötykölődő pótlóbuszokra kényszerítve az ingázókat, és mélyítve a vidéki térségek mobilitási szegénységét. Az államnak kötelessége volna garantálni a polgárok eljutási alapjogát, s a közszolgáltatások felszámolása a területi kohézió elsorvasztását idézte elő."},
                {"type": "narration", "text": "A költségvetési prioritások torzulását leginkább a 35 éves autópálya-koncesszió mutatta meg: minél több százmilliárdos rendelkezésre állási díjat fizetett ki az állam a magántőkealapnak, annál kevesebb forrás maradt a vasútra. Ezzel párhuzamosan az ezer milliárdos kínai hitelből épülő, titkosított Budapest–Belgrád vasútvonal gazdaságilag nyilvánvalóan megtérülhetetlen projektként szolgálta a nagyhatalmi érdekeket az elhalasztott budapesti elővárosi HÉV- és vasútfejlesztések helyett."},
                {"type": "narration", "text": "Bár az olcsó ország- és vármegyebérletek bevezetése népszerű intézkedés volt, a kieső bevételek tovább szárították a MÁV kasszáját. Végső soron elengedhetetlen felismerni: Baross Gábor öröksége ma is érvényes, s mindent egybevetve a modern, klímabarát és biztonságos vasút nem luxus, hanem a magyar gazdaság és társadalom fenntartható jövőjének legfontosabb záloga."}
            ]
        }
    )

    # Discourse Consolidation
    emit_consolidation_lesson(
        28,
        "discourse",
        f"c1-{slug}-consolidation",
        disc_title,
        [
            "I can analyze MÁV rolling stock obsolescence, chronic delay statistics, and speed restrictions.",
            "I can evaluate rural branch line closures, statutory mobility rights, and the 35-year highway concession.",
            "I can critique nontransparent megaprojects (Budapest–Belgrade), tariff populism, and green mobility manifestos."
        ],
        [
            mc("grammar", "recognize", "Milyen szerkezettel diagnosztizálhatjuk a vasúti közlekedés műszaki hanyatlását?", [
                "a vasúti infrastruktúra drámai lepusztulása / a menetrendszerűség szisztematikus összeomlása",
                "hogyha késik a kalauz reggel",
                "amikor lefestik a peron padjait"
            ], 0, ["c1-discourse-railway-crisis-framing"]),
            mc("grammar", "recognize", "Melyik modális kifejezés rögzíti az állampolgárok közlekedési jogát a legszigorúbban?", [
                "kötelessége garantálni az eljutási alapjogot / nem vághatja el a kistelepüléseket",
                "szabadon nézelődhet a vonat ablakából",
                "bármikor sétálhat egyet a mezőn"
            ], 0, ["c1-modal-deontic-public-mobility-rights"]),
            match("vocabulary", "recognize", [["lassújel", "pályahiba miatti kényszerű sebességkorlátozás"], ["mellékvonal-bezárás", "kisvasúti vonalak forgalmának leállítása"], ["autópálya-koncesszió", "gyorsforgalmi utak 35 éves magánkezelése"], ["Budapest–Belgrád vasútvonal", "kínai hitelből épülő titkosított teherfolyosó"], ["vármegyebérlet", "államilag támogatott olcsó tömegközlekedési bérlet"]], ["c1-kozlekedespolitika-vocab"]),
            fb("vocabulary", "recall", "A vasúti pályahiba miatt elrendelt sebességkorlátozást _____ hívjuk. (speed restriction / lassújelnek)", "lassújelnek", "The speed restriction ordered due to track defect is called a speed restriction (lassújel).", ["c1-kozlekedespolitika-vocab"]),
            fb("vocabulary", "recall", "A gyorsforgalmi úthálózat 35 évre történt kiszervezése az autópálya-_____ . (concession / koncesszió)", "koncesszió", "The outsourcing of the expressway network for 35 years is the motorway concession.", ["c1-kozlekedespolitika-vocab"]),
            fb("grammar", "recall", "Az államnak kötelessége _____ szavatolni a kistelepülések vasúti elérhetőségét. (would be / volna)", "volna", "It would be the state's duty to guarantee railway accessibility of small settlements.", ["c1-modal-deontic-public-mobility-rights"]),
            fb("grammar", "context", "Minél több pénzt visz el az autópálya-koncesszió, _____ kevesebb jut a vasúti pályákra. (the more / annál)", "annál", "The more money the highway concession takes, the less goes to railway tracks.", ["c1-adv-proportional-concession-deficits"]),
            fb("grammar", "context", "Végső soron _____ a kötöttpályás zöld közlekedés stratégiai prioritása. (indispensable / elengedhetetlen)", "elengedhetetlen", "Ultimately the strategic priority of fixed-track green transport is indispensable.", ["c1-adv-conclusive-green-transit-synthesis"]),
            mc("grammar", "context", "Mi a funkciója a 'Minél... annál...' arányossági szerkezetnek a közlekedési források elemzésében?", [
                "Az autópályákra fordított magántőke-kifizetések és a vasúti pályaromlás közötti közvetlen összefüggést bizonyítja.",
                "Megmutatja, milyen gyorsan száguld a mozdony.",
                "Elnézést kér az időjárási viszonyok miatt."
            ], 0, ["c1-adv-proportional-concession-deficits"]),
            sb("grammar", "produce", ["A", "kötöttpályás", "közlekedés", "a", "nemzetgazdaság", "nélkülözhetetlen", "motorja."], ["A", "kötöttpályás", "közlekedés", "a", "nemzetgazdaság", "nélkülözhetetlen", "motorja."], "Fixed-track transport is the indispensable motor of national economy.", ["c1-adv-conclusive-green-transit-synthesis"]),
            sw("production", [{"prompt": "Write a critical diagnosis of public transport underfunding using a crisis framing marker.", "answer": "A vasúti infrastruktúra drámai lepusztulása és a járműpark elöregedése a menetrendszerűség szisztematikus összeomlásához vezetett a magyar vasúthálózaton."}], ["c1-discourse-railway-crisis-framing"]),
            sw("production", [{"prompt": "Formulate a concluding thought on sustainable public mobility and railway modernization.", "answer": "Végső soron elengedhetetlen a vasúti közlekedés tömeges modernizációja, a mozdonyok cseréje és az eljutási alapjog biztosítása az ország fenntartható, zöld jövője érdekében."}], ["c1-adv-conclusive-green-transit-synthesis"])
        ]
    )

    print("=== Finished C1 Unit 28 ===")


if __name__ == "__main__":
    generate_unit_28()
