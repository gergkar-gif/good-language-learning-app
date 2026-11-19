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
5. Self-read before committing (added 2026-11-19: the reviewer's reads kept finding ~32 fixes a
   unit). Read your own unit exactly as the reviewer's readers do:
   - `python scripts/fill_c1_prompts.py reader C:/dev/parlour --norm-notes imports/review/es-c1-plan/antigravity/self-read-norm-notes.md <unit id>`
     writes `.scratch/reader-prompt.md`; follow it as a reader (report and fixes file only), with
     fresh eyes: forget that you wrote the unit.
   - Apply your fixes: `python scripts/apply_replacements.py .scratch/fixes-<unit id>.json`, then
     `python scripts/lock_tags.py es-latam c1/<unit id> --update --reason "self-read"` and every check
     of the unit brief again until clean.
   - Copy the read's report to `imports/review/es-c1-antigravity-NN/self-read.md` and the fixes file
     to `imports/review/es-c1-antigravity-NN/self-read-fixes.json`, and put the number of fixes at
     the top of your unit report ("Self-read: N fixes"). The reviewer compares it with its own read.
6. Append to `imports/review/es-c1-plan/lessons-learned.md` under "Writer's notes" one to three
   lines: what your self-review caught in this unit, as a rule (`Unit N: … -> …`). Only real
   findings; none is fine.
7. Commit and push exactly as the unit brief says (one commit per unit: the unit's files, its
   notes if you wrote them, its brief, its report, the self-read report and fixes, the
   lessons-learned lines, and the indexes the scripts wrote). Then go back to step 1 for the next unit.

## When to stop

- This run (user, 2026-11-19): Units 16 to 27, twelve units, with no stop for review in between.
  When Unit 27 is committed, stop and report: the run is done.
- After 4 units in one chat: write a short summary of the four (units, self-read fix counts, check
  counts, anything for the user) at the end of the fourth report and stop; the user starts a fresh
  chat for the next block (long chats lose track of the brief).
- When your allowance is running low: finish or abandon the current unit cleanly (never commit a
  half-written unit; `git stash` it and say so in your last message) and stop.
- When a check cannot be made clean, or a unit's plan does not fit the course (a recap the sheet
  does not support, a skill that does not exist): commit nothing for that unit, describe it, stop.
- Never edit a frozen unit, any es-es file, ROADMAP.md, ACHIEVED.md or the docs.
