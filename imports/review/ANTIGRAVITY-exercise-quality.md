# Task: exercise quality pass (ROADMAP 117)

Two parts, done in this order:

- **Part A: Spanish B1.** Rewrite 726 give-away wrong options in 502
  listed exercises. Mechanical scope, about one session.
- **Part B: Hungarian, all levels.** Review every Hungarian exercise for
  wrong or unnatural Hungarian, answers that don't fit, two right answers
  and give-away options. Large (about 17,700 exercises in 1,355 files),
  done over several sessions, with a stop after A1 for review.

Quality matters more than speed. Take the time to read each exercise in
context. When you are not sure, don't change it: log it (see Part B).

Repository: this one (Parlour). Commit straight to `master`. Nobody else
edits exercise files while this runs.

## Rules for both parts

1. **Exactly one right answer.** Every choice exercise must have exactly
   one acceptable option, the marked one. Before saving a new wrong
   option, ask: would a teacher accept it as an answer to this prompt? If
   possibly yes, choose a different error. ~100 exercises with two right
   answers were just removed from A1-A2; don't add new ones.
2. **Wrong options are near misses.** A wrong option should look plausible
   and be wrong because of the point the exercise teaches (its `teaches`
   tags say which): wrong mood, wrong tense where context allows only one,
   wrong case ending, wrong conjugation, wrong word order, wrong connector.
   No give-aways: no time word that clashes with the tense, no absurd,
   rude or off-topic lines, no "Nem tudom." / "No sé." (they answer
   anything). Exception: at A1, a harmless off-topic line is acceptable
   when a near miss would be too subtle for a beginner, as long as it
   isn't a sensible reply.
3. **Same shape.** Similar length, structure and register as the correct
   option.
4. **Keep conventions.** If options carry an English gloss in square
   brackets, a new option gets one too, translating literally including
   its error (`Es necesario que reducimos los residuos. [It is necessary that we reduce waste.]`).
5. **Don't change structure.** Never change `id`, `teaches`, `category`,
   `stage` or `type`; don't add, remove or reorder exercises or options;
   don't change which option is marked correct unless the marked answer
   is itself wrong (then fix it and say so in the commit message).
6. **Keep formatting.** Exercise files are JSON with non-ASCII written
   as-is; most use 2-space indentation, some 4. Edit in place and keep
   each file's formatting so the diff shows only changed lines.
7. **Copies stay identical.** The same exercise often appears twice: in
   es-es and es-latam (Part A), or in a lesson and again in its unit's
   consolidation file (both parts). Search for the prompt text and make
   the same change in every copy.

Before every commit:

    python scripts/validate-content.py --changed

must pass with no failures.

---

## Part A: Spanish B1 give-away options

### The problem

    ¿Qué harías si la solución no funcionara?
    * Buscaría una alternativa.
    - Busqué una alternativa mañana.      ← past + "tomorrow": obviously wrong
    - Buscaré una alternativa ayer.       ← future + "yesterday": obviously wrong

The exercise is meant to test the conditional but only tests whether
"ayer" and "mañana" are words.

### Work list

`imports/review/es-b1-giveaways.jsonl`, one exercise per line:

    {"id", "courses", "files": [...], "type", "question" (dialogue lines joined with " / "),
     "options", "correct", "teaches", "giveaway_options": [indexes to rewrite]}

Rewrite exactly the options at `giveaway_options`, in every file listed.
Leave the other options alone. Keep es-latam free of *vosotros* forms.

Careful with tense swaps: imperfect vs preterite, perfect vs preterite,
future vs *ir a* + infinitive, and indicative vs subjunctive after
*creer* / *pensar* are often **both** acceptable. Only use one when the
context rules the other out.

### Examples

    teaches: preterito-indefinido
    Marcos: ¿Por qué llegaste tarde al trabajo? / Tú: _____
    * Perdí el autobús y tuve que caminar veinte minutos.
    - Había perdido el autobús mañana.                         (before)
    - Perdía el autobús y tenía que caminar veinte minutos.    (after: imperfect for one event)

    teaches: hypothetical-structures
    A: ¿Qué harías si la solución no funcionara? / B: _____
    * Buscaría una alternativa. [I would look for an alternative.]
    - Busqué una alternativa mañana. [...]                     (before)
    - Busque una alternativa. [I look (subjunctive) for an alternative.]   (after)

    teaches: subjuntivo (necessity)
    A: ¿Qué debería hacer el ayuntamiento? / B: _____
    * Es necesario que reduzca el tráfico y mejore el transporte público.
    - Es necesario que reducirá el tráfico … ayer.             (before)
    - Es necesario que reduce el tráfico y mejora el transporte público.   (after)

A fix to **avoid**:

    teaches: imperfecto-past-description
    A: ¿Era diferente antes? / B: _____
    * Sí, antes era más tranquilo, aunque ahora hay más servicios.
    - Sí, antes fue más tranquilo, aunque ahora hay más servicios.   ✗ arguably acceptable
    - Sí, antes es más tranquilo, aunque ahora había más servicios.  ✓ clearly wrong

### Check and commit

    python imports/review/check-es-b1-giveaways.py

must report `giveaways remaining: 0` and `problems: 0`. A few options may
legitimately need *ayer* or *mañana* (the prompt is about yesterday);
leave those and list their ids in the commit message. One commit:

    fix(es/b1): near-miss distractors instead of time-word give-aways (ROADMAP 117)

with a body saying how many options were rewritten and any ids skipped.

---

## Part B: Hungarian exercises, all levels

### Goal

