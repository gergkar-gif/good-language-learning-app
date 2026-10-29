# HU B1 citizenship batch 48-54: reviewer's notes (Claude, 2026-10-29)

Units 48 `rakosi-era`, 50 `revolution-1956` (reader A), 52 `kadar-era`, 54 `regime-change`
(reader B). Both readers ran without hitting a limit. The reviewer read the 20 segments while
they ran and checked the doubtful claims on the web (`reviewer-facts.md`, with sources).

## Counts

| Unit | proposed | review | rejected | Claude changed / added |
|---|---|---|---|---|
| 48 rakosi-era | 78 | 49 | 0 | 1 (*andezitet* → *követ*: rock type not confirmed) |
| 50 revolution-1956 | 92 | 56 | 0 | 5 (executions "230–350"; "összedrótozott kézzel" dropped; reburial ~250,000 and 23 October "ma nemzeti ünnep"; one Stalin-statue answer; the "25 méteres" statue) |
| 52 kadar-era | 123 | 76 | 0 | 3 (the slogan's unconfirmed venue dropped and executions as in Unit 50; "kádári alku" in the consolidation item; a length give-away the reader left in 02.ex04), 7 hand-made checklist sections dropped |
| 54 regime-change | 129 | 94 | 0 | 5 (reburial crowd ~250,000 in segment, screen, two items and gloss), 7 hand-made checklist / goal sections dropped |

Merged and applied: 408; 62 vocabulary entries (`unmet-added*.txt`), 24 checklists (built by
`add_missing_checklists.py` from the readers' rewritten goal lines), 24 challenges, 100 glosses
(`dictionary*.txt`). Reader tokens: A 321,255, B 373,014 (~175k a unit).

## Facts (verified on the web; sources in `reviewer-facts.md`)

Wrong in the segments and fixed: Recsk an internment / forced-labour camp, not a death camp;
*kékparfás* → ÁVH under Péter Gábor; Rajk foreign minister when arrested (interior minister to
1948), executed 15 October 1949, rehabilitated 1956, reburial crowd an estimate; the 1949
arms replaced the 1946 Kossuth arms, not a "thousand-year royal" one; Nagy's 28 October
announcements were on the radio; the Stalin statue's bronze was 8 m; executions after 1956 an
estimate (230–350) in both Units 50 and 52; the reburial of 16 June 1989 about 250,000 (not
300,000) in Units 50 and 54; the 1982 debt (about $10bn, not over $20bn; ~$20bn by 1989);
the red star came off the Parliament in 1990, after the proclamation; Horn and Mock cut the
fence in June 1989; about 600 crossed at the Pan-European Picnic; the Roundtable agreement was
not signed by the SZDSZ and Fidesz; the MDF won the most seats (not "won").

Kept as written after checking: the summer 1951 deportation to the Hortobágy camps (the
border-zone deportations of June 1951 went there).

Judgements removed or named as views: "a forradalom győzött" (now *átmenetileg*), "a kommunizmus
erkölcsi bukása", the 1956 victims' blood opening the way to "today's Magyar Köztársaság", the
"kádári alku" (now "sok történész ... mások szerint leegyszerűsített"), "goulash communism"
covering up the lack of freedom, the "first domino" of the border opening (now "sok
történész szerint hozzájárult"), praise of Orbán's 1989 speech (now: he demanded the Soviet
withdrawal), "a vérontás nélküli forradalom példája".

**For the user:** invented speeches of real people stay as voice lines (Kádár, Aczél, Nyers,
Szűrös, Horn, Antall, Göncz), none taught as fact; Orbán's and Nagy's (4 November) lines are
close to the record. Two listed words are used nowhere in their unit after the rewrites:
*üdülőhely* (`b1-rakosikorszak-05`, from a deleted option) and *Hazafias Népfront*
(`b1-kadarkorszak-01`, unused since the venue was dropped); accepted at freeze, say if they
should go.

## After applying

- `unmet-words.js`: 62 words listed; 14 left are lookup misses (participles, *-hat* forms,
  comparatives, split verbs, date suffixes after digits, a name).
- `check_unit_refs.py`: only the known *leg-* false positive.
- `check-content`: one length give-away the reader left (02.ex04, rewritten); 0 errors; 17
  `vocab-unused` stems accepted at freeze.
- `validate-content --changed` passes; `--warnings` as after batch 40-46 (the open
  `concessive-postpositions` line only).
- Audit: every story word has a gloss.
- Walk 24/24 with challenges.
