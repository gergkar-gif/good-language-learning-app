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

## Writer's notes (append after each unit)

- Unit 10: every `listening-choice` and `dialogue-complete` item initially put the right answer at index 0 -> rotate option order across 0/1/2/3 when authoring choice items.
- Unit 10: `por el contrario` as a wrong option against `en cambio` in a two-sector contrast could be read as acceptable Spanish -> use an unmistakably wrong discourse relation (`por lo tanto`, `además`) as the distractor.
- Unit 10: `*cuanto/a/os/as*` in a grammar table tripped `latam-vosotros` on `/os/` -> write out `*cuanto, cuanta, cuantos, cuantas*` in full.

