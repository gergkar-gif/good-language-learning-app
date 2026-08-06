# Spanish Mastery — Curriculum Map

Status: draft, v1. Compiled 2026-08-06.

Sources: the 16 curriculum docs (`00-Philosophy` through `15-roadmap`) and the resources currently in `imports/` (653 verb conjugation files, a 132-word dictionary extracted from one story).

Purpose: give a single structural + content view of the curriculum that can drive lesson generation. Where the source docs are explicit, this map reproduces them. Where the docs are placeholders (they say so themselves — several are marked "Future Output"), this map proposes a first draft and flags it as inferred, not sourced. Treat the "Proposed" columns as a starting hypothesis to review, not settled curriculum.

---

## 1. What the docs actually define vs. what's still a placeholder

Worth being clear-eyed about this before using the docs as a generation spec:

| Doc | Status |
|---|---|
| 00 Philosophy, 01 CEFR Framework, 02 Global Progression | Fully defined — vision, level questions, content philosophy. |
| 03 Module Framework | Fully defined — module/lesson structure and counts. |
| 15 Roadmap | Fully defined — module titles and lesson totals per level. |
| 08–11 Reading/Listening/Writing/Speaking Progressions | Fully defined — genre and task types per level. |
| 12 Assessment Framework, 13 Content Standards, 14 Quality Checklist | Fully defined — process and QA rules. |
| 04 Curriculum Dependencies | Defines the *model* (Requires/Introduces/Reinforces/Unlocks) but contains zero actual dependency instances. IDs are described as "Future Implementation." |
| 05 Grammar Graph | Defines categories only (Verbs, Nouns, Adjectives...). Zero actual grammar nodes exist. Explicitly "Future Output." |
| 06 Vocabulary Graph | Defines domains only (People, Everyday Life, Society...). Zero actual vocabulary entries exist. Explicitly "Future Output." |
| 07 Skills Graph | Defines progression stages only (e.g. reading: words → sentences → ... → academic texts). Zero IDs, no per-level assignment. Explicitly "Future Output." |

In short: the *scaffolding* is complete, but the three graphs that would actually drive content generation (grammar, vocabulary, skills, with IDs and dependencies) are empty templates. Sections 3–4 below propose a first pass at filling them, grounded in standard CEFR Spanish sequencing, since nothing in the docs specifies an order.

---

## 2. Level structure (from docs 00, 01, 02, 03, 15 — directly sourced)

| Level | Central Question | Communicative Focus | Primary Reading | Modules | Lessons |
|---|---|---|---|---|---|
| A1 — Fundamentals | How do I survive? | Predictable everyday interactions | Original story | 4 × 5 | 20 |
| A2 — Everyday Life | How do I live? | Independence in daily life | Original story + adapted readers | 4 × 5 | 20 |
| B1 — Society | How does society work? | Confident discussion of real-world topics | Authentic texts | 5 × 6 | 30 |
| B2 — The Hispanic World | Why is the Hispanic world the way it is? | In-depth regional discussion | Regional studies | 6 × 6 | 36 |
| C1 — Ideas & Culture | How do people think? | Sophisticated argument and analysis | Intellectual texts | 6 × 6 | 36 |
| Academy (C2+) | How do experts communicate? | Specialist expertise | Professional/academic sources | Independent, variable length | Open-ended |

Core curriculum total: 142 lessons (A1–C1). Academy is a separate open-ended track (Literature, Philosophy, History, Politics, Economics, Science, Law, Business, Regional Dialects, Translation, Academic Writing, DELE Prep).

---

## 3. Module map with proposed grammar and vocabulary assignment

Module titles and lesson counts are from `15-roadmap.txt`. Grammar sequence and vocabulary-domain assignment are **proposed** — the docs do not specify these; this follows conventional CEFR-Spanish grammar ordering and maps module titles onto the six domains defined in `06-vocabulary-graph.txt`.

### A1 — Fundamentals (4 modules, 20 lessons)

| Module | Proposed Grammar | Vocabulary Domain (from graph) |
|---|---|---|
| 1. Meeting People | Subject pronouns; ser/estar (present); gender & number agreement; articles; question words | People → Identity, Family |
| 2. Everyday Life | Regular -ar/-er/-ir present; tener; reflexive verbs (routines); possessives | Everyday Life → Home, Food |
| 3. Around Town | hay; prepositions of place; ir + a + infinitive; numbers; gustar-type verbs | Everyday Life → Shopping, Travel (local) |
| 4. Looking Ahead | Near future (ir a + inf.); basic connectors (y, pero, porque) | People → Relationships; time/future vocabulary |

