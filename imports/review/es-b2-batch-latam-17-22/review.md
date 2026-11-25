# ES B2 latam batch 17–22 (2026-11-25)

Two Sonnet edit-in-place agents, three units each (A: Ecuador, Peru I, Peru II; B: Bolivia I,
Bolivia II, Chile I). All topic-only. Present-day facts searched before launch; the reviewer's read
of the old texts sent mid-run.

| Unit (app) | check-content before → after | unmet after |
|---|---|---|
| LatAm 17 ecuador | 11 / 8 → 0 / 1 accepted | 0 |
| LatAm 18 peru-cusco-andes | 15 / 10 → 0 / 1 accepted | 0 |
| LatAm 19 peru-coast-lima | 9 / 6 → 0 / 0 | 0 |
| LatAm 20 bolivia-altiplano | 8 / 7 → 0 / 0 | 0 |
| LatAm 21 bolivia-lowlands | 2 / 21 → 0 / 0 | 0 |
| LatAm 22 chile-central | 3 / 26 → 0 / 0 | 0 |

Agent A 328,360 tokens (18 min), agent B 320,171 (16 min): ~108k a unit. Walk 36/36. B2 58/72
frozen. Retired slugs 237 → 47.

## Facts corrected (reviewer-facts.md)

Ecuador's 2008 constitution approved by referendum on 28 September (not "ratified 20 October");
Quito one of the first UNESCO sites, not the first; Valech: about 28,000 people (2004), not "más de
veinte mil"; Diego Quispe Tito as leader of the 1688 split cut; the Eiffel attribution of Iquitos's
Casa de Fierro marked disputed; a dozen superlatives attributed; invented witnesses cut (Don
Teófilo and others) and Allende's speech, Víctor Jara's poem and the 2019 slogan paraphrased.
Present-day: Peru's president-elect Keiko Fujimori (June 2026), Bolivia's Rodrigo Paz and the
lithium contracts, Chile's Kast (March 2026), the Yasuní closure behind schedule.

## Reviewer edits

Valech figure; a repeated sentence in perucosta-05; chilecentro-consolidation challenge rewritten
as fronting (its checklist line); three consolidation `canDo` lines synced. The six leftover
consolidation texts retired (`latam_consolidation_story.py`).

## Not verified

Article 71 of Ecuador's constitution is paraphrased (the source host is not reachable). Agents'
other claims checked against the reviewer's knowledge only. No native read.
