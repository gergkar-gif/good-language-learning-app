#!/usr/bin/env python3
"""
Hungarian C1 Block 5 - Unit 26 Generator:
  - Track 1 (Core): Unit 26 — "Media Ecology, Freedom of the Press & The Public Sphere" (c1-26)
  - Track 2 (Discourse): Unit 26 — "Media Capture: The KESMA Empire, State Propaganda & Digital Resistance" (c1-mediaszabadsag)
"""

import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT))

from scripts.c1_block1.common import mc, match, fb, sb, dc, sw, write_json, emit_instructional_lesson, emit_consolidation_lesson
from scripts.c1_block5.registry_helper import register_unit


def generate_unit_26():
    print("=== Generating C1 Unit 26 ===")
    
    new_skills = {
        "c1-26-vocab": {"kind": "vocabulary"},
        "c1-mediaszabadsag-vocab": {"kind": "vocabulary"},
        "c1-adv-epistemic-discursive-truth": {"kind": "grammar"},
        "c1-participle-manipulative-framing": {"kind": "grammar"},
        "c1-adv-adversative-rhetorical-refutation": {"kind": "grammar"},
        "c1-modal-deliberative-public-sphere": {"kind": "grammar"},
        "c1-adv-scalar-journalistic-integrity": {"kind": "grammar"},
        "c1-discourse-media-capture-framing": {"kind": "grammar"},
        "c1-modal-deontic-public-broadcasting": {"kind": "grammar"},
        "c1-adv-proportional-advertising-distortion": {"kind": "grammar"},
        "c1-epistemic-propaganda-stigmatization": {"kind": "grammar"},
        "c1-adv-conclusive-free-press-defense": {"kind": "grammar"},
    }
    new_titles = {
        "c1-26-vocab": "reading",
        "c1-mediaszabadsag-vocab": "reading",
        "c1-adv-epistemic-discursive-truth": "epistemic truth value adverbials evaluating media claims and objective reality",
        "c1-participle-manipulative-framing": "complex participial structures exposing discursive manipulation and propaganda distortion",
        "c1-adv-adversative-rhetorical-refutation": "adversative rhetorical connectors debunking disinformation narratives and falsehoods",
        "c1-modal-deliberative-public-sphere": "deliberative modal structures articulating public sphere dialogue and journalistic standards",
        "c1-adv-scalar-journalistic-integrity": "scalar evaluative adverbials calibrating press freedom and journalistic independence",
        "c1-discourse-media-capture-framing": "discourse framing markers diagnosing systemic media capture and conglomerate monopolization",
        "c1-modal-deontic-public-broadcasting": "deontic modal structures critiquing state broadcaster capture and bias",
        "c1-adv-proportional-advertising-distortion": "proportional correlative conjunctions mapping state advertising distortion and market foreclosure",
        "c1-epistemic-propaganda-stigmatization": "epistemic stance markers exposing smear campaigns and foreign agent rhetoric",
        "c1-adv-conclusive-free-press-defense": "evaluative synthesis particles formulating manifestos for independent media resilience",
    }
    
    core_title = "Media Ecology, Freedom of the Press & The Public Sphere"
    core_stems = [f"c1-26-0{i}" for i in range(1, 6)] + ["c1-26-consolidation"]
    disc_title = "Media Capture: The KESMA Empire, State Propaganda & Digital Resistance"
    disc_stems = [f"c1-mediaszabadsag-0{i}" for i in range(1, 6)] + ["c1-mediaszabadsag-consolidation"]
    
    register_unit(26, core_title, core_stems, disc_title, disc_stems, new_skills, new_titles)

    # ----------------------------------------------------
    # TRACK 1: CORE (c1-26)
    # ----------------------------------------------------
    core_intro = [
        "A healthy democratic society cannot exist without a pluralistic public sphere, where citizens have access to verified facts and unmanipulated information. In Hungarian cultural history, the freedom of the printed word has been the central battleground of freedom—from the 12 points of 1848 to the somber diary entries of Sándor Márai witnessing the destruction of the bourgeois press.",
        "In this unit, anchored by Márai Sándor's piercing reflections in 'Napló (1943–1948)', you will master the elevated rhetorical register of media ecology, fact-checking, journalistic ethics, discursive manipulation analysis, and the philosophical defense of truth at the C1 level."
    ]

    core_lessons = [
        {
            "num": 1,
            "stem": "c1-26-01",
            "title": "Epistemic Truth Value Adverbials & Fact-Checking",
            "grammar_title": "Epistemic Truth Value Adverbials Evaluating Media Claims and Objective Reality",
            "grammar_skill": "c1-adv-epistemic-discursive-truth",
            "goals": [
                "I can analyze news verification, fact-checking methodology, and media claims (*tényellenőrzés, hírforrás hitelessége, dezinformáció, objektív valóság*).",
                "I can employ elevated epistemic truth value adverbials (*igazolhatóan, megdönthetetlen bizonyossággal, tényszerűen megalapozottan, kétséget kizáróan*).",
                "I can distinguish between verified reporting and unsubstantiated conjecture in formal prose."
            ],
            "vocab": [
                {"lemma": "tényellenőrzés", "translation": "fact-checking", "pos": "noun"},
                {"lemma": "hírforrás hitelessége", "translation": "credibility of news source", "pos": "expression"},
                {"lemma": "dezinformáció", "translation": "disinformation", "pos": "noun"},
                {"lemma": "objektív valóság", "translation": "objective reality", "pos": "expression"},
                {"lemma": "forráskritika", "translation": "source criticism", "pos": "noun"},
                {"lemma": "torzításmentes tájékoztatás", "translation": "unbiased reporting", "pos": "expression"},
                {"lemma": "megalapozottság", "translation": "well-foundedness / substantiate", "pos": "noun"},
                {"lemma": "álhírgyártás", "translation": "fake news generation", "pos": "noun"}
            ],
            "gr_text1": "Epistemic truth value adverbials establish the verifiable factual grounding of statements in investigative and journalistic discourse: `igazolhatóan hamisnak bizonyult` (proved verifiably false), `megdönthetetlen bizonyossággal állítható` (can be stated with incontrovertible certainty), `tényszerűen alátámasztott módon` (in a factually corroborated manner), `kétséget kizáróan verifikált tény` (fact verified beyond doubt).",
            "gr_text2": "Example: `A tényellenőrök kimutatták, hogy a sajtóban megjelent állítás igazolhatóan cáfolható, és megdönthetetlen bizonyossággal félrevezetőnek minősül`.",
            "gr_table": [
                ["A hír igazolhatóan hamis forrásból származott.", "The news verifiably originated from a false source."],
                ["Megdönthetetlen bizonyossággal cáfolták az álhírt a szakértők.", "Experts refuted the fake news with incontrovertible certainty."],
                ["A cikk tényszerűen alátámasztott módon mutatta be a történteket.", "The article presented the events in a factually corroborated manner."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mit jelent a 'forráskritika' a professzionális újságírásban?", [
                    "A felhasznált információk, adatok és tanúvallomások eredetének, megbízhatóságának és motívumainak szigorú ellenőrzését.",
                    "A forrásvíz minőségének ellenőrzését a szerkesztőségi konyhában.",
                    "A cikkek betűtípusának esztétikai értékelését."
                ], 0, ["c1-26-vocab"]),
                fb("grammar", "controlled", "A leleplezett botrányról közzétett adatok _____ alátámasztott tényeken alapulnak. (factually / tényszerűen)", "tényszerűen", "Data published about the exposed scandal are based on factually corroborated facts.", ["c1-adv-epistemic-discursive-truth"]),
                match("vocabulary", "controlled", [["tényellenőrzés", "állítások valóságtartalmának szisztematikus vizsgálata"], ["dezinformáció", "szándékosan terjesztett félrevezető információ"], ["forráskritika", "hírforrások megbízhatóságának ellenőrzése"], ["álhírgyártás", "kitalált hírek iparszerű előállítása"]], ["c1-26-vocab"]),
                fb("grammar", "practice", "A vizsgálat megdönthetetlen _____ bizonyította be a dokumentum hamisítvány voltát. (certainty / bizonyossággal)", "bizonyossággal", "The investigation proved the forged nature of the document with incontrovertible certainty.", ["c1-adv-epistemic-discursive-truth"]),
                sb("grammar", "practice", ["A", "riport", "igazolhatóan", "valós", "adatokra", "építette", "fel", "érvelését."], ["A", "riport", "igazolhatóan", "valós", "adatokra", "építette", "fel", "érvelését."], "The report built its argumentation on verifiably real data.", ["c1-adv-epistemic-discursive-truth"]),
                dc("dialogue", [
                    {"speaker": "Főszerkesztő", "text": "Közölhetjük-e ezt a szenzációs értesülést a címlapon?"},
                    {"speaker": "Tényellenőr", "text": "Semmiképp; a hír még nem nyert _____ megerősítést két független forrásból."},
                    {"speaker": "Főszerkesztő", "text": "Akkor elhalasztjuk a publikálást a hitelesítésig."}
                ], ["kétséget kizáró", "gyors", "hangos"], 0, ["c1-adv-epistemic-discursive-truth"]),
                sw("production", [{"prompt": "Write a sentence formulating the factual verification of a news story using an epistemic truth adverbial.", "answer": "A független tényellenőrök megdönthetetlen bizonyossággal mutatták ki, hogy a közösségi médiában keringő állítás igazolhatóan manipulált felvételeken alapult."}], ["c1-adv-epistemic-discursive-truth"]),
                mc("grammar", "check", "Melyik határozó fejez ki megdönthetetlen valóságtartalmat a legmagasabb bizonyossággal?", [
                    "megdönthetetlen bizonyossággal / kétséget kizáróan igazoltan",
                    "többé-kevésbé talán igaz módon",
                    "úgy tűnik mintha igaz lenne"
                ], 0, ["c1-adv-epistemic-discursive-truth"])
            ]
        },
        {
            "num": 2,
            "stem": "c1-26-02",
            "title": "Discursive Manipulation & Participial Framing",
            "grammar_title": "Complex Participial Structures Exposing Discursive Manipulation and Propaganda Distortion",
            "grammar_skill": "c1-participle-manipulative-framing",
            "goals": [
                "I can analyze propaganda techniques, emotional incitement, and narrative framing (*narratív keretezés, érzelmi manipuláció, bűnbakképzés, karaktergyilkosság*).",
                "I can deploy complex participial structures exposing discursive distortions (*a tényeket elferdítő, a közvéleményt félrevezető, a kontextusból kiragadott*).",
                "I can dissect how political campaigns manufacture pseudo-realities."
            ],
            "vocab": [
                {"lemma": "narratív keretezés", "translation": "narrative framing", "pos": "expression"},
                {"lemma": "karaktergyilkosság", "translation": "character assassination", "pos": "noun"},
                {"lemma": "bűnbakképzés", "translation": "scapegoating", "pos": "noun"},
                {"lemma": "érzelmi polarizáció", "translation": "emotional polarization", "pos": "expression"},
                {"lemma": "kontextusból kiragadás", "translation": "taking out of context", "pos": "expression"},
                {"lemma": "ellenségkép-gyártás", "translation": "enemy image manufacture", "pos": "noun"},
                {"lemma": "pszichológiai hadviselés", "translation": "psychological warfare", "pos": "expression"},
                {"lemma": "sugallmazás", "translation": "innuendo / suggestion", "pos": "noun"}
            ],
            "gr_text1": "Complex participial modifiers expose the deceptive, distortive mechanics of propaganda campaigns: `a valóságot eltorzító propagandakampány` (propaganda campaign distorting reality), `a kontextusából kiragadott mondat` (sentence torn out of its context), `a társadalmat szándékosan megosztó retorika` (rhetoric intentionally dividing society), `az indulatokat szító és félelmet keltő szalagcím` (headline stoking passions and generating fear).",
            "gr_text2": "Example: `A médiakutatók a tényeket elferdítő, a kontextusból kiragadott félmondatokkal operáló lejáratókampányt elemezték`.",
            "gr_table": [
                ["A közvéleményt manipuláló cikkek mélyen aláássák a társadalmi bizalmat.", "Articles manipulating public opinion deeply undermine social trust."],
                ["A kontextusból kiragadott idézetekkel folytatott karaktergyilkosság etikátlan.", "Character assassination conducted with quotes torn from context is unethical."],
                ["Az indulatokat szító szalagcímek a racionális vitát lehetetlenítik el.", "Headlines stoking passions render rational debate impossible."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mi a lényege a 'karaktergyilkosságnak' a politikai médiakampányokban?", [
                    "Egy közéleti személy hitelességének, tisztességének és emberi méltóságának szándékos, hazug vádakkal történő megsemmisítése.",
                    "Egy színész fizikai bántalmazása a színpadon.",
                    "Egy új életrajzi regény megjelenése a könyvesboltokban."
                ], 0, ["c1-26-vocab"]),
                fb("grammar", "controlled", "A valóságot szándékosan _____ cikkek rombolják a nyilvánosság tisztaságát. (distorting / eltorzító)", "eltorzító", "Articles intentionally distorting reality destroy the purity of the public sphere.", ["c1-participle-manipulative-framing"]),
                match("vocabulary", "controlled", [["karaktergyilkosság", "személy szándékos erkölcsi megsemmisítése"], ["bűnbakképzés", "mások hibáztatására épülő bűnbakkeresés"], ["narratív keretezés", "a valóság egyoldalú értelmezési keretbe szorítása"], ["ellenségkép-gyártás", "mesterséges politikai ellenségek képzése"]], ["c1-26-vocab"]),
                fb("grammar", "practice", "A kontextusból _____ mondatokkal nem lehet tisztességes vitát folytatni. (torn out / kiragadott)", "kiragadott", "With sentences torn out of context one cannot conduct a fair debate.", ["c1-participle-manipulative-framing"]),
                sb("grammar", "practice", ["A", "tényeket", "elferdítő", "kampányok", "megmérgezik", "a", "közéletet."], ["A", "tényeket", "elferdítő", "kampányok", "megmérgezik", "a", "közéletet."], "Campaigns distorting facts poison public life.", ["c1-participle-manipulative-framing"]),
                dc("dialogue", [
                    {"speaker": "Elemző", "text": "Hogyan értékelhető a sajtóban indított új lejárató hadjárat?"},
                    {"speaker": "Szociológus", "text": "Ez egy klasszikus, az indulatokat _____ és a közvéleményt félrevezető bűnbakképzési technika."},
                    {"speaker": "Elemző", "text": "Ami teljesen kiszorítja a tárgyszerű érveket."}
                ], ["szító", "nyugtató", "felejtő"], 0, ["c1-participle-manipulative-framing"]),
                sw("production", [{"prompt": "Write a critical exposure of propaganda using a participial framing structure.", "answer": "A hatalom által finanszírozott, a tényeket szándékosan eltorzító és az ellenségképeket sulykoló propagandakampányok végletesen polarizálják a társadalmat."}], ["c1-participle-manipulative-framing"]),
                mc("grammar", "check", "Melyik melléknévi igeneves szerkezet leplezi le a manipulatív médiát a legpontosabban?", [
                    "a tényeket szándékosan eltorzító / az indulatokat szító",
                    "a napfényben melegen sütkérező",
                    "a könyvtárban csendben várakozó"
                ], 0, ["c1-participle-manipulative-framing"])
            ]
        },
        {
            "num": 3,
            "stem": "c1-26-03",
            "title": "Adversative Rhetorical Refutation of Disinformation",
            "grammar_title": "Adversative Rhetorical Connectors Debunking Disinformation Narratives and Falsehoods",
            "grammar_skill": "c1-adv-adversative-rhetorical-refutation",
            "goals": [
                "I can analyze conspiracy theories, state propaganda narratives, and rhetorical refutation (*összeesküvés-elmélet, cáfolat, ellenbizonyítás, álvalóság*).",
                "I can construct elevated adversative rhetorical connectors debunking lies (*ezzel szemben a valóságban, nemhogy nem felel meg a valóságnak, hanem éppen ellenkezőleg, mindazonáltal tényszerűen cáfolható*).",
                "I can articulate rigorous point-by-point journalistic rebuttals."
            ],
            "vocab": [
                {"lemma": "cáfolat", "translation": "refutation / rebuttal", "pos": "noun"},
                {"lemma": "összeesküvés-elmélet", "translation": "conspiracy theory", "pos": "expression"},
                {"lemma": "ellenbizonyítás", "translation": "counter-evidence", "pos": "noun"},
                {"lemma": "álvalóság", "translation": "pseudo-reality", "pos": "noun"},
                {"lemma": "tudatos ködösítés", "translation": "deliberate obfuscation", "pos": "expression"},
                {"lemma": "ténybeli ellentmondás", "translation": "factual contradiction", "pos": "expression"},
                {"lemma": "helyreigazítás", "translation": "rectification / correction", "pos": "noun"},
                {"lemma": "sajtóper", "translation": "press lawsuit / defamation lawsuit", "pos": "noun"}
            ],
            "gr_text1": "Adversative rhetorical connectors introduce definitive, evidence-based rebuttals against propaganda fabrications: `ezzel szemben a valóságban` (in contrast with this in reality), `nemhogy nem felel meg a tényeknek, hanem éppen ellenkezőleg` (far from corresponding to facts, but on the contrary), `mindazonáltal tényszerűen cáfolható` (nevertheless factually refutable), `szemben a terjesztett állítással` (contrary to the disseminated claim).",
            "gr_text2": "Example: `A propaganda állításaival szemben a valóságban a hivatalos statisztikák nemhogy nem javulást mutatnak, hanem éppen ellenkezőleg, drámai visszaesést jeleznek`.",
            "gr_table": [
                ["A propaganda állításával szemben a valóságban a gazdaság recesszióba süllyedt.", "Contrary to propaganda claims in reality the economy sank into recession."],
                ["A vád nemhogy nem igaz, hanem éppen ellenkezőleg, rágalomnak bizonyult.", "The accusation is far from true; on the contrary, it proved to be slander."],
                ["A sajtóközlemény mindazonáltal tényszerűen cáfolható a nyilvános adatok alapján.", "The press release is nevertheless factually refutable on the basis of public data."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mi a jogi következménye annak, ha egy lap sajtópert veszít valótlan állítás miatt?", [
                    "A bíróság helyreigazítás közzétételére és sérelemdíj fizetésére kötelezi a szerkesztőséget.",
                    "A lap újságíróit száműzik az országból.",
                    "A vesztes szerkesztőség köteles ingyen újságot hordani a bíró házához."
                ], 0, ["c1-26-vocab"]),
                fb("grammar", "controlled", "A híreszteléssel szemben a _____ a minisztérium nem hozott ilyen döntést. (in reality / valóságban)", "valóságban", "Contrary to rumors, in reality the ministry made no such decision.", ["c1-adv-adversative-rhetorical-refutation"]),
                match("vocabulary", "controlled", [["cáfolat", "egy állítás valótlanságának bizonyítása"], ["helyreigazítás", "téves sajtóhír kötelező bírósági javítása"], ["sajtóper", "valótlan tényállítás miatti bírósági eljárás"], ["összeesküvés-elmélet", "rejtett háttérhatalmakat feltételező magyarázat"]], ["c1-26-vocab"]),
                fb("grammar", "practice", "Az állítás nemhogy nem felel meg a tényeknek, hanem éppen _____ bizonyult igaznak. (contrary / ellenkezőleg)", "ellenkezőleg", "The claim is far from matching facts; on the contrary, the opposite proved true.", ["c1-adv-adversative-rhetorical-refutation"]),
                sb("grammar", "practice", ["Ezzel", "szemben", "a", "valóságban", "minden", "irat", "hozzáférhető."], ["Ezzel", "szemben", "a", "valóságban", "minden", "irat", "hozzáférhető."], "In contrast with this in reality all documents are accessible.", ["c1-adv-adversative-rhetorical-refutation"]),
                dc("dialogue", [
                    {"speaker": "Riporter", "text": "Hogyan válaszol az ellenzéki politikus a kormányzati sajtó vádjaira?"},
                    {"speaker": "Jogtanácsos", "text": "A vád nemhogy nem igaz, hanem éppen _____ cáfolható a számlákkal."},
                    {"speaker": "Riporter", "text": "Akkor sajtópert indítanak a rágalmazók ellen."}
                ], ["ellenkezőleg", "kicsit", "hangosan"], 0, ["c1-adv-adversative-rhetorical-refutation"]),
                sw("production", [{"prompt": "Write a sentence debunking a disinformation narrative using 'Ezzel szemben a valóságban'.", "answer": "A kormánymédia által terjesztett álhírrel szemben a valóságban a nemzetközi jelentések nemhogy dicsérnék a reformot, hanem súlyos aggályokat fogalmaznak meg."}], ["c1-adv-adversative-rhetorical-refutation"]),
                mc("grammar", "check", "Melyik kötőszószerkezet fejezi ki a leghatározottabb retorikai cáfolatot?", [
                    "nemhogy nem igaz, hanem éppen ellenkezőleg / ezzel szemben a valóságban",
                    "esetleg talán nem pontosan így van",
                    "mindez nem túl érdekes számunkra"
                ], 0, ["c1-adv-adversative-rhetorical-refutation"])
            ]
        },
        {
            "num": 4,
            "stem": "c1-26-04",
            "title": "The Public Sphere & Deliberative Modals",
            "grammar_title": "Deliberative Modal Structures Articulating Public Sphere Dialogue and Journalistic Standards",
            "grammar_skill": "c1-modal-deliberative-public-sphere",
            "goals": [
                "I can analyze Jürgen Habermas's theory of the public sphere, deliberative democracy, and communicative ethics (*polgári nyilvánosság, deliberatív demokrácia, konszenzuskeresés, sajtóetika*).",
                "I can formulate deliberative modal structures articulating journalistic duties (*tárgyilagosan kell tájékoztatnia, biztosítania kell az ellentétes nézőpontok megjelenését, nem szolgáltathatja ki magát*).",
                "I can debate the balance between freedom of speech and protection against hate speech."
            ],
            "vocab": [
                {"lemma": "polgári nyilvánosság", "translation": "bourgeois / democratic public sphere", "pos": "expression"},
                {"lemma": "deliberatív demokrácia", "translation": "deliberative democracy", "pos": "expression"},
                {"lemma": "kommunikatív etika", "translation": "communicative ethics", "pos": "expression"},
                {"lemma": "sajtóetikai kódex", "translation": "journalistic code of ethics", "pos": "expression"},
                {"lemma": "közérdekű tájékoztatás", "translation": "public interest reporting", "pos": "expression"},
                {"lemma": "gyűlöletbeszéd", "translation": "hate speech", "pos": "noun"},
                {"lemma": "véleménypluralizmus", "translation": "pluralism of opinion", "pos": "noun"},
                {"lemma": "szerkesztőségi integritás", "translation": "editorial integrity", "pos": "expression"}
            ],
            "gr_text1": "Deliberative modal structures prescribe ethical requirements and professional mandates for public deliberation: `köteles tiszteletben tartani a többoldalú tájékoztatás elvét` (is obligated to respect the principle of multifaceted reporting), `nem rendelheti alá az igazságot politikai érdekeknek` (must not subordinate truth to political interests), `biztosítania kell a vitapartnerek egyenlő megszólalását` (must secure equal voice for debate partners), `felelősséggel tartozik a nyilvánosság tisztaságáért` (bears responsibility for the purity of the public sphere).",
            "gr_text2": "Example: `A független újságírónak tárgyilagosan, minden érintett felet megszólaltatva kell tájékoztatnia a közvéleményt a vitás kérdésekről`.",
            "gr_table": [
                ["A sajtónak tárgyilagosan kell bemutatnia a különböző álláspontokat.", "The press must objectively present differing standpoints."],
                ["A szerkesztőség nem szolgáltathatja ki magát a hirdetők politikai nyomásának.", "The editorial board must not expose itself to advertisers' political pressure."],
                ["A demokratikus államnak szavatolnia kell a véleménypluralizmus feltételeit.", "The democratic state must guarantee conditions for pluralism of opinion."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mit jelent a 'véleménypluralizmus' a demokratikus média világában?", [
                    "A különböző politikai, társadalmi és világnézeti álláspontok szabad, kiegyensúlyozott megjelenését a nyilvánosságban.",
                    "Azt, hogy minden újságban kötelező viccrovatot vezetni.",
                    "A televíziós csatornák számának korlátozását egyetlen állami adóra."
                ], 0, ["c1-26-vocab"]),
                fb("grammar", "controlled", "A közszolgálati médiának pártatlanul _____ tájékoztatnia a választópolgárokat. (must / kell)", "kell", "Public service media must inform voters impartially.", ["c1-modal-deliberative-public-sphere"]),
                match("vocabulary", "controlled", [["polgári nyilvánosság", "a szabad polgárok érvelő vitáinak tere"], ["deliberatív demokrácia", "érveken és közös vitán alapuló döntéshozatal"], ["sajtóetikai kódex", "újságírói szakmai és erkölcsi szabályzat"], ["véleménypluralizmus", "különböző álláspontok egyidejű jelenléte"]], ["c1-26-vocab"]),
                fb("grammar", "practice", "A szerkesztő nem _____ alá a szakmai integritást a pártpolitikai elvárásoknak. (must not subordinate / rendelheti)", "rendelheti", "The editor must not subordinate professional integrity to party-political expectations.", ["c1-modal-deliberative-public-sphere"]),
                sb("grammar", "practice", ["A", "médiának", "kötelessége", "biztosítani", "a", "sokszínű", "tájékoztatást."], ["A", "médiának", "kötelessége", "biztosítani", "a", "sokszínű", "tájékoztatást."], "The media has a duty to secure diverse reporting.", ["c1-modal-deliberative-public-sphere"]),
                dc("dialogue", [
                    {"speaker": "Médiaetikus", "text": "Hogyan kell eljárnia egy szerkesztőségnek, ha a tulajdonos cenzúrázni akar egy cikket?"},
                    {"speaker": "Főszerkesztő", "text": "A főszerkesztő nem _____ el a szakmai etika szabályaitól, védenie kell a függetlenséget."},
                    {"speaker": "Médiaetikus", "text": "Ez a deliberatív nyilvánosság alapvető garanciája."}
                ], ["térhet", "nézhet", "kérhet"], 0, ["c1-modal-deliberative-public-sphere"]),
                sw("production", [{"prompt": "Write a sentence defining journalistic duty using a deliberative modal structure.", "answer": "A hiteles újságírónak kíméletlen tárgyilagossággal, a hatalomtól függetlenül kell feltárnia az igazságot, és nem rendelheti alá szakmai lelkiismeretét semmilyen politikai érdeknek."}], ["c1-modal-deliberative-public-sphere"]),
                mc("grammar", "check", "Melyik modális kifejezés írja elő a legsürgetőbben az újságírói felelősséget?", [
                    "köteles biztosítani a többoldalú tájékoztatást / nem rendelheti alá",
                    "szabadon dönthet hogy ír-e valamit",
                    "esetleg felhívhatja a barátját"
                ], 0, ["c1-modal-deliberative-public-sphere"])
            ]
        },
        {
            "num": 5,
            "stem": "c1-26-05",
            "title": "Márai Sándor: Diary (1943–1948) & Scalar Journalistic Integrity",
            "grammar_title": "Scalar Evaluative Adverbials Calibrating Press Freedom and Journalistic Independence",
            "grammar_skill": "c1-adv-scalar-journalistic-integrity",
            "goals": [
                "I can analyze Márai Sándor's reflections on totalitarian propaganda, the destruction of bourgeois public life, and the degradation of the language.",
                "I can employ scalar evaluative adverbials calibrating press freedom and integrity (*szakmailag feddhetetlenül, etikailag mélységesen aggályosan, a legszigorúbb mércével mérve*).",
                "I can critique the historical tragedy of intellectual conformism and self-censorship."
            ],
            "vocab": [
                {"lemma": "szellemi konformizmus", "translation": "intellectual conformism", "pos": "expression"},
                {"lemma": "öncenzúra", "translation": "self-censorship", "pos": "noun"},
                {"lemma": "nyelvrontás", "translation": "corruption / degradation of language", "pos": "noun"},
                {"lemma": "írástudók árulása", "translation": "treason of the intellectuals (trahison des clercs)", "pos": "expression"},
                {"lemma": "polgári ethosz", "translation": "bourgeois ethos / civic spirit", "pos": "expression"},
                {"lemma": "totalitárius propaganda", "translation": "totalitarian propaganda", "pos": "expression"},
                {"lemma": "független szellem", "translation": "independent spirit", "pos": "expression"},
                {"lemma": "erkölcsi integritás", "translation": "moral integrity", "pos": "expression"}
            ],
            "gr_text1": "Scalar evaluative adverbials measure the degree of ethical rigor and independence achieved by journalists and intellectuals under political pressure: `szakmailag feddhetetlenül eljárva` (acting in a professionally irreproachable manner), `etikailag mélységesen megalkuvó módon` (in an ethically deeply compromising manner), `a legszigorúbb erkölcsi mércével mérve` (measured by the strictest moral standard), `minden szakmai normát feladva` (abandoning all professional norms).",
            "gr_text2": "Example: `Márai Sándor a legszigorúbb erkölcsi mércével mérve ítélte el azokat az értelmiségieket, akik szakmailag feddhetetlen munkájukat feladva behódoltak a hatalomnak`.",
            "gr_table": [
                ["A riporter szakmailag feddhetetlenül, a fenyegetések ellenére is közölte a tényeket.", "The reporter professionally irreproachably published the facts despite threats."],
                ["A propaganda kiszolgálása etikailag mélységesen megalkuvó magatartás.", "Serving propaganda is an ethically deeply compromising conduct."],
                ["A legszigorúbb erkölcsi mércével mérve az írástudók felelősek a szavak tisztaságáért.", "Measured by the strictest moral standard intellectuals are responsible for the purity of words."]
            ],
            "classic_story": {
                "slug": "marai-naplo-sajtoszabadsag",
                "title": "Napló (1943–1948): A szabad sajtó halála és a szavak felelőssége",
                "author": "Márai Sándor",
                "work": "Napló (1943–1948)",
                "summary": "Márai Sándor megrázó naplójegyzetei a második világháború és az azt követő kommunista hatalomátvétel éveiből. Márai tanúja volt annak, miként zúzza szét az önkényuralom a szabad polgári sajtót, és miként silányítja a propaganda a nemzeti nyelvet hazug szlogenek halmazává. A kassai születésű polgári író nem volt hajlandó kompromisszumot kötni a zsarnoksággal, s végül az emigráció keserű kenyerét választotta a szellemi integritás megőrzéséért.",
                "characters": ["Márai Sándor, a szabad szó és polgári szellem védelmezője"],
                "paragraphs": [
                    {"type": "narration", "text": "Budapest ostroma után, midőn a romok között új zsarnokság vert tanyát, Márai Sándor naplójában döbbenten rögzítette a polgári nyilvánosság végső felszámolását. Az újságok, amelyek egykor a sokszínű gondolat, a szellemes kritika és a szabad polgári vita fórumai voltak, sorra az állami propaganda pártközpontjainak végrehajtóivá züllöttek."},
                    {"type": "dialogue", "speaker": "Márai Sándor", "text": "A zsarnokság első ténykedése mindig a szavak megmérgezése. Elveszik a szavak valódi értelmét: békének hívják az elnyomást, demokráciának az egypárti diktatúrát, és népakarattnak a rettegést. Ha a sajtó elnémul, a nemzet elveszíti lelkiismeretét."},
                    {"type": "narration", "text": "Márai mély fájdalommal szemlélte az írástudók árulását: tehetséges költők és publicisták adták el tollukat a hatalomnak, hogy az új rend szócsöveivé váljanak. A szellemi konformizmus és a gyáva öncenzúra gyorsabban emésztette fel a szabad magyar irodalmat, mint maguk a cenzúrahivatalok betiltó határozatai."},
                    {"type": "narration", "text": "A legszigorúbb erkölcsi mércével mérve Márai számára nem maradt más választás, mint a távozás. 1948-ban elhagyta hazáját, mert tudta: szakmailag feddhetetlenül és emberileg tisztán csak ott élhet és írhat, ahol a leírt szónak súlya van, és a szabadság nem elvont frázis, hanem a létezés egyetlen lehetséges levegője."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Mit nevez Julien Benda és Márai Sándor az 'írástudók árulásának' (la trahison des clercs)?", [
                    "Azt a tragikus jelenséget, amikor a szellemi elit képviselői az egyetemes igazság és erkölcs védelme helyett a politikai hatalom szolgálatába szegődnek.",
                    "Amikor a könyvtárosok elfelejtik visszatenni a könyveket a polcra.",
                    "Egy középkori latin nyelvtanulási módszert."
                ], 0, ["c1-26-vocab"]),
                fb("grammar", "controlled", "A tudósító szakmailag _____ módon tárta fel az igazságot a fenyegetések ellenére. (irreproachably / feddhetetlen)", "feddhetetlen", "The correspondent revealed the truth in a professionally irreproachable manner despite threats.", ["c1-adv-scalar-journalistic-integrity"]),
                match("vocabulary", "controlled", [["szellemi konformizmus", "a hatalomhoz való elvtelen igazodás"], ["öncenzúra", "a belső félelemből fakadó önkorlátozás"], ["nyelvrontás", "a szavak értelmének szándékos eltorzítása propagandával"], ["polgári ethosz", "a független, felelős polgár erkölcsi tartása"]], ["c1-26-vocab"]),
                fb("grammar", "practice", "A legszigorúbb erkölcsi mércével _____ az újságíró nem szolgálhat ki hazug propagandát. (measured / mérve)", "mérve", "Measured by the strictest moral standard the journalist cannot serve lying propaganda.", ["c1-adv-scalar-journalistic-integrity"]),
                sb("grammar", "practice", ["Márai", "Sándor", "megőrizte", "szellemi", "függetlenségét", "az", "emigrációban."], ["Márai", "Sándor", "megőrizte", "szellemi", "függetlenségét", "az", "emigrációban."], "Sándor Márai preserved his intellectual independence in emigration.", ["c1-adv-scalar-journalistic-integrity"]),
                mc("reading", "context", "Miért döntött úgy Márai Sándor 1948-ban, hogy elhagyja Magyarországot?", [
                    "Mert a totalitárius kommunista diktatúrában a sajtó és a szellem szabadsága megszűnt, és nem akart cinkossá válni a szavak megmérgezésében.",
                    "Mert el akarta adni az olasz tengerparti nyaralóját.",
                    "Mert a párizsi divathéten kapott újságírói állást."
                ], 0, ["c1-26-vocab"]),
                sw("production", [{"prompt": "Write a reflection on Márai Sándor's warning about language corruption using 'szakmailag feddhetetlenül'.", "answer": "Márai Sándor tanítása szerint az írástudónak a legnehezebb időkben is szakmailag feddhetetlenül kell védenie az anyanyelv tisztaságát és az erkölcsi igazságot a totalitárius nyelvrontással szemben."}], ["c1-adv-scalar-journalistic-integrity"]),
                mc("grammar", "check", "Melyik kifejezés kalibrálja a morális és szakmai integritást a legemelkedettebb stílusban?", [
                    "a legszigorúbb erkölcsi mércével mérve / szakmailag feddhetetlenül",
                    "többnyire jól viselkedve",
                    "amikor éppen nem figyel senki"
                ], 0, ["c1-adv-scalar-journalistic-integrity"])
            ]
        }
    ]

    for l in core_lessons:
        emit_instructional_lesson(26, "core", l, core_title, core_intro if l["num"] == 1 else None)

    # Core Consolidation Lesson
    emit_consolidation_lesson(
        26,
        "core",
        "c1-26-consolidation",
        core_title,
        [
            "I can master the sophisticated C1 vocabulary of media ecology, fact-checking, and public sphere ethics.",
            "I can employ epistemic truth adverbials, participial framing structures, and adversative rhetorical refutations.",
            "I can evaluate deliberative democracy models, journalistic integrity standards, and Márai Sándor's literary testament."
        ],
        [
            mc("grammar", "recognize", "Melyik kifejezés fejez ki megdönthetetlen tényszerű igazságot a sajtóelemzésben?", [
                "megdönthetetlen bizonyossággal / tényszerűen alátámasztott módon",
                "valószínűleg talán így történt tegnap",
                "érdekes pletykák alapján"
            ], 0, ["c1-adv-epistemic-discursive-truth"]),
            mc("grammar", "recognize", "Milyen szerkezettel leplezhetjük le a manipulatív sajtóhíreket?", [
                "a tényeket szándékosan elferdítő / a kontextusból kiragadott idézetekkel operáló",
                "szépen kinyomtatott színes képekkel díszített",
                "reggelente az újságos standon kapható"
            ], 0, ["c1-participle-manipulative-framing"]),
            match("vocabulary", "recognize", [["tényellenőrzés", "állítások valóságtartalmának szisztematikus vizsgálata"], ["karaktergyilkosság", "személy erkölcsi megsemmisítésére irányuló hadjárat"], ["deliberatív demokrácia", "racionális nyilvános érvelésen alapuló döntéshozatal"], ["nyelvrontás", "a fogalmak eltorzítása a propaganda által"], ["polgári ethosz", "a szabad és felelős egyén erkölcsi tartása"]], ["c1-26-vocab"]),
            fb("vocabulary", "recall", "A tények szándékos eltorzításával operáló sajtótevékenység a _____. (disinformation / dezinformáció)", "dezinformáció", "Press activity operating with intentional distortion of facts is disinformation.", ["c1-26-vocab"]),
            fb("vocabulary", "recall", "Az értelmiség elvtelen politikai behódolását az írástudók _____ nevezik. (treason / árulásának)", "árulásának", "The unprincipled political submission of intellectuals is called the treason of the intellectuals.", ["c1-26-vocab"]),
            fb("grammar", "recall", "A vizsgálat megdönthetetlen _____ cáfolta meg a valótlan vádakat. (certainty / bizonyossággal)", "bizonyossággal", "The investigation refuted untrue accusations with incontrovertible certainty.", ["c1-adv-epistemic-discursive-truth"]),
            fb("grammar", "context", "A kormányszóvivő állításával szemben a _____ a költségvetés hiánya nőtt. (in reality / valóságban)", "valóságban", "Contrary to the government spokesperson's claim, in reality the budget deficit increased.", ["c1-adv-adversative-rhetorical-refutation"]),
            fb("grammar", "context", "A tudósító szakmailag _____ módon végezte feltáró munkáját. (irreproachably / feddhetetlen)", "feddhetetlen", "The correspondent performed investigative work in a professionally irreproachable manner.", ["c1-adv-scalar-journalistic-integrity"]),
            mc("grammar", "context", "Mi a funkciója a 'nemhogy nem... hanem éppen ellenkezőleg' szerkezetnek a vitában?", [
                "Radikális ellentétezéssel mutat rá a hamis narratíva és a cáfoló valóság közötti teljes szakadékra.",
                "Megengedi a vitapartnernek, hogy elkerülje a választ.",
                "Elnézést kér az adatok pontatlansága miatt."
            ], 0, ["c1-adv-adversative-rhetorical-refutation"]),
            sb("grammar", "produce", ["A", "szabad", "nyilvánosság", "a", "demokrácia", "nélkülözhetetlen", "védőpajzsa."], ["A", "szabad", "nyilvánosság", "a", "demokrácia", "nélkülözhetetlen", "védőpajzsa."], "The free public sphere is the indispensable protective shield of democracy.", ["c1-modal-deliberative-public-sphere"]),
            sw("production", [{"prompt": "Formulate a statement debunking media distortion using an adversative connector.", "answer": "A propagandamédia állításaival szemben a valóságban a független források igazolhatóan cáfolták a koholt vádakat, megdönthetetlen bizonyossággal állítva helyre az igazságot."}], ["c1-adv-adversative-rhetorical-refutation"]),
            sw("production", [{"prompt": "Write a critical reflection on Márai Sándor's defense of language and free press.", "answer": "Márai Sándor naplójában világossá tette: a szabad sajtó megfojtása a nyelv megmérgezéséhez és a szellemi élet pusztulásához vezet, ezért a legszigorúbb erkölcsi mércével mérve kell őriznünk a független szót."}], ["c1-adv-scalar-journalistic-integrity"])
        ]
    )

    # ----------------------------------------------------
    # TRACK 2: DISCOURSE (c1-mediaszabadsag)
    # ----------------------------------------------------
    slug = "mediaszabadsag"
    disc_intro = [
        "Over the past decade, Hungary's media landscape underwent an unprecedented structural transformation. Through the consolidation of nearly 500 outlets under the Central European Press and Media Foundation (KESMA), the subjugation of the public broadcaster (MTVA), and the weaponization of state advertising, the government erected an all-encompassing media hegemony.",
        "In this discourse unit, through five serialized investigative accounts, you will analyze the mechanics of media capture, editorial resistance, crowdfunding breakthroughs (Index and Telex), and the defense of the free press against 'sovereignty protection' campaigns at the C1 level."
    ]

    disc_lessons = [
        {
            "num": 1,
            "stem": f"c1-{slug}-01",
            "title": "The KESMA Mega-Foundation & Media Capture Framing",
            "grammar_title": "Discourse Framing Markers Diagnosing Systemic Media Capture and Conglomerate Monopolization",
            "grammar_skill": "c1-discourse-media-capture-framing",
            "goals": [
                "I can analyze the creation of KESMA, the concentration of media ownership, and national strategic exemptions (*médiakoncentráció, nemzetstratégiai jelentőségűvé minősítés, KESMA-alapítvány, piacfelügyelet hiánya*).",
                "I can deploy discourse framing markers diagnosing systemic media capture (*a nyilvánosság szisztematikus centralizálása, a médiaegyensúly drasztikus felborulása, államilag vezérelt médiabirodalom keretében*).",
                "I can debate how antimonopoly competition laws were bypassed in the media sector."
            ],
            "vocab": [
                {"lemma": "KESMA", "translation": "Central European Press and Media Foundation", "pos": "noun"},
                {"lemma": "médiakoncentráció", "translation": "media concentration", "pos": "noun"},
                {"lemma": "nemzetstratégiai jelentőség", "translation": "national strategic significance", "pos": "expression"},
                {"lemma": "piacfelügyelet kiiktatása", "translation": "bypassing of market competition oversight", "pos": "expression"},
                {"lemma": "médiahegemónia", "translation": "media hegemony", "pos": "noun"},
                {"lemma": "vidéki sajtó felszámolása", "translation": "liquidation of independent regional press", "pos": "expression"},
                {"lemma": "egyhangúsítás", "translation": "uniformization / bringing into line", "pos": "noun"},
                {"lemma": "oligarchikus tulajdon", "translation": "oligarchic ownership", "pos": "expression"}
            ],
            "gr_text1": "Discourse framing markers diagnose media monopolization and institutional capture: `a nyilvánosság szisztematikus centralizálása révén` (through the systematic centralization of the public sphere), `a médiaegyensúly drasztikus és visszafordíthatatlan felborulása` (the drastic and irreversible tilting of media balance), `egy államilag vezérelt és közpénzből táplált médiabirodalom keretében` (within the framework of a state-guided media empire fed by public funds).",
            "gr_text2": "Example: `A szakértők a nyilvánosság szisztematikus centralizálásaként értékelték a KESMA létrehozását és a GVH versenyfelügyeleti jogkörének rendeleti kiiktatását`.",
            "gr_table": [
                ["A KESMA létrehozásával a nyilvánosság szisztematikus centralizálása valósult meg.", "With the creation of KESMA systematic centralization of the public sphere was realized."],
                ["A médiaegyensúly drasztikus felborulása ellehetetleníti a kiegyensúlyozott tájékozódást.", "The drastic tilting of media balance renders balanced information impossible."],
                ["Az államilag vezérelt konglomerátum uralja a teljes vidéki napilappiacot.", "The state-guided conglomerate dominates the entire regional daily newspaper market."]
            ],
            "world_story_seg": {
                "seg_slug": "kesma-letrehozasa",
                "title": "A KESMA-monolit és a versenyfelügyelet kiiktatása",
                "summary": "2018 őszén egyetlen nap leforgása alatt csaknem ötszáz kormánypárti médium tulajdonjogát adták át a KESMA alapítványnak, amit a kormány azonnal nemzetstratégiai jelentőségűvé nyilvánított.",
                "paragraphs": [
                    {"type": "narration", "text": "2018 novemberének egyik hűvös reggelén példátlan esemény rázta meg a magyar médiapiacot: a kormánypárti oligarchák mintegy ötszáz televíziós, rádiós, nyomtatott és online médiumukat 'önkéntes adományként' egyetlen központi alapítványnak, a KESMA-nak ajándékozták."},
                    {"type": "dialogue", "speaker": "Kovács Anna médiajogász", "text": "A versenyhivatali vizsgálat elmaradása nem véletlen volt: a kormány egyetlen tollvonással 'nemzetstratégiai jelentőségű összefonódássá' minősítette a fúziót, megakadályozva, hogy a Gazdasági Versenyhivatal vagy a Médiatanács vizsgálhassa a gigantikus monopolhelyzetet."},
                    {"type": "narration", "text": "A nyilvánosság szisztematikus centralizálása a vidéki lakosság körében volt a legpusztítóbb hatású: a megyei napilapok mindegyike központi propagandaszövegeket közölt, elzárva a vidéki polgárokat a plurális hírforrásoktól."},
                    {"type": "narration", "text": "A médiaegyensúly drasztikus felborulása nemzetközi elemzők szerint a modern Európa legkiterjedtebb államilag irányított véleménymonopóliumát hozta létre."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Hogyan akadályozta meg a kormány a KESMA-fúzió versenyjogi vizsgálatát 2018-ban?", [
                    "Kormányrendelettel nemzetstratégiai jelentőségűvé nyilvánította az összefonódást, kizárva a Gazdasági Versenyhivatal eljárását.",
                    "Megvette az Európai Versenyhivatalt.",
                    "Elrendelte, hogy minden újságot postán küldjenek el a miniszterelnöknek."
                ], 0, ["c1-mediaszabadsag-vocab"]),
                fb("grammar", "controlled", "A szakemberek a nyilvánosság _____ centralizálásaként diagnosztizálták a médiabirodalom kialakulását. (systematic / szisztematikus)", "szisztematikus", "Experts diagnosed the development of the media empire as the systematic centralization of the public sphere.", ["c1-discourse-media-capture-framing"]),
                match("vocabulary", "controlled", [["KESMA", "ötszáz kormánypárti médiumot tömörítő alapítvány"], ["médiakoncentráció", "a tulajdon és irányítás szűk körben való összpontosulása"], ["nemzetstratégiai jelentőség", "versenyfelügyeletet kizáró kormányzati jogi minősítés"], ["médiahegemónia", "egyoldalú, kizárólagos médiahatalmi uralom"]], ["c1-mediaszabadsag-vocab"]),
                fb("grammar", "practice", "A médiaegyensúly drasztikus _____ nyomán a vidéki nyilvánosságban megszűnt a pluralizmus. (tilting / felborulása)", "felborulása", "Following the drastic tilting of media balance, pluralism ceased in the regional public sphere.", ["c1-discourse-media-capture-framing"]),
                sb("grammar", "practice", ["A", "nyilvánosság", "szisztematikus", "centralizálása", "felszámolta", "a", "piaci", "versenyt."], ["A", "nyilvánosság", "szisztematikus", "centralizálása", "felszámolta", "a", "piaci", "versenyt."], "The systematic centralization of the public sphere eliminated market competition.", ["c1-discourse-media-capture-framing"]),
                dc("dialogue", [
                    {"speaker": "Újságíró", "text": "Milyen következménye volt a megyei napilapok beolvasztásának a KESMA-ba?"},
                    {"speaker": "Médiakutató", "text": "A nyilvánosság szisztematikus _____ nyomán minden megyében ugyanazokat a központi vezércikkeket közölték szó szerint."},
                    {"speaker": "Újságíró", "text": "Így számolták fel a független helyi tájékoztatást."}
                ], ["centralizálása", "szétszórása", "megnyitása"], 0, ["c1-discourse-media-capture-framing"]),
                sw("production", [{"prompt": "Write a critical diagnosis of media capture using a crisis framing marker.", "answer": "A KESMA létrehozása és a versenyfelügyelet kiiktatása a nyilvánosság szisztematikus centralizálásához, valamint a magyar médiaegyensúly drasztikus és mesterséges felborulásához vezetett."}], ["c1-discourse-media-capture-framing"]),
                mc("grammar", "check", "Melyik kifejezés diagnosztizálja a médiakoncentrációt a legpontosabb társadalomtudományi nyelven?", [
                    "a nyilvánosság szisztematikus centralizálása / a médiaegyensúly drasztikus felborulása",
                    "túl sok betű van a hírekben",
                    "olcsóbbá vált az újságpapír ára"
                ], 0, ["c1-discourse-media-capture-framing"])
            ]
        },
        {
            "num": 2,
            "stem": f"c1-{slug}-02",
            "title": "Public Broadcaster Subjugation & Deontic Mandates",
            "grammar_title": "Deontic Modal Structures Critiquing State Broadcaster Capture and Bias",
            "grammar_skill": "c1-modal-deontic-public-broadcasting",
            "goals": [
                "I can analyze the capture of the public broadcaster (MTVA), editorial blacklists, and scripted news reports (*közmédia elfoglalása, MTVA, feketelista, előre megírt kérdések*).",
                "I can construct deontic modal structures condemning broadcaster bias (*nem viselkedhet kormányszócsőként, köteles megszólaltatni az ellenzéket, nem alkalmazhat politikai cenzúrát*).",
                "I can critique how annual public funding (over 140 billion HUF) is used for partisan communications."
            ],
            "vocab": [
                {"lemma": "közmédia elfoglalása", "translation": "capture of public media", "pos": "expression"},
                {"lemma": "MTVA", "translation": "Media Services and Support Trust Fund", "pos": "noun"},
                {"lemma": "szerkesztőségi feketelista", "translation": "editorial blacklist", "pos": "expression"},
                {"lemma": "kormányszócső", "translation": "government mouthpiece", "pos": "noun"},
                {"lemma": "pártatlan tájékoztatás hiánya", "translation": "lack of impartial reporting", "pos": "expression"},
                {"lemma": "ellenzéki megszólalás tiltása", "translation": "barring opposition voices", "pos": "expression"},
                {"lemma": "közpénzfelhasználás", "translation": "utilization of public funds", "pos": "noun"},
                {"lemma": "hírhamisítás", "translation": "news fabrication / manipulation", "pos": "noun"}
            ],
            "gr_text1": "Deontic modal structures articulate statutory public-service requirements breached by state media: `a közmédiának nem szabadna kormányszócsőként funkcionálnia` (public media should not function as a government mouthpiece), `köteles volna biztosítani a pártatlan tájékoztatást` (would be obligated to ensure impartial reporting), `nem alkalmazhat politikai feketelistákat` (cannot apply political blacklists), `garantálnia kell az ellenzéki vélemények megjelenítését` (must guarantee representation of opposition opinions).",
            "gr_text2": "Example: `A médiatörvény értelmében az MTVA köteles volna pártatlanul, a közpénzekből gazdálkodva kiegyensúlyozottan tájékoztatni, és nem viselkedhetne pártpolitikai fegyverként`.",
            "gr_table": [
                ["A közmédia nem viselkedhet a mindenkori kormányzó hatalom szócsöveként.", "Public media cannot behave as the mouthpiece of ruling power."],
                ["Az MTVA köteles volna egyenlő megszólalási időt biztosítani a vitákban.", "MTVA would be obligated to provide equal speaking time in debates."],
                ["A szerkesztőség nem alkalmazhat titkos politikai tiltólistákat.", "The editorial office cannot apply secret political blacklists."]
            ],
            "world_story_seg": {
                "seg_slug": "mtva-kormanypropaganda",
                "title": "A közmédia megszállása és a szerkesztőségi feketelisták",
                "summary": "Az adófizetők évi több mint 140 milliárd forintjából fenntartott MTVA épületében kiszivárgott felvételek tanúsították a szerkesztői utasításokat és az ellenzéki politikusok elhallgatását.",
                "paragraphs": [
                    {"type": "narration", "text": "A budapesti Kunigunda utcai gyártóbázis zárt falai között a közszolgálatiság eszménye nyomtalanul elenyészett. Kiszivárgott hangfelvételeken a főszerkesztők nyíltan instruálták a munkatársakat: aki nem a kormányzati narratívát képviseli, annak fel is lehet mondani."},
                    {"type": "dialogue", "speaker": "Kovács Anna", "text": "A törvény kógens módon írja elő a kiegyensúlyozottságot: az MTVA nem viselkedhetne kormányszócsőként. Az, hogy az ellenzéki vezetők éveken át egyetlen perc élő megszólalást sem kaptak, a közpénzek kirívó elpazarlása és jogtiprás."},
                    {"type": "narration", "text": "Amikor 2018 decemberében parlamenti képviselők léptek be az MTVA épületébe, hogy beolvassák öt pontjukat, biztonsági őrök erőszakkal dobták ki őket a székházból."},
                    {"type": "narration", "text": "A közmédia a közös nemzeti tájékoztatás helyett a politikai ellenfelek lejáratásának és az oroszbarát dezinformáció közvetítésének első számú hazai bázisává vált."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Hogyan működtek a szerkesztőségi feketelisták az MTVA-ban a kiszivárgott hírek szerint?", [
                    "Meghatározták azon civil szakértők, jogvédők és ellenzéki politikusok névsorát, akiket tilos volt megszólaltatni a hírműsorokban.",
                    "Fekete színű borítékban küldték ki a jutalmakat a riportereknek.",
                    "Kizárólag fekete-fehér televíziókon engedték nézni az adást."
                ], 0, ["c1-mediaszabadsag-vocab"]),
                fb("grammar", "controlled", "A közszolgálati adónak nem _____ pártpropaganda közvetítőjeként működnie. (should not / szabadna)", "szabadna", "The public service channel should not operate as a conduit for party propaganda.", ["c1-modal-deontic-public-broadcasting"]),
                match("vocabulary", "controlled", [["MTVA", "állami médiumokat működtető vagyonkezelő alap"], ["szerkesztőségi feketelista", "nemkívánatos megszólalók titkos tiltólistája"], ["kormányszócső", "kormányzati érdekeket kritikátlanul szajkózó médium"], ["hírhamisítás", "képek és mondatok valótlan összevágása"]], ["c1-mediaszabadsag-vocab"]),
                fb("grammar", "practice", "A közmédiának törvényi kötelessége _____ a demokratikus véleménynyilvánítás szabadságát. (would be / volna)", "volna", "It would be the statutory duty of public media to guarantee freedom of democratic expression.", ["c1-modal-deontic-public-broadcasting"]),
                sb("grammar", "practice", ["A", "közmédia", "nem", "alkalmazhat", "politikai", "feketelistákat", "a", "híradóban."], ["A", "közmédia", "nem", "alkalmazhat", "politikai", "feketelistákat", "a", "híradóban."], "Public media cannot apply political blacklists in news broadcasts.", ["c1-modal-deontic-public-broadcasting"]),
                dc("dialogue", [
                    {"speaker": "Polgár", "text": "Miért fizetünk évi 140 milliárd adóforintot az állami tévének?"},
                    {"speaker": "Jogász", "text": "A közmédiának a közérdeket _____ szolgálnia, nem pedig egyetlen párt kampánygépezeteként működnie."},
                    {"speaker": "Polgár", "text": "Ez a közpénzek botrányos visszaélése."}
                ], ["kellene", "tilos", "szabad"], 0, ["c1-modal-deontic-public-broadcasting"]),
                sw("production", [{"prompt": "Write a sentence critiquing state media capture using a deontic modal structure.", "answer": "Az állami költségvetésből fenntartott közmédiának nem szabadna kormányszócsőként elhallgatnia a társadalmi valóságot, hanem kötelessége volna pártatlan vitateret biztosítani."}], ["c1-modal-deontic-public-broadcasting"]),
                mc("grammar", "check", "Melyik modális kifejezés marasztalja el a közmédia elfogultságát a legerősebben?", [
                    "nem viselkedhet kormányszócsőként / nem alkalmazhat feketelistákat",
                    "időnként elnézést kérhetne a műsorért",
                    "táncolhatna egy jót a stúdióban"
                ], 0, ["c1-modal-deontic-public-broadcasting"])
            ]
        },
        {
            "num": 3,
            "stem": f"c1-{slug}-03",
            "title": "State Advertising Distortion & Proportional Correlatives",
            "grammar_title": "Proportional Correlative Conjunctions Mapping State Advertising Distortion and Market Foreclosure",
            "grammar_skill": "c1-adv-proportional-advertising-distortion",
            "goals": [
                "I can analyze the weaponization of state advertising, market distortion, and private advertiser intimidation (*állami hirdetések fegyverként használata, piactorzítás, magánhirdetők megfélemlítése*).",
                "I can deploy proportional correlative structures mapping market foreclosure (*minél több állami forrást pumpálnak a kormánymédiába, annál nehezebb helyzetbe kerülnek a független lapok*).",
                "I can evaluate economic models of media financial viability under illiberal state pressure."
            ],
            "vocab": [
                {"lemma": "állami hirdetések", "translation": "state advertising / government ads", "pos": "expression"},
                {"lemma": "piactorzítás", "translation": "market distortion", "pos": "noun"},
                {"lemma": "reklámpiaci elvonás", "translation": "ad market deprivation / starvation", "pos": "expression"},
                {"lemma": "hirdetői megfélemlítés", "translation": "advertiser intimidation", "pos": "expression"},
                {"lemma": "közpénz-finanszírozott média", "translation": "public-money-funded media", "pos": "expression"},
                {"lemma": "gazdasági fojtogatás", "translation": "economic strangulation", "pos": "expression"},
                {"lemma": "olvasói támogatás", "translation": "reader contributions / crowdfunding", "pos": "expression"},
                {"lemma": "piaci életképesség", "translation": "market viability", "pos": "expression"}
            ],
            "gr_text1": "Proportional correlative structures map the direct causal link between the influx of non-market state subsidies and the shrinking of independent commercial journalism: `Minél több százmilliárdot öntenek az állami hirdetésekbe, annál inkább torzul a média piaci működése` (The more hundreds of billions they pour into state ads, the more media market operations distort), `Amilyen mértékben kiszorítják a független sajtót a reklámpiacról, olyan arányban nő az olvasói előfizetések életmentő jelentősége` (In proportion as independent press is squeezed out of the ad market, to that extent the life-saving importance of reader subscriptions grows).",
            "gr_text2": "Example: `Minél inkább politikai szempontok alapján osztják el az állami reklámköltést, annál kevésbé érvényesül a valódi piaci verseny`.",
            "gr_table": [
                ["Minél több közpénzt kap a kormánysajtó, annál sebezhetőbbé válnak a piaci szereplők.", "The more public money government press receives, the more vulnerable market players become."],
                ["Amilyen mértékben szűkül a hirdetési piac, olyan arányban növekszik a közösségi finanszírozás súlya.", "To the extent the advertising market narrows, to that extent the weight of crowdfunding increases."],
                ["Minél durvább az állami piactorzítás, annál nagyobb hősies kitartás kell a független szerkesztőségeknek.", "The cruder state market distortion is, the greater heroic perseverance independent newsrooms need."]
            ],
            "world_story_seg": {
                "seg_slug": "allami-hirdetesek-fegyvere",
                "title": "Az állami hirdetések mint gazdasági fojtogató fegyver",
                "summary": "A magyar állam lett a reklámpiac legnagyobb megrendelője: a kék plakátok és kormányzati hirdetések milliárdjai kizárólag a lojális oligarchák médiáját gazdagították, kiszárítva a független sajtót.",
                "paragraphs": [
                    {"type": "narration", "text": "Az illiberális médiapolitika leghatékonyabb eszköze nem a nyílt cenzúra volt, hanem a pénzcsapok egyoldalú megnyitása és elzárása. Az állami szervek, a Szerencsejáték Zrt. és az MVM évi tízmilliárdos reklámbüdzséjét matematikai pontossággal csatornázták a kormánypárti médiumokba."},
                    {"type": "dialogue", "speaker": "Kovács Anna", "text": "Minél több állami pénzt pumpáltak a propagandába, annál inkább kiszorultak a független lapok a reklámpiacról. A magáncégek féltek hirdetni a független felületeken, rettegve a NAV ellenőrzéseitől és a politikai retorziótól."},
                    {"type": "narration", "text": "Ez a gazdasági aszimmetria példátlan piactorzulást eredményezett: míg a kormánysajtó olvasottság nélkül is százmilliárdos nyereséget termelt, a piacvezető független portálok a túlélésért küzdöttek."},
                    {"type": "narration", "text": "A magyar média fennmaradása a kereskedelmi modellről fokozatosan az olvasói közösség önfeláldozó támogatására helyeződött át."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Hogyan torzította el a magyar reklámpiacot az állami hirdetések elosztása?", [
                    "Az állam lett a legnagyobb hirdető, és a forrásokat kizárólag a kormánypárti sajtónak juttatta, gazdaságilag fojtogatva a független médiát.",
                    "Az állam megtiltotta a színes reklámok közzétételét.",
                    "Csak a külföldi autómárkák kaphattak reklámfelületet a lapokban."
                ], 0, ["c1-mediaszabadsag-vocab"]),
                fb("grammar", "controlled", "Minél több állami hirdetést kap a kormánymédia, _____ súlyosabb piactorzulás következik be. (the more / annál)", "annál", "The more state advertising government media receives, the more severe market distortion occurs.", ["c1-adv-proportional-advertising-distortion"]),
                match("vocabulary", "controlled", [["állami hirdetések", "kormányzati pénzből fizetett politikai reklámok"], ["piactorzítás", "a szabad piaci verseny mesterséges felborítása"], ["hirdetői megfélemlítés", "magáncégek elriasztása a független médiától"], ["olvasói támogatás", "közösségi mikroadományok a szerkesztőség védelmére"]], ["c1-mediaszabadsag-vocab"]),
                fb("grammar", "practice", "Amilyen mértékben szűkül a reklámpiac, olyan _____ válik nélkülözhetetlenné az előfizetők szerepe. (proportion / arányban)", "arányban", "In proportion as the advertising market narrows, to that extent the role of subscribers becomes indispensable.", ["c1-adv-proportional-advertising-distortion"]),
                sb("grammar", "practice", ["Minél", "nagyobb", "a", "nyomás,", "annál", "erősebb", "az", "olvasói", "szolidaritás."], ["Minél", "nagyobb", "a", "nyomás,", "annál", "erősebb", "az", "olvasói", "szolidaritás."], "The greater the pressure, the stronger reader solidarity.", ["c1-adv-proportional-advertising-distortion"]),
                dc("dialogue", [
                    {"speaker": "Kiadóvezető", "text": "Túlélhet-e egy független újság pusztán piaci hirdetésekből ma Magyarországon?"},
                    {"speaker": "Médiaelemző", "text": "Aligha; minél inkább elzárják az állami forrásokat, _____ inkább csak az olvasók közvetlen adományai menthetik meg a függetlenséget."},
                    {"speaker": "Kiadóvezető", "text": "Ezért vezettük be a tagsági rendszert."}
                ], ["annál", "soha", "mindig"], 0, ["c1-adv-proportional-advertising-distortion"]),
                sw("production", [{"prompt": "Write a sentence analyzing advertising market distortion using 'Minél... annál...'.", "answer": "Minél több közpénzt pumpál a kormány a lojális sajtóorgánumokba állami hirdetések formájában, annál mélyebbé válik a reklámpiac mesterséges torzulása."}], ["c1-adv-proportional-advertising-distortion"]),
                mc("grammar", "check", "Melyik szerkezet írja le a piacvesztés és az olvasói függőség dinamikáját a legpontosabban?", [
                    "Minél több forrást vonnak el... annál inkább felértékelődik / Amilyen mértékben... olyan arányban",
                    "Ha süt a nap, kimegyünk a strandra",
                    "Nemcsak szép, de gazdag is"
                ], 0, ["c1-adv-proportional-advertising-distortion"])
            ]
        },
        {
            "num": 4,
            "stem": f"c1-{slug}-04",
            "title": "Index to Telex, Digital Resistance & Epistemic Stigma",
            "grammar_title": "Epistemic Stance Markers Exposing Smear Campaigns and Foreign Agent Rhetoric",
            "grammar_skill": "c1-epistemic-propaganda-stigmatization",
            "goals": [
                "I can analyze the 2020 mass resignation at Index.hu, the launch of Telex.hu, and digital reader crowdfunding (*Index-felmondás, Telex elindulása, közösségi finanszírozás, Szuverenitásvédelmi Hivatal*).",
                "I can employ epistemic stance markers exposing smear campaigns and 'foreign agent' rhetoric (*nyilvánvalóan megbélyegző jelleggel, minden alapot nélkülöző rágalomként, politikai megrendelésre*).",
                "I can critique how independent digital newsrooms defend themselves against state-sponsored stigmatization."
            ],
            "vocab": [
                {"lemma": "Index-felmondás", "translation": "mass resignation at Index (July 2020)", "pos": "noun"},
                {"lemma": "Telex", "translation": "Telex.hu (reader-funded portal)", "pos": "noun"},
                {"lemma": "Szuverenitásvédelmi Hivatal", "translation": "Sovereignty Protection Office", "pos": "noun"},
                {"lemma": "külföldi ügynöközés", "translation": "foreign agent smearing", "pos": "expression"},
                {"lemma": "közösségi mikrofinanszírozás", "translation": "reader micro-donations", "pos": "expression"},
                {"lemma": "szerkesztőségi felállás", "translation": "collective editorial resignation", "pos": "expression"},
                {"lemma": "stigmatizáció", "translation": "stigmatization", "pos": "noun"},
                {"lemma": "oknyomozó műhely", "translation": "investigative workshop (Direkt36, Átlátszó)", "pos": "expression"}
            ],
            "gr_text1": "Epistemic stance markers articulate unequivocal factual and ethical assessments debunking state propaganda smear tactics: `nyilvánvalóan megbélyegző jelleggel` (with a manifestly stigmatizing character), `minden valóságalapot nélkülöző politikai rágalomként` (as a political slander lacking all basis in reality), `vélelmezhetően a szabad sajtó elhallgattatására törekedve` (presumptively striving to silence the free press), `joggal tekinthető a szuverenitásvédelmi retorika visszaélésének` (can rightfully be considered an abuse of sovereignty protection rhetoric).",
            "gr_text2": "Example: `A független újságírók elleni külföldi ügynöközés nyilvánvalóan megbélyegző jelleggel, minden ténybeli alapot nélkülözve igyekszik aláásni a társadalmi bizalmat`.",
            "gr_table": [
                ["A vádak nyilvánvalóan megbélyegző jelleggel készültek a sajtó lejáratására.", "The accusations were made with a manifestly stigmatizing character to discredit the press."],
                ["Minden alapot nélkülöző állításnak bizonyult a külföldi befolyásolás vádja.", "The accusation of foreign interference proved to be an assertion lacking all basis."],
                ["A szerkesztőség elleni támadás joggal tekinthető a szuverenitásvédelem politikai fegyverének.", "The attack against the newsroom can rightfully be considered a political weapon of sovereignty protection."]
            ],
            "world_story_seg": {
                "seg_slug": "index-felmondas-telex",
                "title": "Az Index felmondása, a Telex születése és az ügynökvádak",
                "summary": "2020 júliusában az Index több mint nyolcvan munkatársa mondott fel a függetlenség veszélybe kerülése miatt, majd megalapították a Telexet. A hatalom hamarosan 'külföldi ügynökként' támadta az oknyomozókat.",
                "paragraphs": [
                    {"type": "narration", "text": "Amikor 2020 nyarán az Index főszerkesztőjét menesztették a politikai nyomásgyakorlás elleni tiltakozása miatt, a szerkesztőség ritkán látott szolidaritással válaszolt: több mint nyolcvan újságíró adta be felmondását egyetlen napon. Nem voltak hajlandók cenzúrázott kompromisszumok között dolgozni."},
                    {"type": "dialogue", "speaker": "Kovács Anna", "text": "A Telex elindulása és a rekordgyorsasággal összegyűjtött olvasói támogatás a magyar polgári nyilvánosság diadalmas pillanata volt. Bebizonyosodott, hogy a magyar közönség hajlandó fizetni a cenzúrázatlan valóságért."},
                    {"type": "narration", "text": "A hatalom válasza nem késett: megalakult a Szuverenitásvédelmi Hivatal, amely a független sajtót és oknyomozó műhelyeket (Direkt36, Átlátszó) 'külföldi érdekeket szolgáló ügynökökként' igyekezett megbélyegezni."},
                    {"type": "narration", "text": "Ezek a vádak nyilvánvalóan megbélyegző jelleggel, minden ténybeli alapot nélkülözve próbálták megfélemlíteni a korrupciós ügyeket feltáró bátor riportereket."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Miért mondott fel az Index szerkesztősége szinte teljes egészében 2020 júliusában?", [
                    "Mert a főszerkesztő elbocsátása után úgy ítélték meg, hogy a lap tulajdonosi háttere és függetlensége végleg ellehetetlenült a politikai befolyás miatt.",
                    "Mert a szerkesztőség tagjai közösen nyertek a lottón.",
                    "Mert leállt az internetkapcsolat a szerkesztőségben."
                ], 0, ["c1-mediaszabadsag-vocab"]),
                fb("grammar", "controlled", "A független újságírók elleni kampány _____ megbélyegző jelleggel indult el. (manifestly / nyilvánvalóan)", "nyilvánvalóan", "The campaign against independent journalists was launched with a manifestly stigmatizing character.", ["c1-epistemic-propaganda-stigmatization"]),
                match("vocabulary", "controlled", [["Index-felmondás", "nyolcvan újságíró bátor kiállása és közös felmondása"], ["Telex", "olvasói támogatásból született piacvezető hírportál"], ["Szuverenitásvédelmi Hivatal", "független szervezeteket vizsgáló állami hatóság"], ["külföldi ügynöközés", "független újságírók hazaárulással való megbélyegzése"]], ["c1-mediaszabadsag-vocab"]),
                fb("grammar", "practice", "A rágalom minden ténybeli alapot _____ politikai támadásnak bizonyult. (lacking / nélkülöző)", "nélkülöző", "The slander proved to be a political attack lacking all factual basis.", ["c1-epistemic-propaganda-stigmatization"]),
                sb("grammar", "practice", ["A", "közösségi", "finanszírozás", "biztosítja", "a", "szerkesztőségek", "független", "működését."], ["A", "közösségi", "finanszírozás", "biztosítja", "a", "szerkesztőségek", "független", "működését."], "Community financing secures newsrooms' independent operation.", ["c1-epistemic-propaganda-stigmatization"]),
                dc("dialogue", [
                    {"speaker": "Külpolitikai riporter", "text": "Hogyan reagált a szakma a Szuverenitásvédelmi Hivatal jelentéseire?"},
                    {"speaker": "Főszerkesztő", "text": "Ezek a dokumentumok nyilvánvalóan _____ jelleggel íródtak a kritikus hangok elfojtására."},
                    {"speaker": "Külpolitikai riporter", "text": "Ezért perelte be több szerkesztőség is a hivatalt."}
                ], ["megbélyegző", "hasznos", "tudományos"], 0, ["c1-epistemic-propaganda-stigmatization"]),
                sw("production", [{"prompt": "Write a sentence exposing state smear campaigns using an epistemic stance marker.", "answer": "Az oknyomozó újságírók elleni külföldi ügynökvádak nyilvánvalóan megbélyegző jelleggel, minden valós bizonyítékot nélkülözve igyekeznek elhallgattatni a korrupciót feltáró cikkeket."}], ["c1-epistemic-propaganda-stigmatization"]),
                mc("grammar", "check", "Melyik episztemikus kifejezés leplezi le a politikai rágalomhadjáratokat a legmeggyőzőbben?", [
                    "nyilvánvalóan megbélyegző jelleggel / minden ténybeli alapot nélkülözve",
                    "talán nem a legkedvesebb szavakkal",
                    "kissé sietősen megírva"
                ], 0, ["c1-epistemic-propaganda-stigmatization"])
            ]
        },
        {
            "num": 5,
            "stem": f"c1-{slug}-05",
            "title": "Independent Media Resilience & Conclusive Defense",
            "grammar_title": "Evaluative Synthesis Particles Formulating Manifestos for Independent Media Resilience",
            "grammar_skill": "c1-adv-conclusive-free-press-defense",
            "goals": [
                "I can analyze digital newsroom resilience, the European Media Freedom Act (EMFA), and international press solidarity.",
                "I can employ evaluative synthesis particles formulating free press manifestos (*végső soron nélkülözhetetlen, összegzésként leszögezhető, mindent egybevetve a demokratikus nyilvánosság záloga*).",
                "I can articulate visionary arguments for the survival of independent journalism in Hungary."
            ],
            "vocab": [
                {"lemma": "European Media Freedom Act", "translation": "European Media Freedom Act (EMFA)", "pos": "expression"},
                {"lemma": "digitális ellenállóképesség", "translation": "digital media resilience", "pos": "expression"},
                {"lemma": "olvasói közösség", "translation": "community of readers / patrons", "pos": "expression"},
                {"lemma": "szerkesztőségi függetlenség", "translation": "editorial independence", "pos": "expression"},
                {"lemma": "hírlevél-modell", "translation": "newsletter publishing model", "pos": "expression"},
                {"lemma": "podcast-kultúra", "translation": "independent podcast culture", "pos": "expression"},
                {"lemma": "transzparens működés", "translation": "transparent operation", "pos": "expression"},
                {"lemma": "demokratikus nyilvánosság záloga", "translation": "pledge of democratic public sphere", "pos": "expression"}
            ],
            "gr_text1": "Evaluative synthesis particles formulate definitive manifestos defending the non-negotiable role of free speech in society: `végső soron nélkülözhetetlen a szabad társadalom számára` (ultimately indispensable for a free society), `mindent egybevetve a demokratikus nyilvánosság záloga` (all in all the pledge of the democratic public sphere), `konklúzióként leszögezhető` (can be stated as a conclusion), `összességében tekintve a túlélés egyetlen garanciája` (taking it as a whole the sole guarantee of survival).",
            "gr_text2": "Example: `Végső soron nélkülözhetetlen a független szerkesztőségek létezése, hiszen a kritikus sajtó mindent egybevetve a demokratikus nyilvánosság legfőbb záloga`.",
            "gr_table": [
                ["Végső soron nélkülözhetetlen az olvasók tudatos és kitartó támogatása.", "Ultimately readers' conscious and persevering support is indispensable."],
                ["Mindent egybevetve a szabad sajtó a demokrácia fennmaradásának legfőbb záloga.", "All in all the free press is the supreme pledge of democracy's survival."],
                ["Konklúzióként leszögezhető, hogy a digitális független média ellenállt az állami hegemóniának.", "It can be stated as a conclusion that independent digital media resisted state hegemony."]
            ],
            "world_story_seg": {
                "seg_slug": "fuggetlen-media-jovoje",
                "title": "A szabad sajtó védőbástyái és az európai horizont",
                "summary": "A politikai és gazdasági nyomásgyakorlás ellenére a magyar digitális sajtó (Telex, 444, 24.hu, HVG, Válasz Online) a régió egyik legéleterősebb független nyilvánosságát teremtette meg.",
                "paragraphs": [
                    {"type": "narration", "text": "Ha valaki 2018-ban végignézett a KESMA megalakulásán és a Népszabadság bezárásán, azt hihette, hogy a magyar független média éveken belül megsemmisül. Ám a történelem más utat járt be: a magyar digitális szerkesztőségek hihetetlen innovációval és kitartással szervezték újjá magukat."},
                    {"type": "dialogue", "speaker": "Kovács Anna", "text": "Az olvasók tízezrei ismerték fel: ha nem fizetnek a valóságért, a propaganda fog dönteni helyettük. A hírlevelek, podcastok, oknyomozó könyvek és közösségi klubok új polgári nyilvánosságot teremtettek a központosított állami gépezettel szemben."},
                    {"type": "narration", "text": "Az Európai Unió Médiaszabadság Törvénye (EMFA) új védelmi hálót kínál az állami hirdetések átláthatóságára és a szerkesztőségek védelmére. Ám a valódi erőt nem a brüsszeli jogszabályok, hanem a mindennapi újságírói bátorság jelenti."},
                    {"type": "narration", "text": "Végső soron nélkülözhetetlen kimondani: mindent egybevetve a szabad sajtó nem a politika ellensége, hanem a nemzet lelkiismeretének és demokratikus jövőjének egyetlen igaz védőbástyája."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Milyen célt szolgál az Európai Médiaszabadság Törvény (EMFA)?", [
                    "Megvédi az újságírókat a politikai beavatkozástól, kötelezővé teszi az állami hirdetések átláthatóságát és tiltja a szerkesztőségek kémprogramokkal való lehallgatását.",
                    "Betiltja a külföldi filmek sugárzását az európai televíziókban.",
                    "Előírja, hogy minden európai újságot latin betűkkel kell nyomtatni."
                ], 0, ["c1-mediaszabadsag-vocab"]),
                fb("grammar", "controlled", "_____ soron nélkülözhetetlen a szabad és független újságírói műhelyek létezése. (Ultimately / Végső)", "Végső", "Ultimately the existence of free and independent journalistic workshops is indispensable.", ["c1-adv-conclusive-free-press-defense"]),
                match("vocabulary", "controlled", [["European Media Freedom Act", "európai törvény a média függetlenségének védelmére"], ["digitális ellenállóképesség", "szerkesztőségek rugalmas túlélési képessége"], ["transzparens működés", "nyilvános és elszámoltatható gazdálkodás"], ["demokratikus nyilvánosság záloga", "a polgárok szabadságának alapvető feltétele"]], ["c1-mediaszabadsag-vocab"]),
                fb("grammar", "practice", "Mindent _____, az olvasói közösség a független magyar sajtó legerősebb pajzsa. (taking into account / egybevetve)", "egybevetve", "All in all, the community of readers is the strongest shield of the independent Hungarian press.", ["c1-adv-conclusive-free-press-defense"]),
                sb("grammar", "practice", ["Végső", "soron", "nélkülözhetetlen", "a", "független", "sajtó", "támogatása", "Magyarországon."], ["Végső", "soron", "nélkülözhetetlen", "a", "független", "sajtó", "támogatása", "Magyarországon."], "Ultimately supporting the independent press in Hungary is indispensable.", ["c1-adv-conclusive-free-press-defense"]),
                dc("dialogue", [
                    {"speaker": "Egyetemi hallgató", "text": "Van-e jövője a szabad újságírásnak ebben a médiakörnyezetben?"},
                    {"speaker": "Főszerkesztő", "text": "Konklúzióként leszögezhető: mindent egybevetve a szabad szó _____ nem a hatalom jóindulata, hanem a polgárok szabadságvágya."},
                    {"speaker": "Egyetemi hallgató", "text": "Ez ad reményt a jövőre nézve."}
                ], ["záloga", "ára", "féke"], 0, ["c1-adv-conclusive-free-press-defense"]),
                sw("production", [{"prompt": "Write a concluding manifesto on media freedom using 'Végső soron nélkülözhetetlen'.", "answer": "Végső soron nélkülözhetetlen a független szerkesztőségek bátor támogatása, hiszen a szabad és cenzúrázatlan sajtó mindent egybevetve a demokratikus társadalom egyetlen megmaradt záloga."}], ["c1-adv-conclusive-free-press-defense"]),
                mc("grammar", "check", "Melyik szintéziskifejezés összegzi a sajtószabadság melletti kiállást a legemelkedettebben?", [
                    "Végső soron nélkülözhetetlen / mindent egybevetve a demokratikus nyilvánosság záloga",
                    "Így esett a dolog és kész",
                    "Talán majd jobb lesz jövőre"
                ], 0, ["c1-adv-conclusive-free-press-defense"])
            ]
        }
    ]

    for l in disc_lessons:
        emit_instructional_lesson(26, "discourse", l, disc_title, disc_intro if l["num"] == 1 else None)

    # Combined World Story
    write_json(
        f"stories/world/c1/c1-{slug}-kesma-hegemonia.json",
        {
            "id": f"story.c1.{slug}.combined",
            "title": "Médiakoncentráció és a független nyilvánosság harca",
            "level": "C1",
            "lesson": 5,
            "order": 26,
            "type": "world",
            "estimatedMinutes": 8,
            "grammar": ["c1-adv-conclusive-free-press-defense"],
            "summary": "Átfogó tényfeltáró krónika a KESMA-monolit megalakulásáról, az MTVA pártpropagandává züllesztéséről, az állami hirdetések piactorzító hatásáról, valamint az Index felmondását követő telexes olvasói forradalomról.",
            "vocabularyTopics": [
                "Media Capture: The KESMA Empire, State Propaganda & Digital Resistance",
                "Independent Media Resilience & Conclusive Defense"
            ],
            "paragraphs": [
                {"type": "narration", "text": "A magyar médiarendszer 2010 utáni átalakulása a modern európai demokráciák legdrámaibb sajtópolitikai kísérlete volt. A nyilvánosság szisztematikus centralizálása a Közép-Európai Sajtó és Média Alapítvány (KESMA) égisze alatt csaknem ötszáz sajtóorgánumot rendelt egyetlen központi politikai akarat alá, kiiktatva a Gazdasági Versenyhivatal felügyeletét."},
                {"type": "narration", "text": "Ezzel párhuzamosan a több mint 140 milliárd adóforintból gazdálkodó közmédia (MTVA) feladta a közszolgálatiság minden alkotmányos követelményét. A belső feketelisták és a cenzurális utasítások nyomán az állami hírcsatornák kormányszócsővé silányultak, elzárva a vidéki választópolgárokat a valóságtól."},
                {"type": "narration", "text": "A hatalom leghatékonyabb fegyvere azonban a reklámpiac torzítása volt: minél több százmilliárdos állami hirdetést csatornáztak a lojális oligarchákhoz, annál nehezebb gazdasági helyzetbe kényszerültek a független szerkesztőségek. A magánhirdetők politikai megfélemlítése és a frekvenciák elvétele a független sajtó lassú kivéreztetését célozta."},
                {"type": "narration", "text": "A történet azonban mégsem a vereségről, hanem az ellenállóképességről szól. Az Index szerkesztőségének 2020-as hősies felállása és a Telex viharos olvasói sikere megmutatta: a magyar társadalomban él a szabadságvágy. Végső soron nélkülözhetetlen felismerni: mindent egybevetve a szabad, cenzúrázatlan sajtó az a kikezdhetetlen bástya, amely nélkül a magyar nemzet szellemi jövője és függetlensége elképzelhetetlen."}
            ]
        }
    )

    # Discourse Consolidation
    emit_consolidation_lesson(
        26,
        "discourse",
        f"c1-{slug}-consolidation",
        disc_title,
        [
            "I can analyze KESMA media conglomerate concentration, national strategic exemptions, and public broadcaster capture.",
            "I can critique state advertising market distortions, advertiser intimidation, and smear campaigns (Sovereignty Protection Office).",
            "I can formulate manifestos on independent digital newsroom resilience (Telex, 444) and European media freedom legislation."
        ],
        [
            mc("grammar", "recognize", "Milyen szerkezettel diagnosztizálhatjuk a médiarendszer központosítását emelkedett regiszterben?", [
                "a nyilvánosság szisztematikus centralizálása / a médiaegyensúly drasztikus felborulása",
                "amikor új nyomdagépeket szerelnek fel",
                "hogyha késik a reggeli újságkihordó"
            ], 0, ["c1-discourse-media-capture-framing"]),
            mc("grammar", "recognize", "Melyik modális kifejezés fogalmaz meg szigorú törvényi tilalmat a közmédiával szemben?", [
                "nem viselkedhet kormányszócsőként / nem alkalmazhat politikai feketelistákat",
                "bármikor lejátszhat egy kellemes dalt",
                "szabadon választhat a mikrofonok között"
            ], 0, ["c1-modal-deontic-public-broadcasting"]),
            match("vocabulary", "recognize", [["KESMA", "ötszáz médiumot tömörítő kormánypárti óriásalapítvány"], ["MTVA", "állami propagandává alakított közmédia"], ["hirdetői megfélemlítés", "magáncégek elriasztása a független felületektől"], ["Index-felmondás", "több mint nyolcvan újságíró elvi kiállása"], ["Szuverenitásvédelmi Hivatal", "kritikus sajtót megbélyegző állami szervezet"]], ["c1-mediaszabadsag-vocab"]),
            fb("vocabulary", "recall", "A kormánypárti médiabirodalmat egyesítő alapítvány a _____. (KESMA / KESMA)", "KESMA", "The foundation uniting the pro-government media empire is KESMA.", ["c1-mediaszabadsag-vocab"]),
            fb("vocabulary", "recall", "Az Index szerkesztőségének felállása után létrejött olvasói lap a _____. (Telex / Telex)", "Telex", "The reader-funded paper born after the Index resignation is Telex.", ["c1-mediaszabadsag-vocab"]),
            fb("grammar", "recall", "A közszolgálati adóknak nem _____ pártpolitikai szócsőként működniük. (should not / szabadna)", "szabadna", "Public service channels should not operate as party-political mouthpieces.", ["c1-modal-deontic-public-broadcasting"]),
            fb("grammar", "context", "Minél több közpénzt pumpálnak az állami propagandába, _____ inkább sérül a piaci verseny. (the more / annál)", "annál", "The more public money is pumped into state propaganda, the more market competition is damaged.", ["c1-adv-proportional-advertising-distortion"]),
            fb("grammar", "context", "Végső soron _____ a bátor és független szerkesztőségek kitartó támogatása. (indispensable / nélkülözhetetlen)", "nélkülözhetetlen", "Ultimately persevering support for courageous and independent newsrooms is indispensable.", ["c1-adv-conclusive-free-press-defense"]),
            mc("grammar", "context", "Mi a funkciója a 'Minél... annál...' arányossági szerkezetnek a médiapiaci elemzésekben?", [
                "Az állami források piactorzító beáramlása és a szabad sajtó anyagi kivéreztetése közötti egyenes arányosságot bizonyítja.",
                "Megmutatja, milyen drága egy televíziós kamera.",
                "Megmagyarázza a műsorvezetők öltözködési stílusát."
            ], 0, ["c1-adv-proportional-advertising-distortion"]),
            sb("grammar", "produce", ["A", "szabad", "sajtó", "nélkül", "nem", "létezik", "demokratikus", "nyilvánosság."], ["A", "szabad", "sajtó", "nélkül", "nem", "létezik", "demokratikus", "nyilvánosság."], "Without a free press no democratic public sphere exists.", ["c1-adv-conclusive-free-press-defense"]),
            sw("production", [{"prompt": "Write a critical diagnosis of media capture using a crisis framing marker.", "answer": "A KESMA alapítvány létrehozása és a versenyfelügyelet törvényi kiiktatása a nyilvánosság szisztematikus centralizálását és a médiaegyensúly drasztikus felborulását idézte elő."}], ["c1-discourse-media-capture-framing"]),
            sw("production", [{"prompt": "Formulate a concluding thought on media freedom and digital resilience in Hungary.", "answer": "Végső soron nélkülözhetetlen az olvasói közösség hősies szolidaritása, hiszen a független szerkesztőségek megléte mindent egybevetve a magyar polgári nyilvánosság egyetlen valódi záloga."}], ["c1-adv-conclusive-free-press-defense"])
        ]
    )

    print("=== Finished C1 Unit 26 ===")


if __name__ == "__main__":
    generate_unit_26()
