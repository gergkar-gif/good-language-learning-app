# Second read: hu a1 family (Sonnet, 2026-10-09)

Report-only read of the unit as Antigravity committed it unfrozen
(`05d778a5a`), checked and filtered by Claude. Fix every item below, re-lock
where tags change, then freeze. "Met" follows `docs/unit-finish-brief.md`
step 4.

`05d778a5a` changed only the challenges; steps 2 and 3 (reading every screen,
checking every exercise's metadata) found nothing, yet the read below did.
Run 1's review note applies: do steps 2 and 3 on every unit.

## Words and forms used before they are taught

- The "your" possessive (*-d / -od / -ed / -öd*) is taught nowhere, yet the unit uses *anyád* (`a1-26-practice-1`, `a1-26-dialogue-1`, `a1-30-consolidation-13`), *gyereked* (`a1-27-dialogue-2`), *bátyád* (`a1-28-dialogue-1`, `a1-30-consolidation-15`), *feleséged* (`a1-29-dialogue-1`, `a1-30-consolidation-16`), *testvéred* (`a1-27-dialogue-1`, `a1-30-consolidation-14`, the story), *húgod* (`a1-28-dialogue-2`). `possessive-suffixes` ("possessive suffixes across persons") is taught on `a1-26-b-gr`, which only teaches "my". **Add a short "your" section to `a1-26-b-gr`** (*anyád*, *apád*, *családod*, one table or two examples), which makes these items met and fits the skill. Keep the items.
- `a1-29-dialogue-2` (*Kik ők a képen? / Ők a szüleim.*): *kik*, *szüleim* unmet, *képen* first appears in a1-30. Rewrite in a *Ki ő?* frame (*Ki ő? / Ő a nagymamám.*) with a one-fault wrong option, and retag to fit.
- `a1-30-dialogue-1`: right answer *Igen, együtt vagyunk.* uses unmet *vagyunk*; wrong *Nem, egyedül vagyunk.* uses unmet *egyedül* and is nonsense after "many family members". Right: *Igen, együtt vannak.* (what the lesson teaches); wrong: a met one-fault reply.
- `a1-30-practice-6`: wrong option *Egy bátyáim van.* is an unmet plural possessive (`plural-possessive`, A2). Use a met one-fault form. Its `english` "I have one brother" also fits *Egy öcsém van.*: make it "one older brother".

## Misleading content

- `a1-27-check-1` ("Which means 'I have a son'?"): *Fiam van.* is also correct Hungarian. Replace it (e.g. *Nincs fiam.*).
- `a1-28-controlled-1` (*Ő a ____.*, *bátyám / öcsém / húgom*): *a öcsém* is ruled out by the article alone. Use consonant-initial options (*bátyám / nővérem / húgom*).
- `a1-26-dialogue-2`: wrong option *Nem vagyok család.* is absurd. Use a real reply that doesn't fit.
- `a1-27-dialogue-1`, `a1-28-dialogue-2`, `a1-30-consolidation-14`: wrong option *Nincs, van egy testvérem.* / *Nincs, van egy húgom.* contradicts itself. Use a real phrase that fails one way.
- `a1-27-practice-1` ("How do you say 'I have'?"): option *van + accusative suffix* is meta-language and the accusative is unmet. Make all options concrete phrases (*Van testvérem.* / *Vagyok testvérem.* / …).
- `a1-30-practice-1` (the accepted suspect): the stem names the answer and *either* is not a real option. Make it concrete: *Sok családtag van.* vs *Sok családtagok van.*, `teaches` `singular-after-numbers`, `{"1": "plural-nouns-k"}` (check the slug).
- `a1-26-practice-6`: *Szülő ő van.* breaks two things (order and a stray *van*). One fault per option.
- `practice-5` in a1-26 to a1-30 ("Which line comes just before …?"): *Szia!*, *Köszönöm.* give the answer away. Use real questions that fit a different reply (*Hol van?*, *Mi az?*, *Hány éves?*).
- `a1-29-practice-6`: "pointing at a photo of someone far off" contradicts the lesson tip (*ő* for someone present, *az* for a photo). Reword.
- Story `a1-unit-06`: the baby "held by Anna — her one-year-old daughter" is unclear (whose? Anna appears nowhere else). Cut it or give Anna a line.

## Metadata

- `kinship-possessives` vs `possessive-suffixes` (both taught on `a1-26-b-gr`) are used for the same shapes. Rule: a family noun + *-m* is `kinship-possessives`; `possessive-suffixes` only where the person contrast is the point (*anyám* vs *anyád*). Apply it across the unit: `a1-26-practice-1` (person contrast: stays `possessive-suffixes`), `a1-26-practice-4`, `-7`, `a1-26-check-2`, `a1-26-practice-2`, `a1-26-controlled-4`.
- `a1-28-controlled-1` and `a1-29-controlled-1` have the same shape (three possessed family nouns, wrong word = wrong meaning) but different tags. Both are word choices: `a1-family-vocab`, `vocabulary`.
- `a1-27-review-2` ("Which means 'my father'?") reviews a1-26: it keeps the reviewed skill (`kinship-possessives`), not the unit vocab.
- Retag the rewritten items (`a1-29-dialogue-2`, the three *Nincs, van egy …* items) to what their new wrong options show.
- Re-lock after the changes.

## Goals, checklists, challenges

- `a1-29`: line 1 / `canDo` "I can ask who someone is with *Ki ő?*", but the challenge never asks it (and *Ki ő?* is from a1-03). Make line 1 what the lesson adds (introducing grandparents, *nagymama*, *nagypapa*) and copy it to `canDo`.
- `a1-30`: line 1 / `canDo` "…combining this unit's possessive and 'to have' patterns": the lesson teaches *sok*, *egy*, *együtt*. Reword ("I can say there are many family members in the photo and that they are together."), copy to `canDo`. The goal's "we're *együtt*" implies unmet *vagyunk*: "the family is together".
- `a1-30-consolidation`: generic checklist (*I can recognise the main language from this unit.*). Write its own two lines (a1-20-consolidation is the model), copy the first to `canDo`.
- `a1-27` challenge: the scenario says "siblings or children", the task "a sibling, not a son". Make them match.

## Not taken (no action)

- *Az a nagypapám.* / *Az az anyám.* in a1-29: the a1-29 screen teaches it, so it is met there.
- Fill-blank `hint`s that gloss a new noun (*parent* for *szülő*): needed for a new word.
- `a1-28-practice-4`, `-10` builders and their tags: ROADMAP 148(b), parked.
- `a1-30-consolidation-11` repeating `a1-30-controlled-2`: deliberate reuse.
