# HU A2 units 39–44: Claude's review of the readers' fixes (2026-10-15)

Readers (Sonnet, three units each):
- A: 39 `plural-possessed`, 40 `inflected-postpositions`, 41 `inflected-infinitives-necessity`. 385.8k tokens, 23 min. Report file written (`report-plural-possessed.md`).
- B: 42 `post-office`, 43 `banking`, 44 `pharmacy`. 449.3k tokens, 33 min. The report-file write was refused, so Claude saved `report-post-office.md` from the reply.

Fixer (Sonnet): unmet words left in 42–44, 212.0k tokens, 12 min.

`check_fixes.py`: 426 fixes, 0 rejected, 320 to review. All 426 were applied (`merged.json`). The pharmacy auto list's English line for the 220-a example collided with Claude's own; the auto copy was dropped.

Applied reader fixes per unit: 72 / 70 / 58 / 77 / 74 / 75.

## Changed before applying

- a2-195-intro-2, a2-195-check-1, a2-195-consolidation-11: the new wrong options *ruhámat* and *ruhánkat* could be read as "my/our clothes" (collective *ruha*). They are now wrong in person (*ruháidat*, *ruháitokat*). The `distractor_skills` added with *ruhámat* was dropped.
- a2-193-practice-2: the English still said "flowers" after the sentence changed to *házak*.
- a2-198-writing-1: "Thank you for your help, without you I can't solve this" mixed help already given with a present inability. Now *Köszönöm, hogy segítesz, nélküled nem tudom megoldani …*.
- Recap openers in three places used lesson numbers as unit numbers ("from Unit 13" for a2-13, "Unit 14", "Unit 118"). They are now "Unit 3", "Unit 21", "from A1" and "Unit 10" (post-office 207-b). Added to the rulebook § 6.
- a2-211-writing-1: the rewrite kept the unmet *elmagyarázta*. Now *az ügyintéző megnézte a napi limitet*.
- a2-217-practice-2: *Az orvos felírta, a gyógyszerész pedig …* had no object. Now *A gyógyszerész a gépen azonnal látta a ____.*
- a2-220-a example: *Hétfő előtt …* (reader) is now *Munka előtt orvosi ellenőrzésre kell mennie.*, with its English.
- a2-unit-42 question option: *amelyet SMS-ben kapott* (relative *amely*) is now *az SMS-ből*.
- a2-215-practice-2 (fixer): *kaptam a ____ a számlámon* is now *megkaptam … a számlámra*.

## Hand fixes after the readers (units 39–41)

- Unmet words replaced: *lakáskulcs* (191-controlled-1, 195-consolidation-6), *születésnapi*, *legközelebbi*, *Készen állsz az indulásra*, *megkeresem*, *kabátzseb*, *összepakolom* (before a2-195), *iratom* (191), *zaj*, *hagytam*, *eljönnek* (192), *így* (197), *Nem érek rá* (205-consolidation-15).
- Added to lesson vocabulary: *elmegy* (a2-198), *megtesz* (a2-199), *siet* (a2-202).

## Fixer (units 42–44)

The fixer handled about 250 suspects:
- 115 reworded with met words.
- 63 topic words added to the first lesson that uses them (e.g. *kijelző*, *sorszám*, *bankkártya*, *tranzakció*, *diszpécser*, *antibiotikum*, *háziorvos*).
- 34 accepted: forms of met lemmas the checker misses (*megkaptam*, *adnom*, *-het* forms) and vocabulary on screens only.

Claude read every changed Hungarian line. Accepted lists for all six units are in `accept.json` and stored with each frozen unit.

## V4 fold (docs/hu-a1-a2-cefr-gap-proposal.md)

Police and lost-property language went into a2-219 (urgent care and 112):
- A section on screen b covering *rendőrség* (known), *Ellopták a táskámat!*, *Elveszett a telefonom.*, *Feljelentést szeretnék tenni.* and *Talált Tárgyak*.
- Vocabulary: *ellop*, *feljelentés*, *Talált Tárgyak*.
- Four exercises: controlled-5 (matching), practice-5 (*ellopták*), dialogue-3 (*Feljelentést szeretnék tenni*) and check-3 (where to ask for a lost umbrella).
- A third goal and checklist line.

The emergency/police/lost-property fold is now done for `pharmacy`. `problems-requests` (unit 31) has none of it and stays frozen.

## Dictionary

Imported 26 lemmas with `fill-dictionary-gaps.py import`. Nothing existing was changed or removed.

The words: *lakáskulcs*, *végigtapogat*, *Bálint*, *Halászbástya*, *napsütéses*, *projekttervezet*, *túlórázik*, *feladóvevény*, *hatjegyű*, *csekkbefizetés*, *csomagautomata*, *lepecsétel*, *nyitókód*, *nyugtáz*, *sorszám*, *adókártya*, *bankfiók*, *lakcímkártya*, *mappa*, *mobilbankos*, *számlanyitás*, *torokfájás*, *torokgyulladás*, *ügyeleti*, *tolóablak*, *ügyelet*.

Dropped as duplicates of existing senses: *nyugszik* "to rest", *ad*, *ér* "to reach", *alszik*, *hazamegy*.

## For the user (registry is frozen)

- **miatt.** Inflected *miatt* is presented and drilled in a2-199 (11 items plus 2 in the consolidation). Plain *X miatt* is used in passing:
  - on two screens (a2-199-a, a2-202-a);
  - in about 9 items in units 40–44 (a2-200-consolidation-18, a2-202-check-2, a2-204-writing-2 tile, a2-205-consolidation-9, a2-215-controlled-2, a2-215-consolidation-18 and -20, a2-220-controlled-1, a2-220-dialogue-2);
  - on the a2-220-a screen and its speaking step;
  - in a correct story option (a2-unit-43).

  No item is tagged `causal-postpositions`.
- **büszke / vigyáz … -ra** (`verb-government-ra-re`, B1) is drilled in a2-194 and a2-195 and in consolidation-10 (reader A).
- **Lexicalised -ó / -ható words** (`present-participle`, B1): *fájdalomcsillapító*, *lázcsillapító*, *gyulladáscsökkentő*, *torokfertőtlenítő*, *szopogató*, *kapható*. The banking vocabulary also has *elveszett* and *ellopott*. All were left as lexical words.
- **No skill covers past *kellett*, *szabadna* or *lehetne*** (a2-203-b, a2-204-b). These items are tagged `inflected-infinitives`.
- **Facts the reader doubted (not changed):**
  - yellow cheques "díjmentes" at the counter;
  - *személyi igazolvány és lakcímkártya* as the accepted ID;
  - "within 30 days" for disputing a debit;
  - the rounding table;
  - *adókártya* needed to open an account;
  - *104* offered as a wrong option for the European emergency number (104 is the real ambulance number; the question asks for the single European one).

## The user's decisions (2026-10-15, after this batch)

All five are recorded in ACHIEVED.md 153 ("Decisions after units 39–44").
- Plain *X miatt* is A2 and is taught on a2-199-a.
- A listed word with its case (*büszke valamire*) is an A2 chunk.
- Participle-shaped words that a lesson lists in its vocabulary are A2 vocabulary.
- No new skill for *kellett* or *szabadna*: a2-203-b and a2-204-b now recap known material.
- The facts were corrected as described in the ACHIEVED entry.

Police and lost property are now taught in unit 31 (a2-152-c) and recapped in a2-219.
