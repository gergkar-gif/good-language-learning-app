# ES B2 latam batch 11–16 (2026-11-25)

Two Sonnet edit-in-place agents, three units each (A: Dominican Republic, Puerto Rico, Colombia I;
B: Colombia II, Venezuela I and II). All six units topic-only. Present-day facts searched before
launch; the reviewer's read of the old texts sent mid-run.

| Unit (app) | check-content before → after | unmet after (--with-hidden) |
|---|---|---|
| LatAm 11 dominican-republic | 13 / 15 → 0 / 0 | 0 |
| LatAm 12 puerto-rico | 10 / 14 → 0 / 0 | 0 |
| LatAm 13 colombia-andes | 15 / 15 → 0 / 0 | 0 |
| LatAm 14 colombia-caribbean-pacific | 12 / 12 → 0 / 3 accepted (real quotations) | 0 (2 listed by the reviewer) |
| LatAm 15 venezuela-oil-caracas | 14 / 5 → 0 / 1 accepted | 0 |
| LatAm 16 venezuela-llanos-diaspora | 15 / 4 → 0 / 0 | 0 |

Agent A 362,333 tokens (20 min), agent B 346,891 (19 min): ~118k a unit. Walk 36/36 with
challenges. B2 52/72 frozen. Retired slugs in es-latam 435 → 237.

## What the old texts had, and what changed

- **Invented witnesses** in most texts: named people (Don Baudilio, Doña Luz Marina, la doctora
  Arreaza…) speaking in quotation marks, and real people given invented speeches or roles (Luz Marina
  Bernal, Carlos Castaño-Uribe, Diana Trujillo as a "biologist"). All cut. **Scripted:** the
  `story-quote` suspect in check-content (quoted spans of 6+ words in world texts); its first run
  found the real quotations in frozen Costa Rica and Guatemala (accepted) and 31 / 15 hits in es-es B1
  and HU world texts, not read (for those levels' checklists).
- **Leftover consolidation stories:** 27 units had a sixth generated text, `<stem>-consolidation.json`,
  either shown by the consolidation lesson or orphaned but listed for the Reader. **Scripted:**
  `scripts/latam_consolidation_story.py` points the lesson to the rebuilt combined reading and deletes
  the leftover; run on the six units here and on frozen Cuba.
- Facts corrected (reviewer-facts.md): Hispaniola is not the only shared island in the Americas;
  *Kerepakupai Merú*; hyperinflation over 100,000 % in 2018 only; the novel's 1928 figure kept out of
  history; Metrocable and Chiribiquete superlatives attributed. Present-day: Venezuela after 3 January
  2026, Colombia's president since 7 August 2026, UNHCR figures, Puerto Rico's 2024 vote.

## Reviewer edits

- *africano*, *plebiscito* listed (colombiaperiferias-01, -04).
- colombiaperiferias-05.ex02: English pinned to the hypothetical ("in the future") so *haya*, not
  *hay*, is the one answer.
- Four challenge `canDo` lines synced after `fix_shared_checklists.py`; the documented order is now
  checklists → `add_challenges.py` → `fix_shared_checklists.py`.

## Not verified

Agents' ≤90 % claims (report files) checked against the reviewer's knowledge only: Benkos Biohó 1621,
Chiribiquete park 1989, Jimmie Angel 1933, Alma llanera 1914, Puerto Rico's list of status votes.
No native read.
