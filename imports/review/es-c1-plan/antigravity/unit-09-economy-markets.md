# Antigravity brief: ES C1 core Unit 9 `economy-markets` (2026-11-19)

Antigravity writes this ES C1 unit from scratch (user, 2026-11-19: Antigravity writes the C1 units from Unit 9 on). Claude reviews it afterwards: a norm check against the RAE, a second read, fixes, play-through, freeze, planting in es-es.

## Antigravity: how this works

- Work in the main checkout `C:/dev/parlour`, on `master`, up to date first: `git pull --rebase --autostash origin master`. Touch only Unit 9's files (listed in the brief below), `content/es-latam/curriculum/challenges.json` (through `add_challenges.py`), `content/es-latam/indexes/tags.lock.json` (through `lock_tags.py`), `skills/es.json` and the generated indexes (through `set_planned_taught_in.py` / `build_skill_registry.py`), and the report file.
- Rebuild only es-latam: `python build-manifest.py es-latam` (seconds; the full build took minutes on Unit 8). Generated files it rewrites (decks, manifests, curriculum.json) stay out of your commit: `git checkout -- content/*/decks content/*/stories/manifest.json content/*/curriculum/curriculum.json` before committing; the auto-sync job rebuilds them.
- Write es-latam only. Do NOT plant the unit in es-es and do NOT run `freeze_unit.py`: Claude does both after the read.
- Do NOT edit ROADMAP.md, ACHIEVED.md or the docs: Claude records the outcome. Raise anything you would change in the report instead.
- When the unit is done and every check below is clean: one commit (message: `ES C1 core Unit 9 (economy-markets): written by Antigravity, before the read`), `git pull --rebase --autostash origin master`, `git push origin HEAD:master`. The pre-push hook runs the validator and check-content; never bypass it.
- In the report, add at the top: the model and setting you ran as, wall-clock time, and how much of your allowance the unit used if you can see it. Then stop.

## Order of work

1. From `C:/dev/parlour`: `python scripts/set_planned_taught_in.py es c1 economy-markets`, `python build-manifest.py es-latam`, `python scripts/build_word_lesson_index.py es-latam`, then `python scripts/prior_knowledge.py es-latam c1 economy-markets --out .scratch/sheet-economy-markets.md` (the knowledge sheet).
2. Read and follow the unit brief below ("The brief").
3. Write the report to `C:/dev/parlour/imports/review/es-c1-antigravity-09/report.md` and commit it with the unit.

---

## The brief

You are writing ONE NEW unit of the Spanish C1 core of the Parlour language app, from scratch, in the es-latam course. Work ONLY in `C:/dev/parlour` (a git worktree; absolute paths). Never change git or tool config, never bypass hooks. Commit only when the whole unit is done (see "Antigravity: how this works" above). Scratch files only under `C:/dev/parlour/.scratch/` (create it); it is not committed.

## Read first, in this order, and nothing else unless needed to settle a point

1. `C:/dev/parlour/docs/unit-agent-rules.md` § 1–5, § 6a and § 6c (skip § 6b, Hungarian): your rulebook.
2. `C:/dev/parlour/docs/course-generation-brief.md` § 2.2–2.4, § 3, § 4, § 5, § 6, § 7, § 9.2.
3. The knowledge sheet `C:/dev/parlour/.scratch/sheet-economy-markets.md`: what the learner has met (A1–B2 core). Anything under "Known" is recapped as known ("You know *X* from B2 Unit N"), never presented as new. Anything under "later", "Taught only on a screen of a hidden track", or in the list "C1 forms not met yet" below has NOT been met: never in a screen example, an item, an option, a challenge or the text.
4. The unit's plan: `C:/dev/parlour/imports/review/es-c1-plan/level-plan.md` (your unit's row, and the pilot detail if your unit is 1 or 2) and the unit notes below.
Saving tokens (learned on Units 3–4): the knowledge sheet is long, so grep its "Known words" section for each word you plan to list instead of reading it whole; print a recapped screen with `python scripts/show_screen.py es-latam <screen id>` instead of opening its JSON; and you may generate the unit's files from short Python data with `scripts/es_c1_builders.py` (its builders carry the field shapes of the finished C1 units; see its docstring) instead of copying field names from the model files.

5. As JSON-shape models (copy field names exactly; never invent fields): lesson `C:/dev/parlour/content/es-latam/lessons/b2/b2-20-03.json` with its screen `grammar/b2/b2-20-03-a-gr.json`, vocabulary `vocabulary/b2/b2-20-03-voc.json` and exercises `exercises/b2/b2-20-03-ex.json`; lesson `b2-36-05` for the story section; `b2-36-consolidation` for a consolidation; a story file `stories/original/a2/a2-07.json` for the story shape (paragraphs, `narration.pedagogical.comprehensionQuestions`). Schemas: `C:/dev/parlour/content/es-latam/schemas/`.

