# Second read: hu a1 greetings-basic-interaction (Sonnet, 2026-10-09)

Report-only read of the unit after Antigravity's redo (`2a88db810`), checked
and filtered by Claude. Fix every item below; each was verified against the
files. "Met" follows the rule in `docs/unit-finish-brief.md` step 4
(vocabulary list or grammar-screen subject at or before the lesson; a lesson
may use whole phrases from its own grammar examples).

## Words and forms used before they are taught

- `a1-06-dialogue-2`: Károly says *Én megyek. Viszlát!*; *megyek* is never taught. Use *Károly: Viszlát!* (the answer *Viszlát!* stays).
- `a1-06-intro-2`: wrong options *szívesen*, *bocsánat* are first taught in a1-07. Use met words (*jó napot*, *köszönöm*).
- `a1-06-review-2`: wrong option *kérem* is not taught in A1 before a1-102. Use *nem* or *jó*.
- `a1-07-intro-1` (*rendben*), `a1-07-intro-2` (*persze*, *tessék*): taught in a1-10. Use met words.
- `a1-08-check-1`: wrong option *Hol vagy?* (*hol* is taught in a1-13). Use a met phrase that isn't a duplicate of intro-1's options (e.g. *Jó napot!*).
- `a1-09-practice-5` and `a1-10-consolidation-16` (same item): the right answer *Mondom még egyszer, lassabban.* (*mondom* never taught) and the wrong *Nagyon szívesen, nincs mit.* (*nagyon*, *nincs* not taught). Right: *Még egyszer, lassabban!*; wrong: a met phrase of similar length (*Jól vagyok, köszönöm.*).
- `a1-09-dialogue-1`: wrong option *Szívesen, örülök, hogy látlak!* (*örülök*, *látlak* not taught). Use a met real reply that doesn't fit, e.g. *Jól vagyok, köszönöm. És te?*
- `a1-09-dialogue-2`: wrong *Viszontlátásra!* (not taught). Use *Viszlát!*.
- `a1-08-dialogue-1`: wrong *Viszontlátásra, szép napot!* (not taught). Use a met phrase, e.g. *Bocsánat, viszlát!*.
- `a1-10-dialogue-1`: *Mariann: Érted?*: only *értem* is taught. Rewrite the exchange so the prompt uses met words and *Értem.* still answers it, or move the item onto *Rendben* / *Persze*.
- `a1-10-practice-5`: *Kávét?* (accusative, not taught). Use *Kávé?* or *Egy kávé?*.

## Wrong options that give themselves away

- `a1-09-controlled-extra`: *Viszlát, légyszi.* and *Jó estét, légyszi.* are nonsense combinations. Use real phrases with another function (*Köszönöm!*, *Semmi baj.*).
- `a1-10-dialogue-2`: *Jó éjszakát.* is absurd as a reply to *Segíthetek?*. Use a real reply that fails on meaning (*Bocsánat.*).

## Duplicates, answers, hints

- `a1-10-check-1` and `a1-10-check-2` ask the same question back to back (so do intro-2 and controlled-2). Make check-2 test something else from a1-10 (e.g. *Tessék?* as "pardon?").
- `a1-10-practice-3`: add *Köszi* to `answers` (taught in a1-01 and a1-07).
- `a1-08-controlled-1`, `a1-10-consolidation-9` (*Hogy ____?*, hint "informal"): pin the person: hint *you (informal)*.
- `a1-06-practice-2`: gloss *daytime greeting* → *good day*, as in the vocabulary list.
- `a1-09-controlled-1` / `a1-10-controlled-1` (and their copies): make the question punctuation consistent.

## Metadata

- `a1-08-practice-4`, `a1-08-writing-1`, `a1-10-consolidation-19`: the whole-phrase builder and writing of *Hogy vagy?* are tagged `van-zero-copula`; a wrong answer there shows the phrase isn't known, so tag them with the unit vocabulary skill (`category` follows). Re-lock.

## Goals, checklists, challenges

- `a1-06`, `a1-07`: the second checklist/goal line is the generic *I can handle a short basic interaction in Hungarian.* Write lesson-specific lines (a1-06: choosing the greeting for the time of day; a1-07: answering thanks and sorry).
- `a1-10-consolidation` challenge: `canDo` mentions saying goodbye; the target has none. Add a goodbye to scenario, prompt, cues, target and english, or align the checklist line.
- `a1-10` challenge: *Rendben. Persze.* is not one natural reply. Answer with one of them, or make it two exchanges.

## Not taken (no action)

- *Jó vagyok* as the wrong option in `a1-08-check-2`: the *jó* / *jól* contrast is the lesson's point.
- `a1-07-practice-3` (*hol van a kávé*) and `a1-10-practice-3` (*a kávéd*): whole phrases from the lesson's own grammar examples; allowed.
- `a1-10-practice-4` builder word order: ROADMAP 148(b), parked.
- Speaking steps reading speaker labels aloud: an engine issue, fixed by Claude.
