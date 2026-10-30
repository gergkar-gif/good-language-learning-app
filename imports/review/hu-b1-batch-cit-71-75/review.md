# HU B1 citizenship batch 71-75: reviewer's notes (Claude, 2026-10-30)

Units 71 `hungarians-abroad`, 73 `being-hungarian-citizen` (reader A), 74 `kormanyablak`, 75
`tenancy-contracts` (reader B). Units 74 and 75 have no world segments: their unit stories
(`b1-kormanyablak.json`, `b1-alberlet.json`) were read as the text. Both readers hit the 5-hour
limit after one unit each and were resumed with SendMessage after the reset. The reviewer read
the texts while they ran and checked the doubtful claims on the web (`reviewer-facts.md`).

## Counts

| Unit | proposed | review | rejected | Claude changed / added |
|---|---|---|---|---|
| 71 hungarians-abroad | 71 | 63 | 0 | 6 (Article D still misquoted after the reader's fix; "part of the nation" is the 2010 national-cohesion law, not the Fundamental Law; four glued blanks) |
| 73 being-hungarian-citizen | 95 | 75 | 1 (vocabulary entries added by script) | 8 (the President decides every naturalisation; Article XXV has no duty to reply; six glued blanks) |
| 74 kormanyablak | 71 | 43 | 2 (rewritten: a time word only in a wrong option) | 6 (Ügyfélkapu+ restored: it replaced Ügyfélkapu in 2025, the reader had it backwards; two glued blanks found after applying; an absurd option) |
| 75 tenancy-contracts | 63 | 37 | 2 (rewritten: a time word only in a wrong option; vocabulary by script) | 5 (four glued blanks; a challenge target stated a fact the story doesn't) |

After applying, 31 more fill-blanks in these units still had the blank glued to a word (the
readers fixed this pattern in every earlier batch, here only partly): all made whole-word blanks
and their hints adjusted. A fixer now does this and refuses rather than guesses:
`scripts/fix_glued_blanks.py <course> <level> [<stem prefix>] [--apply]` (the whole of B1 and B2
now report none).

Merged and applied: 297; 64 vocabulary entries (`unmet-added*.txt`), 24 checklists, 24
challenges (1 changed), 57 glosses (`dictionary*.txt`). Reader tokens (resumed runs): A 304,985,
B 275,005.

## Facts (verified on the web; sources in `reviewer-facts.md`)

Article D quoted as the Fundamental Law reads it ("az egységes magyar nemzet összetartozását szem
előtt tartva"); Kolozsvár not a Székely town; the Selye János Egyetem's role, the V4's founding
(1991, four from 1993), Schengen (Romania from January 2025; Serbia and Ukraine outside); the 2010
naturalisation rules and the dispute with neighbouring governments named in one line; Article XXXI
without "szent"; compulsory schooling "to the age set by law"; the oath paraphrased, with the
pledge alternative; the exam described as the constitutional-basics test (the course's "thirty-six
units" dropped); the appeal deadline 15 days, address registration within 3 working days;
Ügyfélkapu+.

**For the user:** the citizenship oath's exact wording (Act LV of 1993 § 7 (4)) could not be
retrieved (the law databases refused the fetch tools), so Unit 73 paraphrases it; quote it only
after checking the text. Present-day procedures (the naturalisation figures, Ügyfélkapu+, fees,
deadlines) are as of the sources in October 2026.

## After applying

- `unmet-words.js`: 64 words listed; 27 left are lookup misses (*-hat* forms, split verbs, *-va*
  forms, comparatives).
- `check_unit_refs.py`: no recap reference to check.
- `check-content`: 0 errors; 14 `vocab-unused` stems accepted at freeze.
- `validate-content --changed` passes; `--warnings` at the baseline.
- Audit: every story word has a gloss.
- Walk 24/24 with challenges. HU B1 is 75/75 frozen.
