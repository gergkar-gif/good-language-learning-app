# HU B2 core batch: Units 41, 43, 45 (reader A) and 47, 49, 51 (reader B), 2026-11-04

Both readers hit the 5-hour Sonnet limit and were resumed after the reset (09:50 UTC).
Usage on the resumed runs: reader A 414,362 tokens, reader B 405,537 (~136k a unit if
cumulative).

## Counts

| Unit | baseline e / s | proposed | review | rejected | Claude changed / added | after |
|---|---|---|---|---|---|---|
| 41 `economic-cycles-crisis-adaptation` | 15 / 1 | 101 | 73 | 1 (a recap with unescaped quotes; rewritten) | builder *felükre* → *felére*; 4 b2-21-04 preverb items rewritten (below); *kilábal*, *kétszeres*, *százszoros* listed | 0 / 0 |
| 43 `demographics-generations-life-course` | 7 / 0 | 86 | 60 | 0 | *öregség*, *írónő* listed; a recap unit (*közben*, A1 Unit 33) | 0 / 0 |
| 45 `urban-space-architecture-coexistence` | 23 / 0 | 86 | 59 | 0 | screen example; 2 *révén*/*segítségével* wrong options (one my own duplicate, caught by check-content); 3 items take both *amelynek révén* and *amely révén*; 6 items back on `b2-relative-postpositions` (below); 3 recap units; 4 words listed | 0 / 0 |
| 47 `ecology-infrastructure-stewardship` | 21 / 1 | 103 | 71 | 1 (a *mindig* tell; rewritten) | Tüskevár relabelled (below); b2-24-02-practice-4 category grammar; a recap unit (*céljából*, B1 Unit 48); 18 words listed | 0 / 0 |
| 49 `law-justice-constitutional-principles` | 14 / 1 | 100 | 69 | 0 | *kiszámíthatóság*, *korlátozás* listed; deadlines checked (below) | 0 / 0 |
| 51 `pluralism-heritage-minority-perspectives` | 12 / 1 | 93 | 62 | 0 | *volt választásunk egymás iránt* (not idiomatic: *iránt* takes a feeling or attitude) → *felelősséget éreztünk egymás iránt* in the story (2), reading-3 and the challenge; *szétoszt*, *értékel* listed | 0 / 1 accepted |

567 fixes applied, 36 challenges (1 target rewritten, above), 32 words listed, 154 dictionary
entries (140 lemmas, 14 surface forms). Accepted at freeze: `vocab-unused` b2-26-02
(*szétoszt* is used split, *osztják szét*; *értékel* only in the consolidation, which has no
list). Walk 36/36 with challenges. No new B2 validator warning. B2 26/72 frozen.

## Decided by the user (2026-11-04)

- **Unit 41, b2-21-04:** the lesson's screen teaches *átalakul, leépül, felzárkózik,
  megszilárdul* as preverb contrasts, which is `b2-figurative-preverbs` (Unit 55). The user
  chose to rewrite the 4 items rather than move the skill: controlled-2 asks for the verb
  meaning "to catch up"; controlled-3 no longer contrasts one verb's preverbs (*állt át / le
  / fel*) but three unit verbs (*átalakult / felzárkózott / kilábalt*); controlled-4 and
  check-1 keep the recall of *megszilárdult* with the hint "became stable". All four tag the
  unit vocabulary. The screen still presents the verbs (as words, with the reader's recap).
- **Unit 45:** `b2-relative-postpositions` `taught_in` → **b2-23-01-a-gr** (from a later
  lesson; noted in `skills/frozen-hu.json`). Of the 8 b2-23-01 items the reader retagged to
  `relative-clauses-aki-ami-amely`, 6 test pronoun + postposition (*amely mellett*, *amely
  által*, *amely felé*; wrong options put a case on the pronoun) and went back; controlled-2
  and -3 test the human/non-human pronoun (*akik között* vs *amelyek között*) and keep the
  reader's tag.

## Recurring, scripted

- **Category against the tag:** a reader's fix left `category: vocabulary` on an item tagged
  with a grammar skill (b2-24-02-practice-4), found only by `validate-content.py --changed`.
  Second time in B2 (b2-12-03-practice-4 in batch 17-27). `check_fixes.py` now runs the
  validator's exercise-metadata check on every item a fix touches and rejects a mismatch.
- **Full restitch by accident:** `stitch_track_unit_stories.py` with no argument restitched
  all 85 unit readings again (reverted with `git checkout`). A bare run now refuses; the full
  run needs `--all`.

## Judged by Claude

- **Classics** (`reviewer-facts.md`): b2-24 *Tüskevár* relabelled "Adaptation inspired by":
  Matula's talk of river regulation ruining the Zala filter and letting the water back is the
  1980s Kis-Balaton reservoir debate, not the 1957 novel (reader A's note). The other five
  keep the book's characters and setting with an invented conversation, as in earlier
  batches (*Sorstalanság*'s scene with Steiner and Fleischmann is the novel's last chapter).
- **Present-day facts, Unit 49:** the 15-day appeal (Ákr. 118. §) and the 30-day statement
  of claim (Kp. 39. §) hold; **Unit 51:** 13 recognised nationalities (Nemzetiségi tv., annex
  1; consolidated state in force to 2027-06-30) holds, and reader B's *Tolna* for *Bakony* (not
  a county) is right. Sources in `reviewer-facts.md`; njt.jog.gov.hu is outside the session's
  network allowlist, so the statute texts themselves were not read.
- **Recaps** (`check_unit_refs.py`): 6 wrong units fixed (*harmad* A2 Unit 2, *közben* A1
  Unit 33, *ami* A2 Unit 12, *amely* B1 Unit 10, *révén* B1 Unit 22, *céljából* B1 Unit 48);
  the two bare recaps checked by hand (*-nként* A2 Unit 14, participial phrases B2 Unit 3).
- **Unmet words after applying:** 71 hits; 32 common words listed on the lesson where they
  first appear; the 28 left are comparatives of met adjectives (*gyorsabb*, *kevesebb*),
  split or preverbed met verbs (*megmondtam*, *osztják*, *tehetünk*) and deliberate wrong
  forms (*túllépésében*, *megismerné*, *betartó*).
- Reader B's note on b2-25-03 (*méltányosság* is mainly an authority's power, not a court's)
  left as it is: the screen's own example is an authority remitting a fine.

## Not covered

No native speaker's eye; speaking steps and spoken challenge answers not checked by the walk.