## The unit (already in `content/es-latam/curriculum/units/c1.json` and `skills/es.json`)

- Unit 9, id `economy-markets`, title "Economy & Markets", vocabulary skill `c1-economy-markets-vocab`, track `core`.
- Stems `c1-09-01` … `c1-09-05` and `c1-09-consolidation`. Files under `C:/dev/parlour/content/es-latam/`: `lessons/c1/<stem>.json` (lesson id `lesson.c1.09.0k`, consolidation `lesson.c1.09.consolidation`, `"level": "C1"`); screens `grammar/c1/<stem>-a-gr.json` (and `-b-gr.json` for a second concept); `vocabulary/c1/<stem>-voc.json`; `exercises/c1/<stem>-ex.json` (exercise ids `<stem>.ex01` …); the unit text `stories/original/c1/c1-09.json`, referenced only from lesson `c1-09-05`.
- Before you start, run `python scripts/set_planned_taught_in.py es c1 economy-markets`: it sets `taught_in` for the skills this unit teaches (their planned screens); each of those screens must then exist with exactly that file name. Never edit `skills/*.json`, `tags.lock.json` or generated files by hand.

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
- The unit text (lesson 05): an ORIGINAL text, genre "analysis column", 400–600 Spanish words, in the unit's domain and register, using the unit's words and grammar naturally; no splice of sentences, no textbook copy, no quotation of a real person, no retelling of any real work. Facts only when certain, and list every factual claim in your report. No asterisks in the story file. Never about itself, the course or its reader (`story-meta` must be 0). 3 comprehension questions in English, each needing a specific detail of the text. Title plain.

## Items (rulebook § 2, § 3, § 6)

At least 3 options in every choice item (2 options is a coin toss). One right answer; every wrong option a real Spanish string with exactly one fault and never a possible right answer; no length give-aways or tells (absolute words, time words only one option has); `teaches` exactly one slug by what a wrong answer shows (a tested form → its grammar skill, a tested word → `c1-economy-markets-vocab`); `distractor_skills` on a wrong option that is a real form of another known skill; fill-blanks blank a whole word, carry `english` and a `hint` field (never a parenthesis in `sentence`); `answers` only for true alternatives; multiple-choice items take neither `hint` nor `english`; no English inside a Spanish line; reading items answerable from the text as written. Tags only from `skills/es.json`: the unit's own C1 skills, known A1–B2 skills, or the unit vocabulary skill.

