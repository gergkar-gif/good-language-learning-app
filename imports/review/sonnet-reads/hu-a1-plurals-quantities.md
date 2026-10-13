# hu a1 `plurals-quantities`: second blind read, NOT YET FILTERED (2026-10-13)

After the pilot fix list was applied (commit 883cafc1). Checker 0/0, story
audit clean. Raw findings, condensed; still to be filtered by Claude
(paused by the user to assess token use).

## 1. Found by reading
- a1-37-b says after a vowel only -k (*kicsik*), but a1-39 drills *régi →
  régiek* with no comment → add the exception to a1-39-a (or soften a1-37).
  *kicsiek* also accepted by natives (a1-40-consolidation-7 `answers`?, unsure).
- a1-37-a harmony text: never says when *-ök* applies (a1-05 taught *sör →
  sörök*); calling *könyvek* an exception is misleading → "ö/ü words take
  -ök or -ek; learn each: *sörök*, *könyvek*".
- a1-36-a leads with *könyv*, which a1-37 then calls an exception → lead
  with *asztal*, *szék*.
- a1-40-voc / a1-40-a: *kell* "is needed / must": "must" invites the
  infinitive (a1-118) → "is needed".
- *is* (taught a1-80) in the a1-36-a example, a1-36 speaking step 2 and the
  story twice → drop *is* (unsure for the lesson's own example).
- a1-38-dialogue-1: *A nagy székek itt vannak?* → right answer *Nem, a kicsi
  székek ott vannak.* doesn't answer it (unsure).
- Story a1-unit-08: "Meg counts the chairs" then *Néhány szék*; here/there
  jar; a1-40-reading-1 "only a few" not in the text.
- Builders with natural alternative orders (parked, ROADMAP 148(b)).
- "X székek vannak" options break noun and verb (two faults?) (unsure).
- Near-duplicate items across a1-36/37 and the consolidation.
- a1-37-b tip wording "after the noun"; two-option items; a1-36-a table
  "a könyv van | the book is".

## 2. Metadata
- **`distractor_skills` on ungrammatical options** (*a nagyok asztalok*,
  *a kicsik székek*, *a nagyok ablakok*, *a régiek könyvek*, *az újak
  könyvek*): the spec gives ungrammatical options none. These entries were
  ADDED by the pilot fix list (arm A item), so that item was wrong: remove
  `"0"` in a1-38-introduce-2, -controlled-4, -dialogue-1, -check-2,
  a1-39-practice-1, a1-40-consolidation-13; keep `"1"` where it is a real
  predicate phrase.
- `egyutt-together` on 12 items that test *vannak* agreement with no *együtt*
  (a1-36 ×8, a1-40 ×3, consolidation-11): wrong skill; no *vannak* skill
  exists (frozen list: needs a decision).
- Adjective fill-blanks tagged `adjective-order-before-the-noun` vs unit
  vocabulary: pick one convention.

## 3. Challenges / goals / checklists
No defects; minor canDo/target drift on a1-36 and a1-38.
