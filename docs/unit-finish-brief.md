# Finishing a unit: brief for Antigravity (ROADMAP 153)

The work goes **unit by unit, not problem by problem.** You take one unit,
fix everything that is wrong with it in one go, and freeze it. A frozen unit
is done: nobody works on it again unless the user sees a problem in the app.
Progress is counted in frozen units:

    python scripts/freeze_unit.py --status

Gate 1 is **A1 and A2 in hu, es-es and es-latam**. Order: HU A1 → HU A2 →
Spanish A1 → Spanish A2, each in the order of `content/<course>/curriculum/units/<level>.json`.
The model is `hu a1/reading-hungarian`, frozen 2026-10-09: read the commit
that froze it (`git log -p --grep "reading-hungarian"`) before your first unit.

## Read first

- This file, whole.
- [course-generation-brief.md](course-generation-brief.md) § 6 (exercise
  rules) and § 8.2 (what a reader judges).
- [AGENTS.md](../AGENTS.md) § "Exercise metadata".
- For choice exercises, the rules and **every review note** in
  `imports/review/ANTIGRAVITY-length-giveaway-hu.md` (rules 1–13) and
  `imports/review/ANTIGRAVITY-length-giveaway-es.md`. In one line: each
  wrong option is a different real fact, form or reply, in the same tone and
  about the same length as the correct one; never an absolute, never a stock
  "bad news" line, never absurd.

## One unit

1. **Report.** `python scripts/check-content.py <course> <level> <unit id>`.
   Errors must all be fixed; suspects (`suspect`) must each be fixed or
   accepted with a reason.
2. **Read the whole unit,** not only what is flagged: every lesson's
   exercises, vocabulary list and grammar screens, and the story. You are
   looking for what no check can see: an answer that doesn't answer, two
   right answers, a word or form the learner hasn't met, an English gloss
   written into a sentence, an `english` line that doesn't match, a
   question that depends on a step that isn't shown.
3. **Fix everything in this unit, in one pass.**
   - `length-giveaway` (correct option over 1.3× the longest wrong one):
     shorten the correct option, or make the wrong ones as long and as
     specific. Never accepted.
   - `tell-absolute`, `tell-time-word`: fix when the word lets a learner rule
     the option out without knowing the point; accept when the word is the
     point (*ayer* in a wrong option of a pretérito perfecto item) or the
     options are just other words (*melyik / senki / valami*).
   - `taught-later` (a form used before the screen that teaches it): rewrite
     the exercise so it doesn't need the form. If the form is right there
     and the registry's `taught_in` is wrong, don't change the registry
     (the skill list is frozen): stop and report it.
   - `vocab-unused`: a word in the lesson's vocabulary list that no exercise
     of the lesson uses. Use it in an existing exercise (a matching pair, an
     option, a sentence), or accept if the list is a review list and the
     word is drilled earlier in the unit.
   - Other suspects: fix, or accept with the reason (*the reply to Szia is
     Szia*).
   - What you found by reading: fix it if you are certain; otherwise stop
     and report it with your proposal.
4. **Edit rules.** Edit the JSON text in place (no re-dump), keep each
   file's formatting. Don't change `id`, `type`, `teaches`,
   `distractor_skills`, `category`, `stage` or `correct`; the tags are
   locked. Words you write: only forms you are certain of, at A1/A2 only
   words the learner has met in this unit or earlier.
5. **Check.** Re-run step 1 until it shows only what you will accept, then
   `python scripts/validate-content.py --changed` and
   `python scripts/check-content.py --changed`.
6. **Freeze.**

        python scripts/freeze_unit.py <course> <level> <unit id> --reason "all checks fixed, every exercise read" \
            --accept "<check>:<exercise id>:<why it stays>" ...

   It refuses while anything is left that isn't accepted, and only suspects
   and the two tell checks can be accepted.
7. **Commit the unit on its own:**
   `content(hu): finish and freeze a1/greetings-basic-interaction (ROADMAP 153)`,
   with what you fixed and what you accepted in the body.

## Spanish: both courses at once

es-es and es-latam share most units. Do a unit in both courses together:
the same fix in both copies, then freeze it in each course. es-latam never
gets a *vosotros* form; where the courses must differ, say so in the commit
body.

## Frozen units

- Never edit a frozen unit. `check-content.py --changed` (pre-push) blocks
  it. If you find a problem in one, stop and report it; only the reviewer
  or the user unfreezes (`freeze_unit.py --unfreeze … --reason`).
- A unit you are working on isn't frozen until step 6, so fixing it may
  take several edits; that's fine.

## Runs and stops

Do **four units per run**, each committed and pushed on its own
(`git pull --rebase origin master` first; stage only your files). Then stop
and report, per unit: the counts fixed by kind, every accepted finding with
its reason, every correct option you changed, and anything you stopped on.
The reviewer reads each unit's diff and adds notes below; read them before
the next run.

Do not edit ROADMAP.md or ACHIEVED.md. The reviewer does.

---

## Review notes

(The reviewer adds notes here after each run.)
