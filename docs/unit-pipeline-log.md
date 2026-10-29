### 2026-10-27: HU B1 core units 43–53

- **Cost:** 326k and 421k for three units each (~109k and ~140k a
  unit), the lowest yet: half-size lessons and no session limit.
- **Same generator defects in every unit:** shared goal lines, a template
  first checklist line, glued blanks, builders whose `english` is "Build
  the sentence in the correct order.", screens that are bare phrase
  lists. The readers rewrote nearly every item; the checker counts
  (10–12 errors a unit) understate the work.
- **Unmet words after the read:** reader A did not run `unmet-words.js`
  (it said so). Run it yourself after applying each batch (step 5): here
  it found screen phrases reused in later lessons (*átértékel*, *kiállja
  az idő próbáját*, *megbízik*) that are on no vocabulary list; they go on
  the list of the lesson whose screen teaches them, and the resulting
  `vocab-unused` suspects are accepted at freeze.
- **`check_unit_refs.py`:** reader B wrote recaps as "*X* (A2 Unit 35)";
  the check now reads that form too. Its false positives are recaps of a
  form rather than a word (*kapcsolataimat*, *áttörést*, *adjuk hozzá*).
- **For the user:** 17 of the 36 core units (13, 17, 23, 29, 35, 37, 41,
  43–51, 55, 61, 65, 67, 72) have no skill whose `taught_in` is one of
  their screens, so what they teach (*lehet, hogy*, *kétlem*, *dönt
  vmiről*, *hiába* …) carries A1–A2 tags or the unit vocabulary skill.
  The skill list is frozen (ROADMAP 125).
# Unit pipeline: prompts, measurements, process reviews

