#!/usr/bin/env python3
"""
Hungarian C1 Block 6 - Unit 31 Generator:
  - Track 1 (Core): Unit 31 — "Philosophy of History, Historical Trauma & Post-Communist Memory" (c1-31)
  - Track 2 (Discourse): Unit 31 — "The House of Terror, 1956 Revisionism & Historical Revisionism" (c1-emlekezetpolitika)
"""

import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT))

from scripts.c1_block1.common import mc, match, fb, sb, dc, sw, write_json, emit_instructional_lesson, emit_consolidation_lesson
from scripts.c1_block6.registry_helper import register_unit


def generate_unit_31():
    print("=== Generating C1 Unit 31 ===")
    
    new_skills = {
        "c1-31-vocab": {"kind": "vocabulary"},
        "c1-emlekezetpolitika-vocab": {"kind": "vocabulary"},
        "c1-adv-metahistorical-trauma-analysis": {"kind": "grammar"},
        "c1-participle-collective-guilt-exculpation": {"kind": "grammar"},
        "c1-adv-counter-hysteria-adversatives": {"kind": "grammar"},
        "c1-modal-teleological-historical-catharsis": {"kind": "grammar"},
        "c1-adv-scalar-bibo-political-realism": {"kind": "grammar"},
        "c1-discourse-historical-revisionism-framing": {"kind": "grammar"},
        "c1-modal-deontic-intellectual-honesty": {"kind": "grammar"},
        "c1-adv-proportional-exculpatory-narratives": {"kind": "grammar"},
        "c1-epistemic-ideological-whitewashing": {"kind": "grammar"},
        "c1-adv-conclusive-historical-justice-synthesis": {"kind": "grammar"},
    }
    new_titles = {
        "c1-31-vocab": "reading",
        "c1-emlekezetpolitika-vocab": "reading",
        "c1-adv-metahistorical-trauma-analysis": "metahistorical evaluative adverbials analyzing collective trauma and historical hysteria",
        "c1-participle-collective-guilt-exculpation": "complex participial structures dissecting national victimhood and moral exculpation narratives",
        "c1-adv-counter-hysteria-adversatives": "adversative connectors contrasting democratic political realism with collective national hysteria",
        "c1-modal-teleological-historical-catharsis": "teleological modal structures framing historical truth-telling and collective catharsis",
        "c1-adv-scalar-bibo-political-realism": "scalar evaluative adverbials calibrating istván bibó's diagnostic political philosophy",
        "c1-discourse-historical-revisionism-framing": "discourse framing markers diagnosing state-directed historical revisionism and propaganda",
        "c1-modal-deontic-intellectual-honesty": "deontic modal structures asserting intellectual duty of objective historical reckoning",
        "c1-adv-proportional-exculpatory-narratives": "proportional correlative conjunctions mapping state victimhood propaganda against historical reality",
        "c1-epistemic-ideological-whitewashing": "epistemic stance markers assessing ideological whitewashing of totalitarian collaboration",
        "c1-adv-conclusive-historical-justice-synthesis": "evaluative synthesis particles formulating manifestos for authentic national historical reckoning",
    }
    
    core_title = "Philosophy of History, Historical Trauma & Post-Communist Memory"
    core_stems = [f"c1-31-0{i}" for i in range(1, 6)] + ["c1-31-consolidation"]
    disc_title = "The House of Terror, 1956 Revisionism & Historical Revisionism"
    slug = "emlekezetpolitika"
    disc_stems = [f"c1-{slug}-0{i}" for i in range(1, 6)] + [f"c1-{slug}-consolidation"]
    
    register_unit(31, core_title, core_stems, disc_title, disc_stems, new_skills, new_titles)

    # ----------------------------------------------------
    # TRACK 1: CORE (c1-31)
    # ----------------------------------------------------
    core_intro = [
        "The history of Central and Eastern Europe is scarred by deep collective traumas, existential anxieties, and the pathology of political hysteria. Confronting these historical wounds requires rigorous philosophical self-reflection and the dismantling of self-exculpatory national myths.",
        "In this unit, centered on István Bibó's monumental essay 'A kelet-európai kisállamok nyomorúsága' (The Misery of Small Eastern European States, 1946), you will master the elevated academic register of philosophy of history, trauma analysis, moral reckoning, political realism, and historical catharsis at the C1 level."
    ]

    core_lessons = [
        {
            "num": 1,
            "stem": "c1-31-01",
            "title": "Metahistorical Trauma Analysis & Collective Hysteria",
            "grammar_title": "Metahistorical Evaluative Adverbials Analyzing Collective Trauma and Historical Hysteria",
            "grammar_skill": "c1-adv-metahistorical-trauma-analysis",
            "goals": [
                "I can analyze collective historical trauma, existential fear of community annihilation, and political hysteria (*történelmi trauma, megsemmisülési félelem, politikai hisztéria, metatörténelem*).",
                "I can deploy elevated metahistorical adverbials evaluating national pathology (*metatörténetileg vizsgálva, pszichopolitikailag kódoltan, a kollektív félelmek talaján hisztérikusan reagálva*).",
                "I can critique historical determinism in political philosophy register."
            ],
            "vocab": [
                {"lemma": "történelmi trauma", "translation": "historical trauma", "pos": "expression"},
                {"lemma": "politikai hisztéria", "translation": "political hysteria (Bibó concept)", "pos": "expression"},
                {"lemma": "megsemmisülési félelem", "translation": "fear of national annihilation / extinction", "pos": "expression"},
                {"lemma": "metatörténelem", "translation": "metahistory / philosophy of history", "pos": "noun"},
                {"lemma": "tévút", "translation": "historical blind alley / false path", "pos": "noun"},
                {"lemma": "pszichopolitika", "translation": "psychopolitics", "pos": "noun"},
                {"lemma": "kollektív neurózis", "translation": "collective neurosis", "pos": "expression"},
                {"lemma": "történelmi sokk", "translation": "historical shock / rupture", "pos": "expression"}
            ],
            "gr_text1": "Metahistorical evaluative adverbials analyze the underlying psychological and structural mechanisms of national political behavior: `metatörténetileg vizsgálva` (examined metahistorically), `pszichopolitikailag kódoltan` (psychopolitically encoded), `a kollektív rettegés talaján hisztérikusan reagálva` (reacting hysterically on the ground of collective terror), `történetfilozófiailag megalapozott módon` (in an epistemologically well-founded manner in philosophy of history).",
            "gr_text2": "Example: `A közép-európai nemzetek metatörténetileg vizsgálva a nemzethalál állandó félelmében élve, pszichopolitikailag kódoltan hajlamosak a hisztérikus reakciókra`.",
            "gr_table": [
                ["A társadalom metatörténetileg vizsgálva traumatikus sokkok sorozatát élte át.", "Examined metahistorically society experienced a series of traumatic shocks."],
                ["A politikai elit pszichopolitikailag kódoltan táplálja a megsemmisülési félelmet.", "Psychopolitically encoded the political elite feeds the fear of annihilation."],
                ["A nemzet hisztérikusan reagálva keres bűnbakokat a vereségek után.", "Reacting hysterically the nation seeks scapegoats after defeats."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mit nevezett Bibó István 'politikai hisztériának' a közép-európai térségben?", [
                    "Azt a kóros lélektani állapotot, amikor egy nemzet valós vagy képzelt félelmei miatt elveszíti a realitásérzékét, és demokratikus reformok helyett tekintélyelvű illúziókba menekül.",
                    "A parlamentben történő hangoskodást a képviselők között.",
                    "A választások előtti plakátragasztási versenyt."
                ], 0, ["c1-31-vocab"]),
                fb("grammar", "controlled", "A térség tragédiáit metatörténetileg _____ a kollektív félelmek mechanizmusa tárul fel. (examining / vizsgálva)", "vizsgálva", "Examining metahistorically the tragedies of the region the mechanism of collective fears is revealed.", ["c1-adv-metahistorical-trauma-analysis"]),
                match("vocabulary", "controlled", [["politikai hisztéria", "a realitásérzék elvesztése kollektív félelmek hatására"], ["megsemmisülési félelem", "a nemzet eltűnésétől való egzisztenciális rettegés"], ["tévút", "téves történelmi irányválasztás"], ["metatörténelem", "a történelmi folyamatok mélyebb törvényszerűségeinek vizsgálata"]], ["c1-31-vocab"]),
                fb("grammar", "practice", "A hatalom pszichopolitikailag _____ módon használja fel a történelmi sérelmeket. (encoded / kódolt)", "kódolt", "Power utilizes historical grievances in a psychopolitically encoded manner.", ["c1-adv-metahistorical-trauma-analysis"]),
                sb("grammar", "practice", ["A", "nemzet", "metatörténetileg", "vizsgálva", "traumatikus", "tévutakra", "tévedt."], ["A", "nemzet", "metatörténetileg", "vizsgálva", "traumatikus", "tévutakra", "tévedt."], "Examined metahistorically the nation strayed onto traumatic false paths.", ["c1-adv-metahistorical-trauma-analysis"]),
                dc("dialogue", [
                    {"speaker": "Filozófus", "text": "Miért olyan nehéz a nemzeti traumák higgadt feldolgozása Közép-Európában?"},
                    {"speaker": "Történész", "text": "Mert metatörténetileg vizsgálva a politikai hisztéria _____ teszi az őszinte szembenézést."},
                    {"speaker": "Filozófus", "text": "A félelem eltorzítja a nemzet erkölcsi látását."}
                ], ["lehetetlenné", "könnyűvé", "széppé"], 0, ["c1-adv-metahistorical-trauma-analysis"]),
                sw("production", [{"prompt": "Write a sentence analyzing historical trauma using a metahistorical adverbial.", "answer": "A közép-európai államok fejlődését metatörténetileg vizsgálva nyilvánvalóvá válik, hogy a megsemmisülési félelem pszichopolitikailag kódolt hisztériához és autoriter kísértésekhez vezetett."}], ["c1-adv-metahistorical-trauma-analysis"]),
                mc("grammar", "check", "Melyik határozó fejezi ki a történelmi traumák lélektani hátterét a legszakszerűbben?", [
                    "metatörténetileg vizsgálva / pszichopolitikailag kódoltan",
                    "történelmet olvasgatva szomorúan",
                    "elég sok régi bajt emlegetve"
                ], 0, ["c1-adv-metahistorical-trauma-analysis"])
            ]
        },
        {
            "num": 2,
            "stem": "c1-31-02",
            "title": "Victimhood Narratives & Moral Exculpation",
            "grammar_title": "Complex Participial Structures Dissecting National Victimhood and Moral Exculpation Narratives",
            "grammar_skill": "c1-participle-collective-guilt-exculpation",
            "goals": [
                "I can analyze national victimhood narratives, moral self-exculpation, and the dialectic of perpetrator vs. victim (*áldozati narratíva, morális önfelmentés, bűnbakképzés, felelősséghárítás*).",
                "I can construct complex participial structures dissecting exculpatory myths (*a nemzetet kizárólag passzív áldozatként feltüntető, a belső cinkosságot elhallgató, a felelősséget külső hatalmakra hárító*).",
                "I can critique historical denialism in ethics of memory register."
            ],
            "vocab": [
                {"lemma": "áldozati narratíva", "translation": "victimhood narrative / cult of victimhood", "pos": "expression"},
                {"lemma": "morális önfelmentés", "translation": "moral self-exculpation", "pos": "expression"},
                {"lemma": "felelősséghárítás", "translation": "deflection / evasion of responsibility", "pos": "noun"},
                {"lemma": "bűnbakképzés", "translation": "scapegoating", "pos": "noun"},
                {"lemma": "belső cinkosság", "translation": "internal complicity / collaboration", "pos": "expression"},
                {"lemma": "történelmi felelősség", "translation": "historical responsibility", "pos": "expression"},
                {"lemma": "öncsalás", "translation": "self-delusion / collective bad faith", "pos": "noun"},
                {"lemma": "morális tisztánlátás", "translation": "moral lucidity", "pos": "expression"}
            ],
            "gr_text1": "Complex participial structures specify the deceptive discursive strategies of national self-exculpation: `a nemzetet kizárólag tehetetlen áldozatként láttató történelemszemlélet` (conception of history depicting the nation exclusively as a helpless victim), `a belső kollaborációt és cinkosságot szisztematikusan elhallgató mítoszok` (myths systematically concealing internal collaboration and complicity), `a bűnökért a felelősséget külső ellenségekre hárító politikai retorika` (political rhetoric deflecting responsibility for crimes onto external enemies).",
            "gr_text2": "Example: `A holokauszt hazai tragédiájában a magyar közigazgatás bűnrészességét elfedő és az országot passzív áldozatként beállító emlékezetpolitika mélységesen rombolja a nemzet erkölcsi tisztaságát`.",
            "gr_table": [
                ["A felelősséget kizárólag a német megszállásra hárító narratíva hamis.", "The narrative shifting responsibility exclusively onto German occupation is false."],
                ["A belső cinkosságot elhallgató mítoszok gátolják a katarzist.", "Myths concealing internal complicity obstruct catharsis."],
                ["A nemzetet kizárólag áldozatként láttató történelemkép megakadályozza a felnőtté válást.", "The image of history portraying the nation solely as a victim prevents coming of age."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mit értünk 'morális önfelmentés' alatt a modern történetírásban?", [
                    "Azon törekvést, amellyel egy társadalom eltagadja saját történelmi felelősségét és bűneit, és minden katasztrófáért kizárólag külső nagyhatalmakat vagy bűnbakokat tesz felelőssé.",
                    "Az adósságok elengedését a bankok által.",
                    "A sportversenyeken kapott büntetőpontok törlését."
                ], 0, ["c1-31-vocab"]),
                fb("grammar", "controlled", "A történelmi felelősséget külső hatalmakra _____ elméletek megakadályozzák a valódi megbékélést. (deflecting / hárító)", "hárító", "Theories deflecting historical responsibility onto external powers prevent genuine reconciliation.", ["c1-participle-collective-guilt-exculpation"]),
                match("vocabulary", "controlled", [["áldozati narratíva", "a nemzet tévedhetetlenségét és szenvedését hirdető dogma"], ["morális önfelmentés", "saját bűnök elfedése külső kényszerekre hivatkozva"], ["belső cinkosság", "együttműködés totalitárius hatalmakkal a lakosság részéről"], ["morális tisztánlátás", "a tények bátor, illúziómentes beismerése"]], ["c1-31-vocab"]),
                fb("grammar", "practice", "A belső kollaborációt szisztematikusan _____ mítoszok meghamisítják a múltat. (concealing / elhallgató)", "elhallgató", "Myths systematically concealing internal collaboration falsify the past.", ["c1-participle-collective-guilt-exculpation"]),
                sb("grammar", "practice", ["Az", "önfelmentő", "mítoszok", "gátolják", "a", "nemzeti", "katarzist."], ["Az", "önfelmentő", "mítoszok", "gátolják", "a", "nemzeti", "katarzist."], "Self-exculpating myths obstruct national catharsis.", ["c1-participle-collective-guilt-exculpation"]),
                dc("dialogue", [
                    {"speaker": "Kutató", "text": "Mi a legnagyobb veszélye a Szabadság téri német megszállási emlékmű szimbolikájának?"},
                    {"speaker": "Eszmetörténész", "text": "Az, hogy a magyar államgépezet aktív közreműködését _____ és Magyarországot ártatlan áldozatként jeleníti meg."},
                    {"speaker": "Kutató", "text": "Ez a felelősséghárítás iskolapéldája."}
                ], ["eltakarja", "feltárja", "megvallja"], 0, ["c1-participle-collective-guilt-exculpation"]),
                sw("production", [{"prompt": "Write a critique of victimhood narratives using a complex participial structure.", "answer": "A nemzetet kizárólag passzív áldozatként láttató és a belső cinkosságot elfedő emlékezetpolitikai narratívák megfosztják a társadalmat a történelmi felnőtté válás és a morális tisztánlátás esélyétől."}], ["c1-participle-collective-guilt-exculpation"]),
                mc("grammar", "check", "Melyik szerkezet leplezi le az önfelmentő történelemszemléletet a legpontosabban?", [
                    "a belső cinkosságot szisztematikusan elhallgató és a felelősséget külső erőkre hárító",
                    "a régi könyveket a könyvtárban olvasó",
                    "egy szép márványszobrot leleplező"
                ], 0, ["c1-participle-collective-guilt-exculpation"])
            ]
        },
        {
            "num": 3,
            "stem": "c1-31-03",
            "title": "Democratic Political Realism vs. National Hysteria",
            "grammar_title": "Adversative Connectors Contrasting Democratic Political Realism with Collective National Hysteria",
            "grammar_skill": "c1-adv-counter-hysteria-adversatives",
            "goals": [
                "I can analyze István Bibó's political realism, institutional sanity, and anti-fascist/anti-communist moral resistance (*politikai realizmus, intézményi józanság, hisztériamentes demokrácia, erkölcsi ellenállás*).",
                "I can deploy elevated adversative connectors contrasting realism with collective hysteria (*a hisztérikus félelmekkel és összeesküvés-elméletekkel szemben a valóságban a politikai realizmus, nemhogy nem gyengeség a tényekkel való szembenézés, hanem éppen az egyetlen gyógyír, mindazonáltal a józanság intézményi védelmet igényel*).",
                "I can argue against nationalist demagogy in constitutional political theory."
            ],
            "vocab": [
                {"lemma": "politikai realizmus", "translation": "political realism (Bibó ethos)", "pos": "expression"},
                {"lemma": "intézményi józanság", "translation": "institutional sobriety / sanity", "pos": "expression"},
                {"lemma": "összeesküvés-elmélet", "translation": "conspiracy theory", "pos": "noun"},
                {"lemma": "demagógia", "translation": "demagogy / populist manipulation", "pos": "noun"},
                {"lemma": "félelemmentesség", "translation": "freedom from fear", "pos": "noun"},
                {"lemma": "erkölcsi integritás", "translation": "moral integrity", "pos": "expression"},
                {"lemma": "társadalmi szerződés", "translation": "social contract", "pos": "expression"},
                {"lemma": "demokratikus konszenzus", "translation": "democratic consensus", "pos": "expression"}
            ],
            "gr_text1": "Adversative connectors establish critical demarcations between rational democratic politics and paranoid myth-making: `a nacionalista hisztériakeltéssel szemben a valóságban a józan politikai realizmus` (in contrast with nationalist hysteria-mongering in reality sober political realism), `nemhogy nem nemzetietlen a bűnök elismerése, hanem éppen az érett polgári önbecsülés feltétele` (far from acknowledging crimes being unpatriotic, but rather the condition of mature civic self-respect), `mindazonáltal az összeesküvés-elméletek mérgezik a közéletet` (nevertheless conspiracy theories poison public life).",
            "gr_text2": "Example: `A hisztérikus bűnbakképzéssel szemben a valóságban a bibói politikai realizmus nemhogy nem árulás, hanem a nemzet megmaradásának egyetlen józan útja`.",
            "gr_table": [
                ["A politikai hisztériával szemben a valóságban a józanság teremthet békét.", "In contrast with political hysteria in reality sobriety can create peace."],
                ["A szembenézés nemhogy nem gyengíti a nemzetet, hanem éppen megerősíti.", "Confronting the past is far from weakening the nation; on the contrary, it strengthens it."],
                ["A populista illúziók mindazonáltal elfedik a valós gazdasági problémákat.", "Populist illusions nevertheless conceal real economic problems."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Hogyan fogalmazza meg Bibó István a szabadság lényegét híres tételében?", [
                    "'A szabadság ott kezdődik, ahol megszűnik a félelem.'",
                    "'A szabadság a legerősebb hadsereg birtoklása.'",
                    "'A szabadság az országhatárok napi átrajzolása.'"
                ], 0, ["c1-31-vocab"]),
                fb("grammar", "controlled", "A hisztérikus félelmekkel szemben a valóságban a politikai _____ nyújt védelmet. (realism / realizmus)", "realizmus", "In contrast with hysterical fears in reality political realism provides protection.", ["c1-adv-counter-hysteria-adversatives"]),
                match("vocabulary", "controlled", [["politikai realizmus", "a tények és korlátok illúziómentes elfogadása"], ["intézményi józanság", "a fékek és ellensúlyok higgadt működtetése"], ["összeesküvés-elmélet", "komplex krízisek leegyszerűsítése gonosz háttérerőkre"], ["félelemmentesség", "a demokratikus szabadság alapfeltétele Bibó szerint"]], ["c1-31-vocab"]),
                fb("grammar", "practice", "A tényekkel való szembenézés nemhogy nem gyengeség, _____ éppen a nemzeti nagyság bizonyítéka. (rather / hanem)", "hanem", "Confronting facts is far from weakness; on the contrary, it is proof of national greatness.", ["c1-adv-counter-hysteria-adversatives"]),
                sb("grammar", "practice", ["A", "politikai", "realizmus", "legyőzi", "a", "kollektív", "hisztéria", "démonait."], ["A", "politikai", "realizmus", "legyőzi", "a", "kollektív", "hisztéria", "démonait."], "Political realism overcomes the demons of collective hysteria.", ["c1-adv-counter-hysteria-adversatives"]),
                dc("dialogue", [
                    {"speaker": "Szociológus", "text": "Hogyan fékezhető meg a politikai táborok hisztérikus radikalizálódása?"},
                    {"speaker": "Politológus", "text": "Csakis úgy, ha az összeesküvés-elméletekkel szemben a valóságban a demokratikus _____ teszünk hitet."},
                    {"speaker": "Szociológus", "text": "Ez az egyetlen gát a tekintélyelvű zülléssel szemben."}
                ], ["realizmus mellett", "hisztéria mellett", "félelem mellett"], 0, ["c1-adv-counter-hysteria-adversatives"]),
                sw("production", [{"prompt": "Write a defense of political realism using an adversative connector.", "answer": "A demagóg hisztériakeltéssel szemben a valóságban a bibói politikai realizmus nemhogy nem gyávaság, hanem a demokratikus intézmények és az emberi méltóság megőrzésének legfőbb fundamentuma."}], ["c1-adv-counter-hysteria-adversatives"]),
                mc("grammar", "check", "Melyik ellentétes szerkezet bizonyítja a bibói realizmus felsőbbrendűségét a leghatásosabban?", [
                    "a hisztérikus félelmekkel szemben a valóságban... nemhogy nem gyengeség, hanem a gyógyulás feltétele",
                    "amikor a politikusok kezet fognak a tévében",
                    "ha szép idő van, kimegyünk szavazni"
                ], 0, ["c1-adv-counter-hysteria-adversatives"])
            ]
        },
        {
            "num": 4,
            "stem": "c1-31-04",
            "title": "Truth-Telling & Collective Historical Catharsis",
            "grammar_title": "Teleological Modal Structures Framing Historical Truth-Telling and Collective Catharsis",
            "grammar_skill": "c1-modal-teleological-historical-catharsis",
            "goals": [
                "I can analyze truth commissions, historical catharsis, archival declassification, and lustration (*igazságtétel, történelmi katarzis, levéltári nyilvánosság, ügynökakták*).",
                "I can deploy teleological modal structures expressing historical truth-telling goals (*avégből kell feltárni a múlt bűneit, hogy a társadalom megszabaduljon a mérgező gyanakvástól, abból a célból hozzák nyilvánosságra a titkosszolgálati aktákat, hogy megteremtsék a valós megbékélést*).",
                "I can critique delayed transitional justice in post-communist societies."
            ],
            "vocab": [
                {"lemma": "igazságtétel", "translation": "historical reckoning / transitional justice", "pos": "noun"},
                {"lemma": "történelmi katarzis", "translation": "historical catharsis", "pos": "expression"},
                {"lemma": "levéltári nyilvánosság", "translation": "archival transparency / public access", "pos": "expression"},
                {"lemma": "ügynökakták", "translation": "secret police agent files (informer archives)", "pos": "noun"},
                {"lemma": "megbékélés", "translation": "national / historical reconciliation", "pos": "noun"},
                {"lemma": "morális megtisztulás", "translation": "moral purification / cleansing", "pos": "expression"},
                {"lemma": "kárpótlás", "translation": "restitution / moral compensation", "pos": "noun"},
                {"lemma": "múltfeldolgozás", "translation": "working through the past (Vergangenheitsbewältigung)", "pos": "noun"}
            ],
            "gr_text1": "Teleological modal structures formulate moral and institutional imperatives aimed at genuine historical healing: `avégből kell megnyitni a titkosszolgálati levéltárakat, hogy a nemzet megtisztuljon a diktatúra zsarolási hálóitól` (secret service archives must be opened to the end that the nation be cleansed from the dictatorship's blackmail networks), `abból a célból szükséges a szembenézés, hogy megakadályozzuk a totalitárius mechanizmusok visszatérését` (reckoning is necessary with the goal that we prevent the return of totalitarian mechanisms), `azért kell kimondani az igazságot, nehogy a hazugság váljon a jogrend alapjává` (truth must be spoken lest lies become the basis of the legal order).",
            "gr_text2": "Example: `A társadalomnak abból a célból kell végigvinnie a múltfeldolgozást, hogy a történelmi katarzis révén felszabaduljon a félelem és bűntudat bénultságából`.",
            "gr_table": [
                ["Avégből kell feltárni az ügynökaktákat, hogy véget vessünk a politikai zsarolhatóságnak.", "Informant files must be uncovered to the end that we end political blackmailability."],
                ["Abból a célból szükséges az igazságtétel, hogy helyreállítsuk a jogállam erkölcsi hitelét.", "Transitional justice is necessary with the goal of restoring the moral credit of rule of law."],
                ["Azért kell megismerni a múltat, hogy ne ismételjük meg annak legsötétebb bűneit.", "The past must be known so that we do not repeat its darkest crimes."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Miért tekintik a történészek a rendszerváltás legsúlyosabb mulasztásának az ügynökakták titkosítását?", [
                    "Mert a nyilvánosság elzárása megakadályozta a valódi erkölcsi katarzist, és évtizedekre kiszolgáltatta a politikai elitet a zsarolhatóságnak.",
                    "Mert a papírok eláztak a levéltár pincéjében.",
                    "Mert az ügynökök elfelejtették a fedőneveiket."
                ], 0, ["c1-31-vocab"]),
                fb("grammar", "controlled", "A levéltárakat abból a _____ kell megnyitni, hogy a társadalom megtisztuljon a múlt terheitől. (goal / célból)", "célból", "Archives must be opened with the goal that society be cleansed of the past's burdens.", ["c1-modal-teleological-historical-catharsis"]),
                match("vocabulary", "controlled", [["igazságtétel", "a diktatúra bűneinek és felelőseinek jogi és morális feltárása"], ["történelmi katarzis", "felszabadító lelki megkönnyebbülés az igazság kimondása révén"], ["ügynökakták", "a kommunista állambiztonság besúgói jelentései"], ["múltfeldolgozás", "a társadalmi traumák kibeszélése és beépítése a tudatba"]], ["c1-31-vocab"]),
                fb("grammar", "practice", "Avégből kell kimondani a tényeket, _____ a jövő nemzedékek ne éljenek mérgező hazugságban. (that / hogy)", "hogy", "Facts must be stated to the end that future generations not live in poisonous lies.", ["c1-modal-teleological-historical-catharsis"]),
                sb("grammar", "practice", ["A", "történelmi", "katarzis", "az", "erkölcsi", "megújulás", "nélkülözhetetlen", "feltétele."], ["A", "történelmi", "katarzis", "az", "erkölcsi", "megújulás", "nélkülözhetetlen", "feltétele."], "Historical catharsis is the indispensable condition of moral renewal.", ["c1-modal-teleological-historical-catharsis"]),
                dc("dialogue", [
                    {"speaker": "Történész", "text": "Miért halogatja a politika a kommunista állambiztonsági iratok teljes nyilvánosságát?"},
                    {"speaker": "Jogvédő", "text": "Mert avégből tartják zárolva a dokumentumokat, _____ megvédjék a múltbeli hálózatokat az elszámoltatástól."},
                    {"speaker": "Történész", "text": "De katarzis nélkül a társadalom sohasem gyógyul meg."}
                ], ["hogy", "mert", "ha"], 0, ["c1-modal-teleological-historical-catharsis"]),
                sw("production", [{"prompt": "Write a sentence formulating historical catharsis using a teleological modal structure.", "answer": "A nemzetnek abból a célból kell végrehajtania a teljes körű levéltári nyitást és az igazságtételt, hogy a történelmi katarzis révén megszabaduljon a zsarolhatóság és az elhallgatás évtizedes mételyétől."}], ["c1-modal-teleological-historical-catharsis"]),
                mc("grammar", "check", "Melyik modális célszerkezet fejezi ki a történelmi szembenézés kötelességét a legpontosabban?", [
                    "avégből kell feltárni az igazságot, hogy a nemzet eljusson a morális katarzishoz",
                    "jó lenne ha megkeresnék a régi papírokat a fiókban",
                    "néha illik megemlékezni a halottakról"
                ], 0, ["c1-modal-teleological-historical-catharsis"])
            ]
        },
        {
            "num": 5,
            "stem": "c1-31-05",
            "title": "István Bibó: The Misery of Small Eastern European States",
            "grammar_title": "Scalar Evaluative Adverbials Calibrating István Bibó's Diagnostic Political Philosophy",
            "grammar_skill": "c1-adv-scalar-bibo-political-realism",
            "goals": [
                "I can analyze István Bibó's diagnostic masterpiece, political morality, and democratic institution building (*kelet-európai nyomorúság, tévutak, félelem nélküli demokrácia, erkölcsi tanúságtétel*).",
                "I can deploy scalar evaluative adverbials calibrating diagnostic acuity (*eszmetörténetileg felbecsülhetetlen mértékben, a nemzeti patológiát alapjaiban leleplezve, diagnosztikai szempontból felülmúlhatatlan módon*).",
                "I can synthesize Bibó's moral philosophy for contemporary democratic statehood."
            ],
            "vocab": [
                {"lemma": "kisállami nyomorúság", "translation": "misery of small states (Bibó diagnostic concept)", "pos": "expression"},
                {"lemma": "erkölcsi tanúságtétel", "translation": "moral witness / testimony", "pos": "expression"},
                {"lemma": "demokratikus józanság", "translation": "democratic sobriety / composure", "pos": "expression"},
                {"lemma": "kórtünet", "translation": "symptom of pathology / clinical sign", "pos": "noun"},
                {"lemma": "nemzethalál-vízió", "translation": "vision of national extinction", "pos": "expression"},
                {"lemma": "polgári bátorság", "translation": "civic courage", "pos": "expression"},
                {"lemma": "történelmi tisztánlátás", "translation": "historical lucidity / clear-sightedness", "pos": "expression"},
                {"lemma": "államférfiúi bölcsesség", "translation": "statesmanlike wisdom", "pos": "expression"}
            ],
            "gr_text1": "Scalar evaluative adverbials calibrate the philosophical depth and analytical precision of Bibó's political diagnosis: `eszmetörténetileg felbecsülhetetlen mértékben` (to an inestimable degree in intellectual history), `a kelet-európai patológiákat alapjaiban leleplezve` (fundamentally unmasking Eastern European pathologies), `diagnosztikai szempontból felülmúlhatatlan éleslátással` (with unsurpassed lucidity from a diagnostic perspective), `a polgári demokrácia imperatívuszát megingathatatlanul képviselve` (unwaveringly representing the imperative of civic democracy).",
            "gr_text2": "Example: `Bibó István diagnosztikai szempontból felülmúlhatatlan éleslátással és eszmetörténetileg felbecsülhetetlen mértékben mutatta ki a félelemből fakadó hisztéria pusztító erejét`.",
            "gr_table": [
                ["Bibó eszmetörténetileg felbecsülhetetlen mértékben járult hozzá a politikai etikához.", "Bibó to an inestimable degree in intellectual history contributed to political ethics."],
                ["A nemzeti önáltatást alapjaiban leleplezve mutatott utat a demokrácia felé.", "Fundamentally unmasking national self-delusion he showed the way toward democracy."],
                ["Diagnosztikai szempontból felülmúlhatatlan módon elemezte a kisállami hisztériát.", "With unsurpassed lucidity from a diagnostic perspective he analyzed small-state hysteria."]
            ],
            "classic_story": {
                "slug": "bibo-kisallamok-nyomorusage",
                "title": "Bibó István: A kelet-európai kisállamok nyomorúsága",
                "author": "Bibó István",
                "work": "A kelet-európai kisállamok nyomorúsága (1946)",
                "summary": "Bibó István (1911–1979) jogtudós, politikai gondolkodó, az 1956-os forradalom államminisztere volt, a huszadik századi magyar szellemi élet legtisztább erkölcsi iránytűje. Remekművében a közép- és kelet-európai népek közös tragédiáját diagnosztizálja: a történelmi megrázkódtatások miatt e népek állandó megsemmisülési félelemben élnek, s e félelem a politikai hisztéria tévútjaira vezette őket. Hitvallása szerint a gyógyulás egyetlen útja a hazugságok felszámolása, a demokratikus intézmények tisztelete és a félelem nélküli szabad polgári élet megteremtése.",
                "characters": ["Bibó István, a gondolkodó és államférfi"],
                "paragraphs": [
                    {"type": "narration", "text": "A kelet-európai népek történetének alapvető tapasztalata a bizonytalanság és a fenyegetettség. Míg Nyugaton a nemzetek határai és állami keretei évszázadokon át szervesen alakultak, addig a mi régiónkban a határok folyamatosan változtak, birodalmak dőltek össze, s minden nemzedék átélte az állam pusztulását."},
                    {"type": "dialogue", "speaker": "Bibó István", "text": "A kelet-európai kisállamok nyomorúsága abból a végzetes félelemből fakad, hogy a nemzet létét bármely pillanatban megsemmisíthetik. Ebből a rettegésből születik a politikai hisztéria: az a meggyőződés, hogy a demokrácia luxus, a jogállam gyengeség, s a nemzet megmaradásához erőszakos, tekintélyelvű vezérre van szükség."},
                    {"type": "narration", "text": "A hisztérikus nemzet nem képes a belső problémák valós orvoslására: minden bírálatot hazaárulásnak tekint, s a felelősséget bűnbakokra és külső ellenségekre hárítja. E tévút szükségszerűen erkölcsi zülléshez és újabb nemzeti tragédiákhoz vezet."},
                    {"type": "narration", "text": "Bibó István eszmetörténetileg felbecsülhetetlen mértékben mutatta fel a kiutat: a demokrácia nem más, mint a politikai hisztéria intézményesített gyógymódja. A szabadság ott kezdődik, ahol megszűnik a félelem; s egy nemzet csak akkor válhat valóban naggyá, ha képes illúziók nélkül, a jog és az igazság szellemében kormányozni önmagát."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Hogyan fogalmazza meg Bibó István a kelet-európai kisállamok alapproblémáját?", [
                    "A megsemmisülési félelemből fakadó politikai hisztériaként, amely a demokratikus fejlődés helyett autoriter tévutakra kényszeríti a nemzeteket.",
                    "A hegyek hiányából fakadó rossz időjárásként.",
                    "A nemzetközi vasúti menetrendek pontatlanságaként."
                ], 0, ["c1-31-vocab"]),
                fb("grammar", "controlled", "Bibó esszéi eszmetörténetileg _____ mértékben járultak hozzá a magyar demokrácia elméletéhez. (inestimable / felbecsülhetetlen)", "felbecsülhetetlen", "Bibó's essays to an inestimable degree in intellectual history contributed to Hungarian democratic theory.", ["c1-adv-scalar-bibo-political-realism"]),
                match("vocabulary", "controlled", [["kisállami nyomorúság", "a fenyegetettségből fakadó patologikus politikai működés"], ["erkölcsi tanúságtétel", "hűség az igazsághoz a diktatúra idején is"], ["nemzethalál-vízió", "a magyarság eltűnésétől rettegő romantikus toposz"], ["demokratikus józanság", "a jogállami normák megalkuvás nélküli védelme"]], ["c1-31-vocab"]),
                fb("grammar", "practice", "Bibó a nemzeti hisztériát alapjaiban _____ bizonyította be a szabadság fontosságát. (unmasking / leleplezve)", "leleplezve", "Fundamentally unmasking national hysteria Bibó proved the importance of freedom.", ["c1-adv-scalar-bibo-political-realism"]),
                sb("grammar", "practice", ["A", "szabadság", "ott", "kezdődik", "ahol", "megszűnik", "a", "félelem."], ["A", "szabadság", "ott", "kezdődik", "ahol", "megszűnik", "a", "félelem."], "Freedom begins where fear ends.", ["c1-adv-scalar-bibo-political-realism"]),
                mc("reading", "context", "Milyen orvosságot ajánl Bibó a politikai hisztéria leküzdésére?", [
                    "A tényekkel való bátor szembenézést, a jogállami intézmények tiszteletét és a polgári szabadságjogok félelemmentes gyakorlását.",
                    "Egy újabb diktátor kinevezését a rend fenntartására.",
                    "A határok azonnali katonai lezárását minden irányban."
                ], 0, ["c1-31-vocab"]),
                sw("production", [{"prompt": "Write a reflection on István Bibó's political philosophy using a scalar evaluative adverbial.", "answer": "Bibó István eszmetörténetileg felbecsülhetetlen mértékben, a kisállami hisztériát alapjaiban leleplezve mutatta meg, hogy a nemzeti megmaradás egyetlen garanciája a joguralom és a félelemmentes szabadság."}], ["c1-adv-scalar-bibo-political-realism"]),
                mc("grammar", "check", "Melyik határozói kifejezés méltatja Bibó munkásságát a legméltóbb elméleti regiszterben?", [
                    "eszmetörténetileg felbecsülhetetlen mértékben / diagnosztikai szempontból felülmúlhatatlan éleslátással",
                    "nagyon okos könyveket írva a szobájában",
                    "meglehetősen hosszan fogalmazva a papíron"
                ], 0, ["c1-adv-scalar-bibo-political-realism"])
            ]
        }
    ]

    for l in core_lessons:
        emit_instructional_lesson(31, "core", l, core_title, core_intro if l["num"] == 1 else None)

    # Core Consolidation Lesson
    emit_consolidation_lesson(
        31,
        "core",
        "c1-31-consolidation",
        core_title,
        [
            "I can master the academic vocabulary of philosophy of history, trauma analysis, and transitional justice.",
            "I can employ metahistorical evaluative adverbials, participial exculpation structures, and counter-hysteria adversatives.",
            "I can analyze teleological historical catharsis and synthesize István Bibó's diagnostic political realism."
        ],
        [
            mc("grammar", "recognize", "Melyik kifejezés elemzi szakszerűen a kollektív félelmek hatását a társadalomra?", [
                "metatörténetileg vizsgálva / pszichopolitikailag kódolt hisztérikus reakciókkal",
                "hogyha megijednek a polgárok az utcán",
                "amikor rossz híreket mondanak a rádióban"
            ], 0, ["c1-adv-metahistorical-trauma-analysis"]),
            mc("grammar", "recognize", "Milyen szerkezettel leplezhetjük le az önfelmentő nemzeti narratívákat a legpontosabban?", [
                "a belső cinkosságot elhallgató és a felelősséget kizárólag külső erőkre hárító mítoszok",
                "amikor leporolják a régi zászlókat a múzeumban",
                "hogyha valaki nem emlékszik a dátumokra"
            ], 0, ["c1-participle-collective-guilt-exculpation"]),
            match("vocabulary", "recognize", [["politikai hisztéria", "a realitásérzék elvesztése fenyegetettség hatására"], ["morális önfelmentés", "saját történelmi bűneink eltagadása"], ["igazságtétel", "a diktatúrák bűneinek nyilvános feltárása"], ["katarzis", "felszabadító erkölcsi megtisztulás az igazság által"], ["kisállami nyomorúság", "Bibó diagnózisa a régió kóros beidegződéseiről"]], ["c1-31-vocab"]),
            fb("vocabulary", "recall", "A bűnök elismerése révén bekövetkező erkölcsi megtisztulás a történelmi _____ . (catharsis / katarzis)", "katarzis", "Moral purification occurring through acknowledging sins is historical catharsis.", ["c1-31-vocab"]),
            fb("vocabulary", "recall", "A tényekkel való illúziómentes szembenézés a politikai _____ . (realism / realizmus)", "realizmus", "Illusion-free confrontation with facts is political realism.", ["c1-31-vocab"]),
            fb("grammar", "recall", "A múltat metatörténetileg _____ nyilvánvalóvá válik a félelmek romboló ereje. (examining / vizsgálva)", "vizsgálva", "Examining the past metahistorically the destructive power of fears becomes evident.", ["c1-adv-metahistorical-trauma-analysis"]),
            fb("grammar", "context", "A hisztériával szemben a valóságban a józanság a túlélés valódi _____ . (guarantee / záloga)", "záloga", "In contrast with hysteria in reality sobriety is the true guarantee of survival.", ["c1-adv-counter-hysteria-adversatives"]),
            fb("grammar", "context", "Az aktákat abból a célból kell megnyitni, _____ felszámoljuk a zsarolhatóságot. (that / hogy)", "hogy", "Files must be opened with the goal that we liquidate blackmailability.", ["c1-modal-teleological-historical-catharsis"]),
            mc("grammar", "context", "Mi a funkciója a counter-hysteria ellentétes szerkezeteknek Bibó gondolatrendszerében?", [
                "Annak igazolása, hogy a múlttal való őszinte szembenézés nem a nemzet gyengítése, hanem az erkölcsi gyógyulás záloga.",
                "A politikai vitákban való hangos kiabálás szabályozása.",
                "Az újságcikkek hosszának csökkentése."
            ], 0, ["c1-adv-counter-hysteria-adversatives"]),
            sb("grammar", "produce", ["A", "szabadság", "ott", "kezdődik", "ahol", "megszűnik", "a", "félelem."], ["A", "szabadság", "ott", "kezdődik", "ahol", "megszűnik", "a", "félelem."], "Freedom begins where fear ends.", ["c1-adv-scalar-bibo-political-realism"]),
            sw("production", [{"prompt": "Write a critical evaluation of national victimhood narratives using a participial construction.", "answer": "A nemzetet kizárólag ártatlan áldozatként feltüntető és a totalitárius rezsimekkel való belső cinkosságot elhallgató történelemszemlélet megbénítja a társadalom erkölcsi fejlődését."}], ["c1-participle-collective-guilt-exculpation"]),
            sw("production", [{"prompt": "Synthesize István Bibó's diagnostic political realism using a scalar evaluative adverbial.", "answer": "Bibó István eszmetörténetileg felbecsülhetetlen mértékben, a nemzeti patológiákat alapjaiban leleplezve bizonyította be, hogy a félelem nélküli jogállami demokrácia a nemzeti felemelkedés egyetlen szilárd fundamentuma."}], ["c1-adv-scalar-bibo-political-realism"])
        ]
    )

    # ----------------------------------------------------
    # TRACK 2: DISCOURSE (c1-emlekezetpolitika)
    # ----------------------------------------------------
    disc_intro = [
        "In post-2010 Hungary, history became a primary battleground of state power. The government systematically deployed state resources, museum institutions, and public monuments to construct a revisionist memory politics centered on unilateral victimhood and moral exculpation.",
        "From the House of Terror Museum (Terror Háza) under Schmidt Mária and the controversial German Occupation Monument on Szabadság Square to the ideological reinterpretation of the 1956 Revolution and the whitewashing of the Horthy era, memory politics became an instrument of regime legitimization. In this unit, you will master the analytical discourse of historical revisionism, totalitarian equivalence, and archival transparency at the C1 level."
    ]

    disc_lessons = [
        {
            "num": 1,
            "stem": f"c1-{slug}-01",
            "title": "State-Directed Revisionism & The Politics of Memory",
            "grammar_title": "Discourse Framing Markers Diagnosing State-Directed Historical Revisionism and Propaganda",
            "grammar_skill": "c1-discourse-historical-revisionism-framing",
            "goals": [
                "I can analyze state-directed memory politics, historical revisionism, and propaganda museums (*emlékezetpolitika, történelmi revizionizmus, propaganda-múzeum, ideológiai átírás*).",
                "I can deploy discourse framing markers diagnosing historical distortion (*az államilag vezérelt revizionizmus szisztematikus stratégiája nyomán, az emlékezetpolitikai narratívák átírása következtében, a hatalmi legitimáció igényéből fakadóan*).",
                "I can critique institutionalized historical propaganda in public history register."
            ],
            "vocab": [
                {"lemma": "emlékezetpolitika", "translation": "politics of memory", "pos": "noun"},
                {"lemma": "történelmi revizionizmus", "translation": "historical revisionism", "pos": "expression"},
                {"lemma": "Szabadság téri emlékmű", "translation": "German Occupation Monument on Szabadság Square", "pos": "expression"},
                {"lemma": "relativizálás", "translation": "relativization of historical crimes", "pos": "noun"},
                {"lemma": "propaganda-narratíva", "translation": "propaganda narrative", "pos": "expression"},
                {"lemma": "kánonpolitika", "translation": "canon politics", "pos": "noun"},
                {"lemma": "történelemhamisítás", "translation": "falsification of history", "pos": "noun"},
                {"lemma": "szimbolikus politizálás", "translation": "symbolic politics", "pos": "expression"}
            ],
            "gr_text1": "Discourse framing markers diagnose structural shifts in state-controlled memory policies: `az államilag vezérelt revizionizmus szisztematikus stratégiája nyomán` (in the wake of the systematic strategy of state-directed revisionism), `az emlékezetpolitikai narratívák agresszív átírása következtében` (as a consequence of aggressive rewriting of memory narratives), `a hatalmi mítoszteremtés politikai igényéből fakadóan` (stemming from the political demand of regime myth-making).",
            "gr_text2": "Example: `Az emlékezetpolitikai narratívák átírása következtében a kormányzat a Szabadság téri emlékművel az egész nemzetet ártatlan áldozatként tüntette fel`.",
            "gr_table": [
                ["Az állami revizionizmus nyomán a tankönyvekben elmosták a belső felelősség határait.", "In the wake of state revisionism the boundaries of internal responsibility were blurred in textbooks."],
                ["Az emlékezetpolitika átírása következtében a Horthy-korszak tekintélyuralmi vonásait relativizálták.", "As a consequence of rewriting memory politics authoritarian features of the Horthy era were relativized."],
                ["A szimbolikus politizálás igényéből fakadóan a köztéri emlékművek a megosztás eszközeivé váltak.", "Stemming from the demand of symbolic politics public monuments became instruments of division."]
            ],
            "world_story_seg": {
                "seg_slug": "c1-emlekezetpolitika-01-allami-revizionizmus",
                "title": "A múlt átszabása: Állami revizionizmus a Szabadság téren",
                "summary": "A 2014-ben éjjel felállított német megszállási emlékmű a magyar államgépezet felelősségének elfedését és a kizárólagos áldozati mítosz megteremtését szolgálta.",
                "paragraphs": [
                    {"type": "narration", "text": "2014 tavaszán a kormányzat rendőri kordonok mögött, az éj leple alatt állította fel a német megszállás áldozatainak emlékművét a budapesti Szabadság téren. A kompozíció a náci birodalmi sast a Gábriel arkangyallal szimbolizált ártatlan Magyarországra lecsapó ragadozóként ábrázolta."},
                    {"type": "dialogue", "speaker": "Heller Ágnes", "text": "Az államilag vezérelt revizionizmus szisztematikus stratégiája nyomán ez az emlékmű a huszadik század legszégyenletesebb történelemhamisítása. Azt hazudja, hogy a magyar közigazgatás, a csendőrség és a politikai elit ártatlan volt a félmillió magyar zsidó deportálásában, s minden bűnért kizárólag a német megszállók feleltek."},
                    {"type": "narration", "text": "A társadalom erkölcsi válasza az 'Eleven Emlékmű' lett: polgárok százai vittek köveket, személyes fényképeket és családi dokumentumokat a szobor elé, élő vitafórumot teremtve a hatalmi hazugsággal szemben."},
                    {"type": "narration", "text": "A köztér a nemzeti emlékezet nyílt sebévé vált, megmutatva, hogy a felülről kényszerített revizionista mítoszok nem megbékélést, hanem mély társadalmi törésvonalakat hoznak létre."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Miért váltott ki heves tiltakozást a 2014-es Szabadság téri német megszállási emlékmű?", [
                    "Mert Magyarországot ártatlan arkangyalként ábrázolva elfedte a magyar hatóságok és csendőrség aktív bűnrészességét a holokausztban, kizárólagos áldozatként tüntetve fel az államot.",
                    "Mert az emlékmű túl alacsony volt és nem látszott a fáktól.",
                    "Mert nem szereltek rá megfelelő éjszakai világítást."
                ], 0, ["c1-emlekezetpolitika-vocab"]),
                fb("grammar", "controlled", "Az államilag vezérelt revizionizmus szisztematikus stratégiája _____ elfedték a történelmi bűnöket. (in the wake of / nyomán)", "nyomán", "In the wake of the systematic strategy of state-directed revisionism historical crimes were concealed.", ["c1-discourse-historical-revisionism-framing"]),
                match("vocabulary", "controlled", [["emlékezetpolitika", "a történelmi múlt állami szintű tudatos formálása"], ["történelmi revizionizmus", "a konszenzusos történelmi tények ideológiai átírása"], ["relativizálás", "súlyos bűnök bagatellizálása más eseményekkel való összemosással"], ["Szabadság téri emlékmű", "az állami felelősséget elhárító vitatott szoborcsoport"]], ["c1-emlekezetpolitika-vocab"]),
                fb("grammar", "practice", "Az emlékezetpolitikai narratívák átírása _____ a köztéri szobrok a politikai polarizáció eszközévé váltak. (consequence / következtében)", "következtében", "As a consequence of rewriting memory narratives public statues became tools of polarization.", ["c1-discourse-historical-revisionism-framing"]),
                sb("grammar", "practice", ["Az", "állami", "revizionizmus", "meghamisítja", "a", "holokauszt", "történeti", "valóságát."], ["Az", "állami", "revizionizmus", "meghamisítja", "a", "holokauszt", "történeti", "valóságát."], "State revisionism falsifies the historical reality of the Holocaust.", ["c1-discourse-historical-revisionism-framing"]),
                dc("dialogue", [
                    {"speaker": "Történész", "text": "Hogyan értékelhető az állami történetírás elmúlt évtizedes iránya?"},
                    {"speaker": "Kutató", "text": "Úgy, hogy a hatalmi mítoszteremtés politikai igényéből _____ a Horthy-korszak felelősségét folyamatosan tisztára mossák."},
                    {"speaker": "Történész", "text": "Ez megakadályozza a valós történelmi megbékélést."}
                ], ["fakadóan", "ellenére", "helyett"], 0, ["c1-discourse-historical-revisionism-framing"]),
                sw("production", [{"prompt": "Write a critical diagnosis of state historical revisionism using a discourse framing marker.", "answer": "Az államilag vezérelt revizionizmus szisztematikus stratégiája nyomán és az emlékezetpolitikai narratívák átírása következtében a hatalom a felelősségvállalás helyébe a hamis áldozati mítoszokat állította."}], ["c1-discourse-historical-revisionism-framing"]),
                mc("grammar", "check", "Melyik kifejezés diagnosztizálja a revizionista emlékezetpolitikát a legpontosabban?", [
                    "az államilag vezérelt revizionizmus szisztematikus stratégiája nyomán / az emlékezetpolitika átírása következtében",
                    "amikor új szobrot avatnak a téren délután",
                    "egy szép napon a múzeumba látogatva"
                ], 0, ["c1-discourse-historical-revisionism-framing"])
            ]
        },
        {
            "num": 2,
            "stem": f"c1-{slug}-02",
            "title": "The House of Terror & Totalitarian Equivalence",
            "grammar_title": "Deontic Modal Structures Asserting Intellectual Duty of Objective Historical Reckoning",
            "grammar_skill": "c1-modal-deontic-intellectual-honesty",
            "goals": [
                "I can analyze the House of Terror Museum (Terror Háza), Schmidt Mária's narrative, and the false equivalence of Nazi and Soviet terror (*Terror Háza, totalitárius rezsimek összemosása, belső felelősség eltagadása, muzeológiai manipuláció*).",
                "I can deploy deontic modal structures asserting intellectual duties of historical honesty (*a történettudománynak kötelessége ragaszkodni a források hitelességéhez, nem engedhető meg a diktatúrák bűneinek politikai relativizálása, a kutatóknak kötelező megőrizniük autonómiájukat*).",
                "I can critique narrative bias in museum pedagogy."
            ],
            "vocab": [
                {"lemma": "Terror Háza Múzeum", "translation": "House of Terror Museum (Andrássy út 60)", "pos": "expression"},
                {"lemma": "totalitárius rezsim", "translation": "totalitarian regime", "pos": "expression"},
                {"lemma": "összemosás", "translation": "false equivalence / conflation of regimes", "pos": "noun"},
                {"lemma": "muzeológiai manipuláció", "translation": "museological manipulation / staging", "pos": "expression"},
                {"lemma": "intellektuális tisztesség", "translation": "intellectual honesty / scholarly integrity", "pos": "expression"},
                {"lemma": "forráskritika", "translation": "source criticism", "pos": "noun"},
                {"lemma": "áldozati rangsorolás", "translation": "hierarchy / ranking of victims", "pos": "expression"},
                {"lemma": "deszakralizálás", "translation": "desacralization of historical memory", "pos": "noun"}
            ],
            "gr_text1": "Deontic modal structures articulate uncompromising intellectual and ethical duties of historical scholarship against ideological propaganda: `a történésznek kötelező ellenállnia a politikai megrendeléseknek` (the historian has a mandatory duty to resist political commissions), `nem engedhető meg a nyilas és a kommunista bűnök felületes összemosása a belső felelősség elfedésére` (superficial conflation of Arrow Cross and communist crimes must not be permitted to conceal internal responsibility), `a közgyűjteményeknek kötelességük a tények sokoldalú és hiteles bemutatása` (public collections have a duty to present facts multifaceted and authentic).",
            "gr_text2": "Example: `A szakmának kötelessége megőrizni az intellektuális tisztességet, s a múzeumok nem válhatnak politikai indoktrinációs intézményekké`.",
            "gr_table": [
                ["A történettudománynak kötelessége ragaszkodni a források szigorú kritikájához.", "Historical science has a duty to adhere to strict criticism of sources."],
                ["Nem engedhető meg a totalitárius diktatúrák bűneinek ideológiai relativizálása.", "Ideological relativization of totalitarian dictatorships' crimes cannot be permitted."],
                ["A kutatóknak szavatolniuk kell a tények elfogulatlan bemutatását.", "Researchers must guarantee the unbiased presentation of facts."]
            ],
            "world_story_seg": {
                "seg_slug": "c1-emlekezetpolitika-02-terror-haza-manipulacio",
                "title": "A díszletbe zárt emlékezet: A Terror Háza narratívája",
                "summary": "Az Andrássy út 60. alatti Terror Háza a szovjet és náci rémtettek összemosásával az állami felelősség elfedését és a politikai mítoszépítést szolgálja.",
                "paragraphs": [
                    {"type": "narration", "text": "Az Andrássy út 60. szám alatt 2002-ben megnyílt Terror Háza Múzeum a posztkommunista Magyarország leglátogatottabb és legvitatottabb emlékhelye. Az épület egykor a nyilas Hűség Háza, majd az ÁVH központja volt, pincéiben százakat kínoztak meg."},
                    {"type": "dialogue", "speaker": "Ungváry Krisztián", "text": "A történettudománynak kötelessége az intellektuális tisztesség védelme. Nem engedhető meg, hogy a múzeum a nyilas terrort csupán néhány szobára korlátozza, miközben az egész narratívát a kommunista elnyomásra hegyezi ki, azt sugallva, hogy a nácizmus csak külső epizód volt, a magyar társadalom pedig mindvégig ártatlan maradt."},
                    {"type": "narration", "text": "A múzeum látványos, színházi hatáselemekkel operáló terei a látogatók érzelmi manipulálását célozzák a tárgyilagos forráskritika és a valódi történelmi szembenézés helyett."},
                    {"type": "narration", "text": "A szakmai autonómia feladása oda vezetett, hogy az intézmény az állami ideológia és a politikai revizionizmus legfőbb szimbolikus bástyájává merevedett."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Milyen szakmai bírálat érte a Terror Háza Múzeum kiállítási koncepcióját a történészek részéről?", [
                    "Hogy a nyilas uralom és a holokauszt magyar felelősségét aránytalanul lekicsinyli, s a két diktatúra összemosásával felmenti a társadalmat a belső bűnrészesség alól.",
                    "Hogy az épület homlokzata nem illeszkedik az Andrássy út stílusához.",
                    "Hogy túl olcsók voltak a belépőjegyek a diákok számára."
                ], 0, ["c1-emlekezetpolitika-vocab"]),
                fb("grammar", "controlled", "A kutatóknak kötelességük _____ a szigorú forráskritikához a politikai nyomással szemben. (adhere / ragaszkodniuk)", "ragaszkodniuk", "Researchers have a duty to adhere to strict source criticism against political pressure.", ["c1-modal-deontic-intellectual-honesty"]),
                match("vocabulary", "controlled", [["Terror Háza", "az Andrássy út 60. alatti állami emlékhely"], ["összemosás", "különböző történelmi bűnök téves egyenlőségjele"], ["muzeológiai manipuláció", "érzelmi díszletek alkalmazása a tények tárgyilagos elemzése helyett"], ["intellektuális tisztesség", "az igazság megalkuvás nélküli képviselete"]], ["c1-emlekezetpolitika-vocab"]),
                fb("grammar", "practice", "Nem _____ meg a történelmi tények politikai célú elhallgatása és eltorzítása. (cannot be permitted / engedhető)", "engedhető", "Concealment and distortion of historical facts for political goals cannot be permitted.", ["c1-modal-deontic-intellectual-honesty"]),
                sb("grammar", "practice", ["A", "történészeknek", "kötelességük", "megvédeni", "a", "tudományos", "autonómiát."], ["A", "történészeknek", "kötelességük", "megvédeni", "a", "tudományos", "autonómiát."], "Historians have a duty to defend scientific autonomy.", ["c1-modal-deontic-intellectual-honesty"]),
                dc("dialogue", [
                    {"speaker": "Egyetemi hallgató", "text": "Hogyan kell bemutatni a huszadik századi diktatúrák történetét a múzeumokban?"},
                    {"speaker": "Professzor", "text": "Kizárólag úgy, hogy a szakembereknek kötelező _____ a propaganda hatásvadászatát és a tényekre építeni."},
                    {"speaker": "Egyetemi hallgató", "text": "Ez a tudományos etika elemi parancsa."}
                ], ["elutasítaniuk", "támogatniuk", "másolniuk"], 0, ["c1-modal-deontic-intellectual-honesty"]),
                sw("production", [{"prompt": "Write a sentence formulating the historian's duty using a deontic modal structure.", "answer": "A történészeknek kötelességük megőrizni az intellektuális tisztességet, és nem engedhető meg, hogy a múzeumok a diktatúrák összemosásával az állami önfelmentés eszközeivé váljanak."}], ["c1-modal-deontic-intellectual-honesty"]),
                mc("grammar", "check", "Melyik modális kifejezés írja elő a történész felelősségét a legkategorikusabban?", [
                    "a történettudománynak kötelessége ragaszkodni az igazsághoz / nem engedhető meg a manipuláció",
                    "jó lenne ha mindenki sokat olvasna a könyvtárban",
                    "talán nem ártana beszélgetni a múzeumigazgatóval"
                ], 0, ["c1-modal-deontic-intellectual-honesty"])
            ]
        },
        {
            "num": 3,
            "stem": f"c1-{slug}-03",
            "title": "Rewriting 1956 & The Dózsa László Scandal",
            "grammar_title": "Proportional Correlative Conjunctions Mapping State Victimhood Propaganda Against Historical Reality",
            "grammar_skill": "c1-adv-proportional-exculpatory-narratives",
            "goals": [
                "I can analyze the revision of the 1956 Revolution, the marginalization of Imre Nagy, and the Dózsa László photo scandal (*1956 átértelmezése, Nagy Imre perifériára szorítása, Dózsa László-botrány, szabadságharcos mítosz*).",
                "I can deploy proportional correlative conjunctions mapping propaganda against historical truth (*minél agresszívabban próbálja a hatalom kisajátítani 1956 emlékét, annál nyilvánvalóbbá válik a történelemhamisítás groteszk jellege, amilyen mértékben kitörlik a baloldali és reformkommunista hősöket, olyan arányban csonkítják meg a forradalom valóságát*).",
                "I can critique politically motivated memory distortion in contemporary historiography."
            ],
            "vocab": [
                {"lemma": "1956-os forradalom", "translation": "1956 Hungarian Revolution", "pos": "expression"},
                {"lemma": "Dózsa László-botrány", "translation": "Dózsa László billboard scandal (Pruck Pál)", "pos": "expression"},
                {"lemma": "Nagy Imre", "translation": "Imre Nagy (martyred 1956 Prime Minister)", "pos": "noun"},
                {"lemma": "szoboráthelyezés", "translation": "relocation of statues (e.g. Nagy Imre monument)", "pos": "noun"},
                {"lemma": "történelemhamisítás", "translation": "falsification of history", "pos": "noun"},
                {"lemma": "forradalmi konszenzus", "translation": "revolutionary consensus", "pos": "expression"},
                {"lemma": "óriásplakát-kampány", "translation": "billboard propaganda campaign", "pos": "expression"},
                {"lemma": "hitelességvesztés", "translation": "loss of credibility / authenticity", "pos": "noun"}
            ],
            "gr_text1": "Proportional correlative structures map the inverse relationship between state propaganda expenditure and genuine historical credibility: `minél több százmillióból finanszíroz a kormányzat revizionista óriásplakátokat, annál komikusabb hitelességvesztést szenved el a hivatalos emlékezetpolitika` (the more hundreds of millions the government finances revisionist billboards from, the more comical loss of credibility official memory politics suffers), `amilyen mértékben igyekeznek kitörölni Nagy Imre emlékét a nemzeti panteonból, olyan arányban mélyül a társadalmi felháborodás` (in proportion as they endeavor to erase Imre Nagy's memory from the national pantheon, to that extent public outrage deepens).",
            "gr_text2": "Example: `Minél inkább a jelenkori politikai üzenetekhez próbálják igazítani 1956-ot, annál inkább megfosztják a forradalmat valódi, sokszínű történelmi valóságától`.",
            "gr_table": [
                ["Minél agresszívabb a történelmi átírás, annál hevesebb a szakmai ellenállás.", "The more aggressive the historical rewriting, the fiercer the professional resistance."],
                ["Amilyen mértékben torzítják a tényeket, olyan arányban veszti el a hitelét az állam.", "To the extent they distort facts, to that extent the state loses its credibility."],
                ["Minél inkább kitörlik a mártírokat, annál nyilvánvalóbb a politikai szándék.", "The more they erase martyrs, the more obvious the political intent becomes."]
            ],
            "world_story_seg": {
                "seg_slug": "c1-emlekezetpolitika-03-dozsa-laszlo-es-1956",
                "title": "A kisajátított forradalom: 1956 és a Dózsa László-botrány",
                "summary": "Az 1956-os forradalom 60. évfordulóján a kormányzat átírta a forradalom történetét, plakátokon hamisítva meg Pruck Pál emlékét Dózsa László javára.",
                "paragraphs": [
                    {"type": "narration", "text": "2016-ban, az 1956-os forradalom 60. évfordulóján az állami emlékbizottság milliárdos plakátkampányt indított. Az egyik legismertebb pesti srác, a fegyveres Pruck Pál legendás archív fotója alá azonban nem az ő nevét, hanem egy kormánypárti színész, Dózsa László nevét írták ki."},
                    {"type": "dialogue", "speaker": "Rainer M. János", "text": "Minél makacsabbul tagadja a kormányzati apparátus a tévedést a nyilvánvaló levéltári bizonyítékok ellenére, annál mélyebbre süllyed a hivatalos emlékezetpolitika a hiteltelenség mocsarában. 1956-ból antikommunista fegyveres mítoszt akarnak faragni, kitörölve a munkástanácsokat és Nagy Imre mártíromságát."},
                    {"type": "narration", "text": "Nagy Imre szobrát az éj leple alatt távolították el a Parlament mellől, helyére pedig a Tanácsköztársaság vörösterrorjának Nemzeti Vértanúi emlékművét állították vissza a Horthy-korszak stílusában."},
                    {"type": "narration", "text": "A forradalom sokszínű emlékezete a hatalom ideológiai kényszerzubbonya alá került, elválasztva a nemzetet saját legtisztább 20. századi pillanatától."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Mi volt a 2016-os Dózsa László-plakátbotrány lényege?", [
                    "A forradalom 60. évfordulóján egy híres archív fotón szereplő 15 éves pesti srác, Pruck Pál arcához tévesen egy kormánypárti színész nevét rendelték, s a tévedést a bizonyítékok ellenére sem voltak hajlandók elismerni.",
                    "Hogy a plakátokat túl magasra ragasztották a villanyoszlopokon.",
                    "Hogy fekete-fehér helyett színes papírra nyomtatták a képeket."
                ], 0, ["c1-emlekezetpolitika-vocab"]),
                fb("grammar", "controlled", "Minél makacsabbul ragaszkodnak a propagandához, _____ nevetségesebbé válik az állami történetírás. (the more / annál)", "annál", "The more stubbornly they adhere to propaganda, the more ridiculous state historiography becomes.", ["c1-adv-proportional-exculpatory-narratives"]),
                match("vocabulary", "controlled", [["Dózsa László-botrány", "az 1956-os archív fotó politikai meghamisítása"], ["Nagy Imre szoboráthelyezése", "a mártír miniszterelnök szimbolikus kiszorítása a Kossuth térről"], ["forradalmi konszenzus", "1956 nemzeti egységének eszméje"], ["történelemhamisítás", "levéltári tények felülírása hatalmi szempontokból"]], ["c1-emlekezetpolitika-vocab"]),
                fb("grammar", "practice", "Amilyen mértékben átírják a forradalom történetét, olyan _____ sérül a nemzeti emlékezet. (proportion / arányban)", "arányban", "In proportion as they rewrite the history of the revolution, to that extent national memory is damaged.", ["c1-adv-proportional-exculpatory-narratives"]),
                sb("grammar", "practice", ["Minél", "több", "a", "hamisítás,", "annál", "mélyebb", "a", "hitelességvesztés."], ["Minél", "több", "a", "hamisítás,", "annál", "mélyebb", "a", "hitelességvesztés."], "The more the falsification, the deeper the loss of credibility.", ["c1-adv-proportional-exculpatory-narratives"]),
                dc("dialogue", [
                    {"speaker": "Történelemtanár", "text": "Hogyan tanítsuk 1956 történetét az új tankönyvi átírások után?"},
                    {"speaker": "Szakfelügyelő", "text": "Csakis a forrásokra támaszkodva: minél inkább politikai propagandává silányítják a forradalmat, _____ fontosabb a hiteles tények bemutatása."},
                    {"speaker": "Történelemtanár", "text": "A diákoknak joguk van az igazsághoz."}
                ], ["annál", "mindig", "soha"], 0, ["c1-adv-proportional-exculpatory-narratives"]),
                sw("production", [{"prompt": "Write a sentence analyzing historical distortion using 'Minél... annál...'.", "answer": "Minél inkább megpróbálja a politikai hatalom a saját ideológiájához igazítani az 1956-os forradalmat, annál inkább megsemmisíti a nemzeti konszenzust és a forradalom valódi hitelességét."}], ["c1-adv-proportional-exculpatory-narratives"]),
                mc("grammar", "check", "Melyik arányossági szerkezet ragadja meg a történelemhamisítás dinamikáját a legpontosabban?", [
                    "Minél agresszívabb a történelmi átírás... annál mélyebb hitelességvesztést szenved el az állam / Amilyen mértékben... olyan arányban",
                    "Ha sokáig beszél a szónok, megunják a nézők",
                    "Szépek a régi fényképek a falon"
                ], 0, ["c1-adv-proportional-exculpatory-narratives"])
            ]
        },
        {
            "num": 4,
            "stem": f"c1-{slug}-04",
            "title": "Horthy Era Rehabilitation & Ideological Whitewashing",
            "grammar_title": "Epistemic Stance Markers Assessing Ideological Whitewashing of Totalitarian Collaboration",
            "grammar_skill": "c1-epistemic-ideological-whitewashing",
            "goals": [
                "I can analyze the political rehabilitation of Miklós Horthy, interwar authoritarianism, and antisemitic legislation whitewashing (*Horthy-korszak rehabilitációja, numerus clausus, zsidótörvények, tekintélyelvű rezsim*).",
                "I can deploy epistemic stance markers assessing ideological whitewashing (*kétségkívül bebizonyosodott a Horthy-rendszer felelőssége a tragédiában, minden jel szerint a szoborállítások a tekintélyelvű múlt tisztára mosását szolgálják, aligha vitatható az antiszemitizmus állami intézményesülése*).",
                "I can critique nostalgic authoritarian restoration in political ethics."
            ],
            "vocab": [
                {"lemma": "Horthy-korszak", "translation": "Horthy era (1920–1944 interwar regime)", "pos": "expression"},
                {"lemma": "rehabilitáció", "translation": "political rehabilitation", "pos": "noun"},
                {"lemma": "numerus clausus", "translation": "numerus clausus (1920 anti-Jewish university quota)", "pos": "expression"},
                {"lemma": "zsidótörvények", "translation": "anti-Jewish racial laws (1938–1941)", "pos": "expression"},
                {"lemma": "fehérterror", "translation": "White Terror (1919–1920)", "pos": "noun"},
                {"lemma": "tisztára mosás", "translation": "whitewashing of historical guilt", "pos": "expression"},
                {"lemma": "autoriter nosztalgia", "translation": "authoritarian nostalgia", "pos": "expression"},
                {"lemma": "történelmi bűnrészesség", "translation": "historical complicity", "pos": "expression"}
            ],
            "gr_text1": "Epistemic stance markers formulate objective evidentiary judgments rejecting historical whitewashing: `kétségkívül bebizonyosodott a Horthy-rendszer közvetlen bűnrészessége a kamenyec-podolszkiji és újvidéki mészárlásokban` (the direct complicity of the Horthy regime in the Kamenets-Podolsky and Novi Sad massacres has undoubtedly been demonstrated), `minden jel szerint a Horthy-szobrok avatása a tekintélyelvű államberendezkedés legitimálását célozza` (by all indications the unveiling of Horthy statues aims at legitimizing an authoritarian state order), `aligha vitatható a numerus clausus és a zsidótörvények jogfosztó jellege` (the disenfranchising nature of numerus clausus and anti-Jewish laws can hardly be disputed).",
            "gr_text2": "Example: `Kétségkívül bebizonyosodott, hogy a Horthy-rendszer nem a polgári demokrácia aranykora, hanem a jogfosztó antiszemita törvényhozás és a tragikus háborús vereség korszaka volt`.",
            "gr_table": [
                ["Kétségkívül látható a Horthy-korszak szelektív és nosztalgikus tisztára mosása.", "Undoubtedly the selective and nostalgic whitewashing of the Horthy era is visible."],
                ["Minden jel szerint a kormányzat a két világháború közötti tekintélyuralmi mintákhoz nyúl vissza.", "By all indications the government reaches back to interwar authoritarian models."],
                ["Aligha vitatható a magyar államgépezet felelőssége a deportálásokban.", "Responsibility of the Hungarian state machinery in deportations can hardly be disputed."]
            ],
            "world_story_seg": {
                "seg_slug": "c1-emlekezetpolitika-04-horthy-rehabilitacio",
                "title": "A tisztára mosott kormányzó: A Horthy-kultusz feltámadása",
                "summary": "Középületek elnevezése, szoboravatások és a tankönyvek átszabása: hogyan próbálja a hatalom rehabilitálni Horthy Miklós tekintélyelvű rendszerét.",
                "paragraphs": [
                    {"type": "narration", "text": "A 2010 utáni politikai kurzus fokozatosan nyitotta meg az utat a Horthy-korszak szimbolikus rehabilitációja előtt. Sorra avattak szobrokat a kormányzónak kormánypárti politikusok részvételével, Kenderesen állami tiszteletadás kísérte az újratemetési évfordulót, a parlamentben pedig Horthy-mellszobor kapott helyet."},
                    {"type": "dialogue", "speaker": "Karsai László", "text": "Kétségkívül bebizonyosodott a történelmi tények alapján: Horthy Miklós nem volt megmentő. Aligha vitatható, hogy az ő vezetése alatt fogadták el Európa első antiszemita törvényét, a numerus clausust, s az ő kormányzósága alatt hurcoltak el több mint négyszázezer magyar állampolgárt Auschwitzba a magyar hatóságok segítségével."},
                    {"type": "narration", "text": "Az autoriter nosztalgia és a felelősség elmaszatolása a jelenkori hatalomgyakorlás mintájául szolgál: a vármegyerendszer, a főispáni címek visszahozatala a két világháború közötti félfeudális világ restaurációját idézi."},
                    {"type": "narration", "text": "A múlt tisztára mosása mérgezi a társadalmi békét, s megfosztja Magyarországot attól, hogy a modern európai köztársasági értékek talaján álljon."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Milyen történelmi tények cáfolják Horthy Miklós kizárólagos 'nemzetmentő' mítoszát?", [
                    "A fehérterror gyilkosságai, a numerus clausus, a zsidótörvények bevezetése, a Don-kanyarba küldött 2. magyar hadsereg pusztulása és a vidéki zsidóság deportálása a magyar csendőrség által.",
                    "Hogy nem tudott autót vezetni.",
                    "Hogy nem szerette a színházat."
                ], 0, ["c1-emlekezetpolitika-vocab"]),
                fb("grammar", "controlled", "Kétségkívül _____ a Horthy-korszak felelőssége a jogfosztó törvények bevezetésében. (demonstrated / bebizonyosodott)", "bebizonyosodott", "Undoubtedly the responsibility of the Horthy era in introducing disenfranchising laws has been demonstrated.", ["c1-epistemic-ideological-whitewashing"]),
                match("vocabulary", "controlled", [["numerus clausus", "a zsidó diákok egyetemi felvételét korlátozó 1920-as törvény"], ["Horthy-korszak", "a két világháború közötti félfeudális kormányzóság"], ["tisztára mosás", "a történelmi felelősség elhazudása politikai okokból"], ["autoriter nosztalgia", "vonzódás a korábbi tekintélyelvű rendszerek külsőségeihez"]], ["c1-emlekezetpolitika-vocab"]),
                fb("grammar", "practice", "Aligha vitatható, hogy a Horthy-szobrok állítása a tekintélyelvű múlt _____ szolgálja. (whitewashing / tisztára mosását)", "tisztára mosását", "It can hardly be disputed that erecting Horthy statues serves the whitewashing of the authoritarian past.", ["c1-epistemic-ideological-whitewashing"]),
                sb("grammar", "practice", ["Kétségkívül", "bebizonyosodott", "az", "állami", "bűnrészesség", "a", "deportálásokban."], ["Kétségkívül", "bebizonyosodott", "az", "állami", "bűnrészesség", "a", "deportálásokban."], "Undoubtedly state complicity in deportations has been demonstrated.", ["c1-epistemic-ideological-whitewashing"]),
                dc("dialogue", [
                    {"speaker": "Egyetemista", "text": "Miért aggályos a vármegyék és főispánok visszahozatala a közigazgatásba?"},
                    {"speaker": "Történész", "text": "Mert minden jel szerint ez a Horthy-korszak tekintélyelvű szimbólumrendszerének tudatos _____ jelenti."},
                    {"speaker": "Egyetemista", "text": "A köztársasági hagyomány feladása súlyos visszalépés."},
                ], ["restaurációját", "tagadását", "feledését"], 0, ["c1-epistemic-ideological-whitewashing"]),
                sw("production", [{"prompt": "Write a critical evaluation of authoritarian rehabilitation using an epistemic stance marker.", "answer": "Kétségkívül bebizonyosodott a levéltári források alapján, hogy a Horthy-korszak bűneinek tisztára mosása és az autoriter nosztalgia szembemegy a modern európai köztársasági jogállamiság alapértékeivel."}], ["c1-epistemic-ideological-whitewashing"]),
                mc("grammar", "check", "Melyik episztemikus kifejezés leplezi le a történelmi rehabilitációt a legmeggyőzőbben?", [
                    "kétségkívül bebizonyosodott / aligha vitatható a felelősség elfedése",
                    "úgy tűnik talán nem volt minden tökéletes régen",
                    "reméljük szépen megkoszorúzzák a szobrot"
                ], 0, ["c1-epistemic-ideological-whitewashing"])
            ]
        },
        {
            "num": 5,
            "stem": f"c1-{slug}-05",
            "title": "Historical Justice & The Horizon of Moral Truth",
            "grammar_title": "Evaluative Synthesis Particles Formulating Manifestos for Authentic National Historical Reckoning",
            "grammar_skill": "c1-adv-conclusive-historical-justice-synthesis",
            "goals": [
                "I can analyze democratic memory culture, pluralistic commemoration, and the road to authentic historical justice (*demokratikus emlékezetkultúra, történelmi igazságtétel, erkölcsi katarzis, megbékélés*).",
                "I can deploy evaluative synthesis particles formulating conclusive manifestos (*végső soron elengedhetetlen a múlttal való őszinte szembenézés, mindent egybevetve az igazság kimondása a nemzeti megbékélés egyetlen záloga, végeredményben a revizionista mítoszok összeomlanak a tények súlya alatt*).",
                "I can synthesize a vision for democratic historical consciousness in European Hungary."
            ],
            "vocab": [
                {"lemma": "emlékezetkultúra", "translation": "memory culture / commemorative ethics", "pos": "noun"},
                {"lemma": "történelmi igazság", "translation": "historical truth", "pos": "expression"},
                {"lemma": "megbékélés", "translation": "reconciliation / historical peace", "pos": "noun"},
                {"lemma": "demokratikus öntudat", "translation": "democratic civic consciousness", "pos": "expression"},
                {"lemma": "kollektív felelősség", "translation": "collective moral responsibility", "pos": "expression"},
                {"lemma": "katarzis", "translation": "moral / historical catharsis", "pos": "noun"},
                {"lemma": "történelmi érettség", "translation": "historical maturity", "pos": "expression"},
                {"lemma": "szabad nyilvánosság", "translation": "free public sphere", "pos": "expression"}
            ],
            "gr_text1": "Evaluative synthesis particles formulate definitive moral conclusions asserting the indispensable necessity of historical honesty: `végső soron elengedhetetlen a nemzeti múlttal való illúziómentes szembenézés` (ultimately illusion-free confrontation with the national past is indispensable), `mindent egybevetve az igazság bátor kimondása a valódi megbékélés egyetlen szilárd záloga` (all things considered brave utterance of truth is the sole solid guarantee of genuine reconciliation), `végeredményben az önfelmentő mítoszok lerombolása nélkül nem létezhet érett polgári demokrácia` (in the final analysis without dismantling self-exculpatory myths mature civic democracy cannot exist).",
            "gr_text2": "Example: `Végső soron elengedhetetlen felismerni: mindent egybevetve a nemzet nem a bűnök elhallgatásával, hanem az őszinte szembenézéssel és az igazságtétellel válhat lelkileg szabaddá`.",
            "gr_table": [
                ["Végső soron elengedhetetlen a történelmi tények megalkuvás nélküli feltárása.", "Ultimately uncompromising uncovering of historical facts is indispensable."],
                ["Mindent egybevetve a megbékélés csakis az igazság talaján születhet meg.", "All things considered reconciliation can only be born on the ground of truth."],
                ["Végeredményben a propaganda sohasem győzheti le a levéltári tények valóságát.", "In the final analysis propaganda can never defeat the reality of archival facts."]
            ],
            "world_story_seg": {
                "seg_slug": "c1-emlekezetpolitika-05-tortenelmi-igazsag-jovo",
                "title": "A katarzis horizontja: Az őszinte szembenézés jövője",
                "summary": "A revizionista mítoszok lebontása és a demokratikus emlékezetkultúra megteremtése a magyar társadalom történelmi érettségének záloga.",
                "paragraphs": [
                    {"type": "narration", "text": "A huszonegyedik század harmadik évtizedében a magyar társadalom válaszút előtt áll: vagy folytatja a felelősséghárító, önfelmentő mítoszok ápolását, vagy vállalja a bibói utat, az illúziómentes szembenézést saját történelmével."},
                    {"type": "dialogue", "speaker": "Gyáni Gábor", "text": "Végső soron elengedhetetlen a revizionista mítoszok meghaladása. Mindent egybevetve a nemzeti nagyság nem a tévedhetetlenség hazugságában, hanem az erkölcsi tisztánlátásban rejlik. Amíg nem merjük kimondani a belső cinkosság és a diktatúrák igazságát, addig a múlt foglyai maradunk."},
                    {"type": "narration", "text": "A demokratikus emlékezetkultúra nem bűnbakokat keres, hanem a történelmi katarzist segíti elő: olyan közös teret teremt, ahol a holokauszt, a gulág, 1956 és a rendszerváltás emléke nem hatalmi fegyver, hanem a szabadság közös értéke."},
                    {"type": "narration", "text": "Mindent egybevetve a magyar nemzet jövője az igazság felszabadító erején múlik: a félelem nélküli szembenézés teremtheti meg a szabad, európai polgári Magyarországot."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Mi a demokratikus emlékezetkultúra legfontosabb ismérve?", [
                    "A többhangú, kritikai és forrásokon alapuló múltfeldolgozás, amely nem szolgál ki aktuálpolitikai érdekeket, és képes szembenézni a nemzeti bűnökkel és tragédiákkal is.",
                    "A kötelező iskolai egyenruha viselése a nemzeti ünnepeken.",
                    "A régi pénzérmék gyűjtése."
                ], 0, ["c1-emlekezetpolitika-vocab"]),
                fb("grammar", "controlled", "Végső soron _____ a bátor szembenézés és a történelmi katarzis megélése. (indispensable / elengedhetetlen)", "elengedhetetlen", "Ultimately brave confrontation and living historical catharsis is indispensable.", ["c1-adv-conclusive-historical-justice-synthesis"]),
                match("vocabulary", "controlled", [["emlékezetkultúra", "a társadalom viszonya saját múltjához és emlékeihez"], ["történelmi igazság", "levéltári tényeken nyugvó, manipulációmentes valóság"], ["történelmi érettség", "egy nemzet képessége a saját felelősségének beismerésére"], ["katarzis", "az igazság kimondása révén bekövetkező morális felszabadulás"]], ["c1-emlekezetpolitika-vocab"]),
                fb("grammar", "practice", "Mindent egybevetve az őszinte szembenézés a nemzeti megbékélés egyetlen szilárd _____ . (guarantee / záloga)", "záloga", "All things considered honest confrontation is the sole solid guarantee of national reconciliation.", ["c1-adv-conclusive-historical-justice-synthesis"]),
                sb("grammar", "practice", ["Végső", "soron", "elengedhetetlen", "a", "történelmi", "igazság", "kimondása."], ["Végső", "soron", "elengedhetetlen", "a", "történelmi", "igazság", "kimondása."], "Ultimately stating historical truth is indispensable.", ["c1-adv-conclusive-historical-justice-synthesis"]),
                dc("dialogue", [
                    {"speaker": "Filozófus", "text": "Hogyan érheti el Magyarország a valódi nemzeti megbékélést?"},
                    {"speaker": "Történész", "text": "Kizárólag úgy, ha felismerjük: mindent egybevetve az igazság eltagadása újabb tragédiákhoz vezet, míg a tisztánlátás a nemzet igazi _____."},
                    {"speaker": "Filozófus", "text": "Ez Bibó István örök érvényű tanítása."}
                ], ["záloga", "ára", "terhe"], 0, ["c1-adv-conclusive-historical-justice-synthesis"]),
                sw("production", [{"prompt": "Write a concluding manifesto on historical justice using an evaluative synthesis particle.", "answer": "Végső soron elengedhetetlen a revizionista mítoszok meghaladása és az őszinte szembenézés, hiszen mindent egybevetve a történelmi katarzis és az igazságtétel az érett demokratikus Magyarország egyetlen hiteles záloga."}], ["c1-adv-conclusive-historical-justice-synthesis"]),
                mc("grammar", "check", "Melyik szintetizáló szerkezet fogalmazza meg a történelmi igazságtétel szükségességét a legmagasabb szinten?", [
                    "végső soron elengedhetetlen a múlttal való szembenézés / mindent egybevetve az igazság a megbékélés záloga",
                    "reméljük a jövőben nem lesz több háború a világban",
                    "jó lenne ha mindenki szépen megegyezne a vitákban"
                ], 0, ["c1-adv-conclusive-historical-justice-synthesis"])
            ]
        }
    ]

    for l in disc_lessons:
        emit_instructional_lesson(31, "discourse", l, disc_title, disc_intro if l["num"] == 1 else None)

    # Combined World Story
    write_json(
        f"stories/world/c1/c1-{slug}-revizionizmus-emlekezetpolitika.json",
        {
            "id": f"story.c1.{slug}.combined",
            "title": "A múlt fogságában: Állami revizionizmus és az igazság küzdelme",
            "level": "C1",
            "lesson": 5,
            "order": 31,
            "type": "world",
            "estimatedMinutes": 8,
            "grammar": ["c1-adv-conclusive-historical-justice-synthesis"],
            "summary": "Átfogó tényfeltáró esszé a 2010 utáni magyar állami emlékezetpolitikáról: a Szabadság téri német megszállási emlékműről és az áldozati mítoszról, a Terror Háza totalitárius összemosásáról, az 1956-os forradalom átírásáról és a Dózsa László-botrányról, a Horthy-korszak rehabilitációjáról, valamint a demokratikus történelmi katarzis horizontjáról.",
            "vocabularyTopics": [
                "The House of Terror, 1956 Revisionism & Historical Revisionism",
                "Historical Justice & The Horizon of Moral Truth"
            ],
            "paragraphs": [
                {"type": "narration", "text": "A magyar politikai életben a történelem a hatalomgyakorlás legfontosabb legitimációs eszközévé vált. Az államilag vezérelt revizionizmus szisztematikus stratégiája nyomán a hatalom megkísérelte a huszadik századi nemzeti tragédiák átírását, elfedve a magyar államgépezet belső felelősségét, és az egész társadalmat kizárólagos passzív áldozatként feltüntetve."},
                {"type": "narration", "text": "E stratégia leglátványosabb megnyilvánulása a Szabadság téri német megszállási emlékmű és a Terror Háza Múzeum kiállítási koncepciója lett. A nyilas és a kommunista bűnök felületes összemosásával a hivatalos narratíva azt sugallta, hogy a totalitárius diktatúrák kizárólag külső erők által kényszerített epizódok voltak, elhallgatva a magyar közigazgatás és társadalom bűnrészességét a holokausztban."},
                {"type": "narration", "text": "Az 1956-os forradalom emlékezetét hasonló ideológiai csonkítás érte: minél inkább antikommunista fegyveres mítosszá próbálta redukálni a kormányzat a forradalmat, annál inkább háttérbe szorult Nagy Imre mártíromsága és a munkástanácsok szerepe. A Dózsa László-plakátbotrány leleplezte a politikai mítoszépítés groteszk hitelességvesztését."},
                {"type": "narration", "text": "Ezzel párhuzamosan kezdetét vette a Horthy-korszak tekintélyuralmi rendszerének lopakodó rehabilitációja: a vármegyék, főispánok visszahozatala és a Horthy-szobrok avatása leplezte le az autoriter nosztalgiát. Kétségkívül bebizonyosodott, hogy a múlt tisztára mosása a jelenkori hatalomgyakorlás mintájaként szolgál."},
                {"type": "narration", "text": "Végső soron elengedhetetlen felismerni: mindent egybevetve egyetlen nemzet sem építhet tartós jövőt a történelemhamisítás és az önfelmentés talaján. Ahogyan Bibó István tanította: a szabadság ott kezdődik, ahol megszűnik a félelem. A magyar demokrácia felemelkedése kizárólag a tények bátor feltárásában és a valódi történelmi katarzisban gyökerezhet."}
            ]
        }
    )

    # Discourse Consolidation
    emit_consolidation_lesson(
        31,
        "discourse",
        f"c1-{slug}-consolidation",
        disc_title,
        [
            "I can diagnose state-directed historical revisionism, victimhood propaganda, and monument scandals.",
            "I can evaluate totalitarian equivalence in the House of Terror, 1956 revisionism, and the Dózsa László affair.",
            "I can critique Horthy-era rehabilitation, ideological whitewashing, and formulate manifestos for historical justice."
        ],
        [
            mc("grammar", "recognize", "Milyen szerkezettel diagnosztizálhatjuk az állami emlékezetpolitika revizionista fordulatát?", [
                "az államilag vezérelt revizionizmus szisztematikus stratégiája nyomán / az emlékezetpolitika átírása következtében",
                "hogyha valaki régi könyveket olvas a padláson",
                "amikor új festéket kapnak a kerítések"
            ], 0, ["c1-discourse-historical-revisionism-framing"]),
            mc("grammar", "recognize", "Melyik modális kifejezés írja elő a történész etikai kötelességét a legszigorúbban?", [
                "a kutatóknak kötelességük ragaszkodni az igazsághoz / nem engedhető meg a bűnök relativizálása",
                "szabadon sétálhatnak a múzeumi folyosókon",
                "bármikor megihatnak egy pohár vizet a teremben"
            ], 0, ["c1-modal-deontic-intellectual-honesty"]),
            match("vocabulary", "recognize", [["emlékezetpolitika", "a múlt állami szintű, ideológiai vezérlésű használata"], ["Szabadság téri emlékmű", "az állami felelősséget elhárító áldozati szoborcsoport"], ["Dózsa László-botrány", "az 1956-os pesti srác fotójának politikai meghamisítása"], ["Terror Háza", "a diktatúrákat vitatott módon bemutató emlékhely"], ["Horthy-rehabilitáció", "a két világháború közötti rendszer tekintélyelvű tisztára mosása"]], ["c1-emlekezetpolitika-vocab"]),
            fb("vocabulary", "recall", "A történelmi tények szándékos eltorzítása a történelem-_____ . (falsification / hamisítás)", "hamisítás", "Deliberate distortion of historical facts is falsification of history.", ["c1-emlekezetpolitika-vocab"]),
            fb("vocabulary", "recall", "A bűnök elismerése révén bekövetkező morális megtisztulás a történelmi _____ . (catharsis / katarzis)", "katarzis", "Moral cleansing occurring via acknowledging sins is historical catharsis.", ["c1-emlekezetpolitika-vocab"]),
            fb("grammar", "recall", "A szakembereknek kötelességük _____ a szigorú forráskritikához. (adhere / ragaszkodniuk)", "ragaszkodniuk", "Experts have a duty to adhere to strict source criticism.", ["c1-modal-deontic-intellectual-honesty"]),
            fb("grammar", "context", "Minél több a propaganda, _____ mélyebb a hitelességvesztés. (the deeper / annál)", "annál", "The more the propaganda, the deeper the loss of credibility.", ["c1-adv-proportional-exculpatory-narratives"]),
            fb("grammar", "context", "Végső soron _____ a revizionista mítoszok meghaladása. (indispensable / elengedhetetlen)", "elengedhetetlen", "Ultimately overcoming revisionist myths is indispensable.", ["c1-adv-conclusive-historical-justice-synthesis"]),
            mc("grammar", "context", "Mi a szerepe az episztemikus kifejezéseknek a Horthy-rendszer bírálatában?", [
                "Objektív levéltári súlyt adnak annak kimondására, hogy az antiszemita törvényekért a magyar államgépezet felelős volt.",
                "Elnézést kérnek a múzeumi belépődíjak miatt.",
                "Megmutatják, mikor ér véget a tanév az egyetemen."
            ], 0, ["c1-epistemic-ideological-whitewashing"]),
            sb("grammar", "produce", ["A", "demokratikus", "emlékezet", "az", "igazság", "talaján", "épülhet", "fel."], ["A", "demokratikus", "emlékezet", "az", "igazság", "talaján", "épülhet", "fel."], "Democratic memory can be built on the ground of truth.", ["c1-adv-conclusive-historical-justice-synthesis"]),
            sw("production", [{"prompt": "Write a critical diagnosis of historical revisionism using a proportional correlative.", "answer": "Minél agresszívabban próbálja a politikai hatalom tisztára mosni a huszadik századi diktatúrák belső bűnrészességét, annál mélyebb morális válságba és nemzetközi elszigetelődésbe taszítja a társadalmat."}], ["c1-adv-proportional-exculpatory-narratives"]),
            sw("production", [{"prompt": "Formulate a concluding manifesto on authentic national historical reckoning.", "answer": "Végső soron elengedhetetlen felismerni: mindent egybevetve az illúziómentes szembenézés és a történelmi katarzis a szabad, demokratikus és európai Magyarország egyetlen megkérdőjelezhetetlen fundamentuma."}], ["c1-adv-conclusive-historical-justice-synthesis"])
        ]
    )

    print("=== Finished C1 Unit 31 ===")


if __name__ == "__main__":
    generate_unit_31()