### A2 — Everyday Life (4 modules, 20 lessons)

| Module | Proposed Grammar | Vocabulary Domain |
|---|---|---|
| 1. Living Independently | Stem-changing present (e>ie, o>ue); comparatives/superlatives; direct/indirect object pronouns | Everyday Life → Home, Health |
| 2. Experiences | Preterite (regular + ser/ir/hacer/tener); time markers | People → Relationships; leisure vocabulary |
| 3. Services & Travel | Imperfect; preterite vs. imperfect contrast | Everyday Life → Travel, Health, Shopping |
| 4. Plans & Relationships | Future tense (regular + irregular); conditional (intro); relative clauses (que) | People → Relationships, Professions |

### B1 — Society (5 modules, 30 lessons)

| Module | Proposed Grammar | Vocabulary Domain |
|---|---|---|
| 1. Community | Present perfect; past participles; indefinite/negative pronouns | Society → Government, Environment |
| 2. Media & Technology | Pluperfect; se-passive/impersonal | Society → Media, Technology |
| 3. Education & Work | Present subjunctive (wishes, doubt); formal commands | Society → Education; People → Professions |
| 4. Environment & Travel | Subjunctive with impersonal expressions; adverbial clauses (cuando + subj.); por/para | Society → Environment; Everyday Life → Travel |
| 5. Contemporary Society | Imperfect subjunctive (intro); si-clauses (possible); reported speech (intro) | Society (integrative review) |

### B2 — The Hispanic World (6 modules, 36 lessons)

| Module | Proposed Grammar | Vocabulary Domain |
|---|---|---|
| 1. Spain | Subjunctive review; concession/purpose clauses (aunque, para que) | History & Politics → Geography, History; Culture → Art |
| 2. Mexico | Conditional perfect; compound subjunctive tenses | History & Politics → History; Culture → Music, Film |
| 3. Central America & Caribbean | Hypothetical si-clauses (imperfect subj. + conditional) | History & Politics → Geography; Culture |
| 4. The Andes | Passive/impersonal se (review); discourse connectors | History & Politics → History, Geography |
| 5. The Southern Cone | Complex relative clauses (cuyo, el cual); register | Culture → Literature, Art |
| 6. Contemporary Latin America | Stylistic/regional variation | History & Politics → Politics, International Relations |

### C1 — Ideas & Culture (6 modules, 36 lessons)

| Module | Proposed Grammar | Vocabulary Domain |
|---|---|---|
| 1. History | Narrative past mastery; historical present; complex reported speech | History & Politics → History |
| 2. Politics | Subjunctive nuance (doubt/emotion/value judgment); rhetorical structures | History & Politics → Politics |
| 3. Literature | Literary/narrative tenses; free indirect style | Culture → Literature |
| 4. Philosophy | Nominalized clauses; precise connectors; abstract argumentation | Ideas → Philosophy, Ethics |
| 5. Society & Economics | Formal/academic register; hedging language | Ideas → Psychology; History & Politics → Economics |
| 6. Culture & Identity | Full stylistic control; cohesion devices | Culture (integrative review) |

### Academy (C2+)

Per `03-module-framework.txt`, Academy modules are independent and variable in length; grammar is "maintained through authentic use" rather than sequenced. No new grammar map proposed — content should be organised by domain (Literature, Law, Business, Science, etc.) as listed in doc 00/01/15.

---

## 4. Skills progression pointer (from doc 07, directly sourced)

Each level maps onto a stage of the four skill progressions. This is a direct restatement of doc 07 aligned to level, for quick lesson-generation reference:

| Level | Reading stage | Listening stage | Writing stage | Speaking stage |
|---|---|---|---|---|
| A1 | Words → dialogues | Words → phrases | Words → short guided paragraphs | Repetition → guided dialogue |
| A2 | Stories | Conversations → announcements | Sentences → short narratives | Guided dialogue → conversation |
| B1 | Authentic texts | Interviews → podcasts | Paragraphs → narratives/summaries | Conversation → discussion |
| B2 | Long-form texts | Podcasts → lectures | Reports → essays | Discussion → presentation/debate |
| C1 | Literature, academic texts | Lectures → debates | Essays → academic writing | Presentation → debate/professional |
| Academy | Academic/specialist texts | Specialist podcasts, lectures | Academic/specialist writing | Professional communication |

