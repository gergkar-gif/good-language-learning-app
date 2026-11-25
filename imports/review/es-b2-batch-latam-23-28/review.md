# ES B2 latam batch 23–28 (2026-11-25)

Two Sonnet edit-in-place agents, three units each (A: Chile II, Argentina I, Argentina II; B:
Argentina III, Uruguay, Paraguay). Present-day facts searched before launch; the reviewer's read
of the old texts sent mid-run.

| Unit (app) | check-content before → after | unmet after |
|---|---|---|
| LatAm 23 chile-atacama-patagonia | 1 / 20 → 0 / 0 | 0 |
| LatAm 24 argentina-buenos-aires | 17 / 20 → 0 / 0 | 0 |
| LatAm 25 argentina-pampas-patagonia | 14 / 23 → 0 / 2 accepted | 0 |
| LatAm 26 argentina-politics | 16 / 36 → 0 / 0 | 0 |
| LatAm 27 uruguay | 2 / 28 → 0 / 0 | 0 |
| LatAm 28 paraguay | 6 / 21 → 0 / 0 | 0 (two place names in a reading option) |

Agent A 306,244 tokens (16 min), agent B 310,142 (17 min): ~103k a unit. Walk 36/36. B2 64/72
frozen.

## What changed

- Re-pointed: voseo (core Unit 34) → gerund periphrases; absolute participles (core 35) → *ser*
  passive; contrast markers (core 30) → *sin embargo* / *no obstante*; two of Unit 25's five
  concession lessons → *llegar a* / *terminar por* (B2 Unit 25); Uruguay's second *prepositional-
  phrases* lesson → *pasar a*; Units 23 and 28 topic lessons given known skills.
- Facts corrected: Buenos Aires 1914 "casi la mitad" foreign-born; Humahuaca a cultural landscape;
  the *Martín Fierro* hotel legend cut; the old text's conflation of the June 1955 bombing with the
  September coup separated; judgement words ("criminalmente", "sin precedentes") cut; superlatives
  attributed. Present-day: Milei and the 2025 midterms, Orsi, Peña, Chile's southern state of
  exception under Kast.
- 25 lessons had no goal section: checklists built with `add_missing_checklists.py --from-challenges`.

## Reviewer edits

A recap naming B1 Unit 7 for an A2 phrase reworded; two consolidation challenges (one repeated
lesson 01 word for word; "prohibido en 1955" → "tras el golpe de 1955").

## Not verified

The agents' remaining dated claims checked against the reviewer's knowledge only. Argentine monthly
inflation "around 2 %" in 2025–2026 rests on press reports of INDEC data that differ by month.
