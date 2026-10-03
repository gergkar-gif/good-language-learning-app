#!/usr/bin/env python3
"""
Hungarian C1 Block 3 - Unit 15 Generator:
  - Track 1 (Core): Unit 15 — "Artificial Intelligence, Cognitive Systems & Algorithmic Reason" (c1-15)
  - Track 2 (Discourse): Unit 15 — "AI Ethics, Neural Networks & Technological Sovereignty" (c1-mestersegesintelligencia)
"""

import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT))

from scripts.c1_block1.common import mc, match, fb, sb, dc, sw, write_json, emit_instructional_lesson, emit_consolidation_lesson
from scripts.c1_block3.registry_helper import register_unit


def generate_unit_15():
    print("=== Generating C1 Unit 15 ===")
    
    # Register skills & titles
    new_skills = {
        "c1-15-vocab": {"kind": "vocabulary"},
        "c1-mestersegesintelligencia-vocab": {"kind": "vocabulary"},
        "c1-restrictive-exceptive-adverbials": {"kind": "grammar"},
        "c1-hypothetical-counterfactual-participles": {"kind": "grammar"},
        "c1-complex-proportional-correlatives": {"kind": "grammar"},
        "c1-modal-probabilistic-modifiers": {"kind": "grammar"},
        "c1-adv-nominal-appositive-structures": {"kind": "grammar"},
        "c1-discourse-limiting-particles": {"kind": "grammar"},
        "c1-correlative-causal-adverbials": {"kind": "grammar"},
        "c1-assertive-evidential-markers": {"kind": "grammar"},
        "c1-subjunctive-deliberative-optatives": {"kind": "grammar"},
        "c1-adv-contrastive-focus-inversion": {"kind": "grammar"},
    }
    new_titles = {
        "c1-15-vocab": "reading",
        "c1-mestersegesintelligencia-vocab": "reading",
        "c1-restrictive-exceptive-adverbials": "restrictive and exceptive adverbial clauses expressing conditions or exclusions",
        "c1-hypothetical-counterfactual-participles": "hypothetical and counterfactual adverbial participles in analytical prose",
        "c1-complex-proportional-correlatives": "proportional and comparative correlative sentence structures",
        "c1-modal-probabilistic-modifiers": "epistemic probability modifiers and tentative assertion adverbials",
        "c1-adv-nominal-appositive-structures": "complex appositive noun phrases with clarifying discourse markers",
        "c1-discourse-limiting-particles": "delimiting and focalizing discourse particles in academic debate",
        "c1-correlative-causal-adverbials": "correlative causal adverbials and antecedent consequence argumentation",
        "c1-assertive-evidential-markers": "assertive evidential markers and epistemic certainty expressions",
        "c1-subjunctive-deliberative-optatives": "deliberative and optative subjunctive structures in theoretical evaluation",
        "c1-adv-contrastive-focus-inversion": "contrastive focus syntactic inversion and emphatic word order",
    }
    
    core_title = "Artificial Intelligence, Cognitive Systems & Algorithmic Reason"
    core_stems = [f"c1-15-0{i}" for i in range(1, 6)] + ["c1-15-consolidation"]
    disc_title = "AI Ethics, Neural Networks & Technological Sovereignty"
    disc_stems = [f"c1-mestersegesintelligencia-0{i}" for i in range(1, 6)] + ["c1-mestersegesintelligencia-consolidation"]
    
    register_unit(15, core_title, core_stems, disc_title, disc_stems, new_skills, new_titles)

    # ----------------------------------------------------
    # TRACK 1: CORE (c1-15)
    # ----------------------------------------------------
    core_intro = [
        "In contemporary technology and epistemology, artificial intelligence demands precision in expressing probabilistic reasoning, restrictive qualifications, and cognitive modeling.",
        "In this unit, honoring John von Neumann's monumental foundational work in cybernetics and computational architecture ('The Computer and the Brain'), you will master analytical syntax for machine learning, neural architectures, automated decision systems, and cognitive philosophy at the C1 level."
    ]

    core_lessons = [
        {
            "num": 1,
            "stem": "c1-15-01",
            "title": "Machine Learning Foundations & Algorithmic Logic",
            "grammar_title": "Restrictive and Exceptive Clauses in Algorithmic Logic",
            "grammar_skill": "c1-restrictive-exceptive-adverbials",
            "goals": [
                "I can analyze machine learning fundamentals and loss optimization (*tanító adathalmaz, gradiens-csökkentés, veszteségfüggvény*).",
                "I can construct restrictive and exceptive adverbial clauses (*kivéve ha, mindössze annyiban, pusztán arra szorítkozva*).",
                "I can evaluate statistical overfitting (*túlilleszkedés*) and model convergence in academic Hungarian."
            ],
            "vocab": [
                {"lemma": "gépi tanulás", "translation": "machine learning", "pos": "noun"},
                {"lemma": "algoritmus", "translation": "algorithm", "pos": "noun"},
                {"lemma": "tanító adathalmaz", "translation": "training dataset", "pos": "noun"},
                {"lemma": "túlilleszkedés", "translation": "overfitting", "pos": "noun"},
                {"lemma": "veszteségfüggvény", "translation": "loss function", "pos": "noun"},
                {"lemma": "gradiens-csökkentés", "translation": "gradient descent", "pos": "noun"},
                {"lemma": "konvergencia", "translation": "convergence", "pos": "noun"},
                {"lemma": "regularizáció", "translation": "regularization", "pos": "noun"}
            ],
            "gr_text1": "Restrictive and exceptive clauses qualify conditions or exclusions with mathematical precision using connectors like `kivéve ha` (except if), `mindössze annyiban, hogy` (merely to the extent that), `pusztán annyit jelentve` (meaning merely that), and `eltekintve attól, hogy` (disregarding that): `A modell megbízható predikciókat tesz, kivéve ha az adathalmaz eloszlása alapjaiban tér el a tanító mintától`.",
            "gr_text2": "In algorithmic analysis, restrictive particles (*mindössze, csupán, pusztán*) establish precise operational boundaries, preventing unwarranted generalizations.",
            "gr_table": [
                ["A modell stabil marad, kivéve ha váratlan zaj terheli a bemeneti adatokat.", "The model remains stable, except if unexpected noise burdens input data."],
                ["A tanulási folyamat sikeres, mindössze annyiban korlátozott, hogy nagy számítási kapacitást igényel.", "The learning process is successful, limited merely to the extent that it requires immense computing capacity."],
                ["Eltekintve a szélsőséges értékektől, a konvergencia gyors és megbízható.", "Disregarding extreme outliers, convergence is rapid and reliable."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mit jelent a 'túlilleszkedés' (overfitting) a gépi tanulásban?", [
                    "Amikor a modell túlságosan rögzíti a tanító adatok zaját, így képtelen általánosítani új adatokon.",
                    "Amikor túl kicsi a számítógép memóriája a program futtatásához.",
                    "Amikor az algoritmus hibátlanul működik minden elképzelhető helyzetben."
                ], 0, ["c1-15-vocab"]),
                fb("grammar", "controlled", "A neurális háló képes általánosítani az ismeretlen mintákon, _____ (except if / kivéve ha) a tanító adathalmaz túlzottan elfogult.", "kivéve ha", "The neural network is able to generalize on unseen patterns, except if the training dataset is overly biased.", ["c1-restrictive-exceptive-adverbials"]),
                match("vocabulary", "controlled", [["veszteségfüggvény", "a hiba számszerűsítése"], ["gradiens-csökkentés", "optimalizációs algoritmus"], ["tanító adathalmaz", "bemeneti minta tanuláshoz"], ["regularizáció", "túlilleszkedés megelőzése"]], ["c1-15-vocab"]),
                fb("grammar", "practice", "A tanulás elméletileg befejezettnek tekinthető, _____ annyiban, hogy a hibaérték egy minimális küszöb alatt marad. (merely / mindössze)", "mindössze", "The learning can theoretically be considered complete, merely to the extent that the error remains below a minimum threshold.", ["c1-restrictive-exceptive-adverbials"]),
                sb("grammar", "practice", ["A", "gradiens-csökkentés", "során", "az", "algoritmus", "lépésről", "lépésre", "minimalizálja", "a", "veszteségfüggvényt."], ["A", "gradiens-csökkentés", "során", "az", "algoritmus", "lépésről", "lépésre", "minimalizálja", "a", "veszteségfüggvényt."], "During gradient descent the algorithm minimizes the loss function step by step.", ["c1-restrictive-exceptive-adverbials"]),
                dc("dialogue", [
                    {"speaker": "Adattudós", "text": "Miért téveszt a modellünk az éles környezetben?"},
                    {"speaker": "Kutató", "text": "Valószínűleg túlilleszkedett, _____ nem alkalmaztunk megfelelő regularizációs eljárást a tanulás során."},
                ], ["mivel", "bár", "pedig"], 0, ["c1-restrictive-exceptive-adverbials"]),
                sw("production", [{"prompt": "Formulate a restrictive sentence describing machine learning convergence conditions.", "answer": "A gépi tanulási folyamat garantáltan konvergál az optimális megoldáshoz, kivéve ha a tanulási ráta túl magas, vagy a veszteségfüggvény több lokális minimummal rendelkezik."}], ["c1-restrictive-exceptive-adverbials"]),
                mc("grammar", "check", "Melyik mondat alkalmaz helyesen kivételt kifejező szerkezetet?", [
                    "A modell megbízható predikciót garantál, kivéve ha a bemeneti adatok mintázata drasztikusan módosul.",
                    "A modell megbízható predikciót garantál, miközben a bemeneti adatok mintázata módosul.",
                    "A modell megbízható predikciót garantál, hogy a bemeneti adatok mintázata módosuljon."
                ], 0, ["c1-restrictive-exceptive-adverbials"])
            ]
        },
        {
            "num": 2,
            "stem": "c1-15-02",
            "title": "Deep Learning Architectures & Transformer Models",
            "grammar_title": "Hypothetical Participles in Complex Computational Modeling",
            "grammar_skill": "c1-hypothetical-counterfactual-participles",
            "goals": [
                "I can analyze transformer architectures and self-attention mechanisms (*transzformátor, figyelem-mechanizmus, beágyazás*).",
                "I can employ hypothetical and counterfactual adverbial participles (*feltételezvén, figyelembe véve, eltekintvén*).",
                "I can debate large language model scaling laws and latent representations in advanced technical Hungarian."
            ],
            "vocab": [
                {"lemma": "transzformátor-architektúra", "translation": "transformer architecture", "pos": "noun"},
                {"lemma": "figyelem-mechanizmus", "translation": "self-attention mechanism", "pos": "noun"},
                {"lemma": "látens tér", "translation": "latent space", "pos": "noun"},
                {"lemma": "beágyazás", "translation": "embedding (vector representation)", "pos": "noun"},
                {"lemma": "nagy nyelvi modell", "translation": "large language model (LLM)", "pos": "noun"},
                {"lemma": "finomhangolás", "translation": "fine-tuning", "pos": "noun"},
                {"lemma": "paraméterszám", "translation": "parameter count", "pos": "noun"},
                {"lemma": "skálázhatóság", "translation": "scalability", "pos": "noun"}
            ],
            "gr_text1": "In high-register computational and analytical prose, hypothetical participles ending in *-ván/-vén* or adverbial participle clauses with *-va/-ve* introduce hypothetical premises and counterfactual considerations: `Feltételezvén a korlátlan számítási kapacitást, a modell elméletileg tökéletes reprezentációt építhetne fel`.",
            "gr_text2": "These participial clauses streamline academic syntax by subordinating extensive conditional clauses into compact analytical modifiers: `Figyelembe véve a transzformátorok párhuzamosíthatóságát, nyilvánvalóvá válik fölényük a rekurrens architektúrákkal szemben`.",
            "gr_table": [
                ["Feltételezvén az adatok reprezentatív jellegét, az architektúra hibahatára minimális.", "Assuming the representative nature of the data, the architecture's margin of error is minimal."],
                ["Eltekintvén a magas hardverköltségektől, a modell skálázhatósága páratlan.", "Setting aside high hardware costs, the model's scalability is unmatched."],
                ["Számításba véve a figyelem-mechanizmus komplexitását, kvadratikus növekedéssel kell kalkulálnunk.", "Taking into account the complexity of the attention mechanism, we must calculate with quadratic growth."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mi a transzformátor-architektúra kulcsfontosságú újítása?", [
                    "Az önfigyelem (self-attention) mechanizmusa, amely lehetővé teszi a kontextus párhuzamos feldolgozását szekvenciális lépések nélkül.",
                    "A mágnesszalagos adattárolás bevezetése.",
                    "A képernyők felbontásának megduplázása."
                ], 0, ["c1-15-vocab"]),
                fb("grammar", "controlled", "_____ (Assuming / Feltételezvén) a tanulási adathalmaz sokszínűségét, a nagy nyelvi modell képes megragadni a finom stilisztikai árnyalatokat.", "Feltételezvén", "Assuming the diversity of the training dataset, the large language model can capture subtle stylistic nuances.", ["c1-hypothetical-counterfactual-participles"]),
                match("vocabulary", "controlled", [["látens tér", "többdimenziós reprezentáció"], ["beágyazás", "szavak numerikus vektora"], ["finomhangolás", "célfeladatra való igazítás"], ["paraméterszám", "a modell belső súlyai"]], ["c1-15-vocab"]),
                fb("grammar", "practice", "Minden szempontot figyelembe _____, a transzformátorok forradalmasították a természetes nyelvfeldolgozást. (taking / véve)", "véve", "Taking all aspects into account, transformers revolutionized natural language processing.", ["c1-hypothetical-counterfactual-participles"]),
                sb("grammar", "practice", ["A", "figyelem-mechanizmus", "révén", "a", "modell", "párhuzamosan", "értékeli", "a", "kontextuális", "összefüggéseket."], ["A", "figyelem-mechanizmus", "révén", "a", "modell", "párhuzamosan", "értékeli", "a", "kontextuális", "összefüggéseket."], "Via the attention mechanism the model evaluates contextual relationships in parallel.", ["c1-hypothetical-counterfactual-participles"]),
                dc("dialogue", [
                    {"speaker": "MI-mérnök", "text": "Hogyan javíthatjuk a nyelvi modell szakmai pontosságát?"},
                    {"speaker": "Architekt", "text": "Célzott jogi vagy orvosi szövegeken végzett domain-specifikus _____ révén."},
                ], ["finomhangolás", "törlés", "áramtalanítás"], 0, ["c1-hypothetical-counterfactual-participles"]),
                sw("production", [{"prompt": "Write an analytical sentence using a hypothetical participle to explain model scaling.", "answer": "Feltételezvén a hardveres infrastruktúra exponenciális fejlődését, a milliárdos paraméterszámú modellek hamarosan valós idejű multimodális szintézist valósíthatnak meg."}], ["c1-hypothetical-counterfactual-participles"]),
                mc("grammar", "check", "Melyik kifejezés fejez ki feltételes/feltevést tartalmazó participiális szerkezetet?", [
                    "Feltételezvén a paraméterek stabilitását",
                    "A paraméterek stabilitásának hiányában",
                    "Mivel a paraméterek stabilak voltak"
                ], 0, ["c1-hypothetical-counterfactual-participles"])
            ]
        },
        {
            "num": 3,
            "stem": "c1-15-03",
            "title": "Cognitive Epistemology & Heuristic Reasoning",
            "grammar_title": "Proportional Correlatives in Cognitive Science and Epistemology",
            "grammar_skill": "c1-complex-proportional-correlatives",
            "goals": [
                "I can analyze heuristic reasoning, explainability, and the black box problem (*heurisztika, magyarázhatóság, feketedoboz*).",
                "I can construct complex proportional and comparative correlatives (*minél inkább... annál inkább, egyfelől... másfelől, nem annyira... mint inkább*).",
                "I can evaluate symbolic AI versus connectionist paradigms in Hungarian epistemology."
            ],
            "vocab": [
                {"lemma": "heurisztika", "translation": "heuristics, shortcut reasoning", "pos": "noun"},
                {"lemma": "episztemológia", "translation": "epistemology, theory of knowledge", "pos": "noun"},
                {"lemma": "feketedoboz-jelenség", "translation": "black box phenomenon", "pos": "noun"},
                {"lemma": "magyarázhatóság", "translation": "explainability, interpretability", "pos": "noun"},
                {"lemma": "induktív következtetés", "translation": "inductive inference", "pos": "expression"},
                {"lemma": "dedukció", "translation": "deduction, logical derivation", "pos": "noun"},
                {"lemma": "szimbolikus mesterséges intelligencia", "translation": "symbolic AI, rule-based AI", "pos": "expression"},
                {"lemma": "konnekcionizmus", "translation": "connectionism, neural network paradigm", "pos": "noun"}
            ],
            "gr_text1": "Proportional and comparative correlatives establish nuanced cognitive relationships: `minél komplexebbé válik egy neurális háló, annál nehezebb megérteni belső döntéshozatali mechanizmusait` (the more complex a neural net becomes, the harder it is to understand its internal mechanisms).",
            "gr_text2": "Similarly, `nem annyira X, mint inkább Y` (not so much X as rather Y) and `egyfelől... másfelől` structure balanced epistemological critiques: `A feketedoboz-jelenség nem annyira matematikai hiba, mint inkább a többdimenziós látens terek emberi felfoghatatlanságának következménye`.",
            "gr_table": [
                ["Minél mélyebb a hálózat architektúrája, annál kevésbé magyarázható az egyedi súlyok szerepe.", "The deeper the network's architecture, the less explainable the role of individual weights is."],
                ["Nem annyira az adatok mennyisége, mint inkább azok minősége határozza meg a megismerés hatékonyságát.", "It is not so much the quantity of data as rather its quality that determines the efficiency of cognition."],
                ["Egyfelől csodáljuk a mintafelismerési képességet, másfelől aggodalommal tölt el az átláthatóság hiánya.", "On one hand we admire pattern recognition capacity; on the other hand the lack of transparency causes concern."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mi a lényege a 'feketedoboz-jelenségnek' (black box) a mesterséges intelligenciában?", [
                    "Bár a bemenet és a kimenet ismert, a modell belső döntési logikája az emberi elme számára közvetlenül átláthatatlan.",
                    "Hogy a számítógépeket fekete műanyag házba építik be.",
                    "Hogy a repülőgépek repülési adatait rögzíti."
                ], 0, ["c1-15-vocab"]),
                fb("grammar", "controlled", "Minél komplexebbé válik az algoritmus, _____ (the more / annál) égetőbb kérdéssé válik a döntések magyarázhatósága.", "annál", "The more complex the algorithm becomes, the more pressing the explainability of decisions becomes.", ["c1-complex-proportional-correlatives"]),
                match("vocabulary", "controlled", [["heurisztika", "gyakorlati egyszerűsítő szabály"], ["episztemológia", "ismeretelmélet"], ["magyarázhatóság", "modell belső logikájának feltárhatósága"], ["szimbolikus MI", "szabályalapú logikai rendszer"]], ["c1-15-vocab"]),
                fb("grammar", "practice", "A jelenlegi gépi tanulás nem annyira valódi megértésen, mint _____ (rather / inkább) statisztikai mintafelismerésen alapul.", "inkább", "Current machine learning is based not so much on genuine understanding as rather on statistical pattern recognition.", ["c1-complex-proportional-correlatives"]),
                sb("grammar", "practice", ["A", "magyarázható", "mesterséges", "intelligencia", "a", "bizalom", "elengedhetetlen", "előfeltétele."], ["A", "magyarázható", "mesterséges", "intelligencia", "a", "bizalom", "elengedhetetlen", "előfeltétele."], "Explainable artificial intelligence is the indispensable prerequisite of trust.", ["c1-complex-proportional-correlatives"]),
                dc("dialogue", [
                    {"speaker": "Filozófus", "text": "Képes-e egy nagy nyelvi modell valódi fogalmi megértésre?"},
                    {"speaker": "Kognitív kutató", "text": "Nem annyira intencionalitásról van szó, mint inkább a nyelvi statisztikák virtuóz szintű _____."},
                ], ["tükrözéséről", "eltitkolásáról", "letöltéséről"], 0, ["c1-complex-proportional-correlatives"]),
                sw("production", [{"prompt": "Write a comparative correlative sentence comparing symbolic AI and neural networks.", "answer": "Minél inkább a merev szimbolikus szabályok helyett az adaptív konnekcionista hálózatokra támaszkodunk, annál inkább háttérbe szorul a deduktív bizonyíthatóság a statisztikai valószínűség javára."}], ["c1-complex-proportional-correlatives"]),
                mc("grammar", "check", "Melyik kötőszópár fejez ki arányos összehasonlítást?", [
                    "minél... annál",
                    "noha... mégis",
                    "jóllehet... mindamellett"
                ], 0, ["c1-complex-proportional-correlatives"])
            ]
        },
        {
            "num": 4,
            "stem": "c1-15-04",
            "title": "Algorithmic Governance & Automated Decision Systems",
            "grammar_title": "Epistemic Probability Modifiers in Data-Driven Governance",
            "grammar_skill": "c1-modal-probabilistic-modifiers",
            "goals": [
                "I can analyze automated decision-making and algorithmic risk assessment (*adatalapú döntéshozatal, prediktív elemzés, kockázatértékelés*).",
                "I can employ modal adverbials of epistemic probability (*feltehetően, vélhetően, minden bizonnyal, aligha vitathatóan*).",
                "I can assess social scoring, systemic bias, and institutional oversight mechanisms in elevated Hungarian."
            ],
            "vocab": [
                {"lemma": "adatalapú döntéshozatal", "translation": "data-driven decision making", "pos": "expression"},
                {"lemma": "prediktív elemzés", "translation": "predictive analytics", "pos": "noun"},
                {"lemma": "kockázatértékelés", "translation": "risk assessment", "pos": "noun"},
                {"lemma": "automatizált adminisztráció", "translation": "automated administration", "pos": "noun"},
                {"lemma": "pontozási rendszer", "translation": "scoring system", "pos": "noun"},
                {"lemma": "felügyeleti mechanizmus", "translation": "oversight mechanism", "pos": "noun"},
                {"lemma": "torzítás", "translation": "bias, distortion", "pos": "noun"},
                {"lemma": "megbízhatóság", "translation": "reliability, dependability", "pos": "noun"}
            ],
            "gr_text1": "Modal adverbials of epistemic probability allow policy analysts and scholars to calibrate certainty regarding algorithmic outcomes: `vélhetően` (presumably), `feltehetően` (supposedly), `minden bizonnyal` (in all likelihood), `aligha vitathatóan` (indisputably), and `megkérdőjelezhetően` (questionably).",
            "gr_text2": "Example in governance prose: `Az automatizált elbírálási rendszerek bevezetése vélhetően növeli az adminisztratív hatékonyságot, ám aligha vitathatóan új jogvédelmi aggályokat teremt az állampolgárok számára`.",
            "gr_table": [
                ["Az algoritmus feltehetően a korábbi kifizetési minták alapján becsüli meg a kockázatot.", "The algorithm supposedly estimates risk based on past payment patterns."],
                ["Minden bizonnyal szigorúbb auditra lesz szükség a pénzügyi szektorban.", "In all likelihood stricter audits will be required in the financial sector."],
                ["Aligha vitathatóan torzít a rendszer, ha az adathalmaz nem tükrözi a társadalom valós összetételét.", "The system indisputably biases if the dataset fails to reflect the real composition of society."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mi a kockázata az automatizált adatalapú döntéshozatalnak a közszférában?", [
                    "A történelmi adatokban rejlő társadalmi torzítások (bias) intézményesülése és a jogorvoslat nehézkessége.",
                    "Hogy a nyomtatók túl sok papírt használnak el.",
                    "Hogy az irodákban túl csendes lesz a munkakörnyezet."
                ], 0, ["c1-15-vocab"]),
                fb("grammar", "controlled", "A prediktív pontozási rendszerek alkalmazása _____ (indisputably / aligha vitathatóan) mélyreható átláthatósági kihívásokat vet fel a közigazgatásban.", "aligha vitathatóan", "The application of predictive scoring systems indisputably raises profound transparency challenges in public administration.", ["c1-modal-probabilistic-modifiers"]),
                match("vocabulary", "controlled", [["prediktív elemzés", "jövőbeli események valószínűségi becslése"], ["kockázatértékelés", "veszélyek felmérése"], ["pontozási rendszer", "profilozáson alapuló rangsorolás"], ["felügyeleti mechanizmus", "külső ellenőrző apparátus"]], ["c1-15-vocab"]),
                fb("grammar", "practice", "Az algoritmus döntése _____ a régebbi demográfiai mintákból eredő egyenlőtlenségeket tükrözi. (presumably / vélhetően)", "vélhetően", "The algorithm's decision presumably reflects inequalities stemming from older demographic patterns.", ["c1-modal-probabilistic-modifiers"]),
                sb("grammar", "practice", ["Az", "automatizált", "döntéshozatal", "nem", "helyettesítheti", "a", "felelős", "emberi", "mérlegelést."], ["Az", "automatizált", "döntéshozatal", "nem", "helyettesítheti", "a", "felelős", "emberi", "mérlegelést."], "Automated decision-making cannot replace responsible human deliberation.", ["c1-modal-probabilistic-modifiers"]),
                dc("dialogue", [
                    {"speaker": "Jogvédő", "text": "Hogyan garantálható az állampolgárok védelme az algoritmusokkal szemben?"},
                    {"speaker": "Közigazgatási szakértő", "text": "Kötelező emberi felülvizsgálattal és független etikai _____ létrehozásával."},
                ], ["audit", "félrevezetés", "titkosítás"], 0, ["c1-modal-probabilistic-modifiers"]),
                sw("production", [{"prompt": "Write a sentence using an epistemic probability adverbial to evaluate algorithmic governance.", "answer": "A gépi predikciók kritikátlan elfogadása minden bizonnyal erodálja a jogállami garanciákat, amennyiben az érintettek nem kapnak részletes és érthető indoklást a döntések hátteréről."}], ["c1-modal-probabilistic-modifiers"]),
                mc("grammar", "check", "Melyik modális határozószó fejezi ki a legnagyobb mértékű bizonyosságot?", [
                    "aligha vitathatóan",
                    "esetleg",
                    "tán"
                ], 0, ["c1-modal-probabilistic-modifiers"])
            ]
        },
        {
            "num": 5,
            "stem": "c1-15-05",
            "title": "John von Neumann & The Computational Architecture of the Brain",
            "grammar_title": "Complex Appositive Structures in Cybernetic Philosophy",
            "grammar_skill": "c1-adv-nominal-appositive-structures",
            "goals": [
                "I can analyze John von Neumann's cybernetic insights in 'The Computer and the Brain'.",
                "I can deploy complex appositive noun phrases with clarifying discourse markers (*mint olyan, nevezetesen, tudniillik, mégpedig*).",
                "I can evaluate analog versus digital paradigms and biological neural processing in intellectual Hungarian."
            ],
            "vocab": [
                {"lemma": "automataelmélet", "translation": "automata theory", "pos": "noun"},
                {"lemma": "analóg-digitális dichotómia", "translation": "analog-digital dichotomy", "pos": "expression"},
                {"lemma": "idegrendszeri impulzus", "translation": "neural impulse", "pos": "expression"},
                {"lemma": "számítási kapacitás", "translation": "computing capacity", "pos": "noun"},
                {"lemma": "architektúra", "translation": "computational architecture", "pos": "noun"},
                {"lemma": "kibernetika", "translation": "cybernetics", "pos": "noun"},
                {"lemma": "sztochasztikus folyamat", "translation": "stochastic process", "pos": "noun"},
                {"lemma": "szinergia", "translation": "synergy", "pos": "noun"}
            ],
            "gr_text1": "Complex appositive constructions expand nominal heads using explanatory markers: `nevezetesen` (namely), `tudniillik` (that is to say), `mégpedig` (specifically), and `mint olyan` (as such): `Neumann János felismerte az idegrendszer és az automata közötti alapvető eltérést, nevezetesen azt, hogy az agy alacsonyabb numerikus pontossággal, ám hatalmas párhuzamossággal dolgozik`.",
            "gr_text2": "These appositives allow academic discourse to clarify dense abstract concepts without interrupting the logical progression of the period.",
            "gr_table": [
                ["A modern számítógép, mint olyan, a neumann-i architektúra alapelvein nyugszik.", "The modern computer, as such, rests upon the principles of von Neumann architecture."],
                ["Az agy egyedülálló képessége, tudniillik a hibatűrő sztochasztikus működés, meghaladja a digitális áramköröket.", "The brain's unique ability, that is to say fault-tolerant stochastic operation, exceeds digital circuits."],
                ["Két eltérő logikát látunk, mégpedig a diszkrét bináris kódolást és a folytonos analóg ingerületátvitelt.", "We see two divergent logics, specifically discrete binary encoding and continuous analog signal transmission."]
            ],
            "classic_story": {
                "slug": "c1-15-neumann",
                "author": "Neumann János",
                "work": "A számítógép és az agy (The Computer and the Brain, 1958)",
                "title": "Az elektronikus automata és az emberi idegrendszer szintézise",
                "summary": "John von Neumann's posthumous masterwork exploring the profound parallels, thermodynamic contrasts, and mathematical languages separating artificial computing machines from the human central nervous system.",
                "characters": ["Neumann János"],
                "paragraphs": [
                    {"type": "narration", "text": "Amikor Neumann János a Yale Egyetem Silliman-előadásaira készült halálos betegágyán, nem csupán a modern digitális számítógép atyjaként vetett számot az általa megteremtett architektúrával: egy új tudományág, a bio-kibernetika és a kognitív komputáció alapjait fektette le. 'A számítógép és az agy' (1958) című posztumusz műve az intellektuális tisztánlátás emlékműve."},
                    {"type": "narration", "text": "Neumann az első volt, aki szigorú matematikai precizitással vetette össze az elektronikus vákuumcsövek (későbbi tranzisztorok) működését a biológiai neuronok akciós potenciáljával. Rámutatott az alapvető dichotómiára: míg az ember alkotta gép rendkívül gyors és magas numerikus aritmetikai pontosságot követel meg a soros számításokban, addig az emberi agy viszonylag lassú idegi impulzusokkal, ám döbbenetesen magas szintű párhuzamos feldolgozással és sztochasztikus hibatűréssel operál."},
                    {"type": "narration", "text": "Meglátása szerint az idegrendszer nem tiszta digitális kódolást használ: a sejtek közötti ingerületátvitel analóg és digitális mechanizmusok lenyűgöző szintézise. 'Az agy nyelve nem a matematika formális nyelve' – írta Neumann az utolsó fejezetekben, megsejtve, hogy a mesterséges neurális hálózatok évtizedekkel később nem logikai formulák, hanem sokdimenziós statisztikai súlyozások révén közelítik majd meg az emberi észlelés rugalmasságát."},
                    {"type": "narration", "text": "Neumann öröksége a mai mesterséges intelligencia forradalom idején intő figyelmeztetés és vezérfonal egyszerre. Arra emlékeztet minket, hogy a technológia legnagyobb diadala nem az emberi elme felváltása, hanem annak megértése: a szilícium és a biológia közötti párbeszéd végső soron magának a gondolkodásnak a titkát kutatja."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Milyen alapvető különbséget állapított meg Neumann János a számítógép és az agy között?", [
                    "A gép nagy sebességű soros számításokat végez nagy számtani pontossággal, míg az agy lassabb idegsejtekkel, de masszív párhuzamosítással és hibatűréssel dolgozik.",
                    "Hogy a gép érzelmekkel rendelkezik, az emberi agy viszont csak számokat lát.",
                    "Hogy az agy közvetlenül 220 voltos hálózati feszültséggel működik."
                ], 0, ["c1-15-vocab"]),
                fb("grammar", "controlled", "Neumann feltárta az alapvető különbséget, _____ (specifically / mégpedig) a digitális pontosság és a biológiai hibatűrés ellentétét.", "mégpedig", "Neumann revealed the fundamental difference, specifically the contrast between digital precision and biological fault-tolerance.", ["c1-adv-nominal-appositive-structures"]),
                match("vocabulary", "controlled", [["automataelmélet", "önműködő gépek matematikai modellje"], ["kibernetika", "rendszerek vezérlés- és kommunikációelmélete"], ["sztochasztikus folyamat", "valószínűségi alapú működés"], ["architektúra", "számítógép hardveres és logikai felépítése"]], ["c1-15-vocab"]),
                mc("reading", "practice", "Mit jelentett Neumann híres felismerése, miszerint 'az agy nyelve nem a matematika nyelve'?", [
                    "Hogy az idegrendszer nem merev formális logikai szimbólumokkal, hanem statisztikai és analóg jellegű ingerületi mintázatokkal reprezentálja a világot.",
                    "Hogy az orvosoknak nem szabad matematikát tanulniuk.",
                    "Hogy a számítógépek képtelenek összeadni a törteket."
                ], 0, None),
                sb("grammar", "practice", ["A", "neumann-i", "architektúra", "mindmáig", "a", "digitális", "számítástechnika", "alapköve."], ["A", "neumann-i", "architektúra", "mindmáig", "a", "digitális", "számítástechnika", "alapköve."], "The von Neumann architecture remains to this day the cornerstone of digital computing.", ["c1-adv-nominal-appositive-structures"]),
                sw("production", [{"prompt": "Synthesize John von Neumann's cybernetic thesis using an explanatory appositive.", "answer": "Neumann János zseniális felismerése, tudniillik hogy a biológiai idegrendszer sztochasztikus hibatűrése alapvetően felülmúlja a soros elektronikus gépek merev precizitását, megvetette a modern neurális hálózatok elméleti fundamentumát."}], ["c1-adv-nominal-appositive-structures"]),
                mc("grammar", "check", "Melyik mondat alkalmaz helyesen pontosító értelmező szerkezetet?", [
                    "Megismertük az algoritmus legnagyobb korlátját, nevezetesen az ellenőrizhetetlen feketedoboz-jelenséget.",
                    "Megismertük az algoritmus legnagyobb korlátját, minthogy ellenőrizhetetlen feketedoboz-jelenség.",
                    "Megismertük az algoritmus legnagyobb korlátját, bár ellenőrizhetetlen feketedoboz-jelenség."
                ], 0, ["c1-adv-nominal-appositive-structures"])
            ]
        }
    ]

    for l in core_lessons:
        emit_instructional_lesson(15, "core", l, core_title, core_intro if l["num"] == 1 else None)

    # Core Consolidation
    emit_consolidation_lesson(
        15,
        "core",
        "c1-15-consolidation",
        core_title,
        [
            "I can analyze machine learning foundations, gradient optimization, and regularization.",
            "I can employ restrictive clauses, hypothetical participles, and proportional correlatives.",
            "I can discuss John von Neumann's computational philosophy and neural architectures at the C1 level."
        ],
        [
            mc("grammar", "recognize", "Milyen szerkezettel fejezhetünk ki kivételt vagy korlátozást egy állításban?", [
                "kivéve ha / mindössze annyiban, hogy",
                "minél... annál",
                "jóllehet... mégis"
            ], 0, ["c1-restrictive-exceptive-adverbials"]),
            mc("grammar", "recognize", "Milyen funkciót töltenek be a '-ván/-vén' végű participiumok az akadémiai szövegekben?", [
                "Hipotetikus feltételeket vagy ok-okozati körülményeket sűrítenek elegáns szintaktikai formába.",
                "Kizárólag múlt idejű parancsot fejeznek ki.",
                "Kérdő mondatok végén álló kötőszók."
            ], 0, ["c1-hypothetical-counterfactual-participles"]),
            match("vocabulary", "recognize", [["gradiens-csökkentés", "veszteség minimalizálása"], ["látens tér", "többdimenziós reprezentáció"], ["heurisztika", "gyakorlati egyszerűsítés"], ["aligha vitathatóan", "kétségtelenül, bizonyosan"], ["nevezetesen", "tudniillik, pontosabban"]], ["c1-15-vocab"]),
            fb("vocabulary", "recall", "A modell képtelen volt általánosítani, mert a tanító adatokon súlyos _____ lépett fel. (overfitting / túlilleszkedés)", "túlilleszkedés", "The model was unable to generalize because severe overfitting occurred on the training data.", ["c1-15-vocab"]),
            fb("vocabulary", "recall", "A modern transzformátorok alapja a szövegek többdimenziós vektortérbe történő _____ helyezése. (embedding / beágyazása)", "beágyazása", "The foundation of modern transformers is embedding texts into multidimensional vector space.", ["c1-15-vocab"]),
            fb("grammar", "recall", "A tanulás zökkenőmentes volt, _____ annyiban, hogy az adatbázis tisztítása sokáig tartott. (merely / mindössze)", "mindössze", "The learning was smooth, merely to the extent that cleaning the database took a long time.", ["c1-restrictive-exceptive-adverbials"]),
            fb("grammar", "context", "_____ a gépi modellek exponenciális növekedését, az energiafogyasztás drasztikusan meg fog nőni. (Assuming / Feltételezvén)", "Feltételezvén", "Assuming the exponential growth of machine models, energy consumption will increase drastically.", ["c1-hypothetical-counterfactual-participles"]),
            fb("grammar", "context", "Minél nagyobb a tanító adathalmaz mérete, _____ pontosabbak az algoritmus predikciói. (the / annál)", "annál", "The larger the size of the training dataset, the more accurate the algorithm's predictions are.", ["c1-complex-proportional-correlatives"]),
            mc("grammar", "context", "Hogyan értékelte Neumann János az idegrendszer hibatűrését?", [
                "Felismerte, hogy a biológiai agy sztochasztikus működése dacára képes megőrizni globális stabilitását.",
                "Úgy vélte, az agy egyáltalán nem működőképes.",
                "Azt hitte, az agy egy mechanikus gőzgép."
            ], 0, ["c1-adv-nominal-appositive-structures"]),
            sb("grammar", "produce", ["A", "mesterséges", "intelligencia", "fejlődése", "aligha", "vitathatóan", "új", "társadalmi", "paradigmát", "teremt."], ["A", "mesterséges", "intelligencia", "fejlődése", "aligha", "vitathatóan", "új", "társadalmi", "paradigmát", "teremt."], "The advancement of artificial intelligence indisputably creates a new social paradigm.", ["c1-modal-probabilistic-modifiers"]),
            sw("production", [{"prompt": "Write a critical evaluation of black-box AI in institutional governance.", "answer": "A feketedoboz-jelenség az intézményi döntéshozatalban aligha vitathatóan veszélyezteti a demokratikus elszámoltathatóságot, kivéve ha kötelező magyarázhatósági és emberi felülbírálati garanciákat építünk be a rendszerbe."}], ["c1-restrictive-exceptive-adverbials"]),
            sw("production", [{"prompt": "Formulate a reflection on John von Neumann's computational legacy.", "answer": "Neumann János 'A számítógép és az agy' című műve mindmáig eleven tanúságtétel amellett, hogy a technológiai innováció legmélyebb forrása a biológiai komplexitás alázatos tanulmányozása."}], ["c1-adv-nominal-appositive-structures"])
        ]
    )

    # ----------------------------------------------------
    # TRACK 2: DISCOURSE (c1-mestersegesintelligencia)
    # ----------------------------------------------------
    disc_title = "AI Ethics, Neural Networks & Technological Sovereignty"
    slug = "mestersegesintelligencia"

    disc_intro = [
        "In the European discourse space, artificial intelligence intersects policy regulation, ethical accountability, labor market displacement, and technological sovereignty.",
        "Through serialized case studies spanning Hungarian research centers (SZTAKI, ELTE), the European AI Act, cognitive labor automation, healthcare radiology AI, and existential alignment risks, you will master sophisticated debating registers in C1 Hungarian."
    ]

    disc_lessons = [
        {
            "num": 1,
            "stem": f"c1-{slug}-01",
            "title": "Foundation Models & Hungarian Computing Research",
            "grammar_title": "Delimiting and Focalizing Particles in Tech Discourse",
            "grammar_skill": "c1-discourse-limiting-particles",
            "goals": [
                "I can analyze Hungarian AI research initiatives (*SZTAKI, MILAB, Komondor szuperszámítógép*).",
                "I can utilize delimiting and focalizing particles (*kiváltképp, éppenséggel, egyenesen, voltaképpen*).",
                "I can discuss sovereign language models (Puli, Nyelvmodell) and domestic research infrastructure."
            ],
            "vocab": [
                {"lemma": "kutatóhálózat", "translation": "research network", "pos": "noun"},
                {"lemma": "kiválóság", "translation": "academic excellence", "pos": "noun"},
                {"lemma": "nyelvi reprezentáció", "translation": "linguistic representation", "pos": "noun"},
                {"lemma": "szuperszámítógép", "translation": "supercomputer (Komondor HPC)", "pos": "noun"},
                {"lemma": "nemzeti MI-stratégia", "translation": "national AI strategy", "pos": "expression"},
                {"lemma": "neurális hálózat", "translation": "neural network", "pos": "noun"},
                {"lemma": "adatbázis", "translation": "database", "pos": "noun"},
                {"lemma": "szuverenitás", "translation": "technological sovereignty", "pos": "noun"}
            ],
            "gr_text1": "Delimiting and focalizing particles (*kiváltképp* [especially], *éppenséggel* [as a matter of fact / indeed], *egyenesen* [outright / directly], *tulajdonképpen / voltaképpen* [essentially / strictly speaking]) lend precision and rhetorical force to academic tech discourse.",
            "gr_text2": "Example: `A magyar nyelv agglutináló sajátosságai kiváltképp nagy kihívás elé állítják a nagy nyelvi modelleket, amelyek éppenséggel az angolszász izoláló struktúrákra lettek optimalizálva`.",
            "gr_table": [
                ["A hazai kutatóintézetek kiváltképp a morfológiai elemzés terén értek el áttörést.", "Domestic research institutes reached breakthroughs especially in morphological parsing."],
                ["Ez a technológiai függőség éppenséggel a digitális szuverenitást veszélyezteti.", "This technological dependence indeed jeopardizes digital sovereignty."],
                ["Az eredmények egyenesen felülmúlták a legoptimistább nemzetközi várakozásokat is.", "The results outright surpassed even the most optimistic international expectations."]
            ],
            "world_story_seg": {
                "seg_slug": "alapmodellek",
                "title": "A magyar szó szilíciumba vésve: SZTAKI, MILAB és a nemzeti modellek",
                "summary": "How Hungarian computer scientists and institutions like SZTAKI and MILAB navigate the foundation model era to ensure linguistic and digital sovereignty for Hungarian.",
                "paragraphs": [
                    {"type": "narration", "text": "Amikor a Számítástechnikai és Automatizálási Kutatóintézet (SZTAKI) és a Mesterséges Intelligencia Nemzeti Laboratórium (MILAB) kutatói nekifogtak a saját nagy nyelvi modellek kifejlesztésének, nem csupán mérnöki feladatot oldottak meg: a nemzeti kulturális szuverenitás digitális védvonalát húzták meg."},
                    {"type": "narration", "text": "A magyar nyelv sajátos gazdagsága – az összetett esetragok, a gazdag igeragozás és a szabad szórend – kiváltképp próbára teszi a globális multimodális rendszereket. A debreceni Komondor szuperszámítógép kapacitásával megtámogatott hazai projektek (mint a Puli modellcsalád) bebizonyították, hogy Magyarország képes önálló kutatási kiválósági központként fellépni a generatív forradalom korszakában."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Miért van kiemelt jelentősége a magyar nyelvű saját alapmodellek (pl. Puli) fejlesztésének?", [
                    "Mert biztosítják, hogy a magyar nyelv agglutináló szerkezete és kulturális kontextusa pontosan érvényesüljön a digitális térben.",
                    "Mert betiltják az összes külföldi weboldalt.",
                    "Mert olcsóbbá teszik a billentyűzetek gyártását."
                ], 0, ["c1-mestersegesintelligencia-vocab"]),
                fb("grammar", "controlled", "A nyelvi modellek fejlesztése során a magyar toldalékolási rendszer _____ (especially / kiváltképp) komoly morfológiai előkészítést igényel.", "kiváltképp", "During the development of language models, the Hungarian affixation system especially requires serious morphological preparation.", ["c1-discourse-limiting-particles"]),
                match("vocabulary", "controlled", [["SZTAKI", "kutatóintézet"], ["MILAB", "nemzeti MI laboratórium"], ["szuperszámítógép", "Komondor HPC"], ["digitális szuverenitás", "nemzeti függetlenség a tech szektorban"]], ["c1-mestersegesintelligencia-vocab"]),
                fb("grammar", "practice", "A globális platformoktól való egyoldalú függés _____ (indeed / éppenséggel) az európai adatszuverenitás felszámolásához vezethet.", "éppenséggel", "Unilateral dependence on global platforms can indeed lead to the liquidation of European data sovereignty.", ["c1-discourse-limiting-particles"]),
                sb("grammar", "practice", ["A", "hazai", "kutatóhálózat", "kiváltképp", "nagy", "hangsúlyt", "fektet", "a", "nyelvi", "reprezentációra."], ["A", "hazai", "kutatóhálózat", "kiváltképp", "nagy", "hangsúlyt", "fektet", "a", "nyelvi", "reprezentációra."], "The domestic research network places especially great emphasis on linguistic representation.", ["c1-discourse-limiting-particles"]),
                dc("dialogue", [
                    {"speaker": "Kutató", "text": "Miért nem elegendő az amerikai modellek fordítására hagyatkozni?"},
                    {"speaker": "Nyelvész", "text": "Mert a fordításokból hiányzik a magyar kulturális kontextus és a pontos morfológiai _____."},
                ], ["illeszkedés", "törlés", "szétszakítás"], 0, ["c1-discourse-limiting-particles"]),
                sw("production", [{"prompt": "Write a sentence using a focalizing particle to emphasize technological sovereignty.", "answer": "A független hazai szuperszámítógép-kapacitások kiépítése egyenesen elengedhetetlen ahhoz, hogy a nemzeti kutatás ne szoruljon a globális technológiai óriások kiszolgálójának szerepébe."}], ["c1-discourse-limiting-particles"]),
                mc("grammar", "check", "Melyik mondat alkalmaz határoló/fókuszáló partikulát emelkedett stílusban?", [
                    "A modell pontossága éppenséggel a szakszerű finomhangolásnak köszönhető.",
                    "A modell pontossága mivel szakszerűen finomhangolták.",
                    "A modell pontossága ha szakszerűen finomhangolják."
                ], 0, ["c1-discourse-limiting-particles"])
            ]
        },
        {
            "num": 2,
            "stem": f"c1-{slug}-02",
            "title": "Algorithmic Bias, Transparency & the EU AI Act",
            "grammar_title": "Correlative Causal Connectors in AI Ethics and Regulation",
            "grammar_skill": "c1-correlative-causal-adverbials",
            "goals": [
                "I can analyze the European AI Act risk tiers and compliance audits (*AI Act, nagy kockázatú rendszerek, megfelelőségi audit*).",
                "I can deploy correlative causal connectors (*annál is inkább mivel, abból a megfontolásból fakadóan, arra hivatkozva hogy*).",
                "I can evaluate algorithmic discrimination, human-in-the-loop oversight, and institutional liability."
            ],
            "vocab": [
                {"lemma": "mesterséges intelligencia rendelet", "translation": "AI Act (EU regulation)", "pos": "expression"},
                {"lemma": "algoritmus-etika", "translation": "algorithmic ethics", "pos": "noun"},
                {"lemma": "átláthatóság", "translation": "transparency", "pos": "noun"},
                {"lemma": "diszkriminációmentesség", "translation": "non-discrimination", "pos": "noun"},
                {"lemma": "nagy kockázatú rendszer", "translation": "high-risk AI system", "pos": "expression"},
                {"lemma": "emberi felügyelet", "translation": "human oversight (human-in-the-loop)", "pos": "expression"},
                {"lemma": "megfelelőségi audit", "translation": "conformity audit / assessment", "pos": "noun"},
                {"lemma": "felelősségvállalás", "translation": "accountability, assumption of liability", "pos": "noun"}
            ],
            "gr_text1": "Correlative causal connectors link institutional mandates and regulatory causes: `annál is inkább, mivel...` (all the more so since...), `abból a megfontolásból fakadóan, hogy...` (arising from the consideration that...), and `arra való hivatkozással, hogy...` (with reference to the claim that...).",
            "gr_text2": "Example in EU policy context: `Az Európai Unió szigorú szabályozást vezetett be a nagy kockázatú rendszerekre, annál is inkább, mivel az automatizált arcfelismerés alapvető emberi jogi garanciákat fenyeget`.",
            "gr_table": [
                ["A jogalkotó korlátozza a biometrikus azonosítást, annál is inkább, mivel a visszaélés veszélye rendkívül magas.", "The legislator restricts biometric identification, all the more so since the risk of abuse is extremely high."],
                ["Abból a megfontolásból fakadóan hoztak szabályokat, hogy a polgárok emberi felügyeletet követelhessenek.", "They introduced rules arising from the consideration that citizens should be able to demand human oversight."],
                ["A megfelelőségi audit elengedhetetlen, annál is inkább, mivel a jogsértések súlyos bírságot vonnak maguk után.", "Conformity assessment is indispensable, all the more so since infringements incur severe fines."]
            ],
            "world_story_seg": {
                "seg_slug": "etika",
                "title": "A brüsszeli mérce: Az AI Act és az algoritmus-etika európai útja",
                "summary": "How the European Union enacted the world's first comprehensive horizontal AI legislation, classifying risk tiers and demanding algorithmic transparency.",
                "paragraphs": [
                    {"type": "narration", "text": "Az Európai Parlament és a Tanács által elfogadott Mesterséges Intelligencia Rendelet (AI Act) a digitális korszak egyik legfontosabb jogalkotási mérföldköve. Európa úgy döntött: nem a vadkapitalista adathalászat vagy a tekintélyelvű társadalmi pontozás mintáját követi, hanem a polgárok méltóságára és az alapjogok védelmére alapozza a technológiai fejlődést."},
                    {"type": "narration", "text": "A jogszabály kockázatalapú megközelítést alkalmaz: a tiltott kategóriák (mint a valós idejű távoli biometrikus arcfelismerés a nyilvános terekben) mellett szigorú auditkötelezettséget ír elő a nagy kockázatú rendszerekre – a toborzástól az igazságszolgáltatásig. Az átláthatóság és a kötelező emberi felügyelet követelménye azt hivatott garantálni, hogy a gép mindvégig az ember eszköze maradjon, ne pedig önkényes bírája."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Milyen elvre épül az Európai Unió Mesterséges Intelligencia Rendelete (AI Act)?", [
                    "Kockázatalapú megközelítésre: a minimális kockázatútól a nagy kockázatún át a tiltott rendszerekig terjedő szintekkel.",
                    "A mesterséges intelligencia teljes és feltétel nélküli betiltására az egész kontinensen.",
                    "Minden fejlesztő kötelező adómentességére."
                ], 0, ["c1-mestersegesintelligencia-vocab"]),
                fb("grammar", "controlled", "A szigorú ellenőrzés indokolt, _____ (all the more so since / annál is inkább, mivel) az algoritmusok torzítása közvetlenül csorbíthatja az egyenlő bánásmód elvét.", "annál is inkább, mivel", "Strict oversight is justified, all the more so since algorithmic bias can directly infringe upon the principle of equal treatment.", ["c1-correlative-causal-adverbials"]),
                match("vocabulary", "controlled", [["AI Act", "európai uniós MI rendelet"], ["nagy kockázatú rendszer", "szigorúan auditált MI alkalmazás"], ["emberi felügyelet", "human-in-the-loop elv"], ["megfelelőségi audit", "szabályozási vizsgálat"]], ["c1-mestersegesintelligencia-vocab"]),
                fb("grammar", "practice", "A jogalkotó _____ a megfontolásból fakadóan lépett fel, hogy megelőzze a polgárok automatizált profilozását. (from that / abból)", "abból", "The legislator intervened arising from the consideration that automated profiling of citizens should be prevented.", ["c1-correlative-causal-adverbials"]),
                sb("grammar", "practice", ["A", "nagy", "kockázatú", "rendszereknél", "kötelező", "a", "független", "külső", "megfelelőségi", "audit."], ["A", "nagy", "kockázatú", "rendszereknél", "kötelező", "a", "független", "külső", "megfelelőségi", "audit."], "For high-risk systems, an independent external conformity audit is mandatory.", ["c1-correlative-causal-adverbials"]),
                dc("dialogue", [
                    {"speaker": "Vállalati jogász", "text": "Hogyan készüljünk fel az AI Act hatálybalépésére?"},
                    {"speaker": "Etikai auditor", "text": "A belső algoritmusok kockázati besorolásával és az adatkezelési _____ dokumentálásával."},
                ], ["átláthatóság", "eltitkolás", "megsemmisítés"], 0, ["c1-correlative-causal-adverbials"]),
                sw("production", [{"prompt": "Write a causal sentence explaining why algorithmic transparency is crucial in hiring.", "answer": "A toborzási algoritmusok átláthatósága elengedhetetlen, annál is inkább, mivel a tanító adatokban megbúvó tudattalan előítéletek rendszerszintű diszkriminációt konzerválhatnak a munkaerőpiacon."}], ["c1-correlative-causal-adverbials"]),
                mc("grammar", "check", "Melyik kifejezés kapcsol össze indoklást megerősítő kauzális viszonyt?", [
                    "annál is inkább, mivel",
                    "holott egyébként",
                    "noha egyáltalán"
                ], 0, ["c1-correlative-causal-adverbials"])
            ]
        },
        {
            "num": 3,
            "stem": f"c1-{slug}-03",
            "title": "Cognitive Automation, Labor Market Shifts & Reskilling",
            "grammar_title": "Assertive Evidentials and Epistemic Certainty in Economic Forecasting",
            "grammar_skill": "c1-assertive-evidential-markers",
            "goals": [
                "I can analyze labor market polarization, cognitive automation, and reskilling (*munkaerőpiaci polarizáció, kognitív automatizáció, átképzés*).",
                "I can employ assertive evidentials and epistemic certainty expressions (*a tények tanúsága szerint, bizonyítottnak tekinthető, kétségkívül*).",
                "I can evaluate economic structural shifts and the future of creative professions in Hungary."
            ],
            "vocab": [
                {"lemma": "munkaerőpiaci polarizáció", "translation": "labor market polarization", "pos": "expression"},
                {"lemma": "kognitív automatizáció", "translation": "cognitive automation", "pos": "expression"},
                {"lemma": "rutinfeladat", "translation": "routine task", "pos": "noun"},
                {"lemma": "átképzés", "translation": "reskilling, retraining", "pos": "noun"},
                {"lemma": "hozzáadott érték", "translation": "added value", "pos": "expression"},
                {"lemma": "termelékenységi ugrás", "translation": "productivity leap", "pos": "noun"},
                {"lemma": "munkanélküliség", "translation": "unemployment", "pos": "noun"},
                {"lemma": "strukturális átalakulás", "translation": "structural transformation", "pos": "expression"}
            ],
            "gr_text1": "Assertive evidentials convey epistemic authority and grounded empirical observations: `a kutatások tanúsága szerint` (according to the testimony of research), `kétségkívül` (undoubtedly), `bizonyítottnak tekinthető` (can be regarded as proven), and `szemmel láthatóan` (visibly / manifestly).",
            "gr_text2": "Example in socioeconomic debate: `A tények tanúsága szerint a generatív mesterséges intelligencia immár nem a fizikai munkaköröket, hanem a fehérgalléros és kreatív pozíciókat érinti a legközvetlenebbül`.",
            "gr_table": [
                ["A statisztikák tanúsága szerint a kognitív feladatok automatizálása felgyorsult.", "According to the testimony of statistics, the automation of cognitive tasks has accelerated."],
                ["Bizonyítottnak tekinthető, hogy a magas digitális kompetenciájú munkavállalók bérelőnyre tesznek szert.", "It can be regarded as proven that workers with high digital competence gain a wage premium."],
                ["Kétségkívül új oktatási stratégiára van szükség az átképzés ösztönzésére.", "Undoubtedly a new educational strategy is required to incentivize reskilling."]
            ],
            "world_story_seg": {
                "seg_slug": "automatizacio",
                "title": "A fehérgalléros fordulat: Munkaerőpiac és átképzés a kognitív forradalomban",
                "summary": "How generative AI fundamentally disrupts intellectual and white-collar occupations in Central Europe, requiring massive life-long learning and institutional reskilling.",
                "paragraphs": [
                    {"type": "narration", "text": "Míg a huszadik század ipari robotizációja az üzemcsarnokok futószalagjait és a fizikai munkát alakította át, addig a huszonegyedik század mesterséges intelligenciája az irodák íróasztalaihoz ült be. A szoftverfejlesztés, a jogi szövegezés, a pénzügyi elemzés és a grafikai tervezés világa egyaránt szembesült azzal, hogy az algoritmusok másodpercek alatt végzik el a rutinszerű intellektuális feladatokat."},
                    {"type": "narration", "text": "Közép-Európában ez a strukturális sokk kettős kihívást jelent: a magas hozzáadott értékű szolgáltatóközpontoknak (SSC) radikálisan feljebb kell lépniük az értékláncban, míg az oktatási rendszernek a mechanikus lexikális tudás helyett a kritikai gondolkodásra és az emberi intuícióra kell helyeznie a hangsúlyt. Az átképzés immár nem opció, hanem a gazdasági túlélés záloga."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Miben különbözik a generatív MI hatása a korábbi ipari forradalmaktól?", [
                    "Nem a fizikai kétkezi munkát, hanem a magasan képzett fehérgalléros és kreatív kognitív tevékenységeket érinti közvetlenül.",
                    "Hogy csak a mezőgazdasági termelőket érinti hátrányosan.",
                    "Hogy kizárólag a vasúti közlekedést automatizálja."
                ], 0, ["c1-mestersegesintelligencia-vocab"]),
                fb("grammar", "controlled", "A felmérések _____ szerint (according to the testimony / tanúsága) a cégek több mint fele már beépítette az MI-eszközöket a napi munkafolyamatokba.", "tanúsága", "According to the testimony of surveys, more than half of companies have already integrated AI tools into daily workflows.", ["c1-assertive-evidential-markers"]),
                match("vocabulary", "controlled", [["kognitív automatizáció", "szellemi munka gépesítése"], ["átképzés", "új készségek elsajátítása"], ["termelékenységi ugrás", "hatékonyság hirtelen növekedése"], ["munkaerőpiaci polarizáció", "szélső kategóriák szétválása"]], ["c1-mestersegesintelligencia-vocab"]),
                fb("grammar", "practice", "Tudományosan _____ tekinthető, hogy a sikeres alkalmazkodás kulcsa az emberi intuíció és az algoritmus szinergiája. (proven / bizonyítottnak)", "bizonyítottnak", "It can be regarded as scientifically proven that the key to successful adaptation is the synergy of human intuition and algorithm.", ["c1-assertive-evidential-markers"]),
                sb("grammar", "practice", ["A", "tények", "tanúsága", "szerint", "az", "élethosszig", "tartó", "tanulás", "elengedhetetlen."], ["A", "tények", "tanúsága", "szerint", "az", "élethosszig", "tartó", "tanulás", "elengedhetetlen."], "According to the testimony of facts, lifelong learning is indispensable.", ["c1-assertive-evidential-markers"]),
                dc("dialogue", [
                    {"speaker": "HR-vezető", "text": "Hogyan tartsuk meg a kollégákat az automatizáció korában?"},
                    {"speaker": "Tanácsadó", "text": "Célzott belső _____ programokkal, amelyek megtanítják a munkatársakat a promptolásra és az adatelemzésre."},
                ], ["átképzési", "büntetési", "elbocsátási"], 0, ["c1-assertive-evidential-markers"]),
                sw("production", [{"prompt": "Write an assertive evidential sentence about labor market disruption.", "answer": "A gazdasági mutatók tanúsága szerint a kognitív rutinmunkák automatizálása kétségkívül mélyreható átképzési hullámot tesz elkerülhetetlenné az európai munkaerőpiacon."}], ["c1-assertive-evidential-markers"]),
                mc("grammar", "check", "Melyik állítás tartalmaz episztemikus evidenciát jelölő formulát?", [
                    "A tapasztalatok tanúsága szerint a kreativitás nehezen automatizálható.",
                    "Ha a kreativitás automatizálható volna.",
                    "Bár a kreativitás nem automatizálható."
                ], 0, ["c1-assertive-evidential-markers"])
            ]
        },
        {
            "num": 4,
            "stem": f"c1-{slug}-04",
            "title": "Clinical AI Diagnostics & Digital Healthcare Innovation",
            "grammar_title": "Deliberative and Optative Subjunctive in Medical Decision Making",
            "grammar_skill": "c1-subjunctive-deliberative-optatives",
            "goals": [
                "I can analyze medical imaging, diagnostic AI, and clinical decision support (*képalkotás, radiológiai diagnosztika, klinikai döntéstámogatás*).",
                "I can employ deliberative and optative subjunctive structures (*bármiként alakuljon is, legyen szó akár... akár, elengedhetetlen, hogy biztosítsák*).",
                "I can debate patient safety, algorithmic false negatives, and personalized oncology in Budapest hospitals."
            ],
            "vocab": [
                {"lemma": "orvosi képalkotás", "translation": "medical imaging", "pos": "expression"},
                {"lemma": "radiológiai diagnosztika", "translation": "radiological diagnostics", "pos": "expression"},
                {"lemma": "korai felismerés", "translation": "early detection", "pos": "expression"},
                {"lemma": "klinikai döntéstámogatás", "translation": "clinical decision support", "pos": "expression"},
                {"lemma": "betegbiztonság", "translation": "patient safety", "pos": "noun"},
                {"lemma": "személyre szabott medicina", "translation": "personalized medicine", "pos": "expression"},
                {"lemma": "adatvédelem", "translation": "data protection, HIPAA/GDPR", "pos": "noun"},
                {"lemma": "validáció", "translation": "clinical validation", "pos": "noun"}
            ],
            "gr_text1": "Deliberative and evaluative subjunctive structures weigh complex ethical considerations: `bármiként alakuljon is a technológiai fejlődés` (however technological development unfolds), `legyen szó akár korai daganatszűrésről, akár CT-elemzésről` (whether it concerns early tumor screening or CT analysis), and `elengedhetetlen, hogy az orvos mondja ki a végső szót` (it is essential that the physician pronounce the final word).",
            "gr_text2": "This modal register ensures that deontic necessity, ethical caution, and professional responsibility are properly balanced in clinical discourse.",
            "gr_table": [
                ["Legyen szó akár mammográfiáról, akár tüdőszűrésről, az algoritmus jelentősen csökkenti a tévesztések számát.", "Be it about mammography or lung screening, the algorithm significantly reduces error rates."],
                ["Bármilyen kifinomult legyen is a szoftver, a végső diagnózis felállítása az orvos felelőssége marad.", "However sophisticated the software may be, establishing the final diagnosis remains the doctor's responsibility."],
                ["Kulcsfontosságú, hogy a klinikai validáció során szigorúan ellenőrizzék a betegbiztonsági szempontokat.", "It is crucial that during clinical validation they strictly verify patient safety aspects."]
            ],
            "world_story_seg": {
                "seg_slug": "orvoslas",
                "title": "A gépi szem a klinikán: Radiológia és orvosi mesterséges intelligencia Budapesten",
                "summary": "How Hungarian medical faculties (Semmelweis University) and health-tech spin-offs deploy deep learning to detect early-stage pathologies with superhuman accuracy.",
                "paragraphs": [
                    {"type": "narration", "text": "A Semmelweis Egyetem radiológiai klinikáin és a magyar egészségügyi startupok laborjaiban a mesterséges intelligencia nem a jövő ígérete, hanem a jelen életeket mentő valósága. A neurális hálózatok képesek több tízezer mellkasi röntgenfelvétel vagy agyi MRI-kép tizedmásodperc alatti átfésülésére, észrevéve az emberi szem számára szinte láthatatlan apró mikromeszesedéseket és elváltozásokat."},
                    {"type": "narration", "text": "Az orvosok azonban nem riválist, hanem fáradhatatlan asszisztenst látnak a szoftverben. Az algoritmus tehermentesíti a túlterhelt szakembereket a monotónia alól, lehetővé téve, hogy figyelmüket a bonyolult, kétes esetekre és a betegekkel való közvetlen emberi kapcsolattartásra fordítsák. A magyar orvosi MI-innováció a klinikai döntéstámogatás terén nemzetközi elismerést vívott ki."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Mi az orvosi képalkotó MI legfőbb klinikai haszna a diagnosztikában?", [
                    "A korai stádiumú kóros elváltozások megbízható felismerése és a radiológusok adminisztratív tehermentesítése.",
                    "A betegek azonnali és orvosi vizsgálat nélküli műtőbe küldése.",
                    "Az orvosi egyetemek bezárásának elősegítése."
                ], 0, ["c1-mestersegesintelligencia-vocab"]),
                fb("grammar", "controlled", "_____ szó akár tüdőszűrésről, akár agyi MRI-ről (Be it / Legyen), a gépi felismerés hatékonysága lenyűgöző.", "Legyen", "Be it about lung screening or brain MRI, the efficiency of machine recognition is impressive.", ["c1-subjunctive-deliberative-optatives"]),
                match("vocabulary", "controlled", [["radiológiai diagnosztika", "képalkotó vizsgálatok elemzése"], ["korai felismerés", "betegség időbeni szűrése"], ["klinikai döntéstámogatás", "orvost segítő szoftveres javaslat"], ["betegbiztonság", "páciens védelmének prioritása"]], ["c1-mestersegesintelligencia-vocab"]),
                fb("grammar", "practice", "Bármiként _____ is a technológiai fejlődés, a döntés etikai terhe mindig az orvosé marad. (unfold / alakuljon)", "alakuljon", "However technological development unfolds, the ethical burden of decision always remains with the doctor.", ["c1-subjunctive-deliberative-optatives"]),
                sb("grammar", "practice", ["A", "klinikai", "validáció", "nélkül", "nem", "alkalmazható", "orvosi", "döntéstámogató", "rendszer."], ["A", "klinikai", "validáció", "nélkül", "nem", "alkalmazható", "orvosi", "döntéstámogató", "rendszer."], "Without clinical validation, no medical decision support system may be applied.", ["c1-subjunctive-deliberative-optatives"]),
                dc("dialogue", [
                    {"speaker": "Főorvos", "text": "Hogyan győzzük meg a kételkedő kollégákat az MI használatáról?"},
                    {"speaker": "Klinikai kutató", "text": "Független tesztekkel kell bizonyítani, hogy a szoftver minimalizálja a téves _____ kockázatát."},
                ], ["negatív", "színű", "hangú"], 0, ["c1-subjunctive-deliberative-optatives"]),
                sw("production", [{"prompt": "Write a deliberative subjunctive sentence on medical AI ethics.", "answer": "Bármilyen megbízható legyen is a diagnosztikai neurális hálózat, elengedhetetlen, hogy a végső terápiás döntést mindig az orvos hozza meg a beteg személyes beleegyezésével."}], ["c1-subjunctive-deliberative-optatives"]),
                mc("grammar", "check", "Melyik szerkezet fejez ki mérlegelő vagy megengedő kötőmódot?", [
                    "Bármiként alakuljon is a helyzet",
                    "Mivel úgy alakult a helyzet",
                    "Amikor alakul a helyzet"
                ], 0, ["c1-subjunctive-deliberative-optatives"])
            ]
        },
        {
            "num": 5,
            "stem": f"c1-{slug}-05",
            "title": "Artificial General Intelligence (AGI), Alignment & Digital Epistemology",
            "grammar_title": "Contrastive Focus Inversion in Existential and Epistemic AI Debate",
            "grammar_skill": "c1-adv-contrastive-focus-inversion",
            "goals": [
                "I can analyze Artificial General Intelligence, the alignment problem, and existential risks (*AGI, összehangolás, kontrollprobléma*).",
                "I can apply contrastive focus syntactic inversion (*nem a technológia jelenti a veszélyt, hanem a felelősség hiánya*).",
                "I can synthesize philosophical implications of superintelligence and epistemic autonomy in fluent Hungarian."
            ],
            "vocab": [
                {"lemma": "általános mesterséges intelligencia", "translation": "Artificial General Intelligence (AGI)", "pos": "expression"},
                {"lemma": "összehangolási probléma", "translation": "alignment problem (AI values and human intent)", "pos": "expression"},
                {"lemma": "egzisztenciális kockázat", "translation": "existential risk", "pos": "expression"},
                {"lemma": "digitális szuverenitás", "translation": "digital sovereignty", "pos": "expression"},
                {"lemma": "önvezérlő ágens", "translation": "autonomous agent", "pos": "noun"},
                {"lemma": "szingularitás", "translation": "technological singularity", "pos": "noun"},
                {"lemma": "antropomorfizáció", "translation": "anthropomorphism", "pos": "noun"},
                {"lemma": "kontrollprobléma", "translation": "control problem", "pos": "noun"}
            ],
            "gr_text1": "Contrastive focus inversion in Hungarian moves the emphasized argument directly before the finite verb, leaving the negated counter-argument in post-verbal position or in a paired *nem... hanem...* clause: `Nem a gép intellektusa fenyegeti az emberiséget, hanem a saját értékeink tisztázatlansága` (It is not the machine's intellect that threatens humanity, but the lack of clarity in our own values).",
            "gr_text2": "This syntactic clefting and inversion sharpens polemical debates surrounding superintelligence, shifting attention from sensationalism to structural governance.",
            "gr_table": [
                ["Nem a technológia gyorsulása okozza a válságot, hanem az etikai kontroll lemaradása.", "It is not the acceleration of technology that causes the crisis, but the falling behind of ethical control."],
                ["Nem csupán gazdasági versenyről van szó, hanem magáról az emberi méltóság jövőjéről.", "It is not merely an economic competition, but about the future of human dignity itself."],
                ["Nem az intelligencia hiánya az akadály, hanem a célfüggvények hibás megfogalmazása.", "It is not the lack of intelligence that is the obstacle, but the faulty formulation of objective functions."]
            ],
            "world_story_seg": {
                "seg_slug": "jovo",
                "title": "A Prometheus-pillanat: Szingularitás, összehangolás és az emberi autonómia",
                "summary": "Exploring the existential questions of Artificial General Intelligence, the value alignment dilemma, and how humanity retains moral agency in an automated world.",
                "paragraphs": [
                    {"type": "narration", "text": "Amikor a mesterséges általános intelligencia (AGI) távoli elméleti hipotézisből kézzelfogható mérnöki célkitűzéssé lépett elő, az emberiség saját Prometheus-pillanatával szembesült. A kérdés immár nem az, hogy képesek vagyunk-e nálunk gyorsabb és sokoldalúbb digitális elméket alkotni, hanem az, hogy képesek leszünk-e ezek céljait az emberi virágzás és túlélés egyetemes értékeihez igazítani."},
                    {"type": "narration", "text": "Ez az úgynevezett összehangolási (alignment) probléma: hogyan kódolható a szilíciumba az empátia, az igazságosság és az élet védelme? A digitális korszak legnagyobb kihívása nem technikai, hanem filozófiai. Neumann János, Stanislaw Lem és a kortárs gondolkodók tanítása szerint a gépek tükröt tartanak elénk: annak az intelligenciának a határait mutatják meg, amelyet végső soron nekünk magunknak kell felelősen irányítanunk."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Mit jelent az 'összehangolási probléma' (alignment problem) az AGI kutatásban?", [
                    "Annak biztosítását, hogy a szuperintelligens rendszerek céljai és cselekedetei maradéktalanul összhangban legyenek az emberi értékekkel és túléléssel.",
                    "A számítógépek képernyőjének vízszintbe állítását.",
                    "Az összes jelszó egyformára változtatását."
                ], 0, ["c1-mestersegesintelligencia-vocab"]),
                fb("grammar", "controlled", "Nem a szilícium autonómiája jelenti az igazi veszélyt, _____ (but rather / hanem) az emberi felelősségvállalás hiánya.", "hanem", "It is not the autonomy of silicon that poses the real danger, but rather the lack of human assumption of responsibility.", ["c1-adv-contrastive-focus-inversion"]),
                match("vocabulary", "controlled", [["AGI", "általános mesterséges intelligencia"], ["szingularitás", "technológiai ugrópont"], ["antropomorfizáció", "emberi tulajdonságok téves vetítése a gépre"], ["kontrollprobléma", "szuperintelligens rendszerek irányíthatósága"]], ["c1-mestersegesintelligencia-vocab"]),
                fb("grammar", "practice", "Nem csupán technológiai kihívással állunk szemben, hanem _____ (specifically / sokkal inkább) egzisztenciális önmeghatározási dilemmával.", "sokkal inkább", "We are facing not merely a technological challenge, but much rather an existential dilemma of self-definition.", ["c1-adv-contrastive-focus-inversion"]),
                sb("grammar", "practice", ["Nem", "a", "technológia", "irányítja", "az", "embert,", "hanem", "az", "emberi", "döntés", "formálja", "a", "technológiát."], ["Nem", "a", "technológia", "irányítja", "az", "embert,", "hanem", "az", "emberi", "döntés", "formálja", "a", "technológiát."], "It is not technology that directs man, but human decision that shapes technology.", ["c1-adv-contrastive-focus-inversion"]),
                dc("dialogue", [
                    {"speaker": "Filozófus", "text": "Féljünk-e az általános mesterséges intelligencia eljövetelétől?"},
                    {"speaker": "Informatikus", "text": "Nem a félelem a megoldás, hanem az értékek szigorú és etikus _____ a modellekbe."},
                ], ["beépítése", "kiirtása", "felejtése"], 0, ["c1-adv-contrastive-focus-inversion"]),
                sw("production", [{"prompt": "Write a contrastive focus sentence about the alignment challenge of AGI.", "answer": "Nem a gépi számítási kapacitás növekedése hordozza az egzisztenciális fenyegetést, hanem a gépi célfüggvények és az alapvető emberi értékek szétválása."}], ["c1-adv-contrastive-focus-inversion"]),
                mc("grammar", "check", "Melyik mondat alkalmaz kontrasztív fókuszt és szórendi inverziót?", [
                    "Nem az algoritmus önmagában a veszély, hanem az emberi kontroll feladása.",
                    "Az algoritmus egy veszélyes dolog, mert az ember feladta a kontrollt.",
                    "Ha feladjuk a kontrollt, az algoritmus veszélyessé válhat."
                ], 0, ["c1-adv-contrastive-focus-inversion"])
            ]
        }
    ]

    for l in disc_lessons:
        emit_instructional_lesson(15, "discourse", l, disc_title, disc_intro if l["num"] == 1 else None)

    # Combined Discourse World Story
    write_json(
        f"stories/world/c1/c1-{slug}.json",
        {
            "id": f"story.c1.{slug}",
            "title": "A szilícium ígérete és felelőssége: Mesterséges intelligencia Magyarországon és Európában",
            "level": "C1",
            "type": "world",
            "order": 15,
            "lesson": 5,
            "estimatedMinutes": 8,
            "summary": "Panoramic exploration of artificial intelligence in Hungarian science and European governance: from foundation model research at SZTAKI and the Komondor supercomputer, the landmark regulations of the EU AI Act, cognitive labor automation, life-saving clinical radiology at Semmelweis University, to the ultimate philosophical frontier of AGI alignment and human autonomy.",
            "grammar": [
                "c1-discourse-limiting-particles",
                "c1-correlative-causal-adverbials",
                "c1-assertive-evidential-markers",
                "c1-subjunctive-deliberative-optatives",
                "c1-adv-contrastive-focus-inversion"
            ],
            "vocabularyTopics": [
                "AI Ethics, Neural Networks & Technological Sovereignty",
                "Foundation Models & Hungarian Computing Research",
                "Algorithmic Bias, Transparency & the EU AI Act",
                "Cognitive Automation, Labor Market Shifts & Reskilling",
                "Clinical AI Diagnostics & Digital Healthcare Innovation",
                "Artificial General Intelligence (AGI), Alignment & Digital Epistemology"
            ],
            "paragraphs": [
                {"type": "narration", "text": "A mesterséges intelligencia megjelenése a huszonegyedik században olyan mérföldkő az emberiség történetében, amely a tűz feltalálásához vagy a könyvnyomtatás forradalmához mérhető. Magyarország e technológiai átalakulásban nem passzív megfigyelőként kíván jelen lenni: Neumann János szellemi örökösei a SZTAKI és a hazai egyetemek műhelyeiben, a debreceni Komondor szuperszámítógép segítségével azért küzdenek, hogy anyanyelvünk digitálisan is szuverén maradjon a globális technológiai terekben."},
                {"type": "narration", "text": "Európa mindeközben a jog és az etika fegyverével formálja a jövőt: a brüsszeli AI Act megmutatta a világnak, hogy a haladás nem járhat az emberi méltóság és a diszkriminációmentesség feladásával. A nagy kockázatú algoritmusok szigorú auditálása és az átláthatóság megkövetelése garanciát jelent a polgárok számára."},
                {"type": "narration", "text": "A gazdaságban a fehérgalléros munka kognitív automatizációja gyökeres szemléletváltást követel: az oktatásnak a száraz lexikális adatok helyett a kritikai gondolkodásra és az emberi intuícióra kell építenie, lehetővé téve a dolgozók élethosszig tartó átképzését."},
                {"type": "narration", "text": "Az orvostudományban a mélytanulási algoritmusok immár mindennapi valósággá váltak: a budapesti Semmelweis Egyetem klinikáin és a hazai orvostechnológiai műhelyekben a gépi látás korai stádiumban fedi fel a daganatos elváltozásokat, emberi életeket mentve és tehermentesítve a radiológusokat."},
                {"type": "narration", "text": "A legvégső kérdés azonban filozófiai jellegű: az általános mesterséges intelligencia (AGI) küszöbén állva az emberiségnek el kell döntenie, hogyan hangolja össze a gépi célokat a saját túlélésének és virágzásának értékeivel. Nem a szilícium felett kell győzedelmeskednünk, hanem saját etikai felelősségünket kell bizonyítanunk: garantálva, hogy az intelligens gépek mindvégig az emberiséget és az egyetemes humánumot szolgálják."}
            ]
        }
    )

    # Discourse Consolidation
    emit_consolidation_lesson(
        15,
        "discourse",
        f"c1-{slug}-consolidation",
        disc_title,
        [
            "I can analyze foundation model research and Hungarian supercomputer infrastructure (SZTAKI, Komondor).",
            "I can evaluate EU AI Act compliance tiers, cognitive automation, and healthcare AI diagnostics.",
            "I can synthesize debates on AGI value alignment, epistemic autonomy, and technological sovereignty."
        ],
        [
            mc("grammar", "recognize", "Milyen funkciót töltenek be a 'kiváltképp', 'éppenséggel' partikulák az akadémiai szövegekben?", [
                "Pontosítják, elhatárolják és fókuszálják az állítások érvényességi körét.",
                "Kizárólag kérdő mondatok végén állhatnak.",
                "Tagadást fejeznek ki."
            ], 0, ["c1-discourse-limiting-particles"]),
            mc("grammar", "recognize", "Hogyan emel ki egy ellenpontozó állítást a kontrasztív fókusz inverziója?", [
                "A hangsúlyozott elemet közvetlenül a véges ige elé helyezi, miközben a 'nem... hanem...' szerkezettel élesen szembeállítja az alternatívákat.",
                "Eltünteti az összes igét a mondatból.",
                "Minden szót ábécérendbe állít."
            ], 0, ["c1-adv-contrastive-focus-inversion"]),
            match("vocabulary", "recognize", [["SZTAKI", "magyar kutatóhálózat"], ["AI Act", "európai horizontális MI szabályozás"], ["emberi felügyelet", "human-in-the-loop alapelv"], ["radiológiai diagnosztika", "képalkotó orvosi elemzés"], ["összehangolási probléma", "AGI és emberi értékek harmóniája"]], ["c1-mestersegesintelligencia-vocab"]),
            fb("vocabulary", "recall", "A magyar nyelv sajátos szerkezete miatt a hazai digitális _____ megőrzése kiemelt feladat. (sovereignty / szuverenitás)", "szuverenitás", "Due to the unique structure of the Hungarian language, preserving domestic digital sovereignty is a priority task.", ["c1-mestersegesintelligencia-vocab"]),
            fb("vocabulary", "recall", "Az Európai Unió rendelete szigorú auditot követel meg a nagy _____ rendszerektől. (high-risk / kockázatú)", "kockázatú", "The European Union regulation demands strict audits from high-risk systems.", ["c1-mestersegesintelligencia-vocab"]),
            fb("grammar", "recall", "A digitális szabályozás kulcsfontosságú, _____ is inkább, mivel az algoritmusok polgárok millióinak életét befolyásolják. (all the / annál)", "annál", "Digital regulation is crucial, all the more so since algorithms influence the lives of millions of citizens.", ["c1-correlative-causal-adverbials"]),
            fb("grammar", "context", "A felmérések tanúsága _____ a szellemi munkakörök átalakulása már megkezdődött. (according to / szerint)", "szerint", "According to the testimony of surveys, the transformation of intellectual occupations has already begun.", ["c1-assertive-evidential-markers"]),
            fb("grammar", "context", "Bármiként _____ is a modellek pontossága, a klinikai felelősség az orvosé. (unfold / alakuljon)", "alakuljon", "However the accuracy of models unfolds, clinical responsibility belongs to the doctor.", ["c1-subjunctive-deliberative-optatives"]),
            mc("grammar", "context", "Mi a lényege a 'nem a technológia, hanem az etika' típusú megfogalmazásoknak?", [
                "Kontrasztív fókusszal rámutatnak arra, hogy az igazi döntési pont nem a gép képességeiben, hanem az emberi erkölcsi felelősségben rejlik.",
                "Hogy a gépeket tilos bekapcsolni.",
                "Hogy a mérnököknek nincs szükségük diplomára."
            ], 0, ["c1-adv-contrastive-focus-inversion"]),
            sb("grammar", "produce", ["A", "mesterséges", "intelligencia", "az", "emberi", "virágzást", "és", "méltóságot", "kell", "hogy", "szolgálja."], ["A", "mesterséges", "intelligencia", "az", "emberi", "virágzást", "és", "méltóságot", "kell", "hogy", "szolgálja."], "Artificial intelligence must serve human flourishing and dignity.", ["c1-subjunctive-deliberative-optatives"]),
            sw("production", [{"prompt": "Write a synthesized argument on European AI regulation balancing innovation and human rights.", "answer": "Az Európai Unió AI Act szabályozása nem az innováció elfojtását célozza, hanem kiváltképp azt szavatolja, hogy a technológiai fejlődés szilárd etikai korlátok és emberi felügyelet mellett szolgálja a társadalom javát."}], ["c1-correlative-causal-adverbials"]),
            sw("production", [{"prompt": "Formulate a concluding thought on artificial intelligence and human agency.", "answer": "Nem a szilícium autonómiája dönti el a jövőt, hanem az emberiség erkölcsi érettsége: a mesterséges intelligencia valódi mércéje az, hogy mennyire képes gazdagítani és megóvni a humánus értékeket."}], ["c1-adv-contrastive-focus-inversion"])
        ]
    )

    print("=== Finished C1 Unit 15 ===")


if __name__ == "__main__":
    generate_unit_15()
