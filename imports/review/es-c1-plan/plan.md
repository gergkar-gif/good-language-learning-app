# ES C1 core (es-both): plan, 2026-11-18

Status: **draft for the user's decisions.** Nothing generated yet.

## Starting point (counted 2026-11-18)

- No Spanish C1 exists: no `curriculum/units/c1.json` in es-es or es-latam,
  and `skills/es.json` has no C1 skill (429 skills: A1 66, A2 76, B1 156,
  B2 131).
- ES B2 core: 36 units, frozen in both courses, byte-identical apart from
  one file (215 of 216 lessons). The user's rule since 2026-11-14: core is
  the same in both courses apart from regional varieties; culture tracks
  tell them apart.
- ES B2 already took most of what textbooks file under C1: stylistic
  *-ra*, free indirect discourse, reduplicated subjunctive, absolute
  participles, conditional inversions, cleft sentences, nominalisation,
  hedging, formal register, essay style, rhetorical devices, voseo
  recognition (59 B2 grammar skills). The C1 skill list must not
  duplicate them.
- The engine already knows C1 (`LEVEL_ORDER`, `init.js` LEVELS, decks,
  journey). `guide.js` says "Spanish A1–B2" and needs changing at ship.
- The generation brief's shape table stops at B1. ES B2 lessons have 6–9
  exercises and an 8-item consolidation; HU C1 core has 8–16 and 12.

## Proposal

### Scope

36 core units, `track: "core"`, one file set written once and planted
byte-identical in es-latam and es-es (as B2 core). Pan-Hispanic standard
Spanish: *ustedes*, no *vosotros* forms in answers, no region-marked
words without a gloss. Varieties (leísmo, voseo, *vosotros*) appear as
recognition on screens, never as the only correct answer.

### Unit design

Each unit = a domain topic + one language focus. About 20 units teach a
new C1 skill; the rest push B2 skills to C1 density in a new domain and
tag the unit vocabulary or the existing skill (the HU C1 model: 15 grammar
skills over 36 core units).

Candidate new skills (keyword-checked against `skills/es.json`; each still
to be checked against the B2 screens before the list goes to the user):

| Candidate | Unit topic |
|---|---|
| future subjunctive, recognition (*el que infringiere*) | law and legal texts |
| journalistic conditional of rumour (*habría dimitido*) | press and news |
| headline and nominal style (verbless, infinitive headlines) | press and news |
| *dequeísmo* and *queísmo* (normative *de que*) | language norm |
| verbs whose mood changes meaning (*sentir/decir/comprender que*) | interpretation, perception |
| formal relatives with *el cual*, *lo cual*, preposition + *el cual* | institutions, administration |
| agreement *ad sensum* (*la mayoría de … votaron*) | demography, statistics |
| clitic left dislocation (*El informe lo firmó ayer*) | debate, information structure |
| aspectual *se* (*comerse*, *leerse*, *saberse*) | everyday speech, register |
| intensive *lo + adj + que*, *con lo que* (concessive-causal) | emphasis and complaint |
| *ni que* + imperfect subjunctive, exclamative irony | irony, humour |
| evaluative suffixes in pragmatics (diminutive, augmentative, pejorative) | tone, attitude |
| nominal derivation and parasynthesis (*-miento*, *en-…-ecer*) | science, technology |
| support verbs and collocations (*tomar medidas*, *poner en marcha*) | economy, business |
| verbal idioms (*echar en cara*, *dar largas*) | relationships, conflict |
| spoken discourse markers (*pues*, *vamos*, *hombre*, *venga*) | conversation, interviews |
| mitigation and politeness strategies beyond B2 hedging | negotiation, mediation |
| compound and nominal infinitive (*el haber firmado*) | academic writing |
| normative gerund (no gerund of posteriority or adjectival gerund) | academic writing |
| leísmo and laísmo, recognition | language variation |

Remaining ~16 units: domain units (health and bioethics, environment,
AI and digital ethics, urbanism, education, history and memory, migration
and identity, art and literary criticism, philosophy, work, science
policy, human rights, …) with a closing synthesis unit.

### Lesson shape (decision needed)

Recommended: the ES B2 shape, so B2 and C1 feel the same: 5 teaching
lessons of ~8 exercises (Introduce 1, Controlled 2, Practice 2, Dialogue 1,
Production 1, Check 1; Reading 3 on lesson 05) and a 12-item consolidation.
About 52 exercises a unit, ~1,900 for the level.

### Unit texts (decision needed)

Recommended: one original C1 text per unit on lesson 05, 400–600 words,
in a genre that fits the topic (opinion column, essay, interview, report,
review, a legal text written for the course). No adaptations of
in-copyright works; any text about a real work is labelled "About".
Facts flagged by the writer and checked on the web by the reviewer.

### Process

1. **Level plan [stop].** Check each candidate skill against the B2
   screens; write the 36-unit table (ids, titles, lesson-by-lesson
   grammar and topic), the skill entries (`family`, `title`, `taught_in`,
   `requires`) and the frozen list. The user signs off the skill list;
   it is frozen after this.
2. **Tooling, same session.** A Spanish "New unit" writer template for C1
   (`scripts/templates/new-spanish-c1.txt`, from the HU A2 template and
   the ES B2 edit template); an ES equivalent of `check_c1_forms.py` so
   B2 and below never use a C1 form; a plant script check that es-es and
   es-latam C1 files stay identical.
3. **Pilot [stop]:** Units 1–2, one Sonnet writer each (two agents at
   most), one reader, review, walk, freeze in both courses. Report cost
   and defects before continuing.
4. **Batches of 4 units**: two writers × 2 units, one reader, review,
   apply, lock, walk, freeze per course, commit per unit.
5. **Level checklist** (pipeline doc § "Before calling a level done"),
   C1 challenges in `challenges.json`, a C1 level test, unhide, update
   `guide.js`, ROADMAP/ACHIEVED.

C1 stays hidden until step 5.

### Cost estimate (uncertain)

New HU A2 units cost ~361k tokens each (writer + reader) at 18 exercises
a lesson. A half-size C1 unit with a longer text: guess 250–350k, so
roughly 9–13M tokens for the level, plus review. The pilot measures it.

## Open for the user

1. Start now, or finish the ES B2 latam track first (release-gate order)?
2. Lesson shape: ES B2 size (recommended) or the brief's full size?
3. Identical files in both courses (recommended)?
4. About 20 new C1 skills, the rest domain units (recommended)?
5. Unit texts: original genre texts (recommended) or texts about Hispanic
   works as in B2?