Learned on the pilot (Units 1–2), each a defect a reader had to fix:
- **Pin every production prompt.** A `structured-writing` or `sentence-builder` prompt names what its stored answer needs: the construction ("using «se»", "with «pedir que»"), the person, and the gender where it shows ("as a woman"). If two forms would fit the prompt, the prompt is not pinned.
- **Anchor the context so no wrong option is right in another reading.** Time (a finished past frame, *el martes pasado*, when an item tests the imperfect subjunctive after a past verb), person and register are fixed by the prompt, not left to the learner.
- **A wrong option that is acceptable Spanish is a second right answer**, even if a style guide prefers the other: test only real errors, or ask honestly "Which form is preferred in formal writing?".
- **People:** Carlos works in an office and is not a student (no essays, classes or exams of his: those are Meg's); Meg is a student. No one talks about themselves in the third person.
- **A recap names the right unit:** take the unit number from the knowledge sheet, never from memory.
Learned on Unit 8 (the read found 33 defects, these the most):
- **Natural collocations, logical claims.** Read every Spanish sentence for sense as well as grammar: a rise cannot "exceed the previous decline", a percentage is not measured *en puntos*, *alcanzar un nuevo descenso* is not said. If you would not find the phrase in a quality newspaper, rewrite it.
- **Listening wrong options** are the right sentence with ONE detail changed (a number, *más/menos*, *mayoría/minoría*, the subject), never an unrelated sentence, never with absolutes (*the whole population*, *entire*, *no further*).
- **Every goal and checklist line is practised** by at least one item of its lesson; every form a screen promises (a goal's *la mitad*, *de* before a number) is drilled.
- **A challenge's scenario, cues and target say the same thing** (no "two sentences" over a one-sentence target, no detail in the target that the scenario never gives).
- **`category` follows the tag:** an item tagged with the unit vocabulary skill has `category: vocabulary`.
- **No grammar claim from memory you cannot defend** (Unit 8 listed regular *crecer* among irregular gerunds); and a "wrong" option the dictionary accepts (*en torno de*) is a second right answer.
- The unmet-word checker misses verb forms with attached pronouns (*leyéndolo*, *corrígelo*): avoid them in challenge targets, or confirm the verb is met.

## Challenges

One challenge per lesson, consolidation included (six), written to `C:/dev/parlour/.scratch/challenges-economy-markets.json` as a JSON object keyed by lesson stem, then added with `python scripts/add_challenges.py es-latam c1 .scratch/challenges-economy-markets.json` (fix and rerun until it accepts all six), each entry with exactly the fields of `b2-36-01` in `C:/dev/parlour/content/es-latam/curriculum/challenges.json` (`level` "C1"). Scenario starts with the role ("You are Meg." / "You are Carlos."); Carlos is Hungarian and works in an office, Meg is South African and a student, they live in Budapest; invent no other facts about them; other people stay unnamed; cues say what to include, never the words; target 1–3 sentences of met words using the lesson's grammar; `canDo` = the lesson's first checklist line.

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

This unit teaches no new skill: every lesson recaps known B1/B2 skills at C1 density in economic analysis (screens open with "You know *X* from <Level> Unit N", the unit number taken from the knowledge sheet, and add what is new at C1: how an economic analysis uses the form). Items are tagged with those skills or `c1-economy-markets-vocab`.
Lesson plan:
- 01 explaining causes: recap `formal-cause-connectors` (B1): *debido a*, *a raíz de*, *dado que*, *como consecuencia de*. Do not test *en base a* in any way (the norm has changed on it).
- 02 conditions without *si*: recap `implicit-conditionals` (B2): *De seguir así, los precios subirán*, *De no bajar los tipos, …*.
- 03 what would be different now: recap `mixed-conditionals` (B2): *Si el banco hubiera subido los tipos a tiempo, hoy la inflación sería menor*.
- 04 whatever happens: recap `reduplicated-subjunctive` (B2): *pase lo que pase*, *sea cual sea la decisión*, *cueste lo que cueste*; plus support-verb collocations of the domain as vocabulary (*tomar medidas*, *poner en marcha*, *llevar a cabo*, *dar lugar a*), tagged `c1-economy-markets-vocab`.
- 05 how things ended up: recap `terminar-por-infinitivo` and `perifrasis-pasar-a` (B2): *acabó por subir los tipos*, *pasó a ser el principal exportador*; plus the text and the Reading group.
Domain words: markets, prices, policy (e.g. *la inflación, los tipos de interés, el banco central, la demanda, la oferta, el consumo, el crecimiento* only if no earlier unit lists it, *la recesión, encarecerse, abaratarse* only if Unit 3 did not list *abaratar*: check the sheet, *el poder adquisitivo*); check each against the sheet first: a word an earlier unit lists is used, never re-listed (`vocab-relisted` fails it). Latin America says *las tasas de interés* as often as *los tipos de interés*: use *las tasas de interés* in es-latam and list it so.
Text: an analysis column in an invented newspaper on why prices rose in an unnamed country and what its central bank did (raised interest rates; demand cooled; growth slowed). Only general, uncontroversial economics, hedged where it is a judgement (*suele*, *tiende a*): raising interest rates tends to make credit dearer and cool demand; high inflation reduces purchasing power. No real country, bank, person, figure or study.

## Checks (from `C:/dev/parlour`, in this order; fix and rerun until clean)

- `python build-manifest.py es-latam` (one course: seconds instead of minutes), then `python scripts/build_word_lesson_index.py es-latam` (rerun both after changing a vocabulary list).
- `python scripts/check-content.py es-latam c1 economy-markets`: fix every error (it also fails a choice item with fewer than 3 options, `few-options`, and a word an earlier C1 lesson already lists, `vocab-relisted`: use that word, don't list it again); fix or give a one-line reason for each suspect.
- `node scripts/unmet-words.js es-latam c1 --stems c1-09-01,c1-09-02,c1-09-03,c1-09-04,c1-09-05,c1-09-consolidation --with-hidden` (C1 core is hidden while it is written; `--with-hidden` counts this unit's and earlier C1 units' own lists, not the latam track). Transparent English cognates are skipped already; every other hit is listed in the first lesson that uses it or replaced by a met word.
- `python scripts/check_es_c1_forms.py es-latam c1 --track core`: no hit in your unit.
- `node scripts/render_lesson.js es-latam c1-09-01 c1-09-02 c1-09-03 c1-09-04 c1-09-05 c1-09-consolidation` and read every screen and item as rendered (`!!` = error).
- `python scripts/check_unit_refs.py es-latam c1 economy-markets --bare --named` (read every hit: a recap of a form rather than a word can be a false positive).
- `python scripts/validate-content.py --changed`.
- `python scripts/lock_tags.py es-latam c1/economy-markets --update --reason "new unit, written 2026-11 (ES C1 core)"`.

## Report

As your final reply (write it to `C:/dev/parlour/imports/review/es-c1-antigravity-09/report.md` and commit it with the unit): files created; per lesson the screen(s), word list and item types; the text's genre, word count and every factual claim with how sure you are; "Norm claims" (see Shape); check results (counts); every Spanish line you are unsure of, marked (unsure); and "For the user": anything you could not fix, any place the plan did not fit. Don't pad.
