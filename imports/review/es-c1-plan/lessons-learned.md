# ES C1: lessons learned (read before every unit)

Kept by Claude after each review and by the writer after each unit (append, newest last; one
line each: what went wrong, and the rule that prevents it). The rules that apply to every unit
are also in the writer template; this file adds what the latest reviews found. Before each unit,
also run `python scripts/c1_reviewer_changes.py --last 3` and read what the reviewer changed.

## From the reviews so far (Units 1-8)

- Units 1-2: a screen stated a norm rule more strongly than the RAE (double participles as
  adjectives): state norms only as strongly as the source; a wrong option the norm accepts is a
  second right answer.
- Units 1-2: two-option choice items: always 3+ options (`few-options` fails fewer).
- Units 1-7: production prompts that two answers fit: pin the construction, the verb, the person
  and the gender in the prompt.
- Units 3-7: recaps naming the wrong unit (*con el fin de* "from B2 Unit 12", taught in B1 Unit
  32): take every unit number from the knowledge sheet or `c1_recap_candidates.py`, never memory.
- Units 3-7: consolidation items copying lesson items or screen examples word for word: vary them.
- Units 5-7: a unit's items carried the previous unit's vocabulary tag: check every `teaches` is
  this unit's `c1-<unit id>-vocab` or a real skill.
- Unit 6: the text's commentary contradicted its own articles: reread the text against itself.
- Unit 8: unnatural collocations and illogical claims (a rise "exceeding the decline", a share
  "in points"); listening wrong options that were unrelated multi-fault sentences with absolutes;
  goals no item practised; challenge scenarios not matching their targets; a false claim (*crecer*
  as an irregular gerund); a "wrong" option the DLE accepts (*en torno de*).
- Unit 8: a contested form (*la mayoría de* + bare plural) used as the error: when usage is
  divided, test a form nobody accepts instead (*la mitad de* + bare plural).

- Units 9-10 (reader, 71 fixes): listening wrong options that change TWO details (again: change
  exactly one); a time word or absolute only in wrong or reading options (a tell); a "wrong" option
  that is accepted Spanish (*De pedir el préstamo …, habría pagado* is a valid condition); hints that
  name the agreement being tested or invite another right verb; unnatural phrases (*líneas de
  trabajo*, *organizar sus prestaciones*, the calque *pienso si*); questions about the text that the
  text does not answer; an invented person with a full name and title in a text (keep people
  unnamed: *una investigadora*); Spain-only *a medio plazo* in es-latam (*a mediano plazo*).
- Units 9-10: option order does NOT matter: the app shuffles options when it shows them
  (`engine/lessons.js` `shuffledOptions`). Do not spend effort rotating right answers.
- Unit 10 (notes drafted by the writer): two lessons re-taught B1/B2 screens almost whole. A recap
  lesson must add what the earlier screen did not teach (a C1 variant, a formal or written use,
  a contrast with a near form), never repeat it; see `notes/README.md`.

- Units 11-12 (reader, 57 fixes): a recap that misdescribed the earlier screen (B2 Unit 1 fronts
  adjectives and place phrases, not objects): print the screen with `show_screen.py` before
  recapping it; hints that give away the tested point (the mood, "with accent"): a hint names the
  verb and person only; *-ra* and *-se* imperfect subjunctive are the same form, so an answer
  accepts both (`answers: [hubiera, hubiese]`); real wrong forms of other skills carry
  `distractor_skills` (none of Units 11-12's items had any); illogical exchanges (thanking for the
  floor before it is given), tautologies (*ceñirse al tema y no desviar el tema*), reading questions
  whose premise is not in the text; a lesson goal (topic vs contrastive focus) no item practised.
- Units 8-12: listening wrong options rewritten in every read. `check-content` now flags
  `listening-many-changes` (a wrong option 10+ words away from the right one); fix every hit.

