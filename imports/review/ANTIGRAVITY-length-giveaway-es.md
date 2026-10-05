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

### Block 1 (es-both B1), reviewed 2026-10-05

Commit `c7a78634`. The mechanics are right: all 127 decisions are applied
exactly as written, in every listed copy; the copies are identical;
nothing outside the worksheet changed; no block 1 id is still flagged; the
validator passes; the counts in the report (21 shorten / 106 match / 0 log)
are correct. Most rewrites are good. Rewriting grammar distractors as
"one half of the correct answer" (feature A alone, feature B alone) works
well, so keep doing it.

**Fix these four first, in a separate commit before you start block 2**
(edit the worksheet entry as well, so it still matches the files):

1. `b1-39-01.ex10`: *Me quedé rojo de vergüenza …* is correct Spanish
   (*quedarse rojo* is common), so it is now a second right answer.
   Replace it with a change verb that really is wrong here, e.g.
   *Me convertí en rojo de vergüenza porque no sabía la respuesta.*
   Lesson: when a distractor tests a word choice, check that the wrong
   word really is wrong in the full sentence you wrote, not only in the
   short original.
2. `b1-28-05.ex21`: the shortened *Se permite el acceso en casos de
   emergencia.* dropped the fact the text gives (access **by car**).
   Next to *Está prohibido caminar por la plaza*, it now suggests that
   any access is restricted. Use
   *Se permite entrar en coche en una emergencia.* Rule 1: shortening
   must keep the fact the question asks about.
3. `b1-39-05.ex10`: the correct option ends *hotel boutique*, but both
   wrong ones end *hotel para turistas*, so the correct one is the odd one
   out. Make all three identical apart from the verb:
   *Se puso en un hermoso hotel boutique.* / *Se hizo en un hermoso hotel
   boutique.*
4. `b1-04-05.ex16` ("most complete recommendation"): the new wrong option
   *Revisa el plan inmediatamente en la oficina antes de tomar una
   decisión* is complete enough to argue for. Keep the wrong options as
   long as they are, but make them plainly less complete: no purpose and no
   reason, only time and place details, e.g. *Revisa el plan esta tarde en
   la oficina con tus compañeros.*

**For the next blocks:**

- In `shorten`, aim for about 1.3× or less. A few block 1 results stay
  near 1.5× (`b1-14-05.ex22`, `b1-40-03.ex07`) with distractors of 20
  characters, so the correct option is still the longest by a visible
  margin. Acceptable here, but don't stop at 1.5×.