Every Hungarian exercise reads as if a careful native-speaking teacher
wrote it, has exactly one right answer, and tests what it says it tests.
These exercises were machine-generated and contain errors a native speaker
spots at once. Find and fix them.

### How to work

- Go level by level, **A1, A2, B1, B2, C1**, in the order of
  `imports/review/hu-review-progress.md`. Tick a file there (`[x]`) when
  every exercise in it is reviewed and fixed.
- For each exercise file `content/hu/exercises/<level>/<name>-ex.json`,
  first read its lesson `content/hu/lessons/<level>/<name>.json` and the
  grammar files it references, so you know what is being taught and what
  vocabulary the learner has. Then read the exercises **in order**: the
  learner meets them in sequence.
- Review **all exercise types**, not only multiple choice: fill-blank
  (`sentence`, `answer`, the hint in brackets), structured-writing
  (`prompt`, `answer`), sentence-builder (`solution`, `english`), matching
  pairs, dialogue-complete, listening-choice. Substitution drills are not
  graded but must still be correct Hungarian.
- Commit after every block of about 25 files:

      fix(hu/a1): review a1-01 … a1-12 exercises (ROADMAP 117)

  with a body listing how many exercises changed and the main kinds of
  fix. Run the checks below before each commit.
- **Stop after A1** and report (files done, exercises changed, the most
  common problems, how many questions were logged). Don't start A2 until
  told to continue.

### What to look for

Real examples, all found and fixed in this repository:

**H1. Wrong Hungarian in the prompt or the marked answer.**
- Case endings: nouns that take *-n / -ra / -ról* used with
  *-ban / -ba / -ból*. *a postára / a postán* (not *postába*),
  *az állomásra / állomáson*, *az egyetemre / egyetemen*,
  *a munkahelyre*, *a helyen* (*a helyben* means "locally"), *Budapesten*,
  *a téren*. Also *-hoz/-hez/-höz* vowel harmony.
- Missing pieces: *Mit csinálsz a szabadidődben?* (not *szabadidőben*);
  *szeretném felpróbálni* (not *próbálni*); *Szeretnétek moziba menni
  szombaton?* (not *Szeretnétek együtt programot?*); *Balra van.* (not
  *Bal van.*); *Lehet nyolckor találkozni?* (not *Lehet nyolc óra?*).
- Definite vs indefinite conjugation, word order and focus (the stressed
  element goes right before the verb), agreement, and the answer to
  *Mennyibe kerül?* is *Kétezer forintba.* or *Kétezer forint.*

**H2. The answer doesn't answer the question.**
- *Van jegyünk?* — *Igen. A megálló ott van.* → *Igen, van két jegyünk.*
- *A múzeum és a mozi is itt van?* — *Igen. A könyvtár a téren van.*
- *Hány szoba van a lakásban?* answered with a list of rooms, no number.

**H3. Two acceptable answers.**
- *Nem tudom.* as a wrong option: it answers any question.
- Synonyms: *heti / hetente* for "weekly", *kedvezmény / akció* for
  "discount", *hideg / hűvös* for "cold".
- Yes and no both sensible: *Ő egy nő?* with no referent; *Dolgoztál
  tegnap?* — *Nem, holnap dolgozom.* is a perfectly good reply → make the
  wrong option contradict itself: *Igen, holnap dolgozom.*
- Focus: "emphasis on WHERE" with *Otthon vagyok ma.* vs *Ma otthon
  vagyok.*: in both, *otthon* sits before the verb, so both stress it.
- A question with nothing to match: "Which question fits the meaning?"
  with no meaning given.

**H4. Give-away wrong options.** Time-word clashes (*tegnap* with future,
*holnap* with past), absurd or rude lines (*Fuss ki az épületből és ne
gyere vissza soha többé.*, *Az exportőrök nem használnak pénzt, csak
aranyrudakat.*). Replace with near misses on the taught point.

**H5. Repeated question.** The same question line in two back-to-back
steps of a lesson (*Hol laksz?* asked by Károly, then by Meg). Vary it:
address by name (*És te, Károly, hol laksz?*) or give it its own context.
Consolidation drills that repeat one question with different answers on
purpose (*Hová mész?* → mozi / étterem / gyógyszertár) are fine.

**H6. Lines that depend on another step.** *És a taxi?* or *És az
iskola?* as the whole prompt. Each exercise must make sense on its own.

**H7. English that doesn't match the Hungarian.** Questions, hints and
glosses must translate the Hungarian correctly (*"in the place"* for
*a helyben* was wrong), and an English question must not allow two
answers.

### Don't touch

- `dialogue-complete` exercises in `a1-121` … `a1-150` (lessons and
  consolidations): a native speaker reviewed them on 2026-10-01. Other
  exercise types in those files are in scope.
- Anything outside `content/hu/exercises/` (lessons, grammar, stories,
  dictionaries), even if you spot a problem there; note it in the
  questions file instead.

### When you are not sure

Don't edit. Add the exercise to `imports/review/hu-review-questions.txt`
in the format described at the top of that file: what looks wrong, the
current version and your proposed version. A native speaker answers these
later. Fewer, certain fixes are better than many risky ones.

### Checks before each commit

    python imports/review/check-hu-exercises.py a1      (the level you are on)
    python scripts/validate-content.py --changed

The first must report `errors: 0`. Its `suspects` (give-aways, *Nem
tudom.*, wrong case endings) must each be fixed, or left on purpose and
named in the commit message. The script only catches mechanical
patterns; most of the review is reading.

### Review

After each level a reviewer reads a random sample of the changed
exercises. Problems found there come back to you before the next level
starts.
