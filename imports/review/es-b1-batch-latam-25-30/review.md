# ES B1 latam batch 25–30 (2026-11-26)

Two Sonnet edit-in-place agents, three units each, rolling start; no limit stop.

| Unit (app) | check-content before → after | unmet after |
|---|---|---|
| LatAm 25 political-repression | 26 / 0 → 0 / 0 | 0 |
| LatAm 26 central-america-revolution-conflict | 16 / 0 → 0 / 0 | 0 |
| LatAm 27 southern-cone-dictatorships | 14 / 0 → 0 / 0 | 0 |
| LatAm 28 debt-crisis | 11 / 1 → 0 / 0 | 0 |
| LatAm 29 neoliberalism | 27 / 0 → 0 / 0 | 0 |
| LatAm 30 democratization | 25 / 0 → 0 / 0 | 0 |

Reader A 405,421 tokens (~135k a unit), Reader B 464,607 (~155k a unit; the heaviest so far). Walk
36/36. **B1 latam 30/36 frozen.** Truth-commission figures as checked in `reviewer-facts.md`, each
attributed; Units 26–28's shifted texts rewritten from their lesson titles.

## Reviewer edits

- 25-02.ex03: wrong option *se vigilaban a los periodistas* is accepted by many speakers → *Los
  periodistas vigilaban mucho*.
- 25-02.ex04: fill-blank had both `answer` and `answers` (schema fault hidden behind the expected
  lock failures in the agent's run). Brief now: only "locked tags changed" is the reviewer's.
- 28-03.ex04, ex06 test plural agreement (*se subieron los impuestos*): retagged `pasiva-refleja`.
- *la tasa (de interés)* listed in 28-02; 30-02 challenge `canDo` synced to its checklist.
- Kept: Units 25 and 27 both mention Argentina's 1986–87 laws and their annulment (27 is about
  memory, a recap); the nickname «las locas» (not a witness quotation).
