#!/usr/bin/env python3
"""
Hungarian C1 Block 2 - Unit 09 Generator:
  - Track 1 (Core): Unit 9 — "Bioethics, Human Dignity & Moral Quandaries" (c1-09)
  - Track 2 (Discourse): Unit 9 — "Ethics in Medicine, Biotechnology & Patient Rights" (c1-bioetika)
"""

import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT))

from scripts.c1_block1.common import mc, match, fb, sb, dc, sw, write_json, emit_instructional_lesson, emit_consolidation_lesson
from scripts.c1_block2.registry_helper import register_unit


def generate_unit_9():
    print("=== Generating C1 Unit 9 ===")
    
    # Register skills & titles
    new_skills = {
        "c1-09-vocab": {"kind": "vocabulary"},
        "c1-bioetika-vocab": {"kind": "vocabulary"},
        "c1-counterfactual-syntax": {"kind": "grammar"},
        "c1-deontic-epistemic-distinction": {"kind": "grammar"},
        "c1-ethical-quandaries": {"kind": "grammar"},
        "c1-biomedical-discourse": {"kind": "grammar"},
        "c1-patient-autonomy": {"kind": "grammar"},
    }
    new_titles = {
        "c1-09-vocab": "reading",
        "c1-bioetika-vocab": "reading",
        "c1-counterfactual-syntax": "multi tiered counterfactual conditional syntax and past modal framing",
        "c1-deontic-epistemic-distinction": "deontic necessity and epistemic probability in ethical evaluation",
        "c1-ethical-quandaries": "moral quandaries and bioethical dilemma argumentation structures",
        "c1-biomedical-discourse": "biomedical discourse and medical humanities stylistic registers",
        "c1-patient-autonomy": "patient autonomy end of life jurisprudence and self determination",
    }
    
    core_title = "Bioethics, Human Dignity & Moral Quandaries"
    core_stems = [f"c1-09-0{i}" for i in range(1, 6)] + ["c1-09-consolidation"]
    disc_title = "Ethics in Medicine, Biotechnology & Patient Rights"
    disc_stems = [f"c1-bioetika-0{i}" for i in range(1, 6)] + ["c1-bioetika-consolidation"]
    
    register_unit(9, core_title, core_stems, disc_title, disc_stems, new_skills, new_titles)

    # ----------------------------------------------------
    # TRACK 1: CORE (c1-09)
    # ----------------------------------------------------
    core_intro = [
        "Bioethics and human dignity push Hungarian syntax to its highest philosophical limits: multi-tiered past counterfactual conditionals (ha időben léptek volna, elkerülhető lett volna, hogy...), deontic duty vs. epistemic possibility, and ethical stance calibration.",
        "In this unit, inspired by László Németh's intellectual and medical essays in 'A minőség forradalma' (1940) and physician-philosopher reflections, you will master advanced counterfactual argumentation, moral dilemma formulation, and the Hungarian prose of bioethical deliberation."
    ]

    core_lessons = [
        {
            "num": 1,
            "stem": "c1-09-01",
            "title": "Multi-Tiered Past Counterfactual Syntax",
            "grammar_title": "Complex Counterfactual Conditionals in Retrospective Moral Evaluation",
            "grammar_skill": "c1-counterfactual-syntax",
            "goals": [
                "I can form multi-tiered past counterfactual clauses (*ha... volna, elkerülhető lett volna, hogy...*).",
                "I can embed potential past conditionals (*megtehette volna*) into ethical evaluations.",
                "I can express retrospective moral necessity without ambiguous tense reference."
            ],
            "vocab": [
                {"lemma": "elkerülhető lett volna", "translation": "would have been avoidable", "pos": "expression"},
                {"lemma": "megelőzhető lett volna", "translation": "could have been prevented", "pos": "expression"},
                {"lemma": "kötelessége lett volna", "translation": "it would have been their duty to", "pos": "expression"},
                {"lemma": "felelősségre vonás", "translation": "holding accountable, prosecution", "pos": "noun"},
                {"lemma": "mulasztás", "translation": "omission, neglect, failure to act", "pos": "noun"},
                {"lemma": "erkölcsi dilemmája", "translation": "moral dilemma of", "pos": "noun"},
                {"lemma": "visszatekintve", "translation": "in retrospect, looking back", "pos": "adverb"},
                {"lemma": "szükségszerűség", "translation": "necessity, inevitability", "pos": "noun"}
            ],
            "gr_text1": "Retrospective ethical critique relies on the past conditional auxiliary *volna*. When nested with potential mood (*-hat/-het*), it produces nuanced counterfactual assessments: *Ha a kezelőorvos tájékoztatta volna a beteget, elkerülhető lett volna a tragikus kimenetel.*",
            "gr_text2": "The predicate *kötelessége lett volna [infinitive]* asserts an unfulfilled deontic moral obligation in the past.",
            "gr_table": [
                ["Ha időben beavatkoztak volna, megelőzhető lett volna a kár.", "If they had intervened in time, the damage would have been preventable."],
                ["Az intézménynek kötelessége lett volna kivizsgálni az esetet.", "The institution would have had the duty to investigate the case."],
                ["Visszatekintve belátható, hogy más döntést kellett volna hozni.", "In retrospect it is understandable that a different decision should have been made."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mit fejez ki a 'megelőzhető lett volna' fordulat?", ["Egy múltbeli, elmaradt cselekvés miatt bekövetkezett esemény elkerülhetőségét.", "Egy jövőbeli biztos tervet.", "Jelenbeli egyszerű tényt."], 0, ["c1-09-vocab"]),
                fb("grammar", "controlled", "Ha a döntéshozók körültekintőbben jártak volna el, a tragédia teljes mértékben elkerülhető _____ volna. (would have been / lett)", "lett", "If the decision-makers had acted with greater circumspection, the tragedy would have been completely avoidable.", ["c1-counterfactual-syntax"]),
                match("vocabulary", "controlled", [["elkerülhető lett volna", "would have been avoidable"], ["mulasztás", "omission / neglect"], ["felelősségre vonás", "holding accountable"], ["visszatekintve", "in retrospect"]], ["c1-09-vocab"]),
                fb("grammar", "practice", "A kórháznak kutya _____ lett volna azonnal értesíteni a hozzátartozókat. (duty / kötelessége)", "kötelessége", "The hospital would have had the strict duty to notify the relatives immediately.", ["c1-counterfactual-syntax"]),
                sb("grammar", "practice", ["Visszatekintve", "a", "súlyos", "etikai", "mulasztás", "egyértelműen", "bebizonyosodott."], ["Visszatekintve", "a", "súlyos", "etikai", "mulasztás", "egyértelműen", "bebizonyosodott."], "In retrospect the severe ethical omission was unequivocally proven.", ["c1-counterfactual-syntax"]),
                dc("dialogue", [
                    {"speaker": "Bioetikus", "text": "Hárítható-e a felelősség a váratlan körülményekre?"},
                    {"speaker": "Bizottsági elnök", "text": "Nem, mert a kockázat ismeretében más döntést _____ volna hozniuk."},
                ], ["kellett", "akart", "tudott"], 0, ["c1-counterfactual-syntax"]),
                sw("production", [{"prompt": "Formulate a retrospective ethical critique using 'ha... lett volna'.", "answer": "Ha a klinikai vizsgálatot független etikai bizottság felügyelte volna, a súlyos mellékhatások megelőzhetők lettek volna."}], ["c1-counterfactual-syntax"]),
                mc("grammar", "check", "Melyik mondat fejez ki többlépcsős múltbeli ellenkező tényállású következtetést?", [
                    "Amennyiben a klinika időben felállította volna a diagnózist, elkerülhető lett volna, hogy a beteg állapota visszafordíthatatlanná váljon.",
                    "A beteg meggyógyult, mert jó volt az idő tegnap.",
                    "Ha akarják, majd holnap megvizsgálják a beteget."
                ], 0, ["c1-counterfactual-syntax"])
            ]
        },
        {
            "num": 2,
            "stem": "c1-09-02",
            "title": "Deontic Necessity vs. Epistemic Probability in Bioethics",
            "grammar_title": "Calibrating Moral Duty and Epistemic Risk in Medical Decisions",
            "grammar_skill": "c1-deontic-epistemic-distinction",
            "goals": [
                "I can distinguish deontic moral necessity (*kötelesség, elvárható*) from epistemic uncertainty (*valószínű, meglehet*).",
                "I can frame therapeutic risk assessments using high-precision modal adverbs.",
                "I can articulate doctor-patient ethical obligations in medical consultation Hungarian."
            ],
            "vocab": [
                {"lemma": "elvárható magatartás", "translation": "conduct reasonably expected", "pos": "expression"},
                {"lemma": "etikai kötelesség", "translation": "ethical duty / obligation", "pos": "noun"},
                {"lemma": "minden bizonnyal", "translation": "in all certainty, most certainly", "pos": "adverb"},
                {"lemma": "feltehetőleg", "translation": "presumably, supposedly", "pos": "adverb"},
                {"lemma": "kockázatértékelés", "translation": "risk assessment", "pos": "noun"},
                {"lemma": "aránytalan kockázat", "translation": "disproportionate risk", "pos": "noun"},
                {"lemma": "tájékozott beleegyezés", "translation": "informed consent", "pos": "noun"},
                {"lemma": "mérlegelés tárgyát képezi", "translation": "forms the subject of deliberation", "pos": "expression"}
            ],
            "gr_text1": "Bioethical argumentation carefully distinguishes what an actor *ought to do* (deontic: *elvárható magatartás, etikai imperatívusz*) from what is *likely to occur* (epistemic: *feltehetőleg, minden bizonnyal*).",
            "gr_text2": "Conflating moral duty with statistical probability is a severe fallacy: even if a procedure will *almost certainly succeed* (*minden bizonnyal sikeres lesz*), performing it without informed consent violates deontic duty (*sérti az etikai kötelezettséget*).",
            "gr_table": [
                ["Az orvostól elvárható gondosság etikai és jogi kötelesség.", "Due care expected of a physician is an ethical and legal duty."],
                ["A beavatkozás minden bizonnyal meghosszabbítja az életet, de kockázatos.", "The intervention in all certainty prolongs life, but is risky."],
                ["A terápia folytatása szigorú orvosetikai mérlegelés tárgyát képezi.", "Continuation of therapy forms the subject of strict medical-ethical deliberation."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mit jelent a 'tájékozott beleegyezés' alapelve a gyógyászatban?", ["A beteg önrendelkező jogát arra, hogy a kockázatok teljes megismerése után döntsön a kezelésről.", "A kórházi számla azonnali kifizetését.", "Az orvos utasításainak vakon történő követését."], 0, ["c1-09-vocab"]),
                fb("grammar", "controlled", "A kezelőorvos részéről az adott helyzetben általában _____ gondosság elmulasztása műhibának minősül. (expected / elvárható)", "elvárható", "Failure to provide due care generally expected of the treating physician in the given situation qualifies as malpractice.", ["c1-deontic-epistemic-distinction"]),
                match("vocabulary", "controlled", [["tájékozott beleegyezés", "informed consent"], ["elvárható magatartás", "conduct expected"], ["kockázatértékelés", "risk assessment"], ["etikai kötelesség", "ethical duty"]], ["c1-09-vocab"]),
                fb("grammar", "practice", "Bár a terápia sikere _____ valószínű, a mellékhatások aránytalan terhet rónának a betegre. (highly / felettébb / rendkívül / igen)", "igen", "Although the success of therapy is highly likely, side effects would impose a disproportionate burden on the patient.", ["c1-deontic-epistemic-distinction"]),
                sb("grammar", "practice", ["A", "beteg", "emberi", "méltósága", "minden", "technológiai", "szempontot", "megelőz."], ["A", "beteg", "emberi", "méltósága", "minden", "technológiai", "szempontot", "megelőz."], "The human dignity of the patient precedes every technological consideration.", ["c1-deontic-epistemic-distinction"]),
                dc("dialogue", [
                    {"speaker": "Kutatóorvos", "text": "Alkalmazhatjuk-e a kísérleti szert sürgős esetben beleegyezés nélkül?"},
                    {"speaker": "Etikai tanácsadó", "text": "Nem, a tájékozott beleegyezés mellőzhetetlen etikai _____ képez."},
                ], ["kötelességet", "ötletet", "kívánságot"], 0, ["c1-deontic-epistemic-distinction"]),
                sw("production", [{"prompt": "Contrast moral duty and medical probability in one sentence.", "answer": "Bár az operáció statisztikailag nagy valószínűséggel sikeres lenne, a beteg kifejezett visszautasítása esetén az orvosi etika tiltja a kényszerkezelést."}], ["c1-deontic-epistemic-distinction"]),
                mc("grammar", "check", "Melyik állítás fogalmazza meg helyesen a deontikus kötelezettség abszolút primátusát?", [
                    "A beteg autonómiájának tiszteletben tartása olyan abszolút etikai kötelesség, amely felülírja a puszta statisztikai valószínűségeket.",
                    "Ha az orvos okosabb a betegnél, akkor azt csinál, amit akar.",
                    "A betegnek nincs joga visszautasítani a kezelést, ha a családja úgy akarja."
                ], 0, ["c1-deontic-epistemic-distinction"])
            ]
        },
        {
            "num": 3,
            "stem": "c1-09-03",
            "title": "Structuring Complex Moral Dilemmas and Quandaries",
            "grammar_title": "Antithetical Framing in Insoluble Ethical Choices",
            "grammar_skill": "c1-ethical-quandaries",
            "goals": [
                "I can frame insoluble ethical choices (*morális csapdahelyzet, két rossz közötti választás*).",
                "I can structure multi-premise moral dilemmas using balanced concessive antithesis.",
                "I can analyze classic ethical paradoxes (triage, organ allocation, resource scarcity)."
            ],
            "vocab": [
                {"lemma": "morális csapdahelyzet", "translation": "moral trap / catch-22 situation", "pos": "noun"},
                {"lemma": "két rossz közül a kisebbik", "translation": "the lesser of two evils", "pos": "expression"},
                {"lemma": "erőforrás-szűkösség", "translation": "resource scarcity", "pos": "noun"},
                {"lemma": "triage", "translation": "triage, prioritization of casualties", "pos": "noun"},
                {"lemma": "feloldhatatlan ellentmondás", "translation": "insoluble contradiction", "pos": "noun"},
                {"lemma": "lelkiismereti konfliktus", "translation": "conflict of conscience", "pos": "noun"},
                {"lemma": "értékkonfliktus", "translation": "conflict of values", "pos": "noun"},
                {"lemma": "kényszerhelyzet", "translation": "state of necessity / duress", "pos": "noun"}
            ],
            "gr_text1": "Complex ethical dilemmas (such as emergency pandemic triage) represent situations where every available course of action violates some moral principle. Hungarian frames this via *feloldhatatlan értékkonfliktus*.",
            "gr_text2": "Syntactic structures employ antithetical parallelisms: *Bármelyik döntést hozza is a kezelőorvos, szükségszerűen erkölcsi terhet vesz magára.*",
            "gr_table": [
                ["Erőforrás-szűkösség idején a prioritások felállítása feloldhatatlan dilemmát jelent.", "In times of resource scarcity setting priorities represents an insoluble dilemma."],
                ["Két rossz közül a kisebbik kiválasztása nem szünteti meg az erkölcsi felelősséget.", "Choosing the lesser of two evils does not eliminate moral responsibility."],
                ["A döntéshozó súlyos lelkiismereti konfliktusba kényszerül.", "The decision-maker is forced into a severe conflict of conscience."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mit nevezünk 'morális csapdahelyzetnek' a bioetikában?", ["Olyan kényszerhelyzetet, ahol minden lehetséges döntés valamilyen alapvető erkölcsi értéket sért.", "Egy jól sikerült orvosi vizsgát.", "A gyógyszerek olcsó árát."], 0, ["c1-09-vocab"]),
                fb("grammar", "controlled", "A járvány idején az orvosoknak feloldhatatlan érték-_____ kellett meghozniuk a lélegeztetőgépek elosztásáról szóló döntést. (conflict / konfliktusban)", "konfliktusban", "During the epidemic physicians had to make decisions on the allocation of ventilators in an insoluble conflict of values.", ["c1-ethical-quandaries"]),
                match("vocabulary", "controlled", [["morális csapdahelyzet", "moral trap"], ["erőforrás-szűkösség", "resource scarcity"], ["triage", "triage prioritization"], ["értékkonfliktus", "conflict of values"]], ["c1-09-vocab"]),
                fb("grammar", "practice", "Katasztrófahelyzetben a triage eljárás a két rossz közül a _____ választás kényszerét jelenti. (lesser / kisebbik)", "kisebbik", "In disaster situations the triage procedure represents the compulsion of choosing the lesser of two evils.", ["c1-ethical-quandaries"]),
                sb("grammar", "practice", ["Az", "élet", "mentése", "és", "a", "szenvedés", "csillapítása", "néha", "ütközik", "egymással."], ["Az", "élet", "mentése", "és", "a", "szenvedés", "csillapítása", "néha", "ütközik", "egymással."], "Saving life and alleviating suffering sometimes collide with each other.", ["c1-ethical-quandaries"]),
                dc("dialogue", [
                    {"speaker": "Főorvos", "text": "Hogyan döntsünk az egyetlen szabad intenzív ágy sorsáról?"},
                    {"speaker": "Etikai felelős", "text": "Kizárólag az objektív orvosi esélyek és az előzetes protokoll alapján, kizárva minden szubjektív _____."},
                ], ["részrehajlást", "gyógyszert", "ápolót"], 0, ["c1-ethical-quandaries"]),
                sw("production", [{"prompt": "Describe the ethical dilemma of medical triage during resource scarcity.", "answer": "Extrém erőforrás-szűkösség esetén a triage kényszere feloldhatatlan morális dilemmát teremt: az orvosnak az esélyek alapján kell döntenie anélkül, hogy az emberi élet abszolút értékét relativizálná."}], ["c1-ethical-quandaries"]),
                mc("grammar", "check", "Melyik elv nyújt iránymutatást a bioetikai csapdahelyzetek kezelésében?", [
                    "Az előre rögzített, átlátható és diszkriminációmentes szakmai protokollok alkalmazása.",
                    "A pénzügyi licitálás a betegek között.",
                    "A kezelés azonnali beszüntetése mindenkinél."
                ], 0, ["c1-ethical-quandaries"])
            ]
        },
        {
            "num": 4,
            "stem": "c1-09-04",
            "title": "Patient Autonomy and End-of-Life Jurisprudence",
            "grammar_title": "Self-Determination and End-of-Life Stance Framing",
            "grammar_skill": "c1-patient-autonomy",
            "goals": [
                "I can analyze the legal and ethical boundaries of patient self-determination (*önrendelkezési jog*).",
                "I can navigate Hungarian jurisprudence on the refusal of life-sustaining treatment.",
                "I can express compassionate, philosophically rigorous positions on palliative care and euthanasia."
            ],
            "vocab": [
                {"lemma": "önrendelkezési jog", "translation": "right to self-determination", "pos": "noun"},
                {"lemma": "életfenntartó kezelés", "translation": "life-sustaining treatment", "pos": "noun"},
                {"lemma": "visszautasítás joga", "translation": "right to refuse (treatment)", "pos": "noun"},
                {"lemma": "palliatív ellátás", "translation": "palliative care", "pos": "noun"},
                {"lemma": "eutanázia", "translation": "euthanasia", "pos": "noun"},
                {"lemma": "méltóságteljes halál", "translation": "dignified death / dying with dignity", "pos": "noun"},
                {"lemma": "élő végrendelet", "translation": "living will, advance directive", "pos": "noun"},
                {"lemma": "szenvedésenyhítés", "translation": "alleviation of suffering", "pos": "noun"}
            ],
            "gr_text1": "Hungarian health law grants patients the fundamental right to refuse life-sustaining treatment (*életfenntartó kezelés visszautasítása*) under strict formal conditions: if suffering from an incurable, terminal illness.",
            "gr_text2": "Active euthanasia (*aktív eutanázia*) remains criminalized in Hungary, sparking landmark domestic and European Court of Human Rights cases regarding bodily autonomy versus the state's duty to protect life.",
            "gr_table": [
                ["A beteg önrendelkezési joga a kezelés visszautasítására...", "The patient's right to self-determination to refuse treatment..."],
                ["Méltóságteljes halál és a palliatív szedáció etikai keretei...", "Dignified death and the ethical frameworks of palliative sedation..."],
                ["Az élő végrendelet mint a jövőbeli akarat jogi kinyilvánítása...", "The living will as the legal declaration of future intent..."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Milyen jog illeti meg a gyógyíthatatlan beteget a magyar egészségügyi törvény szerint?", ["A kezelés visszautasításának joga szigorú formai feltételek mellett.", "A kórház épületének elbontása.", "Bármilyen külföldi orvos azonnali behívása állami költségen."], 0, ["c1-09-vocab"]),
                fb("grammar", "controlled", "A beteg emberi méltóságának része a méltóságteljes _____ való jog a gyógyíthatatlan betegség végső stádiumában. (to death / halálhoz)", "halálhoz", "Part of the patient's human dignity is the right to a dignified death in the terminal stage of incurable illness.", ["c1-patient-autonomy"]),
                match("vocabulary", "controlled", [["önrendelkezési jog", "right to self-determination"], ["palliatív ellátás", "palliative care"], ["életfenntartó kezelés", "life-sustaining treatment"], ["élő végrendelet", "living will"]], ["c1-09-vocab"]),
                fb("grammar", "practice", "A terminális állapotban lévő beteg előzetes jognyilatkozatban, úgynevezett élő _____ rendelkezhet a kezelések elutasításáról. (will / végrendeletben)", "végrendeletben", "A patient in terminal condition may dispose of the refusal of treatments in an advance declaration, a so-called living will.", ["c1-patient-autonomy"]),
                sb("grammar", "practice", ["A", "szenvedés", "enyhítése", "a", "palliatív", "orvoslás", "legfőbb", "küldetése."], ["A", "szenvedés", "enyhítése", "a", "palliatív", "orvoslás", "legfőbb", "küldetése."], "Alleviation of suffering is the chief mission of palliative medicine.", ["c1-patient-autonomy"]),
                dc("dialogue", [
                    {"speaker": "Jogász", "text": "Hogyan egyeztethető össze az élethez való jog a beteg akaratával?"},
                    {"speaker": "Etikus", "text": "Az élet szentsége nem jelenthet kötelezettséget a kilátástalan és emberhez méltatlan _____ elviselésére."},
                ], ["szenvedés", "gyógyulás", "pihenés"], 0, ["c1-patient-autonomy"]),
                sw("production", [{"prompt": "Formulate a position on the boundary between life preservation and dignified death.", "answer": "Az orvosi hivatás feladata az élet védelme, de a gyógyítás nem válhat terápiás túlbuzgósággá; a beteg önrendelkező döntése a méltóságteljes elmúlásról tiszteletben tartandó."}], ["c1-patient-autonomy"]),
                mc("grammar", "check", "Mi képezi a palliatív terápia legfontosabb etikai célját?", [
                    "A fájdalomcsillapítás, a tüneti enyhítés és a pszichológiai támogatás biztosítása a beteg méltóságának megőrzésével.",
                    "A beteg elszigetelése a külvilágtól.",
                    "Kizárólag költségcsökkentési szempontok érvényesítése."
                ], 0, ["c1-patient-autonomy"])
            ]
        },
        {
            "num": 5,
            "stem": "c1-09-05",
            "title": "The Quality Revolution and the Healer's Ethos: László Németh",
            "grammar_title": "The Physician-Philosopher Ethos in Hungarian Intellectual History",
            "grammar_skill": "c1-biomedical-discourse",
            "goals": [
                "I can analyze László Németh's vision of the healer and intellectual in 'A minőség forradalma'.",
                "I can explore the synthesis of natural science, medical practice, and moral responsibility.",
                "I can produce elevated philosophical prose on the ethos of human healing."
            ],
            "vocab": [
                {"lemma": "orvosi etosz", "translation": "medical ethos / healer's ethos", "pos": "noun"},
                {"lemma": "a minőség forradalma", "translation": "the revolution of quality", "pos": "noun"},
                {"lemma": "hivatástudat", "translation": "sense of vocation / calling", "pos": "noun"},
                {"lemma": "terápiás nihilizmus", "translation": "therapeutic nihilism", "pos": "noun"},
                {"lemma": "holisztikus szemlélet", "translation": "holistic perspective", "pos": "noun"},
                {"lemma": "embereszmény", "translation": "human ideal, conception of man", "pos": "noun"},
                {"lemma": "elkötelezettség", "translation": "commitment, engagement", "pos": "noun"},
                {"lemma": "lelkiismeretesség", "translation": "conscientiousness", "pos": "noun"}
            ],
            "gr_text1": "László Németh (1901–1975), novelist, playwright, and practicing physician, brought unique scientific rigor and moral fervor to Hungarian essay prose. In *A minőség forradalma*, he argued that true civilization is not quantity, but uncompromising quality of the spirit.",
            "gr_text2": "For Németh, the physician is not a biological technician, but the custodian of the whole person (*a teljes ember gondozója*), uniting empirical observation with deep ethical empathy.",
            "gr_table": [
                ["A minőség forradalma mint az intellektuális és orvosi megújulás záloga...", "The revolution of quality as the pledge of intellectual and medical renewal..."],
                ["Az orvos felelőssége nem ér véget a testi tünetek kezelésénél.", "The physician's responsibility does not end with treating physical symptoms."],
                ["Hivatástudat és mély etikai elkötelezettség a beteg ember mellett...", "Sense of vocation and deep ethical commitment beside the suffering person..."]
            ],
            "classic_story": {
                "slug": "c1-09-nemeth",
                "author": "Németh László",
                "work": "A minőség forradalma (1940) / Magam helyett",
                "title": "A gyógyító felelőssége és a minőség forradalma",
                "summary": "László Németh's profound synthesis of medical science, intellectual vocation, and the uncompromising moral demands of human healing.",
                "characters": ["Németh László"],
                "paragraphs": [
                    {"type": "narration", "text": "Németh László azon ritka szellemi óriások közé tartozott, akik egyszerre voltak avatott művelői a modern természettudománynak és a világirodalomnak. Mint gyakorló orvos és iskolaorvos, nap mint nap a fizikai valóság legnyersebb tényeivel – a betegséggel, a szegénységgel és az emberi esendőséggel – szembesült. Ez a tapasztalat óvta meg őt az üres szellemi absztrakcióktól, miközben orvosi munkáját mindig mély filozófiai távlatba helyezte."},
                    {"type": "narration", "text": "A minőség forradalma című művében Németh kifejtette, hogy a huszadik század igazi tragédiája a mennyiség uralma a minőség felett. A technológiai fejlődés és a tömegtermelés elvakította az embert, miközben elsorvadt a lelkiismeret és a belső igényesség. Az orvosi hivatásban ez a veszély abban nyilvánul meg, amikor a gyógyító puszta szerelővé, biológiai technikussá válik, elfelejtve, hogy minden kórkép mögött egyedi, megismételhetetlen emberi lélek küzd a megmaradásért."},
                    {"type": "narration", "text": "Németh számára az orvosi etosz nem szakmai protokollok rideg betartását jelentette, hanem teljes odaadást: a beteg panaszának értő meghallgatását, a testi és lelki okok holisztikus felderítését és a gyógyítás mélységes felelősségét. A minőség forradalma nem politikai mozgalom, hanem belső morális átalakulás: az az elhatározás, hogy minden munkánkat a legmagasabb intellektuális és erkölcsi mérce szerint végezzük."},
                    {"type": "narration", "text": "Tanítása ma, a géntechnológia és a mesterséges intelligencia korában időszerűbb, mint valaha. Arra emlékeztet, hogy a legfejlettebb orvosi műszer sem pótolhatja az emberi részvétet, és a tudomány igazi nagysága mindig a kiszolgáltatottak melletti önzetlen kiállásban mutatkozik meg."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Mit értett Németh László 'a minőség forradalma' alatt?", ["A belső erkölcsi és intellektuális igényesség primátusát a tömegtermeléssel és felületességgel szemben.", "A kórházak bezárását.", "Kizárólag a legdrágább külföldi gyógyszerek vásárlását."], 0, ["c1-09-vocab"]),
                fb("grammar", "controlled", "Németh László szerint az orvos nem válhat biológiai technikussá; kötelessége a teljes ember _____ vizsgálata. (holistic / holisztikus)", "holisztikus", "According to László Németh the physician must not become a biological technician; it is his duty to examine the whole person holistically.", ["c1-biomedical-discourse"]),
                match("vocabulary", "controlled", [["orvosi etosz", "healer's ethos"], ["hivatástudat", "sense of vocation"], ["a minőség forradalma", "revolution of quality"], ["holisztikus szemlélet", "holistic view"]], ["c1-09-vocab"]),
                mc("reading", "practice", "Miért jelentett óriási előnyt Németh László számára orvosi végzettsége írói munkásságában?", [
                    "Mert közvetlen kapcsolatban tartotta a valósággal, a test törvényeivel és az emberi esendőséggel.",
                    "Mert nem kellett könyveket olvasnia.",
                    "Mert csak orvosi szakkönyveket írt."
                ], 0, None),
                sb("grammar", "practice", ["A", "technológiai", "fejlődés", "nem", "pótolhatja", "az", "orvosi", "részvétet", "és", "figyelmet."], ["A", "technológiai", "fejlődés", "nem", "pótolhatja", "az", "orvosi", "részvétet", "és", "figyelmet."], "Technological advancement cannot replace medical empathy and attentiveness.", ["c1-biomedical-discourse"]),
                sw("production", [{"prompt": "Synthesize Németh László's view of the medical vocation.", "answer": "Németh László értelmezésében a gyógyítás nem gépies biológiai beavatkozás, hanem mély etikai szolgálat, ahol a tudományos precizitás a szenvedő ember iránti feltétlen felelősségvállalással párosul."}], ["c1-biomedical-discourse"]),
                mc("grammar", "check", "Melyik megállapítás fejezi ki legpontosabban Németh orvosetikai örökségét?", [
                    "A tudomány valódi értéke a kiszolgáltatott ember iránti odaadásban és a megalkuvás nélküli minőségben rejlik.",
                    "Az orvosnak semmilyen felelőssége nincs a páciens felé.",
                    "A gépek képesek teljesen felváltani az orvosi empátiát."
                ], 0, ["c1-biomedical-discourse"])
            ]
        }
    ]

    for l in core_lessons:
        emit_instructional_lesson(9, "core", l, core_title, core_intro if l["num"] == 1 else None)

    # Core Consolidation
    emit_consolidation_lesson(
        9,
        "core",
        "c1-09-consolidation",
        core_title,
        [
            "I can manipulate multi-tiered past counterfactual syntax (ha... volna, elkerülhető lett volna).",
            "I can calibrate deontic moral duty versus epistemic probability in bioethics.",
            "I can frame intractable moral dilemmas and synthesize Németh László's quality revolution."
        ],
        [
            mc("grammar", "recognize", "Melyik szerkezet fejez ki múltbeli elmaradt etikai kötelezettséget?", [
                "kötelessége lett volna megtenni",
                "biztosan meg fogja tenni",
                "talán megteszi ma"
            ], 0, ["c1-counterfactual-syntax"]),
            mc("grammar", "recognize", "Mit jelent a 'tájékozott beleegyezés' elve?", [
                "A beteg önrendelkező jogát a kockázatok teljes megismerésén alapuló döntésre.",
                "A kezelés kötelező végrehajtását tiltakozás ellenére is.",
                "Az orvos felmentését minden felelősség alól."
            ], 0, ["c1-deontic-epistemic-distinction"]),
            match("vocabulary", "recognize", [["elkerülhető lett volna", "would have been avoidable"], ["tájékozott beleegyezés", "informed consent"], ["morális csapdahelyzet", "moral trap"], ["palliatív ellátás", "palliative care"], ["orvosi etosz", "healer's ethos"]], ["c1-09-vocab"]),
            fb("vocabulary", "recall", "A bíróság megállapította, hogy a tragédia gondos eljárással _____ lett volna. (preventable / megelőzhető)", "megelőzhető", "The court established that the tragedy would have been preventable with careful procedure.", ["c1-09-vocab"]),
            fb("vocabulary", "recall", "A beteg emberi méltóságának sérthetetlensége a _____ ellátás legfőbb etikai alapköve. (palliative / palliatív)", "palliatív", "The inviolability of patient human dignity is the chief ethical cornerstone of palliative care.", ["c1-09-vocab"]),
            fb("grammar", "recall", "Ha a döntéshozók körültekintőbbek lettek volna, a mulasztás elkerülhető _____ volna. (would have been / lett)", "lett", "If decision-makers had been more circumspect the omission would have been avoidable.", ["c1-counterfactual-syntax"]),
            fb("grammar", "context", "Az orvos részéről az adott helyzetben elvárható gondosság elmulasztása súlyos műhibának _____ meg. (qualifies / felel / minősül)", "minősül", "Failure to provide due care expected of the doctor in the given situation qualifies as severe malpractice.", ["c1-deontic-epistemic-distinction"]),
            fb("grammar", "context", "Németh László szerint az orvos nem válhat biológiai technikussá; a teljes ember _____ gondozója. (holistic / holisztikus)", "holisztikus", "According to László Németh the doctor cannot become a biological technician; he is the holistic caretaker of the whole person.", ["c1-biomedical-discourse"]),
            mc("grammar", "context", "Melyik állítás fogalmazza meg helyesen a bioetikai dilemmák természetét?", [
                "Erőforrás-szűkösség idején a döntéshozó gyakran kényszerül két rossz közül a kisebbik választására.",
                "A kórházakban soha nincsenek nehéz döntések.",
                "A technológia minden etikai kérdést automatikusan megold."
            ], 0, ["c1-ethical-quandaries"]),
            sb("grammar", "produce", ["A", "beteg", "önrendelkezési", "joga", "minden", "orvosi", "beavatkozás", "elidegeníthetetlen", "feltétele."], ["A", "beteg", "önrendelkezési", "joga", "minden", "orvosi", "beavatkozás", "elidegeníthetetlen", "feltétele."], "Patient self-determination is the inalienable condition of every medical intervention.", ["c1-patient-autonomy"]),
            sw("production", [{"prompt": "Draft a retrospective ethical critique of a clinical trial failure.", "answer": "Amennyiben a klinika maradéktalanul betartotta volna a tájékoztatási kötelezettséget, elkerülhető lett volna a páciensek jogainak súlyos sérelme."}], ["c1-counterfactual-syntax"]),
            sw("production", [{"prompt": "Synthesize the core message of Németh László's 'A minőség forradalma'.", "answer": "A gyógyítás nem csupán technológiai beavatkozás, hanem a legmagasabb rendű etikai és emberi felelősségvállalás a másik ember méltóságáért."}], ["c1-biomedical-discourse"])
        ]
    )

    # ----------------------------------------------------
    # TRACK 2: DISCOURSE (c1-bioetika)
    # ----------------------------------------------------
    slug = "bioetika"
    disc_intro = [
        "Biomedical advances—from gene editing and embryology to organ allocation and end-of-life decisions—confront society with profound philosophical dilemmas. In Hungary, these debates involve medicine, theology, constitutional law, and human rights advocacy.",
        "In this unit, you will analyze contemporary bioethical discourse: genomic manipulation and CRISPR ethics, organ transplantation allocation criteria, human embryonic research, the constitutional battle over dignified death (the Dániel Karsai case), and artificial intelligence in medical diagnostics."
    ]

    disc_lessons = [
        {
            "num": 1,
            "stem": f"c1-{slug}-01",
            "title": "CRISPR, Gene Editing and Genomic Sovereignty",
            "grammar_title": "Biotechnology Ethics: Germline Modification and Human Dignity",
            "grammar_skill": "c1-biomedical-discourse",
            "goals": [
                "I can analyze ethical controversies surrounding CRISPR and human genome editing.",
                "I can evaluate the distinction between somatic gene therapy and germline genetic modification (*csíravonal-módosítás*).",
                "I can debate the boundaries between therapeutic correction and genetic enhancement (*eugenika*)."
            ],
            "vocab": [
                {"lemma": "génszerkesztés", "translation": "gene editing", "pos": "noun"},
                {"lemma": "csíravonal-módosítás", "translation": "germline genetic modification", "pos": "noun"},
                {"lemma": "szomatikus sejtterápia", "translation": "somatic cell therapy", "pos": "noun"},
                {"lemma": "örökíthető", "translation": "heritable, transmissible", "pos": "adjective"},
                {"lemma": "eugenika", "translation": "eugenics", "pos": "noun"},
                {"lemma": "genetikai javítás", "translation": "genetic enhancement", "pos": "noun"},
                {"lemma": "bioetikai konszenzus", "translation": "bioethical consensus", "pos": "noun"},
                {"lemma": "genom", "translation": "genome", "pos": "noun"}
            ],
            "gr_text1": "The advent of CRISPR-Cas9 revolutionized biotechnology, making targeted genomic alteration routine. Bioethical demarcation distinguishes *szomatikus génterápia* (treating a living patient's disease) from *csíravonal-módosítás* (altering reproductive cells).",
            "gr_text2": "Germline alteration produces heritable changes (*örökíthető genetikai módosítás*), raising grave risks of neo-eugenics (*új eugenika*) and violating the Oviedo Convention on Human Rights and Biomedicine.",
            "gr_table": [
                ["A szomatikus génterápia és a csíravonal-módosítás etikai elhatárolása...", "Ethical demarcation of somatic gene therapy and germline modification..."],
                ["Az örökíthető beavatkozások tilalma az oviedói egyezményben...", "Prohibition of heritable interventions in the Oviedo Convention..."],
                ["Gyógyítás vagy dizájnerbébik: a genetikai javítás határai...", "Healing or designer babies: the boundaries of genetic enhancement..."]
            ],
            "world_story_seg": {
                "seg_slug": "genszerkesztes",
                "title": "A genom határai és a Prométheuszi kísértés",
                "summary": "How CRISPR technology placed the ultimate genetic power in human hands and ignited international ethical debates.",
                "paragraphs": [
                    {"type": "narration", "text": "Amikor a molekuláris biológusok felfedezték a CRISPR-Cas9 génszerkesztési eljárást, az emberiség átlépte a biológiai evolúció Rubiconját. Ami korábban a természet vagy a sors kifürkészhetetlen játéka volt, az hirtelen szerkeszthető szöveggé vált. A gyógyíthatatlan genetikai betegségek – a cisztás fibrózistól a vérzékenységig – felszámolásának ígérete felcsillantotta az orvoslás régóta várt megváltását."},
                    {"type": "narration", "text": "A technológia azonban Prométheuszi dilemmát rejt magában. A nemzetközi bioetikai közösség szigorú határvonalat húzott a szomatikus gyógyítás és az emberi embriók örökíthető genetikai módosítása közé. Ha megengedjük az emberi faj tervszerű genetikai átalakítását, nemcsak beláthatatlan ökológiai és evolúciós kockázatot vállalunk, hanem megnyitjuk az utat egy új, biológiai kasztrendszer és a géntechnológiai eugenika előtt."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Miért tiltja a nemzetközi bioetika a csíravonal-módosítást?", ["Mert az átalakítások örökölhetők, így a jövő nemzedékek teljes genetikai állományát visszafordíthatatlanul megváltoztatják.", "Mert a technológia túl olcsó.", "Mert nincsenek laboratóriumok a világon."], 0, ["c1-bioetika-vocab"]),
                fb("grammar", "controlled", "A nemzetközi egyezmények szigorúan tiltják az _____ emberi génmódosítások klinikai alkalmazását. (heritable / örökíthető)", "örökíthető", "International conventions strictly prohibit the clinical application of heritable human genetic modifications.", ["c1-biomedical-discourse"]),
                match("vocabulary", "controlled", [["génszerkesztés", "gene editing"], ["csíravonal-módosítás", "germline modification"], ["örökíthető", "heritable"], ["eugenika", "eugenics"]], ["c1-bioetika-vocab"]),
                sb("grammar", "practice", ["A", "genetikai", "gyógyítás", "nem", "csúszhat", "át", "a", "társadalmi", "eugenikába."], ["A", "genetikai", "gyógyítás", "nem", "csúszhat", "át", "a", "társadalmi", "eugenikába."], "Genetic therapy must not slide over into societal eugenics.", ["c1-biomedical-discourse"]),
                sw("production", [{"prompt": "Contrast somatic gene therapy with germline modification.", "answer": "Míg a szomatikus génterápia kizárólag az egyén testi sejtjeit kezeli anélkül, hogy utódaira átterjedne, addig a csíravonal-módosítás a jövőbeli nemzedékek örökítőanyagát alakítja át."}], ["c1-biomedical-discourse"]),
                mc("grammar", "check", "Melyik egyezmény rögzíti az európai bioetika alapelveit?", [
                    "Az oviedói egyezmény az emberi jogokról és a biomedicináról.",
                    "A genfi békeszerződés a hadifoglyokról.",
                    "A római szerződés a közös vámokról."
                ], 0, ["c1-biomedical-discourse"])
            ]
        },
        {
            "num": 2,
            "stem": f"c1-{slug}-02",
            "title": "Organ Transplantation, Brain Death and Allocation Justice",
            "grammar_title": "Transplant Ethics: Distributive Justice and Presumed Consent",
            "grammar_skill": "c1-biomedical-discourse",
            "goals": [
                "I can analyze the legal concept of presumed consent in organ donation (*feltételezett beleegyezés*).",
                "I can evaluate philosophical definitions of brain death (*agyhalál*).",
                "I can debate distributive justice algorithms in donor organ allocation (Eurotransplant)."
            ],
            "vocab": [
                {"lemma": "szervátültetés", "translation": "organ transplantation", "pos": "noun"},
                {"lemma": "feltételezett beleegyezés", "translation": "presumed consent (opt-out donation)", "pos": "noun"},
                {"lemma": "agyhalál", "translation": "brain death", "pos": "noun"},
                {"lemma": "Eurotransplant", "translation": "Eurotransplant international allocation foundation", "pos": "noun"},
                {"lemma": "elosztási igazságosság", "translation": "distributive justice", "pos": "noun"},
                {"lemma": "várólista", "translation": "waiting list", "pos": "noun"},
                {"lemma": "kompatibilitás", "translation": "histocompatibility, biological match", "pos": "noun"},
                {"lemma": "élődonoros transzplantáció", "translation": "living donor transplantation", "pos": "noun"}
            ],
            "gr_text1": "Hungary operates under the legal principle of *feltételezett beleegyezés* (presumed consent / opt-out): every deceased person whose brain death is certified (*agyhalál*) is considered an organ donor unless they registered an explicit objection in life.",
            "gr_text2": "Allocating scarce organs through *Eurotransplant* balances biological compatibility (*szöveti egyezés*), medical urgency, and pediatric priority, strictly excluding wealth or social status from the algorithmic equation.",
            "gr_table": [
                ["A feltételezett beleegyezés elve a magyar transzplantációs jogban...", "The principle of presumed consent in Hungarian transplantation law..."],
                ["Az agyhalál beálltának szigorú orvosi és jogi kritériumai...", "Strict medical and legal criteria for certification of brain death..."],
                ["Disztributív igazságosság az Eurotransplant várólistáin...", "Distributive justice on Eurotransplant waiting lists..."]
            ],
            "world_story_seg": {
                "seg_slug": "transzplantacio",
                "title": "A szívverésen túl: az agyhalál és az élet ajándéka",
                "summary": "How organ transplantation transformed the philosophical meaning of death and created an international framework of altruistic solidarity.",
                "paragraphs": [
                    {"type": "narration", "text": "Az orvostudomány történetében kevés pillanat alakította át annyira a halálról vallott fogalmainkat, mint a szervátültetés megjelenése. Az agyhalál koncepciójának elfogadása – annak felismerése, hogy a teljes agyműködés visszafordíthatatlan leállása jelenti a biológiai személyiség végét, még ha a keringést gépek fenn is tartják – lehetővé tette, hogy egy ember tragédiája mások számára az élet megújulását hozza el."},
                    {"type": "narration", "text": "Magyarország 2013-ban csatlakozott az Eurotransplant hálózatához, amely nyolc európai ország donorjait és recipienseit köti össze. Az algoritmusok által vezérelt szervelosztás az orvosi igazságosság mintapéldája: a vér szerinti és szöveti kompatibilitás, a várakozási idő és a sürgősség az egyetlen megengedett szempont. A rendszer kizár minden vagyoni vagy társadalmi előnyt, megvalósítva az orvosi etika legszebb ígéretét: az élet egyenlő értékét."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Mit jelent a 'feltételezett beleegyezés' elve a magyar donációs jogban?", ["Az elhunyt donornak tekintendő, hacsak életében nem tett írásbeli tiltakozó nyilatkozatot.", "A családtagoknak kell árverésen megvenniük a szerveket.", "Kizárólag önkéntes véradók kaphatnak szervet."], 0, ["c1-bioetika-vocab"]),
                fb("grammar", "controlled", "A donor szervek elosztásánál a szöveti _____ és a klinikai sürgősség az elsődleges szempont. (compatibility / kompatibilitás)", "kompatibilitás", "In allocating donor organs tissue compatibility and clinical urgency are primary considerations.", ["c1-biomedical-discourse"]),
                match("vocabulary", "controlled", [["szervátültetés", "organ transplantation"], ["feltételezett beleegyezés", "presumed consent"], ["agyhalál", "brain death"], ["várólista", "waiting list"]], ["c1-bioetika-vocab"]),
                sb("grammar", "practice", ["A", "szervelosztás", "rendszere", "kizár", "minden", "társadalmi", "és", "vagyoni", "diszkriminációt."], ["A", "szervelosztás", "rendszere", "kizár", "minden", "társadalmi", "és", "vagyoni", "diszkriminációt."], "The organ allocation system excludes all social and wealth discrimination.", ["c1-biomedical-discourse"]),
                sw("production", [{"prompt": "Explain how Eurotransplant ensures distributive justice in organ allocation.", "answer": "Az Eurotransplant objektív orvosi kritériumok – kompatibilitás, sürgősség és várakozási idő – alapján osztja szét a szerveket, garantálva a pártatlan és méltányos eljárást."}], ["c1-biomedical-discourse"]),
                mc("grammar", "check", "Mi képezi a donáció orvosi és jogi előfeltételét elhunyt donornál?", [
                    "Az agyhalál független orvosi bizottság általi kétséget kizáró megállapítása.",
                    "A szívverés átmeneti lassulása.",
                    "A beteg életkorának betöltése."
                ], 0, ["c1-biomedical-discourse"])
            ]
        },
        {
            "num": 3,
            "stem": f"c1-{slug}-03",
            "title": "Embryo Research, In Vitro Fertilization and Stem Cells",
            "grammar_title": "The Status of the Embryo: Dignity, Potentiality and Science",
            "grammar_skill": "c1-biomedical-discourse",
            "goals": [
                "I can analyze ethical perspectives on the moral status of the human embryo (*embrió erkölcsi státusza*).",
                "I can evaluate IVF regulations (*mesterséges megtermékenyítés*) and surplus embryo preservation.",
                "I can formulate nuanced arguments on pluripotent stem cell research."
            ],
            "vocab": [
                {"lemma": "embriókutatás", "translation": "embryo research", "pos": "noun"},
                {"lemma": "őssejt", "translation": "stem cell", "pos": "noun"},
                {"lemma": "mesterséges megtermékenyítés", "translation": "in vitro fertilization (IVF)", "pos": "noun"},
                {"lemma": "fölösleges embrió", "translation": "surplus embryo", "pos": "noun"},
                {"lemma": "morális státusz", "translation": "moral status", "pos": "noun"},
                {"lemma": "potencialitás", "translation": "potentiality", "pos": "noun"},
                {"lemma": "fogantatás", "translation": "conception", "pos": "noun"},
                {"lemma": "pluripotens", "translation": "pluripotent", "pos": "adjective"}
            ],
            "gr_text1": "The moral status of the human embryo represents one of the deepest philosophical divides. The gradualist perspective (*gradualista megközelítés*) holds that moral status develops incrementally with gestational age.",
            "gr_text2": "Conversely, the potentiality argument (*potencialitási elmélet*), prominent in Christian personalism, holds that human dignity begins at conception (*fogantatás*), placing strict limits on destructive embryonic stem cell research.",
            "gr_table": [
                ["A fogantatástól kezdődő emberi méltóság teológiai és jogi érvei...", "Theological and legal arguments for dignity starting from conception..."],
                ["Pluripotens őssejtek alkalmazása a regeneratív medicinában...", "Application of pluripotent stem cells in regenerative medicine..."],
                ["A mesterséges megtermékenyítés során keletkező embriók sorsa...", "The fate of embryos generated during artificial fertilization..."]
            ],
            "world_story_seg": {
                "seg_slug": "embriokutatas",
                "title": "Az élet kezdete és az embrió méltósága",
                "summary": "The clash between scientific exploration in regenerative medicine and philosophical debates on the status of embryonic life.",
                "paragraphs": [
                    {"type": "narration", "text": "Mikor kezdődik az emberi élet? Ez a kérdés évszázadokon át a teológia és a metafizika felségterülete volt, ám a lombikbébi-programok és az őssejtkutatás térnyerésével húsbavágó bioetikai és jogi problémává vált. A mesterséges megtermékenyítés gyermekek százezreinek születését tette lehetővé meddő párok számára, miközben fagyasztókban tárolt embriók ezreinek etikai státuszáról nyitott vitát."},
                    {"type": "narration", "text": "A vitában két markáns filozófiai álláspont feszül egymásnak. Az egyik oldal szerint az embrió a fogantatás pillanatától fogva teljes jogú emberi lény, amelynek méltósága sérthetetlen, így elpusztítása még orvosi kutatás céljából sem megengedhető. A másik oldal a fokozatosság elvét vallja: az idegrendszer kifejlődése előtt álló korai sejthalmaz nem rendelkezik öntudattal, így a pluripotens őssejtek felhasználása súlyos betegségek gyógyítására erkölcsileg igazolható cél."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Miért képezi vita tárgyát az embrionális őssejtkutatás?", ["Mert az őssejtek kinyerése a korai emberi embrió elpusztításával jár.", "Mert az őssejtek nem gyógyítanak semmit.", "Mert a technológiát betiltották a Holdon."], 0, ["c1-bioetika-vocab"]),
                fb("grammar", "controlled", "A gradualista etikai álláspont szerint az embrió morális _____ az idegrendszer fejlődésével párhuzamosan növekszik. (status / státusza)", "státusza", "According to the gradualist ethical position the moral status of the embryo increases in parallel with nervous system development.", ["c1-biomedical-discourse"]),
                match("vocabulary", "controlled", [["őssejt", "stem cell"], ["mesterséges megtermékenyítés", "in vitro fertilization"], ["fogantatás", "conception"], ["potencialitás", "potentiality"]], ["c1-bioetika-vocab"]),
                sb("grammar", "practice", ["Az", "élet", "kezdete", "körüli", "vita", "mély", "filozófiai", "és", "jogi", "kérdés."], ["Az", "élet", "kezdete", "körüli", "vita", "mély", "filozófiai", "és", "jogi", "kérdés."], "The debate around the beginning of life is a profound philosophical and legal question.", ["c1-biomedical-discourse"]),
                sw("production", [{"prompt": "Summarize the clash between the gradualist and potentiality theories of embryonic status.", "answer": "A potencialitási elmélet szerint az emberi méltóság a fogantatás pillanatában kezdődik, míg a gradualista felfogás szerint a morális státusz fokozatosan, a biológiai komplexitással párhuzamosan fejlődik ki."}], ["c1-biomedical-discourse"]),
                mc("grammar", "check", "Melyik állítás világítja meg a lombikbébi-eljárások bioetikai feszültségét?", [
                    "A vágyott gyermek megszületése és a fel nem használt fagyasztott embriók sorsa közötti erkölcsi dilemma.",
                    "Hogy túl kevés orvos dolgozik a kórházban.",
                    "Hogy a lombikok üvegből készülnek."
                ], 0, ["c1-biomedical-discourse"])
            ]
        },
        {
            "num": 4,
            "stem": f"c1-{slug}-04",
            "title": "The Constitutional Battle for Dignified Death: The Dániel Karsai Case",
            "grammar_title": "Active Euthanasia, ALS, and Fundamental Human Rights",
            "grammar_skill": "c1-patient-autonomy",
            "goals": [
                "I can analyze the constitutional litigation surrounding Dániel Karsai and end-of-life autonomy in Hungary.",
                "I can evaluate European Court of Human Rights jurisprudence on assisted dying (Article 8 ECHR).",
                "I can discuss the public, ethical, and legislative repercussions of terminal disease activism."
            ],
            "vocab": [
                {"lemma": "asszisztált öngyilkosság", "translation": "assisted suicide / dying", "pos": "noun"},
                {"lemma": "aktív eutanázia", "translation": "active euthanasia", "pos": "noun"},
                {"lemma": "terminális stádium", "translation": "terminal stage", "pos": "noun"},
                {"lemma": "Emberi Jogok Európai Bírósága", "translation": "European Court of Human Rights (ECtHR)", "pos": "noun"},
                {"lemma": "magánélethez való jog", "translation": "right to private life (Art. 8)", "pos": "noun"},
                {"lemma": "önrendelkezés korlátai", "translation": "limits of self-determination", "pos": "noun"},
                {"lemma": "ALS-betegség", "translation": "ALS disease (amyotrophic lateral sclerosis)", "pos": "noun"},
                {"lemma": "társadalmi párbeszéd", "translation": "societal dialogue / discourse", "pos": "noun"}
            ],
            "gr_text1": "In 2023–2024, Hungarian constitutional lawyer Dr. Dániel Karsai, suffering from terminal ALS, ignited historic national discourse by taking his fight for assisted dying to the European Court of Human Rights and the Constitutional Court.",
            "gr_text2": "Karsai argued that criminalizing assistance to end one's life abroad deprives patients of the right to make the ultimate decision about their own bodily suffering, violating Article 8 of the European Convention.",
            "gr_table": [
                ["A méltóságteljes halálhoz való jog és a testi autonómia...", "The right to a dignified death and bodily autonomy..."],
                ["Karsai Dániel strasbourgi beadványa és az Alkotmánybíróság...", "Dániel Karsai's Strasbourg application and the Constitutional Court..."],
                ["Társadalmi tabuk ledöntése a terminális betegségekkel kapcsolatban...", "Breaking societal taboos regarding terminal illnesses..."]
            ],
            "world_story_seg": {
                "seg_slug": "karsaidaniel",
                "title": "Karsai Dániel és a méltóságteljes elmúlás harca",
                "summary": "How constitutional lawyer Dániel Karsai's personal tragedy and courage transformed the Hungarian debate on dignified death.",
                "paragraphs": [
                    {"type": "narration", "text": "2023 őszén egy bátor bejelentés rázta meg a magyar közéletet. Dr. Karsai Dániel, az elismert alkotmányjogász a nyilvánosság elé lépett, és feltárta, hogy gyógyíthatatlan amiotrófiás laterálszklerózisban (ALS) szenved. A betegség fokozatosan megfosztja az embert minden mozgási képességétől, a beszédtől és a nyeléstől, miközben az elme mindvégig kristálytiszta marad."},
                    {"type": "narration", "text": "Karsai nem a csendes visszahúzódást választotta, hanem jogi harcba szállt a méltóságteljes halálért a strasbourgi Emberi Jogok Európai Bíróságán és a hazai Alkotmánybíróságon. Azzal érvelt, hogy az államnak nincs joga arra kényszeríteni a polgárát, hogy elviselhetetlen, emberhez méltatlan testi szenvedésben élje le élete utolsó heteit. Bár a hatályos törvények nem változtak meg azonnal, küzdelmével példátlan társadalmi empátiát ébresztett, és ledöntötte az elmúlás körüli évszázados tabukat."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Milyen jogi kérdést emelt a nyilvánosság elé Dr. Karsai Dániel?", ["A gyógyíthatatlan betegek méltóságteljes halálhoz és önrendelkezéshez való jogát.", "Az autópályadíjak csökkentését.", "A választójogi korhatár felemelését."], 0, ["c1-bioetika-vocab"]),
                fb("grammar", "controlled", "Karsai beadványa a strasbourgi bíróság előtt a magánélet tiszteletben tartásához és az emberi _____ való jogra épült. (to dignity / méltósághoz)", "méltósághoz", "Karsai's application before the Strasbourg court was built upon the right to respect for private life and human dignity.", ["c1-patient-autonomy"]),
                match("vocabulary", "controlled", [["aktív eutanázia", "active euthanasia"], ["terminális stádium", "terminal stage"], ["ALS-betegség", "ALS disease"], ["társadalmi párbeszéd", "societal dialogue"]], ["c1-bioetika-vocab"]),
                sb("grammar", "practice", ["A", "méltóságteljes", "elmúlás", "kérdése", "az", "egyéni", "szabadság", "végső", "határa."], ["A", "méltóságteljes", "elmúlás", "kérdése", "az", "egyéni", "szabadság", "végső", "határa."], "The question of dignified dying is the ultimate boundary of individual liberty.", ["c1-patient-autonomy"]),
                sw("production", [{"prompt": "Analyze the impact of Dániel Karsai's legal fight on Hungarian public discourse.", "answer": "Karsai Dániel bátorsága emberközelivé tette az eutanázia elvont fogalmát, kényszerítve a társadalmat és a jogászokat arra, hogy szembenézzenek az emberi autonómia és a szenvedés határainak kérdésével."}], ["c1-patient-autonomy"]),
                mc("grammar", "check", "Miért tekinthető történelmi jelentőségűnek a Karsai-ügy?", [
                    "Mert alkotmányjogi szintre emelte a méltóságteljes elmúlásról szóló vitát Magyarországon.",
                    "Mert megszüntette az összes orvosi egyetemet.",
                    "Mert elfelejtődött néhány nap alatt."
                ], 0, ["c1-patient-autonomy"])
            ]
        },
        {
            "num": 5,
            "stem": f"c1-{slug}-05",
            "title": "Artificial Intelligence in Diagnostics and the Healer's Role",
            "grammar_title": "Algorithmic Medicine: Accountability, Bias and Compassion",
            "grammar_skill": "c1-biomedical-discourse",
            "goals": [
                "I can evaluate artificial intelligence in radiological and pathological diagnostics.",
                "I can analyze medical malpractice liability when algorithmic systems err (*felelősség megoszlása*).",
                "I can debate whether automated diagnostics can ever supplant empathetic bedside communication."
            ],
            "vocab": [
                {"lemma": "algoritmikus diagnosztika", "translation": "algorithmic diagnostics", "pos": "noun"},
                {"lemma": "orvosi műhiba", "translation": "medical malpractice", "pos": "noun"},
                {"lemma": "kórszövettan", "translation": "histopathology", "pos": "noun"},
                {"lemma": "képalkotó diagnosztika", "translation": "imaging diagnostics / radiology", "pos": "noun"},
                {"lemma": "felelősség megoszlása", "translation": "distribution of liability", "pos": "noun"},
                {"lemma": "orvos-beteg bizalom", "translation": "doctor-patient trust", "pos": "noun"},
                {"lemma": "empátia", "translation": "empathy", "pos": "noun"},
                {"lemma": "algoritmikus torzítás", "translation": "algorithmic bias", "pos": "noun"}
            ],
            "gr_text1": "AI systems match or exceed human radiologists in detecting melanomas, mammograms, and CT abnormalities. However, algorithmic medicine creates complex legal quandaries: who is liable when an AI diagnostic system misdiagnoses a malignancy?",
            "gr_text2": "Crucially, bioethics insists that diagnosis is only the cognitive half of healing; true medical care requires *empátia* and communicating existential truths with compassion, something no neural network can possess.",
            "gr_table": [
                ["A gépi tanulás forradalma a radiológiai képalkotásban...", "The machine learning revolution in radiological imaging..."],
                ["A polgári jogi felelősség megoszlása szoftverhiba esetén...", "Distribution of civil liability in case of software error..."],
                ["Az orvos-beteg bizalom megőrzése a gépesített egészségügyben...", "Preserving doctor-patient trust in automated healthcare..."]
            ],
            "world_story_seg": {
                "seg_slug": "mestersegesintelligencia",
                "title": "A diagnosztizáló algoritmus és a gyógyító tekintet",
                "summary": "How artificial intelligence transforms medical detection while reaffirming that human empathy remains irreplaceable.",
                "paragraphs": [
                    {"type": "narration", "text": "A modern kórházak folyosóin csendes forradalom zajlik. A mesterséges intelligencia neurális hálói másodpercek töredéke alatt képesek áttekinteni ezer meg ezer CT- és MRI-felvételt, észrevéve a legapróbb daganatos elváltozásokat is, amelyek felett a fáradt emberi szem könnyen átsiklana. A diagnosztika sebessége és pontossága ugrásszerűen megnőtt."},
                    {"type": "narration", "text": "De vajon kié a felelősség, ha a gép téved? És ki mondja el a betegnek, hogy a kór gyógyíthatatlan? A legmélyebb bioetikai tanulság az, hogy a gyógyítás nem pusztán információfeldolgozás, hanem emberi találkozás. Az algoritmus képes felállítani a diagnózist, de nem tudja megfogni a rémült beteg kezét, és nem képes reményt adni ott, ahol a technológia kudarcot vall. A jövő orvosa a géppel együtt dolgozik, de szívvel gyógyít."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Milyen jogi problémát vet fel az AI alkalmazása a diagnosztikában?", ["A kártérítési felelősség megoszlását a szoftverfejlesztő és a kezelőorvos között tévedés esetén.", "Hogy a monitorok fénye túl erős.", "Hogy a robotok nem akarnak kávézni."], 0, ["c1-bioetika-vocab"]),
                fb("grammar", "controlled", "A technológia elterjedése ellenére az orvos-beteg _____ megőrzése a gyógyítás legfőbb záloga. (trust / bizalom)", "bizalom", "Despite the spread of technology preserving doctor-patient trust is the chief pledge of healing.", ["c1-biomedical-discourse"]),
                match("vocabulary", "controlled", [["algoritmikus diagnosztika", "algorithmic diagnostics"], ["orvosi műhiba", "medical malpractice"], ["orvos-beteg bizalom", "doctor-patient trust"], ["empátia", "empathy"]], ["c1-bioetika-vocab"]),
                sb("grammar", "practice", ["A", "technológia", "segítheti", "a", "gyógyítást,", "de", "nem", "helyettesítheti", "az", "embert."], ["A", "technológia", "segítheti", "a", "gyógyítást,", "de", "nem", "helyettesítheti", "az", "embert."], "Technology can assist healing, but cannot replace the human being.", ["c1-biomedical-discourse"]),
                sw("production", [{"prompt": "Reflect on why human empathy remains irreplaceable in automated medicine.", "answer": "Bár az algoritmusok páratlan pontossággal elemeznek adatokat, a gyógyítás etikai és lelki dimenziója – a vigasz, a remény és az emberi jelenlét – kizárólag az emberi empátián alapulhat."}], ["c1-biomedical-discourse"]),
                mc("grammar", "check", "Milyen szerep hárul a jövő orvosára a mesterséges intelligencia korában?", [
                    "A technológiai adatok értő, empátiával és etikai felelősséggel kísért emberi közvetítése a beteg felé.",
                    "A gyógyítás teljes elhagyása a robotok javára.",
                    "A gépek kikapcsolása és a kézi feljegyzésekhez való visszatérés."
                ], 0, ["c1-biomedical-discourse"])
            ]
        }
    ]

    for l in disc_lessons:
        emit_instructional_lesson(9, "discourse", l, disc_title, disc_intro if l["num"] == 1 else None)

    # Combined world story
    write_json(
        f"stories/world/c1/{slug}.json",
        {
            "id": f"story.c1.world.{slug}",
            "title": "A bioetika, az orvosi etosz és a technológia horizontja",
            "level": "C1",
            "type": "world",
            "summary": "Comprehensive chronicle of modern bioethical dilemmas: from CRISPR gene editing and embryonic stem cell research through organ donation ethics, Dániel Karsai's constitutional battle for dignified death, to artificial intelligence diagnostics.",
            "paragraphs": [
                {"type": "narration", "text": "A biomedicinális tudományok huszonegyedik századi robbanásszerű fejlődése olyan szédítő etikai és filozófiai kihívások elé állította az emberiséget, amelyek korábban csak a tudományos-fantasztikus irodalomban léteztek."},
                {"type": "narration", "text": "A CRISPR génszerkesztés megnyitotta az utat az emberi genom közvetlen átírása felé, kikényszerítve a szigorú nemzetközi határvonalat a gyógyítás és a veszélyes eugenikai kísértések között."},
                {"type": "narration", "text": "A szervátültetésben a feltételezett beleegyezés elve és az Eurotransplant pártatlan algoritmusai az elosztási igazságosság legszebb példáját valósították meg, míg az embriókutatás az élet kezdetének titkát vizsgálja."},
                {"type": "narration", "text": "Dr. Karsai Dániel történelmi jogi küzdelme megrendítő erővel helyezte a középpontba a méltóságteljes elmúlás és a beteg önrendelkezési jogának szent sérthetetlenségét."},
                {"type": "narration", "text": "Mindez a mesterséges intelligencia korában arra a végső Németh László-i tanulságra emlékeztet, hogy a technológia puszta eszköz: a gyógyítás igazi forrása az orvosi etosz, a részvét és a másik ember méltósága iránti feltétlen felelősségvállalás."}
            ]
        }
    )

    # Discourse Consolidation
    emit_consolidation_lesson(
        9,
        "discourse",
        f"c1-{slug}-consolidation",
        disc_title,
        [
            "I can analyze biotechnology dilemmas (CRISPR gene editing, embryonic stem cells, Eurotransplant).",
            "I can evaluate constitutional litigation on patient autonomy, end-of-life decisions, and the Karsai case.",
            "I can articulate ethical positions on algorithmic medicine, medical malpractice, and human empathy."
        ],
        [
            mc("grammar", "recognize", "Miért tiltja a bioetika az emberi csíravonal-módosítást?", [
                "Mert a változtatások örökölhetők, beláthatatlan evolúciós és etikai kockázatot teremtve.",
                "Mert senki nem tudja, hogyan kell csinálni.",
                "Mert a gének nem játszanak szerepet az öröklődésben."
            ], 0, ["c1-biomedical-discourse"]),
            mc("grammar", "recognize", "Milyen elven alapul a magyar donációs jogszabály?", [
                "A feltételezett beleegyezés elvén (opt-out rendszer).",
                "Kizárólag a fizetett szervvásárláson.",
                "A sorsolásos szervadományozáson."
            ], 0, ["c1-biomedical-discourse"]),
            match("vocabulary", "recognize", [["génszerkesztés", "gene editing"], ["feltételezett beleegyezés", "presumed consent"], ["őssejt", "stem cell"], ["aktív eutanázia", "active euthanasia"], ["algoritmikus diagnosztika", "algorithmic diagnostics"]], ["c1-bioetika-vocab"]),
            fb("vocabulary", "recall", "A transzplantáció előfeltétele az _____ független orvosok általi kétséget kizáró megállapítása. (brain death / agyhalál)", "agyhalál", "The precondition of transplantation is the certification of brain death beyond doubt by independent doctors.", ["c1-bioetika-vocab"]),
            fb("vocabulary", "recall", "A méltóságteljes halálhoz való jog küzdelmében Karsai Dániel az emberi _____ sérthetetlenségére hivatkozott. (dignity / méltóság)", "méltóság", "In the fight for the right to dignified death Dániel Karsai cited the inviolability of human dignity.", ["c1-bioetika-vocab"]),
            fb("grammar", "recall", "A kezelőorvos nem hajthat végre beavatkozást a páciens tájékozott _____ hiányában. (consent / beleegyezése)", "beleegyezése", "The treating doctor cannot carry out interventions in the absence of the patient's informed consent.", ["c1-patient-autonomy"]),
            fb("grammar", "context", "A gépi tanulás nem pótolhatja az orvos és beteg közötti mély empátiát és kölcsönös _____. (trust / bizalmat)", "bizalmat", "Machine learning cannot replace deep empathy and mutual trust between doctor and patient.", ["c1-biomedical-discourse"]),
            fb("grammar", "context", "Erőforrás-szűkösség esetén a triage kényszere feloldhatatlan morális _____ teremt. (dilemma / dilemmát)", "dilemmát", "In case of resource scarcity the duress of triage creates an insoluble moral dilemma.", ["c1-biomedical-discourse"]),
            mc("grammar", "context", "Melyik állítás foglalja össze legméltóbban az orvosi etika alapkövét?", [
                "A beteg ember méltóságának és önrendelkezésének tiszteletben tartása minden technológiai siker felett áll.",
                "A technológia tökéletes, és nincs szükség emberi orvosokra.",
                "Az orvostudománynak semmilyen erkölcsi határa nem lehet."
            ], 0, ["c1-biomedical-discourse"]),
            sb("grammar", "produce", ["A", "gyógyítás", "igazi", "nagysága", "az", "emberi", "részvétben", "és", "a", "méltóságban", "rejlik."], ["A", "gyógyítás", "igazi", "nagysága", "az", "emberi", "részvétben", "és", "a", "méltóságban", "rejlik."], "The true greatness of healing lies in human compassion and dignity.", ["c1-biomedical-discourse"]),
            sw("production", [{"prompt": "Write a critical evaluation of Dániel Karsai's constitutional legacy.", "answer": "Karsai Dániel fellépése felrázta a társadalom lelkiismeretét, bebizonyítva, hogy az emberi méltóság védelme az elmúlás legnehezebb pillanataiban is a jogállam alapvető kötelezettsége."}], ["c1-patient-autonomy"]),
            sw("production", [{"prompt": "Formulate a concluding thought on the future of biotechnology and human ethics.", "answer": "Amíg a tudományos géntechnológiai vívmányokat szilárd etikai fékek és az emberi méltóság védelme vezérli, addig a technológia az élet szolgálója marad, nem pedig zsarnoka."}], ["c1-biomedical-discourse"])
        ]
    )
    print("=== Finished C1 Unit 9 ===")


if __name__ == "__main__":
    generate_unit_9()
