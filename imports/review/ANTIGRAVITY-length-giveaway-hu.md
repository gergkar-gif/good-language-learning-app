# Task: remove the length give-away from Hungarian choice exercises (ROADMAP 130)

In these choice exercises the correct option is at least twice as long as
the longest wrong option (and 15+ characters longer). It is a full,
specific sentence next to short fragments, so a learner can pick it by
length without understanding anything:

    Eladó: Mit kér?
    Meg: _____
    * Kérek kenyeret, tejet és sajtot.
    - Hol van a piac?

Fix every listed exercise so that **no option stands out by its length or
its level of detail**.

This is the Hungarian counterpart of
`imports/review/ANTIGRAVITY-length-giveaway-es.md`, which you did for
Spanish. Its method (shorten / match / log), its rules and its review notes
carry over. **Read it first, including the review notes at the bottom**,
then this brief. Where the two differ, this brief wins.

Repository: this one (Parlour). Commit straight to `master` and push after
every commit.

## Scope: Hungarian exercise files, and only these

- Edit only the files listed in your worksheet block under
  `content/hu/exercises/`, plus your worksheet and
  `imports/review/hu-review-questions.txt`.
- **Don't touch `content/es-es/`, `content/es-latam/`, `skills/`, any
  `tags.lock.json`, or any `teaches`, `distractor_skills`, `category` or
  `stage` value.** Another agent is retagging Hungarian exercises in these
  same files (ROADMAP 144) and edits exactly those fields.
- Stage only the files you changed: `git add <path> …`, never
  `git add -A` or `git add .`. Run `git pull --rebase origin master` before
  you start a block and before each push. If it complains about local
  changes that aren't yours, or reports a conflict in an exercise file,
  stop and report. Don't stash, reset or commit anything that isn't yours.
- Not part of this task, even though the checker flags them:
  - the 14 `dialogue-complete` exercises in `a1-121` … `a1-150`, a native
    speaker reviewed them on 2026-10-01. Ids: a1-121-dialogue-1,
    a1-124-practice-5, a1-125-consolidation-13, a1-127-practice-5,
    a1-128-dialogue-1, a1-135-dialogue-2, a1-141-practice-5,
    a1-142-practice-5, a1-144-dialogue-1, a1-145-consolidation-13,
    a1-145-consolidation-14, a1-147-dialogue-1, a1-149-dialogue-1,
    a1-150-dialogue-1. After block 1 these 14 are the only A1 hits left;
  - `c1-21-*` and `c1-22-*` (being rewritten, ROADMAP 127). The checker
    skips them already.

## The worksheet comes first

`imports/review/hu-length-giveaway-worksheet.txt` has one entry per
exercise (586 entries; lesson and consolidation copies of the same
exercise are one entry), in five blocks:

| Block | Exercises |
|---|---|
| 1: A1 + A2 | 70 |
| 2: B1, first half | 149 |
| 3: B1, second half | 148 |
| 4: B2 | 55 |
| 5: C1 | 164 |

Each entry shows the question, the options (`*` = correct), **every file
the exercise appears in**, and its lesson. For each block:

1. Read every entry in the block and fill in `decision:` and `why:` (the
   format is at the top of the worksheet) **before** editing any exercise
   in that block. For each unit, read its lesson file first (the `lesson:`
   line) and, for reading questions, its story: you need to know what the
   learner has met and what the text actually says.
2. Apply exactly what the worksheet says, in every file listed.
3. Run the checks, commit, push, **stop and report**.

The reviewer compares the diff with the worksheet entry by entry. An
option changed without a matching decision, or a decision not applied,
counts as an error. Your report counts are checked too, so count, don't
estimate.

**Start each block in a fresh chat.** Re-read this brief, the Spanish brief
and the review notes at the bottom of this file first. **Do block 1 only,
then stop.** The reviewer tells you when to start block 2.

## How to fix one

Choose **one** of these, as in the Spanish brief:

1. **shorten**: cut the correct option down to the key point, in the same
   style as the wrong options. The usual fix for reading questions and
   fact questions.
2. **match**: rewrite the wrong options into equally long, equally specific
   options that are clearly wrong. Use it when the length *is* the point
   (a grammar item that needs a full sentence, a dialogue reply that would
   no longer fit its line if cut short).

Aim for options whose lengths are close. Going just under 2× is not
enough: the correct option should no longer be the obviously fullest one.

## Hungarian-specific rules (these are the risk here)

You are writing Hungarian that nobody checks before it ships. A new option
that is wrong Hungarian *by accident*, or a new "wrong" option that is
actually fine, is worse than the give-away it replaces.

