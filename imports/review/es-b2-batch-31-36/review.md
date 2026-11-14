# ES B2 batch 31–36 (2026-11-13/14): the last core batch

Two Sonnet edit-in-place agents, three units each (A: 31 consequence/causality, 32 advanced
concessives, 33 complex conditionals; B: 34 dialect variation and register, 35 formal registers,
36 own voice). Launched 23:46 UTC; both hit the 5-hour usage limit at once, having written only
baselines; resumed at 02:00 after the reset. Four `taught_in` moves signed off before the batch
(`decisions.md` in the pilot folder).

| Unit (app) | check-content before → after | unmet after |
|---|---|---|
| 31 discourse-markers-consequence-causality | 8 / 24 → 0 / 1 accepted | 0 |
| 32 advanced-concessives | 8 / 29 → 0 / 3 accepted | 0 |
| 33 complex-conditionals | 9 / 34 → 0 / 1 accepted | 0 |
| 34 dialect-variation-register | 13 / 24 → 0 / 1 accepted | 0 |
| 35 formal-registers | 7 / 23 → 0 / 0 | 0 |
| 36 own-voice-synthesis | 12 / 38 → 0 / 0 | 0 |

Agent A 295,492 tokens (9 min, the resumed run; the first run's usage was lost with the limit),
agent B 310,080 (12 min): ~100k a unit at three per agent, against ~166k at two. Walk 36/36.
**B2 core 36/36 frozen** (36/72 with the hidden latam track).

## Texts

All six works are in copyright: texts about the work from `reviewer-facts.md` (web-search
sources only: Wikipedia, Firecrawl and Perplexity were unreachable that night). The old files
were long essays retelling whole plots, endings included (Lispector, Gallegos, Cortázar), with
claims the facts don't support. The new ones run 108–195 words, all claims from the facts file.
Reviewer edits: Unit 31 a tautology cut ("Es de Alagoas y trabaja en Río; por lo tanto…") and a
wrong option fixed ("Del sur, de Recife": Recife is in the northeast); Unit 33 the Oliveira
question tied to the first part (he lives in Buenos Aires in the second); Unit 36 a sentence
about the course itself cut and an ambiguous *su primo* fixed. `story-meta` now also flags
*la unidad N* and *de este curso* (it missed the Unit 36 line).

## Reviewer edits, items and screens

- b2-34-01: the voseo screen called *vos tenés* irregular; it follows the rule just given. Now
  only *sos* is irregular.
- Challenges: 32-consolidation gave Carlos "homework" (he has an office job): now a report for
  his boss; 33-05's target did not fit its scenario; 34-05's target had quotation marks.
- *minero* listed (b2-34-05).
- My brief was wrong: it said B2 Unit 21 presented José María Arguedas. Unit 20 is Alcides
  Arguedas (Bolivia), Unit 21 Céspedes. Agent B caught it; the Unit 35 text says the two are
  different writers.

## For the user

- Forms with no skill of their own (tagged with the nearest skill): *es que* (31-05),
  *aun a riesgo de* / *así* + subjunctive (32-02), *como* + subjunctive warnings (33-04).
- `nominalization` (b2-35-01) overlaps `nominalizacion-despersonalizacion` (b2-21-03): 35-01
  recaps Unit 21 and adds adjective nouns. A merge would need your sign-off.
- Unsure Spanish, not verified against a source: the country lists for regional words in 34-02
  (*departamento*/*apartamento*, *palta*/*aguacate*, *colectivo*/*micro*/*camión*/*guagua*) and
  *ustedeo* in Colombia and Costa Rica (34-01). Standard as far as I know; a native check helps.
