# Antigravity brief: ES C1 core Unit 8 `data-demography` (trial, 2026-11-19)

The user wants to try the new Antigravity models on writing one ES C1 unit from scratch. Claude reviews it afterwards (a norm check against the RAE, a second read, fixes, play-through, freeze, planting in es-es). Same brief the Claude writers of Units 3-7 had, so the results compare.

## Antigravity: how this trial works

- Work in the main checkout `C:/dev/parlour`, on `master`, up to date first: `git pull --rebase origin master`. Touch only Unit 8's files (listed in the brief below), `content/es-latam/curriculum/challenges.json` (through `add_challenges.py`), `content/es-latam/indexes/tags.lock.json` (through `lock_tags.py`), `skills/es.json` and the generated indexes (through `set_planned_taught_in.py` / `build_skill_registry.py`), and the report file. Generated files that `build-manifest.py` rewrites (decks, manifests, curriculum.json) are left out of your commit: `git checkout -- content/*/decks content/*/stories/manifest.json content/*/curriculum/curriculum.json` before committing; the auto-sync job rebuilds them.
- Write es-latam only. Do NOT plant the unit in es-es and do NOT run `freeze_unit.py`: Claude does both after the read.
- Do NOT edit ROADMAP.md, ACHIEVED.md or the docs for this trial: Claude records the outcome. Raise anything you would change in the report instead.
- When the unit is done and every check below is clean: one commit (message: `ES C1 core Unit 8 (data-demography): written by Antigravity (trial), before the read`), `git pull --rebase origin master`, `git push origin HEAD:master`. The pre-push hook runs the validator and check-content; never bypass it.
- In the report, add at the top: the model you ran as, wall-clock time, and how much of your allowance the unit used (as precisely as you can see it). Then stop.

## Order of work

You are writing 1 new unit(s) of the Spanish C1 core of the Parlour language app, one after the other, in `C:/dev/parlour`. Commit only as the trial rules above say. The unit's full brief is below; follow it exactly.

Do the units in this order, and finish each one completely (all its checks clean, tags locked, report written) before you start the next: a later unit builds on the earlier ones (their words are known, their skills recapped, never re-taught or re-listed).

## Unit 8 `data-demography`
1. From `C:/dev/parlour`: `python scripts/set_planned_taught_in.py es c1 data-demography`, `python build-manifest.py`, `python scripts/build_word_lesson_index.py es-latam`, then `python scripts/prior_knowledge.py es-latam c1 data-demography --out .scratch/sheet-data-demography.md` (the knowledge sheet; generate it only now, so it includes the units you have just finished).
2. Read and follow the unit brief below ("The brief").
3. Write the report to `C:/dev/parlour/imports/review/es-c1-antigravity-08/report.md`.

Finish with the report file (committed with the unit), including what in this brief cost you the most and what you would cut.


---

## The brief

You are writing ONE NEW unit of the Spanish C1 core of the Parlour language app, from scratch, in the es-latam course. Work ONLY in `C:/dev/parlour` (a git worktree; absolute paths). Never change git or tool config, never bypass hooks. Commit only when the whole unit is done (see "Antigravity: how this trial works" above). Scratch files only under `C:/dev/parlour/.scratch/` (create it; it is not committed).

## Read first, in this order, and nothing else unless needed to settle a point

1. `C:/dev/parlour/docs/unit-agent-rules.md` § 1–5, § 6a and § 6c (skip § 6b, Hungarian): your rulebook.
2. `C:/dev/parlour/docs/course-generation-brief.md` § 2.2–2.4, § 3, § 4, § 5, § 6, § 7, § 9.2.
3. The knowledge sheet `C:/dev/parlour/.scratch/sheet-data-demography.md`: what the learner has met (A1–B2 core). Anything under "Known" is recapped as known ("You know *X* from B2 Unit N"), never presented as new. Anything under "later", "Taught only on a screen of a hidden track", or in the list "C1 forms not met yet" below has NOT been met: never in a screen example, an item, an option, a challenge or the text.
4. The unit's plan: `C:/dev/parlour/imports/review/es-c1-plan/level-plan.md` (your unit's row, and the pilot detail if your unit is 1 or 2) and the unit notes below.
Saving tokens (learned on Units 3–4): the knowledge sheet is long, so grep its "Known words" section for each word you plan to list instead of reading it whole; print a recapped screen with `python scripts/show_screen.py es-latam <screen id>` instead of opening its JSON; and you may generate the unit's files from short Python data with `scripts/es_c1_builders.py` (its builders carry the field shapes of the finished C1 units; see its docstring) instead of copying field names from the model files.

