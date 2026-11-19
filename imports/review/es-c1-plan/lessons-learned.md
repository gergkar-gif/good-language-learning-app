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

## Writer's notes (append after each unit)

- Unit 10: every `listening-choice` and `dialogue-complete` item initially put the right answer at index 0 -> rotate option order across 0/1/2/3 when authoring choice items. (Reviewer: not needed, the app shuffles options.)
- Unit 10: `por el contrario` as a wrong option against `en cambio` in a two-sector contrast could be read as acceptable Spanish -> use an unmistakably wrong discourse relation (`por lo tanto`, `además`) as the distractor.
- Unit 10: `*cuanto/a/os/as*` in a grammar table tripped `latam-vosotros` on `/os/` -> write out `*cuanto, cuanta, cuantos, cuantas*` in full.
- Unit 11: `c1-11-05-a-gr` initially claimed *hasta el punto de que* was taught in B2 Unit 31, but `check_unit_refs.py` + `show_screen.py` showed B2 Unit 31 only taught *de tal manera que* / *de tal modo que* -> verify every italicised form in a recap opener against the actual B1/B2 screen.
- Unit 11: conjugating the verb inside a multi-word vocabulary expression (`ceda` from `ceder la palabra`) triggered `unmet-words` -> use multi-word verbal expressions in the infinitive in exercises unless the base verb is already met.
- Unit 12: *el lector* inside exercises triggered `item-reader` suspects, and *enfado* in the story triggered `course-variant` -> use concrete roles (*el cliente*, *el periodista*, *el público*) in exercises and *enojo* in es-latam.
- Unit 12: irregular preterite *dedujo* (from new verb *deducir*) tripped `unmet-words` -> prefer regular forms of newly listed irregular verbs in exercises when testing mood contrast.

