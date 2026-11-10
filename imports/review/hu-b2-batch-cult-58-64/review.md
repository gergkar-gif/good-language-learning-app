# HU B2 culture batch: Units 58, 60 (reader A) and 62, 64 (reader B), 2026-11-10

Both readers stopped at the 5-hour Sonnet limit and were resumed after the reset with
SendMessage (not replaced). Reader A 336,663 tokens (35 tool uses after the resume), reader B
349,608 (32): ~172k a unit, resumed notices only.

## Counts

| Unit | proposed | rejected (repaired) | Claude changed / added | after |
|---|---|---|---|---|
| 58 `visegrad-geopolitics` | 98 | 8 (6 cascades rebased, 1 length, 1 goal line by hand) | 9 words listed | 0 / 4 accepted |
| 60 `ombudsman-civic-rights` | 90 | 10 (8 cascades rebased, 1 length, 1 goal line by hand) | 9 words listed | 0 / 4 accepted |
| 62 `paprika-tokaj` | 81 | 1 (length) | 16 words listed | 0 / 2 accepted |
| 64 `sport-national-identity` | 96 | 0 | summary "90 years"; a wrong recap; 10 words listed | 0 / 4 accepted |

365 reader fixes applied; 4 unit readings restitched; 24 challenges; 44 more words listed; 240
dictionary entries. `check_c1_forms.py` 0 hits after the fixes. Accepted at freeze:
`vocab-unused` per lesson. Walk 24/24 with challenges. validate --changed passes. B2 68/72.

## Scripts written in this batch (recurring problems)

- **`scripts/rebase_fixes.py`**: a reader's goal-line fixes that build on an earlier fix to
  the same line were rejected (old text 0x) for the third time; the script rebases each such
  fix on the earlier ones of the same file and refuses where that does not give a single
  match. 14 of 16 rebased here; 2 goal-array lines done by hand.
- **`check_c1_forms.py` takes unit ids**: reader A ran it with the unit id and got a silent 0
  while *szíveskedjék* was in Unit 60; the script now resolves unit ids and fails on a name
  that matches no files.

## Found by the readers (applied)

- Every unit replays the core unit before it (58/57 diplomatic softening, 60/59, 62/61
  *mintha*, 64/63 `annyira-hogy` and Unit 55's preverbs): recaps added, tags corrected (the
  resultative *-ra/-re* items from `mintha` to `ra-re`; preverb items from `annyira-hogy` to
  `b2-figurative-preverbs`).
- Unit 60's C1 *szíveskedjék* rewritten with *kérem, hogy* + subjunctive and *kérném*.
- Unit 62 consolidation ex06 used Unit 63's result clause: rewritten.

## For the user

- Unit 62 is titled `paprika-tokaj` but no segment or lesson covers paprika.

## Not covered

No native speaker's eye; speaking steps not checked. Present-day rules (ombudsman, appeal
deadlines, the 1% procedure, Tokaj's puttonyos rule since 2013) carry "check" in the readers'
facts files and are attributed in the text, not verified article by article.
