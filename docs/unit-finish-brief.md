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
2. **Read every lesson as the learner gets it,** screen by screen:

        node scripts/render_lesson.js <course> <stem> [<stem> ...]

   This runs the app's own lesson builder, so it shows the screens nobody
   writes by hand: the two **Speaking Practice** steps (the engine picks
   them from grammar examples, exercises and vocabulary) and the
   **Communicative Challenge**. Read all of it, not only what is flagged:
   goals, grammar screens, vocabulary, every exercise, the story, the
   speaking steps, the challenge, the checklist. You are looking for what no
   check can see: an answer that doesn't answer, two right answers, a word or
   form the learner hasn't met, an English gloss written into a sentence, an
   `english` line that doesn't match, a question that depends on a step that
   isn't shown, a speaking step whose English isn't its sentence. Any `!!`
   line at the end (a missing file, a missing exercise) is an error.
   Then check that every word of the unit's story can be tapped in the
   Reader: `node scripts/audit-reader-coverage.js <course> --story <story file
   stem> --top 0` must report 0 "not in the dictionary" (names excepted) and
   0 "lookup throws"; a miss is reported, not fixed in the dictionary by
   hand.
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
   - **The challenge: write one for every lesson** in
     `content/<course>/curriculum/challenges.json`, keyed by the lesson stem
     (`a1-06`, `a1-01-02`). The model is `hu` `a1-01` … `a1-05`. Fields:
     `tier` (`tier1` A1, `tier2` A2), `level`, `title`
     (`Communicative Challenge: <short name>`), `scenario` (one situation,
     with the story's people), `prompt` (the task in English), `cues` (2–3),
     `target` (the model answer), `english` (its translation), `canDo` (the
     lesson's first checklist line, copied).
     What the learner sees: at A1 the scenario, then *Say this in
     <language>:* with the `english` line, and the cues as a hint; at A2 the
     scenario, the `prompt` and the cues as *Points to include*, with
     `target` revealed after. So **cues say what to include, never the
     words** (*Greet him back*, not *Greeting (Szia)*: the hint is shown
     before the learner speaks). The target answers the prompt exactly, uses
     only words and forms the learner has met by this lesson, and is short:
     one to three sentences at A1. Check it in the render. es-es and es-latam
     each get their own entry (no *vosotros*, a Latin American setting in
     es-latam).
   - **Speaking steps:** if one is wrong (its English isn't a translation of
     its sentence, the sentence is broken or not taught yet), fix the source
     line it was built from (the grammar example or the exercise's
     `english`); if the source is right and the engine's choice is wrong,
     stop and report it.
   - **Metadata, on every exercise.** The learner model, the review engine
     and the skill map run on it, so a wrong tag teaches the app something
     false about the learner. Rules: [AGENTS.md](../AGENTS.md) § "Exercise
     metadata" and [skill-tagging-spec.md](skill-tagging-spec.md)
     § "Read-through conventions". Check each exercise:
     - `teaches`: the one skill **a wrong answer shows** (a tested form gets
       its grammar skill, a tested word the unit's vocabulary skill).
     - `distractor_skills` (grammar choice items): every wrong option that is
       a real form of **another** skill, by option index; none for a wrong
       form of the same skill. *Én Meg vagyok* for "You are Meg" is
       `{"1": "personal-pronouns"}`.
     - `category` follows the tag (a vocabulary skill is `vocabulary`).
     - `hint` (fill-blanks): only when the blank can't be recovered, never
       the answer, names the person where the form is person-marked.
     - `english` on every fill-blank and sentence-builder, translating the
       completed sentence and fitting no other answer; `answers` lists every
       correct alternative.
     **Whenever you change an option, a sentence or a prompt, re-check that
     exercise's `teaches` and `distractor_skills` against the new text**: a
     replaced wrong option keeps its old `distractor_skills` entry until you
     change it, and the validator can't see that it no longer fits (it
     happened in the model unit: *Ki ő?* replaced by *Ez egy tea.*, still
     recorded as `ki-and-mi`). A new wrong option should be a near miss of
     the skill the exercise teaches, so a wrong answer still shows that
     skill.
     Tags are locked, so after changing any `teaches`, `distractor_skills`
     or `category`, re-lock the unit:
     `python scripts/lock_tags.py <course> <level>/<unit id> --update --reason "..."`,
     and list every tag change in the commit body. Never add, rename or merge
     a skill (the list is frozen): if no skill fits, stop and report.
   - What you found by reading: fix it if you are certain; otherwise stop
     and report it with your proposal.
4. **Edit rules.** Edit the JSON text in place (no re-dump), keep each
   file's formatting. Don't change `id`, `type`, `stage` or `correct`; tags
   change only as in step 3, with a re-lock. Words you write: only forms you are certain of, at A1/A2 only
   words the learner has met in this unit or earlier.
   **What counts as met:** a word or form is met when it is in a vocabulary
   list, or is the subject of a grammar screen, at or before the lesson. A
   lesson may also use whole phrases from its *own* grammar examples. A word
   seen only in another lesson's example, a tip or a story is not met. This
   applies to everything the learner reads: prompts, right answers, wrong
   options, challenge targets.
5. **Check.** Re-run step 1 until it shows only what you will accept, re-run
   the render (no `!!` lines, every screen right), then
   `python scripts/validate-content.py --changed` and
   `python scripts/check-content.py --changed`.
6. **Don't freeze yet.** Commit the unit (step 7) unfrozen. A second
   reader (a Sonnet subagent run by the reviewer) then reads the unit
   independently and the reviewer turns its findings into a checked fix list,
   `imports/review/sonnet-reads/<course>-<level>-<unit id>.md`. Fix every item
   on that list, then freeze:

        python scripts/freeze_unit.py <course> <level> <unit id> --reason "all checks fixed, every exercise read, second read fixed"             --accept "<check>:<exercise id>:<why it stays>" ...

   `freeze_unit.py` refuses while anything is left that isn't accepted, and
   only suspects and the two tell checks can be accepted.
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

Do **four units per run** (or the fix lists for units already read), each committed and pushed on its own
(`git pull --rebase origin master` first; stage only your files). Then stop
and report, per unit: the counts fixed by kind, every accepted finding with
its reason, every correct option you changed, and anything you stopped on.
The reviewer reads each unit's diff and adds notes below; read them before
the next run.

Do not edit ROADMAP.md or ACHIEVED.md. The reviewer does.

---

## Review notes

(The reviewer adds notes here after each run.)

### Run 1 (hu a1 `greetings-basic-interaction`, `introducing-yourself`), reviewed 2026-10-09

Commits `c1efa15dd`, `c4bdb9030`. The checker findings are fixed, the
challenges exist for every lesson, the cues don't give the answers away, and
the suspects you accepted are right. **But steps 2 and 3 (reading every
screen and checking every exercise's metadata) were not done:** neither
commit reports a single reading finding or tag change, and the review found
these. Both units are **unfrozen**; fix them, then freeze them again (a
change that re-freezes a unit passes the pre-push check).

1. `a1-13-practice-3`: its `distractor_skills` still says options 1 and 2 are
   `ki-and-mi` forms, but you replaced them (*Ő egy jó barát.*, *Ki az a
   férfi?*). This is the exact case step 3 warns about. Make the wrong
   options near misses of `spatial-questions-hol-hova` (the skill it
   teaches) or of a skill you then record, and set `distractor_skills` to
   match; re-lock.
2. *az a* + noun (*az a férfi*, *az a barát*) is not taught anywhere in A1:
   `a1-13-practice-3` and `a1-14-dialogue-1` use it in new options. Only
   forms the learner has met.
3. `a1-11` challenge: *A nevem Meg. Hogy hívnak?* uses *nevem* and
   *hívnak*, first met in unit 3's story. Rewrite with what a1-11 teaches
   (*Én Meg vagyok. Te ki vagy?* style).
4. `a1-08`, `a1-09`, `a1-10` share one generic checklist (*I can use the new
   greetings and polite expressions.*), so their challenges share a can-do.
   Write each lesson's own two checklist lines from its goal and content
   (a1-09 is asking someone to repeat or slow down) and copy the first into
   its challenge's `canDo`. This is the kind of thing reading finds.
5. `a1-15-controlled-1` and `-2`: the wrong options break two things at once
   (*Ő Meg van.*: wrong person **and** wrong copula). HU rule 2: break exactly
   one thing, the skill the exercise teaches (`van-zero-copula`): *Én Meg
   van. Itt lakom.*, *Én Meg vagy. Itt lakom.*
6. `a1-15-practice-3`: *Én Meg vagyok.* as a wrong answer to *Hol laksz?* is
   recorded as `van-zero-copula`, but it is a correct copula sentence that
   answers *who*, not *where*: `ki-and-mi`, like option 2. Check the other
   `distractor_skills` in both units the same way: does picking that option
   really show the learner mixing up that skill?
7. `a1-09-dialogue-1` (open since ROADMAP 130): Mariann's line ends in *hogy
   vagy?*, which the learner learned in a1-08, so *Nem értem* doesn't fit.
   Use the proposal in `imports/review/hu-review-questions.txt`: a fast line
   Meg can't follow (*Szia, Meg, elugrom a postára egy levélért, aztán sietek
   a piacra!*), keep *Nem értem. Még egyszer, légyszi.* as the answer, and a
   wrong option that is no reply to it. Remove the entry from the questions
   file.

**From now on the commit body has three sections, each non-empty or saying
why it is empty:** *Checker findings*, *Found by reading* (every defect you
found that no check flagged), *Metadata* (every `teaches`,
`distractor_skills` or `category` you changed, and the exercises whose new
options you re-checked). The reviewer compares *Found by reading* with their
own read of the unit.