How the reviewer (Claude) runs units through Sonnet agents, what each step
costs, and what changed at each review. **Every 2 finished units, the
reviewer reviews the process** (decided by the user 2026-10-13, under
time and usage pressure): add the units' numbers to the table, compare
with the previous rows, pick one or two changes that cut tokens or
reviewer work without losing defects, record them below, and apply them
to the next units. Repeated defects go into `docs/unit-agent-rules.md`
§ 6 at once; a recurring problem gets a script (§ "Script recurring
problems").

## Pipeline (current: the HU A2 method, course-neutral, 2026-10-16)

Read this before working on any unit. Agents read only
`docs/unit-agent-rules.md`; the reviewer (Claude) runs the steps below.
Every script here takes `<course> <level>` and works for hu, es-es and
es-latam. The HU A1 pass used regeneration first (route B); HU A2 used
read-first (route A), which costs about half per unit on real content.

**Choose the route per unit.** Route A (read-first) for real content.
Route B (regenerate, then read) for template stubs, or when a read finds
the unit beyond fixing (HU A1 unit 16: 40+ defects). Units missing from
the course are written from scratch with the "New unit" template (HU A2
units 45–47: ~361k a unit, ~19 fixes a unit afterwards).

**Spanish: one read for both courses.** es-es and es-latam share most
lesson files byte for byte (A1: 147 of 156 exercise files, 115 of 134
screens); the rest differ on purpose (*vosotros*/*os* forms in es-es,
*ustedes*, *jugo*, *tomar* in es-latam). Read the unit in **es-es**,
filter its fixes, then `python scripts/mirror_fixes.py <fixes> es-es
es-latam <out>`: it copies every fix whose text or id matches the sibling
file and lists the rest in `<out>.unmatched.json`. Read the unmatched list
and the es-latam-only files yourself (`cmp` the unit's files first; es-es A2
has one unit more, its last, `vosotros`, which has no es-latam copy). Then run
`check_fixes.py`, apply, lock, check, walk and freeze **per course**:
frozen state, accepted findings and tag locks are per course.

### 2026-10-28: HU B1 core units 55–65

- **Recap units are still the main reviewer fix.** Both readers wrote
  "You know *X* from Unit N" recaps from skill titles (*mivel*, *ezért*
  from A1 Unit 24, *amennyiben* from A2 Unit 13, *muszáj*); 8 were wrong,
  all caught by `check_unit_refs.py`. Its remaining hits across B1 are
  five known false positives (forms, and *nemcsak* spelled as one word).
- **Readers checked unmet words by hand, not with the script** (B said
  so); the reviewer run after applying found 17 hits, most of them
  inflected forms the lookup misses (*hagytak*, *érvelek*, *eljövök*).
- **Unit 65 `reported-speech` teaches nothing new:** it repeats Units 25
  and 53 (reader B). For the user, with the 17 skill-less core units.
### 2026-10-28: HU B1 core units 67–72 (core track finished)

- **Audit flag hid the dictionary gaps.** The reader template runs
  `audit-reader-coverage.js --story … --top 0`, and `--top 0` printed no
  "not in the dictionary" words (reader A, Unit 67, noticed). So the
  readers' dictionary lists only ever held the compound guesses.
  **Scripted:** a `--story` audit now lists every miss. Run over the 32
  core classics it found 62 misses; 44 were glossed.
- **Lemma-keyed glosses don't reach every form.** `fill-dictionary-gaps.py`
  stores a gloss under its lemma, so a form the morphology rules can't
  reduce (*feküdt*, *pátosszal*, *vasággyal*, *gúnnyal*) stays a gap after
  its lemma is added. Those went in as surface-form headwords
  (`word | word | pos | gloss`). The remaining misses are names.
- **Core track check, 2026-10-28:** all 36 core units frozen;
  `check-content` reports nothing unaccepted on any of them; walk
  216/216 with challenges. Not covered: the citizenship track (39 units,
  3 frozen), the B1 level checklist (run once the citizenship track is
  done), and the 17 core units that teach no registry skill.
### 2026-10-28: HU B1 core close-out (user's decisions)

The user took the four recommended options:
- **Skill titles reworded to what their screens teach** (slugs and tags
  unchanged): `kell-infinitive` "obligation with kell + infinitive",
  `mert-because` "causal clauses with mert", `kellene` "giving advice
  with kellene", `ha-clause` "conditional sentences with ha",
  `concessive-annak-ellenere` "concessive clauses with annak ellenére,
  hogy", and, found in the same check, `relative-clauses-aki-ami-amely`
  "relative clauses with aki".
- **`check_unit_refs.py` now counts a word as taught only where it is**
  (italicised on a grammar screen, other than the recapped word, or a
  vocabulary lemma; citizenship screens with a topic in the file name
  map to their lesson). It found 9 more wrong recaps (*amely* "from A2
  Unit 4" on six screens: it is first taught in B1 Unit 10; *bár*,
  *habár*, *majd*, *végeredményben*), all fixed. Its 12 remaining hits
  on B1 are false positives: recaps of a form (*adjuk hozzá*,
  *kapcsolataimat*, *áttörést*, *leg-*), multi-word phrases the screens
  quote rather than italicise, and *nemcsak* against A2's *nem csak*.
  The noun *bár* ('bar') on an early vocabulary list hides the
  conjunction from it, so *bár* was fixed by hand.
- **B2 forms removed from B1 screens:** Unit 63 (*olyannyira/olyan …,
  hogy*, *arról, hogy*), Unit 72 (*ugyebár*, *elvégre* → *hiszen*,
  *persze*; preverb inversion *olvastam el*). Rule added to
  unit-agent-rules § 6b.
- **Unit 65 is now "Review: Reported Speech"** (unit and lesson titles).
- **Skills for the units that teach none: none added.** Claude proposed
  *hiába*, *lehet, hogy / kétlem, hogy* and *az ember*; the user judged
  them vocabulary items, not grammar skills, so all 17 units keep the
  vocabulary tag. *Hiába* had a screen (Unit 35) but no item drilled it:
  three weak items (a weekday blank, an off-topic *azt mondta, hogy*,
  a Unit 9 recap blank) were replaced with *hiába* items, vocabulary-tagged.
- 12 frozen units were unfrozen for these edits and refrozen with their
  accepted findings; all 36 core units check clean, walk 216/216.
### 2026-10-29: HU B1 citizenship Units 64, 66, 68, 69

- **Present-day facts age:** the counties became *megye* again on
  1 October 2026, after the content was written; two frozen units and
  the mock exam carried the old term. The reviewer's segment read before
  the readers finish caught it in time to tell the reader of Unit 66.
  For present-day units, search for changes since the content was
  written (laws, office names, office holders) before calling a fact
  "standard"; the rulebook § 6b now says so.
- **Cost:** ~150k a unit for the civics units, ~180k for the long culture
  units (Unit 69's segments are the longest in the track).

### 2026-10-29: HU B1 citizenship Units 56, 58, 60, 62

- **Civics units are mostly "review":** readers marked nearly every fix
  `kind: hungarian` (451 of 482 to review). Reading them was still
  worth it: the reviewer found a misquoted Nemzeti hitvallás sentence,
  a contested museum used as a neutral fact, and the Fundamental Law's
  opening line attributed to the Avowal, each only in the review list.
- **A thin skill fixed by the next batch:** naming the missing item in
  the focus file (one `concessive-postpositions` item in Unit 58)
  worked first time.

### 2026-10-29: HU B1 citizenship Units 48, 50, 52, 54

- **Readers add checklists by hand:** reader B wrote checklist and
  consolidation-goal sections into the lesson files (14 fixes).
  `add_missing_checklists.py` builds them with the review step before
  them, so the reviewer dropped them. The rulebook now says so.
- **Cross-unit figures:** the same events (the 1956 executions, the
  1989 reburial) appear in two units read by different readers, with
  different numbers. The reviewer made them agree; the batch facts file
  is the place to fix one figure for the batch.
- **A fix that misses its own target:** one reader fix left a length
  give-away (`check-content` after applying caught it).

### 2026-10-29: HU B1 citizenship Units 40, 42, 44, 46

- **Reviewer reads while readers run:** both readers waited on the
  5-hour limit; the reviewer used the wait to read all 22 segments and
  verify the doubtful claims on the web. Most of the readers' "check"
  lines were then already answered, and four errors the readers left
  (the red-map scene, Bethlen's motto, the paprika line, the kidnapping
  order) were caught only by that read.
- **20th-century texts:** more wrong facts than the earlier units
  (dates a day off, invented quotes of real people, loaded labels used
  as neutral words). The rulebook § 6b now names the labels.
- **Thin skill:** retagging an item that used a form before its unit
  left `concessive-postpositions` at 5 exercises; the unit that teaches
  it is frozen, so a later citizenship batch adds one.

### 2026-10-28: HU B1 citizenship Units 32, 34, 36, 38

- **Lost run:** a container restart stopped both readers before either
  wrote a file; the rerun from the same prompts cost ~175k a unit. The
  prompt already says to write each unit's files before the next; a
  restart inside the first unit loses the whole read either way.
- **Generator pattern:** every lesson's ex02 in these units had garbled
  wrong options with several faults and "(Lesson N)" in the stem; both
  readers rewrote all twenty. The later citizenship units come from the
  same generator, so the focus file names it.
- **Cross-reader duplicates:** the two readers wrote the same goal line
  for Unit 36 L4 and Unit 38 L1 (the dual system); `checklist-shared`
  caught it after applying.
- **Invented quotes:** both readers kept the segments' speeches of real
  people (Kossuth, Deák, Andrássy, Bem) as illustrative dialogue; items
  must not teach them as facts (Unit 36 ex03 did).

### 2026-10-28: HU B1 citizenship Units 24, 26, 28, 30

- **Cost:** not measurable (the 5-hour limit before any file); the
  resumed runs alone were ~150k a unit. Fix counts ~108 a unit, lower
  than 16–22: these units' segments are shorter (~6.7k characters).
- **Cross-reader recaps:** reader B recapped *annak dacára, hogy* "from
  B1 Unit 24", a screen reader A rewrote in the same batch.
  `check_unit_refs.py` after applying caught it; reading the readers'
  lists together is not enough, so the script stays the last step.
- **Readers still put verbal nouns into their own new options** (Units
  24 and 30), now listed by `check_fixes.py` before merging, so they
  cost minutes rather than a second pass.
- **Scripted:** `add_challenges.py` stops counting "II." and "1848."
  as sentence ends (four refused targets about kings across batches).

### 2026-10-28: HU B1 citizenship Units 16, 18, 20, 22

- **Cost:** ~190k and ~220k a unit, up from ~160k in the first
  batch. Reader B's two units drew ~170 fixes each: every segment
  carried national-romantic lines and claims the items asked for but no
  segment stated, and every screen taught known A1–B1 material as new.
- **Recaps from skill titles, again:** *révén* "from A2 Unit 18" and
  *amint* "from B1 Unit 1" name the units of skills whose titles list
  the word (`postpositions-altal-reven`, `miutan-mielott`) but whose
  screens never show it. `check_unit_refs.py` caught both; the focus
  file now names them, with *amely* (Unit 10).
- **Hungarian grammar terms in question stems** (*megengedő kötőszó*,
  *névutó*, *ige*): unmet words and the wrong register for a learner.
  Reader A removed them, B only some; the focus file now says stems use
  plain questions or an English meaning line.
- **Scripted:** `add_vocab_words.py` (the list → fixes step for the
  history words, ~100 a batch), which refuses a `pos` the schema rejects
  and a multi-word lemma not tagged `expression`; my hand-made list had
  put `determiner` on *mindkét*.
- **Thin skill after a correct retag:** `historical-routines` (Unit 20,
  the only citizenship-taught skill with few items) fell to 5; caught by
  the `--warnings` diff, as the rulebook says.

### 2026-10-28: HU B1 citizenship Units 8, 10, 12, 14

- **Cost:** not measurable for the first run (the 5-hour limit hit
  both readers before any file was written); the resumed runs reported
  307k and 344k for two units each. The readers' fix counts (~84 a unit)
  match the core units', so the texts, not the items, drove the work:
  every segment had overclaims, mind-reading or national-romantic lines
  (*az egész keresztény Európa lélegzetvisszafojtva figyelt*, *dicső
  férfiág*, "saved Christian Europe") and facts the items asked for that
  no segment stated (Vajk, Koppány, Julianus, Rogerius, Körmöcbánya).
- **Recaps of *amely* again.** Reader A wrote "you know *amely* from A2
  Unit 4" on three Unit 10 screens; *amely* is taught on b1-arpadhaz-02.
  `check_unit_refs.py` would have caught it, but given unit ids it
  skipped every citizenship screen (it matched file stems without the
  topic suffix): **fixed**, and Units 2, 4, 6 rechecked clean.
- **Unmet words in the readers' own new options** (17–85 a batch since
  core 43–53, found only by the reviewer's run after applying): **scripted.**
  `check_fixes.py` now runs `unmet-words.js` before and after applying a
  list (B1 and up) and prints the words each fix brings, so they are
  listed while sorting, not after the merge. Tested on the pre-fix Unit 14:
  23 hits, the same words found by hand.
- **Change for the next batches:** the focus file names *amely* (Unit 10),
  *-ható* (Unit 61) and verbal nouns among the forms to watch in
  options, the three slips found after applying here.
- **Template slip:** reader B wrote "generator scripts" to build its fix
  JSON despite the template's "don't write your own tools"; its fixes were
  sound, so no change beyond the existing rule.

### Route A: read-first batch (HU A2, 2026-10-14 → 2026-10-15)

0. **Batch setup (Spanish, 2026-10-21):** `python scripts/batch_setup.py
   <level> imports/review/<course>-<level>-batch-<first>-<last> A=<n>,<n>,<n>
   B=<n>,<n>,<n> --focus <focus.txt>` adds both worktrees, writes every
   knowledge sheet, the setup.md (pairing, stories, baselines per course,
   files differing es-es/es-latam, the walk command) and both reader
   prompts from `scripts/templates/read-spanish.txt` (the Spanish template
   below, kept there now); write only the batch's focus notes by hand.
   **Knowledge sheets** (HU, or by hand): `python scripts/prior_knowledge.py <course>
   <level> <unit id> --out <worktree>/prior-<unit id>.md` for every unit
   (known grammar and words by unit, earlier screen titles, what this unit
   teaches, what comes later, same-family skills of the next level). ~7k
   tokens a unit; replaces "read the earlier units". Spanish sheets work
   since 2026-10-16 (the script read only HU screen ids before, and also
   missed HU screens such as `a1-16a-gr`, `a1-102-def-gr`).
1. **Readers:** two Sonnet readers at once, **three units each** (two
   when units are heavy; cost tracks the units' defects, not the count:
   ~113–145k a unit), one worktree each (`git worktree add --detach
   /home/user/parlour-read-a origin/master`, removed after), the
   "Read, paired" template below. Each reader writes per unit a fixes
   JSON, a challenges JSON (one challenge per lesson, consolidation
   included) and a report. **The harness often refuses the report write:
   save the report from the reader's reply** before anything else (the
   container can restart).
2. **Sort each fix list:** `python scripts/check_fixes.py <course>
   <level> <unit id> <fixes.json>` → rejected / review / auto. Read only
   the review list (target-language and unsure fixes) and the report's
   non-fix notes; readers propose wrong target-language text a few times a
   batch (rulebook § 6). Delete what you don't take from the review file.
   From B1 it also prints the unmet words each fix brings (`unmet-words.js`
   before and after; 2026-10-28): list them or, in core units, rewrite them.
   Words to list go through `python scripts/add_vocab_words.py <course>
   <level> <words.txt> <out.json>` (`stem | lemma | translation | pos`
   per line), then `apply_replacements.py` and `build_word_lesson_index.py`.
3. **Merge and apply:** `python scripts/merge_fixes.py <batch>/merged.json
   <each .auto.json and filtered .review.json>` (refuses when two readers
   fixed one item differently), then `python scripts/apply_replacements.py
   <batch>/merged.json`. Spanish: mirror here (above).
4. **Dictionary:** the readers' compound glosses (report group 5) through
   `python scripts/fill-dictionary-gaps.py import <reply.txt> <lang>`;
   it stores each under its lemma, so remove a gloss that only fits the
   inflected form (*barátnő* "with her girlfriends").
5. **Left over by hand:** remaining check-content errors and unmet-word
   suspects (a Sonnet fixer when there are many: HU units 42–44 had ~250,
   212k), then `python scripts/add_challenges.py <course> <level>
   <challenges.json>` per unit (it checks fields, level and `canDo`;
   check-content then reports unmet words in targets). Spanish: `python
   scripts/latam_challenges.py <drafts> <drafts.latam.json>` first (course
   words converted, *vosotros* drafts left out for the reviewer).
6. **Check, lock, freeze:** `python scripts/check-content.py <course>
   <level> <unit id>` after every hand edit; `python scripts/lock_tags.py
   <course> <level>/<unit id> --update --reason "..."`; `python
   scripts/validate-content.py --changed`; then `python
   scripts/validate-content.py --warnings` and compare the level's lines
   with origin/master; `python scripts/check_unit_refs.py <course> <level> <unit ids>` for the recaps readers write, and for B1 and above `node scripts/unmet-words.js <course> <level> --stems …` on the applied fixes (readers skip it) (warnings never fail, so a retag that leaves a
   skill under 6 exercises passes `--changed` silently: units 29–34 did
   this to `a2-review-work-past-opinions-vocab`, found only at the level
   checklist); `python scripts/freeze_unit.py <course> <level> <unit id>
   --reason "..." --accept "<check>:<id>:<why>"` for each deliberate
   suspect (consolidation replays, characters' names). Keep each batch's
   accept list in the batch folder: `--unfreeze` drops a unit's accepted
   findings, so a later unfreeze must pass them again.
7. **Records:** fix lists, reports, challenge drafts and accept lists in
   `imports/review/<course>-<level>-batch-<units>/`; a measurements row;
   a process review per batch (what recurred goes into rulebook § 6 the
   same day, anything seen twice gets a script, below). Commit, push.
8. **Walk:** `node scripts/walk_lessons.js <course> <level> --only
   <stems> --jobs 4` with `python scripts/dev-server.py 8131` running,
   after the first frozen units of a new course (an engine defect hits
   every lesson) and at the level checklist.

### Route B: regenerate, then read (HU A1, 2026-10-13)

Two units per Sonnet regenerator ("Regenerate" template; ~119k a unit
paired), each in its own worktree; take each commit with `python
scripts/take_unit_commit.py <course> <level> <unit id> <commit>`
(cherry-pick plus the `challenges.json` and `word-lesson-index.json`
conflicts); then a paired blind read and steps 2–7 of route A.

At most 2 agents at once (CLAUDE.md). Never let an agent bypass hooks.

### Script recurring problems (user, 2026-10-13)

When an issue shows up a second time, stop fixing it by hand or by prompt
and write a Python script, in the same session:

- **A recurring content defect → a check** in `scripts/check-content.py`:
  an error when the rule is certain (`ik-first-person`, `vocab-duplicate`,
  `ds-on-answer`), a suspect when it needs a reader's eye
  (`consolidation-copy`, `reported-question`, `glued-blank`,
  `article-blank`, `take-gloss`). Run it over the whole course at once:
  that is how hits in already-frozen units were found. Add the rule to
  `docs/unit-agent-rules.md` § 6 and AGENTS.md's checker list.
- **A mechanical fix that is always the same → a fixer script**, never a
  prompt. It must refuse rather than guess: write nothing unless every
  change matches exactly (`apply_replacements.py`), and run the checker
  after.
- **A recurring chore or conflict → a script**: `take_unit_commit.py`
  (cherry-pick + the two conflicts every parallel unit causes),
  `merge_challenges.py`, `freeze_unit.py` (refreeze keeps history),
  `walk_lessons.js` (play every lesson), `fill-dictionary-gaps.py merge`
  (dictionary additions survive rebuilds).
- Test a new check on the existing content before trusting it: look at
  its first hits, tighten it until they are real (false positives such as
  the B1/C1 *az* pronoun hits are noted in the process review), and record
  the count.

### Who does what: model choice (measured on HU A1)

(From 2026-10-14 the reader's JSON plus `check_fixes.py` replaces the
Haiku fixer for most lists; see Pipeline route A steps 2–3. Measure the first A2
pairs against the A1 rows before trusting the saving.)


| Job | Model | Why |
|---|---|---|
| Regenerate units (2 per agent) | **Sonnet** | Writes usable Hungarian; ~119k/unit paired. |
| Blind read (report only, 2 units per agent) | **Sonnet** | Finds ~10–25 real defects/unit; Haiku is too weak to find them. |
| Filter the read into a fix list | **Claude (main session)** | Readers propose wrong Hungarian a few times a level; only the filter catches it. Never delegate this. |
| Apply a filtered list, exact old → new | **Claude** with `apply_replacements.py` for short lists (≤ ~40 items); **Haiku** for long ones | Haiku applied 9/9, 11/11, 17/17, 19/19 exact items with no improvisation (74–131k); its only slips came from vague items in Claude's list ("only if that is the exact text"). Doing it directly is cheaper when the list is short. |
| Mechanical translation (e.g. story questions → English) | **Haiku** | 36 questions, 77k, 1 min, all right. Under ~10 items: Claude directly. |
| Build a tool (e.g. the walk test) | **Sonnet**, own worktree | 152k; review and rerun its output before taking it. |
| Judgement calls, registry/skill questions, anything for the user | **Claude**, ask the user | Never left to an agent. |

How to delegate:

- **At most 2 agents running at once** (CLAUDE.md); count before launching.
- Each agent gets its **own worktree** (`git worktree add --detach
  /home/user/parlour-<job> HEAD`) and the rulebook `docs/unit-agent-rules.md`
  only; the prompt templates below say the rest. Name exact files, stems,
  earlier units' ranges and what earlier units own.
- Every prompt says: never bypass hooks or change git/tool config; report
  only (reads); quote option text when naming an option; give fixes as
  exact old → new.
- An agent's report is a claim, not a result: check its Hungarian, rerun
  its commands, take its commit with `take_unit_commit.py`.
- **Usage limits:** a Sonnet weekly limit stops an agent within seconds
  ("resets <time>"). Tell the user and offer: wait, do it in the main
  session, or a weaker Haiku pass. Don't silently downgrade a read to
  Haiku.

### Before calling a level done

Count with the tools before giving the user any number, and say what is
not verified:

- `python scripts/freeze_unit.py --status`: every unit frozen.
- `python scripts/check-content.py <course> <level>`: 0 errors; every
  suspect fixed or accepted (copies, reported questions, glued blanks…).
- `python scripts/validate-content.py --warnings`: none for the level
  (`thin_ok` in `skills/<lang>.json` for a skill the user lets stay thin).
- `node scripts/walk_lessons.js <course> <level>` with
  `python scripts/dev-server.py 8131` running: every lesson plays to its
  summary with no console errors and no failed requests (TTS is stubbed;
  `--live-tts` and the live site can't be reached from the cloud
  container; the user checks audio). A walk counts only for content as it
  is now: rerun the units edited since their last walk (HU A2 units 1–24
  were walked 2026-10-14, then edited, and had to be rerun). Cost: ~2 s a
  lesson at `--jobs 4` in the cloud container (281 HU A2 lessons, ~9 min).
- Challenges are walked since 2026-10-21: each lesson's hand-written
  entry must be the one on screen and its target, typed, must pass the
  app's grader; a lesson with no entry (generated placeholder) fails.
- Not covered by any of this: speaking steps (microphone), spoken
  challenge answers, wrong-answer paths, and a native speaker's eye (the
  user spot-checks).

## Prompt templates

**Batch session (cloud, starts a fresh Claude session on one batch; first used for es A1 6–11).** Fill `{UNITS}` (one line per reader: unit numbers, ids), `{BATCH}` (`imports/review/<course>-<level>-batch-<first>-<last>`) and `{NOTES}`.

```
Run the next unit batch of the Parlour pass in this repo. Follow CLAUDE.md, then docs/unit-pipeline-log.md § "Pipeline" (route A; Spanish: read es-es once, mirror to es-latam) and the template it names. Readers: {UNITS}. Batch folder: {BATCH}. Two Sonnet readers at once, never more; worktrees /home/user/parlour-read-a and -b from origin/master, knowledge sheets in each first. Record as you go: the batch folder gets a setup.md first (start time, pairing, baseline check-content counts per unit and course) and every reader's report, fixes and challenges the moment it returns (commit and push them before filtering; the container can restart); each reader's tokens, minutes and fix counts from its completion notice. Then check_fixes, read every review item against the files (character facts against the stories), merge, apply, mirror, challenges, lock, validate (--changed, and --warnings compared with origin/master), freeze per course with an accept list, walk the batch's lessons in both courses. Records in the same commit: a measurements row and a process review in the pipeline log (compare with the previous rows; pick one or two changes), anything recurring into the rulebook § 6, anything seen twice in this batch scripted as a check-content check tested on the pre-fix content, ROADMAP 153 and ACHIEVED 153 updated. Commit, pull --rebase, push to master, remove the worktrees. Report to the user: cost per unit against the last row, fixes applied/changed, what you could not verify, and any decision that is theirs. {NOTES}
```

Fill `<…>`. Each agent reads `docs/unit-agent-rules.md` and nothing else
by default. Reads end with "fix as an exact old → new replacement; quote
the option text whenever you name an option" and "Run ALL its § 5
commands"; regenerations get the unit's taught/not-yet-taught list
(verbs, cases, *is*, -ik, accusative) spelled out.

**Read.** "You are reviewing one unit of a Hungarian course (Parlour app)
for a learner who knows only English, to find everything wrong with it.
REPORT ONLY: edit, create or commit nothing; change no git or tool
config. Work only in `<folder>`. Unit `hu a1 <unit id>`: lessons
`<stems>`, story `<story stem>`; earlier units `<range>`. Read
`docs/unit-agent-rules.md` first; it is your rulebook (open other docs
only to settle a point it doesn't cover). Run its § 5 commands. Read
every exercise, screen, challenge, goal, checklist, speaking step and the
story, checking § 1–4 and every item of § 6. Skip what check-content
reports. Focus: `<unit-specific grammar to watch>`. Report grouped: 1.
Found by reading; 2. Metadata; 3. Challenges / goals / checklists; 4.
Doubtful. One line each: id, problem quoting the text, fix; mark
uncertain items (unsure). Don't pad. What the learner knows before this
unit is in `<prior sheet path>` (read it first; anything listed there
presented as new is a defect). Also write every fix you give as JSON in
`<fixes path>`, in the format at the top of
`scripts/apply_replacements.py`, each with its exercise or challenge
`id`, `\"kind\": \"hungarian\"` when it changes Hungarian text and
`\"sure\": false` when unsure; quote `old` exactly from the file (that
file is the only one you may create)."

**Regenerate.** "Regenerate hu a1 unit `<n>` `<unit id>` (`<stems>`) in
`<folder>`. Rulebook: `docs/unit-agent-rules.md`; shape:
`docs/course-generation-brief.md` § 2.2/2.3 (read only those). Rewrite
both screens per lesson, story, exercises, goals/checklists, challenges;
keep ids and stems. What the learner already knows is in `<prior sheet
path>`: use it instead of opening earlier units; anything in it is
presented as known (\"You know …\"), never as new. `<unit-specific points>`. Run § 5 checks, fix
everything, lock tags, don't freeze. Commit normally with start/finish
times; report the commit, per-lesson points, and Hungarian you are unsure
of."

**Fix.** "Apply the fix list `<file>` to hu a1 `<unit id>` in `<folder>`.
Rulebook: `docs/unit-agent-rules.md`. Apply every Applied item, nothing
under Not taken; re-lock; run § 5 checks; don't freeze; commit normally
listing each item."

**Read, paired (HU A2 pass, 2026-10-14; challenges added 2026-10-14; report file, same-family list, compound glosses and up to three units per reader added 2026-10-14).** Fill `{W}` (reader worktree), `{N}` (THREE from units 39–44, user 2026-10-15: cost per unit tracks the units' defects, not the count per reader: ~117k for 25–28 at two, ~113k for 29–34 at three, ~145k for 35–38 at two), one `- hu a2 …` line per unit with its unit id, stems (space-separated) and story (`a2-unit-NN`), and `{REPORT}` (`report-<first unit>.md`); put the `prior-<unit>.md` sheets in `{W}` first. Afterwards: `check_fixes.py` per unit, read the review lists, then `merge_fixes.py` over all the filtered lists (it refuses when two readers fixed the same item differently), `apply_replacements.py` on the merged list, and the readers' compound glosses through `fill-dictionary-gaps.py import`.

```
You are reviewing {N} units of the Hungarian A2 course (Parlour app) for a learner who knows only English, to find everything wrong with them. REPORT ONLY: edit, create or commit nothing except the fixes, challenges and report files named below; change no git or tool config; never bypass hooks. Work only in `{W}` (absolute paths).

Units (read all; a later unit must not present an earlier one's material as new: recap, never new):
- `hu a2 {U1}`: lessons {S1}, story `{ST1}`. Knowledge sheet: `{W}/prior-{U1}.md`. Fixes file: `{W}/fixes-{U1}.json`. Challenges file: `{W}/challenges-{U1}.json`.
- `hu a2 {U2}`: (same pattern)
- `hu a2 {U3}`: (same pattern; omit this line for a pair)

Read `{W}/docs/unit-agent-rules.md` first (§ 1–5, § 6a and § 6b); it is your rulebook (open other docs only to settle a point it doesn't cover; it says "a1" in command examples: use `a2`). Read each knowledge sheet before its unit: anything listed there presented as new is a defect, and anything in its "Same family … taught at B1" list that the unit presents or drills is a defect too (report it: either the lesson goes beyond A2 or the skill's level is wrong). Run its § 5 commands for every unit (`python scripts/check-content.py hu a2 <unit id>`, `node scripts/render_lesson.js hu <stems>`, `node scripts/audit-reader-coverage.js hu --story <story stem> --top 0`). Read every exercise, screen, goal, checklist, speaking step and the story as rendered, checking § 1–4 and every item of § 6. Also write a fix for every check-content ERROR (length give-aways: make the wrong options as long as the right one, or shorten the right one, with met words and one fault each; shared checklist lines: reword one). Suspects: fix unmet words in options/prompts with met words; leave consolidation copies and characters' names alone. Do NOT report: missing Listening groups or exercise counts below the brief's numbers (course-wide, parked); vocabulary lists re-listing earlier words; sentence-builder alternative orders.

Known false positives (don't report): *Szabad vagy foglalt vagy?* (natural); *ki* as a literary relative is acceptable Hungarian, so never propose it as a wrong option; a wrong option must never be a possible true answer (*szekrényen* for where clothes are); consolidation items reusing lesson items (the user wants replays). A2 focus: past tense and definite/indefinite conjugation used before taught (see `taught_in` in `skills/hu.json` and the sheet's "later" list); cases taught later (-hoz a2-31, -nál a2-13, -ra/-re a2-29, translative a2-171); plural possessed (-aim, -ai) before a2-13/a2-191; wrong `teaches` (a tested form → its grammar skill, a tested word → the unit vocabulary skill); `distractor_skills` on ungrammatical options; screens restating known A1 material as new.

Write one challenge per lesson of each unit, consolidation included (six per unit), to the unit's challenges file: a JSON object keyed by lesson stem, each entry with exactly the fields of the entries in `{W}/content/hu/curriculum/challenges.json` (`tier` "tier1", `level` "A2", `title` "Communicative Challenge: …", `scenario`, `prompt`, `cues`, `target`, `english`, `canDo`), following the rulebook § 4 (the story's people; cues say what to include, never the words; target 1–3 sentences of met words using the lesson's grammar; `canDo` = the lesson's first checklist line, copied after your own checklist fixes). Report grouped: 1. Found by reading; 2. Metadata; 3. Goals / checklists; 4. Doubtful. One line each: id, problem quoting the text, fix; mark uncertain items (unsure). Don't pad. Also write every fix as JSON in the unit's fixes file, in the format at the top of `scripts/apply_replacements.py`, each with its exercise id, `"kind": "hungarian"` when it changes Hungarian text and `"sure": false` when unsure; quote `old` exactly from the file; when naming an option, quote its text.

Give your full report (the four groups above, plus a 5. Dictionary group: every "literal compound guess" or "not in the dictionary" word from the audit as `word | lemma | pos | gloss |`, one per line, the gloss being the lemma's meaning, never the inflected form's: `fill-dictionary-gaps.py import` stores it under the lemma) as your final reply. Try to write it to `{W}/{REPORT}` first; the harness may refuse a subagent's report file (it did in units 35–38), and then the reply is the only copy, so make it complete. With three units, finish and write each unit's fixes and challenges files before starting the next unit.
```

**Read, Spanish (es-es read once, mirrored to es-latam; written 2026-10-16, first run on A1 units 2–5 the same day).** The HU template above with these changes; measure the first batch against the HU A2 rows before trusting the cost. Decided by the user (2026-10-16): English inside target lines is a defect (fix to `hint`/`english`); a word in no vocabulary list is added to the first lesson that uses it; es-latam challenges as es-es; the A1 prerequisite pairs are resolved. Fill the same placeholders with `es-es <level>` lines, stems as in `content/es-es/curriculum/units/<level>.json` (A1 stems are not uniform: `a1-01-01`, `a1-03c-03`, `a1-demonstrative-01`), stories from `content/es-es/stories/manifest.json`. Replace in the template:

- "the Hungarian A2 course" → "the Spanish `{LEVEL}` course (es-es, Spain; a sibling course es-latam shares most files and gets your fixes copied by script)";
- the rulebook line: "Read `{W}/docs/unit-agent-rules.md` § 1–5, § 6a and § 6c (skip § 6b, Hungarian)";
- the § 5 commands with `es-es` and the level; `"kind": "target"` for fixes that change Spanish;
- the "Known false positives" and "A2 focus" paragraphs with: "Focus: forms used before their screen (`taught_in` in `skills/es.json`; the sheet's 'later' list): past tenses at A1 (all are A2: `preterito-perfecto` a2-01-01, `preterito-indefinido` a2-11-01; *ayer* appears 13 times in es-es A1), numbers and clock times before Unit 6 (`numbers` a1-12-01, `telling-time` a1-12-03; the unit moved from 14 to 6 on 2026-10-16), *gusta/gustan* before a1-gustar-01; § 6c. A fix that only holds in Spain (*vosotros*, *zumo*, *coche*, *billete*) is marked `\"variant\": \"es-es\"` in its JSON so the reviewer doesn't mirror it, and es-latam gets its own word (*jugo*, *carro*, *boleto*; `scripts/course_variants.py`).";
- challenges: `level` the level, the people of the es-es stories (Carlos and Meg at A1), the unit's own setting; es-latam gets the same entries with only course variants changed (user, 2026-10-16);
- add: "check every fact about a character (origin, job, city, family, who is whose friend or teacher) against the stories before using it, in exercises and reading questions as well as challenges; reading questions must be answerable from the story as written" (units 2–5: three of the reviewer's five changes were character facts);
- add (units 6–11): "a multiple-choice item takes neither `hint` nor `english` (the schema rejects both): put the meaning in the question, '<English>. Which sentence says this?', with whole-sentence options"; the batch-session prompt told readers to use `hint` and seven items failed the schema (`check_fixes.py` now rejects them);
- note the story stem is the file stem (`a1-03` is Unit 2's story; Units 3 and 4 have stories `a1-things` and `a1-21` inside a lesson, not on the unit: run the audit on them too).

Afterwards: as HU, plus `mirror_fixes.py` on each filtered list (route A, "Spanish"), and the es-latam-only files read by the reviewer.

**New unit (from scratch; written 2026-10-14 for HU A2 units 45–47).** Fill `{W}` (the agent's worktree), `{SHEET}` (`prior_knowledge.py` output), `{UID}`, `{TITLE}`, `{NUM}`, `{S1}`…`{S5}` (lesson stems), `{PLAN}` (from `docs/hu-a1-a2-cefr-gap-proposal.md`) and `{EXTRA}` (unit-specific notes). Add the unit's row to the unit table and its vocabulary skill to `skills/<lang>.json` / `frozen-<lang>.json` in the agent's worktree before it starts (the validator needs both, and they go in the same commit as the lessons). Then run `python3 build-manifest.py` there (curriculum.json is generated from the unit table; until it is rebuilt, `build_word_lesson_index.py` skips the unit, and in units 45–46 the writers' unmet-word checks ran without their own words) and revert its es-* drift.

```
You are writing ONE NEW unit of the Hungarian A2 course of the Parlour language app, from scratch. Work ONLY in `{W}` (a git worktree; absolute paths). DO NOT COMMIT (the main session collects your files). Never change git or tool config, never bypass hooks.

Read first, in this order, and nothing else unless needed to settle a point:
1. `{W}/docs/unit-agent-rules.md` (rulebook: met words, exercises, metadata, screens, challenges, known defects).
2. `{W}/docs/course-generation-brief.md` § 2 (shape), § 3 (screens), § 4 (vocabulary), § 5 (story), § 6 (exercises), § 7 (tags), § 9.1 (Hungarian).
3. The knowledge sheet `{W}/{SHEET}`: everything the learner knows (all of A1–A2 grammar and 1600 words). Every A2 grammar skill is known by now; anything on the sheet is presented as known ("You know …"), never as new.
4. As a JSON-shape model, the existing lesson `content/hu/lessons/a2/a2-160.json` with its screens, vocabulary, exercise file and story `content/hu/stories/original/a2/a2-unit-32.json`, and challenge entries in `content/hu/curriculum/challenges.json` (A1 entries show the format; key = lesson stem). Copy field names exactly; never invent fields.

The unit (already in `content/hu/curriculum/units/a2.json` and `skills/hu.json`):
- unit id `{UID}`, title "{TITLE}", unit number {NUM} (lesson field `"unit": {NUM}`), vocabulary skill `a2-{UID}-vocab`.
- lessons `a2-{S1}` … `a2-{S5}` and `a2-{S5}-consolidation` (lesson ids `lesson.a2.{S1}` …; files `content/hu/lessons/a2/<stem>.json`, screens `content/hu/grammar/a2/<stem>-a-gr.json` and `-b-gr.json`, vocabulary `content/hu/vocabulary/a2/<stem>-voc.json`, exercises `content/hu/exercises/a2/<stem>-ex.json`, story `content/hu/stories/original/a2/a2-unit-{NUM}.json` on lesson `a2-{S5}`, consolidation exercises `a2-{S5}-consolidation-ex.json`).
- Lesson plan (adjust if a better order emerges, keep the topic): {PLAN}

Rules specific to this job:
- The A2 skill list is CLOSED: no new grammar skills. Each lesson's two screens either (a) present the lesson's key words/phrases as a pattern table (like the existing A2 screen "híd, folyó, Duna: The River and the Bridge"), or (b) apply a known A2 grammar skill to the theme, saying "You know …". Exercises are tagged with the unit vocabulary skill (word meaning) or the existing grammar skill whose form a wrong answer shows (skill slugs from `skills/hu.json`; `taught_in` must be before this unit, which is true for all A1–A2 skills).
- About 20–25 new words over the unit (check each against the knowledge sheet: a known word is used, not re-listed), British English glosses, same `theme` label in all five vocabulary files.
- Exercise counts and section order per brief § 2.2 (A2: Introduce 2, Controlled 4, Practice 4, Listening 2 (`listening-choice`, `dictation`), Dialogue 2, Production 2, Check 2; lesson {S5} also has the story and a Reading group of 3), consolidation per § 2.3 (20 items, 4 groups of 5). Look at an existing A2 listening item shape in the HU B1 or Spanish A2 exercises if you need one (`grep -rl listening-choice content/*/exercises | head`).
- Story 120–200 Hungarian words, the course's A2 characters (see a2-unit-32: Meg, Károly and friends), 3 comprehension questions; Hungarian setting; facts only when certain.
- One challenge per teaching lesson (`a2-{S1}`…`a2-{S5}`) in `content/hu/curriculum/challenges.json`, `"level": "A2"`, tier as in the file, target 1–3 sentences using met words, `canDo` = the lesson's first checklist line.
- Characters' names and the story move forward naturally; this unit is not another unit with nouns swapped.
{EXTRA}

Then run from `{W}`: `python3 build-manifest.py` and then `python scripts/build_word_lesson_index.py hu` (the manifest must come first, or the index doesn't see the new lessons and the unmet-word check is blind; re-run both after changing a vocabulary list); `python scripts/check-content.py hu a2 {UID}` (fix EVERY error; fix or justify each suspect); `node scripts/render_lesson.js hu a2-{S1} a2-{S2} a2-{S3} a2-{S4} a2-{S5} a2-{S5}-consolidation` and read every screen and item as rendered (`!!` = error); `node scripts/audit-reader-coverage.js hu --story a2-unit-{NUM} --top 0`; `python scripts/validate-content.py --changed` (fix everything it reports); `python scripts/lock_tags.py hu a2/{UID} --update --reason "new unit (CEFR gap check, 2026-10-14)"`.

Report concisely: files created, word list, per-lesson topic and screens, check results, every Hungarian line or fact you are unsure of.
```

## Measurements

| Date | Unit | Route | Regen / fix (tok, min) | Read (tok, min) | Real defects in read | Notes |
|---|---|---|---|---|---|---|
| 10-10 | 8 plurals-quantities | Sonnet regen (pilot A) | 251k, 16 | 153k, 4.5 | ~21 | |
| 10-10 | 9 possession | read → fixer (pilot B) | 298k, 23 | 159k, 7.5 | ~14 | |
| 10-13 | 8 + 9 | pilot fix lists, one Sonnet fixer | 142k, 4.5 | | | both units in one agent |
| 10-13 | 11 where-things-are | Sonnet regen | 267k, 14 | 155k, 5.5 | 9 applied | frozen; agent bypassed hooks (now forbidden) |
| 10-13 | 10 foundations-review | Sonnet regen | 245k, 9 | 187k, 5 | ~15 to filter | |
| 10-13 | 8 (second read) | | | 161k, 5 | 8 applied | found a wrong pilot fix-list item |
| 10-13 | 9 (second read) | | | **123k, 3.5** (rules sheet) | 10 applied, 1 false | first read on the rules sheet |
| 10-13 | 8 + 10 fixes | **Haiku** applies filtered lists | 118k Haiku, 2.5 | | all 17 items right | the one slip was in Claude's list |
| 10-13 | 9 fixes | Claude directly | | | | short list |
| 10-13 | 12 going-places | Sonnet regen (rules sheet) | 171k, 9 | 125k, 4.5 | 9 applied | |
| 10-13 | 13 everyday-actions | Sonnet regen (rules sheet) | 204k, 11 | 106k, 2 | 8 applied | read skipped 2 commands |
| 10-13 | 12 + 13 fixes | Haiku | 115k Haiku, 3 | | 16/17; 1 skipped, 1 wrong | both caused by Claude's list |
| 10-13 | 14 questions-negation | regen + § 6 self-check | 171k, 9 | 113k, 2.5 | 9 applied | |
| 10-13 | 15 daily-routine | regen + § 6 self-check | 214k, 12 | 135k, 4 | 11 applied | |
| 10-13 | 14 fixes | Haiku, exact old → new list | 74k Haiku, 1 | | 9/9 | |
| 10-13 | 15 fixes | Haiku, exact old → new list | 83k Haiku, 3 | | 11/11 | |
| 10-13 | 16 time-dates | read first (real content) | | 132k, 4 | 40+ | → regenerate |
| 10-13 | 16 time-dates | Sonnet regen | 177k, 10 | 112k, 3 | 6 applied | Claude applied directly |
| 10-13 | 17 frequency-word-order | verdict-first read → regen | 181k, 9 | 90k + 121k | 9 applied | read caught a reversed answer key |
| 10-13 | A1 story questions ×12 | Haiku translation | 77k Haiku, 1 | | 36 questions | for the English toggle |
| 10-13 | 18 home | regen, no verdict read | 204k, 11 | 126k, 3.5 | 9 applied | |
| 10-13 | 19 food-drink | regen, no verdict read | 160k, 8 | 127k, 4.5 | 10 applied, 1 false | read claimed *Nem van tej.* is correct |
| 10-13 | 20 everyday-hungarian-review | regen (review unit) | 267k, 12 | 191k, 5 | 10 applied | review units cost ~40% more |
| 10-13 | 21 buying-food | regen | 213k, 11 | 137k, 4 | 9 applied | two-right-answer blanks via English "take" |
| 10-13 | 22 market | regen | 217k, 13 | 167k for 22+23 (**83k/unit**), 5.5 | 12 applied | paired read |
| 10-13 | 23 cafe | regen | 180k, 9.5 | (paired) | 7 applied | |
| 10-13 | 22 + 23 fixes | Haiku | 110k Haiku, 2.5 | | 19/19 | |
| 10-13 | 24–33 | paired regen + paired read | ~119k/unit | 83–108k/unit | ~25/unit | numbers in the process reviews below |
| 10-14 | walk test build | Sonnet | 152k, 10.5 | | | HU A1 198/198 in 4.5 min |
| 10-14 | HU A2 25–28 | paired read (2 units/reader) | | 235k + 235k, 10.5 | 128 applied of 132, 0 rejected | ~117k reader tokens/unit (logged as ~59k until 10-15: 470k is for 4 units); 1 skill-level clash (a2-140) found only via the batch note |
| 10-15 | HU A2 29–34 | paired read (**3 units/reader**, trial) | | 327k + 352k, 20 | 235 applied of 236, 0 rejected | ~113k reader tokens/unit (×0.97 of 25–28; first logged as ×1.9 against the wrong ~59k), ~39 applied fixes/unit (×1.2); trial dropped on the wrong figure, back to 2 units/reader |
| 10-15 | HU A2 35–38 | paired read (2 units/reader) | | 301k + 280k, 19 + 17 | 210 applied of 211, 0 rejected; 13 more by Claude | ~145k reader tokens/unit (×1.24 of 25–28); applied reader fixes 56 / 52 / 48 / 54 (~52/unit, ×1.6 of ~32); both report-file writes refused by the harness |
| 10-15 | HU A2 39–44 | paired read (**3 units/reader**) | Sonnet fixer for 42–44 unmet words: 212k, 12 | 386k + 449k, 23 + 33 | 426 applied of 426, 0 rejected; ~20 more by Claude | ~139k reader tokens/unit (A ~129k, B ~150k; ×0.96 of 35–38's ~145k); applied reader fixes 72 / 70 / 58 / 77 / 74 / 75 (~71/unit, ×1.36 of ~52); ~250 unmet-word suspects left in 42–44 needed a fixer (~71k/unit); reader B's report write refused, A's allowed |
| 10-15 | HU A2 45–47 (new units) | **New unit** template, 1 Sonnet writer per unit (45 ∥ 46, then 47); 1 paired reader (3 units) | writers 238k / 273k / 259k, 12.6 / 15.4 / 13.6 | 311k, 15.4 | 56 applied of 56, 0 rejected (45: 5, 46: 12, 47: 39) | ~257k writer + ~104k reader tokens/unit (~361k/unit); reader ×0.75 of 39–44's ~139k, ~19 applied fixes/unit (×0.26 of ~71): written-from-scratch units with the knowledge sheet came back far cleaner than the regenerated/read-first ones; 47's fixes are mostly one rename (*fenyőfa*, 15) and six hints; reader's report write refused again |

| 10-15 | HU A2 walk + level checklist | Claude, no agents | | | 0 walk failures (281/281) | ~9 min of walking; one validate warning left by a batch retag (thin skill), see § Before calling a level done |
| 10-16 | es A1 1 greetings-introductions (both courses) | **Antigravity Argon**, read + fix + mirror + challenges from a brief | 43 min; nearly all of Antigravity's weekly allowance | | 32 applied, 0 rejected; Claude changed 3 (2 challenges, 1 near-copy) | light unit (4 errors / 13 suspects); quality comparable to a Sonnet reader, cost not sustainable for 58 units |
| 10-16 | es A1 2–5 (both courses) | paired read, **Spanish template** (2 units/reader), es-es read once, mirrored | | 229k + 238k, 11.1 + 10.4 | 166 applied of 166, 0 rejected; Claude changed 5 + 1 schema fix | ~117k reader tokens/unit (A 2+3 ~114k, B 4+5 ~119k; = HU A2 25–28's ~117k at two per reader); fixes 52 / 36 / 48 / 30 (~42/unit); 120 of 166 went to review (Spanish text); 165/166 mirrored (the 1 had no es-latam counterpart); walk units 1–5 60/60; both report writes allowed |
| 10-16 | es A1 6–11 (both courses) | paired read, Spanish template, **3 units/reader**, es-es read once, mirrored | | 313k + 306k, 15.3 + ~15 (B hit a Sonnet session limit after writing all its files; resumed for its last report section) | 278 proposed (32 / 57 / 26 / 40 / 89 / 34), 0 rejected for content (1 by a stale word index, restored); Claude changed 16 (10 in the filter, 6 schema), added 12 in es-es after the new checks and `--warnings` (5 answers lists, 1 thin-skill item, 3 stories' key words, 1 story line, 2 challenge glosses) and 8 in es-latam only (3 variant fixes, 5 story question sets) | ~103k reader tokens/unit (A ~104k, B ~102k; ×0.88 of units 2–5's ~117k); ~46 fixes/unit (×1.1 of ~42); 222 of 278 to review; 269/279 mirrored (10 es-es variants or es-latam text); walk 36/36 per course; B's 305,712 is the only usage figure its notices gave (the failure notice had none) |
| 10-21 | es A1 13–18 (both courses) | paired read, Spanish template, 3 units/reader, es-es read once, mirrored | | 346k + 291k, 16.5 + 15.4 | 262 proposed (38 / 41 / 34 / 38 / 59 / 52), 0 rejected; Claude changed 2 and added 1 es-latam-only fix | ~106k reader tokens/unit (A ~115k, B ~97k; ×1.03 of 6–11's ~103k); ~44 fixes/unit (×0.95); 189 of 262 to review; 261/262 mirrored (1 es-es variant), 4 put in es-latam words by the mirror; walk 36/36 per course; A's report write refused, B's allowed |
| 10-21 | es A1 19–24 (both courses) | paired read, Spanish template, 3 units/reader, es-es read once, mirrored | | 395k + 332k, 21.7 + 17.1 | 273 proposed (55 / 45 / 45 / 29 / 47 / 52), 0 rejected; Claude changed 5 (2 retags kept, 1 story logic, 1 option set, 1 spelling) and added 4 (es-latam twins and *pedir*/*clínica*), plus 4 after the new check | ~121k reader tokens/unit (A ~132k, B ~111k; ×1.14 of 13–18's ~106k); ~46 fixes/unit (×1.04); 226 of 273 to review; 272/273 mirrored (1 es-es variant), 1 put in es-latam words; walk 36/36 per course; both report writes allowed |
| 10-21 | es A2 1–6 (both courses) | paired read, Spanish template from `batch_setup.py`, 3 units/reader, mirrored | | 347k + 313k, 21.5 + 17.6 | 263 proposed (58 / 44 / 60 / 36 / 24 / 41), 0 rejected; Claude changed 0, added 8 plus one reflexive pass (84 changes per course) | ~110k reader tokens/unit (A ~116k, B ~104k; ×0.91 of A1 19–24's ~121k on lighter baselines: 22 errors / 143 suspects for six units against 43 / 183); ~44 fixes/unit (×0.95); 186 of 263 to review; 257/263 mirrored, 6 es-latam fixes by hand; walk 36/36 per course; both report writes allowed |
| 10-21 | es A2 7–12 (both courses) | paired read, `batch_setup.py`, 3 units/reader, mirrored | | 351k + 382k (B by its resumed notice), 23.4 + ~20 | 347 proposed (45 / 75 / 39 / 63 / 61 / 64), 0 rejected after 1 reworded; Claude changed 7, added a unit-wide fix (16 lines per course), synced 6 es-latam story question sets, reopened Units 4–6 for `table-repeat` | ~122k reader tokens/unit (A ~117k, B ~127k; ×1.11 of A2 1–6's ~110k on heavier baselines: 50 errors / 106 suspects against 22 / 143); ~58 fixes/unit (×1.32); 245 of 347 to review; 334/347 mirrored; walk 36/36 per course; both report writes allowed |
| 10-21 | es A2 13–18 (both courses) | paired read, `batch_setup.py`, 3 units/reader, mirrored | | 342k + 366k, 21.5 + 21.3 | 277 proposed (43 / 56 / 45 / 50 / 35 / 48), 0 rejected; Claude changed 4, added 17 *vosotros* questions and 6 es-latam items | ~118k reader tokens/unit (×0.97 of 7–12's ~122k); ~46 fixes/unit; 209 of 277 to review; 270/277 mirrored; walk 36/36 per course **with challenges typed and graded** |
| 10-21 | es A2 19–24 (both courses) | paired read, 3 units/reader, both resumed after a session limit, mirrored | | A ~300k (resumed notice), B lost in a container restart | 329 proposed (49 / 65 / 40 / 58 / 50 / 67), 0 rejected after the `check_fixes` index fix; Claude dropped 1, adjusted 3, added 3 item fixes, 7 es-latam items, 6 *vosotros* questions and the user's story-line edits | ~100–120k reader tokens/unit (uncertain: one notice); ~55 fixes/unit; 270 of 329 to review; 316/329 mirrored; walk 36/36 per course with challenges |
| 10-21 | es A2 25–30 (both courses) | paired read, 3 units/reader, mirrored | | 438k + 431k, 28 + 28.8 | 449 proposed (73 / 73 / 65 / 88 / 93 / 57), 0 rejected; Claude adjusted 4, added 2, moved 52 Daniela items/challenges | ~145k reader tokens/unit (**over the ~140k line**); ~75 fixes/unit (×1.36 of 19–24); 397 of 449 to review; 437/449 mirrored; walk 60/60 per course (21–30) |
| 10-21 | es A1 25–26 (both courses) | **one** reader, 2 units, Spanish template, mirrored | | 244k (the resumed notice only; stopped by a Sonnet session limit after 3 of 4 files) | 84 proposed (31 / 53), 0 rejected; Claude changed 3 and fixed one cross-story contradiction | ~122k reader tokens/unit (uncertain: one notice); ~42 fixes/unit; 59 of 84 to review; 84/84 mirrored, 5 put in es-latam words (*billete* → *boleto*); level walk 156/156 per course |
| 10-22 | es A2 31–33 (31–32 both courses, 33 es-es only) | paired read, 2 units + 1, both stopped by a Sonnet session limit before writing a file, resumed | | A 233k, B 182k (resumed notices only; the first runs' usage was lost with the limit) | 213 proposed (61 / 75 / 77), 4 rejected by `check_fixes` (3 builders with an `answer` key, fixed and kept; 1 deliberate *nunca/jamás*, kept); Claude changed 9, restored 7 `distractor_skills` entries the reader removed, added 2 (a B1 option set the es-es unmet check missed, an unmet story option) | cost/unit uncertain (≥ ~140k: the resumed notices alone give 116k + 182k); ~71 fixes/unit; 174 of 213 to review; 102/122 mirrored, 3 es-latam twins by hand, the rest es-es variants or es-latam text the reader fixed directly; level walk 198/198 es-es, 192/192 es-latam with challenges |
| 10-22 | HU A1 + A2 re-walk **with challenges** (first since challenge walking began 10-21) | Claude, no agents | ~18 min | | 0 walk failures (198/198 A1, 281/281 A2) | HU and Spanish A1–A2 now pass the same checklist |
| 10-22 | **HU B1 pilot**: Unit 1 longer-stories (language) ∥ Unit 2 hungary-today-land-symbols (history, facts block) | mechanical pre-pass (1 Sonnet fixer, 25 items) then 1 unit per reader | fixer 83k, 1.5 | A 257k, 13.6; B 326k, 22.4 | 154 proposed (48 / 106), 3 rejected (new tells, option language; rewritten by Claude), Claude added 4 (vármegye official since 2023, double-cross tradition) | ~257k language / ~326k history per unit at **one unit per reader** (fixed per-reader overhead not spread); pre-pass: 24 of 25 applied, then readers rewrote most of them; Unit 2 had 256 unmet-word hits before the pre-pass (6 after the read), Unit 1 37 → 20; walk 12/12 |
| 10-22 | HU B1 3–6 (core 3, 5; citizenship 4, 6) | paired read, **2 units/reader** (one core + one citizenship each), facts block, vocabulary rule (citizenship keeps words) | | A 532k, 43.7; B 554k, 39.7 | 344 proposed (71 / 113 / 51 / 109), 0 rejected; Claude changed 2 (Árpád-ház *1301-ig*, an apposition) | **~272k reader tokens/unit** (no cheaper than the one-unit pilot's 257k / 326k): the cost follows the defects (~86 fixes/unit, ×1.7 of A2), not the per-reader overhead; both readers re-tested their fixes in scratch copies (111 and 118 tool calls; now forbidden in the template); 10 copied question sets rewritten; facts: Aug 20 state holiday and the Pozsony 907 name confirmed; walk 24/24 |
| 10-22 | HU B1 core 7, 9, 11, 13, 15, 17 | paired read, **3 core units/reader**, no-self-testing rule | | A ≥470k, B ≥427k (resumed notices only: both stopped at a Sonnet session limit mid-batch) | 386 proposed (47 / 58 / 51 / 81 / 78 / 71), 6 rejected by the checker (rewritten by Claude), Claude dropped 1 (*elmondott volna* in a story) and restored 1 it had wrongly reversed (Fábián's *te*); 51 Unit 13 fixes first refused by a missing final newline (164 files fixed, `apply_replacements.py` tolerant) | cost/unit not measurable (≥ ~150k from the resumed parts alone); ~64 fixes/unit (×0.75 of 3–6: core units have fewer defects than citizenship ones); reader B ran only the named commands; walk 36/36 |
| 10-23 | HU B1 core 19, 21, 23, 25, 27, 29 | paired read, 3 core units/reader | | A 581k, 39.2; B 430k, 38.9 | 662 proposed (159 / 155 / 151 / 63 / 69 / 65), 7 rejected (5 checker false positives on accented names in English options, 1 `answer`/`answers`, 1 tell; rewritten by Claude), Claude changed 2 story/screen lines | **~194k/unit (A: Units 19–23 were rewritten almost whole, ~155 fixes each) and ~143k/unit (B: Units 25–29, half-size lessons)**; 18 lessons had no checklist, so no `canDo` to copy: `add_missing_checklists.py` (goal lines; consolidations from the challenge drafts); walk 36/36 |
| 10-27 | HU B1 core 31, 33, 35, 37, 39, 41 | paired read, 3 core units/reader; both stopped by the weekly Sonnet limit with Units 35 and 41 written but not reported, resumed after the reset | | not measurable (limit mid-batch; A's last resume 407k cumulative) | 446 proposed (89 / 84 / 90 / 59 / 54 / 70), 9 rejected by the checker (6 length give-aways, 1 *az ____* article blank, 1 *volna* in the prompt, 1 `distractor_skills` naming the item's own skill; rewritten by Claude); Claude dropped 10 (8 screen rewrites that replaced the taught phrases *meg vagyok győződve*, *továbbá*, *tekintettel arra, hogy* with A2 words; a wrong "met in Unit 26" recap; a story line), corrected 2 recap unit numbers and removed 2 unchecked ones, fixed 5 *volna*-in-both-clauses suspects, 1 tell, 1 challenge whose target missed its `canDo` | ~74 fixes/unit; 36 lessons got checklists; `noun-compounds` fell to 5 exercises after a correct retag, one item added; new `check_unit_refs.py` found 5 more wrong recap units (Units 19, 27, 29, 31, 35); walk 36/36 |
| 10-27 | HU B1 core 43, 45, 47, 49, 51, 53 | paired read, 3 core units/reader, no limit hit | | A 326k, 56 tool calls (~109k/unit); B 421k, 70 (~140k/unit) | 433 proposed (72 / 64 / 65 / 79 / 79 / 74), 7 rejected by the checker (5 length, 1 tell, 1 hint = answer, 1 article blank; rewritten by Claude); Claude changed 6 (*arra az eshetőségre* → *esetre*, a story option true of the story, a 94-character story answer, a *noha* unit, the *mielőtt* item's tag) | **cheapest batch so far** (half-size lessons, ~72 fixes/unit); reader A skipped `unmet-words.js`: Claude's run found 19 hits after both lists were applied, 15 of them screen phrases on no vocabulary list (added), 4 lemmatizer false positives; 36 checklists, 92 glosses; walk 36/36 |
| 10-28 | HU B1 core 55, 57, 59, 61, 63, 65 | paired read, 3 core units/reader; both stopped by the 5-hour Sonnet limit after two units, resumed after the reset | | A 384k, B 396k as reported on resume (~128k and ~132k a unit if cumulative) | 443 proposed (68 / 66 / 64 / 81 / 80 / 84), 15 rejected by the checker (9 tells, 3 length, 1 article blank, 1 copy, 1 *take* gloss; rewritten by Claude); Claude changed 6 (*köteles*/*kénytelen* as two answers, a story claim about Gina, 4 wrong recap units) and fixed 8 more recap units with `check_unit_refs.py` | ~74 fixes/unit; unmet-words after applying: 17 hits, 7 added to vocabulary lists, the rest inflected forms the lemma lookup misses; 18 checklists, 36 challenges, 62 glosses; walk 36/36 |
| 10-28 | HU B1 core 67, 70, 72 (last core batch) | paired read, 2 units + 1 | | A 357k (~178k/unit), B 271k (one unit) | 242 proposed (88 / 76 / 78), 0 rejected; Claude corrected 3 recap units | **core track done: 36/36 frozen; every core unit check-content clean, walk 216/216**; the reader audit's `--top 0` had hidden every "not in the dictionary" word since the template began (fixed): 62 story words across the 32 core classics, 44 glossed as surface forms, the rest names |
| 10-28 | HU B1 citizenship 8, 10, 12, 14 (first citizenship batch) | paired read, 2 units/reader, facts block; both stopped by the 5-hour Sonnet limit before writing a file, resumed after the reset | | A 307k, B 344k (resumed notices only) | 337 proposed (101 / 87 / 72 / 77), 7 rejected by the checker (rewritten by Claude); Claude changed 3, dropped 2 (track-numbered consolidation titles), added 10 item fixes, 77 vocabulary entries, 4 challenge edits | ~150–170k reader tokens/unit if the notices are cumulative; 15 placeholder question sets rewritten (none left in HU B1); 85 unmet words after applying (77 listed, 4 forms before their unit rewritten); `check_unit_refs.py` unit filter fixed (it skipped every citizenship screen) and found 2 wrong *amely* recaps; facts web-checked, none disputed; walk 24/24 |
| 10-28 | HU B1 citizenship 16, 18, 20, 22 | paired read, 2 units/reader, no limit hit | | A 380k, 25 min; B 439k, 31 min | 534 proposed (98 / 102 / 160 / 174), 4 rejected by the checker (2 false rejections restored, 2 rewritten); Claude changed 10, added 9 item/screen fixes, 96 vocabulary entries, 2 challenge edits | **~190k (A) and ~220k (B) a unit**; B's units had ~170 fixes each (every segment rewritten for overclaims, every screen a recap); `check_fixes.py` listed the readers' unmet words while sorting (27 / 19 / 14 / 22); 2 wrong recaps (*révén*, *amint*); `historical-routines` thinned to 5 by a correct retag and topped up; walk 24/24 |
| 10-28 | HU B1 citizenship 24, 26, 28, 30 | paired read, 2 units/reader; both stopped by the 5-hour limit before writing a file, resumed | | A 299k, B 290k (resumed runs only) | 431 proposed (94 / 109 / 115 / 113), 10 rejected by the checker (8 rewritten, 2 applied by hand); Claude changed 8, added 8 fixes, 76 vocabulary entries, 24 checklists, 3 challenge edits | lessons from Unit 24 on have goal lines but no checklist (24 built); facts all standard, none disputed; one cross-reader recap break (*annak dacára* recapped from a screen the other reader rewrote); walk 24/24 |
| 10-28 | HU B1 citizenship 32, 34, 36, 38 | paired read, 2 units/reader; first pair lost to a container restart before any file, relaunched | | A 338k, B 372k (rerun) | 411 proposed (96 / 107 / 102 / 106), 2 rejected and rewritten; Claude changed 4, reworded 2 shared lines | ~175k a unit; every lesson's ex02 was a garbled-options generator item, rewritten by both readers; no facts in dispute; walk 24/24 |
| 10-29 | HU B1 citizenship 40, 42, 44, 46 | paired read, 2 units/reader; both hit the 5-hour limit and were resumed | | A 284k, B 307k (resumed runs) | 365 proposed (90 / 102 / 84 / 89), 6 rejected and rewritten; Claude changed 20, added 5 text fixes | ~150k a unit (resumed only); most facts errors of any batch so far; walk 24/24 |
| 10-29 | HU B1 citizenship 48, 50, 52, 54 | paired read, 2 units/reader, no limit hit | | A 321k, B 373k | 422 proposed (78 / 92 / 123 / 129), 0 rejected; Claude changed 14, dropped 14 hand-made checklist sections | ~175k a unit; figures shared between units made to agree; walk 24/24 |
| 10-29 | HU B1 citizenship 56, 58, 60, 62 | paired read, 2 units/reader; both hit the 5-hour limit and were resumed | | A 294k, B 284k (resumed runs) | 481 proposed (120 / 137 / 116 / 108), 2 rejected and rewritten; Claude changed 9, added 3 text fixes | ~145k a unit (resumed only); civics facts checked against the Fundamental Law; walk 24/24 |
| 10-29 | HU B1 citizenship 64, 66, 68, 69 | paired read, 2 units/reader, no limit hit; reader A told of the 2026 megye change mid-read | | A 221k, B 365k | 430 proposed (77 / 82 / 143 / 128), 2 rejected and rewritten; Claude changed 9 | ~145k a unit; Units 2 and 56 refrozen for the megye change; walk 24/24 |

Reads before unit 9's second read used the full docs (brief, AGENTS, spec, registry).

## Process reviews

### 2026-10-13 (after units 10, 11)

- Cost per finished unit ≈ 450k Sonnet tokens on either route; reads
  (150–190k) mostly re-read the same four docs. **Change:** this rules
  sheet replaces them for every agent; templates above replace hand-written
  prompts. Measure on unit 9's second read against the 155–187k reads.
- Reviewer's own cost: filtering by checking each claim in the files is
  where errors were caught (wrong pilot item, "Harminc éves" two-answer
  item), so it stays.
- Done: `check-content.py` `vocab-duplicate` (error); it also found
  *foto* twice in es-es/es-latam `a1-03-01-voc` (left for the Spanish A1 pass).
- Next candidates: a check for `distractor_skills` on non-word options (the Reader
  lexicon can tell a non-word); Haiku for applying an already-filtered
  fix list.

### 2026-10-13 (after units 8, 9, 10 frozen)

- **Rules sheet:** unit 9's read cost 123k / 3.5 min against 155–187k /
  5 min, with as many real findings (and one new class: challenge scenarios
  not naming the target's object). Keep it; every agent uses it.
- **Haiku for applying a filtered list:** 17/17 items right, 118k Haiku
  tokens, 2.5 min, no improvisation. Use Haiku for every fix list from now
  on; Sonnet only for regeneration and reads.
- **Reviewer slips found by the next step:** twice the reviewer's own list
  put `distractor_skills` on the wrong option (pilot a1-44 items; a1-38-check-2,
  where the option order differed). **Change:** a list item naming an option
  index must quote the option text, and the fixer checks the text matches
  before editing. Added to the rules sheet § 3.
- Reads still produce ~1 false claim each (*táskája* does not lengthen):
  filtering against the files stays.

### 2026-10-13 (after units 12, 13 frozen)

- **Cost per unit is down ~30%:** regeneration 171–204k (was 245–267k),
  read 106–125k (was 155–187k), Haiku fix ~58k Haiku. About 300k Sonnet +
  60k Haiku per stub unit, ~25 min wall time with two units in parallel.
  Projection for the 20 HU A1 units left: ~6–7M Sonnet tokens (was ~9M).
- **Remaining errors are the reviewer's fix lists:** a conditional item
  ("only if that is the exact text") made Haiku add *i, í* to a vowel list
  the screen's own tip contradicts; an item asked for `answers` next to
  `answer`, which the schema rejects (`answers` replaces `answer`).
  **Change:** fix-list items are exact old → new replacements, no
  conditionals; field shapes are checked against an existing item first.
- **Regenerators still write words whose meaning needs a form not yet
  taught** (*hallgat* alone = "is silent"). Added to rules § 6.
- **New checks (user: script every repeat defect):** `ds-on-answer`,
  `ds-own-skill` (0 hits course-wide: guards), `glued-blank` (HU suspect: a
  blank glued to a stem in *-a/-e* with a lengthening suffix as the answer;
  3 real hits in B1: b1-18-03.ex03, b1-26-05.ex02, b1-30-03.ex05; one false
  positive, a verb, b1-33-04.ex02).
- `unmet-word` now also scans challenge targets. (It briefly scanned
  stories too; the user ruled 2026-10-13 that stories may use unmet words.)
- **Next to try (units 14, 15):** have each regenerator run a self-check
  against rules § 6 and list what it checked, to see if the read finds
  fewer defects; keep two units in parallel.

### 2026-10-13 (after units 14, 15 frozen)

- **§ 6 self-check in regeneration: dropped.** Reads still found 9–11
  real defects per unit (same as without it) and regeneration cost the
  same or more (171k, 214k).
- **Reads propose exact old → new fixes: kept.** The fix list is then a
  near-copy, Haiku's pass fell to 74–83k / 1–3 min, all items right.
- **Real-content units: read first, then decide.** Unit 16's read found
  40+ defects (no challenges, generic checklists, forms taught later, an
  incoherent story): regenerate when a read finds more than ~30 or the
  challenges/checklists are missing or generic; else fix.
- **New checks this round:** `ds-on-answer`, `ds-own-skill`,
  `glued-blank`, and `unmet-word` over stories and challenge targets;
  `scripts/merge_challenges.py` for parallel-unit conflicts.
- Running cost per stub unit now ≈ 190k regen + 120k read Sonnet + 80k
  Haiku; ~4 units/hour with two agents.

### 2026-10-13 (after units 16, 17 frozen)

- **Verdict-first reads** on old units cost 90k (vs 130k) and decide
  regenerate/fix before anyone pays for a full defect list. Keep for every
  unit not yet read.
- **Regenerated units so far all needed regenerating** (8–17 except 9):
  units 18–33 are probably the same; verdict-first read stays as the gate.
- **Short fix lists (≤ ~8 text edits): the reviewer applies them directly**
  (unit 16, 17); Haiku only for longer lists — the agent's own setup
  (~50k) outweighs a few edits.
- **A read caught a reversed answer key** (a1-84-check-2) that every check
  passed. No script can tell which option is right; reads stay.
- **English toggle (user, 2026-10-13):** A1 comprehension questions in
  Hungarian with `questionEnglish`/`optionsEnglish`; done for units 1–7, 9,
  11–15, 17. The rest (units 8, 10, 16 need Hungarian questions; 18+ need
  English) is done by Sonnet once all units are finished (user).

### 2026-10-13 (planning units 18–33)

- A scripted survey of units 18–33 (check-content counts, challenge entries,
  distinct screens) finds every one with **no challenges** and 18–30 with
  generic checklists shared across lessons: the pattern that sent 16 and 17
  to regeneration. **Change:** regenerate them directly, no verdict read
  (saves ~90k Sonnet per unit, ~1.4M in all); each still gets one blind
  read after regeneration.

### 2026-10-13 (after units 18, 19 frozen)

- Direct regeneration (no verdict read) worked: 18 and 19 needed only
  short fix lists (9–10 items). Keep.
- `scripts/take_unit_commit.py` replaced the hand-written cherry-pick and
  conflict sequence.
- Reads keep producing ~1 false Hungarian claim per unit (*Nem van tej.*,
  *táskája*): filtering stays with the reviewer.
- Reviewer's own slips this round: none found by the next step.

### 2026-10-13 (after units 20, 21 frozen)

- Review units cost ~40% more (read every earlier unit): budget ~460k for
  unit 25 and the A1 end review.
- New repeat defect: English glosses that let two conjugations fit
  ("take" for *kérem*/*veszem*). Added to rules § 6.
- Units 21 and 22 overlap in topic (market lesson in 21): the regeneration
  prompt now names what the previous unit already covers.

### 2026-10-13 (after units 22, 23 frozen): two units per agent

- **Paired read** (one Sonnet agent, units 22 + 23): 167k = 83k per unit
  against 106–191k single, with as many real findings (12 + 7 applied) and
  a cross-unit catch (unit 23's price screen re-teaching unit 21). **Reads
  go in pairs from now on** (user: "double is ok").
- Triples considered and declined for now (user agreed): the fixed cost
  per read is ~40–50k, so a third unit saves only ~13k/unit more, while a
  ~250k-token context risks the detail checks late in the read.
- **Paired regeneration** (24 + 25): 238k = 119k/unit (single: 160–267k),
  14 min for both. But its read found ~16 real defects per unit (single:
  9–12), mostly in the second unit: re-teaching earlier units as new
  (colours from 22, the definite verb from 21) and repeated item shapes.
  Net still cheaper (the extra fixes are Haiku work), so pairs stay, with
  the prompt now listing what earlier units already teach.
- New check `take-gloss` (HU fill-blanks whose English "take" lets *kér-*
  and *vesz-* both fit): the defect recurred in 21, 22, 24, 25 despite the
  rules sheet; the check finds exactly the read's 4 typed items.

### 2026-10-13 (units 26, 27 read)

- The paired read found ~25 items per unit, mostly recap screens presenting
  earlier units as new (the 28+29 prompt already lists "recap, never new").
- New check `consolidation-copy` (suspect): a consolidation item identical
  to a lesson item. 317 hits course-wide, almost all in frozen units 2–7, 9
  (whose consolidations were built as replays; left as they are) and in the
  not-yet-regenerated 28–30; regenerated units have 1–5 each.
- Known `consolidation-copy` suspects in units frozen before the check
  (one each): a1-45-consolidation-10, a1-60-consolidation-4,
  a1-65-consolidation-17, a1-70-consolidation-1, a1-75-consolidation-17.
  Left: reopening five frozen units for one review item each isn't worth it;
  fold them into any later edit of those units.
- New check `reported-question` (suspect): "Anna asks Meg where she is
  going. Which question?" lets *Hová megy?* fit too. 9 hits in HU A1: 2 new
  ones in 28/29 sent to the fixer; a1-124/125 hits are formal *Ön* (3rd
  person is right there, accept); a1-113-practice-3 logged.
- New checks `hova-variant` and `article-blank` (suspects). First run:
  a1-153-controlled-1 (in the fixer's list), a1-151-practice-3 (in the
  list), and a real one in frozen unit 8: a1-36-practice-5 builds *A
  emberek* (fold into the next edit of unit 8); B1/B2 hits logged; the C1
  hits are *az* the pronoun (false positives).
- New check `ik-first-person` (error): *eszek/iszok/dolgozok…* as a right
  answer (the course teaches *eszem/iszom*; *-k* forms are its wrong
  options). One hit course-wide, unit 33 (fixed with its screen, a
  consolidation item and an a1-164 challenge, all *eszek/iszok* → *-m*).

### 2026-10-13 (units 32, 33 frozen): HU A1 complete

- Paired read 32+33: 202k, 10 min (first attempt stopped on the weekly
  Sonnet limit). ~35 items; I applied them myself with one exact-replacement
  script (each old string must match once, else nothing is written) plus a
  JSON pass for `ds`, retags and challenges. Cheaper than a Haiku pass for a
  list this size, and the script caught a double match the list missed
  (*Magyarul tanulsz.* in two items).
- Same pattern again: recap screens presenting earlier units as new
  (a1-158-b, a1-159-a, a1-160-a/b). The regeneration prompt's "recap, never
  new" line is not enough on its own; the reader catches it reliably, so
  keep the read.
- My own edits tripped `length-giveaway` and `unmet-word` once each;
  run check-content after every hand edit, not only before freezing.

### 2026-10-14: follow-ups after HU A1 (user's decisions)

- Consolidation copies: the count I first gave (five) was wrong; the
  frozen units 12–25 had 22 stray copies, units 2–9 are replays. The user
  chose to fix the strays and leave 2–9. 21 rewritten (a1-60, 65, 70, 75,
  80, 115, 120, 125) plus a1-113-practice-3 (reported question → quoted)
  and a1-36-practice-5 (*A emberek* → *Az*). Lesson: count with the
  checker before putting a number to the user.
- `freeze_unit.py` refreezing a frozen unit replaced its reason and lost
  its accepted findings (check-content hides them, so they weren't passed
  back). Fixed: a refreeze keeps the earlier accepted entries and reason.
- Accepted at refreeze: a1-57-introduce-1 (asks about the question form, not
  reported speech), a1-124-controlled-2, a1-124-practice-3,
  a1-125-practice-5 (formal *Ön*: third person is right).
- *hánykor* added through `imports/dictionary/additions-hu.json` (merge
  step, so a dictionary rebuild keeps it). Spanish a1-03-01 duplicate
  *foto* removed in both courses. B1 glued blanks (b1-18-03.ex03,
  b1-26-05.ex02, b1-30-03.ex05) stay parked with HU B1.
- Next, decided by the user: the gate-1 lesson walk test (ROADMAP 153(b))
  on HU A1 before starting HU A2.

### 2026-10-14: two efficiency methods built (for HU A2 onwards)

- **Knowledge sheet** (`scripts/prior_knowledge.py`): ~7k tokens a unit
  (61 known skills, 527 words, every earlier screen title before A1 unit
  32). Replaces agents opening earlier units; aimed at the most common
  read finding in units 24–33 (screens presenting earlier material as
  new). Expected: shorter reads and fix lists; measure on the first A2
  pair.
- **New suspect `recap-unmarked`** in check-content: a grammar screen that
  repeats 2+ example sentences of an earlier unit's screens with no "You
  know"-style wording. HU A1 21 hits (mostly review units 10 and 20, whose
  screens recap without saying so), A2 7, es-es A1 0. It would not have
  caught the unit 32 defects (those screens said "you know" for part and
  presented the rest as new), so it is a partial check; the sheet is the
  prevention.
- **Reader JSON + `scripts/check_fixes.py`**: the reader writes its fixes
  as JSON; the script applies them to the working tree, runs check-content
  on the unit, restores the files and sorts them into rejected / review /
  auto. Tested on a frozen unit with five planted fixes: the good one went
  to auto, the Hungarian and unsure ones to review, a non-matching text and
  a length give-away were rejected, files unchanged afterwards. The reviewer
  then reads only the review list. `apply_replacements.py` now also takes
  `{"file", "id", "set": {...}}` fixes (tags, `distractor_skills`,
  options, challenge fields; null deletes a field).
- Limit: the script knows only whether a fix applies cleanly and passes
  the checks, not whether its Hungarian is right; that stays the
  reviewer's job (the review list).

### 2026-10-15 (new units 45–47 written, read and frozen): HU A2 47/47

- **Cost:** writers 238k / 273k / 259k (one Sonnet agent per unit, two at
  once, 47 after 45 and 46 were merged so its sheet counted their words);
  one reader for all three, 311k (~104k/unit). ~361k a unit in all, against
  ~119k (regeneration) + ~139k (read) for the regenerated A2 units: a unit
  from scratch costs about twice a regeneration, as expected for writing
  every screen and item.
- **Defects:** 56 applied fixes (~19/unit against ~71 in 39–44), 0 rejected;
  the reader checked the writers' challenges instead of drafting (8 scenario
  fixes). Unit 47 carried most of them: one wrong word used throughout
  (*fenyőfa* for the Christmas tree, 15 fixes), six hints spelling out the
  tested ending, and three screens presenting Unit 37/38 chunks as new. The
  sheet lists earlier screen *titles*, not their example chunks, so a writer
  doesn't see that *Boldog névnapot!* was taught; the reader found it.
- **New check `hint-suffix`** (suspect, A1–B1 fill-blanks): a hint with
  "+ -ending" (*buli + -ra*). 0 hits now in hu/es-es/es-latam A1–B1 after the
  fixes; C1 uses suffix hints on purpose (436), so it is level-scoped. Rule
  added to `docs/unit-agent-rules.md` § 6 with experiential *már* (B1) and
  the "check earlier screens for the same chunks" note.
- **Pipeline gap fixed:** `curriculum.json` comes from `build-manifest.py`;
  without it the word index skipped the new units and the writers'
  unmet-word checks were blind to their own words. Now in the "New unit"
  template.
- **Script fixes:** `prior_knowledge.py` numbers units within the level
  ("A2 Unit 37 …"), so "You know … from Unit N" can be copied (its header
  said "unit 78"); `unmet-words.js` accepts a met number + *-kor* (the two old
  suspects *kilenckor* a2-105-consolidation-11 and *tizenegykor*
  a2-107-controlled-3, and five more, were false positives; no content change).
- **Still open (not covered by these checks):** the Reader splits
  *húsvétkor / karácsonykor / szilveszterkor* as *kor* "age" (engine); digit
  years *1848-ban*, *1956-ban* and TTS; the HU A2 walk test and the level
  checklist.

### 2026-10-15: HU A2 walk test and level checklist

- Walk: units 25–47 137/137 on the first run, units 1–24 rerun 144/144
  (edited after their 2026-10-14 walk). No engine or content fix needed;
  the A1 walk had found the only real walk defects so far (the two
  `learnerModel.js` probe 404s). For Spanish A1/A2, run the walk once the
  first units are frozen, not only at the end: it is cheap and an engine
  defect would hit every lesson.
- Checklist: frozen 47/47, check-content 0/0, one validate warning
  (`a2-review-work-past-opinions-vocab` 5 exercises) from a correct retag
  in the units 29–34 batch, logged then as "validate passes". Now a batch
  step (Pipeline step 6). If it recurs, script it: `freeze_unit.py` or
  `lock_tags.py --update` should refuse when a unit's tags leave a skill
  under 6 without `thin_ok`.

### 2026-10-16: Spanish A1 unit 1 by Antigravity (Argon), first Spanish unit

- **Quality:** good on a light unit. It followed the brief to the letter
  (fix JSON, `check_fixes.py`, mirror, `add_challenges.py`, report in the
  set structure) and found the real defects a Sonnet reader finds: two
  right answers in greeting items, forms before their screen as options,
  grammatical "wrong" word orders, same-shape items. Its misses were the
  kind a reviewer catches by reading: a challenge contradicting the story
  (Meg is from South Africa), a near-copy between consolidation and lesson.
  Not measured: what a blind second read would still find.
- **Cost:** 43 minutes and nearly a whole week of Antigravity's allowance
  for the lightest unit. It cannot carry 58 Spanish units; Sonnet readers
  (route A, ~100–150k tokens a unit) stay the default. Antigravity only for
  work its allowance covers.
- **The two-course method worked:** 32/32 fixes mirrored; the unit's
  exercise files stayed identical in both courses.
- **New rule for challenge drafts:** check every character fact against
  the story (origin, job, city) before adding; the challenge checks don't
  read stories.

### 2026-10-16: Spanish A1 units 2–5, first Sonnet batch on the Spanish template

- **Cost:** 467k reader tokens for four units (~117k a unit, 11 min per
  reader), the same per unit as HU A2 25–28 at two per reader. HU 29–34
  and 39–44 cost ~113–139k a unit at three, so three per reader would save
  the fixed setup (~40–50k a reader) without raising per-unit cost.
  **Decided by the user (2026-10-16): three units per reader from units
  6–11**, measured against this row; back to two if a reader's per-unit
  cost goes above ~140k or its late units show thinner reads.
- **Story audio (user, 2026-10-16):** story text fixes that need new
  narration audio are made in the JSON during the pass and logged in
  ROADMAP 153; all A1 story audio is regenerated once, at the end of A1.
- **Defects:** ~42 applied fixes a unit (unit 1 by Antigravity: 32). Both
  readers ran every § 5 command, wrote fixes, challenges and reports (the
  harness allowed both report files this time). 0 rejected by
  `check_fixes.py`; my filter changed 5 of the 120 review items, none for
  Spanish grammar: three character/story facts (Carlos's parents named
  "Ana y Andreas", which no story says; Daniela as Meg's "amiga" when story
  a1-03 makes her the new teacher), one awkward line (*tienen una foto
  juntos*), one weak option set (*por que*). **Change:** the Spanish template
  now tells readers to check character facts in exercises and reading
  questions too, not only in challenges (rulebook § 6c).
- **Missed by `check_fixes.py`:** a fix gave a multiple-choice item an
  `english` field, which the schema rejects; only `validate-content.py
  --changed` caught it after applying. First sighting; if it recurs,
  `check_fixes.py` should validate the schema of each changed file.
- **Scripted the same day (each defect seen 2+ times in this batch):**
  `glued-blank` now covers Spanish (any blank glued to a stem; tested on
  the pre-fix content: all 9 reader finds plus a real one in Unit 6,
  a1-04-03.ex03); new suspect `self-third-person` (4 of 4 reader finds, no
  other hits in es A1–B2); `english-in-target` now flags a bracketed word
  that is in no Spanish dictionary headword (`imports/dictionary/
  spanish-en.json`), in lines and in choice questions with a blank: both
  reader finds (*(older)*, *(brothers)*) plus four real ones in units not
  yet read (a1.06.01.ex10 *(I walk)*, a1.06.06.ex10, a1.07.02.ex06
  *(some)*, a2.imperfectocontraste.01.ex01), no false positives (*(yo)*,
  *(ella)*, *(costar)* pass). The first version used the course word
  index and flagged *(ella)*, *(costar)*: tightened before committing.
- **Checker false positive, open:** `unmet-word` flags the English reading
  option *Meg's friends from class.* (a1-03c-05-r03) in es-latam only; the
  identical item passes in es-es. Accepted at freeze; look at it if it
  shows up again.

### 2026-10-16: Spanish A1 units 6–11, three units per reader

- **Cost:** 313k (reader A, units 6–8) + 306k (reader B, 9–11), ~103k a
  unit, ×0.88 of units 2–5 (~117k at two per reader), with ~10% more fixes
  a unit (~46). Neither reader went above ~140k a unit. Reader B hit a
  Sonnet session limit after writing every fixes and challenges file (the
  "finish each unit's files first" instruction is what saved them) and was
  resumed for its last report section; its 305,712 tokens come from the
  resumed notice only, so B's figure is less certain than A's. **Keep
  three per reader** for units 12–17.
- **Thinner third unit?** No: the third units (8 home, 11 café) had 26
  and 34 fixes on light baselines (1/3 and 7/9), and Claude's filter
  changed two items in each. The misses were in the *first* unit: five
  fill-blanks in Unit 6 accepting verbs their `english` excluded, found
  only by the new `answers-alternatives` check after the freeze (unit
  unfrozen, fixed, refrozen the same session).
- **Filter changes (16 of 278):** six multiple-choice items given a
  `hint` (my batch prompt said "use `hint`" for MC; the schema rejects
  it); three `answers` lists the reader narrowed but not to the one
  answer the English fits; two wrong options that are natural right
  answers (*Tiene una cocina y un baño.*, *Sí, tiene un jardín.*); two
  character facts (Carlos *se levanta temprano* / *a las siete*: he wakes
  at eight in a1-06); one demonstrative answered from the wrong place
  (seller's *esta bolsa* → Meg's *esa*); one non-word option (*estes
  libros*); one reading answer narrowed (*refresco* → *refresco o
  zumo*). None for Spanish grammar.
- **What only the reviewer found:** es-latam story questions copied from
  another story (5 in this batch, 26 A1 stories in all; the readers read
  es-es only); the retag of Unit 10's dialogues leaving
  `a1-demonstratives-vocab` at 5 exercises (`--warnings` diff, as the
  pipeline warns); *coche* mirrored into es-latam, which says *carro*;
  *gusta* in the Unit 6 story.
- **Changes:** (1) `check_fixes.py` validates each changed file against
  its schema and rejects the fix (seen in units 2–5 and again here; tested
  on the pre-fix content: it rejects the reader's six MC `hint` fixes).
  (2) The Spanish template says how MC items carry meaning. (3) Four new
  `check-content` checks and two checker fixes, below. (4) The reviewer
  reads the es-latam stories of each batch (questions, key words, voice)
  as part of "es-latam-only files", since `cmp` shows them as differing
  only by timings.
- **Scripted (each seen twice or more in this batch), tested on the
  pre-fix content (19791490), batch units:** `answers-alternatives`
  (ES suspect: a fill-blank whose `answers` holds different words while
  its `english` fits one) 14 hits in es-es, 13 real, 1 false positive
  (*luego/después*), es-latam 15 (+ *bebes/tomas*, a course variant);
  readers had found 8 of the 13. Course-wide it hits 77 / 94 (es-es /
  es-latam, mostly B1, not read; false positives there include *Ve/Vaya*
  and open "say what he is like" items); left off HU (338 hits,
  unchecked). `story-voice-gender` (error: a recurring character with the
  wrong narration voice) 2 of 2 real, 5 more per Spanish course (a1-04,
  a1-10, a1-11, a1-17 Daniela; a1-13 Kaylee). `story-key-vocab` (suspect:
  A1–A2 `keyVocabulary` absent from the story) 11 of 11 real, no false
  positives after stemming *-se* verbs (*levantarse* → *te levantas*);
  35 more per Spanish course. `story-questions-copy` (suspect: the same
  comprehension questions as another story) 5 of 5 real in es-latam; 38
  es-latam (21 A1, 17 B2) and 26 HU (25 B1 world stories plus their
  source, a1-unit-01, the one false positive per set). **Checker fixes:**
  `unmet-word` counted *me ducho*, *nos acostamos*, *acostarme* as unmet
  (the lexicon reads *duchar*/*acostar*, or only the adjective *ducho*,
  while the list gives *ducharse*): a verb form now counts as met through
  its *-se* lemma where a reflexive pronoun stands before it or fills the
  blank before it, and only when every verb reading's *-se* form is met
  (*siento*/*te sientes* stay flagged: *sentarse* says nothing about
  *sentir(se)*); es-es A1 264 → 237, A2 850 → 820, es-latam 458 → 426,
  846 → 811, 0 new; a first, item-wide version also cleared *Lo siento*
  and *dormir* and was tightened before committing. `vocab-unused` stems
  *lavarse* as *lavar* (17 fewer in es-es, all reflexive verbs used in
  their lessons).
- **Open, the user's:** see ROADMAP 153 (Spanish pass).

### 2026-10-21: Spanish A1 units 13–18, three units per reader

- **Cost:** 346k (reader A, units 13–15) + 291k (reader B, 16–18), ~106k
  a unit, ×1.03 of units 6–11 (~103k), with about the same fixes a unit
  (~44). Reader A's higher cost matches its extra work: four new
  exercises for the new skill, ten checklist rewrites in Unit 14. Neither
  went above ~140k a unit. **Keep three per reader** for units 19–24.
- **Filter:** 189 of 262 fixes went to review (Spanish text); I changed 2
  (a hint printing the answer in English; an -ir endings tip that must
  name *vosotros* in es-es only) and dropped one fix of my own
  (*afuera* → *fuera*: the word is taught in a1-weather-04, so it is a
  course-variant decision, not a story fix). None for Spanish grammar.
  Fewer filter changes than 6–11 (16): the template's MC rule and
  character-fact rule held (0 schema rejections, 0 wrong character
  facts).
- **What only the reviewer found:** the mirror copied *salón* into four
  es-latam items through `set` fixes (the third time a Spain word reached
  es-latam this way after *coche* in 6–11); one es-latam story option
  *Zumo de naranja* (a1-14, pre-existing).
- **Changes:** (1) `mirror_fixes.py` converts mirrored `set` values and
  new texts to the target course's words with `course_variants.convert`
  and lists what it changed (seen twice, scripted; on this batch's list it
  converted exactly the four *salón* items and nothing else). (2) New
  suspect `reading-generic` (reading questions about "the character" or
  the text type; five units of this batch; 13 hits on the pre-fix
  content, all real, 0 elsewhere). (3) Rulebook § 6c: this batch's
  defects, and the new skill's tagging rule for later readers.
- **Not scripted (once each or not mechanical):** usted/subjunctive forms
  as wrong imperative options (Unit 14 only); infinitive recipe options;
  *hay que* before its screen (the `taught-later` check works from tags,
  and these wrong options carried no `distractor_skills`).

### 2026-10-21: Spanish A1 units 19–24

- **Cost:** 395k (reader A, units 19–21) + 332k (reader B, 22–24), ~121k
  a unit (×1.14 of 13–18). Reader A reached ~132k a unit: Unit 19 started
  with 15 errors and 69 suspects and Unit 21 with 9 / 33, the heaviest
  baselines so far. Still under the ~140k limit: **keep three per reader**
  for the last batch (25–26, one reader).
- **Filter:** 226 of 273 to review; I changed 5: two *sé* items moved to
  `present-irregular-yo` (kept on `saber-infinitivo`, the user's scope is
  the -go forms), a story rewrite that gave Carlos an appointment later
  that day but the doctor's medicine already, a wrong option (*conozco un
  profesor*) that can pass because the personal *a* is optional before an
  indefinite person, "favor" → "favour". Added es-latam twins: the *jugo*
  variant fix, *pedir* in an es-latam list, *clínica* (in no list).
- **Scripted:** `infinitive-reply` (seen in units 14, 20, 23): 26 hits on
  the pre-fix A1 content after tightening (a first version also flagged
  *Mi hermana trabajar…* and "Which means …" items, where the infinitive
  is plainly wrong, and lowercase form drills); it then found 2 more real
  ones in frozen units 18 and 20 (fixed, refrozen) and 3 in Unit 26 (next
  batch); A2 2, B1–B2 0. A first version crashed check-content (a helper
  named `words` shadowed a later local), which made two test runs report
  0 hits: read a check's output before trusting a zero.
- **Open, the user's:** `querer-poder` is taught_in a1-08-03, whose screen
  teaches only *querer*; *poder* is first explained in a1-abilities-01
  (Unit 24), and the readers treated earlier *poder* as before its screen.
  Either the Unit 10 screen gets *poder* (unfreeze Unit 10) or the skill
  is split; a registry decision.
- **Not scripted:** unmet Spanish metalanguage in MC question stems
  (`unmet-word` reads options, sentences and prompts, not MC questions);
  reader A found five. Extending `unmet-words.js` to question stems is a
  checker change across all courses: queued.

### 2026-10-21: Spanish A1 units 25–26 and the level checklist (A1 26/26)

- **Cost:** one reader for the last two units, 244k by its resumed notice
  (it stopped at a Sonnet session limit with three of its four files
  written; "finish each unit's files first" again saved the work, and a
  SendMessage after the reset finished it).
- **Filter:** 59 of 84 to review; changed 3 (a wrong option that passes
  colloquially, two `variant` marks the mirror now handles) and fixed a
  contradiction across stories the reader flagged: a1-17 sent Meg south
  with her sisters while a1-19/a1-20 put her on the mountain train with
  Carlos. Reading stories in sequence, not one per unit, is what catches
  this: the last unit of a level should read the level's stories in order.
- **A gate the content checks don't cover:** the push failed on
  `tests/drills/test-scenario-learner-path.js`: a conversation scenario
  required the lemma *ticket*, which existed only because an A1
  vocabulary list had the English word as a Spanish lemma (now *billete*
  / *boleto*). Run the test suite (or push) before calling a batch done,
  not only check-content and validate.
- **Level checklist:** summary in `imports/review/es-a1-level-check/`.

### 2026-10-21: Spanish A2 units 1–6 (first A2 batch)

- **Cost:** 347k (reader A, units 1–3) + 313k (reader B, 4–6), ~110k a
  unit (×0.91 of A1 19–24), ~44 fixes a unit. The early A2 units start
  lighter (3.7 errors / 24 suspects a unit). **Keep three per reader.**
- **Filter:** 186 of 263 to review, none changed: the template's rules
  (character facts, MC meaning, one fault) held for the third batch
  running. The reviewer's work was elsewhere: a doubtful item the reader
  left unfixed (*he lavado las manos* in ~40 lines of Unit 4, made
  reflexive by script), one item my own change made a copy of another
  (`unit-copy`: run check-content after every scripted edit), es-latam
  items with their own text.
- **Changes made this batch:** (1) `batch_setup.py` replaces the setup I
  wrote by hand each batch (sheets, baselines, cmp list, two prompts):
  measure on the next batch whether it cuts the reviewer's setup tokens.
  (2) `latam_challenges.py` replaces the inline es-latam challenge
  conversion. (3) `mirror_fixes.py` refuses a `set` fix where es-latam's
  committed value already differs (it would have put *vosotros* questions
  into three es-latam *ustedes* items; caught on the A1 stem list, 3 of
  3). (4) `unmet-word` reads Spanish MC question stems (the A1 open
  item): 67 new hits in frozen A1, all real (Spanish metalanguage such as
  *¿Cuál es correcta?*, *gerundio*, reading questions with *hace* before
  Unit 14); A2 +103. A first version read every stem sentence and flagged
  English words (*fits*, *sentence*) and ~200 *¿Cómo se dice / Qué
  significa?* formulas: tightened to Spanish questions (¿…?) and the two
  formulas left out.
- **Scripted (seen twice or more in this batch), tested on the pre-fix
  content:** `checklist-you` (units 2, 3, 4: all 7 pre-fix lines; 3 more
  in A2 units 8, 12, 16 and 6 in B1; first versions also flagged "using
  what you know" and HU "where I am, where you are": tightened, 0 false
  positives now); `perfecto-marker` (units 1, 2, 6): weak, it catches the
  story line *ha comprado el día anterior* and nothing in the current
  content, because the Unit 6 lines (*He viajado más que el año pasado*)
  compare with the marker, which I let pass, and *por la mañana* is not a
  finished-past marker. A first version named `texts` crashed every
  exercise check (the shadowing trap of units 19–24): read a new check's
  output, never only its count. `unmet-words.js`: a regular participle
  after *haber* counts through its verb (*nos hemos mojado*: the lexicon
  reads *mojado* as the adjective; 5 A2 and 11 B1 false hits gone, none
  hidden).
- **Not scripted:** reading questions that ask about another story (Unit
  5, five items; no script can tell), the same table on every screen
  (Units 4–6; a reader's call whether the screen still teaches).
- **Open, the user's:** Unit 3 has no grammar of its own; the MC
  formulas left out of `unmet-word`; *ustedes* among friends in es-es
  dialogues (ROADMAP 153).

### 2026-10-21: Spanish A2 units 7–12

- **Cost:** 351k (A) + 382k (B), ~122k a unit (×1.11 of units 1–6),
  with ~58 fixes a unit (×1.32): the per-fix cost fell. Reader B hit a
  Sonnet session limit after writing Units 10–11's files ("finish each
  unit's files first" saved them again) and was resumed after the reset;
  its figure comes from the resumed notice. Under ~140k a unit: **keep
  three per reader.**
- **`batch_setup.py`, first use:** the setup took one command and a
  focus file (the prompt, sheets, baselines and walk line came out
  right); before, it took a dozen tool calls a batch. Keep.
- **Filter:** 245 of 347 to review, 7 changed (one character fact, two
  story lines, one reply in the wrong person, three wordings); and one
  defect the reader repeated in its own fixes: *¿Cuánto tiempo* + present
  (16 lines in Unit 7). Readers copy a unit's own pattern when writing
  new items, so a pattern wrong across a unit is the reviewer's to catch.
- **es-latam:** the mirror left 13 fixes; 6 were story-question
  explanations that es-latam words differently (old, often quoting text
  that the fixes removed, *hubo un festival*). Seen in A1 6–11 too:
  **scripted** as `sync_story_questions.py` (copies es-es questions in
  es-latam words after the batch; it refuses *vosotros* forms).
- **Scripted (seen in three batches):** `table-repeat` (suspect: one
  table on 3+ screens of a unit): on the pre-batch content it lists all
  of Units 4–10 and 12 (30 screens), where readers had rewritten the
  tables in 7–10 and 12 but left 4–6, which were reopened and fixed; 0
  hits in later A2 units, B1 or HU. `unmet-words.js`: shortened
  adjectives (*buen*, *gran*) count through their full form.
- **Seen once, not scripted:** `merge_fixes.py` refusing a reader's
  es-es/es-latam pair on one item (rule written into the rulebook § 6c
  instead).
- **Open, the user's:** *¿Te gustaría…?* removed from the invitations
  unit (ROADMAP 153).

### 2026-10-21: Spanish A2 units 13–18, and the user's decisions

- **Cost:** ~118k a unit, flat against 7–12; neither reader hit a limit.
  **Keep three per reader.**
- **Decisions (user, 2026-10-21):** Unit 3 recast around time words (a
  Sonnet writer in a third slot after the readers; reviewed separately);
  es-es uses *vosotros* where it is natural (friends in the plural; formal
  speakers keep *ustedes*): 50 A2 items in Units 1–12, 4 in A1 and 17 in
  this batch converted by a script with a keep-list I read, the Unit 11
  preterite tables given their es-es *vosotros* rows, and the reader
  template now says it; *¿Cómo se dice / Qué significa?* stay in Spanish.
- **Challenges are walked now** (user asked why they weren't checked):
  `walk_lessons.js` types each lesson's hand-written target into the
  challenge's "Or type your response", requires the app's grader to
  accept it, and fails a lesson with no entry (generated placeholder) or
  a different challenge on screen. The skip on speaking steps no longer
  snoozes later mic steps (the snooze had hidden every challenge after
  the first speaking step). First runs: A1 156/156 and A2 1–12 72/72 per
  course, then 36/36 per batch; a Unit 13 lesson without an entry failed
  as it should before its challenges were added.
- **Readers' *vosotros* work:** reader B did none despite the focus
  note; a script plus a read keep-list was cheaper than prompting again.
  The template now carries the rule for 19–33.
- **Seen once:** a reader marked *salón* fixes `variant: es-es`, which
  made the mirror skip what it would have converted (*sala*). Noted.
- **Open, the user's:** *mientras* with the preterite in Unit 13
  (ROADMAP 153).

### 2026-10-21: Spanish A2 units 19–24

- **Limits and restarts:** both readers hit the Sonnet session limit after
  two units; "finish each unit's files first" kept their work, and both
  resumed after the reset. A container restart then lost reader B's
  completion notice (so its tokens), but not its files or its reply,
  which were read back from the subagent transcript on disk. Cost per
  unit is uncertain for this batch.
- **Story-line questions went to the user** before applying (Budapest
  move, Carlos's childhood): both readers had flagged contradictions they
  couldn't settle, and fixing them one way inside a frozen sequence of
  stories would have been guessing. Answers are in the rulebook § 6c.
- **Scripted:** `check_fixes.py` rebuilds the word index when the list
  adds vocabulary (third sighting of a fix rejected for a word another fix
  had just listed); `unmet-words.js` lemmatises enclitic commands (3 false
  hits in A2, none hidden). `--warnings` again caught a retag that left a
  vocabulary skill at 5: keep the diff in every batch.
- **Not scripted:** orphan error-correction items in Unit 21–22 files that
  no lesson references (*comiba*, *vivíban*): harmless, accepted; a check
  for exercises no lesson uses is a candidate if it shows up again.

### 2026-10-21: Spanish A2 units 25–30

- **Cost:** ~145k a unit, over the ~140k line set in the A1 review, with
  ~75 fixes a unit (the late A2 units were bulk-generated with B1 forms
  and invented scenarios). Per fix the cost fell again. The last batch
  (31–33) goes as two units for one reader and one for the other.
- **Story facts in the focus note worked:** the five contradictions named
  up front (Carlos's exam, scholarship, Meg's work trip, "seis meses",
  Madrid) were all fixed by the readers in the story, its questions and
  the items, with nothing for the reviewer to change. Writing the story
  line into the prompt before the read is cheaper than fixing it after.
- **Course-wide character fix by script:** Daniela speaking in person
  after leaving (a2-20), flagged by both readers: one script moved her
  lines to Ana (with Meg) or Kaylee (otherwise) in Units 21–30 and their
  challenges, both courses, and four frozen units were refrozen with
  `refreeze_changed.py`, which now drops accepted findings that are gone.
- **Scripted:** `vocab-unused` reads stem changes and irregular stems
  (readers flagged the false positive in units 25 and 27).

### 2026-10-22: Spanish A2 units 31–33 (last A2 batch, the finale)

- **Cost:** not measurable this time. Both readers hit a Sonnet session
  limit before writing any file and were resumed after the reset; only
  the resumed runs' usage was reported (233k for 31–32, 182k for 33).
  "Write each unit's files before the next" did not help here, because the
  limit came during the first unit. Resuming by message worked again.
- **The finale in the focus note worked:** the readers rewrote the three
  stories to the Madrid → Valencia → farewell → Budapest line, with
  separate es-es and es-latam endings, and moved items and challenges to
  "visitors in Spain". The reviewer changed only the story logic (why Meg
  is in Carlos's office and has his keys).
- **Reader misreading of a rule:** one reader removed seven
  `distractor_skills` entries because the options "don't fit the
  sentence", though they are real forms (*llueve*, *llovido*). The rulebook
  § 6 and the template now say "well-formed" means the form, not the
  sentence. Three builder fixes carried an `answer` key; the template now
  names the builder fields.
- **Checker blind spot (seen once; not scripted yet):** `unmet-words.js`
  skipped the es-es options of a2.indefinidosnegacion.03.ex07 (*disponibles*,
  *cancelado*, both B1) as English, while es-latam, with *boletos* in place
  of *entradas*, flagged them. The `isEnglish` heuristic for option sets
  ("most options look English") can hide a whole Spanish option set. If it
  recurs, make option sets English only when the item's `question` asks
  for an English meaning.
- **Stories read in order (A1 lesson):** all 33 A2 stories read in
  sequence at the end. No contradictions left. Two weak points for the
  user: no story shows Carlos and Meg leaving Hanoi (Unit 31 opens in
  Madrid "de camino"), and the grandmother in Madrid (father's mother) and
  the grandmother of the Hungarian childhood stories are never told apart.

### 2026-10-22: HU B1 pilot (Units 1 and 2)

- **Cost:** 257k for the language unit and 326k for the history unit, at
  one unit per reader, against ~140k a unit in A2 at two or three per
  reader. Part of it is per-reader overhead (rulebook, sheet, tools) that
  a single unit doesn't share; most of the history unit's is the 256
  unmet-word hits it started with (`check-content` doesn't run
  `unmet-word` from B1: `UNMET_WORD` is A1–A2), which the reader rewrote
  one by one, and the facts list.
- **The mechanical pre-pass is dropped.** 24 of its 25 fixes passed
  `check_fixes`, but the readers then rewrote most of them: absurd wrong
  options (*az egész ország egyetlen hegycsúcs*), two faults, a true wrong
  option, words beyond the level. Evening out lengths without reading the
  item moves the work rather than saving it. Readers fix length give-aways
  and tells in the read, as in A2. `dump_flagged.py` and the fixer
  template stay for a batch of purely mechanical items.
- **Facts block worked:** the reader listed 30 claims and marked the
  uncertain ones; the web check confirmed Romania's Schengen land borders
  (1 Jan 2025) and that the simplified (ethnic-Hungarian) naturalisation
  has no constitutional exam, and found one error the reader had passed:
  *vármegye* has been the official name since 1 Jan 2023, not a
  "traditional" one. Hedged as tradition: the four rivers, the three
  mountains, the bent cross, the double cross's link to St Stephen.
- **B1 findings for the rulebook § 6b:** later-B1 forms used early
  (present participles *-ó/-ő* Unit 11, past participles Unit 3, verbal
  nouns *-ás/-és* Unit 31, *-va/-ve* Unit 57, *ahol* Unit 10, *míg*
  Unit 4, past conditional Unit 39, *hogy* + subjunctive Unit 5); A1–A2
  cases presented as new on B1 screens (*-ból*, *-val*, *-ra*,
  postpositions); the generated challenge screens of the citizenship
  lessons are broken (replaced by the hand-written ones).
- **Decision for the user:** whether B1 history items keep their
  vocabulary (words added to the lesson lists) or are rewritten to met
  words, as the pilot reader did. It decides most of the history units'
  cost.

### 2026-10-22: HU B1 units 3–6

- **Cost:** ~272k a unit at two per reader, the same as the one-unit
  pilot. B1 cost follows the defects (~86 fixes a unit against ~50 in
  A2: later-B1 forms everywhere, absurd wrong options, placeholder
  questions, invented facts), so batch size barely matters. All of B1 at
  this rate is ~20M reader tokens.
- **Change:** the template now forbids testing fixes in scratch copies
  (both readers did it, 111 and 118 tool calls, and the pilot reader of
  Unit 2 too); the reviewer's `check_fixes` already does it. Track order
  changes as the user decided: core units next, three per reader.
- **Facts:** the readers flagged ~95 claims as "check" in two units;
  most are now hedged as tradition in the text (Verecke, the blood oath,
  Álmos and Árpád). Verified on the web: August 20 is the official state
  holiday (Alaptörvény: three national holidays), the 907 battle is real
  but its site uncertain (*pozsonyi csata* kept as the standard name).
  Changed by Claude: the Árpád dynasty "nearly 400 years" → *1301-ig*.

### 2026-10-22: HU B1 core units 7–17 (odd)

- **Cost:** not measurable; both readers hit a Sonnet session limit and
  only their resumed runs reported usage. Fix counts fell to ~64 a unit
  (core units have fewer defects than citizenship units: no invented
  facts, no placeholder questions).
- **Tooling bug found by the batch:** 164 HU B1 files lacked a final
  newline, so `apply_replacements.py` refused every `set` fix on them as
  "doesn't round-trip". Fixed in the files and in the script (a missing
  final newline now counts as round-tripping), so other levels won't hit
  it.
- **Reviewer error, corrected:** I first reversed a reader fix that made
  Fábián's last line in *Bede Anna* informal, reading the scene as
  formal; the adapted story has him use *te* throughout (*a helyedben*,
  the form the lesson teaches). Read the whole scene before overruling a
  register fix.
- **For the user:** `egyreszt-masreszt` has `taught_in` a2-21-b-gr, which
  teaches only *nem csak … hanem … is*; *egyrészt … másrészt* is first
  taught on b1-04-03-a-gr. The skill list is frozen.

### 2026-10-23: HU B1 core units 19–29

- **Cost:** 581k (Units 19, 21, 23) and 430k (25, 27, 29). Reader A's
  units were trade and contract Hungarian far above B1 and got ~155
  fixes each; Units 25–29 are half-size lessons (one exercise group of 8
  per lesson, 48 exercises a unit against ~93), which is why B was cheaper.
- **Structural gap found:** from B1 Unit 25 on, 51 lesson groups (core
  and citizenship) have no "Can you do this?" checklist and no review
  step, so a challenge can't copy its `canDo`. `add_missing_checklists.py`
  builds them from the lesson's goal lines and, for consolidations, which
  have no goals, from the reader's challenge draft (`--from-challenges`).
  Run it on each later batch's units before `add_challenges.py`.
- **Checker false positive, seen 5 times:** `option-language` reads an
  English option with an accented name (*Óbuda*, *Pósalaky*, *café*) as
  Hungarian. **Scripted the same day:** `looks_target` ignores
  capitalised words and English loanwords in the accent test, and counts
  function words only when they are a quarter of the option (*me* in
  "María sent me a message", quoted *nem*/*meg* in an English
  explanation). Course-wide `option-language` hits: es-es B1 24 → 0,
  hu B1 1 → 0, es-latam B1 1 → 0, hu B2 17 → 12; the synthetic true
  mixes are still caught.
- **Template:** reader B wrote its own lemma-lookup tool in the
  scratchpad; the template now says to use `unmet-words.js` only.

### 2026-10-27: HU B1 core units 31–41

- **Cost:** not measurable: both readers hit the weekly Sonnet limit with
  Units 35 and 41 half reported; reader B had in fact finished Unit 41,
  reader A wrote Unit 35's challenges and report on resume (64 s).
- **Recaps name the wrong unit.** Readers rewrite "new" screens as "You
  know *X* from Unit N"; in Unit 35, 2 of about 10 named a unit where *X*
  isn't (*noha* "Unit 24", *megengedett* "B1 Unit 3"; 2 more gave
  unchecked numbers), and one in Unit 39 said the past conditional
  was met in Unit 26 when Unit 39 teaches it. **Scripted:**
  `scripts/check_unit_refs.py <course> <level> [units]` finds the first
  unit whose files contain each recapped word; on all of B1 it found 5
  more, in Units 19, 27, 29, 31 and 35, where the recap copies a skill
  title that names a word its A1/A2 screen never shows (`kell-infinitive`
  promises *muszáj*, `mert-because` *ezért*, `kellene` *ajánlott*,
  `ha-clause` *amennyiben*, `concessive-annak-ellenere` *habár*). Fixed
  on the B1 screens; the skill titles are frozen, **for the user**. One
  known false positive: a recap of a form (*adjuk hozzá*, imperative).
  Run it after applying each batch (pipeline step 5).
- **Readers emptied screens to meet the unmet-word rule:** Unit 41's
  argument phrases were swapped for A2 words (*Biztos, hogy*, *Aztán*,
  *Mivel*). Rejected; the template now says a screen's own new phrases
  stay.
- **My own error, scripted:** rerunning `check_fixes.py` on a list I had
  already reviewed overwrote the edited review file and brought back a
  story fix I had dropped. It now refuses to replace a review list that
  differs unless `--overwrite` is given.
- **Retag left a skill under 6:** the reader rightly moved *ökológiai
  lábnyom* off `noun-compounds` (it is not a compound), leaving 5; the
  `--warnings` diff caught it and one compound item replaced it.
