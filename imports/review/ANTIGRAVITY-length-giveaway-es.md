# Task: remove the length give-away from Spanish B1/B2 choice exercises (ROADMAP 130)

In these choice exercises the correct option is at least twice as long as
the longest wrong option. It is a full, specific sentence next to two
short fragments, so a learner can pick it by length without understanding
anything:

    ¿Qué le ocurrió a Fernando Collor de Mello en Brasil?
    * Fue destituido por el Congreso en 1992 mediante un juicio político, tras un escándalo de corrupción vinculado a su tesorero de campaña.
    - Fue reelegido sin oposición.
    - Nunca enfrentó ninguna acusación de corrupción.

Fix every listed exercise so that **no option stands out by its length or
its level of detail**.

Repository: this one (Parlour). Commit straight to `master` and push after
every commit.

## Scope: Spanish only, and only these files

- Edit only `content/es-es/exercises/b1/`, `content/es-latam/exercises/b1/`
  and `content/es-latam/exercises/b2/`, plus your worksheet and
  `imports/review/es-review-questions.txt`.
- **Don't touch anything under `content/hu/`, `skills/`, or any
  `tags.lock.json`.** Another agent is retagging Hungarian exercises in
  this same checkout at the same time.
- Stage only the files you changed: `git add <path> …`, never
  `git add -A` or `git add .`. If `git pull --rebase` complains about
  local changes that aren't yours, stop and report. Don't stash, reset or
  commit them.
- The Spanish A1/A2 hits (49) and all Hungarian hits are not part of this
  task.

## The worksheet comes first

`imports/review/es-length-giveaway-worksheet.txt` has one entry per
exercise, in four blocks:

| Block | Exercises |
|---|---|
| es-both B1 (the same exercise in es-es and es-latam) | 127 |
| es-es B1 | 159 |
| es-latam B1 | 224 |
| es-latam B2 | 32 |

Each entry shows the question, the options (`*` = correct) and **every
file the exercise appears in**: both courses, and the lesson file plus its
unit's consolidation file where it was copied. Every copy gets the
identical change.

For each block:

1. Read every entry in the block and fill in `decision:` and `why:` (the
   format is at the top of the worksheet) **before** editing any exercise
   in that block.
2. Apply exactly what the worksheet says, in every file listed.
3. Run the checks, commit, push, **stop and report**.

The reviewer compares the diff with the worksheet entry by entry. An
option changed without a matching decision, or a decision not applied,
counts as an error. Your report counts are checked too, so count, don't
estimate.

**Start each block in a fresh chat.** Re-read this brief and the review
notes at the bottom of this file first.

## How to fix one

Choose **one** of these:

1. **shorten**: cut the correct option down to the key point, in the same
   style as the wrong options (the usual fix for reading, history and
   civics questions).
   `Fue destituido por el Congreso en 1992 mediante un juicio político, tras un escándalo de corrupción …`
   → `Fue destituido por el Congreso tras un escándalo de corrupción.`
2. **match**: rewrite the wrong options into equally long, equally
   specific sentences that are clearly wrong. Use this when the length
   *is* the point. Grammar items like "¿Qué oración presenta una
   concesión?" need a full sentence for the right answer, so the wrong
   options become full sentences that lack the feature or misuse it.
   Dialogue replies also usually need match, because a reply cut short
   may no longer fit the next line.

        ¿Qué oración presenta una concesión?
        * Aunque existan semejanzas, los casos presentan diferencias importantes.
        - Los movimientos movilizaron grupos.                   (before)
        - Como existen semejanzas, los casos presentan pocas diferencias.   (after: cause, not concession)

Aim for options whose lengths are close. Going just under 2× is not
enough: the correct option should no longer be the obviously fullest one.

## Rules

1. **The correct option must still be clearly and completely right.**
   When you shorten it, keep the fact or form the question asks about.
   Check that it still answers the exact question, and that it still fits
   the dialogue line after the blank. A shortened answer that no longer
   answers the question is worse than the give-away.
2. **Exactly one right answer.** A new wrong option must be clearly wrong.
   Careful with:
   - **Grammar:** *aunque* + indicative is also concessive. Imperfect and
     preterite, or future and *ir a* + infinitive, are often both
     acceptable. In "which sentence shows X" items, the new wrong options
     must not also show X.
   - **Facts (history, civics, literature):** a wrong option must be
     false, not "also true but less complete". Don't invent new details
     about real people or events in the *correct* option.
3. **Don't swap one give-away for another.** Wrong options must be
   plausible:
   - no absolutes (*sin ningún*, *nunca*, *absoluto*, *total*) when the
     correct option is the only moderate one;
   - no tense clashes (*leerá* in a past story, "will change tomorrow");
   - no off-topic lines.
   Example: `b1-01-05.ex06` "Porque leerá historias de caballeros" is a
   tense give-away; fixing only the length would leave it in place.
4. **Keep conventions.** If options carry an English gloss in square
   brackets, every new or shortened option gets one too, translated
   literally (errors included). Keep es-latam free of *vosotros*.
5. **Don't change structure**: `id`, `type`, `teaches`,
   `distractor_skills`, `category`, `stage`, `correct` and the order of
   options stay as they are. Don't touch the `question`, except to fix a
   number mismatch your change creates.
6. **Keep formatting.** Edit the JSON in place, non-ASCII as-is, with
   each file's own indentation, so the diff shows only changed option
   lines.
7. **When unsure, log it and leave the exercise unchanged.** Write
   `decision: log` and add the exercise to
   `imports/review/es-review-questions.txt`. Create that file using the
   same format as the top of `imports/review/hu-review-questions.txt`
   (`###` id and file, `why:`, `current:`, `proposed:`).

## Checks before each commit

    python imports/review/check-slash-giveaway.py --length es-es b1 --list
    python imports/review/check-slash-giveaway.py --length es-latam b1 --list
    python imports/review/check-slash-giveaway.py --length es-latam b2 --list
    python scripts/validate-content.py --changed

None of the ids in the block you just did may still appear, unless its
decision is `log`. The validator must pass. Its warnings about tags are
known and not yours to fix.

Commit per block, e.g.

    fix(es/b1): remove the length give-away from 127 es-both choice exercises (ROADMAP 130)

The body gives: shorten count, match count, log count, and the ids where
a correct option was changed (all `shorten` ids).

## The report at each stop

- the block's counts (shorten / match / log);
- every id where the **correct option** changed;
- every id where you also fixed a second give-away (rule 3);
- the questions you logged.

---

## Review notes

(The reviewer adds notes here after each stop. Read them before starting
the next block.)
