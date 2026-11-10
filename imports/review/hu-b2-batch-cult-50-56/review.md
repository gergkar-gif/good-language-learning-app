# HU B2 culture batch: Units 50, 52 (reader A) and 54, 56 (reader B), 2026-11-10

No usage limit hit. Reader A 365,963 tokens (54 tool uses, 22 min), reader B 401,259 (55,
25 min): ~192k a unit. Reader A's report file was refused by the harness; its reply was saved
to `report-a.md` the moment it arrived.

## Counts

| Unit | proposed | rejected (repaired) | Claude changed / added | after |
|---|---|---|---|---|
| 50 `constitutional-history` | 71 | 0 | 7 words listed | 0 / 1 accepted |
| 52 `nationalities` | 81 | 1 (length) | 9 words listed | 0 / 1 accepted |
| 54 `hungarians-carpathian-basin` | 118 | 0 | **Rákóczi institution now Egyetem**; 2 words listed | 0 / 2 accepted |
| 56 `emigre-waves` | 96 | 2 (broken JSON, length) | 11 words listed | 0 / 3 accepted |

366 reader fixes applied; 4 unit readings restitched; 24 challenges; 29 more words listed; 133
dictionary entries. `check_c1_forms.py`: 0 hits. Accepted at freeze: `vocab-unused` per
lesson. Walk 24/24 with challenges. validate --changed passes. B2 64/72 frozen.

## Found by the readers (applied)

- **Every unit replays the core unit before it** (50/49 legal register, 52/51 reciprocal and
  distributive, 54/53 concessive conditionals, 56/55 figurative preverbs): recaps added; tags
  corrected where they named the wrong skill (*-andó* items, *-nként* items, concessive items).
- Politics and neighbours: "elszakított nemzetrészek", "újraegyesülés", "ellen-törvény",
  "békediktátum", "felszabadító háborúk", "vérbefojtása" replaced by neutral wording; each
  neighbouring state's rule stated as what its law says; no judgement of a present-day
  government or a neighbouring state remains.
- Grammar: a counterfactual without *volna* in the main clause (Unit 54 screen 02, and its
  speaking step); wrong case names (*annak* "allative", the illative called "allative"); the
  *-nként* rule; five wrong options that were valid focus orders (a second right answer).

## For the user

The *cigány* compounds (*oláhcigány*, *cigányzenekar*, *magyarcigány*) are standard
ethnographic terms but some find them offensive; the readers left them. Say if you want
*roma* forms.

## Not covered

No native speaker's eye; speaking steps and spoken challenge answers not checked by the walk.
Present-day figures (citizenship, census, the minority-language thresholds) carry years or are
attributed, not verified to the month.
