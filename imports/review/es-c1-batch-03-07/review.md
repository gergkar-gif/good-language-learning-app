# ES C1 core batch Units 3-7 (2026-11-18)

Two Sonnet writers, each writing its units in sequence (user: one writer with two units, one with
three): A = Units 3-4 (`science-communication`, `press-news`), B = Units 5-7
(`opinion-editorial`, `legal-language`, `public-administration`). Reviewer norm check before the
read (`norm-research.md`, `norm-notes-*.md`), one Sonnet reader per writer, plant in es-es.
All five units frozen in es-latam and es-es (C1 7/36 per course); C1 core still hidden.

## Cost (tokens)

| Step | Total | Per unit |
|---|---|---|
| Writer A, Units 3-4 | 302k | ~151k |
| Writer B, Units 5-7 | 408k reported (the run was cut by the usage limit and resumed; the figure may not include the first part) | ~136k |
| Reader, Units 3-4 | 244k | ~122k |
| Reader, Units 5-7 | 323k | ~108k |
| **Writer + reader** | | **~245-275k** (pilot: ~485k) |

Sequential writing let each writer build a generator once and reuse it; that, more than the
template, cut the cost. The generator is now `scripts/es_c1_builders.py`.

## Defects

- Reviewer, before the read: Unit 3 *de ahí que* + indicative used as a wrong option (not
  verifiable from a source: the options were made ungrammatical, the screen says "normally the
  subjunctive"); a pleonasm in the Unit 3 text (*la causa puede deberse a*); Unit 5 "never *el hecho
  que*" softened; Unit 6 text "textos jurídicos antiguos" -> "lenguaje jurídico tradicional" (RAE:
  the future subjunctive survives in current legal and administrative texts).
- Readers: 33 fixes (Units 3-4) and 49 (Units 5-7), all accepted. Main classes: recap unit numbers
  wrong (4 in Units 3-4, 2 in Unit 6), unpinned production prompts, consolidation items copying
  lesson items or screen examples, wrong options a native may accept, challenges not practising
  their canDo, tags copied from another unit (4 items in Unit 6 carried Unit 5's vocabulary
  skill), the Unit 6 text's commentary contradicting its own articles.
- Plant: es-es *estacionamiento* tile -> *aparcamiento* (c1-05-04.ex04); 14 *ustedes* lines in
  Unit 7 kept (formal letters use *ustedes* in Spain too).
- Process: a rebase conflict on challenges.json / tags.lock.json was first resolved by taking
  master's side, which dropped Units 5-7's challenges, locks and taught_in; rebuilt with
  `add_challenges.py`, `lock_tags.py`, `set_planned_taught_in.py` before the push.

## Writers compared (two units vs three)

Both came back with clean checks and similar per-unit cost; B's three-unit run read 49 fixes over
three units (~16/unit) against A's 33 over two (~16/unit). No quality difference is visible at
this sample size. B lost no work to the usage limit (its files were on disk; resumed by message).

## For the user

- `estilo-titular` is titled "headline style with verbless and infinitive clauses", but its screen
  covers verbless and present-tense headlines only (the reviewer told the writer to leave
  infinitive headlines out). Proposed title: "headline style with verbless and present-tense
  clauses".
- Frozen B1 Unit 4 (`content/es-latam/grammar/b1/b1-04-02-conditional-advice-gr.json`): "add *-ra,
  -ras, -ra, -ramos, -ran*" gives *hablaramos*; the form is *habláramos*. Needs an unfreeze.
- Recap unit numbers keep coming out wrong from writers; proposed: a check comparing "from <Level>
  Unit N" with the unit where the named form's skill is taught.
