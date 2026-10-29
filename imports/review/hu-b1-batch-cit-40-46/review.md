# HU B1 citizenship batch 40-46: reviewer's notes (Claude, 2026-10-29)

Units 40 `world-war-1`, 42 `trianon-1920` (reader A), 44 `interwar-years`, 46 `world-war-2`
(reader B). Both readers hit the Sonnet 5-hour limit before writing a file and were resumed
with SendMessage after the reset (3:30 UTC). While they ran, the reviewer read all 22 segments
and checked the doubtful claims on the web (`reviewer-facts.md`, with sources).

## Counts

| Unit | proposed | review | rejected | Claude changed / added |
|---|---|---|---|---|
| 40 world-war-1 | 90 | 53 | 2 (rewritten) | 2 (skill of *esett*; borders "megszűntek" → most of the country under foreign troops) |
| 42 trianon-1920 | 102 | 62 | 1 (rewritten) | 5 (population "csaknem kétharmadát"; *lett korlátozva* is a -va form; "sok iskolában"; the *országgyarapítás* sentence; the red-map scene) |
| 44 interwar-years | 84 | 46 | 1 (rewritten) | 6 (forms of address; the *fegyveres semlegesség* options; the paprika line; Bethlen's "motto"; *mintegy ötezer*; a pos `numeral` → `number`) |
| 46 world-war-2 | 89 | 53 | 2 (rewritten) | 7 (Teleki's letter; Horthy's broadcast without the made-up quote; Margit híd; *áldozatul esik* + dative; "hónapokig" siege → "hosszú"; the kidnapping on the morning of 15 October; a `vocabulary` item testing *-ban* → `grammar`) |

Merged and applied: 370; 62 vocabulary entries (`unmet-added.txt`), 24 checklists (10 template
first goal lines rewritten, `goal-lines.json`), 24 challenges (3 changed), 164 glosses
(`dictionary*.txt`). Reader tokens (resumed runs only): A 283,936, B 306,664.

## Facts (verified on the web; sources in `reviewer-facts.md`)

Wrong in the segments and fixed: general mobilisation (31 July 1914, not the day after the
declaration); the armistice (Padua, 3 November, by the army; Belgrade convention, 13 November,
for Károlyi's government); Trianon's population loss (about 63–64 %, not "half"); the bells and
the ten-minute stop on 4 June 1920 were at 10 a.m., not at the 16:32 signing; "Trianon-ima" is
the Magyar Hiszekegy (recited in many, not all, schools); the 2010 law made 4 June a day
(*Napjává*), not an *emlékév*; the Kolozsvár university moved to Szeged in 1921 under Vass
József, before Klebelsberg's ministry; Szent-Györgyi produced vitamin C from Szeged paprika in
quantity (he did not first isolate it from paprika); "Konszolidálni kell!" is not attested as
Bethlen's motto; the state of war was announced on 27 June 1941, the day after the Kassa
bombing; Teleki's quoted words were invented (his letter: *Szószegők lettünk*), and his death
concerned Yugoslavia, not the USSR; Horthy's broadcast is paraphrased (no verbatim text found);
his son was kidnapped that morning, before the broadcast; the Margit híd's Pest half fell on
4 November 1944, the Lánchíd and Erzsébet híd were blown on 18 January 1945.

Named as disputed rather than settled: who bombed Kassa; how far German pressure decided
Hungary's entry into the war; whether 1945 was liberation or occupation; how far the
revisionist gains tied Hungary to the Axis; Don losses (estimates 93,500 to 130,000);
*békediktátum* is now explained as the Hungarian name for a treaty Hungary could not negotiate,
not stated as fact.

**For the user (not settled by a source):** Apponyi's line *helyes-e öngyilkossággal megmenekülni
a halál elől?* is widely quoted but was not found in the sources searched; it stays as his voice
line and no item teaches it. The invented speeches of real people (Tisza, Károlyi, Benárd, Kós,
Bethlen, Klebelsberg, Szent-Györgyi) stay as voice lines, as in earlier batches; Wallenberg's
invented speech was replaced by a rescued person's line. Classroom counts differ between
sources (2,315 by 1928 or 5,784), so the text says *mintegy ötezer*.

## After applying

- `unmet-words.js`: 62 words listed; 19 left are lookup misses (stem changes such as *pokol →
  poklába*, present participles, *-hat* forms, split verbs) and one name.
- `check_unit_refs.py`: one false positive (*kénytelen* is taught in Unit 19, `b1-10-03`; the
  check looks for *kénytelen volt*).
- `check-content`: 0 errors; 28 `vocab-unused` accepted at freeze (`accept.json`). Three
  interwar words are used nowhere in the unit: *restauráció*, *jogkör*, *Szegedi
  Tudományegyetem* (kept on the list under the 2026-10-22 rule; say if they should go).
- `validate-content --changed` passes after one category fix. `--warnings` adds one line:
  `concessive-postpositions` now has 5 exercises (Unit 46 used postpositional *ellenére* before
  Unit 57, which teaches it; Unit 57 is frozen). To restore: one item in a citizenship unit after
  57 (batch 56-62 or later).
- Audit: every story word has a gloss except the place-name part *sur*.
- Walk 24/24 with challenges.
