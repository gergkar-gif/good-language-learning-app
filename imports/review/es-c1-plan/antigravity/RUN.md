# Antigravity: write the ES C1 core units, one after another (general run brief)

User's decision (2026-11-19): Antigravity writes the remaining ES C1 core units unattended; Claude
reads, fixes, freezes and plants them in es-es later, in batches. You do not wait for Claude
between units, but you learn from every review Claude has finished so far.

Start every chat by reading this file to the end. (Revised 2026-11-19 after the review of Units 16-19: the self-read is replaced by targeted checks, and blocks are three units again.) Work in `C:/dev/parlour`.

## The loop (one unit at a time)

1. `git pull --rebase --autostash origin master` (brings in Claude's latest reviews and notes).
2. `python scripts/c1_next_unit.py` names the next unit.
   - "DONE": stop and report.
   - "STOP" (a unit with a new skill and no notes): stop and report; Claude writes those notes.
   - "Draft the notes first": write `imports/review/es-c1-plan/notes/<unit id>.md` exactly as
     `imports/review/es-c1-plan/notes/README.md` says (recap skills from
     `python scripts/c1_recap_candidates.py`).
3. Learn from the reviews: read `imports/review/es-c1-plan/lessons-learned.md`, then run
   `python scripts/c1_reviewer_changes.py --last 3` and read every change the reviewer made to
   your earlier units. Do not repeat any of those defects.
4. Build the unit's brief: `python scripts/fill_c1_prompts.py antigravity C:/dev/parlour <unit id>`.
   It writes `imports/review/es-c1-plan/antigravity/unit-NN-<unit id>.md`. Follow that brief
   exactly, up to and including its checks.
5. Before committing, three targeted checks (the full self-read of Units 16-19 found real defects but
   did not lower what the reviewer's read found, so it is dropped):
   - `python scripts/c1_known_forms.py <unit id>`: every Spanish form on your screens that an
     earlier core screen already shows. For each NOT RECAPPED form the learner needs, the screen
     says "You know *X* from <Level> Unit N" (the unit the tool gives) and teaches only what is
     new about it. This was the most frequent defect of Units 13-19.
   - Render the unit (`node scripts/render_lesson.js es-latam <the six stems>`) and read every
     choice item once with one question only: does EACH wrong option have its own single fault,
     and is none of them acceptable Spanish? Then every prompt: could two answers fit it?
   - Every challenge `tier` is `"tier1"` (the grader scores `tier2` as a transaction and failed a
     correct target in Unit 19).
6. Append to `imports/review/es-c1-plan/lessons-learned.md` under "Writer's notes" one to three
   lines: what your self-review caught in this unit, as a rule (`Unit N: … -> …`). Only real
   findings; none is fine.
7. Run `python scripts/c1_report_check.py <unit number>` and complete the report until it passes (it
   needs the norm-claims list, the checks and your unsure lines: Units 18-19's reports left out
   the norm claims). Then commit and push exactly as the unit brief says (one commit per unit: the unit's files, its
   notes if you wrote them, its brief, its report, the lessons-learned lines, and the indexes the
   scripts wrote). Then go back to step 1 for the next unit.

## When to stop

- This run (user, 2026-11-19): Units 28 to 36, the last nine units of C1 core, with no stop for
  review in between. Unit 36 `own-voice-c1` has reviewer-written notes (a capstone that recaps the
  C1 skills themselves); Units 28-35 are topic units whose notes you draft, following the
  "Topics with real people, works and ideas" rules in `notes/README.md`. When Unit 36 is
  committed, stop and report: C1 core is written.
- After 3 units in one chat: write a short summary of the three (units, check counts, anything for
  the user) at the end of the third report and stop; the user starts a fresh chat for the next
  block. (Four was tried for Units 16-19: the fourth unit had the shortest report, no norm claims
  and the most defects the reviewer found.)
- When your allowance is running low: finish or abandon the current unit cleanly (never commit a
  half-written unit; `git stash` it and say so in your last message) and stop.
- When a check cannot be made clean, or a unit's plan does not fit the course (a recap the sheet
  does not support, a skill that does not exist): commit nothing for that unit, describe it, stop.
- Never edit a frozen unit, any es-es file, ROADMAP.md, ACHIEVED.md or the docs.
