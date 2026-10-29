# HU B1 citizenship batch 64-69: reviewer's notes (Claude, 2026-10-29)

Units 64 `government-institutions-today`, 66 `local-governments-public-administration` (reader
A), 68 `hungarian-culture-science-heritage`, 69 `literary-musical-canon` (reader B). Neither
reader hit a limit. The reviewer read the 20 segments while they ran and checked the doubtful
claims on the web (`reviewer-facts.md`, with sources).

## The 2026 change: megye and kormánymegbízott again

Since 1 October 2026 the counties are called *megye* again and the head of a county government
office is the *kormánymegbízott* again (Act XLIX of 2026 and the 17th amendment of the
Fundamental Law; *vármegye* and *főispán* were the official names from 2023 to 2026). Reader A
was told while reading Unit 66 and used the current terms; the former names appear once, as
former names. The frozen Units 2 (`hungary-today-land-symbols`) and 56 and the mock exam
(`content/hu/cultural-exam.json`) taught "19 vármegye" as today's term: they were unfrozen,
fixed and refrozen with their accepted findings (commit d43c4f39); historical uses (St
Stephen's royal counties, Maria Theresa, Mikszáth) stay.

**For the user (outside B1):** B2 and C1 files also use *vármegye* or *főispán*; some may be
historical and right, some present-day and out of date: b2-mediatortenet, b2-alkotmanytortenet,
b2-25, b2-13-04, b2-nyelvujitas, b2-bartokkodaly, b2-szinhazmuveszet, b2-diaszpora,
b2-gimnaziumok, c1-08-05, c1-07-04, c1-egeszsegugy, c1-kozlekedespolitika, c1-emlekezetpolitika.
The 17th amendment (13 July 2026) also ended the sitting President's mandate, set an age limit
for constitutional judges and new rules for the Kúria president; no B1 text states anything
these changes made false.

## Counts

| Unit | proposed | review | rejected | Claude changed / added |
|---|---|---|---|---|
| 64 government-institutions-today | 77 | 53 | 0 | 4 (the Prime Minister's office in the Karmelita monastery dropped from segment, item and option, not confirmed after the change of government; a builder said a law enters into force on promulgation) |
| 66 local-governments-public-administration | 82 | 68 | 2 (rewritten: an old text without its comma; a copied consolidation item) | 3 (which minister proposes the kormánymegbízott dropped, ministries changed in 2026; two answer variants that don't fit) |
| 68 hungarian-culture-science-heritage | 143 | 79 | 0 | 1 (Szent-Györgyi's prize for vitamin C research, not its extraction) |
| 69 literary-musical-canon | 128 | 62 | 0 | 1 challenge (Beethoven composed the Ode to Joy's melody, Schiller wrote the poem) |

Merged and applied: 429; 12 vocabulary entries (`unmet-added.txt`), 24 checklists, 24
challenges (1 changed), 95 glosses (`dictionary*.txt`); "pl." spelled out in a segment. Reader
tokens: A 220,932, B 365,080. Reader B removed Unit 69's references to the app's mock exam
(`cultural-exam.json`, "Magyar kulturális ismereti vizsga") worded as if it were an official
exam; the mock exam's crown entry also kept the coronation mantle in Parliament, now fixed (it is
in the National Museum).

## Facts (verified on the web; sources in `reviewer-facts.md`)

Unit 64: the institutions as the Fundamental Law sets them (President 5 years, once
re-electable; PM elected by a majority on the President's proposal; ministers appointed by the
President; four court levels; chief prosecutor elected by Parliament; 200,000 signatures;
*egykamarás*, not *egyösszetevős*). Unit 66: *megye*, *kormánymegbízott*, the number of
county-rank cities (23 or 25) and districts (more than 170) no longer stated exactly. Unit 68:
Szent-Györgyi's paprika as in Unit 44; the shared 2023 prizes; Jedlik's priority named as
disputed; Semmelweis (1847, Vienna); the operettas' Vienna premieres; Kalocsa's embroidery is a
hungarikum, not on the UNESCO list (the busójárás 2009 and the matyó folk art 2012 are). Unit 69:
the Iliad's tenth year; the Ode to Joy's melody as the EU anthem; Liszt the Zeneakadémia's first
president; Kertész's prize for his body of work; the 1857 Arany tradition hedged; first, greatest
and only claims hedged or dropped.

## After applying

- `unmet-words.js`: 12 words listed; the rest are lookup misses.
- `check_unit_refs.py`: two false positives (a new example of a Unit 3 form; the known *leg-*).
- `check-content`: 0 errors; 15 `vocab-unused` stems accepted at freeze.
- `validate-content --changed` passes; `--warnings` at the baseline.
- Audit: every story word has a gloss except *herendi* (in the dictionary; the lookup misses it).
- Walk 24/24 with challenges; Units 2 and 56 walked 12/12 after their fix.
