# Second read: hu a1 numbers-personal-information (Sonnet, 2026-10-09)

Report-only read of the unit as Antigravity committed it unfrozen
(`98fdde762`), checked and filtered by Claude. Fix every item below, re-lock
where tags change, then freeze. "Met" follows `docs/unit-finish-brief.md`
step 4.

## Words and forms used before they are taught

- *címem* ("my address") is never taught; a1-18 grammar has only *Mi a címed?*. Used in `a1-18-controlled-2`, `a1-18-practice-3`, `a1-18-writing-2`, the a1-18 challenge target and goal, and the story. Add *A címem Kossuth utca 10.* as an example on the a1-18 address screen (that makes it met), then use one spelling everywhere: `a1-18-writing-2` has *A címem: Kossuth utca 10.* (colon), the story and challenge have none. Drop the colon.
- *telefonszámom* likewise: add *A telefonszámom …* as an example on `a1-19-a-gr`, or take it out of the a1-19 challenge target.
- `a1-17-intro-2` (*Which means "years old"?*): wrong options *éve*, *évben* are unmet. Use met words (*hány*, *szám*).
- `a1-17-practice-2`: *Harminc év vagyok.* uses unmet *év*; *Vagyok harminc.* breaks two things (drops *éves* and moves the verb). Use one-fault near misses, e.g. *Harminc éves vagy.* (wrong person).
- `a1-17-controlled-4` (options *cím*, *utca*) and `a1-17-practice-7` (wrong reply *Kossuth utca 10.*): *cím*, *utca* are first taught in a1-18. Use met words (*hány*, *éves*), and a met wrong reply such as *Jól vagyok.* (*Budapesten* is also a1-18).
- `a1-18-intro-1`: option *telefonszám* is first taught in a1-19. Use *szám*.
- `a1-18-review-1`: *Hány szám?*, *Hány év?* are not real phrases and *év* is unmet. Use real met questions (*Hol laksz?*, *Hogy vagy?*), keeping lengths close.
- `a1-20-check-1`: wrong option *Mi a neved?*: *neved* is unmet (same as *nevem* in the unit 3 fix list). Use *Hogy vagy?* or *Hol laksz?*.
- `a1-20-intro-2`: wrong option *Mi a számod?*: *számod* is unmet (only *telefonszámod* and *címed* are taught). Use *Mi a telefonszámod?* and keep its `ki-and-mi` entry.
- `a1-19-practice-7` and `a1-20-consolidation-16`: *Ez a te születésnapod?* is unmet and odd. Replace with an item from the unit (e.g. *Mi a telefonszámod?* with a wrong reply that answers something else).

## Misleading content

- `a1-20-b-gr` ("Basic Hungarian word order"), the `taught_in` screen of `basic-hungarian-word-order`, shows the learner an authoring instruction: *Keep the question and answer patterns learned in the unit intact. Do not add a new word-order system here.* Rewrite it to teach what the unit shows: the focus (the new information) comes right before the verb: *Harminc éves vagyok.*, *Budapesten lakom.*, and the question word takes that slot (*Hány éves vagy?*, *Hol laksz?*). Short text, the examples it already has.
- `a1-20-controlled-2` and `a1-20-consolidation-11` (*____ éves vagyok.*): `english` "I am one year old." fits only *egy*, but `answers` accepts 19 numbers, including unmet *két*. Make it a single answer: `english` "I am thirty years old.", `answers` ["harminc"], `hint` "thirty" not needed (the English gives it).
- Story `a1-unit-04`, line 26: *Harminckettő éves vagyok.* is wrong before *éves* (it is *harminckét*, and *két* is unmet). Meg is 30 everywhere else (`a1-17-dialogue-2`, `a1-20-dialogue-1`, the challenges): make it *Harminc éves vagyok.* (check the line is Meg's; if not, *Harmincnégy éves vagyok.*).
- `a1-20-writing-1`: "Write three pieces of personal information" is open but has one fixed model answer. Give the facts in the prompt: "Say you are 30, live in Budapest, and your address is Kossuth utca 10."
- a1-17 goal: *Hány éves vagy?.* (double punctuation).

## Metadata

- `basic-hungarian-word-order` is taught in a1-20 but tagged on earlier items that test no focus position (the `taught-later` errors): `a1-16b-practice-6`, `-7` (builders for *Harminc éves vagyok.*) → `cardinal-numbers`; `a1-17-controlled-3`, `a1-17-practice-4`, `a1-17-check-2` → the unit vocabulary skill. In a1-20, `a1-20-practice-4` and `-check-2` (*Mi a telefonszámod?*) are tagged word order while `a1-19-practice-4` tags the same sentence `ki-and-mi`: make all three `ki-and-mi`.
- `cardinal-numbers` before a1-16b (all of a1-16a): a registry question, not yours. The reviewer takes it to the user (`taught_in` should probably be `a1-16a-gr`). Leave these tags as they are.
- Re-lock after the changes.

## Goals, checklists, challenges

- `a1-16a`: goal and checklist line 2 say "ask *hány?*" but no exercise uses *hány*. Add one item (e.g. *____ szám?* … or a choice: which word asks "how many?": *hány* / *hol* / *ki*), tagged `cardinal-numbers`.
- `a1-16b` challenge: `canDo` is line 1 (eleven to nineteen) but the task is the tens. Change the task to the teens (*Tizenegy, tizenkettő.*… use teens the lesson teaches), keeping `canDo` = line 1.
- `a1-19` challenge: target *A telefonszámom: 06 30 123 4567.* in digits; the learner has to say the number. Write the target the way the story does, in met number words (*nulla hat, harminc, …*), and see the *telefonszámom* item above.
- `a1-19` checklist line 2 ("talk about birthdays"): nothing in the lesson teaches it beyond the word *születésnap*. Drop the claim, or reword it to what is taught.

## Not taken (no action)

- `a1-20-intro-1` vs `-intro-2` tagged differently (vocab vs `spatial-questions-hol-hova`): both are defensible; intro-2 asks for the *hol* question.
- `a1-17-dialogue-1`, `-2` wrong option *Harminc vagyok éves.* / *Vagyok harminc éves.*: ungrammatical orders, so no `distractor_skills`; vocab tag is fine.
- Near-duplicate items inside a lesson (a1-17 intro-1 / check-1 etc.): recall by design.
- The two `tell-punctuation` suspects (phone numbers start with digits): accepted, as you did.
- The story's birthday thread (*Mikor van a születésnapod? / Áprilisban.*): stories may run ahead of the lessons; no action.
- a1-16a/16b challenge cues naming the numbers in English: the cue gives the meaning, not the Hungarian; fine.