- Units 13-15 (readers, 94 fixes): the most frequent class: a screen presents as NEW a form the
  knowledge sheet already lists (*a raíz de*, *-ra/-se*, passive *se*, *habrá salido*, the
  prepositional cleft, *debería haber*), or recaps one unit when the form was taught in two. Rule:
  for every Spanish form on a screen, grep the sheet; if it is there, the screen says "You know *X*
  from <Level> Unit N" and teaches only what is new. Also: two wrong options with the SAME fault
  (each wrong option has its own fault); an extra word or detail in only one option (a tell);
  `distractor_skills` on an ungrammatical option (only on real forms of another skill);
  fill-blanks missing equally right answers (*debió / debía* beside *debería*); reading answers
  that add what the text does not say; challenge targets that do not use the canDo's form;
  illogical scenarios (a committee "evaluating the diagnosis").

- Units 16-19 (readers, 166 fixes after the self-reads' 85): screens still present known forms as
  new (*mientras que*, the five verbs of change, accidental *se*, *como* + subjunctive warnings are
  B1/B2); unit texts under 400 words (`c1-text-length` now fails them); options in which two wrong
  answers share a fault; `tier2` on consolidation challenges (every C1 challenge is `tier1`, as
  the brief's model entry; the grader scores tier2 as a transaction and failed one target);
  hints naming the tested point; prompts that two answers fit; reading answers not in the text;
  missing `distractor_skills` on real forms of other skills.

## Writer's notes (append after each unit)

- Unit 10: every `listening-choice` and `dialogue-complete` item initially put the right answer at index 0 -> rotate option order across 0/1/2/3 when authoring choice items. (Reviewer: not needed, the app shuffles options.)
- Unit 10: `por el contrario` as a wrong option against `en cambio` in a two-sector contrast could be read as acceptable Spanish -> use an unmistakably wrong discourse relation (`por lo tanto`, `además`) as the distractor.
- Unit 10: `*cuanto/a/os/as*` in a grammar table tripped `latam-vosotros` on `/os/` -> write out `*cuanto, cuanta, cuantos, cuantas*` in full.
- Unit 11: `c1-11-05-a-gr` initially claimed *hasta el punto de que* was taught in B2 Unit 31, but `check_unit_refs.py` + `show_screen.py` showed B2 Unit 31 only taught *de tal manera que* / *de tal modo que* -> verify every italicised form in a recap opener against the actual B1/B2 screen.
- Unit 11: conjugating the verb inside a multi-word vocabulary expression (`ceda` from `ceder la palabra`) triggered `unmet-words` -> use multi-word verbal expressions in the infinitive in exercises unless the base verb is already met.
- Unit 12: *el lector* inside exercises triggered `item-reader` suspects, and *enfado* in the story triggered `course-variant` -> use concrete roles (*el cliente*, *el periodista*, *el público*) in exercises and *enojo* in es-latam.
- Unit 12: irregular preterite *dedujo* (from new verb *deducir*) tripped `unmet-words` -> prefer regular forms of newly listed irregular verbs in exercises when testing mood contrast.
- Unit 13: a fill-blank hint naming only `deber (3rd person singular)` before `haber` left `debe`/`debió` valid alongside `debería` -> include the English cue (`'should have'`) or anchor the present frame (`hoy`, `present`) so only one form fits.
- Unit 13: Reading Q2 initially used `completely replaced` and two choice distractors had extra time phrases (`el año pasado`, `el mes pasado`) -> remove absolutes and asymmetric time phrases from wrong options during self-review.
- Unit 14: two Reading options initially mentioned details not in the corresponding paragraph (`intermittent clean generation`, `circular-economy rules` in paragraph 5) -> verify every phrase of every reading answer directly against its paragraph.
- Unit 14: grouped italic runs (`*se busca / se buscan*`, `*lo bueno, lo malo, lo importante*`) in recap openers tripped `check_unit_refs.py` -> put each cited form in its own italic run.
- Unit 15: self-review of rendered output caught an asymmetric time word (`hoy`) in only one wrong option (`c1-15-01.ex08`) and a second fault (masculine `solo` with feminine `la discriminación`) in a mood-contrast distractor (`c1-15-05.ex09`) -> inspect every wrong option in the rendered text for asymmetric adverbs and stray gender/number errors.
- Unit 16: self-read caught `no X, pero sí Y` used as a wrong option in a `sino-vs-pero` item (`c1-16-04.ex08`, valid Spanish -> second right answer) and several choice distractors with two tense faults instead of one -> verify every wrong option has exactly one fault and is not accepted in another reading.
- Unit 16: fill-blank hints that named the tested tense, gender, or conjunction (`past baseline`, `feminine singular`, `corrective conjunction`) gave away the answer -> keep hints to bare verb + person, `definite article`, or plain English gloss (`but`).
- Unit 17: self-read caught three `se-aspectual` choice items where all three wrong options repeated the same bare-noun fault, plus a punctuation mismatch between `tiles` (`"entera."`) and `solution` (`"de memoria."`) in `c1-17-01.ex07` -> give each wrong option its own distinct fault and verify `sorted(tiles) == sorted(solution)` on every `sentence-builder`.
- Unit 17: `se rió` in the story carried a pre-2010 accent on monosyllabic `rio` -> check monosyllabic preterites (*rio, vio, dio, fue, fui*) against RAE 2010 orthography.
- Unit 18: 1st-person stance openers (*para ser sincero/a*) cannot open a 3rd-person report (`Para ser sincera, la panadera admitió...` attributes honesty to the narrator, not the baker) and stacking `Dicho esto, en todo caso...` contradicted our own tip against stacking -> pair *para ser sincero/a* with 1st-person speech and never stack two stance openers in examples or exercises.
- Unit 18: sentence-final `, pues.` is acceptable in several Latin American varieties, and `tell-opener` flags choice items where only the right option starts with *pues / bueno / mira* -> use unmistakably wrong markers (e.g. `, o sea.`) as distractors and test mid-turn or non-opener positions when `tell-opener` fires.
- Unit 19: `add_challenges.py` requires `canDo` to match the lesson's **first** checklist item verbatim, and `fb()` in `es_c1_builders.py` takes `answers=[...]` (not `alt=`) for multiple accepted answers -> always copy `checklist[0]` into `canDo` and use `answers=[...]` for `-ra`/`-se` subjunctive pairs.
- Unit 19: self-read caught a redundant condition+connector pair (`como vuelvas..., de lo contrario...`), missing personal *a* (`perderemos el cliente` -> `al cliente`), and an impossible English tense in a listening distractor (`was delayed tomorrow`) -> read every grammar example and distractor aloud in both languages during the self-read.
- Unit 20: self-read caught fill-blank hints naming the tested grammar label or agreement (`present concession`, `agreeing with «la tarifa»`) and a challenge target using `para lo ... que` while `canDo` (`checklist[0]`) named `con lo ... que` -> keep hints to bare lemmas or plain English glosses (`'may well be'`) and verify every challenge target matches `checklist[0]`'s exact form.
- Unit 20: grammar screen tables require 2-column rows (`[left, right]`) and `matching` pairs require 2-element arrays (`[spanish, english]`), not dicts -> always generate 2-column tables and list pairs in builder scripts.
- Unit 21: self-read caught an internal arithmetic mismatch in the satirical column (90 min Monday + 3.5 h Tuesday = 5 hours, not 6) and a `rhetorical-devices` dialogue item whose wrong options only tested `subjunctive-emotion` mood -> check every time/number total inside a story against its own paragraphs, and verify every item's distractors actually break its `teaches` skill.
- Unit 22: self-read caught 4 unmet words (`metió`, `perdona`, `buenísimo`) plus asymmetric time/second-clause phrasing in dialogue distractors and grammar-label hints (`superlative`, `preterite`, `admiring augmentative`) -> keep dialogue distractors strictly symmetric outside the tested form, use plain English glosses in hints, and verify `distractor_skills` slugs against `skills/es.json` (e.g. `imperfect-subjunctive-forms`, not `imperfecto-subjuntivo`).





