#!/usr/bin/env python3
"""
Hungarian C1 Block 5 - Unit 27 Generator:
  - Track 1 (Core): Unit 27 — "Clinical Empiricism, Epidemiology & Medical Ethics" (c1-27)
  - Track 2 (Discourse): Unit 27 — "Healthcare in Crisis: Doctor Wage Reforms, Nurse Shortages & Chamber Control" (c1-egeszsegugy)
"""

import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT))

from scripts.c1_block1.common import mc, match, fb, sb, dc, sw, write_json, emit_instructional_lesson, emit_consolidation_lesson
from scripts.c1_block5.registry_helper import register_unit


def generate_unit_27():
    print("=== Generating C1 Unit 27 ===")
    
    new_skills = {
        "c1-27-vocab": {"kind": "vocabulary"},
        "c1-egeszsegugy-vocab": {"kind": "vocabulary"},
        "c1-adv-clinical-epidemiological-causality": {"kind": "grammar"},
        "c1-participle-prophylactic-intervention": {"kind": "grammar"},
        "c1-adv-counter-dogmatic-adversatives": {"kind": "grammar"},
        "c1-modal-bioethical-imperatives": {"kind": "grammar"},
        "c1-adv-scalar-medical-breakthrough": {"kind": "grammar"},
        "c1-discourse-healthcare-inequity-framing": {"kind": "grammar"},
        "c1-modal-deontic-chamber-autonomy": {"kind": "grammar"},
        "c1-adv-proportional-nurse-shortage": {"kind": "grammar"},
        "c1-epistemic-patient-safety-risk": {"kind": "grammar"},
        "c1-adv-conclusive-public-health-synthesis": {"kind": "grammar"},
    }
    new_titles = {
        "c1-27-vocab": "reading",
        "c1-egeszsegugy-vocab": "reading",
        "c1-adv-clinical-epidemiological-causality": "clinical epidemiological adverbials establishing empirical etiologic causality and infection pathways",
        "c1-participle-prophylactic-intervention": "complex participial structures detailing antiseptic prophylaxis and clinical interventions",
        "c1-adv-counter-dogmatic-adversatives": "adversative connectors confronting medical dogma with empirical statistical evidence",
        "c1-modal-bioethical-imperatives": "bioethical modal structures articulating the physician duty of non-maleficence",
        "c1-adv-scalar-medical-breakthrough": "scalar evaluative adverbials calibrating clinical discovery and public health impact",
        "c1-discourse-healthcare-inequity-framing": "discourse framing markers diagnosing systemic healthcare shortages and structural crises",
        "c1-modal-deontic-chamber-autonomy": "deontic modal structures condemning legislative curtailment of professional medical self-governance",
        "c1-adv-proportional-nurse-shortage": "proportional correlative conjunctions mapping wage gaps to healthcare capacity collapse",
        "c1-epistemic-patient-safety-risk": "epistemic stance markers assessing clinical hazard and systemic patient risk",
        "c1-adv-conclusive-public-health-synthesis": "evaluative synthesis particles formulating comprehensive manifestos for healthcare reconstruction",
    }
    
    core_title = "Clinical Empiricism, Epidemiology & Medical Ethics"
    core_stems = [f"c1-27-0{i}" for i in range(1, 6)] + ["c1-27-consolidation"]
    disc_title = "Healthcare in Crisis: Doctor Wage Reforms, Nurse Shortages & Chamber Control"
    disc_stems = [f"c1-egeszsegugy-0{i}" for i in range(1, 6)] + ["c1-egeszsegugy-consolidation"]
    
    register_unit(27, core_title, core_stems, disc_title, disc_stems, new_skills, new_titles)

    # ----------------------------------------------------
    # TRACK 1: CORE (c1-27)
    # ----------------------------------------------------
    core_intro = [
        "The development of medical science is the triumph of observation, empirical statistics, and sanitary prophylaxis over superstition and entrenched academic hierarchies. Ignác Semmelweis, the 'savior of mothers', revolutionized clinical epidemiology through the rigorous identification of etiologic infection transmission in mid-19th century Vienna and Pest.",
        "In this unit, centered on Semmelweis Ignác's monumental treatise 'A gyermekágyi láz kóroktana' (1861), you will master the elevated academic register of clinical pathology, epidemiological causality, antiseptic protocols, bioethical responsibilities, and medical paradigm shifts at the C1 level."
    ]

    core_lessons = [
        {
            "num": 1,
            "stem": "c1-27-01",
            "title": "Etiologic Causality & Epidemiological Adverbials",
            "grammar_title": "Clinical Epidemiological Adverbials Establishing Empirical Etiologic Causality and Infection Pathways",
            "grammar_skill": "c1-adv-clinical-epidemiological-causality",
            "goals": [
                "I can analyze disease etiology, infection vectors, and epidemiological statistics (*kóroktan, fertőzési vektor, morbiditási statisztika, transzmisszió*).",
                "I can deploy elevated epidemiological adverbials establishing causal links (*kóroktanilag igazoltan, epidemiológiailag alátámasztottan, okságilag kimutatható módon*).",
                "I can critique medical research methodologies in rigorous clinical register."
            ],
            "vocab": [
                {"lemma": "kóroktan", "translation": "etiology (study of causation)", "pos": "noun"},
                {"lemma": "kórbonctan", "translation": "pathological anatomy", "pos": "noun"},
                {"lemma": "fertőzési vektor", "translation": "infection vector", "pos": "expression"},
                {"lemma": "morbiditási ráta", "translation": "morbidity rate", "pos": "expression"},
                {"lemma": "mortalitási statisztika", "translation": "mortality statistics", "pos": "expression"},
                {"lemma": "transzmisszió", "translation": "transmission / transfer", "pos": "noun"},
                {"lemma": "empirikus korreláció", "translation": "empirical correlation", "pos": "expression"},
                {"lemma": "járványtani vizsgálat", "translation": "epidemiological investigation", "pos": "expression"}
            ],
            "gr_text1": "Clinical epidemiological adverbials formulate scientific judgments regarding causal pathways and pathogenic vectors: `kóroktanilag igazoltan` (etiologically confirmed), `epidemiológiailag alátámasztott módon` (in an epidemiologically substantiated manner), `okságilag kimutathatóan` (demonstrably causal), `fertőzéstanilag bizonyítottan` (infectiologically proven).",
            "gr_text2": "Example: `A professzor kóroktanilag igazoltan és epidemiológiailag alátámasztott módon mutatta ki a kórokozók közvetlen átvitelét a kórbonctani vizsgálatok során`.",
            "gr_table": [
                ["A kórokozó közvetlen átvitele kóroktanilag igazoltan okozta a megbetegedést.", "Direct transfer of the pathogen etiologically confirmed caused the illness."],
                ["A mortalitás csökkenése epidemiológiailag alátámasztott módon követte a higiéniai intézkedéseket.", "The decline in mortality followed sanitary measures in an epidemiologically substantiated manner."],
                ["A baktériumok jelenléte okságilag kimutathatóan összefügg a fertőzéssel.", "The presence of bacteria demonstrably causally correlates with infection."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mit jelent a 'kóroktan' (etiológia) az orvostudományban?", [
                    "A betegségek kialakulásának közvetlen és közvetett okait, valamint kórokozóit kutató tudományágat.",
                    "A kórházi ágyak gyártási technológiáját.",
                    "Az orvosi egyetemek történelmi könyvtárát."
                ], 0, ["c1-27-vocab"]),
                fb("grammar", "controlled", "A fertőzés forrását _____ alátámasztott adatokkal azonosították az orvosok. (epidemiologically / epidemiológiailag)", "epidemiológiailag", "Doctors identified the source of infection with epidemiologically substantiated data.", ["c1-adv-clinical-epidemiological-causality"]),
                match("vocabulary", "controlled", [["kóroktan", "a betegségek okait kutató tudomány"], ["kórbonctan", "a betegségek okozta szöveti elváltozások vizsgálata"], ["morbiditási ráta", "a megbetegedések gyakorisági mutatója"], ["transzmisszió", "kórokozó átvitele egyik egyedről a másikra"]], ["c1-27-vocab"]),
                fb("grammar", "practice", "A kutatóknak sikerült okságilag _____ módon bizonyítaniuk a kórokozó szerepét. (demonstrably / kimutatható)", "kimutatható", "Researchers succeeded in demonstrably proving the role of the pathogen in a causal manner.", ["c1-adv-clinical-epidemiological-causality"]),
                sb("grammar", "practice", ["A", "fertőzés", "útja", "kóroktanilag", "igazoltan", "a", "kezeken", "keresztül", "vezetett."], ["A", "fertőzés", "útja", "kóroktanilag", "igazoltan", "a", "kezeken", "keresztül", "vezetett."], "The path of infection etiologically confirmed led through the hands.", ["c1-adv-clinical-epidemiological-causality"]),
                dc("dialogue", [
                    {"speaker": "Klinikai orvos", "text": "Hogyan bizonyíthatjuk az új vírus szerepét a tüdőgyulladásban?"},
                    {"speaker": "Epidemiológus", "text": "Csak akkor, ha kóroktanilag igazoltan és _____ alátámasztott módon kimutatjuk az összefüggést."},
                    {"speaker": "Klinikai orvos", "text": "Akkor kontrollcsoportos vizsgálatot indítunk."}
                ], ["epidemiológiailag", "gyorsan", "véletlenül"], 0, ["c1-adv-clinical-epidemiological-causality"]),
                sw("production", [{"prompt": "Write a sentence formulating an etiologic discovery using an epidemiological adverbial.", "answer": "Semmelweis Ignác kóroktanilag igazoltan és epidemiológiailag alátámasztott statisztikai adatokkal mutatta ki a kórbonctani anyag közvetlen átvitelét a gyermekágyi láz eseteiben."}], ["c1-adv-clinical-epidemiological-causality"]),
                mc("grammar", "check", "Melyik határozói szerkezet jelöli az orvosi ok-okozati viszonyt a legszakszerűbben?", [
                    "kóroktanilag igazoltan / okságilag kimutatható módon",
                    "többnyire úgy gondolva",
                    "szerencsésen eltalálva"
                ], 0, ["c1-adv-clinical-epidemiological-causality"])
            ]
        },
        {
            "num": 2,
            "stem": "c1-27-02",
            "title": "Antiseptic Prophylaxis & Participial Modifiers",
            "grammar_title": "Complex Participial Structures Detailing Antiseptic Prophylaxis and Clinical Interventions",
            "grammar_skill": "c1-participle-prophylactic-intervention",
            "goals": [
                "I can analyze antiseptic protocols, prophylaxis, and chemical sterilization (*antiszepszis, klórmeszes fertőtlenítés, aszepszis, profilaxis*).",
                "I can construct complex participial structures detailing clinical procedures (*a fertőtlenítést kötelezővé tevő, a mikrobákat elpusztító, a mortalitást visszaszorító*).",
                "I can formulate preventative hygiene protocols in academic medical register."
            ],
            "vocab": [
                {"lemma": "antiszepszis", "translation": "antisepsis", "pos": "noun"},
                {"lemma": "aszepszis", "translation": "asepsis (prevention of contact with microorganisms)", "pos": "noun"},
                {"lemma": "profilaxis", "translation": "prophylaxis / prevention", "pos": "noun"},
                {"lemma": "klórmész", "translation": "chlorinated lime (calcium hypochlorite)", "pos": "noun"},
                {"lemma": "fertőtlenítőszer", "translation": "disinfectant", "pos": "noun"},
                {"lemma": "kórházi fertőzés", "translation": "nosocomial / healthcare-associated infection", "pos": "expression"},
                {"lemma": "higiéniai protokoll", "translation": "hygiene protocol", "pos": "expression"},
                {"lemma": "csíraölő hatás", "translation": "germicidal effect", "pos": "expression"}
            ],
            "gr_text1": "Complex participial modifiers specify prophylactic and antiseptic actions with surgical exactness: `a kórbonctani anyagokat megsemmisítő klórmeszes mosakodás` (chlorinated lime washing destroying cadaveric materials), `a kórházi fertőzéseket megelőző szigorú protokoll` (strict protocol preventing nosocomial infections), `a halálozási rátát radikálisan visszaszorító eljárás` (procedure radically suppressing mortality rate).",
            "gr_text2": "Example: `A klinikán bevezetett, a kötelező kézmosást előíró és a kórokozókat elpusztító klóros eljárás azonnal életeket mentett`.",
            "gr_table": [
                ["A klórmeszes kézmosást előíró szabályzat azonnal felére csökkentette a lázat.", "The regulation prescribing chlorinated lime handwashing immediately halved fever."],
                ["A kórbonctani részecskéket elpusztító vegyszerek alkalmazása elengedhetetlen volt.", "Application of chemicals destroying cadaveric particles was indispensable."],
                ["A kórházi fertőzéseket megelőző intézkedések a modern sebészet alapjai.", "Measures preventing hospital infections are the foundations of modern surgery."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Miért alkalmazott Semmelweis Ignác klórmeszes oldatot a sima szappanos kézmosás helyett?", [
                    "Mert felismerte, hogy a boncolás után a kézen maradó láthatatlan szag és cadaver-részecskék csak a klórmész erős oxidáló, csíraölő hatásával tüntethetők el.",
                    "Mert a szappan túl drága volt a bécsi közkórházban.",
                    "Mert a klórmész szép fehérre festette az orvosok bőrét."
                ], 0, ["c1-27-vocab"]),
                fb("grammar", "controlled", "A mortalitást radikálisan _____ eljárás történelmi áttörést hozott. (suppressing / visszaszorító)", "visszaszorító", "The procedure radically suppressing mortality brought a historic breakthrough.", ["c1-participle-prophylactic-intervention"]),
                match("vocabulary", "controlled", [["antiszepszis", "kórokozók vegyszeres elpusztítása élő szöveten"], ["aszepszis", "kórokozó-mentes környezet megteremtése"], ["profilaxis", "betegségek kialakulását megelőző eljárások összessége"], ["kórházi fertőzés", "egészségügyi ellátás során szerzett infekció"]], ["c1-27-vocab"]),
                fb("grammar", "practice", "A kötelező fertőtlenítést _____ rendeletet a klinika igazgatója ellenállással fogadta. (prescribing / előíró)", "előíró", "The decree prescribing mandatory disinfection was met with resistance by the clinic director.", ["c1-participle-prophylactic-intervention"]),
                sb("grammar", "practice", ["A", "klórmeszes", "kézmosást", "előíró", "szabály", "megmentette", "az", "anyák", "életét."], ["A", "klórmeszes", "kézmosást", "előíró", "szabály", "megmentette", "az", "anyák", "életét."], "The rule prescribing chlorinated lime handwashing saved the mothers' lives.", ["c1-participle-prophylactic-intervention"]),
                dc("dialogue", [
                    {"speaker": "Főorvos", "text": "Miért van szükség erre a kellemetlen szagú klórmeszes mosakodásra?"},
                    {"speaker": "Semmelweis", "text": "Mert a bonctermi mérget _____ klóros oldat nélkül a betegágyakhoz lépni egyet jelent a gyilkossággal."},
                    {"speaker": "Főorvos", "text": "Akkor kötelezővé tesszük minden orvostanhallgatónak."}
                ], ["elpusztító", "kedvelő", "felejtő"], 0, ["c1-participle-prophylactic-intervention"]),
                sw("production", [{"prompt": "Write a sentence detailing an antiseptic intervention using a participial modifier.", "answer": "A Semmelweis által bevezetett, a boncolás utáni klórmeszes kézmosást kógens módon előíró profilaktikus eljárás minimálisra csökkentette a kórtermi halálozást."}], ["c1-participle-prophylactic-intervention"]),
                mc("grammar", "check", "Melyik szerkezet írja le a profilaktikus orvosi beavatkozást a legszakszerűbben?", [
                    "a kórbonctani anyagokat elpusztító és fertőzést megelőző eljárás",
                    "a kézmosás után a folyosón sétáló orvosok",
                    "egy szép fehér orvosi köpeny felöltése"
                ], 0, ["c1-participle-prophylactic-intervention"])
            ]
        },
        {
            "num": 3,
            "stem": "c1-27-03",
            "title": "Confronting Medical Dogma & Adversative Refutation",
            "grammar_title": "Adversative Connectors Confronting Medical Dogma with Empirical Statistical Evidence",
            "grammar_skill": "c1-adv-counter-dogmatic-adversatives",
            "goals": [
                "I can analyze the conflict between empirical statistical science and traditional medical dogmas (*miazma-elmélet, tekintélyelvű hierarchia, empirikus cáfolat*).",
                "I can deploy elevated adversative connectors confronting dogmatic falsehoods (*a dogmákkal szemben, nemhogy nem miazmatikus eredetű, hanem éppen kórbonctani átvitel, mindazonáltal statisztikailag cáfolhatatlan*).",
                "I can articulate philosophical arguments defending empirical truth against authoritarian consensus."
            ],
            "vocab": [
                {"lemma": "miazma-elmélet", "translation": "miasma theory (disease caused by foul air)", "pos": "noun"},
                {"lemma": "tekintélyelvű hierarchia", "translation": "authoritarian hierarchy", "pos": "expression"},
                {"lemma": "akadémiai vakság", "translation": "academic blindness", "pos": "expression"},
                {"lemma": "empirikus cáfolat", "translation": "empirical refutation", "pos": "expression"},
                {"lemma": "statisztikai evidencia", "translation": "statistical evidence", "pos": "expression"},
                {"lemma": "kórházi járványtan", "translation": "hospital epidemiology", "pos": "expression"},
                {"lemma": "dogmatikus elutasítás", "translation": "dogmatic rejection", "pos": "expression"},
                {"lemma": "orvosi paradigmaváltás", "translation": "medical paradigm shift", "pos": "expression"}
            ],
            "gr_text1": "Adversative connectors emphasize the stark contrast between traditional theoretical superstition and hard empirical data: `a miazma-elmélet dogmáival szemben a valóságban` (contrary to dogmas of miasma theory in reality), `nemhogy nem a rossz levegő okozza, hanem éppen az orvosok keze` (far from foul air causing it, but rather doctors' hands), `mindazonáltal a statisztikák alapján vitathatatlan` (nevertheless on the basis of statistics indisputable).",
            "gr_text2": "Example: `A bécsi professzorok dogmáival szemben a valóságban a statisztikák nemhogy nem a véletlen ingadozást igazolták, hanem éppen a fertőtlenítés életmentő hatását bizonyították`.",
            "gr_table": [
                ["A tekintélyelvű dogmákkal szemben a valóságban a számok döntöttek.", "Contrary to authoritarian dogmas in reality the numbers decided."],
                ["A kór nemhogy nem a rossz levegőtől származik, hanem éppen a kezek közvetítik.", "The disease is far from originating from bad air; on the contrary, hands transmit it."],
                ["A felfedezés mindazonáltal statisztikailag cáfolhatatlan tényeken alapult.", "The discovery was nevertheless based on statistically irrefutable facts."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mi volt a 'miazma-elmélet', amelyet Semmelweis empirikus adatai megdöntöttek?", [
                    "Az az évszázados orvosi dogma, amely szerint a járványokat a mocsarakból és rothadó anyagokból felszálló 'rossz levegő' (miazma) terjeszti.",
                    "Egy ókori görög zenei elmélet.",
                    "A sebészeti ollók élezésének technikája."
                ], 0, ["c1-27-vocab"]),
                fb("grammar", "controlled", "A korabeli dogmákkal szemben a _____ a klóros lemosás megszüntette a halálozást. (in reality / valóságban)", "valóságban", "Contrary to contemporary dogmas, in reality chlorinated washing eliminated mortality.", ["c1-adv-counter-dogmatic-adversatives"]),
                match("vocabulary", "controlled", [["miazma-elmélet", "a betegségeket a rossz levegőnek tulajdonító elmélet"], ["tekintélyelvű hierarchia", "a rangidős professzorok megkérdőjelezhetetlen hatalma"], ["statisztikai evidencia", "számszerű adatokkal alátámasztott megdönthetetlen bizonyíték"], ["orvosi paradigmaváltás", "az orvosi gondolkodás alapvető forradalmi átalakulása"]], ["c1-27-vocab"]),
                fb("grammar", "practice", "A gyermekágyi láz nemhogy nem kozmikus eredetű, hanem éppen kórbonctani _____ terjed. (transfer / átvitellel)", "átvitellel", "Puerperal fever is far from of cosmic origin; on the contrary, it spreads via cadaveric transfer.", ["c1-adv-counter-dogmatic-adversatives"]),
                sb("grammar", "practice", ["A", "professzorok", "dogmáival", "szemben", "a", "statisztika", "cáfolhatatlan", "volt."], ["A", "professzorok", "dogmáival", "szemben", "a", "statisztika", "cáfolhatatlan", "volt."], "Contrary to the professors' dogmas, the statistics were irrefutable.", ["c1-adv-counter-dogmatic-adversatives"]),
                dc("dialogue", [
                    {"speaker": "Bécsi professzor", "text": "Hogyan merészeli egy fiatal magyar tanársegéd kétségbe vonni tekintélyünket?"},
                    {"speaker": "Semmelweis", "text": "A professzori tekintéllyel szemben a valóságban a számok beszélnek: az I. osztály mortalitása nemhogy nem normális, hanem éppen elkerülhető _____ bizonyít."},
                    {"speaker": "Bécsi professzor", "text": "Ez a vád hallatlan az egyetem falai között."}
                ], ["mészárlást", "ünnepet", "nyugalmat"], 0, ["c1-adv-counter-dogmatic-adversatives"]),
                sw("production", [{"prompt": "Write a sentence confronting medical dogma using 'A dogmákkal szemben a valóságban'.", "answer": "A miazmatikus dogmákkal szemben a valóságban Semmelweis statisztikái nemhogy nem a véletlennek tulajdonították a fertőzést, hanem éppen a fertőtlenítés elmaradásának közvetlen következményeként leplezték le azt."}], ["c1-adv-counter-dogmatic-adversatives"]),
                mc("grammar", "check", "Melyik szerkezet állítja szembe a dogmát a kísérleti ténnyel a leghatásosabban?", [
                    "A dogmákkal szemben a valóságban nemhogy nem... hanem éppen ellenkezőleg",
                    "Úgy tűnik talán hogy máshogy van",
                    "Ha nem hiszik el, az sem baj"
                ], 0, ["c1-adv-counter-dogmatic-adversatives"])
            ]
        },
        {
            "num": 4,
            "stem": "c1-27-04",
            "title": "Medical Ethics & Bioethical Imperative Modals",
            "grammar_title": "Bioethical Modal Structures Articulating the Physician Duty of Non-Maleficence",
            "grammar_skill": "c1-modal-bioethical-imperatives",
            "goals": [
                "I can analyze the Hippocratic oath, the principle of 'primum non nocere', and the moral duty of clinical transparency (*nil nocere elv, orvosi eskü, betegjogok, orvosi hiba feltárása*).",
                "I can deploy bioethical modal structures formulating ethical duties (*kötelessége a beteget védeni, nem teheti ki elkerülhető veszélynek, elszámolással tartozik a lelkiismeretének*).",
                "I can debate the ethical dilemma of institutional cover-ups vs. physician whistleblowing."
            ],
            "vocab": [
                {"lemma": "primum non nocere", "translation": "first, do no harm (nil nocere)", "pos": "expression"},
                {"lemma": "orvosi eskü", "translation": "Hippocratic / medical oath", "pos": "expression"},
                {"lemma": "orvosi mulasztás", "translation": "medical negligence / malpractice", "pos": "expression"},
                {"lemma": "etikai imperatívusz", "translation": "ethical imperative", "pos": "expression"},
                {"lemma": "betegbiztonság", "translation": "patient safety", "pos": "noun"},
                {"lemma": "tájékozott beleegyezés", "translation": "informed consent", "pos": "expression"},
                {"lemma": "szakmai lelkiismeret", "translation": "professional conscience", "pos": "expression"},
                {"lemma": "intézményi elhallgatás", "translation": "institutional cover-up", "pos": "expression"}
            ],
            "gr_text1": "Bioethical modal structures formulate solemn professional and moral commands: `az orvosnak feltétlenül tiszteletben kell tartania a 'primum non nocere' elvét` (the physician must unconditionally respect the 'first, do no harm' principle), `nem teheti ki a pácienst elkerülhető fertőzésveszélynek` (cannot expose the patient to avoidable infection risk), `köteles beismerni a szakmai tévedést` (is obligated to admit professional error), `erkölcsi parancsként kell tekintenie az emberi élet védelmére` (must regard the protection of human life as a moral command).",
            "gr_text2": "Example: `A gyógyítónak minden körülmények között a beteg javát kell szolgálnia, és nem áldozhatja fel az emberi életet a szakmai hiúság oltárán`.",
            "gr_table": [
                ["Az orvos nem teheti ki a pácienst elkerülhető fertőzésveszélynek.", "The physician cannot expose the patient to avoidable infection risk."],
                ["A szakmai lelkiismeret parancsaként kötelező feltárni a mulasztásokat.", "As a command of professional conscience revealing negligences is mandatory."],
                ["A kórháznak garantálnia kell a betegbiztonság legszigorúbb feltételeit.", "The hospital must guarantee the strictest conditions of patient safety."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mit ír elő az orvoslásban a klasszikus 'primum non nocere' (mindenekelőtt ne árts) elv?", [
                    "Azt a legfőbb bioetikai követelményt, hogy az orvos semmilyen beavatkozással vagy mulasztással nem okozhat nagyobb kárt a betegnek, mint maga a betegség.",
                    "Azt, hogy a gyógyszereket mindig ingyen kell osztani.",
                    "Azt, hogy az orvos nem beszélhet idegen nyelven a műtőben."
                ], 0, ["c1-27-vocab"]),
                fb("grammar", "controlled", "A gyógyítónak erkölcsi kötelessége _____ a beteg életének védelmét minden más szempont elé helyezni. (would be / volna)", "volna", "It would be the moral duty of the healer to place the protection of patient life before all other aspects.", ["c1-modal-bioethical-imperatives"]),
                match("vocabulary", "controlled", [["primum non nocere", "a 'mindenekelőtt ne árts' orvosi alapelve"], ["betegbiztonság", "a kezelések kockázatmentességét célzó protokoll"], ["orvosi mulasztás", "a kellő gondosság hiányából fakadó orvosi hiba"], ["etikai imperatívusz", "feltétlen erkölcsi parancs a hivatás gyakorlásában"]], ["c1-27-vocab"]),
                fb("grammar", "practice", "A sebész semmilyen körülmények között nem _____ ki a pácienst fertőzésveszélynek. (must not expose / teheti)", "teheti", "The surgeon under no circumstances must expose the patient to risk of infection.", ["c1-modal-bioethical-imperatives"]),
                sb("grammar", "practice", ["Az", "orvos", "nem", "áldozhatja", "fel", "a", "betegbiztonságot", "a", "tekintélyért."], ["Az", "orvos", "nem", "áldozhatja", "fel", "a", "betegbiztonságot", "a", "tekintélyért."], "The physician cannot sacrifice patient safety for prestige.", ["c1-modal-bioethical-imperatives"]),
                dc("dialogue", [
                    {"speaker": "Kutatóorvos", "text": "Eltussolhatjuk-e a kórházi fertőzési adatokat a hírnév megőrzése érdekében?"},
                    {"speaker": "Klinikaigazgató", "text": "Semmiképp; a szakmai etika értelmében a vezetés nem _____ el a valós adatokat az érintettek elől."},
                    {"speaker": "Kutatóorvos", "text": "A transzparencia a betegbiztonság alapja."}
                ], ["hallgathatja", "mutathatja", "javíthatja"], 0, ["c1-modal-bioethical-imperatives"]),
                sw("production", [{"prompt": "Write a sentence articulating a physician's bioethical duty using a modal structure.", "answer": "Az orvosnak szakmai esküje és lelkiismerete parancsára feltétlenül védelmeznie kell a páciens életét, és nem teheti ki a beteget semmilyen elkerülhető fertőzésveszélynek."}], ["c1-modal-bioethical-imperatives"]),
                mc("grammar", "check", "Melyik modális forma fejez ki feltétlen orvosetikai kötelezettséget?", [
                    "köteles garantálni a betegbiztonságot / nem teheti ki elkerülhető veszélynek",
                    "jó lenne ha megmosná a kezét néha",
                    "tetszés szerint felveheti a kesztyűt"
                ], 0, ["c1-modal-bioethical-imperatives"])
            ]
        },
        {
            "num": 5,
            "stem": "c1-27-05",
            "title": "Semmelweis: The Etiology of Childbed Fever & Scalar Breakthrough",
            "grammar_title": "Scalar Evaluative Adverbials Calibrating Clinical Discovery and Public Health Impact",
            "grammar_skill": "c1-adv-scalar-medical-breakthrough",
            "goals": [
                "I can analyze Semmelweis Ignác's open letters and 1861 masterpiece (*A gyermekágyi láz kóroktana, nyílt levelek a professzorokhoz, klórmész-doktrína*).",
                "I can calibrate scientific breakthroughs using scalar evaluative adverbials (*orvostörténetileg korszakalkotó módon, a halálozást drámaian visszaszorítva, életmentő jelentőséggel*).",
                "I can critique the human tragedy of ahead-of-their-time scientific pioneers."
            ],
            "vocab": [
                {"lemma": "korszakalkotó áttörés", "translation": "epoch-making breakthrough", "pos": "expression"},
                {"lemma": "anyák megmentője", "translation": "savior of mothers", "pos": "expression"},
                {"lemma": "nyílt levél", "translation": "open letter", "pos": "expression"},
                {"lemma": "antiseptikus elv", "translation": "antiseptic principle", "pos": "expression"},
                {"lemma": "kórbonctani fertőzés", "translation": "cadaveric / autopsy infection", "pos": "expression"},
                {"lemma": "tragikus meg nem értettség", "translation": "tragic misunderstanding / lack of recognition", "pos": "expression"},
                {"lemma": "halálozási arány", "translation": "mortality rate / fatality ratio", "pos": "expression"},
                {"lemma": "klinikai igazság", "translation": "clinical truth", "pos": "expression"}
            ],
            "gr_text1": "Scalar evaluative adverbials evaluate the magnitude and revolutionary scope of medical breakthroughs: `orvostörténetileg korszakalkotó módon` (in a historically epoch-making manner), `a mortalitást drámaian és azonnal visszaszorítva` (suppressing mortality dramatically and immediately), `felbecsülhetetlen életmentő jelentőséggel bírva` (possessing inestimable life-saving significance), `az orvosi gondolkodást alapjaiban megújítva` (renewing medical thinking at its foundations).",
            "gr_text2": "Example: `Semmelweis Ignác orvostörténetileg korszakalkotó módon, a mortalitást drámaian visszaszorítva bizonyította be az antiszepszis életmentő igazságát`.",
            "gr_table": [
                ["Semmelweis orvostörténetileg korszakalkotó módon forradalmasította a higiéniát.", "Semmelweis in a historically epoch-making manner revolutionized hygiene."],
                ["A klóros lemosás a gyermekágyi halálozást drámaian visszaszorítva életeket mentett.", "Chlorinated washing suppressing puerperal mortality dramatically saved lives."],
                ["A felfedezés felbecsülhetetlen életmentő jelentőséggel bírt az egyetemes orvoslásban.", "The discovery had inestimable life-saving significance in universal medicine."]
            ],
            "classic_story": {
                "slug": "semmelweis-gyermekagyi-laz",
                "title": "A gyermekágyi láz kóroktana: Az anyák megmentőjének harca",
                "author": "Semmelweis Ignác",
                "work": "A gyermekágyi láz kóroktana (1861)",
                "summary": "Semmelweis Ignác, a magyar és egyetemes orvostudomány egyik legnagyobb alakja a bécsi I. sz. szülészeti klinikán döbbenten szembesült azzal, hogy az orvostanhallgatók által kezelt anyák sokszorta nagyobb arányban halnak meg gyermekágyi lázban, mint a bábák által ellátott II. osztályon. Miután barátja, Kolletschka professzor egy boncolási sebfertőzésben elhunyt, Semmelweis zseniális kórbonctani következtetéssel felismerte: az orvosok maguk hordozzák a holttestekről a fertőző anyagot a szülő nőkre. Bevezette a klórmeszes kézmosást, s a halálozási arány azonnal a töredékére zuhant.",
                "characters": ["Semmelweis Ignác, az anyák megmentője"],
                "paragraphs": [
                    {"type": "narration", "text": "1847 tavaszán a bécsi Allgemeines Krankenhaus falai között Semmelweis Ignác fiatal magyar orvosként olyan rejtéllyel nézett farkasszemet, amely évszázadok óta szedte áldozatait. A kórtermekben virágzó fiatal anyák ezrei haltak kínhalált magas lázban, miközben a korabeli orvosbárók tehetetlenül a miazmákra és a csillagok állására hivatkoztak."},
                    {"type": "dialogue", "speaker": "Semmelweis Ignác", "text": "A gyermekágyi láz nem önálló, titokzatos járvány, hanem kórbonctani anyag közvetlen átvitele által okozott vérfertőzés. Mi magunk, az orvosok és orvostanhallgatók voltunk a gyilkosok, kik a boncteremből mosatlan kézzel léptünk a vajúdó anyák ágyához!"},
                    {"type": "narration", "text": "Amikor Semmelweis elrendelte, hogy minden orvos és diák köteles klórmeszes oldatban kezet mosni mindaddig, míg a hullaszag teljesen el nem tűnik a bőrről, a klinika mortalitása hetek alatt 18 százalékról 1 százalék alá zuhant. A számok nem hazudtak: a higiéniai profilaxis a világ leghatékonyabb életmentő fegyverének bizonyult."},
                    {"type": "narration", "text": "A bécsi professzori kar hiúsága azonban nem bírta elviselni a bűntudat terhét. Semmelweist elüldözték Bécsből, felfedezését elutasították, s a meg nem értett zseni Pesten írta meg monumentális főművét. Orvostörténetileg korszakalkotó módon bizonyította be az igazságot, mely végül Pasteur és Lister munkásságán keresztül győzedelmeskedett az egész világon."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Hogyan jött rá Semmelweis Ignác a gyermekágyi láz valódi kórbonctani eredetére?", [
                    "Kolletschka törvényszéki orvosprofesszor boncolási sebfertőzésben bekövetkezett halálát elemezve rájött, hogy a kórbonctani részecskék véráramba kerülése azonos a gyermekágyi lázzal.",
                    "Egy régi egyiptomi papirusztekercs elolvasása után.",
                    "Véletlenül kiöntötte a teáját a boncasztalra."
                ], 0, ["c1-27-vocab"]),
                fb("grammar", "controlled", "Semmelweis felfedezése orvostörténetileg _____ módon írta át a fertőzésekről vallott nézeteket. (in an epoch-making / korszakalkotó)", "korszakalkotó", "Semmelweis's discovery in an epoch-making manner rewrote views held on infections.", ["c1-adv-scalar-medical-breakthrough"]),
                match("vocabulary", "controlled", [["anyák megmentője", "Semmelweis tiszteletbeli megnevezése"], ["korszakalkotó áttörés", "történelmi horderejű tudományos felfedezés"], ["antiseptikus elv", "kórokozók elpusztításának tana"], ["kórbonctani fertőzés", "holttestekből származó fertőző anyag átvitele"]], ["c1-27-vocab"]),
                fb("grammar", "practice", "A klórmeszes kézmosás a halálozást drámaian _____ mentette meg életek ezreit. (suppressing / visszaszorítva)", "visszaszorítva", "Chlorinated lime handwashing suppressing mortality dramatically saved thousands of lives.", ["c1-adv-scalar-medical-breakthrough"]),
                sb("grammar", "practice", ["Semmelweis", "felfedezése", "felbecsülhetetlen", "életmentő", "jelentőséggel", "bírt."], ["Semmelweis", "felfedezése", "felbecsülhetetlen", "életmentő", "jelentőséggel", "bírt."], "Semmelweis's discovery had inestimable life-saving significance.", ["c1-adv-scalar-medical-breakthrough"]),
                mc("reading", "context", "Miért utasította el a korabeli orvosi tekintélyelvű hierarchia Semmelweis tanait?", [
                    "Mert nem akarták elismerni, hogy a tisztelt orvosok és professzorok mosatlan kezükkel maguk okozták a páciensek halálát.",
                    "Mert nem szerették a klórmész fehér színét a kórházban.",
                    "Mert Semmelweis túl fiatalon kapott orvosi diplomát."
                ], 0, ["c1-27-vocab"]),
                sw("production", [{"prompt": "Write a reflection on Semmelweis's legacy using a scalar breakthrough adverbial.", "answer": "Semmelweis Ignác orvostörténetileg korszakalkotó módon, a mortalitást drámaian visszaszorítva fektette le a modern fertőtlenítés és járványtan alapjait, felbecsülhetetlen életmentő jelentőséggel gazdagítva az emberiséget."}], ["c1-adv-scalar-medical-breakthrough"]),
                mc("grammar", "check", "Melyik kifejezés kalibrálja a tudományos áttörés nagyságát a leghatásosabban?", [
                    "orvostörténetileg korszakalkotó módon / a mortalitást drámaian visszaszorítva",
                    "meglehetősen csendesen vizsgálódva",
                    "egy szép tavaszi délutánon"
                ], 0, ["c1-adv-scalar-medical-breakthrough"])
            ]
        }
    ]

    for l in core_lessons:
        emit_instructional_lesson(27, "core", l, core_title, core_intro if l["num"] == 1 else None)

    # Core Consolidation Lesson
    emit_consolidation_lesson(
        27,
        "core",
        "c1-27-consolidation",
        core_title,
        [
            "I can master the clinical and epidemiological terminology of disease etiology, prophylaxis, and antisepsis.",
            "I can deploy epidemiological adverbials, participial prophylactic modifiers, and counter-dogmatic adversative connectors.",
            "I can evaluate bioethical non-maleficence imperatives and Semmelweis Ignác's historical breakthrough."
        ],
        [
            mc("grammar", "recognize", "Melyik szerkezet fejez ki szigorú epidemiológiai és kórtani okságot?", [
                "kóroktanilag igazoltan / okságilag kimutatható módon",
                "véletlenül éppen úgy alakult tegnap",
                "mert szép idő volt a kórház udvarán"
            ], 0, ["c1-adv-clinical-epidemiological-causality"]),
            mc("grammar", "recognize", "Milyen szerkezettel jellemezhetünk egy életmentő orvosi beavatkozást?", [
                "a kórházi fertőzéseket megelőző és a mortalitást radikálisan visszaszorító eljárás",
                "amikor az orvos leül egy kávéra az ügyeletben",
                "hogyha kinyitják a folyosó ablakait"
            ], 0, ["c1-participle-prophylactic-intervention"]),
            match("vocabulary", "recognize", [["kóroktan", "a betegségek kiváltó okainak tudománya"], ["antiszepszis", "kórokozók elpusztítása fertőtlenítéssel"], ["primum non nocere", "a 'mindenekelőtt ne árts' orvosetikai alapelve"], ["korszakalkotó áttörés", "történelmi jelentőségű tudományos felfedezés"], ["anyák megmentője", "Semmelweis Ignác orvostörténeti epitheton ornansa"]], ["c1-27-vocab"]),
            fb("vocabulary", "recall", "A fertőzéseket vegyszerekkel megelőző eljárások összefoglaló neve az _____. (antisepsis / antiszepszis)", "antiszepszis", "The collective name of procedures preventing infections with chemicals is antisepsis.", ["c1-27-vocab"]),
            fb("vocabulary", "recall", "Az orvosi etika alapköve, a 'mindenekelőtt ne árts' latinul a primum non _____. (nocere / nocere)", "nocere", "The cornerstone of medical ethics, 'first, do no harm' in Latin is primum non nocere.", ["c1-27-vocab"]),
            fb("grammar", "recall", "A fertőzés útját kóroktanilag _____ adatokkal támasztotta alá a vizsgálat. (confirmed / igazolt)", "igazolt", "The investigation substantiated the path of infection with etiologically confirmed data.", ["c1-adv-clinical-epidemiological-causality"]),
            fb("grammar", "context", "A miazmatikus tévedéssel szemben a _____ a mikrobák okozzák a kórt. (in reality / valóságban)", "valóságban", "Contrary to the miasmatic error, in reality microbes cause the illness.", ["c1-adv-counter-dogmatic-adversatives"]),
            fb("grammar", "context", "Semmelweis tanítása orvostörténetileg _____ módon bizonyult igaznak. (in an epoch-making / korszakalkotó)", "korszakalkotó", "Semmelweis's teaching proved true in a historically epoch-making manner.", ["c1-adv-scalar-medical-breakthrough"]),
            mc("grammar", "context", "Hogyan működik az ellentétező érvelés az orvosi tévhitek leleplezésében?", [
                "A tekintélyelvű dogmákat szembesíti a statisztikailag cáfolhatatlan kísérleti adatokkal.",
                "Elnézést kér a professzoroktól a kellemetlen viták miatt.",
                "Megmutatja, milyen drága egy modern sztetoszkóp."
            ], 0, ["c1-adv-counter-dogmatic-adversatives"]),
            sb("grammar", "produce", ["A", "betegbiztonság", "és", "a", "higiénia", "az", "orvoslás", "legfőbb", "törvényei."], ["A", "betegbiztonság", "és", "a", "higiénia", "az", "orvoslás", "legfőbb", "törvényei."], "Patient safety and hygiene are the supreme laws of medicine.", ["c1-modal-bioethical-imperatives"]),
            sw("production", [{"prompt": "Formulate a statement on Semmelweis's antiseptic doctrine using an epidemiological adverbial.", "answer": "Semmelweis Ignác kóroktanilag igazoltan és epidemiológiailag alátámasztott módon bizonyította be, hogy a klórmeszes kézmosás azonnal és radikálisan megszünteti a halálos kórházi fertőzéseket."}], ["c1-adv-clinical-epidemiological-causality"]),
            sw("production", [{"prompt": "Write a critical reflection on the bioethical responsibility of physicians.", "answer": "Az orvosnak a 'primum non nocere' etikai imperatívusza alapján feltétlenül a betegbiztonságot kell szolgálnia, és semmilyen tekintélyelvű dogma vagy intézményi kényelem kedvéért nem kockáztathatja páciensei életét."}], ["c1-modal-bioethical-imperatives"])
        ]
    )

    # ----------------------------------------------------
    # TRACK 2: DISCOURSE (c1-egeszsegugy)
    # ----------------------------------------------------
    slug = "egeszsegugy"
    disc_intro = [
        "Hungary's healthcare system in the 2020s embodies a stark structural duality. While the historic 2021 physician wage reform eradicated informal gratuity payments (*hálapénz*), the simultaneous neglect of nurses, ballooning hospital debts, centralized county management, and the political neutralization of the Hungarian Medical Chamber (*MOK*) pushed public care to the brink of systemic exhaustion.",
        "In this discourse unit, through five serialized investigative accounts, you will analyze the mechanics of healthcare reform, nurse shortages, hospital debt spirals, chamber resistance, and the private-public healthcare divide at the C1 level."
    ]

    disc_lessons = [
        {
            "num": 1,
            "stem": f"c1-{slug}-01",
            "title": "Doctor Wage Reform, Gratuity Ban & Nurse Inequality",
            "grammar_title": "Discourse Framing Markers Diagnosing Systemic Healthcare Shortages and Structural Crises",
            "grammar_skill": "c1-discourse-healthcare-inequity-framing",
            "goals": [
                "I can analyze the 2021 medical wage reform, the criminalization of gratuity payments (*hálapénz kivezetése*), and the widening nurse-doctor wage gap (*szakdolgozói bérfeszültség*).",
                "I can deploy discourse framing markers diagnosing healthcare crises (*a szakdolgozói elvándorlás súlyosbodása, a bérfeszültség drasztikus kiéleződése, az ellátórendszer fokozatos kettészakadása*).",
                "I can debate the socioeconomic consequences of selective healthcare wage reforms."
            ],
            "vocab": [
                {"lemma": "hálapénz kivezetése", "translation": "eradication / criminalization of gratuity money", "pos": "expression"},
                {"lemma": "orvosi béremelés", "translation": "physician wage hike", "pos": "expression"},
                {"lemma": "szakdolgozói bérfeszültség", "translation": "nurse and assistant wage tension", "pos": "expression"},
                {"lemma": "egészségügyi szolgálati jogviszony", "translation": "healthcare service legal relationship (statute)", "pos": "expression"},
                {"lemma": "ápolóhiány", "translation": "nurse shortage", "pos": "noun"},
                {"lemma": "pályaelhagyás", "translation": "career abandonment / leaving the profession", "pos": "noun"},
                {"lemma": "ellátási egyenlőtlenség", "translation": "healthcare inequality", "pos": "expression"},
                {"lemma": "rendszerszintű krízis", "translation": "systemic crisis", "pos": "expression"}
            ],
            "gr_text1": "Discourse framing markers diagnose structural imbalances and operational dysfunction in public services: `a szakdolgozói bérfeszültség drasztikus kiéleződése révén` (through the drastic sharpening of nurse wage tension), `az ápolói elvándorlás és pályaelhagyás súlyosbodásaként` (as the aggravation of nurse emigration and career exit), `az ellátórendszer rendszerszintű kettészakadásának keretében` (within the framework of systemic tearing apart of the care system).",
            "gr_text2": "Example: `A szakértők az ellátórendszer fokozatos kettészakadásaként írták le az orvosi béremelés és a szakdolgozói elhanyagoltság közötti tátongó szakadékot`.",
            "gr_table": [
                ["A szakdolgozói bérfeszültség súlyosbodása tömeges felmondásokhoz vezetett.", "The worsening of healthcare worker wage tension led to mass resignations."],
                ["Az ellátórendszer rendszerszintű kettészakadása veszélyezteti az alapellátást.", "The systemic tearing apart of the healthcare system threatens primary care."],
                ["A hálapénz büntetőjogi kivezetése történelmi lépés volt a tiszta viszonyok felé.", "Criminal eradication of gratuities was a historic step towards clean relations."]
            ],
            "world_story_seg": {
                "seg_slug": "halapenz-beremeles-feszultseg",
                "title": "A hálapénz alkonya és a szakdolgozói bérszakadék",
                "summary": "2021-ben a kormány és az orvosi kamara megállapodásával megtörtént a történelmi orvosi béremelés és a hálapénz büntethetővé tétele. Ám az ápolók kimaradása azonnal mély bérfeszültséget szült.",
                "paragraphs": [
                    {"type": "narration", "text": "Évtizedeken át a megalázó hálapénz borítékai tartották fenn a magyar állami egészségügyet. 2021 januárjában a parlament elfogadta az új egészségügyi szolgálati jogviszonyról szóló törvényt, amely megtriplázta az orvosi béreket, és börtönbüntetéssel fenyegette a borítékok átadását és elfogadását."},
                    {"type": "dialogue", "speaker": "Dr. Molnár Péter kórházi sebész", "text": "A hálapénz megszüntetése erkölcsi megkönnyebbülést hozott. Ám a reform féloldalas maradt: miközben az orvosi bérek európai szintre emelkedtek, a műtősnők, aneszteziológus asszisztensek és ápolók fizetése megalázóan alacsony maradt."},
                    {"type": "narration", "text": "A szakdolgozói elvándorlás súlyosbodása villámgyorsan elérte a műtőket: orvos lett volna, aki operáljon, de műtősnő és aneszteziológus hiányában egész műtőblokkok álltak le."},
                    {"type": "narration", "text": "Az ellátórendszer rendszerszintű kettészakadása bebizonyította: a modern gyógyítás csapatmunka, és az orvosok megbecsülése az ápolók nélkül illúzió marad."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Miért volt történelmi jelentőségű a 2021-es egészségügyi jogviszony-törvény Magyarországon?", [
                    "Mert jelentősen megemelte az orvosok alapbérét, és büntetőjogi felelősségre vonás terhe mellett megtiltotta a hálapénz adását és elfogadását.",
                    "Mert ingyenessé tette a fogorvosi implantátumokat minden lakosnak.",
                    "Mert elrendelte, hogy minden orvos lovaskocsin járjon vizitelni."
                ], 0, ["c1-egeszsegugy-vocab"]),
                fb("grammar", "controlled", "A szakemberek az ellátórendszer _____ kettészakadásaként jellemezték a folyamatot. (systemic / rendszerszintű)", "rendszerszintű", "Experts characterized the process as the systemic tearing apart of the care system.", ["c1-discourse-healthcare-inequity-framing"]),
                match("vocabulary", "controlled", [["hálapénz kivezetése", "az orvosi borítékok büntetőjogi felszámolása"], ["szakdolgozói bérfeszültség", "orvosok és ápolók közötti jövedelmi szakadék"], ["egészségügyi szolgálati jogviszony", "az állami egészségügyben dolgozók kötött jogállása"], ["pályaelhagyás", "az egészségügyi szakma végleges elhagyása"]], ["c1-egeszsegugy-vocab"]),
                fb("grammar", "practice", "A szakdolgozói elvándorlás _____ miatt több kórházi osztály működése leállt. (worsening / súlyosbodása)", "súlyosbodása", "Due to the worsening of healthcare worker emigration several hospital wards ceased operations.", ["c1-discourse-healthcare-inequity-framing"]),
                sb("grammar", "practice", ["A", "szakdolgozók", "megbecsülése", "nélkül", "nem", "működhet", "a", "kórház."], ["A", "szakdolgozók", "megbecsülése", "nélkül", "nem", "működhet", "a", "kórház."], "Without appreciating healthcare workers the hospital cannot operate.", ["c1-discourse-healthcare-inequity-framing"]),
                dc("dialogue", [
                    {"speaker": "Főnővér", "text": "Hogyan élik meg az ápolók az új orvosi bértáblát?"},
                    {"speaker": "Kórházigazgató", "text": "A szakdolgozói bérfeszültség drasztikus _____ tapasztaljuk, ami tömeges pályaelhagyást okoz."},
                    {"speaker": "Főnővér", "text": "Ha nem emelik a béreket, nem lesz aki ellássa a betegeket."}
                ], ["kiéleződését", "csökkenését", "megoldását"], 0, ["c1-discourse-healthcare-inequity-framing"]),
                sw("production", [{"prompt": "Write a sentence diagnosing healthcare wage disparity using a crisis framing marker.", "answer": "Az orvosi bérek történelmi emelése mellett a szakdolgozói bérfeszültség súlyosbodása és az ápolók elvándorlása az ellátórendszer rendszerszintű működésképtelenségét idézte elő."}], ["c1-discourse-healthcare-inequity-framing"]),
                mc("grammar", "check", "Melyik kifejezés diagnosztizálja a kórházi humánerőforrás-válságot a leghitelesebben?", [
                    "a szakdolgozói elvándorlás súlyosbodása / a bérfeszültség kiéleződése",
                    "túl sok kávét isznak a nővérek",
                    "új egyenruhát kaptak a dolgozók"
                ], 0, ["c1-discourse-healthcare-inequity-framing"])
            ]
        },
        {
            "num": 2,
            "stem": f"c1-{slug}-02",
            "title": "Hospital Debt Spirals & County Center Consolidation",
            "grammar_title": "Deontic Modal Structures Condemning Legislative Curtailment of Professional Medical Self-Governance",
            "grammar_skill": "c1-modal-deontic-chamber-autonomy",
            "goals": [
                "I can analyze chronic hospital debt spirals, medical supplier insolvency, and county hospital centralization (*kórházi adósságállomány, beszállítói tartozások, vármegyei centrumkórházak*).",
                "I can formulate deontic modal structures condemning institutional interference (*az államnak tiszteletben kell tartania a szakmai autonómiát, nem foszthatja meg a kórházakat az önálló gazdálkodástól*).",
                "I can evaluate the operational consequences of chronic healthcare underfunding."
            ],
            "vocab": [
                {"lemma": "kórházi adósságállomány", "translation": "hospital debt volume / arrears", "pos": "expression"},
                {"lemma": "adósságkonszolidáció", "translation": "debt consolidation / bailout", "pos": "expression"},
                {"lemma": "beszállítói tartozás", "translation": "debt owed to medical suppliers", "pos": "expression"},
                {"lemma": "vármegyei centrumkórház", "translation": "county center hospital", "pos": "expression"},
                {"lemma": "műtéti várólista", "translation": "surgical waiting list", "pos": "expression"},
                {"lemma": "eszközhiány", "translation": "equipment / supplies shortage", "pos": "noun"},
                {"lemma": "pénzügyi elvonás", "translation": "financial withdrawal / clawback", "pos": "expression"},
                {"lemma": "költségvetési alulfinanszírozottság", "translation": "budgetary underfunding", "pos": "expression"}
            ],
            "gr_text1": "Deontic modal structures formulate governmental obligations to ensure functional solvency and respect institutional self-determination: `az államnak kötelessége volna biztosítani a kórházak valós költségvetési fedezetét` (the state would have a duty to ensure real budgetary coverage for hospitals), `nem háríthatja át a tartozásokat a beszállítókra` (cannot shift debts onto suppliers), `tiszteletben kell tartania a gyógyítók szakmai önállóságát` (must respect healers' professional autonomy), `nem kényszerítheti a vezetést a betegellátás korlátozására` (cannot force management to restrict patient care).",
            "gr_text2": "Example: `A kormánynak törvényi kötelessége szavatolni a kórházak pénzügyi stabilitását, és nem foszthatja meg az intézményeket a működéshez szükséges eszközöktől`.",
            "gr_table": [
                ["Az államnak kötelessége szavatolni a kórházak zavartalan működését.", "The state has a duty to guarantee undisturbed hospital operation."],
                ["A kormányzat nem foszthatja meg az orvosokat a szakmai önrendelkezéstől.", "The government cannot deprive doctors of professional self-determination."],
                ["A pénzügyi vezetés nem sodorhatja csődbe a létfontosságú orvosi beszállítókat.", "Financial leadership cannot drive vital medical suppliers into bankruptcy."]
            ],
            "world_story_seg": {
                "seg_slug": "korhazi-adossag-beszallitok",
                "title": "A százmilliárdos kórházi adósságspirál és az eszközhiány",
                "summary": "Évről évre százmilliárdos adósságot halmoztak fel a magyar kórházak. A kifizetetlen számlák miatt a beszállítók leállították az életmentő műszerek és implantátumok szállítását.",
                "paragraphs": [
                    {"type": "narration", "text": "Minden év vége felé menetrendszerűen megismétlődött a megalázó színjáték: a magyar kórházak kifizetetlen számlái elérték a százmilliárd forintot. A műtétekhez szükséges kötszerek, műszívbillentyűk, csípőprotézisek és steril kesztyűk gyártói hónapokon át hiába vártak a pénzükre."},
                    {"type": "dialogue", "speaker": "Dr. Molnár Péter", "text": "A kormánynak törvényi kötelessége volna valós áron finanszírozni a beavatkozásokat, nem pedig félévente megalázó adósságkonszolidációval foldozgatni a rendszert. Nem kényszeríthetik az orvost arra, hogy amiatt halasszon el műtétet, mert nincs beültethető protézis."},
                    {"type": "narration", "text": "A vármegyei centrumkórházak alá rendelt kisvárosi intézményekben az eszközhiány miatt sorra álltak le a szülészetek és a traumatológiai ellátás, a betegek pedig kénytelenek voltak órákat utazni a legközelebbi megyeszékhelyig."},
                    {"type": "narration", "text": "A várólisták megnyúlása és az állami kifizetések késleltetése nyilvánvalóan veszélyeztette a betegek életét."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Mi az oka a magyar állami kórházak krónikus, újratermelődő adósságállományának?", [
                    "Az, hogy a Nemzeti Egészségbiztosítási Alapkezelő (NEAK) által fizetett eljárási díjak nem fedezik a gyógyítás, a gyógyszerek és a rezsi valós piaci költségeit.",
                    "Az, hogy a kórházi osztályokon aranyból készítik a kilincseket.",
                    "Az orvosok túlzott külföldi konferencialátogatásai."
                ], 0, ["c1-egeszsegugy-vocab"]),
                fb("grammar", "controlled", "A kormánynak kötelessége _____ a kórházak valós költségeit fedező finanszírozást biztosítani. (would be / volna)", "volna", "It would be the government's duty to provide funding covering hospitals' real costs.", ["c1-modal-deontic-chamber-autonomy"]),
                match("vocabulary", "controlled", [["kórházi adósságállomány", "kifizetetlen kórházi számlák összessége"], ["adósságkonszolidáció", "az állam által utólag kifizetett adósságrendezés"], ["beszállítói tartozás", "orvostechnikai cégek felé fennálló elmaradás"], ["műtéti várólista", "halasztható beavatkozásokra várakozók névsora"]], ["c1-egeszsegugy-vocab"]),
                fb("grammar", "practice", "A minisztérium nem _____ meg a kórházakat az önálló gazdálkodás alapvető feltételeitől. (must not deprive / foszthatja)", "foszthatja", "The ministry must not deprive hospitals of the basic conditions of autonomous management.", ["c1-modal-deontic-chamber-autonomy"]),
                sb("grammar", "practice", ["Az", "államnak", "kötelessége", "biztosítani", "a", "kórházak", "stabil", "működését."], ["Az", "államnak", "kötelessége", "biztosítani", "a", "kórházak", "stabil", "működését."], "The state has a duty to secure hospitals' stable operation.", ["c1-modal-deontic-chamber-autonomy"]),
                dc("dialogue", [
                    {"speaker": "Beszállító", "text": "Már hat hónapja nem fizette ki a kórház az életmentő pacemaker számláit."},
                    {"speaker": "Orvosigazgató", "text": "Megértem a felháborodást; az állam nem _____ csődbe az orvosi eszközök szállítóit."},
                    {"speaker": "Beszállító", "text": "Kénytelenek leszünk felfüggeszteni a szállítást a konszolidációig."}
                ], ["sodorhatja", "hívhatja", "kérheti"], 0, ["c1-modal-deontic-chamber-autonomy"]),
                sw("production", [{"prompt": "Write a sentence articulating the state's healthcare obligation using a deontic modal structure.", "answer": "A kormánynak alkotmányos kötelessége szavatolni a kórházak fenntartható költségvetését, és nem kényszerítheti az orvosokat eszközhiányos kompromisszumokra a betegellátás rovására."}], ["c1-modal-deontic-chamber-autonomy"]),
                mc("grammar", "check", "Melyik modális forma fejezi ki a legpontosabban az állami felelősségvállalás kötelezettségét?", [
                    "kötelessége szavatolni / nem foszthatja meg az eszközöktől",
                    "ha kedve tartja, adhat egy kis pénzt",
                    "esetleg meglátogathatja az épületet"
                ], 0, ["c1-modal-deontic-chamber-autonomy"])
            ]
        },
        {
            "num": 3,
            "stem": f"c1-{slug}-03",
            "title": "Nurse Drain vs. Wage Gap Proportional Correlatives",
            "grammar_title": "Proportional Correlative Conjunctions Mapping Wage Gaps to Healthcare Capacity Collapse",
            "grammar_skill": "c1-adv-proportional-nurse-shortage",
            "goals": [
                "I can analyze nurse emigration, healthcare capacity closures, and proportional wage gaps (*ápolói bérszakadék, osztálybezárások, kapacitáscsökkenés, aneszteziológushiány*).",
                "I can deploy proportional correlative conjunctions mapping capacity collapse (*minél nagyobb a bérszakadék, annál több ápoló hagyja el a pályát, amilyen mértékben nő a túlterheltség, olyan arányban romlik az ellátás*).",
                "I can debate the systemic consequences of nursing staff exhaustion."
            ],
            "vocab": [
                {"lemma": "bérszakadék", "translation": "wage gap / disparity", "pos": "noun"},
                {"lemma": "túlterheltség", "translation": "overburdening / overwork", "pos": "noun"},
                {"lemma": "kapacitáscsökkentés", "translation": "capacity reduction / bed cuts", "pos": "expression"},
                {"lemma": "ügyeleti rendszer átalakítása", "translation": "on-call system reorganization", "pos": "expression"},
                {"lemma": "szakdolgozói kiégés", "translation": "healthcare worker burnout", "pos": "expression"},
                {"lemma": "ellátatlan körzet", "translation": "vacant / unserved GP district", "pos": "expression"},
                {"lemma": "ágybezárás", "translation": "hospital bed closure", "pos": "noun"},
                {"lemma": "szakemberhiány", "translation": "shortage of qualified professionals", "pos": "noun"}
            ],
            "gr_text1": "Proportional correlative structures (`minél... annál...`, `amilyen mértékben... olyan arányban...`) illustrate the direct relationship between human resource neglect and the physical collapse of healthcare departments: `Minél szélesebbre nyílik a bérszakadék az orvosok és szakdolgozók között, annál több ápoló hagyja el végleg az állami ellátást` (The wider the wage gap opens between doctors and nurses, the more nurses leave public care permanently), `Amilyen mértékben növekszik a személyzet túlterheltsége, olyan arányban sokasodnak a műtéti halasztások` (In proportion as staff overburdening increases, to that extent surgical postponements multiply).",
            "gr_text2": "Example: `Minél kevesebb megbecsülést kapnak a szakdolgozók, annál gyorsabban kényszerülnek a kórházak egész osztályok bezárására`.",
            "gr_table": [
                ["Minél nagyobb a bérszakadék, annál több képzett nővér vándorol ki Nyugat-Európába.", "The greater the wage gap, the more trained nurses emigrate to Western Europe."],
                ["Amilyen mértékben nő az ápolók túlterheltsége, olyan arányban emelkedik a kiégési ráta.", "To the extent nurse overburdening increases, to that extent the burnout rate rises."],
                ["Minél több a betöltetlen háziorvosi körzet, annál nehezebb a vidéki lakosság hozzáférése a gyógyításhoz.", "The more vacant GP districts there are, the harder rural access to healthcare becomes."]
            ],
            "world_story_seg": {
                "seg_slug": "apolo-elvandorlas-berres",
                "title": "Az ápolói elvándorlás és a szülészetek leállása",
                "summary": "Az ápolók és műtősök hiánya miatt országszerte szülészetek és sürgősségi osztályok kényszerültek ideiglenes vagy végleges bezárásra.",
                "paragraphs": [
                    {"type": "narration", "text": "2023-ban sokkoló hírek lepték el a sajtót: Szolnokon, Keszthelyen, Mohácson és Budapest több kerületében sorra jelentették be a szülészeti és gyermekgyógyászati ügyeletek leállását. A kórtermekben ott álltak a modern inkubátorok, de nem volt szakápoló, aki bekapcsolja őket."},
                    {"type": "dialogue", "speaker": "Dr. Molnár Péter", "text": "Minél inkább elmarad a szakdolgozók fizetése az orvosokétól, annál gyorsabban néptelenednek el a kórtermek. Egy intenzív osztályon egy ápolóra nem juthat öt lélegeztetett beteg anélkül, hogy ne következne be tragédia."},
                    {"type": "narration", "text": "A magyar ápolónők ezrei Ausztriában, Németországban vagy a hazai magánklinikákon vállaltak munkát, ahol emberi munkaidőt és tisztes megélhetést biztosítottak számukra."},
                    {"type": "narration", "text": "Amilyen mértékben elmélyült a szakemberhiány, olyan arányban vált a magyar állami ellátás az orvosok és betegek mindennapi túlélési harcává."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Miért álltak le szülészeti és traumatológiai osztályok több magyar kisvárosban a 2020-as években?", [
                    "Nem orvoshiány, hanem az ügyeletet vállaló szülésznők, altatóasszisztensek és ápolók hiánya és kiégése miatt.",
                    "Mert elromlott a kórház központi kapucsengője.",
                    "Mert a városi tanács elrendelte a délutáni pihenőt."
                ], 0, ["c1-egeszsegugy-vocab"]),
                fb("grammar", "controlled", "Minél nagyobb a bérszakadék az ágazatban, _____ több tapasztalt ápoló vándorol külföldre. (the more / annál)", "annál", "The greater the wage gap in the sector, the more experienced nurses emigrate abroad.", ["c1-adv-proportional-nurse-shortage"]),
                match("vocabulary", "controlled", [["bérszakadék", "jövedelmek közötti aránytalan távolság"], ["szakdolgozói kiégés", "fizikai és lelki kimerülés a túlterheltség miatt"], ["ellátatlan körzet", "állandó orvos nélküli háziorvosi praxis"], ["kapacitáscsökkentés", "működő ágyak és osztályok számának visszavágása"]], ["c1-egeszsegugy-vocab"]),
                fb("grammar", "practice", "Amilyen mértékben növekszik a személyzet túlterheltsége, olyan _____ sokasodnak a hibák. (proportion / arányban)", "arányban", "In proportion as staff overburdening increases, to that extent mistakes multiply.", ["c1-adv-proportional-nurse-shortage"]),
                sb("grammar", "practice", ["Minél", "kevesebb", "az", "ápoló,", "annál", "hosszabbak", "a", "várólisták."], ["Minél", "kevesebb", "az", "ápoló,", "annál", "hosszabbak", "a", "várólisták."], "The fewer the nurses, the longer the waiting lists.", ["c1-adv-proportional-nurse-shortage"]),
                dc("dialogue", [
                    {"speaker": "Újságíró", "text": "Miért zárt be a kisvárosi kórház szülészete a hétvégén?"},
                    {"speaker": "Főorvos", "text": "Minél inkább elvándorolnak az altatóasszisztensek, _____ kevésbé tudjuk garantálni a biztonságos császármetszést."},
                    {"speaker": "Újságíró", "text": "Így a kismamáknak ötven kilométert kell utazniuk."}
                ], ["annál", "mindig", "soha"], 0, ["c1-adv-proportional-nurse-shortage"]),
                sw("production", [{"prompt": "Write a sentence analyzing the nurse shortage using 'Minél... annál...'.", "answer": "Minél tovább mélyül a bérszakadék az orvosok és az ápolók között, annál több szakdolgozó hagyja el a pályát, ellehetetlenítve az állami kórházi osztályok működését."}], ["c1-adv-proportional-nurse-shortage"]),
                mc("grammar", "check", "Melyik szerkezet fejezi ki a bérfeszültség és a kapacitáscsökkenés egyenes arányosságát a legpontosabban?", [
                    "Minél nagyobb a bérszakadék... annál súlyosabb az elvándorlás / Amilyen mértékben... olyan arányban",
                    "Ha sok a hó, leáll a vasút",
                    "Mégis megpróbáltuk a dolgot"
                ], 0, ["c1-adv-proportional-nurse-shortage"])
            ]
        },
        {
            "num": 4,
            "stem": f"c1-{slug}-04",
            "title": "Chamber Neutralization & Patient Safety Stance",
            "grammar_title": "Epistemic Stance Markers Assessing Clinical Hazard and Systemic Patient Risk",
            "grammar_skill": "c1-epistemic-patient-safety-risk",
            "goals": [
                "I can analyze the political crackdown on the Hungarian Medical Chamber (*Magyar Orvosi Kamara, MOK*), compulsory membership abolition, and on-call boycotts (*ügyeleti bojkott*).",
                "I can employ elevated epistemic stance markers assessing clinical hazard (*közvetlenül veszélyezteti a betegbiztonságot, vélelmezhetően elkerülhető halálozáshoz vezet, orvosszakmailag súlyosan aggályos*).",
                "I can critique how political retaliation against professional advocacy undermines clinical governance."
            ],
            "vocab": [
                {"lemma": "Magyar Orvosi Kamara", "translation": "Hungarian Medical Chamber (MOK)", "pos": "noun"},
                {"lemma": "kötelező kamarai tagság", "translation": "compulsory chamber membership", "pos": "expression"},
                {"lemma": "etikai eljárás megvonása", "translation": "stripping of ethical jurisdiction", "pos": "expression"},
                {"lemma": "ügyeleti bojkott", "translation": "boycott of on-call duty contracts", "pos": "expression"},
                {"lemma": "politikai retorzió", "translation": "political retaliation", "pos": "expression"},
                {"lemma": "betegbiztonsági kockázat", "translation": "patient safety risk", "pos": "expression"},
                {"lemma": "orvosi autonómia csorbítása", "translation": "curtailment of medical autonomy", "pos": "expression"},
                {"lemma": "szakmai önszabályozás", "translation": "professional self-regulation", "pos": "expression"}
            ],
            "gr_text1": "Epistemic stance markers articulate evidence-based clinical assessments regarding health risks caused by administrative disruptions: `közvetlenül veszélyezteti a betegbiztonságot` (directly endangers patient safety), `orvosszakmailag súlyosan aggályos döntés` (decision seriously alarming from a professional medical standpoint), `vélelmezhetően elkerülhető halálozási kockázatot idéz elő` (presumptively generates avoidable mortality risk), `minden kétséget kizáróan rontja az ellátás minőségét` (impairs quality of care beyond all doubt).",
            "gr_text2": "Example: `A szakmai szervezetek rámutattak, hogy az új ügyeleti beosztás kényszerű átvitele orvosszakmailag súlyosan aggályos, és közvetlenül veszélyezteti a betegbiztonságot`.",
            "gr_table": [
                ["A tapasztalt szakorvosok hiánya közvetlenül veszélyezteti a betegbiztonságot.", "The lack of experienced specialists directly endangers patient safety."],
                ["A kamara jogköreinek elvonása orvosszakmailag súlyosan aggályos lépés volt.", "Stripping the chamber's powers was a seriously alarming step from a medical standpoint."],
                ["Az elhamarkodott átalakítás vélelmezhetően elkerülhető tragédiákat idéz elő.", "The hasty reorganization presumptively causes avoidable tragedies."]
            ],
            "world_story_seg": {
                "seg_slug": "mok-felszamolasa-retorzio",
                "title": "A Magyar Orvosi Kamara megfegyelmezése és a betegbiztonság",
                "summary": "Amikor a Magyar Orvosi Kamara az új ügyeleti szerződések aláírásának megtagadására szólított fel a méltatlan feltételek miatt, a kormány 24 óra alatt elvette a kamara kötelező tagságát és etikai jogköreit.",
                "paragraphs": [
                    {"type": "narration", "text": "2023 kora tavaszán a kormány és a Magyar Orvosi Kamara közötti feszültség a tetőpontjára hágott. A MOK küldöttközgyűlése nyomásgyakorlásként arra kérte a háziorvosokat, hogy ne írják alá az új, rosszul előkészített ügyeleti szerződéseket."},
                    {"type": "dialogue", "speaker": "Dr. Molnár Péter", "text": "A kormány válasza példátlan és villámgyors retorzió volt: egyetlen nap alatt törvényt hoztak, amellyel eltörölték a kötelező kamarai tagságot, és elvették a kamara évtizedes etikai bírósági jogkörét. Ez a döntés orvosszakmailag súlyosan aggályos volt."},
                    {"type": "narration", "text": "A hatalom az orvostársadalom megtörésére számított, ám a magyar orvosok többsége napokon belül önként megerősítette tagságát a kamarában. Világossá vált: az orvosi autonómia felszámolása közvetlenül veszélyezteti a betegbiztonságot."},
                    {"type": "narration", "text": "A politikai erőfitogtatás árát végső soron a betegek fizették meg, miközben a szakmai párbeszéd helyét a parancsuralmi igazgatás vette át."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Hogyan reagált a kormány a Magyar Orvosi Kamara 2023-as ügyeleti tiltakozására?", [
                    "Rendkívüli jogalkotással megszüntette a kötelező kamarai tagságot és az Egészségügyi Tudományos Tanácshoz helyezte át az etikai eljárásokat.",
                    "Duplájára emelte a kamara költségvetési támogatását.",
                    "Kitüntette a tiltakozó orvosok vezetőit a Parlamentben."
                ], 0, ["c1-egeszsegugy-vocab"]),
                fb("grammar", "controlled", "A szakemberek szerint a szakképzett személyzet hiánya közvetlenül veszélyezteti a _____ . (patient safety / betegbiztonságot)", "betegbiztonságot", "According to experts the lack of qualified staff directly endangers patient safety.", ["c1-epistemic-patient-safety-risk"]),
                match("vocabulary", "controlled", [["Magyar Orvosi Kamara", "az orvosok független szakmai és etikai köztestülete"], ["kötelező kamarai tagság", "az orvosi hivatás gyakorlásának korábbi feltétele"], ["ügyeleti bojkott", "túlterheltség miatti szerződés-aláírási megtagadás"], ["politikai retorzió", "hatalmi bosszú a szakmai kiállásért"]], ["c1-egeszsegugy-vocab"]),
                fb("grammar", "practice", "A sürgősségi ellátás központosítása orvosszakmailag súlyosan _____ lépésnek bizonyult. (alarming / aggályos)", "aggályos", "Centralization of emergency care proved to be a seriously alarming step from a professional medical standpoint.", ["c1-epistemic-patient-safety-risk"]),
                sb("grammar", "practice", ["Az", "orvosi", "autonómia", "csorbítása", "közvetlenül", "veszélyezteti", "a", "betegbiztonságot."], ["Az", "orvosi", "autonómia", "csorbítása", "közvetlenül", "veszélyezteti", "a", "betegbiztonságot."], "Curtailment of medical autonomy directly endangers patient safety.", ["c1-epistemic-patient-safety-risk"]),
                dc("dialogue", [
                    {"speaker": "Háziorvos", "text": "Milyen következménye van annak, hogy a kamara nem gyakorolhat etikai felügyeletet?"},
                    {"speaker": "Kamarai vezető", "text": "Ez a döntés közvetlenül veszélyezteti a _____ és az orvosi hivatás tisztaságát."},
                    {"speaker": "Háziorvos", "text": "Ezért állt ki a szakma egységesen a MOK mellett."}
                ], ["betegbiztonságot", "szórakozást", "pihenést"], 0, ["c1-epistemic-patient-safety-risk"]),
                sw("production", [{"prompt": "Write a sentence assessing clinical hazard using an epistemic stance marker.", "answer": "A traumatológiai és szülészeti ügyeletek közigazgatási centralizációja orvosszakmailag súlyosan aggályos, és közvetlenül veszélyezteti a betegbiztonságot a vidéki körzetekben."}], ["c1-epistemic-patient-safety-risk"]),
                mc("grammar", "check", "Melyik episztemikus kifejezés fogalmazza meg a klinikai veszélyt a legmagasabb szakmai súllyal?", [
                    "közvetlenül veszélyezteti a betegbiztonságot / orvosszakmailag súlyosan aggályos",
                    "esetleg nem a legkényelmesebb",
                    "olykor zavaró lehet"
                ], 0, ["c1-epistemic-patient-safety-risk"])
            ]
        },
        {
            "num": 5,
            "stem": f"c1-{slug}-05",
            "title": "Private-Public Duality & Healthcare Reconstruction",
            "grammar_title": "Evaluative Synthesis Particles Formulating Comprehensive Manifestos for Healthcare Reconstruction",
            "grammar_skill": "c1-adv-conclusive-public-health-synthesis",
            "goals": [
                "I can analyze the explosive boom of private healthcare, out-of-pocket spending, and the two-tiered healthcare reality (*magánegészségügyi bumm, zsebből fizetett ellátás, kettészakadt társadalom, szolidaritásalapú biztosítás*).",
                "I can employ evaluative synthesis particles formulating healthcare manifestos (*végső soron elkerülhetetlen, összegzésként leszögezhető, mindent egybevetve az emberi élet védelmének záloga*).",
                "I can articulate systemic visions for a modern, equitable public health service in Hungary."
            ],
            "vocab": [
                {"lemma": "magánegészségügyi bumm", "translation": "private healthcare boom", "pos": "expression"},
                {"lemma": "zsebből fizetett ellátás", "translation": "out-of-pocket care", "pos": "expression"},
                {"lemma": "kettészakadt egészségügy", "translation": "two-tiered healthcare", "pos": "expression"},
                {"lemma": "szolidaritásalapú biztosítás", "translation": "solidarity-based health insurance", "pos": "expression"},
                {"lemma": "hozzáférési egyenlőség", "translation": "equitable access", "pos": "expression"},
                {"lemma": "egészségügyi rekonstrukció", "translation": "healthcare reconstruction", "pos": "expression"},
                {"lemma": "állami felelősségvállalás", "translation": "state responsibility assumption", "pos": "expression"},
                {"lemma": "emberi élet szentsége", "translation": "sanctity of human life", "pos": "expression"}
            ],
            "gr_text1": "Evaluative synthesis particles formulate definitive manifestos for healthcare systemic revival: `végső soron elkerülhetetlen az állami ellátórendszer átfogó rekonstrukciója` (ultimately comprehensive reconstruction of the state care system is unavoidable), `mindent egybevetve a szolidaritásalapú gyógyítás az egyetlen igazságos út` (all in all solidarity-based healing is the only just path), `konklúzióként leszögezhető` (can be stated as a conclusion), `összességében tekintve az emberi méltóság és élet védelmének záloga` (taking it as a whole the pledge of protecting human dignity and life).",
            "gr_text2": "Example: `Végső soron elkerülhetetlen a szakdolgozói bérek rendezése és a kórházak korszerűsítése, hiszen az állami ellátás megmentése mindent egybevetve a nemzeti egészség záloga`.",
            "gr_table": [
                ["Végső soron elkerülhetetlen az ápolói bérek azonnali és radikális rendezése.", "Ultimately immediate and radical settlement of nurses' wages is unavoidable."],
                ["Mindent egybevetve a szolidaritásalapú állami ellátás az esélyegyenlőség alapja.", "All in all solidarity-based state healthcare is the foundation of equal opportunity."],
                ["Konklúzióként leszögezhető, hogy a magánellátás nem helyettesítheti a sürgősségi állami hálózatot.", "It can be stated as a conclusion that private care cannot replace the state emergency network."]
            ],
            "world_story_seg": {
                "seg_slug": "maganegeszsegugy-rekonstrukcio",
                "title": "A kettészakadt egészségügy és az újjáépítés víziója",
                "summary": "Aki megteheti, a magánklinikákra menekül, míg a szegényebbek a lepusztult állami ellátásban rekednek. A szakma szerint az állami gyógyítás rekonstrukciója elkerülhetetlen.",
                "paragraphs": [
                    {"type": "narration", "text": "A 2020-as évek közepére Magyarországon végleg létrejött a kétsebességes egészségügy. A tehetős polgárok a csillogó magánklinikákon fizetnek százezreket egy MRI-vizsgálatért vagy rutinműtétért, miközben a vidéki szegények hónapokat várnak a daganatos betegségek kivizsgálására a vakolathullató állami kórházakban."},
                    {"type": "dialogue", "speaker": "Dr. Molnár Péter", "text": "Ez a kettészakadás mélységesen igazságtalan és fenntarthatatlan. A magánszektor csak a profitábilis, könnyű beavatkozásokat vállalja; az intenzív terápiát, a traumát, a koraszülött-mentést és a sürgősségi ellátást kizárólag az állami kórházak viszik a hátukon."},
                    {"type": "narration", "text": "Végső soron elkerülhetetlen az állami gyógyítás átfogó rekonstrukciója: a szakdolgozók megbecsülése, az adósságok felszámolása és a betegközpontú intézmények megteremtése."},
                    {"type": "narration", "text": "Mindent egybevetve a közegészségügy nem piaci árucikk, hanem az emberi élet védelmének és a nemzet túlélésének legfőbb garanciája."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Miért nem képes a virágzó magánegészségügyi szektor teljes mértékben helyettesíteni az állami ellátást?", [
                    "Mert a magánklinikák nem tartanak fenn drága és veszteséges sürgősségi, intenzív terápiás és daganatsebészeti infrastruktúrát, így a súlyos kríziseket csak az állam tudja ellátni.",
                    "Mert a magánklinikákon tilos orvosi diplomával dolgozni.",
                    "Mert a magánorvosok csak homeopátiás szereket írhatnak fel."
                ], 0, ["c1-egeszsegugy-vocab"]),
                fb("grammar", "controlled", "_____ soron elkerülhetetlen a közegészségügy átfogó és mélyreható rekonstrukciója. (Ultimately / Végső)", "Végső", "Ultimately the comprehensive and profound reconstruction of public healthcare is unavoidable.", ["c1-adv-conclusive-public-health-synthesis"]),
                match("vocabulary", "controlled", [["magánegészségügyi bumm", "a fizetős magánorvosi ellátás robbanásszerű térnyerése"], ["zsebből fizetett ellátás", "a polgárok saját jövedelméből fedezett gyógyítás"], ["szolidaritásalapú biztosítás", "a rászorultságtól és jövedelemtől független közös biztosítás"], ["egészségügyi rekonstrukció", "az ellátórendszer átfogó újjáépítése"]], ["c1-egeszsegugy-vocab"]),
                fb("grammar", "practice", "Mindent _____, a közösségi egészségügy a társadalmi igazságosság legfőbb fundamentuma. (taking into account / egybevetve)", "egybevetve", "All in all, public healthcare is the supreme foundation of social justice.", ["c1-adv-conclusive-public-health-synthesis"]),
                sb("grammar", "practice", ["Végső", "soron", "elkerülhetetlen", "a", "közegészségügy", "radikális", "megújítása", "Magyarországon."], ["Végső", "soron", "elkerülhetetlen", "a", "közegészségügy", "radikális", "megújítása", "Magyarországon."], "Ultimately the radical renewal of public healthcare in Hungary is unavoidable.", ["c1-adv-conclusive-public-health-synthesis"]),
                dc("dialogue", [
                    {"speaker": "Egészséggazdász", "text": "Hogyan hidalható át a magán- és állami ellátás közötti mély szakadék?"},
                    {"speaker": "Professzor", "text": "Konklúzióként leszögezhető: mindent egybevetve a szolidaritásalapú gyógyítás az egyetlen méltó _____ a polgárok számára."},
                    {"speaker": "Egészséggazdász", "text": "Ezért kell prioritásként kezelni az állami kórházakat."}
                ], ["út", "akadály", "teher"], 0, ["c1-adv-conclusive-public-health-synthesis"]),
                sw("production", [{"prompt": "Write a concluding manifesto on public health reconstruction using 'Végső soron elkerülhetetlen'.", "answer": "Végső soron elkerülhetetlen az ápolói hivatás anyagi és erkölcsi megbecsülése, a kórházak valós finanszírozása és az állami közegészségügy megerősítése az emberi élet védelmének érdekében."}], ["c1-adv-conclusive-public-health-synthesis"]),
                mc("grammar", "check", "Melyik szintéziskifejezés formulázza meg az egészségügyi megújulást a legátfogóbb szinten?", [
                    "Végső soron elkerülhetetlen / mindent egybevetve a szolidaritás záloga",
                    "Majd meglátjuk mi történik jövőre",
                    "Gyorsan befejezzük a vizitet"
                ], 0, ["c1-adv-conclusive-public-health-synthesis"])
            ]
        }
    ]

    for l in disc_lessons:
        emit_instructional_lesson(27, "discourse", l, disc_title, disc_intro if l["num"] == 1 else None)

    # Combined World Story
    write_json(
        f"stories/world/c1/c1-{slug}-korhazi-valsag.json",
        {
            "id": f"story.c1.{slug}.combined",
            "title": "A gyógyítás válsága: Hálapénz, bérfeszültség és intézményi centralizáció",
            "level": "C1",
            "lesson": 5,
            "order": 27,
            "type": "world",
            "estimatedMinutes": 8,
            "grammar": ["c1-adv-conclusive-public-health-synthesis"],
            "summary": "Átfogó krónika a 2021-es orvosi béremelésről és a hálapénz kivezetéséről, az ápolói bérszakadék miatti tömeges pályaelhagyásról, a kórházi adósságspirálról, valamint a Magyar Orvosi Kamara elleni politikai fellépésről.",
            "vocabularyTopics": [
                "Healthcare in Crisis: Doctor Wage Reforms, Nurse Shortages & Chamber Control",
                "Private-Public Duality & Healthcare Reconstruction"
            ],
            "paragraphs": [
                {"type": "narration", "text": "A magyar egészségügy 2020 utáni korszakát drámai ellentmondások jellemezték. A hálapénz történelmi kivezetése és az orvosi alapbérek megtriplázása régóta esedékes, elengedhetetlen reform volt a tiszta viszonyok megteremtésére. Ám a szakdolgozói réteg elhanyagolása nyomán tátongó bérszakadék keletkezett az orvosok és az ápolók között, ami példátlan méretű pályaelhagyási hullámot indított el."},
                {"type": "narration", "text": "Minél szélesebbre nyílt a szakdolgozói bérszakadék, annál több szülészeti, gyermekgyógyászati és traumatológiai osztály kényszerült leállásra országszerte. A modern kórtermekben műszerek álltak, de hiányoztak a szakápolók és altatóasszisztensek, akik nélkül a biztonságos műtétek elvégzése orvosszakmailag súlyosan aggályossá vált, közvetlenül veszélyeztetve a betegbiztonságot."},
                {"type": "narration", "text": "Ezzel párhuzamosan a kórházak újratermelődő százmilliárdos adósságállománya és az orvostechnikai beszállítók felé felhalmozott tartozások miatt krónikus eszközhiány bénította meg a betegellátást. Amikor a Magyar Orvosi Kamara szót emelt az egyoldalú átalakítások ellen, a kormányzat huszonnégy óra alatt elvette a kamara kötelező tagságát és etikai jogköreit, megtorolva a szakmai kiállást."},
                {"type": "narration", "text": "A folyamat a magyar társadalom kettészakadásához vezetett: aki megtehette, a fizetős magánklinikákra menekült, míg a szegényebbek a lepusztult állami ellátásban rekedtek. Végső soron elkerülhetetlen kimondani: a szolidaritásalapú közegészségügy nem költségvetési teher, hanem a nemzet életének és egészségének nélkülözhetetlen fundamentuma."}
            ]
        }
    )

    # Discourse Consolidation
    emit_consolidation_lesson(
        27,
        "discourse",
        f"c1-{slug}-consolidation",
        disc_title,
        [
            "I can analyze the 2021 doctor wage reform, gratuity criminalization, and nurse wage tension.",
            "I can evaluate chronic hospital debt spirals, medical supplier arrears, and county hospital consolidation.",
            "I can debate the political neutralization of the Medical Chamber, clinical hazard markers, and public health reconstruction."
        ],
        [
            mc("grammar", "recognize", "Milyen szerkezettel diagnosztizálhatjuk az egészségügyi rendszer kettészakadását?", [
                "az ellátórendszer rendszerszintű kettészakadása / a szakdolgozói bérfeszültség kiéleződése",
                "hogyha elfogy a géz a szekrényből",
                "amikor az orvosok délután elmennek ebédelni"
            ], 0, ["c1-discourse-healthcare-inequity-framing"]),
            mc("grammar", "recognize", "Melyik modális kifejezés rögzíti az állami egészségügyi felelősséget a legszigorúbban?", [
                "kötelessége szavatolni a kórházak működését / nem foszthatja meg az autonómiától",
                "bármikor festhet egy képet a folyosóra",
                "szabadon dönthet a kerti fák ültetéséről"
            ], 0, ["c1-modal-deontic-chamber-autonomy"]),
            match("vocabulary", "recognize", [["hálapénz kivezetése", "orvosi borítékok büntetőjogi betiltása"], ["kórházi adósságállomány", "egészségügyi intézmények kifizetetlen számlái"], ["Magyar Orvosi Kamara", "orvosok önálló etikai köztestülete"], ["szakdolgozói bérfeszültség", "orvosok és ápolók közötti jövedelmi szakadék"], ["zsebből fizetett ellátás", "állampolgárok által közvetlenül finanszírozott magánorvoslás"]], ["c1-egeszsegugy-vocab"]),
            fb("vocabulary", "recall", "A kifizetetlen kórházi számlák miatt felhalmozódó kötelezettség a kórházi _____ . (debt volume / adósságállomány)", "adósságállomány", "The liability accumulating due to unpaid hospital bills is hospital debt volume.", ["c1-egeszsegugy-vocab"]),
            fb("vocabulary", "recall", "Az orvosok független szakmai szervezete a Magyar Orvosi _____ . (Chamber / Kamara)", "Kamara", "The independent professional organization of doctors is the Hungarian Medical Chamber.", ["c1-egeszsegugy-vocab"]),
            fb("grammar", "recall", "Az államnak kötelessége _____ szavatolni a kórházak fenntartható költségvetését. (would be / volna)", "volna", "It would be the state's duty to guarantee a sustainable hospital budget.", ["c1-modal-deontic-chamber-autonomy"]),
            fb("grammar", "context", "Minél nagyobb a bérszakadék, _____ több ápoló hagyja el az állami kórházakat. (the more / annál)", "annál", "The greater the wage gap, the more nurses leave state hospitals.", ["c1-adv-proportional-nurse-shortage"]),
            fb("grammar", "context", "Végső soron _____ az állami ellátórendszer átfogó és radikális rekonstrukciója. (unavoidable / elkerülhetetlen)", "elkerülhetetlen", "Ultimately comprehensive and radical reconstruction of the state care system is unavoidable.", ["c1-adv-conclusive-public-health-synthesis"]),
            mc("grammar", "context", "Mi a funkciója a 'Minél... annál...' arányossági szerkezetnek az egészségügyi elemzésekben?", [
                "A szakdolgozói bérlemaradás és az osztálybezárások közötti közvetlen ok-okozati összefüggést mutatja be.",
                "Megmagyarázza, hogy miért kell fertőtleníteni a műszereket.",
                "Elnézést kér az időjárás miatti késésekért."
            ], 0, ["c1-adv-proportional-nurse-shortage"]),
            sb("grammar", "produce", ["A", "közegészségügy", "a", "társadalmi", "szolidaritás", "és", "igazságosság", "záloga."], ["A", "közegészségügy", "a", "társadalmi", "szolidaritás", "és", "igazságosság", "záloga."], "Public healthcare is the pledge of social solidarity and justice.", ["c1-adv-conclusive-public-health-synthesis"]),
            sw("production", [{"prompt": "Write a critical diagnosis of healthcare shortages using a crisis framing marker.", "answer": "Az orvosi béremelés féloldalassága miatt a szakdolgozói bérfeszültség drasztikus kiéleződése és a kórházi adósságállomány újratermelődése az ellátórendszer fokozatos kettészakadásához vezetett."}], ["c1-discourse-healthcare-inequity-framing"]),
            sw("production", [{"prompt": "Formulate a concluding thought on public health reconstruction and the right to healthcare.", "answer": "Végső soron elkerülhetetlen az ápolói munka tisztességes megbecsülése, a kórházak fenntartható finanszírozása és az állami közegészségügy megerősítése az emberi méltóság és a betegbiztonság védelmében."}], ["c1-adv-conclusive-public-health-synthesis"])
        ]
    )

    print("=== Finished C1 Unit 27 ===")


if __name__ == "__main__":
    generate_unit_27()
