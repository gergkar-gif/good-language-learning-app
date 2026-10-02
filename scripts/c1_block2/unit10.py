#!/usr/bin/env python3
"""
Hungarian C1 Block 2 - Unit 10 Generator:
  - Track 1 (Core): Unit 10 — "Contractual Precision, Ambiguity & Negotiation Register" (c1-10)
  - Track 2 (Discourse): Unit 10 — "Commercial Negotiation & Corporate Law in Hungary" (c1-szerzodesek)
"""

import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT))

from scripts.c1_block1.common import mc, match, fb, sb, dc, sw, write_json, emit_instructional_lesson, emit_consolidation_lesson
from scripts.c1_block2.registry_helper import register_unit


def generate_unit_10():
    print("=== Generating C1 Unit 10 ===")
    
    # Register skills & titles
    new_skills = {
        "c1-10-vocab": {"kind": "vocabulary"},
        "c1-szerzodesek-vocab": {"kind": "vocabulary"},
        "c1-contractual-stipulations": {"kind": "grammar"},
        "c1-negotiation-hedging": {"kind": "grammar"},
        "c1-liability-exemption": {"kind": "grammar"},
        "c1-corporate-governance": {"kind": "grammar"},
        "c1-eu-harmonization": {"kind": "grammar"},
    }
    new_titles = {
        "c1-10-vocab": "reading",
        "c1-szerzodesek-vocab": "reading",
        "c1-contractual-stipulations": "contractual drafting stipulations and formal covenant formulas",
        "c1-negotiation-hedging": "diplomatic commercial negotiation register and strategic hedging",
        "c1-liability-exemption": "liability limitation indemnity clauses and force majeure framing",
        "c1-corporate-governance": "corporate governance company law and statutory compliance register",
        "c1-eu-harmonization": "european union commercial harmonization and cross border business law",
    }
    
    core_title = "Contractual Precision, Ambiguity & Negotiation Register"
    core_stems = [f"c1-10-0{i}" for i in range(1, 6)] + ["c1-10-consolidation"]
    disc_title = "Commercial Negotiation & Corporate Law in Hungary"
    disc_stems = [f"c1-szerzodesek-0{i}" for i in range(1, 6)] + ["c1-szerzodesek-consolidation"]
    
    register_unit(10, core_title, core_stems, disc_title, disc_stems, new_skills, new_titles)

    # ----------------------------------------------------
    # TRACK 1: CORE (c1-10)
    # ----------------------------------------------------
    core_intro = [
        "Contractual draftsmanship demands surgical semantic precision: eliminating ambiguities, formulating caveats, drafting indemnity clauses, and mastering commercial negotiation registers.",
        "In this unit, inspired by Sándor Márai's examination of middle-class bourgeois morality, legal honor, and obligation in 'Sértődöttek' (1947–1948), you will master contractual covenants, liability disclaimers (felelősségkizárás, vis maior), and high-level business negotiation strategies."
    ]

    core_lessons = [
        {
            "num": 1,
            "stem": "c1-10-01",
            "title": "Contractual Covenants and Operative Clauses",
            "grammar_title": "Operative Verbs and Binding Covenants in Civil Law Contracts",
            "grammar_skill": "c1-contractual-stipulations",
            "goals": [
                "I can draft binding contractual covenants (*szerződő felek rögzítik, megállapodnak, kötelezettséget vállalnak*).",
                "I can formulate performance terms (*teljesítés helye és ideje, átadás-átvétel*).",
                "I can distinguish between unilateral declarations and bilateral consensual agreements."
            ],
            "vocab": [
                {"lemma": "kölcsönösen megállapodnak", "translation": "mutually agree", "pos": "expression"},
                {"lemma": "kötelezettséget vállal", "translation": "undertakes an obligation", "pos": "expression"},
                {"lemma": "szerződésszerű teljesítés", "translation": "contractual performance / fulfillment", "pos": "noun"},
                {"lemma": "átadás-átvételi jegyzőkönyv", "translation": "handover-acceptance protocol / certificate", "pos": "noun"},
                {"lemma": "jogutód", "translation": "legal successor", "pos": "noun"},
                {"lemma": "érvénytelenség", "translation": "invalidity, nullity", "pos": "noun"},
                {"lemma": "részleges érvénytelenség", "translation": "partial invalidity / severability", "pos": "noun"},
                {"lemma": "elválaszthatatlan részét képezi", "translation": "forms an inseparable part of", "pos": "expression"}
            ],
            "gr_text1": "Hungarian civil contract drafting opens with declaratory operative formulas: *A felek egybehangzó akarattal megállapodnak az alábbiakban...* (The parties with concurring intent agree on the following).",
            "gr_text2": "The severability clause (*érvénytelenségi záradék*) ensures that the invalidity of one clause does not void the entire contract: *A szerződés valamely pontjának érvénytelensége nem érinti a fennmaradó rendelkezések érvényességét.*",
            "gr_table": [
                ["A felek kölcsönösen megállapodnak a vételár összegében.", "The parties mutually agree on the purchase price amount."],
                ["A vállalkozó határidőre történő szerződésszerű teljesítésre vállal kötelezettséget.", "The contractor undertakes obligation for timely contractual performance."],
                ["A jelen megállapodás mellékletei annak elválaszthatatlan részét képezik.", "The annexes of the present agreement form an inseparable part thereof."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mit rögzít az 'érvénytelenségi záradék' (severability clause) egy szerződésben?", ["Hogy egyetlen pont érvénytelensége nem teszi érvénytelenné az egész szerződést.", "Hogy senkinek sem kell fizetnie semmit.", "Hogy a szerződés azonnal megszűnik."], 0, ["c1-10-vocab"]),
                fb("grammar", "controlled", "A szerződő felek kölcsönösen és egybehangzóan _____ az alábbi feltételekben. (agree / megállapodnak)", "megállapodnak", "The contracting parties mutually and concurrently agree on the following conditions.", ["c1-contractual-stipulations"]),
                match("vocabulary", "controlled", [["kölcsönösen megállapodnak", "mutually agree"], ["kötelezettséget vállal", "undertakes obligation"], ["jogutód", "legal successor"], ["szerződésszerű teljesítés", "contractual performance"]], ["c1-10-vocab"]),
                fb("grammar", "practice", "A jelen szerződés mellékletei annak elválaszthatatlan részét _____. (form / képezik)", "képezik", "The annexes of the present contract form an inseparable part thereof.", ["c1-contractual-stipulations"]),
                sb("grammar", "practice", ["A", "felek", "jogvitáikat", "elsődlegesen", "békés", "tárgyalások", "útján", "rendezik."], ["A", "felek", "jogvitáikat", "elsődlegesen", "békés", "tárgyalások", "útján", "rendezik."], "The parties settle their legal disputes primarily through peaceful negotiations.", ["c1-contractual-stipulations"]),
                dc("dialogue", [
                    {"speaker": "Jogtanácsos", "text": "Mikor tekinthető a megrendelés teljesítettnek?"},
                    {"speaker": "Projektvezető", "text": "Kizárólag az átadás-átvételi jegyzőkönyv mindkét fél általi _____ után."},
                ], ["aláírása", "eldobása", "másolása"], 0, ["c1-contractual-stipulations"]),
                sw("production", [{"prompt": "Write a formal contractual clause defining a binding obligation.", "answer": "A vállalkozó kifejezett kötelezettséget vállal arra, hogy a munkálatokat a műszaki leírásnak megfelelően, határidőre elvégzi."}], ["c1-contractual-stipulations"]),
                mc("grammar", "check", "Melyik mondat alkalmaz szabályos jogi megfogalmazást szerződéskötéskor?", [
                    "A szerződés a felek cégszerű aláírásának napján lép hatályba.",
                    "A papír akkor él, amikor a főnökök ráírják a nevüket.",
                    "Mindjárt érvényes lesz a megbeszélésünk."
                ], 0, ["c1-contractual-stipulations"])
            ]
        },
        {
            "num": 2,
            "stem": "c1-10-02",
            "title": "Commercial Negotiation Register and Strategic Hedging",
            "grammar_title": "Diplomatic Commercial Register: Concessions, Counter-Offers, and Hedging",
            "grammar_skill": "c1-negotiation-hedging",
            "goals": [
                "I can conduct commercial negotiations using diplomatic, high-register Hungarian.",
                "I can formulate conditional counter-offers (*hajlandóak lennénk elfogadni, feltéve, hogy...*).",
                "I can decline commercial proposals with strategic politeness and firm boundaries."
            ],
            "vocab": [
                {"lemma": "kompromisszumos megoldás", "translation": "compromise solution", "pos": "noun"},
                {"lemma": "ellentételezés", "translation": "consideration, compensation, quid pro quo", "pos": "noun"},
                {"lemma": "engedmény", "translation": "concession, discount, rebate", "pos": "noun"},
                {"lemma": "tárgyalási alap", "translation": "basis for negotiation", "pos": "noun"},
                {"lemma": "hajlandóságot mutat", "translation": "shows willingness to", "pos": "expression"},
                {"lemma": "elzárkózik", "translation": "refuses, rejects, distances oneself", "pos": "verb"},
                {"lemma": "rugalmasság", "translation": "flexibility", "pos": "noun"},
                {"lemma": "holtpont", "translation": "deadlock, impasse", "pos": "noun"}
            ],
            "gr_text1": "Commercial negotiation register balances politeness with tactical firmness. Rather than saying *nem fogadjuk el az árat*, diplomatic Hungarian uses conditional hedging: *Jelenlegi formájában az ajánlat nem képezheti tárgyalási alapunkat, mindazonáltal nyitottak vagyunk a további egyeztetésre.*",
            "gr_text2": "Concessions are framed conditionally: *Hajlandóak volnánk engedményt tenni a szállítási határidő tekintetében, amennyiben a fizetési feltételek kedvezőbbé válnak.*",
            "gr_table": [
                ["A felek kompromisszumos megoldásra törekszenek a tárgyalások során.", "The parties strive for a compromise solution during negotiations."],
                ["Cégünk hajlandóságot mutat a fizetési határidő meghosszabbítására.", "Our firm shows willingness to extend the payment deadline."],
                ["A jelenlegi feltételek mellett elzárkózunk az ajánlat elfogadásától.", "Under current terms we decline acceptance of the offer."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Hogyan utasít el egy professzionális üzleti tárgyaló egy előnytelen ajánlatot?", ["Diplomatikusan jelezve a nyitottságot az észszerűbb módosítások iránt.", "Sértődött kiabálással a tárgyalóteremben.", "Azonnali felállással köszönés nélkül."], 0, ["c1-10-vocab"]),
                fb("grammar", "controlled", "Cégünk hajlandó lenne engedményt tenni az árban, _____ a megrendelt mennyiség eléri a tízezer darabot. (provided that / feltéve hogy)", "feltéve hogy", "Our firm would be willing to make a price concession, provided that the ordered quantity reaches ten thousand units.", ["c1-negotiation-hedging"]),
                match("vocabulary", "controlled", [["kompromisszumos megoldás", "compromise solution"], ["ellentételezés", "consideration / compensation"], ["tárgyalási alap", "basis for negotiation"], ["holtpont", "deadlock / impasse"]], ["c1-10-vocab"]),
                fb("grammar", "practice", "A tárgyalások a vitás pontok miatt sajnos _____ jutottak. (to deadlock / holtpontra)", "holtpontra", "Due to contested points the negotiations unfortunately reached a deadlock.", ["c1-negotiation-hedging"]),
                sb("grammar", "practice", ["A", "hosszú", "távú", "együttműködés", "mindkét", "fél", "részéről", "rugalmasságot", "kíván."], ["A", "hosszú", "távú", "együttműködés", "mindkét", "fél", "részéről", "rugalmasságot", "kíván."], "Long-term cooperation requires flexibility on the part of both parties.", ["c1-negotiation-hedging"]),
                dc("dialogue", [
                    {"speaker": "Beszállító", "text": "Elfogadható-e Önöknek a harmincnapos késedelmi sáv?"},
                    {"speaker": "Beszerzési igazgató", "text": "Ez a feltétel nem képezheti tárgyalási _____ a gyártási ütemterv miatt."},
                    {"speaker": "Beszállító", "text": "Értem, akkor vizsgáljuk meg az alternatív szállítási útvonalakat."},
                ], ["alapunkat", "szerencsénket", "ebédünket"], 0, ["c1-negotiation-hedging"]),
                sw("production", [{"prompt": "Write a diplomatic counter-offer in commercial negotiation Hungarian.", "answer": "Nagyra értékeljük ajánlatukat, mindazonáltal a vételár tekintetében kizárólag volumenkedvezmény biztosítása esetén áll módunkban szerződést kötni."}], ["c1-negotiation-hedging"]),
                mc("grammar", "check", "Melyik megfogalmazás alkalmaz sikeres üzleti tárgyalási finomítást (hedging)?", [
                    "Bár a felajánlott konstrukció figyelemreméltó, megfontolandónak tartanánk a garanciális időszak kibővítését a szerződéskötés előtt.",
                    "Ez az ajánlat semmire sem jó, adjanak jobbat.",
                    "Nem veszünk semmit, amíg le nem viszik az árat a felére."
                ], 0, ["c1-negotiation-hedging"])
            ]
        },
        {
            "num": 3,
            "stem": "c1-10-03",
            "title": "Liability Limitation, Indemnity and Force Majeure",
            "grammar_title": "Drafting Liability Disclaimers, Indemnity, and Vis Maior Clauses",
            "grammar_skill": "c1-liability-exemption",
            "goals": [
                "I can draft liability exclusion and limitation clauses (*felelősségkizárás, kártérítés felső határa*).",
                "I can formulate indemnity and hold-harmless covenants (*kártalanítási kötelezettség*).",
                "I can define unforeseen external impediments using force majeure (*vis maior*) terms."
            ],
            "vocab": [
                {"lemma": "felelősségkizárás", "translation": "limitation / exclusion of liability", "pos": "noun"},
                {"lemma": "kártalanítás", "translation": "indemnification, compensation", "pos": "noun"},
                {"lemma": "vis maior", "translation": "force majeure (act of God)", "pos": "expression"},
                {"lemma": "elháríthatatlan akadály", "translation": "unavoidable impediment", "pos": "noun"},
                {"lemma": "kötbér", "translation": "contractual penalty / liquidated damages", "pos": "noun"},
                {"lemma": "szándékos károkozás", "translation": "intentional infliction of damage", "pos": "noun"},
                {"lemma": "súlyos gondatlanság", "translation": "gross negligence", "pos": "noun"},
                {"lemma": "mentesül a felelősség alól", "translation": "is exempted / released from liability", "pos": "expression"}
            ],
            "gr_text1": "Under the Hungarian Civil Code (Ptk.), liability for intentional damage (*szándékos károkozás*) or harm to life and bodily integrity cannot be lawfully excluded.",
            "gr_text2": "Force majeure (*vis maior*) clauses excuse non-performance only if an impediment is external, unforeseeable at contract execution, and unavoidable: *A fél mentesül a felelősség alól, amennyiben bizonyítja, hogy a szerződésszegést elháríthatatlan külső körülmény okozta.*",
            "gr_table": [
                ["A vállalkozó felelőssége a szerződésben kikötött kötbér összegéig terjed.", "The contractor's liability extends up to the contractual penalty sum stipulated."],
                ["Vis maior esetén mindkét fél mentesül a késedelmi következmények alól.", "In case of force majeure both parties are exempted from delay consequences."],
                ["A szándékos szerződésszegésért való felelősség érvényesen nem zárható ki.", "Liability for intentional breach of contract cannot be validly excluded."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Milyen körülmény minősül 'vis maior'-nak a polgári jogban?", ["Külső, előre nem látható és elháríthatatlan esemény (pl. természeti katasztrófa, háború).", "Hogy a cégvezető elfelejtett bemenni dolgozni.", "Egy sima esős délután."], 0, ["c1-10-vocab"]),
                fb("grammar", "controlled", "A szerződésszegő fél _____ a kártérítési felelősség alól, ha a kárt vis maior okozta. (is exempted / mentesül)", "mentesül", "The breaching party is exempted from damage liability if the damage was caused by force majeure.", ["c1-liability-exemption"]),
                match("vocabulary", "controlled", [["felelősségkizárás", "limitation of liability"], ["vis maior", "force majeure"], ["kötbér", "contractual penalty"], ["súlyos gondatlanság", "gross negligence"]], ["c1-10-vocab"]),
                fb("grammar", "practice", "A jogszabály tiltja a szándékos károkozásért vagy emberi élet kioltásáért való felelősség előzetes _____. (exclusion / kizárását)", "kizárását", "Statutory law prohibits prior exclusion of liability for intentional harm or loss of human life.", ["c1-liability-exemption"]),
                sb("grammar", "practice", ["A", "késedelem", "idejére", "a", "megrendelő", "napi", "kötbér", "fizetésére", "tarthat", "igényt."], ["A", "késedelem", "idejére", "a", "megrendelő", "napi", "kötbér", "fizetésére", "tarthat", "igényt."], "For the duration of delay the customer may claim payment of daily liquidated damages.", ["c1-liability-exemption"]),
                dc("dialogue", [
                    {"speaker": "Kivitelező", "text": "Felelőssé tehetők vagyunk-e a viharkár miatti csúszásért?"},
                    {"speaker": "Ügyvéd", "text": "Nem, mert a természeti csapás dokumentált elháríthatatlan külső _____ minősül."},
                ], ["akadálynak", "javaslatnak", "ötletnek"], 0, ["c1-liability-exemption"]),
                sw("production", [{"prompt": "Draft a standard contractual force majeure clause in Hungarian.", "answer": "Egyik fél sem felelős a szerződéses kötelezettségek elmulasztásáért, amennyiben azt bizonyíthatóan elháríthatatlan külső vis maior esemény okozta."}], ["c1-liability-exemption"]),
                mc("grammar", "check", "Melyik felelősségkizáró kikötés tekinthető jogilag semmisnek a magyar Ptk. szerint?", [
                    "A szándékos károkozásért vagy a testi épség megsértéséért való felelősséget kizáró kikötés.",
                    "A késedelmi kötbér mértékét korlátozó kikötés.",
                    "A határidők pontos naptári kijelölése."
                ], 0, ["c1-liability-exemption"])
            ]
        },
        {
            "num": 4,
            "stem": "c1-10-04",
            "title": "Corporate Governance and Statutory Compliance",
            "grammar_title": "Company Law Registers: Shareholders, Boards, and Fiduciary Duties",
            "grammar_skill": "c1-corporate-governance",
            "goals": [
                "I can navigate Hungarian corporate governance syntax (*társasági jog, közgyűlés, felügyelőbizottság*).",
                "I can articulate officer fiduciary duties and statutory compliance obligations.",
                "I can draft formal corporate board resolutions and minutes in authentic style."
            ],
            "vocab": [
                {"lemma": "közgyűlés", "translation": "general meeting of shareholders", "pos": "noun"},
                {"lemma": "igazgatóság", "translation": "board of directors", "pos": "noun"},
                {"lemma": "felügyelőbizottság", "translation": "supervisory board", "pos": "noun"},
                {"lemma": "vezető tisztségviselő", "translation": "executive officer", "pos": "noun"},
                {"lemma": "társasági szerződés", "translation": "articles of association / partnership deed", "pos": "noun"},
                {"lemma": "összeférhetetlenség", "translation": "conflict of interest", "pos": "noun"},
                {"lemma": "felelősségbiztosítás", "translation": "liability insurance (D&O)", "pos": "noun"},
                {"lemma": "jogszabályi megfelelés", "translation": "statutory compliance", "pos": "noun"}
            ],
            "gr_text1": "Hungarian company law distinguishes internal organs: the supreme body (*közgyűlés / taggyűlés*), executive management (*igazgatóság / ügyvezetés*), and oversight (*felügyelőbizottság*).",
            "gr_text2": "Executive officers owe a fiduciary duty of care: they must conduct company affairs *a társaság érdekeinek elsődlegessége alapján* (with primacy of the company's interests) under severe personal civil liability.",
            "gr_table": [
                ["A közgyűlés határozatképessége a szavazati jogok többségéhez kötött.", "Quorum of the general meeting is conditioned upon majority of voting rights."],
                ["A vezető tisztségviselő a társaság érdekeinek megfelelően köteles eljárni.", "The executive officer is obligated to act in accordance with the company's interests."],
                ["A felügyelőbizottság ellenőrzi a társaság ügyvezetését és pénzügyi beszámolóját.", "The supervisory board inspects company management and financial statements."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Melyik szerv képezi a gazdasági társaság legfőbb döntéshozó testületét?", ["A részvényesek vagy tagok közgyűlése / taggyűlése.", "A portaszolgálat.", "A szomszédos kávéház közönsége."], 0, ["c1-10-vocab"]),
                fb("grammar", "controlled", "A vezető tisztségviselő köteles eljárása során a társaság és a hitelezők érdekeit szem előtt tartani a jogszabályi _____ szellemében. (compliance / megfelelés)", "megfelelés", "In his conduct the executive officer is obligated to keep the interests of the company and creditors in mind in the spirit of statutory compliance.", ["c1-corporate-governance"]),
                match("vocabulary", "controlled", [["közgyűlés", "general meeting"], ["igazgatóság", "board of directors"], ["felügyelőbizottság", "supervisory board"], ["vezető tisztségviselő", "executive officer"]], ["c1-10-vocab"]),
                fb("grammar", "practice", "A közgyűlés kizárólagos hatáskörébe tartozik a társasági _____ módosítása. (articles of association / szerződés)", "szerződés", "Modification of the articles of association falls within the exclusive competence of the general meeting.", ["c1-corporate-governance"]),
                sb("grammar", "practice", ["A", "vezető", "tisztségviselő", "felelősséggel", "tartozik", "az", "okozott", "károkért."], ["A", "vezető", "tisztségviselő", "felelősséggel", "tartozik", "az", "okozott", "károkért."], "The executive officer is liable for damages caused.", ["c1-corporate-governance"]),
                dc("dialogue", [
                    {"speaker": "Részvényes", "text": "Hány százalék szükséges az alapszabály módosításához?"},
                    {"speaker": "Társasági jogász", "text": "A törvény értelmében háromnegyedes _____ többség szükséges."},
                ], ["szavazati", "éhségi", "hangoskodási"], 0, ["c1-corporate-governance"]),
                sw("production", [{"prompt": "Draft a formal corporate resolution approving an annual financial report.", "answer": "A Közgyűlés egyhangúlag elfogadja a társaság előző üzleti évről szóló számviteli beszámolóját és adózott eredményének felosztását."}], ["c1-corporate-governance"]),
                mc("grammar", "check", "Milyen kötelezettség terheli a vezető tisztségviselőt összeférhetetlenség esetén?", [
                    "Köteles bejelenteni az érdekeltségét, és tartózkodni az érintett döntéshozatalban való részvételtől.",
                    "Semmit sem kell tennie, titokban tarthatja.",
                    "Azonnal át kell utalnia a cég vagyonát saját magának."
                ], 0, ["c1-corporate-governance"])
            ]
        },
        {
            "num": 5,
            "stem": "c1-10-05",
            "title": "Middle-Class Honor, Contract and Moral Obligation: Sándor Márai",
            "grammar_title": "Bourgeois Morality, Contractual Integrity and Personal Dignity",
            "grammar_skill": "c1-eu-harmonization",
            "goals": [
                "I can analyze Sándor Márai's moral anatomy of bourgeois contractuality in 'Sértődöttek'.",
                "I can contrast external legal legality with internal moral honor and fidelity.",
                "I can synthesize 20th-century Hungarian reflections on European civic order."
            ],
            "vocab": [
                {"lemma": "polgári ethosz", "translation": "bourgeois / civic ethos", "pos": "noun"},
                {"lemma": "adott szó szentsége", "translation": "sanctity of one's given word", "pos": "expression"},
                {"lemma": "szerződéses hűség", "translation": "contractual fidelity / pacta sunt servanda", "pos": "noun"},
                {"lemma": "belső mérték", "translation": "internal standard / moral compass", "pos": "noun"},
                {"lemma": "becsületbeli ügy", "translation": "matter of honor", "pos": "noun"},
                {"lemma": "jogi formalizmus", "translation": "legal formalism", "pos": "noun"},
                {"lemma": "morális kötelesség", "translation": "moral obligation", "pos": "noun"},
                {"lemma": "polgári társadalom", "translation": "civil / bourgeois society", "pos": "noun"}
            ],
            "gr_text1": "Sándor Márai (1900–1989) was the preeminent chronicler of Central European bourgeois civilization (*polgári kultúra*). In his trilogy *Sértődöttek*, he examined the tragic collapse of European order when formal legality detached from moral honor.",
            "gr_text2": "For Márai, the true foundation of society is not the written police code, but the sanctity of the given word (*az adott szó szentsége* / *pacta sunt servanda*): when men honor contracts out of self-respect rather than fear of punishment.",
            "gr_table": [
                ["Az adott szó szentsége mint a polgári világ alapköve...", "The sanctity of the given word as the cornerstone of the bourgeois world..."],
                ["A szerződéses hűség és a belső erkölcsi mérték parancsa...", "Contractual fidelity and the command of internal moral standards..."],
                ["Amikor a jogi formalizmus elszakad a személyes becsülettől...", "When legal formalism detaches from personal honor..."]
            ],
            "classic_story": {
                "slug": "c1-10-marai",
                "author": "Márai Sándor",
                "work": "Sértődöttek (1947–1948) / Egy polgár vallomásai",
                "title": "A polgári becsület és az adott szó szentsége",
                "summary": "Sándor Márai's timeless meditation on the bourgeois ethos, contractual fidelity, and personal honor as the bedrock of European civilization.",
                "characters": ["Márai Sándor", "Garren Péter"],
                "paragraphs": [
                    {"type": "narration", "text": "Amikor a huszadik század közepén Európa történelmi városai romokban hevertek, és a totalitárius eszmék szétzúzták a jogállam alapjait, Márai Sándor emigrációjának küszöbén megírta monumentális regényciklusát, a Sértődötteket. A kassai patríciusok kései örököse nem pusztán egy korszak pusztulását siratta el, hanem a polgári létezés legmélyebb erkölcsi fundamentumát kísérelte meg megmenteni az emlékezet számára."},
                    {"type": "narration", "text": "Márai számára a polgárság nem társadalmi osztályt vagy vagyoni helyzetet jelentett, hanem minőséget és magatartásformát: a belső mérték és a becsület szigorú törvényét. Ennek a világnak a legszentebb intézménye a szerződés volt. De nem a paragrafusokba foglalt, kényszerrel kikényszerített jogi szöveg, hanem az 'adott szó szentsége': az a csendes kézfogás, amely mögött ott állt egy egész ember élete, családjának hitele és személyes tisztessége."},
                    {"type": "narration", "text": "A regény lapjain Márai leleplezi azt a modern cinizmust, amely a jogot pusztán a ravaszkodás és a kibúvók eszközének tekinti. Ha a törvény betűje elszakad a belső morális felelősségtől, a civilizáció barbárságba zuhan vissza. A szerződéses hűség – a latin bölcsesség szerint a 'pacta sunt servanda' elve – nem jogi formalizmus, hanem az emberi méltóság végső próbája: a bizonyíték arra, hogy az ember képes ura lenni saját ösztöneinek és tiszteletben tartani a másik ember szabadságát."},
                    {"type": "narration", "text": "Márai kristálytiszta, emelkedett mondatai ma is arra intenek, hogy az igazi jogállam nem bírósági épületekben, hanem az állampolgárok szívében és jellemében épül fel. Csak az a társadalom maradhat szabad, amelyben az ígéret szent, és a becsület nem eladó áru a piacon."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Mit jelentett Márai Sándor számára 'az adott szó szentsége'?", ["A személyes becsületen és kölcsönös bizalmon alapuló megkérdőjelezhetetlen morális kötelezettséget.", "Egy régi népmesei fordulatot.", "Az adózás elkerülésének módját."], 0, ["c1-10-vocab"]),
                fb("grammar", "controlled", "Márai szerint a szerződéses hűség nem puszta jogi formalizmus, hanem a polgári _____ legmélyebb erkölcsi alapköve. (ethos / ethosz)", "ethosz", "According to Márai contractual fidelity is not mere legal formalism, but the deepest moral cornerstone of bourgeois ethos.", ["c1-eu-harmonization"]),
                match("vocabulary", "controlled", [["polgári ethosz", "civic ethos"], ["adott szó szentsége", "sanctity of given word"], ["szerződéses hűség", "contractual fidelity"], ["belső mérték", "internal moral compass"]], ["c1-10-vocab"]),
                mc("reading", "practice", "Miért tekintette Márai a szerződés betartását a civilizáció mércéjének?", [
                    "Mert a szerződéses hűség bizonyítja, hogy az ember képes tisztelni mások szabadságát és ura saját ösztöneinek.",
                    "Mert a szerződésekért sok pénzt fizettek az ügyvédeknek.",
                    "Mert nem szerette a könyveket."
                ], 0, None),
                sb("grammar", "practice", ["A", "szabad", "társadalom", "alapja", "az", "adott", "szó", "és", "a", "becsület."], ["A", "szabad", "társadalom", "alapja", "az", "adott", "szó", "és", "a", "becsület."], "The foundation of free society is the given word and honor.", ["c1-eu-harmonization"]),
                sw("production", [{"prompt": "Synthesize Sándor Márai's philosophy of contractual morality.", "answer": "Márai felfogásában a szerződéses hűség a polgári civilizáció gerince: az a képesség, hogy az ember külső kényszer nélkül, önbecsülésből és a másik iránti tiszteletből tartja be ígéreteit."}], ["c1-eu-harmonization"]),
                mc("grammar", "check", "Melyik állítás foglalja össze legméltóbban Márai polgári tanítását?", [
                    "Az igazi jogállamiság fundamentuma a polgárok személyes becsületében és az ígéretek megtartásában gyökerezik.",
                    "A törvényeket csak addig kell betartani, amíg látja a rendőr.",
                    "A pénz felülír minden erkölcsi kötelességet."
                ], 0, ["c1-eu-harmonization"])
            ]
        }
    ]

    for l in core_lessons:
        emit_instructional_lesson(10, "core", l, core_title, core_intro if l["num"] == 1 else None)

    # Core Consolidation
    emit_consolidation_lesson(
        10,
        "core",
        "c1-10-consolidation",
        core_title,
        [
            "I can draft operative contractual covenants (kölcsönösen megállapodnak, kötelezettséget vállal).",
            "I can employ commercial negotiation hedging, counter-offers, and diplomatic firmness.",
            "I can structure force majeure liability disclaimers and evaluate Márai's bourgeois ethos."
        ],
        [
            mc("grammar", "recognize", "Melyik záradék biztosítja, hogy egy pont érvénytelensége ne rontsa le a teljes szerződést?", [
                "érvénytelenségi / részleges érvénytelenségi záradék",
                "székhely-áthelyezési záradék",
                "titoktartási kötelezettségvállalás"
            ], 0, ["c1-contractual-stipulations"]),
            mc("grammar", "recognize", "Milyen jogi következménnyel jár a 'vis maior' esemény?", [
                "Mentesíti a felet a késedelmi felelősség és kártérítés alól elháríthatatlan külső ok miatt.",
                "Megduplázza a fizetendő vételárat.",
                "Azonnal megszünteti a cég működését."
            ], 0, ["c1-liability-exemption"]),
            match("vocabulary", "recognize", [["kölcsönösen megállapodnak", "mutually agree"], ["vis maior", "force majeure"], ["tárgyalási alap", "negotiation basis"], ["közgyűlés", "general meeting"], ["polgári ethosz", "civic ethos"]], ["c1-10-vocab"]),
            fb("vocabulary", "recall", "A jelen szerződés mellékletei annak elválaszthatatlan részét _____. (form / képezik)", "képezik", "The annexes of the present contract form an inseparable part thereof.", ["c1-10-vocab"]),
            fb("vocabulary", "recall", "A polgári világ legfőbb alapköve az adott szó _____. (sanctity / szentsége)", "szentsége", "The chief cornerstone of the bourgeois world is the sanctity of the given word.", ["c1-10-vocab"]),
            fb("grammar", "recall", "A felek jogvitáikat elsődlegesen békés tárgyalások _____ kísérlik meg rendezni. (via / útján)", "útján", "The parties attempt to settle their legal disputes primarily via peaceful negotiations.", ["c1-contractual-stipulations"]),
            fb("grammar", "context", "A cég kizárólag volumenkedvezmény biztosítása esetén mutat _____ a szerződéskötésre. (willingness / hajlandóságot)", "hajlandóságot", "The company shows willingness to contract solely in case of granting volume discount.", ["c1-negotiation-hedging"]),
            fb("grammar", "context", "A jogszabály tiltja a szándékos károkozásért való felelősség előzetes _____. (exclusion / kizárását)", "kizárását", "Statutory law prohibits prior exclusion of liability for intentional harm.", ["c1-liability-exemption"]),
            mc("grammar", "context", "Melyik állítás fogalmaz meg diplomáciai tárgyalási finomítást (hedging)?", [
                "Bár az ajánlat érdekes, jelenlegi formájában kizárólag a szállítási feltételek átdolgozása esetén tudjuk elfogadni.",
                "Nem kell nekünk ez az áru, vigyék vissza.",
                "Adják ide ingyen, és akkor meggondoljuk."
            ], 0, ["c1-negotiation-hedging"]),
            sb("grammar", "produce", ["A", "szerződéses", "hűség", "az", "emberi", "méltóság", "és", "a", "becsület", "próbája."], ["A", "szerződéses", "hűség", "az", "emberi", "méltóság", "és", "a", "becsület", "próbája."], "Contractual fidelity is the test of human dignity and honor.", ["c1-eu-harmonization"]),
            sw("production", [{"prompt": "Draft a formal contractual severability clause in Hungarian.", "answer": "Amennyiben a jelen szerződés bármely rendelkezése érvénytelennek bizonyulna, az nem érinti a fennmaradó rendelkezések érvényességét és hatályát."}], ["c1-contractual-stipulations"]),
            sw("production", [{"prompt": "Synthesize Sándor Márai's view on contracts and civic responsibility.", "answer": "Márai szerint a polgári társadalom nem a paragrafusok rideg szigorán, hanem az adott szó szentségén és az egyén belső erkölcsi mércéjén nyugszik."}], ["c1-eu-harmonization"])
        ]
    )

    # ----------------------------------------------------
    # TRACK 2: DISCOURSE (c1-szerzodesek)
    # ----------------------------------------------------
    slug = "szerzodesek"
    disc_intro = [
        "In a globalized economy, Hungarian commercial negotiation and corporate law operate at the intersection of civil law doctrine, EU regulatory harmonization, and Anglo-American contractual drafting conventions.",
        "In this unit, you will examine Hungarian corporate jurisprudence: cross-border M&A transactions, venture capital term sheets, competition law (Gazdasági Versenyhivatal), public procurement integrity, and the harmonization of domestic business law with the EU Single Market."
    ]

    disc_lessons = [
        {
            "num": 1,
            "stem": f"c1-{slug}-01",
            "title": "Corporate Mergers, Acquisitions and Due Diligence",
            "grammar_title": "M&A Transactions: Due Diligence, Warranties, and Share Purchases",
            "grammar_skill": "c1-corporate-governance",
            "goals": [
                "I can navigate Hungarian corporate acquisition terminology (*felvásárlás, fúzió, átvilágítás*).",
                "I can evaluate legal due diligence reports (*jogi átvilágítás, szavatossági nyilatkozatok*).",
                "I can draft share purchase agreement covenants (*üzletrész-adásvételi szerződés*)."
            ],
            "vocab": [
                {"lemma": "cégfelvásárlás", "translation": "company acquisition, takeover", "pos": "noun"},
                {"lemma": "jogi átvilágítás", "translation": "legal due diligence", "pos": "noun"},
                {"lemma": "üzletrész-adásvételi szerződés", "translation": "share / quota purchase agreement (SPA)", "pos": "noun"},
                {"lemma": "szavatossági nyilatkozat", "translation": "representations and warranties", "pos": "noun"},
                {"lemma": "zárási feltétel", "translation": "condition precedent to closing", "pos": "noun"},
                {"lemma": "titoktartási megállapodás", "translation": "non-disclosure agreement (NDA)", "pos": "noun"},
                {"lemma": "vételár-kiigazítás", "translation": "purchase price adjustment", "pos": "noun"},
                {"lemma": "letéti számla", "translation": "escrow account", "pos": "noun"}
            ],
            "gr_text1": "Cross-border M&A deals in Hungary combine domestic Civil Code rules with international drafting styles. Before signing an SPA (*üzletrész-adásvételi szerződés*), buyers conduct thorough *jogi és pénzügyi átvilágítás* (due diligence).",
            "gr_text2": "Sellers provide exhaustive *szavatossági nyilatkozatok* (representations and warranties) regarding tax liabilities, intellectual property, and litigation, with part of the purchase price held in an escrow account (*letéti számla*).",
            "gr_table": [
                ["A jogi átvilágítás feltárta a társaság rejtett kötelezettségeit...", "Legal due diligence uncovered the company's hidden liabilities..."],
                ["Szavatossági nyilatkozatok tétele a permentességről...", "Giving representations and warranties regarding freedom from litigation..."],
                ["A vételár letéti számlára történő utalása a záráskor...", "Transferring the purchase price to an escrow account at closing..."]
            ],
            "world_story_seg": {
                "seg_slug": "cegfelvasarlas",
                "title": "A tárgyalóasztaltól a zárásig: a vállalati átvilágítás világa",
                "summary": "How international investors and Hungarian corporate lawyers navigate high-stakes mergers and acquisitions.",
                "paragraphs": [
                    {"type": "narration", "text": "Amikor egy nemzetközi befektető úgy dönt, hogy felvásárol egy ígéretes magyar technológiai középvállalatot, a tárgyalások nem az pezsgőbontással kezdődnek, hanem hónapokig tartó kíméletlen vizsgálattal. A jogi és pénzügyi átvilágítás (due diligence) során ügyvédek és könyvvizsgálók hada fésüli át a cég teljes történetét: a munkaszerződésektől az adóbevallásokon át a szellemi tulajdonjogokig."},
                    {"type": "narration", "text": "Az üzletrész-adásvételi szerződés (SPA) megkötése a jogi precizitás csúcsteljesítménye. Az eladónak részletes szavatossági nyilatkozatokat kell tennie a társaság tehermentességéről, miközben a vevő zárási feltételekhez és letéti számlához köti a kifizetést. Egyetlen elhallgatott peres ügy vagy elmaradt környezetvédelmi engedély millió eurós kártérítési kötelezettséget vonhat maga után a felek számára."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Mi a célja a 'jogi átvilágításnak' (due diligence) egy cégfelvásárlás előtt?", ["A céget érintő jogi, adózási és pénzügyi kockázatok alapos feltárása a vételár meghatározásához.", "A cég logójának újratervezése.", "Az alkalmazottak azonnali elbocsátása."], 0, ["c1-szerzodesek-vocab"]),
                fb("grammar", "controlled", "A vevő védelmében a vételár egy részét ügyvédi letéti _____ helyezték el a zárásig. (account / számlán)", "számlán", "In defense of the buyer a portion of the purchase price was deposited in a legal escrow account until closing.", ["c1-corporate-governance"]),
                match("vocabulary", "controlled", [["cégfelvásárlás", "company acquisition"], ["jogi átvilágítás", "legal due diligence"], ["letéti számla", "escrow account"], ["szavatossági nyilatkozat", "representations and warranties"]], ["c1-szerzodesek-vocab"]),
                sb("grammar", "practice", ["A", "szavatossági", "nyilatkozatok", "valódiságáért", "az", "eladó", "anyagi", "felelősséget", "vállal."], ["A", "szavatossági", "nyilatkozatok", "valódiságáért", "az", "eladó", "anyagi", "felelősséget", "vállal."], "The seller undertakes financial liability for the veracity of representations and warranties.", ["c1-corporate-governance"]),
                sw("production", [{"prompt": "Explain the role of representations and warranties in an M&A contract.", "answer": "A szavatossági nyilatkozatok biztosítják a vevőt arról, hogy a társaság nem rendelkezik eltitkolt adósságokkal vagy peres ügyekkel, megszegésük esetén közvetlen kártalanítási igényt alapozva meg."}], ["c1-corporate-governance"]),
                mc("grammar", "check", "Mikor kerül sor a tulajdonjog tényleges átszállására egy felvásárlásnál?", [
                    "A zárási feltételek teljesülése és a vételár megfizetése után, a cégbírósági bejegyzéssel.",
                    "Amikor a felek először találkoznak egy étteremben.",
                    "Kizárólag a miniszter személyes engedélyével."
                ], 0, ["c1-corporate-governance"])
            ]
        },
        {
            "num": 2,
            "stem": f"c1-{slug}-02",
            "title": "Venture Capital, Startups and Term Sheets",
            "grammar_title": "Startup Investment Instruments: Liquidation Preference and Vesting",
            "grammar_skill": "c1-corporate-governance",
            "goals": [
                "I can analyze venture capital financing terms in Hungarian (*kockázati tőkebevonás, befektetési szindikátus*).",
                "I can evaluate term sheet clauses (*likvidációs preferencia, alapítói zárolás / vesting, hígulásvédelem*).",
                "I can draft investment negotiations between founders and institutional venture funds."
            ],
            "vocab": [
                {"lemma": "kockázati tőke", "translation": "venture capital (VC)", "pos": "noun"},
                {"lemma": "term sheet", "translation": "term sheet / befektetési feltétellevél", "pos": "noun"},
                {"lemma": "likvidációs preferencia", "translation": "liquidation preference", "pos": "noun"},
                {"lemma": "hígulásvédelem", "translation": "anti-dilution protection", "pos": "noun"},
                {"lemma": "alapítói zárolás", "translation": "vesting (founder share lock-up)", "pos": "noun"},
                {"lemma": "szindikátusi szerződés", "translation": "shareholders' agreement (SHA)", "pos": "noun"},
                {"lemma": "kivásárlás", "translation": "buyout / exit", "pos": "noun"},
                {"lemma": "értékelés", "translation": "valuation (pre-money / post-money)", "pos": "noun"}
            ],
            "gr_text1": "The Hungarian startup ecosystem relies on venture capital funding (*kockázati tőkebevonás*). Negotiations start with a non-binding *term sheet* outlining the core economic and governance parameters.",
            "gr_text2": "Key protection mechanisms include *likvidációs preferencia* (investors get paid first in an exit) and *hígulásvédelem* (protecting equity percentage in down-rounds), formalized in a binding *szindikátusi szerződés* (shareholders' agreement).",
            "gr_table": [
                ["A kockázati tőkebefektető szindikátusi szerződésben rögzíti jogait...", "The venture capital investor records rights in a shareholders' agreement..."],
                ["Likvidációs preferencia biztosítása az alapítói kifizetések előtt...", "Securing liquidation preference prior to founder payouts..."],
                ["Négyéves alapítói zárolás (vesting) a csapat elkötelezettségének megőrzésére...", "Four-year founder vesting to preserve team commitment..."]
            ],
            "world_story_seg": {
                "seg_slug": "kockazatitoke",
                "title": "A startup álomtól a kockázati tőkéig",
                "summary": "How Hungarian technology innovators and venture capital funds negotiate valuation and control in shareholders' agreements.",
                "paragraphs": [
                    {"type": "narration", "text": "Budapest kávéházaiból és egyetemi inkubátoraiból az elmúlt évtizedben globális sikertörténetek indultak el. Amikor egy feltörekvő magyar szoftveres cég eléri azt a növekedési fázist, ahol a nemzetközi terjeszkedéshez milliókra van szükség, belépnek a kockázati tőkebefektetők (VC). A befektetési feltétellevél (term sheet) aláírása azonban csak a kezdet."},
                    {"type": "narration", "text": "Az alapítók és a befektetők közötti szindikátusi szerződés a hatalom finom megosztásáról szól. A tőkebefektető nemcsak pénzt hoz, hanem szigorú garanciákat kér: likvidációs preferenciát eladás esetén, vétójogokat a stratégiai döntésekben és hígulásvédelmet jövőbeli tőkeemelések idejére. Az alapítók számára a siker záloga a jó megállapodás: megőrizni az irányítást, miközben a tőke segítségével világhódító útra indítják innovációjukat."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Mit garantál a 'likvidációs preferencia' a kockázati tőkebefektetőnek?", ["Hogy a cég eladásakor vagy felszámolásakor a befektető a pénzéhez jusson az alapítók előtt.", "Hogy a befektető ingyen kávézhat a cégnél.", "Hogy nem kell adót fizetnie a nyereség után."], 0, ["c1-szerzodesek-vocab"]),
                fb("grammar", "controlled", "A felek közötti szindikátusi szerződés négyéves alapítói _____ ír elő az elvándorlás megakadályozására. (vesting / zárolást)", "zárolást", "The shareholders' agreement between parties prescribes a four-year founder vesting to prevent departure.", ["c1-corporate-governance"]),
                match("vocabulary", "controlled", [["kockázati tőke", "venture capital"], ["term sheet", "investment term sheet"], ["szindikátusi szerződés", "shareholders' agreement"], ["hígulásvédelem", "anti-dilution"]], ["c1-szerzodesek-vocab"]),
                sb("grammar", "practice", ["A", "befektető", "vétójogot", "kérhet", "a", "társaság", "legfontosabb", "stratégiai", "döntéseiben."], ["A", "befektető", "vétójogot", "kérhet", "a", "társaság", "legfontosabb", "stratégiai", "döntéseiben."], "The investor may request veto rights in the company's most important strategic decisions.", ["c1-corporate-governance"]),
                sw("production", [{"prompt": "Explain why founder vesting is essential in venture capital deals.", "answer": "Az alapítói zárolás (vesting) biztosítja, hogy a kulcsemberek elkötelezettek maradjanak a cég mellett; idő előtti távozás esetén elveszítik a még fel nem szabadult részvényeiket."}], ["c1-corporate-governance"]),
                mc("grammar", "check", "Mi képezi a pre-money és post-money értékelés közötti különbséget?", [
                    "A pre-money értékelés a cég értéke a tőkebevonás előtt, míg a post-money magában foglalja a frissen befektetett tőkét is.",
                    "Semmi, a két szó szinonima.",
                    "A pre-money az adót jelenti, a post-money a nettó profitot."
                ], 0, ["c1-corporate-governance"])
            ]
        },
        {
            "num": 3,
            "stem": f"c1-{slug}-03",
            "title": "Competition Law, Cartels and Regulatory Antitrust: GVH",
            "grammar_title": "Antitrust Compliance: Abuse of Dominant Position and Market Mergers",
            "grammar_skill": "c1-eu-harmonization",
            "goals": [
                "I can navigate Hungarian and EU antitrust terminology (*kartelltilalom, erőfölénnyel való visszaélés*).",
                "I can analyze the regulatory powers of the Hungarian Competition Authority (*Gazdasági Versenyhivatal / GVH*).",
                "I can formulate corporate antitrust compliance strategies and leniency applications (*engedékenységi politika*)."
            ],
            "vocab": [
                {"lemma": "Gazdasági Versenyhivatal", "translation": "Hungarian Competition Authority (GVH)", "pos": "noun"},
                {"lemma": "kartelltilalom", "translation": "prohibition of cartels / collusive agreements", "pos": "noun"},
                {"lemma": "gazdasági erőfölény", "translation": "dominant market position", "pos": "noun"},
                {"lemma": "visszaélés az erőfölénnyel", "translation": "abuse of dominant position", "pos": "expression"},
                {"lemma": "engedékenységi politika", "translation": "leniency policy (whistleblowing cartels)", "pos": "noun"},
                {"lemma": "összefonódás", "translation": "merger / concentration of undertakings", "pos": "noun"},
                {"lemma": "versenyt korlátozó megállapodás", "translation": "anticompetitive agreement", "pos": "noun"},
                {"lemma": "versenyfelügyeleti eljárás", "translation": "competition supervision proceeding", "pos": "noun"}
            ],
            "gr_text1": "The Hungarian Competition Authority (*GVH*) enforces the prohibition of price-fixing and market-sharing cartels (*kartelltilalom*). Competitors colluding in public tenders face astronomical fines or criminal charges.",
            "gr_text2": "The *engedékenységi politika* (leniency policy) grants total immunity from fines to the first cartel member that uncovers the illegal agreement and hands over evidence to the authority.",
            "gr_table": [
                ["A Gazdasági Versenyhivatal versenyfelügyeleti eljárást indít a kartell ellen...", "The Competition Authority initiates proceedings against the cartel..."],
                ["Gazdasági erőfölénnyel való visszaélés tilalma a fogyasztók védelmében...", "Prohibition of abuse of dominant position in defense of consumers..."],
                ["Összefonódás bejelentési kötelezettsége bizonyos árbevételi küszöb felett...", "Notification obligation of merger above specific turnover thresholds..."]
            ],
            "world_story_seg": {
                "seg_slug": "versenyjog",
                "title": "A tisztességes piac őrei: a GVH és a kartellek elleni küzdelem",
                "summary": "How antitrust authorities dismantle secret price-fixing rings and ensure level playing fields in the Hungarian market.",
                "paragraphs": [
                    {"type": "narration", "text": "A szabad piacgazdaság alapja a tisztességes verseny. Amikor azonban a versenytársak a háttérben titokban megállapodnak az árak rögzítéséről vagy a piacok felosztásáról, a fogyasztók és az állam válnak a mesterségesen magasan tartott árak kárvallottjaivá. A Gazdasági Versenyhivatal (GVH) feladata a kartellek felderítése és a gazdasági erőfölénnyel való visszaélések megtorlása."},
                    {"type": "narration", "text": "A hatóság leghatékonyabb fegyvere az úgynevezett engedékenységi politika (leniency). Ez az intézmény a játékelmélet szabályai szerint működik: az a cég, amelyik elsőként feladja kartelltársait és átadja a bizonyítékokat a nyomozóknak, teljes mentességet kap a több milliárdos bírság alól. A folyamatos ellenőrzés biztosítja, hogy a magyar gazdaságban a tehetség és az innováció győzzön, ne pedig a háttéralkuk."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Hogyan ösztönzi a GVH engedékenységi politikája a kartellek leleplezését?", ["Teljes bírságkiszabási mentességet nyújtva az elsőként önként vallomást tevő kartelltag számára.", "Minden cégnek pénzjutalmat adva.", "A versenyvizsgálatok titkosításával."], 0, ["c1-szerzodesek-vocab"]),
                fb("grammar", "controlled", "A piaci szereplők közötti árrögzítő megállapodás szigorú törvényi _____ ütközik. (prohibition / kartelltilalomba)", "kartelltilalomba", "A price-fixing agreement between market actors violates strict statutory cartel prohibition.", ["c1-eu-harmonization"]),
                match("vocabulary", "controlled", [["kartelltilalom", "cartel prohibition"], ["gazdasági erőfölény", "dominant position"], ["engedékenységi politika", "leniency policy"], ["összefonódás", "merger / concentration"]], ["c1-szerzodesek-vocab"]),
                sb("grammar", "practice", ["A", "piaci", "erőfölénnyel", "való", "visszaélést", "a", "törvény", "szigorúan", "tiltja."], ["A", "piaci", "erőfölénnyel", "való", "visszaélést", "a", "törvény", "szigorúan", "tiltja."], "Abuse of market dominance is strictly prohibited by law.", ["c1-eu-harmonization"]),
                sw("production", [{"prompt": "Explain the antitrust danger of market abuse by a dominant corporation.", "answer": "A domináns helyzetben lévő vállalat kiszoríthatja a versenytársakat és indokolatlanul magas árakat kényszeríthet a fogyasztókra, ami tönkreteszi az innovációt és a piaci hatékonyságot."}], ["c1-eu-harmonization"]),
                mc("grammar", "check", "Milyen ügyekben kötelező a GVH előzetes engedélyét kérni?", [
                    "Jelentős árbevételű vállalatok összefonódása (fúziója vagy felvásárlása) esetén.",
                    "Ha egy cég új irodaszereket vásárol.",
                    "Minden egyes új alkalmazott felvételekor."
                ], 0, ["c1-eu-harmonization"])
            ]
        },
        {
            "num": 4,
            "stem": f"c1-{slug}-04",
            "title": "Public Procurement Integrity and Legal Remedies",
            "grammar_title": "Public Procurement Law: Bidding, Challenges, and KDB Review",
            "grammar_skill": "c1-corporate-governance",
            "goals": [
                "I can analyze public procurement tender regulations (*közbeszerzési eljárás, ajánlattétel*).",
                "I can navigate procurement dispute arbitration before the Public Procurement Arbitration Board (*Közbeszerzési Döntőbizottság / KDB*).",
                "I can articulate anti-corruption compliance in state and municipal tenders."
            ],
            "vocab": [
                {"lemma": "közbeszerzési eljárás", "translation": "public procurement proceeding", "pos": "noun"},
                {"lemma": "ajánlati felhívás", "translation": "call for tenders, invitation to tender", "pos": "noun"},
                {"lemma": "ajánlattevő", "translation": "tenderer, bidder", "pos": "noun"},
                {"lemma": "Közbeszerzési Döntőbizottság", "translation": "Public Procurement Arbitration Board (KDB)", "pos": "noun"},
                {"lemma": "jogorvoslati eljárás", "translation": "remedy proceeding, appeal process", "pos": "noun"},
                {"lemma": "aránytalanul alacsony ár", "translation": "abnormally low tender price", "pos": "noun"},
                {"lemma": "összeférhetetlenségi nyilatkozat", "translation": "declaration of non-conflict of interest", "pos": "noun"},
                {"lemma": "támogatói szerződés", "translation": "grant / subsidy agreement", "pos": "noun"}
            ],
            "gr_text1": "Public procurement (*közbeszerzés*) governs billions in state and EU expenditures. Contracting authorities must ensure transparency, equal treatment, and fair competition in tender specifications (*ajánlati felhívás*).",
            "gr_text2": "Aggrieved bidders initiate review before the *Közbeszerzési Döntőbizottság (KDB)*. The KDB may suspend the procedure, annul unlawful decisions, or impose severe fines on infringing contracting authorities.",
            "gr_table": [
                ["Ajánlattétel benyújtása az elektronikus közbeszerzési rendszerben (EKR)...", "Submitting bids in the electronic public procurement system (EKR)..."],
                ["Jogorvoslati kérelem benyújtása a Közbeszerzési Döntőbizottsághoz...", "Filing an application for review to the Public Procurement Arbitration Board..."],
                ["A legkedvezőbb ár-érték arány elvének érvényesítése a bírálatkor...", "Enforcing the best price-quality ratio principle during evaluation..."]
            ],
            "world_story_seg": {
                "seg_slug": "kozbeszerzes",
                "title": "A közpénzek versenye: közbeszerzés és jogorvoslat",
                "summary": "How the rules of public procurement govern large state infrastructure investments and provide remedies against biased tenders.",
                "paragraphs": [
                    {"type": "narration", "text": "Amikor egy város új hidat épít, egy kórház orvosi műszereket vásárol, vagy a vasút felújítását tervezik, a megrendelő nem választhatja egyszerűen a kedvenc partnerét. A közbeszerzési törvény szigorú európai irányelvek alapján írja elő a nyilvános pályáztatást, az esélyegyenlőséget és az ajánlattevők egyenlő elbírálását az Elektronikus Közbeszerzési Rendszerben (EKR)."},
                    {"type": "narration", "text": "Ha egy pályázó úgy érzi, hogy a kiírást egyetlen kiválasztott cégre szabták, vagy a bírálóbizottság jogszerűtlenül zárta ki ajánlatát, a Közbeszerzési Döntőbizottsághoz (KDB) fordulhat jogorvoslatért. A testület gyorsított eljárásban vizsgálja felül a döntéseket, és jogosult felfüggeszteni az eljárást, vagy akár megsemmisíteni az eredményt. A tiszta verseny a közpénzek védelmének egyetlen garanciája."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Melyik testület bírálja el a közbeszerzési eljárásokban felmerülő vitákat Magyarországon?", ["A Közbeszerzési Döntőbizottság (KDB).", "A helyi önkormányzat sportbizottsága.", "A vasúti pénztár."], 0, ["c1-szerzodesek-vocab"]),
                fb("grammar", "controlled", "A jogsérelemre hivatkozó ajánlattevő jogorvoslati _____ terjesztett a Közbeszerzési Döntőbizottság elé. (application / kérelmet)", "kérelmet", "The bidder citing infringement submitted an application for remedy before the Public Procurement Arbitration Board.", ["c1-corporate-governance"]),
                match("vocabulary", "controlled", [["közbeszerzési eljárás", "public procurement proceeding"], ["ajánlattevő", "tenderer / bidder"], ["ajánlati felhívás", "call for tenders"], ["összeférhetetlenségi nyilatkozat", "conflict of interest declaration"]], ["c1-szerzodesek-vocab"]),
                sb("grammar", "practice", ["A", "közbeszerzésben", "minden", "pályázót", "egyenlő", "bánásmód", "illet", "meg."], ["A", "közbeszerzésben", "minden", "pályázót", "egyenlő", "bánásmód", "illet", "meg."], "In public procurement every applicant is entitled to equal treatment.", ["c1-corporate-governance"]),
                sw("production", [{"prompt": "Describe the main goal of public procurement legislation.", "answer": "A közbeszerzési jog célja a közpénzek észszerű és átlátható felhasználása, a tisztességes verseny biztosítása és a korrupció megelőzése az állami beszerzésekben."}], ["c1-corporate-governance"]),
                mc("grammar", "check", "Mi a következménye annak, ha egy ajánlattevő aránytalanul alacsony árat ad meg indoklás nélkül?", [
                    "A hatóság kizárhatja az ajánlatot, ha az ár nem biztosítja a szerződésszerű teljesítést.",
                    "Azonnal meg kell nyernie a pályázatot.",
                    "A törvény tiltja a pályázatok kizárását."
                ], 0, ["c1-corporate-governance"])
            ]
        },
        {
            "num": 5,
            "stem": f"c1-{slug}-05",
            "title": "Cross-Border Commercial Transactions and EU Single Market",
            "grammar_title": "Private International Law: Choice of Law, Rome I, and Brussels Ibis",
            "grammar_skill": "c1-eu-harmonization",
            "goals": [
                "I can analyze private international law in Hungarian commercial contracts (*nemzetközi magánjog*).",
                "I can apply EU choice-of-law and jurisdictional rules (*jogválasztás / Róma I, joghatóság / Brüsszel Ia*).",
                "I can evaluate international commercial arbitration (*választottbíráskodás / MKIK*)."
            ],
            "vocab": [
                {"lemma": "nemzetközi magánjog", "translation": "private international law / conflict of laws", "pos": "noun"},
                {"lemma": "jogválasztás", "translation": "choice of law", "pos": "noun"},
                {"lemma": "joghatóság", "translation": "jurisdiction of courts", "pos": "noun"},
                {"lemma": "választottbíróság", "translation": "arbitration court / tribunal", "pos": "noun"},
                {"lemma": "választottbírósági kikötés", "translation": "arbitration clause", "pos": "noun"},
                {"lemma": "kollíziós szabály", "translation": "conflict rule / choice-of-law rule", "pos": "noun"},
                {"lemma": "végrehajthatóság", "translation": "enforceability", "pos": "noun"},
                {"lemma": "uniós belső piac", "translation": "EU single / internal market", "pos": "noun"}
            ],
            "gr_text1": "Cross-border commercial agreements require explicit conflict-of-law provisions under EU Regulation Rome I: *A felek a jelen szerződésre és abból eredő jogvitákra a magyar anyagi jogot kötik ki.*",
            "gr_text2": "To avoid slow state litigation, international commercial partners frequently agree on an arbitration clause (*választottbírósági kikötés*) assigning disputes to the Permanent Arbitration Court attached to the Hungarian Chamber of Commerce (*MKIK*).",
            "gr_table": [
                ["A felek a magyar jog alkalmazását kötik ki a szerződésben.", "The parties stipulate the application of Hungarian law in the contract."],
                ["A jogviták eldöntésére a Kereskedelmi Választottbíróság illetékes.", "The Commercial Court of Arbitration has jurisdiction to resolve disputes."],
                ["Az uniós joghatósági szabályok közvetlen alkalmazandósága...", "Direct applicability of EU jurisdictional rules..."]
            ],
            "world_story_seg": {
                "seg_slug": "nemzetkozimaganjog",
                "title": "Határok nélkül: a nemzetközi kereskedelmi jog világa",
                "summary": "How cross-border trade, EU single market regulations, and international commercial arbitration unite global business with Hungarian law.",
                "paragraphs": [
                    {"type": "narration", "text": "Az Európai Unió belső piacán az áruk, a szolgáltatások és a tőke szabad mozgása mindennapos valósággá tette a határokon átnyúló üzleti kapcsolatokat. Amikor egy budapesti szoftverfejlesztő cég egy holland multinacionális vállalattal és egy lengyel logisztikai partnerrel köt szerződést, az elsődleges kérdés nemcsak a vételár, hanem a jogi keret: melyik ország törvényei irányadók vita esetén, és melyik bíróság jogosult eljárni?"},
                    {"type": "narration", "text": "Az uniós Róma I. és Brüsszel Ia. rendeletek megadják a feleknek a jogválasztás (choice of law) szabadságát. A nemzetközi kereskedelemben azonban az állami bíróságok helyett egyre gyakrabban a Magyar Kereskedelmi és Iparkamara mellett működő Állandó Választottbíróságot jelölik ki. A választottbíráskodás gyors, diszkrét, és a New York-i Egyezmény révén döntései a világ szinte minden országában közvetlenül végrehajthatók, biztosítva a nemzetközi üzlet zavartalan működését."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Miért részesítik előnyben a nemzetközi cégek a választottbíráskodást az állami bíróságokkal szemben?", ["Mert gyorsabb, a bírák szakértők a gazdasági életben, és a döntések nemzetközileg közvetlenül végrehajthatók.", "Mert a választottbíróság ingyenes.", "Mert a választottbíróságokon nincsenek törvények."], 0, ["c1-szerzodesek-vocab"]),
                fb("grammar", "controlled", "A szerződő felek a jogviták elbírálására a magyar anyagi _____ alkalmazását kötik ki. (law / jogot)", "jogot", "The contracting parties stipulate the application of Hungarian substantive law for adjudicating legal disputes.", ["c1-eu-harmonization"]),
                match("vocabulary", "controlled", [["nemzetközi magánjog", "private international law"], ["jogválasztás", "choice of law"], ["választottbíróság", "arbitration court"], ["végrehajthatóság", "enforceability"]], ["c1-szerzodesek-vocab"]),
                sb("grammar", "practice", ["A", "felek", "szabadon", "választhatják", "meg", "a", "szerződésükre", "irányadó", "nemzeti", "jogot."], ["A", "felek", "szabadon", "választhatják", "meg", "a", "szerződésükre", "irányadó", "nemzeti", "jogot."], "The parties may freely choose the national law governing their contract.", ["c1-eu-harmonization"]),
                sw("production", [{"prompt": "Draft a standard international choice-of-law and arbitration clause.", "answer": "A jelen szerződésre a magyar jog az irányadó. A felek a szerződésből eredő vitás kérdéseket a Magyar Kereskedelmi és Iparkamara mellett működő Választottbíróság kizárólagos hatáskörébe utalják."}], ["c1-eu-harmonization"]),
                mc("grammar", "check", "Melyik uniós rendelet szabályozza a szerződéses kötelezettségekre alkalmazandó jogot?", [
                    "A Róma I. rendelet.",
                    "A lisszaboni szerződés agrárfejezete.",
                    "A schengeni határőrizeti szabályzat."
                ], 0, ["c1-eu-harmonization"])
            ]
        }
    ]

    for l in disc_lessons:
        emit_instructional_lesson(10, "discourse", l, disc_title, disc_intro if l["num"] == 1 else None)

    # Combined world story
    write_json(
        f"stories/world/c1/{slug}.json",
        {
            "id": f"story.c1.world.{slug}",
            "title": "A gazdasági jog, a szerződések és a nemzetközi piac krónikája",
            "level": "C1",
            "type": "world",
            "summary": "Comprehensive chronicle of Hungarian commercial transactions and corporate law: M&A due diligence, startup venture capital term sheets, antitrust competition authority (GVH), public procurement integrity, and cross-border private international law.",
            "paragraphs": [
                {"type": "narration", "text": "A modern piacgazdaság vérkeringését a szerződések milliárdos hálózata és a vállalati jog szigorú szabályrendszere működteti. Magyarországon az uniós csatlakozás óta a hazai polgári jogi hagyomány szervesen ötvöződött a nemzetközi kereskedelmi gyakorlattal."},
                {"type": "narration", "text": "A vállalatfelvásárlások világában a jogi átvilágítás és az üzletrész-adásvételi szerződések szavatossági rendszere garantálja a befektetések biztonságát, míg a startup ökoszisztémában a kockázati tőke szindikátusi szerződései adnak szárnyakat a technológiai innovációnak."},
                {"type": "narration", "text": "A tisztességes piaci versenyt a Gazdasági Versenyhivatal (GVH) szigorú kartellüldözése védi, miközben a közbeszerzési eljárások és a Döntőbizottság ellenőrzése a közpénzek átlátható és esélyegyenlő felhasználását biztosítják."},
                {"type": "narration", "text": "A határokon átnyúló nemzetközi ügyletekben a Róma I. rendelet szerinti jogválasztás és a kereskedelmi választottbíráskodás teremti meg azt a jogbiztonságot, amely nélkülözhetetlen a globális gazdasági integrációban."},
                {"type": "narration", "text": "Ez a sokrétű gazdasági jogi architektúra Márai Sándor polgári eszményének modern folytatása: bizonyíték arra, hogy a gazdasági prosperitás és a polgári szabadság legbiztosabb alapköve az adott szó tisztelete, a szerződéses hűség és a megkérdőjelezhetetlen jogbiztonság."}
            ]
        }
    )

    # Discourse Consolidation
    emit_consolidation_lesson(
        10,
        "discourse",
        f"c1-{slug}-consolidation",
        disc_title,
        [
            "I can navigate corporate M&A transactions, legal due diligence, and share purchase agreements.",
            "I can evaluate venture capital term sheets, shareholder covenants, and antitrust rules (GVH).",
            "I can analyze public procurement integrity and private international commercial law (Rome I, arbitration)."
        ],
        [
            mc("grammar", "recognize", "Mi a célja a jogi átvilágításnak (due diligence) cégfelvásárlás előtt?", [
                "A céget érintő jogi, adózási és pénzügyi kockázatok alapos felderítése.",
                "A céges iroda bútorainak felújítása.",
                "A tulajdonosok azonnali leváltása."
            ], 0, ["c1-corporate-governance"]),
            mc("grammar", "recognize", "Mit tilt a kartelltilalom a versenyjogban?", [
                "A versenytársak közötti titkos árrögzítő és piacfelosztó megállapodásokat.",
                "A jó minőségű termékek gyártását.",
                "A reklámok közzétételét."
            ], 0, ["c1-eu-harmonization"]),
            match("vocabulary", "recognize", [["cégfelvásárlás", "company acquisition"], ["term sheet", "investment term sheet"], ["kartelltilalom", "cartel prohibition"], ["közbeszerzési eljárás", "public procurement"], ["választottbíróság", "arbitration court"]], ["c1-szerzodesek-vocab"]),
            fb("vocabulary", "recall", "A startup befektetésnél a szindikátusi szerződés négyéves alapítói _____ ír elő. (vesting / zárolást)", "zárolást", "In startup investments the shareholders' agreement prescribes a four-year founder vesting.", ["c1-szerzodesek-vocab"]),
            fb("vocabulary", "recall", "A jogsértést észlelő pályázó a Közbeszerzési _____ fordulhat jogorvoslatért. (Arbitration Board / Döntőbizottsághoz)", "Döntőbizottsághoz", "The applicant noticing infringement may turn to the Public Procurement Arbitration Board for remedy.", ["c1-szerzodesek-vocab"]),
            fb("grammar", "recall", "A nemzetközi ügyletekben a felek szabadon dönthetnek az alkalmazandó _____ kérdésében. (choice of law / jogválasztás)", "jogválasztás", "In international transactions parties may freely decide on the matter of choice of law.", ["c1-eu-harmonization"]),
            fb("grammar", "context", "A Gazdasági Versenyhivatal engedékenységi politikája teljes _____ nyújt a kartellt elsőként leleplező cégnek. (immunity / mentességet)", "mentességet", "The Competition Authority's leniency policy grants total immunity to the company first uncovering the cartel.", ["c1-eu-harmonization"]),
            fb("grammar", "context", "A nemzetközi választottbírósági döntések világszerte közvetlenül _____ hajthatók végre. (can be executed / hajthatók)", "hajthatók", "International arbitration decisions can be executed directly worldwide.", ["c1-eu-harmonization"]),
            mc("grammar", "context", "Melyik állítás foglalja össze legmélyebben a gazdasági jog szerepét?", [
                "A kiszámítható, átlátható szerződéses jog és a tisztességes verseny a gazdasági fejlődés és polgári jólét záloga.",
                "A jog csak feleslegesen lassítja a gyors üzletkötéseket.",
                "A legjobb gazdaság az, ahol nincsenek szerződések."
            ], 0, ["c1-corporate-governance"]),
            sb("grammar", "produce", ["A", "tisztességes", "piaci", "verseny", "és", "a", "szerződéses", "hűség", "egymást", "erősíti."], ["A", "tisztességes", "piaci", "verseny", "és", "a", "szerződéses", "hűség", "egymást", "erősíti."], "Fair market competition and contractual fidelity reinforce each other.", ["c1-eu-harmonization"]),
            sw("production", [{"prompt": "Write a short evaluation of the role of arbitration in international commercial trade.", "answer": "A választottbíráskodás a nemzetközi kereskedelem sarokköve: gyors és professzionális vitarendezést biztosít, miközben döntései a New York-i Egyezmény alapján globálisan végrehajthatók."}], ["c1-eu-harmonization"]),
            sw("production", [{"prompt": "Formulate a concluding thought on contractual ethics in business.", "answer": "A modern gazdasági siker nem a jogi kiskapuk kijátszásában, hanem a megbízhatóságban, az adott szó tiszteletében és a hosszú távú kölcsönös bizalom kiépítésében rejlik."}], ["c1-corporate-governance"])
        ]
    )
    print("=== Finished C1 Unit 10 ===")


if __name__ == "__main__":
    generate_unit_10()
