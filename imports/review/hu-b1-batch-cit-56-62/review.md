# HU B1 citizenship batch 56-62: reviewer's notes (Claude, 2026-10-29)

Units 56 `modern-democratic-hungary`, 58 `national-symbols` (reader A), 60
`national-holidays-remembrance-days`, 62 `fundamental-law` (reader B). Both readers hit the
5-hour limit before writing a file and were resumed with SendMessage after the reset. The
reviewer read the 20 segments while they waited and checked the doubtful claims on the web
(`reviewer-facts.md`, with sources).

## Counts

| Unit | proposed | review | rejected | Claude changed / added |
|---|---|---|---|---|
| 56 modern-democratic-hungary | 120 | 119 | 1 (rewritten: answer in prompt) | 1 (*négy szabadság*, not *szabadságjog*) |
| 58 national-symbols | 137 | 137 | 0 | 1 (the Szózat line takes only *kell*) |
| 60 national-holidays-remembrance-days | 116 | 99 | 0 | 4 + 1 text fix (the Holocaust line names the Hungarian authorities' part; "tizenhárom tábornok" → *aradi vértanú* / *honvédtiszt*; a *halhatatlan* builder; the Terror Háza item, not in the segment and itself contested) |
| 62 fundamental-law | 108 | 96 | 1 (rewritten: copy of 02.ex03) | 3 + 2 text fixes (an invented continuation of a Nemzeti hitvallás sentence; one answer variant; a retag; the Fundamental Law opens with the Himnusz line, the Nemzeti hitvallás follows: segment, item and two challenges) |

Merged and applied: 482; 34 vocabulary entries (`unmet-added.txt`), 24 checklists, 24
challenges (2 changed), 66 glosses (`dictionary*.txt`). Reader tokens (resumed runs): A
294,446, B 283,765. Unit 58's reader added the sixth `concessive-postpositions` item
(03.ex05, *a kommunista évtizedek ellenére*), which clears the warning opened in batch 40-46.

## Facts (verified on the web; sources in `reviewer-facts.md`)

Wrong in the segments and fixed: the Fundamental Law adopted 18 April 2011 (signed 25 April),
in force 1 January 2012 (the Opera gala was a celebration, not the entry into force); the
praise of the Fundamental Law replaced by one line naming the dispute; the line *Isten, áldd
meg a magyart!* heads the Fundamental Law, before the Nemzeti hitvallás; the coat of arms'
fields as the Fundamental Law blazons them (first: Árpád stripes; second: triple mound); the
torch march on 22 October; ten states joined the EU in 2004 (Cyprus and Malta included);
Schengen's internal borders (Serbia and Ukraine outside); about two million Hungarians in the
neighbouring countries; *békeszerződés* as the neutral word; Szatmárcseke in Szatmár; the
thirteen of Arad not all generals; the Holocaust line now says the 1944 deportations were
carried out with the Hungarian authorities' help; invented speeches of Martonyi, Medgyessy,
Kölcsey, Erkel, Egressy and Petőfi replaced (Petőfi's by the Nemzeti dal), the Szózat quoted
as written; the readers restated the Fundamental Law's articles (B, R, II, XV, XXX, XXXI, P,
9, T) to match the text.

**For the user:** the Fundamental Law and its amendments are named as disputed in one line
(segments 56/01 and 62/01, 62/05), without taking a side. Present office holders are not
named; Schmitt Pál (2011) and Szűrös Mátyás (1989) are named as historical facts.

## After applying

- `unmet-words.js`: 34 words listed; 13 left are lookup misses (*-hat* forms, split verbs,
  inflected forms, a date suffix).
- `check_unit_refs.py`: no recap reference to check.
- `check-content`: 0 errors; 18 `vocab-unused` stems accepted at freeze (civics terms, dates
  the items write in numerals, phrases, split verbs, consolidation words on lesson 05).
- `validate-content --changed` passes; `--warnings` back to the baseline.
- Audit: every story word has a gloss.
- Walk 24/24 with challenges.
