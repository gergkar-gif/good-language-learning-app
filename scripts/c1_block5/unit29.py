#!/usr/bin/env python3
"""
Hungarian C1 Block 5 - Unit 29 Generator:
  - Track 1 (Core): Unit 29 — "Museology, Monument Preservation & National Cultural Memory" (c1-29)
  - Track 2 (Discourse): Unit 29 — "Cultural Policy Hegemony, the PKÜ Monopoly & the Plight of Independent Theatres" (c1-kulturalisorokseg)
"""

import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT))

from scripts.c1_block1.common import mc, match, fb, sb, dc, sw, write_json, emit_instructional_lesson, emit_consolidation_lesson
from scripts.c1_block5.registry_helper import register_unit


def generate_unit_29():
    print("=== Generating C1 Unit 29 ===")
    
    new_skills = {
        "c1-29-vocab": {"kind": "vocabulary"},
        "c1-kulturalisorokseg-vocab": {"kind": "vocabulary"},
        "c1-adv-museological-authenticity-provenance": {"kind": "grammar"},
        "c1-participle-monument-preservation-ethics": {"kind": "grammar"},
        "c1-adv-counter-pastiche-adversatives": {"kind": "grammar"},
        "c1-modal-teleological-canon-formation": {"kind": "grammar"},
        "c1-adv-scalar-cultural-enlightenment": {"kind": "grammar"},
        "c1-discourse-cultural-hegemony-framing": {"kind": "grammar"},
        "c1-modal-deontic-artistic-autonomy": {"kind": "grammar"},
        "c1-adv-proportional-cultural-defunding": {"kind": "grammar"},
        "c1-epistemic-ideological-canon-polarization": {"kind": "grammar"},
        "c1-adv-conclusive-cultural-renewal-synthesis": {"kind": "grammar"},
    }
    new_titles = {
        "c1-29-vocab": "reading",
        "c1-kulturalisorokseg-vocab": "reading",
        "c1-adv-museological-authenticity-provenance": "museological evaluative adverbials articulating artifact provenance and material authenticity",
        "c1-participle-monument-preservation-ethics": "complex participial structures detailing architectural restoration and heritage conservation ethics",
        "c1-adv-counter-pastiche-adversatives": "adversative connectors contrasting authentic historical layers with ahistorical pastiche reconstructions",
        "c1-modal-teleological-canon-formation": "teleological modal structures framing institutional canonization and cultural memory transmission",
        "c1-adv-scalar-cultural-enlightenment": "scalar evaluative adverbials calibrating nineteenth century public cultural institution building",
        "c1-discourse-cultural-hegemony-framing": "discourse framing markers diagnosing state cultural hegemony and ideological dominance",
        "c1-modal-deontic-artistic-autonomy": "deontic modal structures asserting creative autonomy against political patronage demands",
        "c1-adv-proportional-cultural-defunding": "proportional correlative conjunctions mapping independent sector starvation against megainstitution subsidies",
        "c1-epistemic-ideological-canon-polarization": "epistemic stance markers assessing cultural tribalism and partisan canon polarization",
        "c1-adv-conclusive-cultural-renewal-synthesis": "evaluative synthesis particles formulating manifestos for institutional pluralism and artistic freedom",
    }
    
    core_title = "Museology, Monument Preservation & National Cultural Memory"
    core_stems = [f"c1-29-0{i}" for i in range(1, 6)] + ["c1-29-consolidation"]
    disc_title = "Cultural Policy Hegemony, the PKÜ Monopoly & the Plight of Independent Theatres"
    slug = "kulturalisorokseg"
    disc_stems = [f"c1-{slug}-0{i}" for i in range(1, 6)] + [f"c1-{slug}-consolidation"]
    
    register_unit(29, core_title, core_stems, disc_title, disc_stems, new_skills, new_titles)

    # ----------------------------------------------------
    # TRACK 1: CORE (c1-29)
    # ----------------------------------------------------
    core_intro = [
        "The preservation of cultural heritage and the transmission of collective historical memory form the foundational bedrock of civilized self-awareness. From rigorous museological provenance research to international monument preservation charters, protecting our built and material heritage demands uncompromising intellectual and ethical integrity.",
        "In this unit, centered on Pulszky Ferenc's epochal memoir 'Életem és korom' (The Mission of the National Museum), you will master the elevated academic register of museology, architectural conservation ethics, the Venice Charter, canon formation theory, and cultural institutional history at the C1 level."
    ]

    core_lessons = [
        {
            "num": 1,
            "stem": "c1-29-01",
            "title": "Provenance Research & Museological Authenticity",
            "grammar_title": "Museological Evaluative Adverbials Articulating Artifact Provenance and Material Authenticity",
            "grammar_skill": "c1-adv-museological-authenticity-provenance",
            "goals": [
                "I can analyze artifact provenance, conservation science, and restitution ethics (*proveniencia, állagmegóvás, műtárgyvédelem, restitúciós eljárás*).",
                "I can deploy elevated museological adverbials evaluating authenticity (*muzeológiailag hitelesen, provenienciáját tekintve igazoltan, restaurátori szempontból reverzibilisen*).",
                "I can critique acquisition policies and deaccessioning ethics in public collections."
            ],
            "vocab": [
                {"lemma": "proveniencia", "translation": "provenance / origin of artifact", "pos": "noun"},
                {"lemma": "állagmegóvás", "translation": "preservation of condition / conservation", "pos": "noun"},
                {"lemma": "reverzibilitás", "translation": "reversibility (in restoration)", "pos": "noun"},
                {"lemma": "közgyűjtemény", "translation": "public collection / museum repository", "pos": "noun"},
                {"lemma": "restitúció", "translation": "restitution / return of cultural property", "pos": "noun"},
                {"lemma": "műtárgyvédelem", "translation": "protection of artworks and antiquities", "pos": "noun"},
                {"lemma": "dekontextualizáció", "translation": "decontextualization", "pos": "noun"},
                {"lemma": "tárgyi hitelesség", "translation": "material / artifactual authenticity", "pos": "expression"}
            ],
            "gr_text1": "Museological evaluative adverbials formulate rigorous scientific judgments regarding artifact status and preservation interventions: `muzeológiailag hitelesen` (museologically authentically), `provenienciáját tekintve igazoltan` (substantiated regarding its provenance), `restaurátori szempontból reverzibilisen` (reversibly from a conservator's perspective), `tárgytörténetileg megalapozott módon` (in an artifact-historically well-founded manner).",
            "gr_text2": "Example: `A restaurátor a freskó kiegészítését restaurátori szempontból reverzibilisen és muzeológiailag hitelesen hajtotta végre`.",
            "gr_table": [
                ["A festmény eredetét provenienciáját tekintve igazoltan állapították meg.", "The painting's origin was established in a provenance-wise verified manner."],
                ["A beavatkozás restaurátori szempontból reverzibilisen történt.", "The intervention took place reversibly from a conservator's perspective."],
                ["A kiállítás muzeológiailag hitelesen mutatja be a tárgyak kontextusát.", "The exhibition presents the artifacts' context museologically authentically."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mit jelent a 'reverzibilitás' alapelve a modern restaurálásban?", [
                    "Azt, hogy minden restaurátori beavatkozásnak és kiegészítésnek utólag, az eredeti műtárgy károsítása nélkül eltávolíthatónak kell lennie.",
                    "Azt, hogy a festményt fejjel lefelé kell felakasztani a falra.",
                    "Azt, hogy a múzeumi jegyeket vissza lehet váltani a pénztárnál."
                ], 0, ["c1-29-vocab"]),
                fb("grammar", "controlled", "A gyűjtemény szerzéstörténetét provenienciáját tekintve _____ dokumentumok igazolják. (verified / igazolt)", "igazolt", "Documents verified regarding provenance substantiate the acquisition history.", ["c1-adv-museological-authenticity-provenance"]),
                match("vocabulary", "controlled", [["proveniencia", "a műtárgy eredetének és tulajdonosainak láncolata"], ["restitúció", "jogtalanul elvett műkincsek visszaszolgáltatása"], ["állagmegóvás", "a fizikai romlás megakadályozása"], ["közgyűjtemény", "tudományos állami múzeumi raktár"]], ["c1-29-vocab"]),
                fb("grammar", "practice", "A szakértők muzeológiailag _____ módon tárták fel a leletanyagot. (authentically / hiteles)", "hiteles", "Experts uncovered the artifacts in a museologically authentic manner.", ["c1-adv-museological-authenticity-provenance"]),
                sb("grammar", "practice", ["A", "beavatkozás", "restaurátori", "szempontból", "reverzibilisen", "mentette", "meg", "a", "kódexet."], ["A", "beavatkozás", "restaurátori", "szempontból", "reverzibilisen", "mentette", "meg", "a", "kódexet."], "The intervention reversibly from a conservator's perspective saved the codex.", ["c1-adv-museological-authenticity-provenance"]),
                dc("dialogue", [
                    {"speaker": "Kurátor", "text": "Hogyan dokumentáljuk az új régészeti leletanyag restaurálását?"},
                    {"speaker": "Főrestaurátor", "text": "Kizárólag úgy, hogy minden kiegészítés restaurátori szempontból _____ és azonosítható maradjon."},
                    {"speaker": "Kurátor", "text": "Ez a nemzetközi műtárgyvédelmi etika alapja."}
                ], ["reverzibilisen", "végleg", "titokban"], 0, ["c1-adv-museological-authenticity-provenance"]),
                sw("production", [{"prompt": "Write a sentence formulating museological conservation ethics using an authenticity adverbial.", "answer": "A közgyűjtemények feladata a vitatott műkincsek provenienciáját tekintve igazolt kutatása és az állagmegóvás restaurátori szempontból reverzibilis megvalósítása."}], ["c1-adv-museological-authenticity-provenance"]),
                mc("grammar", "check", "Melyik határozói szerkezet minősíti a műtárgyvédelmi kutatást a legmagasabb szakmai szinten?", [
                    "provenienciáját tekintve igazoltan / muzeológiailag hitelesen",
                    "többé-kevésbé tetszetősen felpolírozva",
                    "jó sok festéket rákent módon"
                ], 0, ["c1-adv-museological-authenticity-provenance"])
            ]
        },
        {
            "num": 2,
            "stem": "c1-29-02",
            "title": "Monument Preservation & Architectural Conservation",
            "grammar_title": "Complex Participial Structures Detailing Architectural Restoration and Heritage Conservation Ethics",
            "grammar_skill": "c1-participle-monument-preservation-ethics",
            "goals": [
                "I can analyze monument preservation charters, historical stratification, and anastylosis (*műemlékvédelem, rétegzettség, anasztilózis, Velencei Charta*).",
                "I can construct complex participial structures detailing conservation interventions (*a történeti rétegeket tiszteletben tartó, az eredeti köveket visszahelyező, a romos falakat megóvó*).",
                "I can critique purist de-restoration versus layered historical authenticity."
            ],
            "vocab": [
                {"lemma": "műemlékvédelem", "translation": "monument protection / heritage preservation", "pos": "noun"},
                {"lemma": "anasztilózis", "translation": "anastylosis (reassembly of fallen original parts)", "pos": "noun"},
                {"lemma": "történeti rétegzettség", "translation": "historical stratification / layers of time", "pos": "expression"},
                {"lemma": "Velencei Charta", "translation": "Venice Charter (1964 monument ethics)", "pos": "expression"},
                {"lemma": "épített örökség", "translation": "built heritage / architectural heritage", "pos": "expression"},
                {"lemma": "kordokumentum", "translation": "document of the era / historical witness", "pos": "noun"},
                {"lemma": "falszövet", "translation": "masonry fabric / structural walling", "pos": "noun"},
                {"lemma": "romkonzerválás", "translation": "consolidation / preservation of ruins", "pos": "noun"}
            ],
            "gr_text1": "Complex participial structures specify delicate architectural conservation actions: `a történeti korok rétegzettségét tiszteletben tartó műemléki felújítás` (monument restoration respecting the stratification of historical eras), `az eredeti kőfaragványokat anasztilózissal visszahelyező eljárás` (procedure replacing original stone carvings through anastylosis), `a pusztulástól megóvott középkori falszövet` (medieval masonry fabric protected from decay).",
            "gr_text2": "Example: `A várrom feltárása során a későbbi korok hozzáépítéseit kordokumentumként megőrző és az eredeti töredékeket visszaépítő restaurátori iskola győzött`.",
            "gr_table": [
                ["A műemlék történeti rétegeit tiszteletben tartó tervezés a hitelesség záloga.", "Planning respecting the monument's historical layers is the guarantee of authenticity."],
                ["Az eredeti kőtöredékeket helyreállító anasztilózis a legnemesebb eljárás.", "Anastylosis restoring original stone fragments is the noblest procedure."],
                ["A romok pusztulását megállító konzerválás megőrzi a történelem tanúságtételét.", "Conservation arresting the decay of ruins preserves the testimony of history."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mi az 'anasztilózis' lényege az építészeti műemlékvédelemben?", [
                    "A leomlott, de eredetileg összetartozó építészeti elemek és kőtöredékek pontos visszahelyezése eredeti helyükre.",
                    "Egy teljes épület lebontása és helyette bevásárlóközpont építése.",
                    "Az épület homlokzatának neoncsövekkel való kivilágítása."
                ], 0, ["c1-29-vocab"]),
                fb("grammar", "controlled", "A történeti korszakok rétegzettségét _____ tartó rekonstrukció megőrzi az épület hitelességét. (respecting / tiszteletben)", "tiszteletben", "Reconstruction respecting the stratification of historical eras preserves authenticity.", ["c1-participle-monument-preservation-ethics"]),
                match("vocabulary", "controlled", [["anasztilózis", "leomlott eredeti kövek visszaépítése"], ["Velencei Charta", "a műemlékvédelem nemzetközi etikai alapdokumentuma"], ["történeti rétegzettség", "az évszázadok során egymásra rakódott építési fázisok"], ["kordokumentum", "a történelem valós tanúságát hordozó épületrész"]], ["c1-29-vocab"]),
                fb("grammar", "practice", "A leomlott oszlopokat anasztilózissal _____ szakemberek kerülték a hipotetikus pótlást. (restoring / helyreállító)", "helyreállító", "Experts restoring fallen columns through anastylosis avoided hypothetical substitution.", ["c1-participle-monument-preservation-ethics"]),
                sb("grammar", "practice", ["A", "rétegeket", "tiszteletben", "tartó", "felújítás", "óvja", "a", "múltat."], ["A", "rétegeket", "tiszteletben", "tartó", "felújítás", "óvja", "a", "múltat."], "Restoration respecting the layers protects the past.", ["c1-participle-monument-preservation-ethics"]),
                dc("dialogue", [
                    {"speaker": "Építészettörténész", "text": "Hogyan nyúljunk a gótikus templom barokk oltárához és toronysisakjához?"},
                    {"speaker": "Műemlékes", "text": "Kizárólag a későbbi korok hozzáépítéseit kordokumentumként _____ és tisztelő szemlélettel."},
                    {"speaker": "Építészettörténész", "text": "Így kerülhetjük el a tizenkilencedik századi purizmus hibáit."}
                ], ["megőrző", "leromboló", "eltakaró"], 0, ["c1-participle-monument-preservation-ethics"]),
                sw("production", [{"prompt": "Write a sentence detailing monument preservation ethics using a participial construction.", "answer": "A történeti rétegeket tiszteletben tartó és az elpusztult részleteket analógiás másolatok helyett anasztilózissal megőrző építészet a Velencei Charta legszebb szellemiségét követi."}], ["c1-participle-monument-preservation-ethics"]),
                mc("grammar", "check", "Melyik szerkezet írja le a műemléki hitelesség tiszteletét a legszakszerűbben?", [
                    "a történeti rétegzettséget tiszteletben tartó és a kordokumentumokat megőrző",
                    "egy szép fényes új vakolattal lefedett",
                    "gyorsan felhúzott betonfal"
                ], 0, ["c1-participle-monument-preservation-ethics"])
            ]
        },
        {
            "num": 3,
            "stem": "c1-29-03",
            "title": "Historical Authenticity vs. Ahistorical Pastiche",
            "grammar_title": "Adversative Connectors Contrasting Authentic Historical Layers with Ahistorical Pastiche Reconstructions",
            "grammar_skill": "c1-adv-counter-pastiche-adversatives",
            "goals": [
                "I can critique historical revisionism in architecture, Disneyfication, and concrete-core pastiche (*pastiche rekonstrukció, historizáló kulissza, hamis kontinuitás, purista bontás*).",
                "I can deploy elevated adversative connectors contrasting genuine material history with fake facadism (*a vasbeton vázra húzott historizáló díszletekkel szemben a valóságban, nemhogy nem hiteles az analógiás visszaépítés, hanem éppen meghamisítja a történelmet, mindazonáltal elfedik a múlt traumáit*).",
                "I can debate the ethics of rebuilding destroyed historical quarters in contemporary urbanism."
            ],
            "vocab": [
                {"lemma": "pastiche", "translation": "pastiche / ahistorical stylistic imitation", "pos": "noun"},
                {"lemma": "kulisszaépítészet", "translation": "facadism / stage-set architecture", "pos": "expression"},
                {"lemma": "hamis kontinuitás", "translation": "false continuity / historical illusion", "pos": "expression"},
                {"lemma": "purizmus", "translation": "purism (dogmatic stripping of later eras)", "pos": "noun"},
                {"lemma": "autenticitás", "translation": "authenticity", "pos": "noun"},
                {"lemma": "díszletszerűség", "translation": "scenic artificiality / theatricality", "pos": "noun"},
                {"lemma": "történelemhamisítás", "translation": "falsification of history", "pos": "noun"},
                {"lemma": "traumanyom", "translation": "trace of historical trauma / scar", "pos": "noun"}
            ],
            "gr_text1": "Adversative connectors establish critical demarcation between authentic material history and nostalgic pastiche decors: `a vasbeton magra húzott gipszkulisszákkal szemben a hiteles műemlék` (in contrast with plaster decors drawn over reinforced concrete cores the authentic monument), `nemhogy nem őrzi meg a múltat a historizáló másolat, hanem éppen eltörli a trauma történeti nyomait` (far from the historicist replica preserving the past, but rather erases historical traces of trauma), `mindazonáltal díszletként funkcionál a valós emlékezet helyett` (nevertheless functions as decor instead of real memory).",
            "gr_text2": "Example: `A romantikus kulisszaépítészettel szemben a valóságban a romok méltóságteljes konzerválása tiszteletben tartja a történelem valódi folytonosságát`.",
            "gr_table": [
                ["A díszletszerű rekonstrukcióval szemben a valóságban a romok hiteles kordokumentumok.", "In contrast with scenic reconstruction in reality ruins are authentic documents of the era."],
                ["A visszaépítés nemhogy nem tudományos, hanem éppen hamis kontinuitást hazudik.", "Rebuilding is far from scientific; on the contrary, it lies a false continuity."],
                ["A modern vasbeton mag mindazonáltal megfosztja az épületet az autenticitástól.", "The modern concrete core nevertheless strips the building of authenticity."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mit nevez az építészetelmélet 'pastiche' (kulisszaépítészet) jelenségnek?", [
                    "A történeti korszakok stílusjegyeinek felületes másolását modern anyagokon (pl. vasbetonon), amely a hitelesség látszatát kelti, de nélkülözi a történeti anyag valódiságát.",
                    "Egy speciális olasz tésztafélét a múzeumi kávézóban.",
                    "A középkori templomok harangozási rendjét."
                ], 0, ["c1-29-vocab"]),
                fb("grammar", "controlled", "A gipszdíszletekkel szemben a valóságban a valódi műemlék _____ tanúságtételt hordoz. (authentic / hiteles)", "hiteles", "In contrast with plaster decors in reality an authentic monument carries genuine testimony.", ["c1-adv-counter-pastiche-adversatives"]),
                match("vocabulary", "controlled", [["pastiche", "stílusutánzat, elméleti mélység nélküli díszlet"], ["kulisszaépítészet", "modern szerkezetre húzott historizáló álhomlokzat"], ["hamis kontinuitás", "a történelmi tragédiák és törések elfedése másolatokkal"], ["traumanyom", "a háborús pusztítás mementójaként megmaradt sérülés"]], ["c1-29-vocab"]),
                fb("grammar", "practice", "A másolatok építése nemhogy nem őrzi a múltat, _____ éppen elhazudja a történelem töréseit. (rather / hanem)", "hanem", "Building replicas is far from preserving the past; on the contrary, it lies away history's ruptures.", ["c1-adv-counter-pastiche-adversatives"]),
                sb("grammar", "practice", ["A", "pastiche", "díszlet", "eltörli", "a", "történelem", "valós", "traumanyomait."], ["A", "pastiche", "díszlet", "eltörli", "a", "történelem", "valós", "traumanyomait."], "The pastiche decor erases the real trauma traces of history.", ["c1-adv-counter-pastiche-adversatives"]),
                dc("dialogue", [
                    {"speaker": "Urbanista", "text": "Miért bírálják a nemzetközi szakemberek a háború előtti minisztériumi paloták visszaépítését a Várban?"},
                    {"speaker": "Kritikus", "text": "Mert a vasbeton magra húzott historizáló díszletekkel szemben a valóságban ez nem más, mint történelemhamisító _____."},
                    {"speaker": "Urbanista", "text": "Ami elhiteti a látogatóval, mintha a huszadik század tragédiái meg sem történtek volna."}
                ], ["pastiche", "anasztilózis", "állagmegóvás"], 0, ["c1-adv-counter-pastiche-adversatives"]),
                sw("production", [{"prompt": "Write a critique of scenic facadism using an adversative connector.", "answer": "A vasbeton vázra húzott historizáló homlokzatokkal szemben a valóságban a hiteles műemlékvédelem megőrzi az idő rétegeit, és elutasítja a hamis kontinuitást sugalló pastiche díszleteket."}], ["c1-adv-counter-pastiche-adversatives"]),
                mc("grammar", "check", "Melyik ellentétes szerkezet leplezi le a történetietlen rekonstrukciókat a leghatásosabban?", [
                    "a historizáló díszletekkel szemben a valóságban... nemhogy nem hiteles, hanem éppen meghamisítja a múltat",
                    "ha süt a nap, szépen ragyog a torony",
                    "tetszik a turistáknak a friss festék"
                ], 0, ["c1-adv-counter-pastiche-adversatives"])
            ]
        },
        {
            "num": 4,
            "stem": "c1-29-04",
            "title": "Institutional Canon Formation & Cultural Memory",
            "grammar_title": "Teleological Modal Structures Framing Institutional Canonization and Cultural Memory Transmission",
            "grammar_skill": "c1-modal-teleological-canon-formation",
            "goals": [
                "I can analyze collective memory theory (Halbwachs, Assmann), canon formation, and symbolic space appropriation (*kollektív emlékezet, kánonképzés, szimbolikus tér, emlékezetpolitika*).",
                "I can deploy teleological modal structures expressing institutional memory goals (*avégből kell fenntartani a közös kánont, hogy a nemzeti identitás ne porladjon szét, abból a célból hozzák létre az emlékhelyeket, hogy rögzítsék a történelmi konszenzust*).",
                "I can critique political instrumentalization of national pantheons."
            ],
            "vocab": [
                {"lemma": "kánonképzés", "translation": "canon formation", "pos": "noun"},
                {"lemma": "kollektív emlékezet", "translation": "collective memory", "pos": "expression"},
                {"lemma": "szimbolikus tér", "translation": "symbolic space / commemorative locus", "pos": "expression"},
                {"lemma": "emlékezetpolitika", "translation": "politics of memory", "pos": "noun"},
                {"lemma": "nemzeti panteon", "translation": "national pantheon", "pos": "expression"},
                {"lemma": "kanonizáció", "translation": "canonization / institutional enshrinement", "pos": "noun"},
                {"lemma": "identitásképzés", "translation": "identity construction", "pos": "noun"},
                {"lemma": "történelmi felejtés", "translation": "historical amnesia / induced forgetting", "pos": "expression"}
            ],
            "gr_text1": "Teleological modal structures formulate deliberate institutional objectives in cultural memory transmission: `avégből kell ápolni a kulturális kánont, hogy a közösség megőrizze szellemi folytonosságát` (it must be nurtured to the end that the community preserve its spiritual continuity), `abból a célból hozzák létre az emlékhelyeket, hogy a jövő nemzedékek megértsék a szabadság árát` (memorials are established with the goal that future generations understand the price of freedom), `azért szükséges a kritikai kánonvizsgálat, nehogy a dogma felülírja a valóságot` (critical canon scrutiny is necessary lest dogma overwrite reality).",
            "gr_text2": "Example: `Az állami emlékezetpolitika abból a célból sajátítja ki a szimbolikus tereket, hogy a múlt szelektív felidézésével igazolja jelenkori hatalmi legitimációját`.",
            "gr_table": [
                ["Avégből kell védeni a kánont, hogy a nemzeti kultúra ne váljon provinciálissá.", "The canon must be protected to the end that national culture not become provincial."],
                ["Abból a célból állítanak emlékműveket, hogy alakítsák a kollektív emlékezetet.", "Monuments are erected with the goal of shaping collective memory."],
                ["Azért szükséges a nyitott kánon, hogy minden generáció megtalálja saját válaszait.", "An open canon is necessary so that every generation finds its own answers."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Hogyan határozza meg Jan Assmann a 'kulturális emlékezet' fogalmát?", [
                    "Azon szövegek, rítusok, emlékhelyek és műalkotások intézményesült összességeként, amelyek fenntartják a társadalom közös identitását évszázadokon át.",
                    "A számítógépek merevlemezének tárolókapacitásaként.",
                    "A diákok által a vizsgák előtt bemagolt évszámokként."
                ], 0, ["c1-29-vocab"]),
                fb("grammar", "controlled", "Az emlékhelyeket abból a _____ létesítik, hogy fenntartsák a kollektív emlékezetet. (goal / célból)", "célból", "Memorial sites are established with the goal of maintaining collective memory.", ["c1-modal-teleological-canon-formation"]),
                match("vocabulary", "controlled", [["kánonképzés", "művek mértékadóvá emelése az oktatásban és közbeszédben"], ["szimbolikus tér", "politikai reprezentációra és emlékezésre szolgáló köztér"], ["emlékezetpolitika", "a múlt állami szintű tudatos formálása"], ["nemzeti panteon", "a történelem legnagyobbnak ítélt alakjainak köre"]], ["c1-29-vocab"]),
                fb("grammar", "practice", "Avégből kell kutatni a múltat, _____ elkerüljük az önfelmentő történelmi mítoszokat. (that / hogy)", "hogy", "The past must be researched to the end that we avoid self-exculpatory historical myths.", ["c1-modal-teleological-canon-formation"]),
                sb("grammar", "practice", ["A", "szimbolikus", "tereket", "a", "hatalmi", "legitimáció", "céljából", "formálják."], ["A", "szimbolikus", "tereket", "a", "hatalmi", "legitimáció", "céljából", "formálják."], "Symbolic spaces are shaped for the goal of power legitimation.", ["c1-modal-teleological-canon-formation"]),
                dc("dialogue", [
                    {"speaker": "Kultúraszociológus", "text": "Miért olyan hevesek a kánonviták a tankönyvek és irodalmi antológiák körül?"},
                    {"speaker": "Irodalomtörténész", "text": "Mert avégből zajlik a harc a szerzők beválogatásáért, _____ a hatalom meghatározhassa a jövő generációk világképét."},
                    {"speaker": "Kultúraszociológus", "text": "A kánon tehát sohasem ártatlan esztétikai lista, hanem hatalmi kérdés."}
                ], ["hogy", "mert", "ha"], 0, ["c1-modal-teleological-canon-formation"]),
                sw("production", [{"prompt": "Write a sentence formulating cultural memory preservation using a teleological modal structure.", "answer": "Az államnak abból a célból kell támogatnia a független közgyűjteményeket, hogy a nemzeti kánon ne politikai jelszavakká silányuljon, hanem a szellemi szabadság eleven forrása maradjon."}], ["c1-modal-teleological-canon-formation"]),
                mc("grammar", "check", "Melyik modális célszerkezet ragadja meg a kánonképzés teleológiáját a legpontosabban?", [
                    "avégből kell ápolni a közös kánont, hogy a társadalmi integráció megmaradjon",
                    "jó lenne ha mindenki olvasna verseket délután",
                    "néha felolvasunk a könyvből"
                ], 0, ["c1-modal-teleological-canon-formation"])
            ]
        },
        {
            "num": 5,
            "stem": "c1-29-05",
            "title": "Pulszky Ferenc: The Mission of the National Museum",
            "grammar_title": "Scalar Evaluative Adverbials Calibrating Nineteenth Century Public Cultural Institution Building",
            "grammar_skill": "c1-adv-scalar-cultural-enlightenment",
            "goals": [
                "I can analyze Pulszky Ferenc's memoir, 19th-century liberal institution building, and museum ethics (*közművelődés, nemzeti önöntudat kútfeje, közkincs, felvilágosult polgárosodás*).",
                "I can deploy scalar evaluative adverbials calibrating civilizational achievement (*művelődéstörténetileg felbecsülhetetlen mértékben, intézményteremtő módon, a polgári szabadságot alapjaiban kiterjesztve*).",
                "I can synthesize the role of public museums in democratic statehood."
            ],
            "vocab": [
                {"lemma": "közművelődés", "translation": "public cultural education / civic enlightenment", "pos": "noun"},
                {"lemma": "kútfej", "translation": "springhead / vital source", "pos": "noun"},
                {"lemma": "közkincs", "translation": "public treasure / common national asset", "pos": "noun"},
                {"lemma": "intézményteremtés", "translation": "institution building", "pos": "noun"},
                {"lemma": "felvilágosult polgár", "translation": "enlightened citizen", "pos": "expression"},
                {"lemma": "nemzeti önérzet", "translation": "national dignity / self-esteem", "pos": "noun"},
                {"lemma": "méltóságteljes", "translation": "dignified / stately", "pos": "adjective"},
                {"lemma": "demokratizálódás", "translation": "democratization of culture", "pos": "noun"}
            ],
            "gr_text1": "Scalar evaluative adverbials calibrate the monumental scale of cultural institution-building: `művelődéstörténetileg felbecsülhetetlen mértékben` (to an inestimable degree in cultural history), `intézményteremtő szempontból korszakalkotó módon` (in an epoch-making manner from an institutional standpoint), `a polgári műveltséget alapjaiban megerősítve` (fundamentally consolidating civic culture), `a tudományosság szigorát maradéktalanul érvényesítve` (flawlessly asserting the rigor of scholarship).",
            "gr_text2": "Example: `Pulszky Ferenc művelődéstörténetileg felbecsülhetetlen mértékben formálta át a Nemzeti Múzeumot a nemzet eleven lelkiismeretévé`.",
            "gr_table": [
                ["A múzeum megnyitása művelődéstörténetileg felbecsülhetetlen mértékben hatott a nemzetre.", "Opening the museum impacted the nation to an inestimable degree in cultural history."],
                ["Pulszky intézményteremtő módon alapozta meg a hazai régészetet.", "Pulszky founded domestic archaeology in an institution-creating manner."],
                ["A polgári szabadságot alapjaiban megerősítve vált a művészet közkinccsé.", "Fundamentally reinforcing civic freedom art became a common treasure."]
            ],
            "classic_story": {
                "slug": "pulszky-nemzeti-muzeum",
                "title": "A Nemzeti Múzeum hivatása",
                "author": "Pulszky Ferenc",
                "work": "A Nemzeti Múzeum hivatása (Életem és korom, 1880)",
                "summary": "Pulszky Ferenc, a reformkor és az 1848-as szabadságharc emigráns diplomatája, majd a kiegyezést követően a Magyar Nemzeti Múzeum legendás főigazgatója volt. Emlékirataiban megörökíti a magyar közgyűjteményi rendszer megteremtésének küzdelmeit. Hitvallása szerint a múzeum nem az arisztokratikus szeszély halotti kamrája és nem a hatalom pompázó kulisszája, hanem a nemzet eleven öntudatának éltető kútfeje, amely a polgári szabadság és a tudományos igazság fundamentumaként áll nyitva minden polgár előtt.",
                "characters": ["Pulszky Ferenc, a múzeumigazgató és tudós polgár"],
                "paragraphs": [
                    {"type": "narration", "text": "Mikor a Nemzeti Múzeum vezetését átvettem, nem csupán az épület falai közt felhalmozott ritkaságok számbavétele várt reám, hanem egy sokkalta súlyosabb eszmei kötelezettség: tudatosítani a honi közvéleményben, hogy e gyűjtemény nem a főúri szeszély és a magánkedvtelés halotti kamrája, hanem a nemzet élő lelkiismerete."},
                    {"type": "dialogue", "speaker": "Pulszky Ferenc", "text": "A műkincs azon szellemi vívmányok megtestesülése, melyek által egy nép igazolja helyét a művelt emberiség panteonjában. Ha elhanyagoljuk emlékeinket, saját gyökereinket száradni engedjük el, s akkor bármily gazdag legyen is az államkincstár, szellemileg koldusokká válunk!"},
                    {"type": "narration", "text": "A restaurálás során a szigorú tudományos aszkézist vallottam: ami töredék maradt ránk, azt töredékként kell tisztelnünk. A hiányt beismerni nem vereség, hanem a történeti igazság iránti alázat megnyilvánulása. A restaurátor keze ne akarjon teremtőbb lenni az eredeti mesternél; feladata az állag megmentése, nem pedig a múlt kozmetikázása."},
                    {"type": "narration", "text": "Pulszky Ferenc művelődéstörténetileg felbecsülhetetlen mértékben tárta szélesre a múzeum kapuit: midőn a polgár belép e termekbe, nem alattvalónak érzi magát, hanem felelős polgárnak, kinek része van a közös örökségben. Ez a múzeum valódi alkotmányos küldetése."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Hogyan fogalmazza meg Pulszky Ferenc a Nemzeti Múzeum valódi hivatását?", [
                    "Nem főúri halotti kamraként, hanem a nemzet eleven lelkiismereteként és a polgári öntudat éltető forrásaként.",
                    "Kizárólag aranytartalékok őrzésére szolgáló kincstárként.",
                    "Olyan bérpalotaként, amely szobákat ad ki utazóknak."
                ], 0, ["c1-29-vocab"]),
                fb("grammar", "controlled", "Pulszky reformjai művelődéstörténetileg _____ mértékben járultak hozzá a polgárosodáshoz. (inestimable / felbecsülhetetlen)", "felbecsülhetetlen", "Pulszky's reforms to an inestimable degree contributed to civic development.", ["c1-adv-scalar-cultural-enlightenment"]),
                match("vocabulary", "controlled", [["kútfej", "éltető forrás, eredet"], ["közkincs", "minden polgárt megillető kulturális vagyon"], ["intézményteremtés", "maradandó tudományos és oktatási alapok lerakása"], ["közművelődés", "a társadalom széles rétegeinek szellemi felemelése"]], ["c1-29-vocab"]),
                fb("grammar", "practice", "A Nemzeti Múzeum intézményteremtő módon, a polgári szabadságot alapjaiban _____ vált a nemzet központjává. (reinforcing / megerősítve)", "megerősítve", "The National Museum, fundamentally reinforcing civic liberty, became the nation's center.", ["c1-adv-scalar-cultural-enlightenment"]),
                sb("grammar", "practice", ["A", "múzeum", "a", "nemzeti", "öntudat", "éltető", "kútfeje."], ["A", "múzeum", "a", "nemzeti", "öntudat", "éltető", "kútfeje."], "The museum is the vital springhead of national consciousness.", ["c1-adv-scalar-cultural-enlightenment"]),
                mc("reading", "context", "Mi volt Pulszky restaurátori alapelve a klasszikus leletek kezelésében?", [
                    "A töredékek alázatos tisztelete a hiú, megtévesztő kiegészítések és a történetietlen kozmetikázás helyett.",
                    "Minden törött szobor kidobása a szemétbe.",
                    "A hiányzó részek tetszőleges gipszmásolatokkal való pótlása."
                ], 0, ["c1-29-vocab"]),
                sw("production", [{"prompt": "Write a reflection on Pulszky Ferenc's museum ethics using a scalar evaluative adverbial.", "answer": "Pulszky Ferenc művelődéstörténetileg felbecsülhetetlen mértékben alapozta meg a magyar közgyűjteményi etikát, bebizonyítva, hogy a tudományos hitelesség és a közkincsek demokratizálása a polgári szabadság legfőbb záloga."}], ["c1-adv-scalar-cultural-enlightenment"]),
                mc("grammar", "check", "Melyik határozó fejezi ki a kulturális fejlődés léptékét a legemelkedettebb stílusban?", [
                    "művelődéstörténetileg felbecsülhetetlen mértékben / a polgári szabadságot alapjaiban kiterjesztve",
                    "elég sok régi tárgyat felhalmozva",
                    "szép rendben a polcokra rakva"
                ], 0, ["c1-adv-scalar-cultural-enlightenment"])
            ]
        }
    ]

    for l in core_lessons:
        emit_instructional_lesson(29, "core", l, core_title, core_intro if l["num"] == 1 else None)

    # Core Consolidation Lesson
    emit_consolidation_lesson(
        29,
        "core",
        "c1-29-consolidation",
        core_title,
        [
            "I can master the academic vocabulary of museology, provenance research, and monument preservation.",
            "I can employ museological authenticity adverbials, participial conservation structures, and counter-pastiche adversatives.",
            "I can analyze teleological canon formation and synthesize Pulszky Ferenc's public cultural enlightenment ethos."
        ],
        [
            mc("grammar", "recognize", "Melyik kifejezés minősíti szakszerűen a műtárgyak szerzéstörténetének kutatását?", [
                "provenienciáját tekintve igazoltan / muzeológiailag hitelesen",
                "szép régi képeket nézegetve a falon",
                "hogyha megkérdezzük az eladót a piacon"
            ], 0, ["c1-adv-museological-authenticity-provenance"]),
            mc("grammar", "recognize", "Milyen szerkezettel fejezhetjük ki a műemléki rétegek tiszteletét a legszakszerűbben?", [
                "a történeti rétegzettséget tiszteletben tartó és a kordokumentumokat megőrző eljárás",
                "amikor lefestik a régi falakat fehérre",
                "hogyha új ablakokat tesznek a várra"
            ], 0, ["c1-participle-monument-preservation-ethics"]),
            match("vocabulary", "recognize", [["proveniencia", "a műkincs eredettörténete"], ["anasztilózis", "leomlott eredeti kövek pontos visszaépítése"], ["pastiche", "történeti hűség nélküli stílusutánzat"], ["kánonképzés", "kulturális értékek beemelése a kollektív emlékezetbe"], ["közkincs", "a nemzet közös szellemi vagyona"]], ["c1-29-vocab"]),
            fb("vocabulary", "recall", "A műemlékvédelemben a leomlott eredeti kövek visszaépítését _____ nevezik. (anastylosis / anasztilózisnak)", "anasztilózisnak", "In monument protection the reassembly of fallen original stones is called anastylosis.", ["c1-29-vocab"]),
            fb("vocabulary", "recall", "A modern vasbeton magra húzott gipszstílusutánzat a _____ építészet. (pastiche / pastiche)", "pastiche", "Plaster stylistic imitation drawn over a modern reinforced concrete core is pastiche architecture.", ["c1-29-vocab"]),
            fb("grammar", "recall", "A restaurálást restaurátori szempontból _____ kell végrehajtani. (reversibly / reverzibilisen)", "reverzibilisen", "Restoration must be executed reversibly from a conservator's perspective.", ["c1-adv-museological-authenticity-provenance"]),
            fb("grammar", "context", "A díszletekkel szemben a valóságban a romok valódi történeti _____ hordoznak. (witness / tanúságtételt)", "tanúságtételt", "In contrast with decors in reality ruins carry genuine historical testimony.", ["c1-adv-counter-pastiche-adversatives"]),
            fb("grammar", "context", "Az emlékhelyeket abból a célból létesítik, _____ ébren tartsák a történelmi emlékezetet. (that / hogy)", "hogy", "Memorial sites are established with the goal that they keep historical memory awake.", ["c1-modal-teleological-canon-formation"]),
            mc("grammar", "context", "Mi a funkciója a pastiche-ellenes ellentétes szerkezeteknek a műemlékvédelmi vitában?", [
                "A vasbeton vázas díszletépítés leleplezése a valódi anyagi és történeti hitelesség védelmében.",
                "Az építőipari munkások dicsérete a gyors falazásért.",
                "A múzeumi belépőjegyek árának megvitatása."
            ], 0, ["c1-adv-counter-pastiche-adversatives"]),
            sb("grammar", "produce", ["A", "múzeum", "a", "nemzet", "eleven", "öntudatának", "kútfeje."], ["A", "múzeum", "a", "nemzet", "eleven", "öntudatának", "kútfeje."], "The museum is the springhead of the nation's living consciousness.", ["c1-adv-scalar-cultural-enlightenment"]),
            sw("production", [{"prompt": "Write a critical evaluation of monumental authenticity contrasting authentic ruins with pastiche decors.", "answer": "A vasbeton vázra húzott historizáló díszletekkel szemben a valóságban a felelős műemlékvédelem az autenticitást és a történeti rétegek tiszteletét tekinti a nemzeti emlékezet legfőbb zálogának."}], ["c1-adv-counter-pastiche-adversatives"]),
            sw("production", [{"prompt": "Synthesize Pulszky Ferenc's museum philosophy using a scalar evaluative adverbial.", "answer": "Pulszky Ferenc művelődéstörténetileg felbecsülhetetlen mértékben bizonyította be, hogy a múzeumok nem a múlt elzárt temetői, hanem a polgári öntudatot és szellemi szabadságot éltető közkincsek."}], ["c1-adv-scalar-cultural-enlightenment"])
        ]
    )

    # ----------------------------------------------------
    # TRACK 2: DISCOURSE (c1-kulturalisorokseg)
    # ----------------------------------------------------
    disc_intro = [
        "In the 2010s, Hungary witnessed an unprecedented, state-orchestrated drive toward cultural hegemony. Following the proclamation of an ideological 'cultural era', public cultural institutions, literary journals, and artistic subsidies were concentrated into top-heavy conglomerates such as the Petőfi Cultural Agency (PKÜ).",
        "At the same time, the constitutional entrenchment of the Hungarian Academy of Arts (MMA), the abolition of corporate tax credits (TAO), and the defunding of independent performing arts venues brought alternative theater to the brink of ruin. In this unit, you will master the analytical discourse of cultural monopolies, ideological canon polarization, and artistic resistance at the C1 level."
    ]

    disc_lessons = [
        {
            "num": 1,
            "stem": f"c1-{slug}-01",
            "title": "Cultural Hegemony & Intellectual Space Conquest",
            "grammar_title": "Discourse Framing Markers Diagnosing State Cultural Hegemony and Ideological Dominance",
            "grammar_skill": "c1-discourse-cultural-hegemony-framing",
            "goals": [
                "I can analyze the Gramscian concept of cultural hegemony, ideological space conquest, and patron-client networks (*szellemi térfoglalás, hegemóniatörekvés, kultúrharc, lojalitási háló*).",
                "I can deploy discourse framing markers diagnosing ideological capture (*a szellemi térfoglalás szisztematikus stratégiája nyomán, a kultúrpolitikai hegemónia kiépülése következtében, a klientúraépítés logikájából fakadóan*).",
                "I can critique regime-driven culture wars in political philosophy register."
            ],
            "vocab": [
                {"lemma": "kulturális hegemónia", "translation": "cultural hegemony", "pos": "expression"},
                {"lemma": "szellemi térfoglalás", "translation": "intellectual conquest / cultural space capture", "pos": "expression"},
                {"lemma": "kultúrharc", "translation": "culture war", "pos": "noun"},
                {"lemma": "klientúraépítés", "translation": "clientele building / patronage networks", "pos": "noun"},
                {"lemma": "korszakváltás", "translation": "epochal shift / cultural era change", "pos": "noun"},
                {"lemma": "politikai lojalitás", "translation": "political loyalty", "pos": "expression"},
                {"lemma": "szellemi élet", "translation": "intellectual / cultural life", "pos": "expression"},
                {"lemma": "ideológiai monopólium", "translation": "ideological monopoly", "pos": "expression"}
            ],
            "gr_text1": "Discourse framing markers diagnose structural shifts in state cultural domination: `a szellemi térfoglalás szisztematikus stratégiája nyomán` (in the wake of the systematic strategy of intellectual space conquest), `a kultúrpolitikai hegemónia kiépülése következtében` (as a consequence of the construction of cultural-political hegemony), `a klientúraépítés logikájából fakadóan` (stemming from the logic of clientele building).",
            "gr_text2": "Example: `A kultúrpolitikai hegemónia kiépülése következtében a szakmai teljesítmény helyett a politikai lojalitás vált az intézményvezetői kinevezések legfőbb kritériumává`.",
            "gr_table": [
                ["A szellemi térfoglalás következtében az állami intézmények egyetlen ideológia szolgálatába álltak.", "As a consequence of intellectual space conquest state institutions entered the service of a single ideology."],
                ["A hegemóniatörekvés nyomán felszámolták a korábbi szellemi pluralizmust.", "In the wake of hegemony drive former intellectual pluralism was eliminated."],
                ["A klientúraépítés logikájából fakadóan a támogatások hűségjutalommá silányultak.", "Stemming from the logic of clientele building subsidies deteriorated into loyalty bonuses."]
            ],
            "world_story_seg": {
                "seg_slug": "c1-kulturalisorokseg-01-kulturharc-terfoglalas",
                "title": "A szellemi térfoglalás krónikája",
                "summary": "A 2018-as választási győzelem után a hatalom meghirdette a kulturális korszakváltást és megkezdte a szellemi térfoglalást az állami intézményekben.",
                "paragraphs": [
                    {"type": "narration", "text": "A politikai kétharmad megszilárdulása után a kormányfő kijelölte a következő harcteret: a politikai berendezkedést kulturális korszakba kell ágyazni. Megkezdődött a szellemi térfoglalás gőzhengerének felvonultatása."},
                    {"type": "dialogue", "speaker": "Varga Zoltán", "text": "A szellemi térfoglalás szisztematikus stratégiája nyomán a kultúrát a rezsim puszta legitimációs eszközévé fokozták le. Nem művészeti értékek versenyeznek, hanem a hatalomhoz való politikai lojalitás foka határozza meg a források sorsát."},
                    {"type": "narration", "text": "A múzeumok, folyóiratok és kutatóintézetek élére lojális pártkatonák kerültek, miközben a független gondolkodókat a nemzetietlenség és a liberalizmus bélyegével szorították a perifériára."},
                    {"type": "narration", "text": "A kultúrharc nem spontán társadalmi vita volt, hanem felülről vezényelt hatalmi expanzió, amelynek célja az alternatív értelmiségi műhelyek elszívása és ellehetetlenítése lett."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Mit jelent a 'szellemi térfoglalás' a kormányzati kultúrpolitika gyakorlatában?", [
                    "A közpénzekből finanszírozott kulturális és tudományos intézmények, lapok és döntőbizottságok ideológiai és személyi uralmát a politikai lojalitás alapján.",
                    "A könyvtári olvasótermek asztalainak átrendezését.",
                    "Új festmények kiakasztását a folyosókon."
                ], 0, ["c1-kulturalisorokseg-vocab"]),
                fb("grammar", "controlled", "A szellemi térfoglalás szisztematikus stratégiája _____ felszámolták az intézmények autonómiáját. (in the wake of / nyomán)", "nyomán", "In the wake of the systematic strategy of intellectual space conquest institutional autonomy was liquidated.", ["c1-discourse-cultural-hegemony-framing"]),
                match("vocabulary", "controlled", [["kulturális hegemónia", "egy politikai erő kizárólagos uralma a művészeti szféra felett"], ["szellemi térfoglalás", "az állami források és pozíciók elfoglalása a lojális elit által"], ["kultúrharc", "politikai törésvonalak mentén szított ideológiai polarizáció"], ["klientúraépítés", "művészek és intézmények hűségre szoktatása támogatásokkal"]], ["c1-kulturalisorokseg-vocab"]),
                fb("grammar", "practice", "A kultúrpolitikai hegemónia kiépülése _____ a szakmai szempontok teljesen háttérbe szorultak. (consequence / következtében)", "következtében", "As a consequence of the establishment of cultural hegemony professional considerations were sidelined.", ["c1-discourse-cultural-hegemony-framing"]),
                sb("grammar", "practice", ["A", "szellemi", "térfoglalás", "felszámolja", "a", "kulturális", "pluralizmust."], ["A", "szellemi", "térfoglalás", "felszámolja", "a", "kulturális", "pluralizmust."], "Intellectual space conquest liquidates cultural pluralism.", ["c1-discourse-cultural-hegemony-framing"]),
                dc("dialogue", [
                    {"speaker": "Kultúrakutató", "text": "Hogyan értékeli a kulturális intézmények tömeges átszervezését?"},
                    {"speaker": "Író", "text": "Egyértelműen úgy, hogy a szellemi térfoglalás szisztematikus stratégiája _____ a hatalom monopolizálni akarja a nemzeti kánont."},
                    {"speaker": "Kultúrakutató", "text": "Ez a folyamat súlyos károkat okoz a magyar kultúra sokszínűségében."}
                ], ["nyomán", "helyett", "nélkül"], 0, ["c1-discourse-cultural-hegemony-framing"]),
                sw("production", [{"prompt": "Write a critical diagnosis of cultural hegemony using a discourse framing marker.", "answer": "A szellemi térfoglalás szisztematikus stratégiája nyomán és a kultúrpolitikai hegemónia kiépülése következtében a hatalom az esztétikai minőség helyére a feltétlen pártpolitikai lojalitást állította."}], ["c1-discourse-cultural-hegemony-framing"]),
                mc("grammar", "check", "Melyik kifejezés diagnosztizálja a kultúrpolitikai fordulatot a leghitelesebben?", [
                    "a szellemi térfoglalás szisztematikus stratégiája nyomán / a kultúrpolitikai hegemónia következtében",
                    "amikor új könyveket raknak a polcra",
                    "egy szép napon váratlanul"
                ], 0, ["c1-discourse-cultural-hegemony-framing"])
            ]
        },
        {
            "num": 2,
            "stem": f"c1-{slug}-02",
            "title": "The PKÜ Holding, Centralization & Monopolies",
            "grammar_title": "Deontic Modal Structures Asserting Creative Autonomy Against Political Patronage Demands",
            "grammar_skill": "c1-modal-deontic-artistic-autonomy",
            "goals": [
                "I can analyze the rise of Demeter Szilárd, the Petőfi Cultural Agency (PKÜ) conglomerate, and resource concentration (*kulturális holding, forráskoncentráció, bürokratikus vízfej, kormánybiztosi irányítás*).",
                "I can deploy deontic modal structures asserting artistic independence (*a művészet nem rendelhető alá pártpolitikai megrendeléseknek, az alkotóknak kötelességük megőrizni szellemi integritásukat, nem engedhetik át az autonómiát*).",
                "I can critique top-heavy cultural mega-institutions."
            ],
            "vocab": [
                {"lemma": "megaintézmény", "translation": "mega-institution / cultural conglomerate", "pos": "noun"},
                {"lemma": "kulturális holding", "translation": "cultural holding company (PKÜ model)", "pos": "expression"},
                {"lemma": "forráskoncentráció", "translation": "concentration of financial resources", "pos": "noun"},
                {"lemma": "kormánybiztos", "translation": "government commissioner", "pos": "noun"},
                {"lemma": "alkotói autonómia", "translation": "creative / artistic autonomy", "pos": "expression"},
                {"lemma": "bürokratikus vízfej", "translation": "bureaucratic top-heaviness", "pos": "expression"},
                {"lemma": "ingatlanvagyon", "translation": "real estate portfolio / property assets", "pos": "noun"},
                {"lemma": "monopólium", "translation": "monopoly over distribution", "pos": "noun"}
            ],
            "gr_text1": "Deontic modal structures articulate moral and professional obligations protecting artistic freedom from state capture: `a művészeti alkotófolyamat nem vethető alá bürokratikus diktátumoknak` (the artistic creation process must not be subjected to bureaucratic dictates), `az értelmiségnek kötelessége ellenállni a forrásmonopóliumoknak` (the intelligentsia has a duty to resist resource monopolies), `a szellemi élet nem silányulhat hivatali propagandává` (intellectual life must not deteriorate into official propaganda).",
            "gr_text2": "Example: `A szellemi élet szereplőinek kötelességük megvédeni a függetlenséget, s a művészek nem rendelhetik alá alkotói autonómiájukat a PKÜ milliárdos forrásainak`.",
            "gr_table": [
                ["A művészet nem rendelhető alá politikai elvárásoknak.", "Art cannot be subordinated to political expectations."],
                ["Az alkotóknak kötelességük megőrizni szellemi függetlenségüket.", "Creators have a duty to preserve their spiritual independence."],
                ["A kulturális intézmények nem alakulhatnak bürokratikus propaganda-gépezetté.", "Cultural institutions cannot turn into a bureaucratic propaganda apparatus."]
            ],
            "world_story_seg": {
                "seg_slug": "c1-kulturalisorokseg-02-pku-intezmenyi-monopolium",
                "title": "A birodalomépítés: A Petőfi Kulturális Ügynökség",
                "summary": "Demeter Szilárd felügyelete alá vonta az irodalmi és zenei támogatásokat, létrehozva a PKÜ megaintézményi holdingját és hatalmas ingatlanvagyonát.",
                "paragraphs": [
                    {"type": "narration", "text": "A Petőfi Irodalmi Múzeum élére kinevezett miniszteri biztos rohamtempóban látott hozzá a források központosításához. Létrejött a Petőfi Kulturális Ügynökség (PKÜ), egy milliárdos költségvetésű holding, amely alá szervezték a folyóirat-támogatásokat, a könnyűzenei pályázatokat és a nemzetközi könyvvásárokat."},
                    {"type": "dialogue", "speaker": "Kovács Melinda", "text": "A művészet nem rendelhető alá egyetlen kormánybiztos személyes ízlésének és ideológiai rosta-szisztémájának. Az alkotói autonómiát nem lehet forintokért feladni, mert a központosított holding a sokszínű szellemi élet halálát jelenti."},
                    {"type": "narration", "text": "A holding nemcsak pénzt, hanem ingatlanokat is bekebelezett: a Hajógyári-szigettől a történelmi palotákig hatalmas vagyon került a vezetés alá, miközben a kritikus műhelyek támogatásait elapasztották."},
                    {"type": "narration", "text": "A bürokratikus vízfej kiépülése demonstrálta a hatalom logikáját: a független szakmai kollégiumok helyét a felülről vezérelt, egyszemélyi döntési mechanizmusok vették át."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Hogyan működik a Petőfi Kulturális Ügynökség (PKÜ) megaintézményi modellje?", [
                    "A korábban autonóm szakmai kuratóriumok által elosztott irodalmi és művészeti forrásokat egyetlen központi holdingba vonja össze, felülről irányított vezetéssel.",
                    "Minden magyar polgárnak ingyen oszt versesköteteket a postán.",
                    "Kizárólag külföldi operaénekeseket foglalkoztat."
                ], 0, ["c1-kulturalisorokseg-vocab"]),
                fb("grammar", "controlled", "A művészek nem _____ alá a szakmai függetlenségüket az állami pénzosztóknak. (must not subordinate / rendelhetik)", "rendelhetik", "Artists must not subordinate their professional independence to state money distributors.", ["c1-modal-deontic-artistic-autonomy"]),
                match("vocabulary", "controlled", [["kulturális holding", "több ágazatot egyetlen cégformába tömörítő megaintézmény"], ["forráskoncentráció", "a költségvetési pénzek központi csatornába terelése"], ["bürokratikus vízfej", "túlméretezett adminisztratív irányítás"], ["alkotói autonómia", "a művész szabadsága a hatalmi beavatkozástól"]], ["c1-kulturalisorokseg-vocab"]),
                fb("grammar", "practice", "Az alkotóknak kötelességük _____ az esztétikai autonómiát a klientúraépítéssel szemben. (defend / megvédeni)", "megvédeni", "Creators have a duty to defend aesthetic autonomy against clientele building.", ["c1-modal-deontic-artistic-autonomy"]),
                sb("grammar", "practice", ["A", "művészet", "nem", "rendelhető", "alá", "pártpolitikai", "elvárásoknak."], ["A", "művészet", "nem", "rendelhető", "alá", "pártpolitikai", "elvárásoknak."], "Art cannot be subordinated to party political expectations.", ["c1-modal-deontic-artistic-autonomy"]),
                dc("dialogue", [
                    {"speaker": "Folyóirat-szerkesztő", "text": "Hogyan éljük túl a PKÜ által diktált forrásmegvonásokat?"},
                    {"speaker": "Író", "text": "Csak úgy, ha nem hódolunk be: a művészet nem _____ alá politikai igazodásnak a túlélési pénzekért cserébe."},
                    {"speaker": "Folyóirat-szerkesztő", "text": "Akkor a független olvasóközönség támogatására kell építenünk."}
                ], ["rendelhető", "felejthető", "építhető"], 0, ["c1-modal-deontic-artistic-autonomy"]),
                sw("production", [{"prompt": "Write a sentence formulating artistic autonomy using a deontic modal structure.", "answer": "A művészek nem rendelhetik alá alkotói szabadságukat a központosított kulturális holdingok ideológiai elvárásainak, és kötelességük megőrizni a független kritikai szellemet."}], ["c1-modal-deontic-artistic-autonomy"]),
                mc("grammar", "check", "Melyik modális kifejezés fogalmazza meg az autonómia védelmét a legkategorikusabban?", [
                    "a művészet nem rendelhető alá politikai lojalitásnak / kötelességük megvédeni a függetlenséget",
                    "esetleg kérhetnének egy kis plusz pénzt",
                    "talán nem ártana barátkozni a miniszterrel"
                ], 0, ["c1-modal-deontic-artistic-autonomy"])
            ]
        },
        {
            "num": 3,
            "stem": f"c1-{slug}-03",
            "title": "Defunding Independent Theatres & Venue Closures",
            "grammar_title": "Proportional Correlative Conjunctions Mapping Independent Sector Starvation Against Megainstitution Subsidies",
            "grammar_skill": "c1-adv-proportional-cultural-defunding",
            "goals": [
                "I can analyze the abolition of corporate cultural tax (TAO), defunding of independent performing arts, and venue closures (*kulturális TAO eltörlése, működési forráskivonás, független színházak, játszóhely-bezárás*).",
                "I can deploy proportional correlative conjunctions mapping fiscal starvation (*minél több tízmilliárdot öntenek a lojális kőszínházakba, annál inkább a puszta túlélésért küzd a független szféra, amilyen mértékben megvonják a működési forrásokat, olyan arányban szűnnek meg az alternatív társulatok*).",
                "I can critique asymmetric arts subsidies in performance studies register."
            ],
            "vocab": [
                {"lemma": "kulturális TAO", "translation": "corporate tax subsidy for culture (abolished 2018)", "pos": "expression"},
                {"lemma": "forráskivonás", "translation": "withdrawal of funds / defunding", "pos": "noun"},
                {"lemma": "független előadó-művészet", "translation": "independent performing arts", "pos": "expression"},
                {"lemma": "működési támogatás", "translation": "operational subsidy", "pos": "expression"},
                {"lemma": "játszóhely-bezárás", "translation": "closure of theater venues (e.g. Átrium)", "pos": "expression"},
                {"lemma": "társulat-feloszlás", "translation": "dissolution of theater troupes", "pos": "expression"},
                {"lemma": "közösségi adománygyűjtés", "translation": "crowdfunding / community donations", "pos": "expression"},
                {"lemma": "létbizonytalanság", "translation": "existential insecurity", "pos": "noun"}
            ],
            "gr_text1": "Proportional correlative structures map the direct fiscal trade-off between the starvation of independent arts and preferential patronage of state theatres: `minél több tízmilliárdos apanázst kapnak a lojális kőszínházak, annál drámaibb forráselvonást szenved el a független szcéna` (the more tens of billions in allowances loyal institutions receive, the more dramatic defunding the independent scene suffers), `amilyen mértékben felszámolják a normatív támogatásokat, olyan arányban lehetetlenülnek el a progresszív műhelyek` (in proportion as normative subsidies are dismantled, to that extent progressive workshops are disabled).",
            "gr_text2": "Example: `Minél inkább a politikai szimpátia vezérli a minisztériumi döntéseket, annál gyorsabban kényszerülnek bezárásra az olyan független játszóhelyek, mint az Átrium`.",
            "gr_table": [
                ["Minél kevesebb működési támogatást kapnak a függetlenek, annál több társulat oszlik fel.", "The less operational support independents receive, the more troupes dissolve."],
                ["Amilyen mértékben növelik a lojális intézmények költségvetését, olyan arányban szorítják ki a függetleneket.", "To the extent they increase loyal institutions' budgets, to that extent independents are marginalized."],
                ["Minél bizonytalanabb a finanszírozás, annál mélyebb a társulatok létbizonytalansága.", "The more precarious the funding, the deeper the troupes' existential insecurity."]
            ],
            "world_story_seg": {
                "seg_slug": "c1-kulturalisorokseg-03-szinhazi-valsag-tao-utan",
                "title": "Függöny le: A független színházak haláltusája",
                "summary": "A TAO 2018-as eltörlése és a működési támogatások megvonása a magyar független színházi szféra összeomlásához és az Átrium bezárásához vezetett.",
                "paragraphs": [
                    {"type": "narration", "text": "2018-ban a kormány egyetlen tollvonással megszüntette a kulturális társasági adókedvezményt (TAO), elvágva a független előadó-művészeti társulatok legfontosabb nézőszám-alapú, autonóm bevételi forrását."},
                    {"type": "dialogue", "speaker": "Molnár Tamás", "text": "Minél több forrást csoportosítanak át az állami kőszínházakhoz, annál gyorsabban vérzik el az alternatív szcéna. Nem gazdasági okok állnak a háttérben: a kritikai színházat akarják elhallgattatni az anyagi ellehetetlenítés által."},
                    {"type": "narration", "text": "A forráskivonás drámai hullámot indított el: az Átrium Színház, a főváros egyik leglátogatottabb független intézménye bejelentette végleges bezárását. A Pintér Béla és Társulata és megannyi kísérleti táncműhely adománygyűjtésre kényszerült a puszta túlélésért."},
                    {"type": "narration", "text": "A magyar színházi kultúra nemzetközileg elismert innovációs műhelyei sodródtak a szakadék szélére, míg a lojális igazgatók rekordméretű költségvetésekből gazdálkodhattak."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Milyen hatással volt a kulturális TAO-rendszer megszüntetése a független színházakra?", [
                    "Megfosztotta őket a jegybevételekkel arányos, politikai ellenőrzéstől mentes állami kiegészítéstől, kiszolgáltatva őket az egyedi miniszteri döntéseknek.",
                    "Azonnal megduplázta a színészek fizetését.",
                    "Ingyenessé tette a színházbérleteket az egyetemistáknak."
                ], 0, ["c1-kulturalisorokseg-vocab"]),
                fb("grammar", "controlled", "Minél több forrást vonnak el a független szférától, _____ több legendás játszóhely zár be. (the more / annál)", "annál", "The more funds they withdraw from the independent sphere, the more legendary venues close down.", ["c1-adv-proportional-cultural-defunding"]),
                match("vocabulary", "controlled", [["kulturális TAO", "jegybevételhez kötött korábbi adókedvezményes támogatás"], ["forráskivonás", "a költségvetési támogatások szándékos elapasztása"], ["játszóhely-bezárás", "a színházak fizikai működésének ellehetetlenülése"], ["létbizonytalanság", "a jövő havi működés anyagi kiszámíthatatlansága"]], ["c1-kulturalisorokseg-vocab"]),
                fb("grammar", "practice", "Amilyen mértékben csökken a támogatás, olyan _____ mélyül a színházak válsága. (proportion / arányban)", "arányban", "In proportion as subsidies decline, to that extent the theaters' crisis deepens.", ["c1-adv-proportional-cultural-defunding"]),
                sb("grammar", "practice", ["Minél", "kevesebb", "a", "támogatás,", "annál", "mélyebb", "a", "válság."], ["Minél", "kevesebb", "a", "támogatás,", "annál", "mélyebb", "a", "válság."], "The less the support, the deeper the crisis.", ["c1-adv-proportional-cultural-defunding"]),
                dc("dialogue", [
                    {"speaker": "Színházigazgató", "text": "Hogyan alakult a független társulatok költségvetése az elmúlt években?"},
                    {"speaker": "Dramaturg", "text": "Drasztikusan romlott: minél több pénzt visz el az állami lojalitási kör, _____ kevesebb morzsa jut a valódi művészeti innovációra."},
                    {"speaker": "Színházigazgató", "text": "Ezért kényszerülünk közönségi adománygyűjtésre."}
                ], ["annál", "mindig", "soha"], 0, ["c1-adv-proportional-cultural-defunding"]),
                sw("production", [{"prompt": "Write a sentence analyzing cultural defunding using 'Minél... annál...'.", "answer": "Minél több milliárd forintot önt a kormányzat a lojális állami kőszínházakba, annál mélyebb létbizonytalanságba taszítja a társadalmi kérdéseket feszegető független színházi műhelyeket."}], ["c1-adv-proportional-cultural-defunding"]),
                mc("grammar", "check", "Melyik szerkezet fejezi ki a forrásmegvonás és színházi pusztulás arányosságát a legpontosabban?", [
                    "Minél kevesebb forrás jut a függetleneknek... annál több társulat kényszerül bezárásra / Amilyen mértékben... olyan arányban",
                    "Ha nem esik az eső, száraz a színpad",
                    "A színészek szeretnek tapsot kapni"
                ], 0, ["c1-adv-proportional-cultural-defunding"])
            ]
        },
        {
            "num": 4,
            "stem": f"c1-{slug}-04",
            "title": "Constitutional Privileges of the MMA & Parity Dissolution",
            "grammar_title": "Epistemic Stance Markers Assessing Cultural Tribalism and Partisan Canon Polarization",
            "grammar_skill": "c1-epistemic-ideological-canon-polarization",
            "goals": [
                "I can analyze the constitutional enshrinement of the Hungarian Academy of Arts (MMA), dissolution of parity in the National Cultural Fund (NKA), and lifetime annuities (*MMA alaptörvényi státusz, testületi paritás felbomlása, NKA kuratóriumok, művészeti életjáradék*).",
                "I can deploy epistemic stance markers assessing ideological polarization (*kétségkívül bebizonyosodott az esztétikai kánon politikai kisajátítása, minden jel szerint a paritás felszámolása a szakmai autonómia végét jelenti, aligha vitatható az intézményes privilégiumok torzító hatása*).",
                "I can critique constitutional capture of cultural distribution bodies."
            ],
            "vocab": [
                {"lemma": "Magyar Művészeti Akadémia", "translation": "Hungarian Academy of Arts (MMA)", "pos": "expression"},
                {"lemma": "testületi paritás", "translation": "institutional parity / equal professional balance", "pos": "expression"},
                {"lemma": "Nemzeti Kulturális Alap", "translation": "National Cultural Fund (NKA)", "pos": "expression"},
                {"lemma": "művészeti életjáradék", "translation": "artistic life annuity", "pos": "expression"},
                {"lemma": "alaptörvényi privilégium", "translation": "constitutional privilege", "pos": "expression"},
                {"lemma": "delegálási jog", "translation": "delegation right / appointment power", "pos": "expression"},
                {"lemma": "szakmai kuratórium", "translation": "professional board of trustees", "pos": "expression"},
                {"lemma": "kiváltságos elit", "translation": "privileged cultural elite", "pos": "expression"}
            ],
            "gr_text1": "Epistemic stance markers formulate analytical evaluations regarding the destruction of institutional checks and balances: `kétségkívül bebizonyosodott a paritásos struktúrák felszámolása` (the liquidation of parity structures has undoubtedly been demonstrated), `minden jel szerint az MMA privilégiumai a szakmai autonómia végét jelentik` (by all indications MMA privileges mean the end of professional autonomy), `aligha vitatható az alkotmányos kiváltságok piactorzító jellege` (the market-distorting nature of constitutional privileges can hardly be disputed).",
            "gr_text2": "Example: `Kétségkívül bebizonyosodott, hogy az MMA alaptörvénybe emelése és az NKA megszállása végleg felborította a testületi paritást a magyar kultúrában`.",
            "gr_table": [
                ["Kétségkívül látható a döntéshozatal átpolitizálódása a Nemzeti Kulturális Alapban.", "Undoubtedly the politicization of decision-making in the National Cultural Fund is visible."],
                ["Minden jel szerint az MMA monopolizálta az állami elismerések és járadékok rendszerét.", "By all indications the MMA has monopolized the system of state honors and annuities."],
                ["Aligha vitatható, hogy a paritás megszűnése ellehetetlenítette az esztétikai vitákat.", "It can hardly be disputed that the end of parity disabled aesthetic debates."]
            ],
            "world_story_seg": {
                "seg_slug": "c1-kulturalisorokseg-04-nka-es-mma-hatalom",
                "title": "A paritás vége: Az NKA és az MMA szövetsége",
                "summary": "A 2011-es Alaptörvénybe beemelt MMA monopolhelyzetbe került, míg a Nemzeti Kulturális Alap kuratóriumaiban felszámolták a szakmai szervezetek paritását.",
                "paragraphs": [
                    {"type": "narration", "text": "A 2011-es Alaptörvény példátlan döntést hozott: a rendszerváltás előtt magánegyesületként alapított Magyar Művészeti Akadémiát (MMA) köztestületi rangra és alkotmányos szintre emelte, tízmilliárdos költségvetést és épületek tucatjait juttatva a szervezetnek."},
                    {"type": "dialogue", "speaker": "Fekete András", "text": "Kétségkívül bebizonyosodott, hogy az MMA privilégiumai nem a magyar művészet egészét szolgálják, hanem egy kiváltságos klientúra életjáradékait garantálják. Az NKA kuratóriumaiban felszámolták a testületi paritást, a szakmai szervezetek pedig elveszítették döntési súlyukat."},
                    {"type": "narration", "text": "A Nemzeti Kulturális Alapban korábban a minisztérium, a szakmai szervezetek és az alkotók egyenlő arányban delegáltak bírálókat. Ezt az egyensúlyt felváltotta az MMA és a miniszter kinevezettjeinek kényelmes többsége."},
                    {"type": "narration", "text": "A független alkotók pályázatai sorra buktak el az ideológiai szűrőkön, miközben az alkotói szabadság helyét a szervilizmus vette át."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Milyen jogállást és privilégiumokat biztosított a 2011-es Alaptörvény az MMA-nak?", [
                    "Köztestületi rangot, alkotmányos szintű védelmet, tízmilliárdos költségvetést és kiemelt delegálási jogot az NKA kuratóriumaiba.",
                    "Kizárólag egy belvárosi iroda bérleti jogát.",
                    "A külföldi festményvásárok szervezési jogát."
                ], 0, ["c1-kulturalisorokseg-vocab"]),
                fb("grammar", "controlled", "Kétségkívül _____ az intézményi paritás felborulása és a források politikai elosztása. (demonstrated / bebizonyosodott)", "bebizonyosodott", "Undoubtedly the overturning of institutional parity and political distribution of funds has been demonstrated.", ["c1-epistemic-ideological-canon-polarization"]),
                match("vocabulary", "controlled", [["testületi paritás", "a szakmai szervezetek és az állam egyenlő arányú döntéshozatala"], ["NKA", "Nemzeti Kulturális Alap, a támogatások fő pályázati forrása"], ["MMA", "Magyar Művészeti Akadémia, alkotmányos kiváltságos köztestület"], ["művészeti életjáradék", "kiemelt alkotóknak járó rendszeres állami juttatás"]], ["c1-kulturalisorokseg-vocab"]),
                fb("grammar", "practice", "Aligha vitatható, hogy a paritás megszűnése a szakmai döntéshozatal _____ jelentette. (end / végét)", "végét", "It can hardly be disputed that the end of parity meant the end of professional decision-making.", ["c1-epistemic-ideological-canon-polarization"]),
                sb("grammar", "practice", ["Kétségkívül", "bebizonyosodott", "a", "testületi", "paritás", "teljes", "felszámolása."], ["Kétségkívül", "bebizonyosodott", "a", "testületi", "paritás", "teljes", "felszámolása."], "Undoubtedly the complete elimination of institutional parity has been demonstrated.", ["c1-epistemic-ideological-canon-polarization"]),
                dc("dialogue", [
                    {"speaker": "Képzőművész", "text": "Miért nem pályáznak már a fiatal független művészek az NKA kollégiumainál?"},
                    {"speaker": "Művészettörténész", "text": "Mert minden jel szerint a testületi paritás felszámolása óta az MMA-delegáltak szavazata _____ minden lényegi támogatást."},
                    {"speaker": "Képzőművész", "text": "Így a tehetség helyett a politikai igazodás dönt."}
                ], ["eldönt", "elfed", "kérdez"], 0, ["c1-epistemic-ideological-canon-polarization"]),
                sw("production", [{"prompt": "Write a critical evaluation of institutional cultural capture using an epistemic stance marker.", "answer": "Kétségkívül bebizonyosodott, hogy az MMA alaptörvényi kiváltságai és az NKA paritásos struktúrájának felszámolása eltorzította az esztétikai versenyt, megfosztva a független szcénát az autonóm forrásoktól."}], ["c1-epistemic-ideological-canon-polarization"]),
                mc("grammar", "check", "Melyik episztemikus kifejezés értékeli a paritás felszámolását a legmagasabb elemzői szinten?", [
                    "kétségkívül bebizonyosodott / aligha vitatható az autonómia felszámolása",
                    "úgy néz ki talán nincs pénz",
                    "lehet hogy valaki elvitte a kulcsot"
                ], 0, ["c1-epistemic-ideological-canon-polarization"])
            ]
        },
        {
            "num": 5,
            "stem": f"c1-{slug}-05",
            "title": "Divided Pantheon: Parallel Cultures & Creative Freedom",
            "grammar_title": "Evaluative Synthesis Particles Formulating Manifestos for Institutional Pluralism and Artistic Freedom",
            "grammar_skill": "c1-adv-conclusive-cultural-renewal-synthesis",
            "goals": [
                "I can analyze parallel intellectual societies, tribal polarization, and cultural resistance (*kettészakadt kultúra, szekértábor-logika, párhuzamos kánonok, alkotói szabadság*).",
                "I can deploy evaluative synthesis particles formulating manifestos (*végső soron elengedhetetlen a szekértáborok meghaladása, mindent egybevetve a kulturális pluralizmus a nemzet megmaradásának záloga, végeredményben a független művészet nem elnyomható*).",
                "I can synthesize a vision for independent Hungarian cultural renewal."
            ],
            "vocab": [
                {"lemma": "kettészakadt kultúra", "translation": "split / divided culture", "pos": "expression"},
                {"lemma": "szekértábor-logika", "translation": "partisan camp mentality / cultural tribalism", "pos": "expression"},
                {"lemma": "párhuzamos kánon", "translation": "parallel literary / artistic canon", "pos": "expression"},
                {"lemma": "kulturális ellenállás", "translation": "cultural resistance / counter-public", "pos": "expression"},
                {"lemma": "pluralizmus", "translation": "institutional / aesthetic pluralism", "pos": "noun"},
                {"lemma": "szellemi szuverenitás", "translation": "intellectual sovereignty", "pos": "expression"},
                {"lemma": "megbékélés", "translation": "reconciliation / civic peace", "pos": "noun"},
                {"lemma": "szellemi megújulás", "translation": "spiritual / intellectual renewal", "pos": "expression"}
            ],
            "gr_text1": "Evaluative synthesis particles formulate comprehensive manifestos summarizing the struggle for artistic autonomy: `végső soron elengedhetetlen a szekértábor-logika felszámolása` (ultimately the liquidation of camp mentality is indispensable), `mindent egybevetve a kultúra sokszínűsége a nemzeti önazonosság legfőbb feltétele` (all things considered cultural diversity is the chief condition of national identity), `végeredményben a hatalom sohasem győzheti le a szabad gondolatot` (in the final analysis power can never defeat free thought).",
            "gr_text2": "Example: `Végső soron elengedhetetlen felismerni: a szekértáborok harca helyett csakis az esztétikai autonómia és a kulturális pluralizmus teremthet valódi szellemi megújulást`.",
            "gr_table": [
                ["Végső soron elengedhetetlen a szakmai párbeszéd helyreállítása a két tábor között.", "Ultimately restoring professional dialogue between the two camps is indispensable."],
                ["Mindent egybevetve a független művészet nélkül a nemzet szellemileg elszegényedik.", "All things considered without independent art the nation is spiritually impoverished."],
                ["Végeredményben a szabadság iránti vágy mindig túléli a politikai hegemóniát.", "In the final analysis the desire for freedom always survives political hegemony."]
            ],
            "world_story_seg": {
                "seg_slug": "c1-kulturalisorokseg-05-parhuzamos-kannonok-jovo",
                "title": "Kettészakadt panteon: Párhuzamos valóságok a kultúrában",
                "summary": "Két írószervezet, két színházi szövetség, két akadémia: a magyar szellemi élet drámai megosztottsága és a független kultúra túlélési stratégiái.",
                "paragraphs": [
                    {"type": "narration", "text": "A 2020-as évekre a magyar kultúra intézményesen kettészakadt. Külön színházi társaságok, külön írószövetségek, külön könyvhetek és külön panteonok léteznek: a két világ szereplői nem beszélnek egymással, a díjak és elismerések értéke pedig devalválódott a szekértábor-harcokban."},
                    {"type": "dialogue", "speaker": "Bálint Eszter", "text": "Végső soron elengedhetetlen a szekértábor-logika meghaladása. Amíg a művészetet politikai hűségeskük alapján értékelik, addig nemzeti tragédiát élünk át. A valódi kultúra nem a hatalom kiszolgálója, hanem a kritikai öntudat őrzője."},
                    {"type": "narration", "text": "Az alternatív szféra a túlélés új útjait keresi: nemzetközi együttműködések, közösségi finanszírozás és civil műhelyek hálózata épül a hivatalos állami struktúrák mellett."},
                    {"type": "narration", "text": "Mindent egybevetve a magyar szellemi élet jövője a szabadság bástyáinak megőrzésén múlik: a kultúra hegemón uralása tiszavirág-életű, míg a valódi művészi alkotások túlélik a politikai kurzusokat."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Mit jelent a 'kettészakadt kultúra' kifejezés a mai magyar valóságban?", [
                    "Egymással nem kommunikáló, párhuzamosan létező művészeti intézményrendszereket, írószervezeteket és kánonokat a politikai polarizáció mentén.",
                    "A könyvek kettévágását a nyomdákban.",
                    "A színházi függöny kettészakadását az előadás alatt."
                ], 0, ["c1-kulturalisorokseg-vocab"]),
                fb("grammar", "controlled", "Végső soron _____ a szekértábor-logika meghaladása és a párbeszéd helyreállítása. (indispensable / elengedhetetlen)", "elengedhetetlen", "Ultimately overcoming camp mentality and restoring dialogue is indispensable.", ["c1-adv-conclusive-cultural-renewal-synthesis"]),
                match("vocabulary", "controlled", [["kettészakadt kultúra", "politikai törésvonalak mentén elszigetelődött párhuzamos szférák"], ["szekértábor-logika", "a kritikai szempontok feláldozása a törzsi hűségért"], ["kulturális ellenállás", "független műhelyek önfenntartása a közösség erejéből"], ["szellemi megújulás", "az alkotói szabadság és pluralizmus újbóli megteremtése"]], ["c1-kulturalisorokseg-vocab"]),
                fb("grammar", "practice", "Mindent egybevetve a művészeti pluralizmus a nemzet megmaradásának legfőbb _____ . (guarantee / záloga)", "záloga", "All things considered artistic pluralism is the primary guarantee of the nation's survival.", ["c1-adv-conclusive-cultural-renewal-synthesis"]),
                sb("grammar", "practice", ["Végső", "soron", "elengedhetetlen", "a", "szabad", "művészet", "védelme."], ["Végső", "soron", "elengedhetetlen", "a", "szabad", "művészet", "védelme."], "Ultimately the protection of free art is indispensable.", ["c1-adv-conclusive-cultural-renewal-synthesis"]),
                dc("dialogue", [
                    {"speaker": "Kultúrfilozófus", "text": "Hogyan győzhető le a magyar szellemi élet mély megosztottsága?"},
                    {"speaker": "Író", "text": "Csakis úgy, ha felismerjük: mindent egybevetve a szabad alkotás nem hatalmi kiváltság, hanem a társadalom közös _____."},
                    {"speaker": "Kultúrfilozófus", "text": "A szabadság nélküli kultúra elsorvad, s vele sorvad a nemzet is."}
                ], ["közkincse", "bűne", "ára"], 0, ["c1-adv-conclusive-cultural-renewal-synthesis"]),
                sw("production", [{"prompt": "Write a concluding manifesto on artistic autonomy using an evaluative synthesis particle.", "answer": "Végső soron elengedhetetlen a szekértábor-logika meghaladása és az intézményi pluralizmus helyreállítása, hiszen mindent egybevetve a független kultúra a nemzeti önazonosság legfőbb fundamentuma."}], ["c1-adv-conclusive-cultural-renewal-synthesis"]),
                mc("grammar", "check", "Melyik szintetizáló szerkezet fogalmazza meg a kulturális megújulás imperatívuszát a legszebben?", [
                    "végső soron elengedhetetlen a szekértáborok meghaladása / mindent egybevetve a pluralizmus a jövő záloga",
                    "reméljük azért nem lesz baj",
                    "jó lenne ha mindenki békén hagyná a másikat"
                ], 0, ["c1-adv-conclusive-cultural-renewal-synthesis"])
            ]
        }
    ]

    for l in disc_lessons:
        emit_instructional_lesson(29, "discourse", l, disc_title, disc_intro if l["num"] == 1 else None)

    # Combined World Story
    write_json(
        f"stories/world/c1/c1-{slug}-kulturharc-hegemonia.json",
        {
            "id": f"story.c1.{slug}.combined",
            "title": "Kultúrharc és hegemónia: A független művészet küzdelme",
            "level": "C1",
            "lesson": 5,
            "order": 29,
            "type": "world",
            "estimatedMinutes": 8,
            "grammar": ["c1-adv-conclusive-cultural-renewal-synthesis"],
            "summary": "Tényfeltáró esszé a 2010 utáni magyar kultúrpolitika fordulatairól: a szellemi térfoglalásról, a Petőfi Kulturális Ügynökség (PKÜ) forrásmonopóliumáról, a független színházak ellehetetlenüléséről és az Átrium bezárásáról, a Magyar Művészeti Akadémia (MMA) privilégiumairól, valamint a kettészakadt kultúra jövőjéről.",
            "vocabularyTopics": [
                "Cultural Policy Hegemony, the PKÜ Monopoly & the Plight of Independent Theatres",
                "Divided Pantheon: Parallel Cultures & Creative Freedom"
            ],
            "paragraphs": [
                {"type": "narration", "text": "A magyar kulturális élet a 2010-es évektől kezdődően mély, autoriter átalakuláson ment keresztül. A politikai hatalom a 'kulturális korszakváltás' jelszavával nyíltan meghirdette a szellemi térfoglalást, amelynek célja a korábbi pluralista intézményrendszer lebontása és az állami erőforrások ideológiai koncentrációja lett. A független szakmai kuratóriumok helyét a politikai lojalitás alapján kinevezett káderek vették át."},
                {"type": "narration", "text": "A forráskoncentráció leglátványosabb szimbólumává a Petőfi Kulturális Ügynökség (PKÜ) vált: egyetlen kormánybiztosi irányítás alá vont megaintézményi holding kebelezte be az irodalmi lapokat, könnyűzenei támogatásokat és a kiemelt ingatlanvagyont. A művészet nem rendelhető alá egyetlen bürokratikus vízfej diktátumainak, ám a hatalom a forráselvonást a fegyelmezés legfőbb eszközévé tette."},
                {"type": "narration", "text": "A legsúlyosabb csapást a független előadó-művészet szenvedte el: a kulturális TAO eltörlése és a működési pályázatok politikai megvonása következtében minél több milliárdot öntött az állam a lojális kőszínházakba, annál inkább a puszta túlélésért küzdött az alternatív szcéna. Legendás alkotóműhelyek, mint az Átrium Színház kényszerültek bezárásra, míg a független társulatok adománygyűjtésre kényszerültek."},
                {"type": "narration", "text": "Ezzel párhuzamosan az Alaptörvénybe emelt Magyar Művészeti Akadémia (MMA) kiváltságos pozícióba került, felborítva a Nemzeti Kulturális Alap (NKA) korábbi testületi paritását. Kétségkívül bebizonyosodott, hogy a kulturális javak elosztása a hatalmi hűség jutalmává silányult, s a magyar szellemi élet két, egymással nem kommunikáló párhuzamos valóságra szakadt."},
                {"type": "narration", "text": "Végső soron elengedhetetlen felismerni: mindent egybevetve a szekértáborok kíméletlen harca nemzeti önpusztításhoz vezet. A magyar kultúra valódi nagysága mindig a kritikai autonómiában, a sokszínűségben és a szellemi szabadságban gyökerezett, amelyet semmilyen felülről vezényelt politikai hegemónia nem képes végleg elfojtani."}
            ]
        }
    )

    # Discourse Consolidation
    emit_consolidation_lesson(
        29,
        "discourse",
        f"c1-{slug}-consolidation",
        disc_title,
        [
            "I can diagnose cultural hegemony, ideological space capture, and clientele networks.",
            "I can evaluate PKÜ centralization, independent theater defunding, and the abolition of cultural TAO.",
            "I can critique MMA constitutional privileges, parity dissolution in NKA, and formulate manifestos for creative freedom."
        ],
        [
            mc("grammar", "recognize", "Milyen szerkezettel diagnosztizálhatjuk az állami kultúrpolitika ideológiai expanzióját?", [
                "a szellemi térfoglalás szisztematikus stratégiája nyomán / a kultúrpolitikai hegemónia következtében",
                "hogyha valaki új színdarabot rendez",
                "amikor kifestik a színház büféjét"
            ], 0, ["c1-discourse-cultural-hegemony-framing"]),
            mc("grammar", "recognize", "Melyik modális kifejezés rögzíti az alkotói szabadság védelmét a legkategorikusabban?", [
                "a művészet nem rendelhető alá politikai elvárásoknak / kötelességük megvédeni a függetlenséget",
                "szabadon sétálhatnak a színpad deszkáin",
                "bármikor megihatnak egy kávét a büfében"
            ], 0, ["c1-modal-deontic-artistic-autonomy"]),
            match("vocabulary", "recognize", [["szellemi térfoglalás", "a kulturális intézmények ideológiai és személyi megszállása"], ["kulturális holding", "a forrásokat centralizáló PKÜ megaszervezet"], ["kulturális TAO", "a független szférát korábban segítő adótámogatás"], ["MMA", "Magyar Művészeti Akadémia, alkotmányos köztestület"], ["kettészakadt kultúra", "politikai alapon egymástól elszigetelődött művészeti világok"]], ["c1-kulturalisorokseg-vocab"]),
            fb("vocabulary", "recall", "A kulturális javak és intézmények központosított holdingja a _____ . (mega-institution / megaintézmény)", "megaintézmény", "The centralized holding of cultural goods and institutions is a mega-institution.", ["c1-kulturalisorokseg-vocab"]),
            fb("vocabulary", "recall", "A társasági adóból származó, 2018-ban eltörölt színházi támogatás a kulturális _____ . (TAO / TAO)", "TAO", "The theater subsidy derived from corporate tax abolished in 2018 was cultural TAO.", ["c1-kulturalisorokseg-vocab"]),
            fb("grammar", "recall", "A művészet nem _____ alá a hatalom politikai elvárásainak. (cannot be subordinated / rendelhető)", "rendelhető", "Art cannot be subordinated to political expectations of power.", ["c1-modal-deontic-artistic-autonomy"]),
            fb("grammar", "context", "Minél több forrást kap a lojális kör, _____ kevesebb jut a független színházaknak. (the less / annál)", "annál", "The more funds the loyal circle gets, the less goes to independent theaters.", ["c1-adv-proportional-cultural-defunding"]),
            fb("grammar", "context", "Végső soron _____ a szekértábor-logika meghaladása a nemzet jövőjéért. (indispensable / elengedhetetlen)", "elengedhetetlen", "Ultimately overcoming camp mentality is indispensable for the nation's future.", ["c1-adv-conclusive-cultural-renewal-synthesis"]),
            mc("grammar", "context", "Mi a szerepe az episztemikus kifejezéseknek a paritás megszűnésének bírálatában?", [
                "Objektív elemzői súlyt adnak annak kimondására, hogy a döntéshozatal átpolitizálódása megtörtént.",
                "Elnézést kérnek a késve érkező vendégektől.",
                "Megmutatják, mikor kezdődik a színházi előadás."
            ], 0, ["c1-epistemic-ideological-canon-polarization"]),
            sb("grammar", "produce", ["A", "szabad", "művészet", "a", "nemzeti", "demokrácia", "nélkülözhetetlen", "bástyája."], ["A", "szabad", "művészet", "a", "nemzeti", "demokrácia", "nélkülözhetetlen", "bástyája."], "Free art is the indispensable bastion of national democracy.", ["c1-adv-conclusive-cultural-renewal-synthesis"]),
            sw("production", [{"prompt": "Write a critical diagnosis of cultural defunding using a proportional correlative.", "answer": "Minél több tízmilliárdos apanázst juttat a kormányzat a lojális intézményeknek, annál drámaibb működési forráskivonást kénytelenek elszenvedni az alternatív és kísérleti színházi társulatok."}], ["c1-adv-proportional-cultural-defunding"]),
            sw("production", [{"prompt": "Formulate a concluding manifesto on artistic freedom and cultural pluralism.", "answer": "Végső soron elengedhetetlen felismerni: mindent egybevetve az alkotói autonómia és a szellemi pluralizmus tiszteletben tartása a magyar kultúra megmaradásának egyetlen hiteles záloga."}], ["c1-adv-conclusive-cultural-renewal-synthesis"])
        ]
    )

    print("=== Finished C1 Unit 29 ===")


if __name__ == "__main__":
    generate_unit_29()
