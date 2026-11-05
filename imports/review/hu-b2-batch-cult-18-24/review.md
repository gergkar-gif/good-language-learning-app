# HU B2 culture batch: Units 18, 20 (reader A) and 22, 24 (reader B), 2026-11-05

No usage limit hit. Reader A 327,909 tokens (34 tool uses, 16.5 min), reader B 351,376 (34,
16.5 min): ~170k a unit. Text first, with a facts file per unit.

## Counts

| Unit | proposed | review | rejected (repaired) | Claude changed / added | after |
|---|---|---|---|---|---|
| 18 `mathematics-chess` | 104 | 85 | 1 (length give-away) | KöMaL solvers cut to Erdős (story and 02.ex06); a "check" note the reader left in the Polgár story removed; "több mint nyolcvan", "egy másik"; an absurd distractor; 7 words listed | 0 / 5 accepted |
| 20 `elite-education` | 74 | 58 | 2 (option-language) | the reader's *-at/-tat* rule rewritten; Babits cut from the Collegium members; a consolidation copy of 01.ex05 replaced; 18 words listed | 0 / 3 accepted |
| 22 `psychoanalysis` | 76 | 54 | 4 (goal fixes built on earlier ones) | **Csáth 1909 → 1912** (missed by the reader); **Magyar Pszichoanalitikus Egyesület**; Ignotus "alapító tagja" restored; 12 words listed | 0 / 2 accepted |
| 24 `kempelen-to-rubik` | 62 | 51 | 3 (length give-away) | 2 wrong options that were a second right answer (*-nak révén*, *-nak segítségével*); MoMA date unhedged; 22 words listed | 0 / 3 accepted |

316 reader fixes applied plus 4 reviewer text fixes and the society name in 4 files; 4 unit
readings restitched; 24 challenges; 59 more words listed (the readers listed ~200); 136
dictionary entries. Accepted at freeze: `vocab-unused` per lesson (culture words) and one
`answer-in-prompt` (the second *akár* of an *akár … akár* pair). Walk 24/24 with challenges.
validate --changed passes. B2 48/72 frozen.

## Found by the readers (applied)

- All four units re-teach core grammar: Unit 18 the concessive indefinites (B2 Unit 7), Unit 20
  the causatives (B2 Unit 19), Unit 22 the mediopassive (A2 Unit 31) and verb government,
  Unit 24 *-andó/-endő* and *révén/segítségével* (B2 Unit 23). Recaps added.
- Unit 24 lesson 02 used relative + postposition (*amelynek révén*, B2 Unit 45, later):
  rewritten with known forms; the item now tests *révén* after an unmarked noun.
- Unit 18: the "preverb inverts behind *is*" rule (*mérkőzött is meg*) removed and the items
  rebuilt without preverbs: a native speaker may accept both orders.
- Facts: Napoleon's game after Kempelen's death, Paradis not blind from birth, Jedlik's
  disputed priority, Lobachevsky's priority, Kosztolányi not a Collegium member, the orders
  dissolved in 1950, Pannonhalma Benedictine, Rubik's age and patent dates, "Café Ignotus" (no
  such café).

## Judged by Claude

- Facts: `reviewer-facts.md`.
- **A reader left a note in the content** ("(a jelenlegi helyzet ellenőrizendő)" inside the
  Polgár story): removed. Its only appearance so far; scripted if it recurs.
- **Readers' replacement claims and rules need the same check as the original:** the new
  *-at/-tat* rule was wrong, Babits and Haar/Riesz/Teller were unconfirmed.

## Not covered

No native speaker's eye; speaking steps and spoken challenge answers not checked by the walk;
the preverb-after-*is* order is avoided, not settled.
