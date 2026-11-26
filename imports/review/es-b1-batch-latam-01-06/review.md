# ES B1 latam batch 1–6 (2026-11-26): the first batch of the B1 Latin America track

Two Sonnet edit-in-place agents, three units each (A: pre-Columbian America, indigenous civilizations,
arrival of the Europeans; B: conquest, colonial society, colonial economy).

| Unit (app) | check-content before → after | unmet after |
|---|---|---|
| LatAm 1 pre-columbian-america | 29 / 2 → 0 / 0 | 0 |
| LatAm 2 indigenous-civilizations | 21 / 4 → 0 / 0 | 0 |
| LatAm 3 arrival-of-europeans | 28 / 2 → 0 / 1 (accepted: *sin embargo* / *no obstante* both right) | 0 |
| LatAm 4 conquest | 24 / 3 → 0 / 0 | 0 |
| LatAm 5 colonial-society | 23 / 1 → 0 / 0 | 0 |
| LatAm 6 colonial-economy | 25 / 0 → 0 / 1 (accepted, same item type) | 0 |

Reader A: 347,603 tokens (~116k a unit); Reader B: 401,752 (~134k a unit). Walk 36/36. **B1 latam 6/36 frozen.**

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

## Units 4–6

All 15 texts new; skills as the notes gave. Reader B found an error in the notes: the examples for
conquest-04 (*pidió que protegiera*) and society-03 (*para que* + past) need the imperfect subjunctive
after a past verb, which is `correlacion-temporal-subjuntivo`, B1 Unit 38 (later). It wrote those texts
in the historical present instead. Checked: no such form in Units 1–6. The brief now states the rule and
the three draft notes for Units 7–12 that repeated it were rewritten before launch; Reader A of 7–9
(already running) was told. Also *llegar a ser* (B2) avoided.

Reviewer edits: "después de 1519" → 1492 (04-05); the fleets sailed "en principio" every year, Tierra
Firme's ports named (Cartagena, Portobelo: not "the north of South America"); challenges: 05-04's
scenario English, 06-05's target re-pointed from *aunque* to the lesson's *sin embargo* and its cue no
longer names the word. Reader B left the tag re-lock to the reviewer (shared lock file): run here.

## Method changes for the rest of the track

- **Rolling start:** each reader's next three units start as soon as its units are frozen, not when the
  whole batch is done (both slots stay busy; never more than two agents).
- `scripts/latam_unit_notes.py` writes the structural part of the unit notes.
- `unmet-words.js --challenges <drafts>`; brief: option-form tells, no past-sequence subjunctive.
