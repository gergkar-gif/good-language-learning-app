# Task: finish Spanish A1 unit 1 `greetings-introductions` in both courses (ROADMAP 153)

The first Spanish unit of the gate-1 pass, and a trial: Claude reviews your
result against the HU A2 units before more Spanish units are handed out.
Note the time you start and finish; put both in the commit body.

The unit: lessons `a1-01-01` … `a1-01-05` and `a1-01-consolidation`, story
`content/es-es/stories/original/a1/a1-01.json` (on lesson `a1-01-05`). It is
the course's first unit, so nothing is known before it except what its own
lessons teach.

es-es and es-latam share almost every file of this unit byte for byte. You
work on **es-es**, write every change as a fix in JSON, and copy the fixes to
es-latam with a script. Only `a1-01-01-sounds-gr.json` and the consolidation
lesson's grammar and vocabulary differ between the courses; read those in
es-latam yourself.

## Read first

1. `docs/unit-agent-rules.md`: your rulebook. Sections 1–5, **6a** and **6c**
   (skip 6b, Hungarian). Open other docs only to settle a point it doesn't cover.
2. `AGENTS.md` § "Exercise metadata" (tags) and § "Latin American Spanish".
3. The scripts' usage lines at the top of `scripts/apply_replacements.py`
   (fix format), `scripts/check_fixes.py`, `scripts/mirror_fixes.py`,
   `scripts/add_challenges.py`.

## What to do

Work in `C:/dev/parlour` on an up-to-date master (`git pull --rebase origin master`).

1. **Run the checks and render the unit:**

       python scripts/check-content.py es-es a1 greetings-introductions
       node scripts/render_lesson.js es-es a1-01-01 a1-01-02 a1-01-03 a1-01-04 a1-01-05 a1-01-consolidation
       node scripts/audit-reader-coverage.js es-es --story a1-01 --top 0

   check-content reports 4 errors (length give-aways) and 13 suspects today.

2. **Read everything as rendered:** every exercise, both grammar screens of
   each lesson, the vocabulary lists, goals, checklists, speaking steps and
   the story. Check rulebook § 1–4 and every item of § 6a and § 6c. A learner
   knows only English. Things to watch in this unit:
   - one right answer per item (greetings have near-synonyms: *buenas
     tardes* / *buenas noches*, *hasta luego* / *hasta mañana*, *¿Cómo
     estás?* / *¿Qué tal?*; `answers` lists every correct alternative);
   - each wrong option fails in exactly one way, on the point the item tests;
   - `tú` / `usted` and *ser* forms used before the screen that teaches them;
   - no English inside a Spanish line (`english-in-target` is an error);
   - glosses that read right to an English speaker.

3. **Write every fix as JSON** in `imports/review/es-a1-batch-01/fixes-greetings-introductions.json`,
   in the format at the top of `scripts/apply_replacements.py`. Fix **every**
   check-content error (a length give-away: make the wrong options as long as
   the right one, or shorten the right one, with met words and one fault
   each), and every suspect that is real; leave a suspect only with a reason.
   On each fix: the exercise `id`, `"kind": "target"` when it changes Spanish
   text, `"sure": false` when unsure, `"why"` in a few words. Quote `old`
   exactly from the file. A fix that only holds in Spain (*vosotros*, *zumo*)
   gets `"variant": "es-es"`.

