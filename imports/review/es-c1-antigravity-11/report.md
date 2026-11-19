# ES C1 Core Unit 11 (`debate-information`) — Antigravity Report

- **Model / setting:** Antigravity (Gemini), default effort
- **Wall-clock time:** ~6 minutes
- **Allowance:** not visible from this environment

## Files created / updated

- Brief: `imports/review/es-c1-plan/antigravity/unit-11-debate-information.md`
- Lessons: `content/es-latam/lessons/c1/c1-11-01.json` … `c1-11-05.json`, `c1-11-consolidation.json`
- Grammar screens: `content/es-latam/grammar/c1/c1-11-01-a-gr.json` … `c1-11-05-a-gr.json`
- Vocabulary: `content/es-latam/vocabulary/c1/c1-11-01-voc.json` … `c1-11-05-voc.json`
- Exercises: `content/es-latam/exercises/c1/c1-11-01-ex.json` … `c1-11-05-ex.json`, `c1-11-consolidation-ex.json`
- Story: `content/es-latam/stories/original/c1/c1-11.json`
- Updated via scripts: `skills/es.json` + generated skill registries (`set_planned_taught_in.py`), `content/es-latam/curriculum/challenges.json` (6 challenges via `add_challenges.py`), `content/es-latam/indexes/tags.lock.json` (55 exercises via `lock_tags.py`)

## Per-lesson summary

- **c1-11-01** — Screen: `c1-11-01-a-gr` (**NEW** `dislocacion-clitica`, contrasting with focus fronting from B2 Unit 1). Words (7): *el moderador, la réplica, el turno de palabra, el enfoque, el razonamiento, el interlocutor, la intervención*. Items (8, 6 types; 7 tagged `dislocacion-clitica`): `multiple-choice` (2), `matching`, `fill-blank` (2), `listening-choice`, `dialogue-complete`, `sentence-builder`.
- **c1-11-02** — Screen: `c1-11-02-a-gr` (recap `contrast-concession-connectors`, B1 Unit 1; `concesivas-si-bien`, B2 Unit 8). Words (6): *la concesión, la falacia, el consenso, la alusión, la contrarréplica, contundente*. Items (8, 6 types): `multiple-choice` (2), `matching`, `fill-blank` (2), `dictation`, `dialogue-complete`, `structured-writing`.
- **c1-11-03** — Screen: `c1-11-03-a-gr` (recap `imperfecto-de-cortesia`, B2 Unit 2; `formal-register`, B2 Unit 14). Words (6): *intervenir, ceder la palabra, pedir la palabra, tomar la palabra, retomar, la brevedad*. Items (8, 6 types): `multiple-choice` (2), `matching`, `fill-blank` (2), `listening-choice`, `dialogue-complete`, `sentence-builder`.
- **c1-11-04** — Screen: `c1-11-04-a-gr` (recap `reformulation-markers`, B2 Unit 29; `discurso-indirecto-deicticos`, B2 Unit 17). Words (6): *tergiversar, la tergiversación, razonar, desviar el tema, ceñirse al tema, el ponente*. Items (8, 6 types): `multiple-choice` (3), `matching`, `fill-blank`, `dictation`, `dialogue-complete`, `structured-writing`.
- **c1-11-05** — Screen: `c1-11-05-a-gr` (recap `consecutivas-de-tal-manera`, B2 Unit 31). Words (6): *el cierre, la síntesis, el foro, la mesa redonda, la contundencia, la ponencia*. Items (11, 6 types): `multiple-choice` (5 incl. 3 reading), `matching`, `fill-blank` (2), `listening-choice`, `dialogue-complete`, `sentence-builder`. Story: `c1-11.json`.
- **c1-11-consolidation** — 12 items, 7 types (`multiple-choice` 3, `matching`, `fill-blank` 3, `listening-choice`, `dictation`, `dialogue-complete`, `sentence-builder`, `structured-writing`), covering `dislocacion-clitica` (3 items, 10 total across the unit) plus all recapped skills and `c1-debate-information-vocab`.

## Unit text (`c1-11.json`)

- **Genre:** debate transcript (invented televised round table *Foro Abierto*, moderator + unnamed *la invitada* and *el invitado*)
- **Word count:** 424 Spanish words
- **Factual claims (all general debate arguments, no real programme/person/statistic):**
  1. Phone notifications can interrupt classroom concentration and limiting phones during school hours tends to encourage social interaction during breaks. (certain — hedged general debate argument)
  2. Teaching digital skills on school computers avoids relying on students' personal devices. (certain — general observation)
  3. Monitoring thirty personal screens at once is very difficult for a teacher. (certain — practical classroom observation)
  4. Age-based rules are an alternative to a blanket ban. (certain — policy option)

## Norm claims (exact wording on screens)

- `c1-11-01-a-gr`: "Fronted **topic** (an object already known from the conversation): the clitic is required (*Ese informe lo firmó la directora*; *Ese informe firmó la directora* is wrong as a topic)." / "Fronted **contrastive focus** (new or contrasted quantity/item): no clitic (*Un solo dato le pido, no diez*)." / "Fronted **indirect object**: the clitic *le / les* is required (*A los interlocutores les preocupa el enfoque*)."
- `c1-11-02-a-gr`: "*si bien* takes the indicative (not the subjunctive) when conceding an accepted fact; second, never add *pero* at the start of the main clause after *si bien*."
- `c1-11-03-a-gr`: "In formal debates, keep *usted* consistent throughout the turn (*Si me permite... le agradezco...*, never mixing *si me permites* with *le cede*)."
- `c1-11-04-a-gr`: "In formal exchanges, *es decir* and *en otras palabras* fit better than informal *o sea*." / "when reporting a past statement from another day and place, do not leave *hoy* or *aquí* unchanged — shift them to *ese día / aquel día* and *allí*."
- `c1-11-05-a-gr`: "When the result is a real fact, the verb is in the **indicative**; when it expresses an intended goal or follows a negated main clause, it takes the **subjunctive**." / "In formal writing, keep the preposition *de* in *hasta el punto de que* (preferred over *hasta el punto que*)."

## Check results

- `python scripts/check-content.py es-latam c1 debate-information`: 0 error(s), 0 suspect(s)
- `node scripts/unmet-words.js es-latam c1 --stems c1-11-01,c1-11-02,c1-11-03,c1-11-04,c1-11-05,c1-11-consolidation --with-hidden`: 0 hits (`[]`)
- `python scripts/check_es_c1_forms.py es-latam c1 --track core`: 0 hit(s)
- `node scripts/render_lesson.js es-latam c1-11-01 ... c1-11-consolidation`: 0 `!!` errors; self-reviewed in full
- `python scripts/check_unit_refs.py es-latam c1 debate-information --bare --named`: 0 recap reference(s) to check (1 unchecked non-italicised reference to B2 Unit 1 emphatic focus fronting, verified against `b2-01-03-a-gr`)
- `python scripts/validate-content.py --changed`: `es-es: 1 passed, 0 failed`, `es-latam: 24 passed, 0 failed`
- `python scripts/lock_tags.py es-latam c1/debate-information --update ...`: locked 55 exercise(s)

## Unsure Spanish lines

None.

## For the user

Nothing blocking. `dislocacion-clitica` has 10 tagged items across Lesson 01 (7) and Consolidation (3); every wrong option without a clitic is pinned as a known topic in context.
