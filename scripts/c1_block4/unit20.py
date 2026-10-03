#!/usr/bin/env python3
"""
Hungarian C1 Block 4 - Unit 20 Generator:
  - Track 1 (Core): Unit 20 — "Ecological Fragility, The Drying Alföld & Environmental Causality" (c1-20)
  - Track 2 (Discourse): Unit 20 — "Water Management, Drought Crises & Wetland Restoration" (c1-vizgazdalkodas)
"""

import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT))

from scripts.c1_block1.common import mc, match, fb, sb, dc, sw, write_json, emit_instructional_lesson, emit_consolidation_lesson
from scripts.c1_block4.registry_helper import register_unit


def generate_unit_20():
    print("=== Generating C1 Unit 20 ===")
    
    # Register skills & titles
    new_skills = {
        "c1-20-vocab": {"kind": "vocabulary"},
        "c1-vizgazdalkodas-vocab": {"kind": "vocabulary"},
        "c1-adv-environmental-causal-chains": {"kind": "grammar"},
        "c1-participle-passive-resultative-state": {"kind": "grammar"},
        "c1-adv-adversative-ecological-concessives": {"kind": "grammar"},
        "c1-complex-hypothetical-counterfactuals": {"kind": "grammar"},
        "c1-adv-scalar-depletion-markers": {"kind": "grammar"},
        "c1-discourse-ecological-threat-framing": {"kind": "grammar"},
        "c1-modal-conservation-deontics": {"kind": "grammar"},
        "c1-adv-proportional-climate-correlatives": {"kind": "grammar"},
        "c1-epistemic-ecological-uncertainty": {"kind": "grammar"},
        "c1-adv-conclusive-environmental-synthesis": {"kind": "grammar"},
    }
    new_titles = {
        "c1-20-vocab": "reading",
        "c1-vizgazdalkodas-vocab": "reading",
        "c1-adv-environmental-causal-chains": "causal postpositional chains articulating multifaceted environmental and ecological crises",
        "c1-participle-passive-resultative-state": "adverbial participial structures expressing degraded environmental and landscape states",
        "c1-adv-adversative-ecological-concessives": "adversative concessive structures contrasting economic gains with ecological costs",
        "c1-complex-hypothetical-counterfactuals": "complex counterfactual conditional structures evaluating historical environmental interventions",
        "c1-adv-scalar-depletion-markers": "scalar depletion adverbials quantifying rates of natural resource exhaustion",
        "c1-discourse-ecological-threat-framing": "discourse framing markers diagnosing acute ecological crises and systemic threats",
        "c1-modal-conservation-deontics": "deontic modal structures formulating statutory environmental obligations and conservation imperatives",
        "c1-adv-proportional-climate-correlatives": "proportional correlative conjunctions mapping interdependent climate and ecological shifts",
        "c1-epistemic-ecological-uncertainty": "epistemic modal adverbials expressing calibrated scientific uncertainty in climate models",
        "c1-adv-conclusive-environmental-synthesis": "conclusive discourse particles synthesizing holistic ecological policy proposals",
    }
    
    core_title = "Ecological Fragility, The Drying Alföld & Environmental Causality"
    core_stems = [f"c1-20-0{i}" for i in range(1, 6)] + ["c1-20-consolidation"]
    disc_title = "Water Management, Drought Crises & Wetland Restoration"
    disc_stems = [f"c1-vizgazdalkodas-0{i}" for i in range(1, 6)] + ["c1-vizgazdalkodas-consolidation"]
    
    register_unit(20, core_title, core_stems, disc_title, disc_stems, new_skills, new_titles)

    # ----------------------------------------------------
    # TRACK 1: CORE (c1-20)
    # ----------------------------------------------------
    core_intro = [
        "The Carpathian Basin is exceptionally vulnerable to climate breakdown: prolonged continental heatwaves, rapid desertification across the Great Hungarian Plain (Alföld), and the legacy of 19th-century hydro-engineering have precipitated a national ecological crisis.",
        "In this unit, anchored by forest engineer Kaán Károly's pioneering 1931 environmental conservation treatise 'Természetvédelem és a magyar táj', you will master the elevated discourse of environmental causality, ecological degradation states, counterfactual historical evaluations, and resource depletion metrics at the C1 level."
    ]

    core_lessons = [
        {
            "num": 1,
            "stem": "c1-20-01",
            "title": "Ecological Vulnerability, Climate Causality & Desertification",
            "grammar_title": "Causal Postpositional Chains Articulating Multifaceted Environmental and Ecological Crises",
            "grammar_skill": "c1-adv-environmental-causal-chains",
            "goals": [
                "I can analyze environmental fragility, desertification, and groundwater decline (*ökológiai sérülékenység, elsivatagosodás, talajvízszint-süllyedés*).",
                "I can deploy complex causal postpositional chains articulating ecological causality (*folytán, következtében, lecsapódásaként, nyomán, eredményeképpen*).",
                "I can articulate multi-stage anthropogenic impacts on regional microclimates in formal academic register."
            ],
            "vocab": [
                {"lemma": "ökológiai sérülékenység", "translation": "ecological vulnerability / fragility", "pos": "expression"},
                {"lemma": "elsivatagosodás", "translation": "desertification", "pos": "noun"},
                {"lemma": "talajvízszint-süllyedés", "translation": "groundwater level drop", "pos": "noun"},
                {"lemma": "aszálykár", "translation": "drought damage", "pos": "noun"},
                {"lemma": "antropogén hatás", "translation": "anthropogenic impact", "pos": "expression"},
                {"lemma": "mikroklíma-romlás", "translation": "microclimate deterioration", "pos": "noun"},
                {"lemma": "ökoszisztéma-összeomlás", "translation": "ecosystem collapse", "pos": "noun"},
                {"lemma": "kiszáradási folyamat", "translation": "desiccation / drying process", "pos": "expression"}
            ],
            "gr_text1": "In ecological analysis, causality is rarely linear; multi-stage causal chains are articulated via formal postpositions and nominalized ablatives: `folytán` (by virtue of / as a consequence of), `következtében` (as a result of), `lecsapódásaként` (as the manifestation/fallout of), `nyomán` (in the wake of), and `eredményeképpen` (as an outcome of). Example: `A drasztikus csapadékhiány folytán a Duna-Tisza közi homokhátság talajvízszintje több méterrel süllyedt, aminek lecsapódásaként az őshonos tölgyesek kiszáradása elkerülhetetlenné vált`.",
            "gr_text2": "These causal postpositions connect multiple causal layers, allowing the speaker to distinguish between trigger events and structural environmental degradation.",
            "gr_table": [
                ["A globális felmelegedés folytán a Kárpát-medencében gyakoribbá váltak az extrém aszályok.", "As a consequence of global warming, extreme droughts have become more frequent in the Carpathian Basin."],
                ["A felelőtlen vízgazdálkodás következtében a homokhátság félsivatagos zónává alakult át.", "As a result of irresponsible water management, the sand ridge turned into a semi-desert zone."],
                ["A mederkotrások nyomán a folyók mélyebbre vágták magukat, elszívva a környező vizeket.", "In the wake of riverbed dredging, rivers cut deeper, draining surrounding waters."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mit nevez a környezettudomány 'antropogén hatásnak'?", [
                    "Az emberi gazdasági és ipari tevékenység által kiváltott környezeti változásokat.",
                    "A meteoritok becsapódása által okozott krátereket.",
                    "A madarak vándorlási útvonalának természetes változását."
                ], 0, ["c1-20-vocab"]),
                fb("grammar", "controlled", "A szélsőséges hőhullámok _____ a kukoricatermés jelentős része megsemmisült. (as a result of / következtében)", "következtében", "As a result of extreme heatwaves significant part of the maize crop was destroyed.", ["c1-adv-environmental-causal-chains"]),
                match("vocabulary", "controlled", [["ökológiai sérülékenység", "egy élőhely érzékenysége a külső zavarokra"], ["talajvízszint-süllyedés", "a föld alatti vízkészlet mélyebbre húzódása"], ["elsivatagosodás", "a talaj terméketlenné válása a szárazság miatt"], ["aszálykár", "a hosszas csapadékhiány okozta gazdasági veszteség"]], ["c1-20-vocab"]),
                fb("grammar", "practice", "A több évtizedes erdőirtás _____ a domboldalak talaja erodálódott. (in the wake of / nyomán)", "nyomán", "In the wake of decades of deforestation the soil of hillsides eroded.", ["c1-adv-environmental-causal-chains"]),
                sb("grammar", "practice", ["A", "csapadékhiány", "folytán", "a", "tavak", "vízszintje", "kritikusra", "csökkent."], ["A", "csapadékhiány", "folytán", "a", "tavak", "vízszintje", "kritikusra", "csökkent."], "Owing to the lack of precipitation the water level of lakes decreased to critical.", ["c1-adv-environmental-causal-chains"]),
                dc("dialogue", [
                    {"speaker": "Hidrológus", "text": "Mi idézte elő az Alföld legsúlyosabb vízhiányát?"},
                    {"speaker": "Klímaszakértő", "text": "A belvízelvezető csatornák túlbuzgó kiépítése _____, a talajvíz nem tudott pótlódni."},
                ], ["folytán", "mögött", "felett"], 0, ["c1-adv-environmental-causal-chains"]),
                sw("production", [{"prompt": "Write a sentence diagnosing environmental desiccation using 'következtében' or 'lecsapódásaként'.", "answer": "A Duna-Tisza közi talajvíz drasztikus megcsappanása következtében az őshonos vizes élőhelyek végleges megsemmisülése fenyeget."}], ["c1-adv-environmental-causal-chains"]),
                mc("grammar", "check", "Melyik névutó fejez ki formális ökológiai ok-okozati összefüggést?", [
                    "folytán / következtében",
                    "ellenére",
                    "helyett"
                ], 0, ["c1-adv-environmental-causal-chains"])
            ]
        },
        {
            "num": 2,
            "stem": "c1-20-02",
            "title": "Degraded Ecosystems, Parched Soils & Participial Degradation States",
            "grammar_title": "Adverbial Participial Structures Expressing Degraded Environmental and Landscape States",
            "grammar_skill": "c1-participle-passive-resultative-state",
            "goals": [
                "I can evaluate landscape degradation, soil salinization, and deforestation (*elszikesedés, termőtalaj-degradáció, tájsebek*).",
                "I can form passive/resultative adverbial participles in `-va/-ve` expressing altered landscape conditions (*kiszáradva, lecsapoltan, felperzselve, kizsigerelve*).",
                "I can characterize the degraded post-industrial and post-agricultural terrain of Central Europe."
            ],
            "vocab": [
                {"lemma": "termőtalaj-degradáció", "translation": "topsoil degradation", "pos": "expression"},
                {"lemma": "elszikesedés", "translation": "soil salinization", "pos": "noun"},
                {"lemma": "tájseb", "translation": "landscape scar / wound", "pos": "noun"},
                {"lemma": "mocsárlecsapolás", "translation": "swamp drainage", "pos": "noun"},
                {"lemma": "kizsigerelt táj", "translation": "depleted / exploited landscape", "pos": "expression"},
                {"lemma": "belvízelvezetés", "translation": "inland water drainage", "pos": "noun"},
                {"lemma": "élőhelyvesztés", "translation": "habitat loss", "pos": "noun"},
                {"lemma": "monokultúrás művelés", "translation": "monoculture cultivation", "pos": "expression"}
            ],
            "gr_text1": "Adverbial participles in `-va/-ve` (and occasionally modal-resultative adjectives in `-t/-tt`) express static resultative states that depict the ongoing physical degradation of the natural landscape: `kiszáradva` (dried out), `elszikesedve` (salinized), `lecsapolva` (drained), `kizsigerelve` (exhausted/exploited), `tönkretéve` (ruined).",
            "gr_text2": "Example: `A lápok lecsapolva, a rétek felszántva hevernek az egykor dúsan virágzó ártér helyén, megfosztva a vidéket természetes hűtőmechanizmusától`.",
            "gr_table": [
                ["A hajdani vadvízország ma kiszáradva és porladva várja az esőt.", "The former wild wetland realm today dried out and crumbling awaits the rain."],
                ["A talaj elszikesedve és kizsigerelve képtelen megtartani a nedvességet.", "The soil salinized and depleted is unable to retain moisture."],
                ["A folyómedrek lebetonozva és kiegyenesítve gyorsítják a víz lefolyását.", "Riverbeds concreted and straightened accelerate the runoff of water."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mit jelent az 'elszikesedés' jelensége a mezőgazdaságban?", [
                    "A talaj felső rétegének káros mértékű sófelhalmozódását, ami gátolja a növények fejlődését.",
                    "A szénsavas ásványvizek palackozásának folyamatát.",
                    "A búza aratásának leggyorsabb modern gépi módszerét."
                ], 0, ["c1-20-vocab"]),
                fb("grammar", "controlled", "A láprétek teljesen _____, a fák elszáradva merednek az ég felé. (drained / lecsapolva)", "lecsapolva", "The moor meadows completely drained, the trees parched stare toward the sky.", ["c1-participle-passive-resultative-state"]),
                match("vocabulary", "controlled", [["elszikesedés", "káros sók felhalmozódása a termőrétegben"], ["tájseb", "a természetes környezet mély, mesterséges sérülése"], ["mocsárlecsapolás", "vizes élőhelyek felszámolása szántóföldszerzésért"], ["monokultúra", "egyetlen növényfaj kizárólagos, kiterjedt termesztése"]], ["c1-20-vocab"]),
                fb("grammar", "practice", "A folyómeder szűk betonfalak közé _____ vezeti el az éltető áradást. (squeezed / szorítva)", "szorítva", "The riverbed squeezed between narrow concrete walls carries away the life-giving flood.", ["c1-participle-passive-resultative-state"]),
                sb("grammar", "practice", ["A", "föld", "kizsigerelve", "és", "kiszáradva", "fekszik", "az", "Alföldön."], ["A", "föld", "kizsigerelve", "és", "kiszáradva", "fekszik", "az", "Alföldön."], "The earth exhausted and dried out lies on the Great Plain.", ["c1-participle-passive-resultative-state"]),
                dc("dialogue", [
                    {"speaker": "Ökológus", "text": "Hogyan néz ki ma a történelmi Nagysárrét területe?"},
                    {"speaker": "Földrajztudós", "text": "A hajdani vizek lecsapolva, a medrek _____ hevernek a forró nyárban."},
                ], ["eltemetve", "repülve", "úszva"], 0, ["c1-participle-passive-resultative-state"]),
                sw("production", [{"prompt": "Describe a parched or degraded landscape using a participial state expression (-va/-ve).", "answer": "A homokhátság egykor gazdag mocsarai lecsapolva, a fenyvesek elszáradva tanúskodnak a fenntarthatatlan tájátalakítás következményeiről."}], ["c1-participle-passive-resultative-state"]),
                mc("grammar", "check", "Melyik mondatrész fejez ki állapotot leíró igeneves szerkezetet?", [
                    "kizsigerelve és kiszáradva hever",
                    "amikor a gazda kimegy a mezőre",
                    "hogy több gabonát tudjon eladni"
                ], 0, ["c1-participle-passive-resultative-state"])
            ]
        },
        {
            "num": 3,
            "stem": "c1-20-03",
            "title": "Short-Term Profit vs. Ecological Viability: Adversative Concessives",
            "grammar_title": "Adversative Concessive Structures Contrasting Economic Gains with Ecological Costs",
            "grammar_skill": "c1-adv-adversative-ecological-concessives",
            "goals": [
                "I can debate the clash between agribusiness revenue and ecological preservation (*agrárlobbi, rövid távú profithajhászás, természeti tőkevesztés*).",
                "I can employ elevated adversative concessive pairs (*ámbár... mégsem, jóllehet... ennek dacára, noha... semmiképp sem*).",
                "I can articulate nuanced critiques of industrial agriculture's unsustainable resource consumption."
            ],
            "vocab": [
                {"lemma": "természeti tőkevesztés", "translation": "loss of natural capital", "pos": "expression"},
                {"lemma": "rövid távú profithajhászás", "translation": "short-term profit-seeking", "pos": "expression"},
                {"lemma": "agrárlobbi", "translation": "agricultural lobby", "pos": "noun"},
                {"lemma": "öntözési túlhasználat", "translation": "irrigation overexploitation", "pos": "expression"},
                {"lemma": "ökoszisztéma-szolgáltatás", "translation": "ecosystem service", "pos": "expression"},
                {"lemma": "tájgazdálkodási reform", "translation": "landscape management reform", "pos": "expression"},
                {"lemma": "ökológiai lábnyom", "translation": "ecological footprint", "pos": "expression"},
                {"lemma": "haszonelvű megközelítés", "translation": "utilitarian approach", "pos": "expression"}
            ],
            "gr_text1": "Adversative concessive structures balance valid economic arguments against overwhelming ecological costs: `ámbár... mégsem` (although... yet not), `jóllehet... ennek dacára` (even though... despite this), `noha... semmiképp sem` (while... in no way).",
            "gr_text2": "Example: `Jóllehet a belvíz gyors elvezetése rövid távon növelte a szántóterületek méretét, ennek dacára hosszú távon felmérhetetlen ökológiai katasztrófát idézett elő`.",
            "gr_table": [
                ["Ámbár az intenzív öntözés átmenetileg növeli a terméshozamot, mégsem fenntartható a karsztvíz kimerülése miatt.", "Although intensive irrigation temporarily increases crop yield, it is still not sustainable due to the depletion of karst water."],
                ["Jóllehet a gazdák újabb gátakat követelnek, ennek dacára a víz visszatartása jelentené a valódi megoldást.", "Even though farmers demand further dikes, despite this, retaining water would represent the real solution."],
                ["Noha az ipari lobbi gazdasági növekedést ígér, semmiképp sem szabad feláldozni ivóvízbázisainkat.", "While the industrial lobby promises economic growth, in no way must we sacrifice our drinking water reserves."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mit jelent az 'ökoszisztéma-szolgáltatás' fogalma az ökológiai közgazdaságtanban?", [
                    "A természet által az emberi társadalom számára ingyenesen nyújtott javakat és folyamatokat (pl. víztisztítás, beporzás, árvízmegelőzés).",
                    "A nemzeti parkok belépőjegyeinek online árusítását.",
                    "A háziállatok orvosi ellátását biztosító állami támogatást."
                ], 0, ["c1-20-vocab"]),
                fb("grammar", "controlled", "Jóllehet a monokultúrás gazdálkodás rekordtermést hozott, ennek _____ a talajélet teljesen elpusztult. (despite this / dacára)", "dacára", "Even though monoculture farming yielded record harvests, despite this soil life completely perished.", ["c1-adv-adversative-ecological-concessives"]),
                match("vocabulary", "controlled", [["természeti tőkevesztés", "az élő környezet megújulóképességének elpazarlása"], ["rövid távú profithajhászás", "a pillanatnyi haszon hajszolása a jövő feláldozásával"], ["ökoszisztéma-szolgáltatás", "a természet ingyenes életfenntartó működése"], ["ökológiai lábnyom", "az emberi fogyasztás természetre gyakorolt terhelése"]], ["c1-20-vocab"]),
                fb("grammar", "practice", "Ámbár a csatornázás védte a vetést, _____ védte meg a tájat a nyári aszálytól. (yet not / mégsem)", "mégsem", "Although canalization protected the sowing, it yet did not protect the landscape from summer drought.", ["c1-adv-adversative-ecological-concessives"]),
                sb("grammar", "practice", ["Jóllehet", "támogatják", "az", "öntözést,", "ennek", "dacára", "a", "vízkészlet", "apad."], ["Jóllehet", "támogatják", "az", "öntözést,", "ennek", "dacára", "a", "vízkészlet", "apad."], "Even though they subsidize irrigation, despite this water reserves dwindle.", ["c1-adv-adversative-ecological-concessives"]),
                dc("dialogue", [
                    {"speaker": "Agrármérnök", "text": "Az iparszerű termelés nélkül éhezne a lakosság!"},
                    {"speaker": "Környezetvédő", "text": "Ámbár a hozamok emelkedtek, _____ szabad szemet hunyni a talajok elsavanyodása felett."},
                ], ["mégsem", "biztosan", "könnyen"], 0, ["c1-adv-adversative-ecological-concessives"]),
                sw("production", [{"prompt": "Formulate a sentence contrasting economic profit with environmental cost using 'Jóllehet... ennek dacára'.", "answer": "Jóllehet az ipari akkumulátorgyárak munkahelyeket teremtenek, ennek dacára mértéktelen vízfogyasztásuk végzetesen veszélyezteti a térség lakossági ivóvízbázisát."}], ["c1-adv-adversative-ecological-concessives"]),
                mc("grammar", "check", "Melyik kötőszói pár fejez ki emelkedett megengedő-ellentétező viszonyt?", [
                    "Jóllehet... ennek dacára",
                    "Nemcsak... hanem is",
                    "Ezért... tehát"
                ], 0, ["c1-adv-adversative-ecological-concessives"])
            ]
        },
        {
            "num": 4,
            "stem": "c1-20-04",
            "title": "Historical River Engineering & Complex Counterfactual Conditionals",
            "grammar_title": "Complex Counterfactual Conditional Structures Evaluating Historical Environmental Interventions",
            "grammar_skill": "c1-complex-hypothetical-counterfactuals",
            "goals": [
                "I can evaluate the historic 19th-century Tisza river regulation and drainage policies (*Tisza-szabályozás, Vásárhelyi Pál, ártéri fokgazdálkodás*).",
                "I can construct complex past-hypothetical counterfactual conditional sentences (*ha nem szabályozták volna... ma nem fenyegetne; lett volna... megmenthető lett volna*).",
                "I can debate historical alternatives to flood-control dykes: floodplain retention vs. expedited runoff."
            ],
            "vocab": [
                {"lemma": "folyószabályozás", "translation": "river regulation / channelization", "pos": "noun"},
                {"lemma": "fokgazdálkodás", "translation": "fok-system floodplain water management", "pos": "noun"},
                {"lemma": "ártér", "translation": "floodplain", "pos": "noun"},
                {"lemma": "kanyarulatátvágás", "translation": "meander cutoff", "pos": "noun"},
                {"lemma": "árvízvédelmi gátrendszer", "translation": "flood protection dike system", "pos": "expression"},
                {"lemma": "lefolyásgyorsítás", "translation": "accelerated runoff", "pos": "noun"},
                {"lemma": "tájrombolás", "translation": "landscape destruction", "pos": "noun"},
                {"lemma": "vízvisszatartás", "translation": "water retention", "pos": "noun"}
            ],
            "gr_text1": "Counterfactual conditionals evaluate historical decisions using the past conditional in `-t/-tt volna` paired with either past or present consequences: `Ha nem vágták volna át a Tisza kanyarulatait, a folyó lassabban vonult volna le, és a talajvíz ma nem süllyedne ilyen vészes ütemben`.",
            "gr_text2": "In academic historiography and environmental economics, this construction allows the speaker to model alternative historical trajectories (e.g. traditional floodplain retention vs. total drainage).",
            "gr_table": [
                ["Ha megőrizték volna az ősi ártéri fokgazdálkodást, az Alföld ma nem száradna ki.", "If they had preserved ancient floodplain management, the Great Plain would not be drying out today."],
                ["Ha a gátépítések helyett víztározókat alakítottak volna ki, elkerülhető lett volna az aszálykatasztrófa.", "If they had developed reservoirs instead of dike building, the drought catastrophe would have been avoidable."],
                ["Amennyiben tiszteletben tartották volna a folyó természetes dinamikáját, a vizes élőhelyek megmaradtak volna.", "Had they respected the natural dynamics of the river, the wetlands would have survived."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mi volt az ősi magyar 'fokgazdálkodás' lényege a folyószabályozások előtt?", [
                    "A folyó áradásának kivezetése a természetes fokokon át az ártérbe, biztosítva a halászatot, a legelőket és a víz tárolását.",
                    "A folyók lebetonozása és gátak közé szorítása a gyorsabb hajózásért.",
                    "A halak szigorú exportálása a bécsi udvar számára."
                ], 0, ["c1-20-vocab"]),
                fb("grammar", "controlled", "Ha a 19. században nem _____ le a mocsarakat, ma több ivóvízünk lenne. (had not drained / csapolták volna)", "csapolták volna", "If in the 19th century they had not drained the marshes, today we would have more drinking water.", ["c1-complex-hypothetical-counterfactuals"]),
                match("vocabulary", "controlled", [["folyószabályozás", "a meder mesterséges átalakítása a hajózásért és árvízvédelemért"], ["fokgazdálkodás", "természetes ártéri vízszétosztó rendszer"], ["kanyarulatátvágás", "a folyókanyarok levágása a vízlefolyás gyorsítására"], ["vízvisszatartás", "a felesleges víz tájban tartása a száraz időszakokra"]], ["c1-20-vocab"]),
                fb("grammar", "practice", "Ha rugalmasabb tájhasználatot választottak volna, elkerülhető _____ a homokhátság félsivatagosodása. (would have been / lett volna)", "lett volna", "If they had chosen more flexible land use, the semi-desertification of the sand ridge would have been avoidable.", ["c1-complex-hypothetical-counterfactuals"]),
                sb("grammar", "practice", ["Ha", "vizet", "tartottak", "volna,", "nem", "pusztulna", "a", "természet."], ["Ha", "vizet", "tartottak", "volna,", "nem", "pusztulna", "a", "természet."], "If they had retained water, nature would not be perishing.", ["c1-complex-hypothetical-counterfactuals"]),
                dc("dialogue", [
                    {"speaker": "Történész", "text": "Hiba volt Vásárhelyi Pál koncepciója a Tisza szabályozására?"},
                    {"speaker": "Vízügyi mérnök", "text": "Ha a korabeli mérnökök számoltak volna a klímaváltozással, más stratégiát _____."},
                ], ["választottak volna", "választanak", "választottak"], 0, ["c1-complex-hypothetical-counterfactuals"]),
                sw("production", [{"prompt": "Write a counterfactual sentence evaluating past river engineering using 'ha... volna'.", "answer": "Ha a tizenkilencedik századi vízrendezés során nem a víz mielőbbi levezetésére törekedtek volna, a mai Alföld nem küzdene ilyen drámai talajvízvesztéssel."}], ["c1-complex-hypothetical-counterfactuals"]),
                mc("grammar", "check", "Melyik igealak fejez ki múltbeli ellenfaktikus (meg nem valósult) feltételt?", [
                    "nem szabályozták volna / megmenthető lett volna",
                    "nem fognak szabályozni",
                    "amint megkezdik a munkát"
                ], 0, ["c1-complex-hypothetical-counterfactuals"])
            ]
        },
        {
            "num": 5,
            "stem": "c1-20-05",
            "title": "Kaán Károly, Great Plain Afforestation & Scalar Depletion Adverbials",
            "grammar_title": "Scalar Depletion Adverbials Quantifying Rates of Natural Resource Exhaustion",
            "grammar_skill": "c1-adv-scalar-depletion-markers",
            "goals": [
                "I can analyze Kaán Károly's seminal 1931 work 'Természetvédelem és a magyar táj' and Great Plain afforestation programs.",
                "I can employ scalar depletion adverbials quantifying resource exhaustion (*visszafordíthatatlanul, vészesen, fokozatosan, drámai ütemben*).",
                "I can synthesize the historical evolution of Hungarian nature protection from forestry science to modern ecological conservation."
            ],
            "vocab": [
                {"lemma": "alföldfásítás", "translation": "afforestation of the Great Plain", "pos": "noun"},
                {"lemma": "természetvédelem úttörője", "translation": "pioneer of nature conservation", "pos": "expression"},
                {"lemma": "talajerózió", "translation": "soil erosion", "pos": "noun"},
                {"lemma": "erdőgazdálkodás", "translation": "forest management / silviculture", "pos": "noun"},
                {"lemma": "vízmérleg", "translation": "water balance / budget", "pos": "noun"},
                {"lemma": "tájökológiai szemlélet", "translation": "landscape ecological perspective", "pos": "expression"},
                {"lemma": "szélvédelem", "translation": "windbreak protection", "pos": "noun"},
                {"lemma": "természeti örökség", "translation": "natural heritage", "pos": "expression"}
            ],
            "gr_text1": "Scalar depletion adverbials calibrate the velocity, momentum, and irreversibility of ecological loss: `visszafordíthatatlanul` (irreversibly), `vészesen` (perilously/alarmingly), `fokozatosan` (gradually), `drámai ütemben` (at a dramatic pace), `szemlátomást` (visibly).",
            "gr_text2": "Example: `A Duna-Tisza közi kutak vize vészesen megcsappant, és a homoktalaj nedvességtartalma visszafordíthatatlanul a kritikus szint alá süllyedt`.",
            "gr_table": [
                ["A talajvízkészlet vészesen csökken a forró nyári hónapokban.", "The groundwater reserve is decreasing perilously during the hot summer months."],
                ["Az őshonos erdőtársulások területe fokozatosan zsugorodik az Alföldön.", "The area of native forest communities is shrinking gradually across the Great Plain."],
                ["A Kárpát-medence vízháztartása visszafordíthatatlanul megváltozott a szabályozások nyomán.", "The water regime of the Carpathian Basin changed irreversibly in the wake of the regulations."]
            ],
            "classic_story": {
                "slug": "c1-20-kaan",
                "author": "Kaán Károly",
                "work": "Természetvédelem és a magyar táj (1931)",
                "title": "Kaán Károly: A magyar táj védelme és az Alföld fásítása",
                "summary": "Forest engineer Kaán Károly's visionary 1931 text inaugurating modern Hungarian nature protection, advocating for the afforestation of the arid Great Plain and a holistic hydrological-landscape perspective.",
                "characters": ["Kaán Károly"],
                "paragraphs": [
                    {"type": "narration", "text": "Amikor Kaán Károly erdőmérnök és államtitkár 1931-ben közzétette monumentális munkáját, a 'Természetvédelem és a magyar táj' című művet, a trianoni békediktátum által megcsonkított ország legsúlyosabb természeti sebére mutatott rá. Magyarország elveszítette hegyvidéki, gazdag fenyveseit és tölgyeseit; az új országhatárok közé szorult csonka haza szinte egyetlen végtelen, száraz és fátlan síksággá vált. Kaán zsenialitása abban állt, hogy a természetvédelmet nem elszigetelt esztétikai kérdésként, hanem a nemzet túlélésének zálogaként fogta fel."},
                    {"type": "narration", "text": "Kaán pontosan látta: a tizenkilencedik századi folyószabályozások ugyan megvédték a városokat a katasztrofális árvizektől, ám a vizek elvezetésével vészesen felborították az Alföld kényes vízmérlegét. A lecsapolt lápok helyén futóhomok és szikes pusztaság maradt, amelyet a kíméletlen tavaszi és nyári szelek akadálytalanul hordtak szét, felperzselve a zsenge vetést és elsorvasztva a termőföldet. A természetes tájegyensúly visszafordíthatatlanul megbomlott."},
                    {"type": "narration", "text": "E drámai pusztulásra válaszul indította el Kaán az alföldfásítás nagyszabású programját. Vallotta, hogy a fáknak és az erdősávoknak nemcsak a faanyagtermelés a feladatuk, hanem az éltető mikroklíma megóvása: a szél fékezése, a párolgás csökkentése és a talajnedvesség megőrzése. Mezővédő erdősávok nélkül az Alföld sorsa a teljes elsivatagosodás lett volna."},
                    {"type": "narration", "text": "Kaán Károly szellemi öröksége ma aktuálisabb, mint valaha. Munkásságával megalapozta az 1935-ös első magyar természetvédelmi törvényt, de ami ennél is fontosabb: megtanított bennünket arra, hogy a tájra osztatlan egészként tekintsünk, ahol a víz, az erdő és az emberi munka egymástól elválaszthatatlan szimbiózisban él vagy pusztul el."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Miért tekintik Kaán Károlyt a magyar természetvédelem úttörőjének?", [
                    "Mert ő ismerte fel, hogy az Alföld fásítása és a mezővédő erdősávok elengedhetetlenek a szikesedés megállításához és a táj klímájának védelméhez.",
                    "Mert ő építette a legelső fa hidat a Dunán.",
                    "Mert egzotikus pálmafákat telepített a budapesti parkokba."
                ], 0, ["c1-20-vocab"]),
                fb("grammar", "controlled", "A homokhátság talajvízszintje _____ apad az egyre forróbb aszályos nyarakon. (perilously / vészesen)", "vészesen", "The groundwater level of the sand ridge is dwindling perilously during increasingly hot drought summers.", ["c1-adv-scalar-depletion-markers"]),
                match("vocabulary", "controlled", [["alföldfásítás", "erdősávok telepítése a síkság klímavédelméért"], ["szélvédelem", "fák ültetése a talaj porlódásának megakadályozására"], ["vízmérleg", "a tájba érkező és onnan távozó víz egyensúlya"], ["tájökológia", "a természeti elemek és az ember kölcsönhatásának tudománya"]], ["c1-20-vocab"]),
                mc("reading", "practice", "Kaán Károly szerint miért borult fel az Alföld természetes tájegyensúlya a 19. század után?", [
                    "Mert a vizek túlzott elvezetése és a fák hiánya miatt a szél felverte a futóhomokot és kiszárította a termőréteget.",
                    "Mert túl sok gyümölcsfát ültettek a folyók mentén.",
                    "Mert a vasúti közlekedés elriasztotta az erdei vadállatokat."
                ], 0, None),
                sb("grammar", "practice", ["A", "talajvízkészlet", "vészesen", "megcsappant", "az", "egész", "Alföldön."], ["A", "talajvízkészlet", "vészesen", "megcsappant", "az", "egész", "Alföldön."], "The groundwater reserve depleted alarmingly across the whole Great Plain.", ["c1-adv-scalar-depletion-markers"]),
                sw("production", [{"prompt": "Write a critical reflection on Kaán Károly's environmental legacy using a scalar depletion adverb.", "answer": "Kaán Károly már egy évszázada figyelmeztetett: ha a táj vízháztartása vészesen felborul, a mezővédő erdősávok hiányában az Alföld sorsa a visszafordíthatatlan elsivatagosodás lesz."}], ["c1-adv-scalar-depletion-markers"]),
                mc("grammar", "check", "Melyik határozószó fejez ki fokozati, mértékbeli kimerülési folyamatot az ökológiai elemzésben?", [
                    "vészesen / visszafordíthatatlanul",
                    "lassan sétálva",
                    "tavaly tavasszal"
                ], 0, ["c1-adv-scalar-depletion-markers"])
            ]
        }
    ]

    for l in core_lessons:
        emit_instructional_lesson(20, "core", l, core_title, core_intro if l["num"] == 1 else None)

    # Core Consolidation Lesson
    emit_consolidation_lesson(
        20,
        "core",
        "c1-20-consolidation",
        core_title,
        [
            "I can master C1 academic vocabulary of ecological fragility, desertification, and soil degradation.",
            "I can deploy environmental causal chains, resultative participial states, and adversative concessives.",
            "I can evaluate counterfactual hydro-engineering scenarios and Kaán Károly's conservation legacy."
        ],
        [
            mc("grammar", "recognize", "Melyik mondat alkalmaz helyes környezeti ok-okozati névutót formális stílusban?", [
                "A talajvíz mélyülése következtében és a folyamatos aszály folytán az őshonos növényvilág elsorvadt.",
                "A növények a folyó mellett pihentek békésen a napsütésben.",
                "Mivel szép volt az idő, kimentek a természetbe túrázni."
            ], 0, ["c1-adv-environmental-causal-chains"]),
            mc("grammar", "recognize", "Milyen szerkezettel fejezhetünk ki degradált környezeti állapotot plasztikusan?", [
                "a lápok lecsapolva, a talaj kizsigerelve és kiszáradva hever",
                "a gazdák vidáman dalolnak a szántóföldön",
                "miután megvásárolták az új traktort a boltban"
            ], 0, ["c1-participle-passive-resultative-state"]),
            match("vocabulary", "recognize", [["elsivatagosodás", "a termékeny talaj átalakulása száraz pusztasággá"], ["ökoszisztéma-szolgáltatás", "a természet életfenntartó folyamatai a társadalom számára"], ["fokgazdálkodás", "hagyományos, áradásra épülő ártéri vízgazdálkodás"], ["alföldfásítás", "mezővédő erdősávok Kaán Károly által indított programja"], ["vízmérleg", "a táj vízkészletének bevétele és kiadása közötti arány"]], ["c1-20-vocab"]),
            fb("vocabulary", "recall", "A Duna-Tisza közi homokhátság legveszélyesebb folyamata a gyors ütemű _____. (desertification / elsivatagosodás)", "elsivatagosodás", "The most dangerous process of the sand ridge between Danube and Tisza is rapid desertification.", ["c1-20-vocab"]),
            fb("vocabulary", "recall", "A folyók gátak közé szorítása helyett ma a tájba illeszkedő _____ kellene előtérbe helyezni. (water retention / vízvisszatartást)", "vízvisszatartást", "Instead of confining rivers between dikes today landscape-conforming water retention should be prioritized.", ["c1-20-vocab"]),
            fb("grammar", "recall", "A fenntarthatatlan talajhasználat _____ a homoktalaj termőképessége végzetesen leromlott. (as a result of / következtében)", "következtében", "As a result of unsustainable soil use the fertility of sandy soil deteriorated fatally.", ["c1-adv-environmental-causal-chains"]),
            fb("grammar", "context", "Jóllehet gátakkal védték a várost, ennek _____ a háttérben fekvő mezők kiszáradtak. (despite this / dacára)", "dacára", "Even though they protected the city with dikes, despite this the fields lying in the background dried out.", ["c1-adv-adversative-ecological-concessives"]),
            fb("grammar", "context", "Ha nem vezették volna el a belvizeket, ma nem apadna ilyen _____ a kútjaink vize. (perilously / vészesen)", "vészesen", "If they had not drained inland waters, today the water in our wells would not be dwindling so perilously.", ["c1-adv-scalar-depletion-markers"]),
            mc("grammar", "context", "Mi a szerepe az ellenfaktikus 'Ha... lett volna' szerkezeteknek a tájtörténeti elemzésekben?", [
                "Lehetővé teszi a 19. századi mérnöki döntések és a korabeli alternatívák objektív kritikai felülvizsgálatát.",
                "Kifejezi a beszélő teljes érdektelenségét a folyók iránt.",
                "Elnézést kér az árvízkárosultaktól a károkért."
            ], 0, ["c1-complex-hypothetical-counterfactuals"]),
            sb("grammar", "produce", ["A", "tájban", "tartott", "víz", "a", "jövő", "legdrágább", "kincse."], ["A", "tájban", "tartott", "víz", "a", "jövő", "legdrágább", "kincse."], "Water retained in the landscape is the most precious treasure of the future.", ["c1-adv-scalar-depletion-markers"]),
            sw("production", [{"prompt": "Write a diagnostic sentence about the ecological crisis of the Great Plain using a causal chain postposition.", "answer": "A gátrendszerek kiépítése és a túlzott csatornázás folytán a Kárpát-medence természetes vízháztartása felborult, elmélyítve a nyári aszályok pusztító hatását."}], ["c1-adv-environmental-causal-chains"]),
            sw("production", [{"prompt": "Formulate a concluding thought on Kaán Károly's conservation philosophy.", "answer": "Kaán Károly öröksége arra int bennünket, hogy a természet védelme nem csupán esztétikai kötelesség, hanem a magyar nemzet megmaradásának elemi ökológiai feltétele."}], ["c1-adv-scalar-depletion-markers"])
        ]
    )

    # ----------------------------------------------------
    # TRACK 2: DISCOURSE (c1-vizgazdalkodas)
    # ----------------------------------------------------
    slug = "vizgazdalkodas"
    disc_intro = [
        "Water is the defining strategic resource of the 21st century. While Hungary once prided itself on being a nation of waters ('a vizek országa'), misdirected hydro-engineering, severe climate droughts, and rampant industrial demand—such as battery gigafactories—have exposed profound vulnerabilities.",
        "In this unit, you will master the elevated discourse of statutory conservation mandates, systemic threat framing, climate correlatives, and policy synthesis in Hungarian environmental politics."
    ]

    disc_lessons = [
        {
            "num": 1,
            "stem": f"c1-{slug}-01",
            "title": "The Drying Danube-Tisza Sand Ridge & Ecological Threat Framing",
            "grammar_title": "Discourse Framing Markers Diagnosing Acute Ecological Crises and Systemic Threats",
            "grammar_skill": "c1-discourse-ecological-threat-framing",
            "goals": [
                "I can analyze the desiccation of the Duna-Tisza Interfluve sand ridge (*homokhátság, talajvízvesztés, félsivatagosodás*).",
                "I can deploy ecological threat framing discourse markers (*akut válsághelyzetet idéz elő, közvetlen fenyegetést jelent, végveszélybe sodor*).",
                "I can articulate the scientific consensus on the aridification of Central Europe."
            ],
            "vocab": [
                {"lemma": "homokhátság", "translation": "sand ridge / interfluve plateau", "pos": "noun"},
                {"lemma": "félsivatagosodás", "translation": "semi-desertification", "pos": "noun"},
                {"lemma": "kiszáradási góc", "translation": "focal point of desiccation", "pos": "expression"},
                {"lemma": "talajvízkészlet", "translation": "groundwater reserve", "pos": "noun"},
                {"lemma": "akut veszélyhelyzet", "translation": "acute emergency / hazard state", "pos": "expression"},
                {"lemma": "éghajlati sérülékenység", "translation": "climate vulnerability", "pos": "expression"},
                {"lemma": "ökológiai katasztrófa", "translation": "ecological catastrophe", "pos": "expression"},
                {"lemma": "visszafordíthatatlan kár", "translation": "irreversible damage", "pos": "expression"}
            ],
            "gr_text1": "Discourse framing markers articulate systemic risk and ecological danger in elevated scientific and policy debate: `akut válsághelyzetet idéz elő` (brings about an acute crisis situation), `közvetlen fenyegetést jelent` (poses a direct threat), `végveszélybe sodor` (drags into ultimate peril), `felbecsülhetetlen kárt okoz` (causes inestimable damage).",
            "gr_text2": "Example: `A Duna-Tisza közi talajvíz öt-hat méteres süllyedése akut válsághelyzetet idéz elő, amely végveszélybe sodorja a térség agráriumát és ivóvízbázisát`.",
            "gr_table": [
                ["A hosszan tartó aszály közvetlen fenyegetést jelent a hazai élelmiszer-biztonságra.", "Prolonged drought poses a direct threat to domestic food security."],
                ["A felelőtlen vízpolitika akut válsághelyzetet idéz elő a Homokhátságon.", "Irresponsible water policy brings about an acute crisis situation on the Sand Ridge."],
                ["A természetes vizes élőhelyek felszámolása végveszélybe sodorja a madárvilágot.", "The eradication of natural wetlands drags the bird fauna into ultimate peril."]
            ],
            "world_story_seg": {
                "seg_slug": "homokhatsag",
                "title": "A Homokhátság szomjúsága: félsivatag születik Európa szívében",
                "summary": "Exploring the rapid aridification of the Danube-Tisza sand ridge, where groundwater levels have dropped by up to six meters, creating an ecological crisis zone.",
                "paragraphs": [
                    {"type": "narration", "text": "Kecskeméttől délre, a Duna és a Tisza folyók közötti magaslaton a táj csendesen, de feltartóztathatatlanul változik. Ahol ötven évvel ezelőtt még tocsogós láprétek, gazdag tanyasi gyümölcsösök és nádas tócsák tarkították a homokbuckákat, ott ma a fű sárgára égett, a szél port kavar, és a régi kutak mélyén száraz csend honol. Az ENSZ Élelmezésügyi és Mezőgazdasági Szervezete nem véletlenül sorolta a Duna-Tisza közi Homokhátságot a félsivatagosodással közvetlenül fenyegetett európai térségek közé."},
                    {"type": "narration", "text": "A kutatók adatai riasztóak: a talajvíz szintje helyenként öt-hat méterrel zuhant lejjebb, a térségből pedig évente több százmillió köbméterrel több víz párolog el, mint amennyi csapadék formájában visszahullik. Ez nem egyszerűen egy szokatlanul száraz nyár következménye: a huszadik századi meggondolatlan csatornázások és a klímaváltozás kettős szorításában a Homokhátság akut ökológiai válságövezetté vált, amely a teljes alföldi életforma jövőjét megkérdőjelezi."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Miért tekintik a Duna-Tisza közi Homokhátságot Európa egyik legsérülékenyebb zónájának?", [
                    "Mert a talajvízszint drámai zuhanása miatt a terület a félsivatagosodás közvetlen határára sodródott.",
                    "Mert túl sok homokos tengerparti üdülőhely épült a térségben.",
                    "Mert a Duna és a Tisza minden évben teljesen elönti a magaslatokat."
                ], 0, ["c1-vizgazdalkodas-vocab"]),
                fb("grammar", "controlled", "A talajvíz mélyülése közvetlen _____ jelent a dél-alföldi gazdálkodók megélhetésére. (threat / fenyegetést)", "fenyegetést", "The dropping of groundwater poses a direct threat to the livelihood of southern Great Plain farmers.", ["c1-discourse-ecological-threat-framing"]),
                match("vocabulary", "controlled", [["homokhátság", "a Duna és Tisza közötti száraz homokos hátság"], ["félsivatagosodás", "a csapadékhiány miatti szélsőséges szárazulattá válás"], ["kiszáradási góc", "a vízhiány által leginkább sújtott központi terület"], ["akut veszélyhelyzet", "azonnali beavatkozást igénylő kritikus állapot"]], ["c1-vizgazdalkodas-vocab"]),
                fb("grammar", "practice", "A folytatódó kizsákmányolás akut _____ idéz elő a természetes vízgyűjtőkben. (crisis situation / válsághelyzetet)", "válsághelyzetet", "Continuing exploitation brings about an acute crisis situation in natural water catchments.", ["c1-discourse-ecological-threat-framing"]),
                sb("grammar", "practice", ["A", "szárazság", "végveszélybe", "sodorja", "a", "térség", "természetes", "élővilágát."], ["A", "szárazság", "végveszélybe", "sodorja", "a", "térség", "természetes", "élővilágát."], "Drought drags the region's natural wildlife into ultimate peril.", ["c1-discourse-ecological-threat-framing"]),
                dc("dialogue", [
                    {"speaker": "Környezetkutató", "text": "Milyen következményekkel jár a Homokhátság vízhiánya?"},
                    {"speaker": "Tájökológus", "text": "A kutak elapadása közvetlen _____ jelent az ott élő lakosság alapvető ivóvízellátására."},
                ], ["veszélyt", "örömet", "segítséget"], 0, ["c1-discourse-ecological-threat-framing"]),
                sw("production", [{"prompt": "Write a sentence framing an environmental threat using 'közvetlen fenyegetést jelent'.", "answer": "A talajvíz folyamatos süllyedése közvetlen fenyegetést jelent a Kárpát-medence mezőgazdasági termelésére és a ritka homoki tölgyesek fennmaradására."}], ["c1-discourse-ecological-threat-framing"]),
                mc("grammar", "check", "Melyik kifejezés alkalmas rendszerszintű ökológiai veszélyhelyzet formális megfogalmazására?", [
                    "akut válsághelyzetet idéz elő / közvetlen fenyegetést jelent",
                    "kicsit melegebb az idő",
                    "nagyon szép a táj délután"
                ], 0, ["c1-discourse-ecological-threat-framing"])
            ]
        },
        {
            "num": 2,
            "stem": f"c1-{slug}-02",
            "title": "The Tisza River Dilemma: Rapid Drainage vs. Water Retention",
            "grammar_title": "Deontic Modal Structures Formulating Statutory Environmental Obligations and Conservation Imperatives",
            "grammar_skill": "c1-modal-conservation-deontics",
            "goals": [
                "I can analyze the historical conflict between flood protection dikes and drought mitigation (*gátépítés, árvízi levezetés, aszályvédelem*).",
                "I can construct statutory deontic modal structures formulating conservation imperatives (*kötelessége megóvni, határozott tiltást szab, elengedhetetlen előírni*).",
                "I can debate the transition from flood runoff acceleration to active landscape water retention."
            ],
            "vocab": [
                {"lemma": "gátépítés", "translation": "dike / levee construction", "pos": "noun"},
                {"lemma": "aszályvédelem", "translation": "drought protection", "pos": "noun"},
                {"lemma": "tájba illeszkedő víztározás", "translation": "landscape-conforming water storage", "pos": "expression"},
                {"lemma": "törvényi kötelezettség", "translation": "statutory obligation", "pos": "expression"},
                {"lemma": "természetvédelmi imperatívusz", "translation": "conservation imperative", "pos": "expression"},
                {"lemma": "hullámtér", "translation": "floodway / river active washland", "pos": "noun"},
                {"lemma": "vízkészlet-gazdálkodás", "translation": "water resources management", "pos": "noun"},
                {"lemma": "hatósági korlátozás", "translation": "regulatory restriction", "pos": "expression"}
            ],
            "gr_text1": "Conservation mandates and statutory duties are articulated through formal deontic verbs, impersonal postpositions, and deontic noun phrases: `kötelessége megóvni` (it is an obligation to preserve), `határozott tiltást szab` (imposes a strict ban), `elengedhetetlen előírni` (it is indispensable to stipulate), `természetvédelmi imperatívuszként jelenik meg` (appears as a conservation imperative).",
            "gr_text2": "Example: `Az állam elidegeníthetetlen törvényi kötelessége megóvni az édesvízkészleteket, és határozott korlátozást kell szabnia a felszíni vizek túlzott elvezetése elé`.",
            "gr_table": [
                ["A jogalkotónak kötelessége megóvni a folyók természetes hullámterét.", "The legislator has the duty to preserve the natural floodway of rivers."],
                ["A vízügyi hatóság határozott tiltást szab a védett területek lecsapolására.", "The water authority imposes a strict ban on the drainage of protected areas."],
                ["Elengedhetetlen előírni a vizek helyben tartását garantáló területhasználati szabályokat.", "It is indispensable to stipulate land use rules guaranteeing the retention of waters on site."]
            ],
            "world_story_seg": {
                "seg_slug": "tiszabeka",
                "title": "A Tisza két arca: az árvizek rémétől a kiszáradó folyóágyig",
                "summary": "Investigating how the 19th-century focus on accelerating flood runoff turned the Tisza into a rapid drainpipe that now leaves the surrounding countryside parched in summer.",
                "paragraphs": [
                    {"type": "narration", "text": "A Tisza a magyar néplélek és költészet legmélyebben megénekelt folyója: a 'szőke Tisza', amely hol csendesen kanyarog a füzek alatt, hol félelmetes haraggal tör át a töltéseken. Amikor a tizenkilencedik század közepén Széchenyi István és Vásárhelyi Pál vezetésével megindult a folyó szabályozása, egyetlen gigantikus cél lebegett a mérnökök szeme előtt: megvédeni a falvakat az áradásoktól, és minél gyorsabban levonultatni a víztömeget a déli határok felé. Százkét kanyarulatot vágtak át, a folyó hossza harmadával rövidült, a víz sebessége pedig megsokszorozódott."},
                    {"type": "narration", "text": "Másfél évszázaddal később a mérleg tragikus fordulatot vett. A Tisza ma már nem kiterjedt ártéri paradicsom, hanem egy mélyre vágódott levezető csatorna. Tavaszi áradások idején a gátak közé szorított árhullám pillanatok alatt elhagyja az országot, nyáron viszont a folyó medre helyenként siralmasan elvékonyodik. A jogalkotó és a társadalom előtt ma elkerülhetetlen feladat áll: felül kell vizsgálni a régi dogmákat, és törvényi imperatívuszként kell kimondani, hogy a folyó vizét nem elvezetni, hanem szétteríteni és megőrizni kell a szomjazó tájban."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Miért alakult ki ellentmondás a Tisza szabályozásának eredeti célja és mai következményei között?", [
                    "Mert a víz gyors elvezetésére tervezett gátrendszer ma megakadályozza, hogy az árhullámok táplálják a kiszáradó alföldi talajokat.",
                    "Mert a Tiszán túl sok tengerjáró hajó közlekedik.",
                    "Mert a folyó vize hirtelen sós vizűvé változott."
                ], 0, ["c1-vizgazdalkodas-vocab"]),
                fb("grammar", "controlled", "A mindenkori kormánynak alkotmányos _____ megóvni a nemzet vízkincsét. (duty / kötelessége)", "kötelessége", "The government of the day has a constitutional duty to preserve the nation's water treasure.", ["c1-modal-conservation-deontics"]),
                match("vocabulary", "controlled", [["gátépítés", "mesterséges földgátak emelése az árvizek megfékezésére"], ["hullámtér", "a folyómeder és a védőtöltés közötti elönthető terület"], ["aszályvédelem", "a talaj nedvességének megőrzését célzó beavatkozások"], ["hatósági korlátozás", "jogi tilalom a természeti erőforrások túlhasználatára"]], ["c1-vizgazdalkodas-vocab"]),
                fb("grammar", "practice", "A törvényhozóknak határozott tiltást kell _____ a mélységi karsztvizek ipari elpazarlására. (impose / szabniuk)", "szabniuk", "Legislators must impose a strict ban on the industrial squandering of deep karst waters.", ["c1-modal-conservation-deontics"]),
                sb("grammar", "practice", ["Elengedhetetlen", "előírni", "a", "vizek", "tájban", "történő", "megtartását."], ["Elengedhetetlen", "előírni", "a", "vizek", "tájban", "történő", "megtartását."], "It is indispensable to stipulate the retention of waters in the landscape.", ["c1-modal-conservation-deontics"]),
                dc("dialogue", [
                    {"speaker": "Természetvédelmi biztos", "text": "Hogyan kényszeríthető ki a fenntartható tájhasználat?"},
                    {"speaker": "Környezetjogász", "text": "Alkotmányos kötelezettségként kell _____ a vizes élőhelyek érinthetetlenségét."},
                ], ["deklarálni", "titkolni", "tagadni"], 0, ["c1-modal-conservation-deontics"]),
                sw("production", [{"prompt": "Write a sentence articulating a statutory conservation mandate using 'kötelessége megóvni'.", "answer": "Az államnak elemi és elidegeníthetetlen kötelessége megóvni stratégiai ivóvízbázisainkat a rövid távú gazdasági érdekek agresszív kizsákmányolásával szemben."}], ["c1-modal-conservation-deontics"]),
                mc("grammar", "check", "Melyik szerkezet fejez ki kötelező érvényű törvényi imperatívuszt?", [
                    "kötelessége megóvni / határozott tiltást szab",
                    "talán megnézheti",
                    "ha ideje engedi, kimegy"
                ], 0, ["c1-modal-conservation-deontics"])
            ]
        },
        {
            "num": 3,
            "stem": f"c1-{slug}-03",
            "title": "Wetland Restoration, Floodplain Farming & Proportional Correlatives",
            "grammar_title": "Proportional Correlative Conjunctions Mapping Interdependent Climate and Ecological Shifts",
            "grammar_skill": "c1-adv-proportional-climate-correlatives",
            "goals": [
                "I can evaluate wetland revitalization, floodplain landscape management, and water buffering (*vizes élőhelyek rehabilitációja, ártéri gazdálkodás, vízmegtartó tájhasználat*).",
                "I can deploy proportional correlative conjunctions (*minél... annál..., minél több vizet tartunk meg... annál ellenállóbbá válik*).",
                "I can articulate ecological synergies between biodiversity restoration and regional climate adaptation."
            ],
            "vocab": [
                {"lemma": "vizes élőhely", "translation": "wetland habitat", "pos": "expression"},
                {"lemma": "ártéri tájgazdálkodás", "translation": "floodplain landscape management", "pos": "expression"},
                {"lemma": "ökoszisztéma-helyreállítás", "translation": "ecosystem restoration", "pos": "expression"},
                {"lemma": "vízpuffer", "translation": "water buffer", "pos": "noun"},
                {"lemma": "mikroklimatikus hűtés", "translation": "microclimatic cooling", "pos": "expression"},
                {"lemma": "tájreziliencia", "translation": "landscape resilience", "pos": "noun"},
                {"lemma": "biodiverzitás-megőrzés", "translation": "biodiversity conservation", "pos": "expression"},
                {"lemma": "mélyfekvésű terület", "translation": "low-lying depression / area", "pos": "expression"}
            ],
            "gr_text1": "Proportional correlatives (`minél... annál...` / `amennyivel... annyival...`) establish functional interdependent relationships between ecological interventions and climate resilience: `Minél több vizet tartunk meg a mélyfekvésű területeken, annál ellenállóbbá válik a térség mikroklímája az aszályhullámokkal szemben`.",
            "gr_text2": "This structure is essential in environmental policy to demonstrate that nature-based solutions yield non-linear, compounding benefits.",
            "gr_table": [
                ["Minél kiterjedtebbek a vizes élőhelyek, annál hatékonyabb a természetes mikroklimatikus hűtés.", "The more extensive the wetlands, the more effective the natural microclimatic cooling."],
                ["Minél gyorsabban folyik le az árhullám, annál súlyosabb aszály fenyegeti a nyarat.", "The faster the flood wave runs off, the more severe drought threatens the summer."],
                ["Amennyivel tudatosabban építünk a természetre, annyival nagyobb lesz a tájreziliencia.", "Inasmuch as we build more consciously on nature, by so much greater will landscape resilience be."]
            ],
            "world_story_seg": {
                "seg_slug": "arteri",
                "title": "Vissza a természethez: az ártéri tájgazdálkodás reneszánsza",
                "summary": "Examining grassroots and ecological initiatives that breach selected dikes to flood low-lying depressions, storing millions of cubic meters of water to revive agriculture.",
                "paragraphs": [
                    {"type": "narration", "text": "A Tisza menti Fokorú-pusztán különös dolog történik tavaszi olvadáskor: ahelyett, hogy a mérnökök megerősítenék a töltéseket, megnyitják a zsilipeket. A folyó zavaros, éltető vize lassan szétterül a mélyfekvésű szántókon, feltölti a hajdani holtágakat, megitatja a réteket, és puha iszapot terít a termőföldre. Néhány hét elteltével a víz visszahúzódik a főmederbe, de a föld mélyében ott marad a nedvesség: a fű smaragdzölden sarjad, a madarak fészket raknak, és a talajvízszint méterekkel emelkedik."},
                    {"type": "narration", "text": "Ez az ártéri tájgazdálkodás újjászületése, amely szakít a folyókkal vívott évszázados háborúval. Az ökológusok rámutattak: minél nagyobb területeket adunk vissza a víznek az árvízi időszakban, annál nagyobb biztonságban vészelhetjük át a nyári hőséget. A vizes élőhelyek gigantikus természetes klímaberendezésként működnek: a párolgás hűti a forró levegőt, csökkenti a jégverést és táplálja a növényzetet. A jövő mezőgazdasága nem a gátak magasításában, hanem a vizek befogadásában rejlik."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Hogyan működnek a vizes élőhelyek 'természetes klímaberendezésként'?", [
                    "A tárolt víz folyamatos párologtatása hűti a környező levegőt és párásítja a mikroklímát az aszály idején.",
                    "Elektromos áramot termelnek a légkondicionálók működtetéséhez.",
                    "Megakadályozzák, hogy a Nap sugarai elérjék a Föld felszínét."
                ], 0, ["c1-vizgazdalkodas-vocab"]),
                fb("grammar", "controlled", "Minél több mélyfekvésű területet adunk vissza a víznek, _____ ellenállóbb lesz a táj az aszállyal szemben. (the more / annál)", "annál", "The more low-lying areas we return to water, the more resilient the landscape will be against drought.", ["c1-adv-proportional-climate-correlatives"]),
                match("vocabulary", "controlled", [["ártéri tájgazdálkodás", "a folyó természetes áradásaira építő gazdálkodási forma"], ["vízpuffer", "víztároló kapacitás a szélsőségek tompítására"], ["mikroklimatikus hűtés", "a párolgás hűsítő hatása a helyi hőmérsékletre"], ["tájreziliencia", "a táj képessége a klímasokkok kiheverésére"]], ["c1-vizgazdalkodas-vocab"]),
                fb("grammar", "practice", "_____ mélyebbre süllyed a talajvíz, annál költségesebb az öntözés fenntartása. (The more / Minél)", "Minél", "The deeper the groundwater sinks, the more costly it is to sustain irrigation.", ["c1-adv-proportional-climate-correlatives"]),
                sb("grammar", "practice", ["Minél", "több", "a", "víz,", "annál", "zöldebb", "marad", "a", "táj."], ["Minél", "több", "a", "víz,", "annál", "zöldebb", "marad", "a", "táj."], "The more the water, the greener the landscape remains.", ["c1-adv-proportional-climate-correlatives"]),
                dc("dialogue", [
                    {"speaker": "Agrárökológus", "text": "Megéri feláldozni néhány szántóföldet vizes élőhely céljára?"},
                    {"speaker": "Tájépítész", "text": "Minél bátrabban terjesztjük ki a vizes puffereket, _____ stabilabb lesz a térség terméshozama."},
                ], ["annál", "amint", "bár"], 0, ["c1-adv-proportional-climate-correlatives"]),
                sw("production", [{"prompt": "Write a proportional correlative sentence demonstrating the benefits of wetland restoration using 'Minél... annál...'.", "answer": "Minél hatékonyabban valósítjuk meg a vizek helyben tartását a tájban, annál kevésbé sújtják a nyári hőhullámok a mezőgazdasági termelést."}], ["c1-adv-proportional-climate-correlatives"]),
                mc("grammar", "check", "Melyik kötőszópár fejez ki funkcionális arányossági viszonyt két ökológiai tényező között?", [
                    "Minél... annál...",
                    "Vagy... vagy...",
                    "Ha... akkor..."
                ], 0, ["c1-adv-proportional-climate-correlatives"])
            ]
        },
        {
            "num": 4,
            "stem": f"c1-{slug}-04",
            "title": "Industrial Water Extraction, Battery Megafactories & Epistemic Uncertainty",
            "grammar_title": "Epistemic Modal Adverbials Expressing Calibrated Scientific Uncertainty in Climate Models",
            "grammar_skill": "c1-epistemic-ecological-uncertainty",
            "goals": [
                "I can analyze industrial water usage, battery gigafactories, and aquifer depletion (*akkumulátorgyárak, ipari vízkivétel, rétegvízkészlet-kimerülés*).",
                "I can employ calibrated epistemic modal adverbials expressing scientific uncertainty (*minden valószínűség szerint, előrejelzések alapján feltételezhetően, bizonytalan kimenetellel*).",
                "I can debate the democratic oversight of strategic groundwater resources vs. foreign direct investment priorities."
            ],
            "vocab": [
                {"lemma": "akkumulátorgyár", "translation": "battery gigafactory", "pos": "noun"},
                {"lemma": "ipari vízkivétel", "translation": "industrial water extraction", "pos": "expression"},
                {"lemma": "rétegvízkészlet", "translation": "confined aquifer / strata water reserve", "pos": "noun"},
                {"lemma": "karsztvízbázis", "translation": "karst water resource", "pos": "noun"},
                {"lemma": "monitoringrendszer", "translation": "monitoring system", "pos": "noun"},
                {"lemma": "szennyezési kockázat", "translation": "pollution / contamination risk", "pos": "expression"},
                {"lemma": "túlterhelt vízinfrastruktúra", "translation": "overburdened water infrastructure", "pos": "expression"},
                {"lemma": "társadalmi ellenállás", "translation": "social / public resistance", "pos": "expression"}
            ],
            "gr_text1": "In environmental risk assessment and hydrological modeling, epistemic modal adverbs calibrate the certainty of projections: `minden valószínűség szerint` (in all likelihood), `feltételezhetően` (presumably / hypothetically), `tudományos modellek alapján valószínűsíthető` (probable based on scientific models), `bizonytalan kimenetellel` (with uncertain outcome), `várhatóan` (expectedly).",
            "gr_text2": "Example: `A debreceni és gödi akkumulátorgyárak extrém vízigénye minden valószínűség szerint túlterheli a helyi vízbázist, előrejelzések alapján feltételezhetően kimerítve a mélységi rétegvizeket`.",
            "gr_table": [
                ["A gigaberuházások vízigénye minden valószínűség szerint felgyorsítja a talajvíz apadását.", "The water demand of gigaprojects in all likelihood accelerates the dwindling of groundwater."],
                ["A modellek alapján feltételezhetően drasztikus vízkorlátozásokra lesz szükség a lakosság körében.", "Based on models presumably drastic water restrictions will be needed among the population."],
                ["A vegyi anyagok karsztvízbe jutása beláthatatlan kimenetellel fenyegeti az egész régiót.", "The seepage of chemicals into karst water threatens the entire region with incalculable outcome."]
            ],
            "world_story_seg": {
                "seg_slug": "akkugyar",
                "title": "Akkumulátorgyárak a szomjazó pusztán: az ipar és a víz összecsapása",
                "summary": "Investigating the fierce national debate surrounding massive battery gigafactories in Debrecen, Göd, and Iváncsa, and their voracious thirst for precious underground aquifers.",
                "paragraphs": [
                    {"type": "narration", "text": "Debrecen határában hatalmas daruk és betonozó gépek százai dolgoznak a sárgára száradt hajdúsági síkságon: itt épül Európa egyik legnagyobb elektromos autóakkumulátor-gyára. A kormányzati kommunikáció az ipari jövőt, az elektromos mobilitás zöld forradalmát és a munkahelyek ezreit ünnepli. Ám a csillogó beruházási prezentációk mögött egyre sötétebb árnyék vetül a térségre: a gyár napi több tízezer köbméteres vízigénye."},
                    {"type": "narration", "text": "A helyi lakosság és a független vízügyi szakemberek riadót fújtak. Egy olyan régióban, ahol az aszály miatt a Nagyerdő fái sorvadoznak és a kutak vízszintje évről évre zuhan, a mélységi rétegvizek és a karsztvízkészletek ipari csapolása minden valószínűség szerint felmérhetetlen kockázatokkal jár. A civil szervezetek és az aggódó polgárok felteszik az alapkérdést: szabad-e egy klímaválsággal küzdő országnak a legdrágább kincsét, a jövő nemzedékek tiszta ivóvizét külföldi multinacionális cégek profitszerzésére áldoznia?"}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Mi a fő környezeti aggály az akkumulátorgyárak magyarországi telepítésével kapcsolatban?", [
                    "A hatalmas napi ipari vízfogyasztásuk és a mélységi vízbázisok elszennyeződésének kockázata a klímasérülékeny térségekben.",
                    "Hogy túl sok zajt csapnak a hétvégi focimeccsek alatt.",
                    "Hogy kizárólag kerékpárral lehet megközelíteni a gyárakat."
                ], 0, ["c1-vizgazdalkodas-vocab"]),
                fb("grammar", "controlled", "A hatalmas ipari vízkivétel minden _____ szerint kimeríti a védett rétegvízkészletet. (in all likelihood / valószínűség)", "valószínűség", "The enormous industrial water extraction in all likelihood depletes the protected strata water reserve.", ["c1-epistemic-ecological-uncertainty"]),
                match("vocabulary", "controlled", [["akkumulátorgyár", "elektromos energiatárolókat előállító gigantikus ipari üzem"], ["rétegvízkészlet", "a föld mélyén fekvő, lassan megújuló tiszta ivóvízbázis"], ["karsztvízbázis", "mészkőhegységek kiterjedt földalatti vízkincse"], ["monitoringrendszer", "a vízminőséget és vízszintet folyamatosan ellenőrző hálózat"]], ["c1-vizgazdalkodas-vocab"]),
                fb("grammar", "practice", "A klímamodellek alapján _____ elkerülhetetlen lesz a szigorú lakossági vízkorlátozás. (presumably / feltételezhetően)", "feltételezhetően", "Based on climate models presumably strict residential water rationing will be unavoidable.", ["c1-epistemic-ecological-uncertainty"]),
                sb("grammar", "practice", ["A", "túlzott", "vízkivétel", "bizonytalan", "kimenetellel", "fenyegeti", "a", "régiót."], ["A", "túlzott", "vízkivétel", "bizonytalan", "kimenetellel", "fenyegeti", "a", "régiót."], "Excessive water extraction threatens the region with uncertain outcome.", ["c1-epistemic-ecological-uncertainty"]),
                dc("dialogue", [
                    {"speaker": "Aggódó polgár", "text": "Biztonságban van a városunk ivóvize a gyárépítés után?"},
                    {"speaker": "Hidrogeológus", "text": "Minden valószínűség szerint a rétegvíz apadása _____ hatással lesz a kutak vízhozamára."},
                ], ["negatív", "vidám", "tökéletes"], 0, ["c1-epistemic-ecological-uncertainty"]),
                sw("production", [{"prompt": "Write a critical evaluative sentence on industrial water demand using 'minden valószínűség szerint'.", "answer": "A tervezett gigaberuházások drasztikus vízigénye minden valószínűség szerint felgyorsítja a karsztvízbázisok kimerülését, veszélyeztetve a lakosság egészséges ivóvízellátását."}], ["c1-epistemic-ecological-uncertainty"]),
                mc("grammar", "check", "Melyik határozószó fejez ki tudományos modellre alapozott episztemikus valószínűséget?", [
                    "minden valószínűség szerint / feltételezhetően",
                    "holnap délután kettőkor",
                    "hangosan kiabálva"
                ], 0, ["c1-epistemic-ecological-uncertainty"])
            ]
        },
        {
            "num": 5,
            "stem": f"c1-{slug}-05",
            "title": "Water Sovereignty, National Strategy & Conclusive Synthesis",
            "grammar_title": "Conclusive Discourse Particles Synthesizing Holistic Ecological Policy Proposals",
            "grammar_skill": "c1-adv-conclusive-environmental-synthesis",
            "goals": [
                "I can formulate a holistic national water strategy and defend water sovereignty (*vízszuverenitás, nemzeti vízvagyon, klímaadaptációs stratégia*).",
                "I can employ elevated conclusive discourse particles to synthesize complex environmental policies (*mindent összevetve, konklúzióként levonható, összegezve a fentieket*).",
                "I can debate the ethical obligations of intergenerational climate solidarity in the Carpathian Basin."
            ],
            "vocab": [
                {"lemma": "vízszuverenitás", "translation": "water sovereignty", "pos": "noun"},
                {"lemma": "nemzeti vízvagyon", "translation": "national water asset / wealth", "pos": "expression"},
                {"lemma": "klímaadaptációs stratégia", "translation": "climate adaptation strategy", "pos": "expression"},
                {"lemma": "generációk közötti szolidaritás", "translation": "intergenerational solidarity", "pos": "expression"},
                {"lemma": "holisztikus szemlélet", "translation": "holistic perspective", "pos": "expression"},
                {"lemma": "tájpolitikai fordulat", "translation": "landscape policy turning point / turnaround", "pos": "expression"},
                {"lemma": "társadalmi konszenzus", "translation": "social consensus", "pos": "expression"},
                {"lemma": "ökológiai jövőkép", "translation": "ecological vision of the future", "pos": "expression"}
            ],
            "gr_text1": "Conclusive synthesis particles summarize multidimensional ecological debates and articulate final policy mandates: `mindent összevetve` (all things considered / taking everything into account), `konklúzióként levonható` (as a conclusion it can be deduced), `összegezve a fentieket` (summarizing the above), `végső soron` (ultimately), `egybehangzóan megállapítható` (it can be congruently established).",
            "gr_text2": "Example: `Mindent összevetve, a vízszuverenitás megőrzése nem mérnöki részletkérdés, hanem a huszonegyedik századi magyar állam fennmaradásának legfőbb stratégiai záloga`.",
            "gr_table": [
                ["Mindent összevetve, a víz elvezetése helyett a vízmegtartásra kell áttérnünk.", "All things considered, instead of water drainage we must transition to water retention."],
                ["Konklúzióként levonható, hogy az édesvízkészlet védelme nemzetbiztonsági prioritás.", "As a conclusion it can be deduced that the protection of freshwater reserves is a national security priority."],
                ["Összegezve a fentieket, valódi tájpolitikai fordulatra van szükség a Kárpát-medencében.", "Summarizing the above, a genuine landscape policy turnaround is needed in the Carpathian Basin."]
            ],
            "world_story_seg": {
                "seg_slug": "vizszuverenitas",
                "title": "Vízszuverenitás: a huszonegyedik század legfontosabb nemzeti kérdése",
                "summary": "Synthesizing the lessons of drought, industrial extraction, and river regulation into a comprehensive vision of Hungarian water sovereignty and intergenerational responsibility.",
                "paragraphs": [
                    {"type": "narration", "text": "Amikor a huszonegyedik század geopolitikai és éghajlati kihívásaira tekintünk, egyetlen igazság ragyog fel félreérthetetlen tisztasággal: a víz a jövő aranya. Magyarország földrajzi fekvése különleges adottság és súlyos felelősség egyszerre: a Kárpát-medence alján fekvő országba a folyók bőségesen hozzák a vizet a környező hegyekből, ám a mai vízgazdálkodási reflexek miatt évente több víz folyik ki az országhatárokon, mint amennyi beérkezik. Szomjazó földeken engedjük át ujjaink között a legféltettebb nemzeti kincsünket."},
                    {"type": "narration", "text": "Mindent összevetve, a huszonegyedik században a vízszuverenitás az önrendelkezés és a nemzetbiztonság legfőbb alappillére. Nem engedhetjük meg, hogy a globális ipari tőke vagy a rövid távú politikai haszonszerzés felélje jövő generációink túlélési tartalékait. A gátak dogmáját felváltó tájreziliencia, a vizes élőhelyek kiterjesztése és a talajélet regenerálása nem csupán szakpolitikai reform, hanem a magyar haza iránti hűség legnemesebb próbája: megőrizni a tájat élhetőnek, zöldnek és éltetőnek mindazoknak, akik utánunk jönnek."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Mit jelent a 'vízszuverenitás' fogalma a 21. századi biztonságpolitikában?", [
                    "A nemzet jogát és stratégiai képességét arra, hogy saját ivóvízkészleteit és vizeit önállóan védje meg és a közösség javára gazdálkodjon vele.",
                    "A haditengerészet kizárólagos jogát a folyami hajózás ellenőrzésére.",
                    "Az ásványvíz-forgalmazó cégek adómentességét."
                ], 0, ["c1-vizgazdalkodas-vocab"]),
                fb("grammar", "controlled", "Mindent _____, a vizek helyben tartása a magyar jövő legfőbb záloga. (taking into account / összevetve)", "összevetve", "All things considered, retaining waters on site is the foremost pledge of the Hungarian future.", ["c1-adv-conclusive-environmental-synthesis"]),
                match("vocabulary", "controlled", [["vízszuverenitás", "az önálló és fenntartható nemzeti vízgazdálkodás joga"], ["klímaadaptáció", "a társadalom felkészülése az éghajlati szélsőségekre"], ["tájpolitikai fordulat", "radikális váltás a vízmegtartó természetes tájhasználat felé"], ["generációk közötti szolidaritás", "a természeti javak megőrzése a jövő nemzedékeknek"]], ["c1-vizgazdalkodas-vocab"]),
                fb("grammar", "practice", "Konklúzióként _____, hogy a jelenlegi vízelvezető gyakorlat fenntarthatatlan. (can be deduced / levonható)", "levonható", "As a conclusion it can be deduced that the current drainage practice is unsustainable.", ["c1-adv-conclusive-environmental-synthesis"]),
                sb("grammar", "practice", ["Mindent", "összevetve,", "a", "víz", "a", "nemzet", "legdrágább", "kincse."], ["Mindent", "összevetve,", "a", "víz", "a", "nemzet", "legdrágább", "kincse."], "All things considered, water is the nation's most precious treasure.", ["c1-adv-conclusive-environmental-synthesis"]),
                dc("dialogue", [
                    {"speaker": "Klímapolitikai szakértő", "text": "Hogyan foglalhatjuk össze a nemzeti vízstratégia lényegét?"},
                    {"speaker": "Ökológus", "text": "Mindent összevetve, a víz elvezetése helyett a vízmegtartást kell _____ tennünk."},
                ], ["prioritássá", "veszéllyé", "titokká"], 0, ["c1-adv-conclusive-environmental-synthesis"]),
                sw("production", [{"prompt": "Write a concluding policy synthesis on water conservation using 'Mindent összevetve'.", "answer": "Mindent összevetve, a Kárpát-medence ökológiai megmaradásának egyetlen záloga a holisztikus vízmegtartás és a természeti tőke feltétlen védelme a jövő nemzedékek számára."}], ["c1-adv-conclusive-environmental-synthesis"]),
                mc("grammar", "check", "Melyik kifejezés tölt be formális összefoglaló, konklúziót levonó szerepet az esszéírásban?", [
                    "Mindent összevetve / Konklúzióként levonható",
                    "Hirtelen felugorva",
                    "A szomszéd szobában"
                ], 0, ["c1-adv-conclusive-environmental-synthesis"])
            ]
        }
    ]

    for l in disc_lessons:
        emit_instructional_lesson(20, "discourse", l, disc_title, disc_intro if l["num"] == 1 else None)

    # Combined World Story
    write_json(
        ROOT / "content" / "hu" / "stories" / "world" / "c1" / f"c1-{slug}.json",
        {
            "id": f"story.c1.{slug}",
            "title": "A vizek országa szomjazik: küzdelem a Kárpát-medence kincséért",
            "level": "C1",
            "type": "world",
            "order": 20,
            "lesson": 5,
            "estimatedMinutes": 8,
            "summary": "Panoramic investigation of Hungary's water crisis: the rapid desiccation and semi-desertification of the Danube-Tisza sand ridge, historical river regulation dilemmas, modern floodplain water retention alternatives, the environmental clash over battery gigafactories, and the imperative for national water sovereignty.",
            "grammar": [
                "c1-discourse-ecological-threat-framing",
                "c1-modal-conservation-deontics",
                "c1-adv-proportional-climate-correlatives",
                "c1-epistemic-ecological-uncertainty",
                "c1-adv-conclusive-environmental-synthesis"
            ],
            "vocabularyTopics": [
                "Water Management, Drought Crises & Wetland Restoration",
                "The Drying Danube-Tisza Sand Ridge & Ecological Threat Framing",
                "The Tisza River Dilemma: Rapid Drainage vs. Water Retention",
                "Wetland Restoration, Floodplain Farming & Proportional Correlatives",
                "Industrial Water Extraction, Battery Megafactories & Epistemic Uncertainty",
                "Water Sovereignty, National Strategy & Conclusive Synthesis"
            ],
            "paragraphs": [
                {"type": "narration", "text": "Magyarország évszázadokon át a 'vizek országaként' élt a köztudatban: a Kárpátok bérceiről alázúduló folyamok, a Duna és a Tisza hatalmas áradásai, a Nagysárrét és a Hanság végtelen lápvilága mind a természet fékezhetetlen bőségét hirdették. Ám a huszonegyedik század hajnalára a kép drámaian megváltozott. A klímaváltozás, a kontinentális aszályok és a múltbeli téves vízrendezések együttesen olyan ökológiai válságot idéztek elő, amely alapjaiban fenyegeti az ország természeti és gazdasági stabilitását."},
                {"type": "narration", "text": "A válság legdrámaibb szimbóluma a Duna-Tisza közi Homokhátság félsivatagosodása, ahol a talajvíz vészes süllyedése miatt erdők és tanyák száradnak ki. Ezzel párhuzamosan a Tisza szabályozásának másfél évszázados dogmája is megkérdőjeleződött: a gátak közé szorított víz gyors elvezetése ahelyett, hogy védené az országot, nyaranta kiszárítja a szántókat. A felismerés egyre sürgetőbb: a vízlefolyás gyorsítása helyett a vizek tájban való megtartására és a vizes élőhelyek revitalizációjára van szükség."},
                {"type": "narration", "text": "A helyzetet tovább élezi a hazai iparpolitika, amely vízigényes akkumulátorgyárak százaival terheli meg a leginkább aszálysújtott régiók ivóvízbázisait. A gazdasági növekedés és a környezeti fenntarthatóság konfliktusa Debrecenben és Gödön éles társadalmi vitákhoz vezetett: a lakosság joggal követeli a mélységi rétegvizek és a karsztkincsek feltétlen törvényi védelmét a rövid távú profithajhászással szemben."},
                {"type": "narration", "text": "Mindent összevetve, a vízszuverenitás nem elvont szakmai fogalom, hanem a nemzet huszonegyedik századi megmaradásának legfőbb próbája. A tájba illeszkedő ártéri gazdálkodás, a vizek szétterítése és az intergenerációs szolidaritás az egyetlen járható út ahhoz, hogy a Kárpát-medence unokáink számára is virágzó, élhető és éltető otthon maradjon."}
            ]
        }
    )

    # Discourse Consolidation
    emit_consolidation_lesson(
        20,
        "discourse",
        f"c1-{slug}-consolidation",
        disc_title,
        [
            "I can analyze water management dilemmas, sand ridge desertification, and battery gigafactory water extraction.",
            "I can deploy statutory conservation mandates, systemic threat framing, and climate correlatives.",
            "I can debate national water sovereignty, floodplain retention, and intergenerational ecological ethics."
        ],
        [
            mc("grammar", "recognize", "Milyen szerkezettel fejezhetünk ki akut ökológiai fenyegetést és rendszerszintű kockázatot?", [
                "akut válsághelyzetet idéz elő / közvetlen fenyegetést jelent / végveszélybe sodor",
                "amikor szép napos délután van a Duna-parton",
                "mivel elolvasták az időjárás-jelentést az újságban"
            ], 0, ["c1-discourse-ecological-threat-framing"]),
            mc("grammar", "recognize", "Melyik kifejezés fejez ki kötelező érvényű törvényi védelmi imperatívuszt?", [
                "törvényi kötelessége megóvni / határozott tiltást szab",
                "szabadon dönthetnek a kirándulásról",
                "ha kedvük tartja, sétálnak a folyó mellett"
            ], 0, ["c1-modal-conservation-deontics"]),
            match("vocabulary", "recognize", [["homokhátság", "Duna-Tisza közi félsivatagosodó tájegység"], ["ártéri tájgazdálkodás", "áradásokra épülő vízmegtartó rendszer"], ["rétegvízkészlet", "védett mélységi tiszta ivóvízkincs"], ["vízszuverenitás", "az önálló nemzeti vízgazdálkodás joga"], ["mikroklimatikus hűtés", "vizes élőhelyek párolgás általi hűtő hatása"]], ["c1-vizgazdalkodas-vocab"]),
            fb("vocabulary", "recall", "A Duna és Tisza közötti _____ a klímaváltozás miatt félsivatagosodás fenyegeti. (sand ridge / homokhátságot)", "homokhátságot", "The sand ridge between Danube and Tisza is threatened by semi-desertification due to climate change.", ["c1-vizgazdalkodas-vocab"]),
            fb("vocabulary", "recall", "Az államnak elemi feladata a stratégiai nemzeti _____ védelme a kizsákmányolástól. (water asset / vízvagyon)", "vízvagyon", "The state's fundamental task is the protection of strategic national water asset from exploitation.", ["c1-vizgazdalkodas-vocab"]),
            fb("grammar", "recall", "A kormánynak törvényi _____ megóvni az ország ivóvízkészleteit. (duty / kötelessége)", "kötelessége", "The government has a statutory duty to preserve the country's drinking water reserves.", ["c1-modal-conservation-deontics"]),
            fb("grammar", "context", "Minél több vizet tartunk meg a tájban, _____ ellenállóbbak lesznek a mezőgazdasági termőföldek. (the more / annál)", "annál", "The more water we retain in the landscape, the more resilient agricultural soils will be.", ["c1-adv-proportional-climate-correlatives"]),
            fb("grammar", "context", "Mindent _____, a vízmegtartás a magyar táj jövőjének egyetlen záloga. (taking into account / összevetve)", "összevetve", "All things considered, water retention is the sole pledge of the Hungarian landscape's future.", ["c1-adv-conclusive-environmental-synthesis"]),
            mc("grammar", "context", "Mi a funkciója a 'Minél... annál...' arányossági szerkezetnek az ökológiai érvelésben?", [
                "Bemutatja a természetes beavatkozások egymást erősítő, pozitív kumulatív hatásait.",
                "Kijelenti, hogy semmit sem szabad csinálni a folyókkal.",
                "Elnézést kér az árvizek miatt."
            ], 0, ["c1-adv-proportional-climate-correlatives"]),
            sb("grammar", "produce", ["A", "víz", "a", "nemzet", "legféltettebb", "természeti", "kincse."], ["A", "víz", "a", "nemzet", "legféltettebb", "természeti", "kincse."], "Water is the nation's most cherished natural treasure.", ["c1-adv-conclusive-environmental-synthesis"]),
            sw("production", [{"prompt": "Write a critical diagnosis of Hungary's water management using an ecological threat framing marker.", "answer": "A felszíni vizek túlzott elvezetése és a mélységi rétegvizek ipari kizsákmányolása akut válsághelyzetet idéz elő, amely közvetlen fenyegetést jelent a Kárpát-medence ivóvízbázisára."}], ["c1-discourse-ecological-threat-framing"]),
            sw("production", [{"prompt": "Formulate a concluding thought on water sovereignty and future generations.", "answer": "Mindent összevetve, a vízszuverenitás feltétlen védelme és a természetes vizes élőhelyek helyreállítása az egyetlen felelős válasz a huszonegyedik század éghajlati kihívásaira."}], ["c1-adv-conclusive-environmental-synthesis"])
        ]
    )

    print("=== Finished C1 Unit 20 ===")


if __name__ == "__main__":
    generate_unit_20()
