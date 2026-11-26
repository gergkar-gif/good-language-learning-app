# ES B1 latam batch 1–6 (2026-11-26): the first batch of the B1 Latin America track

Two Sonnet edit-in-place agents, three units each (A: pre-Columbian America, indigenous civilizations,
arrival of the Europeans; B: conquest, colonial society, colonial economy).

| Unit (app) | check-content before → after | unmet after |
|---|---|---|
| LatAm 1 pre-columbian-america | 29 / 2 → 0 / 0 | 0 |
| LatAm 2 indigenous-civilizations | 21 / 4 → 0 / 0 | 0 |
| LatAm 3 arrival-of-europeans | 28 / 2 → 0 / 1 (accepted: *sin embargo* / *no obstante* both right) | 0 |

Reader A: 347,603 tokens for three units (~116k a unit, the B2 latam rate at three per agent). Walk 18/18.

## Units 1–3: what changed

All 15 texts new (Unit 2's five were each about another lesson's topic); screens, stems, titles and
goals in English; one known skill per lesson as the notes gave; speakers Meg, Carlos or a role.

## Reviewer edits (Units 1–3)

- *tabaco* cut from the list of Taíno loanwords (the RAE gives an Arabic origin influenced by Taíno),
  in the text, item ex05 and the story question; the text now says the Spanish met tobacco there.
- The labour-to-slavery causal chain (03-04) attributed to historians, as the agent's report claimed it was.
- *A pesar de* five times in one text (03-03): one replaced with *sin embargo*.
- *Tawantinsuyo* gloss in quotation marks; the empire's north given as southern Colombia, not Ecuador.
- 03-05.ex05: the right option alone used the lesson's structure and misquoted the text; rewritten.
- Challenges: the Tikal target stated "poco a poco" (not in the text); three targets had unmet words
  (*americanos*, *historiadores*, and *sur* from the reviewer's own first fix). The agent could not see
  them: `unmet-words.js` reads challenges.json, and the drafts were merged after its run.
  **Scripted:** `unmet-words.js --challenges <drafts.json>`; the brief now has the agent run it.
- The agent ran `lock_tags.py --update` itself after re-pointing tags (validator failed otherwise);
  kept, as the reviewer would have run the same step.
