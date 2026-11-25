# ES B2 latam batch 1–4 (2026-11-25): first batch of the Latin America track

Two Sonnet edit-in-place agents, two units each (A: Mexico I mexico-central, Mexico II
mexico-north; B: Mexico III mexico-south, Guatemala), brief = `unit-<x>.txt` +
`scripts/templates/edit-spanish-latam-b2-track.txt`. No usage-limit stop.

| Unit (app) | check-content before → after | unmet after (--with-hidden) |
|---|---|---|
| LatAm 1 mexico-central | 32 / 20 → 0 / 3 accepted | 0 |
| LatAm 2 mexico-north | 23 / 11 → 0 / 3 accepted | 0 |
| LatAm 3 mexico-south | 28 / 13 → 0 / 1 accepted | 0 |
| LatAm 4 guatemala | 30 / 13 → 0 / 0 | 0 |

Agent A 354,086 tokens (15 min), agent B 325,566 (13 min): ~170k a unit, the ES B2 core rate
at two per agent (~166k). Walk 24/24 with challenges. B2 40/72 frozen (core 36, latam 4).

## What changed

- All 20 screens, every question stem, lesson title, goal and the track intro in English; each
  screen a recap of a known skill applied to the region.
- Six lessons re-pointed from skills taught later in core to known ones: mexiconorte-01
  (*ir* + gerund → *conforme*), -03 (*de* + infinitive → *si* clauses), -05 (gerund tag on a
  passive-*se* lesson → `pasiva-refleja`), mexicosur-01 (subjunctive relatives → indicative
  relatives), -02/-05 (*por más que*, *si bien* → *a pesar de que*, *aunque*), guatemala-02
  (*antes de que* → *antes de* + infinitive), -03 (*si bien* → *a pesar de que*). No `taught_in`
  moved.
- All 20 lesson texts rewritten plainer (200–306 words), every reviewer-facts verdict applied;
  the four combined readings restitched, retitled, English summaries, fake `source` lines replaced.
- 15 lessons given checklists (`add_missing_checklists.py`), 24 challenges added.

## Facts corrected (reviewer-facts.md, sources there)

Outdated: the Zapatista Juntas de Buen Gobierno (dissolved November 2023). Wrong: the CEH
genocide regions (Ixil, Q'anjob'al/Chuj, K'iche', Achi; not q'eqchi'), Temple I built by
Jasaw's order (raised over his tomb under his son), "Ministerio" for the SEP, "más de sesenta
lenguas" for the south (68 is all Mexico), subsidence > 40 cm/yr. Cut as unsupported: a dozen
figures and superlatives (Tikal's population, "primer" mixed site, Copper Canyon "cuatro veces",
San Ysidro "más transitado del planeta", 48 Cantones figures). Agents also cut Frida Kahlo from
the muralism text (not a muralist) and gave no figure for the 1968 toll.

## Reviewer edits

- guatemala-01 screen row "fue levantado por orden del rey" (contradicts the fact) → "sobre la
  tumba del rey"; guatemala-02 example "Antes de bajar a Xibalbá, los gemelos eran jóvenes"
  (empty) → "Antes de subir al cielo, los gemelos vencieron a los señores de Xibalbá".
- Guatemala consolidation challenge: its `canDo` was not the checklist's first line; rewritten
  on that line (Tikal explored by expeditions in the mid-19th century, from the text).
- Agents' doubtful wrong options read and kept (each has one fault and none answers the prompt):
  mexicocentro-05.ex07, mexiconorte-02.ex02, -03.ex05, mexicosur-01.ex05.

## Not verified

Claims stated from the agents' and reviewer's knowledge without a fetched source: the CEH's 3 %
for the guerrilla, REMHI (April 1998) and Gerardi's murder two days later, Ríos Montt's 2013
conviction and annulment, Fuego June 2018, LiDAR 2018, Monterrey 2022 drought, Fundidora's
closure 1986, Tecnológico 1943. No native read. Wrong-answer paths and speaking steps unwalked.

## For the user

- Is the B1 latam track read before B2 latam is shown? B2 latam now assumes it is not met.
