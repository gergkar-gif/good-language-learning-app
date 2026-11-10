# Audit: Spanish placement diagnostic (es-es and es-latam), 2026-11-10

Scope: `content/es-es/tests/diagnostic-test.json`, `content/es-latam/tests/diagnostic-test.json`
(3 tiers, 10 core items + 2 reading items each; 30 core items shared, 6 reading
passages differ) and `engine/diagnostic.js`, plus what consumes its result.

Not in scope: the end-of-level tests (`a1-test.json` … `b2-test.json`,
`engine/leveltest.js`), the Hungarian diagnostic, visual design.

Method: every item read; every `teaches` slug looked up in `skills/es.json`;
the engine read in full; four scenarios driven through the real app in
Chromium (`scripts/dev-server.py`); three present-day claims checked on the web.
Nothing was changed in content or engine.

"Confirmed" below means reproduced in the browser or read directly off the
files. "Judgement" means a language or test-design call a native reviewer could
dispute.

## A. Placement logic (engine)

**A1. es-es places strong learners into an empty level. Confirmed.**
`_determinePlacement` returns the level after the highest cleared tier, taken
from `LEVEL_ORDER`, without checking the course has it. es-es has B2 with 0
units. All correct in es-es: "Placed into Level B2", button "Accept Placement &
Jump to Level B2", after which 810 lessons (all of A1, A2, B1) are marked
complete and the Lessons page shows B2 "0 / 0". The same happens with 9/12 on
the B1 tier. es-latam has B2 content (72 units), so there the jump lands
somewhere; it has no C1, which the diagnostic can't reach anyway.

**A2. A 75% tier counts as cleared. Confirmed.** A tier at 70–84% is
"borderline" and placement moves one level up. With 12 items per tier the real
marks are: pass 11/12 or 12/12, borderline 9/12 or 10/12. So 9/12 on A1 gives
"Placed into Level A2", and the primary button marks all 156 A1 lessons
complete. The debrief text calls 9/12 (75%) "just under the 85% mark". The
preface says 70% "lets you choose to start one level higher", but the debrief
presents the higher level as the placement and the lower one as a secondary
button.

**A3. "85%" is really 92%. Confirmed.** The reading items were added after the
threshold was set for 10 items (9/10). With 12 items, 10/12 = 83.3% fails, so
one mistake is allowed, not one in ten. `tests/test-diagnostic.js` still asserts
"9/10 passes" against its own copy of the scoring function with a 10-item tier,
so it passes while describing a rule the engine no longer applies.

**A4. Jumping to B1 or B2 marks elective tracks complete. Confirmed.**
`markLevelComplete('B1')` completes all 76 B1 units, including the 36
`cultura`/`latam` units and, in es-es, whatever CCSE scaffolding sits in B1, and
credits their vocabulary (`creditTestedOutWords`). A 12-item grammar and reading
screener is no evidence for any of that.

**A5. The tests don't test the engine. Confirmed.** `tests/test-diagnostic.js`
re-implements `evaluateTier`; `tests/drills/test-diagnostic-test.js` does the
same for placement. Neither loads `engine/diagnostic.js`, so A1–A3 pass CI.
`scripts/validate-content.py` skips `diagnostic-test.json` by name and
`check-content.py` does not read `tests/`, so no check covers the items' tags or
content either.

**A6. Reading score shares a key with the level tests. Confirmed in code.**
Both write `readingScores[level]` and keep the best percentage. A 2/2 from the
diagnostic (100%) blocks a later 7/8 from the level test from being stored.
Nothing reads the key today, so no visible effect yet.

**A7. Enter on a choice question submits the old answer. Confirmed.** With an
option selected, moving keyboard focus to another option and pressing Enter
advances with the first answer instead of selecting the focused one. (Space
selects correctly.) After a mouse click, Enter does nothing, because focus is
lost when the card re-renders.

**A8. Smaller engine points.**
- "← Quit" discards all answers with no confirmation and no resume.
- A retake sends the `diag:` evidence to `Recycle.credit` again.
- "Start from Level A1 Anyway" saves `level: <placed level>`; nothing reads
  `level` or `jumpedAhead` today, so harmless but wrong.
- Preface says "5 to 7 minutes"; a full run is 36 items and three passages.
- Copy contradicts itself: preface "a screener, not a certificate"; debrief
  "Full CEFR certifications … verified via the official Level Tests";
  transition screen "B1 Foundations Mastered!".
- Accents are stripped before comparison, so the unaccented `altAnswers`
  (`esten`, `viajariamos`, `esteis`) are dead data, and so are the six
  `altAnswers` that repeat `answer`.

## B. What each tier measures

**B1. Half of the B1 tier is A2 material by the course's own registry.**
`teaches` level per `skills/es.json`:

| Item | Slug | Registry level |
|---|---|---|
| a2-05 | `gustar` | A1 |
| a2-06 | `tener-que` | A1 |
| b1-01 | `subjuntivo-deseos` | A2 |
| b1-02 | `cuando-subjuntivo` | A2 |
| b1-03 | `polite-softening` | A2 |
| b1-04 | `ordering-markers` (mis-tag, see C) | A2 |
| b1-09 | `subjunctive-value-judgments` | A2 |

After fixing the two mis-tags (C), 5 of 10 B1 items are still A2 skills
(b1-05 becomes `por-vs-para`, A2). A learner who finished A2 can score 9/12 on
"B1" and be placed in B2.

