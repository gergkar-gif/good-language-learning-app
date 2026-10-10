# Pilot: regenerate hu a1 `where-things-are` (ROADMAP 149 step 3, 153)

A test run, one of three arms. The same week, Sonnet regenerates
`plurals-quantities` (unit 8) and fixes `possession` (unit 9) the current
way; this is unit 11. All three are then read blind and compared on defects left, time and
cost. Note the time you start and finish; put both in the commit body.

## What to do

Regenerate the unit's **lessons and exercises** from scratch under
[docs/course-generation-brief.md](../../docs/course-generation-brief.md),
reusing what already exists around them:

- **Keep:** the stems (`a1-51` … `a1-55`, `a1-55-consolidation`), the
  grammar screens, the vocabulary files and the story
  (`content/hu/stories/original/a1/a1-unit-11.json`). Fix any of them that
  break a rule (a wrong rule, an example or story line using a word or form
  not yet taught, a listed word no exercise uses), and say so in the commit.
- **Write new:** every exercise file (`content/hu/exercises/a1/<stem>-ex.json`),
  each lesson file's `goal`, sections and `checklist` (`content/hu/lessons/a1/<stem>.json`),
  and the six challenges in `content/hu/curriculum/challenges.json`.
  Throw the old exercises away; don't edit them.
- **Shape:** brief § 2.2 for the five lessons (Introduce 2, Controlled 4,
  Practice 5, Dialogue 2, Production 2, Check 2; the story and a Reading
  group of 3 on `a1-55`), § 2.3 for the consolidation (4 × 5). Exercise ids
  `<stem>-<stage>-<n>` (`a1-51-controlled-3`).
- **What the unit may use:** each lesson teaches its own grammar screens'
  point; every exercise uses only what units 1–10 and the unit's own
  earlier lessons taught. "Met" is defined in `docs/unit-finish-brief.md`
  step 4.
- **Rules:** brief § 6 (one right answer, one fault per wrong option, no
  length give-aways, no tells, never the quoted line), § 7, and
  AGENTS.md § "Exercise metadata" for every tag. The skill list is frozen.

## Checks, then commit

    python scripts/check-content.py hu a1 where-things-are
    node scripts/render_lesson.js hu a1-51 a1-52 a1-53 a1-54 a1-55 a1-55-consolidation
    python scripts/validate-content.py --changed

Fix everything the checker reports (accept suspects only with a reason),
read every rendered screen, then lock the new tags:

    python scripts/lock_tags.py hu a1/where-things-are --update --reason "regenerated (pilot)"

**Don't freeze.** Commit the unit on its own,
`content(hu): regenerate a1/where-things-are (pilot, ROADMAP 149)`, with
the start and finish times, what you kept and fixed in the screens,
vocabulary and story, and every accepted suspect. Push, then stop and report.
