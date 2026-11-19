# Antigravity: write the ES C1 core units, one after another (general run brief)

User's decision (2026-11-19): Antigravity writes the remaining ES C1 core units unattended; Claude
reads, fixes, freezes and plants them in es-es later, in batches. You do not wait for Claude
between units, but you learn from every review Claude has finished so far.

Start every chat by reading this file to the end. Work in `C:/dev/parlour`.

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
5. Self-review before committing: render the unit (`node scripts/render_lesson.js es-latam <the six
   stems>`) and read every screen, item, challenge and the text once more against the
   lessons-learned list and the brief's "Learned on …" lists. Fix what you find and rerun the checks.
6. Append to `imports/review/es-c1-plan/lessons-learned.md` under "Writer's notes" one to three
   lines: what your self-review caught in this unit, as a rule (`Unit N: … -> …`). Only real
   findings; none is fine.
7. Commit and push exactly as the unit brief says (one commit per unit: the unit's files, its
   notes if you wrote them, its brief, its report, the lessons-learned lines, and the indexes the
   scripts wrote). Then go back to step 1 for the next unit.

## When to stop

- After 3 units in one chat: write a short summary of the three (units, check counts, anything for
  the user) at the end of the third report and stop; the user starts a fresh chat for the next
  block (long chats lose track of the brief).
- When your allowance is running low: finish or abandon the current unit cleanly (never commit a
  half-written unit; `git stash` it and say so in your last message) and stop.
- When a check cannot be made clean, or a unit's plan does not fit the course (a recap the sheet
  does not support, a skill that does not exist): commit nothing for that unit, describe it, stop.
- Never edit a frozen unit, any es-es file, ROADMAP.md, ACHIEVED.md or the docs.
