# HU C1 culture history rewrite, round 1: Culture Units 25–30 (2026-11-17)

User's decision (2026-11-17): Units 25–36 are rewritten as history of 2010 to spring 2026. Round 1: constitutional-breakdown, media-capture, healthcare-crisis (agent A); railway-decay, cultural-policy, pendulum-politics (agent B). Brief `scripts/templates/edit-hungarian-c1-history.txt`, prompts here.

- Agents (Sonnet, edit in place, three units each): A 410,757 tokens on its resumed run (its first run, stopped by the 5-hour limit, was not reported); B 321,117 (18.5 min). Both stopped by the usage limit once; A resumed with SendMessage after the reset.
- Every text, screen, item, goal and challenge rewritten; new neutral dated unit, lesson and story titles (unit ids and skill slugs unchanged). check-content 0 errors / 0 suspects in all six before freezing (3 accepted `vocab-unused` later), `check_c1_forms` 0, `validate-content` passes. 36 challenges, 42 glosses.
- Reviewer's fact changes (`reviewer-facts.md`): branch lines (10 lines from 1 Aug 2023, MÁV, not "the ministry"); motorway concession (May 2022, ~1,200 km, most of the network); Budapest–Belgrade dates softened, "Serbian section" narrowed to Belgrade–Novi Sad; PKÜ founding softened; EP 2022 "electoral autocracy"; removed as unconfirmed: Semjén as sponsor of the 2023 chamber law, the hospital-debt figures (53 hospitals, 35 suppliers, 98.4bn), the Klubrádió year, the 37 % and 70 % targets, the nurse survey and emigration figures, the 700bn programme cost; the items, goals and challenges that repeated them rewritten. Backticks in screens replaced by italics (47).
- The combined unit readings of all six restitched, with neutral Hungarian titles and summaries (the agents were told not to touch them; the reviewer missed this for 28–30 at first and caught it at round A's report).
- Walked 84/84 (with Culture Units 1–8): the first run failed 6 lessons because a one-time Guide note under a short story covers the Continue button (`engine/guide.js`, `lesson-tap-word`); the walk now closes it like a learner would. **For the user:** the note covering Continue is a small real UI defect.

## Open
- **For the user:** the vocabulary skills of these units keep one-sided titles in `skills/hu.json` (`c1-constitutional-breakdown-vocab`, `c1-media-capture-vocab`, `c1-healthcare-crisis-vocab` …); the skill list is frozen, so retitling needs your sign-off.
- Round 2: Culture Units 31–36 (historical-revisionism, judicial-independence, literary-canon, mta-ceu, pegasus-scandal, civil-society).

# Round 2: Culture Units 31–36 (2026-11-17)

- Agents: A (historical-revisionism, judicial-independence, literary-canon) 434,742 tokens, 27.5 min; B (mta-ceu, pegasus-scandal, civil-society) 400,460, 24.7 min; ~140k a unit. No usage-limit stop. The "no figures unless supplied" note held: neither text carried an unsourced sum or count.
- All six units 0 errors / 0 suspects, `check_c1_forms` 0 (mta-ceu's *feltéve, hogy* / *kivéve, ha* are known from core Unit 7), 36 challenges, 42 glosses, combined readings restitched with neutral titles.
- Reviewer's fact changes: Kósa Lajos spoke on 4 Nov 2021 as chair of the defence committee (not "early 2022, National Security Committee chair"); the unconfirmed Jan 2022 committee hearing and "classified until 2070" removed; teachers' civil disobedience from autumn 2022; CEU founding place; the occupation memorial: plan known early 2014, put up July 2014 (not "construction began July 2014, then protests"); Szépírók Társasága founded 2001 (not 1989); case transfer annulled with the transitional provisions at the end of 2012 (45/2012), not July 2012; administrative-courts law dropped in 2019 (month removed). Items, goals and challenges that repeated them rewritten.
- Unit 25 (frozen) used *Országos Bírói Hivatal*; the office is the *Országos Bírósági Hivatal* (reader A's catch): unfrozen, fixed, refrozen.
- Walked 42/42 (round 2 and Unit 25); all seven frozen. **The C1 culture track's Units 25–36 are done.**