4. **Check, apply and mirror:**

       python scripts/check_fixes.py es-es a1 greetings-introductions imports/review/es-a1-batch-01/fixes-greetings-introductions.json
       python scripts/apply_replacements.py imports/review/es-a1-batch-01/fixes-greetings-introductions.auto.json
       python scripts/apply_replacements.py imports/review/es-a1-batch-01/fixes-greetings-introductions.review.json

   Fix or drop anything `check_fixes.py` rejects, and say which (a fixed
   one goes through `check_fixes.py` again). Then copy the two applied lists
   to es-latam; fixes marked `"variant": "es-es"` are left out by the script:

       python scripts/mirror_fixes.py imports/review/es-a1-batch-01/fixes-greetings-introductions.auto.json es-es es-latam imports/review/es-a1-batch-01/latam.auto.json
       python scripts/mirror_fixes.py imports/review/es-a1-batch-01/fixes-greetings-introductions.review.json es-es es-latam imports/review/es-a1-batch-01/latam.review.json
       python scripts/apply_replacements.py imports/review/es-a1-batch-01/latam.auto.json
       python scripts/apply_replacements.py imports/review/es-a1-batch-01/latam.review.json

   Read both `latam.*.unmatched.json` files: write the es-latam wording for
   each item by hand (no *vosotros*; *ustedes*), and read the three
   es-latam-only files above.

5. **Words in no vocabulary list** (`unmet-word` "is in no vocabulary list"):
   add each to the vocabulary list of the first lesson that uses it, with an
   English gloss, in both courses (user's rule, 2026-10-16).

6. **Challenges: one per lesson, consolidation included (six).** Write them to
   `imports/review/es-a1-batch-01/challenges-greetings-introductions.json`, a
   JSON object keyed by lesson stem, each entry with exactly these fields
   (the shape of `content/hu/curriculum/challenges.json`):
   `tier` "tier1", `level` "A1", `title` "Communicative Challenge: …",
   `scenario`, `prompt`, `cues`, `target`, `english`, `canDo`. Rulebook § 4:
   the story's people (Carlos and Meg), nobody answers for the learner, cues
   say what to include and never the words, the target is 1–3 sentences of
   words met by that lesson, `canDo` is the lesson's first checklist line
   copied exactly (after your own checklist fixes). es-latam gets the same
   six, with only course variants changed.

       python scripts/add_challenges.py es-es a1 imports/review/es-a1-batch-01/challenges-greetings-introductions.json
       python scripts/add_challenges.py es-latam a1 imports/review/es-a1-batch-01/challenges-greetings-introductions.json

   (Write a separate es-latam file only if a target needs a variant.)

7. **Check again, both courses, until clean:**

       python scripts/check-content.py es-es a1 greetings-introductions
       python scripts/check-content.py es-latam a1 greetings-introductions
       python scripts/validate-content.py --changed
       python scripts/validate-content.py --warnings

   0 errors in both courses. Every remaining suspect gets a line in
   `imports/review/es-a1-batch-01/accept.json`:
   `["<check>:<exercise id>:<why it stays>", …]`. No new A1 lines in
   `--warnings`. Render the unit again and read what you changed.

8. **Lock the tags** if you changed any `teaches` or `distractor_skills`:

       python scripts/lock_tags.py es-es a1/greetings-introductions --update --reason "unit read and fixed (153)"
       python scripts/lock_tags.py es-latam a1/greetings-introductions --update --reason "unit read and fixed (153)"

## Don't

- **Don't freeze** the unit; Claude freezes it after review.
- Don't edit `skills/*.json` or any generated index, and don't add, rename
  or retag a skill outside the rules. If no skill fits, report it.
- Don't touch other units, the engine or the scripts. If a script refuses
  or a check looks wrong, stop and report its output.
- Never bypass git hooks (`--no-verify`, `core.hooksPath`).
- Don't "fix" a correct Spanish line you are unsure about: mark it
  `"sure": false` and say why.

## Report and commit

Write `imports/review/es-a1-batch-01/report-greetings-introductions.md`:

1. Found by reading (id, problem quoting the text, fix).
2. Metadata (tags changed and why).
3. Goals, checklists, challenges.
4. Doubtful: every Spanish line you are unsure of.
5. Not fixed, and why (including every accepted suspect).
6. Numbers: errors and suspects before and after, in each course; fixes
   applied in es-es, mirrored, written by hand for es-latam; words added to
   vocabulary lists; start and finish time.

Commit the unit and the folder in one commit,
`content(es): read and fix a1/greetings-introductions in es-es and es-latam (153)`,
with the start and finish times in the body. `git pull --rebase origin master`,
push, then stop and report.
