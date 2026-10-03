#!/usr/bin/env python3
"""
Hungarian C1 Block 5 - Unit 30 Generator:
  - Track 1 (Core): Unit 30 — "Geopolitics, East vs. West & The Carpathian Basin Horizon" (c1-30)
  - Track 2 (Discourse): Unit 30 — "Pendulum Politics, Strategic Neutrality & Euro-Atlantic Crisis" (c1-geopolitika)
"""

import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT))

from scripts.c1_block1.common import mc, match, fb, sb, dc, sw, write_json, emit_instructional_lesson, emit_consolidation_lesson
from scripts.c1_block5.registry_helper import register_unit


def generate_unit_30():
    print("=== Generating C1 Unit 30 ===")
    
    new_skills = {
        "c1-30-vocab": {"kind": "vocabulary"},
        "c1-geopolitika-vocab": {"kind": "vocabulary"},
        "c1-adv-geopolitical-determinism-buffer": {"kind": "grammar"},
        "c1-participle-historical-region-divergence": {"kind": "grammar"},
        "c1-adv-counter-isolation-adversatives": {"kind": "grammar"},
        "c1-modal-teleological-alliance-commitments": {"kind": "grammar"},
        "c1-adv-scalar-ferry-country-destiny": {"kind": "grammar"},
        "c1-discourse-pendulum-politics-framing": {"kind": "grammar"},
        "c1-modal-deontic-energy-security": {"kind": "grammar"},
        "c1-adv-proportional-veto-diplomacy": {"kind": "grammar"},
        "c1-epistemic-debt-trap-exposure": {"kind": "grammar"},
        "c1-adv-conclusive-european-destiny-synthesis": {"kind": "grammar"},
    }
    new_titles = {
        "c1-30-vocab": "reading",
        "c1-geopolitika-vocab": "reading",
        "c1-adv-geopolitical-determinism-buffer": "geopolitical determinist adverbials analyzing regional buffer zones and spatial constraints",
        "c1-participle-historical-region-divergence": "complex participial structures detailing structural divergence across historical european regions",
        "c1-adv-counter-isolation-adversatives": "adversative connectors contrasting shared european integration with sovereign isolation illusions",
        "c1-modal-teleological-alliance-commitments": "teleological modal structures framing collective defense responsibilities and alliance loyalty",
        "c1-adv-scalar-ferry-country-destiny": "scalar evaluative adverbials calibrating visionary prophetic diagnoses of national fate",
        "c1-discourse-pendulum-politics-framing": "discourse framing markers diagnosing tactical pendulum politics and connectivity doctrines",
        "c1-modal-deontic-energy-security": "deontic modal structures asserting national diversification duties against autocratic energy blackmail",
        "c1-adv-proportional-veto-diplomacy": "proportional correlative conjunctions mapping veto extortion against escalating international isolation",
        "c1-epistemic-debt-trap-exposure": "epistemic stance markers assessing autocratic debt trap risks and sovereignty erosion",
        "c1-adv-conclusive-european-destiny-synthesis": "evaluative synthesis particles formulating definitive manifestos for western integration and democracy",
    }
    
    core_title = "Geopolitics, East vs. West & The Carpathian Basin Horizon"
    core_stems = [f"c1-30-0{i}" for i in range(1, 6)] + ["c1-30-consolidation"]
    disc_title = "Pendulum Politics, Strategic Neutrality & Euro-Atlantic Crisis"
    slug = "geopolitika"
    disc_stems = [f"c1-{slug}-0{i}" for i in range(1, 6)] + [f"c1-{slug}-consolidation"]
    
    register_unit(30, core_title, core_stems, disc_title, disc_stems, new_skills, new_titles)

    # ----------------------------------------------------
    # TRACK 1: CORE (c1-30)
    # ----------------------------------------------------
    core_intro = [
        "Situated at the crossroads of European civilizations, the Carpathian Basin has historically oscillated between Eastern steppe empires and Western institutional statehood. From medieval borderland defenses to Jenő Szűcs's structural analysis of Europe's three historical regions, navigating this geopolitical tension demands profound historical clarity.",
        "In this capstone unit of Block 5, centered on Ady Endre's visionary essay 'Komp-ország' (Ferry-Country), you will master the elevated academic register of geopolitical determinism, civilizational fault lines, shared supranational sovereignty, collective security, and national historical destiny at the C1 level."
    ]

    core_lessons = [
        {
            "num": 1,
            "stem": "c1-30-01",
            "title": "Geopolitical Determinist Adverbials & Buffer Zones",
            "grammar_title": "Geopolitical Determinist Adverbials Analyzing Regional Buffer Zones and Spatial Constraints",
            "grammar_skill": "c1-adv-geopolitical-determinism-buffer",
            "goals": [
                "I can analyze geopolitical buffer zones, spheres of influence, and spatial constraints (*ütközőzóna, érdekszféra, földrajzi determinizmus, külpolitikai mozgástér*).",
                "I can deploy elevated geopolitical adverbials evaluating regional balance (*geopolitikailag determinált módon, stratégiailag sérülékenyen, hatalmi szempontból ütközőzónaként viselkedve*).",
                "I can critique small-state survival strategies in international relations register."
            ],
            "vocab": [
                {"lemma": "geopolitika", "translation": "geopolitics", "pos": "noun"},
                {"lemma": "ütközőzóna", "translation": "buffer zone / cordon sanitaire", "pos": "noun"},
                {"lemma": "érdekszféra", "translation": "sphere of influence", "pos": "noun"},
                {"lemma": "külpolitikai mozgástér", "translation": "foreign policy room for maneuver", "pos": "expression"},
                {"lemma": "földrajzi determinizmus", "translation": "geographical determinism", "pos": "expression"},
                {"lemma": "hatalompolitika", "translation": "power politics / Realpolitik", "pos": "noun"},
                {"lemma": "törésvonal", "translation": "civilizational fault line", "pos": "noun"},
                {"lemma": "egyensúlypolitika", "translation": "balance of power politics", "pos": "noun"}
            ],
            "gr_text1": "Geopolitical determinist adverbials formulate rigorous analyses of spatial and structural power dynamics: `geopolitikailag determinált módon` (in a geopolitically determined manner), `stratégiailag sérülékenyen` (strategically vulnerably), `hatalmi szempontból ütközőzónaként elhelyezkedve` (situated as a buffer zone from a power perspective), `történetföldrajzilag kódoltan` (historico-geographically encoded).",
            "gr_text2": "Example: `A Kárpát-medence államai geopolitikailag determinált módon, nagyhatalmi érdekszférák metszéspontjában kénytelenek alakítani külpolitikájukat`.",
            "gr_table": [
                ["Az ország geopolitikailag determinált módon ütközőzónává vált a két birodalom között.", "The country in a geopolitically determined manner became a buffer zone between the two empires."],
                ["A kisállamok stratégiailag sérülékenyen manővereznek a nagyhatalmak árnyékában.", "Small states maneuver strategically vulnerably in the shadow of great powers."],
                ["A határok védelme történetföldrajzilag kódoltan alapozza meg a nemzetbiztonságot.", "Defense of borders historico-geographically encoded establishes national security."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mit jelent az 'ütközőzóna' fogalma a klasszikus geopolitikában?", [
                    "Két egymással rivalizáló nagyhatalom vagy szövetségi tömb közé ékelődő térséget, amely elválasztja a feleket és tompítja a közvetlen összeütközés kockázatát.",
                    "A repülőterek kifutópályája melletti füves területet.",
                    "A határállomásokon működő vámmentes boltok sorát."
                ], 0, ["c1-30-vocab"]),
                fb("grammar", "controlled", "A térség államai geopolitikailag _____ módon váltak nagyhatalmi konfliktusok színterévé. (determined / determinált)", "determinált", "States of the region in a geopolitically determined manner became the scenes of great power conflicts.", ["c1-adv-geopolitical-determinism-buffer"]),
                match("vocabulary", "controlled", [["ütközőzóna", "nagyhatalmakat elválasztó közbenső térség"], ["érdekszféra", "egy domináns birodalom befolyása alatti terület"], ["külpolitikai mozgástér", "egy állam cselekvési szabadságának keretei"], ["törésvonal", "civilizációk és világrendek találkozási sávja"]], ["c1-30-vocab"]),
                fb("grammar", "practice", "A Duna-medence stratégiailag _____ helyzetben volt a hidegháborús évtizedekben. (vulnerably / sérülékenyen)", "sérülékenyen", "The Danube basin was in a strategically vulnerable position during cold war decades.", ["c1-adv-geopolitical-determinism-buffer"]),
                sb("grammar", "practice", ["A", "Kárpát-medence", "geopolitikailag", "determinált", "módon", "ütközőzónaként", "létezett."], ["A", "Kárpát-medence", "geopolitikailag", "determinált", "módon", "ütközőzónaként", "létezett."], "The Carpathian Basin in a geopolitically determined manner existed as a buffer zone.", ["c1-adv-geopolitical-determinism-buffer"]),
                dc("dialogue", [
                    {"speaker": "Diplomata", "text": "Hogyan tarthatja fenn a szuverenitását egy közép-európai kisállam?"},
                    {"speaker": "Biztonságpolitikus", "text": "Csakis úgy, ha felismeri: geopolitikailag _____ módon szövetségesek nélkül menthetetlenül kiszolgáltatottá válik."},
                    {"speaker": "Diplomata", "text": "Ezért elengedhetetlen a megbízható integráció."}
                ], ["determinált", "véletlen", "lassú"], 0, ["c1-adv-geopolitical-determinism-buffer"]),
                sw("production", [{"prompt": "Write a sentence analyzing geopolitical buffer zones using a determinist adverbial.", "answer": "A Kárpát-medence népei geopolitikailag determinált módon, keleti és nyugati birodalmi törekvések ütközőzónájában küzdöttek megmaradásukért az évszázadok viharaiban."}], ["c1-adv-geopolitical-determinism-buffer"]),
                mc("grammar", "check", "Melyik határozó fejezi ki a geopolitikai kényszereket a legmagasabb elméleti regiszterben?", [
                    "geopolitikailag determinált módon / stratégiailag sérülékenyen",
                    "meglehetősen kellemetlen helyen lakva",
                    "térképre nézve szomorúan"
                ], 0, ["c1-adv-geopolitical-determinism-buffer"])
            ]
        },
        {
            "num": 2,
            "stem": "c1-30-02",
            "title": "Szűcs Jenő: The Three Historical Regions of Europe",
            "grammar_title": "Complex Participial Structures Detailing Structural Divergence Across Historical European Regions",
            "grammar_skill": "c1-participle-historical-region-divergence",
            "goals": [
                "I can analyze Jenő Szűcs's seminal thesis on Western Europe, Eastern Europe, and Central-Eastern Europe (*történeti régiók, szerződéses szabadságok, joguralom, második jobbágyság*).",
                "I can construct complex participial structures detailing institutional divergence (*a nyugati jogállamiságot meghonosító, az állami omnipotenciát elutasító, a feudális szabadságjogokat kiharcoló*).",
                "I can critique long-term structural path dependencies in economic history."
            ],
            "vocab": [
                {"lemma": "történeti régió", "translation": "historical region (Szűcs Jenő typology)", "pos": "expression"},
                {"lemma": "joguralom", "translation": "rule of law / supremacy of legal contract", "pos": "noun"},
                {"lemma": "szerződéses szabadság", "translation": "contractual liberty / feudal compact", "pos": "expression"},
                {"lemma": "második jobbágyság", "translation": "second serfdom (early modern enserfment)", "pos": "expression"},
                {"lemma": "állami túlsúly", "translation": "state preponderance / overarching autocracy", "pos": "expression"},
                {"lemma": "útfüggőség", "translation": "path dependency / historical lock-in", "pos": "noun"},
                {"lemma": "társadalmi autonómia", "translation": "societal / municipal autonomy", "pos": "expression"},
                {"lemma": "szerkezeti megrekedés", "translation": "structural stagnation / arrested development", "pos": "expression"}
            ],
            "gr_text1": "Complex participial structures specify the contrasting evolutionary paths of European societies: `a társadalmat a szerződéses szabadságjogok talaján megszervező nyugati modell` (Western model organizing society on the ground of contractual liberties), `az állam omnipotenciáját abszolutizáló és az autonómiákat felszámoló keleti fejlődés` (Eastern development absolutizing state omnipotence and liquidating autonomies), `a két világ között ingadozó és szerkezetileg megrekedt közép-kelet-európai térség` (East-Central European region oscillating between two worlds and structurally stagnating).",
            "gr_text2": "Example: `Szűcs Jenő a polgári autonómiákat és a joguralmat meghonosító nyugati struktúrákkal állította szembe a despota államhatalmat`.",
            "gr_table": [
                ["A városi autonómiákat biztosító jogrend a nyugati polgárosodás alapja.", "The legal order securing municipal autonomies is the basis of Western embourgeoisement."],
                ["Az állam korlátlan túlsúlyát érvényesítő rendszerek elnyomták a társadalmat.", "Systems enforcing the state's unconstrained preponderance suppressed society."],
                ["A nyugati mintákat átvevő, ám szerkezetileg megrekedt régió sajátos utat járt be.", "The region adopting Western models yet structurally stagnating traversed a distinct path."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mi Szűcs Jenő alapvető tézise Európa három történeti régiójáról?", [
                    "Hogy Közép-Kelet-Európa nem puszta földrajzi fogalom, hanem olyan sajátos történeti régió, amely a nyugati jogi struktúrákhoz kapcsolódott, de a társadalmi autonómiák hiánya miatt megrekedt.",
                    "Hogy Európát három folyó osztja fel egyenlő mezőgazdasági parcellákra.",
                    "Hogy a kontinensen csak a svájci óragyártás számít fejlett iparnak."
                ], 0, ["c1-30-vocab"]),
                fb("grammar", "controlled", "A joguralmat és szerződéses szabadságokat _____ intézmények jelentették a Nyugat erejét. (establishing / meghonosító)", "meghonosító", "Institutions establishing the rule of law and contractual liberties constituted the West's strength.", ["c1-participle-historical-region-divergence"]),
                match("vocabulary", "controlled", [["joguralom", "a hatalmat korlátozó jogrendszer supremacy-je"], ["szerződéses szabadság", "a társadalom és az állam közötti jogi kötelék"], ["második jobbágyság", "a kora újkori agrár-alávetettség visszatérése"], ["állami túlsúly", "a civil társadalom feletti autoriter állami hegemónia"]], ["c1-30-vocab"]),
                fb("grammar", "practice", "Az állami omnipotenciát elutasító és a polgári önkormányzatokat _____ modell virágzást hozott. (protecting / védelmező)", "védelmező", "The model rejecting state omnipotence and protecting civic self-governments brought prosperity.", ["c1-participle-historical-region-divergence"]),
                sb("grammar", "practice", ["A", "joguralmat", "meghonosító", "rendszer", "óvja", "a", "polgári", "szabadságot."], ["A", "joguralmat", "meghonosító", "rendszer", "óvja", "a", "polgári", "szabadságot."], "The system establishing the rule of law protects civil liberty.", ["c1-participle-historical-region-divergence"]),
                dc("dialogue", [
                    {"speaker": "Történész", "text": "Miért tért el Magyarország fejlődése a nyugat-európai államokétól a kora újkorban?"},
                    {"speaker": "Szociológus", "text": "Mert a városi polgárságot és autonómiákat hatékonyan _____ polgárosodás helyett a második jobbágyság konzerválódott."},
                    {"speaker": "Történész", "text": "Ez a szerkezeti megrekedés évszázadokra meghatározta az intézményrendszert."}
                ], ["erősítő", "bontó", "tagadó"], 0, ["c1-participle-historical-region-divergence"]),
                sw("production", [{"prompt": "Write a sentence detailing historical divergence using a complex participial structure.", "answer": "A szerződéses szabadságjogokat és a joguralmat meghonosító nyugati struktúrákkal szemben a cári mintákat követő keleti modell az állam korlátlan túlsúlyát intézményesítette."}], ["c1-participle-historical-region-divergence"]),
                mc("grammar", "check", "Melyik szerkezet fejezi ki a történelmi struktúrák szétválását a legpontosabban?", [
                    "a társadalmi autonómiákat és a joguralmat meghonosító nyugati modell",
                    "a piacon kenyeret vásárló emberek",
                    "egy szép régi vár a hegytetőn"
                ], 0, ["c1-participle-historical-region-divergence"])
            ]
        },
        {
            "num": 3,
            "stem": "c1-30-03",
            "title": "Shared Supranational Integration vs. Isolation Illusions",
            "grammar_title": "Adversative Connectors Contrasting Shared European Integration with Sovereign Isolation Illusions",
            "grammar_skill": "c1-adv-counter-isolation-adversatives",
            "goals": [
                "I can analyze shared supranational sovereignty, European federalism, and the illusion of autarkic isolation (*megosztott szuverenitás, szupranacionális döntéshozatal, szubszidiaritás, autarkia*).",
                "I can deploy elevated adversative connectors contrasting integration with isolated vulnerability (*a dacos nemzetállami elszigetelődéssel szemben a valóságban, nemhogy nem csorbítja a szuverenitást a közös döntéshozatal, hanem éppen megsokszorozza a cselekvőképességet, mindazonáltal a magányos dac geopolitikai öngyilkosság*).",
                "I can critique sovereignist populist rhetoric in European law register."
            ],
            "vocab": [
                {"lemma": "megosztott szuverenitás", "translation": "shared / pooled sovereignty", "pos": "expression"},
                {"lemma": "szupranacionális intézmény", "translation": "supranational institution", "pos": "expression"},
                {"lemma": "szubszidiaritás", "translation": "subsidiarity", "pos": "noun"},
                {"lemma": "hatáskörátruházás", "translation": "conferral / transfer of competencies", "pos": "noun"},
                {"lemma": "nemzeti önrendelkezés", "translation": "national self-determination", "pos": "expression"},
                {"lemma": "autarkia", "translation": "autarky / economic self-sufficiency", "pos": "noun"},
                {"lemma": "elszigetelődés", "translation": "diplomatic isolation", "pos": "noun"},
                {"lemma": "kölcsönös függés", "translation": "interdependence", "pos": "expression"}
            ],
            "gr_text1": "Adversative connectors contrast the strength of shared European integration with the catastrophic vulnerabilities of isolated sovereignty: `a bezárkózó, nacionalista illúziókkal szemben a valóságban a közös piac` (in contrast with inward-looking nationalist illusions in reality the single market), `nemhogy nem csökkenti a nemzet súlyát az uniós integráció, hanem éppen globális védőhálót biztosít` (far from EU integration reducing the nation's weight, but rather secures a global safety net), `mindazonáltal az egyedül maradás kiszolgáltatottságot eredményez` (nevertheless remaining alone results in defenselessness).",
            "gr_text2": "Example: `A szuverenitást féltő dacos elszigetelődéssel szemben a valóságban a megosztott szuverenitás nemhogy nem gyengíti, hanem éppen felerősíti a magyar érdekérvényesítést a világban`.",
            "gr_table": [
                ["A dacos elszigetelődéssel szemben a valóságban a megosztott szuverenitás valódi erőt ad.", "In contrast with defiant isolation in reality pooled sovereignty grants genuine strength."],
                ["Az unió nemhogy nem birodalmi elnyomás, hanem éppen demokratikus szerződéses közösség.", "The union is far from imperial oppression; on the contrary, it is a democratic contractual community."],
                ["A magányos különút mindazonáltal elkerülhetetlen perifériára szoruláshoz vezet.", "The lonely separate path nevertheless leads to inevitable marginalization."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mit jelent a 'megosztott szuverenitás' (pooled sovereignty) az Európai Unióban?", [
                    "Azt, hogy a tagállamok bizonyos hatásköröket önkéntesen, közös demokratikus intézmények révén gyakorolnak, így sokkal hatékonyabban védik érdekeiket a globális térben.",
                    "Azt, hogy minden tagállam köteles megváltoztatni az államformáját.",
                    "A nemzeti himnuszok betiltását."
                ], 0, ["c1-30-vocab"]),
                fb("grammar", "controlled", "A szuverenitási szólamokkal szemben a valóságban a teljes bezárkózás gazdasági _____ vezet. (vulnerability / kiszolgáltatottsághoz)", "kiszolgáltatottsághoz", "In contrast with sovereignist slogans in reality complete closing leads to economic vulnerability.", ["c1-adv-counter-isolation-adversatives"]),
                match("vocabulary", "controlled", [["megosztott szuverenitás", "hatáskörök közös gyakorlása a hatékony cselekvésért"], ["szupranacionális intézmény", "nemzetek feletti döntéshozó fórum"], ["szubszidiaritás", "a döntések polgárokhoz legközelebbi meghozatalának elve"], ["kölcsönös függés", "államok egymásra utaltsága a modern gazdaságban"]], ["c1-30-vocab"]),
                fb("grammar", "practice", "Az integráció nemhogy nem gyengíti a nemzetet, _____ éppen megvédi a nagyhatalmi zsarolástól. (rather / hanem)", "hanem", "Integration is far from weakening the nation; on the contrary, it protects it from great power blackmail.", ["c1-adv-counter-isolation-adversatives"]),
                sb("grammar", "practice", ["A", "megosztott", "szuverenitás", "valódi", "cselekvőképességet", "biztosít", "a", "világban."], ["A", "megosztott", "szuverenitás", "valódi", "cselekvőképességet", "biztosít", "a", "világban."], "Pooled sovereignty secures genuine capacity to act in the world.", ["c1-adv-counter-isolation-adversatives"]),
                dc("dialogue", [
                    {"speaker": "Politológus", "text": "Megőrizhető-e az abszolút nemzetállami szuverenitás a globális pénzpiacok korában?"},
                    {"speaker": "Európa-jogász", "text": "Nem, mert a bezárkózó nacionalizmussal szemben a valóságban a közös intézmények _____ erőt jelentenek."},
                    {"speaker": "Politológus", "text": "Aki egyedül marad, az a keleti autokráciák martalékává válik."}
                ], ["többszörös", "semmilyen", "káros"], 0, ["c1-adv-counter-isolation-adversatives"]),
                sw("production", [{"prompt": "Write a critique of sovereignist isolation using an adversative connector.", "answer": "A dacos elszigetelődéssel szemben a valóságban a megosztott szuverenitás és a közös európai intézményrendszer nemhogy nem veszélyezteti a nemzeti létet, hanem a globális versenyképesség egyetlen garanciája."}], ["c1-adv-counter-isolation-adversatives"]),
                mc("grammar", "check", "Melyik ellentétes szerkezet bizonyítja a szuverenitás megosztásának szükségességét a legvilágosabban?", [
                    "az elszigetelődéssel szemben a valóságban... nemhogy nem gyengít, hanem éppen megsokszorozza a cselekvőképességet",
                    "ha kimegyünk a térre, fúj a szél",
                    "jó dolog az önállóság hétvégén"
                ], 0, ["c1-adv-counter-isolation-adversatives"])
            ]
        },
        {
            "num": 4,
            "stem": "c1-30-04",
            "title": "Collective Defense, NATO & Alliance Commitments",
            "grammar_title": "Teleological Modal Structures Framing Collective Defense Responsibilities and Alliance Loyalty",
            "grammar_skill": "c1-modal-teleological-alliance-commitments",
            "goals": [
                "I can analyze NATO Article 5 collective defense, deterrence, and alliance loyalty in wartime (*kollektív védelem, elrettentés, szövetségi hűség, 5. cikkely*).",
                "I can deploy teleological modal structures expressing alliance obligations (*avégből kell hűségesnek lenni a transzatlanti szövetséghez, hogy az ország ne váljon katonai agresszió áldozatává, abból a célból fejlesztik a védelmi képességeket, hogy elrettentsék az expanziót*).",
                "I can critique unreliable ally posture in international security studies."
            ],
            "vocab": [
                {"lemma": "kollektív védelem", "translation": "collective defense (NATO Article 5)", "pos": "expression"},
                {"lemma": "szövetségi hűség", "translation": "alliance loyalty / pact fidelity", "pos": "expression"},
                {"lemma": "elrettentés", "translation": "deterrence / strategic dissuasion", "pos": "noun"},
                {"lemma": "transzatlanti szövetség", "translation": "transatlantic alliance", "pos": "expression"},
                {"lemma": "stratégiai elköteleződés", "translation": "strategic commitment", "pos": "expression"},
                {"lemma": "biztonsági garancia", "translation": "security guarantee", "pos": "expression"},
                {"lemma": "bizalomvesztés", "translation": "loss of mutual trust", "pos": "noun"},
                {"lemma": "geopolitikai vákuum", "translation": "geopolitical vacuum", "pos": "expression"}
            ],
            "gr_text1": "Teleological modal structures formulate vital strategic purposes underlying mutual security compacts: `avégből kell fenntartani a szövetségi hűséget, hogy az ország elkerülje a biztonsági vákuum veszélyét` (alliance loyalty must be maintained to the end that the country avoid the danger of a security vacuum), `abból a célból áll fenn a kollektív védelem, hogy egyetlen tagállam se legyen kiszolgáltatva a katonai agressziónak` (collective defense exists with the goal that no single member state be exposed to military aggression), `azért szükséges a szavahihetőség, nehogy megkérdőjeleződjön az 5. cikkely érvényessége` (credibility is necessary lest the validity of Article 5 be questioned).",
            "gr_text2": "Example: `A kisállamoknak abból a célból kell szigorúan betartaniuk szövetségi kötelezettségeiket, hogy egy krízis idején számíthassanak a NATO elrettentő erejére`.",
            "gr_table": [
                ["Avégből kell ápolni a transzatlanti partnerséget, hogy szavatoljuk a békét.", "The transatlantic partnership must be nurtured to the end that we guarantee peace."],
                ["Abból a célból létezik a NATO, hogy elrettentse a birodalmi agressziót.", "NATO exists with the goal of deterring imperial aggression."],
                ["Azért kell megbízható szövetségesnek lenni, hogy krízisben se maradjunk magunkra.", "One must be a reliable ally so that in a crisis we do not remain alone."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mi képezi az Észak-atlanti Szerződés 5. cikkelyének lényegét?", [
                    "A kollektív védelem elvét, miszerint bármely tagállam elleni fegyveres támadás az egész szövetség elleni támadásnak minősül, és közös katonai fellépést von maga után.",
                    "A közös katonazenekarok fellépési rendjét a nemzeti ünnepeken.",
                    "A repülőjegyek árának csökkentését a katonák családtagjai számára."
                ], 0, ["c1-30-vocab"]),
                fb("grammar", "controlled", "A védelmi képességeket abból a _____ modernizálják, hogy hatékonyan elrettentsék a támadókat. (goal / célból)", "célból", "Defense capabilities are modernized with the goal of effectively deterring attackers.", ["c1-modal-teleological-alliance-commitments"]),
                match("vocabulary", "controlled", [["kollektív védelem", "egy mindenkiért, mindenki egyért elv a védelemben"], ["elrettentés", "a támadás kockázatainak elviselhetetlenné tétele"], ["szövetségi hűség", "a közös szerződések és értékek megbízható tisztelete"], ["biztonsági garancia", "a katonai szövetségesek által nyújtott védelem"]], ["c1-30-vocab"]),
                fb("grammar", "practice", "Avégből kell betartani a kötelezettségeket, _____ a szövetségesek bizalma megmaradjon. (that / hogy)", "hogy", "Obligations must be respected to the end that allies' trust remain.", ["c1-modal-teleological-alliance-commitments"]),
                sb("grammar", "practice", ["A", "kollektív", "védelem", "a", "biztonság", "legfőbb", "alapköve."], ["A", "kollektív", "védelem", "a", "biztonság", "legfőbb", "alapköve."], "Collective defense is the primary cornerstone of security.", ["c1-modal-teleological-alliance-commitments"]),
                dc("dialogue", [
                    {"speaker": "Katonai attasé", "text": "Megengedheti-e magának egy határállam a szövetségesi megbízhatóság relativizálását?"},
                    {"speaker": "Biztonsági szakértő", "text": "Sohasem, hiszen abból a célból tartozunk a NATO-hoz, _____ elkerüljük az ütközőzónák sorsát."},
                    {"speaker": "Katonai attasé", "text": "A hűtlenség katasztrófát hoz a kis népekre."}
                ], ["hogy", "mert", "ha"], 0, ["c1-modal-teleological-alliance-commitments"]),
                sw("production", [{"prompt": "Write a sentence formulating alliance commitments using a teleological modal structure.", "answer": "Magyarországnak avégből kell hűséges és megbízható NATO-szövetségesnek maradnia, hogy a háborús válságok korában szilárdan élvezze a kollektív védelem sérthetetlen garanciáit."}], ["c1-modal-teleological-alliance-commitments"]),
                mc("grammar", "check", "Melyik szerkezet fogalmazza meg a szövetségi hűség célját a legpontosabban?", [
                    "avégből kell fenntartani a szövetségi hűséget, hogy megőrizzük a kollektív védelmet",
                    "jó lenne ha nem lőnének ránk a szomszédok",
                    "szép dolog a katonai egyenruha"
                ], 0, ["c1-modal-teleological-alliance-commitments"])
            ]
        },
        {
            "num": 5,
            "stem": "c1-30-05",
            "title": "Ady Endre: Ferry-Country & National Destiny",
            "grammar_title": "Scalar Evaluative Adverbials Calibrating Visionary Prophetic Diagnoses of National Fate",
            "grammar_skill": "c1-adv-scalar-ferry-country-destiny",
            "goals": [
                "I can analyze Ady Endre's prophetic journalism, the 'Komp-ország' allegory, and the dialectic of Eastern morass vs. Western light (*Komp-ország, keleti láp, nemzeti öntetszelgés, profetikus látnok*).",
                "I can deploy scalar evaluative adverbials calibrating prophetic diagnoses of national fate (*látnoki erővel felbecsülhetetlen mértékben, a nemzeti illúziókat alapjaiban szétzúzva, profetikusan ostorozva a maradiságot*).",
                "I can synthesize Ady's cultural manifesto for 21st-century European Hungary."
            ],
            "vocab": [
                {"lemma": "Komp-ország", "translation": "Ferry-Country (allegory of Hungary drifting between East and West)", "pos": "expression"},
                {"lemma": "keleti láp", "translation": "Eastern morass / Asiatic slough", "pos": "expression"},
                {"lemma": "maradiság", "translation": "reactionary backwardness / obscurantism", "pos": "noun"},
                {"lemma": "nemzeti öntetszelgés", "translation": "national self-complacency / chauvinist conceit", "pos": "expression"},
                {"lemma": "látnok", "translation": "visionary / prophet", "pos": "noun"},
                {"lemma": "nyugati műveltség", "translation": "Western civilization / culture", "pos": "expression"},
                {"lemma": "ostoroz", "translation": "scourge / lash out against moral failings", "pos": "verb"},
                {"lemma": "megbékélés", "translation": "historic reconciliation", "pos": "noun"}
            ],
            "gr_text1": "Scalar evaluative adverbials calibrate the devastating depth and historical impact of prophetic cultural diagnoses: `látnoki erővel felbecsülhetetlen mértékben` (to an inestimable degree with visionary power), `a nemzeti önáltatást alapjaiban szétzúzva` (fundamentally smashing national self-delusion), `profetikusan ostorozva a feudális maradiságot` (prophetically scourging feudal backwardness), `a történelmi felelősséget kíméletlenül felmutatva` (uncompromisingly demonstrating historical responsibility).",
            "gr_text2": "Example: `Ady Endre látnoki erővel felbecsülhetetlen mértékben leplezte le a nemzeti illúziókat, figyelmeztetve Komp-országot a nyugati part eloldásának végzetes veszélyére`.",
            "gr_table": [
                ["Ady látnoki erővel felbecsülhetetlen mértékben diagnosztizálta a magyar sorsot.", "Ady to an inestimable degree with visionary power diagnosed Hungarian destiny."],
                ["A költő a nemzeti illúziókat alapjaiban szétzúzva követelte a polgári haladást.", "Fundamentally smashing national illusions the poet demanded civic progress."],
                ["Profetikusan ostorozva a gőgöt mutatta fel a Nyugathoz való tartozás imperatívuszát.", "Prophetically scourging arrogance he showed the imperative of belonging to the West."]
            ],
            "classic_story": {
                "slug": "ady-komp-orszag",
                "title": "Ady Endre: Komp-ország legképességesebb álmai",
                "author": "Ady Endre",
                "work": "Komp-ország és válogatott publicisztikák (1908)",
                "summary": "Ady Endre a huszadik század elejének legmegrázóbb költő-látnoka volt. Publicisztikájában teremtette meg a híres Komp-ország allegóriát: Magyarország a Kelet és a Nyugat partjai között hánykolódó komp, mely a haladás nagy pillanataiban elindul Európa felé, ám a gyáva maradiság, az úri cifraság és a keleti tunyaság mindig visszarántja a lápba. Hitvallása szerint a nemzet egyetlen megmaradási útja a nyugati kultúra, a törvény előtti egyenlőség és az emberi méltóság feltétlen vállalása.",
                "characters": ["Ady Endre, a költő-publicista és látnok"],
                "paragraphs": [
                    {"type": "narration", "text": "Komp-ország, Komp-ország, Komp-ország: legképességesebb álmaiban is csak mászkált két part között: Kelettől Nyugatig, de inkább vissza. Miért riadtak vissza eleink, mikor már-már valóban európai országgá lettünk? Mert megrettentünk a fénytől, megrettentünk a szabadság nehéz terhétől, s édesebbnek tetszett a pusztai álom, a keleti tunyaság, ahol nem kérnek számon sem gondolatot, sem munkát."},
                    {"type": "dialogue", "speaker": "Ady Endre", "text": "Nem a nemzetünket átkozom én, mikor tollammal korbácsolom a maradiságot, hanem azon hamis prófétákat, kik azt hazudják, hogy mi vagyunk a világ legkülönb népe! E gőg altatott el bennünket, míg körülöttünk a népek szabadságjogokat vívtak ki és modern társadalmat építettek."},
                    {"type": "narration", "text": "Csak egyetlen megváltásunk lehet: a Nyugat. Nem a Nyugat bűnei és cifra spekulációja, hanem a Nyugat munkás szelleme, a kutató ész, a törvény előtti szent egyenlőség és az emberi méltóság sérthetetlensége. Ha eloldjuk a kompot a nyugati parttól, nem a szabadság óceánjára evezünk ki, hanem visszasodródunk a keleti posványba."},
                    {"type": "narration", "text": "Ady Endre látnoki erővel felbecsülhetetlen mértékben tárta fel a magyar sors tragikumát: a nemzeti illúziókat alapjaiban szétzúzva követelte, hogy kössük ki a kompot a művelt világhoz, s ne engedjük, hogy a múlt szellemei visszarántsanak bennünket a sötétségbe."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Mit szimbolizál Ady Endre 'Komp-ország' metaforája?", [
                    "A Kelet és Nyugat, az ázsiai elmaradottság és az európai polgárosodás között tétován ingadozó, megállapodni képtelen Magyarország történelmi drámáját.",
                    "A tiszai révhajózás díjszabását.",
                    "A balatoni halászok ladikjait."
                ], 0, ["c1-30-vocab"]),
                fb("grammar", "controlled", "Ady publicisztikája látnoki erővel _____ mértékben leplezte le a nemzeti öntetszelgést. (inestimable / felbecsülhetetlen)", "felbecsülhetetlen", "Ady's journalism to an inestimable degree with visionary power unmasked national conceit.", ["c1-adv-scalar-ferry-country-destiny"]),
                match("vocabulary", "controlled", [["Komp-ország", "Európa és Ázsia között hánykolódó Magyarország"], ["keleti láp", "a szellemi tunyaság és feudális reakció közege"], ["nemzeti öntetszelgés", "a hibákat elfedő vak nacionalista gőg"], ["nyugati műveltség", "a polgári jogállam és tudományos haladás világa"]], ["c1-30-vocab"]),
                fb("grammar", "practice", "A költő a maradi illúziókat alapjaiban _____ követelte a nemzet felébredését. (smashing / szétzúzva)", "szétzúzva", "Fundamentally smashing reactionary illusions the poet demanded the nation's awakening.", ["c1-adv-scalar-ferry-country-destiny"]),
                sb("grammar", "practice", ["Komp-ország", "két", "part", "között", "mászkált", "Kelettől", "Nyugatig."], ["Komp-ország", "két", "part", "között", "mászkált", "Kelettől", "Nyugatig."], "Ferry-country wandered between two shores from East to West.", ["c1-adv-scalar-ferry-country-destiny"]),
                mc("reading", "context", "Milyen veszélyre figyelmeztet Ady, ha eloldjuk a kompot a nyugati parttól?", [
                    "Hogy nem a szabadság óceánjára evezünk ki, hanem visszasodródunk a keleti posványba és a feudális alávetettségbe.",
                    "Hogy elsüllyed a hajó a viharos szélben.",
                    "Hogy a jegyellenőr megbünteti az utasokat."
                ], 0, ["c1-30-vocab"]),
                sw("production", [{"prompt": "Write a reflection on Ady Endre's geopolitical allegory using a scalar evaluative adverbial.", "answer": "Ady Endre látnoki erővel felbecsülhetetlen mértékben, a nemzeti illúziókat alapjaiban szétzúzva figyelmeztetett arra, hogy Komp-ország kizárólag a nyugati polgári jogállamiság partján találhatja meg valódi megváltását."}], ["c1-adv-scalar-ferry-country-destiny"]),
                mc("grammar", "check", "Melyik határozó fejezi ki Ady társadalomkritikájának súlyát a legméltóságteljesebben?", [
                    "látnoki erővel felbecsülhetetlen mértékben / a nemzeti illúziókat alapjaiban szétzúzva",
                    "meglehetősen mérgesen kiabálva az újságban",
                    "egy szép reggelen verset írva"
                ], 0, ["c1-adv-scalar-ferry-country-destiny"])
            ]
        }
    ]

    for l in core_lessons:
        emit_instructional_lesson(30, "core", l, core_title, core_intro if l["num"] == 1 else None)

    # Core Consolidation Lesson
    emit_consolidation_lesson(
        30,
        "core",
        "c1-30-consolidation",
        core_title,
        [
            "I can master the academic vocabulary of geopolitical determinism, historical regions, and collective defense.",
            "I can employ determinist buffer adverbials, participial regional divergence structures, and counter-isolation adversatives.",
            "I can analyze teleological alliance commitments and synthesize Ady Endre's prophetic Komp-ország allegory."
        ],
        [
            mc("grammar", "recognize", "Melyik kifejezés elemzi szakszerűen a Kárpát-medence geopolitikai helyzetét?", [
                "geopolitikailag determinált módon / stratégiailag sérülékenyen ütközőzónaként",
                "térképen nézelődve zöld mezőkkel borítva",
                "amikor süt a nap a folyók felett"
            ], 0, ["c1-adv-geopolitical-determinism-buffer"]),
            mc("grammar", "recognize", "Milyen szerkezettel fejezhetjük ki a nyugati típusú társadalomfejlődés sajátosságait?", [
                "a szerződéses szabadságjogokat és a joguralmat meghonosító intézményi modell",
                "hogyha az uraság kiadja a parancsot a cselédeknek",
                "amikor sok búzát aratnak a földeken"
            ], 0, ["c1-participle-historical-region-divergence"]),
            match("vocabulary", "recognize", [["ütközőzóna", "nagyhatalmak közötti elválasztó térség"], ["joguralom", "a hatalmat korlátozó szerződéses jogrend"], ["megosztott szuverenitás", "hatáskörök közös gyakorlása a nemzetközi térben"], ["kollektív védelem", "a NATO 5. cikkelyén alapuló biztonsági garancia"], ["Komp-ország", "Kelet és Nyugat között ingadozó Magyarország"]], ["c1-30-vocab"]),
            fb("vocabulary", "recall", "A nagyhatalmak által egymás között kialakított befolyási övezet az _____ . (sphere of influence / érdekszféra)", "érdekszféra", "The zone of influence established by great powers among themselves is the sphere of influence.", ["c1-30-vocab"]),
            fb("vocabulary", "recall", "A hatáskörök közös európai gyakorlását _____ szuverenitásnak hívjuk. (pooled / megosztott)", "megosztott", "The joint European exercise of competencies is called pooled (shared) sovereignty.", ["c1-30-vocab"]),
            fb("grammar", "recall", "A térség államai geopolitikailag _____ módon váltak ütközőzónává. (determined / determinált)", "determinált", "States of the region in a geopolitically determined manner became buffer zones.", ["c1-adv-geopolitical-determinism-buffer"]),
            fb("grammar", "context", "A dacos elszigetelődéssel szemben a valóságban a szövetség ad valódi _____ . (capacity to act / cselekvőképességet)", "cselekvőképességet", "In contrast with defiant isolation in reality the alliance grants genuine capacity to act.", ["c1-adv-counter-isolation-adversatives"]),
            fb("grammar", "context", "A védelmet abból a célból fejlesztik, _____ hatékonyan elrettentsék az agressziót. (that / hogy)", "hogy", "Defense is upgraded with the goal that they effectively deter aggression.", ["c1-modal-teleological-alliance-commitments"]),
            mc("grammar", "context", "Mi a funkciója a megosztott szuverenitást védő ellentétes szerkezeteknek?", [
                "Annak bizonyítása, hogy az elszigetelődés nem szuverenitást, hanem végzetes geopolitikai kiszolgáltatottságot eredményez.",
                "Az útlevél-ellenőrzés díjának megállapítása a repülőtéren.",
                "A határőrök egyenruhájának megdicsérése."
            ], 0, ["c1-adv-counter-isolation-adversatives"]),
            sb("grammar", "produce", ["Komp-ország", "megváltása", "a", "nyugati", "polgári", "műveltségben", "rejlik."], ["Komp-ország", "megváltása", "a", "nyugati", "polgári", "műveltségben", "rejlik."], "Ferry-country's salvation lies in Western civil culture.", ["c1-adv-scalar-ferry-country-destiny"]),
            sw("production", [{"prompt": "Write a critical evaluation of collective defense contrasting isolation with alliance loyalty.", "answer": "A dacos elszigetelődéssel szemben a valóságban a NATO-hűség és a megosztott szuverenitás avégből nélkülözhetetlen, hogy Magyarország megőrizze biztonságát a nagyhatalmi agresszióval szemben."}], ["c1-adv-counter-isolation-adversatives"]),
            sw("production", [{"prompt": "Synthesize Ady Endre's prophetic message using a scalar evaluative adverbial.", "answer": "Ady Endre látnoki erővel felbecsülhetetlen mértékben, a nemzeti önáltatást alapjaiban szétzúzva bizonyította be, hogy Magyarország csakis a nyugati polgári értékek kikötőjében őrizheti meg szabadságát."}], ["c1-adv-scalar-ferry-country-destiny"])
        ]
    )

    # ----------------------------------------------------
    # TRACK 2: DISCOURSE (c1-geopolitika)
    # ----------------------------------------------------
    disc_intro = [
        "In the 21st century, Hungary's foreign policy embarked on an audacious yet perilous trajectory: the doctrine of 'Eastern Opening' (Keleti Nyitás) and economic connectivity. Attempting to balance between Western alliance memberships (EU, NATO) and strategic partnerships with Russia and China revived the historic specter of Hungarian pendulum politics (hintapolitika).",
        "From the classified Paks II nuclear deal with Rosatom and long-term Russian gas reliance to transactional veto diplomacy in Brussels and Chinese battery gigafactories, this course brought severe international isolation. In this unit, you will master the elevated discourse of geopolitical maneuvering, energy vulnerability, and future European integration at the C1 level."
    ]

    disc_lessons = [
        {
            "num": 1,
            "stem": f"c1-{slug}-01",
            "title": "Pendulum Politics & The Eastern Opening Doctrine",
            "grammar_title": "Discourse Framing Markers Diagnosing Tactical Pendulum Politics and Connectivity Doctrines",
            "grammar_skill": "c1-discourse-pendulum-politics-framing",
            "goals": [
                "I can analyze the Eastern Opening doctrine, connectivity rhetoric, and 21st-century pendulum politics (*hintapolitika, Keleti Nyitás, konnektivitás, gazdasági pragmatizmus*).",
                "I can deploy discourse framing markers diagnosing foreign policy opportunism (*a keleti nyitás doktrínája nyomán, a taktikai hintapolitika következtében, a gazdasági semlegesség mítoszából fakadóan*).",
                "I can critique double-dealing diplomacy in European foreign relations register."
            ],
            "vocab": [
                {"lemma": "hintapolitika", "translation": "pendulum politics / double-dealing foreign policy", "pos": "noun"},
                {"lemma": "Keleti Nyitás", "translation": "Eastern Opening policy", "pos": "expression"},
                {"lemma": "konnektivitás", "translation": "connectivity doctrine (economic non-alignment)", "pos": "noun"},
                {"lemma": "gazdasági pragmatizmus", "translation": "economic pragmatism", "pos": "expression"},
                {"lemma": "kettős beszéd", "translation": "doublespeak / two-faced diplomacy", "pos": "expression"},
                {"lemma": "szavahihetőség", "translation": "credibility / diplomatic trustworthiness", "pos": "noun"},
                {"lemma": "taktikai manőverezés", "translation": "tactical maneuvering", "pos": "expression"},
                {"lemma": "autokrácia", "translation": "autocracy / authoritarian regime", "pos": "noun"}
            ],
            "gr_text1": "Discourse framing markers diagnose systemic shifts in international orientation: `a keleti nyitás doktrínája nyomán` (in the wake of the Eastern Opening doctrine), `a taktikai hintapolitika következtében` (as a consequence of tactical pendulum politics), `a gazdasági semlegesség hamis illúziójából fakadóan` (stemming from the false illusion of economic neutrality).",
            "gr_text2": "Example: `A taktikai hintapolitika következtében Magyarország nemzetközi szavahihetősége példátlan mértékben erodálódott szövetségesei körében`.",
            "gr_table": [
                ["A keleti nyitás doktrínája nyomán az ország egyoldalúan kiszolgáltatottá vált az autokráciáknak.", "In the wake of the Eastern Opening doctrine the country became unilaterally vulnerable to autocracies."],
                ["A hintapolitika következtében a Visegrádi Négyek együttműködése felbomlott.", "As a consequence of pendulum politics Visegrad Four cooperation dissolved."],
                ["A kettős beszéd logikájából fakadóan a nyugati partnerek trójai falóként tekintenek Budapestre.", "Stemming from the logic of doublespeak Western partners view Budapest as a Trojan horse."]
            ],
            "world_story_seg": {
                "seg_slug": "c1-geopolitika-01-hintapolitika-kelet-nyugat",
                "title": "A hinta két végén: Keleti Nyitás és elszigetelődés",
                "summary": "A 2010 után meghirdetett Keleti Nyitás és konnektivitás doktrínája a nyugati szövetségesek elidegenedéséhez és a diplomáciai elszigetelődéshez vezetett.",
                "paragraphs": [
                    {"type": "narration", "text": "A kormányzat a 'konnektivitás' és a 'gazdasági semlegesség' jelszavával hirdette meg a világ újbóli blokkosodásának elutasítását. A hivatalos narratíva szerint Magyarországnak híd szerepet kell betöltenie a nyugati piacok és a keleti tőke között."},
                    {"type": "dialogue", "speaker": "Kovács Dániel", "text": "A taktikai hintapolitika következtében az ország szavahihetősége teljesen megsemmisült. Nem lehet egyszerre élvezni a NATO védőernyőjét és az uniós pénzeket, miközben stratégiai partnerséget építünk a szövetségünket fenyegető keleti diktatúrákkal."},
                    {"type": "narration", "text": "A kettős beszéd diplomáciája szétverte a Visegrádi Együttműködést is: Varsó és Prága elfordult Budapesttől, miután a magyar vezetés oroszpárti álláspontra helyezkedett a háborús krízisben."},
                    {"type": "narration", "text": "A híd mítosza gyorsan elillant: a szövetségesek szemében Magyarország nem összekötő kapoccsá, hanem a keleti autokráciák megbízhatatlan trójai falovává minősült át."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Mit értünk 'hintapolitika' alatt a magyar diplomáciatörténetben és jelenkorban?", [
                    "Két egymással szembenálló nagyhatalmi tömb (Nyugat és Kelet) közötti taktikai egyensúlyozást és opportunista ingadozást, amely feladja az elvi elköteleződést.",
                    "A diplomáciai fogadásokon való hintaszékek használatát.",
                    "A játszóterek felújítását célzó minisztériumi programot."
                ], 0, ["c1-geopolitika-vocab"]),
                fb("grammar", "controlled", "A keleti nyitás doktrínája _____ az ország stratégiai partnerségre lépett tekintélyelvű rezsimekkel. (in the wake of / nyomán)", "nyomán", "In the wake of the Eastern Opening doctrine the country entered into strategic partnership with authoritarian regimes.", ["c1-discourse-pendulum-politics-framing"]),
                match("vocabulary", "controlled", [["hintapolitika", "két rivális szövetség közötti opportunista egyensúlyozás"], ["Keleti Nyitás", "orientációváltás az ázsiai és posztszovjet államok felé"], ["konnektivitás", "a gazdasági semlegesség és blokkmentesség kormányzati jelszava"], ["szavahihetőség", "a szövetségesi megbízhatóság nemzetközi tőkéje"]], ["c1-geopolitika-vocab"]),
                fb("grammar", "practice", "A taktikai hintapolitika _____ felbomlott a közép-európai V4-es szövetség. (consequence / következtében)", "következtében", "As a consequence of tactical pendulum politics Central European V4 alliance dissolved.", ["c1-discourse-pendulum-politics-framing"]),
                sb("grammar", "practice", ["A", "hintapolitika", "aláássa", "Magyarország", "nemzetközi", "szavahihetőségét."], ["A", "hintapolitika", "aláássa", "Magyarország", "nemzetközi", "szavahihetőségét."], "Pendulum politics undermines Hungary's international credibility.", ["c1-discourse-pendulum-politics-framing"]),
                dc("dialogue", [
                    {"speaker": "Külpolitikai elemző", "text": "Hogyan ítélik meg Washingtonban és Brüsszelben a magyar gazdasági semlegesség doktrínáját?"},
                    {"speaker": "Diplomata", "text": "Úgy, hogy a keleti nyitás doktrínája _____ Magyarország eltávolodott az euroatlanti értékrendtől."},
                    {"speaker": "Külpolitikai elemző", "text": "Ez a folyamat a legmélyebb diplomáciai elszigetelődéshez vezetett."}
                ], ["nyomán", "nélkül", "helyett"], 0, ["c1-discourse-pendulum-politics-framing"]),
                sw("production", [{"prompt": "Write a critical diagnosis of pendulum politics using a discourse framing marker.", "answer": "A taktikai hintapolitika következtében és a keleti nyitás doktrínája nyomán Magyarország felélte szövetségesi hitelét a transzatlanti közösségben, és végzetesen elszigetelődött Európában."}], ["c1-discourse-pendulum-politics-framing"]),
                mc("grammar", "check", "Melyik kifejezés diagnosztizálja a külpolitikai fordulatot a leghitelesebben?", [
                    "a taktikai hintapolitika következtében / a keleti nyitás doktrínája nyomán",
                    "amikor a miniszter elrepül messzire repülővel",
                    "egy szép napon másfelé nézve"
                ], 0, ["c1-discourse-pendulum-politics-framing"])
            ]
        },
        {
            "num": 2,
            "stem": f"c1-{slug}-02",
            "title": "Energy Vulnerability: Paks II & The Russian Gas Trap",
            "grammar_title": "Deontic Modal Structures Asserting National Diversification Duties Against Autocratic Energy Blackmail",
            "grammar_skill": "c1-modal-deontic-energy-security",
            "goals": [
                "I can analyze the 2014 Paks II nuclear agreement with Rosatom, classified long-term Gazprom gas contracts, and energy blackmail (*Paks II megállapodás, orosz gázfüggőség, hiteltitkosítás, geopolitikai zsarolhatóság*).",
                "I can deploy deontic modal structures asserting diversification duties (*az államnak kötelessége felszámolni az egyoldalú függést, nem kötheti magát évtizedekre egy agresszor nagyhatalomhoz, a nemzetbiztonság nem áldozható fel rövid távú alkukért*).",
                "I can critique energy imperialism in international security economics."
            ],
            "vocab": [
                {"lemma": "Paks II beruházás", "translation": "Paks II nuclear power plant project (Rosatom)", "pos": "expression"},
                {"lemma": "orosz gázfüggőség", "translation": "Russian natural gas dependency", "pos": "expression"},
                {"lemma": "forrásdiverzifikáció", "translation": "source diversification", "pos": "noun"},
                {"lemma": "energetikai kitettség", "translation": "energy exposure / vulnerability", "pos": "expression"},
                {"lemma": "hitelmegállapodás", "translation": "interstate loan agreement", "pos": "noun"},
                {"lemma": "szerződéstitkosítás", "translation": "classification of contracts (30-year secrecy)", "pos": "noun"},
                {"lemma": "geopolitikai zsarolhatóság", "translation": "geopolitical blackmailability", "pos": "expression"},
                {"lemma": "energetikai szuverenitás", "translation": "energy sovereignty", "pos": "expression"}
            ],
            "gr_text1": "Deontic modal structures articulate uncompromising constitutional and security obligations regarding critical infrastructure: `az államnak kötelező szavatolnia az energiaellátás diverzifikációját` (the state has a mandatory duty to guarantee diversification of energy supply), `nem engedhető meg az egyoldalú technológiai és pénzügyi kitettség rögzítése` (unilateral technological and financial exposure must not be allowed to become fixed), `a nemzeti szuverenitás nem szolgáltatható ki külső zsarolási potenciálnak` (national sovereignty cannot be surrendered to external blackmail leverage).",
            "gr_text2": "Example: `Egy felelős kormánynak kötelessége azonnal megnyitni az alternatív energiafolyosókat, s az ország nem láncolhatja magát évtizedekre az orosz atom- és gázmonopóliumhoz`.",
            "gr_table": [
                ["Az államnak kötelessége függetleníteni az országot az orosz energiamonopóliumtól.", "The state has a duty to make the country independent from the Russian energy monopoly."],
                ["A nemzetbiztonság nem áldozható fel titkosított gázalkuk oltárán.", "National security cannot be sacrificed on the altar of classified gas deals."],
                ["A döntéshozóknak szavatolniuk kell a megújuló források prioritását.", "Decision-makers must guarantee the priority of renewable sources."]
            ],
            "world_story_seg": {
                "seg_slug": "c1-geopolitika-02-paks2-es-gazfuggoseg",
                "title": "Nukleáris béklyó: Paks II és a gázalkuk titkai",
                "summary": "A 2014-es Paks II paktum és a Gazprommal kötött titkosított szerződések évtizedekre Moszkvához kötötték a magyar energiapolitikát.",
                "paragraphs": [
                    {"type": "narration", "text": "2014 januárjában Vlagyimir Putyin és Orbán Viktor Moszkvában megállapodtak a paksi atomerőmű bővítéséről: 12,5 milliárd eurós orosz hitel és a Roszatom technológiája. A szerződéseket versenytárgyalás nélkül kötötték meg, a részleteket pedig harminc évre titkosították."},
                    {"type": "dialogue", "speaker": "Szabó Tamás", "text": "Az államnak kötelessége volna garantálni az energetikai diverzifikációt. Nem köthetjük meg az ország kezét évtizedekre egyetlen agresszor birodalom hitelével és fűtőelem-monopóliumával, mert a Paks II nem olcsó áramot, hanem geopolitikai zsarolhatóságot hoz."},
                    {"type": "narration", "text": "Miközben Európa levált az orosz gázról, Magyarország újabb hosszú távú szerződéseket írt alá a Gazprommal, amelyek rekordméretű költségvetési hiányt okoztak az egekbe szökő gázárak idején."},
                    {"type": "narration", "text": "A nukleáris és fosszilis függőség konzerválása megbénította az energetikai átállást, s a magyar szuverenitás legérzékenyebb pontját szolgáltatta ki Moszkvának."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Miért tekintik a nemzetközi szakértők súlyos biztonsági kockázatnak a Paks II beruházást?", [
                    "Mert nyilvános versenytárgyalás nélkül, orosz állami hitelből és a Roszatom kizárólagos technológiájával valósul meg, évtizedekre Moszkvához láncolva az energiaellátást.",
                    "Mert túl sok napelemet építenek az erőmű köré.",
                    "Mert a paksi halászlé receptjét nem osztották meg az oroszokkal."
                ], 0, ["c1-geopolitika-vocab"]),
                fb("grammar", "controlled", "Az államnak kötelessége _____ a nemzeti energiaellátás valós függetlenségét. (guarantee / garantálni)", "garantálni", "The state has a duty to guarantee real independence of national energy supply.", ["c1-modal-deontic-energy-security"]),
                match("vocabulary", "controlled", [["Paks II", "orosz hitelből épülő új nukleáris blokkok"], ["orosz gázfüggőség", "egyoldalú kitettség a Gazprom szállításaival szemben"], ["forrásdiverzifikáció", "több független energetikai beszállító bevonása"], ["szerződéstitkosítás", "a hitel- és beruházási feltételek elzárása a nyilvánosság elől"]], ["c1-geopolitika-vocab"]),
                fb("grammar", "practice", "A nemzet szuverenitása nem _____ ki a keleti autokráciák zsarolási potenciáljának. (cannot be surrendered / szolgáltatható)", "szolgáltatható", "The nation's sovereignty cannot be surrendered to the blackmail leverage of Eastern autocracies.", ["c1-modal-deontic-energy-security"]),
                sb("grammar", "practice", ["Az", "államnak", "kötelessége", "felszámolni", "az", "egyoldalú", "energetikai", "kitettséget."], ["Az", "államnak", "kötelessége", "felszámolni", "az", "egyoldalú", "energetikai", "kitettséget."], "The state has a duty to liquidate unilateral energy exposure.", ["c1-modal-deontic-energy-security"]),
                dc("dialogue", [
                    {"speaker": "Energiapolitikus", "text": "Hogyan számolhatjuk fel az ország krónikus orosz gázfüggőségét?"},
                    {"speaker": "Zöld szakértő", "text": "Csakis úgy, ha felismerjük: a döntéshozóknak kötelező _____ az LNG-terminálokat és a megújuló forrásokat."},
                    {"speaker": "Energiapolitikus", "text": "A monopóliumok fenntartása közvetlen nemzetbiztonsági kockázat."}
                ], ["támogatniuk", "tagadniuk", "zárniuk"], 0, ["c1-modal-deontic-energy-security"]),
                sw("production", [{"prompt": "Write a sentence formulating energy diversification obligations using a deontic modal structure.", "answer": "Az államnak kötelessége felszámolni az egyoldalú orosz gáz- és atomfüggőséget, és nem szolgáltathatja ki a nemzeti szuverenitást Moszkva geopolitikai zsarolásának."}], ["c1-modal-deontic-energy-security"]),
                mc("grammar", "check", "Melyik modális szerkezet rögzíti az energiabiztonsági kötelességet a leghatározottabban?", [
                    "az államnak kötelessége garantálni a diverzifikációt / nem szolgáltathatja ki a szuverenitást",
                    "talán vehetnénk egy kis gázt máshonnan is",
                    "jó lenne ha meleg lenne a radiátor télen"
                ], 0, ["c1-modal-deontic-energy-security"])
            ]
        },
        {
            "num": 3,
            "stem": f"c1-{slug}-03",
            "title": "Transactional Veto Diplomacy & EU Conditionality",
            "grammar_title": "Proportional Correlative Conjunctions Mapping Veto Extortion Against Escalating International Isolation",
            "grammar_skill": "c1-adv-proportional-veto-diplomacy",
            "goals": [
                "I can analyze EU unanimity voting, transactional veto diplomacy, conditionality mechanisms, and frozen EU funds (*vétódiplomácia, tranzakcionális alku, jogállamisági kondicionalitás, forrásbefagyasztás*).",
                "I can deploy proportional correlative conjunctions mapping international alienation (*minél gyakrabban él a kormányzat a vétózsarolással, annál inkább elszigetelődik az Európai Tanácsban, amilyen mértékben blokkolják a közös döntéseket, olyan arányban gyorsul fel az egyhangúsági szabály felszámolása*).",
                "I can critique transactional diplomacy in international governance register."
            ],
            "vocab": [
                {"lemma": "vétódiplomácia", "translation": "veto diplomacy", "pos": "noun"},
                {"lemma": "tranzakcionális politika", "translation": "transactional politics", "pos": "expression"},
                {"lemma": "egyhangúsági szabály", "translation": "unanimity rule (in EU foreign policy)", "pos": "expression"},
                {"lemma": "zsarolási potenciál", "translation": "blackmail leverage / extortion capacity", "pos": "expression"},
                {"lemma": "jogállamisági kondicionalitás", "translation": "rule of law conditionality", "pos": "expression"},
                {"lemma": "forrásbefagyasztás", "translation": "freezing of cohesion funds", "pos": "noun"},
                {"lemma": "szankciós csomag", "translation": "sanctions package", "pos": "noun"},
                {"lemma": "diplomáciai elszigetelődés", "translation": "diplomatic isolation / alienation", "pos": "expression"}
            ],
            "gr_text1": "Proportional correlative structures map the direct diplomatic trade-off between domestic veto posturing and international marginalization: `minél gátlástalanabbul alkalmazza a kormányzat a vétódiplomáciát, annál mélyebb diplomáciai elszigetelődésbe süllyed` (the more unscrupulously the government applies veto diplomacy, the deeper diplomatic isolation it sinks into), `amilyen mértékben zsarolásra használja a szankciós csomagokat, olyan arányban növeli a tagállamok elszántságát az egyhangúsági szabály eltörlésére` (to the extent it uses sanctions packages for extortion, to that extent it increases member states' determination to abolish the unanimity rule).",
            "gr_text2": "Example: `Minél inkább a befagyasztott pénzek kizsarolására használja a miniszterelnök az uniós vétókat, annál inkább felgyorsul a mag-Európa különutas döntéshozatala`.",
            "gr_table": [
                ["Minél többször vétóz a kormány Brüsszelben, annál kevesebb szövetségese marad.", "The more times the government vetoes in Brussels, the fewer allies it has left."],
                ["Amilyen mértékben nő a zsarolási kísérlet, olyan arányban keményedik az uniós válasz.", "To the extent extortion attempts grow, to that extent the EU response hardens."],
                ["Minél inkább blokkolják a segélyeket, annál inkább megkerülik Magyarországot a döntésekben.", "The more they block aid, the more Hungary is bypassed in decisions."]
            ],
            "world_story_seg": {
                "seg_slug": "c1-geopolitika-03-vetodiplomacia-brusszelben",
                "title": "A zsarolás művészete: Vétók és alku a tanácsban",
                "summary": "A magyar kormány az egyhangú uniós döntéshozatalt és a vétójogot zsarolási eszközként használta a jogállamisági forrásbefagyasztások ellen.",
                "paragraphs": [
                    {"type": "narration", "text": "Amikor az Európai Unió tagállamai az orosz agresszióra válaszul gazdasági szankciókat és Ukrajnát támogató hitelcsomagokat dolgoztak ki, a magyar diplomácia rendre az utolsó pillanatban emelt vétót."},
                    {"type": "dialogue", "speaker": "Bíró István", "text": "Minél inkább a jogállamisági eljárásban befagyasztott milliárdok feloldására használja a hatalom a vétójogot, annál inkább megsemmisíti a magyar diplomácia hitelességét. Ez a tranzakcionális politika bumerángként üt vissza az egész nemzetre."},
                    {"type": "narration", "text": "A Kirill pátriárka szankcionálásának blokkolásától az 50 milliárdos uniós segély megakasztásáig terjedő vétósorozat megelégelte a partnerek türelmét: életbe lépett a kondicionalitási mechanizmus, amely milliárdos forrásokat zárolt."},
                    {"type": "narration", "text": "A vétódiplomácia végső eredménye az elszigetelődés lett: a huszonhat tagállam elkezdte kidolgozni a budapesti vétókat megkerülő, különmegállapodásos döntéshozatali mechanizmusokat."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Hogyan működött a 'tranzakcionális vétódiplomácia' a magyar kormány gyakorlatában?", [
                    "A közös uniós döntések és szankciós csomagok megvétózásával zsarolta a tagállamokat, hogy elérje a jogállamisági korrupció miatt befagyasztott források feloldását.",
                    "Minden uniós törvényt azonnal aláírt ellenvetés nélkül.",
                    "Csak a mezőgazdasági termények árában kért engedményeket."
                ], 0, ["c1-geopolitika-vocab"]),
                fb("grammar", "controlled", "Minél gyakrabban él a kormányzat a vétózsarolással, _____ inkább elszigetelődik az Európai Unióban. (the more / annál)", "annál", "The more frequently the government resorts to veto blackmail, the more it is isolated in the EU.", ["c1-adv-proportional-veto-diplomacy"]),
                match("vocabulary", "controlled", [["vétódiplomácia", "közös döntések megakasztása egyéni haszonszerzésért"], ["tranzakcionális politika", "értékek feláldozása azonnali anyagi előnyökért"], ["jogállamisági kondicionalitás", "uniós pénzek megvonása a demokratikus normák megsértése miatt"], ["forrásbefagyasztás", "a kohéziós alapok kifizetésének leállítása"]], ["c1-geopolitika-vocab"]),
                fb("grammar", "practice", "Amilyen mértékben növekszik a zsarolási potenciál fitogtatása, olyan _____ erodálódik a szövetségesek bizalma. (proportion / arányban)", "arányban", "In proportion as flaunting blackmail leverage increases, to that extent allies' trust erodes.", ["c1-adv-proportional-veto-diplomacy"]),
                sb("grammar", "practice", ["Minél", "több", "a", "vétó,", "annál", "mélyebb", "az", "elszigeteltség."], ["Minél", "több", "a", "vétó,", "annál", "mélyebb", "az", "elszigeteltség."], "The more the vetoes, the deeper the isolation.", ["c1-adv-proportional-veto-diplomacy"]),
                dc("dialogue", [
                    {"speaker": "Brüsszeli tudósító", "text": "Meddig tartható fenn a magyar vétózsarolás az Európai Tanácsban?"},
                    {"speaker": "Uniós diplomata", "text": "Nem sokáig: minél többször blokkolja Budapest a közös biztonsági döntéseket, _____ inkább felgyorsul az egyhangúsági szabály felszámolása."},
                    {"speaker": "Brüsszeli tudósító", "text": "Ami a magyar érdekérvényesítés végső vereségét jelentené."}
                ], ["annál", "mindig", "soha"], 0, ["c1-adv-proportional-veto-diplomacy"]),
                sw("production", [{"prompt": "Write a sentence analyzing veto diplomacy using 'Minél... annál...'.", "answer": "Minél gyakrabban alkalmazza a kormányzat a tranzakcionális vétódiplomáciát a befagyasztott források feloldására, annál mélyebb bizalmi válságot idéz elő, és annál inkább elszigetelődik az európai partnerek körében."}], ["c1-adv-proportional-veto-diplomacy"]),
                mc("grammar", "check", "Melyik arányossági szerkezet ragadja meg a vétópolitika elszigetelő hatását a legpontosabban?", [
                    "Minél gátlástalanabbul vétóz a kormányzat... annál mélyebb diplomáciai elszigetelődésbe süllyed / Amilyen mértékben... olyan arányban",
                    "Ha sokáig tart az ülés, elfáradnak a miniszterek",
                    "A brüsszeli épületben sok a folyosó"
                ], 0, ["c1-adv-proportional-veto-diplomacy"])
            ]
        },
        {
            "num": 4,
            "stem": f"c1-{slug}-04",
            "title": "Chinese Mega-Loans, Battery Gigafactories & Debt Traps",
            "grammar_title": "Epistemic Stance Markers Assessing Autocratic Debt Trap Risks and Sovereignty Erosion",
            "grammar_skill": "c1-epistemic-debt-trap-exposure",
            "goals": [
                "I can analyze the Belt and Road Initiative in Hungary, Budapest–Belgrade railway debt, and Chinese battery gigafactories (*adósságcsapda-diplomácia, akkugyár-kolonizáció, titkosított hitelek, környezeti kockázat*).",
                "I can deploy epistemic stance markers assessing autocratic debt trap risks (*kétségkívül bebizonyosodott a távol-keleti hitelfüggőség veszélye, minden jel szerint a titkosított megaprojektek adósságcsapdába vezetik az országot, aligha vitatható az ipari kolonizáció szuverenitást sértő jellege*).",
                "I can critique economic non-alignment in geo-economics register."
            ],
            "vocab": [
                {"lemma": "adósságcsapda-diplomácia", "translation": "debt-trap diplomacy (Belt and Road)", "pos": "expression"},
                {"lemma": "akkumulátorgyár", "translation": "battery gigafactory (CATL, Eve Power)", "pos": "noun"},
                {"lemma": "titkosított hitel", "translation": "classified / confidential loan agreement", "pos": "expression"},
                {"lemma": "geopolitikai hídfőállás", "translation": "geopolitical bridgehead", "pos": "expression"},
                {"lemma": "vízbázisveszélyeztetés", "translation": "endangerment of water aquifers", "pos": "noun"},
                {"lemma": "ipari kolonizáció", "translation": "industrial colonization / subcontracting servitude", "pos": "expression"},
                {"lemma": "energiaintenzív iparosítás", "translation": "energy-intensive industrialization", "pos": "expression"},
                {"lemma": "vendégmunkás-kvóta", "translation": "guest worker quota", "pos": "expression"}
            ],
            "gr_text1": "Epistemic stance markers formulate evidentiary assessments regarding geopolitical debt entanglement and environmental risk: `kétségkívül bebizonyosodott az adósságcsapda kockázata` (the risk of debt trap has undoubtedly been demonstrated), `minden jel szerint a kínai megahitelek felvétele a nemzeti vagyon elzálogosítását jelenti` (by all indications taking Chinese mega-loans means mortgaging national assets), `aligha vitatható az akkumulátorgyárak fenntarthatatlan víz- és energiaigénye` (the unsustainable water and power demand of battery plants can hardly be disputed).",
            "gr_text2": "Example: `Kétségkívül bebizonyosodott, hogy a titkosított kínai hitelekből épülő beruházások nem a magyar jólétet, hanem egy távoli birodalom geopolitikai hídfőállását szolgálják`.",
            "gr_table": [
                ["Kétségkívül látható az adósságcsapda-diplomácia érvényesülése a Budapest–Belgrád projektben.", "Undoubtedly the operation of debt-trap diplomacy is visible in the Budapest–Belgrade project."],
                ["Minden jel szerint a gigantikus akkugyárak kimerítik a hazai vízkészleteket.", "By all indications gigantic battery factories deplete domestic water reserves."],
                ["Aligha vitatható, hogy az ázsiai vendégmunkások beáramlása társadalmi feszültséget kelt.", "It can hardly be disputed that the influx of Asian guest workers creates social tension."]
            ],
            "world_story_seg": {
                "seg_slug": "c1-geopolitika-04-kinai-akkubirodalom",
                "title": "Akkumulátorköztársaság: Kínai gyárak és a környezet ára",
                "summary": "A Budapest–Belgrád vasút és a debreceni CATL akkumulátorgyár felépítése Kína európai hídfőállásává tette Magyarországot, súlyos környezeti és gazdasági kockázatokkal.",
                "paragraphs": [
                    {"type": "narration", "text": "A Keleti Nyitás leglátványosabb fejleménye a hatalmas kínai tőkebeáramlás volt: Debrecenben, Gödön és Komáromban sorra létesültek a távol-keleti akkumulátorkonszernek gigagyárai, amelyekhez az állam százmilliárdos készpénztámogatást és infrastruktúrát biztosított."},
                    {"type": "dialogue", "speaker": "Major Anna", "text": "Kétségkívül bebizonyosodott az adósságcsapda-diplomácia veszélye. A titkosított feltételű Budapest–Belgrád vasúthiteltől a termőföldeket felzabáló akkugyárakig az ország egy idegen birodalom környezetszennyező összeszerelő üzemévé züllik."},
                    {"type": "narration", "text": "A beruházások gigantikus víz- és áramigénye veszélybe sodorta az aszály sújtotta alföldi vízbázisokat, miközben a gyártósorok mellé tízezrével érkeztek a távol-keleti vendégmunkások."},
                    {"type": "narration", "text": "Aligha vitatható a gazdasági aszimmetria: a profit a külföldi konszerneknél csapódik le, míg az adósság, az energiaválság és a mérgező vegyi kockázatok a magyar lakosságra hárulnak."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Mit nevez a nemzetközi szakirodalom 'adósságcsapda-diplomáciának' a kínai hitelek kapcsán?", [
                    "Olyan gigantikus, titkosított feltételű infrastrukturális hitelek nyújtását, amelyek piaci megtérülése kétséges, s a visszafizetés elmaradásakor a hitelező politikai és stratégiai engedményeket kényszerít ki.",
                    "A bankkártyák lejárati dátumának automatikus meghosszabbítását.",
                    "A vasúti talpfák ingyenes cseréjét faanyaghiány idején."
                ], 0, ["c1-geopolitika-vocab"]),
                fb("grammar", "controlled", "Kétségkívül _____ a titkosított megahitelek nemzetgazdasági kockázata. (demonstrated / bebizonyosodott)", "bebizonyosodott", "Undoubtedly the national economic risk of classified mega-loans has been demonstrated.", ["c1-epistemic-debt-trap-exposure"]),
                match("vocabulary", "controlled", [["adósságcsapda", "kölcsönök visszafizetési kényszere révén kialakuló politikai függés"], ["akkumulátorgyár", "víz- és energiaintenzív távol-keleti vegyipari üzem"], ["titkosított hitel", "a közvélemény elől elzárt államközi hitelszerződés"], ["ipari kolonizáció", "egy ország alárendelése külső birodalmi ipari érdekeknek"]], ["c1-geopolitika-vocab"]),
                fb("grammar", "practice", "Aligha vitatható, hogy az akkumulátorgyárak vízigénye veszélyezteti az alföldi _____ . (water aquifers / vízbázist)", "vízbázist", "It can hardly be disputed that the water demand of battery plants endangers lowland water aquifers.", ["c1-epistemic-debt-trap-exposure"]),
                sb("grammar", "practice", ["Kétségkívül", "bebizonyosodott", "az", "adósságcsapda-diplomácia", "súlyos", "veszélye."], ["Kétségkívül", "bebizonyosodott", "az", "adósságcsapda-diplomácia", "súlyos", "veszélye."], "Undoubtedly the severe danger of debt-trap diplomacy has been demonstrated.", ["c1-epistemic-debt-trap-exposure"]),
                dc("dialogue", [
                    {"speaker": "Környezetvédő", "text": "Hogyan egyeztethető össze a debreceni gigagyár a klímavédelmi célokkal?"},
                    {"speaker": "Közgazdász", "text": "Semmiképp: minden jel szerint az energiaintenzív iparosítás feláldozza a jövő nemzedékek ivóvízkészletét egy idegen birodalom gazdasági _____ érdekében."},
                    {"speaker": "Környezetvédő", "text": "Ez a nemzeti szuverenitás legsúlyosabb kiárusítása."}
                ], ["hídfőállása", "békéje", "szépsége"], 0, ["c1-epistemic-debt-trap-exposure"]),
                sw("production", [{"prompt": "Write a critical evaluation of Chinese economic expansion using an epistemic stance marker.", "answer": "Kétségkívül bebizonyosodott, hogy a titkosított feltételű kínai hitelek és a környezetromboló akkumulátorgyárak az adósságcsapda-diplomácia csapdájába hajtják Magyarországot, meggyengítve gazdasági önrendelkezését."}], ["c1-epistemic-debt-trap-exposure"]),
                mc("grammar", "check", "Melyik episztemikus kifejezés értékeli a külföldi eladósodást a leghitelesebben?", [
                    "kétségkívül bebizonyosodott / aligha vitatható az adósságcsapda kockázata",
                    "talán nem kell visszafizetni a kölcsönt",
                    "reméljük jól megépítik a gyárat"
                ], 0, ["c1-epistemic-debt-trap-exposure"])
            ]
        },
        {
            "num": 5,
            "stem": f"c1-{slug}-05",
            "title": "Historical Crossroads: Core Europe or Eastern Periphery",
            "grammar_title": "Evaluative Synthesis Particles Formulating Definitive Manifestos for Western Integration and Democracy",
            "grammar_skill": "c1-adv-conclusive-european-destiny-synthesis",
            "goals": [
                "I can analyze the two-speed Europe model, semi-periphery status, and the final mooring of Ferry-Country (*kétsebességes Európa, mag-Európa, félperiféria, geopolitikai elsodródás*).",
                "I can deploy evaluative synthesis particles formulating historical manifestos (*végső soron elengedhetetlen a nyugati elköteleződés megerősítése, mindent egybevetve az európai demokratikus közösség a magyar jövő egyetlen záloga, végeredményben a keleti autokráciák felé való sodródás nemzeti sorstragédiához vezet*).",
                "I can synthesize a comprehensive vision for European Hungary in 21st-century world order."
            ],
            "vocab": [
                {"lemma": "kétsebességes Európa", "translation": "two-speed Europe", "pos": "expression"},
                {"lemma": "mag-Európa", "translation": "core Europe (inner circle of integration)", "pos": "expression"},
                {"lemma": "félperiféria", "translation": "semi-periphery", "pos": "noun"},
                {"lemma": "geopolitikai elsodródás", "translation": "geopolitical drifting / alienation from the West", "pos": "expression"},
                {"lemma": "európai értékrend", "translation": "European value system / democratic consensus", "pos": "expression"},
                {"lemma": "történelmi felelősség", "translation": "historical responsibility", "pos": "expression"},
                {"lemma": "szövetségesi integritás", "translation": "alliance integrity", "pos": "expression"},
                {"lemma": "jövőforgatókönyv", "translation": "future scenario", "pos": "noun"}
            ],
            "gr_text1": "Evaluative synthesis particles formulate definitive historical manifestos asserting the moral and strategic imperative of Western integration: `végső soron elengedhetetlen a nyugati szövetségi hűség megingathatatlan vállalása` (ultimately unwavering assumption of Western alliance loyalty is indispensable), `mindent egybevetve az európai demokratikus közösséghez tartozás a nemzet megmaradásának egyetlen záloga` (all things considered belonging to the European democratic community is the sole guarantee of the nation's survival), `végeredményben a mag-Európából való kiszorulás a történelmi perifériára süllyedést jelenti` (in the final analysis being squeezed out of core Europe means sinking to the historical periphery).",
            "gr_text2": "Example: `Végső soron elengedhetetlen felismerni: mindent egybevetve a kétsebességes Európa létrejöttekor Magyarország nem engedheti meg magának a keleti perifériára való elsodródást`.",
            "gr_table": [
                ["Végső soron elengedhetetlen a nyugati demokráciákhoz való hűség.", "Ultimately loyalty to Western democracies is indispensable."],
                ["Mindent egybevetve a mag-Európához tartozás a magyar jövő záloga.", "All things considered belonging to core Europe is the guarantee of Hungarian future."],
                ["Végeredményben az elszigetelődés feladja Szent István és Ady Endre örökségét.", "In the final analysis isolation surrenders the heritage of Saint Stephen and Endre Ady."]
            ],
            "world_story_seg": {
                "seg_slug": "c1-geopolitika-05-mag-europa-vagy-periferia",
                "title": "Történelmi válaszút: Mag-Európa vagy keleti periféria",
                "summary": "A kétsebességes Európa létrejötte választásra kényszeríti Magyarországot: a mag-Európa demokratikus közössége vagy a kiszolgáltatott keleti félperiféria.",
                "paragraphs": [
                    {"type": "narration", "text": "Az Európai Unió magállamai megelégelték a döntéshozatal szisztematikus szabotálását. A kétsebességes Európa körvonalai határozottá váltak: a belső mag szorosabb védelmi, költségvetési és politikai unióvá formálódik, miközben az illiberális periféria kiszorul a döntésekből."},
                    {"type": "dialogue", "speaker": "Csonka Gábor", "text": "Végső soron elengedhetetlen a nyugati elköteleződés megerősítése. Mindent egybevetve Magyarország jövője a mag-Európához való megkérdőjelezhetetlen tartozásban rejlik. Ha eloldjuk a kompot a nyugati parttól, nem szuverének leszünk, hanem a keleti autokráciák martaléka."},
                    {"type": "narration", "text": "Ady Endre figyelmeztetése ma élesebben cseng, mint valaha. A szabadság nem ajándék, hanem mindennapi felelősség: a Kárpát-medence nem válhat az ázsiai despotizmus kísérleti terepévé anélkül, hogy a nemzet el ne veszítené jövőjét."},
                    {"type": "narration", "text": "Mindent egybevetve a magyar nemzet sorsa nem az elszigetelt dacban, hanem az európai polgári demokrácia, a jogállam és az emberi méltóság megingathatatlan védelmében teljesedhet ki."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Mit jelent a 'kétsebességes Európa' koncepciója Magyarország jövője szempontjából?", [
                    "Azt, hogy a szorosabb integrációt és jogállamiságot vállaló magállamok (Franciaország, Németország stb.) mélyebb szövetségre lépnek, míg a kimaradó renitens államok a pénzügyi és döntési perifériára rekednek.",
                    "Azt, hogy az unióban kétféle valutát vezetnek be.",
                    "Azt, hogy a vonatok sebességét kettéosztják tehervonatokra és személyvonatokra."
                ], 0, ["c1-geopolitika-vocab"]),
                fb("grammar", "controlled", "Végső soron _____ a mag-Európa demokratikus közösségéhez való hűség. (indispensable / elengedhetetlen)", "elengedhetetlen", "Ultimately loyalty to the democratic community of core Europe is indispensable.", ["c1-adv-conclusive-european-destiny-synthesis"]),
                match("vocabulary", "controlled", [["kétsebességes Európa", "különböző szintű elköteleződést nyújtó integrációs modell"], ["mag-Európa", "a szoros gazdasági és védelmi uniót alkotó belső kör"], ["félperiféria", "a döntésekből kiszoruló, kiszolgáltatott külső zóna"], ["történelmi felelősség", "a jövő generációk sorsát meghatározó nemzeti választás"]], ["c1-geopolitika-vocab"]),
                fb("grammar", "practice", "Mindent egybevetve az európai integráció a nemzeti szuverenitás legfőbb _____ . (guarantee / záloga)", "záloga", "All things considered European integration is the primary guarantee of national sovereignty.", ["c1-adv-conclusive-european-destiny-synthesis"]),
                sb("grammar", "practice", ["Végső", "soron", "elengedhetetlen", "a", "nyugati", "értékek", "védelme."], ["Végső", "soron", "elengedhetetlen", "a", "nyugati", "értékek", "védelme."], "Ultimately the protection of Western values is indispensable.", ["c1-adv-conclusive-european-destiny-synthesis"]),
                dc("dialogue", [
                    {"speaker": "Filozófus", "text": "Hová kössük ki Ady Komp-országát a huszonegyedik század viharaiban?"},
                    {"speaker": "Történész", "text": "Kizárólag a nyugati parthoz: mindent egybevetve az európai jogállam és szabadság az egyetlen tartós _____."},
                    {"speaker": "Filozófus", "text": "Ezen múlik Magyarország megmaradása."}
                ], ["zálogunk", "terhünk", "veszélyünk"], 0, ["c1-adv-conclusive-european-destiny-synthesis"]),
                sw("production", [{"prompt": "Write a concluding manifesto on Hungary's European destiny using an evaluative synthesis particle.", "answer": "Végső soron elengedhetetlen a nyugati demokratikus értékek feltétlen védelme, hiszen mindent egybevetve Magyarország jövője és nemzeti szabadsága kizárólag a mag-Európához való megkérdőjelezhetetlen tartozásban teljesedhet ki."}], ["c1-adv-conclusive-european-destiny-synthesis"]),
                mc("grammar", "check", "Melyik szintetizáló szerkezet fogalmazza meg a nemzet európai küldetését a legmagasabb szinten?", [
                    "végső soron elengedhetetlen a nyugati elköteleződés / mindent egybevetve az integráció a megmaradás záloga",
                    "reméljük valahogy megmaradunk itt a folyók mellett",
                    "jó lenne ha mindenki békén hagyna minket"
                ], 0, ["c1-adv-conclusive-european-destiny-synthesis"])
            ]
        }
    ]

    for l in disc_lessons:
        emit_instructional_lesson(30, "discourse", l, disc_title, disc_intro if l["num"] == 1 else None)

    # Combined World Story
    write_json(
        f"stories/world/c1/c1-{slug}-kelet-nyugat-hintapolitika.json",
        {
            "id": f"story.c1.{slug}.combined",
            "title": "Komp-ország a viharban: Hintapolitika, szuverenitás és Európa",
            "level": "C1",
            "lesson": 5,
            "order": 30,
            "type": "world",
            "estimatedMinutes": 8,
            "grammar": ["c1-adv-conclusive-european-destiny-synthesis"],
            "summary": "Átfogó geopolitikai esszé a 21. századi magyar külpolitika drámájáról: a Keleti Nyitás illúziójáról és a hintapolitikáról, a Paks II atompaktumról és a Gazprom-szerződésekről, a brüsszeli tranzakcionális vétódiplomáciáról, a kínai akkumulátorkolonizációról, valamint a mag-Európa és a keleti periféria közötti történelmi válaszútról.",
            "vocabularyTopics": [
                "Pendulum Politics, Strategic Neutrality & Euro-Atlantic Crisis",
                "Historical Crossroads: Core Europe or Eastern Periphery"
            ],
            "paragraphs": [
                {"type": "narration", "text": "Magyarország a huszonegyedik század harmadik évtizedében mélyreható geopolitikai válsággal néz szembe. A 2010 után kibontakozó 'Keleti Nyitás' és a 'gazdasági semlegesség' doktrínája azt ígérte, hogy az ország hídként kamatoztathatja fekvését a nyugati piacok és a keleti autokráciák között. A valóságban azonban e taktikai hintapolitika az ország nemzetközi szavahihetőségének összeomlásához és a transzatlanti szövetségesek teljes elidegenedéséhez vezetett."},
                {"type": "narration", "text": "A legveszélyesebb kitettséget az energetikai monokultúra jelentette: a 2014-es, versenytárgyalás nélküli Paks II megállapodás és a Gazprommal kötött titkosított gázszerződések évtizedekre Moszkvához béklyózták a hazai infrastruktúrát. Az államnak kötelessége volna szavatolnia a valós forrásdiverzifikációt, ám a politikai vezetés a háborús agresszió idején is megerősítette függőségét az orosz állami konszernektől."},
                {"type": "narration", "text": "Az Európai Unióban folytatott tranzakcionális vétódiplomácia megbénította a közös külpolitikai cselekvést: minél inkább zsarolási eszközként használta Budapest a vétójogot a befagyasztott források megszerzésére, annál mélyebb diplomáciai elszigetelődésbe süllyedt. A partnerek válasza a jogállamisági kondicionalitás szigorítása és az egyhangúsági szabály kikerülését célzó reformok felgyorsítása lett."},
                {"type": "narration", "text": "Ezzel párhuzamosan a kínai gigahitelek (Budapest–Belgrád) és a természeti erőforrásokat felemésztő akkumulátorgyárak betelepítése leleplezte az adósságcsapda-diplomácia veszélyét. Kétségkívül bebizonyosodott, hogy az ország egy idegen birodalom alacsony hozzáadott értékű, környezetszennyező hídfőállásává válik az európai piac kapujában."},
                {"type": "narration", "text": "Végső soron elengedhetetlen felismerni: mindent egybevetve Ady Endre Komp-ország allegóriája ma is a legélesebb nemzeti tükör. A kétsebességes Európa létrejötte nem tűri az ingadozást: Magyarország nem sodródhat a keleti despotizmusok kiszolgáltatott perifériájára. A nemzet jövője, jóléte és szabadsága kizárólag a mag-Európa demokratikus és jogállami közösségéhez való megingathatatlan tartozásban teljesedhet ki."}
            ]
        }
    )

    # Discourse Consolidation
    emit_consolidation_lesson(
        30,
        "discourse",
        f"c1-{slug}-consolidation",
        disc_title,
        [
            "I can diagnose tactical pendulum politics, the Eastern Opening doctrine, and the connectivity myth.",
            "I can evaluate Paks II nuclear dependence, Russian gas exposure, and transactional veto diplomacy in Brussels.",
            "I can critique Chinese battery colonization, debt traps, and formulate manifestos for Core European integration."
        ],
        [
            mc("grammar", "recognize", "Milyen szerkezettel diagnosztizálhatjuk a keleti orientációváltás külpolitikai következményeit?", [
                "a taktikai hintapolitika következtében / a keleti nyitás doktrínája nyomán",
                "hogyha messzire utazik a miniszter úr",
                "amikor új pecsétet kap az útlevél"
            ], 0, ["c1-discourse-pendulum-politics-framing"]),
            mc("grammar", "recognize", "Melyik modális kifejezés rögzíti az energetikai függetlenség kötelességét a legszigorúbban?", [
                "az államnak kötelessége garantálni a diverzifikációt / nem szolgáltathatja ki a szuverenitást",
                "szabadon lekapcsolhatják a villanyt este",
                "bármikor gyújthatnak gyertyát a szobában"
            ], 0, ["c1-modal-deontic-energy-security"]),
            match("vocabulary", "recognize", [["hintapolitika", "keleti és nyugati tömb közötti opportunista ingadozás"], ["Paks II", "orosz állami hitelből épülő nukleáris beruházás"], ["vétódiplomácia", "közös döntések blokkolása befagyasztott pénzek zsarolására"], ["adósságcsapda", "titkosított kínai hitelek révén kialakuló politikai függés"], ["mag-Európa", "a szoros integrációt megvalósító belső európai mag"]], ["c1-geopolitika-vocab"]),
            fb("vocabulary", "recall", "A nyugati és keleti szövetségi tömbök közötti ingadozó taktikázást _____ nevezzük. (pendulum politics / hintapolitikának)", "hintapolitikának", "Opportunistic oscillation between Western and Eastern alliance blocs is called pendulum politics.", ["c1-geopolitika-vocab"]),
            fb("vocabulary", "recall", "A kínai hitelek révén kialakuló stratégiai kiszolgáltatottság az _____ diplomácia. (debt-trap / adósságcsapda)", "adósságcsapda", "Strategic vulnerability unfolding via Chinese loans is debt-trap diplomacy.", ["c1-geopolitika-vocab"]),
            fb("grammar", "recall", "Az államnak kötelessége _____ a nemzeti energiaforrások valódi diverzifikációját. (guarantee / szavatolnia)", "szavatolnia", "The state has a duty to guarantee real diversification of national energy sources.", ["c1-modal-deontic-energy-security"]),
            fb("grammar", "context", "Minél többször vétóz a kormányzat, _____ mélyebb diplomáciai elszigetelődésbe süllyed. (the more / annál)", "annál", "The more times the government vetoes, the deeper diplomatic isolation it sinks into.", ["c1-adv-proportional-veto-diplomacy"]),
            fb("grammar", "context", "Végső soron _____ a nyugati demokratikus értékek megingathatatlan védelme. (indispensable / elengedhetetlen)", "elengedhetetlen", "Ultimately unwavering defense of Western democratic values is indispensable.", ["c1-adv-conclusive-european-destiny-synthesis"]),
            mc("grammar", "context", "Mi a szerepe az episztemikus kifejezéseknek az adósságcsapda leleplezésében?", [
                "Objektív elemzői súlyt adnak annak kimondására, hogy a gazdasági kolonizáció valós nemzetbiztonsági veszélyt jelent.",
                "Elnézést kérnek az építkezés zajáért.",
                "Megmutatják, mikor érkezik meg a következő tehervonat."
            ], 0, ["c1-epistemic-debt-trap-exposure"]),
            sb("grammar", "produce", ["A", "magyar", "jövő", "a", "mag-Európához", "való", "tartozásban", "teljesedhet", "ki."], ["A", "magyar", "jövő", "a", "mag-Európához", "való", "tartozásban", "teljesedhet", "ki."], "Hungarian future can be fulfilled in belonging to core Europe.", ["c1-adv-conclusive-european-destiny-synthesis"]),
            sw("production", [{"prompt": "Write a critical diagnosis of veto diplomacy using a proportional correlative.", "answer": "Minél inkább zsarolási eszközként használja a kormányzat a vétódiplomáciát az uniós fórumokon, annál inkább erodálódik Magyarország szavahihetősége, és annál mélyebb nemzetközi elszigetelődésbe taszítja a nemzetet."}], ["c1-adv-proportional-veto-diplomacy"]),
            sw("production", [{"prompt": "Formulate a concluding manifesto on Hungary's Western integration and future.", "answer": "Végső soron elengedhetetlen felismerni: mindent egybevetve Magyarország megmaradása, jóléte és szabadsága kizárólag a mag-Európa demokratikus és jogállami közösségéhez való hűséges tartozásban garantálható."}], ["c1-adv-conclusive-european-destiny-synthesis"])
        ]
    )

    print("=== Finished C1 Unit 30 ===")


if __name__ == "__main__":
    generate_unit_30()
