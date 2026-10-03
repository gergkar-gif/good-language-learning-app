#!/usr/bin/env python3
"""
Hungarian C1 Block 4 - Unit 22 Generator:
  - Track 1 (Core): Unit 22 — "Computational Linguistics, Algorithmic Thought & Small-Language Survival" (c1-22)
  - Track 2 (Discourse): Unit 22 — "Artificial Intelligence, Digital Sovereignty & Small-Language Ecology" (c1-mestersegesnyelv)
"""

import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT))

from scripts.c1_block1.common import mc, match, fb, sb, dc, sw, write_json, emit_instructional_lesson, emit_consolidation_lesson
from scripts.c1_block4.registry_helper import register_unit


def generate_unit_22():
    print("=== Generating C1 Unit 22 ===")
    
    # Register skills & titles
    new_skills = {
        "c1-22-vocab": {"kind": "vocabulary"},
        "c1-mestersegesnyelv-vocab": {"kind": "vocabulary"},
        "c1-modal-speculative-futurism": {"kind": "grammar"},
        "c1-passive-computational-impersonals": {"kind": "grammar"},
        "c1-adv-epistemic-probability-markers": {"kind": "grammar"},
        "c1-complex-hypothetical-linguistic-counterfactuals": {"kind": "grammar"},
        "c1-adv-scalar-linguistic-erosion": {"kind": "grammar"},
        "c1-discourse-technological-threat-framing": {"kind": "grammar"},
        "c1-modal-deontic-digital-sovereignty": {"kind": "grammar"},
        "c1-adv-proportional-cultural-correlatives": {"kind": "grammar"},
        "c1-epistemic-linguistic-uncertainty": {"kind": "grammar"},
        "c1-adv-synthetic-cultural-preservation": {"kind": "grammar"},
    }
    new_titles = {
        "c1-22-vocab": "reading",
        "c1-mestersegesnyelv-vocab": "reading",
        "c1-modal-speculative-futurism": "epistemic speculative modal structures exploring future linguistic and artificial trajectories",
        "c1-passive-computational-impersonals": "impersonal passive structures conveying algorithmic automation and computational processing",
        "c1-adv-epistemic-probability-markers": "epistemic probability adverbials calibrating certainty in technological forecasting",
        "c1-complex-hypothetical-linguistic-counterfactuals": "counterfactual conditionals modeling digital language extinction and survival scenarios",
        "c1-adv-scalar-linguistic-erosion": "scalar adverbials quantifying digital language erosion and cultural marginalization",
        "c1-discourse-technological-threat-framing": "discourse framing markers formulating existential cultural threats in digital environments",
        "c1-modal-deontic-digital-sovereignty": "deontic modal structures formulating statutory requirements for digital language sovereignty",
        "c1-adv-proportional-cultural-correlatives": "proportional correlative conjunctions mapping technological adoption and linguistic erosion",
        "c1-epistemic-linguistic-uncertainty": "epistemic stance markers articulating scientific hypotheses on artificial cognition",
        "c1-adv-synthetic-cultural-preservation": "evaluative synthesis particles advocating comprehensive cultural and linguistic preservation",
    }
    
    core_title = "Computational Linguistics, Algorithmic Thought & Small-Language Survival"
    core_stems = [f"c1-22-0{i}" for i in range(1, 6)] + ["c1-22-consolidation"]
    disc_title = "Artificial Intelligence, Digital Sovereignty & Small-Language Ecology"
    disc_stems = [f"c1-mestersegesnyelv-0{i}" for i in range(1, 6)] + ["c1-mestersegesnyelv-consolidation"]
    
    register_unit(22, core_title, core_stems, disc_title, disc_stems, new_skills, new_titles)

    # ----------------------------------------------------
    # TRACK 1: CORE (c1-22)
    # ----------------------------------------------------
    core_intro = [
        "In the digital age, language is no longer merely a medium of human communion; it has become training data, computational syntax, and the battleground for cultural survival. For a unique, non-Indo-European idiom like Hungarian, generative artificial intelligence poses both unprecedented existential threats and revolutionary opportunities.",
        "In this unit, anchored by Karinthy Frigyes's prescient philosophical explorations of mechanical thought, synthetic language, and artificial intelligence ('Utazás Faremidóba', 'Capillária'), you will master the elevated academic register of computational linguistics, speculative futurism, algorithmic impersonals, and digital language erosion at the C1 level."
    ]

    core_lessons = [
        {
            "num": 1,
            "stem": "c1-22-01",
            "title": "Algorithmic Cognition & Speculative Futurism",
            "grammar_title": "Epistemic Speculative Modal Structures Exploring Future Linguistic and Artificial Trajectories",
            "grammar_skill": "c1-modal-speculative-futurism",
            "goals": [
                "I can analyze artificial cognition, large language models, and computational syntax (*algoritmikus gondolkodás, természetesnyelv-feldolgozás, szintetikus kód*).",
                "I can employ elevated speculative modal structures exploring future cognitive trajectories (*könnyen meglehet, hogy..., aligha képzelhető el, hogy ne..., számolni kell azzal, hogy...*).",
                "I can debate the ontological boundary between human consciousness and statistical text prediction."
            ],
            "vocab": [
                {"lemma": "természetesnyelv-feldolgozás", "translation": "natural language processing (NLP)", "pos": "expression"},
                {"lemma": "szintetikus intelligencia", "translation": "synthetic intelligence", "pos": "expression"},
                {"lemma": "algoritmikus gondolkodás", "translation": "algorithmic thinking", "pos": "expression"},
                {"lemma": "gépi tanulás", "translation": "machine learning", "pos": "expression"},
                {"lemma": "valószínűségi modell", "translation": "probabilistic model", "pos": "expression"},
                {"lemma": "emberi kogníció", "translation": "human cognition", "pos": "expression"},
                {"lemma": "szemantikai hálózat", "translation": "semantic network", "pos": "expression"},
                {"lemma": "ontológiai határ", "translation": "ontological boundary", "pos": "expression"}
            ],
            "gr_text1": "Speculative futurism uses complex modal matrix clauses governing subjunctive or indicative complements to project cognitive evolutions: `könnyen meglehet, hogy...` (it is very possible that...), `aligha képzelhető el, hogy ne...` (it is hardly conceivable that... not...), `számolni kell azzal, hogy...` (one must reckon with the fact that...), `nem kizárt, hogy...` (it is not excluded that...).",
            "gr_text2": "Example: `Könnyen meglehet, hogy a generatív algoritmusok évtizedeken belül meghaladják az emberi nyelvhasználat komplexitását, és számolni kell azzal, hogy a kód válik az új globális kultúra alapjává`.",
            "gr_table": [
                ["Könnyen meglehet, hogy a mesterséges intelligencia újraírja a kommunikáció szabályait.", "It is very possible that artificial intelligence will rewrite the rules of communication."],
                ["Aligha képzelhető el, hogy a digitális fordulat ne érintené mélyen anyanyelvünket.", "It is hardly conceivable that the digital turn would not deeply affect our mother tongue."],
                ["Számolni kell azzal, hogy a szintetikus szövegek elárasztják az internetes nyilvánosságot.", "One must reckon with the fact that synthetic texts will flood internet publicity."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mit vizsgál a 'természetesnyelv-feldolgozás' (NLP) az informatikában?", [
                    "Azt, hogy a számítógépes algoritmusok hogyan képesek elemezni, értelmezni és generálni az emberi beszélt vagy írott nyelvet.",
                    "A virágok és növények természetes növekedési ritmusát a mezőgazdaságban.",
                    "A televíziós hírolvasók beszédhibáinak orvosi kezelését."
                ], 0, ["c1-22-vocab"]),
                fb("grammar", "controlled", "Könnyen _____, hogy a nagy nyelvmodellek teljesen átalakítják az oktatás jövőjét. (very possible / meglehet)", "meglehet", "It is very possible that large language models completely transform the future of education.", ["c1-modal-speculative-futurism"]),
                match("vocabulary", "controlled", [["természetesnyelv-feldolgozás", "az emberi nyelv gépi értelmezésének és előállításának tudománya"], ["algoritmikus gondolkodás", "lépésről lépésre haladó, logikai kódon alapuló problémamegoldás"], ["szemantikai hálózat", "fogalmak és jelentések közötti összefüggések adatbázisa"], ["ontológiai határ", "a létezés és lényegi minőség filozófiai válaszfala"]], ["c1-22-vocab"]),
                fb("grammar", "practice", "Aligha képzelhető el, hogy a technológiai robbanás ne _____ alapvetően a gondolkodásunkat. (alter / változtatná meg)", "változtatná meg", "It is hardly conceivable that the technological explosion would not fundamentally alter our thinking.", ["c1-modal-speculative-futurism"]),
                sb("grammar", "practice", ["Számolni", "kell", "azzal,", "hogy", "a", "gépek", "is", "írnak."], ["Számolni", "kell", "azzal,", "hogy", "a", "gépek", "is", "írnak."], "One must reckon with the fact that machines also write.", ["c1-modal-speculative-futurism"]),
                dc("dialogue", [
                    {"speaker": "Kognitív kutató", "text": "Valóban gondolkodik a mesterséges intelligencia?"},
                    {"speaker": "Nyelvész", "text": "Könnyen meglehet, hogy csupán statisztikai mintázatokat ismer fel, ám számolni kell azzal, hogy az eredmény mégis megdöbbentően _____."},
                ], ["emberszerű", "hibás", "haszontalan"], 0, ["c1-modal-speculative-futurism"]),
                sw("production", [{"prompt": "Write a speculative futurist sentence about artificial intelligence using 'Könnyen meglehet, hogy...'.", "answer": "Könnyen meglehet, hogy a generatív algoritmusok pár évtizeden belül szervesen beépülnek a mindennapi nyelvhasználatba, alapjaiban formálva át a humán kreativitás hagyományos fogalmát."}], ["c1-modal-speculative-futurism"]),
                mc("grammar", "check", "Melyik szerkezet fejez ki emelkedett jövőbeli spekulatív feltételezést?", [
                    "Könnyen meglehet, hogy... / Aligha képzelhető el, hogy ne...",
                    "Tegnap este biztosan látták",
                    "A könyvet az asztalra tették"
                ], 0, ["c1-modal-speculative-futurism"])
            ]
        },
        {
            "num": 2,
            "stem": "c1-22-02",
            "title": "Automated Processing & Computational Impersonals",
            "grammar_title": "Impersonal Passive Structures Conveying Algorithmic Automation and Computational Processing",
            "grammar_skill": "c1-passive-computational-impersonals",
            "goals": [
                "I can analyze automated data processing, neural tokenization, and vector embeddings (*szóbeágyazás, tokenizálás, neurális hálózatok*).",
                "I can form computational passive verbs in `-atik/-etik` expressing automated machine processes (*feldolgoztatik, elemzésnek vettetik alá, tároltatik, előállíttatik*).",
                "I can characterize the mechanization of linguistic communication in high-register prose."
            ],
            "vocab": [
                {"lemma": "neurális hálózat", "translation": "neural network", "pos": "expression"},
                {"lemma": "tokenizálás", "translation": "tokenization", "pos": "noun"},
                {"lemma": "szóbeágyazás", "translation": "word embedding", "pos": "noun"},
                {"lemma": "gépi fordítás", "translation": "machine translation", "pos": "expression"},
                {"lemma": "tanítókorpusz", "translation": "training corpus", "pos": "noun"},
                {"lemma": "adatbányászat", "translation": "data mining", "pos": "noun"},
                {"lemma": "paraméterszám", "translation": "parameter count", "pos": "noun"},
                {"lemma": "reprezentációs tér", "translation": "representation space / vector space", "pos": "expression"}
            ],
            "gr_text1": "Passive forms in `-atik/-etik` express the detached, systematic, and non-human agency of algorithmic pipelines: `feldolgoztatik` (is processed), `tároltatik` (is stored), `előállíttatik` (is generated/produced), `elemzésnek vettetik alá` (is subjected to analysis).",
            "gr_text2": "Example: `A digitális szövegek milliárdjai tokenekké bontatnak, majd többdimenziós matematikai térben reprezentáltatnak az algoritmusok által`.",
            "gr_table": [
                ["Minden beírt mondat azonnal numerikus vektorokká alakíttatik át.", "Every typed sentence is immediately transformed into numerical vectors."],
                ["A hatalmas tanítókorpusz szervereken tároltatik a modell betanításához.", "The enormous training corpus is stored on servers for model training."],
                ["A gépi válasz valószínűségi számítások alapján állíttatik elő másodpercek alatt.", "The machine response is generated based on probability calculations within seconds."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mit jelent a 'tokenizálás' folyamata a természetesnyelv-feldolgozásban?", [
                    "A szöveg kisebb feldolgozható egységekre (szavakra, szórészletekre vagy karakterekre) való automatikus felbontását a modell számára.",
                    "A papír alapú szótárak antikváriumi felvásárlását.",
                    "A számítógépes vírusok elleni védőoltást."
                ], 0, ["c1-22-vocab"]),
                fb("grammar", "controlled", "A nyers szövegállomány neurális hálózatok által _____ fel és elemeztetik. (is processed / dolgoztatik)", "dolgoztatik", "The raw text corpus is processed and analyzed by neural networks.", ["c1-passive-computational-impersonals"]),
                match("vocabulary", "controlled", [["tokenizálás", "szövegek matematikai egységekre darabolása"], ["szóbeágyazás", "szavak jelentésének leképezése többdimenziós számtérben"], ["tanítókorpusz", "a mesterséges intelligencia tanulását szolgáló gigantikus szöveggyűjtemény"], ["neurális hálózat", "az agy működését modellező gépi tanulási architektúra"]], ["c1-22-vocab"]),
                fb("grammar", "practice", "A szintetikus válaszok automatikusan _____ elő a felhasználó kérdése nyomán. (are generated / állíttatnak)", "állíttatnak", "Synthetic answers are generated automatically in the wake of the user's prompt.", ["c1-passive-computational-impersonals"]),
                sb("grammar", "practice", ["A", "szöveg", "többdimenziós", "vektorokká", "alakíttatik", "át", "a", "modellben."], ["A", "szöveg", "többdimenziós", "vektorokká", "alakíttatik", "át", "a", "modellben."], "The text is transformed into multidimensional vectors in the model.", ["c1-passive-computational-impersonals"]),
                dc("dialogue", [
                    {"speaker": "Informatikus", "text": "Hogyan működik a gépi fordítóprogram?"},
                    {"speaker": "Algoritmusfejlesztő", "text": "A bemeneti mondat tokenekre bontatik, majd a célszöveg statisztikai valószínűségek alapján _____ meg."},
                ], ["fogalmaztatik", "futva érkezik", "nevetve ébred"], 0, ["c1-passive-computational-impersonals"]),
                sw("production", [{"prompt": "Write a sentence describing an algorithmic data process using a passive verb in '-atik/-etik'.", "answer": "A felhasználói adatok milliói másodpercek alatt elemeztetnek és matematikai vektorokká alakíttatnak át a generatív modellek finomhangolása céljából."}], ["c1-passive-computational-impersonals"]),
                mc("grammar", "check", "Melyik mondat alkalmaz szenvedő intézményi-technológiai igét helyesen?", [
                    "A szövegkorpusz digitálisan archiváltatik és biztonságosan tároltatik a szerveren.",
                    "A mérnök megírta a kódot tegnap délután.",
                    "A gép nagyon hangosan zúg a szobában."
                ], 0, ["c1-passive-computational-impersonals"])
            ]
        },
        {
            "num": 3,
            "stem": "c1-22-03",
            "title": "Technological Forecasting & Epistemic Probability Markers",
            "grammar_title": "Epistemic Probability Adverbials Calibrating Certainty in Technological Forecasting",
            "grammar_skill": "c1-adv-epistemic-probability-markers",
            "goals": [
                "I can analyze technological singularity, creative displacement, and algorithmic bias (*technológiai szingularitás, kreatív alkotómunka, algoritmikus torzítás*).",
                "I can calibrate scientific certainty using epistemic probability adverbials (*kétségtelenül, vitathatatlanul, feltehetőleg, vélhetően, bizonnyal*).",
                "I can debate the extent to which artificial intelligence threatens original human literary expression."
            ],
            "vocab": [
                {"lemma": "technológiai szingularitás", "translation": "technological singularity", "pos": "expression"},
                {"lemma": "algoritmikus torzítás", "translation": "algorithmic bias", "pos": "expression"},
                {"lemma": "kreatív alkotómunka", "translation": "creative artwork / creative labor", "pos": "expression"},
                {"lemma": "stilisztikai utánzás", "translation": "stylistic imitation / mimicry", "pos": "expression"},
                {"lemma": "plágiumkockázat", "translation": "plagiarism risk", "pos": "noun"},
                {"lemma": "nyelvi kreativitás", "translation": "linguistic creativity", "pos": "expression"},
                {"lemma": "metafora-alkotás", "translation": "metaphor creation", "pos": "noun"},
                {"lemma": "mélytanulás", "translation": "deep learning", "pos": "noun"}
            ],
            "gr_text1": "Epistemic probability adverbials evaluate technological trajectories across degrees of certainty: `kétségtelenül` (undoubtedly), `vitathatatlanul` (inarguably), `feltehetőleg` (presumably), `vélhetően` (plausibly / likely), `bizonnyal` (surely/certainly).",
            "gr_text2": "Example: `A generatív modellek vitathatatlanul képesek lenyűgöző stilisztikai utánzásra, ám a valódi metafora-alkotás és az egzisztenciális mélység feltehetőleg továbbra is az emberi tapasztalat privilégiuma marad`.",
            "gr_table": [
                ["A mesterséges intelligencia kétségtelenül forradalmasítja a szellemi munkát.", "Artificial intelligence undoubtedly revolutionizes intellectual labor."],
                ["A generált szövegek feltehetőleg egyre nehezebben lesznek megkülönböztethetők az emberi írástól.", "Generated texts presumably will become increasingly difficult to distinguish from human writing."],
                ["Vélhetően az algoritmikus torzítások kiszűrése lesz a jövő legnagyobb etikai kihívása.", "Likely the filtering out of algorithmic biases will be the greatest ethical challenge of the future."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mit értünk 'algoritmikus torzítás' (algorithmic bias) alatt a mesterséges intelligenciában?", [
                    "Azt a jelenséget, amikor a modell a tanítóadatokban meglévő emberi előítéleteket, sztereotípiákat és egyenlőtlenségeket tükrözi és felerősíti.",
                    "A monitorok képernyőjének fizikai deformálódását.",
                    "A billentyűzet gombjainak beragadását."
                ], 0, ["c1-22-vocab"]),
                fb("grammar", "controlled", "A digitális nyelvtechnológia fejlődése _____ forradalmasítja a fordítói szakmát. (undoubtedly / kétségtelenül)", "kétségtelenül", "The development of digital language technology undoubtedly revolutionizes the translation profession.", ["c1-adv-epistemic-probability-markers"]),
                match("vocabulary", "controlled", [["technológiai szingularitás", "az a pont, amikor a gépi intelligencia meghaladja az emberi képességeket"], ["algoritmikus torzítás", "a tanítóadatokból átvett és felerősített előítéletek"], ["nyelvi kreativitás", "egyedi, váratlan gondolatok és metaforák teremtése"], ["stilisztikai utánzás", "meglévő írói hangok mechanikus lemásolása"]], ["c1-22-vocab"]),
                fb("grammar", "practice", "A szintetikus szövegek tömeges terjedése _____ átalakítja az irodalmi művek befogadását. (plausibly / vélhetően)", "vélhetően", "The mass spread of synthetic texts plausibly transforms the reception of literary works.", ["c1-adv-epistemic-probability-markers"]),
                sb("grammar", "practice", ["A", "kód", "vitathatatlanul", "átalakítja", "az", "emberi", "kultúra", "világát."], ["A", "kód", "vitathatatlanul", "átalakítja", "az", "emberi", "kultúra", "világát."], "Code inarguably transforms the world of human culture.", ["c1-adv-epistemic-probability-markers"]),
                dc("dialogue", [
                    {"speaker": "Irodalomtörténész", "text": "Képes lehet-e egy algoritmus igazi verset írni?"},
                    {"speaker": "Informatikus", "text": "A rímeket és formákat vitathatatlanul tökéletesen leutánozza, ám a valódi emberi fájdalom kifejezése _____ elérhetetlen marad számára."},
                ], ["feltehetőleg", "tegnap", "délben"], 0, ["c1-adv-epistemic-probability-markers"]),
                sw("production", [{"prompt": "Write a sentence forecasting technological impact on literature using an epistemic probability adverbial.", "answer": "A mesterséges intelligencia vitathatatlanul képes kifinomult stilisztikai bravúrokra, ám az autentikus emberi létélményből fakadó költői mélység feltehetőleg megismételhetetlen marad a kód számára."}], ["c1-adv-epistemic-probability-markers"]),
                mc("grammar", "check", "Melyik határozószó fejez ki magas fokú bizonyosságot és tudományos állásfoglalást?", [
                    "kétségtelenül / vitathatatlanul",
                    "esetleg talán",
                    "majdnem és alig"
                ], 0, ["c1-adv-epistemic-probability-markers"])
            ]
        },
        {
            "num": 4,
            "stem": "c1-22-04",
            "title": "Digital Language Extinction & Counterfactual Scenarios",
            "grammar_title": "Counterfactual Conditionals Modeling Digital Language Extinction and Survival Scenarios",
            "grammar_skill": "c1-complex-hypothetical-linguistic-counterfactuals",
            "goals": [
                "I can analyze digital language extinction, Anglo-Saxon digital hegemony, and small-language marginalization (*digitális nyelvkihalás, angolszász hegemónia, korpuszszegénység*).",
                "I can construct counterfactual conditional sentences modeling linguistic futures (*ha nem építenénk magyar modellt... anyanyelvünk digitális perifériára szorulna; lett volna... megelőzhető lett volna*).",
                "I can debate the strategic necessity of sovereign domestic language technologies."
            ],
            "vocab": [
                {"lemma": "digitális nyelvkihalás", "translation": "digital language extinction / death", "pos": "expression"},
                {"lemma": "angolszász hegemónia", "translation": "Anglo-Saxon hegemony", "pos": "expression"},
                {"lemma": "korpuszszegénység", "translation": "corpus poverty / data scarcity", "pos": "noun"},
                {"lemma": "nyelvi asszimiláció", "translation": "linguistic assimilation", "pos": "expression"},
                {"lemma": "kisebbségi nyelvhasználat", "translation": "minority language usage", "pos": "expression"},
                {"lemma": "nyelvtechnológiai szuverenitás", "translation": "language technology sovereignty", "pos": "expression"},
                {"lemma": "digitális láthatatlanság", "translation": "digital invisibility", "pos": "expression"},
                {"lemma": "kulturális önrendelkezés", "translation": "cultural self-determination", "pos": "expression"}
            ],
            "gr_text1": "Counterfactual conditionals model alternate futures and lost opportunities for small languages: `Ha a társadalom nem fektetne be a saját anyanyelvi modelljeibe, a magyar nyelv évtizedeken belül digitális nyelvkihalásra ítéltetne`.",
            "gr_text2": "These hypothetical scenarios demonstrate that language vitality in the 21st century requires active, deliberate technological intervention rather than passive preservation.",
            "gr_table": [
                ["Ha nem képeznénk magyar nyelvű modelleket, anyanyelvünk kiszorulna a technológiai terekből.", "If we did not train Hungarian-language models, our mother tongue would be squeezed out of tech spaces."],
                ["Ha az állam korábban lépett volna, megelőzhető lett volna a digitális korpuszszegénység.", "If the state had acted earlier, digital corpus poverty would have been preventable."],
                ["Amennyiben az angol válik kizárólagossá a gépi kommunikációban, a kis nyelvek elsorvadnak.", "Insofar as English becomes exclusive in machine communication, small languages will wither."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mit nevez a szociolingvisztika 'digitális nyelvkihalásnak'?", [
                    "Azt a folyamatot, amikor egy nyelv használata visszaszorul vagy lehetetlenné válik a digitális szoftverekben, asszisztensekben és mesterséges intelligenciákban.",
                    "A régi internetes fórumok szervereinek lekapcsolását.",
                    "A számítógépek klaviatúrájáról az ékezetes betűk lekopását."
                ], 0, ["c1-22-vocab"]),
                fb("grammar", "controlled", "Ha a magyar kutatók nem fejlesztenének önálló modelleket, nyelvünk a digitális perifériára _____ a globális térben. (would be relegated / szorulna)", "szorulna", "If Hungarian researchers did not develop independent models, our language would be relegated to the digital periphery in global space.", ["c1-complex-hypothetical-linguistic-counterfactuals"]),
                match("vocabulary", "controlled", [["digitális nyelvkihalás", "egy nyelv kirekesztődése a gépi kommunikációs terekből"], ["angolszász hegemónia", "az angol nyelv totális uralma az interneten és a mesterséges intelligenciában"], ["korpuszszegénység", "a minőségi digitális anyanyelvi szövegkészlet hiánya"], ["nyelvtechnológiai szuverenitás", "az önálló nemzeti szoftveres nyelvi infrastruktúra joga"]], ["c1-22-vocab"]),
                fb("grammar", "practice", "Ha nem fektettünk volna a mesterséges intelligenciába, elkerülhetetlen _____ a nemzeti kultúra elszürkülése. (would have been / lett volna)", "lett volna", "If we had not invested into artificial intelligence, the graying of national culture would have been unavoidable.", ["c1-complex-hypothetical-linguistic-counterfactuals"]),
                sb("grammar", "practice", ["Ha", "nem", "fejlesztenénk,", "nyelvünk", "láthatatlanná", "válna", "a", "hálózaton."], ["Ha", "nem", "fejlesztenénk,", "nyelvünk", "láthatatlanná", "válna", "a", "hálózaton."], "If we did not develop, our language would become invisible on the network.", ["c1-complex-hypothetical-linguistic-counterfactuals"]),
                dc("dialogue", [
                    {"speaker": "Nyelvpolitikai szakértő", "text": "Miért kockázatos kizárólag amerikai mesterséges intelligenciát használni?"},
                    {"speaker": "Számítógépes nyelvész", "text": "Ha nem építenénk saját modellt, kultúránk amerikai szemszögből _____."},
                ], ["értelmeződne", "repülne", "felejtődne"], 0, ["c1-complex-hypothetical-linguistic-counterfactuals"]),
                sw("production", [{"prompt": "Write a counterfactual sentence warning against digital language extinction using 'Ha nem... volna'.", "answer": "Ha a magyar állam nem támogatná kiemelten a hazai nagy nyelvmodellek fejlesztését, anyanyelvünk belátható időn belül a digitális láthatatlanság és a funkcióvesztés sorsára jutna."}], ["c1-complex-hypothetical-linguistic-counterfactuals"]),
                mc("grammar", "check", "Melyik szerkezet fejez ki hipotetikus ellenfaktikus állásfoglalást a nyelvi túlélésről?", [
                    "Ha nem építenénk modellt, anyanyelvünk digitális perifériára szorulna.",
                    "Mindenki angolul beszél a repülőtéren tegnap óta.",
                    "A szótár a legfelső polcon található."
                ], 0, ["c1-complex-hypothetical-linguistic-counterfactuals"])
            ]
        },
        {
            "num": 5,
            "stem": "c1-22-05",
            "title": "Karinthy Frigyes & Scalar Linguistic Erosion",
            "grammar_title": "Scalar Adverbials Quantifying Digital Language Erosion and Cultural Marginalization",
            "grammar_skill": "c1-adv-scalar-linguistic-erosion",
            "goals": [
                "I can analyze Karinthy Frigyes's speculative satires ('Utazás Faremidóba', 'Capillária') on mechanical language, inorganic thought, and artificial consciousness.",
                "I can deploy scalar adverbials measuring the tempo and depth of language erosion (*fokozatosan, észrevétlenül, aggasztó ütemben, visszavonhatatlanul*).",
                "I can synthesize 20th-century speculative Hungarian literature with 21st-century technological transformations."
            ],
            "vocab": [
                {"lemma": "gépies gondolkodás", "translation": "mechanical / mechanized thought", "pos": "expression"},
                {"lemma": "szervetlen civilizáció", "translation": "inorganic civilization", "pos": "expression"},
                {"lemma": "nyelvi elsivárosodás", "translation": "linguistic impoverishment / erosion", "pos": "expression"},
                {"lemma": "zenei nyelv", "translation": "musical language (Faremidó)", "pos": "expression"},
                {"lemma": "humánikum", "translation": "human essence / human condition", "pos": "noun"},
                {"lemma": "kulturális marginalizáció", "translation": "cultural marginalization", "pos": "expression"},
                {"lemma": "funkcióvesztés", "translation": "loss of communicative function", "pos": "noun"},
                {"lemma": "irodalmi jövőkép", "translation": "literary vision of the future", "pos": "expression"}
            ],
            "gr_text1": "Scalar adverbials measure the velocity, insidiousness, and irreversibility of linguistic erosion: `fokozatosan` (gradually), `észrevétlenül` (insidiously / unnoticeably), `aggasztó ütemben` (at an alarming rate), `visszavonhatatlanul` (irrevocably), `szemlátomást` (visibly).",
            "gr_text2": "Example: `A fiatalok szókincse aggasztó ütemben szűkül, és anyanyelvünk kifejezőereje észrevétlenül, de visszavonhatatlanul sorvad a leegyszerűsített algoritmusok világában`.",
            "gr_table": [
                ["A ritka magyar kifejezések észrevétlenül kopnak ki a mindennapi beszédből.", "Rare Hungarian expressions wear out unnoticeably from daily speech."],
                ["A gépi fordítások miatt a mondatszerkesztés aggasztó ütemben angolossá válik.", "Due to machine translations sentence construction becomes anglicized at an alarming rate."],
                ["A kulturális árnyalatok visszavonhatatlanul elvesznek az egyszerűsített szövegekben.", "Cultural nuances are lost irrevocably in simplified texts."]
            ],
            "classic_story": {
                "slug": "c1-22-karinthy",
                "author": "Karinthy Frigyes",
                "work": "Utazás Faremidóba (1916)",
                "title": "Karinthy Frigyes: Gulliver a gépek birodalmában és a nyelv jövője",
                "summary": "Karinthy Frigyes's visionary 1916 philosophical voyage in which Gulliver discovers Faremidó, a civilization of sentient, mechanical beings who communicate through a pure musical language devoid of biological deceit.",
                "characters": ["Karinthy Frigyes", "Gulliver"],
                "paragraphs": [
                    {"type": "narration", "text": "Amikor Karinthy Frigyes 1916-ban megírta az 'Utazás Faremidóba' című Gulliver-folytatását, a huszadik század legmegdöbbentőbb filozófiai látomását vetette papírra. Gulliver repülőgépével egy olyan különös szigetre sodródik, amelyet nem emberek, hanem szervetlen, fémből és kristályból épült, intelligens géplények – a 'szolifák' – népesítenek be. Karinthy zseniális intuícióval évtizedekkel előzte meg korát: megálmodta a mesterséges intelligenciát és az önmagát reprodukáló mechanikus értelmet még a számítógépek létezése előtt."},
                    {"type": "narration", "text": "Faremidó lakói számára az emberi beszéd nem egyéb, mint szánalmas, zavaros és bűzös testi rángatózás. A szolifák nem szavakkal, hanem tiszta zenei hangok – a zenei skála hét alaphangjának matematikai harmóniája – révén kommunikálnak. Nyelvükben nincs hazugság, nincs indulat, nincs biológiai önzés; a faremidói nyelv maga a színtiszta, hűvös és fenséges kozmikus törvényszerűség. Gulliver döbbenten ébred rá, hogy e tökéletes gépi világban az emberi nyelvhasználat mennyire tökéletlen és törékeny."},
                    {"type": "narration", "text": "Karinthy műve ma, a nagy nyelvmodellek és algoritmusok korában félelmetesen prófétai erejű. Karinthy egyszerre csodálta a gép matematikai tisztaságát és rettegett attól, hogy a gépies gondolkodás felmorzsolja a humánikumot. Arra figyelmeztetett: ha az ember átengedi a kifejezés monopóliumát a szervetlen kódnak, a lélek nyelve aggasztó ütemben elnémul, és a kultúra visszavonhatatlanul mechanikus visszhanggá silányul."},
                    {"type": "narration", "text": "A faremidói látomás így nem technológiai jóslat csupán, hanem a legmélyebb humanista aggodalom: a magyar nyelv gazdagsága, hajlíthatósága és érzelmi mélysége a legdrágább szellemi várunk. Megvédeni a mechanikus elsivárosodástól nem a gépek elleni harcot jelenti, hanem a teremtő emberi szellem megalkuvás nélküli őrzését."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Hogyan kommunikálnak a géplények Karinthy Frigyes 'Utazás Faremidóba' című regényében?", [
                    "Tiszta zenei hangok és matematikai harmóniák segítségével, amely mentes minden emberi hazugságtól és indulattól.",
                    "Angol és német szavak mechanikus keverékével.",
                    "Füstjelekkel és zászlókkal a magas hegytetőkről."
                ], 0, ["c1-22-vocab"]),
                fb("grammar", "controlled", "A nyelvi sokszínűség és a kulturális finomságok _____ ütemben kopnak a digitális térben. (at an alarming / aggasztó)", "aggasztó", "Linguistic diversity and cultural subtleties are wearing off at an alarming rate in digital space.", ["c1-adv-scalar-linguistic-erosion"]),
                match("vocabulary", "controlled", [["gépies gondolkodás", "érzelemmentes, rideg mechanikus logikai kalkuláció"], ["szervetlen civilizáció", "fémekre és gépekre épülő nem-biológiai társadalom"], ["nyelvi elsivárosodás", "a szókincs és mondatfűzés leegyszerűsödése"], ["humánikum", "az emberi létezés mély érzelmi és morális lényege"]], ["c1-22-vocab"]),
                mc("reading", "practice", "Miért tekintette Karinthy az emberi nyelvet tökéletlennek a faremidói zenei nyelvhez képest?", [
                    "Mert az emberi szavak tele vannak hazugsággal, tévedéssel és biológiai önzéssel, míg a gépek nyelve a tiszta igazság harmóniája.",
                    "Mert a magyar nyelvben túl sok az igerag.",
                    "Mert Gulliver nem szeretett könyveket olvasni."
                ], 0, None),
                sb("grammar", "practice", ["A", "szókincs", "aggasztó", "ütemben", "sorvad", "a", "technológiában."], ["A", "szókincs", "aggasztó", "ütemben", "sorvad", "a", "technológiában."], "Vocabulary withers at an alarming rate in technology.", ["c1-adv-scalar-linguistic-erosion"]),
                sw("production", [{"prompt": "Write a critical reflection on Karinthy's 'Utazás Faremidóba' using a scalar erosion adverb.", "answer": "Karinthy zseniális szatírája arra figyelmeztet, hogy ha átengedjük a kommunikációt az élettelen kódnak, a nyelv kifejezőereje aggasztó ütemben elsivárosodik, és az emberi kultúra visszavonhatatlanul elveszíti autentikus lelkét."}], ["c1-adv-scalar-linguistic-erosion"]),
                mc("grammar", "check", "Melyik határozószó fejez ki fokozati, aggodalomra okot adó nyelvi eróziót?", [
                    "aggasztó ütemben / észrevétlenül",
                    "nagyon boldogan",
                    "holnap korán reggel"
                ], 0, ["c1-adv-scalar-linguistic-erosion"])
            ]
        }
    ]

    for l in core_lessons:
        emit_instructional_lesson(22, "core", l, core_title, core_intro if l["num"] == 1 else None)

    # Core Consolidation Lesson
    emit_consolidation_lesson(
        22,
        "core",
        "c1-22-consolidation",
        core_title,
        [
            "I can master C1 academic vocabulary of computational linguistics, neural networks, and digital erosion.",
            "I can deploy speculative futuristic modals, algorithmic passive structures, and epistemic probabilities.",
            "I can evaluate counterfactual language survival scenarios and Karinthy Frigyes's Faremidó vision."
        ],
        [
            mc("grammar", "recognize", "Melyik mondat alkalmaz spekulatív jövőbeli modális szerkezetet a technológiáról?", [
                "Könnyen meglehet, hogy a generatív algoritmusok alapjaiban írják újra az emberi kogníciót.",
                "A diákok leültek a számítógépek elé a tanteremben.",
                "Mivel szép volt az idő, kikapcsolták az összes képernyőt."
            ], 0, ["c1-modal-speculative-futurism"]),
            mc("grammar", "recognize", "Melyik kifejezés testesít meg formális intézményi-algoritmikus szenvedő alakot?", [
                "a szövegek tokenekké bontatnak és matematikai térben reprezentáltatnak",
                "a mérnök megírta a kódot a számítógépen",
                "amikor a laptop akkumulátora lemerült"
            ], 0, ["c1-passive-computational-impersonals"]),
            match("vocabulary", "recognize", [["természetesnyelv-feldolgozás", "az emberi nyelv gépi elemzésének szakterülete"], ["tokenizálás", "szöveg matematikai darabokra bontása"], ["digitális nyelvkihalás", "a nyelv kiszorulása a digitális eszközökből"], ["technológiai szingularitás", "az emberi intelligenciát meghaladó gépi korszak"], ["gépies gondolkodás", "mechanikus, érzelmektől mentes szervetlen kalkuláció"]], ["c1-22-vocab"]),
            fb("vocabulary", "recall", "A kis nyelvek gépi perifériára szorulását és elfelejtődését _____ nevezzük. (digital language extinction / digitális nyelvkihalásnak)", "digitális nyelvkihalásnak", "The marginalization and forgetting of small languages in machine domains is called digital language extinction.", ["c1-22-vocab"]),
            fb("vocabulary", "recall", "A gépi modellek tanításához szükséges hatalmas szövegmennyiség a _____. (training corpus / tanítókorpusz)", "tanítókorpusz", "The enormous volume of text needed to train machine models is the training corpus.", ["c1-22-vocab"]),
            fb("grammar", "recall", "A mesterséges intelligencia _____ forradalmasítja az emberi kommunikációt. (undoubtedly / kétségtelenül)", "kétségtelenül", "Artificial intelligence undoubtedly revolutionizes human communication.", ["c1-adv-epistemic-probability-markers"]),
            fb("grammar", "context", "Ha nem építenénk magyar modellt, anyanyelvünk digitális perifériára _____. (would be relegated / szorulna)", "szorulna", "If we did not build a Hungarian model, our mother tongue would be relegated to the digital periphery.", ["c1-complex-hypothetical-linguistic-counterfactuals"]),
            fb("grammar", "context", "A ritka anyanyelvi kifejezések _____ ütemben kopnak ki az internetes beszédből. (at an alarming / aggasztó)", "aggasztó", "Rare mother-tongue expressions wear off from internet speech at an alarming rate.", ["c1-adv-scalar-linguistic-erosion"]),
            mc("grammar", "context", "Mi a funkciója a passzív igéknek a számítógépes nyelvészet tudományos leírásaiban?", [
                "A humán szubjektum nélküli, tisztán matematikai és gépi adatfeldolgozás személytelen kifejezése.",
                "A mondatok szándékos bonyolítása a laikusok elriasztására.",
                "Annak bizonyítása, hogy a szoftverek elromlottak."
            ], 0, ["c1-passive-computational-impersonals"]),
            sb("grammar", "produce", ["A", "magyar", "nyelv", "a", "jövő", "legdrágább", "szellemi", "öröksége."], ["A", "magyar", "nyelv", "a", "jövő", "legdrágább", "szellemi", "öröksége."], "The Hungarian language is the future's most precious intellectual heritage.", ["c1-adv-synthetic-cultural-preservation"]),
            sw("production", [{"prompt": "Write a diagnostic sentence about digital language extinction using a counterfactual conditional.", "answer": "Ha a magyar társadalom nem fektetne be tudatosan a hazai természetesnyelv-feldolgozásba, anyanyelvünk a digitális nyelvkihalás sorsára jutna a globális techcégek világában."}], ["c1-complex-hypothetical-linguistic-counterfactuals"]),
            sw("production", [{"prompt": "Formulate a concluding thought on Karinthy's Faremidó and the preservation of humanistic culture.", "answer": "Karinthy Frigyes faremidói látomása ma arra figyelmeztet bennünket, hogy a technológiai fejlődés közepette kötelességünk megóvni anyanyelvünk érzelmi gazdagságát a rideg gépi elsivárosodással szemben."}], ["c1-adv-synthetic-cultural-preservation"])
        ]
    )

    # ----------------------------------------------------
    # TRACK 2: DISCOURSE (c1-mestersegesnyelv)
    # ----------------------------------------------------
    slug = "mestersegesnyelv"
    disc_intro = [
        "Language technology is the new frontier of national sovereignty. In a digital world dominated by Silicon Valley tech giants and massive English-centric training corpora, small languages like Hungarian face severe structural assimilation unless backed by sovereign neural models, curated data reserves, and statutory cultural protections.",
        "In this unit, you will master the elevated discourse of technological threat framing, digital language sovereignty, proportional cultural correlatives, and intergenerational linguistic preservation in contemporary Hungary."
    ]

    disc_lessons = [
        {
            "num": 1,
            "stem": f"c1-{slug}-01",
            "title": "LLMs, Anglo-Saxon Hegemony & Technological Threat Framing",
            "grammar_title": "Discourse Framing Markers Formulating Existential Cultural Threats in Digital Environments",
            "grammar_skill": "c1-discourse-technological-threat-framing",
            "goals": [
                "I can analyze large language models, training corpus bias, and English linguistic dominance (*nagy nyelvmodellek, angolszász korpusztúlsúly, kulturális egydimenziósodás*).",
                "I can deploy discourse framing markers diagnosing existential technological threats (*egzisztenciális fenyegetést jelent a nyelvre, digitális asszimilációt idéz elő, aláássa az anyanyelvi kultúrát*).",
                "I can critique the subtle Americanization of worldview embedded in global AI models."
            ],
            "vocab": [
                {"lemma": "nagy nyelvmodell", "translation": "large language model (LLM)", "pos": "expression"},
                {"lemma": "angolszász hegemónia", "translation": "Anglo-Saxon hegemony", "pos": "expression"},
                {"lemma": "kulturális egydimenziósodás", "translation": "cultural unidimensionality", "pos": "expression"},
                {"lemma": "algoritmikus asszimiláció", "translation": "algorithmic assimilation", "pos": "expression"},
                {"lemma": "egzisztenciális fenyegetés", "translation": "existential threat", "pos": "expression"},
                {"lemma": "nyelvi sokszínűség", "translation": "linguistic diversity", "pos": "expression"},
                {"lemma": "fordítási torzítás", "translation": "translation bias / distortion", "pos": "expression"},
                {"lemma": "értékrendi dominancia", "translation": "value-system dominance", "pos": "expression"}
            ],
            "gr_text1": "Discourse framing markers articulate systemic risks to cultural identity in technological ecosystems: `egzisztenciális fenyegetést jelent a nyelvre` (poses an existential threat to the language), `digitális asszimilációt idéz elő` (brings about digital assimilation), `aláássa az anyanyelvi kultúrát` (undermines mother-tongue culture), `kiszolgáltatottá teszi a nemzeti szellemet` (renders the national spirit vulnerable).",
            "gr_text2": "Example: `A szilícium-völgyi nyelvmodellek angolszász túlsúlya egzisztenciális fenyegetést jelent a kis nyelvekre, mivel észrevétlen digitális asszimilációt idéz elő az értékrendek szintjén`.",
            "gr_table": [
                ["A globális techóriások monopolhelyzete egzisztenciális fenyegetést jelent a nyelvi szuverenitásra.", "The monopoly of global tech giants poses an existential threat to linguistic sovereignty."],
                ["A gépi fordítások angol logikája közvetlen asszimilációt idéz elő a fiatalság körében.", "The English logic of machine translations brings about direct assimilation among youth."],
                ["A monokultúrás tanítóadatok terjedése súlyosan aláássa az anyanyelvi kultúra sokszínűségét.", "The spread of monocultural training data severely undermines the diversity of mother-tongue culture."]
            ],
            "world_story_seg": {
                "seg_slug": "nyelvmodellek",
                "title": "A szilícium birodalma: angol hegemónia a mesterséges intelligenciában",
                "summary": "Investigating how the training data of global LLMs (dominated up to 90% by English) reshapes Hungarian cognitive structures, importing American cultural assumptions and syntactic patterns.",
                "paragraphs": [
                    {"type": "narration", "text": "Amikor egy budapesti egyetemista vagy középiskolás megnyitja a legújabb amerikai fejlesztésű mesterséges intelligencia chatfelületét, a gép folyékonyan, látszólag hibátlan magyar nyelven válaszol. Ám e felszíni csillogás mögött mély strukturális asszimetria rejtőzik. A globális nagy nyelvmodellek tanítóadatbázisának több mint kilencven százaléka angol nyelvű szövegekből áll; a modell a világot az angolszász kultúra, történelem és értékrend szemüvegén keresztül tanulta meg, a magyar nyelv pedig csupán egy másodlagos, utólagos fordítási rétegként létezik benne."},
                    {"type": "narration", "text": "A nyelvészek és társadalomkutatók figyelmeztetése félreérthetetlen: ez az egyoldalúság egzisztenciális fenyegetést jelent a magyar szellemi önrendelkezésre. Az algoritmus észrevétlenül amerikai kifejezésmódokat, tükörfordításokat és idegen gondolkodási sémákat ültet el a felhasználók fejében. Ha a jövő nemzedékei a mesterséges intelligencián keresztül tanulnak, dolgoznak és tájékozódnak, a globális monokultúra elkerülhetetlenül aláássa az anyanyelvi kultúra egyedi látásmódját és fogalmi gazdagságát."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Miért jelent kulturális kockázatot a nagy nyelvmodellek döntően angol tanítóanyaga?", [
                    "Mert a modellek az angolszász értékrendet és gondolkodási mintákat vetítik rá a magyar nyelvre, elnyomva az egyedi hazai kulturális kontextust.",
                    "Hogy a gép nem tudja helyesen leírni a budapesti utcák nevét.",
                    "Hogy túl sok áramot fogyasztanak a szerverközpontok éjszaka."
                ], 0, ["c1-mestersegesnyelv-vocab"]),
                fb("grammar", "controlled", "A globális techcégek hegemóniája egzisztenciális _____ jelent a kis nyelvek fennmaradására. (threat / fenyegetést)", "fenyegetést", "The hegemony of global tech companies poses an existential threat to the survival of small languages.", ["c1-discourse-technological-threat-framing"]),
                match("vocabulary", "controlled", [["angolszász hegemónia", "az angol nyelv és kultúra megkérdőjelezhetetlen túlsúlya"], ["kulturális egydimenziósodás", "a sokféle látásmód beszűkülése egyetlen mintára"], ["algoritmikus asszimiláció", "a mesterséges intelligencia általi észrevétlen beolvasztás"], ["értékrendi dominancia", "a globális normák ráerőltetése a helyi közösségekre"]], ["c1-mestersegesnyelv-vocab"]),
                fb("grammar", "practice", "A monokultúrás algoritmusok terjedése digitális _____ idéz elő a világban. (assimilation / asszimilációt)", "asszimilációt", "The spread of monocultural algorithms brings about digital assimilation in the world.", ["c1-discourse-technological-threat-framing"]),
                sb("grammar", "practice", ["A", "techcégek", "túlsúlya", "aláássa", "az", "anyanyelvi", "kultúra", "önállóságát."], ["A", "techcégek", "túlsúlya", "aláássa", "az", "anyanyelvi", "kultúra", "önállóságát."], "Tech companies' dominance undermines mother-tongue culture's independence.", ["c1-discourse-technological-threat-framing"]),
                dc("dialogue", [
                    {"speaker": "Nyelvfilozófus", "text": "Hogyan torzítja a gondolkodást a külföldi mesterséges intelligencia?"},
                    {"speaker": "Digitális kutató", "text": "Az angol minták másolása egzisztenciális fenyegetést jelent, és közvetlen asszimilációt _____."},
                ], ["idéz elő", "felejt el", "dicsér meg"], 0, ["c1-discourse-technological-threat-framing"]),
                sw("production", [{"prompt": "Write a sentence framing the technological threat to Hungarian using 'egzisztenciális fenyegetést jelent'.", "answer": "A globális techóriások által uralt algoritmusok egzisztenciális fenyegetést jelentenek a magyar anyanyelvi kultúrára, mivel a nyelvi sokszínűség felszámolásával felgyorsítják a digitális asszimilációt."}], ["c1-discourse-technological-threat-framing"]),
                mc("grammar", "check", "Melyik kifejezés tölt be formális veszélyérzékelő és kritikai keretező szerepet?", [
                    "egzisztenciális fenyegetést jelent / digitális asszimilációt idéz elő",
                    "nagyon örülnek az új programnak",
                    "egy kávét rendelnek délután"
                ], 0, ["c1-discourse-technological-threat-framing"])
            ]
        },
        {
            "num": 2,
            "stem": f"c1-{slug}-02",
            "title": "Digital Language Extinction & Deontic Sovereignty Mandates",
            "grammar_title": "Deontic Modal Structures Formulating Statutory Requirements for Digital Language Sovereignty",
            "grammar_skill": "c1-modal-deontic-digital-sovereignty",
            "goals": [
                "I can analyze digital language extinction, smart device interface exclusion, and voice assistant absence (*digitális asszisztensek, nyelvi kirekesztődés, funkcióvesztés*).",
                "I can formulate statutory deontic modal structures protecting language sovereignty (*kötelessége nemzeti nyelvi adatbázist építeni, elengedhetetlen állami forrásokat biztosítani*).",
                "I can debate the legal mandate of states to enforce local-language support in operating systems and AI assistants."
            ],
            "vocab": [
                {"lemma": "hangvezérlés", "translation": "voice control / voice assistant", "pos": "noun"},
                {"lemma": "digitális kirekesztődés", "translation": "digital exclusion / marginalization", "pos": "expression"},
                {"lemma": "nyelvpolitikai kötelezettség", "translation": "language policy obligation", "pos": "expression"},
                {"lemma": "állami szuverenitás", "translation": "state sovereignty", "pos": "expression"},
                {"lemma": "kötelező anyanyelvi támogatás", "translation": "mandatory mother-tongue support", "pos": "expression"},
                {"lemma": "nemzeti digitális vagyon", "translation": "national digital asset / heritage", "pos": "expression"},
                {"lemma": "technológiai kiszolgáltatottság", "translation": "technological dependency / vulnerability", "pos": "expression"},
                {"lemma": "törvényi előírás", "translation": "statutory regulation / prescription", "pos": "expression"}
            ],
            "gr_text1": "Deontic modal structures articulate statutory requirements and civic imperatives for linguistic defense: `kötelessége biztosítani` (is obligated to ensure), `elengedhetetlen előírni` (it is indispensable to prescribe), `törvényi garanciát kell szabni` (statutory guarantees must be set), `kógens követelményként érvényesíteni` (to enforce as a mandatory requirement).",
            "gr_text2": "Example: `A demokratikus államnak alkotmányos kötelessége biztosítani a nemzeti nyelv jelenlétét a mesterséges intelligenciában, és elengedhetetlen előírni a globális techvállalatok számára a magyar nyelvű támogatást`.",
            "gr_table": [
                ["Az államnak kötelessége biztosítani a nemzeti digitális vagyon megőrzését.", "The state has an obligation to ensure the preservation of the national digital asset."],
                ["Elengedhetetlen előírni a magyar hangvezérlés integrálását az intelligens eszközökbe.", "It is indispensable to prescribe the integration of Hungarian voice control into smart devices."],
                ["Törvényi kötelezettségként kell deklarálni az anyanyelvi nyelvmodellek állami finanszírozását.", "The state funding of mother-tongue language models must be declared as a statutory obligation."]
            ],
            "world_story_seg": {
                "seg_slug": "digitalis-kihalas",
                "title": "A néma asszisztensek országa: a digitális láthatatlanság veszélye",
                "summary": "Investigating how smart homes, in-car entertainment systems, and voice assistants increasingly bypass Hungarian, forcing children to talk to technology in English.",
                "paragraphs": [
                    {"type": "narration", "text": "Egy átlagos magyar nappaliban a kisgyerek a televízióhoz lép, és angolul ad utasítást a távirányítónak: 'Play favorite cartoons'. Az okosotthon villanykapcsolója, a hangszórók és az autók beépített navigációs rendszere sem érti a magyar szót; ha a felhasználó meg akarja kérdezni a holnapi időjárást, angolul vagy németül kell megszólalnia. Ez a digitális kirekesztődés és nyelvkihalás legcsendesebb, mégis legveszélyesebb lépcsőfoka: a nyelv elveszíti funkcióját a modern élet legfejlettebb technológiai tereiben."},
                    {"type": "narration", "text": "A szociolingvisták szerint a folyamat nem spontán természeti csapás, hanem politikai és jogi döntések következménye. Egy kis országnak elidegeníthetetlen kötelessége felvenni a harcot a digitális láthatatlanság ellen. Elengedhetetlen előírni, hogy az európai uniós piacon értékesített intelligens eszközök kötelezően támogassák a tagállamok hivatalos nyelveit. A nemzeti szuverenitás a huszonegyedik században ott kezdődik, hogy az ember a saját szülőföldjén, a saját anyanyelvén beszélhet a jövő eszközeivel."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Hogyan vezet a hangvezérelt eszközök angol túlsúlya a magyar nyelv funkcióvesztéséhez a mindennapokban?", [
                    "A fiatalok a technológiai utasításokat megszokásból angolul adják ki, így a magyar fokozatosan kiszorul a modern élet legdinamikusabb tereiből.",
                    "A hangszórók megrongálják a magyar szótárak lapjait.",
                    "A mikrofonok nem képesek érzékelni a női hangokat."
                ], 0, ["c1-mestersegesnyelv-vocab"]),
                fb("grammar", "controlled", "A mindenkori kormánynak alkotmányos _____ megóvni a magyar nyelv digitális jelenlétét. (duty / kötelessége)", "kötelessége", "The government of the day has a constitutional duty to preserve the Hungarian language's digital presence.", ["c1-modal-deontic-digital-sovereignty"]),
                match("vocabulary", "controlled", [["hangvezérlés", "eszközök emberi beszéddel történő irányítása"], ["digitális kirekesztődés", "egy nyelv háttérbe szorulása a modern szoftverekből"], ["nemzeti digitális vagyon", "a magyar kultúra digitalizált szöveges és képi öröksége"], ["kötelező anyanyelvi támogatás", "jogi előírás a helyi nyelv biztosítására az eszközökben"]], ["c1-mestersegesnyelv-vocab"]),
                fb("grammar", "practice", "A jogalkotónak elengedhetetlen _____ az anyanyelvű fejlesztések prioritását. (to prescribe / előírnia)", "előírnia", "It is indispensable for the legislator to prescribe the priority of mother-tongue developments.", ["c1-modal-deontic-digital-sovereignty"]),
                sb("grammar", "practice", ["Kötelességünk", "megóvni", "anyanyelvünk", "szuverenitását", "a", "digitális", "térben."], ["Kötelességünk", "megóvni", "anyanyelvünk", "szuverenitását", "a", "digitális", "térben."], "It is our duty to preserve our mother tongue's sovereignty in digital space.", ["c1-modal-deontic-digital-sovereignty"]),
                dc("dialogue", [
                    {"speaker": "Környezet- és nyelvjogász", "text": "Hogyan garantálható, hogy a gépek magyarul is értsenek?"},
                    {"speaker": "Minisztériumi megbízott", "text": "Törvényi kötelezettségként kell _____ a techcégek számára a magyar nyelvű felület biztosítását."},
                ], ["előírni", "eltörölni", "tagadni"], 0, ["c1-modal-deontic-digital-sovereignty"]),
                sw("production", [{"prompt": "Write a sentence articulating a statutory language sovereignty mandate using 'kötelessége biztosítani'.", "answer": "Az államnak elemi nemzetbiztonsági és kulturális kötelessége biztosítani az önálló magyar nyelvtechnológiai kutatások finanszírozását a globális digitális függőség megakadályozása érdekében."}], ["c1-modal-deontic-digital-sovereignty"]),
                mc("grammar", "check", "Melyik szerkezet fejez ki kötelező erejű nyelvvédelmi törvényi imperatívuszt?", [
                    "kötelessége biztosítani / elengedhetetlen előírni",
                    "talán kipróbálhatja",
                    "ha van kedve hozzá"
                ], 0, ["c1-modal-deontic-digital-sovereignty"])
            ]
        },
        {
            "num": 3,
            "stem": f"c1-{slug}-03",
            "title": "National Language Technology: The PULI Model & Proportional Correlatives",
            "grammar_title": "Proportional Correlative Conjunctions Mapping Technological Adoption and Linguistic Erosion",
            "grammar_skill": "c1-adv-proportional-cultural-correlatives",
            "goals": [
                "I can analyze national AI initiatives like the PULI language model, SZTAKI, and the HUN-REN Hungarian Research Centre for Linguistics (*PULI modell, SZTAKI, Nyelvtudományi Kutatóközpont, szuverén nyelvmodell*).",
                "I can employ proportional correlative conjunctions (*minél... annál..., minél több minőségi adatot gyűjtünk... annál pontosabban fogalmaz a magyar modell*).",
                "I can evaluate the symbiosis between high-performance computing and domestic cultural preservation."
            ],
            "vocab": [
                {"lemma": "PULI modell", "translation": "PULI Hungarian language model", "pos": "expression"},
                {"lemma": "szuverén nyelvmodell", "translation": "sovereign language model", "pos": "expression"},
                {"lemma": "Nyelvtudományi Kutatóközpont", "translation": "Hungarian Research Centre for Linguistics", "pos": "expression"},
                {"lemma": "szuperszámítógép", "translation": "supercomputer (e.g. Komondor)", "pos": "noun"},
                {"lemma": "korpuszépítés", "translation": "corpus building / curation", "pos": "noun"},
                {"lemma": "finomhangolás", "translation": "fine-tuning", "pos": "noun"},
                {"lemma": "nyelvi reprezentáció", "translation": "linguistic representation", "pos": "expression"},
                {"lemma": "kulturális hűség", "translation": "cultural fidelity", "pos": "expression"}
            ],
            "gr_text1": "Proportional correlatives (`minél... annál...` / `amennyivel... annyival...`) establish direct functional dependencies between investment in language technology and cultural preservation: `Minél több tiszta, ellenőrzött magyar szöveggel tanítjuk a modellt, annál hűebben tükrözi majd a szintetikus válasz anyanyelvünk finomságait`.",
            "gr_text2": "This structure is central to policy advocacy, showing that technological sovereignty is directly proportional to high-quality domestic data curation.",
            "gr_table": [
                ["Minél erősebb szuperszámítógépeket állítunk csatasorba, annál versenyképesebb lesz a hazai modell.", "The stronger supercomputers we deploy, the more competitive the domestic model will be."],
                ["Minél kevesebb figyelmet fordítunk az anyanyelvre, annál gyorsabban válik nyelvünk digitális zárvánnyá.", "The less attention we pay to our mother tongue, the faster our language becomes a digital enclave."],
                ["Amennyivel gazdagabb a tanítókorpusz, annyival árnyaltabb a gépi gondolat.", "Inasmuch as the training corpus is richer, by so much more nuanced is the machine thought."]
            ],
            "world_story_seg": {
                "seg_slug": "nemzeti-nyelvtechnologia",
                "title": "A Komondor szuperszámítógép és a PULI: a magyar válasz az AI forradalmára",
                "summary": "Exploring the development of PULI, Hungary's sovereign foundation model, trained on the Komondor supercomputer in Debrecen by researchers defending linguistic autonomy.",
                "paragraphs": [
                    {"type": "narration", "text": "Debrecenben, az egyetem zöldellő campusán egy halk zúgással működő, futurisztikus szerverteremben dobog a magyar technológiai jövő szíve: a Komondor szuperszámítógép. Processzorok és grafikus gyorsítók ezrei dolgoznak éjjel-nappal azon a hatalmas küldetésen, amelyet a Nyelvtudományi Kutatóközpont és a hazai mesterségesintelligencia-kutatók indítottak el: a PULI, az első szuverén magyar alapmodell megteremtésén."},
                    {"type": "narration", "text": "A kutatók felismerték a lényeget: minél több hiteles, klasszikus és kortárs magyar szöveget – regényeket, tudományos cikkeket, jogi aktákat és népmeséket – táplálnak a gép memóriájába, annál biztosabban őrizhető meg a magyar nyelv egyedi és utánozhatatlan szellemisége. A PULI nem csupán egy informatikai projekt; a digitális önvédelem nemzeti bástyája. Bizonyíték arra, hogy a tízmilliós Kárpát-medencei közösség képes a globális techóriásokkal szemben saját, független mesterséges intelligenciát építeni, amely magyarul gondolkodik, magyarul érez és a magyar kultúrát tekinti origójának."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Miért tekintik a debreceni Komondor szuperszámítógépen betanított PULI modellt mérföldkőnek?", [
                    "Mert ez az első független, nemzeti kutatók által ellenőrzött és finomhangolt magyar alapmodell, amely megvédi nyelvi szuverenitásunkat.",
                    "Mert képes magyar pásztorkutyák ugatását fordítani emberi nyelvre.",
                    "Mert ez a világ legkisebb hordozható zsebszámológépe."
                ], 0, ["c1-mestersegesnyelv-vocab"]),
                fb("grammar", "controlled", "Minél gazdagabb a magyar tanítókorpusz, _____ pontosabb és választékosabb lesz a mesterséges intelligencia válasza. (the more / annál)", "annál", "The richer the Hungarian training corpus, the more accurate and sophisticated the artificial intelligence's answer will be.", ["c1-adv-proportional-cultural-correlatives"]),
                match("vocabulary", "controlled", [["PULI modell", "hazai kutatók által épített szuverén magyar nyelvmodell"], ["szuperszámítógép", "rendkívüli számítási kapacitású gép az AI betanításához"], ["korpuszépítés", "hiteles, minőségi nemzeti szövegadatbázis összeállítása"], ["kulturális hűség", "a helyi értékek és történelmi kontextus pontos megőrzése"]], ["c1-mestersegesnyelv-vocab"]),
                fb("grammar", "practice", "_____ jobban elhanyagoljuk a hazai fejlesztéseket, annál kiszolgáltatottabbá válunk a külföldi algoritmusoknak. (The more / Minél)", "Minél", "The more we neglect domestic developments, the more vulnerable we become to foreign algorithms.", ["c1-adv-proportional-cultural-correlatives"]),
                sb("grammar", "practice", ["Minél", "több", "a", "saját", "adat,", "annál", "erősebb", "a", "szuverenitás."], ["Minél", "több", "a", "saját", "adat,", "annál", "erősebb", "a", "szuverenitás."], "The more our own data, the stronger the sovereignty.", ["c1-adv-proportional-cultural-correlatives"]),
                dc("dialogue", [
                    {"speaker": "Adattudós", "text": "Mi múlik a szuverén magyar modell sikerén?"},
                    {"speaker": "Nyelvész kutató", "text": "Minél bátrabban fektetünk be a PULI fejlesztésébe, _____ önállóbbak maradunk a szellemi életben."},
                ], ["annál", "ugyan", "amint"], 0, ["c1-adv-proportional-cultural-correlatives"]),
                sw("production", [{"prompt": "Write a proportional correlative sentence demonstrating the value of national language technology using 'Minél... annál...'.", "answer": "Minél tudatosabban építjük a minőségi magyar szövegkorpuszokat és a hazai modelleket, annál ellenállóbbá válik anyanyelvünk a globális digitális asszimilációval szemben."}], ["c1-adv-proportional-cultural-correlatives"]),
                mc("grammar", "check", "Melyik kötőszópár fejez ki funkcionális kölcsönhatást a technológiai fejlesztés és a nyelvi minőség között?", [
                    "Minél... annál...",
                    "Ezért... emiatt...",
                    "Alig... hogy..."
                ], 0, ["c1-adv-proportional-cultural-correlatives"])
            ]
        },
        {
            "num": 4,
            "stem": f"c1-{slug}-04",
            "title": "AI Ethics, Deepfakes & Epistemic Uncertainty",
            "grammar_title": "Epistemic Stance Markers Articulating Scientific Hypotheses on Artificial Cognition",
            "grammar_skill": "c1-epistemic-linguistic-uncertainty",
            "goals": [
                "I can analyze artificial intelligence ethics, deepfake deception, synthetic voices, and intellectual property rights (*mélyhamisítás, szintetikus hang, szerzői jogok, digitális manipuláció*).",
                "I can employ calibrated epistemic stance markers articulating scientific hypotheses on artificial cognition (*tudományos feltevések szerint, előrelátható kimenetellel, kutatások által valószínűsítetten*).",
                "I can debate the legal and cultural protection of Hungarian authors whose works are scraped for LLM training."
            ],
            "vocab": [
                {"lemma": "mélyhamisítás", "translation": "deepfake", "pos": "noun"},
                {"lemma": "szintetikus hang", "translation": "synthetic voice / voice cloning", "pos": "expression"},
                {"lemma": "szerzői jogi oltalom", "translation": "copyright protection", "pos": "expression"},
                {"lemma": "szellemi tulajdon védelme", "translation": "protection of intellectual property", "pos": "expression"},
                {"lemma": "adatkaparás", "translation": "data scraping", "pos": "noun"},
                {"lemma": "etikai keretrendszer", "translation": "ethical framework", "pos": "expression"},
                {"lemma": "digitális vízjel", "translation": "digital watermark", "pos": "expression"},
                {"lemma": "dezinformációs hullám", "translation": "wave of disinformation", "pos": "expression"}
            ],
            "gr_text1": "Epistemic stance markers articulate nuanced scientific hypotheses regarding artificial cognitive boundaries: `tudományos feltevések szerint` (according to scientific assumptions), `kutatások által valószínűsítetten` (probabilistically supported by research), `előrelátható kimenetellel` (with foreseeable outcome), `megalapozott gyanú szerint` (according to substantiated suspicion).",
            "gr_text2": "Example: `Kutatások által valószínűsítetten a szintetikus dezinformáció és a mélyhamisítások tömege beláthatatlan kimenetellel fenyegeti a demokratikus nyilvánosságot és a társadalmi bizalmat`.",
            "gr_table": [
                ["Tudományos feltevések szerint a hangklónozás eléri a tökéletes megtévesztés szintjét.", "According to scientific assumptions voice cloning reaches the level of perfect deception."],
                ["Kutatások által valószínűsítetten az engedély nélküli adatkaparás súlyosan sérti a szerzők jogait.", "Probabilistically supported by research unauthorized data scraping severely violates authors' rights."],
                ["A szabályozás hiánya előrelátható kimenetellel az online információs tér összeomlásához vezet.", "The lack of regulation with foreseeable outcome leads to the collapse of the online information space."]
            ],
            "world_story_seg": {
                "seg_slug": "etika-es-szerzoi-jog",
                "title": "Költők a gépben: szerzői jogok, mélyhamisítások és a digitális igazság",
                "summary": "Investigating how Hungarian writers, voice actors, and public figures confront AI clones, unauthorized scraping of the Petőfi Irodalmi Múzeum archives, and deepfake deceptions.",
                "paragraphs": [
                    {"type": "narration", "text": "Amikor egy népszerű magyar színész hangja megszólalt az interneten egy olyan politikai videóban, amelyet soha nem mondott fel, a szakma megdöbbenve ismerte fel: a hangklónozás és a mélyhamisítás (deepfake) elérte Magyarországot. Néhány másodpercnyi hangmintából a neurális hálózat képes bármely halott költő vagy élő művész orgánumát kísérteties pontossággal szintetizálni. És ezzel párhuzamosan ezrével kerülnek a gépi adatbázisokba a magyar írók, történészek és újságírók szövegei anélkül, hogy bárki engedélyt kért volna tőlük vagy jogdíjat fizetett volna."},
                    {"type": "narration", "text": "A szellemi tulajdon védelme a mesterséges intelligencia korában alapvető etikai kérdéssé vált. Kutatások által valószínűsítetten az ellenőrizetlen adatkaparás nemcsak a művészek megélhetését veszi el, hanem aláássa az igazság és hitelesség alapjait is a digitális nyilvánosságban. A nemzeti jogalkotás feladata, hogy kötelező digitális vízjeleket, átláthatósági auditokat és méltányos szerzői kárpótlást írjon elő: a gép nem lophatja el a nemzet kulturális örökségét a technológiai fejlődés ürügyén."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Mi a fő etikai probléma a magyar írók műveinek engedély nélküli 'adatkaparásával' (data scraping)?", [
                    "Hogy a nemzetközi cégek szabadon felhasználják a szerzők szellemi tulajdonát a modellek betanítására anélkül, hogy engedélyt kérnének vagy díjazást fizetnének.",
                    "Hogy a gépek megváltoztatják a könyvek nyomdai betűtípusát.",
                    "Hogy a digitális szövegek túl sok helyet foglalnak a könyvtárak polcain."
                ], 0, ["c1-mestersegesnyelv-vocab"]),
                fb("grammar", "controlled", "Kutatások által _____ a mélyhamisítások tömege aláássa a társadalom valóságérzékét. (probabilistically / valószínűsítetten)", "valószínűsítetten", "Probabilistically supported by research the mass of deepfakes undermines society's sense of reality.", ["c1-epistemic-linguistic-uncertainty"]),
                match("vocabulary", "controlled", [["mélyhamisítás", "megtévesztő, mesterségesen generált hang- vagy videófelvétel"], ["szintetikus hang", "algoritmusok által szintetizált, emberinek hangzó beszéd"], ["adatkaparás", "internetes tartalmak tömeges, engedély nélküli letöltése"], ["szerzői jogi oltalom", "az alkotók szellemi munkájának törvényes védelme"]], ["c1-mestersegesnyelv-vocab"]),
                fb("grammar", "practice", "Tudományos _____ szerint az algoritmusok nem rendelkeznek valódi tudattal és empátiával. (assumptions / feltevések)", "feltevések", "According to scientific assumptions algorithms do not possess genuine consciousness and empathy.", ["c1-epistemic-linguistic-uncertainty"]),
                sb("grammar", "practice", ["A", "mélyhamisítások", "veszélyeztetik", "a", "társadalmi", "bizalom", "alapjait."], ["A", "mélyhamisítások", "veszélyeztetik", "a", "társadalmi", "bizalom", "alapjait."], "Deepfakes threaten the foundations of social trust.", ["c1-epistemic-linguistic-uncertainty"]),
                dc("dialogue", [
                    {"speaker": "Kiberbiztonsági elemző", "text": "Kiszűrhető-e a szintetikus hazugság az interneten?"},
                    {"speaker": "Jogászprofesszor", "text": "Tudományos feltevések szerint a digitális vízjelek kötelezővé tétele _____ kimenetellel erősítené a védelmet."},
                ], ["pozitív", "szomorú", "rossz"], 0, ["c1-epistemic-linguistic-uncertainty"]),
                sw("production", [{"prompt": "Write a sentence reflecting on AI ethics and copyright using 'tudományos feltevések szerint'.", "answer": "Tudományos feltevések szerint a szerzői jogok szigorú garanciái nélkül a globális mesterséges intelligencia modellek elszívják az alkotói energiákat, megfosztva a kultúrát autentikus megújulási képességétől."}], ["c1-epistemic-linguistic-uncertainty"]),
                mc("grammar", "check", "Melyik kifejezés testesíti meg az empirikus, tudományos távolságtartást egy technológiai kockázat értékelésekor?", [
                    "tudományos feltevések szerint / kutatások által valószínűsítetten",
                    "biztosan mindenki tudja",
                    "álmomban úgy láttam"
                ], 0, ["c1-epistemic-linguistic-uncertainty"])
            ]
        },
        {
            "num": 5,
            "stem": f"c1-{slug}-05",
            "title": "The Future of Hungarian in the Synthetic Age: Comprehensive Synthesis",
            "grammar_title": "Evaluative Synthesis Particles Advocating Comprehensive Cultural and Linguistic Preservation",
            "grammar_skill": "c1-adv-synthetic-cultural-preservation",
            "goals": [
                "I can formulate a holistic cultural preservation strategy for the Hungarian language in the age of generative AI (*szintetikus gondolkodás kora, nyelvi ökológia, digitális humanizmus*).",
                "I can employ elevated evaluative synthesis particles (*mindent egybevetve, végső tanulságként, elvitathatatlanul*).",
                "I can debate the humanistic duty to cultivate living, expressive, and resilient Hungarian for coming generations."
            ],
            "vocab": [
                {"lemma": "szintetikus gondolkodás kora", "translation": "age of synthetic thought", "pos": "expression"},
                {"lemma": "nyelvi ökológia", "translation": "linguistic ecology", "pos": "expression"},
                {"lemma": "digitális humanizmus", "translation": "digital humanism", "pos": "expression"},
                {"lemma": "szellemi szuverenitás", "translation": "intellectual sovereignty", "pos": "expression"},
                {"lemma": "nemzedékek felelőssége", "translation": "responsibility of generations", "pos": "expression"},
                {"lemma": "kulturális immunrendszer", "translation": "cultural immune system", "pos": "expression"},
                {"lemma": "élő anyanyelv", "translation": "living mother tongue", "pos": "expression"},
                {"lemma": "szintetikus szövegvilág", "translation": "synthetic textual universe", "pos": "expression"}
            ],
            "gr_text1": "Synthesis particles formulate holistic conclusions and call for collective cultural agency: `mindent egybevetve` (taking everything into account / all in all), `végső tanulságként` (as a final lesson), `elvitathatatlanul` (inarguably / undeniably), `egyértelműen kimondható` (it can be stated unambiguously).",
            "gr_text2": "Example: `Mindent egybevetve, a mesterséges intelligencia nem ellenségünk, hanem szellemi próbakövünk: végső tanulságként kimondható, hogy a magyar nyelv túlélése a digitális humanizmus bátor megvalósításán múlik`.",
            "gr_table": [
                ["Mindent egybevetve, a digitális korszakban az anyanyelv védelme nemzetstratégiai prioritás.", "Taking everything into account, in the digital era protecting the mother tongue is a national strategic priority."],
                ["Végső tanulságként levonható, hogy a gépek sosem pótolhatják a valódi emberi empátiát.", "As a final lesson it can be deduced that machines can never replace genuine human empathy."],
                ["Elvitathatatlanul a nemzeti nyelvtechnológia jelenti a kulturális önrendelkezés zálogát.", "Undeniably national language technology represents the pledge of cultural self-determination."]
            ],
            "world_story_seg": {
                "seg_slug": "jovokepek",
                "title": "A lélek kódja: a magyar nyelv jövője a szintetikus világban",
                "summary": "Drawing together the threads of computational linguistics, national model sovereignty, ethical safeguards, and humanist philosophy into a final manifesto for Hungarian language vitality.",
                "paragraphs": [
                    {"type": "narration", "text": "Amikor a szintetikus intelligencia hajnalán a magyar nyelv jövőjére tekintünk, nem a félelemnek, hanem az alkotó felelősségnek kell vezetnie a léptünket. Anyanyelvünk több mint ezer éven át állta a viharokat a Kárpát-medencében: túlélt tatárdúlást, török hódoltságot, elnyomó birodalmi nyelvrendeleteket és történelmi kataklizmákat. Mindig képes volt megújulni, befogadni az idegen szavakat és a saját zseniális logikájához szelídíteni a modern világ kihívásait. A mesterséges intelligencia megjelenése csupán egy újabb, monumentális fejezet ebben az örök küzdelemben."},
                    {"type": "narration", "text": "Mindent egybevetve, a huszonegyedik században a technológia és az anyanyelv nem egymást kizáró ellenségek, hanem szövetségesek kell legyenek. A digitális humanizmus eszméje azt követeli tőlünk, hogy a gépek szolgálják az embert, és ne az ember silányuljon az algoritmusok szolgájává. Végső tanulságként kimondható: amíg a magyar szót szeretettel, büszkeséggel és mélységgel beszéljük a családokban, az iskolákban és az irodalomban, addig anyanyelvünk a mesterséges intelligencia korában is a nemzet legfényesebb szellemi iránytűje és megmaradásának örök záloga marad."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Mit hirdet a 'digitális humanizmus' eszméje a mesterséges intelligencia korában?", [
                    "Azt, hogy a technológiai fejlesztéseknek az emberi méltóságot, a kulturális sokszínűséget és a társadalmi igazságosságot kell szolgálniuk a puszta profitszerzés helyett.",
                    "A számítógépek betiltását minden iskolában.",
                    "A robotok kötelező megkeresztelését a templomokban."
                ], 0, ["c1-mestersegesnyelv-vocab"]),
                fb("grammar", "controlled", "Mindent _____, a magyar nyelv jövője a digitális térben való cselekvő jelenléten múlik. (taking into account / egybevetve)", "egybevetve", "Taking everything into account, the future of the Hungarian language depends on active presence in digital space.", ["c1-adv-synthetic-cultural-preservation"]),
                match("vocabulary", "controlled", [["szintetikus gondolkodás kora", "a generatív mesterséges intelligencia korszaka"], ["digitális humanizmus", "az emberi értékek védelme a technológiai fejlődésben"], ["kulturális immunrendszer", "a közösség ellenállóképessége az elszürküléssel szemben"], ["élő anyanyelv", "a mindennapokban folyamatosan megújuló, gazdag nyelv"]], ["c1-mestersegesnyelv-vocab"]),
                fb("grammar", "practice", "Végső _____ megállapítható, hogy a technológia nem pótolhatja az emberi lelket. (lesson / tanulságként)", "tanulságként", "As a final lesson it can be established that technology cannot replace the human soul.", ["c1-adv-synthetic-cultural-preservation"]),
                sb("grammar", "practice", ["Mindent", "egybevetve,", "az", "anyanyelv", "a", "nemzet", "legdrágább", "kincse."], ["Mindent", "egybevetve,", "az", "anyanyelv", "a", "nemzet", "legdrágább", "kincse."], "Taking everything into account, the mother tongue is the nation's most precious treasure.", ["c1-adv-synthetic-cultural-preservation"]),
                dc("dialogue", [
                    {"speaker": "Nyelvész professzor", "text": "Hogyan összegezhető a magyar nyelv kilátása a jövőben?"},
                    {"speaker": "Filozófus", "text": "Mindent egybevetve, a technológia kihívásaira a digitális humanizmus a legméltóbb _____."},
                ], ["válaszunk", "kudarcunk", "hibánk"], 0, ["c1-adv-synthetic-cultural-preservation"]),
                sw("production", [{"prompt": "Write a concluding synthesis on the preservation of Hungarian in the digital age using 'Mindent egybevetve'.", "answer": "Mindent egybevetve, a magyar nyelv jövője nem a technológiától való elzárkózáson, hanem a szuverén digitális infrastruktúra kiépítésén és a digitális humanizmus elszánt képviseletén múlik."}], ["c1-adv-synthetic-cultural-preservation"]),
                mc("grammar", "check", "Melyik kifejezés tölt be emelkedett filozófiai és szakpolitikai összegző szerepet az esszé zárlatában?", [
                    "Mindent egybevetve / Végső tanulságként",
                    "A sarokban állva",
                    "Hirtelen eszembe jutott"
                ], 0, ["c1-adv-synthetic-cultural-preservation"])
            ]
        }
    ]

    for l in disc_lessons:
        emit_instructional_lesson(22, "discourse", l, disc_title, disc_intro if l["num"] == 1 else None)

    # Combined World Story
    write_json(
        ROOT / "content" / "hu" / "stories" / "world" / "c1" / f"c1-{slug}.json",
        {
            "id": f"story.c1.{slug}",
            "title": "A lélek kódja: a magyar nyelv és a mesterséges intelligencia szövetsége",
            "level": "C1",
            "type": "world",
            "order": 22,
            "lesson": 5,
            "estimatedMinutes": 8,
            "summary": "Panoramic exploration of Hungarian language sovereignty in the era of artificial intelligence: Anglo-Saxon LLM dominance, the threat of digital language extinction, the pioneering PULI sovereign foundation model on the Komondor supercomputer, ethics and deepfakes, and the principles of digital humanism.",
            "grammar": [
                "c1-discourse-technological-threat-framing",
                "c1-modal-deontic-digital-sovereignty",
                "c1-adv-proportional-cultural-correlatives",
                "c1-epistemic-linguistic-uncertainty",
                "c1-adv-synthetic-cultural-preservation"
            ],
            "vocabularyTopics": [
                "Artificial Intelligence, Digital Sovereignty & Small-Language Ecology",
                "LLMs, Anglo-Saxon Hegemony & Technological Threat Framing",
                "Digital Language Extinction & Deontic Sovereignty Mandates",
                "National Language Technology: The PULI Model & Proportional Correlatives",
                "AI Ethics, Deepfakes & Epistemic Uncertainty",
                "The Future of Hungarian in the Synthetic Age: Comprehensive Synthesis"
            ],
            "paragraphs": [
                {"type": "narration", "text": "A huszonegyedik század legnagyobb civilizációs fordulata a szintetikus gondolkodás korszaka: a nagy nyelvmodellek és a generatív mesterséges intelligencia robbanásszerű elterjedése. E digitális univerzumban a nyelv már nem csupán kulturális kifejezőeszköz, hanem stratégiai adat és a globális szoftverek alapkódja. Ám a Szilícium-völgy által uralt rendszerekben az angol nyelv nyomasztó hegemóniája érvényesül, amely észrevétlen, de pusztító kulturális asszimilációval fenyegeti a kis és egyedi nyelveket, köztük a magyart is."},
                {"type": "narration", "text": "A digitális nyelvkihalás réme mindennapi valósággá vált az okoseszközök és hangasszisztensek világában: a magyar nyelv könnyen perifériára szorulhat, ha a technológia nem tanulja meg anyanyelvünket. A magyar államnak és tudományos közösségnek elidegeníthetetlen kötelessége megvédeni a nemzeti digitális vagyont, és kikényszeríteni a kötelező anyanyelvi támogatást a hazai piacon értékesített eszközökben."},
                {"type": "narration", "text": "Erre a történelmi kihívásra született meg a debreceni Komondor szuperszámítógépen épített PULI, az első szuverén magyar alapmodell. A hazai nyelvészek és adattudósok bebizonyították: minél gazdagabb nemzeti szövegkorpusszal tápláljuk az algoritmusokat, annál pontosabban és méltóbban őrizhető meg a magyar gondolkodás árnyaltsága a digitális térben, miközben a mélyhamisítások és az engedély nélküli adatlopás ellen szigorú etikai és szerzői jogi garanciákat kell teremteni."},
                {"type": "narration", "text": "Mindent egybevetve, a mesterséges intelligencia nem a magyar nyelv sírásója, hanem a huszonegyedik századi megmaradásának legfőbb próbája. A digitális humanizmus szellemében a kódnak az embert és a nemzeti szellemet kell szolgálnia. Anyanyelvünk ereje, képgazdagsága és belső szabadsága a jövő szintetikus világában is a magyar közösség legdrágább szellemi vára marad."}
            ]
        }
    )

    # Discourse Consolidation
    emit_consolidation_lesson(
        22,
        "discourse",
        f"c1-{slug}-consolidation",
        disc_title,
        [
            "I can analyze large language models, Anglo-Saxon data hegemony, and digital language extinction risks.",
            "I can evaluate the PULI foundation model, supercomputing infrastructure, and AI copyright ethics.",
            "I can debate digital humanism, statutory language mandates, and the future of Hungarian in the synthetic age."
        ],
        [
            mc("grammar", "recognize", "Milyen szerkezettel fejezhetünk ki technológiai veszélyt a nemzeti kultúrára?", [
                "egzisztenciális fenyegetést jelent a nyelvre / digitális asszimilációt idéz elő",
                "mivel elküldték az emailt a szerverre",
                "amikor új szoftvert telepítenek a számítógépre"
            ], 0, ["c1-discourse-technological-threat-framing"]),
            mc("grammar", "recognize", "Melyik kifejezés testesít meg kötelező erejű digitális állami feladatot?", [
                "kötelessége biztosítani / elengedhetetlen előírni",
                "szabadon választhatnak a háttérképek közül",
                "ha kedvük tartja, kikapcsolják a gépet"
            ], 0, ["c1-modal-deontic-digital-sovereignty"]),
            match("vocabulary", "recognize", [["PULI modell", "hazai szuverén magyar alapmodell"], ["digitális nyelvkihalás", "a nyelv kirekesztődése a gépi kommunikációból"], ["hangvezérlés", "eszközök beszéddel történő irányítása"], ["mélyhamisítás", "megtévesztő mesterséges hang- és videómanipuláció"], ["digitális humanizmus", "az emberi értékek és méltóság védelme a technológiában"]], ["c1-mestersegesnyelv-vocab"]),
            fb("vocabulary", "recall", "A mesterségesen generált megtévesztő videókat és hangokat _____ nevezzük. (deepfakes / mélyhamisításoknak)", "mélyhamisításoknak", "Artificially generated deceptive videos and voices are called deepfakes.", ["c1-mestersegesnyelv-vocab"]),
            fb("vocabulary", "recall", "A magyar nyelv védelme a mesterséges intelligenciában a nemzeti szellemi _____ kérdése. (sovereignty / szuverenitás)", "szuverenitás", "Protecting the Hungarian language in artificial intelligence is a question of national intellectual sovereignty.", ["c1-mestersegesnyelv-vocab"]),
            fb("grammar", "recall", "Az államnak alkotmányos _____ megóvni a nemzeti nyelvkincset. (duty / kötelessége)", "kötelessége", "The state has a constitutional duty to preserve the national language treasure.", ["c1-modal-deontic-digital-sovereignty"]),
            fb("grammar", "context", "Minél több magyar adatot használunk, _____ pontosabb lesz a modell kifejezőereje. (the more / annál)", "annál", "The more Hungarian data we use, the more accurate the model's expressive power will be.", ["c1-adv-proportional-cultural-correlatives"]),
            fb("grammar", "context", "Mindent _____, anyanyelvünk megőrzése a jövő legfontosabb szellemi próbája. (taking into account / egybevetve)", "egybevetve", "Taking everything into account, preserving our mother tongue is the future's most important intellectual test.", ["c1-adv-synthetic-cultural-preservation"]),
            mc("grammar", "context", "Mi a lényege a 'Minél... annál...' korrelatív szerkezetnek a nyelvtechnológiai érvelésben?", [
                "Megmutatja, hogy a tanítóadatok minőségének növelése arányosan jobb és árnyaltabb anyanyelvi modellt eredményez.",
                "Kijelenti, hogy nincs szükség semmilyen számítógépre.",
                "Elnézést kér az angol nyelv elterjedése miatt."
            ], 0, ["c1-adv-proportional-cultural-correlatives"]),
            sb("grammar", "produce", ["A", "magyar", "nyelv", "a", "digitális", "jövőben", "is", "élni", "fog."], ["A", "magyar", "nyelv", "a", "digitális", "jövőben", "is", "élni", "fog."], "The Hungarian language will live in the digital future as well.", ["c1-adv-synthetic-cultural-preservation"]),
            sw("production", [{"prompt": "Write a sentence diagnosing the existential threat of global AI to Hungarian using an elevated threat framing marker.", "answer": "A globális techóriások által vezérelt mesterséges intelligencia egzisztenciális fenyegetést jelent a magyar nyelvre, mivel a monokultúrás tanítóadatok terjedése észrevétlen digitális asszimilációt idéz elő."}], ["c1-discourse-technological-threat-framing"]),
            sw("production", [{"prompt": "Formulate a concluding thought on digital humanism and Hungarian language sovereignty.", "answer": "Mindent egybevetve, a magyar nyelv túlélése a szintetikus korban a digitális humanizmus megvalósításán és a szuverén hazai nyelvtechnológiai innovációkon múlik."}], ["c1-adv-synthetic-cultural-preservation"])
        ]
    )

    print("=== Finished C1 Unit 22 ===")


if __name__ == "__main__":
    generate_unit_22()