---

## 5. Existing content resources mapped onto the structure

### 5.1 Verb conjugation data (`imports/verbs/`, 653 files)

Each file gives a full paradigm (indicativo: presente, futuro, imperfecto, pretérito, condicional, and their perfect/compound forms; subjuntivo: presente, imperfecto, futuro, and compounds; imperativo afirmativo/negativo), plus an English gloss per form and a `regular: true/false` flag. Source is Fred Jehle's public-domain Spanish verb data, pulled from `github.com/miko3k/verbos`.

Coverage against the grammar map in Section 3: the tense forms needed for every level from A1 (present) through C1 (subjunctive nuance, compound tenses) already exist in the data. This is usable now for conjugation tables and drills.

What's missing before it can drive generation directly:
- No CEFR or frequency tagging. All 653 verbs are undifferentiated — nothing marks which verbs belong at A1 vs. C1. A frequency list (not present in the repo) is needed to decide which ~15–20 verbs per module get introduced at which level.
- No example sentences in context — only isolated conjugated forms and one-line glosses. Readings/exercises will need to be written separately.
- Licence attribution ("Fred Jehle") is present in each file; worth confirming reuse terms before shipping if not already checked.

### 5.2 Dictionary (`imports/dictionary/spanish-en.json`)

132 entries, each `{en, type, source}`. All 132 have `"type": "unknown"` and `"source": "inline"` — every entry appears to have been extracted from a single story ("Los tres cerditos" / The Three Little Pigs), not compiled as a general dictionary despite the filename.

This is far short of what `06-vocabulary-graph.txt` calls for (domain, subdomain, CEFR level, requires/related-words per entry). Read literally, it looks like a first-pass vocabulary extraction from the planned A1 original story, not the core lexicon for the curriculum. Before this can seed the vocabulary graph it needs: POS tagging (all "unknown" currently), domain/subdomain assignment against the six domains in doc 06, and CEFR-level tagging — plus roughly two orders of magnitude more entries to cover a 142-lesson curriculum.

### 5.3 What has no source yet

- Grammar graph nodes/IDs (doc 05 categories exist, no instances).
- Vocabulary graph nodes/IDs beyond the 132-word story extract.
- Skills graph IDs and per-lesson assignment (doc 07 stages exist, not instantiated).
- Dependency graph instances (Requires/Introduces/Reinforces/Unlocks) — the model exists in doc 04, nothing populated.
- Actual lesson content: 0 of 142 core lessons written.
- App engine/UI: `README.md` references `STRUCTURE.md` and `index.html`; neither exists in the folder yet. The project is currently at the raw-resource stage, not the content or engine stage.

---

## 6. Gaps to close before content generation is realistic

1. Assign each of the 653 verbs to an introduction level (needs a frequency list — none in repo).
2. Build an actual core vocabulary list per level/module (the 132-word dictionary covers a fraction of one A1 reading).
3. Turn Section 3's proposed grammar/vocab sequence into reviewed, ID-based graph entries (e.g. `grammar.present.ser`, `vocab.family.hermano`) per the ID scheme sketched in doc 04.
4. Decide whether the module-level grammar/vocabulary proposal above is accepted, adjusted, or replaced — it is this document's inference, not sourced from the curriculum docs.
5. Write the first lesson end-to-end against `13-content-standards.txt` and `14-quality-checklist.txt` to validate the template before generating at scale.

---

## Appendix: source files consulted

Curriculum docs: `00 - Philosophy.txt`, `01-cefr-framework.txt`, `02-global-progression.txt`, `03-module-framework.txt`, `04-curriculum-dependencies.txt`, `05-grammar-graph.txt`, `06-vocabulary-graph.txt`, `07-skills-graph.txt`, `08-reading-progression.txt`, `09-listening-progression.txt`, `10-writing-progression.txt`, `11-speaking-progression.txt`, `12-assessment-framework.txt`, `13-content-standards.txt`, `14-quality-checklist.txt`, `15-roadmap.txt`.

App resources: `README.md`, `download_verbs.py`, `make_verb_list.py`, `scripts/build_verb_list.py`, `imports/verbs/*.json` (653 files), `imports/dictionary/spanish-en.json`.