5. As JSON-shape models (copy field names exactly; never invent fields): lesson `C:/dev/parlour/content/es-latam/lessons/b2/b2-20-03.json` with its screen `grammar/b2/b2-20-03-a-gr.json`, vocabulary `vocabulary/b2/b2-20-03-voc.json` and exercises `exercises/b2/b2-20-03-ex.json`; lesson `b2-36-05` for the story section; `b2-36-consolidation` for a consolidation; a story file `stories/original/a2/a2-07.json` for the story shape (paragraphs, `narration.pedagogical.comprehensionQuestions`). Schemas: `C:/dev/parlour/content/es-latam/schemas/`.

## The unit (already in `content/es-latam/curriculum/units/c1.json` and `skills/es.json`)

- Unit 8, id `data-demography`, title "Demography & the Language of Data", vocabulary skill `c1-data-demography-vocab`, track `core`.
- Stems `c1-08-01` … `c1-08-05` and `c1-08-consolidation`. Files under `C:/dev/parlour/content/es-latam/`: `lessons/c1/<stem>.json` (lesson id `lesson.c1.08.0k`, consolidation `lesson.c1.08.consolidation`, `"level": "C1"`); screens `grammar/c1/<stem>-a-gr.json` (and `-b-gr.json` for a second concept); `vocabulary/c1/<stem>-voc.json`; `exercises/c1/<stem>-ex.json` (exercise ids `<stem>.ex01` …); the unit text `stories/original/c1/c1-08.json`, referenced only from lesson `c1-08-05`.
- Before you start, run `python scripts/set_planned_taught_in.py es c1 data-demography`: it sets `taught_in` for the skills this unit teaches (their planned screens); each of those screens must then exist with exactly that file name. Never edit `skills/*.json`, `tags.lock.json` or generated files by hand.

## The learner and the course

