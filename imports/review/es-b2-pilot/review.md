# ES B2 pilot: core Units 1 and 2 (2026-11-13)

Spanish B2 exists only in es-latam. Method: two Sonnet **edit-in-place** agents, one
unit each, briefs `brief-a.txt` / `brief-b.txt` (shared part now
`scripts/templates/edit-spanish-latam-b2.txt`); the reviewer applied their diffs
(`agent-a.patch`, `agent-b.patch`), read every screen, both texts and the flagged
items, edited, added challenges, locked, walked and froze.

## Counts

| Unit (app number) | check-content before | after | unmet words before → after | items locked |
|---|---|---|---|---|
| 1 nuance-precision-emphasis | 12 errors / 11 suspects | 0 / 2 accepted | 60 → 0 | 51 |
| 2 narrative-time-aspect | 5 / 17 | 0 / 0 | ~80 → 0 | 43 |

Agent A 292,498 tokens (14 min), agent B 304,407 (14 min): ~300k a unit at one unit
per agent. Walk 12/12, challenges ✓. B2 2/72 frozen.

## What changed

- All 10 grammar screens rewritten in English (they were academic Spanish), with
  recaps by the app's unit numbers; every Spanish question stem asked in English.
- The Borges and Rulfo retellings (both authors in copyright) replaced with original
  texts about the author and the work (336 and 309 words); every claim checked
  (`reviewer-facts.md`).
- Generator defects fixed: wrong claims on screens (*quiso* "deliberate attempt",
  *apenas* "always instant", "imperfecto de ruptura", object fronting "archaic"),
  unmet academic words, length give-aways, time-word tells, *billete* in es-latam,
  hidden-track forms (*negó*, reporting verbs).
- Unit 2 lessons 01–05 had no checklist and no review step: added
  (`add_missing_checklists.py`).

## Reviewer edits to the agents' work

- Borges text: *pasó a formar parte* (*pasar a* + infinitive, B2 Unit 23) → *se
  convirtió en la primera parte de Ficciones* (also more exact).
- Unit 1 comprehension questions and explanations put in English (decision 2).
- b2-02-04: *apenas* "barely" recapped from B2 Unit 1 (agent A taught it there).
- Challenges: Meg "studying Spanish in Budapest" and "the story you studied"
  removed (invented facts).
- Four new items so the two new skills reach 6 (b2-02-04.ex07–08,
  b2-02-consolidation.ex10–11); one tell of my own (*ayer*) removed before commit.

## Decided by the user (2026-11-13), all in `decisions.md`

English screens; texts about in-copyright works; cognate allowance; core homes for
hidden-track skills (proposals in `hidden-skill-homes.md`); one unit-number rule for
all courses (812 recaps renumbered, ACHIEVED 153); new units allowed where a skill
has no core home; `stance-adverbs` taught in b2-01-02; new skills
`conectores-temporales-narrativos` and `imperfecto-de-cortesia`.

## Not verified

Speaking steps, spoken challenge answers, audio, and a native speaker's read of the
Spanish (agents' "unsure" lines: the *que galicado* note, *Decisivo fue estudiar cada
día*, the *de pronto, oía* wrong option — all read by the reviewer and kept).
