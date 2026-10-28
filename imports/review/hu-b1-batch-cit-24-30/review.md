# HU B1 citizenship batch 24-30: reviewer's notes (Claude, 2026-10-28)

Units 24 `driving-out-ottomans`, 26 `rakoczi-war` (reader A), 28 `18th-century-rebuilding`,
30 `reform-age` (reader B). Both readers stopped at the 5-hour Sonnet limit before writing a
file and were resumed after the reset; usage below is the resumed runs only.

## Counts

| Unit | proposed | auto | review | rejected | Claude changed / added |
|---|---|---|---|---|---|
| 24 driving-out-ottomans | 94 | 32 | 58 | 4 (2 rewritten, 2 applied by hand) | 5 changed (verbal-noun options, a hedge, odd options), 2 added, 1 segment hedge |
| 26 rakoczi-war | 109 | 40 | 67 | 2 (rewritten) | 1 changed, 1 added (*Hol?* answered in *-ba*) |
| 28 18th-century-rebuilding | 115 | 36 | 77 | 2 (rewritten) | 1 recap (*annak dacára*), 1 answer list |
| 30 reform-age | 113 | 36 | 75 | 2 (rewritten) | 1 added (03.ex05 verbal nouns) |

Merged and applied: 429; then 8 more fixes (`extra2-4.json`, a goal line by hand), 76
vocabulary entries (`unmet-added.txt`), 24 checklists (from the goal lines), 24 challenges (3
edited), 64 glosses. Reader tokens (resumed runs): A 299,340, B 289,650.

## Facts

All verified from my own knowledge of the standard accounts; none needed a web search or a
decision. Unit 24: Buda retaken 2 Sept 1686 (Lorraine; Abdurrahman fell), Nagyharsány 1687,
Zenta 1697, Karlowitz 1699 without the Temesköz, the Neoacquistica ransom (10%), the 1687 diet
(free election and the right of resistance given up), Brezán 1703; "treated as a conquered
province" now hedged in segment and item. Unit 26: Szécsény 1705, Ónod 1707, the *libertás*,
Trencsén 1708, Szatmár 1711 (Károlyi), Rodostó, death 1735, reburial at Kassa 1906; the
peace's reading named as disputed. Unit 28: Pragmatic Sanction 1723, Silesia 1740, the 1741
diet ("Vitam et sanguinem" hedged as tradition), Urbárium 1767, Ratio Educationis 1777 (no
compulsory schooling: 1868), Edict of Tolerance 1781 (limited), language decree 1784, the
1790 revocations, Bessenyei 1772, Magyar Hírmondó 1780, the first theatre company 1790.
Unit 30: Széchenyi's offer Nov 1825 at 34, Hitel 1830, the Iron Gates in the 1830s, the Chain
Bridge (W. T. Clark design, Adam Clark, opened 1849), the 1836 toll law, Pesti Hírlap 1841,
the 1844 language act, Himnusz 1823 (Erkel 1844), Szózat 1836, the theatre 1837 (Nemzeti from
1840), Védegylet 1844, 3 March and 15 March 1848.

## After applying

- `unmet-words.js`: 76 words listed; remaining hits are split verbs, *-hat* forms and names.
- `check_unit_refs.py`: *annak dacára, hogy* "from B1 Unit 24" (reader B) no longer true once
  reader A rewrote that screen; recap and the item's accepted answers fixed.
- `check-content`: 0 errors; 10 `vocab-unused` accepted at freeze (`accept.json`).
- `validate-content --changed` passes; `--warnings` identical to the baseline.
- `add_challenges.py`: a regnal or ordinal numeral's full stop no longer counts as a
  sentence end (it refused two more targets about kings here; fourth time).
- Walk 24/24 with challenges.
