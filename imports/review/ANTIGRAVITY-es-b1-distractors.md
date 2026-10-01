# Task: rewrite give-away wrong options in Spanish B1 choice exercises

Repository: this one (Parlour). Branch: commit straight to `master`.
Scope: **only** the exercises listed in `imports/review/es-b1-giveaways.jsonl`
(502 exercises, 726 wrong options). Do not edit any other file or exercise.

## The problem

In these exercises the learner can rule out a wrong option without knowing
the grammar, because it contains a time word that clashes with its tense:

    ¿Qué harías si la solución no funcionara?
    * Buscaría una alternativa.
    - Busqué una alternativa mañana.      ← "past + tomorrow": obviously wrong
    - Buscaré una alternativa ayer.       ← "future + yesterday": obviously wrong

The exercise is meant to test the conditional, but it only tests whether
"ayer" and "mañana" are words. The fix: replace each give-away option with a
**near miss**, an option that looks plausible and is wrong *only* because
of the grammar point the exercise teaches (its `teaches` tags tell you
which).

## The work list

`imports/review/es-b1-giveaways.jsonl`, one exercise per line:

    {"id": ..., "courses": ["es-es","es-latam"], "files": [...two paths...],
     "type": "dialogue-complete" | "multiple-choice",
     "question": the prompt as text (dialogue lines joined with " / "),
     "options": [...], "correct": index of the right answer,
     "teaches": [...], "giveaway_options": [indexes to rewrite]}

Rewrite exactly the options at `giveaway_options`. Leave every other option
alone, especially the correct one.

## Rules for a new wrong option

1. **Exactly one right answer.** The new option must be wrong in every
   reasonable reading. Check: would a Spanish teacher accept it as an answer
   to this prompt? If possibly yes, choose a different error. This is the
   most important rule; we just removed ~100 "two right answers" exercises
   from A1-A2 and must not add new ones.
   - Careful with tense swaps: imperfect vs preterite, perfect vs preterite,
     future vs *ir a* + infinitive, and indicative vs subjunctive after
     verbs like *creer* / *pensar* are often **both** acceptable. Only use a
     tense swap when the context rules the other tense out.
2. **Wrong because of the target grammar.** Prefer the error a B1 learner
   actually makes for that point: indicative where the subjunctive is
   required (*Es necesario que reduce…*), the wrong past tense where the
   context leaves only one possible (see the first example below), a wrong
   conditional or *si*-clause form
   (*Si tendría…*), a wrong agreement, a wrong preposition or connector.
3. **No give-aways.** No time word that clashes with the tense, no
   nonsense (*porque cultura*), no off-topic sentence. The option should
   look like something a learner might pick.
4. **Same shape.** Similar length and structure to the correct option and
   to the other options; same register. Don't make it longer or shorter
   than the correct option by much.
5. **Keep the English gloss convention.** If the options carry an English
   gloss in square brackets, the new option needs one too, translating the
   Spanish literally including its error, like the existing ones do:
   `Es necesario que reducimos los residuos. [It is necessary that we reduce waste.]`
6. **Don't touch anything else**: not the prompt, `correct`, `teaches`,
   `category`, `id`, the order of options, or any other field.
7. **Both courses.** Every exercise with two `files` exists in es-es and
   es-latam; make the identical change in both. The 10 exercises with one
   file are course-specific. Keep es-latam free of *vosotros* forms.

## Examples

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

## Files and formatting

Exercise files are JSON with non-ASCII characters written as-is
(`ensure_ascii=False`); most use 2-space indentation, some 4. Edit in place
and keep each file's existing formatting, so the diff shows only the
changed option lines. Don't reformat files.

## Acceptance checks (run before committing)

    python imports/review/check-es-b1-giveaways.py
    python scripts/validate-content.py --changed

The first must report `giveaways remaining: 0` and `problems: 0`; it also
checks that es-es and es-latam copies still match. (A few options may
legitimately need *ayer* or *mañana*, for example when the prompt is about
yesterday. Leave those, and list their ids in the commit message.) The
second must pass with no failures.

## Commit

One commit, message:

    fix(es/b1): near-miss distractors instead of time-word give-aways (ROADMAP 117)

with a short body: how many options were rewritten, and any ids skipped
and why. Don't edit ROADMAP.md or ACHIEVED.md; that is done in review.

A reviewer will read a random sample of the rewritten options against
rule 1 before the work is accepted.
