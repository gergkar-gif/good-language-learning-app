#!/usr/bin/env python3
"""
Generator for Hungarian C1 First Dual Unit:
  - Track 1 (Core): Unit 1 — "The Architecture of Argument & Logical Cohesion" (c1-01)
  - Track 2 (Discourse): Unit 1 — "Language as Worldview: Humboldt, Kosztolányi & Cognitive Linguistics" (c1-nyelvfilozofia)
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASE = ROOT / "content" / "hu"


def write_json(rel_path: str, data: dict):
    path = BASE / rel_path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {path.relative_to(ROOT)}")


def mc(cat, stage, question, options, correct, teaches):
    res = {
        "id": "",
        "type": "multiple-choice",
        "category": cat,
        "stage": stage,
        "question": question,
        "options": options,
        "correct": correct,
    }
    if teaches:
        res["teaches"] = teaches
    return res


def match(cat, stage, pairs, teaches):
    return {
        "id": "",
        "type": "matching",
        "category": cat,
        "stage": stage,
        "pairs": pairs,
        "teaches": teaches,
    }


def fb(cat, stage, sentence, answer, english, teaches):
    assert "____" in sentence, f"Sentence must contain blank '____': {sentence}"
    assert english and len(english.strip()) > 0, "English translation required for fill-blank"
    return {
        "id": "",
        "type": "fill-blank",
        "category": cat,
        "stage": stage,
        "sentence": sentence,
        "answer": answer,
        "english": english,
        "teaches": teaches,
    }


def sb(cat, stage, tiles, solution, english, teaches):
    return {
        "id": "",
        "type": "sentence-builder",
        "category": cat,
        "stage": stage,
        "tiles": tiles,
        "solution": solution,
        "english": english,
        "teaches": teaches,
    }


def dc(stage, prompt, options, correct, teaches):
    return {
        "id": "",
        "type": "dialogue-complete",
        "category": "dialogue",
        "stage": stage,
        "prompt": prompt,
        "options": options,
        "correct": correct,
        "teaches": teaches,
    }


def sw(stage, template, teaches):
    return {
        "id": "",
        "type": "structured-writing",
        "category": "writing",
        "stage": stage,
        "template": template,
        "teaches": teaches,
    }


def update_registries():
    # 1. skill-registry.json
    sr_path = BASE / "indexes" / "skill-registry.json"
    sr = json.loads(sr_path.read_text(encoding="utf-8"))
    new_skills = {
        "c1-01-vocab": {"kind": "vocabulary"},
        "c1-nyelvfilozofia-vocab": {"kind": "vocabulary"},
        "c1-concessive-clauses": {"kind": "grammar"},
        "c1-correlative-balance": {"kind": "grammar"},
        "c1-antithesis-structuring": {"kind": "grammar"},
        "c1-epistemic-discourse": {"kind": "grammar"},
        "c1-essayistic-synthesis": {"kind": "grammar"},
        "c1-linguistic-relativity": {"kind": "grammar"},
        "c1-cognitive-metaphor": {"kind": "grammar"},
    }
    for k, v in new_skills.items():
        if k not in sr["skills"]:
            sr["skills"][k] = v
    sr_path.write_text(json.dumps(sr, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("Updated skill-registry.json")

    # 2. grammar-titles.json
    gt_path = BASE / "indexes" / "grammar-titles.json"
    gt = json.loads(gt_path.read_text(encoding="utf-8"))
    new_titles = {
        "c1-01-vocab": "reading",
        "c1-nyelvfilozofia-vocab": "reading",
        "c1-concessive-clauses": "high-register concessive clauses with jollehet and noha",
        "c1-correlative-balance": "correlative sentence balance and parallel structures",
        "c1-antithesis-structuring": "rhetorical antithesis and counter-thesis structuring",
        "c1-epistemic-discourse": "epistemic stance markers and logical consequence",
        "c1-essayistic-synthesis": "essayistic argumentation and rhetorical synthesis",
        "c1-linguistic-relativity": "linguistic relativity and philosophical discourse",
        "c1-cognitive-metaphor": "cognitive metaphors and spatial conceptualization",
    }
    for k, v in new_titles.items():
        gt[k] = v
    gt_path.write_text(json.dumps(gt, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("Updated grammar-titles.json")

    # 3. curriculum/units/c1.json
    unit_table = [
        {
            "title": "The Architecture of Argument & Logical Cohesion",
            "stems": [
                "c1-01-01",
                "c1-01-02",
                "c1-01-03",
                "c1-01-04",
                "c1-01-05",
                "c1-01-consolidation",
            ],
            "track": "core",
        },
        {
            "title": "Language as Worldview: Humboldt, Kosztolányi & Cognitive Linguistics",
            "stems": [
                "c1-nyelvfilozofia-01",
                "c1-nyelvfilozofia-02",
                "c1-nyelvfilozofia-03",
                "c1-nyelvfilozofia-04",
                "c1-nyelvfilozofia-05",
                "c1-nyelvfilozofia-consolidation",
            ],
            "track": "discourse",
        },
    ]
    u_path = BASE / "curriculum" / "units" / "c1.json"
    u_path.parent.mkdir(parents=True, exist_ok=True)
    u_path.write_text(json.dumps(unit_table, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("Wrote curriculum/units/c1.json")


def generate_core_unit_1():
    unit_title = "The Architecture of Argument & Logical Cohesion"
    unit_intro = [
        "At the C1 level, fluency evolves into rhetorical mastery. It is no longer enough to string sentences together accurately; you must orchestrate ideas, build multi-clause premises, and guide the listener through nuanced concessions and decisive counter-arguments.",
        "In this unit, inspired by Mihály Babits' seminal 1928 essay 'Az írástudók árulása' (The Treason of the Intellectuals), you will master high-register concessive connectors (jóllehet, ámbár, noha, holott, mindazonáltal), balanced correlatives, and the syntactic architecture of academic and essayistic Hungarian.",
    ]

    lessons_data = [
        {
            "stem": "c1-01-01",
            "num": 1,
            "title": "Concession and Counter-Argument: Jóllehet and Noha",
            "grammar_title": "High-Register Concessive Clauses: Jóllehet, Noha, and Ámbár",
            "grammar_skill": "c1-concessive-clauses",
            "goals": [
                "I can structure advanced concessions using jóllehet, noha, and ámbár.",
                "I can distinguish between pure concession (jóllehet) and contrastive adversative nuance (holott).",
                "I can express philosophical and intellectual premises using C1 abstract vocabulary.",
            ],
            "vocab": [
                {"lemma": "jóllehet", "translation": "although, albeit", "pos": "conjunction"},
                {"lemma": "mindazonáltal", "translation": "nevertheless, nonetheless", "pos": "adverb"},
                {"lemma": "noha", "translation": "although, even though", "pos": "conjunction"},
                {"lemma": "holott", "translation": "whereas, even though (contrary to expectation)", "pos": "conjunction"},
                {"lemma": "az érv", "translation": "argument", "pos": "noun"},
                {"lemma": "az érvelés", "translation": "argumentation, reasoning", "pos": "noun"},
                {"lemma": "megalapozott", "translation": "well-founded, justified", "pos": "adjective"},
                {"lemma": "vitatott", "translation": "disputed, contentious", "pos": "adjective"},
                {"lemma": "a tétel", "translation": "thesis, proposition", "pos": "noun"},
                {"lemma": "megcáfol", "translation": "to refute, disprove", "pos": "verb"},
                {"lemma": "kétségkívül", "translation": "undoubtedly, beyond doubt", "pos": "adverb"},
                {"lemma": "az álláspont", "translation": "standpoint, position", "pos": "noun"},
            ],
            "gr_text1": "In C1 formal Hungarian essays and debates, plain *bár* or *de* often lacks the precision needed to weigh conflicting evidence. High-register concessive conjunctions like *jóllehet*, *noha*, and *ámbár* introduce a subordinate clause acknowledging a valid counter-point before the main thesis is affirmed: *Jóllehet a gazdasági mutatók javulnak, a társadalmi feszültségek nem enyhülnek.*",
            "gr_text2": "Pay special attention to *holott*: unlike neutral *noha*, *holott* carries an adversative, almost indignant overtone, highlighting a stark contradiction between reality and expectation: *Mindenki elvárta a segítséget, holott senki sem tett érte semmit.*",
            "gr_table": [
                ["Jóllehet az elmélet tetszetős...", "Although the theory is appealing... (measured concession)"],
                ["Noha későn érkezett...", "Even though he arrived late... (formal concession)"],
                ["Ámbár elismerem az érdemeit...", "Albeit I acknowledge his merits... (elevated concession)"],
                ["Nem segített, holott megtehette volna.", "He didn't help, whereas he easily could have. (sharp contrast)"],
            ],
            "exercises": [
                mc("vocabulary", "introduce", "Which conjunction expresses an elevated, formal concession ('although, albeit') in C1 prose?", ["jóllehet", "mert", "ha"], 0, ["c1-01-vocab"]),
                mc("vocabulary", "introduce", "What is the meaning of the adjective 'megalapozott' in scholarly argumentation?", ["well-founded, solidly justified", "untested and speculative", "hastily assembled"], 0, ["c1-01-vocab"]),
                match("vocabulary", "controlled", [["jóllehet", "although"], ["mindazonáltal", "nevertheless"], ["holott", "whereas / even though"], ["megcáfol", "to refute"], ["az álláspont", "standpoint"]], ["c1-01-vocab"]),
                fb("grammar", "controlled", "A kutató kitartott az elmélete mellett, _____ a kísérleti eredmények nem igazolták azt. (although / even though)", "noha", "The researcher stuck to his theory, even though the experimental results did not confirm it.", ["c1-concessive-clauses"]),
                fb("grammar", "controlled", "A politikus elutasította a javaslatot, _____ korábban támogatásáról biztosította a reformokat. (whereas / contrary to expectations)", "holott", "The politician rejected the proposal, whereas earlier he had assured the reforms of his support.", ["c1-concessive-clauses"]),
                mc("grammar", "controlled", "Which sentence demonstrates the most authentic C1 register for conceding a point before introducing the main thesis?", [
                    "Jóllehet az érvelés megalapozottnak tűnik, a konklúzió mégis téves.",
                    "De az érvelés jó, de a konklúzió rossz.",
                    "Mert az érvelés megalapozott, azért a konklúzió jó.",
                ], 0, ["c1-concessive-clauses"]),
                fb("grammar", "practice", "_____ a szerző elismeri ellenfelei érdemeit, mindazonáltal cáfolja állításaikat. (Albeit / Although)", "Ámbár", "Albeit the author acknowledges the merits of his opponents, he nonetheless refutes their assertions.", ["c1-concessive-clauses"]),
                sb("grammar", "practice", ["Jóllehet", "a", "tétel", "vitatott,", "mégis", "sokan", "támogatják."], ["Jóllehet", "a", "tétel", "vitatott,", "mégis", "sokan", "támogatják."], "Although the thesis is contentious, many nevertheless support it.", ["c1-concessive-clauses"]),
                mc("grammar", "practice", "Why is 'holott' chosen instead of 'jóllehet' in 'Hallgatott a válságról, holott pontosan ismerte a tényeket'?", [
                    "Because it underscores an ironic, culpable contrast between knowledge and silence.",
                    "Because 'holott' can only refer to weather phenomena.",
                    "Because 'jóllehet' cannot be used with the past tense.",
                ], 0, ["c1-concessive-clauses"]),
                fb("vocabulary", "practice", "Az akadémiai bizottság alapos vizsgálat után döntő bizonyítékokkal _____ a feltevést. (refuted)", "megcáfolta", "Following a thorough investigation, the academic committee refuted the hypothesis with decisive evidence.", ["c1-01-vocab"]),
                dc("dialogue", [
                    {"speaker": "Professzor", "text": "Hogyan értékeli a kolléga által előterjesztett hipotézist?"},
                    {"speaker": "Kutató", "text": "_____ a hipotézis rendkívül eredeti, mindazonáltal hiányoznak mögüle a szilárd empirikus adatok."},
                ], ["Jóllehet", "Mivelhogy", "Ezért"], 0, ["c1-concessive-clauses"]),
                dc("dialogue", [
                    {"speaker": "Vitavezető", "text": "Elfogadja a bíráló bizottság álláspontját?"},
                    {"speaker": "Szerző", "text": "Nem fogadhatom el, _____ az észrevételek egy része kétségkívül megszívlelendő."},
                    {"speaker": "Vitavezető", "text": "Értem, tehát a fő premisszákat továbbra is fenntartja."},
                ], ["noha", "tehát", "minthogy"], 0, ["c1-concessive-clauses"]),
                sw("production", [{"prompt": "Write a formal sentence conceding that a theory is controversial, but asserting that it remains valid using 'Jóllehet'.", "answer": "Jóllehet az elmélet vitatott, mindazonáltal érvényes marad."}], ["c1-concessive-clauses"]),
                sw("production", [{"prompt": "Write a critical remark using 'holott' to emphasize that someone remained passive despite knowing the danger.", "answer": "Passzív maradt, holott pontosan látta a közeledő veszélyt."}], ["c1-concessive-clauses"]),
                mc("grammar", "check", "Which connective pair correctly sets up a nuanced concession and reaffirmation?", ["Jóllehet..., mindazonáltal...", "Ezért..., noha...", "Mert..., holott..."], 0, ["c1-concessive-clauses"]),
                fb("vocabulary", "check", "A szerző professzionális vitakultúráját dicséri, hogy minden egyes állítása szilárdan _____. (well-founded)", "megalapozott", "It praises the author's professional debate culture that each of his assertions is solidly well-founded.", ["c1-01-vocab"]),
            ],
        },
        {
            "stem": "c1-01-02",
            "num": 2,
            "title": "Parallelism and Correlative Balance",
            "grammar_title": "Correlative Sentence Balance: Egyfelől... másfelől and Nemhogy... de még... is",
            "grammar_skill": "c1-correlative-balance",
            "goals": [
                "I can balance competing perspectives using 'egyfelől... másfelől' and 'részben... részben'.",
                "I can construct scalar emphatic structures with 'nemhogy... de még... is'.",
                "I can build rhythmic, parallel periodic sentences (*körmondat*) in Hungarian.",
            ],
            "vocab": [
                {"lemma": "egyfelől", "translation": "on the one hand", "pos": "adverb"},
                {"lemma": "másfelől", "translation": "on the other hand", "pos": "adverb"},
                {"lemma": "nemhogy", "translation": "far from, let alone, not only... not", "pos": "conjunction"},
                {"lemma": "körmondat", "translation": "periodic sentence, complex balanced period", "pos": "noun"},
                {"lemma": "a mérlegelés", "translation": "weighing, deliberation", "pos": "noun"},
                {"lemma": "pártatlan", "translation": "impartial, unbiased", "pos": "adjective"},
                {"lemma": "az elfogultság", "translation": "bias, partiality", "pos": "noun"},
                {"lemma": "árusít", "translation": "to sell / compromise (principles)", "pos": "verb"},
                {"lemma": "a pártosság", "translation": "partisanship", "pos": "noun"},
                {"lemma": "összemérhetetlen", "translation": "incommensurable, incomparable", "pos": "adjective"},
                {"lemma": "kiegyensúlyozott", "translation": "balanced, even-keeled", "pos": "adjective"},
                {"lemma": "a szintézis", "translation": "synthesis", "pos": "noun"},
            ],
            "gr_text1": "Classical Hungarian essayistic rhetoric relies heavily on periodic symmetry (*körmondat*). Correlative pairs like *egyfelől... másfelől* (on the one hand... on the other hand) or *nemcsak... hanem... is* (not only... but also) establish an intellectual cadence that demonstrates rigorous deliberation (*mérlegelés*) and fairness (*pártatlanság*).",
            "gr_text2": "The scalar structure *nemhogy... de még... is* (far from doing X, even Y happened / not only did X not occur, but even Y...) requires careful syntactic control: the subordinate clause negated by *nemhogy* is followed by an escalated second clause marked by *de még... is*: *Nemhogy elismerte volna tévedését, de még a bírálóit vádolta meg.*",
            "gr_table": [
                ["Egyfelől tiszteletben tartja a hagyományt, másfelől...", "On the one hand he respects tradition, on the other hand..."],
                ["Nemhogy javult volna a helyzet, de még romlott is.", "Far from improving, the situation actually worsened."],
                ["Részben a fáradtságnak, részben a sietségnek tudható be.", "It can be attributed partly to fatigue, partly to haste."],
            ],
            "exercises": [
                mc("vocabulary", "introduce", "What does 'egyfelől... másfelől' introduce in an essay?", ["a pair of contrasting or complementary perspectives", "a sudden change of topic", "a chronological list of events"], 0, ["c1-01-vocab"]),
                mc("vocabulary", "introduce", "What does 'pártatlan' mean when describing an analyst or judge?", ["impartial, unbiased", "passionate and political", "indifferent and lazy"], 0, ["c1-01-vocab"]),
                match("vocabulary", "controlled", [["egyfelől", "on the one hand"], ["másfelől", "on the other hand"], ["nemhogy", "far from / let alone"], ["pártatlan", "impartial"], ["a szintézis", "synthesis"]], ["c1-01-vocab"]),
                fb("grammar", "controlled", "A döntéshozó _____ a gazdasági érdekeket vette figyelembe, másfelől a társadalmi elvárásokat. (on the one hand)", "egyfelől", "On the one hand the decision-maker took economic interests into account, on the other hand social expectations.", ["c1-correlative-balance"]),
                fb("grammar", "controlled", "A szerző _____ visszavonta volna állítását, de még újabb bizonyítékokat sorakoztatott fel mellette. (far from having / let alone)", "nemhogy", "Far from having withdrawn his claim, the author actually lined up further evidence in its favor.", ["c1-correlative-balance"]),
                mc("grammar", "controlled", "Which sentence correctly demonstrates the scalar escalation of 'nemhogy... de még... is'?", [
                    "Nemhogy segített volna nekünk, de még akadályozott is a munkában.",
                    "Nemhogy segített, de nem akadályozott.",
                    "Nemhogy segített volna, azért akadályozott.",
                ], 0, ["c1-correlative-balance"]),
                fb("grammar", "practice", "A tanulmány erénye, hogy a kérdést _____ mérlegelés után, elfogultság nélkül vizsgálja. (balanced / even-keeled)", "kiegyensúlyozott", "The virtue of the study is that it investigates the question after balanced deliberation, without bias.", ["c1-01-vocab"]),
                sb("grammar", "practice", ["Nemhogy", "engedett", "volna", "a", "nyomásnak,", "de", "még", "keményebben", "kiállt", "az", "igaza", "mellett."], ["Nemhogy", "engedett", "volna", "a", "nyomásnak,", "de", "még", "keményebben", "kiállt", "az", "igaza", "mellett."], "Far from yielding to the pressure, he stood up even more firmly for his truth.", ["c1-correlative-balance"]),
                mc("grammar", "practice", "What mood typically follows 'nemhogy' when expressing an unrealized expectation?", [
                    "Conditional mood (-na/-ne volna)",
                    "Simple future tense",
                    "Imperative only",
                ], 0, ["c1-correlative-balance"]),
                fb("vocabulary", "practice", "A bíráló bizottság tagjaitól szigorú _____ vártak el az intézményi érdekekkel szemben. (impartiality)", "pártatlanságot", "Strict impartiality was expected from the members of the review committee against institutional interests.", ["c1-01-vocab"]),
                dc("dialogue", [
                    {"speaker": "Esszéíró", "text": "Hogyan érdemes felépíteni egy ilyen kényes fejezetet?"},
                    {"speaker": "Szerkesztő", "text": "_____ mutassa be a kortárs vitákat, másfelől vázolja fel a történeti előzményeket is."},
                ], ["Egyfelől", "Ezért", "Minthogy"], 0, ["c1-correlative-balance"]),
                dc("dialogue", [
                    {"speaker": "Kritikus", "text": "Csillapodtak a kedélyek a könyv megjelenése után?"},
                    {"speaker": "Recenzens", "text": "Dehogy! _____ lecsendesedett volna a vita, de még élesebbé vált."},
                ], ["Nemhogy", "Bár", "Mintha"], 0, ["c1-correlative-balance"]),
                sw("production", [{"prompt": "Write a balanced sentence contrasting two aspects using 'Egyfelől... másfelől'.", "answer": "Egyfelől elismeri a reformok szükségességét, másfelől óva int az elhamarkodott döntésektől."}], ["c1-correlative-balance"]),
                sw("production", [{"prompt": "Write a sentence with 'nemhogy... de még... is' showing an unexpected escalation in behavior.", "answer": "Nemhogy bocsánatot kért volna, de még engem vádolt meg tévedéssel."}], ["c1-correlative-balance"]),
                mc("grammar", "check", "In C1 rhetoric, what is the term for a long, harmoniously balanced multi-clause sentence?", ["körmondat (periodic sentence)", "tőmondat", "szóhalmozás"], 0, ["c1-correlative-balance"]),
                fb("vocabulary", "check", "A két tudományág módszertani kiindulópontjai szinte teljesen _____. (incommensurable / incomparable)", "összemérhetetlenek", "The methodological starting points of the two disciplines are almost completely incommensurable.", ["c1-01-vocab"]),
            ],
        },
        {
            "stem": "c1-01-03",
            "num": 3,
            "title": "Structuring Antithesis and Counter-Thesis",
            "grammar_title": "Rhetorical Antithesis: Ezzel szemben, Ellenben, and Csakhogy",
            "grammar_skill": "c1-antithesis-structuring",
            "goals": [
                "I can formulate sharp antitheses using 'ezzel szemben', 'ellenben', and 'csakhogy'.",
                "I can dismantle an opposing thesis by isolating its internal contradictions.",
                "I can deploy high-register vocabulary of intellectual debate and philosophical critique.",
            ],
            "vocab": [
                {"lemma": "ezzel szemben", "translation": "in contrast to this, by contrast", "pos": "expression"},
                {"lemma": "ellenben", "translation": "on the other hand, whereas, however", "pos": "conjunction"},
                {"lemma": "csakhogy", "translation": "the trouble is that, except that, only", "pos": "conjunction"},
                {"lemma": "az ellentmondás", "translation": "contradiction", "pos": "noun"},
                {"lemma": "a visszásság", "translation": "anomaly, absurdity, grievance", "pos": "noun"},
                {"lemma": "álságos", "translation": "specious, hypocritical, disingenuous", "pos": "adjective"},
                {"lemma": "leleplez", "translation": "to unmask, expose", "pos": "verb"},
                {"lemma": "a következetlenség", "translation": "inconsistency", "pos": "noun"},
                {"lemma": "érveléstechnika", "translation": "argumentation technique, argumentation strategy", "pos": "noun"},
                {"lemma": "a premissza", "translation": "premise", "pos": "noun"},
                {"lemma": "csúsztatás", "translation": "distorted framing, deceptive spin", "pos": "noun"},
                {"lemma": "megdönthetetlen", "translation": "irrefutable", "pos": "adjective"},
            ],
            "gr_text1": "Antithesis (*ellentétezés*) is the engine of philosophical debate. While conversational Hungarian defaults to *viszont* or *pedig*, C1 written and public discourse employs *ezzel szemben* (standing at the head of the contrastive proposition) and *ellenben* (often positioned enclitically or at clause boundary) to create sharp analytical polarities: *A pozitivizmus a mérhető tényekre épít; ezzel szemben az egzisztencializmus a szubjektív tapasztalatot állítja a középpontba.*",
            "gr_text2": "The particle *csakhogy* introduces a pivotal obstacle or fatal flaw that punctures a seemingly sound argument: *Az elképzelés elméletben hibátlan, csakhogy figyelmen kívül hagyja az emberi természet esendőségét.* It signals to the reader that the preceding premise is about to be exposed as unrealistic or hypocritical (*álságos*).",
            "gr_table": [
                ["Ezzel szemben a valóság egészen más.", "In contrast to this, reality is entirely different."],
                ["A régiek hittek ebben; a modernek ellenben kételkednek.", "The ancients believed in this; moderns, however, doubt."],
                ["Szép terv, csakhogy megvalósíthatatlan.", "A fine plan, the trouble is that it is unrealizable."],
            ],
            "exercises": [
                mc("vocabulary", "introduce", "What does 'csakhogy' typically introduce in a philosophical critique?", ["a critical snag or fatal flaw in the argument", "an irrelevant historical date", "an agreement with the opponent"], 0, ["c1-01-vocab"]),
                mc("vocabulary", "introduce", "Which adjective characterizes an argument that sounds superficially pious but is actually deceptive?", ["álságos", "megalapozott", "pártatlan"], 0, ["c1-01-vocab"]),
                match("vocabulary", "controlled", [["ezzel szemben", "by contrast"], ["ellenben", "on the other hand / however"], ["csakhogy", "the snag is that"], ["az ellentmondás", "contradiction"], ["leleplez", "to unmask"]], ["c1-01-vocab"]),
                fb("grammar", "controlled", "A hagyományos elmélet a stabilitást hangsúlyozza; _____ a modern megközelítés a dinamikus változást tekinti alapnak. (in contrast to this)", "ezzel szemben", "The traditional theory emphasizes stability; in contrast to this, the modern approach considers dynamic change as foundational.", ["c1-antithesis-structuring"]),
                fb("grammar", "controlled", "Az elmélet logikailag kikezdhetetlennek tűnt, _____ az empirikus adatok hamar megcáfolták. (except that / the trouble was that)", "csakhogy", "The theory seemed logically unassailable, except that empirical data soon refuted it.", ["c1-antithesis-structuring"]),
                mc("grammar", "controlled", "Where does 'ezzel szemben' naturally sit in a contrasting periodic sentence?", [
                    "At the beginning of the contrastive clause, setting up the opposing thesis.",
                    "Exclusively at the very end of the paragraph.",
                    "Only after the verb, attached to an adjective.",
                ], 0, ["c1-antithesis-structuring"]),
                fb("grammar", "practice", "A dogmatikus gondolkodás merev szabályokat követ; a kritikai szellem _____ folytonosan rákérdez az alapokra. (on the other hand / however)", "ellenben", "Dogmatic thinking follows rigid rules; the critical mind, on the other hand, constantly interrogates the fundamentals.", ["c1-antithesis-structuring"]),
                sb("grammar", "practice", ["A", "terv", "ígéretesnek", "látszott,", "csakhogy", "senki", "sem", "vállalta", "a", "kivitelezést."], ["A", "terv", "ígéretesnek", "látszott,", "csakhogy", "senki", "sem", "vállalta", "a", "kivitelezést."], "The plan appeared promising, except that no one undertook its implementation.", ["c1-antithesis-structuring"]),
                mc("grammar", "practice", "What rhetorical purpose does an antithesis serve in Babits' essayistic style?", [
                    "It sharpens the boundary between ethical duty and political opportunism.",
                    "It avoids taking any firm stance on controversial issues.",
                    "It shortens sentences so that readers read faster.",
                ], 0, ["c1-antithesis-structuring"]),
                fb("vocabulary", "practice", "A bíráló cikk pontról pontra _____ a politikai pamfletben rejlő tudatos csúsztatásokat. (unmasked / exposed)", "leleplezte", "The review article unmasked point by point the conscious spin inherent in the political pamphlet.", ["c1-01-vocab"]),
                dc("dialogue", [
                    {"speaker": "Bíráló", "text": "Úgy tűnik, a szerző logikai következtetései levonhatók a premisszákból."},
                    {"speaker": "Recenzens", "text": "Igen, a levezetés formálisan helytálló, _____ maga a kiinduló premissza hamis."},
                ], ["csakhogy", "tehát", "mintegy"], 0, ["c1-antithesis-structuring"]),
                dc("dialogue", [
                    {"speaker": "Filozófus", "text": "Hogyan határozná meg a két iskola viszonyát?"},
                    {"speaker": "Vitapartner", "text": "Az egyik a külső determinációt vallja; a másik _____ az emberi szabadság feltétlenségét hirdeti."},
                ], ["ellenben", "hiszen", "ugyebár"], 0, ["c1-antithesis-structuring"]),
                sw("production", [{"prompt": "Write an antithesis setting up two opposing approaches using 'Ezzel szemben'.", "answer": "A korábbi vezetés halogatta a döntést; ezzel szemben az új elnökség azonnali intézkedéseket hozott."}], ["c1-antithesis-structuring"]),
                sw("production", [{"prompt": "Formulate a rebuttal using 'csakhogy' to point out a fundamental flaw.", "answer": "Az érvelés első pillantásra meggyőző, csakhogy alapvető ténybeli tévedésekre épül."}], ["c1-antithesis-structuring"]),
                mc("grammar", "check", "Which connective expresses a decisive counter-argument pointing out an unforeseen reality barrier?", ["csakhogy", "ugyanis", "vagyis"], 0, ["c1-antithesis-structuring"]),
                fb("vocabulary", "check", "Az esszéíró célja nem a kompromisszumkeresés volt, hanem a mélyben rejlő elvi _____ felmutatása. (contradictions)", "ellentmondások", "The essayist's aim was not to seek compromise, but to reveal the profound principled contradictions beneath the surface.", ["c1-01-vocab"]),
            ],
        },
        {
            "stem": "c1-01-04",
            "num": 4,
            "title": "Epistemic Stance and Logical Consequence",
            "grammar_title": "Epistemic Stance Markers: Ennek fényében, Mindebből következően, and Mindezek dacára",
            "grammar_skill": "c1-epistemic-discourse",
            "goals": [
                "I can frame conclusions and inferential leaps using 'ennek fényében' and 'mindebből következően'.",
                "I can maintain resilient argumentative positions using 'mindezek dacára' and 'ennek ellenére'.",
                "I can deploy high-level discourse markers of deductive synthesis in Hungarian.",
            ],
            "vocab": [
                {"lemma": "ennek fényében", "translation": "in light of this", "pos": "expression"},
                {"lemma": "mindebből következően", "translation": "consequently from all this, as a result of all this", "pos": "expression"},
                {"lemma": "mindezek dacára", "translation": "in spite of all these things, despite all this", "pos": "expression"},
                {"lemma": "a konklúzió", "translation": "conclusion", "pos": "noun"},
                {"lemma": "az okszerűség", "translation": "rationality, causality, logical necessity", "pos": "noun"},
                {"lemma": "cáfolhatatlan", "translation": "irrefutable, incontrovertible", "pos": "adjective"},
                {"lemma": "következtet", "translation": "to conclude, infer, deduce", "pos": "verb"},
                {"lemma": "az előfeltevés", "translation": "presupposition, premise", "pos": "noun"},
                {"lemma": "megkerülhetetlen", "translation": "unavoidable, inescapable", "pos": "adjective"},
                {"lemma": "a kórkép", "translation": "clinical picture, diagnostic assessment (of an era)", "pos": "noun"},
                {"lemma": "hovatovább", "translation": "increasingly, gradually, before long", "pos": "adverb"},
                {"lemma": "szükségszerűen", "translation": "necessarily, inevitably", "pos": "adverb"},
            ],
            "gr_text1": "Advanced argumentation requires explicit signaling of logical transitions. In C1 writing, instead of simple *ezért* or *így*, sophisticated authors use compound relational expressions like *ennek fényében* (in light of this) to re-evaluate previous evidence, or *mindebből következően* (consequently from all this) to launch a deductive breakthrough.",
            "gr_text2": "When holding firm against accumulated counter-evidence or adversity, *mindezek dacára* (in spite of all this) conveys a resolute rhetorical defiance: *A történelem tragédiái mindezek dacára sem tudták kioltani az egyetemes humanizmus eszméjét.* Note the postpositional behavior of *dacára* governing the sublative (*-ra/-re*).",
            "gr_table": [
                ["Ennek fényében újra kell értékelnünk az adatokat.", "In light of this, we must re-evaluate the data."],
                ["Mindebből következően a vád alaptalan.", "Consequently from all this, the accusation is groundless."],
                ["A nehézségek dacára folytatták a munkát.", "In spite of the difficulties, they continued the work."],
            ],
            "exercises": [
                mc("vocabulary", "introduce", "What does 'ennek fényében' indicate when starting a new paragraph?", ["that the following argument is evaluated through newly introduced facts", "that the lights have been turned on", "that the debate has been terminated"], 0, ["c1-01-vocab"]),
                mc("vocabulary", "introduce", "What does 'megkerülhetetlen' mean in literary or political critique?", ["inescapable, unavoidable, essential to address", "easy to bypass", "round and spherical"], 0, ["c1-01-vocab"]),
                match("vocabulary", "controlled", [["ennek fényében", "in light of this"], ["mindebből következően", "consequently from all this"], ["mindezek dacára", "in spite of all this"], ["megkerülhetetlen", "inescapable"], ["a konklúzió", "conclusion"]], ["c1-01-vocab"]),
                fb("grammar", "controlled", "A legfrissebb levéltári források feltárása után, _____ újra kell fogalmaznunk a korszakról alkotott képünket. (in light of this)", "ennek fényében", "Following the uncovering of the freshest archival sources, in light of this we must reformulate our picture of the era.", ["c1-epistemic-discourse"]),
                fb("grammar", "controlled", "A miniszter elveszítette a képviselők bizalmát; _____, lemondása elkerülhetetlenné vált. (consequently from all this)", "mindebből következően", "The minister lost the confidence of the representatives; consequently from all this, his resignation became unavoidable.", ["c1-epistemic-discourse"]),
                mc("grammar", "controlled", "Which expression expresses ethical resilience despite overwhelming historical catastrophe?", [
                    "Mindezek dacára megőrizték szellemi függetlenségüket.",
                    "Ezért elfelejtették a múltat.",
                    "Mert nem történt semmi baj.",
                ], 0, ["c1-epistemic-discourse"]),
                fb("grammar", "practice", "A politikai nyomás és a cenzúra fenyegetése _____, a folyóirat szerkesztői nem alkudtak meg. (in spite of / despite)", "dacára", "In spite of political pressure and the threat of censorship, the editors of the journal did not compromise.", ["c1-epistemic-discourse"]),
                sb("grammar", "practice", ["Ennek", "fényében", "a", "szerző", "következtetése", "szinte", "megkérdőjelezhetetlennek", "tűnik."], ["Ennek", "fényében", "a", "szerző", "következtetése", "szinte", "megkérdőjelezhetetlennek", "tűnik."], "In light of this, the author's conclusion seems almost unquestionable.", ["c1-epistemic-discourse"]),
                mc("grammar", "practice", "What case does the postposition 'dacára' govern in formal Hungarian?", [
                    "Sublative (-ra/-re: mindezek dacára)",
                    "Dative (-nak/-nek)",
                    "Ablative (-tól/-től)",
                ], 0, ["c1-epistemic-discourse"]),
                fb("vocabulary", "practice", "Babits esszéje döbbenetes _____ nyújt a két világháború közötti európai értelmiség válságáról. (clinical picture / diagnostic diagnosis)", "kórképet", "Babits' essay provides a staggering diagnostic diagnosis of the crisis of the interwar European intelligentsia.", ["c1-01-vocab"]),
                dc("dialogue", [
                    {"speaker": "Kutató", "text": "Az összes kísérleti modell ugyanazt a rendellenességet mutatta ki."},
                    {"speaker": "Témavezető", "text": "_____ le kell vonnunk a végső konklúziót: az elmélet revízióra szorul."},
                ], ["Mindebből következően", "Netalántán", "Ugyebár"], 0, ["c1-epistemic-discourse"]),
                dc("dialogue", [
                    {"speaker": "Újságíró", "text": "Hogyan értékeli a tárgyalások eredményét a tegnapi fejlemények után?"},
                    {"speaker": "Elemző", "text": "_____, a kompromisszum esélye minimálisra csökkent."},
                ], ["Ennek fényében", "Csakhogy", "Minthogy"], 0, ["c1-epistemic-discourse"]),
                sw("production", [{"prompt": "Write a sentence opening with 'Ennek fényében' that draws an inference from new facts.", "answer": "Ennek fényében világossá válik, hogy a korábbi döntések elhibázottak voltak."}], ["c1-epistemic-discourse"]),
                sw("production", [{"prompt": "Write an argumentative statement using 'mindezek dacára' indicating perseverance.", "answer": "Mindezek dacára a független kutatók folytatták a munkát a laboratóriumban."}], ["c1-epistemic-discourse"]),
                mc("grammar", "check", "Which connective phrase introduces the inevitable logical consequence derived from an entire chain of arguments?", ["mindebből következően", "habár", "ellenben"], 0, ["c1-epistemic-discourse"]),
                fb("vocabulary", "check", "A modern szellemtörténet számára Babits klasszikus vitairata ma is kihagyhatatlan és _____. (inescapable / unavoidable)", "megkerülhetetlen", "For modern intellectual history, Babits' classic polemical treatise remains indispensable and inescapable today.", ["c1-01-vocab"]),
            ],
        },
        {
            "stem": "c1-01-05",
            "num": 5,
            "title": "Essayistic Synthesis and Rhetorical Climax",
            "grammar_title": "Synthesizing C1 Argumentation: Period, Cadence, and Ethical Stance",
            "grammar_skill": "c1-essayistic-synthesis",
            "goals": [
                "I can analyze Mihály Babits' seminal essay 'Az írástudók árulása' with full stylistic sensitivity.",
                "I can synthesize concessions, correlatives, antitheses, and consequences in a multi-clause period.",
                "I can articulate an ethical and intellectual thesis in refined academic Hungarian.",
            ],
            "vocab": [
                {"lemma": "az írástudó", "translation": "intellectual, clerk (in Julien Benda's sense)", "pos": "noun"},
                {"lemma": "az árulás", "translation": "betrayal, treason", "pos": "noun"},
                {"lemma": "a szellem", "translation": "spirit, intellect, mind", "pos": "noun"},
                {"lemma": "egyetemes", "translation": "universal, catholic", "pos": "adjective"},
                {"lemma": "kiszolgál", "translation": "to serve obsequiously, cater to (a regime or trend)", "pos": "verb"},
                {"lemma": "az elhivatottság", "translation": "vocation, calling, dedication", "pos": "noun"},
                {"lemma": "megalkuvás", "translation": "compromise, opportunism, surrender of principle", "pos": "noun"},
                {"lemma": "a mulandóság", "translation": "transience, ephemerality", "pos": "noun"},
                {"lemma": "az örökkévalóság", "translation": "eternity", "pos": "noun"},
                {"lemma": "érdekvezérelt", "translation": "interest-driven, self-serving", "pos": "adjective"},
                {"lemma": "a méltóság", "translation": "dignity", "pos": "noun"},
                {"lemma": "erkölcsi", "translation": "moral, ethical", "pos": "adjective"},
            ],
            "gr_text1": "At the pinnacle of C1 Hungarian, syntax merges with ethics. In Mihály Babits' masterly 1928 treatise *Az írástudók árulása*, we observe the complete integration of every device studied in this unit: subordinate concessions (*jóllehet*), antithetical contrasts (*ezzel szemben*), parallel periodic balance (*nemcsak... hanem... is*), and resonant moral conclusions (*mindebből következően*).",
            "gr_text2": "Notice how Babits contrasts the transient political passions of the day (*a napi politika mulandó láza*) with the eternal standards of truth, justice, and human dignity (*az igazság és emberség örök mércéje*). An intellectual who trades universal values for tribal or partisan advantage commits what Julien Benda called 'the treason of the clerks'.",
            "gr_table": [
                ["Jóllehet a kor követelményei szorítóak...", "Although the demands of the age are pressing... (concession)"],
                ["...az írástudó mégsem szolgálhatja ki a mulandó hatalmat...", "...the intellectual nevertheless cannot cater to transient power... (antithesis)"],
                ["...mindebből következően felelőssége egyetemes.", "...consequently from all this, his responsibility is universal. (consequence)"],
            ],
            "exercises": [
                mc("vocabulary", "introduce", "What does Babits mean by the term 'írástudó'?", ["the intellectual whose vocation is to uphold universal spiritual and moral truths", "anyone who literally knows the alphabet", "a paid government scribe"], 0, ["c1-01-vocab"]),
                mc("vocabulary", "introduce", "What constitutes the 'treason' (árulás) according to Babits?", ["subordinating universal truth and justice to partisan political interests", "leaving the country without permission", "writing bad poetry"], 0, ["c1-01-vocab"]),
                match("vocabulary", "controlled", [["az írástudó", "intellectual / clerk"], ["az árulás", "treason / betrayal"], ["egyetemes", "universal"], ["megalkuvás", "opportunism / surrender of principle"], ["a méltóság", "dignity"]], ["c1-01-vocab"]),
                fb("grammar", "controlled", "_____ a politika világa gyors és látványos sikereket ígér, az igazi szellemi munka mindazonáltal hosszú távú elköteleződést követel. (Although / Albeit)", "Jóllehet", "Although the world of politics promises swift and spectacular successes, true intellectual work nonetheless requires long-term commitment.", ["c1-essayistic-synthesis"]),
                fb("grammar", "controlled", "Az írástudó nemhogy kiszolgálná a hatalmi érdekeket, _____ bátran rámutat a rendszer visszásságaira is. (but even / but also)", "de még", "Far from catering to power interests, the intellectual even boldly points out the anomalies of the system.", ["c1-essayistic-synthesis"]),
                mc("grammar", "controlled", "Which sentence achieves the most elevated ethical cadence in the spirit of Babits?", [
                    "Jóllehet a tömegek pillanatnyi sikerekre vágynak, az írástudó feladata mindezek dacára az örök értékek őrzése.",
                    "Mert a tömeg sikert akar, azért az író is sikert akar.",
                    "De a politika rossz, de a szellem jó.",
                ], 0, ["c1-essayistic-synthesis"]),
                fb("grammar", "practice", "A szerző elutasítja az elvtelen _____, és mindvégig hű marad eredeti eszményeihez. (opportunism / compromise of principles)", "megalkuvást", "The author rejects unprincipled opportunism, and remains faithful throughout to his original ideals.", ["c1-01-vocab"]),
                sb("grammar", "practice", ["Az", "írástudó", "hivatása", "nem", "a", "hatalom", "kiszolgálása,", "hanem", "az", "igazság", "kimondása."], ["Az", "írástudó", "hivatása", "nem", "a", "hatalom", "kiszolgálása,", "hanem", "az", "igazság", "kimondása."], "The vocation of the intellectual is not the serving of power, but the speaking of truth.", ["c1-essayistic-synthesis"]),
                mc("grammar", "practice", "How does the periodic sentence structure (*körmondat*) reinforce the ethical authority of the author?", [
                    "By methodically anticipating objections and resolving them through balanced, disciplined logic.",
                    "By confounding the reader with endless jargon.",
                    "By proving that the author read many foreign books.",
                ], 0, ["c1-essayistic-synthesis"]),
                fb("vocabulary", "practice", "A humanista szellem legfőbb kötelessége, hogy a mulandó divatokkal szemben az _____ értékeket képviselje. (universal)", "egyetemes", "The highest duty of the humanist spirit is to represent universal values against ephemeral fads.", ["c1-01-vocab"]),
                dc("dialogue", [
                    {"speaker": "Egyetemi hallgató", "text": "Van-e még értelme ma Babits esszéjét olvasni a digitális tömegmédia korában?"},
                    {"speaker": "Irodalomtörténész", "text": "_____ a történelmi díszletek megváltoztak, az intellektuális integritás dilemmája ma még időszerűbb, mint valaha."},
                ], ["Jóllehet", "Ezért", "Minthogy"], 0, ["c1-essayistic-synthesis"]),
                dc("dialogue", [
                    {"speaker": "Filozófus", "text": "Hogyan kerülheti el az értelmiségi a szellemi árulást?"},
                    {"speaker": "Kolléga", "text": "Úgy, hogy nem enged az érdekvezérelt pragmatizmusnak, és mindezek dacára kitart az elvei mellett."},
                ], ["kitart az elvei mellett", "feladja a céljait", "csendben marad"], 0, ["c1-essayistic-synthesis"]),
                sw("production", [{"prompt": "Write a synthesis sentence summarizing the ethical duty of the writer in a crisis.", "answer": "Jóllehet a politikai nyomás elviselhetetlennek tűnik, az írástudó kötelessége mindazonáltal az igazság képviselete."}], ["c1-essayistic-synthesis"]),
                sw("production", [{"prompt": "Formulate a concluding thought on intellectual integrity using 'Mindebből következően'.", "answer": "Mindebből következően a szellemi ember hitelessége kizárólag a meg nem alkuvó függetlenségén alapulhat."}], ["c1-essayistic-synthesis"]),
                mc("reading", "practice", "Babits szövegében mi fenyegeti leginkább a modern kultúrát?", [
                    "Az, hogy a szellemi elit feladja egyetemes bírói szerepét, és a politikai gyűlölet eszközévé válik.",
                    "A papír és a könyvnyomtatás drágulása.",
                    "A külföldi utazások korlátozása.",
                ], 0, None),
                mc("reading", "practice", "Hogyan viszonyul az esszé az 'örökkévalóság' és a 'mulandóság' kettősségéhez?", [
                    "Az írástudó feladata a mulandó érdekek helyett az örök mércék képviselete.",
                    "A mulandóság sokkal fontosabb, mert a pillanatban kell élni.",
                    "A két fogalom között nincs semmiféle különbség.",
                ], 0, None),
            ],
            "story": {
                "slug": "c1-01-babits",
                "author": "Babits Mihály",
                "work": "Az írástudók árulása (1928)",
                "title": "Az írástudók felelőssége és a szellem függetlensége",
                "summary": "Babits Mihály reflections on Julien Benda's treatise: the tragic temptation of intellectuals to abandon their universal, transcendent mission and become instruments of transient political passions and tribal hatred.",
                "characters": ["Babits Mihály", "Julien Benda"],
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "Amikor Julien Benda francia gondolkodó a huszadik század harmadik évtizedében megírta híres könyvét a 'klerikusok', vagyis az írástudók árulásáról, nem egyszerűen politikai röpiratot adott közre, hanem az európai kultúra legmélyebb válságára tapintott rá. Babits Mihály a Nyugat hasábjain azonnal felismerte e mű prófétai súlyát. Az írástudó feladata ugyanis az emberiség kezdete óta az volt, hogy a puszta anyagi kényszerek és a hatalmi harcok zűrzavarában felmutassa az igazság, a jog és az emberség örök mércéjét.",
                    },
                    {
                        "type": "narration",
                        "text": "Jóllehet a modern kor embere büszke tudományos és technikai vívmányaira, a szellemi élet mégis példátlan veszedelembe sodródott. A veszedelem lényege nem a barbárság külső támadásában rejlik, hanem a belső elhivatottság feladásában. Az újkor írástudói közül egyre többen álltak be a napi politika szolgálatába: nemhogy fékezték volna a tömeghisztériát és a nacionalista gyűlöletet, de még szalonképessé és intellektuálisan igazolttá is tették a legvadabb szenvedélyeket.",
                    },
                    {
                        "type": "narration",
                        "text": "Ezzel szemben a klasszikus európai hagyomány mindig abból indult ki, hogy az igazság nem a győztesek kiváltsága, és nem az éppen uralkodó rezsimek szeszélye szerint formálódik. Sokkal inkább olyan transzcendens, egyetemes mérce, amelynek fényében minden világi hatalom tökéletlennek és mulandónak mutatkozik. Amikor egy filozófus, költő vagy tudós lemond erről a bírói szuverenitásról, és a szellem szentélyét a pártpolitikai küzdőtér részévé teszi, elköveti a legsúlyosabb bűnt, amelyet gondolkodó ember elkövethet: az árulást.",
                    },
                    {
                        "type": "narration",
                        "text": "Mindezek dacára Babits nem vesztette el teljesen a reményét. Bár pontosan látta a közeledő totalitárius viharokat, és tudta, hogy a tiszta hangot gyakran túlharsogja a demagógia lármája, mégis megalkuvás nélkül hirdette a szellem autonómiáját. Az írástudó nem zárkózhat elefántcsonttoronyba, de nem is adhatja el a lelkét a hatalom pillanatnyi kegyeiért. Hivatása nem az, hogy a korszellem kiszolgálója legyen, hanem az, hogy a korszellem lelkiismereteként őrködjön az emberi méltóság felett.",
                    },
                    {
                        "type": "narration",
                        "text": "Mindebből következően a tanuló, aki a magyar nyelv legmagasabb rétegeit kutatja, Babits soraiban nemcsak stílusbeli mintát, hanem erkölcsi iránytűt is talál. A magyar próza ezen a szinten már nem szavak véletlen egymásutánja, hanem felelősségteljes gondolkodás: küzdelem a pontosságért, a szabadságért és az igazságért egy olyan világban, amely szüntelenül arra csábít, hogy felejtsük el az örök mércéket.",
                    },
                ],
            },
        },
    ]

    for l in lessons_data:
        stem = l["stem"]
        # 1. Vocabulary
        write_json(
            f"vocabulary/c1/{stem}-voc.json",
            {
                "id": f"vocab.c1.01.{l['num']:02d}",
                "lesson": stem,
                "title": f"C1 Core Vocabulary — {l['title']}",
                "theme": "The Architecture of Argument",
                "words": l["vocab"],
            },
        )

        # 2. Grammar
        gr_slug = l["grammar_skill"].replace("c1-", "")
        write_json(
            f"grammar/c1/{stem}-a-gr.json",
            {
                "id": f"grammar.c1.01.{l['num']:02d}.{gr_slug}",
                "title": l["grammar_title"],
                "sections": [
                    {"type": "text", "title": "The Structural Mechanism", "content": l["gr_text1"]},
                    {"type": "text", "title": "Rhetorical Application & Stance", "content": l["gr_text2"]},
                    {"type": "table", "title": "Patterns in Context", "rows": l["gr_table"]},
                ],
            },
        )

        # 3. Exercises
        ex_list = []
        for idx, ex in enumerate(l["exercises"], start=1):
            ex_copy = dict(ex)
            if ex_copy["category"] == "reading":
                ex_copy["id"] = f"{stem}-reading-{idx}"
            else:
                stage = ex_copy.get("stage", "practice")
                ex_copy["id"] = f"{stem}-{stage}-{idx}"
            ex_list.append(ex_copy)

        write_json(f"exercises/c1/{stem}-ex.json", {"lesson": stem, "exercises": ex_list})

        # 4. Story (only lesson 5 has classic story)
        if "story" in l:
            s = l["story"]
            write_json(
                f"stories/classics/c1/{s['slug']}.json",
                {
                    "id": f"story.c1.classics.{s['slug']}",
                    "title": s["title"],
                    "level": "C1",
                    "type": "classic",
                    "author": s["author"],
                    "work": s["work"],
                    "summary": s["summary"],
                    "characters": s["characters"],
                    "paragraphs": s["paragraphs"],
                },
            )

        # 5. Lesson JSON
        sections = []
        if l["num"] == 1:
            sections.append({"type": "intro", "title": f"Unit 1: {unit_title}", "body": unit_intro})
        sections.append({"type": "goal", "title": "Lesson Goals", "items": l["goals"]})
        sections.append({"type": "recycle", "title": "Quick Review"})
        sections.append({"type": "grammar", "title": l["grammar_title"], "ref": f"grammar/c1/{stem}-a-gr.json"})
        sections.append({"type": "vocabulary", "title": "Lesson Vocabulary", "ref": f"vocabulary/c1/{stem}-voc.json"})

        # Exercise groups
        intro_refs = [e["id"] for e in ex_list if e.get("stage") == "introduce"]
        if intro_refs:
            sections.append({"type": "exercise-group", "title": "Introduce", "ref": f"exercises/c1/{stem}-ex.json", "exerciseRefs": intro_refs})

        controlled_refs = [e["id"] for e in ex_list if e.get("stage") == "controlled"]
        if controlled_refs:
            sections.append({"type": "exercise-group", "title": "Controlled", "ref": f"exercises/c1/{stem}-ex.json", "exerciseRefs": controlled_refs})

        practice_refs = [e["id"] for e in ex_list if e.get("stage") == "practice" and e.get("category") != "reading"]
        if practice_refs:
            sections.append({"type": "exercise-group", "title": "Practice", "ref": f"exercises/c1/{stem}-ex.json", "exerciseRefs": practice_refs})

        if "story" in l:
            sections.append({"type": "story", "title": f"Reading: {l['story']['title']}", "ref": f"stories/classics/c1/{l['story']['slug']}.json"})
            reading_refs = [e["id"] for e in ex_list if e.get("category") == "reading"]
            if reading_refs:
                sections.append({"type": "exercise-group", "title": "Reading Comprehension", "ref": f"exercises/c1/{stem}-ex.json", "exerciseRefs": reading_refs})

        dialogue_refs = [e["id"] for e in ex_list if e.get("stage") == "dialogue" or e.get("category") == "dialogue"]
        if dialogue_refs:
            sections.append({"type": "exercise-group", "title": "Dialogue", "ref": f"exercises/c1/{stem}-ex.json", "exerciseRefs": dialogue_refs})

        prod_refs = [e["id"] for e in ex_list if e.get("stage") == "production" or e.get("category") == "writing"]
        if prod_refs:
            sections.append({"type": "exercise-group", "title": "Production", "ref": f"exercises/c1/{stem}-ex.json", "exerciseRefs": prod_refs})

        sections.append({"type": "srs", "title": "Add to Review"})

        check_refs = [e["id"] for e in ex_list if e.get("stage") == "check"]
        if check_refs:
            sections.append({"type": "exercise-group", "title": "Check", "ref": f"exercises/c1/{stem}-ex.json", "exerciseRefs": check_refs})

        sections.append({"type": "checklist", "title": "Can you do this?", "items": l["goals"]})

        lesson_json = {
            "id": f"lesson.c1.{stem[3:]}",
            "unit": 1,
            "title": l["title"],
            "level": "C1",
            "grammar": l["grammar_title"],
            "goal": l["goals"],
            "sections": sections,
        }
        write_json(f"lessons/c1/{stem}.json", lesson_json)

    # 6. Core Consolidation Lesson (c1-01-consolidation)
    cons_stem = "c1-01-consolidation"
    cons_goals = [
        "I can recognize and analyze high-register concessive, correlative, and antithetical structures.",
        "I can recall C1 vocabulary of philosophical debate and intellectual ethics.",
        "I can produce multi-clause periodic sentences with flawless logical cohesion.",
    ]
    cons_exercises = [
        mc("grammar", "recognize", "Melyik mondat fejezi ki a legpontosabban a megalapozott elméleti engedményt?", [
            "Jóllehet a hipotézis vitatott, mindazonáltal számos empirikus megfigyelés támasztja alá.",
            "Mert a hipotézis rossz, azért nem hiszünk benne.",
            "De a hipotézis jó, de mégsem működik.",
        ], 0, ["c1-concessive-clauses"]),
        mc("grammar", "recognize", "Milyen funkciót tölt be a 'nemhogy... de még... is' szerkezet?", [
            "Skaláris fokozást fejez ki egy elmaradt várakozás és egy meglepő túlteljesítés között.",
            "Kizárólag egyszerű időbeli egymásutániságot jelöl.",
            "Két dolog teljes azonosságát hangsúlyozza.",
        ], 0, ["c1-correlative-balance"]),
        match("vocabulary", "recognize", [["mindazonáltal", "nevertheless"], ["holott", "whereas / contrary to expectations"], ["álságos", "specious / hypocritical"], ["kórkép", "diagnostic picture"], ["megkerülhetetlen", "inescapable"]], ["c1-01-vocab"]),
        fb("vocabulary", "recall", "A szerző nem vett részt a politikai csatározásokban, mert elutasított minden elvtelen _____. (compromise / opportunism)", "megalkuvást", "The author did not participate in political battles because he rejected all unprincipled compromise.", ["c1-01-vocab"]),
        fb("vocabulary", "recall", "Babits esszéje az európai kultúra válságáról szóló legfontosabb szellemi _____. (polemical treatise / manifesto)", "vitairat", "Babits' essay is the most important intellectual polemical treatise on the crisis of European culture.", ["c1-01-vocab"]),
        fb("grammar", "recall", "A professzor _____ elismerte a hibáját, de még a tanítványait hibáztatta a félreértésért. (far from having / let alone)", "nemhogy", "Far from having acknowledged his error, the professor even blamed his students for the misunderstanding.", ["c1-correlative-balance"]),
        fb("grammar", "context", "A kísérlet első pillantásra sikeresnek bizonyult; _____, a részletes mérések kimutatták az eljárás hibáit. (in contrast to this)", "ezzel szemben", "The experiment proved successful at first glance; in contrast to this, detailed measurements revealed the errors of the procedure.", ["c1-antithesis-structuring"]),
        fb("grammar", "context", "A könyvtári források hiányosak voltak; _____ dacára a kutatócsoport rekonstruálta a szöveget. (in spite of all these things)", "mindezek", "Library sources were deficient; in spite of all these things, the research group reconstructed the text.", ["c1-epistemic-discourse"]),
        mc("grammar", "context", "Hogyan értékelhető a 'csakhogy' használata a tudományos kritikában?", [
            "Rámutat arra a döntő elvi vagy gyakorlati hibára, amely megdönti az ellenfél tézisét.",
            "Egyszerűen az 'és' kötőszó szinonimája.",
            "Csak a mondat legvégén állhat kérdő hangsúllyal.",
        ], 0, ["c1-antithesis-structuring"]),
        sb("grammar", "produce", ["Mindebből", "következően", "az", "értelmiség", "nem", "adhatja", "fel", "a", "függetlenségét."], ["Mindebből", "következően", "az", "értelmiség", "nem", "adhatja", "fel", "a", "függetlenségét."], "Consequently from all this, the intelligentsia cannot give up its independence.", ["c1-epistemic-discourse"]),
        sw("production", [{"prompt": "Write a complex C1 periodic sentence summarizing the duty of an intellectual using 'Jóllehet' and 'mindazonáltal'.", "answer": "Jóllehet a pillanatnyi érdekek mást diktálnak, az írástudó mindazonáltal az egyetemes igazság mellett kötelezi el magát."}], ["c1-essayistic-synthesis"]),
        sw("production", [{"prompt": "Formulate a strong conclusion using 'Ennek fényében'.", "answer": "Ennek fényében világossá válik, hogy a szellemi autonómia védelme nem luxus, hanem morális alapkövetelmény."}], ["c1-essayistic-synthesis"]),
    ]

    c_ex_list = []
    for idx, ex in enumerate(cons_exercises, start=1):
        ex_copy = dict(ex)
        ex_copy["id"] = f"{cons_stem}-{idx}"
        c_ex_list.append(ex_copy)

    write_json(f"exercises/c1/{cons_stem}-ex.json", {"lesson": cons_stem, "exercises": c_ex_list})

    cons_sections = [
        {"type": "goal", "title": "Consolidation Goals", "items": cons_goals},
        {"type": "recycle", "title": "Quick Review"},
        {"type": "exercise-group", "title": "Recognize", "ref": f"exercises/c1/{cons_stem}-ex.json", "exerciseRefs": [f"{cons_stem}-1", f"{cons_stem}-2", f"{cons_stem}-3"]},
        {"type": "exercise-group", "title": "Recall", "ref": f"exercises/c1/{cons_stem}-ex.json", "exerciseRefs": [f"{cons_stem}-4", f"{cons_stem}-5", f"{cons_stem}-6"]},
        {"type": "exercise-group", "title": "In Context", "ref": f"exercises/c1/{cons_stem}-ex.json", "exerciseRefs": [f"{cons_stem}-7", f"{cons_stem}-8", f"{cons_stem}-9"]},
        {"type": "exercise-group", "title": "Produce", "ref": f"exercises/c1/{cons_stem}-ex.json", "exerciseRefs": [f"{cons_stem}-10", f"{cons_stem}-11", f"{cons_stem}-12"]},
        {"type": "checklist", "title": "Can you do this?", "items": cons_goals},
    ]

    write_json(
        f"lessons/c1/{cons_stem}.json",
        {
            "id": f"lesson.c1.{cons_stem[3:]}",
            "unit": 1,
            "title": "Unit 1 Consolidation: The Architecture of Argument & Logical Cohesion",
            "level": "C1",
            "sections": cons_sections,
        },
    )


def generate_discourse_unit_1():
    slug = "nyelvfilozofia"
    unit_title = "Language as Worldview: Humboldt, Kosztolányi & Cognitive Linguistics"
    intro_body = [
        "Does language merely label an already existing external reality, or does its grammatical structure actively shape how its speakers perceive time, space, causality, and human relation? This fundamental question lies at the heart of Hungarian intellectual history.",
        "In this unit, you will journey from Wilhelm von Humboldt's concept of the 'inner form of language' and Sámuel Brassai's linguistic discoveries to Dezső Kosztolányi's passionate defense of mother-tongue consciousness, the Sapir-Whorf relativity hypothesis, and modern cognitive metaphors in Hungarian syntax.",
    ]

    lessons_data = [
        {
            "num": 1,
            "stem": f"c1-{slug}-01",
            "title": "The Inner Form of Language: Humboldt's Legacy",
            "grammar_title": "Linguistic Relativity and the Inner Form: Innere Sprachform",
            "grammar_skill": "c1-linguistic-relativity",
            "goals": [
                "I can discuss Wilhelm von Humboldt's concept of language as a dynamic creative activity (energeia).",
                "I can analyze how Hungarian agglutinative morphology reflects an 'inner form of language'.",
                "I can use high-register philosophical and linguistic terminology in Hungarian.",
            ],
            "vocab": [
                {"lemma": "a világkép", "translation": "worldview, conceptual worldview", "pos": "noun"},
                {"lemma": "a szemléletmód", "translation": "way of seeing, mindset, outlook", "pos": "noun"},
                {"lemma": "ragragozó", "translation": "agglutinative", "pos": "adjective"},
                {"lemma": "a nyelvkincs", "translation": "lexical treasure, vocabulary stock", "pos": "noun"},
                {"lemma": "a fogalomalkotás", "translation": "conceptualization, concept formation", "pos": "noun"},
                {"lemma": "kifejezőerő", "translation": "expressive power", "pos": "noun"},
                {"lemma": "az önkifejezés", "translation": "self-expression", "pos": "noun"},
                {"lemma": "az anyanyelv", "translation": "mother tongue, native language", "pos": "noun"},
                {"lemma": "elválaszthatatlan", "translation": "inseparable", "pos": "adjective"},
                {"lemma": "a közvetítő", "translation": "mediator, vehicle, conduit", "pos": "noun"},
                {"lemma": "tükröz", "translation": "to reflect, mirror", "pos": "verb"},
                {"lemma": "a sajátosság", "translation": "peculiarity, characteristic feature", "pos": "noun"},
            ],
            "gr_text1": "Wilhelm von Humboldt famously asserted that language is not a completed product (*ergon*), but a living, creative activity (*energeia*). Each human tongue possesses a distinctive 'inner form' (*innere Sprachform*) that channels how sensations are transformed into concepts.",
            "gr_text2": "When writing about linguistic philosophy in Hungarian, notice how nominal derivations (-ás/-és) and relational compounds (*szemléletmód, világkép, fogalomalkotás*) allow dense conceptual synthesis: *A nyelv nem passzív közvetítő eszköz, hanem a gondolkodás aktív alakítója.*",
            "gr_table": [
                ["A nyelv belső formája...", "The inner form of language... (Humboldtian concept)"],
                ["A fogalomalkotás sajátosságai...", "The specific characteristics of concept formation..."],
                ["Elválaszthatatlan a nemzet szellemi életétől.", "Inseparable from the spiritual/intellectual life of the nation."],
            ],
            "story_seg": {
                "seg_slug": "belsoforma",
                "title": "A nyelv belső formája: Humboldt öröksége",
                "summary": "Wilhelm von Humboldt's profound insight into the creative essence of language and how 19th-century Hungarian thinkers recognized their mother tongue's distinct grammatical genius.",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "A tizenkilencedik század hajnalán Wilhelm von Humboldt forradalmi gondolattal rázta fel az európai filozófiát: a nyelv nem készen kapott jelek halmaza, nem holt leltár, amellyel a külvilág tárgyait utólag megnevezzük, hanem maga az emberi szellem eleven alkotóereje. Minden egyes nyelv sajátos szemléletmódot, egyedi világképet hordoz magában, amely láthatatlanul, de kitörölhetetlenül meghatározza beszélői gondolkodását.",
                    },
                    {
                        "type": "narration",
                        "text": "Humboldt szerint minden nyelvnek létezik egy 'belső formája' (innere Sprachform), egy olyan mélyen gyökerező szerkezeti elv, amely a hangalakot a fogalomalkotással összeköti. Az agglutináló, ragragozó nyelvek – mint amilyen a magyar is – ebben a felfogásban különleges helyet foglalnak el. A szótövekhez tapadó képzők, jelek és ragok rendszere nemcsak elképesztő pontosságot és hajlékonyságot biztosít, hanem a gondolatok végtelen variációs gazdagságát is lehetővé teszi.",
                    },
                    {
                        "type": "narration",
                        "text": "A magyar reformkor gondolkodói azonnal megértették ennek a tételnek a történelmi jelentőségét. Ha a nyelv valóban a gondolkodás formája, akkor az anyanyelv művelése nem pusztán esztétikai vagy irodalmi kérdés, hanem a nemzeti önismeret és a modern polgári felemelkedés záloga. Egy nép mindaddig nem lehet valóban szabad és szuverén, amíg saját szellemi géniuszát nem a saját anyanyelvén éli meg és fogalmazza meg.",
                    },
                ],
            },
            "exercises": [
                mc("vocabulary", "practice", "Mit értett Humboldt a nyelv 'belső formája' (innere Sprachform) alatt?", [
                    "Azt a sajátos szerkezeti és szellemi elvet, amely egy adott nyelv fogalomalkotását és világképét meghatározza.",
                    "A nyomtatott betűk tipográfiai szépségét.",
                    "A szótárak alfabetikus elrendezését.",
                ], 0, ["c1-nyelvfilozofia-vocab"]),
                fb("vocabulary", "practice", "A kutatók szerint az anyanyelv elválaszthatatlan a beszélő közösség általános _____ alakulásától. (worldview)", "világképének", "According to researchers, the mother tongue is inseparable from the evolution of the speech community's general worldview.", ["c1-nyelvfilozofia-vocab"]),
                fb("grammar", "practice", "A filozófus hangsúlyozta, hogy a nyelv nem holt termék, hanem a szellem állandó és dinamikus _____ tevékenysége. (creative / expressive)", "önkifejező", "The philosopher emphasized that language is not a dead product, but the constant and dynamic self-expressive activity of the mind.", ["c1-linguistic-relativity"]),
                mc("grammar", "practice", "Melyik állítás tükrözi a humboldti nyelvfilozófia lényegét?", [
                    "A nyelv a gondolat aktív alakítója és szellemi közege, nem csupán passzív közvetítő eszköz.",
                    "Minden nyelv azonos szavakat használ, csak a kiejtésük tér el.",
                    "A nyelvtan kizárólag a nyelvészek számára érdekes szabálygyűjtemény.",
                ], 0, ["c1-linguistic-relativity"]),
                sb("grammar", "practice", ["Minden", "egyes", "nyelv", "egy", "sajátos", "szemléletmódot", "hordoz", "magában."], ["Minden", "egyes", "nyelv", "egy", "sajátos", "szemléletmódot", "hordoz", "magában."], "Each single language carries within itself a distinctive way of seeing.", ["c1-linguistic-relativity"]),
                match("vocabulary", "practice", [["szemléletmód", "way of seeing / outlook"], ["világkép", "worldview"], ["ragragozó", "agglutinative"], ["fogalomalkotás", "concept formation"], ["elválaszthatatlan", "inseparable"]], ["c1-nyelvfilozofia-vocab"]),
                dc("dialogue", [
                    {"speaker": "Egyetemi hallgató", "text": "Hogyan befolyásolja az agglutináló szerkezet a fogalmak megalkotását?"},
                    {"speaker": "Nyelvész", "text": "A gazdag ragrendszer révén a magyar mondat rendkívül rugalmasan képes finom viszonyokat kifejezni."},
                ], ["rendkívül rugalmasan", "nagyon nehezen", "egyáltalán nem"], 0, ["c1-linguistic-relativity"]),
                sw("production", [{"prompt": "Write a philosophical statement in Hungarian about how language shapes our perception of reality.", "answer": "A nyelv nem pusztán leírja a világot, hanem aktívan alakítja és strukturálja a valóságról alkotott tapasztalatainkat."}], ["c1-linguistic-relativity"]),
            ],
        },
        {
            "num": 2,
            "stem": f"c1-{slug}-02",
            "title": "The Secret Life of Words: Kosztolányi's Poetics",
            "grammar_title": "Expressive Register and Affective Stylistics: Kosztolányi's Poetics",
            "grammar_skill": "c1-linguistic-relativity",
            "goals": [
                "I can analyze Dezső Kosztolányi's essayistic defense of the Hungarian language.",
                "I can discuss his famous list of the ten most beautiful Hungarian words (*a tíz legszebb szó*).",
                "I can evaluate sensory, emotional, and phonetic qualities of Hungarian vocabulary.",
            ],
            "vocab": [
                {"lemma": "a hangulatfestés", "translation": "onomatopoeic atmosphere, tone-painting", "pos": "noun"},
                {"lemma": "a dallamosság", "translation": "melodiousness, euphony", "pos": "noun"},
                {"lemma": "kifinomult", "translation": "refined, sophisticated", "pos": "adjective"},
                {"lemma": "a zeneiség", "translation": "musicality", "pos": "noun"},
                {"lemma": "felülmúlhatatlan", "translation": "insurpassable, second to none", "pos": "adjective"},
                {"lemma": "az érzelmi töltet", "translation": "emotional charge, emotive resonance", "pos": "noun"},
                {"lemma": "a hangzásvilág", "translation": "soundscape, phonetic texture", "pos": "noun"},
                {"lemma": "az anyanyelvi öntudat", "translation": "mother-tongue consciousness", "pos": "noun"},
                {"lemma": "ragyog", "translation": "to shine, radiate", "pos": "verb"},
                {"lemma": "elmélyült", "translation": "profound, deep, immersed", "pos": "adjective"},
                {"lemma": "a varázs", "translation": "magic, enchantment, spell", "pos": "noun"},
                {"lemma": "egyedülálló", "translation": "unique, singular", "pos": "adjective"},
            ],
            "gr_text1": "Dezső Kosztolányi was not merely a poet and novelist; he was Hungarian literature's most passionate philologist-artist. In his legendary essays collected in *Nyelv és lélek* (Language and Soul), he argued that words have a physical body: weight, temperature, scent, and melodic cadence (*dallamosság*).",
            "gr_text2": "In 1933, when asked to select the ten most beautiful Hungarian words, Kosztolányi chose: *láng, gyöngy, anya, ősz, szűz, kard, csók, vér, szív, sír*. Notice that none of these are abstract foreign borrowings; they are primordial, mostly monosyllabic roots charged with existential, physical, and mythic resonance.",
            "gr_table": [
                ["láng, gyöngy, anya, ősz...", "flame, pearl, mother, autumn... (sensory primordial roots)"],
                ["A szavaknak testük és lelkük van.", "Words possess both a body and a soul."],
                ["A hangzás és az értelem elválaszthatatlan egysége.", "The inseparable unity of sound and meaning."],
            ],
            "story_seg": {
                "seg_slug": "tizlegszebb",
                "title": "A szavak titkos élete: Kosztolányi és a tíz legszebb szó",
                "summary": "Kosztolányi Dezső's poetic immersion into the sound, soul, and associative majesty of the Hungarian language.",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "Kosztolányi Dezső számára a magyar nyelv nem egyszerű kommunikációs kódrendszer volt, hanem a legcsodálatosabb, legbonyolultabb hangszer, amelyen ember valaha játszhatott. Gyermekkorától kezdve megszállottan gyűjtötte és ízlelgette a szavakat. Úgy vélte, hogy minden szónak sajátos aurája, színe, tapintása és hőmérséklete van, amelyet a mindennapi beszéd rutinja gyakran elhomályosít.",
                    },
                    {
                        "type": "narration",
                        "text": "Amikor egy párizsi lap mintájára megkérdezték tőle, melyik a tíz legszebb magyar szó, Kosztolányi nem elvont fogalmakat vagy tudományos szakkifejezéseket választott. Listája – láng, gyöngy, anya, ősz, szűz, kard, csók, vér, szív, sír – szinte kizárólag egytagú, ősi, érzéki szavakból állt. Olyan szavak ezek, amelyekben a hangzás tömör zeneisége és a jelentés emberi mélysége tökéletes harmóniában forr össze.",
                    },
                    {
                        "type": "narration",
                        "text": "Kosztolányi tanítása szerint az anyanyelvhez való viszonyunk az önazonosságunk legmélyebb alapja. Idegen nyelveket megtanulhatunk kiválóan, beszélhetünk rajtuk pontosan és szellemesen, de csak azon az egyetlen nyelven tudunk valóban sírni, szeretni és félelem nélkül megnyilatkozni, amelyet az édesanyánk altatódalaival együtt szívtunk magunkba.",
                    },
                ],
            },
            "exercises": [
                mc("vocabulary", "practice", "Milyen szempontok alapján választotta ki Kosztolányi a tíz legszebb magyar szót?", [
                    "A hangzás zeneisége, az érzéki tömörség és az ősi érzelmi mélység alapján.",
                    "A szavak latin etimológiája és tudományos pontossága szerint.",
                    "Aszerint, hogy melyik szót használják a leggyakrabban a hivatalos jogi nyelvben.",
                ], 0, ["c1-nyelvfilozofia-vocab"]),
                fb("vocabulary", "practice", "Kosztolányi esszéiben a szavak nem pusztán fogalmi jelek, hanem gazdag _____ rendelkező eleven lények. (emotional resonance / charge)", "érzelmi töltettel", "In Kosztolányi's essays, words are not merely conceptual signs, but living beings possessing rich emotional resonance.", ["c1-nyelvfilozofia-vocab"]),
                fb("grammar", "practice", "A költő szerint a magyar nyelv rendkívüli _____ a magánhangzók tisztaságából és a mássalhangzók ritmusából fakad. (melodiousness / euphony)", "dallamossága", "According to the poet, the extraordinary melodiousness of the Hungarian language springs from the purity of vowels and rhythm of consonants.", ["c1-linguistic-relativity"]),
                mc("grammar", "practice", "Miért tekintette Kosztolányi felülmúlhatatlannak az anyanyelvi tapasztalatot?", [
                    "Mert a legmélyebb emberi érzelmek és az autentikus önkifejezés csak az anyanyelven élhető át maradéktalanul.",
                    "Mert nem szeretett külföldi országokba utazni.",
                    "Mert szerinte más nyelveknek egyáltalán nincs zeneiségük.",
                ], 0, ["c1-linguistic-relativity"]),
                sb("grammar", "practice", ["A", "szavaknak", "sajátos", "színük,", "illatuk", "és", "zeneiségük", "van."], ["A", "szavaknak", "sajátos", "színük,", "illatuk", "és", "zeneiségük", "van."], "Words have their own distinctive color, scent, and musicality.", ["c1-linguistic-relativity"]),
                match("vocabulary", "practice", [["hangulatfestés", "tone-painting"], ["dallamosság", "melodiousness"], ["kifinomult", "refined"], ["felülmúlhatatlan", "insurpassable"], ["az érzelmi töltet", "emotional charge"]], ["c1-nyelvfilozofia-vocab"]),
                dc("dialogue", [
                    {"speaker": "Kritikus", "text": "Nem túlzás egy írótól, hogy a szavak fizikai testéről és illatáról beszél?"},
                    {"speaker": "Kosztolányi-kutató", "text": "Egyáltalán nem: Kosztolányi számára a stílus maga a legmagasabb rendű érzéki valóság volt."},
                ], ["Egyáltalán nem", "Valószínűleg igen", "Nem érdekes"], 0, ["c1-linguistic-relativity"]),
                sw("production", [{"prompt": "Write an aesthetic reflection in Hungarian on the musicality and emotional power of words.", "answer": "A nyelv legszebb szavai nemcsak gondolatokat közvetítenek, hanem zenei dallamosságukkal a lélek legmélyebb rétegeit szólítják meg."}], ["c1-linguistic-relativity"]),
            ],
        },
        {
            "num": 3,
            "stem": f"c1-{slug}-03",
            "title": "Linguistic Relativity: Does Language Shape Thought?",
            "grammar_title": "The Sapir-Whorf Hypothesis and Linguistic Relativity in Hungarian",
            "grammar_skill": "c1-linguistic-relativity",
            "goals": [
                "I can evaluate the strong vs. weak versions of the Sapir-Whorf linguistic relativity hypothesis.",
                "I can examine how Hungarian preverbs (*igekötők*) shape aspectual and cognitive framing.",
                "I can debate linguistic determinism using precise C1 academic terminology.",
            ],
            "vocab": [
                {"lemma": "a nyelvi relativizmus", "translation": "linguistic relativity", "pos": "noun"},
                {"lemma": "a determinizmus", "translation": "determinism", "pos": "noun"},
                {"lemma": "az igekötő", "translation": "verbal prefix, preverb", "pos": "noun"},
                {"lemma": "a szemlélet", "translation": "perspective, perception, intuition", "pos": "noun"},
                {"lemma": "a cselekvésbelső", "translation": "Aktionsart, internal manner of action", "pos": "noun"},
                {"lemma": "befolyásol", "translation": "to influence", "pos": "verb"},
                {"lemma": "az észlelés", "translation": "perception, cognition", "pos": "noun"},
                {"lemma": "a kognitív", "translation": "cognitive", "pos": "adjective"},
                {"lemma": "viszonylagos", "translation": "relative", "pos": "adjective"},
                {"lemma": "az összefüggés", "translation": "correlation, connection, interrelation", "pos": "noun"},
                {"lemma": "megkérdőjelez", "translation": "to question, call into question", "pos": "verb"},
                {"lemma": "a kísérlet", "translation": "experiment, attempt", "pos": "noun"},
            ],
            "gr_text1": "The Sapir-Whorf hypothesis proposes that the structure of a language influences its speakers' worldview and cognitive processes. The 'strong' version (linguistic determinism) claims language dictates what we can think; the modern 'weak' version claims language gently guides our attentional habits and perceptual salience.",
            "gr_text2": "In Hungarian, verbal prefixes (*meg-, el-, ki-, be-, át-, fel-, le-*) do not merely mark completion (telicity); they encode fine-grained aspectual contours (*cselekvésbelső* / Aktionsart): *olvasgat* vs. *kiolvas* vs. *átolvas* vs. *félreolvas*. Speakers of Hungarian are grammatically trained to pay constant attention to the boundary, direction, and completeness of every event.",
            "gr_table": [
                ["A nyelvi relativizmus gyenge változata...", "The weak version of linguistic relativity... (attentional bias)"],
                ["Az igekötők finom szemantikai hálója...", "The delicate semantic network of verbal prefixes..."],
                ["Befolyásolja az események észlelését.", "It influences the perception of events."],
            ],
            "story_seg": {
                "seg_slug": "relativizmus",
                "title": "Nyelvi relativizmus: Valóban másképp látjuk a világot?",
                "summary": "Exploring whether speaking Hungarian conditions our minds to attend to aspect, spatial orientation, and narrative boundaries in unique ways.",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "A huszonnegyedik század derekán fellángolt a vita Edward Sapir és Benjamin Lee Whorf elmélete nyomán: vajon az anyanyelvünk csupán eszköz-e a gondolataink kifejezésére, vagy inkább láthatatlan börtön – illetve tágas ablak –, amely meghatározza, mit és hogyan vagyunk képesek felfogni a valóságból? Ez a kérdés nyelvi relativizmus néven vonult be a tudománytörténetbe.",
                    },
                    {
                        "type": "narration",
                        "text": "Bár a nyelvi determinizmus merev formáját – miszerint nem is tudnánk olyan dolgokra gondolni, amelyekre nincs szavunk – a modern kognitív tudomány elvetette, a relativizmus mérsékeltebb formája ma is virágzik. A kísérletek egyértelműen bizonyítják, hogy egy nyelv nyelvtani kategóriái finoman, de folyamatosan irányítják a beszélők figyelmét. A magyar nyelvtan például a világ egyik legösszetettebb igekötő-rendszerével rendelkezik.",
                    },
                    {
                        "type": "narration",
                        "text": "Amikor egy magyar beszélő egy cselekvésről számol be, a nyelvtan szinte rákényszeríti, hogy megjelölje annak irányát, határát és eredményességét. Nem mindegy, hogy valaki 'ír', 'megír', 'átír', 'beír', 'kiír' vagy éppen 'összeír' valamit. Ez a rendkívüli szemantikai pontosság azt eredményezi, hogy a magyarul gondolkodó elme ösztönösen az események belső szerkezetére és folyamatára összpontosít.",
                    },
                ],
            },
            "exercises": [
                mc("vocabulary", "practice", "Mit állít a nyelvi relativizmus mérsékelt (gyenge) változata?", [
                    "A nyelvtan és a szókincs finoman irányítja a beszélők figyelmét és észlelési szokásait.",
                    "A nyelv teljesen lehetetlenné teszi az elvont gondolkodást.",
                    "A gondolkodásnak semmi köze sincs a beszélt nyelvhez.",
                ], 0, ["c1-nyelvfilozofia-vocab"]),
                fb("vocabulary", "practice", "A magyar nyelvben az _____ rendkívül gazdag rendszere pontosan jelzi a cselekvés irányát és eredményét. (verbal prefixes / preverbs)", "igekötők", "In the Hungarian language, the extremely rich system of verbal prefixes indicates precisely the direction and result of the action.", ["c1-nyelvfilozofia-vocab"]),
                fb("grammar", "practice", "A kognitív kutatások kimutatták a nyelvi kategóriák és a vizuális _____ közötti szoros összefüggést. (perception / cognition)", "észlelés", "Cognitive research has revealed the close connection between linguistic categories and visual perception.", ["c1-linguistic-relativity"]),
                mc("grammar", "practice", "Milyen szerepet játszanak az igekötők a magyar eseményszemléletben?", [
                    "Kódolják a cselekvés határát, teljességét és finom aspektuális árnyalatait.",
                    "Csak a mondat alanyának számát és nemét mutatják.",
                    "Kizárólag a múlt idő kifejezésére szolgálnak.",
                ], 0, ["c1-linguistic-relativity"]),
                sb("grammar", "practice", ["A", "nyelvtani", "szerkezet", "befolyásolja", "a", "valóság", "megismerésének", "módját."], ["A", "nyelvtani", "szerkezet", "befolyásolja", "a", "valóság", "megismerésének", "módját."], "The grammatical structure influences the way reality is known.", ["c1-linguistic-relativity"]),
                match("vocabulary", "practice", [["a determinizmus", "determinism"], ["az igekötő", "preverb / verbal prefix"], ["a szemlélet", "perspective / perception"], ["kognitív", "cognitive"], ["megkérdőjelez", "to call into question"]], ["c1-nyelvfilozofia-vocab"]),
                dc("dialogue", [
                    {"speaker": "Nyelvész", "text": "Valóban másképp érzékeli az időt egy magyar beszélő az igekötők miatt?"},
                    {"speaker": "Kognitív kutató", "text": "Nem él más fizikai világban, de az események befejezettségére sokkal éberebben figyel."},
                ], ["sokkal éberebben figyel", "egyáltalán nem figyel", "mindent elfelejt"], 0, ["c1-linguistic-relativity"]),
                sw("production", [{"prompt": "Write a critical evaluation in Hungarian about the Sapir-Whorf hypothesis.", "answer": "Bár a nyelvi determinizmus túlzó állítás, az anyanyelv nyelvtani szerkezete kétségkívül alakítja kognitív fókuszunkat."}], ["c1-linguistic-relativity"]),
            ],
        },
        {
            "num": 4,
            "stem": f"c1-{slug}-04",
            "title": "Spatial Cognition and Metaphor in Hungarian Grammar",
            "grammar_title": "Cognitive Metaphors and Spatial Conceptualization in Hungarian",
            "grammar_skill": "c1-cognitive-metaphor",
            "goals": [
                "I can analyze spatial cases and postpositions as conceptual metaphors in Hungarian.",
                "I can decode abstract idioms based on the container, surface, and path schemas.",
                "I can formulate cognitive linguistic analyses of Hungarian figurative language.",
            ],
            "vocab": [
                {"lemma": "a fogalmi metafora", "translation": "conceptual metaphor", "pos": "noun"},
                {"lemma": "a térszemlélet", "translation": "spatial perception, spatial orientation", "pos": "noun"},
                {"lemma": "az elvont", "translation": "abstract", "pos": "adjective"},
                {"lemma": "a tartálymetafora", "translation": "container metaphor", "pos": "noun"},
                {"lemma": "a képi séma", "translation": "image schema", "pos": "noun"},
                {"lemma": "átvitt értelemben", "translation": "in a figurative sense, figuratively speaking", "pos": "expression"},
                {"lemma": "beágyazódik", "translation": "to become embedded", "pos": "verb"},
                {"lemma": "a viszonyrendszer", "translation": "system of relations, relational framework", "pos": "noun"},
                {"lemma": "megtestesít", "translation": "to embody, personify", "pos": "verb"},
                {"lemma": "a tájékozódás", "translation": "orientation, finding one's bearings", "pos": "noun"},
                {"lemma": "a kifejezésmód", "translation": "mode of expression, diction", "pos": "noun"},
                {"lemma": "mélyreható", "translation": "profound, deep, far-reaching", "pos": "adjective"},
            ],
            "gr_text1": "According to George Lakoff and Mark Johnson (*Metaphors We Live By*), human thought is fundamentally metaphorical: we map concrete physical and spatial experiences onto abstract domains. Hungarian, with its 3x3 spatial case system (interior, surface, proximity), is a masterclass in cognitive spatial mapping.",
            "gr_text2": "Abstract states are conceived as containers: *dühbe gurul* (rolls into anger), *kétségbe esik* (falls into doubt), *bízik valakiben* (trusts inside someone). Social roles and events are surfaces: *rajta van a sor* (the turn is upon him), *konferencián vesz részt* (participates upon a conference). Path and direction structures organize decisions: *dűlőre jut* (reaches a path ridge / agreement), *kifelé áll a szénája* (his hay sticks outward / he is about to be dismissed).",
            "gr_table": [
                ["bánatba merül, kétségbe esik...", "plunges into sorrow, falls into despair... (container metaphor: -ba/-be)"],
                ["kitart az elvei mellett...", "stands beside his principles... (postpositional loyalty schema)"],
                ["dűlőre jut, zsákutcába jut...", "reaches a cart-track, reaches a dead-end... (path & journey metaphor)"],
            ],
            "story_seg": {
                "seg_slug": "termetaforak",
                "title": "A tér szelleme: Kognitív metaforák a magyar nyelvben",
                "summary": "How Hungarian's 3-way spatial cases and bodily postpositions shape abstract philosophical thinking and everyday emotional metaphors.",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "A modern kognitív nyelvészet egyik legnagyobb felfedezése, hogy az emberi elme nem elvont matematikai szimbólumokban gondolkodik, hanem a test és a tér konkrét fizikai tapasztalataiból építi fel legbonyolultabb eszméit is. George Lakoff és Mark Johnson elmélete szerint a metafora nem puszta költői dísz, hanem a fogalmi gondolkodás alapvető eszköze: az elvont lelki és társadalmi állapotokat a fizikai tér viszonyaiként éljük meg.",
                    },
                    {
                        "type": "narration",
                        "text": "A magyar nyelv különösen látványos bizonyítéka ennek a törvénynek. A magyar esetrendszer hármas tagozódása – a 'hol?', 'hová?' és 'honnan?' kérdésekre felelő belső, felszíni és közelítő ragok – láthatatlan hálóként szövi át az absztrakt gondolkodást. Amikor kétségbeesünk, valójában egy sötét tartályba zuhanunk (-ba/-be); amikor valakiben megbízunk, a lelkünk belsejébe engedjük be őt (-ban/-ben); és amikor egy feladaton dolgozunk, egy felszínen hordozzuk a terhet (-on/-en/-ön).",
                    },
                    {
                        "type": "narration",
                        "text": "Ugyanez a téri logika uralja az emberi kapcsolatok kifejezéseit is. Ha valaki mellénk áll, hűséget és szolidaritást tanúsít; ha valakivel szembefordulunk, frontális konfliktust vállalunk; és ha valakinek a háta mögött beszélünk, a rejtett árulás terébe lépünk. A magyar nyelvtan tehát nemcsak szavakat ad a kezünkbe, hanem egy teljes, élő téri koordinátarendszert, amelyben a morális és intellektuális világ eligazodási pontjai kirajzolódnak.",
                    },
                ],
            },
            "exercises": [
                mc("vocabulary", "practice", "Hogyan működnek a fogalmi metaforák a kognitív nyelvészet szerint?", [
                    "A konkrét fizikai és téri tapasztalatokat vetítik rá az elvont lelki és szellemi fogalmakra.",
                    "Kizárólag a rímes költeményekben fordulnak elő.",
                    "A szótárakból teljesen kiirtandó nyelvtani hibák.",
                ], 0, ["c1-nyelvfilozofia-vocab"]),
                fb("vocabulary", "practice", "A magyar nyelvben a lelki állapotok kifejezésére gyakran a _____ metaforáját használjuk (pl. kétségbe esik, dühbe gurul). (container)", "tartály", "In the Hungarian language, for expressing mental states we often use the metaphor of the container.", ["c1-nyelvfilozofia-vocab"]),
                fb("grammar", "practice", "Amikor egy nehéz tárgyaláson végre megállapodunk, a magyar szólás szerint _____ jutunk. (to an agreement / resolution - path metaphor)", "dűlőre", "When in a difficult negotiation we finally agree, according to the Hungarian idiom we reach a resolution.", ["c1-cognitive-metaphor"]),
                mc("grammar", "practice", "Melyik kifejezés szemlélteti a felszínmetaforát a társadalmi szerepekben?", [
                    "rajta van a sor",
                    "erdőben sétál",
                    "ágyban fekszik",
                ], 0, ["c1-cognitive-metaphor"]),
                sb("grammar", "practice", ["Az", "elvont", "fogalmakat", "téri", "tapasztalatok", "révén", "értelmezzük."], ["Az", "elvont", "fogalmakat", "téri", "tapasztalatok", "révén", "értelmezzük."], "We interpret abstract concepts by means of spatial experiences.", ["c1-cognitive-metaphor"]),
                match("vocabulary", "practice", [["a fogalmi metafora", "conceptual metaphor"], ["a térszemlélet", "spatial perception"], ["átvitt értelemben", "figuratively speaking"], ["beágyazódik", "to become embedded"], ["a viszonyrendszer", "relational framework"]], ["c1-nyelvfilozofia-vocab"]),
                dc("dialogue", [
                    {"speaker": "Diák", "text": "Miért mondjuk, hogy 'bízom benned', miért a belső esetet használjuk?"},
                    {"speaker": "Tanár", "text": "Mert a másik embert metaforikusan egy védett belső térbe, a szívünkbe fogadjuk be."},
                ], ["védett belső térbe", "távoli városba", "másik szobába"], 0, ["c1-cognitive-metaphor"]),
                sw("production", [{"prompt": "Explain in Hungarian how spatial cases are used figuratively to express emotions.", "answer": "A magyar nyelv a belső esetragokat (-ba/-be, -ban/-ben) tartálymetaforaként használja az elvont lelki állapotok megélésére."}], ["c1-cognitive-metaphor"]),
            ],
        },
        {
            "num": 5,
            "stem": f"c1-{slug}-05",
            "title": "Digital Horizons: Hungarian in the Age of AI",
            "grammar_title": "Discourse on Linguistic Survival and the Digital Sphere",
            "grammar_skill": "c1-linguistic-relativity",
            "goals": [
                "I can analyze the challenges facing medium-sized languages in the era of large language models and global tech.",
                "I can debate linguistic sovereignty, automated translation, and language preservation.",
                "I can synthesize the unit's themes in an elevated C1 philosophical essay.",
            ],
            "vocab": [
                {"lemma": "a nyelvmegőrzés", "translation": "language preservation, maintenance", "pos": "noun"},
                {"lemma": "a mesterséges intelligencia", "translation": "artificial intelligence", "pos": "noun"},
                {"lemma": "a nyelvi szuverenitás", "translation": "linguistic sovereignty", "pos": "noun"},
                {"lemma": "a nyelvtechnológia", "translation": "language technology, computational linguistics", "pos": "noun"},
                {"lemma": "elsorvad", "translation": "to wither, atrophy", "pos": "verb"},
                {"lemma": "a homogenizáció", "translation": "homogenization", "pos": "noun"},
                {"lemma": "a sokszínűség", "translation": "diversity, plurality", "pos": "noun"},
                {"lemma": "a fenntarthatóság", "translation": "sustainability", "pos": "noun"},
                {"lemma": "kiszorít", "translation": "to squeeze out, displace, supplant", "pos": "verb"},
                {"lemma": "az életerő", "translation": "vitality, vigor", "pos": "noun"},
                {"lemma": "elkötelezett", "translation": "committed, dedicated", "pos": "adjective"},
                {"lemma": "a jövőkép", "translation": "vision of the future", "pos": "noun"},
            ],
            "gr_text1": "The 21st century confronts the Hungarian language with an unprecedented challenge: digital existence. If a medium-sized language (~13–15 million speakers) lacks representation in massive training corpora and digital ecosystems, it risks suffering functional domain loss (*tartományvesztés*), becoming restricted to domestic banter while science, business, and AI default to global English.",
            "gr_text2": "When writing about cultural sustainability, notice how C1 discourse bridges technological terminology with humanist philosophy: *A mesterséges intelligencia korában a nyelvi szuverenitás nem technikai részletkérdés, hanem a szellemi autonómia fenntartásának legfőbb záloga.*",
            "gr_table": [
                ["A digitális nyelvmegőrzés záloga...", "The guarantee of digital language preservation..."],
                ["Nem szorulhat a társalgási szintre.", "It must not be squeezed down to mere conversational register."],
                ["A kulturális sokszínűség védelmében.", "In defense of cultural diversity."],
            ],
            "story_seg": {
                "seg_slug": "digitalishorizont",
                "title": "Digitális horizont: A magyar nyelv megmaradása a mesterséges intelligencia korában",
                "summary": "Reflecting on whether Hungarian can maintain its full cognitive richness and sovereignty in the digital age of algorithms and large language models.",
                "paragraphs": [
                    {
                        "type": "narration",
                        "text": "A huszonegyedik század harmadik évtizedében a magyar nyelv történetének talán legdrámaibb fordulópontjához érkezett. Míg a tizenkilencedik században a latinnal és a némettel szemben kellett kivívni a nemzeti nyelv hivatalos jogait, ma a globális angol és a mesterséges intelligencia algoritmusai jelentik az igazi kihívást. A tét nem kisebb, mint hogy a magyar képes lesz-e teljes értékű digitális nyelvként fennmaradni a digitális univerzumban.",
                    },
                    {
                        "type": "narration",
                        "text": "A veszélyt nem a fizikai kihalás jelenti, hanem az úgynevezett funkcionális tartományvesztés. Ha a tudomány, a technológia, a gazdaság és a digitális kommunikáció legújabb rétegei elhagyják a magyar nyelvet, akkor az anyanyelv lassan a családi konyhák és a népművészeti fesztiválok nosztalgikus zárványává zsugorodhat. Ahhoz, hogy egy nyelv élő maradjon, minden új emberi tapasztalatot és technológiai felfedezést a saját szókincsével és logikájával kell megneveznie.",
                    },
                    {
                        "type": "narration",
                        "text": "A magyar kultúra életereje azonban mindig a megújulási képességében rejlett. Ahogyan Kazinczy korában tízezer új szóval vértezték fel a nyelvet, úgy ma a hazai nyelvtechnológusok és kutatók saját nemzeti nyelvi modelleket fejlesztenek. A magyar nyelv belső formája, játékossága és metaforikus mélysége nem múzeumi tárgy, hanem dinamikus jövőkép: a bizonyíték arra, hogy a szellem szabadsága a digitális korban is csak a nyelvek sokszínűségében maradhat fenn.",
                    },
                ],
            },
            "exercises": [
                mc("vocabulary", "practice", "Mit jelent a 'funkcionális tartományvesztés' a szociolingvisztikában?", [
                    "Azt a folyamatot, amikor egy nyelv bizonyos területekről (pl. tudomány, gazdaság, digitális világ) kiszorul.",
                    "Azt, hogy a szótárakból kitörlik a ritkán használt szavakat.",
                    "A nyelvtan szabályainak szándékos leegyszerűsítését.",
                ], 0, ["c1-nyelvfilozofia-vocab"]),
                fb("vocabulary", "practice", "A mesterséges intelligencia korszakában a nemzeti _____ megőrzése létfontosságú kulturális feladattá vált. (linguistic sovereignty)", "nyelvi szuverenitás", "In the era of artificial intelligence, the preservation of national linguistic sovereignty has become a vital cultural task.", ["c1-nyelvfilozofia-vocab"]),
                fb("grammar", "practice", "Ha egy nyelv nem képes lépést tartani a technológiai fejlődéssel, lassan _____ és perifériára szorul. (withers / atrophies)", "elsorvad", "If a language cannot keep pace with technological development, it slowly withers and is pushed to the periphery.", ["c1-linguistic-relativity"]),
                mc("grammar", "practice", "Hogyan maradhat fenn a magyar nyelv teljes értékű digitális kultúraként?", [
                    "Saját nyelvi modellek, digitális korpuszok építésével és a szaknyelvi szókincs folyamatos megújításával.",
                    "Úgy, hogy betiltják a külföldi technológiák használatát.",
                    "Kizárólag kézírásos levelezésre térve vissza.",
                ], 0, ["c1-linguistic-relativity"]),
                sb("grammar", "practice", ["A", "nyelvi", "sokszínűség", "megőrzése", "az", "egyetemes", "emberi", "kultúra", "közös", "felelőssége."], ["A", "nyelvi", "sokszínűség", "megőrzése", "az", "egyetemes", "emberi", "kultúra", "közös", "felelőssége."], "The preservation of linguistic diversity is the shared responsibility of universal human culture.", ["c1-linguistic-relativity"]),
                match("vocabulary", "practice", [["a nyelvmegőrzés", "language preservation"], ["elsorvad", "to wither"], ["a homogenizáció", "homogenization"], ["a sokszínűség", "diversity"], ["a jövőkép", "vision of the future"]], ["c1-nyelvfilozofia-vocab"]),
                dc("dialogue", [
                    {"speaker": "Kutató", "text": "Valóban veszélyben van egy 13 milliós nyelv a digitális világban?"},
                    {"speaker": "Nyelvtechnológus", "text": "Igen, ha nem építünk saját minőségi adatbázisokat és modern nyelvi modelleket."},
                ], ["Igen, ha nem építünk", "Nem, egyáltalán nincs", "Minden teljesen rendben van"], 0, ["c1-linguistic-relativity"]),
                sw("production", [{"prompt": "Write a visionary conclusion in Hungarian on why the survival of Hungarian matters for global intellectual diversity.", "answer": "A magyar nyelv megőrzése azért nélkülözhetetlen, mert egyedülálló logikájával és kifejezőerejével az emberi szellem pótolhatatlan dimenzióját képviseli."}], ["c1-linguistic-relativity"]),
            ],
        },
    ]

    serialized_parts = []
    for l in lessons_data:
        stem = l["stem"]

        # 1. Vocabulary
        write_json(
            f"vocabulary/c1/{stem}-voc.json",
            {
                "id": f"vocab.c1.{slug}.{l['num']:02d}",
                "lesson": stem,
                "title": f"C1 Discourse Vocabulary — {l['title']}",
                "theme": "Language as Worldview",
                "words": l["vocab"],
            },
        )

        # 2. Grammar
        gr_slug = l["grammar_skill"].replace("c1-", "")
        write_json(
            f"grammar/c1/{stem}-a-gr.json",
            {
                "id": f"grammar.c1.{slug}.{l['num']:02d}.{gr_slug}",
                "title": l["grammar_title"],
                "sections": [
                    {"type": "text", "title": "Philosophical & Societal Framework", "content": l["gr_text1"]},
                    {"type": "text", "title": "Linguistic Analysis", "content": l["gr_text2"]},
                    {"type": "table", "title": "Key Conceptual Paradigms", "rows": l["gr_table"]},
                ],
            },
        )

        # 3. Story Segment
        seg = l["story_seg"]
        seg_id = f"story.c1.world.{stem}-{seg['seg_slug']}"
        write_json(
            f"stories/world/c1/{stem}-{seg['seg_slug']}.json",
            {
                "id": seg_id,
                "title": seg["title"],
                "level": "C1",
                "lesson": l["num"],
                "order": l["num"],
                "type": "world",
                "summary": seg["summary"],
                "paragraphs": seg["paragraphs"],
            },
        )
        serialized_parts.extend(seg["paragraphs"])

        # 4. Exercises
        ex_list = []
        for idx, ex in enumerate(l["exercises"], start=1):
            ex_copy = dict(ex)
            ex_copy["id"] = f"{stem}.ex{idx:02d}"
            ex_list.append(ex_copy)

        write_json(f"exercises/c1/{stem}-ex.json", {"lesson": stem, "exercises": ex_list})

        # 5. Lesson JSON
        sections = []
        if l["num"] == 1:
            sections.append({"type": "intro", "title": unit_title, "body": intro_body})
        sections.append({"type": "goal", "title": "Lesson Goals", "items": l["goals"]})
        sections.append({"type": "recycle", "title": "Quick Review"})
        sections.append({"type": "story", "title": f"Reading: {seg['title']}", "ref": f"stories/world/c1/{stem}-{seg['seg_slug']}.json"})
        sections.append({"type": "vocabulary", "title": "Lesson Vocabulary", "ref": f"vocabulary/c1/{stem}-voc.json"})
        sections.append({"type": "grammar", "title": l["grammar_title"], "ref": f"grammar/c1/{stem}-a-gr.json"})
        sections.append({
            "type": "exercise-group",
            "title": "Practice",
            "ref": f"exercises/c1/{stem}-ex.json",
            "exerciseRefs": [e["id"] for e in ex_list],
        })
        sections.append({"type": "srs", "title": "Add to Review"})
        sections.append({"type": "checklist", "title": "Can you do this?", "items": l["goals"]})

        write_json(
            f"lessons/c1/{stem}.json",
            {
                "id": f"lesson.c1.{stem[3:]}",
                "unit": 1,
                "title": l["title"],
                "level": "C1",
                "grammar": l["grammar_title"],
                "goal": l["goals"],
                "sections": sections,
            },
        )

    # Combined Story for the serialized unit
    combined_story_id = f"story.c1.world.{slug}"
    write_json(
        f"stories/world/c1/{slug}.json",
        {
            "id": combined_story_id,
            "title": "A gondolat formája: Nyelv, kultúra és világkép",
            "level": "C1",
            "type": "world",
            "summary": "Complete 5-part serialized reflection on Wilhelm von Humboldt's inner form of language, Kosztolányi's poetics, linguistic relativity, cognitive spatial metaphors, and the survival of Hungarian in the age of AI.",
            "paragraphs": serialized_parts,
        },
    )

    # 6. Discourse Consolidation Lesson (c1-nyelvfilozofia-consolidation)
    cons_stem = f"c1-{slug}-consolidation"
    cons_goals = [
        "I can synthesize the philosophical arguments of Humboldt, Kosztolányi, and modern cognitive linguistics.",
        "I can recall high-level terminology of linguistic relativity and digital language preservation.",
        "I can produce structured reflections on the cultural and cognitive role of the Hungarian language.",
    ]
    cons_exercises = [
        mc("grammar", "recognize", "Mi a lényege a humboldti 'belső forma' (innere Sprachform) fogalmának?", [
            "Minden nyelv rendelkezik egy egyedi szellemi-nyelvtani szervezőelvvel, amely a világképet formálja.",
            "A nyelvtan kizárólag a kiejtés szabályait tartalmazza.",
            "A szavak alakja független a gondolkodástól.",
        ], 0, ["c1-linguistic-relativity"]),
        mc("vocabulary", "recognize", "Mit fejez ki a 'tartományvesztés' kifejezés?", [
            "Azt a folyamatot, amikor egy nyelv bizonyos szakmai vagy technológiai területekről kiszorul.",
            "Egy ország területének csökkenését egy háború után.",
            "A merevlemez adatvesztését egy technikai hiba miatt.",
        ], 0, ["c1-nyelvfilozofia-vocab"]),
        match("vocabulary", "recognize", [["a világkép", "worldview"], ["az igekötő", "preverb"], ["a dallamosság", "melodiousness"], ["elsorvad", "to wither"], ["a szuverenitás", "sovereignty"]], ["c1-nyelvfilozofia-vocab"]),
        fb("vocabulary", "recall", "Kosztolányi szerint az anyanyelv nyújtja az autentikus emberi _____ legmélyebb alapját. (self-expression)", "önkifejezés", "According to Kosztolányi, the mother tongue provides the deepest foundation of authentic human self-expression.", ["c1-nyelvfilozofia-vocab"]),
        fb("vocabulary", "recall", "A kognitív nyelvészet szerint a fizikai térbeli viszonyokból építjük fel a legbonyolultabb _____ fogalmakat is. (abstract)", "elvont", "According to cognitive linguistics, from physical spatial relations we construct even the most complex abstract concepts.", ["c1-nyelvfilozofia-vocab"]),
        fb("grammar", "recall", "A magyar nyelvben az események határát és eredményességét leggyakrabban az _____ kódolják. (verbal prefixes / preverbs)", "igekötők", "In the Hungarian language, the boundary and completeness of events are most frequently encoded by verbal prefixes.", ["c1-linguistic-relativity"]),
        fb("grammar", "context", "Amikor egy megoldhatatlan helyzetbe kerülünk, a tartálymetafora alapján azt mondjuk, hogy _____ jutottunk. (to a dead end)", "zsákutcába", "When we get into an intractable situation, based on the container metaphor we say we have reached a dead end.", ["c1-cognitive-metaphor"]),
        fb("grammar", "context", "A modern technológiai korszakban a nemzeti nyelv védelme a digitális _____ fenntartásának kérdése. (sustainability)", "fenntarthatóság", "In the modern technological era, the protection of the national language is a question of maintaining digital sustainability.", ["c1-nyelvfilozofia-vocab"]),
        mc("grammar", "context", "Hogyan kapcsolódik össze a magyar esetrendszer és az absztrakt gondolkodás?", [
            "A hármas téri tagolás (hol, hová, honnan) szolgál metaforikus alapul az emberi viszonyok és lelki állapotok leírására.",
            "Nincs közöttük semmilyen kapcsolat, mert az esetek csak véletlenszerű toldalékok.",
            "A magyar esetek kizárólag földrajzi térképek leírására alkalmasak.",
        ], 0, ["c1-cognitive-metaphor"]),
        sb("grammar", "produce", ["A", "nyelv", "nem", "pusztán", "eszköz,", "hanem", "a", "gondolat", "élő", "otthona."], ["A", "nyelv", "nem", "pusztán", "eszköz,", "hanem", "a", "gondolat", "élő", "otthona."], "Language is not merely a tool, but the living home of thought.", ["c1-linguistic-relativity"]),
        sw("production", [{"prompt": "Write a summary sentence on why Humboldt considered language an active creative force (energeia).", "answer": "Humboldt szerint a nyelv nem befejezett alkotás, hanem az emberi szellem szüntelenül megújuló teremtő ereje."}], ["c1-linguistic-relativity"]),
        sw("production", [{"prompt": "Formulate a concluding thought on the importance of mother tongue in intellectual freedom.", "answer": "Az anyanyelv a gondolkodás legbensőségesebb tere, amely nélkül nem létezhet igazi szellemi függetlenség."}], ["c1-linguistic-relativity"]),
    ]

    c_ex_list = []
    for idx, ex in enumerate(cons_exercises, start=1):
        ex_copy = dict(ex)
        ex_copy["id"] = f"{cons_stem}.ex{idx:02d}"
        c_ex_list.append(ex_copy)

    write_json(f"exercises/c1/{cons_stem}-ex.json", {"lesson": cons_stem, "exercises": c_ex_list})

    cons_sections = [
        {"type": "goal", "title": "Consolidation Goals", "items": cons_goals},
        {"type": "recycle", "title": "Quick Review"},
        {"type": "exercise-group", "title": "Recognize", "ref": f"exercises/c1/{cons_stem}-ex.json", "exerciseRefs": [f"{cons_stem}.ex01", f"{cons_stem}.ex02", f"{cons_stem}.ex03"]},
        {"type": "exercise-group", "title": "Recall", "ref": f"exercises/c1/{cons_stem}-ex.json", "exerciseRefs": [f"{cons_stem}.ex04", f"{cons_stem}.ex05", f"{cons_stem}.ex06"]},
        {"type": "exercise-group", "title": "In Context", "ref": f"exercises/c1/{cons_stem}-ex.json", "exerciseRefs": [f"{cons_stem}.ex07", f"{cons_stem}.ex08", f"{cons_stem}.ex09"]},
        {"type": "exercise-group", "title": "Produce", "ref": f"exercises/c1/{cons_stem}-ex.json", "exerciseRefs": [f"{cons_stem}.ex10", f"{cons_stem}.ex11", f"{cons_stem}.ex12"]},
        {"type": "checklist", "title": "Can you do this?", "items": cons_goals},
    ]

    write_json(
        f"lessons/c1/{cons_stem}.json",
        {
            "id": f"lesson.c1.{cons_stem[3:]}",
            "unit": 1,
            "title": f"Unit 1 Consolidation: {unit_title}",
            "level": "C1",
            "sections": cons_sections,
        },
    )


if __name__ == "__main__":
    print("=== Generating Hungarian C1 Dual Track Unit 1 ===")
    update_registries()
    generate_core_unit_1()
    generate_discourse_unit_1()
    print("=== Generation Complete ===")
