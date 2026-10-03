#!/usr/bin/env python3
"""
Hungarian C1 Block 4 - Unit 23 Generator:
  - Track 1 (Core): Unit 23 — "Spatial Urban Geometry, Historic Preservation & Architectural Semiotics" (c1-23)
  - Track 2 (Discourse): Unit 23 — "Urbanism in Crisis: Agglomeration Sprawl, Transit & Brownfield Renewal" (c1-varosfejlesztes)
"""

import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT))

from scripts.c1_block1.common import mc, match, fb, sb, dc, sw, write_json, emit_instructional_lesson, emit_consolidation_lesson
from scripts.c1_block4.registry_helper import register_unit


def generate_unit_23():
    print("=== Generating C1 Unit 23 ===")
    
    # Register skills & titles
    new_skills = {
        "c1-23-vocab": {"kind": "vocabulary"},
        "c1-varosfejlesztes-vocab": {"kind": "vocabulary"},
        "c1-adv-spatial-geometric-connectors": {"kind": "grammar"},
        "c1-participle-architectural-epithets": {"kind": "grammar"},
        "c1-adv-contrastive-stylistic-antithesis": {"kind": "grammar"},
        "c1-modal-aesthetic-evaluatives": {"kind": "grammar"},
        "c1-adv-scalar-urban-density": {"kind": "grammar"},
        "c1-discourse-urban-conflict-framing": {"kind": "grammar"},
        "c1-modal-statutory-urban-zoning": {"kind": "grammar"},
        "c1-adv-proportional-urban-mobility": {"kind": "grammar"},
        "c1-epistemic-urbanistic-uncertainty": {"kind": "grammar"},
        "c1-adv-conclusive-urban-synthesis": {"kind": "grammar"},
    }
    new_titles = {
        "c1-23-vocab": "reading",
        "c1-varosfejlesztes-vocab": "reading",
        "c1-adv-spatial-geometric-connectors": "spatial directional adverbials articulating complex urban architectural geometry",
        "c1-participle-architectural-epithets": "ornate participial attributive constructions conveying historic architectural aesthetics",
        "c1-adv-contrastive-stylistic-antithesis": "contrastive stylistic adverbs debating preservation versus modernist redevelopment",
        "c1-modal-aesthetic-evaluatives": "aesthetic evaluative matrix clauses critiquing urban landscape degradation",
        "c1-adv-scalar-urban-density": "scalar density adverbials measuring spatial agglomeration and overcrowding",
        "c1-discourse-urban-conflict-framing": "discourse framing markers diagnosing acute urban spatial conflicts and impasses",
        "c1-modal-statutory-urban-zoning": "deontic modal structures formulating statutory zoning and environmental planning mandates",
        "c1-adv-proportional-urban-mobility": "proportional correlative conjunctions mapping commuter sprawl and infrastructural strain",
        "c1-epistemic-urbanistic-uncertainty": "epistemic stance markers articulating demographic projections in metropolitan planning",
        "c1-adv-conclusive-urban-synthesis": "evaluative synthesis particles formulating holistic master plans for livable cities",
    }
    
    core_title = "Spatial Urban Geometry, Historic Preservation & Architectural Semiotics"
    core_stems = [f"c1-23-0{i}" for i in range(1, 6)] + ["c1-23-consolidation"]
    disc_title = "Urbanism in Crisis: Agglomeration Sprawl, Transit & Brownfield Renewal"
    disc_stems = [f"c1-varosfejlesztes-0{i}" for i in range(1, 6)] + ["c1-varosfejlesztes-consolidation"]
    
    register_unit(23, core_title, core_stems, disc_title, disc_stems, new_skills, new_titles)

    # ----------------------------------------------------
    # TRACK 1: CORE (c1-23)
    # ----------------------------------------------------
    core_intro = [
        "The urban fabric of Budapest is a layered palimpsest of architectural ambition: the grand radial boulevards and monumental historicism of the Fin-de-Siècle, Bauhaus functionalism, socialist-realist interventions, and contemporary real-estate speculation.",
        "In this unit, anchored by Szerb Antal's whimsical yet melancholy urban masterpiece 'Budapesti kalauz marslakók számára' (1935), you will master the elevated academic register of architectural semiotics, geometric spatial descriptions, aesthetic evaluative critique, and historic preservation debates at the C1 level."
    ]

    core_lessons = [
        {
            "num": 1,
            "stem": "c1-23-01",
            "title": "Urban Morphology & Spatial Geometric Adverbials",
            "grammar_title": "Spatial Directional Adverbials Articulating Complex Urban Architectural Geometry",
            "grammar_skill": "c1-adv-spatial-geometric-connectors",
            "goals": [
                "I can analyze urban morphology, radial-concentric boulevards, and spatial axes (*városszerkezet, sugárutas-körutas rendszer, látványtengely*).",
                "I can employ elevated spatial directional adverbials describing architectural geometry (*hossztengelyében elnyúlva, sugarasan szétágazva, szintkülönbséget áthidalva, merőlegesen metszve*).",
                "I can debate the urban planning legacy of the Budapest Public Works Council (Fővárosi Közmunkák Tanácsa)."
            ],
            "vocab": [
                {"lemma": "városszerkezet", "translation": "urban structure / morphology", "pos": "noun"},
                {"lemma": "sugaras-körutas rendszer", "translation": "radial-concentric ring system", "pos": "expression"},
                {"lemma": "látványtengely", "translation": "visual axis / vista", "pos": "noun"},
                {"lemma": "térfal", "translation": "spatial wall / building facade boundary", "pos": "noun"},
                {"lemma": "városszövet", "translation": "urban fabric", "pos": "noun"},
                {"lemma": "közterület-alakítás", "translation": "public realm design", "pos": "expression"},
                {"lemma": "szintkülönbség", "translation": "elevation difference", "pos": "noun"},
                {"lemma": "geometriai rendezettség", "translation": "geometric orderliness", "pos": "expression"}
            ],
            "gr_text1": "Spatial geometric adverbials articulate multi-axis urban perspectives: `hossztengelyében elnyúlva` (extending along its longitudinal axis), `sugarasan szétágazva` (branching out radially), `szintkülönbséget áthidalva` (bridging the elevation difference), `merőlegesen metszve` (intersecting perpendicularly).",
            "gr_text2": "Example: `Az Andrássy út hossztengelyében elnyúlva köti össze a belvárost a Városligettel, míg a körutak koncentrikus ívben ölelik körül a történelmi magot`.",
            "gr_table": [
                ["A sugárutak a belvárosból kiindulva sugarasan ágaznak szét a peremkerületek felé.", "Avenues starting from downtown branch out radially toward outer districts."],
                ["A Lánchíd a Duna szintkülönbségét áthidalva köti össze a hegyes Budát a lapos Pesttel.", "Chain Bridge bridging the elevation difference of the Danube connects hilly Buda with flat Pest."],
                ["A kis utcák merőlegesen metszik a főközlekedési tengelyt.", "Small streets perpendicularly intersect the main transit axis."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mit jelent a 'sugaras-körutas rendszer' Budapest városszerkezetében?", [
                    "A központból kiinduló egyenes sugárutak (pl. Andrássy út) és az azokat övező félköríves körutak (Kiskörút, Nagykörút) geometrikus hálózatát.",
                    "A villamosok forgó kerekeinek műszaki karbantartási tervét.",
                    "A Duna kör alakú mesterséges tavakká alakítását."
                ], 0, ["c1-23-vocab"]),
                fb("grammar", "controlled", "A Nagykörút hatalmas félkörívben elnyúlva, _____ metszi a sugárutakat. (perpendicularly / merőlegesen)", "merőlegesen", "The Grand Boulevard stretching in a huge semicircle perpendicularly intersects the radial avenues.", ["c1-adv-spatial-geometric-connectors"]),
                match("vocabulary", "controlled", [["városszövet", "az épületek és utcák szerves történelmi együttese"], ["látványtengely", "egy monumentális épületre néző tudatosan tervezett utcavonal"], ["szintkülönbség", "a terep magassági eltérése (pl. Buda és Pest között)"], ["térfal", "a teret határoló homlokzatok összessége"]], ["c1-23-vocab"]),
                fb("grammar", "practice", "A sikló a Várhegy meredek _____ áthidalva szállítja az utasokat. (elevation difference / szintkülönbségét)", "szintkülönbségét", "The funicular bridging the steep elevation difference of Castle Hill transports passengers.", ["c1-adv-spatial-geometric-connectors"]),
                sb("grammar", "practice", ["A", "sugárutak", "sugarasan", "ágaznak", "szét", "a", "belvárosból."], ["A", "sugárutak", "sugarasan", "ágaznak", "szét", "a", "belvárosból."], "Avenues branch out radially from the inner city.", ["c1-adv-spatial-geometric-connectors"]),
                dc("dialogue", [
                    {"speaker": "Városépítész", "text": "Hogyan szervezték meg a millenniumi Budapest tereit?"},
                    {"speaker": "Művészettörténész", "text": "A hossztengelyében elnyúló Andrássy út a Hősök tere monumentális szoborcsoportjában _____."},
                ], ["kulminál", "eltéved", "összeomlik"], 0, ["c1-adv-spatial-geometric-connectors"]),
                sw("production", [{"prompt": "Write a sentence describing an urban vista using a geometric spatial connector.", "answer": "Az Andrássy út hossztengelyében elnyúlva vezeti a tekintetet a Hősök tere monumentális emlékműve felé, tökéletes geometriai rendbe foglalva a pesti városszövetet."}], ["c1-adv-spatial-geometric-connectors"]),
                mc("grammar", "check", "Melyik kifejezés testesíti meg a magas szintű térbeli-geometrikus leírást?", [
                    "hossztengelyében elnyúlva / sugarasan szétágazva",
                    "nagyon messze van",
                    "ott áll a sarkon"
                ], 0, ["c1-adv-spatial-geometric-connectors"])
            ]
        },
        {
            "num": 2,
            "stem": "c1-23-02",
            "title": "Historicism, Fin-de-Siècle Eclecticism & Participial Epithets",
            "grammar_title": "Ornate Participial Attributive Constructions Conveying Historic Architectural Aesthetics",
            "grammar_skill": "c1-participle-architectural-epithets",
            "goals": [
                "I can analyze Fin-de-Siècle architecture, historicism, eclecticism, and Art Nouveau (*historizmus, eklektika, szecesszió, stukkódíszítés*).",
                "I can construct ornate participial attributive phrases in `-t/-tt`, `-ó/-ő`, `-va/-ve` (*eklektikusan megformált, historizáló jegyekkel felvértezett, boltívesen kiképzett, aranyozott motívumokkal ékesített*).",
                "I can evaluate the aesthetic philosophy of Ödön Lechner and Hungarian national secession."
            ],
            "vocab": [
                {"lemma": "historizmus", "translation": "historicism (architectural revivalism)", "pos": "noun"},
                {"lemma": "eklektika", "translation": "eclecticism", "pos": "noun"},
                {"lemma": "szecesszió", "translation": "Art Nouveau / Secession", "pos": "noun"},
                {"lemma": "stukkódíszítés", "translation": "stucco ornamentation", "pos": "noun"},
                {"lemma": "homlokzati tagozat", "translation": "facade articulation / molding", "pos": "expression"},
                {"lemma": "Zsolnay kerámia", "translation": "Zsolnay pyrogranite ceramic", "pos": "expression"},
                {"lemma": "kovácsoltvas kapu", "translation": "wrought-iron gate", "pos": "expression"},
                {"lemma": "műemléki érték", "translation": "monument value / heritage status", "pos": "expression"}
            ],
            "gr_text1": "Ornate participial attributes elaborate sensory and architectural details through compound pre-nominal structures: `eklektikusan megformált` (eclectically shaped), `historizáló jegyekkel felvértezett` (equipped with historicizing features), `boltívesen kiképzett` (vaultedly formed), `Zsolnay-kerámiával gazdagon díszített` (richly adorned with Zsolnay ceramic).",
            "gr_text2": "Example: `A Lechner Ödön által tervezett, népi motívumokkal gazdagon ékesített és Zsolnay-kerámiával borított Iparművészeti Múzeum a magyar nemzeti szecesszió legfőbb remekműve`.",
            "gr_table": [
                ["A boltívesen kiképzett kapualj elegáns kovácsoltvas ráccsal zárul.", "The vaultedly formed gateway closes with an elegant wrought-iron grille."],
                ["A historizáló jegyekkel felvértezett bérpaloták büszkén hirdetik a polgári gazdagságot.", "Residential palaces equipped with historicizing features proudly herald bourgeois wealth."],
                ["Az aranyozott stukkókkal díszített díszterem lélegzetelállító látványt nyújt.", "The ceremonial hall decorated with gilded stuccos provides a breathtaking sight."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mi jellemezte a budapesti 'eklektikus' és 'historizáló' építészetet a 19. század végén?", [
                    "A korábbi történelmi stílusok (reneszánsz, gótika, barokk) formaelemeinek szabad, látványos és dekoratív ötvözése a modern bérpalotákon.",
                    "A beton és műanyag kizárólagos használata díszítések nélkül.",
                    "A fák és kertek betiltása a város egész területén."
                ], 0, ["c1-23-vocab"]),
                fb("grammar", "controlled", "A Zsolnay-kerámiával gazdagon _____ tetőzet a magyar szecesszió jelképévé vált. (adorned / díszített)", "díszített", "The roof richly adorned with Zsolnay ceramic became the symbol of Hungarian Secession.", ["c1-participle-architectural-epithets"]),
                match("vocabulary", "controlled", [["historizmus", "múltbeli történelmi korok stílusait felelevenítő építészet"], ["szecesszió", "organikus, növényi formákat alkalmazó újító stílus"], ["Zsolnay kerámia", "időjárásálló, mázas pirogránit díszítőelem"], ["stukkó", "gipszből formált domborműves homlokzati dísz"]], ["c1-23-vocab"]),
                fb("grammar", "practice", "A boltívesen _____ kapualjak a pesti bérházak rejtett kincsei. (formed / kiképzett)", "kiképzett", "The vaultedly formed gateways are the hidden treasures of Pest apartment houses.", ["c1-participle-architectural-epithets"]),
                sb("grammar", "practice", ["A", "díszesen", "megformált", "homlokzatok", "lenyűgözik", "a", "sétálókat."], ["A", "díszesen", "megformált", "homlokzatok", "lenyűgözik", "a", "sétálókat."], "Ornately formed facades impress walkers.", ["c1-participle-architectural-epithets"]),
                dc("dialogue", [
                    {"speaker": "Művészettörténész", "text": "Mi teszi egyedivé a Postatakarékpénztár épületét?"},
                    {"speaker": "Idegenvezető", "text": "A népi motívumokkal gazdagon _____ homlokzat és a méhkasokat formázó tetődíszek."},
                ], ["ékesített", "elrontott", "letagadott"], 0, ["c1-participle-architectural-epithets"]),
                sw("production", [{"prompt": "Write a sentence describing an eclectic or Art Nouveau building using an ornate participial construction.", "answer": "A finom aranyozással ékesített és hullámzó növényi ornamentikával megformált szecessziós palota a pesti polgárság kifinomult esztétikai igényességének örök mementója."}], ["c1-participle-architectural-epithets"]),
                mc("grammar", "check", "Melyik szerkezet képvisel emelkedett építészeti minőségjelzői igenevet?", [
                    "Zsolnay-kerámiával gazdagon díszített / boltívesen kiképzett",
                    "tegnap felépítették a házat",
                    "gyorsan mentek fel a lépcsőn"
                ], 0, ["c1-participle-architectural-epithets"])
            ]
        },
        {
            "num": 3,
            "stem": "c1-23-03",
            "title": "Preservation vs. Modernist Redevelopment: Stylistic Antithesis",
            "grammar_title": "Contrastive Stylistic Adverbs Debating Preservation Versus Modernist Redevelopment",
            "grammar_skill": "c1-adv-contrastive-stylistic-antithesis",
            "goals": [
                "I can analyze the tension between heritage preservation, brutalist modernism, and glass-facade commercialism (*műemlékvédelem, brutalizmus, üvegpaloták, stílustörés*).",
                "I can employ contrastive stylistic antithesis adverbs (*szembeállítva... párhuzamba állítva, míg a historizáló... addig a funkcionalista, ezzel éles ellentétben*).",
                "I can debate the controversial reconstruction of the Buda Castle District (Hauszmann Program)."
            ],
            "vocab": [
                {"lemma": "műemlékvédelem", "translation": "monument preservation / heritage protection", "pos": "noun"},
                {"lemma": "stílustörés", "translation": "stylistic rupture / clash", "pos": "noun"},
                {"lemma": "funkcionalizmus", "translation": "functionalism", "pos": "noun"},
                {"lemma": "brutalizmus", "translation": "brutalist architecture", "pos": "noun"},
                {"lemma": "történeti hűség", "translation": "historical fidelity / accuracy", "pos": "expression"},
                {"lemma": "kortárs beépítés", "translation": "contemporary infill / intervention", "pos": "expression"},
                {"lemma": "építészeti disszonancia", "translation": "architectural dissonance", "pos": "expression"},
                {"lemma": "rekonstrukciós vita", "translation": "reconstruction debate", "pos": "expression"}
            ],
            "gr_text1": "Contrastive stylistic markers frame aesthetic debates between authenticity and contemporary utility: `szembeállítva... párhuzamba állítva` (contrasting with... drawing parallels with), `ezzel éles ellentétben` (in sharp contrast to this), `míg a klasszikus... addig a modern` (while the classical... yet the modern).",
            "gr_text2": "Example: `Míg a műemlékvédők a történeti hűséget és a patinás részletek megőrzését követelik, addig a befektetők ezzel éles ellentétben modern üveg-acél szerkezetekkel törnék meg a történelmi térfalat`.",
            "gr_table": [
                ["Míg a historizmus a múlt pompáját idézi, addig a modernizmus a funkció tisztaságát hirdeti.", "While historicism evokes the splendor of the past, modernism proclaims the purity of function."],
                ["Ezzel éles ellentétben a kortárs felhőkarcolók idegen testként ékelődnek a régi negyedekbe.", "In sharp contrast to this contemporary skyscrapers wedge as foreign bodies into old quarters."],
                ["A Hauszmann-program rekonstrukcióit szembeállítva a modern építészeti elvekkel mély szakmai vita bontakozott ki.", "Contrasting the reconstructions of the Hauszmann Program with modern architectural principles, deep professional debate unfolded."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mi képezi a legfőbb szakmai vitát a budai Várnegyed Hauszmann-programja körül?", [
                    "Hogy a háborúban elpusztult történelmi épületek teljes újraépítése történeti hűségnek vagy anakronisztikus díszletépítésnek tekintendő.",
                    "Hogy a Mátyás-templom tornyát le kell-e festeni pirosra.",
                    "Hogy a Várhegy gyomrában szabad-e földalatti vidámparkot nyitni."
                ], 0, ["c1-23-vocab"]),
                fb("grammar", "controlled", "Míg a műemlékvédők a megőrzést szorgalmazzák, ezzel éles _____ a beruházók a bontást választják. (contrast / ellentétben)", "ellentétben", "While preservationists urge conservation, in sharp contrast with this investors choose demolition.", ["c1-adv-contrastive-stylistic-antithesis"]),
                match("vocabulary", "controlled", [["műemlékvédelem", "az épített örökség megóvása a rombolástól"], ["stílustörés", "egymáshoz nem illő építészeti formák zavaró találkozása"], ["funkcionalizmus", "az épület célját és használhatóságát előtérbe helyező stílus"], ["kortárs beépítés", "modern épület elhelyezése történelmi környezetben"]], ["c1-23-vocab"]),
                fb("grammar", "practice", "Míg a régi homlokzatok gazdagon díszítettek, _____ a modern irodaházak rideg üvegfalakkal határoltak. (meanwhile / addig)", "addig", "While old facades are richly decorated, meanwhile modern office buildings are bounded by cold glass walls.", ["c1-adv-contrastive-stylistic-antithesis"]),
                sb("grammar", "practice", ["Ezzel", "éles", "ellentétben", "a", "modern", "építészet", "a", "funkcióra", "épít."], ["Ezzel", "éles", "ellentétben", "a", "modern", "építészet", "a", "funkcióra", "épít."], "In sharp contrast to this modern architecture builds on function.", ["c1-adv-contrastive-stylistic-antithesis"]),
                dc("dialogue", [
                    {"speaker": "Építészkritikus", "text": "Hogyan értékelhető az új üvegtorony a Duna-parton?"},
                    {"speaker": "Főépítész", "text": "Míg egyesek a fejlődés szimbólumát látják benne, addig mások szerint éles építészeti _____ teremt a klasszikus panorámával."},
                ], ["disszonanciát", "harmóniát", "békét"], 0, ["c1-adv-contrastive-stylistic-antithesis"]),
                sw("production", [{"prompt": "Write a sentence contrasting historical preservation with modernist architecture using 'Míg... addig...'.", "answer": "Míg a műemlékvédelmi szakma a történeti patina és az autentikus anyagok megőrzése mellett érvel, addig az ingatlanfejlesztők a modern funkcionalizmus jelszavával radikálisan átformálják a pesti belváros látképét."}], ["c1-adv-contrastive-stylistic-antithesis"]),
                mc("grammar", "check", "Melyik kötőszószerkezet fejez ki plasztikus stílustani szembeállítást?", [
                    "Míg a klasszikus... addig a modern / Ezzel éles ellentétben",
                    "Nemcsak szép, hanem drága is",
                    "Ezért tehát azonnal megépítették"
                ], 0, ["c1-adv-contrastive-stylistic-antithesis"])
            ]
        },
        {
            "num": 4,
            "stem": "c1-23-04",
            "title": "Architectural Semiotics & Aesthetic Evaluative Clauses",
            "grammar_title": "Aesthetic Evaluative Matrix Clauses Critiquing Urban Landscape Degradation",
            "grammar_skill": "c1-modal-aesthetic-evaluatives",
            "goals": [
                "I can analyze architectural semiotics, monumental symbolism, and urban degradation (*építészeti szemiotika, szimbolikus térfoglalás, városképi tájseb*).",
                "I can employ aesthetic evaluative matrix clauses critiquing visual degradation (*méltán tartható számon, joggal kifogásolható, vitán felül áll, hogy..., megkérdőjelezhetetlen érdeme, hogy...*).",
                "I can articulate critical judgments on public space commercialization and facade erosion."
            ],
            "vocab": [
                {"lemma": "építészeti szemiotika", "translation": "architectural semiotics", "pos": "expression"},
                {"lemma": "szimbolikus térfoglalás", "translation": "symbolic spatial appropriation", "pos": "expression"},
                {"lemma": "városképi tájseb", "translation": "townscape scar / visual wound", "pos": "expression"},
                {"lemma": "homlokzati erózió", "translation": "facade erosion / decay", "pos": "expression"},
                {"lemma": "vizuális szennyezés", "translation": "visual pollution", "pos": "expression"},
                {"lemma": "reklámfelületek elburjánzása", "translation": "proliferation of advertising surfaces", "pos": "expression"},
                {"lemma": "esztétikai minőségromlás", "translation": "aesthetic quality degradation", "pos": "expression"},
                {"lemma": "identitásképző erő", "translation": "identity-forming power", "pos": "expression"}
            ],
            "gr_text1": "Aesthetic evaluative matrix clauses frame subjective architectural criticism as authoritative, defensible artistic consensus: `méltán tartható számon` (is deservedly regarded as), `joggal kifogásolható` (is rightfully objectionable), `vitán felül áll, hogy...` (it is beyond dispute that...), `megkérdőjelezhetetlen érdeme, hogy...` (its unquestionable merit is that...).",
            "gr_text2": "Example: `Vitán felül áll, hogy a történelmi homlokzatok elhanyagolása városképi tájsebet ejtett a Nagykörúton, és joggal kifogásolható a hatalmas óriásplakátok vizuális környezetszennyezése`.",
            "gr_table": [
                ["Vitán felül áll, hogy Budapest panorámája a világörökség legféltettebb része.", "It is beyond dispute that Budapest's panorama is the most cherished part of world heritage."],
                ["Joggal kifogásolható a műemléki belső udvarok illegális átépítése.", "The illegal rebuilding of historic courtyards is rightfully objectionable."],
                ["Méltán tartható számon az Iparművészeti Múzeum a nemzeti géniusz csúcsaként.", "The Museum of Applied Arts is deservedly regarded as the pinnacle of national genius."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mit vizsgál az 'építészeti szemiotika' a városi környezetben?", [
                    "Azt, hogy az épületek formái, anyagai és térbeli elhelyezkedése milyen kulturális, társadalmi és politikai üzeneteket, szimbólumokat hordoznak.",
                    "A tégla és malter kémiai összetételének laboratóriumi elemzését.",
                    "A fűtésszámlák havi alakulását az új lakásokban."
                ], 0, ["c1-23-vocab"]),
                fb("grammar", "controlled", "Joggal _____ a történelmi belváros műemlékeinek engedély nélküli lebontása. (objectionable / kifogásolható)", "kifogásolható", "The unauthorized demolition of historic inner-city monuments is rightfully objectionable.", ["c1-modal-aesthetic-evaluatives"]),
                match("vocabulary", "controlled", [["építészeti szemiotika", "az épített formák jelentéshordozó jelrendszere"], ["szimbolikus térfoglalás", "a hatalom reprezentációja monumentális épületekkel"], ["vizuális szennyezés", "óriásplakátok és reklámok okozta városképi zavar"], ["városképi tájseb", "a történelmi utcaképbe nem illő romos vagy agresszív beépítés"]], ["c1-23-vocab"]),
                fb("grammar", "practice", "Vitán _____ áll, hogy a pesti Duna-part arculata nemzetközi védelmet érdemel. (beyond / felül)", "felül", "It is beyond dispute that the face of the Pest Danube bank deserves international protection.", ["c1-modal-aesthetic-evaluatives"]),
                sb("grammar", "practice", ["Méltán", "tartható", "számon", "a", "Lánchíd", "nemzeti", "jelképként."], ["Méltán", "tartható", "számon", "a", "Lánchíd", "nemzeti", "jelképként."], "Chain Bridge is deservedly regarded as a national symbol.", ["c1-modal-aesthetic-evaluatives"]),
                dc("dialogue", [
                    {"speaker": "Városvédő", "text": "Elfogadható-e a bérpaloták tetőterének túlépítése?"},
                    {"speaker": "Fővárosi szakértő", "text": "Joggal kifogásolható a történelmi tetőformák eltorzítása, amely súlyos esztétikai _____ okoz."},
                ], ["minőségromlást", "örömöt", "nyugalmat"], 0, ["c1-modal-aesthetic-evaluatives"]),
                sw("production", [{"prompt": "Write an evaluative sentence critiquing urban aesthetic degradation using 'Vitán felül áll, hogy...'.", "answer": "Vitán felül áll, hogy a pesti bérházak homlokzati eróziója és a reklámfelületek agresszív terjedése súlyos városképi tájsebeket ejt a történelmi belváros arculatán."}], ["c1-modal-aesthetic-evaluatives"]),
                mc("grammar", "check", "Melyik kifejezés testesíti meg az esztétikai értékítéletet és minősítést megfogalmazó főmondatot?", [
                    "Vitán felül áll, hogy... / Joggal kifogásolható",
                    "Reggel hétkor indult a vonat",
                    "Kékre festették a falat"
                ], 0, ["c1-modal-aesthetic-evaluatives"])
            ]
        },
        {
            "num": 5,
            "stem": "c1-23-05",
            "title": "Szerb Antal: Budapesti kalauz marslakók számára & Scalar Density",
            "grammar_title": "Scalar Density Adverbials Measuring Spatial Agglomeration and Overcrowding",
            "grammar_skill": "c1-adv-scalar-urban-density",
            "goals": [
                "I can analyze Szerb Antal's lyrical urban geography 'Budapesti kalauz marslakók számára' (1935) and the genius loci of Pest and Buda.",
                "I can employ scalar density adverbials measuring spatial agglomeration and overcrowding (*sűrűn, zsúfoltan, fullasztó mértékben, fojtogatóan, szellősen*).",
                "I can synthesize literary flânerie with modern spatial critique of Central European metropolises."
            ],
            "vocab": [
                {"lemma": "genius loci", "translation": "genius loci / spirit of place", "pos": "expression"},
                {"lemma": "városi flâneur", "translation": "urban flâneur / stroller", "pos": "expression"},
                {"lemma": "lakossági sűrűség", "translation": "population density", "pos": "expression"},
                {"lemma": "térbeli zsúfoltság", "translation": "spatial congestion / overcrowding", "pos": "expression"},
                {"lemma": "körfolyosós bérház", "translation": "courtyard balcony apartment building", "pos": "expression"},
                {"lemma": "városi nosztalgia", "translation": "urban nostalgia", "pos": "expression"},
                {"lemma": "szellemi topográfia", "translation": "intellectual topography", "pos": "expression"},
                {"lemma": "városlélektan", "translation": "urban psychology", "pos": "noun"}
            ],
            "gr_text1": "Scalar density adverbials calibrate urban compression, intimacy, and claustrophobia: `sűrűn` (densely), `zsúfoltan` (congestedly/crowdedly), `fullasztó mértékben` (to a suffocating degree), `fojtogatóan` (stiflingly), `szellősen` (airily/spaciously).",
            "gr_text2": "Example: `A pesti zsidónegyed szűk utcái zsúfoltan és fojtogatóan sűrűn épültek be, míg a budai hegyoldal villái szellősen húzódnak meg a fák lombjai alatt`.",
            "gr_table": [
                ["A belvárosi körfolyosós házak lakói sűrűn egymás mellett élik mindennapjaikat.", "Residents of inner-city courtyard balcony houses live their everyday lives densely next to each other."],
                ["A forgalom fojtogatóan rátelepedett a történelmi terekre és sétányokra.", "Traffic settled stiflingly onto historic squares and promenades."],
                ["A budai villanegyed szellősen beépített kertjei nyugalmat sugároznak.", "Airily built gardens of the Buda villa quarter radiate tranquility."]
            ],
            "classic_story": {
                "slug": "c1-23-szerbantal",
                "author": "Szerb Antal",
                "work": "Budapesti kalauz marslakók számára (1935)",
                "title": "Szerb Antal: Budapesti kalauz marslakók számára",
                "summary": "Szerb Antal's whimsical, melancholic, and endlessly witty 1935 essay introducing the spirit, topography, and architectural idiosyncrasies of Budapest to an imaginary visitor from Mars.",
                "characters": ["Szerb Antal", "Marslakó"],
                "paragraphs": [
                    {"type": "narration", "text": "Amikor Szerb Antal 1935-ben megírta apró remekművét, a 'Budapesti kalauz marslakók számára' című esszét, a világirodalom egyik legbájosabb és legmélyebb szerelmi vallomását tette le a magyar főváros lábai elé. Képzeletbeli sétapartnere egy marslakó, akinek nincsenek földi előítéletei, nem ismeri az emberi történelmet, és akit kézen fogva kell végigvezetni a város titkos zugaiban. Szerb Antal kalauzolása nem száraz évszámok és művészettörténeti leírások sora, hanem a városlélektan költészete."},
                    {"type": "narration", "text": "A szerző először Budára kalauzolja a földönkívüli látogatót: a Várnegyed gótikus és barokk csendjébe, a macskaköves sikátorokba, ahol az évszázados hársfák alatt megállt az idő, és a Tabán eltűnt romantikájába. Buda Szerb Antal szemében a múlt, az emlékezés, a költészet és a szellősen elterülő hegyek birodalma. Ezzel szemben Pest a dinamikus, zsúfoltan lüktető, sűrűn beépített polgári jelen: a kávéházak füstös zsongása, a Körút száguldó villamosai és az Andrássy út elegáns fasora."},
                    {"type": "narration", "text": "Szerb Antal zseniálisan ragadta meg Budapest kettős lelkét: azt a különös drámát, hogy a méltóságteljes Duna miként választja el és forrasztja mégis elválaszthatatlan egésszé a hegyvidéki mélabút és a síkvidéki nagyvárosi zsongást. A körfolyosós bérházak gangjain a lakók fojtogatóan közel élnek egymáshoz, mégis minden kapualj mögött egy-egy különös, regényes mikrokozmosz rejtőzik."},
                    {"type": "narration", "text": "A kalauz végső üzenete ma is megszólít bennünket. Szerb Antal arra tanít, hogy ne csupán sietve közlekedjünk a betonfalak között, hanem tanuljunk meg újra 'flâneurként', rácsodálkozó marslakóként sétálni a városban: észrevenni a kovácsoltvas erkélyek rejtett szépségét, beleszagolni a Duna esti párájába, és megérteni, hogy a város nem kövek és utcák halmaza, hanem az emberi lélek legmaradandóbb lenyomata."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Hogyan mutatja be Szerb Antal Budapestet a képzeletbeli marslakónak?", [
                    "Nem száraz adatokkal, hanem a budai hegyvidéki múlt és a pesti nagyvárosi zsongás költői, lélektani kettősségén keresztül.",
                    "Kizárólag a villamosjegyek árainak felsorolásával.",
                    "A parlament épületének műszaki tervrajzaival."
                ], 0, ["c1-23-vocab"]),
                fb("grammar", "controlled", "A pesti belső kerületek bérházai rendkívül _____ és szorosan épültek egymás mellé. (densely / sűrűn)", "sűrűn", "The apartment buildings of Pest's inner districts were built extremely densely and tightly next to each other.", ["c1-adv-scalar-urban-density"]),
                match("vocabulary", "controlled", [["genius loci", "egy hely, város vagy tér megfoghatatlan szellemisége"], ["városi flâneur", "a nagyváros utcáin céltalanul, de figyelmesen sétáló szemlélődő"], ["körfolyosós bérház", "belső udvarra néző nyitott folyosókkal épült pesti ház"], ["szellemi topográfia", "a terek és az irodalmi emlékek összekapcsolódása"]], ["c1-23-vocab"]),
                fb("grammar", "practice", "A forgalom zaja és a szmog _____ telepszik rá a szűk belvárosi utcákra a csúcsidőben. (stiflingly / fojtogatóan)", "fojtogatóan", "Traffic noise and smog settles stiflingly onto narrow inner-city streets during rush hour.", ["c1-adv-scalar-urban-density"]),
                sb("grammar", "practice", ["A", "budai", "hegyoldal", "szellősen", "és", "zölden", "húzódik", "meg."], ["A", "budai", "hegyoldal", "szellősen", "és", "zölden", "húzódik", "meg."], "The Buda hillside lies airily and green.", ["c1-adv-scalar-urban-density"]),
                sw("production", [{"prompt": "Write a lyrical reflection on Szerb Antal's Budapest essay using a scalar density adverb.", "answer": "Szerb Antal zseniális útmutatásával megláthatjuk, hogy míg Pest zsúfoltan és fojtogatóan lüktet a polgári sürgés-forgásban, addig a budai Vár szellősen meghúzódó sikátoraiban maga az örökkévalóság honol."}], ["c1-adv-scalar-urban-density"]),
                mc("grammar", "check", "Melyik határozószó fejez ki térbeli beépítettségi vagy népsűrűségi fokozatot?", [
                    "sűrűn / zsúfoltan / fojtogatóan",
                    "lassan sétálva",
                    "szépen felöltözve"
                ], 0, ["c1-adv-scalar-urban-density"])
            ]
        }
    ]

    for l in core_lessons:
        emit_instructional_lesson(23, "core", l, core_title, core_intro if l["num"] == 1 else None)

    # Core Consolidation Lesson
    emit_consolidation_lesson(
        23,
        "core",
        "c1-23-consolidation",
        core_title,
        [
            "I can master C1 academic vocabulary of urban morphology, Fin-de-Siècle eclecticism, and architectural semiotics.",
            "I can deploy spatial geometric connectors, ornate participial epithets, and stylistic antithesis adverbs.",
            "I can evaluate aesthetic criticism matrix clauses, scalar density metrics, and Szerb Antal's 'Budapesti kalauz'."
        ],
        [
            mc("grammar", "recognize", "Melyik mondat alkalmaz magas szintű geometriai-térbeli határozót?", [
                "Az Andrássy út hossztengelyében elnyúlva köti össze a pesti belvárost a Városligettel.",
                "A turisták leültek a padra a parkban kávézni.",
                "Mivel szép volt az idő, kimentek a Dunapartra sétálni."
            ], 0, ["c1-adv-spatial-geometric-connectors"]),
            mc("grammar", "recognize", "Melyik kifejezés testesíti meg az ékes építészeti minőségjelzői igenevet?", [
                "Zsolnay-kerámiával gazdagon díszített és boltívesen kiképzett homlokzat",
                "a kőműves gyorsan felépítette a téglafalat",
                "amikor megnyílt az új múzeum kapuja"
            ], 0, ["c1-participle-architectural-epithets"]),
            match("vocabulary", "recognize", [["historizmus", "múltbeli stílusokat felelevenítő 19. századi építészet"], ["genius loci", "a hely szelleme és egyedi hangulata"], ["városképi tájseb", "a történelmi utcaképet elcsúfító durva beavatkozás"], ["körfolyosós bérház", "belső udvarra néző gangos pesti lakóépület"], ["szintkülönbség", "a domborzat magasságbeli eltérése"]], ["c1-23-vocab"]),
            fb("vocabulary", "recall", "A hely és a város megfoghatatlan szellemiségét a latin _____ kifejezéssel írjuk le. (spirit of place / genius loci)", "genius loci", "The elusive spirit of a place and city is described with the Latin expression genius loci.", ["c1-23-vocab"]),
            fb("vocabulary", "recall", "A homlokzatok vakolatának pusztulását és leomlását építészeti _____ nevezzük. (erosion / eróziónak)", "eróziónak", "The decay and falling off of facade plaster is called architectural erosion.", ["c1-23-vocab"]),
            fb("grammar", "recall", "A bérházak udvarai _____ kiképzett kő boltívekkel támasztják alá a folyosókat. (vaultedly / boltívesen)", "boltívesen", "Courtyards of apartment houses support balconies with vaultedly formed stone arches.", ["c1-participle-architectural-epithets"]),
            fb("grammar", "context", "Míg a Várnegyed csendes, _____ a pesti belváros zsúfoltan és fojtogatóan lüktet. (meanwhile / addig)", "addig", "While the Castle District is quiet, meanwhile the Pest downtown pulsates crowdedly and stiflingly.", ["c1-adv-contrastive-stylistic-antithesis"]),
            fb("grammar", "context", "Vitán _____ áll, hogy a történelmi örökség védelme nemzetstratégiai feladat. (beyond / felül)", "felül", "It is beyond dispute that the protection of historical heritage is a national strategic task.", ["c1-modal-aesthetic-evaluatives"]),
            mc("grammar", "context", "Mi a funkciója a 'Vitán felül áll, hogy...' szerkezetnek az építészeti kritikában?", [
                "Egy esztétikai vagy örökségvédelmi álláspont autoritatív, megkérdőjelezhetetlen megalapozása.",
                "Elnézést kérés az olvasótól a véleménykülönbségek miatt.",
                "A cikk szerzőjének teljes közömbössége a téma iránt."
            ], 0, ["c1-modal-aesthetic-evaluatives"]),
            sb("grammar", "produce", ["A", "történelmi", "városkép", "a", "nemzet", "legszebb", "közös", "öröksége."], ["A", "történelmi", "városkép", "a", "nemzet", "legszebb", "közös", "öröksége."], "The historic townscape is the nation's most beautiful common heritage.", ["c1-modal-aesthetic-evaluatives"]),
            sw("production", [{"prompt": "Write a sentence diagnosing urban architectural degradation using an aesthetic evaluative clause.", "answer": "Vitán felül áll, hogy a pesti bérházak homlokzati eróziója és az óriásplakátok vizuális környezetszennyezése súlyos városképi tájsebet ejt a világörökségi panorámán."}], ["c1-modal-aesthetic-evaluatives"]),
            sw("production", [{"prompt": "Formulate a concluding thought on Szerb Antal's Budapest guide and the spirit of the city.", "answer": "Szerb Antal kalauza örök érvényű lecke arra, hogy Budapest igazi nagyszerűsége a budai hegyvidéki múlt és a pesti polgári lüktetés páratlanul harmonikus kettősségében rejlik."}], ["c1-adv-scalar-urban-density"])
        ]
    )

    # ----------------------------------------------------
    # TRACK 2: DISCOURSE (c1-varosfejlesztes)
    # ----------------------------------------------------
    slug = "varosfejlesztes"
    disc_intro = [
        "Metropolitan Budapest faces unprecedented structural crises: explosive suburban sprawl chokeholds, car dependency gridlocks, conflicts over City Park development, public transport underfunding, and brownfield gentrification.",
        "In this unit, you will master the elevated discourse of urban conflict framing, statutory zoning mandates, proportional commuter mobility, and participatory urbanism in contemporary Hungarian civic life."
    ]

    disc_lessons = [
        {
            "num": 1,
            "stem": f"c1-{slug}-01",
            "title": "Suburban Sprawl, Car Dependency & Urban Conflict Framing",
            "grammar_title": "Discourse Framing Markers Diagnosing Acute Urban Spatial Conflicts and Impasses",
            "grammar_skill": "c1-discourse-urban-conflict-framing",
            "goals": [
                "I can analyze suburban sprawl, car dependency, and metropolitan traffic gridlock (*agglomerációs szuburbanizáció, autófüggőség, közlekedési patthelyzet, kiköltözési hullám*).",
                "I can deploy discourse framing markers diagnosing acute urban spatial conflicts (*közlekedési patthelyzetet idéz elő, feszültséget generál a térhasználatban, fenntarthatatlan infrastruktúrát teremt*).",
                "I can debate the environmental and fiscal costs of dormitory towns surrounding Budapest."
            ],
            "vocab": [
                {"lemma": "szuburbanizáció", "translation": "suburbanization / sprawl", "pos": "noun"},
                {"lemma": "alvóváros", "translation": "dormitory town / bedroom community", "pos": "noun"},
                {"lemma": "autófüggőség", "translation": "car dependency", "pos": "noun"},
                {"lemma": "közlekedési patthelyzet", "translation": "traffic deadlock / impasse", "pos": "expression"},
                {"lemma": "infrastrukturális deficit", "translation": "infrastructural deficit", "pos": "expression"},
                {"lemma": "ingázási kényszer", "translation": "commuting compulsion / necessity", "pos": "expression"},
                {"lemma": "térhasználati konfliktus", "translation": "spatial use conflict", "pos": "expression"},
                {"lemma": "agglomerációs terhelés", "translation": "agglomeration burden / strain", "pos": "expression"}
            ],
            "gr_text1": "Discourse framing markers articulate systemic urban failure and mobility bottlenecks: `közlekedési patthelyzetet idéz elő` (brings about a traffic impasse), `feszültséget generál a térhasználatban` (generates tension in spatial usage), `túlterheli az alapellátást` (overburdens basic public services), `fenntarthatatlan állapotokat teremt` (creates unsustainable conditions).",
            "gr_text2": "Example: `A budapesti agglomeráció kontrollálatlan szétterülése mindennapos közlekedési patthelyzetet idéz elő a bevezető utakon, és súlyos térhasználati konfliktusokat generál a belváros lakói és az ingázók között`.",
            "gr_table": [
                ["A gépkocsik százezreinek beáramlása közlekedési patthelyzetet idéz elő a hidakon.", "The influx of hundreds of thousands of cars brings about a traffic impasse on bridges."],
                ["A kiköltözési hullám akut feszültséget generál az alvóvárosok iskolai ellátásában.", "The out-migration wave generates acute tension in dormitory towns' school provision."],
                ["A zöldterületek beépítése fenntarthatatlan terhelést ró az agglomerációs infrastruktúrára.", "The building over of green spaces imposes an unsustainable burden on agglomeration infrastructure."]
            ],
            "world_story_seg": {
                "seg_slug": "agglomeracio",
                "title": "A dugóban veszteglő aranykor: a budapesti agglomeráció válsága",
                "summary": "Exploring the morning commute from Érd, Dunakeszi, and Budaörs: three hundred thousand cars entering Budapest daily, creating environmental and infrastructural gridlocks.",
                "paragraphs": [
                    {"type": "narration", "text": "Reggel hét órakor az M3-as és M7-es autópályák bevezető szakaszain a járművek piros féklámpáinak végtelen sora ragyog a reggeli szürkületben. Érdről, Dunakesziről, Szigetszentmiklósról és Budaörsről százezrek indulnak el egyszerre gépkocsival a fővárosi munkahelyek és iskolák felé. A csendes, zöld kertvárosi idill reményében kiköltözött családok mindennapi valósága a végeláthatatlan araszolás: naponta két-három órát töltenek a kormány mögött ülve, miközben a dugó fojtogató füstje lassan beborítja a bevezető utakat."},
                    {"type": "narration", "text": "Ez a folyamat klasszikus agglomerációs válság. Az elmúlt két évtized szabályozatlan kiköltözési hulláma nemcsak Budapest belső kerületeit fosztotta meg adófizető polgáraitól, hanem fenntarthatatlan infrastruktúrát teremtett a környező településeken is. Az alvóvárosokban nincsenek bölcsődék, iskolák, orvosi rendelők és megfelelő csatornahálózat, a főváros pedig képtelen elnyelni a napi háromszázezer beáramló személyautót. A szakemberek szerint akut közlekedési patthelyzet alakult ki, amelynek feloldása nem újabb aszfaltcsíkok leterítésében, hanem a kötöttpályás elővárosi vasút radikális fejlesztésében rejlik."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Miért alakult ki válságos helyzet a budapesti agglomeráció 'alvóvárosaiban'?", [
                    "Mert a lakosságszám robbanásszerűen megnőtt, miközben az iskolák, orvosi rendelők és a közösségi közlekedés nem követték a kiköltözés ütemét.",
                    "Mert a településeken betiltották a televíziózást este nyolc óra után.",
                    "Mert a kertekben kizárólag fenyőfákat engedélyeztek ültetni."
                ], 0, ["c1-varosfejlesztes-vocab"]),
                fb("grammar", "controlled", "A százezer ingázó autó beáramlása mindennapos közlekedési _____ idéz elő a hidakon. (impasse / patthelyzetet)", "patthelyzetet", "The influx of a hundred thousand commuting cars brings about a daily traffic impasse on bridges.", ["c1-discourse-urban-conflict-framing"]),
                match("vocabulary", "controlled", [["szuburbanizáció", "a lakosság kiköltözése a városból a környező településekre"], ["alvóváros", "olyan agglomerációs település, ahonnan a lakók a központba járnak dolgozni"], ["autófüggőség", "az a helyzet, amikor a mindennapi élet autó nélkül lehetetlen"], ["közlekedési patthelyzet", "a forgalom teljes megbénulása a hálózat elégtelensége miatt"]], ["c1-varosfejlesztes-vocab"]),
                fb("grammar", "practice", "A zöldterületek beépítése súlyos feszültséget _____ a helyi lakosság körében. (generates / generál)", "generál", "The building over of green spaces generates severe tension among the local population.", ["c1-discourse-urban-conflict-framing"]),
                sb("grammar", "practice", ["A", "zsúfoltság", "patthelyzetet", "idéz", "elő", "a", "városi", "utakon."], ["A", "zsúfoltság", "patthelyzetet", "idéz", "elő", "a", "városi", "utakon."], "Congestion brings about an impasse on city roads.", ["c1-discourse-urban-conflict-framing"]),
                dc("dialogue", [
                    {"speaker": "Városkutató", "text": "Hogyan oldható meg az elővárosi forgalmi dugók problémája?"},
                    {"speaker": "Közlekedésmérnök", "text": "Az autópályák bővítése nem segít; a kötöttpályás vasút fejlesztése nélkül a patthelyzet csak _____."},
                ], ["mélyül", "megszűnik", "javul"], 0, ["c1-discourse-urban-conflict-framing"]),
                sw("production", [{"prompt": "Write a sentence diagnosing urban traffic congestion using a conflict framing marker.", "answer": "A budapesti agglomeráció robbanásszerű növekedése és a hiányos elővárosi vasúti hálózat mindennapos közlekedési patthelyzetet idéz elő a bevezető utakon, feszültséget generálva az ingázók és a belváros lakói között."}], ["c1-discourse-urban-conflict-framing"]),
                mc("grammar", "check", "Melyik kifejezés tölt be diagnosztizáló szerepet a várostervezési konfliktusok leírásakor?", [
                    "közlekedési patthelyzetet idéz elő / feszültséget generál",
                    "nagyon szép az új bicikliút",
                    "a boltban kenyeret vásárolnak"
                ], 0, ["c1-discourse-urban-conflict-framing"])
            ]
        },
        {
            "num": 2,
            "stem": f"c1-{slug}-02",
            "title": "Brownfield Reclamation, Gentrification & Statutory Zoning",
            "grammar_title": "Deontic Modal Structures Formulating Statutory Zoning and Environmental Planning Mandates",
            "grammar_skill": "c1-modal-statutory-urban-zoning",
            "goals": [
                "I can analyze brownfield reclamation, industrial relic transformation, and gentrification (*rozsdaövezeti rehabilitáció, ipari örökség, dzsentrifikáció, beépítési sűrűség*).",
                "I can employ statutory deontic modal structures formulated in municipal zoning laws (*szigorú beépítési korlátot köteles szabni, zöldfelületi arányt kell előírni, tilalmat kell fenntartani*).",
                "I can debate the displacement of working-class communities by luxury residential developments (e.g. Kopaszi-gát, Millenáris, Rozsdaövezet akciók)."
            ],
            "vocab": [
                {"lemma": "rozsdaövezet", "translation": "brownfield zone / post-industrial area", "pos": "noun"},
                {"lemma": "dzsentrifikáció", "translation": "gentrification", "pos": "noun"},
                {"lemma": "beépítési mutató", "translation": "floor area ratio / building density ratio", "pos": "expression"},
                {"lemma": "zöldfelületi arány", "translation": "green space ratio", "pos": "expression"},
                {"lemma": "övezeti besorolás", "translation": "zoning classification", "pos": "expression"},
                {"lemma": "lakhatási válság", "translation": "housing crisis / affordability crisis", "pos": "expression"},
                {"lemma": "ipari műemlék", "translation": "industrial monument / heritage", "pos": "expression"},
                {"lemma": "spekulatív ingatlanfejlesztés", "translation": "speculative real estate development", "pos": "expression"}
            ],
            "gr_text1": "Deontic modal expressions define legally binding municipal urban planning obligations: `köteles szabni` (is obligated to set), `arányt kell előírni` (a ratio must be prescribed), `tilalmat kell fenntartani` (a prohibition must be maintained), `törvényi kötelezettsége megakadályozni` (it is a statutory obligation to prevent).",
            "gr_text2": "Example: `Az önkormányzatnak szigorú beépítési korlátot köteles szabnia a rozsdaövezetek átalakításakor, és kötelező zöldfelületi arányt kell előírnia a lakóparkok beruházóinak`.",
            "gr_table": [
                ["A városvezetés szigorú beépítési korlátokat köteles előírni a Duna-parton.", "The city administration is obligated to prescribe strict building limits on the Danube bank."],
                ["Kötelező zöldfelületi arányt kell fenntartani az új lakónegyedek engedélyezésekor.", "A mandatory green space ratio must be maintained when permitting new residential quarters."],
                ["Törvényi kötelezettség a történelmi ipari műemlékek védelmének garantálása.", "It is a statutory obligation to guarantee the protection of historic industrial monuments."]
            ],
            "world_story_seg": {
                "seg_slug": "rozsdaovezet",
                "title": "A gyárkémények árnyékában: rozsdaövezetek és a dzsentrifikáció ára",
                "summary": "Investigating how former industrial zones like Csepel, Ferencváros, and Óbuda are transformed from abandoned factory complexes into elite luxury housing quarters, sparking social displacement.",
                "paragraphs": [
                    {"type": "narration", "text": "Ferencváros déli részén és Csepel északi kapujában hatalmas ipari csarnokok téglakéményei merednek az égre: a hajdani Ganz, Láng és Csepel Művek maradványai, ahol valaha munkások tízezrei gyártották a mozdonyokat, acélszerkezeteket és szerszámgépeket. Évtizedeken át elhagyatott rozsdaövezetek voltak ezek, gazverte sínekkel és betört ablakokkal. Ma azonban gőzerővel dübörög a betonozás: csillogó, modern üvegfalú lakóparkok és irodaházak nőnek ki a volt gyárak helyén, a Duna-parti panorámát kínálva a fizetőképes elitnek."},
                    {"type": "narration", "text": "A rozsdaövezeti rehabilitáció a modern várostervezés legnagyobb lehetősége, ám egyben a dzsentrifikáció legveszélyesebb terepe is. Miközben a terület megújul, az egekbe szökő négyzetméterárak miatt a történelmi munkáskerületek lakói kiszorulnak saját szülőhelyükről. A városvezetésnek törvényi kötelessége garanciákat érvényesíteni: nem elég a profitérdekeket kiszolgálni, szigorú beépítési korlátokat kell szabni, megkövetelve a megfizethető bérlakások építését és a közösségi zöldterületek védelmét a luxusnegyedek terjeszkedésével szemben."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Mit nevezünk 'dzsentrifikációnak' a volt ipari és munkáskerületekben?", [
                    "Azt a folyamatot, amikor az elhanyagolt negyedek felújítása miatt a megélhetési és lakhatási költségek megugranak, kiszorítva az eredeti, szegényebb lakosságot a gazdagabb rétegek javára.",
                    "A virágok és díszcserjék ültetését a társasházak erkélyeire.",
                    "A villamosjáratok éjszakai sűrítését hétvégén."
                ], 0, ["c1-varosfejlesztes-vocab"]),
                fb("grammar", "controlled", "A kerületi főépítésznek szigorú zöldfelületi arányt kell _____ a beruházók számára. (prescribe / előírnia)", "előírnia", "The district chief architect must prescribe a strict green space ratio for developers.", ["c1-modal-statutory-urban-zoning"]),
                match("vocabulary", "controlled", [["rozsdaövezet", "elhagyott, egykori ipari terület a város szívében"], ["dzsentrifikáció", "a szegényebb lakosság kiszorulása a felértékelődő negyedekből"], ["beépítési mutató", "a telek beépíthető alapterületének maximális törvényi aránya"], ["ipari műemlék", "megőrzésre érdemes történelmi gyárépület"]], ["c1-varosfejlesztes-vocab"]),
                fb("grammar", "practice", "Az önkormányzat köteles _____ a túlzott beépítésnek a Duna mentén. (to set / határt szabni)", "határt szabni", "The municipality is obligated to set a limit to excessive building along the Danube.", ["c1-modal-statutory-urban-zoning"]),
                sb("grammar", "practice", ["Kötelező", "zöldfelületi", "arányt", "kell", "előírni", "minden", "új", "beruházásnál."], ["Kötelező", "zöldfelületi", "arányt", "kell", "előírni", "minden", "új", "beruházásnál."], "A mandatory green space ratio must be prescribed at every new investment.", ["c1-modal-statutory-urban-zoning"]),
                dc("dialogue", [
                    {"speaker": "Lakóhelyi aktivista", "text": "Megakadályozható-e a zöldterületek elvesztése az új lakóparkoknál?"},
                    {"speaker": "Várostervező", "text": "Csak akkor, ha a szabályozási terv kógens kötelezettségként _____ a magas zöldfelületi arányt."},
                ], ["írja elő", "törli el", "felejti el"], 0, ["c1-modal-statutory-urban-zoning"]),
                sw("production", [{"prompt": "Write a sentence formulating a statutory zoning requirement for brownfield redevelopment.", "answer": "Az önkormányzatnak szigorú beépítési korlátokat köteles előírnia a volt rozsdaövezetek rehabilitációjakor, megkövetelve a közösségi zöldterületek és a megfizethető bérlakások kialakítását."}], ["c1-modal-statutory-urban-zoning"]),
                mc("grammar", "check", "Melyik kifejezés testesíti meg az urbanisztikai kötelező érvényű törvényi előírást?", [
                    "szigorú korlátot köteles szabni / arányt kell előírni",
                    "esetleg lefestheti a kerítést",
                    "ha van elég szabadideje"
                ], 0, ["c1-modal-statutory-urban-zoning"])
            ]
        },
        {
            "num": 3,
            "stem": f"c1-{slug}-03",
            "title": "Transit Battles: Bike Lanes, Railways & Proportional Mobility",
            "grammar_title": "Proportional Correlative Conjunctions Mapping Commuter Sprawl and Infrastructural Strain",
            "grammar_skill": "c1-adv-proportional-urban-mobility",
            "goals": [
                "I can analyze urban transit battles: bike lane politics, suburban train (HÉV) neglect, and micro-mobility (*kerékpáros infrastruktúra, HÉV-járműpark, mikro-mobilitás, modal split*).",
                "I can employ proportional correlative conjunctions (*minél... annál..., minél több teret adunk az autóknak... annál nagyobb dugó keletkezik*).",
                "I can critique the political polarization around active mobility and road space redistribution."
            ],
            "vocab": [
                {"lemma": "kerékpáros infrastruktúra", "translation": "cycling infrastructure", "pos": "expression"},
                {"lemma": "mikro-mobilitás", "translation": "micro-mobility (scooters, shared bikes)", "pos": "noun"},
                {"lemma": "modal split", "translation": "modal split / modal share", "pos": "expression"},
                {"lemma": "HÉV-járműpark", "translation": "suburban railway rolling stock", "pos": "expression"},
                {"lemma": "útfelület-újraelosztás", "translation": "road space redistribution", "pos": "expression"},
                {"lemma": "forgalomcsillapítás", "translation": "traffic calming", "pos": "noun"},
                {"lemma": "gyalogosbarát zóna", "translation": "pedestrian-friendly zone", "pos": "expression"},
                {"lemma": "kötöttpályás fejlesztés", "translation": "rail-bound / fixed-rail development", "pos": "expression"}
            ],
            "gr_text1": "Proportional correlatives (`minél... annál...` / `amennyivel... annyival...`) articulate systemic transport dynamics and induced demand: `Minél több sávot biztosítunk az autósoknak, annál nagyobb forgalmat vonzunk a városba, és minél jobban fejlesztjük a kerékpáros és kötöttpályás hálózatot, annál élhetőbbé válik a főváros`.",
            "gr_text2": "This structure provides rigorous syntactic tools for demonstrating that road expansion paradoxically worsens congestion while transit investment alleviates it.",
            "gr_table": [
                ["Minél sűrűbb és megbízhatóbb a HÉV-közlekedés, annál kevesebben választják a gépkocsit.", "The more frequent and reliable suburban train transit is, the fewer choose the car."],
                ["Minél bátrabban terjesztjük ki a kerékpársávokat, annál biztonságosabbá válik a közlekedés.", "The more boldly we expand bike lanes, the safer transit becomes."],
                ["Amennyivel több közteret adunk a gyalogosoknak, annyival virágzóbb lesz a környék kiskereskedelme.", "Inasmuch as we give more public space to pedestrians, by so much more flourishing will the neighborhood retail be."]
            ],
            "world_story_seg": {
                "seg_slug": "kozlekedes",
                "title": "Sávháború a körúton: kerékpárosok, autósok és a haldokló HÉV-ek",
                "summary": "Investigating Budapest's fierce mobility battles: pop-up bike lanes on the Grand Boulevard, the aging fleet of half-century-old suburban trains, and the fight for livable urban space.",
                "paragraphs": [
                    {"type": "narration", "text": "A budapesti Nagykörúton és az Üllői úton az utóbbi években éles ideológiai és várospolitikai küzdelem zajlik az aszfalt minden négyzetcentiméteréért. Amikor a főváros a pandémia idején védett kerékpársávokat jelölt ki az autós sávok rovására, az autós lobbi dühös tiltakozásba kezdett, a mindennapos forgalmi dugók növekedésével vádolva a városvezetést. Ezzel szemben a kerékpárosok és a környezetvédők tízezrei ünnepelték a történelmi áttörést: végre biztonságosan lehet tekerni a város szívében, és felcsillant a gyalogos- és biciklibarát metropolisz reménye."},
                    {"type": "narration", "text": "Ám a mobilitási forradalom féloldalas maradt. Miközben a belvárosban a mikromobilitás és a villamoshálózat virágzik, az elővárosokat kiszolgáló HÉV-vonalakon ötvenéves, recsegő-ropogó keletnémet vonatok szállítják az ingázókat, állandó műszaki hibákkal és késésekkel küzdve. A közlekedésszociológusok rámutattak a fundamentális törvényszerűségre: minél tovább halogatja az állam a kötöttpályás járműpark korszerűsítését, annál inkább az autóhasználatra kényszeríti az elővárosok lakosságát, ellehetetlenítve a fenntartható városi közlekedést."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Mit jelent a 'modal split' (közlekedési munkamegosztás) fogalma a várostervezésben?", [
                    "Azt az arányszámot, amely bemutatja, hogy a városlakók milyen százalékban választják az autót, a közösségi közlekedést, a kerékpárt vagy a gyaloglást a napi utazásaikhoz.",
                    "A villamosvezetők és buszvezetők fizetési besorolását.",
                    "A hidakon áthaladó teherautók súlykorlátozását."
                ], 0, ["c1-varosfejlesztes-vocab"]),
                fb("grammar", "controlled", "Minél jobban fejlesztjük a kötöttpályás hálózatot, _____ vonzóbbá válik a közösségi közlekedés az autósok számára. (the more / annál)", "annál", "The more we develop the rail network, the more attractive public transit becomes for drivers.", ["c1-adv-proportional-urban-mobility"]),
                match("vocabulary", "controlled", [["kerékpáros infrastruktúra", "védett biciklisávok és tárolók hálózata"], ["modal split", "a különböző közlekedési eszközök használati aránya"], ["HÉV-járműpark", "a budapesti helyiérdekű vasút elöregedett vonatai"], ["forgalomcsillapítás", "a gépjárművek sebességének és számának csökkentése a lakóutcákban"]], ["c1-varosfejlesztes-vocab"]),
                fb("grammar", "practice", "_____ több sávot építünk az autóknak, annál több dugó keletkezik a városban. (The more / Minél)", "Minél", "The more lanes we build for cars, the more traffic jams arise in the city.", ["c1-adv-proportional-urban-mobility"]),
                sb("grammar", "practice", ["Minél", "zöldebb", "a", "város,", "annál", "tisztább", "a", "levegője."], ["Minél", "zöldebb", "a", "város,", "annál", "tisztább", "a", "levegője."], "The greener the city, the cleaner its air.", ["c1-adv-proportional-urban-mobility"]),
                dc("dialogue", [
                    {"speaker": "Kerékpáros aktivista", "text": "Miért van szükség több védett biciklisávra?"},
                    {"speaker": "Urbanista", "text": "Minél nagyobb biztonságot nyújtunk a kerékpározóknak, _____ többen hagyják otthon az autójukat."},
                ], ["annál", "bár", "aligha"], 0, ["c1-adv-proportional-urban-mobility"]),
                sw("production", [{"prompt": "Write a proportional correlative sentence demonstrating induced traffic demand using 'Minél... annál...'.", "answer": "Minél több útfelületet engedünk át az autóforgalomnak a belvárosban, annál elviselhetetlenebbé válnak a forgalmi dugók és a légszennyezés a történelmi negyedekben."}], ["c1-adv-proportional-urban-mobility"]),
                mc("grammar", "check", "Melyik szerkezet fejez ki funkcionális összefüggést az infrastruktúra és az emberi döntések között?", [
                    "Minél... annál...",
                    "Talán... mégsem...",
                    "Bár... mindazonáltal..."
                ], 0, ["c1-adv-proportional-urban-mobility"])
            ]
        },
        {
            "num": 4,
            "stem": f"c1-{slug}-04",
            "title": "The Battle for City Park & Epistemic Demographic Forecasts",
            "grammar_title": "Epistemic Stance Markers Articulating Demographic Projections in Metropolitan Planning",
            "grammar_skill": "c1-epistemic-urbanistic-uncertainty",
            "goals": [
                "I can analyze the City Park debate (Liget Budapest Projekt), public green space defense, and cultural mega-projects (*Városliget, Zene Háza, Néprajzi Múzeum, zöldfelület-védelem*).",
                "I can employ calibrated epistemic stance markers evaluating urban demographic and climatic trajectories (*demográfiai modellek alapján valószínűsíthetően, előrejelzések szerint, becslések alapján feltételezhetően*).",
                "I can debate government mega-investments vs. municipal authority over municipal green parks."
            ],
            "vocab": [
                {"lemma": "zöldfelület-védelem", "translation": "green space conservation", "pos": "expression"},
                {"lemma": "kulturális negyed", "translation": "cultural quarter", "pos": "expression"},
                {"lemma": "lombkorona-borítottság", "translation": "canopy cover", "pos": "noun"},
                {"lemma": "mikroklíma-szabályozás", "translation": "microclimate regulation", "pos": "expression"},
                {"lemma": "Városliget-vita", "translation": "City Park controversy", "pos": "expression"},
                {"lemma": "civil ellenállás", "translation": "civil / grassroots resistance", "pos": "expression"},
                {"lemma": "városi hősziget-hatás", "translation": "urban heat island effect", "pos": "expression"},
                {"lemma": "rekreációs funkció", "translation": "recreational function", "pos": "expression"}
            ],
            "gr_text1": "Epistemic stance markers articulate probabilistic climate and demographic projections in urban master plans: `demográfiai modellek alapján valószínűsíthetően` (probabilistically based on demographic models), `előrejelzések szerint` (according to projections), `becslések alapján feltételezhetően` (presumably based on estimates), `várható kimenetellel` (with expected outcome).",
            "gr_text2": "Example: `Klíma- és demográfiai modellek alapján valószínűsíthetően a belvárosi hősziget-hatás fokozódásával a Városliget öreg fáinak hűtő funkciója felbecsülhetetlen túlélési tényezővé válik`.",
            "gr_table": [
                ["Előrejelzések szerint a forró kánikulai napok száma megkétszereződik a fővárosban.", "According to projections the number of sweltering heatwave days will double in the capital."],
                ["Modellek alapján valószínűsíthetően a parkok lombkoronája akár öt fokkal is csökkenti a hőséget.", "Based on models probabilistically the canopy of parks reduces heat by up to five degrees."],
                ["Becslések szerint az agglomeráció népességnövekedése újabb tízezrekkel terheli meg a várost.", "According to estimates the population growth of the agglomeration burdens the city with further tens of thousands."]
            ],
            "world_story_seg": {
                "seg_slug": "varosliget",
                "title": "Fák vagy múzeumok: a Városligetért vívott évtizedes csata",
                "summary": "Investigating the fierce conflict surrounding the Liget Budapest Project: world-renowned architecture like the House of Music vs. grassroots protests to protect every square meter of green parkland.",
                "paragraphs": [
                    {"type": "narration", "text": "A budapesti Városliget a világ első nyilvános közparkjaként született meg a tizenkilencedik század elején: a pestiek pihenőhelye, zöld menedéke és tüdeje a füstös és zajos kőváros szorításában. Amikor az elmúlt évtizedben a kormányzati akarat egy gigantikus múzeumi negyed – a Liget Budapest Projekt – felépítését határozta el a park fáinak árnyékában, az ország leghevesebb urbanisztikai és politikai konfliktusa robbant ki. Zöld aktivisták, a 'Ligetvédők' láncolták magukat a százéves platánokhoz, hogy megakadályozzák a fakivágásokat a munkagépek előtt."},
                    {"type": "narration", "text": "A vita két homlokegyenest ellenkező városfilozófia összecsapása volt. Az egyik oldalon a nemzetközi építészeti díjakat nyerő Magyar Zene Háza és az új Néprajzi Múzeum ragyogó látványa állt, amely világszínvonalú kulturális turizmust ígért. A másik oldalon viszont ott volt a klímaváltozással küzdő nagyváros elemi szorongása. Klímamodellek alapján valószínűsíthetően a pesti hősziget-hatás enyhítésére minden négyzetméter zöldfelület életmentő szükséglet; a városlakók joggal érezték úgy, hogy a beton és a múzeumok nem vehetik el az unokáik elől a tiszta levegőt és az árnyas fákat."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Miért vált a Városliget beépítése az egyik legvitatottabb környezetvédelmi üggyé Magyarországon?", [
                    "Mert a monumentális új múzeumépületek zöldfelületeket és öreg fákat vettek el egy olyan belváros mellett, amely súlyos hősziget-hatástól és zöldhiánytól szenved.",
                    "Mert a Városligeti-tó vizét sós tengervízzé akarták alakítani.",
                    "Mert a múzeumok kizárólag éjszaka tarthattak volna nyitva."
                ], 0, ["c1-varosfejlesztes-vocab"]),
                fb("grammar", "controlled", "Klíma-előrejelzések _____ a nagyvárosi hősziget-hatás elviselhetetlenné teszi a nyarakat zöldparkok nélkül. (according to / szerint)", "szerint", "According to climate projections the urban heat island effect makes summers unbearable without green parks.", ["c1-epistemic-urbanistic-uncertainty"]),
                match("vocabulary", "controlled", [["zöldfelület-védelem", "a városi parkok és fák megóvása a beépítéstől"], ["városi hősziget-hatás", "a beton és aszfalt felmelegedése miatti magasabb városi hőmérséklet"], ["lombkorona-borítottság", "a fák által árnyékolt felszín aránya"], ["civil ellenállás", "a lakosság alulról szerveződő kiállása a közterekért"]], ["c1-varosfejlesztes-vocab"]),
                fb("grammar", "practice", "Demográfiai modellek alapján _____ az agglomeráció növekedése újabb forgalmi feszültséget generál. (probabilistically / valószínűsíthetően)", "valószínűsíthetően", "Probabilistically based on demographic models the growth of the agglomeration generates further traffic tension.", ["c1-epistemic-urbanistic-uncertainty"]),
                sb("grammar", "practice", ["A", "parkok", "hűsítik", "a", "forró", "városi", "levegőt."], ["A", "parkok", "hűsítik", "a", "forró", "városi", "levegőt."], "Parks cool the hot urban air.", ["c1-epistemic-urbanistic-uncertainty"]),
                dc("dialogue", [
                    {"speaker": "Klímatudós", "text": "Hogyan alakul a főváros hőmérséklete a jövőben?"},
                    {"speaker": "Tájépítész", "text": "Előrejelzések szerint az öreg parkfák lombkoronája nélkül a belváros élhetetlenné _____ a nyár folyamán."},
                ], ["válik", "javul", "örül"], 0, ["c1-epistemic-urbanistic-uncertainty"]),
                sw("production", [{"prompt": "Write a sentence projecting urban heat island impacts using an epistemic stance marker.", "answer": "Klímamodellek alapján valószínűsíthetően a nagyvárosi hősziget-hatás drámai fokozódása várható, amely a Városligethez hasonló kiterjedt zöldfelületek védelmét elemi túlélési kérdéssé teszi."}], ["c1-epistemic-urbanistic-uncertainty"]),
                mc("grammar", "check", "Melyik kifejezés tölt be tudományosan megalapozott előrejelző funkciót a várostervezésben?", [
                    "demográfiai modellek alapján valószínűsíthetően / előrejelzések szerint",
                    "nagyon szépen süt a nap",
                    "a szomszéd tegnap mondta"
                ], 0, ["c1-epistemic-urbanistic-uncertainty"])
            ]
        },
        {
            "num": 5,
            "stem": f"c1-{slug}-05",
            "title": "The 15-Minute City, Participatory Urbanism & Conclusive Synthesis",
            "grammar_title": "Evaluative Synthesis Particles Formulating Holistic Master Plans for Livable Cities",
            "grammar_skill": "c1-adv-conclusive-urban-synthesis",
            "goals": [
                "I can formulate a master plan for the 15-minute city and participatory urbanism (*15 perces város, részvételi költségvetés, élhető metropolisz, közösségi tervezés*).",
                "I can employ elevated evaluative synthesis particles (*mindent összegezve, végső várostervezési konklúzióként, elvitathatatlanul*).",
                "I can synthesize the democratic right to the city (Henri Lefebvre) with ecological resilience in Central Europe."
            ],
            "vocab": [
                {"lemma": "15 perces város", "translation": "15-minute city", "pos": "expression"},
                {"lemma": "részvételi költségvetés", "translation": "participatory budgeting", "pos": "expression"},
                {"lemma": "élhető város", "translation": "livable city", "pos": "expression"},
                {"lemma": "közösségi tervezés", "translation": "participatory / community planning", "pos": "expression"},
                {"lemma": "városhoz való jog", "translation": "right to the city", "pos": "expression"},
                {"lemma": "decentralizált szolgáltatások", "translation": "decentralized public services", "pos": "expression"},
                {"lemma": "emberléptékű terek", "translation": "human-scale public spaces", "pos": "expression"},
                {"lemma": "ökológiai városkép", "translation": "ecological townscape", "pos": "expression"}
            ],
            "gr_text1": "Urban synthesis particles draw holistic conclusions and articulate master-planning principles: `mindent összegezve` (summarizing everything), `végső várostervezési konklúzióként` (as a final urban planning conclusion), `elvitathatatlanul` (inarguably), `összegzésképpen kijelenthető` (by way of summary it can be stated).",
            "gr_text2": "Example: `Mindent összegezve, a huszonegyedik században a város nem autópályák csomópontja, hanem az emberi találkozások tere: végső várostervezési konklúzióként az emberléptékű, tizenöt perces városmodell jelenti az egyetlen fenntartható jövőt`.",
            "gr_table": [
                ["Mindent összegezve, a városnak az emberek, nem pedig az autók igényeit kell szolgálnia.", "Summarizing everything, the city must serve the needs of people, not cars."],
                ["Végső várostervezési konklúzióként kimondható, hogy a zöldterületek védelme a klímatúlélés záloga.", "As a final urban planning conclusion it can be stated that protecting green spaces is the pledge of climate survival."],
                ["Elvitathatatlanul a részvételi demokrácia és a közösségi tervezés teszi valóban magukévá a várost a polgároknak.", "Inarguably participatory democracy and community planning make the city truly their own for citizens."]
            ],
            "world_story_seg": {
                "seg_slug": "kozossegi-varos",
                "title": "A negyedóra ígérete: emberléptékű terek és a részvételi Budapest",
                "summary": "Synthesizing transit, green spaces, and community planning into the vision of a 15-minute Budapest where every essential service is reachable on foot or by bike.",
                "paragraphs": [
                    {"type": "narration", "text": "Újlipótvárosban, a Pozsonyi út platánfái alatt egy szombat délelőtt a kávézók teraszai megteltek beszélgető emberekkel. Pár lépésre ott a pékség, a sarki zöldséges, a gyógyszertár, az iskola és a Szent István park zöld gyepe. Senki sem ül autóba; a mindennapi élet legfontosabb funkciói tíz percnyi kényelmes sétával elérhetők. Ez a '15 perces város' eleven, létező valósága, amely nem futurisztikus utópia, hanem a történelmi európai város legősibb és legbölcsebb találmánya."},
                    {"type": "narration", "text": "Mindent összegezve, Budapest jövője a részvételi városfejlesztésben és az emberléptékű terek visszahódításában rejlik. A részvételi költségvetés szavazásain a polgárok maguk dönthetnek az új közösségi kertekről, fásításokról és gyalogos sétányokról. Végső várostervezési konklúzióként kijelenthető: a modern metropolisz nem a betonóriások és az autópályák diadala, hanem egy olyan szolidáris és zöld közösség otthona, ahol minden polgár büszkén élhet a városhoz való elidegeníthetetlen jogával."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Mit jelent a '15 perces város' koncepciója az urbanisztikában?", [
                    "Azt a várostervezési modellt, amelyben a lakók mindennapi alapvető szükségletei (munka, iskola, bevásárlás, egészségügy, zöldpark) 15 perces sétával vagy biciklizéssel elérhetők.",
                    "Azt a szabályt, hogy tilos 15 percnél tovább parkolni a belvárosban.",
                    "A repülőtérre közlekedő gyorsvasút menetidejét."
                ], 0, ["c1-varosfejlesztes-vocab"]),
                fb("grammar", "controlled", "Mindent _____, az emberléptékű terek visszahódítása az élhető város záloga. (summarizing / összegezve)", "összegezve", "Summarizing everything, reclaiming human-scale spaces is the pledge of a livable city.", ["c1-adv-conclusive-urban-synthesis"]),
                match("vocabulary", "controlled", [["15 perces város", "minden szolgáltatás negyedórányi sétára való elérése"], ["részvételi költségvetés", "a városi költségvetés egy részéről közvetlenül döntő lakossági szavazás"], ["városhoz való jog", "a polgárok joga a terek alakítására és használatára"], ["emberléptékű tér", "a gyalogosok kényelmére és biztonságára tervezett környezet"]], ["c1-varosfejlesztes-vocab"]),
                fb("grammar", "practice", "Végső várostervezési _____ kijelenthető, hogy az autók egyeduralmát fel kell váltania a zöld mobilitásnak. (conclusion / konklúzióként)", "konklúzióként", "As a final urban planning conclusion it can be stated that car hegemony must be replaced by green mobility.", ["c1-adv-conclusive-urban-synthesis"]),
                sb("grammar", "practice", ["Mindent", "összegezve,", "a", "város", "a", "közösség", "közös", "otthona."], ["Mindent", "összegezve,", "a", "város", "a", "közösség", "közös", "otthona."], "Summarizing everything, the city is the community's common home.", ["c1-adv-conclusive-urban-synthesis"]),
                dc("dialogue", [
                    {"speaker": "Főépítész", "text": "Mi a fenntartható városfejlesztés legfontosabb tanulsága?"},
                    {"speaker": "Szociológus", "text": "Mindent összegezve, az emberléptékű és zöld terek biztosítása jelenti az élhető jövő egyetlen _____."},
                ], ["útját", "kudarcát", "veszélyét"], 0, ["c1-adv-conclusive-urban-synthesis"]),
                sw("production", [{"prompt": "Write a concluding policy synthesis on urban planning using 'Mindent összegezve'.", "answer": "Mindent összegezve, Budapest fenntartható jövője a tizenöt perces városmodell bátor megvalósításán, a zöldterületek feltétlen védelmén és a részvételi demokrácia megerősítésén múlik."}], ["c1-adv-conclusive-urban-synthesis"]),
                mc("grammar", "check", "Melyik kifejezés tölt be formális összegző és szintetizáló szerepet a várostervezési érvelés végén?", [
                    "Mindent összegezve / Végső várostervezési konklúzióként",
                    "A metróra várakozva",
                    "Amikor megvették a jegyet"
                ], 0, ["c1-adv-conclusive-urban-synthesis"])
            ]
        }
    ]

    for l in disc_lessons:
        emit_instructional_lesson(23, "discourse", l, disc_title, disc_intro if l["num"] == 1 else None)

    # Combined World Story
    write_json(
        ROOT / "content" / "hu" / "stories" / "world" / "c1" / f"c1-{slug}.json",
        {
            "id": f"story.c1.{slug}",
            "title": "A kővé vált jövő: agglomerációs dugók, rozsdaövezetek és a zöld Budapest",
            "level": "C1",
            "type": "world",
            "order": 23,
            "lesson": 5,
            "estimatedMinutes": 8,
            "summary": "Panoramic exploration of Budapest's urban crisis: suburban sprawl and car dependency gridlocks, brownfield reclamation and the social costs of gentrification, transit battles over pop-up bike lanes and suburban railways, the battle for City Park, and the vision of a 15-minute participatory metropolis.",
            "grammar": [
                "c1-discourse-urban-conflict-framing",
                "c1-modal-statutory-urban-zoning",
                "c1-adv-proportional-urban-mobility",
                "c1-epistemic-urbanistic-uncertainty",
                "c1-adv-conclusive-urban-synthesis"
            ],
            "vocabularyTopics": [
                "Urbanism in Crisis: Agglomeration Sprawl, Transit & Brownfield Renewal",
                "Suburban Sprawl, Car Dependency & Urban Conflict Framing",
                "Brownfield Reclamation, Gentrification & Statutory Zoning",
                "Transit Battles: Bike Lanes, Railways & Proportional Mobility",
                "The Battle for City Park & Epistemic Demographic Forecasts",
                "The 15-Minute City, Participatory Urbanism & Conclusive Synthesis"
            ],
            "paragraphs": [
                {"type": "narration", "text": "Budapest a huszonegyedik században mély urbanisztikai útkeresésen megy keresztül. A magyar főváros kivételes történelmi adottságokkal büszkélkedhet: a Duna fenséges látványtengelyével, a budai hegyek zöld koszorújával és Pest szigorú, mégis elegáns sugárutas-körutas geometriájával. Ám e történelmi díszletek mögött ma kíméletlen strukturális feszültségek feszülnek a növekvő tőkeberuházások és az élhető lakókörnyezet megőrzése között."},
                {"type": "narration", "text": "A legégetőbb kihívást az agglomeráció szétterülése és a robbanásszerű autófüggőség jelenti: az elővárosokból naponta beáramló háromszázezer személyautó mindennapos patthelyzetet idéz elő a hidakon és a belvárosban. Ezzel egy időben a volt ipari rozsdaövezetekben – Ferencvárosban és a Kopaszi-gátnál – modern üvegluxusnegyedek épülnek, ám a szigorú zöldfelületi garanciák hiányában a dzsentrifikáció kiszorítja az eredeti lakosságot, súlyosbítva a fővárosi lakhatási válságot."},
                {"type": "narration", "text": "A közterekért vívott harc a Nagykörút védett kerékpársávjainál és a Városliget beépítése körül élesedett ki leginkább. A fák árnyéka vagy a múzeumi beton közötti választás a klímaváltozás korában elemi túlélési kérdéssé vált. A klímamodellek figyelmeztetése félreérthetetlen: a pesti hősziget-hatás ellen az öreg parkok lombkoronája a leghatékonyabb védelmi pajzs, és a jövő mobilitása a kötöttpályás vasutak és az aktív közlekedés bátor fejlesztésében rejlik."},
                {"type": "narration", "text": "Mindent összegezve, Budapest nem válhat autópályák és luxusingatlanok túszává. A 15 perces város eszméje és a részvételi közösségi tervezés az egyetlen járható út ahhoz, hogy a magyar főváros megőrizze Szerb Antal által megénekelt egyedi lelkét: egy olyan metropoliszként, amely egyszerre tiszteli történelmi patináját és garantálja minden polgára számára az élhető, zöld és emberléptékű otthon szabadságát."}
            ]
        }
    )

    # Discourse Consolidation
    emit_consolidation_lesson(
        23,
        "discourse",
        f"c1-{slug}-consolidation",
        disc_title,
        [
            "I can analyze metropolitan suburbanization, transit gridlocks, and brownfield gentrification in Budapest.",
            "I can evaluate municipal zoning mandates, induced traffic demand, and green space conflicts (Liget Project).",
            "I can debate the 15-minute city master plan, participatory budgeting, and the right to the city."
        ],
        [
            mc("grammar", "recognize", "Milyen szerkezettel fejezhetünk ki éles várostervezési és közlekedési válsághelyzetet?", [
                "közlekedési patthelyzetet idéz elő / feszültséget generál a térhasználatban",
                "mivel zöldre váltott a közlekedési lámpa az úton",
                "amikor a turisták megnézték az Országházat"
            ], 0, ["c1-discourse-urban-conflict-framing"]),
            mc("grammar", "recognize", "Melyik kifejezés testesít meg törvényi övezeti kötelezettséget?", [
                "szigorú beépítési korlátot köteles szabni / zöldfelületi arányt kell előírni",
                "szabadon dönthetnek a függöny színéről a lakásban",
                "ha kedvük tartja, megnézik a tervrajzokat"
            ], 0, ["c1-modal-statutory-urban-zoning"]),
            match("vocabulary", "recognize", [["szuburbanizáció", "a lakosság kiköltözése az agglomerációba"], ["rozsdaövezet", "elhagyott egykori ipari gyárterület"], ["modal split", "a közlekedési eszközök használati megoszlása"], ["15 perces város", "minden alapfunkció negyedórányi elérhetősége"], ["részvételi költségvetés", "közvetlen lakossági döntés a városi forrásokról"]], ["c1-varosfejlesztes-vocab"]),
            fb("vocabulary", "recall", "A belvárosból a környező falvakba történő tömeges kiköltözést _____ nevezzük. (suburbanization / szuburbanizációnak)", "szuburbanizációnak", "Mass out-migration from downtown into surrounding villages is called suburbanization.", ["c1-varosfejlesztes-vocab"]),
            fb("vocabulary", "recall", "Az elhanyagolt egykori gyári területek elnevezése az urbanisztikában a _____. (brownfield / rozsdaövezet)", "rozsdaövezet", "The designation of neglected former factory areas in urbanism is brownfield.", ["c1-varosfejlesztes-vocab"]),
            fb("grammar", "recall", "A városvezetés szigorú zöldfelületi arányt köteles _____ az új negyedekben. (prescribe / előírni)", "előírni", "The city leadership is obligated to prescribe a strict green space ratio in new quarters.", ["c1-modal-statutory-urban-zoning"]),
            fb("grammar", "context", "Minél jobban fejlesztjük a kerékpáros sávokat, _____ biztonságosabbá válik a városi közlekedés. (the more / annál)", "annál", "The more we develop bike lanes, the safer urban transit becomes.", ["c1-adv-proportional-urban-mobility"]),
            fb("grammar", "context", "Mindent _____, az emberléptékű város megteremtése a 21. század legfőbb feladata. (summarizing / összegezve)", "összegezve", "Summarizing everything, creating the human-scale city is the 21st century's foremost task.", ["c1-adv-conclusive-urban-synthesis"]),
            mc("grammar", "context", "Mi a lényege a 'Minél... annál...' korrelatív szerkezetnek a közlekedéspolitikában?", [
                "Szemlélteti az indukált forgalom elvét: több autóút még nagyobb dugót, jobb tömegközlekedés pedig élhetőbb várost eredményez.",
                "Kijelenti, hogy tilos kerékpárt vásárolni.",
                "Elnézést kér az autópályák építése miatt."
            ], 0, ["c1-adv-proportional-urban-mobility"]),
            sb("grammar", "produce", ["A", "város", "minden", "polgár", "közös", "élettere."], ["A", "város", "minden", "polgár", "közös", "élettere."], "The city is every citizen's common living space.", ["c1-adv-conclusive-urban-synthesis"]),
            sw("production", [{"prompt": "Write a critical diagnosis of urban agglomeration crisis using a conflict framing marker.", "answer": "A budapesti agglomeráció kontrollálatlan szuburbanizációja mindennapos közlekedési patthelyzetet idéz elő a bevezető utakon, súlyos térhasználati konfliktusokat generálva a főváros és a hátország között."}], ["c1-discourse-urban-conflict-framing"]),
            sw("production", [{"prompt": "Formulate a concluding thought on the 15-minute city and participatory urbanism.", "answer": "Mindent összegezve, az emberléptékű tizenöt perces városmodell és a részvételi költségvetés megerősítése jelenti az egyetlen fenntartható utat Budapest élhetőségének és közösségi összetartozásának megőrzéséhez."}], ["c1-adv-conclusive-urban-synthesis"])
        ]
    )

    print("=== Finished C1 Unit 23 ===")


if __name__ == "__main__":
    generate_unit_23()