1. **Every word you write must be certainly correct Hungarian.** Case
   endings (*a postán*, not *postába*; *az állomásra*), vowel harmony
   (*-hoz/-hez/-höz*), definite vs indefinite conjugation, the focus
   position before the verb, agreement, accents and long/short vowels.
   If you are not certain of a form, don't use it.
2. **Build wrong options by breaking exactly one thing.** Take the correct
   sentence, or a sentence of the same shape, and break the point the
   exercise teaches (`teaches` says which): wrong person, wrong case
   ending, wrong tense where the context allows only one, wrong connector.
   Don't compose long free-standing sentences, that is where invented
   Hungarian goes wrong. For reading and fact questions make the wrong
   option **false according to the text** (a changed fact), not just
   different.
3. **Exactly one right answer, and say why.** The `why:` line must state
   why the marked option is the only acceptable one. Watch for synonyms
   (*heti / hetente*, *kedvezmény / akció*), for replies that are fine in
   another register, and for options that are true but "less complete".
4. **Don't swap one give-away for another.** No time word that clashes
   with the tense (*tegnap* with a future verb), no absurd, rude or
   off-topic lines, no *Nem tudom.* (it answers anything), no absolutes
   (*soha*, *mindig*, *semmi*) when the correct option is the only
   moderate one. At A1 a harmless off-topic reply is acceptable when a
   near miss would be too subtle for a beginner, **as long as it isn't a
   sensible reply**.
5. **Level-appropriate vocabulary.** At A1/A2 keep new options to words
   the learner has met in that unit or earlier. At B1 and above, keep the
   register of the original.
6. **Two-option exercises** (44 entries, mostly dialogue replies): there is
   one wrong option, so `match:` gives one text. It must be a reply that
   does not fit the prompt, but not an absurd one.
7. **The correct option must still fit.** After shortening it must answer
   the exact question, fit the dialogue line, and keep the fact the
   question asks about. A shortened answer that no longer answers the
   question is worse than the give-away.
8. **Keep conventions.** If options carry an English gloss in square
   brackets, every new or shortened option gets one too, translated
   literally, errors included. (None of the current hits have glosses, but
   check.)
9. **Don't change structure.** `id`, `type`, `teaches`,
   `distractor_skills`, `category`, `stage`, `correct` and the order of
   options stay as they are. Don't touch the `question` or `prompt`, except
   to fix a number mismatch your change creates.
10. **Keep formatting.** Edit the JSON in place, non-ASCII as-is, each
    file's own indentation, so the diff shows only changed option lines.
11. **When unsure, log it and leave the exercise unchanged.** Write
    `decision: log` and add the exercise to
    `imports/review/hu-review-questions.txt` in that file's format (`###`
    id and file, `why:`, `current:`, `proposed:`). Fewer, certain fixes
    beat many risky ones.
12. **Other defects.** If an exercise on your list has a different defect
    (the marked answer doesn't answer the question, two right answers,
    prompt that depends on another step; see
    `imports/review/ANTIGRAVITY-exercise-quality.md`, H1-H7), fix the
    length give-away only if the exercise is then fully correct. Otherwise
    `decision: log`, and name the defect in the logged `why:`. Known one:
    `a1-09-dialogue-1` (prompt asks how Meg is, marked answer is "Nem
    értem. Még egyszer, légyszi."), see
    `imports/review/hu-review-feedback-a1-a2.md` § 2: log it. Don't go
    looking for defects in exercises that aren't on your list.

## Checks before each commit

Run the checker for the level(s) of your block, and the other two:

    python imports/review/check-slash-giveaway.py --length hu a1 a2 --list
    python imports/review/check-hu-exercises.py a1
    python scripts/validate-content.py --changed

(`check-hu-exercises.py` takes one level at a time: run it for each level
in your block.) None of the ids in your block may still appear in the first
list, except `decision: log` entries, and for A1 the 14 excluded
`a1-121…150` ids. `check-hu-exercises.py` must report `errors: 0`. The
validator must pass; its tag warnings are known and not yours.

Commit per block, e.g.

    fix(hu/a1-a2): remove the length give-away from 70 choice exercises (ROADMAP 130)

The body gives: shorten count, match count, log count, and the ids where a
correct option was changed (all `shorten` ids).

## The report at each stop

- the block's counts (shorten / match / log), counted from the worksheet;
- every id where the **correct option** changed;
- every id where you also fixed a second give-away or defect (rule 12);
- every logged question, with its `why`.

Do not edit ROADMAP.md or ACHIEVED.md. The reviewer does.

---

## Review notes

(The reviewer adds notes here after each stop. Read them before starting
the next block.)
