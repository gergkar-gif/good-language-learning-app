# HU B1 citizenship batch 32-38: reviewer's notes (Claude, 2026-10-28)

Units 32 `revolution-1848`, 34 `kossuth-petofi-national-cause` (reader A), 36 `compromise-1867`,
38 `austria-hungary` (reader B). A container restart killed the first pair of readers before
any file was written; both were relaunched from the same prompts.

## Counts

| Unit | proposed | review | rejected | Claude changed / added |
|---|---|---|---|---|
| 32 revolution-1848 | 96 | 63 | 0 | 1 (Isaszeg/Pest order) |
| 34 kossuth-petofi-national-cause | 107 | 68 | 2 (rewritten) | 1 (*segesvári* lowercase) |
| 36 compromise-1867 | 102 | 66 | 0 | 1 (an invented Andrássy quote taught as fact) |
| 38 austria-hungary | 106 | 68 | 0 | 1 (population passed 50 million by 1910), 2 shared checklist lines |

Merged and applied: 411; 51 vocabulary entries (`unmet-added.txt`), 24 checklists, 24
challenges, 80 glosses. Reader tokens (rerun): A 338,173, B 371,645 (~170–185k a unit).

## Facts

All standard; none needed a web search or a decision. Unit 32: Vienna's revolution of 13
March, the Lieutenancy Council's concessions (censorship, Táncsics), the April laws, Jellačić
(September 1848), Debrecen, the dethronement and Kossuth as governor-president (14 April 1849),
Isaszeg (6 April; the imperials left Pest by the campaign's end), Buda (21 May), the Russian
intervention (asked in early May, entered in June), Kossuth's resignation (11 August), Világos
(13 August), Arad (nine hanged, four shot) and Batthyány's execution on 6 October. Unit 34:
Kossuth in New York (December 1851), received by the president and Congress, the Danube
Confederation, the Kossuth-bankó (1848–49 paper money); Petőfi (26 years, Segesvár, fate
disputed); the cockade (Szendrey Júlia, tradition); the three national holidays; the legal
term *állampolgársági eskü*. Unit 36: Bach, the Easter Article (1865), the coronation (8 June
1867, Simor and Andrássy), 1873, Baross (late 1880s); the Compromise's verdict named as
disputed. Unit 38: the common affairs and ministries, the delegations, forint then korona,
German as the language of command, the Millennium (Heroes' Square begun 1896, Vajdahunyad
temporary, the continent's first underground), Budapest 880,000 in 1910, the ZBD transformer
1885, Bosnia 1878, emigration over 1.5 million.

## After applying

- `unmet-words.js`: 51 words listed; the rest are lookup misses and names.
- `check_unit_refs.py`: only the known *leg-* false positive.
- `check-content`: two goal lines shared between Units 36 and 38 (one per reader), reworded;
  0 errors; 15 `vocab-unused` accepted at freeze (`accept.json`).
- `validate-content --changed` passes; `--warnings` identical to the baseline.
- Walk 24/24 with challenges.
