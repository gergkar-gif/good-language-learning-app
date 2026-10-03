#!/usr/bin/env python3
"""
Hungarian C1 Block 5 - Unit 25 Generator:
  - Track 1 (Core): Unit 25 — "Constitutionalism, Separation of Powers & The Hierarchy of Legal Norms" (c1-25)
  - Track 2 (Discourse): Unit 25 — "Constitutional Breakdown: The Fundamental Law, Decrees & Institutional Capture" (c1-alkotmanyjog)
"""

import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT))

from scripts.c1_block1.common import mc, match, fb, sb, dc, sw, write_json, emit_instructional_lesson, emit_consolidation_lesson
from scripts.c1_block5.registry_helper import register_unit


def generate_unit_25():
    print("=== Generating C1 Unit 25 ===")
    
    new_skills = {
        "c1-25-vocab": {"kind": "vocabulary"},
        "c1-alkotmanyjog-vocab": {"kind": "vocabulary"},
        "c1-adv-juridical-normative-obligation": {"kind": "grammar"},
        "c1-participle-constitutional-subordination": {"kind": "grammar"},
        "c1-adv-restrictive-legislative-scope": {"kind": "grammar"},
        "c1-modal-teleological-checks-balances": {"kind": "grammar"},
        "c1-adv-scalar-rule-of-law": {"kind": "grammar"},
        "c1-discourse-constitutional-crisis-framing": {"kind": "grammar"},
        "c1-modal-deontic-emergency-decrees": {"kind": "grammar"},
        "c1-adv-proportional-judicial-independence": {"kind": "grammar"},
        "c1-epistemic-constitutional-incompatibility": {"kind": "grammar"},
        "c1-adv-conclusive-democratic-safeguards": {"kind": "grammar"},
    }
    new_titles = {
        "c1-25-vocab": "reading",
        "c1-alkotmanyjog-vocab": "reading",
        "c1-adv-juridical-normative-obligation": "juridical normative adverbials establishing constitutional compliance and statutory mandates",
        "c1-participle-constitutional-subordination": "complex participial structures expressing hierarchy of legal norms and constitutional subordination",
        "c1-adv-restrictive-legislative-scope": "restrictive legislative connectors delineating statutory competences and limits of executive power",
        "c1-modal-teleological-checks-balances": "teleological modal structures framing checks and balances and institutional counterweights",
        "c1-adv-scalar-rule-of-law": "scalar evaluative adverbials assessing constitutional compliance and rule of law standards",
        "c1-discourse-constitutional-crisis-framing": "discourse framing markers diagnosing constitutional erosion and rule of law backsliding",
        "c1-modal-deontic-emergency-decrees": "deontic modal structures critiquing executive governance by decree",
        "c1-adv-proportional-judicial-independence": "proportional correlative conjunctions mapping judicial autonomy against executive encroachment",
        "c1-epistemic-constitutional-incompatibility": "epistemic stance markers articulating unconstitutionality and fundamental rights violations",
        "c1-adv-conclusive-democratic-safeguards": "evaluative synthesis particles formulating constitutional doctrine and democratic restoration",
    }
    
    core_title = "Constitutionalism, Separation of Powers & The Hierarchy of Legal Norms"
    core_stems = [f"c1-25-0{i}" for i in range(1, 6)] + ["c1-25-consolidation"]
    disc_title = "Constitutional Breakdown: The Fundamental Law, Decrees & Institutional Capture"
    disc_stems = [f"c1-alkotmanyjog-0{i}" for i in range(1, 6)] + ["c1-alkotmanyjog-consolidation"]
    
    register_unit(25, core_title, core_stems, disc_title, disc_stems, new_skills, new_titles)

    # ----------------------------------------------------
    # TRACK 1: CORE (c1-25)
    # ----------------------------------------------------
    core_intro = [
        "Modern constitutionalism rests on the premise that power must be divided, checked, and bounded by legal norms to preserve human liberty. In Hungarian legal and political philosophy, Baron József Eötvös was among the first to systematically articulate how unchecked majoritarian power inevitably devolves into absolutism without institutional guarantees.",
        "In this unit, grounded in Eötvös József's seminal magnum opus 'A XIX. század uralkodó eszméinek befolyása az államra' (1851), you will explore the advanced juridical register of public law, statutory interpretation, constitutional hierarchy, and institutional counterweights at the C1 level."
    ]

    core_lessons = [
        {
            "num": 1,
            "stem": "c1-25-01",
            "title": "Constitutional Norms & Juridical Obligation Adverbials",
            "grammar_title": "Juridical Normative Adverbials Establishing Constitutional Compliance and Statutory Mandates",
            "grammar_skill": "c1-adv-juridical-normative-obligation",
            "goals": [
                "I can analyze constitutional norms, fundamental rights, and cogent vs. dispositive legal provisions (*kógens norma, diszpozitív rendelkezés, normatív erő, jogállami követelmény*).",
                "I can employ elevated juridical normative adverbials establishing statutory mandates (*kógens módon, diszpozitív jelleggel, törvényi kötelezettségként, normatív erővel*).",
                "I can critique statutory compliance and legal duties in formal jurisprudence register."
            ],
            "vocab": [
                {"lemma": "kógens norma", "translation": "cogent / peremptory norm", "pos": "expression"},
                {"lemma": "diszpozitív rendelkezés", "translation": "dispositive provision", "pos": "expression"},
                {"lemma": "normatív erő", "translation": "normative force", "pos": "expression"},
                {"lemma": "jogállami követelmény", "translation": "rule of law requirement", "pos": "expression"},
                {"lemma": "hatásköri túllépés", "translation": "exceeding of competence / ultra vires", "pos": "noun"},
                {"lemma": "alanyi jog", "translation": "subjective right / individual entitlement", "pos": "noun"},
                {"lemma": "törvényi felhatalmazás", "translation": "statutory authorization", "pos": "expression"},
                {"lemma": "jogszabályi hierarchia", "translation": "hierarchy of legal norms", "pos": "expression"}
            ],
            "gr_text1": "Juridical normative adverbials establish the mandatory nature, binding force, and statutory modality of legal rules: `kógens módon` (in a peremptory / non-derogable manner), `diszpozitív jelleggel` (dispositively / subject to derogation), `törvényi kötelezettségként` (as a statutory obligation), `normatív erővel` (with normative force), `alkotmányos kötelességként` (as a constitutional duty).",
            "gr_text2": "Example: `A jogszabály kógens módon tiltja a hatásköri túllépést, és törvényi kötelezettségként írja elő a transzparenciát`.",
            "gr_table": [
                ["A jogszabály kógens módon tiltja a hatásköri önkényt.", "The legislation peremptorily prohibits arbitrary abuse of competence."],
                ["A felek diszpozitív jelleggel eltérhetnek a szerződéses mintától.", "The parties may depart dispositively from the contractual template."],
                ["Az államnak alkotmányos kötelességként kell szavatolnia az alapjogokat.", "The state must guarantee fundamental rights as a constitutional duty."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mit jelent a 'kógens norma' a jogtudományban?", [
                    "Olyan kötelező érvényű jogi szabályt, amelytől a felek akarata vagy alsóbb jogszabály nem térhet el.",
                    "Egy udvarias ajánlást a bíróságok felé.",
                    "Olyan szabályt, amely csak ünnepnapokon érvényes."
                ], 0, ["c1-25-vocab"]),
                fb("grammar", "controlled", "Az alkotmánybíráknak _____ módon kell alkalmazniuk a törvény szellemét. (peremptorily / kógens)", "kógens", "Constitutional judges must apply the spirit of the law in a peremptory manner.", ["c1-adv-juridical-normative-obligation"]),
                match("vocabulary", "controlled", [["kógens norma", "eltérést nem engedő jogi szabály"], ["diszpozitív rendelkezés", "megegyezéssel felülírható szabály"], ["hatásköri túllépés", "hatáskör határainak átlépése"], ["alanyi jog", "személyt megillető közvetlen jog"]], ["c1-25-vocab"]),
                fb("grammar", "practice", "A parlamentnek törvényi _____ kell biztosítania a bíróságok költségvetését. (obligation / kötelezettségként)", "kötelezettségként", "Parliament must secure the budget of courts as a statutory obligation.", ["c1-adv-juridical-normative-obligation"]),
                sb("grammar", "practice", ["A", "törvény", "kógens", "módon", "szabja", "meg", "az", "eljárási", "határidőket."], ["A", "törvény", "kógens", "módon", "szabja", "meg", "az", "eljárási", "határidőket."], "The law peremptorily sets procedural deadlines.", ["c1-adv-juridical-normative-obligation"]),
                dc("dialogue", [
                    {"speaker": "Jogász", "text": "Hogyan ítéli meg a minisztérium új utasítását jogállami szempontból?"},
                    {"speaker": "Professzor", "text": "A rendelet _____ módon ütközik a törvényi hierarchiával, ezért jogilag tarthatatlan."},
                    {"speaker": "Jogász", "text": "Akkor kezdeményezzük az azonnali felülvizsgálatot."}
                ], ["kógens", "kedves", "gyors"], 0, ["c1-adv-juridical-normative-obligation"]),
                sw("production", [{"prompt": "Write a sentence formulating an evaluation of statutory obligation using a juridical adverbial.", "answer": "Az államnak alkotmányos kötelességként, kógens módon kell szavatolnia a bíróságok függetlenségét és a polgárok alapvető jogorvoslati jogát."}], ["c1-adv-juridical-normative-obligation"]),
                mc("grammar", "check", "Melyik kifejezés fejez ki kényszerítő, eltérést nem engedő jogi kötöttséget?", [
                    "kógens módon / törvényi kötelezettségként",
                    "diszpozitív jelleggel ha lehet",
                    "esetlegesen és óvatosan"
                ], 0, ["c1-adv-juridical-normative-obligation"])
            ]
        },
        {
            "num": 2,
            "stem": "c1-25-02",
            "title": "Hierarchy of Norms & Participial Subordination Structures",
            "grammar_title": "Complex Participial Structures Expressing Hierarchy of Legal Norms and Constitutional Subordination",
            "grammar_skill": "c1-participle-constitutional-subordination",
            "goals": [
                "I can analyze the hierarchy of legal norms, constitutional supremacy, and derived statutory validity (*jogszabályi hierarchia, alkotmányi szupremácia, levezetett érvényesség*).",
                "I can formulate complex participial structures expressing legal subordination (*az Alaptörvényből levezetett, a felsőbb normának alárendelt, a törvénnyel ütköző*).",
                "I can resolve normative conflicts between statutory acts and executive decrees."
            ],
            "vocab": [
                {"lemma": "alkotmányi szupremácia", "translation": "constitutional supremacy", "pos": "expression"},
                {"lemma": "alacsonyabb szintű jogszabály", "translation": "lower-level legal norm", "pos": "expression"},
                {"lemma": "érvényességi kellék", "translation": "validity requirement", "pos": "expression"},
                {"lemma": "jogforrási hierarchia", "translation": "hierarchy of sources of law", "pos": "expression"},
                {"lemma": "normakontroll", "translation": "norm control / judicial review", "pos": "noun"},
                {"lemma": "jogalkotási hatáskör", "translation": "legislative competence", "pos": "expression"},
                {"lemma": "megsemmisítés", "translation": "annulment / striking down", "pos": "noun"},
                {"lemma": "alkotmánykonform értelmezés", "translation": "constitution-conforming interpretation", "pos": "expression"}
            ],
            "gr_text1": "Participial subordination structures concisely express how legal norms derive their validity from or bow to higher-ranking norms: `az Alaptörvényből levezetett hatáskör` (competence derived from the Fundamental Law), `a magasabb szintű jogszabálynak alárendelt rendelet` (decree subordinated to higher-level norm), `a törvénnyel ütközőnek minősülő passzus` (passage judged conflicting with statute).",
            "gr_text2": "Example: `A bíróság a jogszabályi hierarchiának alárendelt, az alkotmányos alapelvekkel harmonizált rendeletet tekintette irányadónak`.",
            "gr_table": [
                ["Az Alaptörvényből levezetett alapelvek minden jogágra kiterjednek.", "Principles derived from the Fundamental Law extend to all branches of law."],
                ["A magasabb rendű törvénynek alárendelt helyi rendelet nem vezethet be korlátozást.", "A local decree subordinated to higher-ranking statute cannot introduce restrictions."],
                ["Az alkotmánnyal ütközőnek ítélt rendeleti szakaszt a bíróság megsemmisítette.", "The section of the decree judged conflicting with the constitution was annulled by the court."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mi történik a jogforrási hierarchiában, ha egy miniszteri rendelet ütközik egy parlamenti törvénnyel?", [
                    "A törvény magasabb rendű jogforrás, így a miniszteri rendelet érvénytelen vagy megsemmisítendő.",
                    "A miniszteri rendelet automatikusan törli a törvényt.",
                    "A miniszter döntheti el, melyik szöveget veszik figyelembe."
                ], 0, ["c1-25-vocab"]),
                fb("grammar", "controlled", "A parlamentből _____ felhatalmazás képezi a kormányrendelet jogalapját. (derived / eredeztetett)", "eredeztetett", "The authorization derived from parliament forms the legal ground of the government decree.", ["c1-participle-constitutional-subordination"]),
                match("vocabulary", "controlled", [["normakontroll", "jogszabály alkotmányosságának vizsgálata"], ["megsemmisítés", "alkotmányellenes norma törlése"], ["jogforrási hierarchia", "jogszabályok kötelező rangsora"], ["alacsonyabb szintű jogszabály", "törvénynek alárendelt norma"]], ["c1-25-vocab"]),
                fb("grammar", "practice", "Az Alaptörvénynek _____ rendeletet az Alkotmánybíróság haladéktalanul megsemmisítette. (subordinated / alárendelt)", "alárendelt", "The decree subordinated to the Fundamental Law was immediately struck down by the Constitutional Court.", ["c1-participle-constitutional-subordination"]),
                sb("grammar", "practice", ["A", "törvénynek", "alárendelt", "rendelet", "nem", "szűkítheti", "az", "alapjogokat."], ["A", "törvénynek", "alárendelt", "rendelet", "nem", "szűkítheti", "az", "alapjogokat."], "A decree subordinated to a statute cannot narrow fundamental rights.", ["c1-participle-constitutional-subordination"]),
                dc("dialogue", [
                    {"speaker": "Kutató", "text": "Alkalmazhatja a hatóság ezt az új miniszteri utasítást a polgárokkal szemben?"},
                    {"speaker": "Ügyvéd", "text": "Semmiképpen; a törvénynek szigorúan _____ rendelet nem írhat elő új kötelezettséget."},
                    {"speaker": "Kutató", "text": "Akkor bírósági felülvizsgálatot kezdeményezünk."}
                ], ["alárendelt", "fölérendelt", "megkerülő"], 0, ["c1-participle-constitutional-subordination"]),
                sw("production", [{"prompt": "Write a sentence formulating the subordination of a decree to a higher statute using a participial structure.", "answer": "A parlamenti törvénynek szigorúan alárendelt miniszteri rendelet nem tartalmazhat olyan korlátozásokat, amelyek túllépik az anyagi jogi felhatalmazás kereteit."}], ["c1-participle-constitutional-subordination"]),
                mc("grammar", "check", "Melyik szerkezet fejezi ki a jogforrások egymás alá rendeltségét a legpontosabban?", [
                    "a törvénynek hierarchikusan alárendelt rendelet",
                    "a törvény mellett álló jóbarát",
                    "egy szép jogszabályi gyűjtemény"
                ], 0, ["c1-participle-constitutional-subordination"])
            ]
        },
        {
            "num": 3,
            "stem": "c1-25-03",
            "title": "Legislative Competence & Restrictive Connectors",
            "grammar_title": "Restrictive Legislative Connectors Delineating Statutory Competences and Limits of Executive Power",
            "grammar_skill": "c1-adv-restrictive-legislative-scope",
            "goals": [
                "I can define exclusive legislative competence and statutory authorization (*kizárólagos törvényhozási tárgykör, felhatalmazás terjedelme, hatásköri korlát*).",
                "I can deploy restrictive connectors delineating executive limits (*kizárólag törvényi felhatalmazás alapján, a hatásköri korlátokat nem túllépve, amennyiben a törvény engedi*).",
                "I can argue against executive encroachment into parliamentary domains."
            ],
            "vocab": [
                {"lemma": "kizárólagos tárgykör", "translation": "exclusive statutory subject-matter", "pos": "expression"},
                {"lemma": "végrehajtó hatalom", "translation": "executive power", "pos": "expression"},
                {"lemma": "rendeletalkotási jog", "translation": "decree-making power", "pos": "expression"},
                {"lemma": "hatáskörelvonás", "translation": "usurpation / stripping of competence", "pos": "noun"},
                {"lemma": "törvényhozói monopólium", "translation": "legislative monopoly", "pos": "expression"},
                {"lemma": "túllépés", "translation": "exceeding / overreach", "pos": "noun"},
                {"lemma": "törvényességi felügyelet", "translation": "legality supervision", "pos": "expression"},
                {"lemma": "joghézag", "translation": "lacuna / legal loophole", "pos": "noun"}
            ],
            "gr_text1": "Restrictive connectors delineate the exact boundaries within which executive agencies may act without overstepping legislative will: `kizárólag törvényi felhatalmazás alapján` (solely upon statutory authorization), `a törvényi kereteken belül maradva` (remaining within statutory boundaries), `a hatásköri korlátokat nem túllépve` (without exceeding jurisdictional boundaries), `mindazonáltal kizárólag annyiban` (nevertheless solely insofar as).",
            "gr_text2": "Example: `A minisztérium kizárólag törvényi felhatalmazás alapján, a hatásköri korlátokat szigorúan tiszteletben tartva adhat ki részletszabályokat`.",
            "gr_table": [
                ["A kormány kizárólag törvényi felhatalmazás alapján hozhat döntést.", "The government may make decisions solely on the basis of statutory authorization."],
                ["A hatásköri korlátokat nem túllépve a hatóság csak a tényeket vizsgálhatja.", "Without exceeding competence limits, the authority may only examine facts."],
                ["Alapvető jogok korlátozására kizárólag törvényhozási úton kerülhet sor.", "Restriction of fundamental rights may take place solely via legislative channels."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mely kérdések tartoznak a 'kizárólagos törvényhozási tárgykörbe'?", [
                    "Az alapvető jogok korlátozása és az államszervezet alapvető intézményeinek létrehozása.",
                    "A minisztériumi irodák bútorzatának megvásárlása.",
                    "A pénteki parlamenti büfé menüjének összeállítása."
                ], 0, ["c1-25-vocab"]),
                fb("grammar", "controlled", "A kormány _____ törvényi felhatalmazás alapján szabhat ki kötelezettséget. (solely / kizárólag)", "kizárólag", "The government may impose obligations solely on the basis of statutory authorization.", ["c1-adv-restrictive-legislative-scope"]),
                match("vocabulary", "controlled", [["végrehajtó hatalom", "a törvényeket végrehajtó kormányzat"], ["hatáskörelvonás", "jogosítványok jogellenes elvétele"], ["törvényességi felügyelet", "működés jogi ellenőrzése"], ["törvényhozói monopólium", "kizárólag parlament által szabályozható tárgykör"]], ["c1-25-vocab"]),
                fb("grammar", "practice", "A miniszter a hatásköri korlátokat nem _____ járt el a rendelet megalkotásakor. (exceeding / túllépve)", "túllépve", "The minister acted without exceeding limits of competence when drafting the decree.", ["c1-adv-restrictive-legislative-scope"]),
                sb("grammar", "practice", ["Kizárólag", "törvényi", "úton", "lehet", "korlátozni", "az", "állampolgárok", "szabadságát."], ["Kizárólag", "törvényi", "úton", "lehet", "korlátozni", "az", "állampolgárok", "szabadságát."], "Citizens' freedom can solely be restricted through statutory channels.", ["c1-adv-restrictive-legislative-scope"]),
                dc("dialogue", [
                    {"speaker": "Képviselő", "text": "Szabályozhatja-e a minisztérium ezt az új adónemet egyszerű rendeletben?"},
                    {"speaker": "Jogtudós", "text": "Nem; adót kivetni _____ törvényi felhatalmazás alapján lehetséges, a rendeleti bevezetés jogellenes."},
                    {"speaker": "Képviselő", "text": "Akkor megtámadjuk a rendeletet az Alkotmánybíróságon."}
                ], ["kizárólag", "esetlegesen", "alkalmanként"], 0, ["c1-adv-restrictive-legislative-scope"]),
                sw("production", [{"prompt": "Write a sentence defining the limits of executive power using 'kizárólag törvényi felhatalmazás alapján'.", "answer": "A közigazgatási hatóságok kizárólag törvényi felhatalmazás alapján, a jogállami hatásköri korlátokat szigorúan tiszteletben tartva avatkozhatnak be az állampolgárok jogaiba."}], ["c1-adv-restrictive-legislative-scope"]),
                mc("grammar", "check", "Melyik kifejezés szab szigorú határt a kormányzati beavatkozásnak a jogállamban?", [
                    "kizárólag törvényi felhatalmazás alapján / hatásköri korlátokat nem túllépve",
                    "ahogy a miniszter úr jónak látja",
                    "tetszőleges időpontban"
                ], 0, ["c1-adv-restrictive-legislative-scope"])
            ]
        },
        {
            "num": 4,
            "stem": "c1-25-04",
            "title": "Checks and Balances & Teleological Modals",
            "grammar_title": "Teleological Modal Structures Framing Checks and Balances and Institutional Counterweights",
            "grammar_skill": "c1-modal-teleological-checks-balances",
            "goals": [
                "I can articulate institutional counterweights, checks and balances, and mutual oversight (*fékek és ellensúlyok, intézményi ellensúly, kölcsönös ellenőrzés*).",
                "I can employ teleological modal structures expressing institutional design (*a hatalomkoncentráció megakadályozása végett, az intézményi függetlenség megőrzése céljából*).",
                "I can debate the necessity of independent regulatory authorities in a democracy."
            ],
            "vocab": [
                {"lemma": "fékek és ellensúlyok", "translation": "checks and balances", "pos": "expression"},
                {"lemma": "hatalommegosztás", "translation": "separation of powers", "pos": "noun"},
                {"lemma": "intézményi ellensúly", "translation": "institutional counterweight", "pos": "expression"},
                {"lemma": "hatalomkoncentráció", "translation": "concentration of power", "pos": "noun"},
                {"lemma": "bírói függetlenség", "translation": "judicial independence", "pos": "expression"},
                {"lemma": "független ellenőrző szerv", "translation": "independent supervisory organ", "pos": "expression"},
                {"lemma": "kölcsönös fék", "translation": "mutual check", "pos": "expression"},
                {"lemma": "önkényuralom", "translation": "tyranny / autocracy", "pos": "noun"}
            ],
            "gr_text1": "Teleological postpositional and modal expressions frame institutional architecture by highlighting the purpose of power constraints: `a fékek és ellensúlyok biztosítása céljából` (for the purpose of securing checks and balances), `az önkény megakadályozása végett` (in order to prevent arbitrariness), `a bírói függetlenség védelmére hivatottan` (designated to protect judicial independence), `abból a célból, hogy a hatalom ne összpontosulhasson egyetlen kézben` (with the aim that power may not concentrate in a single hand).",
            "gr_text2": "Example: `A jogalkotó az alkotmányos fékek és ellensúlyok fenntartása céljából független felügyeleti intézményeket hozott létre`.",
            "gr_table": [
                ["A fékek és ellensúlyok fenntartása céljából független bíróságokra van szükség.", "Independent courts are needed for the purpose of maintaining checks and balances."],
                ["A hatalomkoncentráció megakadályozása végett különülnek el a hatalmi ágak.", "Branches of power are separated in order to prevent power concentration."],
                ["Az Alkotmánybíróság a törvényesség őreként a jogbiztonság garantálására hivatott.", "The Constitutional Court as guardian of legality is designated to guarantee legal certainty."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mi a lényege a 'fékek és ellensúlyok' (checks and balances) elvének?", [
                    "A három hatalmi ág egymást kölcsönösen ellenőrzi és korlátozza, megakadályozva az önkényt.",
                    "A parlament minden évben új féket szerel az állami gépjárművekre.",
                    "A miniszterek és a képviselők közösen szavaznak a miniszterelnök fizetéséről."
                ], 0, ["c1-25-vocab"]),
                fb("grammar", "controlled", "A hatalomkoncentráció megelőzése _____ hozták létre az önálló felügyeleti szerveket. (in order to / végett)", "végett", "Autonomous supervisory organs were established in order to prevent concentration of power.", ["c1-modal-teleological-checks-balances"]),
                match("vocabulary", "controlled", [["hatalommegosztás", "törvényhozó, végrehajtó és bírói hatalom elválasztása"], ["intézményi ellensúly", "a túlhatalmat korlátozó szerv"], ["bírói függetlenség", "bírák politikai befolyástól való mentessége"], ["önkényuralom", "törvényes korlátok nélküli uralkodás"]], ["c1-25-vocab"]),
                fb("grammar", "practice", "A jogbiztonság megőrzése _____ a bíróságok döntéseit semmilyen kormányzati szerv nem írhatja felül. (for the purpose of / céljából)", "céljából", "For the purpose of preserving legal certainty, no government body may override court decisions.", ["c1-modal-teleological-checks-balances"]),
                sb("grammar", "practice", ["A", "kölcsönös", "fékek", "és", "ellensúlyok", "rendszere", "a", "demokrácia", "záloga."], ["A", "kölcsönös", "fékek", "és", "ellensúlyok", "rendszere", "a", "demokrácia", "záloga."], "The system of mutual checks and balances is the pledge of democracy.", ["c1-modal-teleological-checks-balances"]),
                dc("dialogue", [
                    {"speaker": "Egyetemi hallgató", "text": "Miért van szükség ombudsmanra és önálló számvevőszékre?"},
                    {"speaker": "Professzor", "text": "Az önkény megelőzése _____ elengedhetetlenek az olyan intézményi ellensúlyok, amelyek a kormánytól függetlenül vizsgálódnak."},
                    {"speaker": "Egyetemi hallgató", "text": "Így marad fenn az alkotmányos egyensúly."}
                ], ["végett", "ellenére", "dacára"], 0, ["c1-modal-teleological-checks-balances"]),
                sw("production", [{"prompt": "Write a sentence formulating the purpose of institutional counterweights using 'céljából' or 'végett'.", "answer": "Az államhatalmi ágak szétválasztása és a fékek és ellensúlyok fenntartása céljából a demokráciák független bíróságokat és autonóm ellenőrző hatóságokat működtetnek."}], ["c1-modal-teleological-checks-balances"]),
                mc("grammar", "check", "Melyik szerkezet fejez ki intézményi célkitűzést emelkedett alkotmányjogi regiszterben?", [
                    "a fékek és ellensúlyok fenntartása céljából / az önkény megakadályozása végett",
                    "hogy ne kelljen dolgozni délután",
                    "mert mindenki elfáradt a vitában"
                ], 0, ["c1-modal-teleological-checks-balances"])
            ]
        },
        {
            "num": 5,
            "stem": "c1-25-05",
            "title": "Eötvös József: The Dominant Ideas of the 19th Century & Scalar Adverbials",
            "grammar_title": "Scalar Evaluative Adverbials Assessing Constitutional Compliance and Rule of Law Standards",
            "grammar_skill": "c1-adv-scalar-rule-of-law",
            "goals": [
                "I can analyze Eötvös József's philosophical treatise on the state, liberty, and institutional guarantees against majority despotism.",
                "I can calibrate constitutional compliance using scalar evaluative adverbials (*alkotmányjogilag aggálytalanul, jogállami szempontból aggasztóan, maradéktalanul eleget téve*).",
                "I can critique 19th-century liberal constitutional theory and its modern relevance."
            ],
            "vocab": [
                {"lemma": "többségi despotizmus", "translation": "majority despotism / tyranny of majority", "pos": "expression"},
                {"lemma": "egyéni szabadság", "translation": "individual liberty", "pos": "expression"},
                {"lemma": "állami omnipotencia", "translation": "state omnipotence", "pos": "expression"},
                {"lemma": "közigazgatási centralizáció", "translation": "administrative centralization", "pos": "expression"},
                {"lemma": "törvény előtti egyenlőség", "translation": "equality before the law", "pos": "expression"},
                {"lemma": "önkormányzatiság", "translation": "self-government / local autonomy", "pos": "noun"},
                {"lemma": "intézményi garancia", "translation": "institutional guarantee", "pos": "expression"},
                {"lemma": "joguralom", "translation": "rule of law / supremacy of law", "pos": "noun"}
            ],
            "gr_text1": "Scalar evaluative adverbials assess the degree, precision, or legitimacy of constitutional alignment: `alkotmányjogilag aggálytalanul` (constitutionally unproblematic), `jogállami szempontból mélységesen aggasztóan` (deeply alarming from a rule of law standpoint), `a jogbiztonság követelményének maradéktalanul eleget téve` (fully satisfying the requirement of legal certainty), `lényegét tekintve antidemokratikusan` (essentially antidemocratic in nature).",
            "gr_text2": "Example: `A tervezet a jogállami követelményeknek maradéktalanul eleget téve garantálja az állampolgárok alkotmányos jogorvoslati jogát`.",
            "gr_table": [
                ["A reform a jogbiztonság követelményének maradéktalanul eleget téve valósult meg.", "The reform was implemented fully satisfying the requirement of legal certainty."],
                ["A hatáskörök koncentrációja jogállami szempontból aggasztóan növeli a kormány súlyát.", "The concentration of competences alarmingly increases government weight from a rule of law perspective."],
                ["A törvényszöveg alkotmányjogilag aggálytalanul illeszkedik az európai jogrendbe.", "The statutory text fits unproblematically from a constitutional law perspective into the European legal order."]
            ],
            "classic_story": {
                "slug": "eotvos-uralkodo-eszmek",
                "title": "A XIX. század uralkodó eszméinek befolyása az államra",
                "author": "Báró Eötvös József",
                "work": "A XIX. század uralkodó eszméinek befolyása az államra (1851)",
                "summary": "Báró Eötvös József klasszikus államtudományi értekezése a szabadság, az egyenlőség és a nemzetiség eszméinek feszültségét, valamint a korlátlan államhatalom veszélyeit elemzi. Eötvös zseniális meglátása szerint a népfelség elve önmagában nem óv meg a zsarnokságtól: a többség despotizmusa éppoly veszedelmes lehet az egyéni szabadságra, mint a monarchikus abszolutizmus, ha hiányoznak a szabad önkormányzatok és az intézményes ellensúlyok.",
                "characters": ["Eötvös József, a jogállam és liberalizmus filozófusa"],
                "paragraphs": [
                    {"type": "narration", "text": "Midőn a tizenkilencedik század hajnalán a szabadság, egyenlőség és nemzetiség eszméi fellobbantak Európában, az emberiség azt hitte, hogy a zsarnokság korszaka végleg leáldozott. Ám a szabadság nem pusztán a hatalom forrásának megváltoztatását jelenti: ha az abszolút királyi hatalmat az abszolút néptöbbség hatalma váltja fel a korlátok lebontásával, a szabadság illúzióvá foszlik, s helyébe a legnyomasztóbb többségi despotizmus lép."},
                    {"type": "dialogue", "speaker": "Eötvös József", "text": "A szabadság legfőbb biztosítéka nem abban áll, hogy ki gyakorolja a hatalmat, hanem abban, hogy miként korlátozzák azt. Az állami omnipotencia elmélete, mely szerint az állam minden egyéni jog forrása és ura, egyenesen a rabszolgasághoz vezet, bármely szép jelszavakkal álcázza is magát."},
                    {"type": "narration", "text": "Eötvös mély meggyőződéssel mutatott rá: a centralizált közigazgatás, amely felszámolja a helyi közösségek autonómiáját és a szabad önkormányzatokat, megfosztja a polgárokat a közéletben való valóságos részvételtől. Ha nincsenek közbeeső testületek az állami főhatalom és az elszigetelt polgár között, a társadalom atomizálódik, és védtelen prédájává válik a mindenkori kormánynak."},
                    {"type": "narration", "text": "A jogbiztonság követelményének maradéktalanul eleget téve kell tehát felépíteni a szabad államot: olyan intézményi garanciákkal, amelyek védik a kisebbséget a többség pillanatnyi szeszélyeitől, tiszteletben tartják az egyén elidegeníthetetlen alanyi jogait, és a törvényuralmat emelik a politikai önkény fölé."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Milyen veszélyre figyelmeztet Eötvös József 'A XIX. század uralkodó eszméi' című művében?", [
                    "Arra, hogy a korlátlan többségi hatalom éppúgy despotizmussá fajulhat, mint az abszolutista uralkodóé.",
                    "Arra, hogy a könyvnyomtatás miatt túl sok könyvet fognak olvasni a parasztok.",
                    "Arra, hogy a vasút elterjedése tönkreteszi a lótenyésztést."
                ], 0, ["c1-25-vocab"]),
                fb("grammar", "controlled", "A törvényjavaslat a jogbiztonság követelményének _____ eleget téve került elfogadásra. (fully / maradéktalanul)", "maradéktalanul", "The draft statute was adopted fully satisfying the requirement of legal certainty.", ["c1-adv-scalar-rule-of-law"]),
                match("vocabulary", "controlled", [["többségi despotizmus", "a többség zsarnoki, korlátlan uralma"], ["állami omnipotencia", "a mindent uraló állam elmélete"], ["önkormányzatiság", "helyi közösségek autonóm igazgatása"], ["joguralom", "a törvények feltétlen uralma az egyéni szeszélyek felett"]], ["c1-25-vocab"]),
                fb("grammar", "practice", "A jogászi elemzés szerint az eljárás jogállami szempontból _____ módon sértette az ártatlanság vélelmét. (alarmingly / aggasztó)", "aggasztó", "According to the legal analysis, the procedure violated the presumption of innocence in an alarming manner from a rule of law perspective.", ["c1-adv-scalar-rule-of-law"]),
                sb("grammar", "practice", ["Az", "intézményi", "garanciák", "maradéktalanul", "védik", "az", "egyéni", "szabadságjogokat."], ["Az", "intézményi", "garanciák", "maradéktalanul", "védik", "az", "egyéni", "szabadságjogokat."], "Institutional guarantees fully protect individual liberties.", ["c1-adv-scalar-rule-of-law"]),
                mc("reading", "context", "Miért tekinti Eötvös létfontosságúnak a helyi önkormányzatokat?", [
                    "Mert közbeeső autonóm testületként megvédik az egyént az állami központi hatalom omnipotenciájától.",
                    "Mert az önkormányzatok fizethetik a legmagasabb adókat a kincstárnak.",
                    "Mert ott lehet a leggyorsabban postagalambokat tartani."
                ], 0, ["c1-25-vocab"]),
                sw("production", [{"prompt": "Write a reflection on Eötvös József's warning about majority despotism using 'maradéktalanul eleget téve'.", "answer": "Eötvös József szerint az igazi szabadság csak a jogállami normáknak maradéktalanul eleget tévő intézményes ellensúlyok és szabad önkormányzatok révén maradhat fenn a többségi despotizmussal szemben."}], ["c1-adv-scalar-rule-of-law"]),
                mc("grammar", "check", "Melyik határozó alkalmas a jogállamisági megfelelés emelkedett, fokozati kifejezésére?", [
                    "maradéktalanul eleget téve / jogállami szempontból aggasztóan",
                    "kicsit sem törődve vele",
                    "vidáman dalolva"
                ], 0, ["c1-adv-scalar-rule-of-law"])
            ]
        }
    ]

    for l in core_lessons:
        emit_instructional_lesson(25, "core", l, core_title, core_intro if l["num"] == 1 else None)

    # Core Consolidation Lesson
    emit_consolidation_lesson(
        25,
        "core",
        "c1-25-consolidation",
        core_title,
        [
            "I can master advanced public law and constitutional terminology (*kógens norma, jogforrási hierarchia, fékek és ellensúlyok*).",
            "I can formulate complex participial subordination and restrictive legislative connectors (*az Alaptörvényből levezetett, kizárólag törvényi felhatalmazás alapján*).",
            "I can synthesize Eötvös József's political philosophy on institutional counterweights against majority tyranny."
        ],
        [
            mc("grammar", "recognize", "Melyik kifejezés jelöl kötelező, eltérést nem engedő törvényi rendelkezést?", [
                "kógens norma / kógens módon előírt kötelezettség",
                "diszpozitív tanács a feleknek",
                "politikai sajtóközlemény"
            ], 0, ["c1-adv-juridical-normative-obligation"]),
            mc("grammar", "recognize", "Melyik szerkezet fejez ki intézményi alárendeltséget a jogforrási hierarchiában?", [
                "a magasabb szintű jogszabálynak alárendelt miniszteri rendelet",
                "amikor a miniszter levelet ír a képviselőnek",
                "a parlament üléstermének fűtési szabályzata"
            ], 0, ["c1-participle-constitutional-subordination"]),
            match("vocabulary", "recognize", [["kógens norma", "kivételt nem tűrő kötelező jogszabály"], ["normakontroll", "törvények alkotmánybírósági felülvizsgálata"], ["hatalommegosztás", "államhatalmi ágak elválasztása és egyensúlya"], ["többségi despotizmus", "a törvényes korlátok nélküli többségi túlhatalom"], ["alanyi jog", "személyt megillető érvényesíthető jogosultság"]], ["c1-25-vocab"]),
            fb("vocabulary", "recall", "A jogszabályok kötelező érvényességi rangsorát jogszabályi _____ nevezzük. (hierarchy / hierarchiának)", "hierarchiának", "The mandatory validity ranking of legal norms is called hierarchy of legal norms.", ["c1-25-vocab"]),
            fb("vocabulary", "recall", "A többség zsarnokságát Eötvös nyomán többségi _____ hívjuk. (despotism / despotizmusnak)", "despotizmusnak", "The tyranny of majority following Eötvös is called majority despotism.", ["c1-25-vocab"]),
            fb("grammar", "recall", "A kormány szervei kizárólag törvényi _____ alapján gyakorolhatják hatalmukat. (authorization / felhatalmazás)", "felhatalmazás", "Organs of the government may exercise their power solely on the basis of statutory authorization.", ["c1-adv-restrictive-legislative-scope"]),
            fb("grammar", "context", "A parlament a fékek és ellensúlyok megőrzése _____ alkotott új törvényt. (for the purpose of / céljából)", "céljából", "Parliament enacted a new statute for the purpose of preserving checks and balances.", ["c1-modal-teleological-checks-balances"]),
            fb("grammar", "context", "A határozat a jogállamiság elvének _____ eleget téve védi az egyéni szabadságot. (fully / maradéktalanul)", "maradéktalanul", "The resolution protects individual liberty fully satisfying the principle of the rule of law.", ["c1-adv-scalar-rule-of-law"]),
            mc("grammar", "context", "Hogyan szolgálja a 'kizárólag törvényi felhatalmazás alapján' fordulat a jogbiztonságot?", [
                "Kijelöli, hogy az államigazgatás nem alkothat önkényesen új kötelezettségeket a polgárok számára parlamenti jóváhagyás nélkül.",
                "Megengedi a rendőrségnek, hogy bármikor bírságoljon.",
                "Eltörli az adófizetési kötelezettséget."
            ], 0, ["c1-adv-restrictive-legislative-scope"]),
            sb("grammar", "produce", ["A", "hatalommegosztás", "és", "a", "joguralom", "a", "szabad", "társadalom", "alappillérei."], ["A", "hatalommegosztás", "és", "a", "joguralom", "a", "szabad", "társadalom", "alappillérei."], "Separation of powers and the rule of law are the fundamental pillars of a free society.", ["c1-adv-scalar-rule-of-law"]),
            sw("production", [{"prompt": "Formulate a statement on why statutory authorization is mandatory for state authorities.", "answer": "A közigazgatási hatóságok kizárólag törvényi felhatalmazás alapján járhatnak el, mivel a jogállami hierarchia nem engedi a végrehajtó hatalom önkényes jogalkotását."}], ["c1-adv-restrictive-legislative-scope"]),
            sw("production", [{"prompt": "Write a critical reflection on Eötvös József's warning about majority despotism.", "answer": "Eötvös József felismerése szerint az alkotmányos fékek és ellensúlyok hiányában a parlamenti többség könnyen despotizmussá fajulhat, ezért a jogbiztonság követelményének maradéktalanul eleget téve meg kell védeni az egyéni szabadságjogokat."}], ["c1-adv-scalar-rule-of-law"])
        ]
    )

    # ----------------------------------------------------
    # TRACK 2: DISCOURSE (c1-alkotmanyjog)
    # ----------------------------------------------------
    slug = "alkotmanyjog"
    disc_intro = [
        "In 2011, Hungary adopted a new constitution—the Fundamental Law (*Alaptörvény*)—marking the beginning of an era of profound constitutional transformation. The dismantling of the system of checks and balances, the curtailment of Constitutional Court powers, and continuous governance by emergency decree (*veszélyhelyzet*) have ignited intense domestic and international controversy over the rule of law.",
        "In this discourse unit, through five serialized investigative accounts, you will analyze the legal mechanisms of democratic backsliding, decree governance, institutional capture, and the European rule of law conditionality mechanism at the C1 level."
    ]

    disc_lessons = [
        {
            "num": 1,
            "stem": f"c1-{slug}-01",
            "title": "The 2011 Fundamental Law & Constitutional Erosion Framing",
            "grammar_title": "Discourse Framing Markers Diagnosing Constitutional Erosion and Rule of Law Backsliding",
            "grammar_skill": "c1-discourse-constitutional-crisis-framing",
            "goals": [
                "I can analyze the transition from the 1989 Constitution to the 2011 Fundamental Law (*Alaptörvény, egypárti alkotmányozás, alkotmányos kontinuitás*).",
                "I can deploy discourse framing markers diagnosing constitutional backsliding (*az alkotmányos fékek felszámolása, a jogállami normák szisztematikus erodálása, egyoldalú hatalomgyakorlás keretében*).",
                "I can debate the democratic legitimacy of unilaterally enacted constitutions."
            ],
            "vocab": [
                {"lemma": "Alaptörvény", "translation": "Fundamental Law (Hungarian constitution)", "pos": "noun"},
                {"lemma": "egypárti alkotmányozás", "translation": "single-party constitution-making", "pos": "expression"},
                {"lemma": "történeti alkotmány", "translation": "historical constitution", "pos": "expression"},
                {"lemma": "Nemzeti Hitvallás", "translation": "National Avowal (preamble)", "pos": "expression"},
                {"lemma": "kétharmados többség", "translation": "two-thirds majority / supermajority", "pos": "expression"},
                {"lemma": "sarkalatos törvény", "translation": "cardinal law", "pos": "expression"},
                {"lemma": "demokratikus legitimitás", "translation": "democratic legitimacy", "pos": "expression"},
                {"lemma": "visszalépés", "translation": "backsliding / regression", "pos": "noun"}
            ],
            "gr_text1": "Discourse framing markers diagnose systemic structural changes and democratic deterioration: `az alkotmányos fékek szisztematikus lebontása` (systematic dismantling of constitutional checks), `a jogállami normák fokozatos erodálása` (gradual erosion of rule-of-law norms), `az egypárti hatalomgyakorlás jegyében` (in the spirit of single-party exercise of power), `a konszenzusos demokrácia felszámolásaként értékelhető módon` (in a manner evaluable as the liquidation of consensual democracy).",
            "gr_text2": "Example: `A jogtudósok a jogállami normák szisztematikus erodálásaként írták le az új alkotmányozási eljárást`.",
            "gr_table": [
                ["A jogállami normák szisztematikus erodálása nemzetközi tiltakozást váltott ki.", "The systematic erosion of rule of law norms triggered international protest."],
                ["Az alkotmányos fékek lebontása egyoldalú hatalomgyakorlást eredményezett.", "The dismantling of constitutional checks resulted in unilateral exercise of power."],
                ["A sarkalatos törvények kiterjesztése a jövőbeli kormányok mozgásterét szűkíti le.", "The expansion of cardinal laws restricts the room for maneuver of future governments."]
            ],
            "world_story_seg": {
                "seg_slug": "alaptorveny-szuletese",
                "title": "Az Alaptörvény születése és a konszenzus hiánya",
                "summary": "2011 tavaszán a parlamenti kétharmad elfogadta az új Alaptörvényt, lezárva a harmadik köztársaság 1989-es alkotmányos korszakát. A vita azonnal fellángolt a társadalmi egyeztetés hiánya és az egyoldalú politikai akarat miatt.",
                "paragraphs": [
                    {"type": "narration", "text": "2011 húsvéthétfőjén a parlamenti patkóban megszületett az új Alaptörvény. A kormánypártok kétharmados többsége történelmi pillanatként, a posztkommunista átmenet végleges lezárásaként ünnepelte a Nemzeti Hitvallással bevezetett szöveget."},
                    {"type": "dialogue", "speaker": "Dr. Varga Dániel alkotmányjogász", "text": "Az alkotmány nem lehet egyetlen párt politikai manifesztuma. A valódi alkotmányozás széles társadalmi párbeszédet és konszenzust követel, nem pedig az ellenzék kizárásával végigvitt rohammunkát."},
                    {"type": "narration", "text": "A kritikusok rámutattak: a jogállami normák szisztematikus erodálása éppen azzal kezdődött, hogy sarkalatos törvények tömegével betonozta be a kormányzat politikai és gazdasági preferenciáit, megkötve a jövőbeli egyszerű többségű kormányok kezét."},
                    {"type": "narration", "text": "A Velencei Bizottság jelentései hamarosan megerősítették az aggodalmakat: az új szöveg az alkotmányos fékek felszámolása felé terelte a magyar államberendezkedést."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Mi a 'sarkalatos törvény' sajátossága a magyar közjogban?", [
                    "Olyan törvény, amelynek elfogadásához és módosításához a jelenlévő országgyűlési képviselők kétharmadának szavazata szükséges.",
                    "Olyan törvény, amelyet csak vasárnap délben hirdethetnek ki.",
                    "Kizárólag a katonaság működésére vonatkozó jogszabály."
                ], 0, ["c1-alkotmanyjog-vocab"]),
                fb("grammar", "controlled", "A szakértők a jogállami normák _____ erodálásaként értékelték az alkotmányozás folyamatát. (systematic / szisztematikus)", "szisztematikus", "Experts evaluated the process of constitution-making as the systematic erosion of rule of law norms.", ["c1-discourse-constitutional-crisis-framing"]),
                match("vocabulary", "controlled", [["Alaptörvény", "Magyarország jelenlegi alaptörvénye"], ["sarkalatos törvény", "kétharmados többséget igénylő törvény"], ["Nemzeti Hitvallás", "az Alaptörvény preambuluma"], ["történeti alkotmány", "íratlan magyar közjogi hagyomány"]], ["c1-alkotmanyjog-vocab"]),
                fb("grammar", "practice", "Az alkotmányos fékek _____ nyomán a hatalom megosztatlanul összpontosult a kormány kezében. (dismantling / felszámolása)", "felszámolása", "Following the dismantling of constitutional checks, power concentrated undivided in the hands of the government.", ["c1-discourse-constitutional-crisis-framing"]),
                sb("grammar", "practice", ["Az", "egypárti", "alkotmányozás", "aláásta", "a", "társadalmi", "konszenzus", "lehetőségét."], ["Az", "egypárti", "alkotmányozás", "aláásta", "a", "társadalmi", "konszenzus", "lehetőségét."], "Single-party constitution-making undermined the possibility of social consensus.", ["c1-discourse-constitutional-crisis-framing"]),
                dc("dialogue", [
                    {"speaker": "Újságíró", "text": "Mi volt a legfőbb nemzetközi bírálat az új Alaptörvénnyel szemben?"},
                    {"speaker": "Jogász", "text": "Az alkotmányos fékek felszámolása és a jogállami normák _____ erodálása keltett riadalmat."},
                    {"speaker": "Újságíró", "text": "Ezért indított vizsgálatot a Velencei Bizottság."}
                ], ["szisztematikus", "szép", "ritka"], 0, ["c1-discourse-constitutional-crisis-framing"]),
                sw("production", [{"prompt": "Write a critical diagnosis of constitutional erosion using a crisis framing marker.", "answer": "Az új Alaptörvény egypárti elfogadása és a sarkalatos törvények túlzott kiterjesztése a jogállami normák szisztematikus erodálását eredményezte Magyarországon."}], ["c1-discourse-constitutional-crisis-framing"]),
                mc("grammar", "check", "Melyik kifejezés diagnosztizálja a jogállami leépülést mélyenszántó közjogi stílusban?", [
                    "a jogállami normák szisztematikus erodálása / az alkotmányos fékek felszámolása",
                    "hirtelen változások a hétvégén",
                    "érdekes hírek az újságban"
                ], 0, ["c1-discourse-constitutional-crisis-framing"])
            ]
        },
        {
            "num": 2,
            "stem": f"c1-{slug}-02",
            "title": "Curtailment of the Constitutional Court & Deontic Limits",
            "grammar_title": "Deontic Modal Structures Critiquing Executive Governance by Decree and State of Danger",
            "grammar_skill": "c1-modal-deontic-emergency-decrees",
            "goals": [
                "I can analyze the curtailment of Constitutional Court powers and the abolition of actio popularis (*actio popularis megszüntetése, költségvetési felülvizsgálat korlátozása, hatáskörcsorbítás*).",
                "I can formulate deontic modal structures condemning unconstitutional power grabs (*nem csorbíthatja a hatásköröket, vissza kell állítania a függetlenséget, nem írhatja felül az alapjogokat*).",
                "I can debate the role of judicial review in safeguarding constitutional democracy."
            ],
            "vocab": [
                {"lemma": "actio popularis", "translation": "popular action (anyone can petition the Constitutional Court)", "pos": "noun"},
                {"lemma": "költségvetési korlátozás", "translation": "fiscal competence limitation", "pos": "expression"},
                {"lemma": "testületi létszám bővítése", "translation": "court packing / expanding bench size", "pos": "expression"},
                {"lemma": "bíróválasztási szabály", "translation": "judicial nomination rule", "pos": "expression"},
                {"lemma": "hatáskörcsorbítás", "translation": "curtailment of competence", "pos": "noun"},
                {"lemma": "alkotmányjogi panasz", "translation": "constitutional complaint", "pos": "expression"},
                {"lemma": "hatásköri korlát", "translation": "jurisdictional limit", "pos": "expression"},
                {"lemma": "érdemi kontroll", "translation": "merit-based oversight", "pos": "expression"}
            ],
            "gr_text1": "Deontic modal structures articulate statutory and constitutional obligations that the executive branch must respect, or prohibited actions: `nem foszthatja meg a bíróságot a felülvizsgálati jogtól` (must not deprive the court of judicial review), `nem csorbíthatja a hatásköröket önkényesen` (must not curtail competences arbitrarily), `köteles garantálni az érdemi normakontrollt` (is obligated to guarantee merit-based norm control), `tiszteletben kell tartania a jogállami határokat` (must respect rule-of-law boundaries).",
            "gr_text2": "Example: `A kormánynak tiszteletben kell tartania az intézményi függetlenséget, és nem csorbíthatja a bíróságok felülvizsgálati jogát`.",
            "gr_table": [
                ["A parlament nem csorbíthatja a bíróságok hatáskörét politikai indokokból.", "Parliament cannot curtail courts' competence for political reasons."],
                ["A hatalom köteles szavatolni az érdemi alkotmánybírósági normakontrollt.", "The power is obligated to guarantee merit-based constitutional judicial review."],
                ["A jogállami rendben a kormány nem írhatja felül az alapvető jogokat.", "In a rule-of-law order the government cannot override fundamental rights."]
            ],
            "world_story_seg": {
                "seg_slug": "alkotmanybirosag-megnyirbalasa",
                "title": "Az Alkotmánybíróság megnyirbálása és a bíróválasztás",
                "summary": "Az Alkotmánybíróság évtizedeken át a jogállam legfőbb bástyája volt. Az Alaptörvény és az azt megelőző módosítások megvonták a költségvetési kérdések vizsgálatának jogát és megszüntették az actio popularist.",
                "paragraphs": [
                    {"type": "narration", "text": "A Sólyom László elnökölte korai Alkotmánybíróság a 'láthatatlan alkotmány' elméletével Európa egyik legtekintélyesebb intézményévé vált. Ám miután a testület megsemmisítette a 98%-os különadót, a kormánypárti többség drasztikus válaszlépésre szánta el magát."},
                    {"type": "dialogue", "speaker": "Dr. Varga Dániel", "text": "A költségvetési törvények felülvizsgálatának megtiltása és a testület létszámának egypárti feltöltése az érdemi fékek és ellensúlyok felszámolását jelentette. A testület elvesztette klasszikus ellensúlyi szerepét."},
                    {"type": "narration", "text": "Az actio popularis megszüntetésével a polgárok nem kérhették többé közvetlenül a törvények absztrakt felülvizsgálatát. Bár bevezették a valódi alkotmányjogi panaszt, az egyéni jogvédelem szűkebb és lassabb keretek közé szorult."},
                    {"type": "narration", "text": "A kormány nem csorbíthatta volna meg ilyen mértékben a bírói felügyeletet anélkül, hogy ne rázta volna meg a jogállamiság alapjait."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Miért volt korszakos jelentőségű az 'actio popularis' megszűnése a magyar alkotmányjogban?", [
                    "Mert korábban bármely állampolgár, érintettség nélkül is kérhette egy alkotmányellenes törvény megsemmisítését.",
                    "Mert ezután minden állampolgárnak ingyen jogi diplomát osztottak.",
                    "Mert betiltották a népszerű színházi előadásokat az Alkotmánybíróság épületében."
                ], 0, ["c1-alkotmanyjog-vocab"]),
                fb("grammar", "controlled", "A kormányzat nem _____ meg a bíróságot a felülvizsgálati hatásköreitől. (must not deprive / foszthatja)", "foszthatja", "The government must not deprive the court of its review competences.", ["c1-modal-deontic-emergency-decrees"]),
                match("vocabulary", "controlled", [["actio popularis", "bárki által kezdeményezhető normakontroll"], ["költségvetési korlátozás", "pénzügyi törvények felülvizsgálatának tilalma"], ["alkotmányjogi panasz", "egyéni jogsérelem miatti beadvány"], ["hatáskörcsorbítás", "intézményi jogkörök szándékos szűkítése"]], ["c1-alkotmanyjog-vocab"]),
                fb("grammar", "practice", "A jogállamban az állam köteles _____ a bíróságok teljes függetlenségét. (to guarantee / garantálni)", "garantálni", "In the rule of law the state is obligated to guarantee the complete independence of courts.", ["c1-modal-deontic-emergency-decrees"]),
                sb("grammar", "practice", ["A", "parlament", "nem", "csorbíthatja", "a", "bírói", "függetlenség", "intézményi", "garanciáit."], ["A", "parlament", "nem", "csorbíthatja", "a", "bírói", "függetlenség", "intézményi", "garanciáit."], "Parliament cannot curtail the institutional guarantees of judicial independence.", ["c1-modal-deontic-emergency-decrees"]),
                dc("dialogue", [
                    {"speaker": "Kérdező", "text": "Milyen következménye volt a bíróság hatáskörcsorbításának?"},
                    {"speaker": "Szakértő", "text": "A parlamenti többség nem _____ volna meg a normakontroll lehetőségét anélkül, hogy ne sérült volna a jogbiztonság."},
                    {"speaker": "Kérdező", "text": "Ezért vált egyoldalúvá a törvényhozás."}
                ], ["vonhatta", "adhatta", "kérhette"], 0, ["c1-modal-deontic-emergency-decrees"]),
                sw("production", [{"prompt": "Write a sentence formulating a constitutional prohibition against executive overreach using 'nem csorbíthatja'.", "answer": "A törvényhozó hatalom semmilyen politikai cél érdekében nem csorbíthatja a bíróságok alkotmányos felülvizsgálati jogkörét."}], ["c1-modal-deontic-emergency-decrees"]),
                mc("grammar", "check", "Melyik modális forma fejez ki alkotmányjogi tilalmat a legszigorúbban?", [
                    "nem csorbíthatja a hatásköröket / nem foszthatja meg",
                    "esetleg elgondolkodhatna rajta",
                    "szívesen megengedi"
                ], 0, ["c1-modal-deontic-emergency-decrees"])
            ]
        },
        {
            "num": 3,
            "stem": f"c1-{slug}-03",
            "title": "Emergency Governance by Decree & Proportional Correlatives",
            "grammar_title": "Proportional Correlative Conjunctions Mapping Judicial Autonomy Against Executive Encroachment",
            "grammar_skill": "c1-adv-proportional-judicial-independence",
            "goals": [
                "I can analyze permanent emergency governance, state of danger decrees, and the marginalization of parliament (*veszélyhelyzeti kormányzás, rendeleti jogalkotás, felhatalmazási törvény*).",
                "I can construct proportional correlatives evaluating legal degradation (*minél hosszabb ideig tart a veszélyhelyzet, annál súlyosabb csorbát szenved a jogbiztonság*).",
                "I can critique the normalization of exceptional legal orders in constitutional democracies."
            ],
            "vocab": [
                {"lemma": "veszélyhelyzet", "translation": "state of danger / emergency", "pos": "noun"},
                {"lemma": "rendeleti kormányzás", "translation": "governance by decree", "pos": "expression"},
                {"lemma": "felhatalmazási törvény", "translation": "enabling act", "pos": "expression"},
                {"lemma": "különleges jogrend", "translation": "special legal order", "pos": "expression"},
                {"lemma": "parlamenti kontroll hiánya", "translation": "lack of parliamentary scrutiny", "pos": "expression"},
                {"lemma": "törvény áttörése", "translation": "overriding / setting aside statute", "pos": "expression"},
                {"lemma": "jogbizonytalanság", "translation": "legal uncertainty", "pos": "noun"},
                {"lemma": "normális működés", "translation": "normal constitutional functioning", "pos": "expression"}
            ],
            "gr_text1": "Proportional correlative structures (`minél... annál...`, `amilyen arányban... olyan mértékben...`) illustrate direct causal linkages between the expansion of exceptional powers and the erosion of constitutional guarantees: `Minél tovább tart a veszélyhelyzeti kormányzás, annál súlyosabb csorbát szenved a jogbiztonság` (The longer governance by emergency decree lasts, the more severe injury legal certainty suffers), `Amilyen mértékben növekszik a rendeleti jogalkotás, olyan arányban szorul háttérbe a parlamenti vita` (In proportion as decree-making expands, to that extent parliamentary debate is sidelined).",
            "gr_text2": "Example: `Minél inkább megszokottá válik a rendeleti jogalkotás, annál nehezebb lesz visszatérni a normális jogállami működéshez`.",
            "gr_table": [
                ["Minél tovább marad fenn a veszélyhelyzet, annál sebezhetőbbé válik a jogbiztonság.", "The longer the state of danger persists, the more vulnerable legal certainty becomes."],
                ["Amilyen mértékben bővül a kormányrendeleti hatáskör, olyan arányban gyengül a parlamenti kontroll.", "To the extent decree competence expands, to that extent parliamentary scrutiny weakens."],
                ["Minél gyakoribb a törvények felülírása rendelettel, annál kiszámíthatatlanabb a gazdasági környezet.", "The more frequent overriding of statutes by decree is, the more unpredictable the economic environment becomes."]
            ],
            "world_story_seg": {
                "seg_slug": "veszelyhelyzeti-kormanyzas",
                "title": "A permanens veszélyhelyzet és a rendeleti állam",
                "summary": "A 2020-as járványt, majd a 2022-es szomszédos háborút követően Magyarországon permanenssé vált a különleges jogrend: a kormány rendeletekkel írhatott felül törvényeket.",
                "paragraphs": [
                    {"type": "narration", "text": "Ami ideiglenes kríziskezelő eszköznek indult a COVID-19 idején, az a szomszédos háborús veszélyhelyzet meghosszabbításával a kormányzás állandó normájává vált. A parlament formális szavazógéppé degradálódott, miközben az éjszaka megjelent Magyar Közlönyökben alapvető adókat és ágazati szabályokat írtak át tollvonással."},
                    {"type": "dialogue", "speaker": "Dr. Varga Dániel", "text": "Minél hosszabb ideig tart ez az állapot, annál inkább erodálódik a jogbiztonság. A különleges jogrend lényege a kivételesség kellene hogy legyen; ha állandósul, felszámolja a jogállamot."},
                    {"type": "narration", "text": "A rendeleti kormányzás lehetővé tette, hogy a kormány a parlament megkerülésével, társadalmi egyeztetés nélkül hozzon stratégiai döntéseket költségvetési átcsoportosításokról és önkormányzati források elvonásáról."},
                    {"type": "narration", "text": "A jogász szakma egyhangúlag figyelmeztetett: a normák stabilitásának elvesztése nemzetközi szinten is elriasztja a minőségi beruházásokat."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Milyen jogkört biztosít a kormánynak a veszélyhelyzeti rendeleti kormányzás?", [
                    "A kormány rendeletével egyes törvények alkalmazását felfüggesztheti, és rendkívüli intézkedéseket hozhat.",
                    "A kormány feloszlathatja az Európai Parlamentet.",
                    "A miniszterek bíróként maguk hozhatnak büntetőbírósági ítéleteket a helyszínen."
                ], 0, ["c1-alkotmanyjog-vocab"]),
                fb("grammar", "controlled", "Minél tovább tart a veszélyhelyzet, _____ kiszolgáltatottabbá válnak a polgárok az önkénynek. (the more / annál)", "annál", "The longer the state of danger lasts, the more vulnerable citizens become to arbitrariness.", ["c1-adv-proportional-judicial-independence"]),
                match("vocabulary", "controlled", [["veszélyhelyzet", "különleges jogrend természeti vagy ember okozta válság idején"], ["felhatalmazási törvény", "kormányt rendkívüli rendeletalkotásra feljogosító törvény"], ["törvény áttörése", "törvényi szabály felülírása kormányrendelettel"], ["jogbizonytalanság", "a jogszabályok kiszámíthatatlansága"]], ["c1-alkotmanyjog-vocab"]),
                fb("grammar", "practice", "Amilyen mértékben szűkül a parlamenti ellenőrzés, olyan _____ növekszik a végrehajtó hatalom önkénye. (proportion / arányban)", "arányban", "In proportion as parliamentary oversight narrows, to that extent executive arbitrariness increases.", ["c1-adv-proportional-judicial-independence"]),
                sb("grammar", "practice", ["Minél", "több", "a", "rendelet,", "annál", "bizonytalanabb", "a", "törvényi", "környezet."], ["Minél", "több", "a", "rendelet,", "annál", "bizonytalanabb", "a", "törvényi", "környezet."], "The more decrees there are, the more uncertain the statutory environment becomes.", ["c1-adv-proportional-judicial-independence"]),
                dc("dialogue", [
                    {"speaker": "Polgár", "text": "Miért probléma, ha a kormány gyorsan, rendeletekkel kormányoz a válság idején?"},
                    {"speaker": "Jogtudós", "text": "Mert minél inkább megszokottá válik a rendeleti jogalkotás, _____ nehezebb lesz visszatérni a normális törvényhozáshoz."},
                    {"speaker": "Polgár", "text": "Így válik az ideiglenesből állandó állapot."}
                ], ["annál", "mindig", "soha"], 0, ["c1-adv-proportional-judicial-independence"]),
                sw("production", [{"prompt": "Write a sentence formulating the erosion of legal certainty using 'Minél... annál...'.", "answer": "Minél hosszabb ideig tart a permanens veszélyhelyzeti rendeleti kormányzás, annál súlyosabb károkat szenved a jogbiztonság és a parlamenti felügyelet."}], ["c1-adv-proportional-judicial-independence"]),
                mc("grammar", "check", "Melyik szerkezet fejez ki egyenes arányosságot a jogszabályi bizonytalanság elemzésében?", [
                    "Minél hosszabb... annál súlyosabb / Amilyen mértékben... olyan arányban",
                    "Bár esett az eső, mégis elmentünk",
                    "Nemcsak szép, hanem okos is"
                ], 0, ["c1-adv-proportional-judicial-independence"])
            ]
        },
        {
            "num": 4,
            "stem": f"c1-{slug}-04",
            "title": "Institutional Capture & Epistemic Incompatibility Stance",
            "grammar_title": "Epistemic Stance Markers Articulating Unconstitutionality and Fundamental Rights Violations",
            "grammar_skill": "c1-epistemic-constitutional-incompatibility",
            "goals": [
                "I can analyze the capture of independent institutions: the President, Prosecutor General, National Judicial Office (OBH), and State Audit Office (ÁSZ).",
                "I can employ elevated epistemic stance markers articulating unconstitutionality (*nyilvánvalóan alaptörvény-ellenes, vélelmezhetően jogfosztó, összeegyeztethetetlen a jogállamisággal*).",
                "I can critique how cadre appointments undermine constitutional counterweights."
            ],
            "vocab": [
                {"lemma": "intézményi foglyul ejtés", "translation": "state capture / institutional capture", "pos": "expression"},
                {"lemma": "Országos Bírósági Hivatal", "translation": "National Judicial Office (OBH)", "pos": "noun"},
                {"lemma": "legfőbb ügyész", "translation": "Prosecutor General", "pos": "expression"},
                {"lemma": "Állami Számvevőszék", "translation": "State Audit Office (ÁSZ)", "pos": "noun"},
                {"lemma": "pártpolitikai lojalitás", "translation": "party-political loyalty", "pos": "expression"},
                {"lemma": "hivatali autonómia", "translation": "institutional autonomy", "pos": "expression"},
                {"lemma": "káderezés", "translation": "cadre vetting / political appointments", "pos": "noun"},
                {"lemma": "jogállami összeegyeztethetetlenség", "translation": "incompatibility with the rule of law", "pos": "expression"}
            ],
            "gr_text1": "Epistemic stance markers articulate rigorous legal conclusions regarding the unconstitutionality or institutional corruption of state measures: `nyilvánvalóan összeegyeztethetetlen a jogállamiság elvével` (manifestly incompatible with the principle of rule of law), `minden kétséget kizáróan alaptörvény-ellenes` (unconstitutional beyond all doubt), `vélelmezhetően a hatalmi érdekeket kiszolgáló intézkedés` (a measure presumptively serving power interests), `joggal tekinthető intézményi foglyul ejtésnek` (may rightfully be regarded as institutional capture).",
            "gr_text2": "Example: `Az önálló ellenőrző szervek pártpolitikai feltöltése nyilvánvalóan összeegyeztethetetlen a hatalommegosztás alkotmányos követelményével`.",
            "gr_table": [
                ["A bírói kinevezések önkényes gyakorlata nyilvánvalóan összeegyeztethetetlen a bírói függetlenséggel.", "The arbitrary practice of judicial appointments is manifestly incompatible with judicial independence."],
                ["A hatósági döntés minden kétséget kizáróan alaptörvény-ellenes sérelmet okozott.", "The administrative decision caused an unconstitutional injury beyond all doubt."],
                ["A felügyelő testületek lojalitásalapú kinevezése joggal tekinthető intézményi foglyul ejtésnek.", "Loyalty-based appointments to supervisory bodies may rightfully be regarded as institutional capture."]
            ],
            "world_story_seg": {
                "seg_slug": "intezmenyi-foglyulejtes",
                "title": "A független intézmények foglyul ejtése és a bírói ellenállás",
                "summary": "Az Országos Bírósági Hivatal elnökének kiterjedt kinevezési jogkörei, a Legfőbb Ügyészség és a Számvevőszék élére állított pártkatonák kiüresítették az autonóm fékeket.",
                "paragraphs": [
                    {"type": "narration", "text": "Az intézményi foglyul ejtés nem egyik napról a másikra következett be, hanem a hivatali mandátumok évtizedes meghosszabbításával és a lojális káderek kinevezésével. Az Állami Számvevőszék ellenzéki pártokat büntető bírságai és a Legfőbb Ügyészség tétlensége a korrupciós ügyekben a rendszer sarokköveivé váltak."},
                    {"type": "dialogue", "speaker": "Dr. Varga Dániel", "text": "A legsúlyosabb csata a bíróságokért zajlott. Amikor az OBH elnöke sorra megsemmisítette a bírói pályázatokat és saját embereit ültette a bírói székekbe, a bírói kar Országos Bírói Tanácsa hősies ellenállást tanúsított."},
                    {"type": "narration", "text": "A független bírák fegyelmi eljárások és sajtóhadjáratok kereszttüzében is kitartottak az integritás mellett. Világossá vált: az intézményi ellensúlyok politikai alárendelése nyilvánvalóan összeegyeztethetetlen az európai jogrenddel."},
                    {"type": "narration", "text": "A jogállam utolsó védvonala a bátor jogalkalmazók lelkiismeretében és az autonóm bírói fórumokban maradt fenn."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Mit jelent az 'intézményi foglyul ejtés' (state capture / institutional capture)?", [
                    "Azt a folyamatot, amikor a független ellenőrző és bírói szervek élére a kormánypárthoz lojális szereplőket ültetnek, kiüresítve a kontrollt.",
                    "Amikor a múzeumok túszul ejtik a kiállított festményeket.",
                    "Egy épületfelújítási eljárást a bíróságokon."
                ], 0, ["c1-alkotmanyjog-vocab"]),
                fb("grammar", "controlled", "A bírói kinevezések politikai megvétózása _____ összeegyeztethetetlen a hatalommegosztással. (manifestly / nyilvánvalóan)", "nyilvánvalóan", "The political vetoing of judicial appointments is manifestly incompatible with the separation of powers.", ["c1-epistemic-constitutional-incompatibility"]),
                match("vocabulary", "controlled", [["intézményi foglyul ejtés", "független szervek pártérdekek alá rendelése"], ["Országos Bírósági Hivatal", "a bíróságok központi igazgatási szerve"], ["legfőbb ügyész", "a vádhatóság függetlennek szánt vezetője"], ["pártpolitikai lojalitás", "pártérdekek feltétlen kiszolgálása"]], ["c1-alkotmanyjog-vocab"]),
                fb("grammar", "practice", "A döntés minden kétséget kizáróan _____ sérelmet okozott a sajtószabadság terén. (unconstitutional / alaptörvény-ellenes)", "alaptörvény-ellenes", "The decision caused an unconstitutional injury beyond all doubt in the field of media freedom.", ["c1-epistemic-constitutional-incompatibility"]),
                sb("grammar", "practice", ["A", "bírói", "függetlenség", "felszámolása", "nyilvánvalóan", "ellentétes", "az", "európai", "értékekkel."], ["A", "bírói", "függetlenség", "felszámolása", "nyilvánvalóan", "ellentétes", "az", "európai", "értékekkel."], "The abolition of judicial independence is manifestly contrary to European values.", ["c1-epistemic-constitutional-incompatibility"]),
                dc("dialogue", [
                    {"speaker": "Bíró", "text": "Hogyan értékelhető az OBT és az OBH elnöke közötti küzdelem?"},
                    {"speaker": "Jogász", "text": "Ez a folyamat minden kétséget kizáróan _____ csorbát ejtett a bíróságok függetlenségén."},
                    {"speaker": "Bíró", "text": "Ezért kértük az Európai Unió Bíróságának állásfoglalását."}
                ], ["alaptörvény-ellenes", "kellemes", "jelentéktelen"], 0, ["c1-epistemic-constitutional-incompatibility"]),
                sw("production", [{"prompt": "Write a sentence formulating an unconstitutional abuse using an epistemic stance marker.", "answer": "A független felügyeleti intézmények lojalitásalapú feltöltése és a bíróságok kormánypárti ellenőrzése nyilvánvalóan összeegyeztethetetlen a demokratikus jogállam alapelvével."}], ["c1-epistemic-constitutional-incompatibility"]),
                mc("grammar", "check", "Melyik episztemikus kifejezés mond ki jogsértést a legnagyobb bizonyossággal?", [
                    "nyilvánvalóan összeegyeztethetetlen / minden kétséget kizáróan alaptörvény-ellenes",
                    "talán nem a legszebb megoldás",
                    "olykor-olykor előfordulhat"
                ], 0, ["c1-epistemic-constitutional-incompatibility"])
            ]
        },
        {
            "num": 5,
            "stem": f"c1-{slug}-05",
            "title": "Rule of Law Conditionality & Conclusive Synthesis",
            "grammar_title": "Evaluative Synthesis Particles Formulating Constitutional Doctrine and Democratic Restoration",
            "grammar_skill": "c1-adv-conclusive-democratic-safeguards",
            "goals": [
                "I can analyze the European Rule of Law Conditionality Mechanism, super-milestones, and funding freezes (*jogállamisági feltételességi mechanizmus, szuper-mérföldkövek, forrásbefagyasztás*).",
                "I can employ evaluative synthesis particles formulating constitutional doctrine (*végső soron elengedhetetlen, összegzésként leszögezhető, mindent egybevetve*).",
                "I can synthesize manifestos for constitutional restoration and democratic reconstruction in Hungary."
            ],
            "vocab": [
                {"lemma": "jogállamisági feltételesség", "translation": "rule of law conditionality", "pos": "expression"},
                {"lemma": "szuper-mérföldkő", "translation": "super-milestone (EU judicial reform criteria)", "pos": "noun"},
                {"lemma": "forrásbefagyasztás", "translation": "freezing of EU funds", "pos": "noun"},
                {"lemma": "Integritás Hatóság", "translation": "Integrity Authority", "pos": "noun"},
                {"lemma": "alkotmányos restauráció", "translation": "constitutional restoration", "pos": "expression"},
                {"lemma": "jogállami helyreállítás", "translation": "rule of law reconstruction", "pos": "expression"},
                {"lemma": "garanciális intézményrendszer", "translation": "guarantee institutional system", "pos": "expression"},
                {"lemma": "demokratikus konszolidáció", "translation": "democratic consolidation", "pos": "expression"}
            ],
            "gr_text1": "Evaluative synthesis particles formulate comprehensive juridical conclusions and normative manifestos for democratic restoration: `végső soron elengedhetetlen` (ultimately indispensable), `mindent egybevetve a jogállam garanciája` (all in all the guarantee of the rule of law), `konklúzióként leszögezhető` (it can be stated as a conclusion), `összességében tekintve az alkotmányos rend alapfeltétele` (taking it as a whole the prerequisite of constitutional order).",
            "gr_text2": "Example: `Végső soron elengedhetetlen a független bíráskodás és a törvényes fékek és ellensúlyok maradéktalan helyreállítása`.",
            "gr_table": [
                ["Végső soron elengedhetetlen a bírói autonómia törvényi helyreállítása.", "Ultimately the statutory restoration of judicial autonomy is indispensable."],
                ["Mindent egybevetve az intézményi fékek nélkül nem képzelhető el európai jogállam.", "All in all European rule of law is unimaginable without institutional checks."],
                ["Konklúzióként leszögezhető, hogy az unió pénzügyi nyomása kikényszerítette az igazságügyi reformot.", "It can be stated as a conclusion that EU financial pressure forced out judicial reform."]
            ],
            "world_story_seg": {
                "seg_slug": "jogallamisagi-mechanizmus",
                "title": "A jogállamisági mechanizmus és a helyreállítás reménye",
                "summary": "Az Európai Bizottság a jogállamisági feltételességi eljárással milliárdos forrásokat fagyasztott be, kikényszerítve az igazságügyi csomagot és a bírói tanács jogköreinek bővítését.",
                "paragraphs": [
                    {"type": "narration", "text": "Éveken át folyt a politikai szópárbaj a brüsszeli folyosókon és Budapesten anélkül, hogy a 7-es cikkely szerinti eljárás érdemi változást hozott volna. Az áttörést a 2021-ben bevezetett jogállamisági feltételességi mechanizmus jelentette, amely a jogállami normák megsértését közvetlenül a felzárkóztatási források befagyasztásához kötötte."},
                    {"type": "dialogue", "speaker": "Dr. Varga Dániel", "text": "A pénzügyi nyomás bizonyult az egyetlen hatékony eszköznek. A huszonhét szuper-mérföldkő teljesítése, az Országos Bírói Tanács vétójogának biztosítása és az Integritás Hatóság felállítása kényszerű, de elkerülhetetlen lépés volt."},
                    {"type": "narration", "text": "A valódi alkotmányos fordulat azonban nem várható pusztán külföldi felügyelettől. Végső soron elengedhetetlen a hazai jogásztársadalom, a szabad média és a polgárok elszántsága a jogállami kultúra újjáépítésére."},
                    {"type": "narration", "text": "Mindent egybevetve a magyar közjog története azt tanítja: a fékek és ellensúlyok rendszere nem elvont doktrína, hanem az emberi méltóság és szabadság mindennapi pajzsa."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Mi a lényege az Európai Unió 'jogállamisági feltételességi mechanizmusának'?", [
                    "Az EU felfüggesztheti a költségvetési kifizetéseket azon tagállamok számára, ahol a jogállamiság sérelme veszélyezteti az unió pénzügyi érdekeit.",
                    "Minden uniós polgárnak kötelező brüsszeli zászlót kitűznie az ablakába.",
                    "Csak azok az országok maradhatnak az EU-ban, amelyek átveszik a belga büntető törvénykönyvet."
                ], 0, ["c1-alkotmanyjog-vocab"]),
                fb("grammar", "controlled", "_____ soron elengedhetetlen a fékek és ellensúlyok rendszerének teljes körű helyreállítása. (Ultimately / Végső)", "Végső", "Ultimately the full-scale restoration of the system of checks and balances is indispensable.", ["c1-adv-conclusive-democratic-safeguards"]),
                match("vocabulary", "controlled", [["szuper-mérföldkő", "az uniós pénzek feloldásához kötött konkrét jogi feltétel"], ["forrásbefagyasztás", "uniós kifizetések felfüggesztése"], ["Integritás Hatóság", "korrupcióellenes független hatóság"], ["jogállami helyreállítás", "a demokratikus normák visszarendezése"]], ["c1-alkotmanyjog-vocab"]),
                fb("grammar", "practice", "Mindent _____, a bírói autonómia a jogállam legfőbb fundamentuma. (taking into account / egybevetve)", "egybevetve", "All in all, judicial autonomy is the supreme foundation of the rule of law.", ["c1-adv-conclusive-democratic-safeguards"]),
                sb("grammar", "practice", ["Végső", "soron", "elengedhetetlen", "a", "törvényuralom", "helyreállítása", "Magyarországon."], ["Végső", "soron", "elengedhetetlen", "a", "törvényuralom", "helyreállítása", "Magyarországon."], "Ultimately the restoration of the rule of law in Hungary is indispensable.", ["c1-adv-conclusive-democratic-safeguards"]),
                dc("dialogue", [
                    {"speaker": "Egyetemi oktató", "text": "Helyreállítható-e a fékek és ellensúlyok rendszere egyetlen törvénnyel?"},
                    {"speaker": "Alkotmányjogász", "text": "Végső soron _____ a társadalom jogtudatának megújítása és az intézmények átfogó reformja."},
                    {"speaker": "Egyetemi oktató", "text": "A valódi jogállamhoz tehát hosszú távú elkötelezettség kell."}
                ], ["elengedhetetlen", "felesleges", "ártalmas"], 0, ["c1-adv-conclusive-democratic-safeguards"]),
                sw("production", [{"prompt": "Write a concluding manifesto on constitutional restoration using 'Végső soron elengedhetetlen'.", "answer": "Végső soron elengedhetetlen az önkényuralmi rendeleti jogalkotás lebontása, a bírói függetlenség garanciális védelme és a fékek és ellensúlyok rendszerének maradéktalan helyreállítása."}], ["c1-adv-conclusive-democratic-safeguards"]),
                mc("grammar", "check", "Melyik szerkezet alkalmas jogi szintézis és záró konklúzió megfogalmazására?", [
                    "Végső soron elengedhetetlen / Mindent egybevetve",
                    "Hirtelen eszünkbe jutott",
                    "Tegnapelőtt délután"
                ], 0, ["c1-adv-conclusive-democratic-safeguards"])
            ]
        }
    ]

    for l in disc_lessons:
        emit_instructional_lesson(25, "discourse", l, disc_title, disc_intro if l["num"] == 1 else None)

    # Combined World Story
    write_json(
        f"stories/world/c1/c1-{slug}-alaptorveny-vita.json",
        {
            "id": f"story.c1.{slug}.combined",
            "title": "Alkotmányos átalakulás, fékek és ellensúlyok a mérlegen",
            "level": "C1",
            "lesson": 5,
            "order": 25,
            "type": "world",
            "estimatedMinutes": 8,
            "grammar": ["c1-adv-conclusive-democratic-safeguards"],
            "summary": "Összefoglaló krónika a 2011-es Alaptörvény elfogadásáról, a fékek és ellensúlyok szisztematikus felszámolásáról, a permanens veszélyhelyzeti kormányzásról, valamint az Európai Unió jogállamisági mechanizmusáról.",
            "vocabularyTopics": [
                "Constitutional Breakdown: The Fundamental Law, Decrees & Institutional Capture",
                "Rule of Law Conditionality & Conclusive Synthesis"
            ],
            "paragraphs": [
                {"type": "narration", "text": "2011 tavaszán a parlamenti kétharmados többség által egyoldalúan elfogadott Alaptörvény lezárta a rendszerváltás konszenzusos közjogi korszakát. Bár a hivatalos retorika a kommunista maradványok felszámolását hirdette, a jogállami normák szisztematikus erodálása vette kezdetét: a sarkalatos törvények parttalan kiterjesztése és az intézményi ellensúlyok átpolitizálása alapjaiban rengette meg a hatalommegosztás egyensúlyát."},
                {"type": "narration", "text": "A legfőbb alkotmányos fék, az Alkotmánybíróság megcsonkítása a költségvetési jogkörök elvonásával, az actio popularis megszüntetésével és a bíróválasztás egypárti feltöltésével valósult meg. A hatalom nem csorbíthatta volna meg a független bírói kontrollt anélkül, hogy ne idézett volna elő súlyos jogbiztonsági válságot, melynek nyomán az állampolgári jogorvoslat formálissá silányult."},
                {"type": "narration", "text": "Ezt követte a különleges jogrend állandósulása: a világjárvány, majd a szomszédos háború ürügyén bevezetett permanens veszélyhelyzet nyomán a rendeleti jogalkotás vált a mindennapi kormányzás alapjává. Minél tovább tartott a parlamentet megkerülő éjszakai dekretális törvénykezés, annál kiszámíthatatlanabbá vált a magyar gazdasági és jogi környezet, teljesen aláásva a normahierarchiát."},
                {"type": "narration", "text": "A nemzetközi közösség sokáig tehetetlenül szemlélte a folyamatot, mígnem a jogállamisági feltételességi mechanizmus és a felzárkóztatási források befagyasztása kényszerítő erővel nem lépett fel. Végső soron elengedhetetlen felismerni: a külső uniós nyomás csak időleges korlátokat szabhat, a valódi alkotmányos újjászületés, a fékek és ellensúlyok helyreállítása és a jogállami kultúra megerősítése kizárólag a magyar társadalom belső elszántságából fakadhat."}
            ]
        }
    )

    # Discourse Consolidation
    emit_consolidation_lesson(
        25,
        "discourse",
        f"c1-{slug}-consolidation",
        disc_title,
        [
            "I can evaluate the 2011 Fundamental Law, cardinal laws, and single-party constitution-making.",
            "I can critique Constitutional Court curtailment, emergency decree governance, and institutional capture.",
            "I can articulate arguments regarding EU rule of law conditionality and constitutional reconstruction."
        ],
        [
            mc("grammar", "recognize", "Milyen szerkezettel fejezhetünk ki súlyos alkotmányos hanyatlást és jogállami visszalépést?", [
                "a jogállami normák szisztematikus erodálása / az alkotmányos fékek felszámolása",
                "mert új irodaszereket vásárolt a minisztérium",
                "amikor a parlament délután háromkor fejezte be az ülést"
            ], 0, ["c1-discourse-constitutional-crisis-framing"]),
            mc("grammar", "recognize", "Melyik kifejezés testesíti meg az intézményi autonómiát védő törvényi tilalmat?", [
                "nem csorbíthatja a bírói hatásköröket / köteles garantálni az érdemi normakontrollt",
                "szabadon dönthet a kávészünet hosszáról",
                "bármikor megnézheti az időjárás-jelentést"
            ], 0, ["c1-modal-deontic-emergency-decrees"]),
            match("vocabulary", "recognize", [["Alaptörvény", "Magyarország alaptörvénye 2011 óta"], ["veszélyhelyzet", "rendeleti jogalkotást biztosító különleges jogrend"], ["actio popularis", "bárki által indítható alkotmányossági vizsgálat"], ["szuper-mérföldkő", "uniós forrásokhoz kötött igazságügyi reformfeltétel"], ["intézményi foglyul ejtés", "független kontrollszervek pártirányítás alá vonása"]], ["c1-alkotmanyjog-vocab"]),
            fb("vocabulary", "recall", "Az ellenőrző és bírói szervek pártpolitikai alárendelését intézményi _____ ejtésnek nevezik. (capture / foglyul)", "foglyul", "The party-political subjugation of supervisory and judicial organs is called institutional capture.", ["c1-alkotmanyjog-vocab"]),
            fb("vocabulary", "recall", "A rendeleti kormányzásra felhatalmazó különleges jogrend a _____. (state of danger / veszélyhelyzet)", "veszélyhelyzet", "The special legal order authorizing decree governance is the state of danger.", ["c1-alkotmanyjog-vocab"]),
            fb("grammar", "recall", "A kormány nem _____ meg a bíróságokat érdemi hatásköreiktől. (must not deprive / foszthatja)", "foszthatja", "The government must not deprive courts of their substantive competences.", ["c1-modal-deontic-emergency-decrees"]),
            fb("grammar", "context", "Minél tovább tart a rendeleti kormányzás, _____ mélyebbé válik a jogbizonytalanság. (the more / annál)", "annál", "The longer decree governance lasts, the deeper legal uncertainty becomes.", ["c1-adv-proportional-judicial-independence"]),
            fb("grammar", "context", "Végső soron _____ a fékek és ellensúlyok törvényes helyreállítása. (indispensable / elengedhetetlen)", "elengedhetetlen", "Ultimately the statutory restoration of checks and balances is indispensable.", ["c1-adv-conclusive-democratic-safeguards"]),
            mc("grammar", "context", "Mi a funkciója a 'Minél... annál...' arányossági szerkezetnek a jogállamisági vitákban?", [
                "A kivételes intézkedések tartóssága és a jogbiztonság pusztulása közötti egyenes arányosságot bizonyítja.",
                "Megmutatja, hogy mennyi pénzbe kerül a parlamenti képviselők ebéde.",
                "Bocsánatot kér az elhúzódó jogi procedúrák miatt."
            ], 0, ["c1-adv-proportional-judicial-independence"]),
            sb("grammar", "produce", ["A", "fékek", "és", "ellensúlyok", "nélkül", "nem", "létezhet", "valódi", "jogállam."], ["A", "fékek", "és", "ellensúlyok", "nélkül", "nem", "létezhet", "valódi", "jogállam."], "Without checks and balances no genuine rule of law can exist.", ["c1-adv-conclusive-democratic-safeguards"]),
            sw("production", [{"prompt": "Write a critical diagnosis of constitutional erosion using a crisis framing marker.", "answer": "Az egypárti alkotmányozás és a független intézmények foglyul ejtése a jogállami normák szisztematikus erodálásához és az alkotmányos fékek felszámolásához vezetett."}], ["c1-discourse-constitutional-crisis-framing"]),
            sw("production", [{"prompt": "Formulate a concluding thought on constitutional restoration and the rule of law in Hungary.", "answer": "Végső soron elengedhetetlen az önkényuralmi rendeleti kormányzás felszámolása, a bírói autonómia megerősítése és a fékek és ellensúlyok rendszerének maradéktalan helyreállítása."}], ["c1-adv-conclusive-democratic-safeguards"])
        ]
    )

    print("=== Finished C1 Unit 25 ===")


if __name__ == "__main__":
    generate_unit_25()