**B2. The B1 tier is a present-subjunctive test.** Six of ten items
(b1-01, 02, 06, 07, 08, 09) have the present subjunctive as the answer. Nothing
on the pluperfect, future, relative clauses, reported speech, passive/`se`, or
the preterite/imperfect contrast in narration. A2 has three preterite items
(two with the same slug) and no present perfect, reflexives or future.

**B3. Reading adds two items at a 33% guess rate each**, and "No se menciona" is
never the right answer in any of the six true/false items in either course.

## C. Item findings (shared by both courses unless marked)

Wrong or disputable keys:

1. **a1-10** `pero _____ tarde va a hacer sol` → `esta`. "por la" is at least
   as natural, the hint asks for "word or phrase", and it is marked wrong.
   Confirmed in the browser.
2. **b1-08** `No creo que Juan (decir) _____ la verdad sobre lo que ocurrió ayer`
   → `diga`. With "lo que ocurrió ayer" the stronger learner writes "haya dicho"
   or "dijera"; both are marked wrong. Confirmed in the browser. The item
   punishes exactly the learners the tier should pass.
3. **b1-09** accepts `estéis` for "todos los participantes (estar)". Third
   person plural subject; and es-latam does not teach *vosotros* at all.
   Confirmed in the browser.
4. **a1-08** accepts "yo tengo", which gives "pero yo solo yo tengo".
   Confirmed. The blank is also open: "alquilo", "quiero" fit and are wrong.
5. **a2-03** `Sí, _____ llamé` → `la`, with `le` as a distractor. The DPD entry
   *llamar* describes the transitive use as general and says intransitive use
   with *le* also occurs, including outside leísta areas (paraphrase of
   rae.es/dpd/llamar, read through a search summary, not the page itself). A
   distractor the academy does not condemn is a bad distractor.
6. **a2-01** `porque _____ un fuerte dolor de cabeza` → `tenía`, with `tuvo`
   as a distractor. *Judgement:* "tuvo" is grammatical here.
7. **b1-03** `¿_____ tan amable de cerrar la ventana?` → `Sería`, with `Es` as
   a distractor. *Judgement:* "¿Es tan amable de…?" is used.

Give-aways and weak distractors:

8. **b1-06** the English-free "Situación" line already contains the tested
   structure: "tú dudas que eso suceda".
9. **a2-04** `búscala` is the only imperative among the options ("la busca",
   "no buscas", "buscando").
10. **b1-04** `sin embargo` is the only option that fits "; ___," (the others
    are "porque", "para que", "a condición de").
11. Reading: es-es a2-r01 correct option "Apenas veinte minutos" is lifted
    word for word from the passage and is the only modified option; es-es
    b1-r01 and es-latam a2-r01, b1-r01 likewise copy the passage, against
    distractors that are absurd ("Que cierren todos los hoteles", "Únicamente en
    el aeropuerto internacional").

Mis-tags (`teaches`):

12. **b1-04** `ordering-markers` → the registry has
    `contrast-concession-connectors` (B1) for *sin embargo*.
13. **b1-05** `subjuntivo-de-finalidad-para-que` → the item tests *para* for a
    deadline; the registry skill is `por-vs-para` (A2).
14. **a2-08** `fuimos` tagged `preterite-irregular-stems`; *ir/ser* is
    suppletive, not a stem change. No dedicated slug found; leave or decide.
15. All 30 items carry `teaches` as an array and no `category`, unlike every
    other exercise. The learner model reads the array, so this works; it is
    simply outside the metadata rules and outside the validator.

Course fit:

16. **a2-03** (es-es): "¿Has llamado…? — Sí, la llamé esta mañana" answers a
    perfect with a preterite plus "esta mañana", which the es-es course teaches
    as a present-perfect marker. In es-latam the question "¿Has llamado…?" is
    the odd half.
17. **es-latam a1-06**: "camarero" twice (prompt and sentence); the course
    word is "mesero" (`scripts/course_variants.py`).
18. **es-latam a1-02**: "auto"; the course word is "carro".
19. **es-latam a2-09**: "los deberes de la escuela"; *Judgement:* "la tarea"
    is the usual Latin American word (not in the variants table).
20. **es-latam a2 reading**: "la municipalidad de Medellín" and "paradas de
    metro". *Judgement:* Colombia says "alcaldía" and "estaciones".

Language slips in passages:

21. **es-es b1 reading**: "el sector turístico sostiene … aunque reconocen":
    singular subject, plural verb.
22. **es-es a2 reading**: "los trenes pasan" about a tram line.

Facts:

23. **es-latam a1 reading**: Parque Metropolitano "abre todos los días de ocho
    de la mañana a siete de la tarde". ChileAtiende lists 6:00 to 20:30 (search
    summary; page not opened). r01 keys on the opening hour.
24. **es-es a1 reading** (Prado): hours and the free slot match what the search
    returned; the 15 € general ticket is what most sources give, two give 17 €
    or 18 €. Not checked on museodelprado.es.
25. **es-es a2 reading** (Valencia tram) and **es-latam a2 reading** (Medellín
    bikes) present invented news about real places as fact. Medellín has had a
    public bike system for years.

## D. What this audit does not cover

- No native-speaker review; items marked *Judgement* need one.
- No check of whether every word in the items and passages has been taught by
  the tier's level.
- No data: there are no response logs, so difficulty and discrimination per
  item are unknown. Every statement about what a tier "measures" is from
  reading the items.
- The end-of-level tests and the Hungarian diagnostic. The engine findings in
  A apply to Hungarian as well; the content findings do not.
- Web checks ran through search summaries; firecrawl and perplexity were
  unreachable from the session.
