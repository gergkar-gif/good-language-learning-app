# Task: Hungarian C1 exercise review (ROADMAP 120)

Review every Hungarian C1 exercise: 432 files, 3,691 exercises, in
`content/hu/exercises/c1/`. This is the same review you did for A1-B2
(ROADMAP 117), now for the C1 units you generated.

**This is a review, not generation.** Don't add units, lessons, stories
or exercises, and don't edit anything outside `content/hu/exercises/c1/`.
If you spot a problem elsewhere, log it in the questions file.

## Read first

1. `imports/review/ANTIGRAVITY-exercise-quality.md`: Part B, "How to
   work", "What to look for" (H1-H7), the rules for both parts and
   "When you are not sure". All of it applies here.
2. `imports/review/hu-review-feedback-a1-a2.md`: all 10 sections. These
   are the mistakes the reviewer found in your earlier rounds. Treat
   them as hard rules. The four that matter most are repeated below.

## The four rules from earlier rounds

**R1. Never put a sensible reply as a wrong option** (feedback section 5).
In dialogue and "choose the reply" exercises, a wrong option with a
different *content* is almost always also a good reply. Wrong options
must be wrong in **form**: the correct reply with an error on the lesson's
grammar point (wrong case, person, tense, conjugation, word order), or a
reply that contradicts itself.

**R2. Never rewrite a correct answer that is right** (section 8). Change
the marked answer only when it is wrong Hungarian or doesn't answer the
question, and then make sure the new one answers that exact question.
Don't rewrite it to show off the lesson's grammar.

**R3. Word-order wrong options must be clearly wrong** (section 10). A
different but grammatical word order is not a wrong option.

**R4. Hints follow section 9.** See the next section: at C1 this is most
of the work.

## The big C1 problem: the hint contains the answer

About 970 of the 1,022 C1 fill-blanks print the answer inside the hint:

    A beteg emberi méltóságának része a méltóságteljes _____ való jog …
    (to death / halálhoz)                         answer: halálhoz

The learner just copies it. Fix every one, using the section 9 rule:

- **The answer is an inflected form** (most of them): replace the
  Hungarian in the hint with the **dictionary form plus the grammar**.
  `(to death / halálhoz)` → `(to death / halál + -hoz)` or
  `(halál, allative)`. `(guarantee / záloga)` → `(guarantee / zálog,
  possessive 3sg)`. `(evaluating / értékelve)` → `(értékel, adverbial
  participle)`. Pick one style per file and keep it.
- **The answer is itself the dictionary form**: keep the English only,
  and add every other correct word to `answers` (a list, replacing
  `answer`) so synonyms are marked right.
- **Multi-word answers** (`közlekedési szegénységbe`): give the base
  phrase and the ending: `(transport poverty / közlekedési szegénység
  + -be)`.
- **Check the English while you are there.** Some are wrong:
  `(mobility trap / közlekedési szegénységbe)` means "into transport
  poverty", not "mobility trap". Fix the English to match the answer.

After the fix, the solved sentence must still read as correct Hungarian,
and the hint must lead to exactly one answer (or list the others in
`answers`).

## How to work

- Go in the order of `imports/review/hu-review-progress.md`, section C1:
  blocks of 12 units (a numbered unit, then a topic unit). Tick each file
  (`[x]`) when every exercise in it is reviewed.
- Before a unit's exercises, read its lessons
  (`content/hu/lessons/c1/<name>.json`) and the grammar they reference.
- Review **all types**: fill-blank, multiple-choice, dialogue-complete,
  structured-writing, sentence-builder, matching. Earlier rounds touched
  almost only choice exercises; the reviewer checks this.
- **Take your time.** Earlier levels went at 2-4 seconds per exercise,
  and the problems the reviewer found came from that speed.
- **Use the questions file.** `imports/review/hu-review-questions.txt`,
  format at the top. Anything you're unsure about (natural Hungarian?
  two acceptable answers?) goes there instead of being changed. Zero
  questions after 600 exercises means you are deciding too much alone.
- Commit after each half block (6 units, about 36 files):

      fix(hu/c1): review c1-01 … c1-emberijogok exercises (ROADMAP 120)

  The body says how many exercises changed, the main kinds of fix, how
  many hints were rewritten, and how many questions were logged.
- `git pull --rebase` and `git push` after every commit. Unpushed
  commits can't be reviewed.

## Checks before each commit

    python imports/review/check-hu-exercises.py c1
    python scripts/validate-content.py --changed

The first must report `errors: 0`. Its suspects for the files you have
done must be 0, or each one named in the commit message with the reason:

- `hint-leak` (new): the answer appears word for word in the hint. Only
  fine when the answer is the dictionary form itself.
- `giveaway`: a time word in a wrong option only (C1 has 32 now).
- `case`: an -n/-ra noun used with -ban/-ba (C1 has 17 now).

The script counts all of C1, so the totals fall as you go. Run it with
`--list` to see the ids.

## Stop after block 1

After the first 12 units (72 files, about 600 exercises), **stop and
report**: files done, exercises changed by type, hints rewritten,
correct answers changed (each id, with why), questions logged, and the
suspect counts left. Don't start block 2 until told to continue.

The reviewer then reads a random sample, diffs every changed correct
answer, and checks the hint rewrites. Problems come back to you as a new
section in `hu-review-feedback-a1-a2.md`.
