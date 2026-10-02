#!/usr/bin/env python3
"""
Hungarian C1 Block 2 - Unit 08 Generator:
  - Track 1 (Core): Unit 8 — "Institutional Impersonalization & Passive Avoidance" (c1-08)
  - Track 2 (Discourse): Unit 8 — "Public Administration, Transparency & Civic Redress" (c1-kozszolgalat)
"""

import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT))

from scripts.c1_block1.common import mc, match, fb, sb, dc, sw, write_json, emit_instructional_lesson, emit_consolidation_lesson
from scripts.c1_block2.registry_helper import register_unit


def generate_unit_8():
    print("=== Generating C1 Unit 8 ===")
    
    # Register skills & titles
    new_skills = {
        "c1-08-vocab": {"kind": "vocabulary"},
        "c1-kozszolgalat-vocab": {"kind": "vocabulary"},
        "c1-passive-avoidance": {"kind": "grammar"},
        "c1-action-nominalization": {"kind": "grammar"},
        "c1-bureaucratic-distancing": {"kind": "grammar"},
        "c1-administrative-remedy": {"kind": "grammar"},
        "c1-civic-transparency": {"kind": "grammar"},
    }
    new_titles = {
        "c1-08-vocab": "reading",
        "c1-kozszolgalat-vocab": "reading",
        "c1-passive-avoidance": "institutional passive avoidance with kerul and nominal structures",
        "c1-action-nominalization": "dense action nominalizations with as es in bureaucratic prose",
        "c1-bureaucratic-distancing": "bureaucratic distancing and official administrative formulations",
        "c1-administrative-remedy": "administrative litigation and civic redress procedural framing",
        "c1-civic-transparency": "freedom of information public administration transparency discourse",
    }
    
    core_title = "Institutional Impersonalization & Passive Avoidance"
    core_stems = [f"c1-08-0{i}" for i in range(1, 6)] + ["c1-08-consolidation"]
    disc_title = "Public Administration, Transparency & Civic Redress"
    disc_stems = [f"c1-kozszolgalat-0{i}" for i in range(1, 6)] + ["c1-kozszolgalat-consolidation"]
    
    register_unit(8, core_title, core_stems, disc_title, disc_stems, new_skills, new_titles)

    # ----------------------------------------------------
    # TRACK 1: CORE (c1-08)
    # ----------------------------------------------------
    core_intro = [
        "Modern institutional and official Hungarian avoids passive voice morphologically, yet achieves complete syntactic impersonalization through high-register periphrastic constructions (megállapításra került, elutasításban részesült) and dense action nominalization (-ás/-és).",
        "In this unit, inspired by Kálmán Mikszáth's sharp satire of provincial bureaucracy and patronage in 'A Noszty fiú esete Tóth Marival' (1908), you will master bureaucratic passive-avoidance, agentless administrative formulations, and official decision-making registers."
    ]

    core_lessons = [
        {
            "num": 1,
            "stem": "c1-08-01",
            "title": "Periphrastic Impersonalization: 'Megállapításra került'",
            "grammar_title": "Passive Avoidance with Verbal Noun + Kerül / Részesül",
            "grammar_skill": "c1-passive-avoidance",
            "goals": [
                "I can form and parse official periphrastic passive equivalents (*megállapításra került, kihirdetésre vár*).",
                "I can manipulate recipient impersonalization using *részesül* (*támogatásban részesült*).",
                "I can distinguish between objective institutional reporting and colloquial active voice."
            ],
            "vocab": [
                {"lemma": "megállapításra került", "translation": "was established / determined", "pos": "expression"},
                {"lemma": "kihirdetésre kerül", "translation": "is promulgated / announced", "pos": "expression"},
                {"lemma": "elutasításban részesül", "translation": "receives rejection, is rejected", "pos": "expression"},
                {"lemma": "támogatásban részesül", "translation": "receives support / subsidy", "pos": "expression"},
                {"lemma": "benyújtásra került", "translation": "was submitted", "pos": "expression"},
                {"lemma": "intézkedés", "translation": "measure, action, arrangement", "pos": "noun"},
                {"lemma": "határozat", "translation": "formal decision, resolution", "pos": "noun"},
                {"lemma": "jogkövetkezmény", "translation": "legal consequence", "pos": "noun"}
            ],
            "gr_text1": "Hungarian has no widely used morphological passive in modern usage. Instead, bureaucratic and journalistic style employs the periphrastic construction *[noun in -ra/-re] + kerül*: *A törvényjavaslat benyújtásra került.* (The bill was submitted).",
            "gr_text2": "When the grammatical subject is the beneficiary or recipient of an action, the construction shifts to *[noun in -ban/-ben] + részesül*: *A kérelmező elutasításban részesült.* (The applicant was rejected).",
            "gr_table": [
                ["A határozat a mai napon kihirdetésre került.", "The resolution was promulgated today."],
                ["A projekt kiemelt állami támogatásban részesült.", "The project received highlighted state subsidy."],
                ["Az intézkedés felülvizsgálatra vár.", "The measure awaits review."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Milyen szerkezettel helyettesíti a hivatali nyelv a szenvedő szerkezetet?", ["A '-ra/-re került' fordulattal.", "A múlt idejű feltételes móddal.", "Egyszerű felkiáltó mondatokkal."], 0, ["c1-08-vocab"]),
                fb("grammar", "controlled", "A vizsgálati jelentés alapos elemzést követően elfogadásra _____. (was / került)", "került", "Following thorough analysis the investigative report was accepted.", ["c1-passive-avoidance"]),
                match("vocabulary", "controlled", [["megállapításra került", "was established"], ["elutasításban részesül", "is rejected"], ["kihirdetésre kerül", "is promulgated"], ["intézkedés", "measure / action"]], ["c1-08-vocab"]),
                fb("grammar", "practice", "A benyújtott pályázat formai hiba miatt azonnali elutasításban _____. (received / részesült)", "részesült", "The submitted tender received immediate rejection due to a formal error.", ["c1-passive-avoidance"]),
                sb("grammar", "practice", ["A", "jegyzőkönyv", "hitelesítés", "után", "irattározásra", "került."], ["A", "jegyzőkönyv", "hitelesítés", "után", "irattározásra", "került."], "Following authentication the minutes were archived.", ["c1-passive-avoidance"]),
                dc("dialogue", [
                    {"speaker": "Ügyintéző", "text": "Megszületett már a döntés a fellebbezésem ügyében?"},
                    {"speaker": "Hivatalnok", "text": "Igen, a határozat tegnap postázásra _____."},
                ], ["került", "ment", "ugrott"], 0, ["c1-passive-avoidance"]),
                sw("production", [{"prompt": "Transform the active sentence 'A bizottság elutasította a kérelmet' into official periphrastic style.", "answer": "A kérelem a bizottság részéről elutasításra került."}], ["c1-passive-avoidance"]),
                mc("grammar", "check", "Melyik mondat alkalmaz szabályos intézményi szenvedő-helyettesítő fordulatot?", [
                    "A közbeszerzési eljárás eredménye a hivatalos értesítőben közzétételre került.",
                    "A hivatal gyorsan kitette a papírt a netre tegnap.",
                    "Mindenki látta, hogy mit csináltak a pénzzel."
                ], 0, ["c1-passive-avoidance"])
            ]
        },
        {
            "num": 2,
            "stem": "c1-08-02",
            "title": "Dense Action Nominalization in Administrative Prose",
            "grammar_title": "Nominal Stacking with -ás / -és in Official Statements",
            "grammar_skill": "c1-action-nominalization",
            "goals": [
                "I can form dense action nominalizations (*-ás / -és*) with possessive modifiers.",
                "I can decode multi-tiered administrative compound nominals (*hatáskör-átruházás, vagyonnyilatkozat-tétel*).",
                "I can compress complex verbal predicates into formal administrative noun phrases."
            ],
            "vocab": [
                {"lemma": "vagyonnyilatkozat-tétel", "translation": "asset declaration submission", "pos": "noun"},
                {"lemma": "hatáskör-átruházás", "translation": "delegation of authority / jurisdiction", "pos": "noun"},
                {"lemma": "kötelezettségvállalás", "translation": "undertaking of commitment / obligation", "pos": "noun"},
                {"lemma": "döntéshozatal", "translation": "decision-making", "pos": "noun"},
                {"lemma": "helyszíni szemle", "translation": "on-site inspection", "pos": "noun"},
                {"lemma": "jegyzőkönyvvezetés", "translation": "minute-taking, recording", "pos": "noun"},
                {"lemma": "kivizsgálás", "translation": "investigation, examination", "pos": "noun"},
                {"lemma": "jogorvoslati kérelem", "translation": "application for legal remedy", "pos": "noun"}
            ],
            "gr_text1": "Hungarian administrative style ('hivatalnoknyelv') relies on transforming entire finite subordinate clauses into abstract nominal phrases headed by *-ás / -és*.",
            "gr_text2": "Compare: *Mielőtt a hatóság átruházta volna a hatáskörét...* (verbal) vs. *A hatáskör átruházását megelőzően...* (nominal). Stacking creates severe institutional gravity.",
            "gr_table": [
                ["A kötelezettségvállalás szabályszerűségének vizsgálata...", "Examination of the regularity of undertaking obligations..."],
                ["A vagyonnyilatkozat-tétel elmulasztása jogkövetkezményt von maga után.", "Failure to submit an asset declaration entails legal consequences."],
                ["A helyszíni szemle lefolytatását követően hoznak döntést.", "Following the conduct of the on-site inspection, a decision is made."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Milyen nyelvtani folyamat jellemzi a hivatali stílus mondattömörítését?", ["Az igék cselekvést kifejező főnevekké alakítása (-ás/-és képzővel).", "Melléknevek teljes elhagyása.", "Rövid tőmondatok kizárólagos használata."], 0, ["c1-08-vocab"]),
                fb("grammar", "controlled", "A panasz érdemi _____ során a szakértői véleményt is beszerezték. (investigation / kivizsgálása)", "kivizsgálása", "During the substantive investigation of the complaint the expert opinion was also obtained.", ["c1-action-nominalization"]),
                match("vocabulary", "controlled", [["döntéshozatal", "decision-making"], ["hatáskör-átruházás", "delegation of authority"], ["kivizsgálás", "investigation"], ["helyszíni szemle", "on-site inspection"]], ["c1-08-vocab"]),
                fb("grammar", "practice", "A jogszabály kötelezővé teszi az éves vagyonnyilatkozat-_____ minden vezető számára. (submission / tételt)", "tételt", "Statutory law makes annual asset declaration submission mandatory for every manager.", ["c1-action-nominalization"]),
                sb("grammar", "practice", ["A", "pénzügyi", "kötelezettségvállalás", "előzetes", "jogászi", "ellenjegyzést", "igényel."], ["A", "pénzügyi", "kötelezettségvállalás", "előzetes", "jogászi", "ellenjegyzést", "igényel."], "Financial commitment requires prior legal countersignature.", ["c1-action-nominalization"]),
                dc("dialogue", [
                    {"speaker": "Főosztályvezető", "text": "Mikor bocsátjuk ki a hivatalos végzést?"},
                    {"speaker": "Referens", "text": "Csak a helyszíni szemle jegyzőkönyvének végleges _____ után."},
                ], ["jóváhagyása", "elszaladása", "törlése"], 0, ["c1-action-nominalization"]),
                sw("production", [{"prompt": "Condense 'Amikor a hatóság megvizsgálta az iratokat' into a nominal prepositional phrase.", "answer": "Az iratok hatósági vizsgálatát követően."}], ["c1-action-nominalization"]),
                mc("grammar", "check", "Melyik mondat testesíti meg a legpontosabb hivatali névszói szerkezetet?", [
                    "A hatáskör-átruházás szabályszerűségének ellenőrzése a felügyeleti szerv feladatát képezi.",
                    "Megnézik, hogy kinek adták át a hatalmat a hivatalban.",
                    "Átruházták a dolgokat, és most mindenki nézi."
                ], 0, ["c1-action-nominalization"])
            ]
        },
        {
            "num": 3,
            "stem": "c1-08-03",
            "title": "Bureaucratic Distancing and Agentless Formulations",
            "grammar_title": "Agent Deletion and Formal Distancing in Administrative Decisions",
            "grammar_skill": "c1-bureaucratic-distancing",
            "goals": [
                "I can formulate official administrative denials without attributing personal blame.",
                "I can deploy agent-deletion phrases (*megállapítást nyert, nyilvántartásba vételre került*).",
                "I can write formal bureaucratic rejections and notifications in authentic high register."
            ],
            "vocab": [
                {"lemma": "megállapítást nyert", "translation": "was established / proven", "pos": "expression"},
                {"lemma": "hiánypótlás", "translation": "remedying of deficiencies", "pos": "noun"},
                {"lemma": "elutasításra talál", "translation": "meets with rejection", "pos": "expression"},
                {"lemma": "tudomásulvétel", "translation": "acknowledgment, taking note", "pos": "noun"},
                {"lemma": "melléklet", "translation": "annex, enclosure, appendix", "pos": "noun"},
                {"lemma": "jogalap hiányában", "translation": "in the absence of legal basis", "pos": "expression"},
                {"lemma": "nyilvántartásba vétel", "translation": "registration, entering into records", "pos": "noun"},
                {"lemma": "illetéktelen", "translation": "unauthorized, incompetent", "pos": "adjective"}
            ],
            "gr_text1": "Bureaucratic etiquette demands depersonalization. Instead of stating 'I rejected your claim because you missed the deadline', the official formula reads: *A kérelem elutasításra került jogalap hiányában, mivel a hiánypótlási határidő eredménytelenül telt el.*",
            "gr_text2": "Verbs like *nyer* (gain) are used as passive auxiliaries: *Megállapítást nyert, hogy a beadvány nem felel meg a törvényi követelményeknek.*",
            "gr_table": [
                ["A vizsgálat során megállapítást nyert a mulasztás ténye.", "During the investigation the fact of failure was established."],
                ["A kérelmet jogalap hiányában elutasították.", "The application was rejected in the absence of a legal basis."],
                ["A hiánypótlási felhívás kibocsátásra került.", "The notice for remedying deficiencies was issued."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Miért használ a hivatali stílus személytelen megfogalmazásokat?", ["Hogy a döntés objektív, intézményi jellegét hangsúlyozza az egyéni szimpátia helyett.", "Mert a hivatalnokok nem tudnak magyarul.", "Hogy senki se értse a levelet."], 0, ["c1-08-vocab"]),
                fb("grammar", "controlled", "A bizonyítási eljárás lefolytatása során kétséget kizáróan megállapítást _____, hogy jogsértés nem történt. (gained / was established / nyert)", "nyert", "During the conduct of the evidentiary procedure it was established beyond doubt that no infringement occurred.", ["c1-bureaucratic-distancing"]),
                match("vocabulary", "controlled", [["megállapítást nyert", "was established"], ["hiánypótlás", "remedying deficiencies"], ["jogalap hiányában", "in absence of legal basis"], ["nyilvántartásba vétel", "registration"]], ["c1-08-vocab"]),
                fb("grammar", "practice", "A kérelem érdemi elbírálása _____ hiányában nem volt lehetséges. (legal basis / jogalap)", "jogalap", "Substantive adjudication of the application was not possible in the absence of a legal basis.", ["c1-bureaucratic-distancing"]),
                sb("grammar", "practice", ["A", "hiánypótlási", "határidő", "eredménytelenül", "telt", "el", "a", "kérelmező", "részéről."], ["A", "hiánypótlási", "határidő", "eredménytelenül", "telt", "el", "a", "kérelmező", "részéről."], "The deadline for remedying deficiencies elapsed without result on the part of the applicant.", ["c1-bureaucratic-distancing"]),
                dc("dialogue", [
                    {"speaker": "Ügyfél", "text": "Miért nem vették nyilvántartásba a beadványomat?"},
                    {"speaker": "Ügyintéző", "text": "Mivel az illeték megfizetésének hiányában a kérelem elutasításra _____."},
                ], ["talált", "futott", "nézett"], 0, ["c1-bureaucratic-distancing"]),
                sw("production", [{"prompt": "Write a formal administrative sentence rejecting a request for lack of legal grounds.", "answer": "Értesítjük, hogy kérelme jogalap hiányában elutasításra került, a döntéssel szemben önálló jogorvoslatnak helye nincs."}], ["c1-bureaucratic-distancing"]),
                mc("grammar", "check", "Melyik hivatali közlés felel meg a legmagasabb szintű személytelen stílusnak?", [
                    "A benyújtott dokumentumok alapján megállapítást nyert, hogy a feltételek nem teljesültek, ezért az eljárás megszüntetésre került.",
                    "Nem fogadjuk el a papírjait, mert hiányosak.",
                    "Kérem, ne hozzon több ilyen lapot hozzánk."
                ], 0, ["c1-bureaucratic-distancing"])
            ]
        },
        {
            "num": 4,
            "stem": "c1-08-04",
            "title": "Administrative Litigation and Civic Redress",
            "grammar_title": "Procedural Framing in Judicial Review of Administrative Action",
            "grammar_skill": "c1-administrative-remedy",
            "goals": [
                "I can navigate the procedural stages of administrative litigation (*közigazgatási per*).",
                "I can formulate claims for annulment or modification (*megsemmisítés, megváltoztatás*).",
                "I can articulate citizen rights against unlawful state decisions in legal Hungarian."
            ],
            "vocab": [
                {"lemma": "közigazgatási per", "translation": "administrative lawsuit / judicial review", "pos": "noun"},
                {"lemma": "megsemmisítés", "translation": "annulment, nullification", "pos": "noun"},
                {"lemma": "megváltoztatás", "translation": "modification, alteration", "pos": "noun"},
                {"lemma": "új eljárásra kötelezés", "translation": "ordering of a new proceeding", "pos": "expression"},
                {"lemma": "jogszerűtlenség", "translation": "unlawfulness, illegality", "pos": "noun"},
                {"lemma": "mérlegelési jogkör", "translation": "discretionary power", "pos": "noun"},
                {"lemma": "visszaélés", "translation": "abuse (of power / law)", "pos": "noun"},
                {"lemma": "kereseti kérelem", "translation": "statement of claim / petition", "pos": "noun"}
            ],
            "gr_text1": "When administrative authorities violate statutory bounds, citizens initiate a *közigazgatási per*. The judicial petition (*kereseti kérelem*) requests the court either to annul the decision (*megsemmisítés*) or alter it (*megváltoztatás*).",
            "gr_text2": "Courts scrutinize discretionary powers (*mérlegelési jogkör*): discretionary freedom does not mean arbitrariness (*önkény*); an abuse of discretion constitutes unlawfulness (*jogszerűtlenség*).",
            "gr_table": [
                ["A bíróság a jogsértő határozatot megsemmisítette és új eljárásra kötelezte a hatóságot.", "The court annulled the unlawful decision and ordered the authority to conduct a new proceeding."],
                ["A mérlegelési jogkörrel való visszaélés törvénysértést valósít meg.", "Abuse of discretionary power constitutes a violation of law."],
                ["A felperes kereseti kérelmében a határozat felülvizsgálatát kéri.", "In the statement of claim the plaintiff requests review of the resolution."]
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Mit kérhet a polgár a bíróságtól közigazgatási perben?", ["A jogsértő határozat megsemmisítését vagy megváltoztatását.", "A miniszter azonnali leváltását.", "A törvénykönyv elégetését."], 0, ["c1-08-vocab"]),
                fb("grammar", "controlled", "A bíróság megállapította a jogsértést, a határozatot hatályon kívül helyezte, és a hatóságot új _____ kötelezte. (to proceeding / eljárásra)", "eljárásra", "The court established the infringement, set aside the resolution, and ordered the authority to conduct a new proceeding.", ["c1-administrative-remedy"]),
                match("vocabulary", "controlled", [["közigazgatási per", "administrative lawsuit"], ["megsemmisítés", "annulment"], ["mérlegelési jogkör", "discretionary power"], ["kereseti kérelem", "statement of claim"]], ["c1-08-vocab"]),
                fb("grammar", "practice", "A hatóság a döntés során túllépte törvényes _____ jogkörét. (discretionary / mérlegelési)", "mérlegelési", "In the decision the authority exceeded its statutory discretionary power.", ["c1-administrative-remedy"]),
                sb("grammar", "practice", ["A", "közigazgatási", "bíráskodás", "a", "polgári", "jogvédelem", "legfőbb", "intézményi", "bástyája."], ["A", "közigazgatási", "bíráskodás", "a", "polgári", "jogvédelem", "legfőbb", "intézményi", "bástyája."], "Administrative adjudication is the chief institutional bastion of civil legal protection.", ["c1-administrative-remedy"]),
                dc("dialogue", [
                    {"speaker": "Ügyvéd", "text": "Hogyan reagált a törvényszék a hatóság önkényes bírságára?"},
                    {"speaker": "Alperes", "text": "A bíróság a határozatot teljes egészében _____ helyezte."},
                ], ["hatályon kívül", "szoba közepére", "asztal alá"], 0, ["c1-administrative-remedy"]),
                sw("production", [{"prompt": "Draft a formal claim in an administrative lawsuit requesting annulment.", "answer": "Kérem a Tisztelt Bíróságot, hogy az alperes jogszabálysértő határozatát semmisítse meg, és kötelezze az alperest a perköltségek viselésére."}], ["c1-administrative-remedy"]),
                mc("grammar", "check", "Melyik állítás foglalja össze legpontosabban a mérlegelési jogkör bírósági felülvizsgálatát?", [
                    "A bíróság vizsgálja, hogy a hatóság a tényeket feltárta-e, és a mérlegelés nem volt-e önkényes vagy iratellenes.",
                    "A hatóság mérlegelése abszolút, abba bíróság sosem szólhat bele.",
                    "A mérlegelés azt jelenti, hogy pénzt kell fizetni a bírónak."
                ], 0, ["c1-administrative-remedy"])
            ]
        },
        {
            "num": 5,
            "stem": "c1-08-05",
            "title": "Bureaucracy and Gentry Patronage: Kálmán Mikszáth",
            "grammar_title": "Satirical Dissection of the Hungarian Administrative Machine",
            "grammar_skill": "c1-civic-transparency",
            "goals": [
                "I can analyze Kálmán Mikszáth's portrayal of county bureaucracy in 'A Noszty fiú esete Tóth Marival'.",
                "I can identify stylistic features of gentry patronage, nepotism, and bureaucratic ritual.",
                "I can compare historical bureaucratic satire with modern administrative ethics."
            ],
            "vocab": [
                {"lemma": "vármegyei közigazgatás", "translation": "county administration", "pos": "noun"},
                {"lemma": "protekció", "translation": "patronage, pull, connections", "pos": "noun"},
                {"lemma": "dzsentri", "translation": "gentry (impoverished Hungarian nobleman)", "pos": "noun"},
                {"lemma": "hivatalnoki kar", "translation": "civil service / bureaucratic corps", "pos": "noun"},
                {"lemma": "hivatali packázás", "translation": "bureaucratic red tape / runaround", "pos": "noun"},
                {"lemma": "összeköttetés", "translation": "connections, networking", "pos": "noun"},
                {"lemma": "korrupció", "translation": "corruption", "pos": "noun"},
                {"lemma": "átláthatóság", "translation": "transparency", "pos": "noun"}
            ],
            "gr_text1": "Kálmán Mikszáth (1847–1910) was the greatest anatomist of Hungary's late 19th-century county administration. In *A Noszty fiú esete Tóth Marival*, he exposed how the impoverished gentry treated public administration not as a civic duty, but as a private family feeding trough (*családi hitbizomány*).",
            "gr_text2": "Mikszáth's prose combines warm, anecdotal storytelling with ruthless sociological precision, dissecting nepotism (*protekció*) and bureaucratic inertia (*hivatali packázás*).",
            "gr_table": [
                ["A vármegyei tisztikar mint az úri osztály menedéke...", "The county administrative staff as the refuge of the gentry class..."],
                ["Protekció és összeköttetések a törvény szigorával szemben...", "Patronage and connections against the rigor of the law..."],
                ["A hivatali formaságok mögé rejtett magánérdek...", "Private interests hidden behind administrative formalities..."]
            ],
            "classic_story": {
                "slug": "c1-08-mikszath",
                "author": "Mikszáth Kálmán",
                "work": "A Noszty fiú esete Tóth Marival (1908)",
                "title": "A vármegyei hivatal és az úri protekció hálója",
                "summary": "Kálmán Mikszáth's masterly satire of county bureaucracy, patronage, and the clashes between the decadent gentry and rising civic wealth.",
                "characters": ["Mikszáth Kálmán", "Noszty Feri", "Tóth Mihály"],
                "paragraphs": [
                    {"type": "narration", "text": "A tizenkilencedik század végi Magyarországon a vármegyeháza nem pusztán közigazgatási hivatal volt, hanem egy zárt társadalmi kaszt szentélye. Mikszáth Kálmán regényében, A Noszty fiú esete Tóth Marival lapjain páratlan iróniával és szociológiai éleslátással mutatja be azt a világot, ahol a törvények rideg betűjét mindig felülírta az úri összeköttetés és a családi protekció."},
                    {"type": "narration", "text": "A birtokait eltékozló, adósságokban úszó dzsentri számára a vármegyei hivatal jelentette a túlélés egyetlen tisztességesnek tekintett formáját. Az alispánok, szolgabírák és jegyzők nem az állampolgárok szolgálatát látták feladatuknak, hanem a saját osztályuk tekintélyének és kényelmének fenntartását. Ha egy rokonnak vagy barátnak állásra volt szüksége, a hivatalnoki kar azonnal új beosztást kreált."},
                    {"type": "narration", "text": "Amikor Noszty Feri, a könnyelmű huszárhadnagy elhatározza, hogy az Amerikából hazatért gazdag polgár, Tóth Mihály lányának hozományával menti meg a családi vagyont, a vármegye teljes adminisztratív gépezete mozgásba lendül, hogy segítse a tervet. A törvényes formaságok, a hivatalos pecsétek és az eljárási szabályok mind csak díszletek egy cinikus magánérdek szolgálatában."},
                    {"type": "narration", "text": "Mikszáth szelíd, anekdotázó humora mögött kíméletlen ítélet húzódik: az az állam, ahol a közigazgatás a polgárok szolgálata helyett a protekció és a kiváltságok védőbástyájává válik, elkerülhetetlenül megmérgezi a közélet tisztaságát. Szavai ma is a professzionális, átlátható és pártatlan közigazgatás elengedhetetlen erkölcsi szükségességére intenek."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Milyen társadalmi jelenséget bírált Mikszáth a vármegyei hivatalok működésében?", ["A dzsentri osztály protekcionizmusát és a hivatalok magáncélú kisajátítását.", "A túlságosan modern számítógépes rendszereket.", "A parasztság túlzott befolyását a politikában."], 0, ["c1-08-vocab"]),
                fb("grammar", "controlled", "Mikszáth regényében a hivatalos eljárások pusztán a családi _____ érvényesítését szolgálták. (patronage / protekció)", "protekció", "In Mikszáth's novel official procedures merely served the enforcement of family patronage.", ["c1-civic-transparency"]),
                match("vocabulary", "controlled", [["vármegyei közigazgatás", "county administration"], ["protekció", "patronage / pull"], ["dzsentri", "gentry"], ["hivatali packázás", "bureaucratic red tape"]], ["c1-08-vocab"]),
                mc("reading", "practice", "Mi volt a vármegyei hivatalok valódi szerepe a lecsúszott nemesség számára?", [
                    "Kényelmes, biztos menedéket és fizetést nyújtott a vagyontalan nemeseknek.",
                    "Kemény fizikai munkát jelentett reggeltől estig.",
                    "A legmodernebb ipari kutatások központja volt."
                ], 0, None),
                sb("grammar", "practice", ["A", "közszolgálat", "nem", "lehet", "egy", "egyetlen", "társadalmi", "osztály", "privilégiuma."], ["A", "közszolgálat", "nem", "lehet", "egy", "egyetlen", "társadalmi", "osztály", "privilégiuma."], "Civil service cannot be the privilege of a single social class.", ["c1-civic-transparency"]),
                sw("production", [{"prompt": "Reflect on Mikszáth's satire in relation to modern principles of public administration.", "answer": "Mikszáth remekműve arra figyelmeztet, hogy a protekcióra és kapcsolati hálókra épülő közigazgatás tönkreteszi a jogállamot. A modern közszolgálat alapja a pártatlanság, a meritokrácia és a teljes átláthatóság kell legyen."}], ["c1-civic-transparency"]),
                mc("grammar", "check", "Melyik állítás foglalja össze legmélyebben Mikszáth regényének máig érvényes üzenetét?", [
                    "A hivatalok működésének tisztasága és átláthatósága az igazságos társadalom alapfeltétele.",
                    "A legjobb közigazgatás az, ahol nincsenek törvények.",
                    "A pénz és a kapcsolatok mindig mindent megoldanak baj nélkül."
                ], 0, ["c1-civic-transparency"])
            ]
        }
    ]

    for l in core_lessons:
        emit_instructional_lesson(8, "core", l, core_title, core_intro if l["num"] == 1 else None)

    # Core Consolidation
    emit_consolidation_lesson(
        8,
        "core",
        "c1-08-consolidation",
        core_title,
        [
            "I can deploy periphrastic passive avoidance forms (megállapításra került, elutasításban részesült).",
            "I can construct dense action nominalizations (-ás/-és) and agentless administrative prose.",
            "I can navigate administrative litigation claims and evaluate Mikszáth's bureaucratic satire."
        ],
        [
            mc("grammar", "recognize", "Melyik szerkezet helyettesíti szabályosan a passzívumot hivatalos magyar szövegben?", [
                "a főnév + -ra/-re került fordulat",
                "a jelen idejű feltételes mód",
                "az ikes igék ragozása"
            ], 0, ["c1-passive-avoidance"]),
            mc("grammar", "recognize", "Mit fejez ki a 'jogalap hiányában' fordulat?", [
                "Azt, hogy a döntésnek nincs törvényes törvényi támasza vagy felhatalmazása.",
                "Hogy a hivatalnok elvesztette a tollát.",
                "Hogy nagyon gyorsan meghozták a döntést."
            ], 0, ["c1-bureaucratic-distancing"]),
            match("vocabulary", "recognize", [["megállapításra került", "was established"], ["vagyonnyilatkozat-tétel", "asset declaration"], ["közigazgatási per", "administrative lawsuit"], ["mérlegelési jogkör", "discretionary power"], ["átláthatóság", "transparency"]], ["c1-08-vocab"]),
            fb("vocabulary", "recall", "A bíróság a jogszabálysértő közigazgatási határozatot _____ helyezte. (aside / hatályon kívül)", "hatályon kívül", "The court set aside the unlawful administrative resolution.", ["c1-08-vocab"]),
            fb("vocabulary", "recall", "A közpénzekkel gazdálkodó intézmények számára az _____ alapvető jogállami követelmény. (transparency / átláthatóság)", "átláthatóság", "For institutions managing public funds transparency is a fundamental rule-of-law requirement.", ["c1-08-vocab"]),
            fb("grammar", "recall", "A pályázati kérelem a formai vizsgálat után azonnali befogadásra _____. (was / került)", "került", "Following formal examination the tender application was accepted.", ["c1-passive-avoidance"]),
            fb("grammar", "context", "A döntéshozatal során a hatóság nem lépheti túl törvényes _____ jogkörét. (discretionary / mérlegelési)", "mérlegelési", "During decision making the authority cannot exceed its statutory discretionary power.", ["c1-administrative-remedy"]),
            fb("grammar", "context", "A felülvizsgálat során kétséget kizáróan megállapítást _____, hogy a tisztviselő jogszerűen járt el. (gained / was established / nyert)", "nyert", "During the review it was established beyond doubt that the official acted lawfully.", ["c1-bureaucratic-distancing"]),
            mc("grammar", "context", "Melyik mondat képvisel hibátlan hivatali tömörítést?", [
                "A hatáskör-átruházás jogszerűségének kivizsgálását követően intézkedésre került sor.",
                "Megnézték, kié a hatáskör, aztán csináltak valamit.",
                "Mivel senki nem tudta, mi a baj, elmentek ebédelni."
            ], 0, ["c1-action-nominalization"]),
            sb("grammar", "produce", ["A", "közigazgatási", "határozatok", "bírósági", "kontrollja", "a", "jogállam", "alapja."], ["A", "közigazgatási", "határozatok", "bírósági", "kontrollja", "a", "jogállam", "alapja."], "Judicial control of administrative decisions is the foundation of the rule of law.", ["c1-administrative-remedy"]),
            sw("production", [{"prompt": "Write a formal administrative sentence using both an action nominalization and passive-avoidance.", "answer": "A panasz érdemi kivizsgálását követően a határozat a felek részére kézbesítésre került."}], ["c1-passive-avoidance"]),
            sw("production", [{"prompt": "Formulate a concluding thought on administrative ethics inspired by Mikszáth.", "answer": "A közigazgatás valódi hivatása a polgárok pártatlan és átlátható szolgálata, amelyben a protekciónak és a magánérdeknek helye nincs."}], ["c1-civic-transparency"])
        ]
    )

    # ----------------------------------------------------
    # TRACK 2: DISCOURSE (c1-kozszolgalat)
    # ----------------------------------------------------
    slug = "kozszolgalat"
    disc_intro = [
        "Public administration is the nervous system of modern statehood. True democratic legitimacy requires transparency, accessible public data, ethical integrity, and independent oversight through ombudsman institutions and administrative courts.",
        "In this unit, you will explore the mechanisms of civic redress: Freedom of Information (FOI / közérdekű adatigénylés), the historic role of the Parliamentary Ombudsman, whistleblower protections, anti-corruption watchdogs, and digital e-governance in Hungary."
    ]

    disc_lessons = [
        {
            "num": 1,
            "stem": f"c1-{slug}-01",
            "title": "Freedom of Information and Public Data Transparency",
            "grammar_title": "The Right to Information and Public Interest Data Requests",
            "grammar_skill": "c1-civic-transparency",
            "goals": [
                "I can analyze the legal architecture of Freedom of Information (*közérdekű adatigénylés*).",
                "I can evaluate transparency obligations of state bodies and municipal companies.",
                "I can draft formal public data inquiries and understand statutory disclosure exemptions."
            ],
            "vocab": [
                {"lemma": "közérdekű adat", "translation": "data of public interest, public information", "pos": "noun"},
                {"lemma": "adatigénylés", "translation": "data request / inquiry", "pos": "noun"},
                {"lemma": "titoktartás", "translation": "confidentiality, secrecy", "pos": "noun"},
                {"lemma": "közpénz", "translation": "public funds", "pos": "noun"},
                {"lemma": "megtagadás", "translation": "refusal, denial", "pos": "noun"},
                {"lemma": "üzleti titok", "translation": "trade secret, commercial secret", "pos": "noun"},
                {"lemma": "elszámoltathatóság", "translation": "accountability", "pos": "noun"},
                {"lemma": "adatvédelmi hatóság", "translation": "data protection authority (NAIH)", "pos": "noun"}
            ],
            "gr_text1": "In Hungarian law, all information concerning the expenditure of public money (*közpénz*) or state tasks qualifies as *közérdekű adat*. Citizens and journalists have the constitutional right to request and receive this data within 15 days.",
            "gr_text2": "Authorities frequently attempt to withhold documents citing *üzleti titok* (trade secret) or decision-preparatory exceptions (*döntéselőkészítő adat*), leading to transparency lawsuits (*adatkiadási per*).",
            "gr_table": [
                ["A közpénzek felhasználása nyilvános és ellenőrizendő...", "The utilization of public funds is open and to be inspected..."],
                ["Közérdekű adatigénylés benyújtása tizenöt napos határidővel...", "Submitting a public interest data request with a fifteen-day deadline..."],
                ["Az üzleti titokra való alaptalan hivatkozás elutasítása...", "Rejecting unfounded invocation of trade secrets..."]
            ],
            "world_story_seg": {
                "seg_slug": "adatigenyles",
                "title": "A közpénzek átláthatósága és a szabad információ",
                "summary": "How freedom of information requests empower citizens and investigative journalists to hold public power accountable.",
                "paragraphs": [
                    {"type": "narration", "text": "A modern demokráciában az információ nem a hatalom monopóliuma, hanem a polgárok köztulajdona. Az Alaptörvény és az információszabadságról szóló törvény egyértelmű alapelvet rögzít: minden olyan adat, amely a közfeladatot ellátó szervek tevékenységére vagy a közpénzek elköltésére vonatkozik, közérdekű adat, és megismerése mindenkit megillet."},
                    {"type": "narration", "text": "A civil szervezetek és az oknyomozó újságírók nap mint nap élnek a közérdekű adatigénylés fegyverével. Legyen szó egy autópálya-építés költségvetéséről, kórházi eszközbeszerzésekről vagy állami támogatások szétosztásáról, a nyilvánosság a korrupció legfőbb ellenszere. Amikor egy minisztérium megtagadja a válaszadást, a bíróságok sorra kötelezik az intézményeket a titkolt adatok haladéktalan kiadására."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Milyen adat minősül 'közérdekű adatnak' a magyar jogban?", ["A közfeladatot ellátó szervek tevékenységére és a közpénzekre vonatkozó információ.", "A magánszemélyek bankszámlaszáma.", "Az állatkerti állatok kedvenc étele."], 0, ["c1-kozszolgalat-vocab"]),
                fb("grammar", "controlled", "A közpénzek felhasználásának átláthatósága a demokratikus _____ sarokköve. (accountability / elszámoltathatóság)", "elszámoltathatóság", "The transparency of using public funds is the cornerstone of democratic accountability.", ["c1-civic-transparency"]),
                match("vocabulary", "controlled", [["közérdekű adat", "public interest data"], ["adatigénylés", "data request"], ["közpénz", "public funds"], ["üzleti titok", "trade secret"]], ["c1-kozszolgalat-vocab"]),
                sb("grammar", "practice", ["A", "közpénzek", "minden", "forintjával", "nyilvánosan", "kell", "elszámolni", "a", "társadalomnak."], ["A", "közpénzek", "minden", "forintjával", "nyilvánosan", "kell", "elszámolni", "a", "társadalomnak."], "Every forint of public funds must be publicly accounted for to society.", ["c1-civic-transparency"]),
                sw("production", [{"prompt": "Explain why authorities cannot withhold public spending data behind trade secrets.", "answer": "Közpénzek felhasználása esetén a közérdekű adatok nyilvánossága megelőzi a magánérdekeket; a törvény értelmében a közpénzre vonatkozó adatok nem minősíthetők üzleti titokká."}], ["c1-civic-transparency"]),
                mc("grammar", "check", "Milyen határidővel köteles válaszolni a hatóság a közérdekű adatigénylésre főszabály szerint?", [
                    "Tizenöt napon belül köteles kiadni a kért adatokat.",
                    "Három éven belül, ha van kedve.",
                    "Soha nem köteles válaszolni."
                ], 0, ["c1-civic-transparency"])
            ]
        },
        {
            "num": 2,
            "stem": f"c1-{slug}-02",
            "title": "The Ombudsman Institution: Citizen Rights Advocate",
            "grammar_title": "The Parliamentary Commissioner and Fundamental Rights Oversight",
            "grammar_skill": "c1-civic-transparency",
            "goals": [
                "I can analyze the mandate and function of the Hungarian Ombudsman (*Alapvető Jogok Biztosa*).",
                "I can evaluate ombudsman reports on vulnerable populations, children, and prisoners.",
                "I can understand moral authority vs. coercive power in institutional dispute resolution."
            ],
            "vocab": [
                {"lemma": "Alapvető Jogok Biztosa", "translation": "Commissioner for Fundamental Rights (Ombudsman)", "pos": "noun"},
                {"lemma": "ombudsman", "translation": "ombudsman, parliamentary commissioner", "pos": "noun"},
                {"lemma": "visszásság", "translation": "anomaly, malady, irregularity", "pos": "noun"},
                {"lemma": "ajánlás", "translation": "formal recommendation", "pos": "noun"},
                {"lemma": "kivizsgálás", "translation": "inquiry, investigation", "pos": "noun"},
                {"lemma": "jogvédelem", "translation": "legal protection of rights", "pos": "noun"},
                {"lemma": "kiszolgáltatottság", "translation": "vulnerability, helplessness", "pos": "noun"},
                {"lemma": "intézkedési javaslat", "translation": "proposal for action", "pos": "noun"}
            ],
            "gr_text1": "Originating in Scandinavia, the ombudsman was introduced into Hungarian constitutional law in 1993. The Commissioner investigates constitutional anomalies (*visszásság*) committed by public authorities.",
            "gr_text2": "The ombudsman has no coercive force to annul laws or jail officials; their weapon is publicity, thorough investigation (*kivizsgálás*), and morally unassailable recommendations (*ajánlások*).",
            "gr_table": [
                ["Az Alapvető Jogok Biztosa vizsgálatot indít alapjogi visszásság gyanúja esetén...", "The Commissioner for Fundamental Rights initiates inquiry upon suspected anomaly..."],
                ["Ajánlás megfogalmazása az illetékes miniszter számára...", "Formulating a recommendation for the competent minister..."],
                ["A kiszolgáltatott csoportok jogvédelmének megerősítése...", "Strengthening the legal protection of vulnerable groups..."]
            ],
            "world_story_seg": {
                "seg_slug": "ombudsman",
                "title": "Az ombudsman és a polgári jogvédelem csendes ereje",
                "summary": "How the institution of the Parliamentary Commissioner defends individual rights against bureaucratic inertia.",
                "paragraphs": [
                    {"type": "narration", "text": "Amikor egy egyszerű állampolgár szembekerül a hatalmas állami bürokráciával, a pereskedés gyakran túl drága, túl lassú és lélekölő folyamat. Erre a küzdelemre hozta létre a skandináv jogfejlődés az ombudsman intézményét, amely a rendszerváltást követően Magyarországon is a polgári jogvédelem nélkülözhetetlen bástyájává vált."},
                    {"type": "narration", "text": "Az Alapvető Jogok Biztosához bárki fordulhat, ha úgy érzi, hogy egy hatóság eljárása sérti az alkotmányos jogait. Bár az ombudsman nem hozhat kötelező bírósági ítéletet, jelentései és nyilvános ajánlásai hatalmas erkölcsi súllyal bírnak. Feltárta a gyermekotthonok állapotát, a fogvatartottak helyzetét és a kórházi ellátás anomáliáit, kényszerítve a döntéshozókat a hibák kijavítására."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Milyen eszközzel rendelkezik az ombudsman a jogsértések orvoslására?", ["Nyilvános vizsgálati jelentésekkel és hivatalos ajánlásokkal.", "Fegyveres rendőri alakulattal.", "Azonnali pénzbírság kiszabásának jogával."], 0, ["c1-kozszolgalat-vocab"]),
                fb("grammar", "controlled", "Az ombudsman feladata felderíteni a hatósági eljárásokban rejlő alapjogi _____ és ajánlást tenni a megoldásra. (anomalies / visszásságokat)", "visszásságokat", "The ombudsman's task is to uncover fundamental rights anomalies in administrative procedures and make recommendations for solution.", ["c1-civic-transparency"]),
                match("vocabulary", "controlled", [["ombudsman", "parliamentary commissioner"], ["visszásság", "anomaly / malady"], ["ajánlás", "recommendation"], ["jogvédelem", "legal protection"]], ["c1-kozszolgalat-vocab"]),
                sb("grammar", "practice", ["Az", "ombudsmani", "jelentés", "erkölcsi", "tekintélye", "változásra", "kényszeríti", "a", "hatóságokat."], ["Az", "ombudsmani", "jelentés", "erkölcsi", "tekintélye", "változásra", "kényszeríti", "a", "hatóságokat."], "The moral authority of the ombudsman report forces authorities to change.", ["c1-civic-transparency"]),
                sw("production", [{"prompt": "Explain why moral authority can be effective without coercive power in public oversight.", "answer": "A nyilvánosság ereje és a tények megkérdőjelezhetetlen feltárása olyan politikai és társadalmi nyomást teremt, amelyet az intézmények nem hagyhatnak figyelmen kívül."}], ["c1-civic-transparency"]),
                mc("grammar", "check", "Ki fordulhat panasszal az Alapvető Jogok Biztosához Magyarországon?", [
                    "Bárki, aki úgy ítéli meg, hogy egy hatóság tevékenysége vagy mulasztása alapvető jogait sérti.",
                    "Kizárólag parlamenti képviselők.",
                    "Csak azok, akik ügyvédet fogadnak."
                ], 0, ["c1-civic-transparency"])
            ]
        },
        {
            "num": 3,
            "stem": f"c1-{slug}-03",
            "title": "Whistleblower Protection and Integrity in Governance",
            "grammar_title": "Whistleblower Systems and Anti-Corruption Watchdogs",
            "grammar_skill": "c1-civic-transparency",
            "goals": [
                "I can analyze whistleblower protection systems (*közérdekű bejelentő védelme*).",
                "I can evaluate institutional compliance mechanisms preventing corruption in Hungary.",
                "I can discuss the psychological, legal, and professional risks of civic whistleblowing."
            ],
            "vocab": [
                {"lemma": "közérdekű bejelentő", "translation": "whistleblower", "pos": "noun"},
                {"lemma": "integritás", "translation": "integrity, probity", "pos": "noun"},
                {"lemma": "megtorlás", "translation": "retaliation, reprisal", "pos": "noun"},
                {"lemma": "visszaélés-bejelentő rendszer", "translation": "whistleblowing reporting system", "pos": "noun"},
                {"lemma": "korrupcióellenes", "translation": "anti-corruption", "pos": "adjective"},
                {"lemma": "titoktartási kötelezettség", "translation": "duty of confidentiality", "pos": "noun"},
                {"lemma": "védelmi intézkedés", "translation": "protective measure", "pos": "noun"},
                {"lemma": "etikai kódex", "translation": "code of ethics", "pos": "noun"}
            ],
            "gr_text1": "Whistleblowers (*közérdekű bejelentők*) are the frontline defenders of institutional integrity. Transposing EU directives, Hungarian law protects individuals who report fraud or corruption from professional retaliation (*megtorlás*).",
            "gr_text2": "Large corporations and public bodies are statutorily required to operate anonymous whistleblowing channels (*belső visszaélés-bejelentési rendszer*), guaranteeing confidentiality.",
            "gr_table": [
                ["A közérdekű bejelentők védelme a megtorlással szemben...", "Protecting whistleblowers against retaliation..."],
                ["Belső visszaélés-bejelentési csatorna működtetése minden intézményben...", "Operating internal whistleblowing channels in every institution..."],
                ["Az intézményi integritás és etikus magatartás biztosítása...", "Ensuring institutional integrity and ethical conduct..."]
            ],
            "world_story_seg": {
                "seg_slug": "bejelentovedelem",
                "title": "A bejelentő bátorsága és az intézményi integritás",
                "summary": "The ethical dilemmas and institutional safeguards surrounding whistleblowers who uncover corruption from within.",
                "paragraphs": [
                    {"type": "narration", "text": "Egyetlen szervezet sem működhet tisztességesen, ha a falain belül elkövetett visszaéléseket a félelem és a csend kultúrája övezi. A közérdekű bejelentők – azok a munkavállalók, akik belső csalásokat, környezetszennyezést vagy korrupciót lepleznek le – rendkívüli személyes és szakmai kockázatot vállalnak a közjó védelmében."},
                    {"type": "narration", "text": "A modern jog ezért szigorú védőhálót von köréjük. A törvény kifejezetten tiltja a bejelentőkkel szembeni bármilyen hátrányos megkülönböztetést, elbocsátást vagy zaklatást. A névtelenséget biztosító bejelentővédelmi rendszerek nemcsak a visszaélések felderítését segítik, hanem az intézményi kultúra megtisztulását és a bizalom helyreállítását is szolgálják."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Milyen jogi védelmet garantál a törvény a közérdekű bejelentőknek?", ["Védelmet a munkahelyi megtorlással, elbocsátással és hátrányos megkülönböztetéssel szemben.", "Azonnali miniszteri kinevezést.", "Adómentességet egész életre."], 0, ["c1-kozszolgalat-vocab"]),
                fb("grammar", "controlled", "A jogszabály szigorúan bünteti a bejelentővel szemben alkalmazott bármilyen jellegű munkahelyi _____. (retaliation / megtorlást)", "megtorlást", "Statutory law strictly penalizes any kind of workplace retaliation applied against the whistleblower.", ["c1-civic-transparency"]),
                match("vocabulary", "controlled", [["közérdekű bejelentő", "whistleblower"], ["integritás", "integrity"], ["megtorlás", "retaliation"], ["etikai kódex", "code of ethics"]], ["c1-kozszolgalat-vocab"]),
                sb("grammar", "practice", ["A", "bejelentők", "védelme", "a", "korrupció", "elleni", "harc", "legfőbb", "feltétele."], ["A", "bejelentők", "védelme", "a", "korrupció", "elleni", "harc", "legfőbb", "feltétele."], "The protection of whistleblowers is the chief condition of the fight against corruption.", ["c1-civic-transparency"]),
                sw("production", [{"prompt": "Write a short policy statement on whistleblowing in public institutions.", "answer": "Az intézmény zéró toleranciát hirdet a korrupcióval szemben, és garantálja a közérdekű bejelentők teljes körű védelmét minden megtorlással szemben."}], ["c1-civic-transparency"]),
                mc("grammar", "check", "Miért tekinthető a belső bejelentővédelmi rendszer hatékony prevenciós eszköznek?", [
                    "Mert elrettenti a döntéshozókat a jogsértésektől, tudva, hogy a visszaélések nem maradhatnak titokban.",
                    "Mert betiltja a belső ellenőrzéseket.",
                    "Mert minden munkatársnak kötelező felmondania."
                ], 0, ["c1-civic-transparency"])
            ]
        },
        {
            "num": 4,
            "stem": f"c1-{slug}-04",
            "title": "Digital Governance, E-Administration and Civic Access",
            "grammar_title": "E-Administration: Ügyfélkapu, Algorithmic Decision-Making and Rights",
            "grammar_skill": "c1-civic-transparency",
            "goals": [
                "I can analyze digital public administration systems in Hungary (*Ügyfélkapu+, DÁP*).",
                "I can evaluate algorithmic decision-making and digital accessibility rights.",
                "I can discuss digital divide risks and citizen data security in Hungarian e-governance."
            ],
            "vocab": [
                {"lemma": "elektronikus közigazgatás", "translation": "e-administration / e-governance", "pos": "noun"},
                {"lemma": "Ügyfélkapu", "translation": "Client Gate (Hungarian government citizen portal)", "pos": "noun"},
                {"lemma": "digitális állampolgárság", "translation": "digital citizenship (DÁP program)", "pos": "noun"},
                {"lemma": "adatbiztonság", "translation": "data security", "pos": "noun"},
                {"lemma": "algoritmikus döntéshozatal", "translation": "algorithmic decision-making", "pos": "noun"},
                {"lemma": "digitális szakadék", "translation": "digital divide", "pos": "noun"},
                {"lemma": "ügyintézés", "translation": "administrative processing, casework", "pos": "noun"},
                {"lemma": "hitelesítés", "translation": "authentication, certification", "pos": "noun"}
            ],
            "gr_text1": "Hungary has shifted toward comprehensive e-administration: the *Ügyfélkapu* (Client Gate) and the *Digitális Állampolgárság Program (DÁP)* have replaced physical paper queues with encrypted online portals.",
            "gr_text2": "Digital administration brings immense efficiency, but also novel legal challenges: algorithmic bias, cybersecurity vulnerabilities, and the *digitális szakadék* (digital divide) affecting the elderly and rural populations.",
            "gr_table": [
                ["A hivatali ügyintézés digitalizációja az Ügyfélkapun keresztül...", "Digitization of administrative processing through Client Gate..."],
                ["Digitális állampolgárság és biometrikus hitelesítés...", "Digital citizenship and biometric authentication..."],
                ["A digitális szakadék áthidalása az idősek és kistelepülések számára...", "Bridging the digital divide for the elderly and small settlements..."]
            ],
            "world_story_seg": {
                "seg_slug": "digitaliskozigazgatas",
                "title": "Az Ügyfélkaputól a digitális állampolgárságig",
                "summary": "The technological transformation of Hungarian public casework and the challenges of equal civic digital access.",
                "paragraphs": [
                    {"type": "narration", "text": "Hosszú évtizedeken át a magyar hivatali ügyintézés szinonimája a sorszámhúzás, a poros folyosókon való várakozás és a végtelen pecsételés volt. A huszonegyedik század harmadik évtizedére azonban a digitális forradalom alapjaiban alakította át a polgárok és az állam kapcsolatát. Az Ügyfélkapu és az új Digitális Állampolgárság Program révén ma már az adóbevallástól az útlevél-igénylésig szinte minden intézhető egy okostelefonról."},
                    {"type": "narration", "text": "A kényelem mögött azonban súlyos alkotmányos kérdések húzódnak. Hogyan garantálható az állampolgárok személyes adatainak sérthetetlensége a kibertámadásokkal szemben? És mi történik azokkal a százezrekkel, akik a digitális szakadék túlsó oldalán rekedtek – az idősekkel és a szegény kistelepülések lakóival? A valódi modern közigazgatás nem hagyhatja magára azokat, akiknek a képernyő nem kaput, hanem falat jelent."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Mi a fő célja az elektronikus közigazgatás elterjesztésének?", ["A hivatali ügyintézés gyorsítása, egyszerűsítése és papírmentesítése.", "A személyes kapcsolatok teljes betiltása.", "Minden hivatal bezárása örökre."], 0, ["c1-kozszolgalat-vocab"]),
                fb("grammar", "controlled", "A digitalizáció során kiemelt figyelmet kell fordítani a _____ szakadék csökkentésére a hátrányos helyzetű térségekben. (digital / digitális)", "digitális", "During digitization highlighted attention must be paid to reducing the digital divide in disadvantaged regions.", ["c1-civic-transparency"]),
                match("vocabulary", "controlled", [["elektronikus közigazgatás", "e-administration"], ["Ügyfélkapu", "Client Gate portal"], ["adatbiztonság", "data security"], ["digitális szakadék", "digital divide"]], ["c1-kozszolgalat-vocab"]),
                sb("grammar", "practice", ["A", "digitális", "állam", "nem", "zárhatja", "ki", "azokat,", "akik", "nem", "értenek", "a", "technológiához."], ["A", "digitális", "állam", "nem", "zárhatja", "ki", "azokat,", "akik", "nem", "értenek", "a", "technológiához."], "The digital state cannot exclude those who do not understand technology.", ["c1-civic-transparency"]),
                sw("production", [{"prompt": "Discuss the ethical dilemma of digital-only public administration.", "answer": "Míg a digitális közigazgatás hatalmas időmegtakarítást jelent, a személyes ügyintézés lehetőségének fenntartása alapvető esélyegyenlőségi követelmény az idősebb generációk számára."}], ["c1-civic-transparency"]),
                mc("grammar", "check", "Melyik tényező jelenti a legnagyobb biztonsági kihívást a digitális államigazgatásban?", [
                    "A központi adatbázisok védelme az illetéktelen hozzáféréssel és a kiberbűnözéssel szemben.",
                    "Hogy túl sok papírt kell kinyomtatni.",
                    "Hogy a számítógépek túl sok áramot fogyasztanak."
                ], 0, ["c1-civic-transparency"])
            ]
        },
        {
            "num": 5,
            "stem": f"c1-{slug}-05",
            "title": "Civil Society Watchdogs and the Future of Integrity",
            "grammar_title": "NGO Oversight, Civic Audit, and Democratic Renewal",
            "grammar_skill": "c1-civic-transparency",
            "goals": [
                "I can evaluate the role of civil society watchdogs (*Transparency International, TASZ, K-Monitor*).",
                "I can debate the balance between state sovereignty and independent civil monitoring.",
                "I can articulate a compelling vision for modern, transparent Hungarian public service."
            ],
            "vocab": [
                {"lemma": "civil szervezet", "translation": "civil society organization / NGO", "pos": "noun"},
                {"lemma": "monitoring", "translation": "monitoring, surveillance, oversight", "pos": "noun"},
                {"lemma": "korrupciós kockázat", "translation": "corruption risk", "pos": "noun"},
                {"lemma": "közbeszerzés", "translation": "public procurement", "pos": "noun"},
                {"lemma": "társadalmi egyeztetés", "translation": "public consultation, civic dialogue", "pos": "noun"},
                {"lemma": "közérdek", "translation": "public interest", "pos": "noun"},
                {"lemma": "pártatlanság", "translation": "impartiality, non-partisanship", "pos": "noun"},
                {"lemma": "hivatásetika", "translation": "professional ethics", "pos": "noun"}
            ],
            "gr_text1": "Civil society watchdogs (*civil szervezetek*) serve as the democratic immune system. Operating open-source databases on public procurement (*közbeszerzések*), asset declarations, and court rulings, they hold public officials accountable.",
            "gr_text2": "The ideal of public service (*közszolgálat*) is fundamentally ethical: true servants of the state embody impartiality (*pártatlanság*), resisting political capture to serve the broad public interest (*közérdek*).",
            "gr_table": [
                ["A civil szervezetek független monitoring tevékenysége...", "Independent monitoring activities of civil society organizations..."],
                ["A közbeszerzési eljárások szigorú társadalmi ellenőrzése...", "Strict societal inspection of public procurement procedures..."],
                ["A pártatlan, hivatásetikán alapuló közszolgálat eszménye...", "The ideal of impartial public service based on professional ethics..."]
            ],
            "world_story_seg": {
                "seg_slug": "civilszervezetek",
                "title": "A civil kurázsi és a jövő közigazgatása",
                "summary": "Civil watchdogs, civic data audits, and the enduring vision of a professional, incorruptible Hungarian public service.",
                "paragraphs": [
                    {"type": "narration", "text": "A demokrácia minőségét végső soron nem az írott törvénykönyvek vastagsága méri, hanem a polgárok ébersége és a civil társadalom ereje. Magyarországon az olyan független szervezetek, mint a Transparency International, a K-Monitor vagy a Társaság a Szabadságjogokért (TASZ), évtizedek óta küzdenek a közpénzek átláthatóságáért és a korrupció visszaszorításáért."},
                    {"type": "narration", "text": "Az általuk fejlesztett adatbázisok, közbeszerzési elemzések és bírósági perek ezerszeresen bizonyították, hogy az államhatalom ellenőrzése nem nemzetellenes tevékenység, hanem a legnemesebb hazafias kötelesség. A jövő közigazgatása csak akkor lehet sikeres, ha a hivatali elit nem ellenségként, hanem partnerként tekint a civil polgárokra: olyan közszolgálatot építve, amely a pártatlanság, a professzionalizmus és a megkérdőjelezhetetlen tisztesség talaján áll."}
                ]
            },
            "exercises": [
                mc("vocabulary", "introduce", "Milyen szerepet töltenek be a civil watchodog szervezetek a demokráciában?", ["Független ellenőrzést és monitoringot végeznek a közpénzek és a hatalom felett.", "Állami adókat vetnek ki a polgárokra.", "Politikai választásokat döntenek el egyedül."], 0, ["c1-kozszolgalat-vocab"]),
                fb("grammar", "controlled", "A közbeszerzések szigorú társadalmi ellenőrzése elengedhetetlen a _____ kockázatok minimalizálásához. (corruption / korrupciós)", "korrupciós", "Strict societal oversight of public procurement is indispensable for minimizing corruption risks.", ["c1-civic-transparency"]),
                match("vocabulary", "controlled", [["civil szervezet", "civil society organization"], ["közbeszerzés", "public procurement"], ["pártatlanság", "impartiality"], ["hivatásetika", "professional ethics"]], ["c1-kozszolgalat-vocab"]),
                sb("grammar", "practice", ["A", "hatalom", "társadalmi", "ellenőrzése", "a", "szabad", "polgárok", "legelidegeníthetetlenebb", "joga."], ["A", "hatalom", "társadalmi", "ellenőrzése", "a", "szabad", "polgárok", "legelidegeníthetetlenebb", "joga."], "Societal oversight of power is the most inalienable right of free citizens.", ["c1-civic-transparency"]),
                sw("production", [{"prompt": "Write a vision statement for the future of Hungarian civil service.", "answer": "A jövő magyar közigazgatása a digitális hatékonyság, a teljes átláthatóság és a pártatlan szakmaiság hármas pillérén nyugszik, amelyben az állam a polgárok megbecsült partnere."}], ["c1-civic-transparency"]),
                mc("grammar", "check", "Mi képezi a professzionális közszolgálat legfőbb erkölcsi mércéjét?", [
                    "A pártatlan, törvényes eljárás és a közérdek megkérdőjelezhetetlen szolgálata.",
                    "A magánvagyon gyarapítása hivatali idő alatt.",
                    "A döntések eltitkolása a nyilvánosság elől."
                ], 0, ["c1-civic-transparency"])
            ]
        }
    ]

    for l in disc_lessons:
        emit_instructional_lesson(8, "discourse", l, disc_title, disc_intro if l["num"] == 1 else None)

    # Combined world story
    write_json(
        f"stories/world/c1/{slug}.json",
        {
            "id": f"story.c1.world.{slug}",
            "title": "A közszolgálat, az átláthatóság és a polgári jogvédelem krónikája",
            "level": "C1",
            "type": "world",
            "summary": "Comprehensive chronicle of Hungarian public administration, civic oversight, and institutional integrity: from Mikszáth's gentry bureaucracy, freedom of information requests, the Ombudsman institution, whistleblower protection, e-governance to civil watchdogs.",
            "paragraphs": [
                {"type": "narration", "text": "A modern közigazgatás az állam idegrendszere, amely meghatározza a polgárok mindennapi életének minőségét és a jogállam hitelét. Mikszáth Kálmán zseniális szatírái már a tizenkilencedik század végén leleplezték a vármegyei hivatalok protekcionista világát, ahol a magánérdek és az úri összeköttetés felülírta a törvény szavát."},
                {"type": "narration", "text": "A demokratikus rendszerváltást követően az információszabadság és a közérdekű adatigénylések forradalmasították a közéletet: kimondták, hogy a közpénzek elköltése nem lehet államtitok vagy üzleti tabu."},
                {"type": "narration", "text": "Az Alapvető Jogok Biztosa (ombudsman) erkölcsi tekintélyével és nyilvános ajánlásaival a legkiszolgáltatottabb csoportok szószólójává vált, míg a bejelentővédelmi rendszerek védőhálót vontak a belső korrupciót leleplező bátor munkavállalók köré."},
                {"type": "narration", "text": "A huszonegyedik században az Ügyfélkapu és a digitális közigazgatás új szintre emelte a hivatali hatékonyságot, miközben a digitális szakadék áthidalása új esélyegyenlőségi feladatokat teremtett."},
                {"type": "narration", "text": "Ez a folyamat ma a civil watchodog szervezetek éber ellenőrzésében és a modern hivatásetika megerősítésében csúcsosodik ki, emlékeztetve arra, hogy a közszolgálat nem hatalmi monopólium, hanem a polgárok tisztességes és átlátható szolgálata."}
            ]
        }
    )

    # Discourse Consolidation
    emit_consolidation_lesson(
        8,
        "discourse",
        f"c1-{slug}-consolidation",
        disc_title,
        [
            "I can navigate public interest data requests (közérdekű adatigénylés) and Freedom of Information rules.",
            "I can analyze the mandate and reports of the Parliamentary Ombudsman (Alapvető Jogok Biztosa).",
            "I can evaluate whistleblower protection, e-governance systems, and civil society watchdog oversight."
        ],
        [
            mc("grammar", "recognize", "Mi minősül közérdekű adatnak a hatályos magyar jogszabályok szerint?", [
                "A közfeladatot ellátó szerv tevékenységére és a közpénzek felhasználására vonatkozó információ.",
                "A magánszemélyek orvosi titkai.",
                "Kizárólag a katonai haditervek."
            ], 0, ["c1-civic-transparency"]),
            mc("grammar", "recognize", "Milyen eszközzel lép fel az Alapvető Jogok Biztosa a jogsértésekkel szemben?", [
                "Nyilvános vizsgálati jelentésekkel és hivatalos ajánlásokkal.",
                "Hadsereg bevetésével.",
                "Azonnali vagyonelkobzással."
            ], 0, ["c1-civic-transparency"]),
            match("vocabulary", "recognize", [["közérdekű adat", "public interest data"], ["ombudsman", "fundamental rights commissioner"], ["közérdekű bejelentő", "whistleblower"], ["Ügyfélkapu", "Client Gate portal"], ["közbeszerzés", "public procurement"]], ["c1-kozszolgalat-vocab"]),
            fb("vocabulary", "recall", "A belső korrupciót leleplező munkatársat a törvény védi a munkahelyi _____ szemben. (retaliation / megtorlással)", "megtorlással", "The employee uncovering internal corruption is protected by law against workplace retaliation.", ["c1-kozszolgalat-vocab"]),
            fb("vocabulary", "recall", "A közbeszerzések független társadalmi ellenőrzése a _____ kockázatok leghatékonyabb ellenszere. (corruption / korrupciós)", "korrupciós", "Independent societal oversight of public procurement is the most effective remedy against corruption risks.", ["c1-kozszolgalat-vocab"]),
            fb("grammar", "recall", "A közérdekű adatok kiadását a hatóság nem tagadhatja meg alaptalanul üzleti _____ hivatkozva. (secret / titokra)", "titokra", "The authority cannot refuse disclosure of public interest data unfounded citing trade secret.", ["c1-civic-transparency"]),
            fb("grammar", "context", "A digitalizáció során elengedhetetlen a digitális _____ áthidalása a kistelepüléseken élők számára. (divide / szakadék)", "szakadék", "During digitization it is indispensable to bridge the digital divide for those living in small settlements.", ["c1-civic-transparency"]),
            fb("grammar", "context", "A tisztviselő döntéseit kizárólag a jogszabályok és a szakmai _____ kell vezérelnie. (impartiality / pártatlanság)", "pártatlanság", "An official's decisions must be guided solely by statutes and professional impartiality.", ["c1-civic-transparency"]),
            mc("grammar", "context", "Melyik állítás foglalja össze legmélyebben a civil társadalom szerepét az államigazgatásban?", [
                "A civil szervezetek független őrködése a közpénzek felett a demokratikus immunrendszer működésének feltétele.",
                "A civil szervezeteknek nem szabad beleszólniuk az állam ügyeibe.",
                "A közigazgatás akkor a legjobb, ha nincsenek külső ellenőrzések."
            ], 0, ["c1-civic-transparency"]),
            sb("grammar", "produce", ["A", "közszolgálat", "legfőbb", "értéke", "a", "tisztesség,", "a", "szakértelem", "és", "az", "átláthatóság."], ["A", "közszolgálat", "legfőbb", "értéke", "a", "tisztesség,", "a", "szakértelem", "és", "az", "átláthatóság."], "The chief value of civil service is probity, expertise, and transparency.", ["c1-civic-transparency"]),
            sw("production", [{"prompt": "Write a critical reflection on the importance of whistleblower protection.", "answer": "A bejelentővédelem garanciája nélkül a szervezeti visszaélések rejtve maradnának; a bátor munkavállalók védelme a tiszta közélet nélkülözhetetlen feltétele."}], ["c1-civic-transparency"]),
            sw("production", [{"prompt": "Formulate a concluding thought on the future of transparent governance.", "answer": "Az átlátható állam nem fenyegetés a hatalom számára, hanem a polgári bizalom és a hosszú távú társadalmi stabilitás legbiztosabb alapköve."}], ["c1-civic-transparency"])
        ]
    )
    print("=== Finished C1 Unit 8 ===")


if __name__ == "__main__":
    generate_unit_8()
