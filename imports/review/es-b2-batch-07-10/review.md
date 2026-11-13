# ES B2 batch 7–10 (2026-11-13)

Two Sonnet edit-in-place agents, two units each (A: Units 7 time clauses + 8
concession; B: Units 9 + 10 conditionals). Both stopped at the 5-hour usage limit
(started 04:51, limit reached before 08:40) and were resumed with SendMessage at
09:01; nothing was lost (partial diffs saved first).

| Unit (app) | check-content before → after | unmet (reviewer's count) |
|---|---|---|
| 7 temporal-clauses-future | 9 / 17 → 0 / 0 | → 0 |
| 8 concession-counter-argument | 19 / 22 → 0 / 1 accepted | → 0 |
| 9 conditionals-potential-scenarios | 10 / 20 → 0 / 1 accepted | → 1 (the name *Luna*) |
| 10 conditionals-counterfactuals-regrets | 8 / 17 → 0 / 0 | → 3 kept: *hubiésemos* as an accepted answer (×2), *haberlo* |

Agent A 325,030 tokens, agent B 324,492 (both runs together): ~163k a unit. Walk 24/24.
B2 10/72 frozen. Six `taught_in` moves for these units were signed off and applied
before the batch (`decisions.md`).

## Reviewer edits

- Texts: Carpentier "Aun cuando el prólogo apareció antes…" (concession with nothing
  conceded) rewritten; "Por eso" non sequitur → "Así"; Vargas Llosa two empty
  counterfactuals removed; García Márquez closing dates drill replaced.
- b2-10-01.ex03, b2-10-05.ex03 accept *hubiésemos* beside *hubiéramos* (a learner's
  correct form was marked wrong).
- b2-10-03.ex05 wrong option "no haber viajar" (not a real string) → "de no viajé".
- Unmet words the agents' counts missed: *ambas* (b2-09-04.ex04 → *las dos*), *sur*
  (b2-09-consolidation.ex06 → *la playa*), *posteriores* (b2-10-consolidation.ex07 →
  *los años ochenta*), *computadora* (challenge b2-07-03, in no list → *bicicleta*).
- Challenge b2-08-04: "vamos a decir" → "voy a decirles" (the scenario is Carlos alone).

## Not verified

The agents' "unsure" Spanish was read and kept: *quisiera/pudiera/debiera* as softer
result forms, *salvo si* + indicative, *si bien* without *que*, *aun* unaccented in *aun
cuando*, *hasta que no* with expletive *no*. A native speaker's read is still owed.

## For the user

- *quisiera*: the A2 `polite-softening` skill title names it but its A2 screen does not
  show it; it first appears on a B1 Unit 35 screen (recapped from there).
- `check_unit_refs.py` counts the hidden latam track as a place a word is first met
  (two false positives in Unit 7): to fix in the script.
