# HU A2 units 35–38: Claude's review of the readers' fixes (2026-10-15)

Readers: A (units 35 `translative-case`, 36 `essive-formal`) 300.8k tokens, 19 min;
B (37 `sociocultural-pragmatics-customs`, 38 `lak-lek-suffix`) 280.0k tokens, 17 min.
Both readers' report-file writes were refused by the harness ("subagents should
return findings as text"); the reports below were saved from their replies.

`check_fixes.py`: 211 fixes, 0 rejected, 173 to review. Applied 210 (merged.json).

## Not taken

- B, unit 37, a2-183-b-gr: *Kovácsné Kati néni a szomszédunkban lakik* → *Kovácsné a szomszédunk*.
  The reader said *a szomszédunkban lakik* means "lives inside our neighbour"; it is natural
  Hungarian for "lives next door to us". Kept.

## Changed before applying

- a2-181-controlled-2: English "Here you go, ma'am" → "Here you are, Grandma" (the Hungarian now says *nagymama*).
- a2-182-controlled-1: *megmondani az időt* (unnatural) → *megmondani, hány óra van*.
- a2-182-practice-1: third option *Segíts nekem …* had the same fault as the second (informal); now
  *Legyen szíves, segíts …* (formal opener, informal verb).
- a2-182-dialogue-2: the reader's *Fizetni szeretnék! — Mást is kér?* was illogical; now
  *—Jó napot, uram! Mit ____? —Egy kávét kérek.* (answer *kér*).
- a2-185-consolidation-14: new wrong option *Szia, nagymama!* could be right for one's own
  grandmother; now *Szia, kedvesem!*.
- a2-187-check-2: *Nem baj, mindenben támogatlak* (no logic) → *Mindig itt vagyok, mindenben ____*.
- a2-187-a-gr: *félt* gloss "hold you dear" → "I worry about you / I fear for you".
- a2-187-b-gr: *Barátok, várlak titeket* → *Kedves barátok, …*.
- a2-188-dialogue-2: *Tessék, egyáltalán nem zavarsz* → *Persze, …*.
- a2-190-dialogue-2: *a peron mellett* → *a peronon*.
- a2-190-consolidation-4: new wrong option *Látlak téged nem.* had the same fault as *Látlak nem.*;
  now *Nem látok téged.* (indefinite with *téged*).
- a2-171-dialogue-2: *—____ vált.* (sentence-initial blank) → *—Jó ____ vált.*

## Applied, with a problem found afterwards

- a2-182-a-gr (B, recap opener): the text fix put unescaped quotes into the JSON
  (*as "Here you are"*); `check_fixes.py` did not catch it because check-content skips
  a file it cannot parse. Fixed by hand; `apply_replacements.py` now refuses a text fix
  that leaves a `.json` file invalid.

## Hand fixes after the readers (hand-fixes.json)

- Unmet words left by the readers' rewrites: a2-187-dialogue-2 (*amint*, *hazaérek*, *rögtön*),
  a2-188-controlled-1 (*sietned*), a2-188-dialogue-1 (*percet*, *lent*, *előtérben*),
  a2-184-dialogue-2 (*házigazdára*, taught a2-185), a2-182-writing-1 (*kinyitni* → *leülni*).
- a2-183 challenge: Carlos introduced himself as *García Carlos*; Hungarians keep a
  foreign name in its own order and the lesson doesn't say otherwise. Now Eszter's
  friend Horváth Katalin introduces herself.

## Dictionary and Reader

- Imported: *barkácsolás*, *nyelvtanár*, *húsleves*, *vendégpapucs*, *beljebb*, *koccintás*.
  The readers' *lát* "to see" and *meghív* "to invite" duplicated existing senses and were removed;
  *észrevesz* was already covered.
- `fill-dictionary-gaps.py` refused to merge ("could not reproduce the layout"): the dictionary
  is in `json.dumps` default layout, which `dump_like` didn't try. Added.
- The Reader read every *-lak/-lek* form as a noun compound (*látlak* = "to see + dwelling").
  `engine/morphology/hungarian.js` now has the *-lak/-lek* (and past *-talak/-telek*) rows:
  course-wide 7 fewer compound guesses and 2 fewer gaps; *félek*, *élek*, *telek*, *falak*
  unchanged; reader tests pass. check-content: *látlak* ×2 no longer flagged; *felébresztelek*
  (a2-190-consolidation-13, accepted) and *köszöntelek* (a2-195-consolidation-16, unit 39,
  next batch) now resolve to lemmas the vocabulary lists only as *-lek* forms.

## Reported, not fixed (registry is frozen: user's decision)

- `valik-verb` `taught_in` a2-171-a-gr, but *válik* is first presented on a2-172-a; a2-171's
  items use *vált* throughout (reader A).
- `lak-lek-suffix` `taught_in` a2-187-b-gr, but the suffix is presented and drilled from a2-187-a (reader B).
- `plural-possessive` `taught_in` a2-13-a-gr, which teaches only the 3rd person singular
  (*szülei*, *testvérei*); the other persons come in a2-191 (Claude, before the read).
- Story a2-unit-35 drills *három hétig*, *sokáig* and its question 3 asks *Mennyi ideig*:
  the terminative *-ig* is B1 (`terminative-case-ig`), though *-tól … -ig* is A1 (`tol-tol`,
  a1-154). Not changed (reader unsure; *három hétig* is everyday Hungarian). Decision needed:
  accept duration *-ig* at A2 in stories, or rewrite.
