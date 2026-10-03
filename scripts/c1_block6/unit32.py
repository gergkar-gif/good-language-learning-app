#!/usr/bin/env python3
"""
Hungarian C1 Block 6 - Unit 32 Generator:
  - Track 1 (Core): Unit 32 — "Constitutional Jurisprudence & Fundamental Rights" (c1-32)
  - Track 2 (Discourse): Unit 32 — "The Dismantling of Independent Judiciary & Rule of Law Breakdown" (c1-jogallamisag)
"""

import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT))

from scripts.c1_block1.common import mc, match, fb, sb, dc, sw, write_json, emit_instructional_lesson, emit_consolidation_lesson
from scripts.c1_block6.registry_helper import register_unit


def generate_unit_32():
    print("=== Generating C1 Unit 32 ===")
    
    new_skills = {
        "c1-32-vocab": {"kind": "vocabulary"},
        "c1-jogallamisag-vocab": {"kind": "vocabulary"},
        "c1-adv-constitutional-norm-control": {"kind": "grammar"},
        "c1-participle-proportionality-test": {"kind": "grammar"},
        "c1-adv-human-dignity-absoluteness": {"kind": "grammar"},
        "c1-causal-constitutional-precedent-ratio": {"kind": "grammar"},
        "c1-syntax-invisible-constitution-doctrine": {"kind": "grammar"},
        "c1-discourse-judicial-subjugation-framing": {"kind": "grammar"},
        "c1-adv-institutional-monopolization-critique": {"kind": "grammar"},
        "c1-modal-deontic-judicial-integrity": {"kind": "grammar"},
        "c1-adv-proportional-eu-infringement-measures": {"kind": "grammar"},
        "c1-adv-conclusive-rule-of-law-restitution": {"kind": "grammar"},
    }
    new_titles = {
        "c1-32-vocab": "reading",
        "c1-jogallamisag-vocab": "reading",
        "c1-adv-constitutional-norm-control": "evaluative adverbials formulating abstract constitutional norm control and review",
        "c1-participle-proportionality-test": "participial constructions framing fundamental rights collision and proportionality tests",
        "c1-adv-human-dignity-absoluteness": "modal adverbials asserting human dignity as an absolute mother right",
        "c1-causal-constitutional-precedent-ratio": "complex causal connectives deducing ratio decidendi in constitutional jurisprudence",
        "c1-syntax-invisible-constitution-doctrine": "hypothetical and deductive syntax structuring the invisible constitution doctrine",
        "c1-discourse-judicial-subjugation-framing": "discourse markers diagnosing political subjugation of the independent judiciary",
        "c1-adv-institutional-monopolization-critique": "critical evaluative adverbials exposing arbitrary executive administrative monopoly over courts",
        "c1-modal-deontic-judicial-integrity": "deontic modal structures asserting constitutional duty of judicial integrity",
        "c1-adv-proportional-eu-infringement-measures": "proportional correlative structures linking judicial backsliding to european union sanctions",
        "c1-adv-conclusive-rule-of-law-restitution": "evaluative conclusive particles articulating systemic constitutional restitution of rule of law",
    }
    
    core_title = "Constitutional Jurisprudence & Fundamental Rights"
    core_stems = [f"c1-32-0{i}" for i in range(1, 6)] + ["c1-32-consolidation"]
    disc_title = "The Dismantling of Independent Judiciary & Rule of Law Breakdown"
    slug = "jogallamisag"
    disc_stems = [f"c1-{slug}-0{i}" for i in range(1, 6)] + [f"c1-{slug}-consolidation"]
    
    register_unit(32, core_title, core_stems, disc_title, disc_stems, new_skills, new_titles)

    # ----------------------------------------------------
    # TRACK 1: CORE (c1-32)
    # ----------------------------------------------------
    core_intro = [
        "Constitutional jurisprudence stands as the ultimate bulwark protecting fundamental rights against executive overreach and tyrannical legislative majorities.",
        "In this unit, centered on the foundational jurisprudence of the Hungarian Constitutional Court led by László Sólyom and his doctrine of the 'Invisible Constitution', you will master the elevated academic register of abstract norm control, fundamental rights proportionality tests, the inviolability of human dignity as a foundational mother right, and constitutional precedent at the C1 level."
    ]

    core_lessons = [
        {
            "num": 1,
            "stem": "c1-32-01",
            "title": "Constitutional Norm Control & Abstract Review",
            "grammar_title": "Evaluative Adverbials Formulating Abstract Constitutional Norm Control and Review",
            "grammar_skill": "c1-adv-constitutional-norm-control",
            "goals": [
                "I can analyze constitutional norm control, abstract judicial review, and the striking down of unconstitutional statutes (*alkotmányossági normakontroll, előzetes és utólagos felülvizsgálat, alaptörvény-ellenesség megsemmisítése*).",
                "I can deploy elevated evaluative adverbials formulating constitutional scrutiny (*alkotmányjogi szempontból vizsgálva, anyagi jogi alapon eljárva, hatáskörileg megsemmisítve*).",
                "I can assess the procedural requirements of legal certainty in constitutional court jurisprudence."
            ],
            "vocab": [
                {"lemma": "alkotmányossági normakontroll", "translation": "constitutional norm control / review", "pos": "expression"},
                {"lemma": "előzetes normakontroll", "translation": "ex-ante constitutional review", "pos": "expression"},
                {"lemma": "utólagos normakontroll", "translation": "ex-post constitutional review", "pos": "expression"},
                {"lemma": "absztrakt felülvizsgálat", "translation": "abstract judicial review", "pos": "expression"},
                {"lemma": "megsemmisítés", "translation": "annulment / striking down of statute", "pos": "noun"},
                {"lemma": "alaptörvény-ellenesség", "translation": "unconstitutionality", "pos": "noun"},
                {"lemma": "jogbiztonság elve", "translation": "principle of legal certainty", "pos": "expression"},
                {"lemma": "hatásköri túllépés", "translation": "ultra vires act / exceeding statutory competence", "pos": "expression"}
            ],
            "gr_text1": "Evaluative adverbials in constitutional law formulate the authoritative grounds on which legislation is scrutinized and struck down: `alkotmányjogi szempontból vizsgálva` (examined from a constitutional law perspective), `anyagi jogi alapon eljárva` (proceeding on substantive legal grounds), `hatáskörileg megsemmisítve` (annulled within constitutional jurisdiction), `a jogbiztonság elvét szigorúan szem előtt tartva` (keeping strictly in mind the principle of legal certainty).",
            "gr_text2": "Example: `A testület az alaptörvény-ellenes jogszabályt alkotmányjogi szempontból vizsgálva, anyagi jogi alapon haladéktalanul megsemmisítette`.",
            "gr_table": [
                ["A bíróság az eljárási hibát alkotmányjogi szempontból vizsgálva semmisnek nyilvánította a törvényt.", "Examining the procedural defect from a constitutional law perspective the court declared the law void."],
                ["A taláros testület hatáskörileg eljárva határozott a vitatott normáról.", "Acting within its jurisdiction the robed body decided on the contested norm."],
                ["A testület a jogbiztonság elvét szem előtt tartva határozta meg a hatálybalépés idejét.", "Keeping the principle of legal certainty in mind the body determined the date of entry into force."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mi az alkotmányossági utólagos normakontroll lényege?", [
                    "A már kihirdetett és hatályba lépett jogszabályok alaptörvény-ellenességének vizsgálata és szükség esetén megsemmisítése.",
                    "A parlamenti képviselők igazolatlan hiányzásának fegyelmi büntetése.",
                    "A minisztériumi költségvetési kiadások utólagos könyvelési ellenőrzése."
                ], 0, ["c1-32-vocab"]),
                fb("grammar", "controlled", "A testület a vitatott passzust alkotmányjogi szempontból _____ megsemmisítette az alaptörvény-ellenes rendelkezést. (examining / vizsgálva)", "vizsgálva", "Examining the contested clause from a constitutional law perspective the body annulled the unconstitutional provision.", ["c1-adv-constitutional-norm-control"]),
                match("vocabulary", "controlled", [
                    ["előzetes normakontroll", "jogszabály kihirdetés előtti alkotmányossági vizsgálata"],
                    ["utólagos normakontroll", "már hatályos jogszabály felülvizsgálata és megsemmisítése"],
                    ["jogbiztonság elve", "a kiszámítható és egyértelmű jogalkotás alapkövetelménye"],
                    ["hatásköri túllépés", "az intézmény törvényes jogkörein kívüli önkényes cselekvés"]
                ], ["c1-32-vocab"]),
                fb("grammar", "practice", "A bíróság anyagi jogi alapon _____ semmisnek mondta ki a rendeletet. (proceeding / eljárva)", "eljárva", "Proceeding on substantive legal grounds the court declared the decree void.", ["c1-adv-constitutional-norm-control"]),
                sb("grammar", "practice", ["Az", "Alkotmánybíróság", "anyagi", "jogi", "alapon", "megsemmisítette", "a", "törvényt."], ["Az", "Alkotmánybíróság", "anyagi", "jogi", "alapon", "megsemmisítette", "a", "törvényt."], "The Constitutional Court annulled the statute on substantive legal grounds.", ["c1-adv-constitutional-norm-control"]),
                dc("dialogue", [
                    {"speaker": "Jogtudós", "text": "Miért olyan lényeges az absztrakt utólagos normakontroll a jogállamban?"},
                    {"speaker": "Alkotmánybíró", "text": "Mert alkotmányjogi szempontból vizsgálva ez garantálja, hogy a parlamenti többség ne hozhasson _____ törvényeket."},
                    {"speaker": "Jogtudós", "text": "Ez a fékek és egyensúlyok legfőbb fundamentuma."}
                ], ["alaptörvény-ellenes", "költségvetési", "nemzetközi"], 0, ["c1-adv-constitutional-norm-control"]),
                sw("production", [{"prompt": "Write a sentence formulating constitutional review using an evaluative adverbial.", "answer": "Az Alkotmánybíróság a vitatott törvényt alkotmányjogi szempontból vizsgálva, anyagi jogi alapon megsemmisítette, a jogbiztonság elvét védve a törvényhozói túlterjeszkedéssel szemben."}], ["c1-adv-constitutional-norm-control"]),
                mc("grammar", "check", "Melyik határozói szerkezet fejezi ki a legpontosabban a bírósági normakontrollt?", [
                    "alkotmányjogi szempontból vizsgálva / anyagi jogi alapon eljárva",
                    "jogszabályokat lapozgatva hirtelen",
                    "parlamenti szavazás után szomorúan"
                ], 0, ["c1-adv-constitutional-norm-control"])
            ]
        },
        {
            "num": 2,
            "stem": "c1-32-02",
            "title": "Fundamental Rights Collision & Proportionality Test",
            "grammar_title": "Participial Constructions Framing Fundamental Rights Collision and Proportionality Tests",
            "grammar_skill": "c1-participle-proportionality-test",
            "goals": [
                "I can analyze fundamental rights collision, constitutional necessity, and the strict proportionality test (*alapjogi kollízió, szükségesség-arányossági teszt, a lényeges tartalom érinthetetlensége*).",
                "I can construct complex participial clauses weighing competing constitutional interests (*egymással versengő alapjogokat mérlegre téve, a legenyhébb eszköz elvét érvényesítve, az arányosság követelményét tiszteletben tartva*).",
                "I can critique legislative restrictions on civil liberties in academic jurisprudence."
            ],
            "vocab": [
                {"lemma": "alapjogi kollízió", "translation": "collision of fundamental rights", "pos": "expression"},
                {"lemma": "arányossági teszt", "translation": "proportionality test", "pos": "expression"},
                {"lemma": "szükségesség-arányosság", "translation": "necessity and proportionality", "pos": "expression"},
                {"lemma": "lényeges tartalom", "translation": "essential content / core of a right", "pos": "expression"},
                {"lemma": "alapjog-korlátozás", "translation": "limitation of fundamental rights", "pos": "noun"},
                {"lemma": "mérlegelési jogkör", "translation": "discretionary power / judicial balancing", "pos": "expression"},
                {"lemma": "legitim cél", "translation": "legitimate objective / constitutional aim", "pos": "expression"},
                {"lemma": "legenyhébb eszköz elve", "translation": "principle of the least restrictive means", "pos": "expression"}
            ],
            "gr_text1": "Participial constructions in constitutional jurisprudence formalize the judicial balancing test between competing fundamental rights: `egymással ütköző alapjogokat mérlegre téve` (weighing conflicting fundamental rights), `a legenyhébb korlátozást előíró eszközt választva` (choosing the tool prescribing the least restriction), `a lényeges tartalom csorbítását elutasítva` (rejecting any curtailment of the essential core).",
            "gr_text2": "Example: `A testület az alapjogok kollízióját feloldva és a legenyhébb eszköz elvét érvényesítve ítélte meg a korlátozás arányosságát`.",
            "gr_table": [
                ["A testület a véleménynyilvánítás szabadságát a személyiségi jogokkal mérlegre téve döntött.", "Weighing freedom of expression against personality rights the body decided."],
                ["A bírák a szükségesség és arányosság elvét szem előtt tartva vizsgálták a törvényt.", "Keeping the principle of necessity and proportionality in mind the judges scrutinized the statute."],
                ["Az alapjog lényeges tartalmát védelmezve utasították el a korlátozást.", "Defending the essential content of the fundamental right they rejected the limitation."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mikor tekinthető alkotmányosnak egy alapjog korlátozása a szükségesség-arányossági teszt szerint?", [
                    "Kizárólag akkor, ha egy másik alapjog vagy alkotmányos érték védelmében elkerülhetetlen, legitim célt szolgál, és a cél elérésére alkalmas legenyhébb eszközt alkalmazza anélkül, hogy a jog lényeges tartalmát sértené.",
                    "Bármikor, amikor a parlamenti többség gazdaságilag kényelmesnek találja.",
                    "Kizárólag rendkívüli téli időjárás és havazás idején."
                ], 0, ["c1-32-vocab"]),
                fb("grammar", "controlled", "A testület a versengő alapjogokat mérlegre _____ állapította meg az aránytalanságot. (putting / téve)", "téve", "Putting competing fundamental rights onto the scale the body established the disproportionality.", ["c1-participle-proportionality-test"]),
                match("vocabulary", "controlled", [
                    ["alapjogi kollízió", "két vagy több alapvető szabadságjog egymással való ütközése"],
                    ["arányossági teszt", "a jogkorlátozás szükségességét és mértékét vizsgáló bírósági mérce"],
                    ["lényeges tartalom", "az alapjog elvonhatatlan magva, amely soha nem korlátozható"],
                    ["legenyhébb eszköz elve", "a célt legkisebb jogi sérelemmel megvalósító intézkedés követelménye"]
                ], ["c1-32-vocab"]),
                fb("grammar", "practice", "A bírák a legenyhébb eszköz elvét _____ korlátozták az állami beavatkozást. (enforcing / érvényesítve)", "érvényesítve", "Enforcing the principle of the least restrictive means the judges restricted state intervention.", ["c1-participle-proportionality-test"]),
                sb("grammar", "practice", ["A", "bíróság", "az", "arányossági", "tesztet", "alkalmazva", "bírálta", "felül", "a", "korlátozást."], ["A", "bíróság", "az", "arányossági", "tesztet", "alkalmazva", "bírálta", "felül", "a", "korlátozást."], "Applying the proportionality test the court reviewed the restriction.", ["c1-participle-proportionality-test"]),
                dc("dialogue", [
                    {"speaker": "Ügyvéd", "text": "Hogyan oldható fel a sajtószabadság és a személyiségi jogok ütközése?"},
                    {"speaker": "Alkotmányjogász", "text": "A két alapjogot gondosan mérlegre _____ a testület a közérdekű viták elsőbbségét hangsúlyozza."},
                    {"speaker": "Ügyvéd", "text": "De a személy emberi méltósága nem sérülhet."}
                ], ["téve", "dobva", "hozva"], 0, ["c1-participle-proportionality-test"]),
                sw("production", [{"prompt": "Write a constitutional analysis of fundamental rights collision using a participial clause.", "answer": "Az egymással ütköző szabadságjogokat mérlegre téve és a legenyhébb eszköz elvét érvényesítve a bíróság megállapította, hogy a törvényhozó túllépte az arányos korlátozás alkotmányos kereteit."}], ["c1-participle-proportionality-test"]),
                mc("grammar", "check", "Melyik szerkezet fogalmazza meg az arányossági vizsgálatot szakszerű melléknévi igeneves formában?", [
                    "a versengő alapjogokat gondosan mérlegre téve és a lényeges tartalmat védelmezve",
                    "törvényeket gyorsan elfogadva a parlamentben",
                    "egy újságcikket elolvasva a tárgyalóteremben"
                ], 0, ["c1-participle-proportionality-test"])
            ]
        },
        {
            "num": 3,
            "stem": "c1-32-03",
            "title": "Human Dignity as the Absolute Mother Right",
            "grammar_title": "Modal Adverbials Asserting Human Dignity as an Absolute Mother Right",
            "grammar_skill": "c1-adv-human-dignity-absoluteness",
            "goals": [
                "I can formulate the jurisprudence of human dignity as an inviolable, absolute foundational right (*emberi méltóság, anyajog, elidegeníthetetlen és oszthatatlan érték, halálbüntetés eltörlése*).",
                "I can deploy assertive modal adverbials establishing non-derogable constitutional principles (*érinthetetlenül fennállva, abszolút módon kizárva, ontológiailag megalapozva, feltétlenül védve*).",
                "I can discuss the landmark 23/1990. AB decision abolishing capital punishment in professional juristic terms."
            ],
            "vocab": [
                {"lemma": "emberi méltóság", "translation": "human dignity", "pos": "expression"},
                {"lemma": "anyajog", "translation": "mother right / foundational right", "pos": "noun"},
                {"lemma": "oszthatatlan", "translation": "indivisible", "pos": "adjective"},
                {"lemma": "elidegeníthetetlen", "translation": "inalienable", "pos": "adjective"},
                {"lemma": "abszolút jog", "translation": "absolute right / non-derogable right", "pos": "expression"},
                {"lemma": "önrendelkezési jog", "translation": "right to self-determination", "pos": "expression"},
                {"lemma": "halálbüntetés eltörlése", "translation": "abolition of capital punishment", "pos": "expression"},
                {"lemma": "személyiségi jog", "translation": "personality right", "pos": "expression"}
            ],
            "gr_text1": "Modal adverbials of absolute constitutional assertion establish rights that admit of no legislative balancing or limitation: `abszolút módon kizárva` (excluding in an absolute manner), `érinthetetlenül fennállva` (standing inviolably), `ontológiailag megalapozottan` (ontologically grounded), `kivétel nélkül érvényesülve` (prevailing without exception).",
            "gr_text2": "Example: `Az emberi méltóság mint anyajog abszolút módon kizárja, hogy az állam az élet elvételével szankcionáljon bármely bűncselekményt`.",
            "gr_table": [
                ["Az emberi méltóság érinthetetlenül fennállva minden más alapjog forrása.", "Standing inviolably human dignity is the source of all other fundamental rights."],
                ["A bíróság abszolút módon kizárta az emberi élet mérlegelésének lehetőségét.", "The court excluded in an absolute manner the possibility of balancing human life."],
                ["Az önrendelkezési jog ontológiailag megalapozva illeti meg a személyt.", "Ontologically grounded the right to self-determination belongs to the individual."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Miért nevezte Sólyom László az emberi méltóságot 'anyajognak'?", [
                    "Mert olyan oszthatatlan és elidegeníthetetlen alapérték, amelyből minden nevesített szabadságjog és személyiségi jog levezethető, és amely soha nem korlátozható.",
                    "Mert csak családos anyák vehetik igénybe az Alkotmánybíróság előtt.",
                    "Mert kizárólag a gyermekvédelmi törvények szövegében szerepel."
                ], 0, ["c1-32-vocab"]),
                fb("grammar", "controlled", "A testület az élethez való jogot abszolút _____ kizárta a mérlegelhető jogok köréből. (manner / módon)", "módon", "The body excluded the right to life from balanced rights in an absolute manner.", ["c1-adv-human-dignity-absoluteness"]),
                match("vocabulary", "controlled", [
                    ["emberi méltóság", "az emberi személyiség abszolút, sérthetetlen lényege"],
                    ["anyajog", "olyan gyökérjog, amelyből az összes többi szabadságjog sarjad"],
                    ["elidegeníthetetlen", "át nem ruházható és meg nem vonható természetes jog"],
                    ["halálbüntetés eltörlése", "a 23/1990. AB határozat történelmi döntése a méltóság védelmében"]
                ], ["c1-32-vocab"]),
                fb("grammar", "practice", "Az emberi méltóság érinthetetlenül _____ az állami hatalom abszolút korlátját jelenti. (standing / fennállva)", "fennállva", "Standing inviolably human dignity represents the absolute limit of state power.", ["c1-adv-human-dignity-absoluteness"]),
                sb("grammar", "practice", ["Az", "emberi", "méltóság", "érinthetetlenül", "minden", "alapjog", "abszolút", "forrása."], ["Az", "emberi", "méltóság", "érinthetetlenül", "minden", "alapjog", "abszolút", "forrása."], "Human dignity is inviolably the absolute source of all fundamental rights.", ["c1-adv-human-dignity-absoluteness"]),
                dc("dialogue", [
                    {"speaker": "Büntetőjogász", "text": "Hogyan indokolta Sólyom László a halálbüntetés feltétlen eltörlését?"},
                    {"speaker": "Alkotmánybíró", "text": "Úgy, hogy az emberi élet és a méltóság elválaszthatatlan egységet képez, amelyet az állam _____ sem vehet el."},
                    {"speaker": "Büntetőjogász", "text": "Az ember soha nem válhat puszta büntetőjogi eszközzé."}
                ], ["semmilyen indokkal", "könnyedén", "gyorsan"], 0, ["c1-adv-human-dignity-absoluteness"]),
                sw("production", [{"prompt": "Write a philosophical assertion of human dignity using a modal adverbial.", "answer": "Az emberi méltóság mint oszthatatlan anyajog abszolút módon kizárja az egyén eszközzé silányítását, érinthetetlenül fennállva a demokratikus jogrend legvégső fundamentumaként."}], ["c1-adv-human-dignity-absoluteness"]),
                mc("grammar", "check", "Melyik kifejezés rögzíti az emberi méltóság abszolút jellegét a leghatározottabban?", [
                    "abszolút módon kizárva / érinthetetlenül fennállva / ontológiailag megalapozva",
                    "többnyire tiszteletben tartva ha lehetséges",
                    "a parlament által néha módosítva"
                ], 0, ["c1-adv-human-dignity-absoluteness"])
            ]
        },
        {
            "num": 4,
            "stem": "c1-32-04",
            "title": "Ratio Decidendi & Constitutional Precedent",
            "grammar_title": "Complex Causal Connectives Deducing Ratio Decidendi in Constitutional Jurisprudence",
            "grammar_skill": "c1-causal-constitutional-precedent-ratio",
            "goals": [
                "I can analyze the binding ratio decidendi of constitutional court decisions, concurring and dissenting opinions (*rendelkező rész, indokolási kötelezettség, párhuzamos indokolás, különvélemény*).",
                "I can deploy complex causal connectives deducing constitutional principles (*abból a nóvumból kiindulva, lévén hogy az értelmezés köti a jogalkotót, annak következtében hogy a precedens megszilárdult*).",
                "I can critique shifts in constitutional case law and the prohibition of retroactive legislation."
            ],
            "vocab": [
                {"lemma": "precedens", "translation": "judicial precedent", "pos": "noun"},
                {"lemma": "indokolás", "translation": "judicial reasoning / justification", "pos": "noun"},
                {"lemma": "rendelkező rész", "translation": "holding / operative part of the decision", "pos": "expression"},
                {"lemma": "jogértelmezési gyakorlat", "translation": "jurisprudence / interpretive practice", "pos": "expression"},
                {"lemma": "párhuzamos indokolás", "translation": "concurring opinion", "pos": "expression"},
                {"lemma": "különvélemény", "translation": "dissenting opinion", "pos": "noun"},
                {"lemma": "jogorvoslathoz való jog", "translation": "right to an effective remedy", "pos": "expression"},
                {"lemma": "visszaható hatály tilalma", "translation": "prohibition of retroactive legislation", "pos": "expression"}
            ],
            "gr_text1": "Complex causal connectives in judicial discourse deduce normative consequences from precedent and constitutional principles: `abból a fundamentumból kiindulva, hogy...` (proceeding from the foundation that...), `lévén hogy a döntés indokolása köti a jogalkalmazót` (inasmuch as the rationale of the decision binds the adjudicator), `annak következtében, hogy a precedensjog organikus egységet képez` (as a consequence of precedent forming an organic unity).",
            "gr_text2": "Example: `A testület, abból a fundamentumból kiindulva, hogy a visszaható hatályú jogalkotás sérti a jogbiztonságot, megsemmisítette a büntető rendelkezést`.",
            "gr_table": [
                ["A testület abból kiindulva döntött, hogy a jogorvoslathoz való jog sérelmet szenvedett.", "The body decided proceeding from the fact that the right to an effective remedy was infringed."],
                ["Lévén hogy a precedens rögzült, az ítélkezési gyakorlat egységessé vált.", "Inasmuch as the precedent solidified the judicial practice became unified."],
                ["Annak következtében semmis a rendelkezés, hogy visszaható hatállyal állapított meg kötelezettséget.", "As a consequence the provision is void because it established an obligation retroactively."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mi a különbség a párhuzamos indokolás és a különvélemény között az Alkotmánybíróságon?", [
                    "A párhuzamos indokolást író bíró egyetért a rendelkező résszel de más indokokkal támasztja alá, míg a különvéleményt megfogalmazó bíró a döntés lényegével és eredményével sem ért egyet.",
                    "A különvéleményt a parlament elnöke írja, a párhuzamos indokolást a miniszterelnök.",
                    "Nincs különbség, mindkettő titkos bírósági feljegyzés."
                ], 0, ["c1-32-vocab"]),
                fb("grammar", "controlled", "A bírák abból a fundamentumból _____ ki, hogy a visszaható hatály tilalma kógens norma. (starting / indultak)", "indultak", "The judges proceeded from the foundation that the prohibition of retroactivity is a mandatory norm.", ["c1-causal-constitutional-precedent-ratio"]),
                match("vocabulary", "controlled", [
                    ["rendelkező rész", "a bírósági határozat kötelező erejű döntése és jogkövetkezménye"],
                    ["párhuzamos indokolás", "egyetértés a döntéssel, eltérő elvi levezetéssel kiegészítve"],
                    ["különvélemény", "a kisebbségben maradt bíró ellenvéleménye a döntés egészével szemben"],
                    ["visszaható hatály tilalma", "törvény nem büntethet olyan cselekményt, amely elkövetésekor nem volt bűn"]
                ], ["c1-32-vocab"]),
                fb("grammar", "practice", "_____ hogy a jogértelmezési gyakorlat köti a bíróságokat, a precedens megdönthetetlen. (inasmuch as / lévén)", "Lévén", "Inasmuch as the interpretive practice binds courts, the precedent is unshakeable.", ["c1-causal-constitutional-precedent-ratio"]),
                sb("grammar", "practice", ["A", "különvélemény", "annak", "következtében", "született,", "hogy", "sérült", "a", "jogbiztonság."], ["A", "különvélemény", "annak", "következtében", "született,", "hogy", "sérült", "a", "jogbiztonság."], "The dissenting opinion was born as a consequence of legal certainty being violated.", ["c1-causal-constitutional-precedent-ratio"]),
                dc("dialogue", [
                    {"speaker": "Kutató", "text": "Miért van óriási súlya az Alkotmánybíróság határozatai indokolásának?"},
                    {"speaker": "Professzor", "text": "Mert abból a tényből kiindulva, hogy a ratio decidendi köti a bírói kart, az indokolás szabja meg a jövőbeli _____."},
                    {"speaker": "Kutató", "text": "Így válik a bíróság a jogrendszer élő őrévé."}
                ], ["joggyakorlatot", "költségvetést", "választást"], 0, ["c1-causal-constitutional-precedent-ratio"]),
                sw("production", [{"prompt": "Write a judicial sentence deducing precedent using a complex causal connective.", "answer": "A testület, abból a fundamentumból kiindulva, hogy a visszaható hatály tilalma a jogállamiság elválaszthatatlan eleme, annak következtében semmisítette meg a passzust, hogy az sértette a szerzett jogokat."}], ["c1-causal-constitutional-precedent-ratio"]),
                mc("grammar", "check", "Melyik kötőszói szerkezet fejez ki logikai oksági következtetést az ítélkezésben?", [
                    "abból a fundamentumból kiindulva, hogy... / lévén hogy... / annak következtében, hogy...",
                    "amikor a bíró belép az ajtón és leül",
                    "ha esetleg valakinek ideje engedi"
                ], 0, ["c1-causal-constitutional-precedent-ratio"])
            ]
        },
        {
            "num": 5,
            "stem": "c1-32-05",
            "title": "Sólyom László: The Invisible Constitution & Human Dignity",
            "grammar_title": "Hypothetical and Deductive Syntax Structuring the Invisible Constitution Doctrine",
            "grammar_skill": "c1-syntax-invisible-constitution-doctrine",
            "goals": [
                "I can analyze the theoretical concept of the 'Invisible Constitution' (*láthatatlan alkotmány, alkotmányos koherencia, értékrendszer, bírói aktivizmus*).",
                "I can construct elevated hypothetical and deductive syntax structuring jurisprudential coherence (*amennyiben az alkotmány szövege csupán keretet nyújt, úgy a bírói gyakorlat hivatott kibontani annak rejtett értéktartalmát*).",
                "I can interpret Sólyom László's doctrine of constitutional continuity and institutional value order."
            ],
            "vocab": [
                {"lemma": "láthatatlan alkotmány", "translation": "invisible constitution doctrine", "pos": "expression"},
                {"lemma": "jogállamisági klauzula", "translation": "rule of law clause", "pos": "expression"},
                {"lemma": "alkotmányos koherencia", "translation": "constitutional coherence", "pos": "expression"},
                {"lemma": "intézményvédelem", "translation": "institutional protection obligation", "pos": "noun"},
                {"lemma": "értékrendszer", "translation": "system of constitutional values", "pos": "noun"},
                {"lemma": "bírói aktivizmus", "translation": "judicial activism", "pos": "expression"},
                {"lemma": "alkotmányos identitás", "translation": "constitutional identity", "pos": "expression"},
                {"lemma": "alkotmányos konszenzus", "translation": "constitutional consensus", "pos": "expression"}
            ],
            "gr_text1": "Hypothetical and deductive syntax in constitutional theory articulates how written constitutional provisions relate to deeper moral principles: `amennyiben az Alkotmány betűje nem ad kifejezett választ, akként a láthatatlan alkotmány szerves elvei nyújtanak zsinórmértéket` (insofar as the letter of the Constitution provides no explicit answer, so the organic principles of the invisible constitution provide the yardstick), `hacsak a bírói gyakorlat nem biztosítja a koherenciát, a jogállam puszta formasággá silányul` (unless judicial jurisprudence ensures coherence, the rule of law degenerates into mere formality).",
            "gr_text2": "Example: `Amennyiben az Alkotmánybíróság nem őrzi meg a normatív egységet, úgy az alkotmányos koherencia elkerülhetetlenül felbomlik`.",
            "gr_table": [
                ["Amennyiben az írott szöveg szűkszavú, úgy a jogelvek koherenciája válik irányadóvá.", "Insofar as the written text is concise so the coherence of legal principles becomes authoritative."],
                ["Hacsak a bírói kar nem védi az alapjogokat, a jogállam alapjai meginognak.", "Unless the judiciary defends fundamental rights the foundations of the rule of law will shake."],
                ["Mivel az alkotmányosság értékrend, a bíróság hivatott annak láthatatlan szövetét kibontani.", "Since constitutionality is a value system the court is called to unfold its invisible fabric."]
            ],
            "classic_story": {
                "slug": "solyom-lathatatlan-alkotmany",
                "title": "Sólyom László: A láthatatlan alkotmány és a méltóság védelme",
                "author": "Sólyom László",
                "work": "Válogatott alkotmánybírósági határozatok és esszék (1990–1998)",
                "summary": "Sólyom László (1942–2023) jogtudós, az Alkotmánybíróság első elnöke (1990–1998), majd a Magyar Köztársaság elnöke (2005–2010) volt, a rendszerváltás utáni magyar jogállamiság legmeghatározóbb teoretikusa. Doktrínája szerint az írott Alkotmány mögött egy elvi, erkölcsi és jogelméleti koherenciát megtestesítő 'láthatatlan alkotmány' áll, amely állandó mércét ad az alapjogok értelmezéséhez. A halálbüntetést eltörlő történelmi határozatában az emberi méltóságot elidegeníthetetlen, abszolút anyajogként definiálta.",
                "characters": ["Sólyom László, az Alkotmánybíróság elnöke", "Alkotmánybírák"],
                "paragraphs": [
                    {"type": "narration", "text": "Az 1989–90-es békés rendszerváltás során felállított Alkotmánybíróság példátlan történelmi feladattal szembesült: a diktatúra romjain, az ezer sebből vérző, toldozott-foldozott Alkotmány szövegéből kellett felépítenie egy stabil, modern európai jogállamot."},
                    {"type": "dialogue", "speaker": "Sólyom László", "text": "Az Alkotmánybíróságnak munkájában folytatnia kell elvi jelentőségű határozataival a 'láthatatlan alkotmány' megfogalmazását: azt a fogalmi hálózatot és szilárd jogelméleti koherenciát, amely az Alkotmány mögött állva megvédi a jogállamiságot a pillanatnyi politikai többségek önkényétől."},
                    {"type": "narration", "text": "A sólyomi doktrína középpontjában az emberi méltóság állt, amelyet a testület abszolút, oszthatatlan 'anyajognak' nyilvánított. A 23/1990. AB határozat, amely eltörölte a halálbüntetést, kimondta: az élet és a méltóság korlátozhatatlan egység, amellyel szemben az állam semmilyen büntetőjogi céllal nem léphet fel."},
                    {"type": "narration", "text": "Sólyom László szellemi hagyatéka bizonyította: a jogállam nem puszta formaságok összessége, hanem a hatalom korlátozottságának és az emberi szabadság feltétlen tiszteletének megbonthatatlan erkölcsi rendszere."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Mit értett Sólyom László a 'láthatatlan alkotmány' fogalma alatt?", [
                    "Az írott Alkotmány mögött húzódó, a bíróság által kibontott koherens jogelvek, alapjogi mércék és erkölcsi értékek szerves rendszerét, amely állandóságot biztosít a politikai hullámverésekkel szemben.",
                    "Egy titkos törvénykönyvet, amelyet kizárólag a bírák olvashatnak el zárt ajtók mögött.",
                    "A parlament épületének láthatatlan tervrajzait."
                ], 0, ["c1-32-vocab"]),
                fb("grammar", "controlled", "Amennyiben a jogalkotó korlátozza az autonómiát, _____ az intézményvédelem elve kötelezi a bíróságot a beavatkozásra. (so / úgy)", "úgy", "Insofar as the legislature restricts autonomy, so the principle of institutional protection obliges the court to intervene.", ["c1-syntax-invisible-constitution-doctrine"]),
                match("vocabulary", "controlled", [
                    ["láthatatlan alkotmány", "az írott alaptörvény mögötti elvi, erkölcsi koherencia rendszere"],
                    ["alkotmányos koherencia", "a jogrendszer belső logikai és elvi ellentmondásmentessége"],
                    ["intézményvédelem", "az alapjogok érvényesülését biztosító szervezeti garanciák fenntartása"],
                    ["bírói aktivizmus", "a bíróság bátor szerepvállalása az alapjogok kibontásában"]
                ], ["c1-32-vocab"]),
                fb("grammar", "practice", "Hacsak a bírói kar nem védi az alapelveket, a jogállamiság puszta _____ válik. (formality / formasággá)", "formasággá", "Unless the judiciary defends foundational principles, the rule of law turns into mere formality.", ["c1-syntax-invisible-constitution-doctrine"]),
                sb("grammar", "practice", ["Amennyiben", "a", "jogállamisági", "klauzula", "érvényesül,", "úgy", "biztosított", "az", "alkotmányos", "koherencia."], ["Amennyiben", "a", "jogállamisági", "klauzula", "érvényesül,", "úgy", "biztosított", "az", "alkotmányos", "koherencia."], "Insofar as the rule of law clause prevails, so constitutional coherence is ensured.", ["c1-syntax-invisible-constitution-doctrine"]),
                dc("dialogue", [
                    {"speaker": "Egyetemi hallgató", "text": "Hogyan óvhatja meg a bíróság a demokráciát a populista jogalkotástól?"},
                    {"speaker": "Sólyom László", "text": "Amennyiben a bírák hűek maradnak a láthatatlan alkotmány elveihez, úgy az alapjogok bástyái _____ fognak állni."},
                    {"speaker": "Egyetemi hallgató", "text": "Ez a joguralom legmélyebb garanciája."}
                ], ["rendületlenül", "ideiglenesen", "bizonytalanul"], 0, ["c1-syntax-invisible-constitution-doctrine"]),
                sw("production", [{"prompt": "Write a deductive sentence explaining the invisible constitution doctrine.", "answer": "Amennyiben az alkotmány szövege nem meríti ki a szabadságjogok teljes mélységét, úgy a bíróságnak a láthatatlan alkotmány szerves koherenciájára támaszkodva kell megőriznie a jogállamiság szubsztanciáját."}], ["c1-syntax-invisible-constitution-doctrine"]),
                mc("grammar", "check", "Melyik mondatszerkezet valósítja meg a hipotetikus-deduktív alkotmányelméleti érvelést?", [
                    "amennyiben a jogalkotó mellőzi a garanciákat, úgy a láthatatlan alkotmány mércéi lépnek elő védőbástyaként",
                    "mivel dél van, az Alkotmánybíróság ebédszünetet tart",
                    "ha a bíró fáradt, akkor hazamegy pihenni"
                ], 0, ["c1-syntax-invisible-constitution-doctrine"])
            ]
        }
    ]

    for l in core_lessons:
        emit_instructional_lesson(32, "core", l, core_title, core_intro if l["num"] == 1 else None)

    # Core Consolidation Lesson
    emit_consolidation_lesson(
        32,
        "core",
        "c1-32-consolidation",
        core_title,
        [
            "I can master the academic vocabulary of constitutional review, abstract norm control, and legal certainty.",
            "I can employ participial proportionality constructions, modal adverbials of human dignity, and causal precedent connectives.",
            "I can analyze and formulate the jurisprudence of the 'Invisible Constitution' and fundamental rights hierarchy."
        ],
        [
            mc("grammar", "recognize", "Melyik határozói szerkezet vizsgálja a legpontosabban a jogszabályok alaptörvény-ellenességét?", [
                "alkotmányjogi szempontból vizsgálva / anyagi jogi alapon eljárva",
                "szavazás után gyorsan döntve a plenáris ülésen",
                "újságcikkeket átfutva a könyvtárszobában"
            ], 0, ["c1-adv-constitutional-norm-control"]),
            mc("grammar", "recognize", "Milyen szerkezettel fejezhetjük ki az alapjogok arányossági mérlegelését a leghitelesebben?", [
                "a versengő alapjogokat mérlegre téve és a legenyhébb eszköz elvét érvényesítve",
                "amikor a törvényeket gyorsan elfogadják",
                "ha a képviselők nem veszekednek egymással"
            ], 0, ["c1-participle-proportionality-test"]),
            match("vocabulary", "recognize", [
                ["alkotmányossági normakontroll", "a jogszabályok alaptörvénnyel való összhangjának felülvizsgálata"],
                ["arányossági teszt", "az alapjog-korlátozás szükségességét ellenőrző mérce"],
                ["emberi méltóság", "minden más szabadságjog abszolút, oszthatatlan forrása"],
                ["láthatatlan alkotmány", "az írott alaptörvény mögötti szerves erkölcsi-jogi rend"]
            ], ["c1-32-vocab"]),
            fb("vocabulary", "recall", "Az emberi méltóság mint _____ nem korlátozható semmilyen állami érdek nevében. (mother right / anyajog)", "anyajog", "Human dignity as a mother right cannot be restricted in the name of any state interest.", ["c1-32-vocab"]),
            fb("vocabulary", "recall", "A bíróság döntése a rendelkező részből és a jogi indokokat tartalmazó _____ áll. (reasoning / indokolásból)", "indokolásból", "The court's decision consists of the operative holding and the judicial reasoning.", ["c1-32-vocab"]),
            fb("grammar", "recall", "A vitatott passzust alkotmányjogi szempontból _____ semmisnek nyilvánították. (examining / vizsgálva)", "vizsgálva", "Examining the contested clause from a constitutional perspective they declared it void.", ["c1-adv-constitutional-norm-control"]),
            fb("grammar", "context", "Az élethez való jogot abszolút _____ védelmezi az Alkotmánybíróság precedense. (manner / módon)", "módon", "The precedent of the Constitutional Court protects the right to life in an absolute manner.", ["c1-adv-human-dignity-absoluteness"]),
            fb("grammar", "context", "Amennyiben a jogállamiság csorbul, _____ a láthatatlan alkotmány nyújt eligazodást. (so / úgy)", "úgy", "Insofar as the rule of law is damaged, so the invisible constitution provides orientation.", ["c1-syntax-invisible-constitution-doctrine"]),
            mc("grammar", "context", "Miért tekinti Sólyom László a láthatatlan alkotmányt a jogrend végső garanciájának?", [
                "Mert a bírói jogértelmezés által kibontott koherens értékrend megvédi az alapjogokat a múló politikai szeszélyektől és az önkénytől.",
                "Mert a láthatatlan dolgokat nem lehet megrongálni semmilyen fegyverrel.",
                "Mert a törvényhozás nem olvashatja a határozatokat."
            ], 0, ["c1-syntax-invisible-constitution-doctrine"]),
            sb("grammar", "produce", ["Az", "emberi", "méltóság", "minden", "alapjog", "abszolút", "és", "oszthatatlan", "fundamentuma."], ["Az", "emberi", "méltóság", "minden", "alapjog", "abszolút", "és", "oszthatatlan", "fundamentuma."], "Human dignity is the absolute and indivisible foundation of all fundamental rights.", ["c1-adv-human-dignity-absoluteness"]),
            sw("production", [{"prompt": "Write a synthesis of constitutional rights proportionality using a participial construction.", "answer": "A bíróság az egymással kollízióba kerülő alapjogokat mérlegre téve, a szükségesség és arányosság elvét szem előtt tartva semmisítette meg a polgárok szabadságát önkényesen csorbító jogszabályt."}], ["c1-participle-proportionality-test"]),
            sw("production", [{"prompt": "Synthesize the invisible constitution doctrine using hypothetical and deductive syntax.", "answer": "Amennyiben az írott alaptörvény keretjellegű normái nem adnak közvetlen eligazítást, úgy a láthatatlan alkotmány erkölcsi koherenciája kötelezi a testületet a szabadságjogok abszolút védelmére."}], ["c1-syntax-invisible-constitution-doctrine"])
        ]
    )

    # ----------------------------------------------------
    # TRACK 2: DISCOURSE (c1-jogallamisag)
    # ----------------------------------------------------
    disc_intro = [
        "The post-2010 constitutional revolution in Hungary initiated a systematic dismantlement of independent judicial oversight, subordinating courts to central administrative power and provoking unprecedented domestic and European rule of law confrontations.",
        "In this unit, following the critical saga of the forced retirement of senior judges, the centralized autocracy of the National Office for the Judiciary (OBH), the brave resistance of the National Judicial Council (OBT), and the EU Article 7 rule-of-law procedures, you will master the analytical discourse of institutional capture, judicial independence, and supranational constitutional sanctions at the C1 level."
    ]

    disc_lessons = [
        {
            "num": 1,
            "stem": f"c1-{slug}-01",
            "title": "The Purge & Forced Retirement of Senior Judges",
            "grammar_title": "Discourse Markers Diagnosing Political Subjugation of the Independent Judiciary",
            "grammar_skill": "c1-discourse-judicial-subjugation-framing",
            "goals": [
                "I can analyze the political purge and forced retirement of senior Hungarian judges in 2011/2012 (*kényszernyugdíjazás, bírói függetlenség csorbítása, elmozdíthatatlanság elve, életkori diszkrimináció*).",
                "I can deploy analytical discourse markers diagnosing judicial capture (*intézményi szintre emelt politikai beavatkozásként értékelve, a hatalmi ágak elválasztásának durva felrúgásaként aposztrofálva, a bírói kar gerincének megtörését célozva*).",
                "I can critique the European Court of Justice ruling on judicial independence."
            ],
            "vocab": [
                {"lemma": "kényszernyugdíjazás", "translation": "forced retirement of judges", "pos": "noun"},
                {"lemma": "bírói függetlenség", "translation": "judicial independence", "pos": "expression"},
                {"lemma": "elmozdíthatatlanság elve", "translation": "principle of irremovability of judges", "pos": "expression"},
                {"lemma": "politikai tisztogatás", "translation": "political purge", "pos": "expression"},
                {"lemma": "Európai Bíróság", "translation": "Court of Justice of the European Union (CJEU)", "pos": "expression"},
                {"lemma": "életkori diszkrimináció", "translation": "age discrimination", "pos": "expression"},
                {"lemma": "jogállami visszalépés", "translation": "rule of law backsliding", "pos": "expression"},
                {"lemma": "hatalmi ágak elválasztása", "translation": "separation of powers", "pos": "expression"}
            ],
            "gr_text1": "Discourse markers of judicial capture diagnose the systemic political subordination of courts: `intézményi szintű politikai beavatkozásként értékelve` (evaluated as institutional-level political intervention), `a hatalmi ágak elválasztásának felrúgásaként aposztrofálva` (characterized as a breach of the separation of powers), `a bírói elmozdíthatatlanság sarokkövét célba véve` (targeting the cornerstone of judicial irremovability).",
            "gr_text2": "Example: `A bírák hirtelen kényszernyugdíjazását az Európai Bíróság életkori diszkriminációként elítélve kimondta a bírói függetlenség sérelmét`.",
            "gr_table": [
                ["A kormány intézkedését politikai tisztogatásként értékelve bírálták a nemzetközi szervezetek.", "Evaluating the government's measure as a political purge international organizations criticized it."],
                ["A bírói elmozdíthatatlanság garanciáját célba véve több száz tapasztalt bírót küldtek el.", "Targeting the guarantee of judicial irremovability several hundred experienced judges were dismissed."],
                ["Az Európai Bíróság a jogállami normák megsértéseként aposztrofálta a nyugdíjazási reformot.", "The European Court characterized the pension reform as an infringement of rule of law norms."]
            ],
            "world_story_seg": {
                "seg_slug": f"c1-{slug}-01-biroi-fuggetlenseg-felszamolasa",
                "title": "A kényszernyugdíjazás és a bírói autonómia megroppantása",
                "summary": "2011 végén a kétharmados többség egyik napról a másikra 70-ről 62 évre csökkentette a bírák nyugdíjkorhatárát, lefejezve a bíróságok vezetését. Az Európai Bíróság elítélte a lépést, de a bírói autonómia súlyos sebeket kapott.",
                "paragraphs": [
                    {"type": "narration", "text": "2011 decemberében döbbenet ülte meg a magyar bíróságok folyosóit: az új Alaptörvény átmeneti rendelkezései nyomán a bírák kötelező nyugdíjkorhatárát egyik napról a másikra 70 évről 62 évre szállították le. Ez nem egyszerű adminisztratív módosítás volt, hanem tervezett intézményi tisztogatás, amelynek célpontjában a bírósági hierarchia csúcsán ülő, autonóm tanácselnökök és bírósági vezetők álltak."},
                    {"type": "dialogue", "speaker": "Kovács bíró", "text": "A bírói elmozdíthatatlanság elvét, amely a független ítélkezés legfőbb európai garanciája, egyetlen tollvonással söpörték félre. Intézményi szintű politikai beavatkozásként értékelve a lépést nyilvánvaló, hogy a bíróságok függetlenségének gerincét akarták megtörni."},
                    {"type": "narration", "text": "Több mint kétszázhetven tekintélyes bírót mozdítottak el állásából néhány hét leforgása alatt. Az Európai Bizottság kötelezettségszegési eljárást indított, és a luxembourgi Európai Bíróság megsemmisítő ítéletben mondta ki: a drasztikus korhatárcsökkentés jogellenes életkori diszkriminációt valósított meg."},
                    {"type": "narration", "text": "Bár a döntés jogilag elmarasztalta a hatalmat, az elmozdított elnökök székeit addigra már lojális káderek töltötték be. A bírói autonómia évtizedes intézményi védőhálója megroppant."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Miért jelentett súlyos jogállami jogsértést a bírák kötelező nyugdíjkorhatárának 62 évre szállítása 2011-ben?", [
                    "Mert célzottan lefejezte a bíróságok független vezetését, megsértve a bírói elmozdíthatatlanság alapelvét és az uniós antidiszkriminációs jogot.",
                    "Mert túl drága volt a bírák nyugdíjának kifizetése az államkincstárnak.",
                    "Mert a fiatalabb bírák nem akartak tárgyalni."
                ], 0, [f"c1-{slug}-vocab"]),
                fb("grammar", "controlled", "A lépést politikai beavatkozásként _____ a luxembourgi bíróság elmarasztalta a tagállamot. (evaluating / értékelve)", "értékelve", "Evaluating the step as a political intervention the Luxembourg court condemned the member state.", ["c1-discourse-judicial-subjugation-framing"]),
                match("vocabulary", "controlled", [
                    ["kényszernyugdíjazás", "a bírói kar felső vezetésének drasztikus, azonnali eltávolítása"],
                    ["bírói függetlenség", "a bíró mentes minden külső politikai és hivatali utasítástól"],
                    ["elmozdíthatatlanság elve", "a bíró törvényes mandátuma nem vonható vissza önkényesen"],
                    ["hatalmi ágak elválasztása", "a bírói, törvényhozói és végrehajtói hatalom szigorú autonómiája"]
                ], [f"c1-{slug}-vocab"]),
                fb("grammar", "practice", "A reformot a jogállami normák felrúgásaként _____ ítélte el a szakma. (characterizing / aposztrofálva)", "aposztrofálva", "Characterizing the reform as an overthrow of rule of law norms the profession condemned it.", ["c1-discourse-judicial-subjugation-framing"]),
                sb("grammar", "practice", ["A", "kényszernyugdíjazás", "durván", "sértette", "a", "bírói", "függetlenség", "elvét."], ["A", "kényszernyugdíjazás", "durván", "sértette", "a", "bírói", "függetlenség", "elvét."], "Forced retirement severely violated the principle of judicial independence.", ["c1-discourse-judicial-subjugation-framing"]),
                dc("dialogue", [
                    {"speaker": "Újságíró", "text": "Hogyan értékelték az európai intézmények a magyar bírói reformot?"},
                    {"speaker": "Uniós jogász", "text": "Intézményi szintű politikai beavatkozásként _____ a bíróság kimondta a jogsértést."},
                    {"speaker": "Újságíró", "text": "De a bírósági pozíciókat addigra már átvették."}
                ], ["értékelve", "örülve", "felejtve"], 0, ["c1-discourse-judicial-subjugation-framing"]),
                sw("production", [{"prompt": "Write a critique of the judicial purge using a discourse framing marker.", "answer": "A tapasztalt bírák hirtelen kényszernyugdíjazását a hatalmi ágak elválasztásának durva felrúgásaként aposztrofálva az Európai Bíróság kimondta a bírói függetlenség súlyos és rendszerszintű sérelmét."}], ["c1-discourse-judicial-subjugation-framing"]),
                mc("grammar", "check", "Melyik kifejezés diagnosztizálja a bíróságok politikai alávetését a legpontosabban?", [
                    "intézményi szintű politikai beavatkozásként értékelve / a bírói függetlenség felrúgásaként aposztrofálva",
                    "amikor a bírák korán mennek haza a bíróságról",
                    "egy kedves törvénymódosítást elfogadva a teremben"
                ], 0, ["c1-discourse-judicial-subjugation-framing"])
            ]
        },
        {
            "num": 2,
            "stem": f"c1-{slug}-02",
            "title": "The Administrative Autocracy of the OBH",
            "grammar_title": "Critical Evaluative Adverbials Exposing Arbitrary Executive Administrative Monopoly over Courts",
            "grammar_skill": "c1-adv-institutional-monopolization-critique",
            "goals": [
                "I can analyze the centralization of court administration in the National Office for the Judiciary (OBH) (*hatalomkoncentráció, OBH-elnöki jogkörök, kinevezési monopólium, bírói önigazgatás elsorvasztása*).",
                "I can deploy critical evaluative adverbials exposing administrative autocracy (*önkényesen érvénytelenítve a pályázatokat, rendszerszinten centralizálva az igazgatást, átláthatatlan módon kirendelve lojális kádereket*).",
                "I can assess Handó Tünde's controversial court administration in constitutional critique register."
            ],
            "vocab": [
                {"lemma": "Országos Bírósági Hivatal", "translation": "National Office for the Judiciary (OBH)", "pos": "expression"},
                {"lemma": "hatalomkoncentráció", "translation": "concentration of administrative power", "pos": "noun"},
                {"lemma": "pályázat érvénytelenítése", "translation": "annulment of judicial appointment competitions", "pos": "expression"},
                {"lemma": "önkényes kinevezés", "translation": "arbitrary judicial appointment", "pos": "expression"},
                {"lemma": "fellebbviteli bíróság", "translation": "court of appeals", "pos": "expression"},
                {"lemma": "bírói önigazgatás", "translation": "judicial self-governance", "pos": "expression"},
                {"lemma": "hivatali visszaélés", "translation": "abuse of official power", "pos": "expression"},
                {"lemma": "kirendelés", "translation": "temporary judicial assignment / transfer", "pos": "noun"}
            ],
            "gr_text1": "Critical evaluative adverbials expose executive monopoly and arbitrary administration in judicial governance: `önkényesen érvénytelenítve a törvényes pályázatokat` (arbitrarily annulling lawful competitions), `rendszerszinten centralizálva a kinevezési jogköröket` (centralizing appointment powers at a systemic level), `átláthatatlan módon megkerülve a bírói testületeket` (bypassing judicial collegiate bodies in an untransparent manner).",
            "gr_text2": "Example: `Az OBH elnöke átláthatatlan módon eljárva és a bírói kollégiumok támogatását figyelmen kívül hagyva érvénytelenítette a nyertes pályázatokat`.",
            "gr_table": [
                ["Az igazgatás rendszerszinten centralizálva számolta fel a helyi bíróságok önállóságát.", "Centralizing court governance at a systemic level the administration abolished the autonomy of local courts."],
                ["Az elnök önkényesen érvénytelenítve a pályázatot saját emberét nevezte ki megbízott vezetőnek.", "Arbitrarily annulling the tender the president appointed their own associate as interim head."],
                ["Átláthatatlan módon kirendelve helyeztek át kényelmetlen ügyeket tárgyaló bírákat.", "Transferring in an untransparent manner judges hearing uncomfortable cases were reassigned."]
            ],
            "world_story_seg": {
                "seg_slug": f"c1-{slug}-02-obh-elnoki-hatalomkoncentracio",
                "title": "Az OBH monokratikus uralma és a pályázatok megsemmisítése",
                "summary": "Az Országos Bírósági Hivatal elnöki tisztségét Handó Tünde kapta meg, aki példátlan személyi hatalommal irányította az igazságszolgáltatást. Számtalan esetben érvénytelenítette a bírói testületek által rangsorolt elnöki pályázatokat.",
                "paragraphs": [
                    {"type": "narration", "text": "A 2012-ben létrehozott Országos Bírósági Hivatal (OBH) olyan centralizált igazgatási modellt valósított meg, amely Európa demokratikus országaiban teljességgel példátlan volt. Az intézmény élére kinevezett Handó Tünde egyszemélyi döntési jogkört kapott a bírósági vezetők kinevezése és az álláshelyek betöltése felett."},
                    {"type": "dialogue", "speaker": "Tanácselnök bíró", "text": "Amikor egy-egy ítélőtábla bírói közössége titkos szavazással, elsöprő többséggel támogatott egy független pályázót, az elnök egyszerűen 'eredménytelennek' nyilvánította a pályázatot minden érdemi indok nélkül. Önkényesen eljárva felülírta a bírói önigazgatás akaratát."},
                    {"type": "narration", "text": "Ezt követően az elnök egyéves időtartamra kirendelte saját bizalmasát a bíróság élére, megkerülve a törvényben előírt pályázati rendszert. Aki szót emelt a gyakorlat ellen, annak a szakmai előmenetele azonnal megfeneklett."},
                    {"type": "narration", "text": "A Velencei Bizottság jelentései nyomatékosan figyelmeztettek: az OBH elnökének monokratikus hatalma ellensúlyok nélkül működik, ami súlyosan rombolja a bíróságok pártatlanságát."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Hogyan éltek vissza az OBH kinevezési jogköreivel a bírói pályázatok során?", [
                    "A nyertes szakmai pályázatokat indokolás nélkül érvénytelenítették, és a bírói kar akarata ellenére lojális ideiglenes megbízottakat ültettek a bíróságok élére.",
                    "Minden bíró fizetését megháromszorozták anélkül hogy kérték volna.",
                    "Sorsolással választották ki a Kúria tagjait."
                ], 0, [f"c1-{slug}-vocab"]),
                fb("grammar", "controlled", "Az elnök átláthatatlan módon _____ érvénytelenítette a legmagasabb pontszámot kapott bíró pályázatát. (acting / eljárva)", "eljárva", "Acting in an untransparent manner the president annulled the application of the judge who received the highest score.", ["c1-adv-institutional-monopolization-critique"]),
                match("vocabulary", "controlled", [
                    ["Országos Bírósági Hivatal", "a bíróságok központi igazgatását ellátó intézmény"],
                    ["hatalomkoncentráció", "a döntési jogkörök egyetlen személy kezében való összpontosulása"],
                    ["pályázat érvénytelenítése", "a szakmai bírálat önkényes félresöprése indokolás nélkül"],
                    ["kirendelés", "bírák ideiglenes áthelyezése a vezetői posztok pályázat nélküli betöltésére"]
                ], [f"c1-{slug}-vocab"]),
                fb("grammar", "practice", "A kinevezéseket rendszerszinten _____ az igazgatás kizárta a kollegiális kontrollt. (centralizing / centralizálva)", "centralizálva", "Centralizing appointments at a systemic level the administration excluded collegial control.", ["c1-adv-institutional-monopolization-critique"]),
                sb("grammar", "practice", ["Az", "OBH", "elnöke", "önkényesen", "felszámolta", "a", "bírói", "önigazgatás", "garanciáit."], ["Az", "OBH", "elnöke", "önkényesen", "felszámolta", "a", "bírói", "önigazgatás", "garanciáit."], "The president of the OBH arbitrarily dismantled the guarantees of judicial self-governance.", ["c1-adv-institutional-monopolization-critique"]),
                dc("dialogue", [
                    {"speaker": "Bíró", "text": "Miért tiltakozott a bírói kar a pályázatok önkényes kezelése ellen?"},
                    {"speaker": "Kollégiumvezető", "text": "Mert az elnök átláthatatlan módon kirendelve a megbízottakat teljesen elsorvasztotta a bírósági _____."},
                    {"speaker": "Bíró", "text": "Ez a személyi függőség közvetlen megteremtése volt."}
                ], ["autonómiát", "épületet", "iratokat"], 0, ["c1-adv-institutional-monopolization-critique"]),
                sw("production", [{"prompt": "Write a critique of judicial centralization using an evaluative adverbial.", "answer": "Az OBH elnöke átláthatatlan módon eljárva és a törvényes pályázatokat önkényesen érvénytelenítve rendszerszinten centralizálta a kinevezési jogköröket a független bírói testületek rovására."}], ["c1-adv-institutional-monopolization-critique"]),
                mc("grammar", "check", "Melyik szerkezet leplezi le az igazgatási hatalomkoncentrációt a legpontosabban?", [
                    "önkényesen érvénytelenítve a pályázatokat / rendszerszinten centralizálva az igazgatást",
                    "új számítógépeket vásárolva a bírósági irodába",
                    "tárgyalási jegyzőkönyvet gépelve délután"
                ], 0, ["c1-adv-institutional-monopolization-critique"])
            ]
        },
        {
            "num": 3,
            "stem": f"c1-{slug}-03",
            "title": "The Resistance of the National Judicial Council",
            "grammar_title": "Deontic Modal Structures Asserting Constitutional Duty of Judicial Integrity",
            "grammar_skill": "c1-modal-deontic-judicial-integrity",
            "goals": [
                "I can analyze the institutional resistance of the National Judicial Council (OBT) against administrative autocracy (*Országos Bírói Tanács, törvénysértések megállapítása, etikai integritás, testületi fellépés*).",
                "I can formulate deontic modal structures asserting constitutional duty and ethical fortitude (*kötelessége ellenállni a politikai nyomásnak, elengedhetetlen a bírói eskü védelmezése, megalkuvást nem ismerve kell őrködni az autonómia felett*).",
                "I can critique authoritarian retaliation against outspoken judicial council members."
            ],
            "vocab": [
                {"lemma": "Országos Bírói Tanács", "translation": "National Judicial Council (OBT)", "pos": "expression"},
                {"lemma": "testületi ellenállás", "translation": "collective / institutional resistance", "pos": "expression"},
                {"lemma": "felügyeleti jogkör", "translation": "supervisory oversight power", "pos": "expression"},
                {"lemma": "bírói autonómia", "translation": "judicial autonomy", "pos": "expression"},
                {"lemma": "törvénysértés megállapítása", "translation": "finding of statutory illegality", "pos": "expression"},
                {"lemma": "integritásvédelem", "translation": "protection of judicial integrity", "pos": "noun"},
                {"lemma": "tisztségviselő", "translation": "elected judicial officer", "pos": "noun"},
                {"lemma": "nyílt szembeszegülés", "translation": "open confrontation / defiance", "pos": "expression"}
            ],
            "gr_text1": "Deontic modal structures articulate the uncompromising constitutional and moral duty of judges to resist political and administrative coercion: `a bírónak kötelessége hűnek maradnia az esküjéhez` (it is the duty of the judge to remain faithful to their oath), `elengedhetetlen a hatalmi visszaélések nyílt megállapítása` (the open finding of abuse of power is indispensable), `megalkuvást nem ismerve kell őrködni a bíróságok függetlensége felett` (one must watch over the independence of courts without compromise).",
            "gr_text2": "Example: `Az OBT tagjainak alkotmányos kötelessége volt nyíltan kimondani az OBH elnökének törvénysértéseit, még a kormányzati sajtóhadjárat kereszttüzében is`.",
            "gr_table": [
                ["A bírónak kötelessége ellenállnia minden pártpolitikai és hivatali nyomásnak.", "It is the duty of the judge to resist all party-political and official pressure."],
                ["Elengedhetetlen a bírói kar etikai integritásának megingathatatlan védelme.", "The unshakeable defense of the judicial corps' ethical integrity is indispensable."],
                ["A testületnek kötelessége volt megállapítani az igazgatási törvénysértéseket.", "It was the duty of the council to establish the administrative violations of law."]
            ],
            "world_story_seg": {
                "seg_slug": f"c1-{slug}-03-obt-intezmenyi-ellenallasa",
                "title": "A törvényesség őrei: Az OBT bátor helytállása",
                "summary": "Amikor az OBH elnöke túllépte hatásköreit, a bírák által választott Országos Bírói Tanács (OBT) példátlan bátorsággal lépett fel: sorozatos törvénysértéseket állapított meg, és kezdeményezte az elnök felmentését.",
                "paragraphs": [
                    {"type": "narration", "text": "2018 tavaszán a magyar igazságszolgáltatás legsúlyosabb belső alkotmányos válsága robbant ki. Az Országos Bírói Tanács (OBT) – a bírák által demokratikusan megválasztott felügyeleti testület – vizsgálatot indított a bírósági kinevezési gyakorlatok ügyében."},
                    {"type": "dialogue", "speaker": "OBT-tag bíró", "text": "Alkotmányos kötelességünk volt hűnek maradni az eskünkhöz és kimondani az igazságot: az OBH elnöke rendszeresen és súlyosan megsértette a törvényeket. Nem engedhetjük, hogy a bírói kar gerincét megtörjék."},
                    {"type": "narration", "text": "Az OBT részletes határozatok sorában állapította meg a törvénysértéseket, és kezdeményezte az elnök felmentését a parlament előtt. Válaszul a kormánymédia példátlan rágalomhadjáratot indított a tanács tagjai ellen, árulónak és külföldi ügynöknek bélyegezve őket."},
                    {"type": "narration", "text": "Az OBT tagjai azonban kitartottak. Hősies helytállásuk bizonyította, hogy a magyar bírói karban létezik egy szilárd mag, amely a legdurvább tekintélyelvű fenyegetések közepette is képes megvédeni a jogállamiság becsületét."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Milyen történelmi lépést tett az Országos Bírói Tanács (OBT) az OBH elnökével szemben?", [
                    "Hivatalosan megállapította az elnök sorozatos törvénysértéseit, és alkotmányos jogával élve kezdeményezte annak parlamenti felmentését.",
                    "Lemondott minden jogköréről és bezárta az irodáját.",
                    "Kérvényezte az igazságügyi minisztérium felügyeletének kiterjesztését."
                ], 0, [f"c1-{slug}-vocab"]),
                fb("grammar", "controlled", "A bírói kar képviselőinek alkotmányos _____ volt ellenállni a törvénytelen nyomásgyakorlásnak. (duty / kötelessége)", "kötelessége", "It was the constitutional duty of the representatives of the judiciary to resist unlawful pressure.", ["c1-modal-deontic-judicial-integrity"]),
                match("vocabulary", "controlled", [
                    ["Országos Bírói Tanács", "a bírák által választott független felügyeleti testület"],
                    ["testületi ellenállás", "a bírói közösség bátor kiállása az igazgatási önkénnyel szemben"],
                    ["felügyeleti jogkör", "a bírósági igazgatás törvényességét ellenőrző hatáskör"],
                    ["törvénysértés megállapítása", "a hivatali visszaélések hivatalos testületi elmarasztalása"]
                ], [f"c1-{slug}-vocab"]),
                fb("grammar", "practice", "Megalkuvást nem ismerve kell _____ az ítélkezés pártatlansága felett. (guard / őrködni)", "őrködni", "Without compromise one must watch over the impartiality of adjudication.", ["c1-modal-deontic-judicial-integrity"]),
                sb("grammar", "practice", ["A", "bíráknak", "kötelessége", "védeni", "a", "bírósági", "autonómia", "integritását."], ["A", "bíráknak", "kötelessége", "védeni", "a", "bírósági", "autonómia", "integritását."], "It is the duty of judges to defend the integrity of judicial autonomy.", ["c1-modal-deontic-judicial-integrity"]),
                dc("dialogue", [
                    {"speaker": "Joghallgató", "text": "Hogyan tudott ellenállni a maroknyi OBT-tag a hatalmas politikai ellenszélben?"},
                    {"speaker": "OBT-tag", "text": "Úgy, hogy felismertük: alkotmányos kötelességünk megalkuvást nem ismerve kiállni a bírói _____ mellett."},
                    {"speaker": "Joghallgató", "text": "Ez a történeti bátorság példája a jövő generációknak."}
                ], ["függetlenség", "fegyelem", "csend"], 0, ["c1-modal-deontic-judicial-integrity"]),
                sw("production", [{"prompt": "Write a sentence formulating the ethical duty of judicial integrity using a deontic modal.", "answer": "A független bírói kar tagjainak alkotmányos kötelessége ellenállni minden külső politikai beavatkozásnak, és megalkuvást nem ismerve kell őrködniük az ítélkezés pártatlansága és az emberi jogok védelme felett."}], ["c1-modal-deontic-judicial-integrity"]),
                mc("grammar", "check", "Melyik szerkezet fogalmazza meg a bírói hivatás deontikus követelményét a leghatározottabban?", [
                    "kötelessége ellenállni a nyomásnak / megalkuvást nem ismerve kell őrködni a függetlenség felett",
                    "talán érdemes lenne elolvasni a szabályzatot néha",
                    "a bíróknak szabadidejükben sétálniuk kell"
                ], 0, ["c1-modal-deontic-judicial-integrity"])
            ]
        },
        {
            "num": 4,
            "stem": f"c1-{slug}-04",
            "title": "Article 7 & European Sanction Mechanisms",
            "grammar_title": "Proportional Correlative Structures Linking Judicial Backsliding to European Union Sanctions",
            "grammar_skill": "c1-adv-proportional-eu-infringement-measures",
            "goals": [
                "I can analyze the EU Article 7 rule of law procedure and financial conditionality mechanism (*7-es cikkely szerinti eljárás, kohéziós források befagyasztása, szupranacionális kontroll, Sargentini-jelentés*).",
                "I can construct proportional correlative structures linking institutional backsliding to sanctions (*minél súlyosabb csorbát szenved a bíróságok függetlensége, annál szigorúbb pénzügyi szankciókat léptet életbe az Unió*).",
                "I can evaluate the international diplomatic consequences of systemic democratic regression."
            ],
            "vocab": [
                {"lemma": "7-es cikkely szerinti eljárás", "translation": "Article 7 TEU procedure", "pos": "expression"},
                {"lemma": "kötelezettségszegési eljárás", "translation": "infringement procedure", "pos": "expression"},
                {"lemma": "jogállamisági mechanizmus", "translation": "rule of law conditionality mechanism", "pos": "expression"},
                {"lemma": "kohéziós források befagyasztása", "translation": "freezing of cohesion funds", "pos": "expression"},
                {"lemma": "szupranacionális kontroll", "translation": "supranational oversight", "pos": "expression"},
                {"lemma": "Sargentini-jelentés", "translation": "Sargentini Report", "pos": "noun"},
                {"lemma": "szisztematikus kockázat", "translation": "systemic risk to EU values", "pos": "expression"},
                {"lemma": "szavazati jog felfüggesztése", "translation": "suspension of voting rights", "pos": "expression"}
            ],
            "gr_text1": "Proportional correlative structures link democratic degradation directly to international and financial countermeasures: `minél inkább elmélyül a jogállamisági válság, annál elkerülhetetlenebbé válik az uniós források zárolása` (the more the rule of law crisis deepens, the more inevitable becomes the freezing of EU funds), `amilyen mértékben sérül a bírói függetlenség, olyan mértékben vonja meg Európa a bizalmat` (to the extent that judicial independence is infringed, to that extent Europe withdraws trust).",
            "gr_text2": "Example: `Minél nyíltabban tagadja meg a tagállam a jogállami normák betartását, annál szigorúbb szupranacionális szankciókkal kell szembenéznie`.",
            "gr_table": [
                ["Minél durvább a bírói autonómia sérelme, annál súlyosabb pénzügyi következményekkel jár.", "The more severe the injury to judicial autonomy the graver financial consequences it brings."],
                ["Amilyen mértékben csorbul a jogbiztonság, olyan mértékben fagyasztják be a támogatásokat.", "To the extent legal certainty is impaired to that extent grants are frozen."],
                ["Minél tovább késik a reform, annál távolabbra kerül a szankciók feloldása.", "The longer reform is delayed the further away the lifting of sanctions gets."]
            ],
            "world_story_seg": {
                "seg_slug": f"c1-{slug}-04-eu-hetes-cikkely-szankciok",
                "title": "A Sargentini-jelentéstől a forrásbefagyasztásig",
                "summary": "A magyar jogállamiság szisztematikus leépítése kiváltotta az Európai Parlament 7-es cikkely szerinti eljárását. Az Unió végül a jogállamisági mechanizmussal milliárdos eurós kohéziós forrásokat zárolt.",
                "paragraphs": [
                    {"type": "narration", "text": "2018 szeptemberében történelmi szavazás zajlott az Európai Parlament plenáris ülésén: a képviselők kétharmados többséggel elfogadták a Judith Sargentini által jegyzett jelentést, megindítva az Unió alapszerződésének 7-es cikkelye szerinti eljárást Magyarországgal szemben."},
                    {"type": "dialogue", "speaker": "Európai parlamenti képviselő", "text": "A bíróságok függetlenségének rendszerszintű csorbítása és a korrupció intézményesülése közvetlen fenyegetést jelent az Európai Unió közös értékeire. Minél tovább halogatja a kormány a reformokat, annál szigorúbb pénzügyi következményekkel kell számolnia."},
                    {"type": "narration", "text": "A politikai figyelmeztetéseket hamarosan pénzügyi szankciók követték. Az EU létrehozta a jogállamisági kondicionalitási mechanizmust, amely kimondta: ha a bíróságok függetlenségének hiánya veszélyezteti az uniós költségvetést, a támogatásokat zárolni kell."},
                    {"type": "narration", "text": "Több ezer milliárd forintnyi kohéziós forrást fagyasztottak be. A bírói függetlenség garanciáinak visszaállítása a gazdasági túlélés feltételévé vált."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Milyen közvetlen pénzügyi következménnyel járt a jogállamisági kondicionalitási mechanizmus alkalmazása Magyarországgal szemben?", [
                    "Több ezer milliárd forintnyi uniós kohéziós és helyreállítási forrást fagyasztottak be mindaddig, amíg az igazságügyi reformok nem biztosítják a bíróságok függetlenségét.",
                    "Az EU azonnal bevezette az eurót Magyarországon.",
                    "Minden magyar állampolgárnak különadót kellett fizetnie Brüsszelnek."
                ], 0, [f"c1-{slug}-vocab"]),
                fb("grammar", "controlled", "Minél súlyosabbak az igazságügyi hiányosságok, _____ szigorúbb szankciókat alkalmaz az Európai Bizottság. (the / annál)", "annál", "The more severe the judicial deficiencies, the stricter sanctions the European Commission applies.", ["c1-adv-proportional-eu-infringement-measures"]),
                match("vocabulary", "controlled", [
                    ["7-es cikkely szerinti eljárás", "az uniós alapértékek súlyos sérelme esetén indítható politikai szankció"],
                    ["jogállamisági mechanizmus", "az uniós pénzek kifizetésének jogállami normákhoz kötése"],
                    ["kohéziós források befagyasztása", "a fejlesztési támogatások zárolása bírósági hiányosságok miatt"],
                    ["Sargentini-jelentés", "az Európai Parlament átfogó elmarasztaló dokumentuma a magyar jogállamiságról"]
                ], [f"c1-{slug}-vocab"]),
                fb("grammar", "practice", "Amilyen mértékben csorbul a bírói autonómia, _____ mértékben szigorodnak az uniós feltételek. (such / olyan)", "olyan", "To such an extent as judicial autonomy is curtailed, to that extent EU conditions become stricter.", ["c1-adv-proportional-eu-infringement-measures"]),
                sb("grammar", "practice", ["Minél", "mélyebb", "a", "jogi", "válság,", "annál", "nagyobb", "a", "pénzügyi", "veszteség."], ["Minél", "mélyebb", "a", "jogi", "válság,", "annál", "nagyobb", "a", "pénzügyi", "veszteség."], "The deeper the legal crisis, the greater the financial loss.", ["c1-adv-proportional-eu-infringement-measures"]),
                dc("dialogue", [
                    {"speaker": "Diplomata", "text": "Miért vált hatásos eszközzé a jogállamisági kondicionalitás?"},
                    {"speaker": "Közgazdász", "text": "Mert minél nyilvánvalóbbá vált a bírói függetlenség sérelme, annál szigorúbban zárolták az uniós _____."},
                    {"speaker": "Diplomata", "text": "A pénzügyi nyomás rákényszerítette a kormányt a tárgyalásokra."}
                ], ["forrásokat", "autókat", "utazásokat"], 0, ["c1-adv-proportional-eu-infringement-measures"]),
                sw("production", [{"prompt": "Write a sentence linking backsliding to sanctions using a proportional correlative structure.", "answer": "Minél inkább elmélyült az igazságszolgáltatás autonómiájának válsága, annál szigorúbb pénzügyi szankciókat és forrásbefagyasztást léptetett életbe az Európai Unió a demokratikus normák kikényszerítésére."}], ["c1-adv-proportional-eu-infringement-measures"]),
                mc("grammar", "check", "Melyik páros kötőszó fejezi ki az arányossági összefüggést a szankciók terén?", [
                    "minél inkább... annál elkerülhetetlenebbé válik / amilyen mértékben... olyan mértékben",
                    "bár esik az eső, mégis kimegyünk a térre",
                    "vagy a parlament dönt vagy a kormányhivatal"
                ], 0, ["c1-adv-proportional-eu-infringement-measures"])
            ]
        },
        {
            "num": 5,
            "stem": f"c1-{slug}-05",
            "title": "Restitution of Constitutional Checks & Balances",
            "grammar_title": "Evaluative Conclusive Particles Articulating Systemic Constitutional Restitution of Rule of Law",
            "grammar_skill": "c1-adv-conclusive-rule-of-law-restitution",
            "goals": [
                "I can analyze the systemic reform package and legal guarantees necessary for the restitution of judicial independence (*fékek és egyensúlyok, alkotmányos helyreállítás, igazságügyi reformcsomag, független ítélkezés*).",
                "I can deploy conclusive evaluative particles articulating democratic restitution (*értelemszerűen elengedhetetlen, fundamentálisan megkövetelt, kétséget kizáróan szükséges, ebből következően kikerülhetetlen*).",
                "I can debate the long-term prospects of rule-of-law consolidation in Central and Eastern Europe."
            ],
            "vocab": [
                {"lemma": "fékek és egyensúlyok", "translation": "checks and balances", "pos": "expression"},
                {"lemma": "alkotmányos helyreállítás", "translation": "constitutional restitution / restoration", "pos": "expression"},
                {"lemma": "igazságügyi reform", "translation": "judicial reform package", "pos": "expression"},
                {"lemma": "garanciális védelem", "translation": "statutory guarantee / safeguards", "pos": "expression"},
                {"lemma": "független ítélkezés", "translation": "independent adjudication", "pos": "expression"},
                {"lemma": "demokratikus kontroll", "translation": "democratic checks and balances", "pos": "expression"},
                {"lemma": "jogállami konszolidáció", "translation": "rule of law consolidation", "pos": "expression"},
                {"lemma": "normatív rend", "translation": "normative constitutional order", "pos": "expression"}
            ],
            "gr_text1": "Conclusive evaluative particles articulate the unavoidable necessity of restoring constitutional equilibrium: `értelemszerűen elengedhetetlen a bírósági önigazgatás megerősítése` (strengthening judicial self-governance is naturally indispensable), `fundamentálisan megkövetelt az elnöki önkény felszámolása` (eliminating presidential autocracy is fundamentally required), `ebből fakadóan kikerülhetetlen a garanciák törvénybe iktatása` (consequently enshrining safeguards in law is inescapable).",
            "gr_text2": "Example: `A demokratikus működéshez fundamentálisan megkövetelt a fékek és egyensúlyok rendszerének teljes körű helyreállítása`.",
            "gr_table": [
                ["A fékek és egyensúlyok rendszere értelemszerűen elengedhetetlen a jogállamban.", "The system of checks and balances is naturally indispensable in a state governed by the rule of law."],
                ["A bírói autonómia védelme fundamentálisan megkövetelt európai norma.", "The defense of judicial autonomy is a fundamentally required European norm."],
                ["Ebből kifolyólag kétséget kizáróan szükséges az OBT jogköreinek kiterjesztése.", "Consequently extending the powers of the OBT is undeniably necessary."]
            ],
            "world_story_seg": {
                "seg_slug": f"c1-{slug}-05-jogallamisag-helyreallitasa",
                "title": "A bírósági autonómia új hajnala: Az igazságügyi reform",
                "summary": "Az európai forrásbefagyasztás és a hazai bírói ellenállás nyomására a magyar parlament 2023-ban elfogadta az igazságügyi reformcsomagot. Az OBT vétójogot és valódi felügyeleti hatalmat kapott.",
                "paragraphs": [
                    {"type": "narration", "text": "2023 májusában a magyar törvényhozás – a brüsszeli feltételek szorításában – visszalépett az elmúlt évtized legsúlyosabb autokratikus intézkedéseiből. Az elfogadott igazságügyi reformcsomag alapjaiban rendezte át a hatalmi egyensúlyt."},
                    {"type": "dialogue", "speaker": "Reformbizottsági bíró", "text": "A fékek és egyensúlyok visszaállítása értelemszerűen elengedhetetlen volt: az OBT kötelező vétójogot kapott az OBH elnökének kinevezési döntéseivel szemben, s megszüntették a bírósági pályázatok önkényes érvénytelenítését."},
                    {"type": "narration", "text": "A reform nem csupán az uniós források feloldásának eszköze volt, hanem történelmi győzelem a független bírói kar számára. A bíróságok önigazgatása megerősödve került ki a hosszú éveken át tartó küzdelemből."},
                    {"type": "narration", "text": "A magyar bírák bátor helytállása megtanította a társadalmat: a jogállamiság nem elvont jogi absztrakció, hanem mindennapi szabadságunk és méltóságunk legfőbb bástyája."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Milyen kulcsfontosságú jogköröket kapott az Országos Bírói Tanács a 2023-as igazságügyi reform során?", [
                    "Kötelező erejű vétójogot és érdemi ellenőrzési jogkört az OBH elnökének kinevezési döntései felett, felszámolva az adminisztratív önkényt.",
                    "Kizárólag tanácsadói szerepet a bíróságok takarítási szerződéseiben.",
                    "Jogot a parlamenti választások elhalasztására."
                ], 0, [f"c1-{slug}-vocab"]),
                fb("grammar", "controlled", "A jogállam helyreállításához fundamentálisan _____ az intézményi garanciák megerősítése. (required / megkövetelt)", "megkövetelt", "For the restitution of the rule of law the strengthening of institutional safeguards is fundamentally required.", ["c1-adv-conclusive-rule-of-law-restitution"]),
                match("vocabulary", "controlled", [
                    ["fékek és egyensúlyok", "a hatalmi ágak kölcsönös ellenőrzésének demokratikus rendszere"],
                    ["alkotmányos helyreállítás", "a felszámolt jogállami garanciák újraépítése a törvényhozásban"],
                    ["igazságügyi reform", "a bírósági függetlenséget visszaállító átfogó jogszabálycsomag"],
                    ["független ítélkezés", "minden külső és belső nyomástól mentes bírói döntéshozatal"]
                ], [f"c1-{slug}-vocab"]),
                fb("grammar", "practice", "A hatalommegosztás garanciái értelemszerűen _____ a demokrácia fenntartásához. (indispensable / elengedhetetlenek)", "elengedhetetlenek", "The guarantees of the separation of powers are naturally indispensable for maintaining democracy.", ["c1-adv-conclusive-rule-of-law-restitution"]),
                sb("grammar", "practice", ["A", "fékek", "és", "egyensúlyok", "értelemszerűen", "elengedhetetlenek", "a", "demokratikus", "rendben."], ["A", "fékek", "és", "egyensúlyok", "értelemszerűen", "elengedhetetlenek", "a", "demokratikus", "rendben."], "Checks and balances are naturally indispensable in the democratic order.", ["c1-adv-conclusive-rule-of-law-restitution"]),
                dc("dialogue", [
                    {"speaker": "Kutató", "text": "Hogyan garantálható a bírói függetlenség hosszú távú megmaradása?"},
                    {"speaker": "Bíró", "text": "Úgy, hogy fundamentálisan megkövetelt az intézményi fékek és egyensúlyok szigorú _____."},
                    {"speaker": "Kutató", "text": "Ez a joguralom legfőbb tanulsága."}
                ], ["védelme", "eltörlése", "feledése"], 0, ["c1-adv-conclusive-rule-of-law-restitution"]),
                sw("production", [{"prompt": "Write a conclusive sentence on constitutional restitution.", "answer": "A bíróságok szervezeti autonómiájának védelme értelemszerűen elengedhetetlen és fundamentálisan megkövetelt feltétele a jogállamiság teljes körű alkotmányos helyreállításának."}], ["c1-adv-conclusive-rule-of-law-restitution"]),
                mc("grammar", "check", "Melyik kifejezés szintetizálja a jogállami helyreállítás elkerülhetetlenségét?", [
                    "értelemszerűen elengedhetetlen / fundamentálisan megkövetelt / ebből fakadóan kikerülhetetlen",
                    "ha van kedvünk, akkor megváltoztatjuk a törvényt",
                    "talán jobb lenne mindent úgy hagyni ahogy van"
                ], 0, ["c1-adv-conclusive-rule-of-law-restitution"])
            ]
        }
    ]

    for l in disc_lessons:
        emit_instructional_lesson(32, "discourse", l, disc_title, disc_intro if l["num"] == 1 else None)

    # Combined World Story
    write_json(
        f"stories/world/c1/c1-{slug}-biroi-fuggetlenseg-jogallamisag.json",
        {
            "id": f"story.c1.{slug}.combined",
            "title": "A bírói függetlenség és a jogállamiság küzdelme Magyarországon",
            "level": "C1",
            "lesson": 5,
            "order": 32,
            "type": "world",
            "estimatedMinutes": 8,
            "grammar": ["c1-adv-conclusive-rule-of-law-restitution"],
            "summary": "Átfogó tényfeltáró krónika a 2010 utáni magyar igazságszolgáltatásról: a bírák kényszernyugdíjazásáról, az OBH elnöki hatalomkoncentrációjáról, az Országos Bírói Tanács (OBT) példátlan ellenállásáról, az uniós 7-es cikkelyről és forrásbefagyasztásról, valamint a fékek és egyensúlyok alkotmányos helyreállításáról.",
            "vocabularyTopics": [
                "The Dismantling of Independent Judiciary & Rule of Law Breakdown",
                "Restitution of Constitutional Checks & Balances"
            ],
            "paragraphs": [
                {"type": "narration", "text": "A 2010 utáni évtizedben Magyarország az európai jogállamisági viták epicentrumává vált. A kétharmados törvényhozási többség elsőként az igazságszolgáltatás autonómiáját vette célba: a bírák 2011-es kényszernyugdíjazásával lefejezték a bíróságok vezetését, hogy helyükre a végrehajtó hatalomhoz lojális kádereket állíthassanak."},
                {"type": "narration", "text": "Az intézményi centralizáció betetőzéseként létrejött az Országos Bírósági Hivatal (OBH), amelynek elnöke egyszemélyi hatalmat gyakorolt a bírói kinevezések, a költségvetés és a pályázatok felett. A nyertes szakmai pályázatok önkényes megsemmisítése és a politikai bizalmasok kirendelése mindennapossá vált, súlyosan veszélyeztetve a belső bírói függetlenséget."},
                {"type": "narration", "text": "A rendszer azonban nem számolt a bírói kar belső etikai erejével. A bírák által választott Országos Bírói Tanács (OBT) példátlan bátorsággal szembeszállt a hivatali önkénnyel: sorozatos törvénysértéseket állapított meg az OBH elnökével szemben, és kezdeményezte annak elmozdítását, miközben tagjai ellenálltak a kormánymédia rágalomhadjáratának."},
                {"type": "narration", "text": "A nemzetközi színtéren az Európai Unió fokozatosan felismerte a tekintélyelvű visszarendeződés veszélyeit. A Sargentini-jelentés nyomán megindult a 7-es cikkely szerinti eljárás, majd a jogállamisági kondicionalitási mechanizmus révén az Unió több ezer milliárd forintnyi fejlesztési pénzt fagyasztott be, a bírói autonómia visszaállításához kötve a kifizetéseket."},
                {"type": "narration", "text": "A pénzügyi kényszer és a hazai szakmai ellenállás végül meghátrálásra kényszerítette a hatalmat: a 2023-as igazságügyi reformcsomag megerősítette az OBT vétójogait és garanciáit. A magyar bírósági válság megmutatta: a jogállamiság nem magától értetődő állapot, hanem mindennap megvédendő szabadságjogunk."}
            ]
        }
    )

    # Discourse Consolidation
    emit_consolidation_lesson(
        32,
        "discourse",
        f"c1-{slug}-consolidation",
        disc_title,
        [
            "I can master the analytical vocabulary of judicial independence, court administration autocracy, and supranational rule of law sanctions.",
            "I can employ discourse markers diagnosing judicial capture, critical evaluative adverbials, and deontic modal structures of integrity.",
            "I can construct proportional correlative structures and conclusive evaluative syntheses on constitutional restitution."
        ],
        [
            mc("grammar", "recognize", "Melyik kifejezés diagnosztizálja szakszerűen a bíróságok politikai alávetését?", [
                "intézményi szintű politikai beavatkozásként értékelve / a bírói autonómia gerincét megtörve",
                "amikor a bírák elfáradnak a délutáni tárgyaláson",
                "hogyha új bútorokat visznek a bírósági szobába"
            ], 0, ["c1-discourse-judicial-subjugation-framing"]),
            mc("grammar", "recognize", "Milyen szerkezettel leplezhető le az igazgatási hatalomkoncentráció a leghitelesebben?", [
                "a pályázatokat önkényesen érvénytelenítve és rendszerszinten centralizálva a jogköröket",
                "egy szép beszédet mondva az ünnepségen",
                "amikor a miniszter meglátogatja az épületet"
            ], 0, ["c1-adv-institutional-monopolization-critique"]),
            match("vocabulary", "recognize", [
                ["kényszernyugdíjazás", "a bírói vezetés 2011-es azonnali, politikai célú eltávolítása"],
                ["Országos Bírósági Hivatal", "az egyszemélyi adminisztratív centralizáció intézménye"],
                ["Országos Bírói Tanács", "a bírák által választott független ellenőrző testület"],
                ["jogállamisági mechanizmus", "uniós pénzügyi szankció a bírói függetlenség védelmében"]
            ], [f"c1-{slug}-vocab"]),
            fb("vocabulary", "recall", "A bíróságok igazgatását az OBH elnöki _____ jellemezte az elmúlt évtizedben. (power concentration / hatalomkoncentrációja)", "hatalomkoncentrációja", "Court governance was characterized by the power concentration of the OBH president over the past decade.", [f"c1-{slug}-vocab"]),
            fb("vocabulary", "recall", "A bírói kar tagjainak etikai _____ védelmezése minden körülmények között elengedhetetlen. (integrity / integritásának)", "integritásának", "Defending the ethical integrity of members of the judiciary is indispensable under all circumstances.", [f"c1-{slug}-vocab"]),
            fb("grammar", "recall", "A reformot intézményi beavatkozásként _____ marasztalta el a nemzetközi bíróság. (evaluating / értékelve)", "értékelve", "Evaluating the reform as institutional intervention the international court condemned it.", ["c1-discourse-judicial-subjugation-framing"]),
            fb("grammar", "context", "Minél jobban sérül a jogbiztonság, _____ szigorúbb forrásbefagyasztást rendel el az Unió. (the / annál)", "annál", "The more legal certainty is damaged, the stricter freezing of funds the Union orders.", ["c1-adv-proportional-eu-infringement-measures"]),
            fb("grammar", "context", "A fékek és egyensúlyok rendszere értelemszerűen _____ a demokráciában. (indispensable / elengedhetetlen)", "elengedhetetlen", "The system of checks and balances is naturally indispensable in a democracy.", ["c1-adv-conclusive-rule-of-law-restitution"]),
            mc("grammar", "context", "Mi a deontikus etikai kötelességek lényege az OBT bíráinak magatartásában?", [
                "A bírói eskü megingathatatlan védelme és a törvénysértések nyílt kimondása a hatalmi nyomással és propagandával szemben.",
                "A kormányrendeletek automatikus végrehajtása kérdések nélkül.",
                "A bírósági tárgyalások elhalasztása rossz időjárás esetén."
            ], 0, ["c1-modal-deontic-judicial-integrity"]),
            sb("grammar", "produce", ["A", "bírói", "függetlenség", "védelme", "fundamentálisan", "megkövetelt", "minden", "demokráciában."], ["A", "bírói", "függetlenség", "védelme", "fundamentálisan", "megkövetelt", "minden", "demokráciában."], "The defense of judicial independence is fundamentally required in every democracy.", ["c1-adv-conclusive-rule-of-law-restitution"]),
            sw("production", [{"prompt": "Write a critical evaluation of judicial backsliding using a proportional correlative structure.", "answer": "Minél nyíltabban próbálta meg a politikai hatalom felszámolni a bírói önigazgatást, annál határozottabbá vált a hazai bírói testületek ellenállása és a szupranacionális uniós intézmények szankciós fellépése."}], ["c1-adv-proportional-eu-infringement-measures"]),
            sw("production", [{"prompt": "Synthesize the historical lesson of the judicial crisis using a conclusive evaluative particle.", "answer": "A fékek és egyensúlyok intézményi helyreállítása értelemszerűen elengedhetetlen és fundamentálisan megkövetelt ahhoz, hogy az igazságszolgáltatás mentes maradjon a mindenkori politikai önkénytől."}], ["c1-adv-conclusive-rule-of-law-restitution"])
        ]
    )

    print("=== Finished C1 Unit 32 ===")


if __name__ == "__main__":
    generate_unit_32()