- In dialogue items, read the line *before* the blank and check that
  each new wrong reply really fails to answer it (`b1-33-05.ex13` does
  this well: *Dijo que …* doesn't answer *¿Qué preguntó…?*).
- Absolutes in wrong options are fine **when the question is about
  nuance** (`b1-34-05.ex02`: categorical vs nuanced opinion). Elsewhere
  rule 3 still applies.

Not yours to fix (outside this task, noted for the queue):
`b1-37.cons.ex05` has *hayáis* (vosotros) in the es-latam copy;
`b1-19-03.ex06` and `b1-29-05.ex02` give the answer away in the question
text itself.

### Block 2 (es-es B1), reviewed 2026-10-05

Commits `2a2f220b` (block 1 fixes) and `b2d5ff08` (block 2). The four
block 1 fixes are applied exactly. Block 2's mechanics are right again:
all 159 decisions applied as written, in every listed copy (lesson and
consolidation copies have identical options), nothing else changed, no
block 2 id still flagged, counts correct (141 shorten / 18 match / 0 log).
Most shortenings are clean.

**Fix these first, in a separate commit before block 3** (worksheet too):

1. `b1-ciudadesautonomas-02.ex02` (and its consolidation copy):
   **the new correct option is false.** The question asks why Melilla's
   20th-century city centre stands out; the text (and the exercise's own
   `explanation`) says: the second city in Spain for modernist and
   art déco buildings, after Barcelona. *Por su recinto amurallado
   medieval completo* is not that, and it isn't true. Use
   *Por sus numerosos edificios modernistas y art déco.* Rule 1: the
   shortened option must say the same thing as the original, only less.
   Re-read the original option before writing each `shorten`; never
   write the new one from memory of the topic.
2. `b1-documentacion-03.ex05`: the original said *el encargado del
   Registro Civil*; the new option says *el juez del Registro Civil*,
   which is no longer accurate (the Registro Civil isn't run by judges
   since 2021) and is a detail you added. Use
   *Ante el encargado del Registro Civil, el alcalde o un notario.*
   Rule 2: when shortening, only remove; don't swap in new facts.
3. `b1-sanidad-01.ex05`: *El INGESA (Sanidad)* reads oddly. Use
   *El INGESA*. The wrong options are institution names too.
4. `b1-sanidad-04.ex06`: *national organ transplant program* is close
   enough to *National Transplant Organization* to be argued for. Use a
   wrong option that is plainly a different thing, e.g.
   *national blood donation service*.

**For the next blocks:** blocks 3 and 4 are es-latam, where much of the
content is history and civics of real countries. Fact errors like item 1
are the worst outcome of this whole pass, so for every `shorten` compare
the new text with the original word by word: what did you drop, and is
anything new?

Not yours to fix (outside this task, noted for the queue):
`b1-fiestas-01.ex05` has *Los tamborradas* (should be *Las*);
`b1-gastronomia-05.ex02` names the restaurant *Can Roca* in the question,
so *Los hermanos Roca* is given away; `b1-historiaantigua-03.ex04` asks
for a port in Huelva, but none of the wrong options is in Huelva. Many
es-es civics (CCSE) items have absurd distractors (*Solo los martes y
jueves*, *En Bruselas*), which is a separate give-away for a later pass.

### Block 3 (es-latam B1), reviewed 2026-10-05

Commits `5f4748b3` (block 2 fixes) and `ead28c80` (block 3). The four
block 2 fixes are applied exactly. Block 3's mechanics are right: all 224
decisions applied as written in every copy, nothing else changed, no
block 3 id still flagged, counts correct (66 shorten / 158 match / 0 log).
No false facts this time, and the shortened history answers keep their
key point. The problems are in the new **wrong** options: several no
longer fit the question they answer.

**Fix these first, in a separate commit before block 4** (worksheet too):

1. `b1-represionpolitica-consolidation.ex12`: the two new wrong options
   are **in English** in a Spanish item (*Although civilian courts
   investigated…*, *Because state censorship was lifted…*). They give the
   answer away and don't answer *¿Por qué es importante la memoria
   histórica?* Write two Spanish *Porque …* options that give a wrong
   reason, e.g. *Porque permite cerrar los casos sin investigar a los
   responsables.* / *Porque sustituye a los tribunales en la búsqueda de
   culpables.*
2. `b1-guerrafria-consolidation.ex11`: the question asks what
   *injerencia* means; the new wrong options (*Fortalecieron el consenso
   democrático…*, *Garantizaron la independencia judicial…*) are plural
   verbs with no subject and define nothing. Use definitions that are
   wrong: *Es la neutralidad de un país frente a las dos superpotencias.*
   / *Es un acuerdo comercial entre países con el mismo sistema
   político.*
3. `b1-guerrafria-consolidation.ex12`: *¿Qué ocurrió con los conflictos
   internos?* is not a yes/no question, but one wrong option starts
   *Sí, …*, and neither wrong option is about internal conflicts. Use
   e.g. *Desaparecieron porque las superpotencias se negaron a
   intervenir.* / *Se resolvieron siempre mediante acuerdos entre los
   partidos nacionales.*
4. `b1-economiasexportacion-03.ex05`: the shortened option is broken:
   *…llegó a controlar una porción tan grande de la industria.* (*tan
   grande* without *que…*, and which industry?). Use *Un empresario
   británico que llegó a controlar gran parte de la industria del
   salitre.*
5. `b1-latamnoventa-03.ex02`: *Entró en vigor el TLCAN y el levantamiento
   en Chiapas* says the uprising "came into force". Use *Entró en vigor
   el TLCAN y estalló un levantamiento en Chiapas.*
6. `b1-conquista-consolidation.ex08`: *¿Cómo actuaron algunos pueblos?*:
   the new wrong options (*Aceptando someterse de inmediato, entregaron
   sus tierras.* / *Evitando cualquier contacto, huyeron hacia las
   montañas.*) describe things some peoples really did, so they can be
   argued for. Use options that are false for any people, e.g.
   *Esperando instrucciones de Europa, eligieron a un rey español.* /
   *Uniéndose todos en un solo imperio, expulsaron a los españoles.*
   If you can't find two clean ones, log it.
7. `b1-sociedadcolonial-02.ex03`: the shortened option lost its subject
   and most of its content (*demostraba que no descendía de judíos*).
   Use *Un documento que probaba que la persona no descendía de judíos
   ni musulmanes; se exigía para cargos públicos.*

**For block 4:**

- **Check every new wrong option against the question, not only
  against the correct option.** A wrong option must be a possible answer
  to *that* question: same language, same grammatical shape (a
  definition for *¿Qué significa…?*, a reason for *¿Por qué…?*, no
  *Sí/No* for an open question). Items 1–3 above all fail this.
- After shortening, read the new option as a sentence on its own:
  every clause complete, every *tan* / *tanto* with its *que*.
- "Some people did X" questions: a wrong option must be false for
  everyone the question could mean.