- The learner knows English and has finished A1–B2 core. C1 is register, precision and density, not exotic grammar: every lesson is about using Spanish well in the unit's domain.
- Screens, lesson titles, goals, checklists and every question stem are in English (as in ES B2): short, explicit, natural; say why a structure works; Spanish forms in running English text in italics (`*…*`), one italic run per term. No Spanish grammar metalanguage the learner has not met.
- Standard Latin American Spanish usable in both courses: *ustedes*, never *vosotros*/*os* (not even as a wrong option); avoid region-marked words (es-latam *carro, computadora, celular, jugo* vs es-es *coche, ordenador, móvil, zumo*) unless the lesson needs one; a later script plants the unit in es-es and swaps those words. Varieties appear only as recognition on a screen.

## Shape (the ES B2 size, decided by the user 2026-11-18)

- Teaching lesson sections, in order: `goal` (2–4 items), `recycle` ("Quick Review"), `grammar` (one per screen), `vocabulary`, exercise groups **Introduce** 1, **Controlled** 2, **Practice** 2, **Dialogue** 1 (`dialogue-complete`), **Production** 1 (`sentence-builder` or `structured-writing`), then `srs`, **Check** 1, `checklist` (the goal items as "I can …", same count and order, each line this lesson's own). Lesson 05 adds the `story` section and a **Reading** group of 3 after Practice. 8 exercises a lesson (11 on lesson 05). At least 5 exercise types a lesson; one of the Practice items is `listening-choice` or `dictation`.
- Consolidation: `goal`, `recycle`, groups **Recognize** 3, **Recall** 3, **In Context** 3, **Produce** 3 (12 items, easy to hard, every lesson covered, at least 5 types, at least 6 different `teaches` tags), `checklist`. Nothing new taught; goal and checklist name what this unit can do.
- Norm claims on a screen (what the RAE accepts or rejects) are stated only as strongly as the source does ("preferred", "usual", "rejected").
- Every normative claim (what the norm accepts, prefers or rejects) is listed in your report under "Norm claims", worded exactly as on the screen; the reviewer checks each against the RAE before the unit is read.
- Screens: brief § 3 (text, table for any paradigm, 3–5 examples, a tip with the mistake English speakers make; at most 300 words of text + tip). A lesson recapping a known skill opens its screen with "You know *X* from B2 Unit N" and adds what is new at C1 (register, density, the domain's typical uses); it never re-teaches it as new.
- Vocabulary: 6–9 new words or chunks a lesson (C1 domain words, collocations, fixed expressions), British English glosses, the same `theme` label in all five files; a word on the knowledge sheet is used, never re-listed; every listed word used in that lesson's items.
- The unit text (lesson 05): an ORIGINAL text, genre "data report", 400–600 Spanish words, in the unit's domain and register, using the unit's words and grammar naturally; no splice of sentences, no textbook copy, no quotation of a real person, no retelling of any real work. Facts only when certain, and list every factual claim in your report. No asterisks in the story file. Never about itself, the course or its reader (`story-meta` must be 0). 3 comprehension questions in English, each needing a specific detail of the text. Title plain.

## Items (rulebook § 2, § 3, § 6)

At least 3 options in every choice item (2 options is a coin toss). One right answer; every wrong option a real Spanish string with exactly one fault and never a possible right answer; no length give-aways or tells (absolute words, time words only one option has); `teaches` exactly one slug by what a wrong answer shows (a tested form → its grammar skill, a tested word → `c1-data-demography-vocab`); `distractor_skills` on a wrong option that is a real form of another known skill; fill-blanks blank a whole word, carry `english` and a `hint` field (never a parenthesis in `sentence`); `answers` only for true alternatives; multiple-choice items take neither `hint` nor `english`; no English inside a Spanish line; reading items answerable from the text as written. Tags only from `skills/es.json`: the unit's own C1 skills, known A1–B2 skills, or the unit vocabulary skill.

Learned on the pilot (Units 1–2), each a defect a reader had to fix:
- **Pin every production prompt.** A `structured-writing` or `sentence-builder` prompt names what its stored answer needs: the construction ("using «se»", "with «pedir que»"), the person, and the gender where it shows ("as a woman"). If two forms would fit the prompt, the prompt is not pinned.
- **Anchor the context so no wrong option is right in another reading.** Time (a finished past frame, *el martes pasado*, when an item tests the imperfect subjunctive after a past verb), person and register are fixed by the prompt, not left to the learner.
- **A wrong option that is acceptable Spanish is a second right answer**, even if a style guide prefers the other: test only real errors, or ask honestly "Which form is preferred in formal writing?".
- **People:** Carlos works in an office and is not a student (no essays, classes or exams of his: those are Meg's); Meg is a student. No one talks about themselves in the third person.
- **A recap names the right unit:** take the unit number from the knowledge sheet, never from memory.
- The unmet-word checker misses verb forms with attached pronouns (*leyéndolo*, *corrígelo*): avoid them in challenge targets, or confirm the verb is met.

## Challenges

One challenge per lesson, consolidation included (six), written to `C:/dev/parlour/.scratch/challenges-data-demography.json` as a JSON object keyed by lesson stem, then added with `python scripts/add_challenges.py es-latam c1 .scratch/challenges-data-demography.json` (fix and rerun until it accepts all six), each entry with exactly the fields of `b2-36-01` in `C:/dev/parlour/content/es-latam/curriculum/challenges.json` (`level` "C1"). Scenario starts with the role ("You are Meg." / "You are Carlos."); Carlos is Hungarian and works in an office, Meg is South African and a student, they live in Budapest; invent no other facts about them; other people stay unnamed; cues say what to include, never the words; target 1–3 sentences of met words using the lesson's grammar; `canDo` = the lesson's first checklist line.

## C1 forms not met yet (never use them in this unit unless this unit teaches them)

- `como-condicional-subjuntivo`: conditions and warnings with como and the subjunctive (taught at c1-19-01-a-gr, Unit 19)
- `con-lo-que-para-lo-que`: evaluative con lo que and para lo que (taught at c1-20-03-a-gr, Unit 20)
- `dislocacion-clitica`: fronted objects picked up by a clitic pronoun (taught at c1-11-01-a-gr, Unit 11)
- `futuro-concesivo`: the concessive future and conditional like será caro, pero (taught at c1-20-01-a-gr, Unit 20)
- `leismo-laismo-reconocimiento`: recognising leísmo and laísmo (taught at c1-25-01-a-gr, Unit 25)
- `marcadores-conversacionales`: spoken discourse markers like pues, vamos and hombre (taught at c1-18-01-a-gr, Unit 18)
- `ni-que-exclamativo`: ironic exclamations with ni que and the imperfect subjunctive (taught at c1-21-01-a-gr, Unit 21)
- `se-aspectual`: aspectual se with verbs like comerse and leerse (taught at c1-17-01-a-gr, Unit 17)
- `sufijos-apreciativos`: evaluative suffixes for tone and attitude (taught at c1-22-01-a-gr, Unit 22)
- `verbos-doble-modo`: verbs whose meaning changes with the indicative or subjunctive (taught at c1-12-01-a-gr, Unit 12)

## Unit notes

Lesson plan (keep the topic and order; adjust details if a better order emerges):
- 01 NEW `concordancia-ad-sensum`, screen `c1-08-01-a-gr`: agreement with quantity and group subjects. What the RAE accepts (reviewer, from rae.es glossary and DPD excerpts, 2026-11-19): after a partitive with a plural complement (*la mayoría de los encuestados*, *la mitad de los alumnos*, *el resto de los vecinos*, *el 40 % de los hogares*) the verb may be singular or plural: *La mitad de los alumnos aprobó / aprobaron*; the plural puts the people in front, the singular the quantity. A collective noun on its own (*la gente*, *el público*, *la población*, *el equipo*) takes a singular verb: *La gente opina*, never *la gente opinan*. After a partitive the noun needs its article: *la mitad de los lápices*, not *la mitad de lápices*. Teach exactly this; say plainly that both forms are correct after a partitive. ITEMS: never mark singular or plural wrong after a partitive; test the real errors only (plural after a bare collective noun; a partitive without its article), or ask which nuance a form gives ("Which version puts the people in front?"). At least 6 items tagged with it.
- 02 describing trends with time phrases: recap `durative-progressive-periphrases`-type skills only if the sheet lists them; otherwise recap `gerund-periphrases` (B2: *ir* + gerund, *la población va envejeciendo*) and `perifrasis-llegar-a-infinitivo` (B2: *llegó a superar*).
- 03 NEW `comparativas-de-lo-que`, screen `c1-08-03-a-gr`: comparing a quantity with what was expected or said. *más / menos de lo que* + a clause (*La población creció más de lo que se esperaba*); with a noun the relative agrees with it: *más dinero del que*, *más personas de las que*, *menos hogares de los que* (*más personas del que…* is the error); *que* when two things are compared (*más que el año pasado*, *más que Ana*, never *más de Ana*); *de* before a number (*más de cien*). Leave out *no más que* (it means "only" and would confuse). At least 6 items tagged with it. Note: frozen B1 texts already use *más de lo que* once or twice in passing, so the screen may say "You may have seen *más de lo que* in passing" but it teaches it here.
- 04 percentages, fractions and approximations in formal reports: recap `numbers`-family skills the sheet lists (B1/B2), vocabulary-led (*el porcentaje, la tasa, aproximadamente, rondar, en torno a, la mitad, un tercio*); tag items with the unit vocabulary skill or the known skill a wrong answer shows.
- 05 interpreting data with caution: recap `hedging` (B2) and `perifrasis-modales-probabilidad-epistemica` (B2): *los datos parecen indicar*, *podría deberse a*; correlation is not cause; plus the text and the Reading group.
Domain words: population and statistics (e.g. *la encuesta, el encuestado, la natalidad, el envejecimiento, la tasa, el porcentaje, el censo, la muestra* only if no earlier unit lists it, *la tendencia, rondar*); check each against the sheet first: a word an earlier C1 unit lists is used, never re-listed.
Text: a data report of an invented regional statistics office on a population that is getting older (birth rate falling, more people over 65, young people moving to cities), with approximate invented figures clearly about an unnamed region ("una región del interior"); it uses partitive agreement and *de lo que / del que* naturally, and ends with a cautious interpretation (what the data do and do not show). No real country, census, institute or statistic.

## Checks (from `C:/dev/parlour`, in this order; fix and rerun until clean)

- `python build-manifest.py`, then `python scripts/build_word_lesson_index.py es-latam` (rerun both after changing a vocabulary list).
- `python scripts/check-content.py es-latam c1 data-demography`: fix every error (it also fails a choice item with fewer than 3 options, `few-options`, and a word an earlier C1 lesson already lists, `vocab-relisted`: use that word, don't list it again); fix or give a one-line reason for each suspect.
- `node scripts/unmet-words.js es-latam c1 --stems c1-08-01,c1-08-02,c1-08-03,c1-08-04,c1-08-05,c1-08-consolidation --with-hidden` (C1 core is hidden while it is written; `--with-hidden` counts this unit's and earlier C1 units' own lists, not the latam track). Transparent English cognates are skipped already; every other hit is listed in the first lesson that uses it or replaced by a met word.
- `python scripts/check_es_c1_forms.py es-latam c1 --track core`: no hit in your unit.
- `node scripts/render_lesson.js es-latam c1-08-01 c1-08-02 c1-08-03 c1-08-04 c1-08-05 c1-08-consolidation` and read every screen and item as rendered (`!!` = error).
- `python scripts/check_unit_refs.py es-latam c1 data-demography --bare --named` (read every hit: a recap of a form rather than a word can be a false positive).
- `python scripts/validate-content.py --changed`.
- `python scripts/lock_tags.py es-latam c1/data-demography --update --reason "new unit, written 2026-11 (ES C1 core)"`.

## Report

As your final reply (write it to `C:/dev/parlour/imports/review/es-c1-antigravity-08/report.md` and commit it with the unit): files created; per lesson the screen(s), word list and item types; the text's genre, word count and every factual claim with how sure you are; "Norm claims" (see Shape); check results (counts); every Spanish line you are unsure of, marked (unsure); and "For the user": anything you could not fix, any place the plan did not fit. Don't pad.
