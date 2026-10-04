# Task: remove the " / " give-away from choice exercises (ROADMAP 126)

In 383 choice exercises the correct option is two phrases joined by
" / ", while every wrong option is a single phrase. A learner can pick
the answer by its shape alone, without knowing anything:

    What does the noun 'álszentség' mean?
    * hypocrisy / sanctimony
    - generous charity
    - military courage

    Melyik kötőszó fejez ki emelkedett összehasonlító-hasonlító viszonyt?
    * miként... akként / amiképpen
    - holott
    - noha

Fix every one so that **no option stands out by its shape**.

Repository: this one (Parlour). Commit straight to `master` and push
after every commit. Edit only `content/*/exercises/`. **Don't touch
`content/hu/exercises/c1/c1-21-*` or `c1-22-*`**: they are being
rewritten separately at the same time (ROADMAP 127).

## The work list

    python imports/review/check-slash-giveaway.py --list

lists every exercise (id and file). Counts: Hungarian A1 12, A2 26, B1 22,
B2 90, C1 167; Castilian Spanish (es-es) 42; Latin American Spanish
(es-latam) 24. Run it with a course and level to see one batch:
`python imports/review/check-slash-giveaway.py hu b2 --list`.

## How to fix one

Read the question and all options first. Then choose **one** of these:

1. **Keep one phrase** (the usual fix). Keep the half that answers the
   question best and is closest in length and style to the wrong
   options. Drop the other half.
   `hypocrisy / sanctimony` → `hypocrisy`.
   `miként... akként / amiképpen` → `miként... akként`.
2. **Give every option the same shape**, if both halves are needed for
   the meaning to be right. Then every wrong option also becomes two
   phrases joined by " / ", and both halves of each wrong option must be
   wrong. Use this rarely.

Never fix it by changing the slash to "or", a comma or brackets: the
correct option would still be the only two-part one.

## Rules

1. **The correct option must still be clearly right** after you shorten
   it. If the half you keep is weaker or ambiguous (for example, a
   gloss that only fits one sense of the word), keep the other half or
   use fix 2.
2. **Exactly one right answer.** Don't change the wrong options unless
   you use fix 2. If one of them turns out to be also correct, log it
   (see below) instead of guessing.
3. **Don't change structure**: `id`, `type`, `teaches`, `category`,
   `stage`, `correct` and the order of options stay as they are.
4. **Copies stay identical.** The same exercise often appears in a lesson
   and again in its unit's consolidation file, or in both es-es and
   es-latam. Search for the question text and make the same change in
   every copy.
5. **Keep formatting.** Edit the JSON in place and keep each file's
   indentation, so the diff shows only the changed option lines.
6. **Don't apply anything you were unsure about.** Add it to
   `imports/review/hu-review-questions.txt` (Hungarian) or
   `imports/review/es-review-questions.txt` (Spanish; create it in the
   same format) and leave the exercise unchanged.

## Order and stop points

1. Spanish (es-es, es-latam) and Hungarian A1, A2, B1: 126 exercises.
   **Stop and report.**
2. Hungarian B2 (90), then C1 (167), only after the go-ahead.

Commit per course and level, e.g.

    fix(hu/b1): remove the " / " give-away from 22 choice exercises (ROADMAP 126)

The body says how many used fix 1 and how many fix 2, lists the ids of
any exercise where the wrong options changed, and how many questions
were logged.

## Checks before each commit

    python imports/review/check-slash-giveaway.py <course> <level>
    python scripts/validate-content.py --changed

The first must report `total: 0` for what you just did. The second must
pass.

## The report at each stop

Exercises changed per course and level, fix 1 vs fix 2 counts, every id
where a wrong option changed, and the questions logged. The reviewer
diffs every changed exercise, so report exactly what you did.

---

## Review of stop 1 (2026-10-04): go ahead with Hungarian B2 and C1

All 126 exercises were read. Good work: every shortened answer still
answers its question, the copies match, and nothing broke. One change by
the reviewer: *recorrer* is now "to travel around" (closer than "to
explore").

Two notes for B2 and C1:

- **Report fix 2 when you use it.** `b1-centrosur-01.ex07`,
  `b1-literatura-02.ex07` and `b1-mediterraneo-02.ex07` used fix 2 (the
  question itself names two things, so the wrong options became two-part
  too). That was the right choice, but the commits said "0 fix 2, no wrong
  options changed". Count it and list the ids.
- **C1 is different.** Most C1 hits are "Melyik kifejezés …" items whose
  correct option stacks two Hungarian phrases
  (*kötelessége szavatolni / nem foszthatja meg*). Keep the phrase that
  best fits the question's wording. Check that it alone still answers it
  (*a legkategorikusabban*, *a legpontosabban*), and that it isn't
  noticeably longer or more elevated than the wrong options. If it is,
  that is a give-away too, so log it.

Do B2 (90), commit, then C1 (167), commit, and stop with the same report.

---

## Review of stop 2 (2026-10-04): done

All 257 B2 and C1 exercises were read and accepted, and the check reports
`total: 0` for every course. The fix-1/fix-2 counts were right this time.
Ten small changes by the reviewer:

- Three C1 consolidation questions asked "Milyen kifejezésekkel" (plural)
  over an answer that is now one phrase. They now say "kifejezéssel".
  When fix 1 leaves one phrase, check that the question doesn't still ask
  for several.
- Four essay-closing items kept the stiffer half (*Végső konklúzióként*,
  *Konklúzióként levonható*). They now keep the natural one
  (*Mindent összegezve* / *összevetve*).
- `c1-egeszsegugy-05-check-8`: the kept phrase was lower-case while its
  distractors are capitalised. It is now capitalised.
- Two B2 glosses were changed: *mulasztás* is now "omission" (not
  "negligence"), and *élcelődik* is now "to banter" (not "to tease
  sardonically").

ROADMAP item 126 is closed (ACHIEVED.md).
