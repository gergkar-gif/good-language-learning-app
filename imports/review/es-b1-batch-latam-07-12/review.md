# ES B1 latam batch 7–12 (2026-11-26)

Two Sonnet edit-in-place agents, three units each, started on a rolling basis (A as soon as Units 1–3
were frozen, B as soon as 4–6 were). Both stopped at the 5-hour limit; partial diffs saved, the same
agents resumed after the reset.

| Unit (app) | check-content before → after | unmet after |
|---|---|---|
| LatAm 7 race-class-power | 36 / 0 → 0 / 0 | 0 (a name) |
| LatAm 8 independence | 33 / 2 → 0 / 0 | 0 (names) |
| LatAm 9 new-republics | 31 / 3 → 0 / 0 | 0 (names) |
| LatAm 10 caudillismo | 35 / 3 → 0 / 0 | 0 |
| LatAm 11 nation-nationalism | 36 / 0 → 0 / 0 | 0 |
| LatAm 12 liberalism-modernization | 23 / 1 → 0 / 0 | 0 |

Resumed runs 310,423 (A) and 316,907 (B) tokens; the first runs' usage was lost with the limit. Walk
36/36. **B1 latam 12/36 frozen.**

## Reviewer edits

- 07-04: tenses smoothed (the value judgements now report what the surviving documents say, present).
- 08-01: José Bonaparte rejected "because they had not elected him" → "a king put there by Napoleon"
  (and item ex05). 08-04: a moralising line in the narrator's voice cut; "independence was the easy
  part" → attributed. 08-05: a repeated sentence. 09-01: the 1823 federation's name (Provincias Unidas
  del Centro de América). 11-02: "symbols are a recent creation" → "were a new creation".
- Challenges: Túpac Amaru II "murió" → executed; the castas abolished "in several countries"; 09-02
  `canDo` synced to its checklist; 11-04 target stated a fact not in the text; nine 10–12 cues that
  named the Spanish word trimmed (allowed by the `cue-quotes-target` rule, but plainer).
- 12-04.ex07: an unmet word and a past-tense question about historians' present view.
- **Vocab slug alias:** two units tagged word items `b1-<file prefix>-vocab` (32 items), which the
  validator rejects. **Scripted:** `fix_vocab_slug_alias.py`; the brief now names the unit id.
- *es decir* (B2 `reformulation-markers`) left in texts: B1 core texts use it too, and texts may sit a
  little above the learner (user, 2026-10-13); it is in no screen or item.
- Texts of Units 10–12 run 148–244 words (brief: 220–300); kept, plain. The brief now says never
  under 200.
